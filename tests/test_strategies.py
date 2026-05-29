"""Tests for the pluggable signal strategies."""

from __future__ import annotations

import strategies


class TestTrendSignal:
    def test_long_above_threshold(self):
        assert strategies.trend_signal(40, 30, -30) == "LONG"

    def test_short_below_threshold(self):
        assert strategies.trend_signal(-40, 30, -30) == "SHORT"

    def test_neutral_inside_band(self):
        assert strategies.trend_signal(10, 30, -30) == "NEUTRAL"

    def test_none_is_neutral(self):
        assert strategies.trend_signal(None, 30, -30) == "NEUTRAL"


class TestMeanReversionSignal:
    def test_buys_oversold_dip_in_uptrend(self):
        # RSI low, at/below lower band, price above EMA200 -> LONG
        assert strategies.mean_reversion_signal(close=100, rsi14=25, bb_lower20=101, bb_upper20=120, ema200=90) == "LONG"

    def test_no_long_when_below_ema200(self):
        # Oversold but in a downtrend -> don't catch the knife
        assert strategies.mean_reversion_signal(close=80, rsi14=25, bb_lower20=81, bb_upper20=120, ema200=90) == "NEUTRAL"

    def test_sells_overbought_rally_in_downtrend(self):
        assert strategies.mean_reversion_signal(close=100, rsi14=75, bb_lower20=80, bb_upper20=99, ema200=110) == "SHORT"

    def test_neutral_midrange(self):
        assert strategies.mean_reversion_signal(close=100, rsi14=50, bb_lower20=90, bb_upper20=110, ema200=95) == "NEUTRAL"

    def test_none_inputs_neutral(self):
        assert strategies.mean_reversion_signal(None, None, None, None, None) == "NEUTRAL"


class TestRegimeAdaptive:
    def _kw(self, **over):
        base = dict(score=40, long_th=30, short_th=-30, close=100, rsi14=25,
                    bb_lower20=101, bb_upper20=120, ema200=90, adx14=10)
        base.update(over)
        return base

    def test_trending_uses_trend_rule(self):
        # High ADX -> trend branch: strong score -> LONG
        assert strategies.raw_signal(strategies.REGIME_ADAPTIVE, **self._kw(adx14=35, score=40)) == "LONG"

    def test_chop_uses_mean_reversion(self):
        # Low ADX, weak score, but oversold dip in uptrend -> MR LONG
        assert strategies.raw_signal(strategies.REGIME_ADAPTIVE, **self._kw(adx14=10, score=5)) == "LONG"

    def test_chop_weak_score_no_mr_setup_is_neutral(self):
        assert strategies.raw_signal(strategies.REGIME_ADAPTIVE, **self._kw(adx14=10, score=5, rsi14=50)) == "NEUTRAL"


class TestRawSignalDispatch:
    def test_unknown_strategy_raises(self):
        import pytest
        with pytest.raises(ValueError, match="Unknown strategy"):
            strategies.raw_signal("bogus", score=1, long_th=30, short_th=-30, close=1,
                                  rsi14=1, bb_lower20=1, bb_upper20=1, ema200=1, adx14=1)


class TestUsesTrendGuards:
    def test_trend_always_guarded(self):
        assert strategies.uses_trend_guards(strategies.TREND, 5) is True

    def test_mean_reversion_never_trend_guarded(self):
        assert strategies.uses_trend_guards(strategies.MEAN_REVERSION, 50) is False

    def test_adaptive_guarded_only_when_trending(self):
        assert strategies.uses_trend_guards(strategies.REGIME_ADAPTIVE, 30) is True
        assert strategies.uses_trend_guards(strategies.REGIME_ADAPTIVE, 10) is False
