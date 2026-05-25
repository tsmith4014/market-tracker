#!/usr/bin/env python3
from __future__ import annotations

from datetime import datetime, timezone
import os
from pathlib import Path

import pandas as pd

OUT_DIR = Path(os.getenv("OUT_DIR", "/data"))
REPORT_PATH = Path(os.getenv("REPORT_PATH", "/data/backtest_report.md"))
MARKET_CSV = Path(os.getenv("MARKET_CSV", str(OUT_DIR / "market_tracker.csv")))


def load_csv(path: Path) -> pd.DataFrame | None:
    return pd.read_csv(path) if path.exists() and path.stat().st_size > 0 else None


def percent(value: float | int | None) -> str:
    if value is None or pd.isna(value):
        return "n/a"
    return f"{float(value) * 100:.2f}%"


def number(value: float | int | None, digits: int = 2) -> str:
    if value is None or pd.isna(value):
        return "n/a"
    return f"{float(value):.{digits}f}"


def latest_signal_table(market: pd.DataFrame | None) -> str:
    if market is None or market.empty:
        return "No market tracker rows were available."
    df = market.copy()
    df["date"] = pd.to_datetime(df["date"])
    latest = df.sort_values(["symbol", "date"]).groupby("symbol", as_index=False).tail(1)
    cols = ["symbol", "date", "close", "composite_score", "signal", "data_source"]
    return latest[cols].sort_values(["signal", "symbol"]).to_markdown(index=False)


def data_freshness_summary(market: pd.DataFrame | None) -> list[str]:
    if market is None or market.empty:
        return ["- Market CSV: unavailable"]
    df = market.copy()
    df["date"] = pd.to_datetime(df["date"])
    rows = len(df)
    symbols = df["symbol"].nunique()
    first = df["date"].min().date().isoformat()
    last = df["date"].max().date().isoformat()
    return [
        f"- Rows: **{rows:,}**",
        f"- Symbols: **{symbols:,}**",
        f"- Date range: **{first}** to **{last}**",
    ]


def summary_section(summary: pd.DataFrame | None) -> list[str]:
    lines = ["## Backtest Summary", ""]
    if summary is None or summary.empty:
        lines.extend(["No backtest summary was generated.", ""])
        return lines
    if "skipped_reason" in summary.columns:
        lines.extend(["### Data Quality / Signal Availability", ""])
        for reason, count in summary["skipped_reason"].value_counts(dropna=False).items():
            lines.append(f"- **{reason}**: {count} symbols")
        lines.append("")
    display_cols = [c for c in ["symbol", "trades", "return", "benchmark_return", "mdd", "sharpe", "exposure", "skipped_reason"] if c in summary.columns]
    formatted = summary[display_cols].copy()
    for col in ["return", "benchmark_return", "mdd", "exposure"]:
        if col in formatted.columns:
            formatted[col] = formatted[col].apply(percent)
    if "sharpe" in formatted.columns:
        formatted["sharpe"] = formatted["sharpe"].apply(number)
    lines.append(formatted.to_markdown(index=False))
    lines.append("")
    return lines


def sweep_sections(summary: pd.DataFrame | None) -> list[str]:
    if summary is None or summary.empty or "symbol" not in summary.columns:
        return []
    lines: list[str] = []
    for symbol in sorted(summary["symbol"].dropna().unique()):
        sweep = load_csv(OUT_DIR / f"threshold_sweep_{symbol}.csv")
        if sweep is None or sweep.empty:
            continue
        ranked = sweep.copy()
        ranked["sort_sharpe"] = pd.to_numeric(ranked.get("sharpe"), errors="coerce").fillna(-999)
        ranked["sort_return"] = pd.to_numeric(ranked.get("return"), errors="coerce").fillna(-999)
        top5 = ranked.sort_values(["sort_sharpe", "sort_return"], ascending=[False, False]).head(5)
        display_cols = [c for c in ["threshold", "return", "benchmark_return", "mdd", "sharpe", "trades", "exposure", "skipped_reason"] if c in top5.columns]
        display = top5[display_cols].copy()
        for col in ["return", "benchmark_return", "mdd", "exposure"]:
            if col in display.columns:
                display[col] = display[col].apply(percent)
        if "sharpe" in display.columns:
            display["sharpe"] = display["sharpe"].apply(number)
        lines.extend([f"## {symbol} Threshold Sweep", "", display.to_markdown(index=False), ""])
    return lines


def main() -> None:
    summary = load_csv(OUT_DIR / "backtest_summary.csv")
    market = load_csv(MARKET_CSV)
    generated = datetime.now(timezone.utc).isoformat(timespec="seconds")
    lines: list[str] = [
        "# Market Tracker Backtest Report",
        "",
        f"_Generated: {generated}_",
        "",
        "## Data Sources",
        "",
        "- Crypto: Kraken -> Coinbase -> CoinGecko OHLC -> CoinPaprika fallback chain.",
        "- Stocks / ETFs / indices: Stooq -> Yahoo Finance fallback chain.",
        "- Data rows are generated from real market APIs. Mock OHLCV rows are not generated.",
        "",
        "## Data Freshness",
        "",
        *data_freshness_summary(market),
        "",
        "## Latest Signals",
        "",
        latest_signal_table(market),
        "",
    ]
    lines.extend(summary_section(summary))
    lines.extend(sweep_sections(summary))
    REPORT_PATH.parent.mkdir(parents=True, exist_ok=True)
    REPORT_PATH.write_text("\n".join(lines), encoding="utf-8")
    print(f"Wrote report -> {REPORT_PATH}")


if __name__ == "__main__":
    main()
