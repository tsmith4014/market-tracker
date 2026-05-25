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
    for col in ["close", "composite_score", "adx14", "atr14", "ema50", "trend_s", "momentum_s", "strength_s", "vol_s", "fib_s", "pivot_s"]:
        df[col] = pd.to_numeric(df[col], errors="coerce")
    df = df.dropna(subset=["symbol", "date", "close", "composite_score"])
    df = df.sort_values(["symbol", "date", "timestamp_ct"]).drop_duplicates(subset=["symbol", "date"], keep="last")
    counts = df["symbol"].value_counts()
    valid_symbols = counts[counts >= MIN_BACKTEST_BARS].index
    return df[df["symbol"].isin(valid_symbols)].sort_values(["symbol", "date"]).reset_index(drop=True)


def apply_guards_row(row: pd.Series, cfg: SymbolCfg, raw_signal: str) -> str:
    if raw_signal == "NEUTRAL":
        return "NEUTRAL"
    min_adx = float(cfg.guards.get("min_adx_for_signal", 0))
    max_atr_pct = float(cfg.guards.get("max_atr_pct", 999))
    adx14 = row.get("adx14"); atr14 = row.get("atr14"); close = row.get("close"); ema50 = row.get("ema50")
    if pd.isna(adx14) or adx14 < min_adx:
        return "NEUTRAL"
    if not pd.isna(close) and not pd.isna(atr14) and 100.0 * atr14 / close > max_atr_pct:
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


def simulate_symbol(df: pd.DataFrame, sym_cfg: SymbolCfg, symbol: str, long_th: float, short_th: float) -> Tuple[pd.DataFrame, dict]:
    d = df[df["symbol"] == symbol].copy().reset_index(drop=True)
    empty_stats = {"symbol": symbol, "trades": 0, "return": 0.0, "benchmark_return": 0.0, "mdd": 0.0, "sharpe": np.nan, "exposure": 0.0}
    if d.empty:
        return pd.DataFrame(), {**empty_stats, "skipped_reason": "no_data"}
    if len(d) < MIN_BACKTEST_BARS:
        return pd.DataFrame(), {**empty_stats, "skipped_reason": "insufficient_bars"}

    fee = float(sym_cfg.fees.get("bps_per_side", 1.0)) / 10000.0
    slip = float(sym_cfg.fees.get("slippage_bps_per_side", 1.0)) / 10000.0
    cost_per_side = fee + slip

    d["raw_signal_name"] = np.where(d["composite_score"] >= long_th, "LONG", np.where(d["composite_score"] <= short_th, "SHORT", "NEUTRAL"))
    d["guarded_signal_name"] = [apply_guards_row(row, sym_cfg, row["raw_signal_name"]) for _, row in d.iterrows()]
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


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--mode", choices=["summary", "sweep", "both"], default="summary")
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
    if args.mode in ("sweep", "both"):
        run_sweep(df, cfg, OUT_DIR, range(args.min, args.max + 1, args.step))
    print(f"Outputs in {OUT_DIR}")


if __name__ == "__main__":
    main()
