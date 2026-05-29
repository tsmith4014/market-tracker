"""Tests for auto-including unusual-options symbols in the tracked universe."""

from __future__ import annotations

import json

import market_tracker as mt
from symbol_manager import SymbolManager


class TestAddStockSymbol:
    def test_registers_with_derived_mappings(self, tmp_symbols_file):
        sm = SymbolManager(str(tmp_symbols_file))
        assert sm.get_symbol_info("FSLR") is None

        added = sm.add_stock_symbol("fslr")
        assert added is True

        info = sm.get_symbol_info("FSLR")
        assert info is not None
        assert info.asset_type == "stock"
        assert sm.get_api_mapping("FSLR", "stooq") == "fslr.us"
        assert sm.get_api_mapping("FSLR", "yfinance") == "FSLR"

    def test_existing_symbol_not_overwritten(self, tmp_symbols_file):
        sm = SymbolManager(str(tmp_symbols_file))
        assert sm.add_stock_symbol("AAPL") is False
        assert sm.get_api_mapping("AAPL", "stooq") == "aapl.us"


class TestOptionsActivityUniverse:
    def test_unknown_equities_added_crypto_skipped(self, tmp_symbols_file, tmp_path, monkeypatch):
        feed = tmp_path / "options_activity.json"
        feed.write_text(json.dumps({
            "alerts": [
                {"symbol": "FSLR", "direction": "bullish"},
                {"symbol": "AAPL", "direction": "bullish"},
                {"symbol": "BTC-USD", "direction": "bearish"},
            ]
        }))

        monkeypatch.setattr(mt, "SYMBOL_MANAGER", SymbolManager(str(tmp_symbols_file)))
        monkeypatch.setattr(mt, "OPTIONS_ACTIVITY_PATH", str(feed))
        monkeypatch.setattr(mt, "TRACK_OPTIONS_SYMBOLS", True)
        monkeypatch.setattr(mt, "TRACK_SYMBOLS", [])
        monkeypatch.setattr(mt, "TRACK_ALL", False)
        monkeypatch.setattr(mt, "TRACK_CRYPTO", [])
        monkeypatch.setattr(mt, "TRACK_STOCKS", ["tech_mega_caps"])
        monkeypatch.setattr(mt, "TRACK_INDICES", False)

        symbols = mt.get_tracking_symbols()

        assert "FSLR" in symbols                      # unknown equity auto-added
        assert symbols.count("AAPL") == 1             # known + flagged, deduped
        assert "BTC-USD" not in symbols               # crypto-style skipped
        assert mt.SYMBOL_MANAGER.get_asset_type("FSLR") == "stock"

    def test_disabled_flag_excludes_options_symbols(self, tmp_symbols_file, tmp_path, monkeypatch):
        feed = tmp_path / "options_activity.json"
        feed.write_text(json.dumps({"alerts": [{"symbol": "FSLR", "direction": "bullish"}]}))

        monkeypatch.setattr(mt, "SYMBOL_MANAGER", SymbolManager(str(tmp_symbols_file)))
        monkeypatch.setattr(mt, "OPTIONS_ACTIVITY_PATH", str(feed))
        monkeypatch.setattr(mt, "TRACK_OPTIONS_SYMBOLS", False)
        monkeypatch.setattr(mt, "TRACK_SYMBOLS", [])
        monkeypatch.setattr(mt, "TRACK_ALL", False)
        monkeypatch.setattr(mt, "TRACK_CRYPTO", [])
        monkeypatch.setattr(mt, "TRACK_STOCKS", ["tech_mega_caps"])
        monkeypatch.setattr(mt, "TRACK_INDICES", False)

        symbols = mt.get_tracking_symbols()
        assert "FSLR" not in symbols
