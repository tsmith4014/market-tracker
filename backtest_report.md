# Market Tracker Backtest Report

_Generated: 2026-07-21T03:54:53+00:00_

## Data Sources

- Crypto: Kraken -> Coinbase -> CoinGecko OHLC -> CoinPaprika fallback chain.
- Stocks / ETFs / indices: Stooq -> Yahoo Finance fallback chain.
- Data rows are generated from real market APIs. Mock OHLCV rows are not generated.

## Data Freshness

- Rows: **92,523**
- Symbols: **161**
- Date range: **2024-02-26** to **2026-07-21**

## Latest Signals

| symbol     | date                |         close |   composite_score | signal   | data_source   |
|:-----------|:--------------------|--------------:|------------------:|:---------|:--------------|
| AAPL       | 2026-07-20 00:00:00 |   326.59      |         50.25     | LONG     | Yahoo Finance |
| AMZN       | 2026-07-20 00:00:00 |   249.99      |         72.4167   | LONG     | Yahoo Finance |
| ARB-USD    | 2026-07-21 00:00:00 |     0.0907    |         48.6667   | LONG     | Kraken API    |
| BAC        | 2026-07-20 00:00:00 |    60.42      |         48.5833   | LONG     | Yahoo Finance |
| BLK        | 2026-07-20 00:00:00 |  1054.11      |         50.25     | LONG     | Yahoo Finance |
| COP        | 2026-07-20 00:00:00 |   115.68      |         74.5      | LONG     | Yahoo Finance |
| CRV-USD    | 2026-07-21 00:00:00 |     0.21582   |         54.4167   | LONG     | Kraken API    |
| CVX        | 2026-07-20 00:00:00 |   189.71      |         71.25     | LONG     | Yahoo Finance |
| DBC        | 2026-07-20 00:00:00 |    29.14      |         73.25     | LONG     | Yahoo Finance |
| DXY-INDEX  | 2026-07-20 00:00:00 |   100.979     |         52.1505   | LONG     | Yahoo Finance |
| EOG        | 2026-07-20 00:00:00 |   141.09      |         74.0833   | LONG     | Yahoo Finance |
| ETH-USD    | 2026-07-21 00:00:00 |  1922.19      |         51.8333   | LONG     | Kraken API    |
| FXI        | 2026-07-20 00:00:00 |    35.04      |         32        | LONG     | Yahoo Finance |
| INJ-USD    | 2026-07-21 00:00:00 |     5.375     |         74.0833   | LONG     | Kraken API    |
| LDO-USD    | 2026-07-21 00:00:00 |     0.398     |         45.8333   | LONG     | Kraken API    |
| LINK-USD   | 2026-07-21 00:00:00 |     8.60355   |         56.4167   | LONG     | Kraken API    |
| LTC-USD    | 2026-07-21 00:00:00 |    47.27      |         51        | LONG     | Kraken API    |
| META       | 2026-07-20 00:00:00 |   645.85      |         59.6667   | LONG     | Yahoo Finance |
| MPC        | 2026-07-20 00:00:00 |   315.31      |         73.75     | LONG     | Yahoo Finance |
| MRK        | 2026-07-20 00:00:00 |   124.4       |         33.9167   | LONG     | Yahoo Finance |
| OXY        | 2026-07-20 00:00:00 |    55.19      |         74.5      | LONG     | Yahoo Finance |
| PEPE-USD   | 2026-07-21 00:00:00 |     2.935e-06 |         52.6667   | LONG     | Kraken API    |
| POL-USD    | 2026-07-21 00:00:00 |     0.08038   |         49        | LONG     | Kraken API    |
| RTX        | 2026-07-20 00:00:00 |   194.44      |         42.8333   | LONG     | Yahoo Finance |
| SCHW       | 2026-07-20 00:00:00 |   102.54      |         61.75     | LONG     | Yahoo Finance |
| SKY-USD    | 2026-07-21 00:00:00 |     0.06351   |         31.5      | LONG     | Kraken API    |
| TMO        | 2026-07-20 00:00:00 |   526.23      |         61.3333   | LONG     | Yahoo Finance |
| UNH        | 2026-07-20 00:00:00 |   421.55      |         39.0833   | LONG     | Yahoo Finance |
| UNI-USD    | 2026-07-21 00:00:00 |     3.712     |         38.8333   | LONG     | Kraken API    |
| UPS        | 2026-07-20 00:00:00 |   113.15      |         74.4167   | LONG     | Yahoo Finance |
| USO        | 2026-07-20 00:00:00 |   125.51      |         62.5833   | LONG     | Yahoo Finance |
| XLE        | 2026-07-20 00:00:00 |    57.94      |         72.75     | LONG     | Yahoo Finance |
| XLF        | 2026-07-20 00:00:00 |    56.04      |         60.0833   | LONG     | Yahoo Finance |
| XOM        | 2026-07-20 00:00:00 |   148.36      |         74.5      | LONG     | Yahoo Finance |
| ZEC-USD    | 2026-07-21 00:00:00 |   550.49      |         66.1667   | LONG     | Kraken API    |
| AAVE-USD   | 2026-07-21 00:00:00 |    91.78      |         22        | NEUTRAL  | Kraken API    |
| ABBV       | 2026-07-20 00:00:00 |   253.38      |         25.6667   | NEUTRAL  | Yahoo Finance |
| ADA-USD    | 2026-07-21 00:00:00 |     0.170713  |         -2        | NEUTRAL  | Kraken API    |
| ADBE       | 2026-07-20 00:00:00 |   234.74      |         21.75     | NEUTRAL  | Yahoo Finance |
| ALGO-USD   | 2026-07-21 00:00:00 |     0.08362   |        -27.9167   | NEUTRAL  | Kraken API    |
| AMAT       | 2026-07-20 00:00:00 |   525.7       |        -20.4167   | NEUTRAL  | Yahoo Finance |
| AMD        | 2026-07-20 00:00:00 |   503.57      |         -3.83333  | NEUTRAL  | Yahoo Finance |
| AMGN       | 2026-07-20 00:00:00 |   364.17      |         22.8333   | NEUTRAL  | Yahoo Finance |
| APT-USD    | 2026-07-21 00:00:00 |     0.6039    |        -21.6667   | NEUTRAL  | Kraken API    |
| ATOM-USD   | 2026-07-21 00:00:00 |     1.4961    |        -16.6667   | NEUTRAL  | Kraken API    |
| AVAX-USD   | 2026-07-21 00:00:00 |     6.626     |         -2        | NEUTRAL  | Kraken API    |
| AVGO       | 2026-07-20 00:00:00 |   378.16      |         -6.75     | NEUTRAL  | Yahoo Finance |
| BA         | 2026-07-20 00:00:00 |   209.48      |        -65.75     | NEUTRAL  | Yahoo Finance |
| BITO       | 2026-07-20 00:00:00 |     8.82      |         11.6667   | NEUTRAL  | Yahoo Finance |
| BTC-USD    | 2026-07-21 00:00:00 | 65423.1       |         33.9167   | NEUTRAL  | Kraken API    |
| C          | 2026-07-20 00:00:00 |   128.72      |        -11.5833   | NEUTRAL  | Yahoo Finance |
| CAT        | 2026-07-20 00:00:00 |   864.3       |        -30.0833   | NEUTRAL  | Yahoo Finance |
| CL         | 2026-07-20 00:00:00 |    91.93      |         12.6667   | NEUTRAL  | Yahoo Finance |
| CMCSA      | 2026-07-20 00:00:00 |    23.78      |          8.58333  | NEUTRAL  | Yahoo Finance |
| COMP-USD   | 2026-07-21 00:00:00 |    16.81      |        -23.6667   | NEUTRAL  | Kraken API    |
| COST       | 2026-07-20 00:00:00 |   935.8       |        -19        | NEUTRAL  | Yahoo Finance |
| CRM        | 2026-07-20 00:00:00 |   173.79      |         17.8333   | NEUTRAL  | Yahoo Finance |
| CSCO       | 2026-07-20 00:00:00 |   110.7       |        -12.25     | NEUTRAL  | Yahoo Finance |
| DASH-USD   | 2026-07-21 00:00:00 |    34.096     |        -52.9167   | NEUTRAL  | Kraken API    |
| DE         | 2026-07-20 00:00:00 |   586         |          9.16667  | NEUTRAL  | Yahoo Finance |
| DIA        | 2026-07-20 00:00:00 |   517.94      |          9.41667  | NEUTRAL  | Yahoo Finance |
| DIS        | 2026-07-20 00:00:00 |    96.41      |        -54.5      | NEUTRAL  | Yahoo Finance |
| DOGE-USD   | 2026-07-21 00:00:00 |     0.0726228 |        -18.9167   | NEUTRAL  | Kraken API    |
| DOT-USD    | 2026-07-21 00:00:00 |     0.8341    |        -18.9167   | NEUTRAL  | Kraken API    |
| EEM        | 2026-07-20 00:00:00 |    63.56      |         -9.83333  | NEUTRAL  | Yahoo Finance |
| EFA        | 2026-07-20 00:00:00 |   102.57      |        -34        | NEUTRAL  | Yahoo Finance |
| ETC-USD    | 2026-07-21 00:00:00 |     6.922     |        -27.9167   | NEUTRAL  | Kraken API    |
| EWJ        | 2026-07-20 00:00:00 |    90.43      |        -20.75     | NEUTRAL  | Yahoo Finance |
| FCX        | 2026-07-20 00:00:00 |    58.79      |         -8.16667  | NEUTRAL  | Yahoo Finance |
| FIL-USD    | 2026-07-21 00:00:00 |     0.739     |        -44.5833   | NEUTRAL  | Kraken API    |
| GDX        | 2026-07-20 00:00:00 |    70.74      |        -62.8333   | NEUTRAL  | Yahoo Finance |
| GDXJ       | 2026-07-20 00:00:00 |    91.66      |        -64.5833   | NEUTRAL  | Yahoo Finance |
| GE         | 2026-07-20 00:00:00 |   341.3       |         -5.41667  | NEUTRAL  | Yahoo Finance |
| GOOGL      | 2026-07-20 00:00:00 |   351.99      |        -15.25     | NEUTRAL  | Yahoo Finance |
| GRT-USD    | 2026-07-21 00:00:00 |     0.01664   |        -20        | NEUTRAL  | Kraken API    |
| GS         | 2026-07-20 00:00:00 |  1055.03      |         37.6667   | NEUTRAL  | Yahoo Finance |
| HBAR-USD   | 2026-07-21 00:00:00 |     0.06708   |        -29        | NEUTRAL  | Kraken API    |
| HD         | 2026-07-20 00:00:00 |   333.04      |        -54.5833   | NEUTRAL  | Yahoo Finance |
| HON        | 2026-07-20 00:00:00 |   226.18      |        -42.5833   | NEUTRAL  | Yahoo Finance |
| HYG        | 2026-07-20 00:00:00 |    79.68      |        -56.75     | NEUTRAL  | Yahoo Finance |
| IBIT       | 2026-07-20 00:00:00 |    36.89      |         -6.33333  | NEUTRAL  | Yahoo Finance |
| ICP-USD    | 2026-07-21 00:00:00 |     2.216     |          7.75     | NEUTRAL  | Kraken API    |
| IEF        | 2026-07-20 00:00:00 |    93.54      |        -64.3333   | NEUTRAL  | Yahoo Finance |
| IEMG       | 2026-07-20 00:00:00 |    77.21      |         -9.83333  | NEUTRAL  | Yahoo Finance |
| INTC       | 2026-07-20 00:00:00 |    97.06      |        -22.8333   | NEUTRAL  | Yahoo Finance |
| INTU       | 2026-07-20 00:00:00 |   293.82      |          0.166667 | NEUTRAL  | Yahoo Finance |
| ITA        | 2026-07-20 00:00:00 |   229.27      |        -22.5      | NEUTRAL  | Yahoo Finance |
| IWM        | 2026-07-20 00:00:00 |   292.31      |          0.166667 | NEUTRAL  | Yahoo Finance |
| JNJ        | 2026-07-20 00:00:00 |   248.82      |         -2.08333  | NEUTRAL  | Yahoo Finance |
| JPM        | 2026-07-20 00:00:00 |   338.87      |         17        | NEUTRAL  | Yahoo Finance |
| KO         | 2026-07-20 00:00:00 |    82.12      |         14.3333   | NEUTRAL  | Yahoo Finance |
| LIN        | 2026-07-20 00:00:00 |   512.05      |          1.33333  | NEUTRAL  | Yahoo Finance |
| LLY        | 2026-07-20 00:00:00 |  1146.9       |        -13.3333   | NEUTRAL  | Yahoo Finance |
| LRCX       | 2026-07-20 00:00:00 |   306.76      |        -36.0833   | NEUTRAL  | Yahoo Finance |
| MCD        | 2026-07-20 00:00:00 |   267.64      |        -36.3333   | NEUTRAL  | Yahoo Finance |
| MS         | 2026-07-20 00:00:00 |   210.94      |         -2.16667  | NEUTRAL  | Yahoo Finance |
| MSFT       | 2026-07-20 00:00:00 |   402.29      |         15        | NEUTRAL  | Yahoo Finance |
| MU         | 2026-07-20 00:00:00 |   865.46      |        -26.5833   | NEUTRAL  | Yahoo Finance |
| NEAR-USD   | 2026-07-21 00:00:00 |     2.0248    |         57        | NEUTRAL  | Kraken API    |
| NEM        | 2026-07-20 00:00:00 |    89.2       |        -62.8333   | NEUTRAL  | Yahoo Finance |
| NKE        | 2026-07-20 00:00:00 |    43.47      |         -3.25     | NEUTRAL  | Yahoo Finance |
| NOW        | 2026-07-20 00:00:00 |   104.7       |          6.08333  | NEUTRAL  | Yahoo Finance |
| NVDA       | 2026-07-20 00:00:00 |   203.28      |          5.91667  | NEUTRAL  | Yahoo Finance |
| OP-USD     | 2026-07-21 00:00:00 |     0.0944    |        -46.25     | NEUTRAL  | Kraken API    |
| PEP        | 2026-07-20 00:00:00 |   135.46      |        -67.3333   | NEUTRAL  | Yahoo Finance |
| PFE        | 2026-07-20 00:00:00 |    24.75      |          0.25     | NEUTRAL  | Yahoo Finance |
| PG         | 2026-07-20 00:00:00 |   149.13      |         17.5      | NEUTRAL  | Yahoo Finance |
| PM         | 2026-07-20 00:00:00 |   192.72      |         60.8333   | NEUTRAL  | Yahoo Finance |
| QCOM       | 2026-07-20 00:00:00 |   170.32      |        -55.8333   | NEUTRAL  | Yahoo Finance |
| QQQ        | 2026-07-20 00:00:00 |   696.06      |        -26.5      | NEUTRAL  | Yahoo Finance |
| RENDER-USD | 2026-07-21 00:00:00 |     1.535     |        -29        | NEUTRAL  | Kraken API    |
| SBUX       | 2026-07-20 00:00:00 |   104.81      |         54.1667   | NEUTRAL  | Yahoo Finance |
| SHIB-USD   | 2026-07-21 00:00:00 |     4.276e-06 |         -9.91667  | NEUTRAL  | Kraken API    |
| SHY        | 2026-07-20 00:00:00 |    81.955     |        -45.4167   | NEUTRAL  | Yahoo Finance |
| SLB        | 2026-07-20 00:00:00 |    46.39      |          2.16667  | NEUTRAL  | Yahoo Finance |
| SMH        | 2026-07-20 00:00:00 |   558.83      |        -17.25     | NEUTRAL  | Yahoo Finance |
| SNX-USD    | 2026-07-21 00:00:00 |     0.2317    |         25.75     | NEUTRAL  | Kraken API    |
| SOL-USD    | 2026-07-21 00:00:00 |    78.13      |          9.33333  | NEUTRAL  | Kraken API    |
| SOXX       | 2026-07-20 00:00:00 |   524.14      |        -19.25     | NEUTRAL  | Yahoo Finance |
| SPY        | 2026-07-20 00:00:00 |   742.09      |         28.3333   | NEUTRAL  | Yahoo Finance |
| SUSHI-USD  | 2026-07-21 00:00:00 |     0.1664    |         26        | NEUTRAL  | Kraken API    |
| T          | 2026-07-20 00:00:00 |    21.95      |          2.41667  | NEUTRAL  | Yahoo Finance |
| TGT        | 2026-07-20 00:00:00 |   139.59      |         57.5      | NEUTRAL  | Yahoo Finance |
| TMUS       | 2026-07-20 00:00:00 |   195.64      |         27.25     | NEUTRAL  | Yahoo Finance |
| TRX-USD    | 2026-07-21 00:00:00 |     0.325891  |         17.8333   | NEUTRAL  | Kraken API    |
| TSLA       | 2026-07-20 00:00:00 |   369.57      |        -69.5      | NEUTRAL  | Yahoo Finance |
| TXN        | 2026-07-20 00:00:00 |   284.07      |        -23.5      | NEUTRAL  | Yahoo Finance |
| VEA        | 2026-07-20 00:00:00 |    69.23      |        -24.5      | NEUTRAL  | Yahoo Finance |
| VIXY       | 2026-07-20 00:00:00 |    21.23      |        -15.75     | NEUTRAL  | Yahoo Finance |
| VNQ        | 2026-07-20 00:00:00 |    99.48      |         59.8333   | NEUTRAL  | Yahoo Finance |
| VTI        | 2026-07-20 00:00:00 |   366.25      |          9.16667  | NEUTRAL  | Yahoo Finance |
| VWO        | 2026-07-20 00:00:00 |    57.93      |        -35.0833   | NEUTRAL  | Yahoo Finance |
| VZ         | 2026-07-20 00:00:00 |    43.5       |        -11.75     | NEUTRAL  | Yahoo Finance |
| WFC        | 2026-07-20 00:00:00 |    86.33      |         28.25     | NEUTRAL  | Yahoo Finance |
| XBI        | 2026-07-20 00:00:00 |   150.94      |         16.4167   | NEUTRAL  | Yahoo Finance |
| XLB        | 2026-07-20 00:00:00 |    50.03      |        -15.8333   | NEUTRAL  | Yahoo Finance |
| XLC        | 2026-07-20 00:00:00 |   110.8       |         -1.83333  | NEUTRAL  | Yahoo Finance |
| XLI        | 2026-07-20 00:00:00 |   178.12      |         20.4167   | NEUTRAL  | Yahoo Finance |
| XLK        | 2026-07-20 00:00:00 |   175.71      |        -26.5      | NEUTRAL  | Yahoo Finance |
| XLM-USD    | 2026-07-21 00:00:00 |     0.188059  |        -36.9167   | NEUTRAL  | Kraken API    |
| XLP        | 2026-07-20 00:00:00 |    84.86      |         59.8333   | NEUTRAL  | Yahoo Finance |
| XLU        | 2026-07-20 00:00:00 |    44.94      |        -23.0833   | NEUTRAL  | Yahoo Finance |
| XLV        | 2026-07-20 00:00:00 |   159.25      |         25.4167   | NEUTRAL  | Yahoo Finance |
| XLY        | 2026-07-20 00:00:00 |   114.61      |        -57.25     | NEUTRAL  | Yahoo Finance |
| XRP-USD    | 2026-07-21 00:00:00 |     1.12132   |         11.5      | NEUTRAL  | Kraken API    |
| YFI-USD    | 2026-07-21 00:00:00 |  2121.5       |          9.08333  | NEUTRAL  | Kraken API    |
| AGG        | 2026-07-20 00:00:00 |    97.95      |        -53.0833   | SHORT    | Yahoo Finance |
| ARKK       | 2026-07-20 00:00:00 |    74.95      |        -54        | SHORT    | Yahoo Finance |
| BCH-USD    | 2026-07-21 00:00:00 |   222.92      |        -51.3333   | SHORT    | Kraken API    |
| BND        | 2026-07-20 00:00:00 |    72.68      |        -53.0833   | SHORT    | Yahoo Finance |
| BONK-USD   | 2026-07-21 00:00:00 |     3.227e-06 |        -46.6667   | SHORT    | Kraken API    |
| FET-USD    | 2026-07-21 00:00:00 |     0.156     |        -31        | SHORT    | Kraken API    |
| GLD        | 2026-07-20 00:00:00 |   367.6       |        -30.9167   | SHORT    | Yahoo Finance |
| IBM        | 2026-07-20 00:00:00 |   213         |        -65.0833   | SHORT    | Yahoo Finance |
| NFLX       | 2026-07-20 00:00:00 |    67.6       |        -48.25     | SHORT    | Yahoo Finance |
| ORCL       | 2026-07-20 00:00:00 |   121.38      |        -54.4167   | SHORT    | Yahoo Finance |
| SLV        | 2026-07-20 00:00:00 |    50.98      |        -32.9167   | SHORT    | Yahoo Finance |
| TIA-USD    | 2026-07-21 00:00:00 |     0.3606    |        -37        | SHORT    | Kraken API    |
| TLT        | 2026-07-20 00:00:00 |    83.89      |        -55.0833   | SHORT    | Yahoo Finance |
| WIF-USD    | 2026-07-21 00:00:00 |     0.1523    |        -42.3333   | SHORT    | Kraken API    |
| WMT        | 2026-07-20 00:00:00 |   112.2       |        -33.75     | SHORT    | Yahoo Finance |

## Edge Summary

- Symbols with trades: **160** of 160
- Beat buy-and-hold: **33.12%** of traded symbols
- Positive return: **28.75%** of traded symbols
- Median strategy return: **-11.02%** (benchmark **14.95%**)
- Median excess vs benchmark: **-25.67%**
- Median Sharpe: **-0.13**
- Median exposure: **44.26%**

> Edge is real only if both _beat buy-and-hold_ and _median excess_ are convincingly positive across many symbols. Treat a single high-return symbol as noise.

## Portfolio Backtest

Actual capital-allocation books (not per-symbol averages). Benchmarks: `equal_weight_buyhold` (whole tracked universe), `spy_buyhold` (100% SPY), and `sixty_forty` (60% SPY / 40% AGG). `high_conf_voltarget` inverse-vol-weights the HIGH-confidence book; `conviction_long_short` is market-neutral. Judge on **Sharpe** and **max_drawdown** out-of-sample, not raw return: a fully-invested long book wins on return in a bull market but carries all the risk.

| strategy              | scope         | ann_return   | ann_vol   |   sharpe | max_drawdown   | total_return   |   avg_gross_exposure |
|:----------------------|:--------------|:-------------|:----------|---------:|:---------------|:---------------|---------------------:|
| equal_weight_buyhold  | full          | -4.14%       | 32.45%    |    -0.13 | -46.77%        | -25.05%        |                 1    |
| equal_weight_buyhold  | out_of_sample | -26.89%      | 30.68%    |    -0.88 | -38.35%        | -28.66%        |                 1    |
| all_signals_ew        | full          | -17.45%      | 26.91%    |    -0.65 | -61.54%        | -47.50%        |                 1    |
| all_signals_ew        | out_of_sample | 25.79%       | 26.31%    |     0.98 | -18.39%        | 26.97%         |                 1    |
| high_conf_ew          | full          | -1.08%       | 31.40%    |    -0.03 | -43.97%        | -16.59%        |                 0.88 |
| high_conf_ew          | out_of_sample | 20.28%       | 33.87%    |     0.6  | -17.94%        | 17.00%         |                 0.88 |
| high_conf_voltarget   | full          | 0.96%        | 28.95%    |     0.03 | -36.21%        | -9.19%         |                 0.88 |
| high_conf_voltarget   | out_of_sample | 14.48%       | 31.36%    |     0.46 | -16.94%        | 10.94%         |                 0.88 |
| conviction_long_short | full          | -18.35%      | 23.00%    |    -0.8  | -49.84%        | -47.34%        |                 0.97 |
| conviction_long_short | out_of_sample | -8.60%       | 26.20%    |    -0.33 | -24.28%        | -12.07%        |                 0.97 |
| spy_buyhold           | full          | 5.98%        | 13.32%    |     0.45 | -17.80%        | 16.81%         |                 0.78 |
| spy_buyhold           | out_of_sample | -3.54%       | 9.78%     |    -0.36 | -13.27%        | -4.20%         |                 0.78 |
| sixty_forty           | full          | 3.59%        | 8.42%     |     0.43 | -10.77%        | 10.38%         |                 0.78 |
| sixty_forty           | out_of_sample | -3.48%       | 6.45%     |    -0.54 | -9.26%         | -3.86%         |                 0.78 |

## Walk-Forward Robustness

Each book measured across contiguous time folds (each a different regime). A book has durable edge only if `mean_sharpe` is positive, `min_sharpe` isn't deeply negative, and `pct_positive_folds` is high — a single great fold doesn't count. `fold_sharpes` lists each fold oldest-to-newest.

| strategy              |   n_folds |   mean_sharpe |   median_sharpe |   min_sharpe | pct_positive_folds   | mean_return   | fold_sharpes                 |
|:----------------------|----------:|--------------:|----------------:|-------------:|:---------------------|:--------------|:-----------------------------|
| equal_weight_buyhold  |         5 |          0.25 |            0.67 |        -1.54 | 60.00%               | -2.05%        | 1.67;-1.54;1.53;-1.09;0.67   |
| all_signals_ew        |         5 |         -0.74 |           -0.25 |        -2.51 | 20.00%               | -10.86%       | -0.25;-0.15;-2.51;0.33;-1.10 |
| high_conf_ew          |         5 |          0.06 |           -0.41 |        -0.67 | 40.00%               | -2.82%        | 1.20;-0.50;-0.67;0.70;-0.41  |
| high_conf_voltarget   |         5 |          0.23 |           -0.16 |        -0.81 | 40.00%               | -1.13%        | 1.94;-0.16;-0.81;0.71;-0.54  |
| conviction_long_short |         5 |         -0.95 |           -1.34 |        -1.68 | 20.00%               | -11.66%       | -1.34;-1.52;-0.53;0.32;-1.68 |
| spy_buyhold           |         5 |          0.67 |           -0.03 |        -0.97 | 40.00%               | 3.56%         | 1.55;-0.35;3.12;-0.97;-0.03  |
| sixty_forty           |         5 |          0.62 |           -0.36 |        -0.95 | 40.00%               | 2.19%         | 1.71;-0.45;3.14;-0.95;-0.36  |

## Strategy Comparison

Each decision rule backtested over the same data. `out_of_sample` is the most recent ~35% of each symbol's history (unseen tail). A rule has real edge only if `median_excess` and `beat_benchmark_pct` stay positive out-of-sample, not just full-sample.

| strategy        | scope         |   symbols | beat_benchmark_pct   | positive_pct   | median_return   | median_benchmark   | median_excess   |   median_sharpe |   total_trades |
|:----------------|:--------------|----------:|:---------------------|:---------------|:----------------|:-------------------|:----------------|----------------:|---------------:|
| trend           | full          |       160 | 33.12%               | 28.75%         | -11.02%         | 14.95%             | -25.67%         |           -0.13 |          11235 |
| trend           | out_of_sample |       160 | 41.25%               | 51.88%         | 1.44%           | 4.12%              | -4.32%          |            0.23 |           3763 |
| mean_reversion  | full          |       157 | 40.76%               | 51.59%         | 0.09%           | 14.87%             | -13.97%         |            0.04 |           1258 |
| mean_reversion  | out_of_sample |       124 | 49.19%               | 59.68%         | 0.37%           | -1.41%             | -0.44%          |            0.5  |            426 |
| regime_adaptive | full          |       160 | 34.38%               | 30.00%         | -11.04%         | 14.95%             | -25.42%         |           -0.13 |          11509 |
| regime_adaptive | out_of_sample |       160 | 40.62%               | 52.50%         | 1.37%           | 4.12%              | -4.32%          |            0.23 |           3870 |

## Signal Calibration

Realized forward return in the signal's direction, grouped by confidence. HIGH should outrank LOW for the confidence score to be meaningful.

| confidence_level   |   horizon |     n | mean_return   | median_return   | win_rate   |
|:-------------------|----------:|------:|:--------------|:----------------|:-----------|
| HIGH               |         5 |  7919 | 0.11%         | 0.10%           | 51.67%     |
| MEDIUM             |         5 | 29152 | 0.01%         | 0.06%           | 50.71%     |
| LOW                |         5 |  3384 | -0.63%        | -0.56%          | 44.50%     |
| ALL                |         5 | 40455 | -0.02%        | 0.03%           | 50.38%     |
| HIGH               |        10 |  7886 | 0.37%         | 0.09%           | 51.03%     |
| MEDIUM             |        10 | 28954 | 0.14%         | 0.11%           | 50.78%     |
| LOW                |        10 |  3329 | -0.91%        | -0.73%          | 45.27%     |
| ALL                |        10 | 40169 | 0.10%         | 0.05%           | 50.37%     |
| HIGH               |        20 |  7801 | 0.76%         | 0.32%           | 52.69%     |
| MEDIUM             |        20 | 28580 | 0.80%         | 0.59%           | 53.36%     |
| LOW                |        20 |  3248 | -0.71%        | -0.51%          | 47.14%     |
| ALL                |        20 | 39629 | 0.67%         | 0.46%           | 52.72%     |

## Backtest Summary

### Data Quality / Signal Availability

- **ok**: 160 symbols

| symbol     |   trades | return   | benchmark_return   | mdd     |   sharpe | exposure   | skipped_reason   |
|:-----------|---------:|:---------|:-------------------|:--------|---------:|:-----------|:-----------------|
| AAPL       |       61 | 17.35%   | 80.28%             | -20.65% |     0.43 | 49.25%     | ok               |
| AAVE-USD   |       74 | -52.09%  | -63.76%            | -68.26% |    -0.48 | 39.27%     | ok               |
| ABBV       |       66 | -20.32%  | 41.70%             | -30.55% |    -0.43 | 47.25%     | ok               |
| ADA-USD    |       90 | -83.04%  | -78.15%            | -89.12% |    -0.67 | 46.93%     | ok               |
| ADBE       |       64 | -29.30%  | -58.12%            | -35.81% |    -0.36 | 57.24%     | ok               |
| AGG        |       71 | -6.87%   | 0.84%              | -10.25% |    -1.14 | 31.95%     | ok               |
| ALGO-USD   |       86 | -50.43%  | -70.60%            | -53.13% |    -0.57 | 38.12%     | ok               |
| AMAT       |       71 | -35.64%  | 158.27%            | -57.21% |    -0.33 | 52.08%     | ok               |
| AMD        |       52 | 5.86%    | 186.10%            | -43.98% |     0.27 | 35.77%     | ok               |
| AMGN       |       69 | -15.41%  | 27.17%             | -34.14% |    -0.29 | 46.26%     | ok               |
| AMZN       |       80 | -36.95%  | 43.07%             | -42.48% |    -1.11 | 38.27%     | ok               |
| APT-USD    |       74 | -43.60%  | -89.95%            | -69.96% |    -0.27 | 41.95%     | ok               |
| ARB-USD    |       72 | -24.36%  | -80.99%            | -62.34% |    -0.05 | 39.46%     | ok               |
| ARKK       |       85 | -35.71%  | 49.66%             | -37.37% |    -0.65 | 39.93%     | ok               |
| ATOM-USD   |       88 | -69.22%  | -69.07%            | -74.39% |    -1.2  | 44.44%     | ok               |
| AVAX-USD   |       72 | -40.41%  | -74.02%            | -60.43% |    -0.38 | 37.93%     | ok               |
| AVGO       |       64 | 14.00%   | 188.86%            | -35.76% |     0.33 | 42.43%     | ok               |
| BA         |       67 | 7.60%    | 4.46%              | -30.56% |     0.25 | 49.25%     | ok               |
| BAC        |       78 | -7.76%   | 79.77%             | -26.91% |    -0.13 | 50.08%     | ok               |
| BCH-USD    |       80 | -10.98%  | -33.07%            | -54.34% |     0.08 | 48.47%     | ok               |
| BITO       |       80 | -5.95%   | -65.81%            | -42.82% |     0.11 | 41.10%     | ok               |
| BLK        |       69 | -7.20%   | 30.78%             | -24.29% |    -0.15 | 42.26%     | ok               |
| BND        |       67 | -7.58%   | 0.87%              | -9.98%  |    -1.22 | 33.11%     | ok               |
| BONK-USD   |       70 | 69.58%   | -82.09%            | -43.77% |     0.72 | 42.15%     | ok               |
| BTC-USD    |       76 | -2.15%   | -32.96%            | -23.38% |     0.12 | 52.87%     | ok               |
| C          |       79 | -30.57%  | 132.51%            | -38.11% |    -0.61 | 51.08%     | ok               |
| CAT        |       72 | 21.25%   | 165.63%            | -21.02% |     0.44 | 55.57%     | ok               |
| CL         |       62 | 7.73%    | 6.71%              | -14.32% |     0.31 | 45.59%     | ok               |
| CMCSA      |       82 | -40.78%  | -39.86%            | -41.06% |    -1.09 | 42.10%     | ok               |
| COMP-USD   |       89 | -42.10%  | -70.29%            | -57.88% |    -0.3  | 45.59%     | ok               |
| COP        |       72 | -21.65%  | 2.90%              | -43.96% |    -0.38 | 42.10%     | ok               |
| COST       |       60 | -2.66%   | 25.55%             | -29.73% |    -0.01 | 43.26%     | ok               |
| CRM        |       63 | -39.56%  | -42.15%            | -41.36% |    -0.83 | 42.76%     | ok               |
| CRV-USD    |       70 | -6.16%   | -57.77%            | -39.89% |     0.17 | 36.40%     | ok               |
| CSCO       |       61 | 21.40%   | 128.72%            | -21.79% |     0.48 | 48.59%     | ok               |
| CVX        |       75 | -14.51%  | 22.83%             | -29.13% |    -0.35 | 39.93%     | ok               |
| DASH-USD   |       61 | -41.76%  | 25.64%             | -64.43% |    -0.02 | 29.12%     | ok               |
| DBC        |       62 | -11.28%  | 32.82%             | -25.70% |    -0.37 | 33.78%     | ok               |
| DE         |       74 | -9.04%   | 61.34%             | -25.24% |    -0.1  | 47.25%     | ok               |
| DIA        |       62 | -4.26%   | 32.56%             | -12.94% |    -0.2  | 43.93%     | ok               |
| DIS        |       68 | -21.66%  | -10.47%            | -28.17% |    -0.42 | 45.59%     | ok               |
| DOGE-USD   |       71 | -22.30%  | -73.27%            | -60.95% |     0.02 | 50.00%     | ok               |
| DOT-USD    |       84 | -57.70%  | -83.39%            | -63.10% |    -0.61 | 47.51%     | ok               |
| DXY-INDEX  |       40 | -1.53%   | 0.38%              | -6.02%  |    -0.23 | 30.80%     | ok               |
| EEM        |       64 | -10.02%  | 57.25%             | -25.67% |    -0.27 | 42.76%     | ok               |
| EFA        |       62 | -9.55%   | 32.71%             | -15.14% |    -0.35 | 44.59%     | ok               |
| EOG        |       81 | -21.46%  | 25.92%             | -48.13% |    -0.43 | 47.42%     | ok               |
| ETC-USD    |       64 | -31.63%  | -66.76%            | -45.98% |    -0.43 | 29.50%     | ok               |
| ETH-USD    |       64 | 147.60%  | -28.62%            | -30.11% |     1.23 | 44.83%     | ok               |
| EWJ        |       62 | -19.59%  | 31.06%             | -30.73% |    -0.65 | 38.60%     | ok               |
| FCX        |       63 | -27.81%  | 54.59%             | -47.47% |    -0.31 | 45.26%     | ok               |
| FET-USD    |       85 | -39.27%  | -79.79%            | -54.02% |    -0.14 | 42.34%     | ok               |
| FIL-USD    |       70 | -47.52%  | -78.37%            | -50.22% |    -0.63 | 32.38%     | ok               |
| FXI        |       44 | -6.84%   | 46.55%             | -23.91% |    -0.09 | 30.12%     | ok               |
| GDX        |       60 | 11.28%   | 169.49%            | -34.99% |     0.3  | 48.09%     | ok               |
| GDXJ       |       66 | -22.87%  | 187.07%            | -44.93% |    -0.21 | 46.09%     | ok               |
| GE         |       76 | 8.17%    | 176.31%            | -27.82% |     0.26 | 52.91%     | ok               |
| GLD        |       50 | 26.01%   | 95.32%             | -16.63% |     0.65 | 47.92%     | ok               |
| GOOGL      |       57 | 76.40%   | 155.86%            | -20.41% |     1.15 | 52.58%     | ok               |
| GRT-USD    |       81 | -18.24%  | -87.96%            | -54.83% |    -0.01 | 41.95%     | ok               |
| GS         |       76 | -2.38%   | 170.37%            | -22.13% |     0.05 | 52.08%     | ok               |
| HD         |       71 | -7.53%   | -10.38%            | -17.69% |    -0.12 | 44.59%     | ok               |
| HON        |       93 | -26.82%  | 14.87%             | -29.80% |    -0.72 | 52.41%     | ok               |
| HYG        |       81 | -9.52%   | 3.35%              | -9.59%  |    -1.11 | 34.28%     | ok               |
| IBIT       |       34 | 30.82%   | -2.95%             | -18.95% |     0.66 | 31.94%     | ok               |
| IBM        |       77 | -17.20%  | 15.68%             | -44.74% |    -0.15 | 49.75%     | ok               |
| ICP-USD    |       77 | -17.50%  | -68.81%            | -52.81% |     0.08 | 34.48%     | ok               |
| IEF        |       78 | -11.07%  | -0.38%             | -11.70% |    -1.57 | 32.95%     | ok               |
| IEMG       |       58 | -8.53%   | 51.84%             | -26.84% |    -0.23 | 42.26%     | ok               |
| INJ-USD    |       77 | -51.12%  | -64.83%            | -76.97% |    -0.46 | 38.31%     | ok               |
| INTC       |       68 | 59.68%   | 125.77%            | -60.60% |     0.64 | 49.08%     | ok               |
| INTU       |       67 | -19.54%  | -55.74%            | -42.15% |    -0.23 | 41.60%     | ok               |
| ITA        |       72 | -2.88%   | 81.63%             | -23.75% |    -0.01 | 48.09%     | ok               |
| IWM        |       48 | 9.40%    | 45.32%             | -12.83% |     0.39 | 35.77%     | ok               |
| JNJ        |       68 | 4.23%    | 54.75%             | -17.51% |     0.2  | 50.92%     | ok               |
| JPM        |       77 | -21.02%  | 84.81%             | -33.43% |    -0.51 | 53.74%     | ok               |
| KO         |       51 | 23.75%   | 35.27%             | -8.20%  |     0.85 | 37.94%     | ok               |
| LDO-USD    |       78 | 28.67%   | -78.04%            | -60.93% |     0.49 | 40.42%     | ok               |
| LIN        |       66 | -4.64%   | 15.08%             | -21.53% |    -0.11 | 38.77%     | ok               |
| LINK-USD   |       75 | -13.84%  | -54.68%            | -49.35% |     0.1  | 43.10%     | ok               |
| LLY        |       71 | -28.67%  | 48.58%             | -53.34% |    -0.42 | 49.25%     | ok               |
| LRCX       |       82 | -26.74%  | 226.77%            | -63.39% |    -0.17 | 44.26%     | ok               |
| LTC-USD    |       72 | -32.21%  | -64.71%            | -53.76% |    -0.26 | 50.00%     | ok               |
| MCD        |       75 | -2.55%   | -9.92%             | -18.81% |    -0.05 | 38.10%     | ok               |
| META       |       74 | -32.00%  | 34.07%             | -40.38% |    -0.57 | 47.92%     | ok               |
| MPC        |       71 | -6.35%   | 82.85%             | -44.76% |     0.01 | 48.92%     | ok               |
| MRK        |       69 | -31.10%  | -3.45%             | -35.95% |    -0.75 | 44.26%     | ok               |
| MS         |       77 | -10.18%  | 146.22%            | -27.79% |    -0.16 | 49.58%     | ok               |
| MSFT       |       81 | -37.64%  | -1.29%             | -39.15% |    -0.99 | 47.09%     | ok               |
| MU         |       49 | 270.03%  | 867.43%            | -68.76% |     1.34 | 59.73%     | ok               |
| NEAR-USD   |       83 | -14.95%  | -40.57%            | -59.86% |     0.1  | 41.00%     | ok               |
| NEM        |       72 | -31.13%  | 197.23%            | -38.49% |    -0.33 | 53.08%     | ok               |
| NFLX       |       68 | 30.02%   | 15.03%             | -21.09% |     0.65 | 54.08%     | ok               |
| NKE        |       91 | -37.92%  | -58.42%            | -55.35% |    -0.53 | 43.93%     | ok               |
| NOW        |       78 | 8.05%    | -32.86%            | -27.34% |     0.26 | 45.59%     | ok               |
| NVDA       |       75 | -26.95%  | 146.63%            | -45.02% |    -0.19 | 59.89%     | ok               |
| OP-USD     |       72 | -36.50%  | -91.65%            | -72.42% |    -0.21 | 34.10%     | ok               |
| ORCL       |       70 | 132.26%  | 9.38%              | -29.47% |     1.03 | 54.58%     | ok               |
| OXY        |       71 | 1.10%    | -8.73%             | -34.15% |     0.14 | 46.09%     | ok               |
| PEP        |       75 | -4.54%   | -19.49%            | -21.35% |    -0.07 | 48.25%     | ok               |
| PEPE-USD   |       81 | 6.54%    | -70.47%            | -57.66% |     0.33 | 45.40%     | ok               |
| PFE        |       79 | -41.51%  | -8.94%             | -42.34% |    -1.34 | 36.11%     | ok               |
| PG         |       68 | -19.51%  | -6.92%             | -24.55% |    -0.74 | 39.77%     | ok               |
| PM         |       83 | -3.22%   | 113.14%            | -33.68% |     0.03 | 55.74%     | ok               |
| POL-USD    |       75 | 37.56%   | -74.72%            | -46.45% |     0.58 | 47.32%     | ok               |
| QCOM       |       73 | -15.25%  | 8.46%              | -56.59% |    -0.04 | 46.09%     | ok               |
| QQQ        |       60 | 20.33%   | 59.45%             | -12.88% |     0.58 | 43.59%     | ok               |
| RENDER-USD |       98 | -19.07%  | -63.10%            | -45.00% |     0.1  | 42.44%     | ok               |
| RTX        |       56 | 26.01%   | 116.00%            | -16.99% |     0.64 | 52.08%     | ok               |
| SBUX       |       62 | -18.75%  | 11.17%             | -29.22% |    -0.34 | 39.77%     | ok               |
| SCHW       |       74 | -12.78%  | 59.22%             | -31.92% |    -0.23 | 48.09%     | ok               |
| SHIB-USD   |       74 | -29.98%  | -73.80%            | -47.96% |    -0.2  | 51.72%     | ok               |
| SHY        |       48 | -2.24%   | 0.42%              | -2.85%  |    -0.79 | 34.28%     | ok               |
| SKY-USD    |       74 | -28.58%  | 9.82%              | -44.74% |    -0.33 | 40.74%     | ok               |
| SLB        |       73 | -23.87%  | -4.47%             | -54.23% |    -0.39 | 51.08%     | ok               |
| SLV        |       60 | 49.35%   | 147.24%            | -42.66% |     0.68 | 43.59%     | ok               |
| SMH        |       48 | 77.71%   | 165.67%            | -33.99% |     1.07 | 47.42%     | ok               |
| SNX-USD    |       58 | -15.26%  | -76.52%            | -34.76% |     0.08 | 37.93%     | ok               |
| SOL-USD    |       70 | -34.01%  | -59.81%            | -56.90% |    -0.11 | 60.15%     | ok               |
| SOXX       |       55 | 73.21%   | 144.64%            | -40.34% |     0.97 | 46.42%     | ok               |
| SPY        |       64 | 2.18%    | 46.66%             | -16.47% |     0.14 | 49.75%     | ok               |
| SUSHI-USD  |       98 | -82.20%  | -81.32%            | -85.70% |    -1.3  | 36.78%     | ok               |
| T          |       64 | 37.51%   | 32.23%             | -17.01% |     0.84 | 53.24%     | ok               |
| TGT        |       60 | -11.39%  | -7.03%             | -40.57% |    -0.15 | 38.60%     | ok               |
| TIA-USD    |       93 | -45.10%  | -88.25%            | -67.89% |    -0.31 | 36.97%     | ok               |
| TLT        |       72 | -21.12%  | -10.36%            | -21.87% |    -1.63 | 32.61%     | ok               |
| TMO        |       61 | 16.75%   | -6.61%             | -18.85% |     0.42 | 51.41%     | ok               |
| TMUS       |       70 | 6.48%    | 19.36%             | -25.71% |     0.23 | 47.75%     | ok               |
| TRX-USD    |       68 | 7.33%    | 37.25%             | -22.90% |     0.28 | 48.66%     | ok               |
| TSLA       |       70 | -14.59%  | 85.34%             | -54.91% |     0.05 | 41.26%     | ok               |
| TXN        |       73 | -12.99%  | 72.90%             | -47.39% |    -0.05 | 52.58%     | ok               |
| UNH        |       74 | 27.43%   | -19.75%            | -26.96% |     0.49 | 52.58%     | ok               |
| UNI-USD    |       86 | -70.76%  | -62.12%            | -80.61% |    -0.81 | 44.64%     | ok               |
| UPS        |       70 | -37.14%  | -23.29%            | -38.83% |    -0.75 | 39.27%     | ok               |
| USO        |       68 | 12.63%   | 72.43%             | -43.35% |     0.32 | 34.28%     | ok               |
| VEA        |       58 | -0.76%   | 42.04%             | -17.93% |     0.02 | 43.93%     | ok               |
| VIXY       |       96 | -80.86%  | -61.26%            | -88.16% |    -1.03 | 32.78%     | ok               |
| VNQ        |       71 | -15.77%  | 18.60%             | -24.92% |    -0.66 | 36.94%     | ok               |
| VTI        |       70 | -4.47%   | 45.78%             | -18.77% |    -0.1  | 50.08%     | ok               |
| VWO        |       78 | -14.45%  | 39.79%             | -25.20% |    -0.51 | 43.59%     | ok               |
| VZ         |       83 | -27.34%  | 9.60%              | -27.34% |    -0.92 | 37.44%     | ok               |
| WFC        |       84 | -16.26%  | 59.49%             | -30.87% |    -0.25 | 50.92%     | ok               |
| WIF-USD    |       70 | -35.24%  | -77.85%            | -51.39% |    -0.12 | 33.14%     | ok               |
| WMT        |       61 | 10.49%   | 88.26%             | -21.31% |     0.35 | 50.25%     | ok               |
| XBI        |       66 | -4.60%   | 55.06%             | -19.79% |    -0.03 | 41.10%     | ok               |
| XLB        |       64 | -10.86%  | 15.93%             | -26.57% |    -0.36 | 36.77%     | ok               |
| XLC        |       69 | 11.95%   | 41.04%             | -12.33% |     0.44 | 53.91%     | ok               |
| XLE        |       75 | -7.99%   | 34.34%             | -37.64% |    -0.12 | 45.26%     | ok               |
| XLF        |       76 | -11.95%  | 39.75%             | -23.61% |    -0.39 | 47.92%     | ok               |
| XLI        |       66 | -2.58%   | 48.38%             | -11.79% |    -0.05 | 43.93%     | ok               |
| XLK        |       40 | 65.83%   | 71.02%             | -14.75% |     1.22 | 45.59%     | ok               |
| XLM-USD    |       69 | 5.21%    | -46.08%            | -50.36% |     0.28 | 45.79%     | ok               |
| XLP        |       66 | 4.67%    | 13.94%             | -11.16% |     0.3  | 41.26%     | ok               |
| XLU        |       67 | -5.24%   | 47.97%             | -20.40% |    -0.19 | 39.10%     | ok               |
| XLV        |       68 | -16.05%  | 8.26%              | -19.97% |    -0.79 | 36.11%     | ok               |
| XLY        |       70 | 3.95%    | 26.05%             | -14.01% |     0.19 | 44.59%     | ok               |
| XOM        |       57 | 6.68%    | 42.31%             | -20.29% |     0.26 | 36.94%     | ok               |
| XRP-USD    |       58 | -30.47%  | -59.41%            | -44.89% |    -0.26 | 33.72%     | ok               |
| YFI-USD    |       81 | -64.19%  | -64.52%            | -71.12% |    -1.03 | 40.61%     | ok               |
| ZEC-USD    |       62 | 61.20%   | 1610.13%           | -47.68% |     0.64 | 36.40%     | ok               |

## AAPL Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 26.51%   | 80.28%             | -21.71% |     0.57 |       68 | 53.41%     | ok               |
|          15 | 22.62%   | 80.28%             | -23.86% |     0.5  |       75 | 60.57%     | ok               |
|          30 | 17.35%   | 80.28%             | -20.65% |     0.43 |       61 | 49.25%     | ok               |
|          35 | 14.71%   | 80.28%             | -22.04% |     0.39 |       61 | 47.75%     | ok               |
|          25 | 14.90%   | 80.28%             | -20.03% |     0.38 |       67 | 51.08%     | ok               |

## AAVE-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 10.06%   | -63.76%            | -43.61% |     0.32 |       40 | 31.99%     | ok               |
|          45 | -4.67%   | -63.76%            | -49.19% |     0.15 |       44 | 27.20%     | ok               |
|          35 | -8.77%   | -63.76%            | -51.96% |     0.13 |       50 | 35.25%     | ok               |
|          15 | -52.34%  | -63.76%            | -61.76% |    -0.33 |       80 | 53.83%     | ok               |
|          50 | -33.87%  | -63.76%            | -47.39% |    -0.36 |       42 | 19.73%     | ok               |

## ABBV Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -12.90%  | 41.70%             | -28.51% |    -0.27 |       50 | 36.44%     | ok               |
|          30 | -20.32%  | 41.70%             | -30.55% |    -0.43 |       66 | 47.25%     | ok               |
|          40 | -20.07%  | 41.70%             | -26.61% |    -0.46 |       66 | 41.10%     | ok               |
|          25 | -22.09%  | 41.70%             | -31.26% |    -0.48 |       69 | 48.75%     | ok               |
|          20 | -22.69%  | 41.70%             | -30.60% |    -0.48 |       69 | 50.58%     | ok               |

## ADA-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -78.05%  | -78.15%            | -86.04% |    -0.6  |       55 | 27.01%     | ok               |
|          45 | -80.39%  | -78.15%            | -88.08% |    -0.63 |       58 | 31.80%     | ok               |
|          35 | -82.82%  | -78.15%            | -89.83% |    -0.67 |       78 | 42.53%     | ok               |
|          30 | -83.04%  | -78.15%            | -89.12% |    -0.67 |       90 | 46.93%     | ok               |
|          15 | -86.96%  | -78.15%            | -91.11% |    -0.72 |       78 | 63.41%     | ok               |

## ADBE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 1.24%    | -58.12%            | -22.53% |     0.14 |       72 | 49.08%     | ok               |
|          25 | -16.00%  | -58.12%            | -31.11% |    -0.1  |       48 | 61.40%     | ok               |
|          40 | -11.88%  | -58.12%            | -24.87% |    -0.11 |       70 | 42.10%     | ok               |
|          20 | -24.28%  | -58.12%            | -32.14% |    -0.24 |       50 | 63.89%     | ok               |
|          15 | -27.73%  | -58.12%            | -32.12% |    -0.3  |       59 | 65.72%     | ok               |

## AGG Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -6.87%   | 0.84%              | -10.25% |    -1.14 |       71 | 31.95%     | ok               |
|          50 | -5.35%   | 0.84%              | -7.92%  |    -1.19 |       48 | 17.14%     | ok               |
|          45 | -6.01%   | 0.84%              | -7.91%  |    -1.21 |       54 | 21.30%     | ok               |
|          20 | -8.25%   | 0.84%              | -11.43% |    -1.21 |       75 | 37.44%     | ok               |
|          25 | -8.43%   | 0.84%              | -12.07% |    -1.29 |       75 | 35.77%     | ok               |

## ALGO-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -50.43%  | -70.60%            | -53.13% |    -0.57 |       86 | 38.12%     | ok               |
|          15 | -61.64%  | -70.60%            | -68.50% |    -0.67 |       84 | 50.38%     | ok               |
|          25 | -61.89%  | -70.60%            | -72.48% |    -0.74 |       84 | 45.02%     | ok               |
|          20 | -65.54%  | -70.60%            | -71.20% |    -0.8  |       86 | 48.08%     | ok               |
|          50 | -45.64%  | -70.60%            | -48.43% |    -0.81 |       42 | 16.86%     | ok               |

## AMAT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -24.22%  | 158.27%            | -54.05% |    -0.11 |       68 | 61.06%     | ok               |
|          30 | -35.64%  | 158.27%            | -57.21% |    -0.33 |       71 | 52.08%     | ok               |
|          35 | -36.09%  | 158.27%            | -55.26% |    -0.36 |       73 | 49.75%     | ok               |
|          50 | -35.95%  | 158.27%            | -48.72% |    -0.4  |       52 | 37.60%     | ok               |
|          20 | -43.03%  | 158.27%            | -60.16% |    -0.44 |       74 | 57.40%     | ok               |

## AMD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 6.74%    | 186.10%            | -44.26% |     0.27 |       54 | 30.62%     | ok               |
|          40 | 5.86%    | 186.10%            | -43.98% |     0.27 |       52 | 35.77%     | ok               |
|          35 | -5.47%   | 186.10%            | -50.71% |     0.16 |       60 | 37.27%     | ok               |
|          45 | -14.79%  | 186.10%            | -53.24% |     0.04 |       60 | 33.44%     | ok               |
|          30 | -17.93%  | 186.10%            | -56.46% |     0.02 |       61 | 39.77%     | ok               |

## AMGN Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -9.83%   | 27.17%             | -26.64% |    -0.12 |       71 | 52.41%     | ok               |
|          35 | -11.27%  | 27.17%             | -31.23% |    -0.18 |       65 | 42.43%     | ok               |
|          15 | -14.46%  | 27.17%             | -27.92% |    -0.22 |       67 | 57.74%     | ok               |
|          30 | -15.41%  | 27.17%             | -34.14% |    -0.29 |       69 | 46.26%     | ok               |
|          25 | -18.85%  | 27.17%             | -33.41% |    -0.37 |       65 | 48.59%     | ok               |

## AMZN Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -17.17%  | 43.07%             | -27.15% |    -0.5  |       52 | 29.12%     | ok               |
|          50 | -23.56%  | 43.07%             | -34.08% |    -0.84 |       50 | 23.13%     | ok               |
|          45 | -26.38%  | 43.07%             | -34.08% |    -0.92 |       54 | 26.12%     | ok               |
|          35 | -30.79%  | 43.07%             | -38.29% |    -0.96 |       68 | 32.78%     | ok               |
|          30 | -36.95%  | 43.07%             | -42.48% |    -1.11 |       80 | 38.27%     | ok               |

## APT-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 19.10%   | -89.95%            | -46.73% |     0.42 |       40 | 18.97%     | ok               |
|          45 | -11.65%  | -89.95%            | -63.86% |     0.05 |       56 | 24.52%     | ok               |
|          20 | -35.67%  | -89.95%            | -70.51% |    -0.12 |       71 | 50.77%     | ok               |
|          40 | -28.66%  | -89.95%            | -63.33% |    -0.14 |       64 | 30.08%     | ok               |
|          35 | -33.89%  | -89.95%            | -64.45% |    -0.18 |       68 | 35.82%     | ok               |

## ARB-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 27.91%   | -80.99%            | -53.74% |     0.49 |       87 | 57.09%     | ok               |
|          40 | 14.17%   | -80.99%            | -43.98% |     0.36 |       52 | 30.65%     | ok               |
|          20 | -3.87%   | -80.99%            | -60.40% |     0.24 |       75 | 50.57%     | ok               |
|          45 | 2.39%    | -80.99%            | -47.43% |     0.23 |       58 | 23.95%     | ok               |
|          35 | -0.22%   | -80.99%            | -54.43% |     0.23 |       64 | 33.91%     | ok               |

## ARKK Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -30.44%  | 49.66%             | -35.59% |    -0.41 |       95 | 51.41%     | ok               |
|          20 | -34.54%  | 49.66%             | -36.24% |    -0.53 |       90 | 46.76%     | ok               |
|          30 | -35.71%  | 49.66%             | -37.37% |    -0.65 |       85 | 39.93%     | ok               |
|          35 | -36.07%  | 49.66%             | -37.73% |    -0.69 |       84 | 37.44%     | ok               |
|          40 | -37.42%  | 49.66%             | -39.04% |    -0.77 |       76 | 32.61%     | ok               |

## ATOM-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -65.78%  | -69.07%            | -71.00% |    -1.01 |       93 | 51.15%     | ok               |
|          15 | -68.93%  | -69.07%            | -70.34% |    -1.01 |       93 | 61.49%     | ok               |
|          45 | -58.00%  | -69.07%            | -64.33% |    -1.08 |       72 | 28.74%     | ok               |
|          30 | -69.22%  | -69.07%            | -74.39% |    -1.2  |       88 | 44.44%     | ok               |
|          20 | -73.06%  | -69.07%            | -74.75% |    -1.22 |       97 | 54.79%     | ok               |

## AVAX-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 3.29%    | -74.02%            | -34.50% |     0.21 |       32 | 18.20%     | ok               |
|          45 | -6.13%   | -74.02%            | -41.07% |     0.07 |       36 | 22.03%     | ok               |
|          40 | -15.98%  | -74.02%            | -45.60% |    -0.06 |       40 | 24.90%     | ok               |
|          15 | -27.31%  | -74.02%            | -52.46% |    -0.07 |       73 | 53.07%     | ok               |
|          25 | -26.19%  | -74.02%            | -52.93% |    -0.11 |       71 | 42.53%     | ok               |

## AVGO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 16.61%   | 188.86%            | -35.84% |     0.36 |       56 | 30.62%     | ok               |
|          30 | 14.00%   | 188.86%            | -35.76% |     0.33 |       64 | 42.43%     | ok               |
|          40 | 12.63%   | 188.86%            | -40.70% |     0.31 |       62 | 36.27%     | ok               |
|          25 | 11.60%   | 188.86%            | -38.01% |     0.3  |       72 | 43.93%     | ok               |
|          45 | 10.69%   | 188.86%            | -41.66% |     0.29 |       58 | 34.11%     | ok               |

## BA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 26.03%   | 4.46%              | -13.34% |     0.67 |       42 | 31.45%     | ok               |
|          35 | 30.46%   | 4.46%              | -23.77% |     0.59 |       72 | 44.59%     | ok               |
|          40 | 20.11%   | 4.46%              | -23.90% |     0.47 |       46 | 38.60%     | ok               |
|          25 | 10.59%   | 4.46%              | -32.48% |     0.29 |       70 | 52.58%     | ok               |
|          30 | 7.60%    | 4.46%              | -30.56% |     0.25 |       67 | 49.25%     | ok               |

## BAC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 4.42%    | 79.77%             | -18.35% |     0.2  |       60 | 37.94%     | ok               |
|          50 | -0.08%   | 79.77%             | -19.12% |     0.06 |       60 | 34.61%     | ok               |
|          20 | -1.73%   | 79.77%             | -20.73% |     0.05 |       78 | 54.58%     | ok               |
|          35 | -1.09%   | 79.77%             | -27.11% |     0.05 |       70 | 46.09%     | ok               |
|          40 | -2.85%   | 79.77%             | -22.59% |    -0.01 |       64 | 40.93%     | ok               |

## BCH-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 1.09%    | -33.07%            | -48.11% |     0.24 |       73 | 54.41%     | ok               |
|          15 | -2.08%   | -33.07%            | -52.32% |     0.21 |       80 | 59.00%     | ok               |
|          25 | -11.51%  | -33.07%            | -54.62% |     0.09 |       72 | 50.57%     | ok               |
|          30 | -10.98%  | -33.07%            | -54.34% |     0.08 |       80 | 48.47%     | ok               |
|          35 | -23.92%  | -33.07%            | -64.08% |    -0.11 |       72 | 44.44%     | ok               |

## BITO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 14.55%   | -65.81%            | -31.98% |     0.34 |       54 | 24.46%     | ok               |
|          45 | -3.63%   | -65.81%            | -41.16% |     0.11 |       62 | 28.12%     | ok               |
|          30 | -5.95%   | -65.81%            | -42.82% |     0.11 |       80 | 41.10%     | ok               |
|          40 | -7.94%   | -65.81%            | -43.67% |     0.06 |       66 | 32.95%     | ok               |
|          15 | -12.88%  | -65.81%            | -48.38% |     0.06 |       89 | 50.08%     | ok               |

## BLK Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | -0.89%   | 30.78%             | -17.97% |     0.04 |       74 | 38.27%     | ok               |
|          20 | -3.15%   | 30.78%             | -21.48% |    -0.01 |       78 | 47.09%     | ok               |
|          40 | -4.56%   | 30.78%             | -20.08% |    -0.09 |       68 | 34.28%     | ok               |
|          30 | -7.20%   | 30.78%             | -24.29% |    -0.15 |       69 | 42.26%     | ok               |
|          25 | -8.14%   | 30.78%             | -23.36% |    -0.17 |       69 | 44.59%     | ok               |

## BND Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -6.44%   | 0.87%              | -9.15%  |    -0.93 |       65 | 38.94%     | ok               |
|          25 | -7.13%   | 0.87%              | -10.23% |    -1.08 |       69 | 36.94%     | ok               |
|          30 | -7.58%   | 0.87%              | -9.98%  |    -1.22 |       67 | 33.11%     | ok               |
|          15 | -8.64%   | 0.87%              | -10.93% |    -1.24 |       75 | 41.76%     | ok               |
|          45 | -7.82%   | 0.87%              | -9.57%  |    -1.51 |       52 | 22.80%     | ok               |

## BONK-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 170.82%  | -82.09%            | -35.57% |     1.24 |       46 | 22.22%     | ok               |
|          25 | 162.55%  | -82.09%            | -46.61% |     1.02 |       67 | 48.28%     | ok               |
|          20 | 147.72%  | -82.09%            | -54.25% |     0.97 |       68 | 52.87%     | ok               |
|          15 | 153.39%  | -82.09%            | -62.48% |     0.96 |       71 | 57.85%     | ok               |
|          45 | 82.77%   | -82.09%            | -42.36% |     0.83 |       56 | 26.82%     | ok               |

## BTC-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 46.18%   | -32.96%            | -14.53% |     0.84 |       46 | 34.87%     | ok               |
|          45 | 40.84%   | -32.96%            | -15.18% |     0.81 |       44 | 30.65%     | ok               |
|          35 | 28.81%   | -32.96%            | -26.34% |     0.58 |       70 | 41.76%     | ok               |
|          50 | 13.98%   | -32.96%            | -18.05% |     0.4  |       42 | 25.29%     | ok               |
|          30 | 13.35%   | -32.96%            | -21.75% |     0.35 |       74 | 48.47%     | ok               |

## C Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -6.29%   | 132.51%            | -22.28% |    -0.1  |       64 | 36.11%     | ok               |
|          45 | -18.56%  | 132.51%            | -30.30% |    -0.43 |       76 | 40.27%     | ok               |
|          25 | -27.45%  | 132.51%            | -35.32% |    -0.52 |       71 | 53.08%     | ok               |
|          15 | -29.86%  | 132.51%            | -36.66% |    -0.54 |       72 | 60.07%     | ok               |
|          40 | -24.27%  | 132.51%            | -35.18% |    -0.56 |       76 | 42.60%     | ok               |

## CAT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 21.25%   | 165.63%            | -21.02% |     0.44 |       72 | 55.57%     | ok               |
|          25 | 21.36%   | 165.63%            | -26.37% |     0.44 |       68 | 58.40%     | ok               |
|          20 | 19.91%   | 165.63%            | -25.65% |     0.42 |       78 | 61.90%     | ok               |
|          45 | 16.29%   | 165.63%            | -27.12% |     0.38 |       56 | 44.26%     | ok               |
|          35 | 13.29%   | 165.63%            | -27.72% |     0.33 |       70 | 49.08%     | ok               |

## CL Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 10.39%   | 6.71%              | -11.22% |     0.45 |       44 | 29.45%     | ok               |
|          30 | 7.73%    | 6.71%              | -14.32% |     0.31 |       62 | 45.59%     | ok               |
|          45 | 3.25%    | 6.71%              | -13.51% |     0.18 |       48 | 32.61%     | ok               |
|          35 | 2.60%    | 6.71%              | -13.83% |     0.15 |       64 | 41.93%     | ok               |
|          40 | -0.38%   | 6.71%              | -12.70% |     0.04 |       58 | 36.61%     | ok               |

## CMCSA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -38.45%  | -39.86%            | -44.02% |    -0.87 |       90 | 57.24%     | ok               |
|          30 | -40.78%  | -39.86%            | -41.06% |    -1.09 |       82 | 42.10%     | ok               |
|          25 | -43.84%  | -39.86%            | -43.88% |    -1.18 |       90 | 47.59%     | ok               |
|          50 | -31.11%  | -39.86%            | -32.82% |    -1.24 |       50 | 14.31%     | ok               |
|          20 | -49.01%  | -39.86%            | -49.05% |    -1.33 |       95 | 53.24%     | ok               |

## COMP-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -4.94%   | -70.29%            | -38.71% |     0.13 |       44 | 20.11%     | ok               |
|          30 | -42.10%  | -70.29%            | -57.88% |    -0.3  |       89 | 45.59%     | ok               |
|          25 | -45.12%  | -70.29%            | -61.30% |    -0.31 |       89 | 52.11%     | ok               |
|          15 | -54.40%  | -70.29%            | -66.20% |    -0.43 |      107 | 63.60%     | ok               |
|          40 | -44.69%  | -70.29%            | -50.69% |    -0.45 |       72 | 33.52%     | ok               |

## COP Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -4.23%   | 2.90%              | -34.85% |    -0.01 |       48 | 28.12%     | ok               |
|          35 | -17.36%  | 2.90%              | -43.58% |    -0.28 |       73 | 38.60%     | ok               |
|          45 | -15.54%  | 2.90%              | -41.14% |    -0.29 |       62 | 31.45%     | ok               |
|          30 | -21.65%  | 2.90%              | -43.96% |    -0.38 |       72 | 42.10%     | ok               |
|          40 | -20.88%  | 2.90%              | -46.86% |    -0.41 |       68 | 34.61%     | ok               |

## COST Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 8.59%    | 25.55%             | -24.32% |     0.31 |       66 | 49.75%     | ok               |
|          25 | 6.98%    | 25.55%             | -24.73% |     0.27 |       63 | 46.92%     | ok               |
|          35 | 2.01%    | 25.55%             | -26.58% |     0.13 |       54 | 40.27%     | ok               |
|          30 | -2.66%   | 25.55%             | -29.73% |    -0.01 |       60 | 43.26%     | ok               |
|          15 | -5.59%   | 25.55%             | -27.30% |    -0.07 |       69 | 53.24%     | ok               |

## CRM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -35.79%  | -42.15%            | -44.67% |    -0.57 |       90 | 54.91%     | ok               |
|          35 | -29.63%  | -42.15%            | -33.08% |    -0.59 |       60 | 37.94%     | ok               |
|          40 | -34.83%  | -42.15%            | -39.11% |    -0.8  |       66 | 33.94%     | ok               |
|          20 | -43.35%  | -42.15%            | -45.69% |    -0.82 |       74 | 48.59%     | ok               |
|          30 | -39.56%  | -42.15%            | -41.36% |    -0.83 |       63 | 42.76%     | ok               |

## CRV-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 18.17%   | -57.77%            | -37.78% |     0.4  |       72 | 31.80%     | ok               |
|          45 | 3.69%    | -57.77%            | -42.29% |     0.24 |       58 | 21.07%     | ok               |
|          40 | -2.10%   | -57.77%            | -38.86% |     0.19 |       62 | 27.39%     | ok               |
|          50 | -0.89%   | -57.77%            | -29.30% |     0.18 |       46 | 17.43%     | ok               |
|          30 | -6.16%   | -57.77%            | -39.89% |     0.17 |       70 | 36.40%     | ok               |

## CSCO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 33.04%   | 128.72%            | -19.34% |     0.72 |       50 | 37.44%     | ok               |
|          45 | 28.54%   | 128.72%            | -19.34% |     0.63 |       51 | 39.10%     | ok               |
|          35 | 23.63%   | 128.72%            | -23.68% |     0.52 |       53 | 45.92%     | ok               |
|          25 | 21.97%   | 128.72%            | -23.28% |     0.49 |       65 | 50.58%     | ok               |
|          30 | 21.40%   | 128.72%            | -21.79% |     0.48 |       61 | 48.59%     | ok               |

## CVX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -9.42%   | 22.83%             | -27.34% |    -0.22 |       77 | 34.78%     | ok               |
|          25 | -10.93%  | 22.83%             | -24.33% |    -0.22 |       75 | 42.60%     | ok               |
|          35 | -10.87%  | 22.83%             | -28.85% |    -0.25 |       69 | 37.10%     | ok               |
|          45 | -10.60%  | 22.83%             | -28.83% |    -0.27 |       67 | 30.95%     | ok               |
|          30 | -14.51%  | 22.83%             | -29.13% |    -0.35 |       75 | 39.93%     | ok               |

## DASH-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 109.42%  | 25.64%             | -24.52% |     0.89 |       38 | 14.75%     | ok               |
|          40 | 64.68%   | 25.64%             | -28.66% |     0.67 |       46 | 21.65%     | ok               |
|          45 | 50.99%   | 25.64%             | -33.08% |     0.6  |       42 | 16.86%     | ok               |
|          35 | -38.60%  | 25.64%             | -63.23% |     0.01 |       67 | 26.25%     | ok               |
|          30 | -41.76%  | 25.64%             | -64.43% |    -0.02 |       61 | 29.12%     | ok               |

## DBC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -6.08%   | 32.82%             | -27.14% |    -0.15 |       75 | 39.27%     | ok               |
|          50 | -5.99%   | 32.82%             | -20.31% |    -0.2  |       42 | 21.80%     | ok               |
|          35 | -8.56%   | 32.82%             | -23.91% |    -0.26 |       64 | 32.45%     | ok               |
|          25 | -9.01%   | 32.82%             | -26.10% |    -0.27 |       64 | 35.61%     | ok               |
|          45 | -8.59%   | 32.82%             | -21.46% |    -0.29 |       58 | 25.46%     | ok               |

## DE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -6.71%   | 61.34%             | -28.94% |    -0.04 |       74 | 52.75%     | ok               |
|          50 | -5.81%   | 61.34%             | -23.21% |    -0.07 |       70 | 31.45%     | ok               |
|          25 | -9.02%   | 61.34%             | -26.67% |    -0.1  |       76 | 50.08%     | ok               |
|          30 | -9.04%   | 61.34%             | -25.24% |    -0.1  |       74 | 47.25%     | ok               |
|          45 | -7.74%   | 61.34%             | -26.88% |    -0.11 |       70 | 35.94%     | ok               |

## DIA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | -2.24%   | 32.56%             | -13.15% |    -0.09 |       62 | 41.76%     | ok               |
|          25 | -2.77%   | 32.56%             | -11.28% |    -0.11 |       62 | 45.09%     | ok               |
|          30 | -4.26%   | 32.56%             | -12.94% |    -0.2  |       62 | 43.93%     | ok               |
|          20 | -6.10%   | 32.56%             | -13.85% |    -0.28 |       66 | 47.42%     | ok               |
|          40 | -6.23%   | 32.56%             | -15.06% |    -0.34 |       68 | 38.94%     | ok               |

## DIS Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 19.76%   | -10.47%            | -14.24% |     0.62 |       50 | 27.29%     | ok               |
|          45 | -5.26%   | -10.47%            | -16.54% |    -0.05 |       53 | 30.95%     | ok               |
|          40 | -6.74%   | -10.47%            | -23.29% |    -0.06 |       65 | 36.27%     | ok               |
|          15 | -16.99%  | -10.47%            | -31.15% |    -0.24 |       88 | 56.91%     | ok               |
|          35 | -16.07%  | -10.47%            | -25.70% |    -0.28 |       75 | 42.26%     | ok               |

## DOGE-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 8.84%    | -73.27%            | -57.89% |     0.36 |       79 | 66.09%     | ok               |
|          20 | -6.28%   | -73.27%            | -55.83% |     0.22 |       78 | 60.54%     | ok               |
|          25 | -7.14%   | -73.27%            | -53.72% |     0.2  |       68 | 55.56%     | ok               |
|          30 | -22.30%  | -73.27%            | -60.95% |     0.02 |       71 | 50.00%     | ok               |
|          35 | -49.12%  | -73.27%            | -63.16% |    -0.45 |       68 | 43.30%     | ok               |

## DOT-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -35.10%  | -83.39%            | -46.87% |    -0.45 |       58 | 25.67%     | ok               |
|          45 | -37.93%  | -83.39%            | -50.16% |    -0.46 |       50 | 30.84%     | ok               |
|          35 | -52.94%  | -83.39%            | -60.35% |    -0.53 |       74 | 41.19%     | ok               |
|          40 | -44.16%  | -83.39%            | -51.87% |    -0.55 |       52 | 33.91%     | ok               |
|          30 | -57.70%  | -83.39%            | -63.10% |    -0.61 |       84 | 47.51%     | ok               |

## DXY-INDEX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -1.53%   | 0.38%              | -6.02%  |    -0.23 |       40 | 30.80%     | ok               |
|          15 | -3.88%   | 0.38%              | -11.37% |    -0.34 |       82 | 77.01%     | ok               |
|          40 | -5.28%   | 0.38%              | -8.08%  |    -0.67 |       72 | 50.54%     | ok               |
|          25 | -6.70%   | 0.38%              | -12.10% |    -0.73 |       80 | 67.03%     | ok               |
|          35 | -6.24%   | 0.38%              | -10.39% |    -0.76 |       71 | 57.05%     | ok               |

## EEM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -5.62%   | 57.25%             | -19.52% |    -0.14 |       64 | 39.10%     | ok               |
|          35 | -6.28%   | 57.25%             | -23.88% |    -0.14 |       66 | 41.10%     | ok               |
|          50 | -5.60%   | 57.25%             | -15.88% |    -0.15 |       52 | 35.11%     | ok               |
|          45 | -6.69%   | 57.25%             | -17.36% |    -0.18 |       54 | 36.77%     | ok               |
|          30 | -10.02%  | 57.25%             | -25.67% |    -0.27 |       64 | 42.76%     | ok               |

## EFA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -2.91%   | 32.71%             | -10.80% |    -0.04 |       62 | 52.25%     | ok               |
|          20 | -9.65%   | 32.71%             | -12.73% |    -0.33 |       69 | 49.25%     | ok               |
|          30 | -9.55%   | 32.71%             | -15.14% |    -0.35 |       62 | 44.59%     | ok               |
|          50 | -8.94%   | 32.71%             | -17.56% |    -0.39 |       54 | 36.11%     | ok               |
|          25 | -11.78%  | 32.71%             | -16.37% |    -0.44 |       64 | 46.59%     | ok               |

## EOG Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -16.64%  | 25.92%             | -39.69% |    -0.36 |       58 | 33.61%     | ok               |
|          30 | -21.46%  | 25.92%             | -48.13% |    -0.43 |       81 | 47.42%     | ok               |
|          40 | -21.57%  | 25.92%             | -43.26% |    -0.49 |       66 | 36.94%     | ok               |
|          35 | -22.33%  | 25.92%             | -46.26% |    -0.49 |       79 | 42.10%     | ok               |
|          25 | -25.45%  | 25.92%             | -51.99% |    -0.51 |       82 | 50.42%     | ok               |

## ETC-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 1.95%    | -66.76%            | -27.89% |     0.16 |       24 | 15.71%     | ok               |
|          35 | -9.67%   | -66.76%            | -42.62% |    -0.01 |       44 | 25.29%     | ok               |
|          45 | -8.31%   | -66.76%            | -35.44% |    -0.02 |       24 | 17.43%     | ok               |
|          40 | -13.75%  | -66.76%            | -40.48% |    -0.12 |       40 | 21.26%     | ok               |
|          30 | -31.63%  | -66.76%            | -45.98% |    -0.43 |       64 | 29.50%     | ok               |

## ETH-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 147.60%  | -28.62%            | -30.11% |     1.23 |       64 | 44.83%     | ok               |
|          30 | 111.99%  | -28.62%            | -32.89% |     1.02 |       68 | 53.45%     | ok               |
|          40 | 43.79%   | -28.62%            | -33.11% |     0.64 |       62 | 37.16%     | ok               |
|          15 | 45.68%   | -28.62%            | -42.74% |     0.61 |       77 | 68.77%     | ok               |
|          20 | 44.14%   | -28.62%            | -39.10% |     0.61 |       82 | 63.03%     | ok               |

## EWJ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -19.59%  | 31.06%             | -30.73% |    -0.65 |       62 | 38.60%     | ok               |
|          20 | -20.96%  | 31.06%             | -31.32% |    -0.68 |       58 | 40.60%     | ok               |
|          25 | -23.24%  | 31.06%             | -31.18% |    -0.78 |       58 | 39.60%     | ok               |
|          45 | -20.37%  | 31.06%             | -27.68% |    -0.79 |       58 | 30.78%     | ok               |
|          35 | -23.45%  | 31.06%             | -32.54% |    -0.81 |       68 | 36.94%     | ok               |

## FCX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -4.31%   | 54.59%             | -27.70% |     0.06 |       52 | 29.78%     | ok               |
|          45 | -8.44%   | 54.59%             | -35.18% |    -0    |       52 | 34.28%     | ok               |
|          40 | -19.35%  | 54.59%             | -43.57% |    -0.19 |       62 | 38.60%     | ok               |
|          30 | -27.81%  | 54.59%             | -47.47% |    -0.31 |       63 | 45.26%     | ok               |
|          35 | -32.25%  | 54.59%             | -50.71% |    -0.42 |       69 | 43.43%     | ok               |

## FET-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -1.87%   | -79.79%            | -59.54% |     0.3  |       88 | 53.07%     | ok               |
|          15 | -16.53%  | -79.79%            | -59.58% |     0.19 |       84 | 56.90%     | ok               |
|          25 | -35.79%  | -79.79%            | -60.09% |    -0.06 |       91 | 46.74%     | ok               |
|          30 | -39.27%  | -79.79%            | -54.02% |    -0.14 |       85 | 42.34%     | ok               |
|          35 | -53.75%  | -79.79%            | -62.73% |    -0.5  |       73 | 34.10%     | ok               |

## FIL-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -23.47%  | -78.37%            | -39.40% |    -0.21 |       46 | 22.80%     | ok               |
|          35 | -44.88%  | -78.37%            | -47.50% |    -0.62 |       56 | 26.82%     | ok               |
|          30 | -47.52%  | -78.37%            | -50.22% |    -0.63 |       70 | 32.38%     | ok               |
|          45 | -41.18%  | -78.37%            | -43.98% |    -0.65 |       40 | 17.05%     | ok               |
|          50 | -39.00%  | -78.37%            | -44.95% |    -0.69 |       36 | 12.64%     | ok               |

## FXI Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -6.30%   | 46.55%             | -22.57% |    -0.07 |       44 | 31.28%     | ok               |
|          30 | -6.84%   | 46.55%             | -23.91% |    -0.09 |       44 | 30.12%     | ok               |
|          45 | -6.49%   | 46.55%             | -26.75% |    -0.09 |       44 | 24.63%     | ok               |
|          15 | -10.11%  | 46.55%             | -21.68% |    -0.15 |       54 | 34.94%     | ok               |
|          50 | -9.19%   | 46.55%             | -24.76% |    -0.18 |       44 | 21.63%     | ok               |

## GDX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 18.06%   | 169.49%            | -35.59% |     0.39 |       73 | 52.91%     | ok               |
|          40 | 13.85%   | 169.49%            | -31.87% |     0.35 |       64 | 42.93%     | ok               |
|          30 | 11.28%   | 169.49%            | -34.99% |     0.3  |       60 | 48.09%     | ok               |
|          35 | 8.95%    | 169.49%            | -32.37% |     0.27 |       68 | 45.26%     | ok               |
|          25 | 6.77%    | 169.49%            | -38.90% |     0.24 |       63 | 49.75%     | ok               |

## GDXJ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -8.75%   | 187.07%            | -45.05% |     0.05 |       67 | 52.75%     | ok               |
|          30 | -22.87%  | 187.07%            | -44.93% |    -0.21 |       66 | 46.09%     | ok               |
|          50 | -20.22%  | 187.07%            | -44.94% |    -0.22 |       58 | 37.77%     | ok               |
|          25 | -26.29%  | 187.07%            | -47.26% |    -0.24 |       70 | 49.58%     | ok               |
|          35 | -26.51%  | 187.07%            | -43.49% |    -0.29 |       68 | 43.76%     | ok               |

## GE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 27.50%   | 176.31%            | -22.29% |     0.57 |       66 | 39.43%     | ok               |
|          45 | 17.87%   | 176.31%            | -25.68% |     0.42 |       74 | 42.26%     | ok               |
|          20 | 11.67%   | 176.31%            | -26.63% |     0.31 |       71 | 56.57%     | ok               |
|          35 | 8.42%    | 176.31%            | -27.11% |     0.26 |       80 | 47.75%     | ok               |
|          30 | 8.17%    | 176.31%            | -27.82% |     0.26 |       76 | 52.91%     | ok               |

## GLD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 33.00%   | 95.32%             | -14.61% |     0.77 |       48 | 50.58%     | ok               |
|          25 | 32.31%   | 95.32%             | -14.61% |     0.77 |       48 | 49.08%     | ok               |
|          30 | 26.01%   | 95.32%             | -16.63% |     0.65 |       50 | 47.92%     | ok               |
|          15 | 24.85%   | 95.32%             | -17.54% |     0.6  |       50 | 54.74%     | ok               |
|          35 | 17.08%   | 95.32%             | -17.29% |     0.48 |       54 | 46.09%     | ok               |

## GOOGL Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 77.95%   | 155.86%            | -19.52% |     1.19 |       61 | 48.75%     | ok               |
|          30 | 76.40%   | 155.86%            | -20.41% |     1.15 |       57 | 52.58%     | ok               |
|          45 | 65.17%   | 155.86%            | -15.47% |     1.12 |       54 | 41.76%     | ok               |
|          25 | 73.72%   | 155.86%            | -19.76% |     1.11 |       55 | 54.58%     | ok               |
|          15 | 71.95%   | 155.86%            | -13.81% |     1.05 |       69 | 61.73%     | ok               |

## GRT-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 16.20%   | -87.96%            | -35.66% |     0.39 |       42 | 21.46%     | ok               |
|          15 | -7.55%   | -87.96%            | -49.67% |     0.18 |       73 | 60.73%     | ok               |
|          20 | -10.76%  | -87.96%            | -46.47% |     0.13 |       81 | 55.17%     | ok               |
|          35 | -8.90%   | -87.96%            | -48.22% |     0.09 |       60 | 36.02%     | ok               |
|          45 | -6.41%   | -87.96%            | -46.59% |     0.09 |       50 | 27.01%     | ok               |

## GS Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 21.11%   | 170.37%            | -20.56% |     0.47 |       74 | 61.06%     | ok               |
|          20 | 4.59%    | 170.37%            | -23.19% |     0.19 |       74 | 57.07%     | ok               |
|          40 | 0.08%    | 170.37%            | -17.88% |     0.09 |       72 | 45.26%     | ok               |
|          25 | -0.70%   | 170.37%            | -23.32% |     0.09 |       74 | 54.58%     | ok               |
|          30 | -2.38%   | 170.37%            | -22.13% |     0.05 |       76 | 52.08%     | ok               |

## HD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -7.53%   | -10.38%            | -17.69% |    -0.12 |       71 | 44.59%     | ok               |
|          25 | -8.25%   | -10.38%            | -18.51% |    -0.14 |       70 | 46.59%     | ok               |
|          15 | -17.75%  | -10.38%            | -27.53% |    -0.37 |      110 | 55.57%     | ok               |
|          35 | -15.13%  | -10.38%            | -22.98% |    -0.38 |       80 | 40.43%     | ok               |
|          40 | -13.89%  | -10.38%            | -19.63% |    -0.39 |       84 | 34.11%     | ok               |

## HON Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -13.43%  | 14.87%             | -21.17% |    -0.4  |       72 | 31.78%     | ok               |
|          45 | -15.16%  | 14.87%             | -19.99% |    -0.43 |       74 | 36.77%     | ok               |
|          40 | -23.52%  | 14.87%             | -26.29% |    -0.66 |       76 | 41.10%     | ok               |
|          35 | -24.98%  | 14.87%             | -27.37% |    -0.69 |       91 | 47.42%     | ok               |
|          30 | -26.82%  | 14.87%             | -29.80% |    -0.72 |       93 | 52.41%     | ok               |

## HYG Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -7.92%   | 3.35%              | -7.92%  |    -0.96 |       70 | 29.45%     | ok               |
|          15 | -9.71%   | 3.35%              | -10.06% |    -1.05 |       88 | 41.43%     | ok               |
|          20 | -9.69%   | 3.35%              | -10.29% |    -1.08 |       86 | 39.10%     | ok               |
|          45 | -8.60%   | 3.35%              | -8.60%  |    -1.08 |       66 | 26.29%     | ok               |
|          30 | -9.52%   | 3.35%              | -9.59%  |    -1.11 |       81 | 34.28%     | ok               |

## IBIT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 53.73%   | -2.95%             | -17.37% |     1.06 |       22 | 22.22%     | ok               |
|          15 | 56.91%   | -2.95%             | -19.20% |     0.95 |       40 | 39.58%     | ok               |
|          45 | 44.27%   | -2.95%             | -17.37% |     0.9  |       26 | 23.61%     | ok               |
|          40 | 38.04%   | -2.95%             | -17.78% |     0.8  |       26 | 25.46%     | ok               |
|          30 | 30.82%   | -2.95%             | -18.95% |     0.66 |       34 | 31.94%     | ok               |

## IBM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -9.02%   | 15.68%             | -43.33% |     0.02 |       93 | 61.90%     | ok               |
|          30 | -17.20%  | 15.68%             | -44.74% |    -0.15 |       77 | 49.75%     | ok               |
|          20 | -20.85%  | 15.68%             | -48.00% |    -0.19 |       75 | 54.41%     | ok               |
|          35 | -19.34%  | 15.68%             | -44.74% |    -0.2  |       71 | 45.42%     | ok               |
|          25 | -28.17%  | 15.68%             | -51.09% |    -0.34 |       74 | 52.41%     | ok               |

## ICP-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 1.02%    | -68.81%            | -32.85% |     0.21 |       50 | 23.75%     | ok               |
|          35 | -4.60%   | -68.81%            | -39.08% |     0.16 |       58 | 28.54%     | ok               |
|          30 | -17.50%  | -68.81%            | -52.81% |     0.08 |       77 | 34.48%     | ok               |
|          50 | -18.12%  | -68.81%            | -43.65% |    -0.09 |       32 | 14.18%     | ok               |
|          45 | -24.62%  | -68.81%            | -40.57% |    -0.18 |       52 | 18.01%     | ok               |

## IEF Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -7.10%   | -0.38%             | -9.79%  |    -0.85 |       72 | 42.43%     | ok               |
|          15 | -7.65%   | -0.38%             | -10.52% |    -0.9  |       71 | 43.93%     | ok               |
|          40 | -8.57%   | -0.38%             | -9.67%  |    -1.34 |       62 | 24.96%     | ok               |
|          45 | -8.24%   | -0.38%             | -9.73%  |    -1.36 |       52 | 22.96%     | ok               |
|          25 | -10.67%  | -0.38%             | -11.19% |    -1.36 |       78 | 39.60%     | ok               |

## IEMG Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -1.83%   | 51.84%             | -13.91% |    -0.01 |       52 | 33.28%     | ok               |
|          45 | -2.63%   | 51.84%             | -14.92% |    -0.04 |       48 | 35.77%     | ok               |
|          35 | -3.50%   | 51.84%             | -22.13% |    -0.06 |       63 | 41.26%     | ok               |
|          40 | -4.13%   | 51.84%             | -18.43% |    -0.09 |       60 | 38.77%     | ok               |
|          25 | -7.75%   | 51.84%             | -25.58% |    -0.2  |       59 | 44.09%     | ok               |

## INJ-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -12.71%  | -64.83%            | -55.31% |     0.03 |       46 | 22.61%     | ok               |
|          35 | -18.38%  | -64.83%            | -60.42% |     0.01 |       62 | 32.76%     | ok               |
|          50 | -22.20%  | -64.83%            | -51.00% |    -0.14 |       50 | 19.54%     | ok               |
|          40 | -26.76%  | -64.83%            | -57.21% |    -0.14 |       52 | 28.93%     | ok               |
|          25 | -53.26%  | -64.83%            | -81.57% |    -0.45 |       79 | 43.10%     | ok               |

## INTC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 99.89%   | 125.77%            | -53.65% |     0.81 |       81 | 59.73%     | ok               |
|          45 | 80.47%   | 125.77%            | -49.32% |     0.77 |       58 | 34.11%     | ok               |
|          20 | 86.64%   | 125.77%            | -52.47% |     0.76 |       80 | 55.91%     | ok               |
|          25 | 83.34%   | 125.77%            | -56.41% |     0.75 |       75 | 51.41%     | ok               |
|          40 | 74.55%   | 125.77%            | -55.86% |     0.72 |       66 | 38.44%     | ok               |

## INTU Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -0.28%   | -55.74%            | -40.73% |     0.11 |       69 | 27.95%     | ok               |
|          45 | -2.22%   | -55.74%            | -41.76% |     0.08 |       67 | 31.95%     | ok               |
|          40 | -8.64%   | -55.74%            | -45.15% |    -0.04 |       67 | 34.94%     | ok               |
|          35 | -15.62%  | -55.74%            | -46.75% |    -0.16 |       71 | 38.44%     | ok               |
|          25 | -18.48%  | -55.74%            | -39.87% |    -0.2  |       68 | 44.26%     | ok               |

## ITA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 0.61%    | 81.63%             | -21.48% |     0.09 |       76 | 38.10%     | ok               |
|          15 | -0.05%   | 81.63%             | -26.46% |     0.08 |       87 | 60.07%     | ok               |
|          30 | -2.88%   | 81.63%             | -23.75% |    -0.01 |       72 | 48.09%     | ok               |
|          35 | -4.95%   | 81.63%             | -23.16% |    -0.08 |       76 | 46.42%     | ok               |
|          40 | -6.04%   | 81.63%             | -20.58% |    -0.12 |       78 | 42.93%     | ok               |

## IWM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 8.60%    | 45.32%             | -14.08% |     0.39 |       42 | 31.28%     | ok               |
|          30 | 9.40%    | 45.32%             | -12.83% |     0.39 |       48 | 35.77%     | ok               |
|          25 | 9.50%    | 45.32%             | -13.55% |     0.39 |       50 | 36.94%     | ok               |
|          35 | 8.35%    | 45.32%             | -14.11% |     0.36 |       48 | 33.61%     | ok               |
|          20 | 5.19%    | 45.32%             | -14.08% |     0.24 |       60 | 37.94%     | ok               |

## JNJ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 19.24%   | 54.75%             | -10.57% |     0.79 |       56 | 37.60%     | ok               |
|          15 | 13.71%   | 54.75%             | -18.02% |     0.48 |       62 | 57.90%     | ok               |
|          45 | 10.73%   | 54.75%             | -13.35% |     0.46 |       56 | 42.43%     | ok               |
|          20 | 8.46%    | 54.75%             | -17.61% |     0.34 |       68 | 54.41%     | ok               |
|          40 | 5.40%    | 54.75%             | -14.77% |     0.25 |       62 | 46.76%     | ok               |

## JPM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 13.98%   | 84.81%             | -15.90% |     0.49 |       54 | 40.43%     | ok               |
|          45 | 3.15%    | 84.81%             | -21.91% |     0.16 |       56 | 43.43%     | ok               |
|          20 | -13.89%  | 84.81%             | -33.59% |    -0.23 |       86 | 58.40%     | ok               |
|          40 | -11.01%  | 84.81%             | -28.47% |    -0.25 |       68 | 46.09%     | ok               |
|          35 | -16.26%  | 84.81%             | -27.43% |    -0.39 |       76 | 50.08%     | ok               |

## KO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 23.75%   | 35.27%             | -8.20%  |     0.85 |       51 | 37.94%     | ok               |
|          35 | 19.96%   | 35.27%             | -8.07%  |     0.75 |       54 | 36.61%     | ok               |
|          40 | 17.46%   | 35.27%             | -9.28%  |     0.71 |       56 | 33.44%     | ok               |
|          25 | 18.64%   | 35.27%             | -9.73%  |     0.69 |       57 | 40.60%     | ok               |
|          50 | 10.20%   | 35.27%             | -12.31% |     0.48 |       38 | 26.96%     | ok               |

## LDO-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 65.77%   | -78.04%            | -46.95% |     0.7  |       83 | 54.02%     | ok               |
|          20 | 50.39%   | -78.04%            | -44.97% |     0.63 |       87 | 49.43%     | ok               |
|          50 | 32.74%   | -78.04%            | -48.04% |     0.57 |       52 | 18.01%     | ok               |
|          30 | 28.67%   | -78.04%            | -60.93% |     0.49 |       78 | 40.42%     | ok               |
|          35 | 25.80%   | -78.04%            | -62.61% |     0.47 |       76 | 33.52%     | ok               |

## LIN Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -0.16%   | 15.08%             | -23.68% |     0.06 |       64 | 49.58%     | ok               |
|          25 | -0.43%   | 15.08%             | -22.01% |     0.05 |       63 | 41.60%     | ok               |
|          20 | -2.57%   | 15.08%             | -23.00% |    -0.02 |       62 | 44.76%     | ok               |
|          35 | -4.03%   | 15.08%             | -21.18% |    -0.1  |       62 | 32.28%     | ok               |
|          30 | -4.64%   | 15.08%             | -21.53% |    -0.11 |       66 | 38.77%     | ok               |

## LINK-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -13.84%  | -54.68%            | -49.35% |     0.1  |       75 | 43.10%     | ok               |
|          45 | -10.48%  | -54.68%            | -38.11% |     0.08 |       52 | 27.59%     | ok               |
|          50 | -10.05%  | -54.68%            | -36.52% |     0.07 |       42 | 22.22%     | ok               |
|          35 | -21.89%  | -54.68%            | -49.18% |    -0.02 |       61 | 37.74%     | ok               |
|          40 | -26.18%  | -54.68%            | -50.55% |    -0.11 |       57 | 31.99%     | ok               |

## LLY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 4.73%    | 48.58%             | -38.23% |     0.2  |       46 | 36.44%     | ok               |
|          15 | -4.58%   | 48.58%             | -48.12% |     0.07 |       63 | 59.90%     | ok               |
|          45 | -7.06%   | 48.58%             | -42.66% |    -0.02 |       54 | 39.93%     | ok               |
|          20 | -19.94%  | 48.58%             | -51.34% |    -0.21 |       72 | 54.91%     | ok               |
|          25 | -21.27%  | 48.58%             | -53.47% |    -0.25 |       68 | 52.25%     | ok               |

## LRCX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -10.54%  | 226.77%            | -60.45% |     0.08 |       83 | 53.91%     | ok               |
|          50 | -15.40%  | 226.77%            | -50.39% |    -0.04 |       80 | 35.61%     | ok               |
|          40 | -17.94%  | 226.77%            | -56.86% |    -0.05 |       72 | 41.43%     | ok               |
|          35 | -23.27%  | 226.77%            | -61.76% |    -0.12 |       80 | 43.43%     | ok               |
|          20 | -25.39%  | 226.77%            | -67.48% |    -0.13 |       89 | 49.42%     | ok               |

## LTC-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -11.72%  | -64.71%            | -44.78% |     0.01 |       58 | 32.38%     | ok               |
|          35 | -22.03%  | -64.71%            | -54.86% |    -0.12 |       68 | 43.49%     | ok               |
|          30 | -32.21%  | -64.71%            | -53.76% |    -0.26 |       72 | 50.00%     | ok               |
|          40 | -31.02%  | -64.71%            | -56.10% |    -0.29 |       60 | 38.70%     | ok               |
|          25 | -34.89%  | -64.71%            | -54.26% |    -0.29 |       76 | 52.49%     | ok               |

## MCD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 1.93%    | -9.92%             | -9.22%  |     0.14 |       40 | 20.80%     | ok               |
|          30 | -2.55%   | -9.92%             | -18.81% |    -0.05 |       75 | 38.10%     | ok               |
|          25 | -3.59%   | -9.92%             | -20.47% |    -0.09 |       75 | 40.77%     | ok               |
|          35 | -7.68%   | -9.92%             | -15.45% |    -0.29 |       67 | 34.44%     | ok               |
|          40 | -7.95%   | -9.92%             | -16.86% |    -0.33 |       71 | 28.79%     | ok               |

## META Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -12.91%  | 34.07%             | -31.45% |    -0.17 |       68 | 37.44%     | ok               |
|          40 | -22.48%  | 34.07%             | -36.03% |    -0.37 |       68 | 40.43%     | ok               |
|          25 | -30.13%  | 34.07%             | -41.24% |    -0.5  |       69 | 51.08%     | ok               |
|          50 | -26.20%  | 34.07%             | -34.15% |    -0.52 |       72 | 33.61%     | ok               |
|          30 | -32.00%  | 34.07%             | -40.38% |    -0.57 |       74 | 47.92%     | ok               |

## MPC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 24.33%   | 82.85%             | -23.96% |     0.53 |       52 | 37.60%     | ok               |
|          45 | 16.44%   | 82.85%             | -25.09% |     0.4  |       58 | 41.26%     | ok               |
|          40 | 14.68%   | 82.85%             | -25.70% |     0.37 |       60 | 43.59%     | ok               |
|          35 | 11.13%   | 82.85%             | -35.90% |     0.31 |       68 | 46.09%     | ok               |
|          30 | -6.35%   | 82.85%             | -44.76% |     0.01 |       71 | 48.92%     | ok               |

## MRK Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -22.16%  | -3.45%             | -30.12% |    -0.41 |       89 | 55.24%     | ok               |
|          25 | -21.79%  | -3.45%             | -31.07% |    -0.44 |       74 | 47.25%     | ok               |
|          20 | -25.62%  | -3.45%             | -29.59% |    -0.54 |       79 | 50.58%     | ok               |
|          50 | -24.49%  | -3.45%             | -27.68% |    -0.7  |       60 | 29.95%     | ok               |
|          45 | -26.34%  | -3.45%             | -27.72% |    -0.71 |       61 | 33.28%     | ok               |

## MS Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -3.32%   | 146.22%            | -19.99% |     0    |       72 | 41.43%     | ok               |
|          15 | -4.98%   | 146.22%            | -22.02% |    -0.01 |       73 | 58.24%     | ok               |
|          20 | -5.09%   | 146.22%            | -25.68% |    -0.02 |       77 | 54.41%     | ok               |
|          30 | -10.18%  | 146.22%            | -27.79% |    -0.16 |       77 | 49.58%     | ok               |
|          35 | -10.11%  | 146.22%            | -25.26% |    -0.17 |       78 | 46.09%     | ok               |

## MSFT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -21.30%  | -1.29%             | -25.26% |    -0.59 |       64 | 33.78%     | ok               |
|          50 | -23.26%  | -1.29%             | -26.14% |    -0.68 |       60 | 28.95%     | ok               |
|          35 | -33.78%  | -1.29%             | -35.38% |    -0.9  |       71 | 42.43%     | ok               |
|          40 | -33.15%  | -1.29%             | -34.77% |    -0.92 |       67 | 37.27%     | ok               |
|          30 | -37.64%  | -1.29%             | -39.15% |    -0.99 |       81 | 47.09%     | ok               |

## MU Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 422.41%  | 867.43%            | -61.96% |     1.55 |       45 | 66.89%     | ok               |
|          25 | 338.97%  | 867.43%            | -67.90% |     1.48 |       47 | 61.23%     | ok               |
|          40 | 287.64%  | 867.43%            | -64.36% |     1.39 |       56 | 55.41%     | ok               |
|          20 | 296.99%  | 867.43%            | -67.25% |     1.37 |       51 | 62.90%     | ok               |
|          30 | 270.03%  | 867.43%            | -68.76% |     1.34 |       49 | 59.73%     | ok               |

## NEAR-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 60.52%   | -40.57%            | -48.95% |     0.74 |       40 | 22.41%     | ok               |
|          50 | 37.56%   | -40.57%            | -53.13% |     0.58 |       34 | 17.62%     | ok               |
|          40 | 34.34%   | -40.57%            | -57.15% |     0.54 |       44 | 26.63%     | ok               |
|          35 | 7.46%    | -40.57%            | -61.02% |     0.3  |       66 | 31.80%     | ok               |
|          15 | -11.22%  | -40.57%            | -54.94% |     0.2  |       87 | 55.56%     | ok               |

## NEM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 3.24%    | 197.23%            | -29.41% |     0.21 |       62 | 61.40%     | ok               |
|          20 | -7.81%   | 197.23%            | -30.47% |     0.07 |       72 | 56.91%     | ok               |
|          25 | -21.27%  | 197.23%            | -37.89% |    -0.14 |       68 | 54.74%     | ok               |
|          50 | -25.02%  | 197.23%            | -33.36% |    -0.27 |       58 | 40.43%     | ok               |
|          30 | -31.13%  | 197.23%            | -38.49% |    -0.33 |       72 | 53.08%     | ok               |

## NFLX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 46.92%   | 15.03%             | -11.94% |     0.98 |       46 | 45.42%     | ok               |
|          50 | 40.65%   | 15.03%             | -16.28% |     0.94 |       46 | 37.94%     | ok               |
|          35 | 41.59%   | 15.03%             | -18.30% |     0.86 |       64 | 49.25%     | ok               |
|          15 | 39.72%   | 15.03%             | -26.59% |     0.74 |       69 | 64.89%     | ok               |
|          45 | 31.03%   | 15.03%             | -15.48% |     0.73 |       52 | 41.76%     | ok               |

## NKE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | -27.03%  | -58.42%            | -42.13% |    -0.38 |       75 | 37.44%     | ok               |
|          20 | -33.86%  | -58.42%            | -50.44% |    -0.42 |       93 | 52.58%     | ok               |
|          25 | -34.08%  | -58.42%            | -51.20% |    -0.44 |       89 | 48.75%     | ok               |
|          15 | -38.05%  | -58.42%            | -55.28% |    -0.5  |       90 | 57.07%     | ok               |
|          40 | -26.61%  | -58.42%            | -31.33% |    -0.51 |       65 | 30.28%     | ok               |

## NOW Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 12.06%   | -32.86%            | -26.36% |     0.31 |       75 | 51.58%     | ok               |
|          30 | 8.05%    | -32.86%            | -27.34% |     0.26 |       78 | 45.59%     | ok               |
|          15 | 3.14%    | -32.86%            | -26.77% |     0.21 |       86 | 54.58%     | ok               |
|          25 | 1.91%    | -32.86%            | -27.28% |     0.19 |       70 | 48.92%     | ok               |
|          40 | -0.36%   | -32.86%            | -30.87% |     0.13 |       68 | 34.78%     | ok               |

## NVDA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -9.60%   | 146.63%            | -35.26% |     0.01 |       76 | 48.48%     | ok               |
|          20 | -14.87%  | 146.63%            | -40.59% |    -0.03 |       72 | 56.51%     | ok               |
|          25 | -14.73%  | 146.63%            | -33.22% |    -0.04 |       73 | 51.52%     | ok               |
|          50 | -18.25%  | 146.63%            | -40.84% |    -0.18 |       58 | 32.44%     | ok               |
|          15 | -26.95%  | 146.63%            | -45.02% |    -0.19 |       75 | 59.89%     | ok               |

## OP-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 27.06%   | -91.65%            | -36.11% |     0.51 |       30 | 11.11%     | ok               |
|          45 | 26.15%   | -91.65%            | -45.76% |     0.48 |       32 | 15.71%     | ok               |
|          40 | 5.05%    | -91.65%            | -53.61% |     0.26 |       50 | 24.52%     | ok               |
|          35 | -22.34%  | -91.65%            | -61.07% |    -0.06 |       56 | 27.59%     | ok               |
|          30 | -36.50%  | -91.65%            | -72.42% |    -0.21 |       72 | 34.10%     | ok               |

## ORCL Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 263.68%  | 9.38%              | -29.32% |     1.43 |       70 | 65.89%     | ok               |
|          25 | 172.82%  | 9.38%              | -27.76% |     1.17 |       71 | 58.40%     | ok               |
|          20 | 168.13%  | 9.38%              | -29.32% |     1.15 |       73 | 61.56%     | ok               |
|          35 | 132.06%  | 9.38%              | -31.95% |     1.04 |       64 | 50.42%     | ok               |
|          30 | 132.26%  | 9.38%              | -29.47% |     1.03 |       70 | 54.58%     | ok               |

## OXY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 3.47%    | -8.73%             | -30.14% |     0.18 |       70 | 40.93%     | ok               |
|          40 | 3.21%    | -8.73%             | -30.31% |     0.17 |       56 | 37.27%     | ok               |
|          50 | 2.93%    | -8.73%             | -32.02% |     0.16 |       46 | 30.12%     | ok               |
|          30 | 1.10%    | -8.73%             | -34.15% |     0.14 |       71 | 46.09%     | ok               |
|          45 | -6.22%   | -8.73%             | -35.02% |    -0.02 |       48 | 32.45%     | ok               |

## PEP Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 12.85%   | -19.49%            | -11.62% |     0.58 |       44 | 27.62%     | ok               |
|          45 | 5.64%    | -19.49%            | -14.22% |     0.28 |       60 | 31.61%     | ok               |
|          40 | 2.08%    | -19.49%            | -18.04% |     0.13 |       70 | 37.10%     | ok               |
|          35 | 1.55%    | -19.49%            | -21.42% |     0.11 |       79 | 41.93%     | ok               |
|          30 | -4.54%   | -19.49%            | -21.35% |    -0.07 |       75 | 48.25%     | ok               |

## PEPE-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 6.54%    | -70.47%            | -57.66% |     0.33 |       81 | 45.40%     | ok               |
|          15 | -2.83%   | -70.47%            | -64.84% |     0.32 |       82 | 62.26%     | ok               |
|          35 | -5.11%   | -70.47%            | -51.35% |     0.2  |       66 | 39.66%     | ok               |
|          25 | -13.09%  | -70.47%            | -53.88% |     0.17 |       93 | 51.34%     | ok               |
|          20 | -24.24%  | -70.47%            | -64.07% |     0.08 |       88 | 58.62%     | ok               |

## PFE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -24.91%  | -8.94%             | -26.10% |    -0.94 |       52 | 18.97%     | ok               |
|          50 | -26.23%  | -8.94%             | -27.28% |    -1.12 |       38 | 15.31%     | ok               |
|          40 | -31.91%  | -8.94%             | -33.01% |    -1.16 |       74 | 23.96%     | ok               |
|          35 | -35.54%  | -8.94%             | -37.03% |    -1.19 |       86 | 31.78%     | ok               |
|          30 | -41.51%  | -8.94%             | -42.34% |    -1.34 |       79 | 36.11%     | ok               |

## PG Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -8.34%   | -6.92%             | -20.08% |    -0.3  |       58 | 33.11%     | ok               |
|          35 | -11.47%  | -6.92%             | -18.99% |    -0.42 |       66 | 36.61%     | ok               |
|          30 | -19.51%  | -6.92%             | -24.55% |    -0.74 |       68 | 39.77%     | ok               |
|          45 | -17.29%  | -6.92%             | -22.43% |    -0.75 |       58 | 30.62%     | ok               |
|          25 | -21.34%  | -6.92%             | -26.24% |    -0.82 |       80 | 41.26%     | ok               |

## PM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | -0.28%   | 113.14%            | -32.20% |     0.09 |       86 | 52.08%     | ok               |
|          20 | -2.79%   | 113.14%            | -31.89% |     0.04 |       87 | 60.73%     | ok               |
|          30 | -3.22%   | 113.14%            | -33.68% |     0.03 |       83 | 55.74%     | ok               |
|          50 | -6.95%   | 113.14%            | -35.70% |    -0.09 |       74 | 42.10%     | ok               |
|          40 | -8.33%   | 113.14%            | -37.94% |    -0.12 |       80 | 48.25%     | ok               |

## POL-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 37.56%   | -74.72%            | -46.45% |     0.58 |       75 | 47.32%     | ok               |
|          25 | 21.28%   | -74.72%            | -46.72% |     0.43 |       68 | 55.17%     | ok               |
|          20 | 10.68%   | -74.72%            | -52.88% |     0.34 |       78 | 60.54%     | ok               |
|          15 | 3.67%    | -74.72%            | -58.42% |     0.28 |       76 | 66.28%     | ok               |
|          50 | 2.59%    | -74.72%            | -23.02% |     0.18 |       48 | 19.73%     | ok               |

## QCOM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -3.88%   | 8.46%              | -54.50% |     0.12 |       71 | 47.75%     | ok               |
|          35 | -4.42%   | 8.46%              | -50.58% |     0.11 |       77 | 43.59%     | ok               |
|          20 | -7.78%   | 8.46%              | -54.38% |     0.08 |       67 | 50.58%     | ok               |
|          30 | -15.25%  | 8.46%              | -56.59% |    -0.04 |       73 | 46.09%     | ok               |
|          15 | -23.11%  | 8.46%              | -57.94% |    -0.13 |       71 | 53.74%     | ok               |

## QQQ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 20.33%   | 59.45%             | -12.88% |     0.58 |       60 | 43.59%     | ok               |
|          25 | 20.78%   | 59.45%             | -12.88% |     0.58 |       57 | 46.26%     | ok               |
|          15 | 21.30%   | 59.45%             | -14.17% |     0.55 |       61 | 51.75%     | ok               |
|          20 | 17.86%   | 59.45%             | -12.98% |     0.5  |       65 | 48.92%     | ok               |
|          35 | 8.03%    | 59.45%             | -18.29% |     0.29 |       66 | 39.93%     | ok               |

## RENDER-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 45.25%   | -63.10%            | -43.43% |     0.61 |       88 | 53.29%     | ok               |
|          15 | 34.05%   | -63.10%            | -44.59% |     0.54 |       88 | 56.59%     | ok               |
|          25 | 15.90%   | -63.10%            | -40.60% |     0.42 |       90 | 49.03%     | ok               |
|          30 | -19.07%  | -63.10%            | -45.00% |     0.1  |       98 | 42.44%     | ok               |
|          35 | -31.74%  | -63.10%            | -41.33% |    -0.12 |       84 | 34.30%     | ok               |

## RTX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 32.90%   | 116.00%            | -18.66% |     0.76 |       74 | 56.41%     | ok               |
|          25 | 27.96%   | 116.00%            | -18.59% |     0.67 |       62 | 53.24%     | ok               |
|          50 | 21.94%   | 116.00%            | -18.42% |     0.66 |       56 | 42.43%     | ok               |
|          35 | 23.28%   | 116.00%            | -18.00% |     0.65 |       52 | 50.08%     | ok               |
|          30 | 26.01%   | 116.00%            | -16.99% |     0.64 |       56 | 52.08%     | ok               |

## SBUX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -11.16%  | 11.17%             | -23.55% |    -0.15 |       63 | 42.10%     | ok               |
|          40 | -15.57%  | 11.17%             | -25.43% |    -0.3  |       60 | 34.11%     | ok               |
|          45 | -15.10%  | 11.17%             | -27.26% |    -0.32 |       66 | 30.28%     | ok               |
|          30 | -18.75%  | 11.17%             | -29.22% |    -0.34 |       62 | 39.77%     | ok               |
|          35 | -20.34%  | 11.17%             | -27.06% |    -0.4  |       58 | 37.10%     | ok               |

## SCHW Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 10.78%   | 59.22%             | -16.53% |     0.37 |       56 | 35.44%     | ok               |
|          50 | 1.89%    | 59.22%             | -13.28% |     0.13 |       58 | 32.45%     | ok               |
|          25 | 0.34%    | 59.22%             | -28.76% |     0.1  |       61 | 50.42%     | ok               |
|          40 | -0.71%   | 59.22%             | -23.35% |     0.06 |       64 | 38.44%     | ok               |
|          20 | -3.89%   | 59.22%             | -29.24% |     0.01 |       71 | 52.75%     | ok               |

## SHIB-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -10.14%  | -73.80%            | -49.21% |     0.12 |       80 | 67.62%     | ok               |
|          20 | -14.96%  | -73.80%            | -46.38% |     0.06 |       77 | 63.22%     | ok               |
|          25 | -15.20%  | -73.80%            | -43.85% |     0.05 |       73 | 58.81%     | ok               |
|          35 | -24.41%  | -73.80%            | -53.32% |    -0.13 |       64 | 45.79%     | ok               |
|          30 | -29.98%  | -73.80%            | -47.96% |    -0.2  |       74 | 51.72%     | ok               |

## SHY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd    |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:-------|---------:|---------:|:-----------|:-----------------|
|          30 | -2.24%   | 0.42%              | -2.85% |    -0.79 |       48 | 34.28%     | ok               |
|          35 | -2.36%   | 0.42%              | -3.27% |    -0.84 |       50 | 32.45%     | ok               |
|          40 | -2.47%   | 0.42%              | -3.33% |    -0.89 |       50 | 30.62%     | ok               |
|          45 | -2.45%   | 0.42%              | -3.23% |    -0.9  |       48 | 27.45%     | ok               |
|          50 | -2.62%   | 0.42%              | -3.40% |    -1.01 |       44 | 24.63%     | ok               |

## SKY-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -28.58%  | 9.82%              | -44.74% |    -0.33 |       74 | 40.74%     | ok               |
|          15 | -32.94%  | 9.82%              | -56.39% |    -0.34 |       64 | 50.54%     | ok               |
|          25 | -32.24%  | 9.82%              | -48.09% |    -0.39 |       69 | 44.23%     | ok               |
|          20 | -42.57%  | 9.82%              | -58.40% |    -0.57 |       66 | 47.71%     | ok               |
|          35 | -37.92%  | 9.82%              | -49.68% |    -0.63 |       66 | 33.55%     | ok               |

## SLB Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 21.68%   | -4.47%             | -21.46% |     0.53 |       52 | 33.61%     | ok               |
|          40 | 17.91%   | -4.47%             | -25.33% |     0.45 |       46 | 37.10%     | ok               |
|          50 | -0.69%   | -4.47%             | -29.64% |     0.07 |       50 | 28.95%     | ok               |
|          35 | -12.19%  | -4.47%             | -43.52% |    -0.15 |       74 | 44.59%     | ok               |
|          30 | -23.87%  | -4.47%             | -54.23% |    -0.39 |       73 | 51.08%     | ok               |

## SLV Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 67.45%   | 147.24%            | -34.10% |     0.86 |       52 | 34.78%     | ok               |
|          45 | 65.43%   | 147.24%            | -31.82% |     0.83 |       58 | 35.94%     | ok               |
|          40 | 63.45%   | 147.24%            | -31.93% |     0.82 |       64 | 38.10%     | ok               |
|          20 | 54.23%   | 147.24%            | -42.66% |     0.72 |       66 | 47.42%     | ok               |
|          35 | 51.14%   | 147.24%            | -36.89% |     0.71 |       70 | 40.77%     | ok               |

## SMH Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 101.09%  | 165.67%            | -30.17% |     1.23 |       47 | 50.25%     | ok               |
|          35 | 79.97%   | 165.67%            | -34.36% |     1.09 |       54 | 46.09%     | ok               |
|          25 | 79.83%   | 165.67%            | -32.94% |     1.08 |       46 | 49.08%     | ok               |
|          30 | 77.71%   | 165.67%            | -33.99% |     1.07 |       48 | 47.42%     | ok               |
|          45 | 64.79%   | 165.67%            | -32.75% |     1.01 |       52 | 40.27%     | ok               |

## SNX-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 5.04%    | -76.52%            | -43.20% |     0.32 |       71 | 48.08%     | ok               |
|          35 | -6.26%   | -76.52%            | -30.08% |     0.17 |       62 | 30.84%     | ok               |
|          30 | -15.26%  | -76.52%            | -34.76% |     0.08 |       58 | 37.93%     | ok               |
|          15 | -29.21%  | -76.52%            | -44.00% |    -0.01 |       79 | 52.68%     | ok               |
|          25 | -25.66%  | -76.52%            | -38.88% |    -0.03 |       72 | 42.53%     | ok               |

## SOL-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 12.13%   | -59.81%            | -51.50% |     0.36 |       58 | 37.16%     | ok               |
|          25 | -21.61%  | -59.81%            | -52.40% |     0.04 |       74 | 57.47%     | ok               |
|          35 | -20.81%  | -59.81%            | -61.91% |     0.03 |       74 | 45.02%     | ok               |
|          45 | -16.39%  | -59.81%            | -59.86% |     0.03 |       62 | 31.80%     | ok               |
|          15 | -30.16%  | -59.81%            | -59.14% |    -0.05 |       76 | 63.60%     | ok               |

## SOXX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 86.21%   | 144.64%            | -38.67% |     1.07 |       55 | 49.08%     | ok               |
|          25 | 83.52%   | 144.64%            | -39.85% |     1.05 |       51 | 48.59%     | ok               |
|          35 | 78.39%   | 144.64%            | -38.63% |     1.03 |       59 | 43.93%     | ok               |
|          15 | 81.53%   | 144.64%            | -37.72% |     1    |       68 | 51.91%     | ok               |
|          30 | 73.21%   | 144.64%            | -40.34% |     0.97 |       55 | 46.42%     | ok               |

## SPY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 13.76%   | 46.66%             | -14.25% |     0.49 |       61 | 53.58%     | ok               |
|          15 | 12.21%   | 46.66%             | -16.80% |     0.44 |       70 | 56.74%     | ok               |
|          25 | 6.68%    | 46.66%             | -15.22% |     0.28 |       61 | 52.58%     | ok               |
|          30 | 2.18%    | 46.66%             | -16.47% |     0.14 |       64 | 49.75%     | ok               |
|          35 | 1.57%    | 46.66%             | -16.72% |     0.12 |       60 | 46.76%     | ok               |

## SUSHI-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -23.49%  | -81.32%            | -40.08% |    -0.19 |       52 | 14.75%     | ok               |
|          45 | -58.58%  | -81.32%            | -64.27% |    -0.77 |       56 | 18.20%     | ok               |
|          40 | -61.52%  | -81.32%            | -68.16% |    -0.77 |       63 | 24.71%     | ok               |
|          35 | -74.59%  | -81.32%            | -80.15% |    -1.06 |       82 | 30.65%     | ok               |
|          15 | -81.69%  | -81.32%            | -81.83% |    -1.09 |       95 | 48.47%     | ok               |

## T Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 59.37%   | 32.23%             | -18.13% |     1.14 |       58 | 57.40%     | ok               |
|          25 | 54.42%   | 32.23%             | -17.66% |     1.08 |       60 | 55.24%     | ok               |
|          15 | 49.65%   | 32.23%             | -15.08% |     0.98 |       69 | 61.40%     | ok               |
|          30 | 37.51%   | 32.23%             | -17.01% |     0.84 |       64 | 53.24%     | ok               |
|          35 | 23.37%   | 32.23%             | -14.49% |     0.6  |       66 | 49.75%     | ok               |

## TGT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -11.14%  | -7.03%             | -42.86% |    -0.11 |       83 | 46.42%     | ok               |
|          45 | -9.60%   | -7.03%             | -29.07% |    -0.15 |       54 | 28.62%     | ok               |
|          30 | -11.39%  | -7.03%             | -40.57% |    -0.15 |       60 | 38.60%     | ok               |
|          25 | -12.02%  | -7.03%             | -43.36% |    -0.15 |       65 | 41.43%     | ok               |
|          15 | -16.76%  | -7.03%             | -40.77% |    -0.21 |       73 | 51.08%     | ok               |

## TIA-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -2.21%   | -88.25%            | -49.23% |     0.16 |       54 | 18.77%     | ok               |
|          40 | -7.13%   | -88.25%            | -45.16% |     0.14 |       68 | 26.05%     | ok               |
|          35 | -8.27%   | -88.25%            | -52.59% |     0.14 |       68 | 31.03%     | ok               |
|          50 | -3.16%   | -88.25%            | -48.70% |     0.1  |       34 | 11.69%     | ok               |
|          30 | -45.10%  | -88.25%            | -67.89% |    -0.31 |       93 | 36.97%     | ok               |

## TLT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -21.12%  | -10.36%            | -21.87% |    -1.63 |       72 | 32.61%     | ok               |
|          50 | -14.45%  | -10.36%            | -15.73% |    -1.69 |       34 | 15.14%     | ok               |
|          40 | -19.49%  | -10.36%            | -20.09% |    -1.87 |       60 | 21.96%     | ok               |
|          15 | -26.90%  | -10.36%            | -27.76% |    -1.89 |       77 | 40.60%     | ok               |
|          35 | -21.89%  | -10.36%            | -22.47% |    -1.92 |       66 | 26.79%     | ok               |

## TMO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 46.41%   | -6.61%             | -8.17%  |     1.04 |       40 | 32.45%     | ok               |
|          45 | 42.16%   | -6.61%             | -10.13% |     0.92 |       46 | 37.27%     | ok               |
|          40 | 40.06%   | -6.61%             | -9.91%  |     0.86 |       49 | 41.76%     | ok               |
|          35 | 22.23%   | -6.61%             | -14.06% |     0.54 |       61 | 46.26%     | ok               |
|          30 | 16.75%   | -6.61%             | -18.85% |     0.42 |       61 | 51.41%     | ok               |

## TMUS Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 7.68%    | 19.36%             | -30.05% |     0.25 |       65 | 59.73%     | ok               |
|          30 | 6.48%    | 19.36%             | -25.71% |     0.23 |       70 | 47.75%     | ok               |
|          20 | 1.46%    | 19.36%             | -29.75% |     0.13 |       71 | 54.08%     | ok               |
|          25 | -1.94%   | 19.36%             | -31.45% |     0.06 |       75 | 50.25%     | ok               |
|          50 | -3.78%   | 19.36%             | -28.89% |    -0.03 |       60 | 35.77%     | ok               |

## TRX-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 11.18%   | 37.25%             | -18.79% |     0.4  |       50 | 36.97%     | ok               |
|          30 | 7.33%    | 37.25%             | -22.90% |     0.28 |       68 | 48.66%     | ok               |
|          35 | 6.44%    | 37.25%             | -21.77% |     0.26 |       64 | 45.40%     | ok               |
|          25 | 5.40%    | 37.25%             | -26.84% |     0.23 |       64 | 51.92%     | ok               |
|          20 | 5.10%    | 37.25%             | -25.45% |     0.22 |       61 | 55.36%     | ok               |

## TSLA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 56.12%   | 85.34%             | -32.60% |     0.73 |       64 | 29.78%     | ok               |
|          40 | 35.10%   | 85.34%             | -45.90% |     0.52 |       63 | 34.61%     | ok               |
|          45 | 14.45%   | 85.34%             | -46.86% |     0.34 |       67 | 31.95%     | ok               |
|          35 | 3.29%    | 85.34%             | -51.29% |     0.23 |       72 | 37.27%     | ok               |
|          30 | -14.59%  | 85.34%             | -54.91% |     0.05 |       70 | 41.26%     | ok               |

## TXN Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 17.86%   | 72.90%             | -45.45% |     0.4  |       64 | 34.61%     | ok               |
|          20 | 3.63%    | 72.90%             | -38.49% |     0.2  |       60 | 58.74%     | ok               |
|          35 | 0.79%    | 72.90%             | -43.28% |     0.15 |       74 | 49.25%     | ok               |
|          15 | -2.29%   | 72.90%             | -38.99% |     0.13 |       65 | 62.56%     | ok               |
|          40 | -1.29%   | 72.90%             | -45.67% |     0.11 |       68 | 46.76%     | ok               |

## UNH Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 27.43%   | -19.75%            | -26.96% |     0.49 |       74 | 52.58%     | ok               |
|          50 | 25.49%   | -19.75%            | -36.82% |     0.49 |       56 | 30.78%     | ok               |
|          15 | 26.14%   | -19.75%            | -32.14% |     0.46 |       75 | 67.55%     | ok               |
|          35 | 23.96%   | -19.75%            | -28.32% |     0.45 |       66 | 47.42%     | ok               |
|          40 | 21.05%   | -19.75%            | -35.73% |     0.42 |       60 | 42.60%     | ok               |

## UNI-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -18.78%  | -62.12%            | -63.75% |     0.02 |       58 | 33.33%     | ok               |
|          45 | -20.77%  | -62.12%            | -58.49% |    -0.03 |       58 | 28.16%     | ok               |
|          35 | -32.57%  | -62.12%            | -68.71% |    -0.13 |       70 | 38.70%     | ok               |
|          50 | -29.10%  | -62.12%            | -57.60% |    -0.19 |       54 | 21.46%     | ok               |
|          30 | -70.76%  | -62.12%            | -80.61% |    -0.81 |       86 | 44.64%     | ok               |

## UPS Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -31.90%  | -23.29%            | -43.07% |    -0.57 |       80 | 47.75%     | ok               |
|          25 | -32.99%  | -23.29%            | -39.04% |    -0.61 |       76 | 44.26%     | ok               |
|          15 | -35.86%  | -23.29%            | -43.86% |    -0.66 |       86 | 52.25%     | ok               |
|          35 | -34.34%  | -23.29%            | -39.90% |    -0.69 |       65 | 33.44%     | ok               |
|          30 | -37.14%  | -23.29%            | -38.83% |    -0.75 |       70 | 39.27%     | ok               |

## USO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 20.81%   | 72.43%             | -33.25% |     0.44 |       50 | 26.79%     | ok               |
|          20 | 18.96%   | 72.43%             | -45.57% |     0.4  |       75 | 39.77%     | ok               |
|          15 | 13.35%   | 72.43%             | -45.74% |     0.33 |       74 | 42.93%     | ok               |
|          30 | 12.63%   | 72.43%             | -43.35% |     0.32 |       68 | 34.28%     | ok               |
|          25 | 9.62%    | 72.43%             | -44.86% |     0.28 |       69 | 37.27%     | ok               |

## VEA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 5.67%    | 42.04%             | -16.28% |     0.26 |       60 | 50.42%     | ok               |
|          20 | 1.41%    | 42.04%             | -17.70% |     0.11 |       61 | 47.75%     | ok               |
|          25 | -0.60%   | 42.04%             | -17.79% |     0.03 |       57 | 46.09%     | ok               |
|          30 | -0.76%   | 42.04%             | -17.93% |     0.02 |       58 | 43.93%     | ok               |
|          35 | -1.87%   | 42.04%             | -16.79% |    -0.03 |       56 | 42.93%     | ok               |

## VIXY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -48.04%  | -61.26%            | -69.78% |    -0.43 |       46 | 10.48%     | ok               |
|          45 | -59.37%  | -61.26%            | -75.03% |    -0.61 |       60 | 16.64%     | ok               |
|          40 | -67.66%  | -61.26%            | -80.72% |    -0.74 |       76 | 21.46%     | ok               |
|          35 | -70.62%  | -61.26%            | -84.37% |    -0.76 |       90 | 26.79%     | ok               |
|          15 | -77.54%  | -61.26%            | -89.47% |    -0.79 |       99 | 44.26%     | ok               |

## VNQ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -7.66%   | 18.60%             | -19.07% |    -0.32 |       56 | 28.12%     | ok               |
|          50 | -8.10%   | 18.60%             | -17.13% |    -0.36 |       52 | 25.62%     | ok               |
|          25 | -12.08%  | 18.60%             | -22.34% |    -0.46 |       65 | 40.10%     | ok               |
|          20 | -13.69%  | 18.60%             | -23.79% |    -0.52 |       68 | 42.76%     | ok               |
|          15 | -15.00%  | 18.60%             | -24.90% |    -0.57 |       65 | 43.93%     | ok               |

## VTI Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 16.77%   | 45.78%             | -13.96% |     0.58 |       64 | 54.08%     | ok               |
|          15 | 10.79%   | 45.78%             | -15.70% |     0.4  |       67 | 56.57%     | ok               |
|          25 | 3.28%    | 45.78%             | -16.10% |     0.17 |       60 | 52.08%     | ok               |
|          30 | -4.47%   | 45.78%             | -18.77% |    -0.1  |       70 | 50.08%     | ok               |
|          35 | -6.87%   | 45.78%             | -20.89% |    -0.2  |       64 | 46.92%     | ok               |

## VWO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -10.12%  | 39.79%             | -24.01% |    -0.3  |       71 | 48.92%     | ok               |
|          50 | -8.49%   | 39.79%             | -21.68% |    -0.3  |       60 | 31.78%     | ok               |
|          40 | -9.57%   | 39.79%             | -23.57% |    -0.34 |       70 | 37.27%     | ok               |
|          20 | -11.14%  | 39.79%             | -26.14% |    -0.35 |       69 | 46.76%     | ok               |
|          45 | -10.27%  | 39.79%             | -23.75% |    -0.38 |       62 | 34.28%     | ok               |

## VZ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -6.80%   | 9.60%              | -12.71% |    -0.19 |       50 | 24.29%     | ok               |
|          45 | -17.93%  | 9.60%              | -20.96% |    -0.59 |       64 | 27.95%     | ok               |
|          35 | -19.10%  | 9.60%              | -22.26% |    -0.61 |       59 | 33.78%     | ok               |
|          25 | -21.86%  | 9.60%              | -22.13% |    -0.63 |       77 | 41.76%     | ok               |
|          40 | -23.63%  | 9.60%              | -23.75% |    -0.81 |       64 | 31.11%     | ok               |

## WFC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -2.88%   | 59.49%             | -18.29% |    -0.02 |       62 | 35.61%     | ok               |
|          35 | -6.40%   | 59.49%             | -23.64% |    -0.06 |       81 | 47.59%     | ok               |
|          20 | -12.65%  | 59.49%             | -29.43% |    -0.14 |       79 | 57.07%     | ok               |
|          45 | -9.69%   | 59.49%             | -23.40% |    -0.21 |       68 | 40.27%     | ok               |
|          40 | -10.99%  | 59.49%             | -24.26% |    -0.24 |       76 | 43.76%     | ok               |

## WIF-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 60.77%   | -77.85%            | -46.21% |     0.67 |       73 | 42.53%     | ok               |
|          20 | 55.08%   | -77.85%            | -40.67% |     0.64 |       67 | 39.85%     | ok               |
|          25 | 2.16%    | -77.85%            | -45.19% |     0.31 |       69 | 37.16%     | ok               |
|          30 | -35.24%  | -77.85%            | -51.39% |    -0.12 |       70 | 33.14%     | ok               |
|          50 | -20.06%  | -77.85%            | -37.87% |    -0.14 |       40 | 12.07%     | ok               |

## WMT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 45.80%   | 88.26%             | -9.18%  |     1.28 |       38 | 41.60%     | ok               |
|          50 | 38.69%   | 88.26%             | -12.19% |     1.17 |       34 | 39.27%     | ok               |
|          40 | 33.66%   | 88.26%             | -12.49% |     0.97 |       44 | 42.93%     | ok               |
|          35 | 32.79%   | 88.26%             | -13.08% |     0.92 |       54 | 47.59%     | ok               |
|          15 | 14.95%   | 88.26%             | -25.74% |     0.41 |       72 | 61.23%     | ok               |

## XBI Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 2.60%    | 55.06%             | -16.56% |     0.15 |       60 | 35.77%     | ok               |
|          45 | 1.81%    | 55.06%             | -16.74% |     0.13 |       52 | 32.61%     | ok               |
|          35 | -3.54%   | 55.06%             | -18.84% |    -0    |       64 | 39.27%     | ok               |
|          30 | -4.60%   | 55.06%             | -19.79% |    -0.03 |       66 | 41.10%     | ok               |
|          25 | -6.81%   | 55.06%             | -23.66% |    -0.08 |       72 | 43.43%     | ok               |

## XLB Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -1.68%   | 15.93%             | -20.68% |    -0.01 |       54 | 31.61%     | ok               |
|          50 | -1.74%   | 15.93%             | -17.59% |    -0.02 |       42 | 27.29%     | ok               |
|          35 | -4.92%   | 15.93%             | -23.62% |    -0.13 |       56 | 34.94%     | ok               |
|          45 | -4.65%   | 15.93%             | -20.79% |    -0.14 |       42 | 28.79%     | ok               |
|          25 | -8.37%   | 15.93%             | -23.87% |    -0.25 |       62 | 40.43%     | ok               |

## XLC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 11.95%   | 41.04%             | -12.33% |     0.44 |       69 | 53.91%     | ok               |
|          40 | 8.12%    | 41.04%             | -13.38% |     0.35 |       70 | 46.42%     | ok               |
|          25 | 8.73%    | 41.04%             | -12.31% |     0.34 |       68 | 55.91%     | ok               |
|          35 | 7.51%    | 41.04%             | -13.38% |     0.32 |       66 | 50.75%     | ok               |
|          20 | 1.27%    | 41.04%             | -13.78% |     0.11 |       74 | 58.74%     | ok               |

## XLE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 7.63%    | 34.34%             | -25.98% |     0.29 |       54 | 36.11%     | ok               |
|          45 | 3.21%    | 34.34%             | -29.68% |     0.16 |       60 | 38.10%     | ok               |
|          35 | 1.04%    | 34.34%             | -31.51% |     0.11 |       65 | 42.76%     | ok               |
|          25 | -5.65%   | 34.34%             | -36.05% |    -0.05 |       83 | 48.25%     | ok               |
|          40 | -5.54%   | 34.34%             | -34.51% |    -0.08 |       64 | 40.60%     | ok               |

## XLF Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -4.67%   | 39.75%             | -18.01% |    -0.1  |       68 | 53.91%     | ok               |
|          15 | -8.62%   | 39.75%             | -19.58% |    -0.23 |       76 | 56.74%     | ok               |
|          25 | -11.32%  | 39.75%             | -23.22% |    -0.36 |       77 | 50.42%     | ok               |
|          30 | -11.95%  | 39.75%             | -23.61% |    -0.39 |       76 | 47.92%     | ok               |
|          35 | -19.02%  | 39.75%             | -27.41% |    -0.76 |       66 | 43.76%     | ok               |

## XLI Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 3.54%    | 48.38%             | -10.36% |     0.18 |       74 | 51.08%     | ok               |
|          20 | -0.39%   | 48.38%             | -12.74% |     0.04 |       65 | 46.42%     | ok               |
|          50 | -1.71%   | 48.38%             | -11.03% |    -0.04 |       62 | 32.95%     | ok               |
|          30 | -2.58%   | 48.38%             | -11.79% |    -0.05 |       66 | 43.93%     | ok               |
|          45 | -3.01%   | 48.38%             | -14.01% |    -0.09 |       66 | 35.44%     | ok               |

## XLK Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 87.25%   | 71.02%             | -14.75% |     1.38 |       39 | 50.92%     | ok               |
|          20 | 71.51%   | 71.02%             | -14.75% |     1.23 |       46 | 48.92%     | ok               |
|          25 | 68.02%   | 71.02%             | -14.75% |     1.23 |       40 | 46.76%     | ok               |
|          30 | 65.83%   | 71.02%             | -14.75% |     1.22 |       40 | 45.59%     | ok               |
|          35 | 47.33%   | 71.02%             | -13.61% |     0.99 |       52 | 42.93%     | ok               |

## XLM-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 26.14%   | -46.08%            | -38.97% |     0.48 |       44 | 27.39%     | ok               |
|          45 | 22.34%   | -46.08%            | -43.99% |     0.44 |       50 | 31.03%     | ok               |
|          30 | 5.21%    | -46.08%            | -50.36% |     0.28 |       69 | 45.79%     | ok               |
|          40 | 1.75%    | -46.08%            | -43.80% |     0.23 |       49 | 35.44%     | ok               |
|          35 | -4.00%   | -46.08%            | -50.42% |     0.17 |       69 | 41.76%     | ok               |

## XLP Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 9.70%    | 13.94%             | -5.66%  |     0.61 |       52 | 32.61%     | ok               |
|          50 | 8.29%    | 13.94%             | -6.08%  |     0.54 |       54 | 30.45%     | ok               |
|          40 | 7.50%    | 13.94%             | -7.77%  |     0.47 |       68 | 36.77%     | ok               |
|          35 | 6.56%    | 13.94%             | -9.73%  |     0.41 |       64 | 39.77%     | ok               |
|          30 | 4.67%    | 13.94%             | -11.16% |     0.3  |       66 | 41.26%     | ok               |

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
|          30 | -16.05%  | 8.26%              | -19.97% |    -0.79 |       68 | 36.11%     | ok               |
|          25 | -17.28%  | 8.26%              | -21.14% |    -0.86 |       70 | 37.44%     | ok               |
|          15 | -21.04%  | 8.26%              | -24.43% |    -1.02 |       81 | 42.26%     | ok               |
|          20 | -20.97%  | 8.26%              | -24.51% |    -1.05 |       75 | 39.10%     | ok               |
|          35 | -20.43%  | 8.26%              | -23.94% |    -1.1  |       66 | 33.61%     | ok               |

## XLY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 5.85%    | 26.05%             | -12.94% |     0.25 |       70 | 41.60%     | ok               |
|          30 | 3.95%    | 26.05%             | -14.01% |     0.19 |       70 | 44.59%     | ok               |
|          50 | 1.64%    | 26.05%             | -11.49% |     0.12 |       50 | 29.45%     | ok               |
|          15 | 1.20%    | 26.05%             | -15.77% |     0.11 |       74 | 51.25%     | ok               |
|          45 | -1.43%   | 26.05%             | -13.48% |    -0    |       54 | 32.11%     | ok               |

## XOM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | 7.82%    | 42.31%             | -19.90% |     0.28 |       57 | 37.94%     | ok               |
|          30 | 6.68%    | 42.31%             | -20.29% |     0.26 |       57 | 36.94%     | ok               |
|          50 | 5.35%    | 42.31%             | -21.35% |     0.23 |       38 | 29.45%     | ok               |
|          20 | 1.69%    | 42.31%             | -25.56% |     0.12 |       64 | 40.27%     | ok               |
|          35 | -0.43%   | 42.31%             | -20.93% |     0.06 |       57 | 35.77%     | ok               |

## XRP-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | -25.11%  | -59.41%            | -46.19% |    -0.14 |       68 | 39.85%     | ok               |
|          40 | -30.47%  | -59.41%            | -44.89% |    -0.26 |       58 | 33.72%     | ok               |
|          30 | -37.23%  | -59.41%            | -54.12% |    -0.33 |       70 | 44.06%     | ok               |
|          45 | -38.24%  | -59.41%            | -46.06% |    -0.42 |       58 | 29.50%     | ok               |
|          50 | -34.88%  | -59.41%            | -38.03% |    -0.46 |       60 | 22.03%     | ok               |

## YFI-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -51.25%  | -64.52%            | -52.26% |    -0.86 |       62 | 27.39%     | ok               |
|          45 | -47.81%  | -64.52%            | -51.53% |    -0.98 |       70 | 21.46%     | ok               |
|          30 | -64.19%  | -64.52%            | -71.12% |    -1.03 |       81 | 40.61%     | ok               |
|          35 | -62.68%  | -64.52%            | -63.36% |    -1.06 |       69 | 34.87%     | ok               |
|          25 | -67.83%  | -64.52%            | -72.16% |    -1.12 |       75 | 45.59%     | ok               |

## ZEC-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 124.86%  | 1610.13%           | -24.66% |     0.9  |       44 | 24.52%     | ok               |
|          35 | 92.42%   | 1610.13%           | -44.34% |     0.77 |       52 | 30.65%     | ok               |
|          25 | 76.83%   | 1610.13%           | -48.59% |     0.7  |       58 | 39.46%     | ok               |
|          30 | 61.20%   | 1610.13%           | -47.68% |     0.64 |       62 | 36.40%     | ok               |
|          50 | 54.57%   | 1610.13%           | -34.17% |     0.6  |       46 | 22.03%     | ok               |
