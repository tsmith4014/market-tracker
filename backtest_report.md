# Market Tracker Backtest Report

_Generated: 2026-10-08T06:09:37+00:00_

## Data Sources

- Crypto: Kraken -> Coinbase -> CoinGecko OHLC -> CoinPaprika fallback chain.
- Stocks / ETFs / indices: Stooq -> Yahoo Finance fallback chain.
- Data rows are generated from real market APIs. Mock OHLCV rows are not generated.

## Data Freshness

- Rows: **92,728**
- Symbols: **161**
- Date range: **2024-05-15** to **2026-10-08**

## Latest Signals

| symbol     | date                |         close |   composite_score | signal   | data_source   |
|:-----------|:--------------------|--------------:|------------------:|:---------|:--------------|
| AAVE-USD   | 2026-10-08 00:00:00 |   173.09      |         65.8333   | LONG     | Kraken API    |
| ABBV       | 2026-10-07 00:00:00 |   271.36      |         63.9167   | LONG     | Yahoo Finance |
| ADA-USD    | 2026-10-08 00:00:00 |     0.253202  |         48.3333   | LONG     | Kraken API    |
| AMAT       | 2026-10-07 00:00:00 |   520.65      |         72.8333   | LONG     | Yahoo Finance |
| AMD        | 2026-10-07 00:00:00 |   645.86      |         71.5833   | LONG     | Yahoo Finance |
| AMGN       | 2026-10-07 00:00:00 |   413.08      |         74.5833   | LONG     | Yahoo Finance |
| AVAX-USD   | 2026-10-08 00:00:00 |    10.893     |         50        | LONG     | Kraken API    |
| BITO       | 2026-10-07 00:00:00 |    11.14      |         38.5833   | LONG     | Yahoo Finance |
| BLK        | 2026-10-07 00:00:00 |  1069.63      |         33        | LONG     | Yahoo Finance |
| COMP-USD   | 2026-10-08 00:00:00 |    23.63      |         40.1667   | LONG     | Kraken API    |
| CRV-USD    | 2026-10-08 00:00:00 |     0.38517   |         57.0833   | LONG     | Kraken API    |
| CSCO       | 2026-10-07 00:00:00 |   117.39      |         74.0833   | LONG     | Yahoo Finance |
| DXY-INDEX  | 2026-10-08 00:00:00 |   102.308     |         80.914    | LONG     | Yahoo Finance |
| FET-USD    | 2026-10-08 00:00:00 |     0.2321    |         30.1667   | LONG     | Kraken API    |
| FIL-USD    | 2026-10-08 00:00:00 |     1.055     |         38.8333   | LONG     | Kraken API    |
| GOOGL      | 2026-10-07 00:00:00 |   350.5       |         55.3333   | LONG     | Yahoo Finance |
| GRT-USD    | 2026-10-08 00:00:00 |     0.02723   |         42.5833   | LONG     | Kraken API    |
| IBIT       | 2026-10-07 00:00:00 |    47.21      |         61.0833   | LONG     | Yahoo Finance |
| ICP-USD    | 2026-10-08 00:00:00 |     3.19      |         44.8333   | LONG     | Kraken API    |
| INTC       | 2026-10-07 00:00:00 |   113.12      |         44.5833   | LONG     | Yahoo Finance |
| LIN        | 2026-10-07 00:00:00 |   483.98      |         38        | LONG     | Yahoo Finance |
| LLY        | 2026-10-07 00:00:00 |  1188.72      |         66.25     | LONG     | Yahoo Finance |
| LRCX       | 2026-10-07 00:00:00 |   329.51      |         59.8333   | LONG     | Yahoo Finance |
| META       | 2026-10-07 00:00:00 |   721.31      |         51.5833   | LONG     | Yahoo Finance |
| MSFT       | 2026-10-07 00:00:00 |   529.76      |         68.75     | LONG     | Yahoo Finance |
| MU         | 2026-10-07 00:00:00 |  1088         |         56.5833   | LONG     | Yahoo Finance |
| NEAR-USD   | 2026-10-08 00:00:00 |     5.4047    |         44.3333   | LONG     | Kraken API    |
| NVDA       | 2026-10-07 00:00:00 |   237.47      |         72.75     | LONG     | Yahoo Finance |
| QQQ        | 2026-10-07 00:00:00 |   757.73      |         74.75     | LONG     | Yahoo Finance |
| RENDER-USD | 2026-10-08 00:00:00 |     2.016     |         46.3333   | LONG     | Kraken API    |
| SMH        | 2026-10-07 00:00:00 |   625.03      |         71.0833   | LONG     | Yahoo Finance |
| SOXX       | 2026-10-07 00:00:00 |   582.82      |         71.0833   | LONG     | Yahoo Finance |
| TIA-USD    | 2026-10-08 00:00:00 |     0.4716    |         30.1667   | LONG     | Kraken API    |
| TMO        | 2026-10-07 00:00:00 |   662.06      |         43.0833   | LONG     | Yahoo Finance |
| TXN        | 2026-10-07 00:00:00 |   288.98      |         71.0833   | LONG     | Yahoo Finance |
| XLE        | 2026-10-07 00:00:00 |    63.36      |         32.5833   | LONG     | Yahoo Finance |
| XLK        | 2026-10-07 00:00:00 |   201.39      |         74.75     | LONG     | Yahoo Finance |
| AAPL       | 2026-10-07 00:00:00 |   336.67      |         40.6667   | NEUTRAL  | Yahoo Finance |
| ALGO-USD   | 2026-10-08 00:00:00 |     0.11762   |         24.5833   | NEUTRAL  | Kraken API    |
| AMZN       | 2026-10-07 00:00:00 |   259.92      |         56.6667   | NEUTRAL  | Yahoo Finance |
| APT-USD    | 2026-10-08 00:00:00 |     0.7689    |        -14.3333   | NEUTRAL  | Kraken API    |
| ARB-USD    | 2026-10-08 00:00:00 |     0.1824    |         10.4167   | NEUTRAL  | Kraken API    |
| ARKK       | 2026-10-07 00:00:00 |    88.3       |         31.1667   | NEUTRAL  | Yahoo Finance |
| ATOM-USD   | 2026-10-08 00:00:00 |     1.7241    |        -25.5833   | NEUTRAL  | Kraken API    |
| AVGO       | 2026-10-07 00:00:00 |   376.51      |         41.9167   | NEUTRAL  | Yahoo Finance |
| BCH-USD    | 2026-10-08 00:00:00 |   295.94      |        -17.6667   | NEUTRAL  | Kraken API    |
| BONK-USD   | 2026-10-08 00:00:00 |     3.414e-06 |        -16.5833   | NEUTRAL  | Kraken API    |
| BTC-USD    | 2026-10-08 00:00:00 | 82825.4       |         13.1667   | NEUTRAL  | Kraken API    |
| CAT        | 2026-10-07 00:00:00 |   813.83      |         12.25     | NEUTRAL  | Yahoo Finance |
| CL         | 2026-10-07 00:00:00 |    87.21      |          1.75     | NEUTRAL  | Yahoo Finance |
| COP        | 2026-10-07 00:00:00 |   129.84      |         22.4167   | NEUTRAL  | Yahoo Finance |
| COST       | 2026-10-07 00:00:00 |   942.25      |         28.25     | NEUTRAL  | Yahoo Finance |
| CRM        | 2026-10-07 00:00:00 |   224.56      |          0.666667 | NEUTRAL  | Yahoo Finance |
| CVX        | 2026-10-07 00:00:00 |   205.15      |        -18.6667   | NEUTRAL  | Yahoo Finance |
| DASH-USD   | 2026-10-08 00:00:00 |    53.497     |        -16.5833   | NEUTRAL  | Kraken API    |
| DBC        | 2026-10-07 00:00:00 |    32.51      |         28.8333   | NEUTRAL  | Yahoo Finance |
| DE         | 2026-10-07 00:00:00 |   656.87      |        -13.3333   | NEUTRAL  | Yahoo Finance |
| DIA        | 2026-10-07 00:00:00 |   511.02      |         13.5833   | NEUTRAL  | Yahoo Finance |
| DIS        | 2026-10-07 00:00:00 |   104.75      |         17        | NEUTRAL  | Yahoo Finance |
| DOT-USD    | 2026-10-08 00:00:00 |     1.0991    |        -29.5833   | NEUTRAL  | Kraken API    |
| EEM        | 2026-10-07 00:00:00 |    67.37      |         12.8333   | NEUTRAL  | Yahoo Finance |
| EOG        | 2026-10-07 00:00:00 |   144.21      |         35.5      | NEUTRAL  | Yahoo Finance |
| ETC-USD    | 2026-10-08 00:00:00 |     8.372     |        -11.9167   | NEUTRAL  | Kraken API    |
| ETH-USD    | 2026-10-08 00:00:00 |  2567.96      |          9.83333  | NEUTRAL  | Kraken API    |
| EWJ        | 2026-10-07 00:00:00 |    98.32      |         59.3333   | NEUTRAL  | Yahoo Finance |
| FCX        | 2026-10-07 00:00:00 |    71.86      |         27.8333   | NEUTRAL  | Yahoo Finance |
| FXI        | 2026-10-07 00:00:00 |    33.42      |        -62.5      | NEUTRAL  | Yahoo Finance |
| GE         | 2026-10-07 00:00:00 |   303.62      |        -60        | NEUTRAL  | Yahoo Finance |
| HBAR-USD   | 2026-10-08 00:00:00 |     0.09256   |         17.9167   | NEUTRAL  | Kraken API    |
| HON        | 2026-10-07 00:00:00 |   208.11      |        -19.25     | NEUTRAL  | Yahoo Finance |
| IBM        | 2026-10-07 00:00:00 |   220.51      |        -67.8333   | NEUTRAL  | Yahoo Finance |
| IEMG       | 2026-10-07 00:00:00 |    82.04      |         22.6667   | NEUTRAL  | Yahoo Finance |
| INJ-USD    | 2026-10-08 00:00:00 |     7.352     |         12.6667   | NEUTRAL  | Kraken API    |
| INTU       | 2026-10-07 00:00:00 |   297.24      |         -2.25     | NEUTRAL  | Yahoo Finance |
| IWM        | 2026-10-07 00:00:00 |   277.7       |         -0.666667 | NEUTRAL  | Yahoo Finance |
| JNJ        | 2026-10-07 00:00:00 |   258.45      |        -45.3333   | NEUTRAL  | Yahoo Finance |
| JPM        | 2026-10-07 00:00:00 |   329.58      |        -15.3333   | NEUTRAL  | Yahoo Finance |
| KO         | 2026-10-07 00:00:00 |    85.82      |        -22.8333   | NEUTRAL  | Yahoo Finance |
| LDO-USD    | 2026-10-08 00:00:00 |     0.454     |         35.0833   | NEUTRAL  | Kraken API    |
| LINK-USD   | 2026-10-08 00:00:00 |    13.1546    |          3.66667  | NEUTRAL  | Kraken API    |
| LTC-USD    | 2026-10-08 00:00:00 |    64.52      |          8.83333  | NEUTRAL  | Kraken API    |
| MPC        | 2026-10-07 00:00:00 |   442.26      |         58.3333   | NEUTRAL  | Yahoo Finance |
| MRK        | 2026-10-07 00:00:00 |   142.79      |         -8.5      | NEUTRAL  | Yahoo Finance |
| NOW        | 2026-10-07 00:00:00 |   137.87      |         26.8333   | NEUTRAL  | Yahoo Finance |
| OP-USD     | 2026-10-08 00:00:00 |     0.1207    |        -14.5833   | NEUTRAL  | Kraken API    |
| ORCL       | 2026-10-07 00:00:00 |   143.56      |        -15.25     | NEUTRAL  | Yahoo Finance |
| OXY        | 2026-10-07 00:00:00 |    58.21      |         31.6667   | NEUTRAL  | Yahoo Finance |
| PEPE-USD   | 2026-10-08 00:00:00 |     4.032e-06 |         14.9167   | NEUTRAL  | Kraken API    |
| PFE        | 2026-10-07 00:00:00 |    28         |         50.3333   | NEUTRAL  | Yahoo Finance |
| PG         | 2026-10-07 00:00:00 |   147.82      |         32.8333   | NEUTRAL  | Yahoo Finance |
| PM         | 2026-10-07 00:00:00 |   192.69      |         33.8333   | NEUTRAL  | Yahoo Finance |
| POL-USD    | 2026-10-08 00:00:00 |     0.10129   |        -14.3333   | NEUTRAL  | Kraken API    |
| QCOM       | 2026-10-07 00:00:00 |   177.12      |         -9.58333  | NEUTRAL  | Yahoo Finance |
| SHY        | 2026-10-07 00:00:00 |    81.16      |        -26.75     | NEUTRAL  | Yahoo Finance |
| SKY-USD    | 2026-10-08 00:00:00 |     0.07913   |         15.5833   | NEUTRAL  | Kraken API    |
| SLV        | 2026-10-07 00:00:00 |    53.82      |        -69.5      | NEUTRAL  | Yahoo Finance |
| SNX-USD    | 2026-10-08 00:00:00 |     0.2417    |        -14.3333   | NEUTRAL  | Kraken API    |
| SOL-USD    | 2026-10-08 00:00:00 |   115.28      |         13.1667   | NEUTRAL  | Kraken API    |
| SPY        | 2026-10-07 00:00:00 |   777.22      |         62.6667   | NEUTRAL  | Yahoo Finance |
| SUSHI-USD  | 2026-10-08 00:00:00 |     0.2341    |         16.4167   | NEUTRAL  | Kraken API    |
| TGT        | 2026-10-07 00:00:00 |   150.92      |        -32.3333   | NEUTRAL  | Yahoo Finance |
| TMUS       | 2026-10-07 00:00:00 |   167.65      |        -28.5833   | NEUTRAL  | Yahoo Finance |
| TRX-USD    | 2026-10-08 00:00:00 |     0.334671  |        -40.5833   | NEUTRAL  | Kraken API    |
| TSLA       | 2026-10-07 00:00:00 |   377.81      |         40.6667   | NEUTRAL  | Yahoo Finance |
| UNH        | 2026-10-07 00:00:00 |   375.98      |         29.6667   | NEUTRAL  | Yahoo Finance |
| UNI-USD    | 2026-10-08 00:00:00 |     7.7089    |          7.33333  | NEUTRAL  | Kraken API    |
| USO        | 2026-10-07 00:00:00 |   143.91      |          3.41667  | NEUTRAL  | Yahoo Finance |
| VIXY       | 2026-10-07 00:00:00 |    16.19      |        -31.5      | NEUTRAL  | Yahoo Finance |
| VTI        | 2026-10-07 00:00:00 |   381.03      |         62.6667   | NEUTRAL  | Yahoo Finance |
| VWO        | 2026-10-07 00:00:00 |    59.85      |        -15.6667   | NEUTRAL  | Yahoo Finance |
| WIF-USD    | 2026-10-08 00:00:00 |     0.2245    |         -0.333333 | NEUTRAL  | Kraken API    |
| WMT        | 2026-10-07 00:00:00 |   108.16      |        -11.8333   | NEUTRAL  | Yahoo Finance |
| XBI        | 2026-10-07 00:00:00 |   150.23      |        -16.1667   | NEUTRAL  | Yahoo Finance |
| XLC        | 2026-10-07 00:00:00 |   111.26      |        -57.0833   | NEUTRAL  | Yahoo Finance |
| XLI        | 2026-10-07 00:00:00 |   167.84      |        -42.6667   | NEUTRAL  | Yahoo Finance |
| XLM-USD    | 2026-10-08 00:00:00 |     0.198687  |         -5.33333  | NEUTRAL  | Kraken API    |
| XLU        | 2026-10-07 00:00:00 |    41.15      |         -7.75     | NEUTRAL  | Yahoo Finance |
| XLV        | 2026-10-07 00:00:00 |   168.81      |         45.6667   | NEUTRAL  | Yahoo Finance |
| XLY        | 2026-10-07 00:00:00 |   111.36      |         -9.41667  | NEUTRAL  | Yahoo Finance |
| XOM        | 2026-10-07 00:00:00 |   164.05      |         28.8333   | NEUTRAL  | Yahoo Finance |
| XRP-USD    | 2026-10-08 00:00:00 |     1.40382   |         13.5833   | NEUTRAL  | Kraken API    |
| YFI-USD    | 2026-10-08 00:00:00 |  2376.1       |        -14.3333   | NEUTRAL  | Kraken API    |
| ZEC-USD    | 2026-10-08 00:00:00 |  1238.69      |          2.83333  | NEUTRAL  | Kraken API    |
| ADBE       | 2026-10-07 00:00:00 |   232.77      |        -33.6667   | SHORT    | Yahoo Finance |
| AGG        | 2026-10-07 00:00:00 |    94.31      |        -57.0833   | SHORT    | Yahoo Finance |
| BA         | 2026-10-07 00:00:00 |   188.32      |        -51.5833   | SHORT    | Yahoo Finance |
| BAC        | 2026-10-07 00:00:00 |    53.52      |        -40.6667   | SHORT    | Yahoo Finance |
| BND        | 2026-10-07 00:00:00 |    70         |        -57.0833   | SHORT    | Yahoo Finance |
| C          | 2026-10-07 00:00:00 |   127.32      |        -30.3333   | SHORT    | Yahoo Finance |
| CMCSA      | 2026-10-07 00:00:00 |    20.94      |        -59.9167   | SHORT    | Yahoo Finance |
| DOGE-USD   | 2026-10-08 00:00:00 |     0.0872241 |        -37.5833   | SHORT    | Kraken API    |
| EFA        | 2026-10-07 00:00:00 |   103.1       |        -30.0833   | SHORT    | Yahoo Finance |
| GDX        | 2026-10-07 00:00:00 |    85.46      |        -57.8333   | SHORT    | Yahoo Finance |
| GDXJ       | 2026-10-07 00:00:00 |   109.14      |        -54.5      | SHORT    | Yahoo Finance |
| GLD        | 2026-10-07 00:00:00 |   375.88      |        -59.5833   | SHORT    | Yahoo Finance |
| GS         | 2026-10-07 00:00:00 |   887.21      |        -59.9167   | SHORT    | Yahoo Finance |
| HD         | 2026-10-07 00:00:00 |   285.77      |        -31.25     | SHORT    | Yahoo Finance |
| HYG        | 2026-10-07 00:00:00 |    77.18      |        -57.0833   | SHORT    | Yahoo Finance |
| IEF        | 2026-10-07 00:00:00 |    89.11      |        -53.75     | SHORT    | Yahoo Finance |
| ITA        | 2026-10-07 00:00:00 |   203.6       |        -36.75     | SHORT    | Yahoo Finance |
| MCD        | 2026-10-07 00:00:00 |   230.88      |        -57.9167   | SHORT    | Yahoo Finance |
| MS         | 2026-10-07 00:00:00 |   189.71      |        -56.1667   | SHORT    | Yahoo Finance |
| NEM        | 2026-10-07 00:00:00 |   113.54      |        -35.3333   | SHORT    | Yahoo Finance |
| NFLX       | 2026-10-07 00:00:00 |    69.7       |        -38.4167   | SHORT    | Yahoo Finance |
| NKE        | 2026-10-07 00:00:00 |    34.36      |        -49.5833   | SHORT    | Yahoo Finance |
| PEP        | 2026-10-07 00:00:00 |   123.73      |        -57.9167   | SHORT    | Yahoo Finance |
| RTX        | 2026-10-07 00:00:00 |   180.26      |        -56.25     | SHORT    | Yahoo Finance |
| SBUX       | 2026-10-07 00:00:00 |    93.58      |        -33.75     | SHORT    | Yahoo Finance |
| SCHW       | 2026-10-07 00:00:00 |    95.58      |        -46.4167   | SHORT    | Yahoo Finance |
| SHIB-USD   | 2026-10-08 00:00:00 |     5.385e-06 |        -37.5833   | SHORT    | Kraken API    |
| SLB        | 2026-10-07 00:00:00 |    47.96      |        -59.9167   | SHORT    | Yahoo Finance |
| T          | 2026-10-07 00:00:00 |    24.47      |        -55.4167   | SHORT    | Yahoo Finance |
| TLT        | 2026-10-07 00:00:00 |    77.15      |        -59.0833   | SHORT    | Yahoo Finance |
| UPS        | 2026-10-07 00:00:00 |    92.29      |        -61.5833   | SHORT    | Yahoo Finance |
| VEA        | 2026-10-07 00:00:00 |    70.26      |        -31.75     | SHORT    | Yahoo Finance |
| VNQ        | 2026-10-07 00:00:00 |    88.69      |        -44.4167   | SHORT    | Yahoo Finance |
| VZ         | 2026-10-07 00:00:00 |    45.77      |        -51.6667   | SHORT    | Yahoo Finance |
| WFC        | 2026-10-07 00:00:00 |    80.26      |        -57.8333   | SHORT    | Yahoo Finance |
| XLB        | 2026-10-07 00:00:00 |    48.98      |        -33.4167   | SHORT    | Yahoo Finance |
| XLF        | 2026-10-07 00:00:00 |    53.75      |        -40.6667   | SHORT    | Yahoo Finance |
| XLP        | 2026-10-07 00:00:00 |    81.7       |        -33.75     | SHORT    | Yahoo Finance |

## Edge Summary

- Symbols with trades: **161** of 161
- Beat buy-and-hold: **31.06%** of traded symbols
- Positive return: **31.06%** of traded symbols
- Median strategy return: **-10.01%** (benchmark **17.97%**)
- Median excess vs benchmark: **-25.07%**
- Median Sharpe: **-0.13**
- Median exposure: **44.26%**

> Edge is real only if both _beat buy-and-hold_ and _median excess_ are convincingly positive across many symbols. Treat a single high-return symbol as noise.

## Portfolio Backtest

Actual capital-allocation books (not per-symbol averages). Benchmarks: `equal_weight_buyhold` (whole tracked universe), `spy_buyhold` (100% SPY), and `sixty_forty` (60% SPY / 40% AGG). `high_conf_voltarget` inverse-vol-weights the HIGH-confidence book; `conviction_long_short` is market-neutral. Judge on **Sharpe** and **max_drawdown** out-of-sample, not raw return: a fully-invested long book wins on return in a bull market but carries all the risk.

| strategy              | scope         | ann_return   | ann_vol   |   sharpe | max_drawdown   | total_return   |   avg_gross_exposure |
|:----------------------|:--------------|:-------------|:----------|---------:|:---------------|:---------------|---------------------:|
| equal_weight_buyhold  | full          | 12.51%       | 28.42%    |     0.44 | -39.53%        | 29.37%         |                 1    |
| equal_weight_buyhold  | out_of_sample | 7.32%        | 27.73%    |     0.26 | -28.22%        | 3.78%          |                 1    |
| all_signals_ew        | full          | -16.82%      | 24.16%    |    -0.7  | -60.53%        | -45.13%        |                 1    |
| all_signals_ew        | out_of_sample | 14.31%       | 23.10%    |     0.62 | -23.20%        | 13.21%         |                 1    |
| high_conf_ew          | full          | 0.25%        | 31.35%    |     0.01 | -44.85%        | -13.02%        |                 0.9  |
| high_conf_ew          | out_of_sample | 28.42%       | 27.39%    |     1.04 | -22.85%        | 29.92%         |                 0.9  |
| high_conf_voltarget   | full          | -0.84%       | 27.95%    |    -0.03 | -38.81%        | -13.23%        |                 0.9  |
| high_conf_voltarget   | out_of_sample | 15.69%       | 22.35%    |     0.7  | -17.00%        | 14.99%         |                 0.9  |
| conviction_long_short | full          | -16.02%      | 22.43%    |    -0.71 | -49.85%        | -43.10%        |                 0.96 |
| conviction_long_short | out_of_sample | 3.18%        | 19.50%    |     0.16 | -26.60%        | 1.38%          |                 0.96 |
| spy_buyhold           | full          | 4.61%        | 13.51%    |     0.34 | -19.00%        | 11.90%         |                 0.79 |
| spy_buyhold           | out_of_sample | 2.51%        | 9.91%     |     0.25 | -12.06%        | 2.18%          |                 0.79 |
| sixty_forty           | full          | 2.25%        | 8.54%     |     0.26 | -11.66%        | 5.90%          |                 0.79 |
| sixty_forty           | out_of_sample | -0.91%       | 6.68%     |    -0.14 | -8.26%         | -1.20%         |                 0.79 |

## Walk-Forward Robustness

Each book measured across contiguous time folds (each a different regime). A book has durable edge only if `mean_sharpe` is positive, `min_sharpe` isn't deeply negative, and `pct_positive_folds` is high — a single great fold doesn't count. `fold_sharpes` lists each fold oldest-to-newest.

| strategy              |   n_folds |   mean_sharpe |   median_sharpe |   min_sharpe | pct_positive_folds   | mean_return   | fold_sharpes                 |
|:----------------------|----------:|--------------:|----------------:|-------------:|:---------------------|:--------------|:-----------------------------|
| equal_weight_buyhold  |         5 |          0.59 |            0.81 |        -0.21 | 60.00%               | 5.88%         | 0.81;1.06;-0.08;-0.21;1.35   |
| all_signals_ew        |         5 |         -0.73 |           -1.28 |        -1.83 | 20.00%               | -9.36%        | -1.28;-1.69;-1.83;1.42;-0.28 |
| high_conf_ew          |         5 |          0.15 |            0.01 |        -0.87 | 60.00%               | -1.17%        | 0.01;-0.57;-0.87;1.30;0.90   |
| high_conf_voltarget   |         5 |          0.18 |            0.22 |        -0.81 | 60.00%               | -1.89%        | 0.22;-0.34;-0.81;0.78;1.05   |
| conviction_long_short |         5 |         -0.69 |           -0.61 |        -1.78 | 20.00%               | -10.37%       | -1.78;-0.49;-0.84;-0.61;0.27 |
| spy_buyhold           |         5 |          0.37 |            0.07 |        -0.19 | 60.00%               | 2.40%         | 1.52;-0.04;0.07;0.51;-0.19   |
| sixty_forty           |         5 |          0.26 |            0.23 |        -0.62 | 80.00%               | 1.20%         | 1.38;0.05;0.28;0.23;-0.62    |

## Strategy Comparison

Each decision rule backtested over the same data. `out_of_sample` is the most recent ~35% of each symbol's history (unseen tail). A rule has real edge only if `median_excess` and `beat_benchmark_pct` stay positive out-of-sample, not just full-sample.

| strategy        | scope         |   symbols | beat_benchmark_pct   | positive_pct   | median_return   | median_benchmark   | median_excess   |   median_sharpe |   total_trades |
|:----------------|:--------------|----------:|:---------------------|:---------------|:----------------|:-------------------|:----------------|----------------:|---------------:|
| trend           | full          |       161 | 31.06%               | 31.06%         | -10.01%         | 17.97%             | -25.07%         |           -0.13 |          11268 |
| trend           | out_of_sample |       161 | 28.57%               | 54.04%         | 0.69%           | 9.64%              | -13.11%         |            0.22 |           3772 |
| mean_reversion  | full          |       156 | 39.74%               | 48.08%         | -0.26%          | 14.54%             | -16.16%         |           -0.01 |           1218 |
| mean_reversion  | out_of_sample |       119 | 31.09%               | 52.10%         | 0.29%           | 8.58%              | -9.55%          |            0.15 |            482 |
| regime_adaptive | full          |       161 | 31.06%               | 32.30%         | -10.49%         | 17.97%             | -25.07%         |           -0.14 |          11537 |
| regime_adaptive | out_of_sample |       161 | 29.19%               | 52.80%         | 0.24%           | 9.64%              | -13.63%         |            0.16 |           3883 |

## Signal Calibration

Realized forward return in the signal's direction, grouped by confidence. HIGH should outrank LOW for the confidence score to be meaningful.

| confidence_level   |   horizon |     n | mean_return   | median_return   | win_rate   |
|:-------------------|----------:|------:|:--------------|:----------------|:-----------|
| HIGH               |         5 |  8033 | 0.18%         | 0.04%           | 50.62%     |
| MEDIUM             |         5 | 29145 | 0.01%         | 0.03%           | 50.28%     |
| LOW                |         5 |  3474 | -0.39%        | -0.41%          | 45.94%     |
| ALL                |         5 | 40652 | 0.01%         | 0.00%           | 49.97%     |
| HIGH               |        10 |  7969 | 0.47%         | 0.08%           | 50.95%     |
| MEDIUM             |        10 | 28824 | 0.18%         | 0.06%           | 50.46%     |
| LOW                |        10 |  3437 | -0.72%        | -0.56%          | 46.49%     |
| ALL                |        10 | 40230 | 0.16%         | 0.03%           | 50.22%     |
| HIGH               |        20 |  7796 | 1.12%         | 0.32%           | 52.71%     |
| MEDIUM             |        20 | 28355 | 0.85%         | 0.53%           | 52.97%     |
| LOW                |        20 |  3394 | -0.50%        | -0.64%          | 46.97%     |
| ALL                |        20 | 39545 | 0.79%         | 0.42%           | 52.40%     |

## Backtest Summary

### Data Quality / Signal Availability

- **ok**: 161 symbols

| symbol     |   trades | return   | benchmark_return   | mdd     |   sharpe | exposure   | skipped_reason   |
|:-----------|---------:|:---------|:-------------------|:--------|---------:|:-----------|:-----------------|
| AAPL       |       64 | 4.32%    | 77.46%             | -23.09% |     0.19 | 51.41%     | ok               |
| AAVE-USD   |       65 | -22.00%  | -2.13%             | -66.17% |    -0    | 42.15%     | ok               |
| ABBV       |       70 | -25.73%  | 65.68%             | -30.52% |    -0.58 | 47.92%     | ok               |
| ADA-USD    |       75 | -31.71%  | -61.81%            | -46.79% |    -0.19 | 46.74%     | ok               |
| ADBE       |       75 | -7.14%   | -52.04%            | -31.20% |     0.04 | 55.91%     | ok               |
| AGG        |       65 | -6.83%   | -2.96%             | -11.01% |    -1.08 | 33.61%     | ok               |
| ALGO-USD   |       76 | -35.17%  | -40.97%            | -38.19% |    -0.27 | 40.23%     | ok               |
| AMAT       |       73 | -36.16%  | 139.39%            | -57.56% |    -0.33 | 51.25%     | ok               |
| AMD        |       52 | 34.62%   | 304.50%            | -40.05% |     0.51 | 36.61%     | ok               |
| AMGN       |       69 | -18.61%  | 29.48%             | -34.19% |    -0.36 | 50.25%     | ok               |
| AMZN       |       80 | -56.43%  | 39.75%             | -56.88% |    -1.62 | 40.77%     | ok               |
| APT-USD    |       72 | -32.01%  | -84.53%            | -62.06% |    -0.11 | 40.23%     | ok               |
| ARB-USD    |       77 | -21.49%  | -41.39%            | -55.44% |     0.08 | 43.87%     | ok               |
| ARKK       |       84 | -23.42%  | 92.92%             | -28.66% |    -0.31 | 42.76%     | ok               |
| ATOM-USD   |       92 | -58.27%  | -57.64%            | -58.27% |    -0.81 | 48.28%     | ok               |
| AVAX-USD   |       68 | -30.12%  | -44.62%            | -45.19% |    -0.2  | 40.23%     | ok               |
| AVGO       |       64 | 15.79%   | 162.16%            | -36.09% |     0.35 | 41.93%     | ok               |
| BA         |       69 | 5.62%    | 6.40%              | -26.26% |     0.22 | 50.92%     | ok               |
| BAC        |       72 | -9.71%   | 37.55%             | -25.80% |    -0.21 | 48.25%     | ok               |
| BCH-USD    |       72 | 20.21%   | -16.42%            | -53.87% |     0.41 | 49.04%     | ok               |
| BITO       |       79 | -18.12%  | -58.49%            | -43.10% |    -0.07 | 42.26%     | ok               |
| BLK        |       85 | -17.03%  | 31.13%             | -26.90% |    -0.43 | 47.92%     | ok               |
| BND        |       67 | -6.80%   | -2.93%             | -10.91% |    -1.03 | 35.77%     | ok               |
| BONK-USD   |       72 | 30.50%   | -79.88%            | -45.22% |     0.51 | 45.59%     | ok               |
| BTC-USD    |       70 | 16.28%   | -12.56%            | -23.38% |     0.4  | 53.07%     | ok               |
| C          |       75 | -34.91%  | 98.19%             | -39.51% |    -0.75 | 46.59%     | ok               |
| CAT        |       70 | 3.48%    | 126.04%            | -22.01% |     0.18 | 48.92%     | ok               |
| CL         |       64 | -5.50%   | -7.74%             | -14.32% |    -0.13 | 39.10%     | ok               |
| CMCSA      |       84 | -34.85%  | -43.08%            | -46.39% |    -0.83 | 42.60%     | ok               |
| COMP-USD   |       95 | -35.33%  | -39.57%            | -55.77% |    -0.17 | 49.23%     | ok               |
| COP        |       66 | -16.32%  | 7.57%              | -41.35% |    -0.22 | 43.43%     | ok               |
| COST       |       58 | -0.57%   | 19.72%             | -30.95% |     0.05 | 41.60%     | ok               |
| CRM        |       65 | -34.52%  | -21.90%            | -45.50% |    -0.51 | 45.92%     | ok               |
| CRV-USD    |       68 | 25.99%   | -44.26%            | -39.89% |     0.47 | 37.93%     | ok               |
| CSCO       |       64 | 19.32%   | 136.34%            | -21.79% |     0.44 | 48.59%     | ok               |
| CVX        |       69 | -11.05%  | 25.82%             | -26.75% |    -0.22 | 42.26%     | ok               |
| DASH-USD   |       57 | -9.06%   | 145.43%            | -64.43% |     0.33 | 30.84%     | ok               |
| DBC        |       66 | -8.14%   | 38.87%             | -24.10% |    -0.21 | 35.27%     | ok               |
| DE         |       70 | -12.17%  | 58.66%             | -23.98% |    -0.18 | 44.26%     | ok               |
| DIA        |       64 | -7.92%   | 27.99%             | -12.94% |    -0.41 | 43.93%     | ok               |
| DIS        |       64 | -8.07%   | 1.93%              | -28.17% |    -0.09 | 43.43%     | ok               |
| DOGE-USD   |       69 | -31.92%  | -48.87%            | -60.95% |    -0.12 | 48.47%     | ok               |
| DOT-USD    |       88 | -58.07%  | -71.95%            | -63.33% |    -0.55 | 49.04%     | ok               |
| DXY-INDEX  |       40 | -0.52%   | -3.46%             | -6.02%  |    -0.07 | 31.17%     | ok               |
| EEM        |       62 | -12.61%  | 54.84%             | -25.38% |    -0.36 | 40.77%     | ok               |
| EFA        |       64 | -11.65%  | 26.04%             | -12.84% |    -0.45 | 42.93%     | ok               |
| EOG        |       78 | -29.89%  | 11.71%             | -47.50% |    -0.64 | 44.43%     | ok               |
| ETC-USD    |       56 | -22.45%  | -47.91%            | -48.09% |    -0.2  | 30.65%     | ok               |
| ETH-USD    |       58 | 178.93%  | 41.10%             | -30.11% |     1.44 | 48.85%     | ok               |
| EWJ        |       62 | -22.99%  | 42.55%             | -29.40% |    -0.8  | 36.44%     | ok               |
| FCX        |       65 | -29.37%  | 34.04%             | -46.84% |    -0.32 | 44.26%     | ok               |
| FET-USD    |       77 | -40.68%  | -65.02%            | -60.12% |    -0.21 | 41.76%     | ok               |
| FIL-USD    |       65 | -48.57%  | -59.69%            | -58.54% |    -0.52 | 36.59%     | ok               |
| FXI        |       50 | -7.64%   | 17.97%             | -24.33% |    -0.11 | 31.95%     | ok               |
| GDX        |       58 | -2.33%   | 137.98%            | -33.31% |     0.1  | 44.26%     | ok               |
| GDXJ       |       68 | -36.38%  | 145.81%            | -41.57% |    -0.48 | 42.60%     | ok               |
| GE         |       78 | -9.80%   | 85.73%             | -27.82% |    -0.07 | 48.25%     | ok               |
| GLD        |       50 | 10.82%   | 70.17%             | -13.87% |     0.34 | 45.26%     | ok               |
| GOOGL      |       57 | 57.34%   | 103.18%            | -17.54% |     1.01 | 47.25%     | ok               |
| GRT-USD    |       77 | 25.63%   | -70.35%            | -45.34% |     0.46 | 45.79%     | ok               |
| GS         |       70 | -4.46%   | 90.35%             | -22.13% |     0    | 48.09%     | ok               |
| HBAR-USD   |       38 | -44.08%  | -10.25%            | -56.39% |    -0.99 | 37.74%     | ok               |
| HD         |       69 | 3.78%    | -18.04%            | -17.15% |     0.18 | 43.09%     | ok               |
| HON        |       89 | -27.58%  | 2.67%              | -33.03% |    -0.69 | 55.24%     | ok               |
| HYG        |       87 | -7.29%   | -0.35%             | -10.59% |    -0.82 | 38.10%     | ok               |
| IBIT       |       38 | 40.42%   | 24.20%             | -18.95% |     0.73 | 34.63%     | ok               |
| IBM        |       69 | -24.27%  | 31.05%             | -48.94% |    -0.28 | 49.92%     | ok               |
| ICP-USD    |       77 | 0.63%    | -30.82%            | -46.42% |     0.26 | 39.27%     | ok               |
| IEF        |       78 | -10.49%  | -4.78%             | -13.34% |    -1.43 | 34.28%     | ok               |
| IEMG       |       62 | -13.09%  | 50.39%             | -29.43% |    -0.4  | 41.26%     | ok               |
| INJ-USD    |       63 | -23.82%  | -21.34%            | -69.96% |     0.01 | 39.85%     | ok               |
| INTC       |       68 | 44.57%   | 261.75%            | -60.60% |     0.55 | 48.09%     | ok               |
| INTU       |       73 | -11.45%  | -54.63%            | -37.50% |    -0.05 | 46.76%     | ok               |
| ITA        |       72 | -1.89%   | 51.53%             | -23.75% |     0.03 | 48.92%     | ok               |
| IWM        |       54 | 6.34%    | 32.59%             | -12.28% |     0.29 | 34.94%     | ok               |
| JNJ        |       64 | 5.87%    | 69.29%             | -16.86% |     0.26 | 47.09%     | ok               |
| JPM        |       73 | -23.85%  | 63.07%             | -32.74% |    -0.65 | 45.76%     | ok               |
| KO         |       54 | 22.97%   | 35.94%             | -8.64%  |     0.82 | 37.60%     | ok               |
| LDO-USD    |       72 | 10.52%   | -42.31%            | -59.24% |     0.37 | 46.93%     | ok               |
| LIN        |       72 | -11.85%  | 12.34%             | -20.61% |    -0.38 | 37.94%     | ok               |
| LINK-USD   |       69 | 31.57%   | -3.55%             | -33.64% |     0.52 | 46.55%     | ok               |
| LLY        |       76 | -35.01%  | 51.04%             | -53.34% |    -0.58 | 49.08%     | ok               |
| LRCX       |       78 | -22.56%  | 247.68%            | -58.79% |    -0.11 | 42.43%     | ok               |
| LTC-USD    |       67 | 15.32%   | -22.49%            | -32.66% |     0.37 | 53.83%     | ok               |
| MCD        |       77 | 2.11%    | -15.70%            | -21.88% |     0.13 | 40.10%     | ok               |
| META       |       78 | -28.05%  | 49.79%             | -44.52% |    -0.4  | 50.25%     | ok               |
| MPC        |       71 | 15.43%   | 156.16%            | -37.91% |     0.36 | 52.08%     | ok               |
| MRK        |       69 | -24.52%  | 8.40%              | -35.95% |    -0.48 | 42.76%     | ok               |
| MS         |       75 | -10.16%  | 88.73%             | -27.79% |    -0.17 | 48.25%     | ok               |
| MSFT       |       83 | -25.31%  | 25.22%             | -38.06% |    -0.54 | 50.58%     | ok               |
| MU         |       51 | 151.83%  | 751.26%            | -68.76% |     1.04 | 53.24%     | ok               |
| NEAR-USD   |       73 | 139.67%  | 133.46%            | -52.25% |     1.02 | 44.25%     | ok               |
| NEM        |       66 | -26.24%  | 162.88%            | -39.56% |    -0.25 | 50.42%     | ok               |
| NFLX       |       78 | 12.61%   | 13.61%             | -21.09% |     0.35 | 53.58%     | ok               |
| NKE        |       79 | -24.27%  | -62.52%            | -55.35% |    -0.24 | 46.42%     | ok               |
| NOW        |       82 | 10.56%   | -9.36%             | -30.43% |     0.3  | 50.42%     | ok               |
| NVDA       |       75 | -46.46%  | 84.89%             | -52.37% |    -0.63 | 54.72%     | ok               |
| OP-USD     |       68 | -40.82%  | -81.24%            | -68.74% |    -0.3  | 33.52%     | ok               |
| ORCL       |       62 | 90.07%   | 18.03%             | -30.61% |     0.82 | 52.91%     | ok               |
| OXY        |       69 | -0.67%   | -8.16%             | -28.48% |     0.11 | 42.26%     | ok               |
| PEP        |       74 | 4.13%    | -31.05%            | -21.35% |     0.19 | 45.92%     | ok               |
| PEPE-USD   |       85 | -45.82%  | -49.18%            | -61.29% |    -0.24 | 49.43%     | ok               |
| PFE        |       81 | -34.82%  | -2.85%             | -41.90% |    -1.07 | 37.44%     | ok               |
| PG         |       64 | -23.31%  | -11.22%            | -24.16% |    -0.94 | 35.27%     | ok               |
| PM         |       79 | -8.05%   | 91.60%             | -35.15% |    -0.09 | 50.92%     | ok               |
| POL-USD    |       81 | 29.19%   | -54.69%            | -38.69% |     0.5  | 50.00%     | ok               |
| QCOM       |       77 | -27.33%  | -8.99%             | -57.69% |    -0.22 | 44.09%     | ok               |
| QQQ        |       66 | 11.28%   | 67.31%             | -14.20% |     0.37 | 45.76%     | ok               |
| RENDER-USD |       92 | -15.42%  | -53.87%            | -44.84% |     0.12 | 46.93%     | ok               |
| RTX        |       64 | 34.84%   | 71.11%             | -16.99% |     0.77 | 52.41%     | ok               |
| SBUX       |       60 | -13.89%  | 23.62%             | -29.22% |    -0.22 | 38.44%     | ok               |
| SCHW       |       80 | -18.82%  | 21.48%             | -31.92% |    -0.42 | 46.26%     | ok               |
| SHIB-USD   |       79 | -44.47%  | -57.57%            | -45.40% |    -0.49 | 52.11%     | ok               |
| SHY        |       46 | -1.78%   | -0.45%             | -3.30%  |    -0.6  | 36.77%     | ok               |
| SKY-USD    |       87 | -53.28%  | 22.06%             | -61.34% |    -0.71 | 45.40%     | ok               |
| SLB        |       75 | -36.69%  | -0.72%             | -57.55% |    -0.68 | 48.59%     | ok               |
| SLV        |       66 | 11.38%   | 98.45%             | -42.66% |     0.31 | 40.60%     | ok               |
| SMH        |       48 | 57.21%   | 167.22%            | -34.29% |     0.88 | 44.26%     | ok               |
| SNX-USD    |       62 | -20.84%  | -62.53%            | -50.27% |    -0.03 | 33.91%     | ok               |
| SOL-USD    |       68 | -10.24%  | -21.37%            | -44.99% |     0.12 | 60.54%     | ok               |
| SOXX       |       54 | 73.64%   | 152.66%            | -39.81% |     0.99 | 43.09%     | ok               |
| SPY        |       64 | -0.12%   | 46.71%             | -15.53% |     0.06 | 50.25%     | ok               |
| SUSHI-USD  |       96 | -82.21%  | -61.62%            | -82.74% |    -1.38 | 39.85%     | ok               |
| T          |       72 | 38.72%   | 41.20%             | -17.01% |     0.83 | 56.74%     | ok               |
| TGT        |       62 | -11.80%  | -4.18%             | -34.98% |    -0.18 | 37.77%     | ok               |
| TIA-USD    |       95 | -68.45%  | -80.05%            | -78.90% |    -0.73 | 42.34%     | ok               |
| TLT        |       70 | -18.85%  | -16.23%            | -22.03% |    -1.41 | 33.94%     | ok               |
| TMO        |       67 | 27.63%   | 10.52%             | -18.85% |     0.58 | 55.57%     | ok               |
| TMUS       |       74 | 2.61%    | 3.06%              | -28.12% |     0.15 | 47.92%     | ok               |
| TRX-USD    |       68 | 9.69%    | 34.76%             | -22.90% |     0.35 | 51.92%     | ok               |
| TSLA       |       78 | -35.10%  | 117.14%            | -58.36% |    -0.22 | 43.09%     | ok               |
| TXN        |       77 | -21.67%  | 47.79%             | -46.98% |    -0.2  | 50.08%     | ok               |
| UNH        |       75 | 23.37%   | -27.35%            | -26.31% |     0.45 | 48.75%     | ok               |
| UNI-USD    |       92 | -54.92%  | 55.02%             | -78.80% |    -0.35 | 50.77%     | ok               |
| UPS        |       72 | -33.36%  | -37.62%            | -39.06% |    -0.64 | 42.10%     | ok               |
| USO        |       67 | -9.34%   | 89.65%             | -44.98% |    -0.01 | 33.28%     | ok               |
| VEA        |       58 | -3.38%   | 37.20%             | -16.11% |    -0.09 | 43.26%     | ok               |
| VIXY       |       94 | -78.22%  | -64.59%            | -88.19% |    -0.94 | 33.28%     | ok               |
| VNQ        |       75 | -13.98%  | 4.39%              | -24.92% |    -0.56 | 39.93%     | ok               |
| VTI        |       68 | -7.66%   | 45.08%             | -17.64% |    -0.22 | 50.25%     | ok               |
| VWO        |       79 | -20.54%  | 34.80%             | -27.17% |    -0.78 | 41.60%     | ok               |
| VZ         |       84 | -19.57%  | 13.04%             | -25.90% |    -0.57 | 41.26%     | ok               |
| WFC        |       80 | -16.70%  | 28.75%             | -28.90% |    -0.27 | 47.75%     | ok               |
| WIF-USD    |       64 | -26.40%  | -58.98%            | -52.76% |    -0.01 | 36.97%     | ok               |
| WMT        |       69 | 4.37%    | 80.78%             | -25.37% |     0.19 | 49.08%     | ok               |
| XBI        |       64 | -3.65%   | 62.22%             | -18.28% |    -0.01 | 39.60%     | ok               |
| XLB        |       62 | -13.31%  | 6.44%              | -25.04% |    -0.47 | 32.28%     | ok               |
| XLC        |       61 | 12.62%   | 34.81%             | -12.33% |     0.47 | 50.25%     | ok               |
| XLE        |       69 | -9.12%   | 34.94%             | -30.31% |    -0.15 | 44.43%     | ok               |
| XLF        |       80 | -8.65%   | 27.43%             | -23.61% |    -0.26 | 46.76%     | ok               |
| XLI        |       82 | -10.01%  | 33.27%             | -17.76% |    -0.35 | 42.76%     | ok               |
| XLK        |       42 | 59.41%   | 89.07%             | -14.75% |     1.13 | 46.59%     | ok               |
| XLM-USD    |       65 | -6.83%   | -23.10%            | -54.58% |     0.15 | 48.08%     | ok               |
| XLP        |       66 | 3.16%    | 5.69%              | -11.16% |     0.22 | 38.10%     | ok               |
| XLU        |       69 | -6.55%   | 13.47%             | -20.40% |    -0.24 | 40.43%     | ok               |
| XLV        |       76 | -22.35%  | 15.47%             | -22.75% |    -1.08 | 37.60%     | ok               |
| XLY        |       75 | -4.15%   | 24.46%             | -18.35% |    -0.06 | 47.59%     | ok               |
| XOM        |       55 | 1.71%    | 38.35%             | -20.29% |     0.12 | 34.28%     | ok               |
| XRP-USD    |       62 | 10.41%   | -34.16%            | -33.91% |     0.32 | 36.78%     | ok               |
| YFI-USD    |       77 | -70.53%  | -54.79%            | -70.53% |    -1.37 | 37.93%     | ok               |
| ZEC-USD    |       59 | 173.34%  | 3284.40%           | -56.50% |     0.98 | 42.53%     | ok               |

## AAPL Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 10.84%   | 77.46%             | -22.53% |     0.31 |       73 | 56.24%     | ok               |
|          15 | 7.99%    | 77.46%             | -24.50% |     0.26 |       82 | 63.56%     | ok               |
|          30 | 4.32%    | 77.46%             | -23.09% |     0.19 |       64 | 51.41%     | ok               |
|          40 | 3.21%    | 77.46%             | -28.08% |     0.17 |       60 | 45.92%     | ok               |
|          35 | 2.82%    | 77.46%             | -24.45% |     0.16 |       64 | 50.08%     | ok               |

## AAVE-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 53.03%   | -2.13%             | -43.61% |     0.67 |       43 | 36.59%     | ok               |
|          45 | 38.77%   | -2.13%             | -49.19% |     0.58 |       48 | 31.42%     | ok               |
|          35 | 33.49%   | -2.13%             | -48.79% |     0.53 |       51 | 39.66%     | ok               |
|          50 | 23.38%   | -2.13%             | -45.07% |     0.45 |       46 | 24.14%     | ok               |
|          15 | -13.38%  | -2.13%             | -61.76% |     0.16 |       72 | 55.36%     | ok               |

## ABBV Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -15.94%  | 65.68%             | -27.91% |    -0.36 |       54 | 34.94%     | ok               |
|          25 | -24.48%  | 65.68%             | -30.41% |    -0.53 |       69 | 49.92%     | ok               |
|          20 | -24.93%  | 65.68%             | -29.62% |    -0.53 |       67 | 51.58%     | ok               |
|          30 | -25.73%  | 65.68%             | -30.52% |    -0.58 |       70 | 47.92%     | ok               |
|          40 | -23.92%  | 65.68%             | -27.36% |    -0.58 |       70 | 40.10%     | ok               |

## ADA-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 23.45%   | -61.81%            | -35.54% |     0.46 |       48 | 27.97%     | ok               |
|          45 | 11.74%   | -61.81%            | -34.64% |     0.34 |       47 | 32.57%     | ok               |
|          40 | -7.31%   | -61.81%            | -40.73% |     0.13 |       59 | 38.51%     | ok               |
|          35 | -11.75%  | -61.81%            | -42.89% |     0.08 |       63 | 42.15%     | ok               |
|          15 | -21.85%  | -61.81%            | -47.27% |     0.06 |       70 | 62.64%     | ok               |

## ADBE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | 9.76%    | -52.04%            | -29.07% |     0.28 |       56 | 60.57%     | ok               |
|          35 | -1.52%   | -52.04%            | -31.73% |     0.11 |       79 | 46.92%     | ok               |
|          20 | -5.40%   | -52.04%            | -31.52% |     0.08 |       64 | 63.89%     | ok               |
|          30 | -7.14%   | -52.04%            | -31.20% |     0.04 |       75 | 55.91%     | ok               |
|          15 | -15.34%  | -52.04%            | -34.98% |    -0.07 |       62 | 66.06%     | ok               |

## AGG Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -5.78%   | -2.96%             | -9.59%  |    -1.03 |       58 | 25.29%     | ok               |
|          50 | -5.12%   | -2.96%             | -8.07%  |    -1.07 |       54 | 20.47%     | ok               |
|          30 | -6.83%   | -2.96%             | -11.01% |    -1.08 |       65 | 33.61%     | ok               |
|          20 | -8.24%   | -2.96%             | -11.89% |    -1.18 |       72 | 38.60%     | ok               |
|          25 | -8.16%   | -2.96%             | -12.28% |    -1.22 |       71 | 36.77%     | ok               |

## ALGO-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -35.17%  | -40.97%            | -38.19% |    -0.27 |       76 | 40.23%     | ok               |
|          15 | -42.15%  | -40.97%            | -51.37% |    -0.31 |       79 | 50.19%     | ok               |
|          25 | -43.46%  | -40.97%            | -54.39% |    -0.38 |       78 | 45.02%     | ok               |
|          20 | -48.23%  | -40.97%            | -53.23% |    -0.44 |       81 | 47.70%     | ok               |
|          35 | -46.50%  | -40.97%            | -50.03% |    -0.57 |       64 | 35.06%     | ok               |

## AMAT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -20.04%  | 139.39%            | -39.20% |    -0.13 |       50 | 35.44%     | ok               |
|          15 | -28.62%  | 139.39%            | -53.90% |    -0.17 |       72 | 60.07%     | ok               |
|          35 | -31.42%  | 139.39%            | -52.00% |    -0.27 |       73 | 48.59%     | ok               |
|          30 | -36.16%  | 139.39%            | -57.56% |    -0.33 |       73 | 51.25%     | ok               |
|          40 | -37.00%  | 139.39%            | -54.64% |    -0.38 |       71 | 43.76%     | ok               |

## AMD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 35.63%   | 304.50%            | -40.05% |     0.52 |       58 | 31.78%     | ok               |
|          40 | 34.62%   | 304.50%            | -40.05% |     0.51 |       52 | 36.61%     | ok               |
|          35 | 31.85%   | 304.50%            | -42.14% |     0.49 |       60 | 38.10%     | ok               |
|          30 | 18.71%   | 304.50%            | -47.00% |     0.39 |       65 | 40.60%     | ok               |
|          25 | 13.53%   | 304.50%            | -51.79% |     0.34 |       61 | 42.76%     | ok               |

## AMGN Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -13.95%  | 29.48%             | -26.65% |    -0.22 |       64 | 56.07%     | ok               |
|          35 | -16.50%  | 29.48%             | -31.29% |    -0.31 |       69 | 46.76%     | ok               |
|          30 | -18.61%  | 29.48%             | -34.19% |    -0.36 |       69 | 50.25%     | ok               |
|          15 | -20.94%  | 29.48%             | -27.98% |    -0.37 |       63 | 60.40%     | ok               |
|          25 | -20.41%  | 29.48%             | -33.47% |    -0.4  |       63 | 52.58%     | ok               |

## AMZN Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -27.29%  | 39.75%             | -28.95% |    -0.83 |       54 | 29.78%     | ok               |
|          50 | -31.74%  | 39.75%             | -33.91% |    -1.16 |       50 | 22.80%     | ok               |
|          45 | -36.87%  | 39.75%             | -37.67% |    -1.31 |       56 | 26.29%     | ok               |
|          35 | -51.03%  | 39.75%             | -51.54% |    -1.48 |       73 | 34.94%     | ok               |
|          30 | -56.43%  | 39.75%             | -56.88% |    -1.62 |       80 | 40.77%     | ok               |

## APT-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 3.34%    | -84.53%            | -61.36% |     0.31 |       76 | 49.81%     | ok               |
|          50 | 6.76%    | -84.53%            | -39.70% |     0.26 |       44 | 16.67%     | ok               |
|          25 | -22.08%  | -84.53%            | -61.15% |     0.04 |       70 | 44.64%     | ok               |
|          45 | -15.94%  | -84.53%            | -59.21% |    -0.01 |       60 | 23.56%     | ok               |
|          15 | -33.11%  | -84.53%            | -63.36% |    -0.04 |       74 | 55.56%     | ok               |

## ARB-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 55.57%   | -41.39%            | -44.26% |     0.64 |       85 | 60.15%     | ok               |
|          45 | 30.34%   | -41.39%            | -35.90% |     0.49 |       56 | 26.82%     | ok               |
|          20 | 15.92%   | -41.39%            | -54.05% |     0.42 |       71 | 54.60%     | ok               |
|          50 | 21.38%   | -41.39%            | -30.72% |     0.42 |       44 | 19.73%     | ok               |
|          40 | 5.58%    | -41.39%            | -40.13% |     0.31 |       57 | 34.10%     | ok               |

## ARKK Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -12.57%  | 92.92%             | -37.76% |    -0.04 |       90 | 54.58%     | ok               |
|          20 | -16.48%  | 92.92%             | -34.82% |    -0.12 |       86 | 49.75%     | ok               |
|          30 | -23.42%  | 92.92%             | -28.66% |    -0.31 |       84 | 42.76%     | ok               |
|          35 | -31.46%  | 92.92%             | -34.08% |    -0.52 |       84 | 40.43%     | ok               |
|          25 | -36.96%  | 92.92%             | -43.18% |    -0.6  |       96 | 45.59%     | ok               |

## ATOM-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -41.59%  | -57.64%            | -48.20% |    -0.33 |       86 | 65.90%     | ok               |
|          25 | -48.34%  | -57.64%            | -49.45% |    -0.52 |       92 | 54.60%     | ok               |
|          20 | -55.70%  | -57.64%            | -57.28% |    -0.66 |       96 | 58.24%     | ok               |
|          30 | -58.27%  | -57.64%            | -58.27% |    -0.81 |       92 | 48.28%     | ok               |
|          35 | -58.92%  | -57.64%            | -61.18% |    -0.93 |       82 | 42.34%     | ok               |

## AVAX-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 32.87%   | -44.62%            | -22.06% |     0.59 |       34 | 19.92%     | ok               |
|          40 | 22.82%   | -44.62%            | -26.27% |     0.46 |       36 | 27.59%     | ok               |
|          45 | 19.37%   | -44.62%            | -23.19% |     0.43 |       30 | 24.52%     | ok               |
|          35 | 3.67%    | -44.62%            | -33.05% |     0.24 |       54 | 33.91%     | ok               |
|          15 | -10.80%  | -44.62%            | -42.39% |     0.12 |       73 | 53.45%     | ok               |

## AVGO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | 19.12%   | 162.16%            | -38.01% |     0.38 |       68 | 44.59%     | ok               |
|          30 | 15.79%   | 162.16%            | -36.09% |     0.35 |       64 | 41.93%     | ok               |
|          50 | 10.84%   | 162.16%            | -36.86% |     0.29 |       56 | 29.78%     | ok               |
|          35 | 7.38%    | 162.16%            | -40.43% |     0.26 |       74 | 38.94%     | ok               |
|          20 | 5.45%    | 162.16%            | -39.42% |     0.24 |       77 | 47.75%     | ok               |

## BA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 40.71%   | 6.40%              | -13.34% |     0.89 |       46 | 35.61%     | ok               |
|          40 | 34.98%   | 6.40%              | -23.87% |     0.67 |       46 | 43.43%     | ok               |
|          35 | 35.60%   | 6.40%              | -18.09% |     0.65 |       64 | 47.59%     | ok               |
|          25 | 15.42%   | 6.40%              | -26.72% |     0.36 |       70 | 54.41%     | ok               |
|          45 | 7.30%    | 6.40%              | -26.76% |     0.25 |       44 | 39.77%     | ok               |

## BAC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 0.63%    | 37.55%             | -23.08% |     0.09 |       64 | 44.93%     | ok               |
|          20 | -1.09%   | 37.55%             | -18.20% |     0.06 |       80 | 52.91%     | ok               |
|          25 | -3.51%   | 37.55%             | -22.11% |    -0.02 |       74 | 50.42%     | ok               |
|          15 | -9.03%   | 37.55%             | -23.94% |    -0.13 |       87 | 60.07%     | ok               |
|          45 | -6.80%   | 37.55%             | -19.47% |    -0.15 |       60 | 36.94%     | ok               |

## BCH-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 55.73%   | -16.42%            | -45.51% |     0.68 |       72 | 57.47%     | ok               |
|          20 | 29.16%   | -16.42%            | -45.63% |     0.49 |       64 | 54.21%     | ok               |
|          30 | 20.21%   | -16.42%            | -53.87% |     0.41 |       72 | 49.04%     | ok               |
|          25 | 19.98%   | -16.42%            | -51.09% |     0.41 |       66 | 50.57%     | ok               |
|          35 | 0.88%    | -16.42%            | -57.99% |     0.22 |       70 | 45.79%     | ok               |

## BITO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -5.40%   | -58.49%            | -31.98% |     0.06 |       54 | 25.79%     | ok               |
|          30 | -18.12%  | -58.49%            | -43.10% |    -0.07 |       79 | 42.26%     | ok               |
|          45 | -18.44%  | -58.49%            | -34.92% |    -0.14 |       60 | 29.28%     | ok               |
|          15 | -27.88%  | -58.49%            | -51.47% |    -0.17 |       86 | 50.42%     | ok               |
|          25 | -25.48%  | -58.49%            | -41.96% |    -0.17 |       83 | 45.42%     | ok               |

## BLK Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | -9.00%   | 31.13%             | -20.79% |    -0.2  |       92 | 44.26%     | ok               |
|          20 | -11.72%  | 31.13%             | -21.48% |    -0.24 |       88 | 52.58%     | ok               |
|          40 | -10.21%  | 31.13%             | -22.83% |    -0.25 |       80 | 39.43%     | ok               |
|          25 | -12.99%  | 31.13%             | -24.62% |    -0.29 |       81 | 50.42%     | ok               |
|          30 | -17.03%  | 31.13%             | -26.90% |    -0.43 |       85 | 47.92%     | ok               |

## BND Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -6.42%   | -2.93%             | -10.21% |    -0.9  |       66 | 40.77%     | ok               |
|          25 | -7.07%   | -2.93%             | -11.27% |    -1.03 |       69 | 38.77%     | ok               |
|          30 | -6.80%   | -2.93%             | -10.91% |    -1.03 |       67 | 35.77%     | ok               |
|          15 | -8.12%   | -2.93%             | -11.52% |    -1.13 |       77 | 43.43%     | ok               |
|          35 | -8.35%   | -2.93%             | -12.42% |    -1.34 |       70 | 32.28%     | ok               |

## BONK-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 156.03%  | -79.88%            | -35.57% |     1.2  |       42 | 21.46%     | ok               |
|          45 | 69.26%   | -79.88%            | -42.36% |     0.75 |       66 | 27.78%     | ok               |
|          15 | 63.58%   | -79.88%            | -63.45% |     0.68 |       68 | 59.96%     | ok               |
|          20 | 54.11%   | -79.88%            | -55.19% |     0.64 |       66 | 55.75%     | ok               |
|          40 | 38.07%   | -79.88%            | -50.07% |     0.55 |       56 | 37.36%     | ok               |

## BTC-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 56.99%   | -12.56%            | -14.50% |     1.04 |       44 | 36.59%     | ok               |
|          45 | 52.08%   | -12.56%            | -12.20% |     1.01 |       42 | 32.57%     | ok               |
|          35 | 55.90%   | -12.56%            | -21.56% |     0.99 |       62 | 42.91%     | ok               |
|          30 | 28.87%   | -12.56%            | -21.75% |     0.59 |       68 | 48.85%     | ok               |
|          50 | 20.45%   | -12.56%            | -20.63% |     0.54 |       42 | 27.01%     | ok               |

## C Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -12.42%  | 98.19%             | -21.80% |    -0.29 |       66 | 31.95%     | ok               |
|          45 | -20.47%  | 98.19%             | -27.40% |    -0.51 |       72 | 35.94%     | ok               |
|          40 | -26.09%  | 98.19%             | -33.13% |    -0.64 |       74 | 38.27%     | ok               |
|          25 | -31.98%  | 98.19%             | -36.78% |    -0.66 |       67 | 48.59%     | ok               |
|          15 | -35.92%  | 98.19%             | -38.73% |    -0.71 |       70 | 55.57%     | ok               |

## CAT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 16.60%   | 126.04%            | -20.92% |     0.37 |       73 | 61.23%     | ok               |
|          25 | 10.83%   | 126.04%            | -22.20% |     0.3  |       66 | 51.25%     | ok               |
|          45 | 4.30%    | 126.04%            | -24.37% |     0.19 |       54 | 37.27%     | ok               |
|          30 | 3.48%    | 126.04%            | -22.01% |     0.18 |       70 | 48.92%     | ok               |
|          20 | 3.25%    | 126.04%            | -23.51% |     0.18 |       76 | 54.24%     | ok               |

## CL Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -1.87%   | -7.74%             | -12.98% |    -0.03 |       42 | 22.96%     | ok               |
|          30 | -5.50%   | -7.74%             | -14.32% |    -0.13 |       64 | 39.10%     | ok               |
|          45 | -7.56%   | -7.74%             | -13.51% |    -0.26 |       48 | 25.79%     | ok               |
|          35 | -9.27%   | -7.74%             | -15.34% |    -0.28 |       64 | 35.27%     | ok               |
|          15 | -13.98%  | -7.74%             | -18.95% |    -0.37 |       64 | 47.42%     | ok               |

## CMCSA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -16.51%  | -43.08%            | -28.41% |    -0.53 |       46 | 16.31%     | ok               |
|          45 | -23.29%  | -43.08%            | -35.13% |    -0.73 |       62 | 20.63%     | ok               |
|          15 | -35.27%  | -43.08%            | -46.99% |    -0.73 |       93 | 57.40%     | ok               |
|          30 | -34.85%  | -43.08%            | -46.39% |    -0.83 |       84 | 42.60%     | ok               |
|          40 | -31.13%  | -43.08%            | -42.51% |    -0.83 |       89 | 28.12%     | ok               |

## COMP-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 4.77%    | -39.57%            | -38.71% |     0.26 |       48 | 24.52%     | ok               |
|          30 | -35.33%  | -39.57%            | -55.77% |    -0.17 |       95 | 49.23%     | ok               |
|          25 | -40.74%  | -39.57%            | -54.62% |    -0.23 |       94 | 57.28%     | ok               |
|          15 | -47.04%  | -39.57%            | -54.29% |    -0.31 |       98 | 67.43%     | ok               |
|          40 | -43.07%  | -39.57%            | -53.14% |    -0.38 |       70 | 37.74%     | ok               |

## COP Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -10.92%  | 7.57%              | -34.61% |    -0.16 |       46 | 27.29%     | ok               |
|          35 | -14.48%  | 7.57%              | -42.05% |    -0.19 |       69 | 40.60%     | ok               |
|          30 | -16.32%  | 7.57%              | -41.35% |    -0.22 |       66 | 43.43%     | ok               |
|          45 | -17.92%  | 7.57%              | -41.10% |    -0.32 |       62 | 31.45%     | ok               |
|          25 | -27.95%  | 7.57%              | -47.42% |    -0.48 |       77 | 46.42%     | ok               |

## COST Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 11.84%   | 19.72%             | -24.32% |     0.41 |       62 | 47.25%     | ok               |
|          25 | 8.21%    | 19.72%             | -24.93% |     0.31 |       57 | 44.26%     | ok               |
|          35 | 3.82%    | 19.72%             | -29.78% |     0.19 |       56 | 39.10%     | ok               |
|          30 | -0.57%   | 19.72%             | -30.95% |     0.05 |       58 | 41.60%     | ok               |
|          15 | -3.32%   | 19.72%             | -27.30% |    -0.02 |       67 | 50.92%     | ok               |

## CRM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | -22.78%  | -21.90%            | -34.06% |    -0.28 |       62 | 41.26%     | ok               |
|          40 | -25.67%  | -21.90%            | -39.44% |    -0.37 |       68 | 37.10%     | ok               |
|          50 | -21.91%  | -21.90%            | -38.24% |    -0.4  |       56 | 24.79%     | ok               |
|          15 | -33.60%  | -21.90%            | -47.54% |    -0.41 |       88 | 57.57%     | ok               |
|          30 | -34.52%  | -21.90%            | -45.50% |    -0.51 |       65 | 45.92%     | ok               |

## CRV-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 61.29%   | -44.26%            | -37.78% |     0.72 |       66 | 33.14%     | ok               |
|          40 | 46.92%   | -44.26%            | -38.86% |     0.63 |       54 | 28.93%     | ok               |
|          45 | 36.80%   | -44.26%            | -42.29% |     0.56 |       54 | 22.22%     | ok               |
|          50 | 35.87%   | -44.26%            | -30.73% |     0.56 |       46 | 18.20%     | ok               |
|          30 | 25.99%   | -44.26%            | -39.89% |     0.47 |       68 | 37.93%     | ok               |

## CSCO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 35.47%   | 136.34%            | -19.34% |     0.73 |       50 | 37.44%     | ok               |
|          45 | 30.89%   | 136.34%            | -19.34% |     0.65 |       52 | 39.10%     | ok               |
|          25 | 25.94%   | 136.34%            | -23.28% |     0.53 |       61 | 49.92%     | ok               |
|          20 | 20.29%   | 136.34%            | -22.72% |     0.45 |       71 | 52.25%     | ok               |
|          30 | 19.32%   | 136.34%            | -21.79% |     0.44 |       64 | 48.59%     | ok               |

## CVX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -7.54%   | 25.82%             | -23.25% |    -0.11 |       73 | 45.26%     | ok               |
|          40 | -8.79%   | 25.82%             | -26.30% |    -0.18 |       71 | 36.61%     | ok               |
|          35 | -10.50%  | 25.82%             | -27.83% |    -0.21 |       69 | 39.10%     | ok               |
|          45 | -9.83%   | 25.82%             | -28.32% |    -0.22 |       63 | 33.11%     | ok               |
|          30 | -11.05%  | 25.82%             | -26.75% |    -0.22 |       69 | 42.26%     | ok               |

## DASH-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 156.61%  | 145.43%            | -33.55% |     1.01 |       38 | 18.01%     | ok               |
|          40 | 107.73%  | 145.43%            | -33.20% |     0.83 |       44 | 24.52%     | ok               |
|          45 | 78.66%   | 145.43%            | -37.63% |     0.72 |       44 | 20.69%     | ok               |
|          25 | -8.59%   | 145.43%            | -64.14% |     0.33 |       63 | 33.14%     | ok               |
|          30 | -9.06%   | 145.43%            | -64.43% |     0.33 |       57 | 30.84%     | ok               |

## DBC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -0.06%   | 38.87%             | -26.05% |     0.07 |       77 | 41.26%     | ok               |
|          20 | -4.46%   | 38.87%             | -25.69% |    -0.08 |       69 | 39.60%     | ok               |
|          25 | -5.25%   | 38.87%             | -24.84% |    -0.11 |       66 | 37.60%     | ok               |
|          50 | -5.52%   | 38.87%             | -18.84% |    -0.15 |       48 | 24.63%     | ok               |
|          35 | -7.73%   | 38.87%             | -23.19% |    -0.2  |       66 | 34.28%     | ok               |

## DE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 2.13%    | 58.66%             | -17.97% |     0.13 |       56 | 29.62%     | ok               |
|          45 | -4.48%   | 58.66%             | -19.53% |    -0.02 |       60 | 34.11%     | ok               |
|          20 | -7.80%   | 58.66%             | -24.11% |    -0.07 |       65 | 48.59%     | ok               |
|          25 | -12.03%  | 58.66%             | -24.29% |    -0.17 |       71 | 46.92%     | ok               |
|          30 | -12.17%  | 58.66%             | -23.98% |    -0.18 |       70 | 44.26%     | ok               |

## DIA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -5.66%   | 27.99%             | -11.17% |    -0.27 |       56 | 45.26%     | ok               |
|          35 | -6.51%   | 27.99%             | -13.15% |    -0.34 |       66 | 40.93%     | ok               |
|          30 | -7.92%   | 27.99%             | -12.94% |    -0.41 |       64 | 43.93%     | ok               |
|          20 | -8.38%   | 27.99%             | -13.60% |    -0.41 |       62 | 47.25%     | ok               |
|          40 | -9.61%   | 27.99%             | -15.06% |    -0.55 |       70 | 37.94%     | ok               |

## DIS Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 34.04%   | 1.93%              | -10.17% |     1.06 |       44 | 25.12%     | ok               |
|          40 | 5.30%    | 1.93%              | -18.75% |     0.21 |       61 | 33.94%     | ok               |
|          45 | 2.94%    | 1.93%              | -16.54% |     0.16 |       45 | 28.95%     | ok               |
|          15 | -4.47%   | 1.93%              | -31.15% |     0.02 |       85 | 54.74%     | ok               |
|          35 | -5.94%   | 1.93%              | -25.70% |    -0.05 |       75 | 40.10%     | ok               |

## DOGE-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -3.01%   | -48.87%            | -57.89% |     0.25 |       74 | 64.18%     | ok               |
|          20 | -7.26%   | -48.87%            | -55.83% |     0.2  |       74 | 58.81%     | ok               |
|          25 | -13.18%  | -48.87%            | -53.72% |     0.13 |       66 | 54.79%     | ok               |
|          30 | -31.92%  | -48.87%            | -60.95% |    -0.12 |       69 | 48.47%     | ok               |
|          50 | -32.68%  | -48.87%            | -52.88% |    -0.29 |       62 | 24.90%     | ok               |

## DOT-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -56.21%  | -71.95%            | -72.06% |    -0.37 |       77 | 64.18%     | ok               |
|          20 | -53.18%  | -71.95%            | -66.32% |    -0.39 |       89 | 60.15%     | ok               |
|          30 | -58.07%  | -71.95%            | -63.33% |    -0.55 |       88 | 49.04%     | ok               |
|          25 | -60.40%  | -71.95%            | -69.99% |    -0.56 |       80 | 55.17%     | ok               |
|          35 | -61.72%  | -71.95%            | -63.01% |    -0.67 |       86 | 43.30%     | ok               |

## DXY-INDEX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd    |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:-------|---------:|---------:|:-----------|:-----------------|
|          50 | -0.52%   | -3.46%             | -6.02% |    -0.07 |       40 | 31.17%     | ok               |
|          40 | -1.42%   | -3.46%             | -7.30% |    -0.17 |       66 | 46.97%     | ok               |
|          45 | -1.88%   | -3.46%             | -8.14% |    -0.25 |       60 | 37.23%     | ok               |
|          30 | -4.03%   | -3.46%             | -9.83% |    -0.47 |       74 | 57.36%     | ok               |
|          35 | -4.19%   | -3.46%             | -9.97% |    -0.52 |       77 | 52.38%     | ok               |

## EEM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -7.81%   | 54.84%             | -15.62% |    -0.23 |       54 | 33.11%     | ok               |
|          45 | -8.14%   | 54.84%             | -16.78% |    -0.24 |       52 | 34.61%     | ok               |
|          40 | -8.48%   | 54.84%             | -18.95% |    -0.24 |       64 | 36.77%     | ok               |
|          35 | -9.39%   | 54.84%             | -23.57% |    -0.25 |       66 | 38.94%     | ok               |
|          30 | -12.61%  | 54.84%             | -25.38% |    -0.36 |       62 | 40.77%     | ok               |

## EFA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -3.38%   | 26.04%             | -10.10% |    -0.06 |       62 | 51.75%     | ok               |
|          20 | -10.97%  | 26.04%             | -13.36% |    -0.39 |       71 | 48.75%     | ok               |
|          25 | -11.80%  | 26.04%             | -14.11% |    -0.44 |       64 | 45.59%     | ok               |
|          30 | -11.65%  | 26.04%             | -12.84% |    -0.45 |       64 | 42.93%     | ok               |
|          35 | -13.10%  | 26.04%             | -14.16% |    -0.52 |       58 | 41.43%     | ok               |

## EOG Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -15.79%  | 11.71%             | -34.41% |    -0.32 |       50 | 30.28%     | ok               |
|          40 | -23.34%  | 11.71%             | -36.53% |    -0.53 |       70 | 34.28%     | ok               |
|          50 | -22.04%  | 11.71%             | -35.63% |    -0.53 |       50 | 27.45%     | ok               |
|          35 | -27.36%  | 11.71%             | -40.63% |    -0.62 |       83 | 39.27%     | ok               |
|          30 | -29.89%  | 11.71%             | -47.50% |    -0.64 |       78 | 44.43%     | ok               |

## ETC-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -5.47%   | -47.91%            | -38.47% |     0.05 |       28 | 20.50%     | ok               |
|          50 | -4.94%   | -47.91%            | -31.28% |     0.05 |       28 | 18.20%     | ok               |
|          40 | -17.03%  | -47.91%            | -43.28% |    -0.15 |       38 | 23.56%     | ok               |
|          35 | -19.28%  | -47.91%            | -45.32% |    -0.16 |       42 | 27.01%     | ok               |
|          30 | -22.45%  | -47.91%            | -48.09% |    -0.2  |       56 | 30.65%     | ok               |

## ETH-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 178.93%  | 41.10%             | -30.11% |     1.44 |       58 | 48.85%     | ok               |
|          30 | 135.30%  | 41.10%             | -32.89% |     1.19 |       60 | 56.51%     | ok               |
|          25 | 92.62%   | 41.10%             | -40.90% |     0.95 |       60 | 60.34%     | ok               |
|          20 | 75.48%   | 41.10%             | -39.10% |     0.83 |       78 | 64.18%     | ok               |
|          40 | 60.51%   | 41.10%             | -33.11% |     0.81 |       62 | 40.80%     | ok               |

## EWJ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -22.99%  | 42.55%             | -29.40% |    -0.8  |       62 | 36.44%     | ok               |
|          20 | -23.95%  | 42.55%             | -30.00% |    -0.81 |       56 | 38.44%     | ok               |
|          45 | -21.95%  | 42.55%             | -25.77% |    -0.87 |       58 | 28.79%     | ok               |
|          25 | -25.82%  | 42.55%             | -29.85% |    -0.9  |       56 | 37.60%     | ok               |
|          15 | -27.60%  | 42.55%             | -31.15% |    -0.9  |       67 | 41.76%     | ok               |

## FCX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 2.51%    | 34.04%             | -29.27% |     0.18 |       50 | 31.61%     | ok               |
|          50 | -0.09%   | 34.04%             | -26.57% |     0.13 |       52 | 27.95%     | ok               |
|          40 | -10.00%  | 34.04%             | -42.89% |    -0.01 |       62 | 36.94%     | ok               |
|          30 | -29.37%  | 34.04%             | -46.84% |    -0.32 |       65 | 44.26%     | ok               |
|          35 | -29.20%  | 34.04%             | -50.12% |    -0.34 |       67 | 42.10%     | ok               |

## FET-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -21.41%  | -65.02%            | -64.89% |     0.09 |       88 | 51.92%     | ok               |
|          15 | -23.47%  | -65.02%            | -59.58% |     0.09 |       82 | 56.51%     | ok               |
|          25 | -26.76%  | -65.02%            | -65.31% |     0.02 |       79 | 46.17%     | ok               |
|          30 | -40.68%  | -65.02%            | -60.12% |    -0.21 |       77 | 41.76%     | ok               |
|          50 | -39.06%  | -65.02%            | -45.19% |    -0.53 |       46 | 14.37%     | ok               |

## FIL-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -42.89%  | -59.69%            | -57.60% |    -0.5  |       50 | 26.05%     | ok               |
|          30 | -48.57%  | -59.69%            | -58.54% |    -0.52 |       65 | 36.59%     | ok               |
|          35 | -52.02%  | -59.69%            | -61.90% |    -0.66 |       60 | 30.46%     | ok               |
|          15 | -64.23%  | -59.69%            | -71.82% |    -0.73 |       91 | 48.47%     | ok               |
|          50 | -46.43%  | -59.69%            | -47.18% |    -0.74 |       38 | 15.52%     | ok               |

## FXI Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -7.38%   | 17.97%             | -22.99% |    -0.1  |       52 | 33.44%     | ok               |
|          15 | -8.23%   | 17.97%             | -21.68% |    -0.11 |       54 | 37.44%     | ok               |
|          30 | -7.64%   | 17.97%             | -24.33% |    -0.11 |       50 | 31.95%     | ok               |
|          20 | -10.91%  | 17.97%             | -24.94% |    -0.19 |       54 | 35.27%     | ok               |
|          35 | -11.21%  | 17.97%             | -27.93% |    -0.22 |       52 | 29.45%     | ok               |

## GDX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 4.31%    | 137.98%            | -33.01% |     0.21 |       76 | 49.58%     | ok               |
|          40 | 4.34%    | 137.98%            | -28.47% |     0.2  |       58 | 38.27%     | ok               |
|          35 | -1.69%   | 137.98%            | -31.73% |     0.1  |       66 | 40.93%     | ok               |
|          30 | -2.33%   | 137.98%            | -33.31% |     0.1  |       58 | 44.26%     | ok               |
|          25 | -8.41%   | 137.98%            | -38.90% |     0.01 |       64 | 45.59%     | ok               |

## GDXJ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -25.32%  | 145.81%            | -42.33% |    -0.2  |       74 | 49.58%     | ok               |
|          50 | -25.39%  | 145.81%            | -46.83% |    -0.33 |       56 | 34.11%     | ok               |
|          35 | -34.57%  | 145.81%            | -38.56% |    -0.46 |       68 | 39.93%     | ok               |
|          30 | -36.38%  | 145.81%            | -41.57% |    -0.48 |       68 | 42.60%     | ok               |
|          40 | -35.79%  | 145.81%            | -44.70% |    -0.52 |       62 | 37.60%     | ok               |

## GE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 4.89%    | 85.73%             | -21.25% |     0.2  |       60 | 33.78%     | ok               |
|          45 | -3.80%   | 85.73%             | -21.88% |     0.02 |       72 | 36.61%     | ok               |
|          30 | -9.80%   | 85.73%             | -27.82% |    -0.07 |       78 | 48.25%     | ok               |
|          20 | -10.40%  | 85.73%             | -25.05% |    -0.07 |       73 | 52.75%     | ok               |
|          25 | -10.91%  | 85.73%             | -29.91% |    -0.09 |       74 | 50.25%     | ok               |

## GLD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | 16.36%   | 70.17%             | -13.87% |     0.45 |       48 | 46.42%     | ok               |
|          20 | 14.78%   | 70.17%             | -13.87% |     0.42 |       49 | 48.09%     | ok               |
|          30 | 10.82%   | 70.17%             | -13.87% |     0.34 |       50 | 45.26%     | ok               |
|          35 | 7.88%    | 70.17%             | -14.65% |     0.27 |       52 | 42.93%     | ok               |
|          15 | 4.23%    | 70.17%             | -17.63% |     0.19 |       57 | 51.41%     | ok               |

## GOOGL Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 61.24%   | 103.18%            | -17.38% |     1.08 |       59 | 43.76%     | ok               |
|          30 | 57.34%   | 103.18%            | -17.54% |     1.01 |       57 | 47.25%     | ok               |
|          45 | 49.77%   | 103.18%            | -11.66% |     1    |       52 | 37.27%     | ok               |
|          25 | 54.94%   | 103.18%            | -16.87% |     0.97 |       57 | 49.75%     | ok               |
|          50 | 45.36%   | 103.18%            | -11.52% |     0.96 |       44 | 32.45%     | ok               |

## GRT-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 64.54%   | -70.35%            | -42.58% |     0.7  |       70 | 62.45%     | ok               |
|          20 | 47.74%   | -70.35%            | -40.19% |     0.61 |       77 | 56.90%     | ok               |
|          50 | 33.06%   | -70.35%            | -30.80% |     0.55 |       44 | 21.07%     | ok               |
|          45 | 33.45%   | -70.35%            | -44.68% |     0.54 |       46 | 27.97%     | ok               |
|          25 | 27.65%   | -70.35%            | -45.66% |     0.48 |       78 | 52.30%     | ok               |

## GS Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 21.56%   | 90.35%             | -20.56% |     0.48 |       68 | 56.41%     | ok               |
|          20 | 2.88%    | 90.35%             | -23.19% |     0.16 |       68 | 53.08%     | ok               |
|          40 | 1.75%    | 90.35%             | -17.88% |     0.13 |       68 | 42.43%     | ok               |
|          25 | -2.33%   | 90.35%             | -23.32% |     0.05 |       68 | 50.58%     | ok               |
|          30 | -4.46%   | 90.35%             | -22.13% |     0    |       70 | 48.09%     | ok               |

## HBAR-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -18.60%  | -10.25%            | -39.26% |    -0.27 |       18 | 18.29%     | ok               |
|          45 | -33.67%  | -10.25%            | -48.27% |    -0.7  |       22 | 24.51%     | ok               |
|          40 | -36.66%  | -10.25%            | -50.61% |    -0.78 |       26 | 29.18%     | ok               |
|          15 | -43.30%  | -10.25%            | -55.78% |    -0.92 |       51 | 50.97%     | ok               |
|          30 | -44.08%  | -10.25%            | -56.39% |    -0.99 |       38 | 37.74%     | ok               |

## HD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 3.78%    | -18.04%            | -17.15% |     0.18 |       69 | 43.09%     | ok               |
|          25 | 1.16%    | -18.04%            | -18.88% |     0.11 |       68 | 45.26%     | ok               |
|          35 | -0.57%   | -18.04%            | -18.52% |     0.06 |       72 | 39.43%     | ok               |
|          40 | -2.26%   | -18.04%            | -18.05% |     0    |       76 | 34.94%     | ok               |
|          45 | -3.05%   | -18.04%            | -18.71% |    -0.03 |       52 | 30.12%     | ok               |

## HON Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -12.15%  | 2.67%              | -21.17% |    -0.31 |       70 | 33.78%     | ok               |
|          45 | -15.82%  | 2.67%              | -22.88% |    -0.41 |       72 | 39.27%     | ok               |
|          35 | -25.64%  | 2.67%              | -31.30% |    -0.66 |       89 | 50.58%     | ok               |
|          30 | -27.58%  | 2.67%              | -33.03% |    -0.69 |       89 | 55.24%     | ok               |
|          40 | -25.95%  | 2.67%              | -31.84% |    -0.7  |       76 | 43.59%     | ok               |

## HYG Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -5.26%   | -0.35%             | -7.94%  |    -0.61 |       70 | 33.11%     | ok               |
|          45 | -6.44%   | -0.35%             | -9.08%  |    -0.78 |       70 | 29.78%     | ok               |
|          35 | -7.07%   | -0.35%             | -9.70%  |    -0.82 |       79 | 34.78%     | ok               |
|          30 | -7.29%   | -0.35%             | -10.59% |    -0.82 |       87 | 38.10%     | ok               |
|          15 | -7.95%   | -0.35%             | -11.21% |    -0.84 |       92 | 45.59%     | ok               |

## IBIT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 55.51%   | 24.20%             | -17.37% |     0.98 |       26 | 25.61%     | ok               |
|          15 | 68.43%   | 24.20%             | -19.20% |     0.98 |       44 | 41.39%     | ok               |
|          45 | 45.94%   | 24.20%             | -17.37% |     0.84 |       30 | 26.84%     | ok               |
|          40 | 39.41%   | 24.20%             | -17.78% |     0.75 |       30 | 28.69%     | ok               |
|          30 | 40.42%   | 24.20%             | -18.95% |     0.73 |       38 | 34.63%     | ok               |

## IBM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -17.64%  | 31.05%             | -49.43% |    -0.11 |       83 | 61.56%     | ok               |
|          35 | -21.42%  | 31.05%             | -47.10% |    -0.23 |       63 | 45.92%     | ok               |
|          30 | -24.27%  | 31.05%             | -48.94% |    -0.28 |       69 | 49.92%     | ok               |
|          20 | -29.45%  | 31.05%             | -53.45% |    -0.35 |       69 | 54.58%     | ok               |
|          45 | -28.12%  | 31.05%             | -48.72% |    -0.4  |       52 | 37.44%     | ok               |

## ICP-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 8.32%    | -30.82%            | -46.78% |     0.3  |       68 | 33.33%     | ok               |
|          40 | 7.56%    | -30.82%            | -40.71% |     0.29 |       60 | 28.54%     | ok               |
|          30 | 0.63%    | -30.82%            | -46.42% |     0.26 |       77 | 39.27%     | ok               |
|          50 | -11.77%  | -30.82%            | -50.31% |     0.02 |       42 | 18.39%     | ok               |
|          15 | -31.63%  | -30.82%            | -58.26% |     0.02 |       77 | 50.19%     | ok               |

## IEF Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -6.41%   | -4.78%             | -10.18% |    -0.75 |       72 | 42.26%     | ok               |
|          15 | -6.96%   | -4.78%             | -10.91% |    -0.81 |       71 | 43.76%     | ok               |
|          50 | -7.10%   | -4.78%             | -9.11%  |    -1.19 |       58 | 22.46%     | ok               |
|          40 | -8.42%   | -4.78%             | -11.24% |    -1.22 |       64 | 27.62%     | ok               |
|          25 | -9.98%   | -4.78%             | -11.95% |    -1.26 |       76 | 39.60%     | ok               |

## IEMG Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -3.66%   | 50.39%             | -14.22% |    -0.09 |       54 | 32.11%     | ok               |
|          45 | -4.00%   | 50.39%             | -14.84% |    -0.1  |       50 | 34.44%     | ok               |
|          40 | -5.48%   | 50.39%             | -18.35% |    -0.15 |       62 | 37.44%     | ok               |
|          35 | -7.92%   | 50.39%             | -24.56% |    -0.22 |       67 | 39.93%     | ok               |
|          30 | -13.09%  | 50.39%             | -29.43% |    -0.4  |       62 | 41.26%     | ok               |

## INJ-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 7.83%    | -21.34%            | -54.34% |     0.32 |       58 | 36.40%     | ok               |
|          40 | -0.33%   | -21.34%            | -49.75% |     0.23 |       50 | 33.33%     | ok               |
|          45 | -6.35%   | -21.34%            | -47.58% |     0.15 |       54 | 27.59%     | ok               |
|          15 | -28.41%  | -21.34%            | -75.74% |     0.03 |       74 | 51.53%     | ok               |
|          20 | -26.64%  | -21.34%            | -76.59% |     0.02 |       72 | 48.28%     | ok               |

## INTC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 70.01%   | 261.75%            | -49.32% |     0.71 |       56 | 33.78%     | ok               |
|          50 | 64.73%   | 261.75%            | -48.35% |     0.68 |       60 | 29.95%     | ok               |
|          15 | 67.73%   | 261.75%            | -53.65% |     0.66 |       80 | 59.90%     | ok               |
|          40 | 60.00%   | 261.75%            | -55.86% |     0.64 |       62 | 37.77%     | ok               |
|          25 | 50.93%   | 261.75%            | -56.41% |     0.59 |       79 | 50.75%     | ok               |

## INTU Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 10.45%   | -54.63%            | -34.58% |     0.3  |       67 | 29.12%     | ok               |
|          45 | -0.12%   | -54.63%            | -39.62% |     0.12 |       65 | 33.11%     | ok               |
|          40 | -4.58%   | -54.63%            | -41.86% |     0.04 |       67 | 37.10%     | ok               |
|          25 | -6.69%   | -54.63%            | -35.05% |     0.03 |       70 | 49.42%     | ok               |
|          30 | -11.45%  | -54.63%            | -37.50% |    -0.05 |       73 | 46.76%     | ok               |

## ITA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 0.82%    | 51.53%             | -27.64% |     0.11 |       83 | 60.73%     | ok               |
|          50 | -0.76%   | 51.53%             | -21.48% |     0.04 |       76 | 37.77%     | ok               |
|          30 | -1.89%   | 51.53%             | -23.75% |     0.03 |       72 | 48.92%     | ok               |
|          20 | -5.62%   | 51.53%             | -27.64% |    -0.07 |       84 | 54.74%     | ok               |
|          35 | -5.78%   | 51.53%             | -23.16% |    -0.1  |       76 | 46.09%     | ok               |

## IWM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | 10.02%   | 32.59%             | -11.96% |     0.41 |       52 | 35.61%     | ok               |
|          20 | 8.56%    | 32.59%             | -11.74% |     0.35 |       58 | 36.61%     | ok               |
|          30 | 6.34%    | 32.59%             | -12.28% |     0.29 |       54 | 34.94%     | ok               |
|          40 | 5.41%    | 32.59%             | -13.56% |     0.27 |       46 | 30.28%     | ok               |
|          15 | 5.23%    | 32.59%             | -13.42% |     0.24 |       76 | 42.43%     | ok               |

## JNJ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 17.23%   | 69.29%             | -10.57% |     0.7  |       42 | 34.94%     | ok               |
|          15 | 12.33%   | 69.29%             | -17.37% |     0.45 |       60 | 53.91%     | ok               |
|          20 | 7.14%    | 69.29%             | -16.96% |     0.3  |       66 | 50.42%     | ok               |
|          45 | 5.96%    | 69.29%             | -13.35% |     0.28 |       48 | 38.94%     | ok               |
|          30 | 5.87%    | 69.29%             | -16.86% |     0.26 |       64 | 47.09%     | ok               |

## JPM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 2.70%    | 63.07%             | -15.90% |     0.15 |       50 | 33.78%     | ok               |
|          45 | -7.54%   | 63.07%             | -21.91% |    -0.17 |       54 | 36.44%     | ok               |
|          20 | -22.51%  | 63.07%             | -35.58% |    -0.49 |       86 | 49.92%     | ok               |
|          35 | -19.58%  | 63.07%             | -27.43% |    -0.55 |       74 | 42.26%     | ok               |
|          40 | -20.23%  | 63.07%             | -28.47% |    -0.58 |       66 | 39.10%     | ok               |

## KO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 22.97%   | 35.94%             | -8.64%  |     0.82 |       54 | 37.60%     | ok               |
|          35 | 18.79%   | 35.94%             | -8.21%  |     0.7  |       58 | 36.11%     | ok               |
|          40 | 15.93%   | 35.94%             | -9.28%  |     0.64 |       60 | 32.78%     | ok               |
|          25 | 16.81%   | 35.94%             | -10.16% |     0.62 |       60 | 40.43%     | ok               |
|          20 | 3.92%    | 35.94%             | -15.99% |     0.19 |       77 | 44.59%     | ok               |

## LDO-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 48.36%   | -42.31%            | -39.99% |     0.61 |       78 | 60.15%     | ok               |
|          20 | 34.97%   | -42.31%            | -43.25% |     0.54 |       80 | 55.36%     | ok               |
|          30 | 10.52%   | -42.31%            | -59.24% |     0.37 |       72 | 46.93%     | ok               |
|          25 | 5.26%    | -42.31%            | -55.04% |     0.34 |       81 | 52.49%     | ok               |
|          35 | -7.24%   | -42.31%            | -61.97% |     0.19 |       78 | 39.46%     | ok               |

## LIN Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -8.81%   | 12.34%             | -22.01% |    -0.25 |       71 | 40.77%     | ok               |
|          20 | -9.56%   | 12.34%             | -23.00% |    -0.27 |       68 | 43.76%     | ok               |
|          15 | -10.17%  | 12.34%             | -23.68% |    -0.29 |       72 | 47.59%     | ok               |
|          30 | -11.85%  | 12.34%             | -20.61% |    -0.38 |       72 | 37.94%     | ok               |
|          35 | -12.82%  | 12.34%             | -19.70% |    -0.45 |       74 | 31.28%     | ok               |

## LINK-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 31.69%   | -3.55%             | -33.71% |     0.53 |       54 | 32.76%     | ok               |
|          30 | 31.57%   | -3.55%             | -33.64% |     0.52 |       69 | 46.55%     | ok               |
|          35 | 10.09%   | -3.55%             | -34.21% |     0.33 |       63 | 42.53%     | ok               |
|          50 | 10.71%   | -3.55%             | -27.92% |     0.32 |       48 | 26.82%     | ok               |
|          40 | 2.97%    | -3.55%             | -34.00% |     0.24 |       59 | 36.97%     | ok               |

## LLY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -2.11%   | 51.04%             | -38.23% |     0.07 |       48 | 35.44%     | ok               |
|          15 | -14.25%  | 51.04%             | -48.12% |    -0.09 |       70 | 60.40%     | ok               |
|          45 | -14.88%  | 51.04%             | -42.66% |    -0.19 |       56 | 38.94%     | ok               |
|          20 | -27.92%  | 51.04%             | -51.34% |    -0.38 |       75 | 55.41%     | ok               |
|          40 | -25.69%  | 51.04%             | -46.23% |    -0.4  |       66 | 41.93%     | ok               |

## LRCX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -6.31%   | 247.68%            | -47.56% |     0.1  |       66 | 39.60%     | ok               |
|          50 | -6.19%   | 247.68%            | -42.40% |     0.08 |       72 | 33.44%     | ok               |
|          45 | -14.87%  | 247.68%            | -47.62% |    -0.02 |       72 | 37.10%     | ok               |
|          35 | -18.18%  | 247.68%            | -56.59% |    -0.05 |       76 | 41.93%     | ok               |
|          30 | -22.56%  | 247.68%            | -58.79% |    -0.11 |       78 | 42.43%     | ok               |

## LTC-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 19.88%   | -22.49%            | -36.44% |     0.43 |       56 | 36.97%     | ok               |
|          35 | 19.74%   | -22.49%            | -34.94% |     0.42 |       66 | 46.55%     | ok               |
|          30 | 15.32%   | -22.49%            | -32.66% |     0.37 |       67 | 53.83%     | ok               |
|          25 | 11.18%   | -22.49%            | -34.22% |     0.33 |       69 | 56.13%     | ok               |
|          15 | -2.33%   | -22.49%            | -46.99% |     0.19 |       79 | 64.37%     | ok               |

## MCD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 13.53%   | -15.70%            | -9.22%  |     0.62 |       46 | 24.96%     | ok               |
|          45 | 4.00%    | -15.70%            | -16.79% |     0.22 |       52 | 28.79%     | ok               |
|          40 | 2.62%    | -15.70%            | -18.49% |     0.16 |       67 | 32.11%     | ok               |
|          30 | 2.11%    | -15.70%            | -21.88% |     0.13 |       77 | 40.10%     | ok               |
|          25 | 1.55%    | -15.70%            | -23.62% |     0.11 |       75 | 42.43%     | ok               |

## META Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -10.27%  | 49.79%             | -37.10% |    -0.07 |       66 | 39.77%     | ok               |
|          40 | -15.54%  | 49.79%             | -40.49% |    -0.16 |       70 | 43.26%     | ok               |
|          50 | -19.91%  | 49.79%             | -38.63% |    -0.29 |       68 | 35.44%     | ok               |
|          35 | -26.14%  | 49.79%             | -40.80% |    -0.37 |       83 | 48.09%     | ok               |
|          25 | -28.07%  | 49.79%             | -45.35% |    -0.39 |       77 | 53.24%     | ok               |

## MPC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 34.68%   | 156.16%            | -18.24% |     0.67 |       50 | 40.10%     | ok               |
|          40 | 32.46%   | 156.16%            | -20.11% |     0.61 |       60 | 46.76%     | ok               |
|          45 | 30.14%   | 156.16%            | -19.46% |     0.59 |       56 | 44.09%     | ok               |
|          35 | 29.47%   | 156.16%            | -31.08% |     0.56 |       68 | 49.42%     | ok               |
|          30 | 15.43%   | 156.16%            | -37.91% |     0.36 |       71 | 52.08%     | ok               |

## MRK Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -13.70%  | 8.40%              | -28.41% |    -0.17 |       85 | 52.08%     | ok               |
|          25 | -15.00%  | 8.40%              | -31.07% |    -0.22 |       72 | 44.43%     | ok               |
|          50 | -15.14%  | 8.40%              | -23.03% |    -0.31 |       58 | 28.62%     | ok               |
|          20 | -19.16%  | 8.40%              | -29.34% |    -0.32 |       77 | 47.75%     | ok               |
|          45 | -17.25%  | 8.40%              | -25.38% |    -0.35 |       59 | 31.95%     | ok               |

## MS Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 0.92%    | 88.73%             | -19.99% |     0.1  |       72 | 39.60%     | ok               |
|          15 | -2.94%   | 88.73%             | -22.02% |     0.03 |       74 | 58.24%     | ok               |
|          20 | -5.24%   | 88.73%             | -25.68% |    -0.03 |       75 | 53.08%     | ok               |
|          30 | -10.16%  | 88.73%             | -27.79% |    -0.17 |       75 | 48.25%     | ok               |
|          35 | -10.09%  | 88.73%             | -26.58% |    -0.18 |       76 | 44.76%     | ok               |

## MSFT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -15.21%  | 25.22%             | -25.54% |    -0.35 |       76 | 37.10%     | ok               |
|          50 | -20.18%  | 25.22%             | -26.37% |    -0.53 |       66 | 31.45%     | ok               |
|          30 | -25.31%  | 25.22%             | -38.06% |    -0.54 |       83 | 50.58%     | ok               |
|          35 | -24.41%  | 25.22%             | -36.28% |    -0.54 |       77 | 46.26%     | ok               |
|          25 | -26.52%  | 25.22%             | -39.13% |    -0.57 |       87 | 53.58%     | ok               |

## MU Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 179.93%  | 751.26%            | -63.96% |     1.14 |       58 | 48.59%     | ok               |
|          15 | 204.26%  | 751.26%            | -61.96% |     1.12 |       51 | 60.23%     | ok               |
|          30 | 151.83%  | 751.26%            | -68.76% |     1.04 |       51 | 53.24%     | ok               |
|          25 | 150.35%  | 751.26%            | -67.90% |     1.02 |       51 | 54.74%     | ok               |
|          35 | 144.86%  | 751.26%            | -69.09% |     1.02 |       63 | 50.92%     | ok               |

## NEAR-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 216.64%  | 133.46%            | -51.95% |     1.31 |       42 | 31.61%     | ok               |
|          45 | 160.80%  | 133.46%            | -45.21% |     1.14 |       44 | 27.39%     | ok               |
|          35 | 154.52%  | 133.46%            | -56.52% |     1.1  |       64 | 36.21%     | ok               |
|          50 | 131.01%  | 133.46%            | -50.61% |     1.05 |       30 | 22.03%     | ok               |
|          30 | 139.67%  | 133.46%            | -52.25% |     1.02 |       73 | 44.25%     | ok               |

## NEM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 5.39%    | 162.88%            | -31.25% |     0.24 |       62 | 58.57%     | ok               |
|          20 | 1.97%    | 162.88%            | -30.50% |     0.19 |       68 | 54.24%     | ok               |
|          25 | -15.67%  | 162.88%            | -39.51% |    -0.07 |       62 | 52.08%     | ok               |
|          50 | -19.26%  | 162.88%            | -33.24% |    -0.17 |       54 | 38.77%     | ok               |
|          30 | -26.24%  | 162.88%            | -39.56% |    -0.25 |       66 | 50.42%     | ok               |

## NFLX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 36.76%   | 13.61%             | -16.28% |     0.89 |       44 | 34.11%     | ok               |
|          40 | 35.65%   | 13.61%             | -14.99% |     0.81 |       50 | 42.10%     | ok               |
|          35 | 34.64%   | 13.61%             | -18.30% |     0.75 |       74 | 46.59%     | ok               |
|          45 | 23.46%   | 13.61%             | -15.48% |     0.6  |       56 | 38.60%     | ok               |
|          15 | 18.31%   | 13.61%             | -26.59% |     0.42 |       71 | 65.06%     | ok               |

## NKE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -17.04%  | -62.52%            | -49.34% |    -0.11 |       83 | 53.08%     | ok               |
|          35 | -15.25%  | -62.52%            | -42.13% |    -0.13 |       71 | 40.27%     | ok               |
|          25 | -20.48%  | -62.52%            | -51.20% |    -0.17 |       83 | 50.42%     | ok               |
|          15 | -22.39%  | -62.52%            | -54.28% |    -0.19 |       86 | 56.91%     | ok               |
|          30 | -24.27%  | -62.52%            | -55.35% |    -0.24 |       79 | 46.42%     | ok               |

## NOW Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 10.56%   | -9.36%             | -30.43% |     0.3  |       82 | 50.42%     | ok               |
|          20 | 8.55%    | -9.36%             | -39.71% |     0.28 |       76 | 56.57%     | ok               |
|          25 | 5.35%    | -9.36%             | -37.51% |     0.24 |       74 | 53.91%     | ok               |
|          15 | 3.06%    | -9.36%             | -43.06% |     0.22 |       84 | 59.57%     | ok               |
|          40 | -2.21%   | -9.36%             | -36.21% |     0.12 |       74 | 40.10%     | ok               |

## NVDA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -30.75%  | 84.89%             | -41.21% |    -0.42 |       74 | 43.49%     | ok               |
|          20 | -39.96%  | 84.89%             | -42.84% |    -0.53 |       74 | 51.52%     | ok               |
|          25 | -39.86%  | 84.89%             | -42.74% |    -0.58 |       75 | 46.52%     | ok               |
|          15 | -46.46%  | 84.89%             | -52.37% |    -0.63 |       75 | 54.72%     | ok               |
|          35 | -41.17%  | 84.89%             | -48.32% |    -0.7  |       84 | 40.64%     | ok               |

## OP-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 14.03%   | -81.24%            | -31.68% |     0.36 |       32 | 9.77%      | ok               |
|          45 | 10.34%   | -81.24%            | -43.25% |     0.31 |       34 | 14.37%     | ok               |
|          40 | -13.53%  | -81.24%            | -53.61% |     0.03 |       46 | 22.61%     | ok               |
|          35 | -35.14%  | -81.24%            | -58.13% |    -0.28 |       56 | 27.39%     | ok               |
|          30 | -40.82%  | -81.24%            | -68.74% |    -0.3  |       68 | 33.52%     | ok               |

## ORCL Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 170.96%  | 18.03%             | -32.54% |     1.13 |       69 | 62.56%     | ok               |
|          25 | 117.86%  | 18.03%             | -27.76% |     0.94 |       61 | 55.07%     | ok               |
|          45 | 102.53%  | 18.03%             | -32.35% |     0.93 |       58 | 40.60%     | ok               |
|          35 | 107.54%  | 18.03%             | -31.95% |     0.92 |       62 | 49.25%     | ok               |
|          20 | 111.78%  | 18.03%             | -29.32% |     0.91 |       70 | 58.24%     | ok               |

## OXY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -0.67%   | -8.16%             | -28.48% |     0.11 |       69 | 42.26%     | ok               |
|          35 | -1.86%   | -8.16%             | -26.37% |     0.08 |       72 | 37.94%     | ok               |
|          50 | -5.50%   | -8.16%             | -27.38% |    -0.01 |       44 | 26.79%     | ok               |
|          40 | -7.91%   | -8.16%             | -28.30% |    -0.04 |       62 | 33.78%     | ok               |
|          25 | -14.41%  | -8.16%             | -38.51% |    -0.13 |       77 | 45.76%     | ok               |

## PEP Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 20.61%   | -31.05%            | -11.62% |     0.86 |       40 | 25.62%     | ok               |
|          45 | 12.90%   | -31.05%            | -14.22% |     0.55 |       56 | 29.62%     | ok               |
|          35 | 8.95%    | -31.05%            | -21.42% |     0.34 |       77 | 39.93%     | ok               |
|          40 | 6.60%    | -31.05%            | -18.04% |     0.29 |       70 | 35.27%     | ok               |
|          30 | 4.13%    | -31.05%            | -21.35% |     0.19 |       74 | 45.92%     | ok               |

## PEPE-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -45.82%  | -49.18%            | -61.29% |    -0.24 |       85 | 49.43%     | ok               |
|          25 | -49.06%  | -49.18%            | -61.43% |    -0.28 |       93 | 54.21%     | ok               |
|          15 | -57.13%  | -49.18%            | -65.60% |    -0.29 |       82 | 63.41%     | ok               |
|          20 | -55.41%  | -49.18%            | -64.22% |    -0.33 |       88 | 59.96%     | ok               |
|          35 | -47.65%  | -49.18%            | -61.54% |    -0.35 |       74 | 44.44%     | ok               |

## PFE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -15.89%  | -2.85%             | -23.37% |    -0.5  |       52 | 21.63%     | ok               |
|          40 | -17.46%  | -2.85%             | -27.08% |    -0.53 |       72 | 26.62%     | ok               |
|          50 | -16.36%  | -2.85%             | -25.42% |    -0.57 |       40 | 18.47%     | ok               |
|          35 | -25.20%  | -2.85%             | -32.87% |    -0.78 |       84 | 33.28%     | ok               |
|          30 | -34.82%  | -2.85%             | -41.90% |    -1.07 |       81 | 37.44%     | ok               |

## PG Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -10.31%  | -11.22%            | -17.50% |    -0.41 |       54 | 28.45%     | ok               |
|          35 | -15.65%  | -11.22%            | -18.57% |    -0.62 |       62 | 32.11%     | ok               |
|          45 | -19.48%  | -11.22%            | -20.34% |    -0.9  |       54 | 25.79%     | ok               |
|          30 | -23.31%  | -11.22%            | -24.16% |    -0.94 |       64 | 35.27%     | ok               |
|          25 | -25.06%  | -11.22%            | -25.86% |    -1.01 |       76 | 36.77%     | ok               |

## PM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | -5.07%   | 91.60%             | -32.20% |    -0.03 |       84 | 47.42%     | ok               |
|          20 | -7.55%   | 91.60%             | -33.51% |    -0.07 |       83 | 56.07%     | ok               |
|          30 | -8.05%   | 91.60%             | -35.15% |    -0.09 |       79 | 50.92%     | ok               |
|          40 | -12.32%  | 91.60%             | -37.94% |    -0.23 |       78 | 43.43%     | ok               |
|          50 | -11.86%  | 91.60%             | -35.70% |    -0.24 |       68 | 37.60%     | ok               |

## POL-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 29.19%   | -54.69%            | -38.69% |     0.5  |       81 | 50.00%     | ok               |
|          25 | 7.51%    | -54.69%            | -41.31% |     0.31 |       73 | 55.36%     | ok               |
|          20 | -4.28%   | -54.69%            | -48.62% |     0.2  |       81 | 59.20%     | ok               |
|          40 | -9.21%   | -54.69%            | -33.57% |     0.07 |       60 | 31.42%     | ok               |
|          15 | -22.73%  | -54.69%            | -54.66% |    -0    |       84 | 63.41%     | ok               |

## QCOM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -15.47%  | -8.99%             | -58.29% |    -0.02 |       75 | 45.59%     | ok               |
|          35 | -17.72%  | -8.99%             | -51.84% |    -0.07 |       79 | 41.60%     | ok               |
|          20 | -22.77%  | -8.99%             | -58.75% |    -0.12 |       70 | 49.08%     | ok               |
|          50 | -21.73%  | -8.99%             | -42.76% |    -0.2  |       60 | 27.95%     | ok               |
|          30 | -27.33%  | -8.99%             | -57.69% |    -0.22 |       77 | 44.09%     | ok               |

## QQQ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 28.03%   | 67.31%             | -14.17% |     0.67 |       63 | 53.74%     | ok               |
|          25 | 19.34%   | 67.31%             | -12.88% |     0.54 |       61 | 47.75%     | ok               |
|          20 | 18.12%   | 67.31%             | -12.98% |     0.5  |       69 | 50.42%     | ok               |
|          30 | 11.28%   | 67.31%             | -14.20% |     0.37 |       66 | 45.76%     | ok               |
|          35 | -0.16%   | 67.31%             | -20.59% |     0.07 |       72 | 41.93%     | ok               |

## RENDER-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 37.03%   | -53.87%            | -43.43% |     0.55 |       89 | 57.66%     | ok               |
|          25 | 30.70%   | -53.87%            | -40.60% |     0.51 |       89 | 52.68%     | ok               |
|          15 | 29.18%   | -53.87%            | -44.59% |     0.51 |       86 | 60.92%     | ok               |
|          30 | -15.42%  | -53.87%            | -44.84% |     0.12 |       92 | 46.93%     | ok               |
|          35 | -29.06%  | -53.87%            | -44.76% |    -0.1  |       82 | 40.04%     | ok               |

## RTX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 48.70%   | 71.11%             | -18.66% |     0.98 |       74 | 57.24%     | ok               |
|          25 | 43.61%   | 71.11%             | -18.59% |     0.91 |       62 | 54.58%     | ok               |
|          15 | 39.71%   | 71.11%             | -19.55% |     0.82 |       67 | 61.73%     | ok               |
|          30 | 34.84%   | 71.11%             | -16.99% |     0.77 |       64 | 52.41%     | ok               |
|          35 | 26.91%   | 71.11%             | -18.00% |     0.69 |       58 | 49.25%     | ok               |

## SBUX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -2.85%   | 23.62%             | -23.55% |     0.04 |       55 | 40.43%     | ok               |
|          40 | -7.42%   | 23.62%             | -25.43% |    -0.09 |       62 | 33.11%     | ok               |
|          45 | -8.92%   | 23.62%             | -27.26% |    -0.15 |       68 | 27.79%     | ok               |
|          20 | -14.46%  | 23.62%             | -30.94% |    -0.2  |       60 | 42.43%     | ok               |
|          30 | -13.89%  | 23.62%             | -29.22% |    -0.22 |       60 | 38.44%     | ok               |

## SCHW Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -6.61%   | 21.48%             | -28.76% |    -0.07 |       67 | 48.59%     | ok               |
|          45 | -5.72%   | 21.48%             | -16.53% |    -0.11 |       60 | 31.28%     | ok               |
|          20 | -11.35%  | 21.48%             | -29.24% |    -0.18 |       75 | 51.08%     | ok               |
|          50 | -8.23%   | 21.48%             | -13.28% |    -0.24 |       54 | 28.45%     | ok               |
|          40 | -13.53%  | 21.48%             | -23.35% |    -0.32 |       70 | 35.77%     | ok               |

## SHIB-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -33.00%  | -57.57%            | -43.62% |    -0.22 |       77 | 58.43%     | ok               |
|          15 | -36.51%  | -57.57%            | -45.04% |    -0.26 |       87 | 66.67%     | ok               |
|          20 | -38.70%  | -57.57%            | -47.04% |    -0.31 |       81 | 61.69%     | ok               |
|          35 | -36.40%  | -57.57%            | -44.56% |    -0.36 |       71 | 45.59%     | ok               |
|          40 | -38.26%  | -57.57%            | -41.69% |    -0.43 |       60 | 37.93%     | ok               |

## SHY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd    |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:-------|---------:|---------:|:-----------|:-----------------|
|          30 | -1.78%   | -0.45%             | -3.30% |    -0.6  |       46 | 36.77%     | ok               |
|          35 | -2.39%   | -0.45%             | -3.61% |    -0.82 |       52 | 35.27%     | ok               |
|          40 | -2.41%   | -0.45%             | -3.58% |    -0.83 |       54 | 33.94%     | ok               |
|          45 | -2.43%   | -0.45%             | -3.43% |    -0.89 |       54 | 28.45%     | ok               |
|          25 | -3.01%   | -0.45%             | -4.43% |    -0.99 |       60 | 38.94%     | ok               |

## SKY-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -56.11%  | 22.06%             | -64.97% |    -0.67 |       73 | 54.60%     | ok               |
|          30 | -53.28%  | 22.06%             | -61.34% |    -0.71 |       87 | 45.40%     | ok               |
|          25 | -58.17%  | 22.06%             | -65.39% |    -0.81 |       80 | 48.66%     | ok               |
|          20 | -62.41%  | 22.06%             | -69.99% |    -0.87 |       75 | 52.11%     | ok               |
|          35 | -56.64%  | 22.06%             | -60.18% |    -0.88 |       80 | 37.55%     | ok               |

## SLB Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 8.54%    | -0.72%             | -28.43% |     0.27 |       48 | 34.61%     | ok               |
|          45 | 8.21%    | -0.72%             | -25.36% |     0.27 |       60 | 31.11%     | ok               |
|          50 | -6.52%   | -0.72%             | -29.54% |    -0.06 |       48 | 26.29%     | ok               |
|          35 | -20.80%  | -0.72%             | -45.96% |    -0.33 |       70 | 42.10%     | ok               |
|          25 | -34.55%  | -0.72%             | -55.80% |    -0.61 |       86 | 53.08%     | ok               |

## SLV Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 45.49%   | 98.45%             | -34.10% |     0.67 |       52 | 30.62%     | ok               |
|          45 | 33.14%   | 98.45%             | -31.82% |     0.55 |       63 | 32.11%     | ok               |
|          40 | 32.08%   | 98.45%             | -34.28% |     0.54 |       67 | 34.11%     | ok               |
|          20 | 21.26%   | 98.45%             | -42.66% |     0.42 |       70 | 44.43%     | ok               |
|          15 | 21.25%   | 98.45%             | -47.98% |     0.42 |       71 | 49.25%     | ok               |

## SMH Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 78.55%   | 167.22%            | -31.66% |     1.06 |       47 | 46.92%     | ok               |
|          25 | 61.61%   | 167.22%            | -33.57% |     0.93 |       44 | 45.59%     | ok               |
|          35 | 59.89%   | 167.22%            | -34.65% |     0.92 |       54 | 42.60%     | ok               |
|          30 | 57.21%   | 167.22%            | -34.29% |     0.88 |       48 | 44.26%     | ok               |
|          45 | 45.76%   | 167.22%            | -33.35% |     0.81 |       54 | 36.77%     | ok               |

## SNX-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | -12.95%  | -62.53%            | -41.29% |     0.05 |       56 | 27.78%     | ok               |
|          20 | -20.49%  | -62.53%            | -50.72% |     0.02 |       71 | 44.06%     | ok               |
|          40 | -13.00%  | -62.53%            | -36.00% |    -0.01 |       46 | 22.80%     | ok               |
|          30 | -20.84%  | -62.53%            | -50.27% |    -0.03 |       62 | 33.91%     | ok               |
|          15 | -42.54%  | -62.53%            | -52.52% |    -0.27 |       77 | 48.66%     | ok               |

## SOL-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 48.67%   | -21.37%            | -38.17% |     0.68 |       58 | 41.38%     | ok               |
|          35 | 23.89%   | -21.37%            | -43.70% |     0.46 |       70 | 47.89%     | ok               |
|          45 | 5.29%    | -21.37%            | -46.83% |     0.25 |       60 | 35.82%     | ok               |
|          25 | 1.07%    | -21.37%            | -41.09% |     0.24 |       70 | 58.43%     | ok               |
|          15 | -2.18%   | -21.37%            | -46.84% |     0.21 |       73 | 64.18%     | ok               |

## SOXX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | 78.60%   | 152.66%            | -39.32% |     1.03 |       53 | 45.26%     | ok               |
|          35 | 74.58%   | 152.66%            | -38.76% |     1.01 |       56 | 40.77%     | ok               |
|          30 | 73.64%   | 152.66%            | -39.81% |     0.99 |       54 | 43.09%     | ok               |
|          20 | 62.83%   | 152.66%            | -39.19% |     0.87 |       59 | 46.26%     | ok               |
|          40 | 49.24%   | 152.66%            | -41.03% |     0.78 |       58 | 38.77%     | ok               |

## SPY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 11.02%   | 46.71%             | -14.25% |     0.41 |       59 | 53.91%     | ok               |
|          15 | 10.49%   | 46.71%             | -16.80% |     0.39 |       63 | 56.57%     | ok               |
|          25 | 6.03%    | 46.71%             | -14.25% |     0.26 |       59 | 52.91%     | ok               |
|          30 | -0.12%   | 46.71%             | -15.53% |     0.06 |       64 | 50.25%     | ok               |
|          35 | -1.09%   | 46.71%             | -15.58% |     0.02 |       62 | 47.09%     | ok               |

## SUSHI-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -14.03%  | -61.62%            | -34.75% |    -0.04 |       58 | 17.05%     | ok               |
|          45 | -60.31%  | -61.62%            | -64.10% |    -0.83 |       60 | 22.03%     | ok               |
|          40 | -63.38%  | -61.62%            | -66.52% |    -0.84 |       63 | 28.54%     | ok               |
|          15 | -78.61%  | -61.62%            | -80.55% |    -1    |       86 | 50.19%     | ok               |
|          35 | -71.02%  | -61.62%            | -73.80% |    -1    |       84 | 33.72%     | ok               |

## T Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 58.62%   | 41.20%             | -15.08% |     1.06 |       73 | 65.56%     | ok               |
|          20 | 54.71%   | 41.20%             | -18.13% |     1.04 |       68 | 61.06%     | ok               |
|          25 | 52.95%   | 41.20%             | -17.66% |     1.02 |       68 | 58.90%     | ok               |
|          30 | 38.72%   | 41.20%             | -17.01% |     0.83 |       72 | 56.74%     | ok               |
|          35 | 23.59%   | 41.20%             | -14.49% |     0.59 |       78 | 52.41%     | ok               |

## TGT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -11.80%  | -4.18%             | -34.98% |    -0.18 |       62 | 37.77%     | ok               |
|          45 | -11.70%  | -4.18%             | -25.62% |    -0.22 |       50 | 28.62%     | ok               |
|          20 | -16.69%  | -4.18%             | -38.96% |    -0.25 |       88 | 45.42%     | ok               |
|          25 | -15.93%  | -4.18%             | -38.33% |    -0.27 |       72 | 40.93%     | ok               |
|          40 | -16.78%  | -4.18%             | -29.65% |    -0.35 |       52 | 31.28%     | ok               |

## TIA-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -56.09%  | -80.05%            | -66.82% |    -0.29 |       97 | 59.20%     | ok               |
|          35 | -43.28%  | -80.05%            | -65.35% |    -0.32 |       76 | 35.44%     | ok               |
|          40 | -52.06%  | -80.05%            | -70.26% |    -0.54 |       78 | 29.31%     | ok               |
|          25 | -65.72%  | -80.05%            | -70.91% |    -0.59 |       96 | 48.28%     | ok               |
|          45 | -45.92%  | -80.05%            | -66.46% |    -0.59 |       62 | 20.31%     | ok               |

## TLT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -11.04%  | -16.23%            | -14.52% |    -1.22 |       38 | 17.47%     | ok               |
|          40 | -15.40%  | -16.23%            | -17.75% |    -1.34 |       56 | 25.46%     | ok               |
|          30 | -18.85%  | -16.23%            | -22.03% |    -1.41 |       70 | 33.94%     | ok               |
|          45 | -14.82%  | -16.23%            | -17.21% |    -1.54 |       44 | 20.97%     | ok               |
|          35 | -19.35%  | -16.23%            | -21.86% |    -1.6  |       68 | 29.12%     | ok               |

## TMO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 53.22%   | 10.52%             | -8.17%  |     1.11 |       48 | 35.77%     | ok               |
|          45 | 47.24%   | 10.52%             | -9.69%  |     0.97 |       52 | 40.60%     | ok               |
|          40 | 42.94%   | 10.52%             | -9.91%  |     0.88 |       57 | 45.42%     | ok               |
|          35 | 37.45%   | 10.52%             | -13.84% |     0.75 |       69 | 50.75%     | ok               |
|          30 | 27.63%   | 10.52%             | -18.85% |     0.58 |       67 | 55.57%     | ok               |

## TMUS Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 2.61%    | 3.06%              | -28.12% |     0.15 |       74 | 47.92%     | ok               |
|          15 | -1.29%   | 3.06%              | -35.31% |     0.08 |       68 | 60.40%     | ok               |
|          25 | -5.09%   | 3.06%              | -33.38% |    -0.01 |       77 | 50.75%     | ok               |
|          20 | -6.98%   | 3.06%              | -33.93% |    -0.05 |       74 | 54.74%     | ok               |
|          50 | -5.70%   | 3.06%              | -30.81% |    -0.08 |       58 | 34.28%     | ok               |

## TRX-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 19.40%   | 34.76%             | -18.79% |     0.62 |       54 | 40.42%     | ok               |
|          35 | 12.39%   | 34.76%             | -21.77% |     0.42 |       68 | 49.04%     | ok               |
|          20 | 11.07%   | 34.76%             | -25.45% |     0.36 |       61 | 59.00%     | ok               |
|          30 | 9.69%    | 34.76%             | -22.90% |     0.35 |       68 | 51.92%     | ok               |
|          25 | 7.03%    | 34.76%             | -26.84% |     0.27 |       66 | 55.56%     | ok               |

## TSLA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 41.47%   | 117.14%            | -30.57% |     0.6  |       64 | 30.12%     | ok               |
|          40 | 13.71%   | 117.14%            | -50.11% |     0.34 |       63 | 35.61%     | ok               |
|          45 | -10.53%  | 117.14%            | -52.01% |     0.07 |       69 | 32.61%     | ok               |
|          35 | -18.00%  | 117.14%            | -58.86% |     0    |       74 | 38.27%     | ok               |
|          30 | -35.10%  | 117.14%            | -58.36% |    -0.22 |       78 | 43.09%     | ok               |

## TXN Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 11.11%   | 47.79%             | -45.45% |     0.3  |       66 | 32.61%     | ok               |
|          35 | -8.45%   | 47.79%             | -43.38% |    -0    |       76 | 46.92%     | ok               |
|          40 | -9.38%   | 47.79%             | -45.67% |    -0.02 |       72 | 44.76%     | ok               |
|          20 | -15.55%  | 47.79%             | -38.98% |    -0.07 |       70 | 56.74%     | ok               |
|          45 | -12.82%  | 47.79%             | -46.24% |    -0.09 |       80 | 38.94%     | ok               |

## UNH Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 23.98%   | -27.35%            | -36.92% |     0.47 |       54 | 28.79%     | ok               |
|          30 | 23.37%   | -27.35%            | -26.31% |     0.45 |       75 | 48.75%     | ok               |
|          20 | 21.10%   | -27.35%            | -26.96% |     0.42 |       78 | 57.90%     | ok               |
|          15 | 21.06%   | -27.35%            | -26.07% |     0.41 |       83 | 64.06%     | ok               |
|          35 | 19.61%   | -27.35%            | -27.49% |     0.41 |       70 | 43.76%     | ok               |

## UNI-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 42.92%   | 55.02%             | -45.09% |     0.61 |       52 | 26.82%     | ok               |
|          45 | 30.82%   | 55.02%             | -51.70% |     0.51 |       58 | 34.29%     | ok               |
|          40 | 13.69%   | 55.02%             | -61.16% |     0.38 |       62 | 39.46%     | ok               |
|          35 | -0.29%   | 55.02%             | -65.47% |     0.27 |       72 | 45.02%     | ok               |
|          20 | -53.73%  | 55.02%             | -80.78% |    -0.26 |       95 | 60.34%     | ok               |

## UPS Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | -27.37%  | -37.62%            | -31.52% |    -0.5  |       64 | 36.27%     | ok               |
|          40 | -27.50%  | -37.62%            | -31.55% |    -0.52 |       60 | 30.95%     | ok               |
|          20 | -32.33%  | -37.62%            | -38.12% |    -0.58 |       86 | 49.25%     | ok               |
|          25 | -32.87%  | -37.62%            | -38.62% |    -0.61 |       78 | 45.92%     | ok               |
|          30 | -33.36%  | -37.62%            | -39.06% |    -0.64 |       72 | 42.10%     | ok               |

## USO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 7.46%    | 89.65%             | -32.38% |     0.25 |       48 | 25.96%     | ok               |
|          20 | 4.01%    | 89.65%             | -44.49% |     0.2  |       77 | 38.10%     | ok               |
|          15 | 0.71%    | 89.65%             | -45.41% |     0.16 |       71 | 41.76%     | ok               |
|          25 | -4.59%   | 89.65%             | -46.08% |     0.07 |       71 | 35.44%     | ok               |
|          50 | -3.42%   | 89.65%             | -29.54% |     0.07 |       52 | 24.13%     | ok               |

## VEA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 8.20%    | 37.20%             | -13.94% |     0.34 |       54 | 49.75%     | ok               |
|          20 | 1.91%    | 37.20%             | -15.50% |     0.13 |       59 | 47.09%     | ok               |
|          25 | -1.95%   | 37.20%             | -15.59% |    -0.02 |       55 | 45.09%     | ok               |
|          30 | -3.38%   | 37.20%             | -16.11% |    -0.09 |       58 | 43.26%     | ok               |
|          35 | -3.45%   | 37.20%             | -14.64% |    -0.09 |       52 | 41.60%     | ok               |

## VIXY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -56.34%  | -64.59%            | -69.78% |    -0.67 |       36 | 10.15%     | ok               |
|          15 | -77.55%  | -64.59%            | -89.47% |    -0.81 |       95 | 44.09%     | ok               |
|          45 | -65.70%  | -64.59%            | -75.03% |    -0.87 |       56 | 15.14%     | ok               |
|          30 | -78.22%  | -64.59%            | -88.19% |    -0.94 |       94 | 33.28%     | ok               |
|          40 | -73.09%  | -64.59%            | -80.72% |    -1    |       68 | 18.97%     | ok               |

## VNQ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -12.01%  | 4.39%              | -22.34% |    -0.45 |       71 | 42.60%     | ok               |
|          45 | -11.81%  | 4.39%              | -19.07% |    -0.54 |       64 | 28.95%     | ok               |
|          30 | -13.98%  | 4.39%              | -24.92% |    -0.56 |       75 | 39.93%     | ok               |
|          20 | -15.80%  | 4.39%              | -24.00% |    -0.61 |       74 | 45.42%     | ok               |
|          50 | -12.68%  | 4.39%              | -17.13% |    -0.61 |       56 | 25.62%     | ok               |

## VTI Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 9.78%    | 45.08%             | -14.91% |     0.38 |       62 | 54.24%     | ok               |
|          15 | 5.27%    | 45.08%             | -17.19% |     0.23 |       59 | 56.57%     | ok               |
|          25 | -0.17%   | 45.08%             | -15.00% |     0.06 |       58 | 52.25%     | ok               |
|          30 | -7.66%   | 45.08%             | -17.64% |    -0.22 |       68 | 50.25%     | ok               |
|          40 | -8.77%   | 45.08%             | -19.77% |    -0.29 |       72 | 42.76%     | ok               |

## VWO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -11.66%  | 34.80%             | -23.75% |    -0.45 |       58 | 31.78%     | ok               |
|          40 | -12.12%  | 34.80%             | -23.57% |    -0.46 |       68 | 34.61%     | ok               |
|          50 | -12.01%  | 34.80%             | -23.51% |    -0.47 |       56 | 28.95%     | ok               |
|          15 | -15.85%  | 34.80%             | -26.00% |    -0.52 |       73 | 47.75%     | ok               |
|          20 | -17.19%  | 34.80%             | -28.09% |    -0.59 |       70 | 45.42%     | ok               |

## VZ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 0.31%    | 13.04%             | -12.96% |     0.07 |       56 | 28.45%     | ok               |
|          45 | -10.78%  | 13.04%             | -21.44% |    -0.29 |       68 | 32.11%     | ok               |
|          35 | -11.44%  | 13.04%             | -22.73% |    -0.3  |       62 | 37.77%     | ok               |
|          25 | -13.00%  | 13.04%             | -22.13% |    -0.31 |       81 | 45.59%     | ok               |
|          40 | -15.11%  | 13.04%             | -24.21% |    -0.44 |       66 | 35.27%     | ok               |

## WFC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | -7.01%   | 28.75%             | -21.57% |    -0.07 |       77 | 44.59%     | ok               |
|          50 | -6.06%   | 28.75%             | -18.29% |    -0.13 |       60 | 32.78%     | ok               |
|          30 | -16.70%  | 28.75%             | -28.90% |    -0.27 |       80 | 47.75%     | ok               |
|          40 | -12.76%  | 28.75%             | -23.94% |    -0.3  |       72 | 41.26%     | ok               |
|          20 | -19.84%  | 28.75%             | -31.40% |    -0.3  |       79 | 52.91%     | ok               |

## WIF-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 78.81%   | -58.98%            | -40.67% |     0.74 |       65 | 44.06%     | ok               |
|          15 | 39.74%   | -58.98%            | -46.21% |     0.56 |       75 | 47.32%     | ok               |
|          25 | 13.85%   | -58.98%            | -44.74% |     0.39 |       63 | 40.04%     | ok               |
|          30 | -26.40%  | -58.98%            | -52.76% |    -0.01 |       64 | 36.97%     | ok               |
|          40 | -21.11%  | -58.98%            | -51.66% |    -0.06 |       58 | 25.10%     | ok               |

## WMT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 35.91%   | 80.78%             | -12.18% |     1.09 |       36 | 37.27%     | ok               |
|          45 | 34.77%   | 80.78%             | -14.14% |     1.02 |       42 | 39.60%     | ok               |
|          35 | 24.94%   | 80.78%             | -18.25% |     0.73 |       58 | 45.92%     | ok               |
|          40 | 23.33%   | 80.78%             | -18.53% |     0.71 |       50 | 41.26%     | ok               |
|          15 | 6.60%    | 80.78%             | -26.24% |     0.24 |       82 | 59.90%     | ok               |

## XBI Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 9.74%    | 62.22%             | -16.08% |     0.32 |       54 | 35.27%     | ok               |
|          45 | 5.57%    | 62.22%             | -15.46% |     0.22 |       52 | 32.78%     | ok               |
|          35 | -1.60%   | 62.22%             | -16.96% |     0.04 |       62 | 38.10%     | ok               |
|          30 | -3.65%   | 62.22%             | -18.28% |    -0.01 |       64 | 39.60%     | ok               |
|          50 | -3.51%   | 62.22%             | -15.95% |    -0.02 |       52 | 29.62%     | ok               |

## XLB Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -3.72%   | 6.44%              | -16.40% |    -0.11 |       40 | 22.80%     | ok               |
|          40 | -4.61%   | 6.44%              | -18.27% |    -0.13 |       56 | 26.96%     | ok               |
|          45 | -7.17%   | 6.44%              | -18.10% |    -0.25 |       44 | 24.46%     | ok               |
|          35 | -7.85%   | 6.44%              | -21.38% |    -0.25 |       56 | 30.45%     | ok               |
|          25 | -10.78%  | 6.44%              | -23.37% |    -0.35 |       64 | 35.94%     | ok               |

## XLC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 12.62%   | 34.81%             | -12.33% |     0.47 |       61 | 50.25%     | ok               |
|          25 | 12.06%   | 34.81%             | -12.31% |     0.45 |       60 | 52.41%     | ok               |
|          50 | 7.97%    | 34.81%             | -11.12% |     0.41 |       64 | 38.60%     | ok               |
|          40 | 8.61%    | 34.81%             | -13.38% |     0.37 |       60 | 44.09%     | ok               |
|          35 | 7.08%    | 34.81%             | -13.38% |     0.31 |       60 | 47.75%     | ok               |

## XLE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -1.77%   | 34.94%             | -25.98% |     0.03 |       54 | 35.94%     | ok               |
|          35 | -4.84%   | 34.94%             | -26.89% |    -0.04 |       63 | 42.43%     | ok               |
|          45 | -5.02%   | 34.94%             | -28.46% |    -0.07 |       58 | 38.10%     | ok               |
|          30 | -9.12%   | 34.94%             | -30.31% |    -0.15 |       69 | 44.43%     | ok               |
|          25 | -12.82%  | 34.94%             | -33.14% |    -0.24 |       80 | 47.42%     | ok               |

## XLF Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -1.15%   | 27.43%             | -18.63% |     0.02 |       72 | 51.91%     | ok               |
|          15 | -3.26%   | 27.43%             | -20.19% |    -0.04 |       76 | 54.58%     | ok               |
|          25 | -8.05%   | 27.43%             | -23.22% |    -0.23 |       79 | 48.75%     | ok               |
|          30 | -8.65%   | 27.43%             | -23.61% |    -0.26 |       80 | 46.76%     | ok               |
|          35 | -15.76%  | 27.43%             | -24.48% |    -0.6  |       70 | 43.09%     | ok               |

## XLI Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 3.66%    | 33.27%             | -12.74% |     0.18 |       86 | 51.25%     | ok               |
|          20 | 1.45%    | 33.27%             | -12.74% |     0.11 |       75 | 46.42%     | ok               |
|          50 | -4.76%   | 33.27%             | -14.94% |    -0.18 |       60 | 31.78%     | ok               |
|          45 | -5.38%   | 33.27%             | -16.29% |    -0.19 |       70 | 34.28%     | ok               |
|          25 | -8.75%   | 33.27%             | -17.00% |    -0.29 |       78 | 44.43%     | ok               |

## XLK Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 75.46%   | 89.07%             | -14.75% |     1.26 |       46 | 49.75%     | ok               |
|          25 | 69.56%   | 89.07%             | -14.75% |     1.23 |       42 | 47.92%     | ok               |
|          15 | 73.67%   | 89.07%             | -14.75% |     1.2  |       46 | 51.58%     | ok               |
|          30 | 59.41%   | 89.07%             | -14.75% |     1.13 |       42 | 46.59%     | ok               |
|          35 | 43.31%   | 89.07%             | -13.43% |     0.92 |       56 | 43.93%     | ok               |

## XLM-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 5.66%    | -23.10%            | -48.81% |     0.26 |       44 | 27.20%     | ok               |
|          45 | 4.49%    | -23.10%            | -51.28% |     0.25 |       54 | 32.18%     | ok               |
|          25 | 0.47%    | -23.10%            | -49.14% |     0.23 |       67 | 50.38%     | ok               |
|          40 | -4.77%   | -23.10%            | -47.28% |     0.16 |       51 | 37.55%     | ok               |
|          30 | -6.83%   | -23.10%            | -54.58% |     0.15 |       65 | 48.08%     | ok               |

## XLP Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 8.13%    | 5.69%              | -5.66%  |     0.53 |       52 | 29.45%     | ok               |
|          50 | 5.69%    | 5.69%              | -6.08%  |     0.39 |       58 | 27.29%     | ok               |
|          40 | 5.95%    | 5.69%              | -7.77%  |     0.38 |       68 | 33.61%     | ok               |
|          35 | 5.02%    | 5.69%              | -9.73%  |     0.33 |       64 | 36.61%     | ok               |
|          30 | 3.16%    | 5.69%              | -11.16% |     0.22 |       66 | 38.10%     | ok               |

## XLU Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 4.61%    | 13.47%             | -13.94% |     0.26 |       54 | 31.28%     | ok               |
|          45 | 3.47%    | 13.47%             | -14.88% |     0.21 |       58 | 32.45%     | ok               |
|          40 | 0.34%    | 13.47%             | -16.41% |     0.06 |       64 | 34.28%     | ok               |
|          35 | -2.32%   | 13.47%             | -19.71% |    -0.06 |       64 | 36.94%     | ok               |
|          30 | -6.55%   | 13.47%             | -20.40% |    -0.24 |       69 | 40.43%     | ok               |

## XLV Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -22.00%  | 15.47%             | -22.40% |    -1.04 |       76 | 39.27%     | ok               |
|          30 | -22.35%  | 15.47%             | -22.75% |    -1.08 |       76 | 37.60%     | ok               |
|          15 | -25.22%  | 15.47%             | -25.35% |    -1.18 |       83 | 43.43%     | ok               |
|          20 | -25.06%  | 15.47%             | -25.19% |    -1.2  |       79 | 40.93%     | ok               |
|          35 | -26.22%  | 15.47%             | -26.58% |    -1.37 |       70 | 34.61%     | ok               |

## XLY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -0.70%   | 24.46%             | -15.77% |     0.06 |       76 | 54.24%     | ok               |
|          30 | -4.15%   | 24.46%             | -18.35% |    -0.06 |       75 | 47.59%     | ok               |
|          20 | -5.95%   | 24.46%             | -19.25% |    -0.1  |       72 | 50.92%     | ok               |
|          25 | -8.05%   | 24.46%             | -19.98% |    -0.17 |       69 | 49.42%     | ok               |
|          50 | -6.34%   | 24.46%             | -15.82% |    -0.22 |       62 | 32.11%     | ok               |

## XOM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | 2.73%    | 38.35%             | -19.90% |     0.15 |       55 | 34.94%     | ok               |
|          30 | 1.71%    | 38.35%             | -20.29% |     0.12 |       55 | 34.28%     | ok               |
|          50 | 0.63%    | 38.35%             | -21.35% |     0.09 |       36 | 26.96%     | ok               |
|          20 | -3.12%   | 38.35%             | -25.56% |    -0.01 |       62 | 37.27%     | ok               |
|          45 | -3.17%   | 38.35%             | -23.33% |    -0.02 |       42 | 28.29%     | ok               |

## XRP-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 27.38%   | -34.16%            | -31.38% |     0.49 |       70 | 43.10%     | ok               |
|          40 | 10.41%   | -34.16%            | -33.91% |     0.32 |       62 | 36.78%     | ok               |
|          45 | -2.35%   | -34.16%            | -37.18% |     0.16 |       60 | 32.57%     | ok               |
|          30 | -4.79%   | -34.16%            | -31.82% |     0.15 |       65 | 48.08%     | ok               |
|          50 | -6.49%   | -34.16%            | -39.26% |     0.09 |       58 | 24.90%     | ok               |

## YFI-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -47.14%  | -54.79%            | -50.13% |    -0.78 |       56 | 27.59%     | ok               |
|          45 | -47.22%  | -54.79%            | -50.21% |    -1.01 |       70 | 22.22%     | ok               |
|          35 | -64.36%  | -54.79%            | -64.36% |    -1.17 |       63 | 34.29%     | ok               |
|          50 | -51.83%  | -54.79%            | -51.83% |    -1.34 |       54 | 16.48%     | ok               |
|          25 | -71.42%  | -54.79%            | -71.42% |    -1.36 |       76 | 41.95%     | ok               |

## ZEC-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 217.75%  | 3284.40%           | -30.64% |     1.11 |       46 | 33.33%     | ok               |
|          35 | 193.41%  | 3284.40%           | -50.84% |     1.04 |       52 | 39.08%     | ok               |
|          25 | 185.09%  | 3284.40%           | -58.07% |     1    |       55 | 45.02%     | ok               |
|          30 | 173.34%  | 3284.40%           | -56.50% |     0.98 |       59 | 42.53%     | ok               |
|          20 | 140.70%  | 3284.40%           | -62.70% |     0.89 |       63 | 46.74%     | ok               |
