#!/usr/bin/env python3
from __future__ import annotations

import argparse
from dataclasses import dataclass
import json
import os
from pathlib import Path
from typing import Tuple

import numpy as np
import pandas as pd

import strategies

CONFIG_PATH = os.getenv("CONFIG_PATH", "/app/config.json")
CSV_PATH = os.getenv("CSV_PATH", "/data/market_tracker.csv")
OUT_DIR = os.getenv("OUT_DIR", "/data")
MIN_BACKTEST_BARS = int(os.getenv("MIN_BACKTEST_BARS", "252"))


@dataclass(frozen=True)
class SymbolCfg:
    weights: dict
    thresholds: dict
    lookbacks: dict
    guards: dict
    fees: dict


def load_config(path: str) -> dict:
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def apply_overrides(symbol: str, cfg: dict) -> SymbolCfg:
    d = cfg.get("defaults", {})
    o = cfg.get("overrides", {}).get(symbol, {})
    return SymbolCfg(
        weights={**d.get("weights", {}), **o.get("weights", {})},
        thresholds={**d.get("thresholds", {}), **o.get("thresholds", {})},
        lookbacks={**d.get("lookbacks", {}), **o.get("lookbacks", {})},
        guards={**d.get("guards", {}), **o.get("guards", {})},
        fees={**d.get("fees", {}), **o.get("fees", {})},
    )


def load_data(csv_path: str) -> pd.DataFrame:
    df = pd.read_csv(csv_path)
    required = {"timestamp_ct", "symbol", "date", "close", "composite_score", "signal", "adx14", "atr14", "ema50", "trend_s", "momentum_s", "strength_s", "vol_s", "fib_s", "pivot_s"}
    missing = required - set(df.columns)
    if missing:
        raise ValueError(f"CSV missing required columns: {sorted(missing)}")
    df["date"] = pd.to_datetime(df["date"])
    numeric_cols = ["close", "composite_score", "adx14", "atr14", "ema50", "trend_s", "momentum_s", "strength_s", "vol_s", "fib_s", "pivot_s"]
    # Columns needed by the mean-reversion / adaptive strategies (optional in older CSVs).
    numeric_cols += [c for c in ["rsi14", "bb_lower20", "bb_upper20", "ema200"] if c in df.columns]
    for col in numeric_cols:
        df[col] = pd.to_numeric(df[col], errors="coerce")
    df = df.dropna(subset=["symbol", "date", "close", "composite_score"])
    df = df.sort_values(["symbol", "date", "timestamp_ct"]).drop_duplicates(subset=["symbol", "date"], keep="last")
    counts = df["symbol"].value_counts()
    valid_symbols = counts[counts >= MIN_BACKTEST_BARS].index
    return df[df["symbol"].isin(valid_symbols)].sort_values(["symbol", "date"]).reset_index(drop=True)


def apply_guards_row(row: pd.Series, cfg: SymbolCfg, raw_signal: str, strategy: str = strategies.TREND) -> str:
    if raw_signal == "NEUTRAL":
        return "NEUTRAL"
    max_atr_pct = float(cfg.guards.get("max_atr_pct", 999))
    adx14 = row.get("adx14"); atr14 = row.get("atr14"); close = row.get("close"); ema50 = row.get("ema50")
    # The extreme-volatility guard applies to every strategy.
    if not pd.isna(close) and not pd.isna(atr14) and 100.0 * atr14 / close > max_atr_pct:
        return "NEUTRAL"
    # Trend-style guards (ADX floor, EMA proximity) only gate trend-driven rows.
    adx_val = None if pd.isna(adx14) else float(adx14)
    if not strategies.uses_trend_guards(strategy, adx_val):
        return raw_signal
    min_adx = float(cfg.guards.get("min_adx_for_signal", 0))
    if pd.isna(adx14) or adx14 < min_adx:
        return "NEUTRAL"
    if cfg.guards.get("require_close_above_ema50_for_long", False) and raw_signal == "LONG" and (pd.isna(close) or pd.isna(ema50) or close <= ema50):
        return "NEUTRAL"
    if cfg.guards.get("require_close_below_ema50_for_short", False) and raw_signal == "SHORT" and (pd.isna(close) or pd.isna(ema50) or close >= ema50):
        return "NEUTRAL"
    return raw_signal


def max_drawdown(equity: pd.Series) -> float:
    peak = equity.cummax()
    drawdown = (equity - peak) / peak.replace(0, np.nan)
    return float(drawdown.min()) if len(drawdown) else 0.0


def annualized_sharpe(returns: pd.Series) -> float:
    clean = returns.dropna()
    if len(clean) < 2:
        return np.nan
    std = clean.std()
    if not np.isfinite(std) or std < 1e-8:
        return np.nan
    return float((clean.mean() * 252) / (std * np.sqrt(252)))


def build_trade_events(d: pd.DataFrame, symbol: str, cost_per_side: float) -> pd.DataFrame:
    events = d[d["position_change"] != 0].copy()
    if events.empty:
        return pd.DataFrame(columns=["symbol", "date", "close", "previous_position", "new_position", "event", "cost_per_side"])

    def event_name(row: pd.Series) -> str:
        previous = row["previous_position"]
        current = row["position"]
        if previous == 0 and current > 0: return "enter_long"
        if previous == 0 and current < 0: return "enter_short"
        if previous > 0 and current == 0: return "exit_long"
        if previous < 0 and current == 0: return "exit_short"
        if previous > 0 and current < 0: return "reverse_long_to_short"
        if previous < 0 and current > 0: return "reverse_short_to_long"
        return "position_change"

    return pd.DataFrame({
        "symbol": symbol,
        "date": events["date"].dt.date.astype(str),
        "close": events["close"].astype(float),
        "previous_position": events["previous_position"].astype(int),
        "new_position": events["position"].astype(int),
        "event": events.apply(event_name, axis=1),
        "cost_per_side": cost_per_side,
    })


def _row_raw_signal(row: pd.Series, strategy: str, long_th: float, short_th: float) -> str:
    return strategies.raw_signal(
        strategy,
        score=strategies._f(row.get("composite_score")),
        long_th=long_th,
        short_th=short_th,
        close=strategies._f(row.get("close")),
        rsi14=strategies._f(row.get("rsi14")),
        bb_lower20=strategies._f(row.get("bb_lower20")),
        bb_upper20=strategies._f(row.get("bb_upper20")),
        ema200=strategies._f(row.get("ema200")),
        adx14=strategies._f(row.get("adx14")),
    )


def simulate_symbol(df: pd.DataFrame, sym_cfg: SymbolCfg, symbol: str, long_th: float, short_th: float, strategy: str = strategies.TREND, min_bars: int | None = None) -> Tuple[pd.DataFrame, dict]:
    min_bars = MIN_BACKTEST_BARS if min_bars is None else min_bars
    d = df[df["symbol"] == symbol].copy().reset_index(drop=True)
    empty_stats = {"symbol": symbol, "trades": 0, "return": 0.0, "benchmark_return": 0.0, "mdd": 0.0, "sharpe": np.nan, "exposure": 0.0}
    if d.empty:
        return pd.DataFrame(), {**empty_stats, "skipped_reason": "no_data"}
    if len(d) < min_bars:
        return pd.DataFrame(), {**empty_stats, "skipped_reason": "insufficient_bars"}

    fee = float(sym_cfg.fees.get("bps_per_side", 1.0)) / 10000.0
    slip = float(sym_cfg.fees.get("slippage_bps_per_side", 1.0)) / 10000.0
    cost_per_side = fee + slip

    d["raw_signal_name"] = [_row_raw_signal(row, strategy, long_th, short_th) for _, row in d.iterrows()]
    d["guarded_signal_name"] = [apply_guards_row(row, sym_cfg, row["raw_signal_name"], strategy) for _, row in d.iterrows()]
    d["signal_numeric"] = d["guarded_signal_name"].map({"LONG": 1, "SHORT": -1, "NEUTRAL": 0}).fillna(0).astype(int)
    d.loc[d.index[-1], "signal_numeric"] = 0
    d["position"] = d["signal_numeric"]
    d["previous_position"] = d["position"].shift(1).fillna(0).astype(int)
    d["position_change"] = d["position"] - d["previous_position"]
    d["asset_return"] = d["close"].pct_change().shift(-1)
    d["trade_cost"] = np.where(d["position_change"] != 0, abs(d["position_change"]) * cost_per_side, 0.0)
    d["strategy_return"] = (d["position"] * d["asset_return"] - d["trade_cost"]).replace([np.inf, -np.inf], np.nan).fillna(0.0)
    d["equity"] = (1 + d["strategy_return"]).cumprod()

    trades = build_trade_events(d, symbol, cost_per_side)
    total_return = float(d["equity"].iloc[-1] - 1.0)
    benchmark_return = float((d["close"].iloc[-1] / d["close"].iloc[0]) - 1.0)
    skipped_reason = "ok"
    if trades.empty:
        skipped_reason = "no_signals" if int((d["raw_signal_name"] != "NEUTRAL").sum()) == 0 else "guards_blocked"
    elif not np.isfinite(total_return):
        skipped_reason = "invalid_returns"

    attribution = {}
    for col in ["trend_s", "momentum_s", "strength_s", "vol_s", "fib_s", "pivot_s"]:
        values = d[col].dropna() if col in d.columns else pd.Series(dtype=float)
        attribution[f"{col}_mean"] = float(values.mean()) if len(values) else np.nan

    stats = {
        "symbol": symbol,
        "trades": int(len(trades)),
        "return": total_return,
        "benchmark_return": benchmark_return,
        "mdd": max_drawdown(d["equity"]),
        "sharpe": annualized_sharpe(d["strategy_return"]),
        "exposure": float((d["position"] != 0).mean()),
        "skipped_reason": skipped_reason,
        **attribution,
    }
    return trades, stats


def run_summary(df: pd.DataFrame, cfg: dict, out_dir: str) -> pd.DataFrame:
    Path(out_dir).mkdir(parents=True, exist_ok=True)
    rows = []
    for symbol in sorted(df["symbol"].unique()):
        scfg = apply_overrides(symbol, cfg)
        trades, stats = simulate_symbol(df, scfg, symbol, float(scfg.thresholds["long"]), float(scfg.thresholds["short"]))
        trades.to_csv(Path(out_dir) / f"backtest_trades_{symbol}.csv", index=False)
        rows.append(stats)
    summary = pd.DataFrame(rows)
    summary.to_csv(Path(out_dir) / "backtest_summary.csv", index=False)
    return summary


def run_sweep(df: pd.DataFrame, cfg: dict, out_dir: str, grid: range) -> None:
    Path(out_dir).mkdir(parents=True, exist_ok=True)
    for symbol in sorted(df["symbol"].unique()):
        scfg = apply_overrides(symbol, cfg)
        records = []
        for threshold in grid:
            _, stats = simulate_symbol(df, scfg, symbol, float(threshold), float(-threshold))
            records.append({"symbol": symbol, "threshold": threshold, **stats})
        pd.DataFrame(records).to_csv(Path(out_dir) / f"threshold_sweep_{symbol}.csv", index=False)


def calibrate_signals(df: pd.DataFrame, horizons: Tuple[int, ...] = (5, 10, 20)) -> pd.DataFrame:
    """Measure whether signals (and confidence buckets) actually predict forward returns.

    For each non-NEUTRAL signal we compute the realized forward return over each
    horizon in the signal's own direction (LONG = +ret, SHORT = -ret). Grouping the
    directional returns by confidence level reveals whether HIGH-confidence calls
    outperform LOW ones — the core test of whether the score carries information.

    Returns a tidy frame: one row per (confidence_level, horizon) plus an ALL row.
    """
    dir_map = {"LONG": 1, "SHORT": -1, "NEUTRAL": 0}
    has_confidence = "confidence_level" in df.columns
    frames = []
    for symbol in df["symbol"].unique():
        d = df[df["symbol"] == symbol].sort_values("date").copy()
        d["dir"] = d["signal"].map(dir_map).fillna(0)
        for h in horizons:
            fwd = d["close"].shift(-h) / d["close"] - 1.0
            sub = pd.DataFrame({
                "horizon": h,
                "confidence_level": d["confidence_level"] if has_confidence else "ALL",
                "dir": d["dir"],
                "directional_return": fwd * d["dir"],
            })
            frames.append(sub[(sub["dir"] != 0) & sub["directional_return"].notna()])

    if not frames:
        return pd.DataFrame(columns=["confidence_level", "horizon", "n", "mean_return", "median_return", "win_rate"])

    events = pd.concat(frames, ignore_index=True)

    def _agg(group: pd.DataFrame) -> dict:
        return {
            "n": int(len(group)),
            "mean_return": float(group["directional_return"].mean()),
            "median_return": float(group["directional_return"].median()),
            "win_rate": float((group["directional_return"] > 0).mean()),
        }

    rows = []
    for h in horizons:
        h_events = events[events["horizon"] == h]
        for level in ["HIGH", "MEDIUM", "LOW", "ALL"]:
            bucket = h_events if level == "ALL" else h_events[h_events["confidence_level"] == level]
            if bucket.empty:
                continue
            rows.append({"confidence_level": level, "horizon": h, **_agg(bucket)})
    return pd.DataFrame(rows)


def run_calibration(df: pd.DataFrame, out_dir: str, horizons: Tuple[int, ...] = (5, 10, 20)) -> pd.DataFrame:
    Path(out_dir).mkdir(parents=True, exist_ok=True)
    calib = calibrate_signals(df, horizons)
    calib.to_csv(Path(out_dir) / "signal_calibration.csv", index=False)
    return calib


def _aggregate_edge(stats_rows: list, strategy: str, scope: str) -> dict:
    """Roll up per-symbol stats into one edge verdict for a strategy/scope."""
    traded = [s for s in stats_rows if s.get("trades", 0) > 0 and np.isfinite(s.get("return", np.nan))]
    n = len(traded)
    if n == 0:
        return {"strategy": strategy, "scope": scope, "symbols": 0, "beat_benchmark_pct": np.nan,
                "positive_pct": np.nan, "median_return": np.nan, "median_benchmark": np.nan,
                "median_excess": np.nan, "median_sharpe": np.nan, "total_trades": 0}
    ret = np.array([s["return"] for s in traded])
    bench = np.array([s["benchmark_return"] for s in traded])
    sharpe = np.array([s["sharpe"] for s in traded], dtype=float)
    return {
        "strategy": strategy,
        "scope": scope,
        "symbols": n,
        "beat_benchmark_pct": float(np.mean(ret > bench)),
        "positive_pct": float(np.mean(ret > 0)),
        "median_return": float(np.median(ret)),
        "median_benchmark": float(np.median(bench)),
        "median_excess": float(np.median(ret - bench)),
        "median_sharpe": float(np.nanmedian(sharpe)),
        "total_trades": int(sum(s["trades"] for s in traded)),
    }


def _oos_slice(df: pd.DataFrame, oos_fraction: float) -> pd.DataFrame:
    """Take the most recent `oos_fraction` of each symbol's history (unseen tail)."""
    parts = []
    for _symbol, g in df.groupby("symbol", sort=False):
        g = g.sort_values("date")
        k = max(1, int(round(len(g) * oos_fraction)))
        parts.append(g.tail(k))
    return pd.concat(parts, ignore_index=True) if parts else df.iloc[0:0]


def compare_strategies(df: pd.DataFrame, cfg: dict, out_dir: str, oos_fraction: float = 0.35, oos_min_bars: int = 60) -> pd.DataFrame:
    """Backtest every strategy variant and report which carries edge.

    Reports both the full sample and an out-of-sample tail so a variant that
    only looks good in-sample is exposed. Returns the comparison frame.
    """
    Path(out_dir).mkdir(parents=True, exist_ok=True)
    oos_df = _oos_slice(df, oos_fraction)
    symbols = sorted(df["symbol"].unique())
    records = []
    for strategy in strategies.STRATEGIES:
        full_stats, oos_stats = [], []
        for symbol in symbols:
            scfg = apply_overrides(symbol, cfg)
            lo, sh = float(scfg.thresholds["long"]), float(scfg.thresholds["short"])
            _, fs = simulate_symbol(df, scfg, symbol, lo, sh, strategy=strategy)
            full_stats.append(fs)
            _, os_ = simulate_symbol(oos_df, scfg, symbol, lo, sh, strategy=strategy, min_bars=oos_min_bars)
            oos_stats.append(os_)
        records.append(_aggregate_edge(full_stats, strategy, "full"))
        records.append(_aggregate_edge(oos_stats, strategy, "out_of_sample"))
    comparison = pd.DataFrame(records)
    comparison.to_csv(Path(out_dir) / "strategy_comparison.csv", index=False)
    return comparison


# --- Portfolio backtest -----------------------------------------------------
#
# Everything above evaluates each symbol in isolation. Real deployment is a
# *portfolio*: capital is split across many names at once. Cross-sectional
# construction (rank the universe, hold the best, short the worst) is where the
# most robust edge tends to live, and a market-neutral book can earn a positive
# Sharpe regardless of market direction. This compares deployable portfolios
# against an equal-weight buy-and-hold benchmark, full-sample and out-of-sample.

HIGH_CONF_THRESHOLD = 0.65


def _portfolio_metrics(port: pd.Series) -> dict:
    clean = port.dropna()
    if len(clean) < 2:
        return {"ann_return": np.nan, "ann_vol": np.nan, "sharpe": np.nan, "max_drawdown": np.nan, "total_return": np.nan}
    ann_return = float(clean.mean() * 252)
    ann_vol = float(clean.std() * np.sqrt(252))
    sharpe = float(ann_return / ann_vol) if ann_vol > 1e-9 else np.nan
    equity = (1 + clean).cumprod()
    return {
        "ann_return": ann_return,
        "ann_vol": ann_vol,
        "sharpe": sharpe,
        "max_drawdown": max_drawdown(equity),
        "total_return": float(equity.iloc[-1] - 1.0),
    }


def _gross_normalize(raw: pd.DataFrame) -> pd.DataFrame:
    gross = raw.abs().sum(axis=1)
    return raw.div(gross.where(gross > 0, np.nan), axis=0).fillna(0.0)


def _conviction_ls_weights(signed: pd.DataFrame, avail: pd.DataFrame, top_quantile: float) -> pd.DataFrame:
    """Market-neutral book: long the highest signed conviction, short the lowest."""
    rows = []
    for dt in signed.index:
        row = signed.loc[dt].where(avail.loc[dt], 0.0)
        row = row[row != 0]
        w = pd.Series(0.0, index=signed.columns)
        if not row.empty:
            k = max(1, int(round(top_quantile * int(avail.loc[dt].sum()))))
            longs = row[row > 0].nlargest(k).index
            shorts = row[row < 0].nsmallest(k).index
            if len(longs):
                w[longs] = 0.5 / len(longs)
            if len(shorts):
                w[shorts] = -0.5 / len(shorts)
        rows.append(w)
    return pd.DataFrame(rows, index=signed.index)


def portfolio_backtest(df: pd.DataFrame, cfg: dict, out_dir: str, top_quantile: float = 0.1, oos_fraction: float = 0.35) -> pd.DataFrame:
    Path(out_dir).mkdir(parents=True, exist_ok=True)
    d = df.copy()
    d["signal_dir"] = d["signal"].map({"LONG": 1, "SHORT": -1, "NEUTRAL": 0}).fillna(0)
    d["conf"] = pd.to_numeric(d.get("confidence_score"), errors="coerce").fillna(0.0)

    close = d.pivot_table(index="date", columns="symbol", values="close", aggfunc="last").sort_index()
    if close.shape[0] < 30 or close.shape[1] < 3:
        empty = pd.DataFrame(columns=["strategy", "scope", "ann_return", "ann_vol", "sharpe", "max_drawdown", "total_return", "avg_gross_exposure"])
        empty.to_csv(Path(out_dir) / "portfolio_comparison.csv", index=False)
        return empty

    sig = d.pivot_table(index="date", columns="symbol", values="signal_dir", aggfunc="last").reindex(index=close.index, columns=close.columns).fillna(0.0)
    conf = d.pivot_table(index="date", columns="symbol", values="conf", aggfunc="last").reindex(index=close.index, columns=close.columns).fillna(0.0)
    avail = close.notna()
    fwd = close.pct_change().shift(-1)  # return realized from t to t+1 (no look-ahead)

    fees = cfg.get("defaults", {}).get("fees", {})
    cost = (float(fees.get("bps_per_side", 1.0)) + float(fees.get("slippage_bps_per_side", 1.0))) / 10000.0

    # Weight books (decided at close t).
    ew_long = avail.div(avail.sum(axis=1).where(lambda s: s > 0, np.nan), axis=0).fillna(0.0)
    books = {
        "equal_weight_buyhold": ew_long,
        "all_signals_ew": _gross_normalize(sig),
        "high_conf_ew": _gross_normalize(sig.where(conf >= HIGH_CONF_THRESHOLD, 0.0)),
        "conviction_long_short": _conviction_ls_weights(sig * conf, avail, top_quantile),
    }

    dates = close.index
    oos_start = dates[int(len(dates) * (1 - oos_fraction))]
    records = []
    for name, W in books.items():
        W = W.reindex(index=close.index, columns=close.columns).fillna(0.0)
        gross_ret = (W * fwd).sum(axis=1)
        turnover = (W - W.shift(1).fillna(0.0)).abs().sum(axis=1)
        port = (gross_ret - turnover * cost).replace([np.inf, -np.inf], np.nan)
        gross_exposure = float(W.abs().sum(axis=1).mean())
        for scope, series in (("full", port), ("out_of_sample", port.loc[oos_start:])):
            records.append({"strategy": name, "scope": scope, **_portfolio_metrics(series), "avg_gross_exposure": round(gross_exposure, 3)})

    comparison = pd.DataFrame(records)
    comparison.to_csv(Path(out_dir) / "portfolio_comparison.csv", index=False)
    return comparison


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--mode", choices=["summary", "sweep", "calibrate", "compare", "portfolio", "both"], default="summary")
    parser.add_argument("--min", type=int, default=15)
    parser.add_argument("--max", type=int, default=50)
    parser.add_argument("--step", type=int, default=5)
    args = parser.parse_args()
    cfg = load_config(CONFIG_PATH)
    df = load_data(CSV_PATH)
    if df.empty:
        raise ValueError(f"No symbols with at least {MIN_BACKTEST_BARS} rows were found in {CSV_PATH}")
    if args.mode in ("summary", "both"):
        run_summary(df, cfg, OUT_DIR)
        run_calibration(df, OUT_DIR)
        compare_strategies(df, cfg, OUT_DIR)
        portfolio_backtest(df, cfg, OUT_DIR)
    if args.mode in ("sweep", "both"):
        run_sweep(df, cfg, OUT_DIR, range(args.min, args.max + 1, args.step))
    if args.mode == "calibrate":
        run_calibration(df, OUT_DIR)
    if args.mode == "compare":
        compare_strategies(df, cfg, OUT_DIR)
    if args.mode == "portfolio":
        portfolio_backtest(df, cfg, OUT_DIR)
    print(f"Outputs in {OUT_DIR}")


if __name__ == "__main__":
    main()
