"""Shared pytest fixtures."""

from __future__ import annotations

import json
from pathlib import Path

import numpy as np
import pandas as pd
import pytest


@pytest.fixture
def trending_up_ohlcv() -> pd.DataFrame:
    """500 bars of steadily rising prices with small intrabar noise.

    Designed so trend indicators (EMA stack, ADX) come out strongly positive
    and signals/composite score are firmly LONG with default config.
    """
    rng = np.random.default_rng(seed=42)
    n = 500
    base = np.linspace(100.0, 200.0, n)
    noise = rng.normal(0, 0.5, n)
    close = base + noise
    high = close + np.abs(rng.normal(0, 0.4, n)) + 0.1
    low = close - np.abs(rng.normal(0, 0.4, n)) - 0.1
    open_ = close + rng.normal(0, 0.2, n)
    volume = rng.integers(900_000, 1_100_000, n).astype(float)
    return pd.DataFrame(
        {
            "Date": pd.date_range("2023-01-01", periods=n, freq="D"),
            "Open": open_,
            "High": np.maximum.reduce([open_, close, high]),
            "Low": np.minimum.reduce([open_, close, low]),
            "Close": close,
            "Volume": volume,
        }
    )


@pytest.fixture
def trending_down_ohlcv() -> pd.DataFrame:
    """500 bars of steadily falling prices. Mirror of trending_up."""
    rng = np.random.default_rng(seed=7)
    n = 500
    base = np.linspace(200.0, 100.0, n)
    noise = rng.normal(0, 0.5, n)
    close = base + noise
    high = close + np.abs(rng.normal(0, 0.4, n)) + 0.1
    low = close - np.abs(rng.normal(0, 0.4, n)) - 0.1
    open_ = close + rng.normal(0, 0.2, n)
    volume = rng.integers(900_000, 1_100_000, n).astype(float)
    return pd.DataFrame(
        {
            "Date": pd.date_range("2023-01-01", periods=n, freq="D"),
            "Open": open_,
            "High": np.maximum.reduce([open_, close, high]),
            "Low": np.minimum.reduce([open_, close, low]),
            "Close": close,
            "Volume": volume,
        }
    )


@pytest.fixture
def flat_ohlcv() -> pd.DataFrame:
    """500 bars of roughly flat prices around 100. Used to verify NEUTRAL signals."""
    rng = np.random.default_rng(seed=13)
    n = 500
    close = 100.0 + rng.normal(0, 0.3, n)
    high = close + np.abs(rng.normal(0, 0.2, n)) + 0.05
    low = close - np.abs(rng.normal(0, 0.2, n)) - 0.05
    open_ = close + rng.normal(0, 0.1, n)
    volume = rng.integers(900_000, 1_100_000, n).astype(float)
    return pd.DataFrame(
        {
            "Date": pd.date_range("2023-01-01", periods=n, freq="D"),
            "Open": open_,
            "High": np.maximum.reduce([open_, close, high]),
            "Low": np.minimum.reduce([open_, close, low]),
            "Close": close,
            "Volume": volume,
        }
    )


@pytest.fixture
def default_symbol_cfg() -> dict:
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


@pytest.fixture
def tmp_symbols_file(tmp_path: Path) -> Path:
    """A minimal symbols.json on disk that the manager can load."""
    data = {
        "crypto": {
            "major": [
                {
                    "symbol": "BTC-USD",
                    "name": "Bitcoin",
                    "kraken": "XBTUSD",
                    "coinbase": "BTC-USD",
                    "coingecko": "bitcoin",
                },
            ],
            "defi": [],
        },
        "stocks": {
            "tech_mega_caps": [
                {
                    "symbol": "AAPL",
                    "name": "Apple Inc.",
                    "stooq": "aapl.us",
                    "yfinance": "AAPL",
                    "sector": "technology",
                },
            ],
        },
        "indices": [
            {
                "symbol": "SPY",
                "name": "SPDR S&P 500 ETF",
                "stooq": "spy.us",
                "yfinance": "SPY",
            }
        ],
    }
    path = tmp_path / "symbols.json"
    path.write_text(json.dumps(data))
    return path
