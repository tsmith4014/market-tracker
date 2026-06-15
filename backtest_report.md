# Market Tracker Backtest Report

_Generated: 2026-06-15T01:41:42+00:00_

## Data Sources

- Crypto: Kraken -> Coinbase -> CoinGecko OHLC -> CoinPaprika fallback chain.
- Stocks / ETFs / indices: Stooq -> Yahoo Finance fallback chain.
- Data rows are generated from real market APIs. Mock OHLCV rows are not generated.

## Data Freshness

- Rows: **92,391**
- Symbols: **161**
- Date range: **2024-01-22** to **2026-06-15**

## Latest Signals

| symbol     | date                |         close |   composite_score | signal   | data_source   |
|:-----------|:--------------------|--------------:|------------------:|:---------|:--------------|
| AMAT       | 2026-06-12 00:00:00 |   567.25      |         71.75     | LONG     | Yahoo Finance |
| ATOM-USD   | 2026-06-15 00:00:00 |     1.9869    |         38.4167   | LONG     | Kraken API    |
| BAC        | 2026-06-12 00:00:00 |    56.02      |         53.25     | LONG     | Yahoo Finance |
| C          | 2026-06-12 00:00:00 |   139.83      |         71.25     | LONG     | Yahoo Finance |
| CRV-USD    | 2026-06-15 00:00:00 |     0.24267   |         41.8333   | LONG     | Kraken API    |
| CSCO       | 2026-06-12 00:00:00 |   121.1       |         46.5833   | LONG     | Yahoo Finance |
| DE         | 2026-06-12 00:00:00 |   577.48      |         75        | LONG     | Yahoo Finance |
| DXY-INDEX  | 2026-06-14 00:00:00 |    99.57      |         75.5376   | LONG     | Yahoo Finance |
| GE         | 2026-06-12 00:00:00 |   335.3       |         63.4167   | LONG     | Yahoo Finance |
| GS         | 2026-06-12 00:00:00 |  1062.75      |         47.25     | LONG     | Yahoo Finance |
| IBM        | 2026-06-12 00:00:00 |   272.24      |         37.5833   | LONG     | Yahoo Finance |
| ITA        | 2026-06-12 00:00:00 |   233.79      |         60.0833   | LONG     | Yahoo Finance |
| JPM        | 2026-06-12 00:00:00 |   320.72      |         56.5833   | LONG     | Yahoo Finance |
| LLY        | 2026-06-12 00:00:00 |  1133         |         69.4167   | LONG     | Yahoo Finance |
| LRCX       | 2026-06-12 00:00:00 |   366.81      |         72.9167   | LONG     | Yahoo Finance |
| MRK        | 2026-06-12 00:00:00 |   119.05      |         55.25     | LONG     | Yahoo Finance |
| MS         | 2026-06-12 00:00:00 |   214.04      |         45.0833   | LONG     | Yahoo Finance |
| MU         | 2026-06-12 00:00:00 |   981.61      |         47.75     | LONG     | Yahoo Finance |
| PG         | 2026-06-12 00:00:00 |   149.61      |         60.3333   | LONG     | Yahoo Finance |
| PM         | 2026-06-12 00:00:00 |   184.3       |         42.0833   | LONG     | Yahoo Finance |
| QQQ        | 2026-06-12 00:00:00 |   721.34      |         48.25     | LONG     | Yahoo Finance |
| RTX        | 2026-06-12 00:00:00 |   183.53      |         54.8333   | LONG     | Yahoo Finance |
| SBUX       | 2026-06-12 00:00:00 |   103.04      |         44.25     | LONG     | Yahoo Finance |
| UNH        | 2026-06-12 00:00:00 |   408.52      |         78.5833   | LONG     | Yahoo Finance |
| UPS        | 2026-06-12 00:00:00 |   108.1       |         76.9167   | LONG     | Yahoo Finance |
| VZ         | 2026-06-12 00:00:00 |    48.11      |         48.75     | LONG     | Yahoo Finance |
| WFC        | 2026-06-12 00:00:00 |    83.73      |         62.25     | LONG     | Yahoo Finance |
| XLK        | 2026-06-12 00:00:00 |   184.8       |         46.5833   | LONG     | Yahoo Finance |
| AAPL       | 2026-06-12 00:00:00 |   291.13      |         -2.08333  | NEUTRAL  | Yahoo Finance |
| AAVE-USD   | 2026-06-15 00:00:00 |    68         |        -19        | NEUTRAL  | Kraken API    |
| ABBV       | 2026-06-12 00:00:00 |   227.73      |         51        | NEUTRAL  | Yahoo Finance |
| ADA-USD    | 2026-06-15 00:00:00 |     0.180704  |        -27.8333   | NEUTRAL  | Kraken API    |
| ADBE       | 2026-06-12 00:00:00 |   204.02      |        -70.75     | NEUTRAL  | Yahoo Finance |
| AGG        | 2026-06-12 00:00:00 |    98.76      |         -2.25     | NEUTRAL  | Yahoo Finance |
| AMD        | 2026-06-12 00:00:00 |   511.57      |         41        | NEUTRAL  | Yahoo Finance |
| AMGN       | 2026-06-12 00:00:00 |   355.2       |         62.3333   | NEUTRAL  | Yahoo Finance |
| AMZN       | 2026-06-12 00:00:00 |   238.55      |        -16.8333   | NEUTRAL  | Yahoo Finance |
| ARB-USD    | 2026-06-15 00:00:00 |     0.0852    |        -22.3333   | NEUTRAL  | Kraken API    |
| ARKK       | 2026-06-12 00:00:00 |    75.65      |        -35.75     | NEUTRAL  | Yahoo Finance |
| AVGO       | 2026-06-12 00:00:00 |   382.07      |        -44.75     | NEUTRAL  | Yahoo Finance |
| BA         | 2026-06-12 00:00:00 |   219.05      |        -10.9167   | NEUTRAL  | Yahoo Finance |
| BND        | 2026-06-12 00:00:00 |    73.24      |         -2.25     | NEUTRAL  | Yahoo Finance |
| BONK-USD   | 2026-06-15 00:00:00 |     4.602e-06 |        -25.6667   | NEUTRAL  | Kraken API    |
| BTC-USD    | 2026-06-15 00:00:00 | 65340.6       |        -13.5      | NEUTRAL  | Kraken API    |
| CAT        | 2026-06-12 00:00:00 |   910.57      |         48.3333   | NEUTRAL  | Yahoo Finance |
| CL         | 2026-06-12 00:00:00 |    89.45      |         32.0833   | NEUTRAL  | Yahoo Finance |
| CMCSA      | 2026-06-12 00:00:00 |    24.5       |        -14.4167   | NEUTRAL  | Yahoo Finance |
| COMP-USD   | 2026-06-15 00:00:00 |    17.91      |         -6        | NEUTRAL  | Kraken API    |
| COP        | 2026-06-12 00:00:00 |   116.98      |        -10.1667   | NEUTRAL  | Yahoo Finance |
| COST       | 2026-06-12 00:00:00 |   982.35      |         -9.83333  | NEUTRAL  | Yahoo Finance |
| CRM        | 2026-06-12 00:00:00 |   165.89      |        -66.5      | NEUTRAL  | Yahoo Finance |
| CVX        | 2026-06-12 00:00:00 |   187.22      |         -9.75     | NEUTRAL  | Yahoo Finance |
| DASH-USD   | 2026-06-15 00:00:00 |    37.998     |        -19.5      | NEUTRAL  | Kraken API    |
| DBC        | 2026-06-12 00:00:00 |    28.55      |        -17.4167   | NEUTRAL  | Yahoo Finance |
| DIA        | 2026-06-12 00:00:00 |   513.06      |         34.5      | NEUTRAL  | Yahoo Finance |
| DOGE-USD   | 2026-06-15 00:00:00 |     0.0884009 |        -27.8333   | NEUTRAL  | Kraken API    |
| EEM        | 2026-06-12 00:00:00 |    67.88      |         37        | NEUTRAL  | Yahoo Finance |
| EFA        | 2026-06-12 00:00:00 |   105.02      |         14        | NEUTRAL  | Yahoo Finance |
| EOG        | 2026-06-12 00:00:00 |   136.65      |         -3.83333  | NEUTRAL  | Yahoo Finance |
| ETC-USD    | 2026-06-15 00:00:00 |     7.166     |        -19        | NEUTRAL  | Kraken API    |
| EWJ        | 2026-06-12 00:00:00 |    92.71      |         21        | NEUTRAL  | Yahoo Finance |
| FCX        | 2026-06-12 00:00:00 |    68.41      |         44.6667   | NEUTRAL  | Yahoo Finance |
| GOOGL      | 2026-06-12 00:00:00 |   359.68      |        -13.5833   | NEUTRAL  | Yahoo Finance |
| HBAR-USD   | 2026-06-15 00:00:00 |     0.08151   |        -60.9167   | NEUTRAL  | Kraken API    |
| HD         | 2026-06-12 00:00:00 |   328.39      |         26.8333   | NEUTRAL  | Yahoo Finance |
| HON        | 2026-06-12 00:00:00 |   220.31      |         -2.5      | NEUTRAL  | Yahoo Finance |
| HYG        | 2026-06-12 00:00:00 |    79.94      |          6.41667  | NEUTRAL  | Yahoo Finance |
| ICP-USD    | 2026-06-15 00:00:00 |     2.491     |        -51.9167   | NEUTRAL  | Kraken API    |
| IEF        | 2026-06-12 00:00:00 |    94.18      |         -4.5      | NEUTRAL  | Yahoo Finance |
| IEMG       | 2026-06-12 00:00:00 |    82.57      |         37        | NEUTRAL  | Yahoo Finance |
| INJ-USD    | 2026-06-15 00:00:00 |     5.099     |        -19.9167   | NEUTRAL  | Kraken API    |
| INTC       | 2026-06-12 00:00:00 |   124.57      |         43        | NEUTRAL  | Yahoo Finance |
| IWM        | 2026-06-12 00:00:00 |   292.95      |         41.5      | NEUTRAL  | Yahoo Finance |
| JNJ        | 2026-06-12 00:00:00 |   240.87      |         66.5      | NEUTRAL  | Yahoo Finance |
| KO         | 2026-06-12 00:00:00 |    82.62      |         55.8333   | NEUTRAL  | Yahoo Finance |
| LIN        | 2026-06-12 00:00:00 |   523.57      |         58.3333   | NEUTRAL  | Yahoo Finance |
| LINK-USD   | 2026-06-15 00:00:00 |     8.12161   |        -19        | NEUTRAL  | Kraken API    |
| LTC-USD    | 2026-06-15 00:00:00 |    45.08      |        -26        | NEUTRAL  | Kraken API    |
| MCD        | 2026-06-12 00:00:00 |   284.81      |         -4.83333  | NEUTRAL  | Yahoo Finance |
| META       | 2026-06-12 00:00:00 |   566.98      |        -67        | NEUTRAL  | Yahoo Finance |
| MPC        | 2026-06-12 00:00:00 |   263.58      |         47.8333   | NEUTRAL  | Yahoo Finance |
| NEAR-USD   | 2026-06-15 00:00:00 |     2.231     |         30.4167   | NEUTRAL  | Kraken API    |
| NEM        | 2026-06-12 00:00:00 |   100.23      |        -27.3333   | NEUTRAL  | Yahoo Finance |
| NKE        | 2026-06-12 00:00:00 |    44.93      |          4.75     | NEUTRAL  | Yahoo Finance |
| NVDA       | 2026-06-12 00:00:00 |   205.19      |        -42.8333   | NEUTRAL  | Yahoo Finance |
| OP-USD     | 2026-06-15 00:00:00 |     0.1101    |         -4.83333  | NEUTRAL  | Kraken API    |
| OXY        | 2026-06-12 00:00:00 |    56.54      |        -24.8333   | NEUTRAL  | Yahoo Finance |
| PEP        | 2026-06-12 00:00:00 |   144.27      |        -18.25     | NEUTRAL  | Yahoo Finance |
| PEPE-USD   | 2026-06-15 00:00:00 |     2.882e-06 |        -25.6667   | NEUTRAL  | Kraken API    |
| PFE        | 2026-06-12 00:00:00 |    26.21      |         62.25     | NEUTRAL  | Yahoo Finance |
| QCOM       | 2026-06-12 00:00:00 |   211.72      |         -0.333333 | NEUTRAL  | Yahoo Finance |
| SCHW       | 2026-06-12 00:00:00 |    91.1       |         11.6667   | NEUTRAL  | Yahoo Finance |
| SHIB-USD   | 2026-06-15 00:00:00 |     4.995e-06 |        -18.8333   | NEUTRAL  | Kraken API    |
| SHY        | 2026-06-12 00:00:00 |    82.07      |        -37.75     | NEUTRAL  | Yahoo Finance |
| SLB        | 2026-06-12 00:00:00 |    56.18      |         19.6667   | NEUTRAL  | Yahoo Finance |
| SMH        | 2026-06-12 00:00:00 |   619.96      |         37        | NEUTRAL  | Yahoo Finance |
| SOXX       | 2026-06-12 00:00:00 |   596.25      |         40.5      | NEUTRAL  | Yahoo Finance |
| SPY        | 2026-06-12 00:00:00 |   741.75      |         22.0833   | NEUTRAL  | Yahoo Finance |
| SUSHI-USD  | 2026-06-15 00:00:00 |     0.1793    |        -49.9167   | NEUTRAL  | Kraken API    |
| TGT        | 2026-06-12 00:00:00 |   135.23      |         63.3333   | NEUTRAL  | Yahoo Finance |
| TLT        | 2026-06-12 00:00:00 |    85.77      |         22.5      | NEUTRAL  | Yahoo Finance |
| TMO        | 2026-06-12 00:00:00 |   469.34      |         -1.58333  | NEUTRAL  | Yahoo Finance |
| TMUS       | 2026-06-12 00:00:00 |   189.1       |         -9.25     | NEUTRAL  | Yahoo Finance |
| TRX-USD    | 2026-06-15 00:00:00 |     0.320029  |        -14.9167   | NEUTRAL  | Kraken API    |
| TSLA       | 2026-06-12 00:00:00 |   406.43      |        -11.5833   | NEUTRAL  | Yahoo Finance |
| TXN        | 2026-06-12 00:00:00 |   301.12      |         25.1667   | NEUTRAL  | Yahoo Finance |
| UNI-USD    | 2026-06-15 00:00:00 |     2.5677    |        -22.3333   | NEUTRAL  | Kraken API    |
| USO        | 2026-06-12 00:00:00 |   125.43      |        -27.3333   | NEUTRAL  | Yahoo Finance |
| VEA        | 2026-06-12 00:00:00 |    71.55      |         39        | NEUTRAL  | Yahoo Finance |
| VIXY       | 2026-06-12 00:00:00 |    23.29      |        -17.4167   | NEUTRAL  | Yahoo Finance |
| VNQ        | 2026-06-12 00:00:00 |    98.51      |         60.3333   | NEUTRAL  | Yahoo Finance |
| VTI        | 2026-06-12 00:00:00 |   366.36      |         22.0833   | NEUTRAL  | Yahoo Finance |
| VWO        | 2026-06-12 00:00:00 |    59.55      |         15.3333   | NEUTRAL  | Yahoo Finance |
| WMT        | 2026-06-12 00:00:00 |   121.04      |         26.1667   | NEUTRAL  | Yahoo Finance |
| XBI        | 2026-06-12 00:00:00 |   133.79      |         56.1667   | NEUTRAL  | Yahoo Finance |
| XLB        | 2026-06-12 00:00:00 |    52.18      |         58.6667   | NEUTRAL  | Yahoo Finance |
| XLC        | 2026-06-12 00:00:00 |   111.65      |        -59.5833   | NEUTRAL  | Yahoo Finance |
| XLE        | 2026-06-12 00:00:00 |    57.55      |        -26.8333   | NEUTRAL  | Yahoo Finance |
| XLF        | 2026-06-12 00:00:00 |    53.34      |         58.3333   | NEUTRAL  | Yahoo Finance |
| XLI        | 2026-06-12 00:00:00 |   176.18      |         55.6667   | NEUTRAL  | Yahoo Finance |
| XLM-USD    | 2026-06-15 00:00:00 |     0.187865  |        -23.6667   | NEUTRAL  | Kraken API    |
| XLP        | 2026-06-12 00:00:00 |    85.82      |         62        | NEUTRAL  | Yahoo Finance |
| XLU        | 2026-06-12 00:00:00 |    44.53      |         10.5833   | NEUTRAL  | Yahoo Finance |
| XLV        | 2026-06-12 00:00:00 |   153.81      |         48.8333   | NEUTRAL  | Yahoo Finance |
| XLY        | 2026-06-12 00:00:00 |   116.6       |        -40.8333   | NEUTRAL  | Yahoo Finance |
| XOM        | 2026-06-12 00:00:00 |   147.01      |        -23.0833   | NEUTRAL  | Yahoo Finance |
| XRP-USD    | 2026-06-15 00:00:00 |     1.178     |        -28        | NEUTRAL  | Kraken API    |
| YFI-USD    | 2026-06-15 00:00:00 |  1911.5       |        -25.6667   | NEUTRAL  | Kraken API    |
| ZEC-USD    | 2026-06-15 00:00:00 |   470.34      |        -34.0833   | NEUTRAL  | Kraken API    |
| ALGO-USD   | 2026-06-15 00:00:00 |     0.09191   |        -51.3333   | SHORT    | Kraken API    |
| APT-USD    | 2026-06-15 00:00:00 |     0.6765    |        -53.6667   | SHORT    | Kraken API    |
| AVAX-USD   | 2026-06-15 00:00:00 |     6.702     |        -49.6667   | SHORT    | Kraken API    |
| BCH-USD    | 2026-06-15 00:00:00 |   210.11      |        -44.3333   | SHORT    | Kraken API    |
| BITO       | 2026-06-12 00:00:00 |     8.65      |        -59.4167   | SHORT    | Yahoo Finance |
| BLK        | 2026-06-12 00:00:00 |  1032         |        -40.0833   | SHORT    | Yahoo Finance |
| DIS        | 2026-06-12 00:00:00 |   100.04      |        -52.0833   | SHORT    | Yahoo Finance |
| DOT-USD    | 2026-06-15 00:00:00 |     0.9863    |        -31.3333   | SHORT    | Kraken API    |
| ETH-USD    | 2026-06-15 00:00:00 |  1709.69      |        -39.6667   | SHORT    | Kraken API    |
| FET-USD    | 2026-06-15 00:00:00 |     0.2094    |        -39.25     | SHORT    | Kraken API    |
| FIL-USD    | 2026-06-15 00:00:00 |     0.785     |        -37        | SHORT    | Kraken API    |
| FXI        | 2026-06-12 00:00:00 |    35.29      |        -42.0833   | SHORT    | Yahoo Finance |
| GDX        | 2026-06-12 00:00:00 |    80.03      |        -53.5833   | SHORT    | Yahoo Finance |
| GDXJ       | 2026-06-12 00:00:00 |   104.26      |        -57.5833   | SHORT    | Yahoo Finance |
| GLD        | 2026-06-12 00:00:00 |   386.54      |        -54.0833   | SHORT    | Yahoo Finance |
| GRT-USD    | 2026-06-15 00:00:00 |     0.02002   |        -49.6667   | SHORT    | Kraken API    |
| IBIT       | 2026-06-12 00:00:00 |    36.04      |        -59.4167   | SHORT    | Yahoo Finance |
| INTU       | 2026-06-12 00:00:00 |   276.73      |        -56.75     | SHORT    | Yahoo Finance |
| LDO-USD    | 2026-06-15 00:00:00 |     0.268     |        -36.3333   | SHORT    | Kraken API    |
| MSFT       | 2026-06-12 00:00:00 |   390.74      |        -51.25     | SHORT    | Yahoo Finance |
| NFLX       | 2026-06-12 00:00:00 |    80.34      |        -61.0833   | SHORT    | Yahoo Finance |
| NOW        | 2026-06-12 00:00:00 |   102.15      |        -47.9167   | SHORT    | Yahoo Finance |
| ORCL       | 2026-06-12 00:00:00 |   184.13      |        -48.8333   | SHORT    | Yahoo Finance |
| POL-USD    | 2026-06-15 00:00:00 |     0.07657   |        -51.3333   | SHORT    | Kraken API    |
| RENDER-USD | 2026-06-15 00:00:00 |     1.799     |        -32.3333   | SHORT    | Kraken API    |
| SKY-USD    | 2026-06-15 00:00:00 |     0.05726   |        -31        | SHORT    | Kraken API    |
| SLV        | 2026-06-12 00:00:00 |    61.29      |        -40.5833   | SHORT    | Yahoo Finance |
| SNX-USD    | 2026-06-15 00:00:00 |     0.2474    |        -33        | SHORT    | Kraken API    |
| SOL-USD    | 2026-06-15 00:00:00 |    70.66      |        -27.8333   | SHORT    | Kraken API    |
| T          | 2026-06-12 00:00:00 |    23.58      |        -53.5833   | SHORT    | Yahoo Finance |
| TIA-USD    | 2026-06-15 00:00:00 |     0.3485    |        -37        | SHORT    | Kraken API    |
| WIF-USD    | 2026-06-15 00:00:00 |     0.164     |        -37        | SHORT    | Kraken API    |

## Edge Summary

- Symbols with trades: **160** of 160
- Beat buy-and-hold: **33.75%** of traded symbols
- Positive return: **36.25%** of traded symbols
- Median strategy return: **-9.24%** (benchmark **17.98%**)
- Median excess vs benchmark: **-31.36%**
- Median Sharpe: **-0.08**
- Median exposure: **44.48%**

> Edge is real only if both _beat buy-and-hold_ and _median excess_ are convincingly positive across many symbols. Treat a single high-return symbol as noise.

## Portfolio Backtest

Actual capital-allocation books (not per-symbol averages). Benchmarks: `equal_weight_buyhold` (whole tracked universe), `spy_buyhold` (100% SPY), and `sixty_forty` (60% SPY / 40% AGG). `high_conf_voltarget` inverse-vol-weights the HIGH-confidence book; `conviction_long_short` is market-neutral. Judge on **Sharpe** and **max_drawdown** out-of-sample, not raw return: a fully-invested long book wins on return in a bull market but carries all the risk.

| strategy              | scope         | ann_return   | ann_vol   |   sharpe | max_drawdown   | total_return   |   avg_gross_exposure |
|:----------------------|:--------------|:-------------|:----------|---------:|:---------------|:---------------|---------------------:|
| equal_weight_buyhold  | full          | -10.63%      | 33.84%    |    -0.31 | -58.07%        | -39.37%        |                 1    |
| equal_weight_buyhold  | out_of_sample | -12.93%      | 34.78%    |    -0.37 | -39.63%        | -18.33%        |                 1    |
| all_signals_ew        | full          | -6.23%       | 28.16%    |    -0.22 | -59.17%        | -26.75%        |                 1    |
| all_signals_ew        | out_of_sample | 6.81%        | 28.62%    |     0.24 | -27.61%        | 2.97%          |                 1    |
| high_conf_ew          | full          | 3.47%        | 32.87%    |     0.11 | -44.79%        | -5.54%         |                 0.89 |
| high_conf_ew          | out_of_sample | 23.11%       | 36.94%    |     0.63 | -20.90%        | 19.19%         |                 0.89 |
| high_conf_voltarget   | full          | 4.03%        | 30.55%    |     0.13 | -36.33%        | -1.71%         |                 0.89 |
| high_conf_voltarget   | out_of_sample | 16.70%       | 35.20%    |     0.47 | -17.06%        | 12.07%         |                 0.89 |
| conviction_long_short | full          | -8.22%       | 23.50%    |    -0.35 | -35.60%        | -28.48%        |                 0.97 |
| conviction_long_short | out_of_sample | -2.35%       | 27.13%    |    -0.09 | -21.22%        | -6.25%         |                 0.97 |
| spy_buyhold           | full          | 8.60%        | 13.36%    |     0.64 | -17.81%        | 26.46%         |                 0.78 |
| spy_buyhold           | out_of_sample | -2.27%       | 9.91%     |    -0.23 | -14.83%        | -2.90%         |                 0.78 |
| sixty_forty           | full          | 4.96%        | 8.46%     |     0.59 | -10.80%        | 15.06%         |                 0.78 |
| sixty_forty           | out_of_sample | -2.43%       | 6.44%     |    -0.38 | -10.06%        | -2.78%         |                 0.78 |

## Walk-Forward Robustness

Each book measured across contiguous time folds (each a different regime). A book has durable edge only if `mean_sharpe` is positive, `min_sharpe` isn't deeply negative, and `pct_positive_folds` is high — a single great fold doesn't count. `fold_sharpes` lists each fold oldest-to-newest.

| strategy              |   n_folds |   mean_sharpe |   median_sharpe |   min_sharpe | pct_positive_folds   | mean_return   | fold_sharpes                 |
|:----------------------|----------:|--------------:|----------------:|-------------:|:---------------------|:--------------|:-----------------------------|
| equal_weight_buyhold  |         5 |          0.01 |           -0.47 |        -1.95 | 40.00%               | -6.21%        | 1.89;-1.95;1.23;-0.47;-0.68  |
| all_signals_ew        |         5 |         -0.02 |            0.61 |        -1.8  | 60.00%               | -3.93%        | 0.73;0.61;-0.98;-1.80;1.34   |
| high_conf_ew          |         5 |          0.42 |            0.11 |        -0.62 | 60.00%               | 0.13%         | 1.83;0.11;-0.62;-0.52;1.30   |
| high_conf_voltarget   |         5 |          0.54 |            0.28 |        -0.79 | 60.00%               | 0.48%         | 2.72;0.28;-0.79;-0.21;0.71   |
| conviction_long_short |         5 |         -0.35 |           -0.21 |        -1.25 | 20.00%               | -6.01%        | -0.73;-0.15;-0.21;-1.25;0.59 |
| spy_buyhold           |         5 |          0.63 |            0.34 |        -0.34 | 80.00%               | 4.96%         | 1.93;0.91;0.34;-0.34;0.32    |
| sixty_forty           |         5 |          0.55 |            0.39 |        -0.26 | 80.00%               | 2.91%         | 1.94;0.58;0.39;-0.26;0.09    |

## Strategy Comparison

Each decision rule backtested over the same data. `out_of_sample` is the most recent ~35% of each symbol's history (unseen tail). A rule has real edge only if `median_excess` and `beat_benchmark_pct` stay positive out-of-sample, not just full-sample.

| strategy        | scope         |   symbols | beat_benchmark_pct   | positive_pct   | median_return   | median_benchmark   | median_excess   |   median_sharpe |   total_trades |
|:----------------|:--------------|----------:|:---------------------|:---------------|:----------------|:-------------------|:----------------|----------------:|---------------:|
| trend           | full          |       160 | 33.75%               | 36.25%         | -9.24%          | 17.98%             | -31.36%         |           -0.08 |          11217 |
| trend           | out_of_sample |       160 | 36.25%               | 53.75%         | 3.53%           | 5.20%              | -8.31%          |            0.37 |           3926 |
| mean_reversion  | full          |       157 | 40.13%               | 49.04%         | -0.10%          | 16.27%             | -18.33%         |           -0.02 |           1244 |
| mean_reversion  | out_of_sample |       129 | 44.19%               | 58.14%         | 0.33%           | 2.74%              | -4.13%          |            0.7  |            476 |
| regime_adaptive | full          |       160 | 33.75%               | 34.38%         | -8.91%          | 17.98%             | -31.36%         |           -0.08 |          11492 |
| regime_adaptive | out_of_sample |       160 | 35.62%               | 54.37%         | 3.73%           | 5.20%              | -7.23%          |            0.38 |           4029 |

## Signal Calibration

Realized forward return in the signal's direction, grouped by confidence. HIGH should outrank LOW for the confidence score to be meaningful.

| confidence_level   |   horizon |     n | mean_return   | median_return   | win_rate   |
|:-------------------|----------:|------:|:--------------|:----------------|:-----------|
| HIGH               |         5 |  8163 | 0.21%         | 0.16%           | 52.60%     |
| MEDIUM             |         5 | 29155 | 0.08%         | 0.10%           | 51.15%     |
| LOW                |         5 |  3262 | -0.55%        | -0.44%          | 45.31%     |
| ALL                |         5 | 40580 | 0.06%         | 0.08%           | 50.97%     |
| HIGH               |        10 |  8127 | 0.52%         | 0.21%           | 52.44%     |
| MEDIUM             |        10 | 28883 | 0.27%         | 0.18%           | 51.47%     |
| LOW                |        10 |  3236 | -0.82%        | -0.69%          | 45.58%     |
| ALL                |        10 | 40246 | 0.24%         | 0.13%           | 51.19%     |
| HIGH               |        20 |  8022 | 0.97%         | 0.53%           | 54.06%     |
| MEDIUM             |        20 | 28297 | 0.85%         | 0.61%           | 53.57%     |
| LOW                |        20 |  3202 | -0.64%        | -0.51%          | 47.10%     |
| ALL                |        20 | 39521 | 0.75%         | 0.53%           | 53.14%     |

## Backtest Summary

### Data Quality / Signal Availability

- **ok**: 160 symbols

| symbol     |   trades | return   | benchmark_return   | mdd     |   sharpe | exposure   | skipped_reason   |
|:-----------|---------:|:---------|:-------------------|:--------|---------:|:-----------|:-----------------|
| AAPL       |       63 | 12.89%   | 50.15%             | -20.65% |     0.35 | 49.08%     | ok               |
| AAVE-USD   |       80 | -62.59%  | -76.23%            | -69.30% |    -0.76 | 36.97%     | ok               |
| ABBV       |       64 | -14.59%  | 37.69%             | -30.55% |    -0.28 | 49.25%     | ok               |
| ADA-USD    |       86 | -83.14%  | -80.58%            | -89.43% |    -0.68 | 46.36%     | ok               |
| ADBE       |       66 | -22.69%  | -66.20%            | -38.01% |    -0.23 | 56.91%     | ok               |
| AGG        |       69 | -6.61%   | 0.57%              | -10.16% |    -1.1  | 31.11%     | ok               |
| ALGO-USD   |       86 | -46.34%  | -75.32%            | -53.13% |    -0.49 | 37.74%     | ok               |
| AMAT       |       67 | -22.11%  | 237.05%            | -57.21% |    -0.15 | 53.41%     | ok               |
| AMD        |       56 | 6.53%    | 204.18%            | -47.17% |     0.28 | 38.44%     | ok               |
| AMGN       |       71 | -19.51%  | 14.52%             | -34.14% |    -0.38 | 48.42%     | ok               |
| AMZN       |       74 | -33.84%  | 54.12%             | -42.48% |    -0.99 | 38.27%     | ok               |
| APT-USD    |       76 | -30.14%  | -92.62%            | -69.96% |    -0.05 | 43.68%     | ok               |
| ARB-USD    |       70 | 7.23%    | -88.66%            | -61.76% |     0.31 | 39.27%     | ok               |
| ARKK       |       79 | -30.02%  | 59.84%             | -32.63% |    -0.5  | 38.94%     | ok               |
| ATOM-USD   |       88 | -64.56%  | -70.11%            | -71.11% |    -1.01 | 43.87%     | ok               |
| AVAX-USD   |       74 | -37.98%  | -81.73%            | -60.45% |    -0.31 | 38.70%     | ok               |
| AVGO       |       60 | 30.52%   | 213.04%            | -35.76% |     0.49 | 45.92%     | ok               |
| BA         |       69 | 9.35%    | 1.92%              | -30.56% |     0.28 | 50.58%     | ok               |
| BAC        |       80 | -14.84%  | 72.10%             | -27.64% |    -0.35 | 46.42%     | ok               |
| BCH-USD    |       76 | -3.45%   | -53.32%            | -53.87% |     0.17 | 46.55%     | ok               |
| BITO       |       78 | 6.16%    | -55.39%            | -42.82% |     0.25 | 39.93%     | ok               |
| BLK        |       75 | -5.68%   | 29.97%             | -20.81% |    -0.1  | 42.10%     | ok               |
| BND        |       65 | -7.32%   | 0.62%              | -9.89%  |    -1.18 | 32.28%     | ok               |
| BONK-USD   |       68 | 77.23%   | -83.34%            | -43.77% |     0.75 | 41.95%     | ok               |
| BTC-USD    |       72 | 6.19%    | -31.00%            | -23.38% |     0.24 | 51.34%     | ok               |
| C          |       83 | -24.67%  | 164.63%            | -37.02% |    -0.46 | 50.58%     | ok               |
| CAT        |       72 | 35.17%   | 215.44%            | -21.02% |     0.63 | 57.07%     | ok               |
| CL         |       60 | 18.47%   | 11.23%             | -14.32% |     0.62 | 48.59%     | ok               |
| CMCSA      |       80 | -36.24%  | -40.07%            | -40.02% |    -0.9  | 44.59%     | ok               |
| COMP-USD   |       89 | -36.73%  | -76.74%            | -58.43% |    -0.21 | 45.02%     | ok               |
| COP        |       75 | -27.01%  | 8.25%              | -44.32% |    -0.52 | 40.77%     | ok               |
| COST       |       60 | 6.71%    | 41.85%             | -29.73% |     0.26 | 46.76%     | ok               |
| CRM        |       65 | -34.20%  | -40.82%            | -40.31% |    -0.68 | 43.59%     | ok               |
| CRV-USD    |       62 | 3.48%    | -70.69%            | -39.89% |     0.27 | 33.72%     | ok               |
| CSCO       |       59 | 25.35%   | 134.83%            | -21.79% |     0.54 | 49.42%     | ok               |
| CVX        |       71 | -18.68%  | 31.39%             | -28.09% |    -0.49 | 41.60%     | ok               |
| DASH-USD   |       65 | -47.28%  | 1.22%              | -64.43% |    -0.08 | 31.61%     | ok               |
| DBC        |       58 | -12.57%  | 29.60%             | -25.35% |    -0.43 | 32.78%     | ok               |
| DE         |       74 | -8.61%   | 50.15%             | -25.24% |    -0.1  | 45.76%     | ok               |
| DIA        |       60 | -2.39%   | 34.99%             | -12.94% |    -0.09 | 45.92%     | ok               |
| DIS        |       63 | -4.67%   | 5.22%              | -24.36% |     0.01 | 48.42%     | ok               |
| DOGE-USD   |       75 | -16.53%  | -73.52%            | -60.95% |     0.09 | 49.81%     | ok               |
| DOT-USD    |       90 | -45.89%  | -85.35%            | -60.49% |    -0.33 | 48.08%     | ok               |
| DXY-INDEX  |       44 | -3.74%   | -3.31%             | -6.06%  |    -0.6  | 28.85%     | ok               |
| EEM        |       64 | -9.40%   | 78.40%             | -25.67% |    -0.25 | 43.43%     | ok               |
| EFA        |       58 | -7.97%   | 41.61%             | -13.53% |    -0.29 | 43.76%     | ok               |
| EOG        |       81 | -29.53%  | 23.51%             | -48.13% |    -0.68 | 46.92%     | ok               |
| ETC-USD    |       64 | -35.69%  | -72.15%            | -48.16% |    -0.51 | 31.23%     | ok               |
| ETH-USD    |       60 | 157.31%  | -47.65%            | -30.11% |     1.28 | 44.83%     | ok               |
| EWJ        |       64 | -18.27%  | 39.04%             | -30.73% |    -0.59 | 41.43%     | ok               |
| FCX        |       71 | -37.44%  | 82.52%             | -48.09% |    -0.51 | 46.09%     | ok               |
| FET-USD    |       75 | -13.30%  | -84.23%            | -48.39% |     0.16 | 38.31%     | ok               |
| FIL-USD    |       70 | -32.36%  | -84.94%            | -48.20% |    -0.27 | 32.76%     | ok               |
| FXI        |       50 | -13.44%  | 66.93%             | -24.33% |    -0.27 | 27.95%     | ok               |
| GDX        |       62 | 4.35%    | 189.96%            | -34.99% |     0.2  | 48.59%     | ok               |
| GDXJ       |       68 | -23.60%  | 210.21%            | -44.93% |    -0.24 | 46.42%     | ok               |
| GE         |       74 | 12.51%   | 220.15%            | -27.82% |     0.32 | 51.58%     | ok               |
| GLD        |       48 | 22.92%   | 106.46%            | -16.63% |     0.61 | 44.09%     | ok               |
| GOOGL      |       63 | 74.57%   | 146.37%            | -20.41% |     1.12 | 54.41%     | ok               |
| GRT-USD    |       89 | -13.06%  | -90.29%            | -56.53% |     0.07 | 41.38%     | ok               |
| GS         |       76 | -2.56%   | 175.35%            | -22.13% |     0.05 | 50.75%     | ok               |
| HD         |       69 | -4.50%   | -7.93%             | -17.69% |    -0.04 | 43.93%     | ok               |
| HON        |       95 | -30.77%  | 16.27%             | -30.77% |    -0.86 | 52.75%     | ok               |
| HYG        |       81 | -9.08%   | 3.51%              | -9.59%  |    -1.06 | 33.94%     | ok               |
| IBIT       |       32 | 34.78%   | -5.18%             | -18.95% |     0.75 | 30.15%     | ok               |
| IBM        |       72 | 23.04%   | 57.52%             | -25.31% |     0.51 | 50.92%     | ok               |
| ICP-USD    |       83 | -4.95%   | -75.89%            | -56.10% |     0.22 | 38.51%     | ok               |
| IEF        |       76 | -10.90%  | -1.10%             | -11.70% |    -1.54 | 32.78%     | ok               |
| IEMG       |       58 | -5.52%   | 71.95%             | -26.84% |    -0.12 | 43.59%     | ok               |
| INJ-USD    |       75 | -52.18%  | -76.35%            | -77.42% |    -0.49 | 37.93%     | ok               |
| INTC       |       70 | 55.82%   | 158.34%            | -60.60% |     0.62 | 49.25%     | ok               |
| INTU       |       65 | -11.12%  | -56.12%            | -43.77% |    -0.07 | 42.60%     | ok               |
| ITA        |       74 | -2.80%   | 91.36%             | -23.75% |    -0.01 | 46.59%     | ok               |
| IWM        |       50 | 8.72%    | 49.05%             | -12.83% |     0.36 | 37.10%     | ok               |
| JNJ        |       73 | 4.83%    | 48.26%             | -17.51% |     0.23 | 50.75%     | ok               |
| JPM        |       77 | -20.21%  | 88.54%             | -33.43% |    -0.5  | 52.75%     | ok               |
| KO         |       51 | 27.92%   | 38.69%             | -8.07%  |     1    | 37.94%     | ok               |
| LDO-USD    |       76 | 17.46%   | -83.58%            | -58.32% |     0.41 | 38.70%     | ok               |
| LIN        |       70 | -2.47%   | 28.81%             | -21.53% |    -0.03 | 39.10%     | ok               |
| LINK-USD   |       70 | -13.55%  | -59.88%            | -50.48% |     0.1  | 41.57%     | ok               |
| LLY        |       69 | -11.03%  | 79.59%             | -53.34% |    -0.05 | 51.41%     | ok               |
| LRCX       |       80 | -14.27%  | 340.06%            | -63.56% |    -0.02 | 46.26%     | ok               |
| LTC-USD    |       66 | -34.00%  | -56.64%            | -53.76% |    -0.29 | 48.47%     | ok               |
| MCD        |       77 | -2.74%   | -4.56%             | -18.81% |    -0.06 | 38.44%     | ok               |
| META       |       72 | -12.94%  | 48.51%             | -38.96% |    -0.08 | 51.08%     | ok               |
| MPC        |       71 | -13.74%  | 70.67%             | -44.76% |    -0.14 | 49.92%     | ok               |
| MRK        |       67 | -23.47%  | -0.32%             | -32.14% |    -0.51 | 47.09%     | ok               |
| MS         |       79 | -16.30%  | 149.67%            | -27.79% |    -0.35 | 47.59%     | ok               |
| MSFT       |       81 | -31.47%  | -1.46%             | -38.02% |    -0.81 | 48.42%     | ok               |
| MU         |       51 | 220.55%  | 999.97%            | -68.76% |     1.24 | 59.23%     | ok               |
| NEAR-USD   |       87 | 2.04%    | -56.12%            | -60.07% |     0.28 | 41.95%     | ok               |
| NEM        |       76 | -26.80%  | 186.37%            | -38.49% |    -0.25 | 55.41%     | ok               |
| NFLX       |       62 | 25.14%   | 65.41%             | -21.09% |     0.59 | 54.24%     | ok               |
| NKE        |       93 | -38.79%  | -55.32%            | -55.35% |    -0.55 | 44.09%     | ok               |
| NOW        |       80 | 20.07%   | -32.12%            | -30.25% |     0.4  | 45.92%     | ok               |
| NVDA       |       74 | -26.54%  | 129.52%            | -45.02% |    -0.19 | 59.71%     | ok               |
| OP-USD     |       74 | 4.44%    | -93.85%            | -70.27% |     0.29 | 35.82%     | ok               |
| ORCL       |       72 | 56.23%   | 67.24%             | -29.47% |     0.65 | 53.41%     | ok               |
| OXY        |       65 | 0.15%    | -0.35%             | -30.85% |     0.12 | 43.59%     | ok               |
| PEP        |       85 | -9.64%   | -12.62%            | -21.35% |    -0.22 | 50.25%     | ok               |
| PEPE-USD   |       77 | 12.84%   | -83.66%            | -57.66% |     0.38 | 43.87%     | ok               |
| PFE        |       77 | -37.69%  | -7.42%             | -42.29% |    -1.17 | 36.77%     | ok               |
| PG         |       62 | -10.32%  | 1.18%              | -21.65% |    -0.36 | 41.26%     | ok               |
| PM         |       81 | 1.42%    | 99.39%             | -33.68% |     0.13 | 57.07%     | ok               |
| POL-USD    |       79 | 67.37%   | -83.30%            | -46.45% |     0.78 | 49.23%     | ok               |
| QCOM       |       77 | -18.79%  | 38.50%             | -57.69% |    -0.09 | 48.09%     | ok               |
| QQQ        |       62 | 15.53%   | 71.04%             | -12.88% |     0.47 | 46.09%     | ok               |
| RENDER-USD |       96 | -17.88%  | -56.75%            | -45.00% |     0.11 | 44.38%     | ok               |
| RTX        |       56 | 19.78%   | 115.87%            | -16.99% |     0.54 | 51.41%     | ok               |
| SBUX       |       64 | -21.86%  | 10.71%             | -29.34% |    -0.43 | 38.44%     | ok               |
| SCHW       |       74 | -21.97%  | 43.17%             | -30.41% |    -0.52 | 45.42%     | ok               |
| SHIB-USD   |       76 | -25.73%  | -76.82%            | -48.95% |    -0.1  | 52.30%     | ok               |
| SHY        |       50 | -2.17%   | 0.00%              | -2.85%  |    -0.75 | 35.61%     | ok               |
| SKY-USD    |       68 | -29.04%  | -0.99%             | -43.98% |    -0.37 | 40.66%     | ok               |
| SLB        |       75 | -30.05%  | 10.85%             | -54.95% |    -0.54 | 49.92%     | ok               |
| SLV        |       60 | 26.46%   | 203.12%            | -42.66% |     0.48 | 40.27%     | ok               |
| SMH        |       48 | 94.32%   | 229.68%            | -33.99% |     1.19 | 51.08%     | ok               |
| SNX-USD    |       63 | 22.00%   | -86.52%            | -32.91% |     0.44 | 40.61%     | ok               |
| SOL-USD    |       68 | -37.63%  | -62.33%            | -55.52% |    -0.15 | 59.96%     | ok               |
| SOXX       |       55 | 80.72%   | 196.54%            | -40.34% |     1.02 | 50.08%     | ok               |
| SPY        |       58 | 7.21%    | 53.43%             | -16.47% |     0.31 | 50.75%     | ok               |
| SUSHI-USD  |       90 | -75.60%  | -88.01%            | -81.22% |    -1.06 | 35.44%     | ok               |
| T          |       64 | 27.61%   | 40.36%             | -17.01% |     0.69 | 50.25%     | ok               |
| TGT        |       56 | -11.79%  | -3.65%             | -41.74% |    -0.16 | 38.60%     | ok               |
| TIA-USD    |       82 | -14.40%  | -92.82%            | -55.60% |     0.1  | 33.72%     | ok               |
| TLT        |       70 | -21.90%  | -9.38%             | -23.75% |    -1.6  | 32.45%     | ok               |
| TMO        |       57 | 13.37%   | -15.19%            | -16.83% |     0.37 | 48.42%     | ok               |
| TMUS       |       70 | 11.16%   | 15.04%             | -24.50% |     0.33 | 48.59%     | ok               |
| TRX-USD    |       70 | 2.00%    | 30.96%             | -22.90% |     0.14 | 48.66%     | ok               |
| TSLA       |       68 | 3.12%    | 94.65%             | -57.89% |     0.24 | 43.26%     | ok               |
| TXN        |       77 | -15.83%  | 72.24%             | -46.98% |    -0.1  | 53.41%     | ok               |
| UNH        |       76 | 23.27%   | -20.36%            | -27.74% |     0.45 | 51.58%     | ok               |
| UNI-USD    |       90 | -67.11%  | -81.58%            | -81.03% |    -0.7  | 41.38%     | ok               |
| UPS        |       66 | -35.51%  | -31.84%            | -40.62% |    -0.7  | 39.43%     | ok               |
| USO        |       68 | 2.80%    | 79.98%             | -43.35% |     0.17 | 34.44%     | ok               |
| VEA        |       58 | -0.98%   | 52.56%             | -17.93% |     0.01 | 44.09%     | ok               |
| VIXY       |       92 | -78.16%  | -59.62%            | -87.63% |    -0.94 | 31.61%     | ok               |
| VNQ        |       75 | -16.77%  | 14.67%             | -24.92% |    -0.7  | 37.60%     | ok               |
| VTI        |       66 | -0.72%   | 52.28%             | -18.77% |     0.04 | 52.08%     | ok               |
| VWO        |       76 | -13.41%  | 51.45%             | -25.20% |    -0.47 | 44.09%     | ok               |
| VZ         |       83 | -20.61%  | 21.55%             | -31.88% |    -0.62 | 38.44%     | ok               |
| WFC        |       86 | -18.93%  | 72.53%             | -30.87% |    -0.33 | 47.25%     | ok               |
| WIF-USD    |       72 | -34.81%  | -89.47%            | -50.40% |    -0.1  | 32.95%     | ok               |
| WMT        |       55 | 32.33%   | 123.61%            | -21.31% |     0.85 | 52.08%     | ok               |
| XBI        |       62 | -4.13%   | 50.31%             | -21.75% |    -0.02 | 39.43%     | ok               |
| XLB        |       70 | -14.85%  | 26.54%             | -26.57% |    -0.51 | 37.60%     | ok               |
| XLC        |       63 | 16.62%   | 48.91%             | -12.33% |     0.57 | 55.74%     | ok               |
| XLE        |       73 | -9.72%   | 43.03%             | -36.18% |    -0.17 | 46.76%     | ok               |
| XLF        |       74 | -11.20%  | 39.96%             | -23.61% |    -0.36 | 48.75%     | ok               |
| XLI        |       64 | 5.29%    | 55.47%             | -11.38% |     0.26 | 46.92%     | ok               |
| XLK        |       42 | 63.88%   | 83.83%             | -14.75% |     1.2  | 48.59%     | ok               |
| XLM-USD    |       69 | 14.82%   | -54.70%            | -45.54% |     0.37 | 45.79%     | ok               |
| XLP        |       72 | 5.69%    | 19.69%             | -10.28% |     0.35 | 42.93%     | ok               |
| XLU        |       69 | -7.05%   | 46.79%             | -18.13% |    -0.28 | 39.27%     | ok               |
| XLV        |       68 | -10.16%  | 9.81%              | -15.55% |    -0.48 | 36.77%     | ok               |
| XLY        |       74 | 0.76%    | 33.93%             | -14.01% |     0.09 | 44.59%     | ok               |
| XOM        |       58 | 1.28%    | 51.84%             | -20.29% |     0.11 | 36.44%     | ok               |
| XRP-USD    |       62 | -36.21%  | -49.68%            | -48.42% |    -0.36 | 35.82%     | ok               |
| YFI-USD    |       83 | -51.43%  | -76.30%            | -67.78% |    -0.73 | 40.61%     | ok               |
| ZEC-USD    |       69 | 43.83%   | 873.79%            | -46.93% |     0.56 | 36.40%     | ok               |

## AAPL Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 22.46%   | 50.15%             | -21.71% |     0.51 |       67 | 53.24%     | ok               |
|          25 | 16.61%   | 50.15%             | -20.03% |     0.42 |       65 | 51.08%     | ok               |
|          15 | 16.53%   | 50.15%             | -23.86% |     0.41 |       74 | 60.57%     | ok               |
|          30 | 12.89%   | 50.15%             | -20.65% |     0.35 |       63 | 49.08%     | ok               |
|          35 | 7.72%    | 50.15%             | -22.04% |     0.26 |       63 | 46.92%     | ok               |

## AAVE-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 5.38%    | -76.23%            | -46.87% |     0.27 |       38 | 26.05%     | ok               |
|          40 | -0.24%   | -76.23%            | -43.61% |     0.21 |       38 | 29.69%     | ok               |
|          35 | -24.98%  | -76.23%            | -51.96% |    -0.1  |       52 | 32.38%     | ok               |
|          50 | -29.70%  | -76.23%            | -47.78% |    -0.27 |       42 | 20.31%     | ok               |
|          15 | -58.51%  | -76.23%            | -66.34% |    -0.47 |       82 | 50.96%     | ok               |

## ABBV Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -1.49%   | 37.69%             | -26.16% |     0.05 |       50 | 38.94%     | ok               |
|          40 | -11.05%  | 37.69%             | -26.61% |    -0.2  |       64 | 43.59%     | ok               |
|          35 | -12.32%  | 37.69%             | -27.83% |    -0.23 |       66 | 46.42%     | ok               |
|          30 | -14.59%  | 37.69%             | -30.55% |    -0.28 |       64 | 49.25%     | ok               |
|          45 | -13.82%  | 37.69%             | -29.59% |    -0.28 |       54 | 40.93%     | ok               |

## ADA-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -82.95%  | -80.58%            | -91.37% |    -0.55 |       80 | 61.49%     | ok               |
|          20 | -82.95%  | -80.58%            | -91.89% |    -0.57 |       84 | 56.70%     | ok               |
|          50 | -78.55%  | -80.58%            | -86.36% |    -0.61 |       57 | 27.01%     | ok               |
|          25 | -84.16%  | -80.58%            | -91.94% |    -0.64 |       83 | 53.45%     | ok               |
|          45 | -80.84%  | -80.58%            | -88.36% |    -0.64 |       60 | 31.80%     | ok               |

## ADBE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 10.63%   | -66.20%            | -21.34% |     0.3  |       76 | 49.25%     | ok               |
|          40 | -3.65%   | -66.20%            | -20.88% |     0.05 |       72 | 42.26%     | ok               |
|          25 | -7.34%   | -66.20%            | -31.29% |     0.04 |       50 | 61.06%     | ok               |
|          15 | -17.23%  | -66.20%            | -31.86% |    -0.11 |       61 | 65.72%     | ok               |
|          20 | -18.85%  | -66.20%            | -34.42% |    -0.14 |       50 | 63.23%     | ok               |

## AGG Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -6.61%   | 0.57%              | -10.16% |    -1.1  |       69 | 31.11%     | ok               |
|          20 | -7.69%   | 0.57%              | -10.67% |    -1.13 |       73 | 36.77%     | ok               |
|          45 | -5.75%   | 0.57%              | -7.89%  |    -1.16 |       52 | 20.47%     | ok               |
|          25 | -7.87%   | 0.57%              | -11.31% |    -1.2  |       73 | 35.11%     | ok               |
|          50 | -5.57%   | 0.57%              | -7.92%  |    -1.25 |       46 | 16.97%     | ok               |

## ALGO-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -46.34%  | -75.32%            | -53.13% |    -0.49 |       86 | 37.74%     | ok               |
|          15 | -55.64%  | -75.32%            | -69.47% |    -0.54 |       82 | 49.43%     | ok               |
|          25 | -58.13%  | -75.32%            | -73.33% |    -0.64 |       88 | 44.83%     | ok               |
|          20 | -60.33%  | -75.32%            | -72.09% |    -0.66 |       86 | 47.32%     | ok               |
|          35 | -52.08%  | -75.32%            | -53.42% |    -0.72 |       64 | 31.23%     | ok               |

## AMAT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -6.93%   | 237.05%            | -54.05% |     0.1  |       64 | 62.06%     | ok               |
|          30 | -22.11%  | 237.05%            | -57.21% |    -0.15 |       67 | 53.41%     | ok               |
|          20 | -27.80%  | 237.05%            | -60.16% |    -0.22 |       70 | 58.57%     | ok               |
|          35 | -27.65%  | 237.05%            | -55.26% |    -0.26 |       69 | 51.25%     | ok               |
|          50 | -25.82%  | 237.05%            | -48.72% |    -0.26 |       50 | 39.27%     | ok               |

## AMD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 6.53%    | 204.18%            | -47.17% |     0.28 |       56 | 38.44%     | ok               |
|          50 | 4.65%    | 204.18%            | -48.79% |     0.25 |       60 | 32.78%     | ok               |
|          35 | -7.05%   | 204.18%            | -54.57% |     0.14 |       62 | 40.43%     | ok               |
|          45 | -14.89%  | 204.18%            | -56.22% |     0.04 |       64 | 35.77%     | ok               |
|          30 | -19.31%  | 204.18%            | -59.88% |     0.02 |       63 | 42.93%     | ok               |

## AMGN Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -14.29%  | 14.52%             | -26.64% |    -0.22 |       74 | 54.58%     | ok               |
|          15 | -17.32%  | 14.52%             | -27.92% |    -0.28 |       72 | 60.23%     | ok               |
|          35 | -16.74%  | 14.52%             | -31.23% |    -0.31 |       69 | 44.76%     | ok               |
|          30 | -19.51%  | 14.52%             | -34.14% |    -0.38 |       71 | 48.42%     | ok               |
|          25 | -23.09%  | 14.52%             | -33.41% |    -0.46 |       69 | 50.92%     | ok               |

## AMZN Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -17.83%  | 54.12%             | -28.70% |    -0.52 |       50 | 29.78%     | ok               |
|          50 | -25.03%  | 54.12%             | -35.48% |    -0.88 |       48 | 24.13%     | ok               |
|          45 | -25.89%  | 54.12%             | -35.47% |    -0.89 |       50 | 26.96%     | ok               |
|          35 | -29.70%  | 54.12%             | -38.29% |    -0.91 |       62 | 32.95%     | ok               |
|          30 | -33.84%  | 54.12%             | -42.48% |    -0.99 |       74 | 38.27%     | ok               |

## APT-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 49.93%   | -92.62%            | -46.73% |     0.72 |       44 | 20.50%     | ok               |
|          45 | 13.99%   | -92.62%            | -63.86% |     0.36 |       60 | 26.63%     | ok               |
|          40 | -7.90%   | -92.62%            | -63.33% |     0.15 |       66 | 32.18%     | ok               |
|          20 | -18.96%  | -92.62%            | -70.51% |     0.1  |       71 | 51.34%     | ok               |
|          35 | -14.51%  | -92.62%            | -64.45% |     0.1  |       70 | 37.74%     | ok               |

## ARB-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 70.50%   | -88.66%            | -52.62% |     0.72 |       85 | 55.36%     | ok               |
|          40 | 49.31%   | -88.66%            | -46.33% |     0.65 |       50 | 30.08%     | ok               |
|          35 | 39.60%   | -88.66%            | -54.93% |     0.57 |       62 | 33.72%     | ok               |
|          20 | 41.03%   | -88.66%            | -59.44% |     0.57 |       75 | 50.00%     | ok               |
|          45 | 24.86%   | -88.66%            | -50.83% |     0.46 |       56 | 23.37%     | ok               |

## ARKK Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -26.33%  | 59.84%             | -34.90% |    -0.32 |       92 | 50.42%     | ok               |
|          20 | -30.68%  | 59.84%             | -34.90% |    -0.44 |       87 | 45.76%     | ok               |
|          30 | -30.02%  | 59.84%             | -32.63% |    -0.5  |       79 | 38.94%     | ok               |
|          35 | -31.21%  | 59.84%             | -33.79% |    -0.56 |       78 | 36.61%     | ok               |
|          40 | -32.66%  | 59.84%             | -34.78% |    -0.64 |       70 | 31.78%     | ok               |

## ATOM-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -62.85%  | -70.11%            | -69.40% |    -0.89 |       93 | 50.38%     | ok               |
|          15 | -68.98%  | -70.11%            | -72.76% |    -1    |       95 | 60.73%     | ok               |
|          30 | -64.56%  | -70.11%            | -71.11% |    -1.01 |       88 | 43.87%     | ok               |
|          45 | -59.16%  | -70.11%            | -64.98% |    -1.09 |       72 | 28.35%     | ok               |
|          35 | -64.16%  | -70.11%            | -68.87% |    -1.11 |       78 | 38.51%     | ok               |

## AVAX-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 15.04%   | -81.73%            | -34.50% |     0.37 |       38 | 19.54%     | ok               |
|          15 | 4.86%    | -81.73%            | -52.46% |     0.3  |       61 | 51.92%     | ok               |
|          45 | 6.27%    | -81.73%            | -41.07% |     0.26 |       40 | 23.56%     | ok               |
|          40 | -8.27%   | -81.73%            | -47.98% |     0.08 |       46 | 26.44%     | ok               |
|          35 | -14.78%  | -81.73%            | -48.82% |     0.02 |       60 | 31.80%     | ok               |

## AVGO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 30.52%   | 213.04%            | -35.76% |     0.49 |       60 | 45.92%     | ok               |
|          25 | 25.88%   | 213.04%            | -38.01% |     0.45 |       64 | 46.59%     | ok               |
|          35 | 21.64%   | 213.04%            | -36.19% |     0.41 |       70 | 43.26%     | ok               |
|          40 | 21.23%   | 213.04%            | -40.70% |     0.4  |       60 | 40.10%     | ok               |
|          50 | 15.24%   | 213.04%            | -35.84% |     0.34 |       62 | 33.94%     | ok               |

## BA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 25.12%   | 1.92%              | -13.34% |     0.65 |       44 | 31.78%     | ok               |
|          35 | 32.58%   | 1.92%              | -23.77% |     0.61 |       74 | 45.92%     | ok               |
|          40 | 13.32%   | 1.92%              | -24.52% |     0.35 |       52 | 39.60%     | ok               |
|          25 | 12.62%   | 1.92%              | -32.48% |     0.32 |       72 | 54.08%     | ok               |
|          30 | 9.35%    | 1.92%              | -30.56% |     0.28 |       69 | 50.58%     | ok               |

## BAC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -3.78%   | 72.10%             | -20.40% |    -0.06 |       60 | 34.44%     | ok               |
|          20 | -7.74%   | 72.10%             | -20.73% |    -0.11 |       80 | 50.92%     | ok               |
|          50 | -7.04%   | 72.10%             | -20.35% |    -0.18 |       58 | 31.45%     | ok               |
|          35 | -8.68%   | 72.10%             | -27.83% |    -0.19 |       72 | 42.43%     | ok               |
|          15 | -12.11%  | 72.10%             | -22.24% |    -0.21 |       82 | 55.24%     | ok               |

## BCH-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 1.60%    | -53.32%            | -45.63% |     0.24 |       73 | 53.07%     | ok               |
|          25 | -4.14%   | -53.32%            | -51.09% |     0.17 |       70 | 48.66%     | ok               |
|          30 | -3.45%   | -53.32%            | -53.87% |     0.17 |       76 | 46.55%     | ok               |
|          15 | -10.02%  | -53.32%            | -49.31% |     0.12 |       82 | 57.66%     | ok               |
|          40 | -18.04%  | -53.32%            | -60.69% |    -0.05 |       63 | 39.66%     | ok               |

## BITO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 20.22%   | -55.39%            | -32.29% |     0.4  |       54 | 25.29%     | ok               |
|          30 | 6.16%    | -55.39%            | -42.82% |     0.25 |       78 | 39.93%     | ok               |
|          15 | -0.51%   | -55.39%            | -48.38% |     0.19 |       87 | 48.75%     | ok               |
|          45 | 0.27%    | -55.39%            | -43.53% |     0.16 |       58 | 28.29%     | ok               |
|          25 | -2.24%   | -55.39%            | -41.73% |     0.16 |       82 | 42.93%     | ok               |

## BLK Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 0.70%    | 29.97%             | -14.19% |     0.09 |       80 | 38.27%     | ok               |
|          40 | -0.67%   | 29.97%             | -15.81% |     0.04 |       70 | 34.11%     | ok               |
|          20 | -4.28%   | 29.97%             | -17.89% |    -0.05 |       77 | 46.59%     | ok               |
|          30 | -5.68%   | 29.97%             | -20.81% |    -0.1  |       75 | 42.10%     | ok               |
|          25 | -6.63%   | 29.97%             | -19.84% |    -0.12 |       75 | 44.43%     | ok               |

## BND Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -6.64%   | 0.62%              | -9.05%  |    -0.97 |       65 | 38.44%     | ok               |
|          25 | -6.87%   | 0.62%              | -10.14% |    -1.05 |       67 | 36.11%     | ok               |
|          30 | -7.32%   | 0.62%              | -9.89%  |    -1.18 |       65 | 32.28%     | ok               |
|          15 | -8.85%   | 0.62%              | -10.58% |    -1.27 |       75 | 41.26%     | ok               |
|          45 | -7.56%   | 0.62%              | -9.57%  |    -1.47 |       50 | 21.96%     | ok               |

## BONK-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 170.82%  | -83.34%            | -35.57% |     1.24 |       46 | 22.22%     | ok               |
|          25 | 200.30%  | -83.34%            | -46.61% |     1.11 |       65 | 48.28%     | ok               |
|          20 | 183.34%  | -83.34%            | -54.25% |     1.06 |       66 | 52.87%     | ok               |
|          15 | 174.11%  | -83.34%            | -62.48% |     1.01 |       67 | 57.28%     | ok               |
|          45 | 85.55%   | -83.34%            | -42.36% |     0.84 |       56 | 27.01%     | ok               |

## BTC-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 51.83%   | -31.00%            | -14.50% |     0.95 |       44 | 34.10%     | ok               |
|          45 | 41.09%   | -31.00%            | -15.18% |     0.81 |       44 | 30.65%     | ok               |
|          35 | 36.01%   | -31.00%            | -22.12% |     0.7  |       68 | 41.00%     | ok               |
|          30 | 17.30%   | -31.00%            | -21.75% |     0.41 |       70 | 47.51%     | ok               |
|          50 | 14.18%   | -31.00%            | -16.15% |     0.4  |       42 | 25.29%     | ok               |

## C Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -7.86%   | 164.63%            | -22.28% |    -0.15 |       68 | 35.27%     | ok               |
|          25 | -21.28%  | 164.63%            | -34.18% |    -0.37 |       75 | 52.58%     | ok               |
|          45 | -16.66%  | 164.63%            | -30.30% |    -0.38 |       82 | 39.77%     | ok               |
|          15 | -23.28%  | 164.63%            | -35.02% |    -0.39 |       76 | 59.23%     | ok               |
|          20 | -23.92%  | 164.63%            | -35.56% |    -0.42 |       83 | 55.57%     | ok               |

## CAT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 35.17%   | 215.44%            | -21.02% |     0.63 |       72 | 57.07%     | ok               |
|          25 | 35.30%   | 215.44%            | -26.37% |     0.63 |       68 | 59.90%     | ok               |
|          20 | 32.56%   | 215.44%            | -25.65% |     0.59 |       78 | 63.23%     | ok               |
|          45 | 25.70%   | 215.44%            | -27.12% |     0.53 |       54 | 45.76%     | ok               |
|          35 | 23.23%   | 215.44%            | -27.72% |     0.48 |       70 | 50.92%     | ok               |

## CL Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 17.24%   | 11.23%             | -12.98% |     0.69 |       44 | 32.45%     | ok               |
|          30 | 18.47%   | 11.23%             | -14.32% |     0.62 |       60 | 48.59%     | ok               |
|          45 | 11.88%   | 11.23%             | -13.51% |     0.49 |       48 | 35.44%     | ok               |
|          35 | 11.18%   | 11.23%             | -13.83% |     0.42 |       64 | 44.76%     | ok               |
|          40 | 7.95%    | 11.23%             | -12.70% |     0.34 |       58 | 39.43%     | ok               |

## CMCSA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -34.75%  | -40.07%            | -49.03% |    -0.76 |       85 | 58.90%     | ok               |
|          30 | -36.24%  | -40.07%            | -40.02% |    -0.9  |       80 | 44.59%     | ok               |
|          25 | -41.75%  | -40.07%            | -45.20% |    -1.07 |       87 | 49.92%     | ok               |
|          50 | -29.51%  | -40.07%            | -33.68% |    -1.08 |       50 | 17.14%     | ok               |
|          20 | -43.00%  | -40.07%            | -47.23% |    -1.08 |       91 | 55.24%     | ok               |

## COMP-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -3.83%   | -76.74%            | -38.71% |     0.15 |       46 | 20.69%     | ok               |
|          30 | -36.73%  | -76.74%            | -58.43% |    -0.21 |       89 | 45.02%     | ok               |
|          25 | -39.96%  | -76.74%            | -60.58% |    -0.22 |       89 | 50.19%     | ok               |
|          15 | -47.94%  | -76.74%            | -65.55% |    -0.31 |      103 | 61.69%     | ok               |
|          40 | -41.16%  | -76.74%            | -47.52% |    -0.37 |       74 | 33.14%     | ok               |

## COP Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -9.77%   | 8.25%              | -34.21% |    -0.15 |       48 | 27.29%     | ok               |
|          45 | -17.04%  | 8.25%              | -40.57% |    -0.33 |       60 | 30.28%     | ok               |
|          35 | -26.56%  | 8.25%              | -43.96% |    -0.52 |       77 | 37.44%     | ok               |
|          30 | -27.01%  | 8.25%              | -44.32% |    -0.52 |       75 | 40.77%     | ok               |
|          40 | -28.99%  | 8.25%              | -46.34% |    -0.65 |       70 | 33.11%     | ok               |

## COST Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | 18.65%   | 41.85%             | -24.73% |     0.56 |       61 | 50.25%     | ok               |
|          20 | 18.04%   | 41.85%             | -24.32% |     0.54 |       62 | 52.75%     | ok               |
|          35 | 11.83%   | 41.85%             | -26.58% |     0.41 |       54 | 43.76%     | ok               |
|          30 | 6.71%    | 41.85%             | -29.73% |     0.26 |       60 | 46.76%     | ok               |
|          40 | 4.97%    | 41.85%             | -28.41% |     0.22 |       56 | 40.77%     | ok               |

## CRM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -29.21%  | -40.82%            | -38.20% |    -0.42 |       90 | 55.24%     | ok               |
|          35 | -23.39%  | -40.82%            | -35.48% |    -0.43 |       62 | 38.77%     | ok               |
|          40 | -30.31%  | -40.82%            | -41.30% |    -0.68 |       68 | 34.94%     | ok               |
|          30 | -34.20%  | -40.82%            | -40.31% |    -0.68 |       65 | 43.59%     | ok               |
|          20 | -39.65%  | -40.82%            | -41.96% |    -0.73 |       78 | 48.92%     | ok               |

## CRV-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 30.31%   | -70.69%            | -37.78% |     0.5  |       64 | 29.12%     | ok               |
|          50 | 23.26%   | -70.69%            | -29.30% |     0.45 |       38 | 16.48%     | ok               |
|          45 | 17.23%   | -70.69%            | -42.29% |     0.39 |       50 | 19.35%     | ok               |
|          40 | 16.21%   | -70.69%            | -38.86% |     0.38 |       52 | 24.90%     | ok               |
|          30 | 3.48%    | -70.69%            | -39.89% |     0.27 |       62 | 33.72%     | ok               |

## CSCO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 28.22%   | 134.83%            | -19.34% |     0.63 |       58 | 38.94%     | ok               |
|          45 | 28.24%   | 134.83%            | -19.34% |     0.62 |       51 | 40.93%     | ok               |
|          30 | 25.35%   | 134.83%            | -21.79% |     0.54 |       59 | 49.42%     | ok               |
|          25 | 24.74%   | 134.83%            | -23.28% |     0.53 |       63 | 51.58%     | ok               |
|          35 | 22.47%   | 134.83%            | -23.68% |     0.5  |       51 | 46.92%     | ok               |

## CVX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -16.77%  | 31.39%             | -27.97% |    -0.4  |       73 | 45.76%     | ok               |
|          25 | -17.12%  | 31.39%             | -27.56% |    -0.41 |       77 | 44.59%     | ok               |
|          30 | -18.68%  | 31.39%             | -28.09% |    -0.49 |       71 | 41.60%     | ok               |
|          45 | -16.57%  | 31.39%             | -28.32% |    -0.5  |       61 | 30.95%     | ok               |
|          35 | -18.44%  | 31.39%             | -27.83% |    -0.5  |       71 | 38.60%     | ok               |

## DASH-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 110.90%  | 1.22%              | -31.38% |     0.88 |       42 | 17.24%     | ok               |
|          40 | 57.71%   | 1.22%              | -34.44% |     0.64 |       46 | 23.75%     | ok               |
|          45 | 52.31%   | 1.22%              | -39.58% |     0.61 |       46 | 19.54%     | ok               |
|          25 | -42.64%  | 1.22%              | -64.14% |    -0.01 |       71 | 34.48%     | ok               |
|          35 | -42.46%  | 1.22%              | -63.23% |    -0.02 |       71 | 28.16%     | ok               |

## DBC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | -9.68%   | 29.60%             | -23.38% |    -0.31 |       60 | 31.61%     | ok               |
|          50 | -8.54%   | 29.60%             | -19.91% |    -0.32 |       42 | 21.13%     | ok               |
|          45 | -9.90%   | 29.60%             | -21.08% |    -0.35 |       54 | 24.46%     | ok               |
|          15 | -12.34%  | 29.60%             | -27.30% |    -0.4  |       69 | 37.10%     | ok               |
|          30 | -12.57%  | 29.60%             | -25.35% |    -0.43 |       58 | 32.78%     | ok               |

## DE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -7.69%   | 50.15%             | -29.90% |    -0.07 |       75 | 51.25%     | ok               |
|          30 | -8.61%   | 50.15%             | -25.24% |    -0.1  |       74 | 45.76%     | ok               |
|          25 | -9.97%   | 50.15%             | -27.66% |    -0.13 |       77 | 48.59%     | ok               |
|          50 | -7.99%   | 50.15%             | -22.53% |    -0.15 |       68 | 30.45%     | ok               |
|          45 | -9.88%   | 50.15%             | -26.22% |    -0.18 |       68 | 34.94%     | ok               |

## DIA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | -0.33%   | 34.99%             | -13.15% |     0.02 |       60 | 43.76%     | ok               |
|          25 | -0.87%   | 34.99%             | -11.28% |    -0.01 |       60 | 47.09%     | ok               |
|          30 | -2.39%   | 34.99%             | -12.94% |    -0.09 |       60 | 45.92%     | ok               |
|          20 | -4.26%   | 34.99%             | -13.85% |    -0.18 |       64 | 49.42%     | ok               |
|          40 | -4.39%   | 34.99%             | -15.06% |    -0.22 |       66 | 40.93%     | ok               |

## DIS Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 37.94%   | 5.22%              | -14.24% |     0.92 |       50 | 31.11%     | ok               |
|          45 | 9.01%    | 5.22%              | -15.37% |     0.29 |       51 | 34.61%     | ok               |
|          40 | 8.03%    | 5.22%              | -22.77% |     0.26 |       63 | 39.77%     | ok               |
|          35 | 1.06%    | 5.22%              | -22.75% |     0.13 |       71 | 45.42%     | ok               |
|          15 | -1.15%   | 5.22%              | -26.63% |     0.1  |       86 | 59.07%     | ok               |

## DOGE-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 16.36%   | -73.52%            | -57.89% |     0.42 |       81 | 64.75%     | ok               |
|          20 | 3.43%    | -73.52%            | -55.83% |     0.31 |       84 | 60.54%     | ok               |
|          25 | -0.99%   | -73.52%            | -53.72% |     0.26 |       70 | 54.79%     | ok               |
|          30 | -16.53%  | -73.52%            | -60.95% |     0.09 |       75 | 49.81%     | ok               |
|          35 | -45.34%  | -73.52%            | -63.16% |    -0.38 |       72 | 43.10%     | ok               |

## DOT-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -19.10%  | -85.35%            | -44.94% |    -0.11 |       56 | 26.25%     | ok               |
|          45 | -23.28%  | -85.35%            | -50.00% |    -0.15 |       52 | 31.03%     | ok               |
|          40 | -31.65%  | -85.35%            | -49.85% |    -0.25 |       56 | 34.48%     | ok               |
|          35 | -43.01%  | -85.35%            | -60.80% |    -0.3  |       80 | 41.57%     | ok               |
|          30 | -45.89%  | -85.35%            | -60.49% |    -0.33 |       90 | 48.08%     | ok               |

## DXY-INDEX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -4.11%   | -3.31%             | -9.98%  |    -0.46 |       68 | 58.35%     | ok               |
|          15 | -5.47%   | -3.31%             | -11.57% |    -0.5  |       90 | 75.70%     | ok               |
|          40 | -4.13%   | -3.31%             | -7.30%  |    -0.52 |       68 | 47.51%     | ok               |
|          50 | -3.74%   | -3.31%             | -6.06%  |    -0.6  |       44 | 28.85%     | ok               |
|          35 | -5.05%   | -3.31%             | -10.12% |    -0.6  |       71 | 53.58%     | ok               |

## EEM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -4.96%   | 78.40%             | -19.52% |    -0.11 |       64 | 39.77%     | ok               |
|          35 | -5.62%   | 78.40%             | -23.88% |    -0.12 |       66 | 41.76%     | ok               |
|          50 | -4.94%   | 78.40%             | -15.88% |    -0.12 |       52 | 35.77%     | ok               |
|          45 | -6.04%   | 78.40%             | -17.36% |    -0.16 |       54 | 37.44%     | ok               |
|          30 | -9.40%   | 78.40%             | -25.67% |    -0.25 |       64 | 43.43%     | ok               |

## EFA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -1.73%   | 41.61%             | -11.24% |    -0    |       60 | 51.75%     | ok               |
|          20 | -8.49%   | 41.61%             | -12.86% |    -0.29 |       65 | 48.75%     | ok               |
|          30 | -7.97%   | 41.61%             | -13.53% |    -0.29 |       58 | 43.76%     | ok               |
|          25 | -10.49%  | 41.61%             | -15.78% |    -0.39 |       62 | 46.26%     | ok               |
|          40 | -9.72%   | 41.61%             | -15.73% |    -0.39 |       62 | 40.10%     | ok               |

## EOG Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -19.95%  | 23.51%             | -39.57% |    -0.49 |       58 | 29.78%     | ok               |
|          45 | -21.85%  | 23.51%             | -38.89% |    -0.53 |       56 | 33.11%     | ok               |
|          40 | -26.92%  | 23.51%             | -42.30% |    -0.68 |       64 | 36.61%     | ok               |
|          30 | -29.53%  | 23.51%             | -48.13% |    -0.68 |       81 | 46.92%     | ok               |
|          35 | -29.88%  | 23.51%             | -45.93% |    -0.74 |       79 | 41.76%     | ok               |

## ETC-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -7.93%   | -72.15%            | -27.89% |    -0.02 |       28 | 17.05%     | ok               |
|          35 | -15.03%  | -72.15%            | -42.62% |    -0.11 |       44 | 27.01%     | ok               |
|          45 | -16.07%  | -72.15%            | -35.44% |    -0.17 |       26 | 18.97%     | ok               |
|          40 | -21.04%  | -72.15%            | -40.48% |    -0.26 |       42 | 22.80%     | ok               |
|          30 | -35.69%  | -72.15%            | -48.16% |    -0.51 |       64 | 31.23%     | ok               |

## ETH-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 157.31%  | -47.65%            | -30.11% |     1.28 |       60 | 44.83%     | ok               |
|          30 | 151.00%  | -47.65%            | -32.89% |     1.2  |       64 | 52.87%     | ok               |
|          40 | 62.72%   | -47.65%            | -33.11% |     0.8  |       56 | 37.36%     | ok               |
|          45 | 34.50%   | -47.65%            | -34.50% |     0.57 |       52 | 33.33%     | ok               |
|          25 | 33.53%   | -47.65%            | -40.90% |     0.53 |       69 | 58.62%     | ok               |

## EWJ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -18.27%  | 39.04%             | -30.73% |    -0.59 |       64 | 41.43%     | ok               |
|          20 | -19.65%  | 39.04%             | -31.32% |    -0.62 |       60 | 43.43%     | ok               |
|          25 | -21.97%  | 39.04%             | -31.18% |    -0.72 |       60 | 42.43%     | ok               |
|          35 | -22.19%  | 39.04%             | -32.54% |    -0.75 |       70 | 39.77%     | ok               |
|          15 | -24.97%  | 39.04%             | -32.24% |    -0.78 |       74 | 46.59%     | ok               |

## FCX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -7.45%   | 82.52%             | -26.57% |     0    |       56 | 29.62%     | ok               |
|          45 | -12.11%  | 82.52%             | -33.82% |    -0.06 |       56 | 33.94%     | ok               |
|          40 | -26.64%  | 82.52%             | -44.23% |    -0.33 |       68 | 39.10%     | ok               |
|          30 | -37.44%  | 82.52%             | -48.09% |    -0.51 |       71 | 46.09%     | ok               |
|          35 | -38.37%  | 82.52%             | -51.29% |    -0.56 |       75 | 43.93%     | ok               |

## FET-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 66.53%   | -84.23%            | -56.84% |     0.7  |       84 | 49.43%     | ok               |
|          15 | 11.40%   | -84.23%            | -59.22% |     0.4  |       84 | 52.49%     | ok               |
|          25 | -1.38%   | -84.23%            | -57.43% |     0.28 |       89 | 42.53%     | ok               |
|          30 | -13.30%  | -84.23%            | -48.39% |     0.16 |       75 | 38.31%     | ok               |
|          45 | -24.59%  | -84.23%            | -48.61% |    -0.13 |       52 | 18.39%     | ok               |

## FIL-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -5.26%   | -84.94%            | -39.40% |     0.11 |       48 | 23.37%     | ok               |
|          35 | -28.47%  | -84.94%            | -45.85% |    -0.23 |       58 | 27.39%     | ok               |
|          30 | -32.36%  | -84.94%            | -48.20% |    -0.27 |       70 | 32.76%     | ok               |
|          45 | -26.74%  | -84.94%            | -43.89% |    -0.27 |       44 | 17.62%     | ok               |
|          50 | -26.52%  | -84.94%            | -44.97% |    -0.32 |       38 | 13.03%     | ok               |

## FXI Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -12.94%  | 66.93%             | -22.99% |    -0.25 |       50 | 29.12%     | ok               |
|          30 | -13.44%  | 66.93%             | -24.33% |    -0.27 |       50 | 27.95%     | ok               |
|          15 | -14.37%  | 66.93%             | -21.68% |    -0.27 |       54 | 32.61%     | ok               |
|          50 | -12.29%  | 66.93%             | -24.39% |    -0.27 |       42 | 20.13%     | ok               |
|          45 | -14.49%  | 66.93%             | -26.75% |    -0.33 |       44 | 22.63%     | ok               |

## GDX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 17.87%   | 189.96%            | -31.87% |     0.41 |       64 | 43.09%     | ok               |
|          20 | 14.57%   | 189.96%            | -35.59% |     0.34 |       73 | 53.24%     | ok               |
|          35 | 10.02%   | 189.96%            | -32.37% |     0.29 |       68 | 45.59%     | ok               |
|          30 | 4.35%    | 189.96%            | -34.99% |     0.2  |       62 | 48.59%     | ok               |
|          25 | 3.61%    | 189.96%            | -33.46% |     0.19 |       63 | 50.08%     | ok               |

## GDXJ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -12.54%  | 210.21%            | -45.05% |    -0.01 |       67 | 53.41%     | ok               |
|          50 | -9.99%   | 210.21%            | -37.88% |    -0.04 |       56 | 37.27%     | ok               |
|          30 | -23.60%  | 210.21%            | -44.93% |    -0.24 |       68 | 46.42%     | ok               |
|          45 | -23.90%  | 210.21%            | -40.41% |    -0.29 |       62 | 39.77%     | ok               |
|          25 | -28.74%  | 210.21%            | -47.26% |    -0.3  |       73 | 49.75%     | ok               |

## GE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 28.66%   | 220.15%            | -22.29% |     0.59 |       66 | 38.44%     | ok               |
|          45 | 18.95%   | 220.15%            | -25.68% |     0.44 |       74 | 41.26%     | ok               |
|          20 | 18.07%   | 220.15%            | -26.63% |     0.4  |       69 | 55.07%     | ok               |
|          35 | 12.77%   | 220.15%            | -27.11% |     0.33 |       80 | 46.59%     | ok               |
|          15 | 13.03%   | 220.15%            | -28.62% |     0.33 |       68 | 57.40%     | ok               |

## GLD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | 29.06%   | 106.46%            | -14.61% |     0.72 |       46 | 45.26%     | ok               |
|          20 | 27.14%   | 106.46%            | -14.61% |     0.68 |       48 | 46.59%     | ok               |
|          30 | 22.92%   | 106.46%            | -16.63% |     0.61 |       48 | 44.09%     | ok               |
|          15 | 19.35%   | 106.46%            | -17.54% |     0.51 |       50 | 50.75%     | ok               |
|          35 | 16.92%   | 106.46%            | -17.29% |     0.48 |       50 | 43.43%     | ok               |

## GOOGL Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | 83.33%   | 146.37%            | -19.76% |     1.19 |       57 | 56.57%     | ok               |
|          30 | 74.57%   | 146.37%            | -20.41% |     1.12 |       63 | 54.41%     | ok               |
|          15 | 73.00%   | 146.37%            | -13.59% |     1.05 |       69 | 64.23%     | ok               |
|          20 | 69.48%   | 146.37%            | -20.57% |     1.04 |       68 | 58.90%     | ok               |
|          35 | 59.20%   | 146.37%            | -22.85% |     1    |       69 | 49.25%     | ok               |

## GRT-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 46.24%   | -90.29%            | -30.00% |     0.71 |       40 | 21.07%     | ok               |
|          45 | 14.37%   | -90.29%            | -48.76% |     0.36 |       48 | 25.86%     | ok               |
|          15 | 9.85%    | -90.29%            | -49.67% |     0.35 |       77 | 60.34%     | ok               |
|          20 | 9.24%    | -90.29%            | -46.47% |     0.33 |       85 | 55.36%     | ok               |
|          40 | 9.50%    | -90.29%            | -48.35% |     0.3  |       50 | 29.12%     | ok               |

## GS Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 26.28%   | 175.35%            | -20.56% |     0.55 |       74 | 59.57%     | ok               |
|          20 | 9.05%    | 175.35%            | -23.19% |     0.28 |       74 | 55.57%     | ok               |
|          25 | 3.53%    | 175.35%            | -23.32% |     0.17 |       74 | 53.08%     | ok               |
|          40 | -1.20%   | 175.35%            | -17.88% |     0.06 |       72 | 44.09%     | ok               |
|          30 | -2.56%   | 175.35%            | -22.13% |     0.05 |       76 | 50.75%     | ok               |

## HD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -4.50%   | -7.93%             | -17.69% |    -0.04 |       69 | 43.93%     | ok               |
|          25 | -5.24%   | -7.93%             | -18.51% |    -0.06 |       68 | 45.92%     | ok               |
|          40 | -10.14%  | -7.93%             | -19.63% |    -0.26 |       80 | 34.11%     | ok               |
|          35 | -13.39%  | -7.93%             | -22.98% |    -0.33 |       76 | 40.27%     | ok               |
|          45 | -13.53%  | -7.93%             | -21.41% |    -0.4  |       62 | 28.95%     | ok               |

## HON Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -17.09%  | 16.27%             | -23.31% |    -0.53 |       74 | 32.11%     | ok               |
|          45 | -19.07%  | 16.27%             | -22.37% |    -0.56 |       78 | 37.27%     | ok               |
|          40 | -27.04%  | 16.27%             | -27.04% |    -0.79 |       80 | 41.60%     | ok               |
|          35 | -28.43%  | 16.27%             | -28.43% |    -0.81 |       95 | 47.92%     | ok               |
|          30 | -30.77%  | 16.27%             | -30.77% |    -0.86 |       95 | 52.75%     | ok               |

## HYG Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -7.98%   | 3.51%              | -7.98%  |    -0.96 |       70 | 29.28%     | ok               |
|          15 | -9.44%   | 3.51%              | -10.29% |    -1.02 |       88 | 41.10%     | ok               |
|          20 | -9.18%   | 3.51%              | -10.29% |    -1.03 |       86 | 38.94%     | ok               |
|          25 | -9.38%   | 3.51%              | -10.11% |    -1.06 |       83 | 36.61%     | ok               |
|          30 | -9.08%   | 3.51%              | -9.59%  |    -1.06 |       81 | 33.94%     | ok               |

## IBIT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 63.57%   | -5.18%             | -19.20% |     1.07 |       38 | 37.99%     | ok               |
|          50 | 51.03%   | -5.18%             | -13.31% |     1.06 |       20 | 22.30%     | ok               |
|          45 | 42.63%   | -5.18%             | -17.12% |     0.91 |       22 | 23.04%     | ok               |
|          40 | 41.23%   | -5.18%             | -17.12% |     0.89 |       24 | 24.51%     | ok               |
|          30 | 34.78%   | -5.18%             | -18.95% |     0.75 |       32 | 30.15%     | ok               |

## IBM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 27.52%   | 57.52%             | -28.20% |     0.54 |       87 | 62.73%     | ok               |
|          30 | 23.04%   | 57.52%             | -25.31% |     0.51 |       72 | 50.92%     | ok               |
|          35 | 20.58%   | 57.52%             | -25.15% |     0.48 |       68 | 46.59%     | ok               |
|          45 | 16.40%   | 57.52%             | -18.33% |     0.42 |       54 | 37.27%     | ok               |
|          40 | 12.97%   | 57.52%             | -24.66% |     0.35 |       64 | 41.26%     | ok               |

## ICP-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 21.03%   | -75.89%            | -32.85% |     0.42 |       58 | 27.01%     | ok               |
|          35 | 8.38%    | -75.89%            | -46.49% |     0.31 |       68 | 32.18%     | ok               |
|          50 | 5.42%    | -75.89%            | -43.65% |     0.25 |       40 | 16.86%     | ok               |
|          30 | -4.95%   | -75.89%            | -56.10% |     0.22 |       83 | 38.51%     | ok               |
|          45 | -8.28%   | -75.89%            | -40.57% |     0.09 |       58 | 21.07%     | ok               |

## IEF Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -7.21%   | -1.10%             | -9.79%  |    -0.86 |       72 | 42.43%     | ok               |
|          15 | -7.76%   | -1.10%             | -10.52% |    -0.91 |       71 | 43.93%     | ok               |
|          40 | -8.39%   | -1.10%             | -9.67%  |    -1.31 |       60 | 24.79%     | ok               |
|          45 | -8.07%   | -1.10%             | -9.73%  |    -1.33 |       50 | 22.80%     | ok               |
|          25 | -10.78%  | -1.10%             | -11.19% |    -1.37 |       78 | 39.60%     | ok               |

## IEMG Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -0.10%   | 71.95%             | -13.91% |     0.05 |       52 | 34.44%     | ok               |
|          35 | -0.32%   | 71.95%             | -22.13% |     0.05 |       63 | 42.60%     | ok               |
|          45 | -0.91%   | 71.95%             | -14.92% |     0.02 |       48 | 36.94%     | ok               |
|          40 | -2.44%   | 71.95%             | -18.43% |    -0.03 |       60 | 39.93%     | ok               |
|          25 | -4.72%   | 71.95%             | -25.58% |    -0.09 |       59 | 45.42%     | ok               |

## INJ-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | -20.16%  | -76.35%            | -61.19% |    -0.01 |       60 | 32.38%     | ok               |
|          45 | -16.04%  | -76.35%            | -56.91% |    -0.02 |       44 | 22.22%     | ok               |
|          50 | -25.16%  | -76.35%            | -52.76% |    -0.19 |       48 | 19.16%     | ok               |
|          40 | -30.93%  | -76.35%            | -59.56% |    -0.21 |       50 | 28.35%     | ok               |
|          15 | -58.66%  | -76.35%            | -83.89% |    -0.45 |       82 | 50.38%     | ok               |

## INTC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 76.11%   | 158.34%            | -49.32% |     0.74 |       60 | 34.28%     | ok               |
|          15 | 82.95%   | 158.34%            | -53.65% |     0.74 |       84 | 61.23%     | ok               |
|          25 | 75.50%   | 158.34%            | -56.41% |     0.72 |       75 | 51.58%     | ok               |
|          40 | 70.33%   | 158.34%            | -55.86% |     0.7  |       68 | 38.60%     | ok               |
|          20 | 72.70%   | 158.34%            | -52.47% |     0.7  |       82 | 56.57%     | ok               |

## INTU Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 4.55%    | -56.12%            | -42.82% |     0.2  |       71 | 29.12%     | ok               |
|          45 | 0.97%    | -56.12%            | -44.66% |     0.14 |       69 | 33.28%     | ok               |
|          40 | -6.59%   | -56.12%            | -48.32% |    -0    |       69 | 35.94%     | ok               |
|          25 | -7.91%   | -56.12%            | -42.24% |    -0.01 |       64 | 45.26%     | ok               |
|          15 | -9.00%   | -56.12%            | -46.90% |    -0.02 |       79 | 50.75%     | ok               |

## ITA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 1.29%    | 91.36%             | -21.48% |     0.11 |       76 | 36.61%     | ok               |
|          15 | -3.39%   | 91.36%             | -28.17% |    -0    |       88 | 58.57%     | ok               |
|          30 | -2.80%   | 91.36%             | -23.75% |    -0.01 |       74 | 46.59%     | ok               |
|          35 | -5.30%   | 91.36%             | -23.16% |    -0.09 |       78 | 44.76%     | ok               |
|          40 | -6.39%   | 91.36%             | -20.58% |    -0.14 |       80 | 41.26%     | ok               |

## IWM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 8.72%    | 49.05%             | -12.83% |     0.36 |       50 | 37.10%     | ok               |
|          25 | 8.83%    | 49.05%             | -14.87% |     0.36 |       52 | 38.27%     | ok               |
|          40 | 6.51%    | 49.05%             | -14.38% |     0.31 |       44 | 32.45%     | ok               |
|          35 | 6.26%    | 49.05%             | -14.41% |     0.28 |       50 | 34.78%     | ok               |
|          20 | 4.54%    | 49.05%             | -15.39% |     0.22 |       62 | 39.27%     | ok               |

## JNJ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 19.30%   | 48.26%             | -10.57% |     0.82 |       58 | 37.27%     | ok               |
|          15 | 15.71%   | 48.26%             | -18.02% |     0.55 |       69 | 58.24%     | ok               |
|          45 | 10.36%   | 48.26%             | -13.35% |     0.46 |       60 | 42.43%     | ok               |
|          20 | 11.34%   | 48.26%             | -17.61% |     0.44 |       75 | 54.74%     | ok               |
|          40 | 7.95%    | 48.26%             | -14.77% |     0.35 |       66 | 46.59%     | ok               |

## JPM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 17.24%   | 88.54%             | -15.90% |     0.6  |       56 | 40.10%     | ok               |
|          45 | 7.12%    | 88.54%             | -21.91% |     0.28 |       56 | 43.26%     | ok               |
|          40 | -7.03%   | 88.54%             | -28.47% |    -0.14 |       68 | 45.76%     | ok               |
|          20 | -13.75%  | 88.54%             | -33.59% |    -0.23 |       88 | 57.07%     | ok               |
|          35 | -12.22%  | 88.54%             | -27.43% |    -0.28 |       74 | 49.42%     | ok               |

## KO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 27.92%   | 38.69%             | -8.07%  |     1    |       51 | 37.94%     | ok               |
|          35 | 24.00%   | 38.69%             | -8.07%  |     0.89 |       54 | 36.61%     | ok               |
|          40 | 21.41%   | 38.69%             | -9.28%  |     0.86 |       56 | 33.44%     | ok               |
|          25 | 22.64%   | 38.69%             | -9.37%  |     0.83 |       57 | 40.60%     | ok               |
|          50 | 14.81%   | 38.69%             | -11.40% |     0.68 |       36 | 26.79%     | ok               |

## LDO-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 30.57%   | -83.58%            | -43.71% |     0.51 |       89 | 48.08%     | ok               |
|          15 | 28.88%   | -83.58%            | -43.48% |     0.51 |       86 | 52.87%     | ok               |
|          30 | 17.46%   | -83.58%            | -58.32% |     0.41 |       76 | 38.70%     | ok               |
|          25 | 0.33%    | -83.58%            | -54.15% |     0.29 |       85 | 44.25%     | ok               |
|          35 | -5.01%   | -83.58%            | -63.16% |     0.2  |       78 | 31.42%     | ok               |

## LIN Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 3.11%    | 28.81%             | -23.70% |     0.16 |       65 | 49.92%     | ok               |
|          25 | 1.83%    | 28.81%             | -22.01% |     0.12 |       67 | 41.93%     | ok               |
|          20 | -0.35%   | 28.81%             | -23.00% |     0.05 |       66 | 45.09%     | ok               |
|          35 | -1.85%   | 28.81%             | -21.18% |    -0.01 |       66 | 32.61%     | ok               |
|          30 | -2.47%   | 28.81%             | -21.53% |    -0.03 |       70 | 39.10%     | ok               |

## LINK-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -13.55%  | -59.88%            | -50.48% |     0.1  |       70 | 41.57%     | ok               |
|          45 | -16.95%  | -59.88%            | -38.56% |    -0    |       50 | 26.25%     | ok               |
|          50 | -16.55%  | -59.88%            | -36.98% |    -0.02 |       40 | 20.88%     | ok               |
|          35 | -27.53%  | -59.88%            | -49.56% |    -0.1  |       60 | 36.40%     | ok               |
|          25 | -39.14%  | -59.88%            | -51.01% |    -0.19 |       68 | 47.51%     | ok               |

## LLY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 30.23%   | 79.59%             | -38.23% |     0.61 |       42 | 39.27%     | ok               |
|          45 | 17.74%   | 79.59%             | -42.66% |     0.41 |       50 | 42.43%     | ok               |
|          15 | 11.03%   | 79.59%             | -48.12% |     0.3  |       63 | 61.90%     | ok               |
|          40 | 0.13%    | 79.59%             | -46.23% |     0.13 |       62 | 44.93%     | ok               |
|          20 | -6.85%   | 79.59%             | -51.34% |     0.03 |       72 | 56.91%     | ok               |

## LRCX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 5.56%    | 340.06%            | -60.45% |     0.24 |       83 | 55.57%     | ok               |
|          50 | -0.52%   | 340.06%            | -50.39% |     0.14 |       80 | 37.44%     | ok               |
|          40 | -3.50%   | 340.06%            | -56.86% |     0.12 |       72 | 43.26%     | ok               |
|          35 | -9.77%   | 340.06%            | -61.76% |     0.04 |       80 | 45.26%     | ok               |
|          20 | -12.38%  | 340.06%            | -67.64% |     0.02 |       87 | 51.25%     | ok               |

## LTC-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -12.22%  | -56.64%            | -44.78% |    -0    |       56 | 31.80%     | ok               |
|          35 | -22.47%  | -56.64%            | -54.86% |    -0.13 |       66 | 42.91%     | ok               |
|          30 | -34.00%  | -56.64%            | -53.76% |    -0.29 |       66 | 48.47%     | ok               |
|          40 | -31.40%  | -56.64%            | -56.10% |    -0.3  |       58 | 38.12%     | ok               |
|          25 | -36.79%  | -56.64%            | -54.26% |    -0.33 |       74 | 50.96%     | ok               |

## MCD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 3.24%    | -4.56%             | -9.22%  |     0.2  |       42 | 20.47%     | ok               |
|          30 | -2.74%   | -4.56%             | -18.81% |    -0.06 |       77 | 38.44%     | ok               |
|          25 | -3.78%   | -4.56%             | -20.47% |    -0.09 |       77 | 41.10%     | ok               |
|          40 | -6.34%   | -4.56%             | -16.86% |    -0.25 |       73 | 28.95%     | ok               |
|          35 | -7.86%   | -4.56%             | -15.45% |    -0.29 |       69 | 34.78%     | ok               |

## META Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 11.51%   | 48.51%             | -31.03% |     0.3  |       66 | 40.60%     | ok               |
|          40 | -0.74%   | 48.51%             | -35.11% |     0.11 |       66 | 43.59%     | ok               |
|          50 | -5.51%   | 48.51%             | -34.00% |     0.02 |       70 | 36.77%     | ok               |
|          25 | -10.54%  | 48.51%             | -39.84% |    -0.03 |       67 | 54.24%     | ok               |
|          35 | -12.14%  | 48.51%             | -34.87% |    -0.07 |       77 | 48.42%     | ok               |

## MPC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 14.51%   | 70.67%             | -23.96% |     0.37 |       52 | 38.60%     | ok               |
|          45 | 7.25%    | 70.67%             | -25.09% |     0.24 |       58 | 42.26%     | ok               |
|          40 | 5.62%    | 70.67%             | -25.70% |     0.22 |       60 | 44.59%     | ok               |
|          35 | 2.36%    | 70.67%             | -35.90% |     0.16 |       68 | 47.09%     | ok               |
|          30 | -13.74%  | 70.67%             | -44.76% |    -0.14 |       71 | 49.92%     | ok               |

## MRK Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -13.30%  | -0.32%             | -29.92% |    -0.19 |       87 | 57.90%     | ok               |
|          25 | -12.88%  | -0.32%             | -31.07% |    -0.21 |       72 | 49.92%     | ok               |
|          20 | -17.15%  | -0.32%             | -29.39% |    -0.31 |       77 | 53.24%     | ok               |
|          50 | -16.01%  | -0.32%             | -22.98% |    -0.41 |       60 | 32.61%     | ok               |
|          45 | -17.61%  | -0.32%             | -23.33% |    -0.43 |       59 | 35.94%     | ok               |

## MS Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -4.17%   | 149.67%            | -19.99% |    -0.03 |       70 | 39.43%     | ok               |
|          35 | -10.90%  | 149.67%            | -25.26% |    -0.2  |       76 | 44.09%     | ok               |
|          15 | -15.53%  | 149.67%            | -23.50% |    -0.27 |       84 | 56.57%     | ok               |
|          20 | -15.99%  | 149.67%            | -25.68% |    -0.31 |       86 | 52.58%     | ok               |
|          30 | -16.30%  | 149.67%            | -27.79% |    -0.35 |       79 | 47.59%     | ok               |

## MSFT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -15.31%  | -1.46%             | -26.27% |    -0.41 |       64 | 35.61%     | ok               |
|          50 | -19.12%  | -1.46%             | -28.83% |    -0.56 |       62 | 30.95%     | ok               |
|          35 | -27.46%  | -1.46%             | -33.68% |    -0.72 |       73 | 43.93%     | ok               |
|          25 | -30.99%  | -1.46%             | -37.59% |    -0.77 |       85 | 51.58%     | ok               |
|          40 | -28.32%  | -1.46%             | -34.46% |    -0.78 |       69 | 38.94%     | ok               |

## MU Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 351.69%  | 999.97%            | -61.96% |     1.45 |       48 | 67.39%     | ok               |
|          25 | 276.31%  | 999.97%            | -67.90% |     1.36 |       49 | 61.06%     | ok               |
|          40 | 235.65%  | 999.97%            | -64.36% |     1.29 |       56 | 54.74%     | ok               |
|          20 | 244.52%  | 999.97%            | -67.25% |     1.27 |       55 | 63.23%     | ok               |
|          30 | 220.55%  | 999.97%            | -68.76% |     1.24 |       51 | 59.23%     | ok               |

## NEAR-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 103.12%  | -56.12%            | -48.01% |     0.99 |       44 | 23.37%     | ok               |
|          50 | 70.90%   | -56.12%            | -53.13% |     0.82 |       38 | 18.39%     | ok               |
|          40 | 60.91%   | -56.12%            | -56.35% |     0.73 |       48 | 27.78%     | ok               |
|          35 | 33.68%   | -56.12%            | -60.50% |     0.53 |       70 | 33.14%     | ok               |
|          15 | 2.00%    | -56.12%            | -54.94% |     0.31 |       89 | 56.13%     | ok               |

## NEM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 31.90%   | 186.37%            | -25.79% |     0.51 |       60 | 64.39%     | ok               |
|          20 | 19.49%   | 186.37%            | -30.47% |     0.39 |       72 | 59.90%     | ok               |
|          25 | -9.11%   | 186.37%            | -32.45% |     0.04 |       70 | 57.57%     | ok               |
|          50 | -13.06%  | 186.37%            | -33.36% |    -0.06 |       60 | 41.26%     | ok               |
|          30 | -26.80%  | 186.37%            | -38.49% |    -0.25 |       76 | 55.41%     | ok               |

## NFLX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 48.18%   | 65.41%             | -11.94% |     1.05 |       44 | 46.59%     | ok               |
|          50 | 35.59%   | 65.41%             | -16.28% |     0.88 |       46 | 39.10%     | ok               |
|          35 | 40.11%   | 65.41%             | -18.30% |     0.86 |       60 | 50.25%     | ok               |
|          45 | 32.16%   | 65.41%             | -15.48% |     0.78 |       50 | 42.93%     | ok               |
|          15 | 34.20%   | 65.41%             | -26.59% |     0.68 |       63 | 64.56%     | ok               |

## NKE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | -28.05%  | -55.32%            | -42.13% |    -0.4  |       77 | 37.60%     | ok               |
|          20 | -37.04%  | -55.32%            | -50.44% |    -0.49 |       97 | 53.41%     | ok               |
|          25 | -37.98%  | -55.32%            | -51.20% |    -0.52 |       95 | 49.42%     | ok               |
|          40 | -27.01%  | -55.32%            | -30.74% |    -0.52 |       67 | 29.95%     | ok               |
|          15 | -40.19%  | -55.32%            | -55.28% |    -0.55 |       98 | 58.07%     | ok               |

## NOW Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 20.60%   | -32.12%            | -26.36% |     0.4  |       79 | 51.91%     | ok               |
|          30 | 20.07%   | -32.12%            | -30.25% |     0.4  |       80 | 45.92%     | ok               |
|          35 | 15.42%   | -32.12%            | -29.30% |     0.36 |       79 | 40.77%     | ok               |
|          15 | 14.08%   | -32.12%            | -26.36% |     0.33 |       87 | 55.24%     | ok               |
|          25 | 13.25%   | -32.12%            | -25.70% |     0.32 |       72 | 49.25%     | ok               |

## NVDA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -4.92%   | 129.52%            | -33.22% |     0.1  |       68 | 51.69%     | ok               |
|          30 | -6.71%   | 129.52%            | -35.26% |     0.06 |       70 | 49.38%     | ok               |
|          20 | -11.23%  | 129.52%            | -40.59% |     0.03 |       71 | 56.15%     | ok               |
|          50 | -14.45%  | 129.52%            | -40.84% |    -0.11 |       60 | 33.51%     | ok               |
|          35 | -17.64%  | 129.52%            | -41.25% |    -0.13 |       82 | 46.52%     | ok               |

## OP-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 74.65%   | -93.85%            | -45.76% |     0.86 |       36 | 17.43%     | ok               |
|          50 | 66.86%   | -93.85%            | -36.11% |     0.86 |       34 | 12.45%     | ok               |
|          40 | 59.18%   | -93.85%            | -53.61% |     0.72 |       48 | 26.05%     | ok               |
|          35 | 32.48%   | -93.85%            | -58.33% |     0.52 |       56 | 29.12%     | ok               |
|          30 | 4.44%    | -93.85%            | -70.27% |     0.29 |       74 | 35.82%     | ok               |

## ORCL Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 142.69%  | 67.24%             | -25.87% |     1.06 |       72 | 65.06%     | ok               |
|          25 | 82.06%   | 67.24%             | -24.79% |     0.79 |       73 | 57.57%     | ok               |
|          20 | 78.93%   | 67.24%             | -25.87% |     0.77 |       75 | 60.73%     | ok               |
|          35 | 56.09%   | 67.24%             | -31.95% |     0.65 |       66 | 49.25%     | ok               |
|          30 | 56.23%   | 67.24%             | -29.47% |     0.65 |       72 | 53.41%     | ok               |

## OXY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 0.15%    | -0.35%             | -30.85% |     0.12 |       65 | 43.59%     | ok               |
|          35 | -0.66%   | -0.35%             | -30.50% |     0.1  |       68 | 38.60%     | ok               |
|          50 | -2.35%   | -0.35%             | -31.07% |     0.05 |       40 | 27.79%     | ok               |
|          40 | -3.09%   | -0.35%             | -32.21% |     0.05 |       56 | 34.61%     | ok               |
|          25 | -13.71%  | -0.35%             | -40.42% |    -0.13 |       73 | 47.09%     | ok               |

## PEP Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 9.77%    | -12.62%            | -11.62% |     0.45 |       46 | 27.79%     | ok               |
|          45 | 0.52%    | -12.62%            | -14.22% |     0.07 |       70 | 32.78%     | ok               |
|          40 | -3.01%   | -12.62%            | -18.04% |    -0.06 |       78 | 38.60%     | ok               |
|          35 | -4.60%   | -12.62%            | -21.42% |    -0.08 |       87 | 43.59%     | ok               |
|          30 | -9.64%   | -12.62%            | -21.35% |    -0.22 |       85 | 50.25%     | ok               |

## PEPE-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 12.84%   | -83.66%            | -57.66% |     0.38 |       77 | 43.87%     | ok               |
|          35 | 4.07%    | -83.66%            | -51.35% |     0.29 |       62 | 38.51%     | ok               |
|          25 | -12.31%  | -83.66%            | -56.30% |     0.17 |       85 | 49.23%     | ok               |
|          15 | -29.05%  | -83.66%            | -65.75% |     0.09 |       81 | 58.81%     | ok               |
|          50 | -15.28%  | -83.66%            | -39.43% |     0.01 |       54 | 22.03%     | ok               |

## PFE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -20.94%  | -7.42%             | -25.65% |    -0.71 |       52 | 21.63%     | ok               |
|          50 | -23.34%  | -7.42%             | -26.92% |    -0.88 |       44 | 17.80%     | ok               |
|          40 | -27.64%  | -7.42%             | -31.95% |    -0.91 |       76 | 26.46%     | ok               |
|          35 | -31.33%  | -7.42%             | -36.39% |    -0.98 |       82 | 33.28%     | ok               |
|          30 | -37.69%  | -7.42%             | -42.29% |    -1.17 |       77 | 36.77%     | ok               |

## PG Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 0.88%    | 1.18%              | -19.77% |     0.09 |       52 | 34.78%     | ok               |
|          35 | -1.36%   | 1.18%              | -18.66% |    -0    |       60 | 38.10%     | ok               |
|          30 | -10.32%  | 1.18%              | -21.65% |    -0.36 |       62 | 41.26%     | ok               |
|          45 | -8.97%   | 1.18%              | -20.43% |    -0.36 |       52 | 32.28%     | ok               |
|          25 | -11.40%  | 1.18%              | -22.55% |    -0.4  |       72 | 42.43%     | ok               |

## PM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 4.79%    | 99.39%             | -32.20% |     0.2  |       88 | 53.08%     | ok               |
|          20 | 2.40%    | 99.39%             | -31.89% |     0.15 |       87 | 61.90%     | ok               |
|          30 | 1.42%    | 99.39%             | -33.68% |     0.13 |       81 | 57.07%     | ok               |
|          25 | -4.92%   | 99.39%             | -37.05% |    -0.01 |       81 | 59.23%     | ok               |
|          50 | -4.61%   | 99.39%             | -35.70% |    -0.03 |       74 | 42.10%     | ok               |

## POL-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 67.37%   | -83.30%            | -46.45% |     0.78 |       79 | 49.23%     | ok               |
|          25 | 60.86%   | -83.30%            | -46.72% |     0.72 |       70 | 57.85%     | ok               |
|          20 | 50.02%   | -83.30%            | -52.88% |     0.64 |       78 | 63.03%     | ok               |
|          15 | 38.09%   | -83.30%            | -58.42% |     0.56 |       78 | 68.58%     | ok               |
|          50 | 22.79%   | -83.30%            | -22.86% |     0.48 |       50 | 20.69%     | ok               |

## QCOM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -6.64%   | 38.50%             | -55.66% |     0.09 |       73 | 50.08%     | ok               |
|          35 | -8.83%   | 38.50%             | -51.84% |     0.05 |       83 | 45.42%     | ok               |
|          20 | -13.47%  | 38.50%             | -57.05% |     0    |       70 | 53.08%     | ok               |
|          30 | -18.79%  | 38.50%             | -57.69% |    -0.09 |       77 | 48.09%     | ok               |
|          15 | -27.85%  | 38.50%             | -60.40% |    -0.2  |       74 | 56.24%     | ok               |

## QQQ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | 20.48%   | 71.04%             | -12.88% |     0.57 |       57 | 49.08%     | ok               |
|          15 | 21.00%   | 71.04%             | -14.17% |     0.54 |       61 | 54.58%     | ok               |
|          20 | 17.56%   | 71.04%             | -12.98% |     0.49 |       65 | 51.75%     | ok               |
|          30 | 15.53%   | 71.04%             | -12.88% |     0.47 |       62 | 46.09%     | ok               |
|          35 | 3.72%    | 71.04%             | -19.00% |     0.18 |       68 | 42.43%     | ok               |

## RENDER-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 49.19%   | -56.75%            | -43.43% |     0.65 |       84 | 54.79%     | ok               |
|          15 | 31.87%   | -56.75%            | -44.59% |     0.55 |       84 | 57.92%     | ok               |
|          25 | 19.62%   | -56.75%            | -40.60% |     0.46 |       88 | 50.83%     | ok               |
|          30 | -17.88%  | -56.75%            | -45.00% |     0.11 |       96 | 44.38%     | ok               |
|          40 | -27.22%  | -56.75%            | -38.60% |    -0.1  |       70 | 29.58%     | ok               |

## RTX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 26.34%   | 115.87%            | -18.66% |     0.66 |       74 | 55.91%     | ok               |
|          50 | 18.86%   | 115.87%            | -18.42% |     0.61 |       54 | 41.76%     | ok               |
|          25 | 21.63%   | 115.87%            | -18.59% |     0.57 |       62 | 52.58%     | ok               |
|          30 | 19.78%   | 115.87%            | -16.99% |     0.54 |       56 | 51.41%     | ok               |
|          35 | 17.19%   | 115.87%            | -18.00% |     0.53 |       52 | 49.42%     | ok               |

## SBUX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -14.56%  | 10.71%             | -23.55% |    -0.23 |       65 | 40.77%     | ok               |
|          40 | -18.26%  | 10.71%             | -25.43% |    -0.39 |       58 | 31.95%     | ok               |
|          45 | -17.36%  | 10.71%             | -27.26% |    -0.4  |       62 | 28.12%     | ok               |
|          30 | -21.86%  | 10.71%             | -29.34% |    -0.43 |       64 | 38.44%     | ok               |
|          35 | -23.87%  | 10.71%             | -30.25% |    -0.51 |       58 | 35.44%     | ok               |

## SCHW Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 2.59%    | 43.17%             | -15.92% |     0.15 |       54 | 33.44%     | ok               |
|          50 | -1.42%   | 43.17%             | -11.75% |     0.01 |       50 | 30.95%     | ok               |
|          40 | -8.05%   | 43.17%             | -21.81% |    -0.15 |       62 | 36.44%     | ok               |
|          25 | -10.23%  | 43.17%             | -28.76% |    -0.16 |       61 | 47.75%     | ok               |
|          20 | -11.91%  | 43.17%             | -29.24% |    -0.2  |       69 | 50.42%     | ok               |

## SHIB-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -2.62%   | -76.82%            | -49.21% |     0.22 |       76 | 68.01%     | ok               |
|          25 | -10.40%  | -76.82%            | -43.85% |     0.12 |       75 | 59.00%     | ok               |
|          20 | -14.31%  | -76.82%            | -46.92% |     0.09 |       79 | 63.79%     | ok               |
|          35 | -13.56%  | -76.82%            | -53.32% |     0.05 |       64 | 46.17%     | ok               |
|          40 | -18.30%  | -76.82%            | -50.74% |    -0.03 |       54 | 38.51%     | ok               |

## SHY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd    |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:-------|---------:|---------:|:-----------|:-----------------|
|          30 | -2.17%   | 0.00%              | -2.85% |    -0.75 |       50 | 35.61%     | ok               |
|          35 | -2.28%   | 0.00%              | -3.27% |    -0.8  |       52 | 33.78%     | ok               |
|          40 | -2.40%   | 0.00%              | -3.33% |    -0.85 |       52 | 31.95%     | ok               |
|          45 | -2.38%   | 0.00%              | -3.23% |    -0.86 |       50 | 28.79%     | ok               |
|          50 | -2.55%   | 0.00%              | -3.40% |    -0.97 |       46 | 25.96%     | ok               |

## SKY-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -33.14%  | -0.99%             | -56.39% |    -0.37 |       58 | 50.83%     | ok               |
|          30 | -29.04%  | -0.99%             | -43.98% |    -0.37 |       68 | 40.66%     | ok               |
|          25 | -32.68%  | -0.99%             | -48.09% |    -0.43 |       63 | 44.44%     | ok               |
|          20 | -42.94%  | -0.99%             | -58.40% |    -0.63 |       60 | 48.23%     | ok               |
|          35 | -39.62%  | -0.99%             | -49.68% |    -0.72 |       60 | 34.52%     | ok               |

## SLB Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 12.74%   | 10.85%             | -23.07% |     0.35 |       46 | 35.44%     | ok               |
|          45 | 11.08%   | 10.85%             | -20.46% |     0.33 |       52 | 32.11%     | ok               |
|          50 | -8.84%   | 10.85%             | -28.89% |    -0.13 |       52 | 28.45%     | ok               |
|          35 | -15.57%  | 10.85%             | -41.81% |    -0.22 |       74 | 43.43%     | ok               |
|          30 | -30.05%  | 10.85%             | -54.95% |    -0.54 |       75 | 49.92%     | ok               |

## SLV Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 56.72%   | 203.12%            | -34.10% |     0.78 |       50 | 32.95%     | ok               |
|          40 | 55.54%   | 203.12%            | -29.75% |     0.76 |       62 | 35.94%     | ok               |
|          45 | 51.78%   | 203.12%            | -31.82% |     0.73 |       56 | 33.94%     | ok               |
|          35 | 41.98%   | 203.12%            | -36.89% |     0.64 |       64 | 38.27%     | ok               |
|          30 | 26.46%   | 203.12%            | -42.66% |     0.48 |       60 | 40.27%     | ok               |

## SMH Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 119.88%  | 229.68%            | -30.17% |     1.34 |       47 | 53.91%     | ok               |
|          35 | 96.79%   | 229.68%            | -34.36% |     1.22 |       54 | 49.75%     | ok               |
|          25 | 96.64%   | 229.68%            | -32.94% |     1.2  |       46 | 52.75%     | ok               |
|          30 | 94.32%   | 229.68%            | -33.99% |     1.19 |       48 | 51.08%     | ok               |
|          45 | 80.19%   | 229.68%            | -32.75% |     1.14 |       52 | 43.93%     | ok               |

## SNX-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 28.58%   | -86.52%            | -28.28% |     0.5  |       68 | 32.95%     | ok               |
|          30 | 22.00%   | -86.52%            | -32.91% |     0.44 |       63 | 40.61%     | ok               |
|          20 | 17.96%   | -86.52%            | -43.20% |     0.42 |       71 | 50.96%     | ok               |
|          25 | -2.64%   | -86.52%            | -36.77% |     0.23 |       74 | 45.02%     | ok               |
|          15 | -20.43%  | -86.52%            | -47.56% |     0.09 |       81 | 54.98%     | ok               |

## SOL-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -12.19%  | -62.33%            | -51.20% |     0.11 |       64 | 39.46%     | ok               |
|          25 | -27.16%  | -62.33%            | -51.71% |    -0.02 |       72 | 57.47%     | ok               |
|          35 | -28.55%  | -62.33%            | -59.05% |    -0.06 |       72 | 46.93%     | ok               |
|          15 | -34.71%  | -62.33%            | -57.85% |    -0.1  |       78 | 64.75%     | ok               |
|          20 | -37.63%  | -62.33%            | -55.52% |    -0.15 |       68 | 59.96%     | ok               |

## SOXX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 95.21%   | 196.54%            | -38.67% |     1.13 |       53 | 52.58%     | ok               |
|          25 | 91.48%   | 196.54%            | -39.85% |     1.1  |       51 | 52.25%     | ok               |
|          35 | 86.13%   | 196.54%            | -38.63% |     1.08 |       59 | 47.59%     | ok               |
|          15 | 90.31%   | 196.54%            | -37.72% |     1.06 |       66 | 55.41%     | ok               |
|          30 | 80.72%   | 196.54%            | -40.34% |     1.02 |       55 | 50.08%     | ok               |

## SPY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 18.02%   | 53.43%             | -14.25% |     0.62 |       56 | 53.91%     | ok               |
|          15 | 16.85%   | 53.43%             | -16.80% |     0.57 |       63 | 56.91%     | ok               |
|          25 | 11.22%   | 53.43%             | -15.22% |     0.42 |       56 | 53.24%     | ok               |
|          30 | 7.21%    | 53.43%             | -16.47% |     0.31 |       58 | 50.75%     | ok               |
|          35 | 3.93%    | 53.43%             | -16.72% |     0.2  |       58 | 48.25%     | ok               |

## SUSHI-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -24.39%  | -88.01%            | -40.79% |    -0.2  |       52 | 14.56%     | ok               |
|          45 | -56.30%  | -88.01%            | -64.69% |    -0.71 |       54 | 17.82%     | ok               |
|          40 | -59.39%  | -88.01%            | -66.97% |    -0.72 |       61 | 24.33%     | ok               |
|          35 | -67.00%  | -88.01%            | -75.30% |    -0.85 |       76 | 29.69%     | ok               |
|          15 | -80.29%  | -88.01%            | -81.81% |    -1    |       90 | 47.32%     | ok               |

## T Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 49.42%   | 40.36%             | -18.13% |     1.03 |       57 | 54.74%     | ok               |
|          25 | 41.76%   | 40.36%             | -17.66% |     0.92 |       62 | 52.41%     | ok               |
|          15 | 41.26%   | 40.36%             | -15.08% |     0.88 |       66 | 58.57%     | ok               |
|          35 | 29.04%   | 40.36%             | -14.49% |     0.73 |       64 | 46.92%     | ok               |
|          30 | 27.61%   | 40.36%             | -17.01% |     0.69 |       64 | 50.25%     | ok               |

## TGT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -6.81%   | -3.65%             | -40.99% |    -0.02 |       77 | 45.92%     | ok               |
|          15 | -9.86%   | -3.65%             | -38.83% |    -0.07 |       67 | 50.42%     | ok               |
|          25 | -10.93%  | -3.65%             | -43.53% |    -0.13 |       61 | 41.26%     | ok               |
|          45 | -10.17%  | -3.65%             | -30.47% |    -0.16 |       50 | 28.95%     | ok               |
|          30 | -11.79%  | -3.65%             | -41.74% |    -0.16 |       56 | 38.60%     | ok               |

## TIA-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 28.97%   | -92.82%            | -41.15% |     0.49 |       60 | 29.31%     | ok               |
|          40 | 22.57%   | -92.82%            | -40.83% |     0.44 |       60 | 25.10%     | ok               |
|          50 | 13.81%   | -92.82%            | -44.86% |     0.36 |       32 | 11.49%     | ok               |
|          45 | 13.67%   | -92.82%            | -45.20% |     0.35 |       52 | 18.77%     | ok               |
|          30 | -14.40%  | -92.82%            | -55.60% |     0.1  |       82 | 33.72%     | ok               |

## TLT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -12.97%  | -9.38%             | -16.02% |    -1.38 |       34 | 14.48%     | ok               |
|          30 | -21.90%  | -9.38%             | -23.75% |    -1.6  |       70 | 32.45%     | ok               |
|          45 | -16.42%  | -9.38%             | -19.55% |    -1.67 |       42 | 17.30%     | ok               |
|          40 | -18.31%  | -9.38%             | -20.25% |    -1.67 |       60 | 21.30%     | ok               |
|          35 | -21.35%  | -9.38%             | -23.22% |    -1.77 |       66 | 26.46%     | ok               |

## TMO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 39.91%   | -15.19%            | -10.55% |     0.92 |       38 | 30.45%     | ok               |
|          45 | 38.67%   | -15.19%            | -12.29% |     0.87 |       46 | 35.61%     | ok               |
|          40 | 36.63%   | -15.19%            | -12.07% |     0.82 |       49 | 40.10%     | ok               |
|          35 | 21.65%   | -15.19%            | -16.12% |     0.53 |       59 | 44.26%     | ok               |
|          30 | 13.37%   | -15.19%            | -16.83% |     0.37 |       57 | 48.42%     | ok               |

## TMUS Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 12.52%   | 15.04%             | -26.87% |     0.35 |       69 | 60.23%     | ok               |
|          30 | 11.16%   | 15.04%             | -24.50% |     0.33 |       70 | 48.59%     | ok               |
|          20 | 5.61%    | 15.04%             | -24.82% |     0.22 |       71 | 54.58%     | ok               |
|          25 | 4.56%    | 15.04%             | -25.91% |     0.19 |       75 | 50.92%     | ok               |
|          50 | 2.92%    | 15.04%             | -22.71% |     0.16 |       60 | 36.11%     | ok               |

## TRX-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 2.00%    | 30.96%             | -22.90% |     0.14 |       70 | 48.66%     | ok               |
|          40 | 1.22%    | 30.96%             | -18.79% |     0.12 |       52 | 37.74%     | ok               |
|          35 | 0.61%    | 30.96%             | -21.77% |     0.11 |       66 | 45.98%     | ok               |
|          25 | 0.17%    | 30.96%             | -26.84% |     0.1  |       66 | 51.92%     | ok               |
|          50 | -0.25%   | 30.96%             | -18.49% |     0.07 |       44 | 32.38%     | ok               |

## TSLA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 83.42%   | 94.65%             | -32.60% |     0.92 |       64 | 31.28%     | ok               |
|          40 | 74.18%   | 94.65%             | -45.90% |     0.8  |       61 | 35.77%     | ok               |
|          45 | 47.57%   | 94.65%             | -46.86% |     0.62 |       65 | 33.11%     | ok               |
|          35 | 27.00%   | 94.65%             | -54.51% |     0.45 |       74 | 38.77%     | ok               |
|          30 | 3.12%    | 94.65%             | -57.89% |     0.24 |       68 | 43.26%     | ok               |

## TXN Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 13.38%   | 72.24%             | -45.45% |     0.33 |       72 | 35.77%     | ok               |
|          20 | 2.88%    | 72.24%             | -38.98% |     0.19 |       62 | 59.90%     | ok               |
|          15 | 0.75%    | 72.24%             | -39.48% |     0.17 |       65 | 64.06%     | ok               |
|          35 | -5.44%   | 72.24%             | -43.38% |     0.05 |       78 | 50.42%     | ok               |
|          40 | -6.08%   | 72.24%             | -45.67% |     0.04 |       76 | 48.25%     | ok               |

## UNH Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 27.87%   | -20.36%            | -36.70% |     0.52 |       50 | 28.29%     | ok               |
|          30 | 23.27%   | -20.36%            | -27.74% |     0.45 |       76 | 51.58%     | ok               |
|          35 | 18.72%   | -20.36%            | -29.80% |     0.39 |       70 | 46.26%     | ok               |
|          15 | 18.93%   | -20.36%            | -31.43% |     0.39 |       79 | 66.56%     | ok               |
|          20 | 16.11%   | -20.36%            | -31.00% |     0.36 |       81 | 61.40%     | ok               |

## UNI-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -1.77%   | -81.58%            | -57.12% |     0.21 |       52 | 25.10%     | ok               |
|          40 | -11.32%  | -81.58%            | -63.75% |     0.11 |       54 | 30.08%     | ok               |
|          50 | -10.68%  | -81.58%            | -54.53% |     0.08 |       50 | 20.50%     | ok               |
|          35 | -24.11%  | -81.58%            | -68.58% |    -0.01 |       72 | 34.87%     | ok               |
|          20 | -67.02%  | -81.58%            | -80.81% |    -0.6  |       99 | 51.53%     | ok               |

## UPS Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -34.15%  | -31.84%            | -42.25% |    -0.64 |       74 | 44.09%     | ok               |
|          35 | -33.05%  | -31.84%            | -40.47% |    -0.65 |       59 | 33.78%     | ok               |
|          20 | -35.25%  | -31.84%            | -45.77% |    -0.66 |       80 | 47.25%     | ok               |
|          30 | -35.51%  | -31.84%            | -40.62% |    -0.7  |       66 | 39.43%     | ok               |
|          40 | -34.39%  | -31.84%            | -42.12% |    -0.71 |       51 | 28.62%     | ok               |

## USO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 10.72%   | 79.98%             | -33.68% |     0.3  |       48 | 27.12%     | ok               |
|          30 | 2.80%    | 79.98%             | -43.35% |     0.17 |       68 | 34.44%     | ok               |
|          40 | -0.60%   | 79.98%             | -41.14% |     0.11 |       59 | 29.78%     | ok               |
|          25 | -1.49%   | 79.98%             | -45.72% |     0.11 |       70 | 37.10%     | ok               |
|          20 | -1.60%   | 79.98%             | -45.77% |     0.11 |       74 | 39.27%     | ok               |

## VEA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 5.44%    | 52.56%             | -16.28% |     0.25 |       60 | 50.58%     | ok               |
|          20 | 1.19%    | 52.56%             | -17.70% |     0.1  |       61 | 47.92%     | ok               |
|          25 | -0.82%   | 52.56%             | -17.79% |     0.02 |       57 | 46.26%     | ok               |
|          30 | -0.98%   | 52.56%             | -17.93% |     0.01 |       58 | 44.09%     | ok               |
|          35 | -2.09%   | 52.56%             | -16.79% |    -0.03 |       56 | 43.09%     | ok               |

## VIXY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -46.17%  | -59.62%            | -68.69% |    -0.39 |       44 | 10.32%     | ok               |
|          45 | -56.13%  | -59.62%            | -74.13% |    -0.55 |       56 | 16.31%     | ok               |
|          40 | -64.59%  | -59.62%            | -80.10% |    -0.66 |       70 | 20.47%     | ok               |
|          35 | -68.29%  | -59.62%            | -83.87% |    -0.7  |       86 | 25.62%     | ok               |
|          15 | -78.52%  | -59.62%            | -89.47% |    -0.83 |      101 | 43.43%     | ok               |

## VNQ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -8.60%   | 14.67%             | -19.07% |    -0.37 |       60 | 28.62%     | ok               |
|          50 | -9.03%   | 14.67%             | -17.13% |    -0.41 |       56 | 26.12%     | ok               |
|          25 | -13.12%  | 14.67%             | -22.34% |    -0.51 |       69 | 40.77%     | ok               |
|          40 | -14.13%  | 14.67%             | -24.84% |    -0.62 |       74 | 32.11%     | ok               |
|          20 | -17.14%  | 14.67%             | -23.79% |    -0.67 |       76 | 43.76%     | ok               |

## VTI Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 17.38%   | 52.28%             | -13.96% |     0.59 |       60 | 55.57%     | ok               |
|          15 | 11.37%   | 52.28%             | -15.70% |     0.41 |       63 | 58.07%     | ok               |
|          25 | 6.34%    | 52.28%             | -16.10% |     0.27 |       58 | 53.91%     | ok               |
|          30 | -0.72%   | 52.28%             | -18.77% |     0.04 |       66 | 52.08%     | ok               |
|          40 | -2.95%   | 52.28%             | -20.44% |    -0.05 |       68 | 45.42%     | ok               |

## VWO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -9.03%   | 51.45%             | -24.01% |    -0.26 |       69 | 49.42%     | ok               |
|          50 | -7.89%   | 51.45%             | -21.68% |    -0.28 |       60 | 32.45%     | ok               |
|          20 | -10.06%  | 51.45%             | -26.14% |    -0.31 |       67 | 47.25%     | ok               |
|          40 | -8.98%   | 51.45%             | -23.57% |    -0.31 |       70 | 37.94%     | ok               |
|          45 | -9.69%   | 51.45%             | -23.75% |    -0.35 |       62 | 34.94%     | ok               |

## VZ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 0.45%    | 21.55%             | -16.98% |     0.08 |       50 | 26.12%     | ok               |
|          45 | -6.49%   | 21.55%             | -20.38% |    -0.15 |       56 | 28.95%     | ok               |
|          35 | -12.02%  | 21.55%             | -24.68% |    -0.33 |       59 | 34.44%     | ok               |
|          25 | -15.31%  | 21.55%             | -28.84% |    -0.4  |       76 | 42.26%     | ok               |
|          40 | -15.07%  | 21.55%             | -26.72% |    -0.45 |       62 | 31.45%     | ok               |

## WFC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -1.11%   | 72.53%             | -18.29% |     0.03 |       58 | 32.45%     | ok               |
|          35 | -5.71%   | 72.53%             | -23.64% |    -0.05 |       81 | 44.09%     | ok               |
|          45 | -7.66%   | 72.53%             | -23.40% |    -0.16 |       64 | 36.77%     | ok               |
|          20 | -15.43%  | 72.53%             | -29.43% |    -0.21 |       81 | 53.41%     | ok               |
|          40 | -10.33%  | 72.53%             | -24.26% |    -0.23 |       76 | 40.27%     | ok               |

## WIF-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 47.92%   | -89.47%            | -46.21% |     0.61 |       73 | 42.34%     | ok               |
|          20 | 45.96%   | -89.47%            | -40.67% |     0.59 |       67 | 39.85%     | ok               |
|          25 | -3.75%   | -89.47%            | -45.19% |     0.27 |       73 | 37.16%     | ok               |
|          30 | -34.81%  | -89.47%            | -50.40% |    -0.1  |       72 | 32.95%     | ok               |
|          50 | -20.06%  | -89.47%            | -37.87% |    -0.14 |       40 | 12.07%     | ok               |

## WMT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 63.69%   | 123.61%            | -9.18%  |     1.61 |       36 | 44.76%     | ok               |
|          50 | 57.04%   | 123.61%            | -12.19% |     1.55 |       30 | 42.60%     | ok               |
|          40 | 53.46%   | 123.61%            | -9.18%  |     1.38 |       40 | 45.92%     | ok               |
|          35 | 54.73%   | 123.61%            | -9.11%  |     1.37 |       48 | 49.58%     | ok               |
|          30 | 32.33%   | 123.61%            | -21.31% |     0.85 |       55 | 52.08%     | ok               |

## XBI Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 3.96%    | 50.31%             | -16.71% |     0.18 |       60 | 34.61%     | ok               |
|          45 | 3.16%    | 50.31%             | -16.88% |     0.16 |       52 | 31.45%     | ok               |
|          35 | -3.05%   | 50.31%             | -21.38% |     0.01 |       62 | 37.77%     | ok               |
|          30 | -4.13%   | 50.31%             | -21.75% |    -0.02 |       62 | 39.43%     | ok               |
|          50 | -5.14%   | 50.31%             | -16.83% |    -0.07 |       54 | 28.29%     | ok               |

## XLB Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -4.67%   | 26.54%             | -20.60% |    -0.12 |       60 | 32.11%     | ok               |
|          50 | -4.61%   | 26.54%             | -17.40% |    -0.14 |       44 | 27.79%     | ok               |
|          35 | -7.91%   | 26.54%             | -23.62% |    -0.24 |       60 | 35.61%     | ok               |
|          45 | -7.43%   | 26.54%             | -20.61% |    -0.25 |       44 | 29.28%     | ok               |
|          25 | -12.47%  | 26.54%             | -23.87% |    -0.4  |       68 | 41.26%     | ok               |

## XLC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 16.62%   | 48.91%             | -12.33% |     0.57 |       63 | 55.74%     | ok               |
|          25 | 14.42%   | 48.91%             | -12.31% |     0.5  |       60 | 57.57%     | ok               |
|          40 | 11.32%   | 48.91%             | -13.38% |     0.44 |       66 | 48.25%     | ok               |
|          35 | 11.30%   | 48.91%             | -13.38% |     0.44 |       62 | 52.75%     | ok               |
|          20 | 6.38%    | 48.91%             | -13.78% |     0.26 |       68 | 60.23%     | ok               |

## XLE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -1.92%   | 43.03%             | -25.98% |     0.02 |       56 | 36.77%     | ok               |
|          35 | -3.79%   | 43.03%             | -32.17% |    -0.02 |       65 | 44.59%     | ok               |
|          45 | -5.17%   | 43.03%             | -30.88% |    -0.07 |       62 | 39.60%     | ok               |
|          25 | -9.70%   | 43.03%             | -36.16% |    -0.16 |       81 | 49.92%     | ok               |
|          30 | -9.72%   | 43.03%             | -36.18% |    -0.17 |       73 | 46.76%     | ok               |

## XLF Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -4.13%   | 39.96%             | -18.01% |    -0.08 |       68 | 54.58%     | ok               |
|          15 | -8.09%   | 39.96%             | -19.58% |    -0.21 |       76 | 57.40%     | ok               |
|          25 | -10.56%  | 39.96%             | -23.22% |    -0.33 |       75 | 51.25%     | ok               |
|          30 | -11.20%  | 39.96%             | -23.61% |    -0.36 |       74 | 48.75%     | ok               |
|          35 | -18.33%  | 39.96%             | -27.41% |    -0.73 |       64 | 44.59%     | ok               |

## XLI Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 11.97%   | 55.47%             | -10.36% |     0.46 |       72 | 54.41%     | ok               |
|          50 | 6.67%    | 55.47%             | -9.25%  |     0.34 |       56 | 35.94%     | ok               |
|          20 | 7.65%    | 55.47%             | -12.74% |     0.33 |       63 | 49.42%     | ok               |
|          45 | 5.61%    | 55.47%             | -12.27% |     0.29 |       62 | 38.27%     | ok               |
|          30 | 5.29%    | 55.47%             | -11.38% |     0.26 |       64 | 46.92%     | ok               |

## XLK Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 83.89%   | 83.83%             | -14.75% |     1.35 |       41 | 54.08%     | ok               |
|          20 | 69.50%   | 83.83%             | -14.75% |     1.21 |       48 | 51.91%     | ok               |
|          25 | 66.05%   | 83.83%             | -14.75% |     1.21 |       42 | 49.75%     | ok               |
|          30 | 63.88%   | 83.83%             | -14.75% |     1.2  |       42 | 48.59%     | ok               |
|          35 | 45.59%   | 83.83%             | -13.61% |     0.96 |       54 | 45.92%     | ok               |

## XLM-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 46.59%   | -54.70%            | -32.06% |     0.65 |       44 | 28.16%     | ok               |
|          45 | 42.18%   | -54.70%            | -37.64% |     0.61 |       50 | 31.80%     | ok               |
|          30 | 14.82%   | -54.70%            | -45.54% |     0.37 |       69 | 45.79%     | ok               |
|          15 | 7.97%    | -54.70%            | -41.37% |     0.32 |       87 | 58.24%     | ok               |
|          20 | 8.33%    | -54.70%            | -44.44% |     0.32 |       77 | 51.53%     | ok               |

## XLP Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 11.12%   | 19.69%             | -5.66%  |     0.68 |       56 | 33.94%     | ok               |
|          50 | 9.69%    | 19.69%             | -6.08%  |     0.61 |       58 | 31.78%     | ok               |
|          40 | 8.89%    | 19.69%             | -7.77%  |     0.54 |       72 | 38.10%     | ok               |
|          35 | 7.94%    | 19.69%             | -9.73%  |     0.48 |       68 | 41.10%     | ok               |
|          30 | 5.69%    | 19.69%             | -10.28% |     0.35 |       72 | 42.93%     | ok               |

## XLU Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 5.66%    | 46.79%             | -9.11%  |     0.31 |       50 | 30.95%     | ok               |
|          45 | 3.49%    | 46.79%             | -10.56% |     0.21 |       54 | 31.95%     | ok               |
|          40 | 0.19%    | 46.79%             | -11.94% |     0.05 |       60 | 33.61%     | ok               |
|          35 | -4.80%   | 46.79%             | -16.24% |    -0.18 |       64 | 36.11%     | ok               |
|          30 | -7.05%   | 46.79%             | -18.13% |    -0.28 |       69 | 39.27%     | ok               |

## XLV Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -10.16%  | 9.81%              | -15.55% |    -0.48 |       68 | 36.77%     | ok               |
|          25 | -11.49%  | 9.81%              | -16.79% |    -0.55 |       70 | 38.10%     | ok               |
|          15 | -14.97%  | 9.81%              | -20.26% |    -0.71 |       79 | 43.09%     | ok               |
|          20 | -14.90%  | 9.81%              | -20.35% |    -0.73 |       73 | 39.93%     | ok               |
|          35 | -14.86%  | 9.81%              | -19.74% |    -0.79 |       66 | 34.28%     | ok               |

## XLY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 2.60%    | 33.93%             | -12.94% |     0.15 |       74 | 41.60%     | ok               |
|          30 | 0.76%    | 33.93%             | -14.01% |     0.09 |       74 | 44.59%     | ok               |
|          15 | -0.76%   | 33.93%             | -15.77% |     0.05 |       76 | 51.58%     | ok               |
|          50 | -0.60%   | 33.93%             | -11.79% |     0.03 |       52 | 29.78%     | ok               |
|          40 | -3.75%   | 33.93%             | -16.99% |    -0.07 |       70 | 37.27%     | ok               |

## XOM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | 2.30%    | 51.84%             | -19.90% |     0.14 |       58 | 37.10%     | ok               |
|          50 | 1.92%    | 51.84%             | -21.35% |     0.13 |       46 | 29.95%     | ok               |
|          30 | 1.28%    | 51.84%             | -20.29% |     0.11 |       58 | 36.44%     | ok               |
|          20 | -1.49%   | 51.84%             | -25.56% |     0.03 |       63 | 39.60%     | ok               |
|          35 | -3.02%   | 51.84%             | -20.93% |    -0.02 |       60 | 35.27%     | ok               |

## XRP-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | -29.67%  | -49.68%            | -50.11% |    -0.21 |       70 | 41.95%     | ok               |
|          40 | -36.21%  | -49.68%            | -48.42% |    -0.36 |       62 | 35.82%     | ok               |
|          30 | -42.86%  | -49.68%            | -58.77% |    -0.42 |       74 | 46.36%     | ok               |
|          45 | -43.39%  | -49.68%            | -50.29% |    -0.52 |       62 | 31.42%     | ok               |
|          50 | -40.94%  | -49.68%            | -40.94% |    -0.58 |       64 | 23.75%     | ok               |

## YFI-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -32.83%  | -76.30%            | -52.37% |    -0.46 |       62 | 27.20%     | ok               |
|          45 | -38.27%  | -76.30%            | -54.04% |    -0.66 |       64 | 22.61%     | ok               |
|          30 | -51.43%  | -76.30%            | -67.78% |    -0.73 |       83 | 40.61%     | ok               |
|          35 | -51.92%  | -76.30%            | -65.91% |    -0.81 |       73 | 34.48%     | ok               |
|          25 | -56.37%  | -76.30%            | -69.14% |    -0.83 |       77 | 45.59%     | ok               |

## ZEC-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 124.17%  | 873.79%            | -24.66% |     0.9  |       50 | 23.18%     | ok               |
|          35 | 86.85%   | 873.79%            | -43.54% |     0.74 |       58 | 30.84%     | ok               |
|          25 | 73.54%   | 873.79%            | -46.61% |     0.69 |       61 | 39.66%     | ok               |
|          50 | 54.10%   | 873.79%            | -37.94% |     0.6  |       52 | 20.69%     | ok               |
|          30 | 43.83%   | 873.79%            | -46.93% |     0.56 |       69 | 36.40%     | ok               |
