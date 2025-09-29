#!/usr/bin/env python3
import os, json, math, argparse
from dataclasses import dataclass
from typing import Dict, List, Tuple
import pandas as pd
import numpy as np

CONFIG_PATH = os.getenv("CONFIG_PATH", "/app/config.json")
CSV_PATH = os.getenv("CSV_PATH", "/data/market_tracker.csv")
OUT_DIR = os.getenv("OUT_DIR", "/data")

@dataclass
class SymbolCfg:
    weights: dict
    thresholds: dict
    lookbacks: dict
    guards: dict
    fees: dict

def load_config(path: str) -> dict:
    with open(path, "r") as f:
        return json.load(f)

def apply_overrides(symbol: str, cfg: dict) -> SymbolCfg:
    d = cfg.get("defaults", {})
    o = cfg.get("overrides", {}).get(symbol, {})
    merged = {
        "weights": {**d.get("weights", {}), **o.get("weights", {})},
        "thresholds": {**d.get("thresholds", {}), **o.get("thresholds", {})},
        "lookbacks": {**d.get("lookbacks", {}), **o.get("lookbacks", {})},
        "guards": {**d.get("guards", {}), **o.get("guards", {})},
        "fees": {**d.get("fees", {}), **o.get("fees", {})}
    }
    return SymbolCfg(**merged)

def load_data(csv_path: str) -> pd.DataFrame:
    df = pd.read_csv(csv_path)
    required = {"timestamp_ct","symbol","date","close","composite_score","signal","adx14","atr14","ema50",
                "trend_s","momentum_s","strength_s","vol_s","fib_s","pivot_s"}
    missing = required - set(df.columns)
    if missing: raise ValueError(f"CSV missing required columns: {missing}")
    df["date"] = pd.to_datetime(df["date"])
    
    # Ensure we have enough data for each symbol
    symbol_counts = df["symbol"].value_counts()
    valid_symbols = symbol_counts[symbol_counts >= 252].index
    df = df[df["symbol"].isin(valid_symbols)]
    
    return df.sort_values(["symbol","date"]).reset_index(drop=True)

def apply_guards_row(row: pd.Series, cfg: SymbolCfg, raw_signal: str) -> str:
    if raw_signal == "NEUTRAL": return "NEUTRAL"
    min_adx = float(cfg.guards.get("min_adx_for_signal", 0))
    max_atr_pct = float(cfg.guards.get("max_atr_pct", 999))
    adx14 = row.get("adx14"); atr14 = row.get("atr14"); close = row.get("close"); ema50 = row.get("ema50")
    if pd.isna(adx14) or adx14 < min_adx: return "NEUTRAL"
    if not pd.isna(close) and not pd.isna(atr14) and 100.0 * atr14 / close > max_atr_pct: return "NEUTRAL"
    if cfg.guards.get("require_close_above_ema50_for_long", False) and raw_signal == "LONG":
        if pd.isna(close) or pd.isna(ema50) or not (close > ema50): return "NEUTRAL"
    if cfg.guards.get("require_close_below_ema50_for_short", False) and raw_signal == "SHORT":
        if pd.isna(close) or pd.isna(ema50) or not (close < ema50): return "NEUTRAL"
    return raw_signal

def simulate_symbol(df: pd.DataFrame, sym_cfg: SymbolCfg, symbol: str,
                    long_th: float, short_th: float,
                    use_trailing_atr_mult: float = 1.5) -> Tuple[pd.DataFrame, dict]:
    d = df[df["symbol"] == symbol].copy().reset_index(drop=True)
    if d.empty: return pd.DataFrame(), {"symbol": symbol, "trades": 0, "return": 0.0, "mdd": 0.0, "sharpe": 0.0, "skipped_reason": "no_data"}

    # Check minimum bars requirement - need at least 252 bars for meaningful backtest
    if len(d) < 252:
        return pd.DataFrame(), {"symbol": symbol, "trades": 0, "return": 0.0, "mdd": 0.0, "sharpe": 0.0, "skipped_reason": "insufficient_bars"}

    fee = float(sym_cfg.fees.get("bps_per_side", 1.0)) / 10000.0
    slip = float(sym_cfg.fees.get("slippage_bps_per_side", 1.0)) / 10000.0
    cost_per_side = fee + slip

    # Generate signals
    d["raw_signal"] = np.where(d["composite_score"] >= long_th, 1, 
                              np.where(d["composite_score"] <= short_th, -1, 0))
    
    # Apply guards
    d["signal"] = d["raw_signal"].copy()
    for idx, row in d.iterrows():
        if row["raw_signal"] != 0:
            raw = "LONG" if row["raw_signal"] > 0 else "SHORT"
            guarded = apply_guards_row(row, sym_cfg, raw)
            d.loc[idx, "signal"] = 1 if guarded == "LONG" else (-1 if guarded == "SHORT" else 0)

    # No fresh entries on last bar (next-bar execution)
    d.loc[d.index[-1], "signal"] = 0

    # Calculate position changes and returns
    d["position"] = d["signal"].fillna(0)
    d["position_change"] = d["position"].diff().fillna(0)
    d["next_close"] = d["close"].shift(-1)
    d["return"] = d["close"].pct_change().shift(-1)
    
    # Calculate P&L with proper transaction costs
    d["trade_cost"] = np.where(d["position_change"] != 0, cost_per_side, 0)
    d["strategy_return"] = d["position"] * d["return"] - d["trade_cost"]
    
    # Calculate equity curve
    d["equity"] = (1 + d["strategy_return"].fillna(0)).cumprod()
    
    # Calculate metrics
    total_return = d["equity"].iloc[-1] - 1.0
    peak = d["equity"].cummax()
    drawdown = (d["equity"] - peak) / peak
    max_drawdown = drawdown.min()
    
    # Calculate Sharpe ratio with proper guards
    strategy_returns = d["strategy_return"].dropna()
    if len(strategy_returns) < 2:
        sharpe = np.nan
    else:
        mean_ret = strategy_returns.mean()
        std_ret = strategy_returns.std()
        if std_ret < 1e-8:
            sharpe = np.nan
        else:
            sharpe = (mean_ret * 252) / (std_ret * np.sqrt(252))
    
    # Count actual trades (position changes)
    trades = int((d["position_change"] != 0).sum())
    
    # Calculate attribution metrics
    valid_subscores = {}
    for col in ["trend_s", "momentum_s", "strength_s", "vol_s", "fib_s", "pivot_s"]:
        if col in d.columns:
            values = d[col].dropna()
            if len(values) > 0 and np.isfinite(values).all():
                valid_subscores[f"{col}_mean"] = float(values.mean())
            else:
                valid_subscores[f"{col}_mean"] = np.nan
        else:
            valid_subscores[f"{col}_mean"] = np.nan

    # Determine skipped reason
    skipped_reason = "ok"
    if trades == 0:
        if (d["raw_signal"] != 0).sum() == 0:
            skipped_reason = "no_signals"
        else:
            skipped_reason = "guards_blocked"
    elif not np.isfinite(total_return):
        skipped_reason = "invalid_returns"
    elif abs(total_return) > 1.0:
        skipped_reason = "extreme_returns"
    elif np.isfinite(sharpe) and abs(sharpe) > 20:
        skipped_reason = "extreme_sharpe"

    result = {
        "symbol": symbol, 
        "trades": trades, 
        "return": float(total_return),
        "mdd": float(max_drawdown), 
        "sharpe": float(sharpe) if np.isfinite(sharpe) else np.nan,
        "skipped_reason": skipped_reason,
        **valid_subscores
    }

    return pd.DataFrame(), result

def run_summary(df: pd.DataFrame, cfg: dict, out_dir: str):
    os.makedirs(out_dir, exist_ok=True)
    syms = sorted(df["symbol"].unique().tolist())
    rows = []
    for sym in syms:
        scfg = apply_overrides(sym, cfg)
        lt, st = float(scfg.thresholds["long"]), float(scfg.thresholds["short"])
        trades, stats = simulate_symbol(df, scfg, sym, lt, st, use_trailing_atr_mult=1.5)
        trades.to_csv(os.path.join(out_dir, f"backtest_trades_{sym}.csv"), index=False)
        rows.append(stats)
    pd.DataFrame(rows).to_csv(os.path.join(out_dir, "backtest_summary.csv"), index=False)

def run_sweep(df: pd.DataFrame, cfg: dict, out_dir: str, grid):
    os.makedirs(out_dir, exist_ok=True)
    syms = sorted(df["symbol"].unique().tolist())
    for sym in syms:
        scfg = apply_overrides(sym, cfg)
        recs = []
        for th in grid:
            lt, st = float(th), float(-th)
            _, stats = simulate_symbol(df, scfg, sym, lt, st, use_trailing_atr_mult=1.5)
            recs.append({"symbol": sym, "threshold": th, **stats})
        pd.DataFrame(recs).to_csv(os.path.join(out_dir, f"threshold_sweep_{sym}.csv"), index=False)

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--mode", choices=["summary","sweep","both"], default="summary")
    p.add_argument("--min", type=int, default=15)
    p.add_argument("--max", type=int, default=50)
    p.add_argument("--step", type=int, default=5)
    a = p.parse_args()

    cfg = load_config(CONFIG_PATH)
    df = load_data(CSV_PATH)

    if a.mode in ("summary","both"): run_summary(df, cfg, OUT_DIR)
    if a.mode in ("sweep","both"): run_sweep(df, cfg, OUT_DIR, range(a.min, a.max+1, a.step))
    print(f"Outputs in {OUT_DIR}")

if __name__ == "__main__":
    main()
