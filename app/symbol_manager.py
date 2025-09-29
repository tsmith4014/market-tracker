#!/usr/bin/env python3
"""
Symbol Management System for Market Tracker
Provides organized, searchable access to all available trading symbols
"""

import json
import os
from typing import Dict, List, Optional, Tuple
from dataclasses import dataclass

@dataclass
class SymbolInfo:
    symbol: str
    name: str
    category: str
    sector: Optional[str] = None
    api_mappings: Dict[str, str] = None

class SymbolManager:
    def __init__(self, symbols_file: str = "/app/symbols.json"):
        self.symbols_file = symbols_file
        self.symbols_data = self._load_symbols()
        self._build_indexes()
    
    def _load_symbols(self) -> dict:
        """Load symbols from JSON file"""
        try:
            with open(self.symbols_file, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            print(f"Warning: {self.symbols_file} not found, using empty symbols")
            return {"crypto": {}, "stocks": {}, "indices": []}
    
    def _build_indexes(self):
        """Build search indexes for fast lookups"""
        self._symbol_to_info = {}
        self._category_index = {}
        self._sector_index = {}
        self._name_index = {}
        
        # Index crypto symbols
        for category, symbols in self.symbols_data.get("crypto", {}).items():
            for symbol_data in symbols:
                symbol = symbol_data["symbol"]
                info = SymbolInfo(
                    symbol=symbol,
                    name=symbol_data["name"],
                    category=category,
                    api_mappings={
                        "kraken": symbol_data.get("kraken", ""),
                        "coinbase": symbol_data.get("coinbase", ""),
                        "coingecko": symbol_data.get("coingecko", "")
                    }
                )
                self._symbol_to_info[symbol] = info
                self._category_index.setdefault(category, []).append(symbol)
                self._name_index[symbol_data["name"].lower()] = symbol
        
        # Index stock symbols
        for category, symbols in self.symbols_data.get("stocks", {}).items():
            for symbol_data in symbols:
                symbol = symbol_data["symbol"]
                info = SymbolInfo(
                    symbol=symbol,
                    name=symbol_data["name"],
                    category=category,
                    sector=symbol_data.get("sector"),
                    api_mappings={
                        "stooq": symbol_data.get("stooq", ""),
                        "yfinance": symbol_data.get("yfinance", "")
                    }
                )
                self._symbol_to_info[symbol] = info
                self._category_index.setdefault(category, []).append(symbol)
                self._sector_index.setdefault(symbol_data.get("sector", "unknown"), []).append(symbol)
                self._name_index[symbol_data["name"].lower()] = symbol
        
        # Index indices
        for symbol_data in self.symbols_data.get("indices", []):
            symbol = symbol_data["symbol"]
            info = SymbolInfo(
                symbol=symbol,
                name=symbol_data["name"],
                category="indices",
                api_mappings={
                    "stooq": symbol_data.get("stooq", ""),
                    "yfinance": symbol_data.get("yfinance", "")
                }
            )
            self._symbol_to_info[symbol] = info
            self._category_index.setdefault("indices", []).append(symbol)
            self._name_index[symbol_data["name"].lower()] = symbol
    
    def get_symbol_info(self, symbol: str) -> Optional[SymbolInfo]:
        """Get detailed information about a symbol"""
        return self._symbol_to_info.get(symbol)
    
    def search_by_name(self, query: str) -> List[str]:
        """Search symbols by name (case-insensitive)"""
        query = query.lower()
        results = []
        for name, symbol in self._name_index.items():
            if query in name:
                results.append(symbol)
        return results
    
    def get_by_category(self, category: str) -> List[str]:
        """Get all symbols in a category"""
        return self._category_index.get(category, [])
    
    def get_by_sector(self, sector: str) -> List[str]:
        """Get all symbols in a sector (stocks only)"""
        return self._sector_index.get(sector, [])
    
    def get_all_crypto(self) -> List[str]:
        """Get all crypto symbols"""
        crypto_symbols = []
        for category in self._category_index:
            if category in ["major", "defi", "layer1", "meme"]:
                crypto_symbols.extend(self._category_index[category])
        return crypto_symbols
    
    def get_all_stocks(self) -> List[str]:
        """Get all stock symbols"""
        stock_symbols = []
        for category in self._category_index:
            if category in ["tech_mega_caps", "semiconductors", "finance", "healthcare", "energy"]:
                stock_symbols.extend(self._category_index[category])
        return stock_symbols
    
    def get_all_indices(self) -> List[str]:
        """Get all index/ETF symbols"""
        return self._category_index.get("indices", [])
    
    def get_api_mapping(self, symbol: str, api: str) -> Optional[str]:
        """Get the API-specific symbol for a given symbol and API"""
        info = self.get_symbol_info(symbol)
        if info and info.api_mappings:
            return info.api_mappings.get(api)
        return None
    
    def get_crypto_for_api(self, api: str) -> List[Tuple[str, str]]:
        """Get (symbol, api_symbol) pairs for crypto symbols for a specific API"""
        results = []
        for symbol in self.get_all_crypto():
            api_symbol = self.get_api_mapping(symbol, api)
            if api_symbol:
                results.append((symbol, api_symbol))
        return results
    
    def get_stocks_for_api(self, api: str) -> List[Tuple[str, str]]:
        """Get (symbol, api_symbol) pairs for stock symbols for a specific API"""
        results = []
        for symbol in self.get_all_stocks():
            api_symbol = self.get_api_mapping(symbol, api)
            if api_symbol:
                results.append((symbol, api_symbol))
        return results
    
    def get_categories(self) -> List[str]:
        """Get all available categories"""
        return list(self._category_index.keys())
    
    def get_sectors(self) -> List[str]:
        """Get all available sectors"""
        return list(self._sector_index.keys())
    
    def get_stats(self) -> Dict[str, int]:
        """Get statistics about available symbols"""
        return {
            "total_symbols": len(self._symbol_to_info),
            "crypto_symbols": len(self.get_all_crypto()),
            "stock_symbols": len(self.get_all_stocks()),
            "index_symbols": len(self.get_all_indices()),
            "categories": len(self.get_categories()),
            "sectors": len(self.get_sectors())
        }
    
    def search(self, query: str) -> Dict[str, List[str]]:
        """Comprehensive search across all fields"""
        query = query.lower()
        results = {
            "by_symbol": [],
            "by_name": [],
            "by_category": [],
            "by_sector": []
        }
        
        # Search by symbol
        for symbol in self._symbol_to_info.keys():
            if query in symbol.lower():
                results["by_symbol"].append(symbol)
        
        # Search by name
        results["by_name"] = self.search_by_name(query)
        
        # Search by category
        for category in self.get_categories():
            if query in category.lower():
                results["by_category"].extend(self.get_by_category(category))
        
        # Search by sector
        for sector in self.get_sectors():
            if query in sector.lower():
                results["by_sector"].extend(self.get_by_sector(sector))
        
        return results

def main():
    """CLI interface for symbol management"""
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
        results = sm.search(args.search)
        print(f"Search results for '{args.search}':")
        for field, symbols in results.items():
            if symbols:
                print(f"  {field}: {', '.join(symbols)}")
    
    elif args.category:
        symbols = sm.get_by_category(args.category)
        print(f"Symbols in category '{args.category}': {', '.join(symbols)}")
    
    elif args.sector:
        symbols = sm.get_by_sector(args.sector)
        print(f"Symbols in sector '{args.sector}': {', '.join(symbols)}")
    
    elif args.stats:
        stats = sm.get_stats()
        print("Symbol Statistics:")
        for key, value in stats.items():
            print(f"  {key}: {value}")
    
    elif args.list_categories:
        categories = sm.get_categories()
        print(f"Available categories: {', '.join(categories)}")
    
    elif args.list_sectors:
        sectors = sm.get_sectors()
        print(f"Available sectors: {', '.join(sectors)}")
    
    else:
        print("Use --help for available options")

if __name__ == "__main__":
    main()
