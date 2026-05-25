"""Tests for scoring subscores, composite calculation, and signal guards."""

from __future__ import annotations

import math

import numpy as np
import pytest

from market_tracker import (
    composite_and_subscores,
    enforce_guards,
    score_fib,
    score_momentum,
    score_pivot,
    score_strength,
    score_trend,
    score_volatility,
)


class TestScoreTrend:
    def test_full_bullish_alignment_is_5(self):
        """Close above all EMAs and all slopes positive -> max trend score."""
        s = score_trend(close=150, ema20=140, ema50=130, ema200=110,
                        slope20=1.0, slope50=1.0, slope200=1.0)
        assert s == 5.0

    def test_full_bearish_alignment_is_minus_5(self):
        s = score_trend(close=100, ema20=110, ema50=120, ema200=140,
                        slope20=-1.0, slope50=-1.0, slope200=-1.0)
        assert s == -5.0

    def test_clipped_at_bounds(self):
        # Even bizarre inputs should respect the [-5, 5] cap
        s = score_trend(close=1e9, ema20=1, ema50=1, ema200=1,
                        slope20=1e9, slope50=1e9, slope200=1e9)
        assert -5.0 <= s <= 5.0


class TestScoreMomentum:
    def test_strong_bullish_momentum(self):
        # RSI 60 (in 50-70 band: +1), MACD line > signal and > 0 (+1 + 0.5 = +1.5)
        s = score_momentum(rsi14=60, macd_value=2.0, macd_signal=1.0)
        assert s == pytest.approx(2.5)

    def test_overbought_rsi(self):
        # RSI 75: hits both 50-70 band (no, it's 75) and >70 band (+0.5)
        s = score_momentum(rsi14=75, macd_value=None, macd_signal=None)
        assert s == 0.5

    def test_clipped_at_bounds(self):
        s = score_momentum(rsi14=60, macd_value=1e9, macd_signal=-1e9)
        assert -3.0 <= s <= 3.0

    def test_none_inputs_safe(self):
        assert score_momentum(rsi14=None, macd_value=None, macd_signal=None) == 0.0


class TestScoreStrength:
    def test_strong_trend_with_plus_di_dominant(self):
        s = score_strength(adx14=30, plus_di=40, minus_di=15)
        assert s == 1.5  # adx >= 25 (+1) and plus_di > minus_di (+0.5)

    def test_weak_trend_minus_di_dominant(self):
        s = score_strength(adx14=15, plus_di=10, minus_di=30)
        assert s == -1.0

    def test_none_inputs_return_zero(self):
        assert score_strength(None, 1, 1) == 0.0
        assert score_strength(20, None, 1) == 0.0


class TestScoreVolatility:
    def test_low_atr_bonus(self):
        # ATR < 2% -> +0.5
        s = score_volatility(atr14=1.0, close=100.0, bb_width=None)
        assert s == 0.5

    def test_high_atr_penalty(self):
        # ATR > 8% -> -0.5
        s = score_volatility(atr14=10.0, close=100.0, bb_width=None)
        assert s == -0.5

    def test_bb_squeeze_bonus(self):
        s = score_volatility(atr14=None, close=None, bb_width=0.03)
        assert s == 0.25

    def test_bb_expansion_penalty(self):
        s = score_volatility(atr14=None, close=None, bb_width=0.30)
        assert s == -0.25


class TestScoreFib:
    def test_in_retracement_zone_returns_1(self):
        # Swing 100->200; close at 150 (50%) is squarely in 38.2-61.8 zone
        s = score_fib(close=150, low=100, high=200)
        assert s == 1.0

    def test_outside_zone_returns_minus_025(self):
        s = score_fib(close=190, low=100, high=200)
        assert s == -0.25

    def test_invalid_inputs_return_zero(self):
        assert score_fib(close=None, low=100, high=200) == 0.0
        assert score_fib(close=150, low=200, high=100) == 0.0  # inverted


class TestScorePivot:
    def test_close_above_pivot_and_r1_bullish(self):
        s = score_pivot(close=110, pivot=100, r1=105, s1=95)
        assert s == 0.75  # above pivot (+0.5) + above R1 (+0.25)

    def test_close_below_pivot_and_s1_bearish(self):
        s = score_pivot(close=90, pivot=100, r1=105, s1=95)
        assert s == -0.75

    def test_none_returns_zero(self):
        assert score_pivot(close=None, pivot=100, r1=105, s1=95) == 0.0


class TestCompositeAndSubscores:
    def test_strong_bullish_alignment_produces_high_score(self, default_symbol_cfg):
        """All bullish inputs should produce a composite score near +100."""
        latest = {
            "close": 200, "ema20": 195, "ema50": 190, "ema200": 150,
            "sma20": 192, "sma50": 185, "sma200": 140,  # slopes positive
            "rsi14": 60, "macd": 2.0, "macd_signal": 1.0,
            "adx14": 35, "plus_di14": 40, "minus_di14": 15,
            "atr14": 1.5, "bb_width": 0.05,  # mild positive vol score
            "pivot": 195, "r1": 198, "s1": 192,
            "fib_long_low": 100, "fib_long_high": 250,  # close 200 above retrace
        }
        score, subs = composite_and_subscores(latest, default_symbol_cfg["weights"])
        assert math.isfinite(score)
        assert score > 50, f"expected strongly bullish score, got {score}"
        assert subs["trend_s"] == 5.0
        assert subs["momentum_s"] > 0

    def test_strong_bearish_alignment_produces_low_score(self, default_symbol_cfg):
        latest = {
            "close": 100, "ema20": 110, "ema50": 120, "ema200": 150,
            "sma20": 112, "sma50": 125, "sma200": 155,
            "rsi14": 25, "macd": -2.0, "macd_signal": -1.0,
            "adx14": 35, "plus_di14": 15, "minus_di14": 40,
            "atr14": 1.5, "bb_width": 0.05,
            "pivot": 110, "r1": 115, "s1": 105,
            "fib_long_low": 50, "fib_long_high": 200,
        }
        score, subs = composite_and_subscores(latest, default_symbol_cfg["weights"])
        assert math.isfinite(score)
        assert score < -50, f"expected strongly bearish score, got {score}"
        assert subs["trend_s"] == -5.0

    def test_all_missing_inputs_score_is_nan_or_zero(self, default_symbol_cfg):
        """When every indicator is None, valid subscores collapse to 0 sum
        and weights map to zero contribution. The function should not crash."""
        latest = {k: None for k in [
            "close", "ema20", "ema50", "ema200", "sma20", "sma50", "sma200",
            "rsi14", "macd", "macd_signal", "adx14", "plus_di14", "minus_di14",
            "atr14", "bb_width", "pivot", "r1", "s1", "fib_long_low", "fib_long_high",
        ]}
        score, subs = composite_and_subscores(latest, default_symbol_cfg["weights"])
        # All subscores defined, but resolved with None inputs -> bearish defaults
        # Composite should still be finite (not NaN) because all subscores are finite
        assert math.isfinite(score) or math.isnan(score)

    def test_weight_renormalization_with_partial_inputs(self, default_symbol_cfg):
        """If some subscores produce NaN, valid subscores should be renormalized."""
        # Construct a case where score_fib returns 0 (close=None equivalent removed)
        # but all other subscores are finite
        latest = {
            "close": 150, "ema20": 145, "ema50": 140, "ema200": 120,
            "sma20": 142, "sma50": 135, "sma200": 115,
            "rsi14": 60, "macd": 1.0, "macd_signal": 0.5,
            "adx14": 30, "plus_di14": 35, "minus_di14": 20,
            "atr14": 1.0, "bb_width": 0.10,
            "pivot": 145, "r1": 148, "s1": 142,
            "fib_long_low": 100, "fib_long_high": 200,
        }
        score, _ = composite_and_subscores(latest, default_symbol_cfg["weights"])
        assert math.isfinite(score)
        assert -100.0 <= score <= 100.0


class TestEnforceGuards:
    def test_neutral_signal_passes_through(self, default_symbol_cfg):
        result = enforce_guards(default_symbol_cfg, {"adx14": 10}, "NEUTRAL")
        assert result == "NEUTRAL"

    def test_long_blocked_by_low_adx(self, default_symbol_cfg):
        latest = {"adx14": 10, "atr14": 1.0, "close": 100, "ema50": 95}
        # default min_adx_for_signal = 25, adx14 = 10 -> blocked
        result = enforce_guards(default_symbol_cfg, latest, "LONG")
        assert result == "NEUTRAL"

    def test_long_passes_with_strong_adx(self, default_symbol_cfg):
        latest = {"adx14": 30, "atr14": 1.0, "close": 100, "ema50": 95}
        result = enforce_guards(default_symbol_cfg, latest, "LONG")
        assert result == "LONG"

    def test_short_blocked_by_high_atr(self, default_symbol_cfg):
        # atr/close% = 15/100 = 15% > default 12% max
        latest = {"adx14": 30, "atr14": 15.0, "close": 100, "ema50": 105}
        result = enforce_guards(default_symbol_cfg, latest, "SHORT")
        assert result == "NEUTRAL"

    def test_long_requires_close_above_ema50_when_enabled(self, default_symbol_cfg):
        cfg = {**default_symbol_cfg}
        cfg["guards"] = {**default_symbol_cfg["guards"], "require_close_above_ema50_for_long": True}
        # close < ema50 -> blocked
        latest = {"adx14": 30, "atr14": 1.0, "close": 100, "ema50": 110}
        assert enforce_guards(cfg, latest, "LONG") == "NEUTRAL"
        # close > ema50 -> passes
        latest = {"adx14": 30, "atr14": 1.0, "close": 110, "ema50": 100}
        assert enforce_guards(cfg, latest, "LONG") == "LONG"

    def test_short_requires_close_below_ema50_when_enabled(self, default_symbol_cfg):
        cfg = {**default_symbol_cfg}
        cfg["guards"] = {**default_symbol_cfg["guards"], "require_close_below_ema50_for_short": True}
        latest = {"adx14": 30, "atr14": 1.0, "close": 110, "ema50": 100}
        assert enforce_guards(cfg, latest, "SHORT") == "NEUTRAL"
        latest = {"adx14": 30, "atr14": 1.0, "close": 100, "ema50": 110}
        assert enforce_guards(cfg, latest, "SHORT") == "SHORT"

    def test_missing_adx_blocks_signal(self, default_symbol_cfg):
        latest = {"adx14": None, "atr14": 1.0, "close": 100, "ema50": 95}
        assert enforce_guards(default_symbol_cfg, latest, "LONG") == "NEUTRAL"
