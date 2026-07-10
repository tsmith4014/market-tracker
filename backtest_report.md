# Market Tracker Backtest Report

_Generated: 2026-07-10T04:17:12+00:00_

## Data Sources

- Crypto: Kraken -> Coinbase -> CoinGecko OHLC -> CoinPaprika fallback chain.
- Stocks / ETFs / indices: Stooq -> Yahoo Finance fallback chain.
- Data rows are generated from real market APIs. Mock OHLCV rows are not generated.

## Data Freshness

- Rows: **92,483**
- Symbols: **161**
- Date range: **2024-02-14** to **2026-07-10**

## Latest Signals

| symbol     | date                |         close |   composite_score | signal   | data_source   |
|:-----------|:--------------------|--------------:|------------------:|:---------|:--------------|
| AAPL       | 2026-07-09 00:00:00 |   316.22      |          56.0833  | LONG     | Yahoo Finance |
| ABBV       | 2026-07-09 00:00:00 |   249.91      |          57.5833  | LONG     | Yahoo Finance |
| AMAT       | 2026-07-09 00:00:00 |   588.66      |          36.4167  | LONG     | Yahoo Finance |
| AMZN       | 2026-07-09 00:00:00 |   247.04      |          67.9167  | LONG     | Yahoo Finance |
| ARB-USD    | 2026-07-10 00:00:00 |     0.0914    |          47.5833  | LONG     | Kraken API    |
| ARKK       | 2026-07-09 00:00:00 |    81.53      |          54.9167  | LONG     | Yahoo Finance |
| AVGO       | 2026-07-09 00:00:00 |   401.11      |          46.1667  | LONG     | Yahoo Finance |
| BAC        | 2026-07-09 00:00:00 |    59.25      |          51.5833  | LONG     | Yahoo Finance |
| C          | 2026-07-09 00:00:00 |   139.57      |          36.9167  | LONG     | Yahoo Finance |
| CL         | 2026-07-09 00:00:00 |    91.01      |          48.25    | LONG     | Yahoo Finance |
| CSCO       | 2026-07-09 00:00:00 |   118.31      |          38.0833  | LONG     | Yahoo Finance |
| DE         | 2026-07-09 00:00:00 |   592.9       |          39.5833  | LONG     | Yahoo Finance |
| GE         | 2026-07-09 00:00:00 |   359.04      |          32.5833  | LONG     | Yahoo Finance |
| IBM        | 2026-07-09 00:00:00 |   295.3       |          62.5833  | LONG     | Yahoo Finance |
| JNJ        | 2026-07-09 00:00:00 |   259.1       |          74.4167  | LONG     | Yahoo Finance |
| JPM        | 2026-07-09 00:00:00 |   335.47      |          36.5833  | LONG     | Yahoo Finance |
| LDO-USD    | 2026-07-10 00:00:00 |     0.309     |          47       | LONG     | Kraken API    |
| LIN        | 2026-07-09 00:00:00 |   525.56      |          69.9167  | LONG     | Yahoo Finance |
| LTC-USD    | 2026-07-10 00:00:00 |    44.37      |          30.1667  | LONG     | Kraken API    |
| NOW        | 2026-07-09 00:00:00 |   108.84      |          39.8333  | LONG     | Yahoo Finance |
| NVDA       | 2026-07-09 00:00:00 |   202.78      |          21       | LONG     | Yahoo Finance |
| OXY        | 2026-07-09 00:00:00 |    52.3       |          44       | LONG     | Yahoo Finance |
| RTX        | 2026-07-09 00:00:00 |   195.2       |          56.4167  | LONG     | Yahoo Finance |
| SBUX       | 2026-07-09 00:00:00 |   106.41      |          72.9167  | LONG     | Yahoo Finance |
| SCHW       | 2026-07-09 00:00:00 |   101.91      |          58.0833  | LONG     | Yahoo Finance |
| SOL-USD    | 2026-07-10 00:00:00 |    78.99      |          51.1667  | LONG     | Kraken API    |
| SPY        | 2026-07-09 00:00:00 |   751.71      |          53.0833  | LONG     | Yahoo Finance |
| TGT        | 2026-07-09 00:00:00 |   132.27      |          55.5833  | LONG     | Yahoo Finance |
| TMO        | 2026-07-09 00:00:00 |   524.71      |          66       | LONG     | Yahoo Finance |
| UNH        | 2026-07-09 00:00:00 |   431.68      |          74.5833  | LONG     | Yahoo Finance |
| UNI-USD    | 2026-07-10 00:00:00 |     3.458     |          47       | LONG     | Kraken API    |
| VTI        | 2026-07-09 00:00:00 |   371.45      |          56.5833  | LONG     | Yahoo Finance |
| WFC        | 2026-07-09 00:00:00 |    86.91      |          55.3333  | LONG     | Yahoo Finance |
| XBI        | 2026-07-09 00:00:00 |   164.28      |          73.25    | LONG     | Yahoo Finance |
| XLE        | 2026-07-09 00:00:00 |    54.82      |          52.6667  | LONG     | Yahoo Finance |
| XLF        | 2026-07-09 00:00:00 |    55.54      |          62.5833  | LONG     | Yahoo Finance |
| XLI        | 2026-07-09 00:00:00 |   181.11      |          60.5833  | LONG     | Yahoo Finance |
| XLU        | 2026-07-09 00:00:00 |    45.13      |          47       | LONG     | Yahoo Finance |
| XLV        | 2026-07-09 00:00:00 |   162.17      |          61.75    | LONG     | Yahoo Finance |
| YFI-USD    | 2026-07-10 00:00:00 |  2145.8       |          42.9167  | LONG     | Kraken API    |
| ZEC-USD    | 2026-07-10 00:00:00 |   490.95      |          72.0833  | LONG     | Kraken API    |
| AAVE-USD   | 2026-07-10 00:00:00 |    93.51      |          28       | NEUTRAL  | Kraken API    |
| ADA-USD    | 2026-07-10 00:00:00 |     0.167638  |           7.66667 | NEUTRAL  | Kraken API    |
| ADBE       | 2026-07-09 00:00:00 |   222.65      |           1.08333 | NEUTRAL  | Yahoo Finance |
| AGG        | 2026-07-09 00:00:00 |    98.18      |         -56.3333  | NEUTRAL  | Yahoo Finance |
| ALGO-USD   | 2026-07-10 00:00:00 |     0.08468   |         -21.5833  | NEUTRAL  | Kraken API    |
| AMD        | 2026-07-09 00:00:00 |   546.72      |          37.3333  | NEUTRAL  | Yahoo Finance |
| AMGN       | 2026-07-09 00:00:00 |   363.62      |          51.8333  | NEUTRAL  | Yahoo Finance |
| APT-USD    | 2026-07-10 00:00:00 |     0.6338    |           9.41667 | NEUTRAL  | Kraken API    |
| ATOM-USD   | 2026-07-10 00:00:00 |     1.5659    |         -15       | NEUTRAL  | Kraken API    |
| AVAX-USD   | 2026-07-10 00:00:00 |     6.792     |          19       | NEUTRAL  | Kraken API    |
| BA         | 2026-07-09 00:00:00 |   223.11      |          33.25    | NEUTRAL  | Yahoo Finance |
| BCH-USD    | 2026-07-10 00:00:00 |   242.09      |          13.5     | NEUTRAL  | Kraken API    |
| BITO       | 2026-07-09 00:00:00 |     8.57      |         -27.25    | NEUTRAL  | Yahoo Finance |
| BLK        | 2026-07-09 00:00:00 |  1019.68      |         -30.75    | NEUTRAL  | Yahoo Finance |
| BND        | 2026-07-09 00:00:00 |    72.83      |         -56.3333  | NEUTRAL  | Yahoo Finance |
| BONK-USD   | 2026-07-10 00:00:00 |     4.018e-06 |         -32.75    | NEUTRAL  | Kraken API    |
| BTC-USD    | 2026-07-10 00:00:00 | 63949.9       |          21.1667  | NEUTRAL  | Kraken API    |
| CAT        | 2026-07-09 00:00:00 |   938.39      |           5.41667 | NEUTRAL  | Yahoo Finance |
| CMCSA      | 2026-07-09 00:00:00 |    23.35      |           7.91667 | NEUTRAL  | Yahoo Finance |
| COMP-USD   | 2026-07-10 00:00:00 |    17.09      |          29.6667  | NEUTRAL  | Kraken API    |
| COP        | 2026-07-09 00:00:00 |   108.02      |         -12       | NEUTRAL  | Yahoo Finance |
| COST       | 2026-07-09 00:00:00 |   912.97      |         -56.0833  | NEUTRAL  | Yahoo Finance |
| CRM        | 2026-07-09 00:00:00 |   162.5       |         -16.0833  | NEUTRAL  | Yahoo Finance |
| CRV-USD    | 2026-07-10 00:00:00 |     0.20541   |           9.66667 | NEUTRAL  | Kraken API    |
| CVX        | 2026-07-09 00:00:00 |   174.05      |         -21       | NEUTRAL  | Yahoo Finance |
| DASH-USD   | 2026-07-10 00:00:00 |    34.805     |         -28.0833  | NEUTRAL  | Kraken API    |
| DBC        | 2026-07-09 00:00:00 |    27.58      |          26.25    | NEUTRAL  | Yahoo Finance |
| DIA        | 2026-07-09 00:00:00 |   524.19      |          40.8333  | NEUTRAL  | Yahoo Finance |
| DIS        | 2026-07-09 00:00:00 |    96.17      |         -66.1667  | NEUTRAL  | Yahoo Finance |
| DOGE-USD   | 2026-07-10 00:00:00 |     0.0740763 |         -14.5     | NEUTRAL  | Kraken API    |
| DOT-USD    | 2026-07-10 00:00:00 |     0.8458    |          -7       | NEUTRAL  | Kraken API    |
| DXY-INDEX  | 2026-07-10 00:00:00 |   100.711     |          24.4624  | NEUTRAL  | Yahoo Finance |
| EEM        | 2026-07-09 00:00:00 |    66.78      |          -6.33333 | NEUTRAL  | Yahoo Finance |
| EFA        | 2026-07-09 00:00:00 |   103.92      |          40.1667  | NEUTRAL  | Yahoo Finance |
| EOG        | 2026-07-09 00:00:00 |   133.54      |          27.25    | NEUTRAL  | Yahoo Finance |
| ETC-USD    | 2026-07-10 00:00:00 |     7.053     |         -22.25    | NEUTRAL  | Kraken API    |
| ETH-USD    | 2026-07-10 00:00:00 |  1776.02      |          34.75    | NEUTRAL  | Kraken API    |
| EWJ        | 2026-07-09 00:00:00 |    93.52      |          22.1667  | NEUTRAL  | Yahoo Finance |
| FCX        | 2026-07-09 00:00:00 |    60.53      |         -16.4167  | NEUTRAL  | Yahoo Finance |
| FIL-USD    | 2026-07-10 00:00:00 |     0.788     |          20.6667  | NEUTRAL  | Kraken API    |
| FXI        | 2026-07-09 00:00:00 |    33.41      |          -9.75    | NEUTRAL  | Yahoo Finance |
| GDX        | 2026-07-09 00:00:00 |    75.78      |         -47       | NEUTRAL  | Yahoo Finance |
| GDXJ       | 2026-07-09 00:00:00 |    99         |         -47       | NEUTRAL  | Yahoo Finance |
| GOOGL      | 2026-07-09 00:00:00 |   358.89      |         -15.6667  | NEUTRAL  | Yahoo Finance |
| GRT-USD    | 2026-07-10 00:00:00 |     0.01769   |         -18.25    | NEUTRAL  | Kraken API    |
| GS         | 2026-07-09 00:00:00 |  1055.97      |          27.3333  | NEUTRAL  | Yahoo Finance |
| HBAR-USD   | 2026-07-10 00:00:00 |     0.0706    |         -15       | NEUTRAL  | Kraken API    |
| HD         | 2026-07-09 00:00:00 |   338.73      |          17.8333  | NEUTRAL  | Yahoo Finance |
| HON        | 2026-07-09 00:00:00 |   223.42      |         -40.25    | NEUTRAL  | Yahoo Finance |
| HYG        | 2026-07-09 00:00:00 |    79.75      |         -42.5833  | NEUTRAL  | Yahoo Finance |
| IBIT       | 2026-07-09 00:00:00 |    35.81      |         -27.25    | NEUTRAL  | Yahoo Finance |
| ICP-USD    | 2026-07-10 00:00:00 |     2.319     |          20.6667  | NEUTRAL  | Kraken API    |
| IEF        | 2026-07-09 00:00:00 |    93.71      |         -53       | NEUTRAL  | Yahoo Finance |
| IEMG       | 2026-07-09 00:00:00 |    81.02      |          -6.33333 | NEUTRAL  | Yahoo Finance |
| INJ-USD    | 2026-07-10 00:00:00 |     4.856     |           9.5     | NEUTRAL  | Kraken API    |
| INTC       | 2026-07-09 00:00:00 |   112.54      |          -9.33333 | NEUTRAL  | Yahoo Finance |
| INTU       | 2026-07-09 00:00:00 |   273.38      |         -23.0833  | NEUTRAL  | Yahoo Finance |
| ITA        | 2026-07-09 00:00:00 |   239.62      |          21.9167  | NEUTRAL  | Yahoo Finance |
| IWM        | 2026-07-09 00:00:00 |   297.24      |          33.8333  | NEUTRAL  | Yahoo Finance |
| KO         | 2026-07-09 00:00:00 |    82.63      |          60.3333  | NEUTRAL  | Yahoo Finance |
| LINK-USD   | 2026-07-10 00:00:00 |     7.90842   |          18.9167  | NEUTRAL  | Kraken API    |
| LLY        | 2026-07-09 00:00:00 |  1216.95      |          51.8333  | NEUTRAL  | Yahoo Finance |
| LRCX       | 2026-07-09 00:00:00 |   353.17      |          12.5833  | NEUTRAL  | Yahoo Finance |
| MCD        | 2026-07-09 00:00:00 |   276.49      |         -49.5     | NEUTRAL  | Yahoo Finance |
| META       | 2026-07-09 00:00:00 |   631.48      |          45.3333  | NEUTRAL  | Yahoo Finance |
| MPC        | 2026-07-09 00:00:00 |   283.3       |          59.5     | NEUTRAL  | Yahoo Finance |
| MRK        | 2026-07-09 00:00:00 |   125.07      |          63.6667  | NEUTRAL  | Yahoo Finance |
| MS         | 2026-07-09 00:00:00 |   222.13      |          29.1667  | NEUTRAL  | Yahoo Finance |
| MSFT       | 2026-07-09 00:00:00 |   384.36      |         -21.0833  | NEUTRAL  | Yahoo Finance |
| MU         | 2026-07-09 00:00:00 |   991.64      |           1.33333 | NEUTRAL  | Yahoo Finance |
| NEAR-USD   | 2026-07-10 00:00:00 |     1.9417    |          20.1667  | NEUTRAL  | Kraken API    |
| NEM        | 2026-07-09 00:00:00 |    94.81      |         -47.5     | NEUTRAL  | Yahoo Finance |
| NKE        | 2026-07-09 00:00:00 |    42.78      |         -44.1667  | NEUTRAL  | Yahoo Finance |
| OP-USD     | 2026-07-10 00:00:00 |     0.1058    |          11.9167  | NEUTRAL  | Kraken API    |
| PEP        | 2026-07-09 00:00:00 |   137.86      |         -48.4167  | NEUTRAL  | Yahoo Finance |
| PEPE-USD   | 2026-07-10 00:00:00 |     2.667e-06 |          26.1667  | NEUTRAL  | Kraken API    |
| PG         | 2026-07-09 00:00:00 |   146.85      |         -27.0833  | NEUTRAL  | Yahoo Finance |
| PM         | 2026-07-09 00:00:00 |   181.17      |          29.6667  | NEUTRAL  | Yahoo Finance |
| POL-USD    | 2026-07-10 00:00:00 |     0.07765   |          17.8333  | NEUTRAL  | Kraken API    |
| QCOM       | 2026-07-09 00:00:00 |   191.11      |         -24.5833  | NEUTRAL  | Yahoo Finance |
| QQQ        | 2026-07-09 00:00:00 |   723.28      |          31.8333  | NEUTRAL  | Yahoo Finance |
| RENDER-USD | 2026-07-10 00:00:00 |     1.566     |          -7.5     | NEUTRAL  | Kraken API    |
| SHIB-USD   | 2026-07-10 00:00:00 |     4.355e-06 |           3.16667 | NEUTRAL  | Kraken API    |
| SHY        | 2026-07-09 00:00:00 |    81.91      |         -44.0833  | NEUTRAL  | Yahoo Finance |
| SKY-USD    | 2026-07-10 00:00:00 |     0.05711   |          -1.58333 | NEUTRAL  | Kraken API    |
| SLB        | 2026-07-09 00:00:00 |    47.24      |         -25.8333  | NEUTRAL  | Yahoo Finance |
| SMH        | 2026-07-09 00:00:00 |   607.73      |          -1.66667 | NEUTRAL  | Yahoo Finance |
| SNX-USD    | 2026-07-10 00:00:00 |     0.2215    |         -18.0833  | NEUTRAL  | Kraken API    |
| SOXX       | 2026-07-09 00:00:00 |   581.7       |          -1.66667 | NEUTRAL  | Yahoo Finance |
| SUSHI-USD  | 2026-07-10 00:00:00 |     0.1642    |          17.8333  | NEUTRAL  | Kraken API    |
| TIA-USD    | 2026-07-10 00:00:00 |     0.4189    |          41.5     | NEUTRAL  | Kraken API    |
| TMUS       | 2026-07-09 00:00:00 |   181.48      |         -15.75    | NEUTRAL  | Yahoo Finance |
| TRX-USD    | 2026-07-10 00:00:00 |     0.331126  |          66.8333  | NEUTRAL  | Kraken API    |
| TSLA       | 2026-07-09 00:00:00 |   406.55      |          38.75    | NEUTRAL  | Yahoo Finance |
| TXN        | 2026-07-09 00:00:00 |   308.53      |          29.3333  | NEUTRAL  | Yahoo Finance |
| UPS        | 2026-07-09 00:00:00 |   110.74      |          67.3333  | NEUTRAL  | Yahoo Finance |
| USO        | 2026-07-09 00:00:00 |   109.01      |          13       | NEUTRAL  | Yahoo Finance |
| VEA        | 2026-07-09 00:00:00 |    70.73      |           2.33333 | NEUTRAL  | Yahoo Finance |
| VIXY       | 2026-07-09 00:00:00 |    20.81      |         -40.5     | NEUTRAL  | Yahoo Finance |
| VNQ        | 2026-07-09 00:00:00 |    97.09      |          19.3333  | NEUTRAL  | Yahoo Finance |
| VWO        | 2026-07-09 00:00:00 |    59.49      |          -4.33333 | NEUTRAL  | Yahoo Finance |
| WIF-USD    | 2026-07-10 00:00:00 |     0.1594    |         -20.0833  | NEUTRAL  | Kraken API    |
| XLB        | 2026-07-09 00:00:00 |    50.26      |         -26.5     | NEUTRAL  | Yahoo Finance |
| XLC        | 2026-07-09 00:00:00 |   110.51      |          -1.08333 | NEUTRAL  | Yahoo Finance |
| XLK        | 2026-07-09 00:00:00 |   185.35      |          25.1667  | NEUTRAL  | Yahoo Finance |
| XLM-USD    | 2026-07-10 00:00:00 |     0.190813  |         -23.4167  | NEUTRAL  | Kraken API    |
| XLP        | 2026-07-09 00:00:00 |    83.2       |          -2.08333 | NEUTRAL  | Yahoo Finance |
| XLY        | 2026-07-09 00:00:00 |   116.85      |          39       | NEUTRAL  | Yahoo Finance |
| XOM        | 2026-07-09 00:00:00 |   137.46      |         -13.6667  | NEUTRAL  | Yahoo Finance |
| XRP-USD    | 2026-07-10 00:00:00 |     1.10715   |          12.1667  | NEUTRAL  | Kraken API    |
| FET-USD    | 2026-07-10 00:00:00 |     0.1624    |         -35.3333  | SHORT    | Kraken API    |
| GLD        | 2026-07-09 00:00:00 |   378.18      |         -30.4167  | SHORT    | Yahoo Finance |
| NFLX       | 2026-07-09 00:00:00 |    75.47      |         -33.25    | SHORT    | Yahoo Finance |
| ORCL       | 2026-07-09 00:00:00 |   144.22      |         -60.9167  | SHORT    | Yahoo Finance |
| PFE        | 2026-07-09 00:00:00 |    24.25      |         -54.0833  | SHORT    | Yahoo Finance |
| SLV        | 2026-07-09 00:00:00 |    54.14      |         -34.4167  | SHORT    | Yahoo Finance |
| T          | 2026-07-09 00:00:00 |    21.04      |         -52.75    | SHORT    | Yahoo Finance |
| TLT        | 2026-07-09 00:00:00 |    84.49      |         -47.25    | SHORT    | Yahoo Finance |
| VZ         | 2026-07-09 00:00:00 |    42.24      |         -42.5833  | SHORT    | Yahoo Finance |
| WMT        | 2026-07-09 00:00:00 |   112.21      |         -56.0833  | SHORT    | Yahoo Finance |

## Edge Summary

- Symbols with trades: **160** of 160
- Beat buy-and-hold: **31.87%** of traded symbols
- Positive return: **30.00%** of traded symbols
- Median strategy return: **-10.88%** (benchmark **16.26%**)
- Median excess vs benchmark: **-27.78%**
- Median Sharpe: **-0.14**
- Median exposure: **44.43%**

> Edge is real only if both _beat buy-and-hold_ and _median excess_ are convincingly positive across many symbols. Treat a single high-return symbol as noise.

## Portfolio Backtest

Actual capital-allocation books (not per-symbol averages). Benchmarks: `equal_weight_buyhold` (whole tracked universe), `spy_buyhold` (100% SPY), and `sixty_forty` (60% SPY / 40% AGG). `high_conf_voltarget` inverse-vol-weights the HIGH-confidence book; `conviction_long_short` is market-neutral. Judge on **Sharpe** and **max_drawdown** out-of-sample, not raw return: a fully-invested long book wins on return in a bull market but carries all the risk.

| strategy              | scope         | ann_return   | ann_vol   |   sharpe | max_drawdown   | total_return   |   avg_gross_exposure |
|:----------------------|:--------------|:-------------|:----------|---------:|:---------------|:---------------|---------------------:|
| equal_weight_buyhold  | full          | -2.83%       | 32.52%    |    -0.09 | -47.00%        | -22.00%        |                 1    |
| equal_weight_buyhold  | out_of_sample | -18.52%      | 31.25%    |    -0.59 | -39.63%        | -22.13%        |                 1    |
| all_signals_ew        | full          | -18.73%      | 27.22%    |    -0.69 | -63.69%        | -49.55%        |                 1    |
| all_signals_ew        | out_of_sample | 18.06%       | 26.77%    |     0.67 | -17.52%        | 16.78%         |                 1    |
| high_conf_ew          | full          | 3.01%        | 30.76%    |     0.1  | -40.60%        | -4.90%         |                 0.88 |
| high_conf_ew          | out_of_sample | 18.65%       | 33.74%    |     0.55 | -17.35%        | 15.05%         |                 0.88 |
| high_conf_voltarget   | full          | 5.65%        | 28.29%    |     0.2  | -34.62%        | 5.43%          |                 0.88 |
| high_conf_voltarget   | out_of_sample | 14.67%       | 31.31%    |     0.47 | -16.94%        | 11.19%         |                 0.88 |
| conviction_long_short | full          | -20.10%      | 22.98%    |    -0.87 | -50.95%        | -49.97%        |                 0.97 |
| conviction_long_short | out_of_sample | -12.91%      | 26.25%    |    -0.49 | -23.09%        | -16.04%        |                 0.97 |
| spy_buyhold           | full          | 6.40%        | 13.37%    |     0.48 | -18.27%        | 18.24%         |                 0.79 |
| spy_buyhold           | out_of_sample | -2.46%       | 9.80%     |    -0.25 | -13.27%        | -3.09%         |                 0.79 |
| sixty_forty           | full          | 3.79%        | 8.46%     |     0.45 | -10.80%        | 11.00%         |                 0.79 |
| sixty_forty           | out_of_sample | -2.88%       | 6.45%     |    -0.45 | -9.26%         | -3.25%         |                 0.79 |

## Walk-Forward Robustness

Each book measured across contiguous time folds (each a different regime). A book has durable edge only if `mean_sharpe` is positive, `min_sharpe` isn't deeply negative, and `pct_positive_folds` is high — a single great fold doesn't count. `fold_sharpes` lists each fold oldest-to-newest.

| strategy              |   n_folds |   mean_sharpe |   median_sharpe |   min_sharpe | pct_positive_folds   | mean_return   | fold_sharpes                  |
|:----------------------|----------:|--------------:|----------------:|-------------:|:---------------------|:--------------|:------------------------------|
| equal_weight_buyhold  |         5 |          0.26 |            0.38 |        -1.67 | 60.00%               | -1.42%        | 1.90;-1.67;1.53;-0.85;0.38    |
| all_signals_ew        |         5 |         -0.64 |           -0.36 |        -2.08 | 0.00%                | -11.88%       | -0.04;-0.36;-2.08;-0.15;-0.56 |
| high_conf_ew          |         5 |          0.28 |            0.33 |        -0.76 | 60.00%               | -0.32%        | 1.47;0.33;-0.76;0.52;-0.14    |
| high_conf_voltarget   |         5 |          0.53 |            0.47 |        -0.74 | 60.00%               | 1.75%         | 2.40;0.71;-0.74;0.47;-0.21    |
| conviction_long_short |         5 |         -1.06 |           -1.58 |        -1.69 | 20.00%               | -12.68%       | -1.65;-1.69;-0.48;0.10;-1.58  |
| spy_buyhold           |         5 |          0.37 |           -0.16 |        -1.05 | 40.00%               | 4.00%         | 1.79;-1.05;1.78;-0.51;-0.16   |
| sixty_forty           |         5 |          0.32 |           -0.45 |        -1.18 | 40.00%               | 2.38%         | 2.00;-1.18;1.79;-0.58;-0.45   |

## Strategy Comparison

Each decision rule backtested over the same data. `out_of_sample` is the most recent ~35% of each symbol's history (unseen tail). A rule has real edge only if `median_excess` and `beat_benchmark_pct` stay positive out-of-sample, not just full-sample.

| strategy        | scope         |   symbols | beat_benchmark_pct   | positive_pct   | median_return   | median_benchmark   | median_excess   |   median_sharpe |   total_trades |
|:----------------|:--------------|----------:|:---------------------|:---------------|:----------------|:-------------------|:----------------|----------------:|---------------:|
| trend           | full          |       160 | 31.87%               | 30.00%         | -10.88%         | 16.26%             | -27.78%         |           -0.14 |          11218 |
| trend           | out_of_sample |       160 | 42.50%               | 52.50%         | 0.94%           | 6.35%              | -5.08%          |            0.24 |           3823 |
| mean_reversion  | full          |       157 | 40.76%               | 50.96%         | 0.06%           | 15.99%             | -17.94%         |            0.04 |           1266 |
| mean_reversion  | out_of_sample |       126 | 49.21%               | 57.94%         | 0.33%           | -0.08%             | -1.90%          |            0.58 |            436 |
| regime_adaptive | full          |       160 | 32.50%               | 33.12%         | -11.46%         | 16.26%             | -28.07%         |           -0.13 |          11491 |
| regime_adaptive | out_of_sample |       160 | 41.88%               | 52.50%         | 1.33%           | 6.35%              | -5.47%          |            0.24 |           3923 |

## Signal Calibration

Realized forward return in the signal's direction, grouped by confidence. HIGH should outrank LOW for the confidence score to be meaningful.

| confidence_level   |   horizon |     n | mean_return   | median_return   | win_rate   |
|:-------------------|----------:|------:|:--------------|:----------------|:-----------|
| HIGH               |         5 |  7975 | 0.13%         | 0.12%           | 52.00%     |
| MEDIUM             |         5 | 29203 | 0.02%         | 0.08%           | 50.89%     |
| LOW                |         5 |  3317 | -0.64%        | -0.56%          | 44.44%     |
| ALL                |         5 | 40495 | -0.01%        | 0.05%           | 50.58%     |
| HIGH               |        10 |  7926 | 0.44%         | 0.13%           | 51.63%     |
| MEDIUM             |        10 | 29003 | 0.18%         | 0.14%           | 51.14%     |
| LOW                |        10 |  3277 | -0.93%        | -0.76%          | 45.07%     |
| ALL                |        10 | 40206 | 0.14%         | 0.09%           | 50.74%     |
| HIGH               |        20 |  7847 | 0.81%         | 0.38%           | 53.08%     |
| MEDIUM             |        20 | 28624 | 0.85%         | 0.63%           | 53.62%     |
| LOW                |        20 |  3244 | -0.65%        | -0.48%          | 47.32%     |
| ALL                |        20 | 39715 | 0.72%         | 0.50%           | 53.00%     |

## Backtest Summary

### Data Quality / Signal Availability

- **ok**: 160 symbols

| symbol     |   trades | return   | benchmark_return   | mdd     |   sharpe | exposure   | skipped_reason   |
|:-----------|---------:|:---------|:-------------------|:--------|---------:|:-----------|:-----------------|
| AAPL       |       65 | 13.21%   | 71.72%             | -20.65% |     0.36 | 48.92%     | ok               |
| AAVE-USD   |       74 | -49.43%  | -65.65%            | -68.26% |    -0.44 | 38.31%     | ok               |
| ABBV       |       66 | -19.43%  | 43.28%             | -30.55% |    -0.41 | 47.25%     | ok               |
| ADA-USD    |       88 | -83.94%  | -77.48%            | -89.69% |    -0.71 | 46.74%     | ok               |
| ADBE       |       66 | -29.52%  | -63.18%            | -35.76% |    -0.36 | 57.07%     | ok               |
| AGG        |       67 | -6.52%   | 1.03%              | -10.08% |    -1.09 | 30.78%     | ok               |
| ALGO-USD   |       86 | -50.43%  | -71.05%            | -53.13% |    -0.57 | 38.12%     | ok               |
| AMAT       |       69 | -31.21%  | 216.16%            | -57.21% |    -0.25 | 53.08%     | ok               |
| AMD        |       54 | 4.65%    | 205.94%            | -43.98% |     0.26 | 35.94%     | ok               |
| AMGN       |       69 | -15.41%  | 25.36%             | -34.14% |    -0.29 | 46.26%     | ok               |
| AMZN       |       80 | -36.33%  | 44.48%             | -42.48% |    -1.08 | 38.27%     | ok               |
| APT-USD    |       74 | -43.60%  | -89.58%            | -69.96% |    -0.27 | 41.95%     | ok               |
| ARB-USD    |       66 | -21.16%  | -80.80%            | -62.34% |    -0.01 | 37.74%     | ok               |
| ARKK       |       85 | -34.18%  | 61.45%             | -36.89% |    -0.6  | 40.27%     | ok               |
| ATOM-USD   |       90 | -68.72%  | -66.65%            | -74.00% |    -1.15 | 45.79%     | ok               |
| AVAX-USD   |       68 | -27.44%  | -74.38%            | -53.72% |    -0.17 | 38.31%     | ok               |
| AVGO       |       62 | 23.56%   | 217.78%            | -35.76% |     0.42 | 43.26%     | ok               |
| BA         |       67 | 7.60%    | 9.70%              | -30.56% |     0.25 | 49.25%     | ok               |
| BAC        |       78 | -10.45%  | 78.84%             | -27.64% |    -0.21 | 49.08%     | ok               |
| BCH-USD    |       76 | -3.77%   | -27.04%            | -53.87% |     0.17 | 49.43%     | ok               |
| BITO       |       80 | -1.17%   | -65.11%            | -42.82% |     0.17 | 42.26%     | ok               |
| BLK        |       77 | -11.24%  | 29.83%             | -24.29% |    -0.28 | 43.09%     | ok               |
| BND        |       65 | -7.32%   | 1.11%              | -9.89%  |    -1.18 | 32.28%     | ok               |
| BONK-USD   |       72 | 45.25%   | -78.13%            | -45.22% |     0.6  | 41.57%     | ok               |
| BTC-USD    |       72 | -0.33%   | -34.66%            | -23.38% |     0.14 | 52.30%     | ok               |
| C          |       79 | -24.66%  | 158.56%            | -37.02% |    -0.45 | 51.58%     | ok               |
| CAT        |       72 | 24.57%   | 196.29%            | -21.02% |     0.49 | 56.74%     | ok               |
| CL         |       62 | 10.88%   | 8.72%              | -14.32% |     0.4  | 46.26%     | ok               |
| CMCSA      |       77 | -38.38%  | -40.71%            | -39.80% |    -1    | 42.93%     | ok               |
| COMP-USD   |       89 | -46.23%  | -67.92%            | -59.17% |    -0.37 | 46.17%     | ok               |
| COP        |       72 | -25.89%  | -1.91%             | -43.96% |    -0.48 | 41.43%     | ok               |
| COST       |       60 | 0.46%    | 26.42%             | -29.73% |     0.08 | 44.43%     | ok               |
| CRM        |       65 | -39.47%  | -43.80%            | -41.36% |    -0.82 | 43.09%     | ok               |
| CRV-USD    |       66 | -10.49%  | -60.87%            | -39.89% |     0.12 | 36.02%     | ok               |
| CSCO       |       59 | 27.39%   | 135.30%            | -21.79% |     0.57 | 49.25%     | ok               |
| CVX        |       71 | -14.65%  | 15.26%             | -26.75% |    -0.36 | 41.26%     | ok               |
| DASH-USD   |       63 | -46.69%  | 35.34%             | -64.43% |    -0.08 | 31.03%     | ok               |
| DBC        |       60 | -13.70%  | 25.76%             | -25.70% |    -0.48 | 32.95%     | ok               |
| DE         |       72 | -7.57%   | 54.09%             | -25.24% |    -0.07 | 47.42%     | ok               |
| DIA        |       60 | -1.88%   | 36.40%             | -12.94% |    -0.06 | 44.59%     | ok               |
| DIS        |       66 | -24.17%  | -13.80%            | -28.17% |    -0.49 | 46.59%     | ok               |
| DOGE-USD   |       77 | -24.91%  | -71.90%            | -60.95% |    -0.01 | 50.57%     | ok               |
| DOT-USD    |       90 | -56.92%  | -82.17%            | -62.71% |    -0.58 | 48.08%     | ok               |
| DXY-INDEX  |       38 | -2.00%   | -0.90%             | -6.02%  |    -0.3  | 30.59%     | ok               |
| EEM        |       64 | -9.40%   | 68.21%             | -25.67% |    -0.25 | 43.43%     | ok               |
| EFA        |       62 | -9.68%   | 38.38%             | -15.14% |    -0.36 | 44.76%     | ok               |
| EOG        |       79 | -25.31%  | 20.30%             | -48.13% |    -0.55 | 46.42%     | ok               |
| ETC-USD    |       64 | -35.69%  | -65.97%            | -48.16% |    -0.51 | 31.23%     | ok               |
| ETH-USD    |       62 | 133.43%  | -35.07%            | -30.11% |     1.17 | 44.83%     | ok               |
| EWJ        |       62 | -18.16%  | 39.58%             | -30.73% |    -0.59 | 39.10%     | ok               |
| FCX        |       63 | -28.65%  | 62.72%             | -48.09% |    -0.33 | 45.09%     | ok               |
| FET-USD    |       79 | -35.78%  | -79.39%            | -48.80% |    -0.1  | 40.04%     | ok               |
| FIL-USD    |       70 | -47.29%  | -76.45%            | -50.88% |    -0.62 | 32.57%     | ok               |
| FXI        |       44 | -6.84%   | 47.38%             | -23.91% |    -0.09 | 30.12%     | ok               |
| GDX        |       60 | 11.28%   | 191.35%            | -34.99% |     0.3  | 48.09%     | ok               |
| GDXJ       |       68 | -23.13%  | 214.09%            | -44.93% |    -0.22 | 46.42%     | ok               |
| GE         |       74 | 16.65%   | 207.08%            | -27.82% |     0.38 | 53.74%     | ok               |
| GLD        |       48 | 25.16%   | 105.06%            | -16.63% |     0.64 | 46.92%     | ok               |
| GOOGL      |       59 | 79.31%   | 145.92%            | -20.41% |     1.18 | 53.08%     | ok               |
| GRT-USD    |       85 | -26.14%  | -87.39%            | -56.53% |    -0.13 | 41.19%     | ok               |
| GS         |       76 | -2.38%   | 179.33%            | -22.13% |     0.05 | 52.08%     | ok               |
| HD         |       73 | -8.53%   | -5.44%             | -18.58% |    -0.15 | 44.43%     | ok               |
| HON        |       94 | -29.10%  | 15.99%             | -31.48% |    -0.8  | 52.75%     | ok               |
| HYG        |       81 | -9.58%   | 3.75%              | -9.59%  |    -1.12 | 34.11%     | ok               |
| IBIT       |       34 | 30.86%   | -5.79%             | -18.95% |     0.67 | 32.47%     | ok               |
| IBM        |       78 | 6.57%    | 60.87%             | -27.54% |     0.23 | 49.75%     | ok               |
| ICP-USD    |       79 | -13.02%  | -67.07%            | -51.29% |     0.12 | 35.06%     | ok               |
| IEF        |       76 | -10.90%  | -0.19%             | -11.70% |    -1.54 | 32.78%     | ok               |
| IEMG       |       58 | -6.92%   | 62.14%             | -26.84% |    -0.17 | 43.43%     | ok               |
| INJ-USD    |       73 | -53.62%  | -66.23%            | -77.42% |    -0.52 | 37.16%     | ok               |
| INTC       |       70 | 55.82%   | 154.67%            | -60.60% |     0.62 | 49.25%     | ok               |
| INTU       |       69 | -20.94%  | -58.40%            | -43.77% |    -0.26 | 42.10%     | ok               |
| ITA        |       72 | -2.66%   | 91.21%             | -23.75% |    -0    | 48.42%     | ok               |
| IWM        |       48 | 9.40%    | 49.27%             | -12.83% |     0.39 | 35.77%     | ok               |
| JNJ        |       72 | 6.80%    | 66.37%             | -17.51% |     0.29 | 50.58%     | ok               |
| JPM        |       73 | -18.71%  | 90.58%             | -33.16% |    -0.44 | 53.74%     | ok               |
| KO         |       49 | 28.93%   | 39.37%             | -8.07%  |     1.03 | 37.77%     | ok               |
| LDO-USD    |       72 | 8.74%    | -81.97%            | -58.32% |     0.34 | 37.74%     | ok               |
| LIN        |       66 | -2.37%   | 25.61%             | -21.53% |    -0.02 | 39.10%     | ok               |
| LINK-USD   |       72 | -18.18%  | -60.50%            | -50.48% |     0.04 | 41.76%     | ok               |
| LLY        |       71 | -27.30%  | 60.69%             | -53.34% |    -0.38 | 50.42%     | ok               |
| LRCX       |       82 | -24.90%  | 285.68%            | -63.39% |    -0.14 | 45.42%     | ok               |
| LTC-USD    |       66 | -34.00%  | -56.19%            | -53.76% |    -0.29 | 48.47%     | ok               |
| MCD        |       75 | -2.55%   | -4.05%             | -18.81% |    -0.05 | 38.10%     | ok               |
| META       |       72 | -29.14%  | 33.43%             | -38.96% |    -0.5  | 48.42%     | ok               |
| MPC        |       71 | -15.39%  | 66.76%             | -44.76% |    -0.17 | 48.92%     | ok               |
| MRK        |       67 | -29.91%  | -0.60%             | -34.46% |    -0.72 | 44.43%     | ok               |
| MS         |       81 | -13.23%  | 164.44%            | -27.79% |    -0.24 | 50.25%     | ok               |
| MSFT       |       85 | -39.14%  | -6.14%             | -39.14% |    -1.05 | 47.75%     | ok               |
| MU         |       51 | 270.20%  | 1111.83%           | -68.76% |     1.34 | 59.90%     | ok               |
| NEAR-USD   |       81 | -0.20%   | -42.82%            | -60.10% |     0.25 | 40.23%     | ok               |
| NEM        |       72 | -31.13%  | 195.17%            | -38.49% |    -0.33 | 53.08%     | ok               |
| NFLX       |       64 | 27.13%   | 30.27%             | -21.09% |     0.6  | 54.58%     | ok               |
| NKE        |       91 | -48.19%  | -59.77%            | -57.25% |    -0.9  | 43.59%     | ok               |
| NOW        |       82 | 8.49%    | -31.29%            | -27.34% |     0.27 | 45.59%     | ok               |
| NVDA       |       75 | -26.94%  | 129.95%            | -45.02% |    -0.2  | 58.82%     | ok               |
| OP-USD     |       68 | -26.26%  | -90.51%            | -70.11% |    -0.06 | 33.91%     | ok               |
| ORCL       |       72 | 93.15%   | 26.22%             | -29.47% |     0.86 | 53.74%     | ok               |
| OXY        |       69 | -0.00%   | -8.73%             | -31.27% |     0.12 | 43.59%     | ok               |
| PEP        |       79 | -6.85%   | -17.71%            | -21.35% |    -0.14 | 48.75%     | ok               |
| PEPE-USD   |       79 | 0.11%    | -73.74%            | -57.66% |     0.28 | 44.83%     | ok               |
| PFE        |       77 | -39.63%  | -10.55%            | -40.87% |    -1.27 | 35.61%     | ok               |
| PG         |       68 | -17.14%  | -5.64%             | -24.55% |    -0.63 | 40.93%     | ok               |
| PM         |       83 | -4.93%   | 103.06%            | -33.68% |    -0.01 | 56.24%     | ok               |
| POL-USD    |       79 | 36.04%   | -75.25%            | -46.45% |     0.56 | 49.62%     | ok               |
| QCOM       |       73 | -15.25%  | 24.15%             | -56.59% |    -0.04 | 46.09%     | ok               |
| QQQ        |       64 | 17.66%   | 66.95%             | -12.88% |     0.52 | 44.59%     | ok               |
| RENDER-USD |       98 | -19.07%  | -62.36%            | -45.00% |     0.1  | 43.37%     | ok               |
| RTX        |       58 | 24.80%   | 113.59%            | -16.99% |     0.62 | 51.58%     | ok               |
| SBUX       |       62 | -18.32%  | 13.12%             | -27.45% |    -0.34 | 39.10%     | ok               |
| SCHW       |       76 | -13.88%  | 61.68%             | -31.92% |    -0.27 | 46.76%     | ok               |
| SHIB-USD   |       78 | -40.18%  | -72.40%            | -48.95% |    -0.37 | 52.49%     | ok               |
| SHY        |       48 | -2.24%   | 0.28%              | -2.85%  |    -0.79 | 34.28%     | ok               |
| SKY-USD    |       70 | -28.56%  | -1.25%             | -43.98% |    -0.34 | 40.40%     | ok               |
| SLB        |       77 | -24.74%  | -1.07%             | -54.13% |    -0.41 | 51.41%     | ok               |
| SLV        |       58 | 46.07%   | 164.87%            | -42.66% |     0.66 | 42.60%     | ok               |
| SMH        |       48 | 83.88%   | 198.93%            | -33.99% |     1.11 | 48.59%     | ok               |
| SNX-USD    |       58 | -13.40%  | -79.86%            | -34.76% |     0.1  | 37.36%     | ok               |
| SOL-USD    |       70 | -32.98%  | -61.78%            | -56.90% |    -0.09 | 59.20%     | ok               |
| SOXX       |       55 | 76.92%   | 177.32%            | -40.34% |     1    | 47.59%     | ok               |
| SPY        |       64 | 3.86%    | 50.77%             | -16.47% |     0.19 | 50.08%     | ok               |
| SUSHI-USD  |       94 | -78.10%  | -81.43%            | -82.41% |    -1.15 | 36.21%     | ok               |
| T          |       64 | 41.17%   | 24.42%             | -17.01% |     0.9  | 52.58%     | ok               |
| TGT        |       60 | -12.69%  | -8.80%             | -40.57% |    -0.18 | 39.10%     | ok               |
| TIA-USD    |       89 | -49.45%  | -87.19%            | -70.38% |    -0.38 | 36.40%     | ok               |
| TLT        |       70 | -21.65%  | -8.97%             | -21.82% |    -1.69 | 31.45%     | ok               |
| TMO        |       61 | 14.21%   | -4.30%             | -18.85% |     0.38 | 49.75%     | ok               |
| TMUS       |       70 | 7.73%    | 12.43%             | -25.69% |     0.26 | 48.42%     | ok               |
| TRX-USD    |       72 | 0.99%    | 47.48%             | -22.90% |     0.12 | 49.04%     | ok               |
| TSLA       |       69 | 5.29%    | 115.44%            | -42.22% |     0.25 | 40.93%     | ok               |
| TXN        |       77 | -17.79%  | 95.43%             | -47.39% |    -0.13 | 53.41%     | ok               |
| UNH        |       74 | 36.64%   | -16.49%            | -26.96% |     0.59 | 52.41%     | ok               |
| UNI-USD    |       90 | -74.83%  | -61.93%            | -80.61% |    -0.95 | 43.10%     | ok               |
| UPS        |       70 | -37.33%  | -23.21%            | -37.55% |    -0.76 | 39.60%     | ok               |
| USO        |       68 | 7.58%    | 52.35%             | -43.35% |     0.25 | 33.61%     | ok               |
| VEA        |       58 | -0.98%   | 48.94%             | -17.93% |     0.01 | 44.09%     | ok               |
| VIXY       |       96 | -80.86%  | -64.05%            | -88.16% |    -1.03 | 32.78%     | ok               |
| VNQ        |       75 | -16.77%  | 16.54%             | -24.92% |    -0.7  | 37.60%     | ok               |
| VTI        |       68 | -2.67%   | 49.86%             | -18.77% |    -0.04 | 50.92%     | ok               |
| VWO        |       76 | -13.41%  | 46.38%             | -25.20% |    -0.47 | 44.09%     | ok               |
| VZ         |       87 | -27.29%  | 5.21%              | -27.89% |    -0.92 | 37.27%     | ok               |
| WFC        |       84 | -16.15%  | 79.09%             | -29.78% |    -0.25 | 50.08%     | ok               |
| WIF-USD    |       68 | -35.28%  | -80.17%            | -50.54% |    -0.13 | 31.99%     | ok               |
| WMT        |       61 | 20.19%   | 99.66%             | -21.31% |     0.58 | 50.58%     | ok               |
| XBI        |       62 | 12.60%   | 80.25%             | -19.80% |     0.37 | 41.10%     | ok               |
| XLB        |       64 | -10.86%  | 20.89%             | -26.57% |    -0.36 | 36.77%     | ok               |
| XLC        |       67 | 11.34%   | 38.92%             | -12.33% |     0.42 | 54.91%     | ok               |
| XLE        |       73 | -12.12%  | 31.62%             | -37.51% |    -0.24 | 46.09%     | ok               |
| XLF        |       76 | -9.08%   | 42.05%             | -23.61% |    -0.28 | 48.25%     | ok               |
| XLI        |       66 | -0.44%   | 53.67%             | -11.74% |     0.03 | 45.26%     | ok               |
| XLK        |       42 | 62.19%   | 80.94%             | -14.75% |     1.17 | 46.09%     | ok               |
| XLM-USD    |       69 | 5.21%    | -44.15%            | -50.36% |     0.28 | 45.79%     | ok               |
| XLP        |       70 | 6.68%    | 14.44%             | -11.56% |     0.41 | 42.26%     | ok               |
| XLU        |       69 | -7.04%   | 49.71%             | -20.40% |    -0.28 | 38.60%     | ok               |
| XLV        |       68 | -13.36%  | 12.54%             | -18.00% |    -0.66 | 35.94%     | ok               |
| XLY        |       70 | 3.26%    | 31.27%             | -14.01% |     0.17 | 44.43%     | ok               |
| XOM        |       57 | -1.58%   | 36.31%             | -20.29% |     0.03 | 37.10%     | ok               |
| XRP-USD    |       58 | -30.47%  | -56.20%            | -44.89% |    -0.26 | 33.72%     | ok               |
| YFI-USD    |       83 | -65.22%  | -64.53%            | -70.46% |    -1.07 | 40.61%     | ok               |
| ZEC-USD    |       64 | 32.72%   | 1425.64%           | -47.68% |     0.5  | 34.48%     | ok               |

## AAPL Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 24.47%   | 71.72%             | -21.71% |     0.54 |       68 | 53.41%     | ok               |
|          15 | 20.64%   | 71.72%             | -23.86% |     0.47 |       75 | 60.57%     | ok               |
|          30 | 13.21%   | 71.72%             | -20.65% |     0.36 |       65 | 48.92%     | ok               |
|          25 | 13.05%   | 71.72%             | -20.03% |     0.35 |       67 | 51.08%     | ok               |
|          35 | 10.56%   | 71.72%             | -22.04% |     0.31 |       63 | 47.25%     | ok               |

## AAVE-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 17.07%   | -65.65%            | -43.61% |     0.39 |       38 | 31.61%     | ok               |
|          35 | -3.71%   | -65.65%            | -51.96% |     0.18 |       50 | 34.29%     | ok               |
|          45 | -3.97%   | -65.65%            | -49.19% |     0.16 |       40 | 26.82%     | ok               |
|          15 | -50.45%  | -65.65%            | -61.76% |    -0.3  |       80 | 52.49%     | ok               |
|          50 | -33.87%  | -65.65%            | -47.39% |    -0.36 |       42 | 19.73%     | ok               |

## ABBV Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -9.27%   | 43.28%             | -27.91% |    -0.16 |       52 | 37.10%     | ok               |
|          40 | -16.09%  | 43.28%             | -26.61% |    -0.34 |       66 | 41.60%     | ok               |
|          35 | -17.29%  | 43.28%             | -27.83% |    -0.37 |       68 | 44.43%     | ok               |
|          30 | -19.43%  | 43.28%             | -30.55% |    -0.41 |       66 | 47.25%     | ok               |
|          45 | -18.71%  | 43.28%             | -29.59% |    -0.43 |       56 | 38.94%     | ok               |

## ADA-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -77.92%  | -77.48%            | -85.97% |    -0.59 |       55 | 26.82%     | ok               |
|          45 | -80.28%  | -77.48%            | -88.02% |    -0.62 |       58 | 31.61%     | ok               |
|          35 | -82.72%  | -77.48%            | -89.77% |    -0.67 |       78 | 42.34%     | ok               |
|          30 | -83.94%  | -77.48%            | -89.69% |    -0.71 |       88 | 46.74%     | ok               |
|          40 | -83.55%  | -77.48%            | -90.19% |    -0.72 |       74 | 36.97%     | ok               |

## ADBE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 0.85%    | -63.18%            | -21.34% |     0.14 |       76 | 49.42%     | ok               |
|          40 | -12.16%  | -63.18%            | -24.87% |    -0.11 |       72 | 42.43%     | ok               |
|          25 | -17.14%  | -63.18%            | -30.16% |    -0.12 |       50 | 61.40%     | ok               |
|          15 | -24.71%  | -63.18%            | -31.45% |    -0.24 |       59 | 65.89%     | ok               |
|          20 | -26.23%  | -63.18%            | -32.24% |    -0.27 |       50 | 63.39%     | ok               |

## AGG Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -5.40%   | 1.03%              | -7.89%  |    -1.09 |       52 | 20.63%     | ok               |
|          30 | -6.52%   | 1.03%              | -10.08% |    -1.09 |       67 | 30.78%     | ok               |
|          50 | -5.22%   | 1.03%              | -7.92%  |    -1.16 |       46 | 17.14%     | ok               |
|          20 | -7.86%   | 1.03%              | -10.83% |    -1.16 |       69 | 36.11%     | ok               |
|          25 | -8.03%   | 1.03%              | -11.47% |    -1.23 |       69 | 34.44%     | ok               |

## ALGO-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -50.43%  | -71.05%            | -53.13% |    -0.57 |       86 | 38.12%     | ok               |
|          15 | -60.12%  | -71.05%            | -68.72% |    -0.63 |       88 | 50.77%     | ok               |
|          25 | -60.38%  | -71.05%            | -72.68% |    -0.69 |       88 | 45.40%     | ok               |
|          20 | -64.17%  | -71.05%            | -71.41% |    -0.76 |       90 | 48.47%     | ok               |
|          50 | -45.64%  | -71.05%            | -48.43% |    -0.81 |       42 | 16.86%     | ok               |

## AMAT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -15.22%  | 216.16%            | -54.05% |     0.02 |       68 | 61.90%     | ok               |
|          30 | -31.21%  | 216.16%            | -57.21% |    -0.25 |       69 | 53.08%     | ok               |
|          35 | -31.70%  | 216.16%            | -55.26% |    -0.27 |       71 | 50.75%     | ok               |
|          50 | -29.97%  | 216.16%            | -48.72% |    -0.27 |       52 | 38.77%     | ok               |
|          20 | -36.24%  | 216.16%            | -60.16% |    -0.3  |       72 | 58.24%     | ok               |

## AMD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 6.74%    | 205.94%            | -44.26% |     0.27 |       54 | 30.62%     | ok               |
|          40 | 4.65%    | 205.94%            | -43.98% |     0.26 |       54 | 35.94%     | ok               |
|          35 | -12.40%  | 205.94%            | -53.66% |     0.08 |       62 | 37.77%     | ok               |
|          45 | -14.79%  | 205.94%            | -53.24% |     0.04 |       60 | 33.44%     | ok               |
|          30 | -23.95%  | 205.94%            | -59.07% |    -0.05 |       63 | 40.27%     | ok               |

## AMGN Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -9.83%   | 25.36%             | -26.64% |    -0.12 |       71 | 52.41%     | ok               |
|          35 | -11.27%  | 25.36%             | -31.23% |    -0.18 |       65 | 42.43%     | ok               |
|          15 | -13.61%  | 25.36%             | -27.92% |    -0.2  |       69 | 58.24%     | ok               |
|          30 | -15.41%  | 25.36%             | -34.14% |    -0.29 |       69 | 46.26%     | ok               |
|          25 | -18.85%  | 25.36%             | -33.41% |    -0.37 |       65 | 48.59%     | ok               |

## AMZN Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -18.13%  | 44.48%             | -28.70% |    -0.53 |       54 | 29.28%     | ok               |
|          50 | -24.42%  | 44.48%             | -35.48% |    -0.87 |       50 | 23.29%     | ok               |
|          35 | -30.11%  | 44.48%             | -38.29% |    -0.94 |       68 | 32.78%     | ok               |
|          45 | -27.20%  | 44.48%             | -35.47% |    -0.96 |       54 | 26.29%     | ok               |
|          30 | -36.33%  | 44.48%             | -42.48% |    -1.08 |       80 | 38.27%     | ok               |

## APT-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 18.79%   | -89.58%            | -46.73% |     0.41 |       40 | 19.16%     | ok               |
|          45 | -11.88%  | -89.58%            | -63.86% |     0.05 |       56 | 24.71%     | ok               |
|          20 | -34.30%  | -89.58%            | -70.51% |    -0.1  |       71 | 51.15%     | ok               |
|          40 | -28.85%  | -89.58%            | -63.33% |    -0.14 |       64 | 30.27%     | ok               |
|          35 | -34.06%  | -89.58%            | -64.45% |    -0.18 |       68 | 36.02%     | ok               |

## ARB-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 36.04%   | -80.80%            | -53.74% |     0.54 |       85 | 55.17%     | ok               |
|          40 | 15.27%   | -80.80%            | -45.73% |     0.37 |       48 | 28.74%     | ok               |
|          20 | 2.23%    | -80.80%            | -60.40% |     0.29 |       73 | 48.66%     | ok               |
|          35 | 4.00%    | -80.80%            | -54.43% |     0.27 |       58 | 32.18%     | ok               |
|          45 | 3.38%    | -80.80%            | -49.08% |     0.24 |       54 | 22.03%     | ok               |

## ARKK Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -23.02%  | 61.45%             | -34.75% |    -0.26 |       92 | 50.42%     | ok               |
|          20 | -28.19%  | 61.45%             | -34.36% |    -0.39 |       89 | 45.92%     | ok               |
|          30 | -34.18%  | 61.45%             | -36.89% |    -0.6  |       85 | 40.27%     | ok               |
|          35 | -37.65%  | 61.45%             | -40.22% |    -0.73 |       86 | 37.77%     | ok               |
|          25 | -41.81%  | 61.45%             | -44.20% |    -0.79 |       93 | 42.26%     | ok               |

## ATOM-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -65.96%  | -66.65%            | -71.56% |    -0.99 |       95 | 52.68%     | ok               |
|          15 | -70.39%  | -66.65%            | -72.91% |    -1.04 |       95 | 62.84%     | ok               |
|          30 | -68.72%  | -66.65%            | -74.00% |    -1.15 |       90 | 45.79%     | ok               |
|          45 | -61.15%  | -66.65%            | -65.46% |    -1.16 |       74 | 29.50%     | ok               |
|          20 | -73.10%  | -66.65%            | -75.43% |    -1.2  |      103 | 56.51%     | ok               |

## AVAX-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 9.93%    | -74.38%            | -29.53% |     0.3  |       32 | 18.39%     | ok               |
|          40 | 7.85%    | -74.38%            | -32.96% |     0.28 |       38 | 24.90%     | ok               |
|          45 | 7.89%    | -74.38%            | -32.82% |     0.28 |       32 | 22.03%     | ok               |
|          35 | 0.08%    | -74.38%            | -36.30% |     0.19 |       56 | 30.27%     | ok               |
|          15 | -19.04%  | -74.38%            | -50.68% |     0.04 |       69 | 52.68%     | ok               |

## AVGO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 23.56%   | 217.78%            | -35.76% |     0.42 |       62 | 43.26%     | ok               |
|          25 | 19.41%   | 217.78%            | -38.01% |     0.38 |       70 | 44.59%     | ok               |
|          35 | 17.62%   | 217.78%            | -36.19% |     0.37 |       70 | 40.43%     | ok               |
|          40 | 17.22%   | 217.78%            | -40.70% |     0.36 |       60 | 37.27%     | ok               |
|          50 | 12.44%   | 217.78%            | -35.84% |     0.31 |       60 | 31.28%     | ok               |

## BA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 26.03%   | 9.70%              | -13.34% |     0.67 |       42 | 31.45%     | ok               |
|          35 | 30.46%   | 9.70%              | -23.77% |     0.59 |       72 | 44.59%     | ok               |
|          40 | 20.11%   | 9.70%              | -23.90% |     0.47 |       46 | 38.60%     | ok               |
|          25 | 10.59%   | 9.70%              | -32.48% |     0.29 |       70 | 52.58%     | ok               |
|          30 | 7.60%    | 9.70%              | -30.56% |     0.25 |       67 | 49.25%     | ok               |

## BAC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -1.76%   | 78.84%             | -21.99% |     0.01 |       62 | 37.77%     | ok               |
|          20 | -4.81%   | 78.84%             | -21.70% |    -0.03 |       80 | 53.58%     | ok               |
|          35 | -5.70%   | 78.84%             | -29.13% |    -0.09 |       70 | 45.26%     | ok               |
|          50 | -4.94%   | 78.84%             | -20.52% |    -0.1  |       60 | 34.44%     | ok               |
|          40 | -7.15%   | 78.84%             | -25.99% |    -0.15 |       64 | 40.93%     | ok               |

## BCH-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 9.27%    | -27.04%            | -45.63% |     0.32 |       69 | 55.36%     | ok               |
|          15 | -3.23%   | -27.04%            | -52.48% |     0.2  |       78 | 59.96%     | ok               |
|          25 | -4.35%   | -27.04%            | -51.94% |     0.17 |       68 | 51.53%     | ok               |
|          30 | -3.77%   | -27.04%            | -53.87% |     0.17 |       76 | 49.43%     | ok               |
|          35 | -24.30%  | -27.04%            | -64.08% |    -0.12 |       70 | 45.59%     | ok               |

## BITO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 20.33%   | -65.11%            | -31.98% |     0.41 |       54 | 25.62%     | ok               |
|          45 | 1.23%    | -65.11%            | -41.16% |     0.17 |       62 | 29.28%     | ok               |
|          30 | -1.17%   | -65.11%            | -42.82% |     0.17 |       80 | 42.26%     | ok               |
|          40 | -3.29%   | -65.11%            | -43.67% |     0.13 |       66 | 34.11%     | ok               |
|          15 | -7.38%   | -65.11%            | -48.38% |     0.12 |       89 | 51.08%     | ok               |

## BLK Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -5.80%   | 29.83%             | -21.48% |    -0.09 |       80 | 47.59%     | ok               |
|          35 | -5.24%   | 29.83%             | -17.97% |    -0.1  |       82 | 39.27%     | ok               |
|          40 | -6.98%   | 29.83%             | -20.08% |    -0.17 |       72 | 34.94%     | ok               |
|          30 | -11.24%  | 29.83%             | -24.29% |    -0.28 |       77 | 43.09%     | ok               |
|          25 | -12.14%  | 29.83%             | -23.36% |    -0.29 |       77 | 45.42%     | ok               |

## BND Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -6.54%   | 1.11%              | -9.37%  |    -0.96 |       63 | 37.77%     | ok               |
|          25 | -7.23%   | 1.11%              | -10.49% |    -1.11 |       67 | 35.77%     | ok               |
|          30 | -7.32%   | 1.11%              | -9.89%  |    -1.18 |       65 | 32.28%     | ok               |
|          15 | -8.80%   | 1.11%              | -10.98% |    -1.27 |       75 | 40.60%     | ok               |
|          45 | -7.22%   | 1.11%              | -9.57%  |    -1.39 |       50 | 22.13%     | ok               |

## BONK-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 179.94%  | -78.13%            | -35.57% |     1.28 |       44 | 21.84%     | ok               |
|          45 | 130.53%  | -78.13%            | -42.36% |     1.06 |       54 | 26.05%     | ok               |
|          20 | 137.48%  | -78.13%            | -55.19% |     0.94 |       68 | 52.87%     | ok               |
|          15 | 139.09%  | -78.13%            | -63.45% |     0.92 |       70 | 58.05%     | ok               |
|          25 | 109.07%  | -78.13%            | -47.99% |     0.86 |       67 | 48.08%     | ok               |

## BTC-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 43.79%   | -34.66%            | -15.92% |     0.81 |       46 | 34.67%     | ok               |
|          45 | 40.84%   | -34.66%            | -15.18% |     0.81 |       44 | 30.65%     | ok               |
|          35 | 26.71%   | -34.66%            | -27.54% |     0.56 |       70 | 41.57%     | ok               |
|          50 | 13.98%   | -34.66%            | -18.05% |     0.4  |       42 | 25.29%     | ok               |
|          30 | 11.49%   | -34.66%            | -21.75% |     0.33 |       74 | 48.28%     | ok               |

## C Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -6.96%   | 158.56%            | -22.28% |    -0.12 |       66 | 36.27%     | ok               |
|          45 | -13.83%  | 158.56%            | -28.12% |    -0.29 |       76 | 40.60%     | ok               |
|          15 | -22.03%  | 158.56%            | -35.02% |    -0.35 |       72 | 60.40%     | ok               |
|          25 | -21.27%  | 158.56%            | -34.18% |    -0.36 |       71 | 53.58%     | ok               |
|          20 | -23.91%  | 158.56%            | -35.56% |    -0.41 |       79 | 56.57%     | ok               |

## CAT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 24.57%   | 196.29%            | -21.02% |     0.49 |       72 | 56.74%     | ok               |
|          25 | 24.68%   | 196.29%            | -26.37% |     0.48 |       68 | 59.57%     | ok               |
|          20 | 23.19%   | 196.29%            | -25.65% |     0.46 |       78 | 63.06%     | ok               |
|          45 | 16.65%   | 196.29%            | -28.85% |     0.39 |       58 | 45.26%     | ok               |
|          35 | 13.63%   | 196.29%            | -27.72% |     0.34 |       72 | 50.08%     | ok               |

## CL Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 13.61%   | 8.72%              | -11.22% |     0.58 |       44 | 30.12%     | ok               |
|          30 | 10.88%   | 8.72%              | -14.32% |     0.4  |       62 | 46.26%     | ok               |
|          45 | 6.27%    | 8.72%              | -13.51% |     0.29 |       48 | 33.28%     | ok               |
|          35 | 5.60%    | 8.72%              | -13.83% |     0.25 |       64 | 42.60%     | ok               |
|          40 | 2.54%    | 8.72%              | -12.70% |     0.15 |       58 | 37.27%     | ok               |

## CMCSA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -36.59%  | -40.71%            | -45.95% |    -0.81 |       86 | 57.74%     | ok               |
|          30 | -38.38%  | -40.71%            | -39.80% |    -1    |       77 | 42.93%     | ok               |
|          25 | -42.15%  | -40.71%            | -43.19% |    -1.12 |       86 | 48.09%     | ok               |
|          20 | -47.48%  | -40.71%            | -48.42% |    -1.27 |       91 | 53.74%     | ok               |
|          50 | -31.96%  | -40.71%            | -33.20% |    -1.29 |       48 | 14.98%     | ok               |

## COMP-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -10.90%  | -67.92%            | -38.71% |     0.05 |       48 | 20.50%     | ok               |
|          25 | -46.85%  | -67.92%            | -61.30% |    -0.34 |       89 | 51.34%     | ok               |
|          30 | -46.23%  | -67.92%            | -59.17% |    -0.37 |       89 | 46.17%     | ok               |
|          15 | -53.93%  | -67.92%            | -66.20% |    -0.42 |      105 | 62.84%     | ok               |
|          40 | -47.94%  | -67.92%            | -50.01% |    -0.51 |       74 | 34.10%     | ok               |

## COP Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -9.76%   | -1.91%             | -35.08% |    -0.15 |       48 | 27.29%     | ok               |
|          35 | -21.85%  | -1.91%             | -43.58% |    -0.39 |       73 | 37.94%     | ok               |
|          45 | -20.42%  | -1.91%             | -41.35% |    -0.42 |       62 | 30.62%     | ok               |
|          30 | -25.89%  | -1.91%             | -43.96% |    -0.48 |       72 | 41.43%     | ok               |
|          40 | -25.44%  | -1.91%             | -47.05% |    -0.54 |       68 | 33.78%     | ok               |

## COST Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 12.08%   | 26.42%             | -24.32% |     0.39 |       66 | 50.92%     | ok               |
|          25 | 10.42%   | 26.42%             | -24.73% |     0.36 |       63 | 48.09%     | ok               |
|          35 | 5.28%    | 26.42%             | -26.58% |     0.23 |       54 | 41.43%     | ok               |
|          30 | 0.46%    | 26.42%             | -29.73% |     0.08 |       60 | 44.43%     | ok               |
|          40 | -1.18%   | 26.42%             | -28.41% |     0.03 |       56 | 38.44%     | ok               |

## CRM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | -29.53%  | -43.80%            | -33.61% |    -0.58 |       62 | 38.27%     | ok               |
|          15 | -36.55%  | -43.80%            | -44.49% |    -0.59 |       92 | 54.91%     | ok               |
|          40 | -34.74%  | -43.80%            | -39.59% |    -0.8  |       68 | 34.28%     | ok               |
|          30 | -39.47%  | -43.80%            | -41.36% |    -0.82 |       65 | 43.09%     | ok               |
|          20 | -44.34%  | -43.80%            | -46.71% |    -0.85 |       78 | 48.75%     | ok               |

## CRV-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 12.72%   | -60.87%            | -37.78% |     0.35 |       68 | 31.42%     | ok               |
|          45 | -1.09%   | -60.87%            | -42.29% |     0.18 |       54 | 20.69%     | ok               |
|          50 | -0.89%   | -60.87%            | -29.30% |     0.18 |       46 | 17.43%     | ok               |
|          40 | -6.61%   | -60.87%            | -38.86% |     0.13 |       58 | 27.01%     | ok               |
|          30 | -10.49%  | -60.87%            | -39.89% |     0.12 |       66 | 36.02%     | ok               |

## CSCO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 34.98%   | 135.30%            | -19.34% |     0.75 |       52 | 38.27%     | ok               |
|          45 | 33.41%   | 135.30%            | -19.34% |     0.7  |       51 | 40.27%     | ok               |
|          25 | 27.99%   | 135.30%            | -23.28% |     0.58 |       63 | 51.25%     | ok               |
|          35 | 27.38%   | 135.30%            | -23.68% |     0.58 |       51 | 46.76%     | ok               |
|          30 | 27.39%   | 135.30%            | -21.79% |     0.57 |       59 | 49.25%     | ok               |

## CVX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -10.94%  | 15.26%             | -23.25% |    -0.22 |       73 | 43.93%     | ok               |
|          20 | -13.96%  | 15.26%             | -25.18% |    -0.31 |       73 | 45.26%     | ok               |
|          35 | -12.78%  | 15.26%             | -27.83% |    -0.31 |       69 | 38.27%     | ok               |
|          40 | -13.26%  | 15.26%             | -26.30% |    -0.36 |       73 | 34.78%     | ok               |
|          30 | -14.65%  | 15.26%             | -26.75% |    -0.36 |       71 | 41.26%     | ok               |

## DASH-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 109.50%  | 35.34%             | -27.01% |     0.89 |       40 | 15.33%     | ok               |
|          40 | 56.05%   | 35.34%             | -32.07% |     0.63 |       48 | 22.99%     | ok               |
|          45 | 51.29%   | 35.34%             | -35.73% |     0.6  |       44 | 17.62%     | ok               |
|          35 | -41.82%  | 35.34%             | -63.23% |    -0.02 |       69 | 27.59%     | ok               |
|          25 | -47.10%  | 35.34%             | -64.14% |    -0.08 |       69 | 33.72%     | ok               |

## DBC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -8.58%   | 25.76%             | -20.31% |    -0.32 |       40 | 20.97%     | ok               |
|          15 | -11.11%  | 25.76%             | -27.14% |    -0.35 |       75 | 38.10%     | ok               |
|          35 | -11.05%  | 25.76%             | -23.91% |    -0.37 |       62 | 31.61%     | ok               |
|          45 | -11.08%  | 25.76%             | -21.46% |    -0.4  |       56 | 24.63%     | ok               |
|          30 | -13.70%  | 25.76%             | -25.70% |    -0.48 |       60 | 32.95%     | ok               |

## DE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -6.70%   | 54.09%             | -28.94% |    -0.04 |       72 | 52.75%     | ok               |
|          30 | -7.57%   | 54.09%             | -25.24% |    -0.07 |       72 | 47.42%     | ok               |
|          25 | -9.01%   | 54.09%             | -26.67% |    -0.1  |       74 | 50.08%     | ok               |
|          50 | -8.73%   | 54.09%             | -24.35% |    -0.15 |       72 | 32.28%     | ok               |
|          45 | -10.55%  | 54.09%             | -27.91% |    -0.18 |       70 | 36.77%     | ok               |

## DIA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 0.19%    | 36.40%             | -13.15% |     0.05 |       60 | 42.43%     | ok               |
|          25 | -0.35%   | 36.40%             | -11.28% |     0.02 |       60 | 45.76%     | ok               |
|          30 | -1.88%   | 36.40%             | -12.94% |    -0.06 |       60 | 44.59%     | ok               |
|          20 | -3.76%   | 36.40%             | -13.85% |    -0.16 |       64 | 48.09%     | ok               |
|          40 | -3.86%   | 36.40%             | -15.06% |    -0.19 |       66 | 39.77%     | ok               |

## DIS Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 15.91%   | -13.80%            | -14.24% |     0.51 |       48 | 28.29%     | ok               |
|          45 | -8.30%   | -13.80%            | -16.54% |    -0.13 |       51 | 31.95%     | ok               |
|          40 | -9.74%   | -13.80%            | -23.29% |    -0.14 |       63 | 37.27%     | ok               |
|          15 | -19.88%  | -13.80%            | -31.15% |    -0.31 |       88 | 58.07%     | ok               |
|          35 | -18.76%  | -13.80%            | -25.70% |    -0.35 |       73 | 43.26%     | ok               |

## DOGE-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 11.62%   | -71.90%            | -57.89% |     0.38 |       83 | 66.86%     | ok               |
|          20 | -6.25%   | -71.90%            | -55.83% |     0.22 |       86 | 61.69%     | ok               |
|          25 | -10.26%  | -71.90%            | -53.72% |     0.17 |       74 | 56.13%     | ok               |
|          30 | -24.91%  | -71.90%            | -60.95% |    -0.01 |       77 | 50.57%     | ok               |
|          35 | -50.83%  | -71.90%            | -64.38% |    -0.49 |       74 | 43.87%     | ok               |

## DOT-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -29.36%  | -82.17%            | -46.17% |    -0.33 |       58 | 25.67%     | ok               |
|          45 | -35.39%  | -82.17%            | -54.01% |    -0.41 |       50 | 30.46%     | ok               |
|          20 | -57.82%  | -82.17%            | -64.09% |    -0.52 |       92 | 60.34%     | ok               |
|          35 | -53.84%  | -82.17%            | -62.62% |    -0.54 |       76 | 40.80%     | ok               |
|          30 | -56.92%  | -82.17%            | -62.71% |    -0.58 |       90 | 48.08%     | ok               |

## DXY-INDEX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -2.00%   | -0.90%             | -6.02%  |    -0.3  |       38 | 30.59%     | ok               |
|          15 | -4.75%   | -0.90%             | -11.37% |    -0.43 |       84 | 76.79%     | ok               |
|          40 | -4.24%   | -0.90%             | -7.30%  |    -0.54 |       74 | 50.11%     | ok               |
|          30 | -4.77%   | -0.90%             | -9.61%  |    -0.54 |       72 | 62.04%     | ok               |
|          25 | -5.73%   | -0.90%             | -12.10% |    -0.61 |       78 | 67.25%     | ok               |

## EEM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -4.96%   | 68.21%             | -19.52% |    -0.11 |       64 | 39.77%     | ok               |
|          35 | -5.62%   | 68.21%             | -23.88% |    -0.12 |       66 | 41.76%     | ok               |
|          50 | -4.94%   | 68.21%             | -15.88% |    -0.12 |       52 | 35.77%     | ok               |
|          45 | -6.04%   | 68.21%             | -17.36% |    -0.16 |       54 | 37.44%     | ok               |
|          30 | -9.40%   | 68.21%             | -25.67% |    -0.25 |       64 | 43.43%     | ok               |

## EFA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -3.05%   | 38.38%             | -10.80% |    -0.05 |       62 | 52.41%     | ok               |
|          20 | -9.78%   | 38.38%             | -12.73% |    -0.34 |       69 | 49.42%     | ok               |
|          30 | -9.68%   | 38.38%             | -15.14% |    -0.36 |       62 | 44.76%     | ok               |
|          50 | -9.07%   | 38.38%             | -17.56% |    -0.4  |       54 | 36.27%     | ok               |
|          25 | -11.91%  | 38.38%             | -16.37% |    -0.45 |       64 | 46.76%     | ok               |

## EOG Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -20.72%  | 20.30%             | -39.69% |    -0.49 |       56 | 32.61%     | ok               |
|          30 | -25.31%  | 20.30%             | -48.13% |    -0.55 |       79 | 46.42%     | ok               |
|          50 | -23.61%  | 20.30%             | -40.57% |    -0.6  |       60 | 29.62%     | ok               |
|          35 | -26.13%  | 20.30%             | -46.26% |    -0.62 |       77 | 41.10%     | ok               |
|          40 | -25.41%  | 20.30%             | -43.26% |    -0.62 |       64 | 35.94%     | ok               |

## ETC-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -7.93%   | -65.97%            | -27.89% |    -0.02 |       28 | 17.05%     | ok               |
|          35 | -15.03%  | -65.97%            | -42.62% |    -0.11 |       44 | 27.01%     | ok               |
|          45 | -16.07%  | -65.97%            | -35.44% |    -0.17 |       26 | 18.97%     | ok               |
|          40 | -21.04%  | -65.97%            | -40.48% |    -0.26 |       42 | 22.80%     | ok               |
|          30 | -35.69%  | -65.97%            | -48.16% |    -0.51 |       64 | 31.23%     | ok               |

## ETH-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 133.43%  | -35.07%            | -30.11% |     1.17 |       62 | 44.83%     | ok               |
|          30 | 112.48%  | -35.07%            | -32.89% |     1.03 |       66 | 52.87%     | ok               |
|          40 | 43.45%   | -35.07%            | -33.11% |     0.64 |       60 | 37.55%     | ok               |
|          20 | 37.72%   | -35.07%            | -39.10% |     0.56 |       84 | 62.26%     | ok               |
|          25 | 36.70%   | -35.07%            | -40.90% |     0.56 |       68 | 58.05%     | ok               |

## EWJ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -18.16%  | 39.58%             | -30.73% |    -0.59 |       62 | 39.10%     | ok               |
|          20 | -19.55%  | 39.58%             | -31.32% |    -0.62 |       58 | 41.10%     | ok               |
|          45 | -18.94%  | 39.58%             | -27.68% |    -0.72 |       58 | 31.28%     | ok               |
|          25 | -21.87%  | 39.58%             | -31.18% |    -0.72 |       58 | 40.10%     | ok               |
|          35 | -22.08%  | 39.58%             | -32.54% |    -0.75 |       68 | 37.44%     | ok               |

## FCX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -4.48%   | 62.72%             | -27.82% |     0.06 |       52 | 29.45%     | ok               |
|          45 | -8.60%   | 62.72%             | -35.29% |    -0    |       52 | 33.94%     | ok               |
|          40 | -20.30%  | 62.72%             | -44.23% |    -0.2  |       62 | 38.44%     | ok               |
|          30 | -28.65%  | 62.72%             | -48.09% |    -0.33 |       63 | 45.09%     | ok               |
|          20 | -34.13%  | 62.72%             | -57.65% |    -0.39 |       70 | 51.91%     | ok               |

## FET-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 6.10%    | -79.39%            | -59.46% |     0.36 |       84 | 50.57%     | ok               |
|          15 | -16.09%  | -79.39%            | -59.58% |     0.19 |       82 | 54.60%     | ok               |
|          25 | -34.04%  | -79.39%            | -60.01% |    -0.05 |       87 | 44.06%     | ok               |
|          30 | -35.78%  | -79.39%            | -48.80% |    -0.1  |       79 | 40.04%     | ok               |
|          35 | -50.53%  | -79.39%            | -60.25% |    -0.44 |       65 | 33.14%     | ok               |

## FIL-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -26.71%  | -76.45%            | -41.11% |    -0.27 |       46 | 22.99%     | ok               |
|          35 | -44.63%  | -76.45%            | -48.17% |    -0.61 |       56 | 27.01%     | ok               |
|          45 | -39.88%  | -76.45%            | -43.98% |    -0.61 |       42 | 17.24%     | ok               |
|          30 | -47.29%  | -76.45%            | -50.88% |    -0.62 |       70 | 32.57%     | ok               |
|          50 | -39.00%  | -76.45%            | -44.95% |    -0.69 |       36 | 12.64%     | ok               |

## FXI Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -6.30%   | 47.38%             | -22.57% |    -0.07 |       44 | 31.28%     | ok               |
|          30 | -6.84%   | 47.38%             | -23.91% |    -0.09 |       44 | 30.12%     | ok               |
|          45 | -6.49%   | 47.38%             | -26.75% |    -0.09 |       44 | 24.63%     | ok               |
|          15 | -8.97%   | 47.38%             | -21.68% |    -0.12 |       52 | 34.78%     | ok               |
|          20 | -10.08%  | 47.38%             | -24.53% |    -0.16 |       50 | 32.45%     | ok               |

## GDX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 18.06%   | 191.35%            | -35.59% |     0.39 |       73 | 52.91%     | ok               |
|          40 | 13.85%   | 191.35%            | -31.87% |     0.35 |       64 | 42.93%     | ok               |
|          30 | 11.28%   | 191.35%            | -34.99% |     0.3  |       60 | 48.09%     | ok               |
|          35 | 8.95%    | 191.35%            | -32.37% |     0.27 |       68 | 45.26%     | ok               |
|          25 | 6.77%    | 191.35%            | -38.90% |     0.24 |       63 | 49.75%     | ok               |

## GDXJ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -7.90%   | 214.09%            | -45.05% |     0.06 |       67 | 53.24%     | ok               |
|          50 | -18.94%  | 214.09%            | -44.94% |    -0.2  |       58 | 37.94%     | ok               |
|          30 | -23.13%  | 214.09%            | -44.93% |    -0.22 |       68 | 46.42%     | ok               |
|          25 | -26.54%  | 214.09%            | -47.26% |    -0.25 |       72 | 49.92%     | ok               |
|          35 | -26.76%  | 214.09%            | -43.49% |    -0.3  |       70 | 44.09%     | ok               |

## GE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 34.70%   | 207.08%            | -22.29% |     0.68 |       66 | 40.60%     | ok               |
|          45 | 24.53%   | 207.08%            | -25.68% |     0.52 |       74 | 43.43%     | ok               |
|          20 | 19.92%   | 207.08%            | -26.63% |     0.43 |       69 | 57.40%     | ok               |
|          35 | 16.92%   | 207.08%            | -27.11% |     0.39 |       80 | 48.75%     | ok               |
|          30 | 16.65%   | 207.08%            | -27.82% |     0.38 |       74 | 53.74%     | ok               |

## GLD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | 31.42%   | 105.06%            | -14.61% |     0.75 |       46 | 48.09%     | ok               |
|          20 | 29.46%   | 105.06%            | -14.61% |     0.71 |       48 | 49.42%     | ok               |
|          30 | 25.16%   | 105.06%            | -16.63% |     0.64 |       48 | 46.92%     | ok               |
|          15 | 21.53%   | 105.06%            | -17.54% |     0.54 |       50 | 53.58%     | ok               |
|          35 | 18.81%   | 105.06%            | -17.29% |     0.52 |       52 | 45.92%     | ok               |

## GOOGL Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 80.35%   | 145.92%            | -19.12% |     1.22 |       63 | 48.42%     | ok               |
|          25 | 81.59%   | 145.92%            | -19.76% |     1.19 |       55 | 55.41%     | ok               |
|          30 | 79.31%   | 145.92%            | -20.41% |     1.18 |       59 | 53.08%     | ok               |
|          45 | 64.33%   | 145.92%            | -15.05% |     1.11 |       56 | 41.60%     | ok               |
|          40 | 60.75%   | 145.92%            | -20.80% |     1.04 |       52 | 43.26%     | ok               |

## GRT-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 23.67%   | -87.39%            | -30.00% |     0.48 |       38 | 20.50%     | ok               |
|          15 | -1.79%   | -87.39%            | -49.67% |     0.24 |       75 | 61.11%     | ok               |
|          20 | -5.20%   | -87.39%            | -46.47% |     0.19 |       83 | 55.56%     | ok               |
|          45 | -3.91%   | -87.39%            | -48.76% |     0.12 |       46 | 25.67%     | ok               |
|          35 | -7.45%   | -87.39%            | -49.87% |     0.1  |       58 | 34.87%     | ok               |

## GS Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 21.11%   | 179.33%            | -20.56% |     0.47 |       74 | 61.06%     | ok               |
|          20 | 4.59%    | 179.33%            | -23.19% |     0.19 |       74 | 57.07%     | ok               |
|          40 | 0.08%    | 179.33%            | -17.88% |     0.09 |       72 | 45.26%     | ok               |
|          25 | -0.70%   | 179.33%            | -23.32% |     0.09 |       74 | 54.58%     | ok               |
|          30 | -2.38%   | 179.33%            | -22.13% |     0.05 |       76 | 52.08%     | ok               |

## HD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -8.53%   | -5.44%             | -18.58% |    -0.15 |       73 | 44.43%     | ok               |
|          25 | -9.24%   | -5.44%             | -19.40% |    -0.17 |       72 | 46.42%     | ok               |
|          45 | -10.76%  | -5.44%             | -19.30% |    -0.3  |       58 | 28.79%     | ok               |
|          35 | -14.52%  | -5.44%             | -22.43% |    -0.36 |       80 | 40.43%     | ok               |
|          40 | -13.27%  | -5.44%             | -19.06% |    -0.36 |       84 | 34.11%     | ok               |

## HON Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -13.43%  | 15.99%             | -21.17% |    -0.4  |       72 | 31.78%     | ok               |
|          45 | -15.16%  | 15.99%             | -19.99% |    -0.43 |       74 | 36.77%     | ok               |
|          40 | -23.52%  | 15.99%             | -26.29% |    -0.66 |       76 | 41.10%     | ok               |
|          35 | -26.77%  | 15.99%             | -29.07% |    -0.75 |       91 | 47.59%     | ok               |
|          30 | -29.10%  | 15.99%             | -31.48% |    -0.8  |       94 | 52.75%     | ok               |

## HYG Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -7.98%   | 3.75%              | -7.98%  |    -0.96 |       70 | 29.28%     | ok               |
|          15 | -9.95%   | 3.75%              | -10.29% |    -1.08 |       88 | 41.26%     | ok               |
|          20 | -9.69%   | 3.75%              | -10.29% |    -1.08 |       86 | 39.10%     | ok               |
|          45 | -8.66%   | 3.75%              | -8.66%  |    -1.09 |       66 | 26.12%     | ok               |
|          25 | -9.88%   | 3.75%              | -10.11% |    -1.11 |       83 | 36.77%     | ok               |

## IBIT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 53.73%   | -5.79%             | -17.37% |     1.07 |       22 | 22.59%     | ok               |
|          15 | 58.82%   | -5.79%             | -19.20% |     0.98 |       40 | 40.00%     | ok               |
|          45 | 44.27%   | -5.79%             | -17.37% |     0.91 |       26 | 24.00%     | ok               |
|          40 | 38.04%   | -5.79%             | -17.78% |     0.81 |       26 | 25.88%     | ok               |
|          30 | 30.86%   | -5.79%             | -18.95% |     0.67 |       34 | 32.47%     | ok               |

## IBM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 20.12%   | 60.87%             | -28.20% |     0.44 |       92 | 62.06%     | ok               |
|          30 | 6.57%    | 60.87%             | -27.54% |     0.23 |       78 | 49.75%     | ok               |
|          20 | 1.88%    | 60.87%             | -34.12% |     0.15 |       76 | 54.41%     | ok               |
|          35 | 1.99%    | 60.87%             | -27.54% |     0.14 |       72 | 45.26%     | ok               |
|          50 | -0.25%   | 60.87%             | -22.50% |     0.09 |       54 | 32.45%     | ok               |

## ICP-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | -1.41%   | -67.07%            | -38.23% |     0.19 |       64 | 28.93%     | ok               |
|          40 | -5.81%   | -67.07%            | -32.85% |     0.12 |       58 | 24.71%     | ok               |
|          30 | -13.02%  | -67.07%            | -51.29% |     0.12 |       79 | 35.06%     | ok               |
|          50 | -16.04%  | -67.07%            | -43.65% |    -0.06 |       36 | 14.94%     | ok               |
|          20 | -42.87%  | -67.07%            | -58.71% |    -0.15 |       88 | 46.17%     | ok               |

## IEF Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -7.23%   | -0.19%             | -10.09% |    -0.87 |       70 | 42.10%     | ok               |
|          15 | -7.78%   | -0.19%             | -10.82% |    -0.92 |       69 | 43.59%     | ok               |
|          40 | -8.39%   | -0.19%             | -9.67%  |    -1.31 |       60 | 24.79%     | ok               |
|          45 | -8.07%   | -0.19%             | -9.73%  |    -1.33 |       50 | 22.80%     | ok               |
|          25 | -10.80%  | -0.19%             | -11.49% |    -1.38 |       76 | 39.27%     | ok               |

## IEMG Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | -1.80%   | 62.14%             | -22.13% |     0    |       63 | 42.43%     | ok               |
|          50 | -1.54%   | 62.14%             | -13.91% |    -0    |       54 | 34.28%     | ok               |
|          40 | -2.44%   | 62.14%             | -18.43% |    -0.03 |       60 | 39.93%     | ok               |
|          45 | -2.35%   | 62.14%             | -14.92% |    -0.03 |       50 | 36.77%     | ok               |
|          25 | -6.13%   | 62.14%             | -25.58% |    -0.14 |       59 | 45.26%     | ok               |

## INJ-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -16.04%  | -66.23%            | -56.91% |    -0.02 |       44 | 22.22%     | ok               |
|          35 | -22.55%  | -66.23%            | -61.19% |    -0.04 |       58 | 31.61%     | ok               |
|          50 | -25.16%  | -66.23%            | -52.76% |    -0.19 |       48 | 19.16%     | ok               |
|          40 | -30.34%  | -66.23%            | -59.56% |    -0.21 |       48 | 27.97%     | ok               |
|          20 | -50.45%  | -66.23%            | -79.76% |    -0.36 |       78 | 46.36%     | ok               |

## INTC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 91.41%   | 154.67%            | -53.65% |     0.78 |       82 | 60.40%     | ok               |
|          45 | 76.11%   | 154.67%            | -49.32% |     0.74 |       60 | 34.28%     | ok               |
|          20 | 80.58%   | 154.67%            | -52.47% |     0.73 |       78 | 56.24%     | ok               |
|          25 | 75.50%   | 154.67%            | -56.41% |     0.72 |       75 | 51.58%     | ok               |
|          40 | 70.33%   | 154.67%            | -55.86% |     0.7  |       68 | 38.60%     | ok               |

## INTU Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -0.39%   | -58.40%            | -40.80% |     0.11 |       71 | 27.79%     | ok               |
|          45 | -3.80%   | -58.40%            | -42.69% |     0.05 |       69 | 31.95%     | ok               |
|          40 | -10.93%  | -58.40%            | -46.52% |    -0.08 |       71 | 35.11%     | ok               |
|          35 | -17.11%  | -58.40%            | -48.24% |    -0.19 |       73 | 38.94%     | ok               |
|          15 | -20.82%  | -58.40%            | -46.90% |    -0.24 |       83 | 50.58%     | ok               |

## ITA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 0.84%    | 91.21%             | -21.48% |     0.09 |       76 | 38.44%     | ok               |
|          15 | -2.59%   | 91.21%             | -28.17% |     0.02 |       84 | 60.07%     | ok               |
|          30 | -2.66%   | 91.21%             | -23.75% |    -0    |       72 | 48.42%     | ok               |
|          35 | -4.73%   | 91.21%             | -23.16% |    -0.07 |       76 | 46.76%     | ok               |
|          40 | -5.82%   | 91.21%             | -20.58% |    -0.11 |       78 | 43.26%     | ok               |

## IWM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 8.60%    | 49.27%             | -14.08% |     0.39 |       42 | 31.28%     | ok               |
|          30 | 9.40%    | 49.27%             | -12.83% |     0.39 |       48 | 35.77%     | ok               |
|          25 | 9.50%    | 49.27%             | -13.55% |     0.39 |       50 | 36.94%     | ok               |
|          35 | 8.35%    | 49.27%             | -14.11% |     0.36 |       48 | 33.61%     | ok               |
|          20 | 5.19%    | 49.27%             | -14.08% |     0.24 |       60 | 37.94%     | ok               |

## JNJ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 24.11%   | 66.37%             | -10.57% |     0.94 |       54 | 37.60%     | ok               |
|          45 | 14.22%   | 66.37%             | -13.35% |     0.58 |       56 | 42.60%     | ok               |
|          15 | 15.10%   | 66.37%             | -18.02% |     0.52 |       68 | 56.91%     | ok               |
|          40 | 11.72%   | 66.37%             | -14.77% |     0.47 |       62 | 46.76%     | ok               |
|          20 | 11.19%   | 66.37%             | -17.61% |     0.42 |       72 | 53.58%     | ok               |

## JPM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 20.10%   | 90.58%             | -15.90% |     0.66 |       52 | 41.43%     | ok               |
|          45 | 8.69%    | 90.58%             | -21.91% |     0.32 |       54 | 44.43%     | ok               |
|          40 | -5.66%   | 90.58%             | -28.47% |    -0.09 |       66 | 46.92%     | ok               |
|          20 | -11.40%  | 90.58%             | -33.59% |    -0.17 |       84 | 58.40%     | ok               |
|          35 | -10.93%  | 90.58%             | -27.43% |    -0.23 |       72 | 50.58%     | ok               |

## KO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 28.93%   | 39.37%             | -8.07%  |     1.03 |       49 | 37.77%     | ok               |
|          35 | 24.98%   | 39.37%             | -8.07%  |     0.93 |       52 | 36.44%     | ok               |
|          40 | 22.37%   | 39.37%             | -9.28%  |     0.9  |       54 | 33.28%     | ok               |
|          25 | 23.60%   | 39.37%             | -9.37%  |     0.86 |       55 | 40.43%     | ok               |
|          50 | 14.81%   | 39.37%             | -11.40% |     0.68 |       36 | 26.79%     | ok               |

## LDO-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 33.16%   | -81.97%            | -43.48% |     0.53 |       83 | 51.72%     | ok               |
|          20 | 20.87%   | -81.97%            | -43.71% |     0.45 |       85 | 47.13%     | ok               |
|          50 | 13.59%   | -81.97%            | -48.77% |     0.35 |       46 | 16.67%     | ok               |
|          30 | 8.74%    | -81.97%            | -58.32% |     0.34 |       72 | 37.74%     | ok               |
|          35 | -0.97%   | -81.97%            | -63.16% |     0.24 |       74 | 30.65%     | ok               |

## LIN Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 2.22%    | 25.61%             | -23.68% |     0.14 |       64 | 49.92%     | ok               |
|          25 | 1.94%    | 25.61%             | -22.01% |     0.13 |       63 | 41.93%     | ok               |
|          20 | -0.25%   | 25.61%             | -23.00% |     0.06 |       62 | 45.09%     | ok               |
|          35 | -1.74%   | 25.61%             | -21.18% |    -0.01 |       62 | 32.61%     | ok               |
|          30 | -2.37%   | 25.61%             | -21.53% |    -0.02 |       66 | 39.10%     | ok               |

## LINK-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -18.18%  | -60.50%            | -50.48% |     0.04 |       72 | 41.76%     | ok               |
|          45 | -16.95%  | -60.50%            | -38.56% |    -0    |       50 | 26.25%     | ok               |
|          50 | -16.55%  | -60.50%            | -36.98% |    -0.02 |       40 | 20.88%     | ok               |
|          35 | -27.53%  | -60.50%            | -49.56% |    -0.1  |       60 | 36.40%     | ok               |
|          40 | -31.51%  | -60.50%            | -50.91% |    -0.19 |       56 | 30.65%     | ok               |

## LLY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 5.11%    | 60.69%             | -38.23% |     0.21 |       46 | 37.44%     | ok               |
|          15 | -2.74%   | 60.69%             | -48.12% |     0.1  |       63 | 61.06%     | ok               |
|          45 | -6.72%   | 60.69%             | -42.66% |    -0.01 |       54 | 40.93%     | ok               |
|          20 | -18.40%  | 60.69%             | -51.34% |    -0.18 |       72 | 56.07%     | ok               |
|          25 | -19.75%  | 60.69%             | -53.47% |    -0.21 |       68 | 53.41%     | ok               |

## LRCX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -8.29%   | 285.68%            | -60.45% |     0.1  |       83 | 55.07%     | ok               |
|          50 | -13.27%  | 285.68%            | -50.39% |    -0.01 |       80 | 36.77%     | ok               |
|          40 | -15.87%  | 285.68%            | -56.86% |    -0.02 |       72 | 42.60%     | ok               |
|          35 | -21.33%  | 285.68%            | -61.76% |    -0.09 |       80 | 44.59%     | ok               |
|          20 | -23.51%  | 285.68%            | -67.48% |    -0.1  |       89 | 50.58%     | ok               |

## LTC-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -12.22%  | -56.19%            | -44.78% |    -0    |       56 | 31.80%     | ok               |
|          35 | -22.47%  | -56.19%            | -54.86% |    -0.13 |       66 | 42.91%     | ok               |
|          30 | -34.00%  | -56.19%            | -53.76% |    -0.29 |       66 | 48.47%     | ok               |
|          40 | -31.40%  | -56.19%            | -56.10% |    -0.3  |       58 | 38.12%     | ok               |
|          25 | -36.79%  | -56.19%            | -54.26% |    -0.33 |       74 | 50.96%     | ok               |

## MCD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 1.93%    | -4.05%             | -9.22%  |     0.14 |       40 | 20.80%     | ok               |
|          30 | -2.55%   | -4.05%             | -18.81% |    -0.05 |       75 | 38.10%     | ok               |
|          25 | -3.59%   | -4.05%             | -20.47% |    -0.09 |       75 | 40.77%     | ok               |
|          35 | -7.68%   | -4.05%             | -15.45% |    -0.29 |       67 | 34.44%     | ok               |
|          40 | -7.95%   | -4.05%             | -16.86% |    -0.33 |       71 | 28.79%     | ok               |

## META Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -9.24%   | 33.43%             | -31.03% |    -0.09 |       66 | 37.94%     | ok               |
|          40 | -19.22%  | 33.43%             | -35.11% |    -0.3  |       66 | 40.93%     | ok               |
|          25 | -27.19%  | 33.43%             | -39.84% |    -0.43 |       67 | 51.58%     | ok               |
|          50 | -23.10%  | 33.43%             | -34.00% |    -0.44 |       70 | 34.11%     | ok               |
|          30 | -29.14%  | 33.43%             | -38.96% |    -0.5  |       72 | 48.42%     | ok               |

## MPC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 12.33%   | 66.76%             | -23.96% |     0.34 |       52 | 37.60%     | ok               |
|          45 | 5.20%    | 66.76%             | -25.09% |     0.21 |       58 | 41.26%     | ok               |
|          40 | 3.61%    | 66.76%             | -25.70% |     0.18 |       60 | 43.59%     | ok               |
|          35 | 0.41%    | 66.76%             | -35.90% |     0.13 |       68 | 46.09%     | ok               |
|          30 | -15.39%  | 66.76%             | -44.76% |    -0.17 |       71 | 48.92%     | ok               |

## MRK Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -20.82%  | -0.60%             | -30.12% |    -0.39 |       87 | 55.41%     | ok               |
|          25 | -20.44%  | -0.60%             | -31.07% |    -0.41 |       72 | 47.42%     | ok               |
|          20 | -24.34%  | -0.60%             | -29.59% |    -0.51 |       77 | 50.75%     | ok               |
|          45 | -23.27%  | -0.60%             | -26.02% |    -0.62 |       57 | 33.61%     | ok               |
|          50 | -22.92%  | -0.60%             | -25.69% |    -0.66 |       56 | 30.62%     | ok               |

## MS Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -2.42%   | 164.44%            | -19.99% |     0.02 |       72 | 41.60%     | ok               |
|          15 | -8.20%   | 164.44%            | -22.02% |    -0.08 |       77 | 58.90%     | ok               |
|          20 | -8.31%   | 164.44%            | -25.68% |    -0.1  |       81 | 55.07%     | ok               |
|          35 | -9.22%   | 164.44%            | -25.26% |    -0.15 |       76 | 46.26%     | ok               |
|          30 | -13.23%  | 164.44%            | -27.79% |    -0.24 |       81 | 50.25%     | ok               |

## MSFT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -23.21%  | -6.14%             | -25.26% |    -0.66 |       68 | 34.44%     | ok               |
|          50 | -24.61%  | -6.14%             | -26.14% |    -0.73 |       64 | 29.45%     | ok               |
|          35 | -35.39%  | -6.14%             | -35.38% |    -0.96 |       75 | 43.09%     | ok               |
|          40 | -34.77%  | -6.14%             | -34.77% |    -0.98 |       71 | 37.94%     | ok               |
|          25 | -38.72%  | -6.14%             | -40.19% |    -1.01 |       89 | 50.92%     | ok               |

## MU Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 450.70%  | 1111.83%           | -61.96% |     1.59 |       47 | 67.72%     | ok               |
|          25 | 357.11%  | 1111.83%           | -67.90% |     1.51 |       47 | 61.56%     | ok               |
|          20 | 318.50%  | 1111.83%           | -67.25% |     1.41 |       53 | 63.73%     | ok               |
|          40 | 288.27%  | 1111.83%           | -64.30% |     1.4  |       56 | 55.07%     | ok               |
|          30 | 270.20%  | 1111.83%           | -68.76% |     1.34 |       51 | 59.90%     | ok               |

## NEAR-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 77.66%   | -42.82%            | -44.39% |     0.86 |       42 | 23.37%     | ok               |
|          50 | 49.39%   | -42.82%            | -49.90% |     0.68 |       38 | 18.39%     | ok               |
|          40 | 51.46%   | -42.82%            | -53.32% |     0.67 |       42 | 27.39%     | ok               |
|          35 | 23.90%   | -42.82%            | -59.02% |     0.45 |       62 | 31.99%     | ok               |
|          30 | -0.20%   | -42.82%            | -60.10% |     0.25 |       81 | 40.23%     | ok               |

## NEM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 3.24%    | 195.17%            | -29.41% |     0.21 |       62 | 61.40%     | ok               |
|          20 | -7.81%   | 195.17%            | -30.47% |     0.07 |       72 | 56.91%     | ok               |
|          25 | -21.27%  | 195.17%            | -37.89% |    -0.14 |       68 | 54.74%     | ok               |
|          50 | -23.65%  | 195.17%            | -32.97% |    -0.25 |       56 | 40.77%     | ok               |
|          30 | -31.13%  | 195.17%            | -38.49% |    -0.33 |       72 | 53.08%     | ok               |

## NFLX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 49.03%   | 30.27%             | -11.94% |     1.01 |       46 | 46.59%     | ok               |
|          50 | 43.03%   | 30.27%             | -16.28% |     0.97 |       48 | 38.94%     | ok               |
|          35 | 41.37%   | 30.27%             | -18.30% |     0.85 |       60 | 50.08%     | ok               |
|          45 | 32.91%   | 30.27%             | -15.48% |     0.76 |       52 | 42.93%     | ok               |
|          25 | 32.27%   | 30.27%             | -21.09% |     0.68 |       62 | 57.07%     | ok               |

## NKE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -33.86%  | -59.77%            | -50.44% |    -0.42 |       93 | 52.58%     | ok               |
|          40 | -26.46%  | -59.77%            | -31.19% |    -0.5  |       63 | 30.12%     | ok               |
|          15 | -38.38%  | -59.77%            | -55.52% |    -0.51 |       91 | 56.91%     | ok               |
|          50 | -23.38%  | -59.77%            | -31.53% |    -0.76 |       46 | 16.97%     | ok               |
|          25 | -45.09%  | -59.77%            | -52.84% |    -0.79 |       91 | 48.59%     | ok               |

## NOW Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 12.52%   | -31.29%            | -26.36% |     0.32 |       79 | 51.58%     | ok               |
|          30 | 8.49%    | -31.29%            | -27.34% |     0.27 |       82 | 45.59%     | ok               |
|          15 | 5.04%    | -31.29%            | -26.36% |     0.23 |       88 | 54.74%     | ok               |
|          25 | 2.32%    | -31.29%            | -25.70% |     0.2  |       74 | 48.92%     | ok               |
|          35 | -1.09%   | -31.29%            | -27.02% |     0.13 |       83 | 40.10%     | ok               |

## NVDA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -2.00%   | 129.95%            | -35.26% |     0.13 |       72 | 47.77%     | ok               |
|          25 | -7.56%   | 129.95%            | -33.22% |     0.06 |       69 | 50.80%     | ok               |
|          20 | -11.34%  | 129.95%            | -40.59% |     0.02 |       70 | 55.61%     | ok               |
|          35 | -15.24%  | 129.95%            | -41.25% |    -0.09 |       80 | 44.92%     | ok               |
|          50 | -14.29%  | 129.95%            | -40.84% |    -0.11 |       56 | 32.09%     | ok               |

## OP-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 27.06%   | -90.51%            | -36.11% |     0.51 |       30 | 11.11%     | ok               |
|          45 | 26.15%   | -90.51%            | -45.76% |     0.48 |       32 | 15.71%     | ok               |
|          40 | 7.79%    | -90.51%            | -53.61% |     0.29 |       46 | 24.14%     | ok               |
|          35 | -9.86%   | -90.51%            | -58.13% |     0.1  |       54 | 27.39%     | ok               |
|          30 | -26.26%  | -90.51%            | -70.11% |    -0.06 |       68 | 33.91%     | ok               |

## ORCL Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 198.34%  | 26.22%             | -29.32% |     1.25 |       74 | 65.22%     | ok               |
|          25 | 123.80%  | 26.22%             | -27.76% |     0.99 |       75 | 57.74%     | ok               |
|          20 | 119.96%  | 26.22%             | -29.32% |     0.97 |       77 | 60.90%     | ok               |
|          35 | 92.98%   | 26.22%             | -31.95% |     0.86 |       66 | 49.58%     | ok               |
|          30 | 93.15%   | 26.22%             | -29.47% |     0.86 |       72 | 53.74%     | ok               |

## OXY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -0.00%   | -8.73%             | -31.27% |     0.12 |       69 | 43.59%     | ok               |
|          50 | 0.83%    | -8.73%             | -30.54% |     0.12 |       36 | 27.79%     | ok               |
|          35 | -4.12%   | -8.73%             | -31.68% |     0.03 |       70 | 39.10%     | ok               |
|          40 | -6.47%   | -8.73%             | -33.36% |    -0.02 |       58 | 35.11%     | ok               |
|          25 | -12.78%  | -8.73%             | -40.06% |    -0.11 |       75 | 47.75%     | ok               |

## PEP Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 11.74%   | -17.71%            | -11.62% |     0.53 |       44 | 26.79%     | ok               |
|          45 | 2.18%    | -17.71%            | -14.22% |     0.14 |       64 | 31.11%     | ok               |
|          35 | -1.13%   | -17.71%            | -21.42% |     0.03 |       83 | 42.10%     | ok               |
|          40 | -1.01%   | -17.71%            | -18.04% |     0.02 |       76 | 37.10%     | ok               |
|          30 | -6.85%   | -17.71%            | -21.35% |    -0.14 |       79 | 48.75%     | ok               |

## PEPE-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -7.44%   | -73.74%            | -64.84% |     0.28 |       80 | 60.15%     | ok               |
|          30 | 0.11%    | -73.74%            | -57.66% |     0.28 |       79 | 44.83%     | ok               |
|          35 | -5.60%   | -73.74%            | -51.35% |     0.2  |       64 | 39.46%     | ok               |
|          25 | -18.07%  | -73.74%            | -53.88% |     0.12 |       85 | 50.00%     | ok               |
|          20 | -27.83%  | -73.74%            | -64.07% |     0.04 |       86 | 56.51%     | ok               |

## PFE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -24.29%  | -10.55%            | -25.27% |    -0.88 |       52 | 19.30%     | ok               |
|          35 | -32.67%  | -10.55%            | -34.05% |    -1.05 |       84 | 31.61%     | ok               |
|          50 | -26.16%  | -10.55%            | -26.99% |    -1.07 |       40 | 15.47%     | ok               |
|          40 | -31.35%  | -10.55%            | -32.26% |    -1.1  |       74 | 24.29%     | ok               |
|          30 | -39.63%  | -10.55%            | -40.87% |    -1.27 |       77 | 35.61%     | ok               |

## PG Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -5.63%   | -5.64%             | -20.08% |    -0.18 |       58 | 34.28%     | ok               |
|          35 | -8.85%   | -5.64%             | -18.99% |    -0.31 |       66 | 37.77%     | ok               |
|          45 | -14.85%  | -5.64%             | -22.43% |    -0.63 |       58 | 31.78%     | ok               |
|          30 | -17.14%  | -5.64%             | -24.55% |    -0.63 |       68 | 40.93%     | ok               |
|          25 | -18.13%  | -5.64%             | -25.42% |    -0.67 |       78 | 42.10%     | ok               |

## PM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | -0.83%   | 103.06%            | -32.20% |     0.07 |       88 | 52.41%     | ok               |
|          20 | -4.51%   | 103.06%            | -31.89% |     0    |       87 | 61.23%     | ok               |
|          30 | -4.93%   | 103.06%            | -33.68% |    -0.01 |       83 | 56.24%     | ok               |
|          50 | -6.95%   | 103.06%            | -35.70% |    -0.09 |       74 | 42.10%     | ok               |
|          40 | -8.33%   | 103.06%            | -37.94% |    -0.12 |       80 | 48.25%     | ok               |

## POL-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | 38.55%   | -75.25%            | -46.72% |     0.57 |       64 | 57.47%     | ok               |
|          30 | 36.04%   | -75.25%            | -46.45% |     0.56 |       79 | 49.62%     | ok               |
|          20 | 27.89%   | -75.25%            | -52.88% |     0.49 |       70 | 61.69%     | ok               |
|          15 | 14.13%   | -75.25%            | -58.42% |     0.38 |       72 | 66.48%     | ok               |
|          50 | -1.96%   | -75.25%            | -22.86% |     0.1  |       50 | 19.92%     | ok               |

## QCOM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -3.88%   | 24.15%             | -54.50% |     0.12 |       71 | 47.75%     | ok               |
|          35 | -4.42%   | 24.15%             | -50.58% |     0.11 |       77 | 43.59%     | ok               |
|          20 | -7.78%   | 24.15%             | -54.38% |     0.08 |       67 | 50.58%     | ok               |
|          30 | -15.25%  | 24.15%             | -56.59% |    -0.04 |       73 | 46.09%     | ok               |
|          15 | -23.11%  | 24.15%             | -57.94% |    -0.13 |       71 | 53.74%     | ok               |

## QQQ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | 21.63%   | 66.95%             | -12.88% |     0.59 |       59 | 47.42%     | ok               |
|          15 | 22.16%   | 66.95%             | -14.17% |     0.57 |       63 | 52.91%     | ok               |
|          30 | 17.66%   | 66.95%             | -12.88% |     0.52 |       64 | 44.59%     | ok               |
|          20 | 18.70%   | 66.95%             | -12.98% |     0.51 |       67 | 50.08%     | ok               |
|          35 | 5.63%    | 66.95%             | -18.29% |     0.23 |       70 | 40.93%     | ok               |

## RENDER-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 45.25%   | -62.36%            | -43.43% |     0.61 |       88 | 54.46%     | ok               |
|          15 | 32.76%   | -62.36%            | -44.59% |     0.54 |       86 | 57.62%     | ok               |
|          25 | 15.90%   | -62.36%            | -40.60% |     0.42 |       90 | 50.10%     | ok               |
|          30 | -19.07%  | -62.36%            | -45.00% |     0.1  |       98 | 43.37%     | ok               |
|          35 | -31.74%  | -62.36%            | -41.33% |    -0.12 |       84 | 35.05%     | ok               |

## RTX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 31.39%   | 113.59%            | -18.66% |     0.73 |       78 | 56.24%     | ok               |
|          25 | 26.72%   | 113.59%            | -18.59% |     0.65 |       64 | 52.75%     | ok               |
|          50 | 20.88%   | 113.59%            | -18.42% |     0.63 |       58 | 41.93%     | ok               |
|          35 | 22.16%   | 113.59%            | -18.00% |     0.63 |       56 | 49.75%     | ok               |
|          30 | 24.80%   | 113.59%            | -16.99% |     0.62 |       58 | 51.58%     | ok               |

## SBUX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -14.13%  | 13.12%             | -23.51% |    -0.27 |       58 | 33.61%     | ok               |
|          45 | -14.12%  | 13.12%             | -25.39% |    -0.3  |       66 | 29.12%     | ok               |
|          30 | -18.32%  | 13.12%             | -27.45% |    -0.34 |       62 | 39.10%     | ok               |
|          35 | -19.87%  | 13.12%             | -25.85% |    -0.39 |       56 | 36.44%     | ok               |
|          25 | -25.97%  | 13.12%             | -32.29% |    -0.45 |       62 | 41.60%     | ok               |

## SCHW Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 8.98%    | 61.68%             | -16.53% |     0.32 |       56 | 34.11%     | ok               |
|          50 | 4.78%    | 61.68%             | -13.28% |     0.22 |       50 | 31.61%     | ok               |
|          25 | -0.92%   | 61.68%             | -28.76% |     0.07 |       63 | 49.08%     | ok               |
|          40 | -2.32%   | 61.68%             | -23.35% |     0.01 |       64 | 37.10%     | ok               |
|          20 | -4.48%   | 61.68%             | -29.24% |    -0.01 |       71 | 51.58%     | ok               |

## SHIB-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -14.61%  | -72.40%            | -49.21% |     0.08 |       80 | 69.73%     | ok               |
|          20 | -26.87%  | -72.40%            | -46.92% |    -0.09 |       81 | 64.56%     | ok               |
|          25 | -27.54%  | -72.40%            | -43.85% |    -0.12 |       77 | 59.58%     | ok               |
|          35 | -27.90%  | -72.40%            | -53.32% |    -0.18 |       66 | 46.17%     | ok               |
|          40 | -31.85%  | -72.40%            | -50.74% |    -0.28 |       56 | 38.51%     | ok               |

## SHY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd    |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:-------|---------:|---------:|:-----------|:-----------------|
|          30 | -2.24%   | 0.28%              | -2.85% |    -0.79 |       48 | 34.28%     | ok               |
|          35 | -2.36%   | 0.28%              | -3.27% |    -0.84 |       50 | 32.45%     | ok               |
|          40 | -2.47%   | 0.28%              | -3.33% |    -0.89 |       50 | 30.62%     | ok               |
|          45 | -2.45%   | 0.28%              | -3.23% |    -0.9  |       48 | 27.45%     | ok               |
|          50 | -2.62%   | 0.28%              | -3.40% |    -1.01 |       44 | 24.63%     | ok               |

## SKY-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -28.56%  | -1.25%             | -43.98% |    -0.34 |       70 | 40.40%     | ok               |
|          15 | -32.92%  | -1.25%             | -56.39% |    -0.35 |       60 | 50.45%     | ok               |
|          25 | -32.22%  | -1.25%             | -48.09% |    -0.4  |       65 | 43.97%     | ok               |
|          20 | -42.55%  | -1.25%             | -58.40% |    -0.59 |       62 | 47.54%     | ok               |
|          35 | -39.77%  | -1.25%             | -49.68% |    -0.69 |       64 | 34.15%     | ok               |

## SLB Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 20.74%   | -1.07%             | -20.46% |     0.51 |       54 | 32.95%     | ok               |
|          40 | 19.16%   | -1.07%             | -23.07% |     0.47 |       46 | 36.77%     | ok               |
|          50 | -4.32%   | -1.07%             | -30.82% |    -0.02 |       52 | 28.45%     | ok               |
|          35 | -10.76%  | -1.07%             | -41.81% |    -0.12 |       74 | 44.76%     | ok               |
|          30 | -24.74%  | -1.07%             | -54.13% |    -0.41 |       77 | 51.41%     | ok               |

## SLV Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 67.45%   | 164.87%            | -34.10% |     0.86 |       52 | 34.78%     | ok               |
|          45 | 65.48%   | 164.87%            | -31.82% |     0.83 |       58 | 35.94%     | ok               |
|          40 | 63.50%   | 164.87%            | -31.93% |     0.82 |       64 | 38.10%     | ok               |
|          35 | 50.56%   | 164.87%            | -36.89% |     0.7  |       66 | 40.27%     | ok               |
|          30 | 46.07%   | 164.87%            | -42.66% |     0.66 |       58 | 42.60%     | ok               |

## SMH Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 108.06%  | 198.93%            | -30.17% |     1.27 |       47 | 51.41%     | ok               |
|          35 | 86.21%   | 198.93%            | -34.36% |     1.14 |       54 | 47.25%     | ok               |
|          25 | 86.07%   | 198.93%            | -32.94% |     1.12 |       46 | 50.25%     | ok               |
|          30 | 83.88%   | 198.93%            | -33.99% |     1.11 |       48 | 48.59%     | ok               |
|          45 | 70.50%   | 198.93%            | -32.75% |     1.06 |       52 | 41.43%     | ok               |

## SNX-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -8.06%   | -79.86%            | -43.20% |     0.19 |       71 | 47.70%     | ok               |
|          35 | -4.20%   | -79.86%            | -30.08% |     0.19 |       62 | 30.27%     | ok               |
|          30 | -13.40%  | -79.86%            | -34.76% |     0.1  |       58 | 37.36%     | ok               |
|          40 | -15.63%  | -79.86%            | -37.40% |    -0.01 |       50 | 24.52%     | ok               |
|          15 | -38.08%  | -79.86%            | -47.56% |    -0.14 |       81 | 52.30%     | ok               |

## SOL-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 5.33%    | -61.78%            | -51.50% |     0.29 |       60 | 37.55%     | ok               |
|          25 | -20.38%  | -61.78%            | -52.40% |     0.05 |       74 | 56.51%     | ok               |
|          45 | -16.11%  | -61.78%            | -59.86% |     0.03 |       62 | 31.80%     | ok               |
|          15 | -25.31%  | -61.78%            | -59.14% |     0.02 |       74 | 63.22%     | ok               |
|          35 | -22.75%  | -61.78%            | -61.91% |     0.01 |       76 | 45.21%     | ok               |

## SOXX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 91.10%   | 177.32%            | -38.67% |     1.11 |       53 | 50.08%     | ok               |
|          25 | 87.45%   | 177.32%            | -39.85% |     1.08 |       51 | 49.75%     | ok               |
|          35 | 82.21%   | 177.32%            | -38.63% |     1.06 |       59 | 45.09%     | ok               |
|          15 | 86.31%   | 177.32%            | -37.72% |     1.03 |       66 | 52.91%     | ok               |
|          30 | 76.92%   | 177.32%            | -40.34% |     1    |       55 | 47.59%     | ok               |

## SPY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 15.64%   | 50.77%             | -14.25% |     0.55 |       61 | 53.91%     | ok               |
|          15 | 14.06%   | 50.77%             | -16.80% |     0.49 |       70 | 57.07%     | ok               |
|          25 | 8.45%    | 50.77%             | -15.22% |     0.34 |       61 | 52.91%     | ok               |
|          30 | 3.86%    | 50.77%             | -16.47% |     0.19 |       64 | 50.08%     | ok               |
|          35 | 3.25%    | 50.77%             | -16.72% |     0.18 |       60 | 47.09%     | ok               |

## SUSHI-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -24.39%  | -81.43%            | -40.79% |    -0.2  |       52 | 14.56%     | ok               |
|          45 | -59.07%  | -81.43%            | -64.69% |    -0.78 |       56 | 18.01%     | ok               |
|          40 | -61.97%  | -81.43%            | -68.54% |    -0.78 |       63 | 24.52%     | ok               |
|          35 | -69.84%  | -81.43%            | -76.44% |    -0.93 |       80 | 30.08%     | ok               |
|          15 | -80.30%  | -81.43%            | -80.30% |    -1.03 |       89 | 47.13%     | ok               |

## T Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 63.62%   | 24.42%             | -18.13% |     1.21 |       58 | 56.74%     | ok               |
|          25 | 58.54%   | 24.42%             | -17.66% |     1.15 |       60 | 54.58%     | ok               |
|          15 | 54.68%   | 24.42%             | -15.08% |     1.06 |       67 | 60.57%     | ok               |
|          30 | 41.17%   | 24.42%             | -17.01% |     0.9  |       64 | 52.58%     | ok               |
|          35 | 26.66%   | 24.42%             | -14.49% |     0.67 |       66 | 49.08%     | ok               |

## TGT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -12.45%  | -8.80%             | -42.86% |    -0.13 |       83 | 46.92%     | ok               |
|          45 | -10.91%  | -8.80%             | -29.07% |    -0.18 |       52 | 29.12%     | ok               |
|          25 | -13.32%  | -8.80%             | -43.36% |    -0.18 |       65 | 41.93%     | ok               |
|          30 | -12.69%  | -8.80%             | -40.57% |    -0.18 |       60 | 39.10%     | ok               |
|          15 | -17.98%  | -8.80%             | -40.77% |    -0.24 |       73 | 51.58%     | ok               |

## TIA-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 2.90%    | -87.19%            | -46.58% |     0.22 |       52 | 18.58%     | ok               |
|          50 | 1.89%    | -87.19%            | -46.02% |     0.18 |       32 | 11.49%     | ok               |
|          35 | -14.76%  | -87.19%            | -49.70% |     0.07 |       66 | 30.84%     | ok               |
|          40 | -14.40%  | -87.19%            | -48.55% |     0.06 |       68 | 26.05%     | ok               |
|          15 | -57.93%  | -87.19%            | -61.13% |    -0.35 |       97 | 52.49%     | ok               |

## TLT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -21.65%  | -8.97%             | -21.82% |    -1.69 |       70 | 31.45%     | ok               |
|          50 | -15.00%  | -8.97%             | -15.73% |    -1.79 |       32 | 14.14%     | ok               |
|          40 | -19.85%  | -8.97%             | -19.85% |    -1.93 |       56 | 20.97%     | ok               |
|          15 | -27.39%  | -8.97%             | -27.71% |    -1.94 |       75 | 39.43%     | ok               |
|          35 | -22.42%  | -8.97%             | -22.42% |    -1.99 |       64 | 25.62%     | ok               |

## TMO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 45.99%   | -4.30%             | -8.17%  |     1.04 |       40 | 31.28%     | ok               |
|          45 | 41.75%   | -4.30%             | -10.13% |     0.91 |       46 | 36.11%     | ok               |
|          40 | 39.66%   | -4.30%             | -9.91%  |     0.86 |       49 | 40.60%     | ok               |
|          35 | 21.88%   | -4.30%             | -14.06% |     0.53 |       61 | 45.09%     | ok               |
|          30 | 14.21%   | -4.30%             | -18.85% |     0.38 |       61 | 49.75%     | ok               |

## TMUS Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 11.88%   | 12.43%             | -28.81% |     0.33 |       67 | 60.40%     | ok               |
|          30 | 7.73%    | 12.43%             | -25.69% |     0.26 |       70 | 48.42%     | ok               |
|          20 | 2.66%    | 12.43%             | -29.75% |     0.16 |       71 | 54.74%     | ok               |
|          25 | -0.78%   | 12.43%             | -31.43% |     0.08 |       75 | 50.92%     | ok               |
|          35 | -4.62%   | 12.43%             | -34.21% |    -0.01 |       70 | 45.26%     | ok               |

## TRX-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 6.87%    | 47.48%             | -18.79% |     0.28 |       52 | 37.16%     | ok               |
|          30 | 0.99%    | 47.48%             | -22.90% |     0.12 |       72 | 49.04%     | ok               |
|          50 | 0.66%    | 47.48%             | -18.49% |     0.1  |       44 | 31.99%     | ok               |
|          35 | 0.16%    | 47.48%             | -21.77% |     0.09 |       68 | 45.79%     | ok               |
|          45 | -0.23%   | 47.48%             | -18.27% |     0.07 |       44 | 33.52%     | ok               |

## TSLA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 66.54%   | 115.44%            | -30.67% |     0.78 |       62 | 34.28%     | ok               |
|          50 | 50.26%   | 115.44%            | -32.60% |     0.68 |       62 | 29.62%     | ok               |
|          45 | 41.09%   | 115.44%            | -31.89% |     0.59 |       66 | 31.61%     | ok               |
|          35 | 27.32%   | 115.44%            | -37.58% |     0.46 |       71 | 36.94%     | ok               |
|          30 | 5.29%    | 115.44%            | -42.22% |     0.25 |       69 | 40.93%     | ok               |

## TXN Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 11.38%   | 95.43%             | -45.45% |     0.3  |       70 | 34.78%     | ok               |
|          20 | 0.55%    | 95.43%             | -38.49% |     0.16 |       62 | 59.73%     | ok               |
|          15 | -5.19%   | 95.43%             | -38.99% |     0.09 |       67 | 63.56%     | ok               |
|          35 | -4.77%   | 95.43%             | -43.28% |     0.06 |       78 | 50.08%     | ok               |
|          40 | -6.74%   | 95.43%             | -45.67% |     0.03 |       72 | 47.59%     | ok               |

## UNH Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 36.64%   | -16.49%            | -26.96% |     0.59 |       74 | 52.41%     | ok               |
|          15 | 36.13%   | -16.49%            | -32.14% |     0.56 |       75 | 67.55%     | ok               |
|          35 | 32.92%   | -16.49%            | -28.32% |     0.55 |       66 | 47.25%     | ok               |
|          50 | 30.03%   | -16.49%            | -36.82% |     0.54 |       54 | 30.95%     | ok               |
|          40 | 24.66%   | -16.49%            | -35.73% |     0.47 |       60 | 42.76%     | ok               |

## UNI-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -23.75%  | -61.93%            | -58.49% |    -0.08 |       56 | 26.25%     | ok               |
|          40 | -28.37%  | -61.93%            | -63.75% |    -0.12 |       60 | 31.61%     | ok               |
|          50 | -30.36%  | -61.93%            | -57.60% |    -0.21 |       54 | 21.46%     | ok               |
|          35 | -40.52%  | -61.93%            | -68.71% |    -0.25 |       72 | 36.97%     | ok               |
|          30 | -74.83%  | -61.93%            | -80.61% |    -0.95 |       90 | 43.10%     | ok               |

## UPS Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -35.14%  | -23.21%            | -44.05% |    -0.66 |       82 | 47.92%     | ok               |
|          35 | -34.38%  | -23.21%            | -37.47% |    -0.7  |       63 | 33.78%     | ok               |
|          25 | -36.17%  | -23.21%            | -40.09% |    -0.7  |       78 | 44.43%     | ok               |
|          15 | -39.08%  | -23.21%            | -45.23% |    -0.75 |       90 | 52.75%     | ok               |
|          40 | -35.65%  | -23.21%            | -38.60% |    -0.75 |       57 | 28.45%     | ok               |

## USO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 13.41%   | 52.35%             | -33.25% |     0.34 |       48 | 25.96%     | ok               |
|          30 | 7.58%    | 52.35%             | -43.35% |     0.25 |       68 | 33.61%     | ok               |
|          40 | 3.59%    | 52.35%             | -41.14% |     0.18 |       61 | 28.79%     | ok               |
|          20 | 2.55%    | 52.35%             | -46.76% |     0.17 |       76 | 38.94%     | ok               |
|          50 | 2.10%    | 52.35%             | -31.13% |     0.15 |       50 | 23.29%     | ok               |

## VEA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 5.44%    | 48.94%             | -16.28% |     0.25 |       60 | 50.58%     | ok               |
|          20 | 1.19%    | 48.94%             | -17.70% |     0.1  |       61 | 47.92%     | ok               |
|          25 | -0.82%   | 48.94%             | -17.79% |     0.02 |       57 | 46.26%     | ok               |
|          30 | -0.98%   | 48.94%             | -17.93% |     0.01 |       58 | 44.09%     | ok               |
|          35 | -2.09%   | 48.94%             | -16.79% |    -0.03 |       56 | 43.09%     | ok               |

## VIXY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -48.04%  | -64.05%            | -69.78% |    -0.43 |       46 | 10.48%     | ok               |
|          45 | -59.37%  | -64.05%            | -75.03% |    -0.61 |       60 | 16.64%     | ok               |
|          40 | -67.66%  | -64.05%            | -80.72% |    -0.74 |       76 | 21.46%     | ok               |
|          35 | -70.62%  | -64.05%            | -84.37% |    -0.76 |       90 | 26.79%     | ok               |
|          15 | -77.15%  | -64.05%            | -89.47% |    -0.77 |      101 | 44.76%     | ok               |

## VNQ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -8.60%   | 16.54%             | -19.07% |    -0.37 |       60 | 28.62%     | ok               |
|          50 | -9.03%   | 16.54%             | -17.13% |    -0.41 |       56 | 26.12%     | ok               |
|          25 | -13.12%  | 16.54%             | -22.34% |    -0.51 |       69 | 40.77%     | ok               |
|          20 | -14.71%  | 16.54%             | -23.79% |    -0.56 |       72 | 43.43%     | ok               |
|          15 | -15.49%  | 16.54%             | -24.90% |    -0.59 |       67 | 44.76%     | ok               |

## VTI Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 18.94%   | 49.86%             | -13.96% |     0.64 |       64 | 54.91%     | ok               |
|          15 | 12.85%   | 49.86%             | -15.70% |     0.45 |       67 | 57.40%     | ok               |
|          25 | 5.19%    | 49.86%             | -16.10% |     0.24 |       60 | 52.91%     | ok               |
|          30 | -2.67%   | 49.86%             | -18.77% |    -0.04 |       68 | 50.92%     | ok               |
|          35 | -5.12%   | 49.86%             | -20.89% |    -0.13 |       62 | 47.75%     | ok               |

## VWO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -7.30%   | 46.38%             | -21.18% |    -0.25 |       60 | 32.61%     | ok               |
|          15 | -9.03%   | 46.38%             | -24.01% |    -0.26 |       69 | 49.42%     | ok               |
|          20 | -10.06%  | 46.38%             | -26.14% |    -0.31 |       67 | 47.25%     | ok               |
|          40 | -8.98%   | 46.38%             | -23.57% |    -0.31 |       70 | 37.94%     | ok               |
|          45 | -9.11%   | 46.38%             | -23.26% |    -0.33 |       62 | 35.11%     | ok               |

## VZ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -6.80%   | 5.21%              | -12.71% |    -0.19 |       50 | 24.29%     | ok               |
|          45 | -17.18%  | 5.21%              | -20.47% |    -0.57 |       62 | 27.79%     | ok               |
|          35 | -19.04%  | 5.21%              | -19.89% |    -0.61 |       63 | 33.61%     | ok               |
|          25 | -21.81%  | 5.21%              | -24.90% |    -0.63 |       81 | 41.60%     | ok               |
|          40 | -22.83%  | 5.21%              | -23.46% |    -0.78 |       66 | 30.78%     | ok               |

## WFC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -0.32%   | 79.09%             | -18.29% |     0.06 |       60 | 34.94%     | ok               |
|          35 | -6.40%   | 79.09%             | -22.53% |    -0.06 |       81 | 46.92%     | ok               |
|          20 | -13.76%  | 79.09%             | -29.87% |    -0.16 |       79 | 56.07%     | ok               |
|          45 | -9.34%   | 79.09%             | -24.02% |    -0.2  |       68 | 39.93%     | ok               |
|          30 | -16.15%  | 79.09%             | -29.78% |    -0.25 |       84 | 50.08%     | ok               |

## WIF-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 60.65%   | -80.17%            | -46.21% |     0.66 |       71 | 41.38%     | ok               |
|          20 | 54.98%   | -80.17%            | -40.67% |     0.64 |       65 | 38.70%     | ok               |
|          25 | 2.09%    | -80.17%            | -45.19% |     0.31 |       67 | 36.02%     | ok               |
|          50 | -12.13%  | -80.17%            | -33.04% |    -0.02 |       38 | 11.69%     | ok               |
|          30 | -35.28%  | -80.17%            | -50.54% |    -0.13 |       68 | 31.99%     | ok               |

## WMT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 57.03%   | 99.66%             | -9.18%  |     1.49 |       38 | 42.60%     | ok               |
|          50 | 49.42%   | 99.66%             | -12.19% |     1.4  |       32 | 40.27%     | ok               |
|          40 | 47.21%   | 99.66%             | -9.83%  |     1.26 |       42 | 43.76%     | ok               |
|          35 | 44.44%   | 99.66%             | -11.54% |     1.17 |       54 | 47.92%     | ok               |
|          30 | 20.19%   | 99.66%             | -21.31% |     0.58 |       61 | 50.58%     | ok               |

## XBI Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 18.47%   | 80.25%             | -16.56% |     0.51 |       60 | 36.11%     | ok               |
|          45 | 17.56%   | 80.25%             | -16.74% |     0.5  |       52 | 32.95%     | ok               |
|          35 | 13.86%   | 80.25%             | -18.84% |     0.4  |       62 | 39.43%     | ok               |
|          30 | 12.60%   | 80.25%             | -19.80% |     0.37 |       62 | 41.10%     | ok               |
|          50 | 7.91%    | 80.25%             | -16.83% |     0.29 |       54 | 29.62%     | ok               |

## XLB Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -1.57%   | 20.89%             | -20.60% |    -0.01 |       56 | 31.45%     | ok               |
|          50 | -1.52%   | 20.89%             | -17.40% |    -0.01 |       40 | 27.12%     | ok               |
|          45 | -4.43%   | 20.89%             | -20.61% |    -0.13 |       40 | 28.62%     | ok               |
|          35 | -4.92%   | 20.89%             | -23.62% |    -0.13 |       56 | 34.94%     | ok               |
|          25 | -8.20%   | 20.89%             | -23.73% |    -0.24 |       64 | 40.60%     | ok               |

## XLC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 11.34%   | 38.92%             | -12.33% |     0.42 |       67 | 54.91%     | ok               |
|          25 | 8.64%    | 38.92%             | -12.31% |     0.34 |       66 | 56.74%     | ok               |
|          40 | 7.53%    | 38.92%             | -13.38% |     0.32 |       68 | 47.42%     | ok               |
|          35 | 6.92%    | 38.92%             | -13.38% |     0.3  |       64 | 51.75%     | ok               |
|          20 | 1.19%    | 38.92%             | -13.41% |     0.11 |       72 | 59.57%     | ok               |

## XLE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 1.65%    | 31.62%             | -25.98% |     0.12 |       50 | 36.44%     | ok               |
|          45 | -3.59%   | 31.62%             | -30.88% |    -0.03 |       58 | 39.10%     | ok               |
|          35 | -4.60%   | 31.62%             | -32.17% |    -0.04 |       65 | 43.93%     | ok               |
|          25 | -12.10%  | 31.62%             | -37.50% |    -0.23 |       81 | 49.25%     | ok               |
|          30 | -12.12%  | 31.62%             | -37.51% |    -0.24 |       73 | 46.09%     | ok               |

## XLF Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -3.10%   | 42.05%             | -18.01% |    -0.04 |       68 | 53.91%     | ok               |
|          15 | -7.11%   | 42.05%             | -19.58% |    -0.18 |       76 | 56.74%     | ok               |
|          30 | -9.08%   | 42.05%             | -23.61% |    -0.28 |       76 | 48.25%     | ok               |
|          25 | -9.86%   | 42.05%             | -23.22% |    -0.3  |       77 | 50.42%     | ok               |
|          35 | -15.32%  | 42.05%             | -25.31% |    -0.58 |       66 | 44.76%     | ok               |

## XLI Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 5.74%    | 53.67%             | -10.36% |     0.26 |       74 | 52.08%     | ok               |
|          20 | 1.79%    | 53.67%             | -12.74% |     0.12 |       65 | 47.75%     | ok               |
|          30 | -0.44%   | 53.67%             | -11.74% |     0.03 |       66 | 45.26%     | ok               |
|          45 | -1.01%   | 53.67%             | -13.96% |     0    |       64 | 36.44%     | ok               |
|          25 | -1.65%   | 53.67%             | -12.51% |    -0.01 |       64 | 46.09%     | ok               |

## XLK Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 81.99%   | 80.94%             | -14.75% |     1.32 |       41 | 51.58%     | ok               |
|          20 | 67.76%   | 80.94%             | -14.75% |     1.19 |       48 | 49.42%     | ok               |
|          25 | 64.34%   | 80.94%             | -14.75% |     1.18 |       42 | 47.25%     | ok               |
|          30 | 62.19%   | 80.94%             | -14.75% |     1.17 |       42 | 46.09%     | ok               |
|          35 | 44.10%   | 80.94%             | -13.61% |     0.94 |       54 | 43.43%     | ok               |

## XLM-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 27.47%   | -44.15%            | -38.97% |     0.49 |       44 | 27.20%     | ok               |
|          45 | 23.64%   | -44.15%            | -43.99% |     0.45 |       50 | 30.84%     | ok               |
|          30 | 5.21%    | -44.15%            | -50.36% |     0.28 |       69 | 45.79%     | ok               |
|          40 | 2.83%    | -44.15%            | -43.80% |     0.24 |       49 | 35.25%     | ok               |
|          35 | -4.00%   | -44.15%            | -50.42% |     0.17 |       69 | 41.76%     | ok               |

## XLP Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 10.77%   | 14.44%             | -6.85%  |     0.67 |       56 | 33.61%     | ok               |
|          40 | 10.06%   | 14.44%             | -7.77%  |     0.61 |       70 | 37.94%     | ok               |
|          50 | 8.70%    | 14.44%             | -7.01%  |     0.56 |       56 | 31.28%     | ok               |
|          35 | 9.10%    | 14.44%             | -9.73%  |     0.54 |       66 | 40.93%     | ok               |
|          30 | 6.68%    | 14.44%             | -11.56% |     0.41 |       70 | 42.26%     | ok               |

## XLU Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 6.39%    | 49.71%             | -12.52% |     0.35 |       50 | 30.78%     | ok               |
|          45 | 4.27%    | 49.71%             | -14.27% |     0.25 |       54 | 31.61%     | ok               |
|          40 | 1.40%    | 49.71%             | -15.59% |     0.11 |       58 | 33.11%     | ok               |
|          35 | -6.17%   | 49.71%             | -19.71% |    -0.25 |       64 | 35.44%     | ok               |
|          30 | -7.04%   | 49.71%             | -20.40% |    -0.28 |       69 | 38.60%     | ok               |

## XLV Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -13.36%  | 12.54%             | -18.00% |    -0.66 |       68 | 35.94%     | ok               |
|          25 | -14.64%  | 12.54%             | -19.21% |    -0.73 |       70 | 37.27%     | ok               |
|          15 | -18.51%  | 12.54%             | -22.57% |    -0.9  |       81 | 42.10%     | ok               |
|          20 | -18.44%  | 12.54%             | -22.66% |    -0.93 |       75 | 38.94%     | ok               |
|          50 | -15.66%  | 12.54%             | -19.39% |    -0.95 |       56 | 24.63%     | ok               |

## XLY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 5.14%    | 31.27%             | -12.94% |     0.23 |       70 | 41.43%     | ok               |
|          30 | 3.26%    | 31.27%             | -14.01% |     0.17 |       70 | 44.43%     | ok               |
|          15 | 1.20%    | 31.27%             | -15.77% |     0.11 |       74 | 51.25%     | ok               |
|          50 | 1.30%    | 31.27%             | -11.79% |     0.1  |       50 | 29.62%     | ok               |
|          40 | -1.91%   | 31.27%             | -16.99% |    -0.01 |       68 | 37.10%     | ok               |

## XOM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 4.35%    | 36.31%             | -21.35% |     0.2  |       42 | 29.45%     | ok               |
|          25 | -0.59%   | 36.31%             | -19.90% |     0.06 |       57 | 37.77%     | ok               |
|          30 | -1.58%   | 36.31%             | -20.29% |     0.03 |       57 | 37.10%     | ok               |
|          20 | -4.27%   | 36.31%             | -25.56% |    -0.04 |       62 | 40.27%     | ok               |
|          40 | -4.30%   | 36.31%             | -21.45% |    -0.05 |       54 | 34.78%     | ok               |

## XRP-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | -25.11%  | -56.20%            | -46.87% |    -0.14 |       68 | 39.85%     | ok               |
|          40 | -30.47%  | -56.20%            | -44.89% |    -0.26 |       58 | 33.72%     | ok               |
|          30 | -37.23%  | -56.20%            | -54.70% |    -0.33 |       70 | 44.06%     | ok               |
|          45 | -38.24%  | -56.20%            | -46.06% |    -0.42 |       58 | 29.50%     | ok               |
|          50 | -34.88%  | -56.20%            | -38.03% |    -0.46 |       60 | 22.03%     | ok               |

## YFI-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -48.10%  | -64.53%            | -53.01% |    -0.77 |       62 | 27.20%     | ok               |
|          45 | -42.00%  | -64.53%            | -54.04% |    -0.79 |       64 | 22.22%     | ok               |
|          35 | -62.85%  | -64.53%            | -66.36% |    -1.07 |       73 | 34.48%     | ok               |
|          30 | -65.22%  | -64.53%            | -70.46% |    -1.07 |       83 | 40.61%     | ok               |
|          25 | -68.76%  | -64.53%            | -71.71% |    -1.16 |       77 | 45.59%     | ok               |

## ZEC-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 92.70%   | 1425.64%           | -24.66% |     0.79 |       46 | 22.22%     | ok               |
|          35 | 65.45%   | 1425.64%           | -44.34% |     0.66 |       54 | 28.74%     | ok               |
|          25 | 47.29%   | 1425.64%           | -48.59% |     0.58 |       60 | 37.93%     | ok               |
|          30 | 32.72%   | 1425.64%           | -47.68% |     0.5  |       64 | 34.48%     | ok               |
|          40 | 31.32%   | 1425.64%           | -48.16% |     0.48 |       56 | 26.05%     | ok               |
