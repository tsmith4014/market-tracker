# Market Tracker Backtest Report

_Generated: 2026-07-22T03:52:43+00:00_

## Data Sources

- Crypto: Kraken -> Coinbase -> CoinGecko OHLC -> CoinPaprika fallback chain.
- Stocks / ETFs / indices: Stooq -> Yahoo Finance fallback chain.
- Data rows are generated from real market APIs. Mock OHLCV rows are not generated.

## Data Freshness

- Rows: **92,527**
- Symbols: **161**
- Date range: **2024-02-27** to **2026-07-22**

## Latest Signals

| symbol     | date                |         close |   composite_score | signal   | data_source   |
|:-----------|:--------------------|--------------:|------------------:|:---------|:--------------|
| AAPL       | 2026-07-21 00:00:00 |   327.74      |         49.0833   | LONG     | Yahoo Finance |
| AAVE-USD   | 2026-07-22 00:00:00 |    96.51      |         30.3333   | LONG     | Kraken API    |
| ABBV       | 2026-07-21 00:00:00 |   256.1       |         36.5      | LONG     | Yahoo Finance |
| AMGN       | 2026-07-21 00:00:00 |   366.24      |         36.0833   | LONG     | Yahoo Finance |
| AMZN       | 2026-07-21 00:00:00 |   247.55      |         68.1667   | LONG     | Yahoo Finance |
| ARB-USD    | 2026-07-22 00:00:00 |     0.0898    |         48.6667   | LONG     | Kraken API    |
| BAC        | 2026-07-21 00:00:00 |    61.22      |         38.25     | LONG     | Yahoo Finance |
| COP        | 2026-07-21 00:00:00 |   117.5       |         71.25     | LONG     | Yahoo Finance |
| CRV-USD    | 2026-07-22 00:00:00 |     0.21387   |         52.4167   | LONG     | Kraken API    |
| CVX        | 2026-07-21 00:00:00 |   191.07      |         72.75     | LONG     | Yahoo Finance |
| DBC        | 2026-07-21 00:00:00 |    29.57      |         73.25     | LONG     | Yahoo Finance |
| DXY-INDEX  | 2026-07-21 00:00:00 |   101.142     |         52.1505   | LONG     | Yahoo Finance |
| EOG        | 2026-07-21 00:00:00 |   143.44      |         71.25     | LONG     | Yahoo Finance |
| ETH-USD    | 2026-07-22 00:00:00 |  1930.89      |         48.1667   | LONG     | Kraken API    |
| FCX        | 2026-07-21 00:00:00 |    62.56      |         53.75     | LONG     | Yahoo Finance |
| INJ-USD    | 2026-07-22 00:00:00 |     5.395     |         76.5833   | LONG     | Kraken API    |
| LDO-USD    | 2026-07-22 00:00:00 |     0.391     |         42.0833   | LONG     | Kraken API    |
| LINK-USD   | 2026-07-22 00:00:00 |     8.70599   |         54.75     | LONG     | Kraken API    |
| LTC-USD    | 2026-07-22 00:00:00 |    46.67      |         52.3333   | LONG     | Kraken API    |
| META       | 2026-07-21 00:00:00 |   643.81      |         57.6667   | LONG     | Yahoo Finance |
| MPC        | 2026-07-21 00:00:00 |   319.76      |         73.75     | LONG     | Yahoo Finance |
| OXY        | 2026-07-21 00:00:00 |    56.5       |         75        | LONG     | Yahoo Finance |
| PEPE-USD   | 2026-07-22 00:00:00 |     2.865e-06 |         50.6667   | LONG     | Kraken API    |
| POL-USD    | 2026-07-22 00:00:00 |     0.07986   |         31        | LONG     | Kraken API    |
| RTX        | 2026-07-21 00:00:00 |   193.67      |         37.8333   | LONG     | Yahoo Finance |
| SCHW       | 2026-07-21 00:00:00 |    99.96      |         45.9167   | LONG     | Yahoo Finance |
| SKY-USD    | 2026-07-22 00:00:00 |     0.06237   |         30.6667   | LONG     | Kraken API    |
| TMO        | 2026-07-21 00:00:00 |   523.46      |         44.6667   | LONG     | Yahoo Finance |
| UNH        | 2026-07-21 00:00:00 |   436.35      |         50.5833   | LONG     | Yahoo Finance |
| UNI-USD    | 2026-07-22 00:00:00 |     3.6772    |         34.6667   | LONG     | Kraken API    |
| UPS        | 2026-07-21 00:00:00 |   116.34      |         76.9167   | LONG     | Yahoo Finance |
| USO        | 2026-07-21 00:00:00 |   128.85      |         69.25     | LONG     | Yahoo Finance |
| XBI        | 2026-07-21 00:00:00 |   154.5       |         36.4167   | LONG     | Yahoo Finance |
| XLE        | 2026-07-21 00:00:00 |    58.5       |         73.25     | LONG     | Yahoo Finance |
| XLF        | 2026-07-21 00:00:00 |    56.11      |         52.0833   | LONG     | Yahoo Finance |
| XLV        | 2026-07-21 00:00:00 |   160.25      |         39.75     | LONG     | Yahoo Finance |
| XOM        | 2026-07-21 00:00:00 |   151.71      |         75        | LONG     | Yahoo Finance |
| ZEC-USD    | 2026-07-22 00:00:00 |   528.89      |         64.1667   | LONG     | Kraken API    |
| ADA-USD    | 2026-07-22 00:00:00 |     0.173859  |         24        | NEUTRAL  | Kraken API    |
| ADBE       | 2026-07-21 00:00:00 |   227.16      |          6.91667  | NEUTRAL  | Yahoo Finance |
| ALGO-USD   | 2026-07-22 00:00:00 |     0.08422   |        -29.9167   | NEUTRAL  | Kraken API    |
| AMAT       | 2026-07-21 00:00:00 |   564.55      |         -3.66667  | NEUTRAL  | Yahoo Finance |
| AMD        | 2026-07-21 00:00:00 |   544.43      |         18.1667   | NEUTRAL  | Yahoo Finance |
| APT-USD    | 2026-07-22 00:00:00 |     0.6106    |        -16.6667   | NEUTRAL  | Kraken API    |
| ARKK       | 2026-07-21 00:00:00 |    77.695     |        -23.5833   | NEUTRAL  | Yahoo Finance |
| ATOM-USD   | 2026-07-22 00:00:00 |     1.4861    |        -27.6667   | NEUTRAL  | Kraken API    |
| AVAX-USD   | 2026-07-22 00:00:00 |     6.58      |        -12        | NEUTRAL  | Kraken API    |
| AVGO       | 2026-07-21 00:00:00 |   386.5       |         16.9167   | NEUTRAL  | Yahoo Finance |
| BA         | 2026-07-21 00:00:00 |   204.8       |        -71.25     | NEUTRAL  | Yahoo Finance |
| BITO       | 2026-07-21 00:00:00 |     9.01      |          8.33333  | NEUTRAL  | Yahoo Finance |
| BLK        | 2026-07-21 00:00:00 |  1038.24      |         28.6667   | NEUTRAL  | Yahoo Finance |
| BTC-USD    | 2026-07-22 00:00:00 | 66266.2       |         41.4167   | NEUTRAL  | Kraken API    |
| C          | 2026-07-21 00:00:00 |   132.84      |         -4.08333  | NEUTRAL  | Yahoo Finance |
| CAT        | 2026-07-21 00:00:00 |   889.97      |        -29.3333   | NEUTRAL  | Yahoo Finance |
| CL         | 2026-07-21 00:00:00 |    90.5       |        -13.3333   | NEUTRAL  | Yahoo Finance |
| CMCSA      | 2026-07-21 00:00:00 |    23.81      |          7.08333  | NEUTRAL  | Yahoo Finance |
| COMP-USD   | 2026-07-22 00:00:00 |    17.37      |         25.6667   | NEUTRAL  | Kraken API    |
| COST       | 2026-07-21 00:00:00 |   929.22      |        -19.5      | NEUTRAL  | Yahoo Finance |
| CRM        | 2026-07-21 00:00:00 |   170.06      |         -3.83333  | NEUTRAL  | Yahoo Finance |
| CSCO       | 2026-07-21 00:00:00 |   112.18      |          4.41667  | NEUTRAL  | Yahoo Finance |
| DASH-USD   | 2026-07-22 00:00:00 |    34.588     |        -15.5833   | NEUTRAL  | Kraken API    |
| DE         | 2026-07-21 00:00:00 |   586.88      |         -1.16667  | NEUTRAL  | Yahoo Finance |
| DIA        | 2026-07-21 00:00:00 |   521.51      |         22.4167   | NEUTRAL  | Yahoo Finance |
| DIS        | 2026-07-21 00:00:00 |    96.14      |        -38.6667   | NEUTRAL  | Yahoo Finance |
| DOGE-USD   | 2026-07-22 00:00:00 |     0.0732843 |        -10.5833   | NEUTRAL  | Kraken API    |
| DOT-USD    | 2026-07-22 00:00:00 |     0.8556    |         18.4167   | NEUTRAL  | Kraken API    |
| EEM        | 2026-07-21 00:00:00 |    65.34      |        -13.0833   | NEUTRAL  | Yahoo Finance |
| EFA        | 2026-07-21 00:00:00 |   104.06      |         31        | NEUTRAL  | Yahoo Finance |
| ETC-USD    | 2026-07-22 00:00:00 |     6.996     |        -16.0833   | NEUTRAL  | Kraken API    |
| EWJ        | 2026-07-21 00:00:00 |    92.74      |         15.6667   | NEUTRAL  | Yahoo Finance |
| FET-USD    | 2026-07-22 00:00:00 |     0.157     |        -17        | NEUTRAL  | Kraken API    |
| FIL-USD    | 2026-07-22 00:00:00 |     0.771     |         -1.33333  | NEUTRAL  | Kraken API    |
| FXI        | 2026-07-21 00:00:00 |    34.63      |         25.25     | NEUTRAL  | Yahoo Finance |
| GDX        | 2026-07-21 00:00:00 |    74.19      |        -42        | NEUTRAL  | Yahoo Finance |
| GDXJ       | 2026-07-21 00:00:00 |    97.09      |        -45.3333   | NEUTRAL  | Yahoo Finance |
| GE         | 2026-07-21 00:00:00 |   340.7       |         -4.91667  | NEUTRAL  | Yahoo Finance |
| GLD        | 2026-07-21 00:00:00 |   374.81      |        -29.8333   | NEUTRAL  | Yahoo Finance |
| GOOGL      | 2026-07-21 00:00:00 |   347.15      |        -26.75     | NEUTRAL  | Yahoo Finance |
| GRT-USD    | 2026-07-22 00:00:00 |     0.01665   |        -22        | NEUTRAL  | Kraken API    |
| GS         | 2026-07-21 00:00:00 |  1085.56      |         50        | NEUTRAL  | Yahoo Finance |
| HBAR-USD   | 2026-07-22 00:00:00 |     0.07027   |          0.416667 | NEUTRAL  | Kraken API    |
| HD         | 2026-07-21 00:00:00 |   331.6       |        -54.0833   | NEUTRAL  | Yahoo Finance |
| HON        | 2026-07-21 00:00:00 |   229.86      |         28.1667   | NEUTRAL  | Yahoo Finance |
| HYG        | 2026-07-21 00:00:00 |    79.65      |        -55.0833   | NEUTRAL  | Yahoo Finance |
| IBIT       | 2026-07-21 00:00:00 |    37.67      |         -9.66667  | NEUTRAL  | Yahoo Finance |
| ICP-USD    | 2026-07-22 00:00:00 |     2.204     |        -25.75     | NEUTRAL  | Kraken API    |
| IEMG       | 2026-07-21 00:00:00 |    79.3       |        -14.8333   | NEUTRAL  | Yahoo Finance |
| INTC       | 2026-07-21 00:00:00 |   105.45      |        -26.0833   | NEUTRAL  | Yahoo Finance |
| INTU       | 2026-07-21 00:00:00 |   289.92      |          2.16667  | NEUTRAL  | Yahoo Finance |
| ITA        | 2026-07-21 00:00:00 |   229.74      |        -22.5      | NEUTRAL  | Yahoo Finance |
| IWM        | 2026-07-21 00:00:00 |   296.54      |         20.6667   | NEUTRAL  | Yahoo Finance |
| JNJ        | 2026-07-21 00:00:00 |   250.61      |          0.416667 | NEUTRAL  | Yahoo Finance |
| JPM        | 2026-07-21 00:00:00 |   345.23      |         22.75     | NEUTRAL  | Yahoo Finance |
| KO         | 2026-07-21 00:00:00 |    81.97      |         17.3333   | NEUTRAL  | Yahoo Finance |
| LIN        | 2026-07-21 00:00:00 |   505.03      |        -29        | NEUTRAL  | Yahoo Finance |
| LLY        | 2026-07-21 00:00:00 |  1175.41      |          7.58333  | NEUTRAL  | Yahoo Finance |
| LRCX       | 2026-07-21 00:00:00 |   322         |        -33.5833   | NEUTRAL  | Yahoo Finance |
| MCD        | 2026-07-21 00:00:00 |   263.91      |        -43.5      | NEUTRAL  | Yahoo Finance |
| MRK        | 2026-07-21 00:00:00 |   126.26      |         28.6667   | NEUTRAL  | Yahoo Finance |
| MS         | 2026-07-21 00:00:00 |   216.4       |         19        | NEUTRAL  | Yahoo Finance |
| MSFT       | 2026-07-21 00:00:00 |   397.75      |         14.1667   | NEUTRAL  | Yahoo Finance |
| MU         | 2026-07-21 00:00:00 |   970.82      |         14.9167   | NEUTRAL  | Yahoo Finance |
| NEAR-USD   | 2026-07-22 00:00:00 |     1.9267    |          6        | NEUTRAL  | Kraken API    |
| NEM        | 2026-07-21 00:00:00 |    92.49      |        -55.3333   | NEUTRAL  | Yahoo Finance |
| NFLX       | 2026-07-21 00:00:00 |    68.67      |        -57        | NEUTRAL  | Yahoo Finance |
| NKE        | 2026-07-21 00:00:00 |    42.96      |        -21.25     | NEUTRAL  | Yahoo Finance |
| NOW        | 2026-07-21 00:00:00 |   102.06      |        -39.1667   | NEUTRAL  | Yahoo Finance |
| NVDA       | 2026-07-21 00:00:00 |   207.29      |         47.4167   | NEUTRAL  | Yahoo Finance |
| OP-USD     | 2026-07-22 00:00:00 |     0.0972    |        -41.25     | NEUTRAL  | Kraken API    |
| PEP        | 2026-07-21 00:00:00 |   135         |        -54.8333   | NEUTRAL  | Yahoo Finance |
| PFE        | 2026-07-21 00:00:00 |    24.94      |          2.66667  | NEUTRAL  | Yahoo Finance |
| PG         | 2026-07-21 00:00:00 |   148.1       |         -3.16667  | NEUTRAL  | Yahoo Finance |
| PM         | 2026-07-21 00:00:00 |   188.04      |         58.6667   | NEUTRAL  | Yahoo Finance |
| QCOM       | 2026-07-21 00:00:00 |   173.5       |        -15.8333   | NEUTRAL  | Yahoo Finance |
| QQQ        | 2026-07-21 00:00:00 |   708.97      |         -8        | NEUTRAL  | Yahoo Finance |
| RENDER-USD | 2026-07-22 00:00:00 |     1.517     |        -29.9167   | NEUTRAL  | Kraken API    |
| SBUX       | 2026-07-21 00:00:00 |   104.45      |         33.5      | NEUTRAL  | Yahoo Finance |
| SHIB-USD   | 2026-07-22 00:00:00 |     4.242e-06 |        -29.9167   | NEUTRAL  | Kraken API    |
| SHY        | 2026-07-21 00:00:00 |    81.89      |        -45.4167   | NEUTRAL  | Yahoo Finance |
| SLB        | 2026-07-21 00:00:00 |    46.59      |         -4.83333  | NEUTRAL  | Yahoo Finance |
| SLV        | 2026-07-21 00:00:00 |    53.08      |        -27.25     | NEUTRAL  | Yahoo Finance |
| SMH        | 2026-07-21 00:00:00 |   584.08      |          3.25     | NEUTRAL  | Yahoo Finance |
| SNX-USD    | 2026-07-22 00:00:00 |     0.2288    |          4.16667  | NEUTRAL  | Kraken API    |
| SOL-USD    | 2026-07-22 00:00:00 |    78.1       |         14        | NEUTRAL  | Kraken API    |
| SOXX       | 2026-07-21 00:00:00 |   552.69      |          1.25     | NEUTRAL  | Yahoo Finance |
| SPY        | 2026-07-21 00:00:00 |   748.28      |         41.5      | NEUTRAL  | Yahoo Finance |
| SUSHI-USD  | 2026-07-22 00:00:00 |     0.1678    |         22.6667   | NEUTRAL  | Kraken API    |
| T          | 2026-07-21 00:00:00 |    22.26      |          5.08333  | NEUTRAL  | Yahoo Finance |
| TGT        | 2026-07-21 00:00:00 |   138.48      |         59.0833   | NEUTRAL  | Yahoo Finance |
| TMUS       | 2026-07-21 00:00:00 |   190.77      |         42.75     | NEUTRAL  | Yahoo Finance |
| TRX-USD    | 2026-07-22 00:00:00 |     0.3284    |         63.8333   | NEUTRAL  | Kraken API    |
| TSLA       | 2026-07-21 00:00:00 |   378.93      |        -67        | NEUTRAL  | Yahoo Finance |
| TXN        | 2026-07-21 00:00:00 |   291.3       |         -6.33333  | NEUTRAL  | Yahoo Finance |
| VEA        | 2026-07-21 00:00:00 |    70.47      |         -2.33333  | NEUTRAL  | Yahoo Finance |
| VIXY       | 2026-07-21 00:00:00 |    20.66      |        -26.5      | NEUTRAL  | Yahoo Finance |
| VNQ        | 2026-07-21 00:00:00 |    99.52      |         69.3333   | NEUTRAL  | Yahoo Finance |
| VTI        | 2026-07-21 00:00:00 |   369.45      |         33.1667   | NEUTRAL  | Yahoo Finance |
| VWO        | 2026-07-21 00:00:00 |    58.86      |        -38.3333   | NEUTRAL  | Yahoo Finance |
| VZ         | 2026-07-21 00:00:00 |    43.78      |         26.6667   | NEUTRAL  | Yahoo Finance |
| WFC        | 2026-07-21 00:00:00 |    87.74      |         33.5833   | NEUTRAL  | Yahoo Finance |
| WIF-USD    | 2026-07-22 00:00:00 |     0.1532    |        -22        | NEUTRAL  | Kraken API    |
| XLB        | 2026-07-21 00:00:00 |    50.1       |        -15.3333   | NEUTRAL  | Yahoo Finance |
| XLC        | 2026-07-21 00:00:00 |   110.03      |        -27        | NEUTRAL  | Yahoo Finance |
| XLI        | 2026-07-21 00:00:00 |   178.66      |         17.0833   | NEUTRAL  | Yahoo Finance |
| XLK        | 2026-07-21 00:00:00 |   180.78      |         -8        | NEUTRAL  | Yahoo Finance |
| XLM-USD    | 2026-07-22 00:00:00 |     0.191316  |         16.4167   | NEUTRAL  | Kraken API    |
| XLP        | 2026-07-21 00:00:00 |    84.06      |         26.9167   | NEUTRAL  | Yahoo Finance |
| XLU        | 2026-07-21 00:00:00 |    44.92      |        -13.9167   | NEUTRAL  | Yahoo Finance |
| XLY        | 2026-07-21 00:00:00 |   114.87      |        -56.75     | NEUTRAL  | Yahoo Finance |
| XRP-USD    | 2026-07-22 00:00:00 |     1.14077   |         20.6667   | NEUTRAL  | Kraken API    |
| YFI-USD    | 2026-07-22 00:00:00 |  2144.9       |         19.0833   | NEUTRAL  | Kraken API    |
| AGG        | 2026-07-21 00:00:00 |    97.74      |        -53.0833   | SHORT    | Yahoo Finance |
| BCH-USD    | 2026-07-22 00:00:00 |   225.01      |        -51.3333   | SHORT    | Kraken API    |
| BND        | 2026-07-21 00:00:00 |    72.515     |        -53.0833   | SHORT    | Yahoo Finance |
| BONK-USD   | 2026-07-22 00:00:00 |     3.073e-06 |        -46.6667   | SHORT    | Kraken API    |
| IBM        | 2026-07-21 00:00:00 |   210.5       |        -65.0833   | SHORT    | Yahoo Finance |
| IEF        | 2026-07-21 00:00:00 |    93.31      |        -51.5      | SHORT    | Yahoo Finance |
| ORCL       | 2026-07-21 00:00:00 |   127.05      |        -48.0833   | SHORT    | Yahoo Finance |
| TIA-USD    | 2026-07-22 00:00:00 |     0.3622    |        -39        | SHORT    | Kraken API    |
| TLT        | 2026-07-21 00:00:00 |    83.66      |        -55.0833   | SHORT    | Yahoo Finance |
| WMT        | 2026-07-21 00:00:00 |   110.39      |        -33.75     | SHORT    | Yahoo Finance |

## Edge Summary

- Symbols with trades: **160** of 160
- Beat buy-and-hold: **33.12%** of traded symbols
- Positive return: **28.75%** of traded symbols
- Median strategy return: **-10.63%** (benchmark **13.97%**)
- Median excess vs benchmark: **-25.39%**
- Median Sharpe: **-0.14**
- Median exposure: **44.17%**

> Edge is real only if both _beat buy-and-hold_ and _median excess_ are convincingly positive across many symbols. Treat a single high-return symbol as noise.

## Portfolio Backtest

Actual capital-allocation books (not per-symbol averages). Benchmarks: `equal_weight_buyhold` (whole tracked universe), `spy_buyhold` (100% SPY), and `sixty_forty` (60% SPY / 40% AGG). `high_conf_voltarget` inverse-vol-weights the HIGH-confidence book; `conviction_long_short` is market-neutral. Judge on **Sharpe** and **max_drawdown** out-of-sample, not raw return: a fully-invested long book wins on return in a bull market but carries all the risk.

| strategy              | scope         | ann_return   | ann_vol   |   sharpe | max_drawdown   | total_return   |   avg_gross_exposure |
|:----------------------|:--------------|:-------------|:----------|---------:|:---------------|:---------------|---------------------:|
| equal_weight_buyhold  | full          | -3.48%       | 32.46%    |    -0.11 | -46.29%        | -23.50%        |                 1    |
| equal_weight_buyhold  | out_of_sample | -24.10%      | 30.64%    |    -0.79 | -38.25%        | -26.49%        |                 1    |
| all_signals_ew        | full          | -18.14%      | 26.82%    |    -0.68 | -62.08%        | -48.49%        |                 1    |
| all_signals_ew        | out_of_sample | 24.18%       | 26.29%    |     0.92 | -18.39%        | 24.81%         |                 1    |
| high_conf_ew          | full          | -1.09%       | 31.47%    |    -0.03 | -44.43%        | -16.66%        |                 0.88 |
| high_conf_ew          | out_of_sample | 21.23%       | 33.88%    |     0.63 | -17.94%        | 18.19%         |                 0.88 |
| high_conf_voltarget   | full          | 1.16%        | 29.02%    |     0.04 | -36.61%        | -8.68%         |                 0.88 |
| high_conf_voltarget   | out_of_sample | 15.70%       | 31.39%    |     0.5  | -16.94%        | 12.39%         |                 0.88 |
| conviction_long_short | full          | -19.41%      | 23.02%    |    -0.84 | -51.03%        | -48.98%        |                 0.97 |
| conviction_long_short | out_of_sample | -10.27%      | 26.15%    |    -0.39 | -24.28%        | -13.62%        |                 0.97 |
| spy_buyhold           | full          | 6.20%        | 13.33%    |     0.46 | -17.80%        | 17.57%         |                 0.78 |
| spy_buyhold           | out_of_sample | -2.76%       | 9.81%     |    -0.28 | -13.27%        | -3.40%         |                 0.78 |
| sixty_forty           | full          | 3.71%        | 8.43%     |     0.44 | -10.77%        | 10.77%         |                 0.78 |
| sixty_forty           | out_of_sample | -3.09%       | 6.46%     |    -0.48 | -9.26%         | -3.46%         |                 0.78 |

## Walk-Forward Robustness

Each book measured across contiguous time folds (each a different regime). A book has durable edge only if `mean_sharpe` is positive, `min_sharpe` isn't deeply negative, and `pct_positive_folds` is high — a single great fold doesn't count. `fold_sharpes` lists each fold oldest-to-newest.

| strategy              |   n_folds |   mean_sharpe |   median_sharpe |   min_sharpe | pct_positive_folds   | mean_return   | fold_sharpes                 |
|:----------------------|----------:|--------------:|----------------:|-------------:|:---------------------|:--------------|:-----------------------------|
| equal_weight_buyhold  |         5 |          0.28 |            0.74 |        -1.51 | 60.00%               | -1.72%        | 1.77;-1.51;1.49;-1.09;0.74   |
| all_signals_ew        |         5 |         -0.74 |           -0.27 |        -2.53 | 20.00%               | -11.14%       | -0.14;-0.27;-2.53;0.38;-1.16 |
| high_conf_ew          |         5 |          0.08 |           -0.39 |        -0.75 | 40.00%               | -2.63%        | 1.37;-0.61;-0.75;0.79;-0.39  |
| high_conf_voltarget   |         5 |          0.26 |           -0.25 |        -0.85 | 40.00%               | -0.93%        | 2.12;-0.25;-0.85;0.74;-0.47  |
| conviction_long_short |         5 |         -1.01 |           -1.41 |        -1.77 | 20.00%               | -12.11%       | -1.41;-1.65;-0.68;0.44;-1.77 |
| spy_buyhold           |         5 |          0.69 |            0.14 |        -1.16 | 60.00%               | 3.76%         | 1.64;-0.42;3.24;-1.16;0.14   |
| sixty_forty           |         5 |          0.63 |           -0.23 |        -1.1  | 40.00%               | 2.27%         | 1.76;-0.48;3.22;-1.10;-0.23  |

## Strategy Comparison

Each decision rule backtested over the same data. `out_of_sample` is the most recent ~35% of each symbol's history (unseen tail). A rule has real edge only if `median_excess` and `beat_benchmark_pct` stay positive out-of-sample, not just full-sample.

| strategy        | scope         |   symbols | beat_benchmark_pct   | positive_pct   | median_return   | median_benchmark   | median_excess   |   median_sharpe |   total_trades |
|:----------------|:--------------|----------:|:---------------------|:---------------|:----------------|:-------------------|:----------------|----------------:|---------------:|
| trend           | full          |       160 | 33.12%               | 28.75%         | -10.63%         | 13.97%             | -25.39%         |           -0.14 |          11246 |
| trend           | out_of_sample |       160 | 41.25%               | 52.50%         | 1.44%           | 5.38%              | -4.64%          |            0.22 |           3759 |
| mean_reversion  | full          |       157 | 40.76%               | 51.59%         | 0.09%           | 13.86%             | -13.70%         |            0.04 |           1258 |
| mean_reversion  | out_of_sample |       124 | 49.19%               | 59.68%         | 0.38%           | -0.50%             | -0.97%          |            0.58 |            428 |
| regime_adaptive | full          |       160 | 33.75%               | 30.63%         | -11.30%         | 13.97%             | -25.67%         |           -0.15 |          11520 |
| regime_adaptive | out_of_sample |       160 | 40.62%               | 53.12%         | 1.37%           | 5.38%              | -3.66%          |            0.22 |           3866 |

## Signal Calibration

Realized forward return in the signal's direction, grouped by confidence. HIGH should outrank LOW for the confidence score to be meaningful.

| confidence_level   |   horizon |     n | mean_return   | median_return   | win_rate   |
|:-------------------|----------:|------:|:--------------|:----------------|:-----------|
| HIGH               |         5 |  7898 | 0.11%         | 0.10%           | 51.66%     |
| MEDIUM             |         5 | 29165 | 0.01%         | 0.06%           | 50.71%     |
| LOW                |         5 |  3384 | -0.63%        | -0.56%          | 44.50%     |
| ALL                |         5 | 40447 | -0.02%        | 0.03%           | 50.38%     |
| HIGH               |        10 |  7870 | 0.36%         | 0.09%           | 51.03%     |
| MEDIUM             |        10 | 28961 | 0.14%         | 0.10%           | 50.73%     |
| LOW                |        10 |  3334 | -0.89%        | -0.72%          | 45.26%     |
| ALL                |        10 | 40165 | 0.10%         | 0.04%           | 50.33%     |
| HIGH               |        20 |  7781 | 0.75%         | 0.31%           | 52.62%     |
| MEDIUM             |        20 | 28594 | 0.80%         | 0.58%           | 53.33%     |
| LOW                |        20 |  3248 | -0.70%        | -0.51%          | 47.17%     |
| ALL                |        20 | 39623 | 0.67%         | 0.45%           | 52.69%     |

## Backtest Summary

### Data Quality / Signal Availability

- **ok**: 160 symbols

| symbol     |   trades | return   | benchmark_return   | mdd     |   sharpe | exposure   | skipped_reason   |
|:-----------|---------:|:---------|:-------------------|:--------|---------:|:-----------|:-----------------|
| AAPL       |       61 | 18.73%   | 79.46%             | -20.65% |     0.45 | 49.25%     | ok               |
| AAVE-USD   |       74 | -48.28%  | -61.98%            | -68.26% |    -0.41 | 39.08%     | ok               |
| ABBV       |       66 | -20.42%  | 43.08%             | -30.55% |    -0.43 | 47.09%     | ok               |
| ADA-USD    |       90 | -83.04%  | -77.48%            | -89.12% |    -0.67 | 46.93%     | ok               |
| ADBE       |       64 | -30.29%  | -58.88%            | -35.81% |    -0.38 | 57.07%     | ok               |
| AGG        |       71 | -6.67%   | 0.76%              | -10.25% |    -1.1  | 32.11%     | ok               |
| ALGO-USD   |       86 | -50.43%  | -69.39%            | -53.13% |    -0.57 | 38.12%     | ok               |
| AMAT       |       71 | -35.42%  | 178.30%            | -57.21% |    -0.33 | 51.91%     | ok               |
| AMD        |       52 | 5.86%    | 205.86%            | -43.98% |     0.27 | 35.77%     | ok               |
| AMGN       |       69 | -15.41%  | 31.51%             | -34.14% |    -0.29 | 46.26%     | ok               |
| AMZN       |       80 | -37.14%  | 42.65%             | -42.48% |    -1.11 | 38.27%     | ok               |
| APT-USD    |       74 | -45.23%  | -89.53%            | -69.65% |    -0.3  | 41.76%     | ok               |
| ARB-USD    |       72 | -25.96%  | -81.11%            | -62.34% |    -0.07 | 39.46%     | ok               |
| ARKK       |       85 | -36.50%  | 50.75%             | -37.96% |    -0.67 | 39.93%     | ok               |
| ATOM-USD   |       86 | -69.66%  | -68.80%            | -74.39% |    -1.22 | 44.25%     | ok               |
| AVAX-USD   |       70 | -41.95%  | -73.48%            | -60.43% |    -0.41 | 37.74%     | ok               |
| AVGO       |       64 | 15.13%   | 198.17%            | -35.76% |     0.34 | 42.26%     | ok               |
| BA         |       67 | 7.60%    | 1.69%              | -30.56% |     0.25 | 49.25%     | ok               |
| BAC        |       78 | -6.54%   | 78.59%             | -26.91% |    -0.09 | 50.25%     | ok               |
| BCH-USD    |       78 | -13.59%  | -30.98%            | -54.34% |     0.05 | 48.47%     | ok               |
| BITO       |       80 | -9.90%   | -66.54%            | -42.82% |     0.05 | 40.93%     | ok               |
| BLK        |       73 | -9.01%   | 29.69%             | -25.46% |    -0.2  | 42.60%     | ok               |
| BND        |       67 | -7.37%   | 0.80%              | -9.98%  |    -1.18 | 33.28%     | ok               |
| BONK-USD   |       72 | 78.81%   | -82.38%            | -45.22% |     0.76 | 42.34%     | ok               |
| BTC-USD    |       76 | -2.15%   | -31.08%            | -23.38% |     0.12 | 52.87%     | ok               |
| C          |       79 | -30.57%  | 138.45%            | -38.11% |    -0.61 | 51.08%     | ok               |
| CAT        |       72 | 20.42%   | 171.64%            | -21.02% |     0.43 | 55.41%     | ok               |
| CL         |       62 | 7.40%    | 4.73%              | -14.32% |     0.3  | 45.42%     | ok               |
| CMCSA      |       81 | -39.28%  | -39.90%            | -41.06% |    -1.04 | 41.76%     | ok               |
| COMP-USD   |       91 | -42.29%  | -68.40%            | -57.88% |    -0.3  | 45.79%     | ok               |
| COP        |       72 | -20.42%  | 5.28%              | -43.96% |    -0.34 | 42.26%     | ok               |
| COST       |       60 | -2.58%   | 24.78%             | -29.73% |    -0.01 | 43.09%     | ok               |
| CRM        |       63 | -39.56%  | -43.22%            | -41.36% |    -0.83 | 42.76%     | ok               |
| CRV-USD    |       70 | -7.01%   | -58.06%            | -39.89% |     0.16 | 36.59%     | ok               |
| CSCO       |       61 | 22.24%   | 132.21%            | -21.79% |     0.49 | 48.59%     | ok               |
| CVX        |       73 | -12.82%  | 25.57%             | -29.13% |    -0.3  | 39.60%     | ok               |
| DASH-USD   |       61 | -41.76%  | 29.05%             | -64.43% |    -0.02 | 29.12%     | ok               |
| DBC        |       62 | -9.97%   | 33.74%             | -25.70% |    -0.32 | 33.94%     | ok               |
| DE         |       74 | -9.70%   | 62.72%             | -25.24% |    -0.11 | 47.09%     | ok               |
| DIA        |       62 | -4.01%   | 33.84%             | -12.94% |    -0.18 | 43.76%     | ok               |
| DIS        |       66 | -17.08%  | -12.14%            | -28.17% |    -0.3  | 45.42%     | ok               |
| DOGE-USD   |       72 | -25.02%  | -72.40%            | -62.31% |    -0.01 | 49.81%     | ok               |
| DOT-USD    |       84 | -57.70%  | -82.47%            | -63.10% |    -0.61 | 47.51%     | ok               |
| DXY-INDEX  |       40 | -2.03%   | 0.53%              | -6.28%  |    -0.3  | 31.02%     | ok               |
| EEM        |       64 | -10.20%  | 61.33%             | -25.67% |    -0.28 | 42.60%     | ok               |
| EFA        |       62 | -9.51%   | 34.27%             | -14.87% |    -0.35 | 44.26%     | ok               |
| EOG        |       81 | -20.15%  | 25.89%             | -48.13% |    -0.39 | 47.59%     | ok               |
| ETC-USD    |       64 | -33.00%  | -65.71%            | -45.54% |    -0.46 | 29.31%     | ok               |
| ETH-USD    |       62 | 146.12%  | -27.49%            | -30.11% |     1.23 | 44.83%     | ok               |
| EWJ        |       62 | -19.80%  | 34.06%             | -30.73% |    -0.66 | 38.44%     | ok               |
| FCX        |       65 | -28.83%  | 63.94%             | -48.22% |    -0.34 | 45.09%     | ok               |
| FET-USD    |       85 | -39.88%  | -79.86%            | -54.02% |    -0.15 | 42.34%     | ok               |
| FIL-USD    |       68 | -47.73%  | -77.33%            | -50.22% |    -0.63 | 32.18%     | ok               |
| FXI        |       48 | -10.00%  | 42.39%             | -24.33% |    -0.17 | 30.28%     | ok               |
| GDX        |       60 | 11.28%   | 185.02%            | -34.99% |     0.3  | 48.09%     | ok               |
| GDXJ       |       66 | -22.87%  | 206.66%            | -44.93% |    -0.21 | 46.09%     | ok               |
| GE         |       76 | 8.72%    | 177.22%            | -27.82% |     0.27 | 52.75%     | ok               |
| GLD        |       50 | 23.54%   | 99.37%             | -16.63% |     0.6  | 48.09%     | ok               |
| GOOGL      |       57 | 77.30%   | 149.96%            | -20.41% |     1.16 | 52.75%     | ok               |
| GRT-USD    |       79 | -16.41%  | -87.97%            | -54.83% |     0.02 | 42.15%     | ok               |
| GS         |       76 | -2.38%   | 177.77%            | -22.13% |     0.05 | 52.08%     | ok               |
| HD         |       71 | -7.53%   | -11.71%            | -17.69% |    -0.12 | 44.59%     | ok               |
| HON        |       93 | -26.82%  | 17.34%             | -29.80% |    -0.72 | 52.41%     | ok               |
| HYG        |       81 | -9.52%   | 3.17%              | -9.59%  |    -1.11 | 34.28%     | ok               |
| IBIT       |       34 | 30.82%   | -0.89%             | -18.95% |     0.66 | 31.87%     | ok               |
| IBM        |       77 | -16.57%  | 13.86%             | -44.74% |    -0.14 | 49.75%     | ok               |
| ICP-USD    |       75 | -17.01%  | -68.46%            | -52.78% |     0.08 | 34.48%     | ok               |
| IEF        |       78 | -11.07%  | -0.41%             | -11.70% |    -1.57 | 32.95%     | ok               |
| IEMG       |       58 | -8.69%   | 55.67%             | -26.84% |    -0.24 | 42.10%     | ok               |
| INJ-USD    |       79 | -54.58%  | -63.81%            | -76.97% |    -0.53 | 38.70%     | ok               |
| INTC       |       68 | 59.68%   | 146.78%            | -60.60% |     0.64 | 49.08%     | ok               |
| INTU       |       67 | -19.54%  | -56.69%            | -42.15% |    -0.23 | 41.60%     | ok               |
| ITA        |       72 | -2.99%   | 81.79%             | -23.75% |    -0.01 | 47.92%     | ok               |
| IWM        |       48 | 9.40%    | 45.36%             | -12.83% |     0.39 | 35.77%     | ok               |
| JNJ        |       68 | 4.23%    | 55.68%             | -17.51% |     0.2  | 50.92%     | ok               |
| JPM        |       77 | -21.06%  | 88.19%             | -33.43% |    -0.51 | 53.58%     | ok               |
| KO         |       51 | 23.75%   | 35.85%             | -8.20%  |     0.85 | 37.94%     | ok               |
| LDO-USD    |       78 | 22.56%   | -78.05%            | -62.63% |     0.45 | 41.00%     | ok               |
| LIN        |       66 | -4.61%   | 13.54%             | -21.53% |    -0.11 | 38.60%     | ok               |
| LINK-USD   |       75 | -12.81%  | -53.47%            | -49.35% |     0.11 | 43.30%     | ok               |
| LLY        |       71 | -28.03%  | 53.65%             | -53.34% |    -0.41 | 49.08%     | ok               |
| LRCX       |       82 | -26.11%  | 245.97%            | -63.39% |    -0.16 | 44.09%     | ok               |
| LTC-USD    |       72 | -33.07%  | -62.84%            | -53.76% |    -0.27 | 50.19%     | ok               |
| MCD        |       75 | -2.55%   | -10.16%            | -18.81% |    -0.05 | 38.10%     | ok               |
| META       |       74 | -32.96%  | 32.19%             | -40.57% |    -0.6  | 47.92%     | ok               |
| MPC        |       71 | -4.30%   | 86.85%             | -44.76% |     0.05 | 48.92%     | ok               |
| MRK        |       69 | -30.17%  | -2.15%             | -35.95% |    -0.72 | 44.26%     | ok               |
| MS         |       77 | -10.18%  | 153.13%            | -27.79% |    -0.16 | 49.58%     | ok               |
| MSFT       |       81 | -37.64%  | -2.39%             | -39.15% |    -0.99 | 47.09%     | ok               |
| MU         |       49 | 260.40%  | 956.96%            | -68.76% |     1.32 | 59.57%     | ok               |
| NEAR-USD   |       83 | -14.95%  | -43.63%            | -59.86% |     0.1  | 41.00%     | ok               |
| NEM        |       72 | -31.13%  | 209.75%            | -38.49% |    -0.33 | 53.08%     | ok               |
| NFLX       |       70 | 25.88%   | 14.13%             | -21.09% |     0.58 | 54.24%     | ok               |
| NKE        |       91 | -37.92%  | -59.14%            | -55.35% |    -0.53 | 43.93%     | ok               |
| NOW        |       78 | 8.05%    | -33.48%            | -27.34% |     0.26 | 45.59%     | ok               |
| NVDA       |       75 | -26.95%  | 160.16%            | -45.02% |    -0.19 | 59.89%     | ok               |
| OP-USD     |       72 | -37.37%  | -91.28%            | -71.26% |    -0.22 | 33.91%     | ok               |
| ORCL       |       70 | 121.41%  | 14.07%             | -29.47% |     0.99 | 54.74%     | ok               |
| OXY        |       71 | 3.50%    | -6.77%             | -34.15% |     0.18 | 46.26%     | ok               |
| PEP        |       78 | -1.07%   | -19.72%            | -21.35% |     0.04 | 47.92%     | ok               |
| PEPE-USD   |       81 | 4.00%    | -70.47%            | -57.66% |     0.31 | 45.59%     | ok               |
| PFE        |       79 | -41.51%  | -7.25%             | -42.34% |    -1.34 | 36.11%     | ok               |
| PG         |       68 | -19.04%  | -7.03%             | -24.55% |    -0.72 | 39.60%     | ok               |
| PM         |       81 | -3.41%   | 108.52%            | -33.68% |     0.02 | 55.57%     | ok               |
| POL-USD    |       75 | 26.61%   | -75.44%            | -46.45% |     0.48 | 48.28%     | ok               |
| QCOM       |       73 | -15.25%  | 9.60%              | -56.59% |    -0.04 | 46.09%     | ok               |
| QQQ        |       60 | 20.33%   | 62.01%             | -12.88% |     0.58 | 43.59%     | ok               |
| RENDER-USD |       98 | -19.07%  | -63.53%            | -45.00% |     0.1  | 42.36%     | ok               |
| RTX        |       56 | 25.51%   | 114.19%            | -16.99% |     0.63 | 52.25%     | ok               |
| SBUX       |       62 | -18.75%  | 10.96%             | -29.22% |    -0.34 | 39.77%     | ok               |
| SCHW       |       74 | -14.97%  | 52.96%             | -31.92% |    -0.29 | 48.25%     | ok               |
| SHIB-USD   |       74 | -29.98%  | -73.45%            | -47.96% |    -0.2  | 51.72%     | ok               |
| SHY        |       48 | -2.24%   | 0.34%              | -2.85%  |    -0.79 | 34.28%     | ok               |
| SKY-USD    |       74 | -29.86%  | 7.85%              | -44.74% |    -0.36 | 40.87%     | ok               |
| SLB        |       73 | -24.35%  | -3.86%             | -54.23% |    -0.4  | 50.92%     | ok               |
| SLV        |       60 | 43.20%   | 158.05%            | -42.66% |     0.63 | 43.76%     | ok               |
| SMH        |       48 | 78.23%   | 178.48%            | -33.99% |     1.07 | 47.25%     | ok               |
| SNX-USD    |       60 | -21.23%  | -76.75%            | -34.76% |     0.01 | 38.12%     | ok               |
| SOL-USD    |       70 | -36.02%  | -58.53%            | -56.90% |    -0.14 | 59.96%     | ok               |
| SOXX       |       57 | 68.86%   | 158.22%            | -41.89% |     0.93 | 46.09%     | ok               |
| SPY        |       64 | 1.99%    | 47.61%             | -16.47% |     0.13 | 49.58%     | ok               |
| SUSHI-USD  |      100 | -82.36%  | -81.06%            | -85.83% |    -1.31 | 36.97%     | ok               |
| T          |       64 | 37.51%   | 32.26%             | -17.01% |     0.84 | 53.24%     | ok               |
| TGT        |       60 | -12.46%  | -8.89%             | -40.57% |    -0.18 | 38.44%     | ok               |
| TIA-USD    |       93 | -45.37%  | -88.07%            | -68.36% |    -0.32 | 37.16%     | ok               |
| TLT        |       72 | -20.91%  | -9.98%             | -21.87% |    -1.61 | 32.78%     | ok               |
| TMO        |       61 | 16.14%   | -7.54%             | -18.85% |     0.41 | 51.58%     | ok               |
| TMUS       |       70 | 6.02%    | 15.89%             | -25.71% |     0.22 | 47.59%     | ok               |
| TRX-USD    |       68 | 7.33%    | 35.51%             | -22.90% |     0.28 | 48.66%     | ok               |
| TSLA       |       70 | -14.59%  | 89.72%             | -54.91% |     0.05 | 41.26%     | ok               |
| TXN        |       73 | -13.33%  | 76.61%             | -47.39% |    -0.06 | 52.41%     | ok               |
| UNH        |       74 | 34.96%   | -15.01%            | -26.96% |     0.57 | 52.58%     | ok               |
| UNI-USD    |       86 | -71.03%  | -61.62%            | -80.61% |    -0.82 | 44.83%     | ok               |
| UPS        |       72 | -35.38%  | -21.54%            | -38.83% |    -0.69 | 39.43%     | ok               |
| USO        |       68 | 15.63%   | 74.48%             | -43.35% |     0.36 | 34.44%     | ok               |
| VEA        |       58 | -0.94%   | 44.32%             | -17.93% |     0.01 | 43.76%     | ok               |
| VIXY       |       96 | -80.86%  | -61.66%            | -88.16% |    -1.03 | 32.78%     | ok               |
| VNQ        |       71 | -15.77%  | 18.50%             | -24.92% |    -0.66 | 36.94%     | ok               |
| VTI        |       70 | -4.74%   | 46.64%             | -18.77% |    -0.11 | 49.92%     | ok               |
| VWO        |       78 | -14.72%  | 41.59%             | -25.20% |    -0.52 | 43.43%     | ok               |
| VZ         |       83 | -27.34%  | 9.64%              | -27.34% |    -0.92 | 37.44%     | ok               |
| WFC        |       84 | -17.30%  | 60.08%             | -30.87% |    -0.28 | 50.75%     | ok               |
| WIF-USD    |       70 | -35.62%  | -76.66%            | -51.39% |    -0.13 | 33.33%     | ok               |
| WMT        |       63 | 12.26%   | 85.25%             | -21.31% |     0.4  | 50.25%     | ok               |
| XBI        |       66 | -9.78%   | 50.16%             | -18.71% |    -0.17 | 40.93%     | ok               |
| XLB        |       62 | -8.25%   | 15.66%             | -24.41% |    -0.26 | 36.44%     | ok               |
| XLC        |       69 | 11.05%   | 38.93%             | -12.33% |     0.42 | 53.74%     | ok               |
| XLE        |       75 | -6.70%   | 36.22%             | -37.64% |    -0.09 | 45.26%     | ok               |
| XLF        |       76 | -12.08%  | 39.54%             | -23.61% |    -0.4  | 47.92%     | ok               |
| XLI        |       66 | -2.72%   | 48.61%             | -11.79% |    -0.06 | 43.76%     | ok               |
| XLK        |       40 | 65.83%   | 75.80%             | -14.75% |     1.22 | 45.59%     | ok               |
| XLM-USD    |       69 | 5.21%    | -44.12%            | -50.36% |     0.28 | 45.79%     | ok               |
| XLP        |       66 | 4.67%    | 12.85%             | -11.16% |     0.3  | 41.26%     | ok               |
| XLU        |       67 | -5.24%   | 45.16%             | -20.40% |    -0.19 | 39.10%     | ok               |
| XLV        |       68 | -15.87%  | 9.21%              | -19.97% |    -0.78 | 35.94%     | ok               |
| XLY        |       70 | 3.95%    | 25.92%             | -14.01% |     0.19 | 44.59%     | ok               |
| XOM        |       57 | 9.09%    | 45.83%             | -20.29% |     0.32 | 37.10%     | ok               |
| XRP-USD    |       58 | -30.47%  | -58.19%            | -44.89% |    -0.26 | 33.72%     | ok               |
| YFI-USD    |       81 | -64.19%  | -63.90%            | -71.12% |    -1.03 | 40.61%     | ok               |
| ZEC-USD    |       64 | 42.98%   | 1438.81%           | -47.68% |     0.55 | 36.78%     | ok               |

## AAPL Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 28.00%   | 79.46%             | -21.71% |     0.59 |       68 | 53.41%     | ok               |
|          15 | 24.06%   | 79.46%             | -23.86% |     0.52 |       75 | 60.57%     | ok               |
|          30 | 18.73%   | 79.46%             | -20.65% |     0.45 |       61 | 49.25%     | ok               |
|          35 | 16.06%   | 79.46%             | -22.04% |     0.41 |       61 | 47.75%     | ok               |
|          25 | 16.25%   | 79.46%             | -20.03% |     0.41 |       67 | 51.08%     | ok               |

## AAVE-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 18.81%   | -61.98%            | -43.61% |     0.41 |       40 | 31.80%     | ok               |
|          45 | 2.92%    | -61.98%            | -49.19% |     0.24 |       44 | 27.01%     | ok               |
|          35 | -1.51%   | -61.98%            | -51.96% |     0.21 |       50 | 35.06%     | ok               |
|          15 | -51.84%  | -61.98%            | -61.76% |    -0.32 |       82 | 54.02%     | ok               |
|          50 | -33.87%  | -61.98%            | -47.39% |    -0.36 |       42 | 19.73%     | ok               |

## ABBV Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -12.99%  | 43.08%             | -28.51% |    -0.27 |       50 | 36.27%     | ok               |
|          30 | -20.42%  | 43.08%             | -30.55% |    -0.43 |       66 | 47.09%     | ok               |
|          25 | -21.34%  | 43.08%             | -31.26% |    -0.45 |       69 | 48.75%     | ok               |
|          20 | -21.94%  | 43.08%             | -30.60% |    -0.46 |       69 | 50.58%     | ok               |
|          40 | -20.16%  | 43.08%             | -26.61% |    -0.46 |       66 | 40.93%     | ok               |

## ADA-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -78.05%  | -77.48%            | -86.04% |    -0.6  |       55 | 27.01%     | ok               |
|          45 | -80.39%  | -77.48%            | -88.08% |    -0.63 |       58 | 31.80%     | ok               |
|          35 | -82.82%  | -77.48%            | -89.83% |    -0.67 |       78 | 42.53%     | ok               |
|          30 | -83.04%  | -77.48%            | -89.12% |    -0.67 |       90 | 46.93%     | ok               |
|          15 | -86.96%  | -77.48%            | -91.11% |    -0.72 |       78 | 63.41%     | ok               |

## ADBE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 1.24%    | -58.88%            | -22.53% |     0.14 |       72 | 49.08%     | ok               |
|          40 | -11.88%  | -58.88%            | -24.87% |    -0.11 |       70 | 42.10%     | ok               |
|          25 | -17.19%  | -58.88%            | -31.11% |    -0.12 |       48 | 61.23%     | ok               |
|          20 | -27.76%  | -58.88%            | -32.14% |    -0.3  |       50 | 63.89%     | ok               |
|          15 | -31.05%  | -58.88%            | -33.12% |    -0.36 |       59 | 65.72%     | ok               |

## AGG Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -6.67%   | 0.76%              | -10.25% |    -1.1  |       71 | 32.11%     | ok               |
|          20 | -7.75%   | 0.76%              | -11.14% |    -1.13 |       75 | 37.77%     | ok               |
|          50 | -5.15%   | 0.76%              | -7.92%  |    -1.14 |       48 | 17.30%     | ok               |
|          45 | -5.80%   | 0.76%              | -7.91%  |    -1.16 |       54 | 21.46%     | ok               |
|          25 | -7.93%   | 0.76%              | -11.78% |    -1.2  |       75 | 36.11%     | ok               |

## ALGO-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -50.43%  | -69.39%            | -53.13% |    -0.57 |       86 | 38.12%     | ok               |
|          15 | -61.64%  | -69.39%            | -68.50% |    -0.67 |       84 | 50.38%     | ok               |
|          25 | -61.89%  | -69.39%            | -72.48% |    -0.74 |       84 | 45.02%     | ok               |
|          20 | -65.54%  | -69.39%            | -71.20% |    -0.8  |       86 | 48.08%     | ok               |
|          50 | -45.64%  | -69.39%            | -48.43% |    -0.81 |       42 | 16.86%     | ok               |

## AMAT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -23.97%  | 178.30%            | -54.05% |    -0.1  |       68 | 60.90%     | ok               |
|          30 | -35.42%  | 178.30%            | -57.21% |    -0.33 |       71 | 51.91%     | ok               |
|          35 | -35.88%  | 178.30%            | -55.26% |    -0.35 |       73 | 49.58%     | ok               |
|          50 | -35.73%  | 178.30%            | -48.72% |    -0.4  |       52 | 37.44%     | ok               |
|          20 | -42.83%  | 178.30%            | -60.16% |    -0.43 |       74 | 57.24%     | ok               |

## AMD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 6.74%    | 205.86%            | -44.26% |     0.27 |       54 | 30.62%     | ok               |
|          40 | 5.86%    | 205.86%            | -43.98% |     0.27 |       52 | 35.77%     | ok               |
|          35 | -5.47%   | 205.86%            | -50.71% |     0.16 |       60 | 37.27%     | ok               |
|          45 | -14.79%  | 205.86%            | -53.24% |     0.04 |       60 | 33.44%     | ok               |
|          30 | -17.93%  | 205.86%            | -56.46% |     0.02 |       61 | 39.77%     | ok               |

## AMGN Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -11.92%  | 31.51%             | -26.64% |    -0.18 |       69 | 52.08%     | ok               |
|          35 | -11.27%  | 31.51%             | -31.23% |    -0.18 |       65 | 42.43%     | ok               |
|          15 | -16.50%  | 31.51%             | -27.92% |    -0.27 |       68 | 57.40%     | ok               |
|          30 | -15.41%  | 31.51%             | -34.14% |    -0.29 |       69 | 46.26%     | ok               |
|          25 | -18.85%  | 31.51%             | -33.41% |    -0.37 |       65 | 48.59%     | ok               |

## AMZN Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -17.42%  | 42.65%             | -27.15% |    -0.51 |       52 | 29.12%     | ok               |
|          50 | -23.79%  | 42.65%             | -34.08% |    -0.85 |       50 | 23.13%     | ok               |
|          45 | -26.60%  | 42.65%             | -34.08% |    -0.93 |       54 | 26.12%     | ok               |
|          35 | -31.00%  | 42.65%             | -38.29% |    -0.97 |       68 | 32.78%     | ok               |
|          30 | -37.14%  | 42.65%             | -42.48% |    -1.11 |       80 | 38.27%     | ok               |

## APT-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 19.10%   | -89.53%            | -46.73% |     0.42 |       40 | 18.97%     | ok               |
|          45 | -11.65%  | -89.53%            | -63.86% |     0.05 |       56 | 24.52%     | ok               |
|          20 | -37.52%  | -89.53%            | -70.51% |    -0.14 |       71 | 50.57%     | ok               |
|          40 | -30.72%  | -89.53%            | -63.33% |    -0.17 |       64 | 29.89%     | ok               |
|          35 | -35.79%  | -89.53%            | -64.09% |    -0.21 |       68 | 35.63%     | ok               |

## ARB-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 26.19%   | -81.11%            | -53.74% |     0.48 |       87 | 57.09%     | ok               |
|          40 | 11.74%   | -81.11%            | -43.98% |     0.34 |       52 | 30.65%     | ok               |
|          20 | -5.17%   | -81.11%            | -58.76% |     0.23 |       75 | 50.57%     | ok               |
|          45 | 0.22%    | -81.11%            | -47.43% |     0.21 |       58 | 23.95%     | ok               |
|          35 | -2.34%   | -81.11%            | -54.43% |     0.2  |       64 | 33.91%     | ok               |

## ARKK Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -32.55%  | 50.75%             | -37.76% |    -0.45 |       94 | 51.41%     | ok               |
|          20 | -36.53%  | 50.75%             | -37.99% |    -0.57 |       89 | 46.76%     | ok               |
|          30 | -36.50%  | 50.75%             | -37.96% |    -0.67 |       85 | 39.93%     | ok               |
|          35 | -36.86%  | 50.75%             | -38.31% |    -0.71 |       84 | 37.44%     | ok               |
|          40 | -38.19%  | 50.75%             | -39.61% |    -0.79 |       76 | 32.61%     | ok               |

## ATOM-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -69.19%  | -68.80%            | -70.03% |    -1.02 |       93 | 61.49%     | ok               |
|          25 | -66.29%  | -68.80%            | -71.00% |    -1.02 |       93 | 50.96%     | ok               |
|          45 | -58.00%  | -68.80%            | -64.33% |    -1.08 |       72 | 28.74%     | ok               |
|          30 | -69.66%  | -68.80%            | -74.39% |    -1.22 |       86 | 44.25%     | ok               |
|          20 | -73.46%  | -68.80%            | -74.75% |    -1.24 |       97 | 54.60%     | ok               |

## AVAX-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 3.29%    | -73.48%            | -34.50% |     0.21 |       32 | 18.20%     | ok               |
|          45 | -6.13%   | -73.48%            | -41.07% |     0.07 |       36 | 22.03%     | ok               |
|          40 | -15.98%  | -73.48%            | -45.60% |    -0.06 |       40 | 24.90%     | ok               |
|          15 | -28.72%  | -73.48%            | -52.46% |    -0.08 |       73 | 53.07%     | ok               |
|          25 | -28.09%  | -73.48%            | -52.93% |    -0.14 |       69 | 42.34%     | ok               |

## AVGO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 16.61%   | 198.17%            | -35.84% |     0.36 |       56 | 30.62%     | ok               |
|          30 | 15.13%   | 198.17%            | -35.76% |     0.34 |       64 | 42.26%     | ok               |
|          40 | 13.75%   | 198.17%            | -40.70% |     0.33 |       62 | 36.11%     | ok               |
|          25 | 12.71%   | 198.17%            | -38.01% |     0.32 |       72 | 43.76%     | ok               |
|          45 | 11.86%   | 198.17%            | -41.66% |     0.31 |       56 | 33.94%     | ok               |

## BA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 26.03%   | 1.69%              | -13.34% |     0.67 |       42 | 31.45%     | ok               |
|          35 | 30.46%   | 1.69%              | -23.77% |     0.59 |       72 | 44.59%     | ok               |
|          40 | 20.11%   | 1.69%              | -23.90% |     0.47 |       46 | 38.60%     | ok               |
|          25 | 10.59%   | 1.69%              | -32.48% |     0.29 |       70 | 52.58%     | ok               |
|          30 | 7.60%    | 1.69%              | -30.56% |     0.25 |       67 | 49.25%     | ok               |

## BAC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 4.19%    | 78.59%             | -19.60% |     0.19 |       62 | 38.27%     | ok               |
|          35 | 0.22%    | 78.59%             | -27.11% |     0.08 |       70 | 46.26%     | ok               |
|          20 | -0.43%   | 78.59%             | -20.73% |     0.08 |       78 | 54.74%     | ok               |
|          50 | -1.60%   | 78.59%             | -20.35% |     0.01 |       62 | 34.78%     | ok               |
|          40 | -3.07%   | 78.59%             | -23.77% |    -0.02 |       66 | 41.26%     | ok               |

## BCH-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -1.94%   | -30.98%            | -48.11% |     0.21 |       73 | 54.41%     | ok               |
|          15 | -5.01%   | -30.98%            | -52.32% |     0.18 |       80 | 59.00%     | ok               |
|          25 | -14.11%  | -30.98%            | -54.62% |     0.05 |       70 | 50.57%     | ok               |
|          30 | -13.59%  | -30.98%            | -54.34% |     0.05 |       78 | 48.47%     | ok               |
|          35 | -26.15%  | -30.98%            | -64.08% |    -0.15 |       70 | 44.44%     | ok               |

## BITO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 8.25%    | -66.54%            | -31.98% |     0.26 |       52 | 24.13%     | ok               |
|          30 | -9.90%   | -66.54%            | -42.82% |     0.05 |       80 | 40.93%     | ok               |
|          45 | -8.94%   | -66.54%            | -41.96% |     0.03 |       60 | 27.79%     | ok               |
|          15 | -16.54%  | -66.54%            | -48.38% |     0.01 |       89 | 49.92%     | ok               |
|          40 | -13.00%  | -66.54%            | -44.44% |    -0.01 |       64 | 32.61%     | ok               |

## BLK Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | -2.85%   | 29.69%             | -19.23% |    -0.02 |       78 | 38.77%     | ok               |
|          20 | -4.92%   | 29.69%             | -21.48% |    -0.06 |       78 | 47.42%     | ok               |
|          40 | -6.45%   | 29.69%             | -21.31% |    -0.15 |       72 | 34.78%     | ok               |
|          30 | -9.01%   | 29.69%             | -25.46% |    -0.2  |       73 | 42.60%     | ok               |
|          25 | -9.93%   | 29.69%             | -24.54% |    -0.22 |       73 | 44.93%     | ok               |

## BND Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -6.22%   | 0.80%              | -9.15%  |    -0.9  |       65 | 39.10%     | ok               |
|          25 | -6.92%   | 0.80%              | -10.23% |    -1.05 |       69 | 37.10%     | ok               |
|          30 | -7.37%   | 0.80%              | -9.98%  |    -1.18 |       67 | 33.28%     | ok               |
|          15 | -8.44%   | 0.80%              | -10.93% |    -1.21 |       75 | 41.93%     | ok               |
|          45 | -7.61%   | 0.80%              | -9.57%  |    -1.46 |       52 | 22.96%     | ok               |

## BONK-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 170.82%  | -82.38%            | -35.57% |     1.24 |       46 | 22.22%     | ok               |
|          25 | 167.57%  | -82.38%            | -47.99% |     1.03 |       67 | 48.66%     | ok               |
|          20 | 152.46%  | -82.38%            | -55.43% |     0.98 |       68 | 53.26%     | ok               |
|          15 | 158.24%  | -82.38%            | -63.45% |     0.97 |       71 | 58.24%     | ok               |
|          40 | 99.24%   | -82.38%            | -50.07% |     0.87 |       52 | 34.10%     | ok               |

## BTC-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 46.18%   | -31.08%            | -14.53% |     0.84 |       46 | 34.87%     | ok               |
|          45 | 40.84%   | -31.08%            | -15.18% |     0.81 |       44 | 30.65%     | ok               |
|          35 | 28.81%   | -31.08%            | -26.34% |     0.58 |       70 | 41.76%     | ok               |
|          50 | 13.98%   | -31.08%            | -18.05% |     0.4  |       42 | 25.29%     | ok               |
|          30 | 13.35%   | -31.08%            | -21.75% |     0.35 |       74 | 48.47%     | ok               |

## C Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -6.29%   | 138.45%            | -22.28% |    -0.1  |       64 | 36.11%     | ok               |
|          45 | -18.56%  | 138.45%            | -30.30% |    -0.43 |       76 | 40.27%     | ok               |
|          25 | -27.05%  | 138.45%            | -34.97% |    -0.5  |       71 | 52.91%     | ok               |
|          15 | -29.52%  | 138.45%            | -36.36% |    -0.53 |       74 | 59.90%     | ok               |
|          20 | -29.49%  | 138.45%            | -36.33% |    -0.55 |       79 | 55.91%     | ok               |

## CAT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 20.42%   | 171.64%            | -21.02% |     0.43 |       72 | 55.41%     | ok               |
|          25 | 20.53%   | 171.64%            | -26.37% |     0.43 |       68 | 58.24%     | ok               |
|          20 | 19.09%   | 171.64%            | -25.65% |     0.41 |       78 | 61.73%     | ok               |
|          45 | 15.49%   | 171.64%            | -27.12% |     0.37 |       56 | 44.09%     | ok               |
|          35 | 12.51%   | 171.64%            | -27.72% |     0.32 |       70 | 48.92%     | ok               |

## CL Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 10.05%   | 4.73%              | -11.22% |     0.44 |       44 | 29.28%     | ok               |
|          30 | 7.40%    | 4.73%              | -14.32% |     0.3  |       62 | 45.42%     | ok               |
|          45 | 2.94%    | 4.73%              | -13.51% |     0.17 |       48 | 32.45%     | ok               |
|          35 | 2.29%    | 4.73%              | -13.83% |     0.14 |       64 | 41.76%     | ok               |
|          40 | -0.68%   | 4.73%              | -12.70% |     0.03 |       58 | 36.44%     | ok               |

## CMCSA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -37.55%  | -39.90%            | -44.10% |    -0.84 |       90 | 56.74%     | ok               |
|          30 | -39.28%  | -39.90%            | -41.06% |    -1.04 |       81 | 41.76%     | ok               |
|          25 | -43.02%  | -39.90%            | -43.52% |    -1.15 |       90 | 47.09%     | ok               |
|          50 | -30.68%  | -39.90%            | -32.53% |    -1.22 |       50 | 14.31%     | ok               |
|          35 | -44.09%  | -39.90%            | -45.72% |    -1.28 |       91 | 36.27%     | ok               |

## COMP-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -4.94%   | -68.40%            | -38.71% |     0.13 |       44 | 20.11%     | ok               |
|          30 | -42.29%  | -68.40%            | -57.88% |    -0.3  |       91 | 45.79%     | ok               |
|          25 | -46.81%  | -68.40%            | -61.30% |    -0.34 |       91 | 52.11%     | ok               |
|          40 | -44.69%  | -68.40%            | -50.69% |    -0.45 |       72 | 33.52%     | ok               |
|          15 | -55.80%  | -68.40%            | -66.20% |    -0.46 |      109 | 63.60%     | ok               |

## COP Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -2.72%   | 5.28%              | -34.85% |     0.03 |       48 | 28.29%     | ok               |
|          35 | -16.06%  | 5.28%              | -43.58% |    -0.25 |       73 | 38.77%     | ok               |
|          45 | -14.21%  | 5.28%              | -41.14% |    -0.25 |       62 | 31.61%     | ok               |
|          30 | -20.42%  | 5.28%              | -43.96% |    -0.34 |       72 | 42.26%     | ok               |
|          40 | -19.63%  | 5.28%              | -46.86% |    -0.38 |       68 | 34.78%     | ok               |

## COST Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 8.69%    | 24.78%             | -24.32% |     0.31 |       66 | 49.58%     | ok               |
|          25 | 7.08%    | 24.78%             | -24.73% |     0.27 |       63 | 46.76%     | ok               |
|          35 | 2.10%    | 24.78%             | -26.58% |     0.13 |       54 | 40.10%     | ok               |
|          30 | -2.58%   | 24.78%             | -29.73% |    -0.01 |       60 | 43.09%     | ok               |
|          15 | -5.51%   | 24.78%             | -27.30% |    -0.07 |       69 | 53.08%     | ok               |

## CRM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -35.79%  | -43.22%            | -44.67% |    -0.57 |       90 | 54.91%     | ok               |
|          35 | -29.63%  | -43.22%            | -33.08% |    -0.59 |       60 | 37.94%     | ok               |
|          40 | -34.83%  | -43.22%            | -39.11% |    -0.8  |       66 | 33.94%     | ok               |
|          20 | -43.35%  | -43.22%            | -45.69% |    -0.82 |       74 | 48.59%     | ok               |
|          30 | -39.56%  | -43.22%            | -41.36% |    -0.83 |       63 | 42.76%     | ok               |

## CRV-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 17.10%   | -58.06%            | -37.78% |     0.39 |       72 | 31.99%     | ok               |
|          45 | 2.75%    | -58.06%            | -42.29% |     0.23 |       58 | 21.26%     | ok               |
|          40 | -2.98%   | -58.06%            | -38.86% |     0.18 |       62 | 27.59%     | ok               |
|          50 | -1.11%   | -58.06%            | -29.30% |     0.17 |       48 | 17.62%     | ok               |
|          30 | -7.01%   | -58.06%            | -39.89% |     0.16 |       70 | 36.59%     | ok               |

## CSCO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 32.24%   | 132.21%            | -19.34% |     0.7  |       52 | 37.10%     | ok               |
|          45 | 28.30%   | 132.21%            | -19.34% |     0.62 |       51 | 38.94%     | ok               |
|          35 | 24.49%   | 132.21%            | -23.68% |     0.53 |       53 | 45.92%     | ok               |
|          25 | 22.81%   | 132.21%            | -23.28% |     0.5  |       65 | 50.58%     | ok               |
|          30 | 22.24%   | 132.21%            | -21.79% |     0.49 |       61 | 48.59%     | ok               |

## CVX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -7.34%   | 25.57%             | -27.34% |    -0.16 |       75 | 34.78%     | ok               |
|          25 | -9.17%   | 25.57%             | -24.33% |    -0.17 |       73 | 42.26%     | ok               |
|          45 | -8.55%   | 25.57%             | -28.83% |    -0.2  |       65 | 30.95%     | ok               |
|          35 | -9.49%   | 25.57%             | -28.85% |    -0.2  |       67 | 36.94%     | ok               |
|          50 | -9.07%   | 25.57%             | -30.69% |    -0.27 |       58 | 26.29%     | ok               |

## DASH-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 98.06%   | 29.05%             | -27.84% |     0.84 |       38 | 15.13%     | ok               |
|          40 | 58.92%   | 29.05%             | -31.16% |     0.64 |       44 | 21.84%     | ok               |
|          45 | 42.80%   | 29.05%             | -36.57% |     0.55 |       42 | 17.24%     | ok               |
|          35 | -38.60%  | 29.05%             | -63.23% |     0.01 |       67 | 26.25%     | ok               |
|          30 | -41.76%  | 29.05%             | -64.43% |    -0.02 |       61 | 29.12%     | ok               |

## DBC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -4.61%   | 33.74%             | -27.07% |    -0.1  |       74 | 39.43%     | ok               |
|          50 | -3.74%   | 33.74%             | -20.31% |    -0.1  |       42 | 22.13%     | ok               |
|          45 | -6.40%   | 33.74%             | -21.46% |    -0.2  |       58 | 25.79%     | ok               |
|          35 | -7.21%   | 33.74%             | -23.91% |    -0.21 |       64 | 32.61%     | ok               |
|          25 | -7.67%   | 33.74%             | -26.10% |    -0.22 |       64 | 35.77%     | ok               |

## DE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -6.02%   | 62.72%             | -23.24% |    -0.08 |       70 | 31.78%     | ok               |
|          20 | -8.63%   | 62.72%             | -29.90% |    -0.08 |       76 | 52.41%     | ok               |
|          45 | -7.95%   | 62.72%             | -26.90% |    -0.11 |       70 | 36.27%     | ok               |
|          30 | -9.70%   | 62.72%             | -25.24% |    -0.11 |       74 | 47.09%     | ok               |
|          25 | -10.89%  | 62.72%             | -27.66% |    -0.14 |       78 | 49.75%     | ok               |

## DIA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | -1.98%   | 33.84%             | -13.15% |    -0.07 |       62 | 41.60%     | ok               |
|          25 | -2.51%   | 33.84%             | -11.28% |    -0.1  |       62 | 44.93%     | ok               |
|          30 | -4.01%   | 33.84%             | -12.94% |    -0.18 |       62 | 43.76%     | ok               |
|          20 | -5.84%   | 33.84%             | -13.85% |    -0.27 |       66 | 47.25%     | ok               |
|          40 | -5.97%   | 33.84%             | -15.06% |    -0.32 |       68 | 38.77%     | ok               |

## DIS Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 19.08%   | -12.14%            | -14.24% |     0.6  |       48 | 26.96%     | ok               |
|          40 | -8.28%   | -12.14%            | -24.07% |    -0.1  |       65 | 36.11%     | ok               |
|          45 | -7.44%   | -12.14%            | -16.54% |    -0.1  |       53 | 30.95%     | ok               |
|          15 | -15.25%  | -12.14%            | -31.15% |    -0.2  |       91 | 56.91%     | ok               |
|          35 | -15.19%  | -12.14%            | -25.70% |    -0.26 |       75 | 42.43%     | ok               |

## DOGE-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 5.04%    | -72.40%            | -59.36% |     0.33 |       80 | 65.90%     | ok               |
|          20 | -9.55%   | -72.40%            | -57.37% |     0.18 |       79 | 60.34%     | ok               |
|          25 | -10.38%  | -72.40%            | -55.33% |     0.17 |       69 | 55.36%     | ok               |
|          30 | -25.02%  | -72.40%            | -62.31% |    -0.01 |       72 | 49.81%     | ok               |
|          35 | -49.12%  | -72.40%            | -63.16% |    -0.45 |       68 | 43.30%     | ok               |

## DOT-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -35.10%  | -82.47%            | -46.87% |    -0.45 |       58 | 25.67%     | ok               |
|          45 | -37.93%  | -82.47%            | -50.16% |    -0.46 |       50 | 30.84%     | ok               |
|          35 | -52.94%  | -82.47%            | -60.35% |    -0.53 |       74 | 41.19%     | ok               |
|          40 | -44.16%  | -82.47%            | -51.87% |    -0.55 |       52 | 33.91%     | ok               |
|          30 | -57.70%  | -82.47%            | -63.10% |    -0.61 |       84 | 47.51%     | ok               |

## DXY-INDEX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -2.03%   | 0.53%              | -6.28%  |    -0.3  |       40 | 31.02%     | ok               |
|          15 | -3.71%   | 0.53%              | -11.37% |    -0.32 |       82 | 77.01%     | ok               |
|          40 | -4.35%   | 0.53%              | -7.30%  |    -0.55 |       72 | 50.33%     | ok               |
|          35 | -5.44%   | 0.53%              | -9.74%  |    -0.66 |       75 | 56.83%     | ok               |
|          30 | -5.83%   | 0.53%              | -9.61%  |    -0.67 |       74 | 61.39%     | ok               |

## EEM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -5.81%   | 61.33%             | -19.52% |    -0.14 |       64 | 38.94%     | ok               |
|          35 | -6.46%   | 61.33%             | -23.88% |    -0.15 |       66 | 40.93%     | ok               |
|          50 | -5.79%   | 61.33%             | -15.88% |    -0.15 |       52 | 34.94%     | ok               |
|          45 | -6.87%   | 61.33%             | -17.36% |    -0.19 |       54 | 36.61%     | ok               |
|          30 | -10.20%  | 61.33%             | -25.67% |    -0.28 |       64 | 42.60%     | ok               |

## EFA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -3.18%   | 34.27%             | -10.80% |    -0.05 |       62 | 52.08%     | ok               |
|          20 | -9.89%   | 34.27%             | -12.73% |    -0.34 |       69 | 49.08%     | ok               |
|          30 | -9.51%   | 34.27%             | -14.87% |    -0.35 |       62 | 44.26%     | ok               |
|          50 | -9.19%   | 34.27%             | -17.56% |    -0.41 |       54 | 35.94%     | ok               |
|          25 | -11.74%  | 34.27%             | -16.11% |    -0.44 |       64 | 46.26%     | ok               |

## EOG Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -20.15%  | 25.89%             | -48.13% |    -0.39 |       81 | 47.59%     | ok               |
|          40 | -20.26%  | 25.89%             | -43.26% |    -0.45 |       66 | 37.10%     | ok               |
|          35 | -21.04%  | 25.89%             | -46.26% |    -0.45 |       79 | 42.26%     | ok               |
|          25 | -24.21%  | 25.89%             | -51.99% |    -0.48 |       82 | 50.58%     | ok               |
|          45 | -20.14%  | 25.89%             | -43.17% |    -0.48 |       60 | 33.61%     | ok               |

## ETC-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 1.95%    | -65.71%            | -27.89% |     0.16 |       24 | 15.71%     | ok               |
|          45 | -8.31%   | -65.71%            | -35.44% |    -0.02 |       24 | 17.43%     | ok               |
|          35 | -11.42%  | -65.71%            | -42.62% |    -0.05 |       42 | 25.10%     | ok               |
|          40 | -15.42%  | -65.71%            | -40.48% |    -0.15 |       38 | 21.07%     | ok               |
|          30 | -33.00%  | -65.71%            | -45.54% |    -0.46 |       64 | 29.31%     | ok               |

## ETH-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 146.12%  | -27.49%            | -30.11% |     1.23 |       62 | 44.83%     | ok               |
|          30 | 110.73%  | -27.49%            | -32.89% |     1.02 |       66 | 53.45%     | ok               |
|          40 | 42.93%   | -27.49%            | -33.11% |     0.64 |       60 | 37.16%     | ok               |
|          15 | 44.73%   | -27.49%            | -42.74% |     0.61 |       77 | 68.77%     | ok               |
|          20 | 43.19%   | -27.49%            | -39.10% |     0.6  |       82 | 63.03%     | ok               |

## EWJ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -19.80%  | 34.06%             | -30.73% |    -0.66 |       62 | 38.44%     | ok               |
|          20 | -21.16%  | 34.06%             | -31.32% |    -0.69 |       58 | 40.43%     | ok               |
|          25 | -23.44%  | 34.06%             | -31.18% |    -0.79 |       58 | 39.43%     | ok               |
|          45 | -20.57%  | 34.06%             | -27.68% |    -0.8  |       58 | 30.62%     | ok               |
|          35 | -23.65%  | 34.06%             | -32.54% |    -0.82 |       68 | 36.77%     | ok               |

## FCX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -1.08%   | 63.94%             | -26.57% |     0.11 |       52 | 29.95%     | ok               |
|          45 | -5.34%   | 63.94%             | -32.99% |     0.05 |       52 | 34.44%     | ok               |
|          40 | -17.80%  | 63.94%             | -42.49% |    -0.16 |       64 | 38.60%     | ok               |
|          30 | -28.83%  | 63.94%             | -48.22% |    -0.34 |       65 | 45.09%     | ok               |
|          35 | -33.22%  | 63.94%             | -51.41% |    -0.44 |       71 | 43.26%     | ok               |

## FET-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -2.53%   | -79.86%            | -59.54% |     0.29 |       88 | 53.26%     | ok               |
|          15 | -17.09%  | -79.86%            | -59.58% |     0.18 |       84 | 57.09%     | ok               |
|          25 | -36.23%  | -79.86%            | -60.09% |    -0.07 |       91 | 46.93%     | ok               |
|          30 | -39.88%  | -79.86%            | -54.02% |    -0.15 |       85 | 42.34%     | ok               |
|          35 | -54.23%  | -79.86%            | -62.73% |    -0.51 |       73 | 34.10%     | ok               |

## FIL-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -23.47%  | -77.33%            | -39.40% |    -0.21 |       46 | 22.80%     | ok               |
|          35 | -44.88%  | -77.33%            | -47.50% |    -0.62 |       56 | 26.82%     | ok               |
|          30 | -47.73%  | -77.33%            | -50.22% |    -0.63 |       68 | 32.18%     | ok               |
|          45 | -41.18%  | -77.33%            | -43.98% |    -0.65 |       40 | 17.05%     | ok               |
|          50 | -39.00%  | -77.33%            | -44.95% |    -0.69 |       36 | 12.64%     | ok               |

## FXI Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -6.49%   | 42.39%             | -26.75% |    -0.09 |       44 | 24.63%     | ok               |
|          25 | -9.49%   | 42.39%             | -22.99% |    -0.15 |       48 | 31.45%     | ok               |
|          30 | -10.00%  | 42.39%             | -24.33% |    -0.17 |       48 | 30.28%     | ok               |
|          50 | -9.19%   | 42.39%             | -24.76% |    -0.18 |       44 | 21.63%     | ok               |
|          40 | -10.79%  | 42.39%             | -28.38% |    -0.2  |       44 | 26.62%     | ok               |

## GDX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 17.08%   | 185.02%            | -35.59% |     0.37 |       73 | 52.75%     | ok               |
|          40 | 13.85%   | 185.02%            | -31.87% |     0.35 |       64 | 42.93%     | ok               |
|          30 | 11.28%   | 185.02%            | -34.99% |     0.3  |       60 | 48.09%     | ok               |
|          35 | 8.95%    | 185.02%            | -32.37% |     0.27 |       68 | 45.26%     | ok               |
|          25 | 5.89%    | 185.02%            | -38.90% |     0.23 |       63 | 49.58%     | ok               |

## GDXJ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -9.51%   | 206.66%            | -45.05% |     0.04 |       67 | 52.58%     | ok               |
|          50 | -18.94%  | 206.66%            | -44.94% |    -0.2  |       58 | 37.94%     | ok               |
|          30 | -22.87%  | 206.66%            | -44.93% |    -0.21 |       66 | 46.09%     | ok               |
|          25 | -26.91%  | 206.66%            | -47.26% |    -0.26 |       70 | 49.42%     | ok               |
|          35 | -26.51%  | 206.66%            | -43.49% |    -0.29 |       68 | 43.76%     | ok               |

## GE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 28.14%   | 177.22%            | -22.29% |     0.58 |       66 | 39.27%     | ok               |
|          45 | 18.47%   | 177.22%            | -25.68% |     0.43 |       74 | 42.10%     | ok               |
|          20 | 12.23%   | 177.22%            | -26.63% |     0.32 |       71 | 56.41%     | ok               |
|          35 | 8.97%    | 177.22%            | -27.11% |     0.27 |       80 | 47.59%     | ok               |
|          30 | 8.72%    | 177.22%            | -27.82% |     0.27 |       76 | 52.75%     | ok               |

## GLD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 30.39%   | 99.37%             | -14.61% |     0.73 |       48 | 50.75%     | ok               |
|          25 | 29.71%   | 99.37%             | -14.61% |     0.72 |       48 | 49.25%     | ok               |
|          30 | 23.54%   | 99.37%             | -16.63% |     0.6  |       50 | 48.09%     | ok               |
|          15 | 22.41%   | 99.37%             | -17.54% |     0.55 |       50 | 54.91%     | ok               |
|          35 | 17.08%   | 99.37%             | -17.29% |     0.48 |       54 | 46.09%     | ok               |

## GOOGL Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 81.69%   | 149.96%            | -18.25% |     1.23 |       59 | 49.25%     | ok               |
|          30 | 77.30%   | 149.96%            | -20.41% |     1.16 |       57 | 52.75%     | ok               |
|          45 | 68.54%   | 149.96%            | -14.13% |     1.16 |       54 | 42.26%     | ok               |
|          25 | 74.60%   | 149.96%            | -19.76% |     1.12 |       55 | 54.74%     | ok               |
|          50 | 60.60%   | 149.96%            | -14.89% |     1.09 |       48 | 37.27%     | ok               |

## GRT-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 16.20%   | -87.97%            | -35.66% |     0.39 |       42 | 21.46%     | ok               |
|          15 | -6.62%   | -87.97%            | -49.67% |     0.19 |       75 | 60.73%     | ok               |
|          20 | -7.84%   | -87.97%            | -46.47% |     0.16 |       81 | 55.36%     | ok               |
|          35 | -6.92%   | -87.97%            | -48.22% |     0.12 |       60 | 36.21%     | ok               |
|          45 | -6.41%   | -87.97%            | -46.59% |     0.09 |       50 | 27.01%     | ok               |

## GS Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 21.11%   | 177.77%            | -20.56% |     0.47 |       74 | 61.06%     | ok               |
|          20 | 4.59%    | 177.77%            | -23.19% |     0.19 |       74 | 57.07%     | ok               |
|          40 | 0.08%    | 177.77%            | -17.88% |     0.09 |       72 | 45.26%     | ok               |
|          25 | -0.70%   | 177.77%            | -23.32% |     0.09 |       74 | 54.58%     | ok               |
|          30 | -2.38%   | 177.77%            | -22.13% |     0.05 |       76 | 52.08%     | ok               |

## HD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -7.53%   | -11.71%            | -17.69% |    -0.12 |       71 | 44.59%     | ok               |
|          25 | -8.25%   | -11.71%            | -18.51% |    -0.14 |       70 | 46.59%     | ok               |
|          15 | -17.46%  | -11.71%            | -27.27% |    -0.37 |      109 | 55.41%     | ok               |
|          35 | -15.13%  | -11.71%            | -22.98% |    -0.38 |       80 | 40.43%     | ok               |
|          40 | -13.89%  | -11.71%            | -19.63% |    -0.39 |       84 | 34.11%     | ok               |

## HON Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -13.43%  | 17.34%             | -21.17% |    -0.4  |       72 | 31.78%     | ok               |
|          45 | -15.16%  | 17.34%             | -19.99% |    -0.43 |       74 | 36.77%     | ok               |
|          40 | -23.52%  | 17.34%             | -26.29% |    -0.66 |       76 | 41.10%     | ok               |
|          35 | -24.98%  | 17.34%             | -27.37% |    -0.69 |       91 | 47.42%     | ok               |
|          30 | -26.82%  | 17.34%             | -29.80% |    -0.72 |       93 | 52.41%     | ok               |

## HYG Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -7.92%   | 3.17%              | -7.92%  |    -0.96 |       70 | 29.45%     | ok               |
|          15 | -9.95%   | 3.17%              | -10.29% |    -1.08 |       88 | 41.26%     | ok               |
|          20 | -9.69%   | 3.17%              | -10.29% |    -1.08 |       86 | 39.10%     | ok               |
|          45 | -8.60%   | 3.17%              | -8.60%  |    -1.08 |       66 | 26.29%     | ok               |
|          30 | -9.52%   | 3.17%              | -9.59%  |    -1.11 |       81 | 34.28%     | ok               |

## IBIT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 53.73%   | -0.89%             | -17.37% |     1.06 |       22 | 22.17%     | ok               |
|          15 | 56.91%   | -0.89%             | -19.20% |     0.95 |       40 | 39.49%     | ok               |
|          45 | 44.27%   | -0.89%             | -17.37% |     0.9  |       26 | 23.56%     | ok               |
|          40 | 38.04%   | -0.89%             | -17.78% |     0.8  |       26 | 25.40%     | ok               |
|          30 | 30.82%   | -0.89%             | -18.95% |     0.66 |       34 | 31.87%     | ok               |

## IBM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -8.32%   | 13.86%             | -43.33% |     0.03 |       93 | 61.90%     | ok               |
|          30 | -16.57%  | 13.86%             | -44.74% |    -0.14 |       77 | 49.75%     | ok               |
|          20 | -20.24%  | 13.86%             | -48.00% |    -0.18 |       75 | 54.41%     | ok               |
|          35 | -18.72%  | 13.86%             | -44.74% |    -0.19 |       71 | 45.42%     | ok               |
|          25 | -27.62%  | 13.86%             | -51.09% |    -0.33 |       74 | 52.41%     | ok               |

## ICP-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 1.02%    | -68.46%            | -32.85% |     0.21 |       50 | 23.75%     | ok               |
|          35 | -4.60%   | -68.46%            | -39.08% |     0.16 |       58 | 28.54%     | ok               |
|          30 | -17.01%  | -68.46%            | -52.78% |     0.08 |       75 | 34.48%     | ok               |
|          50 | -18.12%  | -68.46%            | -43.65% |    -0.09 |       32 | 14.18%     | ok               |
|          45 | -24.62%  | -68.46%            | -40.57% |    -0.18 |       52 | 18.01%     | ok               |

## IEF Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -7.10%   | -0.41%             | -9.79%  |    -0.85 |       72 | 42.43%     | ok               |
|          15 | -7.65%   | -0.41%             | -10.52% |    -0.9  |       71 | 43.93%     | ok               |
|          40 | -8.57%   | -0.41%             | -9.67%  |    -1.34 |       62 | 24.96%     | ok               |
|          45 | -8.24%   | -0.41%             | -9.73%  |    -1.36 |       52 | 22.96%     | ok               |
|          25 | -10.67%  | -0.41%             | -11.19% |    -1.36 |       78 | 39.60%     | ok               |

## IEMG Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | -3.67%   | 55.67%             | -22.13% |    -0.06 |       63 | 41.10%     | ok               |
|          40 | -4.30%   | 55.67%             | -18.43% |    -0.1  |       60 | 38.60%     | ok               |
|          50 | -4.00%   | 55.67%             | -13.91% |    -0.1  |       54 | 32.78%     | ok               |
|          45 | -4.21%   | 55.67%             | -14.92% |    -0.1  |       50 | 35.44%     | ok               |
|          25 | -7.92%   | 55.67%             | -25.58% |    -0.21 |       59 | 43.93%     | ok               |

## INJ-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -12.38%  | -63.81%            | -55.31% |     0.03 |       46 | 22.80%     | ok               |
|          35 | -18.08%  | -63.81%            | -60.42% |     0.02 |       62 | 32.95%     | ok               |
|          50 | -21.91%  | -63.81%            | -51.00% |    -0.14 |       50 | 19.73%     | ok               |
|          40 | -26.48%  | -63.81%            | -57.21% |    -0.14 |       52 | 29.12%     | ok               |
|          15 | -61.40%  | -63.81%            | -83.89% |    -0.51 |       84 | 51.15%     | ok               |

## INTC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 80.47%   | 146.78%            | -49.32% |     0.77 |       58 | 34.11%     | ok               |
|          25 | 84.57%   | 146.78%            | -56.41% |     0.76 |       73 | 51.25%     | ok               |
|          15 | 83.73%   | 146.78%            | -53.65% |     0.74 |       81 | 59.73%     | ok               |
|          40 | 74.55%   | 146.78%            | -55.86% |     0.72 |       66 | 38.44%     | ok               |
|          20 | 71.54%   | 146.78%            | -52.47% |     0.69 |       80 | 55.91%     | ok               |

## INTU Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -0.28%   | -56.69%            | -40.73% |     0.11 |       69 | 27.95%     | ok               |
|          45 | -2.22%   | -56.69%            | -41.76% |     0.08 |       67 | 31.95%     | ok               |
|          40 | -8.64%   | -56.69%            | -45.15% |    -0.04 |       67 | 34.94%     | ok               |
|          35 | -15.62%  | -56.69%            | -46.75% |    -0.16 |       71 | 38.44%     | ok               |
|          25 | -18.48%  | -56.69%            | -39.87% |    -0.2  |       68 | 44.26%     | ok               |

## ITA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 0.57%    | 81.79%             | -25.76% |     0.1  |       87 | 59.90%     | ok               |
|          50 | 0.49%    | 81.79%             | -21.48% |     0.08 |       76 | 37.94%     | ok               |
|          30 | -2.99%   | 81.79%             | -23.75% |    -0.01 |       72 | 47.92%     | ok               |
|          35 | -5.06%   | 81.79%             | -23.16% |    -0.08 |       76 | 46.26%     | ok               |
|          40 | -6.15%   | 81.79%             | -20.58% |    -0.12 |       78 | 42.76%     | ok               |

## IWM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 8.60%    | 45.36%             | -14.08% |     0.39 |       42 | 31.28%     | ok               |
|          30 | 9.40%    | 45.36%             | -12.83% |     0.39 |       48 | 35.77%     | ok               |
|          25 | 9.50%    | 45.36%             | -13.55% |     0.39 |       50 | 36.94%     | ok               |
|          35 | 8.35%    | 45.36%             | -14.11% |     0.36 |       48 | 33.61%     | ok               |
|          20 | 5.19%    | 45.36%             | -14.08% |     0.24 |       60 | 37.94%     | ok               |

## JNJ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 19.24%   | 55.68%             | -10.57% |     0.79 |       56 | 37.60%     | ok               |
|          15 | 13.68%   | 55.68%             | -18.02% |     0.48 |       62 | 57.90%     | ok               |
|          45 | 10.73%   | 55.68%             | -13.35% |     0.46 |       56 | 42.43%     | ok               |
|          20 | 8.43%    | 55.68%             | -17.61% |     0.33 |       68 | 54.41%     | ok               |
|          40 | 5.40%    | 55.68%             | -14.77% |     0.25 |       62 | 46.76%     | ok               |

## JPM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 13.92%   | 88.19%             | -15.90% |     0.49 |       54 | 40.27%     | ok               |
|          45 | 3.10%    | 88.19%             | -21.91% |     0.16 |       56 | 43.26%     | ok               |
|          20 | -13.93%  | 88.19%             | -33.59% |    -0.23 |       86 | 58.24%     | ok               |
|          40 | -11.05%  | 88.19%             | -28.47% |    -0.25 |       68 | 45.92%     | ok               |
|          35 | -16.30%  | 88.19%             | -27.43% |    -0.39 |       76 | 49.92%     | ok               |

## KO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 23.75%   | 35.85%             | -8.20%  |     0.85 |       51 | 37.94%     | ok               |
|          35 | 19.96%   | 35.85%             | -8.07%  |     0.75 |       54 | 36.61%     | ok               |
|          40 | 17.46%   | 35.85%             | -9.28%  |     0.71 |       56 | 33.44%     | ok               |
|          25 | 18.64%   | 35.85%             | -9.73%  |     0.69 |       57 | 40.60%     | ok               |
|          50 | 10.20%   | 35.85%             | -12.31% |     0.48 |       38 | 26.96%     | ok               |

## LDO-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 62.86%   | -78.05%            | -46.95% |     0.69 |       83 | 54.21%     | ok               |
|          20 | 41.38%   | -78.05%            | -47.34% |     0.58 |       85 | 49.81%     | ok               |
|          50 | 30.40%   | -78.05%            | -48.04% |     0.54 |       52 | 18.20%     | ok               |
|          30 | 22.56%   | -78.05%            | -62.63% |     0.45 |       78 | 41.00%     | ok               |
|          35 | 19.75%   | -78.05%            | -64.26% |     0.42 |       78 | 34.10%     | ok               |

## LIN Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -0.13%   | 13.54%             | -23.68% |     0.06 |       64 | 49.42%     | ok               |
|          25 | -0.40%   | 13.54%             | -22.01% |     0.05 |       63 | 41.43%     | ok               |
|          20 | -2.54%   | 13.54%             | -23.00% |    -0.02 |       62 | 44.59%     | ok               |
|          35 | -4.00%   | 13.54%             | -21.18% |    -0.1  |       62 | 32.11%     | ok               |
|          30 | -4.61%   | 13.54%             | -21.53% |    -0.11 |       66 | 38.60%     | ok               |

## LINK-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -12.81%  | -53.47%            | -49.35% |     0.11 |       75 | 43.30%     | ok               |
|          45 | -9.42%   | -53.47%            | -38.11% |     0.1  |       52 | 27.78%     | ok               |
|          50 | -8.98%   | -53.47%            | -36.52% |     0.08 |       42 | 22.41%     | ok               |
|          35 | -20.96%  | -53.47%            | -49.18% |    -0    |       61 | 37.93%     | ok               |
|          40 | -25.30%  | -53.47%            | -50.55% |    -0.1  |       57 | 32.18%     | ok               |

## LLY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 5.68%    | 53.65%             | -38.23% |     0.22 |       46 | 36.27%     | ok               |
|          15 | -3.72%   | 53.65%             | -48.12% |     0.09 |       63 | 59.73%     | ok               |
|          45 | -6.21%   | 53.65%             | -42.66% |    -0    |       54 | 39.77%     | ok               |
|          20 | -19.22%  | 53.65%             | -51.34% |    -0.2  |       72 | 54.74%     | ok               |
|          25 | -20.55%  | 53.65%             | -53.47% |    -0.23 |       68 | 52.08%     | ok               |

## LRCX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -9.77%   | 245.97%            | -60.45% |     0.09 |       83 | 53.74%     | ok               |
|          50 | -14.67%  | 245.97%            | -50.39% |    -0.03 |       80 | 35.44%     | ok               |
|          40 | -17.23%  | 245.97%            | -56.86% |    -0.04 |       72 | 41.26%     | ok               |
|          35 | -22.61%  | 245.97%            | -61.76% |    -0.11 |       80 | 43.26%     | ok               |
|          20 | -24.75%  | 245.97%            | -67.48% |    -0.13 |       89 | 49.25%     | ok               |

## LTC-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -12.84%  | -62.84%            | -44.78% |    -0.01 |       58 | 32.57%     | ok               |
|          35 | -23.02%  | -62.84%            | -54.86% |    -0.14 |       68 | 43.68%     | ok               |
|          30 | -33.07%  | -62.84%            | -53.76% |    -0.27 |       72 | 50.19%     | ok               |
|          40 | -31.89%  | -62.84%            | -56.10% |    -0.31 |       60 | 38.89%     | ok               |
|          25 | -35.72%  | -62.84%            | -54.26% |    -0.31 |       76 | 52.68%     | ok               |

## MCD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 2.85%    | -10.16%            | -9.22%  |     0.19 |       42 | 20.63%     | ok               |
|          30 | -2.55%   | -10.16%            | -18.81% |    -0.05 |       75 | 38.10%     | ok               |
|          25 | -3.59%   | -10.16%            | -20.47% |    -0.09 |       75 | 40.77%     | ok               |
|          35 | -7.68%   | -10.16%            | -15.45% |    -0.29 |       67 | 34.44%     | ok               |
|          40 | -7.95%   | -10.16%            | -16.86% |    -0.33 |       71 | 28.79%     | ok               |

## META Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -14.13%  | 32.19%             | -31.66% |    -0.2  |       68 | 37.44%     | ok               |
|          40 | -23.57%  | 32.19%             | -36.23% |    -0.4  |       68 | 40.43%     | ok               |
|          25 | -31.11%  | 32.19%             | -41.42% |    -0.53 |       69 | 51.08%     | ok               |
|          50 | -27.24%  | 32.19%             | -34.36% |    -0.55 |       72 | 33.61%     | ok               |
|          30 | -32.96%  | 32.19%             | -40.57% |    -0.6  |       74 | 47.92%     | ok               |

## MPC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 27.05%   | 86.85%             | -23.96% |     0.58 |       52 | 37.60%     | ok               |
|          45 | 18.99%   | 86.85%             | -25.09% |     0.44 |       58 | 41.26%     | ok               |
|          40 | 17.19%   | 86.85%             | -25.70% |     0.41 |       60 | 43.59%     | ok               |
|          35 | 13.56%   | 86.85%             | -35.90% |     0.34 |       68 | 46.09%     | ok               |
|          30 | -4.30%   | 86.85%             | -44.76% |     0.05 |       71 | 48.92%     | ok               |

## MRK Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -21.12%  | -2.15%             | -30.12% |    -0.39 |       89 | 55.24%     | ok               |
|          25 | -20.74%  | -2.15%             | -31.07% |    -0.41 |       74 | 47.25%     | ok               |
|          20 | -24.62%  | -2.15%             | -29.59% |    -0.51 |       79 | 50.58%     | ok               |
|          50 | -24.60%  | -2.15%             | -27.68% |    -0.71 |       60 | 29.78%     | ok               |
|          30 | -30.17%  | -2.15%             | -35.95% |    -0.72 |       69 | 44.26%     | ok               |

## MS Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -3.32%   | 153.13%            | -19.99% |     0    |       72 | 41.43%     | ok               |
|          15 | -4.98%   | 153.13%            | -22.02% |    -0.01 |       73 | 58.24%     | ok               |
|          20 | -5.09%   | 153.13%            | -25.68% |    -0.02 |       77 | 54.41%     | ok               |
|          30 | -10.18%  | 153.13%            | -27.79% |    -0.16 |       77 | 49.58%     | ok               |
|          35 | -10.11%  | 153.13%            | -25.26% |    -0.17 |       78 | 46.09%     | ok               |

## MSFT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -21.30%  | -2.39%             | -25.26% |    -0.59 |       64 | 33.78%     | ok               |
|          50 | -23.26%  | -2.39%             | -26.14% |    -0.68 |       60 | 28.95%     | ok               |
|          35 | -33.78%  | -2.39%             | -35.38% |    -0.9  |       71 | 42.43%     | ok               |
|          40 | -33.15%  | -2.39%             | -34.77% |    -0.92 |       67 | 37.27%     | ok               |
|          30 | -37.64%  | -2.39%             | -39.15% |    -0.99 |       81 | 47.09%     | ok               |

## MU Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 346.71%  | 956.96%            | -61.96% |     1.42 |       47 | 66.89%     | ok               |
|          40 | 280.60%  | 956.96%            | -64.07% |     1.38 |       56 | 55.07%     | ok               |
|          25 | 275.37%  | 956.96%            | -67.90% |     1.34 |       49 | 61.23%     | ok               |
|          30 | 260.40%  | 956.96%            | -68.76% |     1.32 |       49 | 59.57%     | ok               |
|          35 | 227.65%  | 956.96%            | -69.15% |     1.24 |       63 | 57.57%     | ok               |

## NEAR-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 60.52%   | -43.63%            | -48.95% |     0.74 |       40 | 22.41%     | ok               |
|          50 | 37.56%   | -43.63%            | -53.13% |     0.58 |       34 | 17.62%     | ok               |
|          40 | 34.34%   | -43.63%            | -57.15% |     0.54 |       44 | 26.63%     | ok               |
|          35 | 7.46%    | -43.63%            | -61.02% |     0.3  |       66 | 31.80%     | ok               |
|          15 | -10.93%  | -43.63%            | -54.94% |     0.2  |       87 | 55.36%     | ok               |

## NEM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 3.24%    | 209.75%            | -29.41% |     0.21 |       62 | 61.40%     | ok               |
|          20 | -7.81%   | 209.75%            | -30.47% |     0.07 |       72 | 56.91%     | ok               |
|          25 | -21.27%  | 209.75%            | -37.89% |    -0.14 |       68 | 54.74%     | ok               |
|          50 | -24.62%  | 209.75%            | -32.97% |    -0.26 |       58 | 40.60%     | ok               |
|          30 | -31.13%  | 209.75%            | -38.49% |    -0.33 |       72 | 53.08%     | ok               |

## NFLX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 41.18%   | 14.13%             | -11.94% |     0.89 |       48 | 45.42%     | ok               |
|          50 | 37.38%   | 14.13%             | -16.28% |     0.88 |       46 | 37.77%     | ok               |
|          35 | 37.08%   | 14.13%             | -18.30% |     0.79 |       66 | 49.42%     | ok               |
|          15 | 35.95%   | 14.13%             | -26.59% |     0.69 |       67 | 65.06%     | ok               |
|          25 | 30.62%   | 14.13%             | -21.09% |     0.66 |       70 | 56.91%     | ok               |

## NKE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | -27.03%  | -59.14%            | -42.13% |    -0.38 |       75 | 37.44%     | ok               |
|          20 | -33.86%  | -59.14%            | -50.44% |    -0.42 |       93 | 52.58%     | ok               |
|          25 | -34.08%  | -59.14%            | -51.20% |    -0.44 |       89 | 48.75%     | ok               |
|          40 | -24.74%  | -59.14%            | -30.29% |    -0.46 |       65 | 30.12%     | ok               |
|          15 | -37.59%  | -59.14%            | -55.28% |    -0.5  |       91 | 56.91%     | ok               |

## NOW Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 12.06%   | -33.48%            | -26.36% |     0.31 |       75 | 51.58%     | ok               |
|          30 | 8.05%    | -33.48%            | -27.34% |     0.26 |       78 | 45.59%     | ok               |
|          15 | 3.14%    | -33.48%            | -26.77% |     0.21 |       86 | 54.58%     | ok               |
|          25 | 1.91%    | -33.48%            | -27.28% |     0.19 |       70 | 48.92%     | ok               |
|          40 | -0.36%   | -33.48%            | -30.87% |     0.13 |       68 | 34.78%     | ok               |

## NVDA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -9.60%   | 160.16%            | -35.26% |     0.01 |       76 | 48.48%     | ok               |
|          20 | -14.87%  | 160.16%            | -40.59% |    -0.03 |       72 | 56.51%     | ok               |
|          25 | -14.73%  | 160.16%            | -33.22% |    -0.04 |       73 | 51.52%     | ok               |
|          50 | -18.25%  | 160.16%            | -40.84% |    -0.18 |       58 | 32.44%     | ok               |
|          15 | -26.95%  | 160.16%            | -45.02% |    -0.19 |       75 | 59.89%     | ok               |

## OP-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 27.06%   | -91.28%            | -36.11% |     0.51 |       30 | 11.11%     | ok               |
|          45 | 26.15%   | -91.28%            | -45.76% |     0.48 |       32 | 15.71%     | ok               |
|          40 | 3.68%    | -91.28%            | -53.61% |     0.25 |       48 | 24.33%     | ok               |
|          35 | -23.40%  | -91.28%            | -59.71% |    -0.08 |       56 | 27.39%     | ok               |
|          30 | -37.37%  | -91.28%            | -71.26% |    -0.22 |       72 | 33.91%     | ok               |

## ORCL Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 248.19%  | 14.07%             | -29.32% |     1.38 |       68 | 65.89%     | ok               |
|          25 | 160.08%  | 14.07%             | -27.76% |     1.13 |       71 | 58.57%     | ok               |
|          20 | 156.71%  | 14.07%             | -29.32% |     1.11 |       71 | 61.56%     | ok               |
|          35 | 121.22%  | 14.07%             | -31.95% |     0.99 |       64 | 50.58%     | ok               |
|          30 | 121.41%  | 14.07%             | -29.47% |     0.99 |       70 | 54.74%     | ok               |

## OXY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 5.92%    | -6.77%             | -30.14% |     0.22 |       70 | 41.10%     | ok               |
|          40 | 5.66%    | -6.77%             | -30.31% |     0.21 |       56 | 37.44%     | ok               |
|          50 | 5.38%    | -6.77%             | -32.02% |     0.21 |       46 | 30.28%     | ok               |
|          30 | 3.50%    | -6.77%             | -34.15% |     0.18 |       71 | 46.26%     | ok               |
|          45 | -3.99%   | -6.77%             | -35.02% |     0.02 |       48 | 32.61%     | ok               |

## PEP Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 13.40%   | -19.72%            | -11.62% |     0.6  |       42 | 27.45%     | ok               |
|          45 | 6.15%    | -19.72%            | -14.22% |     0.3  |       58 | 31.45%     | ok               |
|          35 | 6.17%    | -19.72%            | -21.42% |     0.26 |       79 | 42.10%     | ok               |
|          40 | 2.59%    | -19.72%            | -18.04% |     0.15 |       70 | 37.10%     | ok               |
|          30 | -1.07%   | -19.72%            | -21.35% |     0.04 |       78 | 47.92%     | ok               |

## PEPE-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 4.00%    | -70.47%            | -57.66% |     0.31 |       81 | 45.59%     | ok               |
|          15 | -5.15%   | -70.47%            | -64.84% |     0.3  |       82 | 62.45%     | ok               |
|          35 | -7.37%   | -70.47%            | -51.35% |     0.18 |       66 | 39.85%     | ok               |
|          25 | -15.17%  | -70.47%            | -53.88% |     0.15 |       93 | 51.53%     | ok               |
|          20 | -26.05%  | -70.47%            | -64.07% |     0.07 |       88 | 58.81%     | ok               |

## PFE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -21.69%  | -7.25%             | -22.94% |    -0.8  |       52 | 18.97%     | ok               |
|          50 | -23.07%  | -7.25%             | -24.78% |    -0.96 |       38 | 15.31%     | ok               |
|          40 | -28.95%  | -7.25%             | -30.10% |    -1.02 |       72 | 23.96%     | ok               |
|          35 | -34.18%  | -7.25%             | -35.70% |    -1.14 |       84 | 31.61%     | ok               |
|          30 | -41.51%  | -7.25%             | -42.34% |    -1.34 |       79 | 36.11%     | ok               |

## PG Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -7.81%   | -7.03%             | -20.08% |    -0.28 |       58 | 32.95%     | ok               |
|          35 | -10.95%  | -7.03%             | -18.99% |    -0.4  |       66 | 36.44%     | ok               |
|          30 | -19.04%  | -7.03%             | -24.55% |    -0.72 |       68 | 39.60%     | ok               |
|          45 | -16.81%  | -7.03%             | -22.43% |    -0.73 |       58 | 30.45%     | ok               |
|          25 | -20.89%  | -7.03%             | -26.24% |    -0.8  |       80 | 41.10%     | ok               |

## PM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | -0.28%   | 108.52%            | -32.20% |     0.09 |       86 | 52.08%     | ok               |
|          20 | -2.99%   | 108.52%            | -31.89% |     0.04 |       85 | 60.57%     | ok               |
|          30 | -3.41%   | 108.52%            | -33.68% |     0.02 |       81 | 55.57%     | ok               |
|          50 | -6.95%   | 108.52%            | -35.70% |    -0.09 |       74 | 42.10%     | ok               |
|          40 | -8.33%   | 108.52%            | -37.94% |    -0.12 |       80 | 48.25%     | ok               |

## POL-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 26.61%   | -75.44%            | -46.45% |     0.48 |       75 | 48.28%     | ok               |
|          25 | 16.37%   | -75.44%            | -46.72% |     0.39 |       64 | 55.75%     | ok               |
|          15 | 5.40%    | -75.44%            | -58.42% |     0.3  |       76 | 66.28%     | ok               |
|          20 | 6.23%    | -75.44%            | -52.88% |     0.29 |       76 | 60.92%     | ok               |
|          50 | 2.17%    | -75.44%            | -23.33% |     0.17 |       48 | 19.73%     | ok               |

## QCOM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -3.88%   | 9.60%              | -54.50% |     0.12 |       71 | 47.75%     | ok               |
|          35 | -4.42%   | 9.60%              | -50.58% |     0.11 |       77 | 43.59%     | ok               |
|          20 | -7.78%   | 9.60%              | -54.38% |     0.08 |       67 | 50.58%     | ok               |
|          30 | -15.25%  | 9.60%              | -56.59% |    -0.04 |       73 | 46.09%     | ok               |
|          15 | -23.11%  | 9.60%              | -57.94% |    -0.13 |       71 | 53.74%     | ok               |

## QQQ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 20.33%   | 62.01%             | -12.88% |     0.58 |       60 | 43.59%     | ok               |
|          25 | 20.78%   | 62.01%             | -12.88% |     0.58 |       57 | 46.26%     | ok               |
|          15 | 21.30%   | 62.01%             | -14.17% |     0.55 |       61 | 51.75%     | ok               |
|          20 | 17.86%   | 62.01%             | -12.98% |     0.5  |       65 | 48.92%     | ok               |
|          35 | 8.03%    | 62.01%             | -18.29% |     0.29 |       66 | 39.93%     | ok               |

## RENDER-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 45.25%   | -63.53%            | -43.43% |     0.61 |       88 | 53.19%     | ok               |
|          15 | 34.05%   | -63.53%            | -44.59% |     0.54 |       88 | 56.48%     | ok               |
|          25 | 15.90%   | -63.53%            | -40.60% |     0.42 |       90 | 48.94%     | ok               |
|          30 | -19.07%  | -63.53%            | -45.00% |     0.1  |       98 | 42.36%     | ok               |
|          35 | -31.74%  | -63.53%            | -41.33% |    -0.12 |       84 | 34.24%     | ok               |

## RTX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 31.78%   | 114.19%            | -18.66% |     0.74 |       74 | 56.41%     | ok               |
|          25 | 27.45%   | 114.19%            | -18.59% |     0.67 |       62 | 53.41%     | ok               |
|          50 | 21.90%   | 114.19%            | -18.42% |     0.66 |       56 | 42.43%     | ok               |
|          35 | 22.79%   | 114.19%            | -18.00% |     0.64 |       52 | 50.25%     | ok               |
|          30 | 25.51%   | 114.19%            | -16.99% |     0.63 |       56 | 52.25%     | ok               |

## SBUX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -11.16%  | 10.96%             | -23.55% |    -0.15 |       63 | 42.10%     | ok               |
|          40 | -14.96%  | 10.96%             | -25.43% |    -0.29 |       60 | 33.94%     | ok               |
|          45 | -14.49%  | 10.96%             | -27.26% |    -0.3  |       66 | 30.12%     | ok               |
|          30 | -18.75%  | 10.96%             | -29.22% |    -0.34 |       62 | 39.77%     | ok               |
|          35 | -20.34%  | 10.96%             | -27.06% |    -0.4  |       58 | 37.10%     | ok               |

## SCHW Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 7.99%    | 52.96%             | -16.53% |     0.29 |       56 | 35.61%     | ok               |
|          25 | -2.19%   | 52.96%             | -28.76% |     0.04 |       61 | 50.58%     | ok               |
|          50 | -0.68%   | 52.96%             | -13.28% |     0.04 |       58 | 32.61%     | ok               |
|          40 | -3.21%   | 52.96%             | -23.35% |    -0.01 |       64 | 38.60%     | ok               |
|          20 | -6.30%   | 52.96%             | -29.24% |    -0.05 |       71 | 52.91%     | ok               |

## SHIB-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -11.98%  | -73.45%            | -49.21% |     0.1  |       80 | 67.43%     | ok               |
|          20 | -16.64%  | -73.45%            | -46.38% |     0.04 |       75 | 63.03%     | ok               |
|          25 | -16.88%  | -73.45%            | -43.85% |     0.02 |       71 | 58.62%     | ok               |
|          35 | -24.41%  | -73.45%            | -53.32% |    -0.13 |       64 | 45.79%     | ok               |
|          30 | -29.98%  | -73.45%            | -47.96% |    -0.2  |       74 | 51.72%     | ok               |

## SHY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd    |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:-------|---------:|---------:|:-----------|:-----------------|
|          30 | -2.24%   | 0.34%              | -2.85% |    -0.79 |       48 | 34.28%     | ok               |
|          35 | -2.36%   | 0.34%              | -3.27% |    -0.84 |       50 | 32.45%     | ok               |
|          40 | -2.47%   | 0.34%              | -3.33% |    -0.89 |       50 | 30.62%     | ok               |
|          45 | -2.45%   | 0.34%              | -3.23% |    -0.9  |       48 | 27.45%     | ok               |
|          50 | -2.62%   | 0.34%              | -3.40% |    -1.01 |       44 | 24.63%     | ok               |

## SKY-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -29.86%  | 7.85%              | -44.74% |    -0.36 |       74 | 40.87%     | ok               |
|          15 | -34.15%  | 7.85%              | -56.39% |    -0.36 |       64 | 50.65%     | ok               |
|          25 | -33.46%  | 7.85%              | -48.09% |    -0.42 |       69 | 44.35%     | ok               |
|          20 | -43.60%  | 7.85%              | -58.40% |    -0.6  |       66 | 47.83%     | ok               |
|          35 | -37.92%  | 7.85%              | -49.68% |    -0.63 |       66 | 33.48%     | ok               |

## SLB Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 22.60%   | -3.86%             | -20.36% |     0.54 |       52 | 33.61%     | ok               |
|          40 | 17.17%   | -3.86%             | -25.33% |     0.44 |       46 | 36.94%     | ok               |
|          50 | 0.70%    | -3.86%             | -28.65% |     0.1  |       50 | 29.12%     | ok               |
|          35 | -12.75%  | -3.86%             | -43.52% |    -0.16 |       74 | 44.43%     | ok               |
|          30 | -24.35%  | -3.86%             | -54.23% |    -0.4  |       73 | 50.92%     | ok               |

## SLV Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 67.45%   | 158.05%            | -34.10% |     0.86 |       52 | 34.78%     | ok               |
|          45 | 65.43%   | 158.05%            | -31.82% |     0.83 |       58 | 35.94%     | ok               |
|          40 | 63.45%   | 158.05%            | -31.93% |     0.82 |       64 | 38.10%     | ok               |
|          35 | 51.14%   | 158.05%            | -36.89% |     0.71 |       70 | 40.77%     | ok               |
|          20 | 47.87%   | 158.05%            | -42.66% |     0.66 |       66 | 47.59%     | ok               |

## SMH Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 101.67%  | 178.48%            | -30.17% |     1.23 |       47 | 50.08%     | ok               |
|          35 | 80.49%   | 178.48%            | -34.36% |     1.1  |       54 | 45.92%     | ok               |
|          25 | 80.36%   | 178.48%            | -32.94% |     1.08 |       46 | 48.92%     | ok               |
|          30 | 78.23%   | 178.48%            | -33.99% |     1.07 |       48 | 47.25%     | ok               |
|          45 | 65.27%   | 178.48%            | -32.75% |     1.02 |       52 | 40.10%     | ok               |

## SNX-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -3.26%   | -76.75%            | -43.20% |     0.24 |       73 | 48.47%     | ok               |
|          35 | -12.86%  | -76.75%            | -30.33% |     0.09 |       64 | 31.03%     | ok               |
|          30 | -21.23%  | -76.75%            | -34.76% |     0.01 |       60 | 38.12%     | ok               |
|          15 | -29.91%  | -76.75%            | -44.00% |    -0.02 |       81 | 52.87%     | ok               |
|          40 | -18.26%  | -76.75%            | -40.36% |    -0.04 |       52 | 24.90%     | ok               |

## SOL-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 6.81%    | -58.53%            | -52.35% |     0.3  |       60 | 37.16%     | ok               |
|          25 | -25.29%  | -58.53%            | -53.21% |    -0.01 |       74 | 57.47%     | ok               |
|          35 | -24.52%  | -58.53%            | -62.56% |    -0.02 |       74 | 45.02%     | ok               |
|          45 | -21.38%  | -58.53%            | -59.86% |    -0.04 |       60 | 31.99%     | ok               |
|          15 | -32.29%  | -58.53%            | -59.14% |    -0.07 |       76 | 63.41%     | ok               |

## SOXX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 81.48%   | 158.22%            | -40.27% |     1.04 |       57 | 48.75%     | ok               |
|          35 | 78.57%   | 158.22%            | -38.63% |     1.03 |       59 | 43.76%     | ok               |
|          25 | 78.91%   | 158.22%            | -41.42% |     1.02 |       53 | 48.25%     | ok               |
|          30 | 68.86%   | 158.22%            | -41.89% |     0.93 |       57 | 46.09%     | ok               |
|          15 | 67.33%   | 158.22%            | -39.35% |     0.88 |       70 | 51.75%     | ok               |

## SPY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 13.55%   | 47.61%             | -14.25% |     0.49 |       61 | 53.41%     | ok               |
|          15 | 12.00%   | 47.61%             | -16.80% |     0.43 |       70 | 56.57%     | ok               |
|          25 | 6.49%    | 47.61%             | -15.22% |     0.28 |       61 | 52.41%     | ok               |
|          30 | 1.99%    | 47.61%             | -16.47% |     0.13 |       64 | 49.58%     | ok               |
|          35 | 1.38%    | 47.61%             | -16.72% |     0.11 |       60 | 46.59%     | ok               |

## SUSHI-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -23.49%  | -81.06%            | -40.08% |    -0.19 |       52 | 14.75%     | ok               |
|          45 | -58.58%  | -81.06%            | -64.27% |    -0.77 |       56 | 18.20%     | ok               |
|          40 | -61.52%  | -81.06%            | -68.16% |    -0.77 |       63 | 24.71%     | ok               |
|          35 | -74.59%  | -81.06%            | -80.15% |    -1.06 |       82 | 30.65%     | ok               |
|          15 | -81.54%  | -81.06%            | -81.65% |    -1.08 |       95 | 48.66%     | ok               |

## T Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 59.37%   | 32.26%             | -18.13% |     1.14 |       58 | 57.40%     | ok               |
|          25 | 54.42%   | 32.26%             | -17.66% |     1.08 |       60 | 55.24%     | ok               |
|          15 | 49.61%   | 32.26%             | -15.08% |     0.98 |       69 | 61.40%     | ok               |
|          30 | 37.51%   | 32.26%             | -17.01% |     0.84 |       64 | 53.24%     | ok               |
|          35 | 23.37%   | 32.26%             | -14.49% |     0.6  |       66 | 49.75%     | ok               |

## TGT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -10.71%  | -8.89%             | -41.89% |    -0.1  |       83 | 46.09%     | ok               |
|          25 | -11.60%  | -8.89%             | -42.39% |    -0.14 |       65 | 41.10%     | ok               |
|          45 | -10.70%  | -8.89%             | -29.07% |    -0.17 |       54 | 28.45%     | ok               |
|          30 | -12.46%  | -8.89%             | -40.57% |    -0.18 |       60 | 38.44%     | ok               |
|          15 | -16.36%  | -8.89%             | -39.76% |    -0.2  |       73 | 50.75%     | ok               |

## TIA-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -2.21%   | -88.07%            | -49.23% |     0.16 |       54 | 18.77%     | ok               |
|          40 | -7.13%   | -88.07%            | -45.16% |     0.14 |       68 | 26.05%     | ok               |
|          35 | -9.79%   | -88.07%            | -53.37% |     0.12 |       68 | 31.03%     | ok               |
|          50 | -3.16%   | -88.07%            | -48.70% |     0.1  |       34 | 11.69%     | ok               |
|          30 | -45.37%  | -88.07%            | -68.36% |    -0.32 |       93 | 37.16%     | ok               |

## TLT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -20.91%  | -9.98%             | -21.87% |    -1.61 |       72 | 32.78%     | ok               |
|          50 | -14.21%  | -9.98%             | -15.73% |    -1.66 |       34 | 15.31%     | ok               |
|          40 | -19.27%  | -9.98%             | -20.09% |    -1.84 |       60 | 22.13%     | ok               |
|          15 | -26.70%  | -9.98%             | -27.76% |    -1.87 |       77 | 40.77%     | ok               |
|          35 | -21.68%  | -9.98%             | -22.47% |    -1.9  |       66 | 26.96%     | ok               |

## TMO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 45.64%   | -7.54%             | -8.17%  |     1.02 |       40 | 32.61%     | ok               |
|          45 | 41.41%   | -7.54%             | -10.13% |     0.9  |       46 | 37.44%     | ok               |
|          40 | 39.33%   | -7.54%             | -9.91%  |     0.85 |       49 | 41.93%     | ok               |
|          35 | 21.59%   | -7.54%             | -14.06% |     0.52 |       61 | 46.42%     | ok               |
|          30 | 16.14%   | -7.54%             | -18.85% |     0.41 |       61 | 51.58%     | ok               |

## TMUS Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 7.21%    | 15.89%             | -30.05% |     0.25 |       65 | 59.57%     | ok               |
|          30 | 6.02%    | 15.89%             | -25.71% |     0.22 |       70 | 47.59%     | ok               |
|          20 | 1.03%    | 15.89%             | -29.75% |     0.12 |       71 | 53.91%     | ok               |
|          25 | -2.36%   | 15.89%             | -31.45% |     0.05 |       75 | 50.08%     | ok               |
|          50 | -4.19%   | 15.89%             | -28.89% |    -0.04 |       60 | 35.61%     | ok               |

## TRX-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 11.18%   | 35.51%             | -18.79% |     0.4  |       50 | 36.97%     | ok               |
|          30 | 7.33%    | 35.51%             | -22.90% |     0.28 |       68 | 48.66%     | ok               |
|          35 | 6.44%    | 35.51%             | -21.77% |     0.26 |       64 | 45.40%     | ok               |
|          25 | 5.40%    | 35.51%             | -26.84% |     0.23 |       64 | 51.92%     | ok               |
|          20 | 5.10%    | 35.51%             | -25.45% |     0.22 |       61 | 55.36%     | ok               |

## TSLA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 56.12%   | 89.72%             | -32.60% |     0.73 |       64 | 29.78%     | ok               |
|          40 | 35.10%   | 89.72%             | -45.90% |     0.52 |       63 | 34.61%     | ok               |
|          45 | 14.45%   | 89.72%             | -46.86% |     0.34 |       67 | 31.95%     | ok               |
|          35 | 3.29%    | 89.72%             | -51.29% |     0.23 |       72 | 37.27%     | ok               |
|          30 | -14.59%  | 89.72%             | -54.91% |     0.05 |       70 | 41.26%     | ok               |

## TXN Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 17.86%   | 76.61%             | -45.45% |     0.4  |       64 | 34.61%     | ok               |
|          20 | 3.23%    | 76.61%             | -38.49% |     0.2  |       60 | 58.57%     | ok               |
|          35 | 0.40%    | 76.61%             | -43.28% |     0.14 |       74 | 49.08%     | ok               |
|          15 | -2.67%   | 76.61%             | -38.99% |     0.12 |       65 | 62.40%     | ok               |
|          40 | -1.68%   | 76.61%             | -45.67% |     0.11 |       68 | 46.59%     | ok               |

## UNH Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 34.96%   | -15.01%            | -26.96% |     0.57 |       74 | 52.58%     | ok               |
|          15 | 33.59%   | -15.01%            | -32.14% |     0.54 |       75 | 67.55%     | ok               |
|          35 | 31.29%   | -15.01%            | -28.32% |     0.54 |       66 | 47.42%     | ok               |
|          50 | 28.47%   | -15.01%            | -36.82% |     0.53 |       54 | 30.62%     | ok               |
|          40 | 23.93%   | -15.01%            | -35.73% |     0.46 |       58 | 42.43%     | ok               |

## UNI-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -18.66%  | -61.62%            | -63.75% |     0.02 |       58 | 33.33%     | ok               |
|          45 | -20.65%  | -61.62%            | -58.49% |    -0.03 |       58 | 28.16%     | ok               |
|          35 | -33.20%  | -61.62%            | -68.71% |    -0.14 |       70 | 38.89%     | ok               |
|          50 | -29.10%  | -61.62%            | -57.60% |    -0.19 |       54 | 21.46%     | ok               |
|          30 | -71.03%  | -61.62%            | -80.61% |    -0.82 |       86 | 44.83%     | ok               |

## UPS Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -30.00%  | -21.54%            | -43.07% |    -0.52 |       82 | 47.92%     | ok               |
|          25 | -31.12%  | -21.54%            | -39.04% |    -0.56 |       78 | 44.43%     | ok               |
|          15 | -33.72%  | -21.54%            | -43.86% |    -0.6  |       88 | 52.25%     | ok               |
|          35 | -32.51%  | -21.54%            | -39.90% |    -0.64 |       67 | 33.61%     | ok               |
|          30 | -35.38%  | -21.54%            | -38.83% |    -0.69 |       72 | 39.43%     | ok               |

## USO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 24.03%   | 74.48%             | -33.25% |     0.49 |       50 | 26.96%     | ok               |
|          20 | 25.30%   | 74.48%             | -44.16% |     0.48 |       74 | 39.77%     | ok               |
|          15 | 19.38%   | 74.48%             | -44.33% |     0.4  |       73 | 42.93%     | ok               |
|          30 | 15.63%   | 74.48%             | -43.35% |     0.36 |       68 | 34.44%     | ok               |
|          25 | 15.46%   | 74.48%             | -43.43% |     0.36 |       68 | 37.27%     | ok               |

## VEA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 5.48%    | 44.32%             | -16.28% |     0.25 |       60 | 50.25%     | ok               |
|          20 | 1.23%    | 44.32%             | -17.70% |     0.1  |       61 | 47.59%     | ok               |
|          25 | -0.78%   | 44.32%             | -17.79% |     0.02 |       57 | 45.92%     | ok               |
|          30 | -0.94%   | 44.32%             | -17.93% |     0.01 |       58 | 43.76%     | ok               |
|          35 | -2.05%   | 44.32%             | -16.79% |    -0.03 |       56 | 42.76%     | ok               |

## VIXY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -48.04%  | -61.66%            | -69.78% |    -0.43 |       46 | 10.48%     | ok               |
|          45 | -59.37%  | -61.66%            | -75.03% |    -0.61 |       60 | 16.64%     | ok               |
|          40 | -67.66%  | -61.66%            | -80.72% |    -0.74 |       76 | 21.46%     | ok               |
|          35 | -70.62%  | -61.66%            | -84.37% |    -0.76 |       90 | 26.79%     | ok               |
|          15 | -77.32%  | -61.66%            | -89.47% |    -0.78 |      101 | 44.26%     | ok               |

## VNQ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -7.66%   | 18.50%             | -19.07% |    -0.32 |       56 | 28.12%     | ok               |
|          50 | -8.10%   | 18.50%             | -17.13% |    -0.36 |       52 | 25.62%     | ok               |
|          25 | -12.08%  | 18.50%             | -22.34% |    -0.46 |       65 | 40.10%     | ok               |
|          20 | -13.69%  | 18.50%             | -23.79% |    -0.52 |       68 | 42.76%     | ok               |
|          15 | -15.00%  | 18.50%             | -24.90% |    -0.57 |       65 | 43.93%     | ok               |

## VTI Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 16.45%   | 46.64%             | -13.96% |     0.57 |       64 | 53.91%     | ok               |
|          15 | 10.49%   | 46.64%             | -15.70% |     0.39 |       67 | 56.41%     | ok               |
|          25 | 2.99%    | 46.64%             | -16.10% |     0.16 |       60 | 51.91%     | ok               |
|          30 | -4.74%   | 46.64%             | -18.77% |    -0.11 |       70 | 49.92%     | ok               |
|          35 | -7.13%   | 46.64%             | -20.89% |    -0.21 |       64 | 46.76%     | ok               |

## VWO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -8.20%   | 41.59%             | -21.18% |    -0.29 |       60 | 31.78%     | ok               |
|          15 | -10.40%  | 41.59%             | -24.01% |    -0.31 |       71 | 48.75%     | ok               |
|          40 | -9.86%   | 41.59%             | -23.57% |    -0.35 |       70 | 37.10%     | ok               |
|          20 | -11.42%  | 41.59%             | -26.14% |    -0.36 |       69 | 46.59%     | ok               |
|          45 | -9.99%   | 41.59%             | -23.26% |    -0.36 |       62 | 34.28%     | ok               |

## VZ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -6.80%   | 9.64%              | -12.71% |    -0.19 |       50 | 24.29%     | ok               |
|          45 | -17.93%  | 9.64%              | -20.96% |    -0.59 |       64 | 27.95%     | ok               |
|          35 | -19.10%  | 9.64%              | -22.26% |    -0.61 |       59 | 33.78%     | ok               |
|          25 | -21.86%  | 9.64%              | -22.13% |    -0.63 |       77 | 41.76%     | ok               |
|          40 | -23.63%  | 9.64%              | -23.75% |    -0.81 |       64 | 31.11%     | ok               |

## WFC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -4.09%   | 60.08%             | -18.29% |    -0.06 |       62 | 35.44%     | ok               |
|          35 | -7.56%   | 60.08%             | -23.64% |    -0.09 |       81 | 47.42%     | ok               |
|          20 | -13.73%  | 60.08%             | -29.43% |    -0.16 |       79 | 56.91%     | ok               |
|          45 | -10.81%  | 60.08%             | -23.40% |    -0.24 |       68 | 40.10%     | ok               |
|          40 | -12.10%  | 60.08%             | -24.26% |    -0.27 |       76 | 43.59%     | ok               |

## WIF-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 59.82%   | -76.66%            | -46.21% |     0.66 |       73 | 42.72%     | ok               |
|          20 | 54.17%   | -76.66%            | -40.67% |     0.63 |       67 | 40.04%     | ok               |
|          25 | 1.55%    | -76.66%            | -45.19% |     0.3  |       69 | 37.36%     | ok               |
|          30 | -35.62%  | -76.66%            | -51.39% |    -0.13 |       70 | 33.33%     | ok               |
|          50 | -20.06%  | -76.66%            | -37.87% |    -0.14 |       40 | 12.07%     | ok               |

## WMT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 45.82%   | 85.25%             | -9.18%  |     1.28 |       38 | 41.43%     | ok               |
|          50 | 38.72%   | 85.25%             | -12.19% |     1.17 |       34 | 39.10%     | ok               |
|          40 | 33.68%   | 85.25%             | -12.49% |     0.97 |       44 | 42.76%     | ok               |
|          35 | 32.81%   | 85.25%             | -13.08% |     0.92 |       54 | 47.42%     | ok               |
|          15 | 16.83%   | 85.25%             | -25.74% |     0.45 |       72 | 61.23%     | ok               |

## XBI Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -2.93%   | 50.16%             | -16.08% |     0    |       60 | 35.61%     | ok               |
|          45 | -3.68%   | 50.16%             | -15.62% |    -0.02 |       52 | 32.45%     | ok               |
|          35 | -8.77%   | 50.16%             | -17.75% |    -0.15 |       64 | 39.10%     | ok               |
|          30 | -9.78%   | 50.16%             | -18.71% |    -0.17 |       66 | 40.93%     | ok               |
|          25 | -11.87%  | 50.16%             | -23.66% |    -0.21 |       72 | 43.26%     | ok               |

## XLB Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -0.42%   | 15.66%             | -19.67% |     0.04 |       54 | 31.45%     | ok               |
|          50 | -1.74%   | 15.66%             | -17.59% |    -0.02 |       42 | 27.29%     | ok               |
|          35 | -3.70%   | 15.66%             | -22.65% |    -0.08 |       56 | 34.78%     | ok               |
|          45 | -3.43%   | 15.66%             | -19.78% |    -0.09 |       42 | 28.62%     | ok               |
|          25 | -6.87%   | 15.66%             | -22.63% |    -0.19 |       60 | 40.27%     | ok               |

## XLC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 11.05%   | 38.93%             | -12.33% |     0.42 |       69 | 53.74%     | ok               |
|          25 | 8.31%    | 38.93%             | -12.31% |     0.33 |       68 | 55.57%     | ok               |
|          40 | 7.24%    | 38.93%             | -13.38% |     0.32 |       70 | 46.26%     | ok               |
|          35 | 6.64%    | 38.93%             | -13.38% |     0.29 |       66 | 50.58%     | ok               |
|          45 | 1.32%    | 38.93%             | -13.21% |     0.11 |       70 | 43.26%     | ok               |

## XLE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 9.14%    | 36.22%             | -25.98% |     0.33 |       54 | 36.11%     | ok               |
|          45 | 4.66%    | 36.22%             | -29.68% |     0.2  |       60 | 38.10%     | ok               |
|          35 | 2.46%    | 36.22%             | -31.51% |     0.14 |       65 | 42.76%     | ok               |
|          25 | -4.33%   | 36.22%             | -36.05% |    -0.02 |       83 | 48.25%     | ok               |
|          40 | -4.22%   | 36.22%             | -34.51% |    -0.04 |       64 | 40.60%     | ok               |

## XLF Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -5.08%   | 39.54%             | -18.01% |    -0.11 |       70 | 53.74%     | ok               |
|          15 | -9.01%   | 39.54%             | -19.58% |    -0.24 |       78 | 56.57%     | ok               |
|          25 | -11.45%  | 39.54%             | -23.22% |    -0.36 |       77 | 50.42%     | ok               |
|          30 | -12.08%  | 39.54%             | -23.61% |    -0.4  |       76 | 47.92%     | ok               |
|          35 | -19.14%  | 39.54%             | -27.41% |    -0.76 |       66 | 43.76%     | ok               |

## XLI Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 5.14%    | 48.61%             | -10.36% |     0.24 |       76 | 51.25%     | ok               |
|          20 | -0.27%   | 48.61%             | -12.74% |     0.04 |       67 | 46.42%     | ok               |
|          50 | -1.12%   | 48.61%             | -11.03% |    -0.01 |       60 | 32.61%     | ok               |
|          30 | -2.72%   | 48.61%             | -11.79% |    -0.06 |       66 | 43.76%     | ok               |
|          45 | -2.43%   | 48.61%             | -14.01% |    -0.06 |       64 | 35.11%     | ok               |

## XLK Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 87.25%   | 75.80%             | -14.75% |     1.38 |       39 | 50.92%     | ok               |
|          20 | 71.51%   | 75.80%             | -14.75% |     1.23 |       46 | 48.92%     | ok               |
|          25 | 68.02%   | 75.80%             | -14.75% |     1.23 |       40 | 46.76%     | ok               |
|          30 | 65.83%   | 75.80%             | -14.75% |     1.22 |       40 | 45.59%     | ok               |
|          35 | 47.33%   | 75.80%             | -13.61% |     0.99 |       52 | 42.93%     | ok               |

## XLM-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 26.14%   | -44.12%            | -38.97% |     0.48 |       44 | 27.39%     | ok               |
|          45 | 22.34%   | -44.12%            | -43.99% |     0.44 |       50 | 31.03%     | ok               |
|          30 | 5.21%    | -44.12%            | -50.36% |     0.28 |       69 | 45.79%     | ok               |
|          40 | 1.75%    | -44.12%            | -43.80% |     0.23 |       49 | 35.44%     | ok               |
|          35 | -4.00%   | -44.12%            | -50.42% |     0.17 |       69 | 41.76%     | ok               |

## XLP Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 8.18%    | 12.85%             | -6.85%  |     0.53 |       54 | 32.45%     | ok               |
|          40 | 7.50%    | 12.85%             | -7.77%  |     0.47 |       68 | 36.77%     | ok               |
|          50 | 6.85%    | 12.85%             | -7.01%  |     0.46 |       54 | 30.28%     | ok               |
|          35 | 6.56%    | 12.85%             | -9.73%  |     0.41 |       64 | 39.77%     | ok               |
|          30 | 4.67%    | 12.85%             | -11.16% |     0.3  |       66 | 41.26%     | ok               |

## XLU Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 5.85%    | 45.16%             | -12.97% |     0.32 |       52 | 31.28%     | ok               |
|          45 | 4.45%    | 45.16%             | -14.27% |     0.25 |       54 | 32.28%     | ok               |
|          40 | 1.57%    | 45.16%             | -15.59% |     0.12 |       58 | 33.78%     | ok               |
|          35 | -4.35%   | 45.16%             | -19.71% |    -0.16 |       62 | 35.94%     | ok               |
|          30 | -5.24%   | 45.16%             | -20.40% |    -0.19 |       67 | 39.10%     | ok               |

## XLV Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -15.87%  | 9.21%              | -19.97% |    -0.78 |       68 | 35.94%     | ok               |
|          25 | -16.56%  | 9.21%              | -21.14% |    -0.81 |       70 | 37.44%     | ok               |
|          15 | -20.34%  | 9.21%              | -24.43% |    -0.98 |       81 | 42.26%     | ok               |
|          20 | -20.28%  | 9.21%              | -24.51% |    -1.01 |       75 | 39.10%     | ok               |
|          35 | -20.26%  | 9.21%              | -23.94% |    -1.09 |       66 | 33.44%     | ok               |

## XLY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 5.85%    | 25.92%             | -12.94% |     0.25 |       70 | 41.60%     | ok               |
|          30 | 3.95%    | 25.92%             | -14.01% |     0.19 |       70 | 44.59%     | ok               |
|          15 | 1.20%    | 25.92%             | -15.77% |     0.11 |       74 | 51.25%     | ok               |
|          50 | 1.15%    | 25.92%             | -11.49% |     0.1  |       52 | 29.62%     | ok               |
|          45 | -1.91%   | 25.92%             | -13.48% |    -0.02 |       56 | 32.28%     | ok               |

## XOM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | 10.49%   | 45.83%             | -19.90% |     0.35 |       57 | 37.94%     | ok               |
|          30 | 9.09%    | 45.83%             | -20.29% |     0.32 |       57 | 37.10%     | ok               |
|          50 | 7.73%    | 45.83%             | -21.35% |     0.29 |       38 | 29.62%     | ok               |
|          20 | 2.68%    | 45.83%             | -25.56% |     0.15 |       66 | 40.10%     | ok               |
|          35 | 1.82%    | 45.83%             | -20.93% |     0.13 |       57 | 35.94%     | ok               |

## XRP-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | -24.17%  | -58.19%            | -44.79% |    -0.13 |       68 | 39.66%     | ok               |
|          40 | -30.47%  | -58.19%            | -44.89% |    -0.26 |       58 | 33.72%     | ok               |
|          30 | -36.45%  | -58.19%            | -52.93% |    -0.32 |       70 | 43.87%     | ok               |
|          45 | -38.24%  | -58.19%            | -46.06% |    -0.42 |       58 | 29.50%     | ok               |
|          50 | -34.88%  | -58.19%            | -38.03% |    -0.46 |       60 | 22.03%     | ok               |

## YFI-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -51.25%  | -63.90%            | -52.26% |    -0.86 |       62 | 27.39%     | ok               |
|          45 | -47.81%  | -63.90%            | -51.53% |    -0.98 |       70 | 21.46%     | ok               |
|          30 | -64.19%  | -63.90%            | -71.12% |    -1.03 |       81 | 40.61%     | ok               |
|          35 | -62.68%  | -63.90%            | -63.36% |    -1.06 |       69 | 34.87%     | ok               |
|          25 | -67.83%  | -63.90%            | -72.16% |    -1.12 |       75 | 45.59%     | ok               |

## ZEC-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 107.59%  | 1438.81%           | -24.66% |     0.84 |       46 | 24.52%     | ok               |
|          35 | 78.24%   | 1438.81%           | -44.34% |     0.71 |       54 | 31.03%     | ok               |
|          25 | 68.33%   | 1438.81%           | -48.59% |     0.67 |       58 | 39.66%     | ok               |
|          30 | 42.98%   | 1438.81%           | -47.68% |     0.55 |       64 | 36.78%     | ok               |
|          20 | 41.66%   | 1438.81%           | -54.26% |     0.55 |       69 | 41.95%     | ok               |
