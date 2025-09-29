#!/usr/bin/env python3
import os
import pandas as pd
from datetime import datetime

OUT_DIR = os.getenv("OUT_DIR", "/data")
REPORT_PATH = os.getenv("REPORT_PATH", "/data/backtest_report.md")

def load_csv(path):
    return pd.read_csv(path) if os.path.exists(path) else None

def main():
    summary_path = os.path.join(OUT_DIR, "backtest_summary.csv")
    summary = load_csv(summary_path)
    symbols = summary["symbol"].unique().tolist() if summary is not None else []

    lines = []
    lines.append("# Backtest Report")
    lines.append("")
    lines.append(f"_Generated: {datetime.utcnow().isoformat()}Z_")
    lines.append("")

    if summary is not None and not summary.empty:
        lines.append("## Summary")
        lines.append("")
        lines.append(summary.to_markdown(index=False))
        lines.append("")

    for sym in symbols:
        sweep_path = os.path.join(OUT_DIR, f"threshold_sweep_{sym}.csv")
        sweep = load_csv(sweep_path)
        if sweep is None or sweep.empty: continue
        best = sweep.sort_values(["sharpe","return"], ascending=[False, False]).head(1)
        lines.append(f"## {sym} — Threshold Sweep")
        lines.append("")
        lines.append(best.to_markdown(index=False))
        lines.append("")
        lines.append("Top 5 thresholds by Sharpe:")
        top5 = sweep.sort_values(["sharpe","return"], ascending=[False, False]).head(5)
        lines.append(top5[["threshold","return","mdd","sharpe","trades"]].to_markdown(index=False))
        lines.append("")

    with open(REPORT_PATH, "w") as f:
        f.write("\n".join(lines))
    print(f"Wrote report -> {REPORT_PATH}")

if __name__ == "__main__":
    main()
