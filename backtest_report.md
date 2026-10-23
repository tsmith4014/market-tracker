# Market Tracker Backtest Report

_Generated: 2026-10-23T04:38:04+00:00_

## Data Sources

- Crypto: Kraken -> Coinbase -> CoinGecko OHLC -> CoinPaprika fallback chain.
- Stocks / ETFs / indices: Stooq -> Yahoo Finance fallback chain.
- Data rows are generated from real market APIs. Mock OHLCV rows are not generated.

## Data Freshness

- Rows: **92,754**
- Symbols: **161**
- Date range: **2024-05-31** to **2026-10-23**

## Latest Signals

| symbol     | date                |         close |   composite_score | signal   | data_source   |
|:-----------|:--------------------|--------------:|------------------:|:---------|:--------------|
| ABBV       | 2026-10-22 00:00:00 |   285.19      |         71.5833   | LONG     | Yahoo Finance |
| AMGN       | 2026-10-22 00:00:00 |   447.28      |         71.25     | LONG     | Yahoo Finance |
| CL         | 2026-10-22 00:00:00 |    97.39      |         64.25     | LONG     | Yahoo Finance |
| COMP-USD   | 2026-10-23 00:00:00 |    24.49      |         54.1667   | LONG     | Kraken API    |
| COP        | 2026-10-22 00:00:00 |   145.63      |         68.75     | LONG     | Yahoo Finance |
| COST       | 2026-10-22 00:00:00 |  1018.21      |         64.25     | LONG     | Yahoo Finance |
| CRM        | 2026-10-22 00:00:00 |   250.29      |         74.5833   | LONG     | Yahoo Finance |
| CVX        | 2026-10-22 00:00:00 |   226.68      |         52.75     | LONG     | Yahoo Finance |
| DASH-USD   | 2026-10-23 00:00:00 |    55.116     |         69.6667   | LONG     | Kraken API    |
| DIS        | 2026-10-22 00:00:00 |   113.13      |         73.25     | LONG     | Yahoo Finance |
| EOG        | 2026-10-22 00:00:00 |   157.96      |         75.25     | LONG     | Yahoo Finance |
| HD         | 2026-10-22 00:00:00 |   327.73      |         30        | LONG     | Yahoo Finance |
| IBM        | 2026-10-22 00:00:00 |   252.11      |         65.25     | LONG     | Yahoo Finance |
| INTU       | 2026-10-22 00:00:00 |   354.9       |         46        | LONG     | Yahoo Finance |
| JPM        | 2026-10-22 00:00:00 |   336.54      |         35.4167   | LONG     | Yahoo Finance |
| KO         | 2026-10-22 00:00:00 |    95.34      |         73.25     | LONG     | Yahoo Finance |
| LIN        | 2026-10-22 00:00:00 |   510.36      |         64.25     | LONG     | Yahoo Finance |
| LLY        | 2026-10-22 00:00:00 |  1306.69      |         75.75     | LONG     | Yahoo Finance |
| MPC        | 2026-10-22 00:00:00 |   459.28      |         59.5833   | LONG     | Yahoo Finance |
| NKE        | 2026-10-22 00:00:00 |    38.32      |         35.25     | LONG     | Yahoo Finance |
| NOW        | 2026-10-22 00:00:00 |   157         |         74.75     | LONG     | Yahoo Finance |
| OXY        | 2026-10-22 00:00:00 |    62.5       |         50.75     | LONG     | Yahoo Finance |
| PG         | 2026-10-22 00:00:00 |   165.59      |         81.25     | LONG     | Yahoo Finance |
| PM         | 2026-10-22 00:00:00 |   201.74      |         76.9167   | LONG     | Yahoo Finance |
| RTX        | 2026-10-22 00:00:00 |   194.71      |         53.1667   | LONG     | Yahoo Finance |
| TMO        | 2026-10-22 00:00:00 |   676.54      |         44.75     | LONG     | Yahoo Finance |
| UNH        | 2026-10-22 00:00:00 |   424.98      |         75.75     | LONG     | Yahoo Finance |
| USO        | 2026-10-22 00:00:00 |   162.51      |         75.75     | LONG     | Yahoo Finance |
| WMT        | 2026-10-22 00:00:00 |   121.12      |         66        | LONG     | Yahoo Finance |
| XLB        | 2026-10-22 00:00:00 |    51.69      |         55.25     | LONG     | Yahoo Finance |
| XLE        | 2026-10-22 00:00:00 |    67.57      |         50.75     | LONG     | Yahoo Finance |
| XLF        | 2026-10-22 00:00:00 |    56.65      |         73.25     | LONG     | Yahoo Finance |
| XLP        | 2026-10-22 00:00:00 |    89.99      |         67.75     | LONG     | Yahoo Finance |
| XLU        | 2026-10-22 00:00:00 |    42.87      |         41        | LONG     | Yahoo Finance |
| XLY        | 2026-10-22 00:00:00 |   115.01      |         56.5      | LONG     | Yahoo Finance |
| XOM        | 2026-10-22 00:00:00 |   178.23      |         61.75     | LONG     | Yahoo Finance |
| ZEC-USD    | 2026-10-23 00:00:00 |  1217.33      |         34.1667   | LONG     | Kraken API    |
| AAPL       | 2026-10-22 00:00:00 |   348.22      |         66.5      | NEUTRAL  | Yahoo Finance |
| AAVE-USD   | 2026-10-23 00:00:00 |   148.02      |        -21.3333   | NEUTRAL  | Kraken API    |
| ADBE       | 2026-10-22 00:00:00 |   270.55      |         63.5      | NEUTRAL  | Yahoo Finance |
| AGG        | 2026-10-22 00:00:00 |    96.12      |         23.5833   | NEUTRAL  | Yahoo Finance |
| ALGO-USD   | 2026-10-23 00:00:00 |     0.10848   |        -26.8333   | NEUTRAL  | Kraken API    |
| AMD        | 2026-10-22 00:00:00 |   507.93      |        -16.0833   | NEUTRAL  | Yahoo Finance |
| AMZN       | 2026-10-22 00:00:00 |   250.38      |         18.3333   | NEUTRAL  | Yahoo Finance |
| APT-USD    | 2026-10-23 00:00:00 |     0.7699    |        -13.3333   | NEUTRAL  | Kraken API    |
| ARB-USD    | 2026-10-23 00:00:00 |     0.1831    |         10.0833   | NEUTRAL  | Kraken API    |
| ARKK       | 2026-10-22 00:00:00 |    81.86      |        -25.25     | NEUTRAL  | Yahoo Finance |
| ATOM-USD   | 2026-10-23 00:00:00 |     1.794     |         11.3333   | NEUTRAL  | Kraken API    |
| AVAX-USD   | 2026-10-23 00:00:00 |     9.23      |        -28.8333   | NEUTRAL  | Kraken API    |
| AVGO       | 2026-10-22 00:00:00 |   323.24      |        -65        | NEUTRAL  | Yahoo Finance |
| BA         | 2026-10-22 00:00:00 |   187.55      |        -46.6667   | NEUTRAL  | Yahoo Finance |
| BAC        | 2026-10-22 00:00:00 |    51.08      |        -28.25     | NEUTRAL  | Yahoo Finance |
| BCH-USD    | 2026-10-23 00:00:00 |   282.91      |         -8.91667  | NEUTRAL  | Kraken API    |
| BITO       | 2026-10-22 00:00:00 |    10.86      |        -18.4167   | NEUTRAL  | Yahoo Finance |
| BLK        | 2026-10-22 00:00:00 |  1137.29      |         57.5      | NEUTRAL  | Yahoo Finance |
| BND        | 2026-10-22 00:00:00 |    71.36      |         23.5833   | NEUTRAL  | Yahoo Finance |
| BTC-USD    | 2026-10-23 00:00:00 | 81559         |         -7.25     | NEUTRAL  | Kraken API    |
| CMCSA      | 2026-10-22 00:00:00 |    22.84      |          8.41667  | NEUTRAL  | Yahoo Finance |
| CRV-USD    | 2026-10-23 00:00:00 |     0.36175   |         34.0833   | NEUTRAL  | Kraken API    |
| CSCO       | 2026-10-22 00:00:00 |   104.89      |        -16.25     | NEUTRAL  | Yahoo Finance |
| DBC        | 2026-10-22 00:00:00 |    33.57      |         61.5      | NEUTRAL  | Yahoo Finance |
| DIA        | 2026-10-22 00:00:00 |   527.89      |         63.5      | NEUTRAL  | Yahoo Finance |
| DOT-USD    | 2026-10-23 00:00:00 |     1.171     |        -10.5833   | NEUTRAL  | Kraken API    |
| DXY-INDEX  | 2026-10-23 00:00:00 |   101.666     |         28.4946   | NEUTRAL  | Yahoo Finance |
| EFA        | 2026-10-22 00:00:00 |   103.15      |        -15.6667   | NEUTRAL  | Yahoo Finance |
| ETH-USD    | 2026-10-23 00:00:00 |  2398         |        -13.6667   | NEUTRAL  | Kraken API    |
| EWJ        | 2026-10-22 00:00:00 |    94.6       |        -48.3333   | NEUTRAL  | Yahoo Finance |
| FCX        | 2026-10-22 00:00:00 |    64.59      |        -46.5833   | NEUTRAL  | Yahoo Finance |
| FET-USD    | 2026-10-23 00:00:00 |     0.1872    |        -59.8333   | NEUTRAL  | Kraken API    |
| FIL-USD    | 2026-10-23 00:00:00 |     0.988     |        -15.1667   | NEUTRAL  | Kraken API    |
| FXI        | 2026-10-22 00:00:00 |    32.45      |        -59.6667   | NEUTRAL  | Yahoo Finance |
| GE         | 2026-10-22 00:00:00 |   293.54      |        -69        | NEUTRAL  | Yahoo Finance |
| GOOGL      | 2026-10-22 00:00:00 |   324.22      |        -65        | NEUTRAL  | Yahoo Finance |
| GRT-USD    | 2026-10-23 00:00:00 |     0.02424   |        -24.5833   | NEUTRAL  | Kraken API    |
| HON        | 2026-10-22 00:00:00 |   218.31      |         18.3333   | NEUTRAL  | Yahoo Finance |
| HYG        | 2026-10-22 00:00:00 |    77.1       |        -12.5833   | NEUTRAL  | Yahoo Finance |
| IBIT       | 2026-10-22 00:00:00 |    46.06      |          8.58333  | NEUTRAL  | Yahoo Finance |
| ICP-USD    | 2026-10-23 00:00:00 |     2.752     |        -28.8333   | NEUTRAL  | Kraken API    |
| IEF        | 2026-10-22 00:00:00 |    91.2       |         23.5833   | NEUTRAL  | Yahoo Finance |
| INJ-USD    | 2026-10-23 00:00:00 |     8.223     |         44.25     | NEUTRAL  | Kraken API    |
| IWM        | 2026-10-22 00:00:00 |   276.67      |         -0.166667 | NEUTRAL  | Yahoo Finance |
| JNJ        | 2026-10-22 00:00:00 |   267.61      |         38.6667   | NEUTRAL  | Yahoo Finance |
| LINK-USD   | 2026-10-23 00:00:00 |    12.1266    |         -8.58333  | NEUTRAL  | Kraken API    |
| LTC-USD    | 2026-10-23 00:00:00 |    59.3       |         -8.58333  | NEUTRAL  | Kraken API    |
| MCD        | 2026-10-22 00:00:00 |   252.63      |         21.5833   | NEUTRAL  | Yahoo Finance |
| META       | 2026-10-22 00:00:00 |   648.85      |        -11.3333   | NEUTRAL  | Yahoo Finance |
| MRK        | 2026-10-22 00:00:00 |   147.24      |         62.1667   | NEUTRAL  | Yahoo Finance |
| MSFT       | 2026-10-22 00:00:00 |   521.08      |         13.5833   | NEUTRAL  | Yahoo Finance |
| MU         | 2026-10-22 00:00:00 |   856.49      |        -21.3333   | NEUTRAL  | Yahoo Finance |
| NEAR-USD   | 2026-10-23 00:00:00 |     4.9095    |         16.5833   | NEUTRAL  | Kraken API    |
| NEM        | 2026-10-22 00:00:00 |   114.11      |         -6.41667  | NEUTRAL  | Yahoo Finance |
| NFLX       | 2026-10-22 00:00:00 |    67.05      |        -37.3333   | NEUTRAL  | Yahoo Finance |
| OP-USD     | 2026-10-23 00:00:00 |     0.1198    |        -49.1667   | NEUTRAL  | Kraken API    |
| ORCL       | 2026-10-22 00:00:00 |   125.54      |        -58        | NEUTRAL  | Yahoo Finance |
| PEP        | 2026-10-22 00:00:00 |   138.83      |         26.25     | NEUTRAL  | Yahoo Finance |
| PEPE-USD   | 2026-10-23 00:00:00 |     4.49e-06  |         59.0833   | NEUTRAL  | Kraken API    |
| PFE        | 2026-10-22 00:00:00 |    30.42      |         62        | NEUTRAL  | Yahoo Finance |
| QCOM       | 2026-10-22 00:00:00 |   172.83      |        -45.3333   | NEUTRAL  | Yahoo Finance |
| QQQ        | 2026-10-22 00:00:00 |   704.47      |        -20.8333   | NEUTRAL  | Yahoo Finance |
| RENDER-USD | 2026-10-23 00:00:00 |     1.792     |          0.166667 | NEUTRAL  | Kraken API    |
| SBUX       | 2026-10-22 00:00:00 |   101.91      |         45.3333   | NEUTRAL  | Yahoo Finance |
| SHY        | 2026-10-22 00:00:00 |    81.52      |         14.5833   | NEUTRAL  | Yahoo Finance |
| SKY-USD    | 2026-10-23 00:00:00 |     0.07289   |        -15.9167   | NEUTRAL  | Kraken API    |
| SLB        | 2026-10-22 00:00:00 |    49.55      |         -2        | NEUTRAL  | Yahoo Finance |
| SMH        | 2026-10-22 00:00:00 |   523.35      |        -10.0833   | NEUTRAL  | Yahoo Finance |
| SOL-USD    | 2026-10-23 00:00:00 |   103.76      |        -12.3333   | NEUTRAL  | Kraken API    |
| SOXX       | 2026-10-22 00:00:00 |   475.69      |        -12.0833   | NEUTRAL  | Yahoo Finance |
| SPY        | 2026-10-22 00:00:00 |   763.96      |        -18.3333   | NEUTRAL  | Yahoo Finance |
| TGT        | 2026-10-22 00:00:00 |   158.11      |         56.6667   | NEUTRAL  | Yahoo Finance |
| TIA-USD    | 2026-10-23 00:00:00 |     0.559     |         36.9167   | NEUTRAL  | Kraken API    |
| TLT        | 2026-10-22 00:00:00 |    81.74      |         28.25     | NEUTRAL  | Yahoo Finance |
| TMUS       | 2026-10-22 00:00:00 |   158.79      |        -28.9167   | NEUTRAL  | Yahoo Finance |
| TRX-USD    | 2026-10-23 00:00:00 |     0.329027  |        -20.75     | NEUTRAL  | Kraken API    |
| TSLA       | 2026-10-22 00:00:00 |   374.58      |         19.3333   | NEUTRAL  | Yahoo Finance |
| TXN        | 2026-10-22 00:00:00 |   279.5       |         14.6667   | NEUTRAL  | Yahoo Finance |
| UNI-USD    | 2026-10-23 00:00:00 |     7.1237    |        -12.5833   | NEUTRAL  | Kraken API    |
| UPS        | 2026-10-22 00:00:00 |   101.52      |         28.25     | NEUTRAL  | Yahoo Finance |
| VEA        | 2026-10-22 00:00:00 |    69.26      |        -28        | NEUTRAL  | Yahoo Finance |
| VIXY       | 2026-10-22 00:00:00 |    17.7       |         24.1667   | NEUTRAL  | Yahoo Finance |
| VNQ        | 2026-10-22 00:00:00 |    92.65      |         12.6667   | NEUTRAL  | Yahoo Finance |
| VTI        | 2026-10-22 00:00:00 |   374.9       |        -25        | NEUTRAL  | Yahoo Finance |
| VZ         | 2026-10-22 00:00:00 |    45.2       |         -5.5      | NEUTRAL  | Yahoo Finance |
| WFC        | 2026-10-22 00:00:00 |    83.01      |        -10.0833   | NEUTRAL  | Yahoo Finance |
| XBI        | 2026-10-22 00:00:00 |   151.64      |          0.583333 | NEUTRAL  | Yahoo Finance |
| XLC        | 2026-10-22 00:00:00 |   107.42      |        -60.5      | NEUTRAL  | Yahoo Finance |
| XLI        | 2026-10-22 00:00:00 |   166.73      |        -47.6667   | NEUTRAL  | Yahoo Finance |
| XLK        | 2026-10-22 00:00:00 |   182.34      |        -21.0833   | NEUTRAL  | Yahoo Finance |
| XLV        | 2026-10-22 00:00:00 |   181.3       |         62        | NEUTRAL  | Yahoo Finance |
| XRP-USD    | 2026-10-23 00:00:00 |     1.31578   |        -35.5833   | NEUTRAL  | Kraken API    |
| ADA-USD    | 2026-10-23 00:00:00 |     0.214758  |        -44.5833   | SHORT    | Kraken API    |
| AMAT       | 2026-10-22 00:00:00 |   375.58      |        -62.8333   | SHORT    | Yahoo Finance |
| BONK-USD   | 2026-10-23 00:00:00 |     3.124e-06 |        -40.9167   | SHORT    | Kraken API    |
| C          | 2026-10-22 00:00:00 |   122.51      |        -49.5      | SHORT    | Yahoo Finance |
| CAT        | 2026-10-22 00:00:00 |   704.05      |        -61.5833   | SHORT    | Yahoo Finance |
| DE         | 2026-10-22 00:00:00 |   643.62      |        -31.0833   | SHORT    | Yahoo Finance |
| DOGE-USD   | 2026-10-23 00:00:00 |     0.0792963 |        -41.3333   | SHORT    | Kraken API    |
| EEM        | 2026-10-22 00:00:00 |    61.72      |        -55.8333   | SHORT    | Yahoo Finance |
| ETC-USD    | 2026-10-23 00:00:00 |     7.834     |        -35.25     | SHORT    | Kraken API    |
| GDX        | 2026-10-22 00:00:00 |    81.69      |        -50.5      | SHORT    | Yahoo Finance |
| GDXJ       | 2026-10-22 00:00:00 |   101.2       |        -53.8333   | SHORT    | Yahoo Finance |
| GLD        | 2026-10-22 00:00:00 |   369         |        -46.5      | SHORT    | Yahoo Finance |
| GS         | 2026-10-22 00:00:00 |   891.3       |        -35.4167   | SHORT    | Yahoo Finance |
| HBAR-USD   | 2026-10-23 00:00:00 |     0.08104   |        -49.6667   | SHORT    | Kraken API    |
| IEMG       | 2026-10-22 00:00:00 |    75.44      |        -55.8333   | SHORT    | Yahoo Finance |
| INTC       | 2026-10-22 00:00:00 |    85.49      |        -39.3333   | SHORT    | Yahoo Finance |
| ITA        | 2026-10-22 00:00:00 |   204.48      |        -30.9167   | SHORT    | Yahoo Finance |
| LDO-USD    | 2026-10-23 00:00:00 |     0.389     |        -45.25     | SHORT    | Kraken API    |
| LRCX       | 2026-10-22 00:00:00 |   230.15      |        -67.3333   | SHORT    | Yahoo Finance |
| MS         | 2026-10-22 00:00:00 |   183.97      |        -31.1667   | SHORT    | Yahoo Finance |
| NVDA       | 2026-10-22 00:00:00 |   212.21      |        -17.3333   | SHORT    | Yahoo Finance |
| POL-USD    | 2026-10-23 00:00:00 |     0.09166   |        -37.25     | SHORT    | Kraken API    |
| SCHW       | 2026-10-22 00:00:00 |    91.44      |        -30.25     | SHORT    | Yahoo Finance |
| SHIB-USD   | 2026-10-23 00:00:00 |     5.02e-06  |        -38.5833   | SHORT    | Kraken API    |
| SLV        | 2026-10-22 00:00:00 |    49.34      |        -58.3333   | SHORT    | Yahoo Finance |
| SNX-USD    | 2026-10-23 00:00:00 |     0.2147    |        -46.3333   | SHORT    | Kraken API    |
| SUSHI-USD  | 2026-10-23 00:00:00 |     0.2159    |        -39.25     | SHORT    | Kraken API    |
| T          | 2026-10-22 00:00:00 |    22.74      |        -44.8333   | SHORT    | Yahoo Finance |
| VWO        | 2026-10-22 00:00:00 |    56.85      |        -57.5833   | SHORT    | Yahoo Finance |
| WIF-USD    | 2026-10-23 00:00:00 |     0.2005    |        -41.25     | SHORT    | Kraken API    |
| XLM-USD    | 2026-10-23 00:00:00 |     0.177078  |        -46.3333   | SHORT    | Kraken API    |
| YFI-USD    | 2026-10-23 00:00:00 |  2170.1       |        -38.5833   | SHORT    | Kraken API    |

## Edge Summary

- Symbols with trades: **161** of 161
- Beat buy-and-hold: **32.92%** of traded symbols
- Positive return: **34.16%** of traded symbols
- Median strategy return: **-7.81%** (benchmark **19.50%**)
- Median excess vs benchmark: **-24.89%**
- Median Sharpe: **-0.10**
- Median exposure: **43.93%**

> Edge is real only if both _beat buy-and-hold_ and _median excess_ are convincingly positive across many symbols. Treat a single high-return symbol as noise.

## Portfolio Backtest

Actual capital-allocation books (not per-symbol averages). Benchmarks: `equal_weight_buyhold` (whole tracked universe), `spy_buyhold` (100% SPY), and `sixty_forty` (60% SPY / 40% AGG). `high_conf_voltarget` inverse-vol-weights the HIGH-confidence book; `conviction_long_short` is market-neutral. Judge on **Sharpe** and **max_drawdown** out-of-sample, not raw return: a fully-invested long book wins on return in a bull market but carries all the risk.

| strategy              | scope         | ann_return   | ann_vol   |   sharpe | max_drawdown   | total_return   |   avg_gross_exposure |
|:----------------------|:--------------|:-------------|:----------|---------:|:---------------|:---------------|---------------------:|
| equal_weight_buyhold  | full          | 11.40%       | 28.36%    |     0.4  | -39.53%        | 25.13%         |                 1    |
| equal_weight_buyhold  | out_of_sample | 17.40%       | 27.22%    |     0.64 | -16.18%        | 15.70%         |                 1    |
| all_signals_ew        | full          | -14.24%      | 24.32%    |    -0.59 | -56.33%        | -40.72%        |                 1    |
| all_signals_ew        | out_of_sample | 1.58%        | 22.99%    |     0.07 | -23.10%        | -1.11%         |                 1    |
| high_conf_ew          | full          | -2.54%       | 31.66%    |    -0.08 | -44.55%        | -20.35%        |                 0.9  |
| high_conf_ew          | out_of_sample | 10.22%       | 28.13%    |     0.36 | -22.85%        | 6.81%          |                 0.9  |
| high_conf_voltarget   | full          | -4.31%       | 28.42%    |    -0.15 | -39.67%        | -22.23%        |                 0.9  |
| high_conf_voltarget   | out_of_sample | -0.37%       | 23.27%    |    -0.02 | -17.69%        | -3.31%         |                 0.9  |
| conviction_long_short | full          | -13.50%      | 22.26%    |    -0.61 | -47.93%        | -38.50%        |                 0.97 |
| conviction_long_short | out_of_sample | -3.23%       | 19.41%    |    -0.17 | -26.60%        | -5.29%         |                 0.97 |
| spy_buyhold           | full          | 5.20%        | 13.66%    |     0.38 | -19.00%        | 13.86%         |                 0.79 |
| spy_buyhold           | out_of_sample | -1.39%       | 10.06%    |    -0.14 | -11.61%        | -1.99%         |                 0.79 |
| sixty_forty           | full          | 2.93%        | 8.60%     |     0.34 | -11.66%        | 8.08%          |                 0.79 |
| sixty_forty           | out_of_sample | -2.47%       | 6.72%     |    -0.37 | -8.19%         | -2.82%         |                 0.79 |

## Walk-Forward Robustness

Each book measured across contiguous time folds (each a different regime). A book has durable edge only if `mean_sharpe` is positive, `min_sharpe` isn't deeply negative, and `pct_positive_folds` is high — a single great fold doesn't count. `fold_sharpes` lists each fold oldest-to-newest.

| strategy              |   n_folds |   mean_sharpe |   median_sharpe |   min_sharpe | pct_positive_folds   | mean_return   | fold_sharpes                |
|:----------------------|----------:|--------------:|----------------:|-------------:|:---------------------|:--------------|:----------------------------|
| equal_weight_buyhold  |         5 |          0.64 |            1.06 |        -0.96 | 60.00%               | 6.59%         | 1.06;1.97;-0.96;-0.08;1.21  |
| all_signals_ew        |         5 |         -0.6  |           -0.63 |        -2.38 | 40.00%               | -7.74%        | -1.34;0.11;-2.38;1.26;-0.63 |
| high_conf_ew          |         5 |          0.06 |           -0.17 |        -1.13 | 40.00%               | -2.63%        | 0.24;-0.18;-1.13;1.56;-0.17 |
| high_conf_voltarget   |         5 |          0    |           -0.16 |        -0.95 | 40.00%               | -4.01%        | 0.43;-0.16;-0.95;0.88;-0.17 |
| conviction_long_short |         5 |         -0.59 |           -0.75 |        -1.95 | 40.00%               | -8.76%        | -1.95;0.32;-0.82;-0.75;0.27 |
| spy_buyhold           |         5 |          0.31 |            0.34 |        -0.74 | 60.00%               | 2.77%         | 1.44;0.34;-0.17;0.70;-0.74  |
| sixty_forty           |         5 |          0.26 |            0.36 |        -0.84 | 60.00%               | 1.62%         | 1.35;0.41;-0.00;0.36;-0.84  |

## Strategy Comparison

Each decision rule backtested over the same data. `out_of_sample` is the most recent ~35% of each symbol's history (unseen tail). A rule has real edge only if `median_excess` and `beat_benchmark_pct` stay positive out-of-sample, not just full-sample.

| strategy        | scope         |   symbols | beat_benchmark_pct   | positive_pct   | median_return   | median_benchmark   | median_excess   |   median_sharpe |   total_trades |
|:----------------|:--------------|----------:|:---------------------|:---------------|:----------------|:-------------------|:----------------|----------------:|---------------:|
| trend           | full          |       161 | 32.92%               | 34.16%         | -7.81%          | 19.50%             | -24.89%         |           -0.1  |          11286 |
| trend           | out_of_sample |       161 | 31.06%               | 51.55%         | 0.12%           | 5.30%              | -10.23%         |            0.07 |           3804 |
| mean_reversion  | full          |       157 | 36.31%               | 49.04%         | -0.23%          | 19.11%             | -19.50%         |           -0.01 |           1236 |
| mean_reversion  | out_of_sample |       123 | 33.33%               | 52.03%         | 0.22%           | 4.81%              | -6.49%          |            0.16 |            476 |
| regime_adaptive | full          |       161 | 33.54%               | 34.16%         | -7.91%          | 19.50%             | -23.79%         |           -0.1  |          11550 |
| regime_adaptive | out_of_sample |       161 | 29.81%               | 51.55%         | 0.12%           | 5.30%              | -10.93%         |            0.07 |           3908 |

## Signal Calibration

Realized forward return in the signal's direction, grouped by confidence. HIGH should outrank LOW for the confidence score to be meaningful.

| confidence_level   |   horizon |     n | mean_return   | median_return   | win_rate   |
|:-------------------|----------:|------:|:--------------|:----------------|:-----------|
| HIGH               |         5 |  7821 | 0.23%         | 0.06%           | 51.02%     |
| MEDIUM             |         5 | 29102 | 0.05%         | 0.04%           | 50.38%     |
| LOW                |         5 |  3538 | -0.39%        | -0.39%          | 46.16%     |
| ALL                |         5 | 40461 | 0.05%         | 0.01%           | 50.13%     |
| HIGH               |        10 |  7768 | 0.41%         | 0.06%           | 50.55%     |
| MEDIUM             |        10 | 28906 | 0.14%         | 0.03%           | 50.26%     |
| LOW                |        10 |  3482 | -0.76%        | -0.51%          | 46.87%     |
| ALL                |        10 | 40156 | 0.11%         | 0.01%           | 50.02%     |
| HIGH               |        20 |  7698 | 0.90%         | 0.21%           | 51.70%     |
| MEDIUM             |        20 | 28381 | 0.85%         | 0.55%           | 53.08%     |
| LOW                |        20 |  3373 | -0.45%        | -0.58%          | 47.26%     |
| ALL                |        20 | 39452 | 0.75%         | 0.40%           | 52.32%     |

## Backtest Summary

### Data Quality / Signal Availability

- **ok**: 161 symbols

| symbol     |   trades | return   | benchmark_return   | mdd     |   sharpe | exposure   | skipped_reason   |
|:-----------|---------:|:---------|:-------------------|:--------|---------:|:-----------|:-----------------|
| AAPL       |       63 | 6.22%    | 81.13%             | -20.65% |     0.23 | 49.75%     | ok               |
| AAVE-USD   |       67 | -47.32%  | -42.92%            | -68.26% |    -0.4  | 40.80%     | ok               |
| ABBV       |       68 | -19.27%  | 76.87%             | -30.52% |    -0.38 | 48.42%     | ok               |
| ADA-USD    |       74 | -28.98%  | -71.21%            | -53.34% |    -0.16 | 45.02%     | ok               |
| ADBE       |       71 | -11.61%  | -39.17%            | -31.20% |    -0.03 | 56.91%     | ok               |
| AGG        |       63 | -5.89%   | -0.41%             | -10.74% |    -0.92 | 33.28%     | ok               |
| ALGO-USD   |       76 | -27.99%  | -51.64%            | -39.25% |    -0.16 | 40.04%     | ok               |
| AMAT       |       73 | -33.32%  | 74.62%             | -57.08% |    -0.28 | 51.25%     | ok               |
| AMD        |       54 | 17.68%   | 204.33%            | -40.85% |     0.38 | 36.94%     | ok               |
| AMGN       |       65 | -7.81%   | 46.24%             | -34.19% |    -0.08 | 51.41%     | ok               |
| AMZN       |       82 | -58.58%  | 41.91%             | -59.01% |    -1.71 | 41.26%     | ok               |
| APT-USD    |       72 | -27.31%  | -85.08%            | -57.84% |    -0.06 | 39.85%     | ok               |
| ARB-USD    |       77 | -9.52%   | -53.54%            | -48.19% |     0.19 | 43.30%     | ok               |
| ARKK       |       89 | -29.66%  | 92.84%             | -34.52% |    -0.45 | 43.43%     | ok               |
| ATOM-USD   |       86 | -56.15%  | -63.00%            | -59.23% |    -0.75 | 48.66%     | ok               |
| AVAX-USD   |       66 | -32.18%  | -59.11%            | -45.41% |    -0.24 | 39.66%     | ok               |
| AVGO       |       62 | 23.31%   | 143.30%            | -36.09% |     0.42 | 40.60%     | ok               |
| BA         |       69 | 12.10%   | 5.60%              | -24.47% |     0.32 | 50.75%     | ok               |
| BAC        |       78 | -10.08%  | 27.73%             | -25.28% |    -0.2  | 50.08%     | ok               |
| BCH-USD    |       78 | 3.16%    | -28.18%            | -53.87% |     0.25 | 47.70%     | ok               |
| BITO       |       81 | -24.94%  | -60.19%            | -43.10% |    -0.18 | 40.93%     | ok               |
| BLK        |       81 | -11.50%  | 47.31%             | -26.90% |    -0.26 | 46.09%     | ok               |
| BND        |       64 | -6.07%   | -0.39%             | -10.80% |    -0.93 | 34.78%     | ok               |
| BONK-USD   |       74 | 10.47%   | -84.40%            | -51.50% |     0.37 | 46.36%     | ok               |
| BTC-USD    |       74 | -2.67%   | -23.67%            | -23.38% |     0.09 | 50.57%     | ok               |
| C          |       79 | -34.01%  | 96.61%             | -39.84% |    -0.73 | 46.59%     | ok               |
| CAT        |       70 | 10.71%   | 107.98%            | -21.87% |     0.29 | 48.75%     | ok               |
| CL         |       64 | 5.19%    | 4.77%              | -14.32% |     0.23 | 39.10%     | ok               |
| CMCSA      |       84 | -37.44%  | -39.12%            | -46.48% |    -0.91 | 43.43%     | ok               |
| COMP-USD   |       95 | -33.03%  | -42.85%            | -52.27% |    -0.13 | 50.77%     | ok               |
| COP        |       68 | -10.73%  | 25.03%             | -43.40% |    -0.1  | 44.43%     | ok               |
| COST       |       60 | 2.51%    | 25.72%             | -31.32% |     0.15 | 41.10%     | ok               |
| CRM        |       67 | -22.74%  | 6.76%              | -41.12% |    -0.26 | 47.25%     | ok               |
| CRV-USD    |       64 | 42.17%   | -48.93%            | -39.89% |     0.58 | 36.40%     | ok               |
| CSCO       |       64 | 9.12%    | 125.57%            | -22.29% |     0.27 | 49.75%     | ok               |
| CVX        |       73 | -13.51%  | 39.67%             | -29.13% |    -0.29 | 42.60%     | ok               |
| DASH-USD   |       53 | 6.20%    | 134.25%            | -64.43% |     0.42 | 30.27%     | ok               |
| DBC        |       64 | -7.79%   | 44.26%             | -24.10% |    -0.2  | 35.61%     | ok               |
| DE         |       70 | -9.78%   | 71.74%             | -23.86% |    -0.12 | 43.93%     | ok               |
| DIA        |       64 | -4.46%   | 36.22%             | -12.94% |    -0.21 | 43.26%     | ok               |
| DIS        |       62 | -2.65%   | 8.87%              | -28.17% |     0.03 | 44.09%     | ok               |
| DOGE-USD   |       67 | -16.74%  | -64.96%            | -60.95% |     0.04 | 49.04%     | ok               |
| DOT-USD    |       84 | -48.42%  | -74.95%            | -63.33% |    -0.37 | 47.70%     | ok               |
| DXY-INDEX  |       40 | -1.43%   | -5.90%             | -6.29%  |    -0.21 | 32.47%     | ok               |
| EEM        |       64 | -7.62%   | 47.69%             | -22.68% |    -0.19 | 39.43%     | ok               |
| EFA        |       66 | -13.56%  | 27.06%             | -14.82% |    -0.56 | 39.93%     | ok               |
| EOG        |       78 | -25.50%  | 26.82%             | -47.87% |    -0.51 | 45.26%     | ok               |
| ETC-USD    |       58 | -19.67%  | -57.55%            | -47.84% |    -0.15 | 32.76%     | ok               |
| ETH-USD    |       58 | 143.96%  | -5.02%             | -30.11% |     1.31 | 46.55%     | ok               |
| EWJ        |       62 | -24.44%  | 37.16%             | -30.73% |    -0.87 | 36.27%     | ok               |
| FCX        |       67 | -33.67%  | 22.49%             | -46.84% |    -0.41 | 43.93%     | ok               |
| FET-USD    |       81 | -47.69%  | -75.10%            | -65.38% |    -0.31 | 42.72%     | ok               |
| FIL-USD    |       65 | -40.15%  | -65.51%            | -58.54% |    -0.34 | 37.16%     | ok               |
| FXI        |       46 | -3.03%   | 21.86%             | -23.91% |     0.01 | 30.12%     | ok               |
| GDX        |       64 | -0.42%   | 131.42%            | -33.31% |     0.13 | 43.76%     | ok               |
| GDXJ       |       72 | -30.60%  | 124.24%            | -39.24% |    -0.34 | 43.09%     | ok               |
| GE         |       76 | -8.43%   | 77.75%             | -27.82% |    -0.04 | 48.09%     | ok               |
| GLD        |       50 | 12.75%   | 71.39%             | -13.87% |     0.38 | 45.59%     | ok               |
| GOOGL      |       53 | 60.67%   | 87.95%             | -17.15% |     1.05 | 46.26%     | ok               |
| GRT-USD    |       83 | 54.07%   | -78.11%            | -35.21% |     0.67 | 46.17%     | ok               |
| GS         |       68 | -3.12%   | 95.24%             | -21.94% |     0.03 | 48.09%     | ok               |
| HBAR-USD   |       40 | -40.46%  | -21.42%            | -56.47% |    -0.82 | 39.71%     | ok               |
| HD         |       69 | 0.85%    | -2.13%             | -17.15% |     0.1  | 43.43%     | ok               |
| HON        |       91 | -26.59%  | 9.23%              | -34.05% |    -0.66 | 54.58%     | ok               |
| HYG        |       89 | -7.38%   | -0.04%             | -10.59% |    -0.83 | 39.10%     | ok               |
| IBIT       |       42 | 34.57%   | 21.18%             | -18.95% |     0.64 | 35.07%     | ok               |
| IBM        |       69 | -18.28%  | 51.10%             | -48.94% |    -0.16 | 49.08%     | ok               |
| ICP-USD    |       75 | -11.08%  | -47.80%            | -42.43% |     0.16 | 39.27%     | ok               |
| IEF        |       74 | -9.01%   | -1.72%             | -12.66% |    -1.21 | 33.78%     | ok               |
| IEMG       |       60 | -6.47%   | 43.45%             | -24.73% |    -0.16 | 39.43%     | ok               |
| INJ-USD    |       63 | -27.85%  | -32.17%            | -68.17% |    -0.03 | 40.23%     | ok               |
| INTC       |       66 | 41.91%   | 177.12%            | -60.60% |     0.54 | 47.92%     | ok               |
| INTU       |       73 | 4.88%    | -38.43%            | -38.67% |     0.21 | 46.92%     | ok               |
| ITA        |       78 | 0.37%    | 50.33%             | -23.75% |     0.09 | 48.42%     | ok               |
| IWM        |       54 | 8.07%    | 34.46%             | -8.93%  |     0.35 | 34.28%     | ok               |
| JNJ        |       58 | 11.84%   | 82.46%             | -16.86% |     0.47 | 46.09%     | ok               |
| JPM        |       77 | -25.21%  | 66.09%             | -32.74% |    -0.72 | 44.43%     | ok               |
| KO         |       54 | 29.61%   | 51.50%             | -8.64%  |     1    | 37.44%     | ok               |
| LDO-USD    |       68 | 39.37%   | -55.39%            | -50.81% |     0.56 | 46.93%     | ok               |
| LIN        |       72 | -6.60%   | 17.18%             | -20.61% |    -0.18 | 39.10%     | ok               |
| LINK-USD   |       64 | 56.97%   | -22.80%            | -33.64% |     0.71 | 44.44%     | ok               |
| LLY        |       80 | -31.87%  | 59.29%             | -53.61% |    -0.49 | 49.42%     | ok               |
| LRCX       |       84 | -22.50%  | 146.83%            | -61.08% |    -0.1  | 43.43%     | ok               |
| LTC-USD    |       66 | 7.29%    | -37.21%            | -30.78% |     0.28 | 51.34%     | ok               |
| MCD        |       77 | -2.68%   | -2.42%             | -22.20% |    -0.05 | 40.43%     | ok               |
| META       |       72 | -26.70%  | 38.99%             | -44.90% |    -0.36 | 50.08%     | ok               |
| MPC        |       72 | 15.67%   | 160.05%            | -34.29% |     0.37 | 52.91%     | ok               |
| MRK        |       65 | -23.45%  | 17.29%             | -35.95% |    -0.45 | 42.43%     | ok               |
| MS         |       75 | -6.95%   | 88.03%             | -27.79% |    -0.08 | 48.09%     | ok               |
| MSFT       |       81 | -25.29%  | 25.52%             | -39.15% |    -0.54 | 51.58%     | ok               |
| MU         |       51 | 145.07%  | 585.19%            | -68.76% |     1.02 | 51.58%     | ok               |
| NEAR-USD   |       72 | 144.05%  | 74.53%             | -50.77% |     1.02 | 44.44%     | ok               |
| NEM        |       72 | -28.27%  | 172.08%            | -41.53% |    -0.29 | 49.58%     | ok               |
| NFLX       |       80 | 1.49%    | 4.50%              | -21.85% |     0.13 | 52.08%     | ok               |
| NKE        |       81 | -30.33%  | -59.68%            | -55.35% |    -0.36 | 47.09%     | ok               |
| NOW        |       82 | 12.38%   | 19.50%             | -30.43% |     0.31 | 50.25%     | ok               |
| NVDA       |       79 | -55.13%  | 104.58%            | -52.95% |    -0.86 | 55.97%     | ok               |
| OP-USD     |       70 | -43.71%  | -83.40%            | -60.45% |    -0.37 | 32.76%     | ok               |
| ORCL       |       60 | 97.55%   | 7.13%              | -30.61% |     0.86 | 51.25%     | ok               |
| OXY        |       67 | 6.18%    | 0.00%              | -28.48% |     0.23 | 43.09%     | ok               |
| PEP        |       72 | 1.75%    | -19.71%            | -21.35% |     0.12 | 45.26%     | ok               |
| PEPE-USD   |       81 | -50.17%  | -65.90%            | -61.29% |    -0.34 | 47.51%     | ok               |
| PFE        |       77 | -33.11%  | 6.14%              | -41.77% |    -1.03 | 36.27%     | ok               |
| PG         |       64 | -17.58%  | 0.64%              | -24.55% |    -0.63 | 34.78%     | ok               |
| PM         |       81 | -11.33%  | 98.99%             | -38.30% |    -0.17 | 49.58%     | ok               |
| POL-USD    |       79 | 56.48%   | -60.55%            | -39.06% |     0.71 | 50.77%     | ok               |
| QCOM       |       77 | -28.88%  | -15.30%            | -56.59% |    -0.24 | 42.43%     | ok               |
| QQQ        |       66 | 8.16%    | 56.30%             | -13.49% |     0.29 | 44.59%     | ok               |
| RENDER-USD |       90 | -24.47%  | -61.43%            | -45.71% |     0.01 | 47.13%     | ok               |
| RTX        |       68 | 25.60%   | 80.60%             | -16.99% |     0.61 | 51.75%     | ok               |
| SBUX       |       62 | -12.19%  | 27.04%             | -29.22% |    -0.18 | 38.94%     | ok               |
| SCHW       |       82 | -14.42%  | 24.78%             | -31.92% |    -0.29 | 46.59%     | ok               |
| SHIB-USD   |       79 | -30.75%  | -65.66%            | -46.79% |    -0.25 | 53.26%     | ok               |
| SHY        |       48 | -1.87%   | 0.06%              | -3.30%  |    -0.63 | 36.94%     | ok               |
| SKY-USD    |       87 | -58.48%  | 1.39%              | -62.30% |    -0.92 | 42.91%     | ok               |
| SLB        |       74 | -40.46%  | 7.98%              | -57.55% |    -0.78 | 49.25%     | ok               |
| SLV        |       68 | 18.81%   | 77.74%             | -41.17% |     0.4  | 40.10%     | ok               |
| SMH        |       50 | 45.19%   | 117.63%            | -33.99% |     0.75 | 42.60%     | ok               |
| SNX-USD    |       62 | -5.12%   | -73.62%            | -50.74% |     0.16 | 34.87%     | ok               |
| SOL-USD    |       72 | -15.70%  | -38.47%            | -44.99% |     0.05 | 59.00%     | ok               |
| SOXX       |       56 | 58.31%   | 103.28%            | -40.14% |     0.85 | 42.10%     | ok               |
| SPY        |       62 | 1.31%    | 44.86%             | -15.53% |     0.11 | 48.59%     | ok               |
| SUSHI-USD  |       92 | -72.70%  | -69.88%            | -79.84% |    -1.06 | 40.23%     | ok               |
| T          |       70 | 43.50%   | 24.81%             | -17.01% |     0.84 | 56.91%     | ok               |
| TGT        |       60 | -11.06%  | 1.25%              | -34.42% |    -0.16 | 37.60%     | ok               |
| TIA-USD    |       91 | -36.08%  | -79.06%            | -74.53% |    -0.07 | 43.30%     | ok               |
| TLT        |       66 | -18.82%  | -9.63%             | -22.01% |    -1.42 | 33.11%     | ok               |
| TMO        |       69 | 36.14%   | 19.11%             | -18.85% |     0.7  | 56.57%     | ok               |
| TMUS       |       74 | -4.80%   | -9.24%             | -33.03% |    -0    | 48.92%     | ok               |
| TRX-USD    |       66 | 2.37%    | 22.19%             | -22.90% |     0.15 | 49.23%     | ok               |
| TSLA       |       78 | -35.00%  | 110.34%            | -59.64% |    -0.22 | 42.76%     | ok               |
| TXN        |       79 | -26.83%  | 43.33%             | -46.56% |    -0.3  | 49.92%     | ok               |
| UNH        |       75 | 45.32%   | -14.21%            | -26.31% |     0.68 | 48.59%     | ok               |
| UNI-USD    |       88 | -33.54%  | 18.35%             | -68.13% |    -0.07 | 49.62%     | ok               |
| UPS        |       74 | -39.79%  | -26.93%            | -41.48% |    -0.83 | 41.93%     | ok               |
| USO        |       67 | -5.65%   | 117.20%            | -43.39% |     0.05 | 33.28%     | ok               |
| VEA        |       64 | -5.21%   | 36.55%             | -18.84% |    -0.17 | 41.43%     | ok               |
| VIXY       |       92 | -77.35%  | -61.32%            | -88.17% |    -0.92 | 31.45%     | ok               |
| VNQ        |       71 | -12.02%  | 11.30%             | -24.66% |    -0.47 | 39.77%     | ok               |
| VTI        |       66 | -8.66%   | 43.95%             | -18.77% |    -0.27 | 48.42%     | ok               |
| VWO        |       78 | -15.84%  | 31.96%             | -25.20% |    -0.58 | 39.43%     | ok               |
| VZ         |       84 | -26.67%  | 9.84%              | -30.28% |    -0.81 | 42.76%     | ok               |
| WFC        |       82 | -20.92%  | 38.53%             | -29.78% |    -0.37 | 46.76%     | ok               |
| WIF-USD    |       66 | -28.55%  | -79.43%            | -52.76% |    -0.03 | 38.89%     | ok               |
| WMT        |       71 | 5.48%    | 84.18%             | -25.96% |     0.22 | 48.42%     | ok               |
| XBI        |       62 | 0.99%    | 70.13%             | -17.66% |     0.11 | 38.27%     | ok               |
| XLB        |       68 | -12.36%  | 12.95%             | -24.92% |    -0.43 | 31.95%     | ok               |
| XLC        |       61 | 12.05%   | 29.02%             | -12.33% |     0.46 | 49.25%     | ok               |
| XLE        |       69 | -3.08%   | 45.00%             | -28.90% |     0.01 | 46.26%     | ok               |
| XLF        |       82 | -5.85%   | 36.05%             | -23.61% |    -0.15 | 46.92%     | ok               |
| XLI        |       80 | -8.77%   | 34.99%             | -17.75% |    -0.3  | 42.60%     | ok               |
| XLK        |       44 | 50.25%   | 73.52%             | -14.75% |     1    | 45.26%     | ok               |
| XLM-USD    |       66 | 6.76%    | -38.45%            | -54.58% |     0.29 | 48.08%     | ok               |
| XLP        |       65 | 14.14%   | 16.36%             | -8.96%  |     0.75 | 38.77%     | ok               |
| XLU        |       71 | -4.89%   | 17.90%             | -20.40% |    -0.17 | 38.77%     | ok               |
| XLV        |       74 | -20.38%  | 26.17%             | -22.75% |    -0.97 | 36.27%     | ok               |
| XLY        |       73 | -3.52%   | 30.72%             | -18.35% |    -0.04 | 47.42%     | ok               |
| XOM        |       57 | 3.74%    | 52.00%             | -20.29% |     0.18 | 35.11%     | ok               |
| XRP-USD    |       66 | 6.40%    | -44.15%            | -33.91% |     0.27 | 35.82%     | ok               |
| YFI-USD    |       77 | -57.64%  | -61.79%            | -60.14% |    -1.01 | 38.70%     | ok               |
| ZEC-USD    |       59 | 133.60%  | 2854.68%           | -56.50% |     0.88 | 40.23%     | ok               |

## AAPL Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 12.86%   | 81.13%             | -21.71% |     0.34 |       72 | 54.58%     | ok               |
|          15 | 9.96%    | 81.13%             | -23.86% |     0.29 |       81 | 61.90%     | ok               |
|          30 | 6.22%    | 81.13%             | -20.65% |     0.23 |       63 | 49.75%     | ok               |
|          35 | 4.70%    | 81.13%             | -22.04% |     0.2  |       63 | 48.42%     | ok               |
|          25 | 1.92%    | 81.13%             | -20.87% |     0.15 |       73 | 51.91%     | ok               |

## AAVE-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 10.18%   | -42.92%            | -43.61% |     0.32 |       43 | 35.06%     | ok               |
|          50 | 1.45%    | -42.92%            | -45.07% |     0.2  |       44 | 22.41%     | ok               |
|          45 | -0.09%   | -42.92%            | -49.19% |     0.2  |       48 | 29.89%     | ok               |
|          35 | -9.83%   | -42.92%            | -51.96% |     0.11 |       53 | 38.31%     | ok               |
|          15 | -45.85%  | -42.92%            | -61.76% |    -0.27 |       74 | 53.64%     | ok               |

## ABBV Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -5.83%   | 76.87%             | -23.85% |    -0.07 |       54 | 35.94%     | ok               |
|          20 | -16.11%  | 76.87%             | -28.73% |    -0.29 |       64 | 51.75%     | ok               |
|          25 | -16.20%  | 76.87%             | -30.04% |    -0.3  |       67 | 50.25%     | ok               |
|          30 | -19.27%  | 76.87%             | -30.52% |    -0.38 |       68 | 48.42%     | ok               |
|          40 | -19.32%  | 76.87%             | -27.36% |    -0.43 |       70 | 41.43%     | ok               |

## ADA-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 24.35%   | -71.21%            | -34.64% |     0.47 |       44 | 30.65%     | ok               |
|          50 | 17.24%   | -71.21%            | -35.54% |     0.39 |       46 | 26.25%     | ok               |
|          40 | 4.17%    | -71.21%            | -40.73% |     0.25 |       56 | 36.59%     | ok               |
|          35 | -8.49%   | -71.21%            | -44.83% |     0.11 |       62 | 40.42%     | ok               |
|          15 | -17.21%  | -71.21%            | -47.27% |     0.1  |       73 | 60.54%     | ok               |

## ADBE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | 6.66%    | -39.17%            | -29.07% |     0.24 |       55 | 61.06%     | ok               |
|          35 | -3.98%   | -39.17%            | -31.73% |     0.06 |       78 | 48.25%     | ok               |
|          20 | -7.31%   | -39.17%            | -31.52% |     0.05 |       61 | 64.06%     | ok               |
|          30 | -11.61%  | -39.17%            | -31.20% |    -0.03 |       71 | 56.91%     | ok               |
|          15 | -14.48%  | -39.17%            | -34.98% |    -0.05 |       64 | 65.72%     | ok               |

## AGG Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -5.06%   | -0.41%             | -9.39%  |    -0.91 |       60 | 24.46%     | ok               |
|          30 | -5.89%   | -0.41%             | -10.74% |    -0.92 |       63 | 33.28%     | ok               |
|          35 | -6.72%   | -0.41%             | -11.53% |    -1.08 |       62 | 30.28%     | ok               |
|          20 | -7.79%   | -0.41%             | -11.89% |    -1.12 |       68 | 38.10%     | ok               |
|          25 | -7.62%   | -0.41%             | -12.28% |    -1.14 |       69 | 36.27%     | ok               |

## ALGO-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -27.99%  | -51.64%            | -39.25% |    -0.16 |       76 | 40.04%     | ok               |
|          25 | -37.57%  | -51.64%            | -51.92% |    -0.28 |       80 | 45.02%     | ok               |
|          15 | -45.27%  | -51.64%            | -53.34% |    -0.38 |       77 | 51.34%     | ok               |
|          35 | -40.58%  | -51.64%            | -52.80% |    -0.46 |       64 | 34.87%     | ok               |
|          20 | -48.69%  | -51.64%            | -53.98% |    -0.47 |       81 | 48.08%     | ok               |

## AMAT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -23.72%  | 74.62%             | -54.01% |    -0.09 |       74 | 60.73%     | ok               |
|          50 | -29.51%  | 74.62%             | -48.13% |    -0.27 |       50 | 36.61%     | ok               |
|          30 | -33.32%  | 74.62%             | -57.08% |    -0.28 |       73 | 51.25%     | ok               |
|          35 | -33.04%  | 74.62%             | -54.63% |    -0.29 |       73 | 48.75%     | ok               |
|          20 | -39.31%  | 74.62%             | -60.13% |    -0.35 |       78 | 56.74%     | ok               |

## AMD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 28.37%   | 204.33%            | -38.43% |     0.47 |       54 | 31.95%     | ok               |
|          40 | 17.68%   | 204.33%            | -40.85% |     0.38 |       54 | 36.94%     | ok               |
|          35 | 12.62%   | 204.33%            | -42.92% |     0.33 |       62 | 38.60%     | ok               |
|          45 | 2.46%    | 204.33%            | -48.35% |     0.23 |       60 | 34.78%     | ok               |
|          30 | -2.23%   | 204.33%            | -49.58% |     0.2  |       63 | 41.10%     | ok               |

## AMGN Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -3.26%   | 46.24%             | -26.89% |     0.03 |       64 | 56.57%     | ok               |
|          35 | -5.49%   | 46.24%             | -31.29% |    -0.03 |       67 | 48.09%     | ok               |
|          30 | -7.81%   | 46.24%             | -34.19% |    -0.08 |       65 | 51.41%     | ok               |
|          15 | -10.42%  | 46.24%             | -28.21% |    -0.12 |       63 | 60.57%     | ok               |
|          25 | -9.71%   | 46.24%             | -33.47% |    -0.12 |       61 | 53.58%     | ok               |

## AMZN Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -31.28%  | 41.91%             | -32.17% |    -0.97 |       58 | 30.12%     | ok               |
|          50 | -34.88%  | 41.91%             | -35.56% |    -1.27 |       52 | 22.96%     | ok               |
|          45 | -40.33%  | 41.91%             | -40.96% |    -1.45 |       60 | 26.62%     | ok               |
|          35 | -53.71%  | 41.91%             | -54.20% |    -1.59 |       77 | 35.27%     | ok               |
|          30 | -58.58%  | 41.91%             | -59.01% |    -1.71 |       82 | 41.26%     | ok               |

## APT-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 39.32%   | -85.08%            | -27.79% |     0.68 |       42 | 16.86%     | ok               |
|          45 | -0.07%   | -85.08%            | -52.90% |     0.2  |       56 | 23.56%     | ok               |
|          20 | -15.00%  | -85.08%            | -57.07% |     0.14 |       80 | 49.62%     | ok               |
|          35 | -14.40%  | -85.08%            | -49.10% |     0.07 |       68 | 35.44%     | ok               |
|          30 | -27.31%  | -85.08%            | -57.84% |    -0.06 |       72 | 39.85%     | ok               |

## ARB-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 57.32%   | -53.54%            | -33.60% |     0.67 |       54 | 26.44%     | ok               |
|          50 | 46.51%   | -53.54%            | -30.72% |     0.61 |       42 | 19.35%     | ok               |
|          15 | 37.63%   | -53.54%            | -46.19% |     0.55 |       88 | 58.05%     | ok               |
|          40 | 27.44%   | -53.54%            | -40.13% |     0.48 |       55 | 33.72%     | ok               |
|          35 | 21.94%   | -53.54%            | -45.71% |     0.44 |       71 | 37.93%     | ok               |

## ARKK Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -15.43%  | 92.84%             | -37.76% |    -0.09 |       96 | 55.24%     | ok               |
|          20 | -24.64%  | 92.84%             | -34.82% |    -0.28 |       93 | 50.08%     | ok               |
|          30 | -29.66%  | 92.84%             | -34.52% |    -0.45 |       89 | 43.43%     | ok               |
|          35 | -34.57%  | 92.84%             | -37.45% |    -0.6  |       90 | 40.60%     | ok               |
|          25 | -39.79%  | 92.84%             | -46.36% |    -0.67 |       99 | 45.92%     | ok               |

## ATOM-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -38.30%  | -63.00%            | -48.20% |    -0.28 |       84 | 65.13%     | ok               |
|          25 | -44.22%  | -63.00%            | -51.32% |    -0.43 |       88 | 54.41%     | ok               |
|          20 | -50.33%  | -63.00%            | -57.28% |    -0.54 |       92 | 57.85%     | ok               |
|          30 | -56.15%  | -63.00%            | -59.23% |    -0.75 |       86 | 48.66%     | ok               |
|          35 | -58.34%  | -63.00%            | -62.37% |    -0.91 |       82 | 42.72%     | ok               |

## AVAX-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 53.25%   | -59.11%            | -22.06% |     0.83 |       32 | 19.73%     | ok               |
|          40 | 10.80%   | -59.11%            | -32.06% |     0.31 |       36 | 27.78%     | ok               |
|          45 | 8.12%    | -59.11%            | -28.93% |     0.28 |       30 | 24.52%     | ok               |
|          15 | -5.67%   | -59.11%            | -43.71% |     0.17 |       71 | 52.11%     | ok               |
|          35 | -7.87%   | -59.11%            | -37.03% |     0.08 |       52 | 33.72%     | ok               |

## AVGO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | 26.86%   | 143.30%            | -38.01% |     0.46 |       66 | 43.26%     | ok               |
|          30 | 23.31%   | 143.30%            | -36.09% |     0.42 |       62 | 40.60%     | ok               |
|          50 | 14.97%   | 143.30%            | -36.86% |     0.34 |       54 | 28.62%     | ok               |
|          20 | 12.31%   | 143.30%            | -39.42% |     0.31 |       75 | 46.42%     | ok               |
|          35 | 11.38%   | 143.30%            | -40.43% |     0.3  |       72 | 37.77%     | ok               |

## BA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 44.60%   | 5.60%              | -13.34% |     0.96 |       44 | 35.11%     | ok               |
|          40 | 35.09%   | 5.60%              | -23.87% |     0.68 |       44 | 42.60%     | ok               |
|          35 | 31.46%   | 5.60%              | -18.09% |     0.6  |       64 | 47.25%     | ok               |
|          25 | 22.50%   | 5.60%              | -26.02% |     0.46 |       70 | 54.24%     | ok               |
|          30 | 12.10%   | 5.60%              | -24.47% |     0.32 |       69 | 50.75%     | ok               |

## BAC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -3.35%   | 27.73%             | -18.35% |     0    |       82 | 54.74%     | ok               |
|          15 | -6.38%   | 27.73%             | -21.05% |    -0.06 |       86 | 61.06%     | ok               |
|          35 | -4.96%   | 27.73%             | -26.82% |    -0.07 |       72 | 45.59%     | ok               |
|          45 | -4.27%   | 27.73%             | -17.57% |    -0.07 |       62 | 35.61%     | ok               |
|          50 | -5.32%   | 27.73%             | -14.03% |    -0.12 |       60 | 31.78%     | ok               |

## BCH-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 40.26%   | -28.18%            | -45.51% |     0.57 |       78 | 56.32%     | ok               |
|          20 | 16.33%   | -28.18%            | -45.63% |     0.38 |       70 | 53.07%     | ok               |
|          30 | 3.16%    | -28.18%            | -53.87% |     0.25 |       78 | 47.70%     | ok               |
|          25 | -0.12%   | -28.18%            | -51.09% |     0.22 |       74 | 49.43%     | ok               |
|          35 | -3.19%   | -28.18%            | -57.75% |     0.17 |       70 | 43.68%     | ok               |

## BITO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -5.64%   | -60.19%            | -31.98% |     0.05 |       54 | 24.29%     | ok               |
|          45 | -18.64%  | -60.19%            | -32.05% |    -0.15 |       60 | 27.79%     | ok               |
|          30 | -24.94%  | -60.19%            | -43.10% |    -0.18 |       81 | 40.93%     | ok               |
|          40 | -25.75%  | -60.19%            | -40.13% |    -0.25 |       64 | 32.28%     | ok               |
|          35 | -27.71%  | -60.19%            | -42.34% |    -0.25 |       72 | 36.44%     | ok               |

## BLK Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | -2.97%   | 47.31%             | -20.79% |    -0.02 |       86 | 42.26%     | ok               |
|          40 | -4.40%   | 47.31%             | -22.83% |    -0.07 |       74 | 37.60%     | ok               |
|          20 | -6.30%   | 47.31%             | -21.48% |    -0.09 |       84 | 51.25%     | ok               |
|          25 | -9.14%   | 47.31%             | -24.62% |    -0.18 |       77 | 48.75%     | ok               |
|          30 | -11.50%  | 47.31%             | -26.90% |    -0.26 |       81 | 46.09%     | ok               |

## BND Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -6.52%   | -0.39%             | -10.72% |    -0.93 |       61 | 39.77%     | ok               |
|          30 | -6.07%   | -0.39%             | -10.80% |    -0.93 |       64 | 34.78%     | ok               |
|          25 | -6.44%   | -0.39%             | -11.16% |    -0.94 |       66 | 37.94%     | ok               |
|          40 | -6.59%   | -0.39%             | -11.34% |    -1.1  |       60 | 29.45%     | ok               |
|          15 | -7.90%   | -0.39%             | -12.04% |    -1.12 |       73 | 42.10%     | ok               |

## BONK-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 156.03%  | -84.40%            | -35.57% |     1.2  |       42 | 21.46%     | ok               |
|          15 | 88.47%   | -84.40%            | -62.48% |     0.78 |       70 | 60.54%     | ok               |
|          45 | 50.70%   | -84.40%            | -47.53% |     0.64 |       66 | 27.59%     | ok               |
|          20 | 37.39%   | -84.40%            | -61.03% |     0.56 |       67 | 56.70%     | ok               |
|          40 | 29.35%   | -84.40%            | -53.34% |     0.5  |       58 | 36.78%     | ok               |

## BTC-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 43.79%   | -23.67%            | -14.50% |     0.87 |       42 | 33.91%     | ok               |
|          45 | 39.29%   | -23.67%            | -12.20% |     0.83 |       38 | 30.08%     | ok               |
|          35 | 38.21%   | -23.67%            | -21.56% |     0.77 |       62 | 40.04%     | ok               |
|          50 | 17.33%   | -23.67%            | -20.63% |     0.48 |       34 | 25.29%     | ok               |
|          30 | 10.50%   | -23.67%            | -21.75% |     0.31 |       70 | 46.17%     | ok               |

## C Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -11.28%  | 96.61%             | -22.98% |    -0.26 |       66 | 31.11%     | ok               |
|          45 | -21.39%  | 96.61%             | -30.69% |    -0.53 |       78 | 35.61%     | ok               |
|          40 | -26.33%  | 96.61%             | -35.05% |    -0.64 |       74 | 38.10%     | ok               |
|          25 | -32.34%  | 96.61%             | -36.49% |    -0.67 |       69 | 48.92%     | ok               |
|          15 | -36.30%  | 96.61%             | -37.81% |    -0.72 |       74 | 55.91%     | ok               |

## CAT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 21.66%   | 107.98%            | -21.89% |     0.44 |       72 | 61.23%     | ok               |
|          25 | 18.58%   | 107.98%            | -21.79% |     0.41 |       66 | 51.08%     | ok               |
|          45 | 10.98%   | 107.98%            | -23.84% |     0.3  |       54 | 37.60%     | ok               |
|          30 | 10.71%   | 107.98%            | -21.87% |     0.29 |       70 | 48.75%     | ok               |
|          20 | 8.64%    | 107.98%            | -24.78% |     0.26 |       76 | 54.58%     | ok               |

## CL Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 8.57%    | 4.77%              | -13.51% |     0.38 |       42 | 23.13%     | ok               |
|          30 | 5.19%    | 4.77%              | -14.32% |     0.23 |       64 | 39.10%     | ok               |
|          45 | 2.90%    | 4.77%              | -13.13% |     0.16 |       48 | 25.79%     | ok               |
|          35 | 1.00%    | 4.77%              | -15.39% |     0.1  |       64 | 35.27%     | ok               |
|          15 | -2.91%   | 4.77%              | -19.00% |    -0.01 |       64 | 46.92%     | ok               |

## CMCSA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -17.36%  | -39.12%            | -27.57% |    -0.57 |       48 | 16.47%     | ok               |
|          45 | -22.69%  | -39.12%            | -34.36% |    -0.71 |       62 | 21.13%     | ok               |
|          15 | -37.28%  | -39.12%            | -44.16% |    -0.79 |       90 | 57.90%     | ok               |
|          40 | -30.60%  | -39.12%            | -41.83% |    -0.81 |       89 | 28.62%     | ok               |
|          35 | -35.05%  | -39.12%            | -46.34% |    -0.9  |       91 | 38.27%     | ok               |

## COMP-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -7.37%   | -42.85%            | -38.71% |     0.11 |       54 | 25.67%     | ok               |
|          30 | -33.03%  | -42.85%            | -52.27% |    -0.13 |       95 | 50.77%     | ok               |
|          25 | -39.77%  | -42.85%            | -53.20% |    -0.22 |       94 | 58.81%     | ok               |
|          40 | -45.10%  | -42.85%            | -50.40% |    -0.41 |       72 | 39.46%     | ok               |
|          45 | -44.09%  | -42.85%            | -50.83% |    -0.41 |       66 | 34.29%     | ok               |

## COP Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -1.91%   | 25.03%             | -34.61% |     0.05 |       48 | 28.95%     | ok               |
|          35 | -8.46%   | 25.03%             | -44.33% |    -0.06 |       71 | 41.76%     | ok               |
|          30 | -10.73%  | 25.03%             | -43.40% |    -0.1  |       68 | 44.43%     | ok               |
|          45 | -10.18%  | 25.03%             | -39.75% |    -0.13 |       60 | 32.78%     | ok               |
|          40 | -18.56%  | 25.03%             | -47.35% |    -0.32 |       72 | 36.44%     | ok               |

## COST Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 16.97%   | 25.72%             | -24.32% |     0.54 |       62 | 47.09%     | ok               |
|          25 | 13.60%   | 25.72%             | -24.93% |     0.46 |       59 | 44.26%     | ok               |
|          35 | 7.04%    | 25.72%             | -30.16% |     0.29 |       58 | 38.60%     | ok               |
|          30 | 2.51%    | 25.72%             | -31.32% |     0.15 |       60 | 41.10%     | ok               |
|          15 | 1.12%    | 25.72%             | -27.30% |     0.11 |       67 | 50.75%     | ok               |

## CRM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | -10.45%  | 6.76%              | -28.76% |    -0.05 |       64 | 42.43%     | ok               |
|          40 | -13.80%  | 6.76%              | -34.57% |    -0.12 |       70 | 38.27%     | ok               |
|          15 | -22.75%  | 6.76%              | -47.54% |    -0.2  |       92 | 58.07%     | ok               |
|          30 | -22.74%  | 6.76%              | -41.12% |    -0.26 |       67 | 47.25%     | ok               |
|          25 | -24.45%  | 6.76%              | -43.96% |    -0.28 |       70 | 49.42%     | ok               |

## CRV-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 76.89%   | -48.93%            | -37.78% |     0.81 |       64 | 31.80%     | ok               |
|          40 | 61.13%   | -48.93%            | -38.86% |     0.73 |       52 | 27.59%     | ok               |
|          50 | 42.22%   | -48.93%            | -30.73% |     0.62 |       44 | 17.24%     | ok               |
|          45 | 43.20%   | -48.93%            | -42.29% |     0.62 |       52 | 21.26%     | ok               |
|          30 | 42.17%   | -48.93%            | -39.89% |     0.58 |       64 | 36.40%     | ok               |

## CSCO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 29.54%   | 125.57%            | -19.34% |     0.63 |       50 | 38.60%     | ok               |
|          45 | 25.16%   | 125.57%            | -19.34% |     0.55 |       52 | 40.27%     | ok               |
|          25 | 14.22%   | 125.57%            | -23.28% |     0.36 |       61 | 51.25%     | ok               |
|          40 | 9.78%    | 125.57%            | -22.37% |     0.29 |       56 | 43.09%     | ok               |
|          30 | 9.12%    | 125.57%            | -22.29% |     0.27 |       64 | 49.75%     | ok               |

## CVX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -8.23%   | 39.67%             | -27.34% |    -0.16 |       75 | 37.60%     | ok               |
|          25 | -9.46%   | 39.67%             | -24.33% |    -0.16 |       75 | 45.42%     | ok               |
|          45 | -8.63%   | 39.67%             | -28.83% |    -0.18 |       67 | 34.28%     | ok               |
|          50 | -8.52%   | 39.67%             | -30.69% |    -0.22 |       60 | 29.78%     | ok               |
|          35 | -11.22%  | 39.67%             | -28.85% |    -0.23 |       69 | 39.60%     | ok               |

## DASH-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 166.11%  | 134.25%            | -33.55% |     1.03 |       40 | 18.20%     | ok               |
|          40 | 134.11%  | 134.25%            | -33.20% |     0.92 |       44 | 24.52%     | ok               |
|          45 | 101.35%  | 134.25%            | -37.63% |     0.81 |       44 | 20.69%     | ok               |
|          30 | 6.20%    | 134.25%            | -64.43% |     0.42 |       53 | 30.27%     | ok               |
|          25 | 5.19%    | 134.25%            | -64.14% |     0.42 |       63 | 32.57%     | ok               |

## DBC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 0.81%    | 44.26%             | -25.67% |     0.09 |       75 | 41.26%     | ok               |
|          20 | -3.62%   | 44.26%             | -25.31% |    -0.05 |       67 | 39.60%     | ok               |
|          25 | -4.89%   | 44.26%             | -24.84% |    -0.09 |       64 | 37.77%     | ok               |
|          50 | -6.27%   | 44.26%             | -19.49% |    -0.18 |       50 | 25.46%     | ok               |
|          35 | -7.39%   | 44.26%             | -23.19% |    -0.19 |       64 | 34.61%     | ok               |

## DE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 2.13%    | 71.74%             | -17.97% |     0.13 |       56 | 29.62%     | ok               |
|          45 | -1.88%   | 71.74%             | -18.76% |     0.04 |       60 | 33.78%     | ok               |
|          20 | -5.29%   | 71.74%             | -23.99% |    -0.01 |       65 | 48.25%     | ok               |
|          25 | -9.64%   | 71.74%             | -24.17% |    -0.11 |       71 | 46.59%     | ok               |
|          30 | -9.78%   | 71.74%             | -23.86% |    -0.12 |       70 | 43.93%     | ok               |

## DIA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -2.25%   | 36.22%             | -11.28% |    -0.08 |       58 | 44.43%     | ok               |
|          35 | -4.03%   | 36.22%             | -13.15% |    -0.2  |       66 | 40.10%     | ok               |
|          30 | -4.46%   | 36.22%             | -12.94% |    -0.21 |       64 | 43.26%     | ok               |
|          20 | -4.94%   | 36.22%             | -13.60% |    -0.22 |       62 | 46.59%     | ok               |
|          40 | -7.23%   | 36.22%             | -15.06% |    -0.41 |       70 | 36.77%     | ok               |

## DIS Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 38.87%   | 8.87%              | -10.17% |     1.17 |       46 | 26.46%     | ok               |
|          40 | 12.25%   | 8.87%              | -18.75% |     0.37 |       59 | 34.78%     | ok               |
|          45 | 7.52%    | 8.87%              | -16.54% |     0.27 |       47 | 30.12%     | ok               |
|          35 | -0.39%   | 8.87%              | -25.70% |     0.08 |       73 | 40.77%     | ok               |
|          15 | -3.49%   | 8.87%              | -32.73% |     0.03 |       83 | 55.24%     | ok               |

## DOGE-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 14.71%   | -64.96%            | -56.09% |     0.39 |       73 | 64.37%     | ok               |
|          20 | 15.08%   | -64.96%            | -53.94% |     0.39 |       73 | 59.20%     | ok               |
|          25 | 6.83%    | -64.96%            | -51.74% |     0.31 |       65 | 55.36%     | ok               |
|          30 | -16.74%  | -64.96%            | -60.95% |     0.04 |       67 | 49.04%     | ok               |
|          50 | -19.61%  | -64.96%            | -54.09% |    -0.08 |       60 | 23.18%     | ok               |

## DOT-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -48.00%  | -74.95%            | -72.06% |    -0.25 |       72 | 61.88%     | ok               |
|          20 | -46.69%  | -74.95%            | -66.32% |    -0.29 |       84 | 58.05%     | ok               |
|          30 | -48.42%  | -74.95%            | -63.33% |    -0.37 |       84 | 47.70%     | ok               |
|          25 | -54.91%  | -74.95%            | -69.99% |    -0.46 |       75 | 53.07%     | ok               |
|          35 | -52.69%  | -74.95%            | -62.35% |    -0.48 |       80 | 42.34%     | ok               |

## DXY-INDEX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -1.43%   | -5.90%             | -6.29%  |    -0.21 |       40 | 32.47%     | ok               |
|          40 | -4.49%   | -5.90%             | -8.24%  |    -0.59 |       64 | 47.84%     | ok               |
|          45 | -4.50%   | -5.90%             | -9.07%  |    -0.64 |       60 | 38.53%     | ok               |
|          15 | -8.10%   | -5.90%             | -11.61% |    -0.81 |       91 | 73.16%     | ok               |
|          30 | -6.75%   | -5.90%             | -10.26% |    -0.82 |       72 | 58.01%     | ok               |

## EEM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | -6.11%   | 47.69%             | -22.40% |    -0.14 |       68 | 37.60%     | ok               |
|          25 | -6.52%   | 47.69%             | -23.98% |    -0.15 |       66 | 41.10%     | ok               |
|          50 | -5.68%   | 47.69%             | -15.42% |    -0.15 |       54 | 31.78%     | ok               |
|          45 | -6.40%   | 47.69%             | -16.91% |    -0.18 |       54 | 33.44%     | ok               |
|          40 | -6.74%   | 47.69%             | -19.08% |    -0.18 |       66 | 35.61%     | ok               |

## EFA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -6.16%   | 27.06%             | -11.85% |    -0.17 |       64 | 50.25%     | ok               |
|          20 | -12.90%  | 27.06%             | -15.38% |    -0.48 |       69 | 47.42%     | ok               |
|          50 | -10.48%  | 27.06%             | -17.60% |    -0.49 |       56 | 31.78%     | ok               |
|          45 | -11.40%  | 27.06%             | -16.92% |    -0.52 |       54 | 33.61%     | ok               |
|          25 | -13.99%  | 27.06%             | -17.04% |    -0.56 |       70 | 43.59%     | ok               |

## EOG Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -15.11%  | 26.82%             | -35.34% |    -0.29 |       56 | 31.78%     | ok               |
|          40 | -18.49%  | 26.82%             | -37.39% |    -0.38 |       68 | 35.11%     | ok               |
|          50 | -19.79%  | 26.82%             | -35.63% |    -0.45 |       52 | 28.95%     | ok               |
|          35 | -22.77%  | 26.82%             | -39.96% |    -0.48 |       81 | 40.10%     | ok               |
|          30 | -25.50%  | 26.82%             | -47.87% |    -0.51 |       78 | 45.26%     | ok               |

## ETC-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -4.94%   | -57.55%            | -31.28% |     0.05 |       28 | 18.20%     | ok               |
|          45 | -7.19%   | -57.55%            | -38.47% |     0.02 |       30 | 21.07%     | ok               |
|          30 | -19.67%  | -57.55%            | -47.84% |    -0.15 |       58 | 32.76%     | ok               |
|          35 | -18.76%  | -57.55%            | -46.64% |    -0.15 |       46 | 28.74%     | ok               |
|          40 | -19.83%  | -57.55%            | -43.28% |    -0.2  |       42 | 24.52%     | ok               |

## ETH-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 143.96%  | -5.02%             | -30.11% |     1.31 |       58 | 46.55%     | ok               |
|          30 | 105.80%  | -5.02%             | -32.89% |     1.06 |       60 | 54.21%     | ok               |
|          40 | 64.33%   | -5.02%             | -33.11% |     0.85 |       62 | 38.89%     | ok               |
|          25 | 68.47%   | -5.02%             | -40.90% |     0.81 |       60 | 58.05%     | ok               |
|          20 | 49.34%   | -5.02%             | -39.10% |     0.66 |       84 | 62.64%     | ok               |

## EWJ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -24.44%  | 37.16%             | -30.73% |    -0.87 |       62 | 36.27%     | ok               |
|          20 | -25.38%  | 37.16%             | -31.32% |    -0.88 |       56 | 38.27%     | ok               |
|          25 | -27.22%  | 37.16%             | -31.18% |    -0.97 |       56 | 37.44%     | ok               |
|          15 | -29.07%  | 37.16%             | -32.55% |    -0.97 |       68 | 41.43%     | ok               |
|          35 | -27.48%  | 37.16%             | -32.54% |    -1.01 |       66 | 34.78%     | ok               |

## FCX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -3.06%   | 22.49%             | -31.93% |     0.09 |       52 | 32.11%     | ok               |
|          50 | -6.23%   | 22.49%             | -26.57% |     0.03 |       54 | 28.29%     | ok               |
|          40 | -15.48%  | 22.49%             | -42.89% |    -0.11 |       64 | 36.61%     | ok               |
|          30 | -33.67%  | 22.49%             | -46.84% |    -0.41 |       67 | 43.93%     | ok               |
|          35 | -33.51%  | 22.49%             | -50.12% |    -0.43 |       69 | 41.76%     | ok               |

## FET-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -30.17%  | -75.10%            | -59.58% |     0.02 |       78 | 56.51%     | ok               |
|          20 | -32.97%  | -75.10%            | -65.01% |    -0.03 |       86 | 52.49%     | ok               |
|          25 | -31.51%  | -75.10%            | -65.31% |    -0.03 |       83 | 47.32%     | ok               |
|          30 | -47.69%  | -75.10%            | -65.38% |    -0.31 |       81 | 42.72%     | ok               |
|          50 | -39.06%  | -75.10%            | -45.19% |    -0.53 |       46 | 14.37%     | ok               |

## FIL-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -40.15%  | -65.51%            | -58.54% |    -0.34 |       65 | 37.16%     | ok               |
|          35 | -41.96%  | -65.51%            | -61.90% |    -0.42 |       58 | 31.23%     | ok               |
|          40 | -40.23%  | -65.51%            | -57.60% |    -0.44 |       48 | 26.82%     | ok               |
|          15 | -58.37%  | -65.51%            | -71.82% |    -0.57 |       91 | 49.04%     | ok               |
|          25 | -58.52%  | -65.51%            | -70.65% |    -0.66 |       76 | 40.04%     | ok               |

## FXI Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -0.86%   | 21.86%             | -22.57% |     0.06 |       48 | 31.45%     | ok               |
|          15 | -3.34%   | 21.86%             | -21.68% |     0.01 |       55 | 35.77%     | ok               |
|          30 | -3.03%   | 21.86%             | -23.91% |     0.01 |       46 | 30.12%     | ok               |
|          20 | -4.64%   | 21.86%             | -24.53% |    -0.03 |       50 | 33.28%     | ok               |
|          35 | -6.68%   | 21.86%             | -27.53% |    -0.09 |       48 | 27.79%     | ok               |

## GDX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 4.80%    | 131.42%            | -31.35% |     0.21 |       78 | 49.75%     | ok               |
|          40 | 0.49%    | 131.42%            | -28.04% |     0.13 |       62 | 37.44%     | ok               |
|          30 | -0.42%   | 131.42%            | -33.31% |     0.13 |       64 | 43.76%     | ok               |
|          35 | -5.32%   | 131.42%            | -32.60% |     0.04 |       70 | 40.10%     | ok               |
|          25 | -8.56%   | 131.42%            | -38.90% |     0    |       68 | 45.42%     | ok               |

## GDXJ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -17.38%  | 124.24%            | -40.04% |    -0.07 |       74 | 50.25%     | ok               |
|          35 | -28.62%  | 124.24%            | -37.15% |    -0.32 |       72 | 40.43%     | ok               |
|          50 | -26.01%  | 124.24%            | -46.83% |    -0.34 |       60 | 33.61%     | ok               |
|          30 | -30.60%  | 124.24%            | -39.24% |    -0.34 |       72 | 43.09%     | ok               |
|          25 | -34.81%  | 124.24%            | -41.80% |    -0.39 |       77 | 46.26%     | ok               |

## GE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 4.89%    | 77.75%             | -21.25% |     0.2  |       60 | 33.78%     | ok               |
|          45 | -2.34%   | 77.75%             | -21.88% |     0.05 |       70 | 36.44%     | ok               |
|          30 | -8.43%   | 77.75%             | -27.82% |    -0.04 |       76 | 48.09%     | ok               |
|          25 | -8.86%   | 77.75%             | -29.91% |    -0.05 |       72 | 49.92%     | ok               |
|          20 | -9.37%   | 77.75%             | -25.05% |    -0.05 |       72 | 52.58%     | ok               |

## GLD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | 22.19%   | 71.39%             | -13.87% |     0.56 |       48 | 47.09%     | ok               |
|          20 | 20.53%   | 71.39%             | -13.87% |     0.53 |       49 | 48.75%     | ok               |
|          30 | 12.75%   | 71.39%             | -13.87% |     0.38 |       50 | 45.59%     | ok               |
|          35 | 10.01%   | 71.39%             | -15.09% |     0.32 |       50 | 42.93%     | ok               |
|          15 | 10.18%   | 71.39%             | -18.05% |     0.31 |       55 | 52.25%     | ok               |

## GOOGL Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 64.65%   | 87.95%             | -17.38% |     1.13 |       55 | 42.76%     | ok               |
|          30 | 60.67%   | 87.95%             | -17.15% |     1.05 |       53 | 46.26%     | ok               |
|          45 | 52.94%   | 87.95%             | -11.66% |     1.05 |       48 | 36.27%     | ok               |
|          25 | 58.22%   | 87.95%             | -16.48% |     1.01 |       53 | 48.75%     | ok               |
|          50 | 46.39%   | 87.95%             | -11.52% |     0.98 |       44 | 31.45%     | ok               |

## GRT-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 59.40%   | -78.11%            | -37.08% |     0.68 |       69 | 62.26%     | ok               |
|          30 | 54.07%   | -78.11%            | -35.21% |     0.67 |       83 | 46.17%     | ok               |
|          45 | 40.60%   | -78.11%            | -41.72% |     0.6  |       46 | 27.78%     | ok               |
|          20 | 39.72%   | -78.11%            | -37.17% |     0.56 |       78 | 55.94%     | ok               |
|          25 | 38.69%   | -78.11%            | -37.25% |     0.56 |       80 | 52.30%     | ok               |

## GS Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 21.49%   | 95.24%             | -20.56% |     0.48 |       68 | 56.24%     | ok               |
|          40 | 6.03%    | 95.24%             | -16.16% |     0.22 |       68 | 41.43%     | ok               |
|          20 | 4.32%    | 95.24%             | -23.19% |     0.19 |       66 | 53.08%     | ok               |
|          25 | -0.96%   | 95.24%             | -23.32% |     0.08 |       66 | 50.58%     | ok               |
|          35 | -2.28%   | 95.24%             | -19.95% |     0.05 |       68 | 45.26%     | ok               |

## HBAR-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -21.11%  | -21.42%            | -39.26% |    -0.33 |       22 | 18.01%     | ok               |
|          45 | -32.30%  | -21.42%            | -49.09% |    -0.63 |       24 | 24.63%     | ok               |
|          40 | -34.29%  | -21.42%            | -51.16% |    -0.67 |       30 | 30.51%     | ok               |
|          30 | -40.46%  | -21.42%            | -56.47% |    -0.82 |       40 | 39.71%     | ok               |
|          35 | -39.84%  | -21.42%            | -56.01% |    -0.82 |       30 | 35.29%     | ok               |

## HD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 0.85%    | -2.13%             | -17.15% |     0.1  |       69 | 43.43%     | ok               |
|          35 | -0.02%   | -2.13%             | -18.52% |     0.08 |       72 | 39.43%     | ok               |
|          40 | -0.53%   | -2.13%             | -18.05% |     0.05 |       74 | 34.78%     | ok               |
|          45 | -1.31%   | -2.13%             | -18.71% |     0.03 |       50 | 29.95%     | ok               |
|          25 | -2.59%   | -2.13%             | -18.88% |     0.02 |       70 | 45.92%     | ok               |

## HON Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -9.91%   | 9.23%              | -20.54% |    -0.24 |       66 | 32.28%     | ok               |
|          45 | -13.83%  | 9.23%              | -22.88% |    -0.35 |       70 | 37.77%     | ok               |
|          35 | -24.95%  | 9.23%              | -31.85% |    -0.64 |       91 | 49.58%     | ok               |
|          40 | -24.75%  | 9.23%              | -31.84% |    -0.66 |       78 | 42.26%     | ok               |
|          30 | -26.59%  | 9.23%              | -34.05% |    -0.66 |       91 | 54.58%     | ok               |

## HYG Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -4.83%   | -0.04%             | -7.93%  |    -0.55 |       68 | 33.61%     | ok               |
|          45 | -6.59%   | -0.04%             | -9.07%  |    -0.8  |       68 | 29.95%     | ok               |
|          20 | -7.54%   | -0.04%             | -11.56% |    -0.81 |       92 | 44.76%     | ok               |
|          25 | -7.56%   | -0.04%             | -11.22% |    -0.82 |       89 | 42.43%     | ok               |
|          35 | -7.10%   | -0.04%             | -9.76%  |    -0.82 |       79 | 35.61%     | ok               |

## IBIT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 52.34%   | 21.18%             | -17.37% |     0.93 |       26 | 25.25%     | ok               |
|          15 | 64.32%   | 21.18%             | -19.20% |     0.93 |       44 | 42.69%     | ok               |
|          45 | 42.96%   | 21.18%             | -17.37% |     0.79 |       30 | 26.45%     | ok               |
|          30 | 34.57%   | 21.18%             | -18.95% |     0.64 |       42 | 35.07%     | ok               |
|          40 | 28.89%   | 21.18%             | -21.25% |     0.6  |       34 | 28.66%     | ok               |

## IBM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -11.50%  | 51.10%             | -49.43% |    -0.01 |       83 | 60.57%     | ok               |
|          35 | -17.80%  | 51.10%             | -47.10% |    -0.16 |       65 | 45.76%     | ok               |
|          30 | -18.28%  | 51.10%             | -48.94% |    -0.16 |       69 | 49.08%     | ok               |
|          20 | -24.19%  | 51.10%             | -53.45% |    -0.25 |       69 | 53.58%     | ok               |
|          25 | -29.38%  | 51.10%             | -55.45% |    -0.36 |       66 | 51.25%     | ok               |

## ICP-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -11.08%  | -47.80%            | -42.43% |     0.16 |       75 | 39.27%     | ok               |
|          35 | -19.50%  | -47.80%            | -51.30% |    -0.01 |       72 | 33.91%     | ok               |
|          40 | -20.07%  | -47.80%            | -45.75% |    -0.04 |       64 | 29.12%     | ok               |
|          15 | -39.47%  | -47.80%            | -59.36% |    -0.07 |       76 | 49.43%     | ok               |
|          20 | -41.22%  | -47.80%            | -62.23% |    -0.11 |       85 | 46.74%     | ok               |

## IEF Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -4.80%   | -1.72%             | -10.18% |    -0.57 |       68 | 41.43%     | ok               |
|          15 | -6.04%   | -1.72%             | -10.91% |    -0.7  |       67 | 43.09%     | ok               |
|          25 | -8.44%   | -1.72%             | -11.95% |    -1.07 |       72 | 38.77%     | ok               |
|          40 | -7.91%   | -1.72%             | -10.75% |    -1.14 |       64 | 26.96%     | ok               |
|          45 | -8.10%   | -1.72%             | -10.86% |    -1.2  |       62 | 25.12%     | ok               |

## IEMG Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -3.36%   | 43.45%             | -23.73% |    -0.05 |       61 | 41.76%     | ok               |
|          50 | -3.73%   | 43.45%             | -15.79% |    -0.09 |       56 | 29.95%     | ok               |
|          35 | -4.88%   | 43.45%             | -23.13% |    -0.11 |       67 | 38.10%     | ok               |
|          45 | -4.51%   | 43.45%             | -16.77% |    -0.12 |       52 | 32.45%     | ok               |
|          30 | -6.47%   | 43.45%             | -24.73% |    -0.16 |       60 | 39.43%     | ok               |

## INJ-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 6.03%    | -32.17%            | -51.11% |     0.31 |       60 | 37.16%     | ok               |
|          40 | 6.66%    | -32.17%            | -44.20% |     0.3  |       50 | 33.91%     | ok               |
|          45 | -2.08%   | -32.17%            | -42.01% |     0.2  |       54 | 28.35%     | ok               |
|          30 | -27.85%  | -32.17%            | -68.17% |    -0.03 |       63 | 40.23%     | ok               |
|          15 | -33.93%  | -32.17%            | -73.53% |    -0.06 |       75 | 49.81%     | ok               |

## INTC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 70.01%   | 177.12%            | -49.32% |     0.71 |       56 | 33.78%     | ok               |
|          50 | 64.73%   | 177.12%            | -48.35% |     0.68 |       60 | 29.95%     | ok               |
|          15 | 60.38%   | 177.12%            | -53.65% |     0.63 |       74 | 58.57%     | ok               |
|          20 | 54.47%   | 177.12%            | -52.47% |     0.6  |       76 | 54.74%     | ok               |
|          40 | 51.36%   | 177.12%            | -55.86% |     0.59 |       64 | 37.94%     | ok               |

## INTU Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 20.28%   | -38.43%            | -34.35% |     0.45 |       63 | 28.29%     | ok               |
|          25 | 12.60%   | -38.43%            | -35.05% |     0.32 |       70 | 49.92%     | ok               |
|          35 | 11.00%   | -38.43%            | -42.78% |     0.3  |       71 | 40.93%     | ok               |
|          45 | 7.82%    | -38.43%            | -37.13% |     0.25 |       63 | 32.61%     | ok               |
|          15 | 7.17%    | -38.43%            | -40.67% |     0.24 |       83 | 55.74%     | ok               |

## ITA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 1.27%    | 50.33%             | -21.48% |     0.11 |       74 | 36.11%     | ok               |
|          30 | 0.37%    | 50.33%             | -23.75% |     0.09 |       78 | 48.42%     | ok               |
|          15 | -1.63%   | 50.33%             | -28.17% |     0.05 |       82 | 61.06%     | ok               |
|          40 | -4.62%   | 50.33%             | -20.54% |    -0.07 |       76 | 41.26%     | ok               |
|          35 | -5.32%   | 50.33%             | -23.12% |    -0.09 |       78 | 44.93%     | ok               |

## IWM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | 13.91%   | 34.46%             | -8.60%  |     0.54 |       52 | 35.27%     | ok               |
|          20 | 12.41%   | 34.46%             | -9.67%  |     0.48 |       58 | 36.27%     | ok               |
|          40 | 8.61%    | 34.46%             | -10.28% |     0.39 |       48 | 29.78%     | ok               |
|          35 | 8.15%    | 34.46%             | -10.26% |     0.36 |       52 | 32.28%     | ok               |
|          15 | 8.96%    | 34.46%             | -10.11% |     0.35 |       76 | 42.10%     | ok               |

## JNJ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 20.07%   | 82.46%             | -10.57% |     0.81 |       38 | 34.61%     | ok               |
|          15 | 16.88%   | 82.46%             | -17.37% |     0.59 |       56 | 52.58%     | ok               |
|          30 | 11.84%   | 82.46%             | -16.86% |     0.47 |       58 | 46.09%     | ok               |
|          20 | 11.48%   | 82.46%             | -16.96% |     0.45 |       62 | 49.08%     | ok               |
|          45 | 9.79%    | 82.46%             | -13.35% |     0.43 |       44 | 38.27%     | ok               |

## JPM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 1.03%    | 66.09%             | -15.90% |     0.1  |       52 | 31.95%     | ok               |
|          45 | -9.38%   | 66.09%             | -21.91% |    -0.25 |       56 | 34.61%     | ok               |
|          20 | -23.46%  | 66.09%             | -35.58% |    -0.53 |       88 | 48.75%     | ok               |
|          35 | -21.30%  | 66.09%             | -27.43% |    -0.63 |       76 | 40.60%     | ok               |
|          40 | -21.82%  | 66.09%             | -28.47% |    -0.66 |       68 | 37.27%     | ok               |

## KO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 29.61%   | 51.50%             | -8.64%  |     1    |       54 | 37.44%     | ok               |
|          35 | 25.20%   | 51.50%             | -8.21%  |     0.88 |       58 | 35.94%     | ok               |
|          40 | 22.19%   | 51.50%             | -9.28%  |     0.84 |       60 | 32.61%     | ok               |
|          25 | 23.30%   | 51.50%             | -10.16% |     0.81 |       60 | 40.10%     | ok               |
|          50 | 7.54%    | 51.50%             | -15.35% |     0.36 |       44 | 26.46%     | ok               |

## LDO-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 107.50%  | -55.39%            | -39.01% |     0.88 |       76 | 58.81%     | ok               |
|          20 | 72.19%   | -55.39%            | -41.22% |     0.73 |       77 | 54.21%     | ok               |
|          30 | 39.37%   | -55.39%            | -50.81% |     0.56 |       68 | 46.93%     | ok               |
|          25 | 26.66%   | -55.39%            | -47.69% |     0.48 |       76 | 51.53%     | ok               |
|          35 | 16.36%   | -55.39%            | -58.48% |     0.39 |       78 | 39.85%     | ok               |

## LIN Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -3.45%   | 17.18%             | -23.00% |    -0.05 |       64 | 44.93%     | ok               |
|          25 | -3.38%   | 17.18%             | -22.01% |    -0.05 |       71 | 41.93%     | ok               |
|          15 | -5.31%   | 17.18%             | -23.68% |    -0.11 |       70 | 47.92%     | ok               |
|          30 | -6.60%   | 17.18%             | -20.61% |    -0.18 |       72 | 39.10%     | ok               |
|          45 | -6.93%   | 17.18%             | -17.04% |    -0.24 |       46 | 22.46%     | ok               |

## LINK-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 56.97%   | -22.80%            | -33.64% |     0.71 |       64 | 44.44%     | ok               |
|          45 | 32.86%   | -22.80%            | -33.71% |     0.54 |       50 | 31.03%     | ok               |
|          35 | 31.35%   | -22.80%            | -34.21% |     0.52 |       58 | 40.42%     | ok               |
|          40 | 22.85%   | -22.80%            | -34.00% |     0.44 |       54 | 34.87%     | ok               |
|          25 | 9.41%    | -22.80%            | -46.32% |     0.33 |       60 | 47.89%     | ok               |

## LLY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 3.20%    | 59.29%             | -38.23% |     0.17 |       50 | 35.44%     | ok               |
|          15 | -11.37%  | 59.29%             | -48.12% |    -0.04 |       70 | 60.23%     | ok               |
|          45 | -10.77%  | 59.29%             | -42.99% |    -0.09 |       60 | 39.27%     | ok               |
|          40 | -22.11%  | 59.29%             | -46.54% |    -0.31 |       70 | 42.26%     | ok               |
|          20 | -25.52%  | 59.29%             | -52.31% |    -0.32 |       77 | 55.24%     | ok               |

## LRCX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -8.83%   | 146.83%            | -48.71% |     0.06 |       76 | 34.61%     | ok               |
|          15 | -17.67%  | 146.83%            | -56.69% |     0.02 |       82 | 51.91%     | ok               |
|          40 | -15.44%  | 146.83%            | -55.33% |    -0.01 |       72 | 40.60%     | ok               |
|          35 | -17.06%  | 146.83%            | -58.47% |    -0.03 |       80 | 42.76%     | ok               |
|          20 | -24.79%  | 146.83%            | -62.91% |    -0.09 |       87 | 47.75%     | ok               |

## LTC-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 20.56%   | -37.21%            | -34.94% |     0.43 |       62 | 44.06%     | ok               |
|          45 | 14.29%   | -37.21%            | -37.29% |     0.36 |       56 | 34.48%     | ok               |
|          30 | 7.29%    | -37.21%            | -30.78% |     0.28 |       66 | 51.34%     | ok               |
|          25 | 3.44%    | -37.21%            | -34.22% |     0.24 |       68 | 53.64%     | ok               |
|          50 | -0.03%   | -37.21%            | -36.12% |     0.16 |       56 | 25.67%     | ok               |

## MCD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 10.95%   | -2.42%             | -9.22%  |     0.51 |       46 | 24.96%     | ok               |
|          40 | 2.04%    | -2.42%             | -18.49% |     0.13 |       69 | 32.95%     | ok               |
|          35 | 1.97%    | -2.42%             | -16.97% |     0.13 |       67 | 37.60%     | ok               |
|          45 | 1.88%    | -2.42%             | -16.79% |     0.13 |       56 | 29.12%     | ok               |
|          30 | -2.68%   | -2.42%             | -22.20% |    -0.05 |       77 | 40.43%     | ok               |

## META Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -7.59%   | 38.99%             | -37.54% |    -0.02 |       66 | 39.43%     | ok               |
|          40 | -13.66%  | 38.99%             | -40.90% |    -0.12 |       68 | 42.43%     | ok               |
|          50 | -17.88%  | 38.99%             | -39.33% |    -0.24 |       68 | 35.27%     | ok               |
|          30 | -26.70%  | 38.99%             | -44.90% |    -0.36 |       72 | 50.08%     | ok               |
|          35 | -27.38%  | 38.99%             | -41.40% |    -0.4  |       81 | 47.59%     | ok               |

## MPC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 26.29%   | 160.05%            | -19.02% |     0.54 |       54 | 41.26%     | ok               |
|          40 | 24.21%   | 160.05%            | -20.88% |     0.5  |       64 | 47.92%     | ok               |
|          45 | 22.03%   | 160.05%            | -20.23% |     0.48 |       60 | 45.26%     | ok               |
|          35 | 22.59%   | 160.05%            | -31.08% |     0.47 |       70 | 50.42%     | ok               |
|          30 | 15.67%   | 160.05%            | -34.29% |     0.37 |       72 | 52.91%     | ok               |

## MRK Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -13.09%  | 17.29%             | -28.39% |    -0.16 |       83 | 51.91%     | ok               |
|          25 | -13.85%  | 17.29%             | -31.07% |    -0.2  |       70 | 44.09%     | ok               |
|          20 | -18.07%  | 17.29%             | -29.34% |    -0.29 |       75 | 47.42%     | ok               |
|          50 | -14.54%  | 17.29%             | -23.01% |    -0.3  |       56 | 28.45%     | ok               |
|          45 | -16.67%  | 17.29%             | -25.38% |    -0.33 |       57 | 31.78%     | ok               |

## MS Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 1.49%    | 88.03%             | -22.02% |     0.13 |       76 | 58.07%     | ok               |
|          40 | -0.10%   | 88.03%             | -19.99% |     0.08 |       72 | 39.27%     | ok               |
|          20 | -0.92%   | 88.03%             | -25.68% |     0.07 |       77 | 52.91%     | ok               |
|          30 | -6.95%   | 88.03%             | -27.79% |    -0.08 |       75 | 48.09%     | ok               |
|          25 | -7.50%   | 88.03%             | -28.36% |    -0.09 |       75 | 50.25%     | ok               |

## MSFT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -13.13%  | 25.52%             | -25.26% |    -0.28 |       72 | 37.77%     | ok               |
|          50 | -18.27%  | 25.52%             | -26.14% |    -0.46 |       64 | 32.11%     | ok               |
|          35 | -21.94%  | 25.52%             | -35.38% |    -0.47 |       73 | 46.76%     | ok               |
|          40 | -21.95%  | 25.52%             | -34.77% |    -0.49 |       71 | 41.43%     | ok               |
|          30 | -25.29%  | 25.52%             | -39.15% |    -0.54 |       81 | 51.58%     | ok               |

## MU Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 202.13%  | 585.19%            | -61.96% |     1.12 |       53 | 59.23%     | ok               |
|          40 | 169.88%  | 585.19%            | -64.30% |     1.11 |       58 | 47.25%     | ok               |
|          30 | 145.07%  | 585.19%            | -68.76% |     1.02 |       51 | 51.58%     | ok               |
|          25 | 143.63%  | 585.19%            | -67.90% |     1    |       51 | 53.08%     | ok               |
|          35 | 136.34%  | 585.19%            | -69.35% |     0.99 |       63 | 49.42%     | ok               |

## NEAR-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 197.57%  | 74.53%             | -36.99% |     1.33 |       28 | 22.03%     | ok               |
|          40 | 174.29%  | 74.53%             | -43.85% |     1.17 |       46 | 31.23%     | ok               |
|          30 | 144.05%  | 74.53%             | -50.77% |     1.02 |       72 | 44.44%     | ok               |
|          45 | 130.19%  | 74.53%             | -38.08% |     1.02 |       48 | 27.20%     | ok               |
|          15 | 147.01%  | 74.53%             | -45.00% |     1    |       77 | 56.13%     | ok               |

## NEM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -4.11%   | 172.08%            | -33.11% |     0.12 |       64 | 58.57%     | ok               |
|          20 | -7.65%   | 172.08%            | -32.74% |     0.06 |       73 | 53.91%     | ok               |
|          50 | -12.51%  | 172.08%            | -33.03% |    -0.06 |       48 | 37.77%     | ok               |
|          25 | -21.75%  | 172.08%            | -39.51% |    -0.17 |       70 | 51.58%     | ok               |
|          30 | -28.27%  | 172.08%            | -41.53% |    -0.29 |       72 | 49.58%     | ok               |

## NFLX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 30.77%   | 4.50%              | -16.28% |     0.78 |       44 | 32.28%     | ok               |
|          40 | 29.67%   | 4.50%              | -15.02% |     0.71 |       50 | 40.27%     | ok               |
|          35 | 25.25%   | 4.50%              | -18.30% |     0.6  |       74 | 44.93%     | ok               |
|          45 | 18.05%   | 4.50%              | -15.48% |     0.49 |       56 | 36.77%     | ok               |
|          15 | 9.11%    | 4.50%              | -26.59% |     0.27 |       74 | 64.89%     | ok               |

## NKE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | -16.21%  | -59.68%            | -42.13% |    -0.15 |       71 | 40.43%     | ok               |
|          20 | -23.52%  | -59.68%            | -49.34% |    -0.22 |       83 | 54.08%     | ok               |
|          25 | -26.69%  | -59.68%            | -51.20% |    -0.28 |       83 | 51.41%     | ok               |
|          15 | -28.45%  | -59.68%            | -54.28% |    -0.3  |       86 | 57.90%     | ok               |
|          40 | -20.78%  | -59.68%            | -31.79% |    -0.35 |       65 | 32.28%     | ok               |

## NOW Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 12.38%   | 19.50%             | -30.43% |     0.31 |       82 | 50.25%     | ok               |
|          20 | 11.23%   | 19.50%             | -39.71% |     0.31 |       77 | 56.74%     | ok               |
|          25 | 7.08%    | 19.50%             | -37.51% |     0.26 |       74 | 53.74%     | ok               |
|          15 | 3.10%    | 19.50%             | -43.06% |     0.22 |       85 | 59.73%     | ok               |
|          40 | 2.48%    | 19.50%             | -36.21% |     0.19 |       72 | 39.43%     | ok               |

## NVDA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -36.17%  | 104.58%            | -43.08% |    -0.55 |       78 | 44.21%     | ok               |
|          20 | -44.65%  | 104.58%            | -38.82% |    -0.63 |       78 | 52.23%     | ok               |
|          25 | -44.56%  | 104.58%            | -43.89% |    -0.69 |       79 | 47.24%     | ok               |
|          35 | -45.77%  | 104.58%            | -51.54% |    -0.82 |       88 | 41.35%     | ok               |
|          15 | -55.13%  | 104.58%            | -52.95% |    -0.86 |       79 | 55.97%     | ok               |

## OP-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 29.42%   | -83.40%            | -30.20% |     0.57 |       34 | 9.39%      | ok               |
|          45 | 19.98%   | -83.40%            | -28.24% |     0.42 |       34 | 13.79%     | ok               |
|          40 | -5.98%   | -83.40%            | -43.36% |     0.11 |       46 | 22.03%     | ok               |
|          15 | -44.50%  | -83.40%            | -56.14% |    -0.28 |       75 | 43.87%     | ok               |
|          35 | -38.27%  | -83.40%            | -56.61% |    -0.36 |       56 | 26.63%     | ok               |

## ORCL Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 181.63%  | 7.13%              | -32.54% |     1.17 |       67 | 60.90%     | ok               |
|          25 | 126.44%  | 7.13%              | -27.76% |     0.98 |       59 | 53.41%     | ok               |
|          45 | 110.51%  | 7.13%              | -32.35% |     0.98 |       56 | 38.94%     | ok               |
|          35 | 115.72%  | 7.13%              | -31.95% |     0.96 |       60 | 47.59%     | ok               |
|          20 | 120.12%  | 7.13%              | -29.32% |     0.95 |       68 | 56.57%     | ok               |

## OXY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 6.18%    | 0.00%              | -28.48% |     0.23 |       67 | 43.09%     | ok               |
|          35 | 3.88%    | 0.00%              | -26.37% |     0.18 |       70 | 39.27%     | ok               |
|          40 | -2.52%   | 0.00%              | -28.30% |     0.06 |       60 | 35.11%     | ok               |
|          50 | -2.61%   | 0.00%              | -27.98% |     0.05 |       46 | 28.45%     | ok               |
|          25 | -10.14%  | 0.00%              | -38.51% |    -0.05 |       77 | 46.42%     | ok               |

## PEP Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 17.82%   | -19.71%            | -11.62% |     0.75 |       36 | 24.79%     | ok               |
|          45 | 7.29%    | -19.71%            | -14.22% |     0.34 |       54 | 29.28%     | ok               |
|          35 | 3.99%    | -19.71%            | -21.42% |     0.19 |       73 | 39.77%     | ok               |
|          30 | 1.75%    | -19.71%            | -21.35% |     0.12 |       72 | 45.26%     | ok               |
|          40 | 1.69%    | -19.71%            | -18.04% |     0.12 |       68 | 35.11%     | ok               |

## PEPE-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -50.17%  | -65.90%            | -61.29% |    -0.34 |       81 | 47.51%     | ok               |
|          15 | -62.54%  | -65.90%            | -64.45% |    -0.4  |       78 | 61.88%     | ok               |
|          20 | -58.88%  | -65.90%            | -63.30% |    -0.41 |       84 | 58.43%     | ok               |
|          25 | -56.58%  | -65.90%            | -64.26% |    -0.44 |       91 | 52.49%     | ok               |
|          35 | -51.85%  | -65.90%            | -61.54% |    -0.46 |       70 | 42.53%     | ok               |

## PFE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -13.17%  | 6.14%              | -23.37% |    -0.4  |       50 | 21.46%     | ok               |
|          40 | -14.79%  | 6.14%              | -27.08% |    -0.44 |       70 | 26.46%     | ok               |
|          50 | -13.66%  | 6.14%              | -25.42% |    -0.47 |       38 | 18.30%     | ok               |
|          35 | -23.00%  | 6.14%              | -32.87% |    -0.7  |       80 | 32.95%     | ok               |
|          30 | -33.11%  | 6.14%              | -41.77% |    -1.03 |       77 | 36.27%     | ok               |

## PG Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -6.14%   | 0.64%              | -20.08% |    -0.19 |       54 | 28.12%     | ok               |
|          35 | -9.34%   | 0.64%              | -18.99% |    -0.31 |       62 | 31.61%     | ok               |
|          45 | -15.31%  | 0.64%              | -22.00% |    -0.62 |       54 | 25.62%     | ok               |
|          30 | -17.58%  | 0.64%              | -24.55% |    -0.63 |       64 | 34.78%     | ok               |
|          25 | -19.46%  | 0.64%              | -25.84% |    -0.7  |       76 | 36.27%     | ok               |

## PM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | -8.46%   | 98.99%             | -35.28% |    -0.11 |       86 | 46.09%     | ok               |
|          20 | -10.85%  | 98.99%             | -36.74% |    -0.15 |       85 | 54.74%     | ok               |
|          30 | -11.33%  | 98.99%             | -38.30% |    -0.17 |       81 | 49.58%     | ok               |
|          50 | -12.31%  | 98.99%             | -36.94% |    -0.25 |       68 | 36.61%     | ok               |
|          40 | -14.51%  | 98.99%             | -39.92% |    -0.29 |       80 | 42.26%     | ok               |

## POL-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 56.48%   | -60.55%            | -39.06% |     0.71 |       79 | 50.77%     | ok               |
|          25 | 35.21%   | -60.55%            | -39.06% |     0.54 |       71 | 55.94%     | ok               |
|          20 | 32.28%   | -60.55%            | -39.57% |     0.52 |       77 | 59.00%     | ok               |
|          15 | 2.90%    | -60.55%            | -44.64% |     0.27 |       80 | 62.64%     | ok               |
|          40 | -0.85%   | -60.55%            | -34.52% |     0.17 |       62 | 31.61%     | ok               |

## QCOM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -12.69%  | -15.30%            | -54.83% |     0.02 |       73 | 44.09%     | ok               |
|          20 | -19.11%  | -15.30%            | -54.71% |    -0.07 |       69 | 47.42%     | ok               |
|          35 | -19.48%  | -15.30%            | -50.58% |    -0.1  |       79 | 39.93%     | ok               |
|          15 | -28.88%  | -15.30%            | -58.24% |    -0.21 |       71 | 50.08%     | ok               |
|          30 | -28.88%  | -15.30%            | -56.59% |    -0.24 |       77 | 42.43%     | ok               |

## QQQ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 23.25%   | 56.30%             | -14.17% |     0.58 |       63 | 53.24%     | ok               |
|          25 | 15.48%   | 56.30%             | -12.88% |     0.46 |       63 | 46.92%     | ok               |
|          20 | 13.86%   | 56.30%             | -12.98% |     0.41 |       69 | 49.75%     | ok               |
|          30 | 8.16%    | 56.30%             | -13.49% |     0.29 |       66 | 44.59%     | ok               |
|          35 | -2.96%   | 56.30%             | -19.93% |    -0.01 |       72 | 40.77%     | ok               |

## RENDER-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 27.03%   | -61.43%            | -44.59% |     0.49 |       82 | 61.69%     | ok               |
|          20 | 24.34%   | -61.43%            | -43.43% |     0.47 |       85 | 58.43%     | ok               |
|          25 | 18.59%   | -61.43%            | -41.13% |     0.43 |       85 | 53.45%     | ok               |
|          30 | -24.47%  | -61.43%            | -45.71% |     0.01 |       90 | 47.13%     | ok               |
|          35 | -34.92%  | -61.43%            | -47.93% |    -0.18 |       86 | 40.61%     | ok               |

## RTX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 35.17%   | 80.60%             | -18.66% |     0.76 |       75 | 57.24%     | ok               |
|          25 | 30.55%   | 80.60%             | -18.59% |     0.68 |       63 | 54.58%     | ok               |
|          30 | 25.60%   | 80.60%             | -16.99% |     0.61 |       68 | 51.75%     | ok               |
|          15 | 27.00%   | 80.60%             | -19.55% |     0.61 |       68 | 61.73%     | ok               |
|          50 | 18.57%   | 80.60%             | -18.42% |     0.57 |       60 | 38.60%     | ok               |

## SBUX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -0.93%   | 27.04%             | -23.55% |     0.08 |       57 | 40.93%     | ok               |
|          40 | -2.00%   | 27.04%             | -25.43% |     0.04 |       60 | 32.45%     | ok               |
|          45 | -3.87%   | 27.04%             | -27.26% |    -0.02 |       66 | 27.62%     | ok               |
|          35 | -6.34%   | 27.04%             | -26.54% |    -0.05 |       60 | 35.77%     | ok               |
|          20 | -12.74%  | 27.04%             | -30.94% |    -0.15 |       60 | 42.93%     | ok               |

## SCHW Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -0.62%   | 24.78%             | -29.24% |     0.08 |       75 | 51.75%     | ok               |
|          25 | -0.93%   | 24.78%             | -28.76% |     0.07 |       67 | 49.42%     | ok               |
|          45 | -2.78%   | 24.78%             | -16.53% |    -0.02 |       60 | 30.62%     | ok               |
|          50 | -4.01%   | 24.78%             | -13.28% |    -0.09 |       52 | 27.62%     | ok               |
|          15 | -8.36%   | 24.78%             | -31.37% |    -0.1  |       83 | 56.07%     | ok               |

## SHIB-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | -17.39%  | -65.66%            | -44.56% |    -0.05 |       69 | 47.32%     | ok               |
|          15 | -21.08%  | -65.66%            | -45.04% |    -0.05 |       84 | 67.24%     | ok               |
|          40 | -19.98%  | -65.66%            | -41.14% |    -0.12 |       60 | 39.08%     | ok               |
|          20 | -25.15%  | -65.66%            | -47.68% |    -0.12 |       76 | 62.45%     | ok               |
|          25 | -25.39%  | -65.66%            | -45.06% |    -0.13 |       78 | 59.00%     | ok               |

## SHY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd    |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:-------|---------:|---------:|:-----------|:-----------------|
|          30 | -1.87%   | 0.06%              | -3.30% |    -0.63 |       48 | 36.94%     | ok               |
|          35 | -2.39%   | 0.06%              | -3.61% |    -0.82 |       52 | 35.27%     | ok               |
|          40 | -2.41%   | 0.06%              | -3.58% |    -0.83 |       54 | 33.94%     | ok               |
|          45 | -2.43%   | 0.06%              | -3.43% |    -0.89 |       54 | 28.45%     | ok               |
|          50 | -2.67%   | 0.06%              | -3.40% |    -1.03 |       48 | 24.79%     | ok               |

## SKY-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | -54.40%  | 1.39%              | -59.64% |    -0.86 |       76 | 35.06%     | ok               |
|          30 | -58.48%  | 1.39%              | -62.30% |    -0.92 |       87 | 42.91%     | ok               |
|          15 | -64.93%  | 1.39%              | -65.29% |    -0.97 |       83 | 53.26%     | ok               |
|          25 | -62.82%  | 1.39%              | -65.51% |    -1.01 |       80 | 46.17%     | ok               |
|          40 | -60.39%  | 1.39%              | -62.94% |    -1.1  |       64 | 31.99%     | ok               |

## SLB Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 5.80%    | 7.98%              | -25.36% |     0.22 |       60 | 31.61%     | ok               |
|          40 | 4.07%    | 7.98%              | -28.43% |     0.19 |       50 | 34.94%     | ok               |
|          50 | -7.77%   | 7.98%              | -29.54% |    -0.09 |       52 | 26.29%     | ok               |
|          35 | -26.40%  | 7.98%              | -45.96% |    -0.46 |       74 | 42.60%     | ok               |
|          25 | -38.60%  | 7.98%              | -55.80% |    -0.71 |       85 | 53.24%     | ok               |

## SLV Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 55.21%   | 77.74%             | -31.40% |     0.76 |       54 | 30.12%     | ok               |
|          45 | 42.03%   | 77.74%             | -31.33% |     0.64 |       65 | 31.61%     | ok               |
|          40 | 40.90%   | 77.74%             | -34.28% |     0.63 |       69 | 33.61%     | ok               |
|          20 | 29.36%   | 77.74%             | -41.17% |     0.5  |       72 | 43.93%     | ok               |
|          15 | 29.34%   | 77.74%             | -47.98% |     0.49 |       73 | 48.75%     | ok               |

## SMH Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 64.92%   | 117.63%            | -31.01% |     0.94 |       47 | 45.59%     | ok               |
|          25 | 50.00%   | 117.63%            | -32.94% |     0.8  |       44 | 44.09%     | ok               |
|          35 | 47.67%   | 117.63%            | -34.36% |     0.79 |       56 | 40.93%     | ok               |
|          30 | 45.19%   | 117.63%            | -33.99% |     0.75 |       50 | 42.60%     | ok               |
|          45 | 33.34%   | 117.63%            | -33.68% |     0.65 |       56 | 35.27%     | ok               |

## SNX-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 16.40%   | -73.62%            | -41.29% |     0.39 |       58 | 28.16%     | ok               |
|          20 | 6.92%    | -73.62%            | -53.03% |     0.31 |       71 | 44.06%     | ok               |
|          40 | 10.28%   | -73.62%            | -28.61% |     0.31 |       46 | 22.80%     | ok               |
|          30 | -5.12%   | -73.62%            | -50.74% |     0.16 |       62 | 34.87%     | ok               |
|          15 | -22.73%  | -73.62%            | -54.74% |     0    |       77 | 48.66%     | ok               |

## SOL-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 44.95%   | -38.47%            | -38.17% |     0.65 |       58 | 39.08%     | ok               |
|          35 | 20.79%   | -38.47%            | -43.70% |     0.43 |       70 | 45.59%     | ok               |
|          45 | 15.36%   | -38.47%            | -46.83% |     0.37 |       58 | 33.72%     | ok               |
|          25 | -1.45%   | -38.47%            | -41.09% |     0.21 |       70 | 56.13%     | ok               |
|          50 | 0.21%    | -38.47%            | -46.56% |     0.17 |       58 | 27.97%     | ok               |

## SOXX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | 62.84%   | 103.28%            | -39.65% |     0.89 |       54 | 44.26%     | ok               |
|          35 | 60.04%   | 103.28%            | -38.76% |     0.88 |       56 | 39.60%     | ok               |
|          30 | 58.31%   | 103.28%            | -40.14% |     0.85 |       56 | 42.10%     | ok               |
|          20 | 50.54%   | 103.28%            | -38.67% |     0.75 |       59 | 45.09%     | ok               |
|          40 | 40.46%   | 103.28%            | -41.03% |     0.68 |       58 | 37.44%     | ok               |

## SPY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 11.53%   | 44.86%             | -14.25% |     0.43 |       59 | 52.08%     | ok               |
|          15 | 11.00%   | 44.86%             | -16.80% |     0.41 |       63 | 54.74%     | ok               |
|          25 | 6.52%    | 44.86%             | -14.25% |     0.28 |       59 | 51.08%     | ok               |
|          30 | 1.31%    | 44.86%             | -15.53% |     0.11 |       62 | 48.59%     | ok               |
|          35 | 0.33%    | 44.86%             | -15.58% |     0.07 |       60 | 45.42%     | ok               |

## SUSHI-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 0.80%    | -69.88%            | -34.75% |     0.18 |       52 | 16.67%     | ok               |
|          45 | -38.15%  | -69.88%            | -57.99% |    -0.42 |       56 | 21.65%     | ok               |
|          40 | -41.53%  | -69.88%            | -60.82% |    -0.43 |       59 | 28.74%     | ok               |
|          15 | -65.25%  | -69.88%            | -75.07% |    -0.71 |       86 | 50.00%     | ok               |
|          35 | -60.29%  | -69.88%            | -72.78% |    -0.75 |       80 | 34.48%     | ok               |

## T Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 59.34%   | 24.81%             | -15.08% |     1    |       73 | 65.56%     | ok               |
|          20 | 55.41%   | 24.81%             | -18.13% |     0.98 |       68 | 61.06%     | ok               |
|          25 | 53.64%   | 24.81%             | -17.66% |     0.97 |       68 | 58.90%     | ok               |
|          30 | 43.50%   | 24.81%             | -17.01% |     0.84 |       70 | 56.91%     | ok               |
|          35 | 27.85%   | 24.81%             | -14.49% |     0.62 |       76 | 52.58%     | ok               |

## TGT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -11.06%  | 1.25%              | -34.42% |    -0.16 |       60 | 37.60%     | ok               |
|          45 | -12.30%  | 1.25%              | -26.12% |    -0.24 |       48 | 28.79%     | ok               |
|          20 | -17.93%  | 1.25%              | -39.87% |    -0.27 |       90 | 45.59%     | ok               |
|          25 | -16.48%  | 1.25%              | -38.73% |    -0.28 |       72 | 40.93%     | ok               |
|          35 | -17.42%  | 1.25%              | -32.35% |    -0.35 |       60 | 33.94%     | ok               |

## TIA-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -15.84%  | -79.06%            | -66.82% |     0.21 |       94 | 58.43%     | ok               |
|          25 | -14.21%  | -79.06%            | -69.36% |     0.18 |       90 | 48.28%     | ok               |
|          35 | -9.22%   | -79.06%            | -66.58% |     0.15 |       76 | 36.40%     | ok               |
|          20 | -28.65%  | -79.06%            | -71.57% |     0.06 |       90 | 53.45%     | ok               |
|          30 | -36.08%  | -79.06%            | -74.53% |    -0.07 |       91 | 43.30%     | ok               |

## TLT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -7.35%   | -9.63%             | -12.51% |    -0.8  |       34 | 17.14%     | ok               |
|          40 | -12.97%  | -9.63%             | -17.65% |    -1.14 |       50 | 25.12%     | ok               |
|          45 | -11.50%  | -9.63%             | -15.17% |    -1.19 |       44 | 20.47%     | ok               |
|          30 | -18.82%  | -9.63%             | -22.01% |    -1.42 |       66 | 33.11%     | ok               |
|          35 | -18.49%  | -9.63%             | -21.03% |    -1.54 |       62 | 28.79%     | ok               |

## TMO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 50.78%   | 19.11%             | -8.17%  |     1.07 |       50 | 35.27%     | ok               |
|          45 | 49.72%   | 19.11%             | -9.69%  |     1    |       54 | 40.27%     | ok               |
|          40 | 43.13%   | 19.11%             | -11.15% |     0.88 |       59 | 45.26%     | ok               |
|          35 | 44.66%   | 19.11%             | -13.84% |     0.85 |       69 | 50.92%     | ok               |
|          20 | 40.14%   | 19.11%             | -22.89% |     0.73 |       76 | 62.73%     | ok               |

## TMUS Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -4.80%   | -9.24%             | -33.03% |    -0    |       74 | 48.92%     | ok               |
|          15 | -10.41%  | -9.24%             | -41.04% |    -0.11 |       68 | 61.56%     | ok               |
|          50 | -7.84%   | -9.24%             | -32.38% |    -0.14 |       60 | 34.44%     | ok               |
|          25 | -14.13%  | -9.24%             | -39.29% |    -0.21 |       75 | 51.75%     | ok               |
|          20 | -15.58%  | -9.24%             | -39.79% |    -0.24 |       74 | 55.91%     | ok               |

## TRX-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 11.44%   | 22.19%             | -18.79% |     0.42 |       54 | 38.12%     | ok               |
|          35 | 4.90%    | 22.19%             | -21.77% |     0.22 |       66 | 46.36%     | ok               |
|          20 | 2.44%    | 22.19%             | -25.45% |     0.16 |       61 | 56.13%     | ok               |
|          30 | 2.37%    | 22.19%             | -22.90% |     0.15 |       66 | 49.23%     | ok               |
|          45 | 1.66%    | 22.19%             | -22.76% |     0.13 |       46 | 34.48%     | ok               |

## TSLA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 42.37%   | 110.34%            | -32.60% |     0.61 |       66 | 30.28%     | ok               |
|          40 | 20.23%   | 110.34%            | -45.90% |     0.39 |       67 | 35.44%     | ok               |
|          45 | 2.72%    | 110.34%            | -46.86% |     0.22 |       71 | 32.61%     | ok               |
|          35 | -11.58%  | 110.34%            | -54.51% |     0.07 |       78 | 38.10%     | ok               |
|          30 | -35.00%  | 110.34%            | -59.64% |    -0.22 |       78 | 42.76%     | ok               |

## TXN Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 6.25%    | 43.33%             | -43.95% |     0.22 |       70 | 31.95%     | ok               |
|          35 | -13.72%  | 43.33%             | -42.26% |    -0.09 |       80 | 46.59%     | ok               |
|          40 | -15.22%  | 43.33%             | -44.70% |    -0.12 |       76 | 44.26%     | ok               |
|          20 | -19.86%  | 43.33%             | -37.39% |    -0.14 |       70 | 56.41%     | ok               |
|          45 | -15.86%  | 43.33%             | -45.28% |    -0.14 |       84 | 37.94%     | ok               |

## UNH Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 45.32%   | -14.21%            | -26.31% |     0.68 |       75 | 48.59%     | ok               |
|          50 | 41.52%   | -14.21%            | -36.92% |     0.67 |       54 | 29.12%     | ok               |
|          35 | 40.90%   | -14.21%            | -27.21% |     0.64 |       70 | 43.59%     | ok               |
|          20 | 40.70%   | -14.21%            | -26.96% |     0.62 |       78 | 57.90%     | ok               |
|          15 | 40.65%   | -14.21%            | -26.07% |     0.61 |       83 | 64.06%     | ok               |

## UNI-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 92.10%   | 18.35%             | -25.49% |     0.95 |       50 | 26.44%     | ok               |
|          45 | 75.83%   | 18.35%             | -34.45% |     0.81 |       56 | 33.91%     | ok               |
|          40 | 51.27%   | 18.35%             | -47.29% |     0.65 |       60 | 38.89%     | ok               |
|          35 | 29.05%   | 18.35%             | -54.42% |     0.49 |       68 | 44.25%     | ok               |
|          20 | -29.70%  | 18.35%             | -69.65% |     0.02 |       93 | 59.00%     | ok               |

## UPS Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -28.61%  | -26.93%            | -31.67% |    -0.55 |       60 | 31.45%     | ok               |
|          35 | -30.51%  | -26.93%            | -33.26% |    -0.59 |       66 | 35.77%     | ok               |
|          20 | -34.33%  | -26.93%            | -37.38% |    -0.64 |       86 | 49.75%     | ok               |
|          15 | -36.65%  | -26.93%            | -39.59% |    -0.69 |       88 | 53.58%     | ok               |
|          25 | -36.09%  | -26.93%            | -37.88% |    -0.7  |       76 | 46.26%     | ok               |

## USO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 10.04%   | 117.20%            | -42.51% |     0.28 |       73 | 37.77%     | ok               |
|          15 | 7.46%    | 117.20%            | -40.56% |     0.25 |       68 | 41.10%     | ok               |
|          45 | 4.88%    | 117.20%            | -33.58% |     0.21 |       50 | 26.62%     | ok               |
|          25 | -0.34%   | 117.20%            | -44.87% |     0.14 |       69 | 35.27%     | ok               |
|          50 | -4.23%   | 117.20%            | -29.54% |     0.06 |       54 | 24.46%     | ok               |

## VEA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 5.65%    | 36.55%             | -16.89% |     0.26 |       54 | 49.42%     | ok               |
|          20 | 1.10%    | 36.55%             | -17.40% |     0.1  |       55 | 47.09%     | ok               |
|          25 | -3.88%   | 36.55%             | -18.46% |    -0.11 |       57 | 45.09%     | ok               |
|          30 | -5.21%   | 36.55%             | -18.84% |    -0.17 |       64 | 41.43%     | ok               |
|          35 | -5.86%   | 36.55%             | -17.88% |    -0.2  |       50 | 38.94%     | ok               |

## VIXY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -54.55%  | -61.32%            | -69.78% |    -0.63 |       34 | 8.65%      | ok               |
|          15 | -77.41%  | -61.32%            | -89.47% |    -0.81 |       95 | 42.26%     | ok               |
|          45 | -64.29%  | -61.32%            | -75.03% |    -0.84 |       54 | 13.64%     | ok               |
|          30 | -77.35%  | -61.32%            | -88.17% |    -0.92 |       92 | 31.45%     | ok               |
|          40 | -71.98%  | -61.32%            | -80.72% |    -0.97 |       66 | 17.47%     | ok               |

## VNQ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -7.59%   | 11.30%             | -22.16% |    -0.26 |       67 | 42.43%     | ok               |
|          45 | -9.74%   | 11.30%             | -20.96% |    -0.43 |       60 | 28.45%     | ok               |
|          20 | -12.31%  | 11.30%             | -23.83% |    -0.46 |       72 | 45.09%     | ok               |
|          30 | -12.02%  | 11.30%             | -24.66% |    -0.47 |       71 | 39.77%     | ok               |
|          15 | -13.24%  | 11.30%             | -24.73% |    -0.49 |       67 | 46.42%     | ok               |

## VTI Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 12.69%   | 43.95%             | -13.96% |     0.46 |       62 | 52.58%     | ok               |
|          15 | 8.06%    | 43.95%             | -15.70% |     0.32 |       59 | 54.91%     | ok               |
|          25 | -1.26%   | 43.95%             | -16.10% |     0.02 |       56 | 50.42%     | ok               |
|          30 | -8.66%   | 43.95%             | -18.77% |    -0.27 |       66 | 48.42%     | ok               |
|          40 | -9.76%   | 43.95%             | -20.86% |    -0.34 |       70 | 40.93%     | ok               |

## VWO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -7.44%   | 31.96%             | -21.17% |    -0.27 |       54 | 28.12%     | ok               |
|          15 | -10.93%  | 31.96%             | -24.01% |    -0.34 |       74 | 45.59%     | ok               |
|          45 | -9.19%   | 31.96%             | -23.20% |    -0.34 |       54 | 30.62%     | ok               |
|          40 | -10.23%  | 31.96%             | -23.50% |    -0.38 |       64 | 33.28%     | ok               |
|          20 | -12.30%  | 31.96%             | -26.14% |    -0.4  |       69 | 43.26%     | ok               |

## VZ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -3.10%   | 9.84%              | -12.96% |    -0.04 |       56 | 28.62%     | ok               |
|          20 | -23.78%  | 9.84%              | -35.02% |    -0.48 |       78 | 52.08%     | ok               |
|          35 | -17.92%  | 9.84%              | -26.48% |    -0.52 |       62 | 38.94%     | ok               |
|          25 | -20.67%  | 9.84%              | -26.29% |    -0.54 |       81 | 47.09%     | ok               |
|          45 | -18.61%  | 9.84%              | -26.23% |    -0.57 |       72 | 32.95%     | ok               |

## WFC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | -9.43%   | 38.53%             | -22.54% |    -0.14 |       77 | 43.43%     | ok               |
|          50 | -8.46%   | 38.53%             | -18.29% |    -0.21 |       58 | 32.28%     | ok               |
|          40 | -15.03%  | 38.53%             | -24.88% |    -0.37 |       72 | 40.10%     | ok               |
|          30 | -20.92%  | 38.53%             | -29.78% |    -0.37 |       82 | 46.76%     | ok               |
|          20 | -23.30%  | 38.53%             | -29.87% |    -0.38 |       82 | 52.91%     | ok               |

## WIF-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 16.46%   | -79.43%            | -40.67% |     0.41 |       67 | 45.40%     | ok               |
|          15 | -8.99%   | -79.43%            | -46.21% |     0.21 |       77 | 48.66%     | ok               |
|          25 | -9.20%   | -79.43%            | -44.74% |     0.19 |       65 | 41.57%     | ok               |
|          30 | -28.55%  | -79.43%            | -52.76% |    -0.03 |       66 | 38.89%     | ok               |
|          50 | -13.58%  | -79.43%            | -35.47% |    -0.06 |       38 | 13.98%     | ok               |

## WMT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 37.35%   | 84.18%             | -12.87% |     1.12 |       38 | 36.61%     | ok               |
|          45 | 36.20%   | 84.18%             | -14.82% |     1.04 |       44 | 38.94%     | ok               |
|          35 | 26.26%   | 84.18%             | -18.90% |     0.76 |       60 | 45.26%     | ok               |
|          40 | 24.64%   | 84.18%             | -19.17% |     0.74 |       52 | 40.60%     | ok               |
|          15 | 7.73%    | 84.18%             | -26.82% |     0.26 |       84 | 59.23%     | ok               |

## XBI Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 13.65%   | 70.13%             | -16.08% |     0.41 |       52 | 34.11%     | ok               |
|          45 | 9.33%    | 70.13%             | -15.46% |     0.31 |       50 | 31.61%     | ok               |
|          35 | 3.14%    | 70.13%             | -17.66% |     0.16 |       60 | 36.77%     | ok               |
|          30 | 0.99%    | 70.13%             | -17.66% |     0.11 |       62 | 38.27%     | ok               |
|          50 | 0.10%    | 70.13%             | -15.41% |     0.08 |       50 | 28.62%     | ok               |

## XLB Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -1.32%   | 12.95%             | -16.22% |    -0    |       38 | 21.80%     | ok               |
|          40 | -2.23%   | 12.95%             | -18.60% |    -0.04 |       54 | 26.29%     | ok               |
|          45 | -5.07%   | 12.95%             | -18.61% |    -0.16 |       38 | 23.46%     | ok               |
|          35 | -6.43%   | 12.95%             | -21.91% |    -0.2  |       56 | 29.62%     | ok               |
|          25 | -9.14%   | 12.95%             | -21.80% |    -0.29 |       64 | 36.11%     | ok               |

## XLC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 12.05%   | 29.02%             | -12.33% |     0.46 |       61 | 49.25%     | ok               |
|          25 | 11.50%   | 29.02%             | -12.31% |     0.43 |       60 | 51.41%     | ok               |
|          20 | 10.88%   | 29.02%             | -11.04% |     0.4  |       63 | 53.91%     | ok               |
|          50 | 6.69%    | 29.02%             | -11.12% |     0.35 |       64 | 37.44%     | ok               |
|          40 | 7.26%    | 29.02%             | -13.38% |     0.32 |       62 | 42.93%     | ok               |

## XLE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 1.70%    | 45.00%             | -25.98% |     0.12 |       56 | 37.60%     | ok               |
|          35 | -1.47%   | 45.00%             | -26.89% |     0.05 |       65 | 44.09%     | ok               |
|          45 | -1.65%   | 45.00%             | -28.46% |     0.03 |       60 | 39.77%     | ok               |
|          30 | -3.08%   | 45.00%             | -28.90% |     0.01 |       69 | 46.26%     | ok               |
|          25 | -7.03%   | 45.00%             | -31.79% |    -0.08 |       80 | 49.25%     | ok               |

## XLF Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 2.55%    | 36.05%             | -20.19% |     0.15 |       76 | 54.91%     | ok               |
|          20 | 1.87%    | 36.05%             | -18.63% |     0.13 |       74 | 52.08%     | ok               |
|          25 | -5.23%   | 36.05%             | -23.22% |    -0.13 |       81 | 48.92%     | ok               |
|          30 | -5.85%   | 36.05%             | -23.61% |    -0.15 |       82 | 46.92%     | ok               |
|          35 | -13.18%  | 36.05%             | -24.48% |    -0.49 |       72 | 43.26%     | ok               |

## XLI Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 5.62%    | 34.99%             | -11.06% |     0.25 |       86 | 51.75%     | ok               |
|          20 | 1.42%    | 34.99%             | -12.74% |     0.11 |       75 | 46.42%     | ok               |
|          45 | -4.05%   | 34.99%             | -16.29% |    -0.13 |       68 | 34.11%     | ok               |
|          50 | -5.33%   | 34.99%             | -14.94% |    -0.21 |       62 | 31.61%     | ok               |
|          25 | -7.50%   | 34.99%             | -15.86% |    -0.24 |       76 | 44.26%     | ok               |

## XLK Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 69.22%   | 73.52%             | -14.75% |     1.15 |       47 | 51.08%     | ok               |
|          20 | 65.63%   | 73.52%             | -14.75% |     1.14 |       48 | 48.59%     | ok               |
|          25 | 59.82%   | 73.52%             | -14.75% |     1.1  |       44 | 46.59%     | ok               |
|          30 | 50.25%   | 73.52%             | -14.75% |     1    |       44 | 45.26%     | ok               |
|          35 | 33.49%   | 73.52%             | -14.71% |     0.76 |       56 | 42.60%     | ok               |

## XLM-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | 17.01%   | -38.45%            | -49.14% |     0.39 |       68 | 50.19%     | ok               |
|          40 | 10.72%   | -38.45%            | -47.28% |     0.32 |       50 | 37.36%     | ok               |
|          50 | 9.13%    | -38.45%            | -48.81% |     0.29 |       42 | 25.86%     | ok               |
|          30 | 6.76%    | -38.45%            | -54.58% |     0.29 |       66 | 48.08%     | ok               |
|          45 | 0.99%    | -38.45%            | -51.28% |     0.2  |       56 | 31.42%     | ok               |

## XLP Threshold Sweep

|   threshold | return   | benchmark_return   | mdd    |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:-------|---------:|---------:|:-----------|:-----------------|
|          45 | 19.63%   | 16.36%             | -5.66% |     1.09 |       50 | 30.12%     | ok               |
|          40 | 18.57%   | 16.36%             | -7.32% |     1.01 |       68 | 33.94%     | ok               |
|          35 | 17.54%   | 16.36%             | -8.39% |     0.94 |       64 | 36.94%     | ok               |
|          50 | 15.80%   | 16.36%             | -6.08% |     0.92 |       56 | 28.12%     | ok               |
|          30 | 14.14%   | 16.36%             | -8.96% |     0.75 |       65 | 38.77%     | ok               |

## XLU Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 4.23%    | 17.90%             | -14.03% |     0.25 |       54 | 29.28%     | ok               |
|          45 | 3.09%    | 17.90%             | -14.97% |     0.19 |       58 | 30.45%     | ok               |
|          40 | 0.08%    | 17.90%             | -16.41% |     0.05 |       64 | 32.45%     | ok               |
|          35 | -0.59%   | 17.90%             | -19.71% |     0.02 |       66 | 35.27%     | ok               |
|          30 | -4.89%   | 17.90%             | -20.40% |    -0.17 |       71 | 38.77%     | ok               |

## XLV Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -20.02%  | 26.17%             | -22.40% |    -0.94 |       74 | 37.94%     | ok               |
|          30 | -20.38%  | 26.17%             | -22.75% |    -0.97 |       74 | 36.27%     | ok               |
|          15 | -22.72%  | 26.17%             | -24.70% |    -1.05 |       81 | 41.93%     | ok               |
|          20 | -22.55%  | 26.17%             | -24.54% |    -1.06 |       77 | 39.43%     | ok               |
|          35 | -24.35%  | 26.17%             | -26.58% |    -1.26 |       68 | 33.28%     | ok               |

## XLY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -0.04%   | 30.72%             | -15.77% |     0.08 |       74 | 54.08%     | ok               |
|          30 | -3.52%   | 30.72%             | -18.35% |    -0.04 |       73 | 47.42%     | ok               |
|          20 | -5.33%   | 30.72%             | -19.25% |    -0.08 |       70 | 50.75%     | ok               |
|          25 | -7.45%   | 30.72%             | -19.98% |    -0.15 |       67 | 49.25%     | ok               |
|          50 | -6.20%   | 30.72%             | -15.82% |    -0.21 |       60 | 31.95%     | ok               |

## XOM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | 4.78%    | 52.00%             | -19.90% |     0.2  |       57 | 35.77%     | ok               |
|          30 | 3.74%    | 52.00%             | -20.29% |     0.18 |       57 | 35.11%     | ok               |
|          50 | 2.65%    | 52.00%             | -21.35% |     0.15 |       38 | 27.79%     | ok               |
|          20 | -1.18%   | 52.00%             | -25.56% |     0.05 |       64 | 38.10%     | ok               |
|          45 | -1.23%   | 52.00%             | -23.33% |     0.04 |       44 | 29.12%     | ok               |

## XRP-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 23.15%   | -44.15%            | -31.38% |     0.45 |       72 | 42.53%     | ok               |
|          40 | 6.40%    | -44.15%            | -33.91% |     0.27 |       66 | 35.82%     | ok               |
|          30 | -4.69%   | -44.15%            | -31.82% |     0.15 |       67 | 47.89%     | ok               |
|          45 | -3.54%   | -44.15%            | -37.18% |     0.14 |       60 | 30.27%     | ok               |
|          50 | -8.53%   | -44.15%            | -39.26% |     0.05 |       56 | 22.80%     | ok               |

## YFI-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -45.00%  | -61.79%            | -45.00% |    -0.75 |       54 | 27.39%     | ok               |
|          35 | -50.16%  | -61.79%            | -51.74% |    -0.83 |       62 | 34.67%     | ok               |
|          45 | -43.55%  | -61.79%            | -43.55% |    -0.89 |       66 | 22.80%     | ok               |
|          30 | -57.64%  | -61.79%            | -60.14% |    -1.01 |       77 | 38.70%     | ok               |
|          25 | -60.85%  | -61.79%            | -63.18% |    -1.07 |       76 | 43.30%     | ok               |

## ZEC-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 193.61%  | 2854.68%           | -30.64% |     1.05 |       46 | 31.61%     | ok               |
|          35 | 153.89%  | 2854.68%           | -50.84% |     0.94 |       52 | 36.97%     | ok               |
|          30 | 133.60%  | 2854.68%           | -56.50% |     0.88 |       59 | 40.23%     | ok               |
|          40 | 120.40%  | 2854.68%           | -54.22% |     0.85 |       52 | 34.87%     | ok               |
|          25 | 120.96%  | 2854.68%           | -58.07% |     0.84 |       59 | 42.53%     | ok               |
