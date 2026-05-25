"""End-to-end pipeline tests: OHLCV -> indicators -> scoring -> output rows."""

from __future__ import annotations

import numpy as np
import pandas as pd
import pytest

from market_tracker import (
    SCHEMA_COLUMNS,
    compute_indicators,
    process_df,
    row_to_output,
)


@pytest.fixture
def default_cfg() -> dict:
    return {
        "weights": {"trend": 0.50, "momentum": 0.20, "strength": 0.15, "vol": 0.10, "fib": 0.03, "pivot": 0.02},
        "thresholds": {"long": 30, "short": -30},
        "lookbacks": {"fib_long": 180, "fib_short": 30},
        "guards": {
            "min_adx_for_signal": 25,
            "max_atr_pct": 12.0,
            "require_close_above_ema50_for_long": False,
            "require_close_below_ema50_for_short": False,
        },
        "fees": {"bps_per_side": 2.0, "slippage_bps_per_side": 1.0},
    }


class TestComputeIndicators:
    def test_all_indicator_columns_present(self, trending_up_ohlcv):
        out = compute_indicators(trending_up_ohlcv, fib_long_lb=180, fib_short_lb=30)
        for col in ["EMA20", "EMA50", "EMA200", "SMA20", "SMA50", "SMA200",
                    "RSI14", "MACD", "MACD_SIGNAL", "ATR14", "ADX14", "+DI14", "-DI14",
                    "BB_MID20", "BB_UPPER20", "BB_LOWER20", "BB_WIDTH",
                    "PIVOT", "R1", "S1",
                    "fib_long_low", "fib_long_high",
                    "fib_short_low", "fib_short_high"]:
            assert col in out.columns

    def test_fib_columns_are_nan_during_warmup(self, trending_up_ohlcv):
        out = compute_indicators(trending_up_ohlcv, fib_long_lb=180, fib_short_lb=30)
        # First 179 rows should have NaN fib_long_low (need 180 rows of history)
        assert out["fib_long_low"].iloc[:179].isna().all()
        # 180th row onwards should have values
        assert out["fib_long_low"].iloc[180:].notna().all()

    def test_indicators_finite_after_warmup(self, trending_up_ohlcv):
        out = compute_indicators(trending_up_ohlcv, fib_long_lb=180, fib_short_lb=30)
        # Tail of series should have finite indicators for all key columns
        tail = out.tail(50)
        for col in ["EMA200", "RSI14", "MACD", "ATR14", "ADX14"]:
            assert tail[col].notna().all(), f"{col} has NaNs in tail"
            assert np.isfinite(tail[col]).all(), f"{col} has inf/NaN in tail"


class TestProcessDf:
    def test_strong_uptrend_produces_long_signal_in_recent_rows(self, trending_up_ohlcv, default_cfg):
        """500 bars of steady rising prices should yield LONG signals near the end."""
        out = process_df(trending_up_ohlcv, default_cfg)
        # Tail rows should be scored
        recent = out.tail(20)
        scored = recent[recent["composite_score"].notna()]
        assert not scored.empty, "Expected scored rows in tail of a 500-bar series"
        # Most recent signals should lean LONG
        signals = scored["signal"].tolist()
        long_count = signals.count("LONG")
        assert long_count >= 5, f"Expected LONG signals in clean uptrend, got {signals}"

    def test_strong_downtrend_produces_short_signal_in_recent_rows(self, trending_down_ohlcv, default_cfg):
        out = process_df(trending_down_ohlcv, default_cfg)
        recent = out.tail(20)
        scored = recent[recent["composite_score"].notna()]
        signals = scored["signal"].tolist()
        # With strong downtrend, expect at least some SHORT signals
        short_count = signals.count("SHORT")
        assert short_count >= 1 or "SHORT" in signals, f"Expected SHORT signals in downtrend, got {signals}"

    def test_flat_market_produces_mostly_neutral_signals(self, flat_ohlcv, default_cfg):
        """A flat market has low ADX which the guards block."""
        out = process_df(flat_ohlcv, default_cfg)
        scored = out[out["composite_score"].notna()]
        signals = scored["signal"].tolist()
        neutral_count = signals.count("NEUTRAL")
        # In a flat market, ADX should be low and guards should produce mostly NEUTRAL
        assert neutral_count / max(len(signals), 1) > 0.5, f"Expected mostly NEUTRAL in flat market, got {signals[:20]}"


class TestRowToOutput:
    def test_output_row_has_all_schema_columns(self, trending_up_ohlcv, default_cfg):
        out = process_df(trending_up_ohlcv, default_cfg)
        last = out.iloc[-1]
        row = row_to_output(last, "TEST", "synthetic", "2025-01-01T00:00:00")
        assert set(row.keys()) == set(SCHEMA_COLUMNS)

    def test_output_row_serializable_to_csv(self, trending_up_ohlcv, default_cfg):
        out = process_df(trending_up_ohlcv, default_cfg)
        last = out.iloc[-1]
        row = row_to_output(last, "TEST", "synthetic", "2025-01-01T00:00:00")
        # All values should be None or primitives (float/int/str), not pandas/numpy types
        for k, v in row.items():
            if v is not None:
                assert isinstance(v, int | float | str), f"{k}: unexpected type {type(v)}"

    def test_nans_converted_to_none(self, trending_up_ohlcv, default_cfg):
        out = process_df(trending_up_ohlcv, default_cfg)
        # First few rows have NaN indicators (warmup) — converted to None
        first = out.iloc[0]
        row = row_to_output(first, "TEST", "synthetic", "2025-01-01T00:00:00")
        # ema200 is NaN at index 0; should become None
        assert row["ema200"] is None or np.isfinite(row["ema200"])
