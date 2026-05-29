"""Tests for the co-pilot JSON output module."""

from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path

import numpy as np
import pytest

from copilot_output import (
    CopilotEncoder,
    _round_price,
    assess_bar_recency,
    build_copilot_payload,
    build_signal_payload,
    write_copilot_json,
    write_latest_signals_json,
)


class TestRoundPrice:
    def test_large_price_four_decimals(self):
        assert _round_price(72968.812345) == 72968.8123

    def test_sub_cent_keeps_significant_figures(self):
        # SHIB-like price must not collapse to 0.0
        r = _round_price(5.3e-06)
        assert r is not None and r > 0

    def test_micro_price_preserves_value(self):
        r = _round_price(3.361e-06)
        assert r == pytest.approx(3.361e-06, rel=1e-3)

    def test_none_and_nan_safe(self):
        assert _round_price(None) is None
        assert _round_price(float("nan")) is None

    def test_zero(self):
        assert _round_price(0.0) == 0.0


class TestCopilotEncoder:
    def test_handles_numpy_int(self):
        assert json.dumps({"x": np.int64(42)}, cls=CopilotEncoder) == '{"x": 42}'

    def test_handles_numpy_float(self):
        result = json.loads(json.dumps({"x": np.float64(3.14)}, cls=CopilotEncoder))
        assert result["x"] == pytest.approx(3.14)

    def test_handles_nan_as_none(self):
        result = json.loads(json.dumps({"x": np.nan}, cls=CopilotEncoder))
        assert result["x"] is None

    def test_handles_inf_as_none(self):
        result = json.loads(json.dumps({"x": np.float64(np.inf)}, cls=CopilotEncoder))
        assert result["x"] is None


class TestBuildSignalPayload:
    def test_basic_payload_structure(self):
        row = {
            "close": 100.0, "ema20": 98.0, "ema50": 95.0, "ema200": 85.0,
            "atr14": 2.5, "rsi14": 60.0, "macd_hist": 0.5, "adx14": 30.0,
            "bb_width": 0.08, "rvol": 1.2, "stoch_rsi": 65.0,
            "mom_divergence": 0, "weekly_trend": 1.0,
            "signal": "LONG", "composite_score": 55.0,
            "trend_s": 4.0, "momentum_s": 2.0, "strength_s": 1.5,
            "vol_s": 0.5, "fib_s": 0.5, "pivot_s": 0.5, "volume_s": 0.5,
            "pivot": 97.0, "r1": 102.0, "s1": 94.0,
            "fib_long_low": 80.0, "fib_long_high": 110.0,
            "roc1": 0.01, "roc10": 5.0, "date": "2025-01-15",
            "vwap": 98.5,
        }
        payload = build_signal_payload(
            symbol="BTC-USD", row=row,
            confidence_level="HIGH", confidence_score=0.8,
            quality_grade="A", source="Kraken API",
        )
        assert payload["symbol"] == "BTC-USD"
        assert payload["signal"] == "LONG"
        assert payload["confidence"]["level"] == "HIGH"
        assert payload["confidence"]["score"] == 0.8
        assert payload["price"]["close"] == 100.0
        assert "atr_stop_long" in payload["levels"]
        assert payload["meta"]["quality_grade"] == "A"

    def test_handles_none_values(self):
        row = {k: None for k in [
            "close", "ema20", "ema50", "ema200", "atr14", "rsi14",
            "macd_hist", "adx14", "bb_width", "rvol", "stoch_rsi",
            "mom_divergence", "weekly_trend", "signal", "composite_score",
            "trend_s", "momentum_s", "strength_s", "vol_s", "fib_s",
            "pivot_s", "volume_s", "pivot", "r1", "s1",
            "fib_long_low", "fib_long_high", "roc1", "roc10", "date", "vwap",
        ]}
        row["signal"] = "NEUTRAL"
        payload = build_signal_payload(
            symbol="TEST", row=row,
            confidence_level="LOW", confidence_score=0.0,
            quality_grade="D", source="test",
        )
        assert payload["symbol"] == "TEST"
        assert payload["price"]["close"] is None


class TestBuildCopilotPayload:
    def test_payload_structure(self):
        signals = [{"symbol": "BTC-USD", "signal": "LONG", "confidence": {"level": "HIGH", "score": 0.8}}]
        regime = {"regime": "RISK_ON", "risk_score": 35.0, "dxy_signal": "WEAK_USD"}
        payload = build_copilot_payload(
            signals=signals,
            regime=regime,
            quality_reports=[],
            source_reliability=[],
            run_timestamp="2025-01-15T12:00:00Z",
        )
        assert payload["version"] == "2.1"
        assert "positioning" in payload
        assert payload["summary"]["long_signals"] == 1
        assert payload["market_regime"]["regime"] == "RISK_ON"
        assert len(payload["signals"]) == 1


class TestWriteCopilotJson:
    def test_writes_valid_json(self, tmp_path: Path):
        path = str(tmp_path / "test.json")
        payload = {"version": "2.0", "signals": []}
        write_copilot_json(payload, path)
        with open(path) as f:
            loaded = json.load(f)
        assert loaded["version"] == "2.0"

    def test_creates_parent_dirs(self, tmp_path: Path):
        path = str(tmp_path / "nested" / "deep" / "test.json")
        write_copilot_json({"test": True}, path)
        assert Path(path).exists()


class TestWriteLatestSignalsJson:
    def test_writes_slim_format(self, tmp_path: Path):
        path = str(tmp_path / "latest.json")
        signals = [{
            "symbol": "BTC-USD", "signal": "LONG",
            "composite_score": 55.0,
            "confidence": {"level": "HIGH", "score": 0.8},
            "price": {"close": 100000.0},
            "indicators": {"atr_pct": 2.5, "rsi14": 60.0},
        }]
        write_latest_signals_json(signals, path)
        with open(path) as f:
            loaded = json.load(f)
        assert "generated_at" in loaded
        assert len(loaded["signals"]) == 1
        assert loaded["signals"][0]["symbol"] == "BTC-USD"
        assert loaded["signals"][0]["confidence"] == "HIGH"


class TestAssessBarRecency:
    def test_yesterday_bar_is_complete(self):
        now = datetime(2025, 1, 15, 12, 0, tzinfo=timezone.utc)
        r = assess_bar_recency("2025-01-14", "crypto", now)
        assert r["bar_complete"] is True
        assert r["bar_age_days"] == 1
        assert r["stale"] is False

    def test_today_bar_is_incomplete(self):
        now = datetime(2025, 1, 15, 12, 0, tzinfo=timezone.utc)
        r = assess_bar_recency("2025-01-15", "crypto", now)
        assert r["bar_complete"] is False
        assert r["bar_age_days"] == 0

    def test_old_crypto_bar_is_stale(self):
        now = datetime(2025, 1, 15, 12, 0, tzinfo=timezone.utc)
        r = assess_bar_recency("2025-01-10", "crypto", now)
        assert r["stale"] is True

    def test_weekend_equity_bar_not_stale(self):
        # Friday bar viewed Monday: 3 days old, under the 4-day equity threshold
        now = datetime(2025, 1, 13, 12, 0, tzinfo=timezone.utc)  # Monday
        r = assess_bar_recency("2025-01-10", "stock", now)  # Friday
        assert r["stale"] is False

    def test_none_date_safe(self):
        r = assess_bar_recency(None, "crypto")
        assert r["bar_complete"] is None
        assert r["bar_age_days"] is None


class TestSignalPayloadRecency:
    def test_payload_meta_carries_recency(self):
        now = datetime(2025, 1, 15, 12, 0, tzinfo=timezone.utc)
        row = {"close": 100.0, "signal": "LONG", "date": "2025-01-15"}
        payload = build_signal_payload(
            symbol="BTC-USD", row=row,
            confidence_level="HIGH", confidence_score=0.8,
            quality_grade="A", source="Kraken API",
            asset_type="crypto", now=now,
        )
        assert payload["meta"]["bar_complete"] is False
        assert payload["meta"]["bar_age_days"] == 0
