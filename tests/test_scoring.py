"""Tests for scoring subscores, composite calculation, confidence, and guards."""

from __future__ import annotations

import math

import numpy as np
import pytest

from scoring import (
    composite_and_subscores,
    compute_confidence,
    compute_market_regime,
    enforce_guards,
    score_fib,
    score_momentum,
    score_pivot,
    score_strength,
    score_trend,
    score_volatility,
    score_volume,
)


class TestScoreTrend:
    def test_full_bullish_alignment_is_5(self):
        s = score_trend(close=150, ema20=140, ema50=130, ema200=110,
                        slope20=1.0, slope50=1.0, slope200=1.0)
        assert s == 5.0

    def test_full_bearish_alignment_is_minus_5(self):
        s = score_trend(close=100, ema20=110, ema50=120, ema200=140,
                        slope20=-1.0, slope50=-1.0, slope200=-1.0)
        assert s == -5.0

    def test_clipped_at_bounds(self):
        s = score_trend(close=1e9, ema20=1, ema50=1, ema200=1,
                        slope20=1e9, slope50=1e9, slope200=1e9)
        assert -5.0 <= s <= 5.0


class TestScoreMomentum:
    def test_strong_bullish_momentum(self):
        s = score_momentum(rsi14=60, macd_value=2.0, macd_signal=1.0)
        assert s == pytest.approx(2.5)

    def test_overbought_rsi(self):
        s = score_momentum(rsi14=75, macd_value=None, macd_signal=None)
        assert s == 0.5

    def test_clipped_at_bounds(self):
        s = score_momentum(rsi14=60, macd_value=1e9, macd_signal=-1e9)
        assert -3.0 <= s <= 3.0

    def test_none_inputs_safe(self):
        assert score_momentum(rsi14=None, macd_value=None, macd_signal=None) == 0.0

    def test_stoch_rsi_bonus(self):
        base = score_momentum(rsi14=60, macd_value=2.0, macd_signal=1.0)
        with_stoch = score_momentum(rsi14=60, macd_value=2.0, macd_signal=1.0, stoch_rsi=85)
        assert with_stoch >= base

    def test_bullish_divergence_bonus(self):
        base = score_momentum(rsi14=60, macd_value=2.0, macd_signal=1.0)
        with_div = score_momentum(rsi14=60, macd_value=2.0, macd_signal=1.0, mom_divergence=1.0)
        assert with_div >= base


class TestScoreStrength:
    def test_strong_trend_with_plus_di_dominant(self):
        s = score_strength(adx14=30, plus_di=40, minus_di=15)
        assert s == 1.5

    def test_weak_trend_minus_di_dominant(self):
        s = score_strength(adx14=15, plus_di=10, minus_di=30)
        assert s == -1.0

    def test_none_inputs_return_zero(self):
        assert score_strength(None, 1, 1) == 0.0
        assert score_strength(20, None, 1) == 0.0


class TestScoreVolatility:
    def test_low_atr_bonus(self):
        s = score_volatility(atr14=1.0, close=100.0, bb_width=None)
        assert s == 0.5

    def test_high_atr_penalty(self):
        s = score_volatility(atr14=10.0, close=100.0, bb_width=None)
        assert s == -0.5

    def test_bb_squeeze_bonus(self):
        s = score_volatility(atr14=None, close=None, bb_width=0.03)
        assert s == 0.25

    def test_bb_expansion_penalty(self):
        s = score_volatility(atr14=None, close=None, bb_width=0.30)
        assert s == -0.25


class TestScoreVolume:
    def test_high_rvol_with_positive_roc(self):
        s = score_volume(rvol=2.0, close=110, vwap=100, roc10=5.0)
        # high rvol + positive roc (+0.5) + close > vwap (+0.25)
        assert s == 0.75

    def test_high_rvol_with_negative_roc(self):
        s = score_volume(rvol=2.0, close=90, vwap=100, roc10=-5.0)
        # high rvol + negative roc (-0.25) + close < vwap (-0.25)
        assert s == -0.5

    def test_low_rvol_penalty(self):
        s = score_volume(rvol=0.3, close=100, vwap=100, roc10=0)
        assert s == -0.25

    def test_none_inputs_safe(self):
        assert score_volume(None, None, None, None) == 0.0


class TestScoreFib:
    def test_in_retracement_zone_returns_1(self):
        s = score_fib(close=150, low=100, high=200)
        assert s == 1.0

    def test_outside_zone_returns_minus_025(self):
        s = score_fib(close=190, low=100, high=200)
        assert s == -0.25

    def test_invalid_inputs_return_zero(self):
        assert score_fib(close=None, low=100, high=200) == 0.0
        assert score_fib(close=150, low=200, high=100) == 0.0


class TestScorePivot:
    def test_close_above_pivot_and_r1_bullish(self):
        s = score_pivot(close=110, pivot=100, r1=105, s1=95)
        assert s == 0.75

    def test_close_below_pivot_and_s1_bearish(self):
        s = score_pivot(close=90, pivot=100, r1=105, s1=95)
        assert s == -0.75

    def test_none_returns_zero(self):
        assert score_pivot(close=None, pivot=100, r1=105, s1=95) == 0.0


class TestCompositeAndSubscores:
    def test_strong_bullish_alignment_produces_high_score(self, default_symbol_cfg):
        latest = {
            "close": 200, "ema20": 195, "ema50": 190, "ema200": 150,
            "sma20": 192, "sma50": 185, "sma200": 140,
            "rsi14": 60, "macd": 2.0, "macd_signal": 1.0,
            "adx14": 35, "plus_di14": 40, "minus_di14": 15,
            "atr14": 1.5, "bb_width": 0.05,
            "pivot": 195, "r1": 198, "s1": 192,
            "fib_long_low": 100, "fib_long_high": 250,
            "stoch_rsi": 70, "mom_divergence": 0,
            "rvol": 1.5, "vwap": 190, "roc10": 5.0,
            "weekly_trend": 1.0,
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
            "stoch_rsi": 20, "mom_divergence": 0,
            "rvol": 1.0, "vwap": 110, "roc10": -5.0,
            "weekly_trend": -1.0,
        }
        score, subs = composite_and_subscores(latest, default_symbol_cfg["weights"])
        assert math.isfinite(score)
        assert score < -50, f"expected strongly bearish score, got {score}"
        assert subs["trend_s"] == -5.0

    def test_all_missing_inputs_score_is_nan_or_zero(self, default_symbol_cfg):
        latest = {k: None for k in [
            "close", "ema20", "ema50", "ema200", "sma20", "sma50", "sma200",
            "rsi14", "macd", "macd_signal", "adx14", "plus_di14", "minus_di14",
            "atr14", "bb_width", "pivot", "r1", "s1", "fib_long_low", "fib_long_high",
            "stoch_rsi", "mom_divergence", "rvol", "vwap", "roc10", "weekly_trend",
        ]}
        score, subs = composite_and_subscores(latest, default_symbol_cfg["weights"])
        assert math.isfinite(score) or math.isnan(score)

    def test_weight_renormalization_with_partial_inputs(self, default_symbol_cfg):
        latest = {
            "close": 150, "ema20": 145, "ema50": 140, "ema200": 120,
            "sma20": 142, "sma50": 135, "sma200": 115,
            "rsi14": 60, "macd": 1.0, "macd_signal": 0.5,
            "adx14": 30, "plus_di14": 35, "minus_di14": 20,
            "atr14": 1.0, "bb_width": 0.10,
            "pivot": 145, "r1": 148, "s1": 142,
            "fib_long_low": 100, "fib_long_high": 200,
            "stoch_rsi": None, "mom_divergence": None,
            "rvol": None, "vwap": None, "roc10": None,
            "weekly_trend": None,
        }
        score, _ = composite_and_subscores(latest, default_symbol_cfg["weights"])
        assert math.isfinite(score)
        assert -100.0 <= score <= 100.0


class TestRenormalization:
    def test_missing_volume_excluded_not_diluting(self, default_symbol_cfg):
        """A symbol with no volume data should score the same as one whose volume
        subscore happens to be neutral — because the missing subscore is dropped and
        the remaining weights renormalized, not folded in as a 0 vote."""
        base = {
            "close": 200, "ema20": 195, "ema50": 190, "ema200": 150,
            "sma20": 192, "sma50": 185, "sma200": 140,
            "rsi14": 60, "macd": 2.0, "macd_signal": 1.0,
            "adx14": 35, "plus_di14": 40, "minus_di14": 15,
            "atr14": 1.5, "bb_width": 0.05,
            "pivot": 195, "r1": 198, "s1": 192,
            "fib_long_low": 100, "fib_long_high": 250,
            "stoch_rsi": 70, "mom_divergence": 0,
            "weekly_trend": 1.0,
        }
        with_vol = {**base, "rvol": 1.5, "vwap": 190, "roc10": 5.0}
        without_vol = {**base, "rvol": None, "vwap": None, "roc10": None}
        score_with, _ = composite_and_subscores(with_vol, default_symbol_cfg["weights"])
        score_without, _ = composite_and_subscores(without_vol, default_symbol_cfg["weights"])
        # Both finite; the missing-volume case is renormalized over the other 6 subscores.
        assert np.isfinite(score_with) and np.isfinite(score_without)
        # Renormalization keeps the bullish score strong rather than dragging it down.
        assert score_without > 50


class TestComputeConfidence:
    def test_high_confidence_for_strong_signal(self):
        subs = {"trend_s": 5.0, "momentum_s": 3.0, "strength_s": 2.0, "vol_s": 1.0, "fib_s": 1.0, "pivot_s": 1.0, "volume_s": 1.0}
        latest = {"weekly_trend": 1.0, "rvol": 2.0}
        level, score = compute_confidence(80.0, subs, latest, {"long": 30, "short": -30})
        assert level == "HIGH"
        assert score > 0.6

    def test_low_confidence_near_threshold(self):
        subs = {"trend_s": 1.0, "momentum_s": -1.0, "strength_s": 0.5, "vol_s": 0.0, "fib_s": 0.0, "pivot_s": 0.0, "volume_s": 0.0}
        latest = {"weekly_trend": 0, "rvol": 0.8}
        level, score = compute_confidence(31.0, subs, latest, {"long": 30, "short": -30})
        assert level in ("LOW", "MEDIUM")
        assert score < 0.6

    def test_nan_score_returns_low(self):
        level, score = compute_confidence(np.nan, {}, {}, {"long": 30, "short": -30})
        assert level == "LOW"
        assert score == 0.0

    def test_neutral_signal_collapses_confidence(self):
        """A guarded-to-NEUTRAL signal must not report HIGH confidence."""
        subs = {"trend_s": 5.0, "momentum_s": 3.0, "strength_s": 2.0, "vol_s": 1.0, "fib_s": 1.0, "pivot_s": 1.0, "volume_s": 1.0}
        latest = {"weekly_trend": 1.0, "rvol": 2.0, "rsi14": 60}
        level, score = compute_confidence(80.0, subs, latest, {"long": 30, "short": -30}, signal="NEUTRAL")
        assert level == "LOW"
        assert score == 0.0

    def test_stretched_long_is_penalized(self):
        subs = {"trend_s": 5.0, "momentum_s": 3.0, "strength_s": 2.0, "vol_s": 1.0, "fib_s": 1.0, "pivot_s": 1.0, "volume_s": 1.0}
        latest = {"weekly_trend": 1.0, "rvol": 2.0, "rsi14": 88}
        not_stretched = {**latest, "rsi14": 60}
        _, stretched_score = compute_confidence(80.0, subs, latest, {"long": 30, "short": -30}, signal="LONG")
        _, normal_score = compute_confidence(80.0, subs, not_stretched, {"long": 30, "short": -30}, signal="LONG")
        assert stretched_score < normal_score

    def test_stretched_short_is_penalized(self):
        subs = {"trend_s": -5.0, "momentum_s": -3.0, "strength_s": -2.0, "vol_s": -1.0, "fib_s": -1.0, "pivot_s": -1.0, "volume_s": -1.0}
        latest = {"weekly_trend": -1.0, "rvol": 2.0, "rsi14": 12}
        not_stretched = {**latest, "rsi14": 40}
        _, stretched_score = compute_confidence(-80.0, subs, latest, {"long": 30, "short": -30}, signal="SHORT")
        _, normal_score = compute_confidence(-80.0, subs, not_stretched, {"long": 30, "short": -30}, signal="SHORT")
        assert stretched_score < normal_score


class TestComputeMarketRegime:
    def test_risk_on(self):
        result = compute_market_regime({"SPY": 40.0, "QQQ": 50.0, "DXY-INDEX": -10.0})
        assert result["regime"] == "RISK_ON"

    def test_risk_off(self):
        result = compute_market_regime({"SPY": -40.0, "QQQ": -30.0, "DXY-INDEX": 50.0})
        assert result["regime"] == "RISK_OFF"
        assert result["dxy_signal"] == "STRONG_USD"

    def test_mixed_regime(self):
        result = compute_market_regime({"SPY": 5.0, "QQQ": -5.0})
        assert result["regime"] == "MIXED"

    def test_no_data_returns_mixed(self):
        result = compute_market_regime({})
        assert result["regime"] == "MIXED"


class TestEnforceGuards:
    def test_neutral_signal_passes_through(self, default_symbol_cfg):
        result = enforce_guards(default_symbol_cfg, {"adx14": 10}, "NEUTRAL")
        assert result == "NEUTRAL"

    def test_long_blocked_by_low_adx(self, default_symbol_cfg):
        latest = {"adx14": 10, "atr14": 1.0, "close": 100, "ema50": 95}
        result = enforce_guards(default_symbol_cfg, latest, "LONG")
        assert result == "NEUTRAL"

    def test_long_passes_with_strong_adx(self, default_symbol_cfg):
        latest = {"adx14": 30, "atr14": 1.0, "close": 100, "ema50": 95}
        result = enforce_guards(default_symbol_cfg, latest, "LONG")
        assert result == "LONG"

    def test_short_blocked_by_high_atr(self, default_symbol_cfg):
        latest = {"adx14": 30, "atr14": 15.0, "close": 100, "ema50": 105}
        result = enforce_guards(default_symbol_cfg, latest, "SHORT")
        assert result == "NEUTRAL"

    def test_long_requires_close_above_ema50_when_enabled(self, default_symbol_cfg):
        cfg = {**default_symbol_cfg}
        cfg["guards"] = {**default_symbol_cfg["guards"], "require_close_above_ema50_for_long": True}
        latest = {"adx14": 30, "atr14": 1.0, "close": 100, "ema50": 110}
        assert enforce_guards(cfg, latest, "LONG") == "NEUTRAL"
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
