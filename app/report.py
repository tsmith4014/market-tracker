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


def edge_summary_section(summary: pd.DataFrame | None) -> list[str]:
    """Aggregate verdict: does the strategy carry an edge over buy-and-hold?"""
    lines = ["## Edge Summary", ""]
    if summary is None or summary.empty or "return" not in summary.columns:
        lines.extend(["No backtest summary available to evaluate edge.", ""])
        return lines

    df = summary.copy()
    for col in ["return", "benchmark_return", "sharpe", "exposure", "trades"]:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce")

    traded = df[df["trades"].fillna(0) > 0] if "trades" in df.columns else df
    evaluated = len(traded)
    if evaluated == 0:
        lines.extend(["No symbols generated trades; edge cannot be evaluated.", ""])
        return lines

    beat = (traded["return"] > traded["benchmark_return"]).mean() if "benchmark_return" in traded.columns else float("nan")
    positive = (traded["return"] > 0).mean()
    excess = (traded["return"] - traded["benchmark_return"]) if "benchmark_return" in traded.columns else traded["return"]

    lines.extend([
        f"- Symbols with trades: **{evaluated}** of {len(df)}",
        f"- Beat buy-and-hold: **{percent(beat)}** of traded symbols",
        f"- Positive return: **{percent(positive)}** of traded symbols",
        f"- Median strategy return: **{percent(traded['return'].median())}** "
        f"(benchmark **{percent(traded['benchmark_return'].median()) if 'benchmark_return' in traded.columns else 'n/a'}**)",
        f"- Median excess vs benchmark: **{percent(excess.median())}**",
        f"- Median Sharpe: **{number(traded['sharpe'].median()) if 'sharpe' in traded.columns else 'n/a'}**",
        f"- Median exposure: **{percent(traded['exposure'].median()) if 'exposure' in traded.columns else 'n/a'}**",
        "",
        "> Edge is real only if both _beat buy-and-hold_ and _median excess_ are "
        "convincingly positive across many symbols. Treat a single high-return symbol as noise.",
        "",
    ])
    return lines


def portfolio_section() -> list[str]:
    """Deployable portfolios vs an equal-weight buy-and-hold benchmark."""
    comp = load_csv(OUT_DIR / "portfolio_comparison.csv")
    lines = ["## Portfolio Backtest", ""]
    if comp is None or comp.empty:
        lines.extend(["No portfolio backtest was generated.", ""])
        return lines
    display = comp.copy()
    for col in ["ann_return", "ann_vol", "max_drawdown", "total_return"]:
        if col in display.columns:
            display[col] = display[col].apply(percent)
    for col in ["sharpe", "avg_gross_exposure"]:
        if col in display.columns:
            display[col] = display[col].apply(number)
    lines.extend([
        "Actual capital-allocation books (not per-symbol averages). "
        "`equal_weight_buyhold` is the benchmark; `conviction_long_short` is market-neutral. "
        "Judge on **Sharpe** and **max_drawdown** out-of-sample, not raw return: a "
        "fully-invested long book wins on return in a bull market but carries all the risk.",
        "",
        display.to_markdown(index=False),
        "",
    ])
    return lines


def strategy_comparison_section() -> list[str]:
    """Which decision rule actually beats buy-and-hold, in- and out-of-sample?"""
    comp = load_csv(OUT_DIR / "strategy_comparison.csv")
    lines = ["## Strategy Comparison", ""]
    if comp is None or comp.empty:
        lines.extend(["No strategy comparison was generated.", ""])
        return lines
    display = comp.copy()
    for col in ["beat_benchmark_pct", "positive_pct", "median_return", "median_benchmark", "median_excess"]:
        if col in display.columns:
            display[col] = display[col].apply(percent)
    if "median_sharpe" in display.columns:
        display["median_sharpe"] = display["median_sharpe"].apply(number)
    lines.extend([
        "Each decision rule backtested over the same data. `out_of_sample` is the "
        "most recent ~35% of each symbol's history (unseen tail). A rule has real "
        "edge only if `median_excess` and `beat_benchmark_pct` stay positive "
        "out-of-sample, not just full-sample.",
        "",
        display.to_markdown(index=False),
        "",
    ])
    return lines


def calibration_section() -> list[str]:
    """Does higher confidence actually predict better forward returns?"""
    calib = load_csv(OUT_DIR / "signal_calibration.csv")
    lines = ["## Signal Calibration", ""]
    if calib is None or calib.empty:
        lines.extend(["No calibration data was generated.", ""])
        return lines
    display = calib.copy()
    for col in ["mean_return", "median_return", "win_rate"]:
        if col in display.columns:
            display[col] = display[col].apply(percent)
    order = {"HIGH": 0, "MEDIUM": 1, "LOW": 2, "ALL": 3}
    if "confidence_level" in display.columns:
        display["_o"] = display["confidence_level"].map(order).fillna(9)
        display = display.sort_values(["horizon", "_o"]).drop(columns="_o")
    lines.extend([
        "Realized forward return in the signal's direction, grouped by confidence. "
        "HIGH should outrank LOW for the confidence score to be meaningful.",
        "",
        display.to_markdown(index=False),
        "",
    ])
    return lines


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
    lines.extend(edge_summary_section(summary))
    lines.extend(portfolio_section())
    lines.extend(strategy_comparison_section())
    lines.extend(calibration_section())
    lines.extend(summary_section(summary))
    lines.extend(sweep_sections(summary))
    REPORT_PATH.parent.mkdir(parents=True, exist_ok=True)
    REPORT_PATH.write_text("\n".join(lines), encoding="utf-8")
    print(f"Wrote report -> {REPORT_PATH}")


if __name__ == "__main__":
    main()
