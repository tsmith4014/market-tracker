#!/usr/bin/env python3
from __future__ import annotations

from dataclasses import dataclass, field
import json
import os
from pathlib import Path
from typing import Dict, List, Tuple

DEFAULT_SYMBOLS_FILE = Path(__file__).resolve().with_name("symbols.json")


@dataclass(frozen=True)
class SymbolInfo:
    symbol: str
    name: str
    category: str
    asset_type: str
    sector: str | None = None
    api_mappings: Dict[str, str] = field(default_factory=dict)


class SymbolManager:
    def __init__(self, symbols_file: str | None = None):
        configured_path = symbols_file or os.getenv("SYMBOLS_PATH")
        self.symbols_file = Path(configured_path) if configured_path else DEFAULT_SYMBOLS_FILE
        self.symbols_data = self._load_symbols()
        self._build_indexes()

    def _load_symbols(self) -> dict:
        try:
            with self.symbols_file.open("r", encoding="utf-8") as f:
                return json.load(f)
        except FileNotFoundError:
            print(f"Warning: {self.symbols_file} not found, using empty symbol catalog")
            return {"crypto": {}, "stocks": {}, "indices": []}

    def _build_indexes(self) -> None:
        self._symbol_to_info: Dict[str, SymbolInfo] = {}
        self._category_index: Dict[str, List[str]] = {}
        self._sector_index: Dict[str, List[str]] = {}
        self._name_index: Dict[str, str] = {}
        self._asset_type_index: Dict[str, List[str]] = {"crypto": [], "stock": [], "index": []}

        for category, symbols in self.symbols_data.get("crypto", {}).items():
            for row in symbols:
                self._add_symbol(SymbolInfo(
                    symbol=row["symbol"],
                    name=row["name"],
                    category=category,
                    asset_type="crypto",
                    api_mappings={
                        "kraken": row.get("kraken", ""),
                        "coinbase": row.get("coinbase", ""),
                        "coingecko": row.get("coingecko", ""),
                    },
                ))

        for category, symbols in self.symbols_data.get("stocks", {}).items():
            for row in symbols:
                sector = row.get("sector")
                info = SymbolInfo(
                    symbol=row["symbol"],
                    name=row["name"],
                    category=category,
                    asset_type="stock",
                    sector=sector,
                    api_mappings={
                        "stooq": row.get("stooq", ""),
                        "yfinance": row.get("yfinance", ""),
                    },
                )
                self._add_symbol(info)
                self._sector_index.setdefault(sector or "unknown", []).append(info.symbol)

        for row in self.symbols_data.get("indices", []):
            self._add_symbol(SymbolInfo(
                symbol=row["symbol"],
                name=row["name"],
                category="indices",
                asset_type="index",
                api_mappings={
                    "stooq": row.get("stooq", ""),
                    "yfinance": row.get("yfinance", ""),
                },
            ))

    def _add_symbol(self, info: SymbolInfo) -> None:
        self._symbol_to_info[info.symbol] = info
        self._category_index.setdefault(info.category, []).append(info.symbol)
        self._asset_type_index.setdefault(info.asset_type, []).append(info.symbol)
        self._name_index[info.name.lower()] = info.symbol

    def get_symbol_info(self, symbol: str) -> SymbolInfo | None:
        return self._symbol_to_info.get(symbol)

    def get_asset_type(self, symbol: str) -> str | None:
        info = self.get_symbol_info(symbol)
        return info.asset_type if info else None

    def all_symbols(self) -> List[str]:
        return sorted(self._symbol_to_info.keys())

    def search_by_name(self, query: str) -> List[str]:
        query = query.lower()
        return sorted({symbol for name, symbol in self._name_index.items() if query in name})

    def get_by_category(self, category: str) -> List[str]:
        return list(self._category_index.get(category, []))

    def get_by_sector(self, sector: str) -> List[str]:
        return list(self._sector_index.get(sector, []))

    def get_all_crypto(self) -> List[str]:
        return list(self._asset_type_index.get("crypto", []))

    def get_all_stocks(self) -> List[str]:
        return list(self._asset_type_index.get("stock", []))

    def get_all_indices(self) -> List[str]:
        return list(self._asset_type_index.get("index", []))

    def get_api_mapping(self, symbol: str, api: str) -> str | None:
        info = self.get_symbol_info(symbol)
        if not info:
            return None
        mapping = info.api_mappings.get(api)
        return mapping or None

    def get_crypto_for_api(self, api: str) -> List[Tuple[str, str]]:
        return [(symbol, mapping) for symbol in self.get_all_crypto() if (mapping := self.get_api_mapping(symbol, api))]

    def get_stocks_for_api(self, api: str) -> List[Tuple[str, str]]:
        return [(symbol, mapping) for symbol in self.get_all_stocks() if (mapping := self.get_api_mapping(symbol, api))]

    def get_categories(self) -> List[str]:
        return sorted(self._category_index.keys())

    def get_sectors(self) -> List[str]:
        return sorted(self._sector_index.keys())

    def get_stats(self) -> Dict[str, int]:
        return {
            "total_symbols": len(self._symbol_to_info),
            "crypto_symbols": len(self.get_all_crypto()),
            "stock_symbols": len(self.get_all_stocks()),
            "index_symbols": len(self.get_all_indices()),
            "categories": len(self.get_categories()),
            "sectors": len(self.get_sectors()),
        }

    def search(self, query: str) -> Dict[str, List[str]]:
        query = query.lower()
        results: Dict[str, List[str]] = {
            "by_symbol": [],
            "by_name": [],
            "by_category": [],
            "by_sector": [],
        }
        for symbol in self._symbol_to_info:
            if query in symbol.lower():
                results["by_symbol"].append(symbol)
        results["by_name"] = self.search_by_name(query)
        for category in self.get_categories():
            if query in category.lower():
                results["by_category"].extend(self.get_by_category(category))
        for sector in self.get_sectors():
            if query in sector.lower():
                results["by_sector"].extend(self.get_by_sector(sector))
        return {key: sorted(set(value)) for key, value in results.items()}


def main() -> None:
    import argparse

    parser = argparse.ArgumentParser(description="Market Tracker Symbol Manager")
    parser.add_argument("--search", "-s", help="Search for symbols")
    parser.add_argument("--category", "-c", help="Get symbols by category")
    parser.add_argument("--sector", help="Get symbols by sector")
    parser.add_argument("--stats", action="store_true", help="Show statistics")
    parser.add_argument("--list-categories", action="store_true", help="List all categories")
    parser.add_argument("--list-sectors", action="store_true", help="List all sectors")
    args = parser.parse_args()

    sm = SymbolManager()
    if args.search:
        print(f"Search results for '{args.search}':")
        for field_name, symbols in sm.search(args.search).items():
            if symbols:
                print(f"  {field_name}: {', '.join(symbols)}")
    elif args.category:
        print(f"Symbols in category '{args.category}': {', '.join(sm.get_by_category(args.category))}")
    elif args.sector:
        print(f"Symbols in sector '{args.sector}': {', '.join(sm.get_by_sector(args.sector))}")
    elif args.stats:
        for key, value in sm.get_stats().items():
            print(f"{key}: {value}")
    elif args.list_categories:
        print(f"Available categories: {', '.join(sm.get_categories())}")
    elif args.list_sectors:
        print(f"Available sectors: {', '.join(sm.get_sectors())}")
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
