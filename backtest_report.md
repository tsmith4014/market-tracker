# Market Tracker Backtest Report

_Generated: 2026-11-12T07:11:32+00:00_

## Data Sources

- Crypto: Kraken -> Coinbase -> CoinGecko OHLC -> CoinPaprika fallback chain.
- Stocks / ETFs / indices: Stooq -> Yahoo Finance fallback chain.
- Data rows are generated from real market APIs. Mock OHLCV rows are not generated.

## Data Freshness

- Rows: **92,788**
- Symbols: **161**
- Date range: **2024-06-21** to **2026-11-12**

## Latest Signals

| symbol     | date                |         close |   composite_score | signal   | data_source   |
|:-----------|:--------------------|--------------:|------------------:|:---------|:--------------|
| ABBV       | 2026-11-11 00:00:00 |   294.98      |          55.75    | LONG     | Yahoo Finance |
| AMD        | 2026-11-11 00:00:00 |   552.9       |          63.9167  | LONG     | Yahoo Finance |
| AMGN       | 2026-11-11 00:00:00 |   468.11      |          67.4167  | LONG     | Yahoo Finance |
| BLK        | 2026-11-11 00:00:00 |  1226.31      |          73.5833  | LONG     | Yahoo Finance |
| CL         | 2026-11-11 00:00:00 |    98         |          47.4167  | LONG     | Yahoo Finance |
| CMCSA      | 2026-11-11 00:00:00 |    25.02      |          36.4167  | LONG     | Yahoo Finance |
| COST       | 2026-11-11 00:00:00 |  1087.61      |          62.5833  | LONG     | Yahoo Finance |
| DE         | 2026-11-11 00:00:00 |   691.75      |          52.75    | LONG     | Yahoo Finance |
| DIA        | 2026-11-11 00:00:00 |   524.44      |          57.75    | LONG     | Yahoo Finance |
| DIS        | 2026-11-11 00:00:00 |   119.65      |          73.5833  | LONG     | Yahoo Finance |
| DXY-INDEX  | 2026-11-12 00:00:00 |   103.045     |          72.8495  | LONG     | Yahoo Finance |
| EOG        | 2026-11-11 00:00:00 |   153.77      |          38.0833  | LONG     | Yahoo Finance |
| HD         | 2026-11-11 00:00:00 |   351.31      |          58.4167  | LONG     | Yahoo Finance |
| IBM        | 2026-11-11 00:00:00 |   248.22      |          40.4167  | LONG     | Yahoo Finance |
| JNJ        | 2026-11-11 00:00:00 |   280.41      |          52.4167  | LONG     | Yahoo Finance |
| KO         | 2026-11-11 00:00:00 |    97.57      |          69.9167  | LONG     | Yahoo Finance |
| LIN        | 2026-11-11 00:00:00 |   526.55      |          51.9167  | LONG     | Yahoo Finance |
| LLY        | 2026-11-11 00:00:00 |  1437.29      |          73.5833  | LONG     | Yahoo Finance |
| MCD        | 2026-11-11 00:00:00 |   274.8       |          59.6667  | LONG     | Yahoo Finance |
| MRK        | 2026-11-11 00:00:00 |   147.18      |          60.4167  | LONG     | Yahoo Finance |
| NKE        | 2026-11-11 00:00:00 |    38.32      |          41.75    | LONG     | Yahoo Finance |
| PEP        | 2026-11-11 00:00:00 |   143.94      |          62.1667  | LONG     | Yahoo Finance |
| PG         | 2026-11-11 00:00:00 |   167.67      |          65.4167  | LONG     | Yahoo Finance |
| RTX        | 2026-11-11 00:00:00 |   201.29      |          54.8333  | LONG     | Yahoo Finance |
| SBUX       | 2026-11-11 00:00:00 |   109.89      |          58.4167  | LONG     | Yahoo Finance |
| UNH        | 2026-11-11 00:00:00 |   402.94      |          34.4167  | LONG     | Yahoo Finance |
| UPS        | 2026-11-11 00:00:00 |   112.45      |          58.9167  | LONG     | Yahoo Finance |
| VNQ        | 2026-11-11 00:00:00 |    97.02      |          65.4167  | LONG     | Yahoo Finance |
| WMT        | 2026-11-11 00:00:00 |   125.67      |          36.0833  | LONG     | Yahoo Finance |
| XLB        | 2026-11-11 00:00:00 |    53.02      |          58.6667  | LONG     | Yahoo Finance |
| XLF        | 2026-11-11 00:00:00 |    58.63      |          74.4167  | LONG     | Yahoo Finance |
| XLP        | 2026-11-11 00:00:00 |    91.45      |          51.4167  | LONG     | Yahoo Finance |
| XLU        | 2026-11-11 00:00:00 |    43.82      |          64.1667  | LONG     | Yahoo Finance |
| XLV        | 2026-11-11 00:00:00 |   188.95      |          73.9167  | LONG     | Yahoo Finance |
| XLY        | 2026-11-11 00:00:00 |   120.99      |          60.0833  | LONG     | Yahoo Finance |
| AAPL       | 2026-11-11 00:00:00 |   355.63      |          49.3333  | NEUTRAL  | Yahoo Finance |
| AAVE-USD   | 2026-11-12 00:00:00 |   116.61      |         -29.0833  | NEUTRAL  | Kraken API    |
| ADBE       | 2026-11-11 00:00:00 |   237.6       |         -53.0833  | NEUTRAL  | Yahoo Finance |
| AMAT       | 2026-11-11 00:00:00 |   395.08      |          -6.58333 | NEUTRAL  | Yahoo Finance |
| AMZN       | 2026-11-11 00:00:00 |   266.17      |          64.8333  | NEUTRAL  | Yahoo Finance |
| ARB-USD    | 2026-11-12 00:00:00 |     0.1491    |         -18.5     | NEUTRAL  | Kraken API    |
| AVAX-USD   | 2026-11-12 00:00:00 |     8.587     |           4.41667 | NEUTRAL  | Kraken API    |
| AVGO       | 2026-11-11 00:00:00 |   345.22      |          20.9167  | NEUTRAL  | Yahoo Finance |
| BAC        | 2026-11-11 00:00:00 |    50.67      |         -25.75    | NEUTRAL  | Yahoo Finance |
| BONK-USD   | 2026-11-12 00:00:00 |     2.657e-06 |         -54.75    | NEUTRAL  | Kraken API    |
| C          | 2026-11-11 00:00:00 |   124.21      |          -2.58333 | NEUTRAL  | Yahoo Finance |
| COMP-USD   | 2026-11-12 00:00:00 |    19.78      |         -22       | NEUTRAL  | Kraken API    |
| COP        | 2026-11-11 00:00:00 |   137.86      |           3.25    | NEUTRAL  | Yahoo Finance |
| CRM        | 2026-11-11 00:00:00 |   218.01      |         -14.3333  | NEUTRAL  | Yahoo Finance |
| DBC        | 2026-11-11 00:00:00 |    30.84      |         -16.5833  | NEUTRAL  | Yahoo Finance |
| DOT-USD    | 2026-11-12 00:00:00 |     0.8381    |         -45.5833  | NEUTRAL  | Kraken API    |
| EEM        | 2026-11-11 00:00:00 |    62.04      |         -16.8333  | NEUTRAL  | Yahoo Finance |
| EFA        | 2026-11-11 00:00:00 |   104.66      |          40.5     | NEUTRAL  | Yahoo Finance |
| EWJ        | 2026-11-11 00:00:00 |    92.12      |         -20.3333  | NEUTRAL  | Yahoo Finance |
| FET-USD    | 2026-11-12 00:00:00 |     0.148     |         -21       | NEUTRAL  | Kraken API    |
| FXI        | 2026-11-11 00:00:00 |    33.92      |          19.5833  | NEUTRAL  | Yahoo Finance |
| GDX        | 2026-11-11 00:00:00 |    85.21      |          -5.58333 | NEUTRAL  | Yahoo Finance |
| GDXJ       | 2026-11-11 00:00:00 |   104.51      |         -15.5833  | NEUTRAL  | Yahoo Finance |
| GE         | 2026-11-11 00:00:00 |   342.75      |          54.75    | NEUTRAL  | Yahoo Finance |
| GLD        | 2026-11-11 00:00:00 |   365.17      |         -43       | NEUTRAL  | Yahoo Finance |
| GS         | 2026-11-11 00:00:00 |   926.81      |          22.75    | NEUTRAL  | Yahoo Finance |
| HBAR-USD   | 2026-11-12 00:00:00 |     0.06543   |         -11.5     | NEUTRAL  | Kraken API    |
| HON        | 2026-11-11 00:00:00 |   227.64      |          53.9167  | NEUTRAL  | Yahoo Finance |
| HYG        | 2026-11-11 00:00:00 |    77.35      |          11.1667  | NEUTRAL  | Yahoo Finance |
| ICP-USD    | 2026-11-12 00:00:00 |     2.546     |          -1.33333 | NEUTRAL  | Kraken API    |
| IEF        | 2026-11-11 00:00:00 |    90.94      |         -20.25    | NEUTRAL  | Yahoo Finance |
| IEMG       | 2026-11-11 00:00:00 |    75.47      |         -16.8333  | NEUTRAL  | Yahoo Finance |
| INJ-USD    | 2026-11-12 00:00:00 |     7.457     |           4.25    | NEUTRAL  | Kraken API    |
| INTU       | 2026-11-11 00:00:00 |   342.64      |          24.1667  | NEUTRAL  | Yahoo Finance |
| ITA        | 2026-11-11 00:00:00 |    73.24      |          25.5833  | NEUTRAL  | Yahoo Finance |
| IWM        | 2026-11-11 00:00:00 |   283.09      |          48       | NEUTRAL  | Yahoo Finance |
| JPM        | 2026-11-11 00:00:00 |   343.39      |          57.8333  | NEUTRAL  | Yahoo Finance |
| LDO-USD    | 2026-11-12 00:00:00 |     0.31      |         -21       | NEUTRAL  | Kraken API    |
| LRCX       | 2026-11-11 00:00:00 |   235.88      |         -24.5833  | NEUTRAL  | Yahoo Finance |
| META       | 2026-11-11 00:00:00 |   628.77      |         -21       | NEUTRAL  | Yahoo Finance |
| MPC        | 2026-11-11 00:00:00 |   402.84      |         -17.0833  | NEUTRAL  | Yahoo Finance |
| MS         | 2026-11-11 00:00:00 |   190.61      |          -4.25    | NEUTRAL  | Yahoo Finance |
| MSFT       | 2026-11-11 00:00:00 |   521.13      |           4       | NEUTRAL  | Yahoo Finance |
| MU         | 2026-11-11 00:00:00 |   811.3       |          -8.33333 | NEUTRAL  | Yahoo Finance |
| NEAR-USD   | 2026-11-12 00:00:00 |     3.5034    |         -18.25    | NEUTRAL  | Kraken API    |
| NEM        | 2026-11-11 00:00:00 |   118.47      |          41.1667  | NEUTRAL  | Yahoo Finance |
| ORCL       | 2026-11-11 00:00:00 |   128.38      |          -5.33333 | NEUTRAL  | Yahoo Finance |
| PEPE-USD   | 2026-11-12 00:00:00 |     4.441e-06 |          -3.91667 | NEUTRAL  | Kraken API    |
| PFE        | 2026-11-11 00:00:00 |    29.45      |          18.4167  | NEUTRAL  | Yahoo Finance |
| PM         | 2026-11-11 00:00:00 |   196.35      |         -10.3333  | NEUTRAL  | Yahoo Finance |
| QCOM       | 2026-11-11 00:00:00 |   176.57      |          47.75    | NEUTRAL  | Yahoo Finance |
| QQQ        | 2026-11-11 00:00:00 |   690.38      |          -8.08333 | NEUTRAL  | Yahoo Finance |
| RENDER-USD | 2026-11-12 00:00:00 |     1.535     |         -12.3333  | NEUTRAL  | Kraken API    |
| SCHW       | 2026-11-11 00:00:00 |    92.78      |           2.41667 | NEUTRAL  | Yahoo Finance |
| SLB        | 2026-11-11 00:00:00 |    50.96      |         -28.5833  | NEUTRAL  | Yahoo Finance |
| SPY        | 2026-11-11 00:00:00 |   759.81      |          22.9167  | NEUTRAL  | Yahoo Finance |
| T          | 2026-11-11 00:00:00 |    22.26      |         -10.9167  | NEUTRAL  | Yahoo Finance |
| TGT        | 2026-11-11 00:00:00 |   162.7       |          61.1667  | NEUTRAL  | Yahoo Finance |
| TLT        | 2026-11-11 00:00:00 |    80.92      |         -22.5833  | NEUTRAL  | Yahoo Finance |
| TMO        | 2026-11-11 00:00:00 |   717.71      |          52.1667  | NEUTRAL  | Yahoo Finance |
| TMUS       | 2026-11-11 00:00:00 |   172.16      |          18.3333  | NEUTRAL  | Yahoo Finance |
| TSLA       | 2026-11-11 00:00:00 |   390.84      |          22.8333  | NEUTRAL  | Yahoo Finance |
| TXN        | 2026-11-11 00:00:00 |   309.81      |          39.3333  | NEUTRAL  | Yahoo Finance |
| UNI-USD    | 2026-11-12 00:00:00 |     6.1158    |         -16.25    | NEUTRAL  | Kraken API    |
| USO        | 2026-11-11 00:00:00 |   141.47      |         -15.25    | NEUTRAL  | Yahoo Finance |
| VEA        | 2026-11-11 00:00:00 |    69.92      |          23       | NEUTRAL  | Yahoo Finance |
| VIXY       | 2026-11-11 00:00:00 |    16.93      |         -27       | NEUTRAL  | Yahoo Finance |
| VTI        | 2026-11-11 00:00:00 |   374.25      |          15.4167  | NEUTRAL  | Yahoo Finance |
| VWO        | 2026-11-11 00:00:00 |    57.22      |           3.16667 | NEUTRAL  | Yahoo Finance |
| VZ         | 2026-11-11 00:00:00 |    46.6       |          46.9167  | NEUTRAL  | Yahoo Finance |
| WFC        | 2026-11-11 00:00:00 |    85.8       |          57.4167  | NEUTRAL  | Yahoo Finance |
| XBI        | 2026-11-11 00:00:00 |   156.31      |          61.1667  | NEUTRAL  | Yahoo Finance |
| XLC        | 2026-11-11 00:00:00 |   108.6       |          26.6667  | NEUTRAL  | Yahoo Finance |
| XLE        | 2026-11-11 00:00:00 |    63.37      |         -29       | NEUTRAL  | Yahoo Finance |
| XLI        | 2026-11-11 00:00:00 |   170.97      |          51.4167  | NEUTRAL  | Yahoo Finance |
| XLK        | 2026-11-11 00:00:00 |   174.36      |          -8.08333 | NEUTRAL  | Yahoo Finance |
| XOM        | 2026-11-11 00:00:00 |   166.71      |         -20       | NEUTRAL  | Yahoo Finance |
| YFI-USD    | 2026-11-12 00:00:00 |  1866.6       |         -19       | NEUTRAL  | Kraken API    |
| ZEC-USD    | 2026-11-12 00:00:00 |   980.06      |         -34.5     | NEUTRAL  | Kraken API    |
| ADA-USD    | 2026-11-12 00:00:00 |     0.17164   |         -34.3333  | SHORT    | Kraken API    |
| AGG        | 2026-11-11 00:00:00 |    95.84      |         -31       | SHORT    | Yahoo Finance |
| ALGO-USD   | 2026-11-12 00:00:00 |     0.08863   |         -32.3333  | SHORT    | Kraken API    |
| APT-USD    | 2026-11-12 00:00:00 |     0.5544    |         -34.3333  | SHORT    | Kraken API    |
| ARKK       | 2026-11-11 00:00:00 |    78.47      |         -31.8333  | SHORT    | Yahoo Finance |
| ATOM-USD   | 2026-11-12 00:00:00 |     1.3884    |         -30       | SHORT    | Kraken API    |
| BA         | 2026-11-11 00:00:00 |   174.54      |         -40.75    | SHORT    | Yahoo Finance |
| BCH-USD    | 2026-11-12 00:00:00 |   227.85      |         -53.3333  | SHORT    | Kraken API    |
| BITO       | 2026-11-11 00:00:00 |     9.92      |         -36.8333  | SHORT    | Yahoo Finance |
| BND        | 2026-11-11 00:00:00 |    71.1       |         -42.5833  | SHORT    | Yahoo Finance |
| BTC-USD    | 2026-11-12 00:00:00 | 73367.7       |         -37.25    | SHORT    | Kraken API    |
| CAT        | 2026-11-11 00:00:00 |   601.61      |         -52.5833  | SHORT    | Yahoo Finance |
| CRV-USD    | 2026-11-12 00:00:00 |     0.23735   |         -55.6667  | SHORT    | Kraken API    |
| CSCO       | 2026-11-11 00:00:00 |   100.76      |         -44.8333  | SHORT    | Yahoo Finance |
| CVX        | 2026-11-11 00:00:00 |   213.28      |         -33.25    | SHORT    | Yahoo Finance |
| DASH-USD   | 2026-11-12 00:00:00 |    41.366     |         -52.3333  | SHORT    | Kraken API    |
| DOGE-USD   | 2026-11-12 00:00:00 |     0.0667029 |         -47.6667  | SHORT    | Kraken API    |
| ETC-USD    | 2026-11-12 00:00:00 |     6.617     |         -39.3333  | SHORT    | Kraken API    |
| ETH-USD    | 2026-11-12 00:00:00 |  2039.37      |         -44.5     | SHORT    | Kraken API    |
| FCX        | 2026-11-11 00:00:00 |    62.12      |         -44.8333  | SHORT    | Yahoo Finance |
| FIL-USD    | 2026-11-12 00:00:00 |     0.742     |         -34.3333  | SHORT    | Kraken API    |
| GOOGL      | 2026-11-11 00:00:00 |   293.45      |         -50.5833  | SHORT    | Yahoo Finance |
| GRT-USD    | 2026-11-12 00:00:00 |     0.01718   |         -46.6667  | SHORT    | Kraken API    |
| IBIT       | 2026-11-11 00:00:00 |    42.24      |         -36.8333  | SHORT    | Yahoo Finance |
| INTC       | 2026-11-11 00:00:00 |    62.5       |         -56.5833  | SHORT    | Yahoo Finance |
| LINK-USD   | 2026-11-12 00:00:00 |    10.0301    |         -43       | SHORT    | Kraken API    |
| LTC-USD    | 2026-11-12 00:00:00 |    49.48      |         -43       | SHORT    | Kraken API    |
| NFLX       | 2026-11-11 00:00:00 |    64.54      |         -34.0833  | SHORT    | Yahoo Finance |
| NOW        | 2026-11-11 00:00:00 |   102.76      |         -49.0833  | SHORT    | Yahoo Finance |
| NVDA       | 2026-11-11 00:00:00 |   173.73      |         -63.1667  | SHORT    | Yahoo Finance |
| OP-USD     | 2026-11-12 00:00:00 |     0.0959    |         -38.3333  | SHORT    | Kraken API    |
| OXY        | 2026-11-11 00:00:00 |    57.24      |         -31.25    | SHORT    | Yahoo Finance |
| POL-USD    | 2026-11-12 00:00:00 |     0.08611   |         -34       | SHORT    | Kraken API    |
| SHIB-USD   | 2026-11-12 00:00:00 |     4.32e-06  |         -41       | SHORT    | Kraken API    |
| SHY        | 2026-11-11 00:00:00 |    81.31      |         -40.3333  | SHORT    | Yahoo Finance |
| SKY-USD    | 2026-11-12 00:00:00 |     0.0576    |         -46.3333  | SHORT    | Kraken API    |
| SLV        | 2026-11-11 00:00:00 |    46.65      |         -31.25    | SHORT    | Yahoo Finance |
| SMH        | 2026-11-11 00:00:00 |   506.96      |         -48.8333  | SHORT    | Yahoo Finance |
| SNX-USD    | 2026-11-12 00:00:00 |     0.1617    |         -32.3333  | SHORT    | Kraken API    |
| SOL-USD    | 2026-11-12 00:00:00 |    82.52      |         -51.6667  | SHORT    | Kraken API    |
| SOXX       | 2026-11-11 00:00:00 |   155.4       |         -48.8333  | SHORT    | Yahoo Finance |
| SUSHI-USD  | 2026-11-12 00:00:00 |     0.1708    |         -43.3333  | SHORT    | Kraken API    |
| TIA-USD    | 2026-11-12 00:00:00 |     0.4089    |         -50.6667  | SHORT    | Kraken API    |
| TRX-USD    | 2026-11-12 00:00:00 |     0.316414  |         -62.8333  | SHORT    | Kraken API    |
| WIF-USD    | 2026-11-12 00:00:00 |     0.1532    |         -32.3333  | SHORT    | Kraken API    |
| XLM-USD    | 2026-11-12 00:00:00 |     0.145738  |         -45       | SHORT    | Kraken API    |
| XRP-USD    | 2026-11-12 00:00:00 |     1.03865   |         -53.3333  | SHORT    | Kraken API    |

## Edge Summary

- Symbols with trades: **161** of 161
- Beat buy-and-hold: **35.40%** of traded symbols
- Positive return: **31.68%** of traded symbols
- Median strategy return: **-7.37%** (benchmark **18.30%**)
- Median excess vs benchmark: **-24.72%**
- Median Sharpe: **-0.06**
- Median exposure: **44.43%**

> Edge is real only if both _beat buy-and-hold_ and _median excess_ are convincingly positive across many symbols. Treat a single high-return symbol as noise.

## Portfolio Backtest

Actual capital-allocation books (not per-symbol averages). Benchmarks: `equal_weight_buyhold` (whole tracked universe), `spy_buyhold` (100% SPY), and `sixty_forty` (60% SPY / 40% AGG). `high_conf_voltarget` inverse-vol-weights the HIGH-confidence book; `conviction_long_short` is market-neutral. Judge on **Sharpe** and **max_drawdown** out-of-sample, not raw return: a fully-invested long book wins on return in a bull market but carries all the risk.

| strategy              | scope         | ann_return   | ann_vol   |   sharpe | max_drawdown   | total_return   |   avg_gross_exposure |
|:----------------------|:--------------|:-------------|:----------|---------:|:---------------|:---------------|---------------------:|
| equal_weight_buyhold  | full          | 4.72%        | 28.38%    |     0.17 | -39.53%        | 2.12%          |                 1    |
| equal_weight_buyhold  | out_of_sample | 16.47%       | 26.33%    |     0.63 | -18.44%        | 14.85%         |                 1    |
| all_signals_ew        | full          | -11.51%      | 24.18%    |    -0.48 | -52.21%        | -35.49%        |                 1    |
| all_signals_ew        | out_of_sample | -4.96%       | 21.42%    |    -0.23 | -23.76%        | -7.42%         |                 1    |
| high_conf_ew          | full          | -8.91%       | 30.00%    |    -0.3  | -45.26%        | -33.38%        |                 0.89 |
| high_conf_ew          | out_of_sample | -8.82%       | 27.61%    |    -0.32 | -26.30%        | -12.64%        |                 0.89 |
| high_conf_voltarget   | full          | -9.26%       | 26.70%    |    -0.35 | -39.85%        | -32.16%        |                 0.89 |
| high_conf_voltarget   | out_of_sample | -11.09%      | 23.34%    |    -0.48 | -20.91%        | -13.75%        |                 0.89 |
| conviction_long_short | full          | -14.14%      | 21.97%    |    -0.64 | -48.77%        | -39.53%        |                 0.96 |
| conviction_long_short | out_of_sample | -15.62%      | 17.28%    |    -0.9  | -27.58%        | -16.65%        |                 0.96 |
| spy_buyhold           | full          | 2.88%        | 14.00%    |     0.21 | -19.00%        | 5.96%          |                 0.79 |
| spy_buyhold           | out_of_sample | -2.10%       | 10.92%    |    -0.19 | -11.45%        | -2.82%         |                 0.79 |
| sixty_forty           | full          | 1.20%        | 8.79%     |     0.14 | -11.86%        | 2.51%          |                 0.79 |
| sixty_forty           | out_of_sample | -3.38%       | 7.21%     |    -0.47 | -8.19%         | -3.80%         |                 0.79 |

## Walk-Forward Robustness

Each book measured across contiguous time folds (each a different regime). A book has durable edge only if `mean_sharpe` is positive, `min_sharpe` isn't deeply negative, and `pct_positive_folds` is high — a single great fold doesn't count. `fold_sharpes` lists each fold oldest-to-newest.

| strategy              |   n_folds |   mean_sharpe |   median_sharpe |   min_sharpe | pct_positive_folds   | mean_return   | fold_sharpes                 |
|:----------------------|----------:|--------------:|----------------:|-------------:|:---------------------|:--------------|:-----------------------------|
| equal_weight_buyhold  |         5 |          0.37 |            0.51 |        -0.74 | 60.00%               | 1.23%         | 1.36;1.07;-0.33;-0.74;0.51   |
| all_signals_ew        |         5 |         -0.53 |           -0.34 |        -1.77 | 20.00%               | -7.21%        | -1.26;-0.33;-1.77;1.05;-0.34 |
| high_conf_ew          |         5 |         -0.17 |           -0.54 |        -1.66 | 40.00%               | -6.05%        | 0.83;-1.66;-0.54;1.41;-0.90  |
| high_conf_voltarget   |         5 |         -0.27 |           -0.32 |        -1.88 | 40.00%               | -6.50%        | 0.96;-1.88;-0.32;0.89;-1.01  |
| conviction_long_short |         5 |         -0.66 |           -0.54 |        -1.91 | 40.00%               | -9.15%        | -1.91;0.08;-0.96;0.02;-0.54  |
| spy_buyhold           |         5 |          0.17 |            0.07 |        -0.87 | 80.00%               | 1.31%         | 1.32;0.07;0.01;0.29;-0.87    |
| sixty_forty           |         5 |          0.08 |            0.07 |        -1.06 | 80.00%               | 0.56%         | 1.24;0.07;0.10;0.07;-1.06    |

## Strategy Comparison

Each decision rule backtested over the same data. `out_of_sample` is the most recent ~35% of each symbol's history (unseen tail). A rule has real edge only if `median_excess` and `beat_benchmark_pct` stay positive out-of-sample, not just full-sample.

| strategy        | scope         |   symbols | beat_benchmark_pct   | positive_pct   | median_return   | median_benchmark   | median_excess   |   median_sharpe |   total_trades |
|:----------------|:--------------|----------:|:---------------------|:---------------|:----------------|:-------------------|:----------------|----------------:|---------------:|
| trend           | full          |       161 | 35.40%               | 31.68%         | -7.37%          | 18.30%             | -24.72%         |           -0.06 |          11330 |
| trend           | out_of_sample |       161 | 41.61%               | 44.10%         | -1.21%          | 2.26%              | -4.92%          |            0.02 |           3878 |
| mean_reversion  | full          |       159 | 38.99%               | 47.17%         | -0.23%          | 18.30%             | -19.37%         |           -0.02 |           1292 |
| mean_reversion  | out_of_sample |       131 | 48.09%               | 58.02%         | 0.34%           | 0.32%              | -1.10%          |            0.5  |            446 |
| regime_adaptive | full          |       161 | 36.02%               | 31.68%         | -7.53%          | 18.30%             | -23.44%         |           -0.05 |          11595 |
| regime_adaptive | out_of_sample |       161 | 40.37%               | 44.72%         | -1.10%          | 2.26%              | -4.92%          |            0.02 |           3979 |

## Signal Calibration

Realized forward return in the signal's direction, grouped by confidence. HIGH should outrank LOW for the confidence score to be meaningful.

| confidence_level   |   horizon |     n | mean_return   | median_return   | win_rate   |
|:-------------------|----------:|------:|:--------------|:----------------|:-----------|
| HIGH               |         5 |  7805 | 0.20%         | 0.07%           | 51.24%     |
| MEDIUM             |         5 | 29261 | 0.09%         | 0.07%           | 50.78%     |
| LOW                |         5 |  3636 | -0.22%        | -0.25%          | 47.50%     |
| ALL                |         5 | 40702 | 0.09%         | 0.05%           | 50.57%     |
| HIGH               |        10 |  7686 | 0.45%         | 0.07%           | 50.87%     |
| MEDIUM             |        10 | 28939 | 0.19%         | 0.07%           | 50.55%     |
| LOW                |        10 |  3593 | -0.44%        | -0.21%          | 48.37%     |
| ALL                |        10 | 40218 | 0.18%         | 0.05%           | 50.42%     |
| HIGH               |        20 |  7577 | 0.86%         | 0.18%           | 51.33%     |
| MEDIUM             |        20 | 28399 | 0.70%         | 0.45%           | 52.49%     |
| LOW                |        20 |  3502 | -0.37%        | -0.48%          | 47.77%     |
| ALL                |        20 | 39478 | 0.64%         | 0.32%           | 51.85%     |

## Backtest Summary

### Data Quality / Signal Availability

- **ok**: 161 symbols

| symbol     |   trades | return   | benchmark_return   | mdd     |   sharpe | exposure   | skipped_reason   |
|:-----------|---------:|:---------|:-------------------|:--------|---------:|:-----------|:-----------------|
| AAPL       |       67 | -4.96%   | 71.40%             | -20.65% |     0    | 48.42%     | ok               |
| AAVE-USD   |       67 | -41.54%  | -58.92%            | -64.31% |    -0.31 | 38.89%     | ok               |
| ABBV       |       68 | -16.03%  | 73.12%             | -30.52% |    -0.29 | 50.42%     | ok               |
| ADA-USD    |       74 | -15.12%  | -75.65%            | -52.70% |     0.05 | 49.62%     | ok               |
| ADBE       |       74 | -0.03%   | -55.46%            | -31.20% |     0.14 | 53.58%     | ok               |
| AGG        |       61 | -6.69%   | -1.96%             | -10.37% |    -1.03 | 34.11%     | ok               |
| ALGO-USD   |       82 | -21.98%  | -55.58%            | -42.04% |    -0.06 | 41.95%     | ok               |
| AMAT       |       73 | -42.62%  | 67.83%             | -57.56% |    -0.39 | 51.75%     | ok               |
| AMD        |       54 | 22.07%   | 242.93%            | -38.64% |     0.41 | 36.11%     | ok               |
| AMGN       |       63 | -3.20%   | 51.90%             | -34.19% |     0.03 | 52.91%     | ok               |
| AMZN       |       84 | -59.52%  | 40.77%             | -59.95% |    -1.75 | 41.43%     | ok               |
| APT-USD    |       76 | -36.50%  | -88.81%            | -56.73% |    -0.2  | 39.66%     | ok               |
| ARB-USD    |       75 | 0.13%    | -59.66%            | -45.88% |     0.28 | 42.53%     | ok               |
| ARKK       |       85 | -30.23%  | 81.14%             | -35.78% |    -0.45 | 43.76%     | ok               |
| ATOM-USD   |       80 | -50.97%  | -68.74%            | -59.79% |    -0.68 | 47.13%     | ok               |
| AVAX-USD   |       66 | -31.54%  | -60.90%            | -46.76% |    -0.22 | 41.57%     | ok               |
| AVGO       |       66 | -5.87%   | 108.14%            | -42.02% |     0.1  | 40.27%     | ok               |
| BA         |       65 | 12.40%   | -1.14%             | -24.47% |     0.32 | 52.25%     | ok               |
| BAC        |       78 | -6.49%   | 28.31%             | -22.37% |    -0.1  | 48.92%     | ok               |
| BCH-USD    |       84 | -13.18%  | -46.47%            | -54.04% |     0.06 | 48.28%     | ok               |
| BITO       |       85 | -26.87%  | -59.01%            | -43.13% |    -0.21 | 41.43%     | ok               |
| BLK        |       79 | -5.04%   | 55.70%             | -26.90% |    -0.05 | 47.25%     | ok               |
| BND        |       66 | -7.23%   | -1.96%             | -10.80% |    -1.11 | 34.94%     | ok               |
| BONK-USD   |       74 | 46.11%   | -84.75%            | -53.34% |     0.6  | 45.02%     | ok               |
| BTC-USD    |       81 | -13.11%  | -33.47%            | -25.52% |    -0.11 | 51.92%     | ok               |
| C          |       81 | -35.20%  | 107.05%            | -39.84% |    -0.76 | 47.42%     | ok               |
| CAT        |       70 | 26.28%   | 83.51%             | -21.87% |     0.49 | 51.08%     | ok               |
| CL         |       60 | 5.24%    | 0.75%              | -14.32% |     0.22 | 40.10%     | ok               |
| CMCSA      |       82 | -34.71%  | -30.62%            | -45.88% |    -0.82 | 43.59%     | ok               |
| COMP-USD   |       97 | -50.38%  | -61.42%            | -59.19% |    -0.44 | 48.47%     | ok               |
| COP        |       64 | -14.28%  | 23.82%             | -38.80% |    -0.17 | 43.59%     | ok               |
| COST       |       60 | 3.49%    | 28.21%             | -31.32% |     0.17 | 40.93%     | ok               |
| CRM        |       67 | -29.10%  | -11.04%            | -39.41% |    -0.39 | 46.26%     | ok               |
| CRV-USD    |       62 | 47.17%   | -65.85%            | -39.89% |     0.62 | 36.97%     | ok               |
| CSCO       |       65 | 3.26%    | 113.07%            | -27.23% |     0.18 | 51.25%     | ok               |
| CVX        |       69 | -12.37%  | 37.35%             | -26.75% |    -0.24 | 43.43%     | ok               |
| DASH-USD   |       59 | -10.96%  | 85.61%             | -64.43% |     0.31 | 30.27%     | ok               |
| DBC        |       68 | -11.81%  | 32.93%             | -24.10% |    -0.34 | 36.11%     | ok               |
| DE         |       72 | -4.21%   | 84.45%             | -22.44% |     0.01 | 44.26%     | ok               |
| DIA        |       72 | -9.09%   | 34.01%             | -16.20% |    -0.46 | 44.43%     | ok               |
| DIS        |       62 | 4.16%    | 16.99%             | -27.81% |     0.19 | 46.59%     | ok               |
| DOGE-USD   |       68 | -8.36%   | -65.77%            | -61.52% |     0.12 | 47.32%     | ok               |
| DOT-USD    |       80 | -46.89%  | -79.83%            | -63.40% |    -0.36 | 44.83%     | ok               |
| DXY-INDEX  |       42 | -2.33%   | -5.70%             | -5.53%  |    -0.39 | 30.52%     | ok               |
| EEM        |       66 | -10.56%  | 45.39%             | -24.14% |    -0.26 | 41.60%     | ok               |
| EFA        |       64 | -11.02%  | 34.27%             | -13.32% |    -0.45 | 38.77%     | ok               |
| EOG        |       76 | -29.30%  | 25.99%             | -47.65% |    -0.62 | 43.93%     | ok               |
| ETC-USD    |       56 | -6.16%   | -62.99%            | -46.79% |     0.08 | 35.44%     | ok               |
| ETH-USD    |       61 | 117.66%  | -23.95%            | -30.11% |     1.16 | 47.13%     | ok               |
| EWJ        |       66 | -25.58%  | 39.55%             | -29.40% |    -0.88 | 37.94%     | ok               |
| FCX        |       69 | -28.73%  | 25.34%             | -46.84% |    -0.29 | 45.59%     | ok               |
| FET-USD    |       79 | -28.05%  | -81.37%            | -66.52% |    -0.02 | 44.83%     | ok               |
| FIL-USD    |       69 | -28.42%  | -71.48%            | -58.54% |    -0.14 | 38.70%     | ok               |
| FXI        |       46 | -4.22%   | 28.39%             | -23.91% |    -0.02 | 30.45%     | ok               |
| GDX        |       68 | -6.36%   | 150.69%            | -34.29% |     0.04 | 45.09%     | ok               |
| GDXJ       |       70 | -30.10%  | 146.37%            | -36.01% |    -0.32 | 44.43%     | ok               |
| GE         |       78 | -13.14%  | 108.69%            | -27.82% |    -0.14 | 48.42%     | ok               |
| GLD        |       52 | 11.67%   | 70.02%             | -14.15% |     0.35 | 46.09%     | ok               |
| GOOGL      |       57 | 69.61%   | 63.36%             | -17.43% |     1.09 | 48.59%     | ok               |
| GRT-USD    |       75 | 76.91%   | -82.36%            | -43.87% |     0.8  | 47.89%     | ok               |
| GS         |       68 | -2.77%   | 105.88%            | -21.94% |     0.04 | 47.42%     | ok               |
| HBAR-USD   |       40 | -29.16%  | -36.56%            | -56.47% |    -0.42 | 42.81%     | ok               |
| HD         |       71 | 5.52%    | -1.26%             | -17.15% |     0.22 | 44.76%     | ok               |
| HON        |       89 | -30.23%  | 7.07%              | -34.64% |    -0.79 | 53.91%     | ok               |
| HYG        |       89 | -7.38%   | -0.05%             | -10.59% |    -0.83 | 39.10%     | ok               |
| IBIT       |       46 | 30.75%   | 11.13%             | -18.95% |     0.59 | 35.48%     | ok               |
| IBM        |       69 | -19.93%  | 43.93%             | -48.94% |    -0.19 | 50.75%     | ok               |
| ICP-USD    |       72 | 5.46%    | -57.77%            | -40.56% |     0.31 | 40.04%     | ok               |
| IEF        |       76 | -9.67%   | -3.61%             | -12.21% |    -1.27 | 34.78%     | ok               |
| IEMG       |       62 | -7.37%   | 40.80%             | -24.73% |    -0.17 | 41.43%     | ok               |
| INJ-USD    |       55 | -14.83%  | -45.80%            | -62.42% |     0.11 | 38.89%     | ok               |
| INTC       |       72 | 47.11%   | 101.03%            | -60.60% |     0.57 | 49.42%     | ok               |
| INTU       |       71 | 2.61%    | -45.80%            | -36.67% |     0.18 | 48.09%     | ok               |
| ITA        |       72 | -1.32%   | 63.51%             | -23.75% |     0.04 | 47.42%     | ok               |
| IWM        |       58 | 10.62%   | 41.30%             | -8.62%  |     0.43 | 34.78%     | ok               |
| JNJ        |       60 | 13.24%   | 88.51%             | -17.51% |     0.5  | 46.92%     | ok               |
| JPM        |       75 | -25.99%  | 74.93%             | -32.74% |    -0.75 | 44.43%     | ok               |
| KO         |       52 | 30.66%   | 55.44%             | -8.64%  |     1    | 39.27%     | ok               |
| LDO-USD    |       66 | 56.70%   | -64.81%            | -52.34% |     0.66 | 48.28%     | ok               |
| LIN        |       72 | -3.64%   | 18.93%             | -20.61% |    -0.06 | 41.43%     | ok               |
| LINK-USD   |       70 | 36.86%   | -30.14%            | -35.01% |     0.56 | 43.30%     | ok               |
| LLY        |       80 | -28.74%  | 62.61%             | -52.47% |    -0.4  | 49.58%     | ok               |
| LRCX       |       82 | -24.09%  | 124.57%            | -58.92% |    -0.08 | 45.59%     | ok               |
| LTC-USD    |       69 | 17.24%   | -45.48%            | -30.78% |     0.39 | 50.77%     | ok               |
| MCD        |       75 | 8.48%    | 5.94%              | -22.20% |     0.34 | 40.60%     | ok               |
| META       |       72 | -31.00%  | 27.08%             | -44.90% |    -0.45 | 50.58%     | ok               |
| MPC        |       70 | 11.57%   | 133.30%            | -33.74% |     0.31 | 53.41%     | ok               |
| MRK        |       67 | -23.35%  | 12.59%             | -35.95% |    -0.45 | 43.09%     | ok               |
| MS         |       75 | -6.28%   | 98.22%             | -27.79% |    -0.06 | 47.92%     | ok               |
| MSFT       |       81 | -27.33%  | 15.86%             | -38.06% |    -0.6  | 50.92%     | ok               |
| MU         |       53 | 73.89%   | 481.41%            | -66.33% |     0.72 | 49.92%     | ok               |
| NEAR-USD   |       65 | 174.64%  | 37.77%             | -46.60% |     1.12 | 43.30%     | ok               |
| NEM        |       72 | -28.27%  | 180.34%            | -41.53% |    -0.29 | 49.58%     | ok               |
| NFLX       |       84 | -10.33%  | -5.93%             | -27.17% |    -0.12 | 50.92%     | ok               |
| NKE        |       87 | -34.56%  | -60.57%            | -55.35% |    -0.43 | 47.75%     | ok               |
| NOW        |       81 | -14.52%  | -31.43%            | -42.66% |     0.04 | 52.08%     | ok               |
| NVDA       |       82 | -42.87%  | 33.64%             | -51.27% |    -0.59 | 55.79%     | ok               |
| OP-USD     |       74 | -31.11%  | -85.40%            | -57.83% |    -0.15 | 35.25%     | ok               |
| ORCL       |       60 | 59.79%   | -9.27%             | -31.04% |     0.66 | 50.75%     | ok               |
| OXY        |       67 | 1.75%    | -6.04%             | -28.48% |     0.15 | 43.26%     | ok               |
| PEP        |       72 | 3.95%    | -13.95%            | -21.35% |     0.18 | 45.42%     | ok               |
| PEPE-USD   |       72 | -38.57%  | -64.90%            | -60.19% |    -0.14 | 46.55%     | ok               |
| PFE        |       77 | -32.42%  | 6.16%              | -41.77% |    -0.98 | 37.44%     | ok               |
| PG         |       60 | -18.06%  | -0.35%             | -24.25% |    -0.62 | 36.44%     | ok               |
| PM         |       79 | -7.00%   | 96.51%             | -38.30% |    -0.07 | 48.09%     | ok               |
| POL-USD    |       85 | 6.17%    | -60.68%            | -45.37% |     0.28 | 49.62%     | ok               |
| QCOM       |       79 | -39.35%  | -16.92%            | -50.91% |    -0.43 | 40.27%     | ok               |
| QQQ        |       70 | -6.49%   | 43.78%             | -15.82% |    -0.1  | 43.59%     | ok               |
| RENDER-USD |       92 | -39.92%  | -62.21%            | -54.46% |    -0.2  | 48.28%     | ok               |
| RTX        |       71 | 21.35%   | 90.60%             | -16.99% |     0.52 | 52.25%     | ok               |
| SBUX       |       66 | -6.30%   | 37.52%             | -29.22% |    -0.03 | 40.43%     | ok               |
| SCHW       |       84 | -16.47%  | 26.51%             | -31.92% |    -0.34 | 48.09%     | ok               |
| SHIB-USD   |       79 | -30.85%  | -67.05%            | -52.52% |    -0.27 | 52.30%     | ok               |
| SHY        |       54 | -2.40%   | -0.40%             | -3.30%  |    -0.78 | 38.60%     | ok               |
| SKY-USD    |       87 | -54.56%  | -31.58%            | -63.60% |    -0.79 | 45.02%     | ok               |
| SLB        |       75 | -43.45%  | 11.61%             | -55.41% |    -0.89 | 47.75%     | ok               |
| SLV        |       66 | 29.55%   | 72.91%             | -37.05% |     0.5  | 41.60%     | ok               |
| SMH        |       50 | 41.65%   | 91.39%             | -34.29% |     0.68 | 42.10%     | ok               |
| SNX-USD    |       62 | 10.55%   | -76.29%            | -50.74% |     0.33 | 36.97%     | ok               |
| SOL-USD    |       73 | 12.35%   | -48.82%            | -41.09% |     0.35 | 58.05%     | ok               |
| SOXX       |       56 | 46.56%   | 86.64%             | -39.81% |     0.7  | 40.93%     | ok               |
| SPY        |       63 | -5.24%   | 39.54%             | -15.53% |    -0.12 | 47.75%     | ok               |
| SUSHI-USD  |       91 | -59.09%  | -75.56%            | -76.86% |    -0.66 | 43.49%     | ok               |
| T          |       68 | 52.21%   | 20.98%             | -17.01% |     0.94 | 57.57%     | ok               |
| TGT        |       58 | -8.89%   | 11.34%             | -32.83% |    -0.11 | 37.27%     | ok               |
| TIA-USD    |       91 | -50.23%  | -80.78%            | -78.90% |    -0.27 | 43.87%     | ok               |
| TLT        |       66 | -20.96%  | -13.88%            | -22.01% |    -1.59 | 34.28%     | ok               |
| TMO        |       67 | 38.81%   | 27.12%             | -18.85% |     0.74 | 56.41%     | ok               |
| TMUS       |       74 | -6.80%   | -2.59%             | -33.05% |    -0.05 | 46.76%     | ok               |
| TRX-USD    |       62 | 2.88%    | 10.21%             | -22.90% |     0.17 | 48.28%     | ok               |
| TSLA       |       76 | -32.86%  | 113.56%            | -59.64% |    -0.19 | 42.43%     | ok               |
| TXN        |       83 | -30.18%  | 58.45%             | -46.56% |    -0.35 | 48.75%     | ok               |
| UNH        |       75 | 36.14%   | -16.50%            | -26.31% |     0.58 | 48.75%     | ok               |
| UNI-USD    |       82 | -24.50%  | -10.71%            | -59.93% |     0.04 | 49.23%     | ok               |
| UPS        |       71 | -32.91%  | -17.68%            | -40.15% |    -0.6  | 43.09%     | ok               |
| USO        |       67 | -10.66%  | 79.87%             | -41.99% |    -0.02 | 34.11%     | ok               |
| VEA        |       64 | -7.02%   | 42.43%             | -18.84% |    -0.25 | 41.26%     | ok               |
| VIXY       |       94 | -83.33%  | -62.18%            | -90.81% |    -1.12 | 31.45%     | ok               |
| VNQ        |       71 | -9.90%   | 15.54%             | -24.92% |    -0.36 | 40.43%     | ok               |
| VTI        |       67 | -11.90%  | 39.48%             | -17.64% |    -0.38 | 47.75%     | ok               |
| VWO        |       78 | -15.94%  | 30.19%             | -25.20% |    -0.55 | 41.60%     | ok               |
| VZ         |       86 | -27.73%  | 15.81%             | -31.67% |    -0.84 | 43.26%     | ok               |
| WFC        |       84 | -20.27%  | 47.68%             | -29.91% |    -0.36 | 46.26%     | ok               |
| WIF-USD    |       64 | -0.46%   | -85.04%            | -48.32% |     0.26 | 42.53%     | ok               |
| WMT        |       71 | 5.98%    | 85.05%             | -25.96% |     0.23 | 48.42%     | ok               |
| XBI        |       60 | -0.97%   | 69.20%             | -17.66% |     0.06 | 37.94%     | ok               |
| XLB        |       64 | -8.62%   | 18.30%             | -24.18% |    -0.26 | 34.28%     | ok               |
| XLC        |       61 | 4.97%    | 27.85%             | -12.33% |     0.23 | 49.42%     | ok               |
| XLE        |       68 | -7.50%   | 41.21%             | -34.77% |    -0.11 | 47.25%     | ok               |
| XLF        |       78 | -1.45%   | 41.86%             | -23.61% |     0.01 | 48.92%     | ok               |
| XLI        |       82 | -9.35%   | 39.03%             | -18.27% |    -0.32 | 42.76%     | ok               |
| XLK        |       42 | 29.62%   | 52.67%             | -19.07% |     0.67 | 44.26%     | ok               |
| XLM-USD    |       75 | 2.54%    | -47.01%            | -54.74% |     0.25 | 49.43%     | ok               |
| XLP        |       63 | 15.00%   | 17.74%             | -8.96%  |     0.73 | 40.43%     | ok               |
| XLU        |       69 | 0.04%    | 26.30%             | -20.40% |     0.05 | 40.43%     | ok               |
| XLV        |       72 | -16.07%  | 28.70%             | -21.39% |    -0.7  | 36.77%     | ok               |
| XLY        |       77 | -2.65%   | 32.51%             | -18.44% |    -0.01 | 47.75%     | ok               |
| XOM        |       57 | -0.86%   | 50.51%             | -20.29% |     0.06 | 36.44%     | ok               |
| XRP-USD    |       74 | 1.61%    | -55.24%            | -32.16% |     0.21 | 35.82%     | ok               |
| YFI-USD    |       72 | -50.61%  | -64.91%            | -58.28% |    -0.77 | 39.46%     | ok               |
| ZEC-USD    |       54 | 126.43%  | 1800.08%           | -56.50% |     0.87 | 36.97%     | ok               |

## AAPL Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 0.99%    | 71.40%             | -21.71% |     0.13 |       76 | 53.24%     | ok               |
|          15 | -3.48%   | 71.40%             | -23.86% |     0.05 |       85 | 60.73%     | ok               |
|          30 | -4.96%   | 71.40%             | -20.65% |     0    |       67 | 48.42%     | ok               |
|          35 | -6.32%   | 71.40%             | -22.04% |    -0.03 |       67 | 47.09%     | ok               |
|          25 | -8.80%   | 71.40%             | -22.37% |    -0.07 |       77 | 50.58%     | ok               |

## AAVE-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 4.68%    | -58.92%            | -43.61% |     0.27 |       43 | 33.52%     | ok               |
|          35 | -9.10%   | -58.92%            | -48.79% |     0.12 |       53 | 36.78%     | ok               |
|          45 | -10.37%  | -58.92%            | -49.19% |     0.07 |       48 | 28.54%     | ok               |
|          50 | -11.28%  | -58.92%            | -45.07% |     0.04 |       44 | 21.26%     | ok               |
|          15 | -44.27%  | -58.92%            | -61.33% |    -0.24 |       80 | 53.07%     | ok               |

## ABBV Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -7.94%   | 73.12%             | -28.42% |    -0.12 |       54 | 38.44%     | ok               |
|          20 | -12.73%  | 73.12%             | -28.73% |    -0.2  |       64 | 53.74%     | ok               |
|          25 | -12.83%  | 73.12%             | -30.04% |    -0.2  |       67 | 52.25%     | ok               |
|          30 | -16.03%  | 73.12%             | -30.52% |    -0.29 |       68 | 50.42%     | ok               |
|          40 | -16.08%  | 73.12%             | -27.36% |    -0.32 |       70 | 43.43%     | ok               |

## ADA-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 3.30%    | -75.65%            | -47.22% |     0.3  |       67 | 64.18%     | ok               |
|          40 | 3.76%    | -75.65%            | -41.68% |     0.25 |       56 | 39.27%     | ok               |
|          35 | 2.61%    | -75.65%            | -44.07% |     0.25 |       62 | 43.87%     | ok               |
|          50 | 4.66%    | -75.65%            | -32.89% |     0.24 |       48 | 25.10%     | ok               |
|          45 | -3.06%   | -75.65%            | -38.00% |     0.15 |       56 | 31.99%     | ok               |

## ADBE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | 11.94%   | -55.46%            | -29.07% |     0.31 |       61 | 57.90%     | ok               |
|          30 | -0.03%   | -55.46%            | -31.20% |     0.14 |       74 | 53.58%     | ok               |
|          20 | -1.01%   | -55.46%            | -31.52% |     0.13 |       69 | 61.56%     | ok               |
|          35 | -3.38%   | -55.46%            | -32.89% |     0.07 |       77 | 45.09%     | ok               |
|          15 | -7.74%   | -55.46%            | -34.98% |     0.04 |       69 | 64.23%     | ok               |

## AGG Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -5.61%   | -1.96%             | -9.07%  |    -1.02 |       58 | 23.96%     | ok               |
|          30 | -6.69%   | -1.96%             | -10.37% |    -1.03 |       61 | 34.11%     | ok               |
|          35 | -7.42%   | -1.96%             | -11.22% |    -1.18 |       64 | 30.95%     | ok               |
|          20 | -8.93%   | -1.96%             | -11.89% |    -1.27 |       68 | 39.60%     | ok               |
|          25 | -8.69%   | -1.96%             | -12.28% |    -1.29 |       69 | 37.44%     | ok               |

## ALGO-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -21.98%  | -55.58%            | -42.04% |    -0.06 |       82 | 41.95%     | ok               |
|          25 | -26.10%  | -55.58%            | -50.24% |    -0.09 |       84 | 46.36%     | ok               |
|          15 | -36.42%  | -55.58%            | -54.78% |    -0.21 |       81 | 52.49%     | ok               |
|          35 | -33.74%  | -55.58%            | -52.80% |    -0.3  |       70 | 36.97%     | ok               |
|          20 | -43.05%  | -55.58%            | -57.39% |    -0.35 |       85 | 49.23%     | ok               |

## AMAT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -25.28%  | 67.83%             | -40.12% |    -0.16 |       52 | 35.77%     | ok               |
|          15 | -36.82%  | 67.83%             | -53.90% |    -0.25 |       74 | 60.57%     | ok               |
|          35 | -38.36%  | 67.83%             | -52.00% |    -0.33 |       73 | 49.08%     | ok               |
|          30 | -42.62%  | 67.83%             | -57.56% |    -0.39 |       73 | 51.75%     | ok               |
|          40 | -44.23%  | 67.83%             | -55.32% |    -0.45 |       73 | 44.09%     | ok               |

## AMD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 38.38%   | 242.93%            | -37.12% |     0.55 |       52 | 31.28%     | ok               |
|          40 | 22.07%   | 242.93%            | -38.64% |     0.41 |       54 | 36.11%     | ok               |
|          35 | 16.82%   | 242.93%            | -40.46% |     0.37 |       62 | 37.77%     | ok               |
|          45 | 10.46%   | 242.93%            | -45.45% |     0.31 |       58 | 34.11%     | ok               |
|          30 | -0.75%   | 242.93%            | -47.41% |     0.21 |       65 | 40.43%     | ok               |

## AMGN Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 1.91%    | 51.90%             | -26.65% |     0.14 |       62 | 58.24%     | ok               |
|          35 | -0.76%   | 51.90%             | -31.29% |     0.08 |       65 | 49.58%     | ok               |
|          30 | -3.20%   | 51.90%             | -34.19% |     0.03 |       63 | 52.91%     | ok               |
|          15 | -5.64%   | 51.90%             | -27.98% |    -0.01 |       61 | 62.23%     | ok               |
|          25 | -5.19%   | 51.90%             | -33.47% |    -0.01 |       59 | 55.07%     | ok               |

## AMZN Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -32.85%  | 40.77%             | -33.72% |    -1.02 |       60 | 30.28%     | ok               |
|          50 | -34.90%  | 40.77%             | -35.58% |    -1.27 |       52 | 22.96%     | ok               |
|          45 | -40.35%  | 40.77%             | -40.97% |    -1.45 |       60 | 26.62%     | ok               |
|          35 | -54.77%  | 40.77%             | -55.24% |    -1.63 |       79 | 35.44%     | ok               |
|          30 | -59.52%  | 40.77%             | -59.95% |    -1.75 |       84 | 41.43%     | ok               |

## APT-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 49.37%   | -88.81%            | -25.96% |     0.83 |       42 | 15.90%     | ok               |
|          45 | 11.65%   | -88.81%            | -52.49% |     0.33 |       62 | 23.37%     | ok               |
|          20 | -7.01%   | -88.81%            | -56.22% |     0.22 |       84 | 50.38%     | ok               |
|          15 | -26.10%  | -88.81%            | -58.22% |     0.04 |       79 | 56.70%     | ok               |
|          35 | -23.39%  | -88.81%            | -49.10% |    -0.06 |       72 | 35.25%     | ok               |

## ARB-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 88.94%   | -59.66%            | -33.86% |     0.84 |       58 | 26.25%     | ok               |
|          40 | 53.55%   | -59.66%            | -38.69% |     0.64 |       55 | 33.72%     | ok               |
|          35 | 43.55%   | -59.66%            | -41.25% |     0.58 |       69 | 37.55%     | ok               |
|          50 | 38.21%   | -59.66%            | -33.86% |     0.55 |       46 | 18.39%     | ok               |
|          15 | 31.73%   | -59.66%            | -55.99% |     0.52 |       94 | 58.81%     | ok               |

## ARKK Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -15.23%  | 81.14%             | -37.76% |    -0.08 |       87 | 54.74%     | ok               |
|          20 | -23.71%  | 81.14%             | -35.06% |    -0.25 |       87 | 50.08%     | ok               |
|          30 | -30.23%  | 81.14%             | -35.78% |    -0.45 |       85 | 43.76%     | ok               |
|          35 | -34.95%  | 81.14%             | -40.34% |    -0.6  |       88 | 40.93%     | ok               |
|          40 | -36.25%  | 81.14%             | -42.32% |    -0.66 |       80 | 36.77%     | ok               |

## ATOM-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -37.66%  | -68.74%            | -52.01% |    -0.35 |       82 | 53.07%     | ok               |
|          15 | -45.44%  | -68.74%            | -57.59% |    -0.43 |       84 | 65.52%     | ok               |
|          20 | -48.41%  | -68.74%            | -60.00% |    -0.53 |       88 | 57.66%     | ok               |
|          45 | -46.05%  | -68.74%            | -53.91% |    -0.66 |       72 | 32.38%     | ok               |
|          30 | -50.97%  | -68.74%            | -59.79% |    -0.68 |       80 | 47.13%     | ok               |

## AVAX-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 61.66%   | -60.90%            | -22.06% |     0.91 |       36 | 19.54%     | ok               |
|          40 | 41.79%   | -60.90%            | -26.27% |     0.66 |       40 | 30.08%     | ok               |
|          45 | 31.19%   | -60.90%            | -24.48% |     0.57 |       36 | 25.67%     | ok               |
|          35 | 11.79%   | -60.90%            | -33.05% |     0.33 |       52 | 36.21%     | ok               |
|          15 | -4.83%   | -60.90%            | -43.71% |     0.18 |       71 | 53.07%     | ok               |

## AVGO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -3.16%   | 108.14%            | -40.32% |     0.14 |       70 | 42.93%     | ok               |
|          30 | -5.87%   | 108.14%            | -42.02% |     0.1  |       66 | 40.27%     | ok               |
|          20 | -13.14%  | 108.14%            | -42.52% |     0.02 |       79 | 46.42%     | ok               |
|          50 | -12.99%  | 108.14%            | -41.40% |    -0.02 |       60 | 28.12%     | ok               |
|          35 | -14.98%  | 108.14%            | -45.96% |    -0.03 |       76 | 37.44%     | ok               |

## BA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 29.55%   | -1.14%             | -13.34% |     0.7  |       46 | 35.77%     | ok               |
|          35 | 26.16%   | -1.14%             | -18.09% |     0.53 |       68 | 48.92%     | ok               |
|          40 | 21.55%   | -1.14%             | -23.87% |     0.48 |       48 | 43.59%     | ok               |
|          25 | 21.82%   | -1.14%             | -26.02% |     0.45 |       66 | 55.57%     | ok               |
|          30 | 12.40%   | -1.14%             | -24.47% |     0.32 |       65 | 52.25%     | ok               |

## BAC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 1.17%    | 28.31%             | -13.90% |     0.1  |       54 | 34.11%     | ok               |
|          35 | 0.65%    | 28.31%             | -22.58% |     0.09 |       70 | 44.09%     | ok               |
|          20 | -1.51%   | 28.31%             | -17.80% |     0.05 |       82 | 54.24%     | ok               |
|          50 | -2.10%   | 28.31%             | -12.71% |    -0.01 |       52 | 31.11%     | ok               |
|          40 | -3.01%   | 28.31%             | -17.78% |    -0.03 |       64 | 37.60%     | ok               |

## BCH-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 6.68%    | -46.47%            | -45.64% |     0.3  |       81 | 57.09%     | ok               |
|          20 | 3.91%    | -46.47%            | -45.52% |     0.27 |       76 | 53.83%     | ok               |
|          35 | -7.97%   | -46.47%            | -57.75% |     0.12 |       74 | 44.44%     | ok               |
|          25 | -10.79%  | -46.47%            | -48.42% |     0.1  |       80 | 50.19%     | ok               |
|          30 | -13.18%  | -46.47%            | -54.04% |     0.06 |       84 | 48.28%     | ok               |

## BITO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -11.29%  | -59.01%            | -31.98% |    -0.04 |       54 | 24.29%     | ok               |
|          45 | -15.11%  | -59.01%            | -32.05% |    -0.09 |       58 | 27.62%     | ok               |
|          15 | -28.82%  | -59.01%            | -53.24% |    -0.18 |       83 | 49.92%     | ok               |
|          30 | -26.87%  | -59.01%            | -43.13% |    -0.21 |       85 | 41.43%     | ok               |
|          40 | -24.79%  | -59.01%            | -40.13% |    -0.23 |       68 | 32.61%     | ok               |

## BLK Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 4.69%    | 55.70%             | -20.79% |     0.2  |       86 | 43.76%     | ok               |
|          20 | 1.03%    | 55.70%             | -21.48% |     0.11 |       82 | 51.91%     | ok               |
|          40 | 0.14%    | 55.70%             | -22.83% |     0.08 |       78 | 39.27%     | ok               |
|          25 | -0.42%   | 55.70%             | -24.62% |     0.07 |       75 | 49.75%     | ok               |
|          30 | -5.04%   | 55.70%             | -26.90% |    -0.05 |       79 | 47.25%     | ok               |

## BND Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -7.65%   | -1.96%             | -10.72% |    -1.09 |       63 | 40.77%     | ok               |
|          25 | -7.45%   | -1.96%             | -11.16% |    -1.09 |       68 | 38.60%     | ok               |
|          30 | -7.23%   | -1.96%             | -10.80% |    -1.11 |       66 | 34.94%     | ok               |
|          40 | -7.39%   | -1.96%             | -11.34% |    -1.26 |       58 | 28.79%     | ok               |
|          15 | -9.01%   | -1.96%             | -12.04% |    -1.28 |       75 | 43.09%     | ok               |

## BONK-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 120.39%  | -84.75%            | -23.92% |     1.14 |       38 | 17.05%     | ok               |
|          40 | 151.44%  | -84.75%            | -41.42% |     1.13 |       64 | 34.67%     | ok               |
|          45 | 123.03%  | -84.75%            | -30.84% |     1.07 |       62 | 23.75%     | ok               |
|          35 | 89.62%   | -84.75%            | -47.15% |     0.84 |       62 | 40.42%     | ok               |
|          15 | 82.26%   | -84.75%            | -55.03% |     0.76 |       65 | 61.30%     | ok               |

## BTC-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 34.06%   | -33.47%            | -12.58% |     0.76 |       38 | 29.69%     | ok               |
|          35 | 32.51%   | -33.47%            | -22.51% |     0.68 |       62 | 41.19%     | ok               |
|          40 | 30.10%   | -33.47%            | -19.29% |     0.67 |       48 | 34.67%     | ok               |
|          50 | 17.82%   | -33.47%            | -20.16% |     0.49 |       34 | 25.10%     | ok               |
|          30 | 2.72%    | -33.47%            | -23.71% |     0.18 |       74 | 46.93%     | ok               |

## C Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -12.24%  | 107.05%            | -22.72% |    -0.29 |       68 | 30.95%     | ok               |
|          45 | -22.47%  | 107.05%            | -30.69% |    -0.57 |       78 | 36.27%     | ok               |
|          40 | -27.35%  | 107.05%            | -35.05% |    -0.67 |       74 | 38.77%     | ok               |
|          25 | -34.24%  | 107.05%            | -37.53% |    -0.72 |       71 | 50.08%     | ok               |
|          20 | -36.29%  | 107.05%            | -39.30% |    -0.76 |       77 | 52.75%     | ok               |

## CAT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 41.20%   | 83.51%             | -21.80% |     0.64 |       71 | 61.73%     | ok               |
|          25 | 35.26%   | 83.51%             | -21.79% |     0.6  |       66 | 53.41%     | ok               |
|          45 | 27.05%   | 83.51%             | -23.56% |     0.52 |       54 | 39.60%     | ok               |
|          30 | 26.28%   | 83.51%             | -21.87% |     0.49 |       70 | 51.08%     | ok               |
|          20 | 23.27%   | 83.51%             | -24.56% |     0.45 |       70 | 55.74%     | ok               |

## CL Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 12.23%   | 0.75%              | -10.72% |     0.47 |       42 | 25.12%     | ok               |
|          45 | 8.04%    | 0.75%              | -10.96% |     0.33 |       46 | 28.12%     | ok               |
|          30 | 5.24%    | 0.75%              | -14.32% |     0.22 |       60 | 40.10%     | ok               |
|          40 | 2.87%    | 0.75%              | -15.09% |     0.16 |       52 | 31.45%     | ok               |
|          35 | 1.05%    | 0.75%              | -15.39% |     0.1  |       60 | 36.27%     | ok               |

## CMCSA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -17.90%  | -30.62%            | -28.74% |    -0.59 |       48 | 16.47%     | ok               |
|          15 | -35.26%  | -30.62%            | -43.53% |    -0.72 |       90 | 58.24%     | ok               |
|          45 | -23.19%  | -30.62%            | -35.43% |    -0.73 |       62 | 21.13%     | ok               |
|          30 | -34.71%  | -30.62%            | -45.88% |    -0.82 |       82 | 43.59%     | ok               |
|          35 | -32.97%  | -30.62%            | -46.34% |    -0.82 |       91 | 38.77%     | ok               |

## COMP-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -50.38%  | -61.42%            | -59.19% |    -0.44 |       97 | 48.47%     | ok               |
|          50 | -40.66%  | -61.42%            | -43.38% |    -0.49 |       48 | 22.99%     | ok               |
|          15 | -63.15%  | -61.42%            | -70.92% |    -0.61 |      104 | 67.82%     | ok               |
|          20 | -61.72%  | -61.42%            | -68.52% |    -0.64 |      108 | 62.84%     | ok               |
|          25 | -61.13%  | -61.42%            | -68.03% |    -0.65 |      104 | 56.51%     | ok               |

## COP Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -14.28%  | 23.82%             | -38.80% |    -0.17 |       64 | 43.59%     | ok               |
|          50 | -12.17%  | 23.82%             | -35.99% |    -0.17 |       50 | 31.28%     | ok               |
|          35 | -14.14%  | 23.82%             | -41.20% |    -0.17 |       65 | 40.77%     | ok               |
|          45 | -17.00%  | 23.82%             | -41.02% |    -0.27 |       60 | 34.78%     | ok               |
|          25 | -25.22%  | 23.82%             | -44.40% |    -0.39 |       75 | 46.76%     | ok               |

## COST Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 19.77%   | 28.21%             | -24.32% |     0.6  |       62 | 47.25%     | ok               |
|          25 | 15.84%   | 28.21%             | -24.93% |     0.51 |       59 | 44.26%     | ok               |
|          35 | 8.06%    | 28.21%             | -30.16% |     0.32 |       58 | 38.44%     | ok               |
|          30 | 3.49%    | 28.21%             | -31.32% |     0.17 |       60 | 40.93%     | ok               |
|          15 | 3.54%    | 28.21%             | -27.30% |     0.17 |       67 | 50.92%     | ok               |

## CRM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | -17.82%  | -11.04%            | -26.69% |    -0.19 |       64 | 41.43%     | ok               |
|          40 | -20.90%  | -11.04%            | -32.67% |    -0.27 |       70 | 37.27%     | ok               |
|          15 | -27.51%  | -11.04%            | -47.54% |    -0.29 |       92 | 58.40%     | ok               |
|          30 | -29.10%  | -11.04%            | -39.41% |    -0.39 |       67 | 46.26%     | ok               |
|          20 | -32.67%  | -11.04%            | -45.74% |    -0.41 |       74 | 51.91%     | ok               |

## CRV-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 95.55%   | -65.85%            | -37.78% |     0.92 |       60 | 32.76%     | ok               |
|          40 | 75.32%   | -65.85%            | -38.86% |     0.81 |       52 | 28.93%     | ok               |
|          45 | 49.10%   | -65.85%            | -42.29% |     0.66 |       56 | 22.61%     | ok               |
|          30 | 47.17%   | -65.85%            | -39.89% |     0.62 |       62 | 36.97%     | ok               |
|          50 | 36.37%   | -65.85%            | -30.73% |     0.56 |       50 | 18.39%     | ok               |

## CSCO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 27.76%   | 113.07%            | -21.28% |     0.59 |       54 | 41.76%     | ok               |
|          50 | 26.97%   | 113.07%            | -19.34% |     0.59 |       54 | 39.93%     | ok               |
|          40 | 13.59%   | 113.07%            | -26.55% |     0.35 |       56 | 44.43%     | ok               |
|          35 | 9.95%    | 113.07%            | -26.02% |     0.29 |       60 | 47.92%     | ok               |
|          25 | 3.55%    | 113.07%            | -27.84% |     0.18 |       65 | 52.25%     | ok               |

## CVX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -9.75%   | 37.35%             | -23.25% |    -0.16 |       73 | 46.26%     | ok               |
|          45 | -8.74%   | 37.35%             | -27.82% |    -0.17 |       63 | 35.94%     | ok               |
|          40 | -9.92%   | 37.35%             | -25.79% |    -0.19 |       73 | 39.60%     | ok               |
|          50 | -8.62%   | 37.35%             | -29.71% |    -0.2  |       56 | 31.45%     | ok               |
|          30 | -12.37%  | 37.35%             | -26.75% |    -0.24 |       69 | 43.43%     | ok               |

## DASH-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 88.14%   | 85.61%             | -43.46% |     0.77 |       44 | 17.24%     | ok               |
|          40 | 81.35%   | 85.61%             | -42.64% |     0.73 |       50 | 23.75%     | ok               |
|          45 | 42.35%   | 85.61%             | -46.93% |     0.55 |       48 | 19.73%     | ok               |
|          30 | -10.96%  | 85.61%             | -64.43% |     0.31 |       59 | 30.27%     | ok               |
|          25 | -11.80%  | 85.61%             | -64.14% |     0.31 |       69 | 32.57%     | ok               |

## DBC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -2.68%   | 32.93%             | -26.01% |    -0.01 |       81 | 43.09%     | ok               |
|          20 | -8.86%   | 32.93%             | -25.69% |    -0.22 |       73 | 40.60%     | ok               |
|          25 | -9.03%   | 32.93%             | -24.84% |    -0.23 |       68 | 38.44%     | ok               |
|          50 | -8.86%   | 32.93%             | -18.84% |    -0.28 |       48 | 25.29%     | ok               |
|          45 | -10.62%  | 32.93%             | -20.02% |    -0.32 |       60 | 28.62%     | ok               |

## DE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 4.40%    | 84.45%             | -17.97% |     0.19 |       58 | 30.45%     | ok               |
|          45 | 1.93%    | 84.45%             | -18.05% |     0.13 |       58 | 34.44%     | ok               |
|          20 | -1.56%   | 84.45%             | -20.58% |     0.07 |       64 | 48.42%     | ok               |
|          25 | -2.99%   | 84.45%             | -20.76% |     0.04 |       71 | 46.42%     | ok               |
|          30 | -4.21%   | 84.45%             | -22.44% |     0.01 |       72 | 44.26%     | ok               |

## DIA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -6.99%   | 34.01%             | -13.58% |    -0.33 |       66 | 45.59%     | ok               |
|          20 | -9.11%   | 34.01%             | -15.48% |    -0.43 |       68 | 47.92%     | ok               |
|          35 | -8.69%   | 34.01%             | -16.94% |    -0.45 |       74 | 41.26%     | ok               |
|          30 | -9.09%   | 34.01%             | -16.20% |    -0.46 |       72 | 44.43%     | ok               |
|          40 | -11.29%  | 34.01%             | -18.41% |    -0.63 |       76 | 37.77%     | ok               |

## DIS Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 49.64%   | 16.99%             | -10.17% |     1.35 |       50 | 28.95%     | ok               |
|          40 | 18.61%   | 16.99%             | -18.75% |     0.49 |       65 | 37.10%     | ok               |
|          45 | 15.86%   | 16.99%             | -16.54% |     0.46 |       51 | 32.61%     | ok               |
|          35 | 10.19%   | 16.99%             | -25.30% |     0.31 |       73 | 43.43%     | ok               |
|          15 | 6.12%    | 16.99%             | -32.73% |     0.22 |       79 | 55.91%     | ok               |

## DOGE-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 2.85%    | -65.77%            | -50.23% |     0.22 |       58 | 21.46%     | ok               |
|          15 | -6.82%   | -65.77%            | -60.29% |     0.18 |       81 | 62.45%     | ok               |
|          20 | -9.21%   | -65.77%            | -60.01% |     0.14 |       79 | 56.51%     | ok               |
|          30 | -8.36%   | -65.77%            | -61.52% |     0.12 |       68 | 47.32%     | ok               |
|          25 | -11.59%  | -65.77%            | -60.53% |     0.1  |       72 | 52.11%     | ok               |

## DOT-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -46.03%  | -79.83%            | -65.96% |    -0.29 |       83 | 55.36%     | ok               |
|          15 | -52.48%  | -79.83%            | -73.05% |    -0.33 |       72 | 59.00%     | ok               |
|          30 | -46.89%  | -79.83%            | -63.40% |    -0.36 |       80 | 44.83%     | ok               |
|          25 | -54.42%  | -79.83%            | -71.03% |    -0.46 |       74 | 50.38%     | ok               |
|          35 | -54.45%  | -79.83%            | -65.50% |    -0.54 |       78 | 39.85%     | ok               |

## DXY-INDEX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -2.33%   | -5.70%             | -5.53%  |    -0.39 |       42 | 30.52%     | ok               |
|          40 | -4.24%   | -5.70%             | -6.38%  |    -0.58 |       68 | 46.10%     | ok               |
|          45 | -4.63%   | -5.70%             | -7.61%  |    -0.69 |       64 | 37.23%     | ok               |
|          15 | -8.03%   | -5.70%             | -11.87% |    -0.79 |       99 | 72.51%     | ok               |
|          30 | -6.52%   | -5.70%             | -9.65%  |    -0.79 |       80 | 56.49%     | ok               |

## EEM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -6.35%   | 45.39%             | -25.18% |    -0.12 |       65 | 45.09%     | ok               |
|          25 | -7.37%   | 45.39%             | -23.69% |    -0.15 |       65 | 43.43%     | ok               |
|          35 | -9.11%   | 45.39%             | -23.88% |    -0.22 |       70 | 39.77%     | ok               |
|          15 | -10.40%  | 45.39%             | -26.83% |    -0.23 |       73 | 48.75%     | ok               |
|          40 | -9.56%   | 45.39%             | -19.52% |    -0.25 |       70 | 37.94%     | ok               |

## EFA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -3.08%   | 34.27%             | -10.10% |    -0.06 |       62 | 48.92%     | ok               |
|          20 | -10.05%  | 34.27%             | -13.60% |    -0.37 |       67 | 46.09%     | ok               |
|          30 | -11.02%  | 34.27%             | -13.32% |    -0.45 |       64 | 38.77%     | ok               |
|          25 | -11.46%  | 34.27%             | -15.57% |    -0.45 |       68 | 42.43%     | ok               |
|          40 | -10.91%  | 34.27%             | -15.01% |    -0.49 |       60 | 34.28%     | ok               |

## EOG Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -13.51%  | 25.99%             | -34.41% |    -0.24 |       48 | 32.45%     | ok               |
|          40 | -17.44%  | 25.99%             | -36.18% |    -0.34 |       60 | 35.44%     | ok               |
|          35 | -21.27%  | 25.99%             | -38.93% |    -0.43 |       73 | 39.43%     | ok               |
|          50 | -21.07%  | 25.99%             | -35.63% |    -0.47 |       52 | 29.95%     | ok               |
|          30 | -29.30%  | 25.99%             | -47.65% |    -0.62 |       76 | 43.93%     | ok               |

## ETC-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | -3.06%   | -62.99%            | -43.95% |     0.12 |       48 | 32.18%     | ok               |
|          50 | -2.30%   | -62.99%            | -28.33% |     0.1  |       28 | 18.20%     | ok               |
|          30 | -6.16%   | -62.99%            | -46.79% |     0.08 |       56 | 35.44%     | ok               |
|          45 | -7.15%   | -62.99%            | -35.44% |     0.02 |       34 | 21.46%     | ok               |
|          40 | -8.56%   | -62.99%            | -41.85% |     0.01 |       50 | 26.44%     | ok               |

## ETH-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 117.66%  | -23.95%            | -30.11% |     1.16 |       61 | 47.13%     | ok               |
|          30 | 80.08%   | -23.95%            | -32.89% |     0.89 |       65 | 54.98%     | ok               |
|          40 | 62.74%   | -23.95%            | -33.11% |     0.84 |       62 | 39.27%     | ok               |
|          25 | 58.51%   | -23.95%            | -40.90% |     0.74 |       63 | 58.81%     | ok               |
|          45 | 47.39%   | -23.95%            | -34.50% |     0.71 |       64 | 36.02%     | ok               |

## EWJ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -22.08%  | 39.55%             | -30.00% |    -0.68 |       58 | 40.10%     | ok               |
|          25 | -23.99%  | 39.55%             | -29.85% |    -0.76 |       58 | 39.27%     | ok               |
|          15 | -25.82%  | 39.55%             | -31.15% |    -0.77 |       69 | 43.43%     | ok               |
|          30 | -25.58%  | 39.55%             | -29.40% |    -0.88 |       66 | 37.94%     | ok               |
|          45 | -26.30%  | 39.55%             | -28.62% |    -1.06 |       62 | 29.28%     | ok               |

## FCX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -0.23%   | 25.34%             | -29.52% |     0.14 |       54 | 33.11%     | ok               |
|          50 | -5.88%   | 25.34%             | -26.57% |     0.04 |       58 | 29.28%     | ok               |
|          40 | -13.96%  | 25.34%             | -42.89% |    -0.07 |       66 | 38.10%     | ok               |
|          30 | -28.73%  | 25.34%             | -46.84% |    -0.29 |       69 | 45.59%     | ok               |
|          35 | -32.32%  | 25.34%             | -50.12% |    -0.39 |       71 | 43.26%     | ok               |

## FET-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 16.13%   | -81.37%            | -59.58% |     0.42 |       71 | 57.66%     | ok               |
|          25 | -12.28%  | -81.37%            | -65.31% |     0.18 |       79 | 49.04%     | ok               |
|          20 | -14.15%  | -81.37%            | -66.17% |     0.17 |       82 | 54.21%     | ok               |
|          30 | -28.05%  | -81.37%            | -66.52% |    -0.02 |       79 | 44.83%     | ok               |
|          45 | -32.05%  | -81.37%            | -51.19% |    -0.29 |       52 | 22.41%     | ok               |

## FIL-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -28.42%  | -71.48%            | -58.54% |    -0.14 |       69 | 38.70%     | ok               |
|          15 | -47.93%  | -71.48%            | -71.48% |    -0.34 |       93 | 52.30%     | ok               |
|          40 | -42.11%  | -71.48%            | -59.57% |    -0.44 |       50 | 28.93%     | ok               |
|          35 | -44.74%  | -71.48%            | -67.19% |    -0.45 |       62 | 32.76%     | ok               |
|          20 | -54.34%  | -71.48%            | -74.98% |    -0.49 |       94 | 48.47%     | ok               |

## FXI Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -1.96%   | 28.39%             | -21.68% |     0.04 |       50 | 34.94%     | ok               |
|          25 | -2.08%   | 28.39%             | -22.57% |     0.03 |       48 | 31.78%     | ok               |
|          30 | -4.22%   | 28.39%             | -23.91% |    -0.02 |       46 | 30.45%     | ok               |
|          35 | -6.68%   | 28.39%             | -27.53% |    -0.09 |       48 | 27.79%     | ok               |
|          20 | -7.25%   | 28.39%             | -24.53% |    -0.1  |       48 | 33.11%     | ok               |

## GDX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -2.80%   | 150.69%            | -31.05% |     0.12 |       82 | 51.25%     | ok               |
|          40 | -4.94%   | 150.69%            | -34.42% |     0.05 |       66 | 38.94%     | ok               |
|          30 | -6.36%   | 150.69%            | -34.29% |     0.04 |       68 | 45.09%     | ok               |
|          35 | -10.44%  | 150.69%            | -38.67% |    -0.03 |       74 | 41.60%     | ok               |
|          25 | -15.19%  | 150.69%            | -42.42% |    -0.09 |       72 | 46.92%     | ok               |

## GDXJ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -16.79%  | 146.37%            | -34.84% |    -0.05 |       72 | 51.58%     | ok               |
|          35 | -28.11%  | 146.37%            | -38.09% |    -0.29 |       70 | 41.76%     | ok               |
|          30 | -30.10%  | 146.37%            | -36.01% |    -0.32 |       70 | 44.43%     | ok               |
|          25 | -34.34%  | 146.37%            | -39.67% |    -0.37 |       75 | 47.59%     | ok               |
|          40 | -30.85%  | 146.37%            | -46.16% |    -0.38 |       64 | 39.27%     | ok               |

## GE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 4.89%    | 108.69%            | -21.25% |     0.2  |       60 | 33.78%     | ok               |
|          45 | -7.35%   | 108.69%            | -21.88% |    -0.05 |       72 | 36.77%     | ok               |
|          20 | -13.05%  | 108.69%            | -25.05% |    -0.12 |       73 | 52.75%     | ok               |
|          30 | -13.14%  | 108.69%            | -27.82% |    -0.14 |       78 | 48.42%     | ok               |
|          25 | -13.54%  | 108.69%            | -29.91% |    -0.14 |       74 | 50.25%     | ok               |

## GLD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | 21.05%   | 70.02%             | -13.87% |     0.54 |       48 | 47.59%     | ok               |
|          20 | 19.41%   | 70.02%             | -13.87% |     0.51 |       49 | 49.25%     | ok               |
|          30 | 11.67%   | 70.02%             | -14.15% |     0.35 |       52 | 46.09%     | ok               |
|          35 | 8.96%    | 70.02%             | -15.57% |     0.3  |       52 | 43.43%     | ok               |
|          15 | 9.15%    | 70.02%             | -18.05% |     0.29 |       55 | 52.75%     | ok               |

## GOOGL Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 73.57%   | 63.36%             | -17.38% |     1.15 |       59 | 44.93%     | ok               |
|          30 | 69.61%   | 63.36%             | -17.43% |     1.09 |       57 | 48.59%     | ok               |
|          45 | 61.22%   | 63.36%             | -11.66% |     1.07 |       52 | 38.44%     | ok               |
|          25 | 67.02%   | 63.36%             | -16.76% |     1.05 |       57 | 51.08%     | ok               |
|          50 | 56.47%   | 63.36%             | -11.52% |     1.04 |       44 | 33.61%     | ok               |

## GRT-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 108.46%  | -82.36%            | -36.70% |     0.92 |       70 | 62.45%     | ok               |
|          45 | 80.47%   | -82.36%            | -39.68% |     0.89 |       50 | 29.31%     | ok               |
|          30 | 76.91%   | -82.36%            | -43.87% |     0.8  |       75 | 47.89%     | ok               |
|          35 | 74.39%   | -82.36%            | -37.94% |     0.8  |       66 | 42.53%     | ok               |
|          25 | 76.59%   | -82.36%            | -37.25% |     0.78 |       80 | 53.07%     | ok               |

## GS Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 22.58%   | 105.88%            | -20.56% |     0.5  |       66 | 55.24%     | ok               |
|          40 | 7.27%    | 105.88%            | -16.16% |     0.25 |       64 | 40.93%     | ok               |
|          20 | 7.49%    | 105.88%            | -23.19% |     0.25 |       64 | 51.91%     | ok               |
|          25 | -0.60%   | 105.88%            | -23.32% |     0.09 |       66 | 49.92%     | ok               |
|          35 | -1.92%   | 105.88%            | -19.95% |     0.06 |       68 | 44.59%     | ok               |

## HBAR-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -22.53%  | -36.56%            | -49.09% |    -0.3  |       28 | 27.74%     | ok               |
|          40 | -24.21%  | -36.56%            | -51.16% |    -0.32 |       32 | 33.56%     | ok               |
|          50 | -24.56%  | -36.56%            | -39.47% |    -0.41 |       32 | 18.84%     | ok               |
|          35 | -28.42%  | -36.56%            | -56.01% |    -0.41 |       30 | 38.70%     | ok               |
|          30 | -29.16%  | -36.56%            | -56.47% |    -0.42 |       40 | 42.81%     | ok               |

## HD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 5.52%    | -1.26%             | -17.15% |     0.22 |       71 | 44.76%     | ok               |
|          35 | 4.13%    | -1.26%             | -16.66% |     0.19 |       72 | 40.10%     | ok               |
|          25 | 1.92%    | -1.26%             | -17.03% |     0.13 |       72 | 47.25%     | ok               |
|          40 | 0.77%    | -1.26%             | -15.45% |     0.1  |       74 | 34.78%     | ok               |
|          45 | -0.02%   | -1.26%             | -16.13% |     0.07 |       50 | 29.95%     | ok               |

## HON Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -11.45%  | 7.07%              | -20.54% |    -0.29 |       64 | 31.45%     | ok               |
|          45 | -15.37%  | 7.07%              | -22.88% |    -0.4  |       66 | 36.77%     | ok               |
|          35 | -28.67%  | 7.07%              | -32.46% |    -0.77 |       89 | 48.92%     | ok               |
|          30 | -30.23%  | 7.07%              | -34.64% |    -0.79 |       89 | 53.91%     | ok               |
|          40 | -28.51%  | 7.07%              | -32.19% |    -0.8  |       78 | 41.43%     | ok               |

## HYG Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -4.83%   | -0.05%             | -7.93%  |    -0.55 |       68 | 33.61%     | ok               |
|          45 | -6.59%   | -0.05%             | -9.07%  |    -0.8  |       68 | 29.95%     | ok               |
|          25 | -7.56%   | -0.05%             | -11.22% |    -0.82 |       89 | 42.43%     | ok               |
|          20 | -7.62%   | -0.05%             | -11.64% |    -0.82 |       94 | 44.93%     | ok               |
|          35 | -7.10%   | -0.05%             | -9.76%  |    -0.82 |       79 | 35.61%     | ok               |

## IBIT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 52.34%   | 11.13%             | -17.37% |     0.92 |       26 | 24.56%     | ok               |
|          15 | 59.66%   | 11.13%             | -19.20% |     0.87 |       48 | 42.88%     | ok               |
|          45 | 42.91%   | 11.13%             | -17.37% |     0.78 |       32 | 25.93%     | ok               |
|          30 | 30.75%   | 11.13%             | -18.95% |     0.59 |       46 | 35.48%     | ok               |
|          40 | 27.24%   | 11.13%             | -22.57% |     0.56 |       40 | 28.85%     | ok               |

## IBM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -14.62%  | 43.93%             | -49.43% |    -0.06 |       85 | 62.56%     | ok               |
|          35 | -18.22%  | 43.93%             | -47.10% |    -0.16 |       63 | 47.59%     | ok               |
|          30 | -19.93%  | 43.93%             | -48.94% |    -0.19 |       69 | 50.75%     | ok               |
|          20 | -26.87%  | 43.93%             | -53.45% |    -0.29 |       71 | 55.57%     | ok               |
|          50 | -27.41%  | 43.93%             | -45.97% |    -0.39 |       46 | 36.61%     | ok               |

## ICP-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 5.46%    | -57.77%            | -40.56% |     0.31 |       72 | 40.04%     | ok               |
|          35 | -8.12%   | -57.77%            | -52.30% |     0.14 |       68 | 34.87%     | ok               |
|          40 | -8.24%   | -57.77%            | -46.01% |     0.13 |       62 | 30.65%     | ok               |
|          15 | -30.07%  | -57.77%            | -59.32% |     0.05 |       74 | 51.92%     | ok               |
|          20 | -29.41%  | -57.77%            | -62.99% |     0.04 |       82 | 48.85%     | ok               |

## IEF Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -6.08%   | -3.61%             | -10.18% |    -0.71 |       72 | 42.76%     | ok               |
|          15 | -7.30%   | -3.61%             | -10.91% |    -0.84 |       71 | 44.43%     | ok               |
|          40 | -7.77%   | -3.61%             | -10.34% |    -1.12 |       66 | 26.12%     | ok               |
|          25 | -9.59%   | -3.61%             | -11.95% |    -1.2  |       76 | 39.77%     | ok               |
|          45 | -8.33%   | -3.61%             | -10.45% |    -1.25 |       62 | 23.96%     | ok               |

## IEMG Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -4.26%   | 40.80%             | -23.73% |    -0.06 |       61 | 43.76%     | ok               |
|          35 | -4.18%   | 40.80%             | -21.81% |    -0.07 |       67 | 40.43%     | ok               |
|          20 | -5.87%   | 40.80%             | -25.26% |    -0.11 |       59 | 45.42%     | ok               |
|          40 | -5.81%   | 40.80%             | -18.43% |    -0.14 |       66 | 38.10%     | ok               |
|          30 | -7.37%   | 40.80%             | -24.73% |    -0.17 |       62 | 41.43%     | ok               |

## INJ-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 29.98%   | -45.80%            | -44.07% |     0.5  |       52 | 35.82%     | ok               |
|          40 | 26.67%   | -45.80%            | -35.85% |     0.47 |       44 | 32.76%     | ok               |
|          45 | 5.50%    | -45.80%            | -42.40% |     0.27 |       50 | 26.63%     | ok               |
|          15 | -11.08%  | -45.80%            | -64.35% |     0.18 |       68 | 46.74%     | ok               |
|          25 | -11.61%  | -45.80%            | -57.65% |     0.15 |       59 | 41.95%     | ok               |

## INTC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 86.97%   | 101.03%            | -49.32% |     0.78 |       60 | 34.94%     | ok               |
|          50 | 81.16%   | 101.03%            | -48.35% |     0.76 |       64 | 31.11%     | ok               |
|          40 | 66.46%   | 101.03%            | -55.86% |     0.67 |       68 | 39.10%     | ok               |
|          15 | 66.25%   | 101.03%            | -53.65% |     0.66 |       80 | 60.07%     | ok               |
|          20 | 60.12%   | 101.03%            | -52.47% |     0.63 |       82 | 56.24%     | ok               |

## INTU Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 13.73%   | -45.80%            | -33.65% |     0.35 |       67 | 29.78%     | ok               |
|          35 | 9.89%    | -45.80%            | -40.91% |     0.28 |       69 | 42.26%     | ok               |
|          45 | 7.91%    | -45.80%            | -35.63% |     0.25 |       65 | 33.94%     | ok               |
|          25 | 7.10%    | -45.80%            | -35.24% |     0.24 |       69 | 50.75%     | ok               |
|          40 | 6.18%    | -45.80%            | -37.97% |     0.22 |       69 | 37.44%     | ok               |

## ITA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 0.84%    | 63.51%             | -25.76% |     0.11 |       73 | 59.73%     | ok               |
|          50 | -0.12%   | 63.51%             | -21.48% |     0.06 |       68 | 34.94%     | ok               |
|          30 | -1.32%   | 63.51%             | -23.75% |     0.04 |       72 | 47.42%     | ok               |
|          40 | -4.89%   | 63.51%             | -20.54% |    -0.08 |       70 | 39.93%     | ok               |
|          35 | -5.60%   | 63.51%             | -23.12% |    -0.09 |       72 | 43.59%     | ok               |

## IWM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd    |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:-------|---------:|---------:|:-----------|:-----------------|
|          25 | 17.01%   | 41.30%             | -8.02% |     0.63 |       54 | 36.11%     | ok               |
|          20 | 15.47%   | 41.30%             | -9.67% |     0.57 |       60 | 37.10%     | ok               |
|          15 | 11.92%   | 41.30%             | -8.91% |     0.44 |       78 | 42.93%     | ok               |
|          30 | 10.62%   | 41.30%             | -8.62% |     0.43 |       58 | 34.78%     | ok               |
|          40 | 8.85%    | 41.30%             | -9.06% |     0.4  |       48 | 29.78%     | ok               |

## JNJ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 19.04%   | 88.51%             | -10.97% |     0.75 |       46 | 35.44%     | ok               |
|          15 | 18.33%   | 88.51%             | -18.02% |     0.62 |       58 | 53.41%     | ok               |
|          30 | 13.24%   | 88.51%             | -17.51% |     0.5  |       60 | 46.92%     | ok               |
|          20 | 12.87%   | 88.51%             | -17.61% |     0.48 |       64 | 49.92%     | ok               |
|          45 | 9.19%    | 88.51%             | -13.35% |     0.39 |       50 | 39.27%     | ok               |

## JPM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 1.50%    | 74.93%             | -15.90% |     0.11 |       50 | 31.78%     | ok               |
|          45 | -8.97%   | 74.93%             | -21.91% |    -0.23 |       54 | 34.44%     | ok               |
|          20 | -24.26%  | 74.93%             | -35.58% |    -0.55 |       86 | 48.75%     | ok               |
|          40 | -21.46%  | 74.93%             | -28.47% |    -0.65 |       66 | 37.10%     | ok               |
|          35 | -22.15%  | 74.93%             | -27.43% |    -0.66 |       76 | 40.60%     | ok               |

## KO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 30.66%   | 55.44%             | -8.64%  |     1    |       52 | 39.27%     | ok               |
|          35 | 26.22%   | 55.44%             | -8.73%  |     0.89 |       56 | 37.77%     | ok               |
|          40 | 22.49%   | 55.44%             | -9.28%  |     0.83 |       58 | 34.61%     | ok               |
|          25 | 24.30%   | 55.44%             | -10.61% |     0.82 |       58 | 41.93%     | ok               |
|          50 | 9.47%    | 55.44%             | -16.13% |     0.42 |       44 | 28.79%     | ok               |

## LDO-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 146.12%  | -64.81%            | -39.01% |     1.01 |       73 | 60.15%     | ok               |
|          20 | 79.46%   | -64.81%            | -44.07% |     0.77 |       76 | 55.56%     | ok               |
|          30 | 56.70%   | -64.81%            | -52.34% |     0.66 |       66 | 48.28%     | ok               |
|          25 | 42.50%   | -64.81%            | -48.17% |     0.58 |       72 | 52.87%     | ok               |
|          35 | 27.81%   | -64.81%            | -60.70% |     0.48 |       76 | 41.38%     | ok               |

## LIN Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -0.31%   | 18.93%             | -22.01% |     0.05 |       71 | 44.26%     | ok               |
|          20 | -0.39%   | 18.93%             | -23.00% |     0.05 |       64 | 47.25%     | ok               |
|          15 | -2.31%   | 18.93%             | -23.68% |    -0.01 |       70 | 50.25%     | ok               |
|          30 | -3.64%   | 18.93%             | -20.61% |    -0.06 |       72 | 41.43%     | ok               |
|          45 | -3.18%   | 18.93%             | -17.04% |    -0.07 |       48 | 25.12%     | ok               |

## LINK-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 36.86%   | -30.14%            | -35.01% |     0.56 |       70 | 43.30%     | ok               |
|          35 | 27.98%   | -30.14%            | -34.21% |     0.49 |       66 | 38.70%     | ok               |
|          40 | 22.95%   | -30.14%            | -34.00% |     0.45 |       60 | 33.14%     | ok               |
|          45 | 18.14%   | -30.14%            | -33.71% |     0.4  |       54 | 29.50%     | ok               |
|          50 | 17.72%   | -30.14%            | -27.70% |     0.39 |       46 | 24.33%     | ok               |

## LLY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 5.35%    | 62.61%             | -38.23% |     0.21 |       50 | 35.44%     | ok               |
|          15 | -9.52%   | 62.61%             | -48.12% |    -0    |       70 | 60.23%     | ok               |
|          45 | -8.91%   | 62.61%             | -42.99% |    -0.05 |       60 | 39.27%     | ok               |
|          40 | -18.53%  | 62.61%             | -45.23% |    -0.22 |       70 | 42.43%     | ok               |
|          20 | -22.09%  | 62.61%             | -51.14% |    -0.24 |       77 | 55.41%     | ok               |

## LRCX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -9.95%   | 124.57%            | -48.71% |     0.07 |       76 | 36.61%     | ok               |
|          40 | -18.22%  | 124.57%            | -53.45% |    -0.01 |       72 | 42.93%     | ok               |
|          35 | -19.79%  | 124.57%            | -56.72% |    -0.03 |       80 | 45.09%     | ok               |
|          15 | -24.36%  | 124.57%            | -57.13% |    -0.04 |       80 | 53.91%     | ok               |
|          20 | -24.71%  | 124.57%            | -59.99% |    -0.06 |       84 | 49.75%     | ok               |

## LTC-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 26.69%   | -45.48%            | -34.94% |     0.5  |       66 | 44.06%     | ok               |
|          45 | 20.44%   | -45.48%            | -36.44% |     0.44 |       56 | 33.14%     | ok               |
|          30 | 17.24%   | -45.48%            | -30.78% |     0.39 |       69 | 50.77%     | ok               |
|          25 | 15.87%   | -45.48%            | -34.22% |     0.38 |       69 | 53.45%     | ok               |
|          50 | 6.20%    | -45.48%            | -35.25% |     0.25 |       48 | 24.90%     | ok               |

## MCD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 6.99%    | 5.94%              | -9.22%  |     0.34 |       48 | 25.46%     | ok               |
|          30 | 8.48%    | 5.94%              | -22.20% |     0.34 |       75 | 40.60%     | ok               |
|          35 | 6.35%    | 5.94%              | -16.97% |     0.29 |       67 | 37.94%     | ok               |
|          25 | 5.12%    | 5.94%              | -23.93% |     0.23 |       75 | 43.09%     | ok               |
|          20 | 0.83%    | 5.94%              | -24.58% |     0.09 |       77 | 46.26%     | ok               |

## META Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -16.80%  | 27.08%             | -37.54% |    -0.2  |       68 | 39.27%     | ok               |
|          40 | -20.31%  | 27.08%             | -40.90% |    -0.25 |       68 | 42.60%     | ok               |
|          50 | -21.37%  | 27.08%             | -39.33% |    -0.32 |       68 | 34.78%     | ok               |
|          30 | -31.00%  | 27.08%             | -44.90% |    -0.45 |       72 | 50.58%     | ok               |
|          25 | -33.07%  | 27.08%             | -45.70% |    -0.49 |       73 | 53.24%     | ok               |

## MPC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 19.12%   | 133.30%            | -19.02% |     0.43 |       54 | 41.60%     | ok               |
|          40 | 17.16%   | 133.30%            | -20.88% |     0.39 |       64 | 48.25%     | ok               |
|          35 | 16.33%   | 133.30%            | -31.08% |     0.38 |       70 | 50.92%     | ok               |
|          45 | 15.10%   | 133.30%            | -20.23% |     0.37 |       60 | 45.59%     | ok               |
|          30 | 11.57%   | 133.30%            | -33.74% |     0.31 |       70 | 53.41%     | ok               |

## MRK Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -12.97%  | 12.59%             | -28.39% |    -0.16 |       85 | 52.58%     | ok               |
|          25 | -13.74%  | 12.59%             | -31.07% |    -0.19 |       72 | 44.76%     | ok               |
|          20 | -17.97%  | 12.59%             | -29.34% |    -0.29 |       77 | 48.09%     | ok               |
|          50 | -14.43%  | 12.59%             | -23.01% |    -0.29 |       58 | 29.12%     | ok               |
|          45 | -16.55%  | 12.59%             | -25.38% |    -0.33 |       59 | 32.45%     | ok               |

## MS Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 1.94%    | 98.22%             | -19.99% |     0.13 |       68 | 38.77%     | ok               |
|          15 | 0.94%    | 98.22%             | -22.02% |     0.12 |       74 | 57.24%     | ok               |
|          20 | -2.26%   | 98.22%             | -25.68% |     0.04 |       73 | 52.91%     | ok               |
|          30 | -6.28%   | 98.22%             | -27.79% |    -0.06 |       75 | 47.92%     | ok               |
|          25 | -7.75%   | 98.22%             | -28.36% |    -0.1  |       73 | 50.08%     | ok               |

## MSFT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -16.97%  | 15.86%             | -25.54% |    -0.4  |       72 | 37.10%     | ok               |
|          50 | -20.33%  | 15.86%             | -26.37% |    -0.53 |       62 | 31.95%     | ok               |
|          30 | -27.33%  | 15.86%             | -38.06% |    -0.6  |       81 | 50.92%     | ok               |
|          35 | -26.45%  | 15.86%             | -36.28% |    -0.6  |       75 | 46.59%     | ok               |
|          40 | -26.10%  | 15.86%             | -35.70% |    -0.62 |       71 | 40.77%     | ok               |

## MU Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 93.29%   | 481.41%            | -61.15% |     0.82 |       60 | 45.26%     | ok               |
|          45 | 83.52%   | 481.41%            | -62.31% |     0.78 |       62 | 42.60%     | ok               |
|          30 | 73.89%   | 481.41%            | -66.33% |     0.72 |       53 | 49.92%     | ok               |
|          15 | 76.27%   | 481.41%            | -61.96% |     0.71 |       56 | 58.40%     | ok               |
|          35 | 69.08%   | 481.41%            | -66.69% |     0.7  |       65 | 47.59%     | ok               |

## NEAR-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 223.63%  | 37.77%             | -40.07% |     1.41 |       30 | 22.41%     | ok               |
|          40 | 257.67%  | 37.77%             | -41.76% |     1.41 |       40 | 32.38%     | ok               |
|          45 | 200.17%  | 37.77%             | -38.08% |     1.26 |       42 | 28.35%     | ok               |
|          30 | 174.64%  | 37.77%             | -46.60% |     1.12 |       65 | 43.30%     | ok               |
|          35 | 161.03%  | 37.77%             | -52.15% |     1.11 |       60 | 36.21%     | ok               |

## NEM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -7.46%   | 180.34%            | -35.45% |     0.08 |       66 | 58.90%     | ok               |
|          20 | -7.68%   | 180.34%            | -32.74% |     0.06 |       73 | 53.91%     | ok               |
|          50 | -12.51%  | 180.34%            | -33.03% |    -0.06 |       48 | 37.77%     | ok               |
|          25 | -21.78%  | 180.34%            | -39.51% |    -0.17 |       70 | 51.58%     | ok               |
|          30 | -28.27%  | 180.34%            | -41.53% |    -0.29 |       72 | 49.58%     | ok               |

## NFLX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 16.93%   | -5.93%             | -20.78% |     0.46 |       54 | 38.94%     | ok               |
|          50 | 14.33%   | -5.93%             | -16.28% |     0.43 |       44 | 30.62%     | ok               |
|          35 | 10.69%   | -5.93%             | -18.30% |     0.32 |       78 | 43.76%     | ok               |
|          45 | 2.90%    | -5.93%             | -18.06% |     0.16 |       58 | 34.94%     | ok               |
|          15 | -2.34%   | -5.93%             | -26.59% |     0.08 |       76 | 63.89%     | ok               |

## NKE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | -20.22%  | -60.57%            | -42.13% |    -0.23 |       73 | 39.93%     | ok               |
|          20 | -27.18%  | -60.57%            | -49.34% |    -0.27 |       87 | 55.24%     | ok               |
|          25 | -30.19%  | -60.57%            | -51.20% |    -0.34 |       87 | 52.58%     | ok               |
|          15 | -33.51%  | -60.57%            | -55.79% |    -0.39 |       90 | 59.07%     | ok               |
|          40 | -23.13%  | -60.57%            | -33.81% |    -0.41 |       67 | 32.45%     | ok               |

## NOW Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -13.46%  | -31.43%            | -49.77% |     0.07 |       73 | 57.57%     | ok               |
|          30 | -14.52%  | -31.43%            | -42.66% |     0.04 |       81 | 52.08%     | ok               |
|          15 | -19.87%  | -31.43%            | -52.56% |    -0.01 |       81 | 60.23%     | ok               |
|          25 | -20.65%  | -31.43%            | -47.93% |    -0.03 |       73 | 55.41%     | ok               |
|          35 | -26.13%  | -31.43%            | -48.24% |    -0.14 |       84 | 47.25%     | ok               |

## NVDA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -31.39%  | 33.64%             | -39.21% |    -0.36 |       76 | 51.52%     | ok               |
|          25 | -36.24%  | 33.64%             | -44.52% |    -0.5  |       81 | 47.59%     | ok               |
|          30 | -36.03%  | 33.64%             | -43.72% |    -0.52 |       82 | 44.74%     | ok               |
|          15 | -42.87%  | 33.64%             | -51.27% |    -0.59 |       82 | 55.79%     | ok               |
|          35 | -45.65%  | 33.64%             | -51.85% |    -0.79 |       92 | 41.89%     | ok               |

## OP-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 36.28%   | -85.40%            | -30.63% |     0.66 |       38 | 10.34%     | ok               |
|          45 | 26.69%   | -85.40%            | -28.24% |     0.49 |       40 | 16.48%     | ok               |
|          40 | 0.95%    | -85.40%            | -43.68% |     0.21 |       48 | 24.71%     | ok               |
|          15 | -27.42%  | -85.40%            | -55.83% |    -0.03 |       75 | 46.74%     | ok               |
|          30 | -31.11%  | -85.40%            | -57.83% |    -0.15 |       74 | 35.25%     | ok               |

## ORCL Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 127.80%  | -9.27%             | -37.57% |     0.98 |       67 | 60.40%     | ok               |
|          45 | 92.99%   | -9.27%             | -32.35% |     0.9  |       54 | 37.94%     | ok               |
|          25 | 83.15%   | -9.27%             | -31.04% |     0.79 |       59 | 52.91%     | ok               |
|          35 | 74.48%   | -9.27%             | -31.95% |     0.75 |       60 | 47.09%     | ok               |
|          20 | 78.04%   | -9.27%             | -32.58% |     0.75 |       68 | 56.07%     | ok               |

## OXY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 1.75%    | -6.04%             | -28.48% |     0.15 |       67 | 43.26%     | ok               |
|          35 | 1.89%    | -6.04%             | -26.37% |     0.15 |       68 | 38.94%     | ok               |
|          40 | -2.37%   | -6.04%             | -28.30% |     0.07 |       58 | 35.77%     | ok               |
|          50 | -2.47%   | -6.04%             | -26.34% |     0.06 |       48 | 28.95%     | ok               |
|          25 | -12.44%  | -6.04%             | -38.51% |    -0.09 |       75 | 46.92%     | ok               |

## PEP Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 23.24%   | -13.95%            | -11.62% |     0.9  |       40 | 26.46%     | ok               |
|          45 | 10.82%   | -13.95%            | -14.22% |     0.45 |       52 | 30.12%     | ok               |
|          30 | 3.95%    | -13.95%            | -21.35% |     0.18 |       72 | 45.42%     | ok               |
|          35 | 2.33%    | -13.95%            | -21.42% |     0.14 |       75 | 39.77%     | ok               |
|          40 | -0.02%   | -13.95%            | -18.04% |     0.06 |       68 | 34.94%     | ok               |

## PEPE-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -40.52%  | -64.90%            | -64.58% |    -0.05 |       77 | 60.92%     | ok               |
|          30 | -38.57%  | -64.90%            | -60.19% |    -0.14 |       72 | 46.55%     | ok               |
|          20 | -43.42%  | -64.90%            | -63.48% |    -0.16 |       85 | 56.70%     | ok               |
|          35 | -44.12%  | -64.90%            | -60.83% |    -0.3  |       64 | 42.72%     | ok               |
|          25 | -54.17%  | -64.90%            | -64.37% |    -0.37 |       86 | 51.53%     | ok               |

## PFE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -15.07%  | 6.16%              | -25.81% |    -0.45 |       52 | 22.96%     | ok               |
|          50 | -14.14%  | 6.16%              | -27.79% |    -0.46 |       40 | 19.63%     | ok               |
|          40 | -16.66%  | 6.16%              | -29.39% |    -0.48 |       72 | 27.95%     | ok               |
|          35 | -24.68%  | 6.16%              | -35.00% |    -0.73 |       82 | 34.44%     | ok               |
|          30 | -32.42%  | 6.16%              | -41.77% |    -0.98 |       77 | 37.44%     | ok               |

## PG Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -6.69%   | -0.35%             | -19.77% |    -0.2  |       50 | 29.78%     | ok               |
|          35 | -9.88%   | -0.35%             | -18.66% |    -0.32 |       58 | 33.28%     | ok               |
|          45 | -14.60%  | -0.35%             | -21.69% |    -0.55 |       50 | 27.45%     | ok               |
|          30 | -18.06%  | -0.35%             | -24.25% |    -0.62 |       60 | 36.44%     | ok               |
|          25 | -19.93%  | -0.35%             | -25.55% |    -0.69 |       72 | 37.94%     | ok               |

## PM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | -3.98%   | 96.51%             | -35.28% |    -0    |       84 | 44.59%     | ok               |
|          20 | -6.49%   | 96.51%             | -36.74% |    -0.05 |       83 | 53.24%     | ok               |
|          30 | -7.00%   | 96.51%             | -38.30% |    -0.07 |       79 | 48.09%     | ok               |
|          50 | -9.22%   | 96.51%             | -36.94% |    -0.16 |       66 | 35.44%     | ok               |
|          40 | -11.50%  | 96.51%             | -39.92% |    -0.21 |       78 | 41.10%     | ok               |

## POL-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 6.17%    | -60.68%            | -45.37% |     0.28 |       85 | 49.62%     | ok               |
|          50 | 8.48%    | -60.68%            | -30.34% |     0.28 |       54 | 21.07%     | ok               |
|          20 | 3.15%    | -60.68%            | -47.73% |     0.26 |       85 | 58.43%     | ok               |
|          25 | 2.24%    | -60.68%            | -45.37% |     0.25 |       75 | 54.60%     | ok               |
|          40 | -1.20%   | -60.68%            | -32.62% |     0.17 |       60 | 32.38%     | ok               |

## QCOM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -25.01%  | -16.92%            | -48.56% |    -0.16 |       73 | 42.10%     | ok               |
|          20 | -30.52%  | -16.92%            | -48.41% |    -0.24 |       69 | 45.42%     | ok               |
|          35 | -31.34%  | -16.92%            | -44.12% |    -0.29 |       81 | 37.77%     | ok               |
|          15 | -38.91%  | -16.92%            | -52.44% |    -0.38 |       71 | 48.09%     | ok               |
|          30 | -39.35%  | -16.92%            | -50.91% |    -0.43 |       79 | 40.27%     | ok               |

## QQQ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 3.69%    | 43.78%             | -17.14% |     0.18 |       71 | 52.75%     | ok               |
|          25 | 0.28%    | 43.78%             | -14.03% |     0.09 |       65 | 45.59%     | ok               |
|          20 | -0.93%   | 43.78%             | -14.85% |     0.06 |       77 | 48.75%     | ok               |
|          30 | -6.49%   | 43.78%             | -15.82% |    -0.1  |       70 | 43.59%     | ok               |
|          50 | -14.31%  | 43.78%             | -22.73% |    -0.42 |       62 | 28.12%     | ok               |

## RENDER-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 29.13%   | -62.21%            | -44.75% |     0.51 |       86 | 63.22%     | ok               |
|          20 | 17.68%   | -62.21%            | -43.43% |     0.43 |       91 | 58.81%     | ok               |
|          25 | 4.64%    | -62.21%            | -43.13% |     0.32 |       89 | 54.02%     | ok               |
|          30 | -39.92%  | -62.21%            | -54.46% |    -0.2  |       92 | 48.28%     | ok               |
|          35 | -41.51%  | -62.21%            | -55.67% |    -0.27 |       82 | 42.72%     | ok               |

## RTX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 34.79%   | 90.60%             | -18.66% |     0.73 |       74 | 57.74%     | ok               |
|          25 | 30.19%   | 90.60%             | -18.59% |     0.66 |       62 | 55.07%     | ok               |
|          15 | 26.65%   | 90.60%             | -19.55% |     0.59 |       67 | 62.23%     | ok               |
|          30 | 21.35%   | 90.60%             | -16.99% |     0.52 |       71 | 52.25%     | ok               |
|          50 | 14.89%   | 90.60%             | -18.42% |     0.47 |       62 | 39.43%     | ok               |

## SBUX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | 5.72%    | 37.52%             | -23.55% |     0.22 |       61 | 42.43%     | ok               |
|          40 | 3.51%    | 37.52%             | -25.43% |     0.17 |       60 | 33.94%     | ok               |
|          45 | 1.54%    | 37.52%             | -27.26% |     0.12 |       66 | 29.12%     | ok               |
|          35 | -0.05%   | 37.52%             | -26.54% |     0.1  |       64 | 37.27%     | ok               |
|          50 | -3.81%   | 37.52%             | -25.13% |    -0.01 |       52 | 24.63%     | ok               |

## SCHW Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -1.47%   | 26.51%             | -29.24% |     0.06 |       71 | 52.58%     | ok               |
|          25 | -3.28%   | 26.51%             | -28.76% |     0.02 |       67 | 50.92%     | ok               |
|          45 | -3.45%   | 26.51%             | -16.53% |    -0.04 |       62 | 31.28%     | ok               |
|          15 | -6.89%   | 26.51%             | -31.37% |    -0.06 |       78 | 56.57%     | ok               |
|          50 | -3.90%   | 26.51%             | -13.28% |    -0.08 |       54 | 28.12%     | ok               |

## SHIB-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -9.76%   | -67.05%            | -32.18% |    -0.02 |       50 | 21.84%     | ok               |
|          15 | -19.28%  | -67.05%            | -47.25% |    -0.04 |       85 | 65.71%     | ok               |
|          35 | -17.96%  | -67.05%            | -43.57% |    -0.07 |       75 | 46.36%     | ok               |
|          20 | -22.67%  | -67.05%            | -49.90% |    -0.1  |       78 | 61.11%     | ok               |
|          40 | -22.77%  | -67.05%            | -41.51% |    -0.18 |       62 | 37.55%     | ok               |

## SHY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd    |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:-------|---------:|---------:|:-----------|:-----------------|
|          30 | -2.40%   | -0.40%             | -3.30% |    -0.78 |       54 | 38.60%     | ok               |
|          40 | -2.57%   | -0.40%             | -3.52% |    -0.87 |       58 | 35.11%     | ok               |
|          45 | -2.48%   | -0.40%             | -3.37% |    -0.91 |       56 | 28.79%     | ok               |
|          35 | -2.93%   | -0.40%             | -3.61% |    -0.97 |       56 | 36.44%     | ok               |
|          50 | -2.61%   | -0.40%             | -3.34% |    -1.01 |       48 | 24.96%     | ok               |

## SKY-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -54.64%  | -31.58%            | -65.72% |    -0.68 |       79 | 55.56%     | ok               |
|          35 | -51.23%  | -31.58%            | -60.94% |    -0.76 |       78 | 36.97%     | ok               |
|          30 | -54.56%  | -31.58%            | -63.60% |    -0.79 |       87 | 45.02%     | ok               |
|          25 | -59.70%  | -31.58%            | -66.89% |    -0.9  |       80 | 48.28%     | ok               |
|          40 | -55.63%  | -31.58%            | -63.28% |    -0.94 |       66 | 33.52%     | ok               |

## SLB Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -14.99%  | 11.61%             | -30.85% |    -0.22 |       52 | 33.94%     | ok               |
|          45 | -15.15%  | 11.61%             | -29.16% |    -0.23 |       58 | 31.28%     | ok               |
|          50 | -13.64%  | 11.61%             | -27.89% |    -0.25 |       46 | 24.63%     | ok               |
|          35 | -36.99%  | 11.61%             | -48.67% |    -0.75 |       74 | 41.93%     | ok               |
|          25 | -40.10%  | 11.61%             | -52.31% |    -0.76 |       86 | 51.75%     | ok               |

## SLV Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 66.55%   | 72.91%             | -28.72% |     0.86 |       50 | 31.45%     | ok               |
|          45 | 52.41%   | 72.91%             | -31.33% |     0.73 |       61 | 32.95%     | ok               |
|          40 | 51.20%   | 72.91%             | -34.28% |     0.72 |       65 | 34.94%     | ok               |
|          20 | 41.05%   | 72.91%             | -37.05% |     0.61 |       70 | 45.42%     | ok               |
|          15 | 38.69%   | 72.91%             | -47.98% |     0.57 |       71 | 50.08%     | ok               |

## SMH Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 60.09%   | 91.39%             | -31.66% |     0.85 |       49 | 44.93%     | ok               |
|          25 | 45.62%   | 91.39%             | -33.57% |     0.72 |       46 | 43.43%     | ok               |
|          30 | 41.65%   | 91.39%             | -34.29% |     0.68 |       50 | 42.10%     | ok               |
|          35 | 31.11%   | 91.39%             | -34.65% |     0.57 |       56 | 40.10%     | ok               |
|          45 | 19.52%   | 91.39%             | -32.84% |     0.44 |       56 | 34.28%     | ok               |

## SNX-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 30.87%   | -76.29%            | -29.01% |     0.54 |       46 | 26.82%     | ok               |
|          35 | 30.80%   | -76.29%            | -42.92% |     0.52 |       52 | 31.03%     | ok               |
|          20 | 24.59%   | -76.29%            | -53.03% |     0.47 |       71 | 46.17%     | ok               |
|          15 | 10.82%   | -76.29%            | -54.74% |     0.35 |       72 | 50.19%     | ok               |
|          30 | 10.55%   | -76.29%            | -50.74% |     0.33 |       62 | 36.97%     | ok               |

## SOL-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 66.29%   | -48.82%            | -39.12% |     0.82 |       54 | 38.51%     | ok               |
|          35 | 38.77%   | -48.82%            | -43.12% |     0.59 |       66 | 44.64%     | ok               |
|          45 | 19.67%   | -48.82%            | -46.28% |     0.42 |       48 | 32.38%     | ok               |
|          25 | 16.80%   | -48.82%            | -37.29% |     0.39 |       69 | 55.56%     | ok               |
|          30 | 15.83%   | -48.82%            | -41.75% |     0.38 |       73 | 51.15%     | ok               |

## SOXX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | 50.75%   | 86.64%             | -39.32% |     0.74 |       55 | 43.09%     | ok               |
|          35 | 47.35%   | 86.64%             | -38.76% |     0.72 |       58 | 38.60%     | ok               |
|          30 | 46.56%   | 86.64%             | -39.81% |     0.7  |       56 | 40.93%     | ok               |
|          20 | 37.43%   | 86.64%             | -39.19% |     0.6  |       61 | 44.09%     | ok               |
|          40 | 29.33%   | 86.64%             | -41.03% |     0.53 |       60 | 36.44%     | ok               |

## SPY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 4.32%    | 39.54%             | -14.25% |     0.2  |       60 | 51.25%     | ok               |
|          15 | 1.79%    | 39.54%             | -16.80% |     0.12 |       66 | 54.24%     | ok               |
|          25 | -0.37%   | 39.54%             | -14.25% |     0.05 |       60 | 50.25%     | ok               |
|          30 | -5.24%   | 39.54%             | -15.53% |    -0.12 |       63 | 47.75%     | ok               |
|          35 | -6.16%   | 39.54%             | -15.58% |    -0.17 |       61 | 44.59%     | ok               |

## SUSHI-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -29.69%  | -75.56%            | -40.53% |    -0.37 |       62 | 17.05%     | ok               |
|          35 | -50.68%  | -75.56%            | -68.95% |    -0.56 |       79 | 37.16%     | ok               |
|          15 | -61.40%  | -75.56%            | -78.43% |    -0.57 |       85 | 53.26%     | ok               |
|          20 | -58.74%  | -75.56%            | -76.66% |    -0.58 |       84 | 49.62%     | ok               |
|          25 | -58.15%  | -75.56%            | -76.33% |    -0.61 |       84 | 46.93%     | ok               |

## T Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 66.60%   | 20.98%             | -15.08% |     1.06 |       71 | 66.39%     | ok               |
|          25 | 62.97%   | 20.98%             | -17.66% |     1.06 |       66 | 59.57%     | ok               |
|          20 | 62.49%   | 20.98%             | -18.13% |     1.04 |       66 | 61.90%     | ok               |
|          30 | 52.21%   | 20.98%             | -17.01% |     0.94 |       68 | 57.57%     | ok               |
|          35 | 34.31%   | 20.98%             | -14.49% |     0.71 |       76 | 52.91%     | ok               |

## TGT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -8.89%   | 11.34%             | -32.83% |    -0.11 |       58 | 37.27%     | ok               |
|          25 | -10.70%  | 11.34%             | -34.49% |    -0.14 |       66 | 40.27%     | ok               |
|          20 | -13.69%  | 11.34%             | -36.76% |    -0.18 |       84 | 44.76%     | ok               |
|          45 | -12.30%  | 11.34%             | -26.12% |    -0.24 |       48 | 28.79%     | ok               |
|          15 | -19.64%  | 11.34%             | -36.20% |    -0.3  |       70 | 49.58%     | ok               |

## TIA-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -24.27%  | -80.78%            | -66.82% |     0.14 |       95 | 60.15%     | ok               |
|          20 | -41.10%  | -80.78%            | -71.78% |    -0.07 |       91 | 54.60%     | ok               |
|          25 | -39.30%  | -80.78%            | -70.91% |    -0.08 |       94 | 49.43%     | ok               |
|          35 | -34.56%  | -80.78%            | -67.14% |    -0.15 |       76 | 36.97%     | ok               |
|          30 | -50.23%  | -80.78%            | -78.90% |    -0.27 |       91 | 43.87%     | ok               |

## TLT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -7.29%   | -13.88%            | -12.00% |    -0.81 |       32 | 16.64%     | ok               |
|          40 | -13.43%  | -13.88%            | -17.65% |    -1.19 |       48 | 24.79%     | ok               |
|          45 | -11.45%  | -13.88%            | -14.68% |    -1.2  |       42 | 19.97%     | ok               |
|          30 | -20.96%  | -13.88%            | -22.01% |    -1.59 |       66 | 34.28%     | ok               |
|          35 | -19.97%  | -13.88%            | -21.03% |    -1.67 |       66 | 29.28%     | ok               |

## TMO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 50.73%   | 27.12%             | -8.17%  |     1.07 |       50 | 35.27%     | ok               |
|          45 | 49.68%   | 27.12%             | -9.69%  |     1    |       54 | 40.27%     | ok               |
|          40 | 42.51%   | 27.12%             | -11.54% |     0.87 |       59 | 45.42%     | ok               |
|          35 | 45.43%   | 27.12%             | -13.84% |     0.86 |       67 | 50.75%     | ok               |
|          20 | 42.89%   | 27.12%             | -22.89% |     0.77 |       74 | 62.56%     | ok               |

## TMUS Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -5.52%   | -2.59%             | -41.04% |     0    |       68 | 59.57%     | ok               |
|          30 | -6.80%   | -2.59%             | -33.05% |    -0.05 |       74 | 46.76%     | ok               |
|          25 | -9.44%   | -2.59%             | -39.29% |    -0.09 |       75 | 49.75%     | ok               |
|          20 | -10.97%  | -2.59%             | -39.79% |    -0.12 |       74 | 53.91%     | ok               |
|          50 | -9.75%   | -2.59%             | -32.38% |    -0.2  |       60 | 32.28%     | ok               |

## TRX-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 11.51%   | 10.21%             | -18.79% |     0.42 |       54 | 38.70%     | ok               |
|          50 | 3.84%    | 10.21%             | -22.22% |     0.2  |       44 | 32.95%     | ok               |
|          35 | 3.96%    | 10.21%             | -21.77% |     0.2  |       62 | 45.79%     | ok               |
|          45 | 3.11%    | 10.21%             | -24.19% |     0.18 |       48 | 35.06%     | ok               |
|          30 | 2.88%    | 10.21%             | -22.90% |     0.17 |       62 | 48.28%     | ok               |

## TSLA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 47.27%   | 113.56%            | -30.57% |     0.66 |       62 | 29.95%     | ok               |
|          40 | 18.38%   | 113.56%            | -50.11% |     0.38 |       61 | 35.44%     | ok               |
|          45 | -6.85%   | 113.56%            | -52.01% |     0.11 |       67 | 32.45%     | ok               |
|          35 | -17.25%  | 113.56%            | -60.12% |     0.01 |       74 | 37.94%     | ok               |
|          25 | -32.43%  | 113.56%            | -56.97% |    -0.18 |       72 | 45.26%     | ok               |

## TXN Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -2.53%   | 58.45%             | -43.95% |     0.09 |       70 | 31.61%     | ok               |
|          35 | -17.67%  | 58.45%             | -42.08% |    -0.15 |       84 | 45.42%     | ok               |
|          20 | -23.53%  | 58.45%             | -37.19% |    -0.19 |       74 | 55.24%     | ok               |
|          15 | -25.27%  | 58.45%             | -38.02% |    -0.21 |       79 | 59.57%     | ok               |
|          40 | -22.70%  | 58.45%             | -44.52% |    -0.25 |       78 | 42.93%     | ok               |

## UNH Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 36.14%   | -16.50%            | -26.31% |     0.58 |       75 | 48.75%     | ok               |
|          50 | 31.88%   | -16.50%            | -36.71% |     0.56 |       52 | 29.95%     | ok               |
|          35 | 32.60%   | -16.50%            | -27.21% |     0.55 |       68 | 43.93%     | ok               |
|          15 | 31.12%   | -16.50%            | -26.07% |     0.52 |       82 | 63.89%     | ok               |
|          20 | 28.73%   | -16.50%            | -26.96% |     0.5  |       77 | 57.57%     | ok               |

## UNI-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 80.67%   | -10.71%            | -22.21% |     0.87 |       46 | 25.48%     | ok               |
|          45 | 64.28%   | -10.71%            | -30.17% |     0.74 |       52 | 32.57%     | ok               |
|          40 | 48.20%   | -10.71%            | -43.84% |     0.63 |       60 | 38.70%     | ok               |
|          35 | 36.05%   | -10.71%            | -48.64% |     0.54 |       64 | 43.87%     | ok               |
|          20 | -17.07%  | -10.71%            | -68.99% |     0.15 |       86 | 58.05%     | ok               |

## UPS Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -16.60%  | -17.68%            | -25.52% |    -0.26 |       60 | 33.94%     | ok               |
|          50 | -15.14%  | -17.68%            | -24.11% |    -0.27 |       44 | 24.63%     | ok               |
|          20 | -27.13%  | -17.68%            | -34.48% |    -0.43 |       82 | 50.42%     | ok               |
|          15 | -29.52%  | -17.68%            | -36.63% |    -0.48 |       84 | 53.91%     | ok               |
|          35 | -27.62%  | -17.68%            | -32.02% |    -0.49 |       65 | 37.94%     | ok               |

## USO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 12.18%   | 79.87%             | -35.46% |     0.31 |       64 | 41.76%     | ok               |
|          20 | 7.01%    | 79.87%             | -38.90% |     0.25 |       68 | 38.27%     | ok               |
|          45 | 3.96%    | 79.87%             | -33.97% |     0.2  |       48 | 26.29%     | ok               |
|          25 | -2.76%   | 79.87%             | -41.21% |     0.11 |       68 | 36.27%     | ok               |
|          50 | -3.21%   | 79.87%             | -28.71% |     0.08 |       50 | 24.46%     | ok               |

## VEA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 2.17%    | 42.43%             | -17.27% |     0.14 |       58 | 49.92%     | ok               |
|          20 | -1.45%   | 42.43%             | -17.78% |    -0    |       59 | 47.42%     | ok               |
|          25 | -5.88%   | 42.43%             | -18.46% |    -0.19 |       59 | 45.26%     | ok               |
|          30 | -7.02%   | 42.43%             | -18.84% |    -0.25 |       64 | 41.26%     | ok               |
|          35 | -7.67%   | 42.43%             | -17.88% |    -0.29 |       50 | 38.77%     | ok               |

## VIXY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -54.55%  | -62.18%            | -69.78% |    -0.63 |       34 | 8.65%      | ok               |
|          45 | -64.29%  | -62.18%            | -75.03% |    -0.84 |       54 | 13.64%     | ok               |
|          40 | -71.97%  | -62.18%            | -80.72% |    -0.97 |       68 | 17.64%     | ok               |
|          35 | -78.91%  | -62.18%            | -84.48% |    -1.11 |       92 | 24.29%     | ok               |
|          30 | -83.33%  | -62.18%            | -90.81% |    -1.12 |       94 | 31.45%     | ok               |

## VNQ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -5.89%   | 15.54%             | -22.16% |    -0.18 |       69 | 43.43%     | ok               |
|          45 | -6.22%   | 15.54%             | -19.07% |    -0.24 |       60 | 28.62%     | ok               |
|          50 | -7.15%   | 15.54%             | -17.13% |    -0.3  |       52 | 25.29%     | ok               |
|          30 | -9.90%   | 15.54%             | -24.92% |    -0.36 |       71 | 40.43%     | ok               |
|          20 | -10.70%  | 15.54%             | -23.83% |    -0.37 |       74 | 46.09%     | ok               |

## VTI Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 5.74%    | 39.48%             | -13.96% |     0.25 |       63 | 51.75%     | ok               |
|          15 | -1.50%   | 39.48%             | -15.70% |     0.02 |       62 | 54.41%     | ok               |
|          25 | -4.76%   | 39.48%             | -15.00% |    -0.1  |       57 | 49.75%     | ok               |
|          40 | -8.94%   | 39.48%             | -19.77% |    -0.3  |       70 | 40.10%     | ok               |
|          35 | -10.94%  | 39.48%             | -20.22% |    -0.37 |       64 | 44.43%     | ok               |

## VWO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -7.41%   | 30.19%             | -21.18% |    -0.24 |       56 | 29.95%     | ok               |
|          45 | -9.22%   | 30.19%             | -23.26% |    -0.32 |       58 | 32.45%     | ok               |
|          15 | -11.34%  | 30.19%             | -24.01% |    -0.33 |       72 | 47.09%     | ok               |
|          40 | -10.07%  | 30.19%             | -23.57% |    -0.34 |       68 | 35.27%     | ok               |
|          20 | -11.36%  | 30.19%             | -26.14% |    -0.34 |       67 | 45.09%     | ok               |

## VZ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -2.64%   | 15.81%             | -12.55% |    -0.02 |       56 | 28.45%     | ok               |
|          20 | -21.86%  | 15.81%             | -35.02% |    -0.42 |       79 | 52.91%     | ok               |
|          25 | -18.67%  | 15.81%             | -26.32% |    -0.46 |       82 | 47.92%     | ok               |
|          35 | -18.88%  | 15.81%             | -26.97% |    -0.55 |       64 | 39.10%     | ok               |
|          45 | -18.61%  | 15.81%             | -26.23% |    -0.57 |       72 | 32.95%     | ok               |

## WFC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | -8.51%   | 47.68%             | -22.54% |    -0.11 |       77 | 42.76%     | ok               |
|          50 | -8.46%   | 47.68%             | -18.29% |    -0.21 |       58 | 32.28%     | ok               |
|          45 | -13.32%  | 47.68%             | -24.02% |    -0.33 |       64 | 36.27%     | ok               |
|          40 | -14.17%  | 47.68%             | -24.88% |    -0.34 |       72 | 39.43%     | ok               |
|          20 | -22.10%  | 47.68%             | -29.96% |    -0.35 |       80 | 52.75%     | ok               |

## WIF-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 48.31%   | -85.04%            | -40.67% |     0.61 |       67 | 49.23%     | ok               |
|          25 | 26.49%   | -85.04%            | -44.74% |     0.47 |       63 | 45.21%     | ok               |
|          15 | 15.90%   | -85.04%            | -46.21% |     0.41 |       77 | 52.49%     | ok               |
|          30 | -0.46%   | -85.04%            | -48.32% |     0.26 |       64 | 42.53%     | ok               |
|          35 | -5.18%   | -85.04%            | -52.54% |     0.17 |       60 | 36.59%     | ok               |

## WMT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 37.83%   | 85.05%             | -12.87% |     1.09 |       38 | 36.44%     | ok               |
|          45 | 36.85%   | 85.05%             | -14.82% |     1.02 |       44 | 38.94%     | ok               |
|          35 | 26.86%   | 85.05%             | -18.90% |     0.76 |       60 | 45.26%     | ok               |
|          40 | 25.23%   | 85.05%             | -19.17% |     0.74 |       52 | 40.60%     | ok               |
|          15 | 8.24%    | 85.05%             | -26.82% |     0.27 |       84 | 59.23%     | ok               |

## XBI Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 13.75%   | 69.20%             | -16.08% |     0.41 |       50 | 33.44%     | ok               |
|          45 | 9.43%    | 69.20%             | -15.46% |     0.32 |       48 | 30.95%     | ok               |
|          35 | 1.14%    | 69.20%             | -17.66% |     0.11 |       58 | 36.44%     | ok               |
|          50 | 0.20%    | 69.20%             | -15.41% |     0.08 |       48 | 27.95%     | ok               |
|          30 | -0.97%   | 69.20%             | -17.66% |     0.06 |       60 | 37.94%     | ok               |

## XLB Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 2.45%    | 18.30%             | -15.73% |     0.15 |       40 | 24.63%     | ok               |
|          40 | 2.13%    | 18.30%             | -17.29% |     0.14 |       54 | 28.95%     | ok               |
|          45 | -0.61%   | 18.30%             | -17.09% |     0.03 |       42 | 26.46%     | ok               |
|          35 | -1.61%   | 18.30%             | -20.65% |    -0    |       54 | 32.11%     | ok               |
|          25 | -5.14%   | 18.30%             | -21.62% |    -0.12 |       62 | 38.10%     | ok               |

## XLC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 4.97%    | 27.85%             | -12.33% |     0.23 |       61 | 49.42%     | ok               |
|          25 | 4.46%    | 27.85%             | -12.31% |     0.21 |       60 | 51.58%     | ok               |
|          20 | 3.88%    | 27.85%             | -11.04% |     0.19 |       63 | 54.08%     | ok               |
|          50 | 2.46%    | 27.85%             | -12.48% |     0.16 |       64 | 37.44%     | ok               |
|          40 | 0.48%    | 27.85%             | -13.38% |     0.08 |       62 | 43.09%     | ok               |

## XLE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -0.76%   | 41.21%             | -25.98% |     0.06 |       58 | 38.60%     | ok               |
|          45 | -2.44%   | 41.21%             | -28.46% |     0.01 |       60 | 41.10%     | ok               |
|          30 | -7.50%   | 41.21%             | -34.77% |    -0.11 |       68 | 47.25%     | ok               |
|          20 | -9.80%   | 41.21%             | -34.45% |    -0.14 |       79 | 52.41%     | ok               |
|          15 | -10.97%  | 41.21%             | -36.62% |    -0.16 |       95 | 56.41%     | ok               |

## XLF Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 7.30%    | 41.86%             | -20.19% |     0.29 |       70 | 56.74%     | ok               |
|          20 | 6.64%    | 41.86%             | -18.63% |     0.27 |       70 | 54.08%     | ok               |
|          25 | -0.80%   | 41.86%             | -23.22% |     0.04 |       77 | 50.92%     | ok               |
|          30 | -1.45%   | 41.86%             | -23.61% |     0.01 |       78 | 48.92%     | ok               |
|          35 | -9.52%   | 41.86%             | -24.48% |    -0.31 |       70 | 45.42%     | ok               |

## XLI Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 5.38%    | 39.03%             | -11.06% |     0.24 |       85 | 51.58%     | ok               |
|          20 | 0.03%    | 39.03%             | -12.74% |     0.06 |       77 | 46.59%     | ok               |
|          45 | -4.60%   | 39.03%             | -16.29% |    -0.16 |       70 | 33.94%     | ok               |
|          50 | -5.82%   | 39.03%             | -14.94% |    -0.23 |       62 | 31.45%     | ok               |
|          25 | -8.77%   | 39.03%             | -17.60% |    -0.29 |       78 | 44.43%     | ok               |

## XLK Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | 37.87%   | 52.67%             | -15.04% |     0.78 |       42 | 45.59%     | ok               |
|          20 | 38.19%   | 52.67%             | -19.58% |     0.76 |       52 | 47.92%     | ok               |
|          15 | 40.27%   | 52.67%             | -18.49% |     0.76 |       53 | 50.58%     | ok               |
|          30 | 29.62%   | 52.67%             | -19.07% |     0.67 |       42 | 44.26%     | ok               |
|          35 | 15.12%   | 52.67%             | -21.77% |     0.41 |       58 | 41.43%     | ok               |

## XLM-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | 11.54%   | -47.01%            | -51.61% |     0.34 |       75 | 52.11%     | ok               |
|          15 | 7.56%    | -47.01%            | -61.51% |     0.31 |       76 | 60.73%     | ok               |
|          30 | 2.54%    | -47.01%            | -54.74% |     0.25 |       75 | 49.43%     | ok               |
|          40 | 2.69%    | -47.01%            | -51.08% |     0.23 |       60 | 36.02%     | ok               |
|          50 | -0.33%   | -47.01%            | -46.76% |     0.18 |       42 | 23.37%     | ok               |

## XLP Threshold Sweep

|   threshold | return   | benchmark_return   | mdd    |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:-------|---------:|---------:|:-----------|:-----------------|
|          45 | 22.18%   | 17.74%             | -5.66% |     1.09 |       48 | 32.45%     | ok               |
|          50 | 19.30%   | 17.74%             | -6.08% |     0.99 |       54 | 30.62%     | ok               |
|          40 | 19.91%   | 17.74%             | -7.32% |     0.98 |       64 | 35.77%     | ok               |
|          35 | 18.43%   | 17.74%             | -8.39% |     0.9  |       62 | 38.60%     | ok               |
|          30 | 15.00%   | 17.74%             | -8.96% |     0.73 |       63 | 40.43%     | ok               |

## XLU Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 5.81%    | 26.30%             | -14.03% |     0.33 |       56 | 29.78%     | ok               |
|          45 | 4.65%    | 26.30%             | -14.97% |     0.27 |       60 | 30.95%     | ok               |
|          35 | 4.56%    | 26.30%             | -19.71% |     0.25 |       64 | 36.94%     | ok               |
|          40 | 2.10%    | 26.30%             | -16.41% |     0.14 |       70 | 33.61%     | ok               |
|          30 | 0.04%    | 26.30%             | -20.40% |     0.05 |       69 | 40.43%     | ok               |

## XLV Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -16.07%  | 28.70%             | -21.39% |    -0.7  |       72 | 36.77%     | ok               |
|          25 | -17.21%  | 28.70%             | -22.46% |    -0.74 |       74 | 38.77%     | ok               |
|          20 | -19.84%  | 28.70%             | -24.61% |    -0.86 |       77 | 40.27%     | ok               |
|          15 | -20.44%  | 28.70%             | -25.18% |    -0.87 |       83 | 42.60%     | ok               |
|          35 | -20.25%  | 28.70%             | -25.29% |    -0.95 |       66 | 33.78%     | ok               |

## XLY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 0.85%    | 32.51%             | -16.52% |     0.1  |       78 | 54.41%     | ok               |
|          30 | -2.65%   | 32.51%             | -18.44% |    -0.01 |       77 | 47.75%     | ok               |
|          20 | -4.48%   | 32.51%             | -20.14% |    -0.05 |       74 | 51.08%     | ok               |
|          25 | -6.61%   | 32.51%             | -21.01% |    -0.11 |       71 | 49.58%     | ok               |
|          50 | -5.79%   | 32.51%             | -17.00% |    -0.17 |       66 | 32.45%     | ok               |

## XOM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 3.48%    | 50.51%             | -21.35% |     0.17 |       40 | 29.28%     | ok               |
|          25 | 0.13%    | 50.51%             | -19.90% |     0.08 |       57 | 37.10%     | ok               |
|          30 | -0.86%   | 50.51%             | -20.29% |     0.06 |       57 | 36.44%     | ok               |
|          45 | -1.68%   | 50.51%             | -23.33% |     0.03 |       44 | 30.45%     | ok               |
|          40 | -3.14%   | 50.51%             | -21.45% |    -0.01 |       54 | 33.78%     | ok               |

## XRP-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 9.62%    | -55.24%            | -33.31% |     0.31 |       82 | 43.68%     | ok               |
|          40 | 1.61%    | -55.24%            | -32.16% |     0.21 |       74 | 35.82%     | ok               |
|          30 | -9.37%   | -55.24%            | -34.07% |     0.08 |       72 | 49.23%     | ok               |
|          45 | -8.09%   | -55.24%            | -33.74% |     0.07 |       66 | 29.69%     | ok               |
|          20 | -15.25%  | -55.24%            | -37.79% |     0.02 |       75 | 55.94%     | ok               |

## YFI-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -41.47%  | -64.91%            | -44.76% |    -0.64 |       58 | 27.59%     | ok               |
|          35 | -45.79%  | -64.91%            | -52.87% |    -0.68 |       60 | 35.63%     | ok               |
|          30 | -50.61%  | -64.91%            | -58.28% |    -0.77 |       72 | 39.46%     | ok               |
|          25 | -53.47%  | -64.91%            | -60.71% |    -0.81 |       71 | 43.87%     | ok               |
|          15 | -61.20%  | -64.91%            | -67.95% |    -0.95 |       81 | 52.30%     | ok               |

## ZEC-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 222.23%  | 1800.08%           | -30.64% |     1.13 |       44 | 28.93%     | ok               |
|          35 | 162.09%  | 1800.08%           | -50.84% |     0.97 |       52 | 34.10%     | ok               |
|          50 | 146.25%  | 1800.08%           | -41.34% |     0.95 |       44 | 26.05%     | ok               |
|          40 | 138.59%  | 1800.08%           | -54.22% |     0.91 |       52 | 32.38%     | ok               |
|          30 | 126.43%  | 1800.08%           | -56.50% |     0.87 |       54 | 36.97%     | ok               |
