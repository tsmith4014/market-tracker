# Market Tracker Backtest Report

_Generated: 2026-06-23T01:33:01+00:00_

## Data Sources

- Crypto: Kraken -> Coinbase -> CoinGecko OHLC -> CoinPaprika fallback chain.
- Stocks / ETFs / indices: Stooq -> Yahoo Finance fallback chain.
- Data rows are generated from real market APIs. Mock OHLCV rows are not generated.

## Data Freshness

- Rows: **92,419**
- Symbols: **161**
- Date range: **2024-01-29** to **2026-06-23**

## Latest Signals

| symbol     | date                |         close |   composite_score | signal   | data_source   |
|:-----------|:--------------------|--------------:|------------------:|:---------|:--------------|
| AMAT       | 2026-06-22 00:00:00 |   640.18      |         71.75     | LONG     | Yahoo Finance |
| BAC        | 2026-06-22 00:00:00 |    57.37      |         62.25     | LONG     | Yahoo Finance |
| BLK        | 2026-06-22 00:00:00 |  1051.74      |         51.1667   | LONG     | Yahoo Finance |
| C          | 2026-06-22 00:00:00 |   145.67      |         70.75     | LONG     | Yahoo Finance |
| CSCO       | 2026-06-22 00:00:00 |   121.53      |         47.0833   | LONG     | Yahoo Finance |
| DXY-INDEX  | 2026-06-22 00:00:00 |   101.041     |         82.2581   | LONG     | Yahoo Finance |
| GE         | 2026-06-22 00:00:00 |   355.12      |         56.4167   | LONG     | Yahoo Finance |
| GS         | 2026-06-22 00:00:00 |  1106.37      |         51.0833   | LONG     | Yahoo Finance |
| HD         | 2026-06-22 00:00:00 |   326.62      |         33.9167   | LONG     | Yahoo Finance |
| ITA        | 2026-06-22 00:00:00 |   235.51      |         57.5833   | LONG     | Yahoo Finance |
| JPM        | 2026-06-22 00:00:00 |   331.48      |         61.75     | LONG     | Yahoo Finance |
| LLY        | 2026-06-22 00:00:00 |  1102.08      |         50.25     | LONG     | Yahoo Finance |
| LRCX       | 2026-06-22 00:00:00 |   409.54      |         71.75     | LONG     | Yahoo Finance |
| MS         | 2026-06-22 00:00:00 |   227.09      |         71.9167   | LONG     | Yahoo Finance |
| PG         | 2026-06-22 00:00:00 |   147.68      |         53.5833   | LONG     | Yahoo Finance |
| RTX        | 2026-06-22 00:00:00 |   181.83      |         46.6667   | LONG     | Yahoo Finance |
| SBUX       | 2026-06-22 00:00:00 |   100.15      |         47.4167   | LONG     | Yahoo Finance |
| SCHW       | 2026-06-22 00:00:00 |    92.03      |         34.4167   | LONG     | Yahoo Finance |
| TIA-USD    | 2026-06-23 00:00:00 |     0.3896    |         45.0833   | LONG     | Kraken API    |
| TRX-USD    | 2026-06-23 00:00:00 |     0.333206  |         71.4167   | LONG     | Kraken API    |
| UNH        | 2026-06-22 00:00:00 |   406.68      |         61.25     | LONG     | Yahoo Finance |
| UPS        | 2026-06-22 00:00:00 |   107.24      |         40.4167   | LONG     | Yahoo Finance |
| WFC        | 2026-06-22 00:00:00 |    83.84      |         63.4167   | LONG     | Yahoo Finance |
| XLF        | 2026-06-22 00:00:00 |    53.7       |         63.4167   | LONG     | Yahoo Finance |
| XLM-USD    | 2026-06-23 00:00:00 |     0.200826  |         35.25     | LONG     | Kraken API    |
| AAPL       | 2026-06-22 00:00:00 |   297.01      |         -1.58333  | NEUTRAL  | Yahoo Finance |
| AAVE-USD   | 2026-06-23 00:00:00 |    75.24      |         11.3333   | NEUTRAL  | Kraken API    |
| ABBV       | 2026-06-22 00:00:00 |   230.01      |         30.3333   | NEUTRAL  | Yahoo Finance |
| ADA-USD    | 2026-06-23 00:00:00 |     0.159183  |        -20.6667   | NEUTRAL  | Kraken API    |
| AGG        | 2026-06-22 00:00:00 |    98.63      |        -32.9167   | NEUTRAL  | Yahoo Finance |
| ALGO-USD   | 2026-06-23 00:00:00 |     0.09028   |        -11.5      | NEUTRAL  | Kraken API    |
| AMD        | 2026-06-22 00:00:00 |   551.63      |         43        | NEUTRAL  | Yahoo Finance |
| AMGN       | 2026-06-22 00:00:00 |   344.72      |         69.9167   | NEUTRAL  | Yahoo Finance |
| APT-USD    | 2026-06-23 00:00:00 |     0.6576    |        -11.5      | NEUTRAL  | Kraken API    |
| ARB-USD    | 2026-06-23 00:00:00 |     0.0831    |         -4.83333  | NEUTRAL  | Kraken API    |
| ARKK       | 2026-06-22 00:00:00 |    78.43      |         16.25     | NEUTRAL  | Yahoo Finance |
| ATOM-USD   | 2026-06-23 00:00:00 |     1.8026    |        -31.0833   | NEUTRAL  | Kraken API    |
| AVAX-USD   | 2026-06-23 00:00:00 |     6.27      |        -17        | NEUTRAL  | Kraken API    |
| AVGO       | 2026-06-22 00:00:00 |   392.13      |        -47.25     | NEUTRAL  | Yahoo Finance |
| BA         | 2026-06-22 00:00:00 |   220.83      |        -15.4167   | NEUTRAL  | Yahoo Finance |
| BND        | 2026-06-22 00:00:00 |    73.14      |        -40.4167   | NEUTRAL  | Yahoo Finance |
| BONK-USD   | 2026-06-23 00:00:00 |     4.577e-06 |         -1.33333  | NEUTRAL  | Kraken API    |
| BTC-USD    | 2026-06-23 00:00:00 | 64175.3       |          0.666667 | NEUTRAL  | Kraken API    |
| CAT        | 2026-06-22 00:00:00 |  1022.28      |         60        | NEUTRAL  | Yahoo Finance |
| CL         | 2026-06-22 00:00:00 |    88.67      |         39.25     | NEUTRAL  | Yahoo Finance |
| COMP-USD   | 2026-06-23 00:00:00 |    17.7       |        -12.6667   | NEUTRAL  | Kraken API    |
| COP        | 2026-06-22 00:00:00 |   109.7       |        -20.5833   | NEUTRAL  | Yahoo Finance |
| COST       | 2026-06-22 00:00:00 |   951.35      |        -10.6667   | NEUTRAL  | Yahoo Finance |
| CRV-USD    | 2026-06-23 00:00:00 |     0.21078   |        -19.8333   | NEUTRAL  | Kraken API    |
| CVX        | 2026-06-22 00:00:00 |   175.06      |        -49.75     | NEUTRAL  | Yahoo Finance |
| DASH-USD   | 2026-06-23 00:00:00 |    34.846     |        -47.9167   | NEUTRAL  | Kraken API    |
| DBC        | 2026-06-22 00:00:00 |    27.41      |        -14.8333   | NEUTRAL  | Yahoo Finance |
| DE         | 2026-06-22 00:00:00 |   598.59      |         58.25     | NEUTRAL  | Yahoo Finance |
| DIA        | 2026-06-22 00:00:00 |   517.08      |         43.8333   | NEUTRAL  | Yahoo Finance |
| DIS        | 2026-06-22 00:00:00 |   102.45      |         19.3333   | NEUTRAL  | Yahoo Finance |
| DOGE-USD   | 2026-06-23 00:00:00 |     0.0824519 |        -22.4167   | NEUTRAL  | Kraken API    |
| DOT-USD    | 2026-06-23 00:00:00 |     0.9351    |        -18.6667   | NEUTRAL  | Kraken API    |
| EEM        | 2026-06-22 00:00:00 |    71.21      |         41.8333   | NEUTRAL  | Yahoo Finance |
| EFA        | 2026-06-22 00:00:00 |   104.58      |         14        | NEUTRAL  | Yahoo Finance |
| EOG        | 2026-06-22 00:00:00 |   132.83      |        -24.3333   | NEUTRAL  | Yahoo Finance |
| ETC-USD    | 2026-06-23 00:00:00 |     7.181     |         -4.5      | NEUTRAL  | Kraken API    |
| ETH-USD    | 2026-06-23 00:00:00 |  1730.9       |        -12.6667   | NEUTRAL  | Kraken API    |
| EWJ        | 2026-06-22 00:00:00 |    96.97      |         56.3333   | NEUTRAL  | Yahoo Finance |
| FCX        | 2026-06-22 00:00:00 |    69.21      |         48.8333   | NEUTRAL  | Yahoo Finance |
| FIL-USD    | 2026-06-23 00:00:00 |     0.797     |          2.66667  | NEUTRAL  | Kraken API    |
| GRT-USD    | 2026-06-23 00:00:00 |     0.01937   |         -9.5      | NEUTRAL  | Kraken API    |
| HBAR-USD   | 2026-06-23 00:00:00 |     0.07869   |        -20.75     | NEUTRAL  | Kraken API    |
| HON        | 2026-06-22 00:00:00 |   228.11      |         40        | NEUTRAL  | Yahoo Finance |
| HYG        | 2026-06-22 00:00:00 |    79.94      |         -1.25     | NEUTRAL  | Yahoo Finance |
| ICP-USD    | 2026-06-23 00:00:00 |     2.257     |        -34.0833   | NEUTRAL  | Kraken API    |
| IEF        | 2026-06-22 00:00:00 |    94         |        -42.6667   | NEUTRAL  | Yahoo Finance |
| IEMG       | 2026-06-22 00:00:00 |    86         |         41.8333   | NEUTRAL  | Yahoo Finance |
| INJ-USD    | 2026-06-23 00:00:00 |     4.802     |        -59.5      | NEUTRAL  | Kraken API    |
| INTC       | 2026-06-22 00:00:00 |   140.94      |         63.8333   | NEUTRAL  | Yahoo Finance |
| IWM        | 2026-06-22 00:00:00 |   298.18      |         45.1667   | NEUTRAL  | Yahoo Finance |
| JNJ        | 2026-06-22 00:00:00 |   231.29      |         19        | NEUTRAL  | Yahoo Finance |
| KO         | 2026-06-22 00:00:00 |    79.53      |         20.5      | NEUTRAL  | Yahoo Finance |
| LDO-USD    | 2026-06-23 00:00:00 |     0.267     |         -4.83333  | NEUTRAL  | Kraken API    |
| LIN        | 2026-06-22 00:00:00 |   516.71      |         62.8333   | NEUTRAL  | Yahoo Finance |
| LINK-USD   | 2026-06-23 00:00:00 |     7.88772   |         -1        | NEUTRAL  | Kraken API    |
| LTC-USD    | 2026-06-23 00:00:00 |    44.63      |          0.666667 | NEUTRAL  | Kraken API    |
| MCD        | 2026-06-22 00:00:00 |   270.1       |        -42.6667   | NEUTRAL  | Yahoo Finance |
| META       | 2026-06-22 00:00:00 |   563.85      |        -67.8333   | NEUTRAL  | Yahoo Finance |
| MPC        | 2026-06-22 00:00:00 |   247.29      |          7.66667  | NEUTRAL  | Yahoo Finance |
| MRK        | 2026-06-22 00:00:00 |   115.48      |         -8.66667  | NEUTRAL  | Yahoo Finance |
| MU         | 2026-06-22 00:00:00 |  1211.38      |         54.3333   | NEUTRAL  | Yahoo Finance |
| NEAR-USD   | 2026-06-23 00:00:00 |     2.057     |         13.6667   | NEUTRAL  | Kraken API    |
| NEM        | 2026-06-22 00:00:00 |   101.8       |         -4.16667  | NEUTRAL  | Yahoo Finance |
| NKE        | 2026-06-22 00:00:00 |    43.19      |        -65        | NEUTRAL  | Yahoo Finance |
| NVDA       | 2026-06-22 00:00:00 |   208.65      |        -26.8333   | NEUTRAL  | Yahoo Finance |
| OP-USD     | 2026-06-23 00:00:00 |     0.1011    |        -17.75     | NEUTRAL  | Kraken API    |
| OXY        | 2026-06-22 00:00:00 |    52         |        -14.8333   | NEUTRAL  | Yahoo Finance |
| PEP        | 2026-06-22 00:00:00 |   140.71      |        -19.5      | NEUTRAL  | Yahoo Finance |
| PEPE-USD   | 2026-06-23 00:00:00 |     2.821e-06 |         -2.83333  | NEUTRAL  | Kraken API    |
| PFE        | 2026-06-22 00:00:00 |    25.08      |        -55.5      | NEUTRAL  | Yahoo Finance |
| PM         | 2026-06-22 00:00:00 |   173.17      |         15        | NEUTRAL  | Yahoo Finance |
| POL-USD    | 2026-06-23 00:00:00 |     0.07871   |          0.666667 | NEUTRAL  | Kraken API    |
| QCOM       | 2026-06-22 00:00:00 |   221.9       |         31.6667   | NEUTRAL  | Yahoo Finance |
| QQQ        | 2026-06-22 00:00:00 |   737.95      |         28.3333   | NEUTRAL  | Yahoo Finance |
| RENDER-USD | 2026-06-23 00:00:00 |     1.609     |        -45.25     | NEUTRAL  | Kraken API    |
| SHIB-USD   | 2026-06-23 00:00:00 |     4.66e-06  |        -22.4167   | NEUTRAL  | Kraken API    |
| SHY        | 2026-06-22 00:00:00 |    81.91      |        -43.25     | NEUTRAL  | Yahoo Finance |
| SKY-USD    | 2026-06-23 00:00:00 |     0.05976   |         17.3333   | NEUTRAL  | Kraken API    |
| SLB        | 2026-06-22 00:00:00 |    47.95      |        -13.5      | NEUTRAL  | Yahoo Finance |
| SMH        | 2026-06-22 00:00:00 |   668.91      |         50.8333   | NEUTRAL  | Yahoo Finance |
| SNX-USD    | 2026-06-23 00:00:00 |     0.2454    |         -0.833333 | NEUTRAL  | Kraken API    |
| SOL-USD    | 2026-06-23 00:00:00 |    71.85      |          0.666667 | NEUTRAL  | Kraken API    |
| SOXX       | 2026-06-22 00:00:00 |   655.01      |         56.3333   | NEUTRAL  | Yahoo Finance |
| SPY        | 2026-06-22 00:00:00 |   744.39      |         11.4167   | NEUTRAL  | Yahoo Finance |
| SUSHI-USD  | 2026-06-23 00:00:00 |     0.1712    |        -16.0833   | NEUTRAL  | Kraken API    |
| TGT        | 2026-06-22 00:00:00 |   129.73      |         59.1667   | NEUTRAL  | Yahoo Finance |
| TLT        | 2026-06-22 00:00:00 |    86.09      |         25        | NEUTRAL  | Yahoo Finance |
| TMUS       | 2026-06-22 00:00:00 |   180.06      |        -29.25     | NEUTRAL  | Yahoo Finance |
| TSLA       | 2026-06-22 00:00:00 |   405.05      |        -15.5      | NEUTRAL  | Yahoo Finance |
| TXN        | 2026-06-22 00:00:00 |   332.28      |         54.3333   | NEUTRAL  | Yahoo Finance |
| UNI-USD    | 2026-06-23 00:00:00 |     2.9971    |         21.3333   | NEUTRAL  | Kraken API    |
| USO        | 2026-06-22 00:00:00 |   112.69      |        -18.8333   | NEUTRAL  | Yahoo Finance |
| VEA        | 2026-06-22 00:00:00 |    72.39      |         43.3333   | NEUTRAL  | Yahoo Finance |
| VNQ        | 2026-06-22 00:00:00 |    96.59      |         52        | NEUTRAL  | Yahoo Finance |
| VTI        | 2026-06-22 00:00:00 |   368.81      |         14.9167   | NEUTRAL  | Yahoo Finance |
| VWO        | 2026-06-22 00:00:00 |    61.24      |         32.6667   | NEUTRAL  | Yahoo Finance |
| VZ         | 2026-06-22 00:00:00 |    45.36      |        -29.8333   | NEUTRAL  | Yahoo Finance |
| WIF-USD    | 2026-06-23 00:00:00 |     0.1647    |         -1.33333  | NEUTRAL  | Kraken API    |
| WMT        | 2026-06-22 00:00:00 |   117.18      |         29.6667   | NEUTRAL  | Yahoo Finance |
| XBI        | 2026-06-22 00:00:00 |   145.86      |         66.8333   | NEUTRAL  | Yahoo Finance |
| XLB        | 2026-06-22 00:00:00 |    51.62      |         61.1667   | NEUTRAL  | Yahoo Finance |
| XLE        | 2026-06-22 00:00:00 |    54.06      |        -22.75     | NEUTRAL  | Yahoo Finance |
| XLI        | 2026-06-22 00:00:00 |   181.8       |         64.8333   | NEUTRAL  | Yahoo Finance |
| XLK        | 2026-06-22 00:00:00 |   192.15      |         28.6667   | NEUTRAL  | Yahoo Finance |
| XLP        | 2026-06-22 00:00:00 |    82.18      |         -6.41667  | NEUTRAL  | Yahoo Finance |
| XLU        | 2026-06-22 00:00:00 |    44.72      |         23.9167   | NEUTRAL  | Yahoo Finance |
| XLV        | 2026-06-22 00:00:00 |   150.06      |         10.75     | NEUTRAL  | Yahoo Finance |
| XLY        | 2026-06-22 00:00:00 |   114.94      |        -64.0833   | NEUTRAL  | Yahoo Finance |
| XOM        | 2026-06-22 00:00:00 |   138.47      |        -22.75     | NEUTRAL  | Yahoo Finance |
| XRP-USD    | 2026-06-23 00:00:00 |     1.13134   |        -11.1667   | NEUTRAL  | Kraken API    |
| YFI-USD    | 2026-06-23 00:00:00 |  1800.7       |        -29.9167   | NEUTRAL  | Kraken API    |
| ZEC-USD    | 2026-06-23 00:00:00 |   443.67      |         21.75     | NEUTRAL  | Kraken API    |
| ADBE       | 2026-06-22 00:00:00 |   194.9       |        -63.0833   | SHORT    | Yahoo Finance |
| AMZN       | 2026-06-22 00:00:00 |   232.79      |        -39.3333   | SHORT    | Yahoo Finance |
| BCH-USD    | 2026-06-23 00:00:00 |   196.33      |        -37        | SHORT    | Kraken API    |
| BITO       | 2026-06-22 00:00:00 |     8.76      |        -32.75     | SHORT    | Yahoo Finance |
| CMCSA      | 2026-06-22 00:00:00 |    22.32      |        -47.5833   | SHORT    | Yahoo Finance |
| CRM        | 2026-06-22 00:00:00 |   150.12      |        -60.5833   | SHORT    | Yahoo Finance |
| FET-USD    | 2026-06-23 00:00:00 |     0.185     |        -32        | SHORT    | Kraken API    |
| FXI        | 2026-06-22 00:00:00 |    33.43      |        -48.25     | SHORT    | Yahoo Finance |
| GDX        | 2026-06-22 00:00:00 |    81.44      |        -34.9167   | SHORT    | Yahoo Finance |
| GDXJ       | 2026-06-22 00:00:00 |   106.12      |        -36.9167   | SHORT    | Yahoo Finance |
| GLD        | 2026-06-22 00:00:00 |   384.59      |        -52.75     | SHORT    | Yahoo Finance |
| GOOGL      | 2026-06-22 00:00:00 |   349.68      |        -35.8333   | SHORT    | Yahoo Finance |
| IBIT       | 2026-06-22 00:00:00 |    36.5       |        -32.75     | SHORT    | Yahoo Finance |
| IBM        | 2026-06-22 00:00:00 |   252.22      |        -51.9167   | SHORT    | Yahoo Finance |
| INTU       | 2026-06-22 00:00:00 |   257.77      |        -61.0833   | SHORT    | Yahoo Finance |
| MSFT       | 2026-06-22 00:00:00 |   367.34      |        -61.5833   | SHORT    | Yahoo Finance |
| NFLX       | 2026-06-22 00:00:00 |    72.88      |        -63.3333   | SHORT    | Yahoo Finance |
| NOW        | 2026-06-22 00:00:00 |    93.01      |        -60.5833   | SHORT    | Yahoo Finance |
| ORCL       | 2026-06-22 00:00:00 |   175.07      |        -61.0833   | SHORT    | Yahoo Finance |
| SLV        | 2026-06-22 00:00:00 |    58.91      |        -52.75     | SHORT    | Yahoo Finance |
| T          | 2026-06-22 00:00:00 |    22.1       |        -59.4167   | SHORT    | Yahoo Finance |
| TMO        | 2026-06-22 00:00:00 |   464.01      |        -51.25     | SHORT    | Yahoo Finance |
| VIXY       | 2026-06-22 00:00:00 |    21.85      |        -32.25     | SHORT    | Yahoo Finance |
| XLC        | 2026-06-22 00:00:00 |   106.86      |        -59.5833   | SHORT    | Yahoo Finance |

## Edge Summary

- Symbols with trades: **160** of 160
- Beat buy-and-hold: **36.25%** of traded symbols
- Positive return: **34.38%** of traded symbols
- Median strategy return: **-9.22%** (benchmark **12.73%**)
- Median excess vs benchmark: **-24.60%**
- Median Sharpe: **-0.07**
- Median exposure: **44.70%**

> Edge is real only if both _beat buy-and-hold_ and _median excess_ are convincingly positive across many symbols. Treat a single high-return symbol as noise.

## Portfolio Backtest

Actual capital-allocation books (not per-symbol averages). Benchmarks: `equal_weight_buyhold` (whole tracked universe), `spy_buyhold` (100% SPY), and `sixty_forty` (60% SPY / 40% AGG). `high_conf_voltarget` inverse-vol-weights the HIGH-confidence book; `conviction_long_short` is market-neutral. Judge on **Sharpe** and **max_drawdown** out-of-sample, not raw return: a fully-invested long book wins on return in a bull market but carries all the risk.

| strategy              | scope         | ann_return   | ann_vol   |   sharpe | max_drawdown   | total_return   |   avg_gross_exposure |
|:----------------------|:--------------|:-------------|:----------|---------:|:---------------|:---------------|---------------------:|
| equal_weight_buyhold  | full          | -10.75%      | 33.74%    |    -0.32 | -57.06%        | -39.56%        |                 1    |
| equal_weight_buyhold  | out_of_sample | -7.97%       | 34.21%    |    -0.23 | -39.63%        | -13.70%        |                 1    |
| all_signals_ew        | full          | -8.91%       | 28.17%    |    -0.32 | -59.96%        | -32.53%        |                 1    |
| all_signals_ew        | out_of_sample | 8.37%        | 28.43%    |     0.29 | -23.99%        | 4.76%          |                 1    |
| high_conf_ew          | full          | 3.86%        | 32.87%    |     0.12 | -43.07%        | -4.44%         |                 0.89 |
| high_conf_ew          | out_of_sample | 28.11%       | 36.24%    |     0.78 | -20.67%        | 26.07%         |                 0.89 |
| high_conf_voltarget   | full          | 3.87%        | 30.56%    |     0.13 | -35.11%        | -2.19%         |                 0.89 |
| high_conf_voltarget   | out_of_sample | 19.97%       | 34.37%    |     0.58 | -16.94%        | 16.42%         |                 0.89 |
| conviction_long_short | full          | -9.86%       | 23.54%    |    -0.42 | -36.64%        | -32.03%        |                 0.97 |
| conviction_long_short | out_of_sample | -7.90%       | 27.16%    |    -0.29 | -21.14%        | -11.66%        |                 0.97 |
| spy_buyhold           | full          | 7.74%        | 13.37%    |     0.58 | -17.81%        | 23.23%         |                 0.78 |
| spy_buyhold           | out_of_sample | -2.59%       | 9.98%     |    -0.26 | -14.83%        | -3.24%         |                 0.78 |
| sixty_forty           | full          | 4.40%        | 8.47%     |     0.52 | -10.80%        | 13.12%         |                 0.78 |
| sixty_forty           | out_of_sample | -2.58%       | 6.50%     |    -0.4  | -10.06%        | -2.94%         |                 0.78 |

## Walk-Forward Robustness

Each book measured across contiguous time folds (each a different regime). A book has durable edge only if `mean_sharpe` is positive, `min_sharpe` isn't deeply negative, and `pct_positive_folds` is high — a single great fold doesn't count. `fold_sharpes` lists each fold oldest-to-newest.

| strategy              |   n_folds |   mean_sharpe |   median_sharpe |   min_sharpe | pct_positive_folds   | mean_return   | fold_sharpes                |
|:----------------------|----------:|--------------:|----------------:|-------------:|:---------------------|:--------------|:----------------------------|
| equal_weight_buyhold  |         5 |         -0.09 |           -0.11 |        -1.64 | 40.00%               | -7.25%        | 1.08;-1.64;0.95;-0.73;-0.11 |
| all_signals_ew        |         5 |         -0.21 |            0.17 |        -1.24 | 60.00%               | -6.31%        | 0.17;0.54;-1.24;-1.23;0.69  |
| high_conf_ew          |         5 |          0.33 |           -0.09 |        -0.5  | 40.00%               | -0.25%        | 1.29;-0.10;-0.50;-0.09;1.06 |
| high_conf_voltarget   |         5 |          0.41 |            0.13 |        -0.58 | 80.00%               | -0.02%        | 1.94;0.13;-0.58;0.01;0.53   |
| conviction_long_short |         5 |         -0.43 |           -0.28 |        -1.4  | 40.00%               | -7.16%        | -1.40;0.25;-0.28;-0.74;0.04 |
| spy_buyhold           |         5 |          0.6  |            0.23 |         0.03 | 100.00%              | 4.37%         | 1.25;1.44;0.23;0.06;0.03    |
| sixty_forty           |         5 |          0.53 |            0.24 |        -0.19 | 80.00%               | 2.54%         | 1.36;1.05;0.24;0.17;-0.19   |

## Strategy Comparison

Each decision rule backtested over the same data. `out_of_sample` is the most recent ~35% of each symbol's history (unseen tail). A rule has real edge only if `median_excess` and `beat_benchmark_pct` stay positive out-of-sample, not just full-sample.

| strategy        | scope         |   symbols | beat_benchmark_pct   | positive_pct   | median_return   | median_benchmark   | median_excess   |   median_sharpe |   total_trades |
|:----------------|:--------------|----------:|:---------------------|:---------------|:----------------|:-------------------|:----------------|----------------:|---------------:|
| trend           | full          |       160 | 36.25%               | 34.38%         | -9.22%          | 12.73%             | -24.60%         |           -0.07 |          11204 |
| trend           | out_of_sample |       160 | 37.50%               | 53.75%         | 3.92%           | 3.42%              | -7.74%          |            0.38 |           3926 |
| mean_reversion  | full          |       157 | 42.68%               | 49.04%         | -0.10%          | 12.50%             | -14.59%         |           -0.01 |           1244 |
| mean_reversion  | out_of_sample |       128 | 48.44%               | 57.81%         | 0.33%           | 0.43%              | -2.01%          |            0.67 |            474 |
| regime_adaptive | full          |       160 | 36.88%               | 34.38%         | -9.10%          | 12.73%             | -24.02%         |           -0.08 |          11479 |
| regime_adaptive | out_of_sample |       160 | 36.88%               | 53.75%         | 4.62%           | 3.42%              | -7.89%          |            0.4  |           4029 |

## Signal Calibration

Realized forward return in the signal's direction, grouped by confidence. HIGH should outrank LOW for the confidence score to be meaningful.

| confidence_level   |   horizon |     n | mean_return   | median_return   | win_rate   |
|:-------------------|----------:|------:|:--------------|:----------------|:-----------|
| HIGH               |         5 |  8188 | 0.18%         | 0.13%           | 52.28%     |
| MEDIUM             |         5 | 29209 | 0.08%         | 0.11%           | 51.19%     |
| LOW                |         5 |  3279 | -0.59%        | -0.51%          | 44.92%     |
| ALL                |         5 | 40676 | 0.05%         | 0.07%           | 50.91%     |
| HIGH               |        10 |  8154 | 0.50%         | 0.19%           | 52.28%     |
| MEDIUM             |        10 | 29002 | 0.24%         | 0.15%           | 51.26%     |
| LOW                |        10 |  3256 | -0.87%        | -0.75%          | 45.15%     |
| ALL                |        10 | 40412 | 0.20%         | 0.11%           | 50.97%     |
| HIGH               |        20 |  8067 | 0.91%         | 0.51%           | 53.90%     |
| MEDIUM             |        20 | 28453 | 0.93%         | 0.64%           | 53.70%     |
| LOW                |        20 |  3209 | -0.62%        | -0.51%          | 47.09%     |
| ALL                |        20 | 39729 | 0.80%         | 0.54%           | 53.21%     |

## Backtest Summary

### Data Quality / Signal Availability

- **ok**: 160 symbols

| symbol     |   trades | return   | benchmark_return   | mdd     |   sharpe | exposure   | skipped_reason   |
|:-----------|---------:|:---------|:-------------------|:--------|---------:|:-----------|:-----------------|
| AAPL       |       63 | 13.72%   | 54.91%             | -20.65% |     0.37 | 48.59%     | ok               |
| AAVE-USD   |       76 | -58.88%  | -76.12%            | -68.72% |    -0.67 | 36.40%     | ok               |
| ABBV       |       64 | -13.84%  | 40.33%             | -30.55% |    -0.26 | 48.42%     | ok               |
| ADA-USD    |       84 | -83.00%  | -85.57%            | -89.69% |    -0.67 | 46.17%     | ok               |
| ADBE       |       68 | -22.17%  | -69.07%            | -38.01% |    -0.22 | 57.24%     | ok               |
| AGG        |       69 | -6.61%   | 0.17%              | -10.16% |    -1.1  | 31.11%     | ok               |
| ALGO-USD   |       86 | -50.43%  | -79.72%            | -53.13% |    -0.57 | 38.12%     | ok               |
| AMAT       |       69 | -12.21%  | 279.97%            | -57.21% |     0    | 53.41%     | ok               |
| AMD        |       56 | 0.89%    | 210.20%            | -46.37% |     0.22 | 37.77%     | ok               |
| AMGN       |       71 | -20.36%  | 9.98%              | -34.14% |    -0.41 | 47.59%     | ok               |
| AMZN       |       74 | -33.84%  | 44.36%             | -42.48% |    -0.99 | 38.27%     | ok               |
| APT-USD    |       76 | -26.57%  | -92.94%            | -69.96% |    -0    | 44.25%     | ok               |
| ARB-USD    |       68 | -0.31%   | -89.16%            | -62.67% |     0.24 | 39.27%     | ok               |
| ARKK       |       81 | -33.45%  | 63.02%             | -35.93% |    -0.59 | 39.10%     | ok               |
| ATOM-USD   |       90 | -68.06%  | -72.66%            | -73.96% |    -1.13 | 44.44%     | ok               |
| AVAX-USD   |       74 | -34.19%  | -84.01%            | -60.45% |    -0.24 | 39.66%     | ok               |
| AVGO       |       60 | 30.81%   | 222.01%            | -35.76% |     0.49 | 45.09%     | ok               |
| BA         |       69 | 5.13%    | 7.62%              | -30.56% |     0.21 | 49.58%     | ok               |
| BAC        |       78 | -13.29%  | 70.69%             | -27.64% |    -0.3  | 47.09%     | ok               |
| BCH-USD    |       76 | 1.25%    | -57.87%            | -53.87% |     0.22 | 47.89%     | ok               |
| BITO       |       78 | 4.43%    | -57.97%            | -42.82% |     0.23 | 40.77%     | ok               |
| BLK        |       75 | -6.34%   | 33.35%             | -21.68% |    -0.12 | 43.09%     | ok               |
| BND        |       65 | -7.32%   | 0.21%              | -9.89%  |    -1.18 | 32.28%     | ok               |
| BONK-USD   |       66 | 59.52%   | -86.36%            | -43.77% |     0.67 | 41.76%     | ok               |
| BTC-USD    |       70 | 6.41%    | -38.52%            | -23.38% |     0.25 | 51.15%     | ok               |
| C          |       81 | -22.70%  | 169.21%            | -37.02% |    -0.41 | 50.75%     | ok               |
| CAT        |       70 | 34.32%   | 237.11%            | -21.02% |     0.62 | 56.74%     | ok               |
| CL         |       60 | 13.47%   | 5.61%              | -14.32% |     0.48 | 47.75%     | ok               |
| CMCSA      |       82 | -38.25%  | -48.35%            | -40.02% |    -0.99 | 44.26%     | ok               |
| COMP-USD   |       89 | -36.73%  | -78.99%            | -58.43% |    -0.21 | 45.02%     | ok               |
| COP        |       73 | -24.21%  | -1.70%             | -43.77% |    -0.45 | 40.27%     | ok               |
| COST       |       60 | 4.54%    | 37.08%             | -29.73% |     0.2  | 46.42%     | ok               |
| CRM        |       65 | -35.46%  | -47.85%            | -41.46% |    -0.72 | 43.76%     | ok               |
| CRV-USD    |       62 | -0.75%   | -77.01%            | -39.89% |     0.22 | 34.29%     | ok               |
| CSCO       |       61 | 23.86%   | 132.42%            | -21.79% |     0.52 | 50.58%     | ok               |
| CVX        |       69 | -14.47%  | 17.43%             | -26.75% |    -0.36 | 40.93%     | ok               |
| DASH-USD   |       63 | -37.83%  | -12.97%            | -64.43% |     0.03 | 31.61%     | ok               |
| DBC        |       58 | -12.57%  | 22.26%             | -25.35% |    -0.43 | 32.78%     | ok               |
| DE         |       70 | -7.69%   | 50.52%             | -25.24% |    -0.08 | 45.59%     | ok               |
| DIA        |       60 | -2.42%   | 34.90%             | -12.94% |    -0.09 | 45.92%     | ok               |
| DIS        |       66 | -12.88%  | 5.09%              | -27.58% |    -0.17 | 48.42%     | ok               |
| DOGE-USD   |       76 | -19.44%  | -79.18%            | -62.31% |     0.06 | 49.62%     | ok               |
| DOT-USD    |       90 | -47.22%  | -86.71%            | -61.09% |    -0.35 | 48.08%     | ok               |
| DXY-INDEX  |       40 | -1.03%   | -0.46%             | -6.06%  |    -0.15 | 29.35%     | ok               |
| EEM        |       64 | -9.40%   | 83.01%             | -25.67% |    -0.25 | 43.43%     | ok               |
| EFA        |       62 | -9.68%   | 38.53%             | -15.14% |    -0.36 | 44.76%     | ok               |
| EOG        |       77 | -24.73%  | 15.54%             | -48.13% |    -0.54 | 46.09%     | ok               |
| ETC-USD    |       64 | -35.69%  | -73.29%            | -48.16% |    -0.51 | 31.23%     | ok               |
| ETH-USD    |       58 | 164.78%  | -47.65%            | -30.11% |     1.31 | 44.64%     | ok               |
| EWJ        |       64 | -17.64%  | 46.55%             | -30.73% |    -0.56 | 40.60%     | ok               |
| FCX        |       69 | -31.93%  | 72.04%             | -46.84% |    -0.39 | 45.92%     | ok               |
| FET-USD    |       83 | -15.80%  | -85.86%            | -54.02% |     0.14 | 39.85%     | ok               |
| FIL-USD    |       70 | -33.66%  | -85.39%            | -49.05% |    -0.29 | 33.14%     | ok               |
| FXI        |       46 | -7.07%   | 49.98%             | -24.33% |    -0.1  | 28.45%     | ok               |
| GDX        |       64 | 1.59%    | 187.17%            | -34.99% |     0.16 | 48.09%     | ok               |
| GDXJ       |       70 | -26.28%  | 206.79%            | -44.93% |    -0.29 | 45.92%     | ok               |
| GE         |       74 | 19.16%   | 239.41%            | -27.82% |     0.42 | 52.41%     | ok               |
| GLD        |       48 | 23.39%   | 104.21%            | -16.63% |     0.61 | 44.93%     | ok               |
| GOOGL      |       61 | 69.69%   | 127.79%            | -20.41% |     1.07 | 53.91%     | ok               |
| GRT-USD    |       87 | -10.82%  | -91.13%            | -55.61% |     0.1  | 42.34%     | ok               |
| GS         |       76 | 1.44%    | 190.72%            | -22.13% |     0.13 | 51.58%     | ok               |
| HD         |       71 | -5.19%   | -8.18%             | -17.69% |    -0.06 | 43.76%     | ok               |
| HON        |       97 | -29.20%  | 19.19%             | -30.75% |    -0.8  | 53.08%     | ok               |
| HYG        |       79 | -9.05%   | 2.75%              | -9.59%  |    -1.05 | 34.44%     | ok               |
| IBIT       |       32 | 32.55%   | -3.97%             | -18.95% |     0.71 | 30.99%     | ok               |
| IBM        |       74 | 10.69%   | 34.78%             | -25.31% |     0.31 | 50.42%     | ok               |
| ICP-USD    |       83 | -1.25%   | -78.75%            | -55.67% |     0.25 | 38.89%     | ok               |
| IEF        |       76 | -10.90%  | -1.60%             | -11.70% |    -1.54 | 32.78%     | ok               |
| IEMG       |       58 | -5.52%   | 75.44%             | -26.84% |    -0.12 | 43.59%     | ok               |
| INJ-USD    |       75 | -51.23%  | -79.88%            | -76.97% |    -0.47 | 38.12%     | ok               |
| INTC       |       70 | 55.82%   | 221.49%            | -60.60% |     0.62 | 49.25%     | ok               |
| INTU       |       65 | -14.05%  | -60.52%            | -43.77% |    -0.12 | 42.60%     | ok               |
| ITA        |       74 | -2.08%   | 92.63%             | -23.75% |     0.01 | 47.42%     | ok               |
| IWM        |       50 | 7.15%    | 49.53%             | -12.83% |     0.31 | 36.27%     | ok               |
| JNJ        |       71 | 6.96%    | 45.14%             | -17.51% |     0.3  | 50.42%     | ok               |
| JPM        |       75 | -18.53%  | 91.91%             | -33.43% |    -0.44 | 52.91%     | ok               |
| KO         |       51 | 27.92%   | 33.15%             | -8.07%  |     1    | 37.94%     | ok               |
| LDO-USD    |       74 | 1.95%    | -84.92%            | -60.93% |     0.29 | 37.93%     | ok               |
| LIN        |       68 | -0.80%   | 27.39%             | -21.53% |     0.03 | 38.94%     | ok               |
| LINK-USD   |       70 | -13.55%  | -67.23%            | -50.48% |     0.1  | 41.57%     | ok               |
| LLY        |       69 | -15.36%  | 70.87%             | -53.34% |    -0.13 | 51.41%     | ok               |
| LRCX       |       80 | -5.67%   | 384.20%            | -63.56% |     0.1  | 46.26%     | ok               |
| LTC-USD    |       66 | -34.00%  | -64.38%            | -53.76% |    -0.29 | 48.47%     | ok               |
| MCD        |       75 | -2.55%   | -7.60%             | -18.81% |    -0.05 | 38.10%     | ok               |
| META       |       72 | -16.37%  | 40.60%             | -38.96% |    -0.14 | 50.42%     | ok               |
| MPC        |       71 | -13.74%  | 54.42%             | -44.76% |    -0.14 | 49.92%     | ok               |
| MRK        |       67 | -27.28%  | -4.78%             | -34.46% |    -0.63 | 46.42%     | ok               |
| MS         |       81 | -12.08%  | 159.18%            | -27.79% |    -0.22 | 48.59%     | ok               |
| MSFT       |       83 | -34.69%  | -10.34%            | -39.34% |    -0.91 | 48.25%     | ok               |
| MU         |       51 | 270.20%  | 1260.03%           | -68.76% |     1.34 | 59.90%     | ok               |
| NEAR-USD   |       87 | 4.42%    | -62.19%            | -59.86% |     0.3  | 42.34%     | ok               |
| NEM        |       78 | -29.37%  | 193.80%            | -38.49% |    -0.29 | 54.74%     | ok               |
| NFLX       |       64 | 35.87%   | 26.57%             | -21.09% |     0.75 | 54.91%     | ok               |
| NKE        |       91 | -48.19%  | -58.42%            | -57.25% |    -0.9  | 43.59%     | ok               |
| NOW        |       80 | 25.42%   | -40.93%            | -30.25% |     0.46 | 45.92%     | ok               |
| NVDA       |       74 | -29.05%  | 125.42%            | -45.02% |    -0.24 | 58.82%     | ok               |
| OP-USD     |       74 | 4.19%    | -94.46%            | -70.27% |     0.29 | 35.82%     | ok               |
| ORCL       |       74 | 60.48%   | 53.91%             | -29.47% |     0.67 | 53.58%     | ok               |
| OXY        |       63 | 2.48%    | -10.68%            | -30.85% |     0.16 | 43.09%     | ok               |
| PEP        |       85 | -9.64%   | -16.32%            | -21.35% |    -0.22 | 50.25%     | ok               |
| PEPE-USD   |       75 | 21.63%   | -84.69%            | -57.66% |     0.45 | 43.68%     | ok               |
| PFE        |       77 | -39.46%  | -8.73%             | -42.29% |    -1.25 | 35.94%     | ok               |
| PG         |       62 | -12.71%  | -5.43%             | -21.65% |    -0.46 | 41.43%     | ok               |
| PM         |       83 | -4.21%   | 88.84%             | -33.68% |     0    | 57.74%     | ok               |
| POL-USD    |       79 | 64.83%   | -83.72%            | -46.45% |     0.77 | 49.62%     | ok               |
| QCOM       |       77 | -16.22%  | 48.29%             | -57.69% |    -0.05 | 47.59%     | ok               |
| QQQ        |       62 | 18.95%   | 72.36%             | -12.88% |     0.55 | 46.26%     | ok               |
| RENDER-USD |       96 | -17.59%  | -61.32%            | -45.00% |     0.11 | 43.65%     | ok               |
| RTX        |       58 | 17.94%   | 101.85%            | -16.99% |     0.49 | 51.58%     | ok               |
| SBUX       |       64 | -25.50%  | 6.77%              | -29.34% |    -0.53 | 38.77%     | ok               |
| SCHW       |       74 | -21.97%  | 43.93%             | -30.41% |    -0.52 | 45.42%     | ok               |
| SHIB-USD   |       76 | -21.48%  | -79.52%            | -47.96% |    -0.04 | 52.68%     | ok               |
| SHY        |       50 | -2.32%   | -0.35%             | -2.85%  |    -0.81 | 34.78%     | ok               |
| SKY-USD    |       68 | -29.87%  | 3.34%              | -43.98% |    -0.39 | 40.60%     | ok               |
| SLB        |       75 | -30.05%  | -9.87%             | -54.95% |    -0.54 | 49.92%     | ok               |
| SLV        |       58 | 35.90%   | 177.75%            | -42.66% |     0.57 | 40.60%     | ok               |
| SMH        |       48 | 96.25%   | 251.17%            | -33.99% |     1.2  | 50.58%     | ok               |
| SNX-USD    |       60 | 30.41%   | -86.45%            | -32.91% |     0.51 | 39.85%     | ok               |
| SOL-USD    |       68 | -42.35%  | -72.52%            | -56.90% |    -0.22 | 60.15%     | ok               |
| SOXX       |       55 | 84.32%   | 225.34%            | -40.34% |     1.05 | 49.58%     | ok               |
| SPY        |       60 | 6.50%    | 51.52%             | -16.47% |     0.28 | 50.92%     | ok               |
| SUSHI-USD  |       90 | -75.60%  | -88.75%            | -81.22% |    -1.06 | 35.44%     | ok               |
| T          |       62 | 37.01%   | 28.12%             | -17.01% |     0.86 | 50.75%     | ok               |
| TGT        |       56 | -11.79%  | -8.33%             | -41.74% |    -0.16 | 38.60%     | ok               |
| TIA-USD    |       86 | -16.62%  | -91.97%            | -55.19% |     0.07 | 34.67%     | ok               |
| TLT        |       70 | -22.66%  | -9.25%             | -23.95% |    -1.68 | 31.95%     | ok               |
| TMO        |       59 | 10.02%   | -16.81%            | -16.83% |     0.3  | 47.75%     | ok               |
| TMUS       |       72 | 13.79%   | 10.41%             | -24.50% |     0.38 | 47.92%     | ok               |
| TRX-USD    |       74 | 2.43%    | 37.68%             | -22.90% |     0.15 | 49.43%     | ok               |
| TSLA       |       68 | -4.12%   | 112.15%            | -57.89% |     0.16 | 42.43%     | ok               |
| TXN        |       77 | -15.83%  | 100.12%            | -46.98% |    -0.1  | 53.41%     | ok               |
| UNH        |       78 | 24.49%   | -19.40%            | -27.46% |     0.46 | 51.75%     | ok               |
| UNI-USD    |       88 | -72.81%  | -78.87%            | -80.61% |    -0.89 | 41.76%     | ok               |
| UPS        |       66 | -37.30%  | -32.14%            | -40.62% |    -0.74 | 39.93%     | ok               |
| USO        |       68 | 2.80%    | 56.41%             | -43.35% |     0.17 | 34.44%     | ok               |
| VEA        |       58 | -0.98%   | 51.73%             | -17.93% |     0.01 | 44.09%     | ok               |
| VIXY       |       92 | -78.88%  | -62.61%            | -87.58% |    -0.96 | 31.78%     | ok               |
| VNQ        |       75 | -16.77%  | 12.97%             | -24.92% |    -0.7  | 37.60%     | ok               |
| VTI        |       66 | -0.72%   | 50.95%             | -18.77% |     0.04 | 52.08%     | ok               |
| VWO        |       76 | -13.41%  | 52.45%             | -25.20% |    -0.47 | 44.09%     | ok               |
| VZ         |       85 | -26.94%  | 7.87%              | -31.88% |    -0.93 | 37.77%     | ok               |
| WFC        |       86 | -18.61%  | 66.51%             | -29.91% |    -0.32 | 48.09%     | ok               |
| WIF-USD    |       70 | -36.39%  | -90.70%            | -57.06% |    -0.12 | 32.38%     | ok               |
| WMT        |       57 | 27.23%   | 113.00%            | -21.31% |     0.74 | 51.58%     | ok               |
| XBI        |       60 | -1.28%   | 60.64%             | -21.61% |     0.05 | 39.77%     | ok               |
| XLB        |       70 | -14.85%  | 24.51%             | -26.57% |    -0.51 | 37.60%     | ok               |
| XLC        |       65 | 17.01%   | 36.42%             | -12.33% |     0.58 | 55.57%     | ok               |
| XLE        |       71 | -9.48%   | 28.52%             | -36.18% |    -0.17 | 46.59%     | ok               |
| XLF        |       74 | -11.27%  | 38.58%             | -23.61% |    -0.37 | 48.25%     | ok               |
| XLI        |       64 | 4.40%    | 59.24%             | -11.38% |     0.22 | 46.59%     | ok               |
| XLK        |       42 | 63.21%   | 88.75%             | -14.75% |     1.18 | 48.09%     | ok               |
| XLM-USD    |       71 | -8.71%   | -59.03%            | -48.82% |     0.13 | 45.79%     | ok               |
| XLP        |       70 | 6.70%    | 12.50%             | -11.16% |     0.41 | 42.76%     | ok               |
| XLU        |       69 | -3.67%   | 45.19%             | -18.15% |    -0.12 | 38.27%     | ok               |
| XLV        |       68 | -11.08%  | 6.99%              | -16.83% |    -0.53 | 36.27%     | ok               |
| XLY        |       72 | 1.26%    | 31.97%             | -14.01% |     0.11 | 44.76%     | ok               |
| XOM        |       56 | 4.30%    | 34.27%             | -20.29% |     0.19 | 36.11%     | ok               |
| XRP-USD    |       62 | -36.21%  | -65.35%            | -46.96% |    -0.36 | 35.82%     | ok               |
| YFI-USD    |       81 | -53.87%  | -77.98%            | -67.78% |    -0.79 | 40.42%     | ok               |
| ZEC-USD    |       69 | 48.03%   | 753.05%            | -47.68% |     0.58 | 36.59%     | ok               |

## AAPL Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 23.84%   | 54.91%             | -21.71% |     0.54 |       67 | 52.41%     | ok               |
|          25 | 17.92%   | 54.91%             | -20.03% |     0.44 |       65 | 50.25%     | ok               |
|          15 | 16.48%   | 54.91%             | -23.86% |     0.41 |       76 | 59.90%     | ok               |
|          30 | 13.72%   | 54.91%             | -20.65% |     0.37 |       63 | 48.59%     | ok               |
|          35 | 8.51%    | 54.91%             | -22.04% |     0.27 |       63 | 46.42%     | ok               |

## AAVE-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 5.38%    | -76.12%            | -46.87% |     0.27 |       38 | 26.05%     | ok               |
|          40 | -0.24%   | -76.12%            | -43.61% |     0.21 |       38 | 29.69%     | ok               |
|          35 | -20.11%  | -76.12%            | -51.96% |    -0.03 |       50 | 32.18%     | ok               |
|          50 | -29.70%  | -76.12%            | -47.78% |    -0.27 |       42 | 20.31%     | ok               |
|          15 | -58.09%  | -76.12%            | -64.84% |    -0.46 |       82 | 50.57%     | ok               |

## ABBV Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 2.55%    | 40.33%             | -23.80% |     0.15 |       50 | 37.77%     | ok               |
|          40 | -10.27%  | 40.33%             | -26.61% |    -0.18 |       64 | 42.76%     | ok               |
|          35 | -11.56%  | 40.33%             | -27.83% |    -0.21 |       66 | 45.59%     | ok               |
|          30 | -13.84%  | 40.33%             | -30.55% |    -0.26 |       64 | 48.42%     | ok               |
|          45 | -13.07%  | 40.33%             | -29.59% |    -0.26 |       56 | 39.93%     | ok               |

## ADA-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -83.55%  | -85.57%            | -91.83% |    -0.57 |       80 | 61.69%     | ok               |
|          50 | -77.92%  | -85.57%            | -85.97% |    -0.59 |       55 | 26.82%     | ok               |
|          20 | -83.66%  | -85.57%            | -92.33% |    -0.6  |       86 | 56.51%     | ok               |
|          45 | -80.28%  | -85.57%            | -88.02% |    -0.62 |       58 | 31.61%     | ok               |
|          35 | -82.47%  | -85.57%            | -89.77% |    -0.66 |       76 | 42.15%     | ok               |

## ADBE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 11.38%   | -69.07%            | -21.34% |     0.31 |       78 | 49.58%     | ok               |
|          40 | -3.00%   | -69.07%            | -20.88% |     0.06 |       74 | 42.60%     | ok               |
|          25 | -6.71%   | -69.07%            | -31.29% |     0.05 |       52 | 61.40%     | ok               |
|          15 | -16.67%  | -69.07%            | -31.86% |    -0.1  |       63 | 66.06%     | ok               |
|          20 | -18.30%  | -69.07%            | -34.42% |    -0.13 |       52 | 63.56%     | ok               |

## AGG Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -6.61%   | 0.17%              | -10.16% |    -1.1  |       69 | 31.11%     | ok               |
|          45 | -5.75%   | 0.17%              | -7.89%  |    -1.16 |       52 | 20.47%     | ok               |
|          20 | -8.00%   | 0.17%              | -10.96% |    -1.18 |       73 | 36.61%     | ok               |
|          50 | -5.57%   | 0.17%              | -7.92%  |    -1.25 |       46 | 16.97%     | ok               |
|          25 | -8.17%   | 0.17%              | -11.60% |    -1.25 |       73 | 34.94%     | ok               |

## ALGO-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -50.43%  | -79.72%            | -53.13% |    -0.57 |       86 | 38.12%     | ok               |
|          15 | -58.92%  | -79.72%            | -69.47% |    -0.61 |       86 | 50.19%     | ok               |
|          25 | -61.32%  | -79.72%            | -73.33% |    -0.72 |       88 | 45.21%     | ok               |
|          20 | -63.10%  | -79.72%            | -72.09% |    -0.73 |       88 | 47.89%     | ok               |
|          50 | -45.64%  | -79.72%            | -48.43% |    -0.81 |       42 | 16.86%     | ok               |

## AMAT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 4.89%    | 279.97%            | -54.05% |     0.24 |       66 | 62.06%     | ok               |
|          30 | -12.21%  | 279.97%            | -57.21% |     0    |       69 | 53.41%     | ok               |
|          20 | -18.63%  | 279.97%            | -60.16% |    -0.07 |       72 | 58.57%     | ok               |
|          50 | -16.40%  | 279.97%            | -48.72% |    -0.09 |       52 | 39.27%     | ok               |
|          35 | -18.46%  | 279.97%            | -55.26% |    -0.1  |       71 | 51.25%     | ok               |

## AMD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 0.89%    | 210.20%            | -46.37% |     0.22 |       56 | 37.77%     | ok               |
|          50 | -0.89%   | 210.20%            | -48.02% |     0.19 |       60 | 32.11%     | ok               |
|          35 | -11.97%  | 210.20%            | -54.16% |     0.09 |       62 | 39.77%     | ok               |
|          45 | -19.40%  | 210.20%            | -55.56% |    -0.02 |       64 | 35.11%     | ok               |
|          30 | -23.58%  | 210.20%            | -59.51% |    -0.04 |       63 | 42.26%     | ok               |

## AMGN Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -14.86%  | 9.98%              | -26.64% |    -0.23 |       72 | 53.58%     | ok               |
|          15 | -17.87%  | 9.98%              | -27.92% |    -0.29 |       70 | 59.23%     | ok               |
|          35 | -17.62%  | 9.98%              | -31.23% |    -0.34 |       69 | 43.93%     | ok               |
|          30 | -20.36%  | 9.98%              | -34.14% |    -0.41 |       71 | 47.59%     | ok               |
|          25 | -23.60%  | 9.98%              | -33.41% |    -0.48 |       67 | 49.92%     | ok               |

## AMZN Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -17.83%  | 44.36%             | -28.70% |    -0.52 |       50 | 29.78%     | ok               |
|          50 | -25.03%  | 44.36%             | -35.48% |    -0.88 |       48 | 24.13%     | ok               |
|          45 | -25.89%  | 44.36%             | -35.47% |    -0.89 |       50 | 26.96%     | ok               |
|          35 | -29.70%  | 44.36%             | -38.29% |    -0.91 |       62 | 32.95%     | ok               |
|          30 | -33.84%  | 44.36%             | -42.48% |    -0.99 |       74 | 38.27%     | ok               |

## APT-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 51.21%   | -92.94%            | -46.73% |     0.73 |       44 | 20.69%     | ok               |
|          45 | 14.97%   | -92.94%            | -63.86% |     0.37 |       60 | 26.82%     | ok               |
|          40 | -7.11%   | -92.94%            | -63.33% |     0.16 |       66 | 32.38%     | ok               |
|          20 | -15.40%  | -92.94%            | -70.51% |     0.14 |       71 | 52.30%     | ok               |
|          35 | -13.92%  | -92.94%            | -64.45% |     0.11 |       70 | 38.12%     | ok               |

## ARB-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 60.71%   | -89.16%            | -53.74% |     0.67 |       85 | 56.32%     | ok               |
|          40 | 45.76%   | -89.16%            | -47.60% |     0.62 |       50 | 30.27%     | ok               |
|          35 | 31.50%   | -89.16%            | -56.00% |     0.51 |       60 | 33.72%     | ok               |
|          20 | 29.27%   | -89.16%            | -60.40% |     0.5  |       75 | 50.19%     | ok               |
|          45 | 24.86%   | -89.16%            | -50.83% |     0.46 |       56 | 23.37%     | ok               |

## ARKK Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -27.18%  | 63.02%             | -35.41% |    -0.34 |       91 | 50.58%     | ok               |
|          20 | -31.48%  | 63.02%             | -35.41% |    -0.46 |       86 | 45.92%     | ok               |
|          30 | -33.45%  | 63.02%             | -35.93% |    -0.59 |       81 | 39.10%     | ok               |
|          35 | -33.82%  | 63.02%             | -36.30% |    -0.63 |       80 | 36.61%     | ok               |
|          40 | -35.22%  | 63.02%             | -36.71% |    -0.71 |       72 | 31.78%     | ok               |

## ATOM-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -64.76%  | -72.66%            | -70.96% |    -0.95 |       95 | 50.96%     | ok               |
|          15 | -68.86%  | -72.66%            | -72.24% |    -0.99 |       93 | 60.54%     | ok               |
|          45 | -59.73%  | -72.66%            | -65.47% |    -1.11 |       74 | 28.54%     | ok               |
|          30 | -68.06%  | -72.66%            | -73.96% |    -1.13 |       90 | 44.44%     | ok               |
|          20 | -72.13%  | -72.66%            | -74.90% |    -1.16 |      101 | 54.79%     | ok               |

## AVAX-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 18.71%   | -84.01%            | -32.41% |     0.41 |       36 | 19.35%     | ok               |
|          15 | 10.59%   | -84.01%            | -52.46% |     0.35 |       61 | 53.45%     | ok               |
|          45 | 7.44%    | -84.01%            | -39.20% |     0.27 |       38 | 23.37%     | ok               |
|          40 | -7.64%   | -84.01%            | -46.32% |     0.08 |       44 | 26.44%     | ok               |
|          25 | -16.70%  | -84.01%            | -52.93% |     0.04 |       73 | 44.44%     | ok               |

## AVGO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 30.81%   | 222.01%            | -35.76% |     0.49 |       60 | 45.09%     | ok               |
|          25 | 26.16%   | 222.01%            | -38.01% |     0.45 |       64 | 45.76%     | ok               |
|          35 | 21.91%   | 222.01%            | -36.19% |     0.41 |       70 | 42.43%     | ok               |
|          40 | 21.50%   | 222.01%            | -40.70% |     0.41 |       60 | 39.27%     | ok               |
|          50 | 15.49%   | 222.01%            | -35.84% |     0.34 |       62 | 33.11%     | ok               |

## BA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 27.46%   | 7.62%              | -13.34% |     0.7  |       42 | 31.61%     | ok               |
|          35 | 27.54%   | 7.62%              | -23.77% |     0.55 |       72 | 44.93%     | ok               |
|          40 | 14.97%   | 7.62%              | -23.87% |     0.38 |       48 | 38.94%     | ok               |
|          25 | 8.27%    | 7.62%              | -32.48% |     0.26 |       72 | 53.08%     | ok               |
|          30 | 5.13%    | 7.62%              | -30.56% |     0.21 |       69 | 49.58%     | ok               |

## BAC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -7.58%   | 70.69%             | -21.48% |    -0.1  |       80 | 51.75%     | ok               |
|          45 | -5.24%   | 70.69%             | -22.29% |    -0.1  |       62 | 35.44%     | ok               |
|          50 | -6.79%   | 70.69%             | -20.82% |    -0.17 |       60 | 32.28%     | ok               |
|          35 | -8.69%   | 70.69%             | -29.13% |    -0.19 |       70 | 43.26%     | ok               |
|          15 | -12.78%  | 70.69%             | -23.70% |    -0.22 |       80 | 56.74%     | ok               |

## BCH-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 1.25%    | -57.87%            | -53.87% |     0.22 |       76 | 47.89%     | ok               |
|          20 | -10.68%  | -57.87%            | -54.02% |     0.13 |       70 | 54.41%     | ok               |
|          15 | -20.90%  | -57.87%            | -60.20% |     0.02 |       79 | 59.00%     | ok               |
|          25 | -21.92%  | -57.87%            | -59.80% |    -0.02 |       72 | 50.19%     | ok               |
|          40 | -19.93%  | -57.87%            | -60.69% |    -0.07 |       67 | 40.23%     | ok               |

## BITO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 21.07%   | -57.97%            | -32.29% |     0.41 |       54 | 25.96%     | ok               |
|          30 | 4.43%    | -57.97%            | -42.82% |     0.23 |       78 | 40.77%     | ok               |
|          15 | -1.95%   | -57.97%            | -48.29% |     0.18 |       87 | 49.75%     | ok               |
|          45 | 0.97%    | -57.97%            | -43.53% |     0.17 |       58 | 28.95%     | ok               |
|          25 | -3.83%   | -57.97%            | -41.73% |     0.14 |       82 | 43.76%     | ok               |

## BLK Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | -0.06%   | 33.35%             | -15.13% |     0.07 |       82 | 39.27%     | ok               |
|          40 | -1.95%   | 33.35%             | -17.32% |    -0    |       74 | 34.94%     | ok               |
|          20 | -5.39%   | 33.35%             | -18.79% |    -0.08 |       79 | 47.25%     | ok               |
|          30 | -6.34%   | 33.35%             | -21.68% |    -0.12 |       75 | 43.09%     | ok               |
|          25 | -7.28%   | 33.35%             | -20.72% |    -0.14 |       75 | 45.42%     | ok               |

## BND Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -6.17%   | 0.21%              | -9.05%  |    -0.9  |       63 | 38.10%     | ok               |
|          25 | -6.87%   | 0.21%              | -10.14% |    -1.05 |       67 | 36.11%     | ok               |
|          30 | -7.32%   | 0.21%              | -9.89%  |    -1.18 |       65 | 32.28%     | ok               |
|          15 | -8.39%   | 0.21%              | -10.58% |    -1.21 |       73 | 40.93%     | ok               |
|          45 | -7.56%   | 0.21%              | -9.57%  |    -1.47 |       50 | 21.96%     | ok               |

## BONK-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 170.82%  | -86.36%            | -35.57% |     1.24 |       46 | 22.22%     | ok               |
|          25 | 170.13%  | -86.36%            | -46.61% |     1.04 |       65 | 48.08%     | ok               |
|          20 | 154.87%  | -86.36%            | -54.25% |     0.99 |       66 | 52.68%     | ok               |
|          15 | 160.70%  | -86.36%            | -62.48% |     0.98 |       70 | 57.66%     | ok               |
|          45 | 85.55%   | -86.36%            | -42.36% |     0.84 |       56 | 27.01%     | ok               |

## BTC-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 51.83%   | -38.52%            | -14.50% |     0.95 |       44 | 34.10%     | ok               |
|          45 | 41.09%   | -38.52%            | -15.18% |     0.81 |       44 | 30.65%     | ok               |
|          35 | 36.01%   | -38.52%            | -22.12% |     0.7  |       68 | 41.00%     | ok               |
|          30 | 17.30%   | -38.52%            | -21.75% |     0.41 |       70 | 47.51%     | ok               |
|          50 | 14.18%   | -38.52%            | -16.15% |     0.4  |       42 | 25.29%     | ok               |

## C Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -4.71%   | 169.21%            | -22.28% |    -0.06 |       66 | 35.77%     | ok               |
|          45 | -11.81%  | 169.21%            | -28.12% |    -0.24 |       78 | 39.77%     | ok               |
|          25 | -19.22%  | 169.21%            | -34.18% |    -0.32 |       73 | 52.75%     | ok               |
|          15 | -21.27%  | 169.21%            | -35.02% |    -0.34 |       74 | 59.40%     | ok               |
|          20 | -21.92%  | 169.21%            | -35.56% |    -0.37 |       81 | 55.74%     | ok               |

## CAT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 34.32%   | 237.11%            | -21.02% |     0.62 |       70 | 56.74%     | ok               |
|          25 | 34.44%   | 237.11%            | -26.37% |     0.62 |       66 | 59.57%     | ok               |
|          20 | 31.72%   | 237.11%            | -25.65% |     0.58 |       76 | 62.90%     | ok               |
|          45 | 22.72%   | 237.11%            | -28.85% |     0.49 |       56 | 45.59%     | ok               |
|          15 | 21.50%   | 237.11%            | -30.60% |     0.44 |       69 | 68.89%     | ok               |

## CL Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 13.96%   | 5.61%              | -12.98% |     0.59 |       42 | 31.78%     | ok               |
|          30 | 13.47%   | 5.61%              | -14.32% |     0.48 |       60 | 47.75%     | ok               |
|          45 | 8.76%    | 5.61%              | -13.51% |     0.38 |       46 | 34.78%     | ok               |
|          35 | 8.07%    | 5.61%              | -13.83% |     0.33 |       62 | 44.09%     | ok               |
|          40 | 4.94%    | 5.61%              | -12.70% |     0.24 |       56 | 38.77%     | ok               |

## CMCSA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -33.86%  | -48.35%            | -49.03% |    -0.73 |       87 | 58.74%     | ok               |
|          30 | -38.25%  | -48.35%            | -40.02% |    -0.99 |       82 | 44.26%     | ok               |
|          25 | -43.59%  | -48.35%            | -45.20% |    -1.15 |       89 | 49.58%     | ok               |
|          20 | -45.21%  | -48.35%            | -47.23% |    -1.18 |       93 | 54.74%     | ok               |
|          50 | -32.81%  | -48.35%            | -33.68% |    -1.27 |       50 | 16.47%     | ok               |

## COMP-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -3.83%   | -78.99%            | -38.71% |     0.15 |       46 | 20.69%     | ok               |
|          25 | -37.88%  | -78.99%            | -60.58% |    -0.19 |       87 | 50.00%     | ok               |
|          30 | -36.73%  | -78.99%            | -58.43% |    -0.21 |       89 | 45.02%     | ok               |
|          15 | -46.13%  | -78.99%            | -65.55% |    -0.28 |      101 | 61.49%     | ok               |
|          40 | -41.16%  | -78.99%            | -47.52% |    -0.37 |       74 | 33.14%     | ok               |

## COP Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -9.77%   | -1.70%             | -34.21% |    -0.15 |       48 | 27.29%     | ok               |
|          45 | -15.67%  | -1.70%             | -40.57% |    -0.3  |       58 | 30.12%     | ok               |
|          35 | -23.70%  | -1.70%             | -43.58% |    -0.45 |       75 | 37.10%     | ok               |
|          30 | -24.21%  | -1.70%             | -43.77% |    -0.45 |       73 | 40.27%     | ok               |
|          40 | -26.23%  | -1.70%             | -46.34% |    -0.57 |       68 | 32.78%     | ok               |

## COST Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 17.26%   | 37.08%             | -24.32% |     0.52 |       64 | 52.58%     | ok               |
|          25 | 16.24%   | 37.08%             | -24.73% |     0.5  |       61 | 49.92%     | ok               |
|          35 | 9.56%    | 37.08%             | -26.58% |     0.35 |       54 | 43.43%     | ok               |
|          30 | 4.54%    | 37.08%             | -29.73% |     0.2  |       60 | 46.42%     | ok               |
|          40 | 2.83%    | 37.08%             | -28.41% |     0.16 |       56 | 40.43%     | ok               |

## CRM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -30.57%  | -47.85%            | -38.20% |    -0.45 |       90 | 55.41%     | ok               |
|          35 | -24.86%  | -47.85%            | -36.72% |    -0.47 |       62 | 38.94%     | ok               |
|          40 | -30.31%  | -47.85%            | -41.30% |    -0.68 |       68 | 34.94%     | ok               |
|          30 | -35.46%  | -47.85%            | -41.46% |    -0.72 |       65 | 43.76%     | ok               |
|          20 | -40.81%  | -47.85%            | -43.08% |    -0.76 |       78 | 49.08%     | ok               |

## CRV-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 24.97%   | -77.01%            | -37.78% |     0.46 |       64 | 29.69%     | ok               |
|          50 | 12.00%   | -77.01%            | -29.30% |     0.33 |       40 | 16.67%     | ok               |
|          45 | 6.52%    | -77.01%            | -42.29% |     0.27 |       52 | 19.54%     | ok               |
|          30 | -0.75%   | -77.01%            | -39.89% |     0.22 |       62 | 34.29%     | ok               |
|          40 | -0.48%   | -77.01%            | -38.86% |     0.2  |       56 | 25.67%     | ok               |

## CSCO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 28.18%   | 132.42%            | -19.34% |     0.63 |       58 | 38.94%     | ok               |
|          45 | 26.53%   | 132.42%            | -19.34% |     0.59 |       51 | 41.43%     | ok               |
|          25 | 24.43%   | 132.42%            | -23.28% |     0.52 |       65 | 52.58%     | ok               |
|          35 | 23.84%   | 132.42%            | -23.68% |     0.52 |       53 | 48.09%     | ok               |
|          30 | 23.86%   | 132.42%            | -21.79% |     0.52 |       61 | 50.58%     | ok               |

## CVX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -10.31%  | 17.43%             | -28.32% |    -0.27 |       57 | 30.95%     | ok               |
|          20 | -13.07%  | 17.43%             | -26.07% |    -0.29 |       71 | 45.26%     | ok               |
|          35 | -11.99%  | 17.43%             | -27.83% |    -0.29 |       65 | 37.77%     | ok               |
|          25 | -13.44%  | 17.43%             | -25.65% |    -0.3  |       75 | 44.09%     | ok               |
|          40 | -12.26%  | 17.43%             | -26.30% |    -0.33 |       71 | 34.78%     | ok               |

## DASH-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 129.69%  | -12.97%            | -31.38% |     0.96 |       40 | 17.05%     | ok               |
|          40 | 75.62%   | -12.97%            | -34.44% |     0.72 |       46 | 23.75%     | ok               |
|          45 | 65.87%   | -12.97%            | -39.58% |     0.68 |       44 | 19.35%     | ok               |
|          25 | -32.35%  | -12.97%            | -64.14% |     0.1  |       69 | 34.48%     | ok               |
|          35 | -32.14%  | -12.97%            | -63.23% |     0.09 |       69 | 28.16%     | ok               |

## DBC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -8.05%   | 22.26%             | -19.49% |    -0.3  |       44 | 20.80%     | ok               |
|          35 | -9.68%   | 22.26%             | -23.38% |    -0.31 |       60 | 31.61%     | ok               |
|          15 | -10.28%  | 22.26%             | -27.04% |    -0.32 |       69 | 37.44%     | ok               |
|          45 | -9.42%   | 22.26%             | -20.65% |    -0.33 |       56 | 24.13%     | ok               |
|          30 | -12.57%  | 22.26%             | -25.35% |    -0.43 |       58 | 32.78%     | ok               |

## DE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -6.83%   | 50.52%             | -28.94% |    -0.05 |       70 | 50.92%     | ok               |
|          30 | -7.69%   | 50.52%             | -25.24% |    -0.08 |       70 | 45.59%     | ok               |
|          25 | -9.13%   | 50.52%             | -26.67% |    -0.11 |       72 | 48.25%     | ok               |
|          50 | -9.68%   | 50.52%             | -24.57% |    -0.2  |       70 | 30.45%     | ok               |
|          45 | -11.48%  | 50.52%             | -28.13% |    -0.22 |       68 | 34.94%     | ok               |

## DIA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | -0.36%   | 34.90%             | -13.15% |     0.02 |       60 | 43.76%     | ok               |
|          25 | -0.90%   | 34.90%             | -11.28% |    -0.01 |       60 | 47.09%     | ok               |
|          30 | -2.42%   | 34.90%             | -12.94% |    -0.09 |       60 | 45.92%     | ok               |
|          20 | -4.29%   | 34.90%             | -13.85% |    -0.18 |       64 | 49.42%     | ok               |
|          40 | -4.39%   | 34.90%             | -15.06% |    -0.22 |       66 | 41.10%     | ok               |

## DIS Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 32.27%   | 5.09%              | -14.24% |     0.81 |       50 | 30.45%     | ok               |
|          45 | 4.53%    | 5.09%              | -16.54% |     0.19 |       51 | 33.94%     | ok               |
|          40 | 2.90%    | 5.09%              | -23.29% |     0.16 |       63 | 39.27%     | ok               |
|          35 | -6.69%   | 5.09%              | -25.11% |    -0.03 |       73 | 45.09%     | ok               |
|          15 | -9.23%   | 5.09%              | -30.25% |    -0.06 |       87 | 59.23%     | ok               |

## DOGE-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 18.03%   | -79.18%            | -59.36% |     0.43 |       80 | 64.94%     | ok               |
|          20 | 0.78%    | -79.18%            | -57.37% |     0.28 |       83 | 60.15%     | ok               |
|          25 | -3.40%   | -79.18%            | -55.33% |     0.24 |       73 | 54.79%     | ok               |
|          30 | -19.44%  | -79.18%            | -62.31% |     0.06 |       76 | 49.62%     | ok               |
|          35 | -45.34%  | -79.18%            | -63.16% |    -0.38 |       72 | 43.10%     | ok               |

## DOT-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -19.10%  | -86.71%            | -44.94% |    -0.11 |       56 | 26.25%     | ok               |
|          45 | -27.53%  | -86.71%            | -52.30% |    -0.22 |       50 | 30.84%     | ok               |
|          40 | -35.47%  | -86.71%            | -52.19% |    -0.32 |       56 | 34.29%     | ok               |
|          30 | -47.22%  | -86.71%            | -61.09% |    -0.35 |       90 | 48.08%     | ok               |
|          35 | -46.19%  | -86.71%            | -62.63% |    -0.36 |       80 | 41.38%     | ok               |

## DXY-INDEX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -1.03%   | -0.46%             | -6.06%  |    -0.15 |       40 | 29.35%     | ok               |
|          40 | -3.37%   | -0.46%             | -7.30%  |    -0.42 |       68 | 48.48%     | ok               |
|          15 | -5.72%   | -0.46%             | -11.57% |    -0.53 |       92 | 75.43%     | ok               |
|          35 | -4.65%   | -0.46%             | -10.12% |    -0.55 |       73 | 54.35%     | ok               |
|          45 | -4.09%   | -0.46%             | -8.12%  |    -0.56 |       64 | 37.39%     | ok               |

## EEM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -2.91%   | 83.01%             | -15.88% |    -0.04 |       50 | 36.11%     | ok               |
|          45 | -4.62%   | 83.01%             | -17.36% |    -0.11 |       52 | 37.60%     | ok               |
|          40 | -4.96%   | 83.01%             | -19.52% |    -0.11 |       64 | 39.77%     | ok               |
|          35 | -5.62%   | 83.01%             | -23.88% |    -0.12 |       66 | 41.76%     | ok               |
|          30 | -9.40%   | 83.01%             | -25.67% |    -0.25 |       64 | 43.43%     | ok               |

## EFA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -1.25%   | 38.53%             | -10.80% |     0.02 |       58 | 52.08%     | ok               |
|          20 | -8.10%   | 38.53%             | -12.49% |    -0.27 |       65 | 49.08%     | ok               |
|          30 | -9.68%   | 38.53%             | -15.14% |    -0.36 |       62 | 44.76%     | ok               |
|          50 | -9.07%   | 38.53%             | -17.56% |    -0.4  |       54 | 36.27%     | ok               |
|          25 | -11.12%  | 38.53%             | -16.37% |    -0.41 |       62 | 46.59%     | ok               |

## EOG Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -18.73%  | 15.54%             | -38.89% |    -0.43 |       52 | 32.78%     | ok               |
|          50 | -19.92%  | 15.54%             | -39.55% |    -0.49 |       56 | 29.95%     | ok               |
|          30 | -24.73%  | 15.54%             | -48.13% |    -0.54 |       77 | 46.09%     | ok               |
|          40 | -23.54%  | 15.54%             | -42.28% |    -0.57 |       60 | 36.11%     | ok               |
|          35 | -25.10%  | 15.54%             | -45.93% |    -0.6  |       75 | 40.93%     | ok               |

## ETC-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -7.93%   | -73.29%            | -27.89% |    -0.02 |       28 | 17.05%     | ok               |
|          35 | -15.03%  | -73.29%            | -42.62% |    -0.11 |       44 | 27.01%     | ok               |
|          45 | -16.07%  | -73.29%            | -35.44% |    -0.17 |       26 | 18.97%     | ok               |
|          40 | -21.04%  | -73.29%            | -40.48% |    -0.26 |       42 | 22.80%     | ok               |
|          30 | -35.69%  | -73.29%            | -48.16% |    -0.51 |       64 | 31.23%     | ok               |

## ETH-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 164.78%  | -47.65%            | -30.11% |     1.31 |       58 | 44.64%     | ok               |
|          30 | 147.01%  | -47.65%            | -32.89% |     1.18 |       64 | 53.07%     | ok               |
|          40 | 62.72%   | -47.65%            | -33.11% |     0.8  |       56 | 37.36%     | ok               |
|          45 | 35.50%   | -47.65%            | -34.50% |     0.58 |       52 | 33.52%     | ok               |
|          20 | 39.51%   | -47.65%            | -39.10% |     0.57 |       83 | 63.41%     | ok               |

## EWJ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -17.64%  | 46.55%             | -30.73% |    -0.56 |       64 | 40.60%     | ok               |
|          20 | -19.04%  | 46.55%             | -31.32% |    -0.6  |       60 | 42.60%     | ok               |
|          45 | -18.43%  | 46.55%             | -27.68% |    -0.69 |       60 | 32.78%     | ok               |
|          25 | -21.37%  | 46.55%             | -31.18% |    -0.7  |       60 | 41.60%     | ok               |
|          35 | -21.59%  | 46.55%             | -32.54% |    -0.73 |       70 | 38.94%     | ok               |

## FCX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -6.29%   | 72.04%             | -26.57% |     0.03 |       56 | 29.45%     | ok               |
|          45 | -11.01%  | 72.04%             | -32.99% |    -0.04 |       56 | 33.78%     | ok               |
|          40 | -23.41%  | 72.04%             | -42.89% |    -0.26 |       66 | 39.10%     | ok               |
|          30 | -31.93%  | 72.04%             | -46.84% |    -0.39 |       69 | 45.92%     | ok               |
|          35 | -35.67%  | 72.04%             | -50.12% |    -0.49 |       73 | 43.93%     | ok               |

## FET-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 36.39%   | -85.86%            | -57.62% |     0.55 |       90 | 50.00%     | ok               |
|          15 | 2.01%    | -85.86%            | -59.58% |     0.34 |       86 | 53.07%     | ok               |
|          25 | -10.76%  | -85.86%            | -58.20% |     0.21 |       93 | 43.68%     | ok               |
|          30 | -15.80%  | -85.86%            | -54.02% |     0.14 |       83 | 39.85%     | ok               |
|          45 | -25.27%  | -85.86%            | -48.61% |    -0.14 |       56 | 18.97%     | ok               |

## FIL-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -6.35%   | -85.39%            | -39.40% |     0.09 |       48 | 23.37%     | ok               |
|          35 | -30.36%  | -85.39%            | -45.88% |    -0.27 |       58 | 27.59%     | ok               |
|          45 | -27.58%  | -85.39%            | -43.98% |    -0.29 |       44 | 17.62%     | ok               |
|          30 | -33.66%  | -85.39%            | -49.05% |    -0.29 |       70 | 33.14%     | ok               |
|          50 | -26.52%  | -85.39%            | -44.97% |    -0.32 |       38 | 13.03%     | ok               |

## FXI Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -6.54%   | 49.98%             | -22.99% |    -0.08 |       46 | 29.62%     | ok               |
|          30 | -7.07%   | 49.98%             | -24.33% |    -0.1  |       46 | 28.45%     | ok               |
|          15 | -8.81%   | 49.98%             | -21.68% |    -0.12 |       52 | 32.78%     | ok               |
|          45 | -8.95%   | 49.98%             | -26.75% |    -0.17 |       44 | 22.96%     | ok               |
|          20 | -10.31%  | 49.98%             | -24.94% |    -0.18 |       52 | 30.78%     | ok               |

## GDX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 15.62%   | 187.17%            | -31.87% |     0.37 |       62 | 42.76%     | ok               |
|          20 | 7.79%    | 187.17%            | -35.59% |     0.25 |       77 | 52.91%     | ok               |
|          35 | 7.17%    | 187.17%            | -32.37% |     0.24 |       68 | 45.09%     | ok               |
|          30 | 1.59%    | 187.17%            | -34.99% |     0.16 |       64 | 48.09%     | ok               |
|          25 | -2.52%   | 187.17%            | -38.90% |     0.1  |       67 | 49.75%     | ok               |

## GDXJ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -17.20%  | 206.79%            | -45.05% |    -0.08 |       70 | 53.24%     | ok               |
|          50 | -16.59%  | 206.79%            | -42.44% |    -0.15 |       56 | 37.44%     | ok               |
|          30 | -26.28%  | 206.79%            | -44.93% |    -0.29 |       70 | 45.92%     | ok               |
|          40 | -28.47%  | 206.79%            | -44.27% |    -0.36 |       66 | 41.76%     | ok               |
|          45 | -27.77%  | 206.79%            | -42.73% |    -0.36 |       60 | 39.77%     | ok               |

## GE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 36.27%   | 239.41%            | -22.29% |     0.7  |       66 | 39.27%     | ok               |
|          45 | 25.98%   | 239.41%            | -25.68% |     0.54 |       74 | 42.10%     | ok               |
|          20 | 25.05%   | 239.41%            | -26.63% |     0.5  |       69 | 55.91%     | ok               |
|          35 | 19.44%   | 239.41%            | -27.11% |     0.43 |       80 | 47.42%     | ok               |
|          40 | 18.54%   | 239.41%            | -26.97% |     0.42 |       76 | 43.59%     | ok               |

## GLD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | 29.56%   | 104.21%            | -14.61% |     0.73 |       46 | 46.09%     | ok               |
|          20 | 27.63%   | 104.21%            | -14.61% |     0.69 |       48 | 47.42%     | ok               |
|          30 | 23.39%   | 104.21%            | -16.63% |     0.61 |       48 | 44.93%     | ok               |
|          15 | 19.81%   | 104.21%            | -17.54% |     0.51 |       50 | 51.58%     | ok               |
|          35 | 17.37%   | 104.21%            | -17.29% |     0.49 |       50 | 44.26%     | ok               |

## GOOGL Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 72.43%   | 127.79%            | -19.12% |     1.12 |       63 | 49.25%     | ok               |
|          25 | 71.04%   | 127.79%            | -19.76% |     1.07 |       59 | 56.07%     | ok               |
|          30 | 69.69%   | 127.79%            | -20.41% |     1.07 |       61 | 53.91%     | ok               |
|          15 | 61.41%   | 127.79%            | -13.59% |     0.93 |       71 | 63.73%     | ok               |
|          20 | 58.13%   | 127.79%            | -20.57% |     0.92 |       70 | 58.40%     | ok               |

## GRT-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 36.90%   | -91.13%            | -34.47% |     0.61 |       44 | 21.65%     | ok               |
|          20 | 8.48%    | -91.13%            | -46.47% |     0.33 |       81 | 55.94%     | ok               |
|          15 | 6.56%    | -91.13%            | -49.67% |     0.32 |       73 | 61.11%     | ok               |
|          45 | 9.77%    | -91.13%            | -50.50% |     0.31 |       50 | 26.82%     | ok               |
|          35 | 7.59%    | -91.13%            | -50.72% |     0.29 |       62 | 35.82%     | ok               |

## GS Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 31.46%   | 190.72%            | -20.56% |     0.63 |       74 | 60.40%     | ok               |
|          20 | 13.53%   | 190.72%            | -23.19% |     0.36 |       74 | 56.41%     | ok               |
|          25 | 7.78%    | 190.72%            | -23.32% |     0.25 |       74 | 53.91%     | ok               |
|          40 | 2.85%    | 190.72%            | -17.88% |     0.15 |       72 | 44.93%     | ok               |
|          30 | 1.44%    | 190.72%            | -22.13% |     0.13 |       76 | 51.58%     | ok               |

## HD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -5.19%   | -8.18%             | -17.69% |    -0.06 |       71 | 43.76%     | ok               |
|          25 | -5.93%   | -8.18%             | -18.51% |    -0.08 |       70 | 45.76%     | ok               |
|          45 | -11.57%  | -8.18%             | -20.74% |    -0.33 |       60 | 28.45%     | ok               |
|          40 | -13.58%  | -8.18%             | -19.63% |    -0.38 |       82 | 33.78%     | ok               |
|          35 | -15.81%  | -8.18%             | -22.98% |    -0.4  |       80 | 39.93%     | ok               |

## HON Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -17.61%  | 19.19%             | -22.04% |    -0.51 |       76 | 37.27%     | ok               |
|          50 | -17.09%  | 19.19%             | -23.31% |    -0.53 |       74 | 32.11%     | ok               |
|          40 | -25.72%  | 19.19%             | -26.73% |    -0.74 |       78 | 41.60%     | ok               |
|          35 | -27.43%  | 19.19%             | -28.41% |    -0.77 |       95 | 48.09%     | ok               |
|          30 | -29.20%  | 19.19%             | -30.75% |    -0.8  |       97 | 53.08%     | ok               |

## HYG Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -7.49%   | 2.75%              | -7.49%  |    -0.9  |       70 | 29.62%     | ok               |
|          45 | -8.18%   | 2.75%              | -8.21%  |    -1.02 |       66 | 26.46%     | ok               |
|          30 | -9.05%   | 2.75%              | -9.59%  |    -1.05 |       79 | 34.44%     | ok               |
|          15 | -9.81%   | 2.75%              | -10.16% |    -1.06 |       88 | 41.76%     | ok               |
|          20 | -9.84%   | 2.75%              | -10.45% |    -1.1  |       88 | 39.43%     | ok               |

## IBIT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 52.25%   | -3.97%             | -17.37% |     1.07 |       20 | 23.00%     | ok               |
|          15 | 60.87%   | -3.97%             | -19.20% |     1.03 |       38 | 38.74%     | ok               |
|          45 | 43.79%   | -3.97%             | -17.37% |     0.92 |       22 | 23.73%     | ok               |
|          40 | 38.89%   | -3.97%             | -17.78% |     0.84 |       24 | 25.42%     | ok               |
|          30 | 32.55%   | -3.97%             | -18.95% |     0.71 |       32 | 30.99%     | ok               |

## IBM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 20.51%   | 34.78%             | -28.20% |     0.45 |       89 | 62.40%     | ok               |
|          30 | 10.69%   | 34.78%             | -25.31% |     0.31 |       74 | 50.42%     | ok               |
|          35 | 8.47%    | 34.78%             | -25.15% |     0.27 |       70 | 46.09%     | ok               |
|          45 | 6.12%    | 34.78%             | -18.36% |     0.23 |       56 | 36.61%     | ok               |
|          40 | 2.96%    | 34.78%             | -24.66% |     0.16 |       66 | 40.60%     | ok               |

## ICP-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 20.56%   | -78.75%            | -32.85% |     0.42 |       60 | 27.20%     | ok               |
|          35 | 9.11%    | -78.75%            | -46.18% |     0.31 |       70 | 32.76%     | ok               |
|          30 | -1.25%   | -78.75%            | -55.67% |     0.25 |       83 | 38.89%     | ok               |
|          50 | 5.02%    | -78.75%            | -43.65% |     0.25 |       42 | 17.05%     | ok               |
|          45 | -8.63%   | -78.75%            | -40.57% |     0.08 |       60 | 21.26%     | ok               |

## IEF Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -6.92%   | -1.60%             | -9.79%  |    -0.82 |       70 | 42.26%     | ok               |
|          15 | -7.48%   | -1.60%             | -10.52% |    -0.88 |       69 | 43.76%     | ok               |
|          40 | -8.39%   | -1.60%             | -9.67%  |    -1.31 |       60 | 24.79%     | ok               |
|          45 | -8.07%   | -1.60%             | -9.73%  |    -1.33 |       50 | 22.80%     | ok               |
|          25 | -10.50%  | -1.60%             | -11.19% |    -1.34 |       76 | 39.43%     | ok               |

## IEMG Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 1.46%    | 75.44%             | -13.87% |     0.11 |       52 | 34.78%     | ok               |
|          45 | 0.63%    | 75.44%             | -14.87% |     0.08 |       48 | 37.27%     | ok               |
|          35 | -0.32%   | 75.44%             | -22.13% |     0.05 |       63 | 42.60%     | ok               |
|          40 | -0.92%   | 75.44%             | -18.39% |     0.03 |       60 | 40.27%     | ok               |
|          25 | -4.72%   | 75.44%             | -25.58% |    -0.09 |       59 | 45.42%     | ok               |

## INJ-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -12.91%  | -79.88%            | -55.31% |     0.02 |       44 | 22.41%     | ok               |
|          35 | -18.57%  | -79.88%            | -60.42% |     0.01 |       60 | 32.57%     | ok               |
|          50 | -22.38%  | -79.88%            | -51.00% |    -0.14 |       48 | 19.35%     | ok               |
|          40 | -26.93%  | -79.88%            | -57.21% |    -0.15 |       50 | 28.74%     | ok               |
|          25 | -53.36%  | -79.88%            | -81.57% |    -0.46 |       77 | 42.91%     | ok               |

## INTC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 76.11%   | 221.49%            | -49.32% |     0.74 |       60 | 34.28%     | ok               |
|          15 | 82.95%   | 221.49%            | -53.65% |     0.74 |       84 | 61.23%     | ok               |
|          25 | 75.50%   | 221.49%            | -56.41% |     0.72 |       75 | 51.58%     | ok               |
|          40 | 70.33%   | 221.49%            | -55.86% |     0.7  |       68 | 38.60%     | ok               |
|          20 | 72.70%   | 221.49%            | -52.47% |     0.7  |       82 | 56.57%     | ok               |

## INTU Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 1.10%    | -60.52%            | -42.82% |     0.14 |       71 | 29.12%     | ok               |
|          45 | -2.35%   | -60.52%            | -44.66% |     0.08 |       69 | 33.28%     | ok               |
|          40 | -9.67%   | -60.52%            | -48.32% |    -0.06 |       69 | 35.94%     | ok               |
|          25 | -10.95%  | -60.52%            | -42.24% |    -0.06 |       64 | 45.26%     | ok               |
|          15 | -12.00%  | -60.52%            | -46.90% |    -0.07 |       79 | 50.75%     | ok               |

## ITA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 2.04%    | 92.63%             | -21.48% |     0.13 |       76 | 37.44%     | ok               |
|          15 | -2.01%   | 92.63%             | -28.17% |     0.03 |       86 | 59.07%     | ok               |
|          30 | -2.08%   | 92.63%             | -23.75% |     0.01 |       74 | 47.42%     | ok               |
|          35 | -4.60%   | 92.63%             | -23.16% |    -0.07 |       78 | 45.59%     | ok               |
|          40 | -5.70%   | 92.63%             | -20.58% |    -0.11 |       80 | 42.10%     | ok               |

## IWM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | 7.57%    | 49.53%             | -13.88% |     0.32 |       52 | 37.27%     | ok               |
|          30 | 7.15%    | 49.53%             | -12.83% |     0.31 |       50 | 36.27%     | ok               |
|          40 | 4.98%    | 49.53%             | -14.08% |     0.25 |       44 | 31.61%     | ok               |
|          35 | 4.73%    | 49.53%             | -14.11% |     0.23 |       50 | 33.94%     | ok               |
|          20 | 3.33%    | 49.53%             | -14.41% |     0.17 |       62 | 38.27%     | ok               |

## JNJ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 21.36%   | 45.14%             | -10.57% |     0.9  |       56 | 37.10%     | ok               |
|          15 | 18.58%   | 45.14%             | -18.02% |     0.64 |       65 | 57.74%     | ok               |
|          45 | 12.26%   | 45.14%             | -13.35% |     0.53 |       58 | 42.26%     | ok               |
|          20 | 14.10%   | 45.14%             | -17.61% |     0.53 |       71 | 54.24%     | ok               |
|          40 | 10.14%   | 45.14%             | -14.77% |     0.44 |       64 | 46.26%     | ok               |

## JPM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 20.86%   | 91.91%             | -15.90% |     0.69 |       52 | 40.43%     | ok               |
|          45 | 9.38%    | 91.91%             | -21.91% |     0.34 |       54 | 43.43%     | ok               |
|          40 | -5.07%   | 91.91%             | -28.47% |    -0.07 |       66 | 45.92%     | ok               |
|          20 | -12.51%  | 91.91%             | -33.59% |    -0.2  |       86 | 57.40%     | ok               |
|          35 | -10.37%  | 91.91%             | -27.43% |    -0.21 |       72 | 49.58%     | ok               |

## KO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 27.92%   | 33.15%             | -8.07%  |     1    |       51 | 37.94%     | ok               |
|          35 | 24.00%   | 33.15%             | -8.07%  |     0.89 |       54 | 36.61%     | ok               |
|          40 | 21.41%   | 33.15%             | -9.28%  |     0.86 |       56 | 33.44%     | ok               |
|          25 | 22.64%   | 33.15%             | -9.37%  |     0.83 |       57 | 40.60%     | ok               |
|          50 | 14.81%   | 33.15%             | -11.40% |     0.68 |       36 | 26.79%     | ok               |

## LDO-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 24.99%   | -84.92%            | -46.95% |     0.48 |       81 | 51.92%     | ok               |
|          20 | 13.39%   | -84.92%            | -44.97% |     0.4  |       85 | 47.32%     | ok               |
|          50 | 15.22%   | -84.92%            | -48.04% |     0.37 |       46 | 16.86%     | ok               |
|          30 | 1.95%    | -84.92%            | -60.93% |     0.29 |       74 | 37.93%     | ok               |
|          35 | -0.33%   | -84.92%            | -62.61% |     0.25 |       72 | 31.03%     | ok               |

## LIN Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 4.90%    | 27.39%             | -23.68% |     0.22 |       64 | 49.92%     | ok               |
|          25 | 3.57%    | 27.39%             | -22.01% |     0.18 |       65 | 41.76%     | ok               |
|          20 | 1.35%    | 27.39%             | -23.00% |     0.11 |       64 | 44.93%     | ok               |
|          35 | -0.17%   | 27.39%             | -21.18% |     0.05 |       64 | 32.45%     | ok               |
|          30 | -0.80%   | 27.39%             | -21.53% |     0.03 |       68 | 38.94%     | ok               |

## LINK-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -13.55%  | -67.23%            | -50.48% |     0.1  |       70 | 41.57%     | ok               |
|          45 | -13.92%  | -67.23%            | -38.56% |     0.04 |       50 | 26.44%     | ok               |
|          50 | -13.50%  | -67.23%            | -36.98% |     0.02 |       40 | 21.07%     | ok               |
|          35 | -24.89%  | -67.23%            | -49.56% |    -0.06 |       60 | 36.59%     | ok               |
|          40 | -29.01%  | -67.23%            | -50.91% |    -0.15 |       56 | 30.84%     | ok               |

## LLY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 24.98%   | 70.87%             | -38.23% |     0.53 |       42 | 38.94%     | ok               |
|          45 | 11.63%   | 70.87%             | -42.66% |     0.32 |       50 | 42.26%     | ok               |
|          15 | 5.64%    | 70.87%             | -48.12% |     0.22 |       63 | 61.90%     | ok               |
|          40 | -4.74%   | 70.87%             | -46.23% |     0.04 |       62 | 44.93%     | ok               |
|          20 | -11.37%  | 70.87%             | -51.34% |    -0.05 |       72 | 56.91%     | ok               |

## LRCX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 16.15%   | 384.20%            | -60.45% |     0.35 |       83 | 55.57%     | ok               |
|          50 | 9.46%    | 384.20%            | -50.39% |     0.28 |       80 | 37.44%     | ok               |
|          40 | 6.18%    | 384.20%            | -56.86% |     0.24 |       72 | 43.26%     | ok               |
|          35 | -0.72%   | 384.20%            | -61.76% |     0.16 |       80 | 45.26%     | ok               |
|          20 | -3.60%   | 384.20%            | -67.64% |     0.14 |       87 | 51.25%     | ok               |

## LTC-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -12.22%  | -64.38%            | -44.78% |    -0    |       56 | 31.80%     | ok               |
|          35 | -22.47%  | -64.38%            | -54.86% |    -0.13 |       66 | 42.91%     | ok               |
|          30 | -34.00%  | -64.38%            | -53.76% |    -0.29 |       66 | 48.47%     | ok               |
|          40 | -31.40%  | -64.38%            | -56.10% |    -0.3  |       58 | 38.12%     | ok               |
|          25 | -36.79%  | -64.38%            | -54.26% |    -0.33 |       74 | 50.96%     | ok               |

## MCD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 2.49%    | -7.60%             | -9.22%  |     0.17 |       42 | 20.47%     | ok               |
|          30 | -2.55%   | -7.60%             | -18.81% |    -0.05 |       75 | 38.10%     | ok               |
|          25 | -3.59%   | -7.60%             | -20.47% |    -0.09 |       75 | 40.77%     | ok               |
|          35 | -7.68%   | -7.60%             | -15.45% |    -0.29 |       67 | 34.44%     | ok               |
|          40 | -7.95%   | -7.60%             | -16.86% |    -0.33 |       71 | 28.79%     | ok               |

## META Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 7.11%    | 40.60%             | -31.03% |     0.24 |       66 | 39.93%     | ok               |
|          40 | -4.66%   | 40.60%             | -35.11% |     0.05 |       66 | 42.93%     | ok               |
|          50 | -9.24%   | 40.60%             | -34.00% |    -0.05 |       70 | 36.11%     | ok               |
|          25 | -14.07%  | 40.60%             | -39.84% |    -0.09 |       67 | 53.58%     | ok               |
|          35 | -15.61%  | 40.60%             | -34.87% |    -0.14 |       77 | 47.75%     | ok               |

## MPC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 14.51%   | 54.42%             | -23.96% |     0.37 |       52 | 38.60%     | ok               |
|          45 | 7.25%    | 54.42%             | -25.09% |     0.24 |       58 | 42.26%     | ok               |
|          40 | 5.62%    | 54.42%             | -25.70% |     0.22 |       60 | 44.59%     | ok               |
|          35 | 2.36%    | 54.42%             | -35.90% |     0.16 |       68 | 47.09%     | ok               |
|          30 | -13.74%  | 54.42%             | -44.76% |    -0.14 |       71 | 49.92%     | ok               |

## MRK Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -17.86%  | -4.78%             | -30.12% |    -0.3  |       87 | 57.40%     | ok               |
|          25 | -17.46%  | -4.78%             | -31.07% |    -0.32 |       72 | 49.42%     | ok               |
|          20 | -21.51%  | -4.78%             | -29.59% |    -0.42 |       77 | 52.75%     | ok               |
|          45 | -20.40%  | -4.78%             | -26.02% |    -0.51 |       57 | 35.61%     | ok               |
|          50 | -19.50%  | -4.78%             | -25.69% |    -0.52 |       58 | 32.45%     | ok               |

## MS Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 1.67%    | 159.18%            | -19.99% |     0.12 |       70 | 40.27%     | ok               |
|          35 | -5.47%   | 159.18%            | -25.26% |    -0.06 |       76 | 44.93%     | ok               |
|          15 | -10.26%  | 159.18%            | -24.00% |    -0.13 |       80 | 57.07%     | ok               |
|          20 | -10.36%  | 159.18%            | -25.68% |    -0.16 |       84 | 53.24%     | ok               |
|          30 | -12.08%  | 159.18%            | -27.79% |    -0.22 |       81 | 48.59%     | ok               |

## MSFT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -17.54%  | -10.34%            | -26.27% |    -0.48 |       66 | 35.27%     | ok               |
|          50 | -21.26%  | -10.34%            | -28.83% |    -0.64 |       64 | 30.62%     | ok               |
|          35 | -30.87%  | -10.34%            | -35.08% |    -0.83 |       75 | 43.76%     | ok               |
|          40 | -30.21%  | -10.34%            | -34.46% |    -0.84 |       71 | 38.60%     | ok               |
|          25 | -34.24%  | -10.34%            | -38.91% |    -0.88 |       87 | 51.41%     | ok               |

## MU Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 421.65%  | 1260.03%           | -61.96% |     1.55 |       48 | 68.05%     | ok               |
|          25 | 334.60%  | 1260.03%           | -67.90% |     1.46 |       49 | 61.73%     | ok               |
|          40 | 288.27%  | 1260.03%           | -64.30% |     1.4  |       56 | 55.07%     | ok               |
|          20 | 297.89%  | 1260.03%           | -67.25% |     1.37 |       55 | 63.89%     | ok               |
|          30 | 270.20%  | 1260.03%           | -68.76% |     1.34 |       51 | 59.90%     | ok               |

## NEAR-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 103.12%  | -62.19%            | -48.01% |     0.99 |       44 | 23.37%     | ok               |
|          50 | 70.90%   | -62.19%            | -53.13% |     0.82 |       38 | 18.39%     | ok               |
|          40 | 60.91%   | -62.19%            | -56.35% |     0.73 |       48 | 27.78%     | ok               |
|          35 | 34.38%   | -62.19%            | -60.30% |     0.54 |       70 | 33.33%     | ok               |
|          15 | 14.09%   | -62.19%            | -54.94% |     0.41 |       89 | 56.51%     | ok               |

## NEM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 18.05%   | 193.80%            | -29.41% |     0.38 |       62 | 64.06%     | ok               |
|          20 | 6.94%    | 193.80%            | -30.47% |     0.25 |       74 | 59.57%     | ok               |
|          50 | -13.83%  | 193.80%            | -33.36% |    -0.07 |       60 | 41.43%     | ok               |
|          25 | -17.18%  | 193.80%            | -37.89% |    -0.08 |       72 | 57.07%     | ok               |
|          30 | -29.37%  | 193.80%            | -38.49% |    -0.29 |       78 | 54.74%     | ok               |

## NFLX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 60.89%   | 26.57%             | -11.94% |     1.21 |       46 | 47.25%     | ok               |
|          50 | 47.22%   | 26.57%             | -16.28% |     1.05 |       48 | 39.77%     | ok               |
|          35 | 52.12%   | 26.57%             | -18.30% |     1.02 |       62 | 50.92%     | ok               |
|          45 | 43.49%   | 26.57%             | -15.48% |     0.96 |       52 | 43.59%     | ok               |
|          25 | 41.35%   | 26.57%             | -21.09% |     0.83 |       62 | 57.40%     | ok               |

## NKE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -35.58%  | -58.42%            | -50.44% |    -0.46 |       95 | 52.75%     | ok               |
|          40 | -26.46%  | -58.42%            | -31.19% |    -0.5  |       63 | 30.12%     | ok               |
|          15 | -39.58%  | -58.42%            | -55.52% |    -0.54 |       96 | 57.40%     | ok               |
|          35 | -39.10%  | -58.42%            | -43.08% |    -0.8  |       75 | 37.10%     | ok               |
|          50 | -24.86%  | -58.42%            | -31.53% |    -0.82 |       46 | 17.14%     | ok               |

## NOW Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 25.42%   | -40.93%            | -30.25% |     0.46 |       80 | 45.92%     | ok               |
|          20 | 25.98%   | -40.93%            | -26.36% |     0.46 |       79 | 51.91%     | ok               |
|          15 | 22.49%   | -40.93%            | -26.36% |     0.42 |       87 | 55.07%     | ok               |
|          35 | 17.32%   | -40.93%            | -29.30% |     0.38 |       81 | 40.60%     | ok               |
|          25 | 18.29%   | -40.93%            | -25.70% |     0.38 |       72 | 49.25%     | ok               |

## NVDA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -8.17%   | 125.42%            | -33.22% |     0.05 |       68 | 50.80%     | ok               |
|          30 | -9.90%   | 125.42%            | -35.26% |     0.01 |       70 | 48.48%     | ok               |
|          20 | -14.27%  | 125.42%            | -40.59% |    -0.02 |       71 | 55.26%     | ok               |
|          50 | -17.37%  | 125.42%            | -40.84% |    -0.16 |       60 | 32.62%     | ok               |
|          35 | -20.46%  | 125.42%            | -41.25% |    -0.18 |       82 | 45.63%     | ok               |

## OP-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 74.65%   | -94.46%            | -45.76% |     0.86 |       36 | 17.43%     | ok               |
|          50 | 66.86%   | -94.46%            | -36.11% |     0.86 |       34 | 12.45%     | ok               |
|          40 | 53.12%   | -94.46%            | -53.61% |     0.68 |       50 | 26.25%     | ok               |
|          35 | 27.44%   | -94.46%            | -58.33% |     0.48 |       58 | 29.31%     | ok               |
|          30 | 4.19%    | -94.46%            | -70.27% |     0.29 |       74 | 35.82%     | ok               |

## ORCL Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 149.29%  | 53.91%             | -29.32% |     1.08 |       74 | 65.22%     | ok               |
|          25 | 87.01%   | 53.91%             | -27.76% |     0.82 |       75 | 57.74%     | ok               |
|          20 | 83.80%   | 53.91%             | -29.32% |     0.8  |       77 | 60.90%     | ok               |
|          35 | 60.34%   | 53.91%             | -31.95% |     0.68 |       68 | 49.42%     | ok               |
|          30 | 60.48%   | 53.91%             | -29.47% |     0.67 |       74 | 53.58%     | ok               |

## OXY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 2.48%    | -10.68%            | -30.85% |     0.16 |       63 | 43.09%     | ok               |
|          35 | -0.66%   | -10.68%            | -30.50% |     0.1  |       68 | 38.60%     | ok               |
|          50 | -1.47%   | -10.68%            | -31.07% |     0.07 |       38 | 27.95%     | ok               |
|          40 | -3.09%   | -10.68%            | -32.21% |     0.05 |       56 | 34.61%     | ok               |
|          25 | -11.70%  | -10.68%            | -40.42% |    -0.09 |       71 | 46.59%     | ok               |

## PEP Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 9.33%    | -16.32%            | -11.62% |     0.43 |       48 | 27.62%     | ok               |
|          45 | 0.13%    | -16.32%            | -14.22% |     0.06 |       72 | 32.61%     | ok               |
|          40 | -3.39%   | -16.32%            | -18.04% |    -0.07 |       80 | 38.44%     | ok               |
|          35 | -4.60%   | -16.32%            | -21.42% |    -0.08 |       87 | 43.59%     | ok               |
|          30 | -9.64%   | -16.32%            | -21.35% |    -0.22 |       85 | 50.25%     | ok               |

## PEPE-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 21.63%   | -84.69%            | -57.66% |     0.45 |       75 | 43.68%     | ok               |
|          35 | 14.70%   | -84.69%            | -51.35% |     0.39 |       60 | 38.31%     | ok               |
|          15 | 5.14%    | -84.69%            | -64.84% |     0.37 |       76 | 58.81%     | ok               |
|          25 | -0.45%   | -84.69%            | -53.88% |     0.28 |       81 | 48.85%     | ok               |
|          20 | -18.03%  | -84.69%            | -64.07% |     0.14 |       82 | 55.17%     | ok               |

## PFE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -24.35%  | -8.73%             | -26.78% |    -0.87 |       52 | 20.63%     | ok               |
|          50 | -26.64%  | -8.73%             | -28.02% |    -1.05 |       44 | 16.81%     | ok               |
|          40 | -30.76%  | -8.73%             | -32.98% |    -1.06 |       76 | 25.46%     | ok               |
|          35 | -33.28%  | -8.73%             | -36.39% |    -1.07 |       82 | 32.45%     | ok               |
|          30 | -39.46%  | -8.73%             | -42.29% |    -1.25 |       77 | 35.94%     | ok               |

## PG Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -1.81%   | -5.43%             | -19.77% |    -0.03 |       52 | 34.94%     | ok               |
|          35 | -3.99%   | -5.43%             | -18.66% |    -0.11 |       60 | 38.27%     | ok               |
|          30 | -12.71%  | -5.43%             | -21.65% |    -0.46 |       62 | 41.43%     | ok               |
|          45 | -11.40%  | -5.43%             | -20.43% |    -0.48 |       52 | 32.45%     | ok               |
|          25 | -13.76%  | -5.43%             | -22.55% |    -0.5  |       72 | 42.60%     | ok               |

## PM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | -1.03%   | 88.84%             | -32.20% |     0.07 |       90 | 53.74%     | ok               |
|          20 | -3.79%   | 88.84%             | -31.89% |     0.02 |       87 | 62.73%     | ok               |
|          30 | -4.21%   | 88.84%             | -33.68% |     0    |       83 | 57.74%     | ok               |
|          50 | -5.49%   | 88.84%             | -35.70% |    -0.06 |       74 | 41.93%     | ok               |
|          25 | -10.66%  | 88.84%             | -37.05% |    -0.14 |       81 | 60.07%     | ok               |

## POL-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 64.83%   | -83.72%            | -46.45% |     0.77 |       79 | 49.62%     | ok               |
|          25 | 51.54%   | -83.72%            | -46.72% |     0.66 |       68 | 57.66%     | ok               |
|          20 | 41.20%   | -83.72%            | -52.88% |     0.58 |       76 | 63.03%     | ok               |
|          15 | 40.10%   | -83.72%            | -58.42% |     0.57 |       76 | 68.39%     | ok               |
|          50 | 20.67%   | -83.72%            | -22.86% |     0.45 |       50 | 20.69%     | ok               |

## QCOM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -3.69%   | 48.29%             | -55.66% |     0.13 |       73 | 49.58%     | ok               |
|          35 | -5.95%   | 48.29%             | -51.84% |     0.09 |       83 | 44.93%     | ok               |
|          20 | -7.60%   | 48.29%             | -55.54% |     0.08 |       69 | 52.41%     | ok               |
|          30 | -16.22%  | 48.29%             | -57.69% |    -0.05 |       77 | 47.59%     | ok               |
|          15 | -22.96%  | 48.29%             | -59.01% |    -0.13 |       73 | 55.57%     | ok               |

## QQQ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | 22.96%   | 72.36%             | -12.88% |     0.62 |       57 | 49.08%     | ok               |
|          15 | 23.49%   | 72.36%             | -14.17% |     0.59 |       61 | 54.58%     | ok               |
|          30 | 18.95%   | 72.36%             | -12.88% |     0.55 |       62 | 46.26%     | ok               |
|          20 | 19.99%   | 72.36%             | -12.98% |     0.54 |       65 | 51.75%     | ok               |
|          35 | 6.79%    | 72.36%             | -18.29% |     0.26 |       68 | 42.60%     | ok               |

## RENDER-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 49.72%   | -61.32%            | -43.43% |     0.65 |       84 | 53.89%     | ok               |
|          15 | 32.34%   | -61.32%            | -44.59% |     0.55 |       84 | 56.97%     | ok               |
|          25 | 20.05%   | -61.32%            | -40.60% |     0.46 |       88 | 50.00%     | ok               |
|          30 | -17.59%  | -61.32%            | -45.00% |     0.11 |       96 | 43.65%     | ok               |
|          40 | -27.22%  | -61.32%            | -38.60% |    -0.1  |       70 | 29.10%     | ok               |

## RTX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 24.17%   | 101.85%            | -18.66% |     0.61 |       78 | 56.24%     | ok               |
|          50 | 17.10%   | 101.85%            | -18.42% |     0.55 |       58 | 42.10%     | ok               |
|          25 | 19.76%   | 101.85%            | -18.59% |     0.53 |       64 | 52.75%     | ok               |
|          30 | 17.94%   | 101.85%            | -16.99% |     0.49 |       58 | 51.58%     | ok               |
|          35 | 15.45%   | 101.85%            | -18.00% |     0.48 |       56 | 49.75%     | ok               |

## SBUX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -18.54%  | 6.77%              | -23.55% |    -0.33 |       65 | 41.10%     | ok               |
|          45 | -21.25%  | 6.77%              | -27.26% |    -0.52 |       68 | 28.95%     | ok               |
|          40 | -23.15%  | 6.77%              | -27.00% |    -0.53 |       62 | 32.95%     | ok               |
|          30 | -25.50%  | 6.77%              | -29.34% |    -0.53 |       64 | 38.77%     | ok               |
|          20 | -30.10%  | 6.77%              | -34.85% |    -0.6  |       70 | 43.09%     | ok               |

## SCHW Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 1.55%    | 43.93%             | -15.92% |     0.12 |       54 | 33.28%     | ok               |
|          50 | -2.36%   | 43.93%             | -12.59% |    -0.02 |       48 | 30.78%     | ok               |
|          25 | -10.23%  | 43.93%             | -28.76% |    -0.16 |       61 | 47.75%     | ok               |
|          40 | -8.98%   | 43.93%             | -21.81% |    -0.18 |       62 | 36.27%     | ok               |
|          20 | -11.91%  | 43.93%             | -29.24% |    -0.2  |       69 | 50.42%     | ok               |

## SHIB-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 0.47%    | -79.52%            | -49.21% |     0.25 |       78 | 68.58%     | ok               |
|          25 | -5.28%   | -79.52%            | -43.85% |     0.18 |       75 | 59.39%     | ok               |
|          20 | -9.86%   | -79.52%            | -46.38% |     0.14 |       77 | 63.79%     | ok               |
|          35 | -8.62%   | -79.52%            | -53.32% |     0.11 |       64 | 46.55%     | ok               |
|          40 | -15.26%  | -79.52%            | -49.96% |     0.01 |       54 | 38.89%     | ok               |

## SHY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd    |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:-------|---------:|---------:|:-----------|:-----------------|
|          30 | -2.32%   | -0.35%             | -2.85% |    -0.81 |       50 | 34.78%     | ok               |
|          35 | -2.44%   | -0.35%             | -3.27% |    -0.86 |       52 | 32.95%     | ok               |
|          40 | -2.56%   | -0.35%             | -3.33% |    -0.91 |       52 | 31.11%     | ok               |
|          45 | -2.53%   | -0.35%             | -3.23% |    -0.92 |       50 | 27.95%     | ok               |
|          50 | -2.71%   | -0.35%             | -3.40% |    -1.04 |       46 | 25.12%     | ok               |

## SKY-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -34.15%  | 3.34%              | -56.39% |    -0.39 |       58 | 51.04%     | ok               |
|          30 | -29.87%  | 3.34%              | -43.98% |    -0.39 |       68 | 40.60%     | ok               |
|          25 | -33.46%  | 3.34%              | -48.09% |    -0.45 |       63 | 44.32%     | ok               |
|          20 | -43.60%  | 3.34%              | -58.40% |    -0.64 |       60 | 48.03%     | ok               |
|          35 | -40.88%  | 3.34%              | -49.68% |    -0.75 |       62 | 34.11%     | ok               |

## SLB Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 11.23%   | -9.87%             | -24.10% |     0.32 |       48 | 35.61%     | ok               |
|          45 | 9.59%    | -9.87%             | -21.53% |     0.3  |       54 | 32.28%     | ok               |
|          50 | -10.05%  | -9.87%             | -29.84% |    -0.16 |       54 | 28.62%     | ok               |
|          35 | -16.64%  | -9.87%             | -42.55% |    -0.25 |       74 | 43.59%     | ok               |
|          30 | -30.05%  | -9.87%             | -54.95% |    -0.54 |       75 | 49.92%     | ok               |

## SLV Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 59.62%   | 177.75%            | -34.72% |     0.8  |       54 | 33.44%     | ok               |
|          45 | 57.09%   | 177.75%            | -32.46% |     0.78 |       58 | 34.28%     | ok               |
|          40 | 55.22%   | 177.75%            | -31.93% |     0.76 |       64 | 36.44%     | ok               |
|          35 | 44.28%   | 177.75%            | -36.89% |     0.66 |       64 | 38.44%     | ok               |
|          30 | 35.90%   | 177.75%            | -42.66% |     0.57 |       58 | 40.60%     | ok               |

## SMH Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 122.06%  | 251.17%            | -30.17% |     1.36 |       47 | 53.41%     | ok               |
|          35 | 98.74%   | 251.17%            | -34.36% |     1.23 |       54 | 49.25%     | ok               |
|          25 | 98.59%   | 251.17%            | -32.94% |     1.21 |       46 | 52.25%     | ok               |
|          30 | 96.25%   | 251.17%            | -33.99% |     1.2  |       48 | 50.58%     | ok               |
|          45 | 81.98%   | 251.17%            | -32.75% |     1.16 |       52 | 43.43%     | ok               |

## SNX-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 39.54%   | -86.45%            | -43.20% |     0.57 |       71 | 49.81%     | ok               |
|          35 | 30.36%   | -86.45%            | -28.28% |     0.51 |       64 | 32.57%     | ok               |
|          30 | 30.41%   | -86.45%            | -32.91% |     0.51 |       60 | 39.85%     | ok               |
|          25 | 9.70%    | -86.45%            | -38.05% |     0.34 |       72 | 44.25%     | ok               |
|          15 | -6.01%   | -86.45%            | -47.56% |     0.22 |       81 | 54.41%     | ok               |

## SOL-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -18.45%  | -72.52%            | -54.68% |     0.03 |       64 | 39.27%     | ok               |
|          25 | -32.68%  | -72.52%            | -53.21% |    -0.09 |       72 | 57.66%     | ok               |
|          35 | -33.64%  | -72.52%            | -61.96% |    -0.13 |       72 | 46.74%     | ok               |
|          15 | -37.97%  | -72.52%            | -59.14% |    -0.14 |       74 | 64.75%     | ok               |
|          20 | -42.35%  | -72.52%            | -56.90% |    -0.22 |       68 | 60.15%     | ok               |

## SOXX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 99.11%   | 225.34%            | -38.67% |     1.16 |       53 | 52.08%     | ok               |
|          25 | 95.30%   | 225.34%            | -39.85% |     1.13 |       51 | 51.75%     | ok               |
|          35 | 89.84%   | 225.34%            | -38.63% |     1.11 |       59 | 47.09%     | ok               |
|          15 | 94.11%   | 225.34%            | -37.72% |     1.09 |       66 | 54.91%     | ok               |
|          30 | 84.32%   | 225.34%            | -40.34% |     1.05 |       55 | 49.58%     | ok               |

## SPY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 17.82%   | 51.52%             | -14.25% |     0.61 |       58 | 54.41%     | ok               |
|          15 | 16.25%   | 51.52%             | -16.80% |     0.55 |       67 | 57.57%     | ok               |
|          25 | 10.49%   | 51.52%             | -15.22% |     0.4  |       58 | 53.41%     | ok               |
|          30 | 6.50%    | 51.52%             | -16.47% |     0.28 |       60 | 50.92%     | ok               |
|          35 | 3.93%    | 51.52%             | -16.72% |     0.2  |       58 | 48.25%     | ok               |

## SUSHI-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -24.39%  | -88.75%            | -40.79% |    -0.2  |       52 | 14.56%     | ok               |
|          45 | -56.30%  | -88.75%            | -64.69% |    -0.71 |       54 | 17.82%     | ok               |
|          40 | -59.39%  | -88.75%            | -66.97% |    -0.72 |       61 | 24.33%     | ok               |
|          35 | -67.00%  | -88.75%            | -75.30% |    -0.85 |       76 | 29.69%     | ok               |
|          15 | -80.09%  | -88.75%            | -81.81% |    -0.99 |       88 | 47.13%     | ok               |

## T Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 60.42%   | 28.12%             | -18.13% |     1.2  |       55 | 55.24%     | ok               |
|          25 | 52.20%   | 28.12%             | -17.66% |     1.09 |       60 | 52.91%     | ok               |
|          15 | 51.66%   | 28.12%             | -15.08% |     1.04 |       64 | 59.07%     | ok               |
|          30 | 37.01%   | 28.12%             | -17.01% |     0.86 |       62 | 50.75%     | ok               |
|          35 | 34.43%   | 28.12%             | -14.49% |     0.83 |       62 | 47.59%     | ok               |

## TGT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -8.23%   | -8.33%             | -41.89% |    -0.05 |       79 | 46.09%     | ok               |
|          15 | -11.23%  | -8.33%             | -39.76% |    -0.1  |       69 | 50.58%     | ok               |
|          25 | -10.93%  | -8.33%             | -43.53% |    -0.13 |       61 | 41.26%     | ok               |
|          45 | -10.17%  | -8.33%             | -30.47% |    -0.16 |       50 | 28.95%     | ok               |
|          30 | -11.79%  | -8.33%             | -41.74% |    -0.16 |       56 | 38.60%     | ok               |

## TIA-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 39.46%   | -91.97%            | -31.28% |     0.58 |       62 | 25.10%     | ok               |
|          35 | 33.70%   | -91.97%            | -36.61% |     0.53 |       62 | 29.69%     | ok               |
|          45 | 17.16%   | -91.97%            | -44.21% |     0.39 |       52 | 18.77%     | ok               |
|          50 | 12.07%   | -91.97%            | -44.86% |     0.33 |       32 | 11.69%     | ok               |
|          30 | -16.62%  | -91.97%            | -55.19% |     0.07 |       86 | 34.67%     | ok               |

## TLT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -22.66%  | -9.25%             | -23.95% |    -1.68 |       70 | 31.95%     | ok               |
|          50 | -16.73%  | -9.25%             | -18.47% |    -1.8  |       32 | 14.48%     | ok               |
|          40 | -21.20%  | -9.25%             | -23.26% |    -1.9  |       58 | 21.13%     | ok               |
|          15 | -28.58%  | -9.25%             | -30.26% |    -1.95 |       78 | 40.10%     | ok               |
|          35 | -23.46%  | -9.25%             | -24.74% |    -1.96 |       66 | 26.12%     | ok               |

## TMO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 40.93%   | -16.81%            | -10.55% |     0.94 |       38 | 30.12%     | ok               |
|          45 | 40.14%   | -16.81%            | -12.29% |     0.9  |       46 | 35.11%     | ok               |
|          40 | 38.07%   | -16.81%            | -12.07% |     0.85 |       49 | 39.60%     | ok               |
|          35 | 22.16%   | -16.81%            | -16.12% |     0.54 |       59 | 43.93%     | ok               |
|          30 | 10.02%   | -16.81%            | -16.83% |     0.3  |       59 | 47.75%     | ok               |

## TMUS Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 16.01%   | 10.41%             | -26.87% |     0.41 |       71 | 59.90%     | ok               |
|          30 | 13.79%   | 10.41%             | -24.50% |     0.38 |       72 | 47.92%     | ok               |
|          20 | 8.88%    | 10.41%             | -24.82% |     0.28 |       73 | 54.24%     | ok               |
|          25 | 6.82%    | 10.41%             | -25.91% |     0.24 |       77 | 50.42%     | ok               |
|          50 | 4.50%    | 10.41%             | -22.71% |     0.2  |       58 | 35.77%     | ok               |

## TRX-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 2.99%    | 37.68%             | -18.79% |     0.17 |       54 | 38.12%     | ok               |
|          30 | 2.43%    | 37.68%             | -22.90% |     0.15 |       74 | 49.43%     | ok               |
|          35 | 1.04%    | 37.68%             | -21.77% |     0.12 |       70 | 46.74%     | ok               |
|          25 | 0.59%    | 37.68%             | -26.84% |     0.11 |       70 | 52.68%     | ok               |
|          50 | -0.44%   | 37.68%             | -18.49% |     0.06 |       46 | 32.57%     | ok               |

## TSLA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 70.53%   | 112.15%            | -32.60% |     0.84 |       64 | 30.45%     | ok               |
|          40 | 61.95%   | 112.15%            | -45.90% |     0.73 |       61 | 34.94%     | ok               |
|          45 | 37.20%   | 112.15%            | -46.86% |     0.55 |       65 | 32.28%     | ok               |
|          35 | 18.08%   | 112.15%            | -54.51% |     0.38 |       74 | 37.94%     | ok               |
|          30 | -4.12%   | 112.15%            | -57.89% |     0.16 |       68 | 42.43%     | ok               |

## TXN Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 13.31%   | 100.12%            | -45.45% |     0.33 |       70 | 35.27%     | ok               |
|          20 | 3.67%    | 100.12%            | -38.98% |     0.2  |       63 | 60.07%     | ok               |
|          15 | 1.58%    | 100.12%            | -39.48% |     0.18 |       64 | 64.23%     | ok               |
|          40 | -3.13%   | 100.12%            | -45.67% |     0.08 |       76 | 47.75%     | ok               |
|          35 | -4.23%   | 100.12%            | -43.38% |     0.07 |       78 | 50.08%     | ok               |

## UNH Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 27.11%   | -19.40%            | -36.92% |     0.51 |       50 | 28.79%     | ok               |
|          30 | 24.49%   | -19.40%            | -27.46% |     0.46 |       78 | 51.75%     | ok               |
|          15 | 21.02%   | -19.40%            | -30.48% |     0.41 |       81 | 66.89%     | ok               |
|          35 | 19.89%   | -19.40%            | -29.39% |     0.41 |       72 | 46.42%     | ok               |
|          20 | 17.26%   | -19.40%            | -31.00% |     0.37 |       83 | 61.56%     | ok               |

## UNI-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -15.35%  | -78.87%            | -57.12% |     0.03 |       54 | 25.29%     | ok               |
|          40 | -23.44%  | -78.87%            | -63.75% |    -0.05 |       56 | 30.65%     | ok               |
|          50 | -23.03%  | -78.87%            | -55.74% |    -0.1  |       52 | 20.69%     | ok               |
|          35 | -35.75%  | -78.87%            | -68.71% |    -0.18 |       70 | 35.63%     | ok               |
|          20 | -72.87%  | -78.87%            | -81.22% |    -0.75 |      102 | 52.30%     | ok               |

## UPS Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -36.18%  | -32.14%            | -42.28% |    -0.69 |       74 | 44.59%     | ok               |
|          35 | -34.91%  | -32.14%            | -40.47% |    -0.7  |       59 | 34.28%     | ok               |
|          20 | -37.25%  | -32.14%            | -45.80% |    -0.71 |       80 | 47.75%     | ok               |
|          30 | -37.30%  | -32.14%            | -40.62% |    -0.74 |       66 | 39.93%     | ok               |
|          40 | -36.21%  | -32.14%            | -42.12% |    -0.76 |       51 | 29.12%     | ok               |

## USO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 15.25%   | 56.41%             | -33.25% |     0.36 |       46 | 27.45%     | ok               |
|          30 | 2.80%    | 56.41%             | -43.35% |     0.17 |       68 | 34.44%     | ok               |
|          40 | 1.81%    | 56.41%             | -41.14% |     0.15 |       57 | 29.95%     | ok               |
|          50 | 2.11%    | 56.41%             | -31.13% |     0.15 |       54 | 24.96%     | ok               |
|          25 | -1.92%   | 56.41%             | -45.95% |     0.1  |       68 | 36.94%     | ok               |

## VEA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 5.44%    | 51.73%             | -16.28% |     0.25 |       60 | 50.58%     | ok               |
|          20 | 1.19%    | 51.73%             | -17.70% |     0.1  |       61 | 47.92%     | ok               |
|          25 | -0.82%   | 51.73%             | -17.79% |     0.02 |       57 | 46.26%     | ok               |
|          30 | -0.98%   | 51.73%             | -17.93% |     0.01 |       58 | 44.09%     | ok               |
|          35 | -2.09%   | 51.73%             | -16.79% |    -0.03 |       56 | 43.09%     | ok               |

## VIXY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -46.17%  | -62.61%            | -68.69% |    -0.39 |       44 | 10.32%     | ok               |
|          45 | -56.13%  | -62.61%            | -74.13% |    -0.55 |       56 | 16.31%     | ok               |
|          40 | -64.45%  | -62.61%            | -80.03% |    -0.66 |       70 | 20.63%     | ok               |
|          35 | -68.17%  | -62.61%            | -83.81% |    -0.7  |       86 | 25.79%     | ok               |
|          15 | -76.54%  | -62.61%            | -89.47% |    -0.76 |      103 | 44.26%     | ok               |

## VNQ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -8.60%   | 12.97%             | -19.07% |    -0.37 |       60 | 28.62%     | ok               |
|          50 | -9.03%   | 12.97%             | -17.13% |    -0.41 |       56 | 26.12%     | ok               |
|          25 | -13.12%  | 12.97%             | -22.34% |    -0.51 |       69 | 40.77%     | ok               |
|          40 | -14.13%  | 12.97%             | -24.84% |    -0.62 |       74 | 32.11%     | ok               |
|          20 | -16.52%  | 12.97%             | -23.79% |    -0.64 |       74 | 43.59%     | ok               |

## VTI Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 19.29%   | 50.95%             | -13.96% |     0.64 |       62 | 55.74%     | ok               |
|          15 | 13.18%   | 50.95%             | -15.70% |     0.46 |       65 | 58.24%     | ok               |
|          25 | 6.34%    | 50.95%             | -16.10% |     0.27 |       58 | 53.91%     | ok               |
|          30 | -0.72%   | 50.95%             | -18.77% |     0.04 |       66 | 52.08%     | ok               |
|          40 | -2.95%   | 50.95%             | -20.44% |    -0.05 |       68 | 45.42%     | ok               |

## VWO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -6.69%   | 52.45%             | -21.68% |    -0.22 |       58 | 32.61%     | ok               |
|          15 | -9.03%   | 52.45%             | -24.01% |    -0.26 |       69 | 49.42%     | ok               |
|          45 | -8.51%   | 52.45%             | -23.75% |    -0.3  |       60 | 35.11%     | ok               |
|          20 | -10.06%  | 52.45%             | -26.14% |    -0.31 |       67 | 47.25%     | ok               |
|          40 | -8.98%   | 52.45%             | -23.57% |    -0.31 |       70 | 37.94%     | ok               |

## VZ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -5.46%   | 7.87%              | -16.98% |    -0.15 |       50 | 25.29%     | ok               |
|          45 | -13.94%  | 7.87%              | -20.38% |    -0.46 |       58 | 28.29%     | ok               |
|          35 | -19.03%  | 7.87%              | -24.68% |    -0.63 |       61 | 33.78%     | ok               |
|          25 | -22.06%  | 7.87%              | -28.84% |    -0.68 |       80 | 41.76%     | ok               |
|          40 | -21.83%  | 7.87%              | -26.72% |    -0.77 |       64 | 30.78%     | ok               |

## WFC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -0.98%   | 66.51%             | -18.29% |     0.04 |       58 | 33.28%     | ok               |
|          35 | -5.28%   | 66.51%             | -22.53% |    -0.04 |       79 | 44.93%     | ok               |
|          45 | -8.25%   | 66.51%             | -24.02% |    -0.17 |       66 | 37.94%     | ok               |
|          20 | -16.91%  | 66.51%             | -29.96% |    -0.24 |       79 | 54.24%     | ok               |
|          40 | -11.93%  | 66.51%             | -24.88% |    -0.28 |       76 | 41.26%     | ok               |

## WIF-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 81.89%   | -90.70%            | -46.21% |     0.76 |       73 | 41.57%     | ok               |
|          20 | 75.46%   | -90.70%            | -40.67% |     0.73 |       67 | 38.89%     | ok               |
|          25 | 0.35%    | -90.70%            | -52.41% |     0.3  |       69 | 36.40%     | ok               |
|          30 | -36.39%  | -90.70%            | -57.06% |    -0.12 |       70 | 32.38%     | ok               |
|          50 | -20.06%  | -90.70%            | -37.87% |    -0.14 |       40 | 12.07%     | ok               |

## WMT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 61.06%   | 113.00%            | -9.18%  |     1.57 |       36 | 43.93%     | ok               |
|          50 | 54.52%   | 113.00%            | -12.19% |     1.51 |       30 | 41.76%     | ok               |
|          40 | 50.99%   | 113.00%            | -9.18%  |     1.34 |       40 | 45.09%     | ok               |
|          35 | 48.76%   | 113.00%            | -10.11% |     1.25 |       50 | 49.08%     | ok               |
|          30 | 27.23%   | 113.00%            | -21.31% |     0.74 |       57 | 51.58%     | ok               |

## XBI Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 4.14%    | 60.64%             | -16.56% |     0.19 |       60 | 34.78%     | ok               |
|          45 | 3.34%    | 60.64%             | -16.74% |     0.17 |       52 | 31.61%     | ok               |
|          35 | -0.17%   | 60.64%             | -21.24% |     0.08 |       60 | 38.10%     | ok               |
|          30 | -1.28%   | 60.64%             | -21.61% |     0.05 |       60 | 39.77%     | ok               |
|          25 | -5.82%   | 60.64%             | -24.65% |    -0.05 |       68 | 41.76%     | ok               |

## XLB Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -4.67%   | 24.51%             | -20.60% |    -0.12 |       60 | 32.11%     | ok               |
|          50 | -4.61%   | 24.51%             | -17.40% |    -0.14 |       44 | 27.79%     | ok               |
|          35 | -7.91%   | 24.51%             | -23.62% |    -0.24 |       60 | 35.61%     | ok               |
|          45 | -7.43%   | 24.51%             | -20.61% |    -0.25 |       44 | 29.28%     | ok               |
|          25 | -12.31%  | 24.51%             | -23.73% |    -0.4  |       70 | 41.43%     | ok               |

## XLC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 17.01%   | 36.42%             | -12.33% |     0.58 |       65 | 55.57%     | ok               |
|          25 | 14.80%   | 36.42%             | -12.31% |     0.51 |       62 | 57.40%     | ok               |
|          40 | 12.30%   | 36.42%             | -13.38% |     0.47 |       68 | 48.25%     | ok               |
|          35 | 11.67%   | 36.42%             | -13.38% |     0.44 |       64 | 52.58%     | ok               |
|          20 | 6.73%    | 36.42%             | -13.78% |     0.27 |       70 | 60.07%     | ok               |

## XLE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -1.92%   | 28.52%             | -25.98% |     0.02 |       56 | 36.77%     | ok               |
|          35 | -3.79%   | 28.52%             | -32.17% |    -0.02 |       65 | 44.59%     | ok               |
|          45 | -5.17%   | 28.52%             | -30.88% |    -0.07 |       62 | 39.60%     | ok               |
|          30 | -9.48%   | 28.52%             | -36.18% |    -0.17 |       71 | 46.59%     | ok               |
|          25 | -10.53%  | 28.52%             | -36.92% |    -0.18 |       78 | 49.92%     | ok               |

## XLF Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -5.44%   | 38.58%             | -18.01% |    -0.12 |       66 | 53.91%     | ok               |
|          15 | -9.35%   | 38.58%             | -19.58% |    -0.26 |       74 | 56.74%     | ok               |
|          30 | -11.27%  | 38.58%             | -23.61% |    -0.37 |       74 | 48.25%     | ok               |
|          25 | -12.04%  | 38.58%             | -23.22% |    -0.39 |       75 | 50.42%     | ok               |
|          35 | -18.44%  | 38.58%             | -26.29% |    -0.73 |       66 | 44.09%     | ok               |

## XLI Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 11.07%   | 59.24%             | -10.36% |     0.43 |       72 | 53.24%     | ok               |
|          20 | 6.74%    | 59.24%             | -12.74% |     0.3  |       63 | 49.08%     | ok               |
|          30 | 4.40%    | 59.24%             | -11.38% |     0.22 |       64 | 46.59%     | ok               |
|          45 | 3.80%    | 59.24%             | -12.27% |     0.21 |       62 | 37.77%     | ok               |
|          50 | 3.49%    | 59.24%             | -9.25%  |     0.2  |       56 | 35.77%     | ok               |

## XLK Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 83.14%   | 88.75%             | -14.75% |     1.33 |       41 | 53.58%     | ok               |
|          20 | 68.81%   | 88.75%             | -14.75% |     1.19 |       48 | 51.41%     | ok               |
|          25 | 65.37%   | 88.75%             | -14.75% |     1.19 |       42 | 49.25%     | ok               |
|          30 | 63.21%   | 88.75%             | -14.75% |     1.18 |       42 | 48.09%     | ok               |
|          35 | 45.00%   | 88.75%             | -13.61% |     0.94 |       54 | 45.42%     | ok               |

## XLM-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 11.39%   | -59.03%            | -38.97% |     0.32 |       46 | 27.59%     | ok               |
|          45 | 8.04%    | -59.03%            | -43.99% |     0.29 |       52 | 31.23%     | ok               |
|          30 | -8.71%   | -59.03%            | -48.82% |     0.13 |       71 | 45.79%     | ok               |
|          40 | -14.37%  | -59.03%            | -43.80% |     0.04 |       51 | 35.44%     | ok               |
|          35 | -16.70%  | -59.03%            | -48.88% |     0.02 |       71 | 41.76%     | ok               |

## XLP Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 11.84%   | 12.50%             | -5.66%  |     0.72 |       56 | 34.11%     | ok               |
|          50 | 9.69%    | 12.50%             | -6.08%  |     0.61 |       58 | 31.78%     | ok               |
|          40 | 9.59%    | 12.50%             | -7.77%  |     0.58 |       72 | 38.27%     | ok               |
|          35 | 8.63%    | 12.50%             | -9.73%  |     0.51 |       68 | 41.26%     | ok               |
|          30 | 6.70%    | 12.50%             | -11.16% |     0.41 |       70 | 42.76%     | ok               |

## XLU Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 8.61%    | 45.19%             | -9.11%  |     0.45 |       50 | 30.45%     | ok               |
|          45 | 6.38%    | 45.19%             | -10.56% |     0.35 |       54 | 31.45%     | ok               |
|          40 | 3.44%    | 45.19%             | -11.94% |     0.21 |       58 | 32.95%     | ok               |
|          35 | -0.55%   | 45.19%             | -16.24% |     0.02 |       62 | 35.27%     | ok               |
|          30 | -3.67%   | 45.19%             | -18.15% |    -0.12 |       69 | 38.27%     | ok               |

## XLV Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -11.08%  | 6.99%              | -16.83% |    -0.53 |       68 | 36.27%     | ok               |
|          25 | -12.39%  | 6.99%              | -18.06% |    -0.6  |       70 | 37.60%     | ok               |
|          15 | -16.37%  | 6.99%              | -21.47% |    -0.78 |       81 | 42.43%     | ok               |
|          20 | -16.30%  | 6.99%              | -21.56% |    -0.8  |       75 | 39.27%     | ok               |
|          35 | -15.73%  | 6.99%              | -20.96% |    -0.84 |       66 | 33.78%     | ok               |

## XLY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 3.11%    | 31.97%             | -12.94% |     0.16 |       72 | 41.76%     | ok               |
|          30 | 1.26%    | 31.97%             | -14.01% |     0.11 |       72 | 44.76%     | ok               |
|          15 | -0.76%   | 31.97%             | -15.77% |     0.05 |       76 | 51.58%     | ok               |
|          50 | -0.60%   | 31.97%             | -11.79% |     0.03 |       52 | 29.78%     | ok               |
|          40 | -3.75%   | 31.97%             | -16.99% |    -0.07 |       70 | 37.27%     | ok               |

## XOM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | 5.34%    | 34.27%             | -19.90% |     0.22 |       56 | 36.77%     | ok               |
|          30 | 4.30%    | 34.27%             | -20.29% |     0.19 |       56 | 36.11%     | ok               |
|          50 | 1.92%    | 34.27%             | -21.35% |     0.13 |       46 | 29.95%     | ok               |
|          20 | 1.45%    | 34.27%             | -25.56% |     0.12 |       61 | 39.27%     | ok               |
|          35 | -0.14%   | 34.27%             | -20.93% |     0.07 |       58 | 34.94%     | ok               |

## XRP-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | -29.67%  | -65.35%            | -48.69% |    -0.21 |       70 | 41.95%     | ok               |
|          40 | -36.21%  | -65.35%            | -46.96% |    -0.36 |       62 | 35.82%     | ok               |
|          30 | -42.86%  | -65.35%            | -57.60% |    -0.42 |       74 | 46.36%     | ok               |
|          45 | -43.39%  | -65.35%            | -48.88% |    -0.52 |       62 | 31.42%     | ok               |
|          50 | -40.94%  | -65.35%            | -39.27% |    -0.58 |       64 | 23.75%     | ok               |

## YFI-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -30.68%  | -77.98%            | -50.17% |    -0.41 |       60 | 27.20%     | ok               |
|          45 | -36.29%  | -77.98%            | -51.92% |    -0.62 |       62 | 22.61%     | ok               |
|          35 | -50.37%  | -77.98%            | -64.34% |    -0.77 |       71 | 34.48%     | ok               |
|          30 | -53.87%  | -77.98%            | -67.78% |    -0.79 |       81 | 40.42%     | ok               |
|          15 | -61.13%  | -77.98%            | -74.02% |    -0.83 |       83 | 54.60%     | ok               |

## ZEC-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 124.17%  | 753.05%            | -24.66% |     0.9  |       50 | 23.18%     | ok               |
|          35 | 92.19%   | 753.05%            | -44.34% |     0.77 |       60 | 31.03%     | ok               |
|          25 | 64.78%   | 753.05%            | -48.59% |     0.65 |       61 | 40.04%     | ok               |
|          50 | 54.10%   | 753.05%            | -37.94% |     0.6  |       52 | 20.69%     | ok               |
|          30 | 48.03%   | 753.05%            | -47.68% |     0.58 |       69 | 36.59%     | ok               |
