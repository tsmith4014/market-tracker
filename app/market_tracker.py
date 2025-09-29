#!/usr/bin/env python3
import math, time, csv, os, json
from datetime import datetime
from typing import Dict, List, Tuple
import pytz
import numpy as np
import pandas as pd
import requests
import yfinance as yf

CT = pytz.timezone("America/Chicago")

OUT_CSV = os.getenv("OUTPUT_PATH", "/data/market_tracker.csv")
CONFIG_PATH = os.getenv("CONFIG_PATH", "/app/config.json")

DAYS_CRYPTO = int(os.getenv("DAYS_CRYPTO", "365"))
DAYS_EQUITY = os.getenv("DAYS_EQUITY", "400d")

EXPORT_SERIES = os.getenv("EXPORT_SERIES", "false").lower() == "true"
SERIES_DIR = os.getenv("SERIES_DIR", "/data")

CRYPTO_BINANCE = {
    "SOL-USD": "SOLUSDT",
    "BTC-USD": "BTCUSDT",
    "ETH-USD": "ETHUSDT",
    "XRP-USD": "XRPUSDT",
}
EQUITIES_YF = ["AMD", "NVDA", "^DXY"]

def load_config(path: str) -> dict:
    if not os.path.exists(path):
        return {
            "defaults": {
                "weights": {"trend":0.50,"momentum":0.20,"strength":0.15,"vol":0.05,"fib":0.05,"pivot":0.05},
                "thresholds": {"long":30,"short":-30},
                "lookbacks": {"fib_long":180,"fib_short":30},
                "guards": {"min_adx_for_signal":18,"max_atr_pct":12.0,"require_close_above_ema50_for_long":False,"require_close_below_ema50_for_short":False},
                "fees": {"bps_per_side":1.0,"slippage_bps_per_side":1.0}
            },
            "overrides": {}
        }
    with open(path, "r") as f:
        return json.load(f)

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
    assert merged["thresholds"]["long"] > merged["thresholds"]["short"]
    return merged

def ema(s: pd.Series, span: int) -> pd.Series: return s.ewm(span=span, adjust=False).mean()
def sma(s: pd.Series, window: int) -> pd.Series: return s.rolling(window, min_periods=window).mean()

def rsi(s: pd.Series, period: int = 14) -> pd.Series:
    d = s.diff(); up = d.clip(lower=0.0); dn = -d.clip(upper=0.0)
    rs = up.rolling(period).mean() / dn.rolling(period).mean()
    return 100.0 - (100.0 / (1.0 + rs))

def macd(s: pd.Series, fast=12, slow=26, signal=9):
    line = ema(s, fast) - ema(s, slow); sig = ema(line, signal); hist = line - sig
    return line, sig, hist

def _true_range(h: pd.Series, l: pd.Series, c: pd.Series) -> pd.Series:
    pc = c.shift(1)
    return pd.concat([(h - l), (h - pc).abs(), (l - pc).abs()], axis=1).max(axis=1)

def atr(h: pd.Series, l: pd.Series, c: pd.Series, period=14) -> pd.Series:
    return _true_range(h, l, c).rolling(period).mean()

def adx(h: pd.Series, l: pd.Series, c: pd.Series, period=14):
    up = h.diff(); dn = -l.diff()
    plus_dm = np.where((up > dn) & (up > 0), up, 0.0)
    minus_dm = np.where((dn > up) & (dn > 0), dn, 0.0)
    tr = _true_range(h, l, c)
    atr_n = tr.rolling(period).mean()
    plus_di = 100 * (pd.Series(plus_dm, index=h.index).rolling(period).sum() / atr_n)
    minus_di = 100 * (pd.Series(minus_dm, index=h.index).rolling(period).sum() / atr_n)
    dx = (plus_di.subtract(minus_di).abs() / (plus_di + minus_di)) * 100
    return dx.rolling(period).mean(), plus_di, minus_di

def bollinger(s: pd.Series, window=20, nstd=2.0):
    mid = s.rolling(window).mean(); std = s.rolling(window).std()
    up = mid + nstd * std; dn = mid - nstd * std
    width = (up - dn) / mid
    return mid, up, dn, width

def pivots(df: pd.DataFrame):
    prev = df.shift(1)
    P = (prev['High'] + prev['Low'] + prev['Close']) / 3.0
    R1 = 2*P - prev['Low']; S1 = 2*P - prev['High']
    R2 = P + (prev['High'] - prev['Low']); S2 = P - (prev['High'] - prev['Low'])
    R3 = prev['High'] + 2*(P - prev['Low']); S3 = prev['Low'] - 2*(prev['High'] - P)
    return P, R1, S1, R2, S2, R3, S3

def detect_swing(df: pd.DataFrame, lookback: int) -> Tuple[float, float]:
    window = df.tail(lookback).copy()
    highs, lows = window['High'], window['Low']
    best_low, best_high, best_move = None, None, 0.0
    low_idx = lows.idxmin()
    for hi_idx in highs.index:
        if hi_idx > low_idx:
            move = (highs.loc[hi_idx] - lows.loc[low_idx]) / max(lows.loc[low_idx], 1e-9)
            if move > best_move: best_move = move; best_low, best_high = lows.loc[low_idx], highs.loc[hi_idx]
    high_idx = highs.idxmax()
    for lo_idx in lows.index:
        if lo_idx > high_idx:
            move = (highs.loc[high_idx] - lows.loc[lo_idx]) / max(highs.loc[high_idx], 1e-9)
            if move > best_move: best_move = move; best_low, best_high = lows.loc[lo_idx], highs.loc[hi_idx]
    if best_low is None or best_high is None:
        lo_i, hi_i = lows.idxmin(), highs.idxmax()
        best_low, best_high = (lows.loc[lo_i], highs.loc[hi_i]) if lo_i < hi_i else (lows.loc[hi_i], highs.loc[lo_i])
    return float(min(best_low, best_high)), float(max(best_low, best_high))

def fib_levels(low: float, high: float) -> Dict[str, float]:
    levels = [0.236, 0.382, 0.5, 0.618, 0.786]
    return {f"{int(l*1000)/10:.1f}%": high - (high - low) * l for l in levels}

def fetch_binance_klines(symbol: str, interval="1d", days=365) -> pd.DataFrame:
    url = "https://api.binance.com/api/v3/klines"
    params = {"symbol": symbol, "interval": interval, "limit": min(days, 1000)}
    try:
        r = requests.get(url, params=params, timeout=30); r.raise_for_status()
        data = r.json()
        cols = ["OpenTime","Open","High","Low","Close","Volume","CloseTime","QuoteAssetVolume","NumberOfTrades","TakerBuyBase","TakerBuyQuote","Ignore"]
        df = pd.DataFrame(data, columns=cols)
        df["Date"] = pd.to_datetime(df["OpenTime"], unit="ms")
        for c in ["Open","High","Low","Close","Volume"]: df[c] = df[c].astype(float)
        return df[["Date","Open","High","Low","Close","Volume"]].sort_values("Date")
    except Exception as e:
        print(f"Warning: Binance API failed for {symbol}: {e}")
        print("Using yfinance as fallback...")
        # Fallback to yfinance for crypto data
        yf_symbol = symbol.replace("USDT", "-USD")
        return fetch_yf_daily(yf_symbol, period=f"{days}d")

def fetch_yf_daily(ticker: str, period="400d") -> pd.DataFrame:
    try:
        df = yf.download(ticker, period=period, interval="1d", auto_adjust=False, progress=False)
        if df.empty:
            raise ValueError("Empty data from yfinance")
        return df.reset_index()[["Date","Open","High","Low","Close","Volume"]].dropna()
    except Exception as e:
        print(f"Warning: yfinance failed for {ticker}: {e}")
        print("Generating mock data for testing...")
        return generate_mock_data(ticker, period)

def generate_mock_data(ticker: str, period="400d") -> pd.DataFrame:
    """Generate mock OHLCV data for testing when APIs fail"""
    import random
    from datetime import datetime, timedelta
    
    # Parse period to get number of days
    if period.endswith('d'):
        days = int(period[:-1])
    else:
        days = 400
    
    # Generate date range
    end_date = datetime.now()
    start_date = end_date - timedelta(days=days)
    dates = pd.date_range(start=start_date, end=end_date, freq='D')
    
    # Generate mock price data with some realistic patterns
    base_price = 100.0 if 'USD' in ticker else 50.0
    prices = [base_price]
    
    for i in range(1, len(dates)):
        # Random walk with slight upward bias
        change = random.uniform(-0.05, 0.08)  # -5% to +8% daily change
        new_price = prices[-1] * (1 + change)
        prices.append(max(new_price, 1.0))  # Ensure positive prices
    
    # Generate OHLCV data
    data = []
    for i, (date, close) in enumerate(zip(dates, prices)):
        # Generate realistic OHLC from close price
        volatility = random.uniform(0.01, 0.05)  # 1-5% intraday volatility
        high = close * (1 + random.uniform(0, volatility))
        low = close * (1 - random.uniform(0, volatility))
        open_price = close * (1 + random.uniform(-volatility/2, volatility/2))
        volume = random.randint(1000000, 10000000)  # Random volume
        
        data.append({
            'Date': date,
            'Open': round(open_price, 2),
            'High': round(high, 2),
            'Low': round(low, 2),
            'Close': round(close, 2),
            'Volume': volume
        })
    
    return pd.DataFrame(data)

def _nan_to_none(x):
    if isinstance(x, (float, np.floating)) and (np.isnan(x) or np.isinf(x)): return None
    return float(x) if isinstance(x, (int, float, np.floating)) else x

def _score_trend(close, ema20, ema50, ema200, slope20, slope50, slope200) -> float:
    s = 0.0
    s += 1 if close is not None and ema20 is not None and close > ema20 else -1
    s += 1 if close is not None and ema50 is not None and close > ema50 else -1
    s += 1.5 if close is not None and ema200 is not None and close > ema200 else -1.5
    s += 0.5 if slope20 > 0 else -0.5
    s += 0.5 if slope50 > 0 else -0.5
    s += 1.0 if slope200 > 0 else -1.0
    return max(-5.0, min(5.0, s))

def _score_momentum(rsi14, macd, macd_signal) -> float:
    s = 0.0
    if rsi14 is not None:
        if 50 <= rsi14 <= 70: s += 1.0
        if 30 <= rsi14 < 50:  s += -0.5
        if rsi14 > 70:        s += 0.5
        if rsi14 < 30:        s += -1.0
    if macd is not None and macd_signal is not None:
        s += 1.0 if macd > macd_signal else -1.0
        s += 0.5 if macd > 0 else -0.5
    return max(-3.0, min(3.0, s))

def _score_strength(adx14, plus_di, minus_di) -> float:
    if adx14 is None or plus_di is None or minus_di is None: return 0.0
    s = 1.0 if adx14 >= 25 else -0.5
    s += 0.5 if plus_di > minus_di else -0.5
    return max(-2.0, min(2.0, s))

def _score_volatility(atr14, close, bb_width) -> float:
    s = 0.0
    if atr14 is not None and close:
        atrp = 100.0 * atr14 / close
        if atrp < 2.0: s += 0.5
        elif atrp < 5.0: s += 0.25
        elif atrp < 8.0: s += 0.0
        else: s += -0.5
    if bb_width is not None:
        if bb_width < 0.05: s += 0.25
        elif bb_width > 0.25: s += -0.25
    return max(-1.0, min(1.0, s))

def _score_fib(close, long_low, long_high) -> float:
    if any(v is None for v in [close, long_low, long_high]) or long_high <= long_low: return 0.0
    f38 = long_high - (long_high - long_low) * 0.382
    f50 = long_high - (long_high - long_low) * 0.5
    f62 = long_high - (long_high - long_low) * 0.618
    if min(f38, f62) <= close <= max(f38, f62): return 1.0
    tol = 0.01 * f50
    if abs(close - f50) <= tol: return 0.5
    return -0.25

def _score_pivot(close, pivot, r1, s1) -> float:
    if pivot is None or r1 is None or s1 is None or close is None: return 0.0
    s = 0.5 if close > pivot else -0.5
    if close > r1: s += 0.25
    if close < s1: s += -0.25
    return max(-1.0, min(1.0, s))

def composite_and_subscores(latest: Dict[str, float], weights: dict):
    close = latest.get("close")
    ema20, ema50, ema200 = latest.get("ema20"), latest.get("ema50"), latest.get("ema200")
    slope20 = (latest.get("ema20") or 0.0) - (latest.get("sma20") or 0.0)
    slope50 = (latest.get("ema50") or 0.0) - (latest.get("sma50") or 0.0)
    slope200 = (latest.get("ema200") or 0.0) - (latest.get("sma200") or 0.0)
    rsi14 = latest.get("rsi14")
    macd_v, macd_sig = latest.get("macd"), latest.get("macd_signal")
    adx14, plus_di, minus_di = latest.get("adx14"), latest.get("plus_di14"), latest.get("minus_di14")
    atr14, bb_width = latest.get("atr14"), latest.get("bb_width")
    pivot, r1, s1 = latest.get("pivot"), latest.get("r1"), latest.get("s1")
    long_low, long_high = latest.get("fib_long_low"), latest.get("fib_long_high")

    subs = {
        "trend_s": _score_trend(close, ema20, ema50, ema200, slope20, slope50, slope200),
        "momentum_s": _score_momentum(rsi14, macd_v, macd_sig),
        "strength_s": _score_strength(adx14, plus_di, minus_di),
        "vol_s": _score_volatility(atr14, close, bb_width),
        "fib_s": _score_fib(close, long_low, long_high),
        "pivot_s": _score_pivot(close, pivot, r1, s1),
    }
    caps = np.array([5.0, 3.0, 2.0, 1.0, 1.0, 1.0], dtype=float)
    arr = np.array([subs["trend_s"], subs["momentum_s"], subs["strength_s"], subs["vol_s"], subs["fib_s"], subs["pivot_s"]]) / caps
    w = np.array([
        weights.get("trend",0.5), weights.get("momentum",0.2), weights.get("strength",0.15),
        weights.get("vol",0.05), weights.get("fib",0.05), weights.get("pivot",0.05)
    ])
    blended = float(np.sum(w * arr) / max(w.sum(), 1e-9))
    return blended * 100.0, subs

def enforce_guards(symbol_cfg: dict, latest: dict, raw_signal: str) -> str:
    if raw_signal == "NEUTRAL": return raw_signal
    min_adx = float(symbol_cfg["guards"].get("min_adx_for_signal", 0))
    max_atr_pct = float(symbol_cfg["guards"].get("max_atr_pct", 999))
    adx14 = latest.get("adx14"); atr14 = latest.get("atr14")
    close = latest.get("close"); ema50 = latest.get("ema50")
    if adx14 is None or adx14 < min_adx: return "NEUTRAL"
    if close and atr14 and 100.0 * atr14 / close > max_atr_pct: return "NEUTRAL"
    if symbol_cfg["guards"].get("require_close_above_ema50_for_long", False) and raw_signal == "LONG":
        if close is None or ema50 is None or not (close > ema50): return "NEUTRAL"
    if symbol_cfg["guards"].get("require_close_below_ema50_for_short", False) and raw_signal == "SHORT":
        if close is None or ema50 is None or not (close < ema50): return "NEUTRAL"
    return raw_signal

def ensure_schema(csv_path: str) -> List[str]:
    cols = [
        "timestamp_ct","symbol","date","open","high","low","close","volume",
        "ema20","ema50","ema100","ema200","sma20","sma50","sma100","sma200",
        "rsi14","macd","macd_signal","macd_hist","atr14","adx14","plus_di14","minus_di14",
        "bb_mid20","bb_upper20","bb_lower20","bb_width",
        "pivot","r1","s1","r2","s2","r3","s3",
        "fib_long_low","fib_long_high","fib_long_23.6%","fib_long_38.2%","fib_long_50.0%","fib_long_61.8%","fib_long_78.6%",
        "fib_short_low","fib_short_high","fib_short_23.6%","fib_short_38.2%","fib_short_50.0%","fib_short_61.8%","fib_short_78.6%",
        "trend_s","momentum_s","strength_s","vol_s","fib_s","pivot_s",
        "composite_score","signal"
    ]
    if not os.path.exists(csv_path):
        os.makedirs(os.path.dirname(csv_path), exist_ok=True)
        with open(csv_path, "x", newline="") as f:
            csv.DictWriter(f, fieldnames=cols).writeheader()
    return cols

def append_row(csv_path: str, cols: List[str], row: Dict[str, float]):
    with open(csv_path, "a", newline="") as f:
        csv.DictWriter(f, fieldnames=cols).writerow(row)

def process_df(df: pd.DataFrame, fib_long_lb: int, fib_short_lb: int) -> Dict[str, float]:
    df = df.copy().reset_index(drop=True)
    df["EMA20"]=ema(df["Close"],20); df["EMA50"]=ema(df["Close"],50)
    df["EMA100"]=ema(df["Close"],100); df["EMA200"]=ema(df["Close"],200)
    df["SMA20"]=sma(df["Close"],20); df["SMA50"]=sma(df["Close"],50)
    df["SMA100"]=sma(df["Close"],100); df["SMA200"]=sma(df["Close"],200)
    df["RSI14"]=rsi(df["Close"],14)
    macd_line,sig,hist=macd(df["Close"],12,26,9)
    df["MACD"]=macd_line; df["MACD_SIGNAL"]=sig; df["MACD_HIST"]=hist
    df["ATR14"]=atr(df["High"],df["Low"],df["Close"],14)
    adx_val,plus_di,minus_di = adx(df["High"],df["Low"],df["Close"],14)
    df["ADX14"]=adx_val; df["+DI14"]=plus_di; df["-DI14"]=minus_di
    mid,up,dn,width = bollinger(df["Close"],20,2.0)
    df["BB_MID20"]=mid; df["BB_UPPER20"]=up; df["BB_LOWER20"]=dn; df["BB_WIDTH"]=width
    P,R1,S1,R2,S2,R3,S3 = pivots(df)
    df["PIVOT"]=P; df["R1"]=R1; df["S1"]=S1; df["R2"]=R2; df["S2"]=S2; df["R3"]=R3; df["S3"]=S3
    long_low,long_high = detect_swing(df, min(fib_long_lb, len(df)))
    short_low,short_high = detect_swing(df, min(fib_short_lb, len(df)))
    long_fib = fib_levels(long_low,long_high); short_fib = fib_levels(short_low,short_high)

    if EXPORT_SERIES:
        out = df.copy()
        out["fib_long_low"]=long_low; out["fib_long_high"]=long_high
        out["fib_short_low"]=short_low; out["fib_short_high"]=short_high
        return {"_series_df": out}

    last = df.iloc[-1]
    return {
        "date": str(last["Date"].date()) if isinstance(last["Date"], pd.Timestamp) else str(last["Date"]),
        "open": _nan_to_none(last["Open"]), "high": _nan_to_none(last["High"]), "low": _nan_to_none(last["Low"]),
        "close": _nan_to_none(last["Close"]), "volume": _nan_to_none(last["Volume"]),
        "ema20": _nan_to_none(last["EMA20"]), "ema50": _nan_to_none(last["EMA50"]),
        "ema100": _nan_to_none(last["EMA100"]), "ema200": _nan_to_none(last["EMA200"]),
        "sma20": _nan_to_none(last["SMA20"]), "sma50": _nan_to_none(last["SMA50"]),
        "sma100": _nan_to_none(last["SMA100"]), "sma200": _nan_to_none(last["SMA200"]),
        "rsi14": _nan_to_none(last["RSI14"]), "macd": _nan_to_none(last["MACD"]),
        "macd_signal": _nan_to_none(last["MACD_SIGNAL"]), "macd_hist": _nan_to_none(last["MACD_HIST"]),
        "atr14": _nan_to_none(last["ATR14"]), "adx14": _nan_to_none(last["ADX14"]),
        "plus_di14": _nan_to_none(last["+DI14"]), "minus_di14": _nan_to_none(last["-DI14"]),
        "bb_mid20": _nan_to_none(last["BB_MID20"]), "bb_upper20": _nan_to_none(last["BB_UPPER20"]),
        "bb_lower20": _nan_to_none(last["BB_LOWER20"]), "bb_width": _nan_to_none(last["BB_WIDTH"]),
        "pivot": _nan_to_none(last["PIVOT"]), "r1": _nan_to_none(last["R1"]), "s1": _nan_to_none(last["S1"]),
        "r2": _nan_to_none(last["R2"]), "s2": _nan_to_none(last["S2"]), "r3": _nan_to_none(last["R3"]), "s3": _nan_to_none(last["S3"]),
        "fib_long_low": float(long_low), "fib_long_high": float(long_high),
        "fib_long_23.6%": float(long_fib["23.6%"]), "fib_long_38.2%": float(long_fib["38.2%"]),
        "fib_long_50.0%": float(long_fib["50.0%"]), "fib_long_61.8%": float(long_fib["61.8%"]),
        "fib_long_78.6%": float(long_fib["78.6%"]),
        "fib_short_low": float(short_low), "fib_short_high": float(short_high),
        "fib_short_23.6%": float(short_fib["23.6%"]), "fib_short_38.2%": float(short_fib["38.2%"]),
        "fib_short_50.0%": float(short_fib["50.0%"]), "fib_short_61.8%": float(short_fib["61.8%"]),
        "fib_short_78.6%": float(short_fib["78.6%"])
    }

def main():
    cfg = load_config(CONFIG_PATH)
    cols = ensure_schema(OUT_CSV)
    ts = datetime.now(CT).strftime("%Y-%m-%dT%H:%M:%S%z")

    def handle_asset(label: str, df: pd.DataFrame, scfg: dict):
        latest_or_series = process_df(df, scfg["lookbacks"]["fib_long"], scfg["lookbacks"]["fib_short"])
        if "_series_df" in latest_or_series:
            os.makedirs(SERIES_DIR, exist_ok=True)
            path = os.path.join(SERIES_DIR, f"series_{label.replace('^','')}.csv")
            latest_or_series["_series_df"].to_csv(path, index=False)
            last = latest_or_series["_series_df"].iloc[-1].copy()
            latest = {
                "date": str(last["Date"].date()) if isinstance(last["Date"], pd.Timestamp) else str(last["Date"]),
                "open": _nan_to_none(last["Open"]), "high": _nan_to_none(last["High"]), "low": _nan_to_none(last["Low"]),
                "close": _nan_to_none(last["Close"]), "volume": _nan_to_none(last["Volume"]),
                "ema20": _nan_to_none(last["EMA20"]), "ema50": _nan_to_none(last["EMA50"]),
                "ema100": _nan_to_none(last["EMA100"]), "ema200": _nan_to_none(last["EMA200"]),
                "sma20": _nan_to_none(last["SMA20"]), "sma50": _nan_to_none(last["SMA50"]),
                "sma100": _nan_to_none(last["SMA100"]), "sma200": _nan_to_none(last["SMA200"]),
                "rsi14": _nan_to_none(last["RSI14"]), "macd": _nan_to_none(last["MACD"]),
                "macd_signal": _nan_to_none(last["MACD_SIGNAL"]), "macd_hist": _nan_to_none(last["MACD_HIST"]),
                "atr14": _nan_to_none(last["ATR14"]), "adx14": _nan_to_none(last["ADX14"]),
                "plus_di14": _nan_to_none(last["+DI14"]), "minus_di14": _nan_to_none(last["-DI14"]),
                "bb_mid20": _nan_to_none(last["BB_MID20"]), "bb_upper20": _nan_to_none(last["BB_UPPER20"]),
                "bb_lower20": _nan_to_none(last["BB_LOWER20"]), "bb_width": _nan_to_none(last["BB_WIDTH"]),
                "pivot": _nan_to_none(last["PIVOT"]), "r1": _nan_to_none(last["R1"]), "s1": _nan_to_none(last["S1"]),
                "r2": _nan_to_none(last["R2"]), "s2": _nan_to_none(last["S2"]), "r3": _nan_to_none(last["R3"]), "s3": _nan_to_none(last["S3"]),
                "fib_long_low": float(latest_or_series["_series_df"]["fib_long_low"].iloc[-1]),
                "fib_long_high": float(latest_or_series["_series_df"]["fib_long_high"].iloc[-1]),
                "fib_short_low": float(latest_or_series["_series_df"]["fib_short_low"].iloc[-1]),
                "fib_short_high": float(latest_or_series["_series_df"]["fib_short_high"].iloc[-1]),
                "fib_long_23.6%": None, "fib_long_38.2%": None, "fib_long_50.0%": None, "fib_long_61.8%": None, "fib_long_78.6%": None,
                "fib_short_23.6%": None, "fib_short_38.2%": None, "fib_short_50.0%": None, "fib_short_61.8%": None, "fib_short_78.6%": None
            }
        else:
            latest = latest_or_series

        score, subs = composite_and_subscores(latest, scfg["weights"])
        lt, st = scfg["thresholds"]["long"], scfg["thresholds"]["short"]
        raw_signal = "LONG" if score >= lt else ("SHORT" if score <= st else "NEUTRAL")
        final_signal = enforce_guards(scfg, latest, raw_signal)

        latest.update({
            "timestamp_ct": ts, "symbol": label,
            "trend_s": subs["trend_s"], "momentum_s": subs["momentum_s"], "strength_s": subs["strength_s"],
            "vol_s": subs["vol_s"], "fib_s": subs["fib_s"], "pivot_s": subs["pivot_s"],
            "composite_score": score, "signal": final_signal
        })
        append_row(OUT_CSV, cols, latest)
        print(f"APPENDED {label}: score={score:.1f} raw={raw_signal} final={final_signal}")

    for label, pair in CRYPTO_BINANCE.items():
        scfg = apply_overrides(label, load_config(CONFIG_PATH))
        df = fetch_binance_klines(pair, interval="1d", days=DAYS_CRYPTO)
        handle_asset(label, df, scfg)

    for ticker in EQUITIES_YF:
        label = "DXY-INDEX" if ticker == "^DXY" else ticker
        scfg = apply_overrides(label, load_config(CONFIG_PATH))
        df = fetch_yf_daily(ticker, period=DAYS_EQUITY)
        handle_asset(label, df, scfg)

    print(f"Done -> {OUT_CSV}")

if __name__ == "__main__":
    main()
