# Market Tracker (Crypto + Stocks + ETFs + DXY)

Market Tracker pulls daily OHLCV data, computes technical indicators, creates a weighted composite score from `-100` to `+100`, generates `LONG` / `SHORT` / `NEUTRAL` signals, backtests the signal rules, runs threshold sweeps, and writes a Markdown report.

This repo is designed to be useful in two modes:

1. **Historical mode**: rebuilds a clean, backtest-ready `market_tracker.csv` from recent market history.
2. **Latest mode**: appends/deduplicates the latest scored row per symbol.

The default Docker and GitHub Actions path uses **historical mode** because it makes the backtest/report pipeline useful immediately instead of waiting for hundreds of daily appends.

## Data sources

The tracker uses real market data only. It does not generate mock OHLCV rows.

- **Crypto**: Kraken -> Coinbase -> CoinGecko OHLC -> CoinPaprika fallback chain.
- **Stocks / ETFs / indices**: Stooq -> Yahoo Finance fallback chain.
- **DXY**: configured as `DXY-INDEX` using Yahoo Finance symbol `DX-Y.NYB`.

No API key is required for the primary data path.

## What gets generated

Generated outputs are written to `data/` locally or uploaded as GitHub Actions artifacts in CI:

- `market_tracker.csv`
- `series_<SYMBOL>.csv` when `EXPORT_SERIES=true`
- `backtest_summary.csv`
- `backtest_trades_<SYMBOL>.csv`
- `threshold_sweep_<SYMBOL>.csv`
- `backtest_report.md`

The repository does **not** commit generated CSV data by default. This avoids noisy daily data commits and keeps Git focused on source code. GitHub Actions uploads generated outputs as an artifact instead.

## Quick start

```bash
# Build image
docker compose build

# Run tests
docker compose run --rm test

# 1) Build a backtest-ready historical CSV and per-symbol series files
docker compose run --rm tracker

# 2) Backtest current thresholds and guards
docker compose run --rm backtest

# 3) Sweep thresholds per asset from 15..50 by 5
docker compose run --rm sweep

# 4) Generate Markdown report
docker compose run --rm report

# Inspect outputs
ls -lh data/
```

## Configuration

Edit `app/config.json` to tune per-asset weights, thresholds, guards, lookbacks, and fees.

Supported config blocks:

- `weights`: `trend`, `momentum`, `strength`, `vol`, `fib`, `pivot`
- `thresholds`: `long`, `short`
- `lookbacks`: `fib_long`, `fib_short`
- `guards`: `min_adx_for_signal`, `max_atr_pct`, `require_close_above_ema50_for_long`, `require_close_below_ema50_for_short`
- `fees`: `bps_per_side`, `slippage_bps_per_side`

## Runtime environment variables

| Variable | Default | Purpose |
|---|---:|---|
| `OUTPUT_PATH` | `/data/market_tracker.csv` | Tracker output CSV |
| `CONFIG_PATH` | `/app/config.json` | Strategy config path |
| `SYMBOLS_PATH` | `/app/symbols.json` in Docker, repo-local file outside Docker | Symbol catalog path |
| `DAYS_CRYPTO` | `365` | Crypto history window |
| `DAYS_EQUITY` | `400d` | Stock/ETF/index history window |
| `OUTPUT_MODE` | `historical` | `historical` or `latest` |
| `WRITE_MODE` | `replace` for historical, `append` for latest | CSV write behavior |
| `EXPORT_SERIES` | `false` | Write per-symbol indicator series files |
| `SERIES_DIR` | `/data` | Per-symbol series output directory |
| `TRACK_CRYPTO` | `major,defi` | Crypto categories from `symbols.json` |
| `TRACK_STOCKS` | `tech_mega_caps,semiconductors` | Stock categories from `symbols.json` |
| `TRACK_INDICES` | `true` | Include ETF/index symbols |
| `TRACK_SYMBOLS` | empty | Exact comma-separated symbol override |
| `MIN_BACKTEST_BARS` | `252` | Minimum rows per symbol for backtesting |
| `LOG_LEVEL` | `INFO` | Python logging level |

Examples:

```bash
# Track exact symbols only
docker compose run --rm \
  -e TRACK_SYMBOLS="BTC-USD,ETH-USD,NVDA,AMD,DXY-INDEX" \
  tracker

# Append only the latest scored rows instead of rebuilding history
docker compose run --rm \
  -e OUTPUT_MODE=latest \
  -e WRITE_MODE=append \
  tracker
```

## Symbol catalog CLI

```bash
# Show stats
python app/symbol_search.py --stats

# Search by name/symbol/category/sector
python app/symbol_search.py --search bitcoin
python app/symbol_search.py --search semiconductor

# List categories/sectors
python app/symbol_search.py --list-categories
python app/symbol_search.py --list-sectors

# Export the symbol catalog
python app/symbol_search.py --export symbols_export.json
```

## GitHub Actions

The scheduled workflow runs daily and also supports manual `workflow_dispatch` runs. It:

1. Installs dependencies.
2. Runs the test suite.
3. Generates historical market data.
4. Runs summary backtests.
5. Runs threshold sweeps.
6. Generates the Markdown report.
7. Uploads the generated `data/` directory as a workflow artifact.

Optional S3 upload can be enabled by configuring these repo secrets and uncommenting the S3 upload block in `.github/workflows/market-tracker.yml`:

- `AWS_ACCESS_KEY_ID`
- `AWS_SECRET_ACCESS_KEY`
- `AWS_REGION`
- `S3_BUCKET`

## Host cron alternative

```cron
# m h dom mon dow  command
5 22 * * * cd /path/to/market-tracker && docker compose run --rm tracker >> /var/log/market-tracker.log 2>&1
10 22 * * * cd /path/to/market-tracker && docker compose run --rm backtest >> /var/log/market-backtest.log 2>&1
15 22 * * * cd /path/to/market-tracker && docker compose run --rm sweep >> /var/log/market-sweep.log 2>&1
20 22 * * * cd /path/to/market-tracker && docker compose run --rm report >> /var/log/market-report.log 2>&1
```

## Backtest assumptions

- Signals are generated from composite score thresholds and then filtered through the same guard rules used by the tracker.
- Execution is modeled using next-bar returns. The final bar cannot open a fresh position because there is no next close available.
- Transaction cost is `bps_per_side + slippage_bps_per_side` from config.
- Historical Fibonacci levels are computed from data available up to each row. The backtest does not use future rows to calculate prior Fibonacci levels.
- `backtest_trades_<SYMBOL>.csv` contains position-change events, including entries, exits, and reversals.

## Good next enhancements

This PR-sized foundation intentionally avoids overbuilding. The next valuable layers are:

1. A small dashboard for latest signal, score history, and backtest charts.
2. Slack/email alerting for signal changes.
3. Walk-forward optimization for thresholds and weights.
4. Database persistence if CSV artifacts become too limiting.
5. Provider reliability reporting across runs.
