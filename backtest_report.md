# Market Tracker Backtest Report

_Generated: 2026-07-17T03:43:10+00:00_

## Data Sources

- Crypto: Kraken -> Coinbase -> CoinGecko OHLC -> CoinPaprika fallback chain.
- Stocks / ETFs / indices: Stooq -> Yahoo Finance fallback chain.
- Data rows are generated from real market APIs. Mock OHLCV rows are not generated.

## Data Freshness

- Rows: **92,510**
- Symbols: **161**
- Date range: **2024-02-22** to **2026-07-17**

## Latest Signals

| symbol     | date                |         close |   composite_score | signal   | data_source   |
|:-----------|:--------------------|--------------:|------------------:|:---------|:--------------|
| AAPL       | 2026-07-16 00:00:00 |   333.26      |          53.25    | LONG     | Yahoo Finance |
| ABBV       | 2026-07-16 00:00:00 |   254.39      |          34.8333  | LONG     | Yahoo Finance |
| AMZN       | 2026-07-16 00:00:00 |   249.89      |          68.25    | LONG     | Yahoo Finance |
| ARB-USD    | 2026-07-17 00:00:00 |     0.0906    |          48.6667  | LONG     | Kraken API    |
| BAC        | 2026-07-16 00:00:00 |    61.49      |          49.0833  | LONG     | Yahoo Finance |
| CMCSA      | 2026-07-16 00:00:00 |    24.1       |          31.9167  | LONG     | Yahoo Finance |
| COP        | 2026-07-16 00:00:00 |   112.84      |          53.6667  | LONG     | Yahoo Finance |
| CRV-USD    | 2026-07-17 00:00:00 |     0.21414   |          47       | LONG     | Kraken API    |
| CVX        | 2026-07-16 00:00:00 |   183.86      |          73.6667  | LONG     | Yahoo Finance |
| DBC        | 2026-07-16 00:00:00 |    28.46      |          66.9167  | LONG     | Yahoo Finance |
| DE         | 2026-07-16 00:00:00 |   598.97      |          36.9167  | LONG     | Yahoo Finance |
| DIA        | 2026-07-16 00:00:00 |   524.83      |          43.0833  | LONG     | Yahoo Finance |
| EOG        | 2026-07-16 00:00:00 |   138.46      |          72.3333  | LONG     | Yahoo Finance |
| ETH-USD    | 2026-07-17 00:00:00 |  1856.75      |          48.8333  | LONG     | Kraken API    |
| JPM        | 2026-07-16 00:00:00 |   343.15      |          41.0833  | LONG     | Yahoo Finance |
| KO         | 2026-07-16 00:00:00 |    84.92      |          75.75    | LONG     | Yahoo Finance |
| LDO-USD    | 2026-07-17 00:00:00 |     0.37      |          50.75    | LONG     | Kraken API    |
| LINK-USD   | 2026-07-17 00:00:00 |     8.31835   |          50.6667  | LONG     | Kraken API    |
| LTC-USD    | 2026-07-17 00:00:00 |    45.8       |          53.1667  | LONG     | Kraken API    |
| META       | 2026-07-16 00:00:00 |   664.54      |          57.75    | LONG     | Yahoo Finance |
| MPC        | 2026-07-16 00:00:00 |   305.85      |          73.75    | LONG     | Yahoo Finance |
| MRK        | 2026-07-16 00:00:00 |   127.63      |          54.5833  | LONG     | Yahoo Finance |
| NVDA       | 2026-07-16 00:00:00 |   207.4       |          57.3333  | LONG     | Yahoo Finance |
| OXY        | 2026-07-16 00:00:00 |    53.65      |          51.1667  | LONG     | Yahoo Finance |
| POL-USD    | 2026-07-17 00:00:00 |     0.08243   |          47.3333  | LONG     | Kraken API    |
| RTX        | 2026-07-16 00:00:00 |   194.36      |          42.8333  | LONG     | Yahoo Finance |
| SCHW       | 2026-07-16 00:00:00 |   102.8       |          61.75    | LONG     | Yahoo Finance |
| TMO        | 2026-07-16 00:00:00 |   543.19      |          64.3333  | LONG     | Yahoo Finance |
| UNH        | 2026-07-16 00:00:00 |   423.38      |          43.3333  | LONG     | Yahoo Finance |
| UNI-USD    | 2026-07-17 00:00:00 |     3.5666    |          46.6667  | LONG     | Kraken API    |
| USO        | 2026-07-16 00:00:00 |   119.3       |          51.1667  | LONG     | Yahoo Finance |
| WFC        | 2026-07-16 00:00:00 |    88.07      |          63.8333  | LONG     | Yahoo Finance |
| XLE        | 2026-07-16 00:00:00 |    57.02      |          76.0833  | LONG     | Yahoo Finance |
| XLF        | 2026-07-16 00:00:00 |    56.75      |          63.75    | LONG     | Yahoo Finance |
| XLV        | 2026-07-16 00:00:00 |   161.8       |          50.9167  | LONG     | Yahoo Finance |
| XOM        | 2026-07-16 00:00:00 |   145.95      |          71.6667  | LONG     | Yahoo Finance |
| YFI-USD    | 2026-07-17 00:00:00 |  2164.3       |          44.9167  | LONG     | Kraken API    |
| ZEC-USD    | 2026-07-17 00:00:00 |   538.2       |          69.1667  | LONG     | Kraken API    |
| AAVE-USD   | 2026-07-17 00:00:00 |    91.17      |          17.8333  | NEUTRAL  | Kraken API    |
| ADA-USD    | 2026-07-17 00:00:00 |     0.161063  |         -27.6667  | NEUTRAL  | Kraken API    |
| ADBE       | 2026-07-16 00:00:00 |   235.31      |          24.25    | NEUTRAL  | Yahoo Finance |
| ALGO-USD   | 2026-07-17 00:00:00 |     0.08266   |         -38.25    | NEUTRAL  | Kraken API    |
| AMAT       | 2026-07-16 00:00:00 |   560.93      |          -2.83333 | NEUTRAL  | Yahoo Finance |
| AMD        | 2026-07-16 00:00:00 |   500.94      |           1.16667 | NEUTRAL  | Yahoo Finance |
| AMGN       | 2026-07-16 00:00:00 |   371.58      |          39.3333  | NEUTRAL  | Yahoo Finance |
| APT-USD    | 2026-07-17 00:00:00 |     0.6137    |         -20.4167  | NEUTRAL  | Kraken API    |
| ARKK       | 2026-07-16 00:00:00 |    76.67      |         -11.5833  | NEUTRAL  | Yahoo Finance |
| ATOM-USD   | 2026-07-17 00:00:00 |     1.5089    |         -20.3333  | NEUTRAL  | Kraken API    |
| AVAX-USD   | 2026-07-17 00:00:00 |     6.547     |         -23.6667  | NEUTRAL  | Kraken API    |
| AVGO       | 2026-07-16 00:00:00 |   374.45      |         -15.9167  | NEUTRAL  | Yahoo Finance |
| BA         | 2026-07-16 00:00:00 |   214.34      |         -65.75    | NEUTRAL  | Yahoo Finance |
| BITO       | 2026-07-16 00:00:00 |     8.72      |          12.1667  | NEUTRAL  | Yahoo Finance |
| BLK        | 2026-07-16 00:00:00 |  1087.05      |          39.5     | NEUTRAL  | Yahoo Finance |
| BONK-USD   | 2026-07-17 00:00:00 |     3.381e-06 |         -59.5833  | NEUTRAL  | Kraken API    |
| BTC-USD    | 2026-07-17 00:00:00 | 63648.7       |          13.9167  | NEUTRAL  | Kraken API    |
| C          | 2026-07-16 00:00:00 |   131.71      |          -5.41667 | NEUTRAL  | Yahoo Finance |
| CAT        | 2026-07-16 00:00:00 |   877.17      |         -34.3333  | NEUTRAL  | Yahoo Finance |
| CL         | 2026-07-16 00:00:00 |    94.07      |          45       | NEUTRAL  | Yahoo Finance |
| COMP-USD   | 2026-07-17 00:00:00 |    17.22      |          26       | NEUTRAL  | Kraken API    |
| COST       | 2026-07-16 00:00:00 |   945.57      |          15.4167  | NEUTRAL  | Yahoo Finance |
| CRM        | 2026-07-16 00:00:00 |   172.68      |           8.33333 | NEUTRAL  | Yahoo Finance |
| CSCO       | 2026-07-16 00:00:00 |   109.66      |         -12.25    | NEUTRAL  | Yahoo Finance |
| DASH-USD   | 2026-07-17 00:00:00 |    33.631     |         -43.9167  | NEUTRAL  | Kraken API    |
| DIS        | 2026-07-16 00:00:00 |    99.71      |         -15.3333  | NEUTRAL  | Yahoo Finance |
| DOGE-USD   | 2026-07-17 00:00:00 |     0.0725195 |         -34.9167  | NEUTRAL  | Kraken API    |
| DOT-USD    | 2026-07-17 00:00:00 |     0.865     |          21.3333  | NEUTRAL  | Kraken API    |
| DXY-INDEX  | 2026-07-16 00:00:00 |   100.761     |          28.4946  | NEUTRAL  | Yahoo Finance |
| EEM        | 2026-07-16 00:00:00 |    64.19      |         -12.3333  | NEUTRAL  | Yahoo Finance |
| EFA        | 2026-07-16 00:00:00 |   103.81      |          26.6667  | NEUTRAL  | Yahoo Finance |
| ETC-USD    | 2026-07-17 00:00:00 |     6.94      |         -25.9167  | NEUTRAL  | Kraken API    |
| EWJ        | 2026-07-16 00:00:00 |    91.91      |         -18.6667  | NEUTRAL  | Yahoo Finance |
| FCX        | 2026-07-16 00:00:00 |    58.56      |          -9       | NEUTRAL  | Yahoo Finance |
| FIL-USD    | 2026-07-17 00:00:00 |     0.769     |         -22.4167  | NEUTRAL  | Kraken API    |
| FXI        | 2026-07-16 00:00:00 |    34.53      |          21.5833  | NEUTRAL  | Yahoo Finance |
| GDX        | 2026-07-16 00:00:00 |    71.4       |         -64.5     | NEUTRAL  | Yahoo Finance |
| GDXJ       | 2026-07-16 00:00:00 |    92.65      |         -60       | NEUTRAL  | Yahoo Finance |
| GE         | 2026-07-16 00:00:00 |   345.73      |          -2.08333 | NEUTRAL  | Yahoo Finance |
| GOOGL      | 2026-07-16 00:00:00 |   354.46      |          -2       | NEUTRAL  | Yahoo Finance |
| GRT-USD    | 2026-07-17 00:00:00 |     0.01728   |         -29.25    | NEUTRAL  | Kraken API    |
| GS         | 2026-07-16 00:00:00 |  1095.46      |          63.1667  | NEUTRAL  | Yahoo Finance |
| HBAR-USD   | 2026-07-17 00:00:00 |     0.06655   |         -48.25    | NEUTRAL  | Kraken API    |
| HD         | 2026-07-16 00:00:00 |   348.02      |          13.3333  | NEUTRAL  | Yahoo Finance |
| HON        | 2026-07-16 00:00:00 |   226.33      |         -51       | NEUTRAL  | Yahoo Finance |
| HYG        | 2026-07-16 00:00:00 |    79.8       |         -21.75    | NEUTRAL  | Yahoo Finance |
| IBIT       | 2026-07-16 00:00:00 |    36.39      |         -11.0833  | NEUTRAL  | Yahoo Finance |
| ICP-USD    | 2026-07-17 00:00:00 |     2.137     |         -48.25    | NEUTRAL  | Kraken API    |
| IEMG       | 2026-07-16 00:00:00 |    78.11      |         -12.3333  | NEUTRAL  | Yahoo Finance |
| INJ-USD    | 2026-07-17 00:00:00 |     4.88      |          25.5     | NEUTRAL  | Kraken API    |
| INTC       | 2026-07-16 00:00:00 |    96.98      |         -25.3333  | NEUTRAL  | Yahoo Finance |
| INTU       | 2026-07-16 00:00:00 |   294.79      |          -9.66667 | NEUTRAL  | Yahoo Finance |
| ITA        | 2026-07-16 00:00:00 |   230.89      |         -18.0833  | NEUTRAL  | Yahoo Finance |
| IWM        | 2026-07-16 00:00:00 |   295.59      |          18.1667  | NEUTRAL  | Yahoo Finance |
| JNJ        | 2026-07-16 00:00:00 |   249.97      |          18.0833  | NEUTRAL  | Yahoo Finance |
| LIN        | 2026-07-16 00:00:00 |   520.74      |           7.66667 | NEUTRAL  | Yahoo Finance |
| LLY        | 2026-07-16 00:00:00 |  1169.17      |          25.1667  | NEUTRAL  | Yahoo Finance |
| LRCX       | 2026-07-16 00:00:00 |   320.96      |         -32.75    | NEUTRAL  | Yahoo Finance |
| MCD        | 2026-07-16 00:00:00 |   273.46      |         -32.1667  | NEUTRAL  | Yahoo Finance |
| MS         | 2026-07-16 00:00:00 |   218.37      |           6.33333 | NEUTRAL  | Yahoo Finance |
| MSFT       | 2026-07-16 00:00:00 |   401.1       |           8.33333 | NEUTRAL  | Yahoo Finance |
| MU         | 2026-07-16 00:00:00 |   853.2       |         -40.3333  | NEUTRAL  | Yahoo Finance |
| NEAR-USD   | 2026-07-17 00:00:00 |     1.9988    |          45.8333  | NEUTRAL  | Kraken API    |
| NEM        | 2026-07-16 00:00:00 |    90.83      |         -46.6667  | NEUTRAL  | Yahoo Finance |
| NFLX       | 2026-07-16 00:00:00 |    74.35      |         -17.0833  | NEUTRAL  | Yahoo Finance |
| NKE        | 2026-07-16 00:00:00 |    44.57      |          18.9167  | NEUTRAL  | Yahoo Finance |
| NOW        | 2026-07-16 00:00:00 |   104.01      |           6.58333 | NEUTRAL  | Yahoo Finance |
| OP-USD     | 2026-07-17 00:00:00 |     0.0984    |         -41.25    | NEUTRAL  | Kraken API    |
| PEP        | 2026-07-16 00:00:00 |   139.43      |         -55.3333  | NEUTRAL  | Yahoo Finance |
| PEPE-USD   | 2026-07-17 00:00:00 |     2.756e-06 |          22.3333  | NEUTRAL  | Kraken API    |
| PFE        | 2026-07-16 00:00:00 |    25.14      |           4.91667 | NEUTRAL  | Yahoo Finance |
| PG         | 2026-07-16 00:00:00 |   151.5       |          42.9167  | NEUTRAL  | Yahoo Finance |
| PM         | 2026-07-16 00:00:00 |   189.84      |          63.3333  | NEUTRAL  | Yahoo Finance |
| QCOM       | 2026-07-16 00:00:00 |   170.61      |         -63.3333  | NEUTRAL  | Yahoo Finance |
| QQQ        | 2026-07-16 00:00:00 |   705.94      |         -24       | NEUTRAL  | Yahoo Finance |
| RENDER-USD | 2026-07-17 00:00:00 |     1.49      |         -38.25    | NEUTRAL  | Kraken API    |
| SBUX       | 2026-07-16 00:00:00 |   108.37      |          58.3333  | NEUTRAL  | Yahoo Finance |
| SHIB-USD   | 2026-07-17 00:00:00 |     4.153e-06 |         -25.9167  | NEUTRAL  | Kraken API    |
| SHY        | 2026-07-16 00:00:00 |    82         |         -21.75    | NEUTRAL  | Yahoo Finance |
| SKY-USD    | 2026-07-17 00:00:00 |     0.06135   |          28.6667  | NEUTRAL  | Kraken API    |
| SLB        | 2026-07-16 00:00:00 |    47.08      |          -5.75    | NEUTRAL  | Yahoo Finance |
| SMH        | 2026-07-16 00:00:00 |   568.92      |         -31       | NEUTRAL  | Yahoo Finance |
| SNX-USD    | 2026-07-17 00:00:00 |     0.2286    |         -25.9167  | NEUTRAL  | Kraken API    |
| SOXX       | 2026-07-16 00:00:00 |   530.5       |         -31       | NEUTRAL  | Yahoo Finance |
| SPY        | 2026-07-16 00:00:00 |   750.72      |          55.1667  | NEUTRAL  | Yahoo Finance |
| SUSHI-USD  | 2026-07-17 00:00:00 |     0.1651    |          26       | NEUTRAL  | Kraken API    |
| T          | 2026-07-16 00:00:00 |    21.98      |         -12.5833  | NEUTRAL  | Yahoo Finance |
| TGT        | 2026-07-16 00:00:00 |   140.21      |          50.3333  | NEUTRAL  | Yahoo Finance |
| TIA-USD    | 2026-07-17 00:00:00 |     0.3827    |         -20.0833  | NEUTRAL  | Kraken API    |
| TMUS       | 2026-07-16 00:00:00 |   192.85      |          31.0833  | NEUTRAL  | Yahoo Finance |
| TRX-USD    | 2026-07-17 00:00:00 |     0.321897  |           0.5     | NEUTRAL  | Kraken API    |
| TSLA       | 2026-07-16 00:00:00 |   391.06      |         -41.5833  | NEUTRAL  | Yahoo Finance |
| TXN        | 2026-07-16 00:00:00 |   291.22      |         -22.6667  | NEUTRAL  | Yahoo Finance |
| UPS        | 2026-07-16 00:00:00 |   117.18      |          64.5     | NEUTRAL  | Yahoo Finance |
| VEA        | 2026-07-16 00:00:00 |    70.03      |         -23.3333  | NEUTRAL  | Yahoo Finance |
| VIXY       | 2026-07-16 00:00:00 |    20.56      |         -29       | NEUTRAL  | Yahoo Finance |
| VNQ        | 2026-07-16 00:00:00 |   100.07      |          67.3333  | NEUTRAL  | Yahoo Finance |
| VTI        | 2026-07-16 00:00:00 |   370.58      |          62.6667  | NEUTRAL  | Yahoo Finance |
| VWO        | 2026-07-16 00:00:00 |    58.84      |         -31.3333  | NEUTRAL  | Yahoo Finance |
| VZ         | 2026-07-16 00:00:00 |    43.88      |          -1.5     | NEUTRAL  | Yahoo Finance |
| WMT        | 2026-07-16 00:00:00 |   114.95      |          -5.5     | NEUTRAL  | Yahoo Finance |
| XBI        | 2026-07-16 00:00:00 |   152         |          22.5833  | NEUTRAL  | Yahoo Finance |
| XLB        | 2026-07-16 00:00:00 |    50.89      |         -20.3333  | NEUTRAL  | Yahoo Finance |
| XLC        | 2026-07-16 00:00:00 |   112.65      |          45.25    | NEUTRAL  | Yahoo Finance |
| XLI        | 2026-07-16 00:00:00 |   180.15      |          11.1667  | NEUTRAL  | Yahoo Finance |
| XLK        | 2026-07-16 00:00:00 |   177.52      |         -27.3333  | NEUTRAL  | Yahoo Finance |
| XLM-USD    | 2026-07-17 00:00:00 |     0.184643  |         -59.25    | NEUTRAL  | Kraken API    |
| XLP        | 2026-07-16 00:00:00 |    85.81      |          64       | NEUTRAL  | Yahoo Finance |
| XLU        | 2026-07-16 00:00:00 |    45.47      |          18.4167  | NEUTRAL  | Yahoo Finance |
| XLY        | 2026-07-16 00:00:00 |   117.34      |          48.8333  | NEUTRAL  | Yahoo Finance |
| XRP-USD    | 2026-07-17 00:00:00 |     1.09343   |         -25.9167  | NEUTRAL  | Kraken API    |
| AGG        | 2026-07-16 00:00:00 |    98.13      |         -49.25    | SHORT    | Yahoo Finance |
| BCH-USD    | 2026-07-17 00:00:00 |   223.47      |         -33.8333  | SHORT    | Kraken API    |
| BND        | 2026-07-16 00:00:00 |    72.81      |         -49.25    | SHORT    | Yahoo Finance |
| FET-USD    | 2026-07-17 00:00:00 |     0.1581    |         -36       | SHORT    | Kraken API    |
| GLD        | 2026-07-16 00:00:00 |   364.96      |         -33.4167  | SHORT    | Yahoo Finance |
| IBM        | 2026-07-16 00:00:00 |   219.05      |         -53.6667  | SHORT    | Yahoo Finance |
| IEF        | 2026-07-16 00:00:00 |    93.72      |         -49.25    | SHORT    | Yahoo Finance |
| ORCL       | 2026-07-16 00:00:00 |   124.21      |         -54.4167  | SHORT    | Yahoo Finance |
| SLV        | 2026-07-16 00:00:00 |    50.39      |         -35.4167  | SHORT    | Yahoo Finance |
| SOL-USD    | 2026-07-17 00:00:00 |    75.33      |         -33.6667  | SHORT    | Kraken API    |
| TLT        | 2026-07-16 00:00:00 |    84.21      |         -54.5833  | SHORT    | Yahoo Finance |
| WIF-USD    | 2026-07-17 00:00:00 |     0.1526    |         -40.3333  | SHORT    | Kraken API    |

## Edge Summary

- Symbols with trades: **160** of 160
- Beat buy-and-hold: **31.87%** of traded symbols
- Positive return: **28.75%** of traded symbols
- Median strategy return: **-10.75%** (benchmark **15.80%**)
- Median excess vs benchmark: **-26.94%**
- Median Sharpe: **-0.12**
- Median exposure: **44.26%**

> Edge is real only if both _beat buy-and-hold_ and _median excess_ are convincingly positive across many symbols. Treat a single high-return symbol as noise.

## Portfolio Backtest

Actual capital-allocation books (not per-symbol averages). Benchmarks: `equal_weight_buyhold` (whole tracked universe), `spy_buyhold` (100% SPY), and `sixty_forty` (60% SPY / 40% AGG). `high_conf_voltarget` inverse-vol-weights the HIGH-confidence book; `conviction_long_short` is market-neutral. Judge on **Sharpe** and **max_drawdown** out-of-sample, not raw return: a fully-invested long book wins on return in a bull market but carries all the risk.

| strategy              | scope         | ann_return   | ann_vol   |   sharpe | max_drawdown   | total_return   |   avg_gross_exposure |
|:----------------------|:--------------|:-------------|:----------|---------:|:---------------|:---------------|---------------------:|
| equal_weight_buyhold  | full          | -4.03%       | 32.48%    |    -0.12 | -47.00%        | -24.75%        |                 1    |
| equal_weight_buyhold  | out_of_sample | -20.91%      | 31.05%    |    -0.67 | -39.63%        | -24.04%        |                 1    |
| all_signals_ew        | full          | -19.22%      | 27.17%    |    -0.71 | -63.50%        | -50.27%        |                 1    |
| all_signals_ew        | out_of_sample | 20.79%       | 26.67%    |     0.78 | -18.25%        | 20.25%         |                 1    |
| high_conf_ew          | full          | -0.09%       | 31.53%    |    -0    | -44.15%        | -14.12%        |                 0.88 |
| high_conf_ew          | out_of_sample | 20.35%       | 33.84%    |     0.6  | -17.35%        | 17.10%         |                 0.88 |
| high_conf_voltarget   | full          | 2.46%        | 29.11%    |     0.08 | -36.24%        | -5.04%         |                 0.88 |
| high_conf_voltarget   | out_of_sample | 15.48%       | 31.33%    |     0.49 | -16.94%        | 12.14%         |                 0.88 |
| conviction_long_short | full          | -20.73%      | 23.05%    |    -0.9  | -51.88%        | -50.94%        |                 0.97 |
| conviction_long_short | out_of_sample | -13.02%      | 26.26%    |    -0.5  | -23.88%        | -16.14%        |                 0.97 |
| spy_buyhold           | full          | 6.24%        | 13.32%    |     0.47 | -17.80%        | 17.70%         |                 0.79 |
| spy_buyhold           | out_of_sample | -1.26%       | 9.78%     |    -0.13 | -13.27%        | -1.84%         |                 0.79 |
| sixty_forty           | full          | 3.77%        | 8.43%     |     0.45 | -10.77%        | 10.94%         |                 0.79 |
| sixty_forty           | out_of_sample | -2.16%       | 6.46%     |    -0.33 | -9.26%         | -2.49%         |                 0.79 |

## Walk-Forward Robustness

Each book measured across contiguous time folds (each a different regime). A book has durable edge only if `mean_sharpe` is positive, `min_sharpe` isn't deeply negative, and `pct_positive_folds` is high — a single great fold doesn't count. `fold_sharpes` lists each fold oldest-to-newest.

| strategy              |   n_folds |   mean_sharpe |   median_sharpe |   min_sharpe | pct_positive_folds   | mean_return   | fold_sharpes                 |
|:----------------------|----------:|--------------:|----------------:|-------------:|:---------------------|:--------------|:-----------------------------|
| equal_weight_buyhold  |         5 |          0.23 |            0.29 |        -1.47 | 60.00%               | -2.33%        | 1.70;-1.47;1.56;-0.94;0.29   |
| all_signals_ew        |         5 |         -0.73 |           -0.42 |        -2.37 | 20.00%               | -12.12%       | -0.26;-0.42;-2.37;0.01;-0.64 |
| high_conf_ew          |         5 |          0.1  |           -0.35 |        -0.6  | 40.00%               | -2.41%        | 1.21;-0.35;-0.60;0.62;-0.38  |
| high_conf_voltarget   |         5 |          0.29 |           -0.04 |        -0.61 | 40.00%               | -0.48%        | 1.99;-0.04;-0.61;0.58;-0.46  |
| conviction_long_short |         5 |         -1.06 |           -1.57 |        -1.69 | 20.00%               | -12.94%       | -1.64;-1.57;-0.58;0.19;-1.69 |
| spy_buyhold           |         5 |          0.59 |            0.2  |        -1.12 | 60.00%               | 3.63%         | 1.53;-0.18;2.55;-1.12;0.20   |
| sixty_forty           |         5 |          0.57 |           -0.18 |        -1.09 | 40.00%               | 2.26%         | 1.76;-0.32;2.70;-1.09;-0.18  |

## Strategy Comparison

Each decision rule backtested over the same data. `out_of_sample` is the most recent ~35% of each symbol's history (unseen tail). A rule has real edge only if `median_excess` and `beat_benchmark_pct` stay positive out-of-sample, not just full-sample.

| strategy        | scope         |   symbols | beat_benchmark_pct   | positive_pct   | median_return   | median_benchmark   | median_excess   |   median_sharpe |   total_trades |
|:----------------|:--------------|----------:|:---------------------|:---------------|:----------------|:-------------------|:----------------|----------------:|---------------:|
| trend           | full          |       160 | 31.87%               | 28.75%         | -10.75%         | 15.80%             | -26.94%         |           -0.12 |          11238 |
| trend           | out_of_sample |       160 | 41.88%               | 52.50%         | 0.74%           | 3.51%              | -4.83%          |            0.26 |           3773 |
| mean_reversion  | full          |       157 | 40.13%               | 51.59%         | 0.09%           | 15.10%             | -15.95%         |            0.04 |           1260 |
| mean_reversion  | out_of_sample |       124 | 50.00%               | 59.68%         | 0.38%           | -1.34%             | 0.42%           |            0.58 |            422 |
| regime_adaptive | full          |       160 | 33.12%               | 30.63%         | -10.83%         | 15.80%             | -27.35%         |           -0.12 |          11513 |
| regime_adaptive | out_of_sample |       160 | 41.88%               | 54.37%         | 1.32%           | 3.51%              | -4.36%          |            0.26 |           3874 |

## Signal Calibration

Realized forward return in the signal's direction, grouped by confidence. HIGH should outrank LOW for the confidence score to be meaningful.

| confidence_level   |   horizon |     n | mean_return   | median_return   | win_rate   |
|:-------------------|----------:|------:|:--------------|:----------------|:-----------|
| HIGH               |         5 |  7946 | 0.10%         | 0.10%           | 51.65%     |
| MEDIUM             |         5 | 29138 | 0.02%         | 0.07%           | 50.79%     |
| LOW                |         5 |  3357 | -0.62%        | -0.54%          | 44.65%     |
| ALL                |         5 | 40441 | -0.02%        | 0.04%           | 50.45%     |
| HIGH               |        10 |  7912 | 0.37%         | 0.10%           | 51.20%     |
| MEDIUM             |        10 | 28947 | 0.16%         | 0.11%           | 50.89%     |
| LOW                |        10 |  3308 | -0.92%        | -0.73%          | 45.22%     |
| ALL                |        10 | 40167 | 0.11%         | 0.06%           | 50.48%     |
| HIGH               |        20 |  7820 | 0.77%         | 0.35%           | 52.90%     |
| MEDIUM             |        20 | 28566 | 0.83%         | 0.61%           | 53.48%     |
| LOW                |        20 |  3244 | -0.69%        | -0.50%          | 47.26%     |
| ALL                |        20 | 39630 | 0.70%         | 0.48%           | 52.85%     |

## Backtest Summary

### Data Quality / Signal Availability

- **ok**: 160 symbols

| symbol     |   trades | return   | benchmark_return   | mdd     |   sharpe | exposure   | skipped_reason   |
|:-----------|---------:|:---------|:-------------------|:--------|---------:|:-----------|:-----------------|
| AAPL       |       61 | 20.64%   | 80.76%             | -20.65% |     0.49 | 49.08%     | ok               |
| AAVE-USD   |       74 | -50.73%  | -62.62%            | -68.26% |    -0.46 | 39.46%     | ok               |
| ABBV       |       66 | -19.07%  | 43.93%             | -30.55% |    -0.39 | 47.25%     | ok               |
| ADA-USD    |       88 | -83.94%  | -79.30%            | -89.69% |    -0.71 | 46.74%     | ok               |
| ADBE       |       64 | -30.20%  | -56.23%            | -35.81% |    -0.38 | 57.40%     | ok               |
| AGG        |       69 | -6.80%   | 1.19%              | -9.97%  |    -1.13 | 31.45%     | ok               |
| ALGO-USD   |       86 | -50.43%  | -71.10%            | -53.13% |    -0.57 | 38.12%     | ok               |
| AMAT       |       71 | -34.41%  | 180.84%            | -57.21% |    -0.31 | 52.41%     | ok               |
| AMD        |       52 | 5.86%    | 175.45%            | -43.98% |     0.27 | 35.77%     | ok               |
| AMGN       |       69 | -15.41%  | 30.30%             | -34.14% |    -0.29 | 46.26%     | ok               |
| AMZN       |       80 | -36.92%  | 43.14%             | -42.48% |    -1.11 | 38.27%     | ok               |
| APT-USD    |       74 | -42.76%  | -89.57%            | -69.96% |    -0.26 | 42.15%     | ok               |
| ARB-USD    |       70 | -23.62%  | -80.45%            | -62.34% |    -0.04 | 38.89%     | ok               |
| ARKK       |       81 | -32.60%  | 58.15%             | -34.15% |    -0.56 | 39.60%     | ok               |
| ATOM-USD   |       90 | -70.24%  | -67.93%            | -74.37% |    -1.23 | 44.83%     | ok               |
| AVAX-USD   |       68 | -30.01%  | -74.21%            | -53.72% |    -0.21 | 38.12%     | ok               |
| AVGO       |       64 | 14.37%   | 186.96%            | -35.76% |     0.33 | 42.76%     | ok               |
| BA         |       67 | 7.60%    | 6.37%              | -30.56% |     0.25 | 49.25%     | ok               |
| BAC        |       78 | -6.13%   | 82.95%             | -26.91% |    -0.08 | 49.75%     | ok               |
| BCH-USD    |       76 | -2.55%   | -32.56%            | -53.87% |     0.18 | 48.28%     | ok               |
| BITO       |       80 | -1.36%   | -64.55%            | -42.82% |     0.16 | 41.43%     | ok               |
| BLK        |       71 | -7.59%   | 33.64%             | -24.29% |    -0.16 | 42.43%     | ok               |
| BND        |       67 | -7.74%   | 1.24%              | -9.93%  |    -1.25 | 32.78%     | ok               |
| BONK-USD   |       72 | 45.25%   | -80.83%            | -45.22% |     0.6  | 41.57%     | ok               |
| BTC-USD    |       75 | -1.45%   | -33.54%            | -23.64% |     0.13 | 53.07%     | ok               |
| C          |       81 | -30.58%  | 135.62%            | -38.11% |    -0.61 | 51.25%     | ok               |
| CAT        |       72 | 22.49%   | 172.34%            | -21.02% |     0.46 | 55.91%     | ok               |
| CL         |       62 | 7.91%    | 9.38%              | -14.32% |     0.31 | 45.92%     | ok               |
| CMCSA      |       79 | -38.98%  | -38.64%            | -40.26% |    -1.03 | 42.10%     | ok               |
| COMP-USD   |       91 | -45.09%  | -69.18%            | -57.88% |    -0.35 | 46.17%     | ok               |
| COP        |       72 | -23.58%  | 0.55%              | -43.96% |    -0.43 | 41.76%     | ok               |
| COST       |       60 | -1.21%   | 28.75%             | -29.73% |     0.03 | 43.59%     | ok               |
| CRM        |       63 | -39.56%  | -41.20%            | -41.36% |    -0.83 | 42.76%     | ok               |
| CRV-USD    |       68 | -6.45%   | -59.75%            | -39.89% |     0.17 | 36.21%     | ok               |
| CSCO       |       61 | 22.88%   | 125.78%            | -21.79% |     0.5  | 49.08%     | ok               |
| CVX        |       75 | -17.67%  | 18.29%             | -29.13% |    -0.46 | 39.93%     | ok               |
| DASH-USD   |       63 | -43.77%  | 24.57%             | -64.43% |    -0.05 | 29.69%     | ok               |
| DBC        |       62 | -13.35%  | 29.01%             | -25.70% |    -0.46 | 33.44%     | ok               |
| DE         |       72 | -8.69%   | 67.88%             | -25.24% |    -0.09 | 47.25%     | ok               |
| DIA        |       62 | -3.45%   | 34.39%             | -12.94% |    -0.15 | 44.09%     | ok               |
| DIS        |       66 | -21.41%  | -7.37%             | -28.17% |    -0.41 | 45.76%     | ok               |
| DOGE-USD   |       73 | -28.94%  | -71.33%            | -60.95% |    -0.06 | 50.00%     | ok               |
| DOT-USD    |       88 | -59.88%  | -82.01%            | -63.10% |    -0.65 | 47.89%     | ok               |
| DXY-INDEX  |       38 | -1.15%   | -0.35%             | -6.02%  |    -0.17 | 30.95%     | ok               |
| EEM        |       64 | -10.47%  | 58.03%             | -25.67% |    -0.28 | 43.09%     | ok               |
| EFA        |       60 | -7.84%   | 34.29%             | -13.41% |    -0.27 | 44.93%     | ok               |
| EOG        |       81 | -22.93%  | 18.95%             | -48.13% |    -0.47 | 47.09%     | ok               |
| ETC-USD    |       64 | -33.70%  | -65.78%            | -45.98% |    -0.47 | 30.27%     | ok               |
| ETH-USD    |       64 | 130.32%  | -28.67%            | -30.11% |     1.15 | 44.83%     | ok               |
| EWJ        |       62 | -19.48%  | 33.40%             | -30.73% |    -0.64 | 38.94%     | ok               |
| FCX        |       63 | -27.81%  | 51.44%             | -47.47% |    -0.31 | 45.26%     | ok               |
| FET-USD    |       85 | -40.02%  | -79.15%            | -54.02% |    -0.15 | 41.57%     | ok               |
| FIL-USD    |       70 | -47.29%  | -76.96%            | -50.88% |    -0.62 | 32.57%     | ok               |
| FXI        |       46 | -7.35%   | 44.18%             | -24.33% |    -0.1  | 30.28%     | ok               |
| GDX        |       60 | 11.28%   | 172.94%            | -34.99% |     0.3  | 48.09%     | ok               |
| GDXJ       |       68 | -24.30%  | 191.81%            | -44.93% |    -0.24 | 46.26%     | ok               |
| GE         |       76 | 12.68%   | 185.62%            | -27.82% |     0.33 | 53.08%     | ok               |
| GLD        |       48 | 26.97%   | 94.58%             | -16.63% |     0.67 | 47.59%     | ok               |
| GOOGL      |       59 | 79.31%   | 146.00%            | -20.41% |     1.18 | 53.08%     | ok               |
| GRT-USD    |       85 | -24.58%  | -87.50%            | -55.61% |    -0.1  | 41.76%     | ok               |
| GS         |       76 | -2.38%   | 180.55%            | -22.13% |     0.05 | 52.08%     | ok               |
| HD         |       71 | -7.53%   | -6.28%             | -17.69% |    -0.12 | 44.59%     | ok               |
| HON        |       93 | -26.82%  | 14.02%             | -29.80% |    -0.72 | 52.41%     | ok               |
| HYG        |       81 | -9.08%   | 3.23%              | -9.59%  |    -1.06 | 33.94%     | ok               |
| IBIT       |       34 | 30.82%   | -4.26%             | -18.95% |     0.66 | 32.09%     | ok               |
| IBM        |       77 | -19.46%  | 18.91%             | -44.74% |    -0.2  | 49.75%     | ok               |
| ICP-USD    |       77 | -11.90%  | -69.90%            | -50.29% |     0.13 | 34.48%     | ok               |
| IEF        |       76 | -10.90%  | 0.12%              | -11.70% |    -1.54 | 32.78%     | ok               |
| IEMG       |       58 | -8.94%   | 52.92%             | -26.84% |    -0.25 | 42.60%     | ok               |
| INJ-USD    |       75 | -52.92%  | -65.68%            | -77.42% |    -0.51 | 37.36%     | ok               |
| INTC       |       68 | 59.68%   | 125.64%            | -60.60% |     0.64 | 49.08%     | ok               |
| INTU       |       67 | -19.54%  | -55.19%            | -42.15% |    -0.23 | 41.60%     | ok               |
| ITA        |       72 | -2.69%   | 83.28%             | -23.75% |    -0    | 48.42%     | ok               |
| IWM        |       48 | 9.40%    | 48.21%             | -12.83% |     0.39 | 35.77%     | ok               |
| JNJ        |       68 | 4.23%    | 55.79%             | -17.51% |     0.2  | 50.92%     | ok               |
| JPM        |       75 | -20.07%  | 87.44%             | -33.16% |    -0.48 | 53.74%     | ok               |
| KO         |       49 | 28.93%   | 38.87%             | -8.07%  |     1.03 | 37.77%     | ok               |
| LDO-USD    |       78 | 19.61%   | -76.69%            | -60.93% |     0.43 | 39.66%     | ok               |
| LIN        |       66 | -5.09%   | 16.49%             | -21.53% |    -0.12 | 39.10%     | ok               |
| LINK-USD   |       76 | -18.72%  | -55.38%            | -50.48% |     0.04 | 42.34%     | ok               |
| LLY        |       71 | -28.46%  | 51.91%             | -53.34% |    -0.42 | 49.58%     | ok               |
| LRCX       |       82 | -27.18%  | 239.87%            | -63.39% |    -0.18 | 44.59%     | ok               |
| LTC-USD    |       72 | -34.32%  | -61.63%            | -53.76% |    -0.3  | 49.23%     | ok               |
| MCD        |       75 | -2.55%   | -7.59%             | -18.81% |    -0.05 | 38.10%     | ok               |
| META       |       74 | -30.67%  | 36.70%             | -38.96% |    -0.54 | 47.92%     | ok               |
| MPC        |       71 | -6.62%   | 82.32%             | -44.76% |     0    | 48.92%     | ok               |
| MRK        |       69 | -29.54%  | -1.26%             | -35.95% |    -0.7  | 44.26%     | ok               |
| MS         |       77 | -10.18%  | 154.36%            | -27.79% |    -0.16 | 49.58%     | ok               |
| MSFT       |       83 | -38.30%  | -2.56%             | -39.15% |    -1.02 | 47.42%     | ok               |
| MU         |       51 | 270.20%  | 893.13%            | -68.76% |     1.34 | 59.90%     | ok               |
| NEAR-USD   |       85 | -15.24%  | -37.58%            | -60.07% |     0.09 | 41.00%     | ok               |
| NEM        |       72 | -31.13%  | 194.04%            | -38.49% |    -0.33 | 53.08%     | ok               |
| NFLX       |       64 | 27.79%   | 26.34%             | -21.09% |     0.62 | 54.08%     | ok               |
| NKE        |       91 | -48.19%  | -57.58%            | -57.25% |    -0.9  | 43.59%     | ok               |
| NOW        |       82 | 6.57%    | -32.39%            | -27.34% |     0.25 | 45.92%     | ok               |
| NVDA       |       75 | -25.27%  | 172.18%            | -45.02% |    -0.17 | 59.71%     | ok               |
| OP-USD     |       70 | -26.66%  | -90.81%            | -70.27% |    -0.07 | 33.72%     | ok               |
| ORCL       |       70 | 127.40%  | 11.89%             | -29.47% |     1.02 | 54.24%     | ok               |
| OXY        |       71 | -1.72%   | -11.37%            | -34.15% |     0.09 | 45.76%     | ok               |
| PEP        |       77 | -5.36%   | -17.13%            | -21.35% |    -0.09 | 48.42%     | ok               |
| PEPE-USD   |       79 | 0.11%    | -71.26%            | -57.66% |     0.28 | 44.83%     | ok               |
| PFE        |       77 | -41.09%  | -8.75%             | -41.92% |    -1.32 | 36.27%     | ok               |
| PG         |       68 | -19.68%  | -5.64%             | -24.55% |    -0.75 | 40.10%     | ok               |
| PM         |       83 | -3.22%   | 108.18%            | -33.68% |     0.03 | 55.74%     | ok               |
| POL-USD    |       77 | 34.78%   | -73.24%            | -46.45% |     0.55 | 46.93%     | ok               |
| QCOM       |       73 | -15.25%  | 10.25%             | -56.59% |    -0.04 | 46.09%     | ok               |
| QQQ        |       62 | 19.84%   | 61.15%             | -12.88% |     0.57 | 43.93%     | ok               |
| RENDER-USD |       98 | -19.07%  | -64.18%            | -45.00% |     0.1  | 42.77%     | ok               |
| RTX        |       56 | 25.96%   | 117.09%            | -16.99% |     0.64 | 51.75%     | ok               |
| SBUX       |       64 | -20.04%  | 13.14%             | -29.22% |    -0.38 | 40.10%     | ok               |
| SCHW       |       74 | -12.56%  | 59.06%             | -31.92% |    -0.23 | 47.75%     | ok               |
| SHIB-USD   |       78 | -38.86%  | -73.51%            | -47.96% |    -0.35 | 51.34%     | ok               |
| SHY        |       48 | -2.24%   | 0.45%              | -2.85%  |    -0.79 | 34.28%     | ok               |
| SKY-USD    |       72 | -28.04%  | 6.09%              | -43.98% |    -0.33 | 40.44%     | ok               |
| SLB        |       73 | -23.87%  | -4.43%             | -54.23% |    -0.39 | 51.08%     | ok               |
| SLV        |       58 | 51.15%   | 142.03%            | -42.66% |     0.7  | 43.26%     | ok               |
| SMH        |       48 | 78.07%   | 171.00%            | -33.99% |     1.07 | 47.75%     | ok               |
| SNX-USD    |       58 | -15.26%  | -76.26%            | -34.76% |     0.08 | 37.93%     | ok               |
| SOL-USD    |       72 | -33.65%  | -61.95%            | -56.90% |    -0.1  | 59.77%     | ok               |
| SOXX       |       55 | 73.03%   | 147.35%            | -40.34% |     0.97 | 46.76%     | ok               |
| SPY        |       64 | 1.90%    | 47.93%             | -16.47% |     0.13 | 50.08%     | ok               |
| SUSHI-USD  |       96 | -78.37%  | -81.30%            | -82.62% |    -1.16 | 36.40%     | ok               |
| T          |       64 | 37.55%   | 32.49%             | -17.01% |     0.84 | 53.24%     | ok               |
| TGT        |       60 | -11.50%  | -6.74%             | -40.57% |    -0.16 | 38.94%     | ok               |
| TIA-USD    |       91 | -44.48%  | -88.13%            | -67.47% |    -0.3  | 36.40%     | ok               |
| TLT        |       72 | -21.42%  | -9.09%             | -21.82% |    -1.66 | 32.28%     | ok               |
| TMO        |       61 | 17.61%   | -3.09%             | -18.85% |     0.44 | 50.75%     | ok               |
| TMUS       |       70 | 6.71%    | 17.92%             | -25.71% |     0.24 | 48.09%     | ok               |
| TRX-USD    |       70 | 3.17%    | 33.57%             | -22.90% |     0.17 | 48.85%     | ok               |
| TSLA       |       70 | -14.59%  | 98.10%             | -54.91% |     0.05 | 41.26%     | ok               |
| TXN        |       73 | -13.59%  | 76.04%             | -47.39% |    -0.06 | 52.91%     | ok               |
| UNH        |       74 | 31.58%   | -19.59%            | -26.96% |     0.54 | 52.41%     | ok               |
| UNI-USD    |       88 | -73.61%  | -61.99%            | -80.61% |    -0.9  | 44.06%     | ok               |
| UPS        |       68 | -35.34%  | -21.74%            | -37.08% |    -0.7  | 39.10%     | ok               |
| USO        |       68 | 7.06%    | 62.09%             | -43.35% |     0.24 | 33.94%     | ok               |
| VEA        |       58 | -0.98%   | 43.59%             | -17.93% |     0.01 | 44.09%     | ok               |
| VIXY       |       96 | -80.86%  | -64.31%            | -88.16% |    -1.03 | 32.78%     | ok               |
| VNQ        |       73 | -15.86%  | 17.94%             | -24.92% |    -0.66 | 37.10%     | ok               |
| VTI        |       70 | -4.69%   | 47.15%             | -18.77% |    -0.11 | 50.42%     | ok               |
| VWO        |       78 | -14.72%  | 41.54%             | -25.20% |    -0.52 | 43.93%     | ok               |
| VZ         |       85 | -29.22%  | 7.73%              | -29.08% |    -0.99 | 37.77%     | ok               |
| WFC        |       84 | -15.70%  | 65.02%             | -30.87% |    -0.24 | 50.75%     | ok               |
| WIF-USD    |       70 | -35.32%  | -75.63%            | -50.56% |    -0.13 | 32.38%     | ok               |
| WMT        |       61 | 12.66%   | 96.60%             | -21.31% |     0.41 | 50.58%     | ok               |
| XBI        |       62 | 0.85%    | 61.44%             | -19.80% |     0.11 | 41.10%     | ok               |
| XLB        |       64 | -10.86%  | 17.91%             | -26.57% |    -0.36 | 36.77%     | ok               |
| XLC        |       69 | 10.08%   | 40.95%             | -12.33% |     0.39 | 54.24%     | ok               |
| XLE        |       75 | -9.73%   | 31.79%             | -37.64% |    -0.17 | 45.26%     | ok               |
| XLF        |       78 | -10.63%  | 41.52%             | -23.61% |    -0.34 | 48.09%     | ok               |
| XLI        |       66 | -2.21%   | 50.64%             | -11.79% |    -0.04 | 44.26%     | ok               |
| XLK        |       40 | 65.83%   | 72.54%             | -14.75% |     1.22 | 45.59%     | ok               |
| XLM-USD    |       69 | 5.21%    | -41.96%            | -50.36% |     0.28 | 45.79%     | ok               |
| XLP        |       68 | 4.51%    | 15.10%             | -11.16% |     0.29 | 41.60%     | ok               |
| XLU        |       67 | -5.24%   | 47.82%             | -20.40% |    -0.19 | 39.10%     | ok               |
| XLV        |       68 | -14.74%  | 9.95%              | -19.97% |    -0.72 | 36.11%     | ok               |
| XLY        |       70 | 3.26%    | 28.87%             | -14.01% |     0.17 | 44.43%     | ok               |
| XOM        |       57 | 4.95%    | 39.32%             | -20.29% |     0.21 | 36.61%     | ok               |
| XRP-USD    |       58 | -30.47%  | -54.67%            | -44.89% |    -0.26 | 33.72%     | ok               |
| YFI-USD    |       83 | -66.24%  | -62.67%            | -70.70% |    -1.11 | 40.61%     | ok               |
| ZEC-USD    |       64 | 45.49%   | 1529.43%           | -47.68% |     0.57 | 35.82%     | ok               |

## AAPL Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 31.37%   | 80.76%             | -21.71% |     0.64 |       68 | 53.41%     | ok               |
|          15 | 27.32%   | 80.76%             | -23.86% |     0.57 |       75 | 60.57%     | ok               |
|          30 | 20.64%   | 80.76%             | -20.65% |     0.49 |       61 | 49.08%     | ok               |
|          25 | 19.31%   | 80.76%             | -20.03% |     0.46 |       67 | 51.08%     | ok               |
|          35 | 17.93%   | 80.76%             | -22.04% |     0.44 |       61 | 47.59%     | ok               |

## AAVE-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 13.19%   | -62.62%            | -43.61% |     0.35 |       40 | 32.18%     | ok               |
|          35 | -6.17%   | -62.62%            | -51.96% |     0.16 |       50 | 35.44%     | ok               |
|          45 | -4.67%   | -62.62%            | -49.19% |     0.15 |       44 | 27.20%     | ok               |
|          15 | -51.69%  | -62.62%            | -61.76% |    -0.32 |       80 | 53.83%     | ok               |
|          50 | -33.87%  | -62.62%            | -47.39% |    -0.36 |       42 | 19.73%     | ok               |

## ABBV Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -11.88%  | 43.93%             | -28.51% |    -0.24 |       50 | 36.77%     | ok               |
|          30 | -19.07%  | 43.93%             | -30.55% |    -0.39 |       66 | 47.25%     | ok               |
|          40 | -19.14%  | 43.93%             | -26.61% |    -0.43 |       66 | 41.43%     | ok               |
|          25 | -20.87%  | 43.93%             | -31.26% |    -0.44 |       69 | 48.75%     | ok               |
|          20 | -21.48%  | 43.93%             | -30.60% |    -0.45 |       69 | 50.58%     | ok               |

## ADA-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -77.92%  | -79.30%            | -85.97% |    -0.59 |       55 | 26.82%     | ok               |
|          45 | -80.28%  | -79.30%            | -88.02% |    -0.62 |       58 | 31.61%     | ok               |
|          35 | -82.72%  | -79.30%            | -89.77% |    -0.67 |       78 | 42.34%     | ok               |
|          30 | -83.94%  | -79.30%            | -89.69% |    -0.71 |       88 | 46.74%     | ok               |
|          40 | -83.55%  | -79.30%            | -90.19% |    -0.72 |       74 | 36.97%     | ok               |

## ADBE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 1.24%    | -56.23%            | -22.53% |     0.14 |       72 | 49.08%     | ok               |
|          40 | -11.88%  | -56.23%            | -24.87% |    -0.11 |       70 | 42.10%     | ok               |
|          25 | -17.07%  | -56.23%            | -31.11% |    -0.12 |       48 | 61.56%     | ok               |
|          20 | -25.04%  | -56.23%            | -32.14% |    -0.25 |       48 | 63.73%     | ok               |
|          15 | -30.57%  | -56.23%            | -32.12% |    -0.35 |       57 | 65.72%     | ok               |

## AGG Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -6.80%   | 1.19%              | -9.97%  |    -1.13 |       69 | 31.45%     | ok               |
|          20 | -8.19%   | 1.19%              | -11.27% |    -1.21 |       73 | 36.94%     | ok               |
|          50 | -5.57%   | 1.19%              | -7.92%  |    -1.25 |       46 | 16.97%     | ok               |
|          45 | -6.18%   | 1.19%              | -7.89%  |    -1.25 |       54 | 20.97%     | ok               |
|          25 | -8.36%   | 1.19%              | -11.79% |    -1.28 |       73 | 35.27%     | ok               |

## ALGO-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -50.43%  | -71.10%            | -53.13% |    -0.57 |       86 | 38.12%     | ok               |
|          15 | -61.07%  | -71.10%            | -69.47% |    -0.66 |       88 | 50.57%     | ok               |
|          25 | -61.32%  | -71.10%            | -73.33% |    -0.72 |       88 | 45.21%     | ok               |
|          20 | -65.02%  | -71.10%            | -72.09% |    -0.78 |       90 | 48.28%     | ok               |
|          50 | -45.64%  | -71.10%            | -48.43% |    -0.81 |       42 | 16.86%     | ok               |

## AMAT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -22.77%  | 180.84%            | -54.05% |    -0.09 |       68 | 61.40%     | ok               |
|          30 | -34.41%  | 180.84%            | -57.21% |    -0.31 |       71 | 52.41%     | ok               |
|          35 | -34.87%  | 180.84%            | -55.26% |    -0.33 |       73 | 50.08%     | ok               |
|          50 | -34.72%  | 180.84%            | -48.72% |    -0.37 |       52 | 37.94%     | ok               |
|          20 | -41.94%  | 180.84%            | -60.16% |    -0.41 |       74 | 57.74%     | ok               |

## AMD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 6.74%    | 175.45%            | -44.26% |     0.27 |       54 | 30.62%     | ok               |
|          40 | 5.86%    | 175.45%            | -43.98% |     0.27 |       52 | 35.77%     | ok               |
|          35 | -5.47%   | 175.45%            | -50.71% |     0.16 |       60 | 37.27%     | ok               |
|          45 | -14.79%  | 175.45%            | -53.24% |     0.04 |       60 | 33.44%     | ok               |
|          30 | -17.93%  | 175.45%            | -56.46% |     0.02 |       61 | 39.77%     | ok               |

## AMGN Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -9.83%   | 30.30%             | -26.64% |    -0.12 |       71 | 52.41%     | ok               |
|          35 | -11.27%  | 30.30%             | -31.23% |    -0.18 |       65 | 42.43%     | ok               |
|          15 | -13.63%  | 30.30%             | -27.92% |    -0.2  |       67 | 57.90%     | ok               |
|          30 | -15.41%  | 30.30%             | -34.14% |    -0.29 |       69 | 46.26%     | ok               |
|          25 | -18.85%  | 30.30%             | -33.41% |    -0.37 |       65 | 48.59%     | ok               |

## AMZN Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -17.13%  | 43.14%             | -27.15% |    -0.5  |       52 | 29.12%     | ok               |
|          50 | -23.53%  | 43.14%             | -34.08% |    -0.84 |       50 | 23.13%     | ok               |
|          45 | -26.34%  | 43.14%             | -34.08% |    -0.93 |       54 | 26.12%     | ok               |
|          35 | -30.76%  | 43.14%             | -38.29% |    -0.97 |       68 | 32.78%     | ok               |
|          30 | -36.92%  | 43.14%             | -42.48% |    -1.11 |       80 | 38.27%     | ok               |

## APT-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 19.10%   | -89.57%            | -46.73% |     0.42 |       40 | 18.97%     | ok               |
|          45 | -10.39%  | -89.57%            | -63.86% |     0.07 |       58 | 24.71%     | ok               |
|          20 | -34.30%  | -89.57%            | -70.51% |    -0.1  |       71 | 51.15%     | ok               |
|          40 | -27.60%  | -89.57%            | -63.33% |    -0.12 |       64 | 30.27%     | ok               |
|          35 | -32.91%  | -89.57%            | -64.45% |    -0.16 |       68 | 36.02%     | ok               |

## ARB-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 32.92%   | -80.45%            | -53.74% |     0.52 |       87 | 56.51%     | ok               |
|          40 | 11.67%   | -80.45%            | -45.73% |     0.34 |       52 | 29.89%     | ok               |
|          20 | -0.11%   | -80.45%            | -60.40% |     0.28 |       75 | 50.00%     | ok               |
|          35 | 0.75%    | -80.45%            | -54.43% |     0.24 |       62 | 33.33%     | ok               |
|          45 | 0.15%    | -80.45%            | -49.08% |     0.2  |       58 | 23.18%     | ok               |

## ARKK Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -29.82%  | 58.15%             | -35.57% |    -0.39 |       94 | 51.08%     | ok               |
|          20 | -33.96%  | 58.15%             | -35.48% |    -0.52 |       89 | 46.42%     | ok               |
|          30 | -32.60%  | 58.15%             | -34.15% |    -0.56 |       81 | 39.60%     | ok               |
|          35 | -33.75%  | 58.15%             | -35.28% |    -0.62 |       80 | 37.27%     | ok               |
|          40 | -35.15%  | 58.15%             | -37.19% |    -0.7  |       72 | 32.45%     | ok               |

## ATOM-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -67.62%  | -67.93%            | -71.96% |    -1.06 |       95 | 51.72%     | ok               |
|          15 | -71.35%  | -67.93%            | -71.47% |    -1.09 |       97 | 62.07%     | ok               |
|          30 | -70.24%  | -67.93%            | -74.37% |    -1.23 |       90 | 44.83%     | ok               |
|          45 | -63.05%  | -67.93%            | -65.94% |    -1.25 |       74 | 28.54%     | ok               |
|          20 | -74.39%  | -67.93%            | -75.12% |    -1.26 |      101 | 55.56%     | ok               |

## AVAX-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 6.25%    | -74.21%            | -29.53% |     0.25 |       30 | 18.01%     | ok               |
|          40 | 4.23%    | -74.21%            | -32.96% |     0.23 |       36 | 24.52%     | ok               |
|          45 | 4.27%    | -74.21%            | -32.82% |     0.23 |       30 | 21.65%     | ok               |
|          35 | -3.28%   | -74.21%            | -36.30% |     0.15 |       54 | 29.89%     | ok               |
|          15 | -27.15%  | -74.21%            | -52.46% |    -0.06 |       73 | 53.07%     | ok               |

## AVGO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 15.77%   | 186.96%            | -35.84% |     0.35 |       58 | 30.78%     | ok               |
|          30 | 14.37%   | 186.96%            | -35.76% |     0.33 |       64 | 42.76%     | ok               |
|          40 | 13.00%   | 186.96%            | -40.70% |     0.32 |       62 | 36.61%     | ok               |
|          25 | 11.96%   | 186.96%            | -38.01% |     0.31 |       72 | 44.26%     | ok               |
|          45 | 9.90%    | 186.96%            | -41.66% |     0.28 |       60 | 34.28%     | ok               |

## BA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 23.47%   | 6.37%              | -13.42% |     0.62 |       42 | 31.28%     | ok               |
|          35 | 30.46%   | 6.37%              | -23.77% |     0.59 |       72 | 44.59%     | ok               |
|          40 | 17.66%   | 6.37%              | -25.45% |     0.43 |       46 | 38.44%     | ok               |
|          25 | 10.59%   | 6.37%              | -32.48% |     0.29 |       70 | 52.58%     | ok               |
|          30 | 7.60%    | 6.37%              | -30.56% |     0.25 |       67 | 49.25%     | ok               |

## BAC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 4.65%    | 82.95%             | -19.60% |     0.21 |       62 | 37.77%     | ok               |
|          35 | 0.66%    | 82.95%             | -27.11% |     0.09 |       70 | 45.76%     | ok               |
|          20 | 0.01%    | 82.95%             | -20.73% |     0.09 |       78 | 54.24%     | ok               |
|          50 | -1.57%   | 82.95%             | -20.35% |     0.01 |       62 | 34.78%     | ok               |
|          40 | -2.64%   | 82.95%             | -23.77% |    -0.01 |       66 | 40.77%     | ok               |

## BCH-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 19.33%   | -32.56%            | -45.63% |     0.41 |       69 | 54.02%     | ok               |
|          15 | 4.65%    | -32.56%            | -48.58% |     0.28 |       80 | 58.81%     | ok               |
|          25 | 4.46%    | -32.56%            | -51.09% |     0.27 |       68 | 50.19%     | ok               |
|          30 | -2.55%   | -32.56%            | -53.87% |     0.18 |       76 | 48.28%     | ok               |
|          35 | -23.33%  | -32.56%            | -64.08% |    -0.1  |       70 | 44.44%     | ok               |

## BITO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 20.14%   | -64.55%            | -31.98% |     0.4  |       54 | 24.79%     | ok               |
|          45 | 1.07%    | -64.55%            | -41.16% |     0.17 |       62 | 28.45%     | ok               |
|          30 | -1.36%   | -64.55%            | -42.82% |     0.16 |       80 | 41.43%     | ok               |
|          40 | -3.45%   | -64.55%            | -43.67% |     0.12 |       66 | 33.28%     | ok               |
|          15 | -8.63%   | -64.55%            | -48.38% |     0.11 |       89 | 50.42%     | ok               |

## BLK Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | -1.34%   | 33.64%             | -17.97% |     0.03 |       76 | 38.60%     | ok               |
|          20 | -3.44%   | 33.64%             | -21.48% |    -0.02 |       76 | 47.25%     | ok               |
|          40 | -4.99%   | 33.64%             | -20.08% |    -0.1  |       70 | 34.61%     | ok               |
|          30 | -7.59%   | 33.64%             | -24.29% |    -0.16 |       71 | 42.43%     | ok               |
|          25 | -8.52%   | 33.64%             | -23.36% |    -0.18 |       71 | 44.76%     | ok               |

## BND Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -6.87%   | 1.24%              | -9.36%  |    -1    |       65 | 38.44%     | ok               |
|          25 | -7.57%   | 1.24%              | -10.45% |    -1.16 |       69 | 36.44%     | ok               |
|          30 | -7.74%   | 1.24%              | -9.93%  |    -1.25 |       67 | 32.78%     | ok               |
|          15 | -9.07%   | 1.24%              | -11.14% |    -1.31 |       75 | 41.26%     | ok               |
|          45 | -7.64%   | 1.24%              | -9.57%  |    -1.47 |       52 | 22.63%     | ok               |

## BONK-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 179.94%  | -80.83%            | -35.57% |     1.28 |       44 | 21.84%     | ok               |
|          45 | 130.53%  | -80.83%            | -42.36% |     1.06 |       54 | 26.05%     | ok               |
|          20 | 137.48%  | -80.83%            | -55.19% |     0.94 |       68 | 52.87%     | ok               |
|          15 | 139.09%  | -80.83%            | -63.45% |     0.92 |       70 | 58.05%     | ok               |
|          25 | 109.07%  | -80.83%            | -47.99% |     0.86 |       67 | 48.08%     | ok               |

## BTC-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 43.79%   | -33.54%            | -15.92% |     0.81 |       46 | 34.67%     | ok               |
|          45 | 40.84%   | -33.54%            | -15.18% |     0.81 |       44 | 30.65%     | ok               |
|          35 | 26.71%   | -33.54%            | -27.54% |     0.56 |       70 | 41.57%     | ok               |
|          50 | 13.98%   | -33.54%            | -18.05% |     0.4  |       42 | 25.29%     | ok               |
|          30 | 13.28%   | -33.54%            | -21.75% |     0.35 |       74 | 48.47%     | ok               |

## C Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -6.29%   | 135.62%            | -22.28% |    -0.1  |       64 | 36.11%     | ok               |
|          45 | -18.56%  | 135.62%            | -30.30% |    -0.43 |       76 | 40.27%     | ok               |
|          25 | -27.45%  | 135.62%            | -35.32% |    -0.52 |       73 | 53.24%     | ok               |
|          15 | -29.85%  | 135.62%            | -36.64% |    -0.54 |       74 | 60.23%     | ok               |
|          40 | -24.28%  | 135.62%            | -35.18% |    -0.56 |       78 | 42.76%     | ok               |

## CAT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 22.49%   | 172.34%            | -21.02% |     0.46 |       72 | 55.91%     | ok               |
|          25 | 22.60%   | 172.34%            | -26.37% |     0.46 |       68 | 58.74%     | ok               |
|          20 | 21.13%   | 172.34%            | -25.65% |     0.43 |       78 | 62.23%     | ok               |
|          45 | 17.48%   | 172.34%            | -27.12% |     0.4  |       56 | 44.59%     | ok               |
|          35 | 14.45%   | 172.34%            | -27.72% |     0.35 |       70 | 49.42%     | ok               |

## CL Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 10.58%   | 9.38%              | -11.22% |     0.46 |       44 | 29.78%     | ok               |
|          30 | 7.91%    | 9.38%              | -14.32% |     0.31 |       62 | 45.92%     | ok               |
|          45 | 3.43%    | 9.38%              | -13.51% |     0.18 |       48 | 32.95%     | ok               |
|          35 | 2.78%    | 9.38%              | -13.83% |     0.15 |       64 | 42.26%     | ok               |
|          40 | -0.20%   | 9.38%              | -12.70% |     0.05 |       58 | 36.94%     | ok               |

## CMCSA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -37.22%  | -38.64%            | -44.10% |    -0.83 |       88 | 56.91%     | ok               |
|          30 | -38.98%  | -38.64%            | -40.26% |    -1.03 |       79 | 42.10%     | ok               |
|          25 | -42.72%  | -38.64%            | -42.73% |    -1.14 |       88 | 47.25%     | ok               |
|          50 | -31.28%  | -38.64%            | -32.53% |    -1.25 |       50 | 14.81%     | ok               |
|          20 | -47.99%  | -38.64%            | -47.99% |    -1.29 |       93 | 52.91%     | ok               |

## COMP-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -8.10%   | -69.18%            | -38.71% |     0.09 |       46 | 20.31%     | ok               |
|          25 | -47.14%  | -69.18%            | -61.30% |    -0.34 |       91 | 52.30%     | ok               |
|          30 | -45.09%  | -69.18%            | -57.88% |    -0.35 |       91 | 46.17%     | ok               |
|          15 | -54.19%  | -69.18%            | -66.20% |    -0.42 |      107 | 63.79%     | ok               |
|          40 | -46.33%  | -69.18%            | -50.01% |    -0.48 |       74 | 33.91%     | ok               |

## COP Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -6.91%   | 0.55%              | -35.08% |    -0.08 |       48 | 27.62%     | ok               |
|          35 | -19.39%  | 0.55%              | -43.58% |    -0.33 |       73 | 38.27%     | ok               |
|          45 | -17.90%  | 0.55%              | -41.35% |    -0.35 |       62 | 30.95%     | ok               |
|          30 | -23.58%  | 0.55%              | -43.96% |    -0.43 |       72 | 41.76%     | ok               |
|          40 | -23.09%  | 0.55%              | -47.05% |    -0.48 |       68 | 34.11%     | ok               |

## COST Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 10.21%   | 28.75%             | -24.32% |     0.35 |       66 | 50.08%     | ok               |
|          25 | 8.58%    | 28.75%             | -24.73% |     0.31 |       63 | 47.25%     | ok               |
|          35 | 3.53%    | 28.75%             | -26.58% |     0.18 |       54 | 40.60%     | ok               |
|          30 | -1.21%   | 28.75%             | -29.73% |     0.03 |       60 | 43.59%     | ok               |
|          40 | -2.82%   | 28.75%             | -28.41% |    -0.03 |       56 | 37.60%     | ok               |

## CRM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | -29.63%  | -41.20%            | -33.08% |    -0.59 |       60 | 37.94%     | ok               |
|          15 | -37.00%  | -41.20%            | -44.67% |    -0.6  |       92 | 54.74%     | ok               |
|          40 | -34.83%  | -41.20%            | -39.11% |    -0.8  |       66 | 33.94%     | ok               |
|          30 | -39.56%  | -41.20%            | -41.36% |    -0.83 |       63 | 42.76%     | ok               |
|          20 | -44.42%  | -41.20%            | -46.71% |    -0.86 |       76 | 48.42%     | ok               |

## CRV-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 17.80%   | -59.75%            | -37.78% |     0.4  |       70 | 31.61%     | ok               |
|          45 | 3.36%    | -59.75%            | -42.29% |     0.24 |       56 | 20.88%     | ok               |
|          40 | -2.40%   | -59.75%            | -38.86% |     0.18 |       60 | 27.20%     | ok               |
|          50 | -0.89%   | -59.75%            | -29.30% |     0.18 |       46 | 17.43%     | ok               |
|          30 | -6.45%   | -59.75%            | -39.89% |     0.17 |       68 | 36.21%     | ok               |

## CSCO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 32.93%   | 125.78%            | -19.34% |     0.71 |       52 | 37.60%     | ok               |
|          45 | 28.97%   | 125.78%            | -19.34% |     0.63 |       51 | 39.43%     | ok               |
|          35 | 25.14%   | 125.78%            | -23.68% |     0.54 |       53 | 46.42%     | ok               |
|          25 | 23.46%   | 125.78%            | -23.28% |     0.51 |       65 | 51.08%     | ok               |
|          30 | 22.88%   | 125.78%            | -21.79% |     0.5  |       61 | 49.08%     | ok               |

## CVX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -14.22%  | 18.29%             | -24.33% |    -0.32 |       75 | 42.60%     | ok               |
|          40 | -12.77%  | 18.29%             | -27.34% |    -0.34 |       77 | 34.78%     | ok               |
|          35 | -14.16%  | 18.29%             | -28.85% |    -0.35 |       69 | 37.10%     | ok               |
|          45 | -13.90%  | 18.29%             | -28.83% |    -0.39 |       67 | 30.95%     | ok               |
|          30 | -17.67%  | 18.29%             | -29.13% |    -0.46 |       75 | 39.93%     | ok               |

## DASH-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 116.13%  | 24.57%             | -22.10% |     0.91 |       38 | 14.56%     | ok               |
|          40 | 64.68%   | 24.57%             | -28.66% |     0.67 |       46 | 21.65%     | ok               |
|          45 | 55.83%   | 24.57%             | -30.93% |     0.63 |       42 | 16.67%     | ok               |
|          35 | -38.60%  | 24.57%             | -63.23% |     0.01 |       67 | 26.25%     | ok               |
|          25 | -44.21%  | 24.57%             | -64.14% |    -0.04 |       69 | 32.38%     | ok               |

## DBC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -8.28%   | 29.01%             | -27.14% |    -0.23 |       75 | 38.94%     | ok               |
|          50 | -8.19%   | 29.01%             | -20.31% |    -0.3  |       42 | 21.46%     | ok               |
|          35 | -10.69%  | 29.01%             | -23.91% |    -0.35 |       64 | 32.11%     | ok               |
|          25 | -11.13%  | 29.01%             | -26.10% |    -0.36 |       64 | 35.27%     | ok               |
|          45 | -10.73%  | 29.01%             | -21.46% |    -0.38 |       58 | 25.12%     | ok               |

## DE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -6.38%   | 67.88%             | -28.94% |    -0.03 |       74 | 52.75%     | ok               |
|          25 | -8.70%   | 67.88%             | -26.67% |    -0.09 |       76 | 50.08%     | ok               |
|          30 | -8.69%   | 67.88%             | -25.24% |    -0.09 |       72 | 47.25%     | ok               |
|          50 | -7.52%   | 67.88%             | -23.21% |    -0.12 |       70 | 31.78%     | ok               |
|          45 | -9.42%   | 67.88%             | -26.88% |    -0.15 |       70 | 36.27%     | ok               |

## DIA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | -1.41%   | 34.39%             | -13.15% |    -0.04 |       62 | 41.93%     | ok               |
|          25 | -1.94%   | 34.39%             | -11.28% |    -0.07 |       62 | 45.26%     | ok               |
|          30 | -3.45%   | 34.39%             | -12.94% |    -0.15 |       62 | 44.09%     | ok               |
|          20 | -5.30%   | 34.39%             | -13.85% |    -0.24 |       66 | 47.59%     | ok               |
|          40 | -5.43%   | 34.39%             | -15.06% |    -0.29 |       68 | 39.10%     | ok               |

## DIS Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 17.72%   | -7.37%             | -15.92% |     0.57 |       48 | 27.45%     | ok               |
|          45 | -6.82%   | -7.37%             | -16.68% |    -0.09 |       49 | 31.11%     | ok               |
|          40 | -8.29%   | -7.37%             | -24.79% |    -0.1  |       63 | 36.27%     | ok               |
|          15 | -16.96%  | -7.37%             | -31.15% |    -0.24 |       88 | 57.24%     | ok               |
|          35 | -15.81%  | -7.37%             | -25.70% |    -0.28 |       73 | 42.43%     | ok               |

## DOGE-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 0.88%    | -71.33%            | -57.89% |     0.3  |       81 | 66.67%     | ok               |
|          20 | -13.74%  | -71.33%            | -55.83% |     0.14 |       82 | 60.92%     | ok               |
|          25 | -15.08%  | -71.33%            | -53.72% |     0.12 |       70 | 55.56%     | ok               |
|          30 | -28.94%  | -71.33%            | -60.95% |    -0.06 |       73 | 50.00%     | ok               |
|          35 | -53.47%  | -71.33%            | -64.16% |    -0.54 |       70 | 43.30%     | ok               |

## DOT-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -32.99%  | -82.01%            | -46.17% |    -0.41 |       56 | 25.29%     | ok               |
|          45 | -37.17%  | -82.01%            | -52.51% |    -0.45 |       48 | 30.08%     | ok               |
|          35 | -55.64%  | -82.01%            | -61.83% |    -0.58 |       78 | 40.80%     | ok               |
|          20 | -62.56%  | -82.01%            | -65.30% |    -0.63 |       94 | 60.15%     | ok               |
|          40 | -48.44%  | -82.01%            | -52.18% |    -0.65 |       54 | 33.33%     | ok               |

## DXY-INDEX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -1.15%   | -0.35%             | -6.02%  |    -0.17 |       38 | 30.95%     | ok               |
|          15 | -3.60%   | -0.35%             | -11.37% |    -0.31 |       82 | 77.06%     | ok               |
|          40 | -5.46%   | -0.35%             | -8.08%  |    -0.69 |       74 | 50.65%     | ok               |
|          25 | -6.44%   | -0.35%             | -12.10% |    -0.69 |       78 | 67.10%     | ok               |
|          30 | -6.16%   | -0.35%             | -10.26% |    -0.71 |       70 | 62.12%     | ok               |

## EEM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -4.06%   | 58.03%             | -15.88% |    -0.09 |       50 | 35.77%     | ok               |
|          45 | -5.74%   | 58.03%             | -17.36% |    -0.15 |       52 | 37.27%     | ok               |
|          40 | -6.09%   | 58.03%             | -19.52% |    -0.15 |       64 | 39.43%     | ok               |
|          35 | -6.74%   | 58.03%             | -23.88% |    -0.16 |       66 | 41.43%     | ok               |
|          30 | -10.47%  | 58.03%             | -25.67% |    -0.28 |       64 | 43.09%     | ok               |

## EFA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -3.05%   | 34.29%             | -10.80% |    -0.05 |       62 | 52.41%     | ok               |
|          30 | -7.84%   | 34.29%             | -13.41% |    -0.27 |       60 | 44.93%     | ok               |
|          20 | -9.78%   | 34.29%             | -12.73% |    -0.34 |       69 | 49.42%     | ok               |
|          25 | -10.11%  | 34.29%             | -14.67% |    -0.37 |       62 | 46.92%     | ok               |
|          35 | -11.00%  | 34.29%             | -15.19% |    -0.42 |       60 | 43.93%     | ok               |

## EOG Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -18.19%  | 18.95%             | -39.69% |    -0.4  |       58 | 33.28%     | ok               |
|          30 | -22.93%  | 18.95%             | -48.13% |    -0.47 |       81 | 47.09%     | ok               |
|          35 | -23.78%  | 18.95%             | -46.26% |    -0.54 |       79 | 41.76%     | ok               |
|          40 | -23.03%  | 18.95%             | -43.26% |    -0.54 |       66 | 36.61%     | ok               |
|          25 | -26.84%  | 18.95%             | -51.99% |    -0.55 |       82 | 50.08%     | ok               |

## ETC-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -5.08%   | -65.78%            | -27.89% |     0.04 |       28 | 16.09%     | ok               |
|          35 | -12.40%  | -65.78%            | -42.62% |    -0.06 |       44 | 26.05%     | ok               |
|          45 | -13.47%  | -65.78%            | -35.44% |    -0.12 |       26 | 18.01%     | ok               |
|          40 | -18.60%  | -65.78%            | -40.48% |    -0.21 |       42 | 21.84%     | ok               |
|          30 | -33.70%  | -65.78%            | -45.98% |    -0.47 |       64 | 30.27%     | ok               |

## ETH-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 130.32%  | -28.67%            | -30.11% |     1.15 |       64 | 44.83%     | ok               |
|          30 | 97.20%   | -28.67%            | -32.89% |     0.95 |       68 | 53.45%     | ok               |
|          15 | 35.52%   | -28.67%            | -42.74% |     0.54 |       77 | 68.77%     | ok               |
|          40 | 32.09%   | -28.67%            | -33.11% |     0.54 |       64 | 36.97%     | ok               |
|          20 | 34.08%   | -28.67%            | -39.10% |     0.53 |       82 | 63.03%     | ok               |

## EWJ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -19.48%  | 33.40%             | -30.73% |    -0.64 |       62 | 38.94%     | ok               |
|          20 | -20.84%  | 33.40%             | -31.32% |    -0.68 |       58 | 40.93%     | ok               |
|          25 | -23.13%  | 33.40%             | -31.18% |    -0.78 |       58 | 39.93%     | ok               |
|          45 | -20.25%  | 33.40%             | -27.68% |    -0.78 |       58 | 31.11%     | ok               |
|          35 | -23.34%  | 33.40%             | -32.54% |    -0.81 |       68 | 37.27%     | ok               |

## FCX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -3.35%   | 51.44%             | -26.97% |     0.08 |       52 | 29.62%     | ok               |
|          45 | -7.51%   | 51.44%             | -34.52% |     0.01 |       52 | 34.11%     | ok               |
|          40 | -19.35%  | 51.44%             | -43.57% |    -0.19 |       62 | 38.60%     | ok               |
|          30 | -27.81%  | 51.44%             | -47.47% |    -0.31 |       63 | 45.26%     | ok               |
|          35 | -32.25%  | 51.44%             | -50.71% |    -0.42 |       69 | 43.43%     | ok               |

## FET-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -3.09%   | -79.15%            | -59.54% |     0.29 |       88 | 52.30%     | ok               |
|          15 | -17.57%  | -79.15%            | -59.58% |     0.18 |       84 | 56.13%     | ok               |
|          25 | -36.60%  | -79.15%            | -60.09% |    -0.07 |       91 | 45.98%     | ok               |
|          30 | -40.02%  | -79.15%            | -54.02% |    -0.15 |       85 | 41.57%     | ok               |
|          35 | -53.63%  | -79.15%            | -62.73% |    -0.5  |       69 | 33.72%     | ok               |

## FIL-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -26.71%  | -76.96%            | -41.11% |    -0.27 |       46 | 22.99%     | ok               |
|          35 | -44.63%  | -76.96%            | -48.17% |    -0.61 |       56 | 27.01%     | ok               |
|          45 | -39.88%  | -76.96%            | -43.98% |    -0.61 |       42 | 17.24%     | ok               |
|          30 | -47.29%  | -76.96%            | -50.88% |    -0.62 |       70 | 32.57%     | ok               |
|          50 | -39.00%  | -76.96%            | -44.95% |    -0.69 |       36 | 12.64%     | ok               |

## FXI Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -6.81%   | 44.18%             | -22.99% |    -0.08 |       46 | 31.45%     | ok               |
|          45 | -6.49%   | 44.18%             | -26.75% |    -0.09 |       44 | 24.63%     | ok               |
|          30 | -7.35%   | 44.18%             | -24.33% |    -0.1  |       46 | 30.28%     | ok               |
|          15 | -9.00%   | 44.18%             | -21.68% |    -0.13 |       52 | 34.78%     | ok               |
|          20 | -10.57%  | 44.18%             | -24.94% |    -0.18 |       52 | 32.61%     | ok               |

## GDX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 18.06%   | 172.94%            | -35.59% |     0.39 |       73 | 52.91%     | ok               |
|          40 | 13.85%   | 172.94%            | -31.87% |     0.35 |       64 | 42.93%     | ok               |
|          30 | 11.28%   | 172.94%            | -34.99% |     0.3  |       60 | 48.09%     | ok               |
|          35 | 8.95%    | 172.94%            | -32.37% |     0.27 |       68 | 45.26%     | ok               |
|          25 | 6.77%    | 172.94%            | -38.90% |     0.24 |       63 | 49.75%     | ok               |

## GDXJ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -9.30%   | 191.81%            | -45.05% |     0.04 |       67 | 53.08%     | ok               |
|          50 | -20.22%  | 191.81%            | -44.94% |    -0.22 |       58 | 37.77%     | ok               |
|          30 | -24.30%  | 191.81%            | -44.93% |    -0.24 |       68 | 46.26%     | ok               |
|          25 | -27.66%  | 191.81%            | -47.26% |    -0.27 |       72 | 49.75%     | ok               |
|          35 | -27.87%  | 191.81%            | -43.49% |    -0.32 |       70 | 43.93%     | ok               |

## GE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 30.10%   | 185.62%            | -22.29% |     0.61 |       66 | 39.77%     | ok               |
|          45 | 20.28%   | 185.62%            | -25.68% |     0.46 |       74 | 42.60%     | ok               |
|          20 | 13.95%   | 185.62%            | -26.63% |     0.34 |       71 | 56.91%     | ok               |
|          35 | 12.93%   | 185.62%            | -27.11% |     0.33 |       80 | 47.92%     | ok               |
|          30 | 12.68%   | 185.62%            | -27.82% |     0.33 |       76 | 53.08%     | ok               |

## GLD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 33.98%   | 94.58%             | -14.61% |     0.79 |       48 | 50.25%     | ok               |
|          25 | 33.32%   | 94.58%             | -14.61% |     0.78 |       46 | 48.75%     | ok               |
|          30 | 26.97%   | 94.58%             | -16.63% |     0.67 |       48 | 47.59%     | ok               |
|          15 | 25.77%   | 94.58%             | -17.54% |     0.62 |       50 | 54.41%     | ok               |
|          35 | 17.08%   | 94.58%             | -17.29% |     0.48 |       54 | 46.09%     | ok               |

## GOOGL Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 80.35%   | 146.00%            | -19.12% |     1.22 |       63 | 48.42%     | ok               |
|          25 | 81.59%   | 146.00%            | -19.76% |     1.19 |       55 | 55.41%     | ok               |
|          30 | 79.31%   | 146.00%            | -20.41% |     1.18 |       59 | 53.08%     | ok               |
|          45 | 64.33%   | 146.00%            | -15.05% |     1.11 |       56 | 41.60%     | ok               |
|          40 | 60.75%   | 146.00%            | -20.80% |     1.04 |       52 | 43.26%     | ok               |

## GRT-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 16.38%   | -87.50%            | -34.13% |     0.39 |       42 | 20.88%     | ok               |
|          15 | -3.17%   | -87.50%            | -49.67% |     0.22 |       73 | 61.30%     | ok               |
|          20 | -6.53%   | -87.50%            | -46.47% |     0.18 |       81 | 55.75%     | ok               |
|          35 | -10.09%  | -87.50%            | -51.30% |     0.07 |       60 | 35.44%     | ok               |
|          45 | -7.85%   | -87.50%            | -50.86% |     0.06 |       50 | 26.25%     | ok               |

## GS Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 21.11%   | 180.55%            | -20.56% |     0.47 |       74 | 61.06%     | ok               |
|          20 | 4.59%    | 180.55%            | -23.19% |     0.19 |       74 | 57.07%     | ok               |
|          40 | 0.08%    | 180.55%            | -17.88% |     0.09 |       72 | 45.26%     | ok               |
|          25 | -0.70%   | 180.55%            | -23.32% |     0.09 |       74 | 54.58%     | ok               |
|          30 | -2.38%   | 180.55%            | -22.13% |     0.05 |       76 | 52.08%     | ok               |

## HD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -7.53%   | -6.28%             | -17.69% |    -0.12 |       71 | 44.59%     | ok               |
|          25 | -8.25%   | -6.28%             | -18.51% |    -0.14 |       70 | 46.59%     | ok               |
|          15 | -17.75%  | -6.28%             | -27.53% |    -0.37 |      110 | 55.57%     | ok               |
|          35 | -15.13%  | -6.28%             | -22.98% |    -0.38 |       80 | 40.43%     | ok               |
|          40 | -13.89%  | -6.28%             | -19.63% |    -0.39 |       84 | 34.11%     | ok               |

## HON Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -13.43%  | 14.02%             | -21.17% |    -0.4  |       72 | 31.78%     | ok               |
|          45 | -15.16%  | 14.02%             | -19.99% |    -0.43 |       74 | 36.77%     | ok               |
|          40 | -23.52%  | 14.02%             | -26.29% |    -0.66 |       76 | 41.10%     | ok               |
|          35 | -24.98%  | 14.02%             | -27.37% |    -0.69 |       91 | 47.42%     | ok               |
|          30 | -26.82%  | 14.02%             | -29.80% |    -0.72 |       93 | 52.41%     | ok               |

## HYG Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -7.98%   | 3.23%              | -7.98%  |    -0.96 |       70 | 29.28%     | ok               |
|          15 | -9.44%   | 3.23%              | -10.29% |    -1.02 |       88 | 41.10%     | ok               |
|          20 | -9.18%   | 3.23%              | -10.29% |    -1.03 |       86 | 38.94%     | ok               |
|          25 | -9.38%   | 3.23%              | -10.11% |    -1.06 |       83 | 36.61%     | ok               |
|          30 | -9.08%   | 3.23%              | -9.59%  |    -1.06 |       81 | 33.94%     | ok               |

## IBIT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 53.73%   | -4.26%             | -17.37% |     1.07 |       22 | 22.33%     | ok               |
|          15 | 56.91%   | -4.26%             | -19.20% |     0.95 |       40 | 39.77%     | ok               |
|          45 | 44.27%   | -4.26%             | -17.37% |     0.9  |       26 | 23.72%     | ok               |
|          40 | 38.04%   | -4.26%             | -17.78% |     0.8  |       26 | 25.58%     | ok               |
|          30 | 30.82%   | -4.26%             | -18.95% |     0.66 |       34 | 32.09%     | ok               |

## IBM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -11.49%  | 18.91%             | -43.33% |    -0.02 |       93 | 61.90%     | ok               |
|          30 | -19.46%  | 18.91%             | -44.74% |    -0.2  |       77 | 49.75%     | ok               |
|          20 | -23.00%  | 18.91%             | -48.00% |    -0.23 |       75 | 54.41%     | ok               |
|          35 | -21.53%  | 18.91%             | -44.74% |    -0.24 |       71 | 45.42%     | ok               |
|          25 | -30.12%  | 18.91%             | -51.09% |    -0.39 |       74 | 52.41%     | ok               |

## ICP-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | -0.07%   | -69.90%            | -37.43% |     0.21 |       60 | 28.35%     | ok               |
|          30 | -11.90%  | -69.90%            | -50.29% |     0.13 |       77 | 34.48%     | ok               |
|          40 | -5.35%   | -69.90%            | -32.85% |     0.13 |       54 | 23.95%     | ok               |
|          50 | -18.12%  | -69.90%            | -43.65% |    -0.09 |       32 | 14.18%     | ok               |
|          20 | -44.32%  | -69.90%            | -58.71% |    -0.17 |       86 | 45.40%     | ok               |

## IEF Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -7.23%   | 0.12%              | -10.09% |    -0.87 |       70 | 42.10%     | ok               |
|          15 | -7.78%   | 0.12%              | -10.82% |    -0.92 |       69 | 43.59%     | ok               |
|          40 | -8.39%   | 0.12%              | -9.67%  |    -1.31 |       60 | 24.79%     | ok               |
|          45 | -8.07%   | 0.12%              | -9.73%  |    -1.33 |       50 | 22.80%     | ok               |
|          25 | -10.80%  | 0.12%              | -11.49% |    -1.38 |       76 | 39.27%     | ok               |

## IEMG Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -2.27%   | 52.92%             | -13.91% |    -0.03 |       52 | 33.61%     | ok               |
|          45 | -3.07%   | 52.92%             | -14.92% |    -0.06 |       48 | 36.11%     | ok               |
|          35 | -3.93%   | 52.92%             | -22.13% |    -0.07 |       63 | 41.60%     | ok               |
|          40 | -4.56%   | 52.92%             | -18.43% |    -0.11 |       60 | 39.10%     | ok               |
|          25 | -8.17%   | 52.92%             | -25.58% |    -0.22 |       59 | 44.43%     | ok               |

## INJ-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -16.04%  | -65.68%            | -56.91% |    -0.02 |       44 | 22.22%     | ok               |
|          35 | -21.39%  | -65.68%            | -61.19% |    -0.03 |       60 | 31.80%     | ok               |
|          50 | -25.16%  | -65.68%            | -52.76% |    -0.19 |       48 | 19.16%     | ok               |
|          40 | -30.34%  | -65.68%            | -59.56% |    -0.21 |       48 | 27.97%     | ok               |
|          20 | -50.45%  | -65.68%            | -79.76% |    -0.36 |       78 | 46.36%     | ok               |

## INTC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 100.33%  | 125.64%            | -53.65% |     0.81 |       79 | 59.73%     | ok               |
|          45 | 80.47%   | 125.64%            | -49.32% |     0.77 |       58 | 34.11%     | ok               |
|          20 | 87.05%   | 125.64%            | -52.47% |     0.76 |       78 | 55.91%     | ok               |
|          25 | 79.85%   | 125.64%            | -56.41% |     0.74 |       73 | 51.41%     | ok               |
|          40 | 74.55%   | 125.64%            | -55.86% |     0.72 |       66 | 38.44%     | ok               |

## INTU Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -0.28%   | -55.19%            | -40.73% |     0.11 |       69 | 27.95%     | ok               |
|          45 | -2.22%   | -55.19%            | -41.76% |     0.08 |       67 | 31.95%     | ok               |
|          40 | -8.64%   | -55.19%            | -45.15% |    -0.04 |       67 | 34.94%     | ok               |
|          35 | -15.62%  | -55.19%            | -46.75% |    -0.16 |       71 | 38.44%     | ok               |
|          25 | -18.48%  | -55.19%            | -39.87% |    -0.2  |       68 | 44.26%     | ok               |

## ITA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 0.42%    | 83.28%             | -25.76% |     0.1  |       85 | 59.90%     | ok               |
|          50 | 0.81%    | 83.28%             | -21.48% |     0.09 |       76 | 38.44%     | ok               |
|          30 | -2.69%   | 83.28%             | -23.75% |    -0    |       72 | 48.42%     | ok               |
|          35 | -4.76%   | 83.28%             | -23.16% |    -0.07 |       76 | 46.76%     | ok               |
|          40 | -5.85%   | 83.28%             | -20.58% |    -0.11 |       78 | 43.26%     | ok               |

## IWM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 8.60%    | 48.21%             | -14.08% |     0.39 |       42 | 31.28%     | ok               |
|          30 | 9.40%    | 48.21%             | -12.83% |     0.39 |       48 | 35.77%     | ok               |
|          25 | 9.50%    | 48.21%             | -13.55% |     0.39 |       50 | 36.94%     | ok               |
|          35 | 8.35%    | 48.21%             | -14.11% |     0.36 |       48 | 33.61%     | ok               |
|          20 | 5.19%    | 48.21%             | -14.08% |     0.24 |       60 | 37.94%     | ok               |

## JNJ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 22.39%   | 55.79%             | -10.57% |     0.89 |       54 | 37.77%     | ok               |
|          45 | 13.65%   | 55.79%             | -13.35% |     0.56 |       54 | 42.60%     | ok               |
|          15 | 13.71%   | 55.79%             | -18.02% |     0.48 |       64 | 57.40%     | ok               |
|          20 | 9.85%    | 55.79%             | -17.61% |     0.38 |       68 | 54.08%     | ok               |
|          40 | 8.18%    | 55.79%             | -14.77% |     0.35 |       60 | 46.92%     | ok               |

## JPM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 14.19%   | 87.44%             | -15.90% |     0.5  |       54 | 40.77%     | ok               |
|          45 | 3.35%    | 87.44%             | -21.91% |     0.17 |       56 | 43.76%     | ok               |
|          20 | -12.85%  | 87.44%             | -33.59% |    -0.2  |       84 | 58.40%     | ok               |
|          40 | -10.30%  | 87.44%             | -28.47% |    -0.23 |       68 | 46.26%     | ok               |
|          35 | -15.60%  | 87.44%             | -27.43% |    -0.37 |       76 | 50.25%     | ok               |

## KO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 28.93%   | 38.87%             | -8.07%  |     1.03 |       49 | 37.77%     | ok               |
|          35 | 24.98%   | 38.87%             | -8.07%  |     0.93 |       52 | 36.44%     | ok               |
|          40 | 22.37%   | 38.87%             | -9.28%  |     0.9  |       54 | 33.28%     | ok               |
|          25 | 23.60%   | 38.87%             | -9.37%  |     0.86 |       55 | 40.43%     | ok               |
|          50 | 14.81%   | 38.87%             | -11.40% |     0.68 |       36 | 26.79%     | ok               |

## LDO-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 54.11%   | -76.69%            | -46.95% |     0.64 |       83 | 53.26%     | ok               |
|          20 | 39.81%   | -76.69%            | -44.97% |     0.57 |       87 | 48.66%     | ok               |
|          50 | 31.75%   | -76.69%            | -48.04% |     0.56 |       50 | 17.62%     | ok               |
|          30 | 19.61%   | -76.69%            | -60.93% |     0.43 |       78 | 39.66%     | ok               |
|          35 | 16.95%   | -76.69%            | -62.61% |     0.4  |       76 | 32.76%     | ok               |

## LIN Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -0.63%   | 16.49%             | -23.68% |     0.04 |       64 | 49.92%     | ok               |
|          25 | -0.90%   | 16.49%             | -22.01% |     0.03 |       63 | 41.93%     | ok               |
|          20 | -3.02%   | 16.49%             | -23.00% |    -0.04 |       62 | 45.09%     | ok               |
|          35 | -4.48%   | 16.49%             | -21.18% |    -0.11 |       62 | 32.61%     | ok               |
|          30 | -5.09%   | 16.49%             | -21.53% |    -0.12 |       66 | 39.10%     | ok               |

## LINK-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -18.72%  | -55.38%            | -50.48% |     0.04 |       76 | 42.34%     | ok               |
|          45 | -14.09%  | -55.38%            | -38.56% |     0.04 |       52 | 26.63%     | ok               |
|          50 | -13.67%  | -55.38%            | -36.98% |     0.02 |       42 | 21.26%     | ok               |
|          35 | -25.03%  | -55.38%            | -49.56% |    -0.06 |       62 | 36.78%     | ok               |
|          40 | -29.15%  | -55.38%            | -50.91% |    -0.15 |       58 | 31.03%     | ok               |

## LLY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 5.04%    | 51.91%             | -38.23% |     0.21 |       46 | 36.77%     | ok               |
|          15 | -4.30%   | 51.91%             | -48.12% |     0.08 |       63 | 60.23%     | ok               |
|          45 | -6.78%   | 51.91%             | -42.66% |    -0.02 |       54 | 40.27%     | ok               |
|          20 | -19.71%  | 51.91%             | -51.34% |    -0.21 |       72 | 55.24%     | ok               |
|          25 | -21.03%  | 51.91%             | -53.47% |    -0.24 |       68 | 52.58%     | ok               |

## LRCX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -11.07%  | 239.87%            | -60.45% |     0.07 |       83 | 54.24%     | ok               |
|          50 | -15.90%  | 239.87%            | -50.39% |    -0.05 |       80 | 35.94%     | ok               |
|          40 | -18.43%  | 239.87%            | -56.86% |    -0.06 |       72 | 41.76%     | ok               |
|          35 | -23.72%  | 239.87%            | -61.76% |    -0.13 |       80 | 43.76%     | ok               |
|          20 | -25.83%  | 239.87%            | -67.48% |    -0.14 |       89 | 49.75%     | ok               |

## LTC-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -12.22%  | -61.63%            | -44.78% |    -0    |       56 | 31.80%     | ok               |
|          35 | -22.47%  | -61.63%            | -54.86% |    -0.13 |       66 | 42.91%     | ok               |
|          30 | -34.32%  | -61.63%            | -53.76% |    -0.3  |       72 | 49.23%     | ok               |
|          40 | -31.40%  | -61.63%            | -56.10% |    -0.3  |       58 | 38.12%     | ok               |
|          25 | -36.92%  | -61.63%            | -54.26% |    -0.33 |       76 | 51.72%     | ok               |

## MCD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 1.93%    | -7.59%             | -9.22%  |     0.14 |       40 | 20.80%     | ok               |
|          30 | -2.55%   | -7.59%             | -18.81% |    -0.05 |       75 | 38.10%     | ok               |
|          25 | -3.59%   | -7.59%             | -20.47% |    -0.09 |       75 | 40.77%     | ok               |
|          35 | -7.68%   | -7.59%             | -15.45% |    -0.29 |       67 | 34.44%     | ok               |
|          40 | -7.95%   | -7.59%             | -16.86% |    -0.33 |       71 | 28.79%     | ok               |

## META Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -11.20%  | 36.70%             | -31.03% |    -0.13 |       68 | 37.44%     | ok               |
|          40 | -20.96%  | 36.70%             | -35.11% |    -0.34 |       68 | 40.43%     | ok               |
|          25 | -28.76%  | 36.70%             | -39.84% |    -0.47 |       69 | 51.08%     | ok               |
|          50 | -24.75%  | 36.70%             | -34.00% |    -0.48 |       72 | 33.61%     | ok               |
|          30 | -30.67%  | 36.70%             | -38.96% |    -0.54 |       74 | 47.92%     | ok               |

## MPC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 23.97%   | 82.32%             | -23.96% |     0.53 |       52 | 37.60%     | ok               |
|          45 | 16.11%   | 82.32%             | -25.09% |     0.4  |       58 | 41.26%     | ok               |
|          40 | 14.35%   | 82.32%             | -25.70% |     0.36 |       60 | 43.59%     | ok               |
|          35 | 10.81%   | 82.32%             | -35.90% |     0.3  |       68 | 46.09%     | ok               |
|          30 | -6.62%   | 82.32%             | -44.76% |     0    |       71 | 48.92%     | ok               |

## MRK Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -20.40%  | -1.26%             | -30.12% |    -0.37 |       89 | 55.24%     | ok               |
|          25 | -20.02%  | -1.26%             | -31.07% |    -0.39 |       74 | 47.25%     | ok               |
|          20 | -23.94%  | -1.26%             | -29.59% |    -0.49 |       79 | 50.58%     | ok               |
|          45 | -24.67%  | -1.26%             | -27.72% |    -0.66 |       61 | 33.28%     | ok               |
|          35 | -28.55%  | -1.26%             | -35.44% |    -0.68 |       69 | 40.77%     | ok               |

## MS Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -3.32%   | 154.36%            | -19.99% |     0    |       72 | 41.43%     | ok               |
|          15 | -4.98%   | 154.36%            | -22.02% |    -0.01 |       73 | 58.24%     | ok               |
|          20 | -5.09%   | 154.36%            | -25.68% |    -0.02 |       77 | 54.41%     | ok               |
|          30 | -10.18%  | 154.36%            | -27.79% |    -0.16 |       77 | 49.58%     | ok               |
|          35 | -10.11%  | 154.36%            | -25.26% |    -0.17 |       78 | 46.09%     | ok               |

## MSFT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -22.13%  | -2.56%             | -25.26% |    -0.62 |       66 | 34.11%     | ok               |
|          50 | -23.55%  | -2.56%             | -26.14% |    -0.69 |       62 | 29.12%     | ok               |
|          35 | -34.48%  | -2.56%             | -35.38% |    -0.93 |       73 | 42.76%     | ok               |
|          40 | -33.86%  | -2.56%             | -34.77% |    -0.95 |       69 | 37.60%     | ok               |
|          30 | -38.30%  | -2.56%             | -39.15% |    -1.02 |       83 | 47.42%     | ok               |

## MU Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 443.99%  | 893.13%            | -61.96% |     1.59 |       45 | 67.22%     | ok               |
|          25 | 357.11%  | 893.13%            | -67.90% |     1.51 |       47 | 61.56%     | ok               |
|          20 | 313.39%  | 893.13%            | -67.25% |     1.4  |       51 | 63.23%     | ok               |
|          40 | 290.77%  | 893.13%            | -64.07% |     1.4  |       56 | 55.24%     | ok               |
|          30 | 270.20%  | 893.13%            | -68.76% |     1.34 |       51 | 59.90%     | ok               |

## NEAR-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 73.04%   | -37.58%            | -45.84% |     0.83 |       42 | 22.99%     | ok               |
|          50 | 45.50%   | -37.58%            | -51.20% |     0.65 |       38 | 18.01%     | ok               |
|          40 | 37.61%   | -37.58%            | -54.53% |     0.57 |       44 | 27.20%     | ok               |
|          35 | 15.68%   | -37.58%            | -58.86% |     0.38 |       68 | 32.38%     | ok               |
|          15 | -16.59%  | -37.58%            | -54.94% |     0.14 |       87 | 55.56%     | ok               |

## NEM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 3.24%    | 194.04%            | -29.41% |     0.21 |       62 | 61.40%     | ok               |
|          20 | -7.81%   | 194.04%            | -30.47% |     0.07 |       72 | 56.91%     | ok               |
|          25 | -21.27%  | 194.04%            | -37.89% |    -0.14 |       68 | 54.74%     | ok               |
|          50 | -25.02%  | 194.04%            | -33.36% |    -0.27 |       58 | 40.43%     | ok               |
|          30 | -31.13%  | 194.04%            | -38.49% |    -0.33 |       72 | 53.08%     | ok               |

## NFLX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 46.71%   | 26.34%             | -11.94% |     0.98 |       46 | 45.76%     | ok               |
|          50 | 40.46%   | 26.34%             | -16.28% |     0.94 |       46 | 38.27%     | ok               |
|          35 | 39.17%   | 26.34%             | -18.30% |     0.82 |       60 | 49.25%     | ok               |
|          45 | 30.85%   | 26.34%             | -15.48% |     0.73 |       52 | 42.10%     | ok               |
|          15 | 36.92%   | 26.34%             | -26.59% |     0.7  |       67 | 65.06%     | ok               |

## NKE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -33.86%  | -57.58%            | -50.44% |    -0.42 |       93 | 52.58%     | ok               |
|          40 | -26.46%  | -57.58%            | -31.19% |    -0.5  |       63 | 30.12%     | ok               |
|          15 | -38.38%  | -57.58%            | -55.52% |    -0.51 |       91 | 56.91%     | ok               |
|          25 | -45.09%  | -57.58%            | -52.84% |    -0.79 |       91 | 48.59%     | ok               |
|          35 | -39.10%  | -57.58%            | -43.08% |    -0.8  |       75 | 37.10%     | ok               |

## NOW Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 10.07%   | -32.39%            | -26.36% |     0.29 |       79 | 52.08%     | ok               |
|          30 | 6.57%    | -32.39%            | -27.34% |     0.25 |       82 | 45.92%     | ok               |
|          15 | 1.34%    | -32.39%            | -26.75% |     0.19 |       90 | 55.07%     | ok               |
|          25 | 0.10%    | -32.39%            | -27.28% |     0.17 |       74 | 49.42%     | ok               |
|          40 | -0.36%   | -32.39%            | -30.87% |     0.13 |       68 | 34.78%     | ok               |

## NVDA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -7.53%   | 172.18%            | -35.26% |     0.04 |       76 | 48.31%     | ok               |
|          20 | -12.91%  | 172.18%            | -40.59% |     0    |       72 | 56.33%     | ok               |
|          25 | -12.77%  | 172.18%            | -33.22% |    -0.01 |       73 | 51.34%     | ok               |
|          50 | -16.38%  | 172.18%            | -40.84% |    -0.14 |       58 | 32.26%     | ok               |
|          15 | -25.27%  | 172.18%            | -45.02% |    -0.17 |       75 | 59.71%     | ok               |

## OP-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 27.06%   | -90.81%            | -36.11% |     0.51 |       30 | 11.11%     | ok               |
|          45 | 26.15%   | -90.81%            | -45.76% |     0.48 |       32 | 15.71%     | ok               |
|          40 | 7.79%    | -90.81%            | -53.61% |     0.29 |       46 | 24.14%     | ok               |
|          35 | -10.29%  | -90.81%            | -58.33% |     0.09 |       54 | 27.20%     | ok               |
|          30 | -26.66%  | -90.81%            | -70.27% |    -0.07 |       70 | 33.72%     | ok               |

## ORCL Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 256.07%  | 11.89%             | -29.32% |     1.41 |       70 | 65.56%     | ok               |
|          25 | 167.11%  | 11.89%             | -27.76% |     1.16 |       71 | 58.07%     | ok               |
|          20 | 162.52%  | 11.89%             | -29.32% |     1.13 |       73 | 61.23%     | ok               |
|          35 | 127.20%  | 11.89%             | -31.95% |     1.02 |       64 | 50.08%     | ok               |
|          30 | 127.40%  | 11.89%             | -29.47% |     1.02 |       70 | 54.24%     | ok               |

## OXY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 3.67%    | -11.37%            | -29.57% |     0.18 |       38 | 28.29%     | ok               |
|          35 | 0.73%    | -11.37%            | -30.04% |     0.13 |       70 | 40.43%     | ok               |
|          30 | -1.72%   | -11.37%            | -34.15% |     0.09 |       71 | 45.76%     | ok               |
|          40 | -1.60%   | -11.37%            | -31.65% |     0.08 |       56 | 35.77%     | ok               |
|          45 | -8.62%   | -11.37%            | -34.87% |    -0.08 |       46 | 30.62%     | ok               |

## PEP Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 12.74%   | -17.13%            | -11.62% |     0.57 |       44 | 27.29%     | ok               |
|          45 | 4.63%    | -17.13%            | -14.22% |     0.24 |       62 | 31.45%     | ok               |
|          40 | 0.85%    | -17.13%            | -18.04% |     0.09 |       72 | 37.10%     | ok               |
|          35 | 0.33%    | -17.13%            | -21.42% |     0.08 |       81 | 41.93%     | ok               |
|          30 | -5.36%   | -17.13%            | -21.35% |    -0.09 |       77 | 48.42%     | ok               |

## PEPE-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 0.11%    | -71.26%            | -57.66% |     0.28 |       79 | 44.83%     | ok               |
|          15 | -8.76%   | -71.26%            | -64.84% |     0.27 |       82 | 61.49%     | ok               |
|          35 | -5.60%   | -71.26%            | -51.35% |     0.2  |       64 | 39.46%     | ok               |
|          25 | -18.34%  | -71.26%            | -53.88% |     0.11 |       91 | 50.77%     | ok               |
|          20 | -28.86%  | -71.26%            | -64.07% |     0.03 |       88 | 57.85%     | ok               |

## PFE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -24.41%  | -8.75%             | -25.61% |    -0.92 |       52 | 19.13%     | ok               |
|          50 | -26.23%  | -8.75%             | -27.28% |    -1.12 |       38 | 15.31%     | ok               |
|          40 | -31.46%  | -8.75%             | -32.57% |    -1.14 |       74 | 24.13%     | ok               |
|          35 | -35.07%  | -8.75%             | -36.57% |    -1.17 |       84 | 31.95%     | ok               |
|          30 | -41.09%  | -8.75%             | -41.92% |    -1.32 |       77 | 36.27%     | ok               |

## PG Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -8.53%   | -5.64%             | -20.08% |    -0.31 |       58 | 33.44%     | ok               |
|          35 | -11.65%  | -5.64%             | -18.99% |    -0.43 |       66 | 36.94%     | ok               |
|          30 | -19.68%  | -5.64%             | -24.55% |    -0.75 |       68 | 40.10%     | ok               |
|          45 | -17.47%  | -5.64%             | -22.43% |    -0.76 |       58 | 30.95%     | ok               |
|          25 | -21.51%  | -5.64%             | -26.24% |    -0.83 |       80 | 41.60%     | ok               |

## PM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | -0.28%   | 108.18%            | -32.20% |     0.09 |       86 | 52.08%     | ok               |
|          20 | -2.79%   | 108.18%            | -31.89% |     0.04 |       87 | 60.73%     | ok               |
|          30 | -3.22%   | 108.18%            | -33.68% |     0.03 |       83 | 55.74%     | ok               |
|          50 | -6.95%   | 108.18%            | -35.70% |    -0.09 |       74 | 42.10%     | ok               |
|          40 | -8.33%   | 108.18%            | -37.94% |    -0.12 |       80 | 48.25%     | ok               |

## POL-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 34.78%   | -73.24%            | -46.45% |     0.55 |       77 | 46.93%     | ok               |
|          25 | 20.88%   | -73.24%            | -46.72% |     0.43 |       68 | 54.98%     | ok               |
|          20 | 10.32%   | -73.24%            | -52.88% |     0.33 |       78 | 60.34%     | ok               |
|          15 | -11.47%  | -73.24%            | -58.42% |     0.12 |       78 | 66.09%     | ok               |
|          40 | -9.07%   | -73.24%            | -41.02% |     0.04 |       58 | 30.65%     | ok               |

## QCOM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -3.88%   | 10.25%             | -54.50% |     0.12 |       71 | 47.75%     | ok               |
|          35 | -4.42%   | 10.25%             | -50.58% |     0.11 |       77 | 43.59%     | ok               |
|          20 | -7.78%   | 10.25%             | -54.38% |     0.08 |       67 | 50.58%     | ok               |
|          30 | -15.25%  | 10.25%             | -56.59% |    -0.04 |       73 | 46.09%     | ok               |
|          15 | -23.11%  | 10.25%             | -57.94% |    -0.13 |       71 | 53.74%     | ok               |

## QQQ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 19.84%   | 61.15%             | -12.88% |     0.57 |       62 | 43.93%     | ok               |
|          25 | 20.29%   | 61.15%             | -12.88% |     0.57 |       59 | 46.59%     | ok               |
|          15 | 20.81%   | 61.15%             | -14.17% |     0.54 |       63 | 52.08%     | ok               |
|          20 | 17.38%   | 61.15%             | -12.98% |     0.49 |       67 | 49.25%     | ok               |
|          35 | 7.59%    | 61.15%             | -18.29% |     0.28 |       68 | 40.27%     | ok               |

## RENDER-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 45.25%   | -64.18%            | -43.43% |     0.61 |       88 | 53.71%     | ok               |
|          15 | 34.05%   | -64.18%            | -44.59% |     0.54 |       88 | 57.03%     | ok               |
|          25 | 15.90%   | -64.18%            | -40.60% |     0.42 |       90 | 49.41%     | ok               |
|          30 | -19.07%  | -64.18%            | -45.00% |     0.1  |       98 | 42.77%     | ok               |
|          35 | -31.74%  | -64.18%            | -41.33% |    -0.12 |       84 | 34.57%     | ok               |

## RTX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 32.86%   | 117.09%            | -18.66% |     0.76 |       74 | 56.24%     | ok               |
|          25 | 27.90%   | 117.09%            | -18.59% |     0.67 |       62 | 52.91%     | ok               |
|          35 | 23.23%   | 117.09%            | -18.00% |     0.65 |       52 | 49.75%     | ok               |
|          50 | 21.43%   | 117.09%            | -18.42% |     0.64 |       54 | 42.26%     | ok               |
|          30 | 25.96%   | 117.09%            | -16.99% |     0.64 |       56 | 51.75%     | ok               |

## SBUX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -12.57%  | 13.14%             | -23.55% |    -0.18 |       65 | 42.43%     | ok               |
|          40 | -16.92%  | 13.14%             | -25.43% |    -0.34 |       62 | 34.44%     | ok               |
|          45 | -16.46%  | 13.14%             | -27.26% |    -0.36 |       68 | 30.62%     | ok               |
|          30 | -20.04%  | 13.14%             | -29.22% |    -0.38 |       64 | 40.10%     | ok               |
|          35 | -21.61%  | 13.14%             | -28.06% |    -0.44 |       60 | 37.44%     | ok               |

## SCHW Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 11.06%   | 59.06%             | -16.53% |     0.37 |       56 | 35.11%     | ok               |
|          50 | 2.15%    | 59.06%             | -13.28% |     0.13 |       58 | 32.11%     | ok               |
|          25 | 0.59%    | 59.06%             | -28.76% |     0.11 |       61 | 50.08%     | ok               |
|          40 | -0.46%   | 59.06%             | -23.35% |     0.07 |       64 | 38.10%     | ok               |
|          20 | -3.64%   | 59.06%             | -29.24% |     0.01 |       71 | 52.41%     | ok               |

## SHIB-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -14.52%  | -73.51%            | -49.21% |     0.08 |       80 | 68.39%     | ok               |
|          20 | -25.25%  | -73.51%            | -46.38% |    -0.07 |       81 | 63.41%     | ok               |
|          25 | -25.94%  | -73.51%            | -43.85% |    -0.1  |       77 | 58.43%     | ok               |
|          35 | -26.26%  | -73.51%            | -53.32% |    -0.16 |       64 | 45.02%     | ok               |
|          40 | -30.32%  | -73.51%            | -50.74% |    -0.26 |       54 | 37.36%     | ok               |

## SHY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd    |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:-------|---------:|---------:|:-----------|:-----------------|
|          30 | -2.24%   | 0.45%              | -2.85% |    -0.79 |       48 | 34.28%     | ok               |
|          35 | -2.36%   | 0.45%              | -3.27% |    -0.84 |       50 | 32.45%     | ok               |
|          40 | -2.47%   | 0.45%              | -3.33% |    -0.89 |       50 | 30.62%     | ok               |
|          45 | -2.45%   | 0.45%              | -3.23% |    -0.9  |       48 | 27.45%     | ok               |
|          50 | -2.62%   | 0.45%              | -3.40% |    -1.01 |       44 | 24.63%     | ok               |

## SKY-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -28.04%  | 6.09%              | -43.98% |    -0.33 |       72 | 40.44%     | ok               |
|          15 | -32.44%  | 6.09%              | -56.39% |    -0.33 |       62 | 50.33%     | ok               |
|          25 | -31.73%  | 6.09%              | -48.09% |    -0.38 |       67 | 43.96%     | ok               |
|          20 | -42.13%  | 6.09%              | -58.40% |    -0.57 |       64 | 47.47%     | ok               |
|          35 | -37.92%  | 6.09%              | -49.68% |    -0.63 |       66 | 33.85%     | ok               |

## SLB Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 19.27%   | -4.43%             | -21.46% |     0.48 |       52 | 33.28%     | ok               |
|          40 | 15.58%   | -4.43%             | -25.33% |     0.41 |       46 | 36.77%     | ok               |
|          50 | -2.68%   | -4.43%             | -29.66% |     0.02 |       50 | 28.45%     | ok               |
|          35 | -12.19%  | -4.43%             | -43.52% |    -0.15 |       74 | 44.59%     | ok               |
|          30 | -23.87%  | -4.43%             | -54.23% |    -0.39 |       73 | 51.08%     | ok               |

## SLV Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 65.90%   | 142.03%            | -34.72% |     0.84 |       54 | 34.94%     | ok               |
|          45 | 63.89%   | 142.03%            | -32.46% |     0.82 |       60 | 36.11%     | ok               |
|          40 | 61.93%   | 142.03%            | -31.93% |     0.8  |       66 | 38.27%     | ok               |
|          20 | 56.04%   | 142.03%            | -42.66% |     0.73 |       66 | 47.09%     | ok               |
|          35 | 52.41%   | 142.03%            | -36.89% |     0.72 |       68 | 40.60%     | ok               |

## SMH Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 101.49%  | 171.00%            | -30.17% |     1.23 |       47 | 50.58%     | ok               |
|          35 | 80.32%   | 171.00%            | -34.36% |     1.1  |       54 | 46.42%     | ok               |
|          25 | 80.19%   | 171.00%            | -32.94% |     1.08 |       46 | 49.42%     | ok               |
|          30 | 78.07%   | 171.00%            | -33.99% |     1.07 |       48 | 47.75%     | ok               |
|          45 | 65.12%   | 171.00%            | -32.75% |     1.02 |       52 | 40.60%     | ok               |

## SNX-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -8.06%   | -76.26%            | -43.20% |     0.19 |       71 | 47.70%     | ok               |
|          35 | -6.26%   | -76.26%            | -30.08% |     0.17 |       62 | 30.84%     | ok               |
|          30 | -15.26%  | -76.26%            | -34.76% |     0.08 |       58 | 37.93%     | ok               |
|          40 | -18.26%  | -76.26%            | -40.36% |    -0.04 |       52 | 24.90%     | ok               |
|          15 | -38.08%  | -76.26%            | -47.56% |    -0.14 |       81 | 52.30%     | ok               |

## SOL-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 9.10%    | -61.95%            | -51.50% |     0.33 |       60 | 37.36%     | ok               |
|          25 | -21.17%  | -61.95%            | -52.40% |     0.04 |       76 | 57.09%     | ok               |
|          45 | -16.39%  | -61.95%            | -59.86% |     0.03 |       62 | 31.80%     | ok               |
|          35 | -22.95%  | -61.95%            | -61.91% |     0    |       76 | 45.21%     | ok               |
|          15 | -27.96%  | -61.95%            | -59.14% |    -0.02 |       76 | 63.41%     | ok               |

## SOXX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 86.91%   | 147.35%            | -38.67% |     1.08 |       53 | 49.25%     | ok               |
|          25 | 83.33%   | 147.35%            | -39.85% |     1.05 |       51 | 48.92%     | ok               |
|          35 | 78.21%   | 147.35%            | -38.63% |     1.03 |       59 | 44.26%     | ok               |
|          15 | 82.21%   | 147.35%            | -37.72% |     1.01 |       66 | 52.08%     | ok               |
|          30 | 73.03%   | 147.35%            | -40.34% |     0.97 |       55 | 46.76%     | ok               |

## SPY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 13.46%   | 47.93%             | -14.25% |     0.49 |       61 | 53.91%     | ok               |
|          15 | 11.91%   | 47.93%             | -16.80% |     0.43 |       70 | 57.07%     | ok               |
|          25 | 6.40%    | 47.93%             | -15.22% |     0.27 |       61 | 52.91%     | ok               |
|          30 | 1.90%    | 47.93%             | -16.47% |     0.13 |       64 | 50.08%     | ok               |
|          35 | 1.30%    | 47.93%             | -16.72% |     0.11 |       60 | 47.09%     | ok               |

## SUSHI-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -23.49%  | -81.30%            | -40.08% |    -0.19 |       52 | 14.75%     | ok               |
|          45 | -58.58%  | -81.30%            | -64.27% |    -0.77 |       56 | 18.20%     | ok               |
|          40 | -61.52%  | -81.30%            | -68.16% |    -0.77 |       63 | 24.71%     | ok               |
|          35 | -69.84%  | -81.30%            | -76.44% |    -0.93 |       82 | 30.46%     | ok               |
|          15 | -80.92%  | -81.30%            | -81.13% |    -1.06 |       93 | 48.08%     | ok               |

## T Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 59.42%   | 32.49%             | -18.13% |     1.14 |       58 | 57.40%     | ok               |
|          25 | 54.47%   | 32.49%             | -17.66% |     1.08 |       60 | 55.24%     | ok               |
|          15 | 50.71%   | 32.49%             | -15.08% |     0.99 |       67 | 61.23%     | ok               |
|          30 | 37.55%   | 32.49%             | -17.01% |     0.84 |       64 | 53.24%     | ok               |
|          35 | 23.40%   | 32.49%             | -14.49% |     0.6  |       66 | 49.75%     | ok               |

## TGT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -11.25%  | -6.74%             | -42.86% |    -0.11 |       83 | 46.76%     | ok               |
|          45 | -9.72%   | -6.74%             | -29.07% |    -0.15 |       54 | 28.95%     | ok               |
|          25 | -12.14%  | -6.74%             | -43.36% |    -0.16 |       65 | 41.76%     | ok               |
|          30 | -11.50%  | -6.74%             | -40.57% |    -0.16 |       60 | 38.94%     | ok               |
|          15 | -16.87%  | -6.74%             | -40.77% |    -0.21 |       73 | 51.41%     | ok               |

## TIA-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -0.93%   | -88.13%            | -48.57% |     0.18 |       54 | 18.77%     | ok               |
|          35 | -6.31%   | -88.13%            | -51.57% |     0.16 |       66 | 30.84%     | ok               |
|          40 | -5.92%   | -88.13%            | -44.45% |     0.15 |       68 | 26.05%     | ok               |
|          50 | -1.90%   | -88.13%            | -48.03% |     0.12 |       34 | 11.69%     | ok               |
|          30 | -44.48%  | -88.13%            | -67.47% |    -0.3  |       91 | 36.40%     | ok               |

## TLT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -21.42%  | -9.09%             | -21.82% |    -1.66 |       72 | 32.28%     | ok               |
|          50 | -14.77%  | -9.09%             | -15.73% |    -1.75 |       34 | 14.81%     | ok               |
|          40 | -19.61%  | -9.09%             | -19.86% |    -1.9  |       58 | 21.80%     | ok               |
|          15 | -27.18%  | -9.09%             | -27.72% |    -1.92 |       77 | 40.27%     | ok               |
|          35 | -22.18%  | -9.09%             | -22.42% |    -1.96 |       66 | 26.46%     | ok               |

## TMO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 51.13%   | -3.09%             | -8.17%  |     1.12 |       40 | 32.11%     | ok               |
|          45 | 46.74%   | -3.09%             | -10.13% |     0.99 |       46 | 36.94%     | ok               |
|          40 | 44.58%   | -3.09%             | -9.91%  |     0.94 |       49 | 41.43%     | ok               |
|          35 | 26.17%   | -3.09%             | -14.06% |     0.61 |       61 | 45.92%     | ok               |
|          30 | 17.61%   | -3.09%             | -18.85% |     0.44 |       61 | 50.75%     | ok               |

## TMUS Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 7.91%    | 17.92%             | -30.05% |     0.26 |       65 | 60.07%     | ok               |
|          30 | 6.71%    | 17.92%             | -25.71% |     0.24 |       70 | 48.09%     | ok               |
|          20 | 1.69%    | 17.92%             | -29.75% |     0.14 |       71 | 54.41%     | ok               |
|          25 | -1.72%   | 17.92%             | -31.45% |     0.06 |       75 | 50.58%     | ok               |
|          50 | -3.56%   | 17.92%             | -28.89% |    -0.02 |       60 | 36.11%     | ok               |

## TRX-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 6.87%    | 33.57%             | -18.79% |     0.28 |       52 | 37.16%     | ok               |
|          30 | 3.17%    | 33.57%             | -22.90% |     0.17 |       70 | 48.85%     | ok               |
|          35 | 2.31%    | 33.57%             | -21.77% |     0.15 |       66 | 45.59%     | ok               |
|          20 | 2.01%    | 33.57%             | -25.45% |     0.15 |       63 | 55.75%     | ok               |
|          25 | 1.31%    | 33.57%             | -26.84% |     0.13 |       66 | 52.11%     | ok               |

## TSLA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 56.12%   | 98.10%             | -32.60% |     0.73 |       64 | 29.78%     | ok               |
|          40 | 35.10%   | 98.10%             | -45.90% |     0.52 |       63 | 34.61%     | ok               |
|          45 | 14.45%   | 98.10%             | -46.86% |     0.34 |       67 | 31.95%     | ok               |
|          35 | 3.29%    | 98.10%             | -51.29% |     0.23 |       72 | 37.27%     | ok               |
|          30 | -14.59%  | 98.10%             | -54.91% |     0.05 |       70 | 41.26%     | ok               |

## TXN Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 16.55%   | 76.04%             | -45.45% |     0.38 |       66 | 34.78%     | ok               |
|          20 | 2.93%    | 76.04%             | -38.49% |     0.19 |       60 | 59.07%     | ok               |
|          35 | 0.10%    | 76.04%             | -43.28% |     0.14 |       74 | 49.58%     | ok               |
|          15 | -2.95%   | 76.04%             | -38.99% |     0.12 |       65 | 62.90%     | ok               |
|          40 | -1.97%   | 76.04%             | -45.67% |     0.1  |       68 | 47.09%     | ok               |

## UNH Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 31.58%   | -19.59%            | -26.96% |     0.54 |       74 | 52.41%     | ok               |
|          15 | 32.07%   | -19.59%            | -32.14% |     0.52 |       74 | 67.22%     | ok               |
|          35 | 27.99%   | -19.59%            | -28.32% |     0.5  |       66 | 47.25%     | ok               |
|          50 | 24.65%   | -19.59%            | -36.82% |     0.48 |       56 | 30.95%     | ok               |
|          40 | 20.04%   | -19.59%            | -35.73% |     0.41 |       60 | 42.76%     | ok               |

## UNI-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -21.35%  | -61.99%            | -58.49% |    -0.04 |       56 | 27.59%     | ok               |
|          40 | -26.71%  | -61.99%            | -63.75% |    -0.09 |       60 | 32.76%     | ok               |
|          50 | -29.10%  | -61.99%            | -57.60% |    -0.19 |       54 | 21.46%     | ok               |
|          35 | -39.15%  | -61.99%            | -68.71% |    -0.23 |       72 | 38.12%     | ok               |
|          30 | -73.61%  | -61.99%            | -80.61% |    -0.9  |       88 | 44.06%     | ok               |

## UPS Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -31.90%  | -21.74%            | -43.07% |    -0.57 |       80 | 47.75%     | ok               |
|          25 | -32.99%  | -21.74%            | -39.04% |    -0.61 |       76 | 44.26%     | ok               |
|          35 | -31.68%  | -21.74%            | -37.47% |    -0.62 |       61 | 33.11%     | ok               |
|          15 | -35.37%  | -21.74%            | -43.86% |    -0.65 |       86 | 52.41%     | ok               |
|          30 | -35.34%  | -21.74%            | -37.08% |    -0.7  |       68 | 39.10%     | ok               |

## USO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 14.84%   | 62.09%             | -33.25% |     0.36 |       50 | 26.46%     | ok               |
|          20 | 13.08%   | 62.09%             | -45.57% |     0.32 |       75 | 39.43%     | ok               |
|          15 | 7.74%    | 62.09%             | -45.74% |     0.25 |       74 | 42.60%     | ok               |
|          30 | 7.06%    | 62.09%             | -43.35% |     0.24 |       68 | 33.94%     | ok               |
|          25 | 4.20%    | 62.09%             | -44.86% |     0.2  |       69 | 36.94%     | ok               |

## VEA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 5.81%    | 43.59%             | -15.98% |     0.26 |       60 | 50.42%     | ok               |
|          20 | 1.55%    | 43.59%             | -17.41% |     0.11 |       61 | 47.75%     | ok               |
|          25 | -0.47%   | 43.59%             | -17.50% |     0.03 |       57 | 46.09%     | ok               |
|          30 | -0.98%   | 43.59%             | -17.93% |     0.01 |       58 | 44.09%     | ok               |
|          35 | -2.09%   | 43.59%             | -16.79% |    -0.03 |       56 | 43.09%     | ok               |

## VIXY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -48.04%  | -64.31%            | -69.78% |    -0.43 |       46 | 10.48%     | ok               |
|          45 | -59.37%  | -64.31%            | -75.03% |    -0.61 |       60 | 16.64%     | ok               |
|          40 | -67.66%  | -64.31%            | -80.72% |    -0.74 |       76 | 21.46%     | ok               |
|          15 | -76.43%  | -64.31%            | -89.47% |    -0.75 |       99 | 44.59%     | ok               |
|          35 | -70.62%  | -64.31%            | -84.37% |    -0.76 |       90 | 26.79%     | ok               |

## VNQ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -7.76%   | 17.94%             | -19.07% |    -0.33 |       58 | 28.29%     | ok               |
|          50 | -8.20%   | 17.94%             | -17.13% |    -0.37 |       54 | 25.79%     | ok               |
|          25 | -12.17%  | 17.94%             | -22.34% |    -0.47 |       67 | 40.27%     | ok               |
|          20 | -13.78%  | 17.94%             | -23.79% |    -0.52 |       70 | 42.93%     | ok               |
|          15 | -15.09%  | 17.94%             | -24.90% |    -0.57 |       67 | 44.09%     | ok               |

## VTI Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 16.50%   | 47.15%             | -13.96% |     0.57 |       64 | 54.41%     | ok               |
|          15 | 10.53%   | 47.15%             | -15.70% |     0.39 |       67 | 56.91%     | ok               |
|          25 | 3.03%    | 47.15%             | -16.10% |     0.17 |       60 | 52.41%     | ok               |
|          30 | -4.69%   | 47.15%             | -18.77% |    -0.11 |       70 | 50.42%     | ok               |
|          35 | -7.09%   | 47.15%             | -20.89% |    -0.21 |       64 | 47.25%     | ok               |

## VWO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -10.40%  | 41.54%             | -24.01% |    -0.31 |       71 | 49.25%     | ok               |
|          50 | -8.77%   | 41.54%             | -21.68% |    -0.32 |       60 | 32.11%     | ok               |
|          40 | -9.86%   | 41.54%             | -23.57% |    -0.35 |       70 | 37.60%     | ok               |
|          20 | -11.42%  | 41.54%             | -26.14% |    -0.36 |       69 | 47.09%     | ok               |
|          45 | -10.55%  | 41.54%             | -23.75% |    -0.39 |       62 | 34.61%     | ok               |

## VZ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -6.80%   | 7.73%              | -12.71% |    -0.19 |       50 | 24.29%     | ok               |
|          45 | -17.93%  | 7.73%              | -20.96% |    -0.59 |       64 | 27.95%     | ok               |
|          35 | -21.19%  | 7.73%              | -22.23% |    -0.69 |       61 | 34.11%     | ok               |
|          25 | -23.88%  | 7.73%              | -23.83% |    -0.7  |       79 | 42.10%     | ok               |
|          40 | -25.47%  | 7.73%              | -25.47% |    -0.89 |       66 | 31.28%     | ok               |

## WFC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -2.20%   | 65.02%             | -18.29% |    -0    |       60 | 35.44%     | ok               |
|          35 | -5.77%   | 65.02%             | -23.64% |    -0.04 |       81 | 47.42%     | ok               |
|          20 | -12.06%  | 65.02%             | -29.43% |    -0.13 |       79 | 56.91%     | ok               |
|          45 | -9.08%   | 65.02%             | -23.40% |    -0.19 |       68 | 40.10%     | ok               |
|          40 | -10.39%  | 65.02%             | -24.26% |    -0.22 |       76 | 43.59%     | ok               |

## WIF-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 60.57%   | -75.63%            | -46.21% |     0.66 |       73 | 41.76%     | ok               |
|          20 | 54.89%   | -75.63%            | -40.67% |     0.64 |       67 | 39.08%     | ok               |
|          25 | 2.03%    | -75.63%            | -45.19% |     0.31 |       69 | 36.40%     | ok               |
|          50 | -12.13%  | -75.63%            | -33.04% |    -0.02 |       38 | 11.69%     | ok               |
|          30 | -35.32%  | -75.63%            | -50.56% |    -0.13 |       70 | 32.38%     | ok               |

## WMT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 48.61%   | 96.60%             | -9.18%  |     1.33 |       38 | 41.93%     | ok               |
|          50 | 41.37%   | 96.60%             | -12.19% |     1.23 |       34 | 39.60%     | ok               |
|          40 | 36.28%   | 96.60%             | -12.47% |     1.03 |       44 | 43.26%     | ok               |
|          35 | 35.39%   | 96.60%             | -13.05% |     0.98 |       54 | 47.92%     | ok               |
|          15 | 15.19%   | 96.60%             | -25.74% |     0.42 |       70 | 61.40%     | ok               |

## XBI Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 6.11%    | 61.44%             | -16.56% |     0.23 |       60 | 36.11%     | ok               |
|          45 | 5.29%    | 61.44%             | -16.74% |     0.21 |       52 | 32.95%     | ok               |
|          35 | 1.98%    | 61.44%             | -18.84% |     0.13 |       62 | 39.43%     | ok               |
|          30 | 0.85%    | 61.44%             | -19.80% |     0.11 |       62 | 41.10%     | ok               |
|          25 | -1.60%   | 61.44%             | -23.66% |     0.05 |       72 | 43.43%     | ok               |

## XLB Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -1.68%   | 17.91%             | -20.68% |    -0.01 |       54 | 31.61%     | ok               |
|          50 | -1.74%   | 17.91%             | -17.59% |    -0.02 |       42 | 27.29%     | ok               |
|          35 | -4.92%   | 17.91%             | -23.62% |    -0.13 |       56 | 34.94%     | ok               |
|          45 | -4.65%   | 17.91%             | -20.79% |    -0.14 |       42 | 28.79%     | ok               |
|          25 | -8.37%   | 17.91%             | -23.87% |    -0.25 |       62 | 40.43%     | ok               |

## XLC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 10.08%   | 40.95%             | -12.33% |     0.39 |       69 | 54.24%     | ok               |
|          25 | 6.91%    | 40.95%             | -12.31% |     0.28 |       68 | 56.24%     | ok               |
|          40 | 6.31%    | 40.95%             | -13.38% |     0.28 |       70 | 46.76%     | ok               |
|          35 | 5.71%    | 40.95%             | -13.38% |     0.26 |       66 | 51.08%     | ok               |
|          20 | -0.42%   | 40.95%             | -13.78% |     0.06 |       74 | 59.07%     | ok               |

## XLE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 5.59%    | 31.79%             | -25.98% |     0.23 |       54 | 36.11%     | ok               |
|          45 | 1.26%    | 31.79%             | -29.68% |     0.11 |       60 | 38.10%     | ok               |
|          35 | -0.87%   | 31.79%             | -31.51% |     0.06 |       65 | 42.76%     | ok               |
|          25 | -7.44%   | 31.79%             | -36.05% |    -0.1  |       83 | 48.25%     | ok               |
|          40 | -7.33%   | 31.79%             | -34.51% |    -0.13 |       64 | 40.60%     | ok               |

## XLF Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -3.46%   | 41.52%             | -18.01% |    -0.05 |       68 | 53.91%     | ok               |
|          15 | -7.46%   | 41.52%             | -19.58% |    -0.19 |       76 | 56.74%     | ok               |
|          25 | -10.20%  | 41.52%             | -23.22% |    -0.31 |       77 | 50.42%     | ok               |
|          30 | -10.63%  | 41.52%             | -23.61% |    -0.34 |       78 | 48.09%     | ok               |
|          35 | -17.80%  | 41.52%             | -27.24% |    -0.7  |       68 | 43.93%     | ok               |

## XLI Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 3.93%    | 50.64%             | -10.36% |     0.2  |       74 | 51.41%     | ok               |
|          20 | -0.02%   | 50.64%             | -12.74% |     0.05 |       65 | 46.76%     | ok               |
|          30 | -2.21%   | 50.64%             | -11.79% |    -0.04 |       66 | 44.26%     | ok               |
|          45 | -2.87%   | 50.64%             | -14.01% |    -0.08 |       64 | 35.94%     | ok               |
|          25 | -3.40%   | 50.64%             | -12.51% |    -0.08 |       64 | 45.09%     | ok               |

## XLK Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 87.25%   | 72.54%             | -14.75% |     1.38 |       39 | 50.92%     | ok               |
|          20 | 71.51%   | 72.54%             | -14.75% |     1.23 |       46 | 48.92%     | ok               |
|          25 | 68.02%   | 72.54%             | -14.75% |     1.23 |       40 | 46.76%     | ok               |
|          30 | 65.83%   | 72.54%             | -14.75% |     1.22 |       40 | 45.59%     | ok               |
|          35 | 47.33%   | 72.54%             | -13.61% |     0.99 |       52 | 42.93%     | ok               |

## XLM-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 26.14%   | -41.96%            | -38.97% |     0.48 |       44 | 27.39%     | ok               |
|          45 | 22.34%   | -41.96%            | -43.99% |     0.44 |       50 | 31.03%     | ok               |
|          30 | 5.21%    | -41.96%            | -50.36% |     0.28 |       69 | 45.79%     | ok               |
|          40 | 1.75%    | -41.96%            | -43.80% |     0.23 |       49 | 35.44%     | ok               |
|          35 | -4.00%   | -41.96%            | -50.42% |     0.17 |       69 | 41.76%     | ok               |

## XLP Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 8.02%    | 15.10%             | -6.85%  |     0.52 |       56 | 32.78%     | ok               |
|          40 | 7.33%    | 15.10%             | -7.77%  |     0.46 |       70 | 37.10%     | ok               |
|          50 | 6.68%    | 15.10%             | -7.01%  |     0.45 |       56 | 30.62%     | ok               |
|          35 | 6.40%    | 15.10%             | -9.73%  |     0.4  |       66 | 40.10%     | ok               |
|          30 | 4.51%    | 15.10%             | -11.16% |     0.29 |       68 | 41.60%     | ok               |

## XLU Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 5.85%    | 47.82%             | -12.97% |     0.32 |       52 | 31.28%     | ok               |
|          45 | 4.45%    | 47.82%             | -14.27% |     0.25 |       54 | 32.28%     | ok               |
|          40 | 1.57%    | 47.82%             | -15.59% |     0.12 |       58 | 33.78%     | ok               |
|          35 | -4.35%   | 47.82%             | -19.71% |    -0.16 |       62 | 35.94%     | ok               |
|          30 | -5.24%   | 47.82%             | -20.40% |    -0.19 |       67 | 39.10%     | ok               |

## XLV Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -14.74%  | 9.95%              | -19.97% |    -0.72 |       68 | 36.11%     | ok               |
|          25 | -15.99%  | 9.95%              | -21.14% |    -0.78 |       70 | 37.44%     | ok               |
|          15 | -19.80%  | 9.95%              | -24.43% |    -0.96 |       81 | 42.26%     | ok               |
|          20 | -19.74%  | 9.95%              | -24.51% |    -0.98 |       75 | 39.10%     | ok               |
|          35 | -19.19%  | 9.95%              | -23.94% |    -1.03 |       66 | 33.61%     | ok               |

## XLY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 5.14%    | 28.87%             | -12.94% |     0.23 |       70 | 41.43%     | ok               |
|          30 | 3.26%    | 28.87%             | -14.01% |     0.17 |       70 | 44.43%     | ok               |
|          50 | 1.64%    | 28.87%             | -11.49% |     0.12 |       50 | 29.45%     | ok               |
|          15 | 1.20%    | 28.87%             | -15.77% |     0.11 |       74 | 51.25%     | ok               |
|          45 | -1.43%   | 28.87%             | -13.48% |    -0    |       54 | 32.11%     | ok               |

## XOM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | 5.55%    | 39.32%             | -19.90% |     0.23 |       57 | 37.94%     | ok               |
|          50 | 4.96%    | 39.32%             | -21.35% |     0.22 |       40 | 29.28%     | ok               |
|          30 | 4.95%    | 39.32%             | -20.29% |     0.21 |       57 | 36.61%     | ok               |
|          20 | -0.45%   | 39.32%             | -25.56% |     0.06 |       64 | 40.27%     | ok               |
|          35 | -2.04%   | 39.32%             | -20.93% |     0.01 |       57 | 35.44%     | ok               |

## XRP-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | -25.11%  | -54.67%            | -46.87% |    -0.14 |       68 | 39.85%     | ok               |
|          40 | -30.47%  | -54.67%            | -44.89% |    -0.26 |       58 | 33.72%     | ok               |
|          30 | -37.23%  | -54.67%            | -54.70% |    -0.33 |       70 | 44.06%     | ok               |
|          45 | -38.24%  | -54.67%            | -46.06% |    -0.42 |       58 | 29.50%     | ok               |
|          50 | -34.88%  | -54.67%            | -38.03% |    -0.46 |       60 | 22.03%     | ok               |

## YFI-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -49.62%  | -62.67%            | -50.02% |    -0.82 |       62 | 27.20%     | ok               |
|          45 | -46.03%  | -62.67%            | -51.53% |    -0.92 |       68 | 21.26%     | ok               |
|          30 | -66.24%  | -62.67%            | -70.70% |    -1.11 |       83 | 40.61%     | ok               |
|          35 | -63.93%  | -62.67%            | -63.64% |    -1.11 |       73 | 34.48%     | ok               |
|          25 | -69.67%  | -62.67%            | -71.93% |    -1.19 |       77 | 45.59%     | ok               |

## ZEC-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 111.25%  | 1529.43%           | -24.66% |     0.85 |       46 | 23.56%     | ok               |
|          35 | 81.37%   | 1529.43%           | -44.34% |     0.72 |       54 | 30.08%     | ok               |
|          25 | 61.47%   | 1529.43%           | -48.59% |     0.64 |       60 | 39.27%     | ok               |
|          30 | 45.49%   | 1529.43%           | -47.68% |     0.57 |       64 | 35.82%     | ok               |
|          50 | 45.21%   | 1529.43%           | -34.39% |     0.55 |       48 | 21.07%     | ok               |
