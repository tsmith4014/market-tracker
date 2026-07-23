# Market Tracker Backtest Report

_Generated: 2026-07-23T03:58:19+00:00_

## Data Sources

- Crypto: Kraken -> Coinbase -> CoinGecko OHLC -> CoinPaprika fallback chain.
- Stocks / ETFs / indices: Stooq -> Yahoo Finance fallback chain.
- Data rows are generated from real market APIs. Mock OHLCV rows are not generated.

## Data Freshness

- Rows: **92,532**
- Symbols: **161**
- Date range: **2024-02-28** to **2026-07-23**

## Latest Signals

| symbol     | date                |         close |   composite_score | signal   | data_source   |
|:-----------|:--------------------|--------------:|------------------:|:---------|:--------------|
| AAPL       | 2026-07-22 00:00:00 |   325.89      |         67.0833   | LONG     | Yahoo Finance |
| ABBV       | 2026-07-22 00:00:00 |   253.3       |         33.5833   | LONG     | Yahoo Finance |
| AMGN       | 2026-07-22 00:00:00 |   366.05      |         36.0833   | LONG     | Yahoo Finance |
| AMZN       | 2026-07-22 00:00:00 |   244.85      |         37.6667   | LONG     | Yahoo Finance |
| ARB-USD    | 2026-07-23 00:00:00 |     0.0895    |         40.1667   | LONG     | Kraken API    |
| BAC        | 2026-07-22 00:00:00 |    61.62      |         37.75     | LONG     | Yahoo Finance |
| BLK        | 2026-07-22 00:00:00 |  1056.63      |         54.4167   | LONG     | Yahoo Finance |
| COP        | 2026-07-22 00:00:00 |   118.79      |         71.25     | LONG     | Yahoo Finance |
| CVX        | 2026-07-22 00:00:00 |   192.98      |         73.25     | LONG     | Yahoo Finance |
| DBC        | 2026-07-22 00:00:00 |    29.86      |         73.25     | LONG     | Yahoo Finance |
| EOG        | 2026-07-22 00:00:00 |   144         |         70.75     | LONG     | Yahoo Finance |
| ETH-USD    | 2026-07-23 00:00:00 |  1922.16      |         41.5      | LONG     | Kraken API    |
| FCX        | 2026-07-22 00:00:00 |    65         |         60.4167   | LONG     | Yahoo Finance |
| JNJ        | 2026-07-22 00:00:00 |   255.63      |         30.75     | LONG     | Yahoo Finance |
| LDO-USD    | 2026-07-23 00:00:00 |     0.399     |         47        | LONG     | Kraken API    |
| LINK-USD   | 2026-07-23 00:00:00 |     8.59623   |         52.75     | LONG     | Kraken API    |
| LTC-USD    | 2026-07-23 00:00:00 |    47.09      |         51        | LONG     | Kraken API    |
| MPC        | 2026-07-22 00:00:00 |   315.82      |         70.75     | LONG     | Yahoo Finance |
| OXY        | 2026-07-22 00:00:00 |    57.5       |         71.25     | LONG     | Yahoo Finance |
| RTX        | 2026-07-22 00:00:00 |   194.88      |         39.8333   | LONG     | Yahoo Finance |
| SCHW       | 2026-07-22 00:00:00 |   100.8       |         43.0833   | LONG     | Yahoo Finance |
| SKY-USD    | 2026-07-23 00:00:00 |     0.06307   |         30.6667   | LONG     | Kraken API    |
| SLB        | 2026-07-22 00:00:00 |    47.67      |         32.3333   | LONG     | Yahoo Finance |
| TMO        | 2026-07-22 00:00:00 |   526.46      |         39.8333   | LONG     | Yahoo Finance |
| UNH        | 2026-07-22 00:00:00 |   431.31      |         46.75     | LONG     | Yahoo Finance |
| UNI-USD    | 2026-07-23 00:00:00 |     3.7898    |         36.6667   | LONG     | Kraken API    |
| UPS        | 2026-07-22 00:00:00 |   115.84      |         76.9167   | LONG     | Yahoo Finance |
| USO        | 2026-07-22 00:00:00 |   131.68      |         69.25     | LONG     | Yahoo Finance |
| XLE        | 2026-07-22 00:00:00 |    59.2       |         73.25     | LONG     | Yahoo Finance |
| XLF        | 2026-07-22 00:00:00 |    56.05      |         46.75     | LONG     | Yahoo Finance |
| XOM        | 2026-07-22 00:00:00 |   154.45      |         71.25     | LONG     | Yahoo Finance |
| ZEC-USD    | 2026-07-23 00:00:00 |   515.02      |         42.8333   | LONG     | Kraken API    |
| AAVE-USD   | 2026-07-23 00:00:00 |    96.97      |         25        | NEUTRAL  | Kraken API    |
| ADA-USD    | 2026-07-23 00:00:00 |     0.174351  |         22        | NEUTRAL  | Kraken API    |
| ADBE       | 2026-07-22 00:00:00 |   218.36      |        -12.75     | NEUTRAL  | Yahoo Finance |
| ALGO-USD   | 2026-07-23 00:00:00 |     0.08433   |        -22.25     | NEUTRAL  | Kraken API    |
| AMAT       | 2026-07-22 00:00:00 |   553.92      |          1.08333  | NEUTRAL  | Yahoo Finance |
| AMD        | 2026-07-22 00:00:00 |   552.33      |         26        | NEUTRAL  | Yahoo Finance |
| APT-USD    | 2026-07-23 00:00:00 |     0.6214    |          1.5      | NEUTRAL  | Kraken API    |
| AVAX-USD   | 2026-07-23 00:00:00 |     6.53      |        -22        | NEUTRAL  | Kraken API    |
| AVGO       | 2026-07-22 00:00:00 |   396.81      |         42.4167   | NEUTRAL  | Yahoo Finance |
| BA         | 2026-07-22 00:00:00 |   208.65      |        -63.25     | NEUTRAL  | Yahoo Finance |
| BITO       | 2026-07-22 00:00:00 |     8.95      |          5.83333  | NEUTRAL  | Yahoo Finance |
| BTC-USD    | 2026-07-23 00:00:00 | 65620.9       |         36.0833   | NEUTRAL  | Kraken API    |
| C          | 2026-07-22 00:00:00 |   132.25      |        -13.5833   | NEUTRAL  | Yahoo Finance |
| CAT        | 2026-07-22 00:00:00 |   889.31      |        -18.5833   | NEUTRAL  | Yahoo Finance |
| CL         | 2026-07-22 00:00:00 |    91.63      |          7.66667  | NEUTRAL  | Yahoo Finance |
| CMCSA      | 2026-07-22 00:00:00 |    23.52      |         -4.25     | NEUTRAL  | Yahoo Finance |
| COMP-USD   | 2026-07-23 00:00:00 |    17.15      |         19.8333   | NEUTRAL  | Kraken API    |
| COST       | 2026-07-22 00:00:00 |   927.31      |        -12.3333   | NEUTRAL  | Yahoo Finance |
| CRM        | 2026-07-22 00:00:00 |   163         |        -32.6667   | NEUTRAL  | Yahoo Finance |
| CRV-USD    | 2026-07-23 00:00:00 |     0.21076   |          0.583333 | NEUTRAL  | Kraken API    |
| CSCO       | 2026-07-22 00:00:00 |   112.21      |          4.41667  | NEUTRAL  | Yahoo Finance |
| DASH-USD   | 2026-07-23 00:00:00 |    33.422     |        -43.75     | NEUTRAL  | Kraken API    |
| DE         | 2026-07-22 00:00:00 |   607.33      |         34.8333   | NEUTRAL  | Yahoo Finance |
| DIA        | 2026-07-22 00:00:00 |   521.47      |         20.1667   | NEUTRAL  | Yahoo Finance |
| DIS        | 2026-07-22 00:00:00 |    95.87      |        -30.3333   | NEUTRAL  | Yahoo Finance |
| DOGE-USD   | 2026-07-23 00:00:00 |     0.0725762 |        -20.9167   | NEUTRAL  | Kraken API    |
| DOT-USD    | 2026-07-23 00:00:00 |     0.8227    |        -13.9167   | NEUTRAL  | Kraken API    |
| DXY-INDEX  | 2026-07-22 00:00:00 |   100.977     |         48.1183   | NEUTRAL  | Yahoo Finance |
| EEM        | 2026-07-22 00:00:00 |    64.99      |        -15.5833   | NEUTRAL  | Yahoo Finance |
| EFA        | 2026-07-22 00:00:00 |   104.25      |         30.5      | NEUTRAL  | Yahoo Finance |
| ETC-USD    | 2026-07-23 00:00:00 |     6.901     |        -24.25     | NEUTRAL  | Kraken API    |
| EWJ        | 2026-07-22 00:00:00 |    92.19      |         -4.83333  | NEUTRAL  | Yahoo Finance |
| FET-USD    | 2026-07-23 00:00:00 |     0.1543    |        -20.3333   | NEUTRAL  | Kraken API    |
| FIL-USD    | 2026-07-23 00:00:00 |     0.74      |        -47.0833   | NEUTRAL  | Kraken API    |
| FXI        | 2026-07-22 00:00:00 |    34.43      |         23.5833   | NEUTRAL  | Yahoo Finance |
| GDX        | 2026-07-22 00:00:00 |    76.68      |        -13.8333   | NEUTRAL  | Yahoo Finance |
| GDXJ       | 2026-07-22 00:00:00 |   100.56      |        -17.1667   | NEUTRAL  | Yahoo Finance |
| GE         | 2026-07-22 00:00:00 |   341.19      |         -4.91667  | NEUTRAL  | Yahoo Finance |
| GLD        | 2026-07-22 00:00:00 |   379.12      |        -11.8333   | NEUTRAL  | Yahoo Finance |
| GOOGL      | 2026-07-22 00:00:00 |   342.09      |        -34.25     | NEUTRAL  | Yahoo Finance |
| GRT-USD    | 2026-07-23 00:00:00 |     0.01633   |        -22        | NEUTRAL  | Kraken API    |
| GS         | 2026-07-22 00:00:00 |  1098.2       |         63.3333   | NEUTRAL  | Yahoo Finance |
| HBAR-USD   | 2026-07-23 00:00:00 |     0.07249   |         29.6667   | NEUTRAL  | Kraken API    |
| HD         | 2026-07-22 00:00:00 |   331.45      |        -52.0833   | NEUTRAL  | Yahoo Finance |
| HON        | 2026-07-22 00:00:00 |   232.99      |         59.9167   | NEUTRAL  | Yahoo Finance |
| HYG        | 2026-07-22 00:00:00 |    79.52      |        -57.0833   | NEUTRAL  | Yahoo Finance |
| IBIT       | 2026-07-22 00:00:00 |    37.34      |         -9.33333  | NEUTRAL  | Yahoo Finance |
| ICP-USD    | 2026-07-23 00:00:00 |     2.19      |        -34.9167   | NEUTRAL  | Kraken API    |
| IEMG       | 2026-07-22 00:00:00 |    78.97      |        -15.5833   | NEUTRAL  | Yahoo Finance |
| INJ-USD    | 2026-07-23 00:00:00 |     5.112     |         55.8333   | NEUTRAL  | Kraken API    |
| INTC       | 2026-07-22 00:00:00 |   102.62      |        -19.5833   | NEUTRAL  | Yahoo Finance |
| INTU       | 2026-07-22 00:00:00 |   284.47      |         -1.5      | NEUTRAL  | Yahoo Finance |
| ITA        | 2026-07-22 00:00:00 |   231.11      |        -24.25     | NEUTRAL  | Yahoo Finance |
| IWM        | 2026-07-22 00:00:00 |   293.79      |         -0.333333 | NEUTRAL  | Yahoo Finance |
| JPM        | 2026-07-22 00:00:00 |   348.21      |         32.3333   | NEUTRAL  | Yahoo Finance |
| KO         | 2026-07-22 00:00:00 |    82.2       |         17.3333   | NEUTRAL  | Yahoo Finance |
| LIN        | 2026-07-22 00:00:00 |   508.67      |        -26.5      | NEUTRAL  | Yahoo Finance |
| LLY        | 2026-07-22 00:00:00 |  1163.01      |        -11.1667   | NEUTRAL  | Yahoo Finance |
| LRCX       | 2026-07-22 00:00:00 |   319.29      |        -28.8333   | NEUTRAL  | Yahoo Finance |
| MCD        | 2026-07-22 00:00:00 |   263.57      |        -61.1667   | NEUTRAL  | Yahoo Finance |
| META       | 2026-07-22 00:00:00 |   627.17      |         19.4167   | NEUTRAL  | Yahoo Finance |
| MRK        | 2026-07-22 00:00:00 |   127.47      |         45        | NEUTRAL  | Yahoo Finance |
| MS         | 2026-07-22 00:00:00 |   218.5       |         35.8333   | NEUTRAL  | Yahoo Finance |
| MSFT       | 2026-07-22 00:00:00 |   390.34      |        -22.3333   | NEUTRAL  | Yahoo Finance |
| MU         | 2026-07-22 00:00:00 |   959.48      |         18.4167   | NEUTRAL  | Yahoo Finance |
| NEAR-USD   | 2026-07-23 00:00:00 |     1.8678    |        -21        | NEUTRAL  | Kraken API    |
| NEM        | 2026-07-22 00:00:00 |    95.75      |         -6.33333  | NEUTRAL  | Yahoo Finance |
| NFLX       | 2026-07-22 00:00:00 |    68.53      |        -59.1667   | NEUTRAL  | Yahoo Finance |
| NKE        | 2026-07-22 00:00:00 |    42.21      |        -42.6667   | NEUTRAL  | Yahoo Finance |
| NOW        | 2026-07-22 00:00:00 |    95.46      |        -68.75     | NEUTRAL  | Yahoo Finance |
| NVDA       | 2026-07-22 00:00:00 |   212.06      |         45.3333   | NEUTRAL  | Yahoo Finance |
| OP-USD     | 2026-07-23 00:00:00 |     0.0962    |        -46.5833   | NEUTRAL  | Kraken API    |
| PEP        | 2026-07-22 00:00:00 |   135.65      |        -59        | NEUTRAL  | Yahoo Finance |
| PEPE-USD   | 2026-07-23 00:00:00 |     2.848e-06 |         29.3333   | NEUTRAL  | Kraken API    |
| PFE        | 2026-07-22 00:00:00 |    24.82      |          2.41667  | NEUTRAL  | Yahoo Finance |
| PG         | 2026-07-22 00:00:00 |   149.13      |         27.0833   | NEUTRAL  | Yahoo Finance |
| PM         | 2026-07-22 00:00:00 |   194.3       |         63.3333   | NEUTRAL  | Yahoo Finance |
| POL-USD    | 2026-07-23 00:00:00 |     0.07874   |         -7.16667  | NEUTRAL  | Kraken API    |
| QCOM       | 2026-07-22 00:00:00 |   175.63      |        -12.1667   | NEUTRAL  | Yahoo Finance |
| QQQ        | 2026-07-22 00:00:00 |   705.35      |        -24.8333   | NEUTRAL  | Yahoo Finance |
| RENDER-USD | 2026-07-23 00:00:00 |     1.506     |        -22        | NEUTRAL  | Kraken API    |
| SBUX       | 2026-07-22 00:00:00 |   103.98      |         10.3333   | NEUTRAL  | Yahoo Finance |
| SHIB-USD   | 2026-07-23 00:00:00 |     4.242e-06 |        -24.25     | NEUTRAL  | Kraken API    |
| SHY        | 2026-07-22 00:00:00 |    81.83      |        -31.25     | NEUTRAL  | Yahoo Finance |
| SLV        | 2026-07-22 00:00:00 |    53.92      |        -20.5833   | NEUTRAL  | Yahoo Finance |
| SMH        | 2026-07-22 00:00:00 |   586.91      |          2.66667  | NEUTRAL  | Yahoo Finance |
| SNX-USD    | 2026-07-23 00:00:00 |     0.2186    |         -0.833333 | NEUTRAL  | Kraken API    |
| SOL-USD    | 2026-07-23 00:00:00 |    77.56      |          7.33333  | NEUTRAL  | Kraken API    |
| SOXX       | 2026-07-22 00:00:00 |   555.52      |          2.41667  | NEUTRAL  | Yahoo Finance |
| SPY        | 2026-07-22 00:00:00 |   747.41      |         41        | NEUTRAL  | Yahoo Finance |
| SUSHI-USD  | 2026-07-23 00:00:00 |     0.1695    |         29.3333   | NEUTRAL  | Kraken API    |
| T          | 2026-07-22 00:00:00 |    23.04      |         23.0833   | NEUTRAL  | Yahoo Finance |
| TGT        | 2026-07-22 00:00:00 |   137.92      |         60.8333   | NEUTRAL  | Yahoo Finance |
| TMUS       | 2026-07-22 00:00:00 |   190.94      |         43.25     | NEUTRAL  | Yahoo Finance |
| TRX-USD    | 2026-07-23 00:00:00 |     0.328285  |         53.5      | NEUTRAL  | Kraken API    |
| TSLA       | 2026-07-22 00:00:00 |   374.01      |        -69        | NEUTRAL  | Yahoo Finance |
| TXN        | 2026-07-22 00:00:00 |   294.19      |         -6.83333  | NEUTRAL  | Yahoo Finance |
| VEA        | 2026-07-22 00:00:00 |    70.49      |          3.75     | NEUTRAL  | Yahoo Finance |
| VIXY       | 2026-07-22 00:00:00 |    20.72      |        -26.5      | NEUTRAL  | Yahoo Finance |
| VNQ        | 2026-07-22 00:00:00 |    99.02      |         67.1667   | NEUTRAL  | Yahoo Finance |
| VTI        | 2026-07-22 00:00:00 |   368.87      |         30.6667   | NEUTRAL  | Yahoo Finance |
| VWO        | 2026-07-22 00:00:00 |    58.81      |        -27.5833   | NEUTRAL  | Yahoo Finance |
| VZ         | 2026-07-22 00:00:00 |    44.29      |         23.3333   | NEUTRAL  | Yahoo Finance |
| WFC        | 2026-07-22 00:00:00 |    86.42      |         26.5833   | NEUTRAL  | Yahoo Finance |
| WIF-USD    | 2026-07-23 00:00:00 |     0.1512    |        -22        | NEUTRAL  | Kraken API    |
| WMT        | 2026-07-22 00:00:00 |   109.33      |        -19.5833   | NEUTRAL  | Yahoo Finance |
| XBI        | 2026-07-22 00:00:00 |   152.11      |         16.4167   | NEUTRAL  | Yahoo Finance |
| XLB        | 2026-07-22 00:00:00 |    50.82      |          5.16667  | NEUTRAL  | Yahoo Finance |
| XLC        | 2026-07-22 00:00:00 |   109.2       |        -46.3333   | NEUTRAL  | Yahoo Finance |
| XLI        | 2026-07-22 00:00:00 |   178.85      |         22.4167   | NEUTRAL  | Yahoo Finance |
| XLK        | 2026-07-22 00:00:00 |   180.27      |         -6.83333  | NEUTRAL  | Yahoo Finance |
| XLM-USD    | 2026-07-23 00:00:00 |     0.184748  |        -34.75     | NEUTRAL  | Kraken API    |
| XLP        | 2026-07-22 00:00:00 |    84.38      |         65.4167   | NEUTRAL  | Yahoo Finance |
| XLU        | 2026-07-22 00:00:00 |    45.93      |         36        | NEUTRAL  | Yahoo Finance |
| XLV        | 2026-07-22 00:00:00 |   159.43      |         27.9167   | NEUTRAL  | Yahoo Finance |
| XLY        | 2026-07-22 00:00:00 |   114.02      |        -61.75     | NEUTRAL  | Yahoo Finance |
| XRP-USD    | 2026-07-23 00:00:00 |     1.13486   |         23.0833   | NEUTRAL  | Kraken API    |
| YFI-USD    | 2026-07-23 00:00:00 |  2096.7       |         16.5833   | NEUTRAL  | Kraken API    |
| AGG        | 2026-07-22 00:00:00 |    97.58      |        -48.0833   | SHORT    | Yahoo Finance |
| ARKK       | 2026-07-22 00:00:00 |    76.03      |        -32        | SHORT    | Yahoo Finance |
| ATOM-USD   | 2026-07-23 00:00:00 |     1.4511    |        -33.1667   | SHORT    | Kraken API    |
| BCH-USD    | 2026-07-23 00:00:00 |   217.94      |        -55        | SHORT    | Kraken API    |
| BND        | 2026-07-22 00:00:00 |    72.4       |        -48.0833   | SHORT    | Yahoo Finance |
| BONK-USD   | 2026-07-23 00:00:00 |     3.025e-06 |        -46.6667   | SHORT    | Kraken API    |
| IBM        | 2026-07-22 00:00:00 |   205.77      |        -65.5833   | SHORT    | Yahoo Finance |
| IEF        | 2026-07-22 00:00:00 |    93.1       |        -48.0833   | SHORT    | Yahoo Finance |
| ORCL       | 2026-07-22 00:00:00 |   125.84      |        -35.25     | SHORT    | Yahoo Finance |
| TIA-USD    | 2026-07-23 00:00:00 |     0.3584    |        -42.3333   | SHORT    | Kraken API    |
| TLT        | 2026-07-22 00:00:00 |    83.44      |        -53.4167   | SHORT    | Yahoo Finance |

## Edge Summary

- Symbols with trades: **160** of 160
- Beat buy-and-hold: **34.38%** of traded symbols
- Positive return: **30.00%** of traded symbols
- Median strategy return: **-10.10%** (benchmark **12.95%**)
- Median excess vs benchmark: **-25.75%**
- Median Sharpe: **-0.14**
- Median exposure: **43.93%**

> Edge is real only if both _beat buy-and-hold_ and _median excess_ are convincingly positive across many symbols. Treat a single high-return symbol as noise.

## Portfolio Backtest

Actual capital-allocation books (not per-symbol averages). Benchmarks: `equal_weight_buyhold` (whole tracked universe), `spy_buyhold` (100% SPY), and `sixty_forty` (60% SPY / 40% AGG). `high_conf_voltarget` inverse-vol-weights the HIGH-confidence book; `conviction_long_short` is market-neutral. Judge on **Sharpe** and **max_drawdown** out-of-sample, not raw return: a fully-invested long book wins on return in a bull market but carries all the risk.

| strategy              | scope         | ann_return   | ann_vol   |   sharpe | max_drawdown   | total_return   |   avg_gross_exposure |
|:----------------------|:--------------|:-------------|:----------|---------:|:---------------|:---------------|---------------------:|
| equal_weight_buyhold  | full          | -3.71%       | 32.48%    |    -0.11 | -46.40%        | -24.03%        |                 1    |
| equal_weight_buyhold  | out_of_sample | -23.43%      | 30.63%    |    -0.76 | -38.25%        | -25.96%        |                 1    |
| all_signals_ew        | full          | -16.40%      | 27.07%    |    -0.61 | -60.33%        | -45.75%        |                 1    |
| all_signals_ew        | out_of_sample | 24.31%       | 26.29%    |     0.92 | -18.56%        | 24.99%         |                 1    |
| high_conf_ew          | full          | -0.37%       | 31.51%    |    -0.01 | -43.77%        | -14.82%        |                 0.88 |
| high_conf_ew          | out_of_sample | 22.15%       | 33.88%    |     0.65 | -17.94%        | 19.36%         |                 0.88 |
| high_conf_voltarget   | full          | 1.84%        | 29.06%    |     0.06 | -36.02%        | -6.78%         |                 0.88 |
| high_conf_voltarget   | out_of_sample | 16.49%       | 31.39%    |     0.53 | -16.94%        | 13.34%         |                 0.88 |
| conviction_long_short | full          | -17.52%      | 23.20%    |    -0.75 | -48.21%        | -45.97%        |                 0.97 |
| conviction_long_short | out_of_sample | -10.08%      | 26.15%    |    -0.39 | -24.30%        | -13.43%        |                 0.97 |
| spy_buyhold           | full          | 6.21%        | 13.34%    |     0.47 | -17.80%        | 17.58%         |                 0.79 |
| spy_buyhold           | out_of_sample | -3.09%       | 9.81%     |    -0.31 | -13.27%        | -3.74%         |                 0.79 |
| sixty_forty           | full          | 3.68%        | 8.43%     |     0.44 | -10.77%        | 10.62%         |                 0.79 |
| sixty_forty           | out_of_sample | -3.36%       | 6.46%     |    -0.52 | -9.11%         | -3.74%         |                 0.79 |

## Walk-Forward Robustness

Each book measured across contiguous time folds (each a different regime). A book has durable edge only if `mean_sharpe` is positive, `min_sharpe` isn't deeply negative, and `pct_positive_folds` is high — a single great fold doesn't count. `fold_sharpes` lists each fold oldest-to-newest.

| strategy              |   n_folds |   mean_sharpe |   median_sharpe |   min_sharpe | pct_positive_folds   | mean_return   | fold_sharpes                 |
|:----------------------|----------:|--------------:|----------------:|-------------:|:---------------------|:--------------|:-----------------------------|
| equal_weight_buyhold  |         5 |          0.26 |            0.66 |        -1.37 | 60.00%               | -2.37%        | 1.72;-1.37;1.34;-1.05;0.66   |
| all_signals_ew        |         5 |         -0.68 |           -0.15 |        -2.4  | 20.00%               | -10.35%       | -0.08;-0.15;-2.40;0.35;-1.12 |
| high_conf_ew          |         5 |          0.1  |           -0.42 |        -0.7  | 40.00%               | -2.22%        | 1.35;-0.56;-0.70;0.82;-0.42  |
| high_conf_voltarget   |         5 |          0.28 |           -0.21 |        -0.8  | 40.00%               | -0.56%        | 2.10;-0.21;-0.80;0.75;-0.45  |
| conviction_long_short |         5 |         -0.91 |           -1.34 |        -1.69 | 20.00%               | -11.16%       | -1.39;-1.34;-0.54;0.42;-1.69 |
| spy_buyhold           |         5 |          0.69 |            0.01 |        -1.01 | 60.00%               | 3.72%         | 1.53;-0.35;3.26;-1.01;0.01   |
| sixty_forty           |         5 |          0.63 |           -0.36 |        -0.95 | 40.00%               | 2.23%         | 1.61;-0.40;3.24;-0.95;-0.36  |

## Strategy Comparison

Each decision rule backtested over the same data. `out_of_sample` is the most recent ~35% of each symbol's history (unseen tail). A rule has real edge only if `median_excess` and `beat_benchmark_pct` stay positive out-of-sample, not just full-sample.

| strategy        | scope         |   symbols | beat_benchmark_pct   | positive_pct   | median_return   | median_benchmark   | median_excess   |   median_sharpe |   total_trades |
|:----------------|:--------------|----------:|:---------------------|:---------------|:----------------|:-------------------|:----------------|----------------:|---------------:|
| trend           | full          |       160 | 34.38%               | 30.00%         | -10.10%         | 12.95%             | -25.75%         |           -0.14 |          11236 |
| trend           | out_of_sample |       160 | 40.62%               | 51.88%         | 1.58%           | 5.52%              | -4.24%          |            0.24 |           3759 |
| mean_reversion  | full          |       157 | 40.76%               | 51.59%         | 0.09%           | 12.74%             | -15.00%         |            0.04 |           1254 |
| mean_reversion  | out_of_sample |       124 | 50.00%               | 59.68%         | 0.38%           | 0.01%              | -0.10%          |            0.58 |            428 |
| regime_adaptive | full          |       160 | 35.00%               | 30.63%         | -10.75%         | 12.95%             | -25.96%         |           -0.14 |          11509 |
| regime_adaptive | out_of_sample |       160 | 40.00%               | 52.50%         | 1.51%           | 5.52%              | -3.41%          |            0.24 |           3866 |

## Signal Calibration

Realized forward return in the signal's direction, grouped by confidence. HIGH should outrank LOW for the confidence score to be meaningful.

| confidence_level   |   horizon |     n | mean_return   | median_return   | win_rate   |
|:-------------------|----------:|------:|:--------------|:----------------|:-----------|
| HIGH               |         5 |  7884 | 0.10%         | 0.09%           | 51.56%     |
| MEDIUM             |         5 | 29177 | 0.01%         | 0.07%           | 50.73%     |
| LOW                |         5 |  3391 | -0.63%        | -0.56%          | 44.50%     |
| ALL                |         5 | 40452 | -0.02%        | 0.03%           | 50.37%     |
| HIGH               |        10 |  7856 | 0.35%         | 0.09%           | 50.98%     |
| MEDIUM             |        10 | 28976 | 0.15%         | 0.10%           | 50.75%     |
| LOW                |        10 |  3342 | -0.92%        | -0.73%          | 45.15%     |
| ALL                |        10 | 40174 | 0.10%         | 0.04%           | 50.33%     |
| HIGH               |        20 |  7771 | 0.74%         | 0.31%           | 52.57%     |
| MEDIUM             |        20 | 28601 | 0.81%         | 0.58%           | 53.33%     |
| LOW                |        20 |  3252 | -0.73%        | -0.55%          | 47.11%     |
| ALL                |        20 | 39624 | 0.67%         | 0.45%           | 52.67%     |

## Backtest Summary

### Data Quality / Signal Availability

- **ok**: 160 symbols

| symbol     |   trades | return   | benchmark_return   | mdd     |   sharpe | exposure   | skipped_reason   |
|:-----------|---------:|:---------|:-------------------|:--------|---------:|:-----------|:-----------------|
| AAPL       |       61 | 17.28%   | 79.63%             | -20.65% |     0.43 | 49.25%     | ok               |
| AAVE-USD   |       76 | -52.31%  | -63.31%            | -68.26% |    -0.49 | 39.46%     | ok               |
| ABBV       |       68 | -20.88%  | 42.30%             | -30.55% |    -0.44 | 47.09%     | ok               |
| ADA-USD    |       90 | -83.44%  | -78.44%            | -88.94% |    -0.69 | 47.13%     | ok               |
| ADBE       |       64 | -30.37%  | -60.43%            | -34.98% |    -0.38 | 56.91%     | ok               |
| AGG        |       71 | -6.51%   | 0.40%              | -10.25% |    -1.07 | 32.28%     | ok               |
| ALGO-USD   |       86 | -50.43%  | -68.76%            | -53.13% |    -0.57 | 38.12%     | ok               |
| AMAT       |       71 | -33.68%  | 180.41%            | -57.21% |    -0.3  | 51.75%     | ok               |
| AMD        |       52 | 5.86%    | 212.86%            | -43.98% |     0.27 | 35.77%     | ok               |
| AMGN       |       71 | -15.48%  | 31.93%             | -34.19% |    -0.29 | 46.42%     | ok               |
| AMZN       |       80 | -37.69%  | 41.40%             | -42.48% |    -1.14 | 38.27%     | ok               |
| APT-USD    |       72 | -44.63%  | -89.45%            | -69.64% |    -0.29 | 41.57%     | ok               |
| ARB-USD    |       76 | -29.59%  | -81.89%            | -62.55% |    -0.12 | 39.85%     | ok               |
| ARKK       |       83 | -34.89%  | 48.61%             | -36.39% |    -0.62 | 39.93%     | ok               |
| ATOM-USD   |       88 | -69.32%  | -69.85%            | -74.39% |    -1.21 | 44.44%     | ok               |
| AVAX-USD   |       70 | -43.35%  | -73.89%            | -60.55% |    -0.44 | 38.12%     | ok               |
| AVGO       |       64 | 15.74%   | 207.74%            | -35.76% |     0.35 | 42.10%     | ok               |
| BA         |       67 | 7.60%    | 0.80%              | -30.56% |     0.25 | 49.25%     | ok               |
| BAC        |       78 | -5.93%   | 79.60%             | -26.91% |    -0.08 | 50.42%     | ok               |
| BCH-USD    |       76 | 5.44%    | -32.62%            | -53.87% |     0.27 | 48.08%     | ok               |
| BITO       |       80 | -14.71%  | -68.54%            | -42.82% |    -0.01 | 40.77%     | ok               |
| BLK        |       73 | -9.04%   | 30.50%             | -25.48% |    -0.2  | 42.60%     | ok               |
| BND        |       67 | -7.22%   | 0.42%              | -9.98%  |    -1.15 | 33.44%     | ok               |
| BONK-USD   |       70 | 54.72%   | -81.92%            | -48.17% |     0.64 | 42.53%     | ok               |
| BTC-USD    |       76 | 3.46%    | -31.48%            | -23.38% |     0.2  | 52.49%     | ok               |
| C          |       79 | -30.57%  | 140.24%            | -38.11% |    -0.61 | 51.08%     | ok               |
| CAT        |       72 | 19.71%   | 169.85%            | -21.02% |     0.42 | 55.24%     | ok               |
| CL         |       62 | 6.91%    | 5.55%              | -14.32% |     0.28 | 45.26%     | ok               |
| CMCSA      |       81 | -39.46%  | -40.46%            | -41.06% |    -1.04 | 41.60%     | ok               |
| COMP-USD   |       91 | -42.24%  | -69.24%            | -57.88% |    -0.3  | 45.79%     | ok               |
| COP        |       72 | -19.55%  | 6.02%              | -43.96% |    -0.32 | 42.43%     | ok               |
| COST       |       60 | -3.00%   | 23.98%             | -29.73% |    -0.02 | 42.93%     | ok               |
| CRM        |       63 | -39.56%  | -45.62%            | -41.36% |    -0.83 | 42.76%     | ok               |
| CRV-USD    |       70 | -7.84%   | -59.23%            | -39.89% |     0.15 | 36.59%     | ok               |
| CSCO       |       61 | 20.55%   | 133.48%            | -21.79% |     0.47 | 48.25%     | ok               |
| CVX        |       73 | -12.33%  | 26.68%             | -29.13% |    -0.28 | 39.93%     | ok               |
| DASH-USD   |       61 | -41.76%  | 26.21%             | -64.43% |    -0.02 | 29.12%     | ok               |
| DBC        |       60 | -8.42%   | 35.60%             | -25.15% |    -0.26 | 34.28%     | ok               |
| DE         |       74 | -8.65%   | 66.48%             | -25.24% |    -0.09 | 46.92%     | ok               |
| DIA        |       60 | -3.93%   | 33.85%             | -12.94% |    -0.18 | 43.59%     | ok               |
| DIS        |       66 | -18.12%  | -13.47%            | -28.17% |    -0.32 | 45.26%     | ok               |
| DOGE-USD   |       72 | -25.02%  | -71.88%            | -62.31% |    -0.01 | 49.81%     | ok               |
| DOT-USD    |       86 | -61.03%  | -83.15%            | -66.00% |    -0.68 | 47.70%     | ok               |
| DXY-INDEX  |       40 | -2.19%   | 0.36%              | -6.28%  |    -0.33 | 31.17%     | ok               |
| EEM        |       64 | -9.01%   | 62.60%             | -25.67% |    -0.23 | 42.43%     | ok               |
| EFA        |       60 | -7.52%   | 35.30%             | -13.51% |    -0.27 | 43.93%     | ok               |
| EOG        |       81 | -19.84%  | 26.13%             | -48.13% |    -0.39 | 47.75%     | ok               |
| ETC-USD    |       62 | -31.34%  | -66.95%            | -45.54% |    -0.42 | 29.12%     | ok               |
| ETH-USD    |       64 | 145.84%  | -29.92%            | -30.11% |     1.22 | 45.21%     | ok               |
| EWJ        |       62 | -19.21%  | 34.25%             | -30.73% |    -0.63 | 38.27%     | ok               |
| FCX        |       65 | -25.01%  | 73.75%             | -47.47% |    -0.26 | 45.42%     | ok               |
| FET-USD    |       85 | -40.10%  | -79.60%            | -52.82% |    -0.15 | 42.34%     | ok               |
| FIL-USD    |       68 | -49.51%  | -78.41%            | -49.51% |    -0.65 | 32.76%     | ok               |
| FXI        |       44 | -6.16%   | 46.76%             | -23.91% |    -0.07 | 29.95%     | ok               |
| GDX        |       60 | 10.22%   | 197.44%            | -34.99% |     0.29 | 47.92%     | ok               |
| GDXJ       |       66 | -22.87%  | 222.31%            | -44.93% |    -0.21 | 46.09%     | ok               |
| GE         |       76 | 7.59%    | 174.73%            | -27.82% |     0.25 | 52.58%     | ok               |
| GLD        |       50 | 23.50%   | 101.30%            | -16.63% |     0.6  | 48.09%     | ok               |
| GOOGL      |       57 | 77.30%   | 150.84%            | -20.41% |     1.16 | 52.75%     | ok               |
| GRT-USD    |       81 | -6.83%   | -88.46%            | -50.20% |     0.13 | 42.34%     | ok               |
| GS         |       76 | -2.38%   | 179.31%            | -22.13% |     0.05 | 52.08%     | ok               |
| HD         |       71 | -7.53%   | -12.22%            | -17.69% |    -0.12 | 44.59%     | ok               |
| HON        |       93 | -26.82%  | 19.30%             | -29.80% |    -0.72 | 52.41%     | ok               |
| HYG        |       81 | -9.08%   | 3.02%              | -9.59%  |    -1.06 | 33.94%     | ok               |
| IBIT       |       34 | 30.82%   | -1.76%             | -18.95% |     0.66 | 31.80%     | ok               |
| IBM        |       77 | -14.89%  | 11.05%             | -44.74% |    -0.11 | 49.75%     | ok               |
| ICP-USD    |       75 | -20.49%  | -68.96%            | -54.22% |     0.04 | 35.06%     | ok               |
| IEF        |       80 | -10.89%  | -0.99%             | -11.70% |    -1.54 | 33.11%     | ok               |
| IEMG       |       58 | -7.49%   | 57.06%             | -26.84% |    -0.2  | 41.93%     | ok               |
| INJ-USD    |       79 | -52.55%  | -65.74%            | -76.24% |    -0.48 | 39.27%     | ok               |
| INTC       |       68 | 59.68%   | 144.39%            | -60.60% |     0.64 | 49.08%     | ok               |
| INTU       |       67 | -19.54%  | -56.84%            | -42.15% |    -0.23 | 41.60%     | ok               |
| ITA        |       72 | -4.32%   | 80.37%             | -23.75% |    -0.05 | 47.75%     | ok               |
| IWM        |       48 | 9.40%    | 45.21%             | -12.83% |     0.39 | 35.77%     | ok               |
| JNJ        |       68 | 4.23%    | 58.24%             | -17.51% |     0.2  | 50.92%     | ok               |
| JPM        |       77 | -21.46%  | 88.85%             | -33.43% |    -0.52 | 53.41%     | ok               |
| KO         |       51 | 23.75%   | 36.09%             | -8.20%  |     0.85 | 37.94%     | ok               |
| LDO-USD    |       78 | 37.32%   | -78.58%            | -63.49% |     0.55 | 41.38%     | ok               |
| LIN        |       66 | -5.96%   | 12.74%             | -21.53% |    -0.16 | 38.44%     | ok               |
| LINK-USD   |       75 | -13.76%  | -54.99%            | -49.69% |     0.1  | 43.49%     | ok               |
| LLY        |       71 | -27.33%  | 53.50%             | -53.34% |    -0.39 | 48.92%     | ok               |
| LRCX       |       82 | -25.47%  | 246.05%            | -63.39% |    -0.15 | 43.93%     | ok               |
| LTC-USD    |       72 | -30.71%  | -61.52%            | -53.76% |    -0.23 | 50.19%     | ok               |
| MCD        |       75 | -2.55%   | -10.71%            | -18.81% |    -0.05 | 38.10%     | ok               |
| META       |       74 | -34.28%  | 29.58%             | -42.10% |    -0.63 | 47.92%     | ok               |
| MPC        |       69 | -3.17%   | 88.93%             | -44.76% |     0.07 | 48.92%     | ok               |
| MRK        |       69 | -29.73%  | -0.56%             | -35.95% |    -0.7  | 44.09%     | ok               |
| MS         |       77 | -10.18%  | 153.92%            | -27.79% |    -0.16 | 49.58%     | ok               |
| MSFT       |       81 | -37.64%  | -4.26%             | -39.15% |    -0.99 | 47.09%     | ok               |
| MU         |       49 | 269.00%  | 969.54%            | -68.76% |     1.34 | 59.40%     | ok               |
| NEAR-USD   |       85 | -21.10%  | -42.67%            | -60.95% |     0.03 | 41.57%     | ok               |
| NEM        |       72 | -31.13%  | 220.56%            | -38.49% |    -0.33 | 53.08%     | ok               |
| NFLX       |       68 | 26.03%   | 14.89%             | -21.09% |     0.59 | 53.91%     | ok               |
| NKE        |       89 | -37.36%  | -59.55%            | -55.35% |    -0.52 | 43.76%     | ok               |
| NOW        |       78 | 8.05%    | -37.18%            | -27.34% |     0.26 | 45.59%     | ok               |
| NVDA       |       73 | -24.09%  | 156.63%            | -45.02% |    -0.15 | 59.71%     | ok               |
| OP-USD     |       70 | -31.79%  | -92.02%            | -71.26% |    -0.14 | 33.72%     | ok               |
| ORCL       |       70 | 123.52%  | 12.68%             | -29.47% |     1    | 54.91%     | ok               |
| OXY        |       71 | 5.33%    | -4.58%             | -34.15% |     0.21 | 46.42%     | ok               |
| PEP        |       78 | -0.84%   | -18.79%            | -21.35% |     0.04 | 48.09%     | ok               |
| PEPE-USD   |       81 | 3.39%    | -71.85%            | -57.66% |     0.31 | 45.79%     | ok               |
| PFE        |       79 | -41.51%  | -8.21%             | -42.34% |    -1.34 | 36.11%     | ok               |
| PG         |       68 | -19.42%  | -6.82%             | -24.55% |    -0.74 | 39.43%     | ok               |
| PM         |       81 | -3.41%   | 114.89%            | -33.68% |     0.02 | 55.57%     | ok               |
| POL-USD    |       75 | 23.05%   | -75.38%            | -46.45% |     0.45 | 48.47%     | ok               |
| QCOM       |       73 | -15.25%  | 12.69%             | -56.59% |    -0.04 | 46.09%     | ok               |
| QQQ        |       60 | 20.33%   | 62.05%             | -12.88% |     0.58 | 43.59%     | ok               |
| RENDER-USD |       98 | -19.07%  | -63.80%            | -45.00% |     0.1  | 42.28%     | ok               |
| RTX        |       54 | 27.08%   | 116.73%            | -16.99% |     0.66 | 52.25%     | ok               |
| SBUX       |       62 | -18.75%  | 11.81%             | -29.22% |    -0.34 | 39.77%     | ok               |
| SCHW       |       76 | -14.81%  | 53.54%             | -31.92% |    -0.29 | 48.25%     | ok               |
| SHIB-USD   |       74 | -24.29%  | -73.05%            | -47.96% |    -0.1  | 52.11%     | ok               |
| SHY        |       48 | -2.24%   | 0.17%              | -2.85%  |    -0.79 | 34.28%     | ok               |
| SKY-USD    |       74 | -29.07%  | 9.06%              | -44.74% |    -0.34 | 41.00%     | ok               |
| SLB        |       73 | -24.35%  | -1.02%             | -54.23% |    -0.4  | 50.92%     | ok               |
| SLV        |       60 | 43.15%   | 162.38%            | -42.66% |     0.63 | 43.76%     | ok               |
| SMH        |       48 | 80.23%   | 182.97%            | -33.99% |     1.09 | 47.09%     | ok               |
| SNX-USD    |       60 | -21.31%  | -78.38%            | -35.44% |     0.01 | 38.70%     | ok               |
| SOL-USD    |       70 | -39.53%  | -56.28%            | -56.90% |    -0.19 | 59.77%     | ok               |
| SOXX       |       57 | 70.78%   | 162.50%            | -41.89% |     0.95 | 45.92%     | ok               |
| SPY        |       64 | 2.12%    | 47.63%             | -16.47% |     0.13 | 49.42%     | ok               |
| SUSHI-USD  |      100 | -82.18%  | -81.27%            | -85.70% |    -1.3  | 37.16%     | ok               |
| T          |       64 | 37.51%   | 35.85%             | -17.01% |     0.84 | 53.24%     | ok               |
| TGT        |       60 | -12.14%  | -8.93%             | -40.57% |    -0.17 | 38.27%     | ok               |
| TIA-USD    |       93 | -43.09%  | -88.53%            | -68.36% |    -0.28 | 37.16%     | ok               |
| TLT        |       72 | -20.70%  | -10.78%            | -21.87% |    -1.59 | 32.95%     | ok               |
| TMO        |       61 | 16.80%   | -7.97%             | -18.85% |     0.43 | 51.75%     | ok               |
| TMUS       |       70 | 6.55%    | 16.57%             | -25.71% |     0.23 | 47.42%     | ok               |
| TRX-USD    |       68 | 8.91%    | 37.46%             | -22.90% |     0.32 | 48.47%     | ok               |
| TSLA       |       70 | -14.59%  | 85.12%             | -54.91% |     0.05 | 41.26%     | ok               |
| TXN        |       73 | -12.32%  | 80.44%             | -47.39% |    -0.04 | 52.25%     | ok               |
| UNH        |       72 | 37.54%   | -13.44%            | -26.96% |     0.6  | 52.58%     | ok               |
| UNI-USD    |       86 | -70.15%  | -61.84%            | -80.61% |    -0.79 | 45.02%     | ok               |
| UPS        |       72 | -35.66%  | -21.61%            | -38.83% |    -0.7  | 39.60%     | ok               |
| USO        |       68 | 18.17%   | 78.86%             | -43.35% |     0.4  | 34.61%     | ok               |
| VEA        |       56 | -0.35%   | 45.13%             | -17.93% |     0.04 | 43.59%     | ok               |
| VIXY       |       96 | -80.56%  | -62.13%            | -88.16% |    -1.02 | 32.61%     | ok               |
| VNQ        |       71 | -15.77%  | 16.73%             | -24.92% |    -0.66 | 36.94%     | ok               |
| VTI        |       70 | -4.58%   | 46.66%             | -18.77% |    -0.11 | 49.75%     | ok               |
| VWO        |       78 | -13.39%  | 43.68%             | -25.20% |    -0.47 | 43.26%     | ok               |
| VZ         |       83 | -27.34%  | 10.45%             | -27.34% |    -0.92 | 37.44%     | ok               |
| WFC        |       84 | -17.17%  | 57.93%             | -30.87% |    -0.27 | 50.58%     | ok               |
| WIF-USD    |       70 | -43.94%  | -76.06%            | -57.80% |    -0.24 | 33.52%     | ok               |
| WMT        |       63 | 13.28%   | 83.38%             | -21.31% |     0.42 | 50.25%     | ok               |
| XBI        |       66 | -10.02%  | 49.82%             | -18.72% |    -0.18 | 40.77%     | ok               |
| XLB        |       62 | -8.25%   | 16.96%             | -24.41% |    -0.26 | 36.44%     | ok               |
| XLC        |       69 | 11.81%   | 38.83%             | -12.33% |     0.44 | 53.58%     | ok               |
| XLE        |       75 | -5.39%   | 38.12%             | -37.64% |    -0.05 | 45.26%     | ok               |
| XLF        |       76 | -12.51%  | 38.88%             | -23.61% |    -0.42 | 47.92%     | ok               |
| XLI        |       66 | -3.05%   | 48.26%             | -11.79% |    -0.07 | 43.59%     | ok               |
| XLK        |       40 | 65.83%   | 76.13%             | -14.75% |     1.22 | 45.59%     | ok               |
| XLM-USD    |       69 | 0.26%    | -44.65%            | -50.36% |     0.22 | 45.59%     | ok               |
| XLP        |       66 | 4.67%    | 13.16%             | -11.16% |     0.3  | 41.26%     | ok               |
| XLU        |       67 | -5.24%   | 47.97%             | -20.40% |    -0.19 | 39.10%     | ok               |
| XLV        |       70 | -15.90%  | 9.19%              | -19.97% |    -0.79 | 35.94%     | ok               |
| XLY        |       70 | 3.26%    | 24.50%             | -14.01% |     0.17 | 44.43%     | ok               |
| XOM        |       57 | 11.06%   | 48.05%             | -20.29% |     0.37 | 37.27%     | ok               |
| XRP-USD    |       60 | -31.84%  | -57.33%            | -42.76% |    -0.29 | 33.91%     | ok               |
| YFI-USD    |       81 | -64.19%  | -65.18%            | -71.12% |    -1.03 | 40.61%     | ok               |
| ZEC-USD    |       62 | 50.82%   | 1314.11%           | -47.68% |     0.59 | 36.78%     | ok               |

## AAPL Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 26.44%   | 79.63%             | -21.71% |     0.57 |       68 | 53.41%     | ok               |
|          15 | 22.55%   | 79.63%             | -23.86% |     0.5  |       75 | 60.57%     | ok               |
|          30 | 17.28%   | 79.63%             | -20.65% |     0.43 |       61 | 49.25%     | ok               |
|          35 | 14.64%   | 79.63%             | -22.04% |     0.39 |       61 | 47.75%     | ok               |
|          25 | 14.83%   | 79.63%             | -20.03% |     0.38 |       67 | 51.08%     | ok               |

## AAVE-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 10.06%   | -63.31%            | -43.61% |     0.32 |       40 | 31.99%     | ok               |
|          45 | -4.67%   | -63.31%            | -49.19% |     0.15 |       44 | 27.20%     | ok               |
|          35 | -8.77%   | -63.31%            | -51.96% |     0.13 |       50 | 35.25%     | ok               |
|          15 | -51.61%  | -63.31%            | -61.76% |    -0.31 |       82 | 54.21%     | ok               |
|          50 | -33.87%  | -63.31%            | -47.39% |    -0.36 |       42 | 19.73%     | ok               |

## ABBV Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -12.50%  | 42.30%             | -28.51% |    -0.25 |       50 | 36.11%     | ok               |
|          30 | -20.88%  | 42.30%             | -30.55% |    -0.44 |       68 | 47.09%     | ok               |
|          40 | -19.71%  | 42.30%             | -26.61% |    -0.45 |       66 | 40.77%     | ok               |
|          25 | -21.76%  | 42.30%             | -31.26% |    -0.47 |       69 | 48.75%     | ok               |
|          20 | -22.36%  | 42.30%             | -30.60% |    -0.47 |       69 | 50.58%     | ok               |

## ADA-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -78.29%  | -78.44%            | -86.20% |    -0.6  |       57 | 27.20%     | ok               |
|          45 | -80.61%  | -78.44%            | -88.22% |    -0.64 |       60 | 31.99%     | ok               |
|          35 | -83.23%  | -78.44%            | -89.51% |    -0.69 |       80 | 42.72%     | ok               |
|          30 | -83.44%  | -78.44%            | -88.94% |    -0.69 |       90 | 47.13%     | ok               |
|          15 | -86.80%  | -78.44%            | -90.93% |    -0.71 |       78 | 63.79%     | ok               |

## ADBE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 1.24%    | -60.43%            | -22.53% |     0.14 |       72 | 49.08%     | ok               |
|          40 | -11.88%  | -60.43%            | -24.87% |    -0.11 |       70 | 42.10%     | ok               |
|          25 | -17.29%  | -60.43%            | -31.11% |    -0.12 |       48 | 61.06%     | ok               |
|          20 | -27.87%  | -60.43%            | -32.14% |    -0.3  |       50 | 63.73%     | ok               |
|          15 | -31.15%  | -60.43%            | -33.14% |    -0.36 |       59 | 65.56%     | ok               |

## AGG Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -6.51%   | 0.40%              | -10.25% |    -1.07 |       71 | 32.28%     | ok               |
|          50 | -5.00%   | 0.40%              | -7.92%  |    -1.1  |       48 | 17.47%     | ok               |
|          45 | -5.65%   | 0.40%              | -7.91%  |    -1.13 |       54 | 21.63%     | ok               |
|          20 | -7.91%   | 0.40%              | -11.43% |    -1.16 |       75 | 37.77%     | ok               |
|          25 | -8.08%   | 0.40%              | -12.07% |    -1.23 |       75 | 36.11%     | ok               |

## ALGO-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -50.43%  | -68.76%            | -53.13% |    -0.57 |       86 | 38.12%     | ok               |
|          15 | -63.17%  | -68.76%            | -69.75% |    -0.71 |       86 | 50.57%     | ok               |
|          25 | -61.89%  | -68.76%            | -72.48% |    -0.74 |       84 | 45.02%     | ok               |
|          20 | -65.54%  | -68.76%            | -71.20% |    -0.8  |       86 | 48.08%     | ok               |
|          50 | -45.64%  | -68.76%            | -48.43% |    -0.81 |       42 | 16.86%     | ok               |

## AMAT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -21.92%  | 180.41%            | -54.05% |    -0.07 |       68 | 60.73%     | ok               |
|          30 | -33.68%  | 180.41%            | -57.21% |    -0.3  |       71 | 51.75%     | ok               |
|          35 | -34.15%  | 180.41%            | -55.26% |    -0.32 |       73 | 49.42%     | ok               |
|          50 | -34.00%  | 180.41%            | -48.72% |    -0.36 |       52 | 37.27%     | ok               |
|          20 | -41.29%  | 180.41%            | -60.16% |    -0.4  |       74 | 57.07%     | ok               |

## AMD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 6.74%    | 212.86%            | -44.26% |     0.27 |       54 | 30.62%     | ok               |
|          40 | 5.86%    | 212.86%            | -43.98% |     0.27 |       52 | 35.77%     | ok               |
|          35 | -5.47%   | 212.86%            | -50.71% |     0.16 |       60 | 37.27%     | ok               |
|          45 | -14.79%  | 212.86%            | -53.24% |     0.04 |       60 | 33.44%     | ok               |
|          30 | -17.93%  | 212.86%            | -56.46% |     0.02 |       61 | 39.77%     | ok               |

## AMGN Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -11.99%  | 31.93%             | -26.65% |    -0.18 |       71 | 52.25%     | ok               |
|          35 | -11.34%  | 31.93%             | -31.29% |    -0.19 |       67 | 42.60%     | ok               |
|          15 | -16.87%  | 31.93%             | -27.98% |    -0.28 |       70 | 57.40%     | ok               |
|          30 | -15.48%  | 31.93%             | -34.19% |    -0.29 |       71 | 46.42%     | ok               |
|          25 | -18.92%  | 31.93%             | -33.47% |    -0.37 |       67 | 48.75%     | ok               |

## AMZN Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -18.14%  | 41.40%             | -27.15% |    -0.54 |       52 | 29.12%     | ok               |
|          50 | -24.45%  | 41.40%             | -34.08% |    -0.87 |       50 | 23.13%     | ok               |
|          45 | -27.24%  | 41.40%             | -34.08% |    -0.96 |       54 | 26.12%     | ok               |
|          35 | -31.60%  | 41.40%             | -38.29% |    -1    |       68 | 32.78%     | ok               |
|          30 | -37.69%  | 41.40%             | -42.48% |    -1.14 |       80 | 38.27%     | ok               |

## APT-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 19.10%   | -89.45%            | -46.73% |     0.42 |       40 | 18.97%     | ok               |
|          45 | -11.65%  | -89.45%            | -63.86% |     0.05 |       56 | 24.52%     | ok               |
|          20 | -36.87%  | -89.45%            | -70.51% |    -0.13 |       71 | 50.38%     | ok               |
|          40 | -29.96%  | -89.45%            | -63.33% |    -0.16 |       62 | 29.69%     | ok               |
|          35 | -35.09%  | -89.45%            | -64.08% |    -0.2  |       66 | 35.44%     | ok               |

## ARB-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 30.19%   | -81.89%            | -54.02% |     0.5  |       89 | 56.90%     | ok               |
|          40 | 6.27%    | -81.89%            | -44.30% |     0.29 |       56 | 31.03%     | ok               |
|          20 | -2.11%   | -81.89%            | -59.00% |     0.26 |       75 | 50.38%     | ok               |
|          45 | -0.04%   | -81.89%            | -47.43% |     0.2  |       60 | 24.14%     | ok               |
|          25 | -12.76%  | -81.89%            | -55.53% |     0.15 |       76 | 45.98%     | ok               |

## ARKK Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -30.75%  | 48.61%             | -37.76% |    -0.41 |       96 | 51.58%     | ok               |
|          20 | -34.84%  | 48.61%             | -37.67% |    -0.53 |       91 | 46.92%     | ok               |
|          30 | -34.89%  | 48.61%             | -36.39% |    -0.62 |       83 | 39.93%     | ok               |
|          35 | -36.01%  | 48.61%             | -37.48% |    -0.68 |       82 | 37.60%     | ok               |
|          40 | -37.36%  | 48.61%             | -39.32% |    -0.76 |       74 | 32.78%     | ok               |

## ATOM-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -65.52%  | -69.85%            | -71.00% |    -1    |       93 | 50.96%     | ok               |
|          15 | -70.81%  | -69.85%            | -72.57% |    -1.07 |       91 | 61.69%     | ok               |
|          45 | -62.07%  | -69.85%            | -67.78% |    -1.2  |       72 | 28.93%     | ok               |
|          30 | -69.32%  | -69.85%            | -74.39% |    -1.21 |       88 | 44.44%     | ok               |
|          20 | -72.86%  | -69.85%            | -74.75% |    -1.21 |       97 | 54.60%     | ok               |

## AVAX-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 3.29%    | -73.89%            | -34.50% |     0.21 |       32 | 18.20%     | ok               |
|          45 | -6.13%   | -73.89%            | -41.07% |     0.07 |       36 | 22.03%     | ok               |
|          40 | -15.98%  | -73.89%            | -45.60% |    -0.06 |       40 | 24.90%     | ok               |
|          15 | -28.59%  | -73.89%            | -52.46% |    -0.08 |       73 | 52.87%     | ok               |
|          25 | -29.83%  | -73.89%            | -53.21% |    -0.16 |       69 | 42.72%     | ok               |

## AVGO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 16.61%   | 207.74%            | -35.84% |     0.36 |       56 | 30.62%     | ok               |
|          30 | 15.74%   | 207.74%            | -35.76% |     0.35 |       64 | 42.10%     | ok               |
|          40 | 14.36%   | 207.74%            | -40.70% |     0.33 |       62 | 35.94%     | ok               |
|          25 | 13.30%   | 207.74%            | -38.01% |     0.32 |       72 | 43.59%     | ok               |
|          45 | 11.86%   | 207.74%            | -41.66% |     0.31 |       56 | 33.94%     | ok               |

## BA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 26.03%   | 0.80%              | -13.34% |     0.67 |       42 | 31.45%     | ok               |
|          35 | 30.46%   | 0.80%              | -23.77% |     0.59 |       72 | 44.59%     | ok               |
|          40 | 20.11%   | 0.80%              | -23.90% |     0.47 |       46 | 38.60%     | ok               |
|          25 | 10.59%   | 0.80%              | -32.48% |     0.29 |       70 | 52.58%     | ok               |
|          30 | 7.60%    | 0.80%              | -30.56% |     0.25 |       67 | 49.25%     | ok               |

## BAC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 5.77%    | 79.60%             | -18.35% |     0.24 |       60 | 38.10%     | ok               |
|          35 | 0.87%    | 79.60%             | -27.11% |     0.1  |       70 | 46.42%     | ok               |
|          20 | 0.22%    | 79.60%             | -20.73% |     0.09 |       78 | 54.91%     | ok               |
|          50 | -0.08%   | 79.60%             | -19.12% |     0.06 |       60 | 34.61%     | ok               |
|          40 | -1.59%   | 79.60%             | -22.59% |     0.02 |       64 | 41.10%     | ok               |

## BCH-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 17.70%   | -32.62%            | -45.63% |     0.4  |       69 | 54.02%     | ok               |
|          15 | 4.89%    | -32.62%            | -48.58% |     0.28 |       80 | 58.81%     | ok               |
|          30 | 5.44%    | -32.62%            | -53.87% |     0.27 |       76 | 48.08%     | ok               |
|          25 | 4.69%    | -32.62%            | -51.09% |     0.27 |       70 | 50.19%     | ok               |
|          35 | -17.05%  | -32.62%            | -64.08% |    -0.02 |       70 | 44.25%     | ok               |

## BITO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 2.46%    | -68.54%            | -31.98% |     0.18 |       52 | 23.96%     | ok               |
|          30 | -14.71%  | -68.54%            | -42.82% |    -0.01 |       80 | 40.77%     | ok               |
|          15 | -21.00%  | -68.54%            | -48.38% |    -0.05 |       89 | 49.75%     | ok               |
|          45 | -13.80%  | -68.54%            | -41.96% |    -0.05 |       60 | 27.62%     | ok               |
|          40 | -17.65%  | -68.54%            | -44.44% |    -0.08 |       64 | 32.45%     | ok               |

## BLK Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -3.24%   | 30.50%             | -21.48% |    -0.01 |       78 | 47.59%     | ok               |
|          35 | -2.88%   | 30.50%             | -19.25% |    -0.02 |       78 | 38.77%     | ok               |
|          40 | -6.47%   | 30.50%             | -21.33% |    -0.15 |       72 | 34.78%     | ok               |
|          25 | -8.33%   | 30.50%             | -24.54% |    -0.17 |       73 | 45.09%     | ok               |
|          30 | -9.04%   | 30.50%             | -25.48% |    -0.2  |       73 | 42.60%     | ok               |

## BND Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -6.35%   | 0.42%              | -9.41%  |    -0.92 |       65 | 39.10%     | ok               |
|          25 | -7.05%   | 0.42%              | -10.50% |    -1.07 |       69 | 37.10%     | ok               |
|          30 | -7.22%   | 0.42%              | -9.98%  |    -1.15 |       67 | 33.44%     | ok               |
|          15 | -8.56%   | 0.42%              | -11.19% |    -1.23 |       75 | 41.93%     | ok               |
|          45 | -7.47%   | 0.42%              | -9.57%  |    -1.43 |       52 | 23.13%     | ok               |

## BONK-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 170.78%  | -81.92%            | -35.57% |     1.24 |       48 | 22.41%     | ok               |
|          25 | 162.01%  | -81.92%            | -51.34% |     1.01 |       69 | 48.85%     | ok               |
|          15 | 167.00%  | -81.92%            | -62.48% |     0.99 |       72 | 58.05%     | ok               |
|          20 | 137.59%  | -81.92%            | -58.35% |     0.94 |       69 | 53.26%     | ok               |
|          40 | 82.85%   | -81.92%            | -53.34% |     0.79 |       54 | 35.06%     | ok               |

## BTC-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 52.04%   | -31.48%            | -14.50% |     0.95 |       46 | 34.48%     | ok               |
|          45 | 37.57%   | -31.48%            | -15.18% |     0.76 |       46 | 30.84%     | ok               |
|          35 | 36.20%   | -31.48%            | -22.12% |     0.7  |       70 | 41.38%     | ok               |
|          30 | 19.84%   | -31.48%            | -21.75% |     0.45 |       74 | 48.08%     | ok               |
|          50 | 11.33%   | -31.48%            | -18.05% |     0.34 |       44 | 25.48%     | ok               |

## C Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -6.29%   | 140.24%            | -22.28% |    -0.1  |       64 | 36.11%     | ok               |
|          45 | -18.56%  | 140.24%            | -30.30% |    -0.43 |       76 | 40.27%     | ok               |
|          25 | -27.05%  | 140.24%            | -34.97% |    -0.5  |       71 | 52.91%     | ok               |
|          15 | -29.52%  | 140.24%            | -36.36% |    -0.53 |       74 | 59.90%     | ok               |
|          20 | -29.49%  | 140.24%            | -36.33% |    -0.55 |       79 | 55.91%     | ok               |

## CAT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 19.71%   | 169.85%            | -21.02% |     0.42 |       72 | 55.24%     | ok               |
|          25 | 19.82%   | 169.85%            | -26.37% |     0.42 |       68 | 58.07%     | ok               |
|          20 | 18.39%   | 169.85%            | -25.65% |     0.4  |       78 | 61.56%     | ok               |
|          45 | 14.82%   | 169.85%            | -27.12% |     0.36 |       56 | 43.93%     | ok               |
|          35 | 11.85%   | 169.85%            | -27.72% |     0.31 |       70 | 48.75%     | ok               |

## CL Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 8.83%    | 5.55%              | -11.80% |     0.4  |       44 | 28.95%     | ok               |
|          30 | 6.91%    | 5.55%              | -14.32% |     0.28 |       62 | 45.26%     | ok               |
|          35 | 1.82%    | 5.55%              | -13.83% |     0.12 |       64 | 41.60%     | ok               |
|          45 | 1.73%    | 5.55%              | -14.13% |     0.12 |       50 | 32.11%     | ok               |
|          40 | -1.13%   | 5.55%              | -12.70% |     0.01 |       58 | 36.27%     | ok               |

## CMCSA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -37.84%  | -40.46%            | -44.10% |    -0.85 |       91 | 56.74%     | ok               |
|          30 | -39.46%  | -40.46%            | -41.06% |    -1.04 |       81 | 41.60%     | ok               |
|          25 | -43.29%  | -40.46%            | -43.52% |    -1.16 |       91 | 47.09%     | ok               |
|          50 | -30.84%  | -40.46%            | -32.53% |    -1.23 |       48 | 14.14%     | ok               |
|          35 | -44.25%  | -40.46%            | -45.72% |    -1.29 |       91 | 36.11%     | ok               |

## COMP-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -8.10%   | -69.24%            | -38.71% |     0.09 |       46 | 20.31%     | ok               |
|          30 | -42.24%  | -69.24%            | -57.88% |    -0.3  |       91 | 45.79%     | ok               |
|          25 | -46.70%  | -69.24%            | -61.30% |    -0.34 |       89 | 52.11%     | ok               |
|          40 | -43.93%  | -69.24%            | -50.01% |    -0.43 |       72 | 33.72%     | ok               |
|          15 | -55.71%  | -69.24%            | -66.20% |    -0.46 |      107 | 63.60%     | ok               |

## COP Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -1.65%   | 6.02%              | -34.85% |     0.05 |       48 | 28.45%     | ok               |
|          45 | -13.27%  | 6.02%              | -41.14% |    -0.23 |       62 | 31.78%     | ok               |
|          35 | -15.14%  | 6.02%              | -43.58% |    -0.23 |       73 | 38.94%     | ok               |
|          30 | -19.55%  | 6.02%              | -43.96% |    -0.32 |       72 | 42.43%     | ok               |
|          40 | -18.75%  | 6.02%              | -46.86% |    -0.35 |       68 | 34.94%     | ok               |

## COST Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 8.21%    | 23.98%             | -24.32% |     0.3  |       66 | 49.42%     | ok               |
|          25 | 6.61%    | 23.98%             | -24.73% |     0.26 |       63 | 46.59%     | ok               |
|          35 | 1.65%    | 23.98%             | -26.58% |     0.12 |       54 | 39.93%     | ok               |
|          30 | -3.00%   | 23.98%             | -29.73% |    -0.02 |       60 | 42.93%     | ok               |
|          15 | -5.92%   | 23.98%             | -27.30% |    -0.08 |       69 | 52.91%     | ok               |

## CRM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -35.79%  | -45.62%            | -44.67% |    -0.57 |       90 | 54.91%     | ok               |
|          35 | -29.63%  | -45.62%            | -33.08% |    -0.59 |       60 | 37.94%     | ok               |
|          40 | -34.83%  | -45.62%            | -39.11% |    -0.8  |       66 | 33.94%     | ok               |
|          20 | -43.35%  | -45.62%            | -45.69% |    -0.82 |       74 | 48.59%     | ok               |
|          30 | -39.56%  | -45.62%            | -41.36% |    -0.83 |       63 | 42.76%     | ok               |

## CRV-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 16.06%   | -59.23%            | -37.78% |     0.38 |       72 | 31.99%     | ok               |
|          45 | 1.84%    | -59.23%            | -42.29% |     0.22 |       58 | 21.26%     | ok               |
|          40 | -3.85%   | -59.23%            | -38.86% |     0.17 |       62 | 27.59%     | ok               |
|          50 | -1.99%   | -59.23%            | -29.30% |     0.16 |       48 | 17.62%     | ok               |
|          30 | -7.84%   | -59.23%            | -39.89% |     0.15 |       70 | 36.59%     | ok               |

## CSCO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 32.11%   | 133.48%            | -19.34% |     0.7  |       50 | 37.10%     | ok               |
|          45 | 27.64%   | 133.48%            | -19.34% |     0.61 |       51 | 38.77%     | ok               |
|          35 | 22.76%   | 133.48%            | -23.68% |     0.51 |       53 | 45.59%     | ok               |
|          25 | 21.12%   | 133.48%            | -23.28% |     0.48 |       65 | 50.25%     | ok               |
|          30 | 20.55%   | 133.48%            | -21.79% |     0.47 |       61 | 48.25%     | ok               |

## CVX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -6.42%   | 26.68%             | -27.34% |    -0.13 |       75 | 34.94%     | ok               |
|          25 | -8.65%   | 26.68%             | -24.33% |    -0.16 |       73 | 42.60%     | ok               |
|          45 | -7.63%   | 26.68%             | -28.83% |    -0.17 |       65 | 31.11%     | ok               |
|          35 | -8.59%   | 26.68%             | -28.85% |    -0.18 |       67 | 37.10%     | ok               |
|          50 | -8.16%   | 26.68%             | -30.69% |    -0.24 |       58 | 26.46%     | ok               |

## DASH-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 108.17%  | 26.21%             | -27.82% |     0.88 |       38 | 15.33%     | ok               |
|          40 | 58.92%   | 26.21%             | -31.16% |     0.64 |       44 | 21.84%     | ok               |
|          45 | 50.09%   | 26.21%             | -36.55% |     0.6  |       42 | 17.43%     | ok               |
|          35 | -38.60%  | 26.21%             | -63.23% |     0.01 |       67 | 26.25%     | ok               |
|          30 | -41.76%  | 26.21%             | -64.43% |    -0.02 |       61 | 29.12%     | ok               |

## DBC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -2.96%   | 35.60%             | -26.53% |    -0.04 |       72 | 39.77%     | ok               |
|          50 | -2.79%   | 35.60%             | -20.31% |    -0.06 |       42 | 22.30%     | ok               |
|          35 | -5.60%   | 35.60%             | -23.35% |    -0.15 |       62 | 32.95%     | ok               |
|          45 | -5.48%   | 35.60%             | -21.46% |    -0.16 |       58 | 25.96%     | ok               |
|          25 | -6.07%   | 35.60%             | -25.55% |    -0.16 |       62 | 36.11%     | ok               |

## DE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -4.05%   | 66.48%             | -22.53% |    -0.02 |       70 | 31.45%     | ok               |
|          20 | -7.57%   | 66.48%             | -29.90% |    -0.06 |       76 | 52.25%     | ok               |
|          45 | -6.02%   | 66.48%             | -26.22% |    -0.06 |       70 | 35.94%     | ok               |
|          30 | -8.65%   | 66.48%             | -25.24% |    -0.09 |       74 | 46.92%     | ok               |
|          25 | -9.86%   | 66.48%             | -27.66% |    -0.11 |       78 | 49.58%     | ok               |

## DIA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | -1.90%   | 33.85%             | -13.15% |    -0.07 |       60 | 41.43%     | ok               |
|          25 | -2.43%   | 33.85%             | -11.28% |    -0.09 |       60 | 44.76%     | ok               |
|          30 | -3.93%   | 33.85%             | -12.94% |    -0.18 |       60 | 43.59%     | ok               |
|          20 | -5.81%   | 33.85%             | -13.85% |    -0.27 |       66 | 47.25%     | ok               |
|          40 | -5.90%   | 33.85%             | -15.06% |    -0.32 |       66 | 38.60%     | ok               |

## DIS Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 17.59%   | -13.47%            | -14.24% |     0.56 |       48 | 26.79%     | ok               |
|          40 | -9.42%   | -13.47%            | -24.07% |    -0.13 |       65 | 35.94%     | ok               |
|          45 | -8.60%   | -13.47%            | -16.54% |    -0.14 |       53 | 30.78%     | ok               |
|          15 | -16.31%  | -13.47%            | -31.15% |    -0.23 |       91 | 56.74%     | ok               |
|          35 | -16.25%  | -13.47%            | -25.70% |    -0.28 |       75 | 42.26%     | ok               |

## DOGE-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 5.04%    | -71.88%            | -59.36% |     0.33 |       80 | 65.90%     | ok               |
|          20 | -9.55%   | -71.88%            | -57.37% |     0.18 |       79 | 60.34%     | ok               |
|          25 | -10.38%  | -71.88%            | -55.33% |     0.17 |       69 | 55.36%     | ok               |
|          30 | -25.02%  | -71.88%            | -62.31% |    -0.01 |       72 | 49.81%     | ok               |
|          35 | -47.23%  | -71.88%            | -61.79% |    -0.41 |       68 | 43.49%     | ok               |

## DOT-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -36.94%  | -83.15%            | -48.37% |    -0.49 |       58 | 25.86%     | ok               |
|          45 | -39.69%  | -83.15%            | -51.57% |    -0.5  |       50 | 31.03%     | ok               |
|          35 | -56.64%  | -83.15%            | -62.33% |    -0.6  |       76 | 41.38%     | ok               |
|          40 | -48.55%  | -83.15%            | -55.65% |    -0.65 |       54 | 34.10%     | ok               |
|          30 | -61.03%  | -83.15%            | -66.00% |    -0.68 |       86 | 47.70%     | ok               |

## DXY-INDEX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -2.19%   | 0.36%              | -6.28%  |    -0.33 |       40 | 31.17%     | ok               |
|          15 | -3.87%   | 0.36%              | -11.37% |    -0.33 |       82 | 77.06%     | ok               |
|          40 | -4.51%   | 0.36%              | -7.30%  |    -0.57 |       72 | 50.43%     | ok               |
|          35 | -5.59%   | 0.36%              | -9.74%  |    -0.68 |       75 | 56.93%     | ok               |
|          30 | -5.98%   | 0.36%              | -9.61%  |    -0.69 |       74 | 61.47%     | ok               |

## EEM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -4.56%   | 62.60%             | -19.52% |    -0.1  |       64 | 38.77%     | ok               |
|          50 | -4.54%   | 62.60%             | -15.88% |    -0.11 |       52 | 34.78%     | ok               |
|          35 | -5.22%   | 62.60%             | -23.88% |    -0.11 |       66 | 40.77%     | ok               |
|          45 | -5.64%   | 62.60%             | -17.36% |    -0.15 |       54 | 36.44%     | ok               |
|          25 | -8.10%   | 62.60%             | -25.60% |    -0.2  |       65 | 43.76%     | ok               |

## EFA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -2.61%   | 35.30%             | -10.80% |    -0.03 |       62 | 51.91%     | ok               |
|          30 | -7.52%   | 35.30%             | -13.51% |    -0.27 |       60 | 43.93%     | ok               |
|          20 | -9.37%   | 35.30%             | -12.73% |    -0.32 |       69 | 48.92%     | ok               |
|          40 | -8.92%   | 35.30%             | -15.38% |    -0.36 |       64 | 40.10%     | ok               |
|          50 | -8.66%   | 35.30%             | -17.56% |    -0.38 |       54 | 35.77%     | ok               |

## EOG Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -19.84%  | 26.13%             | -48.13% |    -0.39 |       81 | 47.75%     | ok               |
|          40 | -19.95%  | 26.13%             | -43.26% |    -0.44 |       66 | 37.27%     | ok               |
|          35 | -20.73%  | 26.13%             | -46.26% |    -0.45 |       79 | 42.43%     | ok               |
|          45 | -19.82%  | 26.13%             | -43.17% |    -0.47 |       60 | 33.78%     | ok               |
|          25 | -23.91%  | 26.13%             | -51.99% |    -0.47 |       82 | 50.75%     | ok               |

## ETC-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 1.95%    | -66.95%            | -27.89% |     0.16 |       24 | 15.71%     | ok               |
|          45 | -8.31%   | -66.95%            | -35.44% |    -0.02 |       24 | 17.43%     | ok               |
|          35 | -11.42%  | -66.95%            | -42.62% |    -0.05 |       42 | 25.10%     | ok               |
|          40 | -15.42%  | -66.95%            | -40.48% |    -0.15 |       38 | 21.07%     | ok               |
|          30 | -31.34%  | -66.95%            | -45.54% |    -0.42 |       62 | 29.12%     | ok               |

## ETH-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 145.84%  | -29.92%            | -30.11% |     1.22 |       64 | 45.21%     | ok               |
|          30 | 110.62%  | -29.92%            | -32.89% |     1.02 |       66 | 53.83%     | ok               |
|          15 | 48.63%   | -29.92%            | -42.74% |     0.63 |       75 | 68.77%     | ok               |
|          40 | 42.28%   | -29.92%            | -33.11% |     0.63 |       60 | 37.36%     | ok               |
|          20 | 47.05%   | -29.92%            | -39.10% |     0.63 |       80 | 63.03%     | ok               |

## EWJ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -19.21%  | 34.25%             | -30.73% |    -0.63 |       62 | 38.27%     | ok               |
|          20 | -20.58%  | 34.25%             | -31.32% |    -0.67 |       58 | 40.27%     | ok               |
|          25 | -22.87%  | 34.25%             | -31.18% |    -0.77 |       58 | 39.27%     | ok               |
|          45 | -19.98%  | 34.25%             | -27.68% |    -0.77 |       58 | 30.45%     | ok               |
|          35 | -23.08%  | 34.25%             | -32.54% |    -0.8  |       68 | 36.61%     | ok               |

## FCX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -0.61%   | 73.75%             | -27.70% |     0.12 |       54 | 29.95%     | ok               |
|          45 | -4.90%   | 73.75%             | -35.18% |     0.06 |       54 | 34.44%     | ok               |
|          40 | -16.23%  | 73.75%             | -43.57% |    -0.13 |       64 | 38.77%     | ok               |
|          30 | -25.01%  | 73.75%             | -47.47% |    -0.26 |       65 | 45.42%     | ok               |
|          35 | -29.63%  | 73.75%             | -50.71% |    -0.36 |       71 | 43.59%     | ok               |

## FET-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -2.41%   | -79.60%            | -59.54% |     0.29 |       88 | 53.26%     | ok               |
|          15 | -18.10%  | -79.60%            | -59.58% |     0.17 |       84 | 57.09%     | ok               |
|          25 | -36.15%  | -79.60%            | -60.09% |    -0.07 |       91 | 46.93%     | ok               |
|          30 | -40.10%  | -79.60%            | -52.82% |    -0.15 |       85 | 42.34%     | ok               |
|          35 | -54.39%  | -79.60%            | -61.76% |    -0.51 |       73 | 34.10%     | ok               |

## FIL-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -20.28%  | -78.41%            | -36.87% |    -0.15 |       46 | 22.99%     | ok               |
|          35 | -44.49%  | -78.41%            | -44.75% |    -0.58 |       56 | 27.39%     | ok               |
|          45 | -38.76%  | -78.41%            | -41.68% |    -0.58 |       42 | 17.24%     | ok               |
|          30 | -49.51%  | -78.41%            | -49.51% |    -0.65 |       68 | 32.76%     | ok               |
|          50 | -39.00%  | -78.41%            | -44.95% |    -0.69 |       36 | 12.64%     | ok               |

## FXI Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -6.14%   | 46.76%             | -22.57% |    -0.07 |       44 | 31.28%     | ok               |
|          30 | -6.16%   | 46.76%             | -23.91% |    -0.07 |       44 | 29.95%     | ok               |
|          45 | -6.49%   | 46.76%             | -26.75% |    -0.09 |       44 | 24.63%     | ok               |
|          15 | -9.95%   | 46.76%             | -21.68% |    -0.15 |       54 | 34.94%     | ok               |
|          50 | -9.19%   | 46.76%             | -24.76% |    -0.18 |       44 | 21.63%     | ok               |

## GDX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 15.97%   | 197.44%            | -35.59% |     0.36 |       73 | 52.58%     | ok               |
|          40 | 12.76%   | 197.44%            | -31.87% |     0.33 |       64 | 42.76%     | ok               |
|          30 | 10.22%   | 197.44%            | -34.99% |     0.29 |       60 | 47.92%     | ok               |
|          35 | 7.91%    | 197.44%            | -32.37% |     0.25 |       68 | 45.09%     | ok               |
|          25 | 4.88%    | 197.44%            | -38.90% |     0.21 |       63 | 49.42%     | ok               |

## GDXJ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -10.81%  | 222.31%            | -45.05% |     0.02 |       67 | 52.41%     | ok               |
|          50 | -18.94%  | 222.31%            | -44.94% |    -0.2  |       58 | 37.94%     | ok               |
|          30 | -22.87%  | 222.31%            | -44.93% |    -0.21 |       66 | 46.09%     | ok               |
|          25 | -27.96%  | 222.31%            | -47.26% |    -0.27 |       70 | 49.25%     | ok               |
|          35 | -26.51%  | 222.31%            | -43.49% |    -0.29 |       68 | 43.76%     | ok               |

## GE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 26.81%   | 174.73%            | -22.29% |     0.56 |       66 | 39.10%     | ok               |
|          45 | 17.24%   | 174.73%            | -25.68% |     0.41 |       74 | 41.93%     | ok               |
|          20 | 11.07%   | 174.73%            | -26.63% |     0.3  |       71 | 56.24%     | ok               |
|          35 | 7.83%    | 174.73%            | -27.11% |     0.25 |       80 | 47.42%     | ok               |
|          30 | 7.59%    | 174.73%            | -27.82% |     0.25 |       76 | 52.58%     | ok               |

## GLD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 30.35%   | 101.30%            | -14.61% |     0.72 |       48 | 50.75%     | ok               |
|          25 | 29.67%   | 101.30%            | -14.61% |     0.72 |       48 | 49.25%     | ok               |
|          30 | 23.50%   | 101.30%            | -16.63% |     0.6  |       50 | 48.09%     | ok               |
|          15 | 22.37%   | 101.30%            | -17.54% |     0.55 |       50 | 54.91%     | ok               |
|          35 | 17.08%   | 101.30%            | -17.29% |     0.48 |       54 | 46.09%     | ok               |

## GOOGL Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 81.69%   | 150.84%            | -18.25% |     1.23 |       59 | 49.25%     | ok               |
|          30 | 77.30%   | 150.84%            | -20.41% |     1.16 |       57 | 52.75%     | ok               |
|          45 | 68.54%   | 150.84%            | -14.13% |     1.16 |       54 | 42.26%     | ok               |
|          25 | 74.60%   | 150.84%            | -19.76% |     1.12 |       55 | 54.74%     | ok               |
|          50 | 60.60%   | 150.84%            | -14.89% |     1.09 |       48 | 37.27%     | ok               |

## GRT-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 14.84%   | -88.46%            | -36.42% |     0.37 |       44 | 21.65%     | ok               |
|          15 | -2.51%   | -88.46%            | -49.67% |     0.23 |       73 | 60.73%     | ok               |
|          20 | -3.79%   | -88.46%            | -46.47% |     0.2  |       79 | 55.36%     | ok               |
|          35 | -0.35%   | -88.46%            | -43.55% |     0.2  |       62 | 36.78%     | ok               |
|          45 | -0.96%   | -88.46%            | -41.78% |     0.16 |       54 | 27.20%     | ok               |

## GS Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 21.11%   | 179.31%            | -20.56% |     0.47 |       74 | 61.06%     | ok               |
|          20 | 4.59%    | 179.31%            | -23.19% |     0.19 |       74 | 57.07%     | ok               |
|          40 | 0.08%    | 179.31%            | -17.88% |     0.09 |       72 | 45.26%     | ok               |
|          25 | -0.70%   | 179.31%            | -23.32% |     0.09 |       74 | 54.58%     | ok               |
|          30 | -2.38%   | 179.31%            | -22.13% |     0.05 |       76 | 52.08%     | ok               |

## HD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -7.53%   | -12.22%            | -17.69% |    -0.12 |       71 | 44.59%     | ok               |
|          25 | -8.25%   | -12.22%            | -18.51% |    -0.14 |       70 | 46.59%     | ok               |
|          15 | -17.75%  | -12.22%            | -27.53% |    -0.37 |      110 | 55.57%     | ok               |
|          35 | -15.13%  | -12.22%            | -22.98% |    -0.38 |       80 | 40.43%     | ok               |
|          40 | -13.89%  | -12.22%            | -19.63% |    -0.39 |       84 | 34.11%     | ok               |

## HON Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -13.43%  | 19.30%             | -21.17% |    -0.4  |       72 | 31.78%     | ok               |
|          45 | -15.16%  | 19.30%             | -19.99% |    -0.43 |       74 | 36.77%     | ok               |
|          40 | -23.52%  | 19.30%             | -26.29% |    -0.66 |       76 | 41.10%     | ok               |
|          35 | -24.98%  | 19.30%             | -27.37% |    -0.69 |       91 | 47.42%     | ok               |
|          30 | -26.82%  | 19.30%             | -29.80% |    -0.72 |       93 | 52.41%     | ok               |

## HYG Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -7.98%   | 3.02%              | -7.98%  |    -0.96 |       70 | 29.28%     | ok               |
|          15 | -9.49%   | 3.02%              | -10.34% |    -1.03 |       88 | 40.93%     | ok               |
|          20 | -9.23%   | 3.02%              | -10.34% |    -1.03 |       86 | 38.77%     | ok               |
|          25 | -9.38%   | 3.02%              | -10.11% |    -1.06 |       83 | 36.61%     | ok               |
|          30 | -9.08%   | 3.02%              | -9.59%  |    -1.06 |       81 | 33.94%     | ok               |

## IBIT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 53.73%   | -1.76%             | -17.37% |     1.06 |       22 | 22.12%     | ok               |
|          15 | 56.91%   | -1.76%             | -19.20% |     0.95 |       40 | 39.40%     | ok               |
|          45 | 44.27%   | -1.76%             | -17.37% |     0.9  |       26 | 23.50%     | ok               |
|          40 | 38.04%   | -1.76%             | -17.78% |     0.8  |       26 | 25.35%     | ok               |
|          30 | 30.82%   | -1.76%             | -18.95% |     0.66 |       34 | 31.80%     | ok               |

## IBM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -6.47%   | 11.05%             | -43.33% |     0.06 |       93 | 61.90%     | ok               |
|          30 | -14.89%  | 11.05%             | -44.74% |    -0.11 |       77 | 49.75%     | ok               |
|          20 | -18.63%  | 11.05%             | -48.00% |    -0.15 |       75 | 54.41%     | ok               |
|          35 | -17.08%  | 11.05%             | -44.74% |    -0.15 |       71 | 45.42%     | ok               |
|          25 | -26.16%  | 11.05%             | -51.09% |    -0.3  |       74 | 52.41%     | ok               |

## ICP-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 1.02%    | -68.96%            | -32.85% |     0.21 |       50 | 23.75%     | ok               |
|          35 | -8.66%   | -68.96%            | -42.21% |     0.11 |       60 | 29.12%     | ok               |
|          30 | -20.49%  | -68.96%            | -54.22% |     0.04 |       75 | 35.06%     | ok               |
|          50 | -18.12%  | -68.96%            | -43.65% |    -0.09 |       32 | 14.18%     | ok               |
|          45 | -24.62%  | -68.96%            | -40.57% |    -0.18 |       52 | 18.01%     | ok               |

## IEF Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -6.92%   | -0.99%             | -9.79%  |    -0.82 |       74 | 42.60%     | ok               |
|          15 | -7.47%   | -0.99%             | -10.52% |    -0.88 |       73 | 44.09%     | ok               |
|          40 | -8.39%   | -0.99%             | -9.67%  |    -1.3  |       64 | 25.12%     | ok               |
|          45 | -8.07%   | -0.99%             | -9.73%  |    -1.32 |       54 | 23.13%     | ok               |
|          25 | -10.50%  | -0.99%             | -11.19% |    -1.33 |       80 | 39.77%     | ok               |

## IEMG Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | -2.40%   | 57.06%             | -22.13% |    -0.02 |       63 | 40.93%     | ok               |
|          50 | -3.29%   | 57.06%             | -14.40% |    -0.07 |       56 | 32.45%     | ok               |
|          40 | -3.59%   | 57.06%             | -18.89% |    -0.07 |       62 | 38.27%     | ok               |
|          45 | -3.50%   | 57.06%             | -15.40% |    -0.08 |       52 | 35.11%     | ok               |
|          25 | -6.71%   | 57.06%             | -25.58% |    -0.16 |       59 | 43.76%     | ok               |

## INJ-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -11.46%  | -65.74%            | -52.34% |     0.04 |       44 | 23.37%     | ok               |
|          35 | -19.92%  | -65.74%            | -59.17% |    -0.01 |       62 | 33.33%     | ok               |
|          50 | -23.51%  | -65.74%            | -49.35% |    -0.16 |       48 | 20.11%     | ok               |
|          40 | -28.13%  | -65.74%            | -55.86% |    -0.16 |       52 | 29.50%     | ok               |
|          25 | -54.55%  | -65.74%            | -80.99% |    -0.47 |       79 | 43.87%     | ok               |

## INTC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | 89.46%   | 144.39%            | -56.41% |     0.78 |       75 | 51.41%     | ok               |
|          15 | 92.10%   | 144.39%            | -53.65% |     0.78 |       79 | 59.73%     | ok               |
|          45 | 80.47%   | 144.39%            | -49.32% |     0.77 |       58 | 34.11%     | ok               |
|          20 | 79.36%   | 144.39%            | -52.47% |     0.73 |       78 | 55.91%     | ok               |
|          40 | 74.55%   | 144.39%            | -55.86% |     0.72 |       66 | 38.44%     | ok               |

## INTU Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -0.28%   | -56.84%            | -40.73% |     0.11 |       69 | 27.95%     | ok               |
|          45 | -2.22%   | -56.84%            | -41.76% |     0.08 |       67 | 31.95%     | ok               |
|          40 | -8.64%   | -56.84%            | -45.15% |    -0.04 |       67 | 34.94%     | ok               |
|          35 | -15.62%  | -56.84%            | -46.75% |    -0.16 |       71 | 38.44%     | ok               |
|          25 | -18.48%  | -56.84%            | -39.87% |    -0.2  |       68 | 44.26%     | ok               |

## ITA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -1.40%   | 80.37%             | -25.76% |     0.05 |       87 | 59.90%     | ok               |
|          50 | -0.88%   | 80.37%             | -21.48% |     0.04 |       76 | 37.77%     | ok               |
|          30 | -4.32%   | 80.37%             | -23.75% |    -0.05 |       72 | 47.75%     | ok               |
|          35 | -6.36%   | 80.37%             | -23.16% |    -0.12 |       76 | 46.09%     | ok               |
|          40 | -7.43%   | 80.37%             | -20.58% |    -0.17 |       78 | 42.60%     | ok               |

## IWM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | 9.59%    | 45.21%             | -13.48% |     0.39 |       50 | 37.10%     | ok               |
|          40 | 8.60%    | 45.21%             | -14.08% |     0.39 |       42 | 31.28%     | ok               |
|          30 | 9.40%    | 45.21%             | -12.83% |     0.39 |       48 | 35.77%     | ok               |
|          35 | 8.35%    | 45.21%             | -14.11% |     0.36 |       48 | 33.61%     | ok               |
|          20 | 5.27%    | 45.21%             | -14.01% |     0.24 |       60 | 38.10%     | ok               |

## JNJ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 19.55%   | 58.24%             | -10.57% |     0.8  |       56 | 37.44%     | ok               |
|          15 | 13.68%   | 58.24%             | -18.02% |     0.48 |       62 | 57.90%     | ok               |
|          45 | 11.01%   | 58.24%             | -13.35% |     0.47 |       56 | 42.26%     | ok               |
|          20 | 8.43%    | 58.24%             | -17.61% |     0.33 |       68 | 54.41%     | ok               |
|          40 | 5.67%    | 58.24%             | -14.77% |     0.26 |       62 | 46.59%     | ok               |

## JPM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 13.35%   | 88.85%             | -15.90% |     0.47 |       54 | 40.10%     | ok               |
|          45 | 2.58%    | 88.85%             | -21.91% |     0.15 |       56 | 43.09%     | ok               |
|          20 | -14.36%  | 88.85%             | -33.59% |    -0.24 |       86 | 58.07%     | ok               |
|          40 | -11.50%  | 88.85%             | -28.47% |    -0.26 |       68 | 45.76%     | ok               |
|          35 | -16.72%  | 88.85%             | -27.43% |    -0.41 |       76 | 49.75%     | ok               |

## KO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 23.75%   | 36.09%             | -8.20%  |     0.85 |       51 | 37.94%     | ok               |
|          35 | 19.96%   | 36.09%             | -8.07%  |     0.75 |       54 | 36.61%     | ok               |
|          40 | 17.46%   | 36.09%             | -9.28%  |     0.71 |       56 | 33.44%     | ok               |
|          25 | 18.64%   | 36.09%             | -9.73%  |     0.69 |       57 | 40.60%     | ok               |
|          50 | 10.20%   | 36.09%             | -12.31% |     0.48 |       38 | 26.96%     | ok               |

## LDO-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 76.40%   | -78.58%            | -48.17% |     0.75 |       82 | 54.79%     | ok               |
|          20 | 48.87%   | -78.58%            | -48.55% |     0.62 |       86 | 50.00%     | ok               |
|          50 | 33.03%   | -78.58%            | -48.04% |     0.57 |       52 | 18.20%     | ok               |
|          35 | 37.35%   | -78.58%            | -64.26% |     0.55 |       78 | 34.29%     | ok               |
|          30 | 37.32%   | -78.58%            | -63.49% |     0.55 |       78 | 41.38%     | ok               |

## LIN Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -1.55%   | 12.74%             | -23.68% |     0.01 |       64 | 49.25%     | ok               |
|          25 | -1.82%   | 12.74%             | -22.01% |    -0    |       63 | 41.26%     | ok               |
|          20 | -3.92%   | 12.74%             | -23.00% |    -0.07 |       62 | 44.43%     | ok               |
|          35 | -5.36%   | 12.74%             | -21.18% |    -0.15 |       62 | 31.95%     | ok               |
|          30 | -5.96%   | 12.74%             | -21.53% |    -0.16 |       66 | 38.44%     | ok               |

## LINK-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -13.76%  | -54.99%            | -49.69% |     0.1  |       75 | 43.49%     | ok               |
|          45 | -10.56%  | -54.99%            | -38.11% |     0.08 |       52 | 27.97%     | ok               |
|          50 | -10.12%  | -54.99%            | -36.52% |     0.07 |       42 | 22.61%     | ok               |
|          35 | -21.81%  | -54.99%            | -49.52% |    -0.02 |       61 | 38.12%     | ok               |
|          40 | -26.10%  | -54.99%            | -50.88% |    -0.11 |       57 | 32.38%     | ok               |

## LLY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 6.70%    | 53.50%             | -38.23% |     0.24 |       46 | 36.11%     | ok               |
|          15 | -2.78%   | 53.50%             | -48.12% |     0.1  |       63 | 59.57%     | ok               |
|          45 | -5.30%   | 53.50%             | -42.66% |     0.01 |       54 | 39.60%     | ok               |
|          20 | -18.43%  | 53.50%             | -51.34% |    -0.18 |       72 | 54.58%     | ok               |
|          25 | -19.78%  | 53.50%             | -53.47% |    -0.22 |       68 | 51.91%     | ok               |

## LRCX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -8.98%   | 246.05%            | -60.45% |     0.1  |       83 | 53.58%     | ok               |
|          50 | -13.93%  | 246.05%            | -50.39% |    -0.02 |       80 | 35.27%     | ok               |
|          40 | -16.51%  | 246.05%            | -56.86% |    -0.03 |       72 | 41.10%     | ok               |
|          35 | -21.93%  | 246.05%            | -61.76% |    -0.1  |       80 | 43.09%     | ok               |
|          20 | -24.09%  | 246.05%            | -67.48% |    -0.12 |       89 | 49.08%     | ok               |

## LTC-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -7.37%   | -61.52%            | -43.31% |     0.07 |       56 | 32.38%     | ok               |
|          35 | -20.30%  | -61.52%            | -54.86% |    -0.09 |       68 | 43.68%     | ok               |
|          30 | -30.71%  | -61.52%            | -53.76% |    -0.23 |       72 | 50.19%     | ok               |
|          40 | -29.49%  | -61.52%            | -56.10% |    -0.26 |       60 | 38.89%     | ok               |
|          25 | -33.45%  | -61.52%            | -54.26% |    -0.27 |       76 | 52.68%     | ok               |

## MCD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 2.85%    | -10.71%            | -9.22%  |     0.19 |       42 | 20.63%     | ok               |
|          30 | -2.55%   | -10.71%            | -18.81% |    -0.05 |       75 | 38.10%     | ok               |
|          25 | -3.59%   | -10.71%            | -20.47% |    -0.09 |       75 | 40.77%     | ok               |
|          35 | -7.68%   | -10.71%            | -15.45% |    -0.29 |       67 | 34.44%     | ok               |
|          40 | -7.95%   | -10.71%            | -16.86% |    -0.33 |       71 | 28.79%     | ok               |

## META Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -15.83%  | 29.58%             | -33.43% |    -0.23 |       68 | 37.44%     | ok               |
|          40 | -25.08%  | 29.58%             | -37.88% |    -0.44 |       68 | 40.43%     | ok               |
|          25 | -32.47%  | 29.58%             | -42.94% |    -0.56 |       69 | 51.08%     | ok               |
|          50 | -28.68%  | 29.58%             | -36.05% |    -0.59 |       72 | 33.61%     | ok               |
|          30 | -34.28%  | 29.58%             | -42.10% |    -0.63 |       74 | 47.92%     | ok               |

## MPC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 28.54%   | 88.93%             | -23.96% |     0.6  |       50 | 37.60%     | ok               |
|          45 | 20.39%   | 88.93%             | -25.09% |     0.47 |       56 | 41.26%     | ok               |
|          40 | 18.56%   | 88.93%             | -25.70% |     0.43 |       58 | 43.59%     | ok               |
|          35 | 14.90%   | 88.93%             | -35.90% |     0.37 |       66 | 46.09%     | ok               |
|          30 | -3.17%   | 88.93%             | -44.76% |     0.07 |       69 | 48.92%     | ok               |

## MRK Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -20.62%  | -0.56%             | -30.12% |    -0.37 |       89 | 55.07%     | ok               |
|          25 | -20.24%  | -0.56%             | -31.07% |    -0.4  |       74 | 47.09%     | ok               |
|          20 | -24.15%  | -0.56%             | -29.59% |    -0.5  |       79 | 50.42%     | ok               |
|          50 | -24.10%  | -0.56%             | -27.68% |    -0.69 |       60 | 29.62%     | ok               |
|          45 | -25.99%  | -0.56%             | -27.72% |    -0.7  |       61 | 32.95%     | ok               |

## MS Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -3.32%   | 153.92%            | -19.99% |     0    |       72 | 41.43%     | ok               |
|          15 | -4.98%   | 153.92%            | -22.02% |    -0.01 |       73 | 58.24%     | ok               |
|          20 | -5.09%   | 153.92%            | -25.68% |    -0.02 |       77 | 54.41%     | ok               |
|          30 | -10.18%  | 153.92%            | -27.79% |    -0.16 |       77 | 49.58%     | ok               |
|          35 | -10.11%  | 153.92%            | -25.26% |    -0.17 |       78 | 46.09%     | ok               |

## MSFT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -21.30%  | -4.26%             | -25.26% |    -0.59 |       64 | 33.78%     | ok               |
|          50 | -23.26%  | -4.26%             | -26.14% |    -0.68 |       60 | 28.95%     | ok               |
|          35 | -33.78%  | -4.26%             | -35.38% |    -0.9  |       71 | 42.43%     | ok               |
|          40 | -33.15%  | -4.26%             | -34.77% |    -0.92 |       67 | 37.27%     | ok               |
|          30 | -37.64%  | -4.26%             | -39.15% |    -0.99 |       81 | 47.09%     | ok               |

## MU Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 357.23%  | 969.54%            | -61.96% |     1.44 |       47 | 66.72%     | ok               |
|          40 | 289.68%  | 969.54%            | -64.07% |     1.4  |       56 | 54.91%     | ok               |
|          25 | 284.21%  | 969.54%            | -67.90% |     1.36 |       49 | 61.06%     | ok               |
|          30 | 269.00%  | 969.54%            | -68.76% |     1.34 |       49 | 59.40%     | ok               |
|          35 | 235.47%  | 969.54%            | -69.15% |     1.26 |       63 | 57.40%     | ok               |

## NEAR-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 58.08%   | -42.67%            | -49.73% |     0.73 |       40 | 22.22%     | ok               |
|          50 | 38.01%   | -42.67%            | -52.97% |     0.58 |       34 | 17.82%     | ok               |
|          40 | 32.29%   | -42.67%            | -57.80% |     0.52 |       44 | 26.44%     | ok               |
|          35 | 4.82%    | -42.67%            | -61.61% |     0.28 |       68 | 31.80%     | ok               |
|          15 | -19.72%  | -42.67%            | -54.94% |     0.12 |       85 | 55.56%     | ok               |

## NEM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 3.24%    | 220.56%            | -29.41% |     0.21 |       62 | 61.40%     | ok               |
|          20 | -7.81%   | 220.56%            | -30.47% |     0.07 |       72 | 56.91%     | ok               |
|          25 | -21.27%  | 220.56%            | -37.89% |    -0.14 |       68 | 54.74%     | ok               |
|          50 | -23.65%  | 220.56%            | -32.97% |    -0.25 |       56 | 40.77%     | ok               |
|          30 | -31.13%  | 220.56%            | -38.49% |    -0.33 |       72 | 53.08%     | ok               |

## NFLX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 42.36%   | 14.89%             | -11.94% |     0.91 |       48 | 45.26%     | ok               |
|          50 | 38.57%   | 14.89%             | -16.28% |     0.91 |       46 | 37.60%     | ok               |
|          35 | 37.24%   | 14.89%             | -18.30% |     0.79 |       64 | 49.08%     | ok               |
|          15 | 37.09%   | 14.89%             | -26.59% |     0.7  |       67 | 64.89%     | ok               |
|          25 | 30.77%   | 14.89%             | -21.09% |     0.66 |       68 | 56.57%     | ok               |

## NKE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | -26.37%  | -59.55%            | -42.13% |    -0.36 |       73 | 37.27%     | ok               |
|          20 | -33.26%  | -59.55%            | -50.44% |    -0.41 |       91 | 52.41%     | ok               |
|          25 | -33.48%  | -59.55%            | -51.20% |    -0.42 |       87 | 48.59%     | ok               |
|          15 | -37.59%  | -59.55%            | -55.28% |    -0.5  |       91 | 56.91%     | ok               |
|          40 | -26.37%  | -59.55%            | -31.11% |    -0.5  |       63 | 29.45%     | ok               |

## NOW Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 12.06%   | -37.18%            | -26.36% |     0.31 |       75 | 51.58%     | ok               |
|          30 | 8.05%    | -37.18%            | -27.34% |     0.26 |       78 | 45.59%     | ok               |
|          15 | 3.14%    | -37.18%            | -26.77% |     0.21 |       86 | 54.58%     | ok               |
|          25 | 1.91%    | -37.18%            | -27.28% |     0.19 |       70 | 48.92%     | ok               |
|          40 | -0.36%   | -37.18%            | -30.87% |     0.13 |       68 | 34.78%     | ok               |

## NVDA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -9.60%   | 156.63%            | -35.26% |     0.01 |       76 | 48.48%     | ok               |
|          20 | -14.87%  | 156.63%            | -40.59% |    -0.03 |       72 | 56.51%     | ok               |
|          25 | -14.73%  | 156.63%            | -33.22% |    -0.04 |       73 | 51.52%     | ok               |
|          15 | -24.09%  | 156.63%            | -45.02% |    -0.15 |       73 | 59.71%     | ok               |
|          50 | -18.25%  | 156.63%            | -40.84% |    -0.18 |       58 | 32.44%     | ok               |

## OP-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 27.06%   | -92.02%            | -36.11% |     0.51 |       30 | 11.11%     | ok               |
|          45 | 26.15%   | -92.02%            | -45.76% |     0.48 |       32 | 15.71%     | ok               |
|          40 | 3.68%    | -92.02%            | -53.61% |     0.25 |       48 | 24.33%     | ok               |
|          35 | -16.57%  | -92.02%            | -59.71% |     0.01 |       54 | 27.20%     | ok               |
|          30 | -31.79%  | -92.02%            | -71.26% |    -0.14 |       70 | 33.72%     | ok               |

## ORCL Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 251.51%  | 12.68%             | -29.32% |     1.39 |       68 | 66.06%     | ok               |
|          25 | 162.55%  | 12.68%             | -27.76% |     1.14 |       71 | 58.74%     | ok               |
|          20 | 159.16%  | 12.68%             | -29.32% |     1.11 |       71 | 61.73%     | ok               |
|          35 | 123.33%  | 12.68%             | -31.95% |     1    |       64 | 50.75%     | ok               |
|          30 | 123.52%  | 12.68%             | -29.47% |     1    |       70 | 54.91%     | ok               |

## OXY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 7.80%    | -4.58%             | -30.14% |     0.25 |       70 | 41.26%     | ok               |
|          40 | 7.53%    | -4.58%             | -30.31% |     0.25 |       56 | 37.60%     | ok               |
|          50 | 7.24%    | -4.58%             | -32.02% |     0.25 |       46 | 30.45%     | ok               |
|          30 | 5.33%    | -4.58%             | -34.15% |     0.21 |       71 | 46.42%     | ok               |
|          45 | -2.29%   | -4.58%             | -35.02% |     0.06 |       48 | 32.78%     | ok               |

## PEP Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 13.40%   | -18.79%            | -11.62% |     0.6  |       42 | 27.45%     | ok               |
|          45 | 6.15%    | -18.79%            | -14.22% |     0.3  |       58 | 31.45%     | ok               |
|          35 | 6.41%    | -18.79%            | -21.42% |     0.27 |       79 | 42.26%     | ok               |
|          40 | 2.59%    | -18.79%            | -18.04% |     0.15 |       70 | 37.10%     | ok               |
|          30 | -0.84%   | -18.79%            | -21.35% |     0.04 |       78 | 48.09%     | ok               |

## PEPE-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 6.62%    | -71.85%            | -61.96% |     0.38 |       78 | 62.64%     | ok               |
|          30 | 3.39%    | -71.85%            | -57.66% |     0.31 |       81 | 45.79%     | ok               |
|          25 | -11.86%  | -71.85%            | -53.88% |     0.18 |       91 | 51.53%     | ok               |
|          35 | -7.92%   | -71.85%            | -51.35% |     0.17 |       66 | 40.04%     | ok               |
|          20 | -16.87%  | -71.85%            | -61.13% |     0.16 |       84 | 59.00%     | ok               |

## PFE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -21.69%  | -8.21%             | -22.94% |    -0.8  |       52 | 18.97%     | ok               |
|          50 | -23.07%  | -8.21%             | -24.78% |    -0.96 |       38 | 15.31%     | ok               |
|          40 | -28.95%  | -8.21%             | -30.10% |    -1.02 |       72 | 23.96%     | ok               |
|          35 | -34.18%  | -8.21%             | -35.70% |    -1.14 |       84 | 31.61%     | ok               |
|          30 | -41.51%  | -8.21%             | -42.34% |    -1.34 |       79 | 36.11%     | ok               |

## PG Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -8.24%   | -6.82%             | -20.08% |    -0.3  |       58 | 32.78%     | ok               |
|          35 | -11.37%  | -6.82%             | -18.99% |    -0.42 |       66 | 36.27%     | ok               |
|          30 | -19.42%  | -6.82%             | -24.55% |    -0.74 |       68 | 39.43%     | ok               |
|          45 | -17.21%  | -6.82%             | -22.43% |    -0.75 |       58 | 30.28%     | ok               |
|          25 | -21.26%  | -6.82%             | -26.24% |    -0.82 |       80 | 40.93%     | ok               |

## PM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | -0.28%   | 114.89%            | -32.20% |     0.09 |       86 | 52.08%     | ok               |
|          20 | -2.99%   | 114.89%            | -31.89% |     0.04 |       85 | 60.57%     | ok               |
|          30 | -3.41%   | 114.89%            | -33.68% |     0.02 |       81 | 55.57%     | ok               |
|          50 | -6.95%   | 114.89%            | -35.70% |    -0.09 |       74 | 42.10%     | ok               |
|          40 | -8.33%   | 114.89%            | -37.94% |    -0.12 |       80 | 48.25%     | ok               |

## POL-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 23.05%   | -75.38%            | -46.45% |     0.45 |       75 | 48.47%     | ok               |
|          25 | 13.10%   | -75.38%            | -46.72% |     0.36 |       64 | 55.94%     | ok               |
|          15 | 2.83%    | -75.38%            | -58.42% |     0.27 |       74 | 66.09%     | ok               |
|          20 | 3.64%    | -75.38%            | -52.88% |     0.27 |       74 | 60.73%     | ok               |
|          50 | 2.17%    | -75.38%            | -23.33% |     0.17 |       48 | 19.73%     | ok               |

## QCOM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -3.88%   | 12.69%             | -54.50% |     0.12 |       71 | 47.75%     | ok               |
|          35 | -4.42%   | 12.69%             | -50.58% |     0.11 |       77 | 43.59%     | ok               |
|          20 | -7.78%   | 12.69%             | -54.38% |     0.08 |       67 | 50.58%     | ok               |
|          30 | -15.25%  | 12.69%             | -56.59% |    -0.04 |       73 | 46.09%     | ok               |
|          15 | -23.11%  | 12.69%             | -57.94% |    -0.13 |       71 | 53.74%     | ok               |

## QQQ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 20.33%   | 62.05%             | -12.88% |     0.58 |       60 | 43.59%     | ok               |
|          25 | 20.78%   | 62.05%             | -12.88% |     0.58 |       57 | 46.26%     | ok               |
|          15 | 21.30%   | 62.05%             | -14.17% |     0.55 |       61 | 51.75%     | ok               |
|          20 | 17.86%   | 62.05%             | -12.98% |     0.5  |       65 | 48.92%     | ok               |
|          35 | 8.03%    | 62.05%             | -18.29% |     0.29 |       66 | 39.93%     | ok               |

## RENDER-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 45.25%   | -63.80%            | -43.43% |     0.6  |       88 | 53.09%     | ok               |
|          15 | 34.37%   | -63.80%            | -44.59% |     0.54 |       90 | 56.56%     | ok               |
|          25 | 15.90%   | -63.80%            | -40.60% |     0.42 |       90 | 48.84%     | ok               |
|          30 | -19.07%  | -63.80%            | -45.00% |     0.1  |       98 | 42.28%     | ok               |
|          35 | -31.74%  | -63.80%            | -41.33% |    -0.12 |       84 | 34.17%     | ok               |

## RTX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 33.34%   | 116.73%            | -18.66% |     0.77 |       74 | 56.41%     | ok               |
|          25 | 29.04%   | 116.73%            | -18.59% |     0.69 |       60 | 53.41%     | ok               |
|          35 | 24.32%   | 116.73%            | -18.00% |     0.67 |       50 | 50.25%     | ok               |
|          30 | 27.08%   | 116.73%            | -16.99% |     0.66 |       54 | 52.25%     | ok               |
|          50 | 21.90%   | 116.73%            | -18.42% |     0.66 |       56 | 42.43%     | ok               |

## SBUX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -11.16%  | 11.81%             | -23.55% |    -0.15 |       63 | 42.10%     | ok               |
|          40 | -14.96%  | 11.81%             | -25.43% |    -0.29 |       60 | 33.94%     | ok               |
|          45 | -14.49%  | 11.81%             | -27.26% |    -0.3  |       66 | 30.12%     | ok               |
|          30 | -18.75%  | 11.81%             | -29.22% |    -0.34 |       62 | 39.77%     | ok               |
|          35 | -20.34%  | 11.81%             | -27.06% |    -0.4  |       58 | 37.10%     | ok               |

## SCHW Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 8.90%    | 53.54%             | -16.53% |     0.32 |       56 | 35.77%     | ok               |
|          50 | 2.99%    | 53.54%             | -13.28% |     0.16 |       54 | 32.95%     | ok               |
|          25 | -2.00%   | 53.54%             | -28.76% |     0.05 |       63 | 50.58%     | ok               |
|          40 | -2.39%   | 53.54%             | -23.35% |     0.01 |       64 | 38.77%     | ok               |
|          20 | -5.52%   | 53.54%             | -29.24% |    -0.03 |       71 | 53.08%     | ok               |

## SHIB-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -9.27%   | -73.05%            | -43.85% |     0.12 |       71 | 59.20%     | ok               |
|          15 | -12.40%  | -73.05%            | -49.21% |     0.1  |       78 | 67.43%     | ok               |
|          20 | -15.84%  | -73.05%            | -46.38% |     0.05 |       75 | 63.22%     | ok               |
|          35 | -16.71%  | -73.05%            | -52.43% |    -0.01 |       64 | 45.98%     | ok               |
|          30 | -24.29%  | -73.05%            | -47.96% |    -0.1  |       74 | 52.11%     | ok               |

## SHY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd    |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:-------|---------:|---------:|:-----------|:-----------------|
|          30 | -2.24%   | 0.17%              | -2.85% |    -0.79 |       48 | 34.28%     | ok               |
|          35 | -2.36%   | 0.17%              | -3.27% |    -0.84 |       50 | 32.45%     | ok               |
|          40 | -2.47%   | 0.17%              | -3.33% |    -0.89 |       50 | 30.62%     | ok               |
|          45 | -2.45%   | 0.17%              | -3.23% |    -0.9  |       48 | 27.45%     | ok               |
|          50 | -2.62%   | 0.17%              | -3.40% |    -1.01 |       44 | 24.63%     | ok               |

## SKY-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -29.07%  | 9.06%              | -44.74% |    -0.34 |       74 | 41.00%     | ok               |
|          15 | -33.41%  | 9.06%              | -56.39% |    -0.35 |       64 | 50.76%     | ok               |
|          25 | -32.71%  | 9.06%              | -48.09% |    -0.4  |       69 | 44.47%     | ok               |
|          20 | -42.96%  | 9.06%              | -58.40% |    -0.58 |       66 | 47.94%     | ok               |
|          35 | -38.34%  | 9.06%              | -49.68% |    -0.64 |       68 | 33.62%     | ok               |

## SLB Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 22.60%   | -1.02%             | -20.36% |     0.54 |       52 | 33.61%     | ok               |
|          40 | 17.17%   | -1.02%             | -25.33% |     0.44 |       46 | 36.94%     | ok               |
|          50 | 0.70%    | -1.02%             | -28.65% |     0.1  |       50 | 29.12%     | ok               |
|          35 | -12.75%  | -1.02%             | -43.52% |    -0.16 |       74 | 44.43%     | ok               |
|          30 | -24.35%  | -1.02%             | -54.23% |    -0.4  |       73 | 50.92%     | ok               |

## SLV Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 67.45%   | 162.38%            | -34.10% |     0.86 |       52 | 34.78%     | ok               |
|          45 | 65.43%   | 162.38%            | -31.82% |     0.83 |       58 | 35.94%     | ok               |
|          40 | 63.45%   | 162.38%            | -31.93% |     0.82 |       64 | 38.10%     | ok               |
|          35 | 51.14%   | 162.38%            | -36.89% |     0.71 |       70 | 40.77%     | ok               |
|          20 | 45.53%   | 162.38%            | -42.66% |     0.64 |       66 | 47.75%     | ok               |

## SMH Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 103.94%  | 182.97%            | -30.17% |     1.25 |       47 | 49.92%     | ok               |
|          35 | 82.52%   | 182.97%            | -34.36% |     1.12 |       54 | 45.76%     | ok               |
|          25 | 82.39%   | 182.97%            | -32.94% |     1.1  |       46 | 48.75%     | ok               |
|          30 | 80.23%   | 182.97%            | -33.99% |     1.09 |       48 | 47.09%     | ok               |
|          45 | 67.12%   | 182.97%            | -32.75% |     1.04 |       52 | 39.93%     | ok               |

## SNX-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -0.66%   | -78.38%            | -43.20% |     0.27 |       71 | 48.66%     | ok               |
|          35 | -16.66%  | -78.38%            | -34.24% |     0.05 |       66 | 31.42%     | ok               |
|          30 | -21.31%  | -78.38%            | -35.44% |     0.01 |       60 | 38.70%     | ok               |
|          15 | -31.09%  | -78.38%            | -44.00% |    -0.04 |       81 | 52.87%     | ok               |
|          40 | -19.92%  | -78.38%            | -41.36% |    -0.07 |       54 | 25.10%     | ok               |

## SOL-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -11.67%  | -56.28%            | -58.31% |     0.11 |       60 | 37.74%     | ok               |
|          35 | -27.52%  | -56.28%            | -61.96% |    -0.06 |       72 | 45.21%     | ok               |
|          25 | -29.38%  | -56.28%            | -53.21% |    -0.06 |       74 | 57.28%     | ok               |
|          15 | -36.32%  | -56.28%            | -59.14% |    -0.13 |       78 | 63.41%     | ok               |
|          45 | -30.66%  | -56.28%            | -64.60% |    -0.17 |       64 | 32.57%     | ok               |

## SOXX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 83.54%   | 162.50%            | -40.27% |     1.05 |       57 | 48.59%     | ok               |
|          35 | 80.60%   | 162.50%            | -38.63% |     1.05 |       59 | 43.59%     | ok               |
|          25 | 80.95%   | 162.50%            | -41.42% |     1.03 |       53 | 48.09%     | ok               |
|          30 | 70.78%   | 162.50%            | -41.89% |     0.95 |       57 | 45.92%     | ok               |
|          40 | 62.25%   | 162.50%            | -40.71% |     0.9  |       60 | 41.10%     | ok               |

## SPY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 13.70%   | 47.63%             | -14.25% |     0.49 |       61 | 53.24%     | ok               |
|          15 | 12.15%   | 47.63%             | -16.80% |     0.44 |       70 | 56.41%     | ok               |
|          25 | 6.63%    | 47.63%             | -15.22% |     0.28 |       61 | 52.25%     | ok               |
|          30 | 2.12%    | 47.63%             | -16.47% |     0.13 |       64 | 49.42%     | ok               |
|          35 | 1.51%    | 47.63%             | -16.72% |     0.11 |       60 | 46.42%     | ok               |

## SUSHI-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -23.49%  | -81.27%            | -40.08% |    -0.19 |       52 | 14.75%     | ok               |
|          45 | -58.58%  | -81.27%            | -64.27% |    -0.77 |       56 | 18.20%     | ok               |
|          40 | -61.52%  | -81.27%            | -68.16% |    -0.77 |       63 | 24.71%     | ok               |
|          15 | -80.93%  | -81.27%            | -81.65% |    -1.06 |       93 | 48.66%     | ok               |
|          35 | -74.59%  | -81.27%            | -80.15% |    -1.06 |       82 | 30.65%     | ok               |

## T Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 59.37%   | 35.85%             | -18.13% |     1.14 |       58 | 57.40%     | ok               |
|          25 | 54.42%   | 35.85%             | -17.66% |     1.08 |       60 | 55.24%     | ok               |
|          15 | 49.61%   | 35.85%             | -15.08% |     0.98 |       69 | 61.40%     | ok               |
|          30 | 37.51%   | 35.85%             | -17.01% |     0.84 |       64 | 53.24%     | ok               |
|          35 | 23.37%   | 35.85%             | -14.49% |     0.6  |       66 | 49.75%     | ok               |

## TGT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -10.39%  | -8.93%             | -41.89% |    -0.09 |       83 | 45.92%     | ok               |
|          25 | -11.28%  | -8.93%             | -42.39% |    -0.14 |       65 | 40.93%     | ok               |
|          45 | -10.37%  | -8.93%             | -29.07% |    -0.17 |       54 | 28.29%     | ok               |
|          30 | -12.14%  | -8.93%             | -40.57% |    -0.17 |       60 | 38.27%     | ok               |
|          15 | -16.06%  | -8.93%             | -39.76% |    -0.2  |       73 | 50.58%     | ok               |

## TIA-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -4.20%   | -88.53%            | -45.16% |     0.17 |       66 | 25.86%     | ok               |
|          45 | -2.21%   | -88.53%            | -49.23% |     0.16 |       54 | 18.77%     | ok               |
|          35 | -6.12%   | -88.53%            | -53.37% |     0.16 |       68 | 31.03%     | ok               |
|          50 | -3.16%   | -88.53%            | -48.70% |     0.1  |       34 | 11.69%     | ok               |
|          30 | -43.09%  | -88.53%            | -68.36% |    -0.28 |       93 | 37.16%     | ok               |

## TLT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -20.70%  | -10.78%            | -21.87% |    -1.59 |       72 | 32.95%     | ok               |
|          50 | -13.99%  | -10.78%            | -15.73% |    -1.63 |       34 | 15.47%     | ok               |
|          40 | -19.06%  | -10.78%            | -20.09% |    -1.82 |       60 | 22.30%     | ok               |
|          15 | -26.51%  | -10.78%            | -27.76% |    -1.85 |       77 | 40.93%     | ok               |
|          35 | -21.47%  | -10.78%            | -22.47% |    -1.88 |       66 | 27.12%     | ok               |

## TMO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 45.60%   | -7.97%             | -8.17%  |     1.02 |       40 | 32.61%     | ok               |
|          45 | 41.37%   | -7.97%             | -10.13% |     0.9  |       46 | 37.44%     | ok               |
|          40 | 40.12%   | -7.97%             | -9.91%  |     0.86 |       49 | 42.10%     | ok               |
|          35 | 22.29%   | -7.97%             | -14.06% |     0.54 |       61 | 46.59%     | ok               |
|          30 | 16.80%   | -7.97%             | -18.85% |     0.43 |       61 | 51.75%     | ok               |

## TMUS Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 7.75%    | 16.57%             | -30.05% |     0.26 |       65 | 59.40%     | ok               |
|          30 | 6.55%    | 16.57%             | -25.71% |     0.23 |       70 | 47.42%     | ok               |
|          20 | 1.53%    | 16.57%             | -29.75% |     0.13 |       71 | 53.74%     | ok               |
|          25 | -1.87%   | 16.57%             | -31.45% |     0.06 |       75 | 49.92%     | ok               |
|          50 | -3.71%   | 16.57%             | -28.89% |    -0.02 |       60 | 35.44%     | ok               |

## TRX-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 12.36%   | 37.46%             | -19.12% |     0.43 |       50 | 36.97%     | ok               |
|          30 | 8.91%    | 37.46%             | -22.90% |     0.32 |       68 | 48.47%     | ok               |
|          35 | 8.01%    | 37.46%             | -21.77% |     0.3  |       64 | 45.21%     | ok               |
|          25 | 6.95%    | 37.46%             | -26.84% |     0.27 |       64 | 51.72%     | ok               |
|          20 | 6.65%    | 37.46%             | -25.45% |     0.26 |       61 | 55.17%     | ok               |

## TSLA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 56.12%   | 85.12%             | -32.60% |     0.73 |       64 | 29.78%     | ok               |
|          40 | 35.10%   | 85.12%             | -45.90% |     0.52 |       63 | 34.61%     | ok               |
|          45 | 14.45%   | 85.12%             | -46.86% |     0.34 |       67 | 31.95%     | ok               |
|          35 | 3.29%    | 85.12%             | -51.29% |     0.23 |       72 | 37.27%     | ok               |
|          30 | -14.59%  | 85.12%             | -54.91% |     0.05 |       70 | 41.26%     | ok               |

## TXN Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 19.23%   | 80.44%             | -45.45% |     0.42 |       64 | 34.44%     | ok               |
|          20 | 4.44%    | 80.44%             | -38.49% |     0.21 |       60 | 58.40%     | ok               |
|          35 | 1.57%    | 80.44%             | -43.28% |     0.16 |       74 | 48.92%     | ok               |
|          15 | -1.53%   | 80.44%             | -38.99% |     0.14 |       65 | 62.23%     | ok               |
|          40 | -0.53%   | 80.44%             | -45.67% |     0.13 |       68 | 46.42%     | ok               |

## UNH Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 37.54%   | -13.44%            | -26.96% |     0.6  |       72 | 52.58%     | ok               |
|          15 | 38.06%   | -13.44%            | -32.14% |     0.58 |       72 | 67.39%     | ok               |
|          35 | 33.79%   | -13.44%            | -28.32% |     0.56 |       64 | 47.42%     | ok               |
|          50 | 26.38%   | -13.44%            | -36.82% |     0.5  |       56 | 30.62%     | ok               |
|          20 | 24.46%   | -13.44%            | -33.26% |     0.45 |       73 | 62.23%     | ok               |

## UNI-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -20.17%  | -61.84%            | -63.75% |    -0    |       58 | 33.52%     | ok               |
|          45 | -22.12%  | -61.84%            | -58.49% |    -0.05 |       58 | 28.35%     | ok               |
|          35 | -32.43%  | -61.84%            | -68.71% |    -0.12 |       70 | 39.27%     | ok               |
|          50 | -30.41%  | -61.84%            | -57.60% |    -0.21 |       54 | 21.65%     | ok               |
|          30 | -70.15%  | -61.84%            | -80.61% |    -0.79 |       86 | 45.02%     | ok               |

## UPS Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -30.31%  | -21.61%            | -43.07% |    -0.53 |       82 | 48.09%     | ok               |
|          25 | -31.42%  | -21.61%            | -39.04% |    -0.57 |       78 | 44.59%     | ok               |
|          15 | -34.23%  | -21.61%            | -43.86% |    -0.61 |       88 | 52.25%     | ok               |
|          35 | -32.80%  | -21.61%            | -39.90% |    -0.65 |       67 | 33.78%     | ok               |
|          30 | -35.66%  | -21.61%            | -38.83% |    -0.7  |       72 | 39.60%     | ok               |

## USO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 26.75%   | 78.86%             | -33.25% |     0.53 |       50 | 27.12%     | ok               |
|          20 | 28.05%   | 78.86%             | -44.16% |     0.51 |       74 | 39.93%     | ok               |
|          15 | 22.00%   | 78.86%             | -44.33% |     0.44 |       73 | 43.09%     | ok               |
|          30 | 18.17%   | 78.86%             | -43.35% |     0.4  |       68 | 34.61%     | ok               |
|          25 | 17.99%   | 78.86%             | -43.43% |     0.39 |       68 | 37.44%     | ok               |

## VEA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 6.11%    | 45.13%             | -16.28% |     0.27 |       58 | 50.08%     | ok               |
|          20 | 1.83%    | 45.13%             | -17.70% |     0.13 |       59 | 47.42%     | ok               |
|          25 | -0.19%   | 45.13%             | -17.79% |     0.05 |       55 | 45.76%     | ok               |
|          30 | -0.35%   | 45.13%             | -17.93% |     0.04 |       56 | 43.59%     | ok               |
|          35 | -1.46%   | 45.13%             | -16.79% |    -0.01 |       54 | 42.60%     | ok               |

## VIXY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -48.04%  | -62.13%            | -69.78% |    -0.43 |       46 | 10.48%     | ok               |
|          45 | -59.37%  | -62.13%            | -75.03% |    -0.61 |       60 | 16.64%     | ok               |
|          40 | -67.12%  | -62.13%            | -80.72% |    -0.72 |       74 | 21.30%     | ok               |
|          35 | -70.16%  | -62.13%            | -84.37% |    -0.75 |       90 | 26.62%     | ok               |
|          15 | -76.97%  | -62.13%            | -89.47% |    -0.77 |      101 | 44.09%     | ok               |

## VNQ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -7.66%   | 16.73%             | -19.07% |    -0.32 |       56 | 28.12%     | ok               |
|          50 | -8.10%   | 16.73%             | -17.13% |    -0.36 |       52 | 25.62%     | ok               |
|          25 | -12.08%  | 16.73%             | -22.34% |    -0.46 |       65 | 40.10%     | ok               |
|          20 | -13.69%  | 16.73%             | -23.79% |    -0.52 |       68 | 42.76%     | ok               |
|          15 | -15.00%  | 16.73%             | -24.90% |    -0.57 |       65 | 43.93%     | ok               |

## VTI Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 16.64%   | 46.66%             | -13.96% |     0.58 |       64 | 53.74%     | ok               |
|          15 | 10.67%   | 46.66%             | -15.70% |     0.39 |       67 | 56.24%     | ok               |
|          25 | 3.16%    | 46.66%             | -16.10% |     0.17 |       60 | 51.75%     | ok               |
|          30 | -4.58%   | 46.66%             | -18.77% |    -0.11 |       70 | 49.75%     | ok               |
|          35 | -6.98%   | 46.66%             | -20.89% |    -0.21 |       64 | 46.59%     | ok               |

## VWO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -6.76%   | 43.68%             | -21.18% |    -0.23 |       60 | 31.61%     | ok               |
|          15 | -9.00%   | 43.68%             | -24.01% |    -0.26 |       71 | 48.59%     | ok               |
|          40 | -8.45%   | 43.68%             | -23.57% |    -0.29 |       70 | 36.94%     | ok               |
|          45 | -8.58%   | 43.68%             | -23.26% |    -0.3  |       62 | 34.11%     | ok               |
|          20 | -10.03%  | 43.68%             | -26.14% |    -0.31 |       69 | 46.42%     | ok               |

## VZ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -6.80%   | 10.45%             | -12.71% |    -0.19 |       50 | 24.29%     | ok               |
|          45 | -17.93%  | 10.45%             | -20.96% |    -0.59 |       64 | 27.95%     | ok               |
|          25 | -20.97%  | 10.45%             | -22.13% |    -0.6  |       79 | 41.93%     | ok               |
|          35 | -19.10%  | 10.45%             | -22.26% |    -0.61 |       59 | 33.78%     | ok               |
|          40 | -23.63%  | 10.45%             | -23.75% |    -0.81 |       64 | 31.11%     | ok               |

## WFC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -3.93%   | 57.93%             | -18.29% |    -0.06 |       62 | 35.27%     | ok               |
|          35 | -7.41%   | 57.93%             | -23.64% |    -0.08 |       81 | 47.25%     | ok               |
|          20 | -13.59%  | 57.93%             | -29.43% |    -0.16 |       79 | 56.74%     | ok               |
|          45 | -10.66%  | 57.93%             | -23.40% |    -0.24 |       68 | 39.93%     | ok               |
|          40 | -11.95%  | 57.93%             | -24.26% |    -0.27 |       76 | 43.43%     | ok               |

## WIF-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 61.92%   | -76.06%            | -46.21% |     0.67 |       73 | 42.91%     | ok               |
|          20 | 56.20%   | -76.06%            | -40.67% |     0.64 |       67 | 40.23%     | ok               |
|          25 | -11.57%  | -76.06%            | -52.41% |     0.19 |       69 | 37.55%     | ok               |
|          50 | -24.32%  | -76.06%            | -41.18% |    -0.22 |       42 | 12.26%     | ok               |
|          30 | -43.94%  | -76.06%            | -57.80% |    -0.24 |       70 | 33.52%     | ok               |

## WMT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 45.75%   | 83.38%             | -9.18%  |     1.27 |       38 | 41.26%     | ok               |
|          50 | 38.65%   | 83.38%             | -12.19% |     1.17 |       34 | 38.94%     | ok               |
|          40 | 33.62%   | 83.38%             | -12.49% |     0.97 |       44 | 42.60%     | ok               |
|          35 | 32.74%   | 83.38%             | -13.08% |     0.92 |       54 | 47.25%     | ok               |
|          15 | 17.89%   | 83.38%             | -25.74% |     0.47 |       72 | 61.23%     | ok               |

## XBI Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -1.63%   | 49.82%             | -16.08% |     0.04 |       60 | 35.44%     | ok               |
|          45 | -2.39%   | 49.82%             | -15.62% |     0.01 |       52 | 32.28%     | ok               |
|          35 | -9.01%   | 49.82%             | -17.75% |    -0.15 |       66 | 39.10%     | ok               |
|          30 | -10.02%  | 49.82%             | -18.72% |    -0.18 |       66 | 40.77%     | ok               |
|          25 | -12.21%  | 49.82%             | -23.66% |    -0.22 |       76 | 43.09%     | ok               |

## XLB Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -0.42%   | 16.96%             | -19.67% |     0.04 |       54 | 31.45%     | ok               |
|          50 | -1.74%   | 16.96%             | -17.59% |    -0.02 |       42 | 27.29%     | ok               |
|          35 | -3.70%   | 16.96%             | -22.65% |    -0.08 |       56 | 34.78%     | ok               |
|          45 | -3.43%   | 16.96%             | -19.78% |    -0.09 |       42 | 28.62%     | ok               |
|          25 | -6.87%   | 16.96%             | -22.63% |    -0.19 |       60 | 40.27%     | ok               |

## XLC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 11.81%   | 38.83%             | -12.33% |     0.44 |       69 | 53.58%     | ok               |
|          25 | 9.06%    | 38.83%             | -12.31% |     0.35 |       68 | 55.41%     | ok               |
|          40 | 7.98%    | 38.83%             | -13.38% |     0.34 |       70 | 46.09%     | ok               |
|          35 | 7.37%    | 38.83%             | -13.38% |     0.32 |       66 | 50.42%     | ok               |
|          45 | 2.08%    | 38.83%             | -13.21% |     0.13 |       68 | 43.09%     | ok               |

## XLE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 10.66%   | 38.12%             | -25.98% |     0.37 |       54 | 36.11%     | ok               |
|          45 | 6.12%    | 38.12%             | -29.68% |     0.24 |       60 | 38.10%     | ok               |
|          35 | 3.89%    | 38.12%             | -31.51% |     0.18 |       65 | 42.76%     | ok               |
|          25 | -2.99%   | 38.12%             | -36.05% |     0.01 |       83 | 48.25%     | ok               |
|          40 | -2.88%   | 38.12%             | -34.51% |    -0    |       64 | 40.60%     | ok               |

## XLF Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -5.54%   | 38.88%             | -18.01% |    -0.13 |       70 | 53.74%     | ok               |
|          15 | -9.45%   | 38.88%             | -19.58% |    -0.26 |       78 | 56.57%     | ok               |
|          25 | -11.88%  | 38.88%             | -23.22% |    -0.38 |       77 | 50.42%     | ok               |
|          30 | -12.51%  | 38.88%             | -23.61% |    -0.42 |       76 | 47.92%     | ok               |
|          35 | -19.53%  | 38.88%             | -27.41% |    -0.78 |       66 | 43.76%     | ok               |

## XLI Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 4.90%    | 48.26%             | -10.36% |     0.23 |       76 | 51.25%     | ok               |
|          20 | -0.64%   | 48.26%             | -12.74% |     0.03 |       67 | 46.26%     | ok               |
|          50 | -1.46%   | 48.26%             | -11.03% |    -0.02 |       60 | 32.45%     | ok               |
|          30 | -3.05%   | 48.26%             | -11.79% |    -0.07 |       66 | 43.59%     | ok               |
|          45 | -2.76%   | 48.26%             | -14.01% |    -0.08 |       64 | 34.94%     | ok               |

## XLK Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 87.25%   | 76.13%             | -14.75% |     1.38 |       39 | 50.92%     | ok               |
|          20 | 71.51%   | 76.13%             | -14.75% |     1.23 |       46 | 48.92%     | ok               |
|          25 | 68.02%   | 76.13%             | -14.75% |     1.23 |       40 | 46.76%     | ok               |
|          30 | 65.83%   | 76.13%             | -14.75% |     1.22 |       40 | 45.59%     | ok               |
|          35 | 47.33%   | 76.13%             | -13.61% |     0.99 |       52 | 42.93%     | ok               |

## XLM-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 26.14%   | -44.65%            | -38.97% |     0.48 |       44 | 27.39%     | ok               |
|          45 | 22.34%   | -44.65%            | -43.99% |     0.44 |       50 | 31.03%     | ok               |
|          30 | 0.26%    | -44.65%            | -50.36% |     0.22 |       69 | 45.59%     | ok               |
|          40 | -3.03%   | -44.65%            | -43.80% |     0.17 |       49 | 35.25%     | ok               |
|          35 | -8.51%   | -44.65%            | -50.42% |     0.12 |       69 | 41.57%     | ok               |

## XLP Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 8.18%    | 13.16%             | -6.85%  |     0.53 |       54 | 32.45%     | ok               |
|          40 | 7.50%    | 13.16%             | -7.77%  |     0.47 |       68 | 36.77%     | ok               |
|          50 | 6.85%    | 13.16%             | -7.01%  |     0.46 |       54 | 30.28%     | ok               |
|          35 | 6.56%    | 13.16%             | -9.73%  |     0.41 |       64 | 39.77%     | ok               |
|          30 | 4.67%    | 13.16%             | -11.16% |     0.3  |       66 | 41.26%     | ok               |

## XLU Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 5.85%    | 47.97%             | -12.97% |     0.32 |       52 | 31.28%     | ok               |
|          45 | 4.45%    | 47.97%             | -14.27% |     0.25 |       54 | 32.28%     | ok               |
|          40 | 1.57%    | 47.97%             | -15.59% |     0.12 |       58 | 33.78%     | ok               |
|          35 | -4.35%   | 47.97%             | -19.71% |    -0.16 |       62 | 35.94%     | ok               |
|          30 | -5.24%   | 47.97%             | -20.40% |    -0.19 |       67 | 39.10%     | ok               |

## XLV Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -15.90%  | 9.19%              | -19.97% |    -0.79 |       70 | 35.94%     | ok               |
|          25 | -16.57%  | 9.19%              | -21.14% |    -0.81 |       70 | 37.44%     | ok               |
|          15 | -20.36%  | 9.19%              | -24.43% |    -0.98 |       81 | 42.26%     | ok               |
|          20 | -20.29%  | 9.19%              | -24.51% |    -1.01 |       75 | 39.10%     | ok               |
|          35 | -20.30%  | 9.19%              | -23.94% |    -1.09 |       68 | 33.44%     | ok               |

## XLY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 5.14%    | 24.50%             | -12.94% |     0.23 |       70 | 41.43%     | ok               |
|          30 | 3.26%    | 24.50%             | -14.01% |     0.17 |       70 | 44.43%     | ok               |
|          50 | 1.64%    | 24.50%             | -11.49% |     0.12 |       50 | 29.45%     | ok               |
|          15 | 1.20%    | 24.50%             | -15.77% |     0.11 |       74 | 51.25%     | ok               |
|          45 | -1.43%   | 24.50%             | -13.48% |    -0    |       54 | 32.11%     | ok               |

## XOM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | 12.17%   | 48.05%             | -19.90% |     0.39 |       57 | 37.94%     | ok               |
|          30 | 11.06%   | 48.05%             | -20.29% |     0.37 |       57 | 37.27%     | ok               |
|          50 | 9.67%    | 48.05%             | -21.35% |     0.35 |       38 | 29.78%     | ok               |
|          20 | 4.25%    | 48.05%             | -25.56% |     0.19 |       66 | 40.10%     | ok               |
|          35 | 3.66%    | 48.05%             | -20.93% |     0.18 |       57 | 36.11%     | ok               |

## XRP-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | -22.20%  | -57.33%            | -42.68% |    -0.1  |       68 | 39.46%     | ok               |
|          30 | -34.79%  | -57.33%            | -51.12% |    -0.29 |       70 | 43.68%     | ok               |
|          40 | -31.84%  | -57.33%            | -42.76% |    -0.29 |       60 | 33.91%     | ok               |
|          45 | -39.45%  | -57.33%            | -44.78% |    -0.45 |       60 | 29.69%     | ok               |
|          50 | -36.16%  | -57.33%            | -39.26% |    -0.49 |       62 | 22.22%     | ok               |

## YFI-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -51.25%  | -65.18%            | -52.26% |    -0.86 |       62 | 27.39%     | ok               |
|          45 | -48.30%  | -65.18%            | -51.93% |    -0.99 |       70 | 21.65%     | ok               |
|          30 | -64.19%  | -65.18%            | -71.12% |    -1.03 |       81 | 40.61%     | ok               |
|          35 | -62.68%  | -65.18%            | -63.36% |    -1.06 |       69 | 34.87%     | ok               |
|          25 | -67.83%  | -65.18%            | -72.16% |    -1.12 |       75 | 45.59%     | ok               |

## ZEC-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 102.15%  | 1314.11%           | -24.66% |     0.82 |       46 | 24.71%     | ok               |
|          25 | 77.56%   | 1314.11%           | -48.59% |     0.7  |       56 | 39.66%     | ok               |
|          35 | 73.56%   | 1314.11%           | -44.34% |     0.69 |       54 | 31.23%     | ok               |
|          30 | 50.82%   | 1314.11%           | -47.68% |     0.59 |       62 | 36.78%     | ok               |
|          20 | 49.42%   | 1314.11%           | -54.26% |     0.59 |       67 | 41.95%     | ok               |
