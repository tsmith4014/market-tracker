#!/usr/bin/env python3
"""Post a compact market-tracker summary to Slack via incoming webhook."""
from __future__ import annotations

import json
import os
import sys
import urllib.request
from pathlib import Path


def load_json(path: Path) -> dict:
    if not path.is_file():
        raise FileNotFoundError(path)
    return json.loads(path.read_text(encoding="utf-8"))


def build_message(copilot: dict, latest: dict) -> str:
    summary = copilot.get("summary", {})
    regime = copilot.get("market_regime", {})
    generated = copilot.get("generated_at") or latest.get("generated_at", "unknown")

    longs = [s for s in latest.get("signals", []) if s.get("signal") == "LONG"]
    shorts = [s for s in latest.get("signals", []) if s.get("signal") == "SHORT"]
    longs.sort(key=lambda x: x.get("score", 0), reverse=True)
    shorts.sort(key=lambda x: x.get("score", 0))

    top_long = ", ".join(f"{s['symbol']} ({s['score']:+.0f})" for s in longs[:5]) or "none"
    top_short = ", ".join(f"{s['symbol']} ({s['score']:+.0f})" for s in shorts[:5]) or "none"

    lines = [
        f"*Market Tracker* — {generated}",
        f"Regime: *{regime.get('regime', summary.get('regime', 'UNKNOWN'))}* "
        f"(risk {regime.get('risk_score', summary.get('regime_risk_score', 'n/a'))})",
        f"Signals: {summary.get('long_signals', len(longs))} LONG / "
        f"{summary.get('short_signals', len(shorts))} SHORT / "
        f"{summary.get('neutral_signals', '?')} NEUTRAL "
        f"({summary.get('total_symbols', len(latest.get('signals', [])))} symbols)",
        f"Top LONG: {top_long}",
        f"Top SHORT: {top_short}",
    ]
    hc_long = summary.get("high_confidence_longs") or []
    hc_short = summary.get("high_confidence_shorts") or []
    if hc_long or hc_short:
        lines.append(f"High confidence — LONG: {', '.join(hc_long) or 'none'} | SHORT: {', '.join(hc_short) or 'none'}")
    return "\n".join(lines)


def post_slack(webhook: str, text: str) -> None:
    payload = json.dumps({"text": text}).encode("utf-8")
    req = urllib.request.Request(
        webhook,
        data=payload,
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    with urllib.request.urlopen(req, timeout=30) as resp:
        if resp.status >= 400:
            raise RuntimeError(f"Slack webhook returned {resp.status}")


def main() -> int:
    webhook = os.getenv("SLACK_WEBHOOK_URL", "").strip()
    if not webhook:
        print("SLACK_WEBHOOK_URL not set; skipping Slack notification")
        return 0

    data_dir = Path(os.getenv("DATA_DIR", "data"))
    copilot_path = Path(os.getenv("COPILOT_JSON", data_dir / "copilot_signals.json"))
    latest_path = Path(os.getenv("LATEST_JSON", data_dir / "latest_signals.json"))

    try:
        copilot = load_json(copilot_path)
        latest = load_json(latest_path)
    except FileNotFoundError as exc:
        print(f"Missing output file: {exc}", file=sys.stderr)
        return 1

    text = build_message(copilot, latest)
    post_slack(webhook, text)
    print("Posted market summary to Slack")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
