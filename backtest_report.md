# Market Tracker Backtest Report

_Generated: 2026-09-18T04:38:05+00:00_

## Data Sources

- Crypto: Kraken -> Coinbase -> CoinGecko OHLC -> CoinPaprika fallback chain.
- Stocks / ETFs / indices: Stooq -> Yahoo Finance fallback chain.
- Data rows are generated from real market APIs. Mock OHLCV rows are not generated.

## Data Freshness

- Rows: **92,690**
- Symbols: **161**
- Date range: **2024-04-25** to **2026-09-18**

## Latest Signals

| symbol     | date                |         close |   composite_score | signal   | data_source   |
|:-----------|:--------------------|--------------:|------------------:|:---------|:--------------|
| AAPL       | 2026-09-17 00:00:00 |   337         |         72.9167   | LONG     | Yahoo Finance |
| AMD        | 2026-09-17 00:00:00 |   545.09      |         78.0833   | LONG     | Yahoo Finance |
| APT-USD    | 2026-09-18 00:00:00 |     0.6694    |         52.5833   | LONG     | Kraken API    |
| ARB-USD    | 2026-09-18 00:00:00 |     0.2255    |         66.0833   | LONG     | Kraken API    |
| BTC-USD    | 2026-09-18 00:00:00 | 77202.9       |         44.3333   | LONG     | Kraken API    |
| CRM        | 2026-09-17 00:00:00 |   242.85      |         31.9167   | LONG     | Yahoo Finance |
| CVX        | 2026-09-17 00:00:00 |   211.57      |         58.25     | LONG     | Yahoo Finance |
| DASH-USD   | 2026-09-18 00:00:00 |    60.45      |         41.4167   | LONG     | Kraken API    |
| DBC        | 2026-09-17 00:00:00 |    33.05      |         73.5833   | LONG     | Yahoo Finance |
| DE         | 2026-09-17 00:00:00 |   685.63      |         57.9167   | LONG     | Yahoo Finance |
| DOT-USD    | 2026-09-18 00:00:00 |     1.122     |         45.1667   | LONG     | Kraken API    |
| DXY-INDEX  | 2026-09-18 00:00:00 |   100.203     |         75        | LONG     | Yahoo Finance |
| ETC-USD    | 2026-09-18 00:00:00 |     7.789     |         32.5833   | LONG     | Kraken API    |
| ETH-USD    | 2026-09-18 00:00:00 |  2470.03      |         53.1667   | LONG     | Kraken API    |
| FET-USD    | 2026-09-18 00:00:00 |     0.1812    |         46.8333   | LONG     | Kraken API    |
| GRT-USD    | 2026-09-18 00:00:00 |     0.0192    |         37        | LONG     | Kraken API    |
| IBIT       | 2026-09-17 00:00:00 |    43.3       |         36.4167   | LONG     | Yahoo Finance |
| ICP-USD    | 2026-09-18 00:00:00 |     2.779     |         53.8333   | LONG     | Kraken API    |
| INJ-USD    | 2026-09-18 00:00:00 |     5.835     |         53.8333   | LONG     | Kraken API    |
| INTC       | 2026-09-17 00:00:00 |   108.8       |         78.5833   | LONG     | Yahoo Finance |
| LINK-USD   | 2026-09-18 00:00:00 |    11.7158    |         52.3333   | LONG     | Kraken API    |
| LTC-USD    | 2026-09-18 00:00:00 |    54.44      |         57.3333   | LONG     | Kraken API    |
| META       | 2026-09-17 00:00:00 |   682.31      |         60.25     | LONG     | Yahoo Finance |
| MPC        | 2026-09-17 00:00:00 |   421.96      |         75.75     | LONG     | Yahoo Finance |
| MRK        | 2026-09-17 00:00:00 |   147.15      |         38.5833   | LONG     | Yahoo Finance |
| MSFT       | 2026-09-17 00:00:00 |   497.75      |         47.9167   | LONG     | Yahoo Finance |
| NEAR-USD   | 2026-09-18 00:00:00 |     3.4448    |         67.75     | LONG     | Kraken API    |
| NOW        | 2026-09-17 00:00:00 |   138.47      |         52.0833   | LONG     | Yahoo Finance |
| QCOM       | 2026-09-17 00:00:00 |   188.71      |         79        | LONG     | Yahoo Finance |
| SOL-USD    | 2026-09-18 00:00:00 |   104.93      |         43.25     | LONG     | Kraken API    |
| SUSHI-USD  | 2026-09-18 00:00:00 |     0.2376    |         49.3333   | LONG     | Kraken API    |
| TGT        | 2026-09-17 00:00:00 |   159.83      |         38.5833   | LONG     | Yahoo Finance |
| UNI-USD    | 2026-09-18 00:00:00 |     8.5608    |         58.25     | LONG     | Kraken API    |
| USO        | 2026-09-17 00:00:00 |   155.31      |         69.5833   | LONG     | Yahoo Finance |
| XLV        | 2026-09-17 00:00:00 |   168.81      |         31.5833   | LONG     | Yahoo Finance |
| ZEC-USD    | 2026-09-18 00:00:00 |  1489.72      |         63.8333   | LONG     | Kraken API    |
| AAVE-USD   | 2026-09-18 00:00:00 |   133.76      |         43        | NEUTRAL  | Kraken API    |
| ABBV       | 2026-09-17 00:00:00 |   264.02      |         51        | NEUTRAL  | Yahoo Finance |
| ADA-USD    | 2026-09-18 00:00:00 |     0.213653  |          8.58333  | NEUTRAL  | Kraken API    |
| ADBE       | 2026-09-17 00:00:00 |   252.67      |        -29.5      | NEUTRAL  | Yahoo Finance |
| ALGO-USD   | 2026-09-18 00:00:00 |     0.09381   |         17.5833   | NEUTRAL  | Kraken API    |
| AMGN       | 2026-09-17 00:00:00 |   379.78      |        -16.3333   | NEUTRAL  | Yahoo Finance |
| AMZN       | 2026-09-17 00:00:00 |   251.19      |         -9.75     | NEUTRAL  | Yahoo Finance |
| ARKK       | 2026-09-17 00:00:00 |    86.92      |         30.8333   | NEUTRAL  | Yahoo Finance |
| ATOM-USD   | 2026-09-18 00:00:00 |     1.6183    |         27.0833   | NEUTRAL  | Kraken API    |
| AVAX-USD   | 2026-09-18 00:00:00 |     7.877     |         21.3333   | NEUTRAL  | Kraken API    |
| BAC        | 2026-09-17 00:00:00 |    58.18      |        -15.25     | NEUTRAL  | Yahoo Finance |
| BCH-USD    | 2026-09-18 00:00:00 |   244.52      |        -15.8333   | NEUTRAL  | Kraken API    |
| BITO       | 2026-09-17 00:00:00 |    10.28      |         13.1667   | NEUTRAL  | Yahoo Finance |
| BONK-USD   | 2026-09-18 00:00:00 |     2.811e-06 |        -49.75     | NEUTRAL  | Kraken API    |
| C          | 2026-09-17 00:00:00 |   132.7       |        -10.1667   | NEUTRAL  | Yahoo Finance |
| CAT        | 2026-09-17 00:00:00 |   798.57      |        -12.9167   | NEUTRAL  | Yahoo Finance |
| CL         | 2026-09-17 00:00:00 |    87.73      |        -48.9167   | NEUTRAL  | Yahoo Finance |
| COMP-USD   | 2026-09-18 00:00:00 |    20         |         12.0833   | NEUTRAL  | Kraken API    |
| COP        | 2026-09-17 00:00:00 |   133.19      |         19.3333   | NEUTRAL  | Yahoo Finance |
| CRV-USD    | 2026-09-18 00:00:00 |     0.33999   |         21.0833   | NEUTRAL  | Kraken API    |
| CSCO       | 2026-09-17 00:00:00 |   110.24      |         18.0833   | NEUTRAL  | Yahoo Finance |
| DIA        | 2026-09-17 00:00:00 |   518.35      |        -22.5      | NEUTRAL  | Yahoo Finance |
| DIS        | 2026-09-17 00:00:00 |   105.35      |          6.33333  | NEUTRAL  | Yahoo Finance |
| DOGE-USD   | 2026-09-18 00:00:00 |     0.0841529 |         11.1667   | NEUTRAL  | Kraken API    |
| EEM        | 2026-09-17 00:00:00 |    66.91      |         27.6667   | NEUTRAL  | Yahoo Finance |
| EFA        | 2026-09-17 00:00:00 |   106.04      |        -38.3333   | NEUTRAL  | Yahoo Finance |
| EOG        | 2026-09-17 00:00:00 |   145.47      |         21        | NEUTRAL  | Yahoo Finance |
| EWJ        | 2026-09-17 00:00:00 |    97.91      |         54.3333   | NEUTRAL  | Yahoo Finance |
| FCX        | 2026-09-17 00:00:00 |    70.85      |          0.916667 | NEUTRAL  | Yahoo Finance |
| FIL-USD    | 2026-09-18 00:00:00 |     0.863     |         33.9167   | NEUTRAL  | Kraken API    |
| FXI        | 2026-09-17 00:00:00 |    34.19      |        -59.5      | NEUTRAL  | Yahoo Finance |
| GDX        | 2026-09-17 00:00:00 |    95.92      |         18.9167   | NEUTRAL  | Yahoo Finance |
| GDXJ       | 2026-09-17 00:00:00 |   123.63      |          0.916667 | NEUTRAL  | Yahoo Finance |
| GLD        | 2026-09-17 00:00:00 |   398.36      |        -33.8333   | NEUTRAL  | Yahoo Finance |
| GOOGL      | 2026-09-17 00:00:00 |   347.33      |         51.4167   | NEUTRAL  | Yahoo Finance |
| GS         | 2026-09-17 00:00:00 |   951.47      |        -47.8333   | NEUTRAL  | Yahoo Finance |
| HBAR-USD   | 2026-09-18 00:00:00 |     0.077     |         12.9167   | NEUTRAL  | Kraken API    |
| IBM        | 2026-09-17 00:00:00 |   237.75      |         -4.83333  | NEUTRAL  | Yahoo Finance |
| IEMG       | 2026-09-17 00:00:00 |    81.5       |         27.6667   | NEUTRAL  | Yahoo Finance |
| INTU       | 2026-09-17 00:00:00 |   313.13      |        -63.3333   | NEUTRAL  | Yahoo Finance |
| IWM        | 2026-09-17 00:00:00 |   285.43      |        -16.5833   | NEUTRAL  | Yahoo Finance |
| JNJ        | 2026-09-17 00:00:00 |   270.22      |         20        | NEUTRAL  | Yahoo Finance |
| JPM        | 2026-09-17 00:00:00 |   349.31      |        -24.8333   | NEUTRAL  | Yahoo Finance |
| KO         | 2026-09-17 00:00:00 |    88.06      |         -0.166667 | NEUTRAL  | Yahoo Finance |
| LDO-USD    | 2026-09-18 00:00:00 |     0.378     |         15.3333   | NEUTRAL  | Kraken API    |
| LLY        | 2026-09-17 00:00:00 |  1152.44      |        -29.4167   | NEUTRAL  | Yahoo Finance |
| LRCX       | 2026-09-17 00:00:00 |   269.31      |        -33.8333   | NEUTRAL  | Yahoo Finance |
| MS         | 2026-09-17 00:00:00 |   203.52      |        -17.25     | NEUTRAL  | Yahoo Finance |
| MU         | 2026-09-17 00:00:00 |   977.5       |         45        | NEUTRAL  | Yahoo Finance |
| NEM        | 2026-09-17 00:00:00 |   124.39      |          7.16667  | NEUTRAL  | Yahoo Finance |
| NFLX       | 2026-09-17 00:00:00 |    75.31      |        -47        | NEUTRAL  | Yahoo Finance |
| NVDA       | 2026-09-17 00:00:00 |   219.34      |         25.6667   | NEUTRAL  | Yahoo Finance |
| OP-USD     | 2026-09-18 00:00:00 |     0.1128    |         32.3333   | NEUTRAL  | Kraken API    |
| ORCL       | 2026-09-17 00:00:00 |   150.59      |          5.83333  | NEUTRAL  | Yahoo Finance |
| OXY        | 2026-09-17 00:00:00 |    59.29      |         19.3333   | NEUTRAL  | Yahoo Finance |
| PEPE-USD   | 2026-09-18 00:00:00 |     3.652e-06 |         49.5      | NEUTRAL  | Kraken API    |
| PFE        | 2026-09-17 00:00:00 |    27.64      |          4.08333  | NEUTRAL  | Yahoo Finance |
| PG         | 2026-09-17 00:00:00 |   147.55      |         39.8333   | NEUTRAL  | Yahoo Finance |
| PM         | 2026-09-17 00:00:00 |   190.48      |         42.6667   | NEUTRAL  | Yahoo Finance |
| POL-USD    | 2026-09-18 00:00:00 |     0.10074   |         46.5      | NEUTRAL  | Kraken API    |
| QQQ        | 2026-09-17 00:00:00 |   716.92      |         28.1667   | NEUTRAL  | Yahoo Finance |
| RENDER-USD | 2026-09-18 00:00:00 |     1.501     |         14.3333   | NEUTRAL  | Kraken API    |
| SCHW       | 2026-09-17 00:00:00 |   104.63      |        -26.8333   | NEUTRAL  | Yahoo Finance |
| SHIB-USD   | 2026-09-18 00:00:00 |     5.335e-06 |         23        | NEUTRAL  | Kraken API    |
| SLB        | 2026-09-17 00:00:00 |    52.08      |        -19.5833   | NEUTRAL  | Yahoo Finance |
| SLV        | 2026-09-17 00:00:00 |    58.97      |        -24.3333   | NEUTRAL  | Yahoo Finance |
| SMH        | 2026-09-17 00:00:00 |   560.61      |          6.16667  | NEUTRAL  | Yahoo Finance |
| SNX-USD    | 2026-09-18 00:00:00 |     0.2186    |         36.9167   | NEUTRAL  | Kraken API    |
| SOXX       | 2026-09-17 00:00:00 |   519.1       |         26.5833   | NEUTRAL  | Yahoo Finance |
| SPY        | 2026-09-17 00:00:00 |   762.6       |         -2.33333  | NEUTRAL  | Yahoo Finance |
| T          | 2026-09-17 00:00:00 |    25.39      |          5.41667  | NEUTRAL  | Yahoo Finance |
| TIA-USD    | 2026-09-18 00:00:00 |     0.3872    |         28.3333   | NEUTRAL  | Kraken API    |
| TLT        | 2026-09-17 00:00:00 |    81.78      |        -56.3333   | NEUTRAL  | Yahoo Finance |
| TMO        | 2026-09-17 00:00:00 |   658.32      |         63.5      | NEUTRAL  | Yahoo Finance |
| TMUS       | 2026-09-17 00:00:00 |   166.45      |        -57.75     | NEUTRAL  | Yahoo Finance |
| TRX-USD    | 2026-09-18 00:00:00 |     0.335835  |         42.8333   | NEUTRAL  | Kraken API    |
| TSLA       | 2026-09-17 00:00:00 |   366.2       |         28.3333   | NEUTRAL  | Yahoo Finance |
| TXN        | 2026-09-17 00:00:00 |   258.14      |         13.8333   | NEUTRAL  | Yahoo Finance |
| UNH        | 2026-09-17 00:00:00 |   375.21      |        -24.75     | NEUTRAL  | Yahoo Finance |
| UPS        | 2026-09-17 00:00:00 |   100.17      |        -63.3333   | NEUTRAL  | Yahoo Finance |
| VEA        | 2026-09-17 00:00:00 |    72.15      |        -11.3333   | NEUTRAL  | Yahoo Finance |
| VIXY       | 2026-09-17 00:00:00 |    16.98      |        -10.5      | NEUTRAL  | Yahoo Finance |
| VTI        | 2026-09-17 00:00:00 |   375.34      |         -2.33333  | NEUTRAL  | Yahoo Finance |
| VWO        | 2026-09-17 00:00:00 |    59.91      |        -13        | NEUTRAL  | Yahoo Finance |
| VZ         | 2026-09-17 00:00:00 |    48.33      |         -3.83333  | NEUTRAL  | Yahoo Finance |
| WFC        | 2026-09-17 00:00:00 |    86.89      |          6.33333  | NEUTRAL  | Yahoo Finance |
| WIF-USD    | 2026-09-18 00:00:00 |     0.1916    |         11.5833   | NEUTRAL  | Kraken API    |
| WMT        | 2026-09-17 00:00:00 |   106.79      |         -5.08333  | NEUTRAL  | Yahoo Finance |
| XBI        | 2026-09-17 00:00:00 |   158.25      |          4.91667  | NEUTRAL  | Yahoo Finance |
| XLB        | 2026-09-17 00:00:00 |    50.71      |        -31.4167   | NEUTRAL  | Yahoo Finance |
| XLC        | 2026-09-17 00:00:00 |   112.35      |         57.9167   | NEUTRAL  | Yahoo Finance |
| XLE        | 2026-09-17 00:00:00 |    64.48      |         42.8333   | NEUTRAL  | Yahoo Finance |
| XLF        | 2026-09-17 00:00:00 |    55.88      |        -26.5      | NEUTRAL  | Yahoo Finance |
| XLK        | 2026-09-17 00:00:00 |   188.06      |         44.8333   | NEUTRAL  | Yahoo Finance |
| XLM-USD    | 2026-09-18 00:00:00 |     0.18774   |         39.9167   | NEUTRAL  | Kraken API    |
| XLP        | 2026-09-17 00:00:00 |    83.49      |        -61.5833   | NEUTRAL  | Yahoo Finance |
| XOM        | 2026-09-17 00:00:00 |   163.27      |         29.5      | NEUTRAL  | Yahoo Finance |
| XRP-USD    | 2026-09-18 00:00:00 |     1.31962   |        -10.1667   | NEUTRAL  | Kraken API    |
| YFI-USD    | 2026-09-18 00:00:00 |  2157.6       |        -22.3333   | NEUTRAL  | Kraken API    |
| AGG        | 2026-09-17 00:00:00 |    96.33      |        -52.9167   | SHORT    | Yahoo Finance |
| AMAT       | 2026-09-17 00:00:00 |   417.4       |        -45.9167   | SHORT    | Yahoo Finance |
| AVGO       | 2026-09-17 00:00:00 |   347.3       |        -45.75     | SHORT    | Yahoo Finance |
| BA         | 2026-09-17 00:00:00 |   197         |        -50        | SHORT    | Yahoo Finance |
| BLK        | 2026-09-17 00:00:00 |  1053.96      |        -41.8333   | SHORT    | Yahoo Finance |
| BND        | 2026-09-17 00:00:00 |    71.47      |        -52.9167   | SHORT    | Yahoo Finance |
| CMCSA      | 2026-09-17 00:00:00 |    22.91      |        -58.8333   | SHORT    | Yahoo Finance |
| COST       | 2026-09-17 00:00:00 |   893.93      |        -52.9167   | SHORT    | Yahoo Finance |
| GE         | 2026-09-17 00:00:00 |   313.47      |        -57.4167   | SHORT    | Yahoo Finance |
| HD         | 2026-09-17 00:00:00 |   302.51      |        -57.4167   | SHORT    | Yahoo Finance |
| HON        | 2026-09-17 00:00:00 |   206.49      |        -36.5833   | SHORT    | Yahoo Finance |
| HYG        | 2026-09-17 00:00:00 |    78.72      |        -52.9167   | SHORT    | Yahoo Finance |
| IEF        | 2026-09-17 00:00:00 |    91.25      |        -52.9167   | SHORT    | Yahoo Finance |
| ITA        | 2026-09-17 00:00:00 |   213.88      |        -59.0833   | SHORT    | Yahoo Finance |
| LIN        | 2026-09-17 00:00:00 |   458.48      |        -46.0833   | SHORT    | Yahoo Finance |
| MCD        | 2026-09-17 00:00:00 |   248.48      |        -50.75     | SHORT    | Yahoo Finance |
| NKE        | 2026-09-17 00:00:00 |    36.36      |        -52        | SHORT    | Yahoo Finance |
| PEP        | 2026-09-17 00:00:00 |   133.66      |        -55.0833   | SHORT    | Yahoo Finance |
| RTX        | 2026-09-17 00:00:00 |   193.54      |        -35.3333   | SHORT    | Yahoo Finance |
| SBUX       | 2026-09-17 00:00:00 |    96.67      |        -43.8333   | SHORT    | Yahoo Finance |
| SHY        | 2026-09-17 00:00:00 |    81.36      |        -53.4167   | SHORT    | Yahoo Finance |
| SKY-USD    | 2026-09-18 00:00:00 |     0.06181   |        -51.0833   | SHORT    | Kraken API    |
| VNQ        | 2026-09-17 00:00:00 |    93.81      |        -41.8333   | SHORT    | Yahoo Finance |
| XLI        | 2026-09-17 00:00:00 |   169.01      |        -51.6667   | SHORT    | Yahoo Finance |
| XLU        | 2026-09-17 00:00:00 |    41.69      |        -51.5833   | SHORT    | Yahoo Finance |
| XLY        | 2026-09-17 00:00:00 |   111.39      |        -48.25     | SHORT    | Yahoo Finance |

## Edge Summary

- Symbols with trades: **160** of 160
- Beat buy-and-hold: **30.00%** of traded symbols
- Positive return: **28.12%** of traded symbols
- Median strategy return: **-10.11%** (benchmark **23.53%**)
- Median excess vs benchmark: **-30.83%**
- Median Sharpe: **-0.16**
- Median exposure: **44.44%**

> Edge is real only if both _beat buy-and-hold_ and _median excess_ are convincingly positive across many symbols. Treat a single high-return symbol as noise.

## Portfolio Backtest

Actual capital-allocation books (not per-symbol averages). Benchmarks: `equal_weight_buyhold` (whole tracked universe), `spy_buyhold` (100% SPY), and `sixty_forty` (60% SPY / 40% AGG). `high_conf_voltarget` inverse-vol-weights the HIGH-confidence book; `conviction_long_short` is market-neutral. Judge on **Sharpe** and **max_drawdown** out-of-sample, not raw return: a fully-invested long book wins on return in a bull market but carries all the risk.

| strategy              | scope         | ann_return   | ann_vol   |   sharpe | max_drawdown   | total_return   |   avg_gross_exposure |
|:----------------------|:--------------|:-------------|:----------|---------:|:---------------|:---------------|---------------------:|
| equal_weight_buyhold  | full          | 12.16%       | 28.28%    |     0.43 | -39.63%        | 28.17%         |                 1    |
| equal_weight_buyhold  | out_of_sample | 12.36%       | 27.96%    |     0.44 | -29.33%        | 9.47%          |                 1    |
| all_signals_ew        | full          | -20.56%      | 23.82%    |    -0.86 | -63.45%        | -50.94%        |                 1    |
| all_signals_ew        | out_of_sample | 9.25%        | 23.18%    |     0.4  | -22.52%        | 7.29%          |                 1    |
| high_conf_ew          | full          | -0.13%       | 30.68%    |    -0    | -43.82%        | -13.50%        |                 0.89 |
| high_conf_ew          | out_of_sample | 30.26%       | 26.92%    |     1.12 | -22.85%        | 32.82%         |                 0.89 |
| high_conf_voltarget   | full          | -1.01%       | 27.47%    |    -0.04 | -37.20%        | -13.33%        |                 0.89 |
| high_conf_voltarget   | out_of_sample | 16.77%       | 22.65%    |     0.74 | -16.94%        | 16.30%         |                 0.89 |
| conviction_long_short | full          | -17.53%      | 22.43%    |    -0.78 | -50.00%        | -45.71%        |                 0.97 |
| conviction_long_short | out_of_sample | -11.93%      | 20.34%    |    -0.59 | -26.12%        | -13.89%        |                 0.97 |
| spy_buyhold           | full          | 7.11%        | 13.51%    |     0.53 | -19.00%        | 20.74%         |                 0.79 |
| spy_buyhold           | out_of_sample | 1.38%        | 9.89%     |     0.14 | -12.06%        | 0.96%          |                 0.79 |
| sixty_forty           | full          | 4.33%        | 8.54%     |     0.51 | -11.66%        | 12.81%         |                 0.79 |
| sixty_forty           | out_of_sample | -0.94%       | 6.63%     |    -0.14 | -8.26%         | -1.23%         |                 0.79 |

## Walk-Forward Robustness

Each book measured across contiguous time folds (each a different regime). A book has durable edge only if `mean_sharpe` is positive, `min_sharpe` isn't deeply negative, and `pct_positive_folds` is high — a single great fold doesn't count. `fold_sharpes` lists each fold oldest-to-newest.

| strategy              |   n_folds |   mean_sharpe |   median_sharpe |   min_sharpe | pct_positive_folds   | mean_return   | fold_sharpes                  |
|:----------------------|----------:|--------------:|----------------:|-------------:|:---------------------|:--------------|:------------------------------|
| equal_weight_buyhold  |         5 |          0.71 |            0.82 |        -0.97 | 80.00%               | 6.07%         | 1.86;0.82;0.55;-0.97;1.26     |
| all_signals_ew        |         5 |         -0.93 |           -1.05 |        -2.44 | 20.00%               | -10.62%       | -1.05;-2.44;-2.23;1.46;-0.39  |
| high_conf_ew          |         5 |          0.02 |           -0.16 |        -1.66 | 40.00%               | -1.48%        | -0.16;-1.66;-0.24;1.04;1.12   |
| high_conf_voltarget   |         5 |          0.01 |            0.32 |        -1.68 | 60.00%               | -2.24%        | 0.32;-1.68;-0.14;0.48;1.08    |
| conviction_long_short |         5 |         -0.81 |           -0.77 |        -2    | 0.00%                | -11.18%       | -2.00;-0.77;-0.98;-0.10;-0.19 |
| spy_buyhold           |         5 |          0.63 |            0.36 |        -0.13 | 80.00%               | 4.14%         | 2.40;-0.13;0.36;0.05;0.49     |
| sixty_forty           |         5 |          0.59 |            0.14 |        -0.12 | 60.00%               | 2.58%         | 2.56;-0.12;0.47;-0.11;0.14    |

## Strategy Comparison

Each decision rule backtested over the same data. `out_of_sample` is the most recent ~35% of each symbol's history (unseen tail). A rule has real edge only if `median_excess` and `beat_benchmark_pct` stay positive out-of-sample, not just full-sample.

| strategy        | scope         |   symbols | beat_benchmark_pct   | positive_pct   | median_return   | median_benchmark   | median_excess   |   median_sharpe |   total_trades |
|:----------------|:--------------|----------:|:---------------------|:---------------|:----------------|:-------------------|:----------------|----------------:|---------------:|
| trend           | full          |       160 | 30.00%               | 28.12%         | -10.11%         | 23.53%             | -30.83%         |           -0.16 |          11369 |
| trend           | out_of_sample |       160 | 25.62%               | 48.12%         | -0.59%          | 10.44%             | -11.71%         |            0.04 |           3751 |
| mean_reversion  | full          |       156 | 34.62%               | 48.08%         | -0.22%          | 21.94%             | -22.16%         |           -0.01 |           1272 |
| mean_reversion  | out_of_sample |       119 | 31.93%               | 57.14%         | 0.39%           | 8.47%              | -10.30%         |            0.22 |            492 |
| regime_adaptive | full          |       160 | 28.75%               | 28.75%         | -10.84%         | 23.53%             | -30.68%         |           -0.14 |          11634 |
| regime_adaptive | out_of_sample |       160 | 26.88%               | 48.75%         | -0.62%          | 10.44%             | -11.94%         |            0.06 |           3885 |

## Signal Calibration

Realized forward return in the signal's direction, grouped by confidence. HIGH should outrank LOW for the confidence score to be meaningful.

| confidence_level   |   horizon |     n | mean_return   | median_return   | win_rate   |
|:-------------------|----------:|------:|:--------------|:----------------|:-----------|
| HIGH               |         5 |  7939 | 0.13%         | 0.07%           | 51.18%     |
| MEDIUM             |         5 | 28869 | -0.04%        | 0.01%           | 50.09%     |
| LOW                |         5 |  3596 | -0.47%        | -0.51%          | 45.36%     |
| ALL                |         5 | 40404 | -0.04%        | 0.00%           | 49.88%     |
| HIGH               |        10 |  7904 | 0.38%         | 0.08%           | 50.97%     |
| MEDIUM             |        10 | 28646 | 0.09%         | 0.05%           | 50.42%     |
| LOW                |        10 |  3554 | -0.81%        | -0.63%          | 45.95%     |
| ALL                |        10 | 40104 | 0.07%         | 0.02%           | 50.13%     |
| HIGH               |        20 |  7751 | 0.89%         | 0.32%           | 52.70%     |
| MEDIUM             |        20 | 28122 | 0.71%         | 0.53%           | 52.98%     |
| LOW                |        20 |  3447 | -0.84%        | -0.60%          | 47.03%     |
| ALL                |        20 | 39320 | 0.61%         | 0.41%           | 52.41%     |

## Backtest Summary

### Data Quality / Signal Availability

- **ok**: 160 symbols

| symbol     |   trades | return   | benchmark_return   | mdd     |   sharpe | exposure   | skipped_reason   |
|:-----------|---------:|:---------|:-------------------|:--------|---------:|:-----------|:-----------------|
| AAPL       |       62 | 10.43%   | 98.36%             | -23.09% |     0.3  | 49.92%     | ok               |
| AAVE-USD   |       73 | -37.51%  | -0.35%             | -66.17% |    -0.24 | 41.57%     | ok               |
| ABBV       |       70 | -25.71%  | 57.82%             | -30.52% |    -0.58 | 47.92%     | ok               |
| ADA-USD    |       79 | -39.45%  | -64.93%            | -45.96% |    -0.33 | 46.55%     | ok               |
| ADBE       |       69 | -14.28%  | -46.63%            | -31.20% |    -0.07 | 55.57%     | ok               |
| AGG        |       71 | -7.89%   | 1.27%              | -10.23% |    -1.32 | 32.45%     | ok               |
| ALGO-USD   |       80 | -34.91%  | -47.82%            | -43.00% |    -0.29 | 39.27%     | ok               |
| AMAT       |       67 | -31.35%  | 111.34%            | -57.08% |    -0.27 | 49.58%     | ok               |
| AMD        |       52 | 11.68%   | 254.51%            | -41.09% |     0.32 | 34.44%     | ok               |
| AMGN       |       67 | -6.80%   | 40.98%             | -34.19% |    -0.04 | 50.58%     | ok               |
| AMZN       |       82 | -55.80%  | 44.64%             | -56.90% |    -1.59 | 41.76%     | ok               |
| APT-USD    |       78 | -41.85%  | -85.52%            | -65.32% |    -0.27 | 40.23%     | ok               |
| ARB-USD    |       77 | -18.33%  | -19.72%            | -58.79% |     0.1  | 42.34%     | ok               |
| ARKK       |       88 | -29.50%  | 99.31%             | -31.32% |    -0.44 | 43.59%     | ok               |
| ATOM-USD   |       88 | -60.00%  | -59.34%            | -61.22% |    -0.89 | 46.74%     | ok               |
| AVAX-USD   |       72 | -37.60%  | -58.63%            | -45.19% |    -0.38 | 38.12%     | ok               |
| AVGO       |       64 | 23.60%   | 168.31%            | -36.08% |     0.43 | 41.76%     | ok               |
| BA         |       71 | 0.10%    | 18.10%             | -26.77% |     0.13 | 49.42%     | ok               |
| BAC        |       76 | -13.81%  | 53.47%             | -26.64% |    -0.31 | 48.09%     | ok               |
| BCH-USD    |       78 | 23.02%   | -23.42%            | -53.87% |     0.44 | 49.04%     | ok               |
| BITO       |       76 | -14.59%  | -63.57%            | -39.47% |    -0.03 | 39.93%     | ok               |
| BLK        |       83 | -9.21%   | 39.11%             | -26.90% |    -0.18 | 48.75%     | ok               |
| BND        |       71 | -8.40%   | 1.28%              | -10.37% |    -1.34 | 34.44%     | ok               |
| BONK-USD   |       76 | 26.45%   | -76.11%            | -45.22% |     0.48 | 44.44%     | ok               |
| BTC-USD    |       68 | 21.31%   | -7.69%             | -23.38% |     0.48 | 52.30%     | ok               |
| C          |       77 | -35.16%  | 114.76%            | -41.08% |    -0.76 | 47.92%     | ok               |
| CAT        |       70 | 10.17%   | 136.26%            | -18.88% |     0.29 | 49.58%     | ok               |
| CL         |       60 | 4.27%    | -1.75%             | -14.32% |     0.2  | 40.77%     | ok               |
| CMCSA      |       82 | -42.19%  | -35.45%            | -47.67% |    -1.09 | 42.10%     | ok               |
| COMP-USD   |       97 | -46.68%  | -49.89%            | -56.58% |    -0.37 | 47.89%     | ok               |
| COP        |       70 | -19.17%  | 2.37%              | -43.40% |    -0.29 | 44.43%     | ok               |
| COST       |       62 | 2.10%    | 23.84%             | -29.73% |     0.13 | 41.76%     | ok               |
| CRM        |       67 | -30.48%  | -11.09%            | -45.51% |    -0.42 | 46.42%     | ok               |
| CRV-USD    |       68 | 37.75%   | -41.78%            | -39.89% |     0.55 | 41.57%     | ok               |
| CSCO       |       59 | 18.08%   | 129.19%            | -21.79% |     0.42 | 47.92%     | ok               |
| CVX        |       73 | -9.75%   | 28.01%             | -27.78% |    -0.19 | 41.76%     | ok               |
| DASH-USD   |       57 | -5.35%   | 198.00%            | -64.43% |     0.34 | 29.31%     | ok               |
| DBC        |       64 | -4.71%   | 39.81%             | -24.66% |    -0.09 | 34.44%     | ok               |
| DE         |       74 | -9.86%   | 73.99%             | -22.93% |    -0.12 | 44.59%     | ok               |
| DIA        |       64 | -4.94%   | 36.08%             | -12.94% |    -0.23 | 45.26%     | ok               |
| DIS        |       66 | -14.81%  | -6.58%             | -28.17% |    -0.24 | 43.76%     | ok               |
| DOGE-USD   |       71 | -31.40%  | -45.22%            | -60.95% |    -0.11 | 48.66%     | ok               |
| DOT-USD    |       94 | -62.13%  | -68.12%            | -65.79% |    -0.67 | 48.08%     | ok               |
| DXY-INDEX  |       42 | -3.46%   | -6.08%             | -6.02%  |    -0.54 | 30.30%     | ok               |
| EEM        |       62 | -10.07%  | 64.40%             | -25.38% |    -0.27 | 41.60%     | ok               |
| EFA        |       62 | -11.52%  | 37.11%             | -14.58% |    -0.45 | 42.43%     | ok               |
| EOG        |       81 | -31.44%  | 7.47%              | -48.55% |    -0.69 | 45.26%     | ok               |
| ETC-USD    |       60 | -30.18%  | -47.57%            | -45.54% |    -0.39 | 27.78%     | ok               |
| ETH-USD    |       60 | 156.11%  | 55.45%             | -30.11% |     1.35 | 45.79%     | ok               |
| EWJ        |       64 | -23.51%  | 47.10%             | -29.40% |    -0.82 | 37.10%     | ok               |
| FCX        |       65 | -28.39%  | 43.42%             | -46.84% |    -0.3  | 44.59%     | ok               |
| FET-USD    |       75 | -27.47%  | -60.62%            | -60.12% |    -0.04 | 39.66%     | ok               |
| FIL-USD    |       69 | -60.58%  | -64.21%            | -62.21% |    -0.93 | 32.57%     | ok               |
| FXI        |       48 | -5.41%   | 34.39%             | -24.33% |    -0.05 | 32.28%     | ok               |
| GDX        |       60 | -1.14%   | 179.41%            | -34.99% |     0.12 | 44.93%     | ok               |
| GDXJ       |       68 | -35.32%  | 194.43%            | -44.61% |    -0.45 | 42.93%     | ok               |
| GE         |       80 | -14.76%  | 94.39%             | -27.82% |    -0.17 | 47.75%     | ok               |
| GLD        |       54 | 8.43%    | 84.49%             | -14.86% |     0.28 | 44.93%     | ok               |
| GOOGL      |       55 | 64.10%   | 122.65%            | -20.41% |     1.05 | 47.42%     | ok               |
| GRT-USD    |       85 | -26.48%  | -75.25%            | -53.91% |    -0.16 | 41.95%     | ok               |
| GS         |       66 | -3.01%   | 126.51%            | -22.13% |     0.03 | 47.42%     | ok               |
| HD         |       75 | -6.70%   | -8.88%             | -18.84% |    -0.1  | 42.26%     | ok               |
| HON        |       90 | -23.52%  | 8.23%              | -33.57% |    -0.56 | 55.91%     | ok               |
| HYG        |       87 | -9.06%   | 3.06%              | -10.59% |    -1.04 | 36.27%     | ok               |
| IBIT       |       36 | 28.83%   | 13.92%             | -18.95% |     0.6  | 32.70%     | ok               |
| IBM        |       73 | -25.87%  | 40.76%             | -48.94% |    -0.31 | 50.75%     | ok               |
| ICP-USD    |       77 | -7.44%   | -41.53%            | -47.52% |     0.18 | 36.02%     | ok               |
| IEF        |       86 | -13.29%  | 0.01%              | -13.47% |    -1.9  | 32.61%     | ok               |
| IEMG       |       62 | -11.00%  | 59.06%             | -29.45% |    -0.32 | 41.76%     | ok               |
| INJ-USD    |       71 | -49.40%  | -24.13%            | -74.43% |    -0.42 | 37.93%     | ok               |
| INTC       |       68 | 55.27%   | 209.88%            | -60.60% |     0.61 | 48.25%     | ok               |
| INTU       |       71 | -18.57%  | -50.01%            | -42.60% |    -0.19 | 44.43%     | ok               |
| ITA        |       72 | -0.78%   | 65.79%             | -23.75% |     0.06 | 48.92%     | ok               |
| IWM        |       54 | 11.41%   | 45.27%             | -12.65% |     0.46 | 36.44%     | ok               |
| JNJ        |       68 | -1.50%   | 84.05%             | -17.51% |     0.01 | 47.25%     | ok               |
| JPM        |       73 | -20.40%  | 80.64%             | -32.74% |    -0.53 | 48.09%     | ok               |
| KO         |       54 | 25.74%   | 42.63%             | -8.64%  |     0.9  | 39.93%     | ok               |
| LDO-USD    |       72 | -2.84%   | -44.74%            | -62.63% |     0.25 | 45.98%     | ok               |
| LIN        |       72 | -9.77%   | 3.30%              | -20.61% |    -0.3  | 36.61%     | ok               |
| LINK-USD   |       72 | 38.81%   | -4.23%             | -33.64% |     0.57 | 45.40%     | ok               |
| LLY        |       71 | -30.60%  | 58.99%             | -53.34% |    -0.47 | 48.59%     | ok               |
| LRCX       |       84 | -25.21%  | 198.75%            | -61.08% |    -0.15 | 42.43%     | ok               |
| LTC-USD    |       72 | -10.15%  | -27.73%            | -33.94% |     0.05 | 51.53%     | ok               |
| MCD        |       77 | -4.85%   | -9.84%             | -21.88% |    -0.14 | 37.77%     | ok               |
| META       |       78 | -32.20%  | 54.59%             | -44.52% |    -0.55 | 48.25%     | ok               |
| MPC        |       67 | 12.58%   | 111.50%            | -37.91% |     0.32 | 50.25%     | ok               |
| MRK        |       65 | -23.79%  | 12.57%             | -35.95% |    -0.46 | 44.09%     | ok               |
| MS         |       75 | -10.75%  | 119.88%            | -27.79% |    -0.19 | 47.42%     | ok               |
| MSFT       |       81 | -30.21%  | 24.74%             | -38.06% |    -0.7  | 49.58%     | ok               |
| MU         |       49 | 164.65%  | 776.05%            | -68.76% |     1.08 | 53.91%     | ok               |
| NEAR-USD   |       73 | 48.74%   | 68.86%             | -60.10% |     0.62 | 42.34%     | ok               |
| NEM        |       66 | -26.61%  | 186.55%            | -39.56% |    -0.26 | 52.75%     | ok               |
| NFLX       |       76 | 12.79%   | 33.34%             | -21.09% |     0.35 | 53.24%     | ok               |
| NKE        |       79 | -28.19%  | -61.29%            | -55.35% |    -0.32 | 44.09%     | ok               |
| NOW        |       86 | 8.77%    | -3.34%             | -30.43% |     0.28 | 50.42%     | ok               |
| NVDA       |       77 | -41.45%  | 85.71%             | -52.37% |    -0.5  | 57.04%     | ok               |
| OP-USD     |       70 | -44.56%  | -82.29%            | -68.74% |    -0.39 | 32.76%     | ok               |
| ORCL       |       66 | 87.77%   | 31.07%             | -30.61% |     0.81 | 54.74%     | ok               |
| OXY        |       71 | -3.27%   | -12.65%            | -29.80% |     0.07 | 42.76%     | ok               |
| PEP        |       76 | -3.51%   | -24.35%            | -21.35% |    -0.04 | 45.92%     | ok               |
| PEPE-USD   |       89 | -36.93%  | -47.87%            | -55.59% |    -0.12 | 47.89%     | ok               |
| PFE        |       83 | -38.28%  | 9.42%              | -43.18% |    -1.16 | 39.27%     | ok               |
| PG         |       64 | -21.96%  | -9.23%             | -24.25% |    -0.87 | 36.77%     | ok               |
| PM         |       79 | -3.76%   | 98.23%             | -35.15% |     0.01 | 53.24%     | ok               |
| POL-USD    |       87 | 19.85%   | -43.93%            | -45.67% |     0.42 | 49.23%     | ok               |
| QCOM       |       75 | -16.91%  | 15.56%             | -57.69% |    -0.07 | 43.09%     | ok               |
| QQQ        |       66 | 13.22%   | 68.91%             | -14.20% |     0.41 | 46.42%     | ok               |
| RENDER-USD |      100 | -40.65%  | -59.73%            | -46.98% |    -0.21 | 45.59%     | ok               |
| RTX        |       60 | 35.11%   | 90.29%             | -16.99% |     0.78 | 52.75%     | ok               |
| SBUX       |       58 | -15.40%  | 10.05%             | -29.22% |    -0.26 | 38.27%     | ok               |
| SCHW       |       78 | -15.83%  | 39.71%             | -31.92% |    -0.32 | 47.25%     | ok               |
| SHIB-USD   |       84 | -43.42%  | -54.32%            | -45.01% |    -0.47 | 51.92%     | ok               |
| SHY        |       48 | -2.04%   | 0.21%              | -3.18%  |    -0.7  | 35.11%     | ok               |
| SKY-USD    |       84 | -40.61%  | 6.88%              | -52.23% |    -0.51 | 45.56%     | ok               |
| SLB        |       75 | -35.61%  | 5.34%              | -56.30% |    -0.66 | 49.42%     | ok               |
| SLV        |       70 | 13.57%   | 135.32%            | -42.66% |     0.34 | 41.43%     | ok               |
| SMH        |       48 | 67.47%   | 164.19%            | -34.29% |     0.99 | 44.93%     | ok               |
| SNX-USD    |       62 | -20.22%  | -65.14%            | -47.16% |    -0.03 | 32.76%     | ok               |
| SOL-USD    |       68 | -8.57%   | -16.78%            | -44.99% |     0.13 | 59.77%     | ok               |
| SOXX       |       56 | 69.47%   | 144.39%            | -39.81% |     0.95 | 43.26%     | ok               |
| SPY        |       64 | 3.49%    | 51.46%             | -15.53% |     0.18 | 51.58%     | ok               |
| SUSHI-USD  |      105 | -82.02%  | -55.92%            | -83.31% |    -1.42 | 37.74%     | ok               |
| T          |       70 | 42.64%   | 53.14%             | -17.01% |     0.89 | 58.40%     | ok               |
| TGT        |       60 | -12.70%  | -2.80%             | -36.37% |    -0.2  | 37.77%     | ok               |
| TIA-USD    |       91 | -65.50%  | -84.09%            | -75.38% |    -0.68 | 40.80%     | ok               |
| TLT        |       72 | -20.14%  | -6.84%             | -21.87% |    -1.49 | 34.28%     | ok               |
| TMO        |       67 | 27.91%   | 15.15%             | -18.85% |     0.59 | 54.41%     | ok               |
| TMUS       |       76 | 2.41%    | 1.46%              | -27.06% |     0.15 | 48.25%     | ok               |
| TRX-USD    |       68 | 10.93%   | 34.15%             | -22.90% |     0.38 | 52.30%     | ok               |
| TSLA       |       80 | -35.03%  | 115.18%            | -58.36% |    -0.22 | 43.09%     | ok               |
| TXN        |       75 | -23.22%  | 47.30%             | -48.70% |    -0.23 | 49.92%     | ok               |
| UNH        |       73 | 31.20%   | -24.03%            | -26.31% |     0.53 | 50.08%     | ok               |
| UNI-USD    |       94 | -54.49%  | 65.23%             | -78.80% |    -0.38 | 48.66%     | ok               |
| UPS        |       70 | -34.92%  | -32.04%            | -38.32% |    -0.69 | 40.10%     | ok               |
| USO        |       70 | 10.16%   | 93.08%             | -41.71% |     0.28 | 32.78%     | ok               |
| VEA        |       58 | -2.07%   | 48.70%             | -16.01% |    -0.03 | 43.26%     | ok               |
| VIXY       |       96 | -76.58%  | -69.24%            | -88.17% |    -0.88 | 34.11%     | ok               |
| VNQ        |       77 | -17.72%  | 17.09%             | -24.92% |    -0.75 | 38.60%     | ok               |
| VTI        |       70 | -5.97%   | 50.46%             | -17.64% |    -0.16 | 51.75%     | ok               |
| VWO        |       80 | -16.33%  | 43.19%             | -24.94% |    -0.6  | 41.93%     | ok               |
| VZ         |       82 | -18.51%  | 23.23%             | -25.90% |    -0.53 | 40.93%     | ok               |
| WFC        |       80 | -17.12%  | 44.99%             | -28.90% |    -0.28 | 46.92%     | ok               |
| WIF-USD    |       66 | -26.92%  | -50.49%            | -52.76% |    -0.02 | 35.63%     | ok               |
| WMT        |       65 | 10.38%   | 77.36%             | -21.98% |     0.35 | 48.09%     | ok               |
| XBI        |       66 | -0.88%   | 92.47%             | -18.30% |     0.07 | 41.76%     | ok               |
| XLB        |       60 | -12.29%  | 13.99%             | -25.04% |    -0.43 | 31.95%     | ok               |
| XLC        |       63 | 14.20%   | 44.11%             | -12.33% |     0.52 | 50.58%     | ok               |
| XLE        |       73 | -13.93%  | 33.46%             | -34.24% |    -0.28 | 44.76%     | ok               |
| XLF        |       80 | -9.66%   | 36.69%             | -23.61% |    -0.3  | 45.92%     | ok               |
| XLI        |       76 | -5.41%   | 38.01%             | -14.16% |    -0.16 | 41.60%     | ok               |
| XLK        |       40 | 72.44%   | 90.34%             | -14.75% |     1.29 | 47.59%     | ok               |
| XLM-USD    |       67 | -12.91%  | -20.34%            | -54.58% |     0.07 | 46.36%     | ok               |
| XLP        |       64 | 8.27%    | 10.22%             | -8.96%  |     0.5  | 38.94%     | ok               |
| XLU        |       67 | -3.52%   | 24.60%             | -20.40% |    -0.11 | 39.27%     | ok               |
| XLV        |       68 | -15.65%  | 20.65%             | -19.39% |    -0.71 | 37.27%     | ok               |
| XLY        |       79 | -6.37%   | 27.78%             | -17.65% |    -0.13 | 46.26%     | ok               |
| XOM        |       59 | -2.37%   | 34.57%             | -20.29% |     0.01 | 34.61%     | ok               |
| XRP-USD    |       60 | 9.21%    | -36.72%            | -33.91% |     0.3  | 36.59%     | ok               |
| YFI-USD    |       79 | -67.17%  | -51.84%            | -72.54% |    -1.2  | 38.31%     | ok               |
| ZEC-USD    |       64 | 172.60%  | 4733.61%           | -56.50% |     0.98 | 41.38%     | ok               |

## AAPL Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 17.33%   | 98.36%             | -22.53% |     0.41 |       71 | 54.74%     | ok               |
|          15 | 13.09%   | 98.36%             | -24.50% |     0.34 |       82 | 61.90%     | ok               |
|          40 | 10.52%   | 98.36%             | -28.08% |     0.31 |       56 | 44.59%     | ok               |
|          30 | 10.43%   | 98.36%             | -23.09% |     0.3  |       62 | 49.92%     | ok               |
|          35 | 8.84%    | 98.36%             | -24.45% |     0.28 |       62 | 48.59%     | ok               |

## AAVE-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 36.85%   | -0.35%             | -43.61% |     0.56 |       43 | 34.67%     | ok               |
|          45 | 24.10%   | -0.35%             | -49.19% |     0.45 |       48 | 29.50%     | ok               |
|          35 | 19.38%   | -0.35%             | -48.79% |     0.41 |       51 | 37.74%     | ok               |
|          50 | 10.25%   | -0.35%             | -45.07% |     0.31 |       44 | 22.03%     | ok               |
|          15 | -29.31%  | -0.35%             | -61.76% |    -0.02 |       76 | 55.75%     | ok               |

## ABBV Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -14.35%  | 57.82%             | -26.55% |    -0.31 |       52 | 35.44%     | ok               |
|          30 | -25.71%  | 57.82%             | -30.52% |    -0.58 |       70 | 47.92%     | ok               |
|          40 | -23.90%  | 57.82%             | -27.36% |    -0.58 |       70 | 40.10%     | ok               |
|          45 | -23.98%  | 57.82%             | -27.66% |    -0.59 |       62 | 37.27%     | ok               |
|          25 | -29.30%  | 57.82%             | -34.88% |    -0.66 |       70 | 50.08%     | ok               |

## ADA-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 18.28%   | -64.93%            | -35.54% |     0.41 |       48 | 25.67%     | ok               |
|          45 | 6.71%    | -64.93%            | -34.64% |     0.28 |       49 | 30.46%     | ok               |
|          40 | -12.26%  | -64.93%            | -40.73% |     0.06 |       61 | 36.59%     | ok               |
|          35 | -21.41%  | -64.93%            | -42.89% |    -0.05 |       67 | 41.00%     | ok               |
|          15 | -34.77%  | -64.93%            | -47.27% |    -0.1  |       73 | 63.03%     | ok               |

## ADBE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | 2.93%    | -46.63%            | -29.07% |     0.19 |       53 | 59.23%     | ok               |
|          35 | -4.62%   | -46.63%            | -30.52% |     0.05 |       76 | 47.25%     | ok               |
|          20 | -12.36%  | -46.63%            | -31.52% |    -0.03 |       59 | 62.40%     | ok               |
|          30 | -14.28%  | -46.63%            | -31.20% |    -0.07 |       69 | 55.57%     | ok               |
|          15 | -19.18%  | -46.63%            | -34.98% |    -0.13 |       66 | 64.23%     | ok               |

## AGG Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -5.80%   | 1.27%              | -8.07%  |    -1.25 |       54 | 18.64%     | ok               |
|          45 | -6.73%   | 1.27%              | -8.72%  |    -1.31 |       60 | 23.13%     | ok               |
|          30 | -7.89%   | 1.27%              | -10.23% |    -1.32 |       71 | 32.45%     | ok               |
|          20 | -9.40%   | 1.27%              | -11.55% |    -1.39 |       73 | 37.94%     | ok               |
|          25 | -9.57%   | 1.27%              | -12.19% |    -1.48 |       73 | 36.27%     | ok               |

## ALGO-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -34.91%  | -47.82%            | -43.00% |    -0.29 |       80 | 39.27%     | ok               |
|          15 | -40.56%  | -47.82%            | -51.70% |    -0.3  |       80 | 50.19%     | ok               |
|          25 | -44.02%  | -47.82%            | -59.19% |    -0.41 |       80 | 44.83%     | ok               |
|          20 | -46.81%  | -47.82%            | -55.13% |    -0.44 |       82 | 47.70%     | ok               |
|          35 | -46.20%  | -47.82%            | -49.75% |    -0.62 |       62 | 32.76%     | ok               |

## AMAT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -24.11%  | 111.34%            | -53.90% |    -0.11 |       68 | 58.74%     | ok               |
|          30 | -31.35%  | 111.34%            | -57.08% |    -0.27 |       67 | 49.58%     | ok               |
|          35 | -31.06%  | 111.34%            | -54.63% |    -0.28 |       67 | 47.09%     | ok               |
|          50 | -29.89%  | 111.34%            | -47.29% |    -0.3  |       46 | 35.11%     | ok               |
|          40 | -34.79%  | 111.34%            | -55.84% |    -0.36 |       65 | 42.43%     | ok               |

## AMD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 14.50%   | 254.51%            | -40.05% |     0.34 |       56 | 29.45%     | ok               |
|          40 | 11.68%   | 254.51%            | -41.09% |     0.32 |       52 | 34.44%     | ok               |
|          35 | 9.37%    | 254.51%            | -43.15% |     0.3  |       60 | 35.94%     | ok               |
|          30 | 0.73%    | 254.51%            | -46.73% |     0.22 |       61 | 38.60%     | ok               |
|          25 | -6.18%   | 254.51%            | -52.51% |     0.16 |       61 | 41.26%     | ok               |

## AMGN Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -0.73%   | 40.98%             | -26.65% |     0.09 |       64 | 56.24%     | ok               |
|          35 | -4.38%   | 40.98%             | -31.29% |     0.01 |       67 | 47.09%     | ok               |
|          15 | -5.49%   | 40.98%             | -27.98% |     0    |       63 | 60.23%     | ok               |
|          30 | -6.80%   | 40.98%             | -34.19% |    -0.04 |       67 | 50.58%     | ok               |
|          25 | -8.86%   | 40.98%             | -33.47% |    -0.08 |       61 | 52.91%     | ok               |

## AMZN Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -26.84%  | 44.64%             | -28.95% |    -0.81 |       56 | 30.62%     | ok               |
|          50 | -31.32%  | 44.64%             | -33.94% |    -1.13 |       52 | 23.63%     | ok               |
|          45 | -36.48%  | 44.64%             | -37.70% |    -1.29 |       58 | 27.12%     | ok               |
|          35 | -50.72%  | 44.64%             | -51.56% |    -1.47 |       75 | 35.77%     | ok               |
|          30 | -55.80%  | 44.64%             | -56.90% |    -1.59 |       82 | 41.76%     | ok               |

## APT-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -3.75%   | -85.52%            | -41.46% |     0.1  |       42 | 16.86%     | ok               |
|          45 | -23.53%  | -85.52%            | -58.72% |    -0.14 |       56 | 22.99%     | ok               |
|          20 | -37.66%  | -85.52%            | -66.07% |    -0.17 |       84 | 49.23%     | ok               |
|          35 | -34.80%  | -85.52%            | -57.57% |    -0.23 |       72 | 33.72%     | ok               |
|          30 | -41.85%  | -85.52%            | -65.32% |    -0.27 |       78 | 40.23%     | ok               |

## ARB-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 53.93%   | -19.72%            | -45.20% |     0.63 |       83 | 59.20%     | ok               |
|          45 | 38.29%   | -19.72%            | -37.90% |     0.55 |       56 | 24.71%     | ok               |
|          50 | 28.79%   | -19.72%            | -32.02% |     0.48 |       44 | 17.62%     | ok               |
|          20 | 18.32%   | -19.72%            | -53.77% |     0.44 |       69 | 53.07%     | ok               |
|          40 | 17.93%   | -19.72%            | -40.02% |     0.41 |       57 | 32.38%     | ok               |

## ARKK Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -19.18%  | 99.31%             | -37.76% |    -0.15 |       95 | 56.07%     | ok               |
|          20 | -25.64%  | 99.31%             | -34.82% |    -0.29 |       91 | 51.08%     | ok               |
|          30 | -29.50%  | 99.31%             | -31.32% |    -0.44 |       88 | 43.59%     | ok               |
|          35 | -35.76%  | 99.31%             | -36.46% |    -0.62 |       88 | 41.10%     | ok               |
|          40 | -35.40%  | 99.31%             | -40.75% |    -0.64 |       80 | 36.77%     | ok               |

## ATOM-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -42.12%  | -59.34%            | -48.20% |    -0.36 |       86 | 63.98%     | ok               |
|          25 | -49.57%  | -59.34%            | -52.95% |    -0.56 |       90 | 52.87%     | ok               |
|          20 | -57.02%  | -59.34%            | -59.03% |    -0.72 |       94 | 56.70%     | ok               |
|          30 | -60.00%  | -59.34%            | -61.22% |    -0.89 |       88 | 46.74%     | ok               |
|          45 | -56.83%  | -59.34%            | -57.44% |    -1    |       76 | 31.61%     | ok               |

## AVAX-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 26.00%   | -58.63%            | -22.06% |     0.53 |       30 | 17.05%     | ok               |
|          40 | 18.88%   | -58.63%            | -26.27% |     0.42 |       32 | 24.14%     | ok               |
|          45 | 15.54%   | -58.63%            | -23.19% |     0.38 |       26 | 21.07%     | ok               |
|          35 | -2.83%   | -58.63%            | -33.05% |     0.14 |       52 | 30.46%     | ok               |
|          15 | -12.08%  | -58.63%            | -42.39% |     0.1  |       74 | 52.30%     | ok               |

## AVGO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | 27.15%   | 168.31%            | -38.01% |     0.46 |       68 | 44.43%     | ok               |
|          30 | 23.60%   | 168.31%            | -36.08% |     0.43 |       64 | 41.76%     | ok               |
|          20 | 12.57%   | 168.31%            | -39.42% |     0.32 |       77 | 47.59%     | ok               |
|          50 | 10.84%   | 168.31%            | -36.86% |     0.29 |       56 | 29.78%     | ok               |
|          40 | 10.50%   | 168.31%            | -40.70% |     0.29 |       66 | 35.44%     | ok               |

## BA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 28.77%   | 18.10%             | -13.34% |     0.72 |       46 | 32.95%     | ok               |
|          35 | 21.38%   | 18.10%             | -19.61% |     0.47 |       72 | 45.42%     | ok               |
|          40 | 16.83%   | 18.10%             | -23.87% |     0.41 |       48 | 40.43%     | ok               |
|          25 | 7.03%    | 18.10%             | -27.86% |     0.24 |       72 | 53.08%     | ok               |
|          30 | 0.10%    | 18.10%             | -26.77% |     0.13 |       71 | 49.42%     | ok               |

## BAC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -5.65%   | 53.47%             | -19.19% |    -0.05 |       80 | 52.75%     | ok               |
|          25 | -8.33%   | 53.47%             | -23.37% |    -0.14 |       78 | 50.75%     | ok               |
|          15 | -10.16%  | 53.47%             | -21.05% |    -0.16 |       80 | 58.24%     | ok               |
|          45 | -8.23%   | 53.47%             | -20.78% |    -0.2  |       60 | 36.61%     | ok               |
|          35 | -9.24%   | 53.47%             | -28.15% |    -0.2  |       68 | 44.26%     | ok               |

## BCH-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 83.70%   | -23.42%            | -45.51% |     0.84 |       71 | 58.43%     | ok               |
|          20 | 51.89%   | -23.42%            | -45.82% |     0.65 |       67 | 54.98%     | ok               |
|          25 | 29.77%   | -23.42%            | -51.09% |     0.5  |       68 | 51.53%     | ok               |
|          30 | 23.02%   | -23.42%            | -53.87% |     0.44 |       78 | 49.04%     | ok               |
|          35 | 0.42%    | -23.42%            | -57.99% |     0.22 |       72 | 44.64%     | ok               |

## BITO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 0.07%    | -63.57%            | -31.98% |     0.14 |       54 | 23.96%     | ok               |
|          30 | -14.59%  | -63.57%            | -39.47% |    -0.03 |       76 | 39.93%     | ok               |
|          45 | -13.72%  | -63.57%            | -34.01% |    -0.07 |       60 | 27.45%     | ok               |
|          15 | -22.39%  | -63.57%            | -48.38% |    -0.08 |       87 | 49.08%     | ok               |
|          35 | -18.76%  | -63.57%            | -41.51% |    -0.1  |       68 | 35.77%     | ok               |

## BLK Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -3.41%   | 39.11%             | -21.48% |    -0.01 |       86 | 53.41%     | ok               |
|          35 | -2.97%   | 39.11%             | -20.79% |    -0.01 |       90 | 45.09%     | ok               |
|          40 | -3.80%   | 39.11%             | -22.83% |    -0.04 |       80 | 40.43%     | ok               |
|          25 | -4.79%   | 39.11%             | -24.62% |    -0.05 |       79 | 51.25%     | ok               |
|          30 | -9.21%   | 39.11%             | -26.90% |    -0.18 |       83 | 48.75%     | ok               |

## BND Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -7.33%   | 1.28%              | -9.66%  |    -1.06 |       67 | 39.93%     | ok               |
|          25 | -7.97%   | 1.28%              | -10.73% |    -1.2  |       69 | 37.94%     | ok               |
|          30 | -8.40%   | 1.28%              | -10.37% |    -1.34 |       71 | 34.44%     | ok               |
|          15 | -9.57%   | 1.28%              | -11.52% |    -1.37 |       79 | 42.76%     | ok               |
|          40 | -8.56%   | 1.28%              | -10.43% |    -1.56 |       66 | 27.45%     | ok               |

## BONK-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 148.90%  | -76.11%            | -35.57% |     1.17 |       44 | 21.65%     | ok               |
|          15 | 84.86%   | -76.11%            | -63.45% |     0.76 |       68 | 59.96%     | ok               |
|          25 | 75.56%   | -76.11%            | -47.99% |     0.73 |       71 | 51.15%     | ok               |
|          20 | 74.15%   | -76.11%            | -55.19% |     0.73 |       66 | 55.75%     | ok               |
|          45 | 59.87%   | -76.11%            | -42.36% |     0.7  |       62 | 27.20%     | ok               |

## BTC-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 65.88%   | -7.69%             | -12.20% |     1.17 |       38 | 32.18%     | ok               |
|          35 | 64.02%   | -7.69%             | -21.56% |     1.09 |       60 | 41.95%     | ok               |
|          40 | 60.40%   | -7.69%             | -14.50% |     1.08 |       42 | 36.02%     | ok               |
|          50 | 31.38%   | -7.69%             | -19.38% |     0.73 |       38 | 26.63%     | ok               |
|          30 | 35.58%   | -7.69%             | -21.75% |     0.68 |       66 | 47.89%     | ok               |

## C Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -10.42%  | 114.76%            | -21.80% |    -0.23 |       66 | 33.11%     | ok               |
|          45 | -18.66%  | 114.76%            | -27.40% |    -0.45 |       72 | 37.10%     | ok               |
|          40 | -24.41%  | 114.76%            | -33.13% |    -0.58 |       74 | 39.43%     | ok               |
|          25 | -32.20%  | 114.76%            | -38.39% |    -0.66 |       67 | 49.92%     | ok               |
|          15 | -34.46%  | 114.76%            | -38.73% |    -0.67 |       70 | 56.74%     | ok               |

## CAT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | 18.58%   | 136.26%            | -18.67% |     0.41 |       64 | 52.08%     | ok               |
|          15 | 14.74%   | 136.26%            | -20.14% |     0.35 |       74 | 62.90%     | ok               |
|          20 | 13.14%   | 136.26%            | -18.91% |     0.33 |       76 | 55.74%     | ok               |
|          30 | 10.17%   | 136.26%            | -18.88% |     0.29 |       70 | 49.58%     | ok               |
|          45 | 2.71%    | 136.26%            | -26.22% |     0.16 |       56 | 38.27%     | ok               |

## CL Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 4.27%    | -1.75%             | -14.32% |     0.2  |       60 | 40.77%     | ok               |
|          50 | 3.26%    | -1.75%             | -13.51% |     0.18 |       42 | 25.46%     | ok               |
|          45 | 0.22%    | -1.75%             | -13.51% |     0.06 |       46 | 27.95%     | ok               |
|          35 | -0.41%   | -1.75%             | -13.83% |     0.05 |       62 | 37.27%     | ok               |
|          40 | -3.30%   | -1.75%             | -12.70% |    -0.07 |       56 | 31.95%     | ok               |

## CMCSA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -42.55%  | -35.45%            | -48.00% |    -0.97 |       91 | 56.91%     | ok               |
|          50 | -27.38%  | -35.45%            | -30.41% |    -1.02 |       50 | 13.81%     | ok               |
|          30 | -42.19%  | -35.45%            | -47.67% |    -1.09 |       82 | 42.10%     | ok               |
|          40 | -39.11%  | -35.45%            | -44.10% |    -1.16 |       93 | 26.96%     | ok               |
|          35 | -42.00%  | -35.45%            | -47.50% |    -1.17 |       93 | 36.77%     | ok               |

## COMP-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -5.51%   | -49.89%            | -38.71% |     0.13 |       44 | 21.65%     | ok               |
|          30 | -46.68%  | -49.89%            | -56.58% |    -0.37 |       97 | 47.89%     | ok               |
|          25 | -51.95%  | -49.89%            | -55.45% |    -0.45 |       96 | 55.75%     | ok               |
|          40 | -47.85%  | -49.89%            | -53.14% |    -0.49 |       70 | 35.25%     | ok               |
|          45 | -47.75%  | -49.89%            | -55.45% |    -0.52 |       62 | 29.69%     | ok               |

## COP Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -7.05%   | 2.37%              | -34.21% |    -0.06 |       48 | 29.62%     | ok               |
|          45 | -13.07%  | 2.37%              | -39.38% |    -0.19 |       58 | 33.94%     | ok               |
|          35 | -16.08%  | 2.37%              | -43.58% |    -0.22 |       69 | 41.10%     | ok               |
|          30 | -19.17%  | 2.37%              | -43.40% |    -0.29 |       70 | 44.43%     | ok               |
|          40 | -20.19%  | 2.37%              | -46.34% |    -0.36 |       66 | 37.27%     | ok               |

## COST Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 14.09%   | 23.84%             | -24.32% |     0.47 |       64 | 47.59%     | ok               |
|          25 | 11.06%   | 23.84%             | -24.73% |     0.39 |       63 | 44.76%     | ok               |
|          35 | 7.41%    | 23.84%             | -27.43% |     0.31 |       58 | 39.10%     | ok               |
|          30 | 2.10%    | 23.84%             | -29.73% |     0.13 |       62 | 41.76%     | ok               |
|          15 | -0.81%   | 23.84%             | -27.30% |     0.05 |       67 | 51.08%     | ok               |

## CRM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | -22.97%  | -11.09%            | -34.84% |    -0.28 |       64 | 41.43%     | ok               |
|          15 | -28.95%  | -11.09%            | -47.54% |    -0.31 |       90 | 58.24%     | ok               |
|          40 | -26.71%  | -11.09%            | -40.30% |    -0.39 |       70 | 37.27%     | ok               |
|          50 | -21.91%  | -11.09%            | -38.24% |    -0.4  |       56 | 24.79%     | ok               |
|          30 | -30.48%  | -11.09%            | -45.51% |    -0.42 |       67 | 46.42%     | ok               |

## CRV-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 76.24%   | -41.78%            | -37.78% |     0.79 |       68 | 36.78%     | ok               |
|          40 | 46.02%   | -41.78%            | -38.86% |     0.61 |       58 | 32.38%     | ok               |
|          30 | 37.75%   | -41.78%            | -39.89% |     0.55 |       68 | 41.57%     | ok               |
|          45 | 35.94%   | -41.78%            | -42.29% |     0.55 |       58 | 25.29%     | ok               |
|          50 | 35.01%   | -41.78%            | -30.73% |     0.54 |       50 | 21.26%     | ok               |

## CSCO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 32.21%   | 129.19%            | -19.34% |     0.69 |       48 | 36.77%     | ok               |
|          45 | 27.73%   | 129.19%            | -19.34% |     0.6  |       49 | 38.44%     | ok               |
|          25 | 22.29%   | 129.19%            | -23.28% |     0.49 |       57 | 49.08%     | ok               |
|          35 | 20.52%   | 129.19%            | -23.68% |     0.46 |       53 | 45.42%     | ok               |
|          30 | 18.08%   | 129.19%            | -21.79% |     0.42 |       59 | 47.92%     | ok               |

## CVX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -5.18%   | 28.01%             | -23.80% |    -0.05 |       73 | 44.26%     | ok               |
|          40 | -6.03%   | 28.01%             | -27.34% |    -0.1  |       75 | 36.61%     | ok               |
|          45 | -6.44%   | 28.01%             | -28.83% |    -0.12 |       67 | 33.28%     | ok               |
|          35 | -9.09%   | 28.01%             | -28.85% |    -0.18 |       69 | 38.60%     | ok               |
|          20 | -10.00%  | 28.01%             | -26.37% |    -0.18 |       75 | 45.59%     | ok               |

## DASH-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 234.66%  | 198.00%            | -21.17% |     1.22 |       36 | 16.86%     | ok               |
|          40 | 154.49%  | 198.00%            | -25.22% |     0.99 |       42 | 22.61%     | ok               |
|          45 | 148.24%  | 198.00%            | -26.87% |     0.98 |       38 | 18.77%     | ok               |
|          35 | -3.66%   | 198.00%            | -63.41% |     0.35 |       65 | 27.01%     | ok               |
|          30 | -5.35%   | 198.00%            | -64.43% |     0.34 |       57 | 29.31%     | ok               |

## DBC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -0.35%   | 39.81%             | -27.03% |     0.06 |       79 | 39.60%     | ok               |
|          25 | -2.69%   | 39.81%             | -25.40% |    -0.02 |       64 | 36.44%     | ok               |
|          50 | -3.68%   | 39.81%             | -19.91% |    -0.09 |       48 | 24.46%     | ok               |
|          35 | -4.37%   | 39.81%             | -23.19% |    -0.09 |       64 | 33.28%     | ok               |
|          20 | -4.73%   | 39.81%             | -26.67% |    -0.09 |       71 | 37.94%     | ok               |

## DE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 4.15%    | 73.99%             | -17.97% |     0.19 |       58 | 29.62%     | ok               |
|          45 | -2.38%   | 73.99%             | -19.56% |     0.03 |       62 | 34.28%     | ok               |
|          20 | -5.57%   | 73.99%             | -24.13% |    -0.02 |       69 | 49.42%     | ok               |
|          25 | -8.81%   | 73.99%             | -24.31% |    -0.09 |       75 | 47.42%     | ok               |
|          30 | -9.86%   | 73.99%             | -22.93% |    -0.12 |       74 | 44.59%     | ok               |

## DIA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -1.59%   | 36.08%             | -11.28% |    -0.04 |       58 | 46.59%     | ok               |
|          35 | -3.49%   | 36.08%             | -13.15% |    -0.16 |       66 | 42.26%     | ok               |
|          20 | -4.30%   | 36.08%             | -13.60% |    -0.18 |       62 | 48.75%     | ok               |
|          30 | -4.94%   | 36.08%             | -12.94% |    -0.23 |       64 | 45.26%     | ok               |
|          40 | -6.68%   | 36.08%             | -15.06% |    -0.36 |       70 | 39.27%     | ok               |

## DIS Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 24.34%   | -6.58%             | -10.17% |     0.74 |       44 | 25.12%     | ok               |
|          40 | -4.77%   | -6.58%             | -18.75% |    -0.02 |       63 | 34.11%     | ok               |
|          45 | -4.62%   | -6.58%             | -16.54% |    -0.03 |       49 | 28.95%     | ok               |
|          15 | -11.99%  | -6.58%             | -31.15% |    -0.13 |       89 | 55.57%     | ok               |
|          35 | -12.84%  | -6.58%             | -25.70% |    -0.2  |       77 | 40.43%     | ok               |

## DOGE-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -5.00%   | -45.22%            | -57.89% |     0.23 |       77 | 63.98%     | ok               |
|          20 | -7.39%   | -45.22%            | -55.83% |     0.2  |       78 | 58.81%     | ok               |
|          25 | -15.40%  | -45.22%            | -53.72% |     0.11 |       70 | 54.79%     | ok               |
|          30 | -31.40%  | -45.22%            | -60.95% |    -0.11 |       71 | 48.66%     | ok               |
|          50 | -35.32%  | -45.22%            | -56.78% |    -0.33 |       58 | 23.75%     | ok               |

## DOT-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -65.31%  | -68.12%            | -72.06% |    -0.58 |       85 | 63.79%     | ok               |
|          20 | -61.71%  | -68.12%            | -67.71% |    -0.58 |       95 | 59.96%     | ok               |
|          45 | -46.66%  | -68.12%            | -53.23% |    -0.63 |       54 | 29.89%     | ok               |
|          50 | -44.66%  | -68.12%            | -48.78% |    -0.65 |       60 | 24.33%     | ok               |
|          30 | -62.13%  | -68.12%            | -65.79% |    -0.67 |       94 | 48.08%     | ok               |

## DXY-INDEX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -3.46%   | -6.08%             | -6.02%  |    -0.54 |       42 | 30.30%     | ok               |
|          40 | -4.43%   | -6.08%             | -7.30%  |    -0.57 |       68 | 46.54%     | ok               |
|          45 | -4.78%   | -6.08%             | -8.14%  |    -0.67 |       62 | 36.36%     | ok               |
|          15 | -8.55%   | -6.08%             | -11.61% |    -0.83 |       93 | 72.94%     | ok               |
|          30 | -7.60%   | -6.08%             | -9.83%  |    -0.91 |       78 | 56.93%     | ok               |

## EEM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -5.41%   | 64.40%             | -15.88% |    -0.14 |       54 | 34.11%     | ok               |
|          45 | -5.76%   | 64.40%             | -17.03% |    -0.15 |       52 | 35.61%     | ok               |
|          40 | -6.10%   | 64.40%             | -19.20% |    -0.15 |       64 | 37.77%     | ok               |
|          35 | -6.76%   | 64.40%             | -23.57% |    -0.16 |       66 | 39.77%     | ok               |
|          30 | -10.07%  | 64.40%             | -25.38% |    -0.27 |       62 | 41.60%     | ok               |

## EFA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -4.29%   | 37.11%             | -10.10% |    -0.1  |       62 | 50.42%     | ok               |
|          20 | -11.80%  | 37.11%             | -12.85% |    -0.43 |       71 | 47.42%     | ok               |
|          30 | -11.52%  | 37.11%             | -14.58% |    -0.45 |       62 | 42.43%     | ok               |
|          25 | -13.65%  | 37.11%             | -15.82% |    -0.53 |       66 | 44.59%     | ok               |
|          50 | -11.70%  | 37.11%             | -17.36% |    -0.55 |       56 | 33.28%     | ok               |

## EOG Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -22.05%  | 7.47%              | -38.89% |    -0.5  |       54 | 30.78%     | ok               |
|          50 | -24.51%  | 7.47%              | -37.65% |    -0.6  |       50 | 28.12%     | ok               |
|          40 | -27.95%  | 7.47%              | -40.83% |    -0.67 |       70 | 34.78%     | ok               |
|          30 | -31.44%  | 7.47%              | -48.55% |    -0.69 |       81 | 45.26%     | ok               |
|          35 | -32.10%  | 7.47%              | -44.69% |    -0.77 |       85 | 39.93%     | ok               |

## ETC-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -3.34%   | -47.57%            | -27.89% |     0.06 |       24 | 15.33%     | ok               |
|          45 | -5.35%   | -47.57%            | -35.44% |     0.04 |       24 | 17.24%     | ok               |
|          40 | -15.45%  | -47.57%            | -40.48% |    -0.14 |       34 | 20.11%     | ok               |
|          35 | -20.63%  | -47.57%            | -42.62% |    -0.22 |       44 | 23.95%     | ok               |
|          30 | -30.18%  | -47.57%            | -45.54% |    -0.39 |       60 | 27.78%     | ok               |

## ETH-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 156.11%  | 55.45%             | -30.11% |     1.35 |       60 | 45.79%     | ok               |
|          30 | 123.85%  | 55.45%             | -32.89% |     1.14 |       64 | 53.26%     | ok               |
|          25 | 84.94%   | 55.45%             | -40.90% |     0.91 |       62 | 57.66%     | ok               |
|          40 | 58.24%   | 55.45%             | -33.11% |     0.8  |       60 | 37.93%     | ok               |
|          20 | 68.76%   | 55.45%             | -39.10% |     0.8  |       82 | 61.69%     | ok               |

## EWJ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -24.14%  | 47.10%             | -30.00% |    -0.82 |       58 | 39.27%     | ok               |
|          30 | -23.51%  | 47.10%             | -29.40% |    -0.82 |       64 | 37.10%     | ok               |
|          25 | -26.33%  | 47.10%             | -29.85% |    -0.92 |       58 | 38.27%     | ok               |
|          15 | -28.45%  | 47.10%             | -31.15% |    -0.93 |       71 | 42.76%     | ok               |
|          45 | -23.42%  | 47.10%             | -26.67% |    -0.94 |       62 | 29.28%     | ok               |

## FCX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -0.95%   | 43.42%             | -32.44% |     0.13 |       56 | 32.45%     | ok               |
|          50 | -3.32%   | 43.42%             | -26.57% |     0.08 |       56 | 28.45%     | ok               |
|          40 | -14.59%  | 43.42%             | -42.89% |    -0.09 |       66 | 37.60%     | ok               |
|          30 | -28.39%  | 43.42%             | -46.84% |    -0.3  |       65 | 44.59%     | ok               |
|          35 | -32.81%  | 43.42%             | -50.12% |    -0.41 |       71 | 42.76%     | ok               |

## FET-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -16.07%  | -60.62%            | -64.89% |     0.13 |       90 | 51.53%     | ok               |
|          15 | -25.05%  | -60.62%            | -59.58% |     0.06 |       84 | 56.32%     | ok               |
|          25 | -24.58%  | -60.62%            | -65.31% |     0.02 |       83 | 44.64%     | ok               |
|          30 | -27.47%  | -60.62%            | -60.12% |    -0.04 |       75 | 39.66%     | ok               |
|          50 | -33.37%  | -60.62%            | -40.07% |    -0.53 |       40 | 11.49%     | ok               |

## FIL-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -52.37%  | -64.21%            | -57.27% |    -0.85 |       46 | 21.84%     | ok               |
|          50 | -46.25%  | -64.21%            | -46.77% |    -0.86 |       34 | 12.07%     | ok               |
|          30 | -60.58%  | -64.21%            | -62.21% |    -0.93 |       69 | 32.57%     | ok               |
|          15 | -70.87%  | -64.21%            | -72.08% |    -1    |       94 | 45.79%     | ok               |
|          35 | -64.20%  | -64.21%            | -65.68% |    -1.15 |       60 | 26.05%     | ok               |

## FXI Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -5.14%   | 34.39%             | -22.99% |    -0.04 |       50 | 33.78%     | ok               |
|          30 | -5.41%   | 34.39%             | -24.33% |    -0.05 |       48 | 32.28%     | ok               |
|          15 | -7.71%   | 34.39%             | -21.68% |    -0.09 |       52 | 37.60%     | ok               |
|          20 | -8.76%   | 34.39%             | -24.94% |    -0.13 |       52 | 35.61%     | ok               |
|          35 | -9.06%   | 34.39%             | -27.93% |    -0.15 |       50 | 29.78%     | ok               |

## GDX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 3.52%    | 179.41%            | -35.59% |     0.2  |       74 | 49.25%     | ok               |
|          40 | 1.36%    | 179.41%            | -31.37% |     0.15 |       62 | 38.94%     | ok               |
|          30 | -1.14%   | 179.41%            | -34.99% |     0.12 |       60 | 44.93%     | ok               |
|          35 | -4.90%   | 179.41%            | -31.88% |     0.05 |       70 | 41.76%     | ok               |
|          25 | -6.38%   | 179.41%            | -38.90% |     0.04 |       64 | 46.09%     | ok               |

## GDXJ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -25.27%  | 194.43%            | -44.73% |    -0.21 |       70 | 48.92%     | ok               |
|          50 | -28.16%  | 194.43%            | -46.83% |    -0.38 |       58 | 34.61%     | ok               |
|          30 | -35.32%  | 194.43%            | -44.61% |    -0.45 |       68 | 42.93%     | ok               |
|          35 | -37.00%  | 194.43%            | -41.76% |    -0.5  |       70 | 40.43%     | ok               |
|          25 | -39.64%  | 194.43%            | -46.95% |    -0.51 |       73 | 45.76%     | ok               |

## GE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -1.53%   | 94.39%             | -22.16% |     0.07 |       66 | 34.61%     | ok               |
|          20 | -11.74%  | 94.39%             | -25.05% |    -0.1  |       77 | 51.91%     | ok               |
|          45 | -9.46%   | 94.39%             | -25.56% |    -0.1  |       76 | 37.27%     | ok               |
|          30 | -14.76%  | 94.39%             | -27.82% |    -0.17 |       80 | 47.75%     | ok               |
|          35 | -15.37%  | 94.39%             | -27.11% |    -0.2  |       82 | 42.60%     | ok               |

## GLD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | 13.86%   | 84.49%             | -13.87% |     0.4  |       52 | 46.09%     | ok               |
|          20 | 11.89%   | 84.49%             | -13.87% |     0.36 |       55 | 47.92%     | ok               |
|          30 | 8.43%    | 84.49%             | -14.86% |     0.28 |       54 | 44.93%     | ok               |
|          35 | 5.56%    | 84.49%             | -15.53% |     0.22 |       56 | 42.60%     | ok               |
|          15 | 5.04%    | 84.49%             | -17.54% |     0.2  |       57 | 52.08%     | ok               |

## GOOGL Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 68.16%   | 122.65%            | -18.25% |     1.12 |       57 | 43.93%     | ok               |
|          30 | 64.10%   | 122.65%            | -20.41% |     1.05 |       55 | 47.42%     | ok               |
|          45 | 56.20%   | 122.65%            | -14.13% |     1.03 |       50 | 37.44%     | ok               |
|          25 | 61.60%   | 122.65%            | -19.76% |     1.01 |       55 | 49.92%     | ok               |
|          50 | 49.51%   | 122.65%            | -14.89% |     0.97 |       46 | 32.61%     | ok               |

## GRT-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 24.13%   | -75.25%            | -25.60% |     0.51 |       38 | 17.62%     | ok               |
|          15 | 6.16%    | -75.25%            | -45.50% |     0.31 |       76 | 61.11%     | ok               |
|          20 | -2.68%   | -75.25%            | -42.04% |     0.21 |       83 | 55.36%     | ok               |
|          25 | -15.91%  | -75.25%            | -51.18% |     0.05 |       84 | 50.77%     | ok               |
|          45 | -10.41%  | -75.25%            | -47.52% |    -0.01 |       42 | 23.56%     | ok               |

## GS Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 22.06%   | 126.51%            | -20.56% |     0.49 |       66 | 55.57%     | ok               |
|          20 | 3.31%    | 126.51%            | -23.19% |     0.17 |       66 | 52.25%     | ok               |
|          40 | 3.29%    | 126.51%            | -17.88% |     0.16 |       64 | 41.76%     | ok               |
|          25 | -1.92%   | 126.51%            | -23.32% |     0.06 |       66 | 49.75%     | ok               |
|          30 | -3.01%   | 126.51%            | -22.13% |     0.03 |       66 | 47.42%     | ok               |

## HD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -6.69%   | -8.88%             | -19.21% |    -0.1  |       72 | 44.43%     | ok               |
|          30 | -6.70%   | -8.88%             | -18.84% |    -0.1  |       75 | 42.26%     | ok               |
|          45 | -6.68%   | -8.88%             | -16.42% |    -0.16 |       52 | 28.29%     | ok               |
|          40 | -8.85%   | -8.88%             | -17.28% |    -0.21 |       80 | 33.28%     | ok               |
|          35 | -10.49%  | -8.88%             | -20.61% |    -0.23 |       78 | 38.44%     | ok               |

## HON Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -11.33%  | 8.23%              | -23.16% |    -0.28 |       72 | 35.11%     | ok               |
|          45 | -14.25%  | 8.23%              | -25.06% |    -0.35 |       72 | 40.93%     | ok               |
|          30 | -23.52%  | 8.23%              | -33.57% |    -0.56 |       90 | 55.91%     | ok               |
|          35 | -23.15%  | 8.23%              | -31.82% |    -0.57 |       86 | 51.58%     | ok               |
|          40 | -24.57%  | 8.23%              | -33.77% |    -0.64 |       76 | 45.26%     | ok               |

## HYG Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -7.19%   | 3.06%              | -7.76%  |    -0.85 |       70 | 31.28%     | ok               |
|          15 | -9.51%   | 3.06%              | -11.09% |    -1.02 |       94 | 44.43%     | ok               |
|          35 | -8.69%   | 3.06%              | -9.66%  |    -1.03 |       79 | 33.11%     | ok               |
|          45 | -8.34%   | 3.06%              | -8.86%  |    -1.03 |       70 | 27.95%     | ok               |
|          30 | -9.06%   | 3.06%              | -10.59% |    -1.04 |       87 | 36.27%     | ok               |

## IBIT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 51.64%   | 13.92%             | -17.37% |     0.96 |       24 | 23.63%     | ok               |
|          15 | 54.52%   | 13.92%             | -19.20% |     0.87 |       42 | 39.66%     | ok               |
|          45 | 42.31%   | 13.92%             | -17.37% |     0.81 |       28 | 24.89%     | ok               |
|          40 | 35.94%   | 13.92%             | -17.78% |     0.72 |       28 | 26.79%     | ok               |
|          30 | 28.83%   | 13.92%             | -18.95% |     0.6  |       36 | 32.70%     | ok               |

## IBM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -20.22%  | 40.76%             | -49.43% |    -0.16 |       91 | 63.06%     | ok               |
|          35 | -24.24%  | 40.76%             | -47.10% |    -0.29 |       69 | 46.59%     | ok               |
|          30 | -25.87%  | 40.76%             | -48.94% |    -0.31 |       73 | 50.75%     | ok               |
|          20 | -30.94%  | 40.76%             | -53.45% |    -0.38 |       73 | 55.41%     | ok               |
|          50 | -29.24%  | 40.76%             | -45.88% |    -0.44 |       46 | 34.44%     | ok               |

## ICP-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -7.44%   | -41.53%            | -47.52% |     0.18 |       77 | 36.02%     | ok               |
|          35 | -11.07%  | -41.53%            | -47.24% |     0.08 |       68 | 30.08%     | ok               |
|          40 | -10.85%  | -41.53%            | -40.71% |     0.06 |       60 | 25.67%     | ok               |
|          15 | -35.83%  | -41.53%            | -58.26% |    -0.04 |       75 | 48.66%     | ok               |
|          20 | -38.09%  | -41.53%            | -61.47% |    -0.09 |       84 | 45.79%     | ok               |

## IEF Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -8.29%   | 0.01%              | -10.32% |    -1.01 |       74 | 41.76%     | ok               |
|          15 | -8.83%   | 0.01%              | -11.04% |    -1.06 |       73 | 43.26%     | ok               |
|          50 | -8.19%   | 0.01%              | -9.11%  |    -1.45 |       56 | 20.47%     | ok               |
|          25 | -11.82%  | 0.01%              | -12.20% |    -1.54 |       80 | 38.94%     | ok               |
|          40 | -10.00%  | 0.01%              | -11.37% |    -1.54 |       64 | 25.12%     | ok               |

## IEMG Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -1.30%   | 59.06%             | -14.22% |     0.01 |       54 | 32.78%     | ok               |
|          45 | -2.11%   | 59.06%             | -15.23% |    -0.02 |       50 | 35.27%     | ok               |
|          40 | -3.62%   | 59.06%             | -18.73% |    -0.08 |       62 | 38.27%     | ok               |
|          35 | -6.11%   | 59.06%             | -24.91% |    -0.15 |       67 | 40.77%     | ok               |
|          30 | -11.00%  | 59.06%             | -29.45% |    -0.32 |       62 | 41.76%     | ok               |

## INJ-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | -15.12%  | -24.13%            | -54.35% |     0.06 |       58 | 33.33%     | ok               |
|          40 | -17.56%  | -24.13%            | -49.75% |     0    |       48 | 30.27%     | ok               |
|          45 | -20.18%  | -24.13%            | -47.58% |    -0.07 |       52 | 24.71%     | ok               |
|          15 | -52.88%  | -24.13%            | -80.00% |    -0.35 |       82 | 49.43%     | ok               |
|          20 | -51.72%  | -24.13%            | -77.07% |    -0.37 |       80 | 46.17%     | ok               |

## INTC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 73.82%   | 209.88%            | -49.32% |     0.73 |       58 | 33.11%     | ok               |
|          40 | 74.59%   | 209.88%            | -55.86% |     0.72 |       66 | 37.44%     | ok               |
|          15 | 79.11%   | 209.88%            | -53.65% |     0.72 |       80 | 59.90%     | ok               |
|          50 | 63.68%   | 209.88%            | -48.35% |     0.68 |       64 | 29.12%     | ok               |
|          25 | 61.17%   | 209.88%            | -56.41% |     0.64 |       79 | 50.75%     | ok               |

## INTU Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 6.40%    | -50.01%            | -36.76% |     0.23 |       65 | 26.62%     | ok               |
|          45 | -0.34%   | -50.01%            | -40.64% |     0.11 |       65 | 30.95%     | ok               |
|          40 | -6.98%   | -50.01%            | -44.15% |    -0.01 |       67 | 34.78%     | ok               |
|          25 | -10.28%  | -50.01%            | -39.21% |    -0.03 |       68 | 47.25%     | ok               |
|          15 | -13.56%  | -50.01%            | -43.23% |    -0.08 |       79 | 52.91%     | ok               |

## ITA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 3.46%    | 65.79%             | -21.48% |     0.17 |       72 | 38.77%     | ok               |
|          15 | -0.48%   | 65.79%             | -28.06% |     0.08 |       83 | 60.90%     | ok               |
|          30 | -0.78%   | 65.79%             | -23.75% |     0.06 |       72 | 48.92%     | ok               |
|          35 | -2.85%   | 65.79%             | -23.16% |    -0.01 |       74 | 46.59%     | ok               |
|          40 | -3.04%   | 65.79%             | -20.58% |    -0.02 |       74 | 43.26%     | ok               |

## IWM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 13.45%   | 45.27%             | -13.94% |     0.57 |       46 | 31.95%     | ok               |
|          25 | 12.85%   | 45.27%             | -12.34% |     0.5  |       54 | 37.27%     | ok               |
|          35 | 11.49%   | 45.27%             | -13.94% |     0.47 |       52 | 34.44%     | ok               |
|          30 | 11.41%   | 45.27%             | -12.65% |     0.46 |       54 | 36.44%     | ok               |
|          20 | 11.36%   | 45.27%             | -12.12% |     0.44 |       60 | 38.27%     | ok               |

## JNJ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 16.00%   | 84.05%             | -10.57% |     0.67 |       48 | 34.78%     | ok               |
|          15 | 7.52%    | 84.05%             | -18.02% |     0.3  |       64 | 54.24%     | ok               |
|          45 | 5.14%    | 84.05%             | -13.35% |     0.25 |       50 | 38.77%     | ok               |
|          20 | 2.56%    | 84.05%             | -17.61% |     0.15 |       70 | 50.75%     | ok               |
|          40 | 1.61%    | 84.05%             | -14.77% |     0.12 |       58 | 43.09%     | ok               |

## JPM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 6.98%    | 80.64%             | -15.90% |     0.29 |       52 | 35.27%     | ok               |
|          45 | -3.18%   | 80.64%             | -21.91% |    -0.03 |       54 | 38.27%     | ok               |
|          20 | -18.83%  | 80.64%             | -35.58% |    -0.38 |       82 | 51.91%     | ok               |
|          35 | -15.95%  | 80.64%             | -27.43% |    -0.42 |       74 | 44.59%     | ok               |
|          40 | -16.47%  | 80.64%             | -28.47% |    -0.44 |       66 | 40.93%     | ok               |

## KO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 25.74%   | 42.63%             | -8.64%  |     0.9  |       54 | 39.93%     | ok               |
|          35 | 21.47%   | 42.63%             | -8.21%  |     0.78 |       58 | 38.44%     | ok               |
|          40 | 18.54%   | 42.63%             | -9.28%  |     0.73 |       60 | 35.11%     | ok               |
|          25 | 19.44%   | 42.63%             | -10.16% |     0.7  |       60 | 42.76%     | ok               |
|          20 | 6.26%    | 42.63%             | -15.99% |     0.27 |       77 | 46.92%     | ok               |

## LDO-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 25.76%   | -44.74%            | -46.95% |     0.49 |       77 | 59.58%     | ok               |
|          20 | 20.10%   | -44.74%            | -47.34% |     0.45 |       81 | 54.79%     | ok               |
|          30 | -2.84%   | -44.74%            | -62.63% |     0.25 |       72 | 45.98%     | ok               |
|          25 | -6.82%   | -44.74%            | -58.49% |     0.24 |       81 | 51.72%     | ok               |
|          35 | -16.49%  | -44.74%            | -64.25% |     0.09 |       76 | 37.93%     | ok               |

## LIN Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -6.12%   | 3.30%              | -23.68% |    -0.15 |       72 | 46.26%     | ok               |
|          20 | -6.29%   | 3.30%              | -23.00% |    -0.16 |       66 | 42.10%     | ok               |
|          25 | -6.24%   | 3.30%              | -22.01% |    -0.16 |       69 | 39.27%     | ok               |
|          30 | -9.77%   | 3.30%              | -20.61% |    -0.3  |       72 | 36.61%     | ok               |
|          35 | -10.77%  | 3.30%              | -19.70% |    -0.37 |       70 | 29.78%     | ok               |

## LINK-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 38.81%   | -4.23%             | -33.64% |     0.57 |       72 | 45.40%     | ok               |
|          45 | 36.31%   | -4.23%             | -33.71% |     0.57 |       50 | 30.46%     | ok               |
|          35 | 18.87%   | -4.23%             | -34.21% |     0.41 |       60 | 40.04%     | ok               |
|          50 | 14.59%   | -4.23%             | -27.44% |     0.36 |       44 | 24.52%     | ok               |
|          40 | 12.41%   | -4.23%             | -34.00% |     0.34 |       54 | 34.29%     | ok               |

## LLY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 1.18%    | 58.99%             | -38.23% |     0.13 |       46 | 35.27%     | ok               |
|          15 | -9.74%   | 58.99%             | -48.12% |    -0.01 |       65 | 59.07%     | ok               |
|          45 | -10.49%  | 58.99%             | -42.66% |    -0.09 |       52 | 38.60%     | ok               |
|          20 | -22.11%  | 58.99%             | -51.34% |    -0.26 |       72 | 54.24%     | ok               |
|          25 | -23.39%  | 58.99%             | -53.47% |    -0.29 |       68 | 51.58%     | ok               |

## LRCX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -13.68%  | 198.75%            | -48.71% |    -0.02 |       76 | 33.61%     | ok               |
|          40 | -18.39%  | 198.75%            | -55.33% |    -0.06 |       72 | 39.60%     | ok               |
|          35 | -19.96%  | 198.75%            | -58.47% |    -0.08 |       80 | 41.76%     | ok               |
|          15 | -27.52%  | 198.75%            | -56.69% |    -0.12 |       83 | 51.75%     | ok               |
|          30 | -25.21%  | 198.75%            | -61.08% |    -0.15 |       84 | 42.43%     | ok               |

## LTC-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | -3.28%   | -27.73%            | -34.94% |     0.13 |       70 | 43.87%     | ok               |
|          45 | -2.53%   | -27.73%            | -37.29% |     0.13 |       58 | 32.95%     | ok               |
|          30 | -10.15%  | -27.73%            | -33.94% |     0.05 |       72 | 51.53%     | ok               |
|          25 | -16.57%  | -27.73%            | -34.22% |    -0.03 |       76 | 54.21%     | ok               |
|          40 | -14.38%  | -27.73%            | -40.31% |    -0.05 |       58 | 38.31%     | ok               |

## MCD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 4.84%    | -9.84%             | -9.22%  |     0.27 |       44 | 22.80%     | ok               |
|          45 | -3.09%   | -9.84%             | -16.79% |    -0.1  |       52 | 26.46%     | ok               |
|          30 | -4.85%   | -9.84%             | -21.88% |    -0.14 |       77 | 37.77%     | ok               |
|          40 | -4.38%   | -9.84%             | -18.49% |    -0.15 |       67 | 29.78%     | ok               |
|          25 | -5.37%   | -9.84%             | -23.62% |    -0.16 |       75 | 40.10%     | ok               |

## META Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -15.65%  | 54.59%             | -37.10% |    -0.22 |       68 | 37.44%     | ok               |
|          40 | -21.11%  | 54.59%             | -40.49% |    -0.32 |       70 | 40.93%     | ok               |
|          50 | -24.71%  | 54.59%             | -38.63% |    -0.45 |       70 | 33.11%     | ok               |
|          25 | -32.22%  | 54.59%             | -45.35% |    -0.53 |       77 | 51.25%     | ok               |
|          35 | -31.01%  | 54.59%             | -40.80% |    -0.54 |       83 | 45.76%     | ok               |

## MPC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 46.34%   | 111.50%            | -18.24% |     0.83 |       48 | 39.43%     | ok               |
|          45 | 37.06%   | 111.50%            | -19.46% |     0.69 |       54 | 43.09%     | ok               |
|          40 | 31.88%   | 111.50%            | -20.11% |     0.62 |       56 | 45.26%     | ok               |
|          35 | 27.80%   | 111.50%            | -31.08% |     0.54 |       64 | 47.75%     | ok               |
|          30 | 12.58%   | 111.50%            | -37.91% |     0.32 |       67 | 50.25%     | ok               |

## MRK Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -13.49%  | 12.57%             | -28.87% |    -0.17 |       85 | 53.58%     | ok               |
|          25 | -14.23%  | 12.57%             | -31.07% |    -0.21 |       70 | 45.76%     | ok               |
|          20 | -18.43%  | 12.57%             | -29.34% |    -0.3  |       75 | 49.08%     | ok               |
|          50 | -15.53%  | 12.57%             | -24.92% |    -0.32 |       58 | 30.45%     | ok               |
|          45 | -17.63%  | 12.57%             | -25.38% |    -0.36 |       59 | 33.78%     | ok               |

## MS Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 0.44%    | 119.88%            | -19.99% |     0.09 |       68 | 38.94%     | ok               |
|          15 | -4.40%   | 119.88%            | -22.02% |     0    |       72 | 56.57%     | ok               |
|          20 | -5.87%   | 119.88%            | -25.68% |    -0.05 |       75 | 52.25%     | ok               |
|          30 | -10.75%  | 119.88%            | -27.79% |    -0.19 |       75 | 47.42%     | ok               |
|          35 | -10.68%  | 119.88%            | -26.58% |    -0.19 |       76 | 43.93%     | ok               |

## MSFT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -15.43%  | 24.74%             | -25.54% |    -0.36 |       70 | 36.27%     | ok               |
|          50 | -21.68%  | 24.74%             | -26.37% |    -0.58 |       64 | 30.95%     | ok               |
|          35 | -28.21%  | 24.74%             | -36.28% |    -0.67 |       73 | 45.42%     | ok               |
|          30 | -30.21%  | 24.74%             | -38.06% |    -0.7  |       81 | 49.58%     | ok               |
|          40 | -28.25%  | 24.74%             | -35.70% |    -0.7  |       71 | 40.10%     | ok               |

## MU Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 241.80%  | 776.05%            | -61.96% |     1.21 |       49 | 61.56%     | ok               |
|          40 | 198.76%  | 776.05%            | -64.30% |     1.2  |       54 | 49.08%     | ok               |
|          25 | 175.56%  | 776.05%            | -67.90% |     1.1  |       49 | 55.57%     | ok               |
|          30 | 164.65%  | 776.05%            | -68.76% |     1.08 |       49 | 53.91%     | ok               |
|          35 | 157.20%  | 776.05%            | -69.35% |     1.06 |       61 | 51.58%     | ok               |

## NEAR-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 130.84%  | 68.86%             | -43.08% |     1.08 |       40 | 26.25%     | ok               |
|          40 | 132.53%  | 68.86%             | -52.22% |     1.08 |       40 | 30.27%     | ok               |
|          50 | 98.31%   | 68.86%             | -48.72% |     0.95 |       32 | 21.26%     | ok               |
|          35 | 77.14%   | 68.86%             | -59.02% |     0.8  |       58 | 34.29%     | ok               |
|          30 | 48.74%   | 68.86%             | -60.10% |     0.62 |       73 | 42.34%     | ok               |

## NEM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 3.24%    | 186.55%            | -31.25% |     0.21 |       58 | 60.57%     | ok               |
|          20 | -0.11%   | 186.55%            | -30.50% |     0.16 |       64 | 56.24%     | ok               |
|          25 | -16.10%  | 186.55%            | -39.51% |    -0.07 |       62 | 54.41%     | ok               |
|          50 | -19.35%  | 186.55%            | -32.97% |    -0.17 |       54 | 40.93%     | ok               |
|          30 | -26.61%  | 186.55%            | -39.56% |    -0.26 |       66 | 52.75%     | ok               |

## NFLX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 41.22%   | 33.34%             | -13.37% |     0.91 |       48 | 42.43%     | ok               |
|          50 | 37.08%   | 33.34%             | -16.28% |     0.89 |       44 | 34.78%     | ok               |
|          35 | 41.25%   | 33.34%             | -18.30% |     0.86 |       70 | 46.92%     | ok               |
|          45 | 25.95%   | 33.34%             | -15.48% |     0.65 |       54 | 38.94%     | ok               |
|          15 | 17.50%   | 33.34%             | -26.59% |     0.41 |       71 | 65.39%     | ok               |

## NKE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | -16.79%  | -61.29%            | -42.13% |    -0.17 |       69 | 38.44%     | ok               |
|          20 | -21.34%  | -61.29%            | -49.34% |    -0.18 |       83 | 50.75%     | ok               |
|          25 | -24.60%  | -61.29%            | -51.20% |    -0.25 |       83 | 48.09%     | ok               |
|          15 | -26.42%  | -61.29%            | -54.28% |    -0.27 |       86 | 54.58%     | ok               |
|          40 | -18.46%  | -61.29%            | -31.79% |    -0.3  |       63 | 30.45%     | ok               |

## NOW Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 8.77%    | -3.34%             | -30.43% |     0.28 |       86 | 50.42%     | ok               |
|          20 | 7.34%    | -3.34%             | -39.71% |     0.26 |       81 | 56.91%     | ok               |
|          25 | 3.65%    | -3.34%             | -37.51% |     0.22 |       78 | 53.91%     | ok               |
|          15 | -0.50%   | -3.34%             | -43.06% |     0.18 |       89 | 59.90%     | ok               |
|          40 | 0.11%    | -3.34%             | -36.21% |     0.16 |       78 | 39.93%     | ok               |

## NVDA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -29.07%  | 85.71%             | -41.21% |    -0.37 |       76 | 45.63%     | ok               |
|          20 | -34.34%  | 85.71%             | -45.26% |    -0.39 |       76 | 53.83%     | ok               |
|          25 | -34.23%  | 85.71%             | -45.17% |    -0.43 |       77 | 48.84%     | ok               |
|          15 | -41.45%  | 85.71%             | -52.37% |    -0.5  |       77 | 57.04%     | ok               |
|          35 | -40.59%  | 85.71%             | -48.32% |    -0.66 |       86 | 42.60%     | ok               |

## OP-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 28.55%   | -82.29%            | -31.68% |     0.55 |       30 | 9.39%      | ok               |
|          45 | -8.63%   | -82.29%            | -51.43% |     0.05 |       34 | 14.18%     | ok               |
|          40 | -25.16%  | -82.29%            | -60.29% |    -0.15 |       46 | 21.84%     | ok               |
|          30 | -44.56%  | -82.29%            | -68.74% |    -0.39 |       70 | 32.76%     | ok               |
|          35 | -43.37%  | -82.29%            | -64.14% |    -0.45 |       56 | 26.82%     | ok               |

## ORCL Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 167.68%  | 31.07%             | -32.54% |     1.12 |       73 | 64.39%     | ok               |
|          45 | 102.05%  | 31.07%             | -32.35% |     0.93 |       60 | 41.10%     | ok               |
|          25 | 115.22%  | 31.07%             | -27.76% |     0.93 |       65 | 56.91%     | ok               |
|          20 | 109.22%  | 31.07%             | -29.32% |     0.9  |       74 | 60.07%     | ok               |
|          35 | 98.56%   | 31.07%             | -31.95% |     0.88 |       70 | 50.58%     | ok               |

## OXY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -3.27%   | -12.65%            | -29.80% |     0.07 |       71 | 42.76%     | ok               |
|          35 | -5.25%   | -12.65%            | -28.72% |     0.02 |       74 | 38.60%     | ok               |
|          50 | -6.31%   | -12.65%            | -27.98% |    -0.03 |       44 | 26.96%     | ok               |
|          40 | -11.09%  | -12.65%            | -30.46% |    -0.11 |       64 | 34.44%     | ok               |
|          25 | -16.66%  | -12.65%            | -39.52% |    -0.18 |       79 | 46.26%     | ok               |

## PEP Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 14.31%   | -24.35%            | -11.62% |     0.64 |       38 | 25.79%     | ok               |
|          45 | 7.01%    | -24.35%            | -14.22% |     0.34 |       54 | 29.78%     | ok               |
|          35 | 1.99%    | -24.35%            | -21.42% |     0.13 |       75 | 39.93%     | ok               |
|          40 | -0.20%   | -24.35%            | -18.04% |     0.05 |       68 | 35.27%     | ok               |
|          30 | -3.51%   | -24.35%            | -21.35% |    -0.04 |       76 | 45.92%     | ok               |

## PEPE-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -40.30%  | -47.87%            | -63.12% |    -0.05 |       82 | 63.03%     | ok               |
|          30 | -36.93%  | -47.87%            | -55.59% |    -0.12 |       89 | 47.89%     | ok               |
|          25 | -38.51%  | -47.87%            | -52.98% |    -0.13 |       93 | 53.83%     | ok               |
|          20 | -46.17%  | -47.87%            | -62.32% |    -0.19 |       88 | 59.58%     | ok               |
|          35 | -38.97%  | -47.87%            | -54.42% |    -0.22 |       72 | 41.76%     | ok               |

## PFE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -17.13%  | 9.42%              | -23.37% |    -0.54 |       54 | 22.13%     | ok               |
|          50 | -17.66%  | 9.42%              | -25.98% |    -0.62 |       42 | 18.80%     | ok               |
|          40 | -23.63%  | 9.42%              | -30.07% |    -0.73 |       74 | 27.29%     | ok               |
|          35 | -29.82%  | 9.42%              | -35.41% |    -0.91 |       88 | 34.61%     | ok               |
|          30 | -38.28%  | 9.42%              | -43.18% |    -1.16 |       83 | 39.27%     | ok               |

## PG Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -11.13%  | -9.23%             | -19.77% |    -0.44 |       54 | 30.12%     | ok               |
|          35 | -14.16%  | -9.23%             | -18.66% |    -0.55 |       62 | 33.61%     | ok               |
|          30 | -21.96%  | -9.23%             | -24.25% |    -0.87 |       64 | 36.77%     | ok               |
|          45 | -19.81%  | -9.23%             | -22.13% |    -0.9  |       54 | 27.62%     | ok               |
|          25 | -23.74%  | -9.23%             | -25.94% |    -0.94 |       76 | 38.27%     | ok               |

## PM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | -0.65%   | 98.23%             | -32.20% |     0.08 |       84 | 49.75%     | ok               |
|          20 | -3.24%   | 98.23%             | -33.51% |     0.03 |       83 | 58.40%     | ok               |
|          30 | -3.76%   | 98.23%             | -35.15% |     0.01 |       79 | 53.24%     | ok               |
|          40 | -8.23%   | 98.23%             | -37.94% |    -0.12 |       78 | 45.76%     | ok               |
|          50 | -7.75%   | 98.23%             | -35.70% |    -0.12 |       68 | 39.93%     | ok               |

## POL-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 19.85%   | -43.93%            | -45.67% |     0.42 |       87 | 49.23%     | ok               |
|          25 | 11.52%   | -43.93%            | -46.72% |     0.34 |       74 | 55.94%     | ok               |
|          20 | -4.83%   | -43.93%            | -52.88% |     0.19 |       82 | 60.15%     | ok               |
|          50 | 1.20%    | -43.93%            | -26.14% |     0.17 |       48 | 19.92%     | ok               |
|          40 | -7.76%   | -43.93%            | -40.36% |     0.08 |       54 | 30.08%     | ok               |

## QCOM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | 0.65%    | 15.56%             | -55.66% |     0.18 |       71 | 45.09%     | ok               |
|          35 | -6.93%   | 15.56%             | -51.84% |     0.07 |       77 | 40.77%     | ok               |
|          20 | -11.33%  | 15.56%             | -57.05% |     0.03 |       70 | 48.42%     | ok               |
|          30 | -16.91%  | 15.56%             | -57.69% |    -0.07 |       75 | 43.09%     | ok               |
|          15 | -22.04%  | 15.56%             | -60.40% |    -0.11 |       72 | 51.08%     | ok               |

## QQQ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 27.72%   | 68.91%             | -14.17% |     0.67 |       65 | 54.58%     | ok               |
|          25 | 19.05%   | 68.91%             | -12.88% |     0.53 |       63 | 48.59%     | ok               |
|          20 | 17.83%   | 68.91%             | -12.98% |     0.49 |       71 | 51.25%     | ok               |
|          30 | 13.22%   | 68.91%             | -14.20% |     0.41 |       66 | 46.42%     | ok               |
|          35 | 1.58%    | 68.91%             | -20.59% |     0.12 |       72 | 42.60%     | ok               |

## RENDER-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 20.46%   | -59.73%            | -44.59% |     0.45 |       86 | 61.11%     | ok               |
|          20 | 19.57%   | -59.73%            | -43.43% |     0.44 |       91 | 57.47%     | ok               |
|          25 | 6.03%    | -59.73%            | -40.60% |     0.33 |       91 | 52.49%     | ok               |
|          35 | -34.06%  | -59.73%            | -45.72% |    -0.18 |       80 | 37.93%     | ok               |
|          30 | -40.65%  | -59.73%            | -46.98% |    -0.21 |      100 | 45.59%     | ok               |

## RTX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 43.62%   | 90.29%             | -18.66% |     0.9  |       74 | 57.24%     | ok               |
|          25 | 38.71%   | 90.29%             | -18.59% |     0.83 |       62 | 54.58%     | ok               |
|          30 | 35.11%   | 90.29%             | -16.99% |     0.78 |       60 | 52.75%     | ok               |
|          15 | 35.78%   | 90.29%             | -19.55% |     0.76 |       69 | 62.06%     | ok               |
|          35 | 26.98%   | 90.29%             | -18.00% |     0.69 |       52 | 49.75%     | ok               |

## SBUX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -4.55%   | 10.05%             | -23.55% |     0    |       53 | 40.27%     | ok               |
|          40 | -10.70%  | 10.05%             | -25.43% |    -0.17 |       62 | 33.11%     | ok               |
|          45 | -10.66%  | 10.05%             | -27.26% |    -0.2  |       64 | 28.95%     | ok               |
|          30 | -15.40%  | 10.05%             | -29.22% |    -0.26 |       58 | 38.27%     | ok               |
|          20 | -18.28%  | 10.05%             | -30.94% |    -0.29 |       58 | 41.93%     | ok               |

## SCHW Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -1.02%   | 39.71%             | -16.53% |     0.04 |       62 | 33.28%     | ok               |
|          25 | -3.17%   | 39.71%             | -28.76% |     0.02 |       65 | 49.58%     | ok               |
|          20 | -6.65%   | 39.71%             | -29.24% |    -0.06 |       73 | 52.08%     | ok               |
|          50 | -6.67%   | 39.71%             | -13.28% |    -0.17 |       58 | 30.28%     | ok               |
|          40 | -10.34%  | 39.71%             | -23.35% |    -0.22 |       68 | 36.77%     | ok               |

## SHIB-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -35.51%  | -54.32%            | -40.35% |    -0.26 |       79 | 59.77%     | ok               |
|          15 | -38.58%  | -54.32%            | -45.04% |    -0.29 |       87 | 68.20%     | ok               |
|          20 | -40.71%  | -54.32%            | -43.97% |    -0.34 |       81 | 63.22%     | ok               |
|          35 | -36.69%  | -54.32%            | -46.07% |    -0.37 |       74 | 44.83%     | ok               |
|          50 | -32.35%  | -54.32%            | -40.54% |    -0.44 |       52 | 22.61%     | ok               |

## SHY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd    |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:-------|---------:|---------:|:-----------|:-----------------|
|          30 | -2.04%   | 0.21%              | -3.18% |    -0.7  |       48 | 35.11%     | ok               |
|          35 | -2.57%   | 0.21%              | -3.49% |    -0.9  |       52 | 33.44%     | ok               |
|          40 | -2.71%   | 0.21%              | -3.58% |    -0.96 |       54 | 31.95%     | ok               |
|          25 | -2.91%   | 0.21%              | -4.32% |    -0.97 |       60 | 37.27%     | ok               |
|          45 | -2.66%   | 0.21%              | -3.43% |    -0.98 |       52 | 27.45%     | ok               |

## SKY-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -40.61%  | 6.88%              | -52.23% |    -0.51 |       84 | 45.56%     | ok               |
|          15 | -46.89%  | 6.88%              | -58.78% |    -0.55 |       70 | 54.83%     | ok               |
|          25 | -47.13%  | 6.88%              | -57.47% |    -0.63 |       77 | 49.03%     | ok               |
|          35 | -45.72%  | 6.88%              | -50.91% |    -0.72 |       78 | 38.03%     | ok               |
|          20 | -54.51%  | 6.88%              | -64.70% |    -0.76 |       72 | 52.32%     | ok               |

## SLB Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 12.23%   | 5.34%              | -23.11% |     0.34 |       58 | 33.61%     | ok               |
|          40 | 9.92%    | 5.34%              | -27.08% |     0.29 |       48 | 37.10%     | ok               |
|          50 | -4.09%   | 5.34%              | -31.26% |    -0    |       50 | 29.12%     | ok               |
|          35 | -16.82%  | 5.34%              | -44.77% |    -0.24 |       70 | 43.43%     | ok               |
|          30 | -35.61%  | 5.34%              | -56.30% |    -0.66 |       75 | 49.42%     | ok               |

## SLV Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 44.42%   | 135.32%            | -34.10% |     0.66 |       54 | 30.78%     | ok               |
|          45 | 32.15%   | 135.32%            | -31.82% |     0.54 |       65 | 32.28%     | ok               |
|          40 | 30.57%   | 135.32%            | -34.28% |     0.52 |       71 | 34.44%     | ok               |
|          15 | 20.31%   | 135.32%            | -47.98% |     0.41 |       75 | 50.92%     | ok               |
|          20 | 19.48%   | 135.32%            | -42.66% |     0.4  |       74 | 45.59%     | ok               |

## SMH Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 86.99%   | 164.19%            | -31.66% |     1.13 |       49 | 47.92%     | ok               |
|          35 | 70.33%   | 164.19%            | -34.65% |     1.02 |       54 | 43.26%     | ok               |
|          25 | 69.26%   | 164.19%            | -33.57% |     1    |       46 | 46.59%     | ok               |
|          30 | 67.47%   | 164.19%            | -34.29% |     0.99 |       48 | 44.93%     | ok               |
|          45 | 55.28%   | 164.19%            | -33.35% |     0.93 |       54 | 37.44%     | ok               |

## SNX-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | -8.03%   | -65.14%            | -37.62% |     0.11 |       54 | 26.05%     | ok               |
|          20 | -15.26%  | -65.14%            | -47.56% |     0.08 |       71 | 43.10%     | ok               |
|          40 | -9.43%   | -65.14%            | -36.94% |     0.04 |       44 | 21.46%     | ok               |
|          30 | -20.22%  | -65.14%            | -47.16% |    -0.03 |       62 | 32.76%     | ok               |
|          15 | -40.86%  | -65.14%            | -49.47% |    -0.24 |       81 | 48.08%     | ok               |

## SOL-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 43.24%   | -16.78%            | -38.17% |     0.64 |       56 | 38.12%     | ok               |
|          35 | 19.37%   | -16.78%            | -43.70% |     0.41 |       68 | 44.64%     | ok               |
|          45 | 8.98%    | -16.78%            | -46.83% |     0.3  |       56 | 32.57%     | ok               |
|          25 | 2.13%    | -16.78%            | -41.09% |     0.25 |       70 | 57.85%     | ok               |
|          15 | -2.22%   | -16.78%            | -46.84% |     0.21 |       73 | 63.60%     | ok               |

## SOXX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | 75.64%   | 144.39%            | -39.32% |     1    |       55 | 45.59%     | ok               |
|          35 | 70.38%   | 144.39%            | -38.76% |     0.97 |       58 | 40.93%     | ok               |
|          30 | 69.47%   | 144.39%            | -39.81% |     0.95 |       56 | 43.26%     | ok               |
|          20 | 60.13%   | 144.39%            | -39.19% |     0.85 |       61 | 46.59%     | ok               |
|          40 | 48.85%   | 144.39%            | -41.03% |     0.78 |       58 | 38.77%     | ok               |

## SPY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 13.55%   | 51.46%             | -14.25% |     0.49 |       61 | 55.57%     | ok               |
|          15 | 13.00%   | 51.46%             | -16.80% |     0.46 |       65 | 58.24%     | ok               |
|          25 | 8.06%    | 51.46%             | -14.25% |     0.33 |       61 | 54.41%     | ok               |
|          30 | 3.49%    | 51.46%             | -15.53% |     0.18 |       64 | 51.58%     | ok               |
|          35 | 2.49%    | 51.46%             | -15.58% |     0.15 |       62 | 48.42%     | ok               |

## SUSHI-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -34.38%  | -55.92%            | -42.31% |    -0.49 |       54 | 14.18%     | ok               |
|          15 | -81.17%  | -55.92%            | -83.03% |    -1.12 |       92 | 48.85%     | ok               |
|          20 | -81.83%  | -55.92%            | -82.37% |    -1.24 |       95 | 45.98%     | ok               |
|          45 | -69.18%  | -55.92%            | -69.95% |    -1.26 |       60 | 18.58%     | ok               |
|          40 | -72.16%  | -55.92%            | -72.85% |    -1.26 |       66 | 24.90%     | ok               |

## T Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 65.78%   | 53.14%             | -15.08% |     1.15 |       71 | 67.39%     | ok               |
|          20 | 61.70%   | 53.14%             | -18.13% |     1.13 |       66 | 62.90%     | ok               |
|          25 | 57.32%   | 53.14%             | -17.66% |     1.08 |       66 | 60.57%     | ok               |
|          30 | 42.64%   | 53.14%             | -17.01% |     0.89 |       70 | 58.40%     | ok               |
|          35 | 27.09%   | 53.14%             | -14.49% |     0.65 |       76 | 54.08%     | ok               |

## TGT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -12.70%  | -2.80%             | -36.37% |    -0.2  |       60 | 37.77%     | ok               |
|          25 | -13.74%  | -2.80%             | -39.65% |    -0.21 |       66 | 40.43%     | ok               |
|          20 | -15.49%  | -2.80%             | -40.95% |    -0.22 |       84 | 45.09%     | ok               |
|          45 | -12.96%  | -2.80%             | -26.68% |    -0.25 |       52 | 28.79%     | ok               |
|          15 | -19.93%  | -2.80%             | -40.65% |    -0.3  |       76 | 50.08%     | ok               |

## TIA-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -54.15%  | -84.09%            | -63.05% |    -0.27 |       94 | 58.43%     | ok               |
|          35 | -43.14%  | -84.09%            | -60.91% |    -0.33 |       70 | 34.10%     | ok               |
|          45 | -42.27%  | -84.09%            | -62.76% |    -0.53 |       58 | 18.77%     | ok               |
|          40 | -51.97%  | -84.09%            | -66.99% |    -0.55 |       74 | 28.16%     | ok               |
|          50 | -33.92%  | -84.09%            | -55.83% |    -0.57 |       36 | 11.30%     | ok               |

## TLT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -20.14%  | -6.84%             | -21.87% |    -1.49 |       72 | 34.28%     | ok               |
|          50 | -14.00%  | -6.84%             | -15.03% |    -1.63 |       36 | 15.64%     | ok               |
|          40 | -18.26%  | -6.84%             | -17.88% |    -1.64 |       56 | 24.13%     | ok               |
|          15 | -25.78%  | -6.84%             | -27.76% |    -1.74 |       79 | 42.43%     | ok               |
|          35 | -21.58%  | -6.84%             | -21.37% |    -1.81 |       66 | 28.29%     | ok               |

## TMO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 52.49%   | 15.15%             | -8.17%  |     1.13 |       46 | 33.94%     | ok               |
|          45 | 46.54%   | 15.15%             | -9.69%  |     0.98 |       50 | 38.77%     | ok               |
|          40 | 42.26%   | 15.15%             | -9.91%  |     0.89 |       55 | 43.59%     | ok               |
|          35 | 36.79%   | 15.15%             | -13.84% |     0.75 |       67 | 48.92%     | ok               |
|          20 | 30.39%   | 15.15%             | -22.89% |     0.61 |       76 | 60.40%     | ok               |

## TMUS Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 2.41%    | 1.46%              | -27.06% |     0.15 |       76 | 48.25%     | ok               |
|          15 | -1.02%   | 1.46%              | -34.48% |     0.08 |       68 | 60.90%     | ok               |
|          25 | -5.27%   | 1.46%              | -32.65% |    -0.01 |       79 | 51.08%     | ok               |
|          20 | -6.73%   | 1.46%              | -33.09% |    -0.04 |       74 | 55.24%     | ok               |
|          50 | -6.53%   | 1.46%              | -29.49% |    -0.11 |       60 | 34.94%     | ok               |

## TRX-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 19.40%   | 34.15%             | -18.79% |     0.62 |       54 | 40.42%     | ok               |
|          35 | 12.97%   | 34.15%             | -21.77% |     0.43 |       68 | 49.23%     | ok               |
|          20 | 12.33%   | 34.15%             | -25.45% |     0.39 |       61 | 59.39%     | ok               |
|          30 | 10.93%   | 34.15%             | -22.90% |     0.38 |       68 | 52.30%     | ok               |
|          25 | 8.24%    | 34.15%             | -26.84% |     0.3  |       66 | 55.94%     | ok               |

## TSLA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 41.91%   | 115.18%            | -30.57% |     0.61 |       62 | 29.78%     | ok               |
|          40 | 14.07%   | 115.18%            | -50.11% |     0.34 |       61 | 35.27%     | ok               |
|          45 | -10.25%  | 115.18%            | -52.01% |     0.07 |       67 | 32.28%     | ok               |
|          35 | -17.74%  | 115.18%            | -58.86% |     0    |       72 | 37.94%     | ok               |
|          30 | -35.03%  | 115.18%            | -58.36% |    -0.22 |       80 | 43.09%     | ok               |

## TXN Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 7.81%    | 47.30%             | -45.45% |     0.25 |       60 | 32.11%     | ok               |
|          35 | -10.27%  | 47.30%             | -45.21% |    -0.03 |       74 | 46.76%     | ok               |
|          40 | -11.18%  | 47.30%             | -47.43% |    -0.05 |       70 | 44.59%     | ok               |
|          45 | -11.69%  | 47.30%             | -46.24% |    -0.07 |       76 | 38.60%     | ok               |
|          20 | -17.23%  | 47.30%             | -40.96% |    -0.1  |       68 | 56.57%     | ok               |

## UNH Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 31.20%   | -24.03%            | -26.31% |     0.53 |       73 | 50.08%     | ok               |
|          50 | 28.37%   | -24.03%            | -36.71% |     0.53 |       52 | 29.28%     | ok               |
|          35 | 26.15%   | -24.03%            | -28.26% |     0.48 |       68 | 44.93%     | ok               |
|          15 | 22.91%   | -24.03%            | -29.48% |     0.43 |       79 | 65.22%     | ok               |
|          20 | 20.66%   | -24.03%            | -30.79% |     0.41 |       76 | 58.90%     | ok               |

## UNI-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 36.71%   | 65.23%             | -45.09% |     0.57 |       52 | 24.14%     | ok               |
|          45 | 25.54%   | 65.23%             | -51.70% |     0.47 |       58 | 31.80%     | ok               |
|          40 | 16.49%   | 65.23%             | -61.16% |     0.4  |       62 | 36.40%     | ok               |
|          35 | -0.30%   | 65.23%             | -65.47% |     0.26 |       76 | 42.34%     | ok               |
|          20 | -53.29%  | 65.23%             | -80.78% |    -0.28 |       97 | 58.24%     | ok               |

## UPS Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | -29.07%  | -32.04%            | -31.52% |    -0.55 |       62 | 34.28%     | ok               |
|          40 | -29.19%  | -32.04%            | -31.37% |    -0.57 |       58 | 28.95%     | ok               |
|          20 | -34.41%  | -32.04%            | -38.05% |    -0.64 |       84 | 47.09%     | ok               |
|          25 | -34.94%  | -32.04%            | -38.34% |    -0.68 |       76 | 43.76%     | ok               |
|          30 | -34.92%  | -32.04%            | -38.32% |    -0.69 |       70 | 40.10%     | ok               |

## USO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 18.30%   | 93.08%             | -32.35% |     0.4  |       46 | 25.79%     | ok               |
|          20 | 16.82%   | 93.08%             | -44.43% |     0.37 |       74 | 37.94%     | ok               |
|          25 | 12.86%   | 93.08%             | -44.12% |     0.32 |       68 | 35.44%     | ok               |
|          15 | 11.24%   | 93.08%             | -44.08% |     0.3  |       75 | 41.10%     | ok               |
|          30 | 10.16%   | 93.08%             | -41.71% |     0.28 |       70 | 32.78%     | ok               |

## VEA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 7.54%    | 48.70%             | -13.99% |     0.32 |       56 | 49.58%     | ok               |
|          20 | 1.29%    | 48.70%             | -15.74% |     0.1  |       61 | 46.92%     | ok               |
|          25 | -1.87%   | 48.70%             | -15.84% |    -0.02 |       57 | 45.09%     | ok               |
|          30 | -2.07%   | 48.70%             | -16.01% |    -0.03 |       58 | 43.26%     | ok               |
|          35 | -3.16%   | 48.70%             | -14.84% |    -0.08 |       56 | 42.26%     | ok               |

## VIXY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -55.17%  | -69.24%            | -69.78% |    -0.63 |       40 | 10.82%     | ok               |
|          15 | -75.09%  | -69.24%            | -89.47% |    -0.73 |       97 | 45.26%     | ok               |
|          45 | -64.78%  | -69.24%            | -75.03% |    -0.84 |       60 | 15.81%     | ok               |
|          30 | -76.58%  | -69.24%            | -88.17% |    -0.88 |       96 | 34.11%     | ok               |
|          20 | -80.09%  | -69.24%            | -90.58% |    -0.92 |       93 | 41.26%     | ok               |

## VNQ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -10.36%  | 17.09%             | -19.07% |    -0.46 |       60 | 28.45%     | ok               |
|          50 | -10.79%  | 17.09%             | -17.13% |    -0.5  |       56 | 25.96%     | ok               |
|          25 | -13.95%  | 17.09%             | -22.34% |    -0.54 |       73 | 41.93%     | ok               |
|          40 | -15.01%  | 17.09%             | -24.84% |    -0.67 |       78 | 32.95%     | ok               |
|          20 | -17.48%  | 17.09%             | -24.00% |    -0.68 |       76 | 45.26%     | ok               |

## VTI Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 14.24%   | 50.46%             | -13.96% |     0.51 |       64 | 56.07%     | ok               |
|          15 | 9.54%    | 50.46%             | -15.70% |     0.36 |       61 | 58.40%     | ok               |
|          25 | 1.65%    | 50.46%             | -15.00% |     0.12 |       60 | 53.74%     | ok               |
|          30 | -5.97%   | 50.46%             | -17.64% |    -0.16 |       70 | 51.75%     | ok               |
|          40 | -7.10%   | 50.46%             | -19.77% |    -0.22 |       74 | 44.26%     | ok               |

## VWO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -8.54%   | 43.19%             | -22.18% |    -0.31 |       56 | 29.62%     | ok               |
|          15 | -11.39%  | 43.19%             | -23.73% |    -0.35 |       74 | 48.09%     | ok               |
|          45 | -9.75%   | 43.19%             | -23.75% |    -0.36 |       58 | 32.28%     | ok               |
|          40 | -10.21%  | 43.19%             | -23.57% |    -0.37 |       68 | 35.11%     | ok               |
|          20 | -12.80%  | 43.19%             | -25.88% |    -0.42 |       71 | 45.76%     | ok               |

## VZ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 0.82%    | 23.23%             | -12.55% |     0.09 |       54 | 27.95%     | ok               |
|          25 | -11.39%  | 23.23%             | -22.13% |    -0.26 |       78 | 45.42%     | ok               |
|          35 | -10.26%  | 23.23%             | -22.73% |    -0.26 |       60 | 37.44%     | ok               |
|          45 | -10.75%  | 23.23%             | -21.44% |    -0.29 |       66 | 31.78%     | ok               |
|          40 | -15.28%  | 23.23%             | -24.21% |    -0.45 |       64 | 34.78%     | ok               |

## WFC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | -7.48%   | 44.99%             | -21.57% |    -0.09 |       77 | 43.76%     | ok               |
|          50 | -6.82%   | 44.99%             | -18.29% |    -0.15 |       60 | 32.11%     | ok               |
|          20 | -18.09%  | 44.99%             | -29.87% |    -0.26 |       77 | 52.41%     | ok               |
|          30 | -17.12%  | 44.99%             | -28.90% |    -0.28 |       80 | 46.92%     | ok               |
|          40 | -13.20%  | 44.99%             | -23.94% |    -0.31 |       72 | 40.43%     | ok               |

## WIF-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 70.57%   | -50.49%            | -40.67% |     0.71 |       65 | 43.68%     | ok               |
|          15 | 33.29%   | -50.49%            | -46.21% |     0.52 |       75 | 46.93%     | ok               |
|          25 | 0.90%    | -50.49%            | -44.74% |     0.29 |       69 | 39.46%     | ok               |
|          30 | -26.92%  | -50.49%            | -52.76% |    -0.02 |       66 | 35.63%     | ok               |
|          50 | -12.18%  | -50.49%            | -34.40% |    -0.04 |       32 | 11.30%     | ok               |

## WMT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 38.72%   | 77.36%             | -11.62% |     1.11 |       40 | 39.10%     | ok               |
|          50 | 33.90%   | 77.36%             | -12.19% |     1.05 |       32 | 36.77%     | ok               |
|          35 | 29.02%   | 77.36%             | -16.55% |     0.83 |       56 | 45.26%     | ok               |
|          40 | 27.36%   | 77.36%             | -15.99% |     0.82 |       48 | 40.60%     | ok               |
|          15 | 12.05%   | 77.36%             | -25.74% |     0.35 |       76 | 58.57%     | ok               |

## XBI Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 13.20%   | 92.47%             | -16.08% |     0.39 |       56 | 36.94%     | ok               |
|          45 | 10.67%   | 92.47%             | -15.46% |     0.34 |       52 | 34.28%     | ok               |
|          50 | 2.21%    | 92.47%             | -15.97% |     0.14 |       54 | 30.78%     | ok               |
|          35 | 1.24%    | 92.47%             | -16.96% |     0.12 |       64 | 40.27%     | ok               |
|          30 | -0.88%   | 92.47%             | -18.30% |     0.07 |       66 | 41.76%     | ok               |

## XLB Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -2.33%   | 13.99%             | -18.27% |    -0.04 |       54 | 26.79%     | ok               |
|          50 | -3.17%   | 13.99%             | -16.40% |    -0.08 |       38 | 22.96%     | ok               |
|          45 | -4.96%   | 13.99%             | -18.10% |    -0.16 |       42 | 24.29%     | ok               |
|          35 | -5.65%   | 13.99%             | -21.38% |    -0.16 |       54 | 30.28%     | ok               |
|          25 | -10.56%  | 13.99%             | -23.37% |    -0.35 |       62 | 35.61%     | ok               |

## XLC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 14.20%   | 44.11%             | -12.33% |     0.52 |       63 | 50.58%     | ok               |
|          25 | 13.65%   | 44.11%             | -12.31% |     0.5  |       62 | 52.75%     | ok               |
|          50 | 7.28%    | 44.11%             | -11.12% |     0.38 |       66 | 38.60%     | ok               |
|          20 | 9.83%    | 44.11%             | -11.04% |     0.36 |       67 | 55.41%     | ok               |
|          40 | 7.86%    | 44.11%             | -13.38% |     0.34 |       64 | 44.09%     | ok               |

## XLE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -1.77%   | 33.46%             | -25.98% |     0.03 |       54 | 35.94%     | ok               |
|          35 | -10.46%  | 33.46%             | -30.52% |    -0.19 |       69 | 42.93%     | ok               |
|          45 | -9.47%   | 33.46%             | -29.68% |    -0.2  |       62 | 38.10%     | ok               |
|          30 | -13.93%  | 33.46%             | -34.24% |    -0.28 |       73 | 44.76%     | ok               |
|          25 | -16.00%  | 33.46%             | -35.82% |    -0.32 |       82 | 47.92%     | ok               |

## XLF Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -3.61%   | 36.69%             | -18.63% |    -0.06 |       70 | 51.08%     | ok               |
|          15 | -6.31%   | 36.69%             | -20.19% |    -0.15 |       76 | 53.24%     | ok               |
|          25 | -9.07%   | 36.69%             | -23.22% |    -0.27 |       79 | 47.92%     | ok               |
|          30 | -9.66%   | 36.69%             | -23.61% |    -0.3  |       80 | 45.92%     | ok               |
|          35 | -16.69%  | 36.69%             | -24.48% |    -0.65 |       70 | 42.26%     | ok               |

## XLI Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 8.33%    | 38.01%             | -11.40% |     0.34 |       84 | 49.42%     | ok               |
|          20 | 4.41%    | 38.01%             | -12.74% |     0.22 |       73 | 44.43%     | ok               |
|          25 | -4.84%   | 38.01%             | -15.60% |    -0.13 |       74 | 42.60%     | ok               |
|          50 | -4.31%   | 38.01%             | -14.94% |    -0.16 |       60 | 31.61%     | ok               |
|          30 | -5.41%   | 38.01%             | -14.16% |    -0.16 |       76 | 41.60%     | ok               |

## XLK Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | 83.42%   | 90.34%             | -14.75% |     1.39 |       40 | 48.92%     | ok               |
|          20 | 86.95%   | 90.34%             | -14.75% |     1.39 |       46 | 50.92%     | ok               |
|          15 | 85.05%   | 90.34%             | -14.75% |     1.32 |       46 | 52.75%     | ok               |
|          30 | 72.44%   | 90.34%             | -14.75% |     1.29 |       40 | 47.59%     | ok               |
|          35 | 51.10%   | 90.34%             | -13.43% |     1.03 |       54 | 44.76%     | ok               |

## XLM-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -9.19%   | -20.34%            | -49.14% |     0.12 |       71 | 49.43%     | ok               |
|          50 | -6.60%   | -20.34%            | -48.81% |     0.09 |       44 | 25.48%     | ok               |
|          45 | -7.68%   | -20.34%            | -51.28% |     0.08 |       56 | 30.65%     | ok               |
|          30 | -12.91%  | -20.34%            | -54.58% |     0.07 |       67 | 46.36%     | ok               |
|          40 | -17.21%  | -20.34%            | -47.28% |    -0.02 |       53 | 36.21%     | ok               |

## XLP Threshold Sweep

|   threshold | return   | benchmark_return   | mdd    |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:-------|---------:|---------:|:-----------|:-----------------|
|          45 | 10.73%   | 10.22%             | -5.66% |     0.68 |       50 | 30.28%     | ok               |
|          40 | 10.11%   | 10.22%             | -7.32% |     0.62 |       66 | 34.28%     | ok               |
|          35 | 9.15%    | 10.22%             | -8.39% |     0.56 |       62 | 37.27%     | ok               |
|          50 | 7.63%    | 10.22%             | -6.08% |     0.5  |       54 | 28.62%     | ok               |
|          30 | 8.27%    | 10.22%             | -8.96% |     0.5  |       64 | 38.94%     | ok               |

## XLU Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 4.79%    | 24.60%             | -13.94% |     0.27 |       52 | 30.28%     | ok               |
|          45 | 3.64%    | 24.60%             | -14.88% |     0.22 |       56 | 31.45%     | ok               |
|          40 | 0.51%    | 24.60%             | -16.41% |     0.07 |       62 | 33.28%     | ok               |
|          35 | -2.16%   | 24.60%             | -19.71% |    -0.05 |       62 | 35.94%     | ok               |
|          30 | -3.52%   | 24.60%             | -20.40% |    -0.11 |       67 | 39.27%     | ok               |

## XLV Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -15.65%  | 20.65%             | -19.39% |    -0.71 |       68 | 37.27%     | ok               |
|          25 | -16.57%  | 20.65%             | -21.14% |    -0.75 |       70 | 39.43%     | ok               |
|          20 | -19.84%  | 20.65%             | -24.51% |    -0.91 |       73 | 41.10%     | ok               |
|          15 | -20.36%  | 20.65%             | -24.84% |    -0.91 |       79 | 43.76%     | ok               |
|          35 | -20.06%  | 20.65%             | -23.39% |    -1    |       66 | 34.78%     | ok               |

## XLY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -1.84%   | 27.78%             | -15.77% |     0.03 |       80 | 52.75%     | ok               |
|          30 | -6.37%   | 27.78%             | -17.65% |    -0.13 |       79 | 46.26%     | ok               |
|          20 | -7.04%   | 27.78%             | -19.25% |    -0.13 |       76 | 49.42%     | ok               |
|          25 | -9.11%   | 27.78%             | -19.29% |    -0.2  |       73 | 47.92%     | ok               |
|          50 | -7.75%   | 27.78%             | -14.83% |    -0.28 |       62 | 31.28%     | ok               |

## XOM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 0.63%    | 34.57%             | -21.35% |     0.09 |       36 | 26.96%     | ok               |
|          25 | -1.39%   | 34.57%             | -19.90% |     0.04 |       59 | 35.27%     | ok               |
|          30 | -2.37%   | 34.57%             | -20.29% |     0.01 |       59 | 34.61%     | ok               |
|          45 | -5.91%   | 34.57%             | -23.33% |    -0.1  |       44 | 28.45%     | ok               |
|          20 | -7.00%   | 34.57%             | -25.56% |    -0.11 |       66 | 37.60%     | ok               |

## XRP-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 23.51%   | -36.72%            | -31.38% |     0.45 |       70 | 43.10%     | ok               |
|          40 | 9.21%    | -36.72%            | -33.91% |     0.3  |       60 | 36.59%     | ok               |
|          30 | 4.01%    | -36.72%            | -31.82% |     0.25 |       65 | 47.89%     | ok               |
|          45 | -1.97%   | -36.72%            | -36.27% |     0.16 |       58 | 32.18%     | ok               |
|          20 | -8.04%   | -36.72%            | -38.12% |     0.12 |       77 | 55.94%     | ok               |

## YFI-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -48.65%  | -51.84%            | -50.05% |    -0.84 |       56 | 26.63%     | ok               |
|          45 | -48.73%  | -51.84%            | -50.13% |    -1.08 |       70 | 21.26%     | ok               |
|          35 | -63.97%  | -51.84%            | -66.31% |    -1.16 |       67 | 34.10%     | ok               |
|          30 | -67.17%  | -51.84%            | -72.54% |    -1.2  |       79 | 38.31%     | ok               |
|          15 | -73.02%  | -51.84%            | -76.87% |    -1.29 |       85 | 50.77%     | ok               |

## ZEC-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 236.05%  | 4733.61%           | -30.64% |     1.16 |       46 | 30.27%     | ok               |
|          35 | 206.55%  | 4733.61%           | -50.84% |     1.07 |       52 | 37.16%     | ok               |
|          25 | 192.12%  | 4733.61%           | -58.07% |     1.02 |       56 | 44.25%     | ok               |
|          30 | 172.60%  | 4733.61%           | -56.50% |     0.98 |       64 | 41.38%     | ok               |
|          20 | 144.75%  | 4733.61%           | -62.70% |     0.91 |       63 | 46.36%     | ok               |
