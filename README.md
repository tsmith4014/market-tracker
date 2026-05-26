# Market Tracker (Crypto + Stocks + ETFs + DXY)

Market Tracker pulls daily OHLCV data, computes technical indicators, creates a weighted composite score from `-100` to `+100`, generates `LONG` / `SHORT` / `NEUTRAL` signals, backtests the signal rules, runs threshold sweeps, and writes a Markdown report.

This repo is designed to be useful in two modes:

1. **Historical mode**: rebuilds a clean, backtest-ready `market_tracker.csv` from recent market history.
2. **Latest mode**: appends/deduplicates the latest scored row per symbol.

The default Docker and GitHub Actions path uses **historical mode** because it makes the backtest/report pipeline useful immediately instead of waiting for hundreds of daily appends.

## What's new

- **Real test suite** with 94 tests across indicators, scoring, guards, storage idempotency, and the backtest engine on synthetic data with known outcomes.
- **RSI bug fix**: previous version returned `50.0` (neutral) for pure uptrends/downtrends when all rolling returns had the same sign. Now correctly returns `100` in pure uptrends and `0` in pure downtrends.
- **Symbol catalog cleanup**: removed `MATIC-USD` (Polygon migrated to POL token; Kraken pair dead) and `FTM-USD` (Fantom rebranded to Sonic; similar issue). Fixed Dogecoin Kraken mapping to canonical `XDGUSD`.
- **CI hardening**: split lint+test job from pipeline job; ruff linting on every PR; concurrency lock; scoped permissions; job timeouts.
- **Lint passes cleanly** on tests and is silenced for pre-existing legacy style issues in `app/`.

## Data sources

The tracker uses real market data only. It does not generate mock OHLCV rows.

- **Crypto**: Kraken → Coinbase → CoinGecko OHLC → CoinPaprika fallback chain.
- **Stocks / ETFs / indices**: Stooq → Yahoo Finance fallback chain.
- **DXY**: configured as `DXY-INDEX` using Yahoo Finance symbol `DX-Y.NYB`.

No API key is required for the primary data path.

## What gets generated

Generated outputs are written to `data/` locally or uploaded as GitHub Actions artifacts in CI:

- `market_tracker.csv` — master CSV with one scored row per (symbol, date)
- `series_<SYMBOL>.csv` when `EXPORT_SERIES=true` — full indicator series per symbol
- `backtest_summary.csv` — backtest stats per symbol
- `backtest_trades_<SYMBOL>.csv` — entry/exit/reversal events per symbol
- `threshold_sweep_<SYMBOL>.csv` — threshold optimization grid
- `backtest_report.md` — human-readable Markdown summary

The repository does **not** commit generated CSV data by default. GitHub Actions uploads generated outputs as an artifact instead.

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

### Running tests locally without Docker

```bash
python -m pip install -r app/requirements.txt -r app/requirements-dev.txt
PYTHONPATH=app pytest
PYTHONPATH=app pytest tests/test_indicators.py -v
ruff check .
```

## Configuration

Edit `app/config.json` to tune per-asset weights, thresholds, guards, lookbacks, and fees.

Supported config blocks:

- `weights`: `trend`, `momentum`, `strength`, `vol`, `fib`, `pivot` (renormalized at score time if any subscore is unavailable)
- `thresholds`: `long`, `short` (long must exceed short)
- `lookbacks`: `fib_long`, `fib_short`
- `guards`: `min_adx_for_signal`, `max_atr_pct`, `require_close_above_ema50_for_long`, `require_close_below_ema50_for_short`
- `fees`: `bps_per_side`, `slippage_bps_per_side`

## Runtime environment variables

| Variable | Default | Purpose |
|---|---:|---|
| `OUTPUT_PATH` | `/data/market_tracker.csv` | Tracker output CSV |
| `CONFIG_PATH` | `/app/config.json` | Strategy config path |
| `SYMBOLS_PATH` | `/app/symbols.json` in Docker, repo-local file outside Docker | Symbol catalog path |
| `DAYS_CRYPTO` | `730` | Crypto history window |
| `DAYS_EQUITY` | `800d` | Stock/ETF/index history window |
| `OUTPUT_MODE` | `historical` | `historical` or `latest` |
| `WRITE_MODE` | `replace` for historical, `append` for latest | CSV write behavior |
| `EXPORT_SERIES` | `false` | Write per-symbol indicator series files |
| `SERIES_DIR` | `/data` | Per-symbol series output directory |
| `TRACK_CRYPTO` | `major,defi,layer1,layer2,infrastructure,meme` | Crypto categories from `symbols.json` |
| `TRACK_STOCKS` | all stock groups in `symbols.json` (see catalog) | Stock categories from `symbols.json` |
| `OUTPUT_JSON_PATH` | `/data/copilot_signals.json` | Full co-pilot JSON output |
| `OUTPUT_LATEST_PATH` | `/data/latest_signals.json` | Slim latest-signals JSON |
| `TRACK_ALL` | `false` | If `true`, track every symbol in `symbols.json` |
| `TRACK_INDICES` | `true` | Include ETF/index symbols |
| `TRACK_SYMBOLS` | empty | Exact comma-separated symbol override |
| `MIN_BACKTEST_BARS` | `252` | Minimum rows per symbol for backtesting |
| `LOG_LEVEL` | `INFO` | Python logging level |
| `HTTP_TIMEOUT_SECONDS` | `30` | HTTP timeout for data source calls |
| `REQUEST_DELAY_SECONDS` | `0.5` | Inter-request delay for crypto APIs |

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

The workflow has three jobs (see [docs/DISTRIBUTION.md](docs/DISTRIBUTION.md) for Slack / OpenClaw / Pages):

1. **lint-and-test** — runs on every PR. Ruff + pytest.
2. **run-pipeline** — daily at **03:07 UTC** and on manual **workflow_dispatch** (not on PRs). Tracks **~161 symbols**, writes CSV + JSON, runs backtest/sweep/report, uploads a **30-day artifact**.
3. **distribute** — on `main` only: optional **Slack** webhook post, publishes **GitHub Pages** with `latest_signals.json`, `copilot_signals.json`, and `backtest_report.md`.

**Setup for downstream consumers:**

| Integration | What to configure |
|-------------|-------------------|
| Slack | Repo secret `SLACK_WEBHOOK_URL` |
| GitHub Pages | Repo → Settings → Pages → source: **Deploy from branch** → branch `gh-pages` (created automatically by CI) |
| OpenClaw / agents | Poll `https://<user>.github.io/market-tracker/copilot_signals.json` |

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
- Execution is modeled using next-bar returns: a signal computed at bar `t`'s close earns the close-to-close return from `t` to `t+1`. The final bar cannot open a fresh position because there is no next-bar return.
- Transaction cost is `bps_per_side + slippage_bps_per_side` from config, applied on each position change.
- Historical Fibonacci levels are computed from data available up to each row. The backtest does not use future rows to calculate prior Fibonacci levels.
- Sharpe ratio is `NaN` when there are fewer than 2 returns or when return std-dev is effectively zero — preventing the divide-by-zero blow-ups that produced `-1.2e+12` Sharpe values in earlier reports.
- `backtest_trades_<SYMBOL>.csv` contains position-change events labeled as `enter_long`, `enter_short`, `exit_long`, `exit_short`, `reverse_long_to_short`, or `reverse_short_to_long`.

## Test suite layout

```
tests/
├── conftest.py              # Shared fixtures: synthetic OHLCV (up/down/flat), default config
├── test_indicators.py       # EMA/SMA/RSI/MACD/ATR/ADX/Bollinger/pivots/fib (24 tests)
├── test_scoring.py          # Subscores + composite + guards (31 tests)
├── test_storage.py          # CSV schema + write_rows idempotency (14 tests)
├── test_backtest.py         # Backtest engine on synthetic data with known outcomes (16 tests)
└── test_pipeline.py         # End-to-end OHLCV → indicators → scoring → output rows (9 tests)
```

Total: **94 tests**, all passing.

## Good next enhancements

This PR-sized foundation intentionally avoids overbuilding. The next valuable layers are:

1. A small dashboard for latest signal, score history, and backtest charts.
2. ~~Slack alerting~~ — webhook notify added in CI; tune message format as needed.
3. Walk-forward optimization for thresholds and weights.
4. Database persistence if CSV artifacts become too limiting.
5. Provider reliability reporting across runs.
6. Vectorize `detect_swing` — currently O(N × lookback); fine for 730 days × 30 symbols but worth optimizing if symbol count grows.
