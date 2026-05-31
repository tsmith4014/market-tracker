# Symbol Management System

## Overview

The Market Tracker now includes a comprehensive, searchable symbol management system that supports **56+ symbols** across crypto, stocks, and indices. All data sources are **free** and require **no API keys**.

## Available Symbols

### 📊 Statistics

- **Total Symbols**: 56
- **Crypto Symbols**: 23 (across 4 categories)
- **Stock Symbols**: 28 (across 5 sectors)
- **Index Symbols**: 5 (major ETFs)
- **Categories**: 10
- **Sectors**: 5

### 🔗 Crypto Categories

#### Major Cryptocurrencies (10)

- **BTC-USD**: Bitcoin
- **ETH-USD**: Ethereum
- **SOL-USD**: Solana
- **XRP-USD**: XRP
- **ADA-USD**: Cardano
- **MATIC-USD**: Polygon
- **LINK-USD**: Chainlink
- **UNI-USD**: Uniswap
- **AAVE-USD**: Aave
- **AVAX-USD**: Avalanche

#### DeFi Tokens (5)

- **SUSHI-USD**: SushiSwap
- **CRV-USD**: Curve
- **COMP-USD**: Compound
- **MKR-USD**: Maker
- **YFI-USD**: Yearn Finance

#### Layer 1 Blockchains (5)

- **DOT-USD**: Polkadot
- **ATOM-USD**: Cosmos
- **NEAR-USD**: NEAR Protocol
- **FTM-USD**: Fantom
- **ALGO-USD**: Algorand

#### Meme Coins (3)

- **DOGE-USD**: Dogecoin
- **SHIB-USD**: Shiba Inu
- **PEPE-USD**: Pepe

### 📈 Stock Sectors

#### Technology Mega Caps (8)

- **AAPL**: Apple Inc.
- **MSFT**: Microsoft Corp.
- **GOOGL**: Alphabet Inc.
- **AMZN**: Amazon.com Inc.
- **TSLA**: Tesla Inc.
- **NVDA**: NVIDIA Corp.
- **META**: Meta Platforms Inc.
- **NFLX**: Netflix Inc.

#### Semiconductors (5)

- **AMD**: Advanced Micro Devices
- **INTC**: Intel Corp.
- **QCOM**: Qualcomm Inc.
- **TXN**: Texas Instruments
- **AVGO**: Broadcom Inc.

#### Financial Services (5)

- **JPM**: JPMorgan Chase
- **BAC**: Bank of America
- **WFC**: Wells Fargo
- **GS**: Goldman Sachs
- **MS**: Morgan Stanley

#### Healthcare (5)

- **JNJ**: Johnson & Johnson
- **PFE**: Pfizer Inc.
- **UNH**: UnitedHealth Group
- **ABBV**: AbbVie Inc.
- **MRK**: Merck & Co.

#### Energy (5)

- **XOM**: Exxon Mobil
- **CVX**: Chevron Corp.
- **COP**: ConocoPhillips
- **EOG**: EOG Resources
- **SLB**: Schlumberger

### 📊 Indices/ETFs (5)

- **SPY**: SPDR S&P 500 ETF
- **QQQ**: Invesco QQQ Trust
- **IWM**: iShares Russell 2000 ETF
- **VTI**: Vanguard Total Stock Market ETF
- **DIA**: SPDR Dow Jones Industrial Average ETF

## Search & Management

### Command Line Interface

```bash
# Show symbol statistics
make symbols

# Search for symbols
make search ARGS="--search bitcoin"
make search ARGS="--search apple"
make search ARGS="--search tech"

# List by category
make search ARGS="--category major"
make search ARGS="--category tech_mega_caps"

# List by sector
make search ARGS="--sector technology"
make search ARGS="--sector financial"

# Export to CSV
make search ARGS="--crypto --format csv > crypto_symbols.csv"

# Show all categories
make search ARGS="--list-categories"

# Show all sectors
make search ARGS="--list-sectors"
```

### Python API

```python
from symbol_manager import SymbolManager

sm = SymbolManager()

# Search symbols
results = sm.search("bitcoin")
print(results)

# Get by category
crypto = sm.get_by_category("major")
stocks = sm.get_by_category("tech_mega_caps")

# Get by sector
tech_stocks = sm.get_by_sector("technology")

# Get API mappings
btc_kraken = sm.get_api_mapping("BTC-USD", "kraken")
aapl_stooq = sm.get_api_mapping("AAPL", "stooq")

# Get statistics
stats = sm.get_stats()
print(f"Total symbols: {stats['total_symbols']}")
```

## Configuration

### Environment Variables

Control which symbols to track via environment variables:

```bash
# Track specific crypto categories (default: major,defi)
export TRACK_CRYPTO="major,defi,layer1,meme"

# Track specific stock categories (default: tech_mega_caps,semiconductors)
export TRACK_STOCKS="tech_mega_caps,semiconductors,finance,healthcare,energy"

# Track indices (default: true)
export TRACK_INDICES="true"
```

### Docker Compose

```yaml
services:
  tracker:
    environment:
      - TRACK_CRYPTO=major,defi,layer1
      - TRACK_STOCKS=tech_mega_caps,semiconductors
      - TRACK_INDICES=true
```

## Data Sources

### Crypto APIs (No Key Required)

1. **Kraken API** (Primary) - 565+ USD/USDT pairs
2. **Coinbase API** (Secondary) - 509+ USD/USDT pairs
3. **CoinGecko API** (Tertiary) - 18,890+ coins

### Stock APIs (No Key Required)

1. **Stooq API** (Primary) - Thousands of stocks
2. **Yahoo Finance** (Fallback) - Via yfinance library

### Fallback Chain

- **Crypto**: Kraken → Coinbase → CoinGecko
- **Stocks**: Stooq → Yahoo Finance
- **Indices**: Stooq → Yahoo Finance

## Auto-tracking Unusual-Options Symbols

The daily pipeline reads `data/options_activity.json` (produced from the OpenClaw
heartbeat). Any equity flagged there that is **not** already in `symbols.json` is
registered at run time with derived mappings (`stooq: <sym>.us`, `yfinance: <sym>`)
and scored alongside the catalog, so those names get a real confluence verdict
instead of `NO_TRACKER_DATA`.

- Controlled by `TRACK_OPTIONS_SYMBOLS` (default `true`; set `false` to disable).
- Feed path is `OPTIONS_ACTIVITY_PATH` (default `data/options_activity.json`; `/data/options_activity.json` in Docker).
- Crypto-style tickers (`*-USD`) in the feed are skipped — the options feed is equities/ETFs.

This adds a few symbols to each run, so runs take slightly longer but the
Unusual Options × Tracker section becomes fully populated.

## Adding New Symbols

### 1. Edit `symbols.json`

```json
{
  "crypto": {
    "new_category": [
      {
        "symbol": "NEW-USD",
        "name": "New Token",
        "kraken": "NEWUSD",
        "coinbase": "NEW-USD",
        "coingecko": "new-token",
        "category": "new_category"
      }
    ]
  }
}
```

### 2. Rebuild Docker Image

```bash
make build
```

### 3. Test New Symbol

```bash
make search ARGS="--search new"
```

## API Mappings

Each symbol includes mappings for different APIs:

```json
{
  "symbol": "BTC-USD",
  "name": "Bitcoin",
  "kraken": "XBTUSD",
  "coinbase": "BTC-USD",
  "coingecko": "bitcoin"
}
```

## Performance

- **Search**: O(1) lookup by symbol
- **Category Filter**: O(1) category lookup
- **Sector Filter**: O(1) sector lookup
- **Name Search**: O(n) linear search (optimized for small datasets)

## File Structure

```
app/
├── symbols.json          # Symbol definitions
├── symbol_manager.py     # Core management logic
├── symbol_search.py      # CLI search interface
├── market_tracker.py     # Main tracking application
└── config.json          # Trading parameters
```

## Examples

### Find All Tech Stocks

```bash
make search ARGS="--sector technology"
```

### Export All Crypto to CSV

```bash
make search ARGS="--crypto --format csv" > crypto_export.csv
```

### Search for Specific Company

```bash
make search ARGS="--search microsoft"
```

### Get API Mappings

```bash
make search ARGS="--api-mapping BTC-USD"
```

This system provides a robust, searchable, and organized way to manage all available trading symbols with real-time data from free APIs.
