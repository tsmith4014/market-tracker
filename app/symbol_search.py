#!/usr/bin/env python3
"""
Symbol Search and Management CLI
Provides searchable, organized access to all available trading symbols
"""

import sys
import os
sys.path.append('/app')

from symbol_manager import SymbolManager
import argparse
import json

def main():
    parser = argparse.ArgumentParser(description="Market Tracker Symbol Search")
    parser.add_argument("--search", "-s", help="Search for symbols by name or symbol")
    parser.add_argument("--category", "-c", help="List symbols by category")
    parser.add_argument("--sector", help="List symbols by sector")
    parser.add_argument("--list-categories", action="store_true", help="List all categories")
    parser.add_argument("--list-sectors", action="store_true", help="List all sectors")
    parser.add_argument("--stats", action="store_true", help="Show symbol statistics")
    parser.add_argument("--crypto", action="store_true", help="List all crypto symbols")
    parser.add_argument("--stocks", action="store_true", help="List all stock symbols")
    parser.add_argument("--indices", action="store_true", help="List all index symbols")
    parser.add_argument("--api-mapping", help="Show API mappings for a symbol")
    parser.add_argument("--export", help="Export symbols to JSON file")
    parser.add_argument("--format", choices=["table", "json", "csv"], default="table", help="Output format")
    
    args = parser.parse_args()
    
    sm = SymbolManager()
    
    if args.search:
        results = sm.search(args.search)
        if args.format == "json":
            print(json.dumps(results, indent=2))
        elif args.format == "csv":
            all_symbols = set()
            for field, symbols in results.items():
                all_symbols.update(symbols)
            print("symbol,name,category,sector")
            for symbol in sorted(all_symbols):
                info = sm.get_symbol_info(symbol)
                if info:
                    print(f"{symbol},{info.name},{info.category},{info.sector or ''}")
        else:
            print(f"Search results for '{args.search}':")
            for field, symbols in results.items():
                if symbols:
                    print(f"\n{field.replace('_', ' ').title()}:")
                    for symbol in symbols:
                        info = sm.get_symbol_info(symbol)
                        if info:
                            print(f"  {symbol}: {info.name}")
    
    elif args.category:
        symbols = sm.get_by_category(args.category)
        if args.format == "json":
            print(json.dumps(symbols, indent=2))
        elif args.format == "csv":
            print("symbol,name,category,sector")
            for symbol in symbols:
                info = sm.get_symbol_info(symbol)
                if info:
                    print(f"{symbol},{info.name},{info.category},{info.sector or ''}")
        else:
            print(f"Symbols in category '{args.category}':")
            for symbol in symbols:
                info = sm.get_symbol_info(symbol)
                if info:
                    print(f"  {symbol}: {info.name}")
    
    elif args.sector:
        symbols = sm.get_by_sector(args.sector)
        if args.format == "json":
            print(json.dumps(symbols, indent=2))
        elif args.format == "csv":
            print("symbol,name,category,sector")
            for symbol in symbols:
                info = sm.get_symbol_info(symbol)
                if info:
                    print(f"{symbol},{info.name},{info.category},{info.sector or ''}")
        else:
            print(f"Symbols in sector '{args.sector}':")
            for symbol in symbols:
                info = sm.get_symbol_info(symbol)
                if info:
                    print(f"  {symbol}: {info.name}")
    
    elif args.list_categories:
        categories = sm.get_categories()
        if args.format == "json":
            print(json.dumps(categories, indent=2))
        else:
            print("Available categories:")
            for category in categories:
                count = len(sm.get_by_category(category))
                print(f"  {category}: {count} symbols")
    
    elif args.list_sectors:
        sectors = sm.get_sectors()
        if args.format == "json":
            print(json.dumps(sectors, indent=2))
        else:
            print("Available sectors:")
            for sector in sectors:
                count = len(sm.get_by_sector(sector))
                print(f"  {sector}: {count} symbols")
    
    elif args.stats:
        stats = sm.get_stats()
        if args.format == "json":
            print(json.dumps(stats, indent=2))
        else:
            print("Symbol Statistics:")
            for key, value in stats.items():
                print(f"  {key.replace('_', ' ').title()}: {value}")
    
    elif args.crypto:
        symbols = sm.get_all_crypto()
        if args.format == "json":
            print(json.dumps(symbols, indent=2))
        elif args.format == "csv":
            print("symbol,name,category,sector")
            for symbol in symbols:
                info = sm.get_symbol_info(symbol)
                if info:
                    print(f"{symbol},{info.name},{info.category},{info.sector or ''}")
        else:
            print("All Crypto Symbols:")
            for symbol in symbols:
                info = sm.get_symbol_info(symbol)
                if info:
                    print(f"  {symbol}: {info.name}")
    
    elif args.stocks:
        symbols = sm.get_all_stocks()
        if args.format == "json":
            print(json.dumps(symbols, indent=2))
        elif args.format == "csv":
            print("symbol,name,category,sector")
            for symbol in symbols:
                info = sm.get_symbol_info(symbol)
                if info:
                    print(f"{symbol},{info.name},{info.category},{info.sector or ''}")
        else:
            print("All Stock Symbols:")
            for symbol in symbols:
                info = sm.get_symbol_info(symbol)
                if info:
                    print(f"  {symbol}: {info.name}")
    
    elif args.indices:
        symbols = sm.get_all_indices()
        if args.format == "json":
            print(json.dumps(symbols, indent=2))
        elif args.format == "csv":
            print("symbol,name,category,sector")
            for symbol in symbols:
                info = sm.get_symbol_info(symbol)
                if info:
                    print(f"{symbol},{info.name},{info.category},{info.sector or ''}")
        else:
            print("All Index Symbols:")
            for symbol in symbols:
                info = sm.get_symbol_info(symbol)
                if info:
                    print(f"  {symbol}: {info.name}")
    
    elif args.api_mapping:
        info = sm.get_symbol_info(args.api_mapping)
        if info:
            if args.format == "json":
                print(json.dumps(info.api_mappings, indent=2))
            else:
                print(f"API Mappings for {args.api_mapping}:")
                for api, mapping in info.api_mappings.items():
                    if mapping:
                        print(f"  {api}: {mapping}")
        else:
            print(f"Symbol '{args.api_mapping}' not found")
    
    elif args.export:
        all_symbols = []
        for symbol in sm._symbol_to_info.keys():
            info = sm.get_symbol_info(symbol)
            if info:
                all_symbols.append({
                    "symbol": info.symbol,
                    "name": info.name,
                    "category": info.category,
                    "sector": info.sector,
                    "api_mappings": info.api_mappings
                })
        
        with open(args.export, 'w') as f:
            json.dump(all_symbols, f, indent=2)
        print(f"Exported {len(all_symbols)} symbols to {args.export}")
    
    else:
        print("Use --help for available options")
        print("\nQuick examples:")
        print("  python symbol_search.py --search bitcoin")
        print("  python symbol_search.py --category major")
        print("  python symbol_search.py --sector technology")
        print("  python symbol_search.py --stats")
        print("  python symbol_search.py --crypto --format csv")

if __name__ == "__main__":
    main()
