# Market Tracker Backtest Report

_Generated: 2026-06-04T01:48:49+00:00_

## Data Sources

- Crypto: Kraken -> Coinbase -> CoinGecko OHLC -> CoinPaprika fallback chain.
- Stocks / ETFs / indices: Stooq -> Yahoo Finance fallback chain.
- Data rows are generated from real market APIs. Mock OHLCV rows are not generated.

## Data Freshness

- Rows: **92,351**
- Symbols: **161**
- Date range: **2024-01-10** to **2026-06-04**

## Latest Signals

| symbol     | date                |         close |   composite_score | signal   | data_source   |
|:-----------|:--------------------|--------------:|------------------:|:---------|:--------------|
| AAPL       | 2026-06-03 00:00:00 |   310.26      |          36.0833  | LONG     | Yahoo Finance |
| ABBV       | 2026-06-03 00:00:00 |   217.13      |          67.1667  | LONG     | Yahoo Finance |
| AMD        | 2026-06-03 00:00:00 |   542.52      |          62.25    | LONG     | Yahoo Finance |
| CSCO       | 2026-06-03 00:00:00 |   126.5       |          66.5833  | LONG     | Yahoo Finance |
| DE         | 2026-06-03 00:00:00 |   588.29      |          50.9167  | LONG     | Yahoo Finance |
| DXY-INDEX  | 2026-06-03 00:00:00 |    99.449     |          80.3763  | LONG     | Yahoo Finance |
| FCX        | 2026-06-03 00:00:00 |    70.64      |          73.5833  | LONG     | Yahoo Finance |
| GE         | 2026-06-03 00:00:00 |   314.64      |          65.1667  | LONG     | Yahoo Finance |
| GS         | 2026-06-03 00:00:00 |  1041.02      |          60.9167  | LONG     | Yahoo Finance |
| HON        | 2026-06-03 00:00:00 |   223.26      |          41.5     | LONG     | Yahoo Finance |
| IBM        | 2026-06-03 00:00:00 |   305.63      |          53.5833  | LONG     | Yahoo Finance |
| ICP-USD    | 2026-06-04 00:00:00 |     2.92      |          47.5833  | LONG     | Kraken API    |
| INJ-USD    | 2026-06-04 00:00:00 |     6.343     |          61.8333  | LONG     | Kraken API    |
| INTC       | 2026-06-03 00:00:00 |   112.71      |          44.0833  | LONG     | Yahoo Finance |
| LLY        | 2026-06-03 00:00:00 |  1078.78      |          72.4167  | LONG     | Yahoo Finance |
| LRCX       | 2026-06-03 00:00:00 |   343.71      |          75.75    | LONG     | Yahoo Finance |
| MSFT       | 2026-06-03 00:00:00 |   427.34      |          33.9167  | LONG     | Yahoo Finance |
| MU         | 2026-06-03 00:00:00 |  1079.57      |          66.25    | LONG     | Yahoo Finance |
| ORCL       | 2026-06-03 00:00:00 |   230.33      |          56.9167  | LONG     | Yahoo Finance |
| QCOM       | 2026-06-03 00:00:00 |   250.01      |          65.5833  | LONG     | Yahoo Finance |
| QQQ        | 2026-06-03 00:00:00 |   744.21      |          49.75    | LONG     | Yahoo Finance |
| RENDER-USD | 2026-06-04 00:00:00 |     2.07      |          65.4167  | LONG     | Kraken API    |
| SPY        | 2026-06-03 00:00:00 |   754.24      |          37.5833  | LONG     | Yahoo Finance |
| SUSHI-USD  | 2026-06-04 00:00:00 |     0.2218    |          38.4167  | LONG     | Kraken API    |
| TXN        | 2026-06-03 00:00:00 |   308.59      |          54.0833  | LONG     | Yahoo Finance |
| UPS        | 2026-06-03 00:00:00 |   108.67      |          73.25    | LONG     | Yahoo Finance |
| VTI        | 2026-06-03 00:00:00 |   371.65      |          37.5833  | LONG     | Yahoo Finance |
| XLB        | 2026-06-03 00:00:00 |    51.63      |          47.9167  | LONG     | Yahoo Finance |
| XLK        | 2026-06-03 00:00:00 |   196.23      |          67.75    | LONG     | Yahoo Finance |
| ADBE       | 2026-06-03 00:00:00 |   256.24      |          24.3333  | NEUTRAL  | Yahoo Finance |
| AGG        | 2026-06-03 00:00:00 |    98.5       |         -29.75    | NEUTRAL  | Yahoo Finance |
| ALGO-USD   | 2026-06-04 00:00:00 |     0.1043    |         -26.75    | NEUTRAL  | Kraken API    |
| AMAT       | 2026-06-03 00:00:00 |   500.77      |          64.5     | NEUTRAL  | Yahoo Finance |
| AMGN       | 2026-06-03 00:00:00 |   338.22      |          33.25    | NEUTRAL  | Yahoo Finance |
| AMZN       | 2026-06-03 00:00:00 |   250.02      |         -13.3333  | NEUTRAL  | Yahoo Finance |
| ARKK       | 2026-06-03 00:00:00 |    78.16      |          41.0833  | NEUTRAL  | Yahoo Finance |
| AVGO       | 2026-06-03 00:00:00 |   479.23      |          52       | NEUTRAL  | Yahoo Finance |
| BA         | 2026-06-03 00:00:00 |   210.58      |         -64.5833  | NEUTRAL  | Yahoo Finance |
| BAC        | 2026-06-03 00:00:00 |    52.4       |          52.5     | NEUTRAL  | Yahoo Finance |
| BLK        | 2026-06-03 00:00:00 |   990.87      |         -68.3333  | NEUTRAL  | Yahoo Finance |
| BND        | 2026-06-03 00:00:00 |    73.06      |         -18.5     | NEUTRAL  | Yahoo Finance |
| C          | 2026-06-03 00:00:00 |   129.93      |          42.8333  | NEUTRAL  | Yahoo Finance |
| CAT        | 2026-06-03 00:00:00 |   926.18      |          45       | NEUTRAL  | Yahoo Finance |
| CL         | 2026-06-03 00:00:00 |    84.87      |         -25.3333  | NEUTRAL  | Yahoo Finance |
| CMCSA      | 2026-06-03 00:00:00 |    23.52      |         -20.75    | NEUTRAL  | Yahoo Finance |
| COP        | 2026-06-03 00:00:00 |   119.05      |          25.3333  | NEUTRAL  | Yahoo Finance |
| COST       | 2026-06-03 00:00:00 |   961.83      |         -49.25    | NEUTRAL  | Yahoo Finance |
| CRM        | 2026-06-03 00:00:00 |   190.61      |          20.6667  | NEUTRAL  | Yahoo Finance |
| CVX        | 2026-06-03 00:00:00 |   189.71      |          55       | NEUTRAL  | Yahoo Finance |
| DASH-USD   | 2026-06-04 00:00:00 |    37.187     |         -82.5833  | NEUTRAL  | Kraken API    |
| DBC        | 2026-06-03 00:00:00 |    30.29      |          -7.75    | NEUTRAL  | Yahoo Finance |
| DIA        | 2026-06-03 00:00:00 |   508.26      |          53.6667  | NEUTRAL  | Yahoo Finance |
| DOT-USD    | 2026-06-04 00:00:00 |     1.0708    |         -62.5833  | NEUTRAL  | Kraken API    |
| EEM        | 2026-06-03 00:00:00 |    69.92      |          57.3333  | NEUTRAL  | Yahoo Finance |
| EFA        | 2026-06-03 00:00:00 |   104.12      |          26.3333  | NEUTRAL  | Yahoo Finance |
| EOG        | 2026-06-03 00:00:00 |   141.5       |          63.3333  | NEUTRAL  | Yahoo Finance |
| EWJ        | 2026-06-03 00:00:00 |    93.94      |          35.1667  | NEUTRAL  | Yahoo Finance |
| FET-USD    | 2026-06-04 00:00:00 |     0.2451    |          42.6667  | NEUTRAL  | Kraken API    |
| FIL-USD    | 2026-06-04 00:00:00 |     0.89      |         -52.5833  | NEUTRAL  | Kraken API    |
| GDX        | 2026-06-03 00:00:00 |    85         |         -47       | NEUTRAL  | Yahoo Finance |
| GDXJ       | 2026-06-03 00:00:00 |   110.88      |         -38       | NEUTRAL  | Yahoo Finance |
| GLD        | 2026-06-03 00:00:00 |   407.87      |         -22.6667  | NEUTRAL  | Yahoo Finance |
| GOOGL      | 2026-06-03 00:00:00 |   358.99      |          -6.66667 | NEUTRAL  | Yahoo Finance |
| GRT-USD    | 2026-06-04 00:00:00 |     0.02224   |         -54.75    | NEUTRAL  | Kraken API    |
| HBAR-USD   | 2026-06-04 00:00:00 |     0.08325   |         -21.3333  | NEUTRAL  | Kraken API    |
| HD         | 2026-06-03 00:00:00 |   312.97      |         -11.5833  | NEUTRAL  | Yahoo Finance |
| HYG        | 2026-06-03 00:00:00 |    79.68      |         -43.25    | NEUTRAL  | Yahoo Finance |
| IBIT       | 2026-06-03 00:00:00 |    37         |         -68.3333  | NEUTRAL  | Yahoo Finance |
| IEF        | 2026-06-03 00:00:00 |    94         |         -29.75    | NEUTRAL  | Yahoo Finance |
| IEMG       | 2026-06-03 00:00:00 |    84.84      |          57.3333  | NEUTRAL  | Yahoo Finance |
| INTU       | 2026-06-03 00:00:00 |   311.44      |         -75.8333  | NEUTRAL  | Yahoo Finance |
| ITA        | 2026-06-03 00:00:00 |   224.89      |          13.5     | NEUTRAL  | Yahoo Finance |
| IWM        | 2026-06-03 00:00:00 |   287.67      |          57.3333  | NEUTRAL  | Yahoo Finance |
| JNJ        | 2026-06-03 00:00:00 |   223.24      |         -15.5     | NEUTRAL  | Yahoo Finance |
| JPM        | 2026-06-03 00:00:00 |   300.85      |          -8.91667 | NEUTRAL  | Yahoo Finance |
| KO         | 2026-06-03 00:00:00 |    78.76      |          20.4167  | NEUTRAL  | Yahoo Finance |
| LIN        | 2026-06-03 00:00:00 |   507.57      |          22.1667  | NEUTRAL  | Yahoo Finance |
| MCD        | 2026-06-03 00:00:00 |   273.29      |         -37.1667  | NEUTRAL  | Yahoo Finance |
| META       | 2026-06-03 00:00:00 |   622.98      |          -6.5     | NEUTRAL  | Yahoo Finance |
| MPC        | 2026-06-03 00:00:00 |   267.21      |          51       | NEUTRAL  | Yahoo Finance |
| MRK        | 2026-06-03 00:00:00 |   114.7       |          29.25    | NEUTRAL  | Yahoo Finance |
| MS         | 2026-06-03 00:00:00 |   210.14      |          46.3333  | NEUTRAL  | Yahoo Finance |
| NEAR-USD   | 2026-06-04 00:00:00 |     2.6827    |          60.1667  | NEUTRAL  | Kraken API    |
| NEM        | 2026-06-03 00:00:00 |   107.47      |         -42.75    | NEUTRAL  | Yahoo Finance |
| NFLX       | 2026-06-03 00:00:00 |    81.52      |         -68.3333  | NEUTRAL  | Yahoo Finance |
| NKE        | 2026-06-03 00:00:00 |    43.81      |         -11.75    | NEUTRAL  | Yahoo Finance |
| NOW        | 2026-06-03 00:00:00 |   117.9       |          29.9167  | NEUTRAL  | Yahoo Finance |
| NVDA       | 2026-06-03 00:00:00 |   214.75      |         -13.3333  | NEUTRAL  | Yahoo Finance |
| OXY        | 2026-06-03 00:00:00 |    59.64      |          62.8333  | NEUTRAL  | Yahoo Finance |
| PFE        | 2026-06-03 00:00:00 |    25.34      |         -22       | NEUTRAL  | Yahoo Finance |
| PM         | 2026-06-03 00:00:00 |   175.94      |          17.1667  | NEUTRAL  | Yahoo Finance |
| POL-USD    | 2026-06-04 00:00:00 |     0.09085   |         -18.6667  | NEUTRAL  | Kraken API    |
| RTX        | 2026-06-03 00:00:00 |   172.55      |         -51.6667  | NEUTRAL  | Yahoo Finance |
| SBUX       | 2026-06-03 00:00:00 |    95.89      |          -7.83333 | NEUTRAL  | Yahoo Finance |
| SCHW       | 2026-06-03 00:00:00 |    86.59      |         -69       | NEUTRAL  | Yahoo Finance |
| SHY        | 2026-06-03 00:00:00 |    81.97      |         -53.75    | NEUTRAL  | Yahoo Finance |
| SKY-USD    | 2026-06-04 00:00:00 |     0.06679   |         -14.9167  | NEUTRAL  | Kraken API    |
| SLB        | 2026-06-03 00:00:00 |    56.85      |          38.8333  | NEUTRAL  | Yahoo Finance |
| SLV        | 2026-06-03 00:00:00 |    66.21      |         -19.5833  | NEUTRAL  | Yahoo Finance |
| SMH        | 2026-06-03 00:00:00 |   637.9       |          56.1667  | NEUTRAL  | Yahoo Finance |
| SOXX       | 2026-06-03 00:00:00 |   615.68      |          62.5     | NEUTRAL  | Yahoo Finance |
| TGT        | 2026-06-03 00:00:00 |   124.8       |          32       | NEUTRAL  | Yahoo Finance |
| TIA-USD    | 2026-06-04 00:00:00 |     0.3493    |         -65.75    | NEUTRAL  | Kraken API    |
| TLT        | 2026-06-03 00:00:00 |    85.31      |           5.91667 | NEUTRAL  | Yahoo Finance |
| TMO        | 2026-06-03 00:00:00 |   473.95      |           8.58333 | NEUTRAL  | Yahoo Finance |
| TMUS       | 2026-06-03 00:00:00 |   181.45      |         -69.5     | NEUTRAL  | Yahoo Finance |
| TRX-USD    | 2026-06-04 00:00:00 |     0.330409  |         -18.5833  | NEUTRAL  | Kraken API    |
| TSLA       | 2026-06-03 00:00:00 |   423.7       |          18.4167  | NEUTRAL  | Yahoo Finance |
| UNH        | 2026-06-03 00:00:00 |   377         |          13.0833  | NEUTRAL  | Yahoo Finance |
| USO        | 2026-06-03 00:00:00 |   140.86      |          21.8333  | NEUTRAL  | Yahoo Finance |
| VEA        | 2026-06-03 00:00:00 |    71.67      |          57.3333  | NEUTRAL  | Yahoo Finance |
| VNQ        | 2026-06-03 00:00:00 |    94.41      |          -5.16667 | NEUTRAL  | Yahoo Finance |
| VWO        | 2026-06-03 00:00:00 |    60.33      |          39.3333  | NEUTRAL  | Yahoo Finance |
| VZ         | 2026-06-03 00:00:00 |    46.65      |         -11.3333  | NEUTRAL  | Yahoo Finance |
| WFC        | 2026-06-03 00:00:00 |    78.68      |           1.08333 | NEUTRAL  | Yahoo Finance |
| WMT        | 2026-06-03 00:00:00 |   116.89      |         -14.3333  | NEUTRAL  | Yahoo Finance |
| XBI        | 2026-06-03 00:00:00 |   129.83      |         -26.5     | NEUTRAL  | Yahoo Finance |
| XLC        | 2026-06-03 00:00:00 |   112.08      |         -60.5833  | NEUTRAL  | Yahoo Finance |
| XLE        | 2026-06-03 00:00:00 |    58.71      |          41.6667  | NEUTRAL  | Yahoo Finance |
| XLF        | 2026-06-03 00:00:00 |    50.87      |         -56       | NEUTRAL  | Yahoo Finance |
| XLI        | 2026-06-03 00:00:00 |   174.05      |          65.1667  | NEUTRAL  | Yahoo Finance |
| XLM-USD    | 2026-06-04 00:00:00 |     0.201934  |          65.4167  | NEUTRAL  | Kraken API    |
| XLP        | 2026-06-03 00:00:00 |    82.16      |         -38.75    | NEUTRAL  | Yahoo Finance |
| XLV        | 2026-06-03 00:00:00 |   147.55      |           4.25    | NEUTRAL  | Yahoo Finance |
| XLY        | 2026-06-03 00:00:00 |   116.73      |         -28.8333  | NEUTRAL  | Yahoo Finance |
| XOM        | 2026-06-03 00:00:00 |   152.53      |          29.3333  | NEUTRAL  | Yahoo Finance |
| ZEC-USD    | 2026-06-04 00:00:00 |   608.09      |          -1.08333 | NEUTRAL  | Kraken API    |
| AAVE-USD   | 2026-06-04 00:00:00 |    72.13      |         -52.1667  | SHORT    | Kraken API    |
| ADA-USD    | 2026-06-04 00:00:00 |     0.193773  |         -52.0833  | SHORT    | Kraken API    |
| APT-USD    | 2026-06-04 00:00:00 |     0.78      |         -55.8333  | SHORT    | Kraken API    |
| ARB-USD    | 2026-06-04 00:00:00 |     0.0899    |         -51.6667  | SHORT    | Kraken API    |
| ATOM-USD   | 2026-06-04 00:00:00 |     1.8142    |         -48       | SHORT    | Kraken API    |
| AVAX-USD   | 2026-06-04 00:00:00 |     7.82      |         -51.8333  | SHORT    | Kraken API    |
| BCH-USD    | 2026-06-04 00:00:00 |   235.65      |         -70.8333  | SHORT    | Kraken API    |
| BITO       | 2026-06-03 00:00:00 |     8.9       |         -58.8333  | SHORT    | Yahoo Finance |
| BONK-USD   | 2026-06-04 00:00:00 |     4.862e-06 |         -53.8333  | SHORT    | Kraken API    |
| BTC-USD    | 2026-06-04 00:00:00 | 62771.6       |         -49.8333  | SHORT    | Kraken API    |
| COMP-USD   | 2026-06-04 00:00:00 |    17.33      |         -53.3333  | SHORT    | Kraken API    |
| CRV-USD    | 2026-06-04 00:00:00 |     0.1983    |         -51.3333  | SHORT    | Kraken API    |
| DIS        | 2026-06-03 00:00:00 |    99.39      |         -53.75    | SHORT    | Yahoo Finance |
| DOGE-USD   | 2026-06-04 00:00:00 |     0.0894291 |         -49.8333  | SHORT    | Kraken API    |
| ETC-USD    | 2026-06-04 00:00:00 |     7.51      |         -51.8333  | SHORT    | Kraken API    |
| ETH-USD    | 2026-06-04 00:00:00 |  1774.78      |         -48.6667  | SHORT    | Kraken API    |
| FXI        | 2026-06-03 00:00:00 |    35.54      |         -55.0833  | SHORT    | Yahoo Finance |
| LDO-USD    | 2026-06-04 00:00:00 |     0.283     |         -53.8333  | SHORT    | Kraken API    |
| LINK-USD   | 2026-06-04 00:00:00 |     8.0995    |         -51.3333  | SHORT    | Kraken API    |
| LTC-USD    | 2026-06-04 00:00:00 |    45.97      |         -49.8333  | SHORT    | Kraken API    |
| OP-USD     | 2026-06-04 00:00:00 |     0.1161    |         -41.3333  | SHORT    | Kraken API    |
| PEP        | 2026-06-03 00:00:00 |   142.54      |         -38.5833  | SHORT    | Yahoo Finance |
| PEPE-USD   | 2026-06-04 00:00:00 |     3.016e-06 |         -53.8333  | SHORT    | Kraken API    |
| PG         | 2026-06-03 00:00:00 |   140.19      |         -30.25    | SHORT    | Yahoo Finance |
| SHIB-USD   | 2026-06-04 00:00:00 |     5.04e-06  |         -40.8333  | SHORT    | Kraken API    |
| SNX-USD    | 2026-06-04 00:00:00 |     0.2638    |         -50.1667  | SHORT    | Kraken API    |
| SOL-USD    | 2026-06-04 00:00:00 |    69.52      |         -51.8333  | SHORT    | Kraken API    |
| T          | 2026-06-03 00:00:00 |    23.55      |         -48.75    | SHORT    | Yahoo Finance |
| UNI-USD    | 2026-06-04 00:00:00 |     2.698     |         -53.8333  | SHORT    | Kraken API    |
| VIXY       | 2026-06-03 00:00:00 |    23.52      |         -47.5833  | SHORT    | Yahoo Finance |
| WIF-USD    | 2026-06-04 00:00:00 |     0.1774    |         -37.3333  | SHORT    | Kraken API    |
| XLU        | 2026-06-03 00:00:00 |    43.71      |         -44.25    | SHORT    | Yahoo Finance |
| XRP-USD    | 2026-06-04 00:00:00 |     1.17516   |         -49.3333  | SHORT    | Kraken API    |
| YFI-USD    | 2026-06-04 00:00:00 |  2097         |         -49.3333  | SHORT    | Kraken API    |

## Edge Summary

- Symbols with trades: **160** of 160
- Beat buy-and-hold: **33.12%** of traded symbols
- Positive return: **32.50%** of traded symbols
- Median strategy return: **-9.04%** (benchmark **17.19%**)
- Median excess vs benchmark: **-30.90%**
- Median Sharpe: **-0.10**
- Median exposure: **44.71%**

> Edge is real only if both _beat buy-and-hold_ and _median excess_ are convincingly positive across many symbols. Treat a single high-return symbol as noise.

## Portfolio Backtest

Actual capital-allocation books (not per-symbol averages). Benchmarks: `equal_weight_buyhold` (whole tracked universe), `spy_buyhold` (100% SPY), and `sixty_forty` (60% SPY / 40% AGG). `high_conf_voltarget` inverse-vol-weights the HIGH-confidence book; `conviction_long_short` is market-neutral. Judge on **Sharpe** and **max_drawdown** out-of-sample, not raw return: a fully-invested long book wins on return in a bull market but carries all the risk.

| strategy              | scope         | ann_return   | ann_vol   |   sharpe | max_drawdown   | total_return   |   avg_gross_exposure |
|:----------------------|:--------------|:-------------|:----------|---------:|:---------------|:---------------|---------------------:|
| equal_weight_buyhold  | full          | -9.72%       | 33.79%    |    -0.29 | -57.60%        | -37.60%        |                 1    |
| equal_weight_buyhold  | out_of_sample | -17.89%      | 34.36%    |    -0.52 | -39.63%        | -22.43%        |                 1    |
| all_signals_ew        | full          | -6.31%       | 28.07%    |    -0.22 | -60.00%        | -26.86%        |                 1    |
| all_signals_ew        | out_of_sample | 8.77%        | 28.54%    |     0.31 | -32.68%        | 5.18%          |                 1    |
| high_conf_ew          | full          | -0.07%       | 32.27%    |    -0    | -47.47%        | -14.68%        |                 0.89 |
| high_conf_ew          | out_of_sample | 18.39%       | 37.31%    |     0.49 | -20.90%        | 13.16%         |                 0.89 |
| high_conf_voltarget   | full          | 0.20%        | 29.85%    |     0.01 | -40.35%        | -11.94%        |                 0.89 |
| high_conf_voltarget   | out_of_sample | 10.70%       | 35.56%    |     0.3  | -17.06%        | 4.98%          |                 0.89 |
| conviction_long_short | full          | -10.32%      | 23.35%    |    -0.44 | -40.70%        | -32.81%        |                 0.97 |
| conviction_long_short | out_of_sample | -2.04%       | 27.02%    |    -0.08 | -21.14%        | -5.91%         |                 0.97 |
| spy_buyhold           | full          | 9.56%        | 13.24%    |     0.72 | -17.81%        | 30.23%         |                 0.79 |
| spy_buyhold           | out_of_sample | 0.86%        | 9.35%     |     0.09 | -14.83%        | 0.46%          |                 0.79 |
| sixty_forty           | full          | 5.49%        | 8.38%     |     0.66 | -10.80%        | 16.91%         |                 0.79 |
| sixty_forty           | out_of_sample | -0.70%       | 6.05%     |    -0.12 | -10.09%        | -0.94%         |                 0.79 |

## Walk-Forward Robustness

Each book measured across contiguous time folds (each a different regime). A book has durable edge only if `mean_sharpe` is positive, `min_sharpe` isn't deeply negative, and `pct_positive_folds` is high — a single great fold doesn't count. `fold_sharpes` lists each fold oldest-to-newest.

| strategy              |   n_folds |   mean_sharpe |   median_sharpe |   min_sharpe | pct_positive_folds   | mean_return   | fold_sharpes                 |
|:----------------------|----------:|--------------:|----------------:|-------------:|:---------------------|:--------------|:-----------------------------|
| equal_weight_buyhold  |         5 |          0    |           -0.42 |        -0.68 | 20.00%               | -8.40%        | 1.90;-0.68;-0.45;-0.34;-0.42 |
| all_signals_ew        |         5 |          0.01 |           -0.16 |        -2.3  | 40.00%               | -3.47%        | 0.90;-0.16;-0.17;-2.30;1.78  |
| high_conf_ew          |         5 |          0.31 |           -0.34 |        -0.72 | 40.00%               | -1.51%        | 1.75;-0.34;-0.72;-0.61;1.48  |
| high_conf_voltarget   |         5 |          0.39 |           -0.44 |        -0.46 | 40.00%               | -1.65%        | 2.48;-0.46;-0.44;-0.44;0.81  |
| conviction_long_short |         5 |         -0.44 |           -0.64 |        -1.28 | 40.00%               | -7.13%        | -0.64;-0.84;0.06;-1.28;0.49  |
| spy_buyhold           |         5 |          0.81 |            0.75 |         0.02 | 100.00%              | 5.62%         | 2.12;1.12;0.02;0.02;0.75     |
| sixty_forty           |         5 |          0.7  |            0.44 |         0    | 100.00%              | 3.26%         | 2.11;0.89;0.00;0.06;0.44     |

## Strategy Comparison

Each decision rule backtested over the same data. `out_of_sample` is the most recent ~35% of each symbol's history (unseen tail). A rule has real edge only if `median_excess` and `beat_benchmark_pct` stay positive out-of-sample, not just full-sample.

| strategy        | scope         |   symbols | beat_benchmark_pct   | positive_pct   | median_return   | median_benchmark   | median_excess   |   median_sharpe |   total_trades |
|:----------------|:--------------|----------:|:---------------------|:---------------|:----------------|:-------------------|:----------------|----------------:|---------------:|
| trend           | full          |       160 | 33.12%               | 32.50%         | -9.04%          | 17.19%             | -30.90%         |           -0.1  |          11321 |
| trend           | out_of_sample |       160 | 35.62%               | 58.13%         | 4.12%           | 6.79%              | -9.45%          |            0.4  |           3913 |
| mean_reversion  | full          |       159 | 40.25%               | 47.80%         | -0.14%          | 17.04%             | -16.63%         |           -0.04 |           1270 |
| mean_reversion  | out_of_sample |       128 | 48.44%               | 57.03%         | 0.32%           | 1.70%              | -2.73%          |            0.65 |            478 |
| regime_adaptive | full          |       160 | 34.38%               | 33.12%         | -9.04%          | 17.19%             | -31.00%         |           -0.1  |          11599 |
| regime_adaptive | out_of_sample |       160 | 35.00%               | 59.38%         | 4.35%           | 6.79%              | -9.09%          |            0.42 |           4018 |

## Signal Calibration

Realized forward return in the signal's direction, grouped by confidence. HIGH should outrank LOW for the confidence score to be meaningful.

| confidence_level   |   horizon |     n | mean_return   | median_return   | win_rate   |
|:-------------------|----------:|------:|:--------------|:----------------|:-----------|
| HIGH               |         5 |  8112 | 0.16%         | 0.13%           | 52.32%     |
| MEDIUM             |         5 | 29160 | 0.04%         | 0.10%           | 51.18%     |
| LOW                |         5 |  3265 | -0.59%        | -0.48%          | 45.21%     |
| ALL                |         5 | 40537 | 0.02%         | 0.07%           | 50.92%     |
| HIGH               |        10 |  8074 | 0.51%         | 0.19%           | 52.34%     |
| MEDIUM             |        10 | 28868 | 0.19%         | 0.16%           | 51.32%     |
| LOW                |        10 |  3243 | -0.90%        | -0.73%          | 45.21%     |
| ALL                |        10 | 40185 | 0.17%         | 0.12%           | 51.03%     |
| HIGH               |        20 |  7954 | 0.89%         | 0.47%           | 53.75%     |
| MEDIUM             |        20 | 28218 | 0.75%         | 0.60%           | 53.48%     |
| LOW                |        20 |  3197 | -0.79%        | -0.60%          | 46.61%     |
| ALL                |        20 | 39369 | 0.65%         | 0.50%           | 52.98%     |

## Backtest Summary

### Data Quality / Signal Availability

- **ok**: 160 symbols

| symbol     |   trades | return   | benchmark_return   | mdd     |   sharpe | exposure   | skipped_reason   |
|:-----------|---------:|:---------|:-------------------|:--------|---------:|:-----------|:-----------------|
| AAPL       |       67 | 13.01%   | 66.64%             | -20.65% |     0.36 | 49.25%     | ok               |
| AAVE-USD   |       80 | -63.66%  | -77.56%            | -69.30% |    -0.83 | 35.06%     | ok               |
| ABBV       |       64 | -18.32%  | 31.68%             | -30.55% |    -0.39 | 49.25%     | ok               |
| ADA-USD    |       86 | -85.23%  | -77.48%            | -91.71% |    -0.78 | 45.59%     | ok               |
| ADBE       |       66 | -22.69%  | -56.65%            | -38.01% |    -0.23 | 56.91%     | ok               |
| AGG        |       69 | -7.13%   | 0.14%              | -9.93%  |    -1.17 | 31.11%     | ok               |
| ALGO-USD   |       84 | -52.60%  | -68.25%            | -61.76% |    -0.61 | 38.31%     | ok               |
| AMAT       |       67 | -19.38%  | 234.27%            | -57.80% |    -0.1  | 53.58%     | ok               |
| AMD        |       56 | 52.12%   | 265.23%            | -47.17% |     0.63 | 38.94%     | ok               |
| AMGN       |       71 | -17.88%  | 11.05%             | -34.14% |    -0.34 | 49.42%     | ok               |
| AMZN       |       74 | -33.84%  | 62.64%             | -42.48% |    -0.99 | 38.27%     | ok               |
| APT-USD    |       80 | -47.48%  | -91.19%            | -69.96% |    -0.32 | 42.34%     | ok               |
| ARB-USD    |       74 | 1.90%    | -87.72%            | -61.76% |     0.26 | 38.51%     | ok               |
| ARKK       |       79 | -30.02%  | 58.38%             | -32.63% |    -0.5  | 38.94%     | ok               |
| ATOM-USD   |       90 | -64.27%  | -71.39%            | -68.90% |    -1.05 | 43.30%     | ok               |
| AVAX-USD   |       72 | -38.39%  | -78.23%            | -53.72% |    -0.35 | 36.97%     | ok               |
| AVGO       |       60 | 47.42%   | 343.50%            | -35.76% |     0.63 | 47.09%     | ok               |
| BA         |       69 | 1.80%    | -7.58%             | -30.56% |     0.16 | 51.25%     | ok               |
| BAC        |       80 | -18.78%  | 55.95%             | -27.64% |    -0.48 | 45.59%     | ok               |
| BCH-USD    |       80 | -29.96%  | -46.86%            | -58.22% |    -0.22 | 45.79%     | ok               |
| BITO       |       76 | 3.90%    | -60.20%            | -42.82% |     0.22 | 38.77%     | ok               |
| BLK        |       75 | -1.36%   | 25.05%             | -20.81% |     0.03 | 42.10%     | ok               |
| BND        |       65 | -7.32%   | 0.18%              | -9.89%  |    -1.18 | 32.28%     | ok               |
| BONK-USD   |       70 | 67.15%   | -84.30%            | -43.77% |     0.71 | 40.42%     | ok               |
| BTC-USD    |       74 | -0.33%   | -32.22%            | -30.44% |     0.14 | 50.96%     | ok               |
| C          |       83 | -28.26%  | 145.06%            | -36.36% |    -0.56 | 51.08%     | ok               |
| CAT        |       74 | 28.31%   | 215.73%            | -21.02% |     0.54 | 57.74%     | ok               |
| CL         |       60 | 20.02%   | 5.36%              | -14.32% |     0.66 | 49.42%     | ok               |
| CMCSA      |       80 | -36.01%  | -42.28%            | -39.80% |    -0.9  | 44.26%     | ok               |
| COMP-USD   |       93 | -42.79%  | -77.14%            | -63.55% |    -0.31 | 44.83%     | ok               |
| COP        |       79 | -25.85%  | 7.08%              | -43.99% |    -0.49 | 41.93%     | ok               |
| COST       |       62 | 8.46%    | 42.97%             | -29.73% |     0.31 | 47.42%     | ok               |
| CRM        |       67 | -33.60%  | -27.83%            | -41.46% |    -0.66 | 44.09%     | ok               |
| CRV-USD    |       62 | 6.45%    | -78.68%            | -39.89% |     0.29 | 31.99%     | ok               |
| CSCO       |       59 | 31.43%   | 151.79%            | -21.79% |     0.65 | 48.75%     | ok               |
| CVX        |       73 | -19.31%  | 31.29%             | -29.70% |    -0.52 | 41.76%     | ok               |
| DASH-USD   |       65 | -44.95%  | -3.38%             | -64.43% |    -0.06 | 30.46%     | ok               |
| DBC        |       62 | -14.35%  | 38.82%             | -25.86% |    -0.5  | 33.11%     | ok               |
| DE         |       76 | -9.23%   | 49.42%             | -25.24% |    -0.12 | 45.26%     | ok               |
| DIA        |       58 | -2.19%   | 34.83%             | -12.94% |    -0.08 | 45.92%     | ok               |
| DIS        |       59 | 2.59%    | 11.31%             | -22.67% |     0.16 | 47.42%     | ok               |
| DOGE-USD   |       77 | -15.19%  | -71.46%            | -60.95% |     0.11 | 49.04%     | ok               |
| DOT-USD    |       90 | -48.72%  | -83.99%            | -59.09% |    -0.38 | 46.93%     | ok               |
| DXY-INDEX  |       44 | -3.86%   | -3.16%             | -6.06%  |    -0.63 | 27.11%     | ok               |
| EEM        |       64 | -9.40%   | 79.74%             | -25.67% |    -0.25 | 43.43%     | ok               |
| EFA        |       58 | -8.43%   | 39.25%             | -13.53% |    -0.31 | 43.59%     | ok               |
| EOG        |       83 | -29.95%  | 23.05%             | -48.13% |    -0.69 | 47.75%     | ok               |
| ETC-USD    |       68 | -45.03%  | -70.44%            | -54.24% |    -0.75 | 30.27%     | ok               |
| ETH-USD    |       62 | 139.08%  | -47.11%            | -30.11% |     1.21 | 43.68%     | ok               |
| EWJ        |       64 | -18.27%  | 44.04%             | -30.73% |    -0.59 | 41.43%     | ok               |
| FCX        |       73 | -29.82%  | 71.04%             | -48.31% |    -0.36 | 45.59%     | ok               |
| FET-USD    |       77 | -9.47%   | -80.93%            | -48.39% |     0.2  | 39.85%     | ok               |
| FIL-USD    |       70 | -27.40%  | -81.89%            | -47.25% |    -0.17 | 32.95%     | ok               |
| FXI        |       46 | -13.50%  | 58.03%             | -23.91% |    -0.27 | 26.62%     | ok               |
| GDX        |       60 | 5.77%    | 192.00%            | -34.99% |     0.22 | 49.08%     | ok               |
| GDXJ       |       68 | -21.59%  | 212.51%            | -44.93% |    -0.21 | 46.59%     | ok               |
| GE         |       74 | 5.64%    | 203.97%            | -27.82% |     0.22 | 51.41%     | ok               |
| GLD        |       48 | 19.09%   | 117.53%            | -16.63% |     0.54 | 43.43%     | ok               |
| GOOGL      |       65 | 79.11%   | 152.31%            | -20.41% |     1.16 | 55.24%     | ok               |
| GRT-USD    |       89 | -25.94%  | -89.04%            | -57.25% |    -0.1  | 41.00%     | ok               |
| GS         |       78 | -1.62%   | 172.55%            | -22.13% |     0.06 | 50.58%     | ok               |
| HD         |       69 | -4.53%   | -12.28%            | -17.69% |    -0.04 | 45.09%     | ok               |
| HON        |       95 | -23.99%  | 17.04%             | -28.64% |    -0.66 | 52.08%     | ok               |
| HYG        |       81 | -9.36%   | 2.99%              | -9.72%  |    -1.09 | 34.44%     | ok               |
| IBIT       |       30 | 35.78%   | -2.66%             | -18.95% |     0.79 | 29.18%     | ok               |
| IBM        |       72 | 48.07%   | 89.56%             | -25.31% |     0.89 | 50.92%     | ok               |
| ICP-USD    |       83 | 3.35%    | -70.85%            | -54.72% |     0.29 | 37.93%     | ok               |
| IEF        |       78 | -11.43%  | -1.53%             | -12.27% |    -1.6  | 33.11%     | ok               |
| IEMG       |       58 | -5.52%   | 73.07%             | -26.84% |    -0.12 | 43.59%     | ok               |
| INJ-USD    |       79 | -57.82%  | -68.33%            | -80.14% |    -0.61 | 39.08%     | ok               |
| INTC       |       70 | 55.76%   | 137.43%            | -60.60% |     0.62 | 49.58%     | ok               |
| INTU       |       67 | -15.49%  | -48.84%            | -43.77% |    -0.15 | 42.76%     | ok               |
| ITA        |       70 | 0.26%    | 83.94%             | -23.75% |     0.08 | 45.92%     | ok               |
| IWM        |       50 | 8.72%    | 47.46%             | -12.83% |     0.36 | 37.10%     | ok               |
| JNJ        |       76 | 2.83%    | 37.91%             | -17.51% |     0.16 | 51.41%     | ok               |
| JPM        |       77 | -24.55%  | 75.92%             | -33.04% |    -0.65 | 52.58%     | ok               |
| KO         |       49 | 23.27%   | 30.83%             | -8.07%  |     0.88 | 37.27%     | ok               |
| LDO-USD    |       78 | -5.65%   | -84.91%            | -58.32% |     0.22 | 36.97%     | ok               |
| LIN        |       72 | -3.07%   | 25.05%             | -21.53% |    -0.05 | 39.27%     | ok               |
| LINK-USD   |       72 | -19.12%  | -60.64%            | -55.61% |     0.03 | 40.42%     | ok               |
| LLY        |       69 | -15.20%  | 71.18%             | -53.34% |    -0.13 | 51.41%     | ok               |
| LRCX       |       80 | -15.61%  | 358.47%            | -63.56% |    -0.06 | 45.92%     | ok               |
| LTC-USD    |       68 | -40.05%  | -53.67%            | -55.90% |    -0.4  | 47.32%     | ok               |
| MCD        |       75 | -3.01%   | -7.07%             | -19.14% |    -0.07 | 38.77%     | ok               |
| META       |       74 | -9.91%   | 68.16%             | -38.94% |    -0.03 | 52.08%     | ok               |
| MPC        |       71 | -13.74%  | 74.83%             | -44.76% |    -0.14 | 49.92%     | ok               |
| MRK        |       67 | -21.75%  | -3.50%             | -32.14% |    -0.47 | 47.09%     | ok               |
| MS         |       79 | -16.14%  | 129.71%            | -26.72% |    -0.35 | 46.76%     | ok               |
| MSFT       |       76 | -31.24%  | 11.64%             | -35.58% |    -0.81 | 47.59%     | ok               |
| MU         |       55 | 246.62%  | 1210.48%           | -68.76% |     1.34 | 58.57%     | ok               |
| NEAR-USD   |       91 | -13.24%  | -46.72%            | -60.07% |     0.13 | 43.10%     | ok               |
| NEM        |       70 | -19.45%  | 183.19%            | -38.49% |    -0.12 | 55.74%     | ok               |
| NFLX       |       62 | 22.67%   | 70.43%             | -21.09% |     0.54 | 54.41%     | ok               |
| NKE        |       91 | -35.66%  | -57.78%            | -55.35% |    -0.48 | 45.26%     | ok               |
| NOW        |       78 | 26.78%   | -17.47%            | -31.32% |     0.48 | 46.09%     | ok               |
| NVDA       |       74 | -24.95%  | 145.35%            | -45.02% |    -0.16 | 60.96%     | ok               |
| OP-USD     |       76 | -7.53%   | -93.62%            | -70.11% |     0.17 | 35.44%     | ok               |
| ORCL       |       70 | 74.51%   | 121.64%            | -29.47% |     0.77 | 52.41%     | ok               |
| OXY        |       69 | -0.54%   | 5.00%              | -31.73% |     0.11 | 43.59%     | ok               |
| PEP        |       85 | -9.80%   | -14.61%            | -21.35% |    -0.23 | 49.08%     | ok               |
| PEPE-USD   |       79 | -0.37%   | -83.61%            | -57.66% |     0.27 | 42.72%     | ok               |
| PFE        |       77 | -38.05%  | -12.59%            | -42.29% |    -1.18 | 37.27%     | ok               |
| PG         |       63 | -9.53%   | -6.50%             | -20.33% |    -0.34 | 40.60%     | ok               |
| PM         |       81 | -0.11%   | 86.24%             | -33.68% |     0.09 | 56.91%     | ok               |
| POL-USD    |       82 | 46.77%   | -80.28%            | -46.45% |     0.64 | 47.51%     | ok               |
| QCOM       |       81 | -1.74%   | 79.46%             | -57.69% |     0.14 | 48.59%     | ok               |
| QQQ        |       60 | 24.07%   | 82.18%             | -12.88% |     0.67 | 46.26%     | ok               |
| RENDER-USD |       94 | -8.22%   | -50.24%            | -45.00% |     0.21 | 44.99%     | ok               |
| RTX        |       58 | 18.28%   | 100.45%            | -16.99% |     0.5  | 52.08%     | ok               |
| SBUX       |       65 | -23.13%  | 2.56%              | -31.15% |    -0.46 | 40.27%     | ok               |
| SCHW       |       74 | -21.97%  | 31.56%             | -30.41% |    -0.52 | 45.42%     | ok               |
| SHIB-USD   |       78 | -35.46%  | -76.11%            | -48.95% |    -0.26 | 51.15%     | ok               |
| SHY        |       50 | -2.06%   | -0.01%             | -2.85%  |    -0.7  | 36.77%     | ok               |
| SKY-USD    |       66 | -29.93%  | 15.49%             | -43.98% |    -0.42 | 39.32%     | ok               |
| SLB        |       77 | -31.95%  | 17.34%             | -54.23% |    -0.58 | 51.58%     | ok               |
| SLV        |       58 | 36.93%   | 216.19%            | -42.66% |     0.58 | 40.60%     | ok               |
| SMH        |       50 | 96.53%   | 269.63%            | -33.99% |     1.2  | 51.75%     | ok               |
| SNX-USD    |       67 | 16.03%   | -86.69%            | -32.91% |     0.39 | 39.46%     | ok               |
| SOL-USD    |       70 | -39.19%  | -63.61%            | -56.90% |    -0.18 | 59.00%     | ok               |
| SOXX       |       57 | 87.35%   | 231.13%            | -40.34% |     1.07 | 50.92%     | ok               |
| SPY        |       60 | 9.22%    | 58.27%             | -16.47% |     0.37 | 50.92%     | ok               |
| SUSHI-USD  |       94 | -81.52%  | -83.77%            | -82.20% |    -1.31 | 35.63%     | ok               |
| T          |       66 | 23.16%   | 39.60%             | -17.01% |     0.6  | 49.25%     | ok               |
| TGT        |       58 | -13.41%  | -13.39%            | -40.57% |    -0.2  | 39.10%     | ok               |
| TIA-USD    |       80 | -7.89%   | -92.65%            | -54.78% |     0.17 | 32.76%     | ok               |
| TLT        |       74 | -22.24%  | -11.29%            | -24.21% |    -1.6  | 33.61%     | ok               |
| TMO        |       57 | 19.54%   | -12.87%            | -16.83% |     0.48 | 49.75%     | ok               |
| TMUS       |       68 | 19.76%   | 11.12%             | -24.50% |     0.5  | 48.75%     | ok               |
| TRX-USD    |       70 | -2.64%   | 30.59%             | -22.90% |     0.03 | 49.23%     | ok               |
| TSLA       |       68 | 8.00%    | 81.11%             | -57.89% |     0.29 | 44.09%     | ok               |
| TXN        |       77 | -8.85%   | 84.51%             | -46.98% |     0.01 | 53.08%     | ok               |
| UNH        |       78 | 14.89%   | -29.88%            | -32.44% |     0.35 | 51.91%     | ok               |
| UNI-USD    |       92 | -67.95%  | -79.76%            | -79.17% |    -0.73 | 40.23%     | ok               |
| UPS        |       66 | -35.17%  | -32.60%            | -40.62% |    -0.71 | 38.27%     | ok               |
| USO        |       68 | 2.80%    | 111.63%            | -43.35% |     0.17 | 34.44%     | ok               |
| VEA        |       60 | -2.87%   | 51.04%             | -19.49% |    -0.07 | 43.43%     | ok               |
| VIXY       |       92 | -77.64%  | -59.84%            | -87.63% |    -0.93 | 31.11%     | ok               |
| VNQ        |       77 | -17.89%  | 8.07%              | -24.92% |    -0.76 | 37.77%     | ok               |
| VTI        |       70 | 0.00%    | 56.66%             | -18.77% |     0.06 | 52.25%     | ok               |
| VWO        |       76 | -13.41%  | 50.64%             | -25.20% |    -0.47 | 44.09%     | ok               |
| VZ         |       83 | -19.60%  | 19.37%             | -31.88% |    -0.57 | 39.60%     | ok               |
| WFC        |       84 | -22.02%  | 60.31%             | -30.22% |    -0.41 | 46.92%     | ok               |
| WIF-USD    |       72 | -40.91%  | -90.27%            | -50.40% |    -0.19 | 31.03%     | ok               |
| WMT        |       55 | 33.27%   | 117.42%            | -21.31% |     0.87 | 53.24%     | ok               |
| XBI        |       64 | -8.52%   | 40.31%             | -21.75% |    -0.13 | 40.10%     | ok               |
| XLB        |       68 | -10.36%  | 23.49%             | -24.41% |    -0.34 | 36.94%     | ok               |
| XLC        |       63 | 19.23%   | 52.10%             | -12.33% |     0.64 | 56.74%     | ok               |
| XLE        |       79 | -10.96%  | 43.99%             | -37.17% |    -0.21 | 46.92%     | ok               |
| XLF        |       76 | -11.69%  | 34.54%             | -23.61% |    -0.38 | 49.42%     | ok               |
| XLI        |       66 | 5.40%    | 54.88%             | -11.38% |     0.26 | 47.75%     | ok               |
| XLK        |       40 | 86.10%   | 105.85%            | -14.75% |     1.52 | 48.92%     | ok               |
| XLM-USD    |       69 | 12.32%   | -39.20%            | -45.54% |     0.35 | 47.51%     | ok               |
| XLP        |       72 | 6.07%    | 13.20%             | -10.28% |     0.37 | 43.93%     | ok               |
| XLU        |       69 | -5.60%   | 35.62%             | -15.29% |    -0.21 | 38.60%     | ok               |
| XLV        |       66 | -9.35%   | 4.67%              | -14.23% |    -0.44 | 37.44%     | ok               |
| XLY        |       76 | -0.80%   | 32.41%             | -14.01% |     0.04 | 44.59%     | ok               |
| XOM        |       61 | -0.77%   | 54.55%             | -20.29% |     0.05 | 36.77%     | ok               |
| XRP-USD    |       64 | -38.69%  | -42.80%            | -54.34% |    -0.41 | 35.44%     | ok               |
| YFI-USD    |       85 | -56.42%  | -74.59%            | -67.78% |    -0.91 | 39.08%     | ok               |
| ZEC-USD    |       67 | 46.51%   | 946.09%            | -46.93% |     0.57 | 36.40%     | ok               |

## AAPL Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 25.69%   | 66.64%             | -21.71% |     0.56 |       69 | 53.74%     | ok               |
|          15 | 21.46%   | 66.64%             | -23.86% |     0.49 |       75 | 61.23%     | ok               |
|          25 | 19.68%   | 66.64%             | -20.03% |     0.47 |       67 | 51.58%     | ok               |
|          30 | 13.01%   | 66.64%             | -20.65% |     0.36 |       67 | 49.25%     | ok               |
|          35 | 10.41%   | 66.64%             | -22.04% |     0.31 |       63 | 46.26%     | ok               |

## AAVE-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -3.10%   | -77.56%            | -43.61% |     0.17 |       38 | 27.78%     | ok               |
|          45 | -3.53%   | -77.56%            | -46.87% |     0.16 |       36 | 24.90%     | ok               |
|          35 | -27.13%  | -77.56%            | -51.96% |    -0.15 |       52 | 30.46%     | ok               |
|          50 | -33.42%  | -77.56%            | -47.78% |    -0.37 |       38 | 19.35%     | ok               |
|          15 | -59.90%  | -77.56%            | -66.51% |    -0.52 |       82 | 48.85%     | ok               |

## ABBV Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -5.79%   | 31.68%             | -26.16% |    -0.07 |       50 | 38.94%     | ok               |
|          40 | -14.93%  | 31.68%             | -26.61% |    -0.32 |       64 | 43.59%     | ok               |
|          35 | -16.15%  | 31.68%             | -27.83% |    -0.34 |       66 | 46.42%     | ok               |
|          30 | -18.32%  | 31.68%             | -30.55% |    -0.39 |       64 | 49.25%     | ok               |
|          45 | -17.58%  | 31.68%             | -29.59% |    -0.4  |       54 | 40.93%     | ok               |

## ADA-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -85.94%  | -77.48%            | -91.83% |    -0.67 |       82 | 61.11%     | ok               |
|          20 | -85.94%  | -77.48%            | -92.33% |    -0.69 |       86 | 56.32%     | ok               |
|          25 | -87.19%  | -77.48%            | -92.37% |    -0.78 |       85 | 52.87%     | ok               |
|          30 | -85.23%  | -77.48%            | -91.71% |    -0.78 |       86 | 45.59%     | ok               |
|          45 | -83.64%  | -77.48%            | -89.92% |    -0.78 |       62 | 30.84%     | ok               |

## ADBE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 10.63%   | -56.65%            | -21.34% |     0.3  |       76 | 49.25%     | ok               |
|          40 | -3.65%   | -56.65%            | -20.88% |     0.05 |       72 | 42.26%     | ok               |
|          25 | -9.10%   | -56.65%            | -32.60% |     0.01 |       50 | 61.23%     | ok               |
|          15 | -18.75%  | -56.65%            | -33.11% |    -0.14 |       59 | 65.89%     | ok               |
|          20 | -20.39%  | -56.65%            | -35.67% |    -0.17 |       50 | 63.39%     | ok               |

## AGG Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -5.75%   | 0.14%              | -7.89%  |    -1.16 |       52 | 20.47%     | ok               |
|          30 | -7.13%   | 0.14%              | -9.93%  |    -1.17 |       69 | 31.11%     | ok               |
|          20 | -8.23%   | 0.14%              | -10.85% |    -1.2  |       75 | 36.94%     | ok               |
|          50 | -5.57%   | 0.14%              | -7.92%  |    -1.25 |       46 | 16.97%     | ok               |
|          25 | -8.51%   | 0.14%              | -11.38% |    -1.29 |       73 | 35.11%     | ok               |

## ALGO-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -52.60%  | -68.25%            | -61.76% |    -0.61 |       84 | 38.31%     | ok               |
|          15 | -62.17%  | -68.25%            | -71.55% |    -0.68 |       82 | 50.00%     | ok               |
|          25 | -63.01%  | -68.25%            | -75.73% |    -0.75 |       86 | 45.40%     | ok               |
|          20 | -66.18%  | -68.25%            | -74.61% |    -0.81 |       86 | 47.89%     | ok               |
|          35 | -55.82%  | -68.25%            | -58.56% |    -0.81 |       62 | 31.23%     | ok               |

## AMAT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -5.33%   | 234.27%            | -54.69% |     0.12 |       66 | 62.40%     | ok               |
|          30 | -19.38%  | 234.27%            | -57.80% |    -0.1  |       67 | 53.58%     | ok               |
|          20 | -25.27%  | 234.27%            | -60.72% |    -0.17 |       70 | 58.74%     | ok               |
|          35 | -25.12%  | 234.27%            | -55.89% |    -0.21 |       69 | 51.41%     | ok               |
|          25 | -28.77%  | 234.27%            | -60.95% |    -0.25 |       69 | 56.41%     | ok               |

## AMD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 52.12%   | 265.23%            | -47.17% |     0.63 |       56 | 38.94%     | ok               |
|          50 | 42.17%   | 265.23%            | -48.79% |     0.57 |       60 | 33.44%     | ok               |
|          35 | 32.72%   | 265.23%            | -54.57% |     0.5  |       62 | 40.93%     | ok               |
|          45 | 21.53%   | 265.23%            | -56.22% |     0.41 |       64 | 36.27%     | ok               |
|          30 | 15.22%   | 265.23%            | -59.88% |     0.36 |       63 | 43.43%     | ok               |

## AMGN Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -12.45%  | 11.05%             | -26.64% |    -0.18 |       73 | 55.57%     | ok               |
|          35 | -13.85%  | 11.05%             | -31.23% |    -0.24 |       67 | 45.59%     | ok               |
|          15 | -16.13%  | 11.05%             | -27.92% |    -0.25 |       71 | 61.40%     | ok               |
|          30 | -17.88%  | 11.05%             | -34.14% |    -0.34 |       71 | 49.42%     | ok               |
|          25 | -21.22%  | 11.05%             | -33.41% |    -0.41 |       67 | 51.75%     | ok               |

## AMZN Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -17.83%  | 62.64%             | -28.70% |    -0.52 |       50 | 29.78%     | ok               |
|          50 | -25.03%  | 62.64%             | -35.48% |    -0.88 |       48 | 24.13%     | ok               |
|          45 | -25.89%  | 62.64%             | -35.47% |    -0.89 |       50 | 26.96%     | ok               |
|          35 | -29.70%  | 62.64%             | -38.29% |    -0.91 |       62 | 32.95%     | ok               |
|          30 | -33.84%  | 62.64%             | -42.48% |    -0.99 |       74 | 38.27%     | ok               |

## APT-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 34.42%   | -91.19%            | -46.73% |     0.58 |       44 | 18.97%     | ok               |
|          45 | -9.33%   | -91.19%            | -63.86% |     0.09 |       62 | 25.29%     | ok               |
|          40 | -30.95%  | -91.19%            | -63.33% |    -0.16 |       70 | 31.03%     | ok               |
|          20 | -41.49%  | -91.19%            | -70.51% |    -0.19 |       75 | 50.77%     | ok               |
|          35 | -35.90%  | -91.19%            | -64.45% |    -0.19 |       74 | 36.59%     | ok               |

## ARB-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 53.77%   | -87.72%            | -52.62% |     0.64 |       91 | 54.98%     | ok               |
|          40 | 41.89%   | -87.72%            | -45.37% |     0.59 |       52 | 29.31%     | ok               |
|          35 | 30.33%   | -87.72%            | -54.93% |     0.5  |       66 | 33.14%     | ok               |
|          20 | 28.63%   | -87.72%            | -59.44% |     0.49 |       79 | 49.43%     | ok               |
|          45 | 17.62%   | -87.72%            | -49.55% |     0.39 |       58 | 22.61%     | ok               |

## ARKK Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -30.32%  | 58.38%             | -36.91% |    -0.41 |       96 | 50.92%     | ok               |
|          20 | -30.68%  | 58.38%             | -34.90% |    -0.44 |       87 | 45.76%     | ok               |
|          30 | -30.02%  | 58.38%             | -32.63% |    -0.5  |       79 | 38.94%     | ok               |
|          35 | -31.21%  | 58.38%             | -33.79% |    -0.56 |       78 | 36.61%     | ok               |
|          40 | -32.66%  | 58.38%             | -34.78% |    -0.64 |       70 | 31.78%     | ok               |

## ATOM-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -62.55%  | -71.39%            | -68.50% |    -0.93 |       95 | 49.81%     | ok               |
|          15 | -67.11%  | -71.39%            | -74.68% |    -0.97 |       96 | 60.15%     | ok               |
|          30 | -64.27%  | -71.39%            | -68.90% |    -1.05 |       90 | 43.30%     | ok               |
|          20 | -70.55%  | -71.39%            | -74.33% |    -1.15 |      105 | 54.21%     | ok               |
|          35 | -64.84%  | -71.39%            | -64.84% |    -1.2  |       80 | 38.31%     | ok               |

## AVAX-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 2.34%    | -78.23%            | -29.53% |     0.2  |       34 | 18.77%     | ok               |
|          40 | -0.42%   | -78.23%            | -32.96% |     0.17 |       42 | 24.33%     | ok               |
|          45 | -0.79%   | -78.23%            | -32.82% |     0.16 |       36 | 21.65%     | ok               |
|          35 | -7.59%   | -78.23%            | -36.30% |     0.1  |       60 | 29.69%     | ok               |
|          15 | -19.20%  | -78.23%            | -50.68% |     0.04 |       65 | 50.96%     | ok               |

## AVGO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 47.42%   | 343.50%            | -35.76% |     0.63 |       60 | 47.09%     | ok               |
|          25 | 42.18%   | 343.50%            | -38.01% |     0.59 |       64 | 47.75%     | ok               |
|          35 | 34.97%   | 343.50%            | -36.19% |     0.53 |       70 | 44.26%     | ok               |
|          40 | 29.71%   | 343.50%            | -40.70% |     0.48 |       62 | 40.93%     | ok               |
|          20 | 28.75%   | 343.50%            | -40.10% |     0.47 |       72 | 50.58%     | ok               |

## BA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 18.43%   | -7.58%             | -15.40% |     0.51 |       46 | 31.78%     | ok               |
|          35 | 23.42%   | -7.58%             | -23.77% |     0.49 |       74 | 46.59%     | ok               |
|          25 | 4.84%    | -7.58%             | -32.48% |     0.21 |       72 | 54.74%     | ok               |
|          40 | 4.31%    | -7.58%             | -29.44% |     0.19 |       52 | 40.10%     | ok               |
|          30 | 1.80%    | -7.58%             | -30.56% |     0.16 |       69 | 51.25%     | ok               |

## BAC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -13.76%  | 55.95%             | -21.48% |    -0.27 |       82 | 50.58%     | ok               |
|          45 | -11.75%  | 55.95%             | -22.29% |    -0.34 |       62 | 33.78%     | ok               |
|          35 | -14.47%  | 55.95%             | -29.13% |    -0.38 |       72 | 41.76%     | ok               |
|          15 | -19.06%  | 55.95%             | -23.70% |    -0.4  |       82 | 56.24%     | ok               |
|          50 | -13.19%  | 55.95%             | -20.82% |    -0.42 |       60 | 30.62%     | ok               |

## BCH-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -29.96%  | -46.86%            | -58.22% |    -0.22 |       80 | 45.79%     | ok               |
|          15 | -34.39%  | -46.86%            | -61.84% |    -0.22 |       87 | 57.09%     | ok               |
|          20 | -33.29%  | -46.86%            | -59.43% |    -0.23 |       80 | 52.49%     | ok               |
|          25 | -35.12%  | -46.86%            | -61.30% |    -0.28 |       74 | 48.08%     | ok               |
|          40 | -35.41%  | -46.86%            | -62.46% |    -0.37 |       65 | 38.70%     | ok               |

## BITO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 17.67%   | -60.20%            | -32.29% |     0.38 |       52 | 24.13%     | ok               |
|          30 | 3.90%    | -60.20%            | -42.82% |     0.22 |       76 | 38.77%     | ok               |
|          15 | -2.62%   | -60.20%            | -48.38% |     0.17 |       85 | 47.59%     | ok               |
|          45 | -1.86%   | -60.20%            | -43.53% |     0.13 |       56 | 27.12%     | ok               |
|          25 | -4.32%   | -60.20%            | -41.73% |     0.13 |       80 | 41.76%     | ok               |

## BLK Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 5.32%    | 25.05%             | -14.19% |     0.23 |       80 | 38.27%     | ok               |
|          40 | 4.17%    | 25.05%             | -15.20% |     0.2  |       72 | 33.94%     | ok               |
|          20 | 0.97%    | 25.05%             | -17.89% |     0.1  |       77 | 46.92%     | ok               |
|          30 | -1.36%   | 25.05%             | -20.81% |     0.03 |       75 | 42.10%     | ok               |
|          25 | -2.35%   | 25.05%             | -19.84% |     0.01 |       75 | 44.43%     | ok               |

## BND Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -7.29%   | 0.18%              | -9.32%  |    -1.05 |       67 | 38.77%     | ok               |
|          30 | -7.32%   | 0.18%              | -9.89%  |    -1.18 |       65 | 32.28%     | ok               |
|          25 | -7.86%   | 0.18%              | -10.40% |    -1.19 |       69 | 36.11%     | ok               |
|          15 | -9.30%   | 0.18%              | -10.85% |    -1.33 |       75 | 41.60%     | ok               |
|          45 | -7.22%   | 0.18%              | -9.57%  |    -1.39 |       50 | 22.13%     | ok               |

## BONK-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 140.22%  | -84.30%            | -35.57% |     1.13 |       46 | 21.46%     | ok               |
|          20 | 177.38%  | -84.30%            | -54.25% |     1.05 |       68 | 51.34%     | ok               |
|          25 | 158.79%  | -84.30%            | -46.61% |     1.01 |       67 | 46.55%     | ok               |
|          15 | 168.34%  | -84.30%            | -62.48% |     1    |       69 | 55.75%     | ok               |
|          40 | 79.90%   | -84.30%            | -48.74% |     0.78 |       52 | 32.38%     | ok               |

## BTC-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 48.37%   | -32.22%            | -18.97% |     0.87 |       46 | 33.14%     | ok               |
|          45 | 44.86%   | -32.22%            | -19.59% |     0.87 |       44 | 29.50%     | ok               |
|          35 | 28.23%   | -32.22%            | -31.52% |     0.58 |       70 | 40.23%     | ok               |
|          50 | 14.92%   | -32.22%            | -17.58% |     0.41 |       40 | 25.29%     | ok               |
|          30 | 10.10%   | -32.22%            | -27.92% |     0.3  |       72 | 47.13%     | ok               |

## C Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -13.17%  | 145.06%            | -22.28% |    -0.32 |       68 | 35.27%     | ok               |
|          15 | -25.96%  | 145.06%            | -34.03% |    -0.45 |       76 | 59.73%     | ok               |
|          25 | -24.63%  | 145.06%            | -33.47% |    -0.46 |       75 | 52.91%     | ok               |
|          20 | -26.52%  | 145.06%            | -34.53% |    -0.49 |       81 | 56.07%     | ok               |
|          45 | -22.24%  | 145.06%            | -29.85% |    -0.56 |       82 | 39.93%     | ok               |

## CAT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 28.31%   | 215.73%            | -21.02% |     0.54 |       74 | 57.74%     | ok               |
|          25 | 28.43%   | 215.73%            | -26.37% |     0.54 |       70 | 60.57%     | ok               |
|          20 | 25.83%   | 215.73%            | -25.65% |     0.5  |       80 | 63.89%     | ok               |
|          45 | 20.09%   | 215.73%            | -28.85% |     0.45 |       58 | 46.09%     | ok               |
|          50 | 17.50%   | 215.73%            | -26.39% |     0.41 |       60 | 43.59%     | ok               |

## CL Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 20.02%   | 5.36%              | -14.32% |     0.66 |       60 | 49.42%     | ok               |
|          50 | 15.26%   | 5.36%              | -12.98% |     0.63 |       44 | 33.11%     | ok               |
|          45 | 15.52%   | 5.36%              | -13.51% |     0.62 |       46 | 36.11%     | ok               |
|          35 | 14.30%   | 5.36%              | -13.83% |     0.52 |       62 | 45.76%     | ok               |
|          40 | 10.99%   | 5.36%              | -12.70% |     0.45 |       56 | 40.43%     | ok               |

## CMCSA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -34.99%  | -42.28%            | -49.03% |    -0.77 |       88 | 58.74%     | ok               |
|          30 | -36.01%  | -42.28%            | -39.80% |    -0.9  |       80 | 44.26%     | ok               |
|          20 | -42.09%  | -42.28%            | -47.23% |    -1.05 |       93 | 54.91%     | ok               |
|          25 | -41.18%  | -42.28%            | -44.66% |    -1.06 |       87 | 49.08%     | ok               |
|          50 | -29.51%  | -42.28%            | -33.68% |    -1.08 |       50 | 17.14%     | ok               |

## COMP-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -16.90%  | -77.14%            | -38.71% |    -0.03 |       48 | 20.50%     | ok               |
|          25 | -43.76%  | -77.14%            | -63.29% |    -0.29 |       93 | 50.19%     | ok               |
|          30 | -42.79%  | -77.14%            | -63.55% |    -0.31 |       93 | 44.83%     | ok               |
|          15 | -51.84%  | -77.14%            | -67.05% |    -0.38 |      109 | 61.88%     | ok               |
|          40 | -42.52%  | -77.14%            | -47.33% |    -0.41 |       76 | 32.95%     | ok               |

## COP Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -15.08%  | 7.08%              | -34.85% |    -0.28 |       52 | 28.29%     | ok               |
|          45 | -22.47%  | 7.08%              | -41.14% |    -0.48 |       64 | 31.11%     | ok               |
|          35 | -25.34%  | 7.08%              | -43.91% |    -0.49 |       77 | 38.27%     | ok               |
|          30 | -25.85%  | 7.08%              | -43.99% |    -0.49 |       79 | 41.93%     | ok               |
|          25 | -33.34%  | 7.08%              | -49.23% |    -0.66 |       88 | 46.09%     | ok               |

## COST Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | 20.60%   | 42.97%             | -24.73% |     0.61 |       63 | 50.92%     | ok               |
|          20 | 19.97%   | 42.97%             | -24.32% |     0.58 |       64 | 53.41%     | ok               |
|          35 | 13.66%   | 42.97%             | -26.58% |     0.46 |       56 | 44.43%     | ok               |
|          30 | 8.46%    | 42.97%             | -29.73% |     0.31 |       62 | 47.42%     | ok               |
|          40 | 6.68%    | 42.97%             | -28.41% |     0.27 |       58 | 41.43%     | ok               |

## CRM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -28.31%  | -27.83%            | -38.20% |    -0.4  |       92 | 55.57%     | ok               |
|          35 | -22.69%  | -27.83%            | -36.72% |    -0.41 |       64 | 39.27%     | ok               |
|          40 | -28.29%  | -27.83%            | -41.30% |    -0.61 |       70 | 35.27%     | ok               |
|          30 | -33.60%  | -27.83%            | -41.46% |    -0.66 |       67 | 44.09%     | ok               |
|          20 | -38.89%  | -27.83%            | -42.88% |    -0.71 |       80 | 49.25%     | ok               |

## CRV-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 33.22%   | -78.68%            | -37.78% |     0.53 |       62 | 27.59%     | ok               |
|          40 | 16.99%   | -78.68%            | -38.86% |     0.38 |       52 | 23.95%     | ok               |
|          50 | 14.66%   | -78.68%            | -29.30% |     0.36 |       38 | 16.09%     | ok               |
|          30 | 6.45%    | -78.68%            | -39.89% |     0.29 |       62 | 31.99%     | ok               |
|          45 | 6.55%    | -78.68%            | -42.29% |     0.27 |       52 | 18.97%     | ok               |

## CSCO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 36.78%   | 151.79%            | -19.34% |     0.79 |       56 | 37.94%     | ok               |
|          45 | 33.24%   | 151.79%            | -19.34% |     0.72 |       51 | 40.10%     | ok               |
|          25 | 32.04%   | 151.79%            | -23.28% |     0.65 |       63 | 50.75%     | ok               |
|          30 | 31.43%   | 151.79%            | -21.79% |     0.65 |       59 | 48.75%     | ok               |
|          35 | 28.95%   | 151.79%            | -23.68% |     0.61 |       51 | 46.42%     | ok               |

## CVX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -14.95%  | 31.29%             | -25.91% |    -0.35 |       72 | 44.26%     | ok               |
|          35 | -17.44%  | 31.29%             | -28.85% |    -0.46 |       69 | 38.94%     | ok               |
|          20 | -19.04%  | 31.29%             | -30.41% |    -0.47 |       78 | 45.76%     | ok               |
|          30 | -19.31%  | 31.29%             | -29.70% |    -0.52 |       73 | 41.76%     | ok               |
|          40 | -18.47%  | 31.29%             | -28.41% |    -0.54 |       79 | 35.94%     | ok               |

## DASH-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 109.52%  | -3.38%             | -34.71% |     0.88 |       42 | 15.90%     | ok               |
|          40 | 64.67%   | -3.38%             | -34.44% |     0.67 |       46 | 22.61%     | ok               |
|          45 | 51.31%   | -3.38%             | -42.52% |     0.6  |       46 | 18.20%     | ok               |
|          25 | -35.92%  | -3.38%             | -64.14% |     0.06 |       71 | 33.52%     | ok               |
|          35 | -39.92%  | -3.38%             | -63.23% |     0    |       71 | 27.01%     | ok               |

## DBC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | -10.31%  | 38.82%             | -23.91% |    -0.34 |       60 | 31.45%     | ok               |
|          50 | -8.98%   | 38.82%             | -20.31% |    -0.34 |       42 | 21.13%     | ok               |
|          45 | -10.35%  | 38.82%             | -21.46% |    -0.37 |       54 | 24.46%     | ok               |
|          15 | -13.71%  | 38.82%             | -27.30% |    -0.46 |       65 | 37.94%     | ok               |
|          30 | -14.35%  | 38.82%             | -25.86% |    -0.5  |       62 | 33.11%     | ok               |

## DE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -7.66%   | 49.42%             | -28.94% |    -0.08 |       76 | 50.92%     | ok               |
|          50 | -6.48%   | 49.42%             | -23.74% |    -0.11 |       60 | 29.45%     | ok               |
|          25 | -9.08%   | 49.42%             | -26.67% |    -0.11 |       78 | 48.09%     | ok               |
|          30 | -9.23%   | 49.42%             | -25.24% |    -0.12 |       76 | 45.26%     | ok               |
|          45 | -9.34%   | 49.42%             | -26.94% |    -0.17 |       64 | 34.11%     | ok               |

## DIA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -0.55%   | 34.83%             | -11.28% |     0.01 |       58 | 47.25%     | ok               |
|          35 | -0.55%   | 34.83%             | -13.15% |     0.01 |       60 | 44.09%     | ok               |
|          30 | -2.19%   | 34.83%             | -12.94% |    -0.08 |       58 | 45.92%     | ok               |
|          20 | -3.35%   | 34.83%             | -14.29% |    -0.13 |       60 | 49.75%     | ok               |
|          40 | -4.36%   | 34.83%             | -15.06% |    -0.22 |       66 | 41.10%     | ok               |

## DIS Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 40.04%   | 11.31%             | -14.24% |     0.96 |       46 | 30.12%     | ok               |
|          45 | 9.81%    | 11.31%             | -15.09% |     0.3  |       49 | 33.44%     | ok               |
|          40 | 8.82%    | 11.31%             | -22.77% |     0.28 |       61 | 38.60%     | ok               |
|          35 | 5.61%    | 11.31%             | -20.85% |     0.21 |       69 | 44.43%     | ok               |
|          30 | 2.59%    | 11.31%             | -22.67% |     0.16 |       59 | 47.42%     | ok               |

## DOGE-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 10.70%   | -71.46%            | -57.89% |     0.38 |       83 | 64.56%     | ok               |
|          20 | -1.60%   | -71.46%            | -55.83% |     0.27 |       86 | 60.34%     | ok               |
|          25 | -1.84%   | -71.46%            | -53.72% |     0.26 |       72 | 54.41%     | ok               |
|          30 | -15.19%  | -71.46%            | -60.95% |     0.11 |       77 | 49.04%     | ok               |
|          35 | -44.46%  | -71.46%            | -65.95% |    -0.35 |       74 | 42.34%     | ok               |

## DOT-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -24.98%  | -83.99%            | -43.91% |    -0.21 |       54 | 26.25%     | ok               |
|          45 | -29.59%  | -83.99%            | -48.71% |    -0.26 |       50 | 29.69%     | ok               |
|          40 | -37.31%  | -83.99%            | -48.60% |    -0.35 |       56 | 33.14%     | ok               |
|          30 | -48.72%  | -83.99%            | -59.09% |    -0.38 |       90 | 46.93%     | ok               |
|          35 | -47.72%  | -83.99%            | -60.72% |    -0.38 |       80 | 40.23%     | ok               |

## DXY-INDEX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -3.91%   | -3.16%             | -7.30%  |    -0.49 |       68 | 45.77%     | ok               |
|          30 | -4.68%   | -3.16%             | -10.51% |    -0.53 |       68 | 57.92%     | ok               |
|          15 | -5.96%   | -3.16%             | -12.09% |    -0.55 |       90 | 75.27%     | ok               |
|          45 | -4.11%   | -3.16%             | -8.12%  |    -0.56 |       64 | 35.36%     | ok               |
|          35 | -5.17%   | -3.16%             | -10.65% |    -0.62 |       73 | 52.28%     | ok               |

## EEM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -4.96%   | 79.74%             | -19.52% |    -0.11 |       64 | 39.77%     | ok               |
|          35 | -5.62%   | 79.74%             | -23.88% |    -0.12 |       66 | 41.76%     | ok               |
|          50 | -4.94%   | 79.74%             | -15.88% |    -0.12 |       52 | 35.77%     | ok               |
|          45 | -6.04%   | 79.74%             | -17.36% |    -0.16 |       54 | 37.44%     | ok               |
|          25 | -8.49%   | 79.74%             | -25.60% |    -0.21 |       65 | 44.76%     | ok               |

## EFA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -1.76%   | 39.25%             | -11.27% |    -0    |       58 | 51.41%     | ok               |
|          20 | -7.98%   | 39.25%             | -12.37% |    -0.26 |       63 | 48.59%     | ok               |
|          30 | -8.43%   | 39.25%             | -13.53% |    -0.31 |       58 | 43.59%     | ok               |
|          25 | -10.49%  | 39.25%             | -15.78% |    -0.39 |       62 | 46.26%     | ok               |
|          50 | -9.07%   | 39.25%             | -17.56% |    -0.4  |       54 | 36.27%     | ok               |

## EOG Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -23.61%  | 23.05%             | -39.69% |    -0.58 |       56 | 33.44%     | ok               |
|          50 | -24.73%  | 23.05%             | -40.57% |    -0.64 |       60 | 30.62%     | ok               |
|          30 | -29.95%  | 23.05%             | -48.13% |    -0.69 |       83 | 47.75%     | ok               |
|          25 | -31.71%  | 23.05%             | -51.99% |    -0.7  |       84 | 51.08%     | ok               |
|          40 | -28.13%  | 23.05%             | -43.26% |    -0.72 |       64 | 36.77%     | ok               |

## ETC-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -14.16%  | -70.44%            | -30.24% |    -0.14 |       26 | 16.86%     | ok               |
|          35 | -25.03%  | -70.44%            | -42.62% |    -0.31 |       46 | 25.86%     | ok               |
|          45 | -25.27%  | -70.44%            | -36.69% |    -0.38 |       28 | 18.39%     | ok               |
|          40 | -29.24%  | -70.44%            | -41.87% |    -0.45 |       42 | 21.84%     | ok               |
|          30 | -45.03%  | -70.44%            | -54.24% |    -0.75 |       68 | 30.27%     | ok               |

## ETH-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 139.08%  | -47.11%            | -30.11% |     1.21 |       62 | 43.68%     | ok               |
|          30 | 131.08%  | -47.11%            | -32.89% |     1.13 |       66 | 51.53%     | ok               |
|          40 | 51.19%   | -47.11%            | -33.11% |     0.71 |       58 | 36.21%     | ok               |
|          45 | 33.15%   | -47.11%            | -34.50% |     0.56 |       54 | 32.38%     | ok               |
|          50 | 31.75%   | -47.11%            | -30.50% |     0.55 |       54 | 26.44%     | ok               |

## EWJ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -18.27%  | 44.04%             | -30.73% |    -0.59 |       64 | 41.43%     | ok               |
|          20 | -19.65%  | 44.04%             | -31.32% |    -0.62 |       60 | 43.43%     | ok               |
|          25 | -21.97%  | 44.04%             | -31.18% |    -0.72 |       60 | 42.43%     | ok               |
|          35 | -22.19%  | 44.04%             | -32.54% |    -0.75 |       70 | 39.77%     | ok               |
|          15 | -24.97%  | 44.04%             | -32.24% |    -0.78 |       74 | 46.59%     | ok               |

## FCX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -6.53%   | 71.04%             | -27.80% |     0.02 |       58 | 29.45%     | ok               |
|          45 | -11.02%  | 71.04%             | -35.28% |    -0.05 |       60 | 33.94%     | ok               |
|          40 | -23.71%  | 71.04%             | -44.23% |    -0.28 |       70 | 38.94%     | ok               |
|          20 | -32.36%  | 71.04%             | -57.65% |    -0.36 |       78 | 52.91%     | ok               |
|          30 | -29.82%  | 71.04%             | -48.31% |    -0.36 |       73 | 45.59%     | ok               |

## FET-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 63.34%   | -80.93%            | -51.84% |     0.68 |       86 | 50.57%     | ok               |
|          15 | 12.53%   | -80.93%            | -54.49% |     0.41 |       88 | 53.83%     | ok               |
|          25 | 0.06%    | -80.93%            | -52.50% |     0.3  |       89 | 43.87%     | ok               |
|          30 | -9.47%   | -80.93%            | -48.39% |     0.2  |       77 | 39.85%     | ok               |
|          35 | -33.31%  | -80.93%            | -55.22% |    -0.14 |       65 | 33.33%     | ok               |

## FIL-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -4.64%   | -81.89%            | -43.25% |     0.12 |       46 | 23.56%     | ok               |
|          30 | -27.40%  | -81.89%            | -47.25% |    -0.17 |       70 | 32.95%     | ok               |
|          50 | -20.61%  | -81.89%            | -44.97% |    -0.18 |       38 | 13.79%     | ok               |
|          35 | -26.86%  | -81.89%            | -46.82% |    -0.19 |       56 | 27.39%     | ok               |
|          45 | -24.12%  | -81.89%            | -40.94% |    -0.2  |       44 | 18.01%     | ok               |

## FXI Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -10.98%  | 58.03%             | -23.27% |    -0.23 |       36 | 19.30%     | ok               |
|          25 | -13.03%  | 58.03%             | -22.57% |    -0.26 |       48 | 27.79%     | ok               |
|          30 | -13.50%  | 58.03%             | -23.91% |    -0.27 |       46 | 26.62%     | ok               |
|          15 | -14.93%  | 58.03%             | -21.68% |    -0.29 |       54 | 31.45%     | ok               |
|          20 | -15.98%  | 58.03%             | -24.53% |    -0.34 |       54 | 29.12%     | ok               |

## GDX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 26.05%   | 192.00%            | -31.87% |     0.53 |       60 | 43.59%     | ok               |
|          20 | 14.61%   | 192.00%            | -35.59% |     0.35 |       72 | 53.24%     | ok               |
|          35 | 10.23%   | 192.00%            | -32.37% |     0.29 |       66 | 46.09%     | ok               |
|          30 | 5.77%    | 192.00%            | -34.99% |     0.22 |       60 | 49.08%     | ok               |
|          45 | 4.99%    | 192.00%            | -32.07% |     0.21 |       62 | 40.43%     | ok               |

## GDXJ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -4.27%   | 212.51%            | -45.05% |     0.1  |       66 | 53.08%     | ok               |
|          50 | -8.38%   | 212.51%            | -35.02% |    -0.02 |       58 | 37.27%     | ok               |
|          30 | -21.59%  | 212.51%            | -44.93% |    -0.21 |       68 | 46.59%     | ok               |
|          25 | -23.64%  | 212.51%            | -47.26% |    -0.22 |       71 | 49.75%     | ok               |
|          40 | -23.69%  | 212.51%            | -44.27% |    -0.28 |       64 | 42.26%     | ok               |

## GE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 18.07%   | 203.97%            | -22.29% |     0.43 |       66 | 37.94%     | ok               |
|          20 | 10.86%   | 203.97%            | -26.63% |     0.3  |       69 | 54.91%     | ok               |
|          45 | 10.16%   | 203.97%            | -25.68% |     0.3  |       76 | 40.93%     | ok               |
|          15 | 6.13%    | 203.97%            | -28.62% |     0.23 |       68 | 57.24%     | ok               |
|          35 | 5.88%    | 203.97%            | -27.11% |     0.22 |       80 | 46.42%     | ok               |

## GLD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | 20.63%   | 117.53%            | -14.61% |     0.57 |       46 | 44.43%     | ok               |
|          20 | 19.84%   | 117.53%            | -14.61% |     0.55 |       48 | 45.59%     | ok               |
|          30 | 19.09%   | 117.53%            | -16.63% |     0.54 |       48 | 43.43%     | ok               |
|          35 | 13.28%   | 117.53%            | -17.29% |     0.41 |       50 | 42.76%     | ok               |
|          15 | 13.32%   | 117.53%            | -16.82% |     0.39 |       52 | 50.25%     | ok               |

## GOOGL Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | 82.17%   | 152.31%            | -19.76% |     1.18 |       59 | 57.24%     | ok               |
|          30 | 79.11%   | 152.31%            | -20.41% |     1.16 |       65 | 55.24%     | ok               |
|          15 | 73.73%   | 152.31%            | -13.59% |     1.05 |       69 | 64.73%     | ok               |
|          35 | 63.35%   | 152.31%            | -22.85% |     1.05 |       71 | 50.08%     | ok               |
|          20 | 70.19%   | 152.31%            | -20.57% |     1.05 |       68 | 59.40%     | ok               |

## GRT-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 28.35%   | -89.04%            | -30.82% |     0.52 |       44 | 21.65%     | ok               |
|          45 | 0.87%    | -89.04%            | -49.33% |     0.2  |       50 | 25.86%     | ok               |
|          35 | -4.79%   | -89.04%            | -50.43% |     0.15 |       62 | 34.67%     | ok               |
|          15 | -11.39%  | -89.04%            | -49.67% |     0.15 |       79 | 59.96%     | ok               |
|          40 | -3.43%   | -89.04%            | -48.92% |     0.14 |       52 | 29.12%     | ok               |

## GS Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 24.92%   | 172.55%            | -20.56% |     0.54 |       76 | 59.57%     | ok               |
|          20 | 7.87%    | 172.55%            | -23.19% |     0.26 |       76 | 55.57%     | ok               |
|          25 | 4.46%    | 172.55%            | -23.32% |     0.19 |       76 | 53.08%     | ok               |
|          40 | -0.24%   | 172.55%            | -17.88% |     0.08 |       74 | 43.93%     | ok               |
|          30 | -1.62%   | 172.55%            | -22.13% |     0.06 |       78 | 50.58%     | ok               |

## HD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -4.53%   | -12.28%            | -17.69% |    -0.04 |       69 | 45.09%     | ok               |
|          25 | -5.27%   | -12.28%            | -18.51% |    -0.06 |       68 | 47.09%     | ok               |
|          40 | -10.16%  | -12.28%            | -20.58% |    -0.26 |       80 | 35.27%     | ok               |
|          35 | -13.41%  | -12.28%            | -22.98% |    -0.33 |       76 | 41.43%     | ok               |
|          45 | -13.56%  | -12.28%            | -21.91% |    -0.4  |       62 | 30.12%     | ok               |

## HON Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -16.86%  | 17.04%             | -23.12% |    -0.52 |       74 | 31.95%     | ok               |
|          45 | -19.42%  | 17.04%             | -22.74% |    -0.57 |       80 | 37.44%     | ok               |
|          40 | -20.31%  | 17.04%             | -23.13% |    -0.58 |       80 | 41.43%     | ok               |
|          35 | -21.84%  | 17.04%             | -26.26% |    -0.61 |       95 | 47.75%     | ok               |
|          30 | -23.99%  | 17.04%             | -28.64% |    -0.66 |       95 | 52.08%     | ok               |

## HYG Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -8.16%   | 2.99%              | -8.52%  |    -0.98 |       70 | 29.62%     | ok               |
|          15 | -9.94%   | 2.99%              | -10.29% |    -1.08 |       88 | 41.26%     | ok               |
|          25 | -9.66%   | 2.99%              | -10.02% |    -1.08 |       83 | 37.10%     | ok               |
|          30 | -9.36%   | 2.99%              | -9.72%  |    -1.09 |       81 | 34.44%     | ok               |
|          20 | -9.81%   | 2.99%              | -10.17% |    -1.09 |       84 | 38.94%     | ok               |

## IBIT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 52.15%   | -2.66%             | -12.64% |     1.11 |       18 | 21.20%     | ok               |
|          15 | 64.79%   | -2.66%             | -19.20% |     1.11 |       36 | 37.16%     | ok               |
|          45 | 43.69%   | -2.66%             | -17.12% |     0.95 |       20 | 21.95%     | ok               |
|          40 | 42.27%   | -2.66%             | -17.12% |     0.93 |       22 | 23.44%     | ok               |
|          30 | 35.78%   | -2.66%             | -18.95% |     0.79 |       30 | 29.18%     | ok               |

## IBM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 48.07%   | 89.56%             | -25.31% |     0.89 |       72 | 50.92%     | ok               |
|          15 | 53.45%   | 89.56%             | -28.20% |     0.87 |       87 | 62.73%     | ok               |
|          35 | 45.10%   | 89.56%             | -25.15% |     0.86 |       68 | 46.59%     | ok               |
|          45 | 39.26%   | 89.56%             | -18.33% |     0.82 |       54 | 37.44%     | ok               |
|          40 | 35.95%   | 89.56%             | -24.66% |     0.75 |       64 | 41.26%     | ok               |

## ICP-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 29.10%   | -70.85%            | -29.38% |     0.5  |       58 | 27.20%     | ok               |
|          35 | 21.92%   | -70.85%            | -43.57% |     0.43 |       66 | 31.99%     | ok               |
|          50 | 11.83%   | -70.85%            | -32.83% |     0.33 |       40 | 17.24%     | ok               |
|          30 | 3.35%    | -70.85%            | -54.72% |     0.29 |       83 | 37.93%     | ok               |
|          45 | -2.16%   | -70.85%            | -38.80% |     0.16 |       58 | 21.26%     | ok               |

## IEF Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -8.23%   | -1.53%             | -10.09% |    -0.99 |       72 | 41.93%     | ok               |
|          15 | -8.78%   | -1.53%             | -10.82% |    -1.04 |       71 | 43.43%     | ok               |
|          40 | -8.39%   | -1.53%             | -9.67%  |    -1.31 |       60 | 24.79%     | ok               |
|          45 | -8.07%   | -1.53%             | -9.73%  |    -1.33 |       50 | 22.80%     | ok               |
|          25 | -11.17%  | -1.53%             | -11.86% |    -1.41 |       76 | 39.43%     | ok               |

## IEMG Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | -0.32%   | 73.07%             | -22.13% |     0.05 |       63 | 42.60%     | ok               |
|          50 | -2.69%   | 73.07%             | -14.40% |    -0.05 |       56 | 33.94%     | ok               |
|          40 | -2.99%   | 73.07%             | -18.89% |    -0.05 |       62 | 39.77%     | ok               |
|          45 | -2.90%   | 73.07%             | -15.40% |    -0.05 |       52 | 36.61%     | ok               |
|          25 | -4.72%   | 73.07%             | -25.58% |    -0.09 |       59 | 45.42%     | ok               |

## INJ-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -10.87%  | -68.33%            | -57.50% |     0.05 |       48 | 23.37%     | ok               |
|          50 | -19.83%  | -68.33%            | -52.76% |    -0.12 |       52 | 19.92%     | ok               |
|          35 | -29.57%  | -68.33%            | -66.72% |    -0.14 |       64 | 33.52%     | ok               |
|          40 | -37.62%  | -68.33%            | -66.80% |    -0.33 |       54 | 29.69%     | ok               |
|          20 | -54.78%  | -68.33%            | -81.44% |    -0.44 |       81 | 48.28%     | ok               |

## INTC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 74.71%   | 137.43%            | -49.32% |     0.74 |       62 | 34.61%     | ok               |
|          15 | 78.99%   | 137.43%            | -53.65% |     0.72 |       84 | 61.73%     | ok               |
|          25 | 75.43%   | 137.43%            | -56.41% |     0.72 |       75 | 51.91%     | ok               |
|          40 | 70.27%   | 137.43%            | -55.86% |     0.7  |       68 | 38.94%     | ok               |
|          20 | 72.64%   | 137.43%            | -52.47% |     0.7  |       82 | 56.91%     | ok               |

## INTU Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -2.92%   | -48.84%            | -43.31% |     0.06 |       69 | 28.45%     | ok               |
|          45 | -6.24%   | -48.84%            | -45.13% |     0    |       67 | 32.61%     | ok               |
|          15 | -12.43%  | -48.84%            | -47.30% |    -0.08 |       81 | 50.92%     | ok               |
|          40 | -11.09%  | -48.84%            | -48.32% |    -0.09 |       73 | 35.77%     | ok               |
|          25 | -12.43%  | -48.84%            | -42.24% |    -0.09 |       66 | 45.42%     | ok               |

## ITA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 4.47%    | 83.94%             | -21.48% |     0.21 |       72 | 35.94%     | ok               |
|          30 | 0.26%    | 83.94%             | -23.75% |     0.08 |       70 | 45.92%     | ok               |
|          15 | -2.14%   | 83.94%             | -26.46% |     0.03 |       89 | 58.40%     | ok               |
|          35 | -2.32%   | 83.94%             | -23.16% |    -0    |       74 | 44.09%     | ok               |
|          40 | -3.45%   | 83.94%             | -20.58% |    -0.04 |       76 | 40.60%     | ok               |

## IWM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 8.72%    | 47.46%             | -12.83% |     0.36 |       50 | 37.10%     | ok               |
|          25 | 8.83%    | 47.46%             | -14.87% |     0.36 |       52 | 38.27%     | ok               |
|          40 | 6.51%    | 47.46%             | -14.38% |     0.31 |       44 | 32.45%     | ok               |
|          35 | 6.26%    | 47.46%             | -14.41% |     0.28 |       50 | 34.78%     | ok               |
|          50 | 3.56%    | 47.46%             | -14.56% |     0.2  |       42 | 28.79%     | ok               |

## JNJ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 16.04%   | 37.91%             | -10.70% |     0.71 |       62 | 37.94%     | ok               |
|          15 | 9.95%    | 37.91%             | -18.02% |     0.38 |       72 | 57.90%     | ok               |
|          45 | 7.34%    | 37.91%             | -13.80% |     0.35 |       64 | 43.09%     | ok               |
|          20 | 7.22%    | 37.91%             | -17.61% |     0.31 |       76 | 54.41%     | ok               |
|          40 | 5.00%    | 37.91%             | -14.77% |     0.25 |       70 | 47.25%     | ok               |

## JPM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 11.47%   | 75.92%             | -15.40% |     0.43 |       56 | 39.77%     | ok               |
|          45 | 1.84%    | 75.92%             | -21.44% |     0.12 |       56 | 42.93%     | ok               |
|          40 | -11.61%  | 75.92%             | -28.04% |    -0.28 |       68 | 45.42%     | ok               |
|          20 | -16.78%  | 75.92%             | -33.20% |    -0.31 |       86 | 57.24%     | ok               |
|          35 | -16.55%  | 75.92%             | -27.00% |    -0.42 |       74 | 49.08%     | ok               |

## KO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 23.27%   | 30.83%             | -8.07%  |     0.88 |       49 | 37.27%     | ok               |
|          35 | 19.49%   | 30.83%             | -8.07%  |     0.77 |       52 | 35.94%     | ok               |
|          50 | 16.35%   | 30.83%             | -11.40% |     0.74 |       34 | 26.62%     | ok               |
|          40 | 17.09%   | 30.83%             | -9.28%  |     0.73 |       54 | 32.95%     | ok               |
|          25 | 18.18%   | 30.83%             | -9.37%  |     0.7  |       55 | 39.93%     | ok               |

## LDO-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 6.13%    | -84.91%            | -44.15% |     0.36 |       88 | 51.34%     | ok               |
|          20 | 7.52%    | -84.91%            | -43.71% |     0.36 |       91 | 46.55%     | ok               |
|          30 | -5.65%   | -84.91%            | -58.32% |     0.22 |       78 | 36.97%     | ok               |
|          25 | -19.41%  | -84.91%            | -54.15% |     0.11 |       87 | 42.53%     | ok               |
|          50 | -9.54%   | -84.91%            | -48.77% |     0.02 |       46 | 16.28%     | ok               |

## LIN Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 3.30%    | 25.05%             | -23.70% |     0.17 |       68 | 50.25%     | ok               |
|          25 | 1.46%    | 25.05%             | -22.01% |     0.11 |       68 | 41.93%     | ok               |
|          20 | -0.71%   | 25.05%             | -23.00% |     0.04 |       67 | 45.09%     | ok               |
|          35 | -2.45%   | 25.05%             | -21.18% |    -0.04 |       68 | 32.78%     | ok               |
|          30 | -3.07%   | 25.05%             | -21.53% |    -0.05 |       72 | 39.27%     | ok               |

## LINK-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -19.12%  | -60.64%            | -55.61% |     0.03 |       72 | 40.42%     | ok               |
|          50 | -21.87%  | -60.64%            | -42.26% |    -0.1  |       38 | 20.31%     | ok               |
|          45 | -24.59%  | -60.64%            | -43.89% |    -0.12 |       50 | 24.90%     | ok               |
|          35 | -32.60%  | -60.64%            | -53.72% |    -0.17 |       62 | 35.06%     | ok               |
|          25 | -44.03%  | -60.64%            | -56.54% |    -0.27 |       68 | 45.98%     | ok               |

## LLY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 24.13%   | 71.18%             | -38.23% |     0.52 |       42 | 39.27%     | ok               |
|          45 | 12.23%   | 71.18%             | -42.66% |     0.33 |       50 | 42.43%     | ok               |
|          15 | 5.84%    | 71.18%             | -48.12% |     0.23 |       63 | 61.90%     | ok               |
|          40 | -4.56%   | 71.18%             | -46.23% |     0.04 |       62 | 44.93%     | ok               |
|          20 | -11.21%  | 71.18%             | -51.34% |    -0.05 |       72 | 56.91%     | ok               |

## LRCX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 10.01%   | 358.47%            | -60.45% |     0.29 |       81 | 55.57%     | ok               |
|          50 | 0.69%    | 358.47%            | -50.39% |     0.15 |       76 | 36.61%     | ok               |
|          40 | -8.88%   | 358.47%            | -56.86% |     0.03 |       72 | 42.43%     | ok               |
|          35 | -11.18%  | 358.47%            | -61.76% |     0    |       80 | 44.93%     | ok               |
|          20 | -13.76%  | 358.47%            | -67.64% |    -0.02 |       87 | 50.92%     | ok               |

## LTC-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -24.68%  | -53.67%            | -47.47% |    -0.21 |       58 | 31.23%     | ok               |
|          35 | -29.58%  | -53.67%            | -56.94% |    -0.25 |       68 | 41.76%     | ok               |
|          50 | -32.64%  | -53.67%            | -48.91% |    -0.4  |       52 | 24.52%     | ok               |
|          30 | -40.05%  | -53.67%            | -55.90% |    -0.4  |       68 | 47.32%     | ok               |
|          40 | -37.69%  | -53.67%            | -58.13% |    -0.42 |       60 | 36.97%     | ok               |

## MCD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 3.24%    | -7.07%             | -9.22%  |     0.2  |       42 | 20.47%     | ok               |
|          30 | -3.01%   | -7.07%             | -19.14% |    -0.07 |       75 | 38.77%     | ok               |
|          25 | -4.40%   | -7.07%             | -20.80% |    -0.12 |       77 | 41.26%     | ok               |
|          40 | -6.06%   | -7.07%             | -16.86% |    -0.24 |       73 | 29.62%     | ok               |
|          35 | -8.25%   | -7.07%             | -15.80% |    -0.31 |       69 | 35.27%     | ok               |

## META Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 15.35%   | 68.16%             | -31.03% |     0.36 |       68 | 41.60%     | ok               |
|          40 | 2.67%    | 68.16%             | -35.11% |     0.17 |       68 | 44.59%     | ok               |
|          50 | -2.26%   | 68.16%             | -34.00% |     0.08 |       72 | 37.77%     | ok               |
|          25 | -7.43%   | 68.16%             | -39.82% |     0.02 |       69 | 55.24%     | ok               |
|          35 | -9.09%   | 68.16%             | -34.85% |    -0.02 |       79 | 49.42%     | ok               |

## MPC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 14.51%   | 74.83%             | -23.96% |     0.37 |       52 | 38.60%     | ok               |
|          45 | 7.25%    | 74.83%             | -25.09% |     0.24 |       58 | 42.26%     | ok               |
|          40 | 5.62%    | 74.83%             | -25.70% |     0.22 |       60 | 44.59%     | ok               |
|          35 | 2.36%    | 74.83%             | -35.90% |     0.16 |       68 | 47.09%     | ok               |
|          30 | -13.74%  | 74.83%             | -44.76% |    -0.14 |       71 | 49.92%     | ok               |

## MRK Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -16.06%  | -3.50%             | -29.91% |    -0.27 |       85 | 57.74%     | ok               |
|          25 | -15.65%  | -3.50%             | -31.07% |    -0.29 |       70 | 49.75%     | ok               |
|          20 | -19.79%  | -3.50%             | -29.38% |    -0.39 |       75 | 53.08%     | ok               |
|          30 | -21.75%  | -3.50%             | -32.14% |    -0.47 |       67 | 47.09%     | ok               |
|          35 | -21.54%  | -3.50%             | -30.80% |    -0.47 |       69 | 43.43%     | ok               |

## MS Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -3.98%   | 129.71%            | -19.61% |    -0.03 |       70 | 38.60%     | ok               |
|          35 | -10.73%  | 129.71%            | -21.83% |    -0.2  |       76 | 43.26%     | ok               |
|          15 | -14.36%  | 129.71%            | -25.50% |    -0.24 |       82 | 56.24%     | ok               |
|          20 | -14.82%  | 129.71%            | -25.68% |    -0.28 |       84 | 52.25%     | ok               |
|          50 | -10.06%  | 129.71%            | -15.66% |    -0.3  |       58 | 30.45%     | ok               |

## MSFT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -16.22%  | 11.64%             | -25.28% |    -0.45 |       60 | 35.27%     | ok               |
|          50 | -19.71%  | 11.64%             | -28.69% |    -0.59 |       58 | 30.95%     | ok               |
|          35 | -28.24%  | 11.64%             | -32.77% |    -0.75 |       69 | 43.59%     | ok               |
|          25 | -31.68%  | 11.64%             | -35.99% |    -0.81 |       82 | 50.92%     | ok               |
|          30 | -31.24%  | 11.64%             | -35.58% |    -0.81 |       76 | 47.59%     | ok               |

## MU Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 401.90%  | 1210.48%           | -61.96% |     1.58 |       50 | 66.89%     | ok               |
|          25 | 306.92%  | 1210.48%           | -67.90% |     1.47 |       53 | 60.40%     | ok               |
|          40 | 265.89%  | 1210.48%           | -64.07% |     1.4  |       60 | 53.91%     | ok               |
|          20 | 272.55%  | 1210.48%           | -67.25% |     1.37 |       59 | 62.56%     | ok               |
|          30 | 246.62%  | 1210.48%           | -68.76% |     1.34 |       55 | 58.57%     | ok               |

## NEAR-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 84.92%   | -46.72%            | -45.84% |     0.88 |       48 | 24.71%     | ok               |
|          50 | 55.50%   | -46.72%            | -51.20% |     0.71 |       44 | 19.73%     | ok               |
|          40 | 47.07%   | -46.72%            | -54.53% |     0.63 |       50 | 28.93%     | ok               |
|          35 | 18.40%   | -46.72%            | -58.86% |     0.41 |       74 | 34.48%     | ok               |
|          15 | -6.42%   | -46.72%            | -54.94% |     0.25 |       94 | 58.05%     | ok               |

## NEM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 30.17%   | 183.19%            | -25.79% |     0.49 |       60 | 63.73%     | ok               |
|          20 | 16.24%   | 183.19%            | -30.47% |     0.36 |       70 | 59.23%     | ok               |
|          25 | -2.49%   | 183.19%            | -30.80% |     0.13 |       66 | 57.24%     | ok               |
|          30 | -19.45%  | 183.19%            | -38.49% |    -0.12 |       70 | 55.74%     | ok               |
|          35 | -19.14%  | 183.19%            | -39.55% |    -0.12 |       77 | 52.91%     | ok               |

## NFLX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 44.79%   | 70.43%             | -11.94% |     0.99 |       46 | 46.92%     | ok               |
|          50 | 35.49%   | 70.43%             | -16.28% |     0.87 |       48 | 39.27%     | ok               |
|          35 | 37.35%   | 70.43%             | -18.30% |     0.82 |       60 | 50.42%     | ok               |
|          45 | 32.06%   | 70.43%             | -15.48% |     0.78 |       52 | 43.09%     | ok               |
|          25 | 31.09%   | 70.43%             | -21.09% |     0.68 |       60 | 57.24%     | ok               |

## NKE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | -24.38%  | -57.78%            | -42.13% |    -0.32 |       75 | 38.77%     | ok               |
|          20 | -34.55%  | -57.78%            | -50.44% |    -0.43 |       95 | 54.41%     | ok               |
|          25 | -34.77%  | -57.78%            | -51.20% |    -0.44 |       91 | 50.58%     | ok               |
|          30 | -35.66%  | -57.78%            | -55.35% |    -0.48 |       91 | 45.26%     | ok               |
|          40 | -26.00%  | -57.78%            | -32.59% |    -0.49 |       67 | 30.78%     | ok               |

## NOW Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 35.98%   | -17.47%            | -26.36% |     0.56 |       77 | 51.75%     | ok               |
|          30 | 26.78%   | -17.47%            | -31.32% |     0.48 |       78 | 46.09%     | ok               |
|          15 | 26.94%   | -17.47%            | -27.25% |     0.47 |       86 | 54.91%     | ok               |
|          25 | 25.53%   | -17.47%            | -26.83% |     0.46 |       72 | 49.25%     | ok               |
|          35 | 18.35%   | -17.47%            | -29.30% |     0.39 |       77 | 41.10%     | ok               |

## NVDA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -2.86%   | 145.35%            | -33.22% |     0.13 |       68 | 52.94%     | ok               |
|          30 | -4.69%   | 145.35%            | -35.26% |     0.09 |       70 | 50.62%     | ok               |
|          20 | -9.31%   | 145.35%            | -40.59% |     0.06 |       71 | 57.40%     | ok               |
|          50 | -12.62%  | 145.35%            | -40.84% |    -0.06 |       60 | 34.76%     | ok               |
|          35 | -15.86%  | 145.35%            | -41.25% |    -0.09 |       82 | 47.77%     | ok               |

## OP-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 44.63%   | -93.62%            | -53.61% |     0.62 |       50 | 25.48%     | ok               |
|          45 | 41.49%   | -93.62%            | -45.76% |     0.62 |       38 | 17.05%     | ok               |
|          50 | 34.92%   | -93.62%            | -36.11% |     0.58 |       34 | 12.26%     | ok               |
|          35 | 20.94%   | -93.62%            | -58.13% |     0.42 |       58 | 28.74%     | ok               |
|          30 | -7.53%   | -93.62%            | -70.11% |     0.17 |       76 | 35.44%     | ok               |

## ORCL Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 195.94%  | 121.64%            | -21.44% |     1.27 |       73 | 64.23%     | ok               |
|          25 | 120.50%  | 121.64%            | -24.79% |     1    |       72 | 56.57%     | ok               |
|          20 | 118.19%  | 121.64%            | -22.81% |     0.98 |       76 | 59.90%     | ok               |
|          35 | 74.36%   | 121.64%            | -31.95% |     0.77 |       64 | 48.25%     | ok               |
|          30 | 74.51%   | 121.64%            | -29.47% |     0.77 |       70 | 52.41%     | ok               |

## OXY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 1.58%    | 5.00%              | -30.54% |     0.13 |       36 | 28.79%     | ok               |
|          35 | 0.78%    | 5.00%              | -29.95% |     0.12 |       66 | 38.77%     | ok               |
|          30 | -0.54%   | 5.00%              | -31.73% |     0.11 |       69 | 43.59%     | ok               |
|          40 | -1.69%   | 5.00%              | -31.66% |     0.07 |       54 | 34.78%     | ok               |
|          45 | -7.54%   | 5.00%              | -35.73% |    -0.06 |       42 | 30.62%     | ok               |

## PEP Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 8.79%    | -14.61%            | -11.62% |     0.41 |       44 | 27.95%     | ok               |
|          45 | 1.43%    | -14.61%            | -14.22% |     0.11 |       68 | 32.78%     | ok               |
|          40 | -2.08%   | -14.61%            | -18.04% |    -0.02 |       76 | 38.10%     | ok               |
|          35 | -4.40%   | -14.61%            | -21.42% |    -0.08 |       87 | 42.76%     | ok               |
|          30 | -9.80%   | -14.61%            | -21.35% |    -0.23 |       85 | 49.08%     | ok               |

## PEPE-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -0.37%   | -83.61%            | -57.66% |     0.27 |       79 | 42.72%     | ok               |
|          35 | -7.05%   | -83.61%            | -51.35% |     0.18 |       64 | 37.55%     | ok               |
|          25 | -22.58%  | -83.61%            | -62.34% |     0.06 |       87 | 48.08%     | ok               |
|          15 | -44.26%  | -83.61%            | -70.49% |    -0.08 |       86 | 58.05%     | ok               |
|          50 | -25.09%  | -83.61%            | -39.66% |    -0.13 |       52 | 22.03%     | ok               |

## PFE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -24.03%  | -12.59%            | -27.99% |    -0.84 |       52 | 21.30%     | ok               |
|          35 | -31.86%  | -12.59%            | -36.39% |    -1    |       82 | 33.61%     | ok               |
|          50 | -26.33%  | -12.59%            | -29.22% |    -1.03 |       44 | 17.47%     | ok               |
|          40 | -30.46%  | -12.59%            | -34.09% |    -1.04 |       76 | 26.12%     | ok               |
|          30 | -38.05%  | -12.59%            | -42.29% |    -1.18 |       77 | 37.27%     | ok               |

## PG Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -3.81%   | -6.50%             | -19.77% |    -0.12 |       54 | 34.11%     | ok               |
|          35 | -4.99%   | -6.50%             | -18.66% |    -0.16 |       60 | 37.77%     | ok               |
|          30 | -9.53%   | -6.50%             | -20.33% |    -0.34 |       63 | 40.60%     | ok               |
|          25 | -10.62%  | -6.50%             | -20.01% |    -0.38 |       73 | 41.76%     | ok               |
|          45 | -14.56%  | -6.50%             | -20.33% |    -0.65 |       54 | 31.11%     | ok               |

## PM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 1.44%    | 86.24%             | -32.20% |     0.12 |       84 | 53.08%     | ok               |
|          20 | 0.16%    | 86.24%             | -31.89% |     0.1  |       87 | 61.90%     | ok               |
|          30 | -0.11%   | 86.24%             | -33.68% |     0.09 |       81 | 56.91%     | ok               |
|          50 | -4.69%   | 86.24%             | -35.70% |    -0.03 |       76 | 43.26%     | ok               |
|          25 | -6.99%   | 86.24%             | -37.05% |    -0.06 |       81 | 59.23%     | ok               |

## POL-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 46.77%   | -80.28%            | -46.45% |     0.64 |       82 | 47.51%     | ok               |
|          25 | 35.37%   | -80.28%            | -46.72% |     0.54 |       75 | 56.51%     | ok               |
|          20 | 26.14%   | -80.28%            | -52.88% |     0.47 |       83 | 61.88%     | ok               |
|          50 | 13.48%   | -80.28%            | -22.46% |     0.35 |       52 | 20.69%     | ok               |
|          15 | -1.54%   | -80.28%            | -58.42% |     0.24 |       82 | 68.20%     | ok               |

## QCOM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | 17.87%   | 79.46%             | -55.66% |     0.37 |       75 | 50.75%     | ok               |
|          20 | 14.84%   | 79.46%             | -57.05% |     0.34 |       72 | 53.41%     | ok               |
|          35 | 10.31%   | 79.46%             | -51.84% |     0.29 |       87 | 45.92%     | ok               |
|          30 | -1.74%   | 79.46%             | -57.69% |     0.14 |       81 | 48.59%     | ok               |
|          15 | -4.25%   | 79.46%             | -60.40% |     0.12 |       76 | 56.57%     | ok               |

## QQQ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | 28.26%   | 82.18%             | -12.88% |     0.74 |       57 | 49.08%     | ok               |
|          20 | 27.71%   | 82.18%             | -12.98% |     0.71 |       65 | 51.58%     | ok               |
|          30 | 24.07%   | 82.18%             | -12.88% |     0.67 |       60 | 46.26%     | ok               |
|          15 | 25.04%   | 82.18%             | -14.17% |     0.63 |       65 | 54.08%     | ok               |
|          35 | 11.39%   | 82.18%             | -19.00% |     0.39 |       66 | 42.60%     | ok               |

## RENDER-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 66.75%   | -50.24%            | -43.43% |     0.75 |       82 | 55.65%     | ok               |
|          15 | 47.39%   | -50.24%            | -44.59% |     0.65 |       82 | 58.85%     | ok               |
|          25 | 33.70%   | -50.24%            | -40.60% |     0.56 |       86 | 51.60%     | ok               |
|          30 | -8.22%   | -50.24%            | -45.00% |     0.21 |       94 | 44.99%     | ok               |
|          40 | -18.54%  | -50.24%            | -38.60% |     0.02 |       68 | 30.06%     | ok               |

## RTX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 25.37%   | 100.45%            | -18.66% |     0.64 |       76 | 56.74%     | ok               |
|          25 | 20.69%   | 100.45%            | -18.59% |     0.55 |       64 | 53.41%     | ok               |
|          50 | 15.66%   | 100.45%            | -18.42% |     0.52 |       60 | 41.93%     | ok               |
|          30 | 18.28%   | 100.45%            | -16.99% |     0.5  |       58 | 52.08%     | ok               |
|          35 | 15.71%   | 100.45%            | -18.00% |     0.49 |       54 | 50.08%     | ok               |

## SBUX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -14.19%  | 2.56%              | -23.55% |    -0.22 |       62 | 42.43%     | ok               |
|          45 | -15.92%  | 2.56%              | -27.26% |    -0.35 |       70 | 29.28%     | ok               |
|          40 | -18.90%  | 2.56%              | -27.13% |    -0.4  |       68 | 32.95%     | ok               |
|          30 | -23.13%  | 2.56%              | -31.15% |    -0.46 |       65 | 40.27%     | ok               |
|          50 | -19.01%  | 2.56%              | -26.80% |    -0.47 |       56 | 25.12%     | ok               |

## SCHW Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 2.81%    | 31.56%             | -15.92% |     0.15 |       52 | 33.11%     | ok               |
|          50 | -2.36%   | 31.56%             | -12.59% |    -0.02 |       48 | 30.78%     | ok               |
|          40 | -7.85%   | 31.56%             | -21.81% |    -0.15 |       60 | 36.11%     | ok               |
|          25 | -10.23%  | 31.56%             | -28.76% |    -0.16 |       61 | 47.75%     | ok               |
|          20 | -11.91%  | 31.56%             | -29.24% |    -0.2  |       69 | 50.42%     | ok               |

## SHIB-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -15.11%  | -76.11%            | -49.21% |     0.08 |       80 | 67.05%     | ok               |
|          25 | -22.15%  | -76.11%            | -43.85% |    -0.03 |       77 | 57.85%     | ok               |
|          20 | -27.15%  | -76.11%            | -48.69% |    -0.08 |       83 | 62.84%     | ok               |
|          30 | -35.46%  | -76.11%            | -48.95% |    -0.26 |       78 | 51.15%     | ok               |
|          35 | -34.60%  | -76.11%            | -55.49% |    -0.29 |       68 | 44.83%     | ok               |

## SHY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd    |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:-------|---------:|---------:|:-----------|:-----------------|
|          30 | -2.06%   | -0.01%             | -2.85% |    -0.7  |       50 | 36.77%     | ok               |
|          35 | -2.18%   | -0.01%             | -3.27% |    -0.74 |       52 | 34.94%     | ok               |
|          40 | -2.29%   | -0.01%             | -3.33% |    -0.79 |       52 | 33.11%     | ok               |
|          45 | -2.27%   | -0.01%             | -3.23% |    -0.8  |       50 | 29.95%     | ok               |
|          50 | -2.44%   | -0.01%             | -3.40% |    -0.9  |       46 | 27.12%     | ok               |

## SKY-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -29.93%  | 15.49%             | -43.98% |    -0.42 |       66 | 39.32%     | ok               |
|          25 | -33.53%  | 15.49%             | -48.09% |    -0.48 |       61 | 43.20%     | ok               |
|          15 | -38.89%  | 15.49%             | -56.39% |    -0.53 |       56 | 49.51%     | ok               |
|          20 | -43.65%  | 15.49%             | -58.40% |    -0.67 |       58 | 47.09%     | ok               |
|          35 | -40.38%  | 15.49%             | -49.68% |    -0.79 |       58 | 33.01%     | ok               |

## SLB Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 4.80%    | 17.34%             | -25.33% |     0.2  |       50 | 37.10%     | ok               |
|          45 | 3.25%    | 17.34%             | -22.80% |     0.17 |       56 | 33.78%     | ok               |
|          35 | -21.51%  | 17.34%             | -43.52% |    -0.36 |       78 | 45.09%     | ok               |
|          50 | -17.82%  | 17.34%             | -31.97% |    -0.37 |       58 | 29.78%     | ok               |
|          30 | -31.95%  | 17.34%             | -54.23% |    -0.58 |       77 | 51.58%     | ok               |

## SLV Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 67.27%   | 216.19%            | -29.75% |     0.86 |       60 | 36.27%     | ok               |
|          45 | 62.01%   | 216.19%            | -31.82% |     0.82 |       54 | 34.44%     | ok               |
|          50 | 57.25%   | 216.19%            | -34.10% |     0.78 |       52 | 33.61%     | ok               |
|          35 | 54.63%   | 216.19%            | -36.89% |     0.75 |       62 | 38.60%     | ok               |
|          30 | 36.93%   | 216.19%            | -42.66% |     0.58 |       58 | 40.60%     | ok               |

## SMH Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 122.37%  | 269.63%            | -30.17% |     1.36 |       49 | 54.58%     | ok               |
|          35 | 99.02%   | 269.63%            | -34.36% |     1.23 |       56 | 50.42%     | ok               |
|          25 | 98.87%   | 269.63%            | -32.94% |     1.21 |       48 | 53.41%     | ok               |
|          30 | 96.53%   | 269.63%            | -33.99% |     1.2  |       50 | 51.75%     | ok               |
|          45 | 78.26%   | 269.63%            | -32.75% |     1.12 |       56 | 44.26%     | ok               |

## SNX-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 34.41%   | -86.69%            | -28.28% |     0.55 |       70 | 31.42%     | ok               |
|          30 | 16.03%   | -86.69%            | -32.91% |     0.39 |       67 | 39.46%     | ok               |
|          20 | -2.42%   | -86.69%            | -43.20% |     0.25 |       74 | 50.57%     | ok               |
|          25 | -7.41%   | -86.69%            | -35.81% |     0.18 |       78 | 43.87%     | ok               |
|          40 | -14.01%  | -86.69%            | -34.73% |     0.01 |       58 | 25.29%     | ok               |

## SOL-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -17.24%  | -63.61%            | -57.46% |     0.04 |       66 | 38.31%     | ok               |
|          25 | -28.98%  | -63.61%            | -53.21% |    -0.05 |       74 | 56.51%     | ok               |
|          35 | -32.66%  | -63.61%            | -61.96% |    -0.13 |       74 | 45.79%     | ok               |
|          15 | -37.30%  | -63.61%            | -59.14% |    -0.14 |       80 | 64.18%     | ok               |
|          20 | -39.19%  | -63.61%            | -56.90% |    -0.18 |       70 | 59.00%     | ok               |

## SOXX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 102.37%  | 231.13%            | -38.67% |     1.18 |       55 | 53.41%     | ok               |
|          25 | 98.50%   | 231.13%            | -39.85% |     1.15 |       53 | 53.08%     | ok               |
|          15 | 97.29%   | 231.13%            | -37.72% |     1.11 |       68 | 56.24%     | ok               |
|          35 | 89.44%   | 231.13%            | -38.63% |     1.11 |       63 | 48.09%     | ok               |
|          30 | 87.35%   | 231.13%            | -40.34% |     1.07 |       57 | 50.92%     | ok               |

## SPY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 20.24%   | 58.27%             | -14.25% |     0.68 |       58 | 54.08%     | ok               |
|          15 | 19.47%   | 58.27%             | -16.80% |     0.65 |       63 | 56.91%     | ok               |
|          25 | 13.32%   | 58.27%             | -15.22% |     0.49 |       58 | 53.41%     | ok               |
|          30 | 9.22%    | 58.27%             | -16.47% |     0.37 |       60 | 50.92%     | ok               |
|          35 | 5.88%    | 58.27%             | -16.72% |     0.27 |       60 | 48.42%     | ok               |

## SUSHI-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -32.29%  | -83.77%            | -40.12% |    -0.33 |       52 | 14.94%     | ok               |
|          45 | -61.52%  | -83.77%            | -64.69% |    -0.83 |       52 | 17.62%     | ok               |
|          40 | -65.19%  | -83.77%            | -68.78% |    -0.88 |       63 | 24.52%     | ok               |
|          35 | -73.92%  | -83.77%            | -74.87% |    -1.08 |       80 | 29.69%     | ok               |
|          15 | -83.44%  | -83.77%            | -84.05% |    -1.13 |       90 | 47.51%     | ok               |

## T Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 41.47%   | 39.60%             | -18.13% |     0.91 |       61 | 54.08%     | ok               |
|          25 | 34.62%   | 39.60%             | -17.66% |     0.8  |       65 | 51.58%     | ok               |
|          15 | 33.74%   | 39.60%             | -15.08% |     0.76 |       70 | 57.90%     | ok               |
|          35 | 24.54%   | 39.60%             | -14.49% |     0.64 |       66 | 45.92%     | ok               |
|          30 | 23.16%   | 39.60%             | -17.01% |     0.6  |       66 | 49.25%     | ok               |

## TGT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -11.69%  | -13.39%            | -41.89% |    -0.12 |       81 | 46.76%     | ok               |
|          25 | -12.57%  | -13.39%            | -42.39% |    -0.17 |       63 | 41.76%     | ok               |
|          15 | -14.58%  | -13.39%            | -39.76% |    -0.17 |       71 | 51.25%     | ok               |
|          30 | -13.41%  | -13.39%            | -40.57% |    -0.2  |       58 | 39.10%     | ok               |
|          45 | -11.83%  | -13.39%            | -29.07% |    -0.2  |       52 | 29.45%     | ok               |

## TIA-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 62.17%   | -92.65%            | -32.72% |     0.73 |       56 | 28.93%     | ok               |
|          40 | 55.02%   | -92.65%            | -32.87% |     0.69 |       56 | 24.90%     | ok               |
|          45 | 35.77%   | -92.65%            | -32.94% |     0.57 |       52 | 18.58%     | ok               |
|          50 | 23.57%   | -92.65%            | -38.67% |     0.49 |       34 | 11.30%     | ok               |
|          30 | -7.89%   | -92.65%            | -54.78% |     0.17 |       80 | 32.76%     | ok               |

## TLT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -22.24%  | -11.29%            | -24.21% |    -1.6  |       74 | 33.61%     | ok               |
|          40 | -21.31%  | -11.29%            | -23.31% |    -1.86 |       60 | 22.63%     | ok               |
|          35 | -23.44%  | -11.29%            | -25.38% |    -1.9  |       68 | 27.62%     | ok               |
|          50 | -17.12%  | -11.29%            | -18.99% |    -1.91 |       36 | 14.98%     | ok               |
|          15 | -28.65%  | -11.29%            | -30.94% |    -1.91 |       79 | 41.60%     | ok               |

## TMO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 43.47%   | -12.87%            | -10.55% |     0.99 |       36 | 30.12%     | ok               |
|          45 | 42.11%   | -12.87%            | -12.29% |     0.93 |       46 | 35.27%     | ok               |
|          40 | 39.50%   | -12.87%            | -12.07% |     0.87 |       51 | 39.93%     | ok               |
|          35 | 26.49%   | -12.87%            | -16.12% |     0.62 |       63 | 44.76%     | ok               |
|          30 | 19.54%   | -12.87%            | -16.83% |     0.48 |       57 | 49.75%     | ok               |

## TMUS Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 21.22%   | 11.12%             | -26.87% |     0.51 |       67 | 60.40%     | ok               |
|          30 | 19.76%   | 11.12%             | -24.50% |     0.5  |       68 | 48.75%     | ok               |
|          20 | 13.78%   | 11.12%             | -24.82% |     0.38 |       69 | 54.74%     | ok               |
|          25 | 12.65%   | 11.12%             | -25.91% |     0.36 |       73 | 51.08%     | ok               |
|          50 | 8.80%    | 11.12%             | -18.84% |     0.31 |       58 | 36.61%     | ok               |

## TRX-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -2.64%   | 30.59%             | -22.90% |     0.03 |       70 | 49.23%     | ok               |
|          35 | -3.97%   | 30.59%             | -21.77% |    -0.01 |       66 | 46.55%     | ok               |
|          25 | -4.39%   | 30.59%             | -26.84% |    -0.02 |       66 | 52.49%     | ok               |
|          40 | -3.78%   | 30.59%             | -22.27% |    -0.02 |       52 | 38.51%     | ok               |
|          50 | -6.77%   | 30.59%             | -21.14% |    -0.13 |       46 | 33.14%     | ok               |

## TSLA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 89.25%   | 81.11%             | -32.60% |     0.95 |       64 | 31.78%     | ok               |
|          40 | 79.72%   | 81.11%             | -45.90% |     0.83 |       61 | 36.27%     | ok               |
|          45 | 52.25%   | 81.11%             | -46.86% |     0.66 |       65 | 33.61%     | ok               |
|          35 | 30.35%   | 81.11%             | -54.51% |     0.48 |       76 | 39.43%     | ok               |
|          30 | 8.00%    | 81.11%             | -57.89% |     0.29 |       68 | 44.09%     | ok               |

## TXN Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 14.61%   | 84.51%             | -45.45% |     0.35 |       72 | 35.61%     | ok               |
|          20 | 7.61%    | 84.51%             | -38.98% |     0.25 |       66 | 60.23%     | ok               |
|          15 | 6.52%    | 84.51%             | -39.48% |     0.24 |       69 | 63.89%     | ok               |
|          35 | 2.39%    | 84.51%             | -43.38% |     0.17 |       78 | 50.08%     | ok               |
|          40 | 1.70%    | 84.51%             | -45.67% |     0.16 |       76 | 47.92%     | ok               |

## UNH Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 23.35%   | -29.88%            | -37.02% |     0.46 |       52 | 28.62%     | ok               |
|          30 | 14.89%   | -29.88%            | -32.44% |     0.35 |       78 | 51.91%     | ok               |
|          35 | 11.73%   | -29.88%            | -33.70% |     0.31 |       70 | 46.76%     | ok               |
|          15 | 9.47%    | -29.88%            | -36.68% |     0.28 |       77 | 66.89%     | ok               |
|          40 | 8.52%    | -29.88%            | -38.45% |     0.27 |       64 | 41.10%     | ok               |

## UNI-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -8.12%   | -79.76%            | -53.40% |     0.13 |       52 | 23.56%     | ok               |
|          50 | -11.11%  | -79.76%            | -50.59% |     0.08 |       46 | 20.31%     | ok               |
|          40 | -16.56%  | -79.76%            | -60.60% |     0.04 |       54 | 28.74%     | ok               |
|          35 | -27.78%  | -79.76%            | -65.80% |    -0.06 |       72 | 33.33%     | ok               |
|          20 | -70.99%  | -79.76%            | -80.81% |    -0.71 |      101 | 50.57%     | ok               |

## UPS Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -33.80%  | -32.60%            | -42.25% |    -0.65 |       74 | 42.93%     | ok               |
|          35 | -32.70%  | -32.60%            | -40.47% |    -0.66 |       59 | 32.61%     | ok               |
|          20 | -34.91%  | -32.60%            | -45.77% |    -0.67 |       80 | 46.09%     | ok               |
|          30 | -35.17%  | -32.60%            | -40.62% |    -0.71 |       66 | 38.27%     | ok               |
|          40 | -34.04%  | -32.60%            | -42.12% |    -0.72 |       51 | 27.45%     | ok               |

## USO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 8.31%    | 111.63%            | -35.12% |     0.26 |       50 | 26.79%     | ok               |
|          30 | 2.80%    | 111.63%            | -43.35% |     0.17 |       68 | 34.44%     | ok               |
|          25 | -1.00%   | 111.63%            | -44.86% |     0.11 |       71 | 37.60%     | ok               |
|          20 | -1.10%   | 111.63%            | -44.92% |     0.11 |       75 | 39.77%     | ok               |
|          40 | -1.01%   | 111.63%            | -41.14% |     0.11 |       61 | 29.62%     | ok               |

## VEA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 3.84%    | 51.04%             | -17.55% |     0.2  |       62 | 50.25%     | ok               |
|          20 | 0.28%    | 51.04%             | -18.44% |     0.06 |       61 | 47.75%     | ok               |
|          25 | -2.41%   | 51.04%             | -19.11% |    -0.04 |       59 | 45.92%     | ok               |
|          30 | -2.87%   | 51.04%             | -19.49% |    -0.07 |       60 | 43.43%     | ok               |
|          35 | -4.16%   | 51.04%             | -18.54% |    -0.12 |       56 | 42.26%     | ok               |

## VIXY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -46.17%  | -59.84%            | -68.69% |    -0.39 |       44 | 10.32%     | ok               |
|          45 | -54.34%  | -59.84%            | -74.12% |    -0.52 |       56 | 15.97%     | ok               |
|          40 | -63.74%  | -59.84%            | -79.58% |    -0.65 |       70 | 19.97%     | ok               |
|          35 | -67.54%  | -59.84%            | -83.87% |    -0.69 |       86 | 25.12%     | ok               |
|          15 | -77.33%  | -59.84%            | -89.47% |    -0.8  |       99 | 42.43%     | ok               |

## VNQ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -8.60%   | 8.07%              | -19.07% |    -0.37 |       60 | 28.62%     | ok               |
|          50 | -9.03%   | 8.07%              | -17.13% |    -0.41 |       56 | 26.12%     | ok               |
|          25 | -14.09%  | 8.07%              | -22.16% |    -0.55 |       70 | 41.10%     | ok               |
|          40 | -14.13%  | 8.07%              | -24.84% |    -0.62 |       74 | 32.11%     | ok               |
|          20 | -18.91%  | 8.07%              | -23.61% |    -0.75 |       79 | 44.26%     | ok               |

## VTI Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 18.68%   | 56.66%             | -13.96% |     0.63 |       62 | 55.91%     | ok               |
|          15 | 13.60%   | 56.66%             | -15.70% |     0.48 |       65 | 58.57%     | ok               |
|          25 | 7.52%    | 56.66%             | -16.10% |     0.31 |       60 | 54.24%     | ok               |
|          30 | 0.00%    | 56.66%             | -18.77% |     0.06 |       70 | 52.25%     | ok               |
|          35 | -2.51%   | 56.66%             | -21.19% |    -0.03 |       64 | 49.08%     | ok               |

## VWO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -7.30%   | 50.64%             | -21.18% |    -0.25 |       60 | 32.61%     | ok               |
|          15 | -9.03%   | 50.64%             | -24.01% |    -0.26 |       69 | 49.42%     | ok               |
|          20 | -10.06%  | 50.64%             | -26.14% |    -0.31 |       67 | 47.25%     | ok               |
|          40 | -8.98%   | 50.64%             | -23.57% |    -0.31 |       70 | 37.94%     | ok               |
|          45 | -9.11%   | 50.64%             | -23.26% |    -0.33 |       62 | 35.11%     | ok               |

## VZ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -0.07%   | 19.37%             | -16.98% |     0.06 |       52 | 27.12%     | ok               |
|          45 | -6.97%   | 19.37%             | -20.38% |    -0.16 |       58 | 29.95%     | ok               |
|          35 | -10.90%  | 19.37%             | -24.68% |    -0.28 |       59 | 35.61%     | ok               |
|          25 | -14.23%  | 19.37%             | -28.84% |    -0.35 |       76 | 43.43%     | ok               |
|          40 | -15.51%  | 19.37%             | -26.72% |    -0.45 |       64 | 32.45%     | ok               |

## WFC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -2.27%   | 60.31%             | -18.29% |    -0.01 |       54 | 31.61%     | ok               |
|          35 | -9.30%   | 60.31%             | -23.06% |    -0.14 |       79 | 43.76%     | ok               |
|          45 | -8.75%   | 60.31%             | -23.40% |    -0.19 |       60 | 35.94%     | ok               |
|          20 | -19.71%  | 60.31%             | -28.81% |    -0.3  |       81 | 52.91%     | ok               |
|          40 | -14.40%  | 60.31%             | -24.26% |    -0.36 |       74 | 39.60%     | ok               |

## WIF-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 37.28%   | -90.27%            | -40.67% |     0.55 |       69 | 38.70%     | ok               |
|          15 | 34.92%   | -90.27%            | -46.21% |     0.54 |       76 | 41.57%     | ok               |
|          25 | -5.30%   | -90.27%            | -45.19% |     0.26 |       73 | 35.63%     | ok               |
|          50 | -3.56%   | -90.27%            | -31.17% |     0.11 |       32 | 10.92%     | ok               |
|          45 | -23.46%  | -90.27%            | -44.01% |    -0.18 |       42 | 13.41%     | ok               |

## WMT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 64.81%   | 117.42%            | -9.18%  |     1.63 |       36 | 45.92%     | ok               |
|          50 | 51.49%   | 117.42%            | -12.19% |     1.45 |       32 | 43.26%     | ok               |
|          40 | 54.55%   | 117.42%            | -9.18%  |     1.4  |       40 | 47.09%     | ok               |
|          35 | 55.83%   | 117.42%            | -9.11%  |     1.39 |       48 | 50.75%     | ok               |
|          30 | 33.27%   | 117.42%            | -21.31% |     0.87 |       55 | 53.24%     | ok               |

## XBI Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 1.58%    | 40.31%             | -16.71% |     0.12 |       62 | 34.78%     | ok               |
|          45 | 0.80%    | 40.31%             | -16.88% |     0.1  |       54 | 31.61%     | ok               |
|          50 | -5.14%   | 40.31%             | -16.83% |    -0.07 |       54 | 28.29%     | ok               |
|          35 | -6.74%   | 40.31%             | -21.38% |    -0.09 |       64 | 38.27%     | ok               |
|          30 | -8.52%   | 40.31%             | -21.75% |    -0.13 |       64 | 40.10%     | ok               |

## XLB Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -1.62%   | 23.49%             | -19.67% |    -0.01 |       58 | 31.78%     | ok               |
|          50 | -2.34%   | 23.49%             | -17.59% |    -0.04 |       44 | 27.62%     | ok               |
|          35 | -4.86%   | 23.49%             | -22.65% |    -0.13 |       60 | 35.11%     | ok               |
|          45 | -4.59%   | 23.49%             | -19.78% |    -0.13 |       46 | 28.95%     | ok               |
|          25 | -10.57%  | 23.49%             | -23.63% |    -0.33 |       69 | 41.60%     | ok               |

## XLC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 19.23%   | 52.10%             | -12.33% |     0.64 |       63 | 56.74%     | ok               |
|          25 | 16.99%   | 52.10%             | -12.31% |     0.57 |       60 | 58.57%     | ok               |
|          40 | 13.27%   | 52.10%             | -13.38% |     0.5  |       66 | 49.42%     | ok               |
|          35 | 13.25%   | 52.10%             | -13.38% |     0.49 |       62 | 53.91%     | ok               |
|          20 | 8.76%    | 52.10%             | -13.37% |     0.32 |       68 | 61.23%     | ok               |

## XLE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -0.94%   | 43.99%             | -25.98% |     0.05 |       60 | 37.10%     | ok               |
|          35 | -2.22%   | 43.99%             | -31.00% |     0.03 |       69 | 44.43%     | ok               |
|          45 | -3.24%   | 43.99%             | -29.68% |    -0.02 |       64 | 39.60%     | ok               |
|          25 | -8.70%   | 43.99%             | -35.58% |    -0.13 |       87 | 49.92%     | ok               |
|          40 | -9.27%   | 43.99%             | -34.51% |    -0.19 |       68 | 42.10%     | ok               |

## XLF Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -3.37%   | 34.54%             | -18.01% |    -0.05 |       68 | 55.74%     | ok               |
|          15 | -7.36%   | 34.54%             | -19.58% |    -0.19 |       76 | 58.57%     | ok               |
|          25 | -11.47%  | 34.54%             | -23.22% |    -0.36 |       77 | 52.08%     | ok               |
|          30 | -11.69%  | 34.54%             | -23.61% |    -0.38 |       76 | 49.42%     | ok               |
|          35 | -18.78%  | 34.54%             | -27.06% |    -0.75 |       66 | 45.26%     | ok               |

## XLI Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 12.91%   | 54.88%             | -10.36% |     0.48 |       72 | 55.57%     | ok               |
|          50 | 6.67%    | 54.88%             | -9.25%  |     0.34 |       56 | 35.94%     | ok               |
|          20 | 7.77%    | 54.88%             | -12.74% |     0.34 |       65 | 50.25%     | ok               |
|          45 | 6.35%    | 54.88%             | -12.27% |     0.32 |       64 | 38.60%     | ok               |
|          30 | 5.40%    | 54.88%             | -11.38% |     0.26 |       66 | 47.75%     | ok               |

## XLK Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 105.91%  | 105.85%            | -14.75% |     1.62 |       41 | 54.08%     | ok               |
|          20 | 96.99%   | 105.85%            | -14.75% |     1.56 |       46 | 52.08%     | ok               |
|          25 | 88.56%   | 105.85%            | -14.75% |     1.52 |       40 | 50.08%     | ok               |
|          30 | 86.10%   | 105.85%            | -14.75% |     1.52 |       40 | 48.92%     | ok               |
|          35 | 65.53%   | 105.85%            | -13.61% |     1.29 |       52 | 46.26%     | ok               |

## XLM-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 36.58%   | -39.20%            | -37.64% |     0.56 |       50 | 33.33%     | ok               |
|          50 | 32.76%   | -39.20%            | -32.06% |     0.53 |       46 | 29.50%     | ok               |
|          30 | 12.32%   | -39.20%            | -45.54% |     0.35 |       69 | 47.51%     | ok               |
|          40 | 5.85%    | -39.20%            | -39.92% |     0.28 |       49 | 37.55%     | ok               |
|          35 | 3.86%    | -39.20%            | -44.88% |     0.27 |       69 | 43.68%     | ok               |

## XLP Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 10.43%   | 13.20%             | -5.66%  |     0.64 |       58 | 34.44%     | ok               |
|          40 | 9.28%    | 13.20%             | -7.77%  |     0.56 |       72 | 39.10%     | ok               |
|          35 | 8.32%    | 13.20%             | -9.73%  |     0.5  |       68 | 42.10%     | ok               |
|          50 | 6.61%    | 13.20%             | -6.08%  |     0.43 |       60 | 32.28%     | ok               |
|          30 | 6.07%    | 13.20%             | -10.28% |     0.37 |       72 | 43.93%     | ok               |

## XLU Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 5.74%    | 35.62%             | -9.01%  |     0.32 |       50 | 31.61%     | ok               |
|          50 | 5.69%    | 35.62%             | -9.11%  |     0.32 |       50 | 30.95%     | ok               |
|          40 | 3.01%    | 35.62%             | -9.85%  |     0.19 |       58 | 32.78%     | ok               |
|          35 | -3.82%   | 35.62%             | -14.25% |    -0.13 |       64 | 35.44%     | ok               |
|          30 | -5.60%   | 35.62%             | -15.29% |    -0.21 |       69 | 38.60%     | ok               |

## XLV Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -9.35%   | 4.67%              | -14.23% |    -0.44 |       66 | 37.44%     | ok               |
|          25 | -12.05%  | 4.67%              | -16.79% |    -0.58 |       70 | 39.27%     | ok               |
|          35 | -13.95%  | 4.67%              | -18.49% |    -0.74 |       64 | 34.78%     | ok               |
|          45 | -13.08%  | 4.67%              | -17.57% |    -0.76 |       58 | 27.79%     | ok               |
|          20 | -15.97%  | 4.67%              | -20.35% |    -0.79 |       75 | 40.93%     | ok               |

## XLY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 2.94%    | 32.41%             | -12.94% |     0.16 |       74 | 41.43%     | ok               |
|          30 | -0.80%   | 32.41%             | -14.01% |     0.04 |       76 | 44.59%     | ok               |
|          45 | -1.70%   | 32.41%             | -13.71% |    -0.01 |       52 | 32.28%     | ok               |
|          50 | -1.99%   | 32.41%             | -13.71% |    -0.03 |       52 | 29.62%     | ok               |
|          15 | -4.16%   | 32.41%             | -15.77% |    -0.04 |       81 | 52.75%     | ok               |

## XOM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 1.96%    | 54.55%             | -21.35% |     0.13 |       40 | 29.28%     | ok               |
|          40 | 0.98%    | 54.55%             | -21.45% |     0.1  |       48 | 33.28%     | ok               |
|          25 | -0.20%   | 54.55%             | -19.90% |     0.07 |       61 | 38.10%     | ok               |
|          30 | -0.77%   | 54.55%             | -20.29% |     0.05 |       61 | 36.77%     | ok               |
|          35 | -1.46%   | 54.55%             | -20.93% |     0.03 |       60 | 35.27%     | ok               |

## XRP-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | -32.98%  | -42.80%            | -55.83% |    -0.27 |       74 | 41.38%     | ok               |
|          40 | -38.69%  | -42.80%            | -54.34% |    -0.41 |       64 | 35.44%     | ok               |
|          30 | -45.55%  | -42.80%            | -63.50% |    -0.48 |       78 | 45.79%     | ok               |
|          50 | -43.13%  | -42.80%            | -46.41% |    -0.63 |       64 | 23.56%     | ok               |
|          45 | -49.22%  | -42.80%            | -56.00% |    -0.66 |       64 | 30.84%     | ok               |

## YFI-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -39.83%  | -74.59%            | -50.17% |    -0.68 |       62 | 25.48%     | ok               |
|          30 | -56.42%  | -74.59%            | -67.78% |    -0.91 |       85 | 39.08%     | ok               |
|          45 | -46.13%  | -74.59%            | -51.92% |    -0.96 |       60 | 21.26%     | ok               |
|          35 | -57.19%  | -74.59%            | -64.34% |    -1.01 |       75 | 32.95%     | ok               |
|          50 | -46.82%  | -74.59%            | -51.80% |    -1.07 |       50 | 17.05%     | ok               |

## ZEC-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 124.17%  | 946.09%            | -24.66% |     0.9  |       50 | 23.18%     | ok               |
|          35 | 90.22%   | 946.09%            | -43.54% |     0.76 |       58 | 30.84%     | ok               |
|          25 | 76.78%   | 946.09%            | -46.61% |     0.7  |       59 | 39.66%     | ok               |
|          50 | 54.10%   | 946.09%            | -37.94% |     0.6  |       52 | 20.69%     | ok               |
|          30 | 46.51%   | 946.09%            | -46.93% |     0.57 |       67 | 36.40%     | ok               |
