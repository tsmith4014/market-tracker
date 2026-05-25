"""Backtest engine tests on synthetic data with known outcomes."""

from __future__ import annotations

from pathlib import Path

import numpy as np
import pandas as pd
import pytest

import backtest as bt


def _build_synthetic_csv(tmp_path: Path, prices: list[float], scores: list[float], symbol: str = "TEST") -> Path:
    """Build a market_tracker.csv with N rows for one symbol.

    prices and scores must be the same length. The CSV has all required
    columns. adx14 is set high enough to pass the default guards.
    """
    assert len(prices) == len(scores)
    n = len(prices)
    df = pd.DataFrame({
        "timestamp_ct": ["2025-01-01T00:00:00"] * n,
        "symbol": [symbol] * n,
        "data_source": ["synthetic"] * n,
        "date": pd.date_range("2023-01-01", periods=n, freq="D").strftime("%Y-%m-%d"),
        "close": prices,
        "composite_score": scores,
        "signal": ["NEUTRAL"] * n,
        "adx14": [30.0] * n,  # well above default min 25
        "atr14": [p * 0.01 for p in prices],  # 1% of close, well below max 12%
        "ema50": [p * 0.95 for p in prices],
        "trend_s": [0.0] * n,
        "momentum_s": [0.0] * n,
        "strength_s": [0.0] * n,
        "vol_s": [0.0] * n,
        "fib_s": [0.0] * n,
        "pivot_s": [0.0] * n,
    })
    path = tmp_path / "market_tracker.csv"
    df.to_csv(path, index=False)
    return path


@pytest.fixture
def default_cfg() -> dict:
    return {
        "defaults": {
            "weights": {"trend": 0.5, "momentum": 0.2, "strength": 0.15, "vol": 0.1, "fib": 0.03, "pivot": 0.02},
            "thresholds": {"long": 30, "short": -30},
            "lookbacks": {"fib_long": 180, "fib_short": 30},
            "guards": {
                "min_adx_for_signal": 25,
                "max_atr_pct": 12.0,
                "require_close_above_ema50_for_long": False,
                "require_close_below_ema50_for_short": False,
            },
            "fees": {"bps_per_side": 2.0, "slippage_bps_per_side": 1.0},
        },
        "overrides": {},
    }


class TestLoadData:
    def test_filters_symbols_below_min_bars(self, tmp_path, monkeypatch):
        monkeypatch.setattr(bt, "MIN_BACKTEST_BARS", 252)
        path = _build_synthetic_csv(tmp_path, [100.0] * 100, [0.0] * 100, symbol="TOO_SHORT")
        df = bt.load_data(str(path))
        assert df.empty

    def test_dedupes_on_symbol_date(self, tmp_path, monkeypatch):
        monkeypatch.setattr(bt, "MIN_BACKTEST_BARS", 5)
        df = pd.DataFrame({
            "timestamp_ct": ["2025-01-01T00:00:00", "2025-01-01T12:00:00"] + ["2025-01-02T00:00:00"] * 4,
            "symbol": ["TEST"] * 6,
            "data_source": ["synthetic"] * 6,
            "date": ["2025-01-01"] * 2 + ["2025-01-02", "2025-01-03", "2025-01-04", "2025-01-05"],
            "close": [100.0, 105.0, 110.0, 115.0, 120.0, 125.0],
            "composite_score": [10.0, 20.0, 30.0, 40.0, 50.0, 60.0],
            "signal": ["NEUTRAL"] * 6,
            "adx14": [30.0] * 6, "atr14": [1.0] * 6, "ema50": [95.0] * 6,
            "trend_s": [0.0] * 6, "momentum_s": [0.0] * 6, "strength_s": [0.0] * 6,
            "vol_s": [0.0] * 6, "fib_s": [0.0] * 6, "pivot_s": [0.0] * 6,
        })
        path = tmp_path / "dup.csv"
        df.to_csv(path, index=False)
        loaded = bt.load_data(str(path))
        # Two rows for 2025-01-01 should dedupe to one (later timestamp wins)
        assert len(loaded) == 5
        first_row = loaded[loaded["date"] == "2025-01-01"].iloc[0]
        assert first_row["close"] == 105.0


class TestSimulateSymbol:
    def test_insufficient_bars_returns_skipped(self, default_cfg, monkeypatch):
        monkeypatch.setattr(bt, "MIN_BACKTEST_BARS", 252)
        scfg = bt.apply_overrides("TEST", default_cfg)
        df = pd.DataFrame({"symbol": ["TEST"] * 50, "date": pd.date_range("2025-01-01", periods=50)})
        _, stats = bt.simulate_symbol(df, scfg, "TEST", 30.0, -30.0)
        assert stats["skipped_reason"] == "insufficient_bars"
        assert stats["trades"] == 0

    def test_all_neutral_scores_produces_no_trades(self, tmp_path, default_cfg, monkeypatch):
        monkeypatch.setattr(bt, "MIN_BACKTEST_BARS", 252)
        # Scores all below long threshold (30) and above short threshold (-30)
        prices = list(np.linspace(100.0, 110.0, 300))
        scores = [10.0] * 300
        path = _build_synthetic_csv(tmp_path, prices, scores)
        df = bt.load_data(str(path))
        scfg = bt.apply_overrides("TEST", default_cfg)
        trades, stats = bt.simulate_symbol(df, scfg, "TEST", 30.0, -30.0)
        assert stats["trades"] == 0
        assert stats["skipped_reason"] == "no_signals"
        assert trades.empty

    def test_persistent_long_signal_produces_one_entry_and_one_exit(self, tmp_path, default_cfg, monkeypatch):
        """With LONG score for 100 bars then NEUTRAL for the rest, we expect
        exactly one enter_long and one exit_long event."""
        monkeypatch.setattr(bt, "MIN_BACKTEST_BARS", 252)
        prices = list(np.linspace(100.0, 200.0, 300))
        # 50 bars neutral, then 200 bars LONG, then 50 bars neutral
        scores = [0.0] * 50 + [50.0] * 200 + [0.0] * 50
        path = _build_synthetic_csv(tmp_path, prices, scores)
        df = bt.load_data(str(path))
        scfg = bt.apply_overrides("TEST", default_cfg)
        trades, stats = bt.simulate_symbol(df, scfg, "TEST", 30.0, -30.0)
        # 2 trade events: enter_long, exit_long
        assert stats["trades"] == 2
        assert "enter_long" in trades["event"].tolist()
        assert "exit_long" in trades["event"].tolist()

    def test_buy_and_hold_uptrend_makes_money(self, tmp_path, default_cfg, monkeypatch):
        """Going long for the entire run of a rising market should beat benchmark cost-adjusted
        only marginally (1 round-trip cost). Strategy return ~= benchmark return - costs."""
        monkeypatch.setattr(bt, "MIN_BACKTEST_BARS", 252)
        prices = list(np.linspace(100.0, 200.0, 300))  # +100% over the period
        # All bars LONG
        scores = [50.0] * 300
        path = _build_synthetic_csv(tmp_path, prices, scores)
        df = bt.load_data(str(path))
        scfg = bt.apply_overrides("TEST", default_cfg)
        _, stats = bt.simulate_symbol(df, scfg, "TEST", 30.0, -30.0)
        # Benchmark: ~100% return (200/100 - 1). Strategy compounds the same with 1 round-trip cost.
        # Cost is 3 bps each side * 2 sides = ~6 bps total ≈ negligible relative to ~100%.
        assert stats["return"] > 0.5, f"Expected substantial profit, got {stats['return']:.4f}"
        assert stats["benchmark_return"] > 0.9
        assert stats["exposure"] > 0.99, "Should be fully invested except final bar"

    def test_short_in_downtrend_makes_money(self, tmp_path, default_cfg, monkeypatch):
        monkeypatch.setattr(bt, "MIN_BACKTEST_BARS", 252)
        prices = list(np.linspace(200.0, 110.0, 300))  # -45% over period
        scores = [-50.0] * 300  # All SHORT
        path = _build_synthetic_csv(tmp_path, prices, scores)
        df = bt.load_data(str(path))
        scfg = bt.apply_overrides("TEST", default_cfg)
        _, stats = bt.simulate_symbol(df, scfg, "TEST", 30.0, -30.0)
        # Short an asset that fell 45% should make money
        assert stats["return"] > 0.2
        assert stats["benchmark_return"] < -0.4  # long benchmark would lose money

    def test_costs_eat_into_returns(self, tmp_path, default_cfg, monkeypatch):
        """Strategy return should equal benchmark return minus transaction costs
        (for an always-long position with 1 round-trip)."""
        monkeypatch.setattr(bt, "MIN_BACKTEST_BARS", 252)
        prices = list(np.linspace(100.0, 110.0, 300))
        scores = [50.0] * 300
        path = _build_synthetic_csv(tmp_path, prices, scores)
        df = bt.load_data(str(path))
        scfg = bt.apply_overrides("TEST", default_cfg)
        _, stats = bt.simulate_symbol(df, scfg, "TEST", 30.0, -30.0)
        # Benchmark ~10%, strategy should be slightly less due to entry cost (no exit since signal persists)
        # cost_per_side = (2 + 1) bps = 0.03%. Only entry hits cost (no forced exit in test).
        assert stats["benchmark_return"] > stats["return"]
        # The gap should be small (essentially one entry cost)
        assert stats["benchmark_return"] - stats["return"] < 0.01

    def test_no_lookahead_last_bar_signal_zeroed(self, tmp_path, default_cfg, monkeypatch):
        """The final bar must not open a fresh position because there's no
        next-bar return to apply against it."""
        monkeypatch.setattr(bt, "MIN_BACKTEST_BARS", 252)
        prices = list(np.linspace(100.0, 200.0, 300))
        # Only the final bar has a LONG signal — should produce zero trades
        scores = [0.0] * 299 + [50.0]
        path = _build_synthetic_csv(tmp_path, prices, scores)
        df = bt.load_data(str(path))
        scfg = bt.apply_overrides("TEST", default_cfg)
        _, stats = bt.simulate_symbol(df, scfg, "TEST", 30.0, -30.0)
        assert stats["trades"] == 0


class TestRunSummary:
    def test_writes_summary_and_trades_csvs(self, tmp_path, default_cfg, monkeypatch):
        monkeypatch.setattr(bt, "MIN_BACKTEST_BARS", 252)
        prices = list(np.linspace(100.0, 200.0, 300))
        scores = [0.0] * 50 + [50.0] * 200 + [0.0] * 50
        path = _build_synthetic_csv(tmp_path, prices, scores, symbol="TEST")
        df = bt.load_data(str(path))
        bt.run_summary(df, default_cfg, str(tmp_path))
        assert (tmp_path / "backtest_summary.csv").exists()
        assert (tmp_path / "backtest_trades_TEST.csv").exists()
        summary = pd.read_csv(tmp_path / "backtest_summary.csv")
        assert "symbol" in summary.columns
        assert "return" in summary.columns
        assert "sharpe" in summary.columns


class TestRunSweep:
    def test_writes_one_sweep_csv_per_symbol(self, tmp_path, default_cfg, monkeypatch):
        monkeypatch.setattr(bt, "MIN_BACKTEST_BARS", 252)
        prices = list(np.linspace(100.0, 200.0, 300))
        scores = [50.0] * 300
        path = _build_synthetic_csv(tmp_path, prices, scores, symbol="TEST")
        df = bt.load_data(str(path))
        bt.run_sweep(df, default_cfg, str(tmp_path), range(20, 41, 10))
        sweep_path = tmp_path / "threshold_sweep_TEST.csv"
        assert sweep_path.exists()
        sweep_df = pd.read_csv(sweep_path)
        assert sweep_df["threshold"].tolist() == [20, 30, 40]


class TestSharpeGuard:
    def test_sharpe_nan_for_too_few_returns(self):
        assert np.isnan(bt.annualized_sharpe(pd.Series([0.01])))
        assert np.isnan(bt.annualized_sharpe(pd.Series([], dtype=float)))

    def test_sharpe_nan_for_zero_std(self):
        # All zero returns -> std is 0 -> Sharpe must be NaN, not inf
        result = bt.annualized_sharpe(pd.Series([0.0] * 100))
        assert np.isnan(result)

    def test_sharpe_finite_for_real_returns(self):
        rng = np.random.default_rng(seed=42)
        returns = pd.Series(rng.normal(0.001, 0.01, 252))
        result = bt.annualized_sharpe(returns)
        assert np.isfinite(result)


class TestMaxDrawdown:
    def test_no_drawdown_in_monotonic_uptrend(self):
        equity = pd.Series(np.linspace(1.0, 2.0, 100))
        assert bt.max_drawdown(equity) == pytest.approx(0.0, abs=1e-9)

    def test_drawdown_calculated_correctly(self):
        equity = pd.Series([1.0, 1.5, 1.2, 1.0, 1.4])
        # Peak at 1.5, then trough at 1.0 -> drawdown = (1.0 - 1.5) / 1.5 = -0.333
        assert bt.max_drawdown(equity) == pytest.approx(-1 / 3, abs=1e-6)
