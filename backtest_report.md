# Market Tracker Backtest Report

_Generated: 2026-08-07T03:26:46+00:00_

## Data Sources

- Crypto: Kraken -> Coinbase -> CoinGecko OHLC -> CoinPaprika fallback chain.
- Stocks / ETFs / indices: Stooq -> Yahoo Finance fallback chain.
- Data rows are generated from real market APIs. Mock OHLCV rows are not generated.

## Data Freshness

- Rows: **92,577**
- Symbols: **161**
- Date range: **2024-03-14** to **2026-08-07**

## Latest Signals

| symbol     | date                |         close |   composite_score | signal   | data_source   |
|:-----------|:--------------------|--------------:|------------------:|:---------|:--------------|
| ADBE       | 2026-08-06 00:00:00 |   260.24      |         34.8333   | LONG     | Yahoo Finance |
| AMGN       | 2026-08-06 00:00:00 |   404.85      |         59.75     | LONG     | Yahoo Finance |
| AMZN       | 2026-08-06 00:00:00 |   272.26      |         71.25     | LONG     | Yahoo Finance |
| BA         | 2026-08-06 00:00:00 |   232.19      |         62.5833   | LONG     | Yahoo Finance |
| BLK        | 2026-08-06 00:00:00 |  1129.3       |         58.0833   | LONG     | Yahoo Finance |
| C          | 2026-08-06 00:00:00 |   133.82      |         46.9167   | LONG     | Yahoo Finance |
| COP        | 2026-08-06 00:00:00 |   116.76      |         46.5833   | LONG     | Yahoo Finance |
| CVX        | 2026-08-06 00:00:00 |   189.23      |         54.0833   | LONG     | Yahoo Finance |
| DBC        | 2026-08-06 00:00:00 |    28.86      |         38.9167   | LONG     | Yahoo Finance |
| EEM        | 2026-08-06 00:00:00 |    65.02      |         46.9167   | LONG     | Yahoo Finance |
| FXI        | 2026-08-06 00:00:00 |    35.95      |         33.5      | LONG     | Yahoo Finance |
| GE         | 2026-08-06 00:00:00 |   374.55      |         53.5833   | LONG     | Yahoo Finance |
| HON        | 2026-08-06 00:00:00 |   240.74      |         74.4167   | LONG     | Yahoo Finance |
| IEMG       | 2026-08-06 00:00:00 |    79.34      |         64.9167   | LONG     | Yahoo Finance |
| INTC       | 2026-08-06 00:00:00 |    99.81      |         47.1667   | LONG     | Yahoo Finance |
| INTU       | 2026-08-06 00:00:00 |   321.91      |         33.9167   | LONG     | Yahoo Finance |
| ITA        | 2026-08-06 00:00:00 |   249.99      |         62.75     | LONG     | Yahoo Finance |
| IWM        | 2026-08-06 00:00:00 |   298.25      |         75.5833   | LONG     | Yahoo Finance |
| MSFT       | 2026-08-06 00:00:00 |   499.86      |         60.25     | LONG     | Yahoo Finance |
| OXY        | 2026-08-06 00:00:00 |    56.04      |         56.5833   | LONG     | Yahoo Finance |
| PFE        | 2026-08-06 00:00:00 |    26.2       |         71.3333   | LONG     | Yahoo Finance |
| QQQ        | 2026-08-06 00:00:00 |   714.65      |         65.4167   | LONG     | Yahoo Finance |
| RTX        | 2026-08-06 00:00:00 |   223.25      |         61.75     | LONG     | Yahoo Finance |
| SCHW       | 2026-08-06 00:00:00 |   107.66      |         47.3333   | LONG     | Yahoo Finance |
| SHIB-USD   | 2026-08-07 00:00:00 |     4.692e-06 |         41.5      | LONG     | Kraken API    |
| SLB        | 2026-08-06 00:00:00 |    51.54      |         72.9167   | LONG     | Yahoo Finance |
| SMH        | 2026-08-06 00:00:00 |   571.48      |         63.6667   | LONG     | Yahoo Finance |
| SOXX       | 2026-08-06 00:00:00 |   532.52      |         37.9167   | LONG     | Yahoo Finance |
| T          | 2026-08-06 00:00:00 |    23.71      |         40.6667   | LONG     | Yahoo Finance |
| TGT        | 2026-08-06 00:00:00 |   147.08      |         74.9167   | LONG     | Yahoo Finance |
| TRX-USD    | 2026-08-07 00:00:00 |     0.327714  |         42.4167   | LONG     | Kraken API    |
| UNI-USD    | 2026-08-07 00:00:00 |     4.0297    |         50        | LONG     | Kraken API    |
| VTI        | 2026-08-06 00:00:00 |   379.07      |         74.0833   | LONG     | Yahoo Finance |
| VZ         | 2026-08-06 00:00:00 |    46.99      |         76.9167   | LONG     | Yahoo Finance |
| XBI        | 2026-08-06 00:00:00 |   154.5       |         60.75     | LONG     | Yahoo Finance |
| XLE        | 2026-08-06 00:00:00 |    58.16      |         46.5833   | LONG     | Yahoo Finance |
| XLI        | 2026-08-06 00:00:00 |   184.76      |         73.5833   | LONG     | Yahoo Finance |
| XLK        | 2026-08-06 00:00:00 |   185.33      |         72.0833   | LONG     | Yahoo Finance |
| XLP        | 2026-08-06 00:00:00 |    85.11      |         50.0833   | LONG     | Yahoo Finance |
| XOM        | 2026-08-06 00:00:00 |   154.84      |         59.0833   | LONG     | Yahoo Finance |
| ZEC-USD    | 2026-08-07 00:00:00 |   505.75      |         72.3333   | LONG     | Kraken API    |
| AAPL       | 2026-08-06 00:00:00 |   312.41      |         18.4167   | NEUTRAL  | Yahoo Finance |
| AAVE-USD   | 2026-08-07 00:00:00 |    90.57      |        -25.25     | NEUTRAL  | Kraken API    |
| ABBV       | 2026-08-06 00:00:00 |   243.87      |        -12.8333   | NEUTRAL  | Yahoo Finance |
| ADA-USD    | 2026-08-07 00:00:00 |     0.200015  |         35.75     | NEUTRAL  | Kraken API    |
| AGG        | 2026-08-06 00:00:00 |    97.43      |        -42.6667   | NEUTRAL  | Yahoo Finance |
| ALGO-USD   | 2026-08-07 00:00:00 |     0.09016   |         43.5833   | NEUTRAL  | Kraken API    |
| AMAT       | 2026-08-06 00:00:00 |   527.48      |          2.5      | NEUTRAL  | Yahoo Finance |
| AMD        | 2026-08-06 00:00:00 |   489.28      |        -11.5      | NEUTRAL  | Yahoo Finance |
| APT-USD    | 2026-08-07 00:00:00 |     0.5917    |        -11.9167   | NEUTRAL  | Kraken API    |
| ARKK       | 2026-08-06 00:00:00 |    75.73      |         25.6667   | NEUTRAL  | Yahoo Finance |
| ATOM-USD   | 2026-08-07 00:00:00 |     1.3525    |        -17        | NEUTRAL  | Kraken API    |
| AVAX-USD   | 2026-08-07 00:00:00 |     6.439     |         -6.75     | NEUTRAL  | Kraken API    |
| AVGO       | 2026-08-06 00:00:00 |   420.565     |         39.5      | NEUTRAL  | Yahoo Finance |
| BAC        | 2026-08-06 00:00:00 |    63         |         24.8333   | NEUTRAL  | Yahoo Finance |
| BCH-USD    | 2026-08-07 00:00:00 |   213.33      |         -9.83333  | NEUTRAL  | Kraken API    |
| BITO       | 2026-08-06 00:00:00 |     8.7       |        -10.25     | NEUTRAL  | Yahoo Finance |
| BONK-USD   | 2026-08-07 00:00:00 |     2.96e-06  |        -20.25     | NEUTRAL  | Kraken API    |
| BTC-USD    | 2026-08-07 00:00:00 | 64330.2       |          8.91667  | NEUTRAL  | Kraken API    |
| CAT        | 2026-08-06 00:00:00 |   856.96      |         13.5      | NEUTRAL  | Yahoo Finance |
| CL         | 2026-08-06 00:00:00 |    93         |         57.8333   | NEUTRAL  | Yahoo Finance |
| CMCSA      | 2026-08-06 00:00:00 |    25.17      |         45.3333   | NEUTRAL  | Yahoo Finance |
| COST       | 2026-08-06 00:00:00 |   949.15      |         24.25     | NEUTRAL  | Yahoo Finance |
| CRM        | 2026-08-06 00:00:00 |   186.77      |         19.3333   | NEUTRAL  | Yahoo Finance |
| CRV-USD    | 2026-08-07 00:00:00 |     0.21649   |         46.8333   | NEUTRAL  | Kraken API    |
| CSCO       | 2026-08-06 00:00:00 |   120.88      |         59.5      | NEUTRAL  | Yahoo Finance |
| DE         | 2026-08-06 00:00:00 |   614.84      |         50.3333   | NEUTRAL  | Yahoo Finance |
| DIA        | 2026-08-06 00:00:00 |   538.19      |         62.3333   | NEUTRAL  | Yahoo Finance |
| DIS        | 2026-08-06 00:00:00 |   104.68      |         58.0833   | NEUTRAL  | Yahoo Finance |
| DOGE-USD   | 2026-08-07 00:00:00 |     0.0693062 |         -6        | NEUTRAL  | Kraken API    |
| DOT-USD    | 2026-08-07 00:00:00 |     0.8209    |         27.6667   | NEUTRAL  | Kraken API    |
| DXY-INDEX  | 2026-08-06 00:00:00 |    99.974     |         -6.98925  | NEUTRAL  | Yahoo Finance |
| EFA        | 2026-08-06 00:00:00 |   107.36      |         44.8333   | NEUTRAL  | Yahoo Finance |
| EOG        | 2026-08-06 00:00:00 |   136.2       |         -1.58333  | NEUTRAL  | Yahoo Finance |
| ETC-USD    | 2026-08-07 00:00:00 |     6.51      |        -35.75     | NEUTRAL  | Kraken API    |
| ETH-USD    | 2026-08-07 00:00:00 |  1901.42      |         17.5      | NEUTRAL  | Kraken API    |
| EWJ        | 2026-08-06 00:00:00 |    95.15      |         44.8333   | NEUTRAL  | Yahoo Finance |
| FCX        | 2026-08-06 00:00:00 |    68.18      |         57        | NEUTRAL  | Yahoo Finance |
| FET-USD    | 2026-08-07 00:00:00 |     0.1348    |        -20.6667   | NEUTRAL  | Kraken API    |
| FIL-USD    | 2026-08-07 00:00:00 |     0.7       |         -9.66667  | NEUTRAL  | Kraken API    |
| GDX        | 2026-08-06 00:00:00 |    83.92      |         50.5      | NEUTRAL  | Yahoo Finance |
| GDXJ       | 2026-08-06 00:00:00 |   109.4       |         50.5      | NEUTRAL  | Yahoo Finance |
| GLD        | 2026-08-06 00:00:00 |   389.67      |         28.8333   | NEUTRAL  | Yahoo Finance |
| GOOGL      | 2026-08-06 00:00:00 |   357.75      |         39.5      | NEUTRAL  | Yahoo Finance |
| GRT-USD    | 2026-08-07 00:00:00 |     0.01449   |         -8        | NEUTRAL  | Kraken API    |
| GS         | 2026-08-06 00:00:00 |  1032.58      |        -27.3333   | NEUTRAL  | Yahoo Finance |
| HBAR-USD   | 2026-08-07 00:00:00 |     0.06824   |        -14.6667   | NEUTRAL  | Kraken API    |
| HD         | 2026-08-06 00:00:00 |   349.52      |         53.8333   | NEUTRAL  | Yahoo Finance |
| IBIT       | 2026-08-06 00:00:00 |    36.49      |        -23        | NEUTRAL  | Yahoo Finance |
| IBM        | 2026-08-06 00:00:00 |   233.43      |        -22.6667   | NEUTRAL  | Yahoo Finance |
| ICP-USD    | 2026-08-07 00:00:00 |     2.083     |        -18.6667   | NEUTRAL  | Kraken API    |
| IEF        | 2026-08-06 00:00:00 |    92.95      |        -42.6667   | NEUTRAL  | Yahoo Finance |
| INJ-USD    | 2026-08-07 00:00:00 |     4.501     |        -50.25     | NEUTRAL  | Kraken API    |
| JNJ        | 2026-08-06 00:00:00 |   256.98      |         27.8333   | NEUTRAL  | Yahoo Finance |
| JPM        | 2026-08-06 00:00:00 |   356.3       |         38.3333   | NEUTRAL  | Yahoo Finance |
| KO         | 2026-08-06 00:00:00 |    86.85      |         64        | NEUTRAL  | Yahoo Finance |
| LIN        | 2026-08-06 00:00:00 |   490.11      |        -15.5833   | NEUTRAL  | Yahoo Finance |
| LINK-USD   | 2026-08-07 00:00:00 |     8.1921    |        -32.4167   | NEUTRAL  | Kraken API    |
| LLY        | 2026-08-06 00:00:00 |  1191.94      |         22.5      | NEUTRAL  | Yahoo Finance |
| LRCX       | 2026-08-06 00:00:00 |   305.77      |          7.5      | NEUTRAL  | Yahoo Finance |
| LTC-USD    | 2026-08-07 00:00:00 |    45.53      |        -15.3333   | NEUTRAL  | Kraken API    |
| MCD        | 2026-08-06 00:00:00 |   276.26      |         22.1667   | NEUTRAL  | Yahoo Finance |
| MPC        | 2026-08-06 00:00:00 |   299.25      |         16.4167   | NEUTRAL  | Yahoo Finance |
| MRK        | 2026-08-06 00:00:00 |   128.37      |         50.3333   | NEUTRAL  | Yahoo Finance |
| MS         | 2026-08-06 00:00:00 |   213.75      |         -3.58333  | NEUTRAL  | Yahoo Finance |
| MU         | 2026-08-06 00:00:00 |   881.47      |         -0.833333 | NEUTRAL  | Yahoo Finance |
| NEM        | 2026-08-06 00:00:00 |   105.43      |         54.25     | NEUTRAL  | Yahoo Finance |
| NFLX       | 2026-08-06 00:00:00 |    73.69      |         11.4167   | NEUTRAL  | Yahoo Finance |
| NKE        | 2026-08-06 00:00:00 |    42         |        -62.8333   | NEUTRAL  | Yahoo Finance |
| NOW        | 2026-08-06 00:00:00 |   117.35      |         11.8333   | NEUTRAL  | Yahoo Finance |
| NVDA       | 2026-08-06 00:00:00 |   218.99      |         42.8333   | NEUTRAL  | Yahoo Finance |
| OP-USD     | 2026-08-07 00:00:00 |     0.0876    |        -15        | NEUTRAL  | Kraken API    |
| ORCL       | 2026-08-06 00:00:00 |   143.47      |         -1.58333  | NEUTRAL  | Yahoo Finance |
| PEP        | 2026-08-06 00:00:00 |   138.44      |        -19.5      | NEUTRAL  | Yahoo Finance |
| PEPE-USD   | 2026-08-07 00:00:00 |     2.802e-06 |        -22.4167   | NEUTRAL  | Kraken API    |
| PG         | 2026-08-06 00:00:00 |   146.97      |        -51.8333   | NEUTRAL  | Yahoo Finance |
| PM         | 2026-08-06 00:00:00 |   188.05      |         23.9167   | NEUTRAL  | Yahoo Finance |
| POL-USD    | 2026-08-07 00:00:00 |     0.07502   |        -17        | NEUTRAL  | Kraken API    |
| QCOM       | 2026-08-06 00:00:00 |   160.39      |        -24.25     | NEUTRAL  | Yahoo Finance |
| SBUX       | 2026-08-06 00:00:00 |   105.16      |         24.8333   | NEUTRAL  | Yahoo Finance |
| SHY        | 2026-08-06 00:00:00 |    81.8       |        -49.75     | NEUTRAL  | Yahoo Finance |
| SLV        | 2026-08-06 00:00:00 |    55.85      |          0.166667 | NEUTRAL  | Yahoo Finance |
| SNX-USD    | 2026-08-07 00:00:00 |     0.2138    |         -9.5      | NEUTRAL  | Kraken API    |
| SPY        | 2026-08-06 00:00:00 |   768.56      |         62.8333   | NEUTRAL  | Yahoo Finance |
| SUSHI-USD  | 2026-08-07 00:00:00 |     0.1648    |         -2.25     | NEUTRAL  | Kraken API    |
| TIA-USD    | 2026-08-07 00:00:00 |     0.3375    |        -15        | NEUTRAL  | Kraken API    |
| TMO        | 2026-08-06 00:00:00 |   580.02      |         48.8333   | NEUTRAL  | Yahoo Finance |
| TXN        | 2026-08-06 00:00:00 |   278.4       |        -13.9167   | NEUTRAL  | Yahoo Finance |
| UNH        | 2026-08-06 00:00:00 |   403.97      |        -17.25     | NEUTRAL  | Yahoo Finance |
| USO        | 2026-08-06 00:00:00 |   118.87      |          2.66667  | NEUTRAL  | Yahoo Finance |
| VEA        | 2026-08-06 00:00:00 |    72.12      |         62.3333   | NEUTRAL  | Yahoo Finance |
| VIXY       | 2026-08-06 00:00:00 |    19.53      |        -39.5      | NEUTRAL  | Yahoo Finance |
| VNQ        | 2026-08-06 00:00:00 |    98.04      |         19.9167   | NEUTRAL  | Yahoo Finance |
| VWO        | 2026-08-06 00:00:00 |    59.96      |         44.8333   | NEUTRAL  | Yahoo Finance |
| WFC        | 2026-08-06 00:00:00 |    87.59      |         33.5833   | NEUTRAL  | Yahoo Finance |
| WIF-USD    | 2026-08-07 00:00:00 |     0.1401    |        -36.9167   | NEUTRAL  | Kraken API    |
| WMT        | 2026-08-06 00:00:00 |   112.07      |        -33        | NEUTRAL  | Yahoo Finance |
| XLB        | 2026-08-06 00:00:00 |    52.17      |         60.6667   | NEUTRAL  | Yahoo Finance |
| XLC        | 2026-08-06 00:00:00 |   111.18      |         14.5833   | NEUTRAL  | Yahoo Finance |
| XLF        | 2026-08-06 00:00:00 |    57.81      |         57.8333   | NEUTRAL  | Yahoo Finance |
| XLU        | 2026-08-06 00:00:00 |    43.38      |        -62.5      | NEUTRAL  | Yahoo Finance |
| XLV        | 2026-08-06 00:00:00 |   164.45      |         42.5      | NEUTRAL  | Yahoo Finance |
| XLY        | 2026-08-06 00:00:00 |   118.1       |         44.8333   | NEUTRAL  | Yahoo Finance |
| XRP-USD    | 2026-08-07 00:00:00 |     1.02981   |        -48.25     | NEUTRAL  | Kraken API    |
| YFI-USD    | 2026-08-07 00:00:00 |  2076         |         10.6667   | NEUTRAL  | Kraken API    |
| ARB-USD    | 2026-08-07 00:00:00 |     0.0783    |        -30.3333   | SHORT    | Kraken API    |
| BND        | 2026-08-06 00:00:00 |    72.25      |        -31.4167   | SHORT    | Yahoo Finance |
| COMP-USD   | 2026-08-07 00:00:00 |    16.33      |        -30.8333   | SHORT    | Kraken API    |
| DASH-USD   | 2026-08-07 00:00:00 |    31.115     |        -33        | SHORT    | Kraken API    |
| HYG        | 2026-08-06 00:00:00 |    79.46      |        -32        | SHORT    | Yahoo Finance |
| LDO-USD    | 2026-08-07 00:00:00 |     0.289     |        -48.3333   | SHORT    | Kraken API    |
| META       | 2026-08-06 00:00:00 |   589.9       |        -49.8333   | SHORT    | Yahoo Finance |
| NEAR-USD   | 2026-08-07 00:00:00 |     1.6521    |        -46.3333   | SHORT    | Kraken API    |
| RENDER-USD | 2026-08-07 00:00:00 |     1.345     |        -30        | SHORT    | Kraken API    |
| SKY-USD    | 2026-08-07 00:00:00 |     0.05539   |        -45.8333   | SHORT    | Kraken API    |
| SOL-USD    | 2026-08-07 00:00:00 |    72.67      |        -39.5      | SHORT    | Kraken API    |
| TLT        | 2026-08-06 00:00:00 |    82.52      |        -44.75     | SHORT    | Yahoo Finance |
| TMUS       | 2026-08-06 00:00:00 |   179.97      |        -32.75     | SHORT    | Yahoo Finance |
| TSLA       | 2026-08-06 00:00:00 |   319.53      |        -61.4167   | SHORT    | Yahoo Finance |
| UPS        | 2026-08-06 00:00:00 |   103.2       |        -46.0833   | SHORT    | Yahoo Finance |
| XLM-USD    | 2026-08-07 00:00:00 |     0.161579  |        -47.6667   | SHORT    | Kraken API    |

## Edge Summary

- Symbols with trades: **160** of 160
- Beat buy-and-hold: **29.38%** of traded symbols
- Positive return: **30.63%** of traded symbols
- Median strategy return: **-10.35%** (benchmark **14.90%**)
- Median excess vs benchmark: **-27.39%**
- Median Sharpe: **-0.11**
- Median exposure: **43.64%**

> Edge is real only if both _beat buy-and-hold_ and _median excess_ are convincingly positive across many symbols. Treat a single high-return symbol as noise.

## Portfolio Backtest

Actual capital-allocation books (not per-symbol averages). Benchmarks: `equal_weight_buyhold` (whole tracked universe), `spy_buyhold` (100% SPY), and `sixty_forty` (60% SPY / 40% AGG). `high_conf_voltarget` inverse-vol-weights the HIGH-confidence book; `conviction_long_short` is market-neutral. Judge on **Sharpe** and **max_drawdown** out-of-sample, not raw return: a fully-invested long book wins on return in a bull market but carries all the risk.

| strategy              | scope         | ann_return   | ann_vol   |   sharpe | max_drawdown   | total_return   |   avg_gross_exposure |
|:----------------------|:--------------|:-------------|:----------|---------:|:---------------|:---------------|---------------------:|
| equal_weight_buyhold  | full          | 0.63%        | 29.66%    |     0.02 | -39.63%        | -10.87%        |                 1    |
| equal_weight_buyhold  | out_of_sample | -18.27%      | 28.98%    |    -0.63 | -33.26%        | -21.25%        |                 1    |
| all_signals_ew        | full          | -15.89%      | 25.18%    |    -0.63 | -57.10%        | -43.96%        |                 1    |
| all_signals_ew        | out_of_sample | 15.41%       | 23.79%    |     0.65 | -21.09%        | 14.34%         |                 1    |
| high_conf_ew          | full          | -0.54%       | 30.93%    |    -0.02 | -40.78%        | -14.73%        |                 0.88 |
| high_conf_ew          | out_of_sample | 14.41%       | 25.61%    |     0.56 | -21.81%        | 12.50%         |                 0.88 |
| high_conf_voltarget   | full          | 2.55%        | 28.37%    |     0.09 | -33.87%        | -4.11%         |                 0.88 |
| high_conf_voltarget   | out_of_sample | 7.24%        | 22.22%    |     0.33 | -16.94%        | 5.14%          |                 0.88 |
| conviction_long_short | full          | -17.37%      | 22.76%    |    -0.76 | -46.95%        | -45.51%        |                 0.97 |
| conviction_long_short | out_of_sample | -7.03%       | 22.18%    |    -0.32 | -24.21%        | -9.60%         |                 0.97 |
| spy_buyhold           | full          | 5.50%        | 13.46%    |     0.41 | -19.51%        | 15.01%         |                 0.79 |
| spy_buyhold           | out_of_sample | 1.90%        | 10.00%    |     0.19 | -12.06%        | 1.50%          |                 0.79 |
| sixty_forty           | full          | 3.19%        | 8.52%     |     0.37 | -11.81%        | 8.97%          |                 0.79 |
| sixty_forty           | out_of_sample | -0.23%       | 6.62%     |    -0.03 | -8.26%         | -0.48%         |                 0.79 |

## Walk-Forward Robustness

Each book measured across contiguous time folds (each a different regime). A book has durable edge only if `mean_sharpe` is positive, `min_sharpe` isn't deeply negative, and `pct_positive_folds` is high — a single great fold doesn't count. `fold_sharpes` lists each fold oldest-to-newest.

| strategy              |   n_folds |   mean_sharpe |   median_sharpe |   min_sharpe | pct_positive_folds   | mean_return   | fold_sharpes                 |
|:----------------------|----------:|--------------:|----------------:|-------------:|:---------------------|:--------------|:-----------------------------|
| equal_weight_buyhold  |         5 |          0.31 |            1.15 |        -1.44 | 60.00%               | 0.26%         | 1.53;-0.93;1.15;-1.44;1.25   |
| all_signals_ew        |         5 |         -0.85 |           -0.57 |        -2.42 | 20.00%               | -9.19%        | -0.57;-0.09;-2.42;0.90;-2.09 |
| high_conf_ew          |         5 |          0.08 |            0.09 |        -0.53 | 60.00%               | -2.94%        | 0.79;-0.53;0.17;-0.14;0.09   |
| high_conf_voltarget   |         5 |          0.32 |            0.11 |        -0.26 | 60.00%               | -0.61%        | 1.50;-0.03;0.11;-0.26;0.30   |
| conviction_long_short |         5 |         -0.92 |           -1.31 |        -1.75 | 20.00%               | -11.08%       | -1.66;-1.31;0.28;-0.14;-1.75 |
| spy_buyhold           |         5 |          0.54 |            0.44 |        -1.27 | 60.00%               | 3.07%         | 1.67;-0.02;1.87;-1.27;0.44   |
| sixty_forty           |         5 |          0.47 |            0.03 |        -1.22 | 60.00%               | 1.83%         | 1.69;-0.02;1.87;-1.22;0.03   |

## Strategy Comparison

Each decision rule backtested over the same data. `out_of_sample` is the most recent ~35% of each symbol's history (unseen tail). A rule has real edge only if `median_excess` and `beat_benchmark_pct` stay positive out-of-sample, not just full-sample.

| strategy        | scope         |   symbols | beat_benchmark_pct   | positive_pct   | median_return   | median_benchmark   | median_excess   |   median_sharpe |   total_trades |
|:----------------|:--------------|----------:|:---------------------|:---------------|:----------------|:-------------------|:----------------|----------------:|---------------:|
| trend           | full          |       160 | 29.38%               | 30.63%         | -10.35%         | 14.90%             | -27.39%         |           -0.11 |          11259 |
| trend           | out_of_sample |       160 | 32.50%               | 43.75%         | -2.86%          | 6.69%              | -10.91%         |           -0.16 |           3831 |
| mean_reversion  | full          |       157 | 41.40%               | 50.96%         | 0.06%           | 14.73%             | -14.69%         |            0.04 |           1274 |
| mean_reversion  | out_of_sample |       126 | 46.83%               | 60.32%         | 0.40%           | 2.90%              | -6.04%          |            0.58 |            452 |
| regime_adaptive | full          |       160 | 31.25%               | 31.87%         | -10.57%         | 14.90%             | -27.73%         |           -0.11 |          11546 |
| regime_adaptive | out_of_sample |       160 | 33.12%               | 43.75%         | -2.56%          | 6.69%              | -10.03%         |           -0.16 |           3950 |

## Signal Calibration

Realized forward return in the signal's direction, grouped by confidence. HIGH should outrank LOW for the confidence score to be meaningful.

| confidence_level   |   horizon |     n | mean_return   | median_return   | win_rate   |
|:-------------------|----------:|------:|:--------------|:----------------|:-----------|
| HIGH               |         5 |  7756 | 0.08%         | 0.06%           | 51.15%     |
| MEDIUM             |         5 | 29085 | 0.01%         | 0.06%           | 50.62%     |
| LOW                |         5 |  3426 | -0.66%        | -0.57%          | 44.42%     |
| ALL                |         5 | 40267 | -0.03%        | 0.02%           | 50.19%     |
| HIGH               |        10 |  7704 | 0.29%         | 0.07%           | 50.77%     |
| MEDIUM             |        10 | 28869 | 0.10%         | 0.07%           | 50.52%     |
| LOW                |        10 |  3411 | -0.96%        | -0.78%          | 44.88%     |
| ALL                |        10 | 39984 | 0.05%         | 0.01%           | 50.09%     |
| HIGH               |        20 |  7639 | 0.59%         | 0.25%           | 52.05%     |
| MEDIUM             |        20 | 28457 | 0.70%         | 0.51%           | 52.86%     |
| LOW                |        20 |  3347 | -0.84%        | -0.69%          | 46.67%     |
| ALL                |        20 | 39443 | 0.55%         | 0.36%           | 52.17%     |

## Backtest Summary

### Data Quality / Signal Availability

- **ok**: 160 symbols

| symbol     |   trades | return   | benchmark_return   | mdd     |   sharpe | exposure   | skipped_reason   |
|:-----------|---------:|:---------|:-------------------|:--------|---------:|:-----------|:-----------------|
| AAPL       |       61 | 6.19%    | 80.58%             | -20.65% |     0.23 | 48.59%     | ok               |
| AAVE-USD   |       74 | -48.93%  | -56.14%            | -68.26% |    -0.49 | 37.93%     | ok               |
| ABBV       |       68 | -22.83%  | 34.59%             | -30.52% |    -0.5  | 46.09%     | ok               |
| ADA-USD    |       83 | -14.20%  | -78.74%            | -46.14% |     0.05 | 45.59%     | ok               |
| ADBE       |       68 | -27.06%  | -54.38%            | -30.14% |    -0.3  | 57.24%     | ok               |
| AGG        |       69 | -6.59%   | 0.33%              | -10.17% |    -1.07 | 33.61%     | ok               |
| ALGO-USD   |       80 | -28.14%  | -62.20%            | -41.20% |    -0.19 | 36.59%     | ok               |
| AMAT       |       71 | -35.65%  | 162.75%            | -57.08% |    -0.34 | 49.75%     | ok               |
| AMD        |       54 | 12.04%   | 161.56%            | -41.75% |     0.32 | 34.94%     | ok               |
| AMGN       |       75 | -8.57%   | 49.09%             | -34.19% |    -0.1  | 48.09%     | ok               |
| AMZN       |       81 | -53.56%  | 52.31%             | -54.61% |    -1.51 | 40.10%     | ok               |
| APT-USD    |       72 | -28.16%  | -89.16%            | -66.73% |    -0.06 | 41.76%     | ok               |
| ARB-USD    |       76 | -29.12%  | -79.39%            | -62.55% |    -0.11 | 41.95%     | ok               |
| ARKK       |       89 | -37.14%  | 55.38%             | -38.58% |    -0.66 | 41.10%     | ok               |
| ATOM-USD   |       88 | -68.01%  | -67.50%            | -73.98% |    -1.12 | 46.55%     | ok               |
| AVAX-USD   |       77 | -52.93%  | -67.81%            | -61.58% |    -0.65 | 38.51%     | ok               |
| AVGO       |       60 | 27.80%   | 233.18%            | -35.76% |     0.47 | 40.60%     | ok               |
| BA         |       69 | -5.74%   | 28.18%             | -30.56% |     0.03 | 48.09%     | ok               |
| BAC        |       78 | -5.10%   | 76.52%             | -27.64% |    -0.05 | 50.92%     | ok               |
| BCH-USD    |       76 | 5.55%    | -33.42%            | -54.26% |     0.27 | 50.57%     | ok               |
| BITO       |       80 | -23.62%  | -72.62%            | -39.47% |    -0.17 | 38.94%     | ok               |
| BLK        |       79 | -6.19%   | 39.63%             | -26.90% |    -0.1  | 44.93%     | ok               |
| BND        |       67 | -7.33%   | 0.26%              | -9.98%  |    -1.15 | 35.11%     | ok               |
| BONK-USD   |       68 | 47.58%   | -75.22%            | -51.50% |     0.61 | 42.53%     | ok               |
| BTC-USD    |       72 | 8.49%    | -26.27%            | -23.38% |     0.28 | 51.72%     | ok               |
| C          |       81 | -31.90%  | 134.40%            | -39.51% |    -0.64 | 50.42%     | ok               |
| CAT        |       72 | 15.38%   | 150.63%            | -21.02% |     0.36 | 53.41%     | ok               |
| CL         |       62 | 5.04%    | 5.26%              | -14.32% |     0.23 | 43.43%     | ok               |
| CMCSA      |       80 | -44.68%  | -37.28%            | -48.28% |    -1.2  | 41.76%     | ok               |
| COMP-USD   |       95 | -36.96%  | -66.80%            | -54.23% |    -0.21 | 46.93%     | ok               |
| COP        |       72 | -20.92%  | -2.52%             | -43.96% |    -0.34 | 44.26%     | ok               |
| COST       |       56 | 2.10%    | 29.67%             | -29.73% |     0.13 | 41.43%     | ok               |
| CRM        |       63 | -40.74%  | -38.42%            | -42.51% |    -0.87 | 42.60%     | ok               |
| CRV-USD    |       70 | -0.17%   | -48.33%            | -39.89% |     0.23 | 36.59%     | ok               |
| CSCO       |       59 | 23.34%   | 142.78%            | -21.79% |     0.51 | 47.75%     | ok               |
| CVX        |       71 | -12.51%  | 21.54%             | -29.13% |    -0.28 | 40.77%     | ok               |
| DASH-USD   |       63 | -41.84%  | 28.82%             | -64.43% |    -0.02 | 30.27%     | ok               |
| DBC        |       60 | -13.20%  | 27.25%             | -25.15% |    -0.42 | 35.77%     | ok               |
| DE         |       72 | -4.52%   | 61.70%             | -24.77% |     0    | 44.93%     | ok               |
| DIA        |       60 | -3.93%   | 37.97%             | -12.94% |    -0.18 | 43.59%     | ok               |
| DIS        |       64 | -18.32%  | -6.59%             | -28.17% |    -0.33 | 43.26%     | ok               |
| DOGE-USD   |       70 | -12.05%  | -65.19%            | -62.31% |     0.13 | 48.47%     | ok               |
| DOT-USD    |       88 | -63.03%  | -81.02%            | -67.64% |    -0.74 | 48.08%     | ok               |
| DXY-INDEX  |       42 | -1.69%   | -2.48%             | -6.29%  |    -0.25 | 32.68%     | ok               |
| EEM        |       64 | -12.63%  | 58.51%             | -25.67% |    -0.37 | 40.93%     | ok               |
| EFA        |       58 | -10.12%  | 36.14%             | -13.53% |    -0.39 | 41.26%     | ok               |
| EOG        |       81 | -25.30%  | 10.03%             | -48.13% |    -0.5  | 49.42%     | ok               |
| ETC-USD    |       62 | -31.66%  | -65.70%            | -48.09% |    -0.43 | 28.93%     | ok               |
| ETH-USD    |       60 | 180.36%  | -12.42%            | -30.11% |     1.39 | 45.59%     | ok               |
| EWJ        |       62 | -19.66%  | 37.78%             | -30.73% |    -0.66 | 36.44%     | ok               |
| FCX        |       67 | -29.92%  | 57.39%             | -48.22% |    -0.35 | 45.92%     | ok               |
| FET-USD    |       83 | -43.54%  | -77.02%            | -52.44% |    -0.23 | 41.19%     | ok               |
| FIL-USD    |       68 | -44.63%  | -76.83%            | -48.59% |    -0.54 | 34.10%     | ok               |
| FXI        |       44 | -2.18%   | 48.92%             | -23.91% |     0.03 | 31.11%     | ok               |
| GDX        |       58 | 7.61%    | 180.76%            | -34.99% |     0.25 | 46.42%     | ok               |
| GDXJ       |       64 | -24.86%  | 199.81%            | -44.93% |    -0.25 | 44.59%     | ok               |
| GE         |       80 | 2.71%    | 181.45%            | -27.82% |     0.17 | 51.41%     | ok               |
| GLD        |       50 | 22.55%   | 94.49%             | -16.63% |     0.58 | 47.09%     | ok               |
| GOOGL      |       55 | 78.89%   | 150.00%            | -20.41% |     1.18 | 52.25%     | ok               |
| GRT-USD    |       81 | 5.02%    | -86.41%            | -50.20% |     0.27 | 43.68%     | ok               |
| GS         |       74 | -0.65%   | 165.71%            | -22.13% |     0.09 | 50.42%     | ok               |
| HD         |       71 | -6.99%   | -6.86%             | -17.69% |    -0.11 | 43.59%     | ok               |
| HON        |       93 | -26.66%  | 24.04%             | -29.92% |    -0.71 | 52.41%     | ok               |
| HYG        |       83 | -9.49%   | 3.03%              | -10.00% |    -1.11 | 34.61%     | ok               |
| IBIT       |       34 | 30.82%   | -4.00%             | -18.95% |     0.65 | 31.01%     | ok               |
| IBM        |       75 | -28.39%  | 20.68%             | -48.94% |    -0.37 | 51.08%     | ok               |
| ICP-USD    |       77 | -10.52%  | -65.48%            | -50.29% |     0.15 | 34.67%     | ok               |
| IEF        |       82 | -11.01%  | -0.92%             | -11.84% |    -1.55 | 33.61%     | ok               |
| IEMG       |       60 | -10.62%  | 54.24%             | -26.84% |    -0.31 | 40.43%     | ok               |
| INJ-USD    |       75 | -52.79%  | -59.44%            | -76.24% |    -0.5  | 38.12%     | ok               |
| INTC       |       66 | 56.43%   | 133.47%            | -60.60% |     0.62 | 48.75%     | ok               |
| INTU       |       69 | -16.81%  | -50.48%            | -41.36% |    -0.17 | 42.26%     | ok               |
| ITA        |       74 | -3.58%   | 97.20%             | -23.75% |    -0.03 | 46.26%     | ok               |
| IWM        |       50 | 11.84%   | 47.63%             | -12.83% |     0.47 | 35.77%     | ok               |
| JNJ        |       68 | 6.34%    | 61.41%             | -17.51% |     0.27 | 49.75%     | ok               |
| JPM        |       75 | -22.64%  | 89.55%             | -33.16% |    -0.57 | 51.41%     | ok               |
| KO         |       51 | 23.75%   | 43.55%             | -8.20%  |     0.85 | 37.94%     | ok               |
| LDO-USD    |       80 | 30.28%   | -73.34%            | -61.16% |     0.51 | 43.68%     | ok               |
| LIN        |       68 | -12.48%  | 3.41%              | -20.61% |    -0.41 | 36.94%     | ok               |
| LINK-USD   |       71 | 0.89%    | -44.86%            | -40.80% |     0.24 | 43.49%     | ok               |
| LLY        |       67 | -25.22%  | 56.68%             | -53.34% |    -0.35 | 47.42%     | ok               |
| LRCX       |       82 | -23.96%  | 230.32%            | -61.08% |    -0.14 | 42.26%     | ok               |
| LTC-USD    |       70 | -20.59%  | -56.07%            | -38.94% |    -0.1  | 49.81%     | ok               |
| MCD        |       77 | -2.74%   | -1.94%             | -18.81% |    -0.06 | 38.44%     | ok               |
| META       |       76 | -35.66%  | 19.94%             | -42.43% |    -0.65 | 47.42%     | ok               |
| MPC        |       67 | -11.83%  | 58.35%             | -44.76% |    -0.09 | 49.75%     | ok               |
| MRK        |       67 | -27.34%  | 6.52%              | -35.95% |    -0.63 | 43.59%     | ok               |
| MS         |       77 | -10.18%  | 139.90%            | -27.79% |    -0.16 | 49.58%     | ok               |
| MSFT       |       83 | -31.74%  | 17.55%             | -38.06% |    -0.77 | 47.59%     | ok               |
| MU         |       51 | 236.53%  | 864.09%            | -68.76% |     1.26 | 57.74%     | ok               |
| NEAR-USD   |       83 | 8.37%    | -41.27%            | -59.54% |     0.33 | 40.61%     | ok               |
| NEM        |       70 | -20.55%  | 208.18%            | -38.49% |    -0.15 | 52.75%     | ok               |
| NFLX       |       72 | 18.99%   | 20.21%             | -21.09% |     0.47 | 52.75%     | ok               |
| NKE        |       83 | -36.59%  | -58.11%            | -55.35% |    -0.5  | 44.26%     | ok               |
| NOW        |       82 | 1.23%    | -24.73%            | -26.78% |     0.18 | 46.09%     | ok               |
| NVDA       |       71 | -26.95%  | 143.65%            | -45.14% |    -0.2  | 58.65%     | ok               |
| OP-USD     |       66 | -15.92%  | -90.71%            | -71.26% |     0.07 | 35.25%     | ok               |
| ORCL       |       66 | 101.38%  | 14.29%             | -30.61% |     0.88 | 56.07%     | ok               |
| OXY        |       71 | -4.45%   | -10.45%            | -34.15% |     0.05 | 46.76%     | ok               |
| PEP        |       75 | -5.83%   | -15.98%            | -21.35% |    -0.11 | 47.92%     | ok               |
| PEPE-USD   |       81 | -8.77%   | -59.90%            | -57.66% |     0.2  | 45.98%     | ok               |
| PFE        |       83 | -40.56%  | -6.86%             | -43.15% |    -1.29 | 36.77%     | ok               |
| PG         |       65 | -19.43%  | -9.00%             | -23.92% |    -0.74 | 37.27%     | ok               |
| PM         |       83 | -5.75%   | 100.16%            | -34.97% |    -0.03 | 55.91%     | ok               |
| POL-USD    |       79 | 55.83%   | -69.84%            | -41.08% |     0.73 | 49.43%     | ok               |
| QCOM       |       77 | -22.75%  | -4.78%             | -56.59% |    -0.16 | 45.59%     | ok               |
| QQQ        |       64 | 15.44%   | 62.74%             | -13.49% |     0.47 | 44.09%     | ok               |
| RENDER-USD |       98 | -13.08%  | -61.87%            | -45.62% |     0.14 | 42.15%     | ok               |
| RTX        |       54 | 45.58%   | 143.30%            | -16.99% |     0.95 | 54.08%     | ok               |
| SBUX       |       62 | -19.04%  | 14.73%             | -29.22% |    -0.35 | 39.93%     | ok               |
| SCHW       |       76 | -6.97%   | 61.65%             | -31.92% |    -0.08 | 48.92%     | ok               |
| SHIB-USD   |       76 | -34.77%  | -64.13%            | -47.96% |    -0.31 | 52.30%     | ok               |
| SHY        |       46 | -2.23%   | 0.32%              | -2.85%  |    -0.78 | 34.11%     | ok               |
| SKY-USD    |       76 | -31.42%  | -4.22%             | -47.82% |    -0.38 | 42.65%     | ok               |
| SLB        |       79 | -30.75%  | -3.17%             | -54.23% |    -0.57 | 50.58%     | ok               |
| SLV        |       62 | 40.86%   | 145.71%            | -42.66% |     0.61 | 43.43%     | ok               |
| SMH        |       48 | 69.30%   | 160.40%            | -33.66% |     1.01 | 45.59%     | ok               |
| SNX-USD    |       64 | -2.74%   | -77.08%            | -38.68% |     0.21 | 37.36%     | ok               |
| SOL-USD    |       72 | -28.53%  | -49.80%            | -46.86% |    -0.09 | 59.58%     | ok               |
| SOXX       |       56 | 68.98%   | 141.68%            | -40.14% |     0.95 | 44.09%     | ok               |
| SPY        |       62 | 1.09%    | 49.25%             | -16.47% |     0.1  | 48.75%     | ok               |
| SUSHI-USD  |      104 | -83.70%  | -76.79%            | -86.73% |    -1.37 | 38.31%     | ok               |
| T          |       64 | 32.87%   | 39.39%             | -17.01% |     0.75 | 54.41%     | ok               |
| TGT        |       62 | -17.61%  | -10.49%            | -40.57% |    -0.35 | 37.27%     | ok               |
| TIA-USD    |       89 | -40.67%  | -90.17%            | -68.36% |    -0.24 | 38.89%     | ok               |
| TLT        |       70 | -18.55%  | -11.24%            | -21.87% |    -1.37 | 34.11%     | ok               |
| TMO        |       61 | 29.61%   | -0.84%             | -18.85% |     0.62 | 52.41%     | ok               |
| TMUS       |       70 | 2.49%    | 10.51%             | -27.01% |     0.15 | 46.92%     | ok               |
| TRX-USD    |       70 | 9.99%    | 35.24%             | -22.90% |     0.35 | 48.47%     | ok               |
| TSLA       |       76 | -33.35%  | 96.63%             | -59.64% |    -0.2  | 42.76%     | ok               |
| TXN        |       71 | -14.73%  | 62.67%             | -46.98% |    -0.08 | 50.58%     | ok               |
| UNH        |       74 | 29.76%   | -17.39%            | -26.96% |     0.52 | 51.75%     | ok               |
| UNI-USD    |       92 | -74.70%  | -43.09%            | -80.33% |    -0.95 | 45.98%     | ok               |
| UPS        |       72 | -41.93%  | -32.94%            | -43.16% |    -0.87 | 40.27%     | ok               |
| USO        |       70 | 0.23%    | 55.79%             | -43.35% |     0.14 | 34.28%     | ok               |
| VEA        |       58 | -3.12%   | 44.88%             | -18.85% |    -0.08 | 41.93%     | ok               |
| VIXY       |       96 | -80.31%  | -64.70%            | -88.36% |    -1.02 | 31.95%     | ok               |
| VNQ        |       73 | -17.51%  | 14.83%             | -24.92% |    -0.74 | 37.94%     | ok               |
| VTI        |       70 | -5.54%   | 48.53%             | -18.77% |    -0.14 | 49.25%     | ok               |
| VWO        |       80 | -16.62%  | 43.58%             | -25.20% |    -0.61 | 41.76%     | ok               |
| VZ         |       83 | -25.59%  | 18.15%             | -26.98% |    -0.82 | 38.77%     | ok               |
| WFC        |       84 | -20.37%  | 52.68%             | -29.78% |    -0.36 | 48.92%     | ok               |
| WIF-USD    |       72 | -52.90%  | -75.63%            | -61.76% |    -0.39 | 33.91%     | ok               |
| WMT        |       65 | 9.49%    | 83.66%             | -21.31% |     0.33 | 48.59%     | ok               |
| XBI        |       66 | -1.61%   | 63.58%             | -18.30% |     0.04 | 39.27%     | ok               |
| XLB        |       62 | -11.48%  | 14.96%             | -24.41% |    -0.39 | 34.78%     | ok               |
| XLC        |       65 | 14.08%   | 38.82%             | -12.33% |     0.51 | 52.58%     | ok               |
| XLE        |       75 | -12.90%  | 27.42%             | -37.76% |    -0.26 | 45.42%     | ok               |
| XLF        |       78 | -11.53%  | 41.59%             | -23.61% |    -0.37 | 47.42%     | ok               |
| XLI        |       72 | -5.90%   | 51.42%             | -14.12% |    -0.19 | 42.76%     | ok               |
| XLK        |       42 | 64.39%   | 77.54%             | -14.75% |     1.2  | 45.92%     | ok               |
| XLM-USD    |       67 | 7.13%    | -45.22%            | -50.48% |     0.29 | 45.40%     | ok               |
| XLP        |       66 | 8.96%    | 12.64%             | -8.96%  |     0.54 | 40.60%     | ok               |
| XLU        |       67 | -5.24%   | 36.91%             | -20.40% |    -0.19 | 39.10%     | ok               |
| XLV        |       66 | -15.44%  | 12.68%             | -19.17% |    -0.77 | 34.28%     | ok               |
| XLY        |       66 | 4.16%    | 31.34%             | -14.01% |     0.19 | 43.59%     | ok               |
| XOM        |       55 | 5.77%    | 38.91%             | -20.29% |     0.23 | 37.94%     | ok               |
| XRP-USD    |       52 | -5.00%   | -58.05%            | -33.91% |     0.11 | 32.95%     | ok               |
| YFI-USD    |       81 | -64.19%  | -61.41%            | -71.12% |    -1.03 | 40.61%     | ok               |
| ZEC-USD    |       66 | 36.98%   | 1344.17%           | -50.37% |     0.52 | 37.55%     | ok               |

## AAPL Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 14.49%   | 80.58%             | -21.71% |     0.37 |       68 | 52.75%     | ok               |
|          15 | 11.44%   | 80.58%             | -23.86% |     0.32 |       77 | 60.07%     | ok               |
|          30 | 6.19%    | 80.58%             | -20.65% |     0.23 |       61 | 48.59%     | ok               |
|          25 | 3.98%    | 80.58%             | -20.03% |     0.19 |       67 | 50.42%     | ok               |
|          35 | 3.81%    | 80.58%             | -22.04% |     0.18 |       61 | 47.09%     | ok               |

## AAVE-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 11.46%   | -56.14%            | -43.61% |     0.33 |       40 | 30.65%     | ok               |
|          45 | -2.33%   | -56.14%            | -49.19% |     0.16 |       42 | 26.05%     | ok               |
|          35 | -7.60%   | -56.14%            | -51.96% |     0.12 |       50 | 33.91%     | ok               |
|          50 | -25.64%  | -56.14%            | -45.07% |    -0.24 |       40 | 19.16%     | ok               |
|          15 | -46.46%  | -56.14%            | -61.76% |    -0.29 |       79 | 52.30%     | ok               |

## ABBV Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -11.70%  | 34.59%             | -26.55% |    -0.23 |       50 | 34.44%     | ok               |
|          25 | -22.92%  | 34.59%             | -30.41% |    -0.5  |       67 | 47.92%     | ok               |
|          30 | -22.83%  | 34.59%             | -30.52% |    -0.5  |       68 | 46.09%     | ok               |
|          20 | -23.51%  | 34.59%             | -29.62% |    -0.5  |       67 | 49.75%     | ok               |
|          40 | -21.97%  | 34.59%             | -26.61% |    -0.52 |       66 | 38.94%     | ok               |

## ADA-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 6.88%    | -78.74%            | -35.54% |     0.27 |       56 | 26.82%     | ok               |
|          45 | -1.16%   | -78.74%            | -39.95% |     0.19 |       57 | 31.03%     | ok               |
|          35 | -12.89%  | -78.74%            | -49.56% |     0.07 |       75 | 41.57%     | ok               |
|          30 | -14.20%  | -78.74%            | -46.14% |     0.05 |       83 | 45.59%     | ok               |
|          40 | -13.62%  | -78.74%            | -48.50% |     0.04 |       73 | 36.59%     | ok               |

## ADBE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 5.44%    | -54.38%            | -21.57% |     0.21 |       74 | 49.08%     | ok               |
|          40 | -11.30%  | -54.38%            | -27.85% |    -0.09 |       70 | 41.76%     | ok               |
|          25 | -16.19%  | -54.38%            | -28.72% |    -0.1  |       50 | 61.06%     | ok               |
|          20 | -24.60%  | -54.38%            | -31.52% |    -0.23 |       54 | 64.06%     | ok               |
|          30 | -27.06%  | -54.38%            | -30.14% |    -0.3  |       68 | 57.24%     | ok               |

## AGG Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -6.59%   | 0.33%              | -10.17% |    -1.07 |       69 | 33.61%     | ok               |
|          50 | -5.20%   | 0.33%              | -7.92%  |    -1.14 |       52 | 18.14%     | ok               |
|          20 | -7.92%   | 0.33%              | -11.30% |    -1.14 |       71 | 38.94%     | ok               |
|          25 | -8.10%   | 0.33%              | -11.94% |    -1.22 |       71 | 37.27%     | ok               |
|          45 | -6.24%   | 0.33%              | -8.23%  |    -1.22 |       58 | 22.80%     | ok               |

## ALGO-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -28.14%  | -62.20%            | -41.20% |    -0.19 |       80 | 36.59%     | ok               |
|          35 | -35.82%  | -62.20%            | -43.45% |    -0.41 |       58 | 30.08%     | ok               |
|          25 | -45.80%  | -62.20%            | -60.86% |    -0.46 |       78 | 43.10%     | ok               |
|          15 | -48.78%  | -62.20%            | -54.77% |    -0.47 |       82 | 48.66%     | ok               |
|          20 | -51.02%  | -62.20%            | -56.96% |    -0.53 |       82 | 46.17%     | ok               |

## AMAT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -24.72%  | 162.75%            | -53.90% |    -0.12 |       70 | 58.57%     | ok               |
|          30 | -35.65%  | 162.75%            | -57.08% |    -0.34 |       71 | 49.75%     | ok               |
|          35 | -35.38%  | 162.75%            | -54.63% |    -0.35 |       71 | 47.25%     | ok               |
|          50 | -33.14%  | 162.75%            | -47.29% |    -0.35 |       48 | 35.27%     | ok               |
|          40 | -39.02%  | 162.75%            | -55.84% |    -0.44 |       67 | 42.43%     | ok               |

## AMD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 12.42%   | 161.56%            | -41.14% |     0.32 |       56 | 29.62%     | ok               |
|          40 | 12.04%   | 161.56%            | -41.75% |     0.32 |       54 | 34.94%     | ok               |
|          35 | 4.42%    | 161.56%            | -46.50% |     0.25 |       62 | 36.61%     | ok               |
|          30 | -5.98%   | 161.56%            | -51.00% |     0.16 |       67 | 39.10%     | ok               |
|          25 | -10.81%  | 161.56%            | -55.79% |     0.11 |       67 | 41.60%     | ok               |

## AMGN Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | -2.01%   | 49.09%             | -31.29% |     0.05 |       67 | 44.09%     | ok               |
|          20 | -4.64%   | 49.09%             | -26.65% |     0    |       74 | 54.08%     | ok               |
|          15 | -5.79%   | 49.09%             | -27.98% |    -0.02 |       67 | 58.57%     | ok               |
|          30 | -8.57%   | 49.09%             | -34.19% |    -0.1  |       75 | 48.09%     | ok               |
|          25 | -11.08%  | 49.09%             | -33.47% |    -0.15 |       69 | 50.42%     | ok               |

## AMZN Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -23.27%  | 52.31%             | -28.96% |    -0.69 |       56 | 30.12%     | ok               |
|          50 | -26.15%  | 52.31%             | -34.08% |    -0.92 |       50 | 23.29%     | ok               |
|          45 | -33.38%  | 52.31%             | -35.71% |    -1.17 |       58 | 26.62%     | ok               |
|          35 | -48.19%  | 52.31%             | -49.36% |    -1.38 |       71 | 34.11%     | ok               |
|          30 | -53.56%  | 52.31%             | -54.61% |    -1.51 |       81 | 40.10%     | ok               |

## APT-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 19.10%   | -89.16%            | -46.73% |     0.42 |       40 | 18.97%     | ok               |
|          45 | -11.65%  | -89.16%            | -63.86% |     0.05 |       56 | 24.52%     | ok               |
|          35 | -17.11%  | -89.16%            | -60.63% |     0.04 |       66 | 35.25%     | ok               |
|          20 | -24.12%  | -89.16%            | -68.18% |     0.01 |       71 | 50.19%     | ok               |
|          25 | -28.42%  | -89.16%            | -68.00% |    -0.05 |       68 | 45.79%     | ok               |

## ARB-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 39.10%   | -79.39%            | -51.09% |     0.56 |       86 | 58.24%     | ok               |
|          20 | 6.93%    | -79.39%            | -58.28% |     0.34 |       72 | 52.11%     | ok               |
|          25 | -10.23%  | -79.39%            | -55.53% |     0.18 |       74 | 47.89%     | ok               |
|          40 | -10.08%  | -79.39%            | -48.16% |     0.11 |       60 | 31.42%     | ok               |
|          45 | -10.55%  | -79.39%            | -51.09% |     0.08 |       62 | 24.33%     | ok               |

## ARKK Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -32.31%  | 55.38%             | -37.76% |    -0.43 |       94 | 52.41%     | ok               |
|          20 | -35.78%  | 55.38%             | -37.99% |    -0.54 |       91 | 48.09%     | ok               |
|          30 | -37.14%  | 55.38%             | -38.58% |    -0.66 |       89 | 41.10%     | ok               |
|          35 | -39.25%  | 55.38%             | -40.65% |    -0.76 |       88 | 38.44%     | ok               |
|          40 | -40.53%  | 55.38%             | -41.90% |    -0.84 |       80 | 33.61%     | ok               |

## ATOM-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -60.55%  | -67.50%            | -69.46% |    -0.75 |       83 | 62.64%     | ok               |
|          25 | -64.73%  | -67.50%            | -71.09% |    -0.94 |       93 | 53.26%     | ok               |
|          20 | -68.31%  | -67.50%            | -74.75% |    -1.03 |       93 | 56.51%     | ok               |
|          30 | -68.01%  | -67.50%            | -73.98% |    -1.12 |       88 | 46.55%     | ok               |
|          45 | -61.80%  | -67.50%            | -67.66% |    -1.14 |       74 | 31.42%     | ok               |

## AVAX-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -5.68%   | -67.81%            | -40.19% |     0.08 |       34 | 18.39%     | ok               |
|          40 | -14.36%  | -67.81%            | -47.33% |    -0.05 |       38 | 24.90%     | ok               |
|          45 | -17.71%  | -67.81%            | -47.25% |    -0.12 |       34 | 22.22%     | ok               |
|          15 | -32.68%  | -67.81%            | -43.71% |    -0.15 |       75 | 52.49%     | ok               |
|          35 | -27.85%  | -67.81%            | -48.89% |    -0.22 |       56 | 30.27%     | ok               |

## AVGO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 27.80%   | 233.18%            | -35.76% |     0.47 |       60 | 40.60%     | ok               |
|          25 | 25.11%   | 233.18%            | -38.01% |     0.44 |       68 | 42.10%     | ok               |
|          50 | 24.25%   | 233.18%            | -36.86% |     0.44 |       52 | 29.45%     | ok               |
|          40 | 24.20%   | 233.18%            | -40.70% |     0.44 |       58 | 34.28%     | ok               |
|          35 | 19.66%   | 233.18%            | -36.19% |     0.39 |       68 | 37.60%     | ok               |

## BA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 19.77%   | 28.18%             | -13.34% |     0.54 |       44 | 31.28%     | ok               |
|          35 | 15.81%   | 28.18%             | -23.77% |     0.38 |       72 | 43.93%     | ok               |
|          40 | 9.45%    | 28.18%             | -23.90% |     0.29 |       48 | 38.27%     | ok               |
|          25 | -3.12%   | 28.18%             | -32.48% |     0.08 |       72 | 51.41%     | ok               |
|          30 | -5.74%   | 28.18%             | -30.56% |     0.03 |       69 | 48.09%     | ok               |

## BAC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 1.15%    | 76.52%             | -21.48% |     0.12 |       80 | 55.57%     | ok               |
|          45 | 0.78%    | 76.52%             | -21.87% |     0.09 |       64 | 38.27%     | ok               |
|          35 | -0.06%   | 76.52%             | -29.13% |     0.07 |       70 | 47.09%     | ok               |
|          50 | -2.02%   | 76.52%             | -20.35% |    -0    |       62 | 34.44%     | ok               |
|          15 | -4.39%   | 76.52%             | -23.58% |    -0.01 |       82 | 60.23%     | ok               |

## BCH-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 7.13%    | -33.42%            | -45.51% |     0.31 |       72 | 59.77%     | ok               |
|          30 | 5.55%    | -33.42%            | -54.26% |     0.27 |       76 | 50.57%     | ok               |
|          20 | -3.14%   | -33.42%            | -45.82% |     0.21 |       68 | 56.32%     | ok               |
|          25 | -17.83%  | -33.42%            | -51.09% |     0.03 |       71 | 52.87%     | ok               |
|          35 | -17.01%  | -33.42%            | -64.58% |    -0.01 |       72 | 46.74%     | ok               |

## BITO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -6.98%   | -72.62%            | -31.98% |     0.03 |       54 | 22.30%     | ok               |
|          30 | -23.62%  | -72.62%            | -39.47% |    -0.17 |       80 | 38.94%     | ok               |
|          15 | -29.25%  | -72.62%            | -48.38% |    -0.18 |       89 | 47.92%     | ok               |
|          45 | -21.74%  | -72.62%            | -37.50% |    -0.21 |       62 | 25.96%     | ok               |
|          40 | -25.24%  | -72.62%            | -40.17% |    -0.24 |       66 | 30.78%     | ok               |

## BLK Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 1.38%    | 39.63%             | -21.48% |     0.12 |       80 | 49.58%     | ok               |
|          35 | 0.10%    | 39.63%             | -20.79% |     0.07 |       86 | 41.10%     | ok               |
|          40 | -1.80%   | 39.63%             | -22.83% |     0.01 |       78 | 36.77%     | ok               |
|          25 | -3.69%   | 39.63%             | -24.62% |    -0.02 |       75 | 47.59%     | ok               |
|          30 | -6.19%   | 39.63%             | -26.90% |    -0.1  |       79 | 44.93%     | ok               |

## BND Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -6.22%   | 0.26%              | -9.43%  |    -0.89 |       64 | 40.60%     | ok               |
|          25 | -6.92%   | 0.26%              | -10.55% |    -1.03 |       67 | 38.60%     | ok               |
|          30 | -7.33%   | 0.26%              | -9.98%  |    -1.15 |       67 | 35.11%     | ok               |
|          15 | -8.49%   | 0.26%              | -11.30% |    -1.2  |       76 | 43.43%     | ok               |
|          45 | -7.99%   | 0.26%              | -9.84%  |    -1.51 |       56 | 24.29%     | ok               |

## BONK-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 165.22%  | -75.22%            | -35.57% |     1.21 |       48 | 22.41%     | ok               |
|          25 | 140.14%  | -75.22%            | -54.47% |     0.96 |       65 | 48.47%     | ok               |
|          15 | 128.37%  | -75.22%            | -62.48% |     0.9  |       70 | 57.09%     | ok               |
|          45 | 92.16%   | -75.22%            | -47.53% |     0.87 |       62 | 27.59%     | ok               |
|          20 | 109.90%  | -75.22%            | -61.03% |     0.86 |       65 | 52.68%     | ok               |

## BTC-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 59.43%   | -26.27%            | -14.50% |     1.05 |       42 | 33.72%     | ok               |
|          45 | 44.99%   | -26.27%            | -13.36% |     0.87 |       40 | 30.27%     | ok               |
|          35 | 42.81%   | -26.27%            | -21.56% |     0.79 |       66 | 40.61%     | ok               |
|          30 | 25.66%   | -26.27%            | -21.75% |     0.53 |       70 | 47.32%     | ok               |
|          50 | 14.00%   | -26.27%            | -18.05% |     0.4  |       42 | 25.29%     | ok               |

## C Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -7.33%   | 134.40%            | -21.64% |    -0.13 |       66 | 35.27%     | ok               |
|          45 | -19.47%  | 134.40%            | -29.73% |    -0.46 |       78 | 39.43%     | ok               |
|          25 | -28.45%  | 134.40%            | -36.44% |    -0.54 |       73 | 52.25%     | ok               |
|          40 | -25.11%  | 134.40%            | -34.65% |    -0.58 |       78 | 41.76%     | ok               |
|          20 | -30.85%  | 134.40%            | -37.77% |    -0.59 |       81 | 55.24%     | ok               |

## CAT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 15.38%   | 150.63%            | -21.02% |     0.36 |       72 | 53.41%     | ok               |
|          25 | 15.49%   | 150.63%            | -26.37% |     0.36 |       68 | 56.24%     | ok               |
|          45 | 10.67%   | 150.63%            | -27.12% |     0.3  |       56 | 42.10%     | ok               |
|          20 | 10.19%   | 150.63%            | -25.65% |     0.29 |       80 | 59.90%     | ok               |
|          15 | 9.88%    | 150.63%            | -30.60% |     0.28 |       75 | 67.05%     | ok               |

## CL Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 5.50%    | 5.26%              | -12.98% |     0.27 |       44 | 27.45%     | ok               |
|          30 | 5.04%    | 5.26%              | -14.32% |     0.23 |       62 | 43.43%     | ok               |
|          45 | 0.68%    | 5.26%              | -13.51% |     0.08 |       48 | 30.45%     | ok               |
|          35 | 0.05%    | 5.26%              | -13.83% |     0.06 |       64 | 39.77%     | ok               |
|          40 | -2.86%   | 5.26%              | -12.70% |    -0.05 |       58 | 34.44%     | ok               |

## CMCSA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -41.75%  | -37.28%            | -45.44% |    -0.95 |       90 | 56.24%     | ok               |
|          30 | -44.68%  | -37.28%            | -48.28% |    -1.2  |       80 | 41.76%     | ok               |
|          50 | -30.32%  | -37.28%            | -33.19% |    -1.2  |       46 | 13.31%     | ok               |
|          25 | -46.42%  | -37.28%            | -49.81% |    -1.24 |       89 | 46.92%     | ok               |
|          35 | -44.83%  | -37.28%            | -48.11% |    -1.3  |       93 | 36.11%     | ok               |

## COMP-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -6.30%   | -66.80%            | -38.71% |     0.11 |       48 | 20.88%     | ok               |
|          30 | -36.96%  | -66.80%            | -54.23% |    -0.21 |       95 | 46.93%     | ok               |
|          25 | -40.55%  | -66.80%            | -57.94% |    -0.23 |       95 | 54.60%     | ok               |
|          15 | -52.25%  | -66.80%            | -64.08% |    -0.41 |      105 | 64.94%     | ok               |
|          40 | -45.52%  | -66.80%            | -50.85% |    -0.46 |       72 | 34.67%     | ok               |

## COP Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -3.67%   | -2.52%             | -35.08% |     0.01 |       48 | 30.12%     | ok               |
|          35 | -16.59%  | -2.52%             | -43.58% |    -0.25 |       73 | 40.77%     | ok               |
|          45 | -15.05%  | -2.52%             | -41.35% |    -0.26 |       62 | 33.44%     | ok               |
|          30 | -20.92%  | -2.52%             | -43.96% |    -0.34 |       72 | 44.26%     | ok               |
|          40 | -20.42%  | -2.52%             | -47.05% |    -0.39 |       68 | 36.61%     | ok               |

## COST Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 12.78%   | 29.67%             | -24.32% |     0.43 |       62 | 47.59%     | ok               |
|          25 | 11.11%   | 29.67%             | -24.73% |     0.39 |       59 | 44.76%     | ok               |
|          35 | 6.54%    | 29.67%             | -26.58% |     0.28 |       52 | 38.60%     | ok               |
|          30 | 2.10%    | 29.67%             | -29.73% |     0.13 |       56 | 41.43%     | ok               |
|          15 | -1.95%   | 29.67%             | -27.30% |     0.02 |       65 | 51.08%     | ok               |

## CRM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -36.98%  | -38.42%            | -44.67% |    -0.59 |       90 | 55.24%     | ok               |
|          35 | -31.01%  | -38.42%            | -34.39% |    -0.63 |       60 | 37.77%     | ok               |
|          40 | -36.11%  | -38.42%            | -40.30% |    -0.84 |       66 | 33.78%     | ok               |
|          20 | -44.40%  | -38.42%            | -46.70% |    -0.85 |       74 | 48.92%     | ok               |
|          30 | -40.74%  | -38.42%            | -42.51% |    -0.87 |       63 | 42.60%     | ok               |

## CRV-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 27.72%   | -48.33%            | -37.78% |     0.48 |       70 | 31.80%     | ok               |
|          45 | 12.07%   | -48.33%            | -42.29% |     0.33 |       56 | 21.07%     | ok               |
|          50 | 7.86%    | -48.33%            | -29.30% |     0.28 |       46 | 17.43%     | ok               |
|          40 | 5.82%    | -48.33%            | -38.86% |     0.27 |       60 | 27.39%     | ok               |
|          30 | -0.17%   | -48.33%            | -39.89% |     0.23 |       70 | 36.59%     | ok               |

## CSCO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 35.16%   | 142.78%            | -19.34% |     0.75 |       48 | 36.61%     | ok               |
|          45 | 30.59%   | 142.78%            | -19.34% |     0.66 |       49 | 38.27%     | ok               |
|          35 | 25.61%   | 142.78%            | -23.68% |     0.55 |       51 | 45.09%     | ok               |
|          25 | 24.55%   | 142.78%            | -23.28% |     0.53 |       61 | 49.58%     | ok               |
|          30 | 23.34%   | 142.78%            | -21.79% |     0.51 |       59 | 47.75%     | ok               |

## CVX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -7.98%   | 21.54%             | -24.33% |    -0.13 |       71 | 43.26%     | ok               |
|          40 | -8.51%   | 21.54%             | -27.34% |    -0.18 |       73 | 35.94%     | ok               |
|          45 | -8.52%   | 21.54%             | -28.83% |    -0.19 |       63 | 32.28%     | ok               |
|          35 | -10.63%  | 21.54%             | -28.85% |    -0.23 |       65 | 38.10%     | ok               |
|          30 | -12.51%  | 21.54%             | -29.13% |    -0.28 |       71 | 40.77%     | ok               |

## DASH-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 104.61%  | 28.82%             | -25.18% |     0.87 |       40 | 15.90%     | ok               |
|          40 | 64.07%   | 28.82%             | -28.66% |     0.67 |       48 | 22.61%     | ok               |
|          45 | 47.52%   | 28.82%             | -34.23% |     0.58 |       44 | 18.01%     | ok               |
|          35 | -38.83%  | 28.82%             | -63.23% |     0.01 |       69 | 27.20%     | ok               |
|          30 | -41.84%  | 28.82%             | -64.43% |    -0.02 |       63 | 30.27%     | ok               |

## DBC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -8.19%   | 27.25%             | -26.66% |    -0.21 |       73 | 41.10%     | ok               |
|          25 | -11.13%  | 27.25%             | -25.69% |    -0.33 |       62 | 37.44%     | ok               |
|          20 | -11.66%  | 27.25%             | -25.83% |    -0.35 |       65 | 39.27%     | ok               |
|          50 | -11.24%  | 27.25%             | -20.31% |    -0.4  |       46 | 24.46%     | ok               |
|          30 | -13.20%  | 27.25%             | -25.15% |    -0.42 |       60 | 35.77%     | ok               |

## DE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -4.52%   | 61.70%             | -24.77% |     0    |       72 | 44.93%     | ok               |
|          45 | -4.85%   | 61.70%             | -25.90% |    -0.03 |       62 | 35.77%     | ok               |
|          50 | -5.08%   | 61.70%             | -23.33% |    -0.05 |       68 | 32.45%     | ok               |
|          20 | -8.02%   | 61.70%             | -32.04% |    -0.07 |       74 | 50.42%     | ok               |
|          25 | -8.46%   | 61.70%             | -29.28% |    -0.09 |       78 | 47.42%     | ok               |

## DIA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -2.43%   | 37.97%             | -11.28% |    -0.09 |       60 | 44.76%     | ok               |
|          35 | -2.88%   | 37.97%             | -13.15% |    -0.12 |       62 | 41.60%     | ok               |
|          30 | -3.93%   | 37.97%             | -12.94% |    -0.18 |       60 | 43.59%     | ok               |
|          20 | -5.84%   | 37.97%             | -13.85% |    -0.27 |       66 | 47.25%     | ok               |
|          40 | -6.84%   | 37.97%             | -15.06% |    -0.37 |       68 | 38.77%     | ok               |

## DIS Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 15.73%   | -6.59%             | -16.40% |     0.52 |       48 | 25.62%     | ok               |
|          40 | -9.48%   | -6.59%             | -23.41% |    -0.14 |       61 | 34.11%     | ok               |
|          45 | -10.03%  | -6.59%             | -18.50% |    -0.18 |       49 | 29.45%     | ok               |
|          15 | -18.12%  | -6.59%             | -32.73% |    -0.27 |       89 | 54.74%     | ok               |
|          35 | -16.46%  | -6.59%             | -25.70% |    -0.29 |       73 | 40.27%     | ok               |

## DOGE-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 9.04%    | -65.19%            | -59.36% |     0.35 |       76 | 63.98%     | ok               |
|          25 | 5.11%    | -65.19%            | -55.33% |     0.31 |       67 | 54.02%     | ok               |
|          20 | 1.68%    | -65.19%            | -57.37% |     0.28 |       79 | 59.20%     | ok               |
|          30 | -12.05%  | -65.19%            | -62.31% |     0.13 |       70 | 48.47%     | ok               |
|          35 | -38.10%  | -65.19%            | -61.79% |    -0.27 |       66 | 42.15%     | ok               |

## DOT-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -37.25%  | -81.02%            | -48.63% |    -0.5  |       58 | 26.25%     | ok               |
|          45 | -39.99%  | -81.02%            | -51.81% |    -0.5  |       50 | 31.42%     | ok               |
|          35 | -57.95%  | -81.02%            | -63.08% |    -0.63 |       78 | 41.57%     | ok               |
|          15 | -67.90%  | -81.02%            | -73.29% |    -0.68 |       83 | 63.41%     | ok               |
|          40 | -50.09%  | -81.02%            | -56.98% |    -0.68 |       56 | 34.29%     | ok               |

## DXY-INDEX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -1.69%   | -2.48%             | -6.29%  |    -0.25 |       42 | 32.68%     | ok               |
|          15 | -3.48%   | -2.48%             | -11.37% |    -0.3  |       80 | 75.97%     | ok               |
|          40 | -4.66%   | -2.48%             | -8.24%  |    -0.59 |       68 | 50.43%     | ok               |
|          25 | -6.28%   | -2.48%             | -12.10% |    -0.68 |       78 | 66.45%     | ok               |
|          35 | -5.86%   | -2.48%             | -10.39% |    -0.72 |       71 | 56.49%     | ok               |

## EEM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -6.38%   | 58.51%             | -15.88% |    -0.18 |       50 | 33.61%     | ok               |
|          45 | -8.02%   | 58.51%             | -17.36% |    -0.24 |       52 | 35.11%     | ok               |
|          35 | -8.99%   | 58.51%             | -23.88% |    -0.24 |       66 | 39.27%     | ok               |
|          40 | -8.36%   | 58.51%             | -19.52% |    -0.24 |       64 | 37.27%     | ok               |
|          25 | -11.76%  | 58.51%             | -25.60% |    -0.33 |       65 | 42.26%     | ok               |

## EFA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -5.34%   | 36.14%             | -11.27% |    -0.14 |       62 | 49.42%     | ok               |
|          30 | -10.12%  | 36.14%             | -13.53% |    -0.39 |       58 | 41.26%     | ok               |
|          20 | -11.33%  | 36.14%             | -12.61% |    -0.41 |       67 | 46.59%     | ok               |
|          50 | -10.75%  | 36.14%             | -17.56% |    -0.5  |       54 | 33.94%     | ok               |
|          25 | -12.92%  | 36.14%             | -15.78% |    -0.5  |       64 | 44.09%     | ok               |

## EOG Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -25.30%  | 10.03%             | -48.13% |    -0.5  |       81 | 49.42%     | ok               |
|          35 | -26.13%  | 10.03%             | -46.26% |    -0.57 |       79 | 44.09%     | ok               |
|          40 | -25.40%  | 10.03%             | -43.26% |    -0.57 |       66 | 38.94%     | ok               |
|          25 | -29.10%  | 10.03%             | -51.99% |    -0.58 |       82 | 52.41%     | ok               |
|          45 | -25.29%  | 10.03%             | -43.17% |    -0.59 |       60 | 35.44%     | ok               |

## ETC-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -2.84%   | -65.70%            | -31.28% |     0.08 |       26 | 15.90%     | ok               |
|          45 | -12.62%  | -65.70%            | -38.47% |    -0.1  |       26 | 17.62%     | ok               |
|          35 | -15.58%  | -65.70%            | -45.32% |    -0.12 |       44 | 25.29%     | ok               |
|          40 | -19.39%  | -65.70%            | -43.28% |    -0.23 |       40 | 21.26%     | ok               |
|          30 | -31.66%  | -65.70%            | -48.09% |    -0.43 |       62 | 28.93%     | ok               |

## ETH-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 180.36%  | -12.42%            | -30.11% |     1.39 |       60 | 45.59%     | ok               |
|          30 | 128.00%  | -12.42%            | -32.89% |     1.11 |       66 | 54.21%     | ok               |
|          25 | 77.31%   | -12.42%            | -40.90% |     0.83 |       62 | 59.00%     | ok               |
|          20 | 77.59%   | -12.42%            | -39.10% |     0.82 |       80 | 63.41%     | ok               |
|          15 | 69.27%   | -12.42%            | -42.74% |     0.77 |       75 | 68.97%     | ok               |

## EWJ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -19.66%  | 37.78%             | -30.73% |    -0.66 |       62 | 36.44%     | ok               |
|          20 | -21.03%  | 37.78%             | -31.32% |    -0.7  |       58 | 38.44%     | ok               |
|          25 | -23.30%  | 37.78%             | -31.18% |    -0.8  |       58 | 37.44%     | ok               |
|          45 | -20.39%  | 37.78%             | -27.68% |    -0.81 |       56 | 28.62%     | ok               |
|          35 | -23.47%  | 37.78%             | -32.54% |    -0.83 |       66 | 34.78%     | ok               |

## FCX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -2.83%   | 57.39%             | -26.57% |     0.09 |       56 | 30.62%     | ok               |
|          45 | -7.02%   | 57.39%             | -32.99% |     0.03 |       56 | 35.11%     | ok               |
|          40 | -19.26%  | 57.39%             | -42.49% |    -0.18 |       68 | 39.27%     | ok               |
|          30 | -29.92%  | 57.39%             | -48.22% |    -0.35 |       67 | 45.92%     | ok               |
|          35 | -34.24%  | 57.39%             | -51.41% |    -0.46 |       73 | 44.09%     | ok               |

## FET-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -18.92%  | -77.02%            | -62.04% |     0.13 |       90 | 52.68%     | ok               |
|          15 | -28.68%  | -77.02%            | -59.58% |     0.05 |       84 | 56.70%     | ok               |
|          25 | -33.94%  | -77.02%            | -60.96% |    -0.06 |       85 | 46.17%     | ok               |
|          30 | -43.54%  | -77.02%            | -52.44% |    -0.23 |       83 | 41.19%     | ok               |
|          45 | -38.02%  | -77.02%            | -48.61% |    -0.43 |       50 | 18.20%     | ok               |

## FIL-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -21.24%  | -76.83%            | -34.38% |    -0.16 |       44 | 23.37%     | ok               |
|          35 | -38.50%  | -76.83%            | -41.43% |    -0.45 |       56 | 27.97%     | ok               |
|          30 | -44.63%  | -76.83%            | -48.59% |    -0.54 |       68 | 34.10%     | ok               |
|          45 | -38.83%  | -76.83%            | -41.74% |    -0.58 |       42 | 17.82%     | ok               |
|          15 | -58.77%  | -76.83%            | -61.48% |    -0.68 |       89 | 45.79%     | ok               |

## FXI Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -1.91%   | 48.92%             | -22.57% |     0.04 |       46 | 32.61%     | ok               |
|          30 | -2.18%   | 48.92%             | -23.91% |     0.03 |       44 | 31.11%     | ok               |
|          20 | -4.06%   | 48.92%             | -24.53% |    -0.01 |       48 | 34.11%     | ok               |
|          15 | -4.44%   | 48.92%             | -21.68% |    -0.01 |       51 | 36.44%     | ok               |
|          35 | -6.55%   | 48.92%             | -27.53% |    -0.09 |       44 | 29.12%     | ok               |

## GDX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 12.69%   | 180.76%            | -35.59% |     0.32 |       72 | 50.75%     | ok               |
|          40 | 10.10%   | 180.76%            | -31.87% |     0.29 |       62 | 41.26%     | ok               |
|          30 | 7.61%    | 180.76%            | -34.99% |     0.25 |       58 | 46.42%     | ok               |
|          35 | 5.36%    | 180.76%            | -32.37% |     0.22 |       66 | 43.59%     | ok               |
|          25 | 1.91%    | 180.76%            | -38.90% |     0.17 |       62 | 47.59%     | ok               |

## GDXJ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -13.19%  | 199.81%            | -45.05% |    -0.02 |       66 | 50.58%     | ok               |
|          50 | -21.12%  | 199.81%            | -44.94% |    -0.24 |       58 | 36.94%     | ok               |
|          30 | -24.86%  | 199.81%            | -44.93% |    -0.25 |       64 | 44.59%     | ok               |
|          25 | -29.88%  | 199.81%            | -47.26% |    -0.32 |       69 | 47.42%     | ok               |
|          35 | -28.41%  | 199.81%            | -43.49% |    -0.34 |       66 | 42.26%     | ok               |

## GE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 20.11%   | 181.45%            | -22.29% |     0.46 |       68 | 37.77%     | ok               |
|          45 | 11.04%   | 181.45%            | -25.68% |     0.31 |       76 | 40.60%     | ok               |
|          20 | 4.45%    | 181.45%            | -26.63% |     0.2  |       75 | 55.41%     | ok               |
|          30 | 2.71%    | 181.45%            | -27.82% |     0.17 |       80 | 51.41%     | ok               |
|          35 | 0.48%    | 181.45%            | -27.11% |     0.13 |       84 | 46.09%     | ok               |

## GLD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 29.35%   | 94.49%             | -14.61% |     0.71 |       48 | 49.75%     | ok               |
|          25 | 28.68%   | 94.49%             | -14.61% |     0.7  |       48 | 48.25%     | ok               |
|          30 | 22.55%   | 94.49%             | -16.63% |     0.58 |       50 | 47.09%     | ok               |
|          15 | 21.43%   | 94.49%             | -17.54% |     0.54 |       50 | 53.91%     | ok               |
|          35 | 16.18%   | 94.49%             | -17.29% |     0.46 |       54 | 45.09%     | ok               |

## GOOGL Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 83.32%   | 150.00%            | -18.25% |     1.25 |       57 | 48.75%     | ok               |
|          30 | 78.89%   | 150.00%            | -20.41% |     1.18 |       55 | 52.25%     | ok               |
|          45 | 67.79%   | 150.00%            | -14.13% |     1.15 |       52 | 42.10%     | ok               |
|          25 | 76.17%   | 150.00%            | -19.76% |     1.14 |       53 | 54.24%     | ok               |
|          50 | 60.60%   | 150.00%            | -14.89% |     1.09 |       48 | 37.27%     | ok               |

## GRT-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 21.00%   | -86.41%            | -49.67% |     0.44 |       69 | 61.88%     | ok               |
|          20 | 11.40%   | -86.41%            | -46.47% |     0.35 |       75 | 56.70%     | ok               |
|          50 | 12.33%   | -86.41%            | -36.42% |     0.34 |       44 | 21.46%     | ok               |
|          45 | 9.39%    | -86.41%            | -41.83% |     0.3  |       50 | 26.44%     | ok               |
|          30 | 5.02%    | -86.41%            | -50.20% |     0.27 |       81 | 43.68%     | ok               |

## GS Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 22.54%   | 165.71%            | -20.56% |     0.49 |       74 | 59.23%     | ok               |
|          20 | 5.82%    | 165.71%            | -23.19% |     0.22 |       74 | 55.24%     | ok               |
|          40 | 1.70%    | 165.71%            | -17.88% |     0.13 |       68 | 43.76%     | ok               |
|          25 | 0.47%    | 165.71%            | -23.32% |     0.11 |       74 | 52.75%     | ok               |
|          30 | -0.65%   | 165.71%            | -22.13% |     0.09 |       74 | 50.42%     | ok               |

## HD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -6.99%   | -6.86%             | -17.69% |    -0.11 |       71 | 43.59%     | ok               |
|          25 | -7.72%   | -6.86%             | -18.51% |    -0.13 |       70 | 45.59%     | ok               |
|          45 | -11.03%  | -6.86%             | -20.74% |    -0.31 |       56 | 27.79%     | ok               |
|          40 | -12.64%  | -6.86%             | -19.63% |    -0.34 |       82 | 33.28%     | ok               |
|          15 | -16.96%  | -6.86%             | -27.26% |    -0.35 |      109 | 54.41%     | ok               |

## HON Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -11.49%  | 24.04%             | -21.17% |    -0.32 |       68 | 32.11%     | ok               |
|          45 | -13.26%  | 24.04%             | -19.99% |    -0.35 |       70 | 37.10%     | ok               |
|          40 | -22.09%  | 24.04%             | -27.04% |    -0.6  |       74 | 41.26%     | ok               |
|          35 | -23.58%  | 24.04%             | -28.11% |    -0.63 |       89 | 47.59%     | ok               |
|          30 | -26.66%  | 24.04%             | -29.92% |    -0.71 |       93 | 52.41%     | ok               |

## HYG Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -8.39%   | 3.03%              | -8.39%  |    -1.01 |       72 | 29.95%     | ok               |
|          15 | -9.77%   | 3.03%              | -10.72% |    -1.06 |       90 | 41.93%     | ok               |
|          20 | -9.64%   | 3.03%              | -10.74% |    -1.08 |       88 | 39.43%     | ok               |
|          25 | -9.78%   | 3.03%              | -10.52% |    -1.1  |       85 | 37.27%     | ok               |
|          30 | -9.49%   | 3.03%              | -10.00% |    -1.11 |       83 | 34.61%     | ok               |

## IBIT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 53.73%   | -4.00%             | -17.37% |     1.05 |       22 | 21.57%     | ok               |
|          15 | 56.91%   | -4.00%             | -19.20% |     0.94 |       40 | 38.43%     | ok               |
|          45 | 44.27%   | -4.00%             | -17.37% |     0.89 |       26 | 22.92%     | ok               |
|          40 | 38.04%   | -4.00%             | -17.78% |     0.79 |       26 | 24.72%     | ok               |
|          30 | 30.82%   | -4.00%             | -18.95% |     0.65 |       34 | 31.01%     | ok               |

## IBM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -21.31%  | 20.68%             | -47.64% |    -0.18 |       91 | 63.23%     | ok               |
|          35 | -25.62%  | 20.68%             | -47.10% |    -0.32 |       69 | 46.76%     | ok               |
|          30 | -28.39%  | 20.68%             | -48.94% |    -0.37 |       75 | 51.08%     | ok               |
|          20 | -31.54%  | 20.68%             | -51.95% |    -0.39 |       73 | 55.74%     | ok               |
|          50 | -30.29%  | 20.68%             | -45.88% |    -0.46 |       50 | 34.44%     | ok               |

## ICP-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 3.50%    | -65.48%            | -39.11% |     0.25 |       60 | 28.74%     | ok               |
|          40 | 0.63%    | -65.48%            | -32.85% |     0.2  |       52 | 23.95%     | ok               |
|          30 | -10.52%  | -65.48%            | -50.29% |     0.15 |       77 | 34.67%     | ok               |
|          50 | -18.44%  | -65.48%            | -43.65% |    -0.1  |       34 | 14.37%     | ok               |
|          15 | -45.90%  | -65.48%            | -59.86% |    -0.17 |       77 | 47.32%     | ok               |

## IEF Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -6.92%   | -0.92%             | -10.10% |    -0.82 |       72 | 42.93%     | ok               |
|          15 | -7.47%   | -0.92%             | -10.83% |    -0.87 |       71 | 44.43%     | ok               |
|          25 | -10.50%  | -0.92%             | -11.63% |    -1.32 |       78 | 40.10%     | ok               |
|          45 | -8.16%   | -0.92%             | -9.85%  |    -1.33 |       56 | 23.29%     | ok               |
|          40 | -8.76%   | -0.92%             | -9.92%  |    -1.36 |       66 | 25.46%     | ok               |

## IEMG Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -4.61%   | 54.24%             | -14.40% |    -0.13 |       56 | 31.28%     | ok               |
|          35 | -5.70%   | 54.24%             | -22.13% |    -0.14 |       65 | 39.43%     | ok               |
|          45 | -5.39%   | 54.24%             | -15.40% |    -0.15 |       52 | 33.78%     | ok               |
|          40 | -6.85%   | 54.24%             | -18.89% |    -0.2  |       64 | 36.77%     | ok               |
|          25 | -9.86%   | 54.24%             | -25.58% |    -0.28 |       61 | 42.26%     | ok               |

## INJ-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -10.15%  | -59.44%            | -52.34% |     0.06 |       44 | 23.37%     | ok               |
|          35 | -21.17%  | -59.44%            | -59.17% |    -0.02 |       60 | 32.57%     | ok               |
|          40 | -26.45%  | -59.44%            | -55.86% |    -0.14 |       50 | 29.12%     | ok               |
|          50 | -22.38%  | -59.44%            | -49.35% |    -0.14 |       48 | 20.11%     | ok               |
|          20 | -55.65%  | -59.44%            | -81.16% |    -0.45 |       78 | 46.74%     | ok               |

## INTC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 81.91%   | 133.47%            | -49.32% |     0.78 |       54 | 33.61%     | ok               |
|          40 | 75.94%   | 133.47%            | -55.86% |     0.73 |       62 | 37.94%     | ok               |
|          15 | 80.45%   | 133.47%            | -53.65% |     0.72 |       78 | 60.40%     | ok               |
|          50 | 69.07%   | 133.47%            | -48.35% |     0.71 |       62 | 29.78%     | ok               |
|          25 | 62.37%   | 133.47%            | -56.41% |     0.65 |       77 | 51.25%     | ok               |

## INTU Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -1.11%   | -50.48%            | -41.23% |     0.1  |       69 | 28.29%     | ok               |
|          45 | -1.72%   | -50.48%            | -41.46% |     0.09 |       67 | 32.11%     | ok               |
|          40 | -7.39%   | -50.48%            | -44.40% |    -0.01 |       67 | 34.78%     | ok               |
|          35 | -14.47%  | -50.48%            | -46.02% |    -0.14 |       71 | 38.27%     | ok               |
|          20 | -15.71%  | -50.48%            | -39.89% |    -0.14 |       76 | 47.09%     | ok               |

## ITA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -0.19%   | 97.20%             | -21.48% |     0.06 |       76 | 36.61%     | ok               |
|          15 | -3.49%   | 97.20%             | -25.58% |    -0    |       89 | 58.40%     | ok               |
|          30 | -3.58%   | 97.20%             | -23.75% |    -0.03 |       74 | 46.26%     | ok               |
|          35 | -5.71%   | 97.20%             | -23.16% |    -0.1  |       76 | 44.76%     | ok               |
|          40 | -6.79%   | 97.20%             | -20.58% |    -0.15 |       78 | 41.26%     | ok               |

## IWM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 11.08%   | 47.63%             | -14.08% |     0.49 |       42 | 31.28%     | ok               |
|          30 | 11.84%   | 47.63%             | -12.83% |     0.47 |       50 | 35.77%     | ok               |
|          25 | 11.95%   | 47.63%             | -13.55% |     0.47 |       52 | 36.94%     | ok               |
|          35 | 10.83%   | 47.63%             | -14.11% |     0.45 |       48 | 33.61%     | ok               |
|          20 | 7.53%    | 47.63%             | -14.08% |     0.32 |       62 | 37.94%     | ok               |

## JNJ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 20.35%   | 61.41%             | -10.57% |     0.83 |       52 | 36.77%     | ok               |
|          15 | 18.02%   | 61.41%             | -18.02% |     0.6  |       64 | 56.74%     | ok               |
|          45 | 11.03%   | 61.41%             | -13.77% |     0.47 |       52 | 41.10%     | ok               |
|          20 | 12.57%   | 61.41%             | -17.61% |     0.46 |       70 | 53.24%     | ok               |
|          40 | 6.83%    | 61.41%             | -14.77% |     0.31 |       58 | 45.42%     | ok               |

## JPM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 11.18%   | 89.55%             | -15.90% |     0.41 |       54 | 38.27%     | ok               |
|          45 | 0.62%    | 89.55%             | -21.91% |     0.09 |       56 | 41.26%     | ok               |
|          20 | -15.66%  | 89.55%             | -33.59% |    -0.27 |       84 | 56.07%     | ok               |
|          40 | -13.19%  | 89.55%             | -28.47% |    -0.32 |       68 | 43.93%     | ok               |
|          35 | -18.31%  | 89.55%             | -27.43% |    -0.46 |       76 | 47.92%     | ok               |

## KO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 23.75%   | 43.55%             | -8.20%  |     0.85 |       51 | 37.94%     | ok               |
|          35 | 19.96%   | 43.55%             | -8.07%  |     0.75 |       54 | 36.61%     | ok               |
|          40 | 17.46%   | 43.55%             | -9.28%  |     0.71 |       56 | 33.44%     | ok               |
|          25 | 18.64%   | 43.55%             | -9.73%  |     0.69 |       57 | 40.60%     | ok               |
|          50 | 10.20%   | 43.55%             | -12.31% |     0.48 |       38 | 26.96%     | ok               |

## LDO-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 70.52%   | -73.34%            | -48.17% |     0.72 |       82 | 57.85%     | ok               |
|          20 | 48.25%   | -73.34%            | -45.55% |     0.61 |       84 | 52.68%     | ok               |
|          50 | 33.03%   | -73.34%            | -48.04% |     0.57 |       52 | 18.20%     | ok               |
|          30 | 30.28%   | -73.34%            | -61.16% |     0.51 |       80 | 43.68%     | ok               |
|          35 | 30.31%   | -73.34%            | -61.98% |     0.5  |       80 | 36.59%     | ok               |

## LIN Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -8.40%   | 3.41%              | -23.70% |    -0.23 |       65 | 47.59%     | ok               |
|          25 | -8.62%   | 3.41%              | -22.01% |    -0.25 |       65 | 39.77%     | ok               |
|          20 | -10.58%  | 3.41%              | -23.00% |    -0.32 |       64 | 42.93%     | ok               |
|          30 | -12.48%  | 3.41%              | -20.61% |    -0.41 |       68 | 36.94%     | ok               |
|          35 | -11.92%  | 3.41%              | -20.06% |    -0.42 |       64 | 30.45%     | ok               |

## LINK-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 4.29%    | -44.86%            | -33.71% |     0.25 |       48 | 28.35%     | ok               |
|          30 | 0.89%    | -44.86%            | -40.80% |     0.24 |       71 | 43.49%     | ok               |
|          50 | -0.76%   | -44.86%            | -32.27% |     0.18 |       40 | 22.41%     | ok               |
|          35 | -10.45%  | -44.86%            | -40.61% |     0.11 |       59 | 38.31%     | ok               |
|          40 | -15.36%  | -44.86%            | -42.20% |     0.02 |       55 | 32.57%     | ok               |

## LLY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 6.14%    | 56.68%             | -38.23% |     0.23 |       44 | 34.94%     | ok               |
|          15 | -2.75%   | 56.68%             | -48.12% |     0.1  |       61 | 57.90%     | ok               |
|          45 | -6.11%   | 56.68%             | -42.66% |    -0    |       50 | 38.27%     | ok               |
|          20 | -16.07%  | 56.68%             | -51.34% |    -0.14 |       68 | 53.08%     | ok               |
|          25 | -17.46%  | 56.68%             | -53.47% |    -0.18 |       64 | 50.42%     | ok               |

## LRCX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -13.68%  | 230.32%            | -48.71% |    -0.02 |       76 | 33.61%     | ok               |
|          40 | -17.02%  | 230.32%            | -55.33% |    -0.04 |       70 | 39.43%     | ok               |
|          35 | -18.62%  | 230.32%            | -58.47% |    -0.06 |       78 | 41.60%     | ok               |
|          30 | -23.96%  | 230.32%            | -61.08% |    -0.14 |       82 | 42.26%     | ok               |
|          15 | -30.44%  | 230.32%            | -56.86% |    -0.17 |       87 | 52.25%     | ok               |

## LTC-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | -5.80%   | -56.07%            | -38.62% |     0.1  |       66 | 42.72%     | ok               |
|          45 | -8.26%   | -56.07%            | -37.29% |     0.05 |       56 | 31.99%     | ok               |
|          40 | -15.58%  | -56.07%            | -40.32% |    -0.06 |       56 | 37.74%     | ok               |
|          30 | -20.59%  | -56.07%            | -38.94% |    -0.1  |       70 | 49.81%     | ok               |
|          25 | -24.36%  | -56.07%            | -39.59% |    -0.15 |       74 | 52.68%     | ok               |

## MCD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 3.24%    | -1.94%             | -9.22%  |     0.2  |       42 | 20.47%     | ok               |
|          30 | -2.74%   | -1.94%             | -18.81% |    -0.06 |       77 | 38.44%     | ok               |
|          25 | -3.78%   | -1.94%             | -20.47% |    -0.09 |       77 | 41.10%     | ok               |
|          40 | -6.34%   | -1.94%             | -16.86% |    -0.25 |       73 | 28.95%     | ok               |
|          35 | -7.86%   | -1.94%             | -15.45% |    -0.29 |       69 | 34.78%     | ok               |

## META Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -19.51%  | 19.94%             | -34.72% |    -0.31 |       70 | 37.10%     | ok               |
|          40 | -27.56%  | 19.94%             | -38.23% |    -0.48 |       70 | 40.27%     | ok               |
|          25 | -33.89%  | 19.94%             | -43.26% |    -0.58 |       71 | 50.58%     | ok               |
|          50 | -29.58%  | 19.94%             | -37.54% |    -0.59 |       72 | 33.44%     | ok               |
|          30 | -35.66%  | 19.94%             | -42.43% |    -0.65 |       76 | 47.42%     | ok               |

## MPC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 19.80%   | 58.35%             | -23.96% |     0.46 |       48 | 38.60%     | ok               |
|          45 | 12.20%   | 58.35%             | -25.09% |     0.33 |       54 | 42.26%     | ok               |
|          40 | 7.96%    | 58.35%             | -25.70% |     0.26 |       56 | 44.43%     | ok               |
|          35 | 4.63%    | 58.35%             | -35.90% |     0.2  |       64 | 46.92%     | ok               |
|          30 | -11.83%  | 58.35%             | -44.76% |    -0.09 |       67 | 49.75%     | ok               |

## MRK Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -17.48%  | 6.52%              | -29.91% |    -0.29 |       85 | 53.91%     | ok               |
|          25 | -16.46%  | 6.52%              | -31.07% |    -0.3  |       70 | 46.09%     | ok               |
|          20 | -20.55%  | 6.52%              | -29.38% |    -0.4  |       75 | 49.42%     | ok               |
|          50 | -21.52%  | 6.52%              | -27.68% |    -0.6  |       58 | 29.12%     | ok               |
|          45 | -23.47%  | 6.52%              | -27.72% |    -0.62 |       59 | 32.45%     | ok               |

## MS Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -3.32%   | 139.90%            | -19.99% |     0    |       72 | 41.43%     | ok               |
|          15 | -4.98%   | 139.90%            | -22.02% |    -0.01 |       73 | 58.24%     | ok               |
|          20 | -5.09%   | 139.90%            | -25.68% |    -0.02 |       77 | 54.41%     | ok               |
|          30 | -10.18%  | 139.90%            | -27.79% |    -0.16 |       77 | 49.58%     | ok               |
|          35 | -10.11%  | 139.90%            | -25.26% |    -0.17 |       78 | 46.09%     | ok               |

## MSFT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -14.86%  | 17.55%             | -24.64% |    -0.36 |       66 | 34.44%     | ok               |
|          50 | -16.93%  | 17.55%             | -25.48% |    -0.44 |       60 | 29.62%     | ok               |
|          35 | -28.93%  | 17.55%             | -35.51% |    -0.71 |       73 | 43.26%     | ok               |
|          40 | -28.28%  | 17.55%             | -34.92% |    -0.72 |       69 | 38.10%     | ok               |
|          30 | -31.74%  | 17.55%             | -38.06% |    -0.77 |       83 | 47.59%     | ok               |

## MU Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 283.47%  | 864.09%            | -63.96% |     1.39 |       56 | 52.58%     | ok               |
|          15 | 307.90%  | 864.09%            | -61.96% |     1.32 |       51 | 66.22%     | ok               |
|          25 | 250.40%  | 864.09%            | -67.90% |     1.28 |       51 | 59.40%     | ok               |
|          30 | 236.53%  | 864.09%            | -68.76% |     1.26 |       51 | 57.74%     | ok               |
|          35 | 229.75%  | 864.09%            | -69.09% |     1.26 |       63 | 55.24%     | ok               |

## NEAR-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 58.25%   | -41.27%            | -49.73% |     0.73 |       42 | 22.41%     | ok               |
|          40 | 45.16%   | -41.27%            | -57.80% |     0.63 |       44 | 26.44%     | ok               |
|          50 | 38.01%   | -41.27%            | -52.97% |     0.58 |       34 | 17.82%     | ok               |
|          35 | 17.88%   | -41.27%            | -61.61% |     0.4  |       68 | 31.23%     | ok               |
|          30 | 8.37%    | -41.27%            | -59.54% |     0.33 |       83 | 40.61%     | ok               |

## NEM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 21.11%   | 208.18%            | -29.41% |     0.41 |       58 | 60.73%     | ok               |
|          20 | 8.14%    | 208.18%            | -30.47% |     0.27 |       68 | 56.24%     | ok               |
|          25 | -9.17%   | 208.18%            | -37.89% |     0.04 |       66 | 54.41%     | ok               |
|          30 | -20.55%  | 208.18%            | -38.49% |    -0.15 |       70 | 52.75%     | ok               |
|          50 | -20.83%  | 208.18%            | -33.24% |    -0.22 |       58 | 39.43%     | ok               |

## NFLX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 38.47%   | 20.21%             | -13.37% |     0.85 |       50 | 44.09%     | ok               |
|          50 | 34.26%   | 20.21%             | -16.28% |     0.83 |       48 | 36.11%     | ok               |
|          35 | 34.53%   | 20.21%             | -18.30% |     0.75 |       66 | 48.09%     | ok               |
|          45 | 24.76%   | 20.21%             | -15.48% |     0.62 |       56 | 40.43%     | ok               |
|          15 | 27.72%   | 20.21%             | -26.59% |     0.57 |       69 | 63.89%     | ok               |

## NKE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -30.49%  | -58.11%            | -54.28% |    -0.34 |       88 | 54.91%     | ok               |
|          35 | -25.88%  | -58.11%            | -42.13% |    -0.35 |       73 | 38.27%     | ok               |
|          20 | -30.54%  | -58.11%            | -49.34% |    -0.36 |       87 | 50.92%     | ok               |
|          25 | -33.41%  | -58.11%            | -51.20% |    -0.42 |       87 | 48.25%     | ok               |
|          30 | -36.59%  | -58.11%            | -55.35% |    -0.5  |       83 | 44.26%     | ok               |

## NOW Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 1.23%    | -24.73%            | -26.78% |     0.18 |       82 | 46.09%     | ok               |
|          20 | -1.18%   | -24.73%            | -34.71% |     0.16 |       79 | 52.41%     | ok               |
|          25 | -4.58%   | -24.73%            | -32.31% |     0.11 |       76 | 49.42%     | ok               |
|          15 | -8.40%   | -24.73%            | -38.33% |     0.07 |       87 | 55.41%     | ok               |
|          40 | -7.07%   | -24.73%            | -30.91% |     0.03 |       74 | 35.44%     | ok               |

## NVDA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -13.01%  | 143.65%            | -35.26% |    -0.05 |       74 | 47.42%     | ok               |
|          20 | -18.08%  | 143.65%            | -40.59% |    -0.08 |       70 | 55.44%     | ok               |
|          25 | -17.95%  | 143.65%            | -37.16% |    -0.1  |       71 | 50.45%     | ok               |
|          15 | -26.95%  | 143.65%            | -45.14% |    -0.2  |       71 | 58.65%     | ok               |
|          35 | -24.77%  | 143.65%            | -42.39% |    -0.27 |       82 | 44.56%     | ok               |

## OP-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 21.31%   | -90.71%            | -36.11% |     0.44 |       32 | 11.30%     | ok               |
|          45 | 20.44%   | -90.71%            | -45.76% |     0.42 |       34 | 15.90%     | ok               |
|          40 | 10.62%   | -90.71%            | -53.61% |     0.32 |       48 | 24.33%     | ok               |
|          35 | -12.10%  | -90.71%            | -59.71% |     0.07 |       52 | 28.74%     | ok               |
|          30 | -15.92%  | -90.71%            | -71.26% |     0.07 |       66 | 35.25%     | ok               |

## ORCL Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 209.68%  | 14.29%             | -29.32% |     1.26 |       67 | 65.56%     | ok               |
|          25 | 134.79%  | 14.29%             | -27.76% |     1.01 |       63 | 58.74%     | ok               |
|          20 | 130.94%  | 14.29%             | -29.32% |     0.99 |       70 | 61.40%     | ok               |
|          45 | 108.32%  | 14.29%             | -32.35% |     0.96 |       62 | 42.93%     | ok               |
|          35 | 112.56%  | 14.29%             | -31.95% |     0.94 |       68 | 52.08%     | ok               |

## OXY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | -2.07%   | -10.45%            | -30.04% |     0.08 |       70 | 41.43%     | ok               |
|          30 | -4.45%   | -10.45%            | -34.15% |     0.05 |       71 | 46.76%     | ok               |
|          50 | -4.91%   | -10.45%            | -30.93% |     0    |       44 | 29.78%     | ok               |
|          40 | -7.70%   | -10.45%            | -31.45% |    -0.04 |       58 | 36.94%     | ok               |
|          45 | -16.13%  | -10.45%            | -36.08% |    -0.24 |       50 | 32.11%     | ok               |

## PEP Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 13.04%   | -15.98%            | -11.62% |     0.59 |       42 | 27.45%     | ok               |
|          45 | 5.46%    | -15.98%            | -14.22% |     0.27 |       64 | 32.11%     | ok               |
|          40 | 1.38%    | -15.98%            | -18.04% |     0.11 |       72 | 37.60%     | ok               |
|          35 | 0.24%    | -15.98%            | -21.42% |     0.07 |       79 | 42.26%     | ok               |
|          30 | -5.83%   | -15.98%            | -21.35% |    -0.11 |       75 | 47.92%     | ok               |

## PEPE-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -8.77%   | -59.90%            | -57.66% |     0.2  |       81 | 45.98%     | ok               |
|          15 | -17.71%  | -59.90%            | -61.96% |     0.19 |       78 | 61.88%     | ok               |
|          35 | -11.24%  | -59.90%            | -49.27% |     0.14 |       68 | 40.04%     | ok               |
|          25 | -17.94%  | -59.90%            | -53.88% |     0.12 |       87 | 51.53%     | ok               |
|          20 | -25.81%  | -59.90%            | -61.13% |     0.07 |       84 | 58.43%     | ok               |

## PFE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -20.53%  | -6.86%             | -22.94% |    -0.74 |       54 | 19.13%     | ok               |
|          40 | -26.77%  | -6.86%             | -30.10% |    -0.92 |       74 | 24.29%     | ok               |
|          50 | -23.96%  | -6.86%             | -26.14% |    -0.98 |       42 | 15.64%     | ok               |
|          35 | -32.84%  | -6.86%             | -35.77% |    -1.07 |       88 | 32.11%     | ok               |
|          30 | -40.56%  | -6.86%             | -43.15% |    -1.29 |       83 | 36.77%     | ok               |

## PG Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -8.65%   | -9.00%             | -19.77% |    -0.32 |       54 | 30.78%     | ok               |
|          35 | -11.77%  | -9.00%             | -18.66% |    -0.44 |       62 | 34.28%     | ok               |
|          30 | -19.43%  | -9.00%             | -23.92% |    -0.74 |       65 | 37.27%     | ok               |
|          45 | -17.57%  | -9.00%             | -22.13% |    -0.77 |       54 | 28.29%     | ok               |
|          25 | -21.27%  | -9.00%             | -25.62% |    -0.82 |       77 | 38.77%     | ok               |

## PM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | -2.70%   | 100.16%            | -32.95% |     0.03 |       88 | 52.41%     | ok               |
|          20 | -5.34%   | 100.16%            | -33.29% |    -0.02 |       87 | 60.90%     | ok               |
|          30 | -5.75%   | 100.16%            | -34.97% |    -0.03 |       83 | 55.91%     | ok               |
|          50 | -8.53%   | 100.16%            | -35.70% |    -0.14 |       76 | 42.10%     | ok               |
|          40 | -9.16%   | 100.16%            | -37.94% |    -0.14 |       82 | 48.59%     | ok               |

## POL-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 55.83%   | -69.84%            | -41.08% |     0.73 |       79 | 49.43%     | ok               |
|          25 | 36.70%   | -69.84%            | -46.72% |     0.56 |       64 | 57.47%     | ok               |
|          20 | 25.59%   | -69.84%            | -52.88% |     0.47 |       70 | 61.88%     | ok               |
|          15 | -6.09%   | -69.84%            | -58.42% |     0.17 |       74 | 66.28%     | ok               |
|          40 | -2.43%   | -69.84%            | -38.75% |     0.13 |       54 | 30.08%     | ok               |

## QCOM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -6.42%   | -4.78%             | -54.50% |     0.09 |       73 | 47.59%     | ok               |
|          20 | -10.22%  | -4.78%             | -54.38% |     0.05 |       69 | 50.42%     | ok               |
|          35 | -12.87%  | -4.78%             | -50.58% |    -0.01 |       81 | 43.09%     | ok               |
|          30 | -22.75%  | -4.78%             | -56.59% |    -0.16 |       77 | 45.59%     | ok               |
|          15 | -25.14%  | -4.78%             | -57.94% |    -0.16 |       73 | 53.58%     | ok               |

## QQQ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 24.50%   | 62.74%             | -14.17% |     0.61 |       65 | 52.58%     | ok               |
|          25 | 17.71%   | 62.74%             | -13.90% |     0.51 |       63 | 46.59%     | ok               |
|          30 | 15.44%   | 62.74%             | -13.49% |     0.47 |       64 | 44.09%     | ok               |
|          20 | 14.86%   | 62.74%             | -15.99% |     0.43 |       71 | 49.25%     | ok               |
|          35 | 2.25%    | 62.74%             | -19.93% |     0.14 |       72 | 40.60%     | ok               |

## RENDER-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 37.50%   | -61.87%            | -43.43% |     0.56 |       92 | 53.26%     | ok               |
|          15 | 30.01%   | -61.87%            | -44.59% |     0.51 |       92 | 56.70%     | ok               |
|          25 | 28.84%   | -61.87%            | -40.60% |     0.5  |       90 | 48.66%     | ok               |
|          30 | -13.08%  | -61.87%            | -45.62% |     0.14 |       98 | 42.15%     | ok               |
|          40 | -15.88%  | -61.87%            | -40.91% |     0.04 |       74 | 27.01%     | ok               |

## RTX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 53.05%   | 143.30%            | -18.66% |     1.05 |       72 | 57.90%     | ok               |
|          35 | 42.42%   | 143.30%            | -18.00% |     0.99 |       50 | 52.08%     | ok               |
|          25 | 47.82%   | 143.30%            | -18.59% |     0.98 |       60 | 55.24%     | ok               |
|          30 | 45.58%   | 143.30%            | -16.99% |     0.95 |       54 | 54.08%     | ok               |
|          15 | 44.34%   | 143.30%            | -19.55% |     0.9  |       67 | 62.56%     | ok               |

## SBUX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -9.63%   | 14.73%             | -23.55% |    -0.11 |       59 | 42.10%     | ok               |
|          45 | -12.59%  | 14.73%             | -27.26% |    -0.25 |       68 | 30.45%     | ok               |
|          40 | -15.23%  | 14.73%             | -25.43% |    -0.29 |       64 | 34.11%     | ok               |
|          30 | -19.04%  | 14.73%             | -29.22% |    -0.35 |       62 | 39.93%     | ok               |
|          50 | -16.60%  | 14.73%             | -25.77% |    -0.39 |       56 | 26.12%     | ok               |

## SCHW Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 11.91%   | 61.65%             | -16.53% |     0.4  |       60 | 35.27%     | ok               |
|          25 | 7.03%    | 61.65%             | -28.76% |     0.25 |       63 | 51.25%     | ok               |
|          50 | 5.23%    | 61.65%             | -13.28% |     0.23 |       54 | 32.45%     | ok               |
|          20 | 3.19%    | 61.65%             | -29.24% |     0.16 |       71 | 53.74%     | ok               |
|          40 | 1.17%    | 61.65%             | -23.35% |     0.11 |       66 | 38.44%     | ok               |

## SHIB-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -25.92%  | -64.13%            | -50.97% |    -0.1  |       80 | 67.05%     | ok               |
|          25 | -25.02%  | -64.13%            | -45.80% |    -0.11 |       75 | 59.20%     | ok               |
|          20 | -29.53%  | -64.13%            | -48.24% |    -0.17 |       77 | 63.03%     | ok               |
|          35 | -28.73%  | -64.13%            | -52.76% |    -0.23 |       66 | 46.36%     | ok               |
|          30 | -34.77%  | -64.13%            | -47.96% |    -0.31 |       76 | 52.30%     | ok               |

## SHY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd    |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:-------|---------:|---------:|:-----------|:-----------------|
|          30 | -2.23%   | 0.32%              | -2.85% |    -0.78 |       46 | 34.11%     | ok               |
|          35 | -2.34%   | 0.32%              | -3.27% |    -0.83 |       48 | 32.28%     | ok               |
|          40 | -2.46%   | 0.32%              | -3.33% |    -0.89 |       48 | 30.45%     | ok               |
|          45 | -2.44%   | 0.32%              | -3.23% |    -0.9  |       46 | 27.29%     | ok               |
|          25 | -3.10%   | 0.32%              | -3.99% |    -1.06 |       58 | 36.27%     | ok               |

## SKY-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -35.03%  | -4.22%             | -56.39% |    -0.36 |       65 | 52.31%     | ok               |
|          30 | -31.42%  | -4.22%             | -47.82% |    -0.38 |       76 | 42.65%     | ok               |
|          25 | -34.35%  | -4.22%             | -50.05% |    -0.42 |       70 | 46.22%     | ok               |
|          20 | -44.35%  | -4.22%             | -59.15% |    -0.59 |       67 | 49.58%     | ok               |
|          35 | -37.73%  | -4.22%             | -49.68% |    -0.6  |       70 | 35.29%     | ok               |

## SLB Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 15.14%   | -3.17%             | -21.46% |     0.4  |       56 | 33.44%     | ok               |
|          40 | 11.58%   | -3.17%             | -25.33% |     0.33 |       50 | 36.94%     | ok               |
|          50 | -5.43%   | -3.17%             | -29.64% |    -0.05 |       54 | 28.95%     | ok               |
|          35 | -18.12%  | -3.17%             | -43.52% |    -0.29 |       78 | 44.09%     | ok               |
|          30 | -30.75%  | -3.17%             | -54.23% |    -0.57 |       79 | 50.58%     | ok               |

## SLV Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 63.85%   | 145.71%            | -34.10% |     0.83 |       52 | 33.94%     | ok               |
|          45 | 61.86%   | 145.71%            | -31.82% |     0.81 |       58 | 35.11%     | ok               |
|          40 | 59.93%   | 145.71%            | -31.93% |     0.79 |       64 | 37.27%     | ok               |
|          20 | 48.19%   | 145.71%            | -42.66% |     0.67 |       66 | 47.59%     | ok               |
|          35 | 46.29%   | 145.71%            | -36.89% |     0.67 |       72 | 40.10%     | ok               |

## SMH Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 88.98%   | 160.40%            | -31.01% |     1.15 |       51 | 48.59%     | ok               |
|          35 | 73.36%   | 160.40%            | -34.03% |     1.05 |       52 | 44.09%     | ok               |
|          25 | 71.05%   | 160.40%            | -32.94% |     1.02 |       48 | 47.25%     | ok               |
|          30 | 69.30%   | 160.40%            | -33.66% |     1.01 |       48 | 45.59%     | ok               |
|          45 | 56.54%   | 160.40%            | -33.35% |     0.94 |       52 | 38.44%     | ok               |

## SNX-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 14.46%   | -77.08%            | -30.08% |     0.37 |       60 | 29.50%     | ok               |
|          20 | 8.57%    | -77.08%            | -43.20% |     0.34 |       71 | 48.08%     | ok               |
|          40 | 4.25%    | -77.08%            | -36.00% |     0.24 |       46 | 23.75%     | ok               |
|          30 | -2.74%   | -77.08%            | -38.68% |     0.21 |       64 | 37.36%     | ok               |
|          15 | -23.85%  | -77.08%            | -44.00% |     0.03 |       81 | 52.68%     | ok               |

## SOL-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 21.75%   | -49.80%            | -39.68% |     0.44 |       58 | 36.40%     | ok               |
|          35 | -9.94%   | -49.80%            | -48.34% |     0.11 |       70 | 43.68%     | ok               |
|          25 | -16.53%  | -49.80%            | -41.09% |     0.05 |       76 | 57.09%     | ok               |
|          45 | -13.80%  | -49.80%            | -48.75% |     0.01 |       58 | 30.46%     | ok               |
|          15 | -26.48%  | -49.80%            | -49.65% |    -0.06 |       81 | 63.22%     | ok               |

## SOXX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 73.10%   | 141.68%            | -38.76% |     1    |       60 | 41.43%     | ok               |
|          25 | 75.13%   | 141.68%            | -39.65% |     1    |       54 | 46.42%     | ok               |
|          30 | 68.98%   | 141.68%            | -40.14% |     0.95 |       56 | 44.09%     | ok               |
|          20 | 61.90%   | 141.68%            | -38.67% |     0.86 |       59 | 47.25%     | ok               |
|          40 | 55.00%   | 141.68%            | -41.03% |     0.84 |       60 | 39.10%     | ok               |

## SPY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 12.56%   | 49.25%             | -14.25% |     0.46 |       59 | 52.58%     | ok               |
|          15 | 11.55%   | 49.25%             | -16.80% |     0.42 |       67 | 55.57%     | ok               |
|          25 | 5.55%    | 49.25%             | -15.22% |     0.25 |       59 | 51.58%     | ok               |
|          30 | 1.09%    | 49.25%             | -16.47% |     0.1  |       62 | 48.75%     | ok               |
|          35 | 0.49%    | 49.25%             | -16.72% |     0.08 |       58 | 45.76%     | ok               |

## SUSHI-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -28.52%  | -76.79%            | -40.08% |    -0.27 |       54 | 14.94%     | ok               |
|          40 | -64.10%  | -76.79%            | -70.29% |    -0.84 |       67 | 25.10%     | ok               |
|          45 | -61.36%  | -76.79%            | -65.87% |    -0.84 |       60 | 18.58%     | ok               |
|          15 | -76.80%  | -76.79%            | -82.03% |    -0.91 |       91 | 48.85%     | ok               |
|          35 | -75.94%  | -76.79%            | -81.46% |    -1.1  |       86 | 31.03%     | ok               |

## T Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 53.37%   | 39.39%             | -18.13% |     1.04 |       60 | 58.74%     | ok               |
|          15 | 55.72%   | 39.39%             | -15.08% |     1.04 |       69 | 63.06%     | ok               |
|          25 | 49.22%   | 39.39%             | -17.66% |     0.99 |       60 | 56.41%     | ok               |
|          30 | 32.87%   | 39.39%             | -17.01% |     0.75 |       64 | 54.41%     | ok               |
|          35 | 18.85%   | 39.39%             | -14.49% |     0.51 |       68 | 50.42%     | ok               |

## TGT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -20.25%  | -10.49%            | -44.85% |    -0.35 |       86 | 44.59%     | ok               |
|          30 | -17.61%  | -10.49%            | -40.57% |    -0.35 |       62 | 37.27%     | ok               |
|          25 | -18.60%  | -10.49%            | -43.64% |    -0.35 |       68 | 39.93%     | ok               |
|          15 | -25.34%  | -10.49%            | -42.87% |    -0.45 |       78 | 49.25%     | ok               |
|          45 | -19.82%  | -10.49%            | -32.34% |    -0.49 |       58 | 27.95%     | ok               |

## TIA-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 3.06%    | -90.17%            | -53.37% |     0.26 |       66 | 32.95%     | ok               |
|          40 | -4.77%   | -90.17%            | -48.24% |     0.16 |       68 | 27.59%     | ok               |
|          45 | -2.76%   | -90.17%            | -49.52% |     0.16 |       56 | 19.73%     | ok               |
|          50 | -0.89%   | -90.17%            | -48.70% |     0.14 |       36 | 12.45%     | ok               |
|          25 | -35.55%  | -90.17%            | -59.67% |    -0.11 |       89 | 45.02%     | ok               |

## TLT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -18.55%  | -11.24%            | -21.87% |    -1.37 |       70 | 34.11%     | ok               |
|          40 | -16.68%  | -11.24%            | -18.61% |    -1.51 |       56 | 23.63%     | ok               |
|          50 | -13.36%  | -11.24%            | -14.77% |    -1.55 |       32 | 15.47%     | ok               |
|          35 | -19.34%  | -11.24%            | -21.63% |    -1.62 |       64 | 28.29%     | ok               |
|          15 | -24.52%  | -11.24%            | -27.76% |    -1.66 |       75 | 42.10%     | ok               |

## TMO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 45.96%   | -0.84%             | -8.17%  |     1.03 |       44 | 32.78%     | ok               |
|          45 | 39.62%   | -0.84%             | -9.39%  |     0.87 |       48 | 37.77%     | ok               |
|          40 | 38.35%   | -0.84%             | -9.81%  |     0.83 |       51 | 42.43%     | ok               |
|          35 | 31.34%   | -0.84%             | -13.84% |     0.67 |       61 | 47.09%     | ok               |
|          30 | 29.61%   | -0.84%             | -18.85% |     0.62 |       61 | 52.41%     | ok               |

## TMUS Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 3.64%    | 10.51%             | -31.27% |     0.18 |       65 | 58.90%     | ok               |
|          30 | 2.49%    | 10.51%             | -27.01% |     0.15 |       70 | 46.92%     | ok               |
|          20 | -2.34%   | 10.51%             | -29.81% |     0.05 |       71 | 53.24%     | ok               |
|          25 | -5.61%   | 10.51%             | -32.65% |    -0.02 |       75 | 49.42%     | ok               |
|          50 | -5.74%   | 10.51%             | -28.89% |    -0.08 |       58 | 34.61%     | ok               |

## TRX-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 13.27%   | 35.24%             | -18.79% |     0.46 |       54 | 36.40%     | ok               |
|          30 | 9.99%    | 35.24%             | -22.90% |     0.35 |       70 | 48.47%     | ok               |
|          35 | 8.34%    | 35.24%             | -21.77% |     0.32 |       68 | 45.02%     | ok               |
|          20 | 8.68%    | 35.24%             | -25.45% |     0.31 |       63 | 55.56%     | ok               |
|          25 | 7.94%    | 35.24%             | -26.84% |     0.3  |       66 | 51.72%     | ok               |

## TSLA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 37.47%   | 96.63%             | -32.60% |     0.56 |       66 | 30.62%     | ok               |
|          40 | 17.69%   | 96.63%             | -45.90% |     0.37 |       67 | 35.77%     | ok               |
|          45 | -0.82%   | 96.63%             | -46.86% |     0.18 |       71 | 32.95%     | ok               |
|          35 | -15.97%  | 96.63%             | -54.51% |     0.02 |       78 | 38.60%     | ok               |
|          30 | -33.35%  | 96.63%             | -59.64% |    -0.2  |       76 | 42.76%     | ok               |

## TXN Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 13.40%   | 62.67%             | -45.45% |     0.33 |       66 | 33.28%     | ok               |
|          35 | -4.21%   | 62.67%             | -43.38% |     0.07 |       72 | 47.59%     | ok               |
|          15 | -6.94%   | 62.67%             | -39.48% |     0.06 |       65 | 61.23%     | ok               |
|          40 | -4.85%   | 62.67%             | -45.67% |     0.06 |       70 | 45.42%     | ok               |
|          20 | -7.53%   | 62.67%             | -38.98% |     0.05 |       64 | 56.91%     | ok               |

## UNH Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 29.76%   | -17.39%            | -26.96% |     0.52 |       74 | 51.75%     | ok               |
|          50 | 25.96%   | -17.39%            | -37.02% |     0.49 |       58 | 30.78%     | ok               |
|          35 | 27.07%   | -17.39%            | -28.32% |     0.49 |       66 | 46.42%     | ok               |
|          15 | 26.22%   | -17.39%            | -33.62% |     0.47 |       73 | 66.72%     | ok               |
|          25 | 15.46%   | -17.39%            | -29.39% |     0.35 |       74 | 57.07%     | ok               |

## UNI-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -26.21%  | -43.09%            | -63.24% |    -0.09 |       62 | 34.29%     | ok               |
|          45 | -31.30%  | -43.09%            | -57.91% |    -0.19 |       64 | 29.31%     | ok               |
|          50 | -30.32%  | -43.09%            | -53.71% |    -0.2  |       58 | 22.80%     | ok               |
|          35 | -42.73%  | -43.09%            | -68.27% |    -0.29 |       76 | 40.23%     | ok               |
|          20 | -77.19%  | -43.09%            | -83.47% |    -0.9  |      101 | 56.32%     | ok               |

## UPS Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -39.17%  | -32.94%            | -42.17% |    -0.75 |       86 | 48.09%     | ok               |
|          25 | -39.66%  | -32.94%            | -40.05% |    -0.78 |       78 | 44.76%     | ok               |
|          15 | -41.32%  | -32.94%            | -42.97% |    -0.8  |       88 | 51.91%     | ok               |
|          35 | -38.80%  | -32.94%            | -40.10% |    -0.8  |       67 | 34.44%     | ok               |
|          30 | -41.93%  | -32.94%            | -43.16% |    -0.87 |       72 | 40.27%     | ok               |

## USO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 12.37%   | 55.79%             | -33.25% |     0.32 |       48 | 27.29%     | ok               |
|          20 | 10.58%   | 55.79%             | -44.16% |     0.29 |       74 | 39.93%     | ok               |
|          25 | 7.47%    | 55.79%             | -43.43% |     0.25 |       68 | 37.27%     | ok               |
|          15 | 5.36%    | 55.79%             | -44.33% |     0.22 |       73 | 43.09%     | ok               |
|          30 | 0.23%    | 55.79%             | -43.35% |     0.14 |       70 | 34.28%     | ok               |

## VEA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 4.34%    | 44.88%             | -16.28% |     0.21 |       58 | 48.92%     | ok               |
|          20 | 0.13%    | 44.88%             | -17.70% |     0.06 |       59 | 46.26%     | ok               |
|          30 | -3.12%   | 44.88%             | -18.85% |    -0.08 |       58 | 41.93%     | ok               |
|          25 | -3.42%   | 44.88%             | -19.11% |    -0.09 |       57 | 44.26%     | ok               |
|          35 | -4.20%   | 44.88%             | -17.72% |    -0.13 |       56 | 40.93%     | ok               |

## VIXY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -48.04%  | -64.70%            | -69.78% |    -0.43 |       46 | 10.48%     | ok               |
|          45 | -57.65%  | -64.70%            | -75.03% |    -0.58 |       58 | 16.47%     | ok               |
|          40 | -65.68%  | -64.70%            | -80.72% |    -0.69 |       72 | 20.80%     | ok               |
|          35 | -69.78%  | -64.70%            | -84.29% |    -0.74 |       90 | 25.96%     | ok               |
|          15 | -76.29%  | -64.70%            | -89.47% |    -0.75 |       99 | 43.43%     | ok               |

## VNQ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -9.57%   | 14.83%             | -19.07% |    -0.42 |       58 | 28.95%     | ok               |
|          50 | -10.00%  | 14.83%             | -17.13% |    -0.46 |       54 | 26.46%     | ok               |
|          25 | -13.69%  | 14.83%             | -22.16% |    -0.53 |       66 | 41.26%     | ok               |
|          20 | -16.00%  | 14.83%             | -23.61% |    -0.62 |       69 | 44.09%     | ok               |
|          40 | -15.05%  | 14.83%             | -24.84% |    -0.67 |       72 | 32.45%     | ok               |

## VTI Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 15.46%   | 48.53%             | -13.96% |     0.54 |       64 | 53.24%     | ok               |
|          15 | 9.55%    | 48.53%             | -15.70% |     0.36 |       67 | 55.74%     | ok               |
|          25 | 2.12%    | 48.53%             | -16.10% |     0.13 |       60 | 51.25%     | ok               |
|          30 | -5.54%   | 48.53%             | -18.77% |    -0.14 |       70 | 49.25%     | ok               |
|          40 | -6.89%   | 48.53%             | -20.44% |    -0.22 |       70 | 42.10%     | ok               |

## VWO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -7.37%   | 43.58%             | -21.18% |    -0.26 |       56 | 29.95%     | ok               |
|          45 | -9.18%   | 43.58%             | -23.26% |    -0.33 |       58 | 32.45%     | ok               |
|          15 | -11.71%  | 43.58%             | -24.01% |    -0.36 |       74 | 47.92%     | ok               |
|          40 | -10.21%  | 43.58%             | -23.57% |    -0.37 |       68 | 35.11%     | ok               |
|          20 | -13.11%  | 43.58%             | -26.14% |    -0.43 |       71 | 45.59%     | ok               |

## VZ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -5.60%   | 18.15%             | -12.71% |    -0.14 |       52 | 25.79%     | ok               |
|          25 | -19.09%  | 18.15%             | -22.13% |    -0.52 |       79 | 43.26%     | ok               |
|          45 | -16.87%  | 18.15%             | -21.44% |    -0.53 |       66 | 29.45%     | ok               |
|          35 | -18.06%  | 18.15%             | -22.73% |    -0.55 |       61 | 35.27%     | ok               |
|          40 | -22.65%  | 18.15%             | -24.21% |    -0.75 |       66 | 32.61%     | ok               |

## WFC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | -11.10%  | 52.68%             | -22.54% |    -0.18 |       81 | 45.76%     | ok               |
|          50 | -8.37%   | 52.68%             | -18.29% |    -0.2  |       62 | 33.44%     | ok               |
|          20 | -18.09%  | 52.68%             | -29.87% |    -0.26 |       79 | 54.91%     | ok               |
|          30 | -20.37%  | 52.68%             | -29.78% |    -0.36 |       84 | 48.92%     | ok               |
|          25 | -23.81%  | 52.68%             | -33.38% |    -0.42 |       76 | 51.91%     | ok               |

## WIF-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 29.75%   | -75.63%            | -46.21% |     0.51 |       74 | 43.87%     | ok               |
|          20 | 26.38%   | -75.63%            | -40.67% |     0.48 |       67 | 41.00%     | ok               |
|          25 | -35.79%  | -75.63%            | -52.50% |    -0.07 |       71 | 37.74%     | ok               |
|          50 | -24.32%  | -75.63%            | -41.18% |    -0.22 |       42 | 12.26%     | ok               |
|          30 | -52.90%  | -75.63%            | -61.76% |    -0.39 |       72 | 33.91%     | ok               |

## WMT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 40.91%   | 83.66%             | -9.18%  |     1.18 |       40 | 39.60%     | ok               |
|          50 | 35.47%   | 83.66%             | -12.19% |     1.1  |       34 | 37.10%     | ok               |
|          40 | 29.18%   | 83.66%             | -13.41% |     0.87 |       46 | 40.93%     | ok               |
|          35 | 28.34%   | 83.66%             | -13.99% |     0.83 |       56 | 45.59%     | ok               |
|          15 | 14.98%   | 83.66%             | -25.74% |     0.41 |       72 | 59.73%     | ok               |

## XBI Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 7.87%    | 63.58%             | -16.08% |     0.28 |       58 | 33.94%     | ok               |
|          45 | 4.05%    | 63.58%             | -15.46% |     0.19 |       52 | 30.95%     | ok               |
|          35 | 0.49%    | 63.58%             | -16.96% |     0.09 |       64 | 37.77%     | ok               |
|          30 | -1.61%   | 63.58%             | -18.30% |     0.04 |       66 | 39.27%     | ok               |
|          50 | -4.48%   | 63.58%             | -15.97% |    -0.06 |       54 | 27.62%     | ok               |

## XLB Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -3.93%   | 14.96%             | -19.67% |    -0.1  |       54 | 29.78%     | ok               |
|          50 | -5.21%   | 14.96%             | -17.59% |    -0.17 |       42 | 25.62%     | ok               |
|          35 | -7.10%   | 14.96%             | -22.65% |    -0.22 |       56 | 33.11%     | ok               |
|          45 | -6.83%   | 14.96%             | -19.78% |    -0.23 |       42 | 26.96%     | ok               |
|          25 | -10.16%  | 14.96%             | -22.63% |    -0.32 |       60 | 38.60%     | ok               |

## XLC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 14.08%   | 38.82%             | -12.33% |     0.51 |       65 | 52.58%     | ok               |
|          25 | 11.27%   | 38.82%             | -12.31% |     0.42 |       64 | 54.41%     | ok               |
|          40 | 7.83%    | 38.82%             | -13.38% |     0.34 |       66 | 45.76%     | ok               |
|          35 | 7.01%    | 38.82%             | -13.38% |     0.3  |       64 | 49.92%     | ok               |
|          20 | 3.64%    | 38.82%             | -11.36% |     0.18 |       70 | 57.24%     | ok               |

## XLE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 0.56%    | 27.42%             | -25.98% |     0.09 |       54 | 35.94%     | ok               |
|          45 | -3.56%   | 27.42%             | -29.68% |    -0.03 |       60 | 37.94%     | ok               |
|          35 | -5.59%   | 27.42%             | -31.51% |    -0.06 |       65 | 42.60%     | ok               |
|          25 | -10.69%  | 27.42%             | -36.18% |    -0.18 |       83 | 48.42%     | ok               |
|          30 | -12.90%  | 27.42%             | -37.76% |    -0.26 |       75 | 45.42%     | ok               |

## XLF Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -3.33%   | 41.59%             | -18.01% |    -0.05 |       68 | 53.58%     | ok               |
|          15 | -7.33%   | 41.59%             | -19.58% |    -0.18 |       76 | 56.41%     | ok               |
|          25 | -10.07%  | 41.59%             | -23.22% |    -0.3  |       77 | 50.08%     | ok               |
|          30 | -11.53%  | 41.59%             | -23.61% |    -0.37 |       78 | 47.42%     | ok               |
|          35 | -19.45%  | 41.59%             | -27.41% |    -0.77 |       68 | 43.09%     | ok               |

## XLI Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 4.10%    | 51.42%             | -10.36% |     0.2  |       80 | 50.92%     | ok               |
|          20 | -0.08%   | 51.42%             | -12.74% |     0.05 |       73 | 45.76%     | ok               |
|          25 | -5.33%   | 51.42%             | -14.41% |    -0.16 |       70 | 43.76%     | ok               |
|          30 | -5.90%   | 51.42%             | -14.12% |    -0.19 |       72 | 42.76%     | ok               |
|          45 | -5.62%   | 51.42%             | -16.29% |    -0.2  |       70 | 34.11%     | ok               |

## XLK Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 85.57%   | 77.54%             | -14.75% |     1.33 |       45 | 51.75%     | ok               |
|          20 | 78.49%   | 77.54%             | -14.75% |     1.3  |       48 | 49.42%     | ok               |
|          25 | 74.85%   | 77.54%             | -14.75% |     1.3  |       42 | 47.25%     | ok               |
|          30 | 64.39%   | 77.54%             | -14.75% |     1.2  |       42 | 45.92%     | ok               |
|          35 | 46.04%   | 77.54%             | -13.61% |     0.97 |       54 | 43.26%     | ok               |

## XLM-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 26.14%   | -45.22%            | -38.97% |     0.48 |       44 | 27.39%     | ok               |
|          45 | 22.04%   | -45.22%            | -44.13% |     0.44 |       52 | 31.23%     | ok               |
|          30 | 7.13%    | -45.22%            | -50.48% |     0.29 |       67 | 45.40%     | ok               |
|          25 | 3.85%    | -45.22%            | -48.24% |     0.26 |       69 | 47.89%     | ok               |
|          20 | -4.36%   | -45.22%            | -55.41% |     0.18 |       68 | 50.19%     | ok               |

## XLP Threshold Sweep

|   threshold | return   | benchmark_return   | mdd    |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:-------|---------:|---------:|:-----------|:-----------------|
|          45 | 11.44%   | 12.64%             | -5.66% |     0.71 |       52 | 31.95%     | ok               |
|          40 | 10.81%   | 12.64%             | -7.32% |     0.66 |       68 | 35.94%     | ok               |
|          35 | 9.84%    | 12.64%             | -8.39% |     0.59 |       64 | 38.94%     | ok               |
|          50 | 8.39%    | 12.64%             | -6.08% |     0.55 |       56 | 30.28%     | ok               |
|          30 | 8.96%    | 12.64%             | -8.96% |     0.54 |       66 | 40.60%     | ok               |

## XLU Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 5.85%    | 36.91%             | -12.97% |     0.32 |       52 | 31.28%     | ok               |
|          45 | 4.45%    | 36.91%             | -14.27% |     0.25 |       54 | 32.28%     | ok               |
|          40 | 1.57%    | 36.91%             | -15.59% |     0.12 |       58 | 33.78%     | ok               |
|          35 | -4.35%   | 36.91%             | -19.71% |    -0.16 |       62 | 35.94%     | ok               |
|          30 | -5.24%   | 36.91%             | -20.40% |    -0.19 |       67 | 39.10%     | ok               |

## XLV Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -15.44%  | 12.68%             | -19.17% |    -0.77 |       66 | 34.28%     | ok               |
|          25 | -16.90%  | 12.68%             | -22.09% |    -0.83 |       68 | 36.44%     | ok               |
|          15 | -20.11%  | 12.68%             | -25.33% |    -0.97 |       81 | 41.43%     | ok               |
|          20 | -20.05%  | 12.68%             | -25.42% |    -1    |       73 | 38.27%     | ok               |
|          45 | -17.35%  | 12.68%             | -20.89% |    -1.03 |       56 | 24.96%     | ok               |

## XLY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 4.16%    | 31.34%             | -14.01% |     0.19 |       66 | 43.59%     | ok               |
|          35 | 2.48%    | 31.34%             | -12.94% |     0.14 |       68 | 41.10%     | ok               |
|          15 | 1.44%    | 31.34%             | -15.77% |     0.12 |       72 | 49.75%     | ok               |
|          20 | -1.24%   | 31.34%             | -19.25% |     0.04 |       65 | 46.42%     | ok               |
|          50 | -1.93%   | 31.34%             | -12.26% |    -0.02 |       54 | 29.62%     | ok               |

## XOM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 6.72%    | 38.91%             | -21.35% |     0.26 |       40 | 30.62%     | ok               |
|          25 | 6.83%    | 38.91%             | -19.90% |     0.26 |       55 | 38.60%     | ok               |
|          30 | 5.77%    | 38.91%             | -20.29% |     0.23 |       55 | 37.94%     | ok               |
|          45 | -0.16%   | 38.91%             | -23.33% |     0.07 |       46 | 32.11%     | ok               |
|          40 | -0.40%   | 38.91%             | -21.45% |     0.06 |       54 | 35.27%     | ok               |

## XRP-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 6.29%    | -58.05%            | -31.38% |     0.27 |       62 | 38.70%     | ok               |
|          40 | -5.00%   | -58.05%            | -33.91% |     0.11 |       52 | 32.95%     | ok               |
|          30 | -10.91%  | -58.05%            | -35.71% |     0.05 |       64 | 42.91%     | ok               |
|          45 | -15.61%  | -58.05%            | -36.27% |    -0.06 |       52 | 28.74%     | ok               |
|          20 | -31.73%  | -58.05%            | -49.05% |    -0.23 |       82 | 52.11%     | ok               |

## YFI-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -48.54%  | -61.41%            | -52.84% |    -0.77 |       60 | 28.16%     | ok               |
|          45 | -47.02%  | -61.41%            | -54.66% |    -0.92 |       70 | 22.80%     | ok               |
|          35 | -59.50%  | -61.41%            | -63.29% |    -0.94 |       65 | 35.44%     | ok               |
|          30 | -64.19%  | -61.41%            | -71.12% |    -1.03 |       81 | 40.61%     | ok               |
|          15 | -69.51%  | -61.41%            | -74.96% |    -1.08 |       89 | 53.64%     | ok               |

## ZEC-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 113.92%  | 1344.17%           | -24.66% |     0.86 |       44 | 25.10%     | ok               |
|          35 | 83.05%   | 1344.17%           | -44.34% |     0.73 |       52 | 31.23%     | ok               |
|          25 | 60.16%   | 1344.17%           | -52.17% |     0.63 |       60 | 41.00%     | ok               |
|          50 | 47.05%   | 1344.17%           | -34.17% |     0.56 |       46 | 22.61%     | ok               |
|          40 | 45.78%   | 1344.17%           | -48.16% |     0.56 |       54 | 28.93%     | ok               |
