#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent))

from symbol_manager import SymbolManager


def emit_symbol_rows(symbols: list[str], manager: SymbolManager, output_format: str) -> None:
    if output_format == "json":
        rows = []
        for symbol in symbols:
            info = manager.get_symbol_info(symbol)
            if info:
                rows.append({
                    "symbol": info.symbol,
                    "name": info.name,
                    "category": info.category,
                    "asset_type": info.asset_type,
                    "sector": info.sector,
                    "api_mappings": info.api_mappings,
                })
        print(json.dumps(rows, indent=2))
        return

    if output_format == "csv":
        print("symbol,name,asset_type,category,sector")
        for symbol in symbols:
            info = manager.get_symbol_info(symbol)
            if info:
                print(f"{info.symbol},{info.name},{info.asset_type},{info.category},{info.sector or ''}")
        return

    for symbol in symbols:
        info = manager.get_symbol_info(symbol)
        if info:
            label = f"{info.symbol}: {info.name} [{info.asset_type}/{info.category}]"
            if info.sector:
                label += f" sector={info.sector}"
            print(f"  {label}")


def main() -> None:
    parser = argparse.ArgumentParser(description="Market Tracker Symbol Search")
    parser.add_argument("--search", "-s", help="Search for symbols by name, symbol, category, or sector")
    parser.add_argument("--category", "-c", help="List symbols by category")
    parser.add_argument("--sector", help="List symbols by sector")
    parser.add_argument("--list-categories", action="store_true", help="List all categories")
    parser.add_argument("--list-sectors", action="store_true", help="List all sectors")
    parser.add_argument("--stats", action="store_true", help="Show symbol statistics")
    parser.add_argument("--crypto", action="store_true", help="List all crypto symbols")
    parser.add_argument("--stocks", action="store_true", help="List all stock symbols")
    parser.add_argument("--indices", action="store_true", help="List all index/ETF symbols")
    parser.add_argument("--api-mapping", help="Show API mappings for a symbol")
    parser.add_argument("--export", help="Export all symbols to a JSON file")
    parser.add_argument("--format", choices=["table", "json", "csv"], default="table", help="Output format")
    args = parser.parse_args()

    manager = SymbolManager()

    if args.search:
        results = manager.search(args.search)
        if args.format == "json":
            print(json.dumps(results, indent=2))
        elif args.format == "csv":
            all_symbols = sorted({symbol for symbols in results.values() for symbol in symbols})
            emit_symbol_rows(all_symbols, manager, "csv")
        else:
            print(f"Search results for '{args.search}':")
            for field_name, symbols in results.items():
                if symbols:
                    print(f"\n{field_name.replace('_', ' ').title()}:")
                    emit_symbol_rows(symbols, manager, "table")
        return

    if args.category:
        symbols = manager.get_by_category(args.category)
        if args.format == "table":
            print(f"Symbols in category '{args.category}':")
        emit_symbol_rows(symbols, manager, args.format)
        return

    if args.sector:
        symbols = manager.get_by_sector(args.sector)
        if args.format == "table":
            print(f"Symbols in sector '{args.sector}':")
        emit_symbol_rows(symbols, manager, args.format)
        return

    if args.list_categories:
        categories = manager.get_categories()
        if args.format == "json":
            print(json.dumps(categories, indent=2))
        else:
            for category in categories:
                print(f"{category}: {len(manager.get_by_category(category))} symbols")
        return

    if args.list_sectors:
        sectors = manager.get_sectors()
        if args.format == "json":
            print(json.dumps(sectors, indent=2))
        else:
            for sector in sectors:
                print(f"{sector}: {len(manager.get_by_sector(sector))} symbols")
        return

    if args.stats:
        stats = manager.get_stats()
        if args.format == "json":
            print(json.dumps(stats, indent=2))
        else:
            for key, value in stats.items():
                print(f"{key.replace('_', ' ').title()}: {value}")
        return

    if args.crypto:
        emit_symbol_rows(manager.get_all_crypto(), manager, args.format)
        return

    if args.stocks:
        emit_symbol_rows(manager.get_all_stocks(), manager, args.format)
        return

    if args.indices:
        emit_symbol_rows(manager.get_all_indices(), manager, args.format)
        return

    if args.api_mapping:
        info = manager.get_symbol_info(args.api_mapping)
        if not info:
            raise SystemExit(f"Symbol '{args.api_mapping}' not found")
        if args.format == "json":
            print(json.dumps(info.api_mappings, indent=2))
        else:
            print(f"API mappings for {info.symbol} ({info.name}):")
            for api, mapping in info.api_mappings.items():
                if mapping:
                    print(f"  {api}: {mapping}")
        return

    if args.export:
        rows = []
        for symbol in manager.all_symbols():
            info = manager.get_symbol_info(symbol)
            if info:
                rows.append({
                    "symbol": info.symbol,
                    "name": info.name,
                    "category": info.category,
                    "asset_type": info.asset_type,
                    "sector": info.sector,
                    "api_mappings": info.api_mappings,
                })
        with open(args.export, "w", encoding="utf-8") as f:
            json.dump(rows, f, indent=2)
        print(f"Exported {len(rows)} symbols to {args.export}")
        return

    parser.print_help()
    print("\nExamples:")
    print("  python app/symbol_search.py --search bitcoin")
    print("  python app/symbol_search.py --category major")
    print("  python app/symbol_search.py --sector technology")
    print("  python app/symbol_search.py --stats")
    print("  python app/symbol_search.py --crypto --format csv")


if __name__ == "__main__":
    main()
