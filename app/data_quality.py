"""Data quality assessment and metadata tracking.

Provides quality scores, staleness detection, and source reliability
metrics so downstream consumers know how much to trust each data point.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Dict, List, Optional

import pandas as pd


@dataclass
class DataQualityReport:
    symbol: str
    source: str
    bars_received: int
    bars_expected: int
    completeness: float
    freshness_hours: float
    has_volume: bool
    nan_pct: float
    gap_days: List[str] = field(default_factory=list)
    quality_grade: str = "UNKNOWN"

    def to_dict(self) -> dict:
        return {
            "symbol": self.symbol,
            "source": self.source,
            "bars_received": self.bars_received,
            "bars_expected": self.bars_expected,
            "completeness": round(self.completeness, 4),
            "freshness_hours": round(self.freshness_hours, 1),
            "has_volume": self.has_volume,
            "nan_pct": round(self.nan_pct, 4),
            "gap_count": len(self.gap_days),
            "quality_grade": self.quality_grade,
        }


def assess_quality(
    df: pd.DataFrame,
    symbol: str,
    source: str,
    expected_bars: int,
    asset_type: str = "crypto",
) -> DataQualityReport:
    """Assess data quality for a single symbol's OHLCV dataframe."""
    now = datetime.now(timezone.utc)

    bars_received = len(df)
    completeness = bars_received / max(expected_bars, 1)

    last_date = pd.to_datetime(df["Date"].iloc[-1]) if not df.empty else None
    if last_date is not None:
        if last_date.tzinfo is None:
            last_date = last_date.replace(tzinfo=timezone.utc)
        freshness_hours = (now - last_date).total_seconds() / 3600.0
    else:
        freshness_hours = 9999.0

    has_volume = bool(df["Volume"].notna().any() and (df["Volume"] > 0).any())

    numeric_cols = ["Open", "High", "Low", "Close", "Volume"]
    existing_cols = [c for c in numeric_cols if c in df.columns]
    nan_pct = df[existing_cols].isna().sum().sum() / max(len(df) * len(existing_cols), 1)

    # Detect gaps (missing trading days)
    gap_days: List[str] = []
    if len(df) > 1:
        dates = pd.to_datetime(df["Date"]).sort_values()
        diffs = dates.diff().dt.days.dropna()
        if asset_type == "crypto":
            threshold = 2
        else:
            threshold = 4  # weekends are normal for stocks
        gaps = diffs[diffs > threshold]
        gap_days = [str(dates.iloc[i].date()) for i in gaps.index[:10]]

    # Grade computation
    grade = _compute_grade(completeness, freshness_hours, nan_pct, has_volume, len(gap_days), asset_type)

    return DataQualityReport(
        symbol=symbol,
        source=source,
        bars_received=bars_received,
        bars_expected=expected_bars,
        completeness=completeness,
        freshness_hours=freshness_hours,
        has_volume=has_volume,
        nan_pct=nan_pct,
        gap_days=gap_days,
        quality_grade=grade,
    )


def _compute_grade(
    completeness: float,
    freshness_hours: float,
    nan_pct: float,
    has_volume: bool,
    gap_count: int,
    asset_type: str,
) -> str:
    score = 100.0

    # Completeness penalty
    if completeness < 0.5:
        score -= 40
    elif completeness < 0.8:
        score -= 20
    elif completeness < 0.95:
        score -= 5

    # Freshness penalty
    max_stale = 48 if asset_type == "crypto" else 96
    if freshness_hours > max_stale:
        score -= 30
    elif freshness_hours > max_stale / 2:
        score -= 15

    # NaN penalty
    if nan_pct > 0.1:
        score -= 25
    elif nan_pct > 0.05:
        score -= 10

    # Volume bonus/penalty
    if not has_volume:
        score -= 10

    # Gap penalty
    if gap_count > 5:
        score -= 15
    elif gap_count > 2:
        score -= 5

    if score >= 85:
        return "A"
    elif score >= 70:
        return "B"
    elif score >= 50:
        return "C"
    else:
        return "D"


@dataclass
class SourceReliability:
    source: str
    attempts: int = 0
    successes: int = 0
    failures: int = 0
    avg_latency_ms: float = 0.0
    last_failure_reason: Optional[str] = None

    @property
    def success_rate(self) -> float:
        return self.successes / max(self.attempts, 1)

    def record_success(self, latency_ms: float) -> None:
        self.attempts += 1
        self.successes += 1
        self.avg_latency_ms = (self.avg_latency_ms * (self.successes - 1) + latency_ms) / self.successes

    def record_failure(self, reason: str) -> None:
        self.attempts += 1
        self.failures += 1
        self.last_failure_reason = reason

    def to_dict(self) -> dict:
        return {
            "source": self.source,
            "attempts": self.attempts,
            "successes": self.successes,
            "failures": self.failures,
            "success_rate": self.success_rate,
            "avg_latency_ms": round(self.avg_latency_ms, 1),
            "last_failure_reason": self.last_failure_reason,
        }


class ReliabilityTracker:
    """Track API source reliability across a pipeline run."""

    def __init__(self):
        self._sources: Dict[str, SourceReliability] = {}

    def get_or_create(self, source: str) -> SourceReliability:
        if source not in self._sources:
            self._sources[source] = SourceReliability(source=source)
        return self._sources[source]

    def record_success(self, source: str, latency_ms: float) -> None:
        self.get_or_create(source).record_success(latency_ms)

    def record_failure(self, source: str, reason: str) -> None:
        self.get_or_create(source).record_failure(reason)

    def summary(self) -> List[dict]:
        return [sr.to_dict() for sr in sorted(self._sources.values(), key=lambda x: x.source)]
