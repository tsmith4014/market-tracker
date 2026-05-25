#!/usr/bin/env python3
from __future__ import annotations

import csv
import json
import logging
import os
import time
from dataclasses import dataclass
from datetime import datetime
from io import StringIO
from pathlib import Path
from typing import Dict, Iterable, List, Optional, Tuple

import numpy as np
import pandas as pd
import pytz
import requests
try:
    import yfinance as yf
except ImportError:  # pragma: no cover
    yf = None

from symbol_manager import SymbolInfo, SymbolManager

CT = pytz.timezone("America/Chicago")
OUT_CSV = os.getenv("OUTPUT_PATH", "/data/market_tracker.csv")
CONFIG_PATH = os.getenv("CONFIG_PATH", "/app/config.json")
DAYS_CRYPTO = int(os.getenv("DAYS_CRYPTO", "730"))
DAYS_EQUITY = os.getenv("DAYS_EQUITY", "800d")
OUTPUT_MODE = os.getenv("OUTPUT_MODE", "historical").strip().lower()
WRITE_MODE = os.getenv("WRITE_MODE", "replace" if OUTPUT_MODE == "historical" else "append").strip().lower()
EXPORT_SERIES = os.getenv("EXPORT_SERIES", "false").lower() == "true"
SERIES_DIR = os.getenv("SERIES_DIR", "/data")
HTTP_TIMEOUT_SECONDS = int(os.getenv("HTTP_TIMEOUT_SECONDS", "30"))
REQUEST_DELAY_SECONDS = float(os.getenv("REQUEST_DELAY_SECONDS", "0.5"))

logging.basicConfig(level=os.getenv("LOG_LEVEL", "INFO").upper(), format="%(asctime)s %(levelname)s %(message)s")
LOGGER = logging.getLogger("market_tracker")
SYMBOL_MANAGER = SymbolManager()
TRACK_CRYPTO = [x.strip() for x in os.getenv("TRACK_CRYPTO", "major,defi").split(",") if x.strip()]
TRACK_STOCKS = [x.strip() for x in os.getenv("TRACK_STOCKS", "tech_mega_caps,semiconductors").split(",") if x.strip()]
TRACK_INDICES = os.getenv("TRACK_INDICES", "true").lower() == "true"
TRACK_SYMBOLS = [x.strip().upper() for x in os.getenv("TRACK_SYMBOLS", "").split(",") if x.strip()]

SCHEMA_COLUMNS = [
    "timestamp_ct", "symbol", "data_source", "date", "open", "high", "low", "close", "volume",
    "ema20", "ema50", "ema100", "ema200", "sma20", "sma50", "sma100", "sma200",
    "rsi14", "macd", "macd_signal", "macd_hist", "atr14", "adx14", "plus_di14", "minus_di14",
    "bb_mid20", "bb_upper20", "bb_lower20", "bb_width", "pivot", "r1", "s1", "r2", "s2", "r3", "s3",
    "fib_long_low", "fib_long_high", "fib_long_23.6%", "fib_long_38.2%", "fib_long_50.0%", "fib_long_61.8%", "fib_long_78.6%",
    "fib_short_low", "fib_short_high", "fib_short_23.6%", "fib_short_38.2%", "fib_short_50.0%", "fib_short_61.8%", "fib_short_78.6%",
    "trend_s", "momentum_s", "strength_s", "vol_s", "fib_s", "pivot_s", "composite_score", "signal",
]

@dataclass(frozen=True)
class MarketData:
    df: pd.DataFrame
    source: str


def parse_days(value: str | int) -> int:
    if isinstance(value, int):
        return value
    text = str(value).strip().lower()
    return int(text[:-1] if text.endswith("d") else text)


def dedupe(items: Iterable[str]) -> List[str]:
    seen, result = set(), []
    for item in items:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result


def get_tracking_symbols() -> List[str]:
    if TRACK_SYMBOLS:
        unknown = [s for s in TRACK_SYMBOLS if SYMBOL_MANAGER.get_symbol_info(s) is None]
        if unknown:
            raise ValueError(f"Unknown TRACK_SYMBOLS: {', '.join(unknown)}")
        return dedupe(TRACK_SYMBOLS)
    symbols: List[str] = []
    for category in TRACK_CRYPTO:
        symbols.extend(SYMBOL_MANAGER.get_by_category(category))
    for category in TRACK_STOCKS:
        symbols.extend(SYMBOL_MANAGER.get_by_category(category))
    if TRACK_INDICES:
        symbols.extend(SYMBOL_MANAGER.get_all_indices())
    return dedupe(symbols)


def load_config(path: str) -> dict:
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    return {
        "defaults": {
            "weights": {"trend": 0.50, "momentum": 0.20, "strength": 0.15, "vol": 0.05, "fib": 0.05, "pivot": 0.05},
            "thresholds": {"long": 30, "short": -30},
            "lookbacks": {"fib_long": 180, "fib_short": 30},
            "guards": {"min_adx_for_signal": 18, "max_atr_pct": 12.0, "require_close_above_ema50_for_long": False, "require_close_below_ema50_for_short": False},
            "fees": {"bps_per_side": 1.0, "slippage_bps_per_side": 1.0},
        },
        "overrides": {},
    }


def apply_overrides(symbol: str, cfg: dict) -> dict:
    d = cfg.get("defaults", {})
    o = cfg.get("overrides", {}).get(symbol, {})
    merged = {
        "weights": {**d.get("weights", {}), **o.get("weights", {})},
        "thresholds": {**d.get("thresholds", {}), **o.get("thresholds", {})},
        "lookbacks": {**d.get("lookbacks", {}), **o.get("lookbacks", {})},
        "guards": {**d.get("guards", {}), **o.get("guards", {})},
        "fees": {**d.get("fees", {}), **o.get("fees", {})},
    }
    if merged["thresholds"]["long"] <= merged["thresholds"]["short"]:
        raise ValueError(f"Invalid thresholds for {symbol}")
    return merged


def ema(s: pd.Series, span: int) -> pd.Series: return s.ewm(span=span, adjust=False).mean()
def sma(s: pd.Series, window: int) -> pd.Series: return s.rolling(window, min_periods=window).mean()


def rsi(s: pd.Series, period: int = 14) -> pd.Series:
    d = s.diff(); up = d.clip(lower=0.0); dn = -d.clip(upper=0.0)
    up_mean = up.rolling(period, min_periods=period).mean()
    dn_mean = dn.rolling(period, min_periods=period).mean()
    # Handle edge cases explicitly:
    #   no losses (pure uptrend) -> RSI = 100
    #   no gains (pure downtrend) -> RSI = 0
    #   both zero (flat) -> RSI = 50
    rs = up_mean / dn_mean.replace(0, np.nan)
    out = 100.0 - (100.0 / (1.0 + rs))
    pure_up = (dn_mean == 0) & (up_mean > 0)
    pure_down = (up_mean == 0) & (dn_mean > 0)
    pure_flat = (up_mean == 0) & (dn_mean == 0)
    out = out.where(~pure_up, 100.0)
    out = out.where(~pure_down, 0.0)
    out = out.where(~pure_flat, 50.0)
    return out


def macd(s: pd.Series, fast: int = 12, slow: int = 26, signal: int = 9):
    line = ema(s, fast) - ema(s, slow); sig = ema(line, signal)
    return line, sig, line - sig


def true_range(h: pd.Series, l: pd.Series, c: pd.Series) -> pd.Series:
    pc = c.shift(1)
    return pd.concat([(h - l), (h - pc).abs(), (l - pc).abs()], axis=1).max(axis=1)


def atr(h: pd.Series, l: pd.Series, c: pd.Series, period: int = 14) -> pd.Series:
    return true_range(h, l, c).rolling(period, min_periods=period).mean()


def adx(h: pd.Series, l: pd.Series, c: pd.Series, period: int = 14):
    up = h.diff(); dn = -l.diff()
    plus_dm = np.where((up > dn) & (up > 0), up, 0.0)
    minus_dm = np.where((dn > up) & (dn > 0), dn, 0.0)
    atr_n = true_range(h, l, c).rolling(period, min_periods=period).mean().replace(0, np.nan)
    plus_di = 100 * (pd.Series(plus_dm, index=h.index).rolling(period, min_periods=period).sum() / atr_n)
    minus_di = 100 * (pd.Series(minus_dm, index=h.index).rolling(period, min_periods=period).sum() / atr_n)
    dx = (plus_di.subtract(minus_di).abs() / (plus_di + minus_di).replace(0, np.nan)) * 100
    return dx.rolling(period, min_periods=period).mean(), plus_di, minus_di


def bollinger(s: pd.Series, window: int = 20, nstd: float = 2.0):
    mid = s.rolling(window, min_periods=window).mean(); std = s.rolling(window, min_periods=window).std()
    up = mid + nstd * std; dn = mid - nstd * std
    return mid, up, dn, (up - dn) / mid.replace(0, np.nan)


def pivots(df: pd.DataFrame):
    prev = df.shift(1)
    p = (prev["High"] + prev["Low"] + prev["Close"]) / 3.0
    r1 = 2 * p - prev["Low"]; s1 = 2 * p - prev["High"]
    r2 = p + (prev["High"] - prev["Low"]); s2 = p - (prev["High"] - prev["Low"])
    r3 = prev["High"] + 2 * (p - prev["Low"]); s3 = prev["Low"] - 2 * (prev["High"] - p)
    return p, r1, s1, r2, s2, r3, s3


def detect_swing(df: pd.DataFrame, lookback: int) -> Tuple[float, float]:
    window = df.tail(lookback)
    highs, lows = window["High"], window["Low"]
    best_low = float(lows.iloc[0]); best_high = float(highs.iloc[0]); best_move = 0.0
    low_so_far = best_low; high_so_far = best_high
    for _, row in window.iterrows():
        high = float(row["High"]); low = float(row["Low"])
        up_move = (high - low_so_far) / max(low_so_far, 1e-9)
        if up_move > best_move:
            best_move, best_low, best_high = up_move, low_so_far, high
        down_move = (high_so_far - low) / max(high_so_far, 1e-9)
        if down_move > best_move:
            best_move, best_low, best_high = down_move, low, high_so_far
        low_so_far = min(low_so_far, low); high_so_far = max(high_so_far, high)
    lo, hi = min(best_low, best_high), max(best_low, best_high)
    return (float(lows.min()), float(highs.max())) if hi <= lo else (lo, hi)


def fib_levels(low: float, high: float) -> Dict[str, float]:
    if not np.isfinite(low) or not np.isfinite(high) or high <= low:
        return {k: np.nan for k in ["23.6%", "38.2%", "50.0%", "61.8%", "78.6%"]}
    return {f"{level * 100:.1f}%": high - (high - low) * level for level in [0.236, 0.382, 0.5, 0.618, 0.786]}


def prepare_ohlcv(df: pd.DataFrame) -> pd.DataFrame:
    required = ["Date", "Open", "High", "Low", "Close", "Volume"]
    missing = [c for c in required if c not in df.columns]
    if missing:
        raise ValueError(f"OHLCV data missing required columns: {missing}")
    out = df[required].copy()
    out["Date"] = pd.to_datetime(out["Date"], utc=False).dt.tz_localize(None)
    for c in ["Open", "High", "Low", "Close", "Volume"]:
        out[c] = pd.to_numeric(out[c], errors="coerce")
    out = out.dropna(subset=["Date", "Open", "High", "Low", "Close"])
    out = out[out["Close"] > 0]
    return out.sort_values("Date").drop_duplicates(subset=["Date"], keep="last").reset_index(drop=True)


def validate_data_integrity(df: pd.DataFrame, symbol: str, min_bars: int = 220) -> Tuple[bool, str]:
    if len(df) < min_bars: return False, f"insufficient_bars ({len(df)} < {min_bars})"
    if not df["Date"].is_monotonic_increasing: return False, "non_monotonic_dates"
    if df["Date"].duplicated().any(): return False, "duplicate_dates"
    if not (df["Close"] > 0).all(): return False, "invalid_prices"
    if df["Close"].isna().sum() > len(df) * 0.05: return False, "too_many_nans"
    if (df["High"] < df[["Open", "Close", "Low"]].max(axis=1)).any(): return False, "invalid_high_values"
    if (df["Low"] > df[["Open", "Close", "High"]].min(axis=1)).any(): return False, "invalid_low_values"
    return True, "ok"


def fetch_stooq_data(symbol: str, days: int) -> MarketData:
    stooq_symbol = SYMBOL_MANAGER.get_api_mapping(symbol, "stooq")
    if not stooq_symbol: raise ValueError(f"No Stooq mapping configured for {symbol}")
    r = requests.get(f"https://stooq.com/q/d/l/?s={stooq_symbol}&i=d", timeout=HTTP_TIMEOUT_SECONDS); r.raise_for_status()
    df = pd.read_csv(StringIO(r.text)); df["Date"] = pd.to_datetime(df["Date"])
    df = df[df["Date"] >= datetime.utcnow() - pd.Timedelta(days=days)]
    return MarketData(prepare_ohlcv(df), "Stooq API")


def fetch_yfinance_data(symbol: str, days: int) -> MarketData:
    if yf is None: raise ValueError("yfinance is not installed")
    yf_symbol = SYMBOL_MANAGER.get_api_mapping(symbol, "yfinance") or symbol
    df = yf.download(yf_symbol, period=f"{days}d", interval="1d", auto_adjust=False, progress=False)
    if df.empty: raise ValueError("No data received from Yahoo Finance")
    if isinstance(df.columns, pd.MultiIndex): df.columns = [c[0] for c in df.columns]
    return MarketData(prepare_ohlcv(df.reset_index()[["Date", "Open", "High", "Low", "Close", "Volume"]]), "Yahoo Finance")


def fetch_stock_data(symbol: str, days: int) -> MarketData:
    errors = []
    for name, fn in (("Stooq", fetch_stooq_data), ("Yahoo Finance", fetch_yfinance_data)):
        try:
            LOGGER.info("Trying %s for %s", name, symbol)
            return fn(symbol, days)
        except Exception as exc:
            errors.append(f"{name}: {exc}"); LOGGER.warning("%s failed for %s: %s", name, symbol, exc)
    raise ValueError(f"No stock/index API data available for {symbol}. Attempts: {' | '.join(errors)}")


def fetch_kraken_data(symbol: str, days: int) -> MarketData:
    pair = SYMBOL_MANAGER.get_api_mapping(symbol, "kraken")
    if not pair: raise ValueError(f"No Kraken mapping configured for {symbol}")
    r = requests.get("https://api.kraken.com/0/public/OHLC", params={"pair": pair, "interval": "1440"}, timeout=HTTP_TIMEOUT_SECONDS); r.raise_for_status()
    data = r.json()
    if data.get("error"): raise ValueError(f"Kraken API error: {data['error']}")
    result = data.get("result", {}); candles = result.get(pair)
    if not candles:
        keys = [k for k in result if k != "last"]; candles = result.get(keys[0]) if keys else None
    if not candles: raise ValueError("No OHLC data received from Kraken")
    df = pd.DataFrame([{"Date": pd.to_datetime(int(c[0]), unit="s"), "Open": float(c[1]), "High": float(c[2]), "Low": float(c[3]), "Close": float(c[4]), "Volume": float(c[6])} for c in candles])
    df = df[df["Date"] >= datetime.utcnow() - pd.Timedelta(days=days)]
    return MarketData(prepare_ohlcv(df), "Kraken API")


def fetch_coinbase_data(symbol: str, days: int) -> MarketData:
    product = SYMBOL_MANAGER.get_api_mapping(symbol, "coinbase")
    if not product: raise ValueError(f"No Coinbase mapping configured for {symbol}")
    end = datetime.utcnow(); start = end - pd.Timedelta(days=days)
    r = requests.get(f"https://api.exchange.coinbase.com/products/{product}/candles", params={"start": start.isoformat(), "end": end.isoformat(), "granularity": "86400"}, timeout=HTTP_TIMEOUT_SECONDS); r.raise_for_status()
    data = r.json()
    if not data: raise ValueError("No OHLC data received from Coinbase")
    df = pd.DataFrame([{"Date": pd.to_datetime(int(c[0]), unit="s"), "Low": float(c[1]), "High": float(c[2]), "Open": float(c[3]), "Close": float(c[4]), "Volume": float(c[5])} for c in data])
    return MarketData(prepare_ohlcv(df), "Coinbase API")


def fetch_coingecko_ohlc_data(symbol: str, days: int) -> MarketData:
    coin_id = SYMBOL_MANAGER.get_api_mapping(symbol, "coingecko")
    if not coin_id: raise ValueError(f"No CoinGecko mapping configured for {symbol}")
    selected_days = next((w for w in [1, 7, 14, 30, 90, 180, 365] if days <= w), 365)
    r = requests.get(f"https://api.coingecko.com/api/v3/coins/{coin_id}/ohlc", params={"vs_currency": "usd", "days": selected_days}, timeout=HTTP_TIMEOUT_SECONDS); r.raise_for_status()
    data = r.json()
    if not data: raise ValueError("No OHLC data received from CoinGecko")
    df = pd.DataFrame([{"Date": pd.to_datetime(int(c[0]), unit="ms"), "Open": float(c[1]), "High": float(c[2]), "Low": float(c[3]), "Close": float(c[4]), "Volume": np.nan} for c in data])
    df = df[df["Date"] >= datetime.utcnow() - pd.Timedelta(days=days)]
    return MarketData(prepare_ohlcv(df), "CoinGecko OHLC API")


def fetch_coinpaprika_data(symbol: str, days: int) -> MarketData:
    coin_ids = {"SOL-USD": "sol-solana", "BTC-USD": "btc-bitcoin", "ETH-USD": "eth-ethereum", "XRP-USD": "xrp-ripple"}
    coin_id = coin_ids.get(symbol)
    if not coin_id: raise ValueError(f"No CoinPaprika mapping configured for {symbol}")
    r = requests.get(f"https://api.coinpaprika.com/v1/coins/{coin_id}/ohlcv/historical", params={"start": (datetime.utcnow() - pd.Timedelta(days=days)).strftime("%Y-%m-%d"), "end": datetime.utcnow().strftime("%Y-%m-%d")}, timeout=HTTP_TIMEOUT_SECONDS); r.raise_for_status()
    data = r.json()
    if not data: raise ValueError("No OHLC data received from CoinPaprika")
    df = pd.DataFrame([{"Date": pd.to_datetime(x["time_open"]), "Open": float(x["open"]), "High": float(x["high"]), "Low": float(x["low"]), "Close": float(x["close"]), "Volume": float(x["volume"])} for x in data])
    return MarketData(prepare_ohlcv(df), "CoinPaprika API")


def fetch_crypto_data(symbol: str, days: int) -> MarketData:
    errors = []
    for fn in [fetch_kraken_data, fetch_coinbase_data, fetch_coingecko_ohlc_data, fetch_coinpaprika_data]:
        name = fn.__name__.replace("fetch_", "").replace("_data", "").replace("_", " ").title()
        try:
            LOGGER.info("Trying %s for %s", name, symbol); time.sleep(REQUEST_DELAY_SECONDS)
            return fn(symbol, days)
        except Exception as exc:
            errors.append(f"{name}: {exc}"); LOGGER.warning("%s failed for %s: %s", name, symbol, exc)
    raise ValueError(f"No crypto API data available for {symbol}. Attempts: {' | '.join(errors)}")


def nan_to_none(x):
    if x is None or pd.isna(x): return None
    if isinstance(x, (int, float, np.integer, np.floating)):
        return float(x) if np.isfinite(x) else None
    return x


def finite_or_none(x) -> Optional[float]:
    if x is None or pd.isna(x) or not np.isfinite(x): return None
    return float(x)


def score_trend(close, ema20, ema50, ema200, slope20, slope50, slope200) -> float:
    s = 0.0
    s += 1 if close is not None and ema20 is not None and close > ema20 else -1
    s += 1 if close is not None and ema50 is not None and close > ema50 else -1
    s += 1.5 if close is not None and ema200 is not None and close > ema200 else -1.5
    s += 0.5 if slope20 > 0 else -0.5; s += 0.5 if slope50 > 0 else -0.5; s += 1.0 if slope200 > 0 else -1.0
    return max(-5.0, min(5.0, s))


def score_momentum(rsi14, macd_value, macd_signal) -> float:
    s = 0.0
    if rsi14 is not None:
        if 50 <= rsi14 <= 70: s += 1.0
        if 30 <= rsi14 < 50: s -= 0.5
        if rsi14 > 70: s += 0.5
        if rsi14 < 30: s -= 1.0
    if macd_value is not None and macd_signal is not None:
        s += 1.0 if macd_value > macd_signal else -1.0; s += 0.5 if macd_value > 0 else -0.5
    return max(-3.0, min(3.0, s))


def score_strength(adx14, plus_di, minus_di) -> float:
    if adx14 is None or plus_di is None or minus_di is None: return 0.0
    return max(-2.0, min(2.0, (1.0 if adx14 >= 25 else -0.5) + (0.5 if plus_di > minus_di else -0.5)))


def score_volatility(atr14, close, bb_width) -> float:
    s = 0.0
    if atr14 is not None and close:
        atrp = 100.0 * atr14 / close
        if atrp < 2.0: s += 0.5
        elif atrp < 5.0: s += 0.25
        elif atrp >= 8.0: s -= 0.5
    if bb_width is not None:
        if bb_width < 0.05: s += 0.25
        elif bb_width > 0.25: s -= 0.25
    return max(-1.0, min(1.0, s))


def score_fib(close, low, high) -> float:
    if any(v is None for v in [close, low, high]) or high <= low: return 0.0
    f38 = high - (high - low) * 0.382; f50 = high - (high - low) * 0.5; f62 = high - (high - low) * 0.618
    if min(f38, f62) <= close <= max(f38, f62): return 1.0
    return 0.5 if abs(close - f50) <= 0.01 * f50 else -0.25


def score_pivot(close, pivot, r1, s1) -> float:
    if pivot is None or r1 is None or s1 is None or close is None: return 0.0
    s = 0.5 if close > pivot else -0.5
    if close > r1: s += 0.25
    if close < s1: s -= 0.25
    return max(-1.0, min(1.0, s))


def latest_dict(row: pd.Series) -> Dict[str, float]:
    return {"close": row.get("Close"), "ema20": row.get("EMA20"), "ema50": row.get("EMA50"), "ema200": row.get("EMA200"), "sma20": row.get("SMA20"), "sma50": row.get("SMA50"), "sma200": row.get("SMA200"), "rsi14": row.get("RSI14"), "macd": row.get("MACD"), "macd_signal": row.get("MACD_SIGNAL"), "adx14": row.get("ADX14"), "plus_di14": row.get("+DI14"), "minus_di14": row.get("-DI14"), "atr14": row.get("ATR14"), "bb_width": row.get("BB_WIDTH"), "pivot": row.get("PIVOT"), "r1": row.get("R1"), "s1": row.get("S1"), "fib_long_low": row.get("fib_long_low"), "fib_long_high": row.get("fib_long_high")}


def composite_and_subscores(latest: Dict[str, float], weights: dict) -> Tuple[float, Dict[str, float]]:
    close = finite_or_none(latest.get("close")); ema20 = finite_or_none(latest.get("ema20")); ema50 = finite_or_none(latest.get("ema50")); ema200 = finite_or_none(latest.get("ema200"))
    sma20 = finite_or_none(latest.get("sma20")); sma50 = finite_or_none(latest.get("sma50")); sma200 = finite_or_none(latest.get("sma200"))
    subs = {
        "trend_s": score_trend(close, ema20, ema50, ema200, (ema20 or 0) - (sma20 or 0), (ema50 or 0) - (sma50 or 0), (ema200 or 0) - (sma200 or 0)),
        "momentum_s": score_momentum(finite_or_none(latest.get("rsi14")), finite_or_none(latest.get("macd")), finite_or_none(latest.get("macd_signal"))),
        "strength_s": score_strength(finite_or_none(latest.get("adx14")), finite_or_none(latest.get("plus_di14")), finite_or_none(latest.get("minus_di14"))),
        "vol_s": score_volatility(finite_or_none(latest.get("atr14")), close, finite_or_none(latest.get("bb_width"))),
        "fib_s": score_fib(close, finite_or_none(latest.get("fib_long_low")), finite_or_none(latest.get("fib_long_high"))),
        "pivot_s": score_pivot(close, finite_or_none(latest.get("pivot")), finite_or_none(latest.get("r1")), finite_or_none(latest.get("s1"))),
    }
    caps = {"trend_s": 5, "momentum_s": 3, "strength_s": 2, "vol_s": 1, "fib_s": 1, "pivot_s": 1}
    wm = {"trend_s": "trend", "momentum_s": "momentum", "strength_s": "strength", "vol_s": "vol", "fib_s": "fib", "pivot_s": "pivot"}
    valid = {k: v for k, v in subs.items() if np.isfinite(v)}; total = sum(float(weights.get(wm[k], 0)) for k in valid)
    if not valid or total <= 0: return np.nan, subs
    return sum((valid[k] / caps[k]) * (float(weights.get(wm[k], 0)) / total) for k in valid) * 100.0, subs


def enforce_guards(scfg: dict, latest: dict, raw_signal: str) -> str:
    if raw_signal == "NEUTRAL": return raw_signal
    adx14 = finite_or_none(latest.get("adx14")); atr14 = finite_or_none(latest.get("atr14")); close = finite_or_none(latest.get("close")); ema50 = finite_or_none(latest.get("ema50"))
    if adx14 is None or adx14 < float(scfg["guards"].get("min_adx_for_signal", 0)): return "NEUTRAL"
    if close and atr14 and 100.0 * atr14 / close > float(scfg["guards"].get("max_atr_pct", 999)): return "NEUTRAL"
    if scfg["guards"].get("require_close_above_ema50_for_long", False) and raw_signal == "LONG" and (close is None or ema50 is None or close <= ema50): return "NEUTRAL"
    if scfg["guards"].get("require_close_below_ema50_for_short", False) and raw_signal == "SHORT" and (close is None or ema50 is None or close >= ema50): return "NEUTRAL"
    return raw_signal


def compute_indicators(df: pd.DataFrame, fib_long_lb: int, fib_short_lb: int) -> pd.DataFrame:
    d = prepare_ohlcv(df)
    d["EMA20"] = ema(d["Close"], 20); d["EMA50"] = ema(d["Close"], 50); d["EMA100"] = ema(d["Close"], 100); d["EMA200"] = ema(d["Close"], 200)
    d["SMA20"] = sma(d["Close"], 20); d["SMA50"] = sma(d["Close"], 50); d["SMA100"] = sma(d["Close"], 100); d["SMA200"] = sma(d["Close"], 200)
    d["RSI14"] = rsi(d["Close"], 14); m, sig, hist = macd(d["Close"]); d["MACD"] = m; d["MACD_SIGNAL"] = sig; d["MACD_HIST"] = hist
    d["ATR14"] = atr(d["High"], d["Low"], d["Close"], 14); av, pdi, mdi = adx(d["High"], d["Low"], d["Close"], 14); d["ADX14"] = av; d["+DI14"] = pdi; d["-DI14"] = mdi
    bmid, bup, bdn, bw = bollinger(d["Close"], 20, 2.0); d["BB_MID20"] = bmid; d["BB_UPPER20"] = bup; d["BB_LOWER20"] = bdn; d["BB_WIDTH"] = bw
    p, r1, s1, r2, s2, r3, s3 = pivots(d); d["PIVOT"] = p; d["R1"] = r1; d["S1"] = s1; d["R2"] = r2; d["S2"] = s2; d["R3"] = r3; d["S3"] = s3
    for prefix, lb in (("fib_long", fib_long_lb), ("fib_short", fib_short_lb)):
        lows, highs, levels = [], [], []
        for idx in range(len(d)):
            if idx + 1 < lb: lo, hi, lev = np.nan, np.nan, fib_levels(np.nan, np.nan)
            else: lo, hi = detect_swing(d.iloc[:idx + 1], lb); lev = fib_levels(lo, hi)
            lows.append(lo); highs.append(hi); levels.append(lev)
        d[f"{prefix}_low"] = lows; d[f"{prefix}_high"] = highs
        for name in ["23.6%", "38.2%", "50.0%", "61.8%", "78.6%"]: d[f"{prefix}_{name}"] = [x[name] for x in levels]
    return d


def process_df(df: pd.DataFrame, symbol_cfg: dict) -> pd.DataFrame:
    fl = int(symbol_cfg["lookbacks"]["fib_long"]); fs = int(symbol_cfg["lookbacks"]["fib_short"]); out = compute_indicators(df, fl, fs)
    for c in ["trend_s", "momentum_s", "strength_s", "vol_s", "fib_s", "pivot_s", "composite_score"]: out[c] = np.nan
    out["signal"] = "NEUTRAL"; warmup = max(200, fl, fs)
    for idx, row in out.iterrows():
        if idx + 1 < warmup: continue
        ld = latest_dict(row); score, subs = composite_and_subscores(ld, symbol_cfg["weights"])
        if not np.isfinite(score): continue
        raw = "LONG" if score >= float(symbol_cfg["thresholds"]["long"]) else ("SHORT" if score <= float(symbol_cfg["thresholds"]["short"]) else "NEUTRAL")
        for k, v in subs.items(): out.loc[idx, k] = v
        out.loc[idx, "composite_score"] = score; out.loc[idx, "signal"] = enforce_guards(symbol_cfg, ld, raw)
    return out


def row_to_output(row: pd.Series, symbol: str, source: str, ts: str) -> Dict[str, object]:
    mapping = {"timestamp_ct": ts, "symbol": symbol, "data_source": source, "date": row["Date"].date().isoformat() if isinstance(row["Date"], pd.Timestamp) else str(row["Date"]), "open": row.get("Open"), "high": row.get("High"), "low": row.get("Low"), "close": row.get("Close"), "volume": row.get("Volume"), "ema20": row.get("EMA20"), "ema50": row.get("EMA50"), "ema100": row.get("EMA100"), "ema200": row.get("EMA200"), "sma20": row.get("SMA20"), "sma50": row.get("SMA50"), "sma100": row.get("SMA100"), "sma200": row.get("SMA200"), "rsi14": row.get("RSI14"), "macd": row.get("MACD"), "macd_signal": row.get("MACD_SIGNAL"), "macd_hist": row.get("MACD_HIST"), "atr14": row.get("ATR14"), "adx14": row.get("ADX14"), "plus_di14": row.get("+DI14"), "minus_di14": row.get("-DI14"), "bb_mid20": row.get("BB_MID20"), "bb_upper20": row.get("BB_UPPER20"), "bb_lower20": row.get("BB_LOWER20"), "bb_width": row.get("BB_WIDTH"), "pivot": row.get("PIVOT"), "r1": row.get("R1"), "s1": row.get("S1"), "r2": row.get("R2"), "s2": row.get("S2"), "r3": row.get("R3"), "s3": row.get("S3"), "fib_long_low": row.get("fib_long_low"), "fib_long_high": row.get("fib_long_high"), "fib_long_23.6%": row.get("fib_long_23.6%"), "fib_long_38.2%": row.get("fib_long_38.2%"), "fib_long_50.0%": row.get("fib_long_50.0%"), "fib_long_61.8%": row.get("fib_long_61.8%"), "fib_long_78.6%": row.get("fib_long_78.6%"), "fib_short_low": row.get("fib_short_low"), "fib_short_high": row.get("fib_short_high"), "fib_short_23.6%": row.get("fib_short_23.6%"), "fib_short_38.2%": row.get("fib_short_38.2%"), "fib_short_50.0%": row.get("fib_short_50.0%"), "fib_short_61.8%": row.get("fib_short_61.8%"), "fib_short_78.6%": row.get("fib_short_78.6%"), "trend_s": row.get("trend_s"), "momentum_s": row.get("momentum_s"), "strength_s": row.get("strength_s"), "vol_s": row.get("vol_s"), "fib_s": row.get("fib_s"), "pivot_s": row.get("pivot_s"), "composite_score": row.get("composite_score"), "signal": row.get("signal", "NEUTRAL")}
    return {c: nan_to_none(mapping.get(c)) for c in SCHEMA_COLUMNS}


def ensure_schema(path: str) -> None:
    p = Path(path); p.parent.mkdir(parents=True, exist_ok=True)
    if not p.exists():
        with p.open("w", newline="", encoding="utf-8") as f: csv.DictWriter(f, fieldnames=SCHEMA_COLUMNS).writeheader()


def write_rows(path: str, rows: List[Dict[str, object]], mode: str) -> None:
    p = Path(path); p.parent.mkdir(parents=True, exist_ok=True); df = pd.DataFrame(rows, columns=SCHEMA_COLUMNS)
    if mode == "append" and p.exists() and p.stat().st_size > 0:
        old = pd.read_csv(p); df = pd.concat([old, df], ignore_index=True).drop_duplicates(subset=["symbol", "date"], keep="last").sort_values(["symbol", "date"])
    elif mode != "replace":
        raise ValueError("WRITE_MODE must be 'replace' or 'append'")
    df.to_csv(p, index=False)


def select_rows_for_mode(processed: pd.DataFrame, mode: str) -> pd.DataFrame:
    scored = processed[pd.notna(processed["composite_score"])].copy()
    if mode == "historical": return scored
    if mode == "latest": return scored.tail(1)
    raise ValueError("OUTPUT_MODE must be 'historical' or 'latest'")


def export_series(symbol: str, processed: pd.DataFrame) -> None:
    Path(SERIES_DIR).mkdir(parents=True, exist_ok=True)
    processed.to_csv(Path(SERIES_DIR) / f"series_{symbol.replace('^', '').replace('/', '_')}.csv", index=False)


def fetch_symbol_data(symbol: str, info: SymbolInfo) -> MarketData:
    if info.asset_type == "crypto": return fetch_crypto_data(symbol, DAYS_CRYPTO)
    if info.asset_type in {"stock", "index"}: return fetch_stock_data(symbol, parse_days(DAYS_EQUITY))
    raise ValueError(f"Unsupported asset type for {symbol}: {info.asset_type}")


def main() -> None:
    cfg = load_config(CONFIG_PATH); ts = datetime.now(CT).strftime("%Y-%m-%dT%H:%M:%S%z"); rows: List[Dict[str, object]] = []; skipped = []
    symbols = get_tracking_symbols(); LOGGER.info("Tracking %s symbols: %s", len(symbols), ", ".join(symbols))
    for symbol in symbols:
        info = SYMBOL_MANAGER.get_symbol_info(symbol)
        if not info: skipped.append((symbol, "unknown_symbol")); continue
        try:
            scfg = apply_overrides(symbol, cfg); md = fetch_symbol_data(symbol, info); df = prepare_ohlcv(md.df)
            ok, reason = validate_data_integrity(df, symbol)
            if not ok: skipped.append((symbol, reason)); LOGGER.warning("SKIPPED %s: %s", symbol, reason); continue
            LOGGER.info("%s bars=%s first=%s last=%s source=%s", symbol, len(df), df["Date"].iloc[0].date(), df["Date"].iloc[-1].date(), md.source)
            processed = process_df(df, scfg)
            if EXPORT_SERIES: export_series(symbol, processed)
            selected = select_rows_for_mode(processed, OUTPUT_MODE)
            if selected.empty: skipped.append((symbol, "no_scored_rows")); continue
            rows.extend(row_to_output(row, symbol, md.source, ts) for _, row in selected.iterrows())
            LOGGER.info("APPENDED %s rows=%s latest_score=%.2f latest_signal=%s", symbol, len(selected), selected.iloc[-1]["composite_score"], selected.iloc[-1]["signal"])
        except Exception as exc:
            skipped.append((symbol, str(exc))); LOGGER.exception("SKIPPED %s: %s", symbol, exc)
    ensure_schema(OUT_CSV); write_rows(OUT_CSV, rows, WRITE_MODE)
    LOGGER.info("Wrote %s rows to %s with WRITE_MODE=%s OUTPUT_MODE=%s", len(rows), OUT_CSV, WRITE_MODE, OUTPUT_MODE)
    if skipped: LOGGER.warning("Skipped symbols: %s", "; ".join(f"{s}={r}" for s, r in skipped))


if __name__ == "__main__":
    main()
