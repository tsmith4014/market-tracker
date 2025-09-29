# Market Tracker (Crypto + Stocks + DXY)

Pulls daily OHLCV (Binance for crypto, Yahoo Finance for equities & DXY), computes indicators, **dual Fibonacci retracements**, **composite score** (−100..+100), **signals**, and appends rows to a master CSV. Includes **backtest**, **threshold sweep**, **subscore attribution**, optional **per-asset series export**, and a Markdown **report**.

## Data sources

- Crypto: Binance Spot klines (SOL, BTC, ETH, XRP) — no API key.
- Equities & Dollar Index: Yahoo Finance (AMD, NVDA, ^DXY).

## Quick start

```bash
# Build images
docker compose build

# 1) Append today's rows to data/market_tracker.csv (and series files)
docker compose run --rm tracker

# 2) Backtest current thresholds and guards (writes summary + trades CSVs)
docker compose run --rm backtest

# 3) Sweep thresholds per asset (15..50 by 5) using the same guards
docker compose run --rm sweep

# 4) Generate Markdown report from the outputs
docker compose run --rm report

# Inspect outputs
ls -l data/
```

Outputs you'll see:

- `market_tracker.csv`
- `series_<SYMBOL>.csv` (if `EXPORT_SERIES=true`)
- `backtest_summary.csv`
- `backtest_trades_<SYMBOL>.csv`
- `threshold_sweep_<SYMBOL>.csv`
- `backtest_report.md`

## Configure assets and behavior

Edit `app/config.json` to tune **per-asset weights/thresholds/guards/lookbacks** (kept in Git for auditability).

- Weights: `{trend, momentum, strength, vol, fib, pivot}`
- Thresholds: `{long, short}` (e.g., 30 / −30)
- Lookbacks: `{fib_long, fib_short}`
- Guards: `{min_adx_for_signal, max_atr_pct, require_close_above_ema50_for_long, require_close_below_ema50_for_short}`
- Fees: `{bps_per_side, slippage_bps_per_side}` for backtest

Env vars (set in `docker-compose.yml`):

- `OUTPUT_PATH` (default `/data/market_tracker.csv`)
- `CONFIG_PATH` (default `/app/config.json`)
- `DAYS_CRYPTO=365`, `DAYS_EQUITY=400d`
- `EXPORT_SERIES=true|false`, `SERIES_DIR=/data`

## Schedule

### Host cron:

```cron
# m h dom mon dow  command
5 22 * * * cd /path/to/market-tracker && docker compose run --rm tracker >> /var/log/market-tracker.log 2>&1
10 22 * * * cd /path/to/market-tracker && docker compose run --rm backtest >> /var/log/market-backtest.log 2>&1
15 22 * * * cd /path/to/market-tracker && docker compose run --rm sweep >> /var/log/market-sweep.log 2>&1
20 22 * * * cd /path/to/market-tracker && docker compose run --rm report >> /var/log/market-report.log 2>&1
```

### GitHub Actions (optional)

A daily job runs tracker + commits `data/market_tracker.csv`, then (optionally) uploads to S3 if secrets exist.

Configure repo secrets if you want S3 upload:

- `AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`, `AWS_REGION` (optional), `S3_BUCKET`

## Notes

- Signals use composite score + guards; backtests use the **same** rules.
- Dual Fibonacci: long/short swings detected over configurable lookbacks.
- All indicators and formulas are standard and deterministic.
