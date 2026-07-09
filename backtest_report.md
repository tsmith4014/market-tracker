# Market Tracker Backtest Report

_Generated: 2026-07-09T04:25:57+00:00_

## Data Sources

- Crypto: Kraken -> Coinbase -> CoinGecko OHLC -> CoinPaprika fallback chain.
- Stocks / ETFs / indices: Stooq -> Yahoo Finance fallback chain.
- Data rows are generated from real market APIs. Mock OHLCV rows are not generated.

## Data Freshness

- Rows: **92,479**
- Symbols: **161**
- Date range: **2024-02-13** to **2026-07-09**

## Latest Signals

| symbol     | date                |         close |   composite_score | signal   | data_source   |
|:-----------|:--------------------|--------------:|------------------:|:---------|:--------------|
| AAPL       | 2026-07-08 00:00:00 |   313.39      |         56.0833   | LONG     | Yahoo Finance |
| ABBV       | 2026-07-08 00:00:00 |   252.74      |         59.75     | LONG     | Yahoo Finance |
| AMZN       | 2026-07-08 00:00:00 |   243.62      |         42.75     | LONG     | Yahoo Finance |
| ARKK       | 2026-07-08 00:00:00 |    80.16      |         52.4167   | LONG     | Yahoo Finance |
| BAC        | 2026-07-08 00:00:00 |    58.3       |         46.9167   | LONG     | Yahoo Finance |
| CL         | 2026-07-08 00:00:00 |    93.04      |         74.4167   | LONG     | Yahoo Finance |
| COP        | 2026-07-08 00:00:00 |   110.72      |         30.5      | LONG     | Yahoo Finance |
| DBC        | 2026-07-08 00:00:00 |    27.8       |         49        | LONG     | Yahoo Finance |
| DE         | 2026-07-08 00:00:00 |   596.74      |         39.5833   | LONG     | Yahoo Finance |
| DXY-INDEX  | 2026-07-09 00:00:00 |   100.973     |         60.2151   | LONG     | Yahoo Finance |
| EOG        | 2026-07-08 00:00:00 |   137.59      |         67.9167   | LONG     | Yahoo Finance |
| IBM        | 2026-07-08 00:00:00 |   302.05      |         63.0833   | LONG     | Yahoo Finance |
| ITA        | 2026-07-08 00:00:00 |   239.63      |         55.9167   | LONG     | Yahoo Finance |
| JNJ        | 2026-07-08 00:00:00 |   263.4       |         72.75     | LONG     | Yahoo Finance |
| LIN        | 2026-07-08 00:00:00 |   527.67      |         69.4167   | LONG     | Yahoo Finance |
| MS         | 2026-07-08 00:00:00 |   218.07      |         33.9167   | LONG     | Yahoo Finance |
| NOW        | 2026-07-08 00:00:00 |   107.78      |         37.3333   | LONG     | Yahoo Finance |
| NVDA       | 2026-07-08 00:00:00 |   204.12      |         39.5      | LONG     | Yahoo Finance |
| OXY        | 2026-07-08 00:00:00 |    53.59      |         41.5      | LONG     | Yahoo Finance |
| RTX        | 2026-07-08 00:00:00 |   194.91      |         55.9167   | LONG     | Yahoo Finance |
| SCHW       | 2026-07-08 00:00:00 |   101.7       |         58.0833   | LONG     | Yahoo Finance |
| SOL-USD    | 2026-07-09 00:00:00 |    77.26      |         37.0833   | LONG     | Kraken API    |
| SPY        | 2026-07-08 00:00:00 |   745.4       |         38.9167   | LONG     | Yahoo Finance |
| TGT        | 2026-07-08 00:00:00 |   132.42      |         38.5833   | LONG     | Yahoo Finance |
| TMO        | 2026-07-08 00:00:00 |   510.13      |         62.5833   | LONG     | Yahoo Finance |
| UNH        | 2026-07-08 00:00:00 |   425.6       |         44.75     | LONG     | Yahoo Finance |
| UNI-USD    | 2026-07-09 00:00:00 |     3.26      |         47        | LONG     | Kraken API    |
| WFC        | 2026-07-08 00:00:00 |    85.56      |         50.6667   | LONG     | Yahoo Finance |
| XBI        | 2026-07-08 00:00:00 |   162.97      |         73.25     | LONG     | Yahoo Finance |
| XLE        | 2026-07-08 00:00:00 |    55.6       |         44.4167   | LONG     | Yahoo Finance |
| XLF        | 2026-07-08 00:00:00 |    54.97      |         57.9167   | LONG     | Yahoo Finance |
| XLI        | 2026-07-08 00:00:00 |   180.42      |         45.0833   | LONG     | Yahoo Finance |
| XLU        | 2026-07-08 00:00:00 |    45.36      |         65        | LONG     | Yahoo Finance |
| XLV        | 2026-07-08 00:00:00 |   162.3       |         62.9167   | LONG     | Yahoo Finance |
| XOM        | 2026-07-08 00:00:00 |   141.13      |         48.5      | LONG     | Yahoo Finance |
| YFI-USD    | 2026-07-09 00:00:00 |  2142.5       |         44.6667   | LONG     | Kraken API    |
| ZEC-USD    | 2026-07-09 00:00:00 |   458.25      |         70.0833   | LONG     | Kraken API    |
| AAVE-USD   | 2026-07-09 00:00:00 |    87.12      |         19.3333   | NEUTRAL  | Kraken API    |
| ADA-USD    | 2026-07-09 00:00:00 |     0.166241  |          5.66667  | NEUTRAL  | Kraken API    |
| ADBE       | 2026-07-08 00:00:00 |   220.94      |          0.666667 | NEUTRAL  | Yahoo Finance |
| AGG        | 2026-07-08 00:00:00 |    98.04      |        -61        | NEUTRAL  | Yahoo Finance |
| ALGO-USD   | 2026-07-09 00:00:00 |     0.08508   |        -21.5833   | NEUTRAL  | Kraken API    |
| AMAT       | 2026-07-08 00:00:00 |   570.5       |         17.5833   | NEUTRAL  | Yahoo Finance |
| AMD        | 2026-07-08 00:00:00 |   517.41      |         12        | NEUTRAL  | Yahoo Finance |
| AMGN       | 2026-07-08 00:00:00 |   367.99      |         51.8333   | NEUTRAL  | Yahoo Finance |
| APT-USD    | 2026-07-09 00:00:00 |     0.6206    |        -10.5833   | NEUTRAL  | Kraken API    |
| ARB-USD    | 2026-07-09 00:00:00 |     0.0815    |         15.5833   | NEUTRAL  | Kraken API    |
| ATOM-USD   | 2026-07-09 00:00:00 |     1.5662    |        -15        | NEUTRAL  | Kraken API    |
| AVAX-USD   | 2026-07-09 00:00:00 |     6.475     |         -6.5      | NEUTRAL  | Kraken API    |
| AVGO       | 2026-07-08 00:00:00 |   388.69      |         28.1667   | NEUTRAL  | Yahoo Finance |
| BA         | 2026-07-08 00:00:00 |   224.95      |         29        | NEUTRAL  | Yahoo Finance |
| BCH-USD    | 2026-07-09 00:00:00 |   233.06      |          9        | NEUTRAL  | Kraken API    |
| BLK        | 2026-07-08 00:00:00 |   990.34      |        -56.1667   | NEUTRAL  | Yahoo Finance |
| BND        | 2026-07-08 00:00:00 |    72.7       |        -61        | NEUTRAL  | Yahoo Finance |
| BONK-USD   | 2026-07-09 00:00:00 |     3.979e-06 |        -34.75     | NEUTRAL  | Kraken API    |
| BTC-USD    | 2026-07-09 00:00:00 | 61953         |          0.666667 | NEUTRAL  | Kraken API    |
| C          | 2026-07-08 00:00:00 |   137.39      |         15.9167   | NEUTRAL  | Yahoo Finance |
| CAT        | 2026-07-08 00:00:00 |   948.08      |         16.0833   | NEUTRAL  | Yahoo Finance |
| CMCSA      | 2026-07-08 00:00:00 |    23.19      |         -0.416667 | NEUTRAL  | Yahoo Finance |
| COMP-USD   | 2026-07-09 00:00:00 |    16.68      |          9.66667  | NEUTRAL  | Kraken API    |
| COST       | 2026-07-08 00:00:00 |   953.13      |        -36.75     | NEUTRAL  | Yahoo Finance |
| CRM        | 2026-07-08 00:00:00 |   166.58      |          1.91667  | NEUTRAL  | Yahoo Finance |
| CRV-USD    | 2026-07-09 00:00:00 |     0.20076   |          4.16667  | NEUTRAL  | Kraken API    |
| CSCO       | 2026-07-08 00:00:00 |   113.82      |          4.91667  | NEUTRAL  | Yahoo Finance |
| CVX        | 2026-07-08 00:00:00 |   175.97      |         27.1667   | NEUTRAL  | Yahoo Finance |
| DASH-USD   | 2026-07-09 00:00:00 |    34.011     |        -34.0833   | NEUTRAL  | Kraken API    |
| DIA        | 2026-07-08 00:00:00 |   522.77      |         46.6667   | NEUTRAL  | Yahoo Finance |
| DIS        | 2026-07-08 00:00:00 |    96.7       |        -65.6667   | NEUTRAL  | Yahoo Finance |
| DOGE-USD   | 2026-07-09 00:00:00 |     0.0722489 |        -17        | NEUTRAL  | Kraken API    |
| DOT-USD    | 2026-07-09 00:00:00 |     0.8267    |         -9.5      | NEUTRAL  | Kraken API    |
| EEM        | 2026-07-08 00:00:00 |    66.23      |        -24.8333   | NEUTRAL  | Yahoo Finance |
| EFA        | 2026-07-08 00:00:00 |   103.36      |          5.66667  | NEUTRAL  | Yahoo Finance |
| ETC-USD    | 2026-07-09 00:00:00 |     6.964     |        -27.9167   | NEUTRAL  | Kraken API    |
| ETH-USD    | 2026-07-09 00:00:00 |  1729.94      |         23.6667   | NEUTRAL  | Kraken API    |
| EWJ        | 2026-07-08 00:00:00 |    92.54      |         -2.33333  | NEUTRAL  | Yahoo Finance |
| FCX        | 2026-07-08 00:00:00 |    57.5       |         -8.33333  | NEUTRAL  | Yahoo Finance |
| FIL-USD    | 2026-07-09 00:00:00 |     0.769     |         -4.83333  | NEUTRAL  | Kraken API    |
| FXI        | 2026-07-08 00:00:00 |    33.44      |        -19.5833   | NEUTRAL  | Yahoo Finance |
| GDX        | 2026-07-08 00:00:00 |    73.53      |        -55        | NEUTRAL  | Yahoo Finance |
| GDXJ       | 2026-07-08 00:00:00 |    95.6       |        -57        | NEUTRAL  | Yahoo Finance |
| GE         | 2026-07-08 00:00:00 |   356.03      |         12.0833   | NEUTRAL  | Yahoo Finance |
| GOOGL      | 2026-07-08 00:00:00 |   361.92      |         19.8333   | NEUTRAL  | Yahoo Finance |
| GRT-USD    | 2026-07-09 00:00:00 |     0.01738   |        -20.75     | NEUTRAL  | Kraken API    |
| GS         | 2026-07-08 00:00:00 |  1029.64      |          4.66667  | NEUTRAL  | Yahoo Finance |
| HBAR-USD   | 2026-07-09 00:00:00 |     0.06947   |        -17        | NEUTRAL  | Kraken API    |
| HD         | 2026-07-08 00:00:00 |   336.21      |        -16.3333   | NEUTRAL  | Yahoo Finance |
| HON        | 2026-07-08 00:00:00 |   220.36      |        -46.5      | NEUTRAL  | Yahoo Finance |
| HYG        | 2026-07-08 00:00:00 |    79.66      |        -61.75     | NEUTRAL  | Yahoo Finance |
| ICP-USD    | 2026-07-09 00:00:00 |     2.226     |         -8.58333  | NEUTRAL  | Kraken API    |
| IEF        | 2026-07-08 00:00:00 |    93.51      |        -61        | NEUTRAL  | Yahoo Finance |
| IEMG       | 2026-07-08 00:00:00 |    80.3       |        -24.8333   | NEUTRAL  | Yahoo Finance |
| INJ-USD    | 2026-07-09 00:00:00 |     4.772     |         -5.08333  | NEUTRAL  | Kraken API    |
| INTC       | 2026-07-08 00:00:00 |   110.24      |        -29.8333   | NEUTRAL  | Yahoo Finance |
| IWM        | 2026-07-08 00:00:00 |   293.48      |          7.66667  | NEUTRAL  | Yahoo Finance |
| JPM        | 2026-07-08 00:00:00 |   330.62      |         25.1667   | NEUTRAL  | Yahoo Finance |
| KO         | 2026-07-08 00:00:00 |    83.4       |         60.8333   | NEUTRAL  | Yahoo Finance |
| LDO-USD    | 2026-07-09 00:00:00 |     0.327     |         35.75     | NEUTRAL  | Kraken API    |
| LINK-USD   | 2026-07-09 00:00:00 |     7.61708   |        -10.5833   | NEUTRAL  | Kraken API    |
| LLY        | 2026-07-08 00:00:00 |  1215.83      |         51.3333   | NEUTRAL  | Yahoo Finance |
| LRCX       | 2026-07-08 00:00:00 |   333.15      |         10.4167   | NEUTRAL  | Yahoo Finance |
| LTC-USD    | 2026-07-09 00:00:00 |    43.71      |         11.6667   | NEUTRAL  | Kraken API    |
| MCD        | 2026-07-08 00:00:00 |   278.25      |        -28.5      | NEUTRAL  | Yahoo Finance |
| META       | 2026-07-08 00:00:00 |   603.12      |         10.75     | NEUTRAL  | Yahoo Finance |
| MPC        | 2026-07-08 00:00:00 |   280.68      |         60        | NEUTRAL  | Yahoo Finance |
| MRK        | 2026-07-08 00:00:00 |   125.99      |         64.8333   | NEUTRAL  | Yahoo Finance |
| MU         | 2026-07-08 00:00:00 |   948.8       |         -0.833333 | NEUTRAL  | Yahoo Finance |
| NEAR-USD   | 2026-07-09 00:00:00 |     1.8987    |         14.6667   | NEUTRAL  | Kraken API    |
| NEM        | 2026-07-08 00:00:00 |    93.2       |        -55        | NEUTRAL  | Yahoo Finance |
| NKE        | 2026-07-08 00:00:00 |    42.89      |        -49.5      | NEUTRAL  | Yahoo Finance |
| OP-USD     | 2026-07-09 00:00:00 |     0.1008    |        -24.25     | NEUTRAL  | Kraken API    |
| PEP        | 2026-07-08 00:00:00 |   142.51      |        -46.5      | NEUTRAL  | Yahoo Finance |
| PEPE-USD   | 2026-07-09 00:00:00 |     2.583e-06 |         -3.33333  | NEUTRAL  | Kraken API    |
| PG         | 2026-07-08 00:00:00 |   148.4       |         -9.08333  | NEUTRAL  | Yahoo Finance |
| PM         | 2026-07-08 00:00:00 |   187.07      |         59.1667   | NEUTRAL  | Yahoo Finance |
| POL-USD    | 2026-07-09 00:00:00 |     0.07593   |          7.41667  | NEUTRAL  | Kraken API    |
| QCOM       | 2026-07-08 00:00:00 |   186.56      |        -26.3333   | NEUTRAL  | Yahoo Finance |
| QQQ        | 2026-07-08 00:00:00 |   711.44      |         -0.166667 | NEUTRAL  | Yahoo Finance |
| RENDER-USD | 2026-07-09 00:00:00 |     1.535     |         -2.83333  | NEUTRAL  | Kraken API    |
| SBUX       | 2026-07-08 00:00:00 |   103.87      |         51.6667   | NEUTRAL  | Yahoo Finance |
| SHIB-USD   | 2026-07-09 00:00:00 |     4.239e-06 |         -2.83333  | NEUTRAL  | Kraken API    |
| SHY        | 2026-07-08 00:00:00 |    81.84      |        -58.25     | NEUTRAL  | Yahoo Finance |
| SKY-USD    | 2026-07-09 00:00:00 |     0.0545    |        -25.0833   | NEUTRAL  | Kraken API    |
| SLB        | 2026-07-08 00:00:00 |    47.43      |        -14.6667   | NEUTRAL  | Yahoo Finance |
| SMH        | 2026-07-08 00:00:00 |   593         |         -1.66667  | NEUTRAL  | Yahoo Finance |
| SNX-USD    | 2026-07-09 00:00:00 |     0.2183    |        -20.0833   | NEUTRAL  | Kraken API    |
| SOXX       | 2026-07-08 00:00:00 |   562.03      |         -1.66667  | NEUTRAL  | Yahoo Finance |
| SUSHI-USD  | 2026-07-09 00:00:00 |     0.1594    |          2.66667  | NEUTRAL  | Kraken API    |
| TIA-USD    | 2026-07-09 00:00:00 |     0.3934    |         35.8333   | NEUTRAL  | Kraken API    |
| TLT        | 2026-07-08 00:00:00 |    84.36      |        -60.5      | NEUTRAL  | Yahoo Finance |
| TRX-USD    | 2026-07-09 00:00:00 |     0.328819  |         58.1667   | NEUTRAL  | Kraken API    |
| TSLA       | 2026-07-08 00:00:00 |   394.06      |        -44.9167   | NEUTRAL  | Yahoo Finance |
| TXN        | 2026-07-08 00:00:00 |   301.32      |         23.1667   | NEUTRAL  | Yahoo Finance |
| UPS        | 2026-07-08 00:00:00 |   109.94      |         45.6667   | NEUTRAL  | Yahoo Finance |
| USO        | 2026-07-08 00:00:00 |   112.21      |         18        | NEUTRAL  | Yahoo Finance |
| VEA        | 2026-07-08 00:00:00 |    70.34      |          1.16667  | NEUTRAL  | Yahoo Finance |
| VIXY       | 2026-07-08 00:00:00 |    21.23      |        -25.5      | NEUTRAL  | Yahoo Finance |
| VNQ        | 2026-07-08 00:00:00 |    96.8       |         -2.08333  | NEUTRAL  | Yahoo Finance |
| VTI        | 2026-07-08 00:00:00 |   368.25      |         25.5833   | NEUTRAL  | Yahoo Finance |
| VWO        | 2026-07-08 00:00:00 |    59.17      |        -22.8333   | NEUTRAL  | Yahoo Finance |
| WIF-USD    | 2026-07-09 00:00:00 |     0.1574    |        -26.0833   | NEUTRAL  | Kraken API    |
| XLB        | 2026-07-08 00:00:00 |    50.16      |        -27        | NEUTRAL  | Yahoo Finance |
| XLC        | 2026-07-08 00:00:00 |   109.46      |        -28.25     | NEUTRAL  | Yahoo Finance |
| XLK        | 2026-07-08 00:00:00 |   181.4       |          0.333333 | NEUTRAL  | Yahoo Finance |
| XLM-USD    | 2026-07-09 00:00:00 |     0.180886  |        -31.4167   | NEUTRAL  | Kraken API    |
| XLP        | 2026-07-08 00:00:00 |    84.39      |         40.4167   | NEUTRAL  | Yahoo Finance |
| XLY        | 2026-07-08 00:00:00 |   115.3       |        -39.4167   | NEUTRAL  | Yahoo Finance |
| XRP-USD    | 2026-07-09 00:00:00 |     1.08678   |        -14.0833   | NEUTRAL  | Kraken API    |
| BITO       | 2026-07-08 00:00:00 |     8.44      |        -35.4167   | SHORT    | Yahoo Finance |
| FET-USD    | 2026-07-09 00:00:00 |     0.158     |        -34        | SHORT    | Kraken API    |
| GLD        | 2026-07-08 00:00:00 |   374.45      |        -38.25     | SHORT    | Yahoo Finance |
| IBIT       | 2026-07-08 00:00:00 |    35.23      |        -31.9167   | SHORT    | Yahoo Finance |
| INTU       | 2026-07-08 00:00:00 |   272.1       |        -30.25     | SHORT    | Yahoo Finance |
| MSFT       | 2026-07-08 00:00:00 |   383.34      |        -30.25     | SHORT    | Yahoo Finance |
| NFLX       | 2026-07-08 00:00:00 |    75.59      |        -33.25     | SHORT    | Yahoo Finance |
| ORCL       | 2026-07-08 00:00:00 |   140.49      |        -65.0833   | SHORT    | Yahoo Finance |
| PFE        | 2026-07-08 00:00:00 |    24.05      |        -59.4167   | SHORT    | Yahoo Finance |
| SLV        | 2026-07-08 00:00:00 |    52.83      |        -45.75     | SHORT    | Yahoo Finance |
| T          | 2026-07-08 00:00:00 |    21.12      |        -50.75     | SHORT    | Yahoo Finance |
| TMUS       | 2026-07-08 00:00:00 |   180.14      |        -39.9167   | SHORT    | Yahoo Finance |
| VZ         | 2026-07-08 00:00:00 |    42.45      |        -44.25     | SHORT    | Yahoo Finance |
| WMT        | 2026-07-08 00:00:00 |   113.1       |        -49.8333   | SHORT    | Yahoo Finance |

## Edge Summary

- Symbols with trades: **160** of 160
- Beat buy-and-hold: **33.12%** of traded symbols
- Positive return: **33.12%** of traded symbols
- Median strategy return: **-10.67%** (benchmark **16.98%**)
- Median excess vs benchmark: **-27.97%**
- Median Sharpe: **-0.12**
- Median exposure: **44.59%**

> Edge is real only if both _beat buy-and-hold_ and _median excess_ are convincingly positive across many symbols. Treat a single high-return symbol as noise.

## Portfolio Backtest

Actual capital-allocation books (not per-symbol averages). Benchmarks: `equal_weight_buyhold` (whole tracked universe), `spy_buyhold` (100% SPY), and `sixty_forty` (60% SPY / 40% AGG). `high_conf_voltarget` inverse-vol-weights the HIGH-confidence book; `conviction_long_short` is market-neutral. Judge on **Sharpe** and **max_drawdown** out-of-sample, not raw return: a fully-invested long book wins on return in a bull market but carries all the risk.

| strategy              | scope         | ann_return   | ann_vol   |   sharpe | max_drawdown   | total_return   |   avg_gross_exposure |
|:----------------------|:--------------|:-------------|:----------|---------:|:---------------|:---------------|---------------------:|
| equal_weight_buyhold  | full          | -3.56%       | 32.53%    |    -0.11 | -47.00%        | -23.72%        |                 1    |
| equal_weight_buyhold  | out_of_sample | -20.33%      | 31.24%    |    -0.65 | -39.63%        | -23.62%        |                 1    |
| all_signals_ew        | full          | -17.94%      | 27.23%    |    -0.66 | -63.22%        | -48.33%        |                 1    |
| all_signals_ew        | out_of_sample | 19.79%       | 26.82%    |     0.74 | -17.43%        | 18.92%         |                 1    |
| high_conf_ew          | full          | 4.69%        | 30.82%    |     0.15 | -40.60%        | 0.03%          |                 0.88 |
| high_conf_ew          | out_of_sample | 20.55%       | 33.72%    |     0.61 | -17.35%        | 17.41%         |                 0.88 |
| high_conf_voltarget   | full          | 6.56%        | 28.29%    |     0.23 | -34.62%        | 8.37%          |                 0.88 |
| high_conf_voltarget   | out_of_sample | 16.51%       | 31.29%    |     0.53 | -16.94%        | 13.39%         |                 0.88 |
| conviction_long_short | full          | -19.12%      | 23.04%    |    -0.83 | -49.38%        | -48.49%        |                 0.97 |
| conviction_long_short | out_of_sample | -10.56%      | 26.33%    |    -0.4  | -22.74%        | -13.92%        |                 0.97 |
| spy_buyhold           | full          | 6.42%        | 13.37%    |     0.48 | -18.27%        | 18.31%         |                 0.79 |
| spy_buyhold           | out_of_sample | -2.84%       | 9.77%     |    -0.29 | -13.27%        | -3.47%         |                 0.79 |
| sixty_forty           | full          | 3.84%        | 8.46%     |     0.45 | -10.80%        | 11.18%         |                 0.79 |
| sixty_forty           | out_of_sample | -3.18%       | 6.43%     |    -0.49 | -9.26%         | -3.55%         |                 0.79 |

## Walk-Forward Robustness

Each book measured across contiguous time folds (each a different regime). A book has durable edge only if `mean_sharpe` is positive, `min_sharpe` isn't deeply negative, and `pct_positive_folds` is high — a single great fold doesn't count. `fold_sharpes` lists each fold oldest-to-newest.

| strategy              |   n_folds |   mean_sharpe |   median_sharpe |   min_sharpe | pct_positive_folds   | mean_return   | fold_sharpes                 |
|:----------------------|----------:|--------------:|----------------:|-------------:|:---------------------|:--------------|:-----------------------------|
| equal_weight_buyhold  |         5 |          0.24 |            0.3  |        -1.78 | 60.00%               | -1.79%        | 1.93;-1.78;1.51;-0.76;0.30   |
| all_signals_ew        |         5 |         -0.6  |           -0.22 |        -2.06 | 20.00%               | -11.45%       | 0.05;-0.21;-2.06;-0.22;-0.55 |
| high_conf_ew          |         5 |          0.36 |            0.58 |        -0.9  | 60.00%               | 0.92%         | 1.43;0.73;-0.90;0.58;-0.05   |
| high_conf_voltarget   |         5 |          0.57 |            0.54 |        -0.89 | 60.00%               | 2.48%         | 2.33;0.98;-0.89;0.54;-0.12   |
| conviction_long_short |         5 |         -0.99 |           -1.25 |        -1.72 | 20.00%               | -12.20%       | -1.72;-1.25;-0.56;0.09;-1.53 |
| spy_buyhold           |         5 |          0.36 |           -0.29 |        -1.02 | 40.00%               | 4.03%         | 1.86;-1.02;1.79;-0.52;-0.29  |
| sixty_forty           |         5 |          0.32 |           -0.58 |        -1.14 | 40.00%               | 2.43%         | 2.09;-1.14;1.80;-0.59;-0.58  |

## Strategy Comparison

Each decision rule backtested over the same data. `out_of_sample` is the most recent ~35% of each symbol's history (unseen tail). A rule has real edge only if `median_excess` and `beat_benchmark_pct` stay positive out-of-sample, not just full-sample.

| strategy        | scope         |   symbols | beat_benchmark_pct   | positive_pct   | median_return   | median_benchmark   | median_excess   |   median_sharpe |   total_trades |
|:----------------|:--------------|----------:|:---------------------|:---------------|:----------------|:-------------------|:----------------|----------------:|---------------:|
| trend           | full          |       160 | 33.12%               | 33.12%         | -10.67%         | 16.98%             | -27.97%         |           -0.12 |          11210 |
| trend           | out_of_sample |       160 | 40.62%               | 51.88%         | 0.98%           | 4.77%              | -5.43%          |            0.2  |           3823 |
| mean_reversion  | full          |       157 | 40.76%               | 50.96%         | 0.06%           | 16.85%             | -17.95%         |            0.04 |           1258 |
| mean_reversion  | out_of_sample |       127 | 48.03%               | 58.27%         | 0.33%           | 1.72%              | -1.98%          |            0.63 |            434 |
| regime_adaptive | full          |       160 | 33.75%               | 34.38%         | -11.53%         | 16.98%             | -28.99%         |           -0.13 |          11483 |
| regime_adaptive | out_of_sample |       160 | 40.62%               | 51.88%         | 1.18%           | 4.77%              | -5.63%          |            0.22 |           3925 |

## Signal Calibration

Realized forward return in the signal's direction, grouped by confidence. HIGH should outrank LOW for the confidence score to be meaningful.

| confidence_level   |   horizon |     n | mean_return   | median_return   | win_rate   |
|:-------------------|----------:|------:|:--------------|:----------------|:-----------|
| HIGH               |         5 |  7993 | 0.14%         | 0.13%           | 52.11%     |
| MEDIUM             |         5 | 29208 | 0.03%         | 0.08%           | 50.92%     |
| LOW                |         5 |  3308 | -0.62%        | -0.55%          | 44.50%     |
| ALL                |         5 | 40509 | -0.00%        | 0.05%           | 50.63%     |
| HIGH               |        10 |  7945 | 0.45%         | 0.14%           | 51.74%     |
| MEDIUM             |        10 | 28993 | 0.19%         | 0.15%           | 51.21%     |
| LOW                |        10 |  3281 | -0.93%        | -0.74%          | 45.17%     |
| ALL                |        10 | 40219 | 0.15%         | 0.10%           | 50.82%     |
| HIGH               |        20 |  7865 | 0.82%         | 0.40%           | 53.13%     |
| MEDIUM             |        20 | 28627 | 0.85%         | 0.63%           | 53.63%     |
| LOW                |        20 |  3250 | -0.65%        | -0.48%          | 47.26%     |
| ALL                |        20 | 39742 | 0.72%         | 0.51%           | 53.01%     |

## Backtest Summary

### Data Quality / Signal Availability

- **ok**: 160 symbols

| symbol     |   trades | return   | benchmark_return   | mdd     |   sharpe | exposure   | skipped_reason   |
|:-----------|---------:|:---------|:-------------------|:--------|---------:|:-----------|:-----------------|
| AAPL       |       65 | 12.74%   | 69.36%             | -20.65% |     0.35 | 48.92%     | ok               |
| AAVE-USD   |       74 | -52.89%  | -68.48%            | -68.26% |    -0.51 | 38.12%     | ok               |
| ABBV       |       66 | -17.99%  | 45.85%             | -30.55% |    -0.37 | 47.25%     | ok               |
| ADA-USD    |       88 | -83.94%  | -79.55%            | -89.69% |    -0.71 | 46.74%     | ok               |
| ADBE       |       66 | -29.52%  | -63.29%            | -35.76% |    -0.36 | 57.07%     | ok               |
| AGG        |       69 | -6.61%   | 1.33%              | -10.16% |    -1.1  | 31.11%     | ok               |
| ALGO-USD   |       86 | -50.43%  | -72.85%            | -53.13% |    -0.57 | 38.12%     | ok               |
| AMAT       |       69 | -28.97%  | 216.40%            | -57.21% |    -0.21 | 53.24%     | ok               |
| AMD        |       54 | 4.65%    | 201.63%            | -44.44% |     0.26 | 35.94%     | ok               |
| AMGN       |       69 | -15.41%  | 26.68%             | -34.14% |    -0.29 | 46.26%     | ok               |
| AMZN       |       80 | -36.34%  | 44.46%             | -42.48% |    -1.08 | 38.27%     | ok               |
| APT-USD    |       76 | -39.90%  | -90.47%            | -69.96% |    -0.21 | 42.15%     | ok               |
| ARB-USD    |       66 | -21.16%  | -84.03%            | -62.34% |    -0.01 | 37.74%     | ok               |
| ARKK       |       85 | -33.60%  | 67.42%             | -35.25% |    -0.58 | 39.93%     | ok               |
| ATOM-USD   |       90 | -67.24%  | -68.22%            | -74.00% |    -1.09 | 45.98%     | ok               |
| AVAX-USD   |       68 | -22.52%  | -77.23%            | -53.72% |    -0.09 | 38.51%     | ok               |
| AVGO       |       62 | 24.61%   | 210.54%            | -35.76% |     0.43 | 43.43%     | ok               |
| BA         |       67 | 7.60%    | 10.02%             | -30.56% |     0.25 | 49.25%     | ok               |
| BAC        |       78 | -11.88%  | 78.02%             | -27.64% |    -0.25 | 48.92%     | ok               |
| BCH-USD    |       76 | -3.77%   | -34.05%            | -53.87% |     0.17 | 49.43%     | ok               |
| BITO       |       78 | 5.25%    | -63.98%            | -42.82% |     0.24 | 42.26%     | ok               |
| BLK        |       75 | -9.61%   | 27.28%             | -24.29% |    -0.22 | 43.26%     | ok               |
| BND        |       65 | -7.32%   | 1.31%              | -9.89%  |    -1.18 | 32.28%     | ok               |
| BONK-USD   |       72 | 45.25%   | -80.15%            | -45.22% |     0.6  | 41.57%     | ok               |
| BTC-USD    |       72 | -0.33%   | -38.92%            | -23.38% |     0.14 | 52.30%     | ok               |
| C          |       79 | -24.64%  | 160.41%            | -37.02% |    -0.45 | 51.58%     | ok               |
| CAT        |       72 | 26.11%   | 203.06%            | -21.02% |     0.5  | 56.91%     | ok               |
| CL         |       62 | 13.67%   | 11.47%             | -14.32% |     0.49 | 46.26%     | ok               |
| CMCSA      |       77 | -38.63%  | -40.88%            | -39.80% |    -1.01 | 43.09%     | ok               |
| COMP-USD   |       91 | -42.58%  | -70.83%            | -59.19% |    -0.3  | 46.36%     | ok               |
| COP        |       71 | -24.00%  | 0.87%              | -43.96% |    -0.44 | 41.26%     | ok               |
| COST       |       60 | 1.58%    | 33.44%             | -29.73% |     0.12 | 44.59%     | ok               |
| CRM        |       65 | -39.47%  | -40.75%            | -41.36% |    -0.82 | 43.09%     | ok               |
| CRV-USD    |       66 | -10.49%  | -65.27%            | -39.89% |     0.12 | 36.02%     | ok               |
| CSCO       |       59 | 25.75%   | 129.29%            | -21.79% |     0.55 | 49.42%     | ok               |
| CVX        |       71 | -14.39%  | 16.85%             | -26.75% |    -0.35 | 41.43%     | ok               |
| DASH-USD   |       63 | -44.37%  | 26.50%             | -64.43% |    -0.05 | 31.23%     | ok               |
| DBC        |       58 | -13.18%  | 25.56%             | -25.86% |    -0.46 | 32.61%     | ok               |
| DE         |       72 | -6.97%   | 57.34%             | -25.24% |    -0.05 | 47.25%     | ok               |
| DIA        |       60 | -1.50%   | 36.56%             | -12.94% |    -0.04 | 44.76%     | ok               |
| DIS        |       66 | -23.42%  | -12.46%            | -28.17% |    -0.47 | 46.76%     | ok               |
| DOGE-USD   |       77 | -21.59%  | -74.66%            | -60.95% |     0.03 | 50.77%     | ok               |
| DOT-USD    |       90 | -53.25%  | -84.06%            | -62.71% |    -0.49 | 48.28%     | ok               |
| DXY-INDEX  |       40 | -2.18%   | -0.57%             | -6.28%  |    -0.33 | 30.37%     | ok               |
| EEM        |       64 | -9.40%   | 69.21%             | -25.67% |    -0.25 | 43.43%     | ok               |
| EFA        |       62 | -9.68%   | 39.17%             | -15.14% |    -0.36 | 44.76%     | ok               |
| EOG        |       79 | -23.04%  | 23.92%             | -48.13% |    -0.49 | 46.26%     | ok               |
| ETC-USD    |       64 | -35.69%  | -68.51%            | -48.16% |    -0.51 | 31.23%     | ok               |
| ETH-USD    |       62 | 145.42%  | -40.00%            | -30.11% |     1.22 | 45.02%     | ok               |
| EWJ        |       62 | -18.16%  | 38.66%             | -30.73% |    -0.59 | 39.10%     | ok               |
| FCX        |       63 | -28.65%  | 56.85%             | -48.09% |    -0.33 | 45.09%     | ok               |
| FET-USD    |       79 | -35.88%  | -81.71%            | -48.39% |    -0.1  | 39.66%     | ok               |
| FIL-USD    |       70 | -47.29%  | -78.10%            | -50.88% |    -0.62 | 32.57%     | ok               |
| FXI        |       44 | -6.81%   | 50.63%             | -23.91% |    -0.08 | 30.12%     | ok               |
| GDX        |       60 | 11.28%   | 184.01%            | -34.99% |     0.3  | 48.09%     | ok               |
| GDXJ       |       68 | -23.13%  | 207.20%            | -44.93% |    -0.22 | 46.42%     | ok               |
| GE         |       74 | 18.12%   | 214.67%            | -27.82% |     0.4  | 54.08%     | ok               |
| GLD        |       48 | 26.42%   | 102.92%            | -16.63% |     0.66 | 46.76%     | ok               |
| GOOGL      |       59 | 79.31%   | 149.36%            | -20.41% |     1.18 | 53.08%     | ok               |
| GRT-USD    |       85 | -26.14%  | -88.30%            | -56.53% |    -0.13 | 41.19%     | ok               |
| GS         |       76 | -2.38%   | 171.85%            | -22.13% |     0.05 | 52.08%     | ok               |
| HD         |       73 | -8.50%   | -5.98%             | -18.58% |    -0.15 | 44.43%     | ok               |
| HON        |       94 | -29.10%  | 14.91%             | -31.48% |    -0.8  | 52.75%     | ok               |
| HYG        |       79 | -9.05%   | 4.04%              | -9.59%  |    -1.05 | 34.44%     | ok               |
| IBIT       |       32 | 33.09%   | -7.31%             | -18.95% |     0.7  | 32.31%     | ok               |
| IBM        |       78 | 8.93%    | 64.43%             | -27.54% |     0.27 | 49.75%     | ok               |
| ICP-USD    |       81 | -4.40%   | -70.92%            | -51.29% |     0.21 | 35.63%     | ok               |
| IEF        |       76 | -10.90%  | -0.03%             | -11.70% |    -1.54 | 32.78%     | ok               |
| IEMG       |       58 | -5.52%   | 63.11%             | -26.84% |    -0.12 | 43.59%     | ok               |
| INJ-USD    |       73 | -53.62%  | -70.30%            | -77.42% |    -0.52 | 37.16%     | ok               |
| INTC       |       70 | 55.82%   | 155.42%            | -60.60% |     0.62 | 49.25%     | ok               |
| INTU       |       67 | -18.19%  | -57.37%            | -43.77% |    -0.2  | 42.10%     | ok               |
| ITA        |       72 | -2.65%   | 93.09%             | -23.75% |    -0    | 48.25%     | ok               |
| IWM        |       48 | 9.40%    | 50.80%             | -12.83% |     0.39 | 35.77%     | ok               |
| JNJ        |       72 | 9.08%    | 68.34%             | -17.51% |     0.36 | 50.58%     | ok               |
| JPM        |       73 | -17.86%  | 89.73%             | -33.16% |    -0.41 | 53.91%     | ok               |
| KO         |       49 | 28.93%   | 40.52%             | -8.07%  |     1.03 | 37.77%     | ok               |
| LDO-USD    |       72 | 8.74%    | -82.40%            | -58.32% |     0.34 | 37.74%     | ok               |
| LIN        |       66 | -1.98%   | 26.77%             | -21.53% |    -0.01 | 38.94%     | ok               |
| LINK-USD   |       72 | -18.18%  | -64.86%            | -50.48% |     0.04 | 41.76%     | ok               |
| LLY        |       71 | -25.89%  | 63.64%             | -53.34% |    -0.35 | 50.58%     | ok               |
| LRCX       |       82 | -22.95%  | 273.24%            | -63.39% |    -0.11 | 45.59%     | ok               |
| LTC-USD    |       66 | -34.00%  | -59.17%            | -53.76% |    -0.29 | 48.47%     | ok               |
| MCD        |       75 | -2.55%   | -3.09%             | -18.81% |    -0.05 | 38.10%     | ok               |
| META       |       72 | -27.11%  | 31.08%             | -38.96% |    -0.44 | 48.59%     | ok               |
| MPC        |       71 | -15.39%  | 65.22%             | -44.76% |    -0.17 | 49.08%     | ok               |
| MRK        |       67 | -29.69%  | 0.45%              | -34.46% |    -0.72 | 44.59%     | ok               |
| MS         |       81 | -14.84%  | 159.70%            | -27.79% |    -0.29 | 50.25%     | ok               |
| MSFT       |       83 | -38.48%  | -5.66%             | -38.96% |    -1.02 | 47.75%     | ok               |
| MU         |       51 | 270.20%  | 1063.74%           | -68.76% |     1.34 | 59.90%     | ok               |
| NEAR-USD   |       83 | 9.87%    | -49.77%            | -60.10% |     0.34 | 40.42%     | ok               |
| NEM        |       72 | -31.13%  | 190.89%            | -38.49% |    -0.33 | 53.08%     | ok               |
| NFLX       |       64 | 32.61%   | 36.32%             | -21.09% |     0.69 | 54.58%     | ok               |
| NKE        |       91 | -48.19%  | -59.15%            | -57.25% |    -0.9  | 43.59%     | ok               |
| NOW        |       82 | 9.97%    | -30.35%            | -28.41% |     0.28 | 45.59%     | ok               |
| NVDA       |       74 | -26.41%  | 125.26%            | -45.02% |    -0.19 | 58.65%     | ok               |
| OP-USD     |       68 | -20.09%  | -91.51%            | -70.11% |     0.01 | 33.72%     | ok               |
| ORCL       |       72 | 98.42%   | 23.58%             | -29.47% |     0.89 | 53.58%     | ok               |
| OXY        |       67 | 2.35%    | -6.98%             | -31.37% |     0.16 | 43.59%     | ok               |
| PEP        |       79 | -6.85%   | -15.61%            | -21.35% |    -0.14 | 48.75%     | ok               |
| PEPE-USD   |       79 | 0.11%    | -76.56%            | -57.66% |     0.28 | 44.83%     | ok               |
| PFE        |       77 | -39.13%  | -10.83%            | -40.87% |    -1.25 | 35.44%     | ok               |
| PG         |       68 | -17.45%  | -5.04%             | -24.53% |    -0.65 | 41.10%     | ok               |
| PM         |       83 | -4.96%   | 109.74%            | -33.68% |    -0.01 | 56.41%     | ok               |
| POL-USD    |       79 | 47.25%   | -77.79%            | -46.45% |     0.65 | 49.81%     | ok               |
| QCOM       |       75 | -13.10%  | 24.34%             | -56.59% |    -0.01 | 46.26%     | ok               |
| QQQ        |       64 | 18.95%   | 66.01%             | -12.88% |     0.55 | 44.76%     | ok               |
| RENDER-USD |       98 | -19.07%  | -63.10%            | -45.00% |     0.1  | 43.45%     | ok               |
| RTX        |       58 | 25.71%   | 115.16%            | -16.99% |     0.64 | 51.58%     | ok               |
| SBUX       |       62 | -18.32%  | 10.65%             | -27.45% |    -0.34 | 39.10%     | ok               |
| SCHW       |       76 | -14.05%  | 62.18%             | -31.92% |    -0.27 | 46.59%     | ok               |
| SHIB-USD   |       78 | -36.38%  | -74.84%            | -48.95% |    -0.3  | 52.68%     | ok               |
| SHY        |       48 | -2.24%   | 0.34%              | -2.85%  |    -0.79 | 34.28%     | ok               |
| SKY-USD    |       70 | -28.56%  | -5.76%             | -43.98% |    -0.34 | 40.49%     | ok               |
| SLB        |       77 | -24.72%  | -0.32%             | -54.13% |    -0.41 | 51.41%     | ok               |
| SLV        |       58 | 49.79%   | 161.53%            | -42.66% |     0.69 | 42.43%     | ok               |
| SMH        |       48 | 87.57%   | 197.54%            | -33.99% |     1.14 | 48.75%     | ok               |
| SNX-USD    |       58 | -14.97%  | -82.72%            | -34.76% |     0.08 | 36.97%     | ok               |
| SOL-USD    |       68 | -33.81%  | -64.32%            | -56.90% |    -0.1  | 59.00%     | ok               |
| SOXX       |       57 | 76.19%   | 173.99%            | -41.89% |     0.99 | 47.59%     | ok               |
| SPY        |       64 | 3.93%    | 50.87%             | -16.47% |     0.2  | 50.08%     | ok               |
| SUSHI-USD  |       94 | -78.10%  | -83.36%            | -82.41% |    -1.15 | 36.21%     | ok               |
| T          |       62 | 42.43%   | 24.97%             | -17.01% |     0.92 | 52.58%     | ok               |
| TGT        |       58 | -12.57%  | -9.37%             | -40.57% |    -0.18 | 38.94%     | ok               |
| TIA-USD    |       89 | -49.45%  | -88.76%            | -70.38% |    -0.38 | 36.40%     | ok               |
| TLT        |       68 | -21.58%  | -8.65%             | -21.75% |    -1.68 | 31.61%     | ok               |
| TMO        |       59 | 12.40%   | -5.29%             | -18.85% |     0.35 | 49.42%     | ok               |
| TMUS       |       68 | 8.57%    | 11.56%             | -25.11% |     0.28 | 48.25%     | ok               |
| TRX-USD    |       72 | 0.99%    | 43.66%             | -22.90% |     0.12 | 49.04%     | ok               |
| TSLA       |       71 | 6.61%    | 114.14%            | -42.22% |     0.26 | 41.26%     | ok               |
| TXN        |       77 | -18.33%  | 92.11%             | -47.39% |    -0.14 | 53.58%     | ok               |
| UNH        |       74 | 34.74%   | -17.66%            | -26.96% |     0.57 | 52.41%     | ok               |
| UNI-USD    |       92 | -74.22%  | -67.23%            | -80.61% |    -0.92 | 43.10%     | ok               |
| UPS        |       70 | -37.03%  | -24.13%            | -38.75% |    -0.75 | 39.77%     | ok               |
| USO        |       68 | 5.95%    | 54.45%             | -43.35% |     0.22 | 33.78%     | ok               |
| VEA        |       58 | -0.98%   | 49.95%             | -17.93% |     0.01 | 44.09%     | ok               |
| VIXY       |       96 | -80.86%  | -65.31%            | -88.16% |    -1.03 | 32.78%     | ok               |
| VNQ        |       75 | -16.77%  | 17.11%             | -24.92% |    -0.7  | 37.60%     | ok               |
| VTI        |       68 | -1.57%   | 50.21%             | -18.77% |     0    | 51.08%     | ok               |
| VWO        |       76 | -13.41%  | 47.70%             | -25.20% |    -0.47 | 44.09%     | ok               |
| VZ         |       87 | -27.65%  | 5.78%              | -27.89% |    -0.93 | 37.10%     | ok               |
| WFC        |       86 | -16.94%  | 77.36%             | -29.91% |    -0.27 | 49.92%     | ok               |
| WIF-USD    |       68 | -35.28%  | -81.73%            | -50.54% |    -0.13 | 31.99%     | ok               |
| WMT        |       61 | 18.87%   | 100.60%            | -21.31% |     0.55 | 50.58%     | ok               |
| XBI        |       62 | 12.59%   | 83.69%             | -20.73% |     0.37 | 41.10%     | ok               |
| XLB        |       64 | -10.86%  | 21.42%             | -26.57% |    -0.36 | 36.77%     | ok               |
| XLC        |       67 | 13.12%   | 39.80%             | -12.33% |     0.47 | 55.07%     | ok               |
| XLE        |       73 | -10.98%  | 33.37%             | -37.51% |    -0.21 | 46.09%     | ok               |
| XLF        |       76 | -9.15%   | 41.93%             | -23.61% |    -0.28 | 48.25%     | ok               |
| XLI        |       66 | 0.84%    | 55.64%             | -11.74% |     0.09 | 45.26%     | ok               |
| XLK        |       42 | 63.89%   | 78.93%             | -14.75% |     1.19 | 46.26%     | ok               |
| XLM-USD    |       69 | 5.21%    | -51.18%            | -50.36% |     0.28 | 45.79%     | ok               |
| XLP        |       70 | 6.48%    | 15.86%             | -11.56% |     0.4  | 42.43%     | ok               |
| XLU        |       69 | -7.08%   | 51.30%             | -20.40% |    -0.28 | 38.60%     | ok               |
| XLV        |       68 | -13.29%  | 13.61%             | -17.94% |    -0.66 | 35.77%     | ok               |
| XLY        |       70 | 3.26%    | 30.90%             | -14.01% |     0.17 | 44.43%     | ok               |
| XOM        |       57 | 1.05%    | 39.26%             | -20.29% |     0.1  | 36.94%     | ok               |
| XRP-USD    |       58 | -30.47%  | -59.80%            | -44.89% |    -0.26 | 33.72%     | ok               |
| YFI-USD    |       83 | -63.69%  | -66.20%            | -69.94% |    -1.02 | 40.61%     | ok               |
| ZEC-USD    |       64 | 42.20%   | 1191.57%           | -47.68% |     0.55 | 34.48%     | ok               |

## AAPL Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 23.95%   | 69.36%             | -21.71% |     0.53 |       68 | 53.41%     | ok               |
|          15 | 20.14%   | 69.36%             | -23.86% |     0.46 |       75 | 60.57%     | ok               |
|          30 | 12.74%   | 69.36%             | -20.65% |     0.35 |       65 | 48.92%     | ok               |
|          25 | 12.57%   | 69.36%             | -20.03% |     0.35 |       67 | 51.08%     | ok               |
|          35 | 9.57%    | 69.36%             | -22.04% |     0.29 |       63 | 47.09%     | ok               |

## AAVE-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 9.07%    | -68.48%            | -43.61% |     0.31 |       38 | 31.42%     | ok               |
|          45 | -3.97%   | -68.48%            | -49.19% |     0.16 |       40 | 26.82%     | ok               |
|          35 | -10.29%  | -68.48%            | -51.96% |     0.11 |       50 | 34.10%     | ok               |
|          15 | -53.83%  | -68.48%            | -61.76% |    -0.36 |       80 | 52.30%     | ok               |
|          50 | -33.87%  | -68.48%            | -47.39% |    -0.36 |       42 | 19.73%     | ok               |

## ABBV Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -8.30%   | 45.85%             | -28.42% |    -0.13 |       52 | 37.27%     | ok               |
|          40 | -14.59%  | 45.85%             | -26.61% |    -0.3  |       66 | 41.60%     | ok               |
|          35 | -15.81%  | 45.85%             | -27.83% |    -0.33 |       68 | 44.43%     | ok               |
|          30 | -17.99%  | 45.85%             | -30.55% |    -0.37 |       66 | 47.25%     | ok               |
|          45 | -17.25%  | 45.85%             | -29.59% |    -0.38 |       56 | 38.94%     | ok               |

## ADA-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -77.92%  | -79.55%            | -85.97% |    -0.59 |       55 | 26.82%     | ok               |
|          45 | -80.28%  | -79.55%            | -88.02% |    -0.62 |       58 | 31.61%     | ok               |
|          35 | -82.72%  | -79.55%            | -89.77% |    -0.67 |       78 | 42.34%     | ok               |
|          15 | -86.32%  | -79.55%            | -91.83% |    -0.68 |       82 | 63.98%     | ok               |
|          20 | -86.10%  | -79.55%            | -92.33% |    -0.7  |       92 | 57.85%     | ok               |

## ADBE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 0.85%    | -63.29%            | -21.34% |     0.14 |       76 | 49.42%     | ok               |
|          25 | -15.53%  | -63.29%            | -30.06% |    -0.09 |       50 | 61.23%     | ok               |
|          40 | -12.16%  | -63.29%            | -24.87% |    -0.11 |       72 | 42.43%     | ok               |
|          15 | -23.30%  | -63.29%            | -31.45% |    -0.21 |       61 | 65.72%     | ok               |
|          20 | -24.80%  | -63.29%            | -32.14% |    -0.25 |       50 | 63.23%     | ok               |

## AGG Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -6.61%   | 1.33%              | -10.16% |    -1.1  |       69 | 31.11%     | ok               |
|          45 | -5.75%   | 1.33%              | -7.89%  |    -1.16 |       52 | 20.47%     | ok               |
|          20 | -8.00%   | 1.33%              | -10.96% |    -1.18 |       73 | 36.61%     | ok               |
|          50 | -5.57%   | 1.33%              | -7.92%  |    -1.25 |       46 | 16.97%     | ok               |
|          25 | -8.17%   | 1.33%              | -11.60% |    -1.25 |       73 | 34.94%     | ok               |

## ALGO-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -50.43%  | -72.85%            | -53.13% |    -0.57 |       86 | 38.12%     | ok               |
|          15 | -60.12%  | -72.85%            | -68.72% |    -0.63 |       88 | 50.77%     | ok               |
|          25 | -60.38%  | -72.85%            | -72.68% |    -0.69 |       88 | 45.40%     | ok               |
|          20 | -64.17%  | -72.85%            | -71.41% |    -0.76 |       90 | 48.47%     | ok               |
|          50 | -45.64%  | -72.85%            | -48.43% |    -0.81 |       42 | 16.86%     | ok               |

## AMAT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -15.13%  | 216.40%            | -54.05% |     0.02 |       66 | 61.90%     | ok               |
|          30 | -28.97%  | 216.40%            | -57.21% |    -0.21 |       69 | 53.24%     | ok               |
|          35 | -29.47%  | 216.40%            | -55.26% |    -0.23 |       71 | 50.92%     | ok               |
|          50 | -27.69%  | 216.40%            | -48.72% |    -0.23 |       52 | 38.94%     | ok               |
|          20 | -34.16%  | 216.40%            | -60.16% |    -0.27 |       72 | 58.40%     | ok               |

## AMD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 6.74%    | 201.63%            | -44.26% |     0.27 |       54 | 30.62%     | ok               |
|          40 | 4.65%    | 201.63%            | -44.44% |     0.26 |       54 | 35.94%     | ok               |
|          35 | -8.74%   | 201.63%            | -54.16% |     0.12 |       62 | 37.94%     | ok               |
|          45 | -14.79%  | 201.63%            | -53.24% |     0.04 |       60 | 33.44%     | ok               |
|          30 | -20.78%  | 201.63%            | -59.51% |    -0.01 |       63 | 40.43%     | ok               |

## AMGN Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -9.83%   | 26.68%             | -26.64% |    -0.12 |       71 | 52.41%     | ok               |
|          15 | -12.76%  | 26.68%             | -27.92% |    -0.18 |       68 | 58.40%     | ok               |
|          35 | -11.27%  | 26.68%             | -31.23% |    -0.18 |       65 | 42.43%     | ok               |
|          30 | -15.41%  | 26.68%             | -34.14% |    -0.29 |       69 | 46.26%     | ok               |
|          25 | -18.85%  | 26.68%             | -33.41% |    -0.37 |       65 | 48.59%     | ok               |

## AMZN Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -16.37%  | 44.46%             | -27.15% |    -0.47 |       52 | 29.12%     | ok               |
|          50 | -21.69%  | 44.46%             | -34.08% |    -0.75 |       48 | 23.29%     | ok               |
|          45 | -24.57%  | 44.46%             | -34.08% |    -0.84 |       52 | 26.29%     | ok               |
|          35 | -30.12%  | 44.46%             | -38.29% |    -0.94 |       68 | 32.78%     | ok               |
|          30 | -36.34%  | 44.46%             | -42.48% |    -1.08 |       80 | 38.27%     | ok               |

## APT-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 20.83%   | -90.47%            | -46.73% |     0.44 |       44 | 19.16%     | ok               |
|          45 | -10.36%  | -90.47%            | -64.17% |     0.07 |       60 | 24.71%     | ok               |
|          20 | -29.99%  | -90.47%            | -70.51% |    -0.04 |       73 | 51.34%     | ok               |
|          40 | -24.17%  | -90.47%            | -63.33% |    -0.07 |       66 | 30.46%     | ok               |
|          35 | -29.73%  | -90.47%            | -64.45% |    -0.11 |       70 | 36.21%     | ok               |

## ARB-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 36.04%   | -84.03%            | -53.74% |     0.54 |       85 | 55.17%     | ok               |
|          40 | 15.27%   | -84.03%            | -45.73% |     0.37 |       48 | 28.74%     | ok               |
|          20 | 2.23%    | -84.03%            | -60.40% |     0.29 |       73 | 48.66%     | ok               |
|          35 | 4.00%    | -84.03%            | -54.43% |     0.27 |       58 | 32.18%     | ok               |
|          45 | 3.38%    | -84.03%            | -49.08% |     0.24 |       54 | 22.03%     | ok               |

## ARKK Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -24.32%  | 67.42%             | -34.75% |    -0.28 |       92 | 50.25%     | ok               |
|          20 | -29.40%  | 67.42%             | -34.36% |    -0.42 |       89 | 45.76%     | ok               |
|          30 | -33.60%  | 67.42%             | -35.25% |    -0.58 |       85 | 39.93%     | ok               |
|          35 | -37.11%  | 67.42%             | -38.66% |    -0.71 |       86 | 37.44%     | ok               |
|          40 | -39.13%  | 67.42%             | -40.53% |    -0.82 |       76 | 32.95%     | ok               |

## ATOM-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -64.35%  | -68.22%            | -71.56% |    -0.93 |       95 | 52.87%     | ok               |
|          15 | -69.00%  | -68.22%            | -72.91% |    -0.99 |       95 | 62.84%     | ok               |
|          45 | -59.32%  | -68.22%            | -65.46% |    -1.09 |       74 | 29.69%     | ok               |
|          30 | -67.24%  | -68.22%            | -74.00% |    -1.09 |       90 | 45.98%     | ok               |
|          20 | -71.83%  | -68.22%            | -75.43% |    -1.14 |      103 | 56.70%     | ok               |

## AVAX-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 17.39%   | -77.23%            | -29.53% |     0.4  |       32 | 18.58%     | ok               |
|          45 | 15.21%   | -77.23%            | -32.82% |     0.37 |       32 | 22.22%     | ok               |
|          40 | 15.17%   | -77.23%            | -32.96% |     0.37 |       38 | 25.10%     | ok               |
|          35 | 6.87%    | -77.23%            | -36.30% |     0.28 |       56 | 30.46%     | ok               |
|          15 | -16.66%  | -77.23%            | -52.46% |     0.07 |       69 | 53.07%     | ok               |

## AVGO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 24.61%   | 210.54%            | -35.76% |     0.43 |       62 | 43.43%     | ok               |
|          35 | 18.61%   | 210.54%            | -36.19% |     0.38 |       70 | 40.60%     | ok               |
|          40 | 18.21%   | 210.54%            | -40.70% |     0.37 |       60 | 37.44%     | ok               |
|          25 | 16.72%   | 210.54%            | -38.01% |     0.36 |       68 | 44.59%     | ok               |
|          50 | 12.44%   | 210.54%            | -35.84% |     0.31 |       60 | 31.28%     | ok               |

## BA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 26.03%   | 10.02%             | -13.34% |     0.67 |       42 | 31.45%     | ok               |
|          35 | 30.46%   | 10.02%             | -23.77% |     0.59 |       72 | 44.59%     | ok               |
|          40 | 20.11%   | 10.02%             | -23.90% |     0.47 |       46 | 38.60%     | ok               |
|          25 | 10.59%   | 10.02%             | -32.48% |     0.29 |       70 | 52.58%     | ok               |
|          30 | 7.60%    | 10.02%             | -30.56% |     0.25 |       67 | 49.25%     | ok               |

## BAC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -3.34%   | 78.02%             | -21.99% |    -0.04 |       62 | 37.60%     | ok               |
|          20 | -6.34%   | 78.02%             | -21.70% |    -0.07 |       80 | 53.41%     | ok               |
|          50 | -4.91%   | 78.02%             | -20.52% |    -0.1  |       60 | 34.44%     | ok               |
|          35 | -7.21%   | 78.02%             | -29.13% |    -0.13 |       70 | 45.09%     | ok               |
|          15 | -11.61%  | 78.02%             | -23.91% |    -0.19 |       80 | 58.40%     | ok               |

## BCH-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 17.83%   | -34.05%            | -45.63% |     0.4  |       69 | 55.17%     | ok               |
|          15 | 4.35%    | -34.05%            | -48.75% |     0.28 |       78 | 59.77%     | ok               |
|          25 | 3.14%    | -34.05%            | -51.09% |     0.25 |       68 | 51.34%     | ok               |
|          30 | -3.77%   | -34.05%            | -53.87% |     0.17 |       76 | 49.43%     | ok               |
|          35 | -24.30%  | -34.05%            | -64.08% |    -0.12 |       70 | 45.59%     | ok               |

## BITO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 21.07%   | -63.98%            | -32.29% |     0.41 |       54 | 25.96%     | ok               |
|          30 | 5.25%    | -63.98%            | -42.82% |     0.24 |       78 | 42.26%     | ok               |
|          15 | -1.36%   | -63.98%            | -48.38% |     0.19 |       87 | 51.08%     | ok               |
|          45 | 1.85%    | -63.98%            | -43.53% |     0.18 |       62 | 29.62%     | ok               |
|          35 | 0.10%    | -63.98%            | -47.25% |     0.18 |       70 | 38.10%     | ok               |

## BLK Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | -3.55%   | 27.28%             | -17.97% |    -0.04 |       82 | 39.43%     | ok               |
|          20 | -5.80%   | 27.28%             | -21.48% |    -0.09 |       80 | 47.59%     | ok               |
|          40 | -5.38%   | 27.28%             | -20.08% |    -0.11 |       74 | 35.11%     | ok               |
|          30 | -9.61%   | 27.28%             | -24.29% |    -0.22 |       75 | 43.26%     | ok               |
|          25 | -10.52%  | 27.28%             | -23.36% |    -0.24 |       75 | 45.59%     | ok               |

## BND Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -6.17%   | 1.31%              | -9.05%  |    -0.9  |       63 | 38.10%     | ok               |
|          25 | -6.87%   | 1.31%              | -10.14% |    -1.05 |       67 | 36.11%     | ok               |
|          30 | -7.32%   | 1.31%              | -9.89%  |    -1.18 |       65 | 32.28%     | ok               |
|          15 | -8.39%   | 1.31%              | -10.58% |    -1.21 |       73 | 40.93%     | ok               |
|          45 | -7.56%   | 1.31%              | -9.57%  |    -1.47 |       50 | 21.96%     | ok               |

## BONK-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 179.94%  | -80.15%            | -35.57% |     1.28 |       44 | 21.84%     | ok               |
|          45 | 130.53%  | -80.15%            | -42.36% |     1.06 |       54 | 26.05%     | ok               |
|          20 | 137.48%  | -80.15%            | -55.19% |     0.94 |       68 | 52.87%     | ok               |
|          15 | 139.09%  | -80.15%            | -63.45% |     0.92 |       70 | 58.05%     | ok               |
|          25 | 109.07%  | -80.15%            | -47.99% |     0.86 |       67 | 48.08%     | ok               |

## BTC-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 43.79%   | -38.92%            | -15.92% |     0.81 |       46 | 34.67%     | ok               |
|          45 | 40.84%   | -38.92%            | -15.18% |     0.81 |       44 | 30.65%     | ok               |
|          35 | 26.71%   | -38.92%            | -27.54% |     0.56 |       70 | 41.57%     | ok               |
|          50 | 13.98%   | -38.92%            | -18.05% |     0.4  |       42 | 25.29%     | ok               |
|          30 | 11.49%   | -38.92%            | -21.75% |     0.33 |       74 | 48.28%     | ok               |

## C Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -6.96%   | 160.41%            | -22.28% |    -0.12 |       66 | 36.27%     | ok               |
|          45 | -13.83%  | 160.41%            | -28.12% |    -0.29 |       76 | 40.60%     | ok               |
|          25 | -21.25%  | 160.41%            | -34.18% |    -0.36 |       71 | 53.58%     | ok               |
|          15 | -23.25%  | 160.41%            | -35.02% |    -0.38 |       72 | 60.23%     | ok               |
|          20 | -23.89%  | 160.41%            | -35.56% |    -0.41 |       79 | 56.57%     | ok               |

## CAT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 26.11%   | 203.06%            | -21.02% |     0.5  |       72 | 56.91%     | ok               |
|          25 | 26.23%   | 203.06%            | -26.37% |     0.5  |       68 | 59.73%     | ok               |
|          20 | 24.75%   | 203.06%            | -25.65% |     0.48 |       78 | 63.23%     | ok               |
|          45 | 18.09%   | 203.06%            | -28.85% |     0.41 |       58 | 45.42%     | ok               |
|          35 | 15.04%   | 203.06%            | -27.72% |     0.36 |       72 | 50.25%     | ok               |

## CL Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 16.48%   | 11.47%             | -11.22% |     0.68 |       44 | 30.12%     | ok               |
|          30 | 13.67%   | 11.47%             | -14.32% |     0.49 |       62 | 46.26%     | ok               |
|          45 | 8.95%    | 11.47%             | -13.51% |     0.39 |       48 | 33.28%     | ok               |
|          35 | 8.26%    | 11.47%             | -13.83% |     0.33 |       64 | 42.60%     | ok               |
|          40 | 5.12%    | 11.47%             | -12.70% |     0.24 |       58 | 37.27%     | ok               |

## CMCSA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -36.85%  | -40.88%            | -45.95% |    -0.82 |       86 | 57.90%     | ok               |
|          30 | -38.63%  | -40.88%            | -39.80% |    -1.01 |       77 | 43.09%     | ok               |
|          25 | -42.38%  | -40.88%            | -43.19% |    -1.13 |       86 | 48.25%     | ok               |
|          20 | -47.69%  | -40.88%            | -48.42% |    -1.28 |       91 | 53.91%     | ok               |
|          50 | -32.22%  | -40.88%            | -33.36% |    -1.3  |       48 | 14.98%     | ok               |

## COMP-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -4.86%   | -70.83%            | -38.71% |     0.13 |       50 | 20.69%     | ok               |
|          25 | -43.63%  | -70.83%            | -61.30% |    -0.28 |       89 | 51.34%     | ok               |
|          30 | -42.58%  | -70.83%            | -59.19% |    -0.3  |       91 | 46.36%     | ok               |
|          15 | -51.14%  | -70.83%            | -66.20% |    -0.36 |      105 | 62.84%     | ok               |
|          40 | -44.41%  | -70.83%            | -50.01% |    -0.43 |       76 | 34.29%     | ok               |

## COP Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -9.76%   | 0.87%              | -35.08% |    -0.15 |       48 | 27.29%     | ok               |
|          35 | -21.85%  | 0.87%              | -43.58% |    -0.39 |       73 | 37.94%     | ok               |
|          45 | -20.42%  | 0.87%              | -41.35% |    -0.42 |       62 | 30.62%     | ok               |
|          30 | -24.00%  | 0.87%              | -43.96% |    -0.44 |       71 | 41.26%     | ok               |
|          40 | -25.44%  | 0.87%              | -47.05% |    -0.54 |       68 | 33.78%     | ok               |

## COST Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 13.32%   | 33.44%             | -24.32% |     0.43 |       66 | 51.08%     | ok               |
|          25 | 11.64%   | 33.44%             | -24.73% |     0.39 |       63 | 48.25%     | ok               |
|          35 | 6.45%    | 33.44%             | -26.58% |     0.26 |       54 | 41.60%     | ok               |
|          30 | 1.58%    | 33.44%             | -29.73% |     0.12 |       60 | 44.59%     | ok               |
|          40 | -0.08%   | 33.44%             | -28.41% |     0.06 |       56 | 38.60%     | ok               |

## CRM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -34.75%  | -40.75%            | -44.49% |    -0.54 |       92 | 55.07%     | ok               |
|          35 | -29.53%  | -40.75%            | -33.61% |    -0.58 |       62 | 38.27%     | ok               |
|          40 | -34.74%  | -40.75%            | -39.59% |    -0.8  |       68 | 34.28%     | ok               |
|          30 | -39.47%  | -40.75%            | -41.36% |    -0.82 |       65 | 43.09%     | ok               |
|          20 | -44.34%  | -40.75%            | -46.71% |    -0.85 |       78 | 48.75%     | ok               |

## CRV-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 12.72%   | -65.27%            | -37.78% |     0.35 |       68 | 31.42%     | ok               |
|          45 | -1.09%   | -65.27%            | -42.29% |     0.18 |       54 | 20.69%     | ok               |
|          50 | -0.89%   | -65.27%            | -29.30% |     0.18 |       46 | 17.43%     | ok               |
|          40 | -6.61%   | -65.27%            | -38.86% |     0.13 |       58 | 27.01%     | ok               |
|          30 | -10.49%  | -65.27%            | -39.89% |     0.12 |       66 | 36.02%     | ok               |

## CSCO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 33.16%   | 129.29%            | -19.34% |     0.72 |       54 | 38.44%     | ok               |
|          45 | 31.69%   | 129.29%            | -19.34% |     0.68 |       51 | 40.43%     | ok               |
|          25 | 26.34%   | 129.29%            | -23.28% |     0.56 |       63 | 51.41%     | ok               |
|          35 | 25.74%   | 129.29%            | -23.68% |     0.55 |       51 | 46.92%     | ok               |
|          30 | 25.75%   | 129.29%            | -21.79% |     0.55 |       59 | 49.42%     | ok               |

## CVX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -9.66%   | 16.85%             | -23.25% |    -0.19 |       72 | 43.93%     | ok               |
|          20 | -12.72%  | 16.85%             | -25.18% |    -0.27 |       72 | 45.26%     | ok               |
|          35 | -12.54%  | 16.85%             | -27.83% |    -0.3  |       69 | 38.44%     | ok               |
|          30 | -14.39%  | 16.85%             | -26.75% |    -0.35 |       71 | 41.43%     | ok               |
|          40 | -13.26%  | 16.85%             | -26.30% |    -0.36 |       73 | 34.78%     | ok               |

## DASH-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 112.86%  | 26.50%             | -28.93% |     0.9  |       40 | 15.71%     | ok               |
|          40 | 62.85%   | 26.50%             | -32.07% |     0.66 |       48 | 23.18%     | ok               |
|          45 | 53.72%   | 26.50%             | -37.43% |     0.62 |       44 | 18.01%     | ok               |
|          35 | -39.28%  | 26.50%             | -63.23% |     0.01 |       69 | 27.78%     | ok               |
|          25 | -44.80%  | 26.50%             | -64.14% |    -0.05 |       69 | 33.91%     | ok               |

## DBC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -10.58%  | 25.56%             | -27.30% |    -0.33 |       73 | 37.77%     | ok               |
|          35 | -10.31%  | 25.56%             | -23.91% |    -0.34 |       60 | 31.45%     | ok               |
|          50 | -8.98%   | 25.56%             | -20.31% |    -0.34 |       42 | 21.13%     | ok               |
|          45 | -10.35%  | 25.56%             | -21.46% |    -0.37 |       54 | 24.46%     | ok               |
|          30 | -13.18%  | 25.56%             | -25.86% |    -0.46 |       58 | 32.61%     | ok               |

## DE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -6.10%   | 57.34%             | -28.94% |    -0.03 |       72 | 52.58%     | ok               |
|          30 | -6.97%   | 57.34%             | -25.24% |    -0.05 |       72 | 47.25%     | ok               |
|          25 | -8.42%   | 57.34%             | -26.67% |    -0.08 |       74 | 49.92%     | ok               |
|          50 | -7.34%   | 57.34%             | -23.21% |    -0.11 |       70 | 32.11%     | ok               |
|          45 | -9.24%   | 57.34%             | -26.88% |    -0.14 |       70 | 36.61%     | ok               |

## DIA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 0.58%    | 36.56%             | -13.15% |     0.07 |       60 | 42.60%     | ok               |
|          25 | 0.04%    | 36.56%             | -11.28% |     0.04 |       60 | 45.92%     | ok               |
|          30 | -1.50%   | 36.56%             | -12.94% |    -0.04 |       60 | 44.76%     | ok               |
|          20 | -3.39%   | 36.56%             | -13.85% |    -0.14 |       64 | 48.25%     | ok               |
|          40 | -3.49%   | 36.56%             | -15.06% |    -0.17 |       66 | 39.93%     | ok               |

## DIS Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 17.01%   | -12.46%            | -14.24% |     0.54 |       48 | 28.62%     | ok               |
|          45 | -7.38%   | -12.46%            | -16.54% |    -0.1  |       49 | 32.28%     | ok               |
|          40 | -8.84%   | -12.46%            | -23.29% |    -0.11 |       63 | 37.44%     | ok               |
|          15 | -19.08%  | -12.46%            | -31.15% |    -0.29 |       88 | 58.24%     | ok               |
|          35 | -17.96%  | -12.46%            | -25.70% |    -0.33 |       73 | 43.43%     | ok               |

## DOGE-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 21.09%   | -74.66%            | -57.89% |     0.45 |       83 | 67.05%     | ok               |
|          20 | 0.82%    | -74.66%            | -55.83% |     0.28 |       86 | 61.88%     | ok               |
|          25 | -6.29%   | -74.66%            | -53.72% |     0.21 |       74 | 56.32%     | ok               |
|          30 | -21.59%  | -74.66%            | -60.95% |     0.03 |       77 | 50.77%     | ok               |
|          35 | -48.65%  | -74.66%            | -63.16% |    -0.44 |       74 | 44.06%     | ok               |

## DOT-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -23.35%  | -84.06%            | -46.17% |    -0.2  |       58 | 25.86%     | ok               |
|          45 | -29.89%  | -84.06%            | -54.01% |    -0.29 |       50 | 30.65%     | ok               |
|          20 | -54.23%  | -84.06%            | -64.09% |    -0.44 |       92 | 60.54%     | ok               |
|          35 | -49.91%  | -84.06%            | -62.62% |    -0.45 |       76 | 41.00%     | ok               |
|          30 | -53.25%  | -84.06%            | -62.71% |    -0.49 |       90 | 48.28%     | ok               |

## DXY-INDEX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -2.98%   | -0.57%             | -11.37% |    -0.25 |       82 | 77.01%     | ok               |
|          50 | -2.18%   | -0.57%             | -6.28%  |    -0.33 |       40 | 30.37%     | ok               |
|          40 | -3.99%   | -0.57%             | -7.30%  |    -0.5  |       74 | 49.89%     | ok               |
|          30 | -4.59%   | -0.57%             | -9.61%  |    -0.52 |       72 | 62.04%     | ok               |
|          25 | -5.56%   | -0.57%             | -12.10% |    -0.6  |       78 | 67.25%     | ok               |

## EEM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -4.96%   | 69.21%             | -19.52% |    -0.11 |       64 | 39.77%     | ok               |
|          35 | -5.62%   | 69.21%             | -23.88% |    -0.12 |       66 | 41.76%     | ok               |
|          50 | -4.94%   | 69.21%             | -15.88% |    -0.12 |       52 | 35.77%     | ok               |
|          45 | -6.04%   | 69.21%             | -17.36% |    -0.16 |       54 | 37.44%     | ok               |
|          30 | -9.40%   | 69.21%             | -25.67% |    -0.25 |       64 | 43.43%     | ok               |

## EFA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -3.05%   | 39.17%             | -10.80% |    -0.05 |       62 | 52.41%     | ok               |
|          20 | -9.78%   | 39.17%             | -12.73% |    -0.34 |       69 | 49.42%     | ok               |
|          30 | -9.68%   | 39.17%             | -15.14% |    -0.36 |       62 | 44.76%     | ok               |
|          50 | -9.07%   | 39.17%             | -17.56% |    -0.4  |       54 | 36.27%     | ok               |
|          25 | -11.91%  | 39.17%             | -16.37% |    -0.45 |       64 | 46.76%     | ok               |

## EOG Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -17.81%  | 23.92%             | -39.32% |    -0.4  |       56 | 32.61%     | ok               |
|          30 | -23.04%  | 23.92%             | -48.13% |    -0.49 |       79 | 46.26%     | ok               |
|          50 | -20.79%  | 23.92%             | -40.21% |    -0.52 |       58 | 29.62%     | ok               |
|          35 | -23.43%  | 23.92%             | -45.93% |    -0.54 |       77 | 41.10%     | ok               |
|          40 | -22.68%  | 23.92%             | -42.91% |    -0.54 |       64 | 35.94%     | ok               |

## ETC-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -7.93%   | -68.51%            | -27.89% |    -0.02 |       28 | 17.05%     | ok               |
|          35 | -15.03%  | -68.51%            | -42.62% |    -0.11 |       44 | 27.01%     | ok               |
|          45 | -16.07%  | -68.51%            | -35.44% |    -0.17 |       26 | 18.97%     | ok               |
|          40 | -21.04%  | -68.51%            | -40.48% |    -0.26 |       42 | 22.80%     | ok               |
|          30 | -35.69%  | -68.51%            | -48.16% |    -0.51 |       64 | 31.23%     | ok               |

## ETH-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 145.42%  | -40.00%            | -30.11% |     1.22 |       62 | 45.02%     | ok               |
|          30 | 123.40%  | -40.00%            | -32.89% |     1.08 |       66 | 53.07%     | ok               |
|          40 | 50.82%   | -40.00%            | -33.11% |     0.7  |       60 | 37.74%     | ok               |
|          20 | 42.22%   | -40.00%            | -39.10% |     0.59 |       82 | 62.26%     | ok               |
|          25 | 41.17%   | -40.00%            | -40.90% |     0.59 |       66 | 58.05%     | ok               |

## EWJ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -18.16%  | 38.66%             | -30.73% |    -0.59 |       62 | 39.10%     | ok               |
|          20 | -19.55%  | 38.66%             | -31.32% |    -0.62 |       58 | 41.10%     | ok               |
|          45 | -18.94%  | 38.66%             | -27.68% |    -0.72 |       58 | 31.28%     | ok               |
|          25 | -21.87%  | 38.66%             | -31.18% |    -0.72 |       58 | 40.10%     | ok               |
|          35 | -22.08%  | 38.66%             | -32.54% |    -0.75 |       68 | 37.44%     | ok               |

## FCX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -4.48%   | 56.85%             | -27.82% |     0.06 |       52 | 29.45%     | ok               |
|          45 | -8.60%   | 56.85%             | -35.29% |    -0    |       52 | 33.94%     | ok               |
|          40 | -20.30%  | 56.85%             | -44.23% |    -0.2  |       62 | 38.44%     | ok               |
|          30 | -28.65%  | 56.85%             | -48.09% |    -0.33 |       63 | 45.09%     | ok               |
|          20 | -34.13%  | 56.85%             | -57.65% |    -0.39 |       70 | 51.91%     | ok               |

## FET-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 9.07%    | -81.71%            | -58.75% |     0.38 |       84 | 50.38%     | ok               |
|          15 | -13.74%  | -81.71%            | -59.58% |     0.21 |       82 | 54.41%     | ok               |
|          25 | -32.19%  | -81.71%            | -59.31% |    -0.02 |       87 | 43.87%     | ok               |
|          30 | -35.88%  | -81.71%            | -48.39% |    -0.1  |       79 | 39.66%     | ok               |
|          35 | -51.50%  | -81.71%            | -60.25% |    -0.46 |       65 | 32.95%     | ok               |

## FIL-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -26.71%  | -78.10%            | -41.11% |    -0.27 |       46 | 22.99%     | ok               |
|          35 | -44.63%  | -78.10%            | -48.17% |    -0.61 |       56 | 27.01%     | ok               |
|          45 | -39.88%  | -78.10%            | -43.98% |    -0.61 |       42 | 17.24%     | ok               |
|          30 | -47.29%  | -78.10%            | -50.88% |    -0.62 |       70 | 32.57%     | ok               |
|          50 | -39.00%  | -78.10%            | -44.95% |    -0.69 |       36 | 12.64%     | ok               |

## FXI Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -6.27%   | 50.63%             | -22.57% |    -0.07 |       44 | 31.28%     | ok               |
|          30 | -6.81%   | 50.63%             | -23.91% |    -0.08 |       44 | 30.12%     | ok               |
|          45 | -6.49%   | 50.63%             | -26.75% |    -0.09 |       44 | 24.63%     | ok               |
|          15 | -9.05%   | 50.63%             | -21.68% |    -0.13 |       52 | 34.61%     | ok               |
|          20 | -10.05%  | 50.63%             | -24.53% |    -0.16 |       50 | 32.45%     | ok               |

## GDX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 18.06%   | 184.01%            | -35.59% |     0.39 |       73 | 52.91%     | ok               |
|          40 | 13.85%   | 184.01%            | -31.87% |     0.35 |       64 | 42.93%     | ok               |
|          30 | 11.28%   | 184.01%            | -34.99% |     0.3  |       60 | 48.09%     | ok               |
|          35 | 8.95%    | 184.01%            | -32.37% |     0.27 |       68 | 45.26%     | ok               |
|          25 | 6.77%    | 184.01%            | -38.90% |     0.24 |       63 | 49.75%     | ok               |

## GDXJ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -7.90%   | 207.20%            | -45.05% |     0.06 |       67 | 53.24%     | ok               |
|          50 | -18.94%  | 207.20%            | -44.94% |    -0.2  |       58 | 37.94%     | ok               |
|          30 | -23.13%  | 207.20%            | -44.93% |    -0.22 |       68 | 46.42%     | ok               |
|          25 | -26.54%  | 207.20%            | -47.26% |    -0.25 |       72 | 49.92%     | ok               |
|          35 | -26.76%  | 207.20%            | -43.49% |    -0.3  |       70 | 44.09%     | ok               |

## GE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 39.19%   | 214.67%            | -22.29% |     0.74 |       66 | 40.77%     | ok               |
|          45 | 28.68%   | 214.67%            | -25.68% |     0.58 |       74 | 43.59%     | ok               |
|          20 | 23.96%   | 214.67%            | -26.63% |     0.48 |       69 | 57.57%     | ok               |
|          35 | 18.40%   | 214.67%            | -27.11% |     0.41 |       80 | 49.08%     | ok               |
|          40 | 17.50%   | 214.67%            | -26.97% |     0.41 |       76 | 45.26%     | ok               |

## GLD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | 32.74%   | 102.92%            | -14.61% |     0.78 |       46 | 47.92%     | ok               |
|          20 | 30.76%   | 102.92%            | -14.61% |     0.74 |       48 | 49.25%     | ok               |
|          30 | 26.42%   | 102.92%            | -16.63% |     0.66 |       48 | 46.76%     | ok               |
|          15 | 22.75%   | 102.92%            | -17.54% |     0.56 |       50 | 53.41%     | ok               |
|          35 | 20.01%   | 102.92%            | -17.29% |     0.54 |       52 | 45.76%     | ok               |

## GOOGL Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 80.35%   | 149.36%            | -19.12% |     1.22 |       63 | 48.42%     | ok               |
|          25 | 81.59%   | 149.36%            | -19.76% |     1.19 |       55 | 55.41%     | ok               |
|          30 | 79.31%   | 149.36%            | -20.41% |     1.18 |       59 | 53.08%     | ok               |
|          45 | 64.33%   | 149.36%            | -15.05% |     1.11 |       56 | 41.60%     | ok               |
|          40 | 60.75%   | 149.36%            | -20.80% |     1.04 |       52 | 43.26%     | ok               |

## GRT-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 23.67%   | -88.30%            | -30.00% |     0.48 |       38 | 20.50%     | ok               |
|          15 | -1.79%   | -88.30%            | -49.67% |     0.24 |       75 | 61.11%     | ok               |
|          20 | -5.20%   | -88.30%            | -46.47% |     0.19 |       83 | 55.56%     | ok               |
|          45 | -3.91%   | -88.30%            | -48.76% |     0.12 |       46 | 25.67%     | ok               |
|          35 | -7.45%   | -88.30%            | -49.87% |     0.1  |       58 | 34.87%     | ok               |

## GS Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 21.11%   | 171.85%            | -20.56% |     0.47 |       74 | 61.06%     | ok               |
|          20 | 4.59%    | 171.85%            | -23.19% |     0.19 |       74 | 57.07%     | ok               |
|          40 | 0.08%    | 171.85%            | -17.88% |     0.09 |       72 | 45.26%     | ok               |
|          25 | -0.70%   | 171.85%            | -23.32% |     0.09 |       74 | 54.58%     | ok               |
|          30 | -2.38%   | 171.85%            | -22.13% |     0.05 |       76 | 52.08%     | ok               |

## HD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -8.50%   | -5.98%             | -18.58% |    -0.15 |       73 | 44.43%     | ok               |
|          25 | -9.21%   | -5.98%             | -19.40% |    -0.17 |       72 | 46.42%     | ok               |
|          45 | -10.76%  | -5.98%             | -19.30% |    -0.3  |       58 | 28.79%     | ok               |
|          35 | -14.52%  | -5.98%             | -22.43% |    -0.36 |       80 | 40.43%     | ok               |
|          40 | -13.27%  | -5.98%             | -19.06% |    -0.36 |       84 | 34.11%     | ok               |

## HON Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -13.43%  | 14.91%             | -21.17% |    -0.4  |       72 | 31.78%     | ok               |
|          45 | -15.16%  | 14.91%             | -19.99% |    -0.43 |       74 | 36.77%     | ok               |
|          40 | -23.52%  | 14.91%             | -26.29% |    -0.66 |       76 | 41.10%     | ok               |
|          35 | -26.77%  | 14.91%             | -29.07% |    -0.75 |       91 | 47.59%     | ok               |
|          30 | -29.10%  | 14.91%             | -31.48% |    -0.8  |       94 | 52.75%     | ok               |

## HYG Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -7.49%   | 4.04%              | -7.49%  |    -0.9  |       70 | 29.62%     | ok               |
|          45 | -8.18%   | 4.04%              | -8.21%  |    -1.02 |       66 | 26.46%     | ok               |
|          30 | -9.05%   | 4.04%              | -9.59%  |    -1.05 |       79 | 34.44%     | ok               |
|          15 | -9.81%   | 4.04%              | -10.16% |    -1.06 |       88 | 41.76%     | ok               |
|          20 | -9.84%   | 4.04%              | -10.45% |    -1.1  |       88 | 39.43%     | ok               |

## IBIT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 53.73%   | -7.31%             | -17.37% |     1.07 |       22 | 22.64%     | ok               |
|          15 | 61.53%   | -7.31%             | -19.20% |     1.01 |       38 | 39.86%     | ok               |
|          45 | 44.27%   | -7.31%             | -17.37% |     0.91 |       26 | 24.06%     | ok               |
|          40 | 38.04%   | -7.31%             | -17.78% |     0.81 |       26 | 25.94%     | ok               |
|          30 | 33.09%   | -7.31%             | -18.95% |     0.7  |       32 | 32.31%     | ok               |

## IBM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 22.77%   | 64.43%             | -28.20% |     0.48 |       92 | 62.06%     | ok               |
|          30 | 8.93%    | 64.43%             | -27.54% |     0.27 |       78 | 49.75%     | ok               |
|          20 | 4.13%    | 64.43%             | -34.12% |     0.19 |       76 | 54.41%     | ok               |
|          35 | 4.18%    | 64.43%             | -27.54% |     0.19 |       74 | 45.26%     | ok               |
|          50 | 2.84%    | 64.43%             | -22.50% |     0.15 |       54 | 32.61%     | ok               |

## ICP-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 8.36%    | -70.92%            | -38.23% |     0.3  |       66 | 29.50%     | ok               |
|          40 | 2.64%    | -70.92%            | -32.85% |     0.23 |       60 | 25.10%     | ok               |
|          30 | -4.40%   | -70.92%            | -51.29% |     0.21 |       81 | 35.63%     | ok               |
|          50 | -9.38%   | -70.92%            | -43.65% |     0.05 |       38 | 15.13%     | ok               |
|          20 | -38.34%  | -70.92%            | -58.71% |    -0.09 |       90 | 46.36%     | ok               |

## IEF Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -6.92%   | -0.03%             | -9.79%  |    -0.82 |       70 | 42.26%     | ok               |
|          15 | -7.48%   | -0.03%             | -10.52% |    -0.88 |       69 | 43.76%     | ok               |
|          40 | -8.39%   | -0.03%             | -9.67%  |    -1.31 |       60 | 24.79%     | ok               |
|          45 | -8.07%   | -0.03%             | -9.73%  |    -1.33 |       50 | 22.80%     | ok               |
|          25 | -10.50%  | -0.03%             | -11.19% |    -1.34 |       76 | 39.43%     | ok               |

## IEMG Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -0.10%   | 63.11%             | -13.91% |     0.05 |       52 | 34.44%     | ok               |
|          35 | -0.32%   | 63.11%             | -22.13% |     0.05 |       63 | 42.60%     | ok               |
|          45 | -0.91%   | 63.11%             | -14.92% |     0.02 |       48 | 36.94%     | ok               |
|          40 | -2.44%   | 63.11%             | -18.43% |    -0.03 |       60 | 39.93%     | ok               |
|          25 | -4.72%   | 63.11%             | -25.58% |    -0.09 |       59 | 45.42%     | ok               |

## INJ-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -16.04%  | -70.30%            | -56.91% |    -0.02 |       44 | 22.22%     | ok               |
|          35 | -22.55%  | -70.30%            | -61.19% |    -0.04 |       58 | 31.61%     | ok               |
|          50 | -25.16%  | -70.30%            | -52.76% |    -0.19 |       48 | 19.16%     | ok               |
|          40 | -30.34%  | -70.30%            | -59.56% |    -0.21 |       48 | 27.97%     | ok               |
|          20 | -50.45%  | -70.30%            | -79.76% |    -0.36 |       78 | 46.36%     | ok               |

## INTC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 86.84%   | 155.42%            | -53.65% |     0.76 |       82 | 60.57%     | ok               |
|          45 | 76.11%   | 155.42%            | -49.32% |     0.74 |       60 | 34.28%     | ok               |
|          25 | 75.50%   | 155.42%            | -56.41% |     0.72 |       75 | 51.58%     | ok               |
|          20 | 76.16%   | 155.42%            | -52.47% |     0.71 |       80 | 56.41%     | ok               |
|          40 | 70.33%   | 155.42%            | -55.86% |     0.7  |       68 | 38.60%     | ok               |

## INTU Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -0.39%   | -57.37%            | -40.80% |     0.11 |       71 | 27.79%     | ok               |
|          45 | -3.80%   | -57.37%            | -42.69% |     0.05 |       69 | 31.95%     | ok               |
|          40 | -10.93%  | -57.37%            | -46.52% |    -0.08 |       71 | 35.11%     | ok               |
|          15 | -18.07%  | -57.37%            | -46.90% |    -0.18 |       81 | 50.58%     | ok               |
|          35 | -17.11%  | -57.37%            | -48.24% |    -0.19 |       73 | 38.94%     | ok               |

## ITA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 0.84%    | 93.09%             | -21.48% |     0.09 |       76 | 38.27%     | ok               |
|          15 | -2.59%   | 93.09%             | -28.17% |     0.02 |       84 | 59.90%     | ok               |
|          30 | -2.65%   | 93.09%             | -23.75% |    -0    |       72 | 48.25%     | ok               |
|          35 | -4.73%   | 93.09%             | -23.16% |    -0.07 |       76 | 46.59%     | ok               |
|          40 | -5.82%   | 93.09%             | -20.58% |    -0.11 |       78 | 43.09%     | ok               |

## IWM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 8.60%    | 50.80%             | -14.08% |     0.39 |       42 | 31.28%     | ok               |
|          30 | 9.40%    | 50.80%             | -12.83% |     0.39 |       48 | 35.77%     | ok               |
|          25 | 9.50%    | 50.80%             | -13.55% |     0.39 |       50 | 36.94%     | ok               |
|          35 | 8.35%    | 50.80%             | -14.11% |     0.36 |       48 | 33.61%     | ok               |
|          20 | 5.19%    | 50.80%             | -14.08% |     0.24 |       60 | 37.94%     | ok               |

## JNJ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 26.76%   | 68.34%             | -10.57% |     1.04 |       54 | 37.60%     | ok               |
|          45 | 16.65%   | 68.34%             | -13.35% |     0.66 |       56 | 42.60%     | ok               |
|          15 | 17.55%   | 68.34%             | -18.02% |     0.59 |       68 | 56.91%     | ok               |
|          40 | 14.11%   | 68.34%             | -14.77% |     0.55 |       62 | 46.76%     | ok               |
|          20 | 13.57%   | 68.34%             | -17.61% |     0.5  |       72 | 53.58%     | ok               |

## JPM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 21.36%   | 89.73%             | -15.90% |     0.69 |       52 | 41.60%     | ok               |
|          45 | 9.83%    | 89.73%             | -21.91% |     0.35 |       54 | 44.59%     | ok               |
|          40 | -4.68%   | 89.73%             | -28.47% |    -0.06 |       66 | 47.09%     | ok               |
|          20 | -11.79%  | 89.73%             | -33.59% |    -0.18 |       84 | 58.40%     | ok               |
|          35 | -10.00%  | 89.73%             | -27.43% |    -0.2  |       72 | 50.75%     | ok               |

## KO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 28.93%   | 40.52%             | -8.07%  |     1.03 |       49 | 37.77%     | ok               |
|          35 | 24.98%   | 40.52%             | -8.07%  |     0.93 |       52 | 36.44%     | ok               |
|          40 | 22.37%   | 40.52%             | -9.28%  |     0.9  |       54 | 33.28%     | ok               |
|          25 | 23.60%   | 40.52%             | -9.37%  |     0.86 |       55 | 40.43%     | ok               |
|          50 | 14.81%   | 40.52%             | -11.40% |     0.68 |       36 | 26.79%     | ok               |

## LDO-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 33.16%   | -82.40%            | -43.48% |     0.53 |       83 | 51.72%     | ok               |
|          20 | 20.87%   | -82.40%            | -43.71% |     0.45 |       85 | 47.13%     | ok               |
|          50 | 13.59%   | -82.40%            | -48.77% |     0.35 |       46 | 16.67%     | ok               |
|          30 | 8.74%    | -82.40%            | -58.32% |     0.34 |       72 | 37.74%     | ok               |
|          35 | -0.97%   | -82.40%            | -63.16% |     0.24 |       74 | 30.65%     | ok               |

## LIN Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 2.63%    | 26.77%             | -23.68% |     0.15 |       64 | 49.75%     | ok               |
|          25 | 2.35%    | 26.77%             | -22.01% |     0.14 |       63 | 41.76%     | ok               |
|          20 | 0.15%    | 26.77%             | -23.00% |     0.07 |       62 | 44.93%     | ok               |
|          35 | -1.35%   | 26.77%             | -21.18% |     0.01 |       62 | 32.45%     | ok               |
|          30 | -1.98%   | 26.77%             | -21.53% |    -0.01 |       66 | 38.94%     | ok               |

## LINK-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -18.18%  | -64.86%            | -50.48% |     0.04 |       72 | 41.76%     | ok               |
|          45 | -16.95%  | -64.86%            | -38.56% |    -0    |       50 | 26.25%     | ok               |
|          50 | -16.55%  | -64.86%            | -36.98% |    -0.02 |       40 | 20.88%     | ok               |
|          35 | -27.53%  | -64.86%            | -49.56% |    -0.1  |       60 | 36.40%     | ok               |
|          40 | -31.51%  | -64.86%            | -50.91% |    -0.19 |       56 | 30.65%     | ok               |

## LLY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 7.14%    | 63.64%             | -38.23% |     0.24 |       46 | 37.60%     | ok               |
|          15 | -0.86%   | 63.64%             | -48.12% |     0.13 |       63 | 61.23%     | ok               |
|          45 | -4.92%   | 63.64%             | -42.66% |     0.02 |       54 | 41.10%     | ok               |
|          20 | -16.82%  | 63.64%             | -51.34% |    -0.15 |       72 | 56.24%     | ok               |
|          25 | -18.20%  | 63.64%             | -53.47% |    -0.18 |       68 | 53.58%     | ok               |

## LRCX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -5.91%   | 273.24%            | -60.45% |     0.13 |       83 | 55.24%     | ok               |
|          50 | -11.02%  | 273.24%            | -50.39% |     0.02 |       80 | 36.94%     | ok               |
|          40 | -13.69%  | 273.24%            | -56.86% |     0.01 |       72 | 42.76%     | ok               |
|          35 | -19.30%  | 273.24%            | -61.76% |    -0.06 |       80 | 44.76%     | ok               |
|          20 | -21.53%  | 273.24%            | -67.48% |    -0.08 |       89 | 50.75%     | ok               |

## LTC-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -12.22%  | -59.17%            | -44.78% |    -0    |       56 | 31.80%     | ok               |
|          35 | -22.47%  | -59.17%            | -54.86% |    -0.13 |       66 | 42.91%     | ok               |
|          30 | -34.00%  | -59.17%            | -53.76% |    -0.29 |       66 | 48.47%     | ok               |
|          40 | -31.40%  | -59.17%            | -56.10% |    -0.3  |       58 | 38.12%     | ok               |
|          25 | -36.79%  | -59.17%            | -54.26% |    -0.33 |       74 | 50.96%     | ok               |

## MCD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 2.85%    | -3.09%             | -9.22%  |     0.19 |       42 | 20.63%     | ok               |
|          30 | -2.55%   | -3.09%             | -18.81% |    -0.05 |       75 | 38.10%     | ok               |
|          25 | -3.59%   | -3.09%             | -20.47% |    -0.09 |       75 | 40.77%     | ok               |
|          35 | -7.68%   | -3.09%             | -15.45% |    -0.29 |       67 | 34.44%     | ok               |
|          40 | -7.95%   | -3.09%             | -16.86% |    -0.33 |       71 | 28.79%     | ok               |

## META Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -6.64%   | 31.08%             | -31.03% |    -0.03 |       66 | 38.10%     | ok               |
|          40 | -16.91%  | 31.08%             | -35.11% |    -0.24 |       66 | 41.10%     | ok               |
|          50 | -20.90%  | 31.08%             | -34.00% |    -0.38 |       70 | 34.28%     | ok               |
|          25 | -25.11%  | 31.08%             | -39.84% |    -0.38 |       67 | 51.75%     | ok               |
|          30 | -27.11%  | 31.08%             | -38.96% |    -0.44 |       72 | 48.59%     | ok               |

## MPC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 12.33%   | 65.22%             | -23.96% |     0.34 |       52 | 37.77%     | ok               |
|          45 | 5.20%    | 65.22%             | -25.09% |     0.21 |       58 | 41.43%     | ok               |
|          40 | 3.61%    | 65.22%             | -25.70% |     0.18 |       60 | 43.76%     | ok               |
|          35 | 0.41%    | 65.22%             | -35.90% |     0.13 |       68 | 46.26%     | ok               |
|          30 | -15.39%  | 65.22%             | -44.76% |    -0.17 |       71 | 49.08%     | ok               |

## MRK Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -20.58%  | 0.45%              | -30.12% |    -0.38 |       87 | 55.57%     | ok               |
|          25 | -20.19%  | 0.45%              | -31.07% |    -0.41 |       72 | 47.59%     | ok               |
|          20 | -24.11%  | 0.45%              | -29.59% |    -0.51 |       77 | 50.92%     | ok               |
|          45 | -23.03%  | 0.45%              | -26.02% |    -0.61 |       57 | 33.78%     | ok               |
|          50 | -22.68%  | 0.45%              | -25.69% |    -0.65 |       56 | 30.78%     | ok               |

## MS Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -2.40%   | 159.70%            | -19.99% |     0.02 |       72 | 41.60%     | ok               |
|          15 | -9.91%   | 159.70%            | -22.02% |    -0.12 |       77 | 58.90%     | ok               |
|          20 | -10.02%  | 159.70%            | -25.68% |    -0.14 |       81 | 55.07%     | ok               |
|          35 | -9.20%   | 159.70%            | -25.26% |    -0.14 |       76 | 46.26%     | ok               |
|          30 | -14.84%  | 159.70%            | -27.79% |    -0.29 |       81 | 50.25%     | ok               |

## MSFT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -22.61%  | -5.66%             | -25.26% |    -0.64 |       68 | 34.61%     | ok               |
|          50 | -24.02%  | -5.66%             | -26.34% |    -0.71 |       64 | 29.62%     | ok               |
|          35 | -34.88%  | -5.66%             | -35.38% |    -0.94 |       75 | 43.26%     | ok               |
|          40 | -34.26%  | -5.66%             | -34.77% |    -0.96 |       71 | 38.10%     | ok               |
|          25 | -38.06%  | -5.66%             | -40.01% |    -0.99 |       87 | 50.92%     | ok               |

## MU Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 448.67%  | 1063.74%           | -61.96% |     1.59 |       47 | 67.89%     | ok               |
|          25 | 357.11%  | 1063.74%           | -67.90% |     1.51 |       47 | 61.56%     | ok               |
|          20 | 318.50%  | 1063.74%           | -67.25% |     1.41 |       53 | 63.73%     | ok               |
|          40 | 288.27%  | 1063.74%           | -64.30% |     1.4  |       56 | 55.07%     | ok               |
|          30 | 270.20%  | 1063.74%           | -68.76% |     1.34 |       51 | 59.90%     | ok               |

## NEAR-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 100.21%  | -49.77%            | -43.08% |     0.98 |       44 | 23.75%     | ok               |
|          50 | 68.35%   | -49.77%            | -48.72% |     0.81 |       40 | 18.77%     | ok               |
|          40 | 70.68%   | -49.77%            | -52.22% |     0.8  |       44 | 27.78%     | ok               |
|          35 | 36.41%   | -49.77%            | -59.02% |     0.55 |       64 | 32.18%     | ok               |
|          30 | 9.87%    | -49.77%            | -60.10% |     0.34 |       83 | 40.42%     | ok               |

## NEM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 3.24%    | 190.89%            | -29.41% |     0.21 |       62 | 61.40%     | ok               |
|          20 | -7.81%   | 190.89%            | -30.47% |     0.07 |       72 | 56.91%     | ok               |
|          25 | -21.27%  | 190.89%            | -37.89% |    -0.14 |       68 | 54.74%     | ok               |
|          50 | -23.65%  | 190.89%            | -32.97% |    -0.25 |       56 | 40.77%     | ok               |
|          30 | -31.13%  | 190.89%            | -38.49% |    -0.33 |       72 | 53.08%     | ok               |

## NFLX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 55.70%   | 36.32%             | -11.94% |     1.1  |       46 | 46.76%     | ok               |
|          50 | 49.43%   | 36.32%             | -16.28% |     1.07 |       48 | 39.10%     | ok               |
|          35 | 47.69%   | 36.32%             | -18.30% |     0.93 |       60 | 50.25%     | ok               |
|          45 | 38.86%   | 36.32%             | -15.48% |     0.85 |       52 | 43.09%     | ok               |
|          15 | 43.06%   | 36.32%             | -26.59% |     0.78 |       67 | 65.06%     | ok               |

## NKE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -33.86%  | -59.15%            | -50.44% |    -0.42 |       93 | 52.58%     | ok               |
|          40 | -26.46%  | -59.15%            | -31.19% |    -0.5  |       63 | 30.12%     | ok               |
|          15 | -38.38%  | -59.15%            | -55.52% |    -0.51 |       91 | 56.91%     | ok               |
|          25 | -45.09%  | -59.15%            | -52.84% |    -0.79 |       91 | 48.59%     | ok               |
|          35 | -39.10%  | -59.15%            | -43.08% |    -0.8  |       75 | 37.10%     | ok               |

## NOW Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 14.05%   | -30.35%            | -26.36% |     0.33 |       79 | 51.58%     | ok               |
|          30 | 9.97%    | -30.35%            | -28.41% |     0.28 |       82 | 45.59%     | ok               |
|          15 | 6.47%    | -30.35%            | -26.36% |     0.25 |       88 | 54.74%     | ok               |
|          25 | 3.71%    | -30.35%            | -25.70% |     0.21 |       74 | 48.92%     | ok               |
|          35 | 0.26%    | -30.35%            | -27.43% |     0.15 |       83 | 40.10%     | ok               |

## NVDA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -1.32%   | 125.26%            | -35.26% |     0.14 |       70 | 47.59%     | ok               |
|          25 | -6.89%   | 125.26%            | -33.22% |     0.07 |       68 | 50.62%     | ok               |
|          20 | -10.70%  | 125.26%            | -40.59% |     0.03 |       69 | 55.44%     | ok               |
|          35 | -14.66%  | 125.26%            | -41.25% |    -0.08 |       78 | 44.74%     | ok               |
|          50 | -14.29%  | 125.26%            | -40.84% |    -0.11 |       56 | 32.09%     | ok               |

## OP-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 27.06%   | -91.51%            | -36.11% |     0.51 |       30 | 11.11%     | ok               |
|          45 | 8.56%    | -91.51%            | -53.32% |     0.29 |       34 | 15.90%     | ok               |
|          40 | 0.59%    | -91.51%            | -60.08% |     0.22 |       46 | 24.14%     | ok               |
|          35 | -15.84%  | -91.51%            | -63.95% |     0.03 |       52 | 27.39%     | ok               |
|          30 | -20.09%  | -91.51%            | -70.11% |     0.01 |       68 | 33.72%     | ok               |

## ORCL Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 208.04%  | 23.58%             | -29.32% |     1.28 |       74 | 65.22%     | ok               |
|          25 | 131.08%  | 23.58%             | -27.76% |     1.02 |       75 | 57.74%     | ok               |
|          20 | 127.11%  | 23.58%             | -29.32% |     1    |       77 | 60.90%     | ok               |
|          35 | 98.24%   | 23.58%             | -31.95% |     0.89 |       66 | 49.42%     | ok               |
|          30 | 98.42%   | 23.58%             | -29.47% |     0.89 |       72 | 53.58%     | ok               |

## OXY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 2.35%    | -6.98%             | -31.37% |     0.16 |       67 | 43.59%     | ok               |
|          50 | 0.83%    | -6.98%             | -30.54% |     0.12 |       36 | 27.79%     | ok               |
|          35 | -1.87%   | -6.98%             | -31.78% |     0.08 |       68 | 39.10%     | ok               |
|          40 | -4.27%   | -6.98%             | -33.45% |     0.03 |       56 | 35.11%     | ok               |
|          25 | -10.60%  | -6.98%             | -40.06% |    -0.07 |       73 | 47.59%     | ok               |

## PEP Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 11.74%   | -15.61%            | -11.62% |     0.53 |       44 | 26.79%     | ok               |
|          45 | 2.18%    | -15.61%            | -14.22% |     0.14 |       64 | 31.11%     | ok               |
|          35 | -1.13%   | -15.61%            | -21.42% |     0.03 |       83 | 42.10%     | ok               |
|          40 | -1.01%   | -15.61%            | -18.04% |     0.02 |       76 | 37.10%     | ok               |
|          30 | -6.85%   | -15.61%            | -21.35% |    -0.14 |       79 | 48.75%     | ok               |

## PEPE-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -7.44%   | -76.56%            | -64.84% |     0.28 |       80 | 60.15%     | ok               |
|          30 | 0.11%    | -76.56%            | -57.66% |     0.28 |       79 | 44.83%     | ok               |
|          35 | -5.60%   | -76.56%            | -51.35% |     0.2  |       64 | 39.46%     | ok               |
|          25 | -18.07%  | -76.56%            | -53.88% |     0.12 |       85 | 50.00%     | ok               |
|          20 | -27.83%  | -76.56%            | -64.07% |     0.04 |       86 | 56.51%     | ok               |

## PFE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -26.34%  | -10.83%            | -27.90% |    -1    |       52 | 18.97%     | ok               |
|          35 | -34.49%  | -10.83%            | -36.37% |    -1.15 |       84 | 31.28%     | ok               |
|          50 | -28.16%  | -10.83%            | -29.00% |    -1.2  |       40 | 15.14%     | ok               |
|          40 | -33.21%  | -10.83%            | -34.64% |    -1.21 |       74 | 23.96%     | ok               |
|          30 | -39.13%  | -10.83%            | -40.87% |    -1.25 |       77 | 35.44%     | ok               |

## PG Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -5.99%   | -5.04%             | -20.08% |    -0.2  |       58 | 34.44%     | ok               |
|          35 | -9.20%   | -5.04%             | -18.99% |    -0.32 |       66 | 37.94%     | ok               |
|          45 | -15.18%  | -5.04%             | -22.41% |    -0.64 |       58 | 31.95%     | ok               |
|          30 | -17.45%  | -5.04%             | -24.53% |    -0.65 |       68 | 41.10%     | ok               |
|          25 | -18.44%  | -5.04%             | -25.40% |    -0.68 |       78 | 42.26%     | ok               |

## PM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | -0.86%   | 109.74%            | -32.20% |     0.07 |       88 | 52.58%     | ok               |
|          20 | -4.54%   | 109.74%            | -31.89% |     0    |       87 | 61.40%     | ok               |
|          30 | -4.96%   | 109.74%            | -33.68% |    -0.01 |       83 | 56.41%     | ok               |
|          50 | -6.95%   | 109.74%            | -35.70% |    -0.09 |       74 | 42.10%     | ok               |
|          40 | -8.33%   | 109.74%            | -37.94% |    -0.12 |       80 | 48.25%     | ok               |

## POL-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | 49.97%   | -77.79%            | -46.72% |     0.65 |       64 | 57.66%     | ok               |
|          30 | 47.25%   | -77.79%            | -46.45% |     0.65 |       79 | 49.81%     | ok               |
|          20 | 38.43%   | -77.79%            | -52.88% |     0.56 |       70 | 61.88%     | ok               |
|          15 | 23.53%   | -77.79%            | -58.42% |     0.45 |       72 | 66.67%     | ok               |
|          50 | 6.12%    | -77.79%            | -22.86% |     0.24 |       50 | 20.11%     | ok               |

## QCOM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -1.44%   | 24.34%             | -54.50% |     0.15 |       73 | 47.92%     | ok               |
|          35 | -1.99%   | 24.34%             | -50.58% |     0.14 |       79 | 43.76%     | ok               |
|          20 | -5.44%   | 24.34%             | -54.38% |     0.11 |       69 | 50.75%     | ok               |
|          30 | -13.10%  | 24.34%             | -56.59% |    -0.01 |       75 | 46.26%     | ok               |
|          15 | -21.15%  | 24.34%             | -57.94% |    -0.1  |       73 | 53.91%     | ok               |

## QQQ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | 22.96%   | 66.01%             | -12.88% |     0.62 |       59 | 47.59%     | ok               |
|          15 | 23.49%   | 66.01%             | -14.17% |     0.59 |       63 | 53.08%     | ok               |
|          30 | 18.95%   | 66.01%             | -12.88% |     0.55 |       64 | 44.76%     | ok               |
|          20 | 19.99%   | 66.01%             | -12.98% |     0.54 |       67 | 50.25%     | ok               |
|          35 | 6.79%    | 66.01%             | -18.29% |     0.26 |       70 | 41.10%     | ok               |

## RENDER-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 47.01%   | -63.10%            | -43.43% |     0.62 |       88 | 54.56%     | ok               |
|          15 | 34.37%   | -63.10%            | -44.59% |     0.55 |       86 | 57.74%     | ok               |
|          25 | 15.90%   | -63.10%            | -40.60% |     0.42 |       90 | 50.20%     | ok               |
|          30 | -19.07%  | -63.10%            | -45.00% |     0.1  |       98 | 43.45%     | ok               |
|          35 | -31.74%  | -63.10%            | -41.33% |    -0.12 |       84 | 35.12%     | ok               |

## RTX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 32.35%   | 115.16%            | -18.66% |     0.75 |       78 | 56.24%     | ok               |
|          25 | 27.65%   | 115.16%            | -18.59% |     0.67 |       64 | 52.75%     | ok               |
|          50 | 21.69%   | 115.16%            | -18.42% |     0.65 |       60 | 41.93%     | ok               |
|          35 | 23.06%   | 115.16%            | -18.00% |     0.65 |       56 | 49.75%     | ok               |
|          30 | 25.71%   | 115.16%            | -16.99% |     0.64 |       58 | 51.58%     | ok               |

## SBUX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -14.13%  | 10.65%             | -23.51% |    -0.27 |       58 | 33.61%     | ok               |
|          45 | -14.12%  | 10.65%             | -25.39% |    -0.3  |       66 | 29.12%     | ok               |
|          30 | -18.32%  | 10.65%             | -27.45% |    -0.34 |       62 | 39.10%     | ok               |
|          35 | -19.87%  | 10.65%             | -25.85% |    -0.39 |       56 | 36.44%     | ok               |
|          25 | -25.97%  | 10.65%             | -32.29% |    -0.45 |       62 | 41.60%     | ok               |

## SCHW Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 8.76%    | 62.18%             | -16.53% |     0.32 |       56 | 33.94%     | ok               |
|          50 | 4.56%    | 62.18%             | -13.28% |     0.21 |       50 | 31.45%     | ok               |
|          25 | -1.13%   | 62.18%             | -28.76% |     0.07 |       63 | 48.92%     | ok               |
|          40 | -2.52%   | 62.18%             | -23.35% |     0.01 |       64 | 36.94%     | ok               |
|          20 | -4.67%   | 62.18%             | -29.24% |    -0.01 |       71 | 51.41%     | ok               |

## SHIB-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -9.18%   | -74.84%            | -49.21% |     0.14 |       80 | 69.92%     | ok               |
|          20 | -22.22%  | -74.84%            | -46.92% |    -0.02 |       81 | 64.75%     | ok               |
|          25 | -22.94%  | -74.84%            | -43.85% |    -0.05 |       77 | 59.77%     | ok               |
|          35 | -23.32%  | -74.84%            | -53.32% |    -0.11 |       66 | 46.36%     | ok               |
|          40 | -27.53%  | -74.84%            | -50.74% |    -0.2  |       56 | 38.70%     | ok               |

## SHY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd    |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:-------|---------:|---------:|:-----------|:-----------------|
|          30 | -2.24%   | 0.34%              | -2.85% |    -0.79 |       48 | 34.28%     | ok               |
|          35 | -2.36%   | 0.34%              | -3.27% |    -0.84 |       50 | 32.45%     | ok               |
|          40 | -2.47%   | 0.34%              | -3.33% |    -0.89 |       50 | 30.62%     | ok               |
|          45 | -2.45%   | 0.34%              | -3.23% |    -0.9  |       48 | 27.45%     | ok               |
|          50 | -2.62%   | 0.34%              | -3.40% |    -1.01 |       44 | 24.63%     | ok               |

## SKY-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -28.56%  | -5.76%             | -43.98% |    -0.34 |       70 | 40.49%     | ok               |
|          15 | -32.92%  | -5.76%             | -56.39% |    -0.35 |       60 | 50.56%     | ok               |
|          25 | -32.22%  | -5.76%             | -48.09% |    -0.4  |       65 | 44.07%     | ok               |
|          20 | -42.55%  | -5.76%             | -58.40% |    -0.59 |       62 | 47.65%     | ok               |
|          35 | -39.77%  | -5.76%             | -49.68% |    -0.69 |       64 | 34.23%     | ok               |

## SLB Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 20.74%   | -0.32%             | -20.46% |     0.51 |       54 | 32.95%     | ok               |
|          40 | 19.19%   | -0.32%             | -23.07% |     0.47 |       46 | 36.77%     | ok               |
|          50 | -4.32%   | -0.32%             | -30.82% |    -0.02 |       52 | 28.45%     | ok               |
|          35 | -10.73%  | -0.32%             | -41.81% |    -0.12 |       74 | 44.76%     | ok               |
|          30 | -24.72%  | -0.32%             | -54.13% |    -0.41 |       77 | 51.41%     | ok               |

## SLV Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 69.68%   | 161.53%            | -31.82% |     0.87 |       58 | 35.77%     | ok               |
|          50 | 67.45%   | 161.53%            | -34.10% |     0.86 |       52 | 34.78%     | ok               |
|          40 | 67.66%   | 161.53%            | -31.93% |     0.85 |       64 | 37.94%     | ok               |
|          35 | 54.39%   | 161.53%            | -36.89% |     0.74 |       66 | 40.10%     | ok               |
|          30 | 49.79%   | 161.53%            | -42.66% |     0.69 |       58 | 42.43%     | ok               |

## SMH Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 112.24%  | 197.54%            | -30.17% |     1.3  |       47 | 51.58%     | ok               |
|          35 | 89.94%   | 197.54%            | -34.36% |     1.17 |       54 | 47.42%     | ok               |
|          25 | 89.81%   | 197.54%            | -32.94% |     1.15 |       46 | 50.42%     | ok               |
|          30 | 87.57%   | 197.54%            | -33.99% |     1.14 |       48 | 48.75%     | ok               |
|          45 | 73.92%   | 197.54%            | -32.75% |     1.09 |       52 | 41.60%     | ok               |

## SNX-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | -2.15%   | -82.72%            | -30.08% |     0.21 |       62 | 30.08%     | ok               |
|          20 | -8.06%   | -82.72%            | -43.20% |     0.19 |       71 | 47.70%     | ok               |
|          30 | -14.97%  | -82.72%            | -34.76% |     0.08 |       58 | 36.97%     | ok               |
|          40 | -12.24%  | -82.72%            | -34.88% |     0.04 |       50 | 24.71%     | ok               |
|          15 | -38.08%  | -82.72%            | -47.56% |    -0.14 |       81 | 52.30%     | ok               |

## SOL-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 5.33%    | -64.32%            | -51.50% |     0.29 |       60 | 37.55%     | ok               |
|          25 | -21.37%  | -64.32%            | -52.40% |     0.04 |       72 | 56.32%     | ok               |
|          45 | -16.11%  | -64.32%            | -59.86% |     0.03 |       62 | 31.80%     | ok               |
|          15 | -26.23%  | -64.32%            | -59.14% |     0    |       72 | 63.03%     | ok               |
|          35 | -23.71%  | -64.32%            | -61.91% |    -0.01 |       74 | 45.02%     | ok               |

## SOXX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 90.32%   | 173.99%            | -40.27% |     1.1  |       55 | 50.08%     | ok               |
|          35 | 86.33%   | 173.99%            | -38.63% |     1.09 |       59 | 45.26%     | ok               |
|          25 | 86.68%   | 173.99%            | -41.42% |     1.07 |       53 | 49.75%     | ok               |
|          15 | 85.55%   | 173.99%            | -39.35% |     1.03 |       68 | 52.91%     | ok               |
|          30 | 76.19%   | 173.99%            | -41.89% |     0.99 |       57 | 47.59%     | ok               |

## SPY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 15.72%   | 50.87%             | -14.25% |     0.55 |       61 | 53.91%     | ok               |
|          15 | 14.13%   | 50.87%             | -16.80% |     0.49 |       70 | 57.07%     | ok               |
|          25 | 8.51%    | 50.87%             | -15.22% |     0.34 |       61 | 52.91%     | ok               |
|          30 | 3.93%    | 50.87%             | -16.47% |     0.2  |       64 | 50.08%     | ok               |
|          35 | 3.31%    | 50.87%             | -16.72% |     0.18 |       60 | 47.09%     | ok               |

## SUSHI-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -24.39%  | -83.36%            | -40.79% |    -0.2  |       52 | 14.56%     | ok               |
|          45 | -59.07%  | -83.36%            | -64.69% |    -0.78 |       56 | 18.01%     | ok               |
|          40 | -61.97%  | -83.36%            | -68.54% |    -0.78 |       63 | 24.52%     | ok               |
|          35 | -69.84%  | -83.36%            | -76.44% |    -0.93 |       80 | 30.08%     | ok               |
|          15 | -80.30%  | -83.36%            | -80.30% |    -1.03 |       89 | 47.13%     | ok               |

## T Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 65.08%   | 24.97%             | -18.13% |     1.22 |       56 | 56.74%     | ok               |
|          25 | 59.95%   | 24.97%             | -17.66% |     1.17 |       58 | 54.58%     | ok               |
|          15 | 56.06%   | 24.97%             | -15.08% |     1.07 |       65 | 60.57%     | ok               |
|          30 | 42.43%   | 24.97%             | -17.01% |     0.92 |       62 | 52.58%     | ok               |
|          35 | 27.78%   | 24.97%             | -14.49% |     0.69 |       64 | 49.08%     | ok               |

## TGT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -12.32%  | -9.37%             | -42.86% |    -0.13 |       81 | 46.76%     | ok               |
|          45 | -10.91%  | -9.37%             | -29.07% |    -0.18 |       52 | 29.12%     | ok               |
|          25 | -13.19%  | -9.37%             | -43.36% |    -0.18 |       63 | 41.76%     | ok               |
|          30 | -12.57%  | -9.37%             | -40.57% |    -0.18 |       58 | 38.94%     | ok               |
|          15 | -17.87%  | -9.37%             | -40.77% |    -0.24 |       71 | 51.41%     | ok               |

## TIA-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 2.90%    | -88.76%            | -46.58% |     0.22 |       52 | 18.58%     | ok               |
|          50 | 1.89%    | -88.76%            | -46.02% |     0.18 |       32 | 11.49%     | ok               |
|          35 | -14.76%  | -88.76%            | -49.70% |     0.07 |       66 | 30.84%     | ok               |
|          40 | -14.40%  | -88.76%            | -48.55% |     0.06 |       68 | 26.05%     | ok               |
|          15 | -57.93%  | -88.76%            | -61.13% |    -0.35 |       97 | 52.49%     | ok               |

## TLT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -14.12%  | -8.65%             | -14.86% |    -1.65 |       32 | 14.31%     | ok               |
|          30 | -21.58%  | -8.65%             | -21.75% |    -1.68 |       68 | 31.61%     | ok               |
|          40 | -18.63%  | -8.65%             | -18.63% |    -1.85 |       58 | 20.63%     | ok               |
|          35 | -21.08%  | -8.65%             | -21.08% |    -1.9  |       66 | 25.62%     | ok               |
|          15 | -27.33%  | -8.65%             | -27.64% |    -1.93 |       73 | 39.60%     | ok               |

## TMO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 41.93%   | -5.29%             | -8.17%  |     0.97 |       40 | 31.11%     | ok               |
|          45 | 37.81%   | -5.29%             | -10.13% |     0.85 |       46 | 35.94%     | ok               |
|          40 | 35.78%   | -5.29%             | -9.91%  |     0.8  |       49 | 40.43%     | ok               |
|          35 | 18.49%   | -5.29%             | -14.06% |     0.47 |       61 | 44.93%     | ok               |
|          30 | 12.40%   | -5.29%             | -18.85% |     0.35 |       59 | 49.42%     | ok               |

## TMUS Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 12.72%   | 11.56%             | -28.81% |     0.35 |       67 | 60.23%     | ok               |
|          30 | 8.57%    | 11.56%             | -25.11% |     0.28 |       68 | 48.25%     | ok               |
|          20 | 3.43%    | 11.56%             | -29.75% |     0.17 |       71 | 54.58%     | ok               |
|          25 | -0.01%   | 11.56%             | -30.90% |     0.1  |       73 | 50.75%     | ok               |
|          35 | -3.88%   | 11.56%             | -33.70% |     0.01 |       68 | 45.09%     | ok               |

## TRX-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 6.87%    | 43.66%             | -18.79% |     0.28 |       52 | 37.16%     | ok               |
|          30 | 0.99%    | 43.66%             | -22.90% |     0.12 |       72 | 49.04%     | ok               |
|          50 | 0.66%    | 43.66%             | -18.49% |     0.1  |       44 | 31.99%     | ok               |
|          35 | 0.16%    | 43.66%             | -21.77% |     0.09 |       68 | 45.79%     | ok               |
|          45 | -0.23%   | 43.66%             | -18.27% |     0.07 |       44 | 33.52%     | ok               |

## TSLA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 73.14%   | 114.14%            | -30.67% |     0.82 |       62 | 34.44%     | ok               |
|          50 | 56.12%   | 114.14%            | -32.60% |     0.73 |       64 | 29.78%     | ok               |
|          45 | 46.68%   | 114.14%            | -31.89% |     0.63 |       66 | 31.78%     | ok               |
|          35 | 32.37%   | 114.14%            | -37.58% |     0.5  |       71 | 37.10%     | ok               |
|          30 | 6.61%    | 114.14%            | -42.22% |     0.26 |       71 | 41.26%     | ok               |

## TXN Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 9.93%    | 92.11%             | -45.45% |     0.28 |       72 | 35.11%     | ok               |
|          20 | -0.10%   | 92.11%             | -38.49% |     0.15 |       62 | 59.90%     | ok               |
|          15 | -5.81%   | 92.11%             | -38.99% |     0.08 |       67 | 63.73%     | ok               |
|          35 | -5.39%   | 92.11%             | -43.28% |     0.05 |       78 | 50.25%     | ok               |
|          40 | -7.95%   | 92.11%             | -45.67% |     0.01 |       74 | 47.92%     | ok               |

## UNH Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 34.74%   | -17.66%            | -26.96% |     0.57 |       74 | 52.41%     | ok               |
|          15 | 35.24%   | -17.66%            | -32.14% |     0.56 |       74 | 67.22%     | ok               |
|          50 | 30.07%   | -17.66%            | -36.82% |     0.54 |       54 | 30.95%     | ok               |
|          35 | 31.07%   | -17.66%            | -28.32% |     0.53 |       66 | 47.25%     | ok               |
|          40 | 22.93%   | -17.66%            | -35.73% |     0.45 |       60 | 42.76%     | ok               |

## UNI-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -21.90%  | -67.23%            | -58.49% |    -0.05 |       58 | 26.25%     | ok               |
|          40 | -26.63%  | -67.23%            | -63.75% |    -0.09 |       62 | 31.61%     | ok               |
|          50 | -28.68%  | -67.23%            | -57.60% |    -0.18 |       56 | 21.46%     | ok               |
|          35 | -39.08%  | -67.23%            | -68.71% |    -0.22 |       74 | 36.97%     | ok               |
|          30 | -74.22%  | -67.23%            | -80.61% |    -0.92 |       92 | 43.10%     | ok               |

## UPS Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -34.83%  | -24.13%            | -44.06% |    -0.65 |       82 | 48.09%     | ok               |
|          35 | -34.07%  | -24.13%            | -38.06% |    -0.69 |       63 | 33.94%     | ok               |
|          25 | -35.87%  | -24.13%            | -40.43% |    -0.69 |       78 | 44.59%     | ok               |
|          15 | -38.79%  | -24.13%            | -46.28% |    -0.74 |       90 | 52.91%     | ok               |
|          30 | -37.03%  | -24.13%            | -38.75% |    -0.75 |       70 | 39.77%     | ok               |

## USO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 13.64%   | 54.45%             | -33.25% |     0.34 |       50 | 26.29%     | ok               |
|          30 | 5.95%    | 54.45%             | -43.35% |     0.22 |       68 | 33.78%     | ok               |
|          40 | 2.02%    | 54.45%             | -41.14% |     0.16 |       61 | 28.95%     | ok               |
|          50 | 2.30%    | 54.45%             | -31.13% |     0.15 |       52 | 23.63%     | ok               |
|          20 | 1.00%    | 54.45%             | -46.76% |     0.15 |       76 | 39.10%     | ok               |

## VEA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 5.44%    | 49.95%             | -16.28% |     0.25 |       60 | 50.58%     | ok               |
|          20 | 1.19%    | 49.95%             | -17.70% |     0.1  |       61 | 47.92%     | ok               |
|          25 | -0.82%   | 49.95%             | -17.79% |     0.02 |       57 | 46.26%     | ok               |
|          30 | -0.98%   | 49.95%             | -17.93% |     0.01 |       58 | 44.09%     | ok               |
|          35 | -2.09%   | 49.95%             | -16.79% |    -0.03 |       56 | 43.09%     | ok               |

## VIXY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -48.04%  | -65.31%            | -69.78% |    -0.43 |       46 | 10.48%     | ok               |
|          45 | -59.37%  | -65.31%            | -75.03% |    -0.61 |       60 | 16.64%     | ok               |
|          40 | -67.66%  | -65.31%            | -80.72% |    -0.74 |       76 | 21.46%     | ok               |
|          35 | -70.62%  | -65.31%            | -84.37% |    -0.76 |       90 | 26.79%     | ok               |
|          15 | -77.15%  | -65.31%            | -89.47% |    -0.77 |      101 | 44.76%     | ok               |

## VNQ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -8.60%   | 17.11%             | -19.07% |    -0.37 |       60 | 28.62%     | ok               |
|          50 | -9.03%   | 17.11%             | -17.13% |    -0.41 |       56 | 26.12%     | ok               |
|          25 | -13.12%  | 17.11%             | -22.34% |    -0.51 |       69 | 40.77%     | ok               |
|          20 | -14.71%  | 17.11%             | -23.79% |    -0.56 |       72 | 43.43%     | ok               |
|          15 | -15.49%  | 17.11%             | -24.90% |    -0.59 |       67 | 44.76%     | ok               |

## VTI Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 19.21%   | 50.21%             | -13.96% |     0.65 |       64 | 54.91%     | ok               |
|          15 | 13.11%   | 50.21%             | -15.70% |     0.46 |       67 | 57.40%     | ok               |
|          25 | 5.43%    | 50.21%             | -16.10% |     0.24 |       60 | 52.91%     | ok               |
|          30 | -1.57%   | 50.21%             | -18.77% |     0    |       68 | 51.08%     | ok               |
|          35 | -4.04%   | 50.21%             | -20.89% |    -0.09 |       62 | 47.92%     | ok               |

## VWO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -9.03%   | 47.70%             | -24.01% |    -0.26 |       69 | 49.42%     | ok               |
|          50 | -7.89%   | 47.70%             | -21.68% |    -0.28 |       60 | 32.45%     | ok               |
|          20 | -10.06%  | 47.70%             | -26.14% |    -0.31 |       67 | 47.25%     | ok               |
|          40 | -8.98%   | 47.70%             | -23.57% |    -0.31 |       70 | 37.94%     | ok               |
|          45 | -9.69%   | 47.70%             | -23.75% |    -0.35 |       62 | 34.94%     | ok               |

## VZ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -6.80%   | 5.78%              | -12.71% |    -0.19 |       50 | 24.29%     | ok               |
|          45 | -17.15%  | 5.78%              | -20.47% |    -0.56 |       62 | 27.79%     | ok               |
|          35 | -19.44%  | 5.78%              | -19.89% |    -0.62 |       63 | 33.44%     | ok               |
|          25 | -22.19%  | 5.78%              | -24.90% |    -0.64 |       81 | 41.43%     | ok               |
|          40 | -23.21%  | 5.78%              | -23.46% |    -0.8  |       66 | 30.62%     | ok               |

## WFC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -1.86%   | 77.36%             | -18.29% |     0.01 |       60 | 34.78%     | ok               |
|          35 | -7.10%   | 77.36%             | -22.53% |    -0.08 |       81 | 46.59%     | ok               |
|          20 | -15.21%  | 77.36%             | -29.96% |    -0.2  |       79 | 56.07%     | ok               |
|          45 | -10.02%  | 77.36%             | -24.02% |    -0.22 |       68 | 39.60%     | ok               |
|          30 | -16.94%  | 77.36%             | -29.91% |    -0.27 |       86 | 49.92%     | ok               |

## WIF-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 60.65%   | -81.73%            | -46.21% |     0.66 |       71 | 41.38%     | ok               |
|          20 | 54.98%   | -81.73%            | -40.67% |     0.64 |       65 | 38.70%     | ok               |
|          25 | 2.09%    | -81.73%            | -45.19% |     0.31 |       67 | 36.02%     | ok               |
|          50 | -12.13%  | -81.73%            | -33.04% |    -0.02 |       38 | 11.69%     | ok               |
|          30 | -35.28%  | -81.73%            | -50.54% |    -0.13 |       68 | 31.99%     | ok               |

## WMT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 55.31%   | 100.60%            | -9.18%  |     1.46 |       38 | 42.60%     | ok               |
|          50 | 48.99%   | 100.60%            | -12.19% |     1.39 |       32 | 40.43%     | ok               |
|          40 | 45.60%   | 100.60%            | -9.83%  |     1.23 |       42 | 43.76%     | ok               |
|          35 | 42.85%   | 100.60%            | -11.54% |     1.13 |       54 | 47.92%     | ok               |
|          30 | 18.87%   | 100.60%            | -21.31% |     0.55 |       61 | 50.58%     | ok               |

## XBI Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 17.52%   | 83.69%             | -16.56% |     0.49 |       60 | 35.94%     | ok               |
|          45 | 16.62%   | 83.69%             | -16.74% |     0.48 |       52 | 32.78%     | ok               |
|          35 | 13.86%   | 83.69%             | -20.36% |     0.4  |       62 | 39.43%     | ok               |
|          30 | 12.59%   | 83.69%             | -20.73% |     0.37 |       62 | 41.10%     | ok               |
|          50 | 7.05%    | 83.69%             | -16.83% |     0.26 |       54 | 29.45%     | ok               |

## XLB Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -1.57%   | 21.42%             | -20.60% |    -0.01 |       56 | 31.45%     | ok               |
|          50 | -1.52%   | 21.42%             | -17.40% |    -0.01 |       40 | 27.12%     | ok               |
|          45 | -4.43%   | 21.42%             | -20.61% |    -0.13 |       40 | 28.62%     | ok               |
|          35 | -4.92%   | 21.42%             | -23.62% |    -0.13 |       56 | 34.94%     | ok               |
|          25 | -8.20%   | 21.42%             | -23.73% |    -0.24 |       64 | 40.60%     | ok               |

## XLC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 13.12%   | 39.80%             | -12.33% |     0.47 |       67 | 55.07%     | ok               |
|          25 | 11.47%   | 39.80%             | -12.31% |     0.42 |       64 | 56.74%     | ok               |
|          40 | 9.24%    | 39.80%             | -13.38% |     0.38 |       68 | 47.59%     | ok               |
|          35 | 8.63%    | 39.80%             | -13.38% |     0.35 |       64 | 51.91%     | ok               |
|          20 | 3.83%    | 39.80%             | -13.41% |     0.18 |       70 | 59.57%     | ok               |

## XLE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 1.65%    | 33.37%             | -25.98% |     0.12 |       50 | 36.44%     | ok               |
|          35 | -3.37%   | 33.37%             | -32.17% |    -0    |       65 | 43.93%     | ok               |
|          45 | -3.59%   | 33.37%             | -30.88% |    -0.03 |       58 | 39.10%     | ok               |
|          25 | -10.96%  | 33.37%             | -37.50% |    -0.19 |       81 | 49.25%     | ok               |
|          30 | -10.98%  | 33.37%             | -37.51% |    -0.21 |       73 | 46.09%     | ok               |

## XLF Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -3.18%   | 41.93%             | -18.01% |    -0.04 |       68 | 53.91%     | ok               |
|          15 | -7.19%   | 41.93%             | -19.58% |    -0.18 |       76 | 56.74%     | ok               |
|          30 | -9.15%   | 41.93%             | -23.61% |    -0.28 |       76 | 48.25%     | ok               |
|          25 | -9.94%   | 41.93%             | -23.22% |    -0.3  |       77 | 50.42%     | ok               |
|          35 | -15.39%  | 41.93%             | -25.31% |    -0.58 |       66 | 44.76%     | ok               |

## XLI Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 7.10%    | 55.64%             | -10.36% |     0.3  |       74 | 52.08%     | ok               |
|          20 | 3.10%    | 55.64%             | -12.74% |     0.17 |       65 | 47.75%     | ok               |
|          30 | 0.84%    | 55.64%             | -11.74% |     0.09 |       66 | 45.26%     | ok               |
|          45 | 0.26%    | 55.64%             | -13.96% |     0.06 |       64 | 36.44%     | ok               |
|          50 | -0.04%   | 55.64%             | -11.00% |     0.04 |       58 | 34.44%     | ok               |

## XLK Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 83.90%   | 78.93%             | -14.75% |     1.34 |       41 | 51.75%     | ok               |
|          20 | 69.51%   | 78.93%             | -14.75% |     1.21 |       48 | 49.58%     | ok               |
|          25 | 66.06%   | 78.93%             | -14.75% |     1.2  |       42 | 47.42%     | ok               |
|          30 | 63.89%   | 78.93%             | -14.75% |     1.19 |       42 | 46.26%     | ok               |
|          35 | 45.60%   | 78.93%             | -13.61% |     0.96 |       54 | 43.59%     | ok               |

## XLM-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 27.47%   | -51.18%            | -38.97% |     0.49 |       44 | 27.20%     | ok               |
|          45 | 23.64%   | -51.18%            | -43.99% |     0.45 |       50 | 30.84%     | ok               |
|          30 | 5.21%    | -51.18%            | -50.36% |     0.28 |       69 | 45.79%     | ok               |
|          40 | 2.83%    | -51.18%            | -43.80% |     0.24 |       49 | 35.25%     | ok               |
|          35 | -4.00%   | -51.18%            | -50.42% |     0.17 |       69 | 41.76%     | ok               |

## XLP Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 10.55%   | 15.86%             | -6.85%  |     0.66 |       56 | 33.78%     | ok               |
|          40 | 9.85%    | 15.86%             | -7.77%  |     0.59 |       70 | 38.10%     | ok               |
|          50 | 8.70%    | 15.86%             | -7.01%  |     0.56 |       56 | 31.28%     | ok               |
|          35 | 8.89%    | 15.86%             | -9.73%  |     0.53 |       66 | 41.10%     | ok               |
|          30 | 6.48%    | 15.86%             | -11.56% |     0.4  |       70 | 42.43%     | ok               |

## XLU Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 6.93%    | 51.30%             | -12.19% |     0.37 |       50 | 30.62%     | ok               |
|          45 | 4.80%    | 51.30%             | -13.95% |     0.27 |       54 | 31.45%     | ok               |
|          40 | 1.91%    | 51.30%             | -15.27% |     0.14 |       58 | 32.95%     | ok               |
|          35 | -5.69%   | 51.30%             | -19.41% |    -0.23 |       64 | 35.27%     | ok               |
|          30 | -7.08%   | 51.30%             | -20.40% |    -0.28 |       69 | 38.60%     | ok               |

## XLV Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -13.29%  | 13.61%             | -17.94% |    -0.66 |       68 | 35.77%     | ok               |
|          25 | -14.57%  | 13.61%             | -19.15% |    -0.72 |       70 | 37.10%     | ok               |
|          15 | -18.44%  | 13.61%             | -22.51% |    -0.9  |       81 | 41.93%     | ok               |
|          20 | -18.37%  | 13.61%             | -22.60% |    -0.92 |       75 | 38.77%     | ok               |
|          50 | -15.59%  | 13.61%             | -19.32% |    -0.94 |       56 | 24.46%     | ok               |

## XLY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 5.14%    | 30.90%             | -12.94% |     0.23 |       70 | 41.43%     | ok               |
|          30 | 3.26%    | 30.90%             | -14.01% |     0.17 |       70 | 44.43%     | ok               |
|          50 | 1.64%    | 30.90%             | -11.49% |     0.12 |       50 | 29.45%     | ok               |
|          15 | 1.20%    | 30.90%             | -15.77% |     0.11 |       74 | 51.25%     | ok               |
|          45 | -1.43%   | 30.90%             | -13.48% |    -0    |       54 | 32.11%     | ok               |

## XOM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 4.35%    | 39.26%             | -21.35% |     0.2  |       42 | 29.45%     | ok               |
|          25 | 2.06%    | 39.26%             | -19.90% |     0.13 |       57 | 37.60%     | ok               |
|          30 | 1.05%    | 39.26%             | -20.29% |     0.1  |       57 | 36.94%     | ok               |
|          20 | -1.72%   | 39.26%             | -25.56% |     0.03 |       62 | 40.10%     | ok               |
|          40 | -1.71%   | 39.26%             | -21.45% |     0.02 |       52 | 34.61%     | ok               |

## XRP-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | -25.11%  | -59.80%            | -46.87% |    -0.14 |       68 | 39.85%     | ok               |
|          40 | -30.47%  | -59.80%            | -44.89% |    -0.26 |       58 | 33.72%     | ok               |
|          30 | -37.23%  | -59.80%            | -54.70% |    -0.33 |       70 | 44.06%     | ok               |
|          45 | -38.24%  | -59.80%            | -46.06% |    -0.42 |       58 | 29.50%     | ok               |
|          50 | -34.88%  | -59.80%            | -38.03% |    -0.46 |       60 | 22.03%     | ok               |

## YFI-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -38.27%  | -66.20%            | -54.04% |    -0.68 |       64 | 22.41%     | ok               |
|          40 | -45.82%  | -66.20%            | -52.37% |    -0.71 |       62 | 27.20%     | ok               |
|          35 | -61.22%  | -66.20%            | -65.91% |    -1.02 |       73 | 34.48%     | ok               |
|          30 | -63.69%  | -66.20%            | -69.94% |    -1.02 |       83 | 40.61%     | ok               |
|          50 | -46.78%  | -66.20%            | -54.66% |    -1.05 |       54 | 17.24%     | ok               |

## ZEC-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 106.47%  | 1191.57%           | -24.66% |     0.84 |       46 | 22.22%     | ok               |
|          35 | 77.27%   | 1191.57%           | -44.34% |     0.71 |       54 | 28.74%     | ok               |
|          25 | 57.82%   | 1191.57%           | -48.59% |     0.62 |       60 | 37.93%     | ok               |
|          30 | 42.20%   | 1191.57%           | -47.68% |     0.55 |       64 | 34.48%     | ok               |
|          50 | 41.93%   | 1191.57%           | -34.39% |     0.53 |       48 | 19.73%     | ok               |
