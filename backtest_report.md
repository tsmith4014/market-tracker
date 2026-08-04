# Market Tracker Backtest Report

_Generated: 2026-08-04T03:49:00+00:00_

## Data Sources

- Crypto: Kraken -> Coinbase -> CoinGecko OHLC -> CoinPaprika fallback chain.
- Stocks / ETFs / indices: Stooq -> Yahoo Finance fallback chain.
- Data rows are generated from real market APIs. Mock OHLCV rows are not generated.

## Data Freshness

- Rows: **92,567**
- Symbols: **161**
- Date range: **2024-03-11** to **2026-08-04**

## Latest Signals

| symbol     | date                |         close |   composite_score | signal   | data_source   |
|:-----------|:--------------------|--------------:|------------------:|:---------|:--------------|
| ADBE       | 2026-08-03 00:00:00 |   251.34      |         31.0833   | LONG     | Yahoo Finance |
| AMGN       | 2026-08-03 00:00:00 |   378.87      |         62.5833   | LONG     | Yahoo Finance |
| AMZN       | 2026-08-03 00:00:00 |   284.02      |         78.0833   | LONG     | Yahoo Finance |
| BLK        | 2026-08-03 00:00:00 |  1126.63      |         63.9167   | LONG     | Yahoo Finance |
| COP        | 2026-08-03 00:00:00 |   119.16      |         74.9167   | LONG     | Yahoo Finance |
| CVX        | 2026-08-03 00:00:00 |   193.18      |         73.25     | LONG     | Yahoo Finance |
| DBC        | 2026-08-03 00:00:00 |    28.88      |         54.4167   | LONG     | Yahoo Finance |
| EOG        | 2026-08-03 00:00:00 |   145.68      |         74.4167   | LONG     | Yahoo Finance |
| FXI        | 2026-08-03 00:00:00 |    36.46      |         65.8333   | LONG     | Yahoo Finance |
| GE         | 2026-08-03 00:00:00 |   368.93      |         56.5833   | LONG     | Yahoo Finance |
| HON        | 2026-08-03 00:00:00 |   246.77      |         75.75     | LONG     | Yahoo Finance |
| INTU       | 2026-08-03 00:00:00 |   318.39      |         34.4167   | LONG     | Yahoo Finance |
| IWM        | 2026-08-03 00:00:00 |   296.22      |         42.0833   | LONG     | Yahoo Finance |
| MPC        | 2026-08-03 00:00:00 |   307.03      |         51.5833   | LONG     | Yahoo Finance |
| MSFT       | 2026-08-03 00:00:00 |   487.65      |         63.75     | LONG     | Yahoo Finance |
| OXY        | 2026-08-03 00:00:00 |    55.47      |         73.1667   | LONG     | Yahoo Finance |
| PM         | 2026-08-03 00:00:00 |   187.41      |         44.0833   | LONG     | Yahoo Finance |
| RTX        | 2026-08-03 00:00:00 |   216.65      |         60        | LONG     | Yahoo Finance |
| SCHW       | 2026-08-03 00:00:00 |   105.87      |         51.0833   | LONG     | Yahoo Finance |
| SHIB-USD   | 2026-08-04 00:00:00 |     5.003e-06 |         48.6667   | LONG     | Kraken API    |
| T          | 2026-08-03 00:00:00 |    23.59      |         37.3333   | LONG     | Yahoo Finance |
| TGT        | 2026-08-03 00:00:00 |   149.35      |         75.75     | LONG     | Yahoo Finance |
| TMO        | 2026-08-03 00:00:00 |   574.03      |         60.0833   | LONG     | Yahoo Finance |
| TRX-USD    | 2026-08-04 00:00:00 |     0.328708  |         70.75     | LONG     | Kraken API    |
| VNQ        | 2026-08-03 00:00:00 |    99.07      |         52.0833   | LONG     | Yahoo Finance |
| VZ         | 2026-08-03 00:00:00 |    47.36      |         69.5833   | LONG     | Yahoo Finance |
| XLE        | 2026-08-03 00:00:00 |    58.79      |         69.9167   | LONG     | Yahoo Finance |
| XLF        | 2026-08-03 00:00:00 |    57.38      |         42.25     | LONG     | Yahoo Finance |
| XLI        | 2026-08-03 00:00:00 |   183.16      |         48.75     | LONG     | Yahoo Finance |
| XOM        | 2026-08-03 00:00:00 |   155.06      |         73.5833   | LONG     | Yahoo Finance |
| AAPL       | 2026-08-03 00:00:00 |   303.42      |          2.16667  | NEUTRAL  | Yahoo Finance |
| AAVE-USD   | 2026-08-04 00:00:00 |    92.05      |        -16.4167   | NEUTRAL  | Kraken API    |
| ABBV       | 2026-08-03 00:00:00 |   245.1       |         13.75     | NEUTRAL  | Yahoo Finance |
| ADA-USD    | 2026-08-04 00:00:00 |     0.194029  |         43.0833   | NEUTRAL  | Kraken API    |
| ALGO-USD   | 2026-08-04 00:00:00 |     0.08941   |         36.4167   | NEUTRAL  | Kraken API    |
| AMAT       | 2026-08-03 00:00:00 |   518.21      |        -25.0833   | NEUTRAL  | Yahoo Finance |
| AMD        | 2026-08-03 00:00:00 |   484.64      |        -34.8333   | NEUTRAL  | Yahoo Finance |
| ARB-USD    | 2026-08-04 00:00:00 |     0.0833    |        -15.3333   | NEUTRAL  | Kraken API    |
| ATOM-USD   | 2026-08-04 00:00:00 |     1.3702    |        -26        | NEUTRAL  | Kraken API    |
| AVAX-USD   | 2026-08-04 00:00:00 |     6.873     |         38.6667   | NEUTRAL  | Kraken API    |
| AVGO       | 2026-08-03 00:00:00 |   392.23      |         20.4167   | NEUTRAL  | Yahoo Finance |
| BA         | 2026-08-03 00:00:00 |   233.49      |         48.8333   | NEUTRAL  | Yahoo Finance |
| BAC        | 2026-08-03 00:00:00 |    62.48      |         27.3333   | NEUTRAL  | Yahoo Finance |
| BCH-USD    | 2026-08-04 00:00:00 |   212.7       |        -25.6667   | NEUTRAL  | Kraken API    |
| BITO       | 2026-08-03 00:00:00 |     8.63      |        -32.9167   | NEUTRAL  | Yahoo Finance |
| BONK-USD   | 2026-08-04 00:00:00 |     2.888e-06 |        -30.25     | NEUTRAL  | Kraken API    |
| BTC-USD    | 2026-08-04 00:00:00 | 63691.4       |        -46.25     | NEUTRAL  | Kraken API    |
| C          | 2026-08-03 00:00:00 |   133.57      |         16.0833   | NEUTRAL  | Yahoo Finance |
| CAT        | 2026-08-03 00:00:00 |   830.03      |         -9.83333  | NEUTRAL  | Yahoo Finance |
| CL         | 2026-08-03 00:00:00 |    89.88      |         -9.41667  | NEUTRAL  | Yahoo Finance |
| CMCSA      | 2026-08-03 00:00:00 |    24.56      |         45.3333   | NEUTRAL  | Yahoo Finance |
| COST       | 2026-08-03 00:00:00 |   954.08      |         28.9167   | NEUTRAL  | Yahoo Finance |
| CRM        | 2026-08-03 00:00:00 |   185.95      |         21.8333   | NEUTRAL  | Yahoo Finance |
| CRV-USD    | 2026-08-04 00:00:00 |     0.20615   |        -42.5      | NEUTRAL  | Kraken API    |
| CSCO       | 2026-08-03 00:00:00 |   115.86      |         40.3333   | NEUTRAL  | Yahoo Finance |
| DE         | 2026-08-03 00:00:00 |   605.06      |         52.8333   | NEUTRAL  | Yahoo Finance |
| DIA        | 2026-08-03 00:00:00 |   531.22      |         53.3333   | NEUTRAL  | Yahoo Finance |
| DIS        | 2026-08-03 00:00:00 |    98.14      |         -6.33333  | NEUTRAL  | Yahoo Finance |
| DOGE-USD   | 2026-08-04 00:00:00 |     0.0703444 |        -11        | NEUTRAL  | Kraken API    |
| DOT-USD    | 2026-08-04 00:00:00 |     0.8424    |         12.6667   | NEUTRAL  | Kraken API    |
| DXY-INDEX  | 2026-08-03 00:00:00 |    99.977     |        -11.0215   | NEUTRAL  | Yahoo Finance |
| EEM        | 2026-08-03 00:00:00 |    64.32      |          4.91667  | NEUTRAL  | Yahoo Finance |
| EFA        | 2026-08-03 00:00:00 |   106.02      |         48.8333   | NEUTRAL  | Yahoo Finance |
| ETC-USD    | 2026-08-04 00:00:00 |     6.584     |        -44.5833   | NEUTRAL  | Kraken API    |
| ETH-USD    | 2026-08-04 00:00:00 |  1858.6       |        -21.9167   | NEUTRAL  | Kraken API    |
| EWJ        | 2026-08-03 00:00:00 |    92.91      |         12        | NEUTRAL  | Yahoo Finance |
| FCX        | 2026-08-03 00:00:00 |    63.64      |         45.25     | NEUTRAL  | Yahoo Finance |
| FET-USD    | 2026-08-04 00:00:00 |     0.1445    |        -29        | NEUTRAL  | Kraken API    |
| FIL-USD    | 2026-08-04 00:00:00 |     0.721     |        -20        | NEUTRAL  | Kraken API    |
| GDX        | 2026-08-03 00:00:00 |    76.05      |         -4.83333  | NEUTRAL  | Yahoo Finance |
| GDXJ       | 2026-08-03 00:00:00 |    98.67      |         -4.83333  | NEUTRAL  | Yahoo Finance |
| GLD        | 2026-08-03 00:00:00 |   371.71      |        -31.1667   | NEUTRAL  | Yahoo Finance |
| GOOGL      | 2026-08-03 00:00:00 |   373.51      |         24.6667   | NEUTRAL  | Yahoo Finance |
| GS         | 2026-08-03 00:00:00 |  1027.06      |        -26.5      | NEUTRAL  | Yahoo Finance |
| HBAR-USD   | 2026-08-04 00:00:00 |     0.07101   |         28        | NEUTRAL  | Kraken API    |
| HD         | 2026-08-03 00:00:00 |   340.02      |          5.41667  | NEUTRAL  | Yahoo Finance |
| IBIT       | 2026-08-03 00:00:00 |    36.16      |        -48.6667   | NEUTRAL  | Yahoo Finance |
| ICP-USD    | 2026-08-04 00:00:00 |     2.114     |        -20        | NEUTRAL  | Kraken API    |
| IEMG       | 2026-08-03 00:00:00 |    78.11      |          5.16667  | NEUTRAL  | Yahoo Finance |
| INJ-USD    | 2026-08-04 00:00:00 |     5.015     |          0.666667 | NEUTRAL  | Kraken API    |
| INTC       | 2026-08-03 00:00:00 |    91         |        -16.5      | NEUTRAL  | Yahoo Finance |
| ITA        | 2026-08-03 00:00:00 |   246.08      |         45.3333   | NEUTRAL  | Yahoo Finance |
| JNJ        | 2026-08-03 00:00:00 |   254.41      |         -4.5      | NEUTRAL  | Yahoo Finance |
| JPM        | 2026-08-03 00:00:00 |   352.64      |         35.4167   | NEUTRAL  | Yahoo Finance |
| KO         | 2026-08-03 00:00:00 |    86.86      |         59.8333   | NEUTRAL  | Yahoo Finance |
| LINK-USD   | 2026-08-04 00:00:00 |     8.16981   |        -41.5833   | NEUTRAL  | Kraken API    |
| LLY        | 2026-08-03 00:00:00 |  1121.36      |        -38.6667   | NEUTRAL  | Yahoo Finance |
| LRCX       | 2026-08-03 00:00:00 |   294.61      |        -19.8333   | NEUTRAL  | Yahoo Finance |
| MCD        | 2026-08-03 00:00:00 |   265.23      |        -42.5      | NEUTRAL  | Yahoo Finance |
| MRK        | 2026-08-03 00:00:00 |   127.77      |         51.5      | NEUTRAL  | Yahoo Finance |
| MS         | 2026-08-03 00:00:00 |   211.23      |         -8.5      | NEUTRAL  | Yahoo Finance |
| MU         | 2026-08-03 00:00:00 |   829.5       |        -19.8333   | NEUTRAL  | Yahoo Finance |
| NEAR-USD   | 2026-08-04 00:00:00 |     1.7531    |        -27.25     | NEUTRAL  | Kraken API    |
| NEM        | 2026-08-03 00:00:00 |    95.37      |        -13.8333   | NEUTRAL  | Yahoo Finance |
| NFLX       | 2026-08-03 00:00:00 |    73.33      |        -14.25     | NEUTRAL  | Yahoo Finance |
| NKE        | 2026-08-03 00:00:00 |    42.64      |        -52.8333   | NEUTRAL  | Yahoo Finance |
| NOW        | 2026-08-03 00:00:00 |   114.19      |         15.0833   | NEUTRAL  | Yahoo Finance |
| NVDA       | 2026-08-03 00:00:00 |   206.64      |          0.916667 | NEUTRAL  | Yahoo Finance |
| ORCL       | 2026-08-03 00:00:00 |   141.85      |          0.916667 | NEUTRAL  | Yahoo Finance |
| PEP        | 2026-08-03 00:00:00 |   139.63      |          2.16667  | NEUTRAL  | Yahoo Finance |
| PEPE-USD   | 2026-08-04 00:00:00 |     2.945e-06 |         29.0833   | NEUTRAL  | Kraken API    |
| PFE        | 2026-08-03 00:00:00 |    25.03      |         18.4167   | NEUTRAL  | Yahoo Finance |
| PG         | 2026-08-03 00:00:00 |   144.97      |        -32        | NEUTRAL  | Yahoo Finance |
| QQQ        | 2026-08-03 00:00:00 |   700.07      |         26.4167   | NEUTRAL  | Yahoo Finance |
| SBUX       | 2026-08-03 00:00:00 |   103.37      |         12.1667   | NEUTRAL  | Yahoo Finance |
| SHY        | 2026-08-03 00:00:00 |    81.77      |        -36.4167   | NEUTRAL  | Yahoo Finance |
| SLB        | 2026-08-03 00:00:00 |    49.31      |         46.9167   | NEUTRAL  | Yahoo Finance |
| SLV        | 2026-08-03 00:00:00 |    52.46      |        -44.1667   | NEUTRAL  | Yahoo Finance |
| SMH        | 2026-08-03 00:00:00 |   545.46      |        -15.5833   | NEUTRAL  | Yahoo Finance |
| SNX-USD    | 2026-08-04 00:00:00 |     0.2153    |        -16.5      | NEUTRAL  | Kraken API    |
| SOXX       | 2026-08-03 00:00:00 |   507.68      |        -17.5833   | NEUTRAL  | Yahoo Finance |
| SPY        | 2026-08-03 00:00:00 |   757.67      |         45.8333   | NEUTRAL  | Yahoo Finance |
| TIA-USD    | 2026-08-04 00:00:00 |     0.3372    |        -29        | NEUTRAL  | Kraken API    |
| TMUS       | 2026-08-03 00:00:00 |   177.09      |        -44        | NEUTRAL  | Yahoo Finance |
| TXN        | 2026-08-03 00:00:00 |   269.04      |        -21.0833   | NEUTRAL  | Yahoo Finance |
| UNH        | 2026-08-03 00:00:00 |   415.36      |         13.1667   | NEUTRAL  | Yahoo Finance |
| UNI-USD    | 2026-08-04 00:00:00 |     3.8673    |         24.8333   | NEUTRAL  | Kraken API    |
| UPS        | 2026-08-03 00:00:00 |   106.87      |        -11        | NEUTRAL  | Yahoo Finance |
| USO        | 2026-08-03 00:00:00 |   122.12      |         24.9167   | NEUTRAL  | Yahoo Finance |
| VEA        | 2026-08-03 00:00:00 |    71.04      |         52.6667   | NEUTRAL  | Yahoo Finance |
| VIXY       | 2026-08-03 00:00:00 |    20.35      |        -13.6667   | NEUTRAL  | Yahoo Finance |
| VTI        | 2026-08-03 00:00:00 |   373.84      |         45.8333   | NEUTRAL  | Yahoo Finance |
| VWO        | 2026-08-03 00:00:00 |    59.06      |         19        | NEUTRAL  | Yahoo Finance |
| WFC        | 2026-08-03 00:00:00 |    87.89      |         34.3333   | NEUTRAL  | Yahoo Finance |
| WIF-USD    | 2026-08-04 00:00:00 |     0.1408    |        -52.25     | NEUTRAL  | Kraken API    |
| WMT        | 2026-08-03 00:00:00 |   110.71      |        -29.6667   | NEUTRAL  | Yahoo Finance |
| XBI        | 2026-08-03 00:00:00 |   147.31      |         11.4167   | NEUTRAL  | Yahoo Finance |
| XLB        | 2026-08-03 00:00:00 |    51.01      |         22.1667   | NEUTRAL  | Yahoo Finance |
| XLC        | 2026-08-03 00:00:00 |   111.34      |         -5.25     | NEUTRAL  | Yahoo Finance |
| XLK        | 2026-08-03 00:00:00 |   178.04      |         25.9167   | NEUTRAL  | Yahoo Finance |
| XLM-USD    | 2026-08-04 00:00:00 |     0.170391  |        -60.5833   | NEUTRAL  | Kraken API    |
| XLP        | 2026-08-03 00:00:00 |    84.86      |         48.6667   | NEUTRAL  | Yahoo Finance |
| XLU        | 2026-08-03 00:00:00 |    44.36      |        -56.75     | NEUTRAL  | Yahoo Finance |
| XLV        | 2026-08-03 00:00:00 |   162.24      |         26.6667   | NEUTRAL  | Yahoo Finance |
| XLY        | 2026-08-03 00:00:00 |   118.21      |         26.6667   | NEUTRAL  | Yahoo Finance |
| XRP-USD    | 2026-08-04 00:00:00 |     1.07454   |        -46.25     | NEUTRAL  | Kraken API    |
| YFI-USD    | 2026-08-04 00:00:00 |  2125.7       |         30        | NEUTRAL  | Kraken API    |
| ZEC-USD    | 2026-08-04 00:00:00 |   483.69      |         -4.58333  | NEUTRAL  | Kraken API    |
| AGG        | 2026-08-03 00:00:00 |    97.26      |        -47.5833   | SHORT    | Yahoo Finance |
| APT-USD    | 2026-08-04 00:00:00 |     0.5778    |        -33.3333   | SHORT    | Kraken API    |
| ARKK       | 2026-08-03 00:00:00 |    73.54      |        -49.8333   | SHORT    | Yahoo Finance |
| BND        | 2026-08-03 00:00:00 |    72.15      |        -47.5833   | SHORT    | Yahoo Finance |
| COMP-USD   | 2026-08-04 00:00:00 |    16.5       |        -30.8333   | SHORT    | Kraken API    |
| DASH-USD   | 2026-08-04 00:00:00 |    31.175     |        -53        | SHORT    | Kraken API    |
| GRT-USD    | 2026-08-04 00:00:00 |     0.01478   |        -36.6667   | SHORT    | Kraken API    |
| HYG        | 2026-08-03 00:00:00 |    79.31      |        -49.8333   | SHORT    | Yahoo Finance |
| IBM        | 2026-08-03 00:00:00 |   226.31      |        -32.8333   | SHORT    | Yahoo Finance |
| IEF        | 2026-08-03 00:00:00 |    92.82      |        -47.5833   | SHORT    | Yahoo Finance |
| LDO-USD    | 2026-08-04 00:00:00 |     0.328     |        -31.9167   | SHORT    | Kraken API    |
| LIN        | 2026-08-03 00:00:00 |   480.46      |        -41.8333   | SHORT    | Yahoo Finance |
| LTC-USD    | 2026-08-04 00:00:00 |    44.22      |        -37        | SHORT    | Kraken API    |
| META       | 2026-08-03 00:00:00 |   590.24      |        -45.3333   | SHORT    | Yahoo Finance |
| OP-USD     | 2026-08-04 00:00:00 |     0.0889    |        -42.3333   | SHORT    | Kraken API    |
| POL-USD    | 2026-08-04 00:00:00 |     0.07305   |        -38.6667   | SHORT    | Kraken API    |
| QCOM       | 2026-08-03 00:00:00 |   151.57      |        -45.9167   | SHORT    | Yahoo Finance |
| RENDER-USD | 2026-08-04 00:00:00 |     1.357     |        -40.3333   | SHORT    | Kraken API    |
| SKY-USD    | 2026-08-04 00:00:00 |     0.05604   |        -52.8333   | SHORT    | Kraken API    |
| SOL-USD    | 2026-08-04 00:00:00 |    73.44      |        -46.25     | SHORT    | Kraken API    |
| SUSHI-USD  | 2026-08-04 00:00:00 |     0.1553    |        -35        | SHORT    | Kraken API    |
| TLT        | 2026-08-03 00:00:00 |    82.19      |        -44.25     | SHORT    | Yahoo Finance |
| TSLA       | 2026-08-03 00:00:00 |   322.08      |        -60.9167   | SHORT    | Yahoo Finance |

## Edge Summary

- Symbols with trades: **160** of 160
- Beat buy-and-hold: **30.63%** of traded symbols
- Positive return: **28.75%** of traded symbols
- Median strategy return: **-10.12%** (benchmark **18.03%**)
- Median excess vs benchmark: **-27.11%**
- Median Sharpe: **-0.14**
- Median exposure: **43.93%**

> Edge is real only if both _beat buy-and-hold_ and _median excess_ are convincingly positive across many symbols. Treat a single high-return symbol as noise.

## Portfolio Backtest

Actual capital-allocation books (not per-symbol averages). Benchmarks: `equal_weight_buyhold` (whole tracked universe), `spy_buyhold` (100% SPY), and `sixty_forty` (60% SPY / 40% AGG). `high_conf_voltarget` inverse-vol-weights the HIGH-confidence book; `conviction_long_short` is market-neutral. Judge on **Sharpe** and **max_drawdown** out-of-sample, not raw return: a fully-invested long book wins on return in a bull market but carries all the risk.

| strategy              | scope         | ann_return   | ann_vol   |   sharpe | max_drawdown   | total_return   |   avg_gross_exposure |
|:----------------------|:--------------|:-------------|:----------|---------:|:---------------|:---------------|---------------------:|
| equal_weight_buyhold  | full          | 0.20%        | 31.84%    |     0.01 | -43.58%        | -13.85%        |                 1    |
| equal_weight_buyhold  | out_of_sample | -19.60%      | 29.10%    |    -0.67 | -35.70%        | -22.47%        |                 1    |
| all_signals_ew        | full          | -21.27%      | 26.62%    |    -0.8  | -63.93%        | -53.10%        |                 1    |
| all_signals_ew        | out_of_sample | 13.82%       | 24.07%    |     0.57 | -20.51%        | 12.38%         |                 1    |
| high_conf_ew          | full          | -2.61%       | 31.54%    |    -0.08 | -43.74%        | -20.49%        |                 0.88 |
| high_conf_ew          | out_of_sample | 4.40%        | 27.25%    |     0.16 | -20.42%        | 0.65%          |                 0.88 |
| high_conf_voltarget   | full          | 0.50%        | 29.09%    |     0.02 | -35.34%        | -10.53%        |                 0.88 |
| high_conf_voltarget   | out_of_sample | -1.78%       | 24.08%    |    -0.07 | -16.94%        | -4.96%         |                 0.88 |
| conviction_long_short | full          | -19.45%      | 22.95%    |    -0.85 | -51.44%        | -49.01%        |                 0.97 |
| conviction_long_short | out_of_sample | -10.04%      | 22.86%    |    -0.44 | -23.76%        | -12.65%        |                 0.97 |
| spy_buyhold           | full          | 5.81%        | 13.38%    |     0.43 | -18.13%        | 16.16%         |                 0.78 |
| spy_buyhold           | out_of_sample | -0.77%       | 9.96%     |    -0.08 | -12.06%        | -1.34%         |                 0.78 |
| sixty_forty           | full          | 3.21%        | 8.46%     |     0.38 | -10.90%        | 9.09%          |                 0.78 |
| sixty_forty           | out_of_sample | -1.92%       | 6.59%     |    -0.29 | -8.26%         | -2.26%         |                 0.78 |

## Walk-Forward Robustness

Each book measured across contiguous time folds (each a different regime). A book has durable edge only if `mean_sharpe` is positive, `min_sharpe` isn't deeply negative, and `pct_positive_folds` is high — a single great fold doesn't count. `fold_sharpes` lists each fold oldest-to-newest.

| strategy              |   n_folds |   mean_sharpe |   median_sharpe |   min_sharpe | pct_positive_folds   | mean_return   | fold_sharpes                 |
|:----------------------|----------:|--------------:|----------------:|-------------:|:---------------------|:--------------|:-----------------------------|
| equal_weight_buyhold  |         5 |          0.31 |            0.88 |        -1.12 | 60.00%               | -1.24%        | 1.53;-0.62;0.88;-1.12;0.88   |
| all_signals_ew        |         5 |         -0.93 |           -0.96 |        -2.29 | 20.00%               | -12.66%       | -0.42;-0.96;-2.29;0.67;-1.64 |
| high_conf_ew          |         5 |          0.08 |            0.09 |        -1.02 | 60.00%               | -3.93%        | 0.98;-1.02;0.09;-0.15;0.52   |
| high_conf_voltarget   |         5 |          0.32 |            0.02 |        -0.6  | 60.00%               | -1.78%        | 1.67;-0.60;0.02;-0.26;0.74   |
| conviction_long_short |         5 |         -0.95 |           -1.27 |        -2.08 | 20.00%               | -12.05%       | -1.48;-2.08;0.49;-0.40;-1.27 |
| spy_buyhold           |         5 |          0.55 |            0.08 |        -0.93 | 60.00%               | 3.26%         | 1.73;0.08;1.92;-0.93;-0.04   |
| sixty_forty           |         5 |          0.48 |            0.06 |        -0.85 | 60.00%               | 1.85%         | 1.71;0.06;1.92;-0.85;-0.45   |

## Strategy Comparison

Each decision rule backtested over the same data. `out_of_sample` is the most recent ~35% of each symbol's history (unseen tail). A rule has real edge only if `median_excess` and `beat_benchmark_pct` stay positive out-of-sample, not just full-sample.

| strategy        | scope         |   symbols | beat_benchmark_pct   | positive_pct   | median_return   | median_benchmark   | median_excess   |   median_sharpe |   total_trades |
|:----------------|:--------------|----------:|:---------------------|:---------------|:----------------|:-------------------|:----------------|----------------:|---------------:|
| trend           | full          |       160 | 30.63%               | 28.75%         | -10.12%         | 18.03%             | -27.11%         |           -0.14 |          11287 |
| trend           | out_of_sample |       160 | 35.62%               | 43.75%         | -2.22%          | 3.46%              | -8.26%          |           -0.08 |           3815 |
| mean_reversion  | full          |       157 | 42.68%               | 51.59%         | 0.09%           | 13.47%             | -14.35%         |            0.04 |           1284 |
| mean_reversion  | out_of_sample |       127 | 48.82%               | 59.84%         | 0.39%           | -1.23%             | -0.83%          |            0.63 |            454 |
| regime_adaptive | full          |       160 | 31.87%               | 30.00%         | -10.23%         | 18.03%             | -27.90%         |           -0.14 |          11570 |
| regime_adaptive | out_of_sample |       160 | 36.88%               | 44.38%         | -1.99%          | 3.46%              | -7.33%          |           -0.04 |           3928 |

## Signal Calibration

Realized forward return in the signal's direction, grouped by confidence. HIGH should outrank LOW for the confidence score to be meaningful.

| confidence_level   |   horizon |     n | mean_return   | median_return   | win_rate   |
|:-------------------|----------:|------:|:--------------|:----------------|:-----------|
| HIGH               |         5 |  7770 | 0.09%         | 0.08%           | 51.35%     |
| MEDIUM             |         5 | 29119 | 0.02%         | 0.06%           | 50.63%     |
| LOW                |         5 |  3442 | -0.63%        | -0.55%          | 44.63%     |
| ALL                |         5 | 40331 | -0.02%        | 0.02%           | 50.25%     |
| HIGH               |        10 |  7731 | 0.32%         | 0.08%           | 50.90%     |
| MEDIUM             |        10 | 28912 | 0.12%         | 0.08%           | 50.59%     |
| LOW                |        10 |  3422 | -0.92%        | -0.77%          | 45.03%     |
| ALL                |        10 | 40065 | 0.07%         | 0.02%           | 50.18%     |
| HIGH               |        20 |  7669 | 0.61%         | 0.25%           | 52.01%     |
| MEDIUM             |        20 | 28489 | 0.71%         | 0.52%           | 52.90%     |
| LOW                |        20 |  3344 | -0.76%        | -0.62%          | 46.86%     |
| ALL                |        20 | 39502 | 0.57%         | 0.37%           | 52.22%     |

## Backtest Summary

### Data Quality / Signal Availability

- **ok**: 160 symbols

| symbol     |   trades | return   | benchmark_return   | mdd     |   sharpe | exposure   | skipped_reason   |
|:-----------|---------:|:---------|:-------------------|:--------|---------:|:-----------|:-----------------|
| AAPL       |       61 | 6.01%    | 75.64%             | -20.65% |     0.22 | 49.08%     | ok               |
| AAVE-USD   |       76 | -51.81%  | -52.80%            | -68.26% |    -0.49 | 38.51%     | ok               |
| ABBV       |       70 | -23.13%  | 36.45%             | -30.55% |    -0.5  | 46.76%     | ok               |
| ADA-USD    |       86 | -82.08%  | -70.55%            | -58.47% |    -0.64 | 45.98%     | ok               |
| ADBE       |       68 | -30.61%  | -55.15%            | -32.35% |    -0.37 | 57.07%     | ok               |
| AGG        |       69 | -6.12%   | -0.92%             | -10.17% |    -1    | 33.28%     | ok               |
| ALGO-USD   |       82 | -41.24%  | -64.72%            | -44.44% |    -0.39 | 36.78%     | ok               |
| AMAT       |       71 | -35.85%  | 157.34%            | -57.08% |    -0.34 | 50.25%     | ok               |
| AMD        |       54 | 7.26%    | 144.29%            | -44.27% |     0.28 | 35.27%     | ok               |
| AMGN       |       75 | -14.44%  | 37.59%             | -34.19% |    -0.25 | 47.59%     | ok               |
| AMZN       |       82 | -51.44%  | 65.17%             | -54.51% |    -1.42 | 39.27%     | ok               |
| APT-USD    |       72 | -27.92%  | -90.84%            | -66.73% |    -0.05 | 41.76%     | ok               |
| ARB-USD    |       76 | -33.32%  | -80.07%            | -62.55% |    -0.17 | 41.38%     | ok               |
| ARKK       |       89 | -34.24%  | 45.19%             | -37.98% |    -0.59 | 40.93%     | ok               |
| ATOM-USD   |       88 | -67.48%  | -69.48%            | -73.98% |    -1.1  | 46.74%     | ok               |
| AVAX-USD   |       79 | -59.54%  | -68.56%            | -61.58% |    -0.79 | 38.70%     | ok               |
| AVGO       |       62 | 24.24%   | 203.32%            | -35.76% |     0.43 | 40.93%     | ok               |
| BA         |       67 | 3.44%    | 21.30%             | -30.56% |     0.18 | 48.42%     | ok               |
| BAC        |       78 | -6.12%   | 74.09%             | -27.64% |    -0.08 | 51.08%     | ok               |
| BCH-USD    |       78 | -1.91%   | -31.63%            | -54.26% |     0.19 | 50.77%     | ok               |
| BITO       |       80 | -26.85%  | -73.98%            | -42.82% |    -0.22 | 39.43%     | ok               |
| BLK        |       81 | -7.13%   | 36.53%             | -26.90% |    -0.13 | 44.09%     | ok               |
| BND        |       67 | -7.08%   | -0.93%             | -10.16% |    -1.12 | 34.94%     | ok               |
| BONK-USD   |       70 | 50.64%   | -78.68%            | -51.50% |     0.62 | 42.91%     | ok               |
| BTC-USD    |       72 | 8.49%    | -25.96%            | -23.38% |     0.28 | 51.72%     | ok               |
| C          |       79 | -30.72%  | 132.66%            | -38.11% |    -0.61 | 50.58%     | ok               |
| CAT        |       72 | 17.78%   | 147.79%            | -21.02% |     0.39 | 53.91%     | ok               |
| CL         |       62 | 5.31%    | 1.99%              | -14.32% |     0.23 | 43.93%     | ok               |
| CMCSA      |       80 | -45.38%  | -39.81%            | -48.04% |    -1.23 | 42.10%     | ok               |
| COMP-USD   |       93 | -43.71%  | -67.07%            | -57.10% |    -0.32 | 46.36%     | ok               |
| COP        |       72 | -19.02%  | 3.39%              | -43.77% |    -0.3  | 43.93%     | ok               |
| COST       |       60 | 0.55%    | 33.61%             | -29.73% |     0.08 | 41.76%     | ok               |
| CRM        |       63 | -39.56%  | -39.23%            | -41.36% |    -0.83 | 42.76%     | ok               |
| CRV-USD    |       70 | -0.17%   | -52.61%            | -39.89% |     0.23 | 36.59%     | ok               |
| CSCO       |       59 | 23.34%   | 130.70%            | -21.79% |     0.51 | 47.75%     | ok               |
| CVX        |       71 | -9.65%   | 27.09%             | -29.13% |    -0.2  | 40.60%     | ok               |
| DASH-USD   |       63 | -41.94%  | 22.51%             | -64.43% |    -0.02 | 29.69%     | ok               |
| DBC        |       62 | -12.08%  | 29.16%             | -25.70% |    -0.38 | 35.44%     | ok               |
| DE         |       70 | -5.05%   | 61.33%             | -24.56% |    -0.01 | 45.42%     | ok               |
| DIA        |       58 | -4.54%   | 36.76%             | -12.94% |    -0.21 | 43.26%     | ok               |
| DIS        |       66 | -19.22%  | -12.62%            | -28.17% |    -0.36 | 43.93%     | ok               |
| DOGE-USD   |       72 | -26.18%  | -65.95%            | -62.31% |    -0.03 | 48.85%     | ok               |
| DOT-USD    |       88 | -63.03%  | -81.93%            | -67.64% |    -0.74 | 48.08%     | ok               |
| DXY-INDEX  |       42 | -1.69%   | -1.67%             | -6.29%  |    -0.25 | 32.75%     | ok               |
| EEM        |       64 | -11.10%  | 57.22%             | -25.67% |    -0.31 | 41.10%     | ok               |
| EFA        |       58 | -10.05%  | 34.54%             | -13.53% |    -0.38 | 41.76%     | ok               |
| EOG        |       81 | -18.91%  | 20.58%             | -48.13% |    -0.35 | 49.08%     | ok               |
| ETC-USD    |       62 | -31.66%  | -65.34%            | -48.09% |    -0.43 | 28.93%     | ok               |
| ETH-USD    |       62 | 139.05%  | -16.11%            | -30.11% |     1.19 | 45.98%     | ok               |
| EWJ        |       62 | -20.29%  | 33.49%             | -30.73% |    -0.69 | 36.94%     | ok               |
| FCX        |       67 | -29.92%  | 57.45%             | -48.22% |    -0.35 | 45.92%     | ok               |
| FET-USD    |       87 | -50.78%  | -77.41%            | -52.44% |    -0.33 | 41.57%     | ok               |
| FIL-USD    |       70 | -50.04%  | -77.79%            | -48.59% |    -0.65 | 34.29%     | ok               |
| FXI        |       44 | -0.79%   | 51.66%             | -23.91% |     0.07 | 30.62%     | ok               |
| GDX        |       58 | 6.76%    | 152.41%            | -34.99% |     0.24 | 46.92%     | ok               |
| GDXJ       |       64 | -25.09%  | 169.59%            | -44.93% |    -0.26 | 45.09%     | ok               |
| GE         |       80 | -0.77%   | 177.54%            | -27.82% |     0.11 | 51.58%     | ok               |
| GLD        |       50 | 21.55%   | 84.01%             | -16.63% |     0.56 | 47.59%     | ok               |
| GOOGL      |       55 | 78.89%   | 171.31%            | -20.41% |     1.18 | 52.25%     | ok               |
| GRT-USD    |       83 | -1.12%   | -87.55%            | -50.20% |     0.2  | 43.87%     | ok               |
| GS         |       74 | -0.54%   | 165.97%            | -22.13% |     0.09 | 50.75%     | ok               |
| HD         |       71 | -6.05%   | -8.48%             | -17.69% |    -0.08 | 44.09%     | ok               |
| HON        |       95 | -26.35%  | 24.64%             | -29.81% |    -0.7  | 52.41%     | ok               |
| HYG        |       81 | -8.84%   | 2.48%              | -9.55%  |    -1.03 | 34.28%     | ok               |
| IBIT       |       34 | 30.82%   | -4.87%             | -18.95% |     0.65 | 31.22%     | ok               |
| IBM        |       75 | -25.46%  | 18.04%             | -47.10% |    -0.31 | 50.92%     | ok               |
| ICP-USD    |       79 | -20.15%  | -67.88%            | -50.29% |     0.05 | 34.67%     | ok               |
| IEF        |       82 | -11.16%  | -2.41%             | -11.70% |    -1.57 | 33.78%     | ok               |
| IEMG       |       58 | -9.60%   | 51.82%             | -26.84% |    -0.28 | 40.60%     | ok               |
| INJ-USD    |       75 | -52.79%  | -61.53%            | -76.24% |    -0.5  | 38.12%     | ok               |
| INTC       |       66 | 59.37%   | 102.85%            | -60.60% |     0.64 | 48.59%     | ok               |
| INTU       |       69 | -17.72%  | -51.08%            | -41.36% |    -0.19 | 41.76%     | ok               |
| ITA        |       72 | -4.17%   | 92.36%             | -23.75% |    -0.05 | 46.42%     | ok               |
| IWM        |       48 | 9.40%    | 44.36%             | -12.83% |     0.39 | 35.77%     | ok               |
| JNJ        |       70 | 5.73%    | 57.79%             | -17.51% |     0.25 | 50.58%     | ok               |
| JPM        |       77 | -23.09%  | 87.29%             | -33.43% |    -0.58 | 52.08%     | ok               |
| KO         |       51 | 23.75%   | 44.19%             | -8.20%  |     0.85 | 37.94%     | ok               |
| LDO-USD    |       78 | 34.87%   | -73.76%            | -61.16% |     0.54 | 43.10%     | ok               |
| LIN        |       66 | -9.62%   | 2.34%              | -21.53% |    -0.3  | 37.10%     | ok               |
| LINK-USD   |       73 | -17.80%  | -44.63%            | -39.15% |     0.05 | 43.68%     | ok               |
| LLY        |       69 | -24.98%  | 52.70%             | -53.34% |    -0.35 | 47.59%     | ok               |
| LRCX       |       82 | -22.68%  | 216.38%            | -60.21% |    -0.12 | 42.43%     | ok               |
| LTC-USD    |       72 | -27.94%  | -64.41%            | -47.04% |    -0.2  | 49.81%     | ok               |
| MCD        |       77 | -3.77%   | -10.04%            | -18.81% |    -0.1  | 38.27%     | ok               |
| META       |       76 | -34.60%  | 22.05%             | -42.43% |    -0.62 | 47.42%     | ok               |
| MPC        |       67 | -9.01%   | 69.25%             | -44.76% |    -0.04 | 49.58%     | ok               |
| MRK        |       67 | -27.34%  | 4.07%              | -35.95% |    -0.63 | 43.59%     | ok               |
| MS         |       77 | -10.18%  | 142.96%            | -27.79% |    -0.16 | 49.58%     | ok               |
| MSFT       |       83 | -34.59%  | 20.55%             | -39.15% |    -0.87 | 47.25%     | ok               |
| MU         |       51 | 225.56%  | 777.68%            | -68.76% |     1.23 | 58.24%     | ok               |
| NEAR-USD   |       83 | -5.33%   | -46.37%            | -59.54% |     0.2  | 40.23%     | ok               |
| NEM        |       70 | -20.55%  | 170.63%            | -38.49% |    -0.15 | 52.75%     | ok               |
| NFLX       |       72 | 21.42%   | 22.03%             | -21.09% |     0.51 | 53.24%     | ok               |
| NKE        |       85 | -36.83%  | -57.82%            | -55.35% |    -0.51 | 44.09%     | ok               |
| NOW        |       80 | 1.54%    | -24.55%            | -26.78% |     0.18 | 45.76%     | ok               |
| NVDA       |       73 | -28.45%  | 128.20%            | -45.14% |    -0.22 | 59.00%     | ok               |
| OP-USD     |       66 | -16.82%  | -91.47%            | -71.26% |     0.06 | 35.06%     | ok               |
| ORCL       |       68 | 94.81%   | 24.29%             | -29.47% |     0.85 | 55.91%     | ok               |
| OXY        |       71 | 4.09%    | -9.83%             | -31.61% |     0.19 | 46.26%     | ok               |
| PEP        |       77 | -5.12%   | -15.24%            | -21.35% |    -0.08 | 48.42%     | ok               |
| PEPE-USD   |       81 | -8.77%   | -61.18%            | -57.66% |     0.2  | 45.98%     | ok               |
| PFE        |       79 | -41.91%  | -11.77%            | -42.74% |    -1.36 | 36.61%     | ok               |
| PG         |       66 | -19.86%  | -10.26%            | -24.25% |    -0.76 | 37.94%     | ok               |
| PM         |       83 | -6.79%   | 98.51%             | -34.79% |    -0.06 | 55.74%     | ok               |
| POL-USD    |       81 | 52.97%   | -74.14%            | -41.08% |     0.7  | 49.43%     | ok               |
| QCOM       |       77 | -18.98%  | -11.42%            | -56.59% |    -0.1  | 45.59%     | ok               |
| QQQ        |       60 | 20.33%   | 60.06%             | -12.88% |     0.58 | 43.59%     | ok               |
| RENDER-USD |      100 | -21.49%  | -64.32%            | -43.50% |     0.06 | 42.15%     | ok               |
| RTX        |       54 | 41.27%   | 137.04%            | -16.99% |     0.89 | 53.58%     | ok               |
| SBUX       |       62 | -19.04%  | 12.27%             | -29.22% |    -0.35 | 39.93%     | ok               |
| SCHW       |       76 | -8.99%   | 58.13%             | -31.92% |    -0.13 | 48.92%     | ok               |
| SHIB-USD   |       76 | -29.78%  | -63.29%            | -47.96% |    -0.2  | 52.49%     | ok               |
| SHY        |       46 | -2.23%   | 0.05%              | -2.85%  |    -0.78 | 34.11%     | ok               |
| SKY-USD    |       76 | -32.19%  | -3.10%             | -47.82% |    -0.4  | 42.28%     | ok               |
| SLB        |       77 | -30.27%  | -4.31%             | -54.23% |    -0.55 | 51.08%     | ok               |
| SLV        |       62 | 43.25%   | 134.72%            | -42.66% |     0.63 | 43.93%     | ok               |
| SMH        |       48 | 69.17%   | 146.84%            | -33.99% |     1    | 45.76%     | ok               |
| SNX-USD    |       64 | -19.30%  | -75.67%            | -38.09% |     0.03 | 37.55%     | ok               |
| SOL-USD    |       74 | -47.60%  | -48.87%            | -46.86% |    -0.35 | 59.39%     | ok               |
| SOXX       |       55 | 64.86%   | 125.54%            | -40.34% |     0.91 | 44.76%     | ok               |
| SPY        |       62 | 1.82%    | 48.19%             | -16.47% |     0.12 | 49.25%     | ok               |
| SUSHI-USD  |      104 | -83.33%  | -80.29%            | -86.63% |    -1.35 | 38.31%     | ok               |
| T          |       66 | 34.39%   | 36.12%             | -17.01% |     0.77 | 54.24%     | ok               |
| TGT        |       62 | -18.21%  | -11.14%            | -40.57% |    -0.37 | 37.27%     | ok               |
| TIA-USD    |       89 | -40.67%  | -91.91%            | -68.36% |    -0.24 | 38.89%     | ok               |
| TLT        |       72 | -19.34%  | -14.10%            | -21.87% |    -1.43 | 33.94%     | ok               |
| TMO        |       61 | 25.67%   | -4.24%             | -18.85% |     0.56 | 52.58%     | ok               |
| TMUS       |       68 | 4.31%    | 7.48%              | -25.71% |     0.19 | 46.59%     | ok               |
| TRX-USD    |       70 | 10.65%   | 40.56%             | -22.90% |     0.37 | 48.47%     | ok               |
| TSLA       |       74 | -24.87%  | 81.18%             | -57.89% |    -0.08 | 42.43%     | ok               |
| TXN        |       73 | -17.93%  | 54.45%             | -47.39% |    -0.14 | 50.92%     | ok               |
| UNH        |       74 | 29.80%   | -15.09%            | -26.96% |     0.52 | 52.25%     | ok               |
| UNI-USD    |       90 | -73.84%  | -48.31%            | -80.33% |    -0.89 | 46.17%     | ok               |
| UPS        |       74 | -42.91%  | -30.94%            | -43.14% |    -0.9  | 40.43%     | ok               |
| USO        |       70 | 3.91%    | 65.88%             | -43.35% |     0.19 | 34.78%     | ok               |
| VEA        |       58 | -3.47%   | 42.88%             | -19.24% |    -0.09 | 42.60%     | ok               |
| VIXY       |       94 | -79.98%  | -64.32%            | -88.16% |    -1    | 31.95%     | ok               |
| VNQ        |       73 | -17.08%  | 13.47%             | -24.66% |    -0.72 | 37.77%     | ok               |
| VTI        |       68 | -4.92%   | 47.17%             | -18.77% |    -0.12 | 49.58%     | ok               |
| VWO        |       82 | -16.89%  | 41.06%             | -25.20% |    -0.62 | 42.26%     | ok               |
| VZ         |       83 | -25.00%  | 18.02%             | -26.98% |    -0.8  | 38.27%     | ok               |
| WFC        |       84 | -19.98%  | 53.95%             | -29.78% |    -0.35 | 49.42%     | ok               |
| WIF-USD    |       72 | -52.90%  | -76.95%            | -61.76% |    -0.39 | 33.91%     | ok               |
| WMT        |       65 | 10.14%   | 82.51%             | -21.31% |     0.34 | 49.08%     | ok               |
| XBI        |       66 | -5.68%   | 52.13%             | -18.30% |    -0.07 | 39.43%     | ok               |
| XLB        |       62 | -11.09%  | 12.90%             | -24.41% |    -0.37 | 35.27%     | ok               |
| XLC        |       67 | 11.41%   | 40.16%             | -12.33% |     0.43 | 52.91%     | ok               |
| XLE        |       75 | -8.92%   | 31.99%             | -37.17% |    -0.15 | 45.42%     | ok               |
| XLF        |       78 | -11.97%  | 41.02%             | -23.61% |    -0.39 | 47.75%     | ok               |
| XLI        |       68 | -4.86%   | 50.54%             | -14.12% |    -0.15 | 42.60%     | ok               |
| XLK        |       40 | 65.83%   | 72.20%             | -14.75% |     1.22 | 45.59%     | ok               |
| XLM-USD    |       65 | 7.39%    | -45.27%            | -50.36% |     0.3  | 45.21%     | ok               |
| XLP        |       64 | 9.31%    | 12.29%             | -8.96%  |     0.55 | 40.77%     | ok               |
| XLU        |       67 | -5.24%   | 38.47%             | -20.40% |    -0.19 | 39.10%     | ok               |
| XLV        |       66 | -14.97%  | 10.86%             | -18.72% |    -0.74 | 34.44%     | ok               |
| XLY        |       68 | 3.22%    | 31.48%             | -14.01% |     0.17 | 43.93%     | ok               |
| XOM        |       55 | 8.30%    | 42.23%             | -20.29% |     0.29 | 37.94%     | ok               |
| XRP-USD    |       54 | -22.96%  | -50.91%            | -38.94% |    -0.14 | 33.14%     | ok               |
| YFI-USD    |       81 | -64.19%  | -61.24%            | -71.12% |    -1.03 | 40.61%     | ok               |
| ZEC-USD    |       64 | 38.58%   | 1182.66%           | -49.45% |     0.53 | 37.16%     | ok               |

## AAPL Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 14.29%   | 75.64%             | -21.71% |     0.37 |       68 | 53.24%     | ok               |
|          15 | 10.78%   | 75.64%             | -23.86% |     0.3  |       75 | 60.40%     | ok               |
|          30 | 6.01%    | 75.64%             | -20.65% |     0.22 |       61 | 49.08%     | ok               |
|          25 | 3.80%    | 75.64%             | -20.03% |     0.18 |       67 | 50.92%     | ok               |
|          35 | 3.63%    | 75.64%             | -22.04% |     0.18 |       61 | 47.59%     | ok               |

## AAVE-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 5.18%    | -52.80%            | -43.61% |     0.27 |       42 | 31.23%     | ok               |
|          45 | -7.84%   | -52.80%            | -49.19% |     0.11 |       44 | 26.63%     | ok               |
|          35 | -12.81%  | -52.80%            | -51.96% |     0.08 |       52 | 34.48%     | ok               |
|          15 | -45.45%  | -52.80%            | -61.76% |    -0.24 |       81 | 52.68%     | ok               |
|          50 | -36.50%  | -52.80%            | -45.07% |    -0.42 |       42 | 19.35%     | ok               |

## ABBV Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -13.30%  | 36.45%             | -28.51% |    -0.28 |       50 | 34.78%     | ok               |
|          25 | -23.22%  | 36.45%             | -31.26% |    -0.5  |       69 | 48.59%     | ok               |
|          30 | -23.13%  | 36.45%             | -30.55% |    -0.5  |       70 | 46.76%     | ok               |
|          20 | -23.81%  | 36.45%             | -30.60% |    -0.51 |       69 | 50.42%     | ok               |
|          40 | -22.27%  | 36.45%             | -26.61% |    -0.53 |       68 | 39.60%     | ok               |

## ADA-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -77.68%  | -70.55%            | -48.76% |    -0.58 |       59 | 27.20%     | ok               |
|          45 | -79.36%  | -70.55%            | -54.71% |    -0.59 |       60 | 31.42%     | ok               |
|          35 | -81.81%  | -70.55%            | -61.11% |    -0.64 |       78 | 41.95%     | ok               |
|          30 | -82.08%  | -70.55%            | -58.47% |    -0.64 |       86 | 45.98%     | ok               |
|          40 | -81.96%  | -70.55%            | -61.15% |    -0.66 |       76 | 36.97%     | ok               |

## ADBE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 3.20%    | -55.15%            | -21.57% |     0.18 |       76 | 49.42%     | ok               |
|          40 | -14.98%  | -55.15%            | -29.34% |    -0.17 |       72 | 42.26%     | ok               |
|          25 | -20.27%  | -55.15%            | -28.88% |    -0.17 |       50 | 60.90%     | ok               |
|          20 | -28.23%  | -55.15%            | -32.09% |    -0.3  |       52 | 63.56%     | ok               |
|          15 | -30.82%  | -55.15%            | -36.64% |    -0.34 |       61 | 65.56%     | ok               |

## AGG Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -6.12%   | -0.92%             | -10.17% |    -1    |       69 | 33.28%     | ok               |
|          20 | -7.67%   | -0.92%             | -11.49% |    -1.11 |       71 | 38.77%     | ok               |
|          45 | -5.79%   | -0.92%             | -7.91%  |    -1.14 |       56 | 22.63%     | ok               |
|          50 | -5.29%   | -0.92%             | -7.92%  |    -1.16 |       52 | 18.30%     | ok               |
|          25 | -7.84%   | -0.92%             | -12.13% |    -1.18 |       71 | 37.10%     | ok               |

## ALGO-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -41.24%  | -64.72%            | -44.44% |    -0.39 |       82 | 36.78%     | ok               |
|          35 | -47.53%  | -64.72%            | -47.53% |    -0.61 |       60 | 30.27%     | ok               |
|          15 | -64.43%  | -64.72%            | -62.63% |    -0.77 |       84 | 49.23%     | ok               |
|          25 | -62.38%  | -64.72%            | -66.02% |    -0.77 |       82 | 43.68%     | ok               |
|          50 | -45.64%  | -64.72%            | -48.43% |    -0.81 |       42 | 16.86%     | ok               |

## AMAT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -24.47%  | 157.34%            | -54.69% |    -0.11 |       68 | 59.23%     | ok               |
|          30 | -35.85%  | 157.34%            | -57.08% |    -0.34 |       71 | 50.25%     | ok               |
|          35 | -36.30%  | 157.34%            | -55.13% |    -0.37 |       73 | 47.92%     | ok               |
|          50 | -35.25%  | 157.34%            | -48.72% |    -0.39 |       52 | 35.94%     | ok               |
|          20 | -43.21%  | 157.34%            | -60.72% |    -0.45 |       74 | 55.57%     | ok               |

## AMD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 8.15%    | 144.29%            | -44.55% |     0.28 |       56 | 30.12%     | ok               |
|          40 | 7.26%    | 144.29%            | -44.27% |     0.28 |       54 | 35.27%     | ok               |
|          35 | -0.04%   | 144.29%            | -48.82% |     0.21 |       62 | 36.94%     | ok               |
|          30 | -13.22%  | 144.29%            | -54.80% |     0.08 |       63 | 39.43%     | ok               |
|          45 | -13.67%  | 144.29%            | -53.48% |     0.05 |       62 | 32.95%     | ok               |

## AMGN Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | -8.30%   | 37.59%             | -31.29% |    -0.1  |       67 | 43.59%     | ok               |
|          20 | -10.76%  | 37.59%             | -26.65% |    -0.14 |       74 | 53.58%     | ok               |
|          15 | -14.69%  | 37.59%             | -27.98% |    -0.22 |       71 | 58.40%     | ok               |
|          30 | -14.44%  | 37.59%             | -34.19% |    -0.25 |       75 | 47.59%     | ok               |
|          25 | -16.79%  | 37.59%             | -33.47% |    -0.3  |       69 | 49.92%     | ok               |

## AMZN Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -19.96%  | 65.17%             | -28.96% |    -0.57 |       56 | 29.62%     | ok               |
|          50 | -22.96%  | 65.17%             | -34.08% |    -0.79 |       50 | 22.80%     | ok               |
|          45 | -30.50%  | 65.17%             | -35.71% |    -1.06 |       58 | 26.12%     | ok               |
|          35 | -45.95%  | 65.17%             | -49.36% |    -1.29 |       71 | 33.61%     | ok               |
|          30 | -51.44%  | 65.17%             | -54.51% |    -1.42 |       82 | 39.27%     | ok               |

## APT-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 19.10%   | -90.84%            | -46.73% |     0.42 |       40 | 18.97%     | ok               |
|          45 | -11.65%  | -90.84%            | -63.86% |     0.05 |       56 | 24.52%     | ok               |
|          35 | -17.11%  | -90.84%            | -60.63% |     0.04 |       66 | 35.25%     | ok               |
|          20 | -23.85%  | -90.84%            | -68.18% |     0.02 |       71 | 50.19%     | ok               |
|          25 | -28.18%  | -90.84%            | -68.00% |    -0.05 |       68 | 45.79%     | ok               |

## ARB-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 30.87%   | -80.07%            | -51.09% |     0.51 |       86 | 57.66%     | ok               |
|          20 | 0.60%    | -80.07%            | -58.28% |     0.28 |       72 | 51.53%     | ok               |
|          40 | -3.36%   | -80.07%            | -44.29% |     0.18 |       58 | 31.23%     | ok               |
|          45 | -3.87%   | -80.07%            | -47.43% |     0.16 |       60 | 24.14%     | ok               |
|          25 | -15.54%  | -80.07%            | -55.53% |     0.13 |       74 | 47.32%     | ok               |

## ARKK Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -29.06%  | 45.19%             | -37.76% |    -0.37 |       94 | 52.41%     | ok               |
|          20 | -32.82%  | 45.19%             | -37.99% |    -0.47 |       91 | 47.92%     | ok               |
|          30 | -34.24%  | 45.19%             | -37.98% |    -0.59 |       89 | 40.93%     | ok               |
|          35 | -36.45%  | 45.19%             | -38.33% |    -0.68 |       88 | 38.27%     | ok               |
|          40 | -37.79%  | 45.19%             | -39.63% |    -0.76 |       80 | 33.44%     | ok               |

## ATOM-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -64.20%  | -69.48%            | -69.46% |    -0.84 |       85 | 62.64%     | ok               |
|          25 | -64.15%  | -69.48%            | -71.09% |    -0.93 |       93 | 53.45%     | ok               |
|          45 | -60.15%  | -69.48%            | -67.66% |    -1.09 |       74 | 31.23%     | ok               |
|          30 | -67.48%  | -69.48%            | -73.98% |    -1.1  |       88 | 46.74%     | ok               |
|          20 | -71.19%  | -69.48%            | -74.75% |    -1.12 |       95 | 56.70%     | ok               |

## AVAX-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -5.68%   | -68.56%            | -40.19% |     0.08 |       34 | 18.39%     | ok               |
|          45 | -17.71%  | -68.56%            | -47.25% |    -0.12 |       34 | 22.22%     | ok               |
|          40 | -26.39%  | -68.56%            | -47.33% |    -0.23 |       40 | 25.10%     | ok               |
|          15 | -42.14%  | -68.56%            | -43.73% |    -0.28 |       77 | 52.68%     | ok               |
|          35 | -37.99%  | -68.56%            | -48.89% |    -0.39 |       58 | 30.46%     | ok               |

## AVGO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 26.25%   | 203.32%            | -35.84% |     0.46 |       54 | 29.62%     | ok               |
|          30 | 24.24%   | 203.32%            | -35.76% |     0.43 |       62 | 40.93%     | ok               |
|          40 | 22.75%   | 203.32%            | -40.70% |     0.42 |       60 | 34.78%     | ok               |
|          25 | 21.63%   | 203.32%            | -38.01% |     0.41 |       70 | 42.43%     | ok               |
|          45 | 21.10%   | 203.32%            | -41.66% |     0.4  |       54 | 32.95%     | ok               |

## BA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 23.47%   | 21.30%             | -13.42% |     0.62 |       42 | 31.28%     | ok               |
|          35 | 27.08%   | 21.30%             | -23.77% |     0.55 |       70 | 44.26%     | ok               |
|          40 | 17.66%   | 21.30%             | -25.45% |     0.43 |       46 | 38.44%     | ok               |
|          25 | 6.31%    | 21.30%             | -32.48% |     0.23 |       70 | 51.75%     | ok               |
|          30 | 3.44%    | 21.30%             | -30.56% |     0.18 |       67 | 48.42%     | ok               |

## BAC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 1.57%    | 74.09%             | -20.40% |     0.12 |       62 | 38.27%     | ok               |
|          20 | 1.02%    | 74.09%             | -20.73% |     0.11 |       78 | 55.41%     | ok               |
|          35 | 0.67%    | 74.09%             | -27.83% |     0.09 |       70 | 47.09%     | ok               |
|          15 | -3.77%   | 74.09%             | -22.24% |     0.01 |       80 | 59.73%     | ok               |
|          50 | -3.08%   | 74.09%             | -20.35% |    -0.04 |       62 | 34.61%     | ok               |

## BCH-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -0.72%   | -31.63%            | -47.24% |     0.24 |       74 | 59.77%     | ok               |
|          30 | -1.91%   | -31.63%            | -54.26% |     0.19 |       78 | 50.77%     | ok               |
|          20 | -10.23%  | -31.63%            | -50.86% |     0.13 |       70 | 56.32%     | ok               |
|          40 | -16.36%  | -31.63%            | -61.24% |    -0.01 |       67 | 41.95%     | ok               |
|          25 | -23.23%  | -31.63%            | -57.98% |    -0.03 |       73 | 53.07%     | ok               |

## BITO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -12.12%  | -73.98%            | -31.98% |    -0.06 |       52 | 22.63%     | ok               |
|          30 | -26.85%  | -73.98%            | -42.82% |    -0.22 |       80 | 39.43%     | ok               |
|          15 | -32.24%  | -73.98%            | -48.38% |    -0.23 |       89 | 48.42%     | ok               |
|          45 | -26.07%  | -73.98%            | -41.96% |    -0.29 |       60 | 26.29%     | ok               |
|          40 | -29.37%  | -73.98%            | -44.44% |    -0.31 |       64 | 31.11%     | ok               |

## BLK Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 0.64%    | 36.53%             | -21.48% |     0.1  |       82 | 49.25%     | ok               |
|          35 | -0.85%   | 36.53%             | -20.79% |     0.05 |       86 | 40.27%     | ok               |
|          40 | -2.86%   | 36.53%             | -22.83% |    -0.02 |       78 | 36.11%     | ok               |
|          25 | -4.65%   | 36.53%             | -24.62% |    -0.05 |       77 | 46.76%     | ok               |
|          30 | -7.13%   | 36.53%             | -26.90% |    -0.13 |       81 | 44.09%     | ok               |

## BND Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -6.09%   | -0.93%             | -9.43%  |    -0.87 |       64 | 40.10%     | ok               |
|          25 | -6.97%   | -0.93%             | -10.73% |    -1.05 |       67 | 38.27%     | ok               |
|          30 | -7.08%   | -0.93%             | -10.16% |    -1.12 |       67 | 34.94%     | ok               |
|          15 | -8.36%   | -0.93%             | -11.30% |    -1.19 |       76 | 42.93%     | ok               |
|          45 | -7.56%   | -0.93%             | -9.57%  |    -1.43 |       54 | 24.13%     | ok               |

## BONK-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 165.22%  | -78.68%            | -35.57% |     1.21 |       48 | 22.41%     | ok               |
|          25 | 145.12%  | -78.68%            | -54.47% |     0.97 |       67 | 48.85%     | ok               |
|          15 | 133.10%  | -78.68%            | -62.48% |     0.91 |       72 | 57.47%     | ok               |
|          20 | 114.25%  | -78.68%            | -61.03% |     0.87 |       67 | 53.07%     | ok               |
|          40 | 77.06%   | -78.68%            | -53.34% |     0.76 |       56 | 35.06%     | ok               |

## BTC-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 64.79%   | -25.96%            | -14.50% |     1.12 |       42 | 33.52%     | ok               |
|          45 | 49.87%   | -25.96%            | -13.36% |     0.94 |       40 | 30.08%     | ok               |
|          35 | 42.81%   | -25.96%            | -21.56% |     0.79 |       66 | 40.61%     | ok               |
|          30 | 25.66%   | -25.96%            | -21.75% |     0.53 |       70 | 47.32%     | ok               |
|          50 | 17.90%   | -25.96%            | -18.05% |     0.47 |       40 | 25.10%     | ok               |

## C Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -5.72%   | 132.66%            | -21.64% |    -0.08 |       64 | 35.44%     | ok               |
|          45 | -18.06%  | 132.66%            | -29.73% |    -0.42 |       76 | 39.60%     | ok               |
|          25 | -27.20%  | 132.66%            | -34.97% |    -0.51 |       71 | 52.41%     | ok               |
|          40 | -23.81%  | 132.66%            | -34.65% |    -0.55 |       76 | 41.93%     | ok               |
|          20 | -29.64%  | 132.66%            | -36.33% |    -0.56 |       79 | 55.41%     | ok               |

## CAT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 17.78%   | 147.79%            | -21.02% |     0.39 |       72 | 53.91%     | ok               |
|          25 | 17.89%   | 147.79%            | -26.37% |     0.39 |       68 | 56.74%     | ok               |
|          45 | 12.96%   | 147.79%            | -27.12% |     0.33 |       56 | 42.60%     | ok               |
|          20 | 12.47%   | 147.79%            | -25.65% |     0.32 |       80 | 60.40%     | ok               |
|          15 | 12.19%   | 147.79%            | -30.60% |     0.31 |       75 | 67.55%     | ok               |

## CL Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 5.77%    | 1.99%              | -12.98% |     0.28 |       44 | 27.95%     | ok               |
|          30 | 5.31%    | 1.99%              | -14.32% |     0.23 |       62 | 43.93%     | ok               |
|          45 | 0.93%    | 1.99%              | -13.51% |     0.09 |       48 | 30.95%     | ok               |
|          35 | 0.29%    | 1.99%              | -13.83% |     0.07 |       64 | 40.27%     | ok               |
|          40 | -2.61%   | 1.99%              | -12.70% |    -0.04 |       58 | 34.94%     | ok               |

## CMCSA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -42.45%  | -39.81%            | -45.19% |    -0.98 |       89 | 56.57%     | ok               |
|          30 | -45.38%  | -39.81%            | -48.04% |    -1.23 |       80 | 42.10%     | ok               |
|          50 | -31.14%  | -39.81%            | -32.82% |    -1.24 |       48 | 13.98%     | ok               |
|          25 | -47.07%  | -39.81%            | -49.58% |    -1.27 |       87 | 47.25%     | ok               |
|          35 | -45.52%  | -39.81%            | -47.87% |    -1.33 |       93 | 36.44%     | ok               |

## COMP-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -6.30%   | -67.07%            | -38.71% |     0.11 |       48 | 20.88%     | ok               |
|          30 | -43.71%  | -67.07%            | -57.10% |    -0.32 |       93 | 46.36%     | ok               |
|          25 | -47.17%  | -67.07%            | -60.58% |    -0.35 |       93 | 53.83%     | ok               |
|          15 | -55.02%  | -67.07%            | -65.55% |    -0.44 |      105 | 64.75%     | ok               |
|          40 | -47.97%  | -67.07%            | -53.06% |    -0.51 |       74 | 34.29%     | ok               |

## COP Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -1.69%   | 3.39%              | -35.08% |     0.05 |       48 | 29.62%     | ok               |
|          35 | -14.58%  | 3.39%              | -43.58% |    -0.21 |       73 | 40.43%     | ok               |
|          45 | -13.01%  | 3.39%              | -41.35% |    -0.21 |       62 | 33.11%     | ok               |
|          30 | -19.02%  | 3.39%              | -43.77% |    -0.3  |       72 | 43.93%     | ok               |
|          40 | -18.50%  | 3.39%              | -47.05% |    -0.34 |       68 | 36.27%     | ok               |

## COST Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 12.24%   | 33.61%             | -24.32% |     0.42 |       64 | 48.25%     | ok               |
|          25 | 10.58%   | 33.61%             | -24.73% |     0.38 |       61 | 45.42%     | ok               |
|          35 | 6.54%    | 33.61%             | -26.58% |     0.28 |       52 | 38.60%     | ok               |
|          30 | 0.55%    | 33.61%             | -29.73% |     0.08 |       60 | 41.76%     | ok               |
|          15 | -2.36%   | 33.61%             | -27.30% |     0.01 |       65 | 51.75%     | ok               |

## CRM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -35.79%  | -39.23%            | -44.67% |    -0.57 |       90 | 54.91%     | ok               |
|          35 | -29.63%  | -39.23%            | -33.08% |    -0.59 |       60 | 37.94%     | ok               |
|          40 | -34.83%  | -39.23%            | -39.11% |    -0.8  |       66 | 33.94%     | ok               |
|          20 | -43.35%  | -39.23%            | -45.69% |    -0.82 |       74 | 48.59%     | ok               |
|          30 | -39.56%  | -39.23%            | -41.36% |    -0.83 |       63 | 42.76%     | ok               |

## CRV-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 27.72%   | -52.61%            | -37.78% |     0.48 |       70 | 31.80%     | ok               |
|          45 | 12.07%   | -52.61%            | -42.29% |     0.33 |       56 | 21.07%     | ok               |
|          50 | 7.86%    | -52.61%            | -29.30% |     0.28 |       46 | 17.43%     | ok               |
|          40 | 5.82%    | -52.61%            | -38.86% |     0.27 |       60 | 27.39%     | ok               |
|          30 | -0.17%   | -52.61%            | -39.89% |     0.23 |       70 | 36.59%     | ok               |

## CSCO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 35.16%   | 130.70%            | -19.34% |     0.75 |       48 | 36.61%     | ok               |
|          45 | 30.59%   | 130.70%            | -19.34% |     0.66 |       49 | 38.27%     | ok               |
|          35 | 25.61%   | 130.70%            | -23.68% |     0.55 |       51 | 45.09%     | ok               |
|          25 | 24.55%   | 130.70%            | -23.28% |     0.53 |       61 | 49.58%     | ok               |
|          30 | 23.34%   | 130.70%            | -21.79% |     0.51 |       59 | 47.75%     | ok               |

## CVX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -4.26%   | 27.09%             | -27.34% |    -0.05 |       73 | 35.44%     | ok               |
|          25 | -5.86%   | 27.09%             | -24.33% |    -0.07 |       71 | 43.26%     | ok               |
|          45 | -5.17%   | 27.09%             | -28.83% |    -0.09 |       63 | 31.95%     | ok               |
|          35 | -5.80%   | 27.09%             | -28.85% |    -0.09 |       65 | 37.77%     | ok               |
|          30 | -9.65%   | 27.09%             | -29.13% |    -0.2  |       71 | 40.60%     | ok               |

## DASH-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 97.45%   | 22.51%             | -27.84% |     0.83 |       40 | 15.71%     | ok               |
|          40 | 58.42%   | 22.51%             | -31.16% |     0.64 |       46 | 22.41%     | ok               |
|          45 | 42.36%   | 22.51%             | -36.57% |     0.55 |       44 | 17.82%     | ok               |
|          35 | -38.79%  | 22.51%             | -63.23% |     0.01 |       69 | 26.82%     | ok               |
|          30 | -41.94%  | 22.51%             | -64.43% |    -0.02 |       63 | 29.69%     | ok               |

## DBC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -6.83%   | 29.16%             | -27.07% |    -0.17 |       74 | 40.93%     | ok               |
|          25 | -9.82%   | 29.16%             | -26.10% |    -0.28 |       64 | 37.27%     | ok               |
|          50 | -8.66%   | 29.16%             | -20.31% |    -0.3  |       44 | 23.46%     | ok               |
|          20 | -10.36%  | 29.16%             | -26.24% |    -0.3  |       67 | 39.10%     | ok               |
|          45 | -11.19%  | 29.16%             | -21.46% |    -0.38 |       60 | 27.12%     | ok               |

## DE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -5.08%   | 61.33%             | -30.12% |    -0.01 |       74 | 51.08%     | ok               |
|          30 | -5.05%   | 61.33%             | -24.56% |    -0.01 |       70 | 45.42%     | ok               |
|          45 | -4.42%   | 61.33%             | -24.94% |    -0.02 |       64 | 35.44%     | ok               |
|          50 | -5.03%   | 61.33%             | -23.29% |    -0.05 |       68 | 31.28%     | ok               |
|          25 | -8.69%   | 61.33%             | -28.87% |    -0.09 |       76 | 48.09%     | ok               |

## DIA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -2.93%   | 36.76%             | -11.28% |    -0.12 |       58 | 44.59%     | ok               |
|          35 | -2.94%   | 36.76%             | -13.15% |    -0.13 |       60 | 41.43%     | ok               |
|          30 | -4.54%   | 36.76%             | -12.94% |    -0.21 |       58 | 43.26%     | ok               |
|          20 | -6.32%   | 36.76%             | -14.29% |    -0.3  |       64 | 47.09%     | ok               |
|          40 | -6.89%   | 36.76%             | -15.06% |    -0.38 |       66 | 38.60%     | ok               |

## DIS Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 15.47%   | -12.62%            | -16.40% |     0.51 |       48 | 26.12%     | ok               |
|          40 | -10.47%  | -12.62%            | -24.07% |    -0.16 |       63 | 34.78%     | ok               |
|          45 | -10.23%  | -12.62%            | -18.50% |    -0.18 |       49 | 29.95%     | ok               |
|          15 | -17.12%  | -12.62%            | -31.15% |    -0.25 |       89 | 55.57%     | ok               |
|          35 | -17.38%  | -12.62%            | -25.70% |    -0.32 |       75 | 40.93%     | ok               |

## DOGE-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -8.48%   | -65.95%            | -59.36% |     0.21 |       78 | 64.37%     | ok               |
|          25 | -11.78%  | -65.95%            | -55.33% |     0.15 |       69 | 54.41%     | ok               |
|          20 | -14.66%  | -65.95%            | -57.37% |     0.13 |       81 | 59.58%     | ok               |
|          30 | -26.18%  | -65.95%            | -62.31% |    -0.03 |       72 | 48.85%     | ok               |
|          35 | -48.05%  | -65.95%            | -61.79% |    -0.43 |       68 | 42.53%     | ok               |

## DOT-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -37.25%  | -81.93%            | -48.63% |    -0.5  |       58 | 26.25%     | ok               |
|          45 | -39.99%  | -81.93%            | -51.81% |    -0.5  |       50 | 31.42%     | ok               |
|          35 | -57.95%  | -81.93%            | -63.08% |    -0.63 |       78 | 41.57%     | ok               |
|          15 | -66.50%  | -81.93%            | -73.29% |    -0.64 |       81 | 62.84%     | ok               |
|          20 | -63.99%  | -81.93%            | -68.03% |    -0.68 |       89 | 59.20%     | ok               |

## DXY-INDEX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -1.69%   | -1.67%             | -6.29%  |    -0.25 |       42 | 32.75%     | ok               |
|          15 | -2.97%   | -1.67%             | -11.37% |    -0.25 |       80 | 76.36%     | ok               |
|          40 | -4.66%   | -1.67%             | -8.24%  |    -0.59 |       68 | 50.54%     | ok               |
|          25 | -6.28%   | -1.67%             | -12.10% |    -0.68 |       78 | 66.59%     | ok               |
|          35 | -5.86%   | -1.67%             | -10.39% |    -0.72 |       71 | 56.62%     | ok               |

## EEM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -4.74%   | 57.22%             | -15.88% |    -0.11 |       50 | 33.78%     | ok               |
|          45 | -6.41%   | 57.22%             | -17.36% |    -0.18 |       52 | 35.27%     | ok               |
|          40 | -6.75%   | 57.22%             | -19.52% |    -0.18 |       64 | 37.44%     | ok               |
|          35 | -7.40%   | 57.22%             | -23.88% |    -0.18 |       66 | 39.43%     | ok               |
|          25 | -10.21%  | 57.22%             | -25.60% |    -0.27 |       65 | 42.43%     | ok               |

## EFA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -5.80%   | 34.54%             | -11.76% |    -0.15 |       64 | 50.08%     | ok               |
|          30 | -10.05%  | 34.54%             | -13.53% |    -0.38 |       58 | 41.76%     | ok               |
|          20 | -11.76%  | 34.54%             | -13.10% |    -0.43 |       69 | 47.25%     | ok               |
|          50 | -10.68%  | 34.54%             | -17.56% |    -0.49 |       54 | 34.44%     | ok               |
|          25 | -12.86%  | 34.54%             | -15.78% |    -0.5  |       64 | 44.59%     | ok               |

## EOG Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -13.92%  | 20.58%             | -39.69% |    -0.26 |       58 | 35.27%     | ok               |
|          30 | -18.91%  | 20.58%             | -48.13% |    -0.35 |       81 | 49.08%     | ok               |
|          40 | -19.02%  | 20.58%             | -43.26% |    -0.4  |       66 | 38.60%     | ok               |
|          35 | -19.80%  | 20.58%             | -46.26% |    -0.4  |       79 | 43.76%     | ok               |
|          25 | -23.03%  | 20.58%             | -51.99% |    -0.43 |       82 | 52.08%     | ok               |

## ETC-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -2.84%   | -65.34%            | -31.28% |     0.08 |       26 | 15.90%     | ok               |
|          45 | -12.62%  | -65.34%            | -38.47% |    -0.1  |       26 | 17.62%     | ok               |
|          35 | -15.58%  | -65.34%            | -45.32% |    -0.12 |       44 | 25.29%     | ok               |
|          40 | -19.39%  | -65.34%            | -43.28% |    -0.23 |       40 | 21.26%     | ok               |
|          30 | -31.66%  | -65.34%            | -48.09% |    -0.43 |       62 | 28.93%     | ok               |

## ETH-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 139.05%  | -16.11%            | -30.11% |     1.19 |       62 | 45.98%     | ok               |
|          30 | 94.40%   | -16.11%            | -32.89% |     0.93 |       68 | 54.60%     | ok               |
|          20 | 52.27%   | -16.11%            | -39.10% |     0.66 |       82 | 63.79%     | ok               |
|          25 | 51.18%   | -16.11%            | -40.90% |     0.66 |       64 | 59.39%     | ok               |
|          15 | 45.14%   | -16.11%            | -42.74% |     0.61 |       77 | 69.35%     | ok               |

## EWJ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -20.29%  | 33.49%             | -30.73% |    -0.69 |       62 | 36.94%     | ok               |
|          20 | -21.64%  | 33.49%             | -31.32% |    -0.72 |       58 | 38.94%     | ok               |
|          25 | -23.90%  | 33.49%             | -31.18% |    -0.82 |       58 | 37.94%     | ok               |
|          45 | -21.05%  | 33.49%             | -27.68% |    -0.84 |       58 | 29.12%     | ok               |
|          35 | -24.11%  | 33.49%             | -32.54% |    -0.86 |       68 | 35.27%     | ok               |

## FCX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -2.83%   | 57.45%             | -26.57% |     0.09 |       56 | 30.62%     | ok               |
|          45 | -7.02%   | 57.45%             | -32.99% |     0.03 |       56 | 35.11%     | ok               |
|          40 | -19.26%  | 57.45%             | -42.49% |    -0.18 |       68 | 39.27%     | ok               |
|          30 | -29.92%  | 57.45%             | -48.22% |    -0.35 |       67 | 45.92%     | ok               |
|          35 | -34.24%  | 57.45%             | -51.41% |    -0.46 |       73 | 44.09%     | ok               |

## FET-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -22.20%  | -77.41%            | -61.59% |     0.12 |       92 | 52.68%     | ok               |
|          15 | -31.57%  | -77.41%            | -59.58% |     0.04 |       86 | 56.70%     | ok               |
|          25 | -43.39%  | -77.41%            | -60.50% |    -0.17 |       89 | 46.36%     | ok               |
|          30 | -50.78%  | -77.41%            | -52.44% |    -0.33 |       87 | 41.57%     | ok               |
|          45 | -45.96%  | -77.41%            | -48.61% |    -0.56 |       54 | 18.58%     | ok               |

## FIL-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -21.24%  | -77.79%            | -34.38% |    -0.16 |       44 | 23.37%     | ok               |
|          35 | -44.50%  | -77.79%            | -41.43% |    -0.57 |       58 | 28.16%     | ok               |
|          45 | -38.83%  | -77.79%            | -41.74% |    -0.58 |       42 | 17.82%     | ok               |
|          30 | -50.04%  | -77.79%            | -48.59% |    -0.65 |       70 | 34.29%     | ok               |
|          50 | -41.38%  | -77.79%            | -47.10% |    -0.75 |       38 | 13.03%     | ok               |

## FXI Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -0.51%   | 51.66%             | -22.57% |     0.07 |       46 | 32.11%     | ok               |
|          30 | -0.79%   | 51.66%             | -23.91% |     0.07 |       44 | 30.62%     | ok               |
|          15 | -2.11%   | 51.66%             | -21.68% |     0.04 |       50 | 35.77%     | ok               |
|          20 | -2.69%   | 51.66%             | -24.53% |     0.02 |       48 | 33.61%     | ok               |
|          35 | -5.23%   | 51.66%             | -27.53% |    -0.05 |       44 | 28.62%     | ok               |

## GDX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 11.79%   | 152.41%            | -35.59% |     0.31 |       72 | 51.25%     | ok               |
|          30 | 6.76%    | 152.41%            | -34.99% |     0.24 |       58 | 46.92%     | ok               |
|          40 | 4.82%    | 152.41%            | -31.87% |     0.2  |       64 | 41.60%     | ok               |
|          35 | 4.52%    | 152.41%            | -32.37% |     0.2  |       66 | 44.09%     | ok               |
|          25 | 1.10%    | 152.41%            | -38.90% |     0.15 |       62 | 48.09%     | ok               |

## GDXJ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -13.45%  | 169.59%            | -45.05% |    -0.02 |       66 | 51.08%     | ok               |
|          50 | -21.35%  | 169.59%            | -44.94% |    -0.25 |       58 | 37.44%     | ok               |
|          30 | -25.09%  | 169.59%            | -44.93% |    -0.26 |       64 | 45.09%     | ok               |
|          25 | -30.09%  | 169.59%            | -47.26% |    -0.32 |       69 | 47.92%     | ok               |
|          35 | -28.63%  | 169.59%            | -43.49% |    -0.34 |       66 | 42.76%     | ok               |

## GE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 18.47%   | 177.54%            | -22.29% |     0.44 |       66 | 37.77%     | ok               |
|          45 | 9.53%    | 177.54%            | -25.68% |     0.28 |       74 | 40.60%     | ok               |
|          20 | 3.00%    | 177.54%            | -26.63% |     0.18 |       75 | 55.41%     | ok               |
|          30 | -0.77%   | 177.54%            | -27.82% |     0.11 |       80 | 51.58%     | ok               |
|          15 | -3.35%   | 177.54%            | -28.62% |     0.08 |       76 | 58.07%     | ok               |

## GLD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 28.30%   | 84.01%             | -14.61% |     0.69 |       48 | 50.25%     | ok               |
|          25 | 27.62%   | 84.01%             | -14.61% |     0.68 |       48 | 48.75%     | ok               |
|          30 | 21.55%   | 84.01%             | -16.63% |     0.56 |       50 | 47.59%     | ok               |
|          15 | 20.44%   | 84.01%             | -17.54% |     0.52 |       50 | 54.41%     | ok               |
|          35 | 15.23%   | 84.01%             | -17.29% |     0.44 |       54 | 45.59%     | ok               |

## GOOGL Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 83.32%   | 171.31%            | -18.25% |     1.25 |       57 | 48.75%     | ok               |
|          30 | 78.89%   | 171.31%            | -20.41% |     1.18 |       55 | 52.25%     | ok               |
|          45 | 67.79%   | 171.31%            | -14.13% |     1.15 |       52 | 42.10%     | ok               |
|          25 | 76.17%   | 171.31%            | -19.76% |     1.14 |       53 | 54.24%     | ok               |
|          50 | 60.60%   | 171.31%            | -14.89% |     1.09 |       48 | 37.27%     | ok               |

## GRT-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 14.84%   | -87.55%            | -36.42% |     0.37 |       44 | 21.65%     | ok               |
|          15 | 10.69%   | -87.55%            | -49.67% |     0.35 |       71 | 61.69%     | ok               |
|          20 | 4.88%    | -87.55%            | -46.47% |     0.29 |       77 | 56.90%     | ok               |
|          35 | 0.25%    | -87.55%            | -43.61% |     0.21 |       66 | 37.36%     | ok               |
|          30 | -1.12%   | -87.55%            | -50.20% |     0.2  |       83 | 43.87%     | ok               |

## GS Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 23.32%   | 165.97%            | -20.56% |     0.5  |       74 | 59.73%     | ok               |
|          20 | 6.49%    | 165.97%            | -23.19% |     0.23 |       74 | 55.74%     | ok               |
|          40 | 1.75%    | 165.97%            | -17.88% |     0.13 |       70 | 44.09%     | ok               |
|          25 | 1.10%    | 165.97%            | -23.32% |     0.13 |       74 | 53.24%     | ok               |
|          30 | -0.54%   | 165.97%            | -22.13% |     0.09 |       74 | 50.75%     | ok               |

## HD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -6.05%   | -8.48%             | -17.69% |    -0.08 |       71 | 44.09%     | ok               |
|          25 | -6.79%   | -8.48%             | -18.51% |    -0.1  |       70 | 46.09%     | ok               |
|          35 | -13.78%  | -8.48%             | -22.98% |    -0.33 |       80 | 39.93%     | ok               |
|          45 | -11.66%  | -8.48%             | -21.41% |    -0.34 |       58 | 27.95%     | ok               |
|          15 | -16.44%  | -8.48%             | -27.53% |    -0.34 |      110 | 55.07%     | ok               |

## HON Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -11.43%  | 24.64%             | -21.17% |    -0.32 |       72 | 31.95%     | ok               |
|          45 | -13.21%  | 24.64%             | -19.99% |    -0.35 |       74 | 36.94%     | ok               |
|          40 | -21.75%  | 24.64%             | -26.92% |    -0.6  |       76 | 41.26%     | ok               |
|          35 | -23.25%  | 24.64%             | -27.99% |    -0.62 |       91 | 47.59%     | ok               |
|          30 | -26.35%  | 24.64%             | -29.81% |    -0.7  |       95 | 52.41%     | ok               |

## HYG Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -8.02%   | 2.48%              | -8.22%  |    -0.97 |       70 | 29.62%     | ok               |
|          25 | -9.14%   | 2.48%              | -10.07% |    -1.03 |       83 | 36.94%     | ok               |
|          30 | -8.84%   | 2.48%              | -9.55%  |    -1.03 |       81 | 34.28%     | ok               |
|          20 | -9.29%   | 2.48%              | -10.22% |    -1.04 |       84 | 38.77%     | ok               |
|          15 | -9.76%   | 2.48%              | -10.43% |    -1.06 |       88 | 40.77%     | ok               |

## IBIT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 53.73%   | -4.87%             | -17.37% |     1.05 |       22 | 21.72%     | ok               |
|          15 | 56.91%   | -4.87%             | -19.20% |     0.94 |       40 | 38.69%     | ok               |
|          45 | 44.27%   | -4.87%             | -17.37% |     0.89 |       26 | 23.08%     | ok               |
|          40 | 38.04%   | -4.87%             | -17.78% |     0.79 |       26 | 24.89%     | ok               |
|          30 | 30.82%   | -4.87%             | -18.95% |     0.65 |       34 | 31.22%     | ok               |

## IBM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -18.09%  | 18.04%             | -45.75% |    -0.12 |       91 | 63.06%     | ok               |
|          30 | -25.46%  | 18.04%             | -47.10% |    -0.31 |       75 | 50.92%     | ok               |
|          20 | -28.74%  | 18.04%             | -50.22% |    -0.34 |       73 | 55.57%     | ok               |
|          35 | -27.38%  | 18.04%             | -47.10% |    -0.36 |       69 | 46.59%     | ok               |
|          50 | -30.93%  | 18.04%             | -45.88% |    -0.48 |       52 | 34.28%     | ok               |

## ICP-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -8.14%   | -67.88%            | -34.69% |     0.1  |       52 | 24.14%     | ok               |
|          30 | -20.15%  | -67.88%            | -50.29% |     0.05 |       79 | 34.67%     | ok               |
|          35 | -14.63%  | -67.88%            | -41.66% |     0.03 |       62 | 29.12%     | ok               |
|          50 | -25.55%  | -67.88%            | -43.65% |    -0.21 |       34 | 14.56%     | ok               |
|          15 | -51.83%  | -67.88%            | -59.86% |    -0.26 |       79 | 46.93%     | ok               |

## IEF Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -7.08%   | -2.41%             | -10.10% |    -0.84 |       72 | 43.09%     | ok               |
|          15 | -7.63%   | -2.41%             | -10.83% |    -0.89 |       71 | 44.59%     | ok               |
|          25 | -10.65%  | -2.41%             | -11.63% |    -1.34 |       78 | 40.27%     | ok               |
|          45 | -8.32%   | -2.41%             | -9.73%  |    -1.36 |       56 | 23.46%     | ok               |
|          40 | -8.91%   | -2.41%             | -9.67%  |    -1.38 |       66 | 25.62%     | ok               |

## IEMG Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -3.52%   | 51.82%             | -14.40% |    -0.08 |       54 | 31.45%     | ok               |
|          35 | -4.62%   | 51.82%             | -22.13% |    -0.1  |       63 | 39.60%     | ok               |
|          45 | -4.31%   | 51.82%             | -15.40% |    -0.11 |       50 | 33.94%     | ok               |
|          40 | -5.78%   | 51.82%             | -18.89% |    -0.16 |       62 | 36.94%     | ok               |
|          25 | -8.83%   | 51.82%             | -25.58% |    -0.24 |       59 | 42.43%     | ok               |

## INJ-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -10.15%  | -61.53%            | -52.34% |     0.06 |       44 | 23.37%     | ok               |
|          35 | -21.17%  | -61.53%            | -59.17% |    -0.02 |       60 | 32.57%     | ok               |
|          40 | -26.45%  | -61.53%            | -55.86% |    -0.14 |       50 | 29.12%     | ok               |
|          50 | -22.38%  | -61.53%            | -49.35% |    -0.14 |       48 | 20.11%     | ok               |
|          20 | -55.65%  | -61.53%            | -81.16% |    -0.45 |       78 | 46.74%     | ok               |

## INTC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 106.31%  | 102.85%            | -53.65% |     0.83 |       77 | 60.07%     | ok               |
|          45 | 83.34%   | 102.85%            | -49.32% |     0.78 |       56 | 33.78%     | ok               |
|          40 | 77.32%   | 102.85%            | -55.86% |     0.74 |       64 | 38.10%     | ok               |
|          50 | 70.40%   | 102.85%            | -48.35% |     0.72 |       64 | 29.95%     | ok               |
|          25 | 65.42%   | 102.85%            | -56.41% |     0.67 |       77 | 51.08%     | ok               |

## INTU Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -1.11%   | -51.08%            | -41.23% |     0.1  |       69 | 28.29%     | ok               |
|          45 | -1.72%   | -51.08%            | -41.46% |     0.09 |       67 | 32.11%     | ok               |
|          40 | -7.39%   | -51.08%            | -44.40% |    -0.01 |       67 | 34.78%     | ok               |
|          35 | -14.47%  | -51.08%            | -46.02% |    -0.14 |       71 | 38.27%     | ok               |
|          25 | -17.76%  | -51.08%            | -39.87% |    -0.19 |       70 | 44.59%     | ok               |

## ITA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -0.73%   | 92.36%             | -21.48% |     0.04 |       76 | 36.44%     | ok               |
|          15 | -4.31%   | 92.36%             | -25.76% |    -0.02 |       87 | 58.74%     | ok               |
|          30 | -4.17%   | 92.36%             | -23.75% |    -0.05 |       72 | 46.42%     | ok               |
|          35 | -6.21%   | 92.36%             | -23.16% |    -0.12 |       76 | 44.76%     | ok               |
|          40 | -7.29%   | 92.36%             | -20.58% |    -0.16 |       78 | 41.26%     | ok               |

## IWM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 8.60%    | 44.36%             | -14.08% |     0.39 |       42 | 31.28%     | ok               |
|          30 | 9.40%    | 44.36%             | -12.83% |     0.39 |       48 | 35.77%     | ok               |
|          25 | 9.50%    | 44.36%             | -13.55% |     0.39 |       50 | 36.94%     | ok               |
|          35 | 8.35%    | 44.36%             | -14.11% |     0.36 |       48 | 33.61%     | ok               |
|          20 | 5.19%    | 44.36%             | -14.08% |     0.24 |       60 | 37.94%     | ok               |

## JNJ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 19.99%   | 57.79%             | -10.57% |     0.81 |       54 | 37.10%     | ok               |
|          15 | 16.30%   | 57.79%             | -18.02% |     0.55 |       66 | 57.40%     | ok               |
|          45 | 11.43%   | 57.79%             | -13.35% |     0.48 |       54 | 41.93%     | ok               |
|          20 | 10.93%   | 57.79%             | -17.61% |     0.41 |       72 | 53.91%     | ok               |
|          40 | 6.37%    | 57.79%             | -14.77% |     0.29 |       60 | 46.09%     | ok               |

## JPM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 11.00%   | 87.29%             | -15.90% |     0.41 |       54 | 38.77%     | ok               |
|          45 | 0.45%    | 87.29%             | -21.91% |     0.08 |       56 | 41.76%     | ok               |
|          20 | -16.14%  | 87.29%             | -33.59% |    -0.29 |       86 | 56.74%     | ok               |
|          40 | -13.34%  | 87.29%             | -28.47% |    -0.32 |       68 | 44.43%     | ok               |
|          35 | -18.45%  | 87.29%             | -27.43% |    -0.46 |       76 | 48.42%     | ok               |

## KO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 23.75%   | 44.19%             | -8.20%  |     0.85 |       51 | 37.94%     | ok               |
|          35 | 19.96%   | 44.19%             | -8.07%  |     0.75 |       54 | 36.61%     | ok               |
|          40 | 17.46%   | 44.19%             | -9.28%  |     0.71 |       56 | 33.44%     | ok               |
|          25 | 18.64%   | 44.19%             | -9.73%  |     0.69 |       57 | 40.60%     | ok               |
|          50 | 10.20%   | 44.19%             | -12.31% |     0.48 |       38 | 26.96%     | ok               |

## LDO-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 53.82%   | -73.76%            | -48.17% |     0.64 |       82 | 57.28%     | ok               |
|          50 | 33.03%   | -73.76%            | -48.04% |     0.57 |       52 | 18.20%     | ok               |
|          35 | 34.90%   | -73.76%            | -61.98% |     0.54 |       78 | 36.02%     | ok               |
|          30 | 34.87%   | -73.76%            | -61.16% |     0.54 |       78 | 43.10%     | ok               |
|          20 | 33.73%   | -73.76%            | -45.55% |     0.53 |       84 | 52.11%     | ok               |

## LIN Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -5.41%   | 2.34%              | -23.70% |    -0.12 |       63 | 47.75%     | ok               |
|          25 | -5.64%   | 2.34%              | -22.01% |    -0.14 |       63 | 39.93%     | ok               |
|          20 | -7.66%   | 2.34%              | -23.00% |    -0.21 |       62 | 43.09%     | ok               |
|          30 | -9.62%   | 2.34%              | -21.53% |    -0.3  |       66 | 37.10%     | ok               |
|          35 | -9.05%   | 2.34%              | -21.18% |    -0.3  |       62 | 30.62%     | ok               |

## LINK-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -17.80%  | -44.63%            | -39.15% |     0.05 |       73 | 43.68%     | ok               |
|          45 | -15.04%  | -44.63%            | -33.71% |     0.03 |       50 | 28.54%     | ok               |
|          50 | -19.20%  | -44.63%            | -30.38% |    -0.06 |       44 | 22.61%     | ok               |
|          35 | -27.04%  | -44.63%            | -38.95% |    -0.08 |       61 | 38.51%     | ok               |
|          40 | -31.05%  | -44.63%            | -40.59% |    -0.18 |       57 | 32.76%     | ok               |

## LLY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 6.14%    | 52.70%             | -38.23% |     0.23 |       44 | 34.94%     | ok               |
|          15 | 0.30%    | 52.70%             | -48.12% |     0.15 |       63 | 58.24%     | ok               |
|          45 | -5.81%   | 52.70%             | -42.66% |     0    |       52 | 38.44%     | ok               |
|          20 | -15.80%  | 52.70%             | -51.34% |    -0.14 |       70 | 53.24%     | ok               |
|          25 | -17.19%  | 52.70%             | -53.47% |    -0.17 |       66 | 50.58%     | ok               |

## LRCX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -15.92%  | 216.38%            | -48.71% |    -0.05 |       78 | 33.78%     | ok               |
|          35 | -18.96%  | 216.38%            | -57.54% |    -0.06 |       78 | 41.60%     | ok               |
|          40 | -19.18%  | 216.38%            | -55.33% |    -0.07 |       72 | 39.60%     | ok               |
|          15 | -24.91%  | 216.38%            | -58.63% |    -0.09 |       85 | 52.58%     | ok               |
|          30 | -22.68%  | 216.38%            | -60.21% |    -0.12 |       82 | 42.43%     | ok               |

## LTC-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -5.83%   | -64.41%            | -35.63% |     0.08 |       54 | 31.80%     | ok               |
|          35 | -18.05%  | -64.41%            | -46.78% |    -0.07 |       68 | 42.91%     | ok               |
|          30 | -27.94%  | -64.41%            | -47.04% |    -0.2  |       72 | 49.81%     | ok               |
|          40 | -27.55%  | -64.41%            | -48.25% |    -0.25 |       58 | 37.93%     | ok               |
|          25 | -31.35%  | -64.41%            | -47.60% |    -0.25 |       76 | 52.68%     | ok               |

## MCD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 3.90%    | -10.04%            | -9.22%  |     0.24 |       42 | 20.63%     | ok               |
|          30 | -3.77%   | -10.04%            | -18.81% |    -0.1  |       77 | 38.27%     | ok               |
|          25 | -4.80%   | -10.04%            | -20.47% |    -0.13 |       77 | 40.93%     | ok               |
|          40 | -6.63%   | -10.04%            | -16.86% |    -0.26 |       69 | 28.95%     | ok               |
|          35 | -8.84%   | -10.04%            | -15.45% |    -0.34 |       69 | 34.61%     | ok               |

## META Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -17.15%  | 22.05%             | -34.72% |    -0.25 |       70 | 36.77%     | ok               |
|          40 | -25.44%  | 22.05%             | -38.23% |    -0.43 |       70 | 39.93%     | ok               |
|          25 | -32.80%  | 22.05%             | -43.26% |    -0.55 |       71 | 50.58%     | ok               |
|          50 | -29.54%  | 22.05%             | -37.29% |    -0.59 |       70 | 33.11%     | ok               |
|          30 | -34.60%  | 22.05%             | -42.43% |    -0.62 |       76 | 47.42%     | ok               |

## MPC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 23.63%   | 69.25%             | -23.96% |     0.52 |       48 | 38.44%     | ok               |
|          45 | 15.79%   | 69.25%             | -25.09% |     0.39 |       54 | 42.10%     | ok               |
|          40 | 11.41%   | 69.25%             | -25.70% |     0.31 |       56 | 44.26%     | ok               |
|          35 | 7.97%    | 69.25%             | -35.90% |     0.25 |       64 | 46.76%     | ok               |
|          30 | -9.01%   | 69.25%             | -44.76% |    -0.04 |       67 | 49.58%     | ok               |

## MRK Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -17.73%  | 4.07%              | -30.12% |    -0.3  |       87 | 54.24%     | ok               |
|          25 | -16.71%  | 4.07%              | -31.07% |    -0.31 |       72 | 46.42%     | ok               |
|          20 | -20.79%  | 4.07%              | -29.59% |    -0.41 |       77 | 49.75%     | ok               |
|          50 | -21.52%  | 4.07%              | -27.68% |    -0.6  |       58 | 29.12%     | ok               |
|          45 | -23.47%  | 4.07%              | -27.72% |    -0.62 |       59 | 32.45%     | ok               |

## MS Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -3.32%   | 142.96%            | -19.99% |     0    |       72 | 41.43%     | ok               |
|          15 | -4.98%   | 142.96%            | -22.02% |    -0.01 |       73 | 58.24%     | ok               |
|          20 | -5.09%   | 142.96%            | -25.68% |    -0.02 |       77 | 54.41%     | ok               |
|          30 | -10.18%  | 142.96%            | -27.79% |    -0.16 |       77 | 49.58%     | ok               |
|          35 | -10.11%  | 142.96%            | -25.26% |    -0.17 |       78 | 46.09%     | ok               |

## MSFT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -16.75%  | 20.55%             | -24.64% |    -0.42 |       66 | 33.78%     | ok               |
|          50 | -18.78%  | 20.55%             | -25.48% |    -0.51 |       60 | 28.95%     | ok               |
|          35 | -30.53%  | 20.55%             | -35.38% |    -0.77 |       73 | 42.60%     | ok               |
|          40 | -29.87%  | 20.55%             | -34.77% |    -0.78 |       69 | 37.44%     | ok               |
|          30 | -34.59%  | 20.55%             | -39.15% |    -0.87 |       83 | 47.25%     | ok               |

## MU Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 327.26%  | 777.68%            | -61.96% |     1.36 |       51 | 66.56%     | ok               |
|          40 | 267.94%  | 777.68%            | -64.26% |     1.35 |       56 | 53.24%     | ok               |
|          25 | 238.98%  | 777.68%            | -67.90% |     1.25 |       51 | 59.90%     | ok               |
|          30 | 225.56%  | 777.68%            | -68.76% |     1.23 |       51 | 58.24%     | ok               |
|          35 | 216.39%  | 777.68%            | -69.35% |     1.22 |       63 | 55.91%     | ok               |

## NEAR-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 58.08%   | -46.37%            | -49.73% |     0.73 |       40 | 22.22%     | ok               |
|          40 | 42.37%   | -46.37%            | -57.80% |     0.61 |       40 | 26.05%     | ok               |
|          50 | 38.01%   | -46.37%            | -52.97% |     0.58 |       34 | 17.82%     | ok               |
|          35 | 15.61%   | -46.37%            | -61.61% |     0.38 |       64 | 30.84%     | ok               |
|          30 | -5.33%   | -46.37%            | -59.54% |     0.2  |       83 | 40.23%     | ok               |

## NEM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 16.36%   | 170.63%            | -29.41% |     0.36 |       60 | 60.90%     | ok               |
|          20 | 3.91%    | 170.63%            | -30.47% |     0.22 |       70 | 56.41%     | ok               |
|          25 | -9.17%   | 170.63%            | -37.89% |     0.04 |       66 | 54.41%     | ok               |
|          30 | -20.55%  | 170.63%            | -38.49% |    -0.15 |       70 | 52.75%     | ok               |
|          50 | -19.27%  | 170.63%            | -33.24% |    -0.19 |       56 | 39.77%     | ok               |

## NFLX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 41.25%   | 22.03%             | -13.37% |     0.9  |       50 | 44.59%     | ok               |
|          50 | 36.96%   | 22.03%             | -16.28% |     0.88 |       48 | 36.61%     | ok               |
|          35 | 37.24%   | 22.03%             | -18.30% |     0.79 |       66 | 48.59%     | ok               |
|          45 | 27.27%   | 22.03%             | -15.48% |     0.66 |       56 | 40.93%     | ok               |
|          15 | 30.33%   | 22.03%             | -26.59% |     0.61 |       69 | 64.39%     | ok               |

## NKE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -29.60%  | -57.82%            | -49.34% |    -0.34 |       87 | 51.25%     | ok               |
|          35 | -26.85%  | -57.82%            | -42.13% |    -0.37 |       73 | 37.60%     | ok               |
|          25 | -32.52%  | -57.82%            | -51.20% |    -0.4  |       87 | 48.59%     | ok               |
|          15 | -34.15%  | -57.82%            | -54.28% |    -0.42 |       90 | 55.07%     | ok               |
|          30 | -36.83%  | -57.82%            | -55.35% |    -0.51 |       85 | 44.09%     | ok               |

## NOW Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 1.54%    | -24.55%            | -26.78% |     0.18 |       80 | 45.76%     | ok               |
|          20 | -0.50%   | -24.55%            | -34.71% |     0.17 |       79 | 52.08%     | ok               |
|          25 | -4.29%   | -24.55%            | -32.31% |     0.12 |       74 | 49.08%     | ok               |
|          15 | -9.19%   | -24.55%            | -38.33% |     0.06 |       89 | 55.24%     | ok               |
|          40 | -6.73%   | -24.55%            | -30.91% |     0.04 |       70 | 35.11%     | ok               |

## NVDA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -14.80%  | 128.20%            | -35.26% |    -0.08 |       76 | 47.77%     | ok               |
|          20 | -19.76%  | 128.20%            | -40.59% |    -0.1  |       72 | 55.79%     | ok               |
|          25 | -19.63%  | 128.20%            | -37.16% |    -0.13 |       73 | 50.80%     | ok               |
|          15 | -28.45%  | 128.20%            | -45.14% |    -0.22 |       73 | 59.00%     | ok               |
|          35 | -26.31%  | 128.20%            | -42.39% |    -0.3  |       84 | 44.92%     | ok               |

## OP-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 21.31%   | -91.47%            | -36.11% |     0.44 |       32 | 11.30%     | ok               |
|          45 | 20.44%   | -91.47%            | -45.76% |     0.42 |       34 | 15.90%     | ok               |
|          40 | 9.34%    | -91.47%            | -53.61% |     0.31 |       46 | 24.14%     | ok               |
|          30 | -16.82%  | -91.47%            | -71.26% |     0.06 |       66 | 35.06%     | ok               |
|          35 | -13.04%  | -91.47%            | -59.71% |     0.06 |       52 | 28.54%     | ok               |

## ORCL Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 208.15%  | 24.29%             | -29.32% |     1.25 |       64 | 66.56%     | ok               |
|          25 | 130.17%  | 24.29%             | -27.76% |     1    |       67 | 59.23%     | ok               |
|          20 | 127.19%  | 24.29%             | -29.32% |     0.98 |       67 | 62.23%     | ok               |
|          45 | 110.15%  | 24.29%             | -32.35% |     0.97 |       60 | 42.76%     | ok               |
|          35 | 118.31%  | 24.29%             | -31.95% |     0.97 |       62 | 51.41%     | ok               |

## OXY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 4.09%    | -9.83%             | -31.61% |     0.19 |       71 | 46.26%     | ok               |
|          35 | 2.55%    | -9.83%             | -30.16% |     0.16 |       70 | 40.93%     | ok               |
|          50 | 1.70%    | -9.83%             | -29.57% |     0.14 |       40 | 29.28%     | ok               |
|          40 | -3.48%   | -9.83%             | -31.66% |     0.05 |       58 | 36.61%     | ok               |
|          25 | -10.24%  | -9.83%             | -41.03% |    -0.05 |       79 | 50.42%     | ok               |

## PEP Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 13.88%   | -15.24%            | -11.62% |     0.62 |       44 | 27.62%     | ok               |
|          45 | 5.65%    | -15.24%            | -14.22% |     0.28 |       62 | 31.95%     | ok               |
|          40 | 1.57%    | -15.24%            | -18.04% |     0.11 |       70 | 37.44%     | ok               |
|          35 | 0.42%    | -15.24%            | -21.42% |     0.08 |       77 | 42.10%     | ok               |
|          30 | -5.12%   | -15.24%            | -21.35% |    -0.08 |       77 | 48.42%     | ok               |

## PEPE-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -8.77%   | -61.18%            | -57.66% |     0.2  |       81 | 45.98%     | ok               |
|          15 | -17.71%  | -61.18%            | -61.96% |     0.19 |       78 | 61.88%     | ok               |
|          35 | -11.24%  | -61.18%            | -49.27% |     0.14 |       68 | 40.04%     | ok               |
|          25 | -17.94%  | -61.18%            | -53.88% |     0.12 |       87 | 51.53%     | ok               |
|          20 | -25.81%  | -61.18%            | -61.13% |     0.07 |       84 | 58.43%     | ok               |

## PFE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -24.41%  | -11.77%            | -25.61% |    -0.92 |       52 | 19.13%     | ok               |
|          50 | -26.23%  | -11.77%            | -27.28% |    -1.12 |       38 | 15.31%     | ok               |
|          40 | -31.46%  | -11.77%            | -32.57% |    -1.14 |       74 | 24.13%     | ok               |
|          35 | -35.73%  | -11.77%            | -36.64% |    -1.2  |       86 | 32.11%     | ok               |
|          30 | -41.91%  | -11.77%            | -42.74% |    -1.36 |       79 | 36.61%     | ok               |

## PG Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -8.73%   | -10.26%            | -19.77% |    -0.32 |       56 | 31.28%     | ok               |
|          35 | -11.85%  | -10.26%            | -18.66% |    -0.44 |       64 | 34.78%     | ok               |
|          30 | -19.86%  | -10.26%            | -24.25% |    -0.76 |       66 | 37.94%     | ok               |
|          45 | -17.65%  | -10.26%            | -22.13% |    -0.78 |       56 | 28.79%     | ok               |
|          25 | -21.68%  | -10.26%            | -25.94% |    -0.84 |       78 | 39.43%     | ok               |

## PM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | -3.77%   | 98.51%             | -32.95% |     0.01 |       88 | 52.25%     | ok               |
|          20 | -6.38%   | 98.51%             | -33.12% |    -0.04 |       87 | 60.73%     | ok               |
|          30 | -6.79%   | 98.51%             | -34.79% |    -0.06 |       83 | 55.74%     | ok               |
|          50 | -9.20%   | 98.51%             | -35.70% |    -0.15 |       76 | 42.43%     | ok               |
|          40 | -10.55%  | 98.51%             | -37.94% |    -0.17 |       82 | 48.59%     | ok               |

## POL-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 52.97%   | -74.14%            | -41.08% |     0.7  |       81 | 49.43%     | ok               |
|          25 | 34.19%   | -74.14%            | -46.72% |     0.54 |       66 | 57.47%     | ok               |
|          20 | 23.28%   | -74.14%            | -52.88% |     0.45 |       72 | 61.88%     | ok               |
|          15 | 6.51%    | -74.14%            | -58.42% |     0.31 |       74 | 66.48%     | ok               |
|          40 | 0.42%    | -74.14%            | -38.75% |     0.17 |       54 | 30.27%     | ok               |

## QCOM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -2.57%   | -11.42%            | -54.83% |     0.14 |       75 | 47.42%     | ok               |
|          20 | -6.53%   | -11.42%            | -54.71% |     0.09 |       71 | 50.25%     | ok               |
|          35 | -8.63%   | -11.42%            | -50.58% |     0.05 |       81 | 43.09%     | ok               |
|          30 | -18.98%  | -11.42%            | -56.59% |    -0.1  |       77 | 45.59%     | ok               |
|          15 | -22.06%  | -11.42%            | -58.24% |    -0.12 |       75 | 53.41%     | ok               |

## QQQ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 20.33%   | 60.06%             | -12.88% |     0.58 |       60 | 43.59%     | ok               |
|          25 | 20.78%   | 60.06%             | -12.88% |     0.58 |       57 | 46.26%     | ok               |
|          15 | 22.51%   | 60.06%             | -14.17% |     0.57 |       63 | 52.58%     | ok               |
|          20 | 17.86%   | 60.06%             | -12.98% |     0.5  |       65 | 48.92%     | ok               |
|          35 | 8.03%    | 60.06%             | -18.29% |     0.29 |       66 | 39.93%     | ok               |

## RENDER-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 38.90%   | -64.32%            | -43.43% |     0.57 |       92 | 53.26%     | ok               |
|          15 | 31.34%   | -64.32%            | -44.59% |     0.52 |       92 | 56.70%     | ok               |
|          25 | 12.01%   | -64.32%            | -40.60% |     0.39 |       92 | 48.47%     | ok               |
|          30 | -21.49%  | -64.32%            | -43.50% |     0.06 |      100 | 42.15%     | ok               |
|          40 | -25.08%  | -64.32%            | -38.60% |    -0.06 |       76 | 27.39%     | ok               |

## RTX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 48.53%   | 137.04%            | -18.66% |     0.99 |       72 | 57.40%     | ok               |
|          35 | 38.21%   | 137.04%            | -18.00% |     0.92 |       50 | 51.58%     | ok               |
|          25 | 43.45%   | 137.04%            | -18.59% |     0.91 |       60 | 54.74%     | ok               |
|          30 | 41.27%   | 137.04%            | -16.99% |     0.89 |       54 | 53.58%     | ok               |
|          15 | 40.07%   | 137.04%            | -19.55% |     0.84 |       67 | 62.06%     | ok               |

## SBUX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -9.63%   | 12.27%             | -23.55% |    -0.11 |       59 | 42.10%     | ok               |
|          45 | -12.59%  | 12.27%             | -27.26% |    -0.25 |       68 | 30.45%     | ok               |
|          40 | -15.23%  | 12.27%             | -25.43% |    -0.29 |       64 | 34.11%     | ok               |
|          30 | -19.04%  | 12.27%             | -29.22% |    -0.35 |       62 | 39.93%     | ok               |
|          50 | -16.60%  | 12.27%             | -25.77% |    -0.39 |       56 | 26.12%     | ok               |

## SCHW Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 8.17%    | 58.13%             | -16.53% |     0.3  |       60 | 35.44%     | ok               |
|          25 | 4.70%    | 58.13%             | -28.76% |     0.2  |       63 | 51.25%     | ok               |
|          50 | 2.97%    | 58.13%             | -13.28% |     0.16 |       52 | 32.45%     | ok               |
|          20 | 0.94%    | 58.13%             | -29.24% |     0.12 |       71 | 53.74%     | ok               |
|          40 | -2.21%   | 58.13%             | -23.35% |     0.02 |       66 | 38.60%     | ok               |

## SHIB-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -20.51%  | -63.29%            | -50.97% |    -0.01 |       80 | 67.05%     | ok               |
|          25 | -19.53%  | -63.29%            | -45.80% |    -0.01 |       75 | 59.20%     | ok               |
|          20 | -24.38%  | -63.29%            | -48.24% |    -0.07 |       77 | 63.03%     | ok               |
|          35 | -23.29%  | -63.29%            | -52.76% |    -0.11 |       66 | 46.55%     | ok               |
|          40 | -27.05%  | -63.29%            | -49.11% |    -0.2  |       56 | 39.08%     | ok               |

## SHY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd    |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:-------|---------:|---------:|:-----------|:-----------------|
|          30 | -2.23%   | 0.05%              | -2.85% |    -0.78 |       46 | 34.11%     | ok               |
|          35 | -2.34%   | 0.05%              | -3.27% |    -0.83 |       48 | 32.28%     | ok               |
|          40 | -2.46%   | 0.05%              | -3.33% |    -0.89 |       48 | 30.45%     | ok               |
|          45 | -2.44%   | 0.05%              | -3.23% |    -0.9  |       46 | 27.29%     | ok               |
|          50 | -2.61%   | 0.05%              | -3.40% |    -1.01 |       42 | 24.46%     | ok               |

## SKY-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -35.76%  | -3.10%             | -56.39% |    -0.38 |       65 | 52.01%     | ok               |
|          30 | -32.19%  | -3.10%             | -47.82% |    -0.4  |       76 | 42.28%     | ok               |
|          25 | -35.09%  | -3.10%             | -50.05% |    -0.44 |       70 | 45.88%     | ok               |
|          20 | -44.98%  | -3.10%             | -59.15% |    -0.61 |       67 | 49.26%     | ok               |
|          35 | -38.43%  | -3.10%             | -49.68% |    -0.62 |       70 | 34.88%     | ok               |

## SLB Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 15.85%   | -4.31%             | -21.46% |     0.42 |       54 | 33.78%     | ok               |
|          40 | 12.27%   | -4.31%             | -25.33% |     0.34 |       48 | 37.27%     | ok               |
|          50 | -5.47%   | -4.31%             | -29.66% |    -0.05 |       52 | 28.95%     | ok               |
|          35 | -17.55%  | -4.31%             | -43.52% |    -0.27 |       76 | 44.59%     | ok               |
|          30 | -30.27%  | -4.31%             | -54.23% |    -0.55 |       77 | 51.08%     | ok               |

## SLV Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 66.63%   | 134.72%            | -34.10% |     0.85 |       52 | 34.44%     | ok               |
|          45 | 64.61%   | 134.72%            | -31.82% |     0.83 |       58 | 35.61%     | ok               |
|          40 | 62.64%   | 134.72%            | -31.93% |     0.81 |       64 | 37.77%     | ok               |
|          35 | 48.77%   | 134.72%            | -36.89% |     0.69 |       72 | 40.60%     | ok               |
|          20 | 50.71%   | 134.72%            | -42.66% |     0.69 |       66 | 48.09%     | ok               |

## SMH Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 89.12%   | 146.84%            | -31.01% |     1.15 |       49 | 48.75%     | ok               |
|          35 | 71.31%   | 146.84%            | -34.36% |     1.03 |       54 | 44.43%     | ok               |
|          25 | 71.19%   | 146.84%            | -32.94% |     1.01 |       46 | 47.42%     | ok               |
|          30 | 69.17%   | 146.84%            | -33.99% |     1    |       48 | 45.76%     | ok               |
|          45 | 56.86%   | 146.84%            | -32.75% |     0.94 |       52 | 38.60%     | ok               |

## SNX-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 4.86%    | -75.67%            | -30.08% |     0.28 |       62 | 29.69%     | ok               |
|          20 | -11.72%  | -75.67%            | -43.20% |     0.16 |       73 | 48.28%     | ok               |
|          40 | -4.49%   | -75.67%            | -28.61% |     0.14 |       48 | 23.95%     | ok               |
|          30 | -19.30%  | -75.67%            | -38.09% |     0.03 |       64 | 37.55%     | ok               |
|          45 | -13.81%  | -75.67%            | -42.91% |    -0.05 |       42 | 19.16%     | ok               |

## SOL-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -8.96%   | -48.87%            | -39.68% |     0.13 |       60 | 36.02%     | ok               |
|          35 | -34.01%  | -48.87%            | -48.34% |    -0.17 |       74 | 43.49%     | ok               |
|          25 | -38.81%  | -48.87%            | -41.09% |    -0.22 |       78 | 56.90%     | ok               |
|          45 | -34.89%  | -48.87%            | -48.75% |    -0.27 |       60 | 30.65%     | ok               |
|          15 | -46.10%  | -48.87%            | -49.65% |    -0.31 |       83 | 63.03%     | ok               |

## SOXX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | 74.68%   | 125.54%            | -39.85% |     0.99 |       51 | 46.92%     | ok               |
|          35 | 69.79%   | 125.54%            | -38.63% |     0.97 |       59 | 42.26%     | ok               |
|          30 | 64.86%   | 125.54%            | -40.34% |     0.91 |       55 | 44.76%     | ok               |
|          20 | 62.02%   | 125.54%            | -38.67% |     0.86 |       57 | 47.59%     | ok               |
|          15 | 60.52%   | 125.54%            | -37.72% |     0.82 |       72 | 50.92%     | ok               |

## SPY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 13.36%   | 48.19%             | -14.25% |     0.48 |       59 | 53.08%     | ok               |
|          15 | 11.81%   | 48.19%             | -16.80% |     0.43 |       68 | 56.24%     | ok               |
|          25 | 6.31%    | 48.19%             | -15.22% |     0.27 |       59 | 52.08%     | ok               |
|          30 | 1.82%    | 48.19%             | -16.47% |     0.12 |       62 | 49.25%     | ok               |
|          35 | 1.21%    | 48.19%             | -16.72% |     0.1  |       58 | 46.26%     | ok               |

## SUSHI-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -28.52%  | -80.29%            | -40.08% |    -0.27 |       54 | 14.94%     | ok               |
|          40 | -64.04%  | -80.29%            | -70.25% |    -0.83 |       65 | 24.90%     | ok               |
|          45 | -61.31%  | -80.29%            | -65.82% |    -0.84 |       58 | 18.39%     | ok               |
|          15 | -79.38%  | -80.29%            | -81.89% |    -0.99 |       93 | 49.04%     | ok               |
|          35 | -75.94%  | -80.29%            | -81.46% |    -1.1  |       86 | 31.03%     | ok               |

## T Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 55.12%   | 36.12%             | -18.13% |     1.07 |       62 | 58.57%     | ok               |
|          25 | 50.92%   | 36.12%             | -17.66% |     1.02 |       62 | 56.24%     | ok               |
|          15 | 53.13%   | 36.12%             | -15.08% |     1.01 |       71 | 62.73%     | ok               |
|          30 | 34.39%   | 36.12%             | -17.01% |     0.77 |       66 | 54.24%     | ok               |
|          35 | 18.59%   | 36.12%             | -14.49% |     0.5  |       68 | 50.42%     | ok               |

## TGT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -19.64%  | -11.14%            | -44.02% |    -0.33 |       86 | 44.76%     | ok               |
|          25 | -19.19%  | -11.14%            | -43.64% |    -0.37 |       68 | 39.93%     | ok               |
|          30 | -18.21%  | -11.14%            | -40.57% |    -0.37 |       62 | 37.27%     | ok               |
|          15 | -24.77%  | -11.14%            | -42.01% |    -0.43 |       78 | 49.42%     | ok               |
|          45 | -19.71%  | -11.14%            | -31.75% |    -0.48 |       58 | 27.62%     | ok               |

## TIA-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 3.06%    | -91.91%            | -53.37% |     0.26 |       66 | 32.95%     | ok               |
|          40 | -4.77%   | -91.91%            | -48.24% |     0.16 |       68 | 27.59%     | ok               |
|          45 | -2.76%   | -91.91%            | -49.52% |     0.16 |       56 | 19.73%     | ok               |
|          50 | -0.89%   | -91.91%            | -48.70% |     0.14 |       36 | 12.45%     | ok               |
|          15 | -34.92%  | -91.91%            | -63.05% |    -0.03 |       94 | 54.79%     | ok               |

## TLT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -19.34%  | -14.10%            | -21.87% |    -1.43 |       72 | 33.94%     | ok               |
|          40 | -17.49%  | -14.10%            | -19.02% |    -1.59 |       58 | 23.46%     | ok               |
|          50 | -14.40%  | -14.10%            | -15.05% |    -1.67 |       36 | 15.64%     | ok               |
|          35 | -20.13%  | -14.10%            | -21.63% |    -1.69 |       66 | 28.12%     | ok               |
|          15 | -25.25%  | -14.10%            | -27.76% |    -1.72 |       77 | 41.93%     | ok               |

## TMO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 41.53%   | -4.24%             | -8.17%  |     0.95 |       44 | 32.95%     | ok               |
|          45 | 35.39%   | -4.24%             | -9.80%  |     0.8  |       48 | 37.94%     | ok               |
|          40 | 34.15%   | -4.24%             | -9.81%  |     0.76 |       51 | 42.60%     | ok               |
|          35 | 27.35%   | -4.24%             | -13.84% |     0.61 |       61 | 47.25%     | ok               |
|          30 | 25.67%   | -4.24%             | -18.85% |     0.56 |       61 | 52.58%     | ok               |

## TMUS Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 5.48%    | 7.48%              | -30.05% |     0.21 |       63 | 58.57%     | ok               |
|          30 | 4.31%    | 7.48%              | -25.71% |     0.19 |       68 | 46.59%     | ok               |
|          20 | -0.60%   | 7.48%              | -29.75% |     0.09 |       69 | 52.91%     | ok               |
|          25 | -3.94%   | 7.48%              | -31.45% |     0.01 |       73 | 49.08%     | ok               |
|          35 | -7.65%   | 7.48%              | -34.23% |    -0.08 |       68 | 43.43%     | ok               |

## TRX-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 13.95%   | 40.56%             | -18.79% |     0.48 |       54 | 36.40%     | ok               |
|          30 | 10.65%   | 40.56%             | -22.90% |     0.37 |       70 | 48.47%     | ok               |
|          35 | 8.99%    | 40.56%             | -21.77% |     0.33 |       68 | 45.02%     | ok               |
|          20 | 9.27%    | 40.56%             | -25.45% |     0.32 |       63 | 55.36%     | ok               |
|          25 | 8.59%    | 40.56%             | -26.84% |     0.31 |       66 | 51.72%     | ok               |

## TSLA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 49.33%   | 81.18%             | -32.60% |     0.67 |       66 | 30.62%     | ok               |
|          40 | 27.17%   | 81.18%             | -45.90% |     0.46 |       67 | 35.61%     | ok               |
|          45 | 7.74%    | 81.18%             | -46.86% |     0.27 |       71 | 32.95%     | ok               |
|          35 | -9.21%   | 81.18%             | -54.51% |     0.1  |       78 | 38.44%     | ok               |
|          30 | -24.87%  | 81.18%             | -57.89% |    -0.08 |       74 | 42.43%     | ok               |

## TXN Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 9.77%    | 54.45%             | -45.45% |     0.28 |       64 | 33.44%     | ok               |
|          20 | -5.00%   | 54.45%             | -38.49% |     0.08 |       62 | 57.24%     | ok               |
|          15 | -7.22%   | 54.45%             | -38.99% |     0.06 |       67 | 61.40%     | ok               |
|          35 | -4.93%   | 54.45%             | -43.28% |     0.06 |       74 | 47.59%     | ok               |
|          40 | -7.51%   | 54.45%             | -45.67% |     0.01 |       70 | 45.26%     | ok               |

## UNH Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 29.80%   | -15.09%            | -26.96% |     0.52 |       74 | 52.25%     | ok               |
|          50 | 26.51%   | -15.09%            | -37.02% |     0.5  |       56 | 30.62%     | ok               |
|          35 | 27.11%   | -15.09%            | -28.32% |     0.49 |       66 | 46.92%     | ok               |
|          15 | 26.26%   | -15.09%            | -33.62% |     0.47 |       73 | 67.22%     | ok               |
|          25 | 15.49%   | -15.09%            | -29.39% |     0.35 |       74 | 57.57%     | ok               |

## UNI-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -23.72%  | -48.31%            | -63.24% |    -0.04 |       60 | 34.48%     | ok               |
|          45 | -28.98%  | -48.31%            | -57.91% |    -0.14 |       62 | 29.50%     | ok               |
|          35 | -40.80%  | -48.31%            | -68.27% |    -0.24 |       74 | 40.42%     | ok               |
|          50 | -36.35%  | -48.31%            | -53.71% |    -0.3  |       58 | 22.99%     | ok               |
|          30 | -73.84%  | -48.31%            | -80.33% |    -0.89 |       90 | 46.17%     | ok               |

## UPS Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -39.49%  | -30.94%            | -43.07% |    -0.76 |       86 | 48.59%     | ok               |
|          25 | -39.67%  | -30.94%            | -40.66% |    -0.78 |       80 | 45.09%     | ok               |
|          35 | -38.80%  | -30.94%            | -40.10% |    -0.8  |       67 | 34.44%     | ok               |
|          15 | -41.63%  | -30.94%            | -43.86% |    -0.8  |       88 | 52.41%     | ok               |
|          40 | -40.83%  | -30.94%            | -41.14% |    -0.88 |       59 | 29.78%     | ok               |

## USO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 19.25%   | 65.88%             | -44.92% |     0.4  |       75 | 40.60%     | ok               |
|          15 | 13.62%   | 65.88%             | -45.09% |     0.33 |       74 | 43.76%     | ok               |
|          45 | 11.92%   | 65.88%             | -33.25% |     0.31 |       50 | 27.45%     | ok               |
|          25 | 8.60%    | 65.88%             | -44.86% |     0.26 |       69 | 37.94%     | ok               |
|          30 | 3.91%    | 65.88%             | -43.35% |     0.19 |       70 | 34.78%     | ok               |

## VEA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 4.46%    | 42.88%             | -16.28% |     0.22 |       58 | 49.42%     | ok               |
|          20 | 0.25%    | 42.88%             | -17.70% |     0.06 |       59 | 46.76%     | ok               |
|          25 | -3.31%   | 42.88%             | -19.11% |    -0.08 |       57 | 44.76%     | ok               |
|          30 | -3.47%   | 42.88%             | -19.24% |    -0.09 |       58 | 42.60%     | ok               |
|          35 | -4.54%   | 42.88%             | -18.12% |    -0.14 |       56 | 41.60%     | ok               |

## VIXY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -48.04%  | -64.32%            | -69.78% |    -0.43 |       46 | 10.48%     | ok               |
|          45 | -57.65%  | -64.32%            | -75.03% |    -0.58 |       58 | 16.47%     | ok               |
|          40 | -65.68%  | -64.32%            | -80.72% |    -0.69 |       72 | 20.80%     | ok               |
|          35 | -69.28%  | -64.32%            | -84.37% |    -0.72 |       88 | 25.96%     | ok               |
|          15 | -76.29%  | -64.32%            | -89.47% |    -0.75 |       99 | 43.43%     | ok               |

## VNQ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -11.52%  | 13.47%             | -20.96% |    -0.51 |       58 | 29.12%     | ok               |
|          25 | -13.54%  | 13.47%             | -22.16% |    -0.53 |       66 | 40.93%     | ok               |
|          50 | -11.94%  | 13.47%             | -19.06% |    -0.55 |       54 | 26.62%     | ok               |
|          20 | -15.12%  | 13.47%             | -23.61% |    -0.58 |       69 | 43.59%     | ok               |
|          15 | -16.41%  | 13.47%             | -24.73% |    -0.63 |       66 | 44.76%     | ok               |

## VTI Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 16.22%   | 47.17%             | -13.96% |     0.56 |       62 | 53.58%     | ok               |
|          15 | 10.27%   | 47.17%             | -15.70% |     0.38 |       65 | 56.07%     | ok               |
|          25 | 2.79%    | 47.17%             | -16.10% |     0.16 |       58 | 51.58%     | ok               |
|          30 | -4.92%   | 47.17%             | -18.77% |    -0.12 |       68 | 49.58%     | ok               |
|          35 | -7.31%   | 47.17%             | -20.89% |    -0.22 |       62 | 46.42%     | ok               |

## VWO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -7.67%   | 41.06%             | -21.18% |    -0.27 |       58 | 30.45%     | ok               |
|          45 | -9.47%   | 41.06%             | -23.26% |    -0.35 |       60 | 32.95%     | ok               |
|          15 | -11.97%  | 41.06%             | -24.01% |    -0.37 |       76 | 48.42%     | ok               |
|          40 | -10.50%  | 41.06%             | -23.57% |    -0.38 |       70 | 35.61%     | ok               |
|          20 | -13.40%  | 41.06%             | -26.14% |    -0.44 |       73 | 46.09%     | ok               |

## VZ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -4.86%   | 18.02%             | -12.71% |    -0.11 |       52 | 25.29%     | ok               |
|          25 | -18.45%  | 18.02%             | -22.13% |    -0.5  |       79 | 42.76%     | ok               |
|          45 | -16.22%  | 18.02%             | -21.44% |    -0.51 |       66 | 28.95%     | ok               |
|          35 | -17.42%  | 18.02%             | -22.73% |    -0.53 |       61 | 34.78%     | ok               |
|          40 | -22.04%  | 18.02%             | -24.21% |    -0.72 |       66 | 32.11%     | ok               |

## WFC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | -10.67%  | 53.95%             | -22.54% |    -0.17 |       81 | 46.26%     | ok               |
|          50 | -7.92%   | 53.95%             | -18.29% |    -0.19 |       62 | 33.94%     | ok               |
|          20 | -17.69%  | 53.95%             | -29.87% |    -0.25 |       79 | 55.41%     | ok               |
|          30 | -19.98%  | 53.95%             | -29.78% |    -0.35 |       84 | 49.42%     | ok               |
|          25 | -23.43%  | 53.95%             | -33.38% |    -0.41 |       76 | 52.41%     | ok               |

## WIF-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 29.75%   | -76.95%            | -46.21% |     0.51 |       74 | 43.87%     | ok               |
|          20 | 26.38%   | -76.95%            | -40.67% |     0.48 |       67 | 41.00%     | ok               |
|          25 | -35.79%  | -76.95%            | -52.50% |    -0.07 |       71 | 37.74%     | ok               |
|          50 | -24.32%  | -76.95%            | -41.18% |    -0.22 |       42 | 12.26%     | ok               |
|          30 | -52.90%  | -76.95%            | -61.76% |    -0.39 |       72 | 33.91%     | ok               |

## WMT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 41.75%   | 82.51%             | -9.18%  |     1.19 |       40 | 40.10%     | ok               |
|          50 | 36.27%   | 82.51%             | -12.19% |     1.12 |       34 | 37.60%     | ok               |
|          40 | 29.95%   | 82.51%             | -13.41% |     0.89 |       46 | 41.43%     | ok               |
|          35 | 29.10%   | 82.51%             | -13.99% |     0.84 |       56 | 46.09%     | ok               |
|          15 | 15.66%   | 82.51%             | -25.74% |     0.43 |       72 | 60.23%     | ok               |

## XBI Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 3.14%    | 52.13%             | -16.08% |     0.16 |       60 | 34.11%     | ok               |
|          45 | 2.35%    | 52.13%             | -15.46% |     0.14 |       52 | 30.95%     | ok               |
|          35 | -4.62%   | 52.13%             | -16.96% |    -0.04 |       66 | 37.77%     | ok               |
|          30 | -5.68%   | 52.13%             | -18.30% |    -0.07 |       66 | 39.43%     | ok               |
|          50 | -6.05%   | 52.13%             | -15.97% |    -0.11 |       54 | 27.62%     | ok               |

## XLB Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -3.51%   | 12.90%             | -19.67% |    -0.08 |       54 | 30.28%     | ok               |
|          50 | -4.79%   | 12.90%             | -17.59% |    -0.15 |       42 | 26.12%     | ok               |
|          35 | -6.68%   | 12.90%             | -22.65% |    -0.2  |       56 | 33.61%     | ok               |
|          45 | -6.42%   | 12.90%             | -19.78% |    -0.21 |       42 | 27.45%     | ok               |
|          25 | -9.76%   | 12.90%             | -22.63% |    -0.31 |       60 | 39.10%     | ok               |

## XLC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 11.41%   | 40.16%             | -12.33% |     0.43 |       67 | 52.91%     | ok               |
|          25 | 8.67%    | 40.16%             | -12.31% |     0.34 |       66 | 54.74%     | ok               |
|          40 | 7.83%    | 40.16%             | -13.38% |     0.34 |       66 | 45.76%     | ok               |
|          35 | 7.01%    | 40.16%             | -13.38% |     0.3  |       64 | 49.92%     | ok               |
|          45 | 2.84%    | 40.16%             | -13.21% |     0.16 |       64 | 42.93%     | ok               |

## XLE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 5.75%    | 31.99%             | -25.98% |     0.23 |       54 | 36.11%     | ok               |
|          45 | 1.41%    | 31.99%             | -29.68% |     0.11 |       60 | 38.10%     | ok               |
|          35 | 0.02%    | 31.99%             | -31.00% |     0.08 |       65 | 42.93%     | ok               |
|          25 | -6.61%   | 31.99%             | -35.58% |    -0.08 |       83 | 48.42%     | ok               |
|          40 | -7.19%   | 31.99%             | -34.51% |    -0.13 |       64 | 40.60%     | ok               |

## XLF Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -4.08%   | 41.02%             | -18.01% |    -0.07 |       70 | 53.74%     | ok               |
|          15 | -8.05%   | 41.02%             | -19.58% |    -0.21 |       78 | 56.57%     | ok               |
|          25 | -10.52%  | 41.02%             | -23.22% |    -0.32 |       77 | 50.42%     | ok               |
|          30 | -11.97%  | 41.02%             | -23.61% |    -0.39 |       78 | 47.75%     | ok               |
|          35 | -19.84%  | 41.02%             | -27.41% |    -0.79 |       68 | 43.43%     | ok               |

## XLI Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 3.50%    | 50.54%             | -10.36% |     0.18 |       80 | 50.92%     | ok               |
|          20 | -0.66%   | 50.54%             | -12.74% |     0.03 |       73 | 45.76%     | ok               |
|          30 | -4.86%   | 50.54%             | -14.12% |    -0.15 |       68 | 42.60%     | ok               |
|          25 | -5.88%   | 50.54%             | -14.41% |    -0.18 |       70 | 43.76%     | ok               |
|          50 | -5.17%   | 50.54%             | -13.59% |    -0.2  |       62 | 30.62%     | ok               |

## XLK Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 78.33%   | 72.20%             | -14.75% |     1.27 |       43 | 51.25%     | ok               |
|          20 | 71.51%   | 72.20%             | -14.75% |     1.23 |       46 | 48.92%     | ok               |
|          25 | 68.02%   | 72.20%             | -14.75% |     1.23 |       40 | 46.76%     | ok               |
|          30 | 65.83%   | 72.20%             | -14.75% |     1.22 |       40 | 45.59%     | ok               |
|          35 | 47.33%   | 72.20%             | -13.61% |     0.99 |       52 | 42.93%     | ok               |

## XLM-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 26.14%   | -45.27%            | -38.97% |     0.48 |       44 | 27.39%     | ok               |
|          45 | 22.34%   | -45.27%            | -43.99% |     0.44 |       50 | 31.03%     | ok               |
|          30 | 7.39%    | -45.27%            | -50.36% |     0.3  |       65 | 45.21%     | ok               |
|          25 | 4.10%    | -45.27%            | -48.11% |     0.27 |       67 | 47.70%     | ok               |
|          20 | -4.13%   | -45.27%            | -55.30% |     0.18 |       66 | 50.00%     | ok               |

## XLP Threshold Sweep

|   threshold | return   | benchmark_return   | mdd    |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:-------|---------:|---------:|:-----------|:-----------------|
|          45 | 11.80%   | 12.29%             | -5.66% |     0.73 |       50 | 32.11%     | ok               |
|          40 | 11.17%   | 12.29%             | -7.32% |     0.67 |       66 | 36.11%     | ok               |
|          35 | 10.20%   | 12.29%             | -8.39% |     0.61 |       62 | 39.10%     | ok               |
|          30 | 9.31%    | 12.29%             | -8.96% |     0.55 |       64 | 40.77%     | ok               |
|          50 | 8.36%    | 12.29%             | -6.08% |     0.54 |       54 | 30.28%     | ok               |

## XLU Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 5.85%    | 38.47%             | -12.97% |     0.32 |       52 | 31.28%     | ok               |
|          45 | 4.45%    | 38.47%             | -14.27% |     0.25 |       54 | 32.28%     | ok               |
|          40 | 1.57%    | 38.47%             | -15.59% |     0.12 |       58 | 33.78%     | ok               |
|          35 | -4.35%   | 38.47%             | -19.71% |    -0.16 |       62 | 35.94%     | ok               |
|          30 | -5.24%   | 38.47%             | -20.40% |    -0.19 |       67 | 39.10%     | ok               |

## XLV Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -14.97%  | 10.86%             | -18.72% |    -0.74 |       66 | 34.44%     | ok               |
|          25 | -15.89%  | 10.86%             | -21.14% |    -0.78 |       68 | 36.61%     | ok               |
|          20 | -19.08%  | 10.86%             | -24.51% |    -0.94 |       73 | 38.44%     | ok               |
|          15 | -19.58%  | 10.86%             | -24.84% |    -0.94 |       81 | 41.43%     | ok               |
|          45 | -17.35%  | 10.86%             | -20.89% |    -1.03 |       56 | 24.96%     | ok               |

## XLY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 4.82%    | 31.48%             | -12.94% |     0.22 |       68 | 41.10%     | ok               |
|          30 | 3.22%    | 31.48%             | -14.01% |     0.17 |       68 | 43.93%     | ok               |
|          50 | 1.48%    | 31.48%             | -11.49% |     0.11 |       52 | 29.45%     | ok               |
|          15 | 0.43%    | 31.48%             | -15.77% |     0.09 |       74 | 50.58%     | ok               |
|          20 | -4.08%   | 31.48%             | -19.25% |    -0.05 |       69 | 47.25%     | ok               |

## XOM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | 9.38%    | 42.23%             | -19.90% |     0.32 |       55 | 38.60%     | ok               |
|          50 | 8.44%    | 42.23%             | -21.35% |     0.31 |       38 | 30.78%     | ok               |
|          30 | 8.30%    | 42.23%             | -20.29% |     0.29 |       55 | 37.94%     | ok               |
|          20 | 3.17%    | 42.23%             | -25.56% |     0.16 |       62 | 40.93%     | ok               |
|          45 | 1.44%    | 42.23%             | -23.33% |     0.11 |       44 | 32.28%     | ok               |

## XRP-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | -13.80%  | -50.91%            | -38.85% |     0.02 |       64 | 38.89%     | ok               |
|          40 | -22.96%  | -50.91%            | -38.94% |    -0.14 |       54 | 33.14%     | ok               |
|          30 | -27.75%  | -50.91%            | -47.86% |    -0.17 |       66 | 43.10%     | ok               |
|          45 | -31.57%  | -50.91%            | -40.24% |    -0.3  |       54 | 28.93%     | ok               |
|          50 | -27.85%  | -50.91%            | -38.03% |    -0.32 |       56 | 21.46%     | ok               |

## YFI-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -51.83%  | -61.24%            | -52.84% |    -0.88 |       60 | 27.97%     | ok               |
|          30 | -64.19%  | -61.24%            | -71.12% |    -1.03 |       81 | 40.61%     | ok               |
|          35 | -62.09%  | -61.24%            | -63.29% |    -1.04 |       65 | 35.25%     | ok               |
|          45 | -50.42%  | -61.24%            | -54.66% |    -1.05 |       70 | 22.61%     | ok               |
|          25 | -69.64%  | -61.24%            | -73.69% |    -1.18 |       80 | 46.55%     | ok               |

## ZEC-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 105.68%  | 1182.66%           | -24.66% |     0.83 |       44 | 24.90%     | ok               |
|          35 | 76.00%   | 1182.66%           | -44.34% |     0.7  |       52 | 31.03%     | ok               |
|          25 | 58.23%   | 1182.66%           | -51.83% |     0.63 |       58 | 40.23%     | ok               |
|          30 | 38.58%   | 1182.66%           | -49.45% |     0.53 |       64 | 37.16%     | ok               |
|          50 | 41.39%   | 1182.66%           | -34.17% |     0.53 |       46 | 22.41%     | ok               |
