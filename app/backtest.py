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
    if d.empty: return pd.DataFrame(), {"symbol": symbol, "trades": 0, "return": 0.0, "mdd": 0.0, "sharpe": 0.0}

    fee = float(sym_cfg.fees.get("bps_per_side", 1.0)) / 10000.0
    slip = float(sym_cfg.fees.get("slippage_bps_per_side", 1.0)) / 10000.0
    cost_per_side = fee + slip

    pos = "FLAT"; trades = []; entry_price = None; trail_stop = None

    for _, row in d.iterrows():
        close = row["close"]; score = row["composite_score"]
        raw = "LONG" if score >= long_th else ("SHORT" if score <= short_th else "NEUTRAL")
        sig = apply_guards_row(row, sym_cfg, raw)

        if pos == "LONG" and use_trailing_atr_mult > 0 and not pd.isna(row["atr14"]):
            trail_stop = max(trail_stop or -np.inf, close - use_trailing_atr_mult * row["atr14"])
        elif pos == "SHORT" and use_trailing_atr_mult > 0 and not pd.isna(row["atr14"]):
            trail_stop = min(trail_stop or np.inf, close + use_trailing_atr_mult * row["atr14"])

        exit_reason = None
        if pos == "LONG" and trail_stop is not None and close < trail_stop: exit_reason = "trail_stop"
        if pos == "SHORT" and trail_stop is not None and close > trail_stop: exit_reason = "trail_stop"

        if pos == "FLAT":
            if sig == "LONG":
                entry = close * (1 + cost_per_side)
                pos, entry_price, trail_stop = "LONG", entry, None
                trades.append({"date": row["date"], "action": "BUY", "price": entry, "reason": "signal"})
            elif sig == "SHORT":
                entry = close * (1 - cost_per_side)
                pos, entry_price, trail_stop = "SHORT", entry, None
                trades.append({"date": row["date"], "action": "SELL_SHORT", "price": entry, "reason": "signal"})
        elif pos == "LONG":
            if exit_reason or sig == "SHORT":
                exit_p = close * (1 - cost_per_side)
                trades.append({"date": row["date"], "action": "SELL", "price": exit_p, "reason": exit_reason or "flip"})
                pos, entry_price, trail_stop = "FLAT", None, None
                if sig == "SHORT":
                    entry = close * (1 - cost_per_side)
                    pos, entry_price = "SHORT", entry
                    trades.append({"date": row["date"], "action": "SELL_SHORT", "price": entry, "reason": "flip"})
        elif pos == "SHORT":
            if exit_reason or sig == "LONG":
                exit_p = close * (1 + cost_per_side)
                trades.append({"date": row["date"], "action": "COVER", "price": exit_p, "reason": exit_reason or "flip"})
                pos, entry_price, trail_stop = "FLAT", None, None
                if sig == "LONG":
                    entry = close * (1 + cost_per_side)
                    pos, entry_price = "LONG", entry
                    trades.append({"date": row["date"], "action": "BUY", "price": entry, "reason": "flip"})

    if pos != "FLAT" and entry_price is not None:
        last_close = d.iloc[-1]["close"]
        if pos == "LONG":
            exit_p = last_close * (1 - cost_per_side)
            trades.append({"date": d.iloc[-1]["date"], "action": "SELL", "price": exit_p, "reason": "EOD"})
        else:
            exit_p = last_close * (1 + cost_per_side)
            trades.append({"date": d.iloc[-1]["date"], "action": "COVER", "price": exit_p, "reason": "EOD"})

    tdf = pd.DataFrame(trades)
    if tdf.empty: return tdf, {"symbol": symbol, "trades": 0, "return": 0.0, "mdd": 0.0, "sharpe": 0.0}

    tdf["date"] = pd.to_datetime(tdf["date"])
    pnl = []; stack = []
    for _, tr in tdf.iterrows():
        if tr["action"] in ("BUY","SELL_SHORT"):
            stack.append(tr)
        else:
            if stack:
                en = stack.pop(0)
                if en["action"] == "BUY":
                    ret = (tr["price"] - en["price"]) / en["price"]; side = "LONG"
                else:
                    ret = (en["price"] - tr["price"]) / en["price"]; side = "SHORT"
                pnl.append({"entry_date": en["date"], "exit_date": tr["date"], "side": side, "ret": ret})
    pdf = pd.DataFrame(pnl)
    if pdf.empty: return tdf, {"symbol": symbol, "trades": 0, "return": 0.0, "mdd": 0.0, "sharpe": 0.0}

    total_ret = (1.0 + pdf["ret"]).prod() - 1.0
    d2 = d[["date","close","trend_s","momentum_s","strength_s","vol_s","fib_s","pivot_s"]].copy()
    d2["strat_ret"] = 0.0
    for _, r in pdf.iterrows():
        mask = (d2["date"]>=r["entry_date"]) & (d2["date"]<=r["exit_date"])
        n = mask.sum()
        if n>0: d2.loc[mask, "strat_ret"] += r["ret"]/n
    d2["equity"] = (1.0 + d2["strat_ret"]).cumprod()
    peak = d2["equity"].cummax()
    mdd = ((d2["equity"] - peak)/peak).min()
    sharpe = (d2["strat_ret"].mean() / (d2["strat_ret"].std() + 1e-12)) * np.sqrt(252)

    attrib = {
        "trend_s_mean": d2["trend_s"].mean(),
        "momentum_s_mean": d2["momentum_s"].mean(),
        "strength_s_mean": d2["strength_s"].mean(),
        "vol_s_mean": d2["vol_s"].mean(),
        "fib_s_mean": d2["fib_s"].mean(),
        "pivot_s_mean": d2["pivot_s"].mean()
    }

    return tdf, {"symbol": symbol, "trades": int(len(pdf)), "return": float(total_ret),
                 "mdd": float(mdd), "sharpe": float(sharpe), **attrib}

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
