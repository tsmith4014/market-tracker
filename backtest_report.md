# Market Tracker Backtest Report

_Generated: 2026-10-14T05:00:35+00:00_

## Data Sources

- Crypto: Kraken -> Coinbase -> CoinGecko OHLC -> CoinPaprika fallback chain.
- Stocks / ETFs / indices: Stooq -> Yahoo Finance fallback chain.
- Data rows are generated from real market APIs. Mock OHLCV rows are not generated.

## Data Freshness

- Rows: **92,738**
- Symbols: **161**
- Date range: **2024-05-21** to **2026-10-14**

## Latest Signals

| symbol     | date                |         close |   composite_score | signal   | data_source   |
|:-----------|:--------------------|--------------:|------------------:|:---------|:--------------|
| ABBV       | 2026-10-13 00:00:00 |   274.36      |         74.4167   | LONG     | Yahoo Finance |
| ALGO-USD   | 2026-10-14 00:00:00 |     0.12076   |         37.8333   | LONG     | Kraken API    |
| AMD        | 2026-10-13 00:00:00 |   605.53      |         40.4167   | LONG     | Yahoo Finance |
| AMGN       | 2026-10-13 00:00:00 |   412.84      |         69.9167   | LONG     | Yahoo Finance |
| CL         | 2026-10-13 00:00:00 |    89.95      |         58.5      | LONG     | Yahoo Finance |
| COP        | 2026-10-13 00:00:00 |   140.9       |         71.25     | LONG     | Yahoo Finance |
| COST       | 2026-10-13 00:00:00 |   954.63      |         61.75     | LONG     | Yahoo Finance |
| CRM        | 2026-10-13 00:00:00 |   238.01      |         51.75     | LONG     | Yahoo Finance |
| CSCO       | 2026-10-13 00:00:00 |   115.07      |         72.0833   | LONG     | Yahoo Finance |
| DIA        | 2026-10-13 00:00:00 |   516.21      |         50.9167   | LONG     | Yahoo Finance |
| DXY-INDEX  | 2026-10-14 00:00:00 |   102.094     |         76.3441   | LONG     | Yahoo Finance |
| EOG        | 2026-10-13 00:00:00 |   153.17      |         71.25     | LONG     | Yahoo Finance |
| IBIT       | 2026-10-13 00:00:00 |    47.13      |         42.0833   | LONG     | Yahoo Finance |
| LIN        | 2026-10-13 00:00:00 |   492.11      |         68        | LONG     | Yahoo Finance |
| LLY        | 2026-10-13 00:00:00 |  1166.51      |         50.25     | LONG     | Yahoo Finance |
| META       | 2026-10-13 00:00:00 |   762.5       |         56.25     | LONG     | Yahoo Finance |
| MSFT       | 2026-10-13 00:00:00 |   543.45      |         70.75     | LONG     | Yahoo Finance |
| NEAR-USD   | 2026-10-14 00:00:00 |     5.1117    |         39.6667   | LONG     | Kraken API    |
| NVDA       | 2026-10-13 00:00:00 |   228.52      |         48.5833   | LONG     | Yahoo Finance |
| OXY        | 2026-10-13 00:00:00 |    61.65      |         74.5833   | LONG     | Yahoo Finance |
| QQQ        | 2026-10-13 00:00:00 |   743.57      |         46.0833   | LONG     | Yahoo Finance |
| RENDER-USD | 2026-10-14 00:00:00 |     2.051     |         50        | LONG     | Kraken API    |
| TIA-USD    | 2026-10-14 00:00:00 |     0.5781    |         68.8333   | LONG     | Kraken API    |
| TMO        | 2026-10-13 00:00:00 |   663.04      |         38.4167   | LONG     | Yahoo Finance |
| TXN        | 2026-10-13 00:00:00 |   287.85      |         72.4167   | LONG     | Yahoo Finance |
| UNH        | 2026-10-13 00:00:00 |   377.76      |         56.6667   | LONG     | Yahoo Finance |
| XLE        | 2026-10-13 00:00:00 |    67.2       |         73.25     | LONG     | Yahoo Finance |
| XLF        | 2026-10-13 00:00:00 |    54.82      |         48.9167   | LONG     | Yahoo Finance |
| XLK        | 2026-10-13 00:00:00 |   196.28      |         46.5833   | LONG     | Yahoo Finance |
| XLP        | 2026-10-13 00:00:00 |    84.19      |         55.1667   | LONG     | Yahoo Finance |
| AAPL       | 2026-10-13 00:00:00 |   341.27      |         48.5      | NEUTRAL  | Yahoo Finance |
| AAVE-USD   | 2026-10-14 00:00:00 |   162.59      |         23        | NEUTRAL  | Kraken API    |
| ADA-USD    | 2026-10-14 00:00:00 |     0.237218  |        -23.5833   | NEUTRAL  | Kraken API    |
| ADBE       | 2026-10-13 00:00:00 |   236.28      |        -11.5      | NEUTRAL  | Yahoo Finance |
| AGG        | 2026-10-13 00:00:00 |    94.71      |        -27.25     | NEUTRAL  | Yahoo Finance |
| AMAT       | 2026-10-13 00:00:00 |   464.24      |        -11.0833   | NEUTRAL  | Yahoo Finance |
| AMZN       | 2026-10-13 00:00:00 |   258.58      |         60.8333   | NEUTRAL  | Yahoo Finance |
| APT-USD    | 2026-10-14 00:00:00 |     0.8352    |         21        | NEUTRAL  | Kraken API    |
| ARB-USD    | 2026-10-14 00:00:00 |     0.1921    |         14.3333   | NEUTRAL  | Kraken API    |
| ARKK       | 2026-10-13 00:00:00 |    87.17      |          4.66667  | NEUTRAL  | Yahoo Finance |
| ATOM-USD   | 2026-10-14 00:00:00 |     1.8351    |         41.75     | NEUTRAL  | Kraken API    |
| AVAX-USD   | 2026-10-14 00:00:00 |    10.319     |          3.41667  | NEUTRAL  | Kraken API    |
| AVGO       | 2026-10-13 00:00:00 |   357.31      |        -34        | NEUTRAL  | Yahoo Finance |
| BAC        | 2026-10-13 00:00:00 |    53.96      |        -10        | NEUTRAL  | Yahoo Finance |
| BCH-USD    | 2026-10-14 00:00:00 |   280.25      |        -13.5833   | NEUTRAL  | Kraken API    |
| BITO       | 2026-10-13 00:00:00 |    11.13      |         11.5833   | NEUTRAL  | Yahoo Finance |
| BLK        | 2026-10-13 00:00:00 |  1066.12      |        -14.25     | NEUTRAL  | Yahoo Finance |
| BND        | 2026-10-13 00:00:00 |    70.33      |        -26.75     | NEUTRAL  | Yahoo Finance |
| BONK-USD   | 2026-10-14 00:00:00 |     3.251e-06 |        -28.5833   | NEUTRAL  | Kraken API    |
| BTC-USD    | 2026-10-14 00:00:00 | 83751.7       |         22.75     | NEUTRAL  | Kraken API    |
| CAT        | 2026-10-13 00:00:00 |   772.78      |        -65        | NEUTRAL  | Yahoo Finance |
| COMP-USD   | 2026-10-14 00:00:00 |    23.37      |         14.6667   | NEUTRAL  | Kraken API    |
| CRV-USD    | 2026-10-14 00:00:00 |     0.34158   |        -11.5833   | NEUTRAL  | Kraken API    |
| CVX        | 2026-10-13 00:00:00 |   217.73      |         44        | NEUTRAL  | Yahoo Finance |
| DASH-USD   | 2026-10-14 00:00:00 |    50.807     |        -18.9167   | NEUTRAL  | Kraken API    |
| DBC        | 2026-10-13 00:00:00 |    33.48      |         62.25     | NEUTRAL  | Yahoo Finance |
| DE         | 2026-10-13 00:00:00 |   650         |        -26        | NEUTRAL  | Yahoo Finance |
| DIS        | 2026-10-13 00:00:00 |   108.58      |         64.8333   | NEUTRAL  | Yahoo Finance |
| DOT-USD    | 2026-10-14 00:00:00 |     1.1681    |        -23.5833   | NEUTRAL  | Kraken API    |
| EEM        | 2026-10-13 00:00:00 |    65.74      |        -45        | NEUTRAL  | Yahoo Finance |
| EFA        | 2026-10-13 00:00:00 |   103.47      |        -23.75     | NEUTRAL  | Yahoo Finance |
| ETH-USD    | 2026-10-14 00:00:00 |  2514.03      |         -0.166667 | NEUTRAL  | Kraken API    |
| EWJ        | 2026-10-13 00:00:00 |    97.32      |         14.25     | NEUTRAL  | Yahoo Finance |
| FCX        | 2026-10-13 00:00:00 |    72.42      |         34        | NEUTRAL  | Yahoo Finance |
| FET-USD    | 2026-10-14 00:00:00 |     0.2197    |         19.8333   | NEUTRAL  | Kraken API    |
| FIL-USD    | 2026-10-14 00:00:00 |     1.194     |         36.75     | NEUTRAL  | Kraken API    |
| FXI        | 2026-10-13 00:00:00 |    34.17      |        -11.5      | NEUTRAL  | Yahoo Finance |
| GE         | 2026-10-13 00:00:00 |   307.63      |        -51.1667   | NEUTRAL  | Yahoo Finance |
| GOOGL      | 2026-10-13 00:00:00 |   353.78      |         54.25     | NEUTRAL  | Yahoo Finance |
| GRT-USD    | 2026-10-14 00:00:00 |     0.02635   |         18.0833   | NEUTRAL  | Kraken API    |
| HD         | 2026-10-13 00:00:00 |   293.92      |        -27.25     | NEUTRAL  | Yahoo Finance |
| IBM        | 2026-10-13 00:00:00 |   230.78      |         -7.33333  | NEUTRAL  | Yahoo Finance |
| ICP-USD    | 2026-10-14 00:00:00 |     3.134     |         -0.583333 | NEUTRAL  | Kraken API    |
| IEF        | 2026-10-13 00:00:00 |    89.54      |        -26.75     | NEUTRAL  | Yahoo Finance |
| IEMG       | 2026-10-13 00:00:00 |    80.22      |        -45        | NEUTRAL  | Yahoo Finance |
| INJ-USD    | 2026-10-14 00:00:00 |     8.329     |         36.75     | NEUTRAL  | Kraken API    |
| INTC       | 2026-10-13 00:00:00 |   102.81      |         -2.66667  | NEUTRAL  | Yahoo Finance |
| INTU       | 2026-10-13 00:00:00 |   301.45      |         19.9167   | NEUTRAL  | Yahoo Finance |
| IWM        | 2026-10-13 00:00:00 |   276.7       |        -27.6667   | NEUTRAL  | Yahoo Finance |
| JNJ        | 2026-10-13 00:00:00 |   248.61      |        -45        | NEUTRAL  | Yahoo Finance |
| JPM        | 2026-10-13 00:00:00 |   331.43      |          6.25     | NEUTRAL  | Yahoo Finance |
| KO         | 2026-10-13 00:00:00 |    90.11      |         64.8333   | NEUTRAL  | Yahoo Finance |
| LDO-USD    | 2026-10-14 00:00:00 |     0.431     |         12.3333   | NEUTRAL  | Kraken API    |
| LINK-USD   | 2026-10-14 00:00:00 |    13.0348    |          9.33333  | NEUTRAL  | Kraken API    |
| LRCX       | 2026-10-13 00:00:00 |   301.11      |         -9.33333  | NEUTRAL  | Yahoo Finance |
| LTC-USD    | 2026-10-14 00:00:00 |    62.2       |         18.3333   | NEUTRAL  | Kraken API    |
| MCD        | 2026-10-13 00:00:00 |   235.81      |        -29.25     | NEUTRAL  | Yahoo Finance |
| MPC        | 2026-10-13 00:00:00 |   476.98      |         62.5      | NEUTRAL  | Yahoo Finance |
| MRK        | 2026-10-13 00:00:00 |   141.98      |        -29        | NEUTRAL  | Yahoo Finance |
| MU         | 2026-10-13 00:00:00 |   953.19      |         -2.08333  | NEUTRAL  | Yahoo Finance |
| NFLX       | 2026-10-13 00:00:00 |    70.46      |        -15.25     | NEUTRAL  | Yahoo Finance |
| NKE        | 2026-10-13 00:00:00 |    35.33      |        -27.75     | NEUTRAL  | Yahoo Finance |
| NOW        | 2026-10-13 00:00:00 |   138.61      |         49.1667   | NEUTRAL  | Yahoo Finance |
| OP-USD     | 2026-10-14 00:00:00 |     0.1562    |         51.5      | NEUTRAL  | Kraken API    |
| ORCL       | 2026-10-13 00:00:00 |   143.2       |         -5.83333  | NEUTRAL  | Yahoo Finance |
| PEP        | 2026-10-13 00:00:00 |   127.3       |        -29.25     | NEUTRAL  | Yahoo Finance |
| PEPE-USD   | 2026-10-14 00:00:00 |     4.218e-06 |         21.5833   | NEUTRAL  | Kraken API    |
| PFE        | 2026-10-13 00:00:00 |    28.37      |         38.8333   | NEUTRAL  | Yahoo Finance |
| PG         | 2026-10-13 00:00:00 |   153.04      |         71.4167   | NEUTRAL  | Yahoo Finance |
| PM         | 2026-10-13 00:00:00 |   199.29      |         63.1667   | NEUTRAL  | Yahoo Finance |
| POL-USD    | 2026-10-14 00:00:00 |     0.10159   |        -26.8333   | NEUTRAL  | Kraken API    |
| QCOM       | 2026-10-13 00:00:00 |   176.86      |        -16.5833   | NEUTRAL  | Yahoo Finance |
| SHY        | 2026-10-13 00:00:00 |    81.19      |         -9.08333  | NEUTRAL  | Yahoo Finance |
| SKY-USD    | 2026-10-14 00:00:00 |     0.07782   |          8.58333  | NEUTRAL  | Kraken API    |
| SMH        | 2026-10-13 00:00:00 |   588.12      |         16.4167   | NEUTRAL  | Yahoo Finance |
| SNX-USD    | 2026-10-14 00:00:00 |     0.2405    |        -12.3333   | NEUTRAL  | Kraken API    |
| SOL-USD    | 2026-10-14 00:00:00 |   108.08      |          2.66667  | NEUTRAL  | Kraken API    |
| SOXX       | 2026-10-13 00:00:00 |   543.9       |         -1.58333  | NEUTRAL  | Yahoo Finance |
| SPY        | 2026-10-13 00:00:00 |   778.01      |         63.1667   | NEUTRAL  | Yahoo Finance |
| SUSHI-USD  | 2026-10-14 00:00:00 |     0.2402    |          2.75     | NEUTRAL  | Kraken API    |
| TGT        | 2026-10-13 00:00:00 |   151.99      |        -23.5      | NEUTRAL  | Yahoo Finance |
| TRX-USD    | 2026-10-14 00:00:00 |     0.330859  |        -40.0833   | NEUTRAL  | Kraken API    |
| TSLA       | 2026-10-13 00:00:00 |   375.23      |         -3.83333  | NEUTRAL  | Yahoo Finance |
| UNI-USD    | 2026-10-14 00:00:00 |     7.4982    |          2.41667  | NEUTRAL  | Kraken API    |
| USO        | 2026-10-13 00:00:00 |   153.09      |         46.6667   | NEUTRAL  | Yahoo Finance |
| VEA        | 2026-10-13 00:00:00 |    70.06      |        -27.5833   | NEUTRAL  | Yahoo Finance |
| VIXY       | 2026-10-13 00:00:00 |    16.02      |        -40.5      | NEUTRAL  | Yahoo Finance |
| VNQ        | 2026-10-13 00:00:00 |    91.14      |        -25.75     | NEUTRAL  | Yahoo Finance |
| VTI        | 2026-10-13 00:00:00 |   381.32      |         63.1667   | NEUTRAL  | Yahoo Finance |
| VWO        | 2026-10-13 00:00:00 |    59.68      |        -37.5      | NEUTRAL  | Yahoo Finance |
| WFC        | 2026-10-13 00:00:00 |    80.74      |        -26.5      | NEUTRAL  | Yahoo Finance |
| WMT        | 2026-10-13 00:00:00 |   112.28      |         19.8333   | NEUTRAL  | Yahoo Finance |
| XBI        | 2026-10-13 00:00:00 |   146.8       |        -21.9167   | NEUTRAL  | Yahoo Finance |
| XLB        | 2026-10-13 00:00:00 |    49.72      |        -20        | NEUTRAL  | Yahoo Finance |
| XLC        | 2026-10-13 00:00:00 |   112.28      |          4.91667  | NEUTRAL  | Yahoo Finance |
| XLI        | 2026-10-13 00:00:00 |   168.67      |        -38.4167   | NEUTRAL  | Yahoo Finance |
| XLU        | 2026-10-13 00:00:00 |    41.87      |          3.58333  | NEUTRAL  | Yahoo Finance |
| XLV        | 2026-10-13 00:00:00 |   169.66      |         62.6667   | NEUTRAL  | Yahoo Finance |
| XLY        | 2026-10-13 00:00:00 |   112.36      |         10.1667   | NEUTRAL  | Yahoo Finance |
| XOM        | 2026-10-13 00:00:00 |   174.08      |         44        | NEUTRAL  | Yahoo Finance |
| XRP-USD    | 2026-10-14 00:00:00 |     1.37609   |        -38.5833   | NEUTRAL  | Kraken API    |
| YFI-USD    | 2026-10-14 00:00:00 |  2313.4       |        -26.5833   | NEUTRAL  | Kraken API    |
| ZEC-USD    | 2026-10-14 00:00:00 |  1265.82      |         -5.33333  | NEUTRAL  | Kraken API    |
| BA         | 2026-10-13 00:00:00 |   186.49      |        -38.75     | SHORT    | Yahoo Finance |
| C          | 2026-10-13 00:00:00 |   124.53      |        -54.5833   | SHORT    | Yahoo Finance |
| CMCSA      | 2026-10-13 00:00:00 |    20.88      |        -49.0833   | SHORT    | Yahoo Finance |
| DOGE-USD   | 2026-10-14 00:00:00 |     0.0851288 |        -38.5833   | SHORT    | Kraken API    |
| ETC-USD    | 2026-10-14 00:00:00 |     8.151     |        -38.5833   | SHORT    | Kraken API    |
| GDX        | 2026-10-13 00:00:00 |    87.24      |        -30.3333   | SHORT    | Yahoo Finance |
| GDXJ       | 2026-10-13 00:00:00 |   110.63      |        -52.8333   | SHORT    | Yahoo Finance |
| GLD        | 2026-10-13 00:00:00 |   381.67      |        -39.0833   | SHORT    | Yahoo Finance |
| GS         | 2026-10-13 00:00:00 |   891.91      |        -40        | SHORT    | Yahoo Finance |
| HBAR-USD   | 2026-10-14 00:00:00 |     0.08718   |        -35.6667   | SHORT    | Kraken API    |
| HON        | 2026-10-13 00:00:00 |   207.29      |        -37.9167   | SHORT    | Yahoo Finance |
| HYG        | 2026-10-13 00:00:00 |    77.09      |        -42.5833   | SHORT    | Yahoo Finance |
| ITA        | 2026-10-13 00:00:00 |   204         |        -40.0833   | SHORT    | Yahoo Finance |
| MS         | 2026-10-13 00:00:00 |   186.64      |        -38.3333   | SHORT    | Yahoo Finance |
| NEM        | 2026-10-13 00:00:00 |   115.59      |        -30.3333   | SHORT    | Yahoo Finance |
| RTX        | 2026-10-13 00:00:00 |   183.02      |        -33.4167   | SHORT    | Yahoo Finance |
| SBUX       | 2026-10-13 00:00:00 |    92         |        -31.25     | SHORT    | Yahoo Finance |
| SCHW       | 2026-10-13 00:00:00 |    95.94      |        -32.3333   | SHORT    | Yahoo Finance |
| SHIB-USD   | 2026-10-14 00:00:00 |     5.212e-06 |        -40.25     | SHORT    | Kraken API    |
| SLB        | 2026-10-13 00:00:00 |    48.77      |        -48.25     | SHORT    | Yahoo Finance |
| SLV        | 2026-10-13 00:00:00 |    53.49      |        -56.5833   | SHORT    | Yahoo Finance |
| T          | 2026-10-13 00:00:00 |    22.85      |        -53.1667   | SHORT    | Yahoo Finance |
| TLT        | 2026-10-13 00:00:00 |    78.37      |        -39.9167   | SHORT    | Yahoo Finance |
| TMUS       | 2026-10-13 00:00:00 |   153.73      |        -46.25     | SHORT    | Yahoo Finance |
| UPS        | 2026-10-13 00:00:00 |    94.79      |        -31.25     | SHORT    | Yahoo Finance |
| VZ         | 2026-10-13 00:00:00 |    43.53      |        -48.5833   | SHORT    | Yahoo Finance |
| WIF-USD    | 2026-10-14 00:00:00 |     0.2094    |        -51.5833   | SHORT    | Kraken API    |
| XLM-USD    | 2026-10-14 00:00:00 |     0.190573  |        -42.3333   | SHORT    | Kraken API    |

## Edge Summary

- Symbols with trades: **161** of 161
- Beat buy-and-hold: **33.54%** of traded symbols
- Positive return: **30.43%** of traded symbols
- Median strategy return: **-10.03%** (benchmark **14.92%**)
- Median excess vs benchmark: **-25.91%**
- Median Sharpe: **-0.15**
- Median exposure: **44.26%**

> Edge is real only if both _beat buy-and-hold_ and _median excess_ are convincingly positive across many symbols. Treat a single high-return symbol as noise.

## Portfolio Backtest

Actual capital-allocation books (not per-symbol averages). Benchmarks: `equal_weight_buyhold` (whole tracked universe), `spy_buyhold` (100% SPY), and `sixty_forty` (60% SPY / 40% AGG). `high_conf_voltarget` inverse-vol-weights the HIGH-confidence book; `conviction_long_short` is market-neutral. Judge on **Sharpe** and **max_drawdown** out-of-sample, not raw return: a fully-invested long book wins on return in a bull market but carries all the risk.

| strategy              | scope         | ann_return   | ann_vol   |   sharpe | max_drawdown   | total_return   |   avg_gross_exposure |
|:----------------------|:--------------|:-------------|:----------|---------:|:---------------|:---------------|---------------------:|
| equal_weight_buyhold  | full          | 10.25%       | 28.48%    |     0.36 | -39.53%        | 20.75%         |                 1    |
| equal_weight_buyhold  | out_of_sample | 12.05%       | 28.19%    |     0.43 | -19.75%        | 9.02%          |                 1    |
| all_signals_ew        | full          | -16.49%      | 24.33%    |    -0.68 | -57.77%        | -44.67%        |                 1    |
| all_signals_ew        | out_of_sample | 9.66%        | 24.01%    |     0.4  | -23.20%        | 7.52%          |                 1    |
| high_conf_ew          | full          | -3.48%       | 31.53%    |    -0.11 | -43.43%        | -22.51%        |                 0.9  |
| high_conf_ew          | out_of_sample | 17.18%       | 28.96%    |     0.59 | -22.85%        | 14.79%         |                 0.9  |
| high_conf_voltarget   | full          | -4.92%       | 28.31%    |    -0.17 | -38.37%        | -23.62%        |                 0.9  |
| high_conf_voltarget   | out_of_sample | 4.79%        | 24.10%    |     0.2  | -17.13%        | 1.95%          |                 0.9  |
| conviction_long_short | full          | -13.58%      | 22.23%    |    -0.61 | -45.12%        | -38.68%        |                 0.97 |
| conviction_long_short | out_of_sample | -0.32%       | 19.62%    |    -0.02 | -26.77%        | -2.37%         |                 0.97 |
| spy_buyhold           | full          | 4.54%        | 13.50%    |     0.34 | -19.00%        | 11.69%         |                 0.79 |
| spy_buyhold           | out_of_sample | 2.45%        | 9.92%     |     0.25 | -12.06%        | 2.12%          |                 0.79 |
| sixty_forty           | full          | 2.29%        | 8.53%     |     0.27 | -11.66%        | 6.04%          |                 0.79 |
| sixty_forty           | out_of_sample | -0.70%       | 6.68%     |    -0.11 | -8.26%         | -0.98%         |                 0.79 |

## Walk-Forward Robustness

Each book measured across contiguous time folds (each a different regime). A book has durable edge only if `mean_sharpe` is positive, `min_sharpe` isn't deeply negative, and `pct_positive_folds` is high — a single great fold doesn't count. `fold_sharpes` lists each fold oldest-to-newest.

| strategy              |   n_folds |   mean_sharpe |   median_sharpe |   min_sharpe | pct_positive_folds   | mean_return   | fold_sharpes                 |
|:----------------------|----------:|--------------:|----------------:|-------------:|:---------------------|:--------------|:-----------------------------|
| equal_weight_buyhold  |         5 |          0.48 |            0.64 |        -0.32 | 60.00%               | 4.46%         | 0.64;1.16;-0.13;-0.32;1.04   |
| all_signals_ew        |         5 |         -0.73 |           -1.27 |        -1.95 | 20.00%               | -9.13%        | -1.34;-1.27;-1.95;1.57;-0.66 |
| high_conf_ew          |         5 |         -0.01 |           -0.03 |        -0.82 | 40.00%               | -3.69%        | 0.02;-0.55;-0.82;1.34;-0.03  |
| high_conf_voltarget   |         5 |         -0.07 |           -0.25 |        -0.75 | 40.00%               | -4.58%        | 0.22;-0.37;-0.75;0.82;-0.25  |
| conviction_long_short |         5 |         -0.59 |           -0.61 |        -1.74 | 20.00%               | -9.02%        | -1.74;-0.17;-0.70;-0.61;0.26 |
| spy_buyhold           |         5 |          0.33 |            0.07 |        -0.38 | 60.00%               | 2.34%         | 1.32;0.07;-0.08;0.74;-0.38   |
| sixty_forty           |         5 |          0.24 |            0.13 |        -0.72 | 80.00%               | 1.22%         | 1.25;0.13;0.13;0.42;-0.72    |

## Strategy Comparison

Each decision rule backtested over the same data. `out_of_sample` is the most recent ~35% of each symbol's history (unseen tail). A rule has real edge only if `median_excess` and `beat_benchmark_pct` stay positive out-of-sample, not just full-sample.

| strategy        | scope         |   symbols | beat_benchmark_pct   | positive_pct   | median_return   | median_benchmark   | median_excess   |   median_sharpe |   total_trades |
|:----------------|:--------------|----------:|:---------------------|:---------------|:----------------|:-------------------|:----------------|----------------:|---------------:|
| trend           | full          |       161 | 33.54%               | 30.43%         | -10.03%         | 14.92%             | -25.91%         |           -0.15 |          11318 |
| trend           | out_of_sample |       161 | 29.19%               | 47.83%         | -0.27%          | 8.72%              | -14.72%         |            0.03 |           3828 |
| mean_reversion  | full          |       157 | 40.76%               | 50.32%         | 0.01%           | 14.90%             | -14.41%         |            0.02 |           1228 |
| mean_reversion  | out_of_sample |       121 | 30.58%               | 52.89%         | 0.29%           | 6.94%              | -7.91%          |            0.16 |            492 |
| regime_adaptive | full          |       161 | 34.16%               | 29.81%         | -10.70%         | 14.92%             | -25.91%         |           -0.13 |          11589 |
| regime_adaptive | out_of_sample |       161 | 29.81%               | 47.20%         | -1.03%          | 8.72%              | -15.25%         |           -0    |           3941 |

## Signal Calibration

Realized forward return in the signal's direction, grouped by confidence. HIGH should outrank LOW for the confidence score to be meaningful.

| confidence_level   |   horizon |     n | mean_return   | median_return   | win_rate   |
|:-------------------|----------:|------:|:--------------|:----------------|:-----------|
| HIGH               |         5 |  7935 | 0.20%         | 0.04%           | 50.76%     |
| MEDIUM             |         5 | 29164 | 0.04%         | 0.03%           | 50.25%     |
| LOW                |         5 |  3504 | -0.42%        | -0.43%          | 45.80%     |
| ALL                |         5 | 40603 | 0.03%         | 0.00%           | 49.97%     |
| HIGH               |        10 |  7905 | 0.47%         | 0.09%           | 51.04%     |
| MEDIUM             |        10 | 28889 | 0.18%         | 0.06%           | 50.47%     |
| LOW                |        10 |  3443 | -0.73%        | -0.53%          | 46.62%     |
| ALL                |        10 | 40237 | 0.16%         | 0.03%           | 50.25%     |
| HIGH               |        20 |  7761 | 1.10%         | 0.32%           | 52.63%     |
| MEDIUM             |        20 | 28295 | 0.90%         | 0.56%           | 53.19%     |
| LOW                |        20 |  3382 | -0.49%        | -0.60%          | 47.10%     |
| ALL                |        20 | 39438 | 0.82%         | 0.44%           | 52.56%     |

## Backtest Summary

### Data Quality / Signal Availability

- **ok**: 161 symbols

| symbol     |   trades | return   | benchmark_return   | mdd     |   sharpe | exposure   | skipped_reason   |
|:-----------|---------:|:---------|:-------------------|:--------|---------:|:-----------|:-----------------|
| AAPL       |       63 | 6.16%    | 77.42%             | -20.65% |     0.23 | 50.92%     | ok               |
| AAVE-USD   |       65 | -34.18%  | -26.51%            | -66.17% |    -0.17 | 42.34%     | ok               |
| ABBV       |       70 | -24.49%  | 68.39%             | -30.52% |    -0.54 | 47.92%     | ok               |
| ADA-USD    |       76 | -35.12%  | -70.52%            | -52.70% |    -0.26 | 46.17%     | ok               |
| ADBE       |       71 | -8.14%   | -50.96%            | -31.20% |     0.03 | 56.74%     | ok               |
| AGG        |       67 | -7.20%   | -2.22%             | -11.29% |    -1.14 | 33.78%     | ok               |
| ALGO-USD   |       76 | -19.37%  | -49.53%            | -38.19% |    -0.03 | 40.23%     | ok               |
| AMAT       |       73 | -43.08%  | 111.21%            | -57.56% |    -0.46 | 51.91%     | ok               |
| AMD        |       52 | 26.72%   | 267.75%            | -40.05% |     0.45 | 36.94%     | ok               |
| AMGN       |       67 | -18.92%  | 31.12%             | -34.19% |    -0.37 | 50.92%     | ok               |
| AMZN       |       80 | -55.73%  | 41.18%             | -56.19% |    -1.6  | 41.26%     | ok               |
| APT-USD    |       70 | -23.20%  | -85.77%            | -56.73% |    -0    | 39.66%     | ok               |
| ARB-USD    |       77 | -9.37%   | -57.38%            | -48.19% |     0.19 | 43.30%     | ok               |
| ARKK       |       85 | -27.19%  | 92.85%             | -31.44% |    -0.39 | 43.43%     | ok               |
| ATOM-USD   |       92 | -60.07%  | -65.41%            | -60.07% |    -0.87 | 47.89%     | ok               |
| AVAX-USD   |       68 | -31.87%  | -58.36%            | -45.41% |    -0.24 | 40.04%     | ok               |
| AVGO       |       64 | 17.01%   | 155.37%            | -36.09% |     0.36 | 41.76%     | ok               |
| BA         |       69 | 5.55%    | 0.93%              | -26.13% |     0.22 | 51.08%     | ok               |
| BAC        |       72 | -11.08%  | 36.09%             | -25.80% |    -0.25 | 48.59%     | ok               |
| BCH-USD    |       76 | 0.92%    | -31.32%            | -53.87% |     0.22 | 48.85%     | ok               |
| BITO       |       79 | -24.31%  | -60.41%            | -43.10% |    -0.17 | 41.93%     | ok               |
| BLK        |       85 | -15.14%  | 32.45%             | -26.90% |    -0.37 | 47.25%     | ok               |
| BND        |       65 | -6.82%   | -2.17%             | -10.79% |    -1.04 | 35.61%     | ok               |
| BONK-USD   |       74 | 20.57%   | -85.34%            | -45.22% |     0.44 | 45.79%     | ok               |
| BTC-USD    |       72 | 3.27%    | -19.56%            | -23.38% |     0.19 | 52.11%     | ok               |
| C          |       77 | -35.84%  | 92.35%             | -39.51% |    -0.79 | 46.09%     | ok               |
| CAT        |       70 | 3.76%    | 115.22%            | -21.87% |     0.19 | 48.25%     | ok               |
| CL         |       66 | -6.20%   | -5.48%             | -14.32% |    -0.15 | 38.60%     | ok               |
| CMCSA      |       84 | -34.73%  | -43.18%            | -46.39% |    -0.82 | 43.26%     | ok               |
| COMP-USD   |       97 | -37.68%  | -51.20%            | -55.77% |    -0.21 | 49.81%     | ok               |
| COP        |       70 | -15.24%  | 17.02%             | -43.40% |    -0.19 | 44.09%     | ok               |
| COST       |       60 | -2.81%   | 19.19%             | -31.32% |    -0.03 | 41.10%     | ok               |
| CRM        |       67 | -33.40%  | -16.12%            | -45.50% |    -0.48 | 46.09%     | ok               |
| CRV-USD    |       66 | 26.38%   | -56.25%            | -39.89% |     0.47 | 37.16%     | ok               |
| CSCO       |       64 | 16.96%   | 145.14%            | -21.79% |     0.4  | 49.25%     | ok               |
| CVX        |       71 | -13.64%  | 36.11%             | -27.78% |    -0.3  | 41.76%     | ok               |
| DASH-USD   |       55 | 0.17%    | 106.66%            | -64.43% |     0.39 | 30.46%     | ok               |
| DBC        |       66 | -8.16%   | 40.55%             | -24.10% |    -0.21 | 35.27%     | ok               |
| DE         |       70 | -12.17%  | 68.07%             | -23.98% |    -0.18 | 44.26%     | ok               |
| DIA        |       66 | -7.81%   | 29.45%             | -12.94% |    -0.4  | 43.59%     | ok               |
| DIS        |       60 | -6.18%   | 5.41%              | -28.17% |    -0.05 | 43.09%     | ok               |
| DOGE-USD   |       71 | -30.71%  | -63.28%            | -60.95% |    -0.15 | 48.66%     | ok               |
| DOT-USD    |       86 | -51.64%  | -77.06%            | -63.33% |    -0.43 | 48.47%     | ok               |
| DXY-INDEX  |       40 | -0.69%   | -4.55%             | -6.02%  |    -0.09 | 32.25%     | ok               |
| EEM        |       62 | -12.31%  | 51.61%             | -24.40% |    -0.35 | 40.10%     | ok               |
| EFA        |       68 | -11.10%  | 26.85%             | -12.45% |    -0.43 | 41.93%     | ok               |
| EOG        |       78 | -30.38%  | 18.83%             | -47.87% |    -0.66 | 44.76%     | ok               |
| ETC-USD    |       60 | -26.56%  | -59.21%            | -48.09% |    -0.28 | 31.23%     | ok               |
| ETH-USD    |       58 | 144.86%  | -0.06%             | -30.11% |     1.31 | 48.28%     | ok               |
| EWJ        |       62 | -22.99%  | 41.41%             | -29.40% |    -0.8  | 36.44%     | ok               |
| FCX        |       65 | -29.37%  | 33.32%             | -46.84% |    -0.32 | 44.26%     | ok               |
| FET-USD    |       79 | -46.79%  | -74.11%            | -65.38% |    -0.29 | 42.34%     | ok               |
| FIL-USD    |       65 | -40.15%  | -61.95%            | -58.54% |    -0.34 | 37.16%     | ok               |
| FXI        |       50 | -8.38%   | 19.64%             | -24.33% |    -0.13 | 31.28%     | ok               |
| GDX        |       62 | -2.45%   | 136.23%            | -33.31% |     0.1  | 44.59%     | ok               |
| GDXJ       |       72 | -38.23%  | 136.19%            | -40.39% |    -0.51 | 43.09%     | ok               |
| GE         |       76 | -8.43%   | 91.07%             | -27.82% |    -0.04 | 48.09%     | ok               |
| GLD        |       50 | 9.26%    | 70.21%             | -13.87% |     0.3  | 45.76%     | ok               |
| GOOGL      |       57 | 56.30%   | 98.92%             | -17.54% |     1    | 47.42%     | ok               |
| GRT-USD    |       77 | 66.81%   | -77.69%            | -33.74% |     0.75 | 45.59%     | ok               |
| GS         |       70 | -5.86%   | 89.60%             | -21.94% |    -0.03 | 48.09%     | ok               |
| HBAR-USD   |       40 | -44.37%  | -15.47%            | -56.62% |    -0.99 | 37.64%     | ok               |
| HD         |       67 | 1.75%    | -12.56%            | -17.15% |     0.13 | 43.59%     | ok               |
| HON        |       93 | -26.78%  | 3.05%              | -33.53% |    -0.67 | 54.91%     | ok               |
| HYG        |       87 | -7.18%   | -0.22%             | -10.59% |    -0.81 | 38.77%     | ok               |
| IBIT       |       40 | 39.17%   | 23.99%             | -18.95% |     0.71 | 34.96%     | ok               |
| IBM        |       69 | -26.24%  | 33.04%             | -48.94% |    -0.32 | 49.42%     | ok               |
| ICP-USD    |       79 | -17.84%  | -45.65%            | -46.42% |     0.09 | 39.27%     | ok               |
| IEF        |       78 | -10.57%  | -3.94%             | -13.34% |    -1.44 | 34.28%     | ok               |
| IEMG       |       60 | -11.95%  | 47.38%             | -27.73% |    -0.36 | 40.27%     | ok               |
| INJ-USD    |       65 | -21.00%  | -36.65%            | -69.36% |     0.05 | 40.42%     | ok               |
| INTC       |       68 | 40.26%   | 223.91%            | -60.60% |     0.53 | 48.09%     | ok               |
| INTU       |       73 | -11.45%  | -54.86%            | -37.50% |    -0.05 | 46.76%     | ok               |
| ITA        |       76 | -3.85%   | 49.46%             | -23.75% |    -0.03 | 48.59%     | ok               |
| IWM        |       54 | 6.91%    | 32.81%             | -11.44% |     0.31 | 34.28%     | ok               |
| JNJ        |       60 | 7.29%    | 64.38%             | -16.86% |     0.31 | 46.76%     | ok               |
| JPM        |       73 | -22.86%  | 66.11%             | -32.74% |    -0.63 | 45.09%     | ok               |
| KO         |       54 | 23.40%   | 43.24%             | -8.64%  |     0.83 | 36.94%     | ok               |
| LDO-USD    |       70 | 44.87%   | -60.78%            | -50.47% |     0.6  | 46.55%     | ok               |
| LIN        |       74 | -11.01%  | 13.12%             | -20.61% |    -0.35 | 38.44%     | ok               |
| LINK-USD   |       68 | 43.55%   | -23.77%            | -33.64% |     0.61 | 45.59%     | ok               |
| LLY        |       78 | -37.52%  | 45.24%             | -53.34% |    -0.65 | 49.08%     | ok               |
| LRCX       |       80 | -27.50%  | 212.35%            | -58.92% |    -0.19 | 42.76%     | ok               |
| LTC-USD    |       67 | 3.16%    | -37.85%            | -31.73% |     0.24 | 52.87%     | ok               |
| MCD        |       77 | -0.10%   | -11.31%            | -21.88% |     0.05 | 40.77%     | ok               |
| META       |       76 | -23.10%  | 64.11%             | -44.52% |    -0.29 | 50.25%     | ok               |
| MPC        |       70 | 22.17%   | 170.12%            | -34.29% |     0.46 | 51.91%     | ok               |
| MRK        |       65 | -23.45%  | 8.58%              | -35.95% |    -0.45 | 42.43%     | ok               |
| MS         |       75 | -9.65%   | 83.83%             | -27.79% |    -0.15 | 48.25%     | ok               |
| MSFT       |       85 | -24.63%  | 26.67%             | -39.07% |    -0.52 | 51.25%     | ok               |
| MU         |       51 | 140.26%  | 647.60%            | -68.76% |     1    | 52.75%     | ok               |
| NEAR-USD   |       73 | 153.48%  | 63.10%             | -47.03% |     1.05 | 44.25%     | ok               |
| NEM        |       70 | -28.06%  | 162.47%            | -39.56% |    -0.29 | 50.08%     | ok               |
| NFLX       |       78 | 3.31%    | 8.30%              | -21.09% |     0.17 | 53.08%     | ok               |
| NKE        |       79 | -26.45%  | -61.94%            | -55.35% |    -0.28 | 46.92%     | ok               |
| NOW        |       80 | 11.00%   | -10.81%            | -30.43% |     0.3  | 50.25%     | ok               |
| NVDA       |       77 | -48.50%  | 93.78%             | -52.37% |    -0.68 | 55.44%     | ok               |
| OP-USD     |       70 | -35.09%  | -81.86%            | -58.87% |    -0.23 | 33.14%     | ok               |
| ORCL       |       62 | 85.49%   | 14.90%             | -30.61% |     0.8  | 52.25%     | ok               |
| OXY        |       73 | 2.99%    | -2.68%             | -28.48% |     0.17 | 42.60%     | ok               |
| PEP        |       74 | 0.12%    | -29.70%            | -21.35% |     0.07 | 45.92%     | ok               |
| PEPE-USD   |       83 | -53.85%  | -68.99%            | -61.29% |    -0.4  | 48.47%     | ok               |
| PFE        |       81 | -34.23%  | -0.67%             | -41.90% |    -1.05 | 36.77%     | ok               |
| PG         |       64 | -24.15%  | -9.09%             | -24.16% |    -0.98 | 34.61%     | ok               |
| PM         |       79 | -7.74%   | 98.83%             | -35.15% |    -0.09 | 50.25%     | ok               |
| POL-USD    |       79 | 51.05%   | -60.11%            | -38.69% |     0.67 | 49.62%     | ok               |
| QCOM       |       77 | -29.59%  | -11.94%            | -57.69% |    -0.25 | 43.43%     | ok               |
| QQQ        |       66 | 8.23%    | 63.14%             | -14.20% |     0.29 | 46.09%     | ok               |
| RENDER-USD |       92 | -14.13%  | -60.54%            | -44.65% |     0.13 | 47.13%     | ok               |
| RTX        |       64 | 30.49%   | 73.59%             | -16.99% |     0.7  | 52.08%     | ok               |
| SBUX       |       60 | -10.03%  | 18.37%             | -29.22% |    -0.13 | 38.44%     | ok               |
| SCHW       |       80 | -20.32%  | 21.60%             | -31.92% |    -0.46 | 46.09%     | ok               |
| SHIB-USD   |       81 | -33.77%  | -67.18%            | -47.02% |    -0.3  | 52.11%     | ok               |
| SHY        |       48 | -1.72%   | -0.31%             | -3.18%  |    -0.57 | 37.10%     | ok               |
| SKY-USD    |       85 | -60.53%  | 1.58%              | -61.82% |    -0.97 | 44.44%     | ok               |
| SLB        |       73 | -37.59%  | 0.99%              | -57.55% |    -0.7  | 49.08%     | ok               |
| SLV        |       68 | 4.80%    | 82.75%             | -42.60% |     0.24 | 40.10%     | ok               |
| SMH        |       48 | 48.12%   | 150.62%            | -34.29% |     0.78 | 44.09%     | ok               |
| SNX-USD    |       62 | -9.86%   | -72.45%            | -50.74% |     0.1  | 33.52%     | ok               |
| SOL-USD    |       73 | -21.62%  | -37.62%            | -44.99% |    -0.03 | 59.96%     | ok               |
| SOXX       |       54 | 60.20%   | 133.93%            | -39.81% |     0.86 | 43.09%     | ok               |
| SPY        |       64 | -0.42%   | 46.42%             | -15.53% |     0.05 | 49.58%     | ok               |
| SUSHI-USD  |       94 | -75.66%  | -70.50%            | -76.07% |    -1.2  | 39.27%     | ok               |
| T          |       72 | 47.22%   | 32.31%             | -17.01% |     0.91 | 56.74%     | ok               |
| TGT        |       60 | -11.06%  | -2.43%             | -34.42% |    -0.16 | 37.60%     | ok               |
| TIA-USD    |       91 | -53.15%  | -81.99%            | -78.36% |    -0.33 | 43.30%     | ok               |
| TLT        |       68 | -19.50%  | -14.43%            | -21.85% |    -1.46 | 33.78%     | ok               |
| TMO        |       67 | 25.67%   | 12.36%             | -18.85% |     0.55 | 54.91%     | ok               |
| TMUS       |       74 | -1.37%   | -6.47%             | -30.61% |     0.07 | 47.75%     | ok               |
| TRX-USD    |       66 | 4.06%    | 24.89%             | -22.90% |     0.2  | 50.96%     | ok               |
| TSLA       |       80 | -37.10%  | 101.09%            | -59.64% |    -0.26 | 42.93%     | ok               |
| TXN        |       77 | -23.93%  | 44.64%             | -47.39% |    -0.24 | 50.42%     | ok               |
| UNH        |       77 | 21.42%   | -27.85%            | -26.31% |     0.43 | 48.42%     | ok               |
| UNI-USD    |       88 | -34.82%  | 8.31%              | -69.60% |    -0.09 | 50.00%     | ok               |
| UPS        |       70 | -34.78%  | -34.82%            | -39.06% |    -0.68 | 42.43%     | ok               |
| USO        |       67 | -12.16%  | 101.01%            | -46.69% |    -0.05 | 33.44%     | ok               |
| VEA        |       62 | -4.63%   | 37.26%             | -17.27% |    -0.14 | 42.60%     | ok               |
| VIXY       |       94 | -78.82%  | -63.92%            | -88.17% |    -0.96 | 32.45%     | ok               |
| VNQ        |       73 | -15.25%  | 8.04%              | -24.92% |    -0.61 | 39.93%     | ok               |
| VTI        |       68 | -7.83%   | 44.93%             | -17.64% |    -0.23 | 49.58%     | ok               |
| VWO        |       80 | -18.34%  | 34.02%             | -24.94% |    -0.69 | 40.77%     | ok               |
| VZ         |       84 | -23.65%  | 9.87%              | -27.41% |    -0.72 | 41.60%     | ok               |
| WFC        |       80 | -18.93%  | 31.37%             | -28.90% |    -0.32 | 47.42%     | ok               |
| WIF-USD    |       68 | -31.88%  | -76.98%            | -52.76% |    -0.08 | 37.55%     | ok               |
| WMT        |       69 | 4.37%    | 72.34%             | -25.37% |     0.19 | 49.08%     | ok               |
| XBI        |       64 | -1.55%   | 60.31%             | -17.66% |     0.05 | 38.60%     | ok               |
| XLB        |       66 | -14.62%  | 7.76%              | -24.31% |    -0.53 | 31.95%     | ok               |
| XLC        |       61 | 12.62%   | 35.70%             | -12.33% |     0.47 | 50.25%     | ok               |
| XLE        |       69 | -3.61%   | 43.16%             | -30.31% |    -0    | 45.09%     | ok               |
| XLF        |       82 | -9.89%   | 29.97%             | -23.61% |    -0.31 | 46.59%     | ok               |
| XLI        |       82 | -10.04%  | 34.76%             | -17.79% |    -0.35 | 42.76%     | ok               |
| XLK        |       42 | 53.78%   | 82.88%             | -14.75% |     1.05 | 46.42%     | ok               |
| XLM-USD    |       68 | -2.08%   | -37.69%            | -54.66% |     0.2  | 47.70%     | ok               |
| XLP        |       67 | 0.78%    | 7.76%              | -11.16% |     0.08 | 38.10%     | ok               |
| XLU        |       69 | -6.99%   | 14.92%             | -20.40% |    -0.26 | 39.77%     | ok               |
| XLV        |       76 | -22.38%  | 16.01%             | -22.75% |    -1.08 | 36.94%     | ok               |
| XLY        |       75 | -4.15%   | 25.89%             | -18.35% |    -0.06 | 47.59%     | ok               |
| XOM        |       55 | 1.71%    | 47.71%             | -20.29% |     0.12 | 34.28%     | ok               |
| XRP-USD    |       64 | 6.45%    | -41.87%            | -33.91% |     0.27 | 36.40%     | ok               |
| YFI-USD    |       76 | -64.81%  | -63.65%            | -64.57% |    -1.27 | 37.16%     | ok               |
| ZEC-USD    |       59 | 126.83%  | 2701.11%           | -56.50% |     0.86 | 41.38%     | ok               |

## AAPL Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 12.81%   | 77.42%             | -21.71% |     0.34 |       72 | 55.74%     | ok               |
|          15 | 9.90%    | 77.42%             | -23.86% |     0.29 |       81 | 63.06%     | ok               |
|          30 | 6.16%    | 77.42%             | -20.65% |     0.23 |       63 | 50.92%     | ok               |
|          35 | 4.64%    | 77.42%             | -22.04% |     0.2  |       63 | 49.58%     | ok               |
|          25 | 1.87%    | 77.42%             | -20.87% |     0.15 |       73 | 53.08%     | ok               |

## AAVE-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 29.14%   | -26.51%            | -43.61% |     0.49 |       43 | 36.78%     | ok               |
|          45 | 17.11%   | -26.51%            | -49.19% |     0.39 |       48 | 31.61%     | ok               |
|          35 | 12.65%   | -26.51%            | -48.79% |     0.35 |       51 | 39.85%     | ok               |
|          50 | 11.86%   | -26.51%            | -45.07% |     0.33 |       46 | 23.95%     | ok               |
|          15 | -35.90%  | -26.51%            | -61.76% |    -0.11 |       72 | 55.17%     | ok               |

## ABBV Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -12.17%  | 68.39%             | -26.16% |    -0.25 |       54 | 34.94%     | ok               |
|          20 | -23.17%  | 68.39%             | -28.73% |    -0.48 |       68 | 51.41%     | ok               |
|          25 | -23.26%  | 68.39%             | -30.04% |    -0.49 |       71 | 49.92%     | ok               |
|          40 | -22.39%  | 68.39%             | -27.36% |    -0.53 |       70 | 40.27%     | ok               |
|          30 | -24.49%  | 68.39%             | -30.52% |    -0.54 |       70 | 47.92%     | ok               |

## ADA-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 14.73%   | -70.52%            | -34.64% |     0.37 |       46 | 31.80%     | ok               |
|          50 | 8.17%    | -70.52%            | -35.54% |     0.28 |       48 | 27.39%     | ok               |
|          40 | -4.83%   | -70.52%            | -40.73% |     0.15 |       58 | 37.74%     | ok               |
|          15 | -22.20%  | -70.52%            | -47.27% |     0.05 |       71 | 62.07%     | ok               |
|          35 | -16.40%  | -70.52%            | -44.07% |     0.01 |       64 | 41.57%     | ok               |

## ADBE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | 7.33%    | -50.96%            | -29.07% |     0.25 |       56 | 61.23%     | ok               |
|          35 | -1.80%   | -50.96%            | -31.73% |     0.1  |       79 | 48.25%     | ok               |
|          20 | -6.73%   | -50.96%            | -31.52% |     0.06 |       62 | 64.23%     | ok               |
|          30 | -8.14%   | -50.96%            | -31.20% |     0.03 |       71 | 56.74%     | ok               |
|          15 | -17.20%  | -50.96%            | -34.98% |    -0.1  |       62 | 66.06%     | ok               |

## AGG Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -5.98%   | -2.22%             | -9.79%  |    -1.07 |       60 | 25.29%     | ok               |
|          30 | -7.20%   | -2.22%             | -11.29% |    -1.14 |       67 | 33.78%     | ok               |
|          50 | -5.47%   | -2.22%             | -8.35%  |    -1.15 |       58 | 20.13%     | ok               |
|          20 | -8.32%   | -2.22%             | -11.89% |    -1.2  |       72 | 38.60%     | ok               |
|          25 | -8.23%   | -2.22%             | -12.28% |    -1.23 |       71 | 36.77%     | ok               |

## ALGO-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -19.37%  | -49.53%            | -38.19% |    -0.03 |       76 | 40.23%     | ok               |
|          25 | -29.69%  | -49.53%            | -51.92% |    -0.16 |       78 | 45.02%     | ok               |
|          15 | -33.55%  | -49.53%            | -51.37% |    -0.19 |       77 | 50.38%     | ok               |
|          35 | -33.47%  | -49.53%            | -50.16% |    -0.32 |       64 | 35.06%     | ok               |
|          20 | -42.23%  | -49.53%            | -53.23% |    -0.35 |       81 | 47.70%     | ok               |

## AMAT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -27.65%  | 111.21%            | -38.30% |    -0.25 |       50 | 36.27%     | ok               |
|          15 | -36.35%  | 111.21%            | -53.90% |    -0.29 |       72 | 60.73%     | ok               |
|          35 | -38.85%  | 111.21%            | -52.00% |    -0.4  |       73 | 49.25%     | ok               |
|          30 | -43.08%  | 111.21%            | -57.56% |    -0.46 |       73 | 51.91%     | ok               |
|          40 | -43.83%  | 111.21%            | -54.64% |    -0.51 |       71 | 44.43%     | ok               |

## AMD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 27.66%   | 267.75%            | -40.05% |     0.46 |       58 | 32.11%     | ok               |
|          40 | 26.72%   | 267.75%            | -40.05% |     0.45 |       52 | 36.94%     | ok               |
|          35 | 21.27%   | 267.75%            | -42.14% |     0.41 |       60 | 38.60%     | ok               |
|          30 | 9.19%    | 267.75%            | -47.00% |     0.31 |       65 | 41.10%     | ok               |
|          25 | 4.43%    | 267.75%            | -51.79% |     0.27 |       61 | 43.26%     | ok               |

## AMGN Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -14.37%  | 31.12%             | -26.65% |    -0.22 |       66 | 56.57%     | ok               |
|          35 | -16.88%  | 31.12%             | -31.29% |    -0.32 |       69 | 47.59%     | ok               |
|          15 | -19.43%  | 31.12%             | -27.98% |    -0.33 |       63 | 60.73%     | ok               |
|          30 | -18.92%  | 31.12%             | -34.19% |    -0.37 |       67 | 50.92%     | ok               |
|          25 | -20.59%  | 31.12%             | -33.47% |    -0.4  |       63 | 53.08%     | ok               |

## AMZN Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -29.06%  | 41.18%             | -30.67% |    -0.89 |       58 | 30.12%     | ok               |
|          50 | -31.74%  | 41.18%             | -33.91% |    -1.16 |       50 | 22.80%     | ok               |
|          45 | -38.40%  | 41.18%             | -39.18% |    -1.38 |       60 | 26.62%     | ok               |
|          35 | -52.71%  | 41.18%             | -53.20% |    -1.56 |       75 | 35.44%     | ok               |
|          30 | -55.73%  | 41.18%             | -56.19% |    -1.6  |       80 | 41.26%     | ok               |

## APT-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 25.37%   | -85.77%            | -31.21% |     0.52 |       42 | 16.28%     | ok               |
|          20 | 2.63%    | -85.77%            | -56.22% |     0.3  |       78 | 49.62%     | ok               |
|          45 | -1.29%   | -85.77%            | -53.47% |     0.18 |       58 | 23.18%     | ok               |
|          35 | -14.40%  | -85.77%            | -49.10% |     0.07 |       68 | 35.44%     | ok               |
|          25 | -22.50%  | -85.77%            | -55.69% |     0.03 |       70 | 44.25%     | ok               |

## ARB-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 57.32%   | -57.38%            | -33.60% |     0.67 |       54 | 26.44%     | ok               |
|          50 | 46.51%   | -57.38%            | -30.72% |     0.61 |       42 | 19.35%     | ok               |
|          15 | 35.04%   | -57.38%            | -44.26% |     0.54 |       88 | 59.39%     | ok               |
|          40 | 27.44%   | -57.38%            | -40.13% |     0.48 |       55 | 33.72%     | ok               |
|          35 | 21.94%   | -57.38%            | -45.71% |     0.44 |       71 | 37.93%     | ok               |

## ARKK Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -13.51%  | 92.85%             | -37.76% |    -0.06 |       89 | 54.74%     | ok               |
|          20 | -21.49%  | 92.85%             | -34.82% |    -0.22 |       87 | 49.92%     | ok               |
|          30 | -27.19%  | 92.85%             | -31.44% |    -0.39 |       85 | 43.43%     | ok               |
|          35 | -32.93%  | 92.85%             | -36.46% |    -0.55 |       86 | 40.77%     | ok               |
|          40 | -34.01%  | 92.85%             | -40.75% |    -0.61 |       78 | 36.61%     | ok               |

## ATOM-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -41.59%  | -65.41%            | -48.20% |    -0.33 |       86 | 65.90%     | ok               |
|          25 | -50.61%  | -65.41%            | -51.66% |    -0.57 |       94 | 54.21%     | ok               |
|          20 | -55.70%  | -65.41%            | -57.28% |    -0.66 |       96 | 58.24%     | ok               |
|          30 | -60.07%  | -65.41%            | -60.07% |    -0.87 |       92 | 47.89%     | ok               |
|          35 | -61.11%  | -65.41%            | -63.25% |    -1    |       80 | 41.76%     | ok               |

## AVAX-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 53.25%   | -58.36%            | -22.06% |     0.83 |       32 | 19.73%     | ok               |
|          40 | 19.68%   | -58.36%            | -26.61% |     0.43 |       38 | 27.39%     | ok               |
|          45 | 16.86%   | -58.36%            | -23.19% |     0.39 |       30 | 24.14%     | ok               |
|          35 | 1.03%    | -58.36%            | -33.36% |     0.2  |       56 | 33.72%     | ok               |
|          15 | -12.39%  | -58.36%            | -43.71% |     0.1  |       73 | 53.07%     | ok               |

## AVGO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | 20.38%   | 155.37%            | -38.01% |     0.39 |       68 | 44.43%     | ok               |
|          30 | 17.01%   | 155.37%            | -36.09% |     0.36 |       64 | 41.76%     | ok               |
|          50 | 12.02%   | 155.37%            | -36.86% |     0.31 |       56 | 29.62%     | ok               |
|          35 | 8.52%    | 155.37%            | -40.43% |     0.27 |       74 | 38.77%     | ok               |
|          20 | 6.57%    | 155.37%            | -39.42% |     0.25 |       77 | 47.59%     | ok               |

## BA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 41.10%   | 0.93%              | -13.34% |     0.9  |       46 | 35.77%     | ok               |
|          40 | 35.35%   | 0.93%              | -23.87% |     0.68 |       46 | 43.59%     | ok               |
|          35 | 35.60%   | 0.93%              | -18.09% |     0.65 |       62 | 47.75%     | ok               |
|          25 | 15.35%   | 0.93%              | -26.59% |     0.36 |       70 | 54.58%     | ok               |
|          45 | 7.60%    | 0.93%              | -26.76% |     0.25 |       44 | 39.93%     | ok               |

## BAC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | -0.90%   | 36.09%             | -23.08% |     0.05 |       64 | 45.26%     | ok               |
|          20 | -3.06%   | 36.09%             | -18.20% |     0.01 |       80 | 53.41%     | ok               |
|          25 | -5.43%   | 36.09%             | -22.11% |    -0.07 |       74 | 50.92%     | ok               |
|          45 | -6.80%   | 36.09%             | -19.47% |    -0.15 |       60 | 36.94%     | ok               |
|          15 | -10.85%  | 36.09%             | -23.94% |    -0.18 |       87 | 60.57%     | ok               |

## BCH-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 41.45%   | -31.32%            | -45.51% |     0.58 |       74 | 57.28%     | ok               |
|          20 | 17.32%   | -31.32%            | -45.63% |     0.39 |       66 | 54.02%     | ok               |
|          25 | 0.73%    | -31.32%            | -51.09% |     0.23 |       70 | 50.38%     | ok               |
|          30 | 0.92%    | -31.32%            | -53.87% |     0.22 |       76 | 48.85%     | ok               |
|          35 | -5.16%   | -31.32%            | -57.75% |     0.15 |       70 | 45.02%     | ok               |

## BITO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -8.43%   | -60.41%            | -31.98% |     0.01 |       54 | 25.46%     | ok               |
|          30 | -24.31%  | -60.41%            | -43.10% |    -0.17 |       79 | 41.93%     | ok               |
|          45 | -21.04%  | -60.41%            | -34.45% |    -0.19 |       60 | 28.95%     | ok               |
|          40 | -25.13%  | -60.41%            | -40.13% |    -0.23 |       62 | 33.28%     | ok               |
|          35 | -27.10%  | -60.41%            | -42.34% |    -0.24 |       70 | 37.44%     | ok               |

## BLK Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | -6.56%   | 32.45%             | -20.79% |    -0.12 |       92 | 43.43%     | ok               |
|          40 | -7.81%   | 32.45%             | -22.83% |    -0.17 |       80 | 38.60%     | ok               |
|          20 | -9.72%   | 32.45%             | -21.48% |    -0.18 |       88 | 51.91%     | ok               |
|          25 | -11.02%  | 32.45%             | -24.62% |    -0.23 |       81 | 49.75%     | ok               |
|          30 | -15.14%  | 32.45%             | -26.90% |    -0.37 |       85 | 47.25%     | ok               |

## BND Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -6.44%   | -2.17%             | -10.08% |    -0.9  |       64 | 40.60%     | ok               |
|          25 | -7.09%   | -2.17%             | -11.14% |    -1.04 |       67 | 38.60%     | ok               |
|          30 | -6.82%   | -2.17%             | -10.79% |    -1.04 |       65 | 35.61%     | ok               |
|          15 | -8.15%   | -2.17%             | -11.40% |    -1.14 |       75 | 43.26%     | ok               |
|          40 | -8.07%   | -2.17%             | -11.70% |    -1.36 |       64 | 29.78%     | ok               |

## BONK-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 156.03%  | -85.34%            | -35.57% |     1.2  |       42 | 21.46%     | ok               |
|          45 | 65.56%   | -85.34%            | -42.36% |     0.74 |       64 | 27.39%     | ok               |
|          15 | 66.37%   | -85.34%            | -63.45% |     0.69 |       71 | 60.15%     | ok               |
|          20 | 42.39%   | -85.34%            | -55.43% |     0.58 |       68 | 55.94%     | ok               |
|          40 | 34.97%   | -85.34%            | -50.07% |     0.53 |       56 | 36.97%     | ok               |

## BTC-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 42.83%   | -19.56%            | -14.50% |     0.86 |       44 | 35.44%     | ok               |
|          45 | 38.36%   | -19.56%            | -12.20% |     0.82 |       42 | 31.42%     | ok               |
|          35 | 41.84%   | -19.56%            | -21.56% |     0.81 |       62 | 41.76%     | ok               |
|          50 | 18.02%   | -19.56%            | -20.63% |     0.49 |       38 | 26.44%     | ok               |
|          30 | 17.25%   | -19.56%            | -21.75% |     0.42 |       68 | 47.70%     | ok               |

## C Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -13.09%  | 92.35%             | -21.80% |    -0.32 |       66 | 31.28%     | ok               |
|          45 | -23.47%  | 92.35%             | -29.60% |    -0.61 |       74 | 35.44%     | ok               |
|          40 | -28.84%  | 92.35%             | -35.11% |    -0.73 |       74 | 37.77%     | ok               |
|          25 | -34.58%  | 92.35%             | -36.49% |    -0.74 |       69 | 48.25%     | ok               |
|          30 | -35.84%  | 92.35%             | -39.51% |    -0.79 |       77 | 46.09%     | ok               |

## CAT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 15.03%   | 115.22%            | -21.99% |     0.35 |       73 | 60.90%     | ok               |
|          25 | 11.13%   | 115.22%            | -21.79% |     0.3  |       66 | 50.58%     | ok               |
|          45 | 4.50%    | 115.22%            | -23.48% |     0.2  |       54 | 36.94%     | ok               |
|          30 | 3.76%    | 115.22%            | -21.87% |     0.19 |       70 | 48.25%     | ok               |
|          20 | 1.85%    | 115.22%            | -24.75% |     0.16 |       76 | 53.91%     | ok               |

## CL Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -2.59%   | -5.48%             | -12.98% |    -0.06 |       44 | 22.46%     | ok               |
|          30 | -6.20%   | -5.48%             | -14.32% |    -0.15 |       66 | 38.60%     | ok               |
|          45 | -8.24%   | -5.48%             | -13.13% |    -0.29 |       50 | 25.29%     | ok               |
|          35 | -9.94%   | -5.48%             | -15.39% |    -0.3  |       66 | 34.78%     | ok               |
|          15 | -14.61%  | -5.48%             | -19.00% |    -0.39 |       66 | 46.92%     | ok               |

## CMCSA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -18.51%  | -43.18%            | -28.41% |    -0.6  |       48 | 16.81%     | ok               |
|          45 | -23.14%  | -43.18%            | -35.13% |    -0.72 |       62 | 21.30%     | ok               |
|          15 | -34.90%  | -43.18%            | -46.99% |    -0.72 |       91 | 57.90%     | ok               |
|          30 | -34.73%  | -43.18%            | -46.39% |    -0.82 |       84 | 43.26%     | ok               |
|          40 | -31.00%  | -43.18%            | -42.51% |    -0.82 |       89 | 28.79%     | ok               |

## COMP-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -1.20%   | -51.20%            | -38.71% |     0.19 |       50 | 24.90%     | ok               |
|          30 | -37.68%  | -51.20%            | -55.77% |    -0.21 |       97 | 49.81%     | ok               |
|          25 | -43.96%  | -51.20%            | -54.62% |    -0.28 |       96 | 57.85%     | ok               |
|          15 | -48.64%  | -51.20%            | -54.29% |    -0.34 |       98 | 68.39%     | ok               |
|          40 | -43.87%  | -51.20%            | -52.04% |    -0.39 |       70 | 38.51%     | ok               |

## COP Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -5.09%   | 17.02%             | -34.61% |    -0.02 |       48 | 27.79%     | ok               |
|          35 | -13.77%  | 17.02%             | -44.33% |    -0.17 |       73 | 41.10%     | ok               |
|          30 | -15.24%  | 17.02%             | -43.40% |    -0.19 |       70 | 44.09%     | ok               |
|          45 | -14.14%  | 17.02%             | -41.30% |    -0.22 |       62 | 31.95%     | ok               |
|          40 | -23.33%  | 17.02%             | -48.77% |    -0.44 |       76 | 35.77%     | ok               |

## COST Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 10.90%   | 19.19%             | -24.32% |     0.38 |       62 | 47.09%     | ok               |
|          25 | 7.70%    | 19.19%             | -24.93% |     0.3  |       59 | 44.26%     | ok               |
|          35 | 1.48%    | 19.19%             | -30.16% |     0.11 |       58 | 38.60%     | ok               |
|          30 | -2.81%   | 19.19%             | -31.32% |    -0.03 |       60 | 41.10%     | ok               |
|          15 | -4.13%   | 19.19%             | -27.30% |    -0.04 |       67 | 50.75%     | ok               |

## CRM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | -22.78%  | -16.12%            | -34.06% |    -0.28 |       62 | 41.26%     | ok               |
|          40 | -25.67%  | -16.12%            | -39.44% |    -0.37 |       68 | 37.10%     | ok               |
|          15 | -32.11%  | -16.12%            | -47.54% |    -0.38 |       90 | 57.40%     | ok               |
|          50 | -22.09%  | -16.12%            | -38.38% |    -0.4  |       58 | 24.63%     | ok               |
|          30 | -33.40%  | -16.12%            | -45.50% |    -0.48 |       67 | 46.09%     | ok               |

## CRV-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 57.24%   | -56.25%            | -37.78% |     0.69 |       66 | 32.57%     | ok               |
|          40 | 43.23%   | -56.25%            | -38.86% |     0.6  |       54 | 28.35%     | ok               |
|          45 | 33.87%   | -56.25%            | -42.29% |     0.54 |       54 | 21.84%     | ok               |
|          50 | 32.96%   | -56.25%            | -30.73% |     0.54 |       46 | 17.82%     | ok               |
|          30 | 26.38%   | -56.25%            | -39.89% |     0.47 |       66 | 37.16%     | ok               |

## CSCO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 35.73%   | 145.14%            | -19.34% |     0.73 |       50 | 38.27%     | ok               |
|          45 | 31.14%   | 145.14%            | -19.34% |     0.65 |       52 | 39.93%     | ok               |
|          25 | 23.45%   | 145.14%            | -23.28% |     0.5  |       61 | 50.58%     | ok               |
|          20 | 17.91%   | 145.14%            | -22.72% |     0.41 |       71 | 52.91%     | ok               |
|          30 | 16.96%   | 145.14%            | -21.79% |     0.4  |       64 | 49.25%     | ok               |

## CVX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -9.60%   | 36.11%             | -23.80% |    -0.17 |       73 | 44.59%     | ok               |
|          40 | -10.08%  | 36.11%             | -27.34% |    -0.22 |       73 | 36.61%     | ok               |
|          45 | -10.48%  | 36.11%             | -28.83% |    -0.24 |       65 | 33.28%     | ok               |
|          50 | -10.36%  | 36.11%             | -30.69% |    -0.29 |       58 | 28.79%     | ok               |
|          35 | -13.01%  | 36.11%             | -28.85% |    -0.29 |       67 | 38.60%     | ok               |

## DASH-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 156.61%  | 106.66%            | -33.55% |     1.01 |       38 | 18.01%     | ok               |
|          40 | 125.75%  | 106.66%            | -33.20% |     0.89 |       42 | 24.33%     | ok               |
|          45 | 94.16%   | 106.66%            | -37.63% |     0.78 |       42 | 20.50%     | ok               |
|          30 | 0.17%    | 106.66%            | -64.43% |     0.39 |       55 | 30.46%     | ok               |
|          25 | -5.41%   | 106.66%            | -64.14% |     0.35 |       65 | 32.95%     | ok               |

## DBC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -0.09%   | 40.55%             | -26.05% |     0.07 |       77 | 41.26%     | ok               |
|          20 | -4.49%   | 40.55%             | -25.69% |    -0.08 |       69 | 39.60%     | ok               |
|          25 | -5.28%   | 40.55%             | -24.84% |    -0.11 |       66 | 37.60%     | ok               |
|          50 | -6.09%   | 40.55%             | -19.34% |    -0.18 |       50 | 24.79%     | ok               |
|          35 | -7.76%   | 40.55%             | -23.19% |    -0.2  |       66 | 34.28%     | ok               |

## DE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 2.13%    | 68.07%             | -17.97% |     0.13 |       56 | 29.62%     | ok               |
|          45 | -4.48%   | 68.07%             | -19.53% |    -0.02 |       60 | 34.11%     | ok               |
|          20 | -7.80%   | 68.07%             | -24.11% |    -0.07 |       65 | 48.59%     | ok               |
|          25 | -12.03%  | 68.07%             | -24.29% |    -0.17 |       71 | 46.92%     | ok               |
|          30 | -12.17%  | 68.07%             | -23.98% |    -0.18 |       70 | 44.26%     | ok               |

## DIA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -5.56%   | 29.45%             | -11.17% |    -0.27 |       58 | 44.93%     | ok               |
|          35 | -6.40%   | 29.45%             | -13.15% |    -0.33 |       68 | 40.60%     | ok               |
|          30 | -7.81%   | 29.45%             | -12.94% |    -0.4  |       66 | 43.59%     | ok               |
|          20 | -8.28%   | 29.45%             | -13.60% |    -0.41 |       64 | 46.92%     | ok               |
|          40 | -9.49%   | 29.45%             | -15.06% |    -0.55 |       70 | 37.27%     | ok               |

## DIS Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 32.96%   | 5.41%              | -10.17% |     1.03 |       44 | 25.29%     | ok               |
|          40 | 7.47%    | 5.41%              | -18.75% |     0.26 |       57 | 33.61%     | ok               |
|          45 | 2.94%    | 5.41%              | -16.54% |     0.16 |       45 | 28.95%     | ok               |
|          35 | -4.01%   | 5.41%              | -25.70% |    -0    |       71 | 39.77%     | ok               |
|          15 | -5.29%   | 5.41%              | -32.73% |    -0    |       83 | 54.41%     | ok               |

## DOGE-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 0.39%    | -63.28%            | -57.89% |     0.27 |       73 | 64.18%     | ok               |
|          20 | -7.34%   | -63.28%            | -55.83% |     0.18 |       75 | 58.81%     | ok               |
|          25 | -13.99%  | -63.28%            | -53.72% |     0.1  |       67 | 54.98%     | ok               |
|          30 | -30.71%  | -63.28%            | -60.95% |    -0.15 |       71 | 48.66%     | ok               |
|          50 | -31.67%  | -63.28%            | -55.41% |    -0.28 |       64 | 24.33%     | ok               |

## DOT-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -53.07%  | -77.06%            | -72.06% |    -0.33 |       74 | 63.41%     | ok               |
|          20 | -49.83%  | -77.06%            | -66.32% |    -0.34 |       86 | 59.39%     | ok               |
|          30 | -51.64%  | -77.06%            | -63.33% |    -0.43 |       86 | 48.47%     | ok               |
|          25 | -57.57%  | -77.06%            | -69.99% |    -0.51 |       77 | 54.41%     | ok               |
|          35 | -56.42%  | -77.06%            | -63.01% |    -0.56 |       84 | 42.91%     | ok               |

## DXY-INDEX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd    |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:-------|---------:|---------:|:-----------|:-----------------|
|          50 | -0.69%   | -4.55%             | -6.02% |    -0.09 |       40 | 32.25%     | ok               |
|          40 | -2.05%   | -4.55%             | -7.30% |    -0.25 |       64 | 47.62%     | ok               |
|          45 | -2.05%   | -4.55%             | -8.14% |    -0.27 |       60 | 38.31%     | ok               |
|          30 | -4.95%   | -4.55%             | -9.83% |    -0.59 |       74 | 57.58%     | ok               |
|          35 | -5.11%   | -4.55%             | -9.97% |    -0.64 |       77 | 52.60%     | ok               |

## EEM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -7.77%   | 51.61%             | -15.88% |    -0.23 |       54 | 32.61%     | ok               |
|          45 | -8.11%   | 51.61%             | -17.03% |    -0.24 |       52 | 34.11%     | ok               |
|          35 | -9.08%   | 51.61%             | -23.57% |    -0.24 |       66 | 38.27%     | ok               |
|          40 | -8.44%   | 51.61%             | -19.20% |    -0.24 |       64 | 36.27%     | ok               |
|          30 | -12.31%  | 51.61%             | -24.40% |    -0.35 |       62 | 40.10%     | ok               |

## EFA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -3.47%   | 26.85%             | -10.10% |    -0.06 |       62 | 51.75%     | ok               |
|          20 | -11.05%  | 26.85%             | -13.36% |    -0.39 |       71 | 48.75%     | ok               |
|          30 | -11.10%  | 26.85%             | -12.45% |    -0.43 |       68 | 41.93%     | ok               |
|          40 | -11.21%  | 26.85%             | -13.74% |    -0.47 |       64 | 36.94%     | ok               |
|          25 | -12.85%  | 26.85%             | -15.56% |    -0.49 |       70 | 45.09%     | ok               |

## EOG Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -19.01%  | 18.83%             | -35.29% |    -0.41 |       58 | 30.62%     | ok               |
|          50 | -23.47%  | 18.83%             | -35.58% |    -0.58 |       54 | 27.79%     | ok               |
|          40 | -25.14%  | 18.83%             | -37.34% |    -0.58 |       74 | 34.61%     | ok               |
|          30 | -30.38%  | 18.83%             | -47.87% |    -0.66 |       78 | 44.76%     | ok               |
|          35 | -29.12%  | 18.83%             | -42.07% |    -0.68 |       85 | 39.43%     | ok               |

## ETC-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -5.47%   | -59.21%            | -38.47% |     0.05 |       28 | 20.50%     | ok               |
|          50 | -4.94%   | -59.21%            | -31.28% |     0.05 |       28 | 18.20%     | ok               |
|          40 | -17.03%  | -59.21%            | -43.28% |    -0.15 |       38 | 23.56%     | ok               |
|          35 | -19.28%  | -59.21%            | -45.32% |    -0.16 |       42 | 27.01%     | ok               |
|          30 | -26.56%  | -59.21%            | -48.09% |    -0.28 |       60 | 31.23%     | ok               |

## ETH-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 144.86%  | -0.06%             | -30.11% |     1.31 |       58 | 48.28%     | ok               |
|          30 | 106.56%  | -0.06%             | -32.89% |     1.05 |       60 | 55.94%     | ok               |
|          40 | 64.94%   | -0.06%             | -33.11% |     0.85 |       62 | 40.61%     | ok               |
|          25 | 69.09%   | -0.06%             | -40.90% |     0.81 |       60 | 59.77%     | ok               |
|          50 | 41.55%   | -0.06%             | -30.50% |     0.69 |       66 | 29.89%     | ok               |

## EWJ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -22.99%  | 41.41%             | -29.40% |    -0.8  |       62 | 36.44%     | ok               |
|          20 | -23.95%  | 41.41%             | -30.00% |    -0.81 |       56 | 38.44%     | ok               |
|          25 | -25.82%  | 41.41%             | -29.85% |    -0.9  |       56 | 37.60%     | ok               |
|          15 | -27.60%  | 41.41%             | -31.15% |    -0.9  |       67 | 41.76%     | ok               |
|          45 | -22.89%  | 41.41%             | -26.67% |    -0.92 |       60 | 28.62%     | ok               |

## FCX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 2.51%    | 33.32%             | -29.27% |     0.18 |       50 | 31.61%     | ok               |
|          50 | -0.09%   | 33.32%             | -26.57% |     0.13 |       52 | 27.95%     | ok               |
|          40 | -10.00%  | 33.32%             | -42.89% |    -0.01 |       62 | 36.94%     | ok               |
|          30 | -29.37%  | 33.32%             | -46.84% |    -0.32 |       65 | 44.26%     | ok               |
|          35 | -29.20%  | 33.32%             | -50.12% |    -0.34 |       67 | 42.10%     | ok               |

## FET-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -28.62%  | -74.11%            | -64.89% |     0.02 |       88 | 52.49%     | ok               |
|          15 | -30.49%  | -74.11%            | -59.58% |     0.02 |       82 | 57.09%     | ok               |
|          25 | -30.33%  | -74.11%            | -65.31% |    -0.02 |       81 | 46.93%     | ok               |
|          30 | -46.79%  | -74.11%            | -65.38% |    -0.29 |       79 | 42.34%     | ok               |
|          50 | -39.06%  | -74.11%            | -45.19% |    -0.53 |       46 | 14.37%     | ok               |

## FIL-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -40.15%  | -61.95%            | -58.54% |    -0.34 |       65 | 37.16%     | ok               |
|          35 | -41.96%  | -61.95%            | -61.90% |    -0.42 |       58 | 31.23%     | ok               |
|          40 | -40.23%  | -61.95%            | -57.60% |    -0.44 |       48 | 26.82%     | ok               |
|          15 | -58.37%  | -61.95%            | -71.82% |    -0.57 |       91 | 49.04%     | ok               |
|          25 | -58.52%  | -61.95%            | -70.65% |    -0.66 |       76 | 40.04%     | ok               |

## FXI Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -8.12%   | 19.64%             | -22.99% |    -0.12 |       52 | 32.78%     | ok               |
|          15 | -8.97%   | 19.64%             | -21.68% |    -0.13 |       54 | 36.77%     | ok               |
|          30 | -8.38%   | 19.64%             | -24.33% |    -0.13 |       50 | 31.28%     | ok               |
|          20 | -11.63%  | 19.64%             | -24.94% |    -0.21 |       54 | 34.61%     | ok               |
|          35 | -11.93%  | 19.64%             | -27.93% |    -0.24 |       52 | 28.79%     | ok               |

## GDX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 2.04%    | 136.23%            | -31.44% |     0.18 |       76 | 50.25%     | ok               |
|          40 | 2.74%    | 136.23%            | -28.04% |     0.17 |       60 | 38.44%     | ok               |
|          30 | -2.45%   | 136.23%            | -33.31% |     0.1  |       62 | 44.59%     | ok               |
|          35 | -3.20%   | 136.23%            | -31.73% |     0.08 |       68 | 41.10%     | ok               |
|          25 | -10.43%  | 136.23%            | -38.90% |    -0.03 |       66 | 46.26%     | ok               |

## GDXJ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -26.47%  | 136.19%            | -41.17% |    -0.22 |       74 | 50.25%     | ok               |
|          50 | -28.98%  | 136.19%            | -46.83% |    -0.4  |       58 | 34.44%     | ok               |
|          35 | -36.47%  | 136.19%            | -37.32% |    -0.49 |       72 | 40.43%     | ok               |
|          30 | -38.23%  | 136.19%            | -40.39% |    -0.51 |       72 | 43.09%     | ok               |
|          25 | -41.98%  | 136.19%            | -42.91% |    -0.56 |       77 | 46.26%     | ok               |

## GE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 4.89%    | 91.07%             | -21.25% |     0.2  |       60 | 33.78%     | ok               |
|          45 | -2.34%   | 91.07%             | -21.88% |     0.05 |       70 | 36.44%     | ok               |
|          30 | -8.43%   | 91.07%             | -27.82% |    -0.04 |       76 | 48.09%     | ok               |
|          25 | -8.86%   | 91.07%             | -29.91% |    -0.05 |       72 | 49.92%     | ok               |
|          20 | -9.37%   | 91.07%             | -25.05% |    -0.05 |       72 | 52.58%     | ok               |

## GLD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | 14.72%   | 70.21%             | -13.87% |     0.42 |       48 | 46.92%     | ok               |
|          20 | 13.16%   | 70.21%             | -13.87% |     0.38 |       49 | 48.59%     | ok               |
|          30 | 9.26%    | 70.21%             | -13.87% |     0.3  |       50 | 45.76%     | ok               |
|          35 | 6.37%    | 70.21%             | -15.09% |     0.24 |       52 | 43.43%     | ok               |
|          15 | 2.76%    | 70.21%             | -18.05% |     0.16 |       57 | 51.91%     | ok               |

## GOOGL Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 60.18%   | 98.92%             | -17.38% |     1.07 |       59 | 43.93%     | ok               |
|          30 | 56.30%   | 98.92%             | -17.54% |     1    |       57 | 47.42%     | ok               |
|          45 | 48.78%   | 98.92%             | -11.66% |     0.98 |       52 | 37.44%     | ok               |
|          25 | 53.92%   | 98.92%             | -16.87% |     0.95 |       57 | 49.92%     | ok               |
|          50 | 44.40%   | 98.92%             | -11.52% |     0.94 |       44 | 32.61%     | ok               |

## GRT-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 66.81%   | -77.69%            | -33.74% |     0.75 |       77 | 45.59%     | ok               |
|          15 | 60.16%   | -77.69%            | -42.58% |     0.68 |       69 | 62.45%     | ok               |
|          45 | 45.48%   | -77.69%            | -39.70% |     0.64 |       48 | 27.97%     | ok               |
|          25 | 41.14%   | -77.69%            | -37.67% |     0.57 |       78 | 52.30%     | ok               |
|          50 | 31.50%   | -77.69%            | -31.62% |     0.53 |       46 | 21.26%     | ok               |

## GS Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 19.78%   | 89.60%             | -20.56% |     0.45 |       68 | 56.41%     | ok               |
|          20 | 1.37%    | 89.60%             | -23.19% |     0.13 |       68 | 53.08%     | ok               |
|          40 | 0.00%    | 89.60%             | -16.45% |     0.09 |       68 | 42.26%     | ok               |
|          25 | -3.76%   | 89.60%             | -23.32% |     0.02 |       68 | 50.58%     | ok               |
|          30 | -5.86%   | 89.60%             | -21.94% |    -0.03 |       70 | 48.09%     | ok               |

## HBAR-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -18.60%  | -15.47%            | -39.26% |    -0.27 |       18 | 17.87%     | ok               |
|          45 | -33.67%  | -15.47%            | -48.27% |    -0.69 |       22 | 23.95%     | ok               |
|          40 | -36.66%  | -15.47%            | -50.61% |    -0.77 |       26 | 28.52%     | ok               |
|          30 | -44.37%  | -15.47%            | -56.62% |    -0.99 |       40 | 37.64%     | ok               |
|          35 | -43.78%  | -15.47%            | -56.16% |    -1    |       30 | 33.08%     | ok               |

## HD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 1.75%    | -12.56%            | -17.15% |     0.13 |       67 | 43.59%     | ok               |
|          40 | 1.06%    | -12.56%            | -16.74% |     0.1  |       72 | 34.78%     | ok               |
|          35 | 0.87%    | -12.56%            | -17.81% |     0.1  |       70 | 39.60%     | ok               |
|          45 | 0.27%    | -12.56%            | -17.41% |     0.07 |       48 | 29.95%     | ok               |
|          25 | -0.82%   | -12.56%            | -18.17% |     0.06 |       66 | 45.76%     | ok               |

## HON Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -11.48%  | 3.05%              | -20.54% |    -0.29 |       70 | 33.11%     | ok               |
|          45 | -15.18%  | 3.05%              | -22.88% |    -0.39 |       72 | 38.60%     | ok               |
|          35 | -25.07%  | 3.05%              | -31.30% |    -0.64 |       89 | 49.92%     | ok               |
|          30 | -26.78%  | 3.05%              | -33.53% |    -0.67 |       93 | 54.91%     | ok               |
|          40 | -25.39%  | 3.05%              | -31.84% |    -0.68 |       76 | 42.93%     | ok               |

## HYG Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -5.15%   | -0.22%             | -7.94%  |    -0.59 |       70 | 33.78%     | ok               |
|          45 | -6.60%   | -0.22%             | -9.08%  |    -0.8  |       70 | 30.28%     | ok               |
|          35 | -6.97%   | -0.22%             | -9.70%  |    -0.8  |       79 | 35.44%     | ok               |
|          30 | -7.18%   | -0.22%             | -10.59% |    -0.81 |       87 | 38.77%     | ok               |
|          15 | -7.84%   | -0.22%             | -11.21% |    -0.83 |       92 | 46.26%     | ok               |

## IBIT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 68.14%   | 23.99%             | -19.20% |     0.97 |       44 | 41.87%     | ok               |
|          50 | 52.34%   | 23.99%             | -17.37% |     0.94 |       26 | 25.61%     | ok               |
|          45 | 42.96%   | 23.99%             | -17.37% |     0.8  |       30 | 26.83%     | ok               |
|          40 | 36.57%   | 23.99%             | -17.78% |     0.71 |       30 | 28.66%     | ok               |
|          30 | 39.17%   | 23.99%             | -18.95% |     0.71 |       40 | 34.96%     | ok               |

## IBM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -20.11%  | 33.04%             | -49.43% |    -0.16 |       83 | 60.90%     | ok               |
|          35 | -23.03%  | 33.04%             | -47.10% |    -0.26 |       63 | 45.76%     | ok               |
|          30 | -26.24%  | 33.04%             | -48.94% |    -0.32 |       69 | 49.42%     | ok               |
|          50 | -27.32%  | 33.04%             | -45.88% |    -0.39 |       46 | 35.11%     | ok               |
|          45 | -27.96%  | 33.04%             | -48.72% |    -0.39 |       50 | 37.60%     | ok               |

## ICP-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -17.84%  | -45.65%            | -46.42% |     0.09 |       79 | 39.27%     | ok               |
|          35 | -11.56%  | -45.65%            | -51.30% |     0.09 |       70 | 33.33%     | ok               |
|          40 | -12.10%  | -45.65%            | -45.75% |     0.07 |       62 | 28.74%     | ok               |
|          15 | -44.09%  | -45.65%            | -59.36% |    -0.13 |       79 | 50.57%     | ok               |
|          20 | -46.10%  | -45.65%            | -62.50% |    -0.18 |       88 | 47.51%     | ok               |

## IEF Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -6.49%   | -3.94%             | -10.18% |    -0.76 |       72 | 42.26%     | ok               |
|          15 | -7.04%   | -3.94%             | -10.91% |    -0.82 |       71 | 43.76%     | ok               |
|          40 | -8.44%   | -3.94%             | -11.24% |    -1.23 |       64 | 27.12%     | ok               |
|          50 | -7.38%   | -3.94%             | -9.11%  |    -1.24 |       58 | 22.13%     | ok               |
|          25 | -10.06%  | -3.94%             | -11.95% |    -1.27 |       76 | 39.60%     | ok               |

## IEMG Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -3.44%   | 47.38%             | -14.22% |    -0.08 |       54 | 31.45%     | ok               |
|          45 | -4.23%   | 47.38%             | -15.23% |    -0.11 |       50 | 33.94%     | ok               |
|          40 | -5.71%   | 47.38%             | -18.73% |    -0.16 |       62 | 36.94%     | ok               |
|          35 | -7.10%   | 47.38%             | -23.75% |    -0.19 |       65 | 39.27%     | ok               |
|          25 | -11.20%  | 47.38%             | -26.49% |    -0.33 |       60 | 42.10%     | ok               |

## INJ-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 11.82%   | -36.65%            | -52.61% |     0.36 |       60 | 36.97%     | ok               |
|          40 | 12.49%   | -36.65%            | -45.92% |     0.35 |       50 | 33.72%     | ok               |
|          45 | 3.26%    | -36.65%            | -43.79% |     0.25 |       54 | 28.16%     | ok               |
|          30 | -21.00%  | -36.65%            | -69.36% |     0.05 |       65 | 40.42%     | ok               |
|          15 | -35.41%  | -36.65%            | -76.78% |    -0.07 |       77 | 51.34%     | ok               |

## INTC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 70.01%   | 223.91%            | -49.32% |     0.71 |       56 | 33.78%     | ok               |
|          50 | 64.73%   | 223.91%            | -48.35% |     0.68 |       60 | 29.95%     | ok               |
|          15 | 64.27%   | 223.91%            | -53.65% |     0.65 |       76 | 59.73%     | ok               |
|          40 | 51.36%   | 223.91%            | -55.86% |     0.59 |       64 | 37.94%     | ok               |
|          25 | 46.47%   | 223.91%            | -56.41% |     0.56 |       77 | 50.75%     | ok               |

## INTU Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 14.17%   | -54.86%            | -32.38% |     0.35 |       67 | 28.95%     | ok               |
|          45 | -0.12%   | -54.86%            | -39.62% |     0.12 |       65 | 33.11%     | ok               |
|          40 | -4.58%   | -54.86%            | -41.86% |     0.04 |       67 | 37.10%     | ok               |
|          25 | -6.72%   | -54.86%            | -35.05% |     0.03 |       70 | 49.42%     | ok               |
|          30 | -11.45%  | -54.86%            | -37.50% |    -0.05 |       73 | 46.76%     | ok               |

## ITA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -1.54%   | 49.46%             | -28.06% |     0.05 |       83 | 60.90%     | ok               |
|          50 | -1.65%   | 49.46%             | -21.48% |     0.01 |       76 | 36.94%     | ok               |
|          30 | -3.85%   | 49.46%             | -23.75% |    -0.03 |       76 | 48.59%     | ok               |
|          20 | -7.82%   | 49.46%             | -28.06% |    -0.13 |       84 | 54.91%     | ok               |
|          40 | -7.20%   | 49.46%             | -20.58% |    -0.15 |       76 | 41.93%     | ok               |

## IWM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | 10.60%   | 32.81%             | -11.13% |     0.43 |       52 | 34.94%     | ok               |
|          20 | 9.14%    | 32.81%             | -10.90% |     0.37 |       58 | 35.94%     | ok               |
|          30 | 6.91%    | 32.81%             | -11.44% |     0.31 |       54 | 34.28%     | ok               |
|          40 | 5.96%    | 32.81%             | -12.74% |     0.3  |       46 | 29.62%     | ok               |
|          15 | 5.79%    | 32.81%             | -12.59% |     0.25 |       76 | 41.76%     | ok               |

## JNJ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 17.02%   | 64.38%             | -10.57% |     0.7  |       40 | 34.78%     | ok               |
|          15 | 13.80%   | 64.38%             | -17.37% |     0.5  |       58 | 53.41%     | ok               |
|          20 | 8.54%    | 64.38%             | -16.96% |     0.35 |       64 | 49.92%     | ok               |
|          45 | 7.01%    | 64.38%             | -13.35% |     0.32 |       46 | 38.44%     | ok               |
|          30 | 7.29%    | 64.38%             | -16.86% |     0.31 |       60 | 46.76%     | ok               |

## JPM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 4.03%    | 66.11%             | -15.90% |     0.2  |       50 | 33.11%     | ok               |
|          45 | -6.34%   | 66.11%             | -21.91% |    -0.14 |       54 | 35.77%     | ok               |
|          20 | -21.51%  | 66.11%             | -35.58% |    -0.47 |       86 | 49.25%     | ok               |
|          35 | -18.54%  | 66.11%             | -27.43% |    -0.53 |       74 | 41.60%     | ok               |
|          40 | -19.19%  | 66.11%             | -28.47% |    -0.56 |       66 | 38.44%     | ok               |

## KO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 23.40%   | 43.24%             | -8.64%  |     0.83 |       54 | 36.94%     | ok               |
|          35 | 19.21%   | 43.24%             | -8.21%  |     0.71 |       58 | 35.44%     | ok               |
|          40 | 16.34%   | 43.24%             | -9.28%  |     0.66 |       60 | 32.11%     | ok               |
|          25 | 17.22%   | 43.24%             | -10.16% |     0.64 |       60 | 39.77%     | ok               |
|          20 | 4.28%    | 43.24%             | -15.99% |     0.21 |       77 | 43.93%     | ok               |

## LDO-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 70.58%   | -60.78%            | -39.01% |     0.72 |       77 | 59.20%     | ok               |
|          20 | 55.19%   | -60.78%            | -40.80% |     0.65 |       79 | 54.41%     | ok               |
|          30 | 44.87%   | -60.78%            | -50.47% |     0.6  |       70 | 46.55%     | ok               |
|          25 | 21.03%   | -60.78%            | -50.23% |     0.44 |       80 | 51.53%     | ok               |
|          35 | 21.59%   | -60.78%            | -58.19% |     0.43 |       76 | 39.08%     | ok               |

## LIN Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -8.00%   | 13.12%             | -23.00% |    -0.21 |       66 | 44.26%     | ok               |
|          25 | -7.93%   | 13.12%             | -22.01% |    -0.22 |       73 | 41.26%     | ok               |
|          15 | -9.79%   | 13.12%             | -23.68% |    -0.27 |       72 | 47.75%     | ok               |
|          30 | -11.01%  | 13.12%             | -20.61% |    -0.35 |       74 | 38.44%     | ok               |
|          35 | -11.93%  | 13.12%             | -19.70% |    -0.42 |       74 | 31.78%     | ok               |

## LINK-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 43.55%   | -23.77%            | -33.64% |     0.61 |       68 | 45.59%     | ok               |
|          45 | 22.32%   | -23.77%            | -33.71% |     0.44 |       52 | 31.99%     | ok               |
|          35 | 20.12%   | -23.77%            | -34.21% |     0.42 |       62 | 41.57%     | ok               |
|          40 | 12.35%   | -23.77%            | -34.00% |     0.34 |       58 | 36.02%     | ok               |
|          25 | 0.06%    | -23.77%            | -46.32% |     0.25 |       64 | 49.04%     | ok               |

## LLY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -5.90%   | 45.24%             | -38.23% |    -0.01 |       50 | 35.44%     | ok               |
|          15 | -17.54%  | 45.24%             | -48.12% |    -0.15 |       70 | 60.40%     | ok               |
|          45 | -18.17%  | 45.24%             | -42.66% |    -0.26 |       58 | 38.94%     | ok               |
|          20 | -30.71%  | 45.24%             | -51.34% |    -0.44 |       77 | 55.41%     | ok               |
|          25 | -31.45%  | 45.24%             | -53.47% |    -0.47 |       73 | 52.41%     | ok               |

## LRCX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -9.25%   | 212.35%            | -42.40% |     0.04 |       72 | 33.78%     | ok               |
|          40 | -12.29%  | 212.35%            | -47.73% |     0.02 |       68 | 39.93%     | ok               |
|          45 | -20.04%  | 212.35%            | -47.62% |    -0.1  |       72 | 37.60%     | ok               |
|          35 | -23.40%  | 212.35%            | -56.72% |    -0.13 |       78 | 42.26%     | ok               |
|          30 | -27.50%  | 212.35%            | -58.92% |    -0.19 |       80 | 42.76%     | ok               |

## LTC-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 13.70%   | -37.85%            | -34.94% |     0.35 |       64 | 45.79%     | ok               |
|          45 | 11.87%   | -37.85%            | -37.46% |     0.33 |       58 | 36.21%     | ok               |
|          30 | 3.16%    | -37.85%            | -31.73% |     0.24 |       67 | 52.87%     | ok               |
|          25 | -0.54%   | -37.85%            | -34.22% |     0.2  |       69 | 55.17%     | ok               |
|          40 | -7.07%   | -37.85%            | -40.31% |     0.08 |       56 | 41.38%     | ok               |

## MCD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 10.53%   | -11.31%            | -9.22%  |     0.49 |       46 | 25.12%     | ok               |
|          45 | 1.26%    | -11.31%            | -16.79% |     0.1  |       52 | 28.95%     | ok               |
|          30 | -0.10%   | -11.31%            | -21.88% |     0.05 |       77 | 40.77%     | ok               |
|          40 | -0.09%   | -11.31%            | -18.49% |     0.05 |       67 | 32.28%     | ok               |
|          25 | -0.65%   | -11.31%            | -23.62% |     0.03 |       75 | 43.09%     | ok               |

## META Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -6.37%   | 64.11%             | -37.10% |     0    |       66 | 39.93%     | ok               |
|          40 | -12.74%  | 64.11%             | -40.49% |    -0.11 |       70 | 43.09%     | ok               |
|          50 | -16.43%  | 64.11%             | -38.63% |    -0.21 |       68 | 35.61%     | ok               |
|          25 | -22.47%  | 64.11%             | -45.35% |    -0.27 |       77 | 53.08%     | ok               |
|          30 | -23.10%  | 64.11%             | -44.52% |    -0.29 |       76 | 50.25%     | ok               |

## MPC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 34.68%   | 170.12%            | -18.24% |     0.67 |       50 | 40.10%     | ok               |
|          40 | 32.46%   | 170.12%            | -20.11% |     0.61 |       60 | 46.76%     | ok               |
|          45 | 30.14%   | 170.12%            | -19.46% |     0.59 |       56 | 44.09%     | ok               |
|          35 | 29.47%   | 170.12%            | -31.08% |     0.56 |       68 | 49.42%     | ok               |
|          30 | 22.17%   | 170.12%            | -34.29% |     0.46 |       70 | 51.91%     | ok               |

## MRK Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -13.09%  | 8.58%              | -28.39% |    -0.16 |       83 | 51.91%     | ok               |
|          25 | -13.85%  | 8.58%              | -31.07% |    -0.2  |       70 | 44.09%     | ok               |
|          20 | -18.07%  | 8.58%              | -29.34% |    -0.29 |       75 | 47.42%     | ok               |
|          50 | -14.54%  | 8.58%              | -23.01% |    -0.3  |       56 | 28.45%     | ok               |
|          45 | -16.67%  | 8.58%              | -25.38% |    -0.33 |       57 | 31.78%     | ok               |

## MS Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -0.31%   | 83.83%             | -19.99% |     0.07 |       72 | 39.43%     | ok               |
|          15 | -2.39%   | 83.83%             | -22.02% |     0.05 |       74 | 58.24%     | ok               |
|          20 | -4.70%   | 83.83%             | -25.68% |    -0.02 |       75 | 53.08%     | ok               |
|          30 | -9.65%   | 83.83%             | -27.79% |    -0.15 |       75 | 48.25%     | ok               |
|          25 | -11.03%  | 83.83%             | -28.36% |    -0.19 |       73 | 50.42%     | ok               |

## MSFT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -11.96%  | 26.67%             | -24.64% |    -0.25 |       74 | 37.60%     | ok               |
|          50 | -17.12%  | 26.67%             | -25.48% |    -0.43 |       64 | 31.95%     | ok               |
|          35 | -21.36%  | 26.67%             | -35.38% |    -0.45 |       75 | 46.59%     | ok               |
|          40 | -21.55%  | 26.67%             | -34.92% |    -0.48 |       73 | 41.43%     | ok               |
|          30 | -24.63%  | 26.67%             | -39.07% |    -0.52 |       85 | 51.25%     | ok               |

## MU Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 167.07%  | 647.60%            | -63.96% |     1.1  |       58 | 48.09%     | ok               |
|          15 | 190.29%  | 647.60%            | -61.96% |     1.09 |       51 | 59.73%     | ok               |
|          30 | 140.26%  | 647.60%            | -68.76% |     1    |       51 | 52.75%     | ok               |
|          25 | 138.86%  | 647.60%            | -67.90% |     0.98 |       51 | 54.24%     | ok               |
|          35 | 133.62%  | 647.60%            | -69.09% |     0.98 |       63 | 50.42%     | ok               |

## NEAR-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 188.04%  | 63.10%             | -38.95% |     1.3  |       28 | 21.84%     | ok               |
|          40 | 201.45%  | 63.10%             | -41.76% |     1.25 |       42 | 31.42%     | ok               |
|          45 | 152.99%  | 63.10%             | -38.08% |     1.11 |       44 | 27.39%     | ok               |
|          30 | 153.48%  | 63.10%             | -47.03% |     1.05 |       73 | 44.25%     | ok               |
|          35 | 142.72%  | 63.10%             | -52.37% |     1.05 |       64 | 36.02%     | ok               |

## NEM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -1.76%   | 162.47%            | -31.25% |     0.15 |       63 | 58.57%     | ok               |
|          20 | -2.49%   | 162.47%            | -30.50% |     0.13 |       70 | 54.08%     | ok               |
|          25 | -19.39%  | 162.47%            | -39.51% |    -0.13 |       66 | 51.91%     | ok               |
|          50 | -19.11%  | 162.47%            | -33.24% |    -0.17 |       52 | 38.27%     | ok               |
|          30 | -28.06%  | 162.47%            | -39.56% |    -0.29 |       70 | 50.08%     | ok               |

## NFLX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 28.96%   | 8.30%              | -16.28% |     0.74 |       44 | 33.44%     | ok               |
|          40 | 27.88%   | 8.30%              | -15.02% |     0.67 |       50 | 41.43%     | ok               |
|          35 | 23.52%   | 8.30%              | -18.30% |     0.56 |       74 | 46.09%     | ok               |
|          45 | 16.42%   | 8.30%              | -15.48% |     0.46 |       56 | 37.94%     | ok               |
|          15 | 10.25%   | 8.30%              | -26.59% |     0.29 |       71 | 65.06%     | ok               |

## NKE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | -16.21%  | -61.94%            | -42.13% |    -0.15 |       71 | 40.43%     | ok               |
|          20 | -21.11%  | -61.94%            | -50.44% |    -0.18 |       85 | 53.91%     | ok               |
|          25 | -22.70%  | -61.94%            | -51.20% |    -0.21 |       83 | 51.08%     | ok               |
|          15 | -26.20%  | -61.94%            | -55.28% |    -0.26 |       87 | 57.74%     | ok               |
|          30 | -26.45%  | -61.94%            | -55.35% |    -0.28 |       79 | 46.92%     | ok               |

## NOW Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 11.00%   | -10.81%            | -30.43% |     0.3  |       80 | 50.25%     | ok               |
|          20 | 8.52%    | -10.81%            | -39.71% |     0.28 |       75 | 56.57%     | ok               |
|          25 | 5.77%    | -10.81%            | -37.51% |     0.25 |       72 | 53.74%     | ok               |
|          15 | 0.58%    | -10.81%            | -43.06% |     0.19 |       83 | 59.57%     | ok               |
|          40 | 1.17%    | -10.81%            | -36.21% |     0.17 |       72 | 39.43%     | ok               |

## NVDA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -34.05%  | 93.78%             | -41.21% |    -0.5  |       76 | 44.03%     | ok               |
|          20 | -42.81%  | 93.78%             | -42.84% |    -0.59 |       76 | 52.05%     | ok               |
|          25 | -42.72%  | 93.78%             | -42.74% |    -0.65 |       77 | 47.06%     | ok               |
|          15 | -48.50%  | 93.78%             | -52.37% |    -0.68 |       77 | 55.44%     | ok               |
|          35 | -43.97%  | 93.78%             | -49.92% |    -0.78 |       86 | 41.18%     | ok               |

## OP-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 37.50%   | -81.86%            | -22.60% |     0.69 |       32 | 9.20%      | ok               |
|          45 | 33.05%   | -81.86%            | -25.91% |     0.57 |       34 | 13.79%     | ok               |
|          40 | 4.27%    | -81.86%            | -38.97% |     0.24 |       46 | 22.03%     | ok               |
|          15 | -36.95%  | -81.86%            | -55.83% |    -0.16 |       74 | 44.64%     | ok               |
|          35 | -28.86%  | -81.86%            | -51.88% |    -0.2  |       58 | 27.01%     | ok               |

## ORCL Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 164.44%  | 14.90%             | -32.54% |     1.11 |       69 | 61.90%     | ok               |
|          25 | 112.61%  | 14.90%             | -27.76% |     0.92 |       61 | 54.41%     | ok               |
|          45 | 97.66%   | 14.90%             | -32.35% |     0.91 |       58 | 39.93%     | ok               |
|          35 | 102.55%  | 14.90%             | -31.95% |     0.9  |       62 | 48.59%     | ok               |
|          20 | 106.68%  | 14.90%             | -29.32% |     0.89 |       70 | 57.57%     | ok               |

## OXY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 2.99%    | -2.68%             | -28.48% |     0.17 |       73 | 42.60%     | ok               |
|          35 | 0.68%    | -2.68%             | -26.37% |     0.13 |       74 | 38.10%     | ok               |
|          50 | -1.66%   | -2.68%             | -26.34% |     0.07 |       46 | 27.12%     | ok               |
|          40 | -5.52%   | -2.68%             | -28.30% |     0.01 |       64 | 33.94%     | ok               |
|          25 | -11.27%  | -2.68%             | -38.51% |    -0.07 |       79 | 46.26%     | ok               |

## PEP Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 15.04%   | -29.70%            | -11.62% |     0.64 |       40 | 25.12%     | ok               |
|          45 | 7.69%    | -29.70%            | -14.22% |     0.35 |       56 | 29.12%     | ok               |
|          35 | 5.84%    | -29.70%            | -21.42% |     0.25 |       77 | 39.60%     | ok               |
|          40 | 3.56%    | -29.70%            | -18.04% |     0.18 |       70 | 34.94%     | ok               |
|          30 | 0.12%    | -29.70%            | -21.35% |     0.07 |       74 | 45.92%     | ok               |

## PEPE-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -53.85%  | -68.99%            | -61.29% |    -0.4  |       83 | 48.47%     | ok               |
|          25 | -59.79%  | -68.99%            | -64.26% |    -0.49 |       93 | 53.45%     | ok               |
|          15 | -67.94%  | -68.99%            | -69.80% |    -0.51 |       82 | 62.64%     | ok               |
|          35 | -55.41%  | -68.99%            | -61.54% |    -0.53 |       72 | 43.49%     | ok               |
|          20 | -64.80%  | -68.99%            | -66.84% |    -0.54 |       88 | 59.20%     | ok               |

## PFE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -15.89%  | -0.67%             | -23.37% |    -0.5  |       52 | 21.63%     | ok               |
|          40 | -17.46%  | -0.67%             | -27.08% |    -0.53 |       72 | 26.62%     | ok               |
|          50 | -16.36%  | -0.67%             | -25.42% |    -0.57 |       40 | 18.47%     | ok               |
|          35 | -25.41%  | -0.67%             | -32.87% |    -0.78 |       82 | 33.11%     | ok               |
|          30 | -34.23%  | -0.67%             | -41.90% |    -1.05 |       81 | 36.77%     | ok               |

## PG Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -11.29%  | -9.09%             | -17.50% |    -0.46 |       54 | 27.79%     | ok               |
|          35 | -16.57%  | -9.09%             | -18.57% |    -0.67 |       62 | 31.45%     | ok               |
|          45 | -20.36%  | -9.09%             | -20.08% |    -0.95 |       54 | 25.12%     | ok               |
|          30 | -24.15%  | -9.09%             | -24.16% |    -0.98 |       64 | 34.61%     | ok               |
|          25 | -25.92%  | -9.09%             | -25.66% |    -1.06 |       74 | 35.94%     | ok               |

## PM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | -4.75%   | 98.83%             | -32.20% |    -0.02 |       84 | 46.76%     | ok               |
|          20 | -7.24%   | 98.83%             | -33.51% |    -0.07 |       83 | 55.41%     | ok               |
|          30 | -7.74%   | 98.83%             | -35.15% |    -0.09 |       79 | 50.25%     | ok               |
|          40 | -12.02%  | 98.83%             | -37.94% |    -0.23 |       78 | 42.76%     | ok               |
|          50 | -11.56%  | 98.83%             | -35.70% |    -0.23 |       68 | 36.94%     | ok               |

## POL-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 51.05%   | -60.11%            | -38.69% |     0.67 |       79 | 49.62%     | ok               |
|          25 | 25.17%   | -60.11%            | -38.69% |     0.46 |       71 | 54.98%     | ok               |
|          20 | 20.09%   | -60.11%            | -41.15% |     0.42 |       77 | 58.62%     | ok               |
|          40 | 4.59%    | -60.11%            | -31.98% |     0.24 |       56 | 30.84%     | ok               |
|          15 | -4.60%   | -60.11%            | -46.34% |     0.19 |       82 | 62.64%     | ok               |

## QCOM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -12.93%  | -11.94%            | -55.66% |     0.02 |       71 | 45.26%     | ok               |
|          20 | -19.33%  | -11.94%            | -55.54% |    -0.07 |       67 | 48.59%     | ok               |
|          35 | -20.28%  | -11.94%            | -51.84% |    -0.11 |       79 | 40.93%     | ok               |
|          15 | -29.08%  | -11.94%            | -59.01% |    -0.21 |       69 | 51.25%     | ok               |
|          30 | -29.59%  | -11.94%            | -57.69% |    -0.25 |       77 | 43.43%     | ok               |

## QQQ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 24.52%   | 63.14%             | -14.17% |     0.61 |       63 | 54.08%     | ok               |
|          25 | 16.07%   | 63.14%             | -12.88% |     0.47 |       61 | 48.09%     | ok               |
|          20 | 14.88%   | 63.14%             | -12.98% |     0.43 |       69 | 50.75%     | ok               |
|          30 | 8.23%    | 63.14%             | -14.20% |     0.29 |       66 | 46.09%     | ok               |
|          35 | -2.89%   | 63.14%             | -20.59% |    -0.01 |       72 | 42.26%     | ok               |

## RENDER-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 35.83%   | -60.54%            | -43.43% |     0.55 |       87 | 58.05%     | ok               |
|          15 | 33.24%   | -60.54%            | -44.59% |     0.53 |       82 | 61.49%     | ok               |
|          25 | 29.55%   | -60.54%            | -41.13% |     0.51 |       87 | 53.07%     | ok               |
|          30 | -14.13%  | -60.54%            | -44.65% |     0.13 |       92 | 47.13%     | ok               |
|          35 | -28.95%  | -60.54%            | -46.00% |    -0.09 |       86 | 40.80%     | ok               |

## RTX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 46.20%   | 73.59%             | -18.66% |     0.93 |       74 | 57.24%     | ok               |
|          25 | 41.20%   | 73.59%             | -18.59% |     0.86 |       62 | 54.58%     | ok               |
|          15 | 37.36%   | 73.59%             | -19.55% |     0.78 |       67 | 61.73%     | ok               |
|          30 | 30.49%   | 73.59%             | -16.99% |     0.7  |       64 | 52.08%     | ok               |
|          35 | 22.81%   | 73.59%             | -18.00% |     0.61 |       58 | 48.92%     | ok               |

## SBUX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | 1.51%    | 18.37%             | -23.55% |     0.13 |       55 | 40.43%     | ok               |
|          40 | -4.77%   | 18.37%             | -25.43% |    -0.03 |       60 | 32.45%     | ok               |
|          45 | -6.16%   | 18.37%             | -27.26% |    -0.08 |       66 | 27.45%     | ok               |
|          20 | -10.59%  | 18.37%             | -30.94% |    -0.11 |       58 | 42.43%     | ok               |
|          35 | -9.05%   | 18.37%             | -26.54% |    -0.11 |       58 | 35.61%     | ok               |

## SCHW Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -7.25%   | 21.60%             | -28.76% |    -0.08 |       67 | 48.59%     | ok               |
|          45 | -7.31%   | 21.60%             | -16.53% |    -0.16 |       62 | 30.78%     | ok               |
|          20 | -11.96%  | 21.60%             | -29.24% |    -0.2  |       75 | 51.08%     | ok               |
|          50 | -8.48%   | 21.60%             | -13.28% |    -0.25 |       54 | 27.79%     | ok               |
|          40 | -15.33%  | 21.60%             | -23.35% |    -0.38 |       72 | 35.44%     | ok               |

## SHIB-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | -24.49%  | -67.18%            | -44.56% |    -0.16 |       71 | 45.98%     | ok               |
|          40 | -23.73%  | -67.18%            | -41.14% |    -0.18 |       60 | 38.12%     | ok               |
|          15 | -31.87%  | -67.18%            | -45.04% |    -0.21 |       86 | 66.67%     | ok               |
|          25 | -32.69%  | -67.18%            | -45.29% |    -0.25 |       80 | 58.05%     | ok               |
|          20 | -34.22%  | -67.18%            | -47.68% |    -0.27 |       80 | 61.69%     | ok               |

## SHY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd    |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:-------|---------:|---------:|:-----------|:-----------------|
|          30 | -1.72%   | -0.31%             | -3.18% |    -0.57 |       48 | 37.10%     | ok               |
|          35 | -2.27%   | -0.31%             | -3.49% |    -0.78 |       52 | 35.44%     | ok               |
|          40 | -2.41%   | -0.31%             | -3.58% |    -0.83 |       54 | 33.94%     | ok               |
|          45 | -2.40%   | -0.31%             | -3.43% |    -0.88 |       54 | 28.62%     | ok               |
|          25 | -3.02%   | -0.31%             | -4.32% |    -1    |       62 | 39.60%     | ok               |

## SKY-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | -57.23%  | 1.58%              | -59.75% |    -0.93 |       78 | 36.78%     | ok               |
|          30 | -60.53%  | 1.58%              | -61.82% |    -0.97 |       85 | 44.44%     | ok               |
|          15 | -66.61%  | 1.58%              | -67.57% |    -1.02 |       75 | 53.83%     | ok               |
|          25 | -64.66%  | 1.58%              | -65.67% |    -1.06 |       78 | 47.70%     | ok               |
|          40 | -62.68%  | 1.58%              | -64.87% |    -1.17 |       66 | 33.33%     | ok               |

## SLB Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 5.35%    | 0.99%              | -28.43% |     0.21 |       50 | 35.11%     | ok               |
|          45 | 5.03%    | 0.99%              | -25.36% |     0.2  |       62 | 31.61%     | ok               |
|          50 | -9.45%   | 0.99%              | -30.44% |    -0.14 |       52 | 26.29%     | ok               |
|          35 | -22.18%  | 0.99%              | -45.96% |    -0.36 |       72 | 42.76%     | ok               |
|          25 | -35.65%  | 0.99%              | -55.80% |    -0.63 |       84 | 53.08%     | ok               |

## SLV Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 36.90%   | 82.75%             | -34.04% |     0.59 |       54 | 30.12%     | ok               |
|          45 | 25.27%   | 82.75%             | -31.75% |     0.47 |       65 | 31.61%     | ok               |
|          40 | 24.28%   | 82.75%             | -34.28% |     0.46 |       69 | 33.61%     | ok               |
|          15 | 14.08%   | 82.75%             | -47.98% |     0.35 |       73 | 48.75%     | ok               |
|          20 | 14.10%   | 82.75%             | -42.60% |     0.34 |       72 | 43.93%     | ok               |

## SMH Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 67.45%   | 150.62%            | -31.66% |     0.96 |       47 | 46.92%     | ok               |
|          25 | 52.26%   | 150.62%            | -33.57% |     0.83 |       44 | 45.42%     | ok               |
|          35 | 50.64%   | 150.62%            | -34.65% |     0.82 |       54 | 42.43%     | ok               |
|          30 | 48.12%   | 150.62%            | -34.29% |     0.78 |       48 | 44.09%     | ok               |
|          45 | 37.33%   | 150.62%            | -33.35% |     0.7  |       54 | 36.61%     | ok               |

## SNX-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 3.99%    | -72.45%            | -41.29% |     0.25 |       54 | 27.20%     | ok               |
|          40 | 1.46%    | -72.45%            | -37.52% |     0.19 |       44 | 22.41%     | ok               |
|          20 | -9.46%   | -72.45%            | -53.03% |     0.14 |       71 | 43.68%     | ok               |
|          30 | -9.86%   | -72.45%            | -50.74% |     0.1  |       62 | 33.52%     | ok               |
|          15 | -34.57%  | -72.45%            | -54.74% |    -0.16 |       77 | 48.28%     | ok               |

## SOL-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 30.62%   | -37.62%            | -39.83% |     0.52 |       62 | 40.42%     | ok               |
|          35 | 8.78%    | -37.62%            | -43.79% |     0.31 |       76 | 46.93%     | ok               |
|          45 | 6.55%    | -37.62%            | -46.91% |     0.27 |       60 | 35.06%     | ok               |
|          15 | -5.45%   | -37.62%            | -46.84% |     0.18 |       72 | 63.98%     | ok               |
|          50 | -4.03%   | -37.62%            | -46.56% |     0.11 |       60 | 29.12%     | ok               |

## SOXX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | 64.78%   | 133.93%            | -39.32% |     0.9  |       53 | 45.26%     | ok               |
|          35 | 61.07%   | 133.93%            | -38.76% |     0.88 |       56 | 40.77%     | ok               |
|          30 | 60.20%   | 133.93%            | -39.81% |     0.86 |       54 | 43.09%     | ok               |
|          20 | 50.23%   | 133.93%            | -39.19% |     0.75 |       59 | 46.26%     | ok               |
|          40 | 41.37%   | 133.93%            | -41.03% |     0.69 |       58 | 38.60%     | ok               |

## SPY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 10.69%   | 46.42%             | -14.25% |     0.4  |       59 | 53.24%     | ok               |
|          15 | 10.16%   | 46.42%             | -16.80% |     0.38 |       63 | 55.91%     | ok               |
|          25 | 5.72%    | 46.42%             | -14.25% |     0.25 |       59 | 52.25%     | ok               |
|          30 | -0.42%   | 46.42%             | -15.53% |     0.05 |       64 | 49.58%     | ok               |
|          35 | -1.38%   | 46.42%             | -15.58% |     0.01 |       62 | 46.42%     | ok               |

## SUSHI-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -7.44%   | -70.50%            | -34.75% |     0.06 |       54 | 16.67%     | ok               |
|          45 | -42.50%  | -70.50%            | -57.99% |    -0.51 |       56 | 21.46%     | ok               |
|          40 | -46.95%  | -70.50%            | -60.82% |    -0.54 |       59 | 27.97%     | ok               |
|          35 | -58.49%  | -70.50%            | -67.69% |    -0.74 |       80 | 32.95%     | ok               |
|          15 | -76.43%  | -70.50%            | -78.43% |    -1.02 |       89 | 49.62%     | ok               |

## T Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 68.34%   | 32.31%             | -15.08% |     1.12 |       73 | 65.56%     | ok               |
|          20 | 64.19%   | 32.31%             | -18.13% |     1.11 |       68 | 61.06%     | ok               |
|          25 | 62.32%   | 32.31%             | -17.66% |     1.09 |       68 | 58.90%     | ok               |
|          30 | 47.22%   | 32.31%             | -17.01% |     0.91 |       72 | 56.74%     | ok               |
|          35 | 31.17%   | 32.31%             | -14.49% |     0.69 |       78 | 52.41%     | ok               |

## TGT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -11.06%  | -2.43%             | -34.42% |    -0.16 |       60 | 37.60%     | ok               |
|          45 | -11.97%  | -2.43%             | -25.85% |    -0.23 |       48 | 28.62%     | ok               |
|          20 | -16.69%  | -2.43%             | -38.96% |    -0.25 |       88 | 45.42%     | ok               |
|          25 | -15.22%  | -2.43%             | -37.81% |    -0.25 |       70 | 40.77%     | ok               |
|          35 | -17.42%  | -2.43%             | -32.35% |    -0.35 |       60 | 33.94%     | ok               |

## TIA-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -31.60%  | -81.99%            | -66.82% |     0.05 |       96 | 59.20%     | ok               |
|          35 | -28.22%  | -81.99%            | -66.58% |    -0.08 |       74 | 36.40%     | ok               |
|          20 | -45.61%  | -81.99%            | -71.78% |    -0.15 |       91 | 53.83%     | ok               |
|          25 | -43.95%  | -81.99%            | -70.91% |    -0.15 |       94 | 48.66%     | ok               |
|          45 | -33.38%  | -81.99%            | -64.89% |    -0.32 |       62 | 20.69%     | ok               |

## TLT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -10.85%  | -14.43%            | -13.43% |    -1.16 |       36 | 17.97%     | ok               |
|          40 | -15.69%  | -14.43%            | -17.65% |    -1.36 |       54 | 25.46%     | ok               |
|          45 | -14.35%  | -14.43%            | -15.92% |    -1.46 |       46 | 20.97%     | ok               |
|          30 | -19.50%  | -14.43%            | -21.85% |    -1.46 |       68 | 33.78%     | ok               |
|          35 | -19.63%  | -14.43%            | -21.33% |    -1.63 |       66 | 29.12%     | ok               |

## TMO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 55.48%   | 12.36%             | -8.17%  |     1.15 |       48 | 35.11%     | ok               |
|          45 | 43.70%   | 12.36%             | -9.69%  |     0.92 |       54 | 39.93%     | ok               |
|          40 | 37.37%   | 12.36%             | -9.91%  |     0.8  |       59 | 44.93%     | ok               |
|          35 | 33.92%   | 12.36%             | -13.84% |     0.7  |       69 | 50.08%     | ok               |
|          20 | 32.50%   | 12.36%             | -22.89% |     0.63 |       78 | 61.06%     | ok               |

## TMUS Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -1.37%   | -6.47%             | -30.61% |     0.07 |       74 | 47.75%     | ok               |
|          15 | -7.18%   | -6.47%             | -38.92% |    -0.04 |       68 | 60.40%     | ok               |
|          25 | -10.76%  | -6.47%             | -37.09% |    -0.14 |       77 | 50.75%     | ok               |
|          50 | -7.84%   | -6.47%             | -32.38% |    -0.14 |       60 | 34.44%     | ok               |
|          20 | -12.53%  | -6.47%             | -37.62% |    -0.17 |       74 | 54.74%     | ok               |

## TRX-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 13.27%   | 24.89%             | -18.79% |     0.47 |       54 | 39.85%     | ok               |
|          35 | 6.62%    | 24.89%             | -21.77% |     0.27 |       66 | 48.08%     | ok               |
|          30 | 4.06%    | 24.89%             | -22.90% |     0.2  |       66 | 50.96%     | ok               |
|          20 | 4.13%    | 24.89%             | -25.45% |     0.2  |       61 | 57.85%     | ok               |
|          45 | 3.33%    | 24.89%             | -22.76% |     0.18 |       46 | 36.21%     | ok               |

## TSLA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 41.47%   | 101.09%            | -30.57% |     0.6  |       64 | 30.12%     | ok               |
|          40 | 13.71%   | 101.09%            | -50.11% |     0.34 |       63 | 35.61%     | ok               |
|          45 | -10.53%  | 101.09%            | -52.01% |     0.07 |       69 | 32.61%     | ok               |
|          35 | -20.51%  | 101.09%            | -60.12% |    -0.03 |       76 | 38.10%     | ok               |
|          30 | -37.10%  | 101.09%            | -59.64% |    -0.26 |       80 | 42.93%     | ok               |

## TXN Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 8.82%    | 44.64%             | -45.45% |     0.26 |       68 | 32.78%     | ok               |
|          35 | -11.15%  | 44.64%             | -43.28% |    -0.05 |       78 | 47.25%     | ok               |
|          40 | -12.70%  | 44.64%             | -45.67% |    -0.08 |       74 | 44.93%     | ok               |
|          20 | -16.69%  | 44.64%             | -38.49% |    -0.09 |       68 | 56.91%     | ok               |
|          45 | -13.83%  | 44.64%             | -46.24% |    -0.11 |       82 | 38.77%     | ok               |

## UNH Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 23.18%   | -27.85%            | -36.32% |     0.46 |       56 | 28.62%     | ok               |
|          30 | 21.42%   | -27.85%            | -26.31% |     0.43 |       77 | 48.42%     | ok               |
|          35 | 17.73%   | -27.85%            | -27.21% |     0.38 |       72 | 43.43%     | ok               |
|          20 | 17.56%   | -27.85%            | -26.96% |     0.38 |       80 | 57.74%     | ok               |
|          15 | 17.53%   | -27.85%            | -26.07% |     0.37 |       85 | 63.89%     | ok               |

## UNI-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 108.39%  | 8.31%              | -21.42% |     1.04 |       46 | 26.05%     | ok               |
|          45 | 85.00%   | 8.31%              | -30.17% |     0.87 |       54 | 33.33%     | ok               |
|          40 | 60.77%   | 8.31%              | -43.84% |     0.72 |       58 | 38.51%     | ok               |
|          35 | 41.01%   | 8.31%              | -50.48% |     0.58 |       68 | 44.06%     | ok               |
|          20 | -37.10%  | 8.31%              | -74.08% |    -0.06 |       92 | 59.58%     | ok               |

## UPS Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | -28.34%  | -34.82%            | -31.52% |    -0.53 |       62 | 36.44%     | ok               |
|          40 | -28.13%  | -34.82%            | -31.55% |    -0.53 |       58 | 30.95%     | ok               |
|          20 | -33.34%  | -34.82%            | -38.09% |    -0.6  |       84 | 49.92%     | ok               |
|          25 | -33.87%  | -34.82%            | -38.59% |    -0.64 |       76 | 46.59%     | ok               |
|          15 | -35.70%  | -34.82%            | -40.28% |    -0.65 |       86 | 53.74%     | ok               |

## USO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 5.79%    | 101.01%            | -33.44% |     0.22 |       48 | 25.79%     | ok               |
|          20 | 4.37%    | 101.01%            | -44.30% |     0.21 |       74 | 37.77%     | ok               |
|          15 | 1.03%    | 101.01%            | -45.22% |     0.17 |       68 | 41.43%     | ok               |
|          25 | -4.18%   | 101.01%            | -45.85% |     0.08 |       68 | 35.27%     | ok               |
|          50 | -3.42%   | 101.01%            | -29.54% |     0.07 |       52 | 24.13%     | ok               |

## VEA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 6.65%    | 37.26%             | -15.69% |     0.29 |       54 | 49.92%     | ok               |
|          20 | 0.45%    | 37.26%             | -16.74% |     0.07 |       59 | 47.25%     | ok               |
|          25 | -3.38%   | 37.26%             | -16.83% |    -0.08 |       57 | 45.26%     | ok               |
|          30 | -4.63%   | 37.26%             | -17.27% |    -0.14 |       62 | 42.60%     | ok               |
|          35 | -5.35%   | 37.26%             | -16.11% |    -0.18 |       52 | 40.77%     | ok               |

## VIXY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -57.58%  | -63.92%            | -69.78% |    -0.7  |       36 | 9.48%      | ok               |
|          15 | -78.19%  | -63.92%            | -89.47% |    -0.83 |       95 | 43.43%     | ok               |
|          45 | -66.67%  | -63.92%            | -75.03% |    -0.9  |       56 | 14.48%     | ok               |
|          30 | -78.82%  | -63.92%            | -88.17% |    -0.96 |       94 | 32.45%     | ok               |
|          20 | -82.56%  | -63.92%            | -90.58% |    -1.02 |       91 | 39.43%     | ok               |

## VNQ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -10.44%  | 8.04%              | -19.07% |    -0.47 |       62 | 28.45%     | ok               |
|          25 | -13.31%  | 8.04%              | -22.34% |    -0.51 |       69 | 42.60%     | ok               |
|          50 | -11.33%  | 8.04%              | -17.13% |    -0.54 |       54 | 25.12%     | ok               |
|          30 | -15.25%  | 8.04%              | -24.92% |    -0.61 |       73 | 39.93%     | ok               |
|          40 | -15.18%  | 8.04%              | -24.84% |    -0.67 |       80 | 33.94%     | ok               |

## VTI Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 11.55%   | 44.93%             | -13.96% |     0.43 |       62 | 53.74%     | ok               |
|          15 | 6.96%    | 44.93%             | -15.70% |     0.28 |       59 | 56.07%     | ok               |
|          25 | -0.35%   | 44.93%             | -15.00% |     0.05 |       58 | 51.58%     | ok               |
|          30 | -7.83%   | 44.93%             | -17.64% |    -0.23 |       68 | 49.58%     | ok               |
|          40 | -8.93%   | 44.93%             | -19.77% |    -0.3  |       72 | 42.10%     | ok               |

## VWO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -10.73%  | 34.02%             | -22.18% |    -0.41 |       56 | 28.45%     | ok               |
|          15 | -13.52%  | 34.02%             | -23.73% |    -0.44 |       74 | 46.92%     | ok               |
|          45 | -11.92%  | 34.02%             | -23.75% |    -0.46 |       58 | 31.11%     | ok               |
|          40 | -12.37%  | 34.02%             | -23.57% |    -0.47 |       68 | 33.94%     | ok               |
|          20 | -14.90%  | 34.02%             | -25.88% |    -0.5  |       71 | 44.59%     | ok               |

## VZ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -3.10%   | 9.87%              | -12.96% |    -0.04 |       56 | 28.62%     | ok               |
|          20 | -20.64%  | 9.87%              | -35.02% |    -0.4  |       78 | 50.92%     | ok               |
|          25 | -17.40%  | 9.87%              | -23.26% |    -0.44 |       81 | 45.92%     | ok               |
|          45 | -17.05%  | 9.87%              | -23.23% |    -0.51 |       70 | 32.61%     | ok               |
|          35 | -17.66%  | 9.87%              | -24.31% |    -0.51 |       64 | 38.27%     | ok               |

## WFC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -6.21%   | 31.37%             | -18.29% |    -0.13 |       58 | 32.61%     | ok               |
|          35 | -9.50%   | 31.37%             | -21.57% |    -0.14 |       77 | 44.26%     | ok               |
|          20 | -20.24%  | 31.37%             | -29.87% |    -0.31 |       77 | 52.75%     | ok               |
|          30 | -18.93%  | 31.37%             | -28.90% |    -0.32 |       80 | 47.42%     | ok               |
|          40 | -15.09%  | 31.37%             | -23.94% |    -0.37 |       72 | 40.93%     | ok               |

## WIF-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 21.62%   | -76.98%            | -40.67% |     0.45 |       69 | 44.44%     | ok               |
|          25 | 9.21%    | -76.98%            | -44.74% |     0.35 |       67 | 40.42%     | ok               |
|          15 | -4.96%   | -76.98%            | -46.21% |     0.26 |       79 | 47.70%     | ok               |
|          50 | -7.18%   | -76.98%            | -35.47% |     0.05 |       34 | 13.03%     | ok               |
|          30 | -31.88%  | -76.98%            | -52.76% |    -0.08 |       68 | 37.55%     | ok               |

## WMT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 35.91%   | 72.34%             | -12.18% |     1.09 |       36 | 37.27%     | ok               |
|          45 | 34.77%   | 72.34%             | -14.14% |     1.02 |       42 | 39.60%     | ok               |
|          35 | 24.94%   | 72.34%             | -18.25% |     0.73 |       58 | 45.92%     | ok               |
|          40 | 23.33%   | 72.34%             | -18.53% |     0.71 |       50 | 41.26%     | ok               |
|          15 | 6.60%    | 72.34%             | -26.24% |     0.24 |       82 | 59.90%     | ok               |

## XBI Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 10.79%   | 60.31%             | -16.08% |     0.34 |       54 | 34.44%     | ok               |
|          45 | 6.58%    | 60.31%             | -15.46% |     0.25 |       52 | 31.95%     | ok               |
|          35 | 0.55%    | 60.31%             | -17.66% |     0.1  |       62 | 37.10%     | ok               |
|          30 | -1.55%   | 60.31%             | -17.66% |     0.05 |       64 | 38.60%     | ok               |
|          50 | -2.42%   | 60.31%             | -15.57% |     0.01 |       52 | 28.95%     | ok               |

## XLB Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -3.99%   | 7.76%              | -15.73% |    -0.12 |       40 | 22.13%     | ok               |
|          40 | -4.87%   | 7.76%              | -17.46% |    -0.14 |       56 | 26.29%     | ok               |
|          45 | -7.42%   | 7.76%              | -17.30% |    -0.26 |       44 | 23.79%     | ok               |
|          35 | -8.10%   | 7.76%              | -20.65% |    -0.26 |       56 | 29.78%     | ok               |
|          25 | -12.35%  | 7.76%              | -22.62% |    -0.42 |       64 | 35.94%     | ok               |

## XLC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 12.62%   | 35.70%             | -12.33% |     0.47 |       61 | 50.25%     | ok               |
|          25 | 12.06%   | 35.70%             | -12.31% |     0.45 |       60 | 52.41%     | ok               |
|          50 | 7.23%    | 35.70%             | -11.12% |     0.38 |       64 | 38.44%     | ok               |
|          40 | 7.80%    | 35.70%             | -13.38% |     0.34 |       62 | 43.93%     | ok               |
|          35 | 7.08%    | 35.70%             | -13.38% |     0.31 |       60 | 47.75%     | ok               |

## XLE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 1.15%    | 43.16%             | -25.98% |     0.11 |       56 | 36.44%     | ok               |
|          35 | -2.01%   | 43.16%             | -26.89% |     0.03 |       65 | 42.93%     | ok               |
|          45 | -2.19%   | 43.16%             | -28.46% |     0.02 |       60 | 38.60%     | ok               |
|          30 | -3.61%   | 43.16%             | -30.31% |    -0    |       69 | 45.09%     | ok               |
|          25 | -7.54%   | 43.16%             | -33.14% |    -0.1  |       80 | 48.09%     | ok               |

## XLF Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -2.50%   | 29.97%             | -18.63% |    -0.02 |       74 | 51.75%     | ok               |
|          15 | -4.02%   | 29.97%             | -20.19% |    -0.07 |       78 | 54.58%     | ok               |
|          25 | -9.30%   | 29.97%             | -23.22% |    -0.28 |       81 | 48.59%     | ok               |
|          30 | -9.89%   | 29.97%             | -23.61% |    -0.31 |       82 | 46.59%     | ok               |
|          35 | -16.91%  | 29.97%             | -24.48% |    -0.66 |       72 | 42.93%     | ok               |

## XLI Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 5.22%    | 34.76%             | -11.40% |     0.23 |       86 | 51.41%     | ok               |
|          20 | 1.42%    | 34.76%             | -12.74% |     0.11 |       75 | 46.42%     | ok               |
|          50 | -4.76%   | 34.76%             | -14.94% |    -0.18 |       60 | 31.78%     | ok               |
|          45 | -5.38%   | 34.76%             | -16.29% |    -0.19 |       70 | 34.28%     | ok               |
|          25 | -8.78%   | 34.76%             | -17.03% |    -0.29 |       78 | 44.43%     | ok               |

## XLK Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 73.83%   | 82.88%             | -14.75% |     1.2  |       45 | 51.91%     | ok               |
|          20 | 69.51%   | 82.88%             | -14.75% |     1.19 |       46 | 49.75%     | ok               |
|          25 | 63.57%   | 82.88%             | -14.75% |     1.15 |       42 | 47.75%     | ok               |
|          30 | 53.78%   | 82.88%             | -14.75% |     1.05 |       42 | 46.42%     | ok               |
|          35 | 34.75%   | 82.88%             | -13.61% |     0.78 |       56 | 43.59%     | ok               |

## XLM-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | 7.33%    | -37.69%            | -49.14% |     0.3  |       70 | 49.81%     | ok               |
|          40 | 1.55%    | -37.69%            | -47.28% |     0.22 |       52 | 36.97%     | ok               |
|          30 | -2.08%   | -37.69%            | -54.66% |     0.2  |       68 | 47.70%     | ok               |
|          50 | 0.51%    | -37.69%            | -48.81% |     0.19 |       42 | 26.63%     | ok               |
|          45 | -0.66%   | -37.69%            | -51.28% |     0.18 |       54 | 31.61%     | ok               |

## XLP Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 7.90%    | 7.76%              | -5.66%  |     0.52 |       54 | 29.28%     | ok               |
|          50 | 5.50%    | 7.76%              | -6.08%  |     0.38 |       60 | 27.12%     | ok               |
|          40 | 5.73%    | 7.76%              | -7.77%  |     0.37 |       70 | 33.44%     | ok               |
|          35 | 4.80%    | 7.76%              | -9.73%  |     0.31 |       66 | 36.44%     | ok               |
|          30 | 0.78%    | 7.76%              | -11.16% |     0.08 |       67 | 38.10%     | ok               |

## XLU Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 4.02%    | 14.92%             | -14.03% |     0.23 |       54 | 30.45%     | ok               |
|          45 | 2.87%    | 14.92%             | -14.97% |     0.18 |       58 | 31.61%     | ok               |
|          40 | -0.13%   | 14.92%             | -16.41% |     0.04 |       64 | 33.61%     | ok               |
|          35 | -2.78%   | 14.92%             | -19.71% |    -0.08 |       64 | 36.27%     | ok               |
|          30 | -6.99%   | 14.92%             | -20.40% |    -0.26 |       69 | 39.77%     | ok               |

## XLV Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -22.02%  | 16.01%             | -22.40% |    -1.05 |       76 | 38.60%     | ok               |
|          30 | -22.38%  | 16.01%             | -22.75% |    -1.08 |       76 | 36.94%     | ok               |
|          15 | -25.24%  | 16.01%             | -25.35% |    -1.18 |       83 | 42.76%     | ok               |
|          20 | -25.08%  | 16.01%             | -25.19% |    -1.2  |       79 | 40.27%     | ok               |
|          35 | -26.25%  | 16.01%             | -26.58% |    -1.37 |       70 | 33.94%     | ok               |

## XLY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -0.70%   | 25.89%             | -15.77% |     0.06 |       76 | 54.24%     | ok               |
|          30 | -4.15%   | 25.89%             | -18.35% |    -0.06 |       75 | 47.59%     | ok               |
|          20 | -5.95%   | 25.89%             | -19.25% |    -0.1  |       72 | 50.92%     | ok               |
|          25 | -8.05%   | 25.89%             | -19.98% |    -0.17 |       69 | 49.42%     | ok               |
|          50 | -6.34%   | 25.89%             | -15.82% |    -0.22 |       62 | 32.11%     | ok               |

## XOM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | 2.73%    | 47.71%             | -19.90% |     0.15 |       55 | 34.94%     | ok               |
|          50 | 1.92%    | 47.71%             | -21.35% |     0.13 |       38 | 27.12%     | ok               |
|          30 | 1.71%    | 47.71%             | -20.29% |     0.12 |       55 | 34.28%     | ok               |
|          20 | -3.12%   | 47.71%             | -25.56% |    -0.01 |       62 | 37.27%     | ok               |
|          45 | -3.17%   | 47.71%             | -23.33% |    -0.02 |       42 | 28.29%     | ok               |

## XRP-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 21.83%   | -41.87%            | -31.38% |     0.44 |       72 | 42.91%     | ok               |
|          40 | 6.45%    | -41.87%            | -33.91% |     0.27 |       64 | 36.40%     | ok               |
|          45 | -4.00%   | -41.87%            | -37.18% |     0.14 |       60 | 31.99%     | ok               |
|          30 | -8.94%   | -41.87%            | -31.82% |     0.1  |       67 | 47.89%     | ok               |
|          50 | -8.08%   | -41.87%            | -39.26% |     0.06 |       58 | 24.33%     | ok               |

## YFI-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -48.89%  | -63.65%            | -48.54% |    -0.85 |       56 | 27.01%     | ok               |
|          35 | -57.45%  | -63.65%            | -57.16% |    -1.05 |       62 | 33.52%     | ok               |
|          45 | -48.94%  | -63.65%            | -48.94% |    -1.1  |       68 | 21.65%     | ok               |
|          30 | -64.81%  | -63.65%            | -64.57% |    -1.27 |       76 | 37.16%     | ok               |
|          50 | -50.86%  | -63.65%            | -50.86% |    -1.3  |       52 | 16.28%     | ok               |

## ZEC-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 184.14%  | 2701.11%           | -30.64% |     1.03 |       46 | 32.57%     | ok               |
|          35 | 146.53%  | 2701.11%           | -50.84% |     0.92 |       52 | 38.12%     | ok               |
|          30 | 126.83%  | 2701.11%           | -56.50% |     0.86 |       59 | 41.38%     | ok               |
|          25 | 117.64%  | 2701.11%           | -58.07% |     0.83 |       57 | 43.87%     | ok               |
|          40 | 108.95%  | 2701.11%           | -54.22% |     0.81 |       54 | 36.02%     | ok               |
