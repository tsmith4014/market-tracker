# Unusual Options Activity × Market Tracker — Integration Contract

This document defines how an external **unusual-options-activity (UOA) scanner**
(e.g. an openclaw skill running on your Mac) feeds the market tracker so the
Slack channel gets *combined* analysis: options flow **cross-referenced** with
the tracker's directional signal, calibrated confidence, and macro regime.

> **Framing:** this is analytical context for **paper trading / education**.
> Neither system places trades. The tracker's directional signal does not beat
> buy-and-hold on its own (see the README "Research Findings"); the value here is
> *confluence* — when independent options flow and the tracker agree.

## Data flow

```
openclaw UOA scanner (your Mac)                market-tracker (CI / Docker)
  └─ writes options_activity.json  ───────────►  scripts/slack_notify.py
                                                   ├─ loads copilot_signals.json
                                                   ├─ options_enrichment.enrich()
                                                   └─ posts combined Slack message
```

The UOA app and the tracker stay fully decoupled. The only coupling is **one
JSON file** the UOA app drops where the tracker's notifier can read it.

## Input the UOA app must emit: `options_activity.json`

```json
{
  "generated_at": "2026-05-29T14:55:00Z",
  "source": "openclaw-uoa",
  "alerts": [
    {
      "symbol": "NVDA",
      "direction": "bullish",
      "type": "call",
      "premium_usd": 1850000,
      "contracts": 6200,
      "sentiment_score": 0.82,
      "strike": 220.0,
      "expiry": "2026-06-20",
      "notes": "repeated ask-side call sweeps"
    }
  ]
}
```

### Field reference

| field | required | meaning |
|-------|----------|---------|
| `symbol` | **yes** | Ticker, matched against the tracker universe (upper-cased). |
| `direction` | preferred | `bullish` / `bearish`. Accepts `call`/`put`, `long`/`short` aliases. If omitted, inferred from `type`. |
| `type` | optional | `call` / `put` — used only to infer direction if `direction` is missing. |
| `premium_usd` | optional | $ notional of the flow. Used to rank/scale alerts. |
| `contracts` | optional | Contract count. |
| `sentiment_score` | optional | 0–1 conviction from your scanner. |
| `strike`, `expiry` | optional | Surfaced in detail views. |
| `notes` | optional | Free text (e.g. "sweeps, ask-side"). |

Unknown fields are ignored; missing optional fields are tolerated.

## OpenClaw `~/.openclaw/.env`

OpenClaw stores **local secrets and config** in `~/.openclaw/.env` (dotenv format).
The gateway and skills read this file; it is **not** committed to git.

`scripts/slack_notify.py` and `scripts/local_daily.sh` automatically load
`~/.openclaw/.env` when `SLACK_WEBHOOK_URL` is not already set in your shell.
Existing shell exports win (we do not override).

Typical keys (names only):

- `SLACK_WEBHOOK_URL` — incoming webhook used by `slack_notify.py`
- `SLACK_BOT_TOKEN` / `SLACK_APP_TOKEN` — used by OpenClaw’s Slack gateway (separate)

Convert heartbeat → tracker feed:

```bash
python3 scripts/openclaw_to_options_activity.py
```

## Wiring it up

Point the notifier at the file with `OPTIONS_JSON` (defaults to
`<DATA_DIR>/options_activity.json`):

```bash
OPTIONS_JSON=/path/to/options_activity.json \
SLACK_WEBHOOK_URL=... \
python scripts/slack_notify.py
```

If the file is absent or empty, the notifier posts the normal tracker summary
with **no** options section — the integration is purely additive.

Two practical placement options:
1. **Shared path / artifact** — the UOA app writes `options_activity.json` into
   the tracker's `data/` dir (or a path you set via `OPTIONS_JSON`).
2. **openclaw posts, tracker enriches** — since openclaw already owns the Slack
   channel, the UOA app can hand its JSON to the tracker step (or vice-versa) and
   let one of them post the merged message.

## What the enrichment produces

Per alert, a **confluence verdict**:

| verdict | meaning |
|---------|---------|
| `CONFLUENT_BULLISH` / `CONFLUENT_BEARISH` | Flow and tracker agree on direction (strongest). |
| `FLOW_LEADS_BULLISH` / `FLOW_LEADS_BEARISH` | Flow has a view, tracker is neutral — watch for confirmation. |
| `CONFLICT` | Flow and tracker disagree — stand aside. |
| `NO_TRACKER_DATA` | Symbol not in the tracker universe — flow stands alone. |

Each verdict is combined with **regime agreement** (is the macro backdrop
risk-on/off in the flow's direction?) and the tracker's **HIGH/MEDIUM/LOW
confidence** to rank which alerts surface first, plus a one-line paper-trade note.

## Programmatic use

```python
import options_enrichment as oe

feed = oe.load_options_activity("options_activity.json")
copilot = json.load(open("copilot_signals.json"))
enriched = oe.enrich(feed, copilot)        # dict with ranked "enriched" list
slack_lines = oe.to_slack_lines(enriched)  # ready to append to a Slack post
```
