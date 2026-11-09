# Market Tracker Backtest Report

_Generated: 2026-11-09T06:17:44+00:00_

## Data Sources

- Crypto: Kraken -> Coinbase -> CoinGecko OHLC -> CoinPaprika fallback chain.
- Stocks / ETFs / indices: Stooq -> Yahoo Finance fallback chain.
- Data rows are generated from real market APIs. Mock OHLCV rows are not generated.

## Data Freshness

- Rows: **92,782**
- Symbols: **161**
- Date range: **2024-06-17** to **2026-11-09**

## Latest Signals

| symbol     | date                |         close |   composite_score | signal   | data_source   |
|:-----------|:--------------------|--------------:|------------------:|:---------|:--------------|
| AAPL       | 2026-11-06 00:00:00 |   342.37      |          36.5833  | LONG     | Yahoo Finance |
| ABBV       | 2026-11-06 00:00:00 |   291.31      |          53.75    | LONG     | Yahoo Finance |
| AGG        | 2026-11-06 00:00:00 |    96.55      |          37.0833  | LONG     | Yahoo Finance |
| AMGN       | 2026-11-06 00:00:00 |   460.42      |          74.9167  | LONG     | Yahoo Finance |
| BLK        | 2026-11-06 00:00:00 |  1178.87      |          69.9167  | LONG     | Yahoo Finance |
| BND        | 2026-11-06 00:00:00 |    71.59      |          37.0833  | LONG     | Yahoo Finance |
| CL         | 2026-11-06 00:00:00 |    96.56      |          46.9167  | LONG     | Yahoo Finance |
| COST       | 2026-11-06 00:00:00 |  1053.56      |          57.9167  | LONG     | Yahoo Finance |
| DE         | 2026-11-06 00:00:00 |   671.65      |          52.75    | LONG     | Yahoo Finance |
| DIS        | 2026-11-06 00:00:00 |   116.75      |          74.9167  | LONG     | Yahoo Finance |
| FXI        | 2026-11-06 00:00:00 |    34.95      |          32.8333  | LONG     | Yahoo Finance |
| GDX        | 2026-11-06 00:00:00 |    87.6       |          45.6667  | LONG     | Yahoo Finance |
| HD         | 2026-11-06 00:00:00 |   343.47      |          55.9167  | LONG     | Yahoo Finance |
| IEF        | 2026-11-06 00:00:00 |    91.86      |          37.0833  | LONG     | Yahoo Finance |
| INTU       | 2026-11-06 00:00:00 |   341.5       |          50.6667  | LONG     | Yahoo Finance |
| JNJ        | 2026-11-06 00:00:00 |   276.22      |          56.0833  | LONG     | Yahoo Finance |
| KO         | 2026-11-06 00:00:00 |    95.67      |          65.4167  | LONG     | Yahoo Finance |
| LIN        | 2026-11-06 00:00:00 |   515.25      |          58.4167  | LONG     | Yahoo Finance |
| LLY        | 2026-11-06 00:00:00 |  1354         |          73.25    | LONG     | Yahoo Finance |
| MCD        | 2026-11-06 00:00:00 |   276.52      |          61.8333  | LONG     | Yahoo Finance |
| MRK        | 2026-11-06 00:00:00 |   146.73      |          70.4167  | LONG     | Yahoo Finance |
| PEP        | 2026-11-06 00:00:00 |   141.34      |          60.9167  | LONG     | Yahoo Finance |
| PEPE-USD   | 2026-11-09 00:00:00 |     5.034e-06 |          55.6667  | LONG     | Kraken API    |
| PG         | 2026-11-06 00:00:00 |   165.4       |          64.9167  | LONG     | Yahoo Finance |
| SBUX       | 2026-11-06 00:00:00 |   105.41      |          59.75    | LONG     | Yahoo Finance |
| SHY        | 2026-11-06 00:00:00 |    81.63      |          46.1667  | LONG     | Yahoo Finance |
| TLT        | 2026-11-06 00:00:00 |    81.92      |          35.0833  | LONG     | Yahoo Finance |
| UPS        | 2026-11-06 00:00:00 |   108.3       |          63       | LONG     | Yahoo Finance |
| VIXY       | 2026-11-06 00:00:00 |    21.03      |          37.5833  | LONG     | Yahoo Finance |
| VNQ        | 2026-11-06 00:00:00 |    95.73      |          67.1667  | LONG     | Yahoo Finance |
| WMT        | 2026-11-06 00:00:00 |   125.52      |          55.9167  | LONG     | Yahoo Finance |
| XLB        | 2026-11-06 00:00:00 |    51.95      |          58.4167  | LONG     | Yahoo Finance |
| XLF        | 2026-11-06 00:00:00 |    57.16      |          71.9167  | LONG     | Yahoo Finance |
| XLP        | 2026-11-06 00:00:00 |    90.08      |          57.9167  | LONG     | Yahoo Finance |
| XLU        | 2026-11-06 00:00:00 |    43.13      |          40.1667  | LONG     | Yahoo Finance |
| XLV        | 2026-11-06 00:00:00 |   184.8       |          73.25    | LONG     | Yahoo Finance |
| XLY        | 2026-11-06 00:00:00 |   117.58      |          56.4167  | LONG     | Yahoo Finance |
| AAVE-USD   | 2026-11-09 00:00:00 |   129.86      |          13.75    | NEUTRAL  | Kraken API    |
| ADBE       | 2026-11-06 00:00:00 |   239.3       |         -44.75    | NEUTRAL  | Yahoo Finance |
| AMD        | 2026-11-06 00:00:00 |   449.04      |         -14.0833  | NEUTRAL  | Yahoo Finance |
| AMZN       | 2026-11-06 00:00:00 |   259.3       |          41.6667  | NEUTRAL  | Yahoo Finance |
| ARB-USD    | 2026-11-09 00:00:00 |     0.1729    |          49.1667  | NEUTRAL  | Kraken API    |
| BAC        | 2026-11-06 00:00:00 |    49.42      |          -9.41667 | NEUTRAL  | Yahoo Finance |
| BCH-USD    | 2026-11-09 00:00:00 |   239.38      |         -59.25    | NEUTRAL  | Kraken API    |
| BONK-USD   | 2026-11-09 00:00:00 |     2.716e-06 |         -61.25    | NEUTRAL  | Kraken API    |
| C          | 2026-11-06 00:00:00 |   119.05      |         -59.5     | NEUTRAL  | Yahoo Finance |
| CMCSA      | 2026-11-06 00:00:00 |    24.39      |          22.6667  | NEUTRAL  | Yahoo Finance |
| COP        | 2026-11-06 00:00:00 |   136.27      |          -1.58333 | NEUTRAL  | Yahoo Finance |
| CVX        | 2026-11-06 00:00:00 |   212.61      |         -19.5833  | NEUTRAL  | Yahoo Finance |
| DASH-USD   | 2026-11-09 00:00:00 |    46.405     |         -32.25    | NEUTRAL  | Kraken API    |
| DBC        | 2026-11-06 00:00:00 |    31.54      |         -18.3333  | NEUTRAL  | Yahoo Finance |
| DIA        | 2026-11-06 00:00:00 |   512.22      |          -4.25    | NEUTRAL  | Yahoo Finance |
| DOT-USD    | 2026-11-09 00:00:00 |     0.8624    |         -57.9167  | NEUTRAL  | Kraken API    |
| DXY-INDEX  | 2026-11-09 00:00:00 |   102.112     |          48.6559  | NEUTRAL  | Yahoo Finance |
| EFA        | 2026-11-06 00:00:00 |   101.89      |         -38.4167  | NEUTRAL  | Yahoo Finance |
| EOG        | 2026-11-06 00:00:00 |   147.13      |           2.41667 | NEUTRAL  | Yahoo Finance |
| GDXJ       | 2026-11-06 00:00:00 |   107.74      |          -6       | NEUTRAL  | Yahoo Finance |
| GE         | 2026-11-06 00:00:00 |   323.24      |          57.5833  | NEUTRAL  | Yahoo Finance |
| GLD        | 2026-11-06 00:00:00 |   372.52      |         -47.3333  | NEUTRAL  | Yahoo Finance |
| GS         | 2026-11-06 00:00:00 |   865.82      |         -46.1667  | NEUTRAL  | Yahoo Finance |
| HON        | 2026-11-06 00:00:00 |   220.05      |          25.1667  | NEUTRAL  | Yahoo Finance |
| HYG        | 2026-11-06 00:00:00 |    77.23      |         -11.5833  | NEUTRAL  | Yahoo Finance |
| IBM        | 2026-11-06 00:00:00 |   245         |          12.5833  | NEUTRAL  | Yahoo Finance |
| INJ-USD    | 2026-11-09 00:00:00 |     8.115     |          54.0833  | NEUTRAL  | Kraken API    |
| ITA        | 2026-11-06 00:00:00 |    68.98      |         -37.1667  | NEUTRAL  | Yahoo Finance |
| IWM        | 2026-11-06 00:00:00 |   273.67      |         -26.25    | NEUTRAL  | Yahoo Finance |
| JPM        | 2026-11-06 00:00:00 |   334.49      |          18       | NEUTRAL  | Yahoo Finance |
| MPC        | 2026-11-06 00:00:00 |   372.74      |         -20.8333  | NEUTRAL  | Yahoo Finance |
| MS         | 2026-11-06 00:00:00 |   181.44      |         -32       | NEUTRAL  | Yahoo Finance |
| MSFT       | 2026-11-06 00:00:00 |   530.61      |          15.8333  | NEUTRAL  | Yahoo Finance |
| NEAR-USD   | 2026-11-09 00:00:00 |     3.5506    |         -23.25    | NEUTRAL  | Kraken API    |
| NEM        | 2026-11-06 00:00:00 |   120.91      |          38.1667  | NEUTRAL  | Yahoo Finance |
| NKE        | 2026-11-06 00:00:00 |    38.59      |          28.9167  | NEUTRAL  | Yahoo Finance |
| ORCL       | 2026-11-06 00:00:00 |   116.1       |         -55.8333  | NEUTRAL  | Yahoo Finance |
| PFE        | 2026-11-06 00:00:00 |    29.39      |          23.9167  | NEUTRAL  | Yahoo Finance |
| PM         | 2026-11-06 00:00:00 |   197.88      |           4.66667 | NEUTRAL  | Yahoo Finance |
| POL-USD    | 2026-11-09 00:00:00 |     0.08772   |         -20.6667  | NEUTRAL  | Kraken API    |
| QCOM       | 2026-11-06 00:00:00 |   165.41      |         -50       | NEUTRAL  | Yahoo Finance |
| SCHW       | 2026-11-06 00:00:00 |    91.49      |         -19.0833  | NEUTRAL  | Yahoo Finance |
| SLB        | 2026-11-06 00:00:00 |    49.92      |         -13.3333  | NEUTRAL  | Yahoo Finance |
| SPY        | 2026-11-06 00:00:00 |   735.29      |         -15.25    | NEUTRAL  | Yahoo Finance |
| TGT        | 2026-11-06 00:00:00 |   158.41      |          60.8333  | NEUTRAL  | Yahoo Finance |
| TMO        | 2026-11-06 00:00:00 |   694.76      |          31.3333  | NEUTRAL  | Yahoo Finance |
| TMUS       | 2026-11-06 00:00:00 |   162.01      |         -14.3333  | NEUTRAL  | Yahoo Finance |
| TSLA       | 2026-11-06 00:00:00 |   358.22      |         -54.0833  | NEUTRAL  | Yahoo Finance |
| TXN        | 2026-11-06 00:00:00 |   277.36      |         -10.1667  | NEUTRAL  | Yahoo Finance |
| UNH        | 2026-11-06 00:00:00 |   394.15      |          -1.58333 | NEUTRAL  | Yahoo Finance |
| UNI-USD    | 2026-11-09 00:00:00 |     6.8212    |           2.75    | NEUTRAL  | Kraken API    |
| USO        | 2026-11-06 00:00:00 |   148.41      |          -8.58333 | NEUTRAL  | Yahoo Finance |
| VEA        | 2026-11-06 00:00:00 |    67.9       |         -51.75    | NEUTRAL  | Yahoo Finance |
| VTI        | 2026-11-06 00:00:00 |   361.93      |         -17       | NEUTRAL  | Yahoo Finance |
| VZ         | 2026-11-06 00:00:00 |    45.69      |          -5.58333 | NEUTRAL  | Yahoo Finance |
| WFC        | 2026-11-06 00:00:00 |    83.94      |          44.9167  | NEUTRAL  | Yahoo Finance |
| XBI        | 2026-11-06 00:00:00 |   152.21      |          18.5     | NEUTRAL  | Yahoo Finance |
| XLI        | 2026-11-06 00:00:00 |   162.67      |         -48.5     | NEUTRAL  | Yahoo Finance |
| XOM        | 2026-11-06 00:00:00 |   165.87      |         -15.8333  | NEUTRAL  | Yahoo Finance |
| XRP-USD    | 2026-11-09 00:00:00 |     1.09563   |         -62.5833  | NEUTRAL  | Kraken API    |
| YFI-USD    | 2026-11-09 00:00:00 |  1957.5       |         -17       | NEUTRAL  | Kraken API    |
| ZEC-USD    | 2026-11-09 00:00:00 |  1219.21      |           2.58333 | NEUTRAL  | Kraken API    |
| ADA-USD    | 2026-11-09 00:00:00 |     0.174999  |         -48.3333  | SHORT    | Kraken API    |
| ALGO-USD   | 2026-11-09 00:00:00 |     0.09061   |         -45       | SHORT    | Kraken API    |
| AMAT       | 2026-11-06 00:00:00 |   332.72      |         -53.0833  | SHORT    | Yahoo Finance |
| APT-USD    | 2026-11-09 00:00:00 |     0.5738    |         -50       | SHORT    | Kraken API    |
| ARKK       | 2026-11-06 00:00:00 |    75.46      |         -33.5     | SHORT    | Yahoo Finance |
| ATOM-USD   | 2026-11-09 00:00:00 |     1.3143    |         -51.6667  | SHORT    | Kraken API    |
| AVAX-USD   | 2026-11-09 00:00:00 |     7.934     |         -32.3333  | SHORT    | Kraken API    |
| AVGO       | 2026-11-06 00:00:00 |   293.69      |         -58.0833  | SHORT    | Yahoo Finance |
| BA         | 2026-11-06 00:00:00 |   173.4       |         -55.75    | SHORT    | Yahoo Finance |
| BITO       | 2026-11-06 00:00:00 |    10.08      |         -38.8333  | SHORT    | Yahoo Finance |
| BTC-USD    | 2026-11-09 00:00:00 | 74446.7       |         -40.5833  | SHORT    | Kraken API    |
| CAT        | 2026-11-06 00:00:00 |   558.63      |         -63.4167  | SHORT    | Yahoo Finance |
| COMP-USD   | 2026-11-09 00:00:00 |    19.87      |         -44.3333  | SHORT    | Kraken API    |
| CRM        | 2026-11-06 00:00:00 |   213.65      |         -44.3333  | SHORT    | Yahoo Finance |
| CRV-USD    | 2026-11-09 00:00:00 |     0.25741   |         -49.6667  | SHORT    | Kraken API    |
| CSCO       | 2026-11-06 00:00:00 |    93.85      |         -47.5833  | SHORT    | Yahoo Finance |
| DOGE-USD   | 2026-11-09 00:00:00 |     0.0690835 |         -48       | SHORT    | Kraken API    |
| EEM        | 2026-11-06 00:00:00 |    59.33      |         -50.8333  | SHORT    | Yahoo Finance |
| ETC-USD    | 2026-11-09 00:00:00 |     6.696     |         -42.3333  | SHORT    | Kraken API    |
| ETH-USD    | 2026-11-09 00:00:00 |  2128.87      |         -44.5     | SHORT    | Kraken API    |
| EWJ        | 2026-11-06 00:00:00 |    88.26      |         -55.4167  | SHORT    | Yahoo Finance |
| FCX        | 2026-11-06 00:00:00 |    59.42      |         -59.4167  | SHORT    | Yahoo Finance |
| FET-USD    | 2026-11-09 00:00:00 |     0.1409    |         -47       | SHORT    | Kraken API    |
| FIL-USD    | 2026-11-09 00:00:00 |     0.756     |         -48       | SHORT    | Kraken API    |
| GOOGL      | 2026-11-06 00:00:00 |   284.78      |         -61.4167  | SHORT    | Yahoo Finance |
| GRT-USD    | 2026-11-09 00:00:00 |     0.01832   |         -49.6667  | SHORT    | Kraken API    |
| HBAR-USD   | 2026-11-09 00:00:00 |     0.06619   |         -35.6667  | SHORT    | Kraken API    |
| IBIT       | 2026-11-06 00:00:00 |    42.88      |         -38.8333  | SHORT    | Yahoo Finance |
| ICP-USD    | 2026-11-09 00:00:00 |     2.345     |         -30.3333  | SHORT    | Kraken API    |
| IEMG       | 2026-11-06 00:00:00 |    72.2       |         -50.8333  | SHORT    | Yahoo Finance |
| INTC       | 2026-11-06 00:00:00 |    56.28      |         -61.5833  | SHORT    | Yahoo Finance |
| LDO-USD    | 2026-11-09 00:00:00 |     0.317     |         -46.3333  | SHORT    | Kraken API    |
| LINK-USD   | 2026-11-09 00:00:00 |    10.4411    |         -39.25    | SHORT    | Kraken API    |
| LRCX       | 2026-11-06 00:00:00 |   200.44      |         -63.75    | SHORT    | Yahoo Finance |
| LTC-USD    | 2026-11-09 00:00:00 |    50.63      |         -41       | SHORT    | Kraken API    |
| META       | 2026-11-06 00:00:00 |   610.15      |         -45.9167  | SHORT    | Yahoo Finance |
| MU         | 2026-11-06 00:00:00 |   690         |         -41.5     | SHORT    | Yahoo Finance |
| NFLX       | 2026-11-06 00:00:00 |    63.41      |         -43.25    | SHORT    | Yahoo Finance |
| NOW        | 2026-11-06 00:00:00 |   101.97      |         -51.5833  | SHORT    | Yahoo Finance |
| NVDA       | 2026-11-06 00:00:00 |   186.64      |         -45.6667  | SHORT    | Yahoo Finance |
| OP-USD     | 2026-11-09 00:00:00 |     0.0993    |         -36.3333  | SHORT    | Kraken API    |
| OXY        | 2026-11-06 00:00:00 |    56.38      |         -34.8333  | SHORT    | Yahoo Finance |
| QQQ        | 2026-11-06 00:00:00 |   656.1       |         -38.8333  | SHORT    | Yahoo Finance |
| RENDER-USD | 2026-11-09 00:00:00 |     1.562     |         -41.3333  | SHORT    | Kraken API    |
| RTX        | 2026-11-06 00:00:00 |   189.53      |         -37.5833  | SHORT    | Yahoo Finance |
| SHIB-USD   | 2026-11-09 00:00:00 |     4.385e-06 |         -42.3333  | SHORT    | Kraken API    |
| SKY-USD    | 2026-11-09 00:00:00 |     0.06219   |         -43       | SHORT    | Kraken API    |
| SLV        | 2026-11-06 00:00:00 |    46.87      |         -56.0833  | SHORT    | Yahoo Finance |
| SMH        | 2026-11-06 00:00:00 |   463.96      |         -54.75    | SHORT    | Yahoo Finance |
| SNX-USD    | 2026-11-09 00:00:00 |     0.1569    |         -48.3333  | SHORT    | Kraken API    |
| SOL-USD    | 2026-11-09 00:00:00 |    86.61      |         -47.9167  | SHORT    | Kraken API    |
| SOXX       | 2026-11-06 00:00:00 |   136.53      |         -56.5     | SHORT    | Yahoo Finance |
| SUSHI-USD  | 2026-11-09 00:00:00 |     0.1733    |         -51.6667  | SHORT    | Kraken API    |
| T          | 2026-11-06 00:00:00 |    21.63      |         -38.25    | SHORT    | Yahoo Finance |
| TIA-USD    | 2026-11-09 00:00:00 |     0.422     |         -53.6667  | SHORT    | Kraken API    |
| TRX-USD    | 2026-11-09 00:00:00 |     0.317234  |         -50.8333  | SHORT    | Kraken API    |
| VWO        | 2026-11-06 00:00:00 |    55.29      |         -53.8333  | SHORT    | Yahoo Finance |
| WIF-USD    | 2026-11-09 00:00:00 |     0.1542    |         -52.3333  | SHORT    | Kraken API    |
| XLC        | 2026-11-06 00:00:00 |   104.79      |         -42.75    | SHORT    | Yahoo Finance |
| XLE        | 2026-11-06 00:00:00 |    61.62      |         -34.8333  | SHORT    | Yahoo Finance |
| XLK        | 2026-11-06 00:00:00 |   164.74      |         -40.5833  | SHORT    | Yahoo Finance |
| XLM-USD    | 2026-11-09 00:00:00 |     0.14572   |         -43       | SHORT    | Kraken API    |

## Edge Summary

- Symbols with trades: **161** of 161
- Beat buy-and-hold: **36.02%** of traded symbols
- Positive return: **31.68%** of traded symbols
- Median strategy return: **-7.95%** (benchmark **16.93%**)
- Median excess vs benchmark: **-23.86%**
- Median Sharpe: **-0.07**
- Median exposure: **44.43%**

> Edge is real only if both _beat buy-and-hold_ and _median excess_ are convincingly positive across many symbols. Treat a single high-return symbol as noise.

## Portfolio Backtest

Actual capital-allocation books (not per-symbol averages). Benchmarks: `equal_weight_buyhold` (whole tracked universe), `spy_buyhold` (100% SPY), and `sixty_forty` (60% SPY / 40% AGG). `high_conf_voltarget` inverse-vol-weights the HIGH-confidence book; `conviction_long_short` is market-neutral. Judge on **Sharpe** and **max_drawdown** out-of-sample, not raw return: a fully-invested long book wins on return in a bull market but carries all the risk.

| strategy              | scope         | ann_return   | ann_vol   |   sharpe | max_drawdown   | total_return   |   avg_gross_exposure |
|:----------------------|:--------------|:-------------|:----------|---------:|:---------------|:---------------|---------------------:|
| equal_weight_buyhold  | full          | 7.19%        | 28.51%    |     0.25 | -39.53%        | 10.00%         |                 1    |
| equal_weight_buyhold  | out_of_sample | 10.98%       | 26.62%    |     0.41 | -18.44%        | 8.28%          |                 1    |
| all_signals_ew        | full          | -12.39%      | 24.21%    |    -0.51 | -54.46%        | -37.33%        |                 1    |
| all_signals_ew        | out_of_sample | 2.33%        | 21.63%    |     0.11 | -23.38%        | 0.00%          |                 1    |
| high_conf_ew          | full          | -7.58%       | 29.89%    |    -0.25 | -46.49%        | -30.65%        |                 0.89 |
| high_conf_ew          | out_of_sample | -4.30%       | 27.11%    |    -0.16 | -22.80%        | -8.22%         |                 0.89 |
| high_conf_voltarget   | full          | -8.05%       | 26.57%    |    -0.3  | -41.00%        | -29.65%        |                 0.89 |
| high_conf_voltarget   | out_of_sample | -7.57%       | 22.77%    |    -0.33 | -17.69%        | -10.37%        |                 0.89 |
| conviction_long_short | full          | -15.78%      | 21.99%    |    -0.72 | -50.16%        | -42.60%        |                 0.96 |
| conviction_long_short | out_of_sample | -14.32%      | 17.27%    |    -0.83 | -27.62%        | -15.54%        |                 0.96 |
| spy_buyhold           | full          | 2.85%        | 13.93%    |     0.2  | -19.00%        | 5.93%          |                 0.78 |
| spy_buyhold           | out_of_sample | -2.51%       | 10.82%    |    -0.23 | -11.45%        | -3.25%         |                 0.78 |
| sixty_forty           | full          | 1.36%        | 8.73%     |     0.16 | -11.66%        | 3.04%          |                 0.78 |
| sixty_forty           | out_of_sample | -3.39%       | 7.14%     |    -0.47 | -8.19%         | -3.81%         |                 0.78 |

## Walk-Forward Robustness

Each book measured across contiguous time folds (each a different regime). A book has durable edge only if `mean_sharpe` is positive, `min_sharpe` isn't deeply negative, and `pct_positive_folds` is high — a single great fold doesn't count. `fold_sharpes` lists each fold oldest-to-newest.

| strategy              |   n_folds |   mean_sharpe |   median_sharpe |   min_sharpe | pct_positive_folds   | mean_return   | fold_sharpes                 |
|:----------------------|----------:|--------------:|----------------:|-------------:|:---------------------|:--------------|:-----------------------------|
| equal_weight_buyhold  |         5 |          0.48 |            0.59 |        -0.85 | 60.00%               | 3.20%         | 1.51;1.51;-0.37;-0.85;0.59   |
| all_signals_ew        |         5 |         -0.59 |           -0.43 |        -1.85 | 20.00%               | -7.51%        | -1.51;-0.43;-1.85;1.24;-0.38 |
| high_conf_ew          |         5 |         -0.17 |           -0.49 |        -1.67 | 40.00%               | -5.26%        | 0.44;-1.67;-0.49;1.59;-0.73  |
| high_conf_voltarget   |         5 |         -0.26 |           -0.34 |        -1.77 | 40.00%               | -5.90%        | 0.61;-1.77;-0.34;0.98;-0.77  |
| conviction_long_short |         5 |         -0.73 |           -0.65 |        -2.1  | 40.00%               | -9.89%        | -2.10;0.16;-1.22;0.18;-0.65  |
| spy_buyhold           |         5 |          0.17 |            0.08 |        -0.88 | 80.00%               | 1.30%         | 1.34;0.08;0.02;0.30;-0.88    |
| sixty_forty           |         5 |          0.11 |            0.07 |        -0.93 | 80.00%               | 0.66%         | 1.31;0.09;0.07;0.03;-0.93    |

## Strategy Comparison

Each decision rule backtested over the same data. `out_of_sample` is the most recent ~35% of each symbol's history (unseen tail). A rule has real edge only if `median_excess` and `beat_benchmark_pct` stay positive out-of-sample, not just full-sample.

| strategy        | scope         |   symbols | beat_benchmark_pct   | positive_pct   | median_return   | median_benchmark   | median_excess   |   median_sharpe |   total_trades |
|:----------------|:--------------|----------:|:---------------------|:---------------|:----------------|:-------------------|:----------------|----------------:|---------------:|
| trend           | full          |       161 | 36.02%               | 31.68%         | -7.95%          | 16.93%             | -23.86%         |           -0.07 |          11327 |
| trend           | out_of_sample |       161 | 46.58%               | 49.69%         | -0.02%          | -0.76%             | -2.08%          |            0.12 |           3899 |
| mean_reversion  | full          |       159 | 38.99%               | 49.06%         | -0.05%          | 16.93%             | -18.23%         |           -0.01 |           1282 |
| mean_reversion  | out_of_sample |       133 | 51.13%               | 57.89%         | 0.31%           | -1.48%             | 1.19%           |            0.5  |            462 |
| regime_adaptive | full          |       161 | 36.65%               | 32.92%         | -8.26%          | 16.93%             | -21.97%         |           -0.07 |          11599 |
| regime_adaptive | out_of_sample |       161 | 47.20%               | 50.93%         | 0.44%           | -0.76%             | -2.00%          |            0.15 |           4004 |

## Signal Calibration

Realized forward return in the signal's direction, grouped by confidence. HIGH should outrank LOW for the confidence score to be meaningful.

| confidence_level   |   horizon |     n | mean_return   | median_return   | win_rate   |
|:-------------------|----------:|------:|:--------------|:----------------|:-----------|
| HIGH               |         5 |  7856 | 0.21%         | 0.08%           | 51.30%     |
| MEDIUM             |         5 | 29106 | 0.08%         | 0.06%           | 50.63%     |
| LOW                |         5 |  3622 | -0.21%        | -0.26%          | 47.49%     |
| ALL                |         5 | 40584 | 0.08%         | 0.04%           | 50.48%     |
| HIGH               |        10 |  7765 | 0.45%         | 0.09%           | 51.02%     |
| MEDIUM             |        10 | 28798 | 0.19%         | 0.07%           | 50.52%     |
| LOW                |        10 |  3581 | -0.46%        | -0.26%          | 48.14%     |
| ALL                |        10 | 40144 | 0.18%         | 0.05%           | 50.40%     |
| HIGH               |        20 |  7659 | 0.84%         | 0.18%           | 51.44%     |
| MEDIUM             |        20 | 28315 | 0.70%         | 0.46%           | 52.53%     |
| LOW                |        20 |  3481 | -0.41%        | -0.50%          | 47.63%     |
| ALL                |        20 | 39455 | 0.63%         | 0.32%           | 51.89%     |

## Backtest Summary

### Data Quality / Signal Availability

- **ok**: 161 symbols

| symbol     |   trades | return   | benchmark_return   | mdd     |   sharpe | exposure   | skipped_reason   |
|:-----------|---------:|:---------|:-------------------|:--------|---------:|:-----------|:-----------------|
| AAPL       |       68 | -13.32%  | 58.01%             | -23.09% |    -0.18 | 48.42%     | ok               |
| AAVE-USD   |       65 | -43.38%  | -48.37%            | -64.31% |    -0.34 | 38.70%     | ok               |
| ABBV       |       68 | -17.54%  | 71.68%             | -30.52% |    -0.33 | 50.25%     | ok               |
| ADA-USD    |       76 | -18.92%  | -73.31%            | -52.70% |    -0    | 48.85%     | ok               |
| ADBE       |       74 | 2.80%    | -53.87%            | -31.20% |     0.18 | 54.08%     | ok               |
| AGG        |       63 | -6.68%   | -1.05%             | -11.01% |    -1.06 | 33.28%     | ok               |
| ALGO-USD   |       82 | -30.48%  | -51.61%            | -43.23% |    -0.18 | 42.15%     | ok               |
| AMAT       |       73 | -32.84%  | 37.00%             | -57.56% |    -0.23 | 51.75%     | ok               |
| AMD        |       52 | 27.92%   | 183.48%            | -38.64% |     0.46 | 36.11%     | ok               |
| AMGN       |       63 | -4.79%   | 51.81%             | -34.19% |    -0.01 | 52.41%     | ok               |
| AMZN       |       84 | -58.73%  | 40.88%             | -59.16% |    -1.73 | 41.60%     | ok               |
| APT-USD    |       74 | -32.42%  | -87.56%            | -56.73% |    -0.13 | 39.85%     | ok               |
| ARB-USD    |       73 | 14.33%   | -48.00%            | -43.51% |     0.39 | 42.72%     | ok               |
| ARKK       |       85 | -25.96%  | 70.99%             | -31.47% |    -0.36 | 43.43%     | ok               |
| ATOM-USD   |       84 | -55.52%  | -68.53%            | -64.83% |    -0.79 | 47.32%     | ok               |
| AVAX-USD   |       68 | -28.61%  | -59.66%            | -46.93% |    -0.18 | 41.95%     | ok               |
| AVGO       |       66 | 0.17%    | 60.59%             | -40.82% |     0.17 | 40.27%     | ok               |
| BA         |       65 | 13.16%   | -2.80%             | -24.47% |     0.33 | 51.75%     | ok               |
| BAC        |       78 | -6.49%   | 25.08%             | -22.37% |    -0.1  | 48.92%     | ok               |
| BCH-USD    |       82 | -14.22%  | -39.54%            | -54.04% |     0.04 | 47.89%     | ok               |
| BITO       |       85 | -27.99%  | -59.94%            | -43.13% |    -0.23 | 40.93%     | ok               |
| BLK        |       79 | -7.95%   | 50.93%             | -26.90% |    -0.14 | 47.25%     | ok               |
| BND        |       67 | -6.73%   | -1.11%             | -10.91% |    -1.04 | 34.94%     | ok               |
| BONK-USD   |       78 | 36.32%   | -81.68%            | -56.46% |     0.54 | 45.02%     | ok               |
| BTC-USD    |       79 | -8.25%   | -28.67%            | -23.58% |    -0.02 | 51.53%     | ok               |
| C          |       81 | -35.20%  | 98.22%             | -39.84% |    -0.76 | 47.42%     | ok               |
| CAT        |       70 | 36.90%   | 73.27%             | -21.87% |     0.62 | 50.58%     | ok               |
| CL         |       60 | 4.74%    | 0.64%              | -14.32% |     0.21 | 39.77%     | ok               |
| CMCSA      |       84 | -37.44%  | -30.25%            | -46.48% |    -0.91 | 43.43%     | ok               |
| COMP-USD   |       99 | -45.56%  | -55.32%            | -61.00% |    -0.33 | 49.04%     | ok               |
| COP        |       64 | -15.84%  | 24.40%             | -39.71% |    -0.2  | 43.59%     | ok               |
| COST       |       60 | -2.02%   | 21.39%             | -31.32% |     0    | 40.93%     | ok               |
| CRM        |       67 | -31.16%  | -7.30%             | -41.56% |    -0.44 | 46.09%     | ok               |
| CRV-USD    |       64 | 21.28%   | -58.88%            | -39.89% |     0.43 | 36.97%     | ok               |
| CSCO       |       65 | 11.24%   | 105.41%            | -23.09% |     0.31 | 50.75%     | ok               |
| CVX        |       69 | -13.20%  | 38.79%             | -27.78% |    -0.27 | 42.93%     | ok               |
| DASH-USD   |       57 | -15.94%  | 117.96%            | -64.43% |     0.28 | 30.65%     | ok               |
| DBC        |       68 | -11.81%  | 36.24%             | -24.10% |    -0.34 | 36.11%     | ok               |
| DE         |       72 | -4.58%   | 77.11%             | -21.34% |    -0    | 43.93%     | ok               |
| DIA        |       70 | -9.43%   | 31.82%             | -15.92% |    -0.48 | 44.26%     | ok               |
| DIS        |       62 | -1.12%   | 15.00%             | -27.81% |     0.07 | 45.76%     | ok               |
| DOGE-USD   |       68 | -19.71%  | -61.36%            | -60.39% |    -0.02 | 47.70%     | ok               |
| DOT-USD    |       80 | -50.30%  | -77.87%            | -63.40% |    -0.42 | 45.40%     | ok               |
| DXY-INDEX  |       40 | -2.35%   | -6.47%             | -6.06%  |    -0.38 | 30.95%     | ok               |
| EEM        |       66 | -6.34%   | 39.60%             | -24.14% |    -0.13 | 41.10%     | ok               |
| EFA        |       64 | -9.07%   | 30.39%             | -12.63% |    -0.35 | 38.94%     | ok               |
| EOG        |       78 | -29.89%  | 23.56%             | -47.87% |    -0.63 | 44.76%     | ok               |
| ETC-USD    |       54 | -4.96%   | -59.94%            | -45.54% |     0.1  | 34.67%     | ok               |
| ETH-USD    |       59 | 108.52%  | -14.09%            | -30.11% |     1.11 | 46.55%     | ok               |
| EWJ        |       66 | -22.18%  | 32.50%             | -29.40% |    -0.76 | 37.44%     | ok               |
| FCX        |       69 | -25.17%  | 25.73%             | -46.84% |    -0.23 | 45.09%     | ok               |
| FET-USD    |       79 | -32.13%  | -80.43%            | -66.52% |    -0.06 | 44.83%     | ok               |
| FIL-USD    |       71 | -37.35%  | -68.73%            | -61.02% |    -0.27 | 38.89%     | ok               |
| FXI        |       46 | -3.03%   | 31.89%             | -23.91% |     0.01 | 30.12%     | ok               |
| GDX        |       66 | -3.66%   | 163.86%            | -33.40% |     0.08 | 44.93%     | ok               |
| GDXJ       |       68 | -25.61%  | 159.68%            | -35.04% |    -0.24 | 44.26%     | ok               |
| GE         |       78 | -13.14%  | 98.03%             | -27.82% |    -0.14 | 48.42%     | ok               |
| GLD        |       52 | 11.67%   | 73.58%             | -14.15% |     0.35 | 46.09%     | ok               |
| GOOGL      |       57 | 72.70%   | 60.67%             | -18.46% |     1.12 | 48.42%     | ok               |
| GRT-USD    |       75 | 51.93%   | -79.53%            | -43.87% |     0.65 | 47.89%     | ok               |
| GS         |       68 | -2.77%   | 92.33%             | -21.94% |     0.04 | 47.42%     | ok               |
| HBAR-USD   |       40 | -28.48%  | -35.82%            | -56.47% |    -0.4  | 43.25%     | ok               |
| HD         |       73 | 4.12%    | -1.73%             | -17.15% |     0.18 | 44.59%     | ok               |
| HON        |       89 | -28.67%  | 5.03%              | -33.87% |    -0.74 | 53.58%     | ok               |
| HYG        |       87 | -6.94%   | 0.16%              | -10.69% |    -0.77 | 39.60%     | ok               |
| IBIT       |       46 | 28.87%   | 12.81%             | -18.95% |     0.56 | 35.10%     | ok               |
| IBM        |       69 | -19.93%  | 44.54%             | -48.94% |    -0.19 | 50.75%     | ok               |
| ICP-USD    |       72 | 4.81%    | -52.63%            | -40.43% |     0.31 | 39.66%     | ok               |
| IEF        |       80 | -9.97%   | -2.44%             | -13.34% |    -1.35 | 34.11%     | ok               |
| IEMG       |       62 | -3.04%   | 35.10%             | -24.73% |    -0.03 | 40.93%     | ok               |
| INJ-USD    |       57 | -18.95%  | -31.81%            | -64.24% |     0.06 | 39.08%     | ok               |
| INTC       |       70 | 64.91%   | 81.67%             | -60.60% |     0.66 | 48.92%     | ok               |
| INTU       |       71 | 6.71%    | -43.32%            | -37.44% |     0.24 | 47.92%     | ok               |
| ITA        |       72 | -1.32%   | 55.10%             | -23.75% |     0.04 | 47.42%     | ok               |
| IWM        |       58 | 10.62%   | 36.56%             | -8.62%  |     0.43 | 34.78%     | ok               |
| JNJ        |       60 | 12.36%   | 89.26%             | -17.51% |     0.47 | 46.59%     | ok               |
| JPM        |       75 | -25.99%  | 71.55%             | -32.74% |    -0.75 | 44.43%     | ok               |
| KO         |       52 | 28.12%   | 52.78%             | -8.64%  |     0.94 | 38.77%     | ok               |
| LDO-USD    |       66 | 65.61%   | -58.94%            | -53.44% |     0.71 | 48.08%     | ok               |
| LIN        |       70 | -5.04%   | 16.93%             | -20.61% |    -0.11 | 41.10%     | ok               |
| LINK-USD   |       68 | 29.72%   | -23.07%            | -35.01% |     0.5  | 43.10%     | ok               |
| LLY        |       80 | -32.96%  | 52.99%             | -52.47% |    -0.5  | 49.58%     | ok               |
| LRCX       |       82 | -10.29%  | 87.03%             | -58.92% |     0.08 | 45.26%     | ok               |
| LTC-USD    |       69 | 10.16%   | -42.03%            | -30.78% |     0.32 | 50.77%     | ok               |
| MCD        |       77 | 8.94%    | 9.08%              | -22.20% |     0.36 | 40.43%     | ok               |
| META       |       72 | -29.66%  | 20.43%             | -44.90% |    -0.43 | 50.25%     | ok               |
| MPC        |       70 | 10.68%   | 117.05%            | -33.74% |     0.29 | 53.24%     | ok               |
| MRK        |       67 | -23.59%  | 15.08%             | -35.95% |    -0.45 | 42.60%     | ok               |
| MS         |       77 | -7.18%   | 86.97%             | -27.79% |    -0.09 | 48.42%     | ok               |
| MSFT       |       83 | -28.52%  | 18.34%             | -39.07% |    -0.63 | 50.92%     | ok               |
| MU         |       53 | 96.55%   | 366.75%            | -68.76% |     0.83 | 49.92%     | ok               |
| NEAR-USD   |       63 | 169.55%  | 53.37%             | -47.35% |     1.11 | 42.91%     | ok               |
| NEM        |       70 | -25.86%  | 195.55%            | -39.56% |    -0.25 | 49.75%     | ok               |
| NFLX       |       84 | -7.29%   | -6.17%             | -27.17% |    -0.05 | 50.92%     | ok               |
| NKE        |       85 | -30.90%  | -59.38%            | -55.35% |    -0.36 | 48.09%     | ok               |
| NOW        |       79 | -8.26%   | -29.72%            | -42.66% |     0.12 | 51.58%     | ok               |
| NVDA       |       82 | -41.13%  | 58.06%             | -51.51% |    -0.55 | 55.79%     | ok               |
| OP-USD     |       72 | -34.58%  | -83.20%            | -58.87% |    -0.2  | 34.87%     | ok               |
| ORCL       |       58 | 72.68%   | -17.84%            | -30.61% |     0.74 | 50.42%     | ok               |
| OXY        |       67 | 2.72%    | -6.35%             | -28.48% |     0.17 | 43.26%     | ok               |
| PEP        |       74 | 1.81%    | -14.93%            | -21.35% |     0.12 | 45.09%     | ok               |
| PEPE-USD   |       74 | -35.81%  | -54.48%            | -57.70% |    -0.11 | 46.93%     | ok               |
| PFE        |       77 | -32.40%  | 8.93%              | -41.77% |    -0.98 | 37.44%     | ok               |
| PG         |       62 | -19.49%  | -1.25%             | -24.55% |    -0.69 | 36.11%     | ok               |
| PM         |       81 | -7.98%   | 93.90%             | -37.61% |    -0.09 | 48.75%     | ok               |
| POL-USD    |       83 | 13.64%   | -59.11%            | -44.63% |     0.36 | 50.57%     | ok               |
| QCOM       |       79 | -41.99%  | -25.56%            | -56.59% |    -0.48 | 40.77%     | ok               |
| QQQ        |       70 | -2.41%   | 35.26%             | -14.20% |     0.01 | 43.59%     | ok               |
| RENDER-USD |       90 | -43.38%  | -58.42%            | -54.16% |    -0.25 | 48.66%     | ok               |
| RTX        |       68 | 22.85%   | 81.42%             | -16.99% |     0.55 | 51.75%     | ok               |
| SBUX       |       66 | -10.12%  | 29.61%             | -29.22% |    -0.12 | 39.93%     | ok               |
| SCHW       |       84 | -16.47%  | 25.66%             | -31.92% |    -0.34 | 48.09%     | ok               |
| SHIB-USD   |       81 | -34.31%  | -64.72%            | -52.52% |    -0.33 | 52.49%     | ok               |
| SHY        |       54 | -1.88%   | 0.12%              | -3.18%  |    -0.62 | 38.44%     | ok               |
| SKY-USD    |       87 | -57.85%  | -12.41%            | -63.60% |    -0.89 | 44.44%     | ok               |
| SLB        |       78 | -48.25%  | 14.42%             | -58.27% |    -1.03 | 48.25%     | ok               |
| SLV        |       66 | 29.20%   | 74.11%             | -37.05% |     0.5  | 41.10%     | ok               |
| SMH        |       50 | 51.22%   | 70.27%             | -34.29% |     0.79 | 42.10%     | ok               |
| SNX-USD    |       60 | 12.33%   | -75.21%            | -50.74% |     0.35 | 36.59%     | ok               |
| SOL-USD    |       75 | -11.67%  | -41.44%            | -44.96% |     0.1  | 58.24%     | ok               |
| SOXX       |       56 | 64.26%   | 59.98%             | -39.81% |     0.88 | 40.93%     | ok               |
| SPY        |       63 | -5.21%   | 34.40%             | -15.53% |    -0.12 | 47.75%     | ok               |
| SUSHI-USD  |       91 | -59.63%  | -72.55%            | -76.86% |    -0.68 | 42.91%     | ok               |
| T          |       68 | 54.46%   | 22.41%             | -17.01% |     0.97 | 57.24%     | ok               |
| TGT        |       58 | -8.89%   | 9.27%              | -32.83% |    -0.11 | 37.27%     | ok               |
| TIA-USD    |       91 | -44.86%  | -78.43%            | -75.93% |    -0.19 | 43.10%     | ok               |
| TLT        |       66 | -19.75%  | -12.60%            | -21.85% |    -1.5  | 34.11%     | ok               |
| TMO        |       63 | 30.62%   | 22.32%             | -18.85% |     0.63 | 54.91%     | ok               |
| TMUS       |       74 | -7.14%   | -8.67%             | -33.05% |    -0.06 | 47.25%     | ok               |
| TRX-USD    |       62 | 2.61%    | 14.06%             | -22.90% |     0.16 | 47.70%     | ok               |
| TSLA       |       74 | -30.19%  | 91.11%             | -58.36% |    -0.15 | 42.76%     | ok               |
| TXN        |       81 | -31.25%  | 42.31%             | -46.56% |    -0.37 | 48.59%     | ok               |
| UNH        |       73 | 38.75%   | -19.43%            | -26.31% |     0.61 | 49.08%     | ok               |
| UNI-USD    |       84 | -29.15%  | 13.82%             | -59.93% |    -0.02 | 49.43%     | ok               |
| UPS        |       74 | -36.84%  | -20.28%            | -41.49% |    -0.72 | 41.76%     | ok               |
| USO        |       67 | -13.41%  | 90.78%             | -43.78% |    -0.06 | 34.28%     | ok               |
| VEA        |       62 | -5.22%   | 36.67%             | -17.27% |    -0.17 | 41.93%     | ok               |
| VIXY       |       96 | -81.63%  | -52.55%            | -89.87% |    -1.07 | 31.45%     | ok               |
| VNQ        |       71 | -11.10%  | 14.41%             | -24.92% |    -0.41 | 39.93%     | ok               |
| VTI        |       67 | -11.87%  | 34.69%             | -17.64% |    -0.38 | 47.75%     | ok               |
| VWO        |       78 | -12.94%  | 25.66%             | -25.20% |    -0.43 | 41.10%     | ok               |
| VZ         |       87 | -29.15%  | 15.79%             | -31.67% |    -0.9  | 43.43%     | ok               |
| WFC        |       86 | -21.60%  | 44.13%             | -29.91% |    -0.39 | 46.59%     | ok               |
| WIF-USD    |       64 | -1.06%   | -81.07%            | -48.32% |     0.26 | 41.95%     | ok               |
| WMT        |       71 | 6.62%    | 86.18%             | -25.96% |     0.25 | 48.42%     | ok               |
| XBI        |       60 | 0.63%    | 68.02%             | -17.66% |     0.1  | 37.77%     | ok               |
| XLB        |       64 | -10.47%  | 15.91%             | -24.18% |    -0.33 | 33.78%     | ok               |
| XLC        |       61 | 8.81%    | 23.97%             | -12.33% |     0.35 | 49.58%     | ok               |
| XLE        |       69 | 1.53%    | 39.62%             | -28.77% |     0.12 | 47.25%     | ok               |
| XLF        |       78 | -3.92%   | 39.38%             | -23.61% |    -0.07 | 48.42%     | ok               |
| XLI        |       84 | -10.61%  | 32.80%             | -18.31% |    -0.38 | 42.93%     | ok               |
| XLK        |       42 | 36.92%   | 42.56%             | -14.75% |     0.79 | 43.93%     | ok               |
| XLM-USD    |       73 | 6.21%    | -44.63%            | -54.58% |     0.28 | 48.66%     | ok               |
| XLP        |       63 | 13.28%   | 15.96%             | -8.96%  |     0.66 | 39.93%     | ok               |
| XLU        |       69 | -1.54%   | 24.71%             | -20.40% |    -0.02 | 39.93%     | ok               |
| XLV        |       74 | -19.40%  | 26.81%             | -22.82% |    -0.87 | 36.61%     | ok               |
| XLY        |       77 | -4.80%   | 29.59%             | -18.44% |    -0.07 | 47.75%     | ok               |
| XOM        |       55 | 2.46%    | 53.07%             | -20.29% |     0.14 | 36.27%     | ok               |
| XRP-USD    |       70 | -1.22%   | -49.33%            | -33.91% |     0.17 | 35.06%     | ok               |
| YFI-USD    |       74 | -52.80%  | -61.57%            | -58.28% |    -0.83 | 40.04%     | ok               |
| ZEC-USD    |       54 | 126.43%  | 2429.48%           | -56.50% |     0.87 | 36.97%     | ok               |

## AAPL Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -7.90%   | 58.01%             | -22.53% |    -0.05 |       77 | 53.24%     | ok               |
|          15 | -11.97%  | 58.01%             | -24.50% |    -0.12 |       86 | 60.73%     | ok               |
|          30 | -13.32%  | 58.01%             | -23.09% |    -0.18 |       68 | 48.42%     | ok               |
|          35 | -14.56%  | 58.01%             | -24.45% |    -0.22 |       68 | 47.09%     | ok               |
|          40 | -14.24%  | 58.01%             | -28.08% |    -0.22 |       64 | 42.93%     | ok               |

## AAVE-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 4.68%    | -48.37%            | -43.61% |     0.27 |       43 | 33.52%     | ok               |
|          35 | -9.10%   | -48.37%            | -48.79% |     0.12 |       53 | 36.78%     | ok               |
|          45 | -10.37%  | -48.37%            | -49.19% |     0.07 |       48 | 28.54%     | ok               |
|          50 | -11.28%  | -48.37%            | -45.07% |     0.04 |       44 | 21.26%     | ok               |
|          15 | -41.76%  | -48.37%            | -60.36% |    -0.2  |       76 | 52.68%     | ok               |

## ABBV Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -9.60%   | 71.68%             | -28.42% |    -0.16 |       54 | 38.27%     | ok               |
|          20 | -14.31%  | 71.68%             | -28.73% |    -0.23 |       64 | 53.58%     | ok               |
|          25 | -14.41%  | 71.68%             | -30.04% |    -0.24 |       67 | 52.08%     | ok               |
|          30 | -17.54%  | 71.68%             | -30.52% |    -0.33 |       68 | 50.25%     | ok               |
|          40 | -17.59%  | 71.68%             | -27.36% |    -0.37 |       70 | 43.26%     | ok               |

## ADA-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 10.96%   | -73.31%            | -32.15% |     0.32 |       48 | 25.86%     | ok               |
|          15 | 2.20%    | -73.31%            | -47.27% |     0.29 |       69 | 63.41%     | ok               |
|          35 | 7.03%    | -73.31%            | -44.07% |     0.29 |       64 | 43.30%     | ok               |
|          45 | 6.79%    | -73.31%            | -37.32% |     0.28 |       54 | 32.38%     | ok               |
|          40 | 3.58%    | -73.31%            | -41.47% |     0.25 |       60 | 38.89%     | ok               |

## ADBE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | 15.11%   | -53.87%            | -29.07% |     0.35 |       61 | 58.40%     | ok               |
|          30 | 2.80%    | -53.87%            | -31.20% |     0.18 |       74 | 54.08%     | ok               |
|          20 | 1.79%    | -53.87%            | -31.52% |     0.17 |       69 | 62.06%     | ok               |
|          35 | -0.64%   | -53.87%            | -32.89% |     0.12 |       77 | 45.59%     | ok               |
|          15 | -5.09%   | -53.87%            | -34.98% |     0.08 |       69 | 64.73%     | ok               |

## AGG Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -5.44%   | -1.05%             | -9.59%  |    -0.99 |       52 | 23.96%     | ok               |
|          50 | -4.84%   | -1.05%             | -8.07%  |    -1.04 |       50 | 18.97%     | ok               |
|          30 | -6.68%   | -1.05%             | -11.01% |    -1.06 |       63 | 33.28%     | ok               |
|          20 | -8.26%   | -1.05%             | -11.89% |    -1.18 |       68 | 39.27%     | ok               |
|          35 | -7.28%   | -1.05%             | -11.73% |    -1.19 |       62 | 29.78%     | ok               |

## ALGO-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -30.48%  | -51.61%            | -43.23% |    -0.18 |       82 | 42.15%     | ok               |
|          25 | -34.15%  | -51.61%            | -51.61% |    -0.21 |       84 | 46.55%     | ok               |
|          15 | -40.88%  | -51.61%            | -54.11% |    -0.28 |       79 | 52.49%     | ok               |
|          35 | -38.18%  | -51.61%            | -52.80% |    -0.38 |       70 | 37.36%     | ok               |
|          20 | -47.04%  | -51.61%            | -56.75% |    -0.42 |       83 | 49.23%     | ok               |

## AMAT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -18.25%  | 37.00%             | -40.12% |    -0.06 |       52 | 36.11%     | ok               |
|          15 | -26.05%  | 37.00%             | -53.90% |    -0.1  |       74 | 60.57%     | ok               |
|          35 | -27.85%  | 37.00%             | -52.00% |    -0.17 |       73 | 49.08%     | ok               |
|          30 | -32.84%  | 37.00%             | -57.56% |    -0.23 |       73 | 51.75%     | ok               |
|          40 | -34.73%  | 37.00%             | -55.32% |    -0.29 |       73 | 44.09%     | ok               |

## AMD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 45.01%   | 183.48%            | -37.12% |     0.6  |       50 | 31.28%     | ok               |
|          40 | 27.92%   | 183.48%            | -38.64% |     0.46 |       52 | 36.11%     | ok               |
|          35 | 17.30%   | 183.48%            | -40.22% |     0.37 |       60 | 37.60%     | ok               |
|          45 | 15.75%   | 183.48%            | -42.84% |     0.36 |       56 | 34.11%     | ok               |
|          30 | -0.34%   | 183.48%            | -47.20% |     0.22 |       63 | 40.27%     | ok               |

## AMGN Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 0.24%    | 51.81%             | -26.65% |     0.11 |       62 | 57.74%     | ok               |
|          35 | -2.39%   | 51.81%             | -31.29% |     0.05 |       65 | 49.08%     | ok               |
|          30 | -4.79%   | 51.81%             | -34.19% |    -0.01 |       63 | 52.41%     | ok               |
|          15 | -7.19%   | 51.81%             | -27.98% |    -0.04 |       61 | 61.73%     | ok               |
|          25 | -6.75%   | 51.81%             | -33.47% |    -0.04 |       59 | 54.58%     | ok               |

## AMZN Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -32.85%  | 40.88%             | -33.72% |    -1.02 |       60 | 30.28%     | ok               |
|          50 | -34.90%  | 40.88%             | -35.58% |    -1.27 |       52 | 22.96%     | ok               |
|          45 | -40.35%  | 40.88%             | -40.97% |    -1.45 |       60 | 26.62%     | ok               |
|          35 | -55.29%  | 40.88%             | -55.76% |    -1.66 |       81 | 35.61%     | ok               |
|          30 | -58.73%  | 40.88%             | -59.16% |    -1.73 |       84 | 41.60%     | ok               |

## APT-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 43.73%   | -87.56%            | -27.79% |     0.76 |       40 | 15.90%     | ok               |
|          45 | 13.94%   | -87.56%            | -52.49% |     0.36 |       62 | 23.37%     | ok               |
|          20 | -5.65%   | -87.56%            | -56.22% |     0.23 |       82 | 50.00%     | ok               |
|          15 | -28.45%  | -87.56%            | -58.22% |     0.01 |       79 | 56.13%     | ok               |
|          35 | -18.51%  | -87.56%            | -49.10% |     0.01 |       72 | 35.44%     | ok               |

## ARB-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 80.06%   | -48.00%            | -28.01% |     0.8  |       52 | 25.29%     | ok               |
|          50 | 54.63%   | -48.00%            | -30.72% |     0.66 |       42 | 18.39%     | ok               |
|          40 | 56.01%   | -48.00%            | -38.69% |     0.66 |       53 | 32.95%     | ok               |
|          35 | 54.09%   | -48.00%            | -40.80% |     0.64 |       67 | 37.36%     | ok               |
|          15 | 36.29%   | -48.00%            | -52.10% |     0.54 |       92 | 58.43%     | ok               |

## ARKK Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -10.04%  | 70.99%             | -37.76% |    -0    |       86 | 54.41%     | ok               |
|          20 | -19.04%  | 70.99%             | -34.82% |    -0.17 |       87 | 49.75%     | ok               |
|          30 | -25.96%  | 70.99%             | -31.47% |    -0.36 |       85 | 43.43%     | ok               |
|          35 | -33.73%  | 70.99%             | -39.22% |    -0.57 |       86 | 40.77%     | ok               |
|          25 | -36.62%  | 70.99%             | -42.86% |    -0.58 |       95 | 45.92%     | ok               |

## ATOM-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -40.37%  | -68.53%            | -56.26% |    -0.34 |       82 | 65.13%     | ok               |
|          25 | -43.44%  | -68.53%            | -58.01% |    -0.46 |       86 | 53.26%     | ok               |
|          20 | -48.13%  | -68.53%            | -62.05% |    -0.53 |       90 | 57.47%     | ok               |
|          45 | -45.91%  | -68.53%            | -55.84% |    -0.65 |       74 | 32.76%     | ok               |
|          40 | -51.74%  | -68.53%            | -62.66% |    -0.77 |       72 | 38.12%     | ok               |

## AVAX-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 51.06%   | -59.66%            | -22.06% |     0.81 |       34 | 19.54%     | ok               |
|          40 | 20.77%   | -59.66%            | -26.27% |     0.44 |       40 | 29.69%     | ok               |
|          45 | 11.74%   | -59.66%            | -24.48% |     0.33 |       36 | 25.29%     | ok               |
|          35 | 6.15%    | -59.66%            | -33.05% |     0.27 |       54 | 36.21%     | ok               |
|          15 | 2.90%    | -59.66%            | -43.71% |     0.26 |       73 | 54.21%     | ok               |

## AVGO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | 3.05%    | 60.59%             | -39.09% |     0.21 |       70 | 42.93%     | ok               |
|          30 | 0.17%    | 60.59%             | -40.82% |     0.17 |       66 | 40.27%     | ok               |
|          20 | -3.77%   | 60.59%             | -40.93% |     0.14 |       79 | 46.26%     | ok               |
|          35 | -10.37%  | 60.59%             | -44.84% |     0.03 |       74 | 37.27%     | ok               |
|          15 | -14.55%  | 60.59%             | -41.62% |     0.02 |       79 | 51.25%     | ok               |

## BA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 32.47%   | -2.80%             | -13.34% |     0.75 |       46 | 35.77%     | ok               |
|          35 | 27.01%   | -2.80%             | -18.09% |     0.54 |       68 | 48.42%     | ok               |
|          40 | 23.76%   | -2.80%             | -23.87% |     0.51 |       46 | 43.26%     | ok               |
|          25 | 22.64%   | -2.80%             | -26.02% |     0.46 |       66 | 55.07%     | ok               |
|          30 | 13.16%   | -2.80%             | -24.47% |     0.33 |       65 | 51.75%     | ok               |

## BAC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 1.87%    | 25.08%             | -16.89% |     0.13 |       80 | 54.08%     | ok               |
|          35 | 0.65%    | 25.08%             | -22.58% |     0.09 |       70 | 44.09%     | ok               |
|          45 | -0.38%   | 25.08%             | -15.21% |     0.05 |       56 | 34.28%     | ok               |
|          15 | -3.92%   | 25.08%             | -21.05% |    -0    |       86 | 60.07%     | ok               |
|          25 | -3.71%   | 25.08%             | -22.01% |    -0.02 |       80 | 52.08%     | ok               |

## BCH-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 17.04%   | -39.54%            | -45.51% |     0.39 |       80 | 56.51%     | ok               |
|          20 | 2.67%    | -39.54%            | -45.52% |     0.25 |       74 | 53.45%     | ok               |
|          35 | -9.06%   | -39.54%            | -57.75% |     0.1  |       72 | 44.06%     | ok               |
|          25 | -11.85%  | -39.54%            | -48.42% |     0.08 |       78 | 49.81%     | ok               |
|          30 | -14.22%  | -39.54%            | -54.04% |     0.04 |       82 | 47.89%     | ok               |

## BITO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -1.54%   | -59.94%            | -31.98% |     0.11 |       52 | 24.13%     | ok               |
|          45 | -15.11%  | -59.94%            | -32.05% |    -0.09 |       58 | 27.62%     | ok               |
|          15 | -30.70%  | -59.94%            | -53.24% |    -0.21 |       85 | 49.58%     | ok               |
|          40 | -24.97%  | -59.94%            | -40.13% |    -0.23 |       66 | 32.28%     | ok               |
|          30 | -27.99%  | -59.94%            | -43.13% |    -0.23 |       85 | 40.93%     | ok               |

## BLK Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 1.48%    | 50.93%             | -20.79% |     0.12 |       86 | 43.76%     | ok               |
|          20 | -2.07%   | 50.93%             | -21.48% |     0.03 |       82 | 51.91%     | ok               |
|          25 | -3.47%   | 50.93%             | -24.62% |    -0.01 |       75 | 49.75%     | ok               |
|          40 | -2.93%   | 50.93%             | -22.83% |    -0.01 |       78 | 39.27%     | ok               |
|          30 | -7.95%   | 50.93%             | -26.90% |    -0.14 |       79 | 47.25%     | ok               |

## BND Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -6.50%   | -1.11%             | -10.21% |    -0.92 |       64 | 40.93%     | ok               |
|          25 | -6.94%   | -1.11%             | -11.27% |    -1.02 |       69 | 38.60%     | ok               |
|          30 | -6.73%   | -1.11%             | -10.91% |    -1.04 |       67 | 34.94%     | ok               |
|          15 | -7.86%   | -1.11%             | -11.52% |    -1.1  |       76 | 43.43%     | ok               |
|          40 | -7.78%   | -1.11%             | -11.70% |    -1.34 |       56 | 28.79%     | ok               |

## BONK-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 105.74%  | -81.68%            | -28.97% |     1.06 |       38 | 16.48%     | ok               |
|          40 | 124.38%  | -81.68%            | -46.83% |     1.02 |       66 | 34.10%     | ok               |
|          45 | 104.72%  | -81.68%            | -35.44% |     0.98 |       62 | 22.99%     | ok               |
|          15 | 77.30%   | -81.68%            | -56.25% |     0.74 |       65 | 61.49%     | ok               |
|          35 | 65.17%   | -81.68%            | -53.18% |     0.72 |       66 | 40.04%     | ok               |

## BTC-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 33.26%   | -28.67%            | -12.58% |     0.74 |       40 | 29.89%     | ok               |
|          35 | 33.26%   | -28.67%            | -22.51% |     0.69 |       62 | 40.61%     | ok               |
|          40 | 29.80%   | -28.67%            | -19.29% |     0.66 |       48 | 34.67%     | ok               |
|          50 | 17.11%   | -28.67%            | -20.63% |     0.48 |       36 | 25.29%     | ok               |
|          30 | 3.36%    | -28.67%            | -23.71% |     0.19 |       72 | 46.36%     | ok               |

## C Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -12.24%  | 98.22%             | -22.72% |    -0.29 |       68 | 30.95%     | ok               |
|          45 | -22.47%  | 98.22%             | -30.69% |    -0.57 |       78 | 36.27%     | ok               |
|          40 | -27.35%  | 98.22%             | -35.05% |    -0.67 |       74 | 38.77%     | ok               |
|          25 | -34.24%  | 98.22%             | -37.53% |    -0.72 |       71 | 50.08%     | ok               |
|          20 | -36.29%  | 98.22%             | -39.30% |    -0.76 |       77 | 52.75%     | ok               |

## CAT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 49.44%   | 73.27%             | -21.99% |     0.73 |       73 | 61.73%     | ok               |
|          25 | 46.63%   | 73.27%             | -21.79% |     0.73 |       66 | 52.91%     | ok               |
|          45 | 37.73%   | 73.27%             | -23.56% |     0.66 |       54 | 39.10%     | ok               |
|          30 | 36.90%   | 73.27%             | -21.87% |     0.62 |       70 | 50.58%     | ok               |
|          50 | 31.92%   | 73.27%             | -21.79% |     0.59 |       54 | 37.27%     | ok               |

## CL Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 12.26%   | 0.64%              | -10.72% |     0.47 |       42 | 25.12%     | ok               |
|          45 | 6.45%    | 0.64%              | -10.96% |     0.28 |       46 | 27.62%     | ok               |
|          30 | 4.74%    | 0.64%              | -14.32% |     0.21 |       60 | 39.77%     | ok               |
|          40 | 1.36%    | 0.64%              | -15.09% |     0.11 |       52 | 30.95%     | ok               |
|          35 | 0.57%    | 0.64%              | -15.39% |     0.08 |       60 | 35.94%     | ok               |

## CMCSA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -15.93%  | -30.25%            | -26.31% |    -0.51 |       48 | 16.31%     | ok               |
|          45 | -23.42%  | -30.25%            | -34.99% |    -0.74 |       60 | 20.97%     | ok               |
|          15 | -36.63%  | -30.25%            | -44.16% |    -0.76 |       88 | 58.40%     | ok               |
|          40 | -31.30%  | -30.25%            | -42.42% |    -0.84 |       89 | 28.45%     | ok               |
|          30 | -37.44%  | -30.25%            | -46.48% |    -0.91 |       84 | 43.43%     | ok               |

## COMP-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -29.57%  | -55.32%            | -43.08% |    -0.24 |       50 | 23.37%     | ok               |
|          30 | -45.56%  | -55.32%            | -61.00% |    -0.33 |       99 | 49.04%     | ok               |
|          25 | -52.26%  | -55.32%            | -65.80% |    -0.43 |      100 | 57.28%     | ok               |
|          20 | -53.98%  | -55.32%            | -67.03% |    -0.44 |      106 | 63.41%     | ok               |
|          15 | -56.88%  | -55.32%            | -70.36% |    -0.45 |      103 | 68.20%     | ok               |

## COP Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -9.15%   | 24.40%             | -34.61% |    -0.1  |       48 | 30.45%     | ok               |
|          35 | -14.47%  | 24.40%             | -41.23% |    -0.18 |       67 | 41.26%     | ok               |
|          30 | -15.84%  | 24.40%             | -39.71% |    -0.2  |       64 | 43.59%     | ok               |
|          45 | -14.10%  | 24.40%             | -39.75% |    -0.2  |       60 | 34.11%     | ok               |
|          40 | -19.52%  | 24.40%             | -46.32% |    -0.32 |       66 | 37.27%     | ok               |

## COST Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 13.40%   | 21.39%             | -24.32% |     0.44 |       62 | 47.25%     | ok               |
|          25 | 9.68%    | 21.39%             | -24.93% |     0.35 |       59 | 44.26%     | ok               |
|          35 | 2.31%    | 21.39%             | -30.16% |     0.14 |       58 | 38.44%     | ok               |
|          15 | -1.97%   | 21.39%             | -27.30% |     0.02 |       67 | 50.92%     | ok               |
|          30 | -2.02%   | 21.39%             | -31.32% |     0    |       60 | 40.93%     | ok               |

## CRM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | -20.20%  | -7.30%             | -29.29% |    -0.23 |       64 | 41.26%     | ok               |
|          40 | -23.19%  | -7.30%             | -35.06% |    -0.32 |       70 | 37.10%     | ok               |
|          15 | -29.63%  | -7.30%             | -47.54% |    -0.33 |       94 | 58.24%     | ok               |
|          30 | -31.16%  | -7.30%             | -41.56% |    -0.44 |       67 | 46.09%     | ok               |
|          20 | -34.62%  | -7.30%             | -45.98% |    -0.45 |       74 | 51.75%     | ok               |

## CRV-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 57.12%   | -58.88%            | -37.78% |     0.69 |       64 | 32.57%     | ok               |
|          40 | 52.86%   | -58.88%            | -38.86% |     0.67 |       54 | 28.54%     | ok               |
|          45 | 37.85%   | -58.88%            | -42.29% |     0.57 |       56 | 22.03%     | ok               |
|          50 | 26.08%   | -58.88%            | -30.73% |     0.47 |       50 | 17.82%     | ok               |
|          30 | 21.28%   | -58.88%            | -39.89% |     0.43 |       64 | 36.97%     | ok               |

## CSCO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 37.68%   | 105.41%            | -19.34% |     0.75 |       52 | 41.26%     | ok               |
|          50 | 30.48%   | 105.41%            | -19.34% |     0.64 |       52 | 39.77%     | ok               |
|          40 | 22.36%   | 105.41%            | -22.37% |     0.49 |       56 | 43.93%     | ok               |
|          35 | 18.44%   | 105.41%            | -23.68% |     0.43 |       60 | 47.42%     | ok               |
|          25 | 11.54%   | 105.41%            | -23.73% |     0.31 |       65 | 51.75%     | ok               |

## CVX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -9.13%   | 38.79%             | -23.80% |    -0.14 |       71 | 45.76%     | ok               |
|          40 | -12.19%  | 38.79%             | -27.34% |    -0.27 |       75 | 39.10%     | ok               |
|          30 | -13.20%  | 38.79%             | -27.78% |    -0.27 |       69 | 42.93%     | ok               |
|          20 | -14.19%  | 38.79%             | -24.10% |    -0.28 |       75 | 47.42%     | ok               |
|          45 | -12.58%  | 38.79%             | -28.83% |    -0.29 |       67 | 35.77%     | ok               |

## DASH-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 115.44%  | 117.96%            | -43.46% |     0.87 |       42 | 17.82%     | ok               |
|          40 | 71.19%   | 117.96%            | -42.64% |     0.69 |       48 | 24.14%     | ok               |
|          45 | 63.01%   | 117.96%            | -46.93% |     0.65 |       46 | 20.31%     | ok               |
|          30 | -15.94%  | 117.96%            | -64.43% |     0.28 |       57 | 30.65%     | ok               |
|          25 | -16.74%  | 117.96%            | -64.14% |     0.27 |       67 | 32.95%     | ok               |

## DBC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -4.85%   | 36.24%             | -26.05% |    -0.08 |       81 | 42.43%     | ok               |
|          20 | -8.86%   | 36.24%             | -25.69% |    -0.22 |       73 | 40.60%     | ok               |
|          25 | -9.03%   | 36.24%             | -24.84% |    -0.23 |       68 | 38.44%     | ok               |
|          50 | -9.26%   | 36.24%             | -18.84% |    -0.3  |       50 | 25.46%     | ok               |
|          35 | -11.42%  | 36.24%             | -23.19% |    -0.33 |       68 | 35.11%     | ok               |

## DE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 1.37%    | 77.11%             | -17.97% |     0.11 |       58 | 29.95%     | ok               |
|          45 | -1.03%   | 77.11%             | -18.05% |     0.06 |       58 | 33.94%     | ok               |
|          20 | -3.07%   | 77.11%             | -22.20% |     0.04 |       66 | 48.59%     | ok               |
|          25 | -4.48%   | 77.11%             | -22.39% |     0    |       73 | 46.59%     | ok               |
|          30 | -4.58%   | 77.11%             | -21.34% |    -0    |       72 | 43.93%     | ok               |

## DIA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -7.33%   | 31.82%             | -13.29% |    -0.35 |       64 | 45.42%     | ok               |
|          20 | -9.57%   | 31.82%             | -15.31% |    -0.46 |       68 | 47.59%     | ok               |
|          35 | -9.02%   | 31.82%             | -16.66% |    -0.47 |       72 | 41.10%     | ok               |
|          30 | -9.43%   | 31.82%             | -15.92% |    -0.48 |       70 | 44.26%     | ok               |
|          40 | -11.61%  | 31.82%             | -18.14% |    -0.65 |       74 | 37.60%     | ok               |

## DIS Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 41.23%   | 15.00%             | -10.17% |     1.18 |       50 | 28.29%     | ok               |
|          40 | 11.94%   | 15.00%             | -18.75% |     0.36 |       65 | 36.44%     | ok               |
|          45 | 9.35%    | 15.00%             | -16.54% |     0.31 |       51 | 31.95%     | ok               |
|          15 | 3.47%    | 15.00%             | -32.73% |     0.17 |       81 | 55.57%     | ok               |
|          35 | 1.18%    | 15.00%             | -25.30% |     0.12 |       73 | 42.43%     | ok               |

## DOGE-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -15.05%  | -61.36%            | -59.12% |     0.1  |       81 | 62.84%     | ok               |
|          50 | -8.24%   | -61.36%            | -51.01% |     0.08 |       56 | 22.03%     | ok               |
|          20 | -19.46%  | -61.36%            | -58.83% |     0.02 |       79 | 57.28%     | ok               |
|          30 | -19.71%  | -61.36%            | -60.39% |    -0.02 |       68 | 47.70%     | ok               |
|          25 | -21.57%  | -61.36%            | -59.36% |    -0.02 |       72 | 52.87%     | ok               |

## DOT-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -49.50%  | -77.87%            | -65.96% |    -0.35 |       83 | 55.94%     | ok               |
|          15 | -54.39%  | -77.87%            | -72.35% |    -0.37 |       72 | 59.77%     | ok               |
|          30 | -50.30%  | -77.87%            | -63.40% |    -0.42 |       80 | 45.40%     | ok               |
|          25 | -57.35%  | -77.87%            | -71.03% |    -0.53 |       74 | 50.96%     | ok               |
|          35 | -57.08%  | -77.87%            | -65.25% |    -0.6  |       80 | 39.85%     | ok               |

## DXY-INDEX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -2.35%   | -6.47%             | -6.06%  |    -0.38 |       40 | 30.95%     | ok               |
|          40 | -4.84%   | -6.47%             | -7.30%  |    -0.67 |       68 | 46.54%     | ok               |
|          45 | -4.82%   | -6.47%             | -8.12%  |    -0.72 |       62 | 37.45%     | ok               |
|          15 | -9.12%   | -6.47%             | -11.81% |    -0.92 |       97 | 72.51%     | ok               |
|          30 | -7.97%   | -6.47%             | -9.98%  |    -1.01 |       78 | 56.71%     | ok               |

## EEM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -1.92%   | 39.60%             | -25.18% |     0.01 |       65 | 44.59%     | ok               |
|          25 | -3.00%   | 39.60%             | -23.69% |    -0.02 |       65 | 42.93%     | ok               |
|          35 | -4.82%   | 39.60%             | -23.88% |    -0.08 |       70 | 39.27%     | ok               |
|          15 | -6.17%   | 39.60%             | -26.83% |    -0.1  |       73 | 48.25%     | ok               |
|          40 | -5.29%   | 39.60%             | -19.52% |    -0.11 |       70 | 37.44%     | ok               |

## EFA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -0.91%   | 30.39%             | -10.10% |     0.03 |       60 | 49.08%     | ok               |
|          20 | -8.09%   | 30.39%             | -12.23% |    -0.28 |       67 | 46.26%     | ok               |
|          30 | -9.07%   | 30.39%             | -12.63% |    -0.35 |       64 | 38.94%     | ok               |
|          25 | -9.53%   | 30.39%             | -13.73% |    -0.36 |       68 | 42.60%     | ok               |
|          40 | -8.70%   | 30.39%             | -14.58% |    -0.37 |       58 | 34.28%     | ok               |

## EOG Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -15.43%  | 23.56%             | -35.34% |    -0.29 |       52 | 32.78%     | ok               |
|          40 | -18.81%  | 23.56%             | -37.39% |    -0.37 |       64 | 36.11%     | ok               |
|          35 | -22.58%  | 23.56%             | -39.96% |    -0.46 |       77 | 40.10%     | ok               |
|          50 | -21.23%  | 23.56%             | -35.63% |    -0.48 |       52 | 30.28%     | ok               |
|          30 | -29.89%  | 23.56%             | -47.87% |    -0.63 |       78 | 44.76%     | ok               |

## ETC-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | -1.83%   | -59.94%            | -42.62% |     0.14 |       46 | 31.42%     | ok               |
|          30 | -4.96%   | -59.94%            | -45.54% |     0.1  |       54 | 34.67%     | ok               |
|          50 | -2.30%   | -59.94%            | -28.33% |     0.1  |       28 | 18.20%     | ok               |
|          45 | -6.54%   | -59.94%            | -35.44% |     0.03 |       32 | 21.26%     | ok               |
|          40 | -8.94%   | -59.94%            | -40.48% |     0.01 |       46 | 25.67%     | ok               |

## ETH-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 108.52%  | -14.09%            | -30.11% |     1.11 |       59 | 46.55%     | ok               |
|          30 | 71.77%   | -14.09%            | -32.89% |     0.84 |       65 | 54.60%     | ok               |
|          40 | 55.90%   | -14.09%            | -33.11% |     0.78 |       60 | 38.70%     | ok               |
|          45 | 46.60%   | -14.09%            | -34.50% |     0.71 |       62 | 35.63%     | ok               |
|          25 | 51.29%   | -14.09%            | -40.90% |     0.68 |       61 | 58.43%     | ok               |

## EWJ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -18.52%  | 32.50%             | -30.00% |    -0.56 |       58 | 39.60%     | ok               |
|          25 | -20.52%  | 32.50%             | -29.85% |    -0.64 |       58 | 38.77%     | ok               |
|          15 | -22.43%  | 32.50%             | -31.15% |    -0.66 |       69 | 42.93%     | ok               |
|          30 | -22.18%  | 32.50%             | -29.40% |    -0.76 |       66 | 37.44%     | ok               |
|          45 | -23.62%  | 32.50%             | -27.35% |    -0.96 |       62 | 28.45%     | ok               |

## FCX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 3.46%    | 25.73%             | -30.39% |     0.19 |       54 | 32.78%     | ok               |
|          50 | 0.84%    | 25.73%             | -26.57% |     0.15 |       56 | 29.12%     | ok               |
|          40 | -9.66%   | 25.73%             | -42.89% |    -0    |       66 | 37.60%     | ok               |
|          30 | -25.17%  | 25.73%             | -46.84% |    -0.23 |       69 | 45.09%     | ok               |
|          35 | -28.94%  | 25.73%             | -50.12% |    -0.32 |       71 | 42.76%     | ok               |

## FET-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 9.55%    | -80.43%            | -59.58% |     0.37 |       71 | 57.66%     | ok               |
|          25 | -17.25%  | -80.43%            | -65.31% |     0.13 |       79 | 49.04%     | ok               |
|          20 | -19.01%  | -80.43%            | -66.17% |     0.13 |       82 | 54.21%     | ok               |
|          30 | -32.13%  | -80.43%            | -66.52% |    -0.06 |       79 | 44.83%     | ok               |
|          45 | -35.65%  | -80.43%            | -51.19% |    -0.34 |       54 | 22.61%     | ok               |

## FIL-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -37.35%  | -68.73%            | -61.02% |    -0.27 |       71 | 38.89%     | ok               |
|          40 | -37.92%  | -68.73%            | -57.60% |    -0.37 |       48 | 28.16%     | ok               |
|          15 | -52.63%  | -68.73%            | -72.54% |    -0.42 |       95 | 52.11%     | ok               |
|          35 | -45.70%  | -68.73%            | -66.22% |    -0.48 |       62 | 32.38%     | ok               |
|          20 | -60.43%  | -68.73%            | -77.06% |    -0.62 |       94 | 48.66%     | ok               |

## FXI Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -0.74%   | 31.89%             | -21.68% |     0.07 |       50 | 34.61%     | ok               |
|          25 | -0.86%   | 31.89%             | -22.57% |     0.06 |       48 | 31.45%     | ok               |
|          30 | -3.03%   | 31.89%             | -23.91% |     0.01 |       46 | 30.12%     | ok               |
|          20 | -6.09%   | 31.89%             | -24.53% |    -0.07 |       48 | 32.78%     | ok               |
|          35 | -6.68%   | 31.89%             | -27.53% |    -0.09 |       48 | 27.79%     | ok               |

## GDX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 0.00%    | 163.86%            | -30.00% |     0.15 |       80 | 51.08%     | ok               |
|          40 | -2.19%   | 163.86%            | -33.54% |     0.09 |       64 | 38.77%     | ok               |
|          30 | -3.66%   | 163.86%            | -33.40% |     0.08 |       66 | 44.93%     | ok               |
|          35 | -7.85%   | 163.86%            | -37.85% |     0.01 |       72 | 41.43%     | ok               |
|          25 | -12.74%  | 163.86%            | -41.65% |    -0.06 |       70 | 46.76%     | ok               |

## GDXJ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -11.44%  | 159.68%            | -34.84% |     0.02 |       70 | 51.41%     | ok               |
|          35 | -23.49%  | 159.68%            | -37.15% |    -0.21 |       68 | 41.60%     | ok               |
|          30 | -25.61%  | 159.68%            | -35.04% |    -0.24 |       68 | 44.26%     | ok               |
|          25 | -30.12%  | 159.68%            | -39.58% |    -0.29 |       73 | 47.42%     | ok               |
|          40 | -26.41%  | 159.68%            | -44.70% |    -0.29 |       62 | 39.10%     | ok               |

## GE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 4.89%    | 98.03%             | -21.25% |     0.2  |       60 | 33.78%     | ok               |
|          45 | -7.35%   | 98.03%             | -21.88% |    -0.05 |       72 | 36.77%     | ok               |
|          30 | -13.14%  | 98.03%             | -27.82% |    -0.14 |       78 | 48.42%     | ok               |
|          25 | -13.54%  | 98.03%             | -29.91% |    -0.14 |       74 | 50.25%     | ok               |
|          20 | -14.02%  | 98.03%             | -25.05% |    -0.14 |       74 | 52.91%     | ok               |

## GLD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | 21.05%   | 73.58%             | -13.87% |     0.54 |       48 | 47.59%     | ok               |
|          20 | 19.41%   | 73.58%             | -13.87% |     0.51 |       49 | 49.25%     | ok               |
|          30 | 11.67%   | 73.58%             | -14.15% |     0.35 |       52 | 46.09%     | ok               |
|          35 | 8.96%    | 73.58%             | -15.57% |     0.3  |       52 | 43.43%     | ok               |
|          15 | 9.15%    | 73.58%             | -18.05% |     0.29 |       55 | 52.75%     | ok               |

## GOOGL Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 75.48%   | 60.67%             | -17.38% |     1.18 |       59 | 44.59%     | ok               |
|          45 | 66.23%   | 60.67%             | -11.66% |     1.14 |       52 | 37.94%     | ok               |
|          30 | 72.70%   | 60.67%             | -18.46% |     1.12 |       57 | 48.42%     | ok               |
|          50 | 61.33%   | 60.67%             | -11.52% |     1.11 |       44 | 33.11%     | ok               |
|          25 | 70.07%   | 60.67%             | -17.79% |     1.08 |       57 | 50.92%     | ok               |

## GRT-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 79.02%   | -79.53%            | -36.70% |     0.79 |       70 | 62.45%     | ok               |
|          45 | 53.31%   | -79.53%            | -39.68% |     0.7  |       50 | 29.50%     | ok               |
|          30 | 51.93%   | -79.53%            | -43.87% |     0.65 |       75 | 47.89%     | ok               |
|          35 | 49.76%   | -79.53%            | -37.94% |     0.64 |       66 | 42.53%     | ok               |
|          25 | 51.66%   | -79.53%            | -37.25% |     0.64 |       80 | 53.07%     | ok               |

## GS Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 22.58%   | 92.33%             | -20.56% |     0.5  |       66 | 55.24%     | ok               |
|          40 | 7.27%    | 92.33%             | -16.16% |     0.25 |       64 | 40.93%     | ok               |
|          20 | 7.49%    | 92.33%             | -23.19% |     0.25 |       64 | 51.91%     | ok               |
|          25 | -0.60%   | 92.33%             | -23.32% |     0.09 |       66 | 49.92%     | ok               |
|          35 | -1.92%   | 92.33%             | -19.95% |     0.06 |       68 | 44.59%     | ok               |

## HBAR-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -21.78%  | -35.82%            | -49.09% |    -0.28 |       28 | 28.03%     | ok               |
|          40 | -23.48%  | -35.82%            | -51.16% |    -0.31 |       32 | 33.91%     | ok               |
|          35 | -27.72%  | -35.82%            | -56.01% |    -0.4  |       30 | 39.10%     | ok               |
|          30 | -28.48%  | -35.82%            | -56.47% |    -0.4  |       40 | 43.25%     | ok               |
|          50 | -24.56%  | -35.82%            | -39.47% |    -0.41 |       32 | 19.03%     | ok               |

## HD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 4.12%    | -1.73%             | -17.15% |     0.18 |       73 | 44.59%     | ok               |
|          35 | 2.75%    | -1.73%             | -18.52% |     0.15 |       74 | 39.93%     | ok               |
|          25 | 0.57%    | -1.73%             | -18.88% |     0.1  |       74 | 47.09%     | ok               |
|          40 | -1.42%   | -1.73%             | -18.05% |     0.03 |       76 | 34.94%     | ok               |
|          45 | -2.19%   | -1.73%             | -18.71% |     0    |       52 | 30.12%     | ok               |

## HON Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -10.86%  | 5.03%              | -20.54% |    -0.27 |       64 | 31.95%     | ok               |
|          45 | -14.48%  | 5.03%              | -22.88% |    -0.37 |       66 | 37.10%     | ok               |
|          35 | -27.07%  | 5.03%              | -31.66% |    -0.72 |       89 | 48.59%     | ok               |
|          30 | -28.67%  | 5.03%              | -33.87% |    -0.74 |       89 | 53.58%     | ok               |
|          40 | -26.84%  | 5.03%              | -31.84% |    -0.74 |       74 | 41.26%     | ok               |

## HYG Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -4.17%   | 0.16%              | -7.76%  |    -0.47 |       68 | 34.28%     | ok               |
|          45 | -5.94%   | 0.16%              | -8.86%  |    -0.71 |       68 | 30.62%     | ok               |
|          35 | -6.39%   | 0.16%              | -9.66%  |    -0.73 |       77 | 36.11%     | ok               |
|          30 | -6.94%   | 0.16%              | -10.69% |    -0.77 |       87 | 39.60%     | ok               |
|          25 | -7.66%   | 0.16%              | -11.32% |    -0.83 |       89 | 42.60%     | ok               |

## IBIT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 52.34%   | 12.81%             | -17.37% |     0.92 |       26 | 24.71%     | ok               |
|          15 | 57.37%   | 12.81%             | -19.20% |     0.85 |       48 | 42.55%     | ok               |
|          45 | 42.91%   | 12.81%             | -17.37% |     0.78 |       32 | 26.08%     | ok               |
|          30 | 28.87%   | 12.81%             | -18.95% |     0.56 |       46 | 35.10%     | ok               |
|          40 | 27.12%   | 12.81%             | -22.57% |     0.56 |       38 | 28.63%     | ok               |

## IBM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -13.99%  | 44.54%             | -49.43% |    -0.05 |       83 | 62.40%     | ok               |
|          35 | -18.22%  | 44.54%             | -47.10% |    -0.16 |       63 | 47.59%     | ok               |
|          30 | -19.93%  | 44.54%             | -48.94% |    -0.19 |       69 | 50.75%     | ok               |
|          20 | -26.33%  | 44.54%             | -53.45% |    -0.28 |       69 | 55.41%     | ok               |
|          50 | -27.41%  | 44.54%             | -45.97% |    -0.39 |       46 | 36.61%     | ok               |

## ICP-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 4.81%    | -52.63%            | -40.43% |     0.31 |       72 | 39.66%     | ok               |
|          15 | -24.93%  | -52.63%            | -59.70% |     0.1  |       72 | 51.34%     | ok               |
|          20 | -24.23%  | -52.63%            | -63.34% |     0.09 |       80 | 48.28%     | ok               |
|          40 | -13.27%  | -52.63%            | -46.21% |     0.06 |       62 | 29.89%     | ok               |
|          35 | -14.64%  | -52.63%            | -52.13% |     0.06 |       70 | 34.29%     | ok               |

## IEF Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -5.17%   | -2.44%             | -10.18% |    -0.61 |       72 | 42.43%     | ok               |
|          15 | -6.41%   | -2.44%             | -10.91% |    -0.74 |       71 | 44.09%     | ok               |
|          25 | -8.72%   | -2.44%             | -11.95% |    -1.09 |       76 | 39.43%     | ok               |
|          40 | -8.18%   | -2.44%             | -11.24% |    -1.19 |       60 | 26.46%     | ok               |
|          50 | -7.12%   | -2.44%             | -9.11%  |    -1.21 |       54 | 21.46%     | ok               |

## IEMG Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | 0.22%    | 35.10%             | -23.73% |     0.07 |       61 | 43.26%     | ok               |
|          35 | 0.30%    | 35.10%             | -21.81% |     0.07 |       67 | 39.93%     | ok               |
|          20 | -1.47%   | 35.10%             | -25.26% |     0.02 |       59 | 44.93%     | ok               |
|          40 | -1.41%   | 35.10%             | -18.43% |     0.01 |       66 | 37.60%     | ok               |
|          30 | -3.04%   | 35.10%             | -24.73% |    -0.03 |       62 | 40.93%     | ok               |

## INJ-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 26.67%   | -31.81%            | -35.85% |     0.47 |       44 | 32.76%     | ok               |
|          35 | 23.68%   | -31.81%            | -46.78% |     0.45 |       54 | 36.02%     | ok               |
|          45 | 7.95%    | -31.81%            | -38.47% |     0.3  |       52 | 27.20%     | ok               |
|          30 | -18.95%  | -31.81%            | -64.24% |     0.06 |       57 | 39.08%     | ok               |
|          15 | -23.81%  | -31.81%            | -66.08% |     0.05 |       71 | 47.13%     | ok               |

## INTC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 109.61%  | 81.67%             | -49.32% |     0.89 |       58 | 34.44%     | ok               |
|          50 | 103.09%  | 81.67%             | -48.35% |     0.87 |       62 | 30.62%     | ok               |
|          40 | 86.61%   | 81.67%             | -55.86% |     0.77 |       66 | 38.60%     | ok               |
|          15 | 86.38%   | 81.67%             | -53.65% |     0.74 |       78 | 59.57%     | ok               |
|          20 | 79.50%   | 81.67%             | -52.47% |     0.72 |       80 | 55.74%     | ok               |

## INTU Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 16.92%   | -43.32%            | -34.18% |     0.4  |       67 | 29.62%     | ok               |
|          35 | 12.94%   | -43.32%            | -41.63% |     0.33 |       69 | 41.93%     | ok               |
|          25 | 12.00%   | -43.32%            | -35.24% |     0.31 |       69 | 50.75%     | ok               |
|          45 | 10.47%   | -43.32%            | -36.41% |     0.29 |       65 | 33.61%     | ok               |
|          40 | 9.84%    | -43.32%            | -38.72% |     0.28 |       69 | 37.27%     | ok               |

## ITA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -0.12%   | 55.10%             | -21.48% |     0.06 |       68 | 34.94%     | ok               |
|          30 | -1.32%   | 55.10%             | -23.75% |     0.04 |       72 | 47.42%     | ok               |
|          15 | -2.28%   | 55.10%             | -28.06% |     0.04 |       73 | 59.90%     | ok               |
|          40 | -4.89%   | 55.10%             | -20.54% |    -0.08 |       70 | 39.93%     | ok               |
|          35 | -5.60%   | 55.10%             | -23.12% |    -0.09 |       72 | 43.59%     | ok               |

## IWM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd    |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:-------|---------:|---------:|:-----------|:-----------------|
|          25 | 17.01%   | 36.56%             | -8.02% |     0.63 |       54 | 36.11%     | ok               |
|          20 | 15.47%   | 36.56%             | -9.67% |     0.57 |       60 | 37.10%     | ok               |
|          40 | 10.02%   | 36.56%             | -9.06% |     0.45 |       48 | 29.62%     | ok               |
|          15 | 11.92%   | 36.56%             | -8.91% |     0.44 |       78 | 42.93%     | ok               |
|          30 | 10.62%   | 36.56%             | -8.62% |     0.43 |       58 | 34.78%     | ok               |

## JNJ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 18.54%   | 89.26%             | -10.97% |     0.74 |       44 | 35.27%     | ok               |
|          15 | 17.41%   | 89.26%             | -18.02% |     0.59 |       58 | 53.08%     | ok               |
|          30 | 12.36%   | 89.26%             | -17.51% |     0.47 |       60 | 46.59%     | ok               |
|          20 | 11.99%   | 89.26%             | -17.61% |     0.45 |       64 | 49.58%     | ok               |
|          45 | 8.40%    | 89.26%             | -13.35% |     0.37 |       50 | 38.94%     | ok               |

## JPM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 1.50%    | 71.55%             | -15.90% |     0.11 |       50 | 31.78%     | ok               |
|          45 | -8.97%   | 71.55%             | -21.91% |    -0.23 |       54 | 34.44%     | ok               |
|          20 | -24.26%  | 71.55%             | -35.58% |    -0.55 |       86 | 48.75%     | ok               |
|          40 | -21.46%  | 71.55%             | -28.47% |    -0.65 |       66 | 37.10%     | ok               |
|          35 | -22.15%  | 71.55%             | -27.43% |    -0.66 |       76 | 40.60%     | ok               |

## KO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 28.12%   | 52.78%             | -8.64%  |     0.94 |       52 | 38.77%     | ok               |
|          35 | 23.77%   | 52.78%             | -8.73%  |     0.82 |       56 | 37.27%     | ok               |
|          40 | 20.79%   | 52.78%             | -9.28%  |     0.77 |       58 | 33.94%     | ok               |
|          25 | 21.88%   | 52.78%             | -10.61% |     0.75 |       58 | 41.43%     | ok               |
|          50 | 8.01%    | 52.78%             | -16.13% |     0.37 |       42 | 28.12%     | ok               |

## LDO-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 135.64%  | -58.94%            | -39.01% |     0.98 |       72 | 59.77%     | ok               |
|          20 | 86.07%   | -58.94%            | -44.07% |     0.8  |       75 | 55.17%     | ok               |
|          30 | 65.61%   | -58.94%            | -53.44% |     0.71 |       66 | 48.08%     | ok               |
|          25 | 50.51%   | -58.94%            | -48.17% |     0.62 |       74 | 52.68%     | ok               |
|          35 | 38.27%   | -58.94%            | -60.70% |     0.56 |       76 | 41.00%     | ok               |

## LIN Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -1.76%   | 16.93%             | -22.01% |     0.01 |       69 | 43.93%     | ok               |
|          20 | -2.53%   | 16.93%             | -23.00% |    -0.02 |       64 | 46.76%     | ok               |
|          15 | -4.41%   | 16.93%             | -23.68% |    -0.08 |       70 | 49.75%     | ok               |
|          30 | -5.04%   | 16.93%             | -20.61% |    -0.11 |       70 | 41.10%     | ok               |
|          35 | -5.91%   | 16.93%             | -19.70% |    -0.16 |       72 | 34.78%     | ok               |

## LINK-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 29.72%   | -23.07%            | -35.01% |     0.5  |       68 | 43.10%     | ok               |
|          35 | 17.80%   | -23.07%            | -34.21% |     0.4  |       62 | 39.27%     | ok               |
|          45 | 11.40%   | -23.07%            | -33.71% |     0.33 |       54 | 30.08%     | ok               |
|          40 | 10.95%   | -23.07%            | -34.00% |     0.32 |       56 | 33.72%     | ok               |
|          50 | 11.01%   | -23.07%            | -27.70% |     0.32 |       46 | 24.90%     | ok               |

## LLY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -0.88%   | 52.99%             | -38.23% |     0.1  |       50 | 35.44%     | ok               |
|          15 | -14.87%  | 52.99%             | -48.12% |    -0.09 |       70 | 60.23%     | ok               |
|          45 | -14.30%  | 52.99%             | -42.99% |    -0.16 |       60 | 39.27%     | ok               |
|          40 | -23.35%  | 52.99%             | -45.23% |    -0.32 |       70 | 42.43%     | ok               |
|          20 | -26.70%  | 52.99%             | -51.14% |    -0.33 |       77 | 55.41%     | ok               |

## LRCX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 12.29%   | 87.03%             | -42.40% |     0.31 |       74 | 36.27%     | ok               |
|          40 | 8.54%    | 87.03%             | -47.73% |     0.28 |       70 | 42.43%     | ok               |
|          45 | -1.06%   | 87.03%             | -47.62% |     0.18 |       74 | 40.10%     | ok               |
|          35 | -5.21%   | 87.03%             | -56.72% |     0.14 |       80 | 44.76%     | ok               |
|          15 | -9.35%   | 87.03%             | -56.52% |     0.13 |       81 | 53.41%     | ok               |

## LTC-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 18.97%   | -42.03%            | -34.94% |     0.41 |       68 | 44.06%     | ok               |
|          45 | 14.03%   | -42.03%            | -36.44% |     0.36 |       56 | 33.52%     | ok               |
|          30 | 10.16%   | -42.03%            | -30.78% |     0.32 |       69 | 50.77%     | ok               |
|          25 | 8.88%    | -42.03%            | -34.22% |     0.3  |       69 | 53.45%     | ok               |
|          50 | 1.89%    | -42.03%            | -35.25% |     0.19 |       50 | 25.10%     | ok               |

## MCD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 9.38%    | 9.08%              | -9.22%  |     0.45 |       48 | 25.12%     | ok               |
|          30 | 8.94%    | 9.08%              | -22.20% |     0.36 |       77 | 40.43%     | ok               |
|          35 | 6.81%    | 9.08%              | -16.97% |     0.3  |       69 | 37.77%     | ok               |
|          25 | 5.56%    | 9.08%              | -23.93% |     0.25 |       77 | 42.93%     | ok               |
|          20 | 1.26%    | 9.08%              | -24.58% |     0.1  |       79 | 46.09%     | ok               |

## META Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -13.50%  | 20.43%             | -37.54% |    -0.14 |       68 | 39.27%     | ok               |
|          40 | -17.14%  | 20.43%             | -40.90% |    -0.19 |       68 | 42.60%     | ok               |
|          50 | -22.46%  | 20.43%             | -39.33% |    -0.34 |       68 | 34.94%     | ok               |
|          30 | -29.66%  | 20.43%             | -44.90% |    -0.43 |       72 | 50.25%     | ok               |
|          25 | -31.78%  | 20.43%             | -45.70% |    -0.46 |       73 | 52.91%     | ok               |

## MPC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 19.12%   | 117.05%            | -19.02% |     0.43 |       54 | 41.60%     | ok               |
|          40 | 17.16%   | 117.05%            | -20.88% |     0.39 |       64 | 48.25%     | ok               |
|          35 | 16.33%   | 117.05%            | -31.08% |     0.38 |       70 | 50.92%     | ok               |
|          45 | 15.10%   | 117.05%            | -20.23% |     0.37 |       60 | 45.59%     | ok               |
|          30 | 10.68%   | 117.05%            | -33.74% |     0.29 |       70 | 53.24%     | ok               |

## MRK Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -13.24%  | 15.08%             | -28.39% |    -0.16 |       85 | 52.08%     | ok               |
|          25 | -14.00%  | 15.08%             | -31.07% |    -0.2  |       72 | 44.26%     | ok               |
|          20 | -18.22%  | 15.08%             | -29.34% |    -0.3  |       77 | 47.59%     | ok               |
|          50 | -14.69%  | 15.08%             | -23.01% |    -0.3  |       58 | 28.62%     | ok               |
|          45 | -16.81%  | 15.08%             | -25.38% |    -0.34 |       59 | 31.95%     | ok               |

## MS Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 0.02%    | 86.97%             | -22.02% |     0.1  |       74 | 57.74%     | ok               |
|          40 | 0.40%    | 86.97%             | -19.99% |     0.09 |       70 | 39.10%     | ok               |
|          20 | -3.21%   | 86.97%             | -25.68% |     0.02 |       75 | 53.41%     | ok               |
|          30 | -7.18%   | 86.97%             | -27.79% |    -0.09 |       77 | 48.42%     | ok               |
|          25 | -8.64%   | 86.97%             | -28.36% |    -0.12 |       75 | 50.58%     | ok               |

## MSFT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -15.96%  | 18.34%             | -24.64% |    -0.37 |       70 | 36.94%     | ok               |
|          50 | -19.36%  | 18.34%             | -25.48% |    -0.5  |       60 | 31.78%     | ok               |
|          35 | -25.42%  | 18.34%             | -35.38% |    -0.57 |       73 | 46.26%     | ok               |
|          40 | -25.20%  | 18.34%             | -34.92% |    -0.59 |       69 | 40.60%     | ok               |
|          30 | -28.52%  | 18.34%             | -39.07% |    -0.63 |       83 | 50.92%     | ok               |

## MU Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 118.49%  | 366.75%            | -63.96% |     0.93 |       60 | 45.26%     | ok               |
|          30 | 96.55%   | 366.75%            | -68.76% |     0.83 |       53 | 49.92%     | ok               |
|          35 | 91.12%   | 366.75%            | -69.09% |     0.81 |       65 | 47.59%     | ok               |
|          15 | 99.24%   | 366.75%            | -61.96% |     0.8  |       56 | 58.40%     | ok               |
|          25 | 85.56%   | 366.75%            | -67.90% |     0.77 |       55 | 51.58%     | ok               |

## NEAR-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 235.36%  | 53.37%             | -37.89% |     1.45 |       28 | 22.61%     | ok               |
|          40 | 257.67%  | 53.37%             | -41.76% |     1.41 |       40 | 32.38%     | ok               |
|          45 | 200.17%  | 53.37%             | -38.08% |     1.26 |       42 | 28.35%     | ok               |
|          30 | 169.55%  | 53.37%             | -47.35% |     1.11 |       63 | 42.91%     | ok               |
|          35 | 158.28%  | 53.37%             | -52.65% |     1.1  |       58 | 36.02%     | ok               |

## NEM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -4.57%   | 195.55%            | -30.50% |     0.1  |       71 | 54.08%     | ok               |
|          15 | -7.30%   | 195.55%            | -35.45% |     0.08 |       66 | 58.74%     | ok               |
|          50 | -12.51%  | 195.55%            | -33.03% |    -0.06 |       48 | 37.77%     | ok               |
|          25 | -19.14%  | 195.55%            | -39.51% |    -0.12 |       68 | 51.75%     | ok               |
|          30 | -25.86%  | 195.55%            | -39.56% |    -0.25 |       70 | 49.75%     | ok               |

## NFLX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 18.49%   | -6.17%             | -20.78% |     0.49 |       54 | 39.10%     | ok               |
|          50 | 16.07%   | -6.17%             | -16.28% |     0.47 |       44 | 31.11%     | ok               |
|          35 | 14.45%   | -6.17%             | -18.30% |     0.39 |       78 | 43.76%     | ok               |
|          45 | 4.47%    | -6.17%             | -18.06% |     0.19 |       58 | 35.44%     | ok               |
|          15 | 0.97%    | -6.17%             | -26.59% |     0.14 |       76 | 63.89%     | ok               |

## NKE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | -18.39%  | -59.38%            | -42.13% |    -0.19 |       73 | 40.43%     | ok               |
|          20 | -24.98%  | -59.38%            | -49.34% |    -0.24 |       87 | 55.24%     | ok               |
|          25 | -28.09%  | -59.38%            | -51.20% |    -0.3  |       87 | 52.58%     | ok               |
|          15 | -31.51%  | -59.38%            | -55.79% |    -0.35 |       90 | 59.07%     | ok               |
|          30 | -30.90%  | -59.38%            | -55.35% |    -0.36 |       85 | 48.09%     | ok               |

## NOW Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -8.26%   | -29.72%            | -42.66% |     0.12 |       79 | 51.58%     | ok               |
|          20 | -10.81%  | -29.72%            | -49.77% |     0.1  |       73 | 57.40%     | ok               |
|          25 | -14.84%  | -29.72%            | -47.93% |     0.04 |       71 | 54.91%     | ok               |
|          15 | -16.43%  | -29.72%            | -52.56% |     0.03 |       81 | 60.23%     | ok               |
|          35 | -20.72%  | -29.72%            | -48.24% |    -0.07 |       82 | 46.76%     | ok               |

## NVDA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -29.29%  | 58.06%             | -39.50% |    -0.32 |       76 | 51.52%     | ok               |
|          25 | -34.29%  | 58.06%             | -44.52% |    -0.46 |       81 | 47.59%     | ok               |
|          30 | -34.07%  | 58.06%             | -43.72% |    -0.48 |       82 | 44.74%     | ok               |
|          15 | -41.13%  | 58.06%             | -51.51% |    -0.55 |       82 | 55.79%     | ok               |
|          35 | -43.99%  | 58.06%             | -52.08% |    -0.75 |       92 | 41.89%     | ok               |

## OP-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 23.24%   | -83.20%            | -30.63% |     0.49 |       34 | 9.58%      | ok               |
|          45 | 12.13%   | -83.20%            | -36.09% |     0.33 |       40 | 15.52%     | ok               |
|          40 | -10.05%  | -83.20%            | -47.76% |     0.08 |       50 | 24.14%     | ok               |
|          15 | -34.08%  | -83.20%            | -55.83% |    -0.12 |       75 | 45.79%     | ok               |
|          30 | -34.58%  | -83.20%            | -58.87% |    -0.2  |       72 | 34.87%     | ok               |

## ORCL Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 146.17%  | -17.84%            | -32.54% |     1.06 |       65 | 60.07%     | ok               |
|          25 | 97.93%   | -17.84%            | -27.76% |     0.86 |       57 | 52.58%     | ok               |
|          45 | 84.00%   | -17.84%            | -32.35% |     0.85 |       54 | 38.10%     | ok               |
|          35 | 88.56%   | -17.84%            | -31.95% |     0.84 |       58 | 46.76%     | ok               |
|          20 | 92.41%   | -17.84%            | -29.32% |     0.83 |       66 | 55.74%     | ok               |

## OXY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 2.72%    | -6.35%             | -28.48% |     0.17 |       67 | 43.26%     | ok               |
|          35 | 1.42%    | -6.35%             | -26.37% |     0.14 |       68 | 39.10%     | ok               |
|          40 | -2.82%   | -6.35%             | -28.30% |     0.06 |       58 | 35.94%     | ok               |
|          50 | -4.85%   | -6.35%             | -27.38% |     0.01 |       48 | 29.28%     | ok               |
|          25 | -11.60%  | -6.35%             | -38.51% |    -0.07 |       77 | 46.76%     | ok               |

## PEP Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 16.49%   | -14.93%            | -11.62% |     0.69 |       40 | 25.46%     | ok               |
|          45 | 4.94%    | -14.93%            | -14.22% |     0.25 |       52 | 29.28%     | ok               |
|          30 | 1.81%    | -14.93%            | -21.35% |     0.12 |       74 | 45.09%     | ok               |
|          35 | 0.22%    | -14.93%            | -21.42% |     0.07 |       77 | 39.43%     | ok               |
|          40 | -1.83%   | -14.93%            | -18.04% |    -0.01 |       68 | 34.44%     | ok               |

## PEPE-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -42.79%  | -54.48%            | -62.32% |    -0.09 |       81 | 61.30%     | ok               |
|          30 | -35.81%  | -54.48%            | -57.70% |    -0.11 |       74 | 46.93%     | ok               |
|          20 | -41.00%  | -54.48%            | -61.15% |    -0.13 |       89 | 57.28%     | ok               |
|          35 | -41.61%  | -54.48%            | -58.37% |    -0.27 |       66 | 43.10%     | ok               |
|          25 | -52.11%  | -54.48%            | -62.02% |    -0.35 |       88 | 51.92%     | ok               |

## PFE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -12.26%  | 8.93%              | -23.37% |    -0.35 |       50 | 22.63%     | ok               |
|          50 | -11.32%  | 8.93%              | -25.42% |    -0.35 |       38 | 19.30%     | ok               |
|          40 | -13.90%  | 8.93%              | -27.08% |    -0.39 |       70 | 27.62%     | ok               |
|          35 | -22.19%  | 8.93%              | -32.87% |    -0.65 |       80 | 34.11%     | ok               |
|          30 | -32.40%  | 8.93%              | -41.77% |    -0.98 |       77 | 37.44%     | ok               |

## PG Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -8.32%   | -1.25%             | -20.08% |    -0.27 |       52 | 29.45%     | ok               |
|          35 | -11.45%  | -1.25%             | -18.99% |    -0.38 |       60 | 32.95%     | ok               |
|          45 | -16.09%  | -1.25%             | -22.00% |    -0.62 |       52 | 27.12%     | ok               |
|          30 | -19.49%  | -1.25%             | -24.55% |    -0.69 |       62 | 36.11%     | ok               |
|          25 | -21.33%  | -1.25%             | -25.84% |    -0.76 |       74 | 37.60%     | ok               |

## PM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | -5.00%   | 93.90%             | -34.56% |    -0.03 |       86 | 45.26%     | ok               |
|          20 | -7.48%   | 93.90%             | -36.03% |    -0.07 |       85 | 53.91%     | ok               |
|          30 | -7.98%   | 93.90%             | -37.61% |    -0.09 |       81 | 48.75%     | ok               |
|          50 | -9.99%   | 93.90%             | -36.94% |    -0.18 |       68 | 35.61%     | ok               |
|          40 | -12.25%  | 93.90%             | -39.92% |    -0.23 |       80 | 41.26%     | ok               |

## POL-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 13.64%   | -59.11%            | -44.63% |     0.36 |       83 | 50.57%     | ok               |
|          25 | 6.01%    | -59.11%            | -44.63% |     0.29 |       73 | 55.36%     | ok               |
|          20 | -3.19%   | -59.11%            | -46.84% |     0.2  |       84 | 59.00%     | ok               |
|          40 | 0.84%    | -59.11%            | -31.71% |     0.19 |       60 | 32.18%     | ok               |
|          50 | -5.81%   | -59.11%            | -29.40% |     0.06 |       52 | 21.07%     | ok               |

## QCOM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -28.27%  | -25.56%            | -54.50% |    -0.21 |       73 | 42.60%     | ok               |
|          20 | -33.55%  | -25.56%            | -54.38% |    -0.29 |       69 | 45.92%     | ok               |
|          35 | -34.33%  | -25.56%            | -50.58% |    -0.35 |       81 | 38.27%     | ok               |
|          15 | -41.58%  | -25.56%            | -57.94% |    -0.42 |       71 | 48.59%     | ok               |
|          30 | -41.99%  | -25.56%            | -56.59% |    -0.48 |       79 | 40.77%     | ok               |

## QQQ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 8.21%    | 35.26%             | -14.17% |     0.28 |       71 | 52.75%     | ok               |
|          25 | 4.65%    | 35.26%             | -12.88% |     0.2  |       65 | 45.59%     | ok               |
|          20 | 3.39%    | 35.26%             | -12.98% |     0.17 |       77 | 48.75%     | ok               |
|          30 | -2.41%   | 35.26%             | -14.20% |     0.01 |       70 | 43.59%     | ok               |
|          35 | -12.44%  | 35.26%             | -20.59% |    -0.3  |       76 | 39.77%     | ok               |

## RENDER-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 21.61%   | -58.42%            | -44.75% |     0.46 |       84 | 63.41%     | ok               |
|          20 | 10.90%   | -58.42%            | -43.37% |     0.38 |       89 | 59.20%     | ok               |
|          25 | -1.38%   | -58.42%            | -43.13% |     0.27 |       87 | 54.41%     | ok               |
|          30 | -43.38%  | -58.42%            | -54.16% |    -0.25 |       90 | 48.66%     | ok               |
|          35 | -47.39%  | -58.42%            | -57.40% |    -0.37 |       84 | 43.10%     | ok               |

## RTX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 36.77%   | 81.42%             | -18.66% |     0.77 |       73 | 57.40%     | ok               |
|          25 | 32.09%   | 81.42%             | -18.59% |     0.7  |       61 | 54.74%     | ok               |
|          15 | 28.50%   | 81.42%             | -19.55% |     0.63 |       66 | 61.90%     | ok               |
|          30 | 22.85%   | 81.42%             | -16.99% |     0.55 |       68 | 51.75%     | ok               |
|          50 | 14.34%   | 81.42%             | -18.42% |     0.46 |       60 | 39.27%     | ok               |

## SBUX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | 1.41%    | 29.61%             | -23.55% |     0.13 |       61 | 41.93%     | ok               |
|          40 | 0.03%    | 29.61%             | -25.43% |     0.09 |       62 | 33.61%     | ok               |
|          45 | -1.87%   | 29.61%             | -27.26% |     0.04 |       68 | 28.79%     | ok               |
|          35 | -4.13%   | 29.61%             | -26.54% |     0.01 |       64 | 36.77%     | ok               |
|          20 | -10.68%  | 29.61%             | -30.94% |    -0.1  |       64 | 43.93%     | ok               |

## SCHW Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -1.47%   | 25.66%             | -29.24% |     0.06 |       71 | 52.58%     | ok               |
|          25 | -3.28%   | 25.66%             | -28.76% |     0.02 |       67 | 50.92%     | ok               |
|          15 | -5.55%   | 25.66%             | -31.37% |    -0.03 |       76 | 56.41%     | ok               |
|          45 | -3.45%   | 25.66%             | -16.53% |    -0.04 |       62 | 31.28%     | ok               |
|          50 | -3.90%   | 25.66%             | -13.28% |    -0.08 |       54 | 28.12%     | ok               |

## SHIB-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -19.82%  | -64.72%            | -43.76% |    -0.04 |       85 | 66.48%     | ok               |
|          20 | -23.23%  | -64.72%            | -47.65% |    -0.1  |       80 | 61.88%     | ok               |
|          50 | -14.72%  | -64.72%            | -32.18% |    -0.1  |       50 | 22.41%     | ok               |
|          35 | -23.56%  | -64.72%            | -43.57% |    -0.16 |       75 | 46.36%     | ok               |
|          40 | -26.98%  | -64.72%            | -41.51% |    -0.25 |       58 | 37.74%     | ok               |

## SHY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd    |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:-------|---------:|---------:|:-----------|:-----------------|
|          30 | -1.88%   | 0.12%              | -3.18% |    -0.62 |       54 | 38.44%     | ok               |
|          35 | -2.42%   | 0.12%              | -3.49% |    -0.81 |       56 | 36.27%     | ok               |
|          40 | -2.50%   | 0.12%              | -3.58% |    -0.85 |       56 | 34.94%     | ok               |
|          25 | -2.83%   | 0.12%              | -4.32% |    -0.91 |       64 | 41.26%     | ok               |
|          45 | -2.66%   | 0.12%              | -3.43% |    -0.97 |       56 | 29.45%     | ok               |

## SKY-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -57.93%  | -12.41%            | -65.72% |    -0.77 |       79 | 54.98%     | ok               |
|          35 | -54.76%  | -12.41%            | -60.94% |    -0.87 |       78 | 36.40%     | ok               |
|          30 | -57.85%  | -12.41%            | -63.60% |    -0.89 |       87 | 44.44%     | ok               |
|          25 | -62.61%  | -12.41%            | -66.89% |    -1    |       80 | 47.70%     | ok               |
|          45 | -57.33%  | -12.41%            | -61.83% |    -1.05 |       74 | 27.20%     | ok               |

## SLB Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -5.98%   | 14.42%             | -24.85% |    -0.03 |       58 | 30.95%     | ok               |
|          40 | -11.54%  | 14.42%             | -28.04% |    -0.14 |       50 | 33.78%     | ok               |
|          50 | -11.75%  | 14.42%             | -27.36% |    -0.2  |       48 | 24.79%     | ok               |
|          35 | -36.22%  | 14.42%             | -47.04% |    -0.74 |       78 | 41.76%     | ok               |
|          25 | -43.70%  | 14.42%             | -54.16% |    -0.87 |       87 | 52.08%     | ok               |

## SLV Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 71.24%   | 74.11%             | -28.72% |     0.9  |       50 | 31.28%     | ok               |
|          45 | 56.70%   | 74.11%             | -31.33% |     0.77 |       61 | 32.78%     | ok               |
|          40 | 55.46%   | 74.11%             | -34.28% |     0.75 |       65 | 34.78%     | ok               |
|          20 | 40.66%   | 74.11%             | -37.05% |     0.6  |       70 | 44.93%     | ok               |
|          35 | 36.25%   | 74.11%             | -37.86% |     0.57 |       74 | 37.94%     | ok               |

## SMH Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 70.91%   | 70.27%             | -31.66% |     0.96 |       49 | 44.93%     | ok               |
|          25 | 55.45%   | 70.27%             | -33.57% |     0.83 |       46 | 43.43%     | ok               |
|          30 | 51.22%   | 70.27%             | -34.29% |     0.79 |       50 | 42.10%     | ok               |
|          35 | 39.97%   | 70.27%             | -34.65% |     0.68 |       56 | 40.10%     | ok               |
|          45 | 27.60%   | 70.27%             | -33.35% |     0.55 |       56 | 34.28%     | ok               |

## SNX-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 31.04%   | -75.21%            | -41.29% |     0.53 |       54 | 30.46%     | ok               |
|          40 | 26.63%   | -75.21%            | -30.13% |     0.5  |       46 | 26.05%     | ok               |
|          20 | 26.59%   | -75.21%            | -53.03% |     0.48 |       69 | 45.79%     | ok               |
|          15 | 12.60%   | -75.21%            | -54.74% |     0.37 |       70 | 49.81%     | ok               |
|          30 | 12.33%   | -75.21%            | -50.74% |     0.35 |       60 | 36.59%     | ok               |

## SOL-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 44.94%   | -41.44%            | -40.41% |     0.65 |       58 | 39.27%     | ok               |
|          35 | 11.41%   | -41.44%            | -44.32% |     0.34 |       72 | 45.02%     | ok               |
|          45 | 6.03%    | -41.44%            | -47.42% |     0.26 |       54 | 32.95%     | ok               |
|          15 | 0.55%    | -41.44%            | -46.18% |     0.24 |       71 | 63.41%     | ok               |
|          25 | -1.96%   | -41.44%            | -39.39% |     0.2  |       69 | 55.75%     | ok               |

## SOXX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | 68.96%   | 59.98%             | -39.32% |     0.91 |       55 | 43.09%     | ok               |
|          35 | 65.15%   | 59.98%             | -38.76% |     0.9  |       58 | 38.60%     | ok               |
|          30 | 64.26%   | 59.98%             | -39.81% |     0.88 |       56 | 40.93%     | ok               |
|          20 | 54.04%   | 59.98%             | -39.19% |     0.77 |       61 | 44.09%     | ok               |
|          40 | 44.95%   | 59.98%             | -41.03% |     0.71 |       60 | 36.44%     | ok               |

## SPY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 4.35%    | 34.40%             | -14.25% |     0.21 |       60 | 51.25%     | ok               |
|          15 | 4.29%    | 34.40%             | -16.80% |     0.2  |       66 | 54.08%     | ok               |
|          25 | -0.34%   | 34.40%             | -14.25% |     0.05 |       60 | 50.25%     | ok               |
|          30 | -5.21%   | 34.40%             | -15.53% |    -0.12 |       63 | 47.75%     | ok               |
|          35 | -6.13%   | 34.40%             | -15.58% |    -0.16 |       61 | 44.59%     | ok               |

## SUSHI-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -8.82%   | -72.55%            | -34.86% |     0.04 |       60 | 17.05%     | ok               |
|          35 | -41.97%  | -72.55%            | -68.76% |    -0.35 |       79 | 36.97%     | ok               |
|          45 | -35.78%  | -72.55%            | -58.06% |    -0.36 |       64 | 23.37%     | ok               |
|          40 | -39.30%  | -72.55%            | -62.11% |    -0.37 |       66 | 31.61%     | ok               |
|          15 | -61.91%  | -72.55%            | -78.43% |    -0.59 |       85 | 52.68%     | ok               |

## T Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 71.51%   | 22.41%             | -15.08% |     1.12 |       71 | 65.89%     | ok               |
|          20 | 67.28%   | 22.41%             | -18.13% |     1.1  |       66 | 61.40%     | ok               |
|          25 | 65.38%   | 22.41%             | -17.66% |     1.09 |       66 | 59.23%     | ok               |
|          30 | 54.46%   | 22.41%             | -17.01% |     0.97 |       68 | 57.24%     | ok               |
|          35 | 36.33%   | 22.41%             | -14.49% |     0.74 |       74 | 52.58%     | ok               |

## TGT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -8.89%   | 9.27%              | -32.83% |    -0.11 |       58 | 37.27%     | ok               |
|          25 | -10.70%  | 9.27%              | -34.49% |    -0.14 |       66 | 40.27%     | ok               |
|          20 | -12.30%  | 9.27%              | -36.78% |    -0.15 |       86 | 44.93%     | ok               |
|          45 | -12.30%  | 9.27%              | -26.12% |    -0.24 |       48 | 28.79%     | ok               |
|          15 | -18.34%  | 9.27%              | -36.22% |    -0.26 |       72 | 49.75%     | ok               |

## TIA-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -32.13%  | -78.43%            | -69.28% |     0.06 |       96 | 59.58%     | ok               |
|          25 | -31.89%  | -78.43%            | -69.36% |     0    |       92 | 48.47%     | ok               |
|          35 | -26.19%  | -78.43%            | -66.58% |    -0.05 |       74 | 36.02%     | ok               |
|          20 | -47.22%  | -78.43%            | -73.95% |    -0.15 |       92 | 54.02%     | ok               |
|          30 | -44.86%  | -78.43%            | -75.93% |    -0.19 |       91 | 43.10%     | ok               |

## TLT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -9.84%   | -12.60%            | -13.09% |    -1.09 |       30 | 16.97%     | ok               |
|          40 | -14.77%  | -12.60%            | -17.65% |    -1.31 |       48 | 24.46%     | ok               |
|          45 | -13.38%  | -12.60%            | -15.60% |    -1.4  |       40 | 19.97%     | ok               |
|          30 | -19.75%  | -12.60%            | -21.85% |    -1.5  |       66 | 34.11%     | ok               |
|          35 | -19.56%  | -12.60%            | -21.68% |    -1.66 |       66 | 28.62%     | ok               |

## TMO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 50.73%   | 22.32%             | -8.17%  |     1.07 |       50 | 35.27%     | ok               |
|          45 | 43.82%   | 22.32%             | -9.69%  |     0.92 |       54 | 40.10%     | ok               |
|          35 | 41.67%   | 22.32%             | -13.84% |     0.81 |       65 | 50.42%     | ok               |
|          40 | 36.94%   | 22.32%             | -11.54% |     0.79 |       59 | 45.26%     | ok               |
|          20 | 36.28%   | 22.32%             | -22.89% |     0.68 |       74 | 60.90%     | ok               |

## TMUS Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -5.87%   | -8.67%             | -41.04% |    -0.01 |       68 | 60.07%     | ok               |
|          30 | -7.14%   | -8.67%             | -33.05% |    -0.06 |       74 | 47.25%     | ok               |
|          25 | -9.77%   | -8.67%             | -39.29% |    -0.1  |       75 | 50.25%     | ok               |
|          20 | -11.30%  | -8.67%             | -39.79% |    -0.13 |       74 | 54.41%     | ok               |
|          50 | -10.08%  | -8.67%             | -32.38% |    -0.21 |       60 | 32.78%     | ok               |

## TRX-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 11.22%   | 14.06%             | -18.79% |     0.42 |       54 | 38.12%     | ok               |
|          50 | 3.84%    | 14.06%             | -22.22% |     0.2  |       44 | 32.95%     | ok               |
|          35 | 3.69%    | 14.06%             | -21.77% |     0.19 |       62 | 45.21%     | ok               |
|          45 | 2.84%    | 14.06%             | -24.19% |     0.17 |       48 | 34.48%     | ok               |
|          30 | 2.61%    | 14.06%             | -22.90% |     0.16 |       62 | 47.70%     | ok               |

## TSLA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 47.27%   | 91.11%             | -30.57% |     0.66 |       62 | 29.95%     | ok               |
|          40 | 18.38%   | 91.11%             | -50.11% |     0.38 |       61 | 35.44%     | ok               |
|          45 | -6.85%   | 91.11%             | -52.01% |     0.11 |       67 | 32.45%     | ok               |
|          35 | -14.63%  | 91.11%             | -58.86% |     0.04 |       72 | 38.10%     | ok               |
|          30 | -30.19%  | 91.11%             | -58.36% |    -0.15 |       74 | 42.76%     | ok               |

## TXN Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -4.03%   | 42.31%             | -43.95% |     0.06 |       68 | 31.45%     | ok               |
|          35 | -18.93%  | 42.31%             | -42.08% |    -0.17 |       82 | 45.26%     | ok               |
|          20 | -24.70%  | 42.31%             | -37.19% |    -0.21 |       72 | 55.07%     | ok               |
|          15 | -26.42%  | 42.31%             | -38.02% |    -0.23 |       77 | 59.40%     | ok               |
|          40 | -23.89%  | 42.31%             | -44.52% |    -0.27 |       76 | 42.76%     | ok               |

## UNH Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 38.75%   | -19.43%            | -26.31% |     0.61 |       73 | 49.08%     | ok               |
|          35 | 34.53%   | -19.43%            | -27.21% |     0.57 |       68 | 44.09%     | ok               |
|          50 | 31.88%   | -19.43%            | -36.71% |     0.56 |       52 | 29.95%     | ok               |
|          20 | 29.32%   | -19.43%            | -28.00% |     0.5  |       77 | 57.74%     | ok               |
|          15 | 29.29%   | -19.43%            | -27.12% |     0.5  |       82 | 63.89%     | ok               |

## UNI-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 80.67%   | 13.82%             | -22.21% |     0.87 |       46 | 25.48%     | ok               |
|          45 | 64.28%   | 13.82%             | -30.17% |     0.74 |       52 | 32.57%     | ok               |
|          40 | 48.20%   | 13.82%             | -43.84% |     0.63 |       60 | 38.70%     | ok               |
|          35 | 36.05%   | 13.82%             | -48.64% |     0.54 |       64 | 43.87%     | ok               |
|          20 | -22.17%  | 13.82%             | -68.99% |     0.1  |       88 | 58.24%     | ok               |

## UPS Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -31.40%  | -20.28%            | -36.91% |    -0.54 |       84 | 49.75%     | ok               |
|          40 | -28.95%  | -20.28%            | -31.45% |    -0.54 |       60 | 31.95%     | ok               |
|          35 | -30.68%  | -20.28%            | -32.39% |    -0.58 |       66 | 36.11%     | ok               |
|          15 | -33.82%  | -20.28%            | -39.14% |    -0.59 |       86 | 53.58%     | ok               |
|          25 | -33.26%  | -20.28%            | -38.17% |    -0.6  |       76 | 46.26%     | ok               |

## USO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 6.14%    | 90.78%             | -38.44% |     0.24 |       63 | 41.60%     | ok               |
|          20 | 3.62%    | 90.78%             | -40.84% |     0.2  |       70 | 38.27%     | ok               |
|          45 | 3.90%    | 90.78%             | -34.01% |     0.19 |       50 | 26.96%     | ok               |
|          25 | -5.70%   | 90.78%             | -42.99% |     0.07 |       66 | 36.11%     | ok               |
|          50 | -5.15%   | 90.78%             | -30.14% |     0.04 |       54 | 25.29%     | ok               |

## VEA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 3.75%    | 36.67%             | -15.99% |     0.19 |       56 | 50.25%     | ok               |
|          20 | -0.56%   | 36.67%             | -17.04% |     0.03 |       59 | 47.59%     | ok               |
|          25 | -4.35%   | 36.67%             | -17.13% |    -0.12 |       57 | 45.59%     | ok               |
|          30 | -5.22%   | 36.67%             | -17.27% |    -0.17 |       62 | 41.93%     | ok               |
|          35 | -5.68%   | 36.67%             | -16.11% |    -0.19 |       50 | 39.60%     | ok               |

## VIXY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -54.55%  | -52.55%            | -69.78% |    -0.63 |       34 | 8.65%      | ok               |
|          45 | -64.29%  | -52.55%            | -75.03% |    -0.84 |       54 | 13.64%     | ok               |
|          40 | -73.26%  | -52.55%            | -81.61% |    -1.01 |       70 | 17.80%     | ok               |
|          35 | -76.76%  | -52.55%            | -84.77% |    -1.05 |       94 | 24.29%     | ok               |
|          30 | -81.63%  | -52.55%            | -89.87% |    -1.07 |       96 | 31.45%     | ok               |

## VNQ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -7.36%   | 14.41%             | -22.34% |    -0.24 |       70 | 42.76%     | ok               |
|          45 | -7.47%   | 14.41%             | -19.07% |    -0.31 |       60 | 28.12%     | ok               |
|          50 | -8.39%   | 14.41%             | -17.13% |    -0.37 |       52 | 24.79%     | ok               |
|          30 | -11.10%  | 14.41%             | -24.92% |    -0.41 |       71 | 39.93%     | ok               |
|          20 | -12.09%  | 14.41%             | -24.00% |    -0.43 |       75 | 45.42%     | ok               |

## VTI Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 5.77%    | 34.69%             | -13.96% |     0.25 |       63 | 51.75%     | ok               |
|          15 | 1.03%    | 34.69%             | -15.70% |     0.1  |       62 | 54.24%     | ok               |
|          25 | -4.73%   | 34.69%             | -15.00% |    -0.1  |       57 | 49.75%     | ok               |
|          40 | -8.92%   | 34.69%             | -19.77% |    -0.3  |       70 | 40.10%     | ok               |
|          35 | -10.91%  | 34.69%             | -20.22% |    -0.37 |       64 | 44.43%     | ok               |

## VWO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -5.12%   | 25.66%             | -21.18% |    -0.15 |       56 | 29.78%     | ok               |
|          15 | -8.18%   | 25.66%             | -24.01% |    -0.22 |       72 | 46.59%     | ok               |
|          45 | -6.97%   | 25.66%             | -23.26% |    -0.23 |       58 | 32.28%     | ok               |
|          20 | -8.20%   | 25.66%             | -26.14% |    -0.23 |       67 | 44.59%     | ok               |
|          40 | -8.04%   | 25.66%             | -23.57% |    -0.26 |       68 | 34.94%     | ok               |

## VZ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -2.64%   | 15.79%             | -12.55% |    -0.02 |       56 | 28.45%     | ok               |
|          20 | -23.40%  | 15.79%             | -35.02% |    -0.46 |       80 | 53.08%     | ok               |
|          25 | -20.27%  | 15.79%             | -26.32% |    -0.51 |       83 | 48.09%     | ok               |
|          45 | -18.61%  | 15.79%             | -26.23% |    -0.57 |       72 | 32.95%     | ok               |
|          35 | -20.48%  | 15.79%             | -26.97% |    -0.61 |       65 | 39.27%     | ok               |

## WFC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | -10.04%  | 44.13%             | -22.54% |    -0.15 |       79 | 43.09%     | ok               |
|          50 | -8.46%   | 44.13%             | -18.29% |    -0.21 |       58 | 32.28%     | ok               |
|          45 | -14.77%  | 44.13%             | -24.02% |    -0.38 |       66 | 36.61%     | ok               |
|          20 | -23.40%  | 44.13%             | -29.96% |    -0.38 |       82 | 53.08%     | ok               |
|          30 | -21.60%  | 44.13%             | -29.91% |    -0.39 |       86 | 46.59%     | ok               |

## WIF-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 47.41%   | -81.07%            | -40.67% |     0.6  |       67 | 48.66%     | ok               |
|          25 | 25.73%   | -81.07%            | -44.74% |     0.47 |       63 | 44.64%     | ok               |
|          15 | 15.20%   | -81.07%            | -46.21% |     0.4  |       77 | 51.92%     | ok               |
|          30 | -1.06%   | -81.07%            | -48.32% |     0.26 |       64 | 41.95%     | ok               |
|          35 | -5.75%   | -81.07%            | -52.54% |     0.17 |       60 | 36.02%     | ok               |

## WMT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 38.84%   | 86.18%             | -12.87% |     1.11 |       38 | 36.61%     | ok               |
|          45 | 37.68%   | 86.18%             | -14.82% |     1.04 |       44 | 38.94%     | ok               |
|          35 | 27.63%   | 86.18%             | -18.90% |     0.77 |       60 | 45.26%     | ok               |
|          40 | 25.99%   | 86.18%             | -19.17% |     0.75 |       52 | 40.60%     | ok               |
|          15 | 8.90%    | 86.18%             | -26.82% |     0.28 |       84 | 59.23%     | ok               |

## XBI Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 13.75%   | 68.02%             | -16.08% |     0.41 |       50 | 33.44%     | ok               |
|          45 | 9.43%    | 68.02%             | -15.46% |     0.32 |       48 | 30.95%     | ok               |
|          35 | 2.78%    | 68.02%             | -17.66% |     0.15 |       58 | 36.27%     | ok               |
|          30 | 0.63%    | 68.02%             | -17.66% |     0.1  |       60 | 37.77%     | ok               |
|          50 | 0.20%    | 68.02%             | -15.41% |     0.08 |       48 | 27.95%     | ok               |

## XLB Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 0.38%    | 15.91%             | -15.73% |     0.07 |       40 | 24.13%     | ok               |
|          40 | 0.07%    | 15.91%             | -17.29% |     0.06 |       54 | 28.45%     | ok               |
|          45 | -2.62%   | 15.91%             | -17.09% |    -0.05 |       42 | 25.96%     | ok               |
|          35 | -3.60%   | 15.91%             | -20.65% |    -0.08 |       54 | 31.61%     | ok               |
|          25 | -7.05%   | 15.91%             | -21.62% |    -0.19 |       62 | 37.60%     | ok               |

## XLC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 8.81%    | 23.97%             | -12.33% |     0.35 |       61 | 49.58%     | ok               |
|          25 | 8.28%    | 23.97%             | -12.31% |     0.33 |       60 | 51.75%     | ok               |
|          50 | 3.60%    | 23.97%             | -12.48% |     0.21 |       64 | 37.77%     | ok               |
|          40 | 4.16%    | 23.97%             | -13.38% |     0.21 |       62 | 43.26%     | ok               |
|          20 | 4.01%    | 23.97%             | -14.06% |     0.19 |       65 | 54.08%     | ok               |

## XLE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 1.53%    | 39.62%             | -28.77% |     0.12 |       69 | 47.25%     | ok               |
|          50 | -0.76%   | 39.62%             | -25.98% |     0.06 |       58 | 38.60%     | ok               |
|          35 | -2.44%   | 39.62%             | -26.44% |     0.03 |       65 | 44.93%     | ok               |
|          45 | -2.15%   | 39.62%             | -28.46% |     0.02 |       60 | 40.93%     | ok               |
|          25 | -3.25%   | 39.62%             | -31.78% |     0.02 |       79 | 50.42%     | ok               |

## XLF Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 4.61%    | 39.38%             | -20.19% |     0.21 |       70 | 56.24%     | ok               |
|          20 | 3.96%    | 39.38%             | -18.63% |     0.19 |       70 | 53.58%     | ok               |
|          25 | -3.29%   | 39.38%             | -23.22% |    -0.05 |       77 | 50.42%     | ok               |
|          30 | -3.92%   | 39.38%             | -23.61% |    -0.07 |       78 | 48.42%     | ok               |
|          35 | -11.79%  | 39.38%             | -24.48% |    -0.4  |       70 | 44.93%     | ok               |

## XLI Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 4.98%    | 32.80%             | -11.40% |     0.23 |       85 | 51.25%     | ok               |
|          20 | 0.03%    | 32.80%             | -12.74% |     0.06 |       77 | 46.59%     | ok               |
|          50 | -4.76%   | 32.80%             | -14.94% |    -0.18 |       60 | 31.78%     | ok               |
|          45 | -5.38%   | 32.80%             | -16.29% |    -0.19 |       70 | 34.28%     | ok               |
|          25 | -10.03%  | 32.80%             | -18.74% |    -0.34 |       80 | 44.59%     | ok               |

## XLK Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | 45.64%   | 42.56%             | -14.75% |     0.91 |       42 | 45.26%     | ok               |
|          20 | 45.98%   | 42.56%             | -14.75% |     0.88 |       52 | 47.59%     | ok               |
|          15 | 48.18%   | 42.56%             | -17.54% |     0.88 |       53 | 50.25%     | ok               |
|          30 | 36.92%   | 42.56%             | -14.75% |     0.79 |       42 | 43.93%     | ok               |
|          35 | 23.09%   | 42.56%             | -15.98% |     0.57 |       56 | 41.26%     | ok               |

## XLM-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | 12.17%   | -44.63%            | -49.16% |     0.34 |       75 | 51.34%     | ok               |
|          40 | 8.69%    | -44.63%            | -49.47% |     0.3  |       54 | 36.21%     | ok               |
|          30 | 6.21%    | -44.63%            | -54.58% |     0.28 |       73 | 48.66%     | ok               |
|          50 | 6.75%    | -44.63%            | -48.14% |     0.26 |       40 | 24.52%     | ok               |
|          15 | -1.67%   | -44.63%            | -61.51% |     0.23 |       78 | 60.34%     | ok               |

## XLP Threshold Sweep

|   threshold | return   | benchmark_return   | mdd    |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:-------|---------:|---------:|:-----------|:-----------------|
|          45 | 19.92%   | 15.96%             | -5.66% |     1    |       48 | 31.61%     | ok               |
|          50 | 17.09%   | 15.96%             | -6.08% |     0.89 |       54 | 29.78%     | ok               |
|          40 | 17.68%   | 15.96%             | -7.32% |     0.88 |       66 | 35.11%     | ok               |
|          35 | 16.66%   | 15.96%             | -8.39% |     0.82 |       62 | 38.10%     | ok               |
|          30 | 13.28%   | 15.96%             | -8.96% |     0.66 |       63 | 39.93%     | ok               |

## XLU Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 5.77%    | 24.71%             | -14.03% |     0.32 |       54 | 29.45%     | ok               |
|          45 | 4.61%    | 24.71%             | -14.97% |     0.27 |       58 | 30.62%     | ok               |
|          35 | 2.92%    | 24.71%             | -19.71% |     0.18 |       64 | 36.44%     | ok               |
|          40 | 0.52%    | 24.71%             | -16.41% |     0.07 |       68 | 33.11%     | ok               |
|          30 | -1.54%   | 24.71%             | -20.40% |    -0.02 |       69 | 39.93%     | ok               |

## XLV Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -19.03%  | 26.81%             | -22.46% |    -0.84 |       74 | 38.27%     | ok               |
|          30 | -19.40%  | 26.81%             | -22.82% |    -0.87 |       74 | 36.61%     | ok               |
|          15 | -21.76%  | 26.81%             | -24.77% |    -0.95 |       81 | 42.26%     | ok               |
|          20 | -21.60%  | 26.81%             | -24.61% |    -0.96 |       77 | 39.77%     | ok               |
|          35 | -23.41%  | 26.81%             | -26.64% |    -1.14 |       68 | 33.61%     | ok               |

## XLY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -1.37%   | 29.59%             | -16.52% |     0.04 |       78 | 54.41%     | ok               |
|          30 | -4.80%   | 29.59%             | -18.44% |    -0.07 |       77 | 47.75%     | ok               |
|          20 | -6.59%   | 29.59%             | -20.14% |    -0.11 |       74 | 51.08%     | ok               |
|          25 | -8.67%   | 29.59%             | -21.01% |    -0.18 |       71 | 49.58%     | ok               |
|          50 | -7.87%   | 29.59%             | -17.00% |    -0.26 |       66 | 32.45%     | ok               |

## XOM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 3.48%    | 53.07%             | -21.35% |     0.17 |       40 | 29.28%     | ok               |
|          25 | 3.49%    | 53.07%             | -19.90% |     0.17 |       55 | 36.94%     | ok               |
|          30 | 2.46%    | 53.07%             | -20.29% |     0.14 |       55 | 36.27%     | ok               |
|          45 | -1.68%   | 53.07%             | -23.33% |     0.03 |       44 | 30.45%     | ok               |
|          40 | -3.14%   | 53.07%             | -21.45% |    -0.01 |       54 | 33.78%     | ok               |

## XRP-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 11.31%   | -49.33%            | -33.31% |     0.33 |       80 | 43.10%     | ok               |
|          40 | -1.22%   | -49.33%            | -33.91% |     0.17 |       70 | 35.06%     | ok               |
|          30 | -10.43%  | -49.33%            | -33.97% |     0.07 |       73 | 49.04%     | ok               |
|          45 | -8.23%   | -49.33%            | -36.27% |     0.07 |       62 | 28.93%     | ok               |
|          20 | -16.72%  | -49.33%            | -36.83% |     0    |       79 | 55.94%     | ok               |

## YFI-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -44.06%  | -61.57%            | -44.76% |    -0.71 |       60 | 28.16%     | ok               |
|          35 | -48.19%  | -61.57%            | -52.87% |    -0.74 |       62 | 36.21%     | ok               |
|          30 | -52.80%  | -61.57%            | -58.28% |    -0.83 |       74 | 40.04%     | ok               |
|          25 | -55.53%  | -61.57%            | -60.71% |    -0.87 |       73 | 44.44%     | ok               |
|          15 | -64.59%  | -61.57%            | -67.95% |    -1.06 |       83 | 52.30%     | ok               |

## ZEC-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 225.39%  | 2429.48%           | -30.64% |     1.14 |       46 | 29.69%     | ok               |
|          35 | 162.09%  | 2429.48%           | -50.84% |     0.97 |       52 | 34.10%     | ok               |
|          50 | 137.27%  | 2429.48%           | -41.34% |     0.92 |       48 | 26.63%     | ok               |
|          40 | 143.13%  | 2429.48%           | -54.22% |     0.92 |       52 | 32.57%     | ok               |
|          30 | 126.43%  | 2429.48%           | -56.50% |     0.87 |       54 | 36.97%     | ok               |
