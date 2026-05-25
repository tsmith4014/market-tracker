"""Tests for CSV storage idempotency and schema enforcement."""

from __future__ import annotations

from pathlib import Path

import pandas as pd
import pytest

from market_tracker import SCHEMA_COLUMNS, ensure_schema, select_rows_for_mode, write_rows


def make_row(symbol: str, date: str, close: float, score: float = 50.0, ts: str = "2025-01-01T00:00:00") -> dict:
    row = {col: None for col in SCHEMA_COLUMNS}
    row.update({
        "timestamp_ct": ts,
        "symbol": symbol,
        "data_source": "test",
        "date": date,
        "close": close,
        "composite_score": score,
        "signal": "NEUTRAL",
    })
    return row


class TestEnsureSchema:
    def test_creates_file_with_header_if_missing(self, tmp_path: Path):
        path = tmp_path / "out.csv"
        ensure_schema(str(path))
        assert path.exists()
        header = path.read_text(encoding="utf-8").splitlines()[0].split(",")
        assert header == SCHEMA_COLUMNS

    def test_idempotent_if_exists(self, tmp_path: Path):
        path = tmp_path / "out.csv"
        ensure_schema(str(path))
        content_before = path.read_text(encoding="utf-8")
        ensure_schema(str(path))
        assert path.read_text(encoding="utf-8") == content_before

    def test_creates_parent_dirs(self, tmp_path: Path):
        path = tmp_path / "nested" / "deep" / "out.csv"
        ensure_schema(str(path))
        assert path.exists()


class TestWriteRowsReplace:
    def test_replace_writes_fresh_csv(self, tmp_path: Path):
        path = tmp_path / "out.csv"
        rows = [make_row("BTC-USD", "2025-01-01", 100.0)]
        write_rows(str(path), rows, "replace")
        df = pd.read_csv(path)
        assert len(df) == 1
        assert df["symbol"].iloc[0] == "BTC-USD"

    def test_replace_overwrites_existing(self, tmp_path: Path):
        path = tmp_path / "out.csv"
        write_rows(str(path), [make_row("BTC-USD", "2025-01-01", 100.0)], "replace")
        write_rows(str(path), [make_row("ETH-USD", "2025-01-02", 200.0)], "replace")
        df = pd.read_csv(path)
        assert len(df) == 1
        assert df["symbol"].iloc[0] == "ETH-USD"


class TestWriteRowsAppend:
    def test_append_to_empty_file_works(self, tmp_path: Path):
        path = tmp_path / "out.csv"
        ensure_schema(str(path))  # header only, size > 0 but no data rows
        rows = [make_row("BTC-USD", "2025-01-01", 100.0)]
        write_rows(str(path), rows, "append")
        df = pd.read_csv(path)
        assert len(df) == 1

    def test_append_adds_new_rows(self, tmp_path: Path):
        path = tmp_path / "out.csv"
        write_rows(str(path), [make_row("BTC-USD", "2025-01-01", 100.0)], "replace")
        write_rows(str(path), [make_row("BTC-USD", "2025-01-02", 110.0)], "append")
        df = pd.read_csv(path)
        assert len(df) == 2
        assert sorted(df["date"].tolist()) == ["2025-01-01", "2025-01-02"]

    def test_append_dedupes_on_symbol_date_keep_last(self, tmp_path: Path):
        """Idempotency core test: same (symbol, date) replaces the older row."""
        path = tmp_path / "out.csv"
        old = make_row("BTC-USD", "2025-01-01", 100.0, score=50.0, ts="2025-01-01T00:00:00")
        write_rows(str(path), [old], "replace")
        new = make_row("BTC-USD", "2025-01-01", 105.0, score=60.0, ts="2025-01-01T12:00:00")
        write_rows(str(path), [new], "append")
        df = pd.read_csv(path)
        assert len(df) == 1, "duplicate (symbol, date) should be deduped"
        assert df["close"].iloc[0] == 105.0, "later row should win"
        assert df["composite_score"].iloc[0] == 60.0

    def test_append_idempotent_across_many_runs(self, tmp_path: Path):
        """Running the same write 5 times should leave the file unchanged."""
        path = tmp_path / "out.csv"
        rows = [
            make_row("BTC-USD", "2025-01-01", 100.0),
            make_row("ETH-USD", "2025-01-01", 200.0),
        ]
        write_rows(str(path), rows, "replace")
        baseline = pd.read_csv(path).sort_values(["symbol", "date"]).reset_index(drop=True)
        for _ in range(5):
            write_rows(str(path), rows, "append")
        final = pd.read_csv(path).sort_values(["symbol", "date"]).reset_index(drop=True)
        pd.testing.assert_frame_equal(baseline, final)

    def test_append_sorts_by_symbol_date(self, tmp_path: Path):
        path = tmp_path / "out.csv"
        write_rows(str(path), [
            make_row("ETH-USD", "2025-01-02", 200.0),
            make_row("BTC-USD", "2025-01-01", 100.0),
        ], "replace")
        write_rows(str(path), [
            make_row("BTC-USD", "2025-01-02", 110.0),
            make_row("ETH-USD", "2025-01-01", 190.0),
        ], "append")
        df = pd.read_csv(path)
        # After dedupe/sort: BTC 1, BTC 2, ETH 1, ETH 2
        assert df["symbol"].tolist() == ["BTC-USD", "BTC-USD", "ETH-USD", "ETH-USD"]
        assert df["date"].tolist() == ["2025-01-01", "2025-01-02", "2025-01-01", "2025-01-02"]

    def test_invalid_write_mode_raises(self, tmp_path: Path):
        path = tmp_path / "out.csv"
        with pytest.raises(ValueError, match="WRITE_MODE"):
            write_rows(str(path), [make_row("BTC-USD", "2025-01-01", 100.0)], "merge")


class TestSelectRowsForMode:
    def _df(self) -> pd.DataFrame:
        return pd.DataFrame({
            "date": pd.date_range("2025-01-01", periods=5),
            "composite_score": [None, None, 10.0, 20.0, 30.0],
            "signal": ["NEUTRAL"] * 5,
        })

    def test_historical_returns_all_scored_rows(self):
        result = select_rows_for_mode(self._df(), "historical")
        assert len(result) == 3
        assert result["composite_score"].tolist() == [10.0, 20.0, 30.0]

    def test_latest_returns_only_last_scored(self):
        result = select_rows_for_mode(self._df(), "latest")
        assert len(result) == 1
        assert result["composite_score"].iloc[0] == 30.0

    def test_invalid_mode_raises(self):
        with pytest.raises(ValueError, match="OUTPUT_MODE"):
            select_rows_for_mode(self._df(), "bogus")
