# Market Tracker Backtest Report

_Generated: 2026-11-19T07:14:31+00:00_

## Data Sources

- Crypto: Kraken -> Coinbase -> CoinGecko OHLC -> CoinPaprika fallback chain.
- Stocks / ETFs / indices: Stooq -> Yahoo Finance fallback chain.
- Data rows are generated from real market APIs. Mock OHLCV rows are not generated.

## Data Freshness

- Rows: **92,800**
- Symbols: **161**
- Date range: **2024-06-28** to **2026-11-19**

## Latest Signals

| symbol     | date                |         close |   composite_score | signal   | data_source   |
|:-----------|:--------------------|--------------:|------------------:|:---------|:--------------|
| CL         | 2026-11-18 00:00:00 |    98.85      |          60.9167  | LONG     | Yahoo Finance |
| CMCSA      | 2026-11-18 00:00:00 |    25.24      |          34.8333  | LONG     | Yahoo Finance |
| COST       | 2026-11-18 00:00:00 |  1096.62      |          59.5833  | LONG     | Yahoo Finance |
| DIS        | 2026-11-18 00:00:00 |   122.36      |          79.25    | LONG     | Yahoo Finance |
| DXY-INDEX  | 2026-11-19 00:00:00 |   103.862     |          82.2581  | LONG     | Yahoo Finance |
| GE         | 2026-11-18 00:00:00 |   328.1       |          67.1667  | LONG     | Yahoo Finance |
| HD         | 2026-11-18 00:00:00 |   337.64      |          48.5833  | LONG     | Yahoo Finance |
| KO         | 2026-11-18 00:00:00 |    98.09      |          73.0833  | LONG     | Yahoo Finance |
| LLY        | 2026-11-18 00:00:00 |  1382.75      |          48.0833  | LONG     | Yahoo Finance |
| MCD        | 2026-11-18 00:00:00 |   274.03      |          46.8333  | LONG     | Yahoo Finance |
| PEP        | 2026-11-18 00:00:00 |   141.87      |          61.8333  | LONG     | Yahoo Finance |
| PG         | 2026-11-18 00:00:00 |   170.29      |          71.0833  | LONG     | Yahoo Finance |
| SBUX       | 2026-11-18 00:00:00 |   109.11      |          36.0833  | LONG     | Yahoo Finance |
| TGT        | 2026-11-18 00:00:00 |   165.93      |          82.5833  | LONG     | Yahoo Finance |
| UPS        | 2026-11-18 00:00:00 |   111.03      |          36.0833  | LONG     | Yahoo Finance |
| VNQ        | 2026-11-18 00:00:00 |    95.18      |          39.8333  | LONG     | Yahoo Finance |
| WMT        | 2026-11-18 00:00:00 |   127.36      |          34.0833  | LONG     | Yahoo Finance |
| XLP        | 2026-11-18 00:00:00 |    91.18      |          37.75    | LONG     | Yahoo Finance |
| XLU        | 2026-11-18 00:00:00 |    43.55      |          41.8333  | LONG     | Yahoo Finance |
| XLY        | 2026-11-18 00:00:00 |   119.2       |          45.5833  | LONG     | Yahoo Finance |
| AAPL       | 2026-11-18 00:00:00 |   352.45      |          57.8333  | NEUTRAL  | Yahoo Finance |
| ABBV       | 2026-11-18 00:00:00 |   286.01      |          12.1667  | NEUTRAL  | Yahoo Finance |
| ADBE       | 2026-11-18 00:00:00 |   226.2       |         -48.6667  | NEUTRAL  | Yahoo Finance |
| AMD        | 2026-11-18 00:00:00 |   530.14      |          14.8333  | NEUTRAL  | Yahoo Finance |
| AMGN       | 2026-11-18 00:00:00 |   443.89      |          15.9167  | NEUTRAL  | Yahoo Finance |
| AMZN       | 2026-11-18 00:00:00 |   267.74      |          67.8333  | NEUTRAL  | Yahoo Finance |
| ARB-USD    | 2026-11-19 00:00:00 |     0.1278    |         -61.9167  | NEUTRAL  | Kraken API    |
| ATOM-USD   | 2026-11-19 00:00:00 |     1.3221    |         -17       | NEUTRAL  | Kraken API    |
| AVAX-USD   | 2026-11-19 00:00:00 |     7.062     |         -54.25    | NEUTRAL  | Kraken API    |
| AVGO       | 2026-11-18 00:00:00 |   354.05      |          16.1667  | NEUTRAL  | Yahoo Finance |
| BAC        | 2026-11-18 00:00:00 |    48.91      |         -46.6667  | NEUTRAL  | Yahoo Finance |
| BLK        | 2026-11-18 00:00:00 |  1169.21      |          23.9167  | NEUTRAL  | Yahoo Finance |
| C          | 2026-11-18 00:00:00 |   117.34      |         -65       | NEUTRAL  | Yahoo Finance |
| COP        | 2026-11-18 00:00:00 |   134.4       |         -14       | NEUTRAL  | Yahoo Finance |
| DE         | 2026-11-18 00:00:00 |   644.75      |         -12.0833  | NEUTRAL  | Yahoo Finance |
| DIA        | 2026-11-18 00:00:00 |   501.73      |         -41.25    | NEUTRAL  | Yahoo Finance |
| EFA        | 2026-11-18 00:00:00 |   100.26      |         -61.75    | NEUTRAL  | Yahoo Finance |
| EOG        | 2026-11-18 00:00:00 |   149.69      |           1.66667 | NEUTRAL  | Yahoo Finance |
| FET-USD    | 2026-11-19 00:00:00 |     0.13      |         -19       | NEUTRAL  | Kraken API    |
| GDX        | 2026-11-18 00:00:00 |    74.82      |         -63.75    | NEUTRAL  | Yahoo Finance |
| GDXJ       | 2026-11-18 00:00:00 |    90.07      |         -63.75    | NEUTRAL  | Yahoo Finance |
| GLD        | 2026-11-18 00:00:00 |   341.19      |         -64.5     | NEUTRAL  | Yahoo Finance |
| GOOGL      | 2026-11-18 00:00:00 |   282.44      |         -23.75    | NEUTRAL  | Yahoo Finance |
| GRT-USD    | 2026-11-19 00:00:00 |     0.01741   |         -19       | NEUTRAL  | Kraken API    |
| GS         | 2026-11-18 00:00:00 |   873.18      |         -64.5     | NEUTRAL  | Yahoo Finance |
| HBAR-USD   | 2026-11-19 00:00:00 |     0.0557    |         -62.9167  | NEUTRAL  | Kraken API    |
| HON        | 2026-11-18 00:00:00 |   222.7       |          -5.91667 | NEUTRAL  | Yahoo Finance |
| HYG        | 2026-11-18 00:00:00 |    76.65      |         -60.5     | NEUTRAL  | Yahoo Finance |
| ICP-USD    | 2026-11-19 00:00:00 |     2.28      |         -47.25    | NEUTRAL  | Kraken API    |
| INJ-USD    | 2026-11-19 00:00:00 |     7.148     |         -25       | NEUTRAL  | Kraken API    |
| INTU       | 2026-11-18 00:00:00 |   313.24      |         -21.5833  | NEUTRAL  | Yahoo Finance |
| ITA        | 2026-11-18 00:00:00 |    69.39      |         -48.8333  | NEUTRAL  | Yahoo Finance |
| IWM        | 2026-11-18 00:00:00 |   270.12      |         -58.75    | NEUTRAL  | Yahoo Finance |
| JNJ        | 2026-11-18 00:00:00 |   272.7       |           5.41667 | NEUTRAL  | Yahoo Finance |
| JPM        | 2026-11-18 00:00:00 |   324.11      |         -43.25    | NEUTRAL  | Yahoo Finance |
| LIN        | 2026-11-18 00:00:00 |   512.16      |          14.5833  | NEUTRAL  | Yahoo Finance |
| META       | 2026-11-18 00:00:00 |   616.38      |         -17       | NEUTRAL  | Yahoo Finance |
| MPC        | 2026-11-18 00:00:00 |   373.86      |         -16.3333  | NEUTRAL  | Yahoo Finance |
| MRK        | 2026-11-18 00:00:00 |   137.78      |         -14       | NEUTRAL  | Yahoo Finance |
| MS         | 2026-11-18 00:00:00 |   181.17      |         -42.1667  | NEUTRAL  | Yahoo Finance |
| MSFT       | 2026-11-18 00:00:00 |   508.29      |         -24.8333  | NEUTRAL  | Yahoo Finance |
| NEAR-USD   | 2026-11-19 00:00:00 |     3.4174    |           7.75    | NEUTRAL  | Kraken API    |
| NEM        | 2026-11-18 00:00:00 |   104.53      |         -62       | NEUTRAL  | Yahoo Finance |
| NFLX       | 2026-11-18 00:00:00 |    59.82      |         -50.3333  | NEUTRAL  | Yahoo Finance |
| NKE        | 2026-11-18 00:00:00 |    36.31      |         -28.5833  | NEUTRAL  | Yahoo Finance |
| ORCL       | 2026-11-18 00:00:00 |   113.89      |         -61.25    | NEUTRAL  | Yahoo Finance |
| PFE        | 2026-11-18 00:00:00 |    28.06      |         -25.25    | NEUTRAL  | Yahoo Finance |
| PM         | 2026-11-18 00:00:00 |   192.73      |         -31.8333  | NEUTRAL  | Yahoo Finance |
| QCOM       | 2026-11-18 00:00:00 |   159.81      |         -58       | NEUTRAL  | Yahoo Finance |
| RENDER-USD | 2026-11-19 00:00:00 |     1.437     |         -43.25    | NEUTRAL  | Kraken API    |
| RTX        | 2026-11-18 00:00:00 |   197.45      |          14.4167  | NEUTRAL  | Yahoo Finance |
| SCHW       | 2026-11-18 00:00:00 |    92.56      |          22.4167  | NEUTRAL  | Yahoo Finance |
| SHY        | 2026-11-18 00:00:00 |    81.34      |         -56.25    | NEUTRAL  | Yahoo Finance |
| SNX-USD    | 2026-11-19 00:00:00 |     0.1591    |         -11       | NEUTRAL  | Kraken API    |
| SPY        | 2026-11-18 00:00:00 |   730.2       |         -53.5     | NEUTRAL  | Yahoo Finance |
| T          | 2026-11-18 00:00:00 |    21.95      |         -21.0833  | NEUTRAL  | Yahoo Finance |
| TMO        | 2026-11-18 00:00:00 |   692.74      |          -1.83333 | NEUTRAL  | Yahoo Finance |
| TMUS       | 2026-11-18 00:00:00 |   164.02      |          15.9167  | NEUTRAL  | Yahoo Finance |
| TSLA       | 2026-11-18 00:00:00 |   383.72      |           7.16667 | NEUTRAL  | Yahoo Finance |
| TXN        | 2026-11-18 00:00:00 |   292.43      |         -14.8333  | NEUTRAL  | Yahoo Finance |
| UNH        | 2026-11-18 00:00:00 |   349.91      |         -48.3333  | NEUTRAL  | Yahoo Finance |
| VEA        | 2026-11-18 00:00:00 |    66.68      |         -63.75    | NEUTRAL  | Yahoo Finance |
| VIXY       | 2026-11-18 00:00:00 |    20.4       |          26.4167  | NEUTRAL  | Yahoo Finance |
| VTI        | 2026-11-18 00:00:00 |   359.48      |         -53.5     | NEUTRAL  | Yahoo Finance |
| VZ         | 2026-11-18 00:00:00 |    46.13      |          43.25    | NEUTRAL  | Yahoo Finance |
| WFC        | 2026-11-18 00:00:00 |    80.92      |         -25.3333  | NEUTRAL  | Yahoo Finance |
| XBI        | 2026-11-18 00:00:00 |   145.04      |         -44.5     | NEUTRAL  | Yahoo Finance |
| XLC        | 2026-11-18 00:00:00 |   105.58      |         -15.5833  | NEUTRAL  | Yahoo Finance |
| XLF        | 2026-11-18 00:00:00 |    56.42      |           7.41667 | NEUTRAL  | Yahoo Finance |
| XLI        | 2026-11-18 00:00:00 |   164.66      |         -64.5     | NEUTRAL  | Yahoo Finance |
| XLV        | 2026-11-18 00:00:00 |   181.17      |          21.6667  | NEUTRAL  | Yahoo Finance |
| ZEC-USD    | 2026-11-19 00:00:00 |   939.86      |         -24.5833  | NEUTRAL  | Kraken API    |
| AAVE-USD   | 2026-11-19 00:00:00 |   109.38      |         -44.5833  | SHORT    | Kraken API    |
| ADA-USD    | 2026-11-19 00:00:00 |     0.153764  |         -46.3333  | SHORT    | Kraken API    |
| AGG        | 2026-11-18 00:00:00 |    95.53      |         -46.75    | SHORT    | Yahoo Finance |
| ALGO-USD   | 2026-11-19 00:00:00 |     0.07777   |         -51.6667  | SHORT    | Kraken API    |
| AMAT       | 2026-11-18 00:00:00 |   352.3       |         -36.9167  | SHORT    | Yahoo Finance |
| APT-USD    | 2026-11-19 00:00:00 |     0.4339    |         -57.3333  | SHORT    | Kraken API    |
| ARKK       | 2026-11-18 00:00:00 |    71.06      |         -49.3333  | SHORT    | Yahoo Finance |
| BA         | 2026-11-18 00:00:00 |   162.91      |         -48.25    | SHORT    | Yahoo Finance |
| BCH-USD    | 2026-11-19 00:00:00 |   207.18      |         -53.3333  | SHORT    | Kraken API    |
| BITO       | 2026-11-18 00:00:00 |     8.31      |         -50.0833  | SHORT    | Yahoo Finance |
| BND        | 2026-11-18 00:00:00 |    70.87      |         -46.75    | SHORT    | Yahoo Finance |
| BONK-USD   | 2026-11-19 00:00:00 |     2.371e-06 |         -44.5833  | SHORT    | Kraken API    |
| BTC-USD    | 2026-11-19 00:00:00 | 63691.3       |         -47.6667  | SHORT    | Kraken API    |
| CAT        | 2026-11-18 00:00:00 |   558.77      |         -37.4167  | SHORT    | Yahoo Finance |
| COMP-USD   | 2026-11-19 00:00:00 |    18.05      |         -30       | SHORT    | Kraken API    |
| CRM        | 2026-11-18 00:00:00 |   190.4       |         -49.5833  | SHORT    | Yahoo Finance |
| CRV-USD    | 2026-11-19 00:00:00 |     0.19818   |         -43.3333  | SHORT    | Kraken API    |
| CSCO       | 2026-11-18 00:00:00 |    97.18      |         -46.5     | SHORT    | Yahoo Finance |
| CVX        | 2026-11-18 00:00:00 |   205.88      |         -35.3333  | SHORT    | Yahoo Finance |
| DASH-USD   | 2026-11-19 00:00:00 |    37.07      |         -49       | SHORT    | Kraken API    |
| DBC        | 2026-11-18 00:00:00 |    29.51      |         -55.8333  | SHORT    | Yahoo Finance |
| DOGE-USD   | 2026-11-19 00:00:00 |     0.0594639 |         -49.6667  | SHORT    | Kraken API    |
| DOT-USD    | 2026-11-19 00:00:00 |     0.72      |         -51.6667  | SHORT    | Kraken API    |
| EEM        | 2026-11-18 00:00:00 |    57.88      |         -48.25    | SHORT    | Yahoo Finance |
| ETC-USD    | 2026-11-19 00:00:00 |     5.948     |         -46.3333  | SHORT    | Kraken API    |
| ETH-USD    | 2026-11-19 00:00:00 |  1806.42      |         -47.8333  | SHORT    | Kraken API    |
| EWJ        | 2026-11-18 00:00:00 |    88.04      |         -52.75    | SHORT    | Yahoo Finance |
| FCX        | 2026-11-18 00:00:00 |    51.45      |         -62.3333  | SHORT    | Yahoo Finance |
| FIL-USD    | 2026-11-19 00:00:00 |     0.572     |         -57.3333  | SHORT    | Kraken API    |
| FXI        | 2026-11-18 00:00:00 |    32.39      |         -30.25    | SHORT    | Yahoo Finance |
| IBIT       | 2026-11-18 00:00:00 |    35.36      |         -50.0833  | SHORT    | Yahoo Finance |
| IBM        | 2026-11-18 00:00:00 |   228.53      |         -38.5833  | SHORT    | Yahoo Finance |
| IEF        | 2026-11-18 00:00:00 |    90.67      |         -46.75    | SHORT    | Yahoo Finance |
| IEMG       | 2026-11-18 00:00:00 |    70.57      |         -48.25    | SHORT    | Yahoo Finance |
| INTC       | 2026-11-18 00:00:00 |    54.67      |         -53.75    | SHORT    | Yahoo Finance |
| LDO-USD    | 2026-11-19 00:00:00 |     0.272     |         -49.6667  | SHORT    | Kraken API    |
| LINK-USD   | 2026-11-19 00:00:00 |     9.15846   |         -49.6667  | SHORT    | Kraken API    |
| LRCX       | 2026-11-18 00:00:00 |   211.67      |         -40.9167  | SHORT    | Yahoo Finance |
| LTC-USD    | 2026-11-19 00:00:00 |    44.66      |         -49.6667  | SHORT    | Kraken API    |
| MU         | 2026-11-18 00:00:00 |   705.27      |         -60       | SHORT    | Yahoo Finance |
| NOW        | 2026-11-18 00:00:00 |    90.59      |         -49.9167  | SHORT    | Yahoo Finance |
| NVDA       | 2026-11-18 00:00:00 |   150.96      |         -65.5833  | SHORT    | Yahoo Finance |
| OP-USD     | 2026-11-19 00:00:00 |     0.0767    |         -55.3333  | SHORT    | Kraken API    |
| OXY        | 2026-11-18 00:00:00 |    53.76      |         -61.5833  | SHORT    | Yahoo Finance |
| PEPE-USD   | 2026-11-19 00:00:00 |     3.812e-06 |         -52       | SHORT    | Kraken API    |
| POL-USD    | 2026-11-19 00:00:00 |     0.08227   |         -46       | SHORT    | Kraken API    |
| QQQ        | 2026-11-18 00:00:00 |   659.51      |         -33.5     | SHORT    | Yahoo Finance |
| SHIB-USD   | 2026-11-19 00:00:00 |     3.841e-06 |         -49.6667  | SHORT    | Kraken API    |
| SKY-USD    | 2026-11-19 00:00:00 |     0.04802   |         -52.0833  | SHORT    | Kraken API    |
| SLB        | 2026-11-18 00:00:00 |    48.41      |         -56.5833  | SHORT    | Yahoo Finance |
| SLV        | 2026-11-18 00:00:00 |    40.7       |         -48.75    | SHORT    | Yahoo Finance |
| SMH        | 2026-11-18 00:00:00 |   459.54      |         -63.0833  | SHORT    | Yahoo Finance |
| SOL-USD    | 2026-11-19 00:00:00 |    74.97      |         -44.6667  | SHORT    | Kraken API    |
| SOXX       | 2026-11-18 00:00:00 |   141.85      |         -55.25    | SHORT    | Yahoo Finance |
| SUSHI-USD  | 2026-11-19 00:00:00 |     0.1553    |         -43       | SHORT    | Kraken API    |
| TIA-USD    | 2026-11-19 00:00:00 |     0.3539    |         -45.3333  | SHORT    | Kraken API    |
| TLT        | 2026-11-18 00:00:00 |    80.22      |         -46.75    | SHORT    | Yahoo Finance |
| TRX-USD    | 2026-11-19 00:00:00 |     0.312469  |         -48.8333  | SHORT    | Kraken API    |
| UNI-USD    | 2026-11-19 00:00:00 |     5.207     |         -55.3333  | SHORT    | Kraken API    |
| USO        | 2026-11-18 00:00:00 |   136.11      |         -37.3333  | SHORT    | Yahoo Finance |
| VWO        | 2026-11-18 00:00:00 |    53.76      |         -48.75    | SHORT    | Yahoo Finance |
| WIF-USD    | 2026-11-19 00:00:00 |     0.1346    |         -49.6667  | SHORT    | Kraken API    |
| XLB        | 2026-11-18 00:00:00 |    50.46      |         -42.8333  | SHORT    | Yahoo Finance |
| XLE        | 2026-11-18 00:00:00 |    61.29      |         -35.3333  | SHORT    | Yahoo Finance |
| XLK        | 2026-11-18 00:00:00 |   163.81      |         -41.8333  | SHORT    | Yahoo Finance |
| XLM-USD    | 2026-11-19 00:00:00 |     0.137506  |         -31.6667  | SHORT    | Kraken API    |
| XOM        | 2026-11-18 00:00:00 |   160.58      |         -35.3333  | SHORT    | Yahoo Finance |
| XRP-USD    | 2026-11-19 00:00:00 |     0.98231   |         -49.6667  | SHORT    | Kraken API    |
| YFI-USD    | 2026-11-19 00:00:00 |  1735.2       |         -44.3333  | SHORT    | Kraken API    |

## Edge Summary

- Symbols with trades: **161** of 161
- Beat buy-and-hold: **37.89%** of traded symbols
- Positive return: **33.54%** of traded symbols
- Median strategy return: **-6.81%** (benchmark **14.86%**)
- Median excess vs benchmark: **-19.60%**
- Median Sharpe: **-0.04**
- Median exposure: **44.43%**

> Edge is real only if both _beat buy-and-hold_ and _median excess_ are convincingly positive across many symbols. Treat a single high-return symbol as noise.

## Portfolio Backtest

Actual capital-allocation books (not per-symbol averages). Benchmarks: `equal_weight_buyhold` (whole tracked universe), `spy_buyhold` (100% SPY), and `sixty_forty` (60% SPY / 40% AGG). `high_conf_voltarget` inverse-vol-weights the HIGH-confidence book; `conviction_long_short` is market-neutral. Judge on **Sharpe** and **max_drawdown** out-of-sample, not raw return: a fully-invested long book wins on return in a bull market but carries all the risk.

| strategy              | scope         | ann_return   | ann_vol   |   sharpe | max_drawdown   | total_return   |   avg_gross_exposure |
|:----------------------|:--------------|:-------------|:----------|---------:|:---------------|:---------------|---------------------:|
| equal_weight_buyhold  | full          | 4.50%        | 28.49%    |     0.16 | -39.53%        | 1.37%          |                 1    |
| equal_weight_buyhold  | out_of_sample | 16.03%       | 26.20%    |     0.61 | -20.82%        | 14.35%         |                 1    |
| all_signals_ew        | full          | -11.03%      | 24.35%    |    -0.45 | -51.65%        | -34.64%        |                 1    |
| all_signals_ew        | out_of_sample | -5.53%       | 21.41%    |    -0.26 | -22.87%        | -7.98%         |                 1    |
| high_conf_ew          | full          | -9.66%       | 30.08%    |    -0.32 | -47.69%        | -34.93%        |                 0.89 |
| high_conf_ew          | out_of_sample | 2.58%        | 25.09%    |     0.1  | -27.61%        | -0.60%         |                 0.89 |
| high_conf_voltarget   | full          | -10.65%      | 26.81%    |    -0.4  | -42.17%        | -35.02%        |                 0.89 |
| high_conf_voltarget   | out_of_sample | -0.44%       | 20.28%    |    -0.02 | -23.45%        | -2.64%         |                 0.89 |
| conviction_long_short | full          | -16.24%      | 22.09%    |    -0.74 | -52.78%        | -43.31%        |                 0.96 |
| conviction_long_short | out_of_sample | -7.24%       | 16.72%    |    -0.43 | -23.15%        | -8.78%         |                 0.96 |
| spy_buyhold           | full          | 2.54%        | 14.02%    |     0.18 | -19.00%        | 4.85%          |                 0.79 |
| spy_buyhold           | out_of_sample | -5.92%       | 10.90%    |    -0.54 | -10.96%        | -6.69%         |                 0.79 |
| sixty_forty           | full          | 1.01%        | 8.80%     |     0.12 | -11.86%        | 1.92%          |                 0.79 |
| sixty_forty           | out_of_sample | -5.82%       | 7.21%     |    -0.81 | -7.94%         | -6.26%         |                 0.79 |

## Walk-Forward Robustness

Each book measured across contiguous time folds (each a different regime). A book has durable edge only if `mean_sharpe` is positive, `min_sharpe` isn't deeply negative, and `pct_positive_folds` is high — a single great fold doesn't count. `fold_sharpes` lists each fold oldest-to-newest.

| strategy              |   n_folds |   mean_sharpe |   median_sharpe |   min_sharpe | pct_positive_folds   | mean_return   | fold_sharpes                 |
|:----------------------|----------:|--------------:|----------------:|-------------:|:---------------------|:--------------|:-----------------------------|
| equal_weight_buyhold  |         5 |          0.35 |            0.12 |        -0.49 | 60.00%               | 1.03%         | 1.36;1.14;-0.49;-0.37;0.12   |
| all_signals_ew        |         5 |         -0.49 |           -0.48 |        -1.99 | 40.00%               | -6.70%        | -1.23;-0.48;-1.99;1.09;0.15  |
| high_conf_ew          |         5 |         -0.18 |           -0.35 |        -2.05 | 40.00%               | -6.43%        | 1.08;-2.05;-0.35;1.16;-0.77  |
| high_conf_voltarget   |         5 |         -0.32 |           -0.19 |        -2.29 | 40.00%               | -7.18%        | 1.15;-2.29;-0.19;0.66;-0.94  |
| conviction_long_short |         5 |         -0.71 |           -0.35 |        -2.21 | 20.00%               | -10.20%       | -2.21;-0.35;-1.06;-0.19;0.26 |
| spy_buyhold           |         5 |          0.08 |            0.2  |        -1.03 | 60.00%               | 1.12%         | 1.35;0.21;-0.35;0.20;-1.03   |
| sixty_forty           |         5 |          0    |           -0    |        -1.26 | 40.00%               | 0.46%         | 1.33;0.19;-0.24;-0.00;-1.26  |

## Strategy Comparison

Each decision rule backtested over the same data. `out_of_sample` is the most recent ~35% of each symbol's history (unseen tail). A rule has real edge only if `median_excess` and `beat_benchmark_pct` stay positive out-of-sample, not just full-sample.

| strategy        | scope         |   symbols | beat_benchmark_pct   | positive_pct   | median_return   | median_benchmark   | median_excess   |   median_sharpe |   total_trades |
|:----------------|:--------------|----------:|:---------------------|:---------------|:----------------|:-------------------|:----------------|----------------:|---------------:|
| trend           | full          |       161 | 37.89%               | 33.54%         | -6.81%          | 14.86%             | -19.60%         |           -0.04 |          11368 |
| trend           | out_of_sample |       161 | 49.69%               | 52.17%         | 1.01%           | -3.11%             | -0.24%          |            0.19 |           3874 |
| mean_reversion  | full          |       159 | 41.51%               | 45.91%         | -0.23%          | 14.86%             | -17.02%         |           -0.02 |           1288 |
| mean_reversion  | out_of_sample |       131 | 59.54%               | 58.78%         | 0.41%           | -4.47%             | 4.57%           |            0.54 |            442 |
| regime_adaptive | full          |       161 | 37.89%               | 31.68%         | -8.28%          | 14.86%             | -21.28%         |           -0.03 |          11630 |
| regime_adaptive | out_of_sample |       161 | 49.69%               | 51.55%         | 0.73%           | -3.11%             | -0.24%          |            0.22 |           3975 |

## Signal Calibration

Realized forward return in the signal's direction, grouped by confidence. HIGH should outrank LOW for the confidence score to be meaningful.

| confidence_level   |   horizon |     n | mean_return   | median_return   | win_rate   |
|:-------------------|----------:|------:|:--------------|:----------------|:-----------|
| HIGH               |         5 |  7811 | 0.20%         | 0.07%           | 51.13%     |
| MEDIUM             |         5 | 29353 | 0.11%         | 0.07%           | 50.78%     |
| LOW                |         5 |  3673 | -0.22%        | -0.26%          | 47.45%     |
| ALL                |         5 | 40837 | 0.10%         | 0.05%           | 50.55%     |
| HIGH               |        10 |  7710 | 0.47%         | 0.09%           | 51.01%     |
| MEDIUM             |        10 | 29023 | 0.24%         | 0.07%           | 50.56%     |
| LOW                |        10 |  3634 | -0.39%        | -0.24%          | 48.21%     |
| ALL                |        10 | 40367 | 0.22%         | 0.06%           | 50.43%     |
| HIGH               |        20 |  7543 | 0.97%         | 0.23%           | 51.82%     |
| MEDIUM             |        20 | 28377 | 0.76%         | 0.46%           | 52.57%     |
| LOW                |        20 |  3554 | -0.12%        | -0.37%          | 48.28%     |
| ALL                |        20 | 39474 | 0.72%         | 0.34%           | 52.04%     |

## Backtest Summary

### Data Quality / Signal Availability

- **ok**: 161 symbols

| symbol     |   trades | return   | benchmark_return   | mdd     |   sharpe | exposure   | skipped_reason   |
|:-----------|---------:|:---------|:-------------------|:--------|---------:|:-----------|:-----------------|
| AAPL       |       67 | -6.37%   | 67.34%             | -20.65% |    -0.03 | 47.59%     | ok               |
| AAVE-USD   |       69 | -45.67%  | -60.23%            | -64.31% |    -0.37 | 39.85%     | ok               |
| ABBV       |       68 | -16.75%  | 66.75%             | -30.52% |    -0.31 | 49.75%     | ok               |
| ADA-USD    |       74 | -15.90%  | -75.58%            | -52.70% |     0.04 | 50.00%     | ok               |
| ADBE       |       74 | -5.25%   | -59.28%            | -31.20% |     0.06 | 53.08%     | ok               |
| AGG        |       65 | -6.81%   | -1.59%             | -10.74% |    -1.04 | 34.78%     | ok               |
| ALGO-USD   |       82 | -21.35%  | -55.83%            | -44.43% |    -0.04 | 42.34%     | ok               |
| AMAT       |       73 | -33.08%  | 49.29%             | -53.91% |    -0.23 | 51.41%     | ok               |
| AMD        |       54 | 18.32%   | 226.82%            | -38.64% |     0.38 | 36.27%     | ok               |
| AMGN       |       63 | -8.21%   | 42.07%             | -34.19% |    -0.08 | 53.74%     | ok               |
| AMZN       |       84 | -57.75%  | 38.55%             | -59.16% |    -1.68 | 41.43%     | ok               |
| APT-USD    |       76 | -24.53%  | -90.76%            | -57.67% |    -0.01 | 40.61%     | ok               |
| ARB-USD    |       75 | 0.46%    | -59.79%            | -42.38% |     0.28 | 42.53%     | ok               |
| ARKK       |       89 | -26.65%  | 61.68%             | -38.67% |    -0.37 | 44.76%     | ok               |
| ATOM-USD   |       80 | -58.44%  | -68.02%            | -62.98% |    -0.89 | 45.02%     | ok               |
| AVAX-USD   |       64 | -33.01%  | -62.89%            | -46.76% |    -0.26 | 40.42%     | ok               |
| AVGO       |       68 | -7.44%   | 120.52%            | -44.82% |     0.08 | 39.60%     | ok               |
| BA         |       63 | 24.00%   | -10.49%            | -24.47% |     0.48 | 53.08%     | ok               |
| BAC        |       78 | -7.42%   | 22.98%             | -23.14% |    -0.12 | 49.08%     | ok               |
| BCH-USD    |       82 | -5.92%   | -55.25%            | -54.04% |     0.15 | 49.04%     | ok               |
| BITO       |       83 | -10.58%  | -63.08%            | -43.13% |     0.03 | 41.76%     | ok               |
| BLK        |       79 | -9.43%   | 48.51%             | -26.90% |    -0.17 | 47.25%     | ok               |
| BND        |       68 | -6.96%   | -1.64%             | -10.80% |    -1.05 | 35.77%     | ok               |
| BONK-USD   |       72 | 42.11%   | -83.85%            | -53.32% |     0.58 | 44.64%     | ok               |
| BTC-USD    |       79 | 3.58%    | -40.36%            | -25.52% |     0.2  | 52.68%     | ok               |
| C          |       81 | -37.36%  | 84.90%             | -39.84% |    -0.83 | 46.76%     | ok               |
| CAT        |       70 | 35.56%   | 67.75%             | -21.87% |     0.6  | 51.91%     | ok               |
| CL         |       60 | 7.48%    | 1.87%              | -14.32% |     0.29 | 40.27%     | ok               |
| CMCSA      |       82 | -34.14%  | -31.23%            | -45.88% |    -0.79 | 44.43%     | ok               |
| COMP-USD   |       95 | -45.29%  | -66.84%            | -52.17% |    -0.38 | 48.28%     | ok               |
| COP        |       66 | -14.27%  | 17.50%             | -37.99% |    -0.16 | 43.93%     | ok               |
| COST       |       60 | 5.20%    | 29.02%             | -31.32% |     0.22 | 41.10%     | ok               |
| CRM        |       69 | -20.80%  | -25.94%            | -39.41% |    -0.21 | 46.59%     | ok               |
| CRV-USD    |       64 | 62.48%   | -67.23%            | -39.89% |     0.71 | 38.12%     | ok               |
| CSCO       |       67 | 0.91%    | 104.55%            | -29.36% |     0.14 | 52.08%     | ok               |
| CVX        |       69 | -16.12%  | 31.62%             | -26.75% |    -0.35 | 43.43%     | ok               |
| DASH-USD   |       59 | -16.74%  | 83.81%             | -64.43% |     0.27 | 30.46%     | ok               |
| DBC        |       70 | -9.67%   | 27.03%             | -24.10% |    -0.26 | 36.44%     | ok               |
| DE         |       72 | -6.90%   | 72.56%             | -21.16% |    -0.05 | 44.43%     | ok               |
| DIA        |       72 | -9.41%   | 28.28%             | -16.20% |    -0.48 | 43.76%     | ok               |
| DIS        |       62 | 3.63%    | 23.23%             | -27.81% |     0.17 | 47.09%     | ok               |
| DOGE-USD   |       68 | -12.13%  | -65.55%            | -61.52% |     0.08 | 47.13%     | ok               |
| DOT-USD    |       76 | -53.69%  | -81.26%            | -67.54% |    -0.53 | 41.76%     | ok               |
| DXY-INDEX  |       40 | -0.39%   | -3.98%             | -5.13%  |    -0.05 | 30.74%     | ok               |
| EEM        |       68 | -5.70%   | 35.90%             | -24.14% |    -0.1  | 42.26%     | ok               |
| EFA        |       64 | -11.02%  | 28.00%             | -13.32% |    -0.45 | 38.77%     | ok               |
| EOG        |       76 | -30.76%  | 18.92%             | -47.65% |    -0.65 | 44.43%     | ok               |
| ETC-USD    |       56 | 2.98%    | -64.77%            | -46.79% |     0.22 | 36.78%     | ok               |
| ETH-USD    |       63 | 135.96%  | -28.91%            | -30.11% |     1.25 | 48.28%     | ok               |
| EWJ        |       70 | -24.40%  | 29.02%             | -29.40% |    -0.83 | 38.44%     | ok               |
| FCX        |       67 | -16.13%  | 5.86%              | -46.84% |    -0.07 | 46.09%     | ok               |
| FET-USD    |       79 | -44.23%  | -81.22%            | -66.52% |    -0.25 | 44.25%     | ok               |
| FIL-USD    |       65 | -0.90%   | -76.75%            | -58.54% |     0.22 | 39.27%     | ok               |
| FXI        |       46 | -4.25%   | 24.62%             | -23.91% |    -0.02 | 30.45%     | ok               |
| GDX        |       68 | -6.36%   | 120.51%            | -34.29% |     0.04 | 45.09%     | ok               |
| GDXJ       |       70 | -30.10%  | 113.84%            | -36.01% |    -0.32 | 44.43%     | ok               |
| GE         |       80 | -13.89%  | 106.39%            | -27.82% |    -0.15 | 49.08%     | ok               |
| GLD        |       52 | 11.67%   | 58.69%             | -14.15% |     0.35 | 46.09%     | ok               |
| GOOGL      |       55 | 75.56%   | 55.06%             | -17.55% |     1.14 | 49.92%     | ok               |
| GRT-USD    |       73 | 73.50%   | -80.11%            | -38.70% |     0.79 | 46.55%     | ok               |
| GS         |       68 | -2.77%   | 93.04%             | -21.94% |     0.04 | 47.42%     | ok               |
| HBAR-USD   |       42 | -23.19%  | -45.99%            | -56.47% |    -0.25 | 42.14%     | ok               |
| HD         |       69 | 5.97%    | -1.92%             | -17.15% |     0.23 | 44.93%     | ok               |
| HON        |       87 | -27.99%  | 5.51%              | -32.93% |    -0.71 | 52.08%     | ok               |
| HYG        |       89 | -6.76%   | -0.64%             | -10.59% |    -0.75 | 39.77%     | ok               |
| IBIT       |       46 | 55.09%   | -6.97%             | -18.95% |     0.85 | 36.10%     | ok               |
| IBM        |       71 | -21.28%  | 32.14%             | -48.94% |    -0.22 | 50.42%     | ok               |
| ICP-USD    |       72 | 6.42%    | -57.72%            | -43.16% |     0.32 | 40.04%     | ok               |
| IEF        |       80 | -10.61%  | -3.18%             | -12.66% |    -1.4  | 35.27%     | ok               |
| IEMG       |       64 | -2.46%   | 31.83%             | -24.73% |    -0.01 | 42.10%     | ok               |
| INJ-USD    |       55 | -12.40%  | -38.22%            | -61.35% |     0.13 | 38.70%     | ok               |
| INTC       |       72 | 67.15%   | 76.53%             | -60.60% |     0.67 | 50.25%     | ok               |
| INTU       |       73 | -9.54%   | -52.34%            | -37.44% |    -0.01 | 47.09%     | ok               |
| ITA        |       72 | 0.52%    | 57.64%             | -22.33% |     0.09 | 47.09%     | ok               |
| IWM        |       56 | 10.39%   | 33.14%             | -8.62%  |     0.42 | 34.44%     | ok               |
| JNJ        |       60 | 10.93%   | 86.58%             | -17.51% |     0.42 | 47.92%     | ok               |
| JPM        |       77 | -28.81%  | 60.24%             | -32.74% |    -0.85 | 44.93%     | ok               |
| KO         |       54 | 28.01%   | 54.11%             | -8.64%  |     0.93 | 39.93%     | ok               |
| LDO-USD    |       70 | 86.85%   | -66.83%            | -47.94% |     0.82 | 48.28%     | ok               |
| LIN        |       72 | -6.27%   | 16.72%             | -20.61% |    -0.15 | 42.26%     | ok               |
| LINK-USD   |       72 | 31.60%   | -32.33%            | -35.01% |     0.52 | 43.30%     | ok               |
| LLY        |       82 | -34.29%  | 52.73%             | -53.34% |    -0.53 | 49.75%     | ok               |
| LRCX       |       87 | -26.28%  | 98.78%             | -61.92% |    -0.11 | 45.42%     | ok               |
| LTC-USD    |       67 | 29.79%   | -48.43%            | -32.28% |     0.52 | 51.53%     | ok               |
| MCD        |       77 | 7.05%    | 7.53%              | -22.20% |     0.29 | 41.26%     | ok               |
| META       |       70 | -31.84%  | 22.24%             | -44.52% |    -0.47 | 49.58%     | ok               |
| MPC        |       70 | 11.57%   | 115.51%            | -33.74% |     0.31 | 53.41%     | ok               |
| MRK        |       67 | -24.79%  | 11.29%             | -35.95% |    -0.48 | 43.59%     | ok               |
| MS         |       71 | -3.98%   | 86.41%             | -27.79% |    -0.01 | 47.59%     | ok               |
| MSFT       |       81 | -26.37%  | 13.72%             | -37.80% |    -0.57 | 50.58%     | ok               |
| MU         |       53 | 88.04%   | 436.20%            | -64.76% |     0.79 | 49.42%     | ok               |
| NEAR-USD   |       65 | 177.42%  | 50.55%             | -46.60% |     1.13 | 43.49%     | ok               |
| NEM        |       70 | -25.86%  | 149.65%            | -39.56% |    -0.25 | 49.75%     | ok               |
| NFLX       |       86 | -5.70%   | -11.36%            | -27.17% |    -0.01 | 50.58%     | ok               |
| NKE        |       89 | -45.53%  | -51.82%            | -55.35% |    -0.79 | 47.42%     | ok               |
| NOW        |       81 | -3.88%   | -42.42%            | -42.66% |     0.17 | 51.91%     | ok               |
| NVDA       |       82 | -32.74%  | 19.37%             | -50.87% |    -0.37 | 55.79%     | ok               |
| OP-USD     |       72 | -15.35%  | -86.81%            | -57.66% |     0.07 | 36.21%     | ok               |
| ORCL       |       60 | 60.08%   | -19.34%            | -31.06% |     0.66 | 49.92%     | ok               |
| OXY        |       67 | 8.32%    | -14.71%            | -28.48% |     0.26 | 43.43%     | ok               |
| PEP        |       70 | 3.01%    | -13.98%            | -21.35% |     0.16 | 46.09%     | ok               |
| PEPE-USD   |       74 | -37.18%  | -63.96%            | -60.19% |    -0.12 | 47.13%     | ok               |
| PFE        |       79 | -33.58%  | 0.29%              | -42.77% |    -1.02 | 37.60%     | ok               |
| PG         |       62 | -17.11%  | 3.26%              | -24.55% |    -0.58 | 37.44%     | ok               |
| PM         |       77 | -5.63%   | 90.20%             | -37.61% |    -0.03 | 47.75%     | ok               |
| POL-USD    |       87 | 4.76%    | -58.77%            | -46.25% |     0.27 | 48.85%     | ok               |
| QCOM       |       77 | -35.78%  | -19.77%            | -50.90% |    -0.37 | 40.10%     | ok               |
| QQQ        |       72 | -3.52%   | 37.65%             | -15.84% |    -0.01 | 43.26%     | ok               |
| RENDER-USD |       86 | -44.24%  | -57.83%            | -54.95% |    -0.28 | 46.74%     | ok               |
| RTX        |       73 | 16.35%   | 96.68%             | -16.99% |     0.43 | 52.91%     | ok               |
| SBUX       |       64 | -9.07%   | 40.15%             | -29.22% |    -0.09 | 40.60%     | ok               |
| SCHW       |       84 | -16.47%  | 25.61%             | -31.92% |    -0.34 | 48.09%     | ok               |
| SHIB-USD   |       79 | -31.81%  | -67.59%            | -54.82% |    -0.28 | 51.72%     | ok               |
| SHY        |       56 | -2.37%   | -0.38%             | -3.30%  |    -0.76 | 39.10%     | ok               |
| SKY-USD    |       85 | -46.16%  | -46.82%            | -63.39% |    -0.55 | 46.17%     | ok               |
| SLB        |       78 | -42.24%  | 2.61%              | -55.21% |    -0.84 | 48.09%     | ok               |
| SLV        |       66 | 47.72%   | 53.18%             | -37.05% |     0.67 | 42.43%     | ok               |
| SMH        |       50 | 59.72%   | 76.27%             | -33.66% |     0.87 | 41.93%     | ok               |
| SNX-USD    |       62 | -5.41%   | -74.46%            | -50.74% |     0.16 | 36.78%     | ok               |
| SOL-USD    |       73 | 7.12%    | -50.24%            | -43.77% |     0.3  | 58.81%     | ok               |
| SOXX       |       58 | 61.04%   | 72.55%             | -40.14% |     0.83 | 41.10%     | ok               |
| SPY        |       63 | -5.19%   | 34.17%             | -15.53% |    -0.12 | 46.92%     | ok               |
| SUSHI-USD  |       89 | -59.76%  | -75.75%            | -78.98% |    -0.66 | 44.44%     | ok               |
| T          |       68 | 52.21%   | 14.86%             | -17.01% |     0.94 | 57.57%     | ok               |
| TGT        |       60 | -6.39%   | 12.08%             | -32.83% |    -0.05 | 37.77%     | ok               |
| TIA-USD    |       85 | -45.09%  | -79.40%            | -74.75% |    -0.2  | 44.25%     | ok               |
| TLT        |       68 | -21.48%  | -12.60%            | -22.12% |    -1.62 | 34.94%     | ok               |
| TMO        |       67 | 38.81%   | 25.27%             | -18.85% |     0.74 | 56.41%     | ok               |
| TMUS       |       74 | -6.51%   | -6.90%             | -33.05% |    -0.04 | 45.92%     | ok               |
| TRX-USD    |       60 | 9.98%    | 14.00%             | -22.90% |     0.37 | 49.04%     | ok               |
| TSLA       |       74 | -35.94%  | 93.92%             | -58.36% |    -0.24 | 41.76%     | ok               |
| TXN        |       83 | -30.18%  | 50.33%             | -46.56% |    -0.35 | 48.75%     | ok               |
| UNH        |       74 | 45.70%   | -31.29%            | -26.31% |     0.68 | 48.25%     | ok               |
| UNI-USD    |       80 | 5.36%    | -29.95%            | -60.31% |     0.33 | 50.00%     | ok               |
| UPS        |       71 | -35.11%  | -18.87%            | -41.37% |    -0.66 | 44.26%     | ok               |
| USO        |       70 | -10.02%  | 71.01%             | -42.74% |    -0    | 33.78%     | ok               |
| VEA        |       64 | -7.02%   | 34.93%             | -18.84% |    -0.25 | 41.26%     | ok               |
| VIXY       |      100 | -84.95%  | -53.00%            | -91.70% |    -1.2  | 31.95%     | ok               |
| VNQ        |       71 | -11.08%  | 13.63%             | -24.66% |    -0.41 | 40.60%     | ok               |
| VTI        |       67 | -11.63%  | 34.38%             | -17.64% |    -0.37 | 46.92%     | ok               |
| VWO        |       80 | -14.50%  | 22.85%             | -25.20% |    -0.49 | 41.76%     | ok               |
| VZ         |       86 | -27.73%  | 11.86%             | -31.67% |    -0.84 | 43.26%     | ok               |
| WFC        |       80 | -20.00%  | 36.25%             | -30.94% |    -0.35 | 46.76%     | ok               |
| WIF-USD    |       64 | 11.03%   | -83.83%            | -48.32% |     0.36 | 43.87%     | ok               |
| WMT        |       69 | 7.51%    | 88.10%             | -25.96% |     0.27 | 48.59%     | ok               |
| XBI        |       60 | 1.08%    | 56.44%             | -17.66% |     0.11 | 37.60%     | ok               |
| XLB        |       66 | -12.19%  | 14.28%             | -24.92% |    -0.4  | 34.61%     | ok               |
| XLC        |       61 | 4.09%    | 23.25%             | -12.33% |     0.2  | 48.59%     | ok               |
| XLE        |       72 | -5.01%   | 34.48%             | -34.77% |    -0.04 | 47.75%     | ok               |
| XLF        |       78 | -5.16%   | 37.24%             | -23.61% |    -0.12 | 49.75%     | ok               |
| XLI        |       82 | -12.77%  | 35.11%             | -18.27% |    -0.49 | 42.60%     | ok               |
| XLK        |       44 | 34.83%   | 44.82%             | -19.09% |     0.75 | 43.93%     | ok               |
| XLM-USD    |       83 | -8.28%   | -47.39%            | -58.34% |     0.13 | 49.23%     | ok               |
| XLP        |       63 | 14.66%   | 19.07%             | -8.96%  |     0.71 | 41.26%     | ok               |
| XLU        |       69 | -0.58%   | 27.83%             | -20.40% |     0.02 | 41.26%     | ok               |
| XLV        |       74 | -20.98%  | 24.30%             | -22.82% |    -0.93 | 37.94%     | ok               |
| XLY        |       77 | -5.70%   | 30.70%             | -18.44% |    -0.1  | 47.59%     | ok               |
| XOM        |       59 | 2.83%    | 39.49%             | -20.29% |     0.15 | 36.77%     | ok               |
| XRP-USD    |       72 | 4.62%    | -56.13%            | -33.93% |     0.25 | 36.97%     | ok               |
| YFI-USD    |       74 | -44.24%  | -66.35%            | -55.00% |    -0.59 | 40.61%     | ok               |
| ZEC-USD    |       54 | 126.43%  | 2087.25%           | -56.50% |     0.87 | 36.97%     | ok               |

## AAPL Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -0.51%   | 67.34%             | -21.71% |     0.1  |       76 | 52.41%     | ok               |
|          15 | -4.91%   | 67.34%             | -23.86% |     0.02 |       85 | 59.90%     | ok               |
|          30 | -6.37%   | 67.34%             | -20.65% |    -0.03 |       67 | 47.59%     | ok               |
|          35 | -7.71%   | 67.34%             | -22.04% |    -0.06 |       67 | 46.26%     | ok               |
|          25 | -10.16%  | 67.34%             | -22.37% |    -0.1  |       77 | 49.75%     | ok               |

## AAVE-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -7.29%   | -60.23%            | -43.61% |     0.14 |       45 | 34.10%     | ok               |
|          50 | -11.92%  | -60.23%            | -45.47% |     0.03 |       42 | 21.84%     | ok               |
|          35 | -17.30%  | -60.23%            | -48.79% |     0.02 |       55 | 37.74%     | ok               |
|          45 | -18.57%  | -60.23%            | -49.19% |    -0.03 |       50 | 28.74%     | ok               |
|          15 | -39.57%  | -60.23%            | -59.76% |    -0.16 |       80 | 54.21%     | ok               |

## ABBV Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -2.84%   | 66.75%             | -23.80% |     0.01 |       54 | 37.10%     | ok               |
|          20 | -13.49%  | 66.75%             | -28.73% |    -0.22 |       64 | 53.08%     | ok               |
|          25 | -13.59%  | 66.75%             | -30.04% |    -0.22 |       67 | 51.58%     | ok               |
|          30 | -16.75%  | 66.75%             | -30.52% |    -0.31 |       68 | 49.75%     | ok               |
|          40 | -16.81%  | 66.75%             | -27.36% |    -0.35 |       70 | 42.76%     | ok               |

## ADA-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 6.22%    | -75.58%            | -46.50% |     0.33 |       67 | 64.75%     | ok               |
|          35 | -0.19%   | -75.58%            | -44.07% |     0.22 |       64 | 44.25%     | ok               |
|          40 | -5.42%   | -75.58%            | -41.68% |     0.14 |       58 | 39.66%     | ok               |
|          20 | -17.81%  | -75.58%            | -53.45% |     0.08 |       83 | 58.81%     | ok               |
|          50 | -6.60%   | -75.58%            | -32.89% |     0.08 |       50 | 24.71%     | ok               |

## ADBE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | 9.29%    | -59.28%            | -29.07% |     0.27 |       59 | 57.24%     | ok               |
|          20 | -5.80%   | -59.28%            | -31.52% |     0.06 |       67 | 60.57%     | ok               |
|          30 | -5.25%   | -59.28%            | -31.20% |     0.06 |       74 | 53.08%     | ok               |
|          35 | -7.59%   | -59.28%            | -32.89% |     0    |       75 | 44.93%     | ok               |
|          15 | -12.20%  | -59.28%            | -34.98% |    -0.04 |       67 | 63.23%     | ok               |

## AGG Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -6.81%   | -1.59%             | -10.74% |    -1.04 |       65 | 34.78%     | ok               |
|          45 | -6.35%   | -1.59%             | -9.39%  |    -1.16 |       60 | 24.13%     | ok               |
|          20 | -8.66%   | -1.59%             | -11.89% |    -1.22 |       70 | 40.43%     | ok               |
|          25 | -8.43%   | -1.59%             | -12.28% |    -1.23 |       71 | 38.27%     | ok               |
|          35 | -8.07%   | -1.59%             | -11.53% |    -1.29 |       66 | 31.45%     | ok               |

## ALGO-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -21.71%  | -55.83%            | -51.07% |    -0.03 |       86 | 46.74%     | ok               |
|          30 | -21.35%  | -55.83%            | -44.43% |    -0.04 |       82 | 42.34%     | ok               |
|          15 | -40.10%  | -55.83%            | -57.68% |    -0.27 |       85 | 53.64%     | ok               |
|          20 | -41.72%  | -55.83%            | -58.82% |    -0.32 |       85 | 49.81%     | ok               |
|          35 | -42.97%  | -55.83%            | -52.80% |    -0.48 |       72 | 36.40%     | ok               |

## AMAT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -32.14%  | 49.29%             | -53.90% |    -0.18 |       76 | 60.40%     | ok               |
|          50 | -26.61%  | 49.29%             | -41.04% |    -0.18 |       50 | 35.44%     | ok               |
|          35 | -30.03%  | 49.29%             | -47.88% |    -0.2  |       73 | 48.59%     | ok               |
|          30 | -33.08%  | 49.29%             | -53.91% |    -0.23 |       73 | 51.41%     | ok               |
|          40 | -38.54%  | 49.29%             | -50.74% |    -0.35 |       71 | 43.43%     | ok               |

## AMD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 34.13%   | 226.82%            | -37.12% |     0.51 |       52 | 31.45%     | ok               |
|          40 | 18.32%   | 226.82%            | -38.64% |     0.38 |       54 | 36.27%     | ok               |
|          35 | 13.24%   | 226.82%            | -40.22% |     0.34 |       62 | 37.94%     | ok               |
|          45 | 7.07%    | 226.82%            | -45.23% |     0.28 |       58 | 34.28%     | ok               |
|          30 | -3.80%   | 226.82%            | -47.20% |     0.19 |       65 | 40.60%     | ok               |

## AMGN Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -3.36%   | 42.07%             | -26.65% |     0.04 |       62 | 59.07%     | ok               |
|          35 | -5.90%   | 42.07%             | -31.29% |    -0.03 |       65 | 50.42%     | ok               |
|          30 | -8.21%   | 42.07%             | -34.19% |    -0.08 |       63 | 53.74%     | ok               |
|          50 | -6.81%   | 42.07%             | -24.20% |    -0.11 |       54 | 34.78%     | ok               |
|          15 | -10.52%  | 42.07%             | -27.98% |    -0.11 |       61 | 63.06%     | ok               |

## AMZN Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -34.83%  | 38.55%             | -37.17% |    -1.11 |       62 | 30.78%     | ok               |
|          50 | -34.80%  | 38.55%             | -36.99% |    -1.27 |       54 | 23.13%     | ok               |
|          45 | -42.11%  | 38.55%             | -44.04% |    -1.53 |       62 | 27.12%     | ok               |
|          30 | -57.75%  | 38.55%             | -59.16% |    -1.68 |       84 | 41.43%     | ok               |
|          35 | -56.20%  | 38.55%             | -57.67% |    -1.7  |       81 | 35.94%     | ok               |

## APT-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 54.31%   | -90.76%            | -25.96% |     0.88 |       44 | 16.86%     | ok               |
|          20 | 15.35%   | -90.76%            | -56.22% |     0.41 |       84 | 51.72%     | ok               |
|          45 | 14.80%   | -90.76%            | -52.49% |     0.37 |       64 | 24.14%     | ok               |
|          15 | -8.33%   | -90.76%            | -58.22% |     0.23 |       79 | 58.05%     | ok               |
|          40 | -8.86%   | -90.76%            | -53.58% |     0.13 |       60 | 30.65%     | ok               |

## ARB-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 81.02%   | -59.79%            | -33.86% |     0.8  |       58 | 26.25%     | ok               |
|          40 | 47.12%   | -59.79%            | -38.69% |     0.6  |       55 | 33.72%     | ok               |
|          35 | 41.73%   | -59.79%            | -37.63% |     0.57 |       69 | 37.74%     | ok               |
|          50 | 35.87%   | -59.79%            | -33.86% |     0.53 |       50 | 18.39%     | ok               |
|          15 | 29.86%   | -59.79%            | -55.99% |     0.51 |       97 | 57.85%     | ok               |

## ARKK Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -9.73%   | 61.68%             | -37.76% |     0    |       88 | 55.57%     | ok               |
|          20 | -19.80%  | 61.68%             | -35.06% |    -0.18 |       91 | 51.08%     | ok               |
|          30 | -26.65%  | 61.68%             | -38.67% |    -0.37 |       89 | 44.76%     | ok               |
|          35 | -34.47%  | 61.68%             | -43.49% |    -0.58 |       94 | 41.60%     | ok               |
|          25 | -37.22%  | 61.68%             | -47.50% |    -0.59 |       99 | 47.25%     | ok               |

## ATOM-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -45.94%  | -68.02%            | -57.59% |    -0.44 |       82 | 65.71%     | ok               |
|          25 | -47.78%  | -68.02%            | -55.83% |    -0.56 |       82 | 51.34%     | ok               |
|          20 | -51.37%  | -68.02%            | -61.00% |    -0.59 |       90 | 57.28%     | ok               |
|          45 | -48.43%  | -68.02%            | -53.91% |    -0.73 |       66 | 31.03%     | ok               |
|          40 | -55.35%  | -68.02%            | -61.53% |    -0.88 |       64 | 35.06%     | ok               |

## AVAX-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 58.75%   | -62.89%            | -22.06% |     0.88 |       36 | 18.97%     | ok               |
|          40 | 33.32%   | -62.89%            | -26.27% |     0.58 |       40 | 29.31%     | ok               |
|          45 | 28.83%   | -62.89%            | -24.48% |     0.54 |       36 | 25.10%     | ok               |
|          35 | 9.38%    | -62.89%            | -33.05% |     0.3  |       50 | 35.06%     | ok               |
|          15 | -10.43%  | -62.89%            | -43.71% |     0.12 |       72 | 52.49%     | ok               |

## AVGO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -7.44%   | 120.52%            | -44.82% |     0.08 |       68 | 39.60%     | ok               |
|          25 | -8.51%   | 120.52%            | -45.43% |     0.07 |       72 | 42.43%     | ok               |
|          20 | -15.60%  | 120.52%            | -45.94% |    -0.01 |       81 | 46.26%     | ok               |
|          50 | -14.44%  | 120.52%            | -44.23% |    -0.04 |       62 | 27.45%     | ok               |
|          35 | -16.40%  | 120.52%            | -48.57% |    -0.05 |       78 | 36.77%     | ok               |

## BA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 39.18%   | -10.49%            | -18.09% |     0.69 |       66 | 49.75%     | ok               |
|          50 | 26.23%   | -10.49%            | -13.34% |     0.64 |       48 | 35.61%     | ok               |
|          25 | 34.39%   | -10.49%            | -26.02% |     0.61 |       64 | 56.41%     | ok               |
|          40 | 24.87%   | -10.49%            | -23.87% |     0.53 |       50 | 43.93%     | ok               |
|          30 | 24.00%   | -10.49%            | -24.47% |     0.48 |       63 | 53.08%     | ok               |

## BAC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 3.21%    | 22.98%             | -16.89% |     0.16 |       84 | 55.07%     | ok               |
|          35 | -0.35%   | 22.98%             | -23.35% |     0.06 |       70 | 44.26%     | ok               |
|          15 | -2.66%   | 22.98%             | -21.05% |     0.03 |       90 | 61.06%     | ok               |
|          25 | -2.45%   | 22.98%             | -22.01% |     0.02 |       84 | 52.41%     | ok               |
|          45 | -2.85%   | 22.98%             | -16.06% |    -0.03 |       56 | 34.28%     | ok               |

## BCH-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 15.61%   | -55.25%            | -45.64% |     0.38 |       79 | 57.85%     | ok               |
|          20 | 12.60%   | -55.25%            | -45.52% |     0.35 |       74 | 54.60%     | ok               |
|          35 | -0.27%   | -55.25%            | -57.75% |     0.21 |       72 | 45.21%     | ok               |
|          25 | -3.32%   | -55.25%            | -48.42% |     0.18 |       78 | 50.96%     | ok               |
|          30 | -5.92%   | -55.25%            | -54.04% |     0.15 |       82 | 49.04%     | ok               |

## BITO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 2.15%    | -63.08%            | -31.98% |     0.17 |       54 | 24.46%     | ok               |
|          45 | -2.25%   | -63.08%            | -32.05% |     0.11 |       58 | 27.95%     | ok               |
|          30 | -10.58%  | -63.08%            | -43.13% |     0.03 |       83 | 41.76%     | ok               |
|          35 | -12.20%  | -63.08%            | -42.80% |    -0    |       74 | 37.44%     | ok               |
|          40 | -11.92%  | -63.08%            | -40.13% |    -0.02 |       68 | 32.78%     | ok               |

## BLK Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | -0.15%   | 48.51%             | -20.79% |     0.07 |       86 | 43.76%     | ok               |
|          20 | -3.64%   | 48.51%             | -21.48% |    -0    |       82 | 51.91%     | ok               |
|          25 | -5.02%   | 48.51%             | -24.62% |    -0.05 |       75 | 49.75%     | ok               |
|          40 | -4.49%   | 48.51%             | -22.83% |    -0.05 |       78 | 39.27%     | ok               |
|          30 | -9.43%   | 48.51%             | -26.90% |    -0.17 |       79 | 47.25%     | ok               |

## BND Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -7.38%   | -1.64%             | -10.72% |    -1.04 |       65 | 41.60%     | ok               |
|          25 | -7.18%   | -1.64%             | -11.16% |    -1.04 |       70 | 39.43%     | ok               |
|          30 | -6.96%   | -1.64%             | -10.80% |    -1.05 |       68 | 35.77%     | ok               |
|          40 | -7.02%   | -1.64%             | -11.24% |    -1.17 |       60 | 29.45%     | ok               |
|          15 | -8.75%   | -1.64%             | -12.04% |    -1.22 |       77 | 43.93%     | ok               |

## BONK-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 138.89%  | -83.85%            | -23.92% |     1.21 |       40 | 17.62%     | ok               |
|          40 | 120.58%  | -83.85%            | -43.89% |     1.01 |       64 | 34.48%     | ok               |
|          45 | 89.47%   | -83.85%            | -33.76% |     0.9  |       64 | 23.75%     | ok               |
|          35 | 76.66%   | -83.85%            | -48.16% |     0.78 |       62 | 40.23%     | ok               |
|          15 | 62.86%   | -83.85%            | -55.03% |     0.68 |       65 | 60.73%     | ok               |

## BTC-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 57.97%   | -40.36%            | -21.12% |     1.01 |       60 | 42.15%     | ok               |
|          40 | 51.00%   | -40.36%            | -17.26% |     0.96 |       48 | 35.63%     | ok               |
|          45 | 42.87%   | -40.36%            | -12.58% |     0.88 |       40 | 30.84%     | ok               |
|          30 | 22.46%   | -40.36%            | -22.34% |     0.5  |       72 | 47.89%     | ok               |
|          50 | 16.46%   | -40.36%            | -20.16% |     0.46 |       36 | 25.29%     | ok               |

## C Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -15.13%  | 84.90%             | -22.98% |    -0.38 |       68 | 30.78%     | ok               |
|          45 | -24.76%  | 84.90%             | -30.69% |    -0.65 |       78 | 35.77%     | ok               |
|          40 | -29.50%  | 84.90%             | -35.05% |    -0.75 |       74 | 38.27%     | ok               |
|          25 | -36.44%  | 84.90%             | -37.53% |    -0.79 |       71 | 49.42%     | ok               |
|          20 | -38.42%  | 84.90%             | -39.30% |    -0.83 |       77 | 52.08%     | ok               |

## CAT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 48.58%   | 67.75%             | -21.89% |     0.72 |       68 | 62.23%     | ok               |
|          25 | 45.19%   | 67.75%             | -21.79% |     0.7  |       66 | 54.24%     | ok               |
|          30 | 35.56%   | 67.75%             | -21.87% |     0.6  |       70 | 51.91%     | ok               |
|          20 | 31.94%   | 67.75%             | -24.78% |     0.55 |       70 | 56.91%     | ok               |
|          45 | 29.40%   | 67.75%             | -23.84% |     0.55 |       56 | 40.60%     | ok               |

## CL Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 13.55%   | 1.87%              | -10.72% |     0.51 |       44 | 24.96%     | ok               |
|          45 | 9.24%    | 1.87%              | -10.96% |     0.36 |       46 | 28.12%     | ok               |
|          30 | 7.48%    | 1.87%              | -14.32% |     0.29 |       60 | 40.27%     | ok               |
|          40 | 4.01%    | 1.87%              | -15.09% |     0.19 |       52 | 31.45%     | ok               |
|          35 | 3.19%    | 1.87%              | -15.39% |     0.17 |       60 | 36.44%     | ok               |

## CMCSA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -18.88%  | -31.23%            | -28.74% |    -0.63 |       50 | 16.64%     | ok               |
|          15 | -34.70%  | -31.23%            | -43.53% |    -0.7  |       90 | 59.07%     | ok               |
|          45 | -24.11%  | -31.23%            | -35.43% |    -0.76 |       64 | 21.30%     | ok               |
|          30 | -34.14%  | -31.23%            | -45.88% |    -0.79 |       82 | 44.43%     | ok               |
|          35 | -33.39%  | -31.23%            | -46.34% |    -0.83 |       93 | 39.43%     | ok               |

## COMP-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -30.88%  | -66.84%            | -41.50% |    -0.31 |       44 | 21.84%     | ok               |
|          30 | -45.29%  | -66.84%            | -52.17% |    -0.38 |       95 | 48.28%     | ok               |
|          15 | -62.22%  | -66.84%            | -70.31% |    -0.63 |      104 | 67.82%     | ok               |
|          20 | -60.75%  | -66.84%            | -66.44% |    -0.65 |      108 | 62.84%     | ok               |
|          25 | -60.37%  | -66.84%            | -64.40% |    -0.67 |      104 | 56.51%     | ok               |

## COP Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -14.27%  | 17.50%             | -37.99% |    -0.16 |       66 | 43.93%     | ok               |
|          50 | -12.17%  | 17.50%             | -35.99% |    -0.17 |       50 | 31.28%     | ok               |
|          35 | -14.12%  | 17.50%             | -40.42% |    -0.17 |       67 | 41.10%     | ok               |
|          45 | -17.00%  | 17.50%             | -41.02% |    -0.27 |       60 | 34.78%     | ok               |
|          40 | -22.24%  | 17.50%             | -46.75% |    -0.38 |       66 | 37.94%     | ok               |

## COST Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 20.04%   | 29.02%             | -24.32% |     0.6  |       62 | 47.09%     | ok               |
|          25 | 16.57%   | 29.02%             | -24.93% |     0.53 |       59 | 44.26%     | ok               |
|          35 | 9.84%    | 29.02%             | -30.16% |     0.37 |       58 | 38.60%     | ok               |
|          30 | 5.20%    | 29.02%             | -31.32% |     0.22 |       60 | 41.10%     | ok               |
|          15 | 3.77%    | 29.02%             | -27.30% |     0.18 |       67 | 50.75%     | ok               |

## CRM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | -8.20%   | -25.94%            | -26.69% |    -0    |       66 | 41.76%     | ok               |
|          40 | -11.64%  | -25.94%            | -32.67% |    -0.08 |       72 | 37.60%     | ok               |
|          15 | -20.36%  | -25.94%            | -47.54% |    -0.15 |       94 | 58.57%     | ok               |
|          30 | -20.80%  | -25.94%            | -39.41% |    -0.21 |       69 | 46.59%     | ok               |
|          25 | -24.20%  | -25.94%            | -43.32% |    -0.27 |       72 | 49.25%     | ok               |

## CRV-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 105.65%  | -67.23%            | -37.78% |     0.96 |       64 | 33.72%     | ok               |
|          40 | 84.38%   | -67.23%            | -38.86% |     0.86 |       56 | 29.89%     | ok               |
|          30 | 62.48%   | -67.23%            | -39.89% |     0.71 |       64 | 38.12%     | ok               |
|          45 | 56.08%   | -67.23%            | -42.29% |     0.7  |       58 | 23.37%     | ok               |
|          50 | 38.14%   | -67.23%            | -30.73% |     0.58 |       52 | 18.97%     | ok               |

## CSCO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 26.78%   | 104.55%            | -22.62% |     0.58 |       54 | 41.76%     | ok               |
|          50 | 25.99%   | 104.55%            | -19.64% |     0.57 |       54 | 39.93%     | ok               |
|          40 | 10.94%   | 104.55%            | -28.70% |     0.31 |       58 | 44.93%     | ok               |
|          35 | 7.40%    | 104.55%            | -28.19% |     0.25 |       62 | 48.59%     | ok               |
|          20 | 6.58%    | 104.55%            | -29.33% |     0.23 |       73 | 55.07%     | ok               |

## CVX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -11.08%  | 31.62%             | -23.25% |    -0.2  |       73 | 46.42%     | ok               |
|          45 | -11.34%  | 31.62%             | -27.82% |    -0.25 |       63 | 35.77%     | ok               |
|          40 | -12.49%  | 31.62%             | -25.79% |    -0.27 |       73 | 39.43%     | ok               |
|          20 | -14.58%  | 31.62%             | -23.74% |    -0.29 |       75 | 47.75%     | ok               |
|          50 | -11.22%  | 31.62%             | -29.71% |    -0.29 |       56 | 31.28%     | ok               |

## DASH-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 113.33%  | 83.81%             | -43.46% |     0.87 |       44 | 17.62%     | ok               |
|          40 | 88.07%   | 83.81%             | -42.64% |     0.76 |       50 | 24.52%     | ok               |
|          45 | 58.91%   | 83.81%             | -46.93% |     0.63 |       46 | 20.88%     | ok               |
|          25 | -12.63%  | 83.81%             | -64.14% |     0.31 |       69 | 32.76%     | ok               |
|          30 | -16.74%  | 83.81%             | -64.43% |     0.27 |       59 | 30.46%     | ok               |

## DBC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -0.19%   | 27.03%             | -26.01% |     0.06 |       83 | 43.76%     | ok               |
|          20 | -6.65%   | 27.03%             | -25.69% |    -0.14 |       75 | 40.93%     | ok               |
|          25 | -6.83%   | 27.03%             | -24.84% |    -0.15 |       70 | 38.77%     | ok               |
|          30 | -9.67%   | 27.03%             | -24.10% |    -0.26 |       70 | 36.44%     | ok               |
|          50 | -8.86%   | 27.03%             | -18.84% |    -0.28 |       48 | 25.29%     | ok               |

## DE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -2.14%   | 72.56%             | -19.95% |     0.06 |       63 | 48.59%     | ok               |
|          25 | -3.56%   | 72.56%             | -20.14% |     0.02 |       70 | 46.59%     | ok               |
|          30 | -6.90%   | 72.56%             | -21.16% |    -0.05 |       72 | 44.43%     | ok               |
|          50 | -5.12%   | 72.56%             | -17.97% |    -0.06 |       62 | 30.45%     | ok               |
|          45 | -8.39%   | 72.56%             | -22.07% |    -0.12 |       62 | 34.11%     | ok               |

## DIA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -7.32%   | 28.28%             | -13.58% |    -0.35 |       66 | 44.93%     | ok               |
|          20 | -9.43%   | 28.28%             | -15.48% |    -0.45 |       68 | 47.25%     | ok               |
|          35 | -9.01%   | 28.28%             | -16.94% |    -0.47 |       74 | 40.60%     | ok               |
|          30 | -9.41%   | 28.28%             | -16.20% |    -0.48 |       72 | 43.76%     | ok               |
|          40 | -11.60%  | 28.28%             | -18.41% |    -0.65 |       76 | 37.10%     | ok               |

## DIS Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 53.03%   | 23.23%             | -10.17% |     1.38 |       50 | 29.78%     | ok               |
|          40 | 21.30%   | 23.23%             | -18.75% |     0.54 |       65 | 37.94%     | ok               |
|          45 | 18.49%   | 23.23%             | -16.54% |     0.51 |       51 | 33.44%     | ok               |
|          35 | 9.63%    | 23.23%             | -25.30% |     0.3  |       73 | 43.93%     | ok               |
|          15 | 8.52%    | 23.23%             | -32.73% |     0.27 |       79 | 56.74%     | ok               |

## DOGE-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -1.36%   | -65.55%            | -50.23% |     0.17 |       60 | 20.88%     | ok               |
|          15 | -8.45%   | -65.55%            | -60.29% |     0.17 |       81 | 62.45%     | ok               |
|          20 | -10.80%  | -65.55%            | -60.01% |     0.12 |       79 | 56.51%     | ok               |
|          40 | -7.78%   | -65.55%            | -62.29% |     0.11 |       60 | 34.87%     | ok               |
|          30 | -12.13%  | -65.55%            | -61.52% |     0.08 |       68 | 47.13%     | ok               |

## DOT-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -25.29%  | -81.26%            | -46.51% |    -0.28 |       54 | 19.54%     | ok               |
|          40 | -35.84%  | -81.26%            | -50.22% |    -0.39 |       56 | 31.80%     | ok               |
|          35 | -46.23%  | -81.26%            | -58.57% |    -0.41 |       70 | 37.74%     | ok               |
|          20 | -52.38%  | -81.26%            | -70.04% |    -0.42 |       90 | 52.87%     | ok               |
|          15 | -59.42%  | -81.26%            | -76.85% |    -0.47 |       81 | 57.28%     | ok               |

## DXY-INDEX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -0.39%   | -3.98%             | -5.13%  |    -0.05 |       40 | 30.74%     | ok               |
|          40 | -2.76%   | -3.98%             | -6.56%  |    -0.38 |       68 | 46.54%     | ok               |
|          45 | -2.74%   | -3.98%             | -6.67%  |    -0.41 |       62 | 37.45%     | ok               |
|          15 | -6.92%   | -3.98%             | -11.14% |    -0.69 |       95 | 72.73%     | ok               |
|          30 | -5.79%   | -3.98%             | -9.30%  |    -0.73 |       78 | 56.93%     | ok               |

## EEM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -3.50%   | 35.90%             | -26.88% |    -0.03 |       68 | 45.59%     | ok               |
|          25 | -4.56%   | 35.90%             | -25.42% |    -0.06 |       68 | 43.93%     | ok               |
|          30 | -5.70%   | 35.90%             | -24.14% |    -0.1  |       68 | 42.26%     | ok               |
|          15 | -6.29%   | 35.90%             | -28.49% |    -0.1  |       74 | 49.42%     | ok               |
|          35 | -7.59%   | 35.90%             | -23.88% |    -0.17 |       72 | 40.10%     | ok               |

## EFA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -3.40%   | 28.00%             | -10.29% |    -0.07 |       62 | 49.08%     | ok               |
|          20 | -10.35%  | 28.00%             | -13.88% |    -0.38 |       67 | 46.26%     | ok               |
|          30 | -11.02%  | 28.00%             | -13.32% |    -0.45 |       64 | 38.77%     | ok               |
|          25 | -11.46%  | 28.00%             | -15.57% |    -0.45 |       68 | 42.43%     | ok               |
|          40 | -10.91%  | 28.00%             | -15.01% |    -0.49 |       60 | 34.28%     | ok               |

## EOG Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -12.96%  | 18.92%             | -34.41% |    -0.23 |       46 | 32.11%     | ok               |
|          40 | -17.04%  | 18.92%             | -36.18% |    -0.33 |       60 | 35.44%     | ok               |
|          50 | -20.56%  | 18.92%             | -35.63% |    -0.46 |       50 | 29.62%     | ok               |
|          35 | -22.90%  | 18.92%             | -38.93% |    -0.46 |       73 | 39.93%     | ok               |
|          30 | -30.76%  | 18.92%             | -47.65% |    -0.65 |       76 | 44.43%     | ok               |

## ETC-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 6.38%    | -64.77%            | -43.95% |     0.26 |       48 | 33.52%     | ok               |
|          30 | 2.98%    | -64.77%            | -46.79% |     0.22 |       56 | 36.78%     | ok               |
|          50 | -6.53%   | -64.77%            | -30.22% |     0.02 |       32 | 18.58%     | ok               |
|          40 | -11.46%  | -64.77%            | -41.85% |    -0.03 |       52 | 27.39%     | ok               |
|          45 | -11.45%  | -64.77%            | -35.44% |    -0.05 |       38 | 22.22%     | ok               |

## ETH-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 135.96%  | -28.91%            | -30.11% |     1.25 |       63 | 48.28%     | ok               |
|          30 | 98.20%   | -28.91%            | -32.89% |     1    |       65 | 56.13%     | ok               |
|          40 | 76.42%   | -28.91%            | -33.11% |     0.94 |       64 | 40.42%     | ok               |
|          25 | 74.45%   | -28.91%            | -40.90% |     0.84 |       63 | 59.96%     | ok               |
|          45 | 53.45%   | -28.91%            | -34.50% |     0.76 |       68 | 36.78%     | ok               |

## EWJ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -18.53%  | 29.02%             | -30.00% |    -0.54 |       58 | 40.93%     | ok               |
|          15 | -22.44%  | 29.02%             | -31.15% |    -0.64 |       69 | 44.26%     | ok               |
|          25 | -22.79%  | 29.02%             | -29.85% |    -0.71 |       62 | 39.77%     | ok               |
|          30 | -24.40%  | 29.02%             | -29.40% |    -0.83 |       70 | 38.44%     | ok               |
|          45 | -25.13%  | 29.02%             | -28.91% |    -1    |       66 | 29.78%     | ok               |

## FCX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 15.58%   | 5.86%              | -30.39% |     0.36 |       54 | 33.78%     | ok               |
|          50 | 9.04%    | 5.86%              | -26.57% |     0.27 |       58 | 29.95%     | ok               |
|          40 | 1.25%    | 5.86%              | -42.89% |     0.17 |       64 | 38.60%     | ok               |
|          30 | -16.13%  | 5.86%              | -46.84% |    -0.07 |       67 | 46.09%     | ok               |
|          35 | -20.35%  | 5.86%              | -50.12% |    -0.15 |       69 | 43.76%     | ok               |

## FET-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 18.10%   | -81.22%            | -59.58% |     0.43 |       69 | 58.43%     | ok               |
|          20 | -23.48%  | -81.22%            | -66.17% |     0.08 |       82 | 54.60%     | ok               |
|          25 | -30.34%  | -81.22%            | -65.31% |    -0.02 |       81 | 48.66%     | ok               |
|          30 | -44.23%  | -81.22%            | -66.52% |    -0.25 |       79 | 44.25%     | ok               |
|          45 | -37.46%  | -81.22%            | -51.19% |    -0.4  |       52 | 22.41%     | ok               |

## FIL-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -0.90%   | -76.75%            | -58.54% |     0.22 |       65 | 39.27%     | ok               |
|          40 | -17.32%  | -76.75%            | -57.60% |    -0.01 |       52 | 31.23%     | ok               |
|          35 | -27.12%  | -76.75%            | -65.35% |    -0.13 |       64 | 34.48%     | ok               |
|          25 | -35.13%  | -76.75%            | -70.65% |    -0.18 |       76 | 42.91%     | ok               |
|          15 | -39.54%  | -76.75%            | -72.83% |    -0.19 |       89 | 52.11%     | ok               |

## FXI Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -0.43%   | 24.62%             | -21.68% |     0.08 |       51 | 35.11%     | ok               |
|          25 | -2.11%   | 24.62%             | -22.57% |     0.03 |       48 | 31.78%     | ok               |
|          20 | -3.57%   | 24.62%             | -24.53% |    -0    |       48 | 33.11%     | ok               |
|          30 | -4.25%   | 24.62%             | -23.91% |    -0.02 |       46 | 30.45%     | ok               |
|          35 | -6.68%   | 24.62%             | -27.53% |    -0.09 |       48 | 27.79%     | ok               |

## GDX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -2.80%   | 120.51%            | -31.05% |     0.12 |       82 | 51.25%     | ok               |
|          40 | -4.94%   | 120.51%            | -34.42% |     0.05 |       66 | 38.94%     | ok               |
|          30 | -6.36%   | 120.51%            | -34.29% |     0.04 |       68 | 45.09%     | ok               |
|          35 | -10.44%  | 120.51%            | -38.67% |    -0.03 |       74 | 41.60%     | ok               |
|          25 | -15.19%  | 120.51%            | -42.42% |    -0.09 |       72 | 46.92%     | ok               |

## GDXJ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -16.79%  | 113.84%            | -34.84% |    -0.05 |       72 | 51.58%     | ok               |
|          35 | -28.11%  | 113.84%            | -38.09% |    -0.29 |       70 | 41.76%     | ok               |
|          30 | -30.10%  | 113.84%            | -36.01% |    -0.32 |       70 | 44.43%     | ok               |
|          25 | -34.34%  | 113.84%            | -39.67% |    -0.37 |       75 | 47.59%     | ok               |
|          40 | -30.85%  | 113.84%            | -46.16% |    -0.38 |       64 | 39.27%     | ok               |

## GE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 3.98%    | 106.39%            | -21.25% |     0.18 |       62 | 34.44%     | ok               |
|          45 | -8.15%   | 106.39%            | -21.88% |    -0.07 |       74 | 37.44%     | ok               |
|          30 | -13.89%  | 106.39%            | -27.82% |    -0.15 |       80 | 49.08%     | ok               |
|          25 | -14.29%  | 106.39%            | -29.91% |    -0.16 |       76 | 50.92%     | ok               |
|          20 | -14.76%  | 106.39%            | -25.38% |    -0.16 |       76 | 53.58%     | ok               |

## GLD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | 21.05%   | 58.69%             | -13.87% |     0.54 |       48 | 47.59%     | ok               |
|          20 | 19.41%   | 58.69%             | -13.87% |     0.51 |       49 | 49.25%     | ok               |
|          30 | 11.67%   | 58.69%             | -14.15% |     0.35 |       52 | 46.09%     | ok               |
|          35 | 8.96%    | 58.69%             | -15.57% |     0.3  |       52 | 43.43%     | ok               |
|          15 | 9.21%    | 58.69%             | -18.05% |     0.29 |       53 | 52.58%     | ok               |

## GOOGL Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 78.28%   | 55.06%             | -17.38% |     1.19 |       59 | 46.09%     | ok               |
|          30 | 75.56%   | 55.06%             | -17.55% |     1.14 |       55 | 49.92%     | ok               |
|          25 | 72.88%   | 55.06%             | -16.87% |     1.1  |       55 | 52.41%     | ok               |
|          45 | 58.29%   | 55.06%             | -11.66% |     1.03 |       52 | 38.60%     | ok               |
|          50 | 53.63%   | 55.06%             | -11.52% |     1    |       44 | 33.78%     | ok               |

## GRT-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 77.62%   | -80.11%            | -37.14% |     0.87 |       50 | 27.20%     | ok               |
|          35 | 83.96%   | -80.11%            | -29.35% |     0.87 |       66 | 40.61%     | ok               |
|          15 | 88.51%   | -80.11%            | -36.70% |     0.83 |       68 | 62.07%     | ok               |
|          30 | 73.50%   | -80.11%            | -38.70% |     0.79 |       73 | 46.55%     | ok               |
|          40 | 63.66%   | -80.11%            | -38.09% |     0.76 |       52 | 33.33%     | ok               |

## GS Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 22.58%   | 93.04%             | -20.56% |     0.5  |       66 | 55.24%     | ok               |
|          40 | 7.27%    | 93.04%             | -16.16% |     0.25 |       64 | 40.93%     | ok               |
|          20 | 7.49%    | 93.04%             | -23.19% |     0.25 |       64 | 51.91%     | ok               |
|          25 | -0.60%   | 93.04%             | -23.32% |     0.09 |       66 | 49.92%     | ok               |
|          35 | -1.92%   | 93.04%             | -19.95% |     0.06 |       68 | 44.59%     | ok               |

## HBAR-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -20.86%  | -45.99%            | -58.64% |    -0.17 |       52 | 56.19%     | ok               |
|          30 | -23.19%  | -45.99%            | -56.47% |    -0.25 |       42 | 42.14%     | ok               |
|          45 | -22.53%  | -45.99%            | -49.09% |    -0.29 |       28 | 27.09%     | ok               |
|          40 | -24.21%  | -45.99%            | -51.16% |    -0.32 |       32 | 32.78%     | ok               |
|          20 | -29.56%  | -45.99%            | -63.19% |    -0.38 |       55 | 51.51%     | ok               |

## HD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 5.97%    | -1.92%             | -17.15% |     0.23 |       69 | 44.93%     | ok               |
|          35 | 4.57%    | -1.92%             | -15.36% |     0.2  |       70 | 40.27%     | ok               |
|          25 | 2.35%    | -1.92%             | -16.67% |     0.14 |       70 | 47.42%     | ok               |
|          40 | 1.20%    | -1.92%             | -14.18% |     0.11 |       72 | 34.94%     | ok               |
|          45 | 0.41%    | -1.92%             | -12.98% |     0.08 |       48 | 30.12%     | ok               |

## HON Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -11.14%  | 5.51%              | -20.43% |    -0.28 |       64 | 30.78%     | ok               |
|          45 | -14.75%  | 5.51%              | -22.88% |    -0.38 |       66 | 35.94%     | ok               |
|          35 | -26.88%  | 5.51%              | -31.30% |    -0.71 |       87 | 47.25%     | ok               |
|          30 | -27.99%  | 5.51%              | -32.93% |    -0.71 |       87 | 52.08%     | ok               |
|          40 | -27.07%  | 5.51%              | -31.84% |    -0.75 |       74 | 40.10%     | ok               |

## HYG Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -4.33%   | -0.64%             | -7.76%  |    -0.49 |       72 | 34.44%     | ok               |
|          45 | -6.10%   | -0.64%             | -8.86%  |    -0.73 |       72 | 30.78%     | ok               |
|          35 | -6.55%   | -0.64%             | -9.66%  |    -0.75 |       81 | 36.27%     | ok               |
|          30 | -6.76%   | -0.64%             | -10.59% |    -0.75 |       89 | 39.77%     | ok               |
|          25 | -7.49%   | -0.64%             | -11.22% |    -0.81 |       91 | 42.76%     | ok               |

## IBIT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 89.38%   | -6.97%             | -19.20% |     1.11 |       48 | 43.44%     | ok               |
|          50 | 58.33%   | -6.97%             | -17.37% |     0.98 |       28 | 24.71%     | ok               |
|          45 | 56.73%   | -6.97%             | -17.37% |     0.93 |       34 | 26.25%     | ok               |
|          30 | 55.09%   | -6.97%             | -18.95% |     0.85 |       46 | 36.10%     | ok               |
|          40 | 44.41%   | -6.97%             | -22.57% |     0.78 |       42 | 29.34%     | ok               |

## IBM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -15.16%  | 32.14%             | -49.43% |    -0.07 |       89 | 62.40%     | ok               |
|          35 | -19.60%  | 32.14%             | -47.10% |    -0.19 |       65 | 47.25%     | ok               |
|          30 | -21.28%  | 32.14%             | -48.94% |    -0.22 |       71 | 50.42%     | ok               |
|          20 | -27.33%  | 32.14%             | -53.45% |    -0.3  |       75 | 55.41%     | ok               |
|          50 | -27.56%  | 32.14%             | -45.97% |    -0.39 |       46 | 36.11%     | ok               |

## ICP-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 6.42%    | -57.72%            | -43.16% |     0.32 |       72 | 40.04%     | ok               |
|          35 | -2.13%   | -57.72%            | -52.30% |     0.21 |       64 | 34.67%     | ok               |
|          40 | -4.83%   | -57.72%            | -46.01% |     0.17 |       60 | 30.84%     | ok               |
|          15 | -35.32%  | -57.72%            | -65.32% |    -0.01 |       83 | 52.49%     | ok               |
|          20 | -34.13%  | -57.72%            | -67.56% |    -0.01 |       85 | 48.66%     | ok               |

## IEF Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -5.84%   | -3.18%             | -10.18% |    -0.67 |       74 | 43.59%     | ok               |
|          15 | -7.06%   | -3.18%             | -10.91% |    -0.8  |       73 | 45.26%     | ok               |
|          40 | -8.17%   | -3.18%             | -10.75% |    -1.17 |       62 | 27.45%     | ok               |
|          45 | -8.15%   | -3.18%             | -10.86% |    -1.2  |       60 | 25.12%     | ok               |
|          50 | -7.33%   | -3.18%             | -9.32%  |    -1.24 |       56 | 21.63%     | ok               |

## IEMG Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | 0.83%    | 31.83%             | -23.73% |     0.09 |       63 | 44.43%     | ok               |
|          20 | -0.88%   | 31.83%             | -25.26% |     0.04 |       61 | 46.09%     | ok               |
|          30 | -2.46%   | 31.83%             | -24.73% |    -0.01 |       64 | 42.10%     | ok               |
|          35 | -2.63%   | 31.83%             | -21.81% |    -0.02 |       69 | 40.77%     | ok               |
|          40 | -5.20%   | 31.83%             | -18.43% |    -0.11 |       68 | 38.27%     | ok               |

## INJ-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 33.68%   | -38.22%            | -42.48% |     0.53 |       52 | 35.63%     | ok               |
|          40 | 31.33%   | -38.22%            | -33.49% |     0.51 |       42 | 32.38%     | ok               |
|          45 | 13.61%   | -38.22%            | -39.58% |     0.35 |       48 | 26.05%     | ok               |
|          25 | -9.09%   | -38.22%            | -56.45% |     0.18 |       59 | 41.76%     | ok               |
|          15 | -11.08%  | -38.22%            | -64.35% |     0.18 |       68 | 46.74%     | ok               |

## INTC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 112.45%  | 76.53%             | -49.32% |     0.89 |       60 | 35.77%     | ok               |
|          50 | 105.85%  | 76.53%             | -48.35% |     0.88 |       64 | 31.95%     | ok               |
|          40 | 89.14%   | 76.53%             | -55.86% |     0.78 |       68 | 39.93%     | ok               |
|          15 | 92.67%   | 76.53%             | -53.65% |     0.76 |       76 | 60.57%     | ok               |
|          20 | 81.94%   | 76.53%             | -52.47% |     0.73 |       82 | 57.07%     | ok               |

## INTU Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 8.52%    | -52.34%            | -34.18% |     0.26 |       67 | 28.79%     | ok               |
|          35 | 4.42%    | -52.34%            | -41.63% |     0.2  |       69 | 41.10%     | ok               |
|          45 | 2.53%    | -52.34%            | -36.41% |     0.16 |       65 | 32.78%     | ok               |
|          40 | 0.89%    | -52.34%            | -38.72% |     0.13 |       69 | 36.27%     | ok               |
|          25 | -3.37%   | -52.34%            | -35.24% |     0.09 |       71 | 50.25%     | ok               |

## ITA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 0.31%    | 57.64%             | -26.15% |     0.1  |       73 | 59.40%     | ok               |
|          30 | 0.52%    | 57.64%             | -22.33% |     0.09 |       72 | 47.09%     | ok               |
|          50 | -0.54%   | 57.64%             | -21.48% |     0.05 |       68 | 34.78%     | ok               |
|          35 | -4.77%   | 57.64%             | -22.44% |    -0.07 |       72 | 43.43%     | ok               |
|          20 | -5.79%   | 57.64%             | -26.56% |    -0.07 |       72 | 53.74%     | ok               |

## IWM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd    |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:-------|---------:|---------:|:-----------|:-----------------|
|          25 | 15.74%   | 33.14%             | -8.39% |     0.59 |       54 | 35.94%     | ok               |
|          20 | 11.17%   | 33.14%             | -9.67% |     0.44 |       64 | 36.94%     | ok               |
|          30 | 10.39%   | 33.14%             | -8.62% |     0.42 |       56 | 34.44%     | ok               |
|          40 | 8.67%    | 33.14%             | -9.21% |     0.4  |       44 | 29.28%     | ok               |
|          35 | 8.33%    | 33.14%             | -9.25% |     0.36 |       52 | 31.95%     | ok               |

## JNJ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 20.77%   | 86.58%             | -10.97% |     0.78 |       40 | 37.10%     | ok               |
|          15 | 15.92%   | 86.58%             | -18.02% |     0.54 |       58 | 54.41%     | ok               |
|          45 | 10.43%   | 86.58%             | -13.35% |     0.43 |       46 | 40.77%     | ok               |
|          30 | 10.93%   | 86.58%             | -17.51% |     0.42 |       60 | 47.92%     | ok               |
|          20 | 10.56%   | 86.58%             | -17.61% |     0.4  |       64 | 50.92%     | ok               |

## JPM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 0.07%    | 60.24%             | -15.90% |     0.06 |       52 | 32.11%     | ok               |
|          45 | -10.24%  | 60.24%             | -21.91% |    -0.27 |       56 | 34.78%     | ok               |
|          20 | -27.14%  | 60.24%             | -35.58% |    -0.64 |       88 | 49.25%     | ok               |
|          40 | -22.56%  | 60.24%             | -28.47% |    -0.69 |       68 | 37.44%     | ok               |
|          35 | -25.11%  | 60.24%             | -29.39% |    -0.77 |       78 | 41.10%     | ok               |

## KO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 28.01%   | 54.11%             | -8.64%  |     0.93 |       54 | 39.93%     | ok               |
|          40 | 23.14%   | 54.11%             | -9.28%  |     0.84 |       58 | 35.44%     | ok               |
|          35 | 23.66%   | 54.11%             | -8.73%  |     0.82 |       58 | 38.44%     | ok               |
|          25 | 21.78%   | 54.11%             | -10.61% |     0.75 |       60 | 42.60%     | ok               |
|          50 | 10.05%   | 54.11%             | -16.13% |     0.44 |       44 | 29.62%     | ok               |

## LDO-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 226.72%  | -66.83%            | -38.70% |     1.24 |       76 | 60.54%     | ok               |
|          20 | 132.98%  | -66.83%            | -41.80% |     0.98 |       79 | 55.36%     | ok               |
|          30 | 86.85%   | -66.83%            | -47.94% |     0.82 |       70 | 48.28%     | ok               |
|          25 | 84.97%   | -66.83%            | -46.04% |     0.8  |       76 | 52.68%     | ok               |
|          35 | 5.31%    | -66.83%            | -58.88% |     0.3  |       84 | 41.19%     | ok               |

## LIN Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -3.11%   | 16.72%             | -23.00% |    -0.04 |       64 | 48.09%     | ok               |
|          25 | -3.04%   | 16.72%             | -22.01% |    -0.04 |       71 | 45.09%     | ok               |
|          15 | -4.98%   | 16.72%             | -23.68% |    -0.09 |       70 | 51.08%     | ok               |
|          45 | -3.83%   | 16.72%             | -17.04% |    -0.1  |       48 | 25.79%     | ok               |
|          30 | -6.27%   | 16.72%             | -20.61% |    -0.15 |       72 | 42.26%     | ok               |

## LINK-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 36.57%   | -32.33%            | -34.21% |     0.56 |       66 | 38.89%     | ok               |
|          30 | 31.60%   | -32.33%            | -35.01% |     0.52 |       72 | 43.30%     | ok               |
|          40 | 29.06%   | -32.33%            | -36.88% |     0.5  |       58 | 33.14%     | ok               |
|          50 | 25.00%   | -32.33%            | -31.02% |     0.47 |       46 | 24.14%     | ok               |
|          45 | 25.18%   | -32.33%            | -34.80% |     0.47 |       54 | 29.69%     | ok               |

## LLY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -2.85%   | 52.73%             | -39.36% |     0.06 |       52 | 35.61%     | ok               |
|          15 | -15.02%  | 52.73%             | -48.12% |    -0.09 |       70 | 60.23%     | ok               |
|          45 | -16.01%  | 52.73%             | -44.03% |    -0.19 |       62 | 39.43%     | ok               |
|          20 | -26.83%  | 52.73%             | -51.14% |    -0.33 |       77 | 55.41%     | ok               |
|          40 | -24.87%  | 52.73%             | -46.22% |    -0.35 |       72 | 42.60%     | ok               |

## LRCX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -16.49%  | 98.78%             | -56.69% |     0.06 |       82 | 54.08%     | ok               |
|          50 | -11.18%  | 98.78%             | -48.71% |     0.05 |       76 | 35.77%     | ok               |
|          35 | -21.11%  | 98.78%             | -59.36% |    -0.04 |       84 | 44.76%     | ok               |
|          20 | -23.72%  | 98.78%             | -62.91% |    -0.04 |       87 | 49.92%     | ok               |
|          40 | -24.60%  | 98.78%             | -56.29% |    -0.1  |       76 | 42.43%     | ok               |

## LTC-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 36.28%   | -48.43%            | -36.35% |     0.59 |       66 | 45.02%     | ok               |
|          30 | 29.79%   | -48.43%            | -32.28% |     0.52 |       67 | 51.53%     | ok               |
|          25 | 28.29%   | -48.43%            | -35.65% |     0.5  |       67 | 54.21%     | ok               |
|          45 | 25.71%   | -48.43%            | -36.44% |     0.49 |       58 | 33.72%     | ok               |
|          40 | 10.18%   | -48.43%            | -41.60% |     0.31 |       56 | 39.85%     | ok               |

## MCD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 7.92%    | 7.53%              | -9.22%  |     0.38 |       50 | 26.12%     | ok               |
|          30 | 7.05%    | 7.53%              | -22.20% |     0.29 |       77 | 41.26%     | ok               |
|          35 | 5.59%    | 7.53%              | -16.97% |     0.26 |       69 | 38.44%     | ok               |
|          25 | 4.82%    | 7.53%              | -23.93% |     0.22 |       75 | 43.93%     | ok               |
|          20 | 0.55%    | 7.53%              | -24.58% |     0.08 |       77 | 47.09%     | ok               |

## META Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -17.09%  | 22.24%             | -37.10% |    -0.21 |       66 | 38.44%     | ok               |
|          40 | -20.59%  | 22.24%             | -40.49% |    -0.26 |       66 | 41.76%     | ok               |
|          50 | -21.65%  | 22.24%             | -38.90% |    -0.33 |       66 | 33.94%     | ok               |
|          30 | -31.84%  | 22.24%             | -44.52% |    -0.47 |       70 | 49.58%     | ok               |
|          35 | -31.90%  | 22.24%             | -40.80% |    -0.5  |       79 | 47.25%     | ok               |

## MPC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 20.28%   | 115.51%            | -18.24% |     0.45 |       52 | 41.43%     | ok               |
|          40 | 18.30%   | 115.51%            | -20.11% |     0.41 |       62 | 48.09%     | ok               |
|          35 | 17.46%   | 115.51%            | -30.41% |     0.39 |       68 | 50.75%     | ok               |
|          45 | 16.22%   | 115.51%            | -19.46% |     0.38 |       58 | 45.42%     | ok               |
|          30 | 11.57%   | 115.51%            | -33.74% |     0.31 |       70 | 53.41%     | ok               |

## MRK Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -14.60%  | 11.29%             | -28.39% |    -0.19 |       85 | 53.08%     | ok               |
|          25 | -15.36%  | 11.29%             | -31.07% |    -0.23 |       72 | 45.26%     | ok               |
|          20 | -19.51%  | 11.29%             | -29.34% |    -0.33 |       77 | 48.59%     | ok               |
|          50 | -16.04%  | 11.29%             | -23.01% |    -0.34 |       58 | 29.62%     | ok               |
|          45 | -18.12%  | 11.29%             | -25.38% |    -0.37 |       59 | 32.95%     | ok               |

## MS Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 3.17%    | 86.41%             | -19.99% |     0.16 |       66 | 38.60%     | ok               |
|          15 | 0.85%    | 86.41%             | -22.02% |     0.12 |       72 | 56.57%     | ok               |
|          20 | -1.39%   | 86.41%             | -25.68% |     0.06 |       71 | 52.41%     | ok               |
|          30 | -3.98%   | 86.41%             | -27.79% |    -0.01 |       71 | 47.59%     | ok               |
|          25 | -5.49%   | 86.41%             | -28.36% |    -0.04 |       69 | 49.75%     | ok               |

## MSFT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -15.87%  | 13.72%             | -25.23% |    -0.37 |       72 | 36.77%     | ok               |
|          50 | -19.62%  | 13.72%             | -26.37% |    -0.51 |       62 | 31.45%     | ok               |
|          30 | -26.37%  | 13.72%             | -37.80% |    -0.57 |       81 | 50.58%     | ok               |
|          35 | -25.48%  | 13.72%             | -36.02% |    -0.58 |       75 | 46.26%     | ok               |
|          40 | -25.13%  | 13.72%             | -35.43% |    -0.59 |       71 | 40.43%     | ok               |

## MU Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 107.92%  | 436.20%            | -61.12% |     0.88 |       60 | 44.93%     | ok               |
|          45 | 95.67%   | 436.20%            | -62.28% |     0.84 |       62 | 42.10%     | ok               |
|          15 | 105.01%  | 436.20%            | -61.96% |     0.82 |       58 | 58.07%     | ok               |
|          30 | 88.04%   | 436.20%            | -64.76% |     0.79 |       53 | 49.42%     | ok               |
|          35 | 82.84%   | 436.20%            | -65.13% |     0.77 |       65 | 47.09%     | ok               |

## NEAR-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 246.37%  | 50.55%             | -41.76% |     1.37 |       42 | 32.76%     | ok               |
|          50 | 207.33%  | 50.55%             | -43.09% |     1.36 |       32 | 22.61%     | ok               |
|          45 | 190.69%  | 50.55%             | -38.08% |     1.23 |       44 | 28.74%     | ok               |
|          35 | 168.71%  | 50.55%             | -51.21% |     1.14 |       62 | 36.59%     | ok               |
|          30 | 177.42%  | 50.55%             | -46.60% |     1.13 |       65 | 43.49%     | ok               |

## NEM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -4.57%   | 149.65%            | -30.50% |     0.1  |       71 | 54.08%     | ok               |
|          15 | -7.30%   | 149.65%            | -35.45% |     0.08 |       66 | 58.74%     | ok               |
|          50 | -12.51%  | 149.65%            | -33.03% |    -0.06 |       48 | 37.77%     | ok               |
|          25 | -19.14%  | 149.65%            | -39.51% |    -0.12 |       68 | 51.75%     | ok               |
|          30 | -25.86%  | 149.65%            | -39.56% |    -0.25 |       70 | 49.75%     | ok               |

## NFLX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 18.87%   | -11.36%            | -20.78% |     0.5  |       54 | 38.10%     | ok               |
|          50 | 16.23%   | -11.36%            | -16.28% |     0.48 |       44 | 29.78%     | ok               |
|          35 | 13.10%   | -11.36%            | -18.30% |     0.37 |       82 | 43.26%     | ok               |
|          15 | 6.93%    | -11.36%            | -26.59% |     0.24 |       76 | 63.89%     | ok               |
|          45 | 4.62%    | -11.36%            | -18.06% |     0.2  |       58 | 34.11%     | ok               |

## NKE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -24.14%  | -51.82%            | -33.81% |    -0.44 |       67 | 32.45%     | ok               |
|          35 | -32.71%  | -51.82%            | -42.13% |    -0.6  |       73 | 39.43%     | ok               |
|          25 | -41.87%  | -51.82%            | -51.20% |    -0.67 |       87 | 52.25%     | ok               |
|          20 | -43.61%  | -51.82%            | -49.69% |    -0.7  |       90 | 55.24%     | ok               |
|          50 | -25.61%  | -51.82%            | -39.39% |    -0.78 |       50 | 19.80%     | ok               |

## NOW Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -3.88%   | -42.42%            | -42.66% |     0.17 |       81 | 51.91%     | ok               |
|          20 | -7.08%   | -42.42%            | -49.77% |     0.14 |       73 | 57.57%     | ok               |
|          25 | -10.77%  | -42.42%            | -47.93% |     0.09 |       73 | 55.24%     | ok               |
|          15 | -13.96%  | -42.42%            | -52.56% |     0.06 |       81 | 60.23%     | ok               |
|          35 | -16.93%  | -42.42%            | -48.24% |    -0.01 |       84 | 47.09%     | ok               |

## NVDA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -19.22%  | 19.37%             | -38.70% |    -0.14 |       76 | 51.52%     | ok               |
|          25 | -24.93%  | 19.37%             | -44.52% |    -0.26 |       81 | 47.59%     | ok               |
|          30 | -24.69%  | 19.37%             | -43.72% |    -0.27 |       82 | 44.74%     | ok               |
|          15 | -32.74%  | 19.37%             | -50.87% |    -0.37 |       82 | 55.79%     | ok               |
|          35 | -36.01%  | 19.37%             | -51.44% |    -0.54 |       92 | 41.89%     | ok               |

## OP-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 48.43%   | -86.81%            | -33.09% |     0.77 |       44 | 11.69%     | ok               |
|          45 | 37.98%   | -86.81%            | -30.78% |     0.59 |       46 | 17.82%     | ok               |
|          40 | 14.46%   | -86.81%            | -43.68% |     0.36 |       50 | 26.05%     | ok               |
|          15 | -12.17%  | -86.81%            | -55.83% |     0.15 |       75 | 48.28%     | ok               |
|          30 | -15.35%  | -86.81%            | -57.66% |     0.07 |       72 | 36.21%     | ok               |

## ORCL Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 128.21%  | -19.34%            | -37.59% |     0.98 |       67 | 59.57%     | ok               |
|          45 | 84.40%   | -19.34%            | -32.35% |     0.85 |       54 | 37.27%     | ok               |
|          25 | 83.49%   | -19.34%            | -31.06% |     0.79 |       59 | 52.08%     | ok               |
|          35 | 74.80%   | -19.34%            | -31.95% |     0.76 |       60 | 46.26%     | ok               |
|          20 | 78.37%   | -19.34%            | -32.60% |     0.76 |       68 | 55.24%     | ok               |

## OXY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 8.32%    | -14.71%            | -28.48% |     0.26 |       67 | 43.43%     | ok               |
|          35 | 6.50%    | -14.71%            | -26.37% |     0.23 |       72 | 38.60%     | ok               |
|          50 | -1.22%   | -14.71%            | -26.34% |     0.08 |       48 | 27.95%     | ok               |
|          40 | -2.03%   | -14.71%            | -28.30% |     0.08 |       58 | 35.11%     | ok               |
|          25 | -6.78%   | -14.71%            | -38.51% |     0.02 |       75 | 47.09%     | ok               |

## PEP Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 15.75%   | -13.98%            | -11.62% |     0.65 |       40 | 26.62%     | ok               |
|          45 | 4.21%    | -13.98%            | -14.22% |     0.21 |       54 | 30.45%     | ok               |
|          30 | 3.01%    | -13.98%            | -21.35% |     0.16 |       70 | 46.09%     | ok               |
|          35 | 1.41%    | -13.98%            | -21.42% |     0.11 |       73 | 40.43%     | ok               |
|          40 | -1.46%   | -13.98%            | -18.04% |     0    |       68 | 35.77%     | ok               |

## PEPE-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -40.82%  | -63.96%            | -65.53% |    -0.05 |       81 | 61.69%     | ok               |
|          30 | -37.18%  | -63.96%            | -60.19% |    -0.12 |       74 | 47.13%     | ok               |
|          20 | -42.14%  | -63.96%            | -63.48% |    -0.14 |       87 | 57.28%     | ok               |
|          35 | -42.86%  | -63.96%            | -60.83% |    -0.28 |       66 | 43.30%     | ok               |
|          25 | -53.14%  | -63.96%            | -64.37% |    -0.35 |       88 | 52.11%     | ok               |

## PFE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -15.07%  | 0.29%              | -25.81% |    -0.45 |       52 | 22.96%     | ok               |
|          50 | -14.14%  | 0.29%              | -27.79% |    -0.46 |       40 | 19.63%     | ok               |
|          40 | -18.08%  | 0.29%              | -30.60% |    -0.53 |       74 | 28.12%     | ok               |
|          35 | -25.97%  | 0.29%              | -36.12% |    -0.78 |       84 | 34.61%     | ok               |
|          30 | -33.58%  | 0.29%              | -42.77% |    -1.02 |       79 | 37.60%     | ok               |

## PG Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -5.61%   | 3.26%              | -20.08% |    -0.16 |       52 | 30.78%     | ok               |
|          35 | -8.83%   | 3.26%              | -18.99% |    -0.27 |       60 | 34.28%     | ok               |
|          45 | -13.61%  | 3.26%              | -22.00% |    -0.5  |       52 | 28.45%     | ok               |
|          30 | -17.11%  | 3.26%              | -24.55% |    -0.58 |       62 | 37.44%     | ok               |
|          25 | -19.00%  | 3.26%              | -25.84% |    -0.65 |       74 | 38.94%     | ok               |

## PM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | -2.57%   | 90.20%             | -34.56% |     0.03 |       82 | 44.26%     | ok               |
|          20 | -5.12%   | 90.20%             | -36.03% |    -0.02 |       81 | 52.91%     | ok               |
|          30 | -5.63%   | 90.20%             | -37.61% |    -0.03 |       77 | 47.75%     | ok               |
|          50 | -9.22%   | 90.20%             | -36.94% |    -0.16 |       66 | 35.44%     | ok               |
|          40 | -11.18%  | 90.20%             | -39.92% |    -0.2  |       76 | 40.60%     | ok               |

## POL-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | 10.29%   | -58.77%            | -46.25% |     0.33 |       79 | 53.83%     | ok               |
|          50 | 10.08%   | -58.77%            | -30.34% |     0.3  |       52 | 20.50%     | ok               |
|          30 | 4.76%    | -58.77%            | -46.25% |     0.27 |       87 | 48.85%     | ok               |
|          20 | 2.91%    | -58.77%            | -48.58% |     0.26 |       89 | 57.85%     | ok               |
|          15 | -1.53%   | -58.77%            | -48.61% |     0.23 |       94 | 63.03%     | ok               |

## QCOM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -20.59%  | -19.77%            | -48.54% |    -0.09 |       71 | 41.93%     | ok               |
|          20 | -26.43%  | -19.77%            | -48.40% |    -0.18 |       67 | 45.26%     | ok               |
|          35 | -27.29%  | -19.77%            | -44.11% |    -0.23 |       79 | 37.60%     | ok               |
|          15 | -35.32%  | -19.77%            | -52.43% |    -0.31 |       69 | 47.92%     | ok               |
|          30 | -35.78%  | -19.77%            | -50.90% |    -0.37 |       77 | 40.10%     | ok               |

## QQQ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 6.99%    | 37.65%             | -17.16% |     0.25 |       73 | 52.41%     | ok               |
|          25 | 3.47%    | 37.65%             | -14.05% |     0.17 |       67 | 45.26%     | ok               |
|          20 | 2.22%    | 37.65%             | -14.88% |     0.14 |       79 | 48.42%     | ok               |
|          30 | -3.52%   | 37.65%             | -15.84% |    -0.01 |       72 | 43.26%     | ok               |
|          35 | -14.06%  | 37.65%             | -20.59% |    -0.34 |       80 | 39.27%     | ok               |

## RENDER-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 3.61%    | -57.83%            | -44.12% |     0.33 |       88 | 62.84%     | ok               |
|          20 | -3.66%   | -57.83%            | -48.40% |     0.25 |       89 | 57.47%     | ok               |
|          25 | -5.90%   | -57.83%            | -48.19% |     0.23 |       83 | 52.49%     | ok               |
|          50 | -20.98%  | -57.83%            | -44.12% |    -0.18 |       56 | 17.62%     | ok               |
|          30 | -44.24%  | -57.83%            | -54.95% |    -0.28 |       86 | 46.74%     | ok               |

## RTX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 27.30%   | 96.68%             | -18.66% |     0.61 |       74 | 58.74%     | ok               |
|          25 | 23.72%   | 96.68%             | -18.59% |     0.55 |       64 | 55.91%     | ok               |
|          15 | 18.16%   | 96.68%             | -19.55% |     0.45 |       69 | 62.73%     | ok               |
|          50 | 13.31%   | 96.68%             | -18.42% |     0.43 |       62 | 39.77%     | ok               |
|          30 | 16.35%   | 96.68%             | -16.99% |     0.43 |       73 | 52.91%     | ok               |

## SBUX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | 2.36%    | 40.15%             | -23.55% |     0.15 |       59 | 42.43%     | ok               |
|          40 | 0.23%    | 40.15%             | -25.43% |     0.1  |       60 | 34.28%     | ok               |
|          45 | -1.73%   | 40.15%             | -27.26% |     0.05 |       64 | 29.62%     | ok               |
|          35 | -3.94%   | 40.15%             | -26.54% |     0.01 |       62 | 37.44%     | ok               |
|          50 | -4.25%   | 40.15%             | -25.13% |    -0.02 |       52 | 25.12%     | ok               |

## SCHW Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -1.47%   | 25.61%             | -29.24% |     0.06 |       71 | 52.58%     | ok               |
|          25 | -3.28%   | 25.61%             | -28.76% |     0.02 |       67 | 50.92%     | ok               |
|          45 | -3.45%   | 25.61%             | -16.53% |    -0.04 |       62 | 31.28%     | ok               |
|          50 | -3.90%   | 25.61%             | -13.28% |    -0.08 |       54 | 28.12%     | ok               |
|          15 | -8.22%   | 25.61%             | -31.37% |    -0.09 |       80 | 56.74%     | ok               |

## SHIB-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -18.57%  | -67.59%            | -47.25% |    -0.02 |       85 | 65.71%     | ok               |
|          20 | -22.00%  | -67.59%            | -49.90% |    -0.08 |       78 | 61.11%     | ok               |
|          35 | -19.09%  | -67.59%            | -44.69% |    -0.08 |       75 | 45.79%     | ok               |
|          25 | -28.29%  | -67.59%            | -50.56% |    -0.19 |       78 | 57.66%     | ok               |
|          50 | -18.96%  | -67.59%            | -32.18% |    -0.19 |       52 | 21.07%     | ok               |

## SHY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd    |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:-------|---------:|---------:|:-----------|:-----------------|
|          30 | -2.37%   | -0.38%             | -3.30% |    -0.76 |       56 | 39.10%     | ok               |
|          40 | -2.60%   | -0.38%             | -3.58% |    -0.87 |       60 | 35.44%     | ok               |
|          35 | -2.90%   | -0.38%             | -3.61% |    -0.96 |       58 | 36.94%     | ok               |
|          45 | -2.67%   | -0.38%             | -3.43% |    -0.98 |       58 | 28.79%     | ok               |
|          50 | -2.67%   | -0.38%             | -3.40% |    -1.03 |       48 | 24.79%     | ok               |

## SKY-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -43.13%  | -46.82%            | -63.51% |    -0.4  |       77 | 56.90%     | ok               |
|          30 | -46.16%  | -46.82%            | -63.39% |    -0.55 |       85 | 46.17%     | ok               |
|          35 | -44.99%  | -46.82%            | -62.59% |    -0.58 |       76 | 37.93%     | ok               |
|          25 | -52.25%  | -46.82%            | -66.70% |    -0.67 |       78 | 49.43%     | ok               |
|          20 | -57.01%  | -46.82%            | -70.01% |    -0.74 |       81 | 53.07%     | ok               |

## SLB Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -5.18%   | 2.61%              | -25.01% |    -0.01 |       58 | 31.28%     | ok               |
|          40 | -6.15%   | 2.61%              | -26.80% |    -0.02 |       52 | 34.11%     | ok               |
|          50 | -9.10%   | 2.61%              | -27.89% |    -0.13 |       46 | 24.63%     | ok               |
|          35 | -29.41%  | 2.61%              | -43.63% |    -0.55 |       76 | 42.10%     | ok               |
|          25 | -39.50%  | 2.61%              | -52.62% |    -0.74 |       87 | 51.91%     | ok               |

## SLV Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 65.47%   | 53.18%             | -28.72% |     0.85 |       52 | 31.61%     | ok               |
|          45 | 58.36%   | 53.18%             | -31.33% |     0.78 |       63 | 33.28%     | ok               |
|          40 | 57.10%   | 53.18%             | -34.28% |     0.77 |       67 | 35.27%     | ok               |
|          20 | 60.83%   | 53.18%             | -37.05% |     0.76 |       70 | 46.26%     | ok               |
|          15 | 58.14%   | 53.18%             | -47.98% |     0.72 |       71 | 50.92%     | ok               |

## SMH Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 80.51%   | 76.27%             | -31.01% |     1.03 |       49 | 44.76%     | ok               |
|          25 | 64.19%   | 76.27%             | -32.94% |     0.91 |       46 | 43.26%     | ok               |
|          30 | 59.72%   | 76.27%             | -33.66% |     0.87 |       50 | 41.93%     | ok               |
|          35 | 47.83%   | 76.27%             | -34.03% |     0.76 |       56 | 39.93%     | ok               |
|          45 | 36.70%   | 76.27%             | -32.84% |     0.67 |       54 | 34.44%     | ok               |

## SNX-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 24.53%   | -74.46%            | -29.01% |     0.48 |       46 | 26.05%     | ok               |
|          35 | 24.46%   | -74.46%            | -42.92% |     0.47 |       52 | 30.27%     | ok               |
|          20 | 6.10%    | -74.46%            | -53.03% |     0.3  |       72 | 46.36%     | ok               |
|          45 | 2.78%    | -74.46%            | -34.25% |     0.19 |       46 | 21.07%     | ok               |
|          15 | -6.87%   | -74.46%            | -54.74% |     0.18 |       73 | 50.77%     | ok               |

## SOL-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 79.71%   | -50.24%            | -39.12% |     0.9  |       54 | 40.23%     | ok               |
|          35 | 38.14%   | -50.24%            | -43.12% |     0.58 |       68 | 45.98%     | ok               |
|          45 | 31.27%   | -50.24%            | -46.28% |     0.54 |       50 | 33.33%     | ok               |
|          25 | 18.90%   | -50.24%            | -38.08% |     0.41 |       67 | 56.32%     | ok               |
|          30 | 15.30%   | -50.24%            | -42.49% |     0.38 |       75 | 52.49%     | ok               |

## SOXX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | 65.64%   | 72.55%             | -39.65% |     0.87 |       56 | 43.26%     | ok               |
|          30 | 61.04%   | 72.55%             | -40.14% |     0.83 |       58 | 41.10%     | ok               |
|          35 | 58.62%   | 72.55%             | -38.76% |     0.82 |       58 | 38.60%     | ok               |
|          20 | 53.13%   | 72.55%             | -38.67% |     0.75 |       61 | 44.09%     | ok               |
|          15 | 39.03%   | 72.55%             | -37.72% |     0.6  |       79 | 47.75%     | ok               |

## SPY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 3.94%    | 34.17%             | -14.25% |     0.19 |       62 | 50.58%     | ok               |
|          15 | 1.42%    | 34.17%             | -16.80% |     0.11 |       68 | 53.58%     | ok               |
|          25 | -0.32%   | 34.17%             | -14.25% |     0.05 |       60 | 49.42%     | ok               |
|          30 | -5.19%   | 34.17%             | -15.53% |    -0.12 |       63 | 46.92%     | ok               |
|          35 | -6.11%   | 34.17%             | -15.58% |    -0.16 |       61 | 43.76%     | ok               |

## SUSHI-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -30.87%  | -75.75%            | -43.52% |    -0.36 |       62 | 17.82%     | ok               |
|          15 | -57.57%  | -75.75%            | -78.02% |    -0.47 |       83 | 54.60%     | ok               |
|          20 | -56.70%  | -75.75%            | -77.38% |    -0.51 |       84 | 50.96%     | ok               |
|          45 | -43.65%  | -75.75%            | -58.64% |    -0.55 |       64 | 24.33%     | ok               |
|          35 | -52.59%  | -75.75%            | -71.77% |    -0.59 |       77 | 37.93%     | ok               |

## T Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 66.55%   | 14.86%             | -15.08% |     1.06 |       71 | 66.39%     | ok               |
|          25 | 62.97%   | 14.86%             | -17.66% |     1.06 |       66 | 59.57%     | ok               |
|          20 | 62.44%   | 14.86%             | -18.13% |     1.04 |       66 | 61.90%     | ok               |
|          30 | 52.21%   | 14.86%             | -17.01% |     0.94 |       68 | 57.57%     | ok               |
|          35 | 34.31%   | 14.86%             | -14.49% |     0.71 |       76 | 52.91%     | ok               |

## TGT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -6.39%   | 12.08%             | -32.83% |    -0.05 |       60 | 37.77%     | ok               |
|          25 | -8.35%   | 12.08%             | -34.56% |    -0.08 |       68 | 40.93%     | ok               |
|          20 | -11.42%  | 12.08%             | -36.83% |    -0.13 |       86 | 45.42%     | ok               |
|          45 | -9.89%   | 12.08%             | -26.12% |    -0.17 |       50 | 29.28%     | ok               |
|          35 | -13.09%  | 12.08%             | -30.71% |    -0.23 |       60 | 34.11%     | ok               |

## TIA-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -33.59%  | -79.40%            | -66.94% |     0.05 |       93 | 60.54%     | ok               |
|          20 | -39.05%  | -79.40%            | -68.67% |    -0.06 |       87 | 54.60%     | ok               |
|          25 | -37.18%  | -79.40%            | -69.36% |    -0.06 |       90 | 49.43%     | ok               |
|          35 | -29.44%  | -79.40%            | -65.55% |    -0.07 |       76 | 37.93%     | ok               |
|          30 | -45.09%  | -79.40%            | -74.75% |    -0.2  |       85 | 44.25%     | ok               |

## TLT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -7.83%   | -12.60%            | -12.51% |    -0.87 |       32 | 16.81%     | ok               |
|          40 | -14.00%  | -12.60%            | -17.65% |    -1.23 |       50 | 25.46%     | ok               |
|          45 | -12.92%  | -12.60%            | -15.17% |    -1.35 |       44 | 20.47%     | ok               |
|          30 | -21.48%  | -12.60%            | -22.12% |    -1.62 |       68 | 34.94%     | ok               |
|          35 | -20.50%  | -12.60%            | -21.15% |    -1.71 |       68 | 29.95%     | ok               |

## TMO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 45.90%   | 25.27%             | -8.17%  |     0.99 |       50 | 35.11%     | ok               |
|          45 | 44.88%   | 25.27%             | -9.69%  |     0.93 |       54 | 40.10%     | ok               |
|          40 | 37.94%   | 25.27%             | -11.54% |     0.8  |       59 | 45.26%     | ok               |
|          35 | 40.76%   | 25.27%             | -13.84% |     0.79 |       67 | 50.58%     | ok               |
|          20 | 41.41%   | 25.27%             | -22.89% |     0.75 |       75 | 62.40%     | ok               |

## TMUS Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -5.23%   | -6.90%             | -41.04% |     0.01 |       68 | 58.74%     | ok               |
|          30 | -6.51%   | -6.90%             | -33.05% |    -0.04 |       74 | 45.92%     | ok               |
|          25 | -9.16%   | -6.90%             | -39.29% |    -0.09 |       75 | 48.92%     | ok               |
|          20 | -10.70%  | -6.90%             | -39.79% |    -0.12 |       74 | 53.08%     | ok               |
|          50 | -10.15%  | -6.90%             | -32.38% |    -0.22 |       58 | 31.95%     | ok               |

## TRX-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 19.21%   | 14.00%             | -18.79% |     0.65 |       52 | 39.46%     | ok               |
|          50 | 10.05%   | 14.00%             | -22.22% |     0.41 |       46 | 33.52%     | ok               |
|          35 | 11.14%   | 14.00%             | -21.77% |     0.4  |       60 | 46.55%     | ok               |
|          45 | 9.65%    | 14.00%             | -24.19% |     0.39 |       48 | 35.63%     | ok               |
|          30 | 9.98%    | 14.00%             | -22.90% |     0.37 |       60 | 49.04%     | ok               |

## TSLA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 47.27%   | 93.92%             | -30.57% |     0.66 |       62 | 29.95%     | ok               |
|          40 | 17.48%   | 93.92%             | -50.11% |     0.37 |       61 | 35.11%     | ok               |
|          45 | -6.85%   | 93.92%             | -52.01% |     0.11 |       67 | 32.45%     | ok               |
|          35 | -21.23%  | 93.92%             | -58.86% |    -0.04 |       72 | 37.44%     | ok               |
|          25 | -34.44%  | 93.92%             | -54.86% |    -0.21 |       70 | 44.43%     | ok               |

## TXN Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -2.53%   | 50.33%             | -43.95% |     0.09 |       70 | 31.61%     | ok               |
|          35 | -17.67%  | 50.33%             | -42.08% |    -0.15 |       84 | 45.42%     | ok               |
|          20 | -23.53%  | 50.33%             | -37.19% |    -0.19 |       74 | 55.24%     | ok               |
|          15 | -25.27%  | 50.33%             | -38.02% |    -0.21 |       79 | 59.57%     | ok               |
|          40 | -22.70%  | 50.33%             | -44.52% |    -0.25 |       78 | 42.93%     | ok               |

## UNH Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 45.70%   | -31.29%            | -26.31% |     0.68 |       74 | 48.25%     | ok               |
|          35 | 41.06%   | -31.29%            | -27.21% |     0.64 |       69 | 43.26%     | ok               |
|          15 | 40.32%   | -31.29%            | -26.07% |     0.61 |       81 | 63.39%     | ok               |
|          20 | 37.76%   | -31.29%            | -26.96% |     0.59 |       76 | 57.07%     | ok               |
|          25 | 36.56%   | -31.29%            | -24.25% |     0.59 |       74 | 53.08%     | ok               |

## UNI-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 125.08%  | -29.95%            | -22.21% |     1.11 |       52 | 26.05%     | ok               |
|          45 | 108.16%  | -29.95%            | -30.17% |     0.98 |       58 | 33.72%     | ok               |
|          40 | 81.07%   | -29.95%            | -43.84% |     0.82 |       62 | 40.04%     | ok               |
|          35 | 66.33%   | -29.95%            | -48.64% |     0.73 |       64 | 45.21%     | ok               |
|          30 | 5.36%    | -29.95%            | -60.31% |     0.33 |       80 | 50.00%     | ok               |

## UPS Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -16.78%  | -18.87%            | -24.11% |    -0.31 |       44 | 25.29%     | ok               |
|          40 | -18.72%  | -18.87%            | -25.98% |    -0.31 |       60 | 34.78%     | ok               |
|          20 | -25.84%  | -18.87%            | -33.47% |    -0.4  |       78 | 51.08%     | ok               |
|          15 | -28.28%  | -18.87%            | -35.66% |    -0.45 |       80 | 54.58%     | ok               |
|          25 | -29.58%  | -18.87%            | -36.37% |    -0.5  |       71 | 47.92%     | ok               |

## USO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 11.27%   | 71.01%             | -37.66% |     0.3  |       67 | 42.43%     | ok               |
|          20 | 9.68%    | 71.01%             | -40.99% |     0.28 |       73 | 38.77%     | ok               |
|          45 | 3.06%    | 71.01%             | -33.97% |     0.18 |       48 | 25.79%     | ok               |
|          25 | -2.41%   | 71.01%             | -42.17% |     0.11 |       73 | 36.11%     | ok               |
|          50 | -4.05%   | 71.01%             | -28.71% |     0.06 |       50 | 23.96%     | ok               |

## VEA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 2.17%    | 34.93%             | -17.27% |     0.14 |       58 | 49.92%     | ok               |
|          20 | -1.45%   | 34.93%             | -17.78% |    -0    |       59 | 47.42%     | ok               |
|          25 | -5.88%   | 34.93%             | -18.46% |    -0.19 |       59 | 45.26%     | ok               |
|          30 | -7.02%   | 34.93%             | -18.84% |    -0.25 |       64 | 41.26%     | ok               |
|          35 | -7.67%   | 34.93%             | -17.88% |    -0.29 |       50 | 38.77%     | ok               |

## VIXY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -55.68%  | -53.00%            | -70.53% |    -0.66 |       34 | 8.82%      | ok               |
|          45 | -64.29%  | -53.00%            | -75.03% |    -0.84 |       54 | 13.64%     | ok               |
|          40 | -73.26%  | -53.00%            | -81.61% |    -1.01 |       70 | 17.80%     | ok               |
|          35 | -80.39%  | -53.00%            | -85.57% |    -1.17 |       96 | 24.63%     | ok               |
|          30 | -84.95%  | -53.00%            | -91.70% |    -1.2  |      100 | 31.95%     | ok               |

## VNQ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -7.44%   | 13.63%             | -22.16% |    -0.24 |       69 | 43.43%     | ok               |
|          30 | -11.08%  | 13.63%             | -24.66% |    -0.41 |       71 | 40.60%     | ok               |
|          45 | -10.22%  | 13.63%             | -20.96% |    -0.43 |       60 | 28.79%     | ok               |
|          20 | -12.17%  | 13.63%             | -23.83% |    -0.44 |       74 | 46.09%     | ok               |
|          50 | -10.19%  | 13.63%             | -19.06% |    -0.45 |       50 | 25.62%     | ok               |

## VTI Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 6.06%    | 34.38%             | -13.96% |     0.26 |       63 | 50.92%     | ok               |
|          15 | -1.69%   | 34.38%             | -15.70% |     0.01 |       64 | 53.74%     | ok               |
|          25 | -4.47%   | 34.38%             | -15.00% |    -0.09 |       57 | 48.92%     | ok               |
|          40 | -8.67%   | 34.38%             | -19.77% |    -0.29 |       70 | 39.27%     | ok               |
|          35 | -10.67%  | 34.38%             | -20.22% |    -0.36 |       64 | 43.59%     | ok               |

## VWO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -7.32%   | 22.85%             | -24.01% |    -0.18 |       74 | 47.59%     | ok               |
|          20 | -7.34%   | 22.85%             | -26.14% |    -0.19 |       69 | 45.59%     | ok               |
|          50 | -7.41%   | 22.85%             | -21.18% |    -0.24 |       56 | 29.95%     | ok               |
|          45 | -8.58%   | 22.85%             | -23.26% |    -0.29 |       60 | 32.45%     | ok               |
|          40 | -9.43%   | 22.85%             | -23.57% |    -0.32 |       70 | 35.27%     | ok               |

## VZ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -3.10%   | 11.86%             | -12.96% |    -0.04 |       56 | 28.62%     | ok               |
|          20 | -22.26%  | 11.86%             | -35.02% |    -0.43 |       80 | 52.75%     | ok               |
|          25 | -19.09%  | 11.86%             | -26.32% |    -0.47 |       83 | 47.75%     | ok               |
|          35 | -18.88%  | 11.86%             | -26.97% |    -0.55 |       64 | 39.10%     | ok               |
|          45 | -18.61%  | 11.86%             | -26.23% |    -0.57 |       72 | 32.95%     | ok               |

## WFC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | -8.38%   | 36.25%             | -24.89% |    -0.11 |       75 | 43.43%     | ok               |
|          50 | -8.94%   | 36.25%             | -20.08% |    -0.22 |       58 | 32.61%     | ok               |
|          40 | -14.04%  | 36.25%             | -25.23% |    -0.34 |       70 | 40.10%     | ok               |
|          30 | -20.00%  | 36.25%             | -30.94% |    -0.35 |       80 | 46.76%     | ok               |
|          20 | -22.41%  | 36.25%             | -32.32% |    -0.36 |       80 | 52.91%     | ok               |

## WIF-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 65.43%   | -83.83%            | -40.67% |     0.7  |       67 | 50.57%     | ok               |
|          25 | 41.10%   | -83.83%            | -44.74% |     0.57 |       63 | 46.55%     | ok               |
|          15 | 29.28%   | -83.83%            | -46.21% |     0.5  |       77 | 53.83%     | ok               |
|          30 | 11.03%   | -83.83%            | -48.32% |     0.36 |       64 | 43.87%     | ok               |
|          35 | 3.46%    | -83.83%            | -52.54% |     0.27 |       62 | 37.74%     | ok               |

## WMT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 37.97%   | 88.10%             | -12.87% |     1.1  |       36 | 35.77%     | ok               |
|          45 | 36.95%   | 88.10%             | -14.82% |     1.04 |       42 | 38.27%     | ok               |
|          35 | 28.70%   | 88.10%             | -18.90% |     0.8  |       58 | 45.42%     | ok               |
|          40 | 25.32%   | 88.10%             | -19.17% |     0.74 |       50 | 39.93%     | ok               |
|          15 | 9.81%    | 88.10%             | -26.82% |     0.3  |       82 | 59.40%     | ok               |

## XBI Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 13.75%   | 56.44%             | -16.08% |     0.41 |       50 | 33.44%     | ok               |
|          45 | 9.43%    | 56.44%             | -15.46% |     0.32 |       48 | 30.95%     | ok               |
|          35 | 3.24%    | 56.44%             | -17.66% |     0.16 |       58 | 36.11%     | ok               |
|          30 | 1.08%    | 56.44%             | -17.66% |     0.11 |       60 | 37.60%     | ok               |
|          50 | 0.20%    | 56.44%             | -15.41% |     0.08 |       48 | 27.95%     | ok               |

## XLB Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -0.10%   | 14.28%             | -16.22% |     0.05 |       38 | 24.29%     | ok               |
|          40 | -1.03%   | 14.28%             | -18.60% |     0.02 |       54 | 28.79%     | ok               |
|          45 | -3.90%   | 14.28%             | -18.61% |    -0.1  |       38 | 25.96%     | ok               |
|          35 | -4.86%   | 14.28%             | -21.91% |    -0.12 |       54 | 32.11%     | ok               |
|          25 | -7.94%   | 14.28%             | -21.62% |    -0.22 |       62 | 38.60%     | ok               |

## XLC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 4.09%    | 23.25%             | -12.33% |     0.2  |       61 | 48.59%     | ok               |
|          50 | 1.60%    | 23.25%             | -12.48% |     0.12 |       64 | 36.61%     | ok               |
|          25 | 0.70%    | 23.25%             | -12.31% |     0.09 |       64 | 51.08%     | ok               |
|          40 | -0.36%   | 23.25%             | -13.38% |     0.04 |       62 | 42.26%     | ok               |
|          35 | -1.03%   | 23.25%             | -13.38% |     0.02 |       60 | 46.09%     | ok               |

## XLE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -0.76%   | 34.48%             | -25.98% |     0.06 |       58 | 38.60%     | ok               |
|          45 | -2.44%   | 34.48%             | -28.46% |     0.01 |       60 | 41.10%     | ok               |
|          30 | -5.01%   | 34.48%             | -34.77% |    -0.04 |       72 | 47.75%     | ok               |
|          20 | -9.93%   | 34.48%             | -35.29% |    -0.14 |       80 | 52.91%     | ok               |
|          15 | -11.09%  | 34.48%             | -37.43% |    -0.16 |       96 | 56.91%     | ok               |

## XLF Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 3.25%    | 37.24%             | -20.19% |     0.17 |       70 | 57.57%     | ok               |
|          20 | 2.62%    | 37.24%             | -18.63% |     0.15 |       70 | 54.91%     | ok               |
|          25 | -4.54%   | 37.24%             | -23.22% |    -0.09 |       77 | 51.75%     | ok               |
|          30 | -5.16%   | 37.24%             | -23.61% |    -0.12 |       78 | 49.75%     | ok               |
|          35 | -12.93%  | 37.24%             | -24.48% |    -0.44 |       70 | 46.26%     | ok               |

## XLI Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 1.58%    | 35.11%             | -11.06% |     0.11 |       83 | 51.25%     | ok               |
|          20 | -3.75%   | 35.11%             | -12.74% |    -0.08 |       77 | 46.42%     | ok               |
|          45 | -8.73%   | 35.11%             | -16.29% |    -0.36 |       72 | 32.95%     | ok               |
|          40 | -10.81%  | 35.11%             | -14.16% |    -0.43 |       80 | 35.61%     | ok               |
|          50 | -9.90%   | 35.11%             | -14.94% |    -0.44 |       64 | 30.45%     | ok               |

## XLK Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 51.40%   | 44.82%             | -18.51% |     0.91 |       54 | 50.75%     | ok               |
|          25 | 43.41%   | 44.82%             | -15.06% |     0.87 |       44 | 45.26%     | ok               |
|          20 | 43.97%   | 44.82%             | -19.61% |     0.85 |       54 | 47.75%     | ok               |
|          30 | 34.83%   | 44.82%             | -19.09% |     0.75 |       44 | 43.93%     | ok               |
|          35 | 16.72%   | 44.82%             | -21.79% |     0.45 |       60 | 40.93%     | ok               |

## XLM-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 18.09%   | -47.39%            | -61.51% |     0.41 |       76 | 61.30%     | ok               |
|          25 | 9.63%    | -47.39%            | -55.46% |     0.32 |       83 | 52.11%     | ok               |
|          40 | 6.00%    | -47.39%            | -53.36% |     0.27 |       68 | 35.82%     | ok               |
|          45 | 3.93%    | -47.39%            | -49.94% |     0.24 |       62 | 28.35%     | ok               |
|          20 | -4.41%   | -47.39%            | -63.66% |     0.19 |       82 | 55.56%     | ok               |

## XLP Threshold Sweep

|   threshold | return   | benchmark_return   | mdd    |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:-------|---------:|---------:|:-----------|:-----------------|
|          45 | 21.45%   | 19.07%             | -5.66% |     1.05 |       48 | 33.11%     | ok               |
|          50 | 18.58%   | 19.07%             | -6.08% |     0.94 |       54 | 31.28%     | ok               |
|          40 | 19.12%   | 19.07%             | -7.32% |     0.93 |       66 | 36.44%     | ok               |
|          35 | 18.08%   | 19.07%             | -8.39% |     0.87 |       62 | 39.43%     | ok               |
|          30 | 14.66%   | 19.07%             | -8.96% |     0.71 |       63 | 41.26%     | ok               |

## XLU Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 4.81%    | 27.83%             | -14.03% |     0.28 |       56 | 30.45%     | ok               |
|          35 | 3.92%    | 27.83%             | -19.71% |     0.22 |       64 | 37.77%     | ok               |
|          45 | 3.66%    | 27.83%             | -14.97% |     0.22 |       60 | 31.61%     | ok               |
|          40 | 1.14%    | 27.83%             | -16.41% |     0.1  |       70 | 34.28%     | ok               |
|          30 | -0.58%   | 27.83%             | -20.40% |     0.02 |       69 | 41.26%     | ok               |

## XLV Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -20.62%  | 24.30%             | -22.46% |    -0.9  |       74 | 39.60%     | ok               |
|          30 | -20.98%  | 24.30%             | -22.82% |    -0.93 |       74 | 37.94%     | ok               |
|          15 | -23.30%  | 24.30%             | -24.77% |    -1    |       81 | 43.59%     | ok               |
|          20 | -23.14%  | 24.30%             | -24.61% |    -1.02 |       77 | 41.10%     | ok               |
|          35 | -24.92%  | 24.30%             | -26.64% |    -1.19 |       68 | 34.94%     | ok               |

## XLY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 0.99%    | 30.70%             | -16.52% |     0.11 |       76 | 54.58%     | ok               |
|          20 | -4.36%   | 30.70%             | -20.14% |    -0.04 |       72 | 51.25%     | ok               |
|          30 | -5.70%   | 30.70%             | -18.44% |    -0.1  |       77 | 47.59%     | ok               |
|          25 | -9.54%   | 30.70%             | -21.01% |    -0.2  |       71 | 49.42%     | ok               |
|          50 | -8.74%   | 30.70%             | -17.00% |    -0.29 |       66 | 32.28%     | ok               |

## XOM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | 3.86%    | 39.49%             | -19.90% |     0.18 |       59 | 37.44%     | ok               |
|          50 | 3.48%    | 39.49%             | -21.35% |     0.17 |       40 | 29.28%     | ok               |
|          30 | 2.83%    | 39.49%             | -20.29% |     0.15 |       59 | 36.77%     | ok               |
|          45 | -1.68%   | 39.49%             | -23.33% |     0.03 |       44 | 30.45%     | ok               |
|          40 | -3.14%   | 39.49%             | -21.45% |    -0.01 |       54 | 33.78%     | ok               |

## XRP-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 18.10%   | -56.13%            | -33.31% |     0.4  |       76 | 44.25%     | ok               |
|          40 | 4.62%    | -56.13%            | -33.93% |     0.25 |       72 | 36.97%     | ok               |
|          30 | 1.19%    | -56.13%            | -34.85% |     0.22 |       65 | 49.23%     | ok               |
|          20 | -1.38%   | -56.13%            | -37.79% |     0.2  |       72 | 55.56%     | ok               |
|          45 | -4.94%   | -56.13%            | -36.97% |     0.12 |       62 | 31.03%     | ok               |

## YFI-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -44.24%  | -66.35%            | -55.00% |    -0.59 |       74 | 40.61%     | ok               |
|          35 | -43.58%  | -66.35%            | -49.17% |    -0.64 |       64 | 35.82%     | ok               |
|          25 | -47.47%  | -66.35%            | -57.62% |    -0.64 |       73 | 45.02%     | ok               |
|          40 | -41.78%  | -66.35%            | -44.76% |    -0.65 |       60 | 27.78%     | ok               |
|          15 | -55.61%  | -66.35%            | -65.43% |    -0.77 |       81 | 53.45%     | ok               |

## ZEC-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 196.35%  | 2087.25%           | -30.64% |     1.07 |       46 | 28.35%     | ok               |
|          35 | 162.09%  | 2087.25%           | -50.84% |     0.97 |       52 | 34.10%     | ok               |
|          40 | 138.59%  | 2087.25%           | -54.22% |     0.91 |       52 | 32.38%     | ok               |
|          30 | 126.43%  | 2087.25%           | -56.50% |     0.87 |       54 | 36.97%     | ok               |
|          50 | 115.00%  | 2087.25%           | -41.34% |     0.85 |       42 | 24.52%     | ok               |
