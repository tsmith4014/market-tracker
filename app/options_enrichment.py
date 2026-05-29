"""Cross-reference unusual options activity (UOA) with market-tracker signals.

This is the bridge between two systems that both feed a Slack channel:

  1. An external UOA scanner (the user's openclaw app) that flags unusual
     options flow (sweeps, large premium, call/put skew) per ticker.
  2. This market-tracker, which produces a directional signal, a calibrated
     confidence level, and a macro regime per ticker.

Flow alone is noisy; a trend signal alone doesn't beat buy-and-hold (we proved
that). But their *confluence* is genuinely informative context for PAPER
TRADING: "unusual call buying in a name the tracker also rates LONG/HIGH in a
risk-on regime" is a very different note than "unusual calls in a name the
tracker rates SHORT". This module computes that confluence and frames it for a
Slack post — as analysis/context, never as automated trade execution.

Input contract (what the UOA app emits) is documented in
docs/OPTIONS_INTEGRATION.md.
"""
from __future__ import annotations

import json
from pathlib import Path
from typing import Dict, List

# Confluence verdicts, strongest agreement first.
CONFLUENT_BULLISH = "CONFLUENT_BULLISH"
CONFLUENT_BEARISH = "CONFLUENT_BEARISH"
FLOW_LEADS_BULLISH = "FLOW_LEADS_BULLISH"   # options bullish, tracker neutral
FLOW_LEADS_BEARISH = "FLOW_LEADS_BEARISH"
CONFLICT = "CONFLICT"                       # options and tracker disagree
NO_TRACKER_DATA = "NO_TRACKER_DATA"

# Rank used to sort enriched alerts (higher = surface first).
_VERDICT_RANK = {
    CONFLUENT_BULLISH: 5,
    CONFLUENT_BEARISH: 5,
    FLOW_LEADS_BULLISH: 3,
    FLOW_LEADS_BEARISH: 3,
    CONFLICT: 2,
    NO_TRACKER_DATA: 1,
}


def load_options_activity(path: str | Path) -> dict:
    """Load and lightly normalize a UOA JSON file. Missing file -> empty feed."""
    p = Path(path)
    if not p.is_file() or p.stat().st_size == 0:
        return {"generated_at": None, "source": None, "alerts": []}
    data = json.loads(p.read_text(encoding="utf-8"))
    alerts = []
    for raw in data.get("alerts", []):
        sym = str(raw.get("symbol", "")).strip().upper()
        if not sym:
            continue
        alerts.append({
            "symbol": sym,
            "direction": _normalize_direction(raw),
            "premium_usd": _num(raw.get("premium_usd")),
            "contracts": _num(raw.get("contracts")),
            "sentiment_score": _num(raw.get("sentiment_score")),
            "strike": _num(raw.get("strike")),
            "expiry": raw.get("expiry"),
            "notes": raw.get("notes"),
        })
    return {"generated_at": data.get("generated_at"), "source": data.get("source"), "alerts": alerts}


def index_signals(copilot_payload: dict) -> Dict[str, dict]:
    """Map symbol -> the slim signal facts we need from a copilot payload."""
    out: Dict[str, dict] = {}
    for s in copilot_payload.get("signals", []):
        out[s["symbol"]] = {
            "signal": s.get("signal", "NEUTRAL"),
            "confidence": s.get("confidence", {}).get("level", "LOW"),
            "confidence_score": s.get("confidence", {}).get("score", 0.0),
            "composite_score": s.get("composite_score"),
            "rsi14": s.get("indicators", {}).get("rsi14"),
            "atr_pct": s.get("indicators", {}).get("atr_pct"),
            "close": s.get("price", {}).get("close"),
        }
    return out


def _confluence(flow_dir: str, tracker_signal: str | None) -> str:
    if tracker_signal is None:
        return NO_TRACKER_DATA
    if flow_dir == "bullish":
        if tracker_signal == "LONG":
            return CONFLUENT_BULLISH
        if tracker_signal == "SHORT":
            return CONFLICT
        return FLOW_LEADS_BULLISH
    if flow_dir == "bearish":
        if tracker_signal == "SHORT":
            return CONFLUENT_BEARISH
        if tracker_signal == "LONG":
            return CONFLICT
        return FLOW_LEADS_BEARISH
    return NO_TRACKER_DATA


def enrich(options_feed: dict, copilot_payload: dict) -> dict:
    """Join UOA alerts to tracker signals and produce confluence-ranked context."""
    sig_by_symbol = index_signals(copilot_payload)
    regime = copilot_payload.get("market_regime", {}).get("regime", "UNKNOWN")
    enriched: List[dict] = []
    for a in options_feed.get("alerts", []):
        tracker = sig_by_symbol.get(a["symbol"])
        tracker_signal = tracker["signal"] if tracker else None
        verdict = _confluence(a["direction"], tracker_signal)
        # Regime agreement: does the macro backdrop support the flow direction?
        regime_agrees = (
            (a["direction"] == "bullish" and regime == "RISK_ON")
            or (a["direction"] == "bearish" and regime == "RISK_OFF")
        )
        enriched.append({
            "symbol": a["symbol"],
            "flow_direction": a["direction"],
            "premium_usd": a["premium_usd"],
            "notes": a.get("notes"),
            "tracker_signal": tracker_signal,
            "tracker_confidence": tracker["confidence"] if tracker else None,
            "tracker_score": tracker["composite_score"] if tracker else None,
            "rsi14": tracker["rsi14"] if tracker else None,
            "confluence": verdict,
            "regime_agrees": regime_agrees,
            "paper_idea": _paper_idea(a, tracker, verdict, regime_agrees),
            "_rank": _VERDICT_RANK.get(verdict, 0)
            + (1 if regime_agrees else 0)
            + (1 if tracker and tracker["confidence"] == "HIGH" else 0),
        })
    enriched.sort(key=lambda e: (e["_rank"], e["premium_usd"] or 0), reverse=True)
    for e in enriched:
        e.pop("_rank", None)
    return {
        "generated_at": options_feed.get("generated_at"),
        "regime": regime,
        "alert_count": len(enriched),
        "enriched": enriched,
    }


def _paper_idea(alert: dict, tracker: dict | None, verdict: str, regime_agrees: bool) -> str:
    """A short, clearly-framed PAPER-TRADING note. Not financial advice."""
    sym = alert["symbol"]
    if verdict in (CONFLUENT_BULLISH, CONFLUENT_BEARISH):
        side = "bullish" if verdict == CONFLUENT_BULLISH else "bearish"
        strength = "strong" if (regime_agrees and tracker and tracker["confidence"] == "HIGH") else "moderate"
        return f"Paper: {strength} {side} confluence on {sym} (options flow + tracker agree). Educational only."
    if verdict in (FLOW_LEADS_BULLISH, FLOW_LEADS_BEARISH):
        return f"Paper: options flow {alert['direction']} on {sym} but tracker is neutral — watch for confirmation. Educational only."
    if verdict == CONFLICT:
        return f"Paper: CONFLICT on {sym} — options flow {alert['direction']} vs tracker {tracker['signal'] if tracker else 'n/a'}. Stand aside. Educational only."
    return f"Paper: {sym} not tracked by market-tracker; flow stands alone. Educational only."


def to_slack_lines(enriched_payload: dict, max_alerts: int = 6) -> List[str]:
    """Format the enriched confluence as Slack lines (appended to the daily post)."""
    items = enriched_payload.get("enriched", [])
    if not items:
        return []
    lines = ["", f"*Unusual Options × Tracker* ({enriched_payload.get('alert_count', 0)} alerts, regime {enriched_payload.get('regime', '?')})"]
    icons = {
        CONFLUENT_BULLISH: "✅📈", CONFLUENT_BEARISH: "✅📉",
        FLOW_LEADS_BULLISH: "👀📈", FLOW_LEADS_BEARISH: "👀📉",
        CONFLICT: "⚠️", NO_TRACKER_DATA: "❔",
    }
    for e in items[:max_alerts]:
        prem = f" ${e['premium_usd']/1e6:.1f}M" if e.get("premium_usd") else ""
        conf = f"/{e['tracker_confidence']}" if e.get("tracker_confidence") else ""
        tracker = e.get("tracker_signal") or "untracked"
        lines.append(
            f"{icons.get(e['confluence'], '•')} {e['symbol']}{prem}: "
            f"flow {e['flow_direction']} vs tracker {tracker}{conf} → {e['confluence']}"
        )
    lines.append("_Paper-trading context only — not financial advice._")
    return lines


def _normalize_direction(raw: dict) -> str:
    d = str(raw.get("direction", "")).strip().lower()
    if d in ("bullish", "bull", "long", "call", "calls"):
        return "bullish"
    if d in ("bearish", "bear", "short", "put", "puts"):
        return "bearish"
    # Fall back to option type if direction wasn't given.
    t = str(raw.get("type", "")).strip().lower()
    if t in ("call", "calls"):
        return "bullish"
    if t in ("put", "puts"):
        return "bearish"
    return "unknown"


def _num(x) -> float | None:
    try:
        return float(x)
    except (TypeError, ValueError):
        return None
