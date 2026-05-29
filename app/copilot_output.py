"""Structured JSON output for trade co-pilot consumption.

Generates a machine-readable JSON payload with:
- Latest signals with confidence levels
- Market regime classification
- Data quality metadata
- Source reliability stats
- Actionable summary optimized for LLM consumption
"""
from __future__ import annotations

import json
import math
from datetime import datetime, timezone
from pathlib import Path
from typing import List
from zoneinfo import ZoneInfo

import numpy as np
import pandas as pd

# Reference timezones for deciding whether a daily bar has settled.
_CRYPTO_TZ = ZoneInfo("UTC")
_EQUITY_TZ = ZoneInfo("America/New_York")
# A bar older than this many days is considered stale (accounts for weekends/holidays).
_STALE_DAYS = {"crypto": 2, "stock": 4, "index": 4}


def assess_bar_recency(
    bar_date: str | None,
    asset_type: str,
    now: datetime | None = None,
) -> dict:
    """Decide whether the latest daily bar is settled and how stale it is.

    Crypto days settle at 00:00 UTC; equities settle on the US/Eastern calendar.
    A bar dated today (in the reference timezone) is still in progress, so any
    signal computed from it can change before the day closes.
    """
    now = now or datetime.now(timezone.utc)
    tz = _CRYPTO_TZ if asset_type == "crypto" else _EQUITY_TZ
    today_ref = now.astimezone(tz).date()

    if not bar_date:
        return {"bar_date": None, "bar_age_days": None, "bar_complete": None, "stale": None}

    try:
        parsed = datetime.fromisoformat(str(bar_date)).date()
    except (ValueError, TypeError):
        return {"bar_date": bar_date, "bar_age_days": None, "bar_complete": None, "stale": None}

    age_days = (today_ref - parsed).days
    stale_threshold = _STALE_DAYS.get(asset_type, 4)
    return {
        "bar_date": parsed.isoformat(),
        "bar_age_days": age_days,
        "bar_complete": age_days >= 1,
        "stale": age_days > stale_threshold,
    }


class CopilotEncoder(json.JSONEncoder):
    """Handle numpy/pandas types in JSON serialization."""

    def encode(self, obj):
        return super().encode(self._sanitize(obj))

    def _sanitize(self, obj):
        if isinstance(obj, dict):
            return {k: self._sanitize(v) for k, v in obj.items()}
        if isinstance(obj, list):
            return [self._sanitize(v) for v in obj]
        if isinstance(obj, (np.integer,)):
            return int(obj)
        if isinstance(obj, (np.floating,)):
            return float(obj) if np.isfinite(obj) else None
        if isinstance(obj, float):
            if not np.isfinite(obj):
                return None
            return obj
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        if isinstance(obj, pd.Timestamp):
            return obj.isoformat()
        if obj is not None and isinstance(obj, float) and np.isnan(obj):
            return None
        return obj

    def default(self, obj):
        if isinstance(obj, (np.integer,)):
            return int(obj)
        if isinstance(obj, (np.floating,)):
            return float(obj) if np.isfinite(obj) else None
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        if isinstance(obj, pd.Timestamp):
            return obj.isoformat()
        return super().default(obj)


def build_signal_payload(
    symbol: str,
    row: dict,
    confidence_level: str,
    confidence_score: float,
    quality_grade: str,
    source: str,
    asset_type: str = "crypto",
    now: datetime | None = None,
) -> dict:
    """Build a single symbol's signal payload for the co-pilot."""

    recency = assess_bar_recency(row.get("date"), asset_type, now)

    close = row.get("close")
    ema20 = row.get("ema20")
    ema50 = row.get("ema50")
    ema200 = row.get("ema200")
    atr14 = row.get("atr14")

    # Compute key levels for trade planning
    levels = {}
    if close and atr14 and np.isfinite(atr14):
        levels["atr_stop_long"] = _round_price(close - 2.0 * atr14)
        levels["atr_stop_short"] = _round_price(close + 2.0 * atr14)
        levels["atr_target_1r"] = _round_price(close + 2.0 * atr14)
        levels["atr_target_2r"] = _round_price(close + 4.0 * atr14)

    if row.get("pivot") and np.isfinite(row.get("pivot", np.nan)):
        levels["pivot"] = _round_price(row["pivot"])
        levels["r1"] = _round_price(row.get("r1")) if row.get("r1") and np.isfinite(row.get("r1", np.nan)) else None
        levels["s1"] = _round_price(row.get("s1")) if row.get("s1") and np.isfinite(row.get("s1", np.nan)) else None

    # Position in range (0=at support, 1=at resistance)
    fib_low = row.get("fib_long_low")
    fib_high = row.get("fib_long_high")
    range_position = None
    if fib_low and fib_high and close and fib_high > fib_low:
        range_position = round((close - fib_low) / (fib_high - fib_low), 3)

    return {
        "symbol": symbol,
        "signal": row.get("signal", "NEUTRAL"),
        "composite_score": _safe_round(row.get("composite_score"), 2),
        "confidence": {
            "level": confidence_level,
            "score": confidence_score,
        },
        "price": {
            "close": _round_price(close),
            "change_pct_1d": _safe_round(row.get("roc1"), 2),
            "change_pct_10d": _safe_round(row.get("roc10"), 2),
            "range_position": range_position,
        },
        "indicators": {
            "rsi14": _safe_round(row.get("rsi14"), 2),
            "macd_hist": _safe_round(row.get("macd_hist"), 4),
            "adx14": _safe_round(row.get("adx14"), 2),
            "atr_pct": _safe_round(100.0 * atr14 / close, 2) if close and atr14 else None,
            "bb_width": _safe_round(row.get("bb_width"), 4),
            "rvol": _safe_round(row.get("rvol"), 2),
            "stoch_rsi": _safe_round(row.get("stoch_rsi"), 2),
            "mom_divergence": row.get("mom_divergence"),
            "weekly_trend": _weekly_label(row.get("weekly_trend")),
        },
        "subscores": {
            "trend": _safe_round(row.get("trend_s"), 2),
            "momentum": _safe_round(row.get("momentum_s"), 2),
            "strength": _safe_round(row.get("strength_s"), 2),
            "volatility": _safe_round(row.get("vol_s"), 2),
            "fibonacci": _safe_round(row.get("fib_s"), 2),
            "pivot": _safe_round(row.get("pivot_s"), 2),
            "volume": _safe_round(row.get("volume_s"), 2),
        },
        "levels": levels,
        "moving_averages": {
            "ema20": _round_price(ema20),
            "ema50": _round_price(ema50),
            "ema200": _round_price(ema200),
            "vwap20": _round_price(row.get("vwap")),
        },
        "meta": {
            "data_source": source,
            "quality_grade": quality_grade,
            "date": row.get("date"),
            "bar_complete": recency["bar_complete"],
            "bar_age_days": recency["bar_age_days"],
            "stale": recency["stale"],
        },
    }


def build_copilot_payload(
    signals: List[dict],
    regime: dict,
    quality_reports: List[dict],
    source_reliability: List[dict],
    run_timestamp: str,
    positioning: dict | None = None,
) -> dict:
    """Build the complete co-pilot JSON payload."""

    # Generate actionable summary
    longs = [s for s in signals if s["signal"] == "LONG"]
    shorts = [s for s in signals if s["signal"] == "SHORT"]
    high_conf_longs = [s for s in longs if s["confidence"]["level"] == "HIGH"]
    high_conf_shorts = [s for s in shorts if s["confidence"]["level"] == "HIGH"]

    partial_bar = [s["symbol"] for s in signals if s.get("meta", {}).get("bar_complete") is False]
    stale = [s["symbol"] for s in signals if s.get("meta", {}).get("stale") is True]

    summary = {
        "total_symbols": len(signals),
        "long_signals": len(longs),
        "short_signals": len(shorts),
        "neutral_signals": len(signals) - len(longs) - len(shorts),
        "high_confidence_longs": [s["symbol"] for s in high_conf_longs],
        "high_confidence_shorts": [s["symbol"] for s in high_conf_shorts],
        "partial_bar_symbols": partial_bar,
        "stale_symbols": stale,
        "regime": regime.get("regime", "UNKNOWN"),
        "regime_risk_score": regime.get("risk_score", 0),
    }

    return {
        "version": "2.1",
        "generated_at": run_timestamp,
        "summary": summary,
        "market_regime": regime,
        "positioning": positioning or {},
        "signals": signals,
        "data_quality": quality_reports,
        "source_reliability": source_reliability,
    }


def write_copilot_json(payload: dict, path: str) -> None:
    """Write the co-pilot payload to a JSON file."""
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(payload, indent=2, cls=CopilotEncoder), encoding="utf-8")


def write_latest_signals_json(signals: List[dict], path: str) -> None:
    """Write a slim latest-signals-only file for quick polling."""
    slim = []
    for s in signals:
        slim.append({
            "symbol": s["symbol"],
            "signal": s["signal"],
            "score": s["composite_score"],
            "confidence": s["confidence"]["level"],
            "confidence_score": s["confidence"]["score"],
            "close": s["price"]["close"],
            "atr_pct": s["indicators"]["atr_pct"],
            "rsi14": s["indicators"]["rsi14"],
            "bar_complete": s.get("meta", {}).get("bar_complete"),
            "stale": s.get("meta", {}).get("stale"),
        })
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)
    payload = {
        "generated_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "signals": slim,
    }
    p.write_text(json.dumps(payload, indent=2, cls=CopilotEncoder), encoding="utf-8")


def _safe_round(val, digits: int) -> float | None:
    if val is None or (isinstance(val, float) and not np.isfinite(val)):
        return None
    try:
        return round(float(val), digits)
    except (TypeError, ValueError):
        return None


def _round_price(val) -> float | None:
    """Round a price with precision scaled to its magnitude.

    Fixed 4-decimal rounding collapses sub-cent assets (SHIB, PEPE, BONK) to
    0.0. Scale the precision so micro-priced tokens keep meaningful digits.
    """
    if val is None or (isinstance(val, float) and not np.isfinite(val)):
        return None
    try:
        v = float(val)
    except (TypeError, ValueError):
        return None
    a = abs(v)
    if a == 0:
        return 0.0
    if a >= 1:
        digits = 4
    elif a >= 0.01:
        digits = 6
    else:
        # Keep ~5 significant figures for very small prices.
        digits = min(15, 4 - int(math.floor(math.log10(a))))
    return round(v, digits)


def _weekly_label(val) -> str | None:
    if val is None or (isinstance(val, float) and not np.isfinite(val)):
        return None
    if val > 0:
        return "BULLISH"
    elif val < 0:
        return "BEARISH"
    return "NEUTRAL"
