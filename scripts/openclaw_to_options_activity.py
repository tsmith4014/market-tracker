#!/usr/bin/env python3
"""Convert OpenClaw heartbeat JSON into market-tracker options_activity.json."""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

_TRIGGER_RE = re.compile(
    r"^([A-Z0-9.\-]+) unusual options activity",
    re.IGNORECASE,
)
_PREMIUM_RE = re.compile(r"premium notional \$?([\d.]+)\s*M", re.IGNORECASE)


def _direction_from_trigger(text: str) -> str:
    lower = text.lower()
    if "call-side" in lower or "call side" in lower:
        return "bullish"
    if "put-side" in lower or "put side" in lower:
        return "bearish"
    if "bias bullish" in lower:
        return "bullish"
    if "bias bearish" in lower:
        return "bearish"
    return "unknown"


def _premium_usd(text: str) -> float | None:
    m = _PREMIUM_RE.search(text)
    if not m:
        return None
    return float(m.group(1)) * 1_000_000


def heartbeat_to_options_activity(heartbeat: dict) -> dict:
    alerts: list[dict] = []
    for trigger in heartbeat.get("triggers") or []:
        if not isinstance(trigger, str):
            continue
        m = _TRIGGER_RE.match(trigger.strip())
        if not m:
            continue
        symbol = m.group(1).upper()
        alerts.append(
            {
                "symbol": symbol,
                "direction": _direction_from_trigger(trigger),
                "premium_usd": _premium_usd(trigger),
                "notes": trigger[:240],
            }
        )
    return {
        "generated_at": heartbeat.get("asOf"),
        "source": "openclaw-heartbeat",
        "alerts": alerts,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--input",
        type=Path,
        default=Path.home() / ".openclaw/workspace/data/latest_heartbeat.json",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("data/options_activity.json"),
    )
    args = parser.parse_args()
    heartbeat = json.loads(args.input.read_text(encoding="utf-8"))
    payload = heartbeat_to_options_activity(heartbeat)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote {len(payload['alerts'])} alerts to {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
