"""Tests for unusual-options-activity x market-tracker enrichment."""

from __future__ import annotations

import json
from pathlib import Path

import options_enrichment as oe


def _copilot(signals_spec):
    """Build a minimal copilot payload from (symbol, signal, conf_level, score) tuples."""
    return {
        "market_regime": {"regime": "RISK_ON"},
        "signals": [
            {
                "symbol": sym,
                "signal": sig,
                "confidence": {"level": lvl, "score": 0.7 if lvl == "HIGH" else 0.4},
                "composite_score": score,
                "indicators": {"rsi14": 55.0, "atr_pct": 2.0},
                "price": {"close": 100.0},
            }
            for sym, sig, lvl, score in signals_spec
        ],
    }


class TestLoadOptionsActivity:
    def test_missing_file_returns_empty(self, tmp_path):
        feed = oe.load_options_activity(tmp_path / "nope.json")
        assert feed["alerts"] == []

    def test_normalizes_symbols_and_direction(self, tmp_path):
        p = tmp_path / "uoa.json"
        p.write_text(json.dumps({
            "generated_at": "2026-05-29T00:00:00Z",
            "alerts": [
                {"symbol": "nvda", "type": "call", "premium_usd": 1_000_000},
                {"symbol": "TSLA", "direction": "put"},
            ],
        }))
        feed = oe.load_options_activity(p)
        assert feed["alerts"][0]["symbol"] == "NVDA"
        assert feed["alerts"][0]["direction"] == "bullish"  # inferred from type=call
        assert feed["alerts"][1]["direction"] == "bearish"

    def test_skips_rows_without_symbol(self, tmp_path):
        p = tmp_path / "uoa.json"
        p.write_text(json.dumps({"alerts": [{"direction": "bullish"}, {"symbol": "AMD", "direction": "bullish"}]}))
        feed = oe.load_options_activity(p)
        assert [a["symbol"] for a in feed["alerts"]] == ["AMD"]


class TestConfluence:
    def test_bullish_flow_long_tracker_is_confluent(self):
        feed = {"alerts": [{"symbol": "NVDA", "direction": "bullish", "premium_usd": 2e6, "notes": None}]}
        out = oe.enrich(feed, _copilot([("NVDA", "LONG", "HIGH", 60)]))
        e = out["enriched"][0]
        assert e["confluence"] == oe.CONFLUENT_BULLISH
        assert e["regime_agrees"] is True  # RISK_ON + bullish

    def test_bullish_flow_short_tracker_is_conflict(self):
        feed = {"alerts": [{"symbol": "BTC-USD", "direction": "bullish", "premium_usd": 1e6, "notes": None}]}
        out = oe.enrich(feed, _copilot([("BTC-USD", "SHORT", "MEDIUM", -45)]))
        assert out["enriched"][0]["confluence"] == oe.CONFLICT

    def test_flow_leads_when_tracker_neutral(self):
        feed = {"alerts": [{"symbol": "AMD", "direction": "bullish", "premium_usd": 5e5, "notes": None}]}
        out = oe.enrich(feed, _copilot([("AMD", "NEUTRAL", "LOW", 10)]))
        assert out["enriched"][0]["confluence"] == oe.FLOW_LEADS_BULLISH

    def test_untracked_symbol(self):
        feed = {"alerts": [{"symbol": "ZZZZ", "direction": "bearish", "premium_usd": 3e5, "notes": None}]}
        out = oe.enrich(feed, _copilot([("NVDA", "LONG", "HIGH", 60)]))
        assert out["enriched"][0]["confluence"] == oe.NO_TRACKER_DATA

    def test_confluent_high_conf_ranks_first(self):
        feed = {"alerts": [
            {"symbol": "ZZZZ", "direction": "bullish", "premium_usd": 9e6, "notes": None},
            {"symbol": "NVDA", "direction": "bullish", "premium_usd": 1e6, "notes": None},
        ]}
        out = oe.enrich(feed, _copilot([("NVDA", "LONG", "HIGH", 60)]))
        # NVDA (confluent + HIGH + regime) should outrank the untracked larger-premium flow.
        assert out["enriched"][0]["symbol"] == "NVDA"


class TestSlackLines:
    def test_empty_when_no_alerts(self):
        assert oe.to_slack_lines({"enriched": []}) == []

    def test_formats_alerts_with_disclaimer(self):
        feed = {"alerts": [{"symbol": "NVDA", "direction": "bullish", "premium_usd": 2e6, "notes": None}]}
        out = oe.enrich(feed, _copilot([("NVDA", "LONG", "HIGH", 60)]))
        lines = oe.to_slack_lines(out)
        assert any("NVDA" in ln for ln in lines)
        assert any("not financial advice" in ln.lower() for ln in lines)


class TestPaperFraming:
    def test_paper_idea_is_educational(self):
        feed = {"alerts": [{"symbol": "NVDA", "direction": "bullish", "premium_usd": 2e6, "notes": None}]}
        out = oe.enrich(feed, _copilot([("NVDA", "LONG", "HIGH", 60)]))
        assert "educational" in out["enriched"][0]["paper_idea"].lower()
