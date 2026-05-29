#!/usr/bin/env python3
"""Market Tracker Pipeline - v2.0

Fetches OHLCV data from multiple free API sources, computes technical indicators,
generates composite trading signals with confidence levels, and outputs structured
data for both CSV analysis and JSON co-pilot consumption.
"""
from __future__ import annotations

import csv
import json
import logging
import os
import time
from dataclasses import dataclass
from datetime import datetime, timezone
from io import StringIO
from pathlib import Path
from typing import Dict, Iterable, List, Tuple

import numpy as np
import pandas as pd
import pytz
import requests

try:
    import yfinance as yf
except ImportError:  # pragma: no cover
    yf = None

from copilot_output import (
    build_copilot_payload,
    build_signal_payload,
    write_copilot_json,
    write_latest_signals_json,
)
from data_quality import ReliabilityTracker, assess_quality
from indicators import compute_all_indicators
from scoring import (
    composite_and_subscores,
    compute_confidence,
    compute_market_regime,
    compute_positioning,
    enforce_guards,
    finite_or_none,
    latest_dict,
)
from strategies import raw_signal
from symbol_manager import SymbolInfo, SymbolManager

# --- Configuration ---
CT = pytz.timezone("America/Chicago")
OUT_CSV = os.getenv("OUTPUT_PATH", "/data/market_tracker.csv")
OUT_JSON = os.getenv("OUTPUT_JSON_PATH", "/data/copilot_signals.json")
OUT_LATEST = os.getenv("OUTPUT_LATEST_PATH", "/data/latest_signals.json")
CONFIG_PATH = os.getenv("CONFIG_PATH", "/app/config.json")
DAYS_CRYPTO = int(os.getenv("DAYS_CRYPTO", "730"))
DAYS_EQUITY = os.getenv("DAYS_EQUITY", "800d")
OUTPUT_MODE = os.getenv("OUTPUT_MODE", "historical").strip().lower()
WRITE_MODE = os.getenv("WRITE_MODE", "replace" if OUTPUT_MODE == "historical" else "append").strip().lower()
EXPORT_SERIES = os.getenv("EXPORT_SERIES", "false").lower() == "true"
EXPORT_JSON = os.getenv("EXPORT_JSON", "true").lower() == "true"
SERIES_DIR = os.getenv("SERIES_DIR", "/data")
HTTP_TIMEOUT_SECONDS = int(os.getenv("HTTP_TIMEOUT_SECONDS", "30"))
REQUEST_DELAY_SECONDS = float(os.getenv("REQUEST_DELAY_SECONDS", "0.5"))

logging.basicConfig(
    level=os.getenv("LOG_LEVEL", "INFO").upper(),
    format="%(asctime)s %(levelname)s %(message)s",
)
LOGGER = logging.getLogger("market_tracker")
SYMBOL_MANAGER = SymbolManager()
_DEFAULT_CRYPTO_CATEGORIES = "major,defi,layer1,layer2,infrastructure,meme"
_DEFAULT_STOCK_CATEGORIES = (
    "tech_mega_caps,enterprise_software,semiconductors,finance,healthcare,energy,"
    "consumer,industrial,staples,communications,materials_mining"
)
TRACK_CRYPTO = [x.strip() for x in os.getenv("TRACK_CRYPTO", _DEFAULT_CRYPTO_CATEGORIES).split(",") if x.strip()]
TRACK_STOCKS = [x.strip() for x in os.getenv("TRACK_STOCKS", _DEFAULT_STOCK_CATEGORIES).split(",") if x.strip()]
TRACK_ALL = os.getenv("TRACK_ALL", "false").lower() == "true"
TRACK_INDICES = os.getenv("TRACK_INDICES", "true").lower() == "true"
TRACK_SYMBOLS = [x.strip().upper() for x in os.getenv("TRACK_SYMBOLS", "").split(",") if x.strip()]

SCHEMA_COLUMNS = [
    "timestamp_ct", "symbol", "data_source", "date", "open", "high", "low", "close", "volume",
    "ema20", "ema50", "ema100", "ema200", "sma20", "sma50", "sma100", "sma200",
    "rsi14", "macd", "macd_signal", "macd_hist", "atr14", "adx14", "plus_di14", "minus_di14",
    "bb_mid20", "bb_upper20", "bb_lower20", "bb_width", "pivot", "r1", "s1", "r2", "s2", "r3", "s3",
    "fib_long_low", "fib_long_high", "fib_long_23.6%", "fib_long_38.2%", "fib_long_50.0%", "fib_long_61.8%", "fib_long_78.6%",
    "fib_short_low", "fib_short_high", "fib_short_23.6%", "fib_short_38.2%", "fib_short_50.0%", "fib_short_61.8%", "fib_short_78.6%",
    "vwap20", "rvol", "obv", "roc10", "roc20", "stoch_rsi", "mom_divergence", "weekly_trend",
    "trend_s", "momentum_s", "strength_s", "vol_s", "fib_s", "pivot_s", "volume_s",
    "composite_score", "signal", "confidence_level", "confidence_score",
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
    if TRACK_ALL:
        return dedupe(SYMBOL_MANAGER.all_symbols())
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
            "weights": {"trend": 0.45, "momentum": 0.20, "strength": 0.15, "vol": 0.08, "fib": 0.03, "pivot": 0.02, "volume": 0.07},
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
        "strategy": o.get("strategy", d.get("strategy", "trend")),
    }
    if merged["thresholds"]["long"] <= merged["thresholds"]["short"]:
        raise ValueError(f"Invalid thresholds for {symbol}")
    return merged


# --- Data Preparation ---

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
    # Some index/FX feeds (e.g. DXY) occasionally publish inconsistent OHLC; clamp to a valid envelope.
    ohlc = out[["Open", "High", "Low", "Close"]]
    out["High"] = ohlc.max(axis=1)
    out["Low"] = ohlc.min(axis=1)
    return out.sort_values("Date").drop_duplicates(subset=["Date"], keep="last").reset_index(drop=True)


def validate_data_integrity(df: pd.DataFrame, symbol: str, min_bars: int = 220) -> Tuple[bool, str]:
    if len(df) < min_bars:
        return False, f"insufficient_bars ({len(df)} < {min_bars})"
    if not df["Date"].is_monotonic_increasing:
        return False, "non_monotonic_dates"
    if df["Date"].duplicated().any():
        return False, "duplicate_dates"
    if not (df["Close"] > 0).all():
        return False, "invalid_prices"
    if df["Close"].isna().sum() > len(df) * 0.05:
        return False, "too_many_nans"
    if (df["High"] < df[["Open", "Close", "Low"]].max(axis=1)).any():
        return False, "invalid_high_values"
    if (df["Low"] > df[["Open", "Close", "High"]].min(axis=1)).any():
        return False, "invalid_low_values"
    return True, "ok"


# --- Data Fetchers ---

def fetch_yahoo_chart_data(symbol: str, days: int) -> MarketData:
    yf_symbol = SYMBOL_MANAGER.get_api_mapping(symbol, "yfinance") or symbol
    url = f"https://query1.finance.yahoo.com/v8/finance/chart/{yf_symbol}"
    headers = {"User-Agent": "Mozilla/5.0 (compatible; MarketTracker/1.0)"}
    r = requests.get(
        url,
        params={"range": f"{max(days, 7)}d", "interval": "1d", "includePrePost": "false"},
        headers=headers,
        timeout=(5, HTTP_TIMEOUT_SECONDS),
    )
    r.raise_for_status()
    result = (r.json().get("chart") or {}).get("result")
    if not result:
        raise ValueError("No chart data in Yahoo Finance response")
    block = result[0]
    quote = (block.get("indicators") or {}).get("quote", [{}])[0]
    timestamps = block.get("timestamp") or []
    if not timestamps or not quote.get("close"):
        raise ValueError("Yahoo Finance chart payload missing OHLCV series")
    df = pd.DataFrame(
        {
            "Date": pd.to_datetime(timestamps, unit="s"),
            "Open": quote.get("open"),
            "High": quote.get("high"),
            "Low": quote.get("low"),
            "Close": quote.get("close"),
            "Volume": quote.get("volume"),
        }
    )
    df = df[df["Date"] >= datetime.utcnow() - pd.Timedelta(days=days)]
    return MarketData(prepare_ohlcv(df), "Yahoo Finance Chart API")


def fetch_stooq_data(symbol: str, days: int) -> MarketData:
    stooq_symbol = SYMBOL_MANAGER.get_api_mapping(symbol, "stooq")
    if not stooq_symbol:
        raise ValueError(f"No Stooq mapping configured for {symbol}")
    r = requests.get(
        f"https://stooq.com/q/d/l/?s={stooq_symbol}&i=d",
        timeout=(5, HTTP_TIMEOUT_SECONDS),
    )
    r.raise_for_status()
    df = pd.read_csv(StringIO(r.text))
    df["Date"] = pd.to_datetime(df["Date"])
    df = df[df["Date"] >= datetime.utcnow() - pd.Timedelta(days=days)]
    return MarketData(prepare_ohlcv(df), "Stooq API")


def fetch_yfinance_data(symbol: str, days: int) -> MarketData:
    if yf is None:
        raise ValueError("yfinance is not installed")
    yf_symbol = SYMBOL_MANAGER.get_api_mapping(symbol, "yfinance") or symbol
    df = yf.download(
        yf_symbol, period=f"{days}d", interval="1d", auto_adjust=False, progress=False, threads=False
    )
    if df.empty:
        raise ValueError("No data received from Yahoo Finance")
    if isinstance(df.columns, pd.MultiIndex):
        df.columns = [c[0] for c in df.columns]
    return MarketData(
        prepare_ohlcv(df.reset_index()[["Date", "Open", "High", "Low", "Close", "Volume"]]),
        "Yahoo Finance",
    )


def fetch_stock_data(symbol: str, days: int, tracker: ReliabilityTracker) -> MarketData:
    errors = []
    providers = (
        ("Yahoo Finance", fetch_yfinance_data),
        ("Yahoo Finance Chart API", fetch_yahoo_chart_data),
        ("Stooq", fetch_stooq_data),
    )
    if yf is None:
        providers = (("Yahoo Finance Chart API", fetch_yahoo_chart_data), ("Stooq", fetch_stooq_data))
    for name, fn in providers:
        try:
            LOGGER.info("Trying %s for %s", name, symbol)
            t0 = time.time()
            result = fn(symbol, days)
            tracker.record_success(name, (time.time() - t0) * 1000)
            return result
        except Exception as exc:
            tracker.record_failure(name, str(exc))
            errors.append(f"{name}: {exc}")
            LOGGER.warning("%s failed for %s: %s", name, symbol, exc)
    raise ValueError(f"No stock/index API data available for {symbol}. Attempts: {' | '.join(errors)}")


def fetch_kraken_data(symbol: str, days: int) -> MarketData:
    pair = SYMBOL_MANAGER.get_api_mapping(symbol, "kraken")
    if not pair:
        raise ValueError(f"No Kraken mapping configured for {symbol}")
    r = requests.get(
        "https://api.kraken.com/0/public/OHLC",
        params={"pair": pair, "interval": "1440"},
        timeout=HTTP_TIMEOUT_SECONDS,
    )
    r.raise_for_status()
    data = r.json()
    if data.get("error"):
        raise ValueError(f"Kraken API error: {data['error']}")
    result = data.get("result", {})
    candles = result.get(pair)
    if not candles:
        keys = [k for k in result if k != "last"]
        candles = result.get(keys[0]) if keys else None
    if not candles:
        raise ValueError("No OHLC data received from Kraken")
    df = pd.DataFrame([{
        "Date": pd.to_datetime(int(c[0]), unit="s"),
        "Open": float(c[1]), "High": float(c[2]),
        "Low": float(c[3]), "Close": float(c[4]),
        "Volume": float(c[6]),
    } for c in candles])
    df = df[df["Date"] >= datetime.utcnow() - pd.Timedelta(days=days)]
    return MarketData(prepare_ohlcv(df), "Kraken API")


def fetch_coinbase_data(symbol: str, days: int) -> MarketData:
    product = SYMBOL_MANAGER.get_api_mapping(symbol, "coinbase")
    if not product:
        raise ValueError(f"No Coinbase mapping configured for {symbol}")
    end = datetime.utcnow()
    start = end - pd.Timedelta(days=days)
    r = requests.get(
        f"https://api.exchange.coinbase.com/products/{product}/candles",
        params={"start": start.isoformat(), "end": end.isoformat(), "granularity": "86400"},
        timeout=HTTP_TIMEOUT_SECONDS,
    )
    r.raise_for_status()
    data = r.json()
    if not data:
        raise ValueError("No OHLC data received from Coinbase")
    df = pd.DataFrame([{
        "Date": pd.to_datetime(int(c[0]), unit="s"),
        "Low": float(c[1]), "High": float(c[2]),
        "Open": float(c[3]), "Close": float(c[4]),
        "Volume": float(c[5]),
    } for c in data])
    return MarketData(prepare_ohlcv(df), "Coinbase API")


def fetch_coingecko_ohlc_data(symbol: str, days: int) -> MarketData:
    coin_id = SYMBOL_MANAGER.get_api_mapping(symbol, "coingecko")
    if not coin_id:
        raise ValueError(f"No CoinGecko mapping configured for {symbol}")
    selected_days = next((w for w in [1, 7, 14, 30, 90, 180, 365] if days <= w), 365)
    r = requests.get(
        f"https://api.coingecko.com/api/v3/coins/{coin_id}/ohlc",
        params={"vs_currency": "usd", "days": selected_days},
        timeout=HTTP_TIMEOUT_SECONDS,
    )
    r.raise_for_status()
    data = r.json()
    if not data:
        raise ValueError("No OHLC data received from CoinGecko")
    df = pd.DataFrame([{
        "Date": pd.to_datetime(int(c[0]), unit="ms"),
        "Open": float(c[1]), "High": float(c[2]),
        "Low": float(c[3]), "Close": float(c[4]),
        "Volume": np.nan,
    } for c in data])
    df = df[df["Date"] >= datetime.utcnow() - pd.Timedelta(days=days)]
    return MarketData(prepare_ohlcv(df), "CoinGecko OHLC API")


def fetch_coinpaprika_data(symbol: str, days: int) -> MarketData:
    coin_ids = {"SOL-USD": "sol-solana", "BTC-USD": "btc-bitcoin", "ETH-USD": "eth-ethereum", "XRP-USD": "xrp-ripple"}
    coin_id = coin_ids.get(symbol)
    if not coin_id:
        raise ValueError(f"No CoinPaprika mapping configured for {symbol}")
    r = requests.get(
        f"https://api.coinpaprika.com/v1/coins/{coin_id}/ohlcv/historical",
        params={
            "start": (datetime.utcnow() - pd.Timedelta(days=days)).strftime("%Y-%m-%d"),
            "end": datetime.utcnow().strftime("%Y-%m-%d"),
        },
        timeout=HTTP_TIMEOUT_SECONDS,
    )
    r.raise_for_status()
    data = r.json()
    if not data:
        raise ValueError("No OHLC data received from CoinPaprika")
    df = pd.DataFrame([{
        "Date": pd.to_datetime(x["time_open"]),
        "Open": float(x["open"]), "High": float(x["high"]),
        "Low": float(x["low"]), "Close": float(x["close"]),
        "Volume": float(x["volume"]),
    } for x in data])
    return MarketData(prepare_ohlcv(df), "CoinPaprika API")


def fetch_crypto_data(symbol: str, days: int, tracker: ReliabilityTracker) -> MarketData:
    errors = []
    for fn in [fetch_kraken_data, fetch_coinbase_data, fetch_coingecko_ohlc_data, fetch_coinpaprika_data]:
        name = fn.__name__.replace("fetch_", "").replace("_data", "").replace("_", " ").title()
        try:
            LOGGER.info("Trying %s for %s", name, symbol)
            time.sleep(REQUEST_DELAY_SECONDS)
            t0 = time.time()
            result = fn(symbol, days)
            tracker.record_success(name, (time.time() - t0) * 1000)
            return result
        except Exception as exc:
            tracker.record_failure(name, str(exc))
            errors.append(f"{name}: {exc}")
            LOGGER.warning("%s failed for %s: %s", name, symbol, exc)
    raise ValueError(f"No crypto API data available for {symbol}. Attempts: {' | '.join(errors)}")


# --- Processing ---

def nan_to_none(x):
    if x is None or pd.isna(x):
        return None
    if isinstance(x, (int, float, np.integer, np.floating)):
        return float(x) if np.isfinite(x) else None
    return x


def process_df(df: pd.DataFrame, symbol_cfg: dict) -> pd.DataFrame:
    fl = int(symbol_cfg["lookbacks"]["fib_long"])
    fs = int(symbol_cfg["lookbacks"]["fib_short"])
    out = compute_all_indicators(prepare_ohlcv(df), fl, fs)

    score_cols = ["trend_s", "momentum_s", "strength_s", "vol_s", "fib_s", "pivot_s", "volume_s", "composite_score"]
    for c in score_cols:
        out[c] = np.nan
    out["signal"] = "NEUTRAL"
    out["confidence_level"] = "LOW"
    out["confidence_score"] = 0.0

    warmup = max(200, fl, fs)
    for idx, row in out.iterrows():
        if idx + 1 < warmup:
            continue
        ld = latest_dict(row)
        score, subs = composite_and_subscores(ld, symbol_cfg["weights"])
        if not np.isfinite(score):
            continue

        strategy = symbol_cfg.get("strategy", "trend")
        raw = raw_signal(
            strategy,
            score=score,
            long_th=float(symbol_cfg["thresholds"]["long"]),
            short_th=float(symbol_cfg["thresholds"]["short"]),
            close=finite_or_none(ld.get("close")),
            rsi14=finite_or_none(ld.get("rsi14")),
            bb_lower20=finite_or_none(row.get("BB_LOWER20")),
            bb_upper20=finite_or_none(row.get("BB_UPPER20")),
            ema200=finite_or_none(ld.get("ema200")),
            adx14=finite_or_none(ld.get("adx14")),
        )
        signal = enforce_guards(symbol_cfg, ld, raw, strategy)
        conf_level, conf_score = compute_confidence(score, subs, ld, symbol_cfg["thresholds"], signal)

        for k, v in subs.items():
            out.loc[idx, k] = v
        out.loc[idx, "composite_score"] = score
        out.loc[idx, "signal"] = signal
        out.loc[idx, "confidence_level"] = conf_level
        out.loc[idx, "confidence_score"] = conf_score

    return out


def row_to_output(row: pd.Series, symbol: str, source: str, ts: str) -> Dict[str, object]:
    mapping = {
        "timestamp_ct": ts, "symbol": symbol, "data_source": source,
        "date": row["Date"].date().isoformat() if isinstance(row["Date"], pd.Timestamp) else str(row["Date"]),
        "open": row.get("Open"), "high": row.get("High"), "low": row.get("Low"),
        "close": row.get("Close"), "volume": row.get("Volume"),
        "ema20": row.get("EMA20"), "ema50": row.get("EMA50"),
        "ema100": row.get("EMA100"), "ema200": row.get("EMA200"),
        "sma20": row.get("SMA20"), "sma50": row.get("SMA50"),
        "sma100": row.get("SMA100"), "sma200": row.get("SMA200"),
        "rsi14": row.get("RSI14"), "macd": row.get("MACD"),
        "macd_signal": row.get("MACD_SIGNAL"), "macd_hist": row.get("MACD_HIST"),
        "atr14": row.get("ATR14"), "adx14": row.get("ADX14"),
        "plus_di14": row.get("+DI14"), "minus_di14": row.get("-DI14"),
        "bb_mid20": row.get("BB_MID20"), "bb_upper20": row.get("BB_UPPER20"),
        "bb_lower20": row.get("BB_LOWER20"), "bb_width": row.get("BB_WIDTH"),
        "pivot": row.get("PIVOT"), "r1": row.get("R1"), "s1": row.get("S1"),
        "r2": row.get("R2"), "s2": row.get("S2"), "r3": row.get("R3"), "s3": row.get("S3"),
        "fib_long_low": row.get("fib_long_low"), "fib_long_high": row.get("fib_long_high"),
        "fib_long_23.6%": row.get("fib_long_23.6%"), "fib_long_38.2%": row.get("fib_long_38.2%"),
        "fib_long_50.0%": row.get("fib_long_50.0%"), "fib_long_61.8%": row.get("fib_long_61.8%"),
        "fib_long_78.6%": row.get("fib_long_78.6%"),
        "fib_short_low": row.get("fib_short_low"), "fib_short_high": row.get("fib_short_high"),
        "fib_short_23.6%": row.get("fib_short_23.6%"), "fib_short_38.2%": row.get("fib_short_38.2%"),
        "fib_short_50.0%": row.get("fib_short_50.0%"), "fib_short_61.8%": row.get("fib_short_61.8%"),
        "fib_short_78.6%": row.get("fib_short_78.6%"),
        "vwap20": row.get("VWAP20"), "rvol": row.get("RVOL"), "obv": row.get("OBV"),
        "roc10": row.get("ROC10"), "roc20": row.get("ROC20"),
        "stoch_rsi": row.get("STOCH_RSI"), "mom_divergence": row.get("MOM_DIVERGENCE"),
        "weekly_trend": row.get("WEEKLY_TREND"),
        "trend_s": row.get("trend_s"), "momentum_s": row.get("momentum_s"),
        "strength_s": row.get("strength_s"), "vol_s": row.get("vol_s"),
        "fib_s": row.get("fib_s"), "pivot_s": row.get("pivot_s"),
        "volume_s": row.get("volume_s"),
        "composite_score": row.get("composite_score"), "signal": row.get("signal", "NEUTRAL"),
        "confidence_level": row.get("confidence_level", "LOW"),
        "confidence_score": row.get("confidence_score", 0.0),
    }
    return {c: nan_to_none(mapping.get(c)) for c in SCHEMA_COLUMNS}


# --- Output ---

def ensure_schema(path: str) -> None:
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)
    if not p.exists():
        with p.open("w", newline="", encoding="utf-8") as f:
            csv.DictWriter(f, fieldnames=SCHEMA_COLUMNS).writeheader()


def write_rows(path: str, rows: List[Dict[str, object]], mode: str) -> None:
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)
    df = pd.DataFrame(rows, columns=SCHEMA_COLUMNS)
    if mode == "append" and p.exists() and p.stat().st_size > 0:
        old = pd.read_csv(p)
        df = pd.concat([old, df], ignore_index=True).drop_duplicates(
            subset=["symbol", "date"], keep="last",
        ).sort_values(["symbol", "date"])
    elif mode != "replace":
        raise ValueError("WRITE_MODE must be 'replace' or 'append'")
    df.to_csv(p, index=False)


def select_rows_for_mode(processed: pd.DataFrame, mode: str) -> pd.DataFrame:
    scored = processed[pd.notna(processed["composite_score"])].copy()
    if mode == "historical":
        return scored
    if mode == "latest":
        return scored.tail(1)
    raise ValueError("OUTPUT_MODE must be 'historical' or 'latest'")


def export_series(symbol: str, processed: pd.DataFrame) -> None:
    Path(SERIES_DIR).mkdir(parents=True, exist_ok=True)
    processed.to_csv(
        Path(SERIES_DIR) / f"series_{symbol.replace('^', '').replace('/', '_')}.csv",
        index=False,
    )


def fetch_symbol_data(symbol: str, info: SymbolInfo, tracker: ReliabilityTracker) -> MarketData:
    if info.asset_type == "crypto":
        return fetch_crypto_data(symbol, DAYS_CRYPTO, tracker)
    if info.asset_type in {"stock", "index"}:
        return fetch_stock_data(symbol, parse_days(DAYS_EQUITY), tracker)
    raise ValueError(f"Unsupported asset type for {symbol}: {info.asset_type}")


# --- Main Pipeline ---

def main() -> None:
    cfg = load_config(CONFIG_PATH)
    ts = datetime.now(CT).strftime("%Y-%m-%dT%H:%M:%S%z")
    run_timestamp = datetime.now(timezone.utc).isoformat(timespec="seconds")

    rows: List[Dict[str, object]] = []
    skipped = []
    copilot_signals: List[dict] = []
    quality_reports: List[dict] = []
    latest_scores: Dict[str, float] = {}
    tracker = ReliabilityTracker()

    symbols = get_tracking_symbols()
    LOGGER.info("Tracking %s symbols: %s", len(symbols), ", ".join(symbols))

    for symbol in symbols:
        info = SYMBOL_MANAGER.get_symbol_info(symbol)
        if not info:
            skipped.append((symbol, "unknown_symbol"))
            continue
        try:
            scfg = apply_overrides(symbol, cfg)
            md = fetch_symbol_data(symbol, info, tracker)
            df = prepare_ohlcv(md.df)

            ok, reason = validate_data_integrity(df, symbol)
            if not ok:
                skipped.append((symbol, reason))
                LOGGER.warning("SKIPPED %s: %s", symbol, reason)
                continue

            LOGGER.info(
                "%s bars=%s first=%s last=%s source=%s",
                symbol, len(df), df["Date"].iloc[0].date(), df["Date"].iloc[-1].date(), md.source,
            )

            # Assess data quality
            expected_bars = DAYS_CRYPTO if info.asset_type == "crypto" else parse_days(DAYS_EQUITY)
            dq = assess_quality(df, symbol, md.source, expected_bars, info.asset_type)
            quality_reports.append(dq.to_dict())

            processed = process_df(df, scfg)
            if EXPORT_SERIES:
                export_series(symbol, processed)

            selected = select_rows_for_mode(processed, OUTPUT_MODE)
            if selected.empty:
                skipped.append((symbol, "no_scored_rows"))
                continue

            rows.extend(row_to_output(row, symbol, md.source, ts) for _, row in selected.iterrows())

            # Build co-pilot signal from the latest row
            last_row = selected.iloc[-1]
            ld = latest_dict(last_row)
            score = last_row.get("composite_score", np.nan)
            latest_scores[symbol] = float(score) if np.isfinite(score) else 0.0

            copilot_row = {
                **{k: nan_to_none(v) for k, v in ld.items()},
                "signal": last_row.get("signal", "NEUTRAL"),
                "composite_score": nan_to_none(score),
                "trend_s": nan_to_none(last_row.get("trend_s")),
                "momentum_s": nan_to_none(last_row.get("momentum_s")),
                "strength_s": nan_to_none(last_row.get("strength_s")),
                "vol_s": nan_to_none(last_row.get("vol_s")),
                "fib_s": nan_to_none(last_row.get("fib_s")),
                "pivot_s": nan_to_none(last_row.get("pivot_s")),
                "volume_s": nan_to_none(last_row.get("volume_s")),
                "macd_hist": nan_to_none(last_row.get("MACD_HIST")),
                "roc1": nan_to_none(last_row.get("Close") / selected.iloc[-2].get("Close") - 1) if len(selected) > 1 else None,
                "roc10": nan_to_none(last_row.get("ROC10")),
                "date": last_row["Date"].date().isoformat() if isinstance(last_row["Date"], pd.Timestamp) else str(last_row["Date"]),
            }

            conf_level = last_row.get("confidence_level", "LOW")
            conf_score = last_row.get("confidence_score", 0.0)

            sig_payload = build_signal_payload(
                symbol=symbol,
                row=copilot_row,
                confidence_level=conf_level,
                confidence_score=float(conf_score) if conf_score else 0.0,
                quality_grade=dq.quality_grade,
                source=md.source,
                asset_type=info.asset_type,
            )
            copilot_signals.append(sig_payload)

            LOGGER.info(
                "PROCESSED %s score=%.2f signal=%s confidence=%s(%s) quality=%s",
                symbol, score, last_row.get("signal"), conf_level, conf_score, dq.quality_grade,
            )

        except Exception as exc:
            skipped.append((symbol, str(exc)))
            LOGGER.exception("SKIPPED %s: %s", symbol, exc)

    # Write CSV output
    ensure_schema(OUT_CSV)
    write_rows(OUT_CSV, rows, WRITE_MODE)
    LOGGER.info("Wrote %s rows to %s with WRITE_MODE=%s OUTPUT_MODE=%s", len(rows), OUT_CSV, WRITE_MODE, OUTPUT_MODE)

    # Write JSON co-pilot output
    if EXPORT_JSON and copilot_signals:
        regime = compute_market_regime(latest_scores)
        positioning = compute_positioning(regime, copilot_signals)
        payload = build_copilot_payload(
            signals=copilot_signals,
            regime=regime,
            quality_reports=quality_reports,
            source_reliability=tracker.summary(),
            run_timestamp=run_timestamp,
            positioning=positioning,
        )
        write_copilot_json(payload, OUT_JSON)
        write_latest_signals_json(copilot_signals, OUT_LATEST)
        LOGGER.info(
            "Wrote co-pilot JSON: %s signals, regime=%s, to %s",
            len(copilot_signals), regime["regime"], OUT_JSON,
        )

    if skipped:
        LOGGER.warning("Skipped symbols: %s", "; ".join(f"{s}={r}" for s, r in skipped))


if __name__ == "__main__":
    main()
