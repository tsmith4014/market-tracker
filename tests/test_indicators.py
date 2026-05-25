"""Pure-function tests for technical indicators in market_tracker."""

from __future__ import annotations

import numpy as np
import pandas as pd
import pytest

from market_tracker import (
    adx,
    atr,
    bollinger,
    detect_swing,
    ema,
    fib_levels,
    macd,
    pivots,
    rsi,
    sma,
    true_range,
)


class TestEMA:
    def test_ema_first_value_equals_first_input(self):
        series = pd.Series([10.0, 20.0, 30.0])
        result = ema(series, span=5)
        assert result.iloc[0] == pytest.approx(10.0)

    def test_ema_converges_to_constant_input(self):
        series = pd.Series([50.0] * 100)
        result = ema(series, span=10)
        assert result.iloc[-1] == pytest.approx(50.0)

    def test_ema_lags_trending_input(self):
        """EMA should be below close prices in a rising series."""
        series = pd.Series(np.linspace(100, 200, 100))
        result = ema(series, span=20)
        # EMA of a linearly rising series lags below the last value
        assert result.iloc[-1] < series.iloc[-1]
        assert result.iloc[-1] > series.iloc[0]


class TestSMA:
    def test_sma_first_window_minus_one_is_nan(self):
        series = pd.Series([1.0, 2.0, 3.0, 4.0, 5.0])
        result = sma(series, window=3)
        assert pd.isna(result.iloc[0])
        assert pd.isna(result.iloc[1])
        assert result.iloc[2] == pytest.approx(2.0)

    def test_sma_mean_calculation(self):
        series = pd.Series([1.0, 2.0, 3.0, 4.0, 5.0])
        result = sma(series, window=3)
        assert result.iloc[2] == pytest.approx((1 + 2 + 3) / 3)
        assert result.iloc[3] == pytest.approx((2 + 3 + 4) / 3)
        assert result.iloc[4] == pytest.approx((3 + 4 + 5) / 3)


class TestRSI:
    def test_rsi_monotonic_up_returns_high(self):
        """100 bars of strictly increasing prices should produce RSI near 100."""
        series = pd.Series(np.linspace(100, 200, 100))
        result = rsi(series, period=14)
        # All gains and no losses -> RSI = 100
        assert result.iloc[-1] == pytest.approx(100.0, abs=1.0)

    def test_rsi_monotonic_down_returns_low(self):
        """100 bars of strictly decreasing prices should produce RSI near 0."""
        series = pd.Series(np.linspace(200, 100, 100))
        result = rsi(series, period=14)
        assert result.iloc[-1] == pytest.approx(0.0, abs=1.0)

    def test_rsi_in_valid_range(self):
        rng = np.random.default_rng(seed=1)
        series = pd.Series(100 + rng.normal(0, 5, 200).cumsum() * 0.1)
        result = rsi(series.abs() + 50, period=14).dropna()
        assert (result >= 0).all()
        assert (result <= 100).all()


class TestMACD:
    def test_macd_returns_three_series(self):
        series = pd.Series(np.linspace(100, 200, 100))
        line, sig, hist = macd(series)
        assert len(line) == len(series)
        assert len(sig) == len(series)
        assert len(hist) == len(series)

    def test_macd_histogram_is_line_minus_signal(self):
        series = pd.Series(np.linspace(100, 200, 100))
        line, sig, hist = macd(series)
        # Compare on non-NaN region
        assert (hist - (line - sig)).abs().max() < 1e-9

    def test_macd_positive_in_uptrend(self):
        series = pd.Series(np.linspace(100, 200, 100))
        line, _, _ = macd(series)
        # In a steady uptrend, fast EMA > slow EMA -> MACD line > 0
        assert line.iloc[-1] > 0


class TestTrueRangeATR:
    def test_true_range_with_no_gaps(self):
        """When prev close = today's low, TR = high - low."""
        h = pd.Series([110.0, 115.0, 120.0])
        l = pd.Series([100.0, 105.0, 110.0])
        c = pd.Series([110.0, 115.0, 120.0])  # prev close = today's high
        tr = true_range(h, l, c)
        # First bar: no prior close, so just high-low
        assert tr.iloc[0] == pytest.approx(10.0)

    def test_atr_positive_in_volatile_series(self):
        rng = np.random.default_rng(seed=2)
        n = 100
        close = 100 + rng.normal(0, 5, n).cumsum()
        high = close + np.abs(rng.normal(0, 2, n)) + 0.1
        low = close - np.abs(rng.normal(0, 2, n)) - 0.1
        a = atr(pd.Series(high), pd.Series(low), pd.Series(close), period=14)
        assert (a.dropna() > 0).all()


class TestADX:
    def test_adx_strong_in_steady_uptrend(self):
        """A pure linear uptrend should produce ADX above 25."""
        n = 100
        close = pd.Series(np.linspace(100, 200, n))
        high = close + 0.5
        low = close - 0.5
        adx_v, plus_di, minus_di = adx(high, low, close, period=14)
        # In monotonic uptrend, +DI dominates -DI and ADX is elevated
        assert adx_v.iloc[-1] > 25, f"ADX={adx_v.iloc[-1]} in clean uptrend"
        assert plus_di.iloc[-1] > minus_di.iloc[-1]

    def test_adx_weak_in_choppy_series(self):
        """Sideways random walk should not produce strong-trend ADX values."""
        rng = np.random.default_rng(seed=3)
        n = 200
        # zero-mean returns, very mean-reverting
        close = pd.Series(100 + np.cumsum(rng.normal(0, 0.5, n)) * 0.1)
        high = close + 0.2
        low = close - 0.2
        adx_v, _, _ = adx(high, low, close, period=14)
        # Strong trends typically show ADX > 50; noise should stay below that
        assert adx_v.iloc[-1] < 50


class TestBollinger:
    def test_bollinger_upper_above_mid_above_lower(self):
        series = pd.Series(np.linspace(100, 200, 100) + np.random.default_rng(4).normal(0, 1, 100))
        mid, up, dn, width = bollinger(series, window=20, nstd=2.0)
        valid = mid.dropna().index
        assert (up.loc[valid] >= mid.loc[valid]).all()
        assert (mid.loc[valid] >= dn.loc[valid]).all()

    def test_bollinger_width_zero_for_constant_series(self):
        series = pd.Series([50.0] * 100)
        _, _, _, width = bollinger(series, window=20, nstd=2.0)
        assert width.dropna().iloc[-1] == pytest.approx(0.0, abs=1e-9)


class TestPivots:
    def test_pivots_classical_formula(self):
        df = pd.DataFrame({
            "High": [110.0, 120.0],
            "Low": [100.0, 105.0],
            "Close": [105.0, 115.0],
        })
        p, r1, s1, r2, s2, r3, s3 = pivots(df)
        # Pivot for bar 1 uses bar 0's OHLC: (110 + 100 + 105) / 3
        assert p.iloc[1] == pytest.approx((110 + 100 + 105) / 3)
        assert r1.iloc[1] == pytest.approx(2 * ((110 + 100 + 105) / 3) - 100)
        assert s1.iloc[1] == pytest.approx(2 * ((110 + 100 + 105) / 3) - 110)


class TestFibLevels:
    def test_fib_levels_returns_five_values(self):
        levels = fib_levels(100.0, 200.0)
        assert set(levels.keys()) == {"23.6%", "38.2%", "50.0%", "61.8%", "78.6%"}

    def test_fib_50_percent_is_midpoint(self):
        levels = fib_levels(100.0, 200.0)
        assert levels["50.0%"] == pytest.approx(150.0)

    def test_fib_levels_invalid_inputs_return_nan(self):
        for low, high in [(np.nan, 100), (100, np.nan), (100, 100), (200, 100)]:
            levels = fib_levels(low, high)
            for value in levels.values():
                assert pd.isna(value)

    def test_fib_38_above_62(self):
        """38.2% retrace from a low->high swing should be above the 61.8% retrace."""
        levels = fib_levels(100.0, 200.0)
        assert levels["38.2%"] > levels["61.8%"]


class TestDetectSwing:
    def test_swing_detects_obvious_uptrend(self):
        df = pd.DataFrame({
            "High": np.linspace(100, 200, 50),
            "Low": np.linspace(95, 195, 50),
        })
        low, high = detect_swing(df, lookback=50)
        assert low < high
        assert low == pytest.approx(95.0, abs=0.01)
        assert high == pytest.approx(200.0, abs=0.01)

    def test_swing_invariant_low_lt_high(self):
        rng = np.random.default_rng(seed=5)
        df = pd.DataFrame({
            "High": 100 + np.abs(rng.normal(0, 5, 100)).cumsum(),
            "Low": 100 - np.abs(rng.normal(0, 5, 100)).cumsum(),
        })
        # Ensure highs are above lows row-wise
        df["High"] = np.maximum(df["High"], df["Low"] + 1)
        low, high = detect_swing(df, lookback=100)
        assert low < high
