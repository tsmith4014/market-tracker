"""Tests for data quality assessment module."""

from __future__ import annotations

import numpy as np
import pandas as pd
import pytest

from data_quality import ReliabilityTracker, assess_quality


class TestAssessQuality:
    def _make_df(self, n=500, has_volume=True, gaps=False):
        # End at today so freshness check passes
        end = pd.Timestamp.now(tz="UTC").normalize()
        dates = pd.date_range(end - pd.Timedelta(days=n - 1), periods=n, freq="D")
        close = np.linspace(100, 200, n)
        df = pd.DataFrame({
            "Date": dates,
            "Open": close - 1,
            "High": close + 2,
            "Low": close - 2,
            "Close": close,
            "Volume": np.ones(n) * 1000 if has_volume else np.full(n, np.nan),
        })
        if gaps:
            # Remove 10 rows to create gaps
            df = df.drop(df.index[100:110]).reset_index(drop=True)
        return df

    def test_good_data_gets_grade_a(self):
        df = self._make_df(500)
        report = assess_quality(df, "BTC-USD", "Kraken API", 500, "crypto")
        assert report.quality_grade == "A"
        assert report.completeness == 1.0
        assert report.has_volume is True
        assert report.nan_pct == 0.0

    def test_incomplete_data_lowers_grade(self):
        df = self._make_df(200)
        report = assess_quality(df, "BTC-USD", "Kraken API", 500, "crypto")
        assert report.completeness < 0.5
        assert report.quality_grade in ("C", "D")

    def test_no_volume_penalized(self):
        df = self._make_df(500, has_volume=False)
        report = assess_quality(df, "BTC-USD", "CoinGecko", 500, "crypto")
        assert report.has_volume is False

    def test_gaps_detected(self):
        df = self._make_df(500, gaps=True)
        report = assess_quality(df, "BTC-USD", "Kraken API", 500, "crypto")
        assert report.to_dict()["gap_count"] > 0

    def test_to_dict_serializable(self):
        df = self._make_df(500)
        report = assess_quality(df, "BTC-USD", "Kraken API", 500, "crypto")
        d = report.to_dict()
        assert isinstance(d, dict)
        assert d["symbol"] == "BTC-USD"
        assert isinstance(d["completeness"], float)


class TestReliabilityTracker:
    def test_record_success(self):
        tracker = ReliabilityTracker()
        tracker.record_success("Kraken API", 150.0)
        tracker.record_success("Kraken API", 250.0)
        summary = tracker.summary()
        assert len(summary) == 1
        assert summary[0]["successes"] == 2
        assert summary[0]["success_rate"] == 1.0
        assert summary[0]["avg_latency_ms"] == pytest.approx(200.0)

    def test_record_failure(self):
        tracker = ReliabilityTracker()
        tracker.record_failure("CoinGecko", "rate_limited")
        summary = tracker.summary()
        assert summary[0]["failures"] == 1
        assert summary[0]["success_rate"] == 0.0
        assert summary[0]["last_failure_reason"] == "rate_limited"

    def test_mixed_results(self):
        tracker = ReliabilityTracker()
        tracker.record_success("Kraken API", 100.0)
        tracker.record_failure("Kraken API", "timeout")
        tracker.record_success("Kraken API", 200.0)
        summary = tracker.summary()
        assert summary[0]["attempts"] == 3
        assert summary[0]["success_rate"] == pytest.approx(2 / 3)
