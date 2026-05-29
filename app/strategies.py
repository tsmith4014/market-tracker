"""Signal-generation strategies.

The production composite score is pure trend-following, which the backtest on
real 2024-2026 data showed badly underperforms buy-and-hold (it chases breakouts
and gets whipsawed in chop). These pluggable strategies let us A/B alternative
decision rules over the *same* indicator data, so a variant with measured edge
can be selected via config instead of guessed at.

Strategies are intentionally parameter-light (fixed, motivated thresholds) to
limit overfitting across the 161-symbol universe.
"""
from __future__ import annotations

from typing import Optional

import numpy as np

TREND = "trend"
MEAN_REVERSION = "mean_reversion"
REGIME_ADAPTIVE = "regime_adaptive"
STRATEGIES = (TREND, MEAN_REVERSION, REGIME_ADAPTIVE)

# ADX above this marks a trending regime; below it the market is chopping.
ADX_TREND_FLOOR = 25.0
# Mean-reversion RSI bands.
MR_RSI_LOW = 30.0
MR_RSI_HIGH = 70.0


def _f(x) -> Optional[float]:
    try:
        v = float(x)
    except (TypeError, ValueError):
        return None
    return v if np.isfinite(v) else None


def trend_signal(score: Optional[float], long_th: float, short_th: float) -> str:
    """Breakout/trend rule: act in the direction of a strong composite score."""
    if score is None:
        return "NEUTRAL"
    if score >= long_th:
        return "LONG"
    if score <= short_th:
        return "SHORT"
    return "NEUTRAL"


def mean_reversion_signal(
    close: Optional[float],
    rsi14: Optional[float],
    bb_lower20: Optional[float],
    bb_upper20: Optional[float],
    ema200: Optional[float],
    rsi_low: float = MR_RSI_LOW,
    rsi_high: float = MR_RSI_HIGH,
) -> str:
    """Fade extremes, but only with the longer-term trend.

    Buy oversold pullbacks inside an uptrend (close >= EMA200); sell overbought
    rallies inside a downtrend. The trend filter avoids catching falling knives.
    """
    if close is None or rsi14 is None:
        return "NEUTRAL"
    in_uptrend = ema200 is None or close >= ema200
    in_downtrend = ema200 is None or close <= ema200
    oversold = rsi14 <= rsi_low and (bb_lower20 is None or close <= bb_lower20)
    overbought = rsi14 >= rsi_high and (bb_upper20 is None or close >= bb_upper20)
    if oversold and in_uptrend:
        return "LONG"
    if overbought and in_downtrend:
        return "SHORT"
    return "NEUTRAL"


def raw_signal(
    strategy: str,
    *,
    score: Optional[float],
    long_th: float,
    short_th: float,
    close: Optional[float],
    rsi14: Optional[float],
    bb_lower20: Optional[float],
    bb_upper20: Optional[float],
    ema200: Optional[float],
    adx14: Optional[float],
) -> str:
    """Dispatch to the configured strategy and return LONG/SHORT/NEUTRAL."""
    if strategy == TREND:
        return trend_signal(score, long_th, short_th)
    if strategy == MEAN_REVERSION:
        return mean_reversion_signal(close, rsi14, bb_lower20, bb_upper20, ema200)
    if strategy == REGIME_ADAPTIVE:
        # Trend-follow when a trend is established, fade extremes when chopping.
        if adx14 is not None and adx14 >= ADX_TREND_FLOOR:
            return trend_signal(score, long_th, short_th)
        return mean_reversion_signal(close, rsi14, bb_lower20, bb_upper20, ema200)
    raise ValueError(f"Unknown strategy: {strategy}")


def uses_trend_guards(strategy: str, adx14: Optional[float]) -> bool:
    """Whether trend-style guards (ADX floor, EMA proximity) apply to a row.

    Mean-reversion deliberately fires in low-ADX chop, so the trend ADX floor
    must not gate it. The adaptive strategy uses trend guards only on the rows
    where it actually took the trend branch.
    """
    if strategy == TREND:
        return True
    if strategy == MEAN_REVERSION:
        return False
    if strategy == REGIME_ADAPTIVE:
        return adx14 is not None and adx14 >= ADX_TREND_FLOOR
    return True
