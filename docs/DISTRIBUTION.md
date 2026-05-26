# Distributing Market Tracker Outputs

The daily GitHub Actions pipeline produces machine-readable outputs for downstream tools.

## Generated files

| File | Purpose |
|------|---------|
| `copilot_signals.json` | Full payload: signals, confidence, regime, data quality (OpenClaw / LLM agents) |
| `latest_signals.json` | Slim polling file: symbol, signal, score, confidence |
| `market_tracker.csv` | Historical scored rows for backtests |
| `backtest_report.md` | Human-readable summary |

## GitHub Actions

- **Schedule:** daily at 03:07 UTC (`cron: 7 3 * * *`)
- **Manual run:** Actions → Market Tracker → Run workflow
- **Artifacts:** `market-tracker-output` (30-day retention) on every non-PR run
- **GitHub Pages:** publishes `latest_signals.json`, `copilot_signals.json`, and `backtest_report.md` when Pages is enabled on the repo

### Public URLs (after Pages deploy)

Replace `OWNER` and `REPO` with your GitHub org/user and repository name:

- Dashboard: `https://OWNER.github.io/REPO/`
- Latest signals: `https://OWNER.github.io/REPO/latest_signals.json`
- Co-pilot JSON: `https://OWNER.github.io/REPO/copilot_signals.json`

### GitHub Pages settings (important)

CI publishes to the **`gh-pages` branch** (not `main`). In the repo:

**Settings → Pages → Build and deployment**

1. **Source:** Deploy from a branch  
2. **Branch:** `gh-pages` / `(root)`  
3. Click **Save**

The `gh-pages` branch is created automatically on the first successful **`distribute`** job (after **run-pipeline** completes on `main`). Until then, the branch will not appear in the dropdown.

Trigger a run: **Actions → Market Tracker → Run workflow** (branch `main`).

## Slack

1. Create a Slack [Incoming Webhook](https://api.slack.com/messaging/webhooks).
2. Add repository secret: **`SLACK_WEBHOOK_URL`**
3. The `distribute` job posts a daily summary after each successful pipeline run.

## OpenClaw / agents

Point your agent at the published JSON (or download the Actions artifact):

```text
https://OWNER.github.io/REPO/copilot_signals.json
```

The payload includes `summary`, `market_regime`, `signals[]` with confidence and levels — designed for trade co-pilot consumption.

## Local / Docker

Same files are written to `./data/` when you run `make run-tracker`.
