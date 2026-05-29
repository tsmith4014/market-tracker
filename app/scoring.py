"""Signal scoring engine with confidence estimation.

Computes composite scores from technical indicators and assigns
confidence levels for downstream consumption by trade co-pilots.
"""
from __future__ import annotations

from typing import Dict, Optional, Tuple

import numpy as np
import pandas as pd


def finite_or_none(x) -> Optional[float]:
    if x is None or pd.isna(x) or not np.isfinite(x):
        return None
    return float(x)


def score_trend(close, ema20, ema50, ema200, slope20, slope50, slope200) -> float:
    s = 0.0
    s += 1 if close is not None and ema20 is not None and close > ema20 else -1
    s += 1 if close is not None and ema50 is not None and close > ema50 else -1
    s += 1.5 if close is not None and ema200 is not None and close > ema200 else -1.5
    s += 0.5 if slope20 > 0 else -0.5
    s += 0.5 if slope50 > 0 else -0.5
    s += 1.0 if slope200 > 0 else -1.0
    return max(-5.0, min(5.0, s))


def score_momentum(rsi14, macd_value, macd_signal, stoch_rsi=None, mom_divergence=None) -> float:
    s = 0.0
    if rsi14 is not None:
        if 50 <= rsi14 <= 70:
            s += 1.0
        elif 30 <= rsi14 < 50:
            s -= 0.5
        elif rsi14 > 70:
            s += 0.5
        elif rsi14 < 30:
            s -= 1.0
    if macd_value is not None and macd_signal is not None:
        s += 1.0 if macd_value > macd_signal else -1.0
        s += 0.5 if macd_value > 0 else -0.5
    if stoch_rsi is not None:
        if stoch_rsi > 80:
            s += 0.25
        elif stoch_rsi < 20:
            s -= 0.25
    if mom_divergence is not None and mom_divergence != 0:
        s += 0.5 * mom_divergence
    return max(-3.0, min(3.0, s))


def score_strength(adx14, plus_di, minus_di) -> float:
    if adx14 is None or plus_di is None or minus_di is None:
        return 0.0
    return max(-2.0, min(2.0, (1.0 if adx14 >= 25 else -0.5) + (0.5 if plus_di > minus_di else -0.5)))


def score_volatility(atr14, close, bb_width) -> float:
    s = 0.0
    if atr14 is not None and close:
        atrp = 100.0 * atr14 / close
        if atrp < 2.0:
            s += 0.5
        elif atrp < 5.0:
            s += 0.25
        elif atrp >= 8.0:
            s -= 0.5
    if bb_width is not None:
        if bb_width < 0.05:
            s += 0.25
        elif bb_width > 0.25:
            s -= 0.25
    return max(-1.0, min(1.0, s))


def score_fib(close, low, high) -> float:
    if any(v is None for v in [close, low, high]) or high <= low:
        return 0.0
    f38 = high - (high - low) * 0.382
    f50 = high - (high - low) * 0.5
    f62 = high - (high - low) * 0.618
    if min(f38, f62) <= close <= max(f38, f62):
        return 1.0
    return 0.5 if abs(close - f50) <= 0.01 * f50 else -0.25


def score_pivot(close, pivot, r1, s1) -> float:
    if pivot is None or r1 is None or s1 is None or close is None:
        return 0.0
    s = 0.5 if close > pivot else -0.5
    if close > r1:
        s += 0.25
    if close < s1:
        s -= 0.25
    return max(-1.0, min(1.0, s))


def score_volume(rvol, close, vwap, roc10) -> float:
    """Score based on volume confirmation of price moves."""
    s = 0.0
    if rvol is not None:
        if rvol > 1.5:
            s += 0.5 if roc10 is not None and roc10 > 0 else -0.25
        elif rvol < 0.5:
            s -= 0.25
    if close is not None and vwap is not None:
        if close > vwap:
            s += 0.25
        elif close < vwap:
            s -= 0.25
    return max(-1.0, min(1.0, s))


def latest_dict(row: pd.Series) -> Dict[str, float]:
    return {
        "close": row.get("Close"),
        "ema20": row.get("EMA20"),
        "ema50": row.get("EMA50"),
        "ema200": row.get("EMA200"),
        "sma20": row.get("SMA20"),
        "sma50": row.get("SMA50"),
        "sma200": row.get("SMA200"),
        "rsi14": row.get("RSI14"),
        "macd": row.get("MACD"),
        "macd_signal": row.get("MACD_SIGNAL"),
        "adx14": row.get("ADX14"),
        "plus_di14": row.get("+DI14"),
        "minus_di14": row.get("-DI14"),
        "atr14": row.get("ATR14"),
        "bb_width": row.get("BB_WIDTH"),
        "pivot": row.get("PIVOT"),
        "r1": row.get("R1"),
        "s1": row.get("S1"),
        "fib_long_low": row.get("fib_long_low"),
        "fib_long_high": row.get("fib_long_high"),
        "stoch_rsi": row.get("STOCH_RSI"),
        "mom_divergence": row.get("MOM_DIVERGENCE"),
        "rvol": row.get("RVOL"),
        "vwap": row.get("VWAP20"),
        "roc10": row.get("ROC10"),
        "weekly_trend": row.get("WEEKLY_TREND"),
    }


def composite_and_subscores(latest: Dict[str, float], weights: dict) -> Tuple[float, Dict[str, float]]:
    close = finite_or_none(latest.get("close"))
    ema20 = finite_or_none(latest.get("ema20"))
    ema50 = finite_or_none(latest.get("ema50"))
    ema200 = finite_or_none(latest.get("ema200"))
    sma20 = finite_or_none(latest.get("sma20"))
    sma50 = finite_or_none(latest.get("sma50"))
    sma200 = finite_or_none(latest.get("sma200"))

    subs = {
        "trend_s": score_trend(
            close, ema20, ema50, ema200,
            (ema20 or 0) - (sma20 or 0),
            (ema50 or 0) - (sma50 or 0),
            (ema200 or 0) - (sma200 or 0),
        ),
        "momentum_s": score_momentum(
            finite_or_none(latest.get("rsi14")),
            finite_or_none(latest.get("macd")),
            finite_or_none(latest.get("macd_signal")),
            finite_or_none(latest.get("stoch_rsi")),
            finite_or_none(latest.get("mom_divergence")),
        ),
        "strength_s": score_strength(
            finite_or_none(latest.get("adx14")),
            finite_or_none(latest.get("plus_di14")),
            finite_or_none(latest.get("minus_di14")),
        ),
        "vol_s": score_volatility(
            finite_or_none(latest.get("atr14")),
            close,
            finite_or_none(latest.get("bb_width")),
        ),
        "fib_s": score_fib(
            close,
            finite_or_none(latest.get("fib_long_low")),
            finite_or_none(latest.get("fib_long_high")),
        ),
        "pivot_s": score_pivot(
            close,
            finite_or_none(latest.get("pivot")),
            finite_or_none(latest.get("r1")),
            finite_or_none(latest.get("s1")),
        ),
        "volume_s": score_volume(
            finite_or_none(latest.get("rvol")),
            close,
            finite_or_none(latest.get("vwap")),
            finite_or_none(latest.get("roc10")),
        ),
    }

    caps = {
        "trend_s": 5, "momentum_s": 3, "strength_s": 2,
        "vol_s": 1, "fib_s": 1, "pivot_s": 1, "volume_s": 1,
    }
    wm = {
        "trend_s": "trend", "momentum_s": "momentum", "strength_s": "strength",
        "vol_s": "vol", "fib_s": "fib", "pivot_s": "pivot", "volume_s": "volume",
    }

    # A subscore always returns a finite value (0.0 when inputs are missing), so we
    # track availability from the underlying inputs. Unavailable subscores are dropped
    # and the remaining weights renormalized, rather than letting a missing indicator
    # cast a diluting "neutral" vote.
    rvol = finite_or_none(latest.get("rvol"))
    vwap = finite_or_none(latest.get("vwap"))
    available = {
        "trend_s": close is not None and any(x is not None for x in (ema20, ema50, ema200)),
        "momentum_s": finite_or_none(latest.get("rsi14")) is not None or finite_or_none(latest.get("macd")) is not None,
        "strength_s": finite_or_none(latest.get("adx14")) is not None,
        "vol_s": (finite_or_none(latest.get("atr14")) is not None and close is not None)
        or finite_or_none(latest.get("bb_width")) is not None,
        "fib_s": close is not None
        and finite_or_none(latest.get("fib_long_low")) is not None
        and finite_or_none(latest.get("fib_long_high")) is not None,
        "pivot_s": close is not None and finite_or_none(latest.get("pivot")) is not None,
        "volume_s": rvol is not None or (close is not None and vwap is not None),
    }

    valid = {k: v for k, v in subs.items() if np.isfinite(v) and available[k]}
    total = sum(float(weights.get(wm[k], 0)) for k in valid)
    if not valid or total <= 0:
        return np.nan, subs
    return sum((valid[k] / caps[k]) * (float(weights.get(wm[k], 0)) / total) for k in valid) * 100.0, subs


def enforce_guards(scfg: dict, latest: dict, raw_signal: str, strategy: str = "trend") -> str:
    if raw_signal == "NEUTRAL":
        return raw_signal
    adx14 = finite_or_none(latest.get("adx14"))
    atr14 = finite_or_none(latest.get("atr14"))
    close = finite_or_none(latest.get("close"))
    ema50 = finite_or_none(latest.get("ema50"))

    # Extreme-volatility guard applies to every strategy.
    if close and atr14 and 100.0 * atr14 / close > float(scfg["guards"].get("max_atr_pct", 999)):
        return "NEUTRAL"
    # Trend-style guards (ADX floor, EMA proximity) gate only trend-driven rows.
    # Mean-reversion deliberately fires in low-ADX chop, so they must not apply.
    trend_guarded = strategy == "trend" or (strategy == "regime_adaptive" and adx14 is not None and adx14 >= 25.0)
    if not trend_guarded:
        return raw_signal
    if adx14 is None or adx14 < float(scfg["guards"].get("min_adx_for_signal", 0)):
        return "NEUTRAL"
    if scfg["guards"].get("require_close_above_ema50_for_long", False) and raw_signal == "LONG":
        if close is None or ema50 is None or close <= ema50:
            return "NEUTRAL"
    if scfg["guards"].get("require_close_below_ema50_for_short", False) and raw_signal == "SHORT":
        if close is None or ema50 is None or close >= ema50:
            return "NEUTRAL"
    return raw_signal


def compute_confidence(
    score: float,
    subs: Dict[str, float],
    latest: Dict[str, float],
    thresholds: dict,
    signal: str | None = None,
) -> Tuple[str, float]:
    """Compute signal confidence level and numeric confidence score.

    Confidence is based on:
    - How far the composite score is from the threshold (margin)
    - Whether multiple subscores agree on direction (confluence)
    - Whether weekly trend aligns with the signal
    - Volume confirmation

    A penalty is applied for "stretched" entries (going LONG when already very
    overbought, or SHORT when already very oversold) because those chase a move
    that has mostly happened. If the guarded signal is NEUTRAL there is nothing
    actionable, so confidence collapses to LOW/0.

    Returns:
        (level, numeric) where level is HIGH/MEDIUM/LOW and numeric is 0.0 to 1.0
    """
    if not np.isfinite(score):
        return "LOW", 0.0
    if signal == "NEUTRAL":
        return "LOW", 0.0

    long_th = float(thresholds.get("long", 30))
    short_th = float(thresholds.get("short", -30))

    # Margin: how far past the threshold
    if score >= long_th:
        margin = (score - long_th) / max(100.0 - long_th, 1.0)
    elif score <= short_th:
        margin = (short_th - score) / max(100.0 + short_th, 1.0)
    else:
        margin = 0.0

    # Direction comes from the actionable signal when available, else the score.
    if signal == "LONG":
        signal_dir = 1
    elif signal == "SHORT":
        signal_dir = -1
    else:
        signal_dir = 1 if score > 0 else -1

    # Confluence: count how many subscores agree with the signal direction
    agreeing = sum(1 for v in subs.values() if np.isfinite(v) and np.sign(v) == signal_dir)
    total_subs = sum(1 for v in subs.values() if np.isfinite(v))
    confluence = agreeing / max(total_subs, 1)

    # Weekly alignment bonus
    weekly = finite_or_none(latest.get("weekly_trend"))
    weekly_bonus = 0.15 if weekly is not None and np.sign(weekly) == signal_dir else 0.0

    # Volume confirmation bonus
    rvol = finite_or_none(latest.get("rvol"))
    vol_bonus = 0.1 if rvol is not None and rvol > 1.2 else 0.0

    # Stretched-entry penalty: longing into extreme overbought or shorting into
    # extreme oversold chases a move that has largely played out.
    rsi = finite_or_none(latest.get("rsi14"))
    stretched = rsi is not None and ((signal_dir > 0 and rsi >= 80) or (signal_dir < 0 and rsi <= 20))
    stretched_penalty = 0.2 if stretched else 0.0

    numeric = max(0.0, min(1.0, margin * 0.4 + confluence * 0.35 + weekly_bonus + vol_bonus - stretched_penalty))

    if numeric >= 0.65:
        level = "HIGH"
    elif numeric >= 0.35:
        level = "MEDIUM"
    else:
        level = "LOW"

    return level, round(numeric, 3)


def compute_market_regime(scores: Dict[str, float]) -> Dict[str, str]:
    """Classify market regime from cross-asset signals.

    Looks at broad market ETFs (SPY, QQQ) and safe-havens (DXY) to
    determine if the macro environment is risk-on, risk-off, or mixed.
    """
    spy_score = scores.get("SPY")
    qqq_score = scores.get("QQQ")
    dxy_score = scores.get("DXY-INDEX")

    risk_assets = [v for v in [spy_score, qqq_score] if v is not None and np.isfinite(v)]
    risk_avg = np.mean(risk_assets) if risk_assets else 0.0

    regime = "MIXED"
    if risk_avg > 20:
        regime = "RISK_ON"
    elif risk_avg < -20:
        regime = "RISK_OFF"

    # DXY rising is typically risk-off for equities/crypto
    dxy_signal = "NEUTRAL"
    if dxy_score is not None and np.isfinite(dxy_score):
        if dxy_score > 30:
            dxy_signal = "STRONG_USD"
        elif dxy_score < -30:
            dxy_signal = "WEAK_USD"

    return {
        "regime": regime,
        "risk_score": round(float(risk_avg), 2),
        "dxy_signal": dxy_signal,
    }
