# Market Tracker Backtest Report

_Generated: 2026-06-18T01:43:28+00:00_

## Data Sources

- Crypto: Kraken -> Coinbase -> CoinGecko OHLC -> CoinPaprika fallback chain.
- Stocks / ETFs / indices: Stooq -> Yahoo Finance fallback chain.
- Data rows are generated from real market APIs. Mock OHLCV rows are not generated.

## Data Freshness

- Rows: **92,400**
- Symbols: **161**
- Date range: **2024-01-25** to **2026-06-18**

## Latest Signals

| symbol     | date                |         close |   composite_score | signal   | data_source   |
|:-----------|:--------------------|--------------:|------------------:|:---------|:--------------|
| AMAT       | 2026-06-17 00:00:00 |   592.92      |         71.75     | LONG     | Yahoo Finance |
| BAC        | 2026-06-17 00:00:00 |    56.53      |         50.75     | LONG     | Yahoo Finance |
| BLK        | 2026-06-17 00:00:00 |  1057.38      |         53.1667   | LONG     | Yahoo Finance |
| C          | 2026-06-17 00:00:00 |   143.78      |         70.75     | LONG     | Yahoo Finance |
| DXY-INDEX  | 2026-06-17 00:00:00 |   100.25      |         83.0645   | LONG     | Yahoo Finance |
| GE         | 2026-06-17 00:00:00 |   357.03      |         63.9167   | LONG     | Yahoo Finance |
| GS         | 2026-06-17 00:00:00 |  1099.14      |         51.5833   | LONG     | Yahoo Finance |
| HD         | 2026-06-17 00:00:00 |   327.48      |         33.9167   | LONG     | Yahoo Finance |
| ITA        | 2026-06-17 00:00:00 |   242.79      |         60.5833   | LONG     | Yahoo Finance |
| JPM        | 2026-06-17 00:00:00 |   333.46      |         52.75     | LONG     | Yahoo Finance |
| LLY        | 2026-06-17 00:00:00 |  1112         |         45.4167   | LONG     | Yahoo Finance |
| LRCX       | 2026-06-17 00:00:00 |   374.18      |         70.9167   | LONG     | Yahoo Finance |
| MS         | 2026-06-17 00:00:00 |   224.96      |         74.0833   | LONG     | Yahoo Finance |
| MU         | 2026-06-17 00:00:00 |  1043.19      |         44.0833   | LONG     | Yahoo Finance |
| PG         | 2026-06-17 00:00:00 |   150.56      |         78.1667   | LONG     | Yahoo Finance |
| RTX        | 2026-06-17 00:00:00 |   192.58      |         65.5833   | LONG     | Yahoo Finance |
| TIA-USD    | 2026-06-18 00:00:00 |     0.3986    |         36.4167   | LONG     | Kraken API    |
| UNH        | 2026-06-17 00:00:00 |   399.53      |         61.0833   | LONG     | Yahoo Finance |
| WFC        | 2026-06-17 00:00:00 |    83.81      |         57.5833   | LONG     | Yahoo Finance |
| XLM-USD    | 2026-06-18 00:00:00 |     0.2442    |         68.8333   | LONG     | Kraken API    |
| AAPL       | 2026-06-17 00:00:00 |   295.95      |         -1.58333  | NEUTRAL  | Yahoo Finance |
| AAVE-USD   | 2026-06-18 00:00:00 |    74.4       |         14.6667   | NEUTRAL  | Kraken API    |
| ABBV       | 2026-06-17 00:00:00 |   221.23      |         19.0833   | NEUTRAL  | Yahoo Finance |
| ADA-USD    | 2026-06-18 00:00:00 |     0.167864  |        -21        | NEUTRAL  | Kraken API    |
| AGG        | 2026-06-17 00:00:00 |    98.61      |        -41.9167   | NEUTRAL  | Yahoo Finance |
| ALGO-USD   | 2026-06-18 00:00:00 |     0.10027   |        -10        | NEUTRAL  | Kraken API    |
| AMD        | 2026-06-17 00:00:00 |   512.48      |         24.6667   | NEUTRAL  | Yahoo Finance |
| AMGN       | 2026-06-17 00:00:00 |   341.66      |         28.5833   | NEUTRAL  | Yahoo Finance |
| AMZN       | 2026-06-17 00:00:00 |   237.5       |        -17.3333   | NEUTRAL  | Yahoo Finance |
| APT-USD    | 2026-06-18 00:00:00 |     0.6781    |        -19        | NEUTRAL  | Kraken API    |
| ARB-USD    | 2026-06-18 00:00:00 |     0.0872    |        -15.5      | NEUTRAL  | Kraken API    |
| ARKK       | 2026-06-17 00:00:00 |    78.49      |         16.75     | NEUTRAL  | Yahoo Finance |
| ATOM-USD   | 2026-06-18 00:00:00 |     1.8841    |         -3.33333  | NEUTRAL  | Kraken API    |
| AVAX-USD   | 2026-06-18 00:00:00 |     6.784     |        -21        | NEUTRAL  | Kraken API    |
| AVGO       | 2026-06-17 00:00:00 |   392.9       |        -44.25     | NEUTRAL  | Yahoo Finance |
| BA         | 2026-06-17 00:00:00 |   225.63      |         24.5      | NEUTRAL  | Yahoo Finance |
| BND        | 2026-06-17 00:00:00 |    73.14      |        -41.9167   | NEUTRAL  | Yahoo Finance |
| BONK-USD   | 2026-06-18 00:00:00 |     4.684e-06 |        -10        | NEUTRAL  | Kraken API    |
| BTC-USD    | 2026-06-18 00:00:00 | 64619.9       |          0.666667 | NEUTRAL  | Kraken API    |
| CAT        | 2026-06-17 00:00:00 |   955.92      |         62.8333   | NEUTRAL  | Yahoo Finance |
| CL         | 2026-06-17 00:00:00 |    90.58      |         41.6667   | NEUTRAL  | Yahoo Finance |
| COMP-USD   | 2026-06-18 00:00:00 |    17.53      |        -12.5833   | NEUTRAL  | Kraken API    |
| COP        | 2026-06-17 00:00:00 |   111.21      |        -21.0833   | NEUTRAL  | Yahoo Finance |
| COST       | 2026-06-17 00:00:00 |   965.59      |        -24.3333   | NEUTRAL  | Yahoo Finance |
| CRM        | 2026-06-17 00:00:00 |   155.02      |        -69        | NEUTRAL  | Yahoo Finance |
| CRV-USD    | 2026-06-18 00:00:00 |     0.22599   |         17.3333   | NEUTRAL  | Kraken API    |
| CSCO       | 2026-06-17 00:00:00 |   117.33      |         15.9167   | NEUTRAL  | Yahoo Finance |
| CVX        | 2026-06-17 00:00:00 |   177.58      |        -23.5833   | NEUTRAL  | Yahoo Finance |
| DASH-USD   | 2026-06-18 00:00:00 |    36.435     |        -21.3333   | NEUTRAL  | Kraken API    |
| DBC        | 2026-06-17 00:00:00 |    27.71      |        -15.3333   | NEUTRAL  | Yahoo Finance |
| DE         | 2026-06-17 00:00:00 |   588.47      |         62.8333   | NEUTRAL  | Yahoo Finance |
| DIA        | 2026-06-17 00:00:00 |   516.3       |         41.3333   | NEUTRAL  | Yahoo Finance |
| DOGE-USD   | 2026-06-18 00:00:00 |     0.0861631 |        -11.5      | NEUTRAL  | Kraken API    |
| DOT-USD    | 2026-06-18 00:00:00 |     1.0074    |        -21        | NEUTRAL  | Kraken API    |
| EEM        | 2026-06-17 00:00:00 |    68.56      |         17.6667   | NEUTRAL  | Yahoo Finance |
| EFA        | 2026-06-17 00:00:00 |   103.78      |          1.33333  | NEUTRAL  | Yahoo Finance |
| EOG        | 2026-06-17 00:00:00 |   133.25      |        -26.0833   | NEUTRAL  | Yahoo Finance |
| ETC-USD    | 2026-06-18 00:00:00 |     7.379     |          2.66667  | NEUTRAL  | Kraken API    |
| ETH-USD    | 2026-06-18 00:00:00 |  1757.25      |        -24        | NEUTRAL  | Kraken API    |
| EWJ        | 2026-06-17 00:00:00 |    94.45      |         34.3333   | NEUTRAL  | Yahoo Finance |
| FCX        | 2026-06-17 00:00:00 |    69.06      |         53.3333   | NEUTRAL  | Yahoo Finance |
| FET-USD    | 2026-06-18 00:00:00 |     0.201     |        -59.8333   | NEUTRAL  | Kraken API    |
| FIL-USD    | 2026-06-18 00:00:00 |     0.804     |        -19        | NEUTRAL  | Kraken API    |
| GDX        | 2026-06-17 00:00:00 |    84.36      |         18.8333   | NEUTRAL  | Yahoo Finance |
| GDXJ       | 2026-06-17 00:00:00 |   109.79      |        -28.1667   | NEUTRAL  | Yahoo Finance |
| GOOGL      | 2026-06-17 00:00:00 |   363.79      |        -14.4167   | NEUTRAL  | Yahoo Finance |
| GRT-USD    | 2026-06-18 00:00:00 |     0.01958   |        -24.3333   | NEUTRAL  | Kraken API    |
| HBAR-USD   | 2026-06-18 00:00:00 |     0.08151   |        -29.75     | NEUTRAL  | Kraken API    |
| HON        | 2026-06-17 00:00:00 |   228.61      |         47.5      | NEUTRAL  | Yahoo Finance |
| HYG        | 2026-06-17 00:00:00 |    79.73      |        -48.4167   | NEUTRAL  | Yahoo Finance |
| IBM        | 2026-06-17 00:00:00 |   262.35      |        -23.5833   | NEUTRAL  | Yahoo Finance |
| ICP-USD    | 2026-06-18 00:00:00 |     2.336     |        -63.5833   | NEUTRAL  | Kraken API    |
| IEF        | 2026-06-17 00:00:00 |    94.02      |        -47.6667   | NEUTRAL  | Yahoo Finance |
| IEMG       | 2026-06-17 00:00:00 |    83.02      |         17.6667   | NEUTRAL  | Yahoo Finance |
| INJ-USD    | 2026-06-18 00:00:00 |     5.491     |         31        | NEUTRAL  | Kraken API    |
| INTC       | 2026-06-17 00:00:00 |   121.1       |         40.1667   | NEUTRAL  | Yahoo Finance |
| INTU       | 2026-06-17 00:00:00 |   269.08      |        -64        | NEUTRAL  | Yahoo Finance |
| IWM        | 2026-06-17 00:00:00 |   289.88      |         17.1667   | NEUTRAL  | Yahoo Finance |
| JNJ        | 2026-06-17 00:00:00 |   234.2       |         62.3333   | NEUTRAL  | Yahoo Finance |
| KO         | 2026-06-17 00:00:00 |    79.93      |          6.83333  | NEUTRAL  | Yahoo Finance |
| LDO-USD    | 2026-06-18 00:00:00 |     0.281     |         -3.33333  | NEUTRAL  | Kraken API    |
| LIN        | 2026-06-17 00:00:00 |   515.85      |         60.8333   | NEUTRAL  | Yahoo Finance |
| LINK-USD   | 2026-06-18 00:00:00 |     8.10152   |         -1.33333  | NEUTRAL  | Kraken API    |
| LTC-USD    | 2026-06-18 00:00:00 |    44.95      |        -15.5      | NEUTRAL  | Kraken API    |
| MCD        | 2026-06-17 00:00:00 |   283.82      |          1.66667  | NEUTRAL  | Yahoo Finance |
| META       | 2026-06-17 00:00:00 |   567.58      |        -69.5      | NEUTRAL  | Yahoo Finance |
| MPC        | 2026-06-17 00:00:00 |   244.61      |         -5.83333  | NEUTRAL  | Yahoo Finance |
| MRK        | 2026-06-17 00:00:00 |   115.44      |        -10.8333   | NEUTRAL  | Yahoo Finance |
| NEAR-USD   | 2026-06-18 00:00:00 |     2.2253    |         34.6667   | NEUTRAL  | Kraken API    |
| NEM        | 2026-06-17 00:00:00 |   105.67      |         24.3333   | NEUTRAL  | Yahoo Finance |
| NKE        | 2026-06-17 00:00:00 |    44.19      |        -51.6667   | NEUTRAL  | Yahoo Finance |
| NVDA       | 2026-06-17 00:00:00 |   204.65      |        -41.5833   | NEUTRAL  | Yahoo Finance |
| OP-USD     | 2026-06-18 00:00:00 |     0.1092    |          2.5      | NEUTRAL  | Kraken API    |
| OXY        | 2026-06-17 00:00:00 |    53.04      |        -25.25     | NEUTRAL  | Yahoo Finance |
| PEP        | 2026-06-17 00:00:00 |   141.59      |        -17.4167   | NEUTRAL  | Yahoo Finance |
| PEPE-USD   | 2026-06-18 00:00:00 |     2.95e-06  |         -3.33333  | NEUTRAL  | Kraken API    |
| PFE        | 2026-06-17 00:00:00 |    25.92      |        -16.9167   | NEUTRAL  | Yahoo Finance |
| PM         | 2026-06-17 00:00:00 |   179.44      |         25.9167   | NEUTRAL  | Yahoo Finance |
| QCOM       | 2026-06-17 00:00:00 |   212.97      |         -2.83333  | NEUTRAL  | Yahoo Finance |
| QQQ        | 2026-06-17 00:00:00 |   722.51      |         26.1667   | NEUTRAL  | Yahoo Finance |
| RENDER-USD | 2026-06-18 00:00:00 |     1.73      |        -42.5833   | NEUTRAL  | Kraken API    |
| SBUX       | 2026-06-17 00:00:00 |    99.82      |         14.75     | NEUTRAL  | Yahoo Finance |
| SCHW       | 2026-06-17 00:00:00 |    94.51      |         45.75     | NEUTRAL  | Yahoo Finance |
| SHIB-USD   | 2026-06-18 00:00:00 |     4.952e-06 |         -6.83333  | NEUTRAL  | Kraken API    |
| SHY        | 2026-06-17 00:00:00 |    81.88      |        -49.9167   | NEUTRAL  | Yahoo Finance |
| SKY-USD    | 2026-06-18 00:00:00 |     0.05707   |        -19        | NEUTRAL  | Kraken API    |
| SLB        | 2026-06-17 00:00:00 |    50.33      |        -29        | NEUTRAL  | Yahoo Finance |
| SMH        | 2026-06-17 00:00:00 |   623.97      |         31.3333   | NEUTRAL  | Yahoo Finance |
| SNX-USD    | 2026-06-18 00:00:00 |     0.2546    |        -17.5      | NEUTRAL  | Kraken API    |
| SOL-USD    | 2026-06-18 00:00:00 |    72.41      |         14.6667   | NEUTRAL  | Kraken API    |
| SOXX       | 2026-06-17 00:00:00 |   599.73      |         31.3333   | NEUTRAL  | Yahoo Finance |
| SPY        | 2026-06-17 00:00:00 |   740.96      |         -7.08333  | NEUTRAL  | Yahoo Finance |
| SUSHI-USD  | 2026-06-18 00:00:00 |     0.1902    |        -19.25     | NEUTRAL  | Kraken API    |
| TGT        | 2026-06-17 00:00:00 |   127.81      |         29        | NEUTRAL  | Yahoo Finance |
| TLT        | 2026-06-17 00:00:00 |    86.33      |         29.1667   | NEUTRAL  | Yahoo Finance |
| TMUS       | 2026-06-17 00:00:00 |   181.31      |        -29.75     | NEUTRAL  | Yahoo Finance |
| TRX-USD    | 2026-06-18 00:00:00 |     0.321188  |         17.75     | NEUTRAL  | Kraken API    |
| TSLA       | 2026-06-17 00:00:00 |   396.38      |        -61.25     | NEUTRAL  | Yahoo Finance |
| TXN        | 2026-06-17 00:00:00 |   301.88      |         14.1667   | NEUTRAL  | Yahoo Finance |
| UNI-USD    | 2026-06-18 00:00:00 |     3.2354    |         29.3333   | NEUTRAL  | Kraken API    |
| UPS        | 2026-06-17 00:00:00 |   105.13      |         28.6667   | NEUTRAL  | Yahoo Finance |
| USO        | 2026-06-17 00:00:00 |   114.23      |        -25.0833   | NEUTRAL  | Yahoo Finance |
| VEA        | 2026-06-17 00:00:00 |    72         |         40.8333   | NEUTRAL  | Yahoo Finance |
| VIXY       | 2026-06-17 00:00:00 |    22.7       |        -28.0833   | NEUTRAL  | Yahoo Finance |
| VNQ        | 2026-06-17 00:00:00 |    95.61      |         21.6667   | NEUTRAL  | Yahoo Finance |
| VTI        | 2026-06-17 00:00:00 |   365.76      |         -9.33333  | NEUTRAL  | Yahoo Finance |
| VWO        | 2026-06-17 00:00:00 |    59.81      |         17.75     | NEUTRAL  | Yahoo Finance |
| VZ         | 2026-06-17 00:00:00 |    45.84      |         -3.33333  | NEUTRAL  | Yahoo Finance |
| WIF-USD    | 2026-06-18 00:00:00 |     0.1691    |         11.1667   | NEUTRAL  | Kraken API    |
| WMT        | 2026-06-17 00:00:00 |   118.13      |         20.8333   | NEUTRAL  | Yahoo Finance |
| XBI        | 2026-06-17 00:00:00 |   139.39      |         63.5      | NEUTRAL  | Yahoo Finance |
| XLB        | 2026-06-17 00:00:00 |    52.02      |         53.1667   | NEUTRAL  | Yahoo Finance |
| XLE        | 2026-06-17 00:00:00 |    54.67      |        -23.5833   | NEUTRAL  | Yahoo Finance |
| XLF        | 2026-06-17 00:00:00 |    54.05      |         50.5      | NEUTRAL  | Yahoo Finance |
| XLI        | 2026-06-17 00:00:00 |   179.6       |         61.1667   | NEUTRAL  | Yahoo Finance |
| XLK        | 2026-06-17 00:00:00 |   185.8       |         26.6667   | NEUTRAL  | Yahoo Finance |
| XLP        | 2026-06-17 00:00:00 |    83.68      |         23.9167   | NEUTRAL  | Yahoo Finance |
| XLU        | 2026-06-17 00:00:00 |    44.46      |        -10.4167   | NEUTRAL  | Yahoo Finance |
| XLV        | 2026-06-17 00:00:00 |   150.71      |         14.75     | NEUTRAL  | Yahoo Finance |
| XLY        | 2026-06-17 00:00:00 |   115.49      |        -63.75     | NEUTRAL  | Yahoo Finance |
| XOM        | 2026-06-17 00:00:00 |   140.74      |        -23.0833   | NEUTRAL  | Yahoo Finance |
| XRP-USD    | 2026-06-18 00:00:00 |     1.18979   |          0.666667 | NEUTRAL  | Kraken API    |
| YFI-USD    | 2026-06-18 00:00:00 |  1941.8       |        -13.5      | NEUTRAL  | Kraken API    |
| ZEC-USD    | 2026-06-18 00:00:00 |   482.94      |         51.9167   | NEUTRAL  | Kraken API    |
| ADBE       | 2026-06-17 00:00:00 |   196.28      |        -57.75     | SHORT    | Yahoo Finance |
| BCH-USD    | 2026-06-18 00:00:00 |   213.77      |        -37        | SHORT    | Kraken API    |
| BITO       | 2026-06-17 00:00:00 |     8.73      |        -55.3333   | SHORT    | Yahoo Finance |
| CMCSA      | 2026-06-17 00:00:00 |    22.69      |        -34.75     | SHORT    | Yahoo Finance |
| DIS        | 2026-06-17 00:00:00 |   100.86      |        -39.4167   | SHORT    | Yahoo Finance |
| FXI        | 2026-06-17 00:00:00 |    33.65      |        -48.5      | SHORT    | Yahoo Finance |
| GLD        | 2026-06-17 00:00:00 |   388.6       |        -55        | SHORT    | Yahoo Finance |
| IBIT       | 2026-06-17 00:00:00 |    36.36      |        -53.5833   | SHORT    | Yahoo Finance |
| MSFT       | 2026-06-17 00:00:00 |   378.91      |        -58.25     | SHORT    | Yahoo Finance |
| NFLX       | 2026-06-17 00:00:00 |    76.96      |        -61.5833   | SHORT    | Yahoo Finance |
| NOW        | 2026-06-17 00:00:00 |    95.48      |        -55.0833   | SHORT    | Yahoo Finance |
| ORCL       | 2026-06-17 00:00:00 |   183.53      |        -58        | SHORT    | Yahoo Finance |
| POL-USD    | 2026-06-18 00:00:00 |     0.07756   |        -33        | SHORT    | Kraken API    |
| SLV        | 2026-06-17 00:00:00 |    60.61      |        -58.3333   | SHORT    | Yahoo Finance |
| T          | 2026-06-17 00:00:00 |    22.44      |        -59.9167   | SHORT    | Yahoo Finance |
| TMO        | 2026-06-17 00:00:00 |   461.69      |        -38.0833   | SHORT    | Yahoo Finance |
| XLC        | 2026-06-17 00:00:00 |   109.2       |        -59.5833   | SHORT    | Yahoo Finance |

## Edge Summary

- Symbols with trades: **160** of 160
- Beat buy-and-hold: **35.00%** of traded symbols
- Positive return: **33.75%** of traded symbols
- Median strategy return: **-8.92%** (benchmark **14.01%**)
- Median excess vs benchmark: **-27.33%**
- Median Sharpe: **-0.07**
- Median exposure: **44.42%**

> Edge is real only if both _beat buy-and-hold_ and _median excess_ are convincingly positive across many symbols. Treat a single high-return symbol as noise.

## Portfolio Backtest

Actual capital-allocation books (not per-symbol averages). Benchmarks: `equal_weight_buyhold` (whole tracked universe), `spy_buyhold` (100% SPY), and `sixty_forty` (60% SPY / 40% AGG). `high_conf_voltarget` inverse-vol-weights the HIGH-confidence book; `conviction_long_short` is market-neutral. Judge on **Sharpe** and **max_drawdown** out-of-sample, not raw return: a fully-invested long book wins on return in a bull market but carries all the risk.

| strategy              | scope         | ann_return   | ann_vol   |   sharpe | max_drawdown   | total_return   |   avg_gross_exposure |
|:----------------------|:--------------|:-------------|:----------|---------:|:---------------|:---------------|---------------------:|
| equal_weight_buyhold  | full          | -8.95%       | 33.86%    |    -0.26 | -57.60%        | -36.12%        |                 1    |
| equal_weight_buyhold  | out_of_sample | -4.10%       | 34.35%    |    -0.12 | -39.63%        | -10.07%        |                 1    |
| all_signals_ew        | full          | -7.80%       | 28.22%    |    -0.28 | -59.79%        | -30.15%        |                 1    |
| all_signals_ew        | out_of_sample | 10.49%       | 28.42%    |     0.37 | -24.86%        | 7.13%          |                 1    |
| high_conf_ew          | full          | 2.27%        | 32.93%    |     0.07 | -44.81%        | -8.98%         |                 0.89 |
| high_conf_ew          | out_of_sample | 30.45%       | 36.48%    |     0.83 | -20.80%        | 29.02%         |                 0.89 |
| high_conf_voltarget   | full          | 3.13%        | 30.62%    |     0.1  | -36.86%        | -4.42%         |                 0.89 |
| high_conf_voltarget   | out_of_sample | 24.43%       | 34.70%    |     0.7  | -16.98%        | 21.86%         |                 0.89 |
| conviction_long_short | full          | -8.34%       | 23.52%    |    -0.35 | -35.88%        | -28.69%        |                 0.97 |
| conviction_long_short | out_of_sample | -3.21%       | 27.16%    |    -0.12 | -21.02%        | -7.09%         |                 0.97 |
| spy_buyhold           | full          | 7.75%        | 13.40%    |     0.58 | -17.81%        | 23.16%         |                 0.79 |
| spy_buyhold           | out_of_sample | -3.20%       | 10.00%    |    -0.32 | -14.83%        | -3.86%         |                 0.79 |
| sixty_forty           | full          | 4.42%        | 8.49%     |     0.52 | -10.80%        | 13.11%         |                 0.79 |
| sixty_forty           | out_of_sample | -3.08%       | 6.51%     |    -0.47 | -10.06%        | -3.44%         |                 0.79 |

## Walk-Forward Robustness

Each book measured across contiguous time folds (each a different regime). A book has durable edge only if `mean_sharpe` is positive, `min_sharpe` isn't deeply negative, and `pct_positive_folds` is high — a single great fold doesn't count. `fold_sharpes` lists each fold oldest-to-newest.

| strategy              |   n_folds |   mean_sharpe |   median_sharpe |   min_sharpe | pct_positive_folds   | mean_return   | fold_sharpes                |
|:----------------------|----------:|--------------:|----------------:|-------------:|:---------------------|:--------------|:----------------------------|
| equal_weight_buyhold  |         5 |         -0    |           -0.45 |        -1.62 | 40.00%               | -6.04%        | 1.47;-1.62;1.14;-0.45;-0.57 |
| all_signals_ew        |         5 |         -0.14 |            0.34 |        -1.72 | 60.00%               | -5.07%        | 0.34;0.51;-1.06;-1.72;1.24  |
| high_conf_ew          |         5 |          0.3  |           -0.03 |        -0.59 | 40.00%               | -0.92%        | 1.30;-0.03;-0.59;-0.36;1.20 |
| high_conf_voltarget   |         5 |          0.43 |            0.19 |        -0.63 | 60.00%               | -0.32%        | 2.16;0.19;-0.63;-0.19;0.61  |
| conviction_long_short |         5 |         -0.34 |           -0.24 |        -1.41 | 40.00%               | -6.04%        | -1.41;0.48;-0.24;-0.97;0.43 |
| spy_buyhold           |         5 |          0.56 |            0.27 |        -0.35 | 80.00%               | 4.40%         | 1.59;1.22;0.27;-0.35;0.09   |
| sixty_forty           |         5 |          0.49 |            0.29 |        -0.23 | 60.00%               | 2.55%         | 1.67;0.84;0.29;-0.23;-0.14  |

## Strategy Comparison

Each decision rule backtested over the same data. `out_of_sample` is the most recent ~35% of each symbol's history (unseen tail). A rule has real edge only if `median_excess` and `beat_benchmark_pct` stay positive out-of-sample, not just full-sample.

| strategy        | scope         |   symbols | beat_benchmark_pct   | positive_pct   | median_return   | median_benchmark   | median_excess   |   median_sharpe |   total_trades |
|:----------------|:--------------|----------:|:---------------------|:---------------|:----------------|:-------------------|:----------------|----------------:|---------------:|
| trend           | full          |       160 | 35.00%               | 33.75%         | -8.92%          | 14.01%             | -27.33%         |           -0.07 |          11205 |
| trend           | out_of_sample |       160 | 35.00%               | 53.12%         | 3.28%           | 7.30%              | -8.93%          |            0.38 |           3935 |
| mean_reversion  | full          |       157 | 41.40%               | 48.41%         | -0.20%          | 12.24%             | -17.04%         |           -0.03 |           1248 |
| mean_reversion  | out_of_sample |       128 | 42.19%               | 57.81%         | 0.33%           | 2.77%              | -5.12%          |            0.67 |            474 |
| regime_adaptive | full          |       160 | 36.25%               | 33.75%         | -9.67%          | 14.01%             | -26.74%         |           -0.06 |          11480 |
| regime_adaptive | out_of_sample |       160 | 35.00%               | 54.37%         | 3.72%           | 7.30%              | -8.97%          |            0.38 |           4038 |

## Signal Calibration

Realized forward return in the signal's direction, grouped by confidence. HIGH should outrank LOW for the confidence score to be meaningful.

| confidence_level   |   horizon |     n | mean_return   | median_return   | win_rate   |
|:-------------------|----------:|------:|:--------------|:----------------|:-----------|
| HIGH               |         5 |  8179 | 0.19%         | 0.15%           | 52.45%     |
| MEDIUM             |         5 | 29182 | 0.07%         | 0.09%           | 51.05%     |
| LOW                |         5 |  3274 | -0.55%        | -0.49%          | 45.14%     |
| ALL                |         5 | 40635 | 0.04%         | 0.07%           | 50.85%     |
| HIGH               |        10 |  8139 | 0.50%         | 0.20%           | 52.33%     |
| MEDIUM             |        10 | 28890 | 0.24%         | 0.16%           | 51.32%     |
| LOW                |        10 |  3255 | -0.82%        | -0.72%          | 45.38%     |
| ALL                |        10 | 40284 | 0.21%         | 0.12%           | 51.04%     |
| HIGH               |        20 |  8043 | 0.96%         | 0.53%           | 54.00%     |
| MEDIUM             |        20 | 28342 | 0.87%         | 0.62%           | 53.58%     |
| LOW                |        20 |  3216 | -0.58%        | -0.50%          | 47.17%     |
| ALL                |        20 | 39601 | 0.77%         | 0.53%           | 53.15%     |

## Backtest Summary

### Data Quality / Signal Availability

- **ok**: 160 symbols

| symbol     |   trades | return   | benchmark_return   | mdd     |   sharpe | exposure   | skipped_reason   |
|:-----------|---------:|:---------|:-------------------|:--------|---------:|:-----------|:-----------------|
| AAPL       |       63 | 12.73%   | 52.42%             | -20.65% |     0.35 | 48.59%     | ok               |
| AAVE-USD   |       78 | -62.44%  | -74.38%            | -69.19% |    -0.76 | 36.78%     | ok               |
| ABBV       |       64 | -14.48%  | 33.97%             | -30.55% |    -0.27 | 48.75%     | ok               |
| ADA-USD    |       86 | -82.04%  | -82.23%            | -89.12% |    -0.63 | 46.36%     | ok               |
| ADBE       |       66 | -22.82%  | -68.47%            | -38.12% |    -0.23 | 56.74%     | ok               |
| AGG        |       69 | -6.61%   | 0.44%              | -10.16% |    -1.1  | 31.11%     | ok               |
| ALGO-USD   |       86 | -50.43%  | -71.28%            | -53.13% |    -0.57 | 38.12%     | ok               |
| AMAT       |       69 | -20.65%  | 243.46%            | -57.21% |    -0.12 | 53.41%     | ok               |
| AMD        |       56 | -0.51%   | 184.19%            | -46.42% |     0.21 | 38.10%     | ok               |
| AMGN       |       71 | -19.54%  | 10.12%             | -34.14% |    -0.38 | 47.92%     | ok               |
| AMZN       |       74 | -33.84%  | 50.55%             | -42.48% |    -0.99 | 38.27%     | ok               |
| APT-USD    |       76 | -30.32%  | -92.01%            | -69.96% |    -0.05 | 44.25%     | ok               |
| ARB-USD    |       68 | -0.31%   | -87.60%            | -62.67% |     0.24 | 39.27%     | ok               |
| ARKK       |       81 | -32.67%  | 71.30%             | -35.19% |    -0.57 | 38.94%     | ok               |
| ATOM-USD   |       88 | -67.61%  | -70.01%            | -73.59% |    -1.11 | 44.25%     | ok               |
| AVAX-USD   |       70 | -25.69%  | -80.78%            | -53.72% |    -0.13 | 38.89%     | ok               |
| AVGO       |       60 | 29.51%   | 219.43%            | -35.76% |     0.48 | 45.42%     | ok               |
| BA         |       69 | 3.09%    | 11.76%             | -30.56% |     0.18 | 50.08%     | ok               |
| BAC        |       78 | -14.56%  | 69.30%             | -27.64% |    -0.34 | 46.76%     | ok               |
| BCH-USD    |       76 | -5.72%   | -50.07%            | -53.87% |     0.14 | 47.13%     | ok               |
| BITO       |       78 | 4.89%    | -54.58%            | -42.82% |     0.23 | 40.43%     | ok               |
| BLK        |       75 | -5.83%   | 33.77%             | -21.49% |    -0.11 | 42.76%     | ok               |
| BND        |       65 | -7.32%   | 0.45%              | -9.89%  |    -1.18 | 32.28%     | ok               |
| BONK-USD   |       68 | 69.11%   | -82.13%            | -43.77% |     0.72 | 41.95%     | ok               |
| BTC-USD    |       70 | 6.41%    | -31.61%            | -23.38% |     0.25 | 51.15%     | ok               |
| C          |       83 | -23.83%  | 167.60%            | -37.02% |    -0.44 | 50.58%     | ok               |
| CAT        |       70 | 34.32%   | 217.82%            | -21.02% |     0.62 | 56.74%     | ok               |
| CL         |       60 | 17.30%   | 11.52%             | -14.32% |     0.59 | 48.09%     | ok               |
| CMCSA      |       80 | -39.47%  | -46.52%            | -41.34% |    -1.03 | 44.09%     | ok               |
| COMP-USD   |       89 | -36.73%  | -75.98%            | -58.43% |    -0.21 | 45.02%     | ok               |
| COP        |       73 | -24.21%  | -0.75%             | -43.77% |    -0.45 | 40.27%     | ok               |
| COST       |       60 | 6.71%    | 42.02%             | -29.73% |     0.26 | 46.76%     | ok               |
| CRM        |       67 | -35.73%  | -44.44%            | -41.69% |    -0.73 | 43.93%     | ok               |
| CRV-USD    |       64 | -12.43%  | -72.13%            | -39.89% |     0.1  | 34.48%     | ok               |
| CSCO       |       59 | 21.90%   | 124.21%            | -21.79% |     0.49 | 50.42%     | ok               |
| CVX        |       69 | -14.77%  | 19.53%             | -26.75% |    -0.37 | 41.43%     | ok               |
| DASH-USD   |       67 | -45.83%  | 3.47%              | -64.43% |    -0.06 | 31.99%     | ok               |
| DBC        |       58 | -12.57%  | 23.10%             | -25.35% |    -0.43 | 32.78%     | ok               |
| DE         |       72 | -6.65%   | 49.73%             | -25.24% |    -0.05 | 45.92%     | ok               |
| DIA        |       60 | -2.42%   | 35.70%             | -12.94% |    -0.09 | 45.92%     | ok               |
| DIS        |       63 | -6.30%   | 6.33%              | -24.86% |    -0.02 | 48.42%     | ok               |
| DOGE-USD   |       75 | -16.53%  | -74.51%            | -60.95% |     0.09 | 49.81%     | ok               |
| DOT-USD    |       90 | -47.22%  | -84.24%            | -61.09% |    -0.35 | 48.08%     | ok               |
| DXY-INDEX  |       44 | -3.31%   | -1.61%             | -6.06%  |    -0.52 | 29.07%     | ok               |
| EEM        |       64 | -9.40%   | 76.43%             | -25.67% |    -0.25 | 43.43%     | ok               |
| EFA        |       58 | -8.33%   | 38.89%             | -13.87% |    -0.3  | 43.93%     | ok               |
| EOG        |       79 | -25.23%  | 16.02%             | -48.13% |    -0.55 | 46.26%     | ok               |
| ETC-USD    |       64 | -35.69%  | -69.97%            | -48.16% |    -0.51 | 31.23%     | ok               |
| ETH-USD    |       60 | 157.31%  | -43.97%            | -30.11% |     1.28 | 44.83%     | ok               |
| EWJ        |       64 | -17.33%  | 43.28%             | -30.73% |    -0.55 | 40.93%     | ok               |
| FCX        |       69 | -31.93%  | 75.10%             | -46.84% |    -0.39 | 45.92%     | ok               |
| FET-USD    |       77 | -2.40%   | -83.82%            | -48.39% |     0.26 | 39.08%     | ok               |
| FIL-USD    |       70 | -33.66%  | -83.66%            | -49.05% |    -0.29 | 33.14%     | ok               |
| FXI        |       48 | -6.46%   | 47.91%             | -24.33% |    -0.08 | 28.29%     | ok               |
| GDX        |       62 | -0.08%   | 198.62%            | -34.99% |     0.13 | 48.25%     | ok               |
| GDXJ       |       68 | -27.45%  | 219.25%            | -44.93% |    -0.31 | 46.09%     | ok               |
| GE         |       74 | 19.80%   | 244.31%            | -27.82% |     0.43 | 52.08%     | ok               |
| GLD        |       48 | 22.12%   | 107.65%            | -16.63% |     0.59 | 44.59%     | ok               |
| GOOGL      |       63 | 69.02%   | 139.54%            | -20.41% |     1.06 | 54.08%     | ok               |
| GRT-USD    |       87 | -14.10%  | -89.86%            | -57.16% |     0.06 | 41.95%     | ok               |
| GS         |       76 | 0.77%    | 187.21%            | -22.13% |     0.12 | 51.25%     | ok               |
| HD         |       71 | -3.66%   | -6.69%             | -17.69% |    -0.02 | 43.76%     | ok               |
| HON        |       97 | -30.18%  | 19.74%             | -30.77% |    -0.84 | 52.91%     | ok               |
| HYG        |       81 | -9.52%   | 2.63%              | -9.59%  |    -1.11 | 34.28%     | ok               |
| IBIT       |       32 | 33.20%   | -4.34%             | -18.95% |     0.72 | 30.66%     | ok               |
| IBM        |       72 | 10.19%   | 37.77%             | -25.31% |     0.3  | 50.58%     | ok               |
| ICP-USD    |       83 | -1.35%   | -76.13%            | -55.67% |     0.25 | 38.70%     | ok               |
| IEF        |       76 | -10.90%  | -1.17%             | -11.70% |    -1.54 | 32.78%     | ok               |
| IEMG       |       58 | -5.52%   | 69.78%             | -26.84% |    -0.12 | 43.59%     | ok               |
| INJ-USD    |       75 | -52.18%  | -72.65%            | -77.42% |    -0.49 | 37.93%     | ok               |
| INTC       |       70 | 55.82%   | 144.40%            | -60.60% |     0.62 | 49.25%     | ok               |
| INTU       |       65 | -12.52%  | -58.05%            | -43.77% |    -0.09 | 42.93%     | ok               |
| ITA        |       74 | 0.95%    | 99.55%             | -23.75% |     0.1  | 47.09%     | ok               |
| IWM        |       50 | 9.03%    | 47.92%             | -12.83% |     0.37 | 36.61%     | ok               |
| JNJ        |       71 | 6.64%    | 46.78%             | -17.51% |     0.29 | 50.58%     | ok               |
| JPM        |       77 | -18.40%  | 92.82%             | -33.43% |    -0.44 | 52.75%     | ok               |
| KO         |       51 | 27.92%   | 35.11%             | -8.07%  |     1    | 37.94%     | ok               |
| LDO-USD    |       76 | 10.11%   | -82.68%            | -60.93% |     0.36 | 38.51%     | ok               |
| LIN        |       68 | -0.80%   | 27.85%             | -21.53% |     0.03 | 38.94%     | ok               |
| LINK-USD   |       70 | -13.55%  | -58.15%            | -50.48% |     0.1  | 41.57%     | ok               |
| LLY        |       69 | -12.23%  | 77.18%             | -53.34% |    -0.07 | 51.41%     | ok               |
| LRCX       |       80 | -15.79%  | 332.28%            | -63.56% |    -0.04 | 46.26%     | ok               |
| LTC-USD    |       66 | -34.00%  | -54.31%            | -53.76% |    -0.29 | 48.47%     | ok               |
| MCD        |       75 | -2.55%   | -4.51%             | -18.81% |    -0.05 | 38.10%     | ok               |
| META       |       72 | -14.70%  | 44.36%             | -38.96% |    -0.11 | 50.75%     | ok               |
| MPC        |       71 | -13.74%  | 55.54%             | -44.76% |    -0.14 | 49.92%     | ok               |
| MRK        |       67 | -26.59%  | -3.90%             | -34.46% |    -0.6  | 46.76%     | ok               |
| MS         |       81 | -12.90%  | 155.58%            | -27.79% |    -0.25 | 48.25%     | ok               |
| MSFT       |       79 | -33.57%  | -6.41%             | -37.19% |    -0.88 | 47.92%     | ok               |
| MU         |       51 | 240.66%  | 1069.50%           | -68.76% |     1.28 | 59.73%     | ok               |
| NEAR-USD   |       87 | 4.05%    | -53.19%            | -59.86% |     0.29 | 42.15%     | ok               |
| NEM        |       78 | -29.69%  | 206.38%            | -38.49% |    -0.3  | 55.07%     | ok               |
| NFLX       |       64 | 30.32%   | 36.94%             | -21.09% |     0.67 | 54.74%     | ok               |
| NKE        |       91 | -37.92%  | -56.15%            | -55.35% |    -0.53 | 43.93%     | ok               |
| NOW        |       80 | 25.51%   | -37.73%            | -30.25% |     0.46 | 45.92%     | ok               |
| NVDA       |       74 | -30.35%  | 117.05%            | -45.02% |    -0.26 | 59.18%     | ok               |
| OP-USD     |       74 | 4.44%    | -93.68%            | -70.27% |     0.29 | 35.82%     | ok               |
| ORCL       |       74 | 51.80%   | 59.59%             | -29.47% |     0.62 | 53.58%     | ok               |
| OXY        |       63 | 2.48%    | -8.57%             | -30.85% |     0.16 | 43.09%     | ok               |
| PEP        |       85 | -10.61%  | -14.99%            | -21.35% |    -0.25 | 50.08%     | ok               |
| PEPE-USD   |       77 | 10.36%   | -82.50%            | -57.66% |     0.36 | 43.87%     | ok               |
| PFE        |       77 | -39.48%  | -5.64%             | -42.29% |    -1.26 | 36.27%     | ok               |
| PG         |       62 | -10.70%  | -3.25%             | -21.65% |    -0.37 | 41.43%     | ok               |
| PM         |       81 | -1.25%   | 96.73%             | -33.68% |     0.07 | 57.57%     | ok               |
| POL-USD    |       79 | 65.25%   | -83.62%            | -46.45% |     0.77 | 49.90%     | ok               |
| QCOM       |       77 | -18.84%  | 37.87%             | -57.69% |    -0.09 | 47.92%     | ok               |
| QQQ        |       62 | 19.13%   | 69.46%             | -12.88% |     0.55 | 46.26%     | ok               |
| RENDER-USD |       96 | -17.59%  | -58.41%            | -45.00% |     0.11 | 44.10%     | ok               |
| RTX        |       58 | 23.73%   | 111.77%            | -16.99% |     0.62 | 51.58%     | ok               |
| SBUX       |       62 | -25.08%  | 7.79%              | -29.34% |    -0.52 | 38.60%     | ok               |
| SCHW       |       74 | -21.97%  | 48.34%             | -30.41% |    -0.52 | 45.42%     | ok               |
| SHIB-USD   |       76 | -24.16%  | -76.64%            | -48.95% |    -0.08 | 52.49%     | ok               |
| SHY        |       50 | -2.29%   | -0.35%             | -2.85%  |    -0.79 | 35.11%     | ok               |
| SKY-USD    |       68 | -28.81%  | -1.31%             | -43.98% |    -0.37 | 41.08%     | ok               |
| SLB        |       75 | -29.08%  | -4.08%             | -54.95% |    -0.52 | 50.25%     | ok               |
| SLV        |       58 | 32.14%   | 189.45%            | -42.66% |     0.54 | 40.27%     | ok               |
| SMH        |       48 | 94.32%   | 224.36%            | -33.99% |     1.19 | 50.92%     | ok               |
| SNX-USD    |       63 | 8.38%    | -84.85%            | -32.91% |     0.33 | 40.04%     | ok               |
| SOL-USD    |       68 | -42.35%  | -60.37%            | -56.90% |    -0.22 | 60.15%     | ok               |
| SOXX       |       55 | 81.22%   | 192.87%            | -40.34% |     1.03 | 49.92%     | ok               |
| SPY        |       60 | 6.50%    | 51.83%             | -16.47% |     0.28 | 50.92%     | ok               |
| SUSHI-USD  |       90 | -75.60%  | -86.35%            | -81.22% |    -1.06 | 35.44%     | ok               |
| T          |       62 | 34.99%   | 30.62%             | -17.01% |     0.83 | 50.42%     | ok               |
| TGT        |       56 | -11.79%  | -10.11%            | -41.74% |    -0.16 | 38.60%     | ok               |
| TIA-USD    |       84 | -9.69%   | -91.37%            | -51.71% |     0.15 | 33.91%     | ok               |
| TLT        |       70 | -23.41%  | -8.12%             | -24.34% |    -1.73 | 32.28%     | ok               |
| TMO        |       57 | 18.33%   | -14.22%            | -16.83% |     0.46 | 48.09%     | ok               |
| TMUS       |       72 | 14.20%   | 11.53%             | -24.50% |     0.39 | 48.25%     | ok               |
| TRX-USD    |       72 | 0.38%    | 44.17%             | -22.90% |     0.1  | 48.85%     | ok               |
| TSLA       |       68 | -8.45%   | 117.04%            | -57.89% |     0.12 | 42.76%     | ok               |
| TXN        |       73 | -12.13%  | 80.31%             | -46.98% |    -0.04 | 54.08%     | ok               |
| UNH        |       76 | 20.56%   | -19.03%            | -27.46% |     0.42 | 52.08%     | ok               |
| UNI-USD    |       90 | -71.33%  | -74.90%            | -81.03% |    -0.85 | 41.19%     | ok               |
| UPS        |       66 | -37.28%  | -34.17%            | -40.62% |    -0.74 | 39.93%     | ok               |
| USO        |       68 | 2.80%    | 58.15%             | -43.35% |     0.17 | 34.44%     | ok               |
| VEA        |       58 | -0.98%   | 52.45%             | -17.93% |     0.01 | 44.09%     | ok               |
| VIXY       |       94 | -78.97%  | -61.10%            | -87.58% |    -0.97 | 31.95%     | ok               |
| VNQ        |       75 | -16.77%  | 12.24%             | -24.92% |    -0.7  | 37.60%     | ok               |
| VTI        |       66 | -0.72%   | 50.94%             | -18.77% |     0.04 | 52.08%     | ok               |
| VWO        |       76 | -13.41%  | 48.97%             | -25.20% |    -0.47 | 44.09%     | ok               |
| VZ         |       85 | -27.35%  | 8.39%              | -31.88% |    -0.95 | 38.10%     | ok               |
| WFC        |       86 | -18.64%  | 68.02%             | -29.91% |    -0.33 | 47.75%     | ok               |
| WIF-USD    |       72 | -39.70%  | -88.67%            | -50.54% |    -0.17 | 32.57%     | ok               |
| WMT        |       57 | 28.98%   | 117.63%            | -21.31% |     0.78 | 51.91%     | ok               |
| XBI        |       62 | -4.13%   | 57.50%             | -21.75% |    -0.02 | 39.43%     | ok               |
| XLB        |       70 | -14.85%  | 26.14%             | -26.57% |    -0.51 | 37.60%     | ok               |
| XLC        |       65 | 15.90%   | 41.03%             | -12.33% |     0.55 | 55.57%     | ok               |
| XLE        |       71 | -9.48%   | 30.74%             | -36.18% |    -0.17 | 46.59%     | ok               |
| XLF        |       76 | -11.92%  | 40.35%             | -23.61% |    -0.39 | 48.42%     | ok               |
| XLI        |       64 | 4.74%    | 58.08%             | -11.38% |     0.24 | 46.59%     | ok               |
| XLK        |       42 | 62.81%   | 82.07%             | -14.75% |     1.17 | 48.42%     | ok               |
| XLM-USD    |       71 | 29.68%   | -41.80%            | -45.54% |     0.5  | 45.79%     | ok               |
| XLP        |       70 | 6.70%    | 15.77%             | -11.16% |     0.41 | 42.76%     | ok               |
| XLU        |       69 | -4.57%   | 45.70%             | -18.15% |    -0.17 | 38.60%     | ok               |
| XLV        |       68 | -10.43%  | 8.83%              | -16.81% |    -0.5  | 36.44%     | ok               |
| XLY        |       74 | 0.76%    | 35.16%             | -14.01% |     0.09 | 44.59%     | ok               |
| XOM        |       56 | 4.30%    | 37.80%             | -20.29% |     0.19 | 36.11%     | ok               |
| XRP-USD    |       62 | -36.21%  | -52.88%            | -48.42% |    -0.36 | 35.82%     | ok               |
| YFI-USD    |       81 | -53.87%  | -75.07%            | -67.78% |    -0.79 | 40.42%     | ok               |
| ZEC-USD    |       69 | 41.84%   | 900.91%            | -46.93% |     0.55 | 36.59%     | ok               |

## AAPL Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 22.28%   | 52.42%             | -21.71% |     0.51 |       67 | 52.75%     | ok               |
|          25 | 16.44%   | 52.42%             | -20.03% |     0.42 |       65 | 50.58%     | ok               |
|          15 | 15.05%   | 52.42%             | -23.86% |     0.38 |       76 | 60.23%     | ok               |
|          30 | 12.73%   | 52.42%             | -20.65% |     0.35 |       63 | 48.59%     | ok               |
|          35 | 7.12%    | 52.42%             | -22.04% |     0.25 |       63 | 46.26%     | ok               |

## AAVE-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 5.38%    | -74.38%            | -46.87% |     0.27 |       38 | 26.05%     | ok               |
|          40 | -0.24%   | -74.38%            | -43.61% |     0.21 |       38 | 29.69%     | ok               |
|          35 | -24.98%  | -74.38%            | -51.96% |    -0.1  |       52 | 32.38%     | ok               |
|          50 | -29.70%  | -74.38%            | -47.78% |    -0.27 |       42 | 20.31%     | ok               |
|          15 | -61.40%  | -74.38%            | -65.37% |    -0.53 |       82 | 50.38%     | ok               |

## ABBV Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 1.73%    | 33.97%             | -23.85% |     0.13 |       50 | 38.27%     | ok               |
|          40 | -10.94%  | 33.97%             | -26.61% |    -0.2  |       64 | 43.09%     | ok               |
|          35 | -12.21%  | 33.97%             | -27.83% |    -0.23 |       66 | 45.92%     | ok               |
|          30 | -14.48%  | 33.97%             | -30.55% |    -0.27 |       64 | 48.75%     | ok               |
|          45 | -13.71%  | 33.97%             | -29.59% |    -0.28 |       54 | 40.43%     | ok               |

## ADA-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -81.97%  | -82.23%            | -91.37% |    -0.51 |       80 | 61.49%     | ok               |
|          20 | -81.85%  | -82.23%            | -91.89% |    -0.53 |       84 | 56.51%     | ok               |
|          50 | -78.05%  | -82.23%            | -86.04% |    -0.6  |       55 | 27.01%     | ok               |
|          25 | -83.13%  | -82.23%            | -91.94% |    -0.6  |       83 | 53.26%     | ok               |
|          45 | -80.39%  | -82.23%            | -88.08% |    -0.63 |       58 | 31.80%     | ok               |

## ADBE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 10.43%   | -68.47%            | -21.34% |     0.29 |       76 | 49.08%     | ok               |
|          40 | -3.82%   | -68.47%            | -20.88% |     0.05 |       72 | 42.10%     | ok               |
|          25 | -9.26%   | -68.47%            | -32.72% |     0.01 |       50 | 61.06%     | ok               |
|          15 | -18.75%  | -68.47%            | -33.11% |    -0.14 |       59 | 65.89%     | ok               |
|          20 | -20.53%  | -68.47%            | -35.78% |    -0.17 |       50 | 63.23%     | ok               |

## AGG Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -6.61%   | 0.44%              | -10.16% |    -1.1  |       69 | 31.11%     | ok               |
|          45 | -5.75%   | 0.44%              | -7.89%  |    -1.16 |       52 | 20.47%     | ok               |
|          20 | -8.00%   | 0.44%              | -10.96% |    -1.18 |       73 | 36.61%     | ok               |
|          50 | -5.57%   | 0.44%              | -7.92%  |    -1.25 |       46 | 16.97%     | ok               |
|          25 | -8.17%   | 0.44%              | -11.60% |    -1.25 |       73 | 34.94%     | ok               |

## ALGO-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -50.43%  | -71.28%            | -53.13% |    -0.57 |       86 | 38.12%     | ok               |
|          15 | -59.02%  | -71.28%            | -69.47% |    -0.61 |       82 | 49.81%     | ok               |
|          25 | -61.32%  | -71.28%            | -73.33% |    -0.72 |       88 | 45.21%     | ok               |
|          20 | -63.36%  | -71.28%            | -72.09% |    -0.74 |       86 | 47.70%     | ok               |
|          50 | -45.64%  | -71.28%            | -48.43% |    -0.81 |       42 | 16.86%     | ok               |

## AMAT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -5.19%   | 243.46%            | -54.05% |     0.12 |       66 | 62.06%     | ok               |
|          30 | -20.65%  | 243.46%            | -57.21% |    -0.12 |       69 | 53.41%     | ok               |
|          20 | -26.45%  | 243.46%            | -60.16% |    -0.19 |       72 | 58.57%     | ok               |
|          35 | -26.30%  | 243.46%            | -55.26% |    -0.23 |       71 | 51.25%     | ok               |
|          50 | -24.43%  | 243.46%            | -48.72% |    -0.24 |       52 | 39.27%     | ok               |

## AMD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -0.51%   | 184.19%            | -46.42% |     0.21 |       56 | 38.10%     | ok               |
|          50 | -2.26%   | 184.19%            | -48.07% |     0.18 |       60 | 32.45%     | ok               |
|          35 | -13.19%  | 184.19%            | -54.16% |     0.08 |       62 | 40.10%     | ok               |
|          45 | -20.51%  | 184.19%            | -55.61% |    -0.03 |       64 | 35.44%     | ok               |
|          30 | -24.64%  | 184.19%            | -59.51% |    -0.05 |       63 | 42.60%     | ok               |

## AMGN Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -13.98%  | 10.12%             | -26.64% |    -0.21 |       72 | 53.91%     | ok               |
|          15 | -17.02%  | 10.12%             | -27.92% |    -0.27 |       70 | 59.57%     | ok               |
|          35 | -16.77%  | 10.12%             | -31.23% |    -0.31 |       69 | 44.26%     | ok               |
|          30 | -19.54%  | 10.12%             | -34.14% |    -0.38 |       71 | 47.92%     | ok               |
|          25 | -22.81%  | 10.12%             | -33.41% |    -0.46 |       67 | 50.25%     | ok               |

## AMZN Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -17.83%  | 50.55%             | -28.70% |    -0.52 |       50 | 29.78%     | ok               |
|          50 | -25.03%  | 50.55%             | -35.48% |    -0.88 |       48 | 24.13%     | ok               |
|          45 | -25.89%  | 50.55%             | -35.47% |    -0.89 |       50 | 26.96%     | ok               |
|          35 | -29.70%  | 50.55%             | -38.29% |    -0.91 |       62 | 32.95%     | ok               |
|          30 | -33.84%  | 50.55%             | -42.48% |    -0.99 |       74 | 38.27%     | ok               |

## APT-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 51.21%   | -92.01%            | -46.73% |     0.73 |       44 | 20.69%     | ok               |
|          45 | 14.97%   | -92.01%            | -63.86% |     0.37 |       60 | 26.82%     | ok               |
|          40 | -7.11%   | -92.01%            | -63.33% |     0.16 |       66 | 32.38%     | ok               |
|          35 | -13.92%  | -92.01%            | -64.45% |     0.11 |       70 | 38.12%     | ok               |
|          20 | -19.17%  | -92.01%            | -70.51% |     0.1  |       71 | 51.92%     | ok               |

## ARB-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 56.87%   | -87.60%            | -53.74% |     0.65 |       83 | 55.94%     | ok               |
|          40 | 45.76%   | -87.60%            | -47.60% |     0.62 |       50 | 30.27%     | ok               |
|          35 | 31.50%   | -87.60%            | -56.00% |     0.51 |       60 | 33.72%     | ok               |
|          20 | 31.11%   | -87.60%            | -60.40% |     0.51 |       73 | 50.00%     | ok               |
|          45 | 24.86%   | -87.60%            | -50.83% |     0.46 |       56 | 23.37%     | ok               |

## ARKK Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -26.33%  | 71.30%             | -34.90% |    -0.32 |       92 | 50.42%     | ok               |
|          20 | -30.68%  | 71.30%             | -34.90% |    -0.44 |       87 | 45.76%     | ok               |
|          30 | -32.67%  | 71.30%             | -35.19% |    -0.57 |       81 | 38.94%     | ok               |
|          35 | -33.82%  | 71.30%             | -36.30% |    -0.63 |       80 | 36.61%     | ok               |
|          40 | -35.22%  | 71.30%             | -36.71% |    -0.71 |       72 | 31.78%     | ok               |

## ATOM-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -64.93%  | -70.01%            | -71.10% |    -0.95 |       93 | 50.96%     | ok               |
|          15 | -69.45%  | -70.01%            | -72.76% |    -1.01 |       93 | 60.73%     | ok               |
|          45 | -59.16%  | -70.01%            | -64.98% |    -1.09 |       72 | 28.35%     | ok               |
|          30 | -67.61%  | -70.01%            | -73.59% |    -1.11 |       88 | 44.25%     | ok               |
|          20 | -72.28%  | -70.01%            | -75.03% |    -1.16 |      101 | 54.79%     | ok               |

## AVAX-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 23.77%   | -80.78%            | -29.53% |     0.47 |       34 | 19.16%     | ok               |
|          45 | 18.70%   | -80.78%            | -32.82% |     0.41 |       34 | 22.99%     | ok               |
|          40 | 18.66%   | -80.78%            | -32.96% |     0.41 |       40 | 25.86%     | ok               |
|          35 | 10.11%   | -80.78%            | -36.30% |     0.32 |       58 | 31.23%     | ok               |
|          15 | 3.57%    | -80.78%            | -52.46% |     0.28 |       61 | 52.49%     | ok               |

## AVGO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 29.51%   | 219.43%            | -35.76% |     0.48 |       60 | 45.42%     | ok               |
|          25 | 24.91%   | 219.43%            | -38.01% |     0.44 |       64 | 46.09%     | ok               |
|          35 | 20.70%   | 219.43%            | -36.19% |     0.4  |       70 | 42.76%     | ok               |
|          40 | 20.29%   | 219.43%            | -40.70% |     0.39 |       60 | 39.60%     | ok               |
|          50 | 14.35%   | 219.43%            | -35.84% |     0.33 |       62 | 33.44%     | ok               |

## BA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 25.12%   | 11.76%             | -13.34% |     0.65 |       44 | 31.78%     | ok               |
|          35 | 24.99%   | 11.76%             | -23.77% |     0.51 |       74 | 45.42%     | ok               |
|          40 | 13.01%   | 11.76%             | -23.87% |     0.35 |       50 | 39.27%     | ok               |
|          25 | 6.17%    | 11.76%             | -32.48% |     0.23 |       72 | 53.58%     | ok               |
|          30 | 3.09%    | 11.76%             | -30.56% |     0.18 |       69 | 50.08%     | ok               |

## BAC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -5.36%   | 69.30%             | -21.23% |    -0.11 |       62 | 35.27%     | ok               |
|          20 | -8.93%   | 69.30%             | -21.48% |    -0.14 |       80 | 51.41%     | ok               |
|          50 | -6.90%   | 69.30%             | -19.75% |    -0.18 |       60 | 32.11%     | ok               |
|          35 | -10.03%  | 69.30%             | -29.13% |    -0.23 |       70 | 42.93%     | ok               |
|          15 | -14.05%  | 69.30%             | -23.70% |    -0.26 |       80 | 56.41%     | ok               |

## BCH-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 6.07%    | -50.07%            | -45.63% |     0.29 |       69 | 53.26%     | ok               |
|          15 | -6.06%   | -50.07%            | -48.75% |     0.17 |       78 | 57.85%     | ok               |
|          25 | -6.40%   | -50.07%            | -51.09% |     0.14 |       70 | 49.23%     | ok               |
|          30 | -5.72%   | -50.07%            | -53.87% |     0.14 |       76 | 47.13%     | ok               |
|          40 | -23.59%  | -50.07%            | -60.69% |    -0.13 |       65 | 40.04%     | ok               |

## BITO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 18.79%   | -54.58%            | -32.29% |     0.39 |       54 | 25.79%     | ok               |
|          30 | 4.89%    | -54.58%            | -42.82% |     0.23 |       78 | 40.43%     | ok               |
|          15 | -1.52%   | -54.58%            | -48.29% |     0.19 |       87 | 49.42%     | ok               |
|          45 | -0.93%   | -54.58%            | -43.53% |     0.15 |       58 | 28.79%     | ok               |
|          25 | -3.41%   | -54.58%            | -41.73% |     0.14 |       82 | 43.43%     | ok               |

## BLK Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 0.48%    | 33.77%             | -14.93% |     0.08 |       82 | 38.94%     | ok               |
|          40 | -1.40%   | 33.77%             | -16.72% |     0.02 |       72 | 34.61%     | ok               |
|          20 | -4.88%   | 33.77%             | -18.60% |    -0.06 |       79 | 46.92%     | ok               |
|          30 | -5.83%   | 33.77%             | -21.49% |    -0.11 |       75 | 42.76%     | ok               |
|          25 | -6.78%   | 33.77%             | -20.53% |    -0.13 |       75 | 45.09%     | ok               |

## BND Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -6.17%   | 0.45%              | -9.05%  |    -0.9  |       63 | 38.10%     | ok               |
|          25 | -6.87%   | 0.45%              | -10.14% |    -1.05 |       67 | 36.11%     | ok               |
|          30 | -7.32%   | 0.45%              | -9.89%  |    -1.18 |       65 | 32.28%     | ok               |
|          15 | -8.39%   | 0.45%              | -10.58% |    -1.21 |       73 | 40.93%     | ok               |
|          45 | -7.56%   | 0.45%              | -9.57%  |    -1.47 |       50 | 21.96%     | ok               |

## BONK-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 170.82%  | -82.13%            | -35.57% |     1.24 |       46 | 22.22%     | ok               |
|          25 | 186.54%  | -82.13%            | -46.61% |     1.08 |       65 | 48.28%     | ok               |
|          20 | 170.36%  | -82.13%            | -54.25% |     1.03 |       66 | 52.87%     | ok               |
|          15 | 167.34%  | -82.13%            | -62.48% |     0.99 |       69 | 57.66%     | ok               |
|          45 | 85.55%   | -82.13%            | -42.36% |     0.84 |       56 | 27.01%     | ok               |

## BTC-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 51.83%   | -31.61%            | -14.50% |     0.95 |       44 | 34.10%     | ok               |
|          45 | 41.09%   | -31.61%            | -15.18% |     0.81 |       44 | 30.65%     | ok               |
|          35 | 36.01%   | -31.61%            | -22.12% |     0.7  |       68 | 41.00%     | ok               |
|          30 | 17.30%   | -31.61%            | -21.75% |     0.41 |       70 | 47.51%     | ok               |
|          50 | 14.18%   | -31.61%            | -16.15% |     0.4  |       42 | 25.29%     | ok               |

## C Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -5.95%   | 167.60%            | -22.28% |    -0.09 |       66 | 35.44%     | ok               |
|          45 | -13.10%  | 167.60%            | -28.12% |    -0.28 |       80 | 39.60%     | ok               |
|          25 | -20.40%  | 167.60%            | -34.18% |    -0.35 |       75 | 52.58%     | ok               |
|          15 | -22.42%  | 167.60%            | -35.02% |    -0.37 |       76 | 59.23%     | ok               |
|          20 | -23.07%  | 167.60%            | -35.56% |    -0.4  |       83 | 55.57%     | ok               |

## CAT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 34.32%   | 217.82%            | -21.02% |     0.62 |       70 | 56.74%     | ok               |
|          25 | 34.44%   | 217.82%            | -26.37% |     0.62 |       66 | 59.57%     | ok               |
|          20 | 31.72%   | 217.82%            | -25.65% |     0.58 |       76 | 62.90%     | ok               |
|          45 | 22.72%   | 217.82%            | -28.85% |     0.49 |       56 | 45.59%     | ok               |
|          15 | 21.50%   | 217.82%            | -30.60% |     0.44 |       69 | 68.89%     | ok               |

## CL Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 17.81%   | 11.52%             | -12.98% |     0.72 |       42 | 32.11%     | ok               |
|          30 | 17.30%   | 11.52%             | -14.32% |     0.59 |       60 | 48.09%     | ok               |
|          45 | 12.42%   | 11.52%             | -13.51% |     0.51 |       46 | 35.11%     | ok               |
|          35 | 11.72%   | 11.52%             | -13.83% |     0.44 |       62 | 44.43%     | ok               |
|          40 | 8.48%    | 11.52%             | -12.70% |     0.36 |       56 | 39.10%     | ok               |

## CMCSA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -35.07%  | -46.52%            | -50.07% |    -0.77 |       88 | 58.74%     | ok               |
|          30 | -39.47%  | -46.52%            | -41.34% |    -1.03 |       80 | 44.09%     | ok               |
|          50 | -31.32%  | -46.52%            | -33.45% |    -1.19 |       52 | 16.97%     | ok               |
|          25 | -44.61%  | -46.52%            | -46.32% |    -1.19 |       88 | 49.58%     | ok               |
|          20 | -46.20%  | -46.52%            | -48.31% |    -1.22 |       92 | 54.74%     | ok               |

## COMP-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -1.28%   | -75.98%            | -38.71% |     0.18 |       46 | 20.50%     | ok               |
|          25 | -37.88%  | -75.98%            | -60.58% |    -0.19 |       87 | 50.00%     | ok               |
|          30 | -36.73%  | -75.98%            | -58.43% |    -0.21 |       89 | 45.02%     | ok               |
|          15 | -46.13%  | -75.98%            | -65.55% |    -0.28 |      101 | 61.49%     | ok               |
|          40 | -39.60%  | -75.98%            | -46.99% |    -0.35 |       74 | 32.95%     | ok               |

## COP Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -9.77%   | -0.75%             | -34.21% |    -0.15 |       48 | 27.29%     | ok               |
|          45 | -15.67%  | -0.75%             | -40.57% |    -0.3  |       58 | 30.12%     | ok               |
|          35 | -23.70%  | -0.75%             | -43.58% |    -0.45 |       75 | 37.10%     | ok               |
|          30 | -24.21%  | -0.75%             | -43.77% |    -0.45 |       73 | 40.27%     | ok               |
|          40 | -26.23%  | -0.75%             | -46.34% |    -0.57 |       68 | 32.78%     | ok               |

## COST Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | 18.65%   | 42.02%             | -24.73% |     0.56 |       61 | 50.25%     | ok               |
|          20 | 18.04%   | 42.02%             | -24.32% |     0.54 |       62 | 52.75%     | ok               |
|          35 | 11.83%   | 42.02%             | -26.58% |     0.41 |       54 | 43.76%     | ok               |
|          30 | 6.71%    | 42.02%             | -29.73% |     0.26 |       60 | 46.76%     | ok               |
|          40 | 4.97%    | 42.02%             | -28.41% |     0.22 |       56 | 40.77%     | ok               |

## CRM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -30.57%  | -44.44%            | -38.20% |    -0.45 |       90 | 55.41%     | ok               |
|          35 | -25.17%  | -44.44%            | -36.98% |    -0.48 |       64 | 39.10%     | ok               |
|          40 | -30.31%  | -44.44%            | -41.30% |    -0.68 |       68 | 34.94%     | ok               |
|          30 | -35.73%  | -44.44%            | -41.69% |    -0.73 |       67 | 43.93%     | ok               |
|          20 | -40.81%  | -44.44%            | -43.08% |    -0.76 |       78 | 49.08%     | ok               |

## CRV-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 12.00%   | -72.13%            | -29.30% |     0.33 |       40 | 16.67%     | ok               |
|          35 | 10.27%   | -72.13%            | -37.78% |     0.33 |       66 | 29.89%     | ok               |
|          45 | 6.52%    | -72.13%            | -42.29% |     0.27 |       52 | 19.54%     | ok               |
|          40 | -0.06%   | -72.13%            | -38.86% |     0.2  |       56 | 25.67%     | ok               |
|          30 | -12.43%  | -72.13%            | -39.89% |     0.1  |       64 | 34.48%     | ok               |

## CSCO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 28.18%   | 124.21%            | -19.34% |     0.63 |       58 | 38.94%     | ok               |
|          45 | 26.53%   | 124.21%            | -19.34% |     0.59 |       51 | 41.43%     | ok               |
|          25 | 22.47%   | 124.21%            | -23.28% |     0.49 |       63 | 52.41%     | ok               |
|          35 | 21.85%   | 124.21%            | -23.68% |     0.49 |       51 | 47.92%     | ok               |
|          30 | 21.90%   | 124.21%            | -21.79% |     0.49 |       59 | 50.42%     | ok               |

## CVX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -12.66%  | 19.53%             | -24.98% |    -0.28 |       73 | 44.26%     | ok               |
|          20 | -13.07%  | 19.53%             | -26.07% |    -0.29 |       71 | 45.26%     | ok               |
|          30 | -14.77%  | 19.53%             | -26.75% |    -0.37 |       69 | 41.43%     | ok               |
|          35 | -14.52%  | 19.53%             | -27.83% |    -0.37 |       69 | 38.44%     | ok               |
|          45 | -13.32%  | 19.53%             | -28.32% |    -0.38 |       59 | 30.12%     | ok               |

## DASH-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 110.90%  | 3.47%              | -31.38% |     0.88 |       42 | 17.24%     | ok               |
|          40 | 56.83%   | 3.47%              | -34.44% |     0.63 |       48 | 23.95%     | ok               |
|          45 | 52.31%   | 3.47%              | -39.58% |     0.61 |       46 | 19.54%     | ok               |
|          25 | -41.06%  | 3.47%              | -64.14% |     0.01 |       73 | 34.87%     | ok               |
|          35 | -40.88%  | 3.47%              | -63.23% |    -0    |       73 | 28.54%     | ok               |

## DBC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -7.91%   | 23.10%             | -19.36% |    -0.29 |       42 | 20.97%     | ok               |
|          35 | -9.68%   | 23.10%             | -23.38% |    -0.31 |       60 | 31.61%     | ok               |
|          45 | -9.28%   | 23.10%             | -20.53% |    -0.32 |       54 | 24.29%     | ok               |
|          15 | -10.81%  | 23.10%             | -27.30% |    -0.34 |       67 | 37.10%     | ok               |
|          30 | -12.57%  | 23.10%             | -25.35% |    -0.43 |       58 | 32.78%     | ok               |

## DE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -5.78%   | 49.73%             | -28.94% |    -0.03 |       72 | 51.25%     | ok               |
|          30 | -6.65%   | 49.73%             | -25.24% |    -0.05 |       72 | 45.92%     | ok               |
|          25 | -8.11%   | 49.73%             | -26.67% |    -0.09 |       74 | 48.59%     | ok               |
|          50 | -9.41%   | 49.73%             | -24.35% |    -0.19 |       70 | 30.62%     | ok               |
|          15 | -14.06%  | 49.73%             | -27.41% |    -0.21 |       78 | 54.58%     | ok               |

## DIA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | -0.36%   | 35.70%             | -13.15% |     0.02 |       60 | 43.76%     | ok               |
|          25 | -0.90%   | 35.70%             | -11.28% |    -0.01 |       60 | 47.09%     | ok               |
|          30 | -2.42%   | 35.70%             | -12.94% |    -0.09 |       60 | 45.92%     | ok               |
|          20 | -4.29%   | 35.70%             | -13.85% |    -0.18 |       64 | 49.42%     | ok               |
|          40 | -4.42%   | 35.70%             | -15.06% |    -0.22 |       66 | 40.93%     | ok               |

## DIS Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 35.94%   | 6.33%              | -14.24% |     0.88 |       50 | 30.78%     | ok               |
|          45 | 7.43%    | 6.33%              | -16.54% |     0.25 |       51 | 34.28%     | ok               |
|          40 | 5.75%    | 6.33%              | -23.29% |     0.22 |       63 | 39.60%     | ok               |
|          35 | -1.07%   | 6.33%              | -23.26% |     0.08 |       71 | 45.26%     | ok               |
|          15 | -2.41%   | 6.33%              | -27.62% |     0.07 |       86 | 59.23%     | ok               |

## DOGE-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 18.72%   | -74.51%            | -57.89% |     0.43 |       79 | 64.94%     | ok               |
|          20 | 4.42%    | -74.51%            | -55.83% |     0.31 |       82 | 60.34%     | ok               |
|          25 | 0.09%    | -74.51%            | -53.72% |     0.27 |       72 | 54.98%     | ok               |
|          30 | -16.53%  | -74.51%            | -60.95% |     0.09 |       75 | 49.81%     | ok               |
|          35 | -45.34%  | -74.51%            | -63.16% |    -0.38 |       72 | 43.10%     | ok               |

## DOT-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -19.10%  | -84.24%            | -44.94% |    -0.11 |       56 | 26.25%     | ok               |
|          45 | -27.53%  | -84.24%            | -52.30% |    -0.22 |       50 | 30.84%     | ok               |
|          40 | -35.47%  | -84.24%            | -52.19% |    -0.32 |       56 | 34.29%     | ok               |
|          30 | -47.22%  | -84.24%            | -61.09% |    -0.35 |       90 | 48.08%     | ok               |
|          35 | -46.19%  | -84.24%            | -62.63% |    -0.36 |       80 | 41.38%     | ok               |

## DXY-INDEX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -2.63%   | -1.61%             | -9.99%  |    -0.27 |       68 | 58.57%     | ok               |
|          35 | -2.69%   | -1.61%             | -9.23%  |    -0.3  |       69 | 53.80%     | ok               |
|          40 | -2.77%   | -1.61%             | -7.30%  |    -0.34 |       68 | 47.51%     | ok               |
|          15 | -4.43%   | -1.61%             | -11.63% |    -0.39 |       90 | 75.70%     | ok               |
|          50 | -3.31%   | -1.61%             | -6.06%  |    -0.52 |       44 | 29.07%     | ok               |

## EEM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -2.91%   | 76.43%             | -15.88% |    -0.04 |       50 | 36.11%     | ok               |
|          45 | -4.62%   | 76.43%             | -17.36% |    -0.11 |       52 | 37.60%     | ok               |
|          40 | -4.96%   | 76.43%             | -19.52% |    -0.11 |       64 | 39.77%     | ok               |
|          35 | -5.62%   | 76.43%             | -23.88% |    -0.12 |       66 | 41.76%     | ok               |
|          30 | -9.40%   | 76.43%             | -25.67% |    -0.25 |       64 | 43.43%     | ok               |

## EFA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -1.25%   | 38.89%             | -10.80% |     0.02 |       58 | 52.08%     | ok               |
|          20 | -8.10%   | 38.89%             | -12.49% |    -0.27 |       65 | 49.08%     | ok               |
|          30 | -8.33%   | 38.89%             | -13.87% |    -0.3  |       58 | 43.93%     | ok               |
|          40 | -9.72%   | 38.89%             | -15.73% |    -0.39 |       62 | 40.10%     | ok               |
|          50 | -9.07%   | 38.89%             | -17.56% |    -0.4  |       54 | 36.27%     | ok               |

## EOG Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -15.90%  | 16.02%             | -38.89% |    -0.35 |       52 | 32.61%     | ok               |
|          50 | -17.13%  | 16.02%             | -37.65% |    -0.41 |       56 | 29.78%     | ok               |
|          40 | -21.40%  | 16.02%             | -40.83% |    -0.51 |       62 | 36.11%     | ok               |
|          35 | -23.01%  | 16.02%             | -44.05% |    -0.53 |       77 | 40.93%     | ok               |
|          30 | -25.23%  | 16.02%             | -48.13% |    -0.55 |       79 | 46.26%     | ok               |

## ETC-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -7.93%   | -69.97%            | -27.89% |    -0.02 |       28 | 17.05%     | ok               |
|          35 | -15.03%  | -69.97%            | -42.62% |    -0.11 |       44 | 27.01%     | ok               |
|          45 | -16.07%  | -69.97%            | -35.44% |    -0.17 |       26 | 18.97%     | ok               |
|          40 | -21.04%  | -69.97%            | -40.48% |    -0.26 |       42 | 22.80%     | ok               |
|          30 | -35.69%  | -69.97%            | -48.16% |    -0.51 |       64 | 31.23%     | ok               |

## ETH-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 157.31%  | -43.97%            | -30.11% |     1.28 |       60 | 44.83%     | ok               |
|          30 | 137.37%  | -43.97%            | -32.89% |     1.14 |       66 | 53.07%     | ok               |
|          40 | 62.72%   | -43.97%            | -33.11% |     0.8  |       56 | 37.36%     | ok               |
|          45 | 34.50%   | -43.97%            | -34.50% |     0.57 |       52 | 33.33%     | ok               |
|          25 | 29.26%   | -43.97%            | -40.90% |     0.5  |       71 | 59.00%     | ok               |

## EWJ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -17.33%  | 43.28%             | -30.73% |    -0.55 |       64 | 40.93%     | ok               |
|          20 | -18.73%  | 43.28%             | -31.32% |    -0.59 |       60 | 42.93%     | ok               |
|          25 | -21.07%  | 43.28%             | -31.18% |    -0.69 |       60 | 41.93%     | ok               |
|          35 | -21.29%  | 43.28%             | -32.54% |    -0.71 |       70 | 39.27%     | ok               |
|          15 | -24.11%  | 43.28%             | -32.24% |    -0.75 |       74 | 46.09%     | ok               |

## FCX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -7.45%   | 75.10%             | -26.57% |     0    |       56 | 29.62%     | ok               |
|          45 | -12.11%  | 75.10%             | -33.82% |    -0.06 |       56 | 33.94%     | ok               |
|          40 | -23.41%  | 75.10%             | -42.89% |    -0.26 |       66 | 39.10%     | ok               |
|          30 | -31.93%  | 75.10%             | -46.84% |    -0.39 |       69 | 45.92%     | ok               |
|          35 | -35.67%  | 75.10%             | -50.12% |    -0.49 |       73 | 43.93%     | ok               |

## FET-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 58.11%   | -83.82%            | -57.24% |     0.66 |       84 | 49.23%     | ok               |
|          15 | 9.94%    | -83.82%            | -59.58% |     0.39 |       82 | 52.49%     | ok               |
|          25 | 3.44%    | -83.82%            | -57.82% |     0.32 |       87 | 42.91%     | ok               |
|          30 | -2.40%   | -83.82%            | -48.39% |     0.26 |       77 | 39.08%     | ok               |
|          35 | -28.11%  | -83.82%            | -58.16% |    -0.06 |       65 | 32.57%     | ok               |

## FIL-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -6.35%   | -83.66%            | -39.40% |     0.09 |       48 | 23.37%     | ok               |
|          35 | -30.36%  | -83.66%            | -45.88% |    -0.27 |       58 | 27.59%     | ok               |
|          45 | -27.58%  | -83.66%            | -43.98% |    -0.29 |       44 | 17.62%     | ok               |
|          30 | -33.66%  | -83.66%            | -49.05% |    -0.29 |       70 | 33.14%     | ok               |
|          50 | -26.52%  | -83.66%            | -44.97% |    -0.32 |       38 | 13.03%     | ok               |

## FXI Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -5.92%   | 47.91%             | -22.99% |    -0.06 |       48 | 29.45%     | ok               |
|          30 | -6.46%   | 47.91%             | -24.33% |    -0.08 |       48 | 28.29%     | ok               |
|          15 | -7.60%   | 47.91%             | -21.68% |    -0.09 |       54 | 32.78%     | ok               |
|          20 | -9.12%   | 47.91%             | -24.94% |    -0.14 |       54 | 30.78%     | ok               |
|          45 | -9.54%   | 47.91%             | -26.75% |    -0.18 |       44 | 22.63%     | ok               |

## GDX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 12.93%   | 198.62%            | -31.87% |     0.33 |       62 | 42.76%     | ok               |
|          20 | 6.04%    | 198.62%            | -35.59% |     0.23 |       75 | 53.08%     | ok               |
|          35 | 5.34%    | 198.62%            | -32.37% |     0.22 |       68 | 45.26%     | ok               |
|          30 | -0.08%   | 198.62%            | -34.99% |     0.13 |       62 | 48.25%     | ok               |
|          45 | -1.99%   | 198.62%            | -32.07% |     0.08 |       58 | 39.43%     | ok               |

## GDXJ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -20.35%  | 219.25%            | -45.05% |    -0.13 |       69 | 53.24%     | ok               |
|          50 | -16.59%  | 219.25%            | -42.44% |    -0.15 |       56 | 37.44%     | ok               |
|          30 | -27.45%  | 219.25%            | -44.93% |    -0.31 |       68 | 46.09%     | ok               |
|          45 | -27.77%  | 219.25%            | -42.73% |    -0.36 |       60 | 39.77%     | ok               |
|          40 | -29.17%  | 219.25%            | -44.27% |    -0.38 |       64 | 41.60%     | ok               |

## GE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 37.00%   | 244.31%            | -22.29% |     0.71 |       66 | 38.94%     | ok               |
|          45 | 26.66%   | 244.31%            | -25.68% |     0.55 |       74 | 41.76%     | ok               |
|          20 | 25.73%   | 244.31%            | -26.63% |     0.5  |       69 | 55.57%     | ok               |
|          35 | 20.08%   | 244.31%            | -27.11% |     0.44 |       80 | 47.09%     | ok               |
|          40 | 19.18%   | 244.31%            | -26.97% |     0.43 |       76 | 43.26%     | ok               |

## GLD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | 28.23%   | 107.65%            | -14.61% |     0.7  |       46 | 45.76%     | ok               |
|          20 | 26.32%   | 107.65%            | -14.61% |     0.66 |       48 | 47.09%     | ok               |
|          30 | 22.12%   | 107.65%            | -16.63% |     0.59 |       48 | 44.59%     | ok               |
|          15 | 18.58%   | 107.65%            | -17.54% |     0.49 |       50 | 51.25%     | ok               |
|          35 | 16.16%   | 107.65%            | -17.29% |     0.46 |       50 | 43.93%     | ok               |

## GOOGL Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | 72.94%   | 139.54%            | -19.76% |     1.09 |       59 | 56.41%     | ok               |
|          30 | 69.02%   | 139.54%            | -20.41% |     1.06 |       63 | 54.08%     | ok               |
|          15 | 63.21%   | 139.54%            | -13.59% |     0.95 |       71 | 64.06%     | ok               |
|          35 | 54.14%   | 139.54%            | -22.85% |     0.94 |       69 | 48.92%     | ok               |
|          20 | 59.88%   | 139.54%            | -20.57% |     0.94 |       70 | 58.74%     | ok               |

## GRT-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 46.24%   | -89.86%            | -30.00% |     0.71 |       40 | 21.07%     | ok               |
|          45 | 13.62%   | -89.86%            | -48.76% |     0.35 |       48 | 26.25%     | ok               |
|          15 | 8.23%    | -89.86%            | -49.67% |     0.33 |       73 | 60.73%     | ok               |
|          20 | 7.63%    | -89.86%            | -46.47% |     0.32 |       81 | 55.75%     | ok               |
|          35 | 9.24%    | -89.86%            | -49.87% |     0.31 |       60 | 35.44%     | ok               |

## GS Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 30.60%   | 187.21%            | -20.56% |     0.61 |       74 | 60.07%     | ok               |
|          20 | 12.78%   | 187.21%            | -23.19% |     0.34 |       74 | 56.07%     | ok               |
|          25 | 7.07%    | 187.21%            | -23.32% |     0.24 |       74 | 53.58%     | ok               |
|          40 | 2.18%    | 187.21%            | -17.88% |     0.14 |       72 | 44.59%     | ok               |
|          30 | 0.77%    | 187.21%            | -22.13% |     0.12 |       76 | 51.25%     | ok               |

## HD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -3.66%   | -6.69%             | -17.69% |    -0.02 |       71 | 43.76%     | ok               |
|          25 | -4.41%   | -6.69%             | -18.51% |    -0.04 |       70 | 45.76%     | ok               |
|          40 | -10.30%  | -6.69%             | -19.63% |    -0.27 |       80 | 33.94%     | ok               |
|          45 | -10.38%  | -6.69%             | -20.74% |    -0.29 |       60 | 28.79%     | ok               |
|          35 | -12.63%  | -6.69%             | -22.98% |    -0.3  |       78 | 40.10%     | ok               |

## HON Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -17.09%  | 19.74%             | -23.31% |    -0.53 |       74 | 32.11%     | ok               |
|          45 | -18.75%  | 19.74%             | -22.07% |    -0.55 |       76 | 37.10%     | ok               |
|          40 | -26.75%  | 19.74%             | -26.75% |    -0.78 |       78 | 41.43%     | ok               |
|          35 | -28.43%  | 19.74%             | -28.43% |    -0.81 |       95 | 47.92%     | ok               |
|          30 | -30.18%  | 19.74%             | -30.77% |    -0.84 |       97 | 52.91%     | ok               |

## HYG Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -7.92%   | 2.63%              | -7.92%  |    -0.96 |       70 | 29.45%     | ok               |
|          15 | -9.71%   | 2.63%              | -10.06% |    -1.05 |       88 | 41.43%     | ok               |
|          20 | -9.69%   | 2.63%              | -10.29% |    -1.08 |       86 | 39.10%     | ok               |
|          45 | -8.60%   | 2.63%              | -8.60%  |    -1.08 |       66 | 26.29%     | ok               |
|          30 | -9.52%   | 2.63%              | -9.59%  |    -1.11 |       81 | 34.28%     | ok               |

## IBIT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 61.66%   | -4.34%             | -19.20% |     1.04 |       38 | 38.44%     | ok               |
|          50 | 49.26%   | -4.34%             | -17.37% |     1.03 |       20 | 22.87%     | ok               |
|          45 | 40.96%   | -4.34%             | -17.37% |     0.88 |       22 | 23.60%     | ok               |
|          40 | 39.57%   | -4.34%             | -17.78% |     0.85 |       24 | 25.06%     | ok               |
|          30 | 33.20%   | -4.34%             | -18.95% |     0.72 |       32 | 30.66%     | ok               |

## IBM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 14.19%   | 37.77%             | -28.20% |     0.35 |       87 | 62.40%     | ok               |
|          30 | 10.19%   | 37.77%             | -25.31% |     0.3  |       72 | 50.58%     | ok               |
|          35 | 7.98%    | 37.77%             | -25.15% |     0.26 |       68 | 46.26%     | ok               |
|          45 | 5.65%    | 37.77%             | -18.33% |     0.22 |       54 | 36.77%     | ok               |
|          40 | 2.50%    | 37.77%             | -24.66% |     0.15 |       64 | 40.77%     | ok               |

## ICP-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 21.03%   | -76.13%            | -32.85% |     0.42 |       58 | 27.01%     | ok               |
|          35 | 9.43%    | -76.13%            | -45.97% |     0.32 |       68 | 32.38%     | ok               |
|          50 | 5.42%    | -76.13%            | -43.65% |     0.25 |       40 | 16.86%     | ok               |
|          30 | -1.35%   | -76.13%            | -55.67% |     0.25 |       83 | 38.70%     | ok               |
|          45 | -8.28%   | -76.13%            | -40.57% |     0.09 |       58 | 21.07%     | ok               |

## IEF Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -6.92%   | -1.17%             | -9.79%  |    -0.82 |       70 | 42.26%     | ok               |
|          15 | -7.48%   | -1.17%             | -10.52% |    -0.88 |       69 | 43.76%     | ok               |
|          40 | -8.39%   | -1.17%             | -9.67%  |    -1.31 |       60 | 24.79%     | ok               |
|          45 | -8.07%   | -1.17%             | -9.73%  |    -1.33 |       50 | 22.80%     | ok               |
|          25 | -10.50%  | -1.17%             | -11.19% |    -1.34 |       76 | 39.43%     | ok               |

## IEMG Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 1.46%    | 69.78%             | -13.87% |     0.11 |       52 | 34.78%     | ok               |
|          45 | 0.63%    | 69.78%             | -14.87% |     0.08 |       48 | 37.27%     | ok               |
|          35 | -0.32%   | 69.78%             | -22.13% |     0.05 |       63 | 42.60%     | ok               |
|          40 | -0.92%   | 69.78%             | -18.39% |     0.03 |       60 | 40.27%     | ok               |
|          25 | -4.72%   | 69.78%             | -25.58% |    -0.09 |       59 | 45.42%     | ok               |

## INJ-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -12.91%  | -72.65%            | -55.31% |     0.02 |       44 | 22.41%     | ok               |
|          35 | -20.16%  | -72.65%            | -61.19% |    -0.01 |       60 | 32.38%     | ok               |
|          50 | -22.38%  | -72.65%            | -51.00% |    -0.14 |       48 | 19.35%     | ok               |
|          40 | -28.35%  | -72.65%            | -58.05% |    -0.17 |       50 | 28.54%     | ok               |
|          20 | -56.26%  | -72.65%            | -81.53% |    -0.46 |       82 | 47.13%     | ok               |

## INTC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 76.11%   | 144.40%            | -49.32% |     0.74 |       60 | 34.28%     | ok               |
|          15 | 82.95%   | 144.40%            | -53.65% |     0.74 |       84 | 61.23%     | ok               |
|          25 | 75.50%   | 144.40%            | -56.41% |     0.72 |       75 | 51.58%     | ok               |
|          40 | 70.33%   | 144.40%            | -55.86% |     0.7  |       68 | 38.60%     | ok               |
|          20 | 72.70%   | 144.40%            | -52.47% |     0.7  |       82 | 56.57%     | ok               |

## INTU Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 2.90%    | -58.05%            | -42.82% |     0.17 |       71 | 29.45%     | ok               |
|          45 | -0.62%   | -58.05%            | -44.66% |     0.11 |       69 | 33.61%     | ok               |
|          40 | -8.06%   | -58.05%            | -48.32% |    -0.03 |       69 | 36.27%     | ok               |
|          25 | -9.36%   | -58.05%            | -42.24% |    -0.03 |       64 | 45.59%     | ok               |
|          15 | -10.44%  | -58.05%            | -46.90% |    -0.04 |       79 | 51.08%     | ok               |

## ITA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 5.19%    | 99.55%             | -21.48% |     0.23 |       76 | 37.10%     | ok               |
|          15 | 1.02%    | 99.55%             | -28.17% |     0.11 |       86 | 58.74%     | ok               |
|          30 | 0.95%    | 99.55%             | -23.75% |     0.1  |       74 | 47.09%     | ok               |
|          35 | -1.65%   | 99.55%             | -23.16% |     0.02 |       78 | 45.26%     | ok               |
|          40 | -2.79%   | 99.55%             | -20.58% |    -0.02 |       80 | 41.76%     | ok               |

## IWM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | 9.46%    | 47.92%             | -14.62% |     0.38 |       52 | 37.60%     | ok               |
|          30 | 9.03%    | 47.92%             | -12.83% |     0.37 |       50 | 36.61%     | ok               |
|          40 | 6.82%    | 47.92%             | -14.38% |     0.32 |       44 | 31.95%     | ok               |
|          35 | 6.57%    | 47.92%             | -14.41% |     0.3  |       50 | 34.28%     | ok               |
|          20 | 5.15%    | 47.92%             | -15.14% |     0.24 |       62 | 38.60%     | ok               |

## JNJ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 21.36%   | 46.78%             | -10.57% |     0.9  |       56 | 37.10%     | ok               |
|          15 | 17.79%   | 46.78%             | -18.02% |     0.62 |       65 | 57.74%     | ok               |
|          45 | 12.26%   | 46.78%             | -13.35% |     0.53 |       58 | 42.26%     | ok               |
|          20 | 13.34%   | 46.78%             | -17.61% |     0.5  |       71 | 54.24%     | ok               |
|          40 | 9.81%    | 46.78%             | -14.77% |     0.42 |       64 | 46.42%     | ok               |

## JPM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 21.04%   | 92.82%             | -15.90% |     0.7  |       54 | 40.27%     | ok               |
|          45 | 9.55%    | 92.82%             | -21.91% |     0.34 |       56 | 43.26%     | ok               |
|          40 | -4.92%   | 92.82%             | -28.47% |    -0.07 |       68 | 45.76%     | ok               |
|          20 | -11.79%  | 92.82%             | -33.59% |    -0.18 |       88 | 57.07%     | ok               |
|          35 | -10.23%  | 92.82%             | -27.43% |    -0.21 |       74 | 49.42%     | ok               |

## KO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 27.92%   | 35.11%             | -8.07%  |     1    |       51 | 37.94%     | ok               |
|          35 | 24.00%   | 35.11%             | -8.07%  |     0.89 |       54 | 36.61%     | ok               |
|          40 | 21.41%   | 35.11%             | -9.28%  |     0.86 |       56 | 33.44%     | ok               |
|          25 | 22.64%   | 35.11%             | -9.37%  |     0.83 |       57 | 40.60%     | ok               |
|          50 | 14.81%   | 35.11%             | -11.40% |     0.68 |       36 | 26.79%     | ok               |

## LDO-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 22.47%   | -82.68%            | -44.97% |     0.46 |       87 | 47.89%     | ok               |
|          15 | 16.20%   | -82.68%            | -46.95% |     0.43 |       84 | 52.68%     | ok               |
|          50 | 15.22%   | -82.68%            | -48.04% |     0.37 |       46 | 16.86%     | ok               |
|          30 | 10.11%   | -82.68%            | -60.93% |     0.36 |       76 | 38.51%     | ok               |
|          25 | -5.90%   | -82.68%            | -56.60% |     0.24 |       83 | 44.06%     | ok               |

## LIN Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 4.87%    | 27.85%             | -23.70% |     0.22 |       63 | 49.75%     | ok               |
|          25 | 3.57%    | 27.85%             | -22.01% |     0.18 |       65 | 41.76%     | ok               |
|          20 | 1.35%    | 27.85%             | -23.00% |     0.11 |       64 | 44.93%     | ok               |
|          35 | -0.17%   | 27.85%             | -21.18% |     0.05 |       64 | 32.45%     | ok               |
|          30 | -0.80%   | 27.85%             | -21.53% |     0.03 |       68 | 38.94%     | ok               |

## LINK-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -13.55%  | -58.15%            | -50.48% |     0.1  |       70 | 41.57%     | ok               |
|          45 | -16.95%  | -58.15%            | -38.56% |    -0    |       50 | 26.25%     | ok               |
|          50 | -16.55%  | -58.15%            | -36.98% |    -0.02 |       40 | 20.88%     | ok               |
|          35 | -27.53%  | -58.15%            | -49.56% |    -0.1  |       60 | 36.40%     | ok               |
|          40 | -31.51%  | -58.15%            | -50.91% |    -0.19 |       56 | 30.65%     | ok               |

## LLY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 28.48%   | 77.18%             | -38.23% |     0.59 |       42 | 39.27%     | ok               |
|          45 | 16.16%   | 77.18%             | -42.66% |     0.39 |       50 | 42.43%     | ok               |
|          15 | 9.54%    | 77.18%             | -48.12% |     0.28 |       63 | 61.90%     | ok               |
|          40 | -1.22%   | 77.18%             | -46.23% |     0.1  |       62 | 44.93%     | ok               |
|          20 | -8.10%   | 77.18%             | -51.34% |     0.01 |       72 | 56.91%     | ok               |

## LRCX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 3.69%    | 332.28%            | -60.45% |     0.23 |       83 | 55.57%     | ok               |
|          50 | -2.28%   | 332.28%            | -50.39% |     0.12 |       80 | 37.44%     | ok               |
|          40 | -5.21%   | 332.28%            | -56.86% |     0.1  |       72 | 43.26%     | ok               |
|          35 | -11.36%  | 332.28%            | -61.76% |     0.02 |       80 | 45.26%     | ok               |
|          20 | -13.93%  | 332.28%            | -67.64% |     0    |       87 | 51.25%     | ok               |

## LTC-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -12.22%  | -54.31%            | -44.78% |    -0    |       56 | 31.80%     | ok               |
|          35 | -22.47%  | -54.31%            | -54.86% |    -0.13 |       66 | 42.91%     | ok               |
|          30 | -34.00%  | -54.31%            | -53.76% |    -0.29 |       66 | 48.47%     | ok               |
|          40 | -31.40%  | -54.31%            | -56.10% |    -0.3  |       58 | 38.12%     | ok               |
|          25 | -36.79%  | -54.31%            | -54.26% |    -0.33 |       74 | 50.96%     | ok               |

## MCD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 3.90%    | -4.51%             | -9.22%  |     0.24 |       42 | 20.63%     | ok               |
|          30 | -2.55%   | -4.51%             | -18.81% |    -0.05 |       75 | 38.10%     | ok               |
|          25 | -3.59%   | -4.51%             | -20.47% |    -0.09 |       75 | 40.77%     | ok               |
|          40 | -6.63%   | -4.51%             | -16.86% |    -0.26 |       69 | 28.95%     | ok               |
|          35 | -7.68%   | -4.51%             | -15.45% |    -0.29 |       67 | 34.44%     | ok               |

## META Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 9.25%    | 44.36%             | -31.03% |     0.27 |       66 | 40.27%     | ok               |
|          40 | -2.76%   | 44.36%             | -35.11% |     0.08 |       66 | 43.26%     | ok               |
|          50 | -7.43%   | 44.36%             | -34.00% |    -0.01 |       70 | 36.44%     | ok               |
|          25 | -12.36%  | 44.36%             | -39.84% |    -0.06 |       67 | 53.91%     | ok               |
|          35 | -13.92%  | 44.36%             | -34.87% |    -0.11 |       77 | 48.09%     | ok               |

## MPC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 14.51%   | 55.54%             | -23.96% |     0.37 |       52 | 38.60%     | ok               |
|          45 | 7.25%    | 55.54%             | -25.09% |     0.24 |       58 | 42.26%     | ok               |
|          40 | 5.62%    | 55.54%             | -25.70% |     0.22 |       60 | 44.59%     | ok               |
|          35 | 2.36%    | 55.54%             | -35.90% |     0.16 |       68 | 47.09%     | ok               |
|          30 | -13.74%  | 55.54%             | -44.76% |    -0.14 |       71 | 49.92%     | ok               |

## MRK Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -17.07%  | -3.90%             | -30.12% |    -0.28 |       87 | 57.74%     | ok               |
|          25 | -16.67%  | -3.90%             | -31.07% |    -0.3  |       72 | 49.75%     | ok               |
|          20 | -20.76%  | -3.90%             | -29.59% |    -0.4  |       77 | 53.08%     | ok               |
|          45 | -19.63%  | -3.90%             | -26.02% |    -0.48 |       57 | 35.94%     | ok               |
|          50 | -18.73%  | -3.90%             | -25.69% |    -0.49 |       58 | 32.78%     | ok               |

## MS Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 0.72%    | 155.58%            | -19.99% |     0.1  |       70 | 39.93%     | ok               |
|          35 | -6.36%   | 155.58%            | -25.26% |    -0.08 |       76 | 44.59%     | ok               |
|          15 | -10.72%  | 155.58%            | -24.02% |    -0.15 |       82 | 56.91%     | ok               |
|          20 | -11.21%  | 155.58%            | -25.68% |    -0.18 |       84 | 52.91%     | ok               |
|          30 | -12.90%  | 155.58%            | -27.79% |    -0.25 |       81 | 48.25%     | ok               |

## MSFT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -17.91%  | -6.41%             | -25.28% |    -0.5  |       62 | 35.11%     | ok               |
|          50 | -22.49%  | -6.41%             | -28.69% |    -0.69 |       60 | 30.62%     | ok               |
|          35 | -29.69%  | -6.41%             | -32.79% |    -0.79 |       71 | 43.43%     | ok               |
|          40 | -30.52%  | -6.41%             | -33.59% |    -0.86 |       67 | 38.44%     | ok               |
|          25 | -34.00%  | -6.41%             | -37.59% |    -0.88 |       85 | 51.25%     | ok               |

## MU Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 380.03%  | 1069.50%           | -61.96% |     1.49 |       48 | 67.89%     | ok               |
|          25 | 299.92%  | 1069.50%           | -67.90% |     1.4  |       49 | 61.56%     | ok               |
|          40 | 257.28%  | 1069.50%           | -64.30% |     1.33 |       56 | 54.91%     | ok               |
|          20 | 266.14%  | 1069.50%           | -67.25% |     1.31 |       55 | 63.73%     | ok               |
|          30 | 240.66%  | 1069.50%           | -68.76% |     1.28 |       51 | 59.73%     | ok               |

## NEAR-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 99.44%   | -53.19%            | -48.95% |     0.97 |       44 | 23.18%     | ok               |
|          50 | 70.90%   | -53.19%            | -53.13% |     0.82 |       38 | 18.39%     | ok               |
|          40 | 57.99%   | -53.19%            | -57.15% |     0.71 |       48 | 27.59%     | ok               |
|          35 | 31.48%   | -53.19%            | -61.02% |     0.51 |       70 | 32.95%     | ok               |
|          15 | 14.09%   | -53.19%            | -54.94% |     0.41 |       89 | 56.51%     | ok               |

## NEM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 19.64%   | 206.38%            | -28.11% |     0.39 |       62 | 64.23%     | ok               |
|          20 | 8.38%    | 206.38%            | -30.47% |     0.27 |       74 | 59.73%     | ok               |
|          50 | -13.83%  | 206.38%            | -33.36% |    -0.07 |       60 | 41.43%     | ok               |
|          25 | -17.56%  | 206.38%            | -37.88% |    -0.08 |       72 | 57.40%     | ok               |
|          30 | -29.69%  | 206.38%            | -38.49% |    -0.3  |       78 | 55.07%     | ok               |

## NFLX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 54.32%   | 36.94%             | -11.94% |     1.13 |       46 | 47.09%     | ok               |
|          50 | 41.21%   | 36.94%             | -16.28% |     0.97 |       48 | 39.60%     | ok               |
|          35 | 45.92%   | 36.94%             | -18.30% |     0.95 |       62 | 50.75%     | ok               |
|          45 | 37.64%   | 36.94%             | -15.48% |     0.87 |       52 | 43.43%     | ok               |
|          25 | 35.58%   | 36.94%             | -21.09% |     0.75 |       62 | 57.24%     | ok               |

## NKE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | -27.03%  | -56.15%            | -42.13% |    -0.38 |       75 | 37.44%     | ok               |
|          20 | -36.88%  | -56.15%            | -50.44% |    -0.49 |       97 | 52.91%     | ok               |
|          25 | -37.10%  | -56.15%            | -51.20% |    -0.5  |       93 | 49.08%     | ok               |
|          40 | -26.61%  | -56.15%            | -31.33% |    -0.51 |       65 | 30.28%     | ok               |
|          30 | -37.92%  | -56.15%            | -55.35% |    -0.53 |       91 | 43.93%     | ok               |

## NOW Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 25.51%   | -37.73%            | -30.25% |     0.46 |       80 | 45.92%     | ok               |
|          20 | 26.07%   | -37.73%            | -26.36% |     0.46 |       79 | 51.91%     | ok               |
|          15 | 19.25%   | -37.73%            | -26.36% |     0.39 |       87 | 55.24%     | ok               |
|          35 | 17.41%   | -37.73%            | -29.30% |     0.38 |       81 | 40.60%     | ok               |
|          25 | 18.38%   | -37.73%            | -25.70% |     0.38 |       72 | 49.25%     | ok               |

## NVDA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -9.86%   | 117.05%            | -33.22% |     0.03 |       68 | 51.16%     | ok               |
|          30 | -11.55%  | 117.05%            | -35.26% |    -0.02 |       70 | 48.84%     | ok               |
|          20 | -15.84%  | 117.05%            | -40.59% |    -0.04 |       71 | 55.61%     | ok               |
|          50 | -18.88%  | 117.05%            | -40.84% |    -0.19 |       60 | 32.98%     | ok               |
|          35 | -21.91%  | 117.05%            | -41.25% |    -0.21 |       82 | 45.99%     | ok               |

## OP-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 74.65%   | -93.68%            | -45.76% |     0.86 |       36 | 17.43%     | ok               |
|          50 | 66.86%   | -93.68%            | -36.11% |     0.86 |       34 | 12.45%     | ok               |
|          40 | 59.18%   | -93.68%            | -53.61% |     0.72 |       48 | 26.05%     | ok               |
|          35 | 32.48%   | -93.68%            | -58.33% |     0.52 |       56 | 29.12%     | ok               |
|          30 | 4.44%    | -93.68%            | -70.27% |     0.29 |       74 | 35.82%     | ok               |

## ORCL Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 135.81%  | 59.59%             | -29.32% |     1.03 |       74 | 65.22%     | ok               |
|          25 | 76.90%   | 59.59%             | -27.76% |     0.76 |       75 | 57.74%     | ok               |
|          20 | 73.86%   | 59.59%             | -29.32% |     0.74 |       77 | 60.90%     | ok               |
|          35 | 51.67%   | 59.59%             | -31.95% |     0.62 |       68 | 49.42%     | ok               |
|          30 | 51.80%   | 59.59%             | -29.47% |     0.62 |       74 | 53.58%     | ok               |

## OXY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 2.48%    | -8.57%             | -30.85% |     0.16 |       63 | 43.09%     | ok               |
|          35 | -0.66%   | -8.57%             | -30.50% |     0.1  |       68 | 38.60%     | ok               |
|          50 | -2.35%   | -8.57%             | -31.07% |     0.05 |       40 | 27.79%     | ok               |
|          40 | -3.09%   | -8.57%             | -32.21% |     0.05 |       56 | 34.61%     | ok               |
|          25 | -11.70%  | -8.57%             | -40.42% |    -0.09 |       71 | 46.59%     | ok               |

## PEP Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 9.77%    | -14.99%            | -11.62% |     0.45 |       46 | 27.79%     | ok               |
|          45 | -0.55%   | -14.99%            | -14.22% |     0.03 |       70 | 32.61%     | ok               |
|          40 | -4.05%   | -14.99%            | -18.04% |    -0.09 |       78 | 38.44%     | ok               |
|          35 | -5.62%   | -14.99%            | -21.42% |    -0.12 |       87 | 43.43%     | ok               |
|          30 | -10.61%  | -14.99%            | -21.35% |    -0.25 |       85 | 50.08%     | ok               |

## PEPE-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 10.36%   | -82.50%            | -57.66% |     0.36 |       77 | 43.87%     | ok               |
|          35 | 4.07%    | -82.50%            | -51.35% |     0.29 |       62 | 38.51%     | ok               |
|          25 | -14.24%  | -82.50%            | -56.30% |     0.15 |       85 | 49.23%     | ok               |
|          15 | -30.68%  | -82.50%            | -65.75% |     0.07 |       81 | 59.39%     | ok               |
|          50 | -15.28%  | -82.50%            | -39.43% |     0.01 |       54 | 22.03%     | ok               |

## PFE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -23.21%  | -5.64%             | -25.65% |    -0.81 |       52 | 21.13%     | ok               |
|          50 | -25.54%  | -5.64%             | -26.92% |    -1    |       44 | 17.30%     | ok               |
|          40 | -29.72%  | -5.64%             | -31.95% |    -1.01 |       76 | 25.96%     | ok               |
|          35 | -33.30%  | -5.64%             | -36.39% |    -1.07 |       82 | 32.78%     | ok               |
|          30 | -39.48%  | -5.64%             | -42.29% |    -1.26 |       77 | 36.27%     | ok               |

## PG Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 0.45%    | -3.25%             | -19.77% |     0.07 |       52 | 34.94%     | ok               |
|          35 | -1.78%   | -3.25%             | -18.66% |    -0.02 |       60 | 38.27%     | ok               |
|          30 | -10.70%  | -3.25%             | -21.65% |    -0.37 |       62 | 41.43%     | ok               |
|          45 | -9.36%   | -3.25%             | -20.43% |    -0.38 |       52 | 32.45%     | ok               |
|          25 | -11.77%  | -3.25%             | -22.55% |    -0.42 |       72 | 42.60%     | ok               |

## PM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 2.02%    | 96.73%             | -32.20% |     0.14 |       88 | 53.58%     | ok               |
|          20 | -0.30%   | 96.73%             | -31.89% |     0.09 |       87 | 62.40%     | ok               |
|          30 | -1.25%   | 96.73%             | -33.68% |     0.07 |       81 | 57.57%     | ok               |
|          25 | -7.42%   | 96.73%             | -37.05% |    -0.07 |       81 | 59.73%     | ok               |
|          50 | -6.11%   | 96.73%             | -35.70% |    -0.07 |       76 | 42.43%     | ok               |

## POL-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 65.25%   | -83.62%            | -46.45% |     0.77 |       79 | 49.90%     | ok               |
|          25 | 58.21%   | -83.62%            | -46.72% |     0.7  |       68 | 57.80%     | ok               |
|          20 | 47.42%   | -83.62%            | -52.88% |     0.63 |       76 | 63.20%     | ok               |
|          15 | 46.27%   | -83.62%            | -58.42% |     0.61 |       76 | 68.59%     | ok               |
|          50 | 20.67%   | -83.62%            | -22.86% |     0.45 |       50 | 20.81%     | ok               |

## QCOM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -6.70%   | 37.87%             | -55.66% |     0.09 |       73 | 49.92%     | ok               |
|          35 | -8.89%   | 37.87%             | -51.84% |     0.05 |       83 | 45.26%     | ok               |
|          20 | -13.53%  | 37.87%             | -57.05% |     0    |       70 | 52.91%     | ok               |
|          30 | -18.84%  | 37.87%             | -57.69% |    -0.09 |       77 | 47.92%     | ok               |
|          15 | -27.90%  | 37.87%             | -60.40% |    -0.2  |       74 | 56.07%     | ok               |

## QQQ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | 24.22%   | 69.46%             | -12.88% |     0.64 |       57 | 49.25%     | ok               |
|          15 | 24.76%   | 69.46%             | -14.17% |     0.61 |       61 | 54.74%     | ok               |
|          20 | 21.22%   | 69.46%             | -12.98% |     0.56 |       65 | 51.91%     | ok               |
|          30 | 19.13%   | 69.46%             | -12.88% |     0.55 |       62 | 46.26%     | ok               |
|          35 | 6.95%    | 69.46%             | -19.00% |     0.27 |       68 | 42.60%     | ok               |

## RENDER-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 49.72%   | -58.41%            | -43.43% |     0.65 |       84 | 54.45%     | ok               |
|          15 | 32.34%   | -58.41%            | -44.59% |     0.55 |       84 | 57.56%     | ok               |
|          25 | 20.05%   | -58.41%            | -40.60% |     0.46 |       88 | 50.52%     | ok               |
|          30 | -17.59%  | -58.41%            | -45.00% |     0.11 |       96 | 44.10%     | ok               |
|          40 | -27.22%  | -58.41%            | -38.60% |    -0.1  |       70 | 29.40%     | ok               |

## RTX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 30.27%   | 111.77%            | -18.66% |     0.73 |       78 | 56.24%     | ok               |
|          50 | 22.85%   | 111.77%            | -18.42% |     0.71 |       58 | 42.10%     | ok               |
|          25 | 25.64%   | 111.77%            | -18.59% |     0.65 |       64 | 52.75%     | ok               |
|          35 | 21.12%   | 111.77%            | -18.00% |     0.62 |       56 | 49.75%     | ok               |
|          30 | 23.73%   | 111.77%            | -16.99% |     0.62 |       58 | 51.58%     | ok               |

## SBUX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -18.08%  | 7.79%              | -23.55% |    -0.32 |       63 | 40.93%     | ok               |
|          45 | -18.83%  | 7.79%              | -27.26% |    -0.44 |       64 | 28.45%     | ok               |
|          40 | -20.84%  | 7.79%              | -25.43% |    -0.46 |       60 | 32.45%     | ok               |
|          30 | -25.08%  | 7.79%              | -29.34% |    -0.52 |       62 | 38.60%     | ok               |
|          50 | -22.32%  | 7.79%              | -27.78% |    -0.58 |       52 | 24.63%     | ok               |

## SCHW Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 1.55%    | 48.34%             | -15.92% |     0.12 |       54 | 33.28%     | ok               |
|          50 | -2.36%   | 48.34%             | -12.59% |    -0.02 |       48 | 30.78%     | ok               |
|          25 | -10.23%  | 48.34%             | -28.76% |    -0.16 |       61 | 47.75%     | ok               |
|          40 | -8.98%   | 48.34%             | -21.81% |    -0.18 |       62 | 36.27%     | ok               |
|          20 | -11.91%  | 48.34%             | -29.24% |    -0.2  |       69 | 50.42%     | ok               |

## SHIB-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 0.77%    | -76.64%            | -49.21% |     0.25 |       74 | 68.01%     | ok               |
|          25 | -8.52%   | -76.64%            | -43.85% |     0.14 |       75 | 59.20%     | ok               |
|          20 | -9.86%   | -76.64%            | -46.38% |     0.14 |       77 | 63.79%     | ok               |
|          35 | -11.74%  | -76.64%            | -53.32% |     0.07 |       64 | 46.36%     | ok               |
|          40 | -16.59%  | -76.64%            | -50.74% |    -0.01 |       54 | 38.70%     | ok               |

## SHY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd    |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:-------|---------:|---------:|:-----------|:-----------------|
|          30 | -2.29%   | -0.35%             | -2.85% |    -0.79 |       50 | 35.11%     | ok               |
|          35 | -2.40%   | -0.35%             | -3.27% |    -0.84 |       52 | 33.28%     | ok               |
|          40 | -2.52%   | -0.35%             | -3.33% |    -0.9  |       52 | 31.45%     | ok               |
|          45 | -2.50%   | -0.35%             | -3.23% |    -0.91 |       50 | 28.29%     | ok               |
|          50 | -2.67%   | -0.35%             | -3.40% |    -1.02 |       46 | 25.46%     | ok               |

## SKY-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -32.93%  | -1.31%             | -56.39% |    -0.36 |       58 | 51.17%     | ok               |
|          30 | -28.81%  | -1.31%             | -43.98% |    -0.37 |       68 | 41.08%     | ok               |
|          25 | -32.46%  | -1.31%             | -48.09% |    -0.43 |       63 | 44.84%     | ok               |
|          20 | -42.75%  | -1.31%             | -58.40% |    -0.62 |       60 | 48.59%     | ok               |
|          35 | -39.99%  | -1.31%             | -49.68% |    -0.73 |       62 | 34.51%     | ok               |

## SLB Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 12.78%   | -4.08%             | -24.10% |     0.35 |       48 | 35.94%     | ok               |
|          45 | 10.18%   | -4.08%             | -21.53% |     0.31 |       54 | 32.45%     | ok               |
|          50 | -10.05%  | -4.08%             | -29.84% |    -0.16 |       54 | 28.62%     | ok               |
|          35 | -15.48%  | -4.08%             | -42.55% |    -0.22 |       74 | 43.93%     | ok               |
|          30 | -29.08%  | -4.08%             | -54.95% |    -0.52 |       75 | 50.25%     | ok               |

## SLV Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 56.72%   | 189.45%            | -34.10% |     0.78 |       50 | 32.95%     | ok               |
|          45 | 54.24%   | 189.45%            | -31.82% |     0.75 |       54 | 33.78%     | ok               |
|          40 | 52.39%   | 189.45%            | -31.93% |     0.73 |       60 | 35.94%     | ok               |
|          35 | 40.33%   | 189.45%            | -36.89% |     0.62 |       62 | 38.10%     | ok               |
|          30 | 32.14%   | 189.45%            | -42.66% |     0.54 |       58 | 40.27%     | ok               |

## SMH Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 119.88%  | 224.36%            | -30.17% |     1.34 |       47 | 53.74%     | ok               |
|          35 | 96.78%   | 224.36%            | -34.36% |     1.21 |       54 | 49.58%     | ok               |
|          25 | 96.64%   | 224.36%            | -32.94% |     1.2  |       46 | 52.58%     | ok               |
|          30 | 94.32%   | 224.36%            | -33.99% |     1.19 |       48 | 50.92%     | ok               |
|          45 | 80.19%   | 224.36%            | -32.75% |     1.14 |       52 | 43.76%     | ok               |

## SNX-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 23.42%   | -84.85%            | -28.28% |     0.45 |       66 | 32.76%     | ok               |
|          30 | 8.38%    | -84.85%            | -32.91% |     0.33 |       63 | 40.04%     | ok               |
|          20 | -0.61%   | -84.85%            | -43.20% |     0.27 |       75 | 50.57%     | ok               |
|          25 | -15.24%  | -84.85%            | -36.73% |     0.1  |       76 | 44.64%     | ok               |
|          40 | -16.75%  | -84.85%            | -41.74% |    -0.01 |       54 | 27.01%     | ok               |

## SOL-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -18.45%  | -60.37%            | -54.68% |     0.03 |       64 | 39.27%     | ok               |
|          25 | -32.68%  | -60.37%            | -53.21% |    -0.09 |       72 | 57.66%     | ok               |
|          35 | -33.64%  | -60.37%            | -61.96% |    -0.13 |       72 | 46.74%     | ok               |
|          15 | -39.62%  | -60.37%            | -59.14% |    -0.17 |       76 | 64.94%     | ok               |
|          20 | -42.35%  | -60.37%            | -56.90% |    -0.22 |       68 | 60.15%     | ok               |

## SOXX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 95.75%   | 192.87%            | -38.67% |     1.13 |       53 | 52.41%     | ok               |
|          25 | 92.01%   | 192.87%            | -39.85% |     1.11 |       51 | 52.08%     | ok               |
|          35 | 86.64%   | 192.87%            | -38.63% |     1.09 |       59 | 47.42%     | ok               |
|          15 | 90.84%   | 192.87%            | -37.72% |     1.06 |       66 | 55.24%     | ok               |
|          30 | 81.22%   | 192.87%            | -40.34% |     1.03 |       55 | 49.92%     | ok               |

## SPY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 17.86%   | 51.83%             | -14.25% |     0.61 |       58 | 54.41%     | ok               |
|          15 | 16.69%   | 51.83%             | -16.80% |     0.56 |       65 | 57.40%     | ok               |
|          25 | 10.49%   | 51.83%             | -15.22% |     0.4  |       58 | 53.41%     | ok               |
|          30 | 6.50%    | 51.83%             | -16.47% |     0.28 |       60 | 50.92%     | ok               |
|          35 | 3.93%    | 51.83%             | -16.72% |     0.2  |       58 | 48.25%     | ok               |

## SUSHI-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -24.39%  | -86.35%            | -40.79% |    -0.2  |       52 | 14.56%     | ok               |
|          45 | -56.30%  | -86.35%            | -64.69% |    -0.71 |       54 | 17.82%     | ok               |
|          40 | -59.39%  | -86.35%            | -66.97% |    -0.72 |       61 | 24.33%     | ok               |
|          35 | -67.00%  | -86.35%            | -75.30% |    -0.85 |       76 | 29.69%     | ok               |
|          15 | -80.09%  | -86.35%            | -81.81% |    -0.99 |       88 | 47.13%     | ok               |

## T Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 58.05%   | 30.62%             | -18.13% |     1.17 |       55 | 54.91%     | ok               |
|          25 | 49.95%   | 30.62%             | -17.66% |     1.06 |       60 | 52.58%     | ok               |
|          15 | 49.42%   | 30.62%             | -15.08% |     1.01 |       64 | 58.74%     | ok               |
|          30 | 34.99%   | 30.62%             | -17.01% |     0.83 |       62 | 50.42%     | ok               |
|          35 | 32.44%   | 30.62%             | -14.49% |     0.79 |       62 | 47.25%     | ok               |

## TGT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -6.81%   | -10.11%            | -40.99% |    -0.02 |       77 | 45.92%     | ok               |
|          15 | -9.86%   | -10.11%            | -38.83% |    -0.07 |       67 | 50.42%     | ok               |
|          25 | -10.93%  | -10.11%            | -43.53% |    -0.13 |       61 | 41.26%     | ok               |
|          45 | -10.17%  | -10.11%            | -30.47% |    -0.16 |       50 | 28.95%     | ok               |
|          30 | -11.79%  | -10.11%            | -41.74% |    -0.16 |       56 | 38.60%     | ok               |

## TIA-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 38.52%   | -91.37%            | -34.66% |     0.57 |       60 | 29.31%     | ok               |
|          40 | 37.75%   | -91.37%            | -31.28% |     0.56 |       60 | 24.90%     | ok               |
|          45 | 15.72%   | -91.37%            | -44.21% |     0.37 |       50 | 18.58%     | ok               |
|          50 | 13.81%   | -91.37%            | -44.86% |     0.36 |       32 | 11.49%     | ok               |
|          30 | -9.69%   | -91.37%            | -51.71% |     0.15 |       84 | 33.91%     | ok               |

## TLT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -13.79%  | -8.12%             | -16.06% |    -1.47 |       34 | 14.64%     | ok               |
|          30 | -23.41%  | -8.12%             | -24.34% |    -1.73 |       70 | 32.28%     | ok               |
|          40 | -19.00%  | -8.12%             | -20.30% |    -1.76 |       60 | 21.13%     | ok               |
|          45 | -17.82%  | -8.12%             | -19.55% |    -1.83 |       42 | 17.14%     | ok               |
|          35 | -22.91%  | -8.12%             | -23.85% |    -1.93 |       68 | 26.29%     | ok               |

## TMO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 43.47%   | -14.22%            | -10.55% |     0.99 |       36 | 30.12%     | ok               |
|          45 | 42.67%   | -14.22%            | -12.29% |     0.94 |       44 | 35.11%     | ok               |
|          40 | 40.56%   | -14.22%            | -12.07% |     0.89 |       47 | 39.60%     | ok               |
|          35 | 25.16%   | -14.22%            | -16.12% |     0.6  |       57 | 43.76%     | ok               |
|          30 | 18.33%   | -14.22%            | -16.83% |     0.46 |       57 | 48.09%     | ok               |

## TMUS Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 15.59%   | 11.53%             | -26.87% |     0.41 |       71 | 59.90%     | ok               |
|          30 | 14.20%   | 11.53%             | -24.50% |     0.39 |       72 | 48.25%     | ok               |
|          20 | 8.49%    | 11.53%             | -24.82% |     0.27 |       73 | 54.24%     | ok               |
|          25 | 7.41%    | 11.53%             | -25.91% |     0.25 |       77 | 50.58%     | ok               |
|          50 | 4.50%    | 11.53%             | -22.71% |     0.2  |       58 | 35.77%     | ok               |

## TRX-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 1.22%    | 44.17%             | -18.79% |     0.12 |       52 | 37.74%     | ok               |
|          30 | 0.38%    | 44.17%             | -22.90% |     0.1  |       72 | 48.85%     | ok               |
|          50 | -0.25%   | 44.17%             | -18.49% |     0.07 |       44 | 32.38%     | ok               |
|          35 | -0.99%   | 44.17%             | -21.77% |     0.06 |       68 | 46.17%     | ok               |
|          25 | -1.43%   | 44.17%             | -26.84% |     0.06 |       68 | 52.11%     | ok               |

## TSLA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 62.83%   | 117.04%            | -32.60% |     0.78 |       64 | 30.78%     | ok               |
|          40 | 54.63%   | 117.04%            | -45.90% |     0.67 |       61 | 35.27%     | ok               |
|          45 | 31.00%   | 117.04%            | -46.86% |     0.49 |       65 | 32.61%     | ok               |
|          35 | 12.75%   | 117.04%            | -54.51% |     0.33 |       74 | 38.27%     | ok               |
|          30 | -8.45%   | 117.04%            | -57.89% |     0.12 |       68 | 42.76%     | ok               |

## TXN Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 13.31%   | 80.31%             | -45.45% |     0.33 |       70 | 35.27%     | ok               |
|          20 | 4.58%    | 80.31%             | -38.98% |     0.22 |       61 | 60.23%     | ok               |
|          15 | 1.58%    | 80.31%             | -39.48% |     0.18 |       64 | 64.23%     | ok               |
|          35 | -0.02%   | 80.31%             | -43.38% |     0.13 |       74 | 50.75%     | ok               |
|          40 | -0.14%   | 80.31%             | -45.67% |     0.13 |       74 | 48.09%     | ok               |

## UNH Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 24.81%   | -19.03%            | -36.91% |     0.48 |       50 | 28.62%     | ok               |
|          30 | 20.56%   | -19.03%            | -27.46% |     0.42 |       76 | 52.08%     | ok               |
|          35 | 16.11%   | -19.03%            | -29.39% |     0.36 |       70 | 46.76%     | ok               |
|          15 | 16.31%   | -19.03%            | -30.48% |     0.36 |       79 | 67.05%     | ok               |
|          20 | 13.55%   | -19.03%            | -31.00% |     0.33 |       81 | 61.90%     | ok               |

## UNI-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -15.35%  | -74.90%            | -57.12% |     0.03 |       54 | 25.29%     | ok               |
|          40 | -25.14%  | -74.90%            | -63.75% |    -0.08 |       58 | 30.46%     | ok               |
|          50 | -23.03%  | -74.90%            | -55.74% |    -0.1  |       52 | 20.69%     | ok               |
|          35 | -34.14%  | -74.90%            | -69.40% |    -0.16 |       72 | 35.25%     | ok               |
|          20 | -70.29%  | -74.90%            | -80.81% |    -0.68 |       99 | 51.53%     | ok               |

## UPS Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -35.99%  | -34.17%            | -42.28% |    -0.69 |       74 | 44.43%     | ok               |
|          35 | -34.89%  | -34.17%            | -40.47% |    -0.7  |       59 | 34.28%     | ok               |
|          20 | -37.07%  | -34.17%            | -45.80% |    -0.7  |       80 | 47.59%     | ok               |
|          30 | -37.28%  | -34.17%            | -40.62% |    -0.74 |       66 | 39.93%     | ok               |
|          40 | -36.19%  | -34.17%            | -42.12% |    -0.76 |       51 | 29.12%     | ok               |

## USO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 15.25%   | 58.15%             | -33.25% |     0.36 |       46 | 27.45%     | ok               |
|          30 | 2.80%    | 58.15%             | -43.35% |     0.17 |       68 | 34.44%     | ok               |
|          40 | 1.81%    | 58.15%             | -41.14% |     0.15 |       57 | 29.95%     | ok               |
|          50 | 2.11%    | 58.15%             | -31.13% |     0.15 |       54 | 24.96%     | ok               |
|          25 | -1.92%   | 58.15%             | -45.95% |     0.1  |       68 | 36.94%     | ok               |

## VEA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 5.44%    | 52.45%             | -16.28% |     0.25 |       60 | 50.58%     | ok               |
|          20 | 1.19%    | 52.45%             | -17.70% |     0.1  |       61 | 47.92%     | ok               |
|          25 | -0.82%   | 52.45%             | -17.79% |     0.02 |       57 | 46.26%     | ok               |
|          30 | -0.98%   | 52.45%             | -17.93% |     0.01 |       58 | 44.09%     | ok               |
|          35 | -2.09%   | 52.45%             | -16.79% |    -0.03 |       56 | 43.09%     | ok               |

## VIXY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -46.17%  | -61.10%            | -68.69% |    -0.39 |       44 | 10.32%     | ok               |
|          45 | -56.13%  | -61.10%            | -74.13% |    -0.55 |       56 | 16.31%     | ok               |
|          40 | -64.45%  | -61.10%            | -80.03% |    -0.66 |       70 | 20.63%     | ok               |
|          35 | -68.17%  | -61.10%            | -83.81% |    -0.7  |       86 | 25.79%     | ok               |
|          15 | -78.77%  | -61.10%            | -89.47% |    -0.83 |      102 | 44.09%     | ok               |

## VNQ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -8.60%   | 12.24%             | -19.07% |    -0.37 |       60 | 28.62%     | ok               |
|          50 | -9.03%   | 12.24%             | -17.13% |    -0.41 |       56 | 26.12%     | ok               |
|          25 | -13.12%  | 12.24%             | -22.34% |    -0.51 |       69 | 40.77%     | ok               |
|          40 | -14.13%  | 12.24%             | -24.84% |    -0.62 |       74 | 32.11%     | ok               |
|          20 | -16.52%  | 12.24%             | -23.79% |    -0.64 |       74 | 43.59%     | ok               |

## VTI Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 19.29%   | 50.94%             | -13.96% |     0.64 |       62 | 55.74%     | ok               |
|          15 | 13.18%   | 50.94%             | -15.70% |     0.46 |       65 | 58.24%     | ok               |
|          25 | 6.34%    | 50.94%             | -16.10% |     0.27 |       58 | 53.91%     | ok               |
|          30 | -0.72%   | 50.94%             | -18.77% |     0.04 |       66 | 52.08%     | ok               |
|          40 | -2.95%   | 50.94%             | -20.44% |    -0.05 |       68 | 45.42%     | ok               |

## VWO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -6.69%   | 48.97%             | -21.68% |    -0.22 |       58 | 32.61%     | ok               |
|          15 | -9.03%   | 48.97%             | -24.01% |    -0.26 |       69 | 49.42%     | ok               |
|          45 | -8.51%   | 48.97%             | -23.75% |    -0.3  |       60 | 35.11%     | ok               |
|          20 | -10.06%  | 48.97%             | -26.14% |    -0.31 |       67 | 47.25%     | ok               |
|          40 | -8.98%   | 48.97%             | -23.57% |    -0.31 |       70 | 37.94%     | ok               |

## VZ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -5.99%   | 8.39%              | -16.98% |    -0.17 |       50 | 25.62%     | ok               |
|          45 | -14.43%  | 8.39%              | -20.38% |    -0.47 |       58 | 28.62%     | ok               |
|          35 | -19.49%  | 8.39%              | -24.68% |    -0.65 |       61 | 34.11%     | ok               |
|          25 | -22.50%  | 8.39%              | -28.84% |    -0.69 |       78 | 41.93%     | ok               |
|          40 | -22.28%  | 8.39%              | -26.72% |    -0.79 |       64 | 31.11%     | ok               |

## WFC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -1.01%   | 68.02%             | -18.29% |     0.03 |       58 | 32.95%     | ok               |
|          35 | -5.31%   | 68.02%             | -22.53% |    -0.04 |       79 | 44.59%     | ok               |
|          45 | -8.29%   | 68.02%             | -24.02% |    -0.17 |       66 | 37.60%     | ok               |
|          20 | -16.94%  | 68.02%             | -29.96% |    -0.24 |       79 | 53.91%     | ok               |
|          40 | -11.96%  | 68.02%             | -24.88% |    -0.28 |       76 | 40.93%     | ok               |

## WIF-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 35.16%   | -88.67%            | -46.21% |     0.54 |       75 | 42.15%     | ok               |
|          20 | 33.36%   | -88.67%            | -40.67% |     0.53 |       69 | 39.66%     | ok               |
|          25 | -10.96%  | -88.67%            | -45.19% |     0.21 |       73 | 36.78%     | ok               |
|          50 | -20.06%  | -88.67%            | -37.87% |    -0.14 |       40 | 12.07%     | ok               |
|          30 | -39.70%  | -88.67%            | -50.54% |    -0.17 |       72 | 32.57%     | ok               |

## WMT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 63.24%   | 117.63%            | -9.18%  |     1.61 |       36 | 44.26%     | ok               |
|          50 | 56.61%   | 117.63%            | -12.19% |     1.55 |       30 | 42.10%     | ok               |
|          40 | 53.03%   | 117.63%            | -9.18%  |     1.38 |       40 | 45.42%     | ok               |
|          35 | 50.82%   | 117.63%            | -10.09% |     1.29 |       50 | 49.42%     | ok               |
|          30 | 28.98%   | 117.63%            | -21.31% |     0.78 |       57 | 51.91%     | ok               |

## XBI Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 3.96%    | 57.50%             | -16.71% |     0.18 |       60 | 34.61%     | ok               |
|          45 | 3.16%    | 57.50%             | -16.88% |     0.16 |       52 | 31.45%     | ok               |
|          35 | -3.05%   | 57.50%             | -21.38% |     0.01 |       62 | 37.77%     | ok               |
|          30 | -4.13%   | 57.50%             | -21.75% |    -0.02 |       62 | 39.43%     | ok               |
|          50 | -5.14%   | 57.50%             | -16.83% |    -0.07 |       54 | 28.29%     | ok               |

## XLB Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -4.67%   | 26.14%             | -20.60% |    -0.12 |       60 | 32.11%     | ok               |
|          50 | -4.61%   | 26.14%             | -17.40% |    -0.14 |       44 | 27.79%     | ok               |
|          35 | -7.91%   | 26.14%             | -23.62% |    -0.24 |       60 | 35.61%     | ok               |
|          45 | -7.43%   | 26.14%             | -20.61% |    -0.25 |       44 | 29.28%     | ok               |
|          25 | -12.31%  | 26.14%             | -23.73% |    -0.4  |       70 | 41.43%     | ok               |

## XLC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 15.90%   | 41.03%             | -12.33% |     0.55 |       65 | 55.57%     | ok               |
|          25 | 13.72%   | 41.03%             | -12.31% |     0.48 |       62 | 57.40%     | ok               |
|          40 | 10.63%   | 41.03%             | -13.38% |     0.42 |       68 | 48.09%     | ok               |
|          35 | 10.61%   | 41.03%             | -13.38% |     0.41 |       64 | 52.58%     | ok               |
|          20 | 5.72%    | 41.03%             | -13.78% |     0.24 |       70 | 60.07%     | ok               |

## XLE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -1.92%   | 30.74%             | -25.98% |     0.02 |       56 | 36.77%     | ok               |
|          35 | -3.79%   | 30.74%             | -32.17% |    -0.02 |       65 | 44.59%     | ok               |
|          45 | -5.17%   | 30.74%             | -30.88% |    -0.07 |       62 | 39.60%     | ok               |
|          30 | -9.48%   | 30.74%             | -36.18% |    -0.17 |       71 | 46.59%     | ok               |
|          25 | -10.53%  | 30.74%             | -36.92% |    -0.18 |       78 | 49.92%     | ok               |

## XLF Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -4.85%   | 40.35%             | -18.01% |    -0.1  |       66 | 54.24%     | ok               |
|          15 | -8.79%   | 40.35%             | -19.58% |    -0.24 |       74 | 57.07%     | ok               |
|          25 | -11.49%  | 40.35%             | -23.22% |    -0.36 |       75 | 50.75%     | ok               |
|          30 | -11.92%  | 40.35%             | -23.61% |    -0.39 |       76 | 48.42%     | ok               |
|          35 | -18.99%  | 40.35%             | -27.24% |    -0.76 |       66 | 44.26%     | ok               |

## XLI Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 11.61%   | 58.08%             | -10.36% |     0.45 |       72 | 53.58%     | ok               |
|          20 | 7.09%    | 58.08%             | -12.74% |     0.31 |       63 | 49.08%     | ok               |
|          30 | 4.74%    | 58.08%             | -11.38% |     0.24 |       64 | 46.59%     | ok               |
|          45 | 4.31%    | 58.08%             | -12.27% |     0.23 |       62 | 38.10%     | ok               |
|          50 | 4.00%    | 58.08%             | -9.25%  |     0.23 |       56 | 36.11%     | ok               |

## XLK Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 82.69%   | 82.07%             | -14.75% |     1.32 |       41 | 53.91%     | ok               |
|          20 | 68.40%   | 82.07%             | -14.75% |     1.18 |       48 | 51.75%     | ok               |
|          25 | 64.97%   | 82.07%             | -14.75% |     1.18 |       42 | 49.58%     | ok               |
|          30 | 62.81%   | 82.07%             | -14.75% |     1.17 |       42 | 48.42%     | ok               |
|          35 | 44.65%   | 82.07%             | -13.61% |     0.94 |       54 | 45.76%     | ok               |

## XLM-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 56.88%   | -41.80%            | -32.06% |     0.73 |       46 | 27.78%     | ok               |
|          45 | 52.16%   | -41.80%            | -37.64% |     0.69 |       52 | 31.42%     | ok               |
|          30 | 29.68%   | -41.80%            | -45.54% |     0.5  |       71 | 45.79%     | ok               |
|          40 | 20.60%   | -41.80%            | -39.92% |     0.42 |       51 | 35.63%     | ok               |
|          35 | 18.33%   | -41.80%            | -44.88% |     0.4  |       71 | 41.76%     | ok               |

## XLP Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 11.84%   | 15.77%             | -5.66%  |     0.72 |       56 | 34.11%     | ok               |
|          50 | 9.69%    | 15.77%             | -6.08%  |     0.61 |       58 | 31.78%     | ok               |
|          40 | 9.59%    | 15.77%             | -7.77%  |     0.58 |       72 | 38.27%     | ok               |
|          35 | 8.63%    | 15.77%             | -9.73%  |     0.51 |       68 | 41.26%     | ok               |
|          30 | 6.70%    | 15.77%             | -11.16% |     0.41 |       70 | 42.76%     | ok               |

## XLU Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 7.60%    | 45.70%             | -9.11%  |     0.41 |       50 | 30.78%     | ok               |
|          45 | 5.39%    | 45.70%             | -10.56% |     0.3  |       54 | 31.78%     | ok               |
|          40 | 2.48%    | 45.70%             | -11.94% |     0.16 |       58 | 33.28%     | ok               |
|          35 | -1.48%   | 45.70%             | -16.24% |    -0.02 |       62 | 35.61%     | ok               |
|          30 | -4.57%   | 45.70%             | -18.15% |    -0.17 |       69 | 38.60%     | ok               |

## XLV Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -10.43%  | 8.83%              | -16.81% |    -0.5  |       68 | 36.44%     | ok               |
|          25 | -11.75%  | 8.83%              | -18.03% |    -0.56 |       70 | 37.77%     | ok               |
|          15 | -15.27%  | 8.83%              | -21.44% |    -0.72 |       81 | 42.76%     | ok               |
|          20 | -15.20%  | 8.83%              | -21.53% |    -0.74 |       75 | 39.60%     | ok               |
|          35 | -15.11%  | 8.83%              | -20.94% |    -0.8  |       66 | 33.94%     | ok               |

## XLY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 2.60%    | 35.16%             | -12.94% |     0.15 |       74 | 41.60%     | ok               |
|          30 | 0.76%    | 35.16%             | -14.01% |     0.09 |       74 | 44.59%     | ok               |
|          15 | -0.76%   | 35.16%             | -15.77% |     0.05 |       76 | 51.58%     | ok               |
|          50 | -0.60%   | 35.16%             | -11.79% |     0.03 |       52 | 29.78%     | ok               |
|          40 | -3.75%   | 35.16%             | -16.99% |    -0.07 |       70 | 37.27%     | ok               |

## XOM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | 5.34%    | 37.80%             | -19.90% |     0.22 |       56 | 36.77%     | ok               |
|          30 | 4.30%    | 37.80%             | -20.29% |     0.19 |       56 | 36.11%     | ok               |
|          20 | 1.45%    | 37.80%             | -25.56% |     0.12 |       61 | 39.27%     | ok               |
|          50 | 0.21%    | 37.80%             | -21.35% |     0.08 |       46 | 29.78%     | ok               |
|          35 | -1.82%   | 37.80%             | -20.93% |     0.02 |       58 | 34.78%     | ok               |

## XRP-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | -29.67%  | -52.88%            | -50.11% |    -0.21 |       70 | 41.95%     | ok               |
|          40 | -36.21%  | -52.88%            | -48.42% |    -0.36 |       62 | 35.82%     | ok               |
|          30 | -42.86%  | -52.88%            | -58.77% |    -0.42 |       74 | 46.36%     | ok               |
|          45 | -43.39%  | -52.88%            | -50.29% |    -0.52 |       62 | 31.42%     | ok               |
|          50 | -40.94%  | -52.88%            | -40.94% |    -0.58 |       64 | 23.75%     | ok               |

## YFI-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -30.68%  | -75.07%            | -50.17% |    -0.41 |       60 | 27.20%     | ok               |
|          45 | -36.29%  | -75.07%            | -51.92% |    -0.62 |       62 | 22.61%     | ok               |
|          35 | -50.37%  | -75.07%            | -64.34% |    -0.77 |       71 | 34.48%     | ok               |
|          30 | -53.87%  | -75.07%            | -67.78% |    -0.79 |       81 | 40.42%     | ok               |
|          50 | -41.48%  | -75.07%            | -51.80% |    -0.84 |       52 | 17.43%     | ok               |

## ZEC-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 124.17%  | 900.91%            | -24.66% |     0.9  |       50 | 23.18%     | ok               |
|          35 | 84.16%   | 900.91%            | -43.54% |     0.73 |       60 | 31.03%     | ok               |
|          25 | 71.15%   | 900.91%            | -46.61% |     0.68 |       61 | 39.85%     | ok               |
|          50 | 54.10%   | 900.91%            | -37.94% |     0.6  |       52 | 20.69%     | ok               |
|          30 | 41.84%   | 900.91%            | -46.93% |     0.55 |       69 | 36.59%     | ok               |
