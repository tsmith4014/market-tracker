# Market Tracker Backtest Report

_Generated: 2026-06-24T01:25:26+00:00_

## Data Sources

- Crypto: Kraken -> Coinbase -> CoinGecko OHLC -> CoinPaprika fallback chain.
- Stocks / ETFs / indices: Stooq -> Yahoo Finance fallback chain.
- Data rows are generated from real market APIs. Mock OHLCV rows are not generated.

## Data Freshness

- Rows: **92,424**
- Symbols: **161**
- Date range: **2024-01-30** to **2026-06-24**

## Latest Signals

| symbol     | date                |         close |   composite_score | signal   | data_source   |
|:-----------|:--------------------|--------------:|------------------:|:---------|:--------------|
| AMAT       | 2026-06-23 00:00:00 |   585.88      |         67.0833   | LONG     | Yahoo Finance |
| BAC        | 2026-06-23 00:00:00 |    57.91      |         62.25     | LONG     | Yahoo Finance |
| C          | 2026-06-23 00:00:00 |   144.97      |         67.0833   | LONG     | Yahoo Finance |
| CAT        | 2026-06-23 00:00:00 |   984.24      |         69.9167   | LONG     | Yahoo Finance |
| CSCO       | 2026-06-23 00:00:00 |   121.15      |         36.4167   | LONG     | Yahoo Finance |
| DE         | 2026-06-23 00:00:00 |   591.94      |         70.4167   | LONG     | Yahoo Finance |
| DXY-INDEX  | 2026-06-23 00:00:00 |   101.429     |         83.0645   | LONG     | Yahoo Finance |
| GE         | 2026-06-23 00:00:00 |   356.47      |         58.0833   | LONG     | Yahoo Finance |
| GS         | 2026-06-23 00:00:00 |  1094.44      |         47.4167   | LONG     | Yahoo Finance |
| ITA        | 2026-06-23 00:00:00 |   235.93      |         52.4167   | LONG     | Yahoo Finance |
| JPM        | 2026-06-23 00:00:00 |   334.14      |         60.5833   | LONG     | Yahoo Finance |
| LLY        | 2026-06-23 00:00:00 |  1107.08      |         34.25     | LONG     | Yahoo Finance |
| LRCX       | 2026-06-23 00:00:00 |   371.33      |         65.4167   | LONG     | Yahoo Finance |
| MS         | 2026-06-23 00:00:00 |   226.03      |         69.9167   | LONG     | Yahoo Finance |
| PG         | 2026-06-23 00:00:00 |   150.86      |         82.8333   | LONG     | Yahoo Finance |
| PM         | 2026-06-23 00:00:00 |   178.69      |         48.75     | LONG     | Yahoo Finance |
| RTX        | 2026-06-23 00:00:00 |   186.39      |         67.5833   | LONG     | Yahoo Finance |
| SBUX       | 2026-06-23 00:00:00 |   101.05      |         67.4167   | LONG     | Yahoo Finance |
| SCHW       | 2026-06-23 00:00:00 |    93.17      |         67.6667   | LONG     | Yahoo Finance |
| TIA-USD    | 2026-06-24 00:00:00 |     0.3832    |         41.75     | LONG     | Kraken API    |
| TRX-USD    | 2026-06-24 00:00:00 |     0.328604  |         51.4167   | LONG     | Kraken API    |
| UNH        | 2026-06-23 00:00:00 |   409.25      |         57.4167   | LONG     | Yahoo Finance |
| WFC        | 2026-06-23 00:00:00 |    84.13      |         56.6667   | LONG     | Yahoo Finance |
| WMT        | 2026-06-23 00:00:00 |   119.42      |         35.6667   | LONG     | Yahoo Finance |
| XLF        | 2026-06-23 00:00:00 |    53.88      |         65.4167   | LONG     | Yahoo Finance |
| AAPL       | 2026-06-23 00:00:00 |   294.3       |         -2.08333  | NEUTRAL  | Yahoo Finance |
| AAVE-USD   | 2026-06-24 00:00:00 |    72.32      |         -6.66667  | NEUTRAL  | Kraken API    |
| ABBV       | 2026-06-23 00:00:00 |   234.76      |         54.3333   | NEUTRAL  | Yahoo Finance |
| ADA-USD    | 2026-06-24 00:00:00 |     0.152535  |        -20.6667   | NEUTRAL  | Kraken API    |
| AGG        | 2026-06-23 00:00:00 |    98.71      |         -2.25     | NEUTRAL  | Yahoo Finance |
| ALGO-USD   | 2026-06-24 00:00:00 |     0.09538   |          0.666667 | NEUTRAL  | Kraken API    |
| AMD        | 2026-06-23 00:00:00 |   519.85      |         24.1667   | NEUTRAL  | Yahoo Finance |
| AMGN       | 2026-06-23 00:00:00 |   347.01      |         69.4167   | NEUTRAL  | Yahoo Finance |
| AMZN       | 2026-06-23 00:00:00 |   234.11      |        -11.8333   | NEUTRAL  | Yahoo Finance |
| APT-USD    | 2026-06-24 00:00:00 |     0.6517    |         -2.83333  | NEUTRAL  | Kraken API    |
| ARB-USD    | 2026-06-24 00:00:00 |     0.0786    |         -6.5      | NEUTRAL  | Kraken API    |
| ARKK       | 2026-06-23 00:00:00 |    76.68      |        -23.25     | NEUTRAL  | Yahoo Finance |
| ATOM-USD   | 2026-06-24 00:00:00 |     1.7152    |        -48.9167   | NEUTRAL  | Kraken API    |
| AVAX-USD   | 2026-06-24 00:00:00 |     6.48      |        -10.3333   | NEUTRAL  | Kraken API    |
| AVGO       | 2026-06-23 00:00:00 |   380.15      |        -50.5833   | NEUTRAL  | Yahoo Finance |
| BA         | 2026-06-23 00:00:00 |   216.71      |        -35.4167   | NEUTRAL  | Yahoo Finance |
| BLK        | 2026-06-23 00:00:00 |  1015.33      |        -24.4167   | NEUTRAL  | Yahoo Finance |
| BND        | 2026-06-23 00:00:00 |    73.22      |        -12.5833   | NEUTRAL  | Yahoo Finance |
| BONK-USD   | 2026-06-24 00:00:00 |     4.4e-06   |         -4.83333  | NEUTRAL  | Kraken API    |
| BTC-USD    | 2026-06-24 00:00:00 | 62822.7       |         -2.83333  | NEUTRAL  | Kraken API    |
| CL         | 2026-06-23 00:00:00 |    91.43      |         67.8333   | NEUTRAL  | Yahoo Finance |
| COMP-USD   | 2026-06-24 00:00:00 |    16.94      |        -14.5      | NEUTRAL  | Kraken API    |
| COP        | 2026-06-23 00:00:00 |   109.97      |        -21.0833   | NEUTRAL  | Yahoo Finance |
| COST       | 2026-06-23 00:00:00 |   957.68      |         -8.16667  | NEUTRAL  | Yahoo Finance |
| CVX        | 2026-06-23 00:00:00 |   175.98      |        -22.75     | NEUTRAL  | Yahoo Finance |
| DASH-USD   | 2026-06-24 00:00:00 |    36.397     |        -30.25     | NEUTRAL  | Kraken API    |
| DBC        | 2026-06-23 00:00:00 |    27.12      |        -17.0833   | NEUTRAL  | Yahoo Finance |
| DIA        | 2026-06-23 00:00:00 |   516.62      |         19.3333   | NEUTRAL  | Yahoo Finance |
| DIS        | 2026-06-23 00:00:00 |   103.53      |         26.1667   | NEUTRAL  | Yahoo Finance |
| DOGE-USD   | 2026-06-24 00:00:00 |     0.0790248 |        -35.75     | NEUTRAL  | Kraken API    |
| DOT-USD    | 2026-06-24 00:00:00 |     0.9106    |        -15        | NEUTRAL  | Kraken API    |
| EEM        | 2026-06-23 00:00:00 |    67.17      |          9        | NEUTRAL  | Yahoo Finance |
| EFA        | 2026-06-23 00:00:00 |   102.46      |        -36.3333   | NEUTRAL  | Yahoo Finance |
| EOG        | 2026-06-23 00:00:00 |   134.9       |        -20.8333   | NEUTRAL  | Yahoo Finance |
| ETC-USD    | 2026-06-24 00:00:00 |     7.076     |         -2.5      | NEUTRAL  | Kraken API    |
| ETH-USD    | 2026-06-24 00:00:00 |  1665.12      |        -18        | NEUTRAL  | Kraken API    |
| EWJ        | 2026-06-23 00:00:00 |    92.75      |         14.1667   | NEUTRAL  | Yahoo Finance |
| FCX        | 2026-06-23 00:00:00 |    64.4       |        -15.3333   | NEUTRAL  | Yahoo Finance |
| FIL-USD    | 2026-06-24 00:00:00 |     0.786     |          0.666667 | NEUTRAL  | Kraken API    |
| GOOGL      | 2026-06-23 00:00:00 |   346.13      |        -28.5833   | NEUTRAL  | Yahoo Finance |
| GRT-USD    | 2026-06-24 00:00:00 |     0.01892   |         -2.83333  | NEUTRAL  | Kraken API    |
| HBAR-USD   | 2026-06-24 00:00:00 |     0.07794   |        -12.0833   | NEUTRAL  | Kraken API    |
| HD         | 2026-06-23 00:00:00 |   324.45      |         15.9167   | NEUTRAL  | Yahoo Finance |
| HON        | 2026-06-23 00:00:00 |   222.37      |          3.75     | NEUTRAL  | Yahoo Finance |
| HYG        | 2026-06-23 00:00:00 |    79.87      |        -46.75     | NEUTRAL  | Yahoo Finance |
| IBM        | 2026-06-23 00:00:00 |   264.94      |         -0.666667 | NEUTRAL  | Yahoo Finance |
| ICP-USD    | 2026-06-24 00:00:00 |     2.208     |        -34.0833   | NEUTRAL  | Kraken API    |
| IEF        | 2026-06-23 00:00:00 |    94.12      |        -43        | NEUTRAL  | Yahoo Finance |
| IEMG       | 2026-06-23 00:00:00 |    81.32      |         -4.33333  | NEUTRAL  | Yahoo Finance |
| INJ-USD    | 2026-06-24 00:00:00 |     4.534     |        -59.8333   | NEUTRAL  | Kraken API    |
| INTC       | 2026-06-23 00:00:00 |   132.28      |         52.3333   | NEUTRAL  | Yahoo Finance |
| IWM        | 2026-06-23 00:00:00 |   295.32      |         38.8333   | NEUTRAL  | Yahoo Finance |
| JNJ        | 2026-06-23 00:00:00 |   239.08      |         67.8333   | NEUTRAL  | Yahoo Finance |
| KO         | 2026-06-23 00:00:00 |    80.31      |         54.5      | NEUTRAL  | Yahoo Finance |
| LDO-USD    | 2026-06-24 00:00:00 |     0.259     |         -6.5      | NEUTRAL  | Kraken API    |
| LIN        | 2026-06-23 00:00:00 |   512.26      |         60.8333   | NEUTRAL  | Yahoo Finance |
| LINK-USD   | 2026-06-24 00:00:00 |     7.60027   |        -15.75     | NEUTRAL  | Kraken API    |
| LTC-USD    | 2026-06-24 00:00:00 |    42.16      |         -4.5      | NEUTRAL  | Kraken API    |
| MCD        | 2026-06-23 00:00:00 |   271.66      |        -55.5      | NEUTRAL  | Yahoo Finance |
| META       | 2026-06-23 00:00:00 |   562.2       |        -67.3333   | NEUTRAL  | Yahoo Finance |
| MPC        | 2026-06-23 00:00:00 |   248.52      |         -1.25     | NEUTRAL  | Yahoo Finance |
| MRK        | 2026-06-23 00:00:00 |   119.6       |         48.3333   | NEUTRAL  | Yahoo Finance |
| MU         | 2026-06-23 00:00:00 |  1051.77      |         31.5      | NEUTRAL  | Yahoo Finance |
| NEAR-USD   | 2026-06-24 00:00:00 |     1.9797    |         -4.33333  | NEUTRAL  | Kraken API    |
| NEM        | 2026-06-23 00:00:00 |    97.84      |        -53.1667   | NEUTRAL  | Yahoo Finance |
| NKE        | 2026-06-23 00:00:00 |    42.38      |        -55.8333   | NEUTRAL  | Yahoo Finance |
| NVDA       | 2026-06-23 00:00:00 |   200.04      |        -43.25     | NEUTRAL  | Yahoo Finance |
| OP-USD     | 2026-06-24 00:00:00 |     0.1015    |        -14.0833   | NEUTRAL  | Kraken API    |
| OXY        | 2026-06-23 00:00:00 |    52.23      |        -14.8333   | NEUTRAL  | Yahoo Finance |
| PEP        | 2026-06-23 00:00:00 |   142.05      |         -9.83333  | NEUTRAL  | Yahoo Finance |
| PEPE-USD   | 2026-06-24 00:00:00 |     2.7e-06   |         -4.5      | NEUTRAL  | Kraken API    |
| PFE        | 2026-06-23 00:00:00 |    24.72      |        -57.75     | NEUTRAL  | Yahoo Finance |
| POL-USD    | 2026-06-24 00:00:00 |     0.07721   |         -2.83333  | NEUTRAL  | Kraken API    |
| QCOM       | 2026-06-23 00:00:00 |   204.13      |          0.416667 | NEUTRAL  | Yahoo Finance |
| QQQ        | 2026-06-23 00:00:00 |   713.65      |         -4.33333  | NEUTRAL  | Yahoo Finance |
| RENDER-USD | 2026-06-24 00:00:00 |     1.594     |        -34.9167   | NEUTRAL  | Kraken API    |
| SHIB-USD   | 2026-06-24 00:00:00 |     4.568e-06 |        -27.9167   | NEUTRAL  | Kraken API    |
| SHY        | 2026-06-23 00:00:00 |    81.97      |        -40.25     | NEUTRAL  | Yahoo Finance |
| SKY-USD    | 2026-06-24 00:00:00 |     0.05561   |        -22.5      | NEUTRAL  | Kraken API    |
| SLB        | 2026-06-23 00:00:00 |    47.79      |        -16.8333   | NEUTRAL  | Yahoo Finance |
| SMH        | 2026-06-23 00:00:00 |   622.05      |         27.6667   | NEUTRAL  | Yahoo Finance |
| SNX-USD    | 2026-06-24 00:00:00 |     0.2286    |        -20.6667   | NEUTRAL  | Kraken API    |
| SOL-USD    | 2026-06-24 00:00:00 |    69.64      |          0.666667 | NEUTRAL  | Kraken API    |
| SOXX       | 2026-06-23 00:00:00 |   603.39      |         37.5      | NEUTRAL  | Yahoo Finance |
| SPY        | 2026-06-23 00:00:00 |   733.58      |         -9.08333  | NEUTRAL  | Yahoo Finance |
| SUSHI-USD  | 2026-06-24 00:00:00 |     0.166     |        -37.75     | NEUTRAL  | Kraken API    |
| TGT        | 2026-06-23 00:00:00 |   134.11      |         63.3333   | NEUTRAL  | Yahoo Finance |
| TLT        | 2026-06-23 00:00:00 |    86.2       |         24.1667   | NEUTRAL  | Yahoo Finance |
| TMUS       | 2026-06-23 00:00:00 |   184.57      |        -18.25     | NEUTRAL  | Yahoo Finance |
| TXN        | 2026-06-23 00:00:00 |   304.36      |         26.6667   | NEUTRAL  | Yahoo Finance |
| UNI-USD    | 2026-06-24 00:00:00 |     2.9356    |         16.5      | NEUTRAL  | Kraken API    |
| UPS        | 2026-06-23 00:00:00 |   105.83      |         20.1667   | NEUTRAL  | Yahoo Finance |
| USO        | 2026-06-23 00:00:00 |   111.26      |        -21.0833   | NEUTRAL  | Yahoo Finance |
| VEA        | 2026-06-23 00:00:00 |    70.17      |         -2.33333  | NEUTRAL  | Yahoo Finance |
| VIXY       | 2026-06-23 00:00:00 |    22.98      |         -7.25     | NEUTRAL  | Yahoo Finance |
| VNQ        | 2026-06-23 00:00:00 |    97.86      |         52        | NEUTRAL  | Yahoo Finance |
| VTI        | 2026-06-23 00:00:00 |   363.7       |         -7.08333  | NEUTRAL  | Yahoo Finance |
| VWO        | 2026-06-23 00:00:00 |    59.36      |         -9        | NEUTRAL  | Yahoo Finance |
| VZ         | 2026-06-23 00:00:00 |    46.73      |         17.4167   | NEUTRAL  | Yahoo Finance |
| WIF-USD    | 2026-06-24 00:00:00 |     0.1572    |         -4.83333  | NEUTRAL  | Kraken API    |
| XBI        | 2026-06-23 00:00:00 |   147.03      |         59.5      | NEUTRAL  | Yahoo Finance |
| XLB        | 2026-06-23 00:00:00 |    50.87      |          5.33333  | NEUTRAL  | Yahoo Finance |
| XLE        | 2026-06-23 00:00:00 |    54.46      |        -22.25     | NEUTRAL  | Yahoo Finance |
| XLI        | 2026-06-23 00:00:00 |   178.15      |         60.6667   | NEUTRAL  | Yahoo Finance |
| XLK        | 2026-06-23 00:00:00 |   184.19      |          4.66667  | NEUTRAL  | Yahoo Finance |
| XLM-USD    | 2026-06-24 00:00:00 |     0.196112  |        -10.4167   | NEUTRAL  | Kraken API    |
| XLP        | 2026-06-23 00:00:00 |    83.72      |         22.0833   | NEUTRAL  | Yahoo Finance |
| XLU        | 2026-06-23 00:00:00 |    45.07      |         44.4167   | NEUTRAL  | Yahoo Finance |
| XLV        | 2026-06-23 00:00:00 |   152.18      |         36.0833   | NEUTRAL  | Yahoo Finance |
| XLY        | 2026-06-23 00:00:00 |   113.76      |        -64.0833   | NEUTRAL  | Yahoo Finance |
| XOM        | 2026-06-23 00:00:00 |   139.73      |        -20.5833   | NEUTRAL  | Yahoo Finance |
| XRP-USD    | 2026-06-24 00:00:00 |     1.10674   |        -14.0833   | NEUTRAL  | Kraken API    |
| YFI-USD    | 2026-06-24 00:00:00 |  1756.1       |        -27.9167   | NEUTRAL  | Kraken API    |
| ZEC-USD    | 2026-06-24 00:00:00 |   417.25      |          8.41667  | NEUTRAL  | Kraken API    |
| ADBE       | 2026-06-23 00:00:00 |   197.43      |        -63.0833   | SHORT    | Yahoo Finance |
| BCH-USD    | 2026-06-24 00:00:00 |   194.55      |        -35        | SHORT    | Kraken API    |
| BITO       | 2026-06-23 00:00:00 |     8.47      |        -35.75     | SHORT    | Yahoo Finance |
| CMCSA      | 2026-06-23 00:00:00 |    22.8       |        -40.0833   | SHORT    | Yahoo Finance |
| CRM        | 2026-06-23 00:00:00 |   153.42      |        -61.0833   | SHORT    | Yahoo Finance |
| CRV-USD    | 2026-06-24 00:00:00 |     0.20384   |        -33.5      | SHORT    | Kraken API    |
| FET-USD    | 2026-06-24 00:00:00 |     0.1745    |        -36        | SHORT    | Kraken API    |
| FXI        | 2026-06-23 00:00:00 |    32.83      |        -59.5833   | SHORT    | Yahoo Finance |
| GDX        | 2026-06-23 00:00:00 |    77.66      |        -37.4167   | SHORT    | Yahoo Finance |
| GDXJ       | 2026-06-23 00:00:00 |   100.56      |        -39.4167   | SHORT    | Yahoo Finance |
| GLD        | 2026-06-23 00:00:00 |   377.32      |        -53.25     | SHORT    | Yahoo Finance |
| IBIT       | 2026-06-23 00:00:00 |    35.31      |        -35.75     | SHORT    | Yahoo Finance |
| INTU       | 2026-06-23 00:00:00 |   258.05      |        -60.5833   | SHORT    | Yahoo Finance |
| MSFT       | 2026-06-23 00:00:00 |   373.94      |        -61.0833   | SHORT    | Yahoo Finance |
| NFLX       | 2026-06-23 00:00:00 |    72.82      |        -59.4167   | SHORT    | Yahoo Finance |
| NOW        | 2026-06-23 00:00:00 |    95.94      |        -58.5833   | SHORT    | Yahoo Finance |
| ORCL       | 2026-06-23 00:00:00 |   165.16      |        -69.5833   | SHORT    | Yahoo Finance |
| SLV        | 2026-06-23 00:00:00 |    55.73      |        -61.9167   | SHORT    | Yahoo Finance |
| T          | 2026-06-23 00:00:00 |    22.81      |        -51.9167   | SHORT    | Yahoo Finance |
| TMO        | 2026-06-23 00:00:00 |   469.35      |        -49.0833   | SHORT    | Yahoo Finance |
| TSLA       | 2026-06-23 00:00:00 |   381.61      |        -55.75     | SHORT    | Yahoo Finance |
| XLC        | 2026-06-23 00:00:00 |   107.27      |        -55.4167   | SHORT    | Yahoo Finance |

## Edge Summary

- Symbols with trades: **160** of 160
- Beat buy-and-hold: **36.25%** of traded symbols
- Positive return: **32.50%** of traded symbols
- Median strategy return: **-9.44%** (benchmark **14.37%**)
- Median excess vs benchmark: **-25.92%**
- Median Sharpe: **-0.08**
- Median exposure: **44.61%**

> Edge is real only if both _beat buy-and-hold_ and _median excess_ are convincingly positive across many symbols. Treat a single high-return symbol as noise.

## Portfolio Backtest

Actual capital-allocation books (not per-symbol averages). Benchmarks: `equal_weight_buyhold` (whole tracked universe), `spy_buyhold` (100% SPY), and `sixty_forty` (60% SPY / 40% AGG). `high_conf_voltarget` inverse-vol-weights the HIGH-confidence book; `conviction_long_short` is market-neutral. Judge on **Sharpe** and **max_drawdown** out-of-sample, not raw return: a fully-invested long book wins on return in a bull market but carries all the risk.

| strategy              | scope         | ann_return   | ann_vol   |   sharpe | max_drawdown   | total_return   |   avg_gross_exposure |
|:----------------------|:--------------|:-------------|:----------|---------:|:---------------|:---------------|---------------------:|
| equal_weight_buyhold  | full          | -8.49%       | 33.44%    |    -0.25 | -55.28%        | -35.00%        |                 1    |
| equal_weight_buyhold  | out_of_sample | -9.69%       | 34.24%    |    -0.28 | -39.63%        | -15.28%        |                 1    |
| all_signals_ew        | full          | -8.91%       | 28.12%    |    -0.32 | -59.63%        | -32.46%        |                 1    |
| all_signals_ew        | out_of_sample | 6.79%        | 28.53%    |     0.24 | -24.06%        | 2.98%          |                 1    |
| high_conf_ew          | full          | 5.15%        | 32.39%    |     0.16 | -46.26%        | -0.06%         |                 0.89 |
| high_conf_ew          | out_of_sample | 16.97%       | 35.23%    |     0.48 | -20.80%        | 12.35%         |                 0.89 |
| high_conf_voltarget   | full          | 5.35%        | 29.99%    |     0.18 | -39.23%        | 2.91%          |                 0.89 |
| high_conf_voltarget   | out_of_sample | 9.03%        | 32.76%    |     0.28 | -16.98%        | 4.14%          |                 0.89 |
| conviction_long_short | full          | -10.37%      | 23.55%    |    -0.44 | -37.36%        | -33.04%        |                 0.97 |
| conviction_long_short | out_of_sample | -12.62%      | 26.77%    |    -0.47 | -21.16%        | -15.91%        |                 0.97 |
| spy_buyhold           | full          | 7.30%        | 13.41%    |     0.54 | -17.81%        | 21.53%         |                 0.78 |
| spy_buyhold           | out_of_sample | -3.95%       | 10.09%    |    -0.39 | -14.83%        | -4.65%         |                 0.78 |
| sixty_forty           | full          | 4.12%        | 8.49%     |     0.49 | -10.80%        | 12.14%         |                 0.78 |
| sixty_forty           | out_of_sample | -3.37%       | 6.56%     |    -0.51 | -10.06%        | -3.75%         |                 0.78 |

## Walk-Forward Robustness

Each book measured across contiguous time folds (each a different regime). A book has durable edge only if `mean_sharpe` is positive, `min_sharpe` isn't deeply negative, and `pct_positive_folds` is high — a single great fold doesn't count. `fold_sharpes` lists each fold oldest-to-newest.

| strategy              |   n_folds |   mean_sharpe |   median_sharpe |   min_sharpe | pct_positive_folds   | mean_return   | fold_sharpes                 |
|:----------------------|----------:|--------------:|----------------:|-------------:|:---------------------|:--------------|:-----------------------------|
| equal_weight_buyhold  |         5 |         -0.03 |           -0.2  |        -1.44 | 40.00%               | -5.99%        | 1.25;-1.44;1.09;-0.86;-0.20  |
| all_signals_ew        |         5 |         -0.21 |            0.17 |        -1.33 | 60.00%               | -6.23%        | 0.17;0.60;-1.18;-1.33;0.66   |
| high_conf_ew          |         5 |          0.38 |            0.6  |        -0.77 | 60.00%               | 0.86%         | 1.28;0.60;-0.77;-0.11;0.91   |
| high_conf_voltarget   |         5 |          0.48 |            0.47 |        -0.86 | 60.00%               | 1.35%         | 1.98;0.81;-0.86;-0.00;0.47   |
| conviction_long_short |         5 |         -0.45 |           -0.31 |        -1.48 | 20.00%               | -7.45%        | -1.48;0.24;-0.31;-0.70;-0.02 |
| spy_buyhold           |         5 |          0.53 |            0.34 |        -0.25 | 60.00%               | 4.11%         | 1.39;1.26;0.34;-0.07;-0.25   |
| sixty_forty           |         5 |          0.46 |            0.37 |        -0.44 | 80.00%               | 2.37%         | 1.49;0.86;0.37;0.00;-0.44    |

## Strategy Comparison

Each decision rule backtested over the same data. `out_of_sample` is the most recent ~35% of each symbol's history (unseen tail). A rule has real edge only if `median_excess` and `beat_benchmark_pct` stay positive out-of-sample, not just full-sample.

| strategy        | scope         |   symbols | beat_benchmark_pct   | positive_pct   | median_return   | median_benchmark   | median_excess   |   median_sharpe |   total_trades |
|:----------------|:--------------|----------:|:---------------------|:---------------|:----------------|:-------------------|:----------------|----------------:|---------------:|
| trend           | full          |       160 | 36.25%               | 32.50%         | -9.44%          | 14.37%             | -25.92%         |           -0.08 |          11211 |
| trend           | out_of_sample |       160 | 38.12%               | 55.00%         | 3.69%           | 3.09%              | -6.66%          |            0.39 |           3914 |
| mean_reversion  | full          |       157 | 42.04%               | 49.04%         | -0.10%          | 14.14%             | -16.06%         |           -0.01 |           1244 |
| mean_reversion  | out_of_sample |       128 | 47.66%               | 57.81%         | 0.33%           | 0.66%              | -1.75%          |            0.67 |            474 |
| regime_adaptive | full          |       160 | 36.88%               | 33.12%         | -9.41%          | 14.37%             | -25.52%         |           -0.08 |          11486 |
| regime_adaptive | out_of_sample |       160 | 37.50%               | 55.62%         | 3.77%           | 3.09%              | -7.02%          |            0.41 |           4017 |

## Signal Calibration

Realized forward return in the signal's direction, grouped by confidence. HIGH should outrank LOW for the confidence score to be meaningful.

| confidence_level   |   horizon |     n | mean_return   | median_return   | win_rate   |
|:-------------------|----------:|------:|:--------------|:----------------|:-----------|
| HIGH               |         5 |  8185 | 0.18%         | 0.14%           | 52.30%     |
| MEDIUM             |         5 | 29231 | 0.08%         | 0.11%           | 51.19%     |
| LOW                |         5 |  3268 | -0.60%        | -0.52%          | 44.86%     |
| ALL                |         5 | 40684 | 0.05%         | 0.07%           | 50.91%     |
| HIGH               |        10 |  8149 | 0.48%         | 0.18%           | 52.19%     |
| MEDIUM             |        10 | 29036 | 0.25%         | 0.16%           | 51.31%     |
| LOW                |        10 |  3251 | -0.87%        | -0.73%          | 45.25%     |
| ALL                |        10 | 40436 | 0.21%         | 0.11%           | 51.00%     |
| HIGH               |        20 |  8064 | 0.90%         | 0.50%           | 53.79%     |
| MEDIUM             |        20 | 28498 | 0.95%         | 0.65%           | 53.75%     |
| LOW                |        20 |  3201 | -0.63%        | -0.51%          | 47.11%     |
| ALL                |        20 | 39763 | 0.81%         | 0.54%           | 53.23%     |

## Backtest Summary

### Data Quality / Signal Availability

- **ok**: 160 symbols

| symbol     |   trades | return   | benchmark_return   | mdd     |   sharpe | exposure   | skipped_reason   |
|:-----------|---------:|:---------|:-------------------|:--------|---------:|:-----------|:-----------------|
| AAPL       |       61 | 15.16%   | 56.51%             | -20.65% |     0.4  | 48.25%     | ok               |
| AAVE-USD   |       74 | -58.05%  | -76.60%            | -68.72% |    -0.65 | 36.21%     | ok               |
| ABBV       |       64 | -14.37%  | 42.35%             | -30.55% |    -0.27 | 48.25%     | ok               |
| ADA-USD    |       86 | -82.46%  | -84.63%            | -89.37% |    -0.65 | 46.55%     | ok               |
| ADBE       |       68 | -23.18%  | -68.56%            | -38.01% |    -0.24 | 57.40%     | ok               |
| AGG        |       69 | -6.61%   | 0.06%              | -10.16% |    -1.1  | 31.11%     | ok               |
| ALGO-USD   |       86 | -50.43%  | -76.01%            | -53.13% |    -0.57 | 38.12%     | ok               |
| AMAT       |       69 | -18.58%  | 252.43%            | -57.21% |    -0.08 | 53.41%     | ok               |
| AMD        |       56 | 4.27%    | 202.13%            | -46.37% |     0.25 | 37.60%     | ok               |
| AMGN       |       71 | -20.65%  | 10.29%             | -34.14% |    -0.41 | 47.42%     | ok               |
| AMZN       |       76 | -34.23%  | 47.24%             | -42.48% |    -1    | 38.44%     | ok               |
| APT-USD    |       76 | -26.57%  | -92.31%            | -69.96% |    -0    | 44.25%     | ok               |
| ARB-USD    |       68 | -0.31%   | -88.73%            | -62.67% |     0.24 | 39.27%     | ok               |
| ARKK       |       81 | -32.67%  | 63.64%             | -35.19% |    -0.57 | 38.94%     | ok               |
| ATOM-USD   |       88 | -67.30%  | -70.89%            | -73.34% |    -1.1  | 44.64%     | ok               |
| AVAX-USD   |       74 | -32.75%  | -81.82%            | -60.43% |    -0.21 | 39.85%     | ok               |
| AVGO       |       60 | 31.85%   | 214.65%            | -35.76% |     0.5  | 44.93%     | ok               |
| BA         |       69 | 2.44%    | 8.12%              | -30.56% |     0.17 | 49.58%     | ok               |
| BAC        |       78 | -12.47%  | 66.46%             | -27.64% |    -0.27 | 47.25%     | ok               |
| BCH-USD    |       78 | -11.62%  | -54.42%            | -54.90% |     0.07 | 49.23%     | ok               |
| BITO       |       78 | 7.89%    | -59.71%            | -42.82% |     0.27 | 40.93%     | ok               |
| BLK        |       75 | -9.58%   | 29.88%             | -24.27% |    -0.22 | 43.26%     | ok               |
| BND        |       65 | -7.32%   | 0.14%              | -9.89%  |    -1.18 | 32.28%     | ok               |
| BONK-USD   |       68 | 45.20%   | -86.43%            | -48.17% |     0.59 | 41.95%     | ok               |
| BTC-USD    |       70 | 6.41%    | -37.92%            | -23.38% |     0.25 | 51.15%     | ok               |
| C          |       83 | -25.07%  | 153.93%            | -38.66% |    -0.47 | 51.08%     | ok               |
| CAT        |       70 | 34.32%   | 222.96%            | -21.02% |     0.62 | 56.74%     | ok               |
| CL         |       60 | 13.11%   | 8.55%              | -14.32% |     0.47 | 47.59%     | ok               |
| CMCSA      |       82 | -40.28%  | -47.85%            | -40.36% |    -1.06 | 44.26%     | ok               |
| COMP-USD   |       89 | -36.73%  | -78.78%            | -58.43% |    -0.21 | 45.02%     | ok               |
| COP        |       73 | -24.21%  | -3.58%             | -43.77% |    -0.45 | 40.27%     | ok               |
| COST       |       60 | 3.54%    | 36.67%             | -29.73% |     0.17 | 46.26%     | ok               |
| CRM        |       67 | -35.64%  | -46.68%            | -40.31% |    -0.72 | 43.59%     | ok               |
| CRV-USD    |       62 | -0.75%   | -75.02%            | -39.89% |     0.22 | 34.29%     | ok               |
| CSCO       |       61 | 23.47%   | 131.91%            | -21.79% |     0.51 | 50.75%     | ok               |
| CVX        |       69 | -14.47%  | 17.23%             | -26.75% |    -0.36 | 40.93%     | ok               |
| DASH-USD   |       63 | -37.83%  | 1.96%              | -64.43% |     0.03 | 31.61%     | ok               |
| DBC        |       58 | -12.57%  | 20.16%             | -25.35% |    -0.43 | 32.78%     | ok               |
| DE         |       70 | -7.69%   | 49.13%             | -25.24% |    -0.08 | 45.59%     | ok               |
| DIA        |       60 | -2.42%   | 34.37%             | -12.94% |    -0.09 | 45.92%     | ok               |
| DIS        |       66 | -11.82%  | 6.80%              | -27.60% |    -0.14 | 48.09%     | ok               |
| DOGE-USD   |       76 | -19.44%  | -77.91%            | -62.31% |     0.06 | 49.62%     | ok               |
| DOT-USD    |       90 | -48.18%  | -85.41%            | -61.09% |    -0.37 | 48.28%     | ok               |
| DXY-INDEX  |       40 | -0.65%   | -0.08%             | -6.06%  |    -0.09 | 29.50%     | ok               |
| EEM        |       64 | -9.40%   | 74.02%             | -25.67% |    -0.25 | 43.43%     | ok               |
| EFA        |       60 | -7.94%   | 35.91%             | -13.51% |    -0.28 | 44.43%     | ok               |
| EOG        |       77 | -24.73%  | 15.52%             | -48.13% |    -0.54 | 46.09%     | ok               |
| ETC-USD    |       64 | -35.69%  | -72.13%            | -48.16% |    -0.51 | 31.23%     | ok               |
| ETH-USD    |       60 | 165.68%  | -48.14%            | -30.11% |     1.31 | 44.83%     | ok               |
| EWJ        |       64 | -17.34%  | 40.68%             | -30.73% |    -0.55 | 40.43%     | ok               |
| FCX        |       67 | -31.44%  | 61.12%             | -46.84% |    -0.38 | 45.76%     | ok               |
| FET-USD    |       83 | -10.84%  | -85.13%            | -54.02% |     0.19 | 40.04%     | ok               |
| FIL-USD    |       70 | -35.91%  | -84.19%            | -48.33% |    -0.32 | 33.72%     | ok               |
| FXI        |       46 | -5.41%   | 49.70%             | -24.33% |    -0.05 | 28.62%     | ok               |
| GDX        |       64 | 5.53%    | 175.88%            | -34.99% |     0.22 | 48.09%     | ok               |
| GDXJ       |       68 | -23.08%  | 193.43%            | -44.93% |    -0.22 | 45.92%     | ok               |
| GE         |       74 | 19.62%   | 233.50%            | -27.82% |     0.43 | 52.58%     | ok               |
| GLD        |       48 | 25.72%   | 100.07%            | -16.63% |     0.66 | 45.09%     | ok               |
| GOOGL      |       61 | 76.47%   | 128.53%            | -20.41% |     1.14 | 53.74%     | ok               |
| GRT-USD    |       85 | -2.04%   | -90.37%            | -54.83% |     0.2  | 42.91%     | ok               |
| GS         |       76 | 0.34%    | 182.90%            | -22.13% |     0.11 | 51.75%     | ok               |
| HD         |       71 | -6.19%   | -9.14%             | -17.69% |    -0.09 | 43.76%     | ok               |
| HON        |       97 | -30.18%  | 14.59%             | -29.80% |    -0.84 | 52.91%     | ok               |
| HYG        |       79 | -9.05%   | 2.79%              | -9.59%  |    -1.05 | 34.44%     | ok               |
| IBIT       |       32 | 36.87%   | -7.10%             | -18.95% |     0.77 | 31.16%     | ok               |
| IBM        |       74 | 4.70%    | 41.02%             | -25.31% |     0.2  | 50.42%     | ok               |
| ICP-USD    |       85 | -7.81%   | -77.64%            | -58.62% |     0.19 | 39.46%     | ok               |
| IEF        |       76 | -10.90%  | -1.61%             | -11.70% |    -1.54 | 32.78%     | ok               |
| IEMG       |       58 | -5.52%   | 67.08%             | -26.84% |    -0.12 | 43.59%     | ok               |
| INJ-USD    |       77 | -51.80%  | -78.09%            | -76.97% |    -0.47 | 38.70%     | ok               |
| INTC       |       70 | 55.82%   | 208.20%            | -60.60% |     0.62 | 49.25%     | ok               |
| INTU       |       67 | -13.49%  | -60.16%            | -43.77% |    -0.11 | 42.60%     | ok               |
| ITA        |       74 | -1.91%   | 93.24%             | -23.75% |     0.02 | 47.59%     | ok               |
| IWM        |       50 | 8.07%    | 49.37%             | -12.83% |     0.34 | 36.11%     | ok               |
| JNJ        |       71 | 6.64%    | 50.58%             | -17.51% |     0.29 | 50.58%     | ok               |
| JPM        |       73 | -17.54%  | 89.56%             | -33.16% |    -0.41 | 52.91%     | ok               |
| KO         |       51 | 27.92%   | 34.07%             | -8.07%  |     1    | 37.94%     | ok               |
| LDO-USD    |       76 | -1.03%   | -84.03%            | -60.93% |     0.26 | 38.12%     | ok               |
| LIN        |       68 | -0.80%   | 25.60%             | -21.53% |     0.03 | 38.94%     | ok               |
| LINK-USD   |       69 | -11.40%  | -68.73%            | -49.35% |     0.12 | 41.57%     | ok               |
| LLY        |       69 | -14.97%  | 71.65%             | -53.34% |    -0.13 | 51.41%     | ok               |
| LRCX       |       80 | -13.45%  | 344.29%            | -63.56% |     0    | 46.26%     | ok               |
| LTC-USD    |       66 | -34.00%  | -63.47%            | -53.76% |    -0.29 | 48.47%     | ok               |
| MCD        |       75 | -2.55%   | -7.80%             | -18.81% |    -0.05 | 38.10%     | ok               |
| META       |       72 | -16.17%  | 40.53%             | -38.96% |    -0.14 | 50.25%     | ok               |
| MPC        |       71 | -13.74%  | 46.28%             | -44.76% |    -0.14 | 49.92%     | ok               |
| MRK        |       67 | -27.51%  | -1.69%             | -34.46% |    -0.63 | 46.26%     | ok               |
| MS         |       81 | -12.49%  | 157.97%            | -27.79% |    -0.23 | 48.75%     | ok               |
| MSFT       |       83 | -34.29%  | -8.48%             | -38.02% |    -0.9  | 48.09%     | ok               |
| MU         |       51 | 270.20%  | 1120.72%           | -68.76% |     1.34 | 59.90%     | ok               |
| NEAR-USD   |       89 | -6.29%   | -60.14%            | -61.22% |     0.2  | 42.34%     | ok               |
| NEM        |       78 | -29.66%  | 183.51%            | -38.49% |    -0.3  | 54.58%     | ok               |
| NFLX       |       64 | 39.11%   | 29.38%             | -21.09% |     0.81 | 54.91%     | ok               |
| NKE        |       91 | -48.19%  | -59.32%            | -57.25% |    -0.9  | 43.59%     | ok               |
| NOW        |       80 | 21.71%   | -38.95%            | -30.25% |     0.42 | 45.92%     | ok               |
| NVDA       |       74 | -27.23%  | 121.65%            | -45.02% |    -0.21 | 58.65%     | ok               |
| OP-USD     |       74 | -4.12%   | -94.05%            | -72.42% |     0.21 | 36.21%     | ok               |
| ORCL       |       74 | 68.95%   | 44.67%             | -29.47% |     0.72 | 53.58%     | ok               |
| OXY        |       63 | 2.48%    | -11.32%            | -30.85% |     0.16 | 43.09%     | ok               |
| PEP        |       85 | -10.61%  | -16.25%            | -21.35% |    -0.25 | 50.08%     | ok               |
| PEPE-USD   |       75 | 21.63%   | -83.17%            | -57.66% |     0.45 | 43.68%     | ok               |
| PFE        |       77 | -40.46%  | -8.51%             | -42.29% |    -1.3  | 35.77%     | ok               |
| PG         |       62 | -11.59%  | -4.21%             | -21.65% |    -0.41 | 41.43%     | ok               |
| PM         |       83 | -4.17%   | 94.74%             | -33.68% |     0.01 | 57.57%     | ok               |
| POL-USD    |       79 | 64.83%   | -82.58%            | -46.45% |     0.77 | 49.62%     | ok               |
| QCOM       |       77 | -14.12%  | 39.83%             | -57.69% |    -0.02 | 47.42%     | ok               |
| QQQ        |       62 | 19.74%   | 67.80%             | -12.88% |     0.56 | 46.09%     | ok               |
| RENDER-USD |       96 | -17.59%  | -61.68%            | -45.00% |     0.11 | 43.56%     | ok               |
| RTX        |       58 | 20.20%   | 105.73%            | -16.99% |     0.54 | 51.58%     | ok               |
| SBUX       |       64 | -24.83%  | 7.41%              | -29.34% |    -0.51 | 38.94%     | ok               |
| SCHW       |       76 | -21.03%  | 44.72%             | -30.41% |    -0.49 | 45.59%     | ok               |
| SHIB-USD   |       74 | -23.15%  | -77.51%            | -49.00% |    -0.07 | 53.26%     | ok               |
| SHY        |       50 | -2.26%   | -0.22%             | -2.85%  |    -0.79 | 34.61%     | ok               |
| SKY-USD    |       68 | -29.87%  | -3.84%             | -43.98% |    -0.39 | 40.51%     | ok               |
| SLB        |       75 | -25.47%  | -3.16%             | -55.49% |    -0.44 | 49.58%     | ok               |
| SLV        |       58 | 43.23%   | 163.00%            | -42.66% |     0.64 | 40.77%     | ok               |
| SMH        |       48 | 98.22%   | 229.84%            | -33.99% |     1.22 | 50.42%     | ok               |
| SNX-USD    |       60 | 19.87%   | -85.87%            | -32.91% |     0.42 | 40.04%     | ok               |
| SOL-USD    |       66 | -41.15%  | -72.39%            | -56.63% |    -0.2  | 59.58%     | ok               |
| SOXX       |       55 | 87.22%   | 204.40%            | -40.34% |     1.08 | 49.42%     | ok               |
| SPY        |       60 | 6.50%    | 49.44%             | -16.47% |     0.28 | 50.92%     | ok               |
| SUSHI-USD  |       90 | -79.45%  | -87.69%            | -84.18% |    -1.18 | 35.63%     | ok               |
| T          |       62 | 32.61%   | 30.12%             | -17.01% |     0.78 | 50.92%     | ok               |
| TGT        |       56 | -10.02%  | -4.56%             | -40.57% |    -0.12 | 38.44%     | ok               |
| TIA-USD    |       86 | -17.99%  | -91.75%            | -56.16% |     0.06 | 34.87%     | ok               |
| TLT        |       72 | -21.57%  | -9.95%             | -23.63% |    -1.59 | 31.78%     | ok               |
| TMO        |       59 | 6.96%    | -17.24%            | -16.83% |     0.24 | 47.75%     | ok               |
| TMUS       |       70 | 14.84%   | 14.14%             | -24.50% |     0.4  | 47.75%     | ok               |
| TRX-USD    |       74 | 1.02%    | 43.93%             | -22.90% |     0.12 | 49.62%     | ok               |
| TSLA       |       68 | -3.79%   | 99.18%             | -57.89% |     0.17 | 42.26%     | ok               |
| TXN        |       77 | -15.83%  | 87.82%             | -46.98% |    -0.1  | 53.41%     | ok               |
| UNH        |       76 | 26.10%   | -18.74%            | -27.46% |     0.48 | 52.08%     | ok               |
| UNI-USD    |       86 | -72.14%  | -77.89%            | -80.61% |    -0.87 | 41.57%     | ok               |
| UPS        |       68 | -38.15%  | -27.04%            | -40.62% |    -0.77 | 40.10%     | ok               |
| USO        |       68 | 2.80%    | 52.81%             | -43.35% |     0.17 | 34.44%     | ok               |
| VEA        |       58 | -0.98%   | 47.26%             | -17.93% |     0.01 | 44.09%     | ok               |
| VIXY       |       94 | -79.98%  | -59.94%            | -88.16% |    -1    | 31.95%     | ok               |
| VNQ        |       75 | -16.77%  | 15.54%             | -24.92% |    -0.7  | 37.60%     | ok               |
| VTI        |       66 | -0.58%   | 49.07%             | -18.77% |     0.04 | 51.91%     | ok               |
| VWO        |       76 | -13.41%  | 49.18%             | -25.20% |    -0.47 | 44.09%     | ok               |
| VZ         |       85 | -27.66%  | 10.03%             | -31.88% |    -0.96 | 37.60%     | ok               |
| WFC        |       86 | -18.33%  | 64.35%             | -29.91% |    -0.32 | 48.25%     | ok               |
| WIF-USD    |       68 | -43.81%  | -89.76%            | -57.06% |    -0.24 | 32.18%     | ok               |
| WMT        |       57 | 26.80%   | 116.35%            | -21.31% |     0.73 | 51.41%     | ok               |
| XBI        |       60 | -1.28%   | 65.63%             | -21.61% |     0.05 | 39.77%     | ok               |
| XLB        |       70 | -14.85%  | 22.14%             | -26.57% |    -0.51 | 37.60%     | ok               |
| XLC        |       65 | 17.35%   | 37.88%             | -12.33% |     0.58 | 55.57%     | ok               |
| XLE        |       71 | -9.48%   | 28.14%             | -36.18% |    -0.17 | 46.59%     | ok               |
| XLF        |       76 | -12.11%  | 37.31%             | -23.61% |    -0.4  | 48.25%     | ok               |
| XLI        |       64 | 4.36%    | 55.98%             | -11.38% |     0.22 | 46.42%     | ok               |
| XLK        |       42 | 64.57%   | 82.44%             | -14.75% |     1.2  | 47.92%     | ok               |
| XLM-USD    |       69 | 0.26%    | -54.72%            | -50.36% |     0.22 | 45.59%     | ok               |
| XLP        |       70 | 7.46%    | 13.97%             | -10.28% |     0.45 | 42.60%     | ok               |
| XLU        |       71 | -6.68%   | 46.38%             | -18.15% |    -0.26 | 38.94%     | ok               |
| XLV        |       68 | -11.29%  | 8.26%              | -16.83% |    -0.54 | 36.11%     | ok               |
| XLY        |       72 | 1.32%    | 30.69%             | -14.01% |     0.11 | 44.59%     | ok               |
| XOM        |       56 | 4.30%    | 33.27%             | -20.29% |     0.19 | 36.11%     | ok               |
| XRP-USD    |       62 | -29.52%  | -62.55%            | -46.96% |    -0.24 | 35.63%     | ok               |
| YFI-USD    |       83 | -54.99%  | -76.98%            | -67.78% |    -0.82 | 40.61%     | ok               |
| ZEC-USD    |       69 | 50.10%   | 793.09%            | -47.68% |     0.59 | 36.40%     | ok               |

## AAPL Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 26.35%   | 56.51%             | -21.71% |     0.58 |       65 | 52.25%     | ok               |
|          25 | 20.31%   | 56.51%             | -20.03% |     0.48 |       63 | 50.08%     | ok               |
|          15 | 18.76%   | 56.51%             | -23.86% |     0.44 |       76 | 59.73%     | ok               |
|          30 | 15.16%   | 56.51%             | -20.65% |     0.4  |       61 | 48.25%     | ok               |
|          35 | 9.89%    | 56.51%             | -22.04% |     0.3  |       61 | 46.09%     | ok               |

## AAVE-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 5.38%    | -76.60%            | -46.87% |     0.27 |       38 | 26.05%     | ok               |
|          40 | -0.24%   | -76.60%            | -43.61% |     0.21 |       38 | 29.69%     | ok               |
|          35 | -20.11%  | -76.60%            | -51.96% |    -0.03 |       50 | 32.18%     | ok               |
|          50 | -29.70%  | -76.60%            | -47.78% |    -0.27 |       42 | 20.31%     | ok               |
|          15 | -58.89%  | -76.60%            | -64.84% |    -0.48 |       80 | 50.38%     | ok               |

## ABBV Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 1.86%    | 42.35%             | -23.85% |     0.13 |       50 | 37.77%     | ok               |
|          40 | -10.82%  | 42.35%             | -26.61% |    -0.2  |       64 | 42.60%     | ok               |
|          35 | -12.10%  | 42.35%             | -27.83% |    -0.23 |       66 | 45.42%     | ok               |
|          30 | -14.37%  | 42.35%             | -30.55% |    -0.27 |       64 | 48.25%     | ok               |
|          45 | -13.60%  | 42.35%             | -29.59% |    -0.28 |       54 | 39.93%     | ok               |

## ADA-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -81.66%  | -84.63%            | -91.26% |    -0.5  |       78 | 62.26%     | ok               |
|          20 | -81.66%  | -84.63%            | -91.79% |    -0.52 |       84 | 56.90%     | ok               |
|          50 | -78.05%  | -84.63%            | -86.04% |    -0.6  |       55 | 27.01%     | ok               |
|          45 | -80.39%  | -84.63%            | -88.08% |    -0.63 |       58 | 31.80%     | ok               |
|          25 | -84.01%  | -84.63%            | -91.94% |    -0.63 |       81 | 53.07%     | ok               |

## ADBE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 9.93%    | -68.56%            | -21.34% |     0.29 |       78 | 49.75%     | ok               |
|          40 | -4.26%   | -68.56%            | -20.88% |     0.04 |       74 | 42.76%     | ok               |
|          25 | -7.93%   | -68.56%            | -31.29% |     0.03 |       52 | 61.56%     | ok               |
|          15 | -17.75%  | -68.56%            | -31.86% |    -0.12 |       63 | 66.22%     | ok               |
|          20 | -19.36%  | -68.56%            | -34.42% |    -0.15 |       52 | 63.73%     | ok               |

## AGG Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -6.61%   | 0.06%              | -10.16% |    -1.1  |       69 | 31.11%     | ok               |
|          45 | -5.75%   | 0.06%              | -7.89%  |    -1.16 |       52 | 20.47%     | ok               |
|          20 | -8.00%   | 0.06%              | -10.96% |    -1.18 |       73 | 36.61%     | ok               |
|          50 | -5.57%   | 0.06%              | -7.92%  |    -1.25 |       46 | 16.97%     | ok               |
|          25 | -8.17%   | 0.06%              | -11.60% |    -1.25 |       73 | 34.94%     | ok               |

## ALGO-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -50.43%  | -76.01%            | -53.13% |    -0.57 |       86 | 38.12%     | ok               |
|          15 | -59.53%  | -76.01%            | -68.50% |    -0.62 |       82 | 50.00%     | ok               |
|          25 | -61.89%  | -76.01%            | -72.48% |    -0.74 |       84 | 45.02%     | ok               |
|          20 | -63.65%  | -76.01%            | -71.20% |    -0.75 |       84 | 47.70%     | ok               |
|          50 | -45.64%  | -76.01%            | -48.43% |    -0.81 |       42 | 16.86%     | ok               |

## AMAT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -2.71%   | 252.43%            | -54.05% |     0.15 |       66 | 62.06%     | ok               |
|          30 | -18.58%  | 252.43%            | -57.21% |    -0.08 |       69 | 53.41%     | ok               |
|          20 | -24.53%  | 252.43%            | -60.16% |    -0.15 |       72 | 58.57%     | ok               |
|          35 | -24.37%  | 252.43%            | -55.26% |    -0.19 |       71 | 51.25%     | ok               |
|          50 | -22.46%  | 252.43%            | -48.72% |    -0.19 |       52 | 39.27%     | ok               |

## AMD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 4.27%    | 202.13%            | -46.37% |     0.25 |       56 | 37.60%     | ok               |
|          50 | 2.43%    | 202.13%            | -48.02% |     0.23 |       60 | 31.95%     | ok               |
|          35 | -9.02%   | 202.13%            | -54.16% |     0.12 |       62 | 39.60%     | ok               |
|          45 | -16.69%  | 202.13%            | -55.56% |     0.02 |       64 | 34.94%     | ok               |
|          30 | -21.02%  | 202.13%            | -59.51% |    -0.01 |       63 | 42.10%     | ok               |

## AMGN Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -15.41%  | 10.29%             | -26.64% |    -0.25 |       73 | 53.58%     | ok               |
|          15 | -18.41%  | 10.29%             | -27.92% |    -0.3  |       71 | 59.23%     | ok               |
|          35 | -17.92%  | 10.29%             | -31.23% |    -0.34 |       69 | 43.76%     | ok               |
|          30 | -20.65%  | 10.29%             | -34.14% |    -0.41 |       71 | 47.42%     | ok               |
|          25 | -23.88%  | 10.29%             | -33.41% |    -0.49 |       67 | 49.75%     | ok               |

## AMZN Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -17.83%  | 47.24%             | -28.70% |    -0.52 |       50 | 29.78%     | ok               |
|          50 | -25.03%  | 47.24%             | -35.48% |    -0.88 |       48 | 24.13%     | ok               |
|          45 | -25.89%  | 47.24%             | -35.47% |    -0.89 |       50 | 26.96%     | ok               |
|          35 | -30.12%  | 47.24%             | -38.29% |    -0.93 |       64 | 33.11%     | ok               |
|          30 | -34.23%  | 47.24%             | -42.48% |    -1    |       76 | 38.44%     | ok               |

## APT-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 51.21%   | -92.31%            | -46.73% |     0.73 |       44 | 20.69%     | ok               |
|          45 | 14.97%   | -92.31%            | -63.86% |     0.37 |       60 | 26.82%     | ok               |
|          40 | -7.11%   | -92.31%            | -63.33% |     0.16 |       66 | 32.38%     | ok               |
|          20 | -15.40%  | -92.31%            | -70.51% |     0.14 |       71 | 52.30%     | ok               |
|          35 | -13.92%  | -92.31%            | -64.45% |     0.11 |       70 | 38.12%     | ok               |

## ARB-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 61.07%   | -88.73%            | -53.74% |     0.67 |       87 | 56.51%     | ok               |
|          40 | 45.76%   | -88.73%            | -47.60% |     0.62 |       50 | 30.27%     | ok               |
|          35 | 31.50%   | -88.73%            | -56.00% |     0.51 |       60 | 33.72%     | ok               |
|          20 | 29.27%   | -88.73%            | -60.40% |     0.5  |       75 | 50.19%     | ok               |
|          45 | 24.86%   | -88.73%            | -50.83% |     0.46 |       56 | 23.37%     | ok               |

## ARKK Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -24.32%  | 63.64%             | -34.75% |    -0.28 |       90 | 50.25%     | ok               |
|          20 | -28.79%  | 63.64%             | -34.66% |    -0.4  |       85 | 45.59%     | ok               |
|          30 | -32.67%  | 63.64%             | -35.19% |    -0.57 |       81 | 38.94%     | ok               |
|          35 | -33.82%  | 63.64%             | -36.30% |    -0.63 |       80 | 36.61%     | ok               |
|          40 | -35.22%  | 63.64%             | -36.71% |    -0.71 |       72 | 31.78%     | ok               |

## ATOM-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -63.36%  | -70.89%            | -69.81% |    -0.9  |       91 | 50.96%     | ok               |
|          15 | -68.39%  | -70.89%            | -71.82% |    -0.97 |       91 | 60.34%     | ok               |
|          45 | -57.82%  | -70.89%            | -63.84% |    -1.04 |       74 | 28.93%     | ok               |
|          30 | -67.30%  | -70.89%            | -73.34% |    -1.1  |       88 | 44.64%     | ok               |
|          20 | -71.71%  | -70.89%            | -74.51% |    -1.14 |       99 | 54.60%     | ok               |

## AVAX-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 15.04%   | -81.82%            | -34.50% |     0.37 |       38 | 19.54%     | ok               |
|          15 | 6.91%    | -81.82%            | -52.46% |     0.32 |       61 | 53.45%     | ok               |
|          45 | 6.34%    | -81.82%            | -41.07% |     0.26 |       42 | 23.75%     | ok               |
|          40 | -8.53%   | -81.82%            | -46.84% |     0.07 |       46 | 26.82%     | ok               |
|          25 | -16.70%  | -81.82%            | -52.93% |     0.04 |       73 | 44.44%     | ok               |

## AVGO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 31.85%   | 214.65%            | -35.76% |     0.5  |       60 | 44.93%     | ok               |
|          25 | 27.17%   | 214.65%            | -38.01% |     0.46 |       64 | 45.59%     | ok               |
|          35 | 22.88%   | 214.65%            | -36.19% |     0.42 |       70 | 42.26%     | ok               |
|          40 | 22.47%   | 214.65%            | -40.70% |     0.42 |       60 | 39.10%     | ok               |
|          50 | 16.41%   | 214.65%            | -35.84% |     0.35 |       62 | 32.95%     | ok               |

## BA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 26.03%   | 8.12%              | -13.34% |     0.67 |       42 | 31.45%     | ok               |
|          35 | 24.20%   | 8.12%              | -23.77% |     0.5  |       74 | 44.93%     | ok               |
|          40 | 13.69%   | 8.12%              | -23.90% |     0.36 |       48 | 38.77%     | ok               |
|          25 | 5.50%    | 8.12%              | -32.48% |     0.22 |       72 | 53.08%     | ok               |
|          30 | 2.44%    | 8.12%              | -30.56% |     0.17 |       69 | 49.58%     | ok               |

## BAC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -4.38%   | 66.46%             | -22.31% |    -0.07 |       60 | 36.11%     | ok               |
|          20 | -6.97%   | 66.46%             | -21.70% |    -0.09 |       80 | 51.75%     | ok               |
|          50 | -5.93%   | 66.46%             | -20.84% |    -0.14 |       58 | 32.95%     | ok               |
|          35 | -7.83%   | 66.46%             | -29.13% |    -0.16 |       70 | 43.43%     | ok               |
|          15 | -12.20%  | 66.46%             | -23.91% |    -0.21 |       80 | 56.74%     | ok               |

## BCH-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -15.81%  | -54.42%            | -58.01% |     0.08 |       76 | 59.58%     | ok               |
|          30 | -11.62%  | -54.42%            | -54.90% |     0.07 |       78 | 49.23%     | ok               |
|          20 | -20.96%  | -54.42%            | -59.67% |     0.01 |       72 | 55.56%     | ok               |
|          40 | -21.22%  | -54.42%            | -61.24% |    -0.09 |       71 | 40.80%     | ok               |
|          25 | -30.83%  | -54.42%            | -64.70% |    -0.14 |       73 | 51.53%     | ok               |

## BITO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 21.07%   | -59.71%            | -32.29% |     0.41 |       54 | 25.96%     | ok               |
|          30 | 7.89%    | -59.71%            | -42.82% |     0.27 |       78 | 40.93%     | ok               |
|          15 | 1.30%    | -59.71%            | -48.29% |     0.21 |       87 | 49.92%     | ok               |
|          25 | -0.65%   | -59.71%            | -41.73% |     0.18 |       82 | 43.93%     | ok               |
|          45 | 0.97%    | -59.71%            | -43.53% |     0.17 |       58 | 28.95%     | ok               |

## BLK Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | -3.36%   | 29.88%             | -17.94% |    -0.04 |       82 | 39.60%     | ok               |
|          40 | -5.19%   | 29.88%             | -20.06% |    -0.11 |       74 | 35.27%     | ok               |
|          20 | -8.67%   | 29.88%             | -21.48% |    -0.17 |       79 | 47.42%     | ok               |
|          30 | -9.58%   | 29.88%             | -24.27% |    -0.22 |       75 | 43.26%     | ok               |
|          25 | -10.49%  | 29.88%             | -23.34% |    -0.24 |       75 | 45.59%     | ok               |

## BND Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -6.45%   | 0.14%              | -9.32%  |    -0.94 |       63 | 37.94%     | ok               |
|          25 | -7.14%   | 0.14%              | -10.40% |    -1.09 |       67 | 35.94%     | ok               |
|          30 | -7.32%   | 0.14%              | -9.89%  |    -1.18 |       65 | 32.28%     | ok               |
|          15 | -8.65%   | 0.14%              | -10.85% |    -1.25 |       73 | 40.77%     | ok               |
|          45 | -7.56%   | 0.14%              | -9.57%  |    -1.47 |       50 | 21.96%     | ok               |

## BONK-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 170.78%  | -86.43%            | -35.57% |     1.24 |       48 | 22.41%     | ok               |
|          15 | 160.70%  | -86.43%            | -62.48% |     0.98 |       70 | 57.66%     | ok               |
|          25 | 145.88%  | -86.43%            | -51.34% |     0.97 |       67 | 48.28%     | ok               |
|          20 | 131.99%  | -86.43%            | -58.35% |     0.92 |       67 | 52.87%     | ok               |
|          40 | 71.60%   | -86.43%            | -53.34% |     0.74 |       52 | 34.48%     | ok               |

## BTC-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 56.93%   | -37.92%            | -14.50% |     1.02 |       44 | 33.91%     | ok               |
|          45 | 45.84%   | -37.92%            | -13.36% |     0.88 |       44 | 30.46%     | ok               |
|          35 | 36.01%   | -37.92%            | -22.12% |     0.7  |       68 | 41.00%     | ok               |
|          50 | 18.09%   | -37.92%            | -16.15% |     0.48 |       40 | 25.10%     | ok               |
|          30 | 17.30%   | -37.92%            | -21.75% |     0.41 |       70 | 47.51%     | ok               |

## C Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -5.17%   | 153.93%            | -22.28% |    -0.07 |       66 | 35.94%     | ok               |
|          45 | -12.23%  | 153.93%            | -28.12% |    -0.25 |       78 | 39.93%     | ok               |
|          15 | -21.65%  | 153.93%            | -35.02% |    -0.35 |       74 | 59.57%     | ok               |
|          25 | -21.65%  | 153.93%            | -35.86% |    -0.38 |       73 | 53.08%     | ok               |
|          40 | -18.44%  | 153.93%            | -33.20% |    -0.4  |       82 | 42.43%     | ok               |

## CAT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 34.32%   | 222.96%            | -21.02% |     0.62 |       70 | 56.74%     | ok               |
|          25 | 34.44%   | 222.96%            | -26.37% |     0.62 |       66 | 59.57%     | ok               |
|          20 | 31.72%   | 222.96%            | -25.65% |     0.58 |       76 | 62.90%     | ok               |
|          45 | 22.72%   | 222.96%            | -28.85% |     0.49 |       56 | 45.59%     | ok               |
|          15 | 21.50%   | 222.96%            | -30.60% |     0.44 |       69 | 68.89%     | ok               |

## CL Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 13.60%   | 8.55%              | -12.98% |     0.57 |       42 | 31.61%     | ok               |
|          30 | 13.11%   | 8.55%              | -14.32% |     0.47 |       60 | 47.59%     | ok               |
|          45 | 8.41%    | 8.55%              | -13.51% |     0.37 |       46 | 34.61%     | ok               |
|          35 | 7.72%    | 8.55%              | -13.83% |     0.32 |       62 | 43.93%     | ok               |
|          40 | 4.60%    | 8.55%              | -12.70% |     0.22 |       56 | 38.60%     | ok               |

## CMCSA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -36.03%  | -47.85%            | -49.03% |    -0.79 |       87 | 58.74%     | ok               |
|          30 | -40.28%  | -47.85%            | -40.36% |    -1.06 |       82 | 44.26%     | ok               |
|          25 | -45.44%  | -47.85%            | -45.52% |    -1.22 |       89 | 49.58%     | ok               |
|          20 | -47.01%  | -47.85%            | -47.23% |    -1.25 |       93 | 54.74%     | ok               |
|          50 | -33.59%  | -47.85%            | -33.68% |    -1.31 |       50 | 16.31%     | ok               |

## COMP-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 0.22%    | -78.78%            | -38.71% |     0.2  |       48 | 20.88%     | ok               |
|          25 | -37.88%  | -78.78%            | -60.58% |    -0.19 |       87 | 50.00%     | ok               |
|          30 | -36.73%  | -78.78%            | -58.43% |    -0.21 |       89 | 45.02%     | ok               |
|          15 | -46.13%  | -78.78%            | -65.55% |    -0.28 |      101 | 61.49%     | ok               |
|          40 | -41.16%  | -78.78%            | -47.52% |    -0.37 |       74 | 33.14%     | ok               |

## COP Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -9.77%   | -3.58%             | -34.21% |    -0.15 |       48 | 27.29%     | ok               |
|          45 | -15.67%  | -3.58%             | -40.57% |    -0.3  |       58 | 30.12%     | ok               |
|          35 | -23.70%  | -3.58%             | -43.58% |    -0.45 |       75 | 37.10%     | ok               |
|          30 | -24.21%  | -3.58%             | -43.77% |    -0.45 |       73 | 40.27%     | ok               |
|          40 | -26.23%  | -3.58%             | -46.34% |    -0.57 |       68 | 32.78%     | ok               |

## COST Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 16.14%   | 36.67%             | -24.32% |     0.49 |       64 | 52.41%     | ok               |
|          25 | 15.12%   | 36.67%             | -24.73% |     0.48 |       61 | 49.75%     | ok               |
|          35 | 8.50%    | 36.67%             | -26.58% |     0.32 |       54 | 43.26%     | ok               |
|          30 | 3.54%    | 36.67%             | -29.73% |     0.17 |       60 | 46.26%     | ok               |
|          40 | 1.84%    | 36.67%             | -28.41% |     0.12 |       56 | 40.27%     | ok               |

## CRM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -30.76%  | -46.68%            | -39.57% |    -0.45 |       92 | 55.24%     | ok               |
|          35 | -25.07%  | -46.68%            | -35.48% |    -0.47 |       64 | 38.77%     | ok               |
|          40 | -31.83%  | -46.68%            | -41.30% |    -0.72 |       70 | 34.94%     | ok               |
|          30 | -35.64%  | -46.68%            | -40.31% |    -0.72 |       67 | 43.59%     | ok               |
|          20 | -40.97%  | -46.68%            | -41.99% |    -0.77 |       80 | 48.92%     | ok               |

## CRV-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 24.97%   | -75.02%            | -37.78% |     0.46 |       64 | 29.69%     | ok               |
|          50 | 12.00%   | -75.02%            | -29.30% |     0.33 |       40 | 16.67%     | ok               |
|          45 | 6.52%    | -75.02%            | -42.29% |     0.27 |       52 | 19.54%     | ok               |
|          30 | -0.75%   | -75.02%            | -39.89% |     0.22 |       62 | 34.29%     | ok               |
|          40 | -0.48%   | -75.02%            | -38.86% |     0.2  |       56 | 25.67%     | ok               |

## CSCO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 28.18%   | 131.91%            | -19.34% |     0.63 |       58 | 38.94%     | ok               |
|          45 | 26.10%   | 131.91%            | -19.34% |     0.58 |       53 | 41.60%     | ok               |
|          25 | 24.04%   | 131.91%            | -23.28% |     0.52 |       65 | 52.75%     | ok               |
|          35 | 23.46%   | 131.91%            | -23.68% |     0.51 |       53 | 48.25%     | ok               |
|          30 | 23.47%   | 131.91%            | -21.79% |     0.51 |       61 | 50.75%     | ok               |

## CVX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -9.17%   | 17.23%             | -28.32% |    -0.23 |       57 | 31.11%     | ok               |
|          40 | -11.10%  | 17.23%             | -26.30% |    -0.29 |       69 | 34.94%     | ok               |
|          20 | -13.07%  | 17.23%             | -26.07% |    -0.29 |       71 | 45.26%     | ok               |
|          35 | -11.99%  | 17.23%             | -27.83% |    -0.29 |       65 | 37.77%     | ok               |
|          25 | -13.44%  | 17.23%             | -25.65% |    -0.3  |       75 | 44.09%     | ok               |

## DASH-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 117.52%  | 1.96%              | -35.01% |     0.91 |       40 | 17.24%     | ok               |
|          40 | 75.62%   | 1.96%              | -34.44% |     0.72 |       46 | 23.75%     | ok               |
|          45 | 57.09%   | 1.96%              | -42.78% |     0.63 |       44 | 19.54%     | ok               |
|          25 | -32.35%  | 1.96%              | -64.14% |     0.1  |       69 | 34.48%     | ok               |
|          35 | -32.14%  | 1.96%              | -63.23% |     0.09 |       69 | 28.16%     | ok               |

## DBC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -8.05%   | 20.16%             | -19.49% |    -0.3  |       44 | 20.80%     | ok               |
|          35 | -9.68%   | 20.16%             | -23.38% |    -0.31 |       60 | 31.61%     | ok               |
|          15 | -10.28%  | 20.16%             | -27.04% |    -0.32 |       69 | 37.44%     | ok               |
|          45 | -9.42%   | 20.16%             | -20.65% |    -0.33 |       56 | 24.13%     | ok               |
|          30 | -12.57%  | 20.16%             | -25.35% |    -0.43 |       58 | 32.78%     | ok               |

## DE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -6.83%   | 49.13%             | -28.94% |    -0.05 |       70 | 50.92%     | ok               |
|          30 | -7.69%   | 49.13%             | -25.24% |    -0.08 |       70 | 45.59%     | ok               |
|          25 | -9.13%   | 49.13%             | -26.67% |    -0.11 |       72 | 48.25%     | ok               |
|          50 | -10.11%  | 49.13%             | -24.93% |    -0.21 |       70 | 30.62%     | ok               |
|          45 | -11.48%  | 49.13%             | -28.13% |    -0.22 |       68 | 34.94%     | ok               |

## DIA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | -0.36%   | 34.37%             | -13.15% |     0.02 |       60 | 43.76%     | ok               |
|          25 | -0.90%   | 34.37%             | -11.28% |    -0.01 |       60 | 47.09%     | ok               |
|          30 | -2.42%   | 34.37%             | -12.94% |    -0.09 |       60 | 45.92%     | ok               |
|          20 | -4.29%   | 34.37%             | -13.85% |    -0.18 |       64 | 49.42%     | ok               |
|          40 | -4.39%   | 34.37%             | -15.06% |    -0.22 |       66 | 41.10%     | ok               |

## DIS Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 33.03%   | 6.80%              | -14.24% |     0.83 |       50 | 30.28%     | ok               |
|          45 | 5.13%    | 6.80%              | -16.54% |     0.21 |       51 | 33.78%     | ok               |
|          40 | 4.18%    | 6.80%              | -22.77% |     0.19 |       63 | 38.94%     | ok               |
|          35 | -5.53%   | 6.80%              | -25.11% |    -0.01 |       73 | 44.76%     | ok               |
|          15 | -7.13%   | 6.80%              | -30.25% |    -0.01 |       87 | 59.07%     | ok               |

## DOGE-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 18.03%   | -77.91%            | -59.36% |     0.43 |       80 | 64.94%     | ok               |
|          20 | 0.78%    | -77.91%            | -57.37% |     0.28 |       83 | 60.15%     | ok               |
|          25 | -3.40%   | -77.91%            | -55.33% |     0.24 |       73 | 54.79%     | ok               |
|          30 | -19.44%  | -77.91%            | -62.31% |     0.06 |       76 | 49.62%     | ok               |
|          35 | -43.31%  | -77.91%            | -61.79% |    -0.34 |       72 | 43.30%     | ok               |

## DOT-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -19.10%  | -85.41%            | -44.94% |    -0.11 |       56 | 26.25%     | ok               |
|          45 | -22.32%  | -85.41%            | -48.88% |    -0.13 |       52 | 31.23%     | ok               |
|          40 | -30.80%  | -85.41%            | -48.73% |    -0.24 |       56 | 34.67%     | ok               |
|          35 | -43.34%  | -85.41%            | -59.90% |    -0.3  |       80 | 41.95%     | ok               |
|          30 | -48.18%  | -85.41%            | -61.09% |    -0.37 |       90 | 48.28%     | ok               |

## DXY-INDEX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -0.65%   | -0.08%             | -6.06%  |    -0.09 |       40 | 29.50%     | ok               |
|          40 | -2.99%   | -0.08%             | -7.30%  |    -0.37 |       68 | 48.59%     | ok               |
|          15 | -5.36%   | -0.08%             | -11.57% |    -0.49 |       92 | 75.49%     | ok               |
|          45 | -3.72%   | -0.08%             | -8.12%  |    -0.5  |       64 | 37.53%     | ok               |
|          35 | -4.29%   | -0.08%             | -10.12% |    -0.51 |       73 | 54.45%     | ok               |

## EEM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -2.91%   | 74.02%             | -15.88% |    -0.04 |       50 | 36.11%     | ok               |
|          45 | -4.62%   | 74.02%             | -17.36% |    -0.11 |       52 | 37.60%     | ok               |
|          40 | -4.96%   | 74.02%             | -19.52% |    -0.11 |       64 | 39.77%     | ok               |
|          35 | -5.62%   | 74.02%             | -23.88% |    -0.12 |       66 | 41.76%     | ok               |
|          30 | -9.40%   | 74.02%             | -25.67% |    -0.25 |       64 | 43.43%     | ok               |

## EFA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -1.25%   | 35.91%             | -10.80% |     0.02 |       58 | 52.08%     | ok               |
|          20 | -8.10%   | 35.91%             | -12.49% |    -0.27 |       65 | 49.08%     | ok               |
|          30 | -7.94%   | 35.91%             | -13.51% |    -0.28 |       60 | 44.43%     | ok               |
|          40 | -9.34%   | 35.91%             | -15.38% |    -0.38 |       64 | 40.60%     | ok               |
|          50 | -9.07%   | 35.91%             | -17.56% |    -0.4  |       54 | 36.27%     | ok               |

## EOG Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -18.73%  | 15.52%             | -38.89% |    -0.43 |       52 | 32.78%     | ok               |
|          50 | -19.92%  | 15.52%             | -39.55% |    -0.49 |       56 | 29.95%     | ok               |
|          30 | -24.73%  | 15.52%             | -48.13% |    -0.54 |       77 | 46.09%     | ok               |
|          40 | -23.54%  | 15.52%             | -42.28% |    -0.57 |       60 | 36.11%     | ok               |
|          35 | -25.10%  | 15.52%             | -45.93% |    -0.6  |       75 | 40.93%     | ok               |

## ETC-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -7.93%   | -72.13%            | -27.89% |    -0.02 |       28 | 17.05%     | ok               |
|          35 | -15.03%  | -72.13%            | -42.62% |    -0.11 |       44 | 27.01%     | ok               |
|          45 | -16.07%  | -72.13%            | -35.44% |    -0.17 |       26 | 18.97%     | ok               |
|          40 | -21.04%  | -72.13%            | -40.48% |    -0.26 |       42 | 22.80%     | ok               |
|          30 | -35.69%  | -72.13%            | -48.16% |    -0.51 |       64 | 31.23%     | ok               |

## ETH-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 165.68%  | -48.14%            | -30.11% |     1.31 |       60 | 44.83%     | ok               |
|          30 | 147.46%  | -48.14%            | -32.89% |     1.19 |       62 | 53.45%     | ok               |
|          40 | 62.72%   | -48.14%            | -33.11% |     0.8  |       56 | 37.36%     | ok               |
|          45 | 38.98%   | -48.14%            | -34.50% |     0.61 |       52 | 33.72%     | ok               |
|          20 | 35.29%   | -48.14%            | -39.10% |     0.54 |       81 | 63.41%     | ok               |

## EWJ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -17.34%  | 40.68%             | -30.73% |    -0.55 |       64 | 40.43%     | ok               |
|          20 | -18.74%  | 40.68%             | -31.32% |    -0.59 |       60 | 42.43%     | ok               |
|          45 | -18.13%  | 40.68%             | -27.68% |    -0.68 |       60 | 32.61%     | ok               |
|          25 | -21.09%  | 40.68%             | -31.18% |    -0.69 |       60 | 41.43%     | ok               |
|          35 | -21.30%  | 40.68%             | -32.54% |    -0.72 |       70 | 38.77%     | ok               |

## FCX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -6.29%   | 61.12%             | -26.57% |     0.03 |       56 | 29.45%     | ok               |
|          45 | -11.01%  | 61.12%             | -32.99% |    -0.04 |       56 | 33.78%     | ok               |
|          40 | -23.41%  | 61.12%             | -42.89% |    -0.26 |       66 | 39.10%     | ok               |
|          30 | -31.44%  | 61.12%             | -46.84% |    -0.38 |       67 | 45.76%     | ok               |
|          35 | -35.67%  | 61.12%             | -50.12% |    -0.49 |       73 | 43.93%     | ok               |

## FET-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 44.43%   | -85.13%            | -57.24% |     0.59 |       90 | 50.19%     | ok               |
|          15 | 8.01%    | -85.13%            | -59.58% |     0.38 |       86 | 53.26%     | ok               |
|          25 | -5.51%   | -85.13%            | -57.82% |     0.25 |       93 | 43.87%     | ok               |
|          30 | -10.84%  | -85.13%            | -54.02% |     0.19 |       83 | 40.04%     | ok               |
|          45 | -20.81%  | -85.13%            | -48.61% |    -0.07 |       56 | 18.97%     | ok               |

## FIL-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -2.45%   | -84.19%            | -36.87% |     0.14 |       48 | 23.56%     | ok               |
|          45 | -24.61%  | -84.19%            | -41.68% |    -0.23 |       46 | 17.82%     | ok               |
|          35 | -29.88%  | -84.19%            | -45.02% |    -0.24 |       58 | 28.16%     | ok               |
|          30 | -35.91%  | -84.19%            | -48.33% |    -0.32 |       70 | 33.72%     | ok               |
|          50 | -26.52%  | -84.19%            | -44.97% |    -0.32 |       38 | 13.03%     | ok               |

## FXI Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -4.86%   | 49.70%             | -22.99% |    -0.04 |       46 | 29.78%     | ok               |
|          30 | -5.41%   | 49.70%             | -24.33% |    -0.05 |       46 | 28.62%     | ok               |
|          15 | -7.18%   | 49.70%             | -21.68% |    -0.08 |       52 | 32.95%     | ok               |
|          45 | -7.32%   | 49.70%             | -26.75% |    -0.12 |       44 | 23.13%     | ok               |
|          20 | -8.70%   | 49.70%             | -24.94% |    -0.13 |       52 | 30.95%     | ok               |

## GDX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 15.59%   | 175.88%            | -31.87% |     0.37 |       62 | 42.76%     | ok               |
|          20 | 11.96%   | 175.88%            | -35.59% |     0.31 |       77 | 52.91%     | ok               |
|          35 | 7.14%    | 175.88%            | -32.37% |     0.24 |       68 | 45.09%     | ok               |
|          30 | 5.53%    | 175.88%            | -34.99% |     0.22 |       64 | 48.09%     | ok               |
|          25 | 1.25%    | 175.88%            | -38.90% |     0.16 |       67 | 49.75%     | ok               |

## GDXJ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -13.66%  | 193.43%            | -45.05% |    -0.02 |       70 | 53.24%     | ok               |
|          50 | -16.59%  | 193.43%            | -42.44% |    -0.15 |       56 | 37.44%     | ok               |
|          30 | -23.08%  | 193.43%            | -44.93% |    -0.22 |       68 | 45.92%     | ok               |
|          35 | -26.71%  | 193.43%            | -43.49% |    -0.3  |       70 | 43.59%     | ok               |
|          25 | -29.61%  | 193.43%            | -47.26% |    -0.31 |       74 | 49.58%     | ok               |

## GE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 36.79%   | 233.50%            | -22.29% |     0.71 |       66 | 39.43%     | ok               |
|          45 | 26.46%   | 233.50%            | -25.68% |     0.55 |       74 | 42.26%     | ok               |
|          20 | 25.53%   | 233.50%            | -26.63% |     0.5  |       69 | 56.07%     | ok               |
|          35 | 19.89%   | 233.50%            | -27.11% |     0.44 |       80 | 47.59%     | ok               |
|          40 | 18.99%   | 233.50%            | -26.97% |     0.43 |       76 | 43.76%     | ok               |

## GLD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | 32.01%   | 100.07%            | -14.61% |     0.77 |       46 | 46.26%     | ok               |
|          20 | 30.04%   | 100.07%            | -14.61% |     0.73 |       48 | 47.59%     | ok               |
|          30 | 25.72%   | 100.07%            | -16.63% |     0.66 |       48 | 45.09%     | ok               |
|          15 | 22.07%   | 100.07%            | -17.54% |     0.56 |       50 | 51.75%     | ok               |
|          35 | 19.59%   | 100.07%            | -17.29% |     0.54 |       50 | 44.43%     | ok               |

## GOOGL Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 76.48%   | 128.53%            | -19.12% |     1.16 |       65 | 49.25%     | ok               |
|          30 | 76.47%   | 128.53%            | -20.41% |     1.14 |       61 | 53.74%     | ok               |
|          25 | 74.63%   | 128.53%            | -19.76% |     1.11 |       61 | 55.74%     | ok               |
|          15 | 64.80%   | 128.53%            | -13.59% |     0.96 |       73 | 63.39%     | ok               |
|          20 | 61.44%   | 128.53%            | -20.57% |     0.96 |       72 | 58.07%     | ok               |

## GRT-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 37.41%   | -90.37%            | -35.66% |     0.62 |       44 | 22.03%     | ok               |
|          20 | 8.48%    | -90.37%            | -46.47% |     0.33 |       81 | 55.94%     | ok               |
|          15 | 7.03%    | -90.37%            | -49.67% |     0.32 |       75 | 61.30%     | ok               |
|          45 | 10.67%   | -90.37%            | -46.59% |     0.32 |       52 | 27.59%     | ok               |
|          35 | 7.72%    | -90.37%            | -48.22% |     0.3  |       62 | 36.59%     | ok               |

## GS Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 30.04%   | 182.90%            | -20.56% |     0.61 |       74 | 60.57%     | ok               |
|          20 | 12.30%   | 182.90%            | -23.19% |     0.33 |       74 | 56.57%     | ok               |
|          25 | 6.62%    | 182.90%            | -23.32% |     0.23 |       74 | 54.08%     | ok               |
|          40 | 1.74%    | 182.90%            | -17.88% |     0.13 |       72 | 45.09%     | ok               |
|          30 | 0.34%    | 182.90%            | -22.13% |     0.11 |       76 | 51.75%     | ok               |

## HD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -6.19%   | -9.14%             | -17.69% |    -0.09 |       71 | 43.76%     | ok               |
|          25 | -6.92%   | -9.14%             | -18.51% |    -0.11 |       70 | 45.76%     | ok               |
|          45 | -11.92%  | -9.14%             | -20.74% |    -0.35 |       60 | 28.29%     | ok               |
|          40 | -13.94%  | -9.14%             | -19.63% |    -0.39 |       82 | 33.61%     | ok               |
|          35 | -16.17%  | -9.14%             | -22.98% |    -0.42 |       80 | 39.77%     | ok               |

## HON Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -17.09%  | 14.59%             | -21.90% |    -0.53 |       74 | 32.11%     | ok               |
|          45 | -18.75%  | 14.59%             | -20.64% |    -0.55 |       76 | 37.10%     | ok               |
|          40 | -26.75%  | 14.59%             | -26.29% |    -0.78 |       78 | 41.43%     | ok               |
|          35 | -28.43%  | 14.59%             | -27.37% |    -0.81 |       95 | 47.92%     | ok               |
|          30 | -30.18%  | 14.59%             | -29.80% |    -0.84 |       97 | 52.91%     | ok               |

## HYG Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -7.49%   | 2.79%              | -7.49%  |    -0.9  |       70 | 29.62%     | ok               |
|          45 | -8.18%   | 2.79%              | -8.21%  |    -1.02 |       66 | 26.46%     | ok               |
|          30 | -9.05%   | 2.79%              | -9.59%  |    -1.05 |       79 | 34.44%     | ok               |
|          15 | -9.75%   | 2.79%              | -10.10% |    -1.06 |       88 | 41.60%     | ok               |
|          20 | -9.79%   | 2.79%              | -10.39% |    -1.09 |       88 | 39.27%     | ok               |

## IBIT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 66.12%   | -7.10%             | -19.20% |     1.08 |       38 | 38.89%     | ok               |
|          50 | 52.25%   | -7.10%             | -17.37% |     1.06 |       20 | 22.95%     | ok               |
|          45 | 43.79%   | -7.10%             | -17.37% |     0.91 |       22 | 23.67%     | ok               |
|          40 | 38.85%   | -7.10%             | -17.78% |     0.84 |       24 | 25.36%     | ok               |
|          30 | 36.87%   | -7.10%             | -18.95% |     0.77 |       32 | 31.16%     | ok               |

## IBM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 13.98%   | 41.02%             | -28.20% |     0.35 |       89 | 62.40%     | ok               |
|          30 | 4.70%    | 41.02%             | -25.31% |     0.2  |       74 | 50.42%     | ok               |
|          35 | 2.60%    | 41.02%             | -25.15% |     0.15 |       70 | 46.09%     | ok               |
|          45 | 0.38%    | 41.02%             | -22.48% |     0.1  |       56 | 36.61%     | ok               |
|          20 | -3.32%   | 41.02%             | -34.12% |     0.05 |       73 | 54.74%     | ok               |

## ICP-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 8.92%    | -77.64%            | -36.45% |     0.31 |       62 | 27.59%     | ok               |
|          30 | -7.81%   | -77.64%            | -58.62% |     0.19 |       85 | 39.46%     | ok               |
|          35 | -7.07%   | -77.64%            | -54.17% |     0.14 |       74 | 33.52%     | ok               |
|          50 | -4.13%   | -77.64%            | -43.65% |     0.14 |       42 | 17.24%     | ok               |
|          15 | -30.85%  | -77.64%            | -63.03% |     0.04 |       79 | 52.49%     | ok               |

## IEF Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -7.23%   | -1.61%             | -10.09% |    -0.87 |       70 | 42.10%     | ok               |
|          15 | -7.78%   | -1.61%             | -10.82% |    -0.92 |       69 | 43.59%     | ok               |
|          40 | -8.39%   | -1.61%             | -9.67%  |    -1.31 |       60 | 24.79%     | ok               |
|          45 | -8.07%   | -1.61%             | -9.73%  |    -1.33 |       50 | 22.80%     | ok               |
|          25 | -10.80%  | -1.61%             | -11.49% |    -1.38 |       76 | 39.27%     | ok               |

## IEMG Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 1.46%    | 67.08%             | -13.87% |     0.11 |       52 | 34.78%     | ok               |
|          45 | 0.63%    | 67.08%             | -14.87% |     0.08 |       48 | 37.27%     | ok               |
|          35 | -0.32%   | 67.08%             | -22.13% |     0.05 |       63 | 42.60%     | ok               |
|          40 | -0.92%   | 67.08%             | -18.39% |     0.03 |       60 | 40.27%     | ok               |
|          25 | -4.72%   | 67.08%             | -25.58% |    -0.09 |       59 | 45.42%     | ok               |

## INJ-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -9.97%   | -78.09%            | -53.80% |     0.06 |       42 | 22.61%     | ok               |
|          35 | -18.70%  | -78.09%            | -60.42% |     0.01 |       62 | 32.76%     | ok               |
|          50 | -19.76%  | -78.09%            | -49.35% |    -0.1  |       46 | 19.54%     | ok               |
|          40 | -27.04%  | -78.09%            | -57.21% |    -0.15 |       52 | 28.93%     | ok               |
|          25 | -53.83%  | -78.09%            | -81.57% |    -0.46 |       77 | 43.30%     | ok               |

## INTC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 76.11%   | 208.20%            | -49.32% |     0.74 |       60 | 34.28%     | ok               |
|          15 | 82.95%   | 208.20%            | -53.65% |     0.74 |       84 | 61.23%     | ok               |
|          25 | 75.50%   | 208.20%            | -56.41% |     0.72 |       75 | 51.58%     | ok               |
|          40 | 70.33%   | 208.20%            | -55.86% |     0.7  |       68 | 38.60%     | ok               |
|          20 | 72.70%   | 208.20%            | -52.47% |     0.7  |       82 | 56.57%     | ok               |

## INTU Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 1.77%    | -60.16%            | -42.82% |     0.15 |       73 | 29.12%     | ok               |
|          45 | -1.71%   | -60.16%            | -44.66% |     0.09 |       71 | 33.28%     | ok               |
|          40 | -9.07%   | -60.16%            | -48.32% |    -0.05 |       71 | 35.94%     | ok               |
|          25 | -10.36%  | -60.16%            | -42.24% |    -0.05 |       66 | 45.26%     | ok               |
|          15 | -11.42%  | -60.16%            | -46.90% |    -0.06 |       81 | 50.75%     | ok               |

## ITA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 2.22%    | 93.24%             | -21.48% |     0.14 |       76 | 37.60%     | ok               |
|          15 | -1.84%   | 93.24%             | -28.17% |     0.04 |       86 | 59.23%     | ok               |
|          30 | -1.91%   | 93.24%             | -23.75% |     0.02 |       74 | 47.59%     | ok               |
|          35 | -4.43%   | 93.24%             | -23.16% |    -0.06 |       78 | 45.76%     | ok               |
|          40 | -5.53%   | 93.24%             | -20.58% |    -0.11 |       80 | 42.26%     | ok               |

## IWM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | 8.50%    | 49.37%             | -13.30% |     0.35 |       52 | 37.10%     | ok               |
|          30 | 8.07%    | 49.37%             | -12.83% |     0.34 |       50 | 36.11%     | ok               |
|          40 | 5.88%    | 49.37%             | -14.08% |     0.28 |       44 | 31.45%     | ok               |
|          35 | 5.63%    | 49.37%             | -14.11% |     0.26 |       50 | 33.78%     | ok               |
|          20 | 4.22%    | 49.37%             | -13.83% |     0.21 |       62 | 38.10%     | ok               |

## JNJ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 21.36%   | 50.58%             | -10.57% |     0.9  |       56 | 37.10%     | ok               |
|          15 | 17.79%   | 50.58%             | -18.02% |     0.62 |       65 | 57.74%     | ok               |
|          45 | 12.26%   | 50.58%             | -13.35% |     0.53 |       58 | 42.26%     | ok               |
|          20 | 13.34%   | 50.58%             | -17.61% |     0.5  |       71 | 54.24%     | ok               |
|          40 | 9.81%    | 50.58%             | -14.77% |     0.42 |       64 | 46.42%     | ok               |

## JPM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 21.83%   | 89.56%             | -15.90% |     0.71 |       52 | 40.60%     | ok               |
|          45 | 10.26%   | 89.56%             | -21.91% |     0.36 |       54 | 43.59%     | ok               |
|          40 | -4.30%   | 89.56%             | -28.47% |    -0.05 |       66 | 46.09%     | ok               |
|          20 | -11.45%  | 89.56%             | -33.59% |    -0.17 |       84 | 57.40%     | ok               |
|          35 | -9.65%   | 89.56%             | -27.43% |    -0.19 |       72 | 49.75%     | ok               |

## KO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 27.92%   | 34.07%             | -8.07%  |     1    |       51 | 37.94%     | ok               |
|          35 | 24.00%   | 34.07%             | -8.07%  |     0.89 |       54 | 36.61%     | ok               |
|          40 | 21.41%   | 34.07%             | -9.28%  |     0.86 |       56 | 33.44%     | ok               |
|          25 | 22.64%   | 34.07%             | -9.37%  |     0.83 |       57 | 40.60%     | ok               |
|          50 | 14.81%   | 34.07%             | -11.40% |     0.68 |       36 | 26.79%     | ok               |

## LDO-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 24.99%   | -84.03%            | -46.95% |     0.48 |       81 | 51.92%     | ok               |
|          20 | 13.39%   | -84.03%            | -44.97% |     0.4  |       85 | 47.32%     | ok               |
|          50 | 15.22%   | -84.03%            | -48.04% |     0.37 |       46 | 16.86%     | ok               |
|          30 | -1.03%   | -84.03%            | -60.93% |     0.26 |       76 | 38.12%     | ok               |
|          35 | -3.23%   | -84.03%            | -62.61% |     0.22 |       74 | 31.23%     | ok               |

## LIN Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 4.87%    | 25.60%             | -23.70% |     0.22 |       63 | 49.75%     | ok               |
|          25 | 3.57%    | 25.60%             | -22.01% |     0.18 |       65 | 41.76%     | ok               |
|          20 | 1.35%    | 25.60%             | -23.00% |     0.11 |       64 | 44.93%     | ok               |
|          35 | -0.17%   | 25.60%             | -21.18% |     0.05 |       64 | 32.45%     | ok               |
|          30 | -0.80%   | 25.60%             | -21.53% |     0.03 |       68 | 38.94%     | ok               |

## LINK-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -11.40%  | -68.73%            | -49.35% |     0.12 |       69 | 41.57%     | ok               |
|          45 | -13.28%  | -68.73%            | -38.11% |     0.05 |       50 | 26.63%     | ok               |
|          50 | -12.86%  | -68.73%            | -36.52% |     0.03 |       40 | 21.26%     | ok               |
|          35 | -24.33%  | -68.73%            | -49.18% |    -0.05 |       59 | 36.78%     | ok               |
|          25 | -34.06%  | -68.73%            | -46.32% |    -0.12 |       68 | 47.13%     | ok               |

## LLY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 25.51%   | 71.65%             | -38.23% |     0.54 |       44 | 38.94%     | ok               |
|          45 | 12.11%   | 71.65%             | -42.66% |     0.32 |       52 | 42.26%     | ok               |
|          15 | 6.12%    | 71.65%             | -48.12% |     0.23 |       63 | 61.90%     | ok               |
|          40 | -4.30%   | 71.65%             | -46.23% |     0.05 |       62 | 44.93%     | ok               |
|          20 | -10.97%  | 71.65%             | -51.34% |    -0.04 |       72 | 56.91%     | ok               |

## LRCX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 6.58%    | 344.29%            | -60.45% |     0.26 |       83 | 55.57%     | ok               |
|          50 | 0.44%    | 344.29%            | -50.39% |     0.16 |       80 | 37.44%     | ok               |
|          40 | -2.58%   | 344.29%            | -56.86% |     0.14 |       72 | 43.26%     | ok               |
|          35 | -8.90%   | 344.29%            | -61.76% |     0.06 |       80 | 45.26%     | ok               |
|          20 | -11.54%  | 344.29%            | -67.64% |     0.04 |       87 | 51.25%     | ok               |

## LTC-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -12.22%  | -63.47%            | -44.78% |    -0    |       56 | 31.80%     | ok               |
|          35 | -22.47%  | -63.47%            | -54.86% |    -0.13 |       66 | 42.91%     | ok               |
|          30 | -34.00%  | -63.47%            | -53.76% |    -0.29 |       66 | 48.47%     | ok               |
|          40 | -31.40%  | -63.47%            | -56.10% |    -0.3  |       58 | 38.12%     | ok               |
|          25 | -36.79%  | -63.47%            | -54.26% |    -0.33 |       74 | 50.96%     | ok               |

## MCD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 2.49%    | -7.80%             | -9.22%  |     0.17 |       42 | 20.47%     | ok               |
|          30 | -2.55%   | -7.80%             | -18.81% |    -0.05 |       75 | 38.10%     | ok               |
|          25 | -3.59%   | -7.80%             | -20.47% |    -0.09 |       75 | 40.77%     | ok               |
|          35 | -7.68%   | -7.80%             | -15.45% |    -0.29 |       67 | 34.44%     | ok               |
|          40 | -7.95%   | -7.80%             | -16.86% |    -0.33 |       71 | 28.79%     | ok               |

## META Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 7.37%    | 40.53%             | -31.03% |     0.24 |       66 | 39.77%     | ok               |
|          40 | -4.43%   | 40.53%             | -35.11% |     0.05 |       66 | 42.76%     | ok               |
|          50 | -9.02%   | 40.53%             | -34.00% |    -0.04 |       70 | 35.94%     | ok               |
|          25 | -13.87%  | 40.53%             | -39.84% |    -0.09 |       67 | 53.41%     | ok               |
|          35 | -15.40%  | 40.53%             | -34.87% |    -0.13 |       77 | 47.59%     | ok               |

## MPC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 14.51%   | 46.28%             | -23.96% |     0.37 |       52 | 38.60%     | ok               |
|          45 | 7.25%    | 46.28%             | -25.09% |     0.24 |       58 | 42.26%     | ok               |
|          40 | 5.62%    | 46.28%             | -25.70% |     0.22 |       60 | 44.59%     | ok               |
|          35 | 2.36%    | 46.28%             | -35.90% |     0.16 |       68 | 47.09%     | ok               |
|          30 | -13.74%  | 46.28%             | -44.76% |    -0.14 |       71 | 49.92%     | ok               |

## MRK Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -18.12%  | -1.69%             | -30.12% |    -0.31 |       87 | 57.24%     | ok               |
|          25 | -17.72%  | -1.69%             | -31.07% |    -0.33 |       72 | 49.25%     | ok               |
|          20 | -21.75%  | -1.69%             | -29.59% |    -0.43 |       77 | 52.58%     | ok               |
|          45 | -20.65%  | -1.69%             | -26.02% |    -0.52 |       57 | 35.44%     | ok               |
|          50 | -19.70%  | -1.69%             | -25.69% |    -0.53 |       56 | 32.28%     | ok               |

## MS Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 1.20%    | 157.97%            | -19.99% |     0.11 |       70 | 40.43%     | ok               |
|          35 | -5.91%   | 157.97%            | -25.26% |    -0.07 |       76 | 45.09%     | ok               |
|          15 | -10.67%  | 157.97%            | -24.00% |    -0.14 |       80 | 57.24%     | ok               |
|          20 | -10.78%  | 157.97%            | -25.68% |    -0.17 |       84 | 53.41%     | ok               |
|          30 | -12.49%  | 157.97%            | -27.79% |    -0.23 |       81 | 48.75%     | ok               |

## MSFT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -18.80%  | -8.48%             | -26.27% |    -0.53 |       66 | 35.27%     | ok               |
|          50 | -22.46%  | -8.48%             | -28.83% |    -0.68 |       64 | 30.62%     | ok               |
|          35 | -30.45%  | -8.48%             | -33.68% |    -0.81 |       75 | 43.59%     | ok               |
|          25 | -33.84%  | -8.48%             | -37.59% |    -0.86 |       87 | 51.25%     | ok               |
|          40 | -31.27%  | -8.48%             | -34.46% |    -0.88 |       71 | 38.60%     | ok               |

## MU Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 421.65%  | 1120.72%           | -61.96% |     1.55 |       48 | 68.05%     | ok               |
|          25 | 334.60%  | 1120.72%           | -67.90% |     1.46 |       49 | 61.73%     | ok               |
|          40 | 288.27%  | 1120.72%           | -64.30% |     1.4  |       56 | 55.07%     | ok               |
|          20 | 297.89%  | 1120.72%           | -67.25% |     1.37 |       55 | 63.89%     | ok               |
|          30 | 270.20%  | 1120.72%           | -68.76% |     1.34 |       51 | 59.90%     | ok               |

## NEAR-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 99.44%   | -60.14%            | -48.95% |     0.97 |       44 | 23.18%     | ok               |
|          50 | 70.90%   | -60.14%            | -53.13% |     0.82 |       38 | 18.39%     | ok               |
|          40 | 57.99%   | -60.14%            | -57.15% |     0.71 |       48 | 27.59%     | ok               |
|          35 | 31.48%   | -60.14%            | -61.02% |     0.51 |       70 | 32.95%     | ok               |
|          15 | 2.55%    | -60.14%            | -54.94% |     0.32 |       87 | 57.09%     | ok               |

## NEM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 17.58%   | 183.51%            | -29.41% |     0.37 |       62 | 63.89%     | ok               |
|          20 | 6.51%    | 183.51%            | -30.47% |     0.25 |       74 | 59.40%     | ok               |
|          50 | -13.83%  | 183.51%            | -33.36% |    -0.07 |       60 | 41.43%     | ok               |
|          25 | -17.51%  | 183.51%            | -37.89% |    -0.08 |       72 | 56.91%     | ok               |
|          30 | -29.66%  | 183.51%            | -38.49% |    -0.3  |       78 | 54.58%     | ok               |

## NFLX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 64.73%   | 29.38%             | -11.94% |     1.27 |       46 | 47.25%     | ok               |
|          50 | 50.73%   | 29.38%             | -16.28% |     1.12 |       48 | 39.77%     | ok               |
|          35 | 55.75%   | 29.38%             | -18.30% |     1.08 |       62 | 50.92%     | ok               |
|          45 | 46.92%   | 29.38%             | -15.48% |     1.02 |       52 | 43.59%     | ok               |
|          25 | 44.72%   | 29.38%             | -21.09% |     0.88 |       62 | 57.40%     | ok               |

## NKE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -35.58%  | -59.32%            | -50.44% |    -0.46 |       95 | 52.75%     | ok               |
|          40 | -26.46%  | -59.32%            | -31.19% |    -0.5  |       63 | 30.12%     | ok               |
|          15 | -39.58%  | -59.32%            | -55.52% |    -0.54 |       96 | 57.40%     | ok               |
|          35 | -39.10%  | -59.32%            | -43.08% |    -0.8  |       75 | 37.10%     | ok               |
|          50 | -24.86%  | -59.32%            | -31.53% |    -0.82 |       46 | 17.14%     | ok               |

## NOW Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 24.34%   | -38.95%            | -26.36% |     0.44 |       77 | 51.75%     | ok               |
|          30 | 21.71%   | -38.95%            | -30.25% |     0.42 |       80 | 45.92%     | ok               |
|          15 | 17.55%   | -38.95%            | -26.36% |     0.37 |       88 | 55.07%     | ok               |
|          25 | 14.79%   | -38.95%            | -25.70% |     0.34 |       72 | 49.25%     | ok               |
|          35 | 13.84%   | -38.95%            | -29.30% |     0.34 |       81 | 40.60%     | ok               |

## NVDA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -5.82%   | 121.65%            | -33.22% |     0.09 |       68 | 50.62%     | ok               |
|          30 | -7.59%   | 121.65%            | -35.26% |     0.04 |       70 | 48.31%     | ok               |
|          20 | -12.07%  | 121.65%            | -40.59% |     0.01 |       71 | 55.08%     | ok               |
|          50 | -15.20%  | 121.65%            | -40.84% |    -0.12 |       58 | 32.44%     | ok               |
|          35 | -18.42%  | 121.65%            | -41.25% |    -0.15 |       82 | 45.45%     | ok               |

## OP-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 74.65%   | -94.05%            | -45.76% |     0.86 |       36 | 17.43%     | ok               |
|          50 | 66.86%   | -94.05%            | -36.11% |     0.86 |       34 | 12.45%     | ok               |
|          40 | 58.63%   | -94.05%            | -53.61% |     0.72 |       52 | 26.63%     | ok               |
|          35 | 17.28%   | -94.05%            | -61.07% |     0.39 |       58 | 29.69%     | ok               |
|          30 | -4.12%   | -94.05%            | -72.42% |     0.21 |       74 | 36.21%     | ok               |

## ORCL Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 162.46%  | 44.67%             | -29.32% |     1.13 |       74 | 65.22%     | ok               |
|          25 | 96.88%   | 44.67%             | -27.76% |     0.87 |       75 | 57.74%     | ok               |
|          20 | 93.50%   | 44.67%             | -29.32% |     0.84 |       77 | 60.90%     | ok               |
|          35 | 68.81%   | 44.67%             | -31.95% |     0.73 |       68 | 49.42%     | ok               |
|          30 | 68.95%   | 44.67%             | -29.47% |     0.72 |       74 | 53.58%     | ok               |

## OXY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 2.48%    | -11.32%            | -30.85% |     0.16 |       63 | 43.09%     | ok               |
|          35 | -0.66%   | -11.32%            | -30.50% |     0.1  |       68 | 38.60%     | ok               |
|          50 | -2.35%   | -11.32%            | -31.07% |     0.05 |       40 | 27.79%     | ok               |
|          40 | -3.09%   | -11.32%            | -32.21% |     0.05 |       56 | 34.61%     | ok               |
|          25 | -11.70%  | -11.32%            | -40.42% |    -0.09 |       71 | 46.59%     | ok               |

## PEP Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 9.77%    | -16.25%            | -11.62% |     0.45 |       46 | 27.79%     | ok               |
|          45 | -0.55%   | -16.25%            | -14.22% |     0.03 |       70 | 32.61%     | ok               |
|          40 | -4.05%   | -16.25%            | -18.04% |    -0.09 |       78 | 38.44%     | ok               |
|          35 | -5.62%   | -16.25%            | -21.42% |    -0.12 |       87 | 43.43%     | ok               |
|          30 | -10.61%  | -16.25%            | -21.35% |    -0.25 |       85 | 50.08%     | ok               |

## PEPE-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 21.63%   | -83.17%            | -57.66% |     0.45 |       75 | 43.68%     | ok               |
|          15 | 13.75%   | -83.17%            | -61.96% |     0.43 |       74 | 59.00%     | ok               |
|          35 | 14.70%   | -83.17%            | -51.35% |     0.39 |       60 | 38.31%     | ok               |
|          25 | -0.45%   | -83.17%            | -53.88% |     0.28 |       81 | 48.85%     | ok               |
|          20 | -11.32%  | -83.17%            | -61.13% |     0.2  |       80 | 55.36%     | ok               |

## PFE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -25.59%  | -8.51%             | -26.78% |    -0.93 |       52 | 20.47%     | ok               |
|          40 | -31.90%  | -8.51%             | -32.98% |    -1.12 |       76 | 25.29%     | ok               |
|          50 | -27.85%  | -8.51%             | -28.02% |    -1.12 |       44 | 16.64%     | ok               |
|          35 | -34.38%  | -8.51%             | -36.39% |    -1.12 |       82 | 32.28%     | ok               |
|          30 | -40.46%  | -8.51%             | -42.29% |    -1.3  |       77 | 35.77%     | ok               |

## PG Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -0.54%   | -4.21%             | -19.77% |     0.03 |       52 | 34.94%     | ok               |
|          35 | -2.75%   | -4.21%             | -18.66% |    -0.06 |       60 | 38.27%     | ok               |
|          30 | -11.59%  | -4.21%             | -21.65% |    -0.41 |       62 | 41.43%     | ok               |
|          45 | -10.26%  | -4.21%             | -20.43% |    -0.42 |       52 | 32.45%     | ok               |
|          25 | -12.65%  | -4.21%             | -22.55% |    -0.45 |       72 | 42.60%     | ok               |

## PM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | -0.99%   | 94.74%             | -32.20% |     0.07 |       90 | 53.58%     | ok               |
|          20 | -3.75%   | 94.74%             | -31.89% |     0.02 |       87 | 62.56%     | ok               |
|          30 | -4.17%   | 94.74%             | -33.68% |     0.01 |       83 | 57.57%     | ok               |
|          50 | -5.49%   | 94.74%             | -35.70% |    -0.06 |       74 | 41.93%     | ok               |
|          25 | -10.63%  | 94.74%             | -37.05% |    -0.14 |       81 | 59.90%     | ok               |

## POL-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 64.83%   | -82.58%            | -46.45% |     0.77 |       79 | 49.62%     | ok               |
|          25 | 51.54%   | -82.58%            | -46.72% |     0.66 |       68 | 57.66%     | ok               |
|          20 | 41.20%   | -82.58%            | -52.88% |     0.58 |       76 | 63.03%     | ok               |
|          15 | 40.10%   | -82.58%            | -58.42% |     0.57 |       76 | 68.39%     | ok               |
|          50 | 20.67%   | -82.58%            | -22.86% |     0.45 |       50 | 20.69%     | ok               |

## QCOM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -1.27%   | 39.83%             | -55.66% |     0.16 |       73 | 49.42%     | ok               |
|          35 | -3.59%   | 39.83%             | -51.84% |     0.12 |       83 | 44.76%     | ok               |
|          20 | -5.28%   | 39.83%             | -55.54% |     0.11 |       69 | 52.25%     | ok               |
|          30 | -14.12%  | 39.83%             | -57.69% |    -0.02 |       77 | 47.42%     | ok               |
|          15 | -21.02%  | 39.83%             | -59.01% |    -0.1  |       73 | 55.41%     | ok               |

## QQQ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | 23.79%   | 67.80%             | -12.88% |     0.64 |       57 | 48.92%     | ok               |
|          15 | 24.32%   | 67.80%             | -14.17% |     0.6  |       61 | 54.41%     | ok               |
|          30 | 19.74%   | 67.80%             | -12.88% |     0.56 |       62 | 46.09%     | ok               |
|          20 | 20.79%   | 67.80%             | -12.98% |     0.55 |       65 | 51.58%     | ok               |
|          35 | 7.50%    | 67.80%             | -18.29% |     0.28 |       68 | 42.43%     | ok               |

## RENDER-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 49.72%   | -61.68%            | -43.43% |     0.65 |       84 | 53.78%     | ok               |
|          15 | 32.34%   | -61.68%            | -44.59% |     0.55 |       84 | 56.85%     | ok               |
|          25 | 20.05%   | -61.68%            | -40.60% |     0.46 |       88 | 49.90%     | ok               |
|          30 | -17.59%  | -61.68%            | -45.00% |     0.11 |       96 | 43.56%     | ok               |
|          40 | -27.22%  | -61.68%            | -38.60% |    -0.1  |       70 | 29.04%     | ok               |

## RTX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 26.55%   | 105.73%            | -18.66% |     0.65 |       78 | 56.24%     | ok               |
|          25 | 22.06%   | 105.73%            | -18.59% |     0.57 |       64 | 52.75%     | ok               |
|          30 | 20.20%   | 105.73%            | -16.99% |     0.54 |       58 | 51.58%     | ok               |
|          35 | 17.67%   | 105.73%            | -18.00% |     0.53 |       56 | 49.75%     | ok               |
|          50 | 16.39%   | 105.73%            | -18.42% |     0.53 |       58 | 41.93%     | ok               |

## SBUX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -17.81%  | 7.41%              | -23.55% |    -0.32 |       65 | 41.26%     | ok               |
|          40 | -22.46%  | 7.41%              | -27.00% |    -0.51 |       62 | 33.11%     | ok               |
|          30 | -24.83%  | 7.41%              | -29.34% |    -0.51 |       64 | 38.94%     | ok               |
|          45 | -22.03%  | 7.41%              | -27.26% |    -0.54 |       68 | 29.28%     | ok               |
|          20 | -29.47%  | 7.41%              | -34.85% |    -0.58 |       70 | 43.26%     | ok               |

## SCHW Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 2.59%    | 44.72%             | -15.92% |     0.15 |       54 | 33.44%     | ok               |
|          50 | -1.42%   | 44.72%             | -11.75% |     0.01 |       50 | 30.95%     | ok               |
|          25 | -9.15%   | 44.72%             | -28.76% |    -0.13 |       63 | 47.92%     | ok               |
|          40 | -8.05%   | 44.72%             | -21.81% |    -0.15 |       62 | 36.44%     | ok               |
|          20 | -10.84%  | 44.72%             | -29.24% |    -0.17 |       71 | 50.58%     | ok               |

## SHIB-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 2.53%    | -77.51%            | -49.21% |     0.27 |       78 | 68.58%     | ok               |
|          25 | -7.29%   | -77.51%            | -43.86% |     0.16 |       73 | 59.96%     | ok               |
|          20 | -8.55%   | -77.51%            | -46.38% |     0.15 |       77 | 63.98%     | ok               |
|          35 | -10.90%  | -77.51%            | -52.43% |     0.08 |       64 | 47.13%     | ok               |
|          40 | -15.59%  | -77.51%            | -49.00% |     0.01 |       56 | 38.89%     | ok               |

## SHY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd    |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:-------|---------:|---------:|:-----------|:-----------------|
|          30 | -2.26%   | -0.22%             | -2.85% |    -0.79 |       50 | 34.61%     | ok               |
|          35 | -2.38%   | -0.22%             | -3.27% |    -0.84 |       52 | 32.78%     | ok               |
|          40 | -2.50%   | -0.22%             | -3.33% |    -0.89 |       52 | 30.95%     | ok               |
|          45 | -2.47%   | -0.22%             | -3.23% |    -0.9  |       50 | 27.79%     | ok               |
|          50 | -2.65%   | -0.22%             | -3.40% |    -1.02 |       46 | 24.96%     | ok               |

## SKY-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -34.15%  | -3.84%             | -56.39% |    -0.39 |       58 | 50.93%     | ok               |
|          30 | -29.87%  | -3.84%             | -43.98% |    -0.39 |       68 | 40.51%     | ok               |
|          25 | -33.46%  | -3.84%             | -48.09% |    -0.45 |       63 | 44.21%     | ok               |
|          20 | -43.60%  | -3.84%             | -58.40% |    -0.64 |       60 | 47.92%     | ok               |
|          35 | -40.88%  | -3.84%             | -49.68% |    -0.75 |       62 | 34.03%     | ok               |

## SLB Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 19.99%   | -3.16%             | -24.10% |     0.49 |       46 | 35.44%     | ok               |
|          45 | 18.22%   | -3.16%             | -21.53% |     0.47 |       52 | 32.11%     | ok               |
|          50 | -2.98%   | -3.16%             | -29.84% |     0.01 |       52 | 28.45%     | ok               |
|          35 | -11.13%  | -3.16%             | -43.22% |    -0.13 |       72 | 43.26%     | ok               |
|          30 | -25.47%  | -3.16%             | -55.49% |    -0.44 |       75 | 49.58%     | ok               |

## SLV Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 69.82%   | 163.00%            | -34.10% |     0.88 |       52 | 33.44%     | ok               |
|          45 | 67.13%   | 163.00%            | -31.82% |     0.86 |       56 | 34.28%     | ok               |
|          40 | 65.13%   | 163.00%            | -31.93% |     0.84 |       62 | 36.44%     | ok               |
|          35 | 52.07%   | 163.00%            | -36.89% |     0.72 |       64 | 38.60%     | ok               |
|          30 | 43.23%   | 163.00%            | -42.66% |     0.64 |       58 | 40.77%     | ok               |

## SMH Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 124.29%  | 229.84%            | -30.17% |     1.37 |       47 | 53.24%     | ok               |
|          35 | 100.73%  | 229.84%            | -34.36% |     1.25 |       54 | 49.08%     | ok               |
|          25 | 100.58%  | 229.84%            | -32.94% |     1.23 |       46 | 52.08%     | ok               |
|          30 | 98.22%   | 229.84%            | -33.99% |     1.22 |       48 | 50.42%     | ok               |
|          45 | 83.80%   | 229.84%            | -32.75% |     1.18 |       52 | 43.26%     | ok               |

## SNX-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 41.50%   | -85.87%            | -43.20% |     0.58 |       73 | 50.00%     | ok               |
|          35 | 32.60%   | -85.87%            | -28.28% |     0.53 |       64 | 32.95%     | ok               |
|          30 | 19.87%   | -85.87%            | -32.91% |     0.42 |       60 | 40.04%     | ok               |
|          25 | 12.79%   | -85.87%            | -38.01% |     0.37 |       72 | 44.64%     | ok               |
|          15 | -4.70%   | -85.87%            | -44.00% |     0.24 |       83 | 54.60%     | ok               |

## SOL-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -6.90%   | -72.39%            | -49.00% |     0.17 |       62 | 39.66%     | ok               |
|          35 | -24.24%  | -72.39%            | -57.20% |    -0    |       70 | 47.13%     | ok               |
|          25 | -29.34%  | -72.39%            | -51.59% |    -0.05 |       68 | 57.28%     | ok               |
|          15 | -33.90%  | -72.39%            | -56.45% |    -0.09 |       75 | 64.18%     | ok               |
|          30 | -35.44%  | -72.39%            | -57.97% |    -0.15 |       74 | 53.07%     | ok               |

## SOXX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 102.23%  | 204.40%            | -38.67% |     1.18 |       53 | 51.91%     | ok               |
|          25 | 98.36%   | 204.40%            | -39.85% |     1.16 |       51 | 51.58%     | ok               |
|          35 | 92.82%   | 204.40%            | -38.63% |     1.14 |       59 | 46.92%     | ok               |
|          15 | 97.15%   | 204.40%            | -37.72% |     1.11 |       66 | 54.74%     | ok               |
|          30 | 87.22%   | 204.40%            | -40.34% |     1.08 |       55 | 49.42%     | ok               |

## SPY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 17.82%   | 49.44%             | -14.25% |     0.61 |       58 | 54.41%     | ok               |
|          15 | 16.21%   | 49.44%             | -16.80% |     0.55 |       67 | 57.57%     | ok               |
|          25 | 10.49%   | 49.44%             | -15.22% |     0.4  |       58 | 53.41%     | ok               |
|          30 | 6.50%    | 49.44%             | -16.47% |     0.28 |       60 | 50.92%     | ok               |
|          35 | 3.93%    | 49.44%             | -16.72% |     0.2  |       58 | 48.25%     | ok               |

## SUSHI-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -23.49%  | -87.69%            | -40.08% |    -0.19 |       52 | 14.75%     | ok               |
|          45 | -55.77%  | -87.69%            | -64.27% |    -0.7  |       54 | 18.01%     | ok               |
|          40 | -58.91%  | -87.69%            | -66.57% |    -0.7  |       61 | 24.52%     | ok               |
|          15 | -76.99%  | -87.69%            | -78.98% |    -0.89 |       87 | 46.93%     | ok               |
|          35 | -71.87%  | -87.69%            | -78.94% |    -0.97 |       76 | 30.08%     | ok               |

## T Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 55.27%   | 30.12%             | -18.13% |     1.11 |       55 | 55.41%     | ok               |
|          25 | 47.31%   | 30.12%             | -17.66% |     1.01 |       60 | 53.08%     | ok               |
|          15 | 46.79%   | 30.12%             | -15.08% |     0.96 |       64 | 59.23%     | ok               |
|          30 | 32.61%   | 30.12%             | -17.01% |     0.78 |       62 | 50.92%     | ok               |
|          35 | 30.11%   | 30.12%             | -14.49% |     0.74 |       62 | 47.75%     | ok               |

## TGT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -8.23%   | -4.56%             | -41.89% |    -0.05 |       79 | 46.09%     | ok               |
|          25 | -9.14%   | -4.56%             | -42.39% |    -0.09 |       61 | 41.10%     | ok               |
|          15 | -11.23%  | -4.56%             | -39.76% |    -0.1  |       69 | 50.58%     | ok               |
|          45 | -8.37%   | -4.56%             | -29.07% |    -0.12 |       50 | 28.79%     | ok               |
|          30 | -10.02%  | -4.56%             | -40.57% |    -0.12 |       56 | 38.44%     | ok               |

## TIA-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 37.17%   | -91.75%            | -31.28% |     0.56 |       62 | 25.29%     | ok               |
|          35 | 31.50%   | -91.75%            | -37.98% |     0.51 |       62 | 29.89%     | ok               |
|          45 | 13.19%   | -91.75%            | -45.43% |     0.34 |       52 | 18.77%     | ok               |
|          50 | 12.07%   | -91.75%            | -44.86% |     0.33 |       32 | 11.69%     | ok               |
|          30 | -17.99%  | -91.75%            | -56.16% |     0.06 |       86 | 34.87%     | ok               |

## TLT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -21.57%  | -9.95%             | -23.63% |    -1.59 |       72 | 31.78%     | ok               |
|          50 | -15.89%  | -9.95%             | -17.64% |    -1.81 |       32 | 14.14%     | ok               |
|          15 | -27.89%  | -9.95%             | -30.27% |    -1.89 |       77 | 39.93%     | ok               |
|          35 | -22.74%  | -9.95%             | -24.76% |    -1.9  |       64 | 25.79%     | ok               |
|          40 | -21.20%  | -9.95%             | -23.26% |    -1.9  |       58 | 21.13%     | ok               |

## TMO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 37.00%   | -17.24%            | -8.17%  |     0.87 |       38 | 30.12%     | ok               |
|          45 | 36.24%   | -17.24%            | -10.13% |     0.83 |       46 | 35.11%     | ok               |
|          40 | 34.23%   | -17.24%            | -9.91%  |     0.78 |       49 | 39.60%     | ok               |
|          35 | 18.76%   | -17.24%            | -14.06% |     0.48 |       59 | 43.93%     | ok               |
|          30 | 6.96%    | -17.24%            | -16.83% |     0.24 |       59 | 47.75%     | ok               |

## TMUS Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 14.84%   | 14.14%             | -24.50% |     0.4  |       70 | 47.75%     | ok               |
|          15 | 14.07%   | 14.14%             | -26.87% |     0.38 |       71 | 59.90%     | ok               |
|          20 | 7.07%    | 14.14%             | -24.82% |     0.25 |       73 | 54.24%     | ok               |
|          25 | 5.07%    | 14.14%             | -26.28% |     0.2  |       77 | 50.42%     | ok               |
|          50 | 4.50%    | 14.14%             | -22.71% |     0.2  |       58 | 35.77%     | ok               |

## TRX-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 1.57%    | 43.93%             | -18.79% |     0.13 |       54 | 38.31%     | ok               |
|          30 | 1.02%    | 43.93%             | -22.90% |     0.12 |       74 | 49.62%     | ok               |
|          35 | -0.36%   | 43.93%             | -21.77% |     0.08 |       70 | 46.93%     | ok               |
|          25 | -0.80%   | 43.93%             | -26.84% |     0.07 |       70 | 52.87%     | ok               |
|          50 | -1.81%   | 43.93%             | -18.49% |     0.02 |       46 | 32.76%     | ok               |

## TSLA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 71.13%   | 99.18%             | -32.60% |     0.85 |       64 | 30.28%     | ok               |
|          40 | 62.51%   | 99.18%             | -45.90% |     0.73 |       61 | 34.78%     | ok               |
|          45 | 37.67%   | 99.18%             | -46.86% |     0.55 |       65 | 32.11%     | ok               |
|          35 | 18.49%   | 99.18%             | -54.51% |     0.38 |       74 | 37.77%     | ok               |
|          30 | -3.79%   | 99.18%             | -57.89% |     0.17 |       68 | 42.26%     | ok               |

## TXN Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 13.31%   | 87.82%             | -45.45% |     0.33 |       70 | 35.27%     | ok               |
|          20 | 2.88%    | 87.82%             | -38.98% |     0.19 |       62 | 59.90%     | ok               |
|          15 | 0.75%    | 87.82%             | -39.48% |     0.17 |       65 | 64.06%     | ok               |
|          40 | -3.13%   | 87.82%             | -45.67% |     0.08 |       76 | 47.75%     | ok               |
|          35 | -4.23%   | 87.82%             | -43.38% |     0.07 |       78 | 50.08%     | ok               |

## UNH Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 27.67%   | -18.74%            | -36.91% |     0.52 |       50 | 29.45%     | ok               |
|          30 | 26.10%   | -18.74%            | -27.46% |     0.48 |       76 | 52.08%     | ok               |
|          35 | 21.44%   | -18.74%            | -29.39% |     0.43 |       70 | 46.76%     | ok               |
|          15 | 21.65%   | -18.74%            | -30.48% |     0.42 |       79 | 67.05%     | ok               |
|          20 | 18.77%   | -18.74%            | -31.00% |     0.39 |       81 | 61.90%     | ok               |

## UNI-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -18.07%  | -77.89%            | -58.49% |    -0    |       54 | 25.67%     | ok               |
|          40 | -23.44%  | -77.89%            | -63.75% |    -0.05 |       56 | 30.65%     | ok               |
|          50 | -25.51%  | -77.89%            | -57.60% |    -0.14 |       52 | 21.07%     | ok               |
|          35 | -35.75%  | -77.89%            | -68.71% |    -0.18 |       70 | 35.63%     | ok               |
|          20 | -74.18%  | -77.89%            | -81.62% |    -0.79 |      102 | 52.30%     | ok               |

## UPS Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -37.04%  | -27.04%            | -42.28% |    -0.72 |       76 | 44.76%     | ok               |
|          35 | -35.79%  | -27.04%            | -40.47% |    -0.72 |       61 | 34.44%     | ok               |
|          20 | -38.09%  | -27.04%            | -45.80% |    -0.73 |       82 | 47.92%     | ok               |
|          30 | -38.15%  | -27.04%            | -40.62% |    -0.77 |       68 | 40.10%     | ok               |
|          40 | -37.07%  | -27.04%            | -42.12% |    -0.78 |       53 | 29.28%     | ok               |

## USO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 15.25%   | 52.81%             | -33.25% |     0.36 |       46 | 27.45%     | ok               |
|          30 | 2.80%    | 52.81%             | -43.35% |     0.17 |       68 | 34.44%     | ok               |
|          40 | 1.81%    | 52.81%             | -41.14% |     0.15 |       57 | 29.95%     | ok               |
|          50 | 2.11%    | 52.81%             | -31.13% |     0.15 |       54 | 24.96%     | ok               |
|          25 | -1.92%   | 52.81%             | -45.95% |     0.1  |       68 | 36.94%     | ok               |

## VEA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 5.44%    | 47.26%             | -16.28% |     0.25 |       60 | 50.58%     | ok               |
|          20 | 1.19%    | 47.26%             | -17.70% |     0.1  |       61 | 47.92%     | ok               |
|          25 | -0.82%   | 47.26%             | -17.79% |     0.02 |       57 | 46.26%     | ok               |
|          30 | -0.98%   | 47.26%             | -17.93% |     0.01 |       58 | 44.09%     | ok               |
|          35 | -2.09%   | 47.26%             | -16.79% |    -0.03 |       56 | 43.09%     | ok               |

## VIXY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -46.17%  | -59.94%            | -68.69% |    -0.39 |       44 | 10.32%     | ok               |
|          45 | -56.13%  | -59.94%            | -74.13% |    -0.55 |       56 | 16.31%     | ok               |
|          40 | -64.45%  | -59.94%            | -80.03% |    -0.66 |       70 | 20.63%     | ok               |
|          35 | -68.17%  | -59.94%            | -83.81% |    -0.7  |       86 | 25.79%     | ok               |
|          15 | -77.14%  | -59.94%            | -89.47% |    -0.77 |      101 | 44.76%     | ok               |

## VNQ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -8.60%   | 15.54%             | -19.07% |    -0.37 |       60 | 28.62%     | ok               |
|          50 | -9.03%   | 15.54%             | -17.13% |    -0.41 |       56 | 26.12%     | ok               |
|          25 | -13.12%  | 15.54%             | -22.34% |    -0.51 |       69 | 40.77%     | ok               |
|          40 | -14.13%  | 15.54%             | -24.84% |    -0.62 |       74 | 32.11%     | ok               |
|          20 | -16.52%  | 15.54%             | -23.79% |    -0.64 |       74 | 43.59%     | ok               |

## VTI Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 19.45%   | 49.07%             | -13.96% |     0.65 |       62 | 55.57%     | ok               |
|          15 | 13.34%   | 49.07%             | -15.70% |     0.47 |       65 | 58.07%     | ok               |
|          25 | 6.49%    | 49.07%             | -16.10% |     0.28 |       58 | 53.74%     | ok               |
|          30 | -0.58%   | 49.07%             | -18.77% |     0.04 |       66 | 51.91%     | ok               |
|          40 | -2.82%   | 49.07%             | -20.44% |    -0.05 |       68 | 45.26%     | ok               |

## VWO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -6.69%   | 49.18%             | -21.68% |    -0.22 |       58 | 32.61%     | ok               |
|          15 | -9.03%   | 49.18%             | -24.01% |    -0.26 |       69 | 49.42%     | ok               |
|          45 | -8.51%   | 49.18%             | -23.75% |    -0.3  |       60 | 35.11%     | ok               |
|          20 | -10.06%  | 49.18%             | -26.14% |    -0.31 |       67 | 47.25%     | ok               |
|          40 | -8.98%   | 49.18%             | -23.57% |    -0.31 |       70 | 37.94%     | ok               |

## VZ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -6.39%   | 10.03%             | -16.98% |    -0.18 |       50 | 25.12%     | ok               |
|          45 | -14.79%  | 10.03%             | -20.38% |    -0.49 |       58 | 28.12%     | ok               |
|          35 | -19.83%  | 10.03%             | -24.68% |    -0.66 |       61 | 33.61%     | ok               |
|          25 | -25.16%  | 10.03%             | -28.84% |    -0.79 |       80 | 41.76%     | ok               |
|          40 | -22.61%  | 10.03%             | -26.72% |    -0.8  |       64 | 30.62%     | ok               |

## WFC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -0.64%   | 64.35%             | -18.29% |     0.05 |       58 | 33.44%     | ok               |
|          35 | -4.95%   | 64.35%             | -22.53% |    -0.03 |       79 | 45.09%     | ok               |
|          45 | -7.94%   | 64.35%             | -24.02% |    -0.16 |       66 | 38.10%     | ok               |
|          20 | -16.63%  | 64.35%             | -29.96% |    -0.23 |       79 | 54.41%     | ok               |
|          40 | -11.62%  | 64.35%             | -24.88% |    -0.27 |       76 | 41.43%     | ok               |

## WIF-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 60.65%   | -89.76%            | -46.21% |     0.66 |       71 | 41.38%     | ok               |
|          20 | 54.98%   | -89.76%            | -40.67% |     0.64 |       65 | 38.70%     | ok               |
|          25 | -11.37%  | -89.76%            | -52.41% |     0.2  |       67 | 36.21%     | ok               |
|          50 | -20.06%  | -89.76%            | -37.87% |    -0.14 |       40 | 12.07%     | ok               |
|          30 | -43.81%  | -89.76%            | -57.06% |    -0.24 |       68 | 32.18%     | ok               |

## WMT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 60.53%   | 116.35%            | -9.18%  |     1.56 |       36 | 43.76%     | ok               |
|          50 | 54.00%   | 116.35%            | -12.19% |     1.5  |       30 | 41.60%     | ok               |
|          40 | 50.49%   | 116.35%            | -9.18%  |     1.33 |       40 | 44.93%     | ok               |
|          35 | 48.27%   | 116.35%            | -10.11% |     1.24 |       50 | 48.92%     | ok               |
|          30 | 26.80%   | 116.35%            | -21.31% |     0.73 |       57 | 51.41%     | ok               |

## XBI Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 4.14%    | 65.63%             | -16.56% |     0.19 |       60 | 34.78%     | ok               |
|          45 | 3.34%    | 65.63%             | -16.74% |     0.17 |       52 | 31.61%     | ok               |
|          35 | -0.17%   | 65.63%             | -21.24% |     0.08 |       60 | 38.10%     | ok               |
|          30 | -1.28%   | 65.63%             | -21.61% |     0.05 |       60 | 39.77%     | ok               |
|          25 | -5.82%   | 65.63%             | -24.65% |    -0.05 |       68 | 41.76%     | ok               |

## XLB Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -4.67%   | 22.14%             | -20.60% |    -0.12 |       60 | 32.11%     | ok               |
|          50 | -4.61%   | 22.14%             | -17.40% |    -0.14 |       44 | 27.79%     | ok               |
|          35 | -7.91%   | 22.14%             | -23.62% |    -0.24 |       60 | 35.61%     | ok               |
|          45 | -7.43%   | 22.14%             | -20.61% |    -0.25 |       44 | 29.28%     | ok               |
|          25 | -12.31%  | 22.14%             | -23.73% |    -0.4  |       70 | 41.43%     | ok               |

## XLC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 17.35%   | 37.88%             | -12.33% |     0.58 |       65 | 55.57%     | ok               |
|          25 | 15.14%   | 37.88%             | -12.31% |     0.52 |       62 | 57.40%     | ok               |
|          40 | 12.63%   | 37.88%             | -13.38% |     0.48 |       68 | 48.25%     | ok               |
|          35 | 12.00%   | 37.88%             | -13.38% |     0.45 |       64 | 52.58%     | ok               |
|          20 | 7.05%    | 37.88%             | -13.78% |     0.27 |       70 | 60.07%     | ok               |

## XLE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -1.92%   | 28.14%             | -25.98% |     0.02 |       56 | 36.77%     | ok               |
|          35 | -3.79%   | 28.14%             | -32.17% |    -0.02 |       65 | 44.59%     | ok               |
|          45 | -5.17%   | 28.14%             | -30.88% |    -0.07 |       62 | 39.60%     | ok               |
|          30 | -9.48%   | 28.14%             | -36.18% |    -0.17 |       71 | 46.59%     | ok               |
|          25 | -10.53%  | 28.14%             | -36.92% |    -0.18 |       78 | 49.92%     | ok               |

## XLF Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -6.34%   | 37.31%             | -18.01% |    -0.16 |       68 | 53.91%     | ok               |
|          15 | -10.21%  | 37.31%             | -19.58% |    -0.29 |       76 | 56.74%     | ok               |
|          30 | -12.11%  | 37.31%             | -23.61% |    -0.4  |       76 | 48.25%     | ok               |
|          25 | -12.87%  | 37.31%             | -23.22% |    -0.42 |       77 | 50.42%     | ok               |
|          35 | -18.14%  | 37.31%             | -25.31% |    -0.72 |       66 | 44.76%     | ok               |

## XLI Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 11.03%   | 55.98%             | -10.36% |     0.43 |       72 | 53.08%     | ok               |
|          20 | 6.70%    | 55.98%             | -12.74% |     0.3  |       63 | 48.92%     | ok               |
|          30 | 4.36%    | 55.98%             | -11.38% |     0.22 |       64 | 46.42%     | ok               |
|          45 | 3.76%    | 55.98%             | -12.27% |     0.21 |       62 | 37.60%     | ok               |
|          50 | 3.45%    | 55.98%             | -9.25%  |     0.2  |       56 | 35.61%     | ok               |

## XLK Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 84.66%   | 82.44%             | -14.75% |     1.34 |       41 | 53.41%     | ok               |
|          20 | 70.21%   | 82.44%             | -14.75% |     1.21 |       48 | 51.25%     | ok               |
|          25 | 66.75%   | 82.44%             | -14.75% |     1.2  |       42 | 49.08%     | ok               |
|          30 | 64.57%   | 82.44%             | -14.75% |     1.2  |       42 | 47.92%     | ok               |
|          35 | 46.21%   | 82.44%             | -13.61% |     0.96 |       54 | 45.26%     | ok               |

## XLM-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 26.14%   | -54.72%            | -38.97% |     0.48 |       44 | 27.39%     | ok               |
|          45 | 22.34%   | -54.72%            | -43.99% |     0.44 |       50 | 31.03%     | ok               |
|          30 | 0.26%    | -54.72%            | -50.36% |     0.22 |       69 | 45.59%     | ok               |
|          40 | -3.03%   | -54.72%            | -43.80% |     0.17 |       49 | 35.25%     | ok               |
|          35 | -8.51%   | -54.72%            | -50.42% |     0.12 |       69 | 41.57%     | ok               |

## XLP Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 11.54%   | 13.97%             | -5.66%  |     0.71 |       56 | 33.78%     | ok               |
|          50 | 9.52%    | 13.97%             | -6.08%  |     0.6  |       58 | 31.61%     | ok               |
|          40 | 9.29%    | 13.97%             | -7.77%  |     0.56 |       72 | 37.94%     | ok               |
|          35 | 8.34%    | 13.97%             | -9.73%  |     0.5  |       68 | 40.93%     | ok               |
|          30 | 7.46%    | 13.97%             | -10.28% |     0.45 |       70 | 42.60%     | ok               |

## XLU Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 8.58%    | 46.38%             | -9.11%  |     0.45 |       50 | 30.28%     | ok               |
|          45 | 6.34%    | 46.38%             | -10.56% |     0.35 |       54 | 31.28%     | ok               |
|          40 | 2.95%    | 46.38%             | -11.94% |     0.18 |       60 | 32.95%     | ok               |
|          35 | -3.87%   | 46.38%             | -16.24% |    -0.14 |       66 | 35.61%     | ok               |
|          30 | -6.68%   | 46.38%             | -18.15% |    -0.26 |       71 | 38.94%     | ok               |

## XLV Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -11.29%  | 8.26%              | -16.83% |    -0.54 |       68 | 36.11%     | ok               |
|          25 | -12.59%  | 8.26%              | -18.06% |    -0.61 |       70 | 37.44%     | ok               |
|          15 | -16.56%  | 8.26%              | -21.47% |    -0.79 |       81 | 42.26%     | ok               |
|          20 | -16.49%  | 8.26%              | -21.56% |    -0.81 |       75 | 39.10%     | ok               |
|          35 | -15.92%  | 8.26%              | -20.96% |    -0.85 |       66 | 33.61%     | ok               |

## XLY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 3.17%    | 30.69%             | -12.94% |     0.17 |       72 | 41.60%     | ok               |
|          30 | 1.32%    | 30.69%             | -14.01% |     0.11 |       72 | 44.59%     | ok               |
|          15 | -0.70%   | 30.69%             | -15.77% |     0.06 |       76 | 51.41%     | ok               |
|          50 | -0.60%   | 30.69%             | -11.79% |     0.03 |       52 | 29.78%     | ok               |
|          40 | -3.75%   | 30.69%             | -16.99% |    -0.07 |       70 | 37.27%     | ok               |

## XOM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | 5.34%    | 33.27%             | -19.90% |     0.22 |       56 | 36.77%     | ok               |
|          30 | 4.30%    | 33.27%             | -20.29% |     0.19 |       56 | 36.11%     | ok               |
|          50 | 1.92%    | 33.27%             | -21.35% |     0.13 |       46 | 29.95%     | ok               |
|          20 | 1.45%    | 33.27%             | -25.56% |     0.12 |       61 | 39.27%     | ok               |
|          35 | -0.14%   | 33.27%             | -20.93% |     0.07 |       58 | 34.94%     | ok               |

## XRP-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | -22.30%  | -62.55%            | -48.69% |    -0.09 |       70 | 41.76%     | ok               |
|          40 | -29.52%  | -62.55%            | -46.96% |    -0.24 |       62 | 35.63%     | ok               |
|          30 | -36.87%  | -62.55%            | -57.60% |    -0.32 |       74 | 46.17%     | ok               |
|          45 | -37.45%  | -62.55%            | -48.88% |    -0.4  |       62 | 31.23%     | ok               |
|          50 | -34.75%  | -62.55%            | -39.27% |    -0.45 |       64 | 23.56%     | ok               |

## YFI-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -32.83%  | -76.98%            | -52.37% |    -0.46 |       62 | 27.20%     | ok               |
|          45 | -38.27%  | -76.98%            | -54.04% |    -0.66 |       64 | 22.61%     | ok               |
|          35 | -51.92%  | -76.98%            | -65.91% |    -0.81 |       73 | 34.48%     | ok               |
|          30 | -54.99%  | -76.98%            | -67.78% |    -0.82 |       83 | 40.61%     | ok               |
|          50 | -41.48%  | -76.98%            | -51.80% |    -0.84 |       52 | 17.43%     | ok               |

## ZEC-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 130.32%  | 793.09%            | -24.66% |     0.92 |       48 | 23.56%     | ok               |
|          35 | 100.34%  | 793.09%            | -44.34% |     0.8  |       56 | 31.23%     | ok               |
|          25 | 67.08%   | 793.09%            | -48.59% |     0.66 |       61 | 39.85%     | ok               |
|          50 | 58.32%   | 793.09%            | -37.62% |     0.62 |       50 | 21.07%     | ok               |
|          30 | 50.10%   | 793.09%            | -47.68% |     0.59 |       69 | 36.40%     | ok               |
