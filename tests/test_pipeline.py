"""End-to-end pipeline tests: OHLCV -> indicators -> scoring -> output rows."""

from __future__ import annotations

import numpy as np
import pandas as pd
import pytest

from indicators import compute_all_indicators
from market_tracker import (
    SCHEMA_COLUMNS,
    process_df,
    row_to_output,
)


@pytest.fixture
def default_cfg() -> dict:
    return {
        "weights": {"trend": 0.45, "momentum": 0.20, "strength": 0.15, "vol": 0.08, "fib": 0.03, "pivot": 0.02, "volume": 0.07},
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
        out = compute_all_indicators(trending_up_ohlcv, fib_long_lb=180, fib_short_lb=30)
        for col in ["EMA20", "EMA50", "EMA200", "SMA20", "SMA50", "SMA200",
                    "RSI14", "MACD", "MACD_SIGNAL", "ATR14", "ADX14", "+DI14", "-DI14",
                    "BB_MID20", "BB_UPPER20", "BB_LOWER20", "BB_WIDTH",
                    "PIVOT", "R1", "S1",
                    "fib_long_low", "fib_long_high",
                    "fib_short_low", "fib_short_high",
                    "VWAP20", "RVOL", "OBV", "ROC10", "ROC20",
                    "STOCH_RSI", "MOM_DIVERGENCE", "WEEKLY_TREND"]:
            assert col in out.columns

    def test_fib_columns_are_nan_during_warmup(self, trending_up_ohlcv):
        out = compute_all_indicators(trending_up_ohlcv, fib_long_lb=180, fib_short_lb=30)
        assert out["fib_long_low"].iloc[:179].isna().all()
        assert out["fib_long_low"].iloc[180:].notna().all()

    def test_indicators_finite_after_warmup(self, trending_up_ohlcv):
        out = compute_all_indicators(trending_up_ohlcv, fib_long_lb=180, fib_short_lb=30)
        tail = out.tail(50)
        for col in ["EMA200", "RSI14", "MACD", "ATR14", "ADX14"]:
            assert tail[col].notna().all(), f"{col} has NaNs in tail"
            assert np.isfinite(tail[col]).all(), f"{col} has inf/NaN in tail"


class TestProcessDf:
    def test_strong_uptrend_produces_long_signal_in_recent_rows(self, trending_up_ohlcv, default_cfg):
        out = process_df(trending_up_ohlcv, default_cfg)
        recent = out.tail(20)
        scored = recent[recent["composite_score"].notna()]
        assert not scored.empty, "Expected scored rows in tail of a 500-bar series"
        signals = scored["signal"].tolist()
        long_count = signals.count("LONG")
        assert long_count >= 5, f"Expected LONG signals in clean uptrend, got {signals}"

    def test_strong_downtrend_produces_short_signal_in_recent_rows(self, trending_down_ohlcv, default_cfg):
        out = process_df(trending_down_ohlcv, default_cfg)
        recent = out.tail(20)
        scored = recent[recent["composite_score"].notna()]
        signals = scored["signal"].tolist()
        short_count = signals.count("SHORT")
        assert short_count >= 1 or "SHORT" in signals, f"Expected SHORT signals in downtrend, got {signals}"

    def test_flat_market_produces_mostly_neutral_signals(self, flat_ohlcv, default_cfg):
        out = process_df(flat_ohlcv, default_cfg)
        scored = out[out["composite_score"].notna()]
        signals = scored["signal"].tolist()
        neutral_count = signals.count("NEUTRAL")
        assert neutral_count / max(len(signals), 1) > 0.5, f"Expected mostly NEUTRAL in flat market, got {signals[:20]}"

    def test_confidence_columns_present(self, trending_up_ohlcv, default_cfg):
        out = process_df(trending_up_ohlcv, default_cfg)
        assert "confidence_level" in out.columns
        assert "confidence_score" in out.columns
        scored = out[out["composite_score"].notna()]
        assert scored["confidence_level"].isin(["HIGH", "MEDIUM", "LOW"]).all()
        assert (scored["confidence_score"] >= 0).all()
        assert (scored["confidence_score"] <= 1).all()

    def test_volume_subscore_present(self, trending_up_ohlcv, default_cfg):
        out = process_df(trending_up_ohlcv, default_cfg)
        assert "volume_s" in out.columns


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
        for k, v in row.items():
            if v is not None:
                assert isinstance(v, int | float | str), f"{k}: unexpected type {type(v)}"

    def test_nans_converted_to_none(self, trending_up_ohlcv, default_cfg):
        out = process_df(trending_up_ohlcv, default_cfg)
        first = out.iloc[0]
        row = row_to_output(first, "TEST", "synthetic", "2025-01-01T00:00:00")
        assert row["ema200"] is None or np.isfinite(row["ema200"])

    def test_new_columns_in_output(self, trending_up_ohlcv, default_cfg):
        out = process_df(trending_up_ohlcv, default_cfg)
        last = out.iloc[-1]
        row = row_to_output(last, "TEST", "synthetic", "2025-01-01T00:00:00")
        assert "vwap20" in row
        assert "rvol" in row
        assert "roc10" in row
        assert "stoch_rsi" in row
        assert "confidence_level" in row
        assert "confidence_score" in row
        assert "volume_s" in row


class TestStrategySwitch:
    def test_mean_reversion_strategy_runs(self, trending_up_ohlcv, default_cfg):
        cfg = {**default_cfg, "strategy": "mean_reversion"}
        out = process_df(trending_up_ohlcv, cfg)
        scored = out[out["composite_score"].notna()]
        assert not scored.empty
        assert scored["signal"].isin(["LONG", "SHORT", "NEUTRAL"]).all()

    def test_regime_adaptive_strategy_runs(self, trending_up_ohlcv, default_cfg):
        cfg = {**default_cfg, "strategy": "regime_adaptive"}
        out = process_df(trending_up_ohlcv, cfg)
        scored = out[out["composite_score"].notna()]
        assert not scored.empty
        # Strong uptrend under adaptive logic should still surface LONGs.
        assert (scored["signal"] == "LONG").any()

    def test_default_is_trend(self, trending_up_ohlcv, default_cfg):
        # No strategy key -> behaves as trend (LONG-heavy in a clean uptrend)
        out = process_df(trending_up_ohlcv, default_cfg)
        recent = out.tail(20)
        scored = recent[recent["composite_score"].notna()]
        assert (scored["signal"] == "LONG").sum() >= 5
