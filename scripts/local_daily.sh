#!/usr/bin/env bash
# Local daily flow: OpenClaw heartbeat -> options_activity.json -> tracker -> Slack
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"

echo "==> OpenClaw heartbeat -> options_activity.json"
python3 scripts/openclaw_to_options_activity.py \
  --input "${OPENCLAW_HEARTBEAT:-$HOME/.openclaw/workspace/data/latest_heartbeat.json}" \
  --output data/options_activity.json

echo "==> Market tracker (docker)"
docker compose run --rm tracker

echo "==> Slack notify"
export DATA_DIR="${DATA_DIR:-$ROOT/data}"
export OPTIONS_JSON="${OPTIONS_JSON:-$DATA_DIR/options_activity.json}"
if [[ -z "${SLACK_WEBHOOK_URL:-}" ]] && [[ -f "$HOME/.openclaw/.env" ]]; then
  set -a
  # shellcheck disable=SC1091
  source "$HOME/.openclaw/.env"
  set +a
fi
if [[ -z "${SLACK_WEBHOOK_URL:-}" ]]; then
  echo "SLACK_WEBHOOK_URL not set — printing preview only:"
  PYTHONPATH=app python3 -c "
import json, sys
from pathlib import Path
sys.path.insert(0, 'scripts')
from slack_notify import build_message, build_options_lines
d = Path('data')
c = json.loads((d/'copilot_signals.json').read_text())
l = json.loads((d/'latest_signals.json').read_text())
t = build_message(c, l)
o = build_options_lines(c, d/'options_activity.json')
if o: t = t + '\n' + '\n'.join(o)
print(t)
"
  exit 0
fi
python3 scripts/slack_notify.py
echo "Done."
