"""Pure-function tests for technical indicators."""

from __future__ import annotations

import numpy as np
import pandas as pd
import pytest

from indicators import (
    adx,
    atr,
    bollinger,
    compute_all_indicators,
    detect_swing,
    ema,
    fib_levels,
    macd,
    momentum_divergence,
    obv,
    pivots,
    rate_of_change,
    relative_volume,
    rsi,
    sma,
    stochastic_rsi,
    true_range,
    vwap,
    weekly_trend_alignment,
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
        series = pd.Series(np.linspace(100, 200, 100))
        result = ema(series, span=20)
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
        series = pd.Series(np.linspace(100, 200, 100))
        result = rsi(series, period=14)
        assert result.iloc[-1] == pytest.approx(100.0, abs=1.0)

    def test_rsi_monotonic_down_returns_low(self):
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
        assert (hist - (line - sig)).abs().max() < 1e-9

    def test_macd_positive_in_uptrend(self):
        series = pd.Series(np.linspace(100, 200, 100))
        line, _, _ = macd(series)
        assert line.iloc[-1] > 0


class TestTrueRangeATR:
    def test_true_range_with_no_gaps(self):
        h = pd.Series([110.0, 115.0, 120.0])
        l = pd.Series([100.0, 105.0, 110.0])
        c = pd.Series([110.0, 115.0, 120.0])
        tr = true_range(h, l, c)
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
        n = 100
        close = pd.Series(np.linspace(100, 200, n))
        high = close + 0.5
        low = close - 0.5
        adx_v, plus_di, minus_di = adx(high, low, close, period=14)
        assert adx_v.iloc[-1] > 25, f"ADX={adx_v.iloc[-1]} in clean uptrend"
        assert plus_di.iloc[-1] > minus_di.iloc[-1]

    def test_adx_weak_in_choppy_series(self):
        rng = np.random.default_rng(seed=3)
        n = 200
        close = pd.Series(100 + np.cumsum(rng.normal(0, 0.5, n)) * 0.1)
        high = close + 0.2
        low = close - 0.2
        adx_v, _, _ = adx(high, low, close, period=14)
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
        df["High"] = np.maximum(df["High"], df["Low"] + 1)
        low, high = detect_swing(df, lookback=100)
        assert low < high


class TestVWAP:
    def test_vwap_equals_close_when_constant_volume(self):
        df = pd.DataFrame({
            "High": [110.0] * 30,
            "Low": [90.0] * 30,
            "Close": [100.0] * 30,
            "Volume": [1000.0] * 30,
        })
        result = vwap(df, period=20)
        assert result.iloc[-1] == pytest.approx(100.0)

    def test_vwap_weights_toward_high_volume(self):
        df = pd.DataFrame({
            "High": [110.0, 120.0, 110.0],
            "Low": [90.0, 100.0, 90.0],
            "Close": [100.0, 110.0, 100.0],
            "Volume": [100.0, 10000.0, 100.0],
        })
        result = vwap(df, period=3)
        # VWAP should lean toward 110 due to high volume on that bar
        assert result.iloc[-1] > 103.0


class TestRelativeVolume:
    def test_rvol_is_one_for_constant_volume(self):
        df = pd.DataFrame({"Volume": [1000.0] * 30})
        result = relative_volume(df, period=20)
        assert result.iloc[-1] == pytest.approx(1.0)

    def test_rvol_above_one_for_spike(self):
        vol = [1000.0] * 25 + [5000.0]
        df = pd.DataFrame({"Volume": vol})
        result = relative_volume(df, period=20)
        assert result.iloc[-1] > 2.0


class TestRateOfChange:
    def test_roc_positive_for_rising_prices(self):
        series = pd.Series(np.linspace(100, 200, 50))
        result = rate_of_change(series, period=10)
        assert result.iloc[-1] > 0

    def test_roc_zero_for_constant(self):
        series = pd.Series([100.0] * 20)
        result = rate_of_change(series, period=10)
        assert result.iloc[-1] == pytest.approx(0.0)


class TestOBV:
    def test_obv_increases_on_up_close(self):
        close = pd.Series([100.0, 101.0, 102.0, 103.0])
        volume = pd.Series([1000.0, 1000.0, 1000.0, 1000.0])
        result = obv(close, volume)
        # Each bar up adds volume
        assert result.iloc[-1] > 0

    def test_obv_decreases_on_down_close(self):
        close = pd.Series([103.0, 102.0, 101.0, 100.0])
        volume = pd.Series([1000.0, 1000.0, 1000.0, 1000.0])
        result = obv(close, volume)
        assert result.iloc[-1] < 0


class TestStochasticRSI:
    def test_stoch_rsi_in_valid_range(self):
        rng = np.random.default_rng(seed=10)
        series = pd.Series(100 + rng.normal(0, 2, 200).cumsum())
        result = stochastic_rsi(series.abs() + 50, 14, 14).dropna()
        assert (result >= 0).all()
        assert (result <= 100).all()


class TestMomentumDivergence:
    def test_bullish_divergence(self):
        # Price making lower lows but RSI making higher lows
        close = pd.Series([100.0] * 14 + [95.0] * 14 + [90.0])
        rsi_vals = pd.Series([30.0] * 14 + [35.0] * 14 + [40.0])
        result = momentum_divergence(close, rsi_vals, lookback=14)
        assert result.iloc[-1] == 1.0  # bullish

    def test_bearish_divergence(self):
        close = pd.Series([100.0] * 14 + [105.0] * 14 + [110.0])
        rsi_vals = pd.Series([70.0] * 14 + [65.0] * 14 + [60.0])
        result = momentum_divergence(close, rsi_vals, lookback=14)
        assert result.iloc[-1] == -1.0  # bearish


class TestWeeklyTrendAlignment:
    def test_returns_series_same_length(self, trending_up_ohlcv):
        result = weekly_trend_alignment(trending_up_ohlcv)
        assert len(result) == len(trending_up_ohlcv)

    def test_bullish_in_uptrend(self, trending_up_ohlcv):
        result = weekly_trend_alignment(trending_up_ohlcv)
        # After warmup, should be bullish in a 500-bar uptrend
        assert result.iloc[-1] >= 0


class TestComputeAllIndicators:
    def test_all_new_columns_present(self, trending_up_ohlcv):
        out = compute_all_indicators(trending_up_ohlcv, fib_long_lb=180, fib_short_lb=30)
        for col in ["VWAP20", "RVOL", "OBV", "ROC10", "ROC20",
                    "STOCH_RSI", "MOM_DIVERGENCE", "WEEKLY_TREND"]:
            assert col in out.columns, f"Missing column: {col}"

    def test_classic_columns_still_present(self, trending_up_ohlcv):
        out = compute_all_indicators(trending_up_ohlcv, fib_long_lb=180, fib_short_lb=30)
        for col in ["EMA20", "EMA50", "EMA200", "SMA20", "SMA50", "SMA200",
                    "RSI14", "MACD", "MACD_SIGNAL", "ATR14", "ADX14", "+DI14", "-DI14",
                    "BB_MID20", "BB_UPPER20", "BB_LOWER20", "BB_WIDTH",
                    "PIVOT", "R1", "S1",
                    "fib_long_low", "fib_long_high",
                    "fib_short_low", "fib_short_high"]:
            assert col in out.columns
