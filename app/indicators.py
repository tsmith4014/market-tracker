"""Technical indicator computation module.

Vectorized implementations of all indicators used by the market tracker.
Separated from the main pipeline for testability and reuse.
"""
from __future__ import annotations

from typing import Dict, Tuple

import numpy as np
import pandas as pd


def ema(s: pd.Series, span: int) -> pd.Series:
    return s.ewm(span=span, adjust=False).mean()


def sma(s: pd.Series, window: int) -> pd.Series:
    return s.rolling(window, min_periods=window).mean()


def rsi(s: pd.Series, period: int = 14) -> pd.Series:
    d = s.diff()
    up = d.clip(lower=0.0)
    dn = -d.clip(upper=0.0)
    up_mean = up.rolling(period, min_periods=period).mean()
    dn_mean = dn.rolling(period, min_periods=period).mean()

    rs = up_mean / dn_mean.replace(0, np.nan)
    out = 100.0 - (100.0 / (1.0 + rs))

    pure_up = (dn_mean == 0) & (up_mean > 0)
    pure_down = (up_mean == 0) & (dn_mean > 0)
    pure_flat = (up_mean == 0) & (dn_mean == 0)
    out = out.where(~pure_up, 100.0)
    out = out.where(~pure_down, 0.0)
    out = out.where(~pure_flat, 50.0)
    return out


def macd(s: pd.Series, fast: int = 12, slow: int = 26, signal: int = 9) -> Tuple[pd.Series, pd.Series, pd.Series]:
    line = ema(s, fast) - ema(s, slow)
    sig = ema(line, signal)
    return line, sig, line - sig


def true_range(h: pd.Series, l: pd.Series, c: pd.Series) -> pd.Series:
    pc = c.shift(1)
    return pd.concat([(h - l), (h - pc).abs(), (l - pc).abs()], axis=1).max(axis=1)


def atr(h: pd.Series, l: pd.Series, c: pd.Series, period: int = 14) -> pd.Series:
    return true_range(h, l, c).rolling(period, min_periods=period).mean()


def adx(h: pd.Series, l: pd.Series, c: pd.Series, period: int = 14) -> Tuple[pd.Series, pd.Series, pd.Series]:
    up = h.diff()
    dn = -l.diff()
    plus_dm = np.where((up > dn) & (up > 0), up, 0.0)
    minus_dm = np.where((dn > up) & (dn > 0), dn, 0.0)
    atr_n = true_range(h, l, c).rolling(period, min_periods=period).mean().replace(0, np.nan)
    plus_di = 100 * (pd.Series(plus_dm, index=h.index).rolling(period, min_periods=period).sum() / atr_n)
    minus_di = 100 * (pd.Series(minus_dm, index=h.index).rolling(period, min_periods=period).sum() / atr_n)
    dx = (plus_di.subtract(minus_di).abs() / (plus_di + minus_di).replace(0, np.nan)) * 100
    return dx.rolling(period, min_periods=period).mean(), plus_di, minus_di


def bollinger(s: pd.Series, window: int = 20, nstd: float = 2.0) -> Tuple[pd.Series, pd.Series, pd.Series, pd.Series]:
    mid = s.rolling(window, min_periods=window).mean()
    std = s.rolling(window, min_periods=window).std()
    up = mid + nstd * std
    dn = mid - nstd * std
    return mid, up, dn, (up - dn) / mid.replace(0, np.nan)


def pivots(df: pd.DataFrame) -> Tuple[pd.Series, pd.Series, pd.Series, pd.Series, pd.Series, pd.Series, pd.Series]:
    prev = df.shift(1)
    p = (prev["High"] + prev["Low"] + prev["Close"]) / 3.0
    r1 = 2 * p - prev["Low"]
    s1 = 2 * p - prev["High"]
    r2 = p + (prev["High"] - prev["Low"])
    s2 = p - (prev["High"] - prev["Low"])
    r3 = prev["High"] + 2 * (p - prev["Low"])
    s3 = prev["Low"] - 2 * (prev["High"] - p)
    return p, r1, s1, r2, s2, r3, s3


def vwap(df: pd.DataFrame, period: int = 20) -> pd.Series:
    """Rolling VWAP over the given period."""
    typical_price = (df["High"] + df["Low"] + df["Close"]) / 3.0
    vol = df["Volume"].replace(0, np.nan)
    tp_vol = typical_price * vol
    return tp_vol.rolling(period, min_periods=1).sum() / vol.rolling(period, min_periods=1).sum()


def relative_volume(df: pd.DataFrame, period: int = 20) -> pd.Series:
    """Volume relative to its rolling average. >1 means above-average volume."""
    avg_vol = df["Volume"].rolling(period, min_periods=period).mean()
    return df["Volume"] / avg_vol.replace(0, np.nan)


def rate_of_change(s: pd.Series, period: int = 10) -> pd.Series:
    """Price rate of change as a percentage."""
    return s.pct_change(periods=period) * 100.0


def obv(close: pd.Series, volume: pd.Series) -> pd.Series:
    """On-Balance Volume."""
    direction = np.sign(close.diff())
    return (volume * direction).fillna(0).cumsum()


def stochastic_rsi(s: pd.Series, rsi_period: int = 14, stoch_period: int = 14) -> pd.Series:
    """Stochastic RSI - RSI of RSI, normalized to 0-100."""
    rsi_values = rsi(s, rsi_period)
    min_rsi = rsi_values.rolling(stoch_period, min_periods=stoch_period).min()
    max_rsi = rsi_values.rolling(stoch_period, min_periods=stoch_period).max()
    rng = (max_rsi - min_rsi).replace(0, np.nan)
    return ((rsi_values - min_rsi) / rng) * 100.0


def momentum_divergence(close: pd.Series, rsi_series: pd.Series, lookback: int = 14) -> pd.Series:
    """Detect divergence between price and RSI.

    Returns:
        +1: bullish divergence (price making lower lows, RSI making higher lows)
        -1: bearish divergence (price making higher highs, RSI making lower highs)
         0: no divergence
    """
    price_change = close.diff(lookback)
    rsi_change = rsi_series.diff(lookback)

    bullish = (price_change < 0) & (rsi_change > 0)
    bearish = (price_change > 0) & (rsi_change < 0)

    result = pd.Series(0.0, index=close.index)
    result = result.where(~bullish, 1.0)
    result = result.where(~bearish, -1.0)
    return result


def detect_swing(df: pd.DataFrame, lookback: int) -> Tuple[float, float]:
    window = df.tail(lookback)
    highs, lows = window["High"], window["Low"]
    best_low = float(lows.iloc[0])
    best_high = float(highs.iloc[0])
    best_move = 0.0
    low_so_far = best_low
    high_so_far = best_high
    for _, row in window.iterrows():
        high = float(row["High"])
        low = float(row["Low"])
        up_move = (high - low_so_far) / max(low_so_far, 1e-9)
        if up_move > best_move:
            best_move, best_low, best_high = up_move, low_so_far, high
        down_move = (high_so_far - low) / max(high_so_far, 1e-9)
        if down_move > best_move:
            best_move, best_low, best_high = down_move, low, high_so_far
        low_so_far = min(low_so_far, low)
        high_so_far = max(high_so_far, high)
    lo, hi = min(best_low, best_high), max(best_low, best_high)
    return (float(lows.min()), float(highs.max())) if hi <= lo else (lo, hi)


def fib_levels(low: float, high: float) -> Dict[str, float]:
    if not np.isfinite(low) or not np.isfinite(high) or high <= low:
        return {k: np.nan for k in ["23.6%", "38.2%", "50.0%", "61.8%", "78.6%"]}
    return {f"{level * 100:.1f}%": high - (high - low) * level for level in [0.236, 0.382, 0.5, 0.618, 0.786]}


def weekly_trend_alignment(df: pd.DataFrame) -> pd.Series:
    """Compute weekly EMA trend and map it back to daily bars.

    Returns a series with values:
        +1: weekly trend is bullish (close > weekly EMA20)
        -1: weekly trend is bearish (close < weekly EMA20)
         0: insufficient data
    """
    df_copy = df[["Date", "Close"]].copy()
    df_copy = df_copy.set_index("Date")
    weekly = df_copy.resample("W-FRI").agg({"Close": "last"}).dropna()
    if len(weekly) < 20:
        return pd.Series(0.0, index=df.index)
    weekly["ema20w"] = ema(weekly["Close"], 20)
    weekly["trend"] = np.where(weekly["Close"] > weekly["ema20w"], 1.0, -1.0)
    weekly_trend = weekly["trend"].reindex(df_copy.index, method="ffill").fillna(0.0)
    weekly_trend.index = df.index
    return weekly_trend


def compute_all_indicators(df: pd.DataFrame, fib_long_lb: int, fib_short_lb: int) -> pd.DataFrame:
    """Compute the full indicator suite on prepared OHLCV data."""
    d = df.copy()

    # Moving averages
    d["EMA20"] = ema(d["Close"], 20)
    d["EMA50"] = ema(d["Close"], 50)
    d["EMA100"] = ema(d["Close"], 100)
    d["EMA200"] = ema(d["Close"], 200)
    d["SMA20"] = sma(d["Close"], 20)
    d["SMA50"] = sma(d["Close"], 50)
    d["SMA100"] = sma(d["Close"], 100)
    d["SMA200"] = sma(d["Close"], 200)

    # Momentum
    d["RSI14"] = rsi(d["Close"], 14)
    m, sig, hist = macd(d["Close"])
    d["MACD"] = m
    d["MACD_SIGNAL"] = sig
    d["MACD_HIST"] = hist

    # Volatility and trend strength
    d["ATR14"] = atr(d["High"], d["Low"], d["Close"], 14)
    av, pdi, mdi = adx(d["High"], d["Low"], d["Close"], 14)
    d["ADX14"] = av
    d["+DI14"] = pdi
    d["-DI14"] = mdi
    bmid, bup, bdn, bw = bollinger(d["Close"], 20, 2.0)
    d["BB_MID20"] = bmid
    d["BB_UPPER20"] = bup
    d["BB_LOWER20"] = bdn
    d["BB_WIDTH"] = bw

    # Pivot points
    p, r1, s1, r2, s2, r3, s3 = pivots(d)
    d["PIVOT"] = p
    d["R1"] = r1
    d["S1"] = s1
    d["R2"] = r2
    d["S2"] = s2
    d["R3"] = r3
    d["S3"] = s3

    # Volume indicators
    has_volume = d["Volume"].notna().any() and (d["Volume"] > 0).any()
    if has_volume:
        d["VWAP20"] = vwap(d, 20)
        d["RVOL"] = relative_volume(d, 20)
        d["OBV"] = obv(d["Close"], d["Volume"])
    else:
        d["VWAP20"] = np.nan
        d["RVOL"] = np.nan
        d["OBV"] = np.nan

    # Rate of change
    d["ROC10"] = rate_of_change(d["Close"], 10)
    d["ROC20"] = rate_of_change(d["Close"], 20)

    # Stochastic RSI
    d["STOCH_RSI"] = stochastic_rsi(d["Close"], 14, 14)

    # Momentum divergence
    d["MOM_DIVERGENCE"] = momentum_divergence(d["Close"], d["RSI14"], 14)

    # Multi-timeframe: weekly trend alignment
    d["WEEKLY_TREND"] = weekly_trend_alignment(d)

    # Fibonacci levels
    for prefix, lb in (("fib_long", fib_long_lb), ("fib_short", fib_short_lb)):
        lows, highs, levels = [], [], []
        for idx in range(len(d)):
            if idx + 1 < lb:
                lo, hi, lev = np.nan, np.nan, fib_levels(np.nan, np.nan)
            else:
                lo, hi = detect_swing(d.iloc[:idx + 1], lb)
                lev = fib_levels(lo, hi)
            lows.append(lo)
            highs.append(hi)
            levels.append(lev)
        d[f"{prefix}_low"] = lows
        d[f"{prefix}_high"] = highs
        for name in ["23.6%", "38.2%", "50.0%", "61.8%", "78.6%"]:
            d[f"{prefix}_{name}"] = [x[name] for x in levels]

    return d
