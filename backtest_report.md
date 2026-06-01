# Market Tracker Backtest Report

_Generated: 2026-06-01T01:44:13+00:00_

## Data Sources

- Crypto: Kraken -> Coinbase -> CoinGecko OHLC -> CoinPaprika fallback chain.
- Stocks / ETFs / indices: Stooq -> Yahoo Finance fallback chain.
- Data rows are generated from real market APIs. Mock OHLCV rows are not generated.

## Data Freshness

- Rows: **92,339**
- Symbols: **161**
- Date range: **2024-01-05** to **2026-06-01**

## Latest Signals

| symbol     | date                |         close |   composite_score | signal   | data_source   |
|:-----------|:--------------------|--------------:|------------------:|:---------|:--------------|
| AAPL       | 2026-05-29 00:00:00 |   312.06      |         62.0833   | LONG     | Yahoo Finance |
| ABBV       | 2026-05-29 00:00:00 |   217.72      |         63.5      | LONG     | Yahoo Finance |
| ALGO-USD   | 2026-06-01 00:00:00 |     0.12585   |         68.3333   | LONG     | Kraken API    |
| AMD        | 2026-05-29 00:00:00 |   516.1       |         63.4167   | LONG     | Yahoo Finance |
| BAC        | 2026-05-29 00:00:00 |    51.6       |         51.6667   | LONG     | Yahoo Finance |
| CL         | 2026-05-29 00:00:00 |    90.13      |         72.75     | LONG     | Yahoo Finance |
| CSCO       | 2026-05-29 00:00:00 |   120.42      |         72.0833   | LONG     | Yahoo Finance |
| DXY-INDEX  | 2026-05-31 00:00:00 |    99.058     |         83.6022   | LONG     | Yahoo Finance |
| FCX        | 2026-05-29 00:00:00 |    65.71      |         76.9167   | LONG     | Yahoo Finance |
| FET-USD    | 2026-06-01 00:00:00 |     0.265     |         41        | LONG     | Kraken API    |
| HBAR-USD   | 2026-06-01 00:00:00 |     0.09481   |         54.0833   | LONG     | Kraken API    |
| HON        | 2026-05-29 00:00:00 |   237.86      |         75.75     | LONG     | Yahoo Finance |
| HYG        | 2026-05-29 00:00:00 |    80.31      |         71.3333   | LONG     | Yahoo Finance |
| IBM        | 2026-05-29 00:00:00 |   297.8       |         63.75     | LONG     | Yahoo Finance |
| ICP-USD    | 2026-06-01 00:00:00 |     2.73      |         45.6667   | LONG     | Kraken API    |
| INJ-USD    | 2026-06-01 00:00:00 |     6.431     |         61.8333   | LONG     | Kraken API    |
| INTC       | 2026-05-29 00:00:00 |   114.68      |         33.4167   | LONG     | Yahoo Finance |
| ITA        | 2026-05-29 00:00:00 |   235.44      |         70.5833   | LONG     | Yahoo Finance |
| KO         | 2026-05-29 00:00:00 |    79.01      |         30.3333   | LONG     | Yahoo Finance |
| LLY        | 2026-05-29 00:00:00 |  1105         |         73.25     | LONG     | Yahoo Finance |
| META       | 2026-05-29 00:00:00 |   632.51      |         33.1667   | LONG     | Yahoo Finance |
| MRK        | 2026-05-29 00:00:00 |   118.72      |         73.4167   | LONG     | Yahoo Finance |
| MU         | 2026-05-29 00:00:00 |   971         |         65.0833   | LONG     | Yahoo Finance |
| NOW        | 2026-05-29 00:00:00 |   124.37      |         34.75     | LONG     | Yahoo Finance |
| ORCL       | 2026-05-29 00:00:00 |   225.78      |         60.0833   | LONG     | Yahoo Finance |
| PM         | 2026-05-29 00:00:00 |   177.38      |         30.5833   | LONG     | Yahoo Finance |
| QCOM       | 2026-05-29 00:00:00 |   251.02      |         63.4167   | LONG     | Yahoo Finance |
| QQQ        | 2026-05-29 00:00:00 |   738.31      |         51.4167   | LONG     | Yahoo Finance |
| RENDER-USD | 2026-06-01 00:00:00 |     2.087     |         70.9167   | LONG     | Kraken API    |
| SMH        | 2026-05-29 00:00:00 |   598.93      |         67.4167   | LONG     | Yahoo Finance |
| SOXX       | 2026-05-29 00:00:00 |   569.08      |         67.4167   | LONG     | Yahoo Finance |
| SPY        | 2026-05-29 00:00:00 |   756.48      |         38.0833   | LONG     | Yahoo Finance |
| TGT        | 2026-05-29 00:00:00 |   127.07      |         71.5833   | LONG     | Yahoo Finance |
| TSLA       | 2026-05-29 00:00:00 |   435.79      |         50.6667   | LONG     | Yahoo Finance |
| TXN        | 2026-05-29 00:00:00 |   305.68      |         49.8333   | LONG     | Yahoo Finance |
| UNH        | 2026-05-29 00:00:00 |   380.31      |         46.8333   | LONG     | Yahoo Finance |
| UPS        | 2026-05-29 00:00:00 |   106.69      |         85.8333   | LONG     | Yahoo Finance |
| VTI        | 2026-05-29 00:00:00 |   372.54      |         53.0833   | LONG     | Yahoo Finance |
| XLK        | 2026-05-29 00:00:00 |   191.02      |         64.5833   | LONG     | Yahoo Finance |
| XLM-USD    | 2026-06-01 00:00:00 |     0.257942  |         65.5      | LONG     | Kraken API    |
| ADBE       | 2026-05-29 00:00:00 |   259.21      |         20.1667   | NEUTRAL  | Yahoo Finance |
| AGG        | 2026-05-29 00:00:00 |    99.06      |         25        | NEUTRAL  | Yahoo Finance |
| AMAT       | 2026-05-29 00:00:00 |   450.06      |         60.6667   | NEUTRAL  | Yahoo Finance |
| AMGN       | 2026-05-29 00:00:00 |   336.79      |         40.25     | NEUTRAL  | Yahoo Finance |
| AMZN       | 2026-05-29 00:00:00 |   270.64      |         28.3333   | NEUTRAL  | Yahoo Finance |
| ARKK       | 2026-05-29 00:00:00 |    81.95      |         44.8333   | NEUTRAL  | Yahoo Finance |
| ATOM-USD   | 2026-06-01 00:00:00 |     1.9615    |        -24.8333   | NEUTRAL  | Kraken API    |
| AVGO       | 2026-05-29 00:00:00 |   446.77      |         30.5      | NEUTRAL  | Yahoo Finance |
| BA         | 2026-05-29 00:00:00 |   231.15      |         10.6667   | NEUTRAL  | Yahoo Finance |
| BITO       | 2026-05-29 00:00:00 |    10.02      |        -65.8333   | NEUTRAL  | Yahoo Finance |
| BLK        | 2026-05-29 00:00:00 |  1046.88      |        -55.8333   | NEUTRAL  | Yahoo Finance |
| BND        | 2026-05-29 00:00:00 |    73.46      |          7        | NEUTRAL  | Yahoo Finance |
| C          | 2026-05-29 00:00:00 |   125.9       |         26.5      | NEUTRAL  | Yahoo Finance |
| CAT        | 2026-05-29 00:00:00 |   875.87      |          2.91667  | NEUTRAL  | Yahoo Finance |
| CMCSA      | 2026-05-29 00:00:00 |    24.87      |        -17.5      | NEUTRAL  | Yahoo Finance |
| COP        | 2026-05-29 00:00:00 |   113.98      |        -13.6667   | NEUTRAL  | Yahoo Finance |
| COST       | 2026-05-29 00:00:00 |   956.32      |        -45        | NEUTRAL  | Yahoo Finance |
| CRM        | 2026-05-29 00:00:00 |   191.1       |         24.1667   | NEUTRAL  | Yahoo Finance |
| CVX        | 2026-05-29 00:00:00 |   182.46      |         -5.58333  | NEUTRAL  | Yahoo Finance |
| DASH-USD   | 2026-06-01 00:00:00 |    40.626     |        -31.0833   | NEUTRAL  | Kraken API    |
| DBC        | 2026-05-29 00:00:00 |    29.48      |        -19.8333   | NEUTRAL  | Yahoo Finance |
| DE         | 2026-05-29 00:00:00 |   542.18      |        -11.5833   | NEUTRAL  | Yahoo Finance |
| DIA        | 2026-05-29 00:00:00 |   510.78      |         55        | NEUTRAL  | Yahoo Finance |
| DIS        | 2026-05-29 00:00:00 |   101.83      |        -54.5833   | NEUTRAL  | Yahoo Finance |
| DOT-USD    | 2026-06-01 00:00:00 |     1.1848    |        -44.5833   | NEUTRAL  | Kraken API    |
| EEM        | 2026-05-29 00:00:00 |    68.6       |         48.6667   | NEUTRAL  | Yahoo Finance |
| EFA        | 2026-05-29 00:00:00 |   104.8       |         56.1667   | NEUTRAL  | Yahoo Finance |
| EOG        | 2026-05-29 00:00:00 |   133.38      |         -4.91667  | NEUTRAL  | Yahoo Finance |
| ETC-USD    | 2026-06-01 00:00:00 |     8.157     |        -60.5833   | NEUTRAL  | Kraken API    |
| EWJ        | 2026-05-29 00:00:00 |    92.96      |         40.1667   | NEUTRAL  | Yahoo Finance |
| FIL-USD    | 2026-06-01 00:00:00 |     0.938     |        -28.1667   | NEUTRAL  | Kraken API    |
| FXI        | 2026-05-29 00:00:00 |    35.05      |        -63.8333   | NEUTRAL  | Yahoo Finance |
| GDX        | 2026-05-29 00:00:00 |    89.49      |        -13.25     | NEUTRAL  | Yahoo Finance |
| GDXJ       | 2026-05-29 00:00:00 |   119.29      |         -9.83333  | NEUTRAL  | Yahoo Finance |
| GE         | 2026-05-29 00:00:00 |   323.76      |         54        | NEUTRAL  | Yahoo Finance |
| GLD        | 2026-05-29 00:00:00 |   417.12      |        -27.5833   | NEUTRAL  | Yahoo Finance |
| GOOGL      | 2026-05-29 00:00:00 |   380.34      |         14.1667   | NEUTRAL  | Yahoo Finance |
| GRT-USD    | 2026-06-01 00:00:00 |     0.02593   |        -11.75     | NEUTRAL  | Kraken API    |
| GS         | 2026-05-29 00:00:00 |  1025.56      |         51        | NEUTRAL  | Yahoo Finance |
| HD         | 2026-05-29 00:00:00 |   317.14      |         -2.75     | NEUTRAL  | Yahoo Finance |
| IBIT       | 2026-05-29 00:00:00 |    41.63      |        -65.8333   | NEUTRAL  | Yahoo Finance |
| IEF        | 2026-05-29 00:00:00 |    94.65      |         -3.5      | NEUTRAL  | Yahoo Finance |
| IEMG       | 2026-05-29 00:00:00 |    83.47      |         52.1667   | NEUTRAL  | Yahoo Finance |
| INTU       | 2026-05-29 00:00:00 |   331.53      |        -70.5833   | NEUTRAL  | Yahoo Finance |
| IWM        | 2026-05-29 00:00:00 |   290.43      |         57.8333   | NEUTRAL  | Yahoo Finance |
| JNJ        | 2026-05-29 00:00:00 |   225.33      |          5.25     | NEUTRAL  | Yahoo Finance |
| JPM        | 2026-05-29 00:00:00 |   299.31      |        -17.3333   | NEUTRAL  | Yahoo Finance |
| LIN        | 2026-05-29 00:00:00 |   497.69      |         -0.916667 | NEUTRAL  | Yahoo Finance |
| LINK-USD   | 2026-06-01 00:00:00 |     9.12      |        -55.5833   | NEUTRAL  | Kraken API    |
| LRCX       | 2026-05-29 00:00:00 |   318.18      |         60.3333   | NEUTRAL  | Yahoo Finance |
| MCD        | 2026-05-29 00:00:00 |   279.2       |        -26.3333   | NEUTRAL  | Yahoo Finance |
| MPC        | 2026-05-29 00:00:00 |   248.77      |         29.5      | NEUTRAL  | Yahoo Finance |
| MS         | 2026-05-29 00:00:00 |   208         |         51        | NEUTRAL  | Yahoo Finance |
| MSFT       | 2026-05-29 00:00:00 |   450.24      |         58.25     | NEUTRAL  | Yahoo Finance |
| NEAR-USD   | 2026-06-01 00:00:00 |     2.2785    |         46.8333   | NEUTRAL  | Kraken API    |
| NEM        | 2026-05-29 00:00:00 |   109.81      |        -33.5      | NEUTRAL  | Yahoo Finance |
| NFLX       | 2026-05-29 00:00:00 |    86.02      |        -37        | NEUTRAL  | Yahoo Finance |
| NKE        | 2026-05-29 00:00:00 |    46.23      |         21.5833   | NEUTRAL  | Yahoo Finance |
| NVDA       | 2026-05-29 00:00:00 |   211.14      |          3.66667  | NEUTRAL  | Yahoo Finance |
| OXY        | 2026-05-29 00:00:00 |    56.63      |          0.833333 | NEUTRAL  | Yahoo Finance |
| PFE        | 2026-05-29 00:00:00 |    26.18      |         43.9167   | NEUTRAL  | Yahoo Finance |
| PG         | 2026-05-29 00:00:00 |   143.56      |        -11.75     | NEUTRAL  | Yahoo Finance |
| POL-USD    | 2026-06-01 00:00:00 |     0.09242   |         22.1667   | NEUTRAL  | Kraken API    |
| RTX        | 2026-05-29 00:00:00 |   179.66      |         25.75     | NEUTRAL  | Yahoo Finance |
| SBUX       | 2026-05-29 00:00:00 |    99.16      |         -5.41667  | NEUTRAL  | Yahoo Finance |
| SCHW       | 2026-05-29 00:00:00 |    87.35      |        -63.25     | NEUTRAL  | Yahoo Finance |
| SHY        | 2026-05-29 00:00:00 |    82.3       |         19.6667   | NEUTRAL  | Yahoo Finance |
| SKY-USD    | 2026-06-01 00:00:00 |     0.06849   |        -11.25     | NEUTRAL  | Kraken API    |
| SLB        | 2026-05-29 00:00:00 |    54.55      |         22.5833   | NEUTRAL  | Yahoo Finance |
| SLV        | 2026-05-29 00:00:00 |    68.33      |        -13.75     | NEUTRAL  | Yahoo Finance |
| SUSHI-USD  | 2026-06-01 00:00:00 |     0.2114    |        -13.5833   | NEUTRAL  | Kraken API    |
| T          | 2026-05-29 00:00:00 |    24.8       |        -29.75     | NEUTRAL  | Yahoo Finance |
| TIA-USD    | 2026-06-01 00:00:00 |     0.3969    |        -18.6667   | NEUTRAL  | Kraken API    |
| TLT        | 2026-05-29 00:00:00 |    85.76      |         -5.75     | NEUTRAL  | Yahoo Finance |
| TMO        | 2026-05-29 00:00:00 |   492.51      |         25.9167   | NEUTRAL  | Yahoo Finance |
| TMUS       | 2026-05-29 00:00:00 |   187.53      |        -57.4167   | NEUTRAL  | Yahoo Finance |
| TRX-USD    | 2026-06-01 00:00:00 |     0.351308  |         16.6667   | NEUTRAL  | Kraken API    |
| USO        | 2026-05-29 00:00:00 |   129.09      |        -21.8333   | NEUTRAL  | Yahoo Finance |
| VEA        | 2026-05-29 00:00:00 |    71.77      |         59.8333   | NEUTRAL  | Yahoo Finance |
| VNQ        | 2026-05-29 00:00:00 |    95.7       |          8.66667  | NEUTRAL  | Yahoo Finance |
| VWO        | 2026-05-29 00:00:00 |    59.88      |         12.6667   | NEUTRAL  | Yahoo Finance |
| VZ         | 2026-05-29 00:00:00 |    47.81      |         66.6667   | NEUTRAL  | Yahoo Finance |
| WFC        | 2026-05-29 00:00:00 |    77.54      |         -3.08333  | NEUTRAL  | Yahoo Finance |
| XBI        | 2026-05-29 00:00:00 |   136.69      |         62.8333   | NEUTRAL  | Yahoo Finance |
| XLB        | 2026-05-29 00:00:00 |    51.15      |         42.3333   | NEUTRAL  | Yahoo Finance |
| XLC        | 2026-05-29 00:00:00 |   115.69      |        -16.5      | NEUTRAL  | Yahoo Finance |
| XLE        | 2026-05-29 00:00:00 |    56.29      |        -13.1667   | NEUTRAL  | Yahoo Finance |
| XLF        | 2026-05-29 00:00:00 |    51.58      |         21.75     | NEUTRAL  | Yahoo Finance |
| XLI        | 2026-05-29 00:00:00 |   173.13      |         35.6667   | NEUTRAL  | Yahoo Finance |
| XLP        | 2026-05-29 00:00:00 |    82.91      |         -5.58333  | NEUTRAL  | Yahoo Finance |
| XLU        | 2026-05-29 00:00:00 |    44.42      |        -11.1667   | NEUTRAL  | Yahoo Finance |
| XLV        | 2026-05-29 00:00:00 |   149.47      |         57.0833   | NEUTRAL  | Yahoo Finance |
| XLY        | 2026-05-29 00:00:00 |   120.87      |         42.6667   | NEUTRAL  | Yahoo Finance |
| XOM        | 2026-05-29 00:00:00 |   145.26      |         -7.83333  | NEUTRAL  | Yahoo Finance |
| ZEC-USD    | 2026-06-01 00:00:00 |   579.88      |          5.75     | NEUTRAL  | Kraken API    |
| AAVE-USD   | 2026-06-01 00:00:00 |    82.17      |        -45.6667   | SHORT    | Kraken API    |
| ADA-USD    | 2026-06-01 00:00:00 |     0.235001  |        -47.6667   | SHORT    | Kraken API    |
| APT-USD    | 2026-06-01 00:00:00 |     0.9443    |        -30.3333   | SHORT    | Kraken API    |
| ARB-USD    | 2026-06-01 00:00:00 |     0.1023    |        -51.6667   | SHORT    | Kraken API    |
| AVAX-USD   | 2026-06-01 00:00:00 |     8.96      |        -42.3333   | SHORT    | Kraken API    |
| BCH-USD    | 2026-06-01 00:00:00 |   300.21      |        -65.1667   | SHORT    | Kraken API    |
| BONK-USD   | 2026-06-01 00:00:00 |     5.516e-06 |        -46.3333   | SHORT    | Kraken API    |
| BTC-USD    | 2026-06-01 00:00:00 | 73536.2       |        -44.3333   | SHORT    | Kraken API    |
| COMP-USD   | 2026-06-01 00:00:00 |    18.51      |        -43        | SHORT    | Kraken API    |
| CRV-USD    | 2026-06-01 00:00:00 |     0.2154    |        -44.3333   | SHORT    | Kraken API    |
| DOGE-USD   | 2026-06-01 00:00:00 |     0.10044   |        -42.3333   | SHORT    | Kraken API    |
| ETH-USD    | 2026-06-01 00:00:00 |  2004.64      |        -37.6667   | SHORT    | Kraken API    |
| LDO-USD    | 2026-06-01 00:00:00 |     0.326     |        -42.3333   | SHORT    | Kraken API    |
| LTC-USD    | 2026-06-01 00:00:00 |    51.93      |        -44.3333   | SHORT    | Kraken API    |
| OP-USD     | 2026-06-01 00:00:00 |     0.1186    |        -37.3333   | SHORT    | Kraken API    |
| PEP        | 2026-05-29 00:00:00 |   144.19      |        -46.5      | SHORT    | Yahoo Finance |
| PEPE-USD   | 2026-06-01 00:00:00 |     3.409e-06 |        -42.3333   | SHORT    | Kraken API    |
| SHIB-USD   | 2026-06-01 00:00:00 |     5.52e-06  |        -40.6667   | SHORT    | Kraken API    |
| SNX-USD    | 2026-06-01 00:00:00 |     0.2936    |        -42.6667   | SHORT    | Kraken API    |
| SOL-USD    | 2026-06-01 00:00:00 |    82.27      |        -42.3333   | SHORT    | Kraken API    |
| UNI-USD    | 2026-06-01 00:00:00 |     3.015     |        -42.3333   | SHORT    | Kraken API    |
| VIXY       | 2026-05-29 00:00:00 |    23.29      |        -48.0833   | SHORT    | Yahoo Finance |
| WIF-USD    | 2026-06-01 00:00:00 |     0.1921    |        -42.6667   | SHORT    | Kraken API    |
| WMT        | 2026-05-29 00:00:00 |   115.75      |        -46.0833   | SHORT    | Yahoo Finance |
| XRP-USD    | 2026-06-01 00:00:00 |     1.32802   |        -44.3333   | SHORT    | Kraken API    |
| YFI-USD    | 2026-06-01 00:00:00 |  2318         |        -40.6667   | SHORT    | Kraken API    |

## Edge Summary

- Symbols with trades: **160** of 160
- Beat buy-and-hold: **33.75%** of traded symbols
- Positive return: **33.75%** of traded symbols
- Median strategy return: **-9.07%** (benchmark **18.68%**)
- Median excess vs benchmark: **-31.01%**
- Median Sharpe: **-0.08**
- Median exposure: **44.70%**

> Edge is real only if both _beat buy-and-hold_ and _median excess_ are convincingly positive across many symbols. Treat a single high-return symbol as noise.

## Portfolio Backtest

Actual capital-allocation books (not per-symbol averages). Benchmarks: `equal_weight_buyhold` (whole tracked universe), `spy_buyhold` (100% SPY), and `sixty_forty` (60% SPY / 40% AGG). `high_conf_voltarget` inverse-vol-weights the HIGH-confidence book; `conviction_long_short` is market-neutral. Judge on **Sharpe** and **max_drawdown** out-of-sample, not raw return: a fully-invested long book wins on return in a bull market but carries all the risk.

| strategy              | scope         | ann_return   | ann_vol   |   sharpe | max_drawdown   | total_return   |   avg_gross_exposure |
|:----------------------|:--------------|:-------------|:----------|---------:|:---------------|:---------------|---------------------:|
| equal_weight_buyhold  | full          | -9.64%       | 33.83%    |    -0.28 | -57.60%        | -37.54%        |                 1    |
| equal_weight_buyhold  | out_of_sample | -10.78%      | 34.47%    |    -0.31 | -39.63%        | -16.34%        |                 1    |
| all_signals_ew        | full          | -7.38%       | 28.13%    |    -0.26 | -60.61%        | -29.32%        |                 1    |
| all_signals_ew        | out_of_sample | 1.59%        | 28.58%    |     0.06 | -32.68%        | -2.60%         |                 1    |
| high_conf_ew          | full          | 2.27%        | 32.28%    |     0.07 | -46.82%        | -8.42%         |                 0.89 |
| high_conf_ew          | out_of_sample | 28.80%       | 37.49%    |     0.77 | -20.90%        | 26.38%         |                 0.89 |
| high_conf_voltarget   | full          | 2.32%        | 29.89%    |     0.08 | -39.39%        | -6.14%         |                 0.89 |
| high_conf_voltarget   | out_of_sample | 20.57%       | 35.79%    |     0.57 | -17.06%        | 16.54%         |                 0.89 |
| conviction_long_short | full          | -10.75%      | 23.25%    |    -0.46 | -41.12%        | -33.71%        |                 0.97 |
| conviction_long_short | out_of_sample | -5.39%       | 26.91%    |    -0.2  | -20.75%        | -9.19%         |                 0.97 |
| spy_buyhold           | full          | 10.70%       | 13.23%    |     0.81 | -17.81%        | 34.93%         |                 0.78 |
| spy_buyhold           | out_of_sample | 1.61%        | 9.33%     |     0.17 | -14.83%        | 1.26%          |                 0.78 |
| sixty_forty           | full          | 6.17%        | 8.38%     |     0.74 | -10.80%        | 19.41%         |                 0.78 |
| sixty_forty           | out_of_sample | -0.26%       | 6.03%     |    -0.04 | -10.09%        | -0.47%         |                 0.78 |

## Walk-Forward Robustness

Each book measured across contiguous time folds (each a different regime). A book has durable edge only if `mean_sharpe` is positive, `min_sharpe` isn't deeply negative, and `pct_positive_folds` is high — a single great fold doesn't count. `fold_sharpes` lists each fold oldest-to-newest.

| strategy              |   n_folds |   mean_sharpe |   median_sharpe |   min_sharpe | pct_positive_folds   | mean_return   | fold_sharpes                 |
|:----------------------|----------:|--------------:|----------------:|-------------:|:---------------------|:--------------|:-----------------------------|
| equal_weight_buyhold  |         5 |         -0.06 |            0.07 |        -1.61 | 60.00%               | -7.74%        | 1.83;-1.61;0.23;-0.82;0.07   |
| all_signals_ew        |         5 |          0.08 |            0.91 |        -2.15 | 60.00%               | -3.78%        | 0.91;1.13;-0.93;-2.15;1.41   |
| high_conf_ew          |         5 |          0.39 |           -0.16 |        -0.68 | 40.00%               | -0.11%        | 1.76;-0.16;-0.68;-0.57;1.60  |
| high_conf_voltarget   |         5 |          0.47 |           -0.28 |        -0.46 | 40.00%               | -0.37%        | 2.46;-0.28;-0.36;-0.46;1.00  |
| conviction_long_short |         5 |         -0.45 |           -0.43 |        -0.92 | 20.00%               | -7.71%        | -0.43;-0.43;-0.51;-0.92;0.06 |
| spy_buyhold           |         5 |          0.87 |            0.73 |        -0.26 | 80.00%               | 6.40%         | 2.21;1.48;0.19;-0.26;0.73    |
| sixty_forty           |         5 |          0.76 |            0.41 |        -0.13 | 80.00%               | 3.70%         | 2.15;1.21;0.16;-0.13;0.41    |

## Strategy Comparison

Each decision rule backtested over the same data. `out_of_sample` is the most recent ~35% of each symbol's history (unseen tail). A rule has real edge only if `median_excess` and `beat_benchmark_pct` stay positive out-of-sample, not just full-sample.

| strategy        | scope         |   symbols | beat_benchmark_pct   | positive_pct   | median_return   | median_benchmark   | median_excess   |   median_sharpe |   total_trades |
|:----------------|:--------------|----------:|:---------------------|:---------------|:----------------|:-------------------|:----------------|----------------:|---------------:|
| trend           | full          |       160 | 33.75%               | 33.75%         | -9.07%          | 18.68%             | -31.01%         |           -0.08 |          11337 |
| trend           | out_of_sample |       160 | 36.25%               | 52.50%         | 1.26%           | 8.32%              | -7.70%          |            0.19 |           3954 |
| mean_reversion  | full          |       159 | 38.36%               | 47.80%         | -0.20%          | 18.43%             | -18.02%         |           -0.04 |           1262 |
| mean_reversion  | out_of_sample |       127 | 42.52%               | 56.69%         | 0.32%           | 4.26%              | -6.52%          |            0.64 |            472 |
| regime_adaptive | full          |       160 | 34.38%               | 33.75%         | -9.18%          | 18.68%             | -31.07%         |           -0.09 |          11613 |
| regime_adaptive | out_of_sample |       160 | 36.25%               | 54.37%         | 1.31%           | 8.32%              | -7.79%          |            0.22 |           4057 |

## Signal Calibration

Realized forward return in the signal's direction, grouped by confidence. HIGH should outrank LOW for the confidence score to be meaningful.

| confidence_level   |   horizon |     n | mean_return   | median_return   | win_rate   |
|:-------------------|----------:|------:|:--------------|:----------------|:-----------|
| HIGH               |         5 |  8088 | 0.15%         | 0.13%           | 52.30%     |
| MEDIUM             |         5 | 29169 | 0.01%         | 0.09%           | 51.01%     |
| LOW                |         5 |  3275 | -0.64%        | -0.49%          | 45.01%     |
| ALL                |         5 | 40532 | -0.01%        | 0.06%           | 50.78%     |
| HIGH               |        10 |  8047 | 0.50%         | 0.19%           | 52.29%     |
| MEDIUM             |        10 | 28840 | 0.16%         | 0.15%           | 51.25%     |
| LOW                |        10 |  3249 | -0.94%        | -0.77%          | 45.03%     |
| ALL                |        10 | 40136 | 0.13%         | 0.11%           | 50.95%     |
| HIGH               |        20 |  7916 | 0.86%         | 0.46%           | 53.66%     |
| MEDIUM             |        20 | 28210 | 0.74%         | 0.61%           | 53.54%     |
| LOW                |        20 |  3195 | -0.67%        | -0.51%          | 46.98%     |
| ALL                |        20 | 39321 | 0.65%         | 0.51%           | 53.03%     |

## Backtest Summary

### Data Quality / Signal Availability

- **ok**: 160 symbols

| symbol     |   trades | return   | benchmark_return   | mdd     |   sharpe | exposure   | skipped_reason   |
|:-----------|---------:|:---------|:-------------------|:--------|---------:|:-----------|:-----------------|
| AAPL       |       67 | 13.67%   | 72.24%             | -20.65% |     0.37 | 48.75%     | ok               |
| AAVE-USD   |       82 | -69.87%  | -74.55%            | -71.25% |    -1.03 | 34.67%     | ok               |
| ABBV       |       64 | -16.71%  | 34.28%             | -30.55% |    -0.34 | 49.25%     | ok               |
| ADA-USD    |       86 | -87.68%  | -73.14%            | -91.71% |    -0.92 | 45.02%     | ok               |
| ADBE       |       66 | -24.79%  | -54.09%            | -39.11% |    -0.27 | 57.07%     | ok               |
| AGG        |       73 | -7.43%   | 0.88%              | -10.16% |    -1.22 | 31.61%     | ok               |
| ALGO-USD   |       84 | -46.79%  | -62.14%            | -61.76% |    -0.49 | 38.12%     | ok               |
| AMAT       |       67 | -19.38%  | 202.05%            | -57.80% |    -0.1  | 53.58%     | ok               |
| AMD        |       56 | 55.11%   | 272.42%            | -47.17% |     0.65 | 38.94%     | ok               |
| AMGN       |       71 | -17.45%  | 11.15%             | -34.14% |    -0.32 | 49.92%     | ok               |
| AMZN       |       74 | -33.84%  | 86.34%             | -42.48% |    -0.99 | 38.27%     | ok               |
| APT-USD    |       80 | -55.52%  | -89.16%            | -69.98% |    -0.49 | 41.76%     | ok               |
| ARB-USD    |       74 | -11.10%  | -86.54%            | -61.76% |     0.13 | 38.51%     | ok               |
| ARKK       |       81 | -32.67%  | 67.59%             | -34.13% |    -0.57 | 38.94%     | ok               |
| ATOM-USD   |       92 | -67.37%  | -69.61%            | -69.12% |    -1.17 | 43.30%     | ok               |
| AVAX-USD   |       72 | -42.15%  | -75.45%            | -53.54% |    -0.43 | 36.40%     | ok               |
| AVGO       |       60 | 48.21%   | 325.79%            | -35.76% |     0.63 | 47.42%     | ok               |
| BA         |       71 | 4.66%    | -7.17%             | -30.56% |     0.21 | 51.58%     | ok               |
| BAC        |       78 | -20.55%  | 49.87%             | -27.64% |    -0.54 | 45.92%     | ok               |
| BCH-USD    |       80 | -44.02%  | -31.80%            | -58.22% |    -0.51 | 45.21%     | ok               |
| BITO       |       76 | 3.90%    | -53.20%            | -42.82% |     0.22 | 38.77%     | ok               |
| BLK        |       75 | -1.96%   | 33.73%             | -20.81% |     0.01 | 42.43%     | ok               |
| BND        |       67 | -7.84%   | 0.98%              | -9.89%  |    -1.25 | 32.61%     | ok               |
| BONK-USD   |       72 | 50.09%   | -82.74%            | -45.22% |     0.62 | 39.85%     | ok               |
| BTC-USD    |       74 | -15.71%  | -21.89%            | -31.57% |    -0.14 | 50.19%     | ok               |
| C          |       83 | -29.99%  | 131.73%            | -36.36% |    -0.61 | 51.58%     | ok               |
| CAT        |       74 | 30.32%   | 203.14%            | -21.02% |     0.57 | 58.24%     | ok               |
| CL         |       60 | 22.58%   | 12.69%             | -14.32% |     0.74 | 49.08%     | ok               |
| CMCSA      |       80 | -36.01%  | -38.35%            | -39.80% |    -0.9  | 44.26%     | ok               |
| COMP-USD   |       91 | -44.84%  | -76.31%            | -63.55% |    -0.35 | 44.25%     | ok               |
| COP        |       81 | -27.18%  | -2.19%             | -43.99% |    -0.52 | 42.10%     | ok               |
| COST       |       64 | 10.01%   | 45.78%             | -29.73% |     0.35 | 48.09%     | ok               |
| CRM        |       68 | -31.42%  | -23.90%            | -40.29% |    -0.6  | 44.76%     | ok               |
| CRV-USD    |       60 | 8.54%    | -76.07%            | -39.89% |     0.31 | 31.23%     | ok               |
| CSCO       |       61 | 23.67%   | 140.41%            | -21.79% |     0.53 | 48.42%     | ok               |
| CVX        |       75 | -19.18%  | 21.32%             | -29.70% |    -0.51 | 42.10%     | ok               |
| DASH-USD   |       65 | -44.95%  | 3.58%              | -64.43% |    -0.06 | 30.46%     | ok               |
| DBC        |       62 | -12.97%  | 33.21%             | -25.70% |    -0.44 | 33.78%     | ok               |
| DE         |       74 | -11.10%  | 36.93%             | -25.98% |    -0.17 | 45.59%     | ok               |
| DIA        |       58 | -1.59%   | 36.34%             | -12.94% |    -0.05 | 46.42%     | ok               |
| DIS        |       59 | 2.59%    | 12.02%             | -22.67% |     0.16 | 47.42%     | ok               |
| DOGE-USD   |       77 | -27.16%  | -67.73%            | -60.95% |    -0.03 | 48.28%     | ok               |
| DOT-USD    |       88 | -46.93%  | -82.81%            | -57.66% |    -0.34 | 46.74%     | ok               |
| DXY-INDEX  |       42 | -4.07%   | -5.14%             | -6.05%  |    -0.67 | 26.68%     | ok               |
| EEM        |       64 | -9.40%   | 73.94%             | -25.67% |    -0.25 | 43.43%     | ok               |
| EFA        |       60 | -9.30%   | 41.30%             | -13.53% |    -0.34 | 43.76%     | ok               |
| EOG        |       83 | -29.95%  | 10.80%             | -48.13% |    -0.69 | 47.75%     | ok               |
| ETC-USD    |       70 | -46.65%  | -68.53%            | -54.25% |    -0.8  | 30.27%     | ok               |
| ETH-USD    |       62 | 113.02%  | -39.76%            | -30.11% |     1.08 | 43.10%     | ok               |
| EWJ        |       64 | -18.27%  | 46.32%             | -30.73% |    -0.59 | 41.43%     | ok               |
| FCX        |       73 | -35.07%  | 58.68%             | -48.56% |    -0.49 | 45.09%     | ok               |
| FET-USD    |       77 | -3.25%   | -79.82%            | -48.39% |     0.25 | 39.66%     | ok               |
| FIL-USD    |       70 | -26.60%  | -81.01%            | -46.68% |    -0.16 | 32.76%     | ok               |
| FXI        |       44 | -10.87%  | 50.88%             | -23.91% |    -0.2  | 26.46%     | ok               |
| GDX        |       62 | 3.89%    | 200.60%            | -34.99% |     0.19 | 48.92%     | ok               |
| GDXJ       |       66 | -22.23%  | 231.55%            | -44.93% |    -0.22 | 47.25%     | ok               |
| GE         |       74 | 8.49%    | 221.22%            | -27.82% |     0.26 | 51.91%     | ok               |
| GLD        |       50 | 17.86%   | 120.29%            | -16.63% |     0.51 | 43.93%     | ok               |
| GOOGL      |       65 | 81.90%   | 180.22%            | -20.41% |     1.19 | 55.57%     | ok               |
| GRT-USD    |       91 | -28.32%  | -87.38%            | -57.25% |    -0.13 | 41.38%     | ok               |
| GS         |       76 | -0.53%   | 165.39%            | -22.13% |     0.09 | 50.92%     | ok               |
| HD         |       69 | -0.67%   | -7.52%             | -17.69% |     0.06 | 45.59%     | ok               |
| HON        |       95 | -19.02%  | 24.00%             | -28.64% |    -0.5  | 51.58%     | ok               |
| HYG        |       83 | -8.84%   | 4.73%              | -9.57%  |    -1.02 | 34.78%     | ok               |
| IBIT       |       30 | 35.78%   | 9.52%              | -18.95% |     0.79 | 29.40%     | ok               |
| IBM        |       74 | 45.79%   | 87.11%             | -25.31% |     0.9  | 50.42%     | ok               |
| ICP-USD    |       81 | 7.21%    | -73.26%            | -50.29% |     0.32 | 36.78%     | ok               |
| IEF        |       80 | -11.63%  | -0.71%             | -12.27% |    -1.63 | 33.28%     | ok               |
| IEMG       |       58 | -5.52%   | 68.02%             | -26.84% |    -0.12 | 43.59%     | ok               |
| INJ-USD    |       77 | -56.58%  | -68.99%            | -80.97% |    -0.6  | 38.31%     | ok               |
| INTC       |       70 | 65.46%   | 144.57%            | -60.60% |     0.67 | 49.92%     | ok               |
| INTU       |       67 | -14.99%  | -43.71%            | -43.77% |    -0.14 | 42.93%     | ok               |
| ITA        |       70 | 4.96%    | 90.12%             | -23.75% |     0.22 | 45.42%     | ok               |
| IWM        |       50 | 9.94%    | 50.29%             | -12.83% |     0.4  | 36.77%     | ok               |
| JNJ        |       76 | 2.53%    | 39.84%             | -17.51% |     0.15 | 51.58%     | ok               |
| JPM        |       75 | -23.90%  | 73.74%             | -31.97% |    -0.63 | 52.91%     | ok               |
| KO         |       49 | 23.88%   | 32.41%             | -8.07%  |     0.9  | 37.10%     | ok               |
| LDO-USD    |       80 | -22.36%  | -82.81%            | -60.93% |     0.05 | 36.59%     | ok               |
| LIN        |       72 | -3.07%   | 21.65%             | -21.53% |    -0.05 | 39.27%     | ok               |
| LINK-USD   |       70 | -21.53%  | -57.63%            | -55.61% |    -0    | 40.04%     | ok               |
| LLY        |       69 | -12.48%  | 78.64%             | -53.34% |    -0.08 | 51.08%     | ok               |
| LRCX       |       82 | -16.50%  | 334.43%            | -63.56% |    -0.07 | 46.26%     | ok               |
| LTC-USD    |       68 | -46.55%  | -48.29%            | -55.90% |    -0.55 | 46.74%     | ok               |
| MCD        |       75 | -0.66%   | -3.39%             | -19.14% |     0.03 | 39.27%     | ok               |
| META       |       72 | 4.38%    | 79.72%             | -33.10% |     0.2  | 52.25%     | ok               |
| MPC        |       71 | -13.72%  | 63.13%             | -44.76% |    -0.13 | 49.92%     | ok               |
| MRK        |       67 | -17.88%  | 1.28%              | -32.14% |    -0.36 | 47.09%     | ok               |
| MS         |       81 | -16.73%  | 123.08%            | -26.72% |    -0.36 | 47.75%     | ok               |
| MSFT       |       74 | -25.88%  | 22.43%             | -30.56% |    -0.65 | 47.25%     | ok               |
| MU         |       55 | 207.77%  | 1063.57%           | -68.76% |     1.24 | 58.57%     | ok               |
| NEAR-USD   |       91 | -4.59%   | -55.40%            | -60.07% |     0.22 | 43.10%     | ok               |
| NEM        |       70 | -19.45%  | 172.21%            | -38.49% |    -0.12 | 55.74%     | ok               |
| NFLX       |       64 | 23.70%   | 81.45%             | -21.09% |     0.56 | 54.91%     | ok               |
| NKE        |       93 | -37.98%  | -54.71%            | -55.35% |    -0.53 | 45.76%     | ok               |
| NOW        |       78 | 23.56%   | -8.03%             | -31.32% |     0.44 | 45.76%     | ok               |
| NVDA       |       72 | -20.14%  | 145.61%            | -45.02% |    -0.08 | 61.14%     | ok               |
| OP-USD     |       78 | -4.02%   | -93.55%            | -70.11% |     0.2  | 35.06%     | ok               |
| ORCL       |       72 | 71.80%   | 119.78%            | -29.47% |     0.76 | 52.08%     | ok               |
| OXY        |       71 | 0.50%    | -3.92%             | -31.01% |     0.13 | 44.26%     | ok               |
| PEP        |       83 | -11.60%  | -14.65%            | -21.35% |    -0.29 | 48.42%     | ok               |
| PEPE-USD   |       79 | -11.05%  | -80.89%            | -57.66% |     0.17 | 42.15%     | ok               |
| PFE        |       77 | -38.05%  | -11.16%            | -42.29% |    -1.18 | 37.27%     | ok               |
| PG         |       61 | -9.88%   | -2.62%             | -20.33% |    -0.36 | 40.43%     | ok               |
| PM         |       83 | 3.66%    | 86.13%             | -33.68% |     0.17 | 56.91%     | ok               |
| POL-USD    |       80 | 47.17%   | -80.72%            | -46.45% |     0.65 | 47.32%     | ok               |
| QCOM       |       81 | -1.14%   | 83.59%             | -57.69% |     0.15 | 48.42%     | ok               |
| QQQ        |       60 | 24.16%   | 86.09%             | -12.88% |     0.68 | 46.09%     | ok               |
| RENDER-USD |       94 | -7.47%   | -49.83%            | -45.00% |     0.22 | 44.64%     | ok               |
| RTX        |       58 | 19.25%   | 110.42%            | -16.99% |     0.52 | 52.58%     | ok               |
| SBUX       |       65 | -23.57%  | 6.64%              | -31.15% |    -0.48 | 40.77%     | ok               |
| SCHW       |       76 | -22.57%  | 29.93%             | -30.41% |    -0.53 | 45.76%     | ok               |
| SHIB-USD   |       78 | -40.41%  | -74.52%            | -48.95% |    -0.35 | 50.38%     | ok               |
| SHY        |       50 | -1.95%   | 0.50%              | -2.85%  |    -0.66 | 37.27%     | ok               |
| SKY-USD    |       66 | -29.93%  | 18.43%             | -43.98% |    -0.42 | 39.61%     | ok               |
| SLB        |       77 | -29.41%  | 5.19%              | -54.23% |    -0.51 | 51.91%     | ok               |
| SLV        |       58 | 36.93%   | 222.16%            | -42.66% |     0.58 | 40.60%     | ok               |
| SMH        |       50 | 86.91%   | 260.63%            | -33.99% |     1.13 | 51.75%     | ok               |
| SNX-USD    |       67 | 9.85%    | -85.78%            | -32.91% |     0.34 | 38.70%     | ok               |
| SOL-USD    |       72 | -51.34%  | -55.24%            | -56.90% |    -0.39 | 58.62%     | ok               |
| SOXX       |       57 | 75.74%   | 215.08%            | -40.34% |     0.98 | 50.92%     | ok               |
| SPY        |       60 | 10.00%   | 61.67%             | -16.47% |     0.4  | 50.75%     | ok               |
| SUSHI-USD  |       91 | -77.13%  | -84.92%            | -77.97% |    -1.16 | 35.25%     | ok               |
| T          |       64 | 14.38%   | 41.96%             | -17.01% |     0.42 | 49.42%     | ok               |
| TGT        |       58 | -9.55%   | -9.72%             | -40.57% |    -0.11 | 39.27%     | ok               |
| TIA-USD    |       76 | -0.51%   | -91.62%            | -51.15% |     0.24 | 33.33%     | ok               |
| TLT        |       70 | -22.73%  | -10.94%            | -24.69% |    -1.65 | 33.44%     | ok               |
| TMO        |       59 | 25.18%   | -7.29%             | -16.83% |     0.58 | 50.25%     | ok               |
| TMUS       |       68 | 19.70%   | 14.79%             | -24.50% |     0.49 | 49.25%     | ok               |
| TRX-USD    |       70 | -2.64%   | 35.80%             | -22.90% |     0.03 | 49.23%     | ok               |
| TSLA       |       68 | 13.21%   | 83.50%             | -57.89% |     0.34 | 43.93%     | ok               |
| TXN        |       77 | -5.90%   | 85.15%             | -46.98% |     0.06 | 52.91%     | ok               |
| UNH        |       78 | 15.34%   | -29.23%            | -32.80% |     0.35 | 52.25%     | ok               |
| UNI-USD    |       92 | -73.76%  | -77.35%            | -81.03% |    -0.9  | 40.04%     | ok               |
| UPS        |       66 | -36.35%  | -32.78%            | -40.62% |    -0.75 | 37.77%     | ok               |
| USO        |       68 | 2.80%    | 87.01%             | -43.35% |     0.17 | 34.44%     | ok               |
| VEA        |       60 | -2.87%   | 52.28%             | -19.49% |    -0.07 | 43.43%     | ok               |
| VIXY       |       90 | -77.40%  | -62.44%            | -87.63% |    -0.92 | 30.62%     | ok               |
| VNQ        |       81 | -18.88%  | 10.50%             | -24.92% |    -0.79 | 38.27%     | ok               |
| VTI        |       70 | 0.58%    | 59.81%             | -18.77% |     0.08 | 52.08%     | ok               |
| VWO        |       76 | -13.41%  | 47.89%             | -25.20% |    -0.47 | 44.09%     | ok               |
| VZ         |       83 | -21.84%  | 18.93%             | -31.88% |    -0.65 | 40.10%     | ok               |
| WFC        |       84 | -23.33%  | 55.33%             | -30.22% |    -0.45 | 47.42%     | ok               |
| WIF-USD    |       72 | -40.75%  | -89.43%            | -50.40% |    -0.19 | 30.65%     | ok               |
| WMT        |       53 | 38.75%   | 121.59%            | -21.31% |     0.99 | 53.24%     | ok               |
| XBI        |       64 | -3.68%   | 53.07%             | -20.48% |    -0    | 40.43%     | ok               |
| XLB        |       66 | -10.52%  | 21.29%             | -24.41% |    -0.34 | 36.77%     | ok               |
| XLC        |       63 | 21.96%   | 60.59%             | -12.33% |     0.71 | 57.24%     | ok               |
| XLE        |       81 | -11.84%  | 32.95%             | -37.64% |    -0.23 | 47.09%     | ok               |
| XLF        |       76 | -11.55%  | 36.64%             | -23.61% |    -0.38 | 49.92%     | ok               |
| XLI        |       66 | 5.61%    | 55.37%             | -11.38% |     0.27 | 48.09%     | ok               |
| XLK        |       42 | 77.76%   | 107.50%            | -14.75% |     1.43 | 48.59%     | ok               |
| XLM-USD    |       69 | 38.97%   | -26.13%            | -40.13% |     0.57 | 47.13%     | ok               |
| XLP        |       72 | 8.49%    | 15.14%             | -8.96%  |     0.5  | 44.26%     | ok               |
| XLU        |       67 | -4.20%   | 37.67%             | -13.66% |    -0.15 | 38.27%     | ok               |
| XLV        |       66 | -8.65%   | 7.44%              | -14.71% |    -0.4  | 37.77%     | ok               |
| XLY        |       78 | -1.30%   | 40.04%             | -14.01% |     0.03 | 44.76%     | ok               |
| XOM        |       61 | -0.77%   | 41.54%             | -20.29% |     0.05 | 36.77%     | ok               |
| XRP-USD    |       64 | -45.45%  | -38.03%            | -54.34% |    -0.57 | 34.87%     | ok               |
| YFI-USD    |       85 | -60.30%  | -72.77%            | -67.78% |    -1.06 | 38.51%     | ok               |
| ZEC-USD    |       67 | 46.51%   | 836.35%            | -46.93% |     0.57 | 36.40%     | ok               |

## AAPL Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 22.94%   | 72.24%             | -21.71% |     0.52 |       69 | 53.74%     | ok               |
|          25 | 19.69%   | 72.24%             | -20.03% |     0.47 |       67 | 51.25%     | ok               |
|          15 | 18.80%   | 72.24%             | -23.86% |     0.44 |       75 | 61.23%     | ok               |
|          30 | 13.67%   | 72.24%             | -20.65% |     0.37 |       67 | 48.75%     | ok               |
|          35 | 11.05%   | 72.24%             | -22.04% |     0.32 |       63 | 45.76%     | ok               |

## AAVE-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -14.22%  | -74.55%            | -43.61% |     0.03 |       38 | 27.20%     | ok               |
|          45 | -14.61%  | -74.55%            | -46.87% |     0.01 |       36 | 24.33%     | ok               |
|          35 | -35.50%  | -74.55%            | -51.96% |    -0.29 |       52 | 29.89%     | ok               |
|          50 | -32.67%  | -74.55%            | -47.78% |    -0.35 |       36 | 19.16%     | ok               |
|          15 | -66.75%  | -74.55%            | -68.63% |    -0.69 |       84 | 48.47%     | ok               |

## ABBV Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -5.06%   | 34.28%             | -27.91% |    -0.05 |       48 | 39.27%     | ok               |
|          40 | -12.20%  | 34.28%             | -26.61% |    -0.24 |       62 | 43.76%     | ok               |
|          35 | -14.49%  | 34.28%             | -27.83% |    -0.3  |       66 | 46.42%     | ok               |
|          45 | -14.93%  | 34.28%             | -29.59% |    -0.32 |       52 | 41.10%     | ok               |
|          30 | -16.71%  | 34.28%             | -30.55% |    -0.34 |       64 | 49.25%     | ok               |

## ADA-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -88.09%  | -73.14%            | -91.83% |    -0.78 |       82 | 61.11%     | ok               |
|          20 | -88.49%  | -73.14%            | -92.33% |    -0.83 |       88 | 56.13%     | ok               |
|          50 | -83.55%  | -73.14%            | -88.20% |    -0.83 |       55 | 26.82%     | ok               |
|          45 | -86.10%  | -73.14%            | -89.92% |    -0.91 |       60 | 30.27%     | ok               |
|          30 | -87.68%  | -73.14%            | -91.71% |    -0.92 |       86 | 45.02%     | ok               |

## ADBE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 9.36%    | -54.09%            | -21.34% |     0.28 |       74 | 49.25%     | ok               |
|          40 | -4.81%   | -54.09%            | -20.88% |     0.03 |       72 | 42.26%     | ok               |
|          25 | -10.65%  | -54.09%            | -33.75% |    -0.01 |       50 | 61.23%     | ok               |
|          15 | -19.55%  | -54.09%            | -33.77% |    -0.15 |       59 | 65.72%     | ok               |
|          20 | -21.75%  | -54.09%            | -36.77% |    -0.19 |       50 | 63.39%     | ok               |

## AGG Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -8.30%   | 0.88%              | -10.95% |    -1.21 |       77 | 37.27%     | ok               |
|          30 | -7.43%   | 0.88%              | -10.16% |    -1.22 |       73 | 31.61%     | ok               |
|          45 | -6.34%   | 0.88%              | -7.89%  |    -1.25 |       54 | 20.80%     | ok               |
|          25 | -8.59%   | 0.88%              | -11.59% |    -1.31 |       75 | 35.44%     | ok               |
|          15 | -9.41%   | 0.88%              | -12.40% |    -1.34 |       81 | 40.77%     | ok               |

## ALGO-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -46.79%  | -62.14%            | -61.76% |    -0.49 |       84 | 38.12%     | ok               |
|          15 | -57.35%  | -62.14%            | -70.86% |    -0.57 |       80 | 49.81%     | ok               |
|          25 | -57.46%  | -62.14%            | -75.14% |    -0.62 |       86 | 45.40%     | ok               |
|          35 | -50.40%  | -62.14%            | -54.80% |    -0.68 |       62 | 31.03%     | ok               |
|          20 | -61.86%  | -62.14%            | -73.99% |    -0.7  |       84 | 47.70%     | ok               |

## AMAT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -5.33%   | 202.05%            | -54.69% |     0.12 |       66 | 62.40%     | ok               |
|          30 | -19.38%  | 202.05%            | -57.80% |    -0.1  |       67 | 53.58%     | ok               |
|          20 | -25.27%  | 202.05%            | -60.72% |    -0.17 |       70 | 58.74%     | ok               |
|          35 | -25.12%  | 202.05%            | -55.89% |    -0.21 |       69 | 51.41%     | ok               |
|          25 | -28.77%  | 202.05%            | -60.95% |    -0.25 |       69 | 56.41%     | ok               |

## AMD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 55.11%   | 272.42%            | -47.17% |     0.65 |       56 | 38.94%     | ok               |
|          50 | 44.97%   | 272.42%            | -48.79% |     0.59 |       60 | 33.44%     | ok               |
|          35 | 35.34%   | 272.42%            | -54.57% |     0.51 |       62 | 40.93%     | ok               |
|          45 | 23.92%   | 272.42%            | -56.22% |     0.43 |       64 | 36.27%     | ok               |
|          30 | 17.49%   | 272.42%            | -59.88% |     0.38 |       63 | 43.43%     | ok               |

## AMGN Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -11.73%  | 11.15%             | -26.64% |    -0.16 |       73 | 55.91%     | ok               |
|          35 | -13.41%  | 11.15%             | -31.23% |    -0.22 |       67 | 46.09%     | ok               |
|          15 | -15.43%  | 11.15%             | -27.92% |    -0.23 |       72 | 61.73%     | ok               |
|          30 | -17.45%  | 11.15%             | -34.14% |    -0.32 |       71 | 49.92%     | ok               |
|          25 | -20.81%  | 11.15%             | -33.41% |    -0.4  |       67 | 52.25%     | ok               |

## AMZN Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -17.83%  | 86.34%             | -28.70% |    -0.52 |       50 | 29.78%     | ok               |
|          50 | -25.03%  | 86.34%             | -35.48% |    -0.88 |       48 | 24.13%     | ok               |
|          45 | -25.89%  | 86.34%             | -35.47% |    -0.89 |       50 | 26.96%     | ok               |
|          35 | -29.70%  | 86.34%             | -38.29% |    -0.91 |       62 | 32.95%     | ok               |
|          30 | -33.84%  | 86.34%             | -42.48% |    -0.99 |       74 | 38.27%     | ok               |

## APT-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 28.30%   | -89.16%            | -46.73% |     0.52 |       46 | 18.77%     | ok               |
|          45 | -14.07%  | -89.16%            | -64.17% |     0.03 |       64 | 25.10%     | ok               |
|          40 | -33.41%  | -89.16%            | -63.33% |    -0.2  |       70 | 30.84%     | ok               |
|          35 | -39.04%  | -89.16%            | -64.48% |    -0.25 |       74 | 36.21%     | ok               |
|          20 | -49.29%  | -89.16%            | -70.51% |    -0.32 |       77 | 50.38%     | ok               |

## ARB-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 37.06%   | -86.54%            | -52.62% |     0.55 |       89 | 55.36%     | ok               |
|          40 | 27.70%   | -86.54%            | -45.37% |     0.48 |       52 | 28.93%     | ok               |
|          20 | 14.58%   | -86.54%            | -59.44% |     0.4  |       79 | 49.81%     | ok               |
|          50 | 14.45%   | -86.54%            | -44.38% |     0.36 |       40 | 16.67%     | ok               |
|          35 | 12.53%   | -86.54%            | -54.93% |     0.35 |       66 | 32.95%     | ok               |

## ARKK Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -29.68%  | 67.59%             | -39.54% |    -0.39 |       96 | 51.41%     | ok               |
|          20 | -31.80%  | 67.59%             | -35.95% |    -0.47 |       89 | 45.92%     | ok               |
|          30 | -32.67%  | 67.59%             | -34.13% |    -0.57 |       81 | 38.94%     | ok               |
|          35 | -33.82%  | 67.59%             | -35.25% |    -0.63 |       80 | 36.61%     | ok               |
|          40 | -34.16%  | 67.59%             | -35.67% |    -0.68 |       70 | 31.61%     | ok               |

## ATOM-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -69.03%  | -69.61%            | -74.68% |    -1.04 |       96 | 60.15%     | ok               |
|          25 | -66.36%  | -69.61%            | -68.50% |    -1.06 |       99 | 49.62%     | ok               |
|          30 | -67.37%  | -69.61%            | -69.12% |    -1.17 |       92 | 43.30%     | ok               |
|          35 | -64.71%  | -69.61%            | -65.16% |    -1.19 |       80 | 38.70%     | ok               |
|          20 | -72.26%  | -69.61%            | -74.33% |    -1.21 |      105 | 54.21%     | ok               |

## AVAX-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -0.47%   | -75.45%            | -29.53% |     0.16 |       32 | 18.58%     | ok               |
|          45 | -3.51%   | -75.45%            | -32.82% |     0.12 |       34 | 21.46%     | ok               |
|          35 | -13.17%  | -75.45%            | -36.01% |     0.02 |       58 | 29.12%     | ok               |
|          40 | -11.97%  | -75.45%            | -32.65% |    -0    |       40 | 23.56%     | ok               |
|          15 | -23.49%  | -75.45%            | -50.68% |    -0.01 |       65 | 51.15%     | ok               |

## AVGO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 48.21%   | 325.79%            | -35.76% |     0.63 |       60 | 47.42%     | ok               |
|          25 | 42.94%   | 325.79%            | -38.01% |     0.59 |       64 | 48.09%     | ok               |
|          35 | 35.61%   | 325.79%            | -36.19% |     0.53 |       72 | 44.59%     | ok               |
|          40 | 29.71%   | 325.79%            | -40.70% |     0.48 |       62 | 40.93%     | ok               |
|          20 | 29.43%   | 325.79%            | -40.10% |     0.47 |       72 | 50.92%     | ok               |

## BA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 23.99%   | -7.17%             | -23.77% |     0.49 |       76 | 46.76%     | ok               |
|          50 | 16.03%   | -7.17%             | -16.71% |     0.46 |       46 | 31.61%     | ok               |
|          25 | 7.78%    | -7.17%             | -32.48% |     0.25 |       74 | 55.07%     | ok               |
|          30 | 4.66%    | -7.17%             | -30.56% |     0.21 |       71 | 51.58%     | ok               |
|          40 | 2.19%    | -7.17%             | -30.87% |     0.15 |       52 | 39.93%     | ok               |

## BAC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -10.23%  | 49.87%             | -20.40% |    -0.28 |       58 | 33.94%     | ok               |
|          20 | -14.81%  | 49.87%             | -20.73% |    -0.3  |       79 | 50.58%     | ok               |
|          35 | -14.80%  | 49.87%             | -27.83% |    -0.39 |       70 | 41.93%     | ok               |
|          15 | -19.29%  | 49.87%             | -22.24% |    -0.4  |       81 | 55.57%     | ok               |
|          50 | -13.28%  | 49.87%             | -20.35% |    -0.42 |       56 | 30.95%     | ok               |

## BCH-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -48.02%  | -31.80%            | -61.84% |    -0.49 |       87 | 57.09%     | ok               |
|          30 | -44.02%  | -31.80%            | -58.22% |    -0.51 |       80 | 45.21%     | ok               |
|          20 | -48.59%  | -31.80%            | -59.88% |    -0.53 |       84 | 52.30%     | ok               |
|          25 | -49.45%  | -31.80%            | -61.30% |    -0.59 |       76 | 47.70%     | ok               |
|          40 | -48.38%  | -31.80%            | -62.46% |    -0.68 |       65 | 38.12%     | ok               |

## BITO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 17.67%   | -53.20%            | -32.29% |     0.38 |       52 | 24.13%     | ok               |
|          30 | 3.90%    | -53.20%            | -42.82% |     0.22 |       76 | 38.77%     | ok               |
|          15 | -2.62%   | -53.20%            | -48.38% |     0.17 |       85 | 47.59%     | ok               |
|          45 | -1.86%   | -53.20%            | -43.53% |     0.13 |       56 | 27.12%     | ok               |
|          25 | -4.32%   | -53.20%            | -41.73% |     0.13 |       80 | 41.76%     | ok               |

## BLK Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 4.68%    | 33.73%             | -14.19% |     0.21 |       80 | 38.60%     | ok               |
|          40 | 3.48%    | 33.73%             | -15.20% |     0.18 |       74 | 34.28%     | ok               |
|          20 | 0.36%    | 33.73%             | -17.89% |     0.09 |       77 | 47.25%     | ok               |
|          30 | -1.96%   | 33.73%             | -20.81% |     0.01 |       75 | 42.43%     | ok               |
|          25 | -2.94%   | 33.73%             | -19.84% |    -0.01 |       75 | 44.76%     | ok               |

## BND Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -7.25%   | 0.98%              | -9.05%  |    -1.05 |       69 | 39.27%     | ok               |
|          25 | -7.47%   | 0.98%              | -10.14% |    -1.13 |       71 | 36.61%     | ok               |
|          30 | -7.84%   | 0.98%              | -9.89%  |    -1.25 |       67 | 32.61%     | ok               |
|          15 | -9.46%   | 0.98%              | -10.58% |    -1.35 |       73 | 42.26%     | ok               |
|          45 | -8.27%   | 0.98%              | -9.57%  |    -1.58 |       52 | 22.13%     | ok               |

## BONK-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 130.52%  | -82.74%            | -35.57% |     1.09 |       42 | 21.07%     | ok               |
|          20 | 140.72%  | -82.74%            | -55.43% |     0.95 |       68 | 50.96%     | ok               |
|          45 | 101.63%  | -82.74%            | -42.36% |     0.94 |       52 | 24.52%     | ok               |
|          25 | 124.58%  | -82.74%            | -47.99% |     0.91 |       67 | 46.17%     | ok               |
|          15 | 132.88%  | -82.74%            | -63.45% |     0.91 |       69 | 55.36%     | ok               |

## BTC-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 28.33%   | -21.89%            | -19.59% |     0.63 |       42 | 28.93%     | ok               |
|          40 | 25.48%   | -21.89%            | -20.30% |     0.57 |       46 | 32.38%     | ok               |
|          50 | 14.92%   | -21.89%            | -17.58% |     0.41 |       40 | 25.29%     | ok               |
|          35 | 8.44%    | -21.89%            | -32.64% |     0.28 |       70 | 39.46%     | ok               |
|          30 | -6.89%   | -21.89%            | -29.09% |     0.02 |       72 | 46.36%     | ok               |

## C Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -13.97%  | 131.73%            | -21.64% |    -0.34 |       70 | 35.27%     | ok               |
|          15 | -27.74%  | 131.73%            | -34.03% |    -0.5  |       76 | 60.23%     | ok               |
|          25 | -26.44%  | 131.73%            | -33.47% |    -0.5  |       75 | 53.41%     | ok               |
|          20 | -28.30%  | 131.73%            | -34.53% |    -0.54 |       81 | 56.57%     | ok               |
|          45 | -22.96%  | 131.73%            | -29.28% |    -0.59 |       84 | 39.93%     | ok               |

## CAT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 30.32%   | 203.14%            | -21.02% |     0.57 |       74 | 58.24%     | ok               |
|          25 | 30.43%   | 203.14%            | -26.37% |     0.56 |       70 | 61.06%     | ok               |
|          20 | 27.79%   | 203.14%            | -25.65% |     0.53 |       80 | 64.39%     | ok               |
|          45 | 21.92%   | 203.14%            | -28.85% |     0.47 |       58 | 46.59%     | ok               |
|          50 | 19.30%   | 203.14%            | -26.39% |     0.44 |       60 | 44.09%     | ok               |

## CL Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 22.58%   | 12.69%             | -14.32% |     0.74 |       60 | 49.08%     | ok               |
|          45 | 17.77%   | 12.69%             | -13.51% |     0.7  |       46 | 35.94%     | ok               |
|          50 | 16.80%   | 12.69%             | -13.51% |     0.69 |       44 | 33.11%     | ok               |
|          35 | 16.75%   | 12.69%             | -13.83% |     0.59 |       62 | 45.42%     | ok               |
|          15 | 17.47%   | 12.69%             | -13.35% |     0.56 |       60 | 56.41%     | ok               |

## CMCSA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -36.01%  | -38.35%            | -39.80% |    -0.9  |       80 | 44.26%     | ok               |
|          15 | -39.51%  | -38.35%            | -49.03% |    -0.93 |       89 | 58.74%     | ok               |
|          25 | -41.18%  | -38.35%            | -44.66% |    -1.06 |       87 | 49.08%     | ok               |
|          20 | -42.72%  | -38.35%            | -47.23% |    -1.08 |       95 | 55.07%     | ok               |
|          50 | -29.51%  | -38.35%            | -33.68% |    -1.08 |       50 | 17.14%     | ok               |

## COMP-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -20.22%  | -76.31%            | -38.71% |    -0.09 |       46 | 19.73%     | ok               |
|          25 | -45.78%  | -76.31%            | -63.29% |    -0.32 |       91 | 49.62%     | ok               |
|          30 | -44.84%  | -76.31%            | -63.55% |    -0.35 |       91 | 44.25%     | ok               |
|          15 | -54.66%  | -76.31%            | -67.05% |    -0.43 |      109 | 61.69%     | ok               |
|          40 | -44.82%  | -76.31%            | -47.56% |    -0.46 |       74 | 32.18%     | ok               |

## COP Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -16.52%  | -2.19%             | -34.85% |    -0.32 |       54 | 28.12%     | ok               |
|          45 | -23.78%  | -2.19%             | -41.14% |    -0.52 |       66 | 30.95%     | ok               |
|          35 | -26.65%  | -2.19%             | -43.88% |    -0.52 |       81 | 38.10%     | ok               |
|          30 | -27.18%  | -2.19%             | -43.99% |    -0.52 |       81 | 42.10%     | ok               |
|          25 | -34.54%  | -2.19%             | -49.23% |    -0.7  |       90 | 46.26%     | ok               |

## COST Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | 22.40%   | 45.78%             | -24.73% |     0.65 |       63 | 51.58%     | ok               |
|          20 | 21.77%   | 45.78%             | -24.32% |     0.62 |       64 | 54.08%     | ok               |
|          35 | 16.57%   | 45.78%             | -26.58% |     0.54 |       56 | 44.93%     | ok               |
|          40 | 9.41%    | 45.78%             | -28.41% |     0.35 |       58 | 41.93%     | ok               |
|          30 | 10.01%   | 45.78%             | -29.73% |     0.35 |       64 | 48.09%     | ok               |

## CRM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -24.32%  | -23.90%            | -38.20% |    -0.31 |       91 | 56.24%     | ok               |
|          35 | -20.16%  | -23.90%            | -35.46% |    -0.34 |       66 | 39.93%     | ok               |
|          40 | -27.40%  | -23.90%            | -41.30% |    -0.59 |       70 | 35.61%     | ok               |
|          30 | -31.42%  | -23.90%            | -40.29% |    -0.6  |       68 | 44.76%     | ok               |
|          20 | -37.89%  | -23.90%            | -42.67% |    -0.68 |       79 | 49.75%     | ok               |

## CRV-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 35.85%   | -76.07%            | -37.78% |     0.55 |       60 | 26.82%     | ok               |
|          50 | 29.03%   | -76.07%            | -29.30% |     0.51 |       34 | 15.71%     | ok               |
|          40 | 19.29%   | -76.07%            | -38.86% |     0.41 |       50 | 23.18%     | ok               |
|          45 | 16.48%   | -76.07%            | -42.29% |     0.38 |       48 | 18.39%     | ok               |
|          30 | 8.54%    | -76.07%            | -39.89% |     0.31 |       60 | 31.23%     | ok               |

## CSCO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 30.21%   | 140.41%            | -19.34% |     0.69 |       56 | 37.44%     | ok               |
|          45 | 26.84%   | 140.41%            | -19.34% |     0.62 |       51 | 39.60%     | ok               |
|          30 | 23.67%   | 140.41%            | -21.79% |     0.53 |       61 | 48.42%     | ok               |
|          25 | 23.35%   | 140.41%            | -23.28% |     0.52 |       66 | 50.58%     | ok               |
|          40 | 21.13%   | 140.41%            | -19.61% |     0.5  |       53 | 42.10%     | ok               |

## CVX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -14.81%  | 21.32%             | -25.91% |    -0.34 |       74 | 44.59%     | ok               |
|          35 | -16.76%  | 21.32%             | -28.85% |    -0.44 |       69 | 39.10%     | ok               |
|          20 | -18.91%  | 21.32%             | -30.41% |    -0.47 |       80 | 46.09%     | ok               |
|          30 | -19.18%  | 21.32%             | -29.70% |    -0.51 |       75 | 42.10%     | ok               |
|          40 | -17.80%  | 21.32%             | -28.41% |    -0.52 |       79 | 36.11%     | ok               |

## DASH-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 109.52%  | 3.58%              | -34.71% |     0.88 |       42 | 15.90%     | ok               |
|          40 | 64.67%   | 3.58%              | -34.44% |     0.67 |       46 | 22.61%     | ok               |
|          45 | 51.31%   | 3.58%              | -42.52% |     0.6  |       46 | 18.20%     | ok               |
|          25 | -35.92%  | 3.58%              | -64.14% |     0.06 |       71 | 33.52%     | ok               |
|          35 | -39.92%  | 3.58%              | -63.23% |     0    |       71 | 27.01%     | ok               |

## DBC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -7.75%   | 33.21%             | -20.31% |    -0.29 |       40 | 21.13%     | ok               |
|          45 | -9.53%   | 33.21%             | -21.46% |    -0.33 |       54 | 24.63%     | ok               |
|          35 | -11.02%  | 33.21%             | -23.91% |    -0.37 |       62 | 31.61%     | ok               |
|          15 | -11.67%  | 33.21%             | -26.60% |    -0.38 |       65 | 38.44%     | ok               |
|          30 | -12.97%  | 33.21%             | -25.70% |    -0.44 |       62 | 33.78%     | ok               |

## DE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -9.56%   | 36.93%             | -28.94% |    -0.12 |       74 | 51.25%     | ok               |
|          50 | -7.18%   | 36.93%             | -23.74% |    -0.13 |       62 | 29.78%     | ok               |
|          15 | -11.19%  | 36.93%             | -27.41% |    -0.16 |       78 | 54.58%     | ok               |
|          25 | -10.96%  | 36.93%             | -26.67% |    -0.16 |       76 | 48.42%     | ok               |
|          30 | -11.10%  | 36.93%             | -25.98% |    -0.17 |       74 | 45.59%     | ok               |

## DIA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | 0.07%    | 36.34%             | -11.28% |     0.04 |       58 | 47.75%     | ok               |
|          35 | 0.07%    | 36.34%             | -13.15% |     0.04 |       60 | 44.59%     | ok               |
|          30 | -1.59%   | 36.34%             | -12.94% |    -0.05 |       58 | 46.42%     | ok               |
|          20 | -2.76%   | 36.34%             | -14.29% |    -0.1  |       60 | 50.25%     | ok               |
|          40 | -3.77%   | 36.34%             | -15.06% |    -0.18 |       66 | 41.60%     | ok               |

## DIS Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 40.04%   | 12.02%             | -14.24% |     0.96 |       46 | 30.12%     | ok               |
|          45 | 9.81%    | 12.02%             | -15.09% |     0.3  |       49 | 33.44%     | ok               |
|          40 | 8.82%    | 12.02%             | -22.77% |     0.28 |       61 | 38.60%     | ok               |
|          35 | 5.61%    | 12.02%             | -20.85% |     0.21 |       69 | 44.43%     | ok               |
|          30 | 2.59%    | 12.02%             | -22.67% |     0.16 |       59 | 47.42%     | ok               |

## DOGE-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -1.64%   | -67.73%            | -57.89% |     0.28 |       83 | 64.56%     | ok               |
|          20 | -12.57%  | -67.73%            | -55.83% |     0.16 |       86 | 60.34%     | ok               |
|          25 | -15.60%  | -67.73%            | -53.72% |     0.12 |       74 | 53.83%     | ok               |
|          30 | -27.16%  | -67.73%            | -60.95% |    -0.03 |       77 | 48.28%     | ok               |
|          35 | -52.30%  | -67.73%            | -67.40% |    -0.51 |       74 | 41.57%     | ok               |

## DOT-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -24.98%  | -82.81%            | -43.91% |    -0.21 |       54 | 26.25%     | ok               |
|          45 | -29.59%  | -82.81%            | -48.71% |    -0.26 |       50 | 29.69%     | ok               |
|          30 | -46.93%  | -82.81%            | -57.66% |    -0.34 |       88 | 46.74%     | ok               |
|          35 | -45.90%  | -82.81%            | -59.34% |    -0.35 |       78 | 40.04%     | ok               |
|          40 | -37.31%  | -82.81%            | -48.60% |    -0.35 |       56 | 33.14%     | ok               |

## DXY-INDEX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -6.31%   | -5.14%             | -12.09% |    -0.58 |       90 | 75.27%     | ok               |
|          40 | -4.73%   | -5.14%             | -7.30%  |    -0.6  |       70 | 45.55%     | ok               |
|          30 | -5.44%   | -5.14%             | -10.51% |    -0.62 |       68 | 57.70%     | ok               |
|          50 | -4.07%   | -5.14%             | -6.05%  |    -0.67 |       42 | 26.68%     | ok               |
|          45 | -4.93%   | -5.14%             | -8.12%  |    -0.68 |       66 | 35.14%     | ok               |

## EEM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -4.96%   | 73.94%             | -19.52% |    -0.11 |       64 | 39.77%     | ok               |
|          35 | -5.62%   | 73.94%             | -23.88% |    -0.12 |       66 | 41.76%     | ok               |
|          50 | -4.94%   | 73.94%             | -15.88% |    -0.12 |       52 | 35.77%     | ok               |
|          45 | -6.04%   | 73.94%             | -17.36% |    -0.16 |       54 | 37.44%     | ok               |
|          25 | -8.49%   | 73.94%             | -25.60% |    -0.21 |       65 | 44.76%     | ok               |

## EFA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -1.66%   | 41.30%             | -11.27% |     0    |       60 | 51.75%     | ok               |
|          20 | -7.88%   | 41.30%             | -12.37% |    -0.26 |       65 | 48.92%     | ok               |
|          30 | -9.30%   | 41.30%             | -13.53% |    -0.34 |       60 | 43.76%     | ok               |
|          50 | -9.33%   | 41.30%             | -17.80% |    -0.41 |       56 | 36.44%     | ok               |
|          25 | -11.34%  | 41.30%             | -15.78% |    -0.42 |       64 | 46.42%     | ok               |

## EOG Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -29.95%  | 10.80%             | -48.13% |    -0.69 |       83 | 47.75%     | ok               |
|          25 | -31.71%  | 10.80%             | -51.99% |    -0.7  |       84 | 51.08%     | ok               |
|          40 | -28.13%  | 10.80%             | -43.26% |    -0.72 |       64 | 36.77%     | ok               |
|          45 | -28.02%  | 10.80%             | -43.17% |    -0.76 |       58 | 33.28%     | ok               |
|          35 | -30.72%  | 10.80%             | -46.26% |    -0.77 |       81 | 42.43%     | ok               |

## ETC-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -14.16%  | -68.53%            | -30.24% |    -0.14 |       26 | 16.86%     | ok               |
|          35 | -25.86%  | -68.53%            | -42.62% |    -0.33 |       44 | 25.48%     | ok               |
|          45 | -26.10%  | -68.53%            | -36.69% |    -0.4  |       26 | 18.01%     | ok               |
|          40 | -30.03%  | -68.53%            | -41.87% |    -0.48 |       40 | 21.46%     | ok               |
|          30 | -46.65%  | -68.53%            | -54.25% |    -0.8  |       70 | 30.27%     | ok               |

## ETH-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 113.02%  | -39.76%            | -30.11% |     1.08 |       62 | 43.10%     | ok               |
|          30 | 105.90%  | -39.76%            | -32.89% |     1.01 |       66 | 50.96%     | ok               |
|          40 | 44.66%   | -39.76%            | -33.11% |     0.66 |       56 | 35.82%     | ok               |
|          50 | 31.75%   | -39.76%            | -30.50% |     0.55 |       54 | 26.44%     | ok               |
|          45 | 27.41%   | -39.76%            | -34.50% |     0.5  |       52 | 31.99%     | ok               |

## EWJ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -18.27%  | 46.32%             | -30.73% |    -0.59 |       64 | 41.43%     | ok               |
|          20 | -19.65%  | 46.32%             | -31.32% |    -0.62 |       60 | 43.43%     | ok               |
|          25 | -21.97%  | 46.32%             | -31.18% |    -0.72 |       60 | 42.43%     | ok               |
|          35 | -22.19%  | 46.32%             | -32.54% |    -0.75 |       70 | 39.77%     | ok               |
|          15 | -24.97%  | 46.32%             | -32.24% |    -0.78 |       74 | 46.59%     | ok               |

## FCX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -13.05%  | 58.68%             | -27.80% |    -0.11 |       58 | 28.95%     | ok               |
|          45 | -17.23%  | 58.68%             | -35.28% |    -0.17 |       60 | 33.44%     | ok               |
|          40 | -29.04%  | 58.68%             | -44.23% |    -0.4  |       70 | 38.44%     | ok               |
|          20 | -36.87%  | 58.68%             | -57.65% |    -0.46 |       80 | 52.75%     | ok               |
|          30 | -35.07%  | 58.68%             | -48.56% |    -0.49 |       73 | 45.09%     | ok               |

## FET-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 79.75%   | -79.82%            | -47.06% |     0.76 |       86 | 50.57%     | ok               |
|          15 | 23.84%   | -79.82%            | -54.00% |     0.48 |       88 | 53.83%     | ok               |
|          25 | 10.12%   | -79.82%            | -47.79% |     0.37 |       89 | 43.87%     | ok               |
|          30 | -3.25%   | -79.82%            | -48.39% |     0.25 |       77 | 39.66%     | ok               |
|          35 | -28.73%  | -79.82%            | -53.17% |    -0.09 |       65 | 33.14%     | ok               |

## FIL-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -4.52%   | -81.01%            | -43.79% |     0.12 |       48 | 23.18%     | ok               |
|          50 | -17.17%  | -81.01%            | -42.59% |    -0.12 |       38 | 13.22%     | ok               |
|          30 | -26.60%  | -81.01%            | -46.68% |    -0.16 |       70 | 32.76%     | ok               |
|          35 | -26.06%  | -81.01%            | -46.24% |    -0.18 |       56 | 27.20%     | ok               |
|          45 | -24.84%  | -81.01%            | -41.50% |    -0.22 |       46 | 17.82%     | ok               |

## FXI Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -10.87%  | 50.88%             | -23.91% |    -0.2  |       44 | 26.46%     | ok               |
|          50 | -10.98%  | 50.88%             | -23.27% |    -0.23 |       36 | 19.30%     | ok               |
|          25 | -12.39%  | 50.88%             | -22.57% |    -0.24 |       46 | 27.45%     | ok               |
|          45 | -12.44%  | 50.88%             | -24.52% |    -0.27 |       40 | 21.30%     | ok               |
|          15 | -14.30%  | 50.88%             | -21.68% |    -0.28 |       52 | 31.11%     | ok               |

## GDX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 21.37%   | 200.60%            | -31.87% |     0.46 |       60 | 43.09%     | ok               |
|          20 | 14.61%   | 200.60%            | -35.59% |     0.35 |       72 | 53.24%     | ok               |
|          35 | 6.14%    | 200.60%            | -32.37% |     0.23 |       66 | 45.59%     | ok               |
|          30 | 3.89%    | 200.60%            | -34.99% |     0.19 |       62 | 48.92%     | ok               |
|          50 | 3.99%    | 200.60%            | -28.64% |     0.19 |       50 | 38.27%     | ok               |

## GDXJ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -8.43%   | 231.55%            | -45.05% |     0.04 |       67 | 52.91%     | ok               |
|          50 | -10.73%  | 231.55%            | -35.02% |    -0.06 |       62 | 37.77%     | ok               |
|          30 | -22.23%  | 231.55%            | -44.93% |    -0.22 |       66 | 47.25%     | ok               |
|          25 | -26.04%  | 231.55%            | -47.26% |    -0.26 |       70 | 49.75%     | ok               |
|          40 | -24.73%  | 231.55%            | -44.27% |    -0.3  |       64 | 42.76%     | ok               |

## GE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 21.26%   | 221.22%            | -22.29% |     0.49 |       66 | 38.44%     | ok               |
|          45 | 13.14%   | 221.22%            | -25.68% |     0.35 |       76 | 41.43%     | ok               |
|          20 | 13.85%   | 221.22%            | -26.63% |     0.34 |       69 | 55.41%     | ok               |
|          15 | 8.99%    | 221.22%            | -28.62% |     0.27 |       68 | 57.74%     | ok               |
|          35 | 8.74%    | 221.22%            | -27.11% |     0.27 |       80 | 46.92%     | ok               |

## GLD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | 19.38%   | 120.29%            | -14.61% |     0.54 |       48 | 44.93%     | ok               |
|          20 | 18.59%   | 120.29%            | -14.61% |     0.52 |       50 | 46.09%     | ok               |
|          30 | 17.86%   | 120.29%            | -16.63% |     0.51 |       50 | 43.93%     | ok               |
|          35 | 12.10%   | 120.29%            | -17.29% |     0.38 |       52 | 43.26%     | ok               |
|          15 | 12.22%   | 120.29%            | -16.82% |     0.37 |       52 | 50.75%     | ok               |

## GOOGL Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | 91.02%   | 180.22%            | -19.76% |     1.26 |       59 | 57.74%     | ok               |
|          15 | 89.59%   | 180.22%            | -13.59% |     1.2  |       67 | 65.06%     | ok               |
|          30 | 81.90%   | 180.22%            | -20.41% |     1.19 |       65 | 55.57%     | ok               |
|          20 | 78.46%   | 180.22%            | -20.57% |     1.13 |       68 | 59.90%     | ok               |
|          35 | 65.89%   | 180.22%            | -22.85% |     1.08 |       71 | 50.42%     | ok               |

## GRT-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 24.22%   | -87.38%            | -30.82% |     0.47 |       46 | 22.03%     | ok               |
|          15 | -10.69%  | -87.38%            | -49.67% |     0.16 |       79 | 60.54%     | ok               |
|          45 | -2.37%   | -87.38%            | -49.33% |     0.15 |       52 | 26.25%     | ok               |
|          35 | -7.85%   | -87.38%            | -50.43% |     0.11 |       64 | 35.06%     | ok               |
|          40 | -6.53%   | -87.38%            | -48.92% |     0.1  |       54 | 29.50%     | ok               |

## GS Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 26.30%   | 165.39%            | -20.56% |     0.56 |       74 | 59.90%     | ok               |
|          20 | 9.07%    | 165.39%            | -23.19% |     0.28 |       74 | 55.91%     | ok               |
|          25 | 5.62%    | 165.39%            | -23.32% |     0.21 |       74 | 53.41%     | ok               |
|          40 | 0.86%    | 165.39%            | -17.88% |     0.11 |       72 | 44.26%     | ok               |
|          30 | -0.53%   | 165.39%            | -22.13% |     0.09 |       76 | 50.92%     | ok               |

## HD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -0.67%   | -7.52%             | -17.69% |     0.06 |       69 | 45.59%     | ok               |
|          25 | -1.44%   | -7.52%             | -18.51% |     0.04 |       68 | 47.59%     | ok               |
|          35 | -9.91%   | -7.52%             | -22.98% |    -0.21 |       76 | 41.93%     | ok               |
|          40 | -10.67%  | -7.52%             | -20.58% |    -0.28 |       82 | 35.44%     | ok               |
|          20 | -14.17%  | -7.52%             | -23.94% |    -0.3  |       85 | 50.75%     | ok               |

## HON Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -11.42%  | 24.00%             | -23.12% |    -0.33 |       74 | 31.45%     | ok               |
|          45 | -14.16%  | 24.00%             | -22.74% |    -0.4  |       80 | 36.94%     | ok               |
|          40 | -15.10%  | 24.00%             | -23.13% |    -0.41 |       80 | 40.93%     | ok               |
|          35 | -16.73%  | 24.00%             | -26.26% |    -0.45 |       95 | 47.25%     | ok               |
|          30 | -19.02%  | 24.00%             | -28.64% |    -0.5  |       95 | 51.58%     | ok               |

## HYG Threshold Sweep

|   threshold | return   | benchmark_return   | mdd    |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:-------|---------:|---------:|:-----------|:-----------------|
|          40 | -7.28%   | 4.73%              | -8.02% |    -0.87 |       70 | 29.78%     | ok               |
|          15 | -8.56%   | 4.73%              | -9.99% |    -0.91 |       90 | 42.10%     | ok               |
|          20 | -8.48%   | 4.73%              | -9.99% |    -0.93 |       88 | 39.77%     | ok               |
|          45 | -7.96%   | 4.73%              | -8.70% |    -0.99 |       66 | 26.62%     | ok               |
|          25 | -9.14%   | 4.73%              | -9.87% |    -1.02 |       85 | 37.44%     | ok               |

## IBIT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 52.15%   | 9.52%              | -12.64% |     1.12 |       18 | 21.36%     | ok               |
|          15 | 64.79%   | 9.52%              | -19.20% |     1.11 |       36 | 37.44%     | ok               |
|          45 | 43.69%   | 9.52%              | -17.12% |     0.96 |       20 | 22.11%     | ok               |
|          40 | 42.27%   | 9.52%              | -17.12% |     0.93 |       22 | 23.62%     | ok               |
|          30 | 35.78%   | 9.52%              | -18.95% |     0.79 |       30 | 29.40%     | ok               |

## IBM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 54.17%   | 87.11%             | -28.20% |     0.91 |       87 | 62.56%     | ok               |
|          30 | 45.79%   | 87.11%             | -25.31% |     0.9  |       74 | 50.42%     | ok               |
|          35 | 39.44%   | 87.11%             | -25.15% |     0.82 |       70 | 45.92%     | ok               |
|          45 | 32.44%   | 87.11%             | -18.73% |     0.75 |       54 | 36.77%     | ok               |
|          50 | 27.72%   | 87.11%             | -21.46% |     0.67 |       52 | 33.78%     | ok               |

## ICP-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 26.47%   | -73.26%            | -36.91% |     0.47 |       64 | 30.84%     | ok               |
|          40 | 19.79%   | -73.26%            | -29.38% |     0.41 |       58 | 26.44%     | ok               |
|          50 | 12.63%   | -73.26%            | -32.35% |     0.33 |       38 | 16.67%     | ok               |
|          30 | 7.21%    | -73.26%            | -50.29% |     0.32 |       81 | 36.78%     | ok               |
|          20 | -23.37%  | -73.26%            | -56.15% |     0.08 |       94 | 48.08%     | ok               |

## IEF Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -8.36%   | -0.71%             | -9.79%  |    -1    |       74 | 42.26%     | ok               |
|          15 | -8.91%   | -0.71%             | -10.52% |    -1.05 |       73 | 43.76%     | ok               |
|          40 | -8.39%   | -0.71%             | -9.67%  |    -1.31 |       60 | 24.79%     | ok               |
|          45 | -8.07%   | -0.71%             | -9.73%  |    -1.33 |       50 | 22.80%     | ok               |
|          25 | -10.98%  | -0.71%             | -11.58% |    -1.38 |       76 | 39.77%     | ok               |

## IEMG Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | -0.32%   | 68.02%             | -22.13% |     0.05 |       63 | 42.60%     | ok               |
|          50 | -2.69%   | 68.02%             | -14.40% |    -0.05 |       56 | 33.94%     | ok               |
|          40 | -2.99%   | 68.02%             | -18.89% |    -0.05 |       62 | 39.77%     | ok               |
|          45 | -2.90%   | 68.02%             | -15.40% |    -0.05 |       52 | 36.61%     | ok               |
|          25 | -4.72%   | 68.02%             | -25.58% |    -0.09 |       59 | 45.42%     | ok               |

## INJ-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -11.23%  | -68.99%            | -58.69% |     0.03 |       48 | 22.99%     | ok               |
|          50 | -13.89%  | -68.99%            | -52.76% |    -0.03 |       52 | 19.73%     | ok               |
|          35 | -27.50%  | -68.99%            | -68.10% |    -0.12 |       62 | 32.76%     | ok               |
|          40 | -34.79%  | -68.99%            | -67.68% |    -0.29 |       52 | 29.12%     | ok               |
|          20 | -49.60%  | -68.99%            | -80.74% |    -0.35 |       81 | 47.89%     | ok               |

## INTC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 90.13%   | 144.57%            | -53.65% |     0.77 |       84 | 62.06%     | ok               |
|          25 | 86.35%   | 144.57%            | -56.41% |     0.77 |       75 | 52.25%     | ok               |
|          45 | 76.87%   | 144.57%            | -49.32% |     0.75 |       62 | 35.11%     | ok               |
|          20 | 83.38%   | 144.57%            | -52.47% |     0.75 |       82 | 57.24%     | ok               |
|          40 | 72.42%   | 144.57%            | -55.86% |     0.71 |       68 | 39.43%     | ok               |

## INTU Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -1.36%   | -43.71%            | -42.41% |     0.09 |       69 | 28.62%     | ok               |
|          45 | -4.74%   | -43.71%            | -44.25% |     0.03 |       67 | 32.78%     | ok               |
|          15 | -9.50%   | -43.71%            | -47.30% |    -0.03 |       81 | 51.41%     | ok               |
|          25 | -11.92%  | -43.71%            | -42.24% |    -0.08 |       66 | 45.59%     | ok               |
|          40 | -11.09%  | -43.71%            | -48.32% |    -0.09 |       73 | 35.77%     | ok               |

## ITA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 9.38%    | 90.12%             | -21.48% |     0.37 |       72 | 35.44%     | ok               |
|          30 | 4.96%    | 90.12%             | -23.75% |     0.22 |       70 | 45.42%     | ok               |
|          35 | 2.26%    | 90.12%             | -23.16% |     0.14 |       74 | 43.59%     | ok               |
|          15 | 1.15%    | 90.12%             | -26.46% |     0.11 |       89 | 58.40%     | ok               |
|          40 | 1.08%    | 90.12%             | -20.58% |     0.1  |       76 | 40.10%     | ok               |

## IWM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 9.94%    | 50.29%             | -12.83% |     0.4  |       50 | 36.77%     | ok               |
|          25 | 8.91%    | 50.29%             | -14.80% |     0.36 |       52 | 38.44%     | ok               |
|          35 | 7.46%    | 50.29%             | -14.41% |     0.33 |       50 | 34.44%     | ok               |
|          40 | 6.82%    | 50.29%             | -14.38% |     0.32 |       44 | 31.95%     | ok               |
|          20 | 3.62%    | 50.29%             | -15.32% |     0.18 |       64 | 39.60%     | ok               |

## JNJ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 15.67%   | 39.84%             | -11.39% |     0.69 |       62 | 38.27%     | ok               |
|          15 | 10.62%   | 39.84%             | -18.02% |     0.4  |       72 | 58.24%     | ok               |
|          20 | 7.87%    | 39.84%             | -17.61% |     0.33 |       76 | 54.74%     | ok               |
|          45 | 6.05%    | 39.84%             | -15.23% |     0.3  |       64 | 43.26%     | ok               |
|          40 | 4.54%    | 39.84%             | -14.77% |     0.23 |       70 | 47.59%     | ok               |

## JPM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 10.69%   | 73.74%             | -15.37% |     0.41 |       56 | 40.27%     | ok               |
|          45 | 1.13%    | 73.74%             | -21.42% |     0.1  |       56 | 43.43%     | ok               |
|          40 | -10.85%  | 73.74%             | -26.90% |    -0.26 |       66 | 45.76%     | ok               |
|          20 | -16.13%  | 73.74%             | -32.15% |    -0.3  |       84 | 57.40%     | ok               |
|          35 | -15.83%  | 73.74%             | -25.84% |    -0.4  |       72 | 49.42%     | ok               |

## KO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 23.88%   | 32.41%             | -8.07%  |     0.9  |       49 | 37.10%     | ok               |
|          35 | 19.53%   | 32.41%             | -8.07%  |     0.77 |       52 | 35.94%     | ok               |
|          50 | 16.39%   | 32.41%             | -11.40% |     0.75 |       34 | 26.62%     | ok               |
|          25 | 19.12%   | 32.41%             | -9.33%  |     0.74 |       55 | 39.60%     | ok               |
|          40 | 17.12%   | 32.41%             | -9.28%  |     0.73 |       54 | 32.95%     | ok               |

## LDO-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -12.56%  | -82.81%            | -47.58% |     0.22 |       86 | 50.96%     | ok               |
|          20 | -11.48%  | -82.81%            | -44.97% |     0.21 |       91 | 46.17%     | ok               |
|          30 | -22.36%  | -82.81%            | -60.93% |     0.05 |       80 | 36.59%     | ok               |
|          50 | -11.51%  | -82.81%            | -48.04% |    -0.01 |       44 | 16.28%     | ok               |
|          25 | -33.65%  | -82.81%            | -56.60% |    -0.05 |       87 | 42.15%     | ok               |

## LIN Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 3.30%    | 21.65%             | -23.70% |     0.17 |       68 | 50.25%     | ok               |
|          25 | 1.46%    | 21.65%             | -22.01% |     0.11 |       68 | 41.93%     | ok               |
|          20 | -0.71%   | 21.65%             | -23.00% |     0.04 |       67 | 45.09%     | ok               |
|          35 | -2.45%   | 21.65%             | -21.18% |    -0.04 |       68 | 32.78%     | ok               |
|          30 | -3.07%   | 21.65%             | -21.53% |    -0.05 |       72 | 39.27%     | ok               |

## LINK-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -21.53%  | -57.63%            | -55.61% |    -0    |       70 | 40.04%     | ok               |
|          50 | -22.09%  | -57.63%            | -42.26% |    -0.11 |       36 | 20.11%     | ok               |
|          45 | -26.83%  | -57.63%            | -43.89% |    -0.15 |       48 | 24.52%     | ok               |
|          35 | -34.60%  | -57.63%            | -53.72% |    -0.21 |       60 | 34.67%     | ok               |
|          25 | -45.70%  | -57.63%            | -56.54% |    -0.3  |       66 | 45.59%     | ok               |

## LLY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 28.11%   | 78.64%             | -38.23% |     0.59 |       42 | 38.94%     | ok               |
|          45 | 15.82%   | 78.64%             | -42.66% |     0.39 |       50 | 42.10%     | ok               |
|          15 | 9.22%    | 78.64%             | -48.12% |     0.27 |       63 | 61.56%     | ok               |
|          40 | -1.50%   | 78.64%             | -46.23% |     0.1  |       62 | 44.59%     | ok               |
|          20 | -8.36%   | 78.64%             | -51.34% |     0    |       72 | 56.57%     | ok               |

## LRCX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 12.61%   | 334.43%            | -60.45% |     0.32 |       81 | 56.07%     | ok               |
|          50 | 0.69%    | 334.43%            | -50.39% |     0.15 |       76 | 36.61%     | ok               |
|          40 | -9.55%   | 334.43%            | -56.86% |     0.02 |       74 | 42.60%     | ok               |
|          35 | -12.11%  | 334.43%            | -61.76% |    -0.01 |       82 | 45.26%     | ok               |
|          20 | -14.66%  | 334.43%            | -67.64% |    -0.03 |       89 | 51.25%     | ok               |

## LTC-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -31.32%  | -48.29%            | -47.47% |    -0.35 |       56 | 30.65%     | ok               |
|          50 | -32.64%  | -48.29%            | -48.91% |    -0.4  |       52 | 24.52%     | ok               |
|          35 | -37.21%  | -48.29%            | -56.94% |    -0.4  |       68 | 41.19%     | ok               |
|          30 | -46.55%  | -48.29%            | -55.90% |    -0.55 |       68 | 46.74%     | ok               |
|          40 | -44.45%  | -48.29%            | -58.13% |    -0.58 |       60 | 36.40%     | ok               |

## MCD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 2.92%    | -3.39%             | -9.22%  |     0.19 |       44 | 20.47%     | ok               |
|          30 | -0.66%   | -3.39%             | -19.14% |     0.03 |       75 | 39.27%     | ok               |
|          25 | -2.03%   | -3.39%             | -20.77% |    -0.02 |       75 | 41.76%     | ok               |
|          40 | -6.24%   | -3.39%             | -16.86% |    -0.24 |       73 | 29.78%     | ok               |
|          35 | -7.87%   | -3.39%             | -15.80% |    -0.29 |       71 | 35.77%     | ok               |

## META Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 21.42%   | 79.72%             | -31.03% |     0.44 |       68 | 42.10%     | ok               |
|          40 | 8.07%    | 79.72%             | -35.11% |     0.25 |       68 | 45.09%     | ok               |
|          25 | 7.25%    | 79.72%             | -33.76% |     0.24 |       67 | 55.41%     | ok               |
|          30 | 4.38%    | 79.72%             | -33.10% |     0.2  |       72 | 52.25%     | ok               |
|          50 | 2.89%    | 79.72%             | -34.00% |     0.17 |       72 | 38.27%     | ok               |

## MPC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 14.51%   | 63.13%             | -23.96% |     0.37 |       52 | 38.60%     | ok               |
|          45 | 7.28%    | 63.13%             | -25.09% |     0.25 |       58 | 42.26%     | ok               |
|          40 | 5.66%    | 63.13%             | -25.70% |     0.22 |       60 | 44.59%     | ok               |
|          35 | 2.39%    | 63.13%             | -35.90% |     0.16 |       68 | 47.09%     | ok               |
|          30 | -13.72%  | 63.13%             | -44.76% |    -0.13 |       71 | 49.92%     | ok               |

## MRK Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -11.90%  | 1.28%              | -29.91% |    -0.17 |       85 | 57.74%     | ok               |
|          25 | -11.47%  | 1.28%              | -31.07% |    -0.18 |       70 | 49.75%     | ok               |
|          20 | -15.81%  | 1.28%              | -29.38% |    -0.29 |       75 | 53.08%     | ok               |
|          35 | -17.26%  | 1.28%              | -30.50% |    -0.35 |       67 | 43.59%     | ok               |
|          30 | -17.88%  | 1.28%              | -32.14% |    -0.36 |       67 | 47.09%     | ok               |

## MS Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -2.45%   | 123.08%            | -19.61% |     0.01 |       70 | 38.77%     | ok               |
|          35 | -10.96%  | 123.08%            | -21.83% |    -0.21 |       74 | 43.93%     | ok               |
|          50 | -10.06%  | 123.08%            | -15.66% |    -0.3  |       58 | 30.45%     | ok               |
|          20 | -16.57%  | 123.08%            | -25.68% |    -0.33 |       84 | 52.58%     | ok               |
|          30 | -16.73%  | 123.08%            | -26.72% |    -0.36 |       81 | 47.75%     | ok               |

## MSFT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -9.69%   | 22.43%             | -25.28% |    -0.24 |       58 | 34.94%     | ok               |
|          50 | -13.45%  | 22.43%             | -28.69% |    -0.38 |       56 | 30.62%     | ok               |
|          35 | -22.64%  | 22.43%             | -30.52% |    -0.58 |       67 | 43.26%     | ok               |
|          40 | -23.56%  | 22.43%             | -32.42% |    -0.64 |       63 | 38.27%     | ok               |
|          25 | -26.35%  | 22.43%             | -31.00% |    -0.64 |       80 | 50.58%     | ok               |

## MU Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 345.64%  | 1063.57%           | -61.96% |     1.48 |       50 | 66.89%     | ok               |
|          25 | 261.30%  | 1063.57%           | -67.90% |     1.37 |       53 | 60.40%     | ok               |
|          40 | 222.27%  | 1063.57%           | -64.36% |     1.29 |       60 | 54.08%     | ok               |
|          20 | 230.79%  | 1063.57%           | -67.25% |     1.27 |       59 | 62.56%     | ok               |
|          30 | 207.77%  | 1063.57%           | -68.76% |     1.24 |       55 | 58.57%     | ok               |

## NEAR-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 86.16%   | -55.40%            | -46.05% |     0.88 |       48 | 25.48%     | ok               |
|          40 | 58.71%   | -55.40%            | -54.71% |     0.71 |       48 | 29.50%     | ok               |
|          50 | 50.31%   | -55.40%            | -51.39% |     0.67 |       46 | 20.31%     | ok               |
|          35 | 29.86%   | -55.40%            | -58.99% |     0.5  |       70 | 34.67%     | ok               |
|          15 | -5.42%   | -55.40%            | -54.94% |     0.26 |       94 | 58.62%     | ok               |

## NEM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 30.17%   | 172.21%            | -25.79% |     0.49 |       60 | 63.73%     | ok               |
|          20 | 16.24%   | 172.21%            | -30.47% |     0.36 |       70 | 59.23%     | ok               |
|          25 | -2.49%   | 172.21%            | -30.80% |     0.13 |       66 | 57.24%     | ok               |
|          30 | -19.45%  | 172.21%            | -38.49% |    -0.12 |       70 | 55.74%     | ok               |
|          35 | -19.14%  | 172.21%            | -39.55% |    -0.12 |       77 | 52.91%     | ok               |

## NFLX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 43.82%   | 81.45%             | -11.94% |     0.97 |       48 | 47.09%     | ok               |
|          50 | 37.40%   | 81.45%             | -16.28% |     0.92 |       50 | 39.10%     | ok               |
|          35 | 39.59%   | 81.45%             | -18.30% |     0.85 |       62 | 50.75%     | ok               |
|          45 | 30.35%   | 81.45%             | -15.48% |     0.75 |       56 | 43.09%     | ok               |
|          25 | 32.27%   | 81.45%             | -21.09% |     0.7  |       60 | 57.74%     | ok               |

## NKE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | -27.12%  | -54.71%            | -42.13% |    -0.38 |       77 | 39.27%     | ok               |
|          20 | -35.79%  | -54.71%            | -50.44% |    -0.46 |       97 | 54.91%     | ok               |
|          25 | -37.16%  | -54.71%            | -51.20% |    -0.5  |       95 | 51.08%     | ok               |
|          15 | -39.00%  | -54.71%            | -55.28% |    -0.52 |       98 | 59.57%     | ok               |
|          40 | -27.38%  | -54.71%            | -31.64% |    -0.52 |       67 | 31.11%     | ok               |

## NOW Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 43.44%   | -8.03%             | -26.36% |     0.64 |       77 | 51.25%     | ok               |
|          15 | 33.91%   | -8.03%             | -27.25% |     0.55 |       86 | 54.41%     | ok               |
|          25 | 32.42%   | -8.03%             | -26.83% |     0.54 |       72 | 48.75%     | ok               |
|          35 | 26.03%   | -8.03%             | -29.30% |     0.49 |       75 | 40.93%     | ok               |
|          30 | 23.56%   | -8.03%             | -31.32% |     0.44 |       78 | 45.76%     | ok               |

## NVDA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | 3.36%    | 145.61%            | -33.22% |     0.22 |       66 | 53.12%     | ok               |
|          30 | 1.42%    | 145.61%            | -35.26% |     0.18 |       68 | 50.80%     | ok               |
|          20 | -3.50%   | 145.61%            | -40.59% |     0.14 |       69 | 57.58%     | ok               |
|          35 | -10.46%  | 145.61%            | -41.25% |     0    |       80 | 47.95%     | ok               |
|          50 | -11.03%  | 145.61%            | -40.84% |    -0.03 |       60 | 35.29%     | ok               |

## OP-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 39.44%   | -93.55%            | -60.08% |     0.58 |       50 | 25.67%     | ok               |
|          50 | 30.16%   | -93.55%            | -36.11% |     0.53 |       36 | 12.64%     | ok               |
|          35 | 21.82%   | -93.55%            | -63.95% |     0.43 |       56 | 28.93%     | ok               |
|          45 | 17.45%   | -93.55%            | -53.32% |     0.39 |       42 | 17.62%     | ok               |
|          30 | -4.02%   | -93.55%            | -70.11% |     0.2  |       78 | 35.06%     | ok               |

## ORCL Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 186.64%  | 119.78%            | -21.44% |     1.25 |       73 | 64.23%     | ok               |
|          25 | 117.22%  | 119.78%            | -24.79% |     0.99 |       72 | 56.24%     | ok               |
|          20 | 117.05%  | 119.78%            | -22.81% |     0.98 |       76 | 59.73%     | ok               |
|          35 | 75.64%   | 119.78%            | -31.95% |     0.78 |       62 | 47.59%     | ok               |
|          30 | 71.80%   | 119.78%            | -29.47% |     0.76 |       72 | 52.08%     | ok               |

## OXY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 2.99%    | -3.92%             | -29.57% |     0.16 |       36 | 28.62%     | ok               |
|          30 | 0.50%    | -3.92%             | -31.01% |     0.13 |       71 | 44.26%     | ok               |
|          35 | 0.47%    | -3.92%             | -30.16% |     0.12 |       68 | 38.94%     | ok               |
|          40 | -1.69%   | -3.92%             | -31.66% |     0.07 |       54 | 34.78%     | ok               |
|          45 | -6.26%   | -3.92%             | -34.84% |    -0.03 |       42 | 30.45%     | ok               |

## PEP Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 8.79%    | -14.65%            | -11.62% |     0.41 |       44 | 27.95%     | ok               |
|          45 | -1.68%   | -14.65%            | -14.22% |    -0.02 |       66 | 32.78%     | ok               |
|          40 | -4.85%   | -14.65%            | -18.04% |    -0.13 |       78 | 37.94%     | ok               |
|          35 | -7.10%   | -14.65%            | -21.42% |    -0.17 |       89 | 42.60%     | ok               |
|          30 | -11.60%  | -14.65%            | -21.35% |    -0.29 |       83 | 48.42%     | ok               |

## PEPE-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -11.05%  | -80.89%            | -57.66% |     0.17 |       79 | 42.15%     | ok               |
|          35 | -17.01%  | -80.89%            | -51.35% |     0.06 |       64 | 36.97%     | ok               |
|          25 | -32.94%  | -80.89%            | -62.34% |    -0.06 |       89 | 47.70%     | ok               |
|          50 | -24.78%  | -80.89%            | -39.66% |    -0.13 |       50 | 21.84%     | ok               |
|          15 | -52.00%  | -80.89%            | -73.07% |    -0.19 |       86 | 58.05%     | ok               |

## PFE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -24.03%  | -11.16%            | -27.99% |    -0.84 |       52 | 21.30%     | ok               |
|          35 | -31.86%  | -11.16%            | -36.39% |    -1    |       82 | 33.61%     | ok               |
|          50 | -26.33%  | -11.16%            | -29.22% |    -1.03 |       44 | 17.47%     | ok               |
|          40 | -30.46%  | -11.16%            | -34.09% |    -1.04 |       76 | 26.12%     | ok               |
|          30 | -38.05%  | -11.16%            | -42.29% |    -1.18 |       77 | 37.27%     | ok               |

## PG Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -4.32%   | -2.62%             | -19.77% |    -0.14 |       56 | 33.94%     | ok               |
|          35 | -4.99%   | -2.62%             | -18.66% |    -0.16 |       60 | 37.77%     | ok               |
|          30 | -9.88%   | -2.62%             | -20.33% |    -0.36 |       61 | 40.43%     | ok               |
|          25 | -10.96%  | -2.62%             | -20.01% |    -0.4  |       71 | 41.60%     | ok               |
|          45 | -15.02%  | -2.62%             | -20.33% |    -0.68 |       56 | 30.95%     | ok               |

## PM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 3.94%    | 86.13%             | -31.89% |     0.18 |       89 | 61.90%     | ok               |
|          30 | 3.66%    | 86.13%             | -33.68% |     0.17 |       83 | 56.91%     | ok               |
|          35 | 2.43%    | 86.13%             | -32.20% |     0.15 |       86 | 53.24%     | ok               |
|          25 | -3.48%   | 86.13%             | -37.05% |     0.02 |       83 | 59.23%     | ok               |
|          50 | -3.76%   | 86.13%             | -35.70% |    -0.01 |       78 | 43.43%     | ok               |

## POL-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 47.17%   | -80.72%            | -46.45% |     0.65 |       80 | 47.32%     | ok               |
|          25 | 25.95%   | -80.72%            | -46.72% |     0.47 |       72 | 56.51%     | ok               |
|          20 | 24.45%   | -80.72%            | -52.88% |     0.46 |       80 | 62.07%     | ok               |
|          50 | 15.30%   | -80.72%            | -22.46% |     0.38 |       54 | 20.50%     | ok               |
|          15 | 1.71%    | -80.72%            | -58.42% |     0.27 |       77 | 68.58%     | ok               |

## QCOM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | 18.59%   | 83.59%             | -55.66% |     0.38 |       75 | 50.58%     | ok               |
|          20 | 17.48%   | 83.59%             | -57.05% |     0.37 |       72 | 53.41%     | ok               |
|          35 | 10.98%   | 83.59%             | -51.84% |     0.3  |       87 | 45.76%     | ok               |
|          15 | -2.05%   | 83.59%             | -60.40% |     0.15 |       76 | 56.57%     | ok               |
|          30 | -1.14%   | 83.59%             | -57.69% |     0.15 |       81 | 48.42%     | ok               |

## QQQ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | 28.36%   | 86.09%             | -12.88% |     0.74 |       57 | 48.92%     | ok               |
|          20 | 27.81%   | 86.09%             | -12.98% |     0.71 |       65 | 51.41%     | ok               |
|          15 | 27.72%   | 86.09%             | -14.17% |     0.68 |       65 | 54.08%     | ok               |
|          30 | 24.16%   | 86.09%             | -12.88% |     0.68 |       60 | 46.09%     | ok               |
|          35 | 11.47%   | 86.09%             | -19.00% |     0.39 |       66 | 42.43%     | ok               |

## RENDER-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 68.12%   | -49.83%            | -43.43% |     0.76 |       82 | 55.36%     | ok               |
|          15 | 48.60%   | -49.83%            | -44.59% |     0.66 |       82 | 58.58%     | ok               |
|          25 | 34.80%   | -49.83%            | -40.60% |     0.57 |       86 | 51.29%     | ok               |
|          30 | -7.47%   | -49.83%            | -45.00% |     0.22 |       94 | 44.64%     | ok               |
|          40 | -17.87%  | -49.83%            | -38.60% |     0.02 |       68 | 29.61%     | ok               |

## RTX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 26.40%   | 110.42%            | -18.66% |     0.66 |       76 | 57.24%     | ok               |
|          25 | 21.68%   | 110.42%            | -18.59% |     0.57 |       64 | 53.91%     | ok               |
|          50 | 15.99%   | 110.42%            | -18.42% |     0.53 |       60 | 42.26%     | ok               |
|          30 | 19.25%   | 110.42%            | -16.99% |     0.52 |       58 | 52.58%     | ok               |
|          35 | 16.66%   | 110.42%            | -18.00% |     0.52 |       54 | 50.58%     | ok               |

## SBUX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -14.68%  | 6.64%              | -23.55% |    -0.23 |       62 | 42.93%     | ok               |
|          45 | -16.40%  | 6.64%              | -27.26% |    -0.36 |       70 | 29.78%     | ok               |
|          40 | -19.36%  | 6.64%              | -27.13% |    -0.42 |       68 | 33.44%     | ok               |
|          30 | -23.57%  | 6.64%              | -31.15% |    -0.48 |       65 | 40.77%     | ok               |
|          20 | -26.43%  | 6.64%              | -34.48% |    -0.49 |       67 | 44.93%     | ok               |

## SCHW Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 2.81%    | 29.93%             | -15.92% |     0.15 |       52 | 33.11%     | ok               |
|          50 | -2.36%   | 29.93%             | -12.59% |    -0.02 |       48 | 30.78%     | ok               |
|          40 | -7.85%   | 29.93%             | -21.81% |    -0.15 |       60 | 36.11%     | ok               |
|          25 | -10.93%  | 29.93%             | -28.76% |    -0.18 |       63 | 48.09%     | ok               |
|          20 | -12.59%  | 29.93%             | -29.24% |    -0.22 |       71 | 50.75%     | ok               |

## SHIB-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -20.24%  | -74.52%            | -49.21% |     0.02 |       80 | 67.05%     | ok               |
|          25 | -29.64%  | -74.52%            | -43.85% |    -0.13 |       81 | 57.66%     | ok               |
|          20 | -31.55%  | -74.52%            | -48.69% |    -0.14 |       83 | 62.84%     | ok               |
|          30 | -40.41%  | -74.52%            | -48.95% |    -0.35 |       78 | 50.38%     | ok               |
|          40 | -37.16%  | -74.52%            | -53.38% |    -0.37 |       56 | 36.59%     | ok               |

## SHY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd    |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:-------|---------:|---------:|:-----------|:-----------------|
|          30 | -1.95%   | 0.50%              | -2.85% |    -0.66 |       50 | 37.27%     | ok               |
|          35 | -2.07%   | 0.50%              | -3.27% |    -0.7  |       52 | 35.44%     | ok               |
|          40 | -2.19%   | 0.50%              | -3.33% |    -0.75 |       52 | 33.61%     | ok               |
|          45 | -2.16%   | 0.50%              | -3.23% |    -0.76 |       50 | 30.45%     | ok               |
|          50 | -2.34%   | 0.50%              | -3.40% |    -0.86 |       46 | 27.62%     | ok               |

## SKY-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -29.93%  | 18.43%             | -43.98% |    -0.42 |       66 | 39.61%     | ok               |
|          25 | -33.53%  | 18.43%             | -48.09% |    -0.48 |       61 | 43.52%     | ok               |
|          15 | -39.94%  | 18.43%             | -56.39% |    -0.56 |       56 | 49.88%     | ok               |
|          20 | -44.61%  | 18.43%             | -58.40% |    -0.7  |       58 | 47.43%     | ok               |
|          35 | -40.38%  | 18.43%             | -49.68% |    -0.79 |       58 | 33.25%     | ok               |

## SLB Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 11.63%   | 5.19%              | -23.33% |     0.33 |       50 | 37.27%     | ok               |
|          45 | 6.27%    | 5.19%              | -20.73% |     0.23 |       56 | 33.78%     | ok               |
|          35 | -16.40%  | 5.19%              | -42.01% |    -0.23 |       78 | 45.26%     | ok               |
|          50 | -17.63%  | 5.19%              | -32.46% |    -0.36 |       58 | 29.95%     | ok               |
|          30 | -29.41%  | 5.19%              | -54.23% |    -0.51 |       77 | 51.91%     | ok               |

## SLV Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 67.27%   | 222.16%            | -29.75% |     0.86 |       60 | 36.27%     | ok               |
|          45 | 62.01%   | 222.16%            | -31.82% |     0.82 |       54 | 34.44%     | ok               |
|          50 | 57.25%   | 222.16%            | -34.10% |     0.78 |       52 | 33.61%     | ok               |
|          35 | 54.63%   | 222.16%            | -36.89% |     0.75 |       62 | 38.60%     | ok               |
|          30 | 36.93%   | 222.16%            | -42.66% |     0.58 |       58 | 40.60%     | ok               |

## SMH Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 118.98%  | 260.63%            | -30.17% |     1.33 |       49 | 54.74%     | ok               |
|          35 | 89.28%   | 260.63%            | -34.36% |     1.16 |       56 | 50.42%     | ok               |
|          25 | 89.14%   | 260.63%            | -32.94% |     1.14 |       48 | 53.41%     | ok               |
|          30 | 86.91%   | 260.63%            | -33.99% |     1.13 |       50 | 51.75%     | ok               |
|          15 | 86.04%   | 260.63%            | -32.34% |     1.06 |       57 | 56.74%     | ok               |

## SNX-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 29.67%   | -85.78%            | -28.28% |     0.51 |       68 | 30.84%     | ok               |
|          30 | 9.85%    | -85.78%            | -32.91% |     0.34 |       67 | 38.70%     | ok               |
|          20 | -6.18%   | -85.78%            | -43.20% |     0.22 |       76 | 50.19%     | ok               |
|          25 | -16.06%  | -85.78%            | -35.81% |     0.08 |       78 | 43.30%     | ok               |
|          40 | -15.66%  | -85.78%            | -33.19% |    -0.02 |       54 | 24.71%     | ok               |

## SOL-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -33.70%  | -55.24%            | -60.05% |    -0.19 |       66 | 37.55%     | ok               |
|          25 | -39.40%  | -55.24%            | -53.21% |    -0.2  |       74 | 55.94%     | ok               |
|          35 | -42.54%  | -55.24%            | -61.96% |    -0.29 |       74 | 45.21%     | ok               |
|          15 | -48.77%  | -55.24%            | -59.14% |    -0.32 |       80 | 64.18%     | ok               |
|          20 | -51.34%  | -55.24%            | -56.90% |    -0.39 |       72 | 58.62%     | ok               |

## SOXX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 96.02%   | 215.08%            | -38.67% |     1.14 |       55 | 53.58%     | ok               |
|          15 | 91.09%   | 215.08%            | -37.72% |     1.07 |       68 | 56.41%     | ok               |
|          25 | 86.20%   | 215.08%            | -39.85% |     1.07 |       53 | 53.08%     | ok               |
|          35 | 77.59%   | 215.08%            | -38.63% |     1.01 |       65 | 48.09%     | ok               |
|          30 | 75.74%   | 215.08%            | -40.34% |     0.98 |       57 | 50.92%     | ok               |

## SPY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 22.83%   | 61.67%             | -14.25% |     0.75 |       58 | 54.08%     | ok               |
|          15 | 22.03%   | 61.67%             | -16.80% |     0.72 |       63 | 56.91%     | ok               |
|          25 | 14.12%   | 61.67%             | -15.22% |     0.51 |       58 | 53.24%     | ok               |
|          30 | 10.00%   | 61.67%             | -16.47% |     0.4  |       60 | 50.75%     | ok               |
|          35 | 6.64%    | 61.67%             | -16.72% |     0.29 |       60 | 48.25%     | ok               |

## SUSHI-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -32.29%  | -84.92%            | -40.12% |    -0.33 |       52 | 14.94%     | ok               |
|          45 | -61.52%  | -84.92%            | -64.69% |    -0.83 |       52 | 17.62%     | ok               |
|          40 | -63.97%  | -84.92%            | -68.78% |    -0.84 |       61 | 24.33%     | ok               |
|          35 | -67.72%  | -84.92%            | -74.72% |    -0.91 |       77 | 29.31%     | ok               |
|          15 | -79.50%  | -84.92%            | -80.65% |    -0.99 |       87 | 47.13%     | ok               |

## T Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 32.11%   | 41.96%             | -18.13% |     0.75 |       61 | 53.91%     | ok               |
|          25 | 25.72%   | 41.96%             | -17.66% |     0.64 |       64 | 51.41%     | ok               |
|          15 | 24.90%   | 41.96%             | -15.08% |     0.61 |       70 | 57.74%     | ok               |
|          35 | 15.20%   | 41.96%             | -14.49% |     0.45 |       64 | 46.26%     | ok               |
|          30 | 14.38%   | 41.96%             | -17.01% |     0.42 |       64 | 49.42%     | ok               |

## TGT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -7.11%   | -9.72%             | -41.89% |    -0.03 |       81 | 47.09%     | ok               |
|          15 | -10.15%  | -9.72%             | -39.76% |    -0.08 |       71 | 51.58%     | ok               |
|          25 | -8.67%   | -9.72%             | -42.39% |    -0.08 |       63 | 41.93%     | ok               |
|          45 | -8.08%   | -9.72%             | -29.07% |    -0.11 |       52 | 29.12%     | ok               |
|          30 | -9.55%   | -9.72%             | -40.57% |    -0.11 |       58 | 39.27%     | ok               |

## TIA-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 68.01%   | -91.62%            | -31.67% |     0.77 |       56 | 29.50%     | ok               |
|          40 | 56.57%   | -91.62%            | -33.03% |     0.7  |       58 | 25.67%     | ok               |
|          45 | 36.17%   | -91.62%            | -34.08% |     0.57 |       56 | 19.16%     | ok               |
|          50 | 20.47%   | -91.62%            | -40.21% |     0.45 |       36 | 11.49%     | ok               |
|          15 | -7.32%   | -91.62%            | -42.16% |     0.25 |       95 | 50.77%     | ok               |

## TLT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -18.28%  | -10.94%            | -20.35% |    -1.65 |       60 | 22.30%     | ok               |
|          30 | -22.73%  | -10.94%            | -24.69% |    -1.65 |       70 | 33.44%     | ok               |
|          50 | -16.26%  | -10.94%            | -18.15% |    -1.78 |       36 | 15.14%     | ok               |
|          45 | -17.99%  | -10.94%            | -19.60% |    -1.81 |       42 | 17.97%     | ok               |
|          35 | -22.23%  | -10.94%            | -24.20% |    -1.82 |       68 | 27.45%     | ok               |

## TMO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 51.23%   | -7.29%             | -12.29% |     1.07 |       46 | 35.44%     | ok               |
|          40 | 49.15%   | -7.29%             | -12.07% |     1.02 |       51 | 40.43%     | ok               |
|          50 | 43.47%   | -7.29%             | -10.55% |     0.99 |       36 | 30.12%     | ok               |
|          35 | 35.24%   | -7.29%             | -16.12% |     0.77 |       63 | 45.26%     | ok               |
|          30 | 25.18%   | -7.29%             | -16.83% |     0.58 |       59 | 50.25%     | ok               |

## TMUS Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 21.16%   | 14.79%             | -26.87% |     0.51 |       67 | 60.90%     | ok               |
|          30 | 19.70%   | 14.79%             | -24.50% |     0.49 |       68 | 49.25%     | ok               |
|          20 | 13.72%   | 14.79%             | -24.82% |     0.38 |       69 | 55.24%     | ok               |
|          25 | 12.59%   | 14.79%             | -25.91% |     0.36 |       73 | 51.58%     | ok               |
|          50 | 8.75%    | 14.79%             | -18.84% |     0.31 |       58 | 37.10%     | ok               |

## TRX-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -2.64%   | 35.80%             | -22.90% |     0.03 |       70 | 49.23%     | ok               |
|          35 | -3.97%   | 35.80%             | -21.77% |    -0.01 |       66 | 46.55%     | ok               |
|          25 | -4.39%   | 35.80%             | -26.84% |    -0.02 |       66 | 52.49%     | ok               |
|          40 | -3.78%   | 35.80%             | -22.27% |    -0.02 |       52 | 38.51%     | ok               |
|          50 | -6.77%   | 35.80%             | -21.14% |    -0.13 |       46 | 33.14%     | ok               |

## TSLA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 102.30%  | 83.50%             | -32.60% |     1.04 |       64 | 31.78%     | ok               |
|          40 | 92.11%   | 83.50%             | -45.90% |     0.91 |       61 | 36.27%     | ok               |
|          45 | 62.75%   | 83.50%             | -46.86% |     0.73 |       65 | 33.61%     | ok               |
|          35 | 39.42%   | 83.50%             | -54.51% |     0.55 |       74 | 39.43%     | ok               |
|          30 | 13.21%   | 83.50%             | -57.89% |     0.34 |       68 | 43.93%     | ok               |

## TXN Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 14.50%   | 85.15%             | -45.45% |     0.35 |       70 | 35.44%     | ok               |
|          20 | 5.78%    | 85.15%             | -38.98% |     0.23 |       66 | 60.07%     | ok               |
|          40 | 5.93%    | 85.15%             | -45.67% |     0.22 |       74 | 47.59%     | ok               |
|          35 | 5.71%    | 85.15%             | -43.38% |     0.22 |       78 | 49.92%     | ok               |
|          15 | 4.71%    | 85.15%             | -39.48% |     0.22 |       69 | 63.73%     | ok               |

## UNH Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 23.45%   | -29.23%            | -37.02% |     0.47 |       52 | 29.12%     | ok               |
|          30 | 15.34%   | -29.23%            | -32.80% |     0.35 |       78 | 52.25%     | ok               |
|          35 | 11.93%   | -29.23%            | -34.05% |     0.31 |       70 | 47.25%     | ok               |
|          15 | 10.28%   | -29.23%            | -36.80% |     0.29 |       77 | 67.05%     | ok               |
|          40 | 7.82%    | -29.23%            | -39.28% |     0.26 |       66 | 41.43%     | ok               |

## UNI-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -18.74%  | -77.35%            | -57.12% |    -0    |       54 | 23.75%     | ok               |
|          50 | -23.75%  | -77.35%            | -55.74% |    -0.1  |       50 | 20.31%     | ok               |
|          40 | -31.27%  | -77.35%            | -63.75% |    -0.16 |       58 | 28.74%     | ok               |
|          35 | -41.14%  | -77.35%            | -69.40% |    -0.26 |       74 | 33.52%     | ok               |
|          20 | -73.91%  | -77.35%            | -80.81% |    -0.8  |      101 | 50.00%     | ok               |

## UPS Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -35.01%  | -32.78%            | -42.25% |    -0.69 |       74 | 42.43%     | ok               |
|          35 | -33.93%  | -32.78%            | -40.47% |    -0.7  |       59 | 32.11%     | ok               |
|          20 | -36.10%  | -32.78%            | -45.77% |    -0.7  |       80 | 45.59%     | ok               |
|          30 | -36.35%  | -32.78%            | -40.62% |    -0.75 |       66 | 37.77%     | ok               |
|          40 | -35.24%  | -32.78%            | -42.12% |    -0.76 |       51 | 26.96%     | ok               |

## USO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 8.31%    | 87.01%             | -35.12% |     0.26 |       50 | 26.79%     | ok               |
|          30 | 2.80%    | 87.01%             | -43.35% |     0.17 |       68 | 34.44%     | ok               |
|          25 | 1.57%    | 87.01%             | -43.43% |     0.16 |       70 | 37.44%     | ok               |
|          20 | 0.27%    | 87.01%             | -44.16% |     0.14 |       74 | 39.43%     | ok               |
|          40 | -1.01%   | 87.01%             | -41.14% |     0.11 |       61 | 29.62%     | ok               |

## VEA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 4.85%    | 52.28%             | -17.55% |     0.23 |       64 | 50.42%     | ok               |
|          20 | 1.26%    | 52.28%             | -18.44% |     0.1  |       63 | 47.92%     | ok               |
|          25 | -2.41%   | 52.28%             | -19.11% |    -0.04 |       59 | 45.92%     | ok               |
|          30 | -2.87%   | 52.28%             | -19.49% |    -0.07 |       60 | 43.43%     | ok               |
|          35 | -4.16%   | 52.28%             | -18.54% |    -0.12 |       56 | 42.26%     | ok               |

## VIXY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -46.17%  | -62.44%            | -68.69% |    -0.39 |       44 | 10.32%     | ok               |
|          45 | -53.84%  | -62.44%            | -74.12% |    -0.51 |       54 | 15.47%     | ok               |
|          40 | -63.34%  | -62.44%            | -79.44% |    -0.64 |       68 | 19.47%     | ok               |
|          35 | -67.18%  | -62.44%            | -83.87% |    -0.68 |       84 | 24.63%     | ok               |
|          15 | -77.08%  | -62.44%            | -89.47% |    -0.79 |       97 | 41.93%     | ok               |

## VNQ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -8.60%   | 10.50%             | -19.07% |    -0.37 |       60 | 28.62%     | ok               |
|          50 | -9.03%   | 10.50%             | -17.13% |    -0.41 |       56 | 26.12%     | ok               |
|          25 | -15.75%  | 10.50%             | -22.16% |    -0.61 |       76 | 41.76%     | ok               |
|          40 | -14.13%  | 10.50%             | -24.84% |    -0.62 |       74 | 32.11%     | ok               |
|          15 | -19.94%  | 10.50%             | -24.74% |    -0.77 |       78 | 46.59%     | ok               |

## VTI Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 19.36%   | 59.81%             | -13.96% |     0.65 |       62 | 55.74%     | ok               |
|          15 | 15.88%   | 59.81%             | -15.70% |     0.54 |       65 | 58.57%     | ok               |
|          25 | 8.13%    | 59.81%             | -16.10% |     0.33 |       60 | 54.08%     | ok               |
|          30 | 0.58%    | 59.81%             | -18.77% |     0.08 |       70 | 52.08%     | ok               |
|          35 | -1.96%   | 59.81%             | -21.19% |    -0.01 |       64 | 48.92%     | ok               |

## VWO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -7.30%   | 47.89%             | -21.18% |    -0.25 |       60 | 32.61%     | ok               |
|          15 | -9.03%   | 47.89%             | -24.01% |    -0.26 |       69 | 49.42%     | ok               |
|          20 | -10.06%  | 47.89%             | -26.14% |    -0.31 |       67 | 47.25%     | ok               |
|          40 | -8.98%   | 47.89%             | -23.57% |    -0.31 |       70 | 37.94%     | ok               |
|          45 | -9.11%   | 47.89%             | -23.26% |    -0.33 |       62 | 35.11%     | ok               |

## VZ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -2.86%   | 18.93%             | -16.98% |    -0.03 |       52 | 27.62%     | ok               |
|          45 | -9.56%   | 18.93%             | -20.38% |    -0.25 |       58 | 30.45%     | ok               |
|          35 | -13.38%  | 18.93%             | -24.68% |    -0.36 |       59 | 36.11%     | ok               |
|          25 | -16.62%  | 18.93%             | -28.84% |    -0.43 |       76 | 43.93%     | ok               |
|          40 | -17.86%  | 18.93%             | -26.72% |    -0.54 |       64 | 32.95%     | ok               |

## WFC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -2.27%   | 55.33%             | -18.29% |    -0.01 |       54 | 31.61%     | ok               |
|          35 | -10.82%  | 55.33%             | -23.06% |    -0.17 |       79 | 44.26%     | ok               |
|          45 | -9.25%   | 55.33%             | -23.40% |    -0.21 |       64 | 36.27%     | ok               |
|          20 | -20.25%  | 55.33%             | -28.08% |    -0.32 |       79 | 53.24%     | ok               |
|          40 | -15.89%  | 55.33%             | -24.26% |    -0.41 |       76 | 40.10%     | ok               |

## WIF-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 29.23%   | -89.43%            | -40.67% |     0.5  |       69 | 38.12%     | ok               |
|          15 | 27.02%   | -89.43%            | -46.21% |     0.49 |       76 | 41.00%     | ok               |
|          25 | -5.04%   | -89.43%            | -45.19% |     0.25 |       73 | 35.25%     | ok               |
|          50 | -3.56%   | -89.43%            | -31.17% |     0.11 |       32 | 10.92%     | ok               |
|          45 | -16.27%  | -89.43%            | -44.01% |    -0.06 |       40 | 13.22%     | ok               |

## WMT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 64.57%   | 121.59%            | -9.85%  |     1.63 |       34 | 45.92%     | ok               |
|          50 | 54.40%   | 121.59%            | -12.19% |     1.51 |       32 | 43.59%     | ok               |
|          35 | 60.43%   | 121.59%            | -9.90%  |     1.5  |       46 | 50.58%     | ok               |
|          40 | 57.57%   | 121.59%            | -9.99%  |     1.48 |       38 | 46.76%     | ok               |
|          30 | 38.75%   | 121.59%            | -21.31% |     0.99 |       53 | 53.24%     | ok               |

## XBI Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 0.61%    | 53.07%             | -16.71% |     0.1  |       62 | 35.11%     | ok               |
|          45 | -0.16%   | 53.07%             | -16.88% |     0.08 |       54 | 31.95%     | ok               |
|          35 | -1.80%   | 53.07%             | -20.11% |     0.04 |       64 | 38.60%     | ok               |
|          30 | -3.68%   | 53.07%             | -20.48% |    -0    |       64 | 40.43%     | ok               |
|          50 | -6.10%   | 53.07%             | -16.83% |    -0.1  |       56 | 28.62%     | ok               |

## XLB Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 0.40%    | 21.29%             | -17.59% |     0.07 |       42 | 27.29%     | ok               |
|          40 | -1.80%   | 21.29%             | -19.67% |    -0.01 |       56 | 31.61%     | ok               |
|          45 | -2.15%   | 21.29%             | -19.78% |    -0.03 |       44 | 28.45%     | ok               |
|          35 | -5.03%   | 21.29%             | -22.65% |    -0.13 |       58 | 34.94%     | ok               |
|          25 | -10.74%  | 21.29%             | -23.63% |    -0.34 |       67 | 41.43%     | ok               |

## XLC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 21.96%   | 60.59%             | -12.33% |     0.71 |       63 | 57.24%     | ok               |
|          25 | 19.67%   | 60.59%             | -12.31% |     0.64 |       60 | 59.07%     | ok               |
|          40 | 15.87%   | 60.59%             | -13.38% |     0.58 |       66 | 49.92%     | ok               |
|          35 | 15.84%   | 60.59%             | -13.38% |     0.57 |       62 | 54.41%     | ok               |
|          20 | 11.25%   | 60.59%             | -13.37% |     0.39 |       68 | 61.73%     | ok               |

## XLE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -0.94%   | 32.95%             | -25.98% |     0.05 |       60 | 37.10%     | ok               |
|          35 | -3.18%   | 32.95%             | -31.51% |     0    |       71 | 44.59%     | ok               |
|          45 | -3.24%   | 32.95%             | -29.68% |    -0.02 |       64 | 39.60%     | ok               |
|          25 | -9.60%   | 32.95%             | -36.05% |    -0.16 |       89 | 50.08%     | ok               |
|          40 | -10.37%  | 32.95%             | -34.51% |    -0.22 |       70 | 42.26%     | ok               |

## XLF Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -3.21%   | 36.64%             | -18.01% |    -0.05 |       68 | 56.24%     | ok               |
|          15 | -7.22%   | 36.64%             | -19.58% |    -0.18 |       76 | 59.07%     | ok               |
|          25 | -11.33%  | 36.64%             | -23.22% |    -0.36 |       77 | 52.58%     | ok               |
|          30 | -11.55%  | 36.64%             | -23.61% |    -0.38 |       76 | 49.92%     | ok               |
|          35 | -18.65%  | 36.64%             | -27.06% |    -0.74 |       66 | 45.76%     | ok               |

## XLI Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 13.87%   | 55.37%             | -10.36% |     0.51 |       72 | 56.07%     | ok               |
|          20 | 7.98%    | 55.37%             | -12.74% |     0.34 |       65 | 50.58%     | ok               |
|          50 | 6.69%    | 55.37%             | -9.25%  |     0.34 |       58 | 35.77%     | ok               |
|          45 | 6.38%    | 55.37%             | -12.27% |     0.32 |       66 | 38.44%     | ok               |
|          30 | 5.61%    | 55.37%             | -11.38% |     0.27 |       66 | 48.09%     | ok               |

## XLK Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 107.55%  | 107.50%            | -14.75% |     1.64 |       41 | 54.08%     | ok               |
|          20 | 93.70%   | 107.50%            | -14.75% |     1.53 |       46 | 51.91%     | ok               |
|          25 | 85.41%   | 107.50%            | -14.75% |     1.49 |       40 | 49.92%     | ok               |
|          30 | 77.76%   | 107.50%            | -14.75% |     1.43 |       42 | 48.59%     | ok               |
|          35 | 58.22%   | 107.50%            | -16.03% |     1.19 |       52 | 45.92%     | ok               |

## XLM-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 68.98%   | -26.13%            | -31.45% |     0.81 |       50 | 32.95%     | ok               |
|          50 | 64.26%   | -26.13%            | -25.31% |     0.79 |       46 | 29.12%     | ok               |
|          30 | 38.97%   | -26.13%            | -40.13% |     0.57 |       69 | 47.13%     | ok               |
|          40 | 30.96%   | -26.13%            | -33.96% |     0.51 |       49 | 37.16%     | ok               |
|          35 | 28.49%   | -26.13%            | -39.41% |     0.49 |       69 | 43.30%     | ok               |

## XLP Threshold Sweep

|   threshold | return   | benchmark_return   | mdd    |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:-------|---------:|---------:|:-----------|:-----------------|
|          40 | 11.77%   | 15.14%             | -7.32% |     0.69 |       72 | 39.43%     | ok               |
|          45 | 11.31%   | 15.14%             | -5.66% |     0.69 |       58 | 34.94%     | ok               |
|          35 | 10.80%   | 15.14%             | -8.39% |     0.63 |       68 | 42.43%     | ok               |
|          50 | 7.83%    | 15.14%             | -6.08% |     0.5  |       60 | 32.95%     | ok               |
|          30 | 8.49%    | 15.14%             | -8.96% |     0.5  |       72 | 44.26%     | ok               |

## XLU Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 7.31%    | 37.67%             | -8.58%  |     0.39 |       48 | 31.28%     | ok               |
|          50 | 7.26%    | 37.67%             | -8.47%  |     0.39 |       48 | 30.62%     | ok               |
|          40 | 4.54%    | 37.67%             | -8.58%  |     0.26 |       56 | 32.45%     | ok               |
|          35 | -2.39%   | 37.67%             | -13.87% |    -0.07 |       62 | 35.11%     | ok               |
|          30 | -4.20%   | 37.67%             | -13.66% |    -0.15 |       67 | 38.27%     | ok               |

## XLV Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -8.65%   | 7.44%              | -14.71% |    -0.4  |       66 | 37.77%     | ok               |
|          25 | -11.37%  | 7.44%              | -17.25% |    -0.54 |       70 | 39.60%     | ok               |
|          45 | -11.82%  | 7.44%              | -16.50% |    -0.69 |       54 | 27.45%     | ok               |
|          50 | -11.88%  | 7.44%              | -15.90% |    -0.71 |       52 | 25.12%     | ok               |
|          15 | -15.39%  | 7.44%              | -20.69% |    -0.73 |       83 | 44.43%     | ok               |

## XLY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 2.94%    | 40.04%             | -12.94% |     0.16 |       74 | 41.43%     | ok               |
|          30 | -1.30%   | 40.04%             | -14.01% |     0.03 |       78 | 44.76%     | ok               |
|          50 | -0.91%   | 40.04%             | -13.71% |     0.02 |       50 | 29.78%     | ok               |
|          15 | -2.54%   | 40.04%             | -15.77% |     0.01 |       81 | 53.41%     | ok               |
|          45 | -1.70%   | 40.04%             | -13.71% |    -0.01 |       52 | 32.28%     | ok               |

## XOM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 1.96%    | 41.54%             | -21.35% |     0.13 |       40 | 29.28%     | ok               |
|          40 | 0.98%    | 41.54%             | -21.45% |     0.1  |       48 | 33.28%     | ok               |
|          25 | -0.20%   | 41.54%             | -19.90% |     0.07 |       61 | 38.10%     | ok               |
|          30 | -0.77%   | 41.54%             | -20.29% |     0.05 |       61 | 36.77%     | ok               |
|          35 | -1.46%   | 41.54%             | -20.93% |     0.03 |       60 | 35.27%     | ok               |

## XRP-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | -40.36%  | -38.03%            | -55.83% |    -0.41 |       74 | 40.80%     | ok               |
|          40 | -45.45%  | -38.03%            | -54.34% |    -0.57 |       64 | 34.87%     | ok               |
|          30 | -51.55%  | -38.03%            | -63.50% |    -0.63 |       78 | 45.21%     | ok               |
|          50 | -43.13%  | -38.03%            | -46.41% |    -0.63 |       64 | 23.56%     | ok               |
|          45 | -53.71%  | -38.03%            | -56.00% |    -0.79 |       62 | 30.27%     | ok               |

## YFI-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -45.19%  | -72.77%            | -50.17% |    -0.85 |       62 | 24.90%     | ok               |
|          45 | -46.71%  | -72.77%            | -51.92% |    -0.98 |       58 | 20.88%     | ok               |
|          30 | -60.30%  | -72.77%            | -67.78% |    -1.06 |       85 | 38.51%     | ok               |
|          50 | -46.82%  | -72.77%            | -51.80% |    -1.07 |       50 | 17.05%     | ok               |
|          35 | -61.00%  | -72.77%            | -64.34% |    -1.17 |       75 | 32.38%     | ok               |

## ZEC-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 124.17%  | 836.35%            | -24.66% |     0.9  |       50 | 23.18%     | ok               |
|          35 | 90.22%   | 836.35%            | -43.54% |     0.76 |       58 | 30.84%     | ok               |
|          25 | 76.78%   | 836.35%            | -46.61% |     0.7  |       59 | 39.66%     | ok               |
|          50 | 54.10%   | 836.35%            | -37.94% |     0.6  |       52 | 20.69%     | ok               |
|          30 | 46.51%   | 836.35%            | -46.93% |     0.57 |       67 | 36.40%     | ok               |
