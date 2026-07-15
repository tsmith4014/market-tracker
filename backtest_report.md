# Market Tracker Backtest Report

_Generated: 2026-07-15T03:40:55+00:00_

## Data Sources

- Crypto: Kraken -> Coinbase -> CoinGecko OHLC -> CoinPaprika fallback chain.
- Stocks / ETFs / indices: Stooq -> Yahoo Finance fallback chain.
- Data rows are generated from real market APIs. Mock OHLCV rows are not generated.

## Data Freshness

- Rows: **92,501**
- Symbols: **161**
- Date range: **2024-02-20** to **2026-07-15**

## Latest Signals

| symbol     | date                |         close |   composite_score | signal   | data_source   |
|:-----------|:--------------------|--------------:|------------------:|:---------|:--------------|
| AAPL       | 2026-07-14 00:00:00 |   314.86      |         54.0833   | LONG     | Yahoo Finance |
| AAVE-USD   | 2026-07-15 00:00:00 |    98.59      |         40        | LONG     | Kraken API    |
| ABBV       | 2026-07-14 00:00:00 |   244.78      |         42.5833   | LONG     | Yahoo Finance |
| AMZN       | 2026-07-14 00:00:00 |   247.49      |         65.6667   | LONG     | Yahoo Finance |
| ARB-USD    | 2026-07-15 00:00:00 |     0.0909    |         43.3333   | LONG     | Kraken API    |
| BAC        | 2026-07-14 00:00:00 |    60.62      |         51.5833   | LONG     | Yahoo Finance |
| COP        | 2026-07-14 00:00:00 |   111.87      |         51.1667   | LONG     | Yahoo Finance |
| CVX        | 2026-07-14 00:00:00 |   181.76      |         71.1667   | LONG     | Yahoo Finance |
| DBC        | 2026-07-14 00:00:00 |    28.63      |         69.9167   | LONG     | Yahoo Finance |
| DIA        | 2026-07-14 00:00:00 |   524.69      |         43.0833   | LONG     | Yahoo Finance |
| EOG        | 2026-07-14 00:00:00 |   138.01      |         72.0833   | LONG     | Yahoo Finance |
| ETH-USD    | 2026-07-15 00:00:00 |  1868.58      |         50        | LONG     | Kraken API    |
| JNJ        | 2026-07-14 00:00:00 |   253.85      |         42.5833   | LONG     | Yahoo Finance |
| JPM        | 2026-07-14 00:00:00 |   342.89      |         30.75     | LONG     | Yahoo Finance |
| LDO-USD    | 2026-07-15 00:00:00 |     0.328     |         47        | LONG     | Kraken API    |
| META       | 2026-07-14 00:00:00 |   661.04      |         61.0833   | LONG     | Yahoo Finance |
| MPC        | 2026-07-14 00:00:00 |   303.4       |         69.25     | LONG     | Yahoo Finance |
| MRK        | 2026-07-14 00:00:00 |   120.78      |         39.0833   | LONG     | Yahoo Finance |
| NVDA       | 2026-07-14 00:00:00 |   211.8       |         49.9167   | LONG     | Yahoo Finance |
| OXY        | 2026-07-14 00:00:00 |    54.57      |         71.1667   | LONG     | Yahoo Finance |
| POL-USD    | 2026-07-15 00:00:00 |     0.08458   |         49        | LONG     | Kraken API    |
| RTX        | 2026-07-14 00:00:00 |   193.39      |         61.3333   | LONG     | Yahoo Finance |
| SBUX       | 2026-07-14 00:00:00 |   106.17      |         67.0833   | LONG     | Yahoo Finance |
| SCHW       | 2026-07-14 00:00:00 |   101.1       |         60.9167   | LONG     | Yahoo Finance |
| SKY-USD    | 2026-07-15 00:00:00 |     0.06135   |         32.3333   | LONG     | Kraken API    |
| SPY        | 2026-07-14 00:00:00 |   751.83      |         52.5833   | LONG     | Yahoo Finance |
| TMO        | 2026-07-14 00:00:00 |   534.07      |         65.5      | LONG     | Yahoo Finance |
| UNH        | 2026-07-14 00:00:00 |   425.19      |         53.25     | LONG     | Yahoo Finance |
| UNI-USD    | 2026-07-15 00:00:00 |     3.6604    |         47        | LONG     | Kraken API    |
| USO        | 2026-07-14 00:00:00 |   120.17      |         74.6667   | LONG     | Yahoo Finance |
| WFC        | 2026-07-14 00:00:00 |    85.29      |         40.8333   | LONG     | Yahoo Finance |
| XBI        | 2026-07-14 00:00:00 |   155.45      |         56.5833   | LONG     | Yahoo Finance |
| XLE        | 2026-07-14 00:00:00 |    56.95      |         69.4167   | LONG     | Yahoo Finance |
| XLF        | 2026-07-14 00:00:00 |    56.18      |         62.0833   | LONG     | Yahoo Finance |
| XLU        | 2026-07-14 00:00:00 |    45.69      |         53.4167   | LONG     | Yahoo Finance |
| XLV        | 2026-07-14 00:00:00 |   158.29      |         44.5833   | LONG     | Yahoo Finance |
| XOM        | 2026-07-14 00:00:00 |   145.09      |         71.1667   | LONG     | Yahoo Finance |
| YFI-USD    | 2026-07-15 00:00:00 |  2122.3       |         44.9167   | LONG     | Kraken API    |
| ZEC-USD    | 2026-07-15 00:00:00 |   555.17      |         67.8333   | LONG     | Kraken API    |
| ADA-USD    | 2026-07-15 00:00:00 |     0.163291  |          2.5      | NEUTRAL  | Kraken API    |
| ADBE       | 2026-07-14 00:00:00 |   220.78      |         -1.41667  | NEUTRAL  | Yahoo Finance |
| ALGO-USD   | 2026-07-15 00:00:00 |     0.08433   |        -23.25     | NEUTRAL  | Kraken API    |
| AMAT       | 2026-07-14 00:00:00 |   595.7       |         33.5      | NEUTRAL  | Yahoo Finance |
| AMD        | 2026-07-14 00:00:00 |   548.13      |         36.8333   | NEUTRAL  | Yahoo Finance |
| AMGN       | 2026-07-14 00:00:00 |   355.25      |         13.3333   | NEUTRAL  | Yahoo Finance |
| APT-USD    | 2026-07-15 00:00:00 |     0.6215    |         -8.75     | NEUTRAL  | Kraken API    |
| ARKK       | 2026-07-14 00:00:00 |    79.52      |          9.33333  | NEUTRAL  | Yahoo Finance |
| ATOM-USD   | 2026-07-15 00:00:00 |     1.5652    |         -8.33333  | NEUTRAL  | Kraken API    |
| AVAX-USD   | 2026-07-15 00:00:00 |     6.626     |        -13.1667   | NEUTRAL  | Kraken API    |
| AVGO       | 2026-07-14 00:00:00 |   389.11      |         27.6667   | NEUTRAL  | Yahoo Finance |
| BA         | 2026-07-14 00:00:00 |   217.11      |        -46.0833   | NEUTRAL  | Yahoo Finance |
| BCH-USD    | 2026-07-15 00:00:00 |   231.96      |         11        | NEUTRAL  | Kraken API    |
| BITO       | 2026-07-14 00:00:00 |     8.75      |         -2.83333  | NEUTRAL  | Yahoo Finance |
| BLK        | 2026-07-14 00:00:00 |  1025.44      |          5.41667  | NEUTRAL  | Yahoo Finance |
| BONK-USD   | 2026-07-15 00:00:00 |     3.76e-06  |        -52.9167   | NEUTRAL  | Kraken API    |
| BTC-USD    | 2026-07-15 00:00:00 | 64564.9       |         25.0833   | NEUTRAL  | Kraken API    |
| C          | 2026-07-14 00:00:00 |   133.27      |         -3.83333  | NEUTRAL  | Yahoo Finance |
| CAT        | 2026-07-14 00:00:00 |   933.34      |         -3.83333  | NEUTRAL  | Yahoo Finance |
| CL         | 2026-07-14 00:00:00 |    91.03      |         23.4167   | NEUTRAL  | Yahoo Finance |
| CMCSA      | 2026-07-14 00:00:00 |    23.19      |          5.75     | NEUTRAL  | Yahoo Finance |
| COMP-USD   | 2026-07-15 00:00:00 |    16.94      |         29.6667   | NEUTRAL  | Kraken API    |
| COST       | 2026-07-14 00:00:00 |   921.75      |        -53.8333   | NEUTRAL  | Yahoo Finance |
| CRM        | 2026-07-14 00:00:00 |   167.56      |          2.41667  | NEUTRAL  | Yahoo Finance |
| CRV-USD    | 2026-07-15 00:00:00 |     0.22764   |         37.75     | NEUTRAL  | Kraken API    |
| CSCO       | 2026-07-14 00:00:00 |   117.09      |         11.9167   | NEUTRAL  | Yahoo Finance |
| DASH-USD   | 2026-07-15 00:00:00 |    34.388     |        -21.25     | NEUTRAL  | Kraken API    |
| DE         | 2026-07-14 00:00:00 |   584.4       |          9.66667  | NEUTRAL  | Yahoo Finance |
| DIS        | 2026-07-14 00:00:00 |    95.87      |        -72.3333   | NEUTRAL  | Yahoo Finance |
| DOGE-USD   | 2026-07-15 00:00:00 |     0.0738706 |         -0.833333 | NEUTRAL  | Kraken API    |
| DOT-USD    | 2026-07-15 00:00:00 |     0.8513    |         11.6667   | NEUTRAL  | Kraken API    |
| DXY-INDEX  | 2026-07-14 00:00:00 |   100.829     |         45.9677   | NEUTRAL  | Yahoo Finance |
| EEM        | 2026-07-14 00:00:00 |    65.67      |         -9.75     | NEUTRAL  | Yahoo Finance |
| EFA        | 2026-07-14 00:00:00 |   103.96      |         36        | NEUTRAL  | Yahoo Finance |
| ETC-USD    | 2026-07-15 00:00:00 |     7.019     |         -1.25     | NEUTRAL  | Kraken API    |
| EWJ        | 2026-07-14 00:00:00 |    93.89      |         41.3333   | NEUTRAL  | Yahoo Finance |
| FCX        | 2026-07-14 00:00:00 |    61.95      |         -8.08333  | NEUTRAL  | Yahoo Finance |
| FET-USD    | 2026-07-15 00:00:00 |     0.1608    |        -29.3333   | NEUTRAL  | Kraken API    |
| FIL-USD    | 2026-07-15 00:00:00 |     0.782     |         16.75     | NEUTRAL  | Kraken API    |
| FXI        | 2026-07-14 00:00:00 |    33.77      |          6.91667  | NEUTRAL  | Yahoo Finance |
| GDX        | 2026-07-14 00:00:00 |    74.88      |        -48.1667   | NEUTRAL  | Yahoo Finance |
| GDXJ       | 2026-07-14 00:00:00 |    98.37      |        -48.1667   | NEUTRAL  | Yahoo Finance |
| GE         | 2026-07-14 00:00:00 |   353.73      |          5.91667  | NEUTRAL  | Yahoo Finance |
| GOOGL      | 2026-07-14 00:00:00 |   359.51      |         38.6667   | NEUTRAL  | Yahoo Finance |
| GRT-USD    | 2026-07-15 00:00:00 |     0.01782   |        -19.5833   | NEUTRAL  | Kraken API    |
| GS         | 2026-07-14 00:00:00 |  1140         |         66.8333   | NEUTRAL  | Yahoo Finance |
| HD         | 2026-07-14 00:00:00 |   337.74      |         -9        | NEUTRAL  | Yahoo Finance |
| HON        | 2026-07-14 00:00:00 |   222.68      |        -39.5      | NEUTRAL  | Yahoo Finance |
| HYG        | 2026-07-14 00:00:00 |    79.68      |        -52.5833   | NEUTRAL  | Yahoo Finance |
| IBIT       | 2026-07-14 00:00:00 |    36.58      |         -6.33333  | NEUTRAL  | Yahoo Finance |
| ICP-USD    | 2026-07-15 00:00:00 |     2.19      |        -23.25     | NEUTRAL  | Kraken API    |
| IEF        | 2026-07-14 00:00:00 |    93.55      |        -58        | NEUTRAL  | Yahoo Finance |
| IEMG       | 2026-07-14 00:00:00 |    79.72      |         -9.75     | NEUTRAL  | Yahoo Finance |
| INJ-USD    | 2026-07-15 00:00:00 |     4.986     |         29.1667   | NEUTRAL  | Kraken API    |
| INTC       | 2026-07-14 00:00:00 |   107.76      |        -34        | NEUTRAL  | Yahoo Finance |
| INTU       | 2026-07-14 00:00:00 |   282.43      |         -8.83333  | NEUTRAL  | Yahoo Finance |
| ITA        | 2026-07-14 00:00:00 |   235.27      |          7.91667  | NEUTRAL  | Yahoo Finance |
| IWM        | 2026-07-14 00:00:00 |   294.51      |          3.83333  | NEUTRAL  | Yahoo Finance |
| KO         | 2026-07-14 00:00:00 |    83.08      |         58.6667   | NEUTRAL  | Yahoo Finance |
| LIN        | 2026-07-14 00:00:00 |   522.54      |         30        | NEUTRAL  | Yahoo Finance |
| LINK-USD   | 2026-07-15 00:00:00 |     8.28687   |         39.75     | NEUTRAL  | Kraken API    |
| LLY        | 2026-07-14 00:00:00 |  1152.54      |         11.5      | NEUTRAL  | Yahoo Finance |
| LRCX       | 2026-07-14 00:00:00 |   346.1       |          8.83333  | NEUTRAL  | Yahoo Finance |
| LTC-USD    | 2026-07-15 00:00:00 |    44.82      |         28        | NEUTRAL  | Kraken API    |
| MCD        | 2026-07-14 00:00:00 |   268.94      |        -30.1667   | NEUTRAL  | Yahoo Finance |
| MS         | 2026-07-14 00:00:00 |   227.67      |         61.8333   | NEUTRAL  | Yahoo Finance |
| MSFT       | 2026-07-14 00:00:00 |   384.93      |        -16.0833   | NEUTRAL  | Yahoo Finance |
| MU         | 2026-07-14 00:00:00 |   983.12      |         -7.66667  | NEUTRAL  | Yahoo Finance |
| NEAR-USD   | 2026-07-15 00:00:00 |     2.0181    |         56.1667   | NEUTRAL  | Kraken API    |
| NEM        | 2026-07-14 00:00:00 |    94.75      |        -48.1667   | NEUTRAL  | Yahoo Finance |
| NFLX       | 2026-07-14 00:00:00 |    73.53      |        -26.5833   | NEUTRAL  | Yahoo Finance |
| NKE        | 2026-07-14 00:00:00 |    42.86      |        -27.5833   | NEUTRAL  | Yahoo Finance |
| NOW        | 2026-07-14 00:00:00 |   104.85      |         15.6667   | NEUTRAL  | Yahoo Finance |
| OP-USD     | 2026-07-15 00:00:00 |     0.1016    |         -5.08333  | NEUTRAL  | Kraken API    |
| PEP        | 2026-07-14 00:00:00 |   135.45      |        -67.8333   | NEUTRAL  | Yahoo Finance |
| PEPE-USD   | 2026-07-15 00:00:00 |     2.789e-06 |         20.3333   | NEUTRAL  | Kraken API    |
| PG         | 2026-07-14 00:00:00 |   146.08      |        -40.3333   | NEUTRAL  | Yahoo Finance |
| PM         | 2026-07-14 00:00:00 |   175.95      |         -5.83333  | NEUTRAL  | Yahoo Finance |
| QCOM       | 2026-07-14 00:00:00 |   178.1       |        -27.5833   | NEUTRAL  | Yahoo Finance |
| QQQ        | 2026-07-14 00:00:00 |   719.71      |         28.3333   | NEUTRAL  | Yahoo Finance |
| RENDER-USD | 2026-07-15 00:00:00 |     1.531     |        -19.5833   | NEUTRAL  | Kraken API    |
| SHIB-USD   | 2026-07-15 00:00:00 |     4.211e-06 |        -18.9167   | NEUTRAL  | Kraken API    |
| SHY        | 2026-07-14 00:00:00 |    81.93      |        -50.75     | NEUTRAL  | Yahoo Finance |
| SLB        | 2026-07-14 00:00:00 |    47.54      |         23        | NEUTRAL  | Yahoo Finance |
| SMH        | 2026-07-14 00:00:00 |   600.31      |          0.333333 | NEUTRAL  | Yahoo Finance |
| SNX-USD    | 2026-07-15 00:00:00 |     0.2368    |         16.4167   | NEUTRAL  | Kraken API    |
| SOL-USD    | 2026-07-15 00:00:00 |    77.41      |         17.8333   | NEUTRAL  | Kraken API    |
| SOXX       | 2026-07-14 00:00:00 |   567.92      |         -1.66667  | NEUTRAL  | Yahoo Finance |
| SUSHI-USD  | 2026-07-15 00:00:00 |     0.1667    |         29.6667   | NEUTRAL  | Kraken API    |
| TGT        | 2026-07-14 00:00:00 |   134         |         28.3333   | NEUTRAL  | Yahoo Finance |
| TIA-USD    | 2026-07-15 00:00:00 |     0.4098    |         44.8333   | NEUTRAL  | Kraken API    |
| TMUS       | 2026-07-14 00:00:00 |   187.13      |          6.75     | NEUTRAL  | Yahoo Finance |
| TRX-USD    | 2026-07-15 00:00:00 |     0.325846  |         39.8333   | NEUTRAL  | Kraken API    |
| TSLA       | 2026-07-14 00:00:00 |   396.18      |        -41.5833   | NEUTRAL  | Yahoo Finance |
| TXN        | 2026-07-14 00:00:00 |   305.55      |         31.3333   | NEUTRAL  | Yahoo Finance |
| UPS        | 2026-07-14 00:00:00 |   113.67      |         64        | NEUTRAL  | Yahoo Finance |
| VEA        | 2026-07-14 00:00:00 |    70.6       |          7.66667  | NEUTRAL  | Yahoo Finance |
| VIXY       | 2026-07-14 00:00:00 |    20.66      |        -36.5      | NEUTRAL  | Yahoo Finance |
| VNQ        | 2026-07-14 00:00:00 |    97.57      |         23.3333   | NEUTRAL  | Yahoo Finance |
| VTI        | 2026-07-14 00:00:00 |   371.16      |         66.8333   | NEUTRAL  | Yahoo Finance |
| VWO        | 2026-07-14 00:00:00 |    59.08      |        -19.5      | NEUTRAL  | Yahoo Finance |
| XLB        | 2026-07-14 00:00:00 |    50.64      |        -21.5      | NEUTRAL  | Yahoo Finance |
| XLC        | 2026-07-14 00:00:00 |   111.45      |          8.16667  | NEUTRAL  | Yahoo Finance |
| XLI        | 2026-07-14 00:00:00 |   180.45      |         25        | NEUTRAL  | Yahoo Finance |
| XLK        | 2026-07-14 00:00:00 |   183.62      |          3.66667  | NEUTRAL  | Yahoo Finance |
| XLM-USD    | 2026-07-15 00:00:00 |     0.182359  |        -45.25     | NEUTRAL  | Kraken API    |
| XLP        | 2026-07-14 00:00:00 |    83.42      |         -5.41667  | NEUTRAL  | Yahoo Finance |
| XLY        | 2026-07-14 00:00:00 |   115.9       |         -3        | NEUTRAL  | Yahoo Finance |
| XRP-USD    | 2026-07-15 00:00:00 |     1.09974   |          0.416667 | NEUTRAL  | Kraken API    |
| AGG        | 2026-07-14 00:00:00 |    98         |        -46.75     | SHORT    | Yahoo Finance |
| BND        | 2026-07-14 00:00:00 |    72.7       |        -46.75     | SHORT    | Yahoo Finance |
| GLD        | 2026-07-14 00:00:00 |   372.15      |        -30.75     | SHORT    | Yahoo Finance |
| HBAR-USD   | 2026-07-15 00:00:00 |     0.06733   |        -30        | SHORT    | Kraken API    |
| IBM        | 2026-07-14 00:00:00 |   217.07      |        -38.8333   | SHORT    | Yahoo Finance |
| ORCL       | 2026-07-14 00:00:00 |   127.94      |        -60.5833   | SHORT    | Yahoo Finance |
| PFE        | 2026-07-14 00:00:00 |    24.25      |        -33.25     | SHORT    | Yahoo Finance |
| SLV        | 2026-07-14 00:00:00 |    53.17      |        -32.75     | SHORT    | Yahoo Finance |
| T          | 2026-07-14 00:00:00 |    21.28      |        -38.75     | SHORT    | Yahoo Finance |
| TLT        | 2026-07-14 00:00:00 |    84.08      |        -52.5833   | SHORT    | Yahoo Finance |
| VZ         | 2026-07-14 00:00:00 |    42.47      |        -49.3333   | SHORT    | Yahoo Finance |
| WIF-USD    | 2026-07-15 00:00:00 |     0.154     |        -37.3333   | SHORT    | Kraken API    |
| WMT        | 2026-07-14 00:00:00 |   113.7       |        -39.5      | SHORT    | Yahoo Finance |

## Edge Summary

- Symbols with trades: **160** of 160
- Beat buy-and-hold: **32.50%** of traded symbols
- Positive return: **30.00%** of traded symbols
- Median strategy return: **-9.71%** (benchmark **16.53%**)
- Median excess vs benchmark: **-28.05%**
- Median Sharpe: **-0.12**
- Median exposure: **44.26%**

> Edge is real only if both _beat buy-and-hold_ and _median excess_ are convincingly positive across many symbols. Treat a single high-return symbol as noise.

## Portfolio Backtest

Actual capital-allocation books (not per-symbol averages). Benchmarks: `equal_weight_buyhold` (whole tracked universe), `spy_buyhold` (100% SPY), and `sixty_forty` (60% SPY / 40% AGG). `high_conf_voltarget` inverse-vol-weights the HIGH-confidence book; `conviction_long_short` is market-neutral. Judge on **Sharpe** and **max_drawdown** out-of-sample, not raw return: a fully-invested long book wins on return in a bull market but carries all the risk.

| strategy              | scope         | ann_return   | ann_vol   |   sharpe | max_drawdown   | total_return   |   avg_gross_exposure |
|:----------------------|:--------------|:-------------|:----------|---------:|:---------------|:---------------|---------------------:|
| equal_weight_buyhold  | full          | -2.84%       | 32.51%    |    -0.09 | -47.00%        | -22.03%        |                 1    |
| equal_weight_buyhold  | out_of_sample | -22.53%      | 31.08%    |    -0.73 | -39.63%        | -25.35%        |                 1    |
| all_signals_ew        | full          | -19.11%      | 27.35%    |    -0.7  | -63.68%        | -50.22%        |                 1    |
| all_signals_ew        | out_of_sample | 19.31%       | 26.79%    |     0.72 | -18.32%        | 18.34%         |                 1    |
| high_conf_ew          | full          | 0.28%        | 31.50%    |     0.01 | -44.03%        | -13.14%        |                 0.88 |
| high_conf_ew          | out_of_sample | 21.73%       | 33.76%    |     0.64 | -17.35%        | 18.87%         |                 0.88 |
| high_conf_voltarget   | full          | 2.24%        | 29.09%    |     0.08 | -36.22%        | -5.67%         |                 0.88 |
| high_conf_voltarget   | out_of_sample | 15.40%       | 31.31%    |     0.49 | -16.94%        | 12.06%         |                 0.88 |
| conviction_long_short | full          | -17.95%      | 23.23%    |    -0.77 | -48.26%        | -46.73%        |                 0.97 |
| conviction_long_short | out_of_sample | -12.19%      | 26.27%    |    -0.46 | -23.90%        | -15.39%        |                 0.97 |
| spy_buyhold           | full          | 6.75%        | 13.35%    |     0.51 | -18.27%        | 19.53%         |                 0.78 |
| spy_buyhold           | out_of_sample | -1.64%       | 9.77%     |    -0.17 | -13.27%        | -2.24%         |                 0.78 |
| sixty_forty           | full          | 4.02%        | 8.44%     |     0.48 | -10.80%        | 11.79%         |                 0.78 |
| sixty_forty           | out_of_sample | -2.41%       | 6.45%     |    -0.37 | -9.26%         | -2.76%         |                 0.78 |

## Walk-Forward Robustness

Each book measured across contiguous time folds (each a different regime). A book has durable edge only if `mean_sharpe` is positive, `min_sharpe` isn't deeply negative, and `pct_positive_folds` is high — a single great fold doesn't count. `fold_sharpes` lists each fold oldest-to-newest.

| strategy              |   n_folds |   mean_sharpe |   median_sharpe |   min_sharpe | pct_positive_folds   | mean_return   | fold_sharpes                 |
|:----------------------|----------:|--------------:|----------------:|-------------:|:---------------------|:--------------|:-----------------------------|
| equal_weight_buyhold  |         5 |          0.3  |            0.55 |        -1.31 | 60.00%               | -1.41%        | 1.93;-1.31;1.59;-1.24;0.55   |
| all_signals_ew        |         5 |         -0.68 |           -0.56 |        -2.04 | 20.00%               | -12.28%       | 0.15;-0.56;-2.04;-0.00;-0.97 |
| high_conf_ew          |         5 |          0.13 |           -0.32 |        -0.55 | 40.00%               | -2.28%        | 1.36;-0.55;-0.36;0.53;-0.32  |
| high_conf_voltarget   |         5 |          0.31 |           -0.31 |        -0.45 | 40.00%               | -0.72%        | 2.21;-0.31;-0.34;0.44;-0.45  |
| conviction_long_short |         5 |         -0.92 |           -1.22 |        -2.01 | 20.00%               | -11.41%       | -1.34;-1.22;-0.37;0.31;-2.01 |
| spy_buyhold           |         5 |          0.64 |            0.23 |        -1.14 | 60.00%               | 4.02%         | 1.84;-0.27;2.54;-1.14;0.23   |
| sixty_forty           |         5 |          0.6  |           -0.13 |        -1.16 | 40.00%               | 2.45%         | 2.05;-0.43;2.69;-1.16;-0.13  |

## Strategy Comparison

Each decision rule backtested over the same data. `out_of_sample` is the most recent ~35% of each symbol's history (unseen tail). A rule has real edge only if `median_excess` and `beat_benchmark_pct` stay positive out-of-sample, not just full-sample.

| strategy        | scope         |   symbols | beat_benchmark_pct   | positive_pct   | median_return   | median_benchmark   | median_excess   |   median_sharpe |   total_trades |
|:----------------|:--------------|----------:|:---------------------|:---------------|:----------------|:-------------------|:----------------|----------------:|---------------:|
| trend           | full          |       160 | 32.50%               | 30.00%         | -9.71%          | 16.53%             | -28.05%         |           -0.12 |          11259 |
| trend           | out_of_sample |       160 | 42.50%               | 51.88%         | 0.71%           | 4.64%              | -2.87%          |            0.19 |           3818 |
| mean_reversion  | full          |       157 | 40.13%               | 51.59%         | 0.09%           | 15.85%             | -16.49%         |            0.04 |           1258 |
| mean_reversion  | out_of_sample |       125 | 52.00%               | 59.20%         | 0.36%           | -1.68%             | 1.36%           |            0.63 |            424 |
| regime_adaptive | full          |       160 | 33.12%               | 31.87%         | -10.88%         | 16.53%             | -28.45%         |           -0.12 |          11533 |
| regime_adaptive | out_of_sample |       160 | 42.50%               | 52.50%         | 1.09%           | 4.64%              | -3.32%          |            0.19 |           3918 |

## Signal Calibration

Realized forward return in the signal's direction, grouped by confidence. HIGH should outrank LOW for the confidence score to be meaningful.

| confidence_level   |   horizon |     n | mean_return   | median_return   | win_rate   |
|:-------------------|----------:|------:|:--------------|:----------------|:-----------|
| HIGH               |         5 |  7914 | 0.12%         | 0.11%           | 51.77%     |
| MEDIUM             |         5 | 29216 | 0.02%         | 0.07%           | 50.80%     |
| LOW                |         5 |  3342 | -0.62%        | -0.55%          | 44.55%     |
| ALL                |         5 | 40472 | -0.01%        | 0.04%           | 50.48%     |
| HIGH               |        10 |  7871 | 0.41%         | 0.11%           | 51.34%     |
| MEDIUM             |        10 | 29038 | 0.17%         | 0.13%           | 51.00%     |
| LOW                |        10 |  3294 | -0.88%        | -0.72%          | 45.32%     |
| ALL                |        10 | 40203 | 0.13%         | 0.07%           | 50.60%     |
| HIGH               |        20 |  7781 | 0.77%         | 0.33%           | 52.78%     |
| MEDIUM             |        20 | 28650 | 0.85%         | 0.63%           | 53.61%     |
| LOW                |        20 |  3244 | -0.65%        | -0.49%          | 47.32%     |
| ALL                |        20 | 39675 | 0.71%         | 0.50%           | 52.93%     |

## Backtest Summary

### Data Quality / Signal Availability

- **ok**: 160 symbols

| symbol     |   trades | return   | benchmark_return   | mdd     |   sharpe | exposure   | skipped_reason   |
|:-----------|---------:|:---------|:-------------------|:--------|---------:|:-----------|:-----------------|
| AAPL       |       63 | 12.16%   | 73.42%             | -20.65% |     0.34 | 49.08%     | ok               |
| AAVE-USD   |       74 | -46.69%  | -59.15%            | -68.26% |    -0.38 | 39.27%     | ok               |
| ABBV       |       66 | -21.68%  | 39.28%             | -30.55% |    -0.47 | 47.25%     | ok               |
| ADA-USD    |       90 | -83.04%  | -76.06%            | -89.12% |    -0.67 | 46.93%     | ok               |
| ADBE       |       64 | -32.26%  | -59.26%            | -37.56% |    -0.42 | 57.57%     | ok               |
| AGG        |       71 | -6.91%   | 0.83%              | -10.16% |    -1.15 | 31.28%     | ok               |
| ALGO-USD   |       86 | -50.43%  | -69.42%            | -53.13% |    -0.57 | 38.12%     | ok               |
| AMAT       |       71 | -30.74%  | 214.95%            | -57.21% |    -0.24 | 52.75%     | ok               |
| AMD        |       52 | 5.86%    | 230.82%            | -43.98% |     0.27 | 35.77%     | ok               |
| AMGN       |       69 | -15.41%  | 25.30%             | -34.14% |    -0.29 | 46.26%     | ok               |
| AMZN       |       80 | -34.72%  | 48.13%             | -42.48% |    -1.02 | 38.27%     | ok               |
| APT-USD    |       74 | -42.40%  | -89.47%            | -69.96% |    -0.25 | 42.34%     | ok               |
| ARB-USD    |       68 | -22.71%  | -79.71%            | -62.34% |    -0.03 | 38.70%     | ok               |
| ARKK       |       85 | -36.86%  | 63.32%             | -38.31% |    -0.66 | 40.60%     | ok               |
| ATOM-USD   |       88 | -70.44%  | -65.81%            | -73.75% |    -1.23 | 45.40%     | ok               |
| AVAX-USD   |       70 | -32.89%  | -73.39%            | -55.62% |    -0.26 | 38.51%     | ok               |
| AVGO       |       64 | 21.68%   | 217.24%            | -35.76% |     0.41 | 43.09%     | ok               |
| BA         |       67 | 7.60%    | 6.76%              | -30.56% |     0.25 | 49.25%     | ok               |
| BAC        |       78 | -7.46%   | 78.50%             | -26.91% |    -0.12 | 49.42%     | ok               |
| BCH-USD    |       76 | 2.97%    | -28.59%            | -53.87% |     0.24 | 48.08%     | ok               |
| BITO       |       80 | -1.60%   | -64.52%            | -42.82% |     0.16 | 41.76%     | ok               |
| BLK        |       71 | -7.59%   | 28.48%             | -24.29% |    -0.16 | 42.43%     | ok               |
| BND        |       67 | -7.60%   | 0.85%              | -9.89%  |    -1.22 | 32.45%     | ok               |
| BONK-USD   |       70 | 41.58%   | -78.20%            | -45.22% |     0.58 | 41.76%     | ok               |
| BTC-USD    |       76 | -3.75%   | -33.07%            | -24.23% |     0.09 | 52.68%     | ok               |
| C          |       81 | -29.95%  | 140.47%            | -38.09% |    -0.59 | 51.58%     | ok               |
| CAT        |       72 | 25.75%   | 197.49%            | -21.02% |     0.5  | 56.24%     | ok               |
| CL         |       62 | 9.72%    | 7.59%              | -14.32% |     0.37 | 46.26%     | ok               |
| CMCSA      |       79 | -39.33%  | -40.61%            | -40.24% |    -1.04 | 42.43%     | ok               |
| COMP-USD   |       91 | -45.98%  | -66.85%            | -58.41% |    -0.36 | 46.55%     | ok               |
| COP        |       74 | -26.58%  | 2.13%              | -43.96% |    -0.5  | 41.60%     | ok               |
| COST       |       62 | -1.11%   | 27.02%             | -29.73% |     0.04 | 44.09%     | ok               |
| CRM        |       63 | -40.72%  | -41.49%            | -42.49% |    -0.86 | 42.93%     | ok               |
| CRV-USD    |       68 | -6.45%   | -56.72%            | -39.89% |     0.17 | 36.21%     | ok               |
| CSCO       |       61 | 22.19%   | 142.52%            | -21.79% |     0.49 | 49.42%     | ok               |
| CVX        |       75 | -18.11%  | 18.03%             | -29.13% |    -0.47 | 39.60%     | ok               |
| DASH-USD   |       63 | -46.35%  | 33.19%             | -64.43% |    -0.08 | 30.08%     | ok               |
| DBC        |       60 | -12.19%  | 30.67%             | -25.15% |    -0.41 | 33.28%     | ok               |
| DE         |       72 | -8.54%   | 63.52%             | -25.24% |    -0.09 | 47.59%     | ok               |
| DIA        |       60 | -2.24%   | 36.04%             | -12.94% |    -0.08 | 44.09%     | ok               |
| DIS        |       68 | -17.71%  | -12.40%            | -28.17% |    -0.31 | 46.09%     | ok               |
| DOGE-USD   |       73 | -25.08%  | -70.33%            | -60.95% |    -0.01 | 50.38%     | ok               |
| DOT-USD    |       88 | -59.56%  | -82.13%            | -63.10% |    -0.65 | 48.08%     | ok               |
| DXY-INDEX  |       38 | -1.23%   | -0.53%             | -6.02%  |    -0.18 | 31.02%     | ok               |
| EEM        |       64 | -9.40%   | 63.60%             | -25.67% |    -0.25 | 43.43%     | ok               |
| EFA        |       60 | -7.42%   | 36.11%             | -13.02% |    -0.26 | 44.26%     | ok               |
| EOG        |       81 | -23.18%  | 21.99%             | -48.13% |    -0.48 | 46.76%     | ok               |
| ETC-USD    |       64 | -33.98%  | -65.26%            | -46.54% |    -0.47 | 30.65%     | ok               |
| ETH-USD    |       66 | 134.73%  | -28.92%            | -30.11% |     1.17 | 45.02%     | ok               |
| EWJ        |       62 | -18.16%  | 38.22%             | -30.73% |    -0.59 | 39.10%     | ok               |
| FCX        |       63 | -27.81%  | 62.43%             | -47.47% |    -0.31 | 45.26%     | ok               |
| FET-USD    |       83 | -39.93%  | -79.10%            | -54.02% |    -0.15 | 41.38%     | ok               |
| FIL-USD    |       70 | -46.58%  | -76.45%            | -50.22% |    -0.6  | 32.95%     | ok               |
| FXI        |       44 | -6.84%   | 47.34%             | -23.91% |    -0.09 | 30.12%     | ok               |
| GDX        |       60 | 11.28%   | 177.44%            | -34.99% |     0.3  | 48.09%     | ok               |
| GDXJ       |       68 | -23.13%  | 203.42%            | -44.93% |    -0.22 | 46.42%     | ok               |
| GE         |       76 | 12.65%   | 198.23%            | -27.82% |     0.33 | 53.58%     | ok               |
| GLD        |       48 | 27.07%   | 98.51%             | -16.63% |     0.67 | 47.42%     | ok               |
| GOOGL      |       61 | 76.69%   | 154.75%            | -20.41% |     1.15 | 52.91%     | ok               |
| GRT-USD    |       83 | -18.35%  | -86.56%            | -54.83% |    -0.01 | 42.15%     | ok               |
| GS         |       76 | -2.38%   | 196.47%            | -22.13% |     0.05 | 52.08%     | ok               |
| HD         |       71 | -7.53%   | -6.85%             | -17.69% |    -0.12 | 44.59%     | ok               |
| HON        |       93 | -26.82%  | 13.24%             | -29.80% |    -0.72 | 52.41%     | ok               |
| HYG        |       81 | -9.08%   | 3.39%              | -9.59%  |    -1.06 | 33.94%     | ok               |
| IBIT       |       34 | 30.82%   | -3.76%             | -18.95% |     0.67 | 32.24%     | ok               |
| IBM        |       78 | -20.21%  | 18.33%             | -44.08% |    -0.21 | 49.58%     | ok               |
| ICP-USD    |       77 | -15.33%  | -68.56%            | -51.29% |     0.1  | 35.06%     | ok               |
| IEF        |       76 | -10.90%  | -0.37%             | -11.70% |    -1.54 | 32.78%     | ok               |
| IEMG       |       58 | -7.95%   | 57.77%             | -26.84% |    -0.21 | 42.93%     | ok               |
| INJ-USD    |       75 | -55.12%  | -63.74%            | -77.42% |    -0.55 | 37.55%     | ok               |
| INTC       |       70 | 55.82%   | 142.05%            | -60.60% |     0.62 | 49.25%     | ok               |
| INTU       |       67 | -19.54%  | -56.27%            | -42.15% |    -0.23 | 41.60%     | ok               |
| ITA        |       72 | -2.69%   | 87.57%             | -23.75% |    -0    | 48.42%     | ok               |
| IWM        |       48 | 9.40%    | 48.08%             | -12.83% |     0.39 | 35.77%     | ok               |
| JNJ        |       68 | 7.15%    | 60.81%             | -17.51% |     0.3  | 50.75%     | ok               |
| JPM        |       77 | -18.98%  | 90.78%             | -33.43% |    -0.45 | 53.91%     | ok               |
| KO         |       49 | 28.93%   | 36.87%             | -8.07%  |     1.03 | 37.77%     | ok               |
| LDO-USD    |       78 | 8.66%    | -78.29%            | -62.63% |     0.35 | 39.46%     | ok               |
| LIN        |       66 | -2.67%   | 19.86%             | -21.53% |    -0.03 | 39.43%     | ok               |
| LINK-USD   |       73 | -16.53%  | -54.68%            | -49.35% |     0.06 | 42.15%     | ok               |
| LLY        |       71 | -27.14%  | 52.52%             | -53.34% |    -0.39 | 49.92%     | ok               |
| LRCX       |       80 | -23.99%  | 284.37%            | -63.56% |    -0.13 | 45.09%     | ok               |
| LTC-USD    |       70 | -36.00%  | -58.18%            | -53.76% |    -0.33 | 49.04%     | ok               |
| MCD        |       75 | -2.55%   | -8.10%             | -18.81% |    -0.05 | 38.10%     | ok               |
| META       |       72 | -28.91%  | 40.13%             | -38.96% |    -0.49 | 47.92%     | ok               |
| MPC        |       71 | -6.42%   | 84.67%             | -44.76% |     0.01 | 48.75%     | ok               |
| MRK        |       69 | -32.33%  | -5.17%             | -35.95% |    -0.8  | 44.26%     | ok               |
| MS         |       79 | -10.35%  | 166.75%            | -27.79% |    -0.17 | 49.75%     | ok               |
| MSFT       |       83 | -38.30%  | -4.43%             | -39.15% |    -1.02 | 47.42%     | ok               |
| MU         |       51 | 270.20%  | 1118.09%           | -68.76% |     1.34 | 59.90%     | ok               |
| NEAR-USD   |       85 | -16.55%  | -36.58%            | -60.07% |     0.08 | 41.38%     | ok               |
| NEM        |       72 | -27.67%  | 185.48%            | -38.49% |    -0.27 | 53.91%     | ok               |
| NFLX       |       64 | 30.76%   | 27.85%             | -21.09% |     0.66 | 54.41%     | ok               |
| NKE        |       91 | -37.92%  | -58.51%            | -55.35% |    -0.53 | 43.93%     | ok               |
| NOW        |       84 | 4.35%    | -30.36%            | -28.87% |     0.22 | 45.76%     | ok               |
| NVDA       |       75 | -23.69%  | 152.04%            | -45.02% |    -0.14 | 59.36%     | ok               |
| OP-USD     |       72 | -29.45%  | -90.60%            | -70.27% |    -0.11 | 33.91%     | ok               |
| ORCL       |       72 | 116.52%  | 17.97%             | -29.47% |     0.97 | 54.24%     | ok               |
| OXY        |       71 | -0.03%   | -8.38%             | -34.15% |     0.12 | 45.42%     | ok               |
| PEP        |       79 | -5.52%   | -19.69%            | -21.35% |    -0.1  | 48.59%     | ok               |
| PEPE-USD   |       79 | 0.11%    | -70.77%            | -57.66% |     0.28 | 44.83%     | ok               |
| PFE        |       79 | -40.08%  | -12.11%            | -41.48% |    -1.29 | 35.94%     | ok               |
| PG         |       68 | -18.64%  | -7.84%             | -24.55% |    -0.7  | 40.43%     | ok               |
| PM         |       85 | -4.28%   | 96.29%             | -33.68% |     0    | 55.91%     | ok               |
| POL-USD    |       77 | 40.66%   | -72.21%            | -46.45% |     0.6  | 46.74%     | ok               |
| QCOM       |       73 | -15.25%  | 17.20%             | -56.59% |    -0.04 | 46.09%     | ok               |
| QQQ        |       64 | 18.25%   | 68.42%             | -12.88% |     0.53 | 43.93%     | ok               |
| RENDER-USD |       98 | -19.07%  | -63.20%            | -45.00% |     0.1  | 42.94%     | ok               |
| RTX        |       58 | 24.20%   | 112.56%            | -16.99% |     0.61 | 51.58%     | ok               |
| SBUX       |       67 | -22.19%  | 13.60%             | -29.22% |    -0.44 | 40.27%     | ok               |
| SCHW       |       74 | -14.01%  | 59.01%             | -31.92% |    -0.27 | 47.42%     | ok               |
| SHIB-USD   |       78 | -36.70%  | -73.14%            | -47.96% |    -0.31 | 51.92%     | ok               |
| SHY        |       50 | -2.39%   | 0.27%              | -2.85%  |    -0.84 | 34.44%     | ok               |
| SKY-USD    |       72 | -28.04%  | 6.09%              | -43.98% |    -0.33 | 40.18%     | ok               |
| SLB        |       75 | -25.47%  | -2.02%             | -54.23% |    -0.43 | 51.08%     | ok               |
| SLV        |       58 | 48.52%   | 152.35%            | -42.66% |     0.68 | 43.09%     | ok               |
| SMH        |       48 | 89.01%   | 203.52%            | -33.99% |     1.15 | 48.09%     | ok               |
| SNX-USD    |       58 | -15.26%  | -75.49%            | -34.76% |     0.08 | 37.93%     | ok               |
| SOL-USD    |       70 | -33.39%  | -61.41%            | -56.90% |    -0.1  | 59.58%     | ok               |
| SOXX       |       57 | 76.42%   | 177.21%            | -41.89% |     0.99 | 46.92%     | ok               |
| SPY        |       64 | 4.26%    | 51.35%             | -16.47% |     0.21 | 50.08%     | ok               |
| SUSHI-USD  |       96 | -81.50%  | -80.20%            | -85.18% |    -1.27 | 36.59%     | ok               |
| T          |       64 | 42.17%   | 25.84%             | -17.01% |     0.92 | 52.91%     | ok               |
| TGT        |       60 | -11.24%  | -10.60%            | -40.57% |    -0.15 | 39.27%     | ok               |
| TIA-USD    |       89 | -42.33%  | -86.85%            | -66.21% |    -0.27 | 36.21%     | ok               |
| TLT        |       72 | -21.30%  | -9.44%             | -21.82% |    -1.65 | 31.95%     | ok               |
| TMO        |       61 | 15.63%   | -2.57%             | -18.85% |     0.41 | 50.42%     | ok               |
| TMUS       |       70 | 7.70%    | 15.48%             | -25.71% |     0.26 | 48.42%     | ok               |
| TRX-USD    |       72 | 0.99%    | 40.18%             | -22.90% |     0.12 | 49.04%     | ok               |
| TSLA       |       69 | 5.29%    | 104.47%            | -42.22% |     0.25 | 40.93%     | ok               |
| TXN        |       73 | -12.16%  | 87.75%             | -47.39% |    -0.04 | 53.24%     | ok               |
| UNH        |       74 | 29.58%   | -18.40%            | -27.86% |     0.51 | 52.58%     | ok               |
| UNI-USD    |       88 | -72.70%  | -59.94%            | -80.61% |    -0.87 | 43.87%     | ok               |
| UPS        |       70 | -37.14%  | -23.53%            | -38.83% |    -0.75 | 39.27%     | ok               |
| USO        |       68 | 7.84%    | 65.93%             | -43.35% |     0.25 | 33.61%     | ok               |
| VEA        |       58 | -0.98%   | 46.38%             | -17.93% |     0.01 | 44.09%     | ok               |
| VIXY       |       94 | -79.98%  | -65.01%            | -88.16% |    -1    | 31.95%     | ok               |
| VNQ        |       73 | -15.70%  | 15.85%             | -24.92% |    -0.65 | 37.27%     | ok               |
| VTI        |       72 | -3.15%   | 50.33%             | -18.77% |    -0.05 | 50.58%     | ok               |
| VWO        |       78 | -13.87%  | 43.50%             | -25.20% |    -0.49 | 44.26%     | ok               |
| VZ         |       85 | -27.48%  | 4.86%              | -27.83% |    -0.92 | 37.60%     | ok               |
| WFC        |       84 | -18.36%  | 64.75%             | -30.87% |    -0.31 | 50.42%     | ok               |
| WIF-USD    |       68 | -35.28%  | -76.05%            | -50.54% |    -0.13 | 31.99%     | ok               |
| WMT        |       61 | 13.67%   | 93.96%             | -21.31% |     0.43 | 50.58%     | ok               |
| XBI        |       62 | 5.11%    | 68.27%             | -19.80% |     0.21 | 41.10%     | ok               |
| XLB        |       62 | -9.41%   | 19.17%             | -25.37% |    -0.3  | 36.61%     | ok               |
| XLC        |       67 | 12.36%   | 41.38%             | -12.33% |     0.45 | 54.41%     | ok               |
| XLE        |       75 | -7.99%   | 34.33%             | -37.64% |    -0.12 | 45.26%     | ok               |
| XLF        |       76 | -10.01%  | 42.16%             | -23.61% |    -0.32 | 47.75%     | ok               |
| XLI        |       66 | -0.61%   | 53.37%             | -11.79% |     0.03 | 44.59%     | ok               |
| XLK        |       40 | 65.83%   | 83.15%             | -14.75% |     1.22 | 45.59%     | ok               |
| XLM-USD    |       69 | 5.21%    | -41.96%            | -50.36% |     0.28 | 45.79%     | ok               |
| XLP        |       68 | 5.21%    | 12.65%             | -11.16% |     0.33 | 41.93%     | ok               |
| XLU        |       67 | -4.23%   | 49.34%             | -20.40% |    -0.15 | 38.94%     | ok               |
| XLV        |       68 | -15.42%  | 9.07%              | -19.97% |    -0.77 | 36.11%     | ok               |
| XLY        |       72 | 2.75%    | 30.72%             | -14.01% |     0.15 | 44.26%     | ok               |
| XOM        |       57 | 4.33%    | 41.21%             | -20.29% |     0.19 | 36.27%     | ok               |
| XRP-USD    |       58 | -30.47%  | -54.05%            | -44.89% |    -0.26 | 33.72%     | ok               |
| YFI-USD    |       81 | -65.87%  | -62.58%            | -70.70% |    -1.09 | 40.80%     | ok               |
| ZEC-USD    |       64 | 50.08%   | 1605.07%           | -47.68% |     0.59 | 35.44%     | ok               |

## AAPL Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 22.20%   | 73.42%             | -21.71% |     0.5  |       68 | 53.41%     | ok               |
|          15 | 18.44%   | 73.42%             | -23.86% |     0.43 |       75 | 60.57%     | ok               |
|          30 | 12.16%   | 73.42%             | -20.65% |     0.34 |       63 | 49.08%     | ok               |
|          25 | 10.99%   | 73.42%             | -20.03% |     0.32 |       67 | 51.08%     | ok               |
|          35 | 8.85%    | 73.42%             | -22.04% |     0.28 |       65 | 47.42%     | ok               |

## AAVE-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 22.47%   | -59.15%            | -43.61% |     0.44 |       40 | 31.99%     | ok               |
|          45 | 5.03%    | -59.15%            | -46.87% |     0.26 |       44 | 27.01%     | ok               |
|          35 | 1.52%    | -59.15%            | -51.96% |     0.24 |       50 | 35.25%     | ok               |
|          15 | -47.76%  | -59.15%            | -61.76% |    -0.25 |       80 | 53.45%     | ok               |
|          50 | -29.26%  | -59.15%            | -43.73% |    -0.28 |       42 | 19.54%     | ok               |

## ABBV Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -11.38%  | 39.28%             | -28.51% |    -0.22 |       50 | 37.10%     | ok               |
|          40 | -18.44%  | 39.28%             | -26.61% |    -0.41 |       66 | 41.60%     | ok               |
|          35 | -19.60%  | 39.28%             | -27.83% |    -0.44 |       68 | 44.43%     | ok               |
|          45 | -19.94%  | 39.28%             | -29.59% |    -0.46 |       56 | 38.60%     | ok               |
|          30 | -21.68%  | 39.28%             | -30.55% |    -0.47 |       66 | 47.25%     | ok               |

## ADA-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -77.92%  | -76.06%            | -85.97% |    -0.59 |       55 | 26.82%     | ok               |
|          45 | -80.28%  | -76.06%            | -88.02% |    -0.62 |       58 | 31.61%     | ok               |
|          35 | -82.72%  | -76.06%            | -89.77% |    -0.67 |       78 | 42.34%     | ok               |
|          30 | -83.04%  | -76.06%            | -89.12% |    -0.67 |       90 | 46.93%     | ok               |
|          40 | -83.55%  | -76.06%            | -90.19% |    -0.72 |       74 | 36.97%     | ok               |

## ADBE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 1.24%    | -59.26%            | -22.53% |     0.14 |       72 | 49.08%     | ok               |
|          40 | -11.88%  | -59.26%            | -24.87% |    -0.11 |       70 | 42.10%     | ok               |
|          25 | -19.52%  | -59.26%            | -32.07% |    -0.16 |       48 | 61.73%     | ok               |
|          20 | -27.26%  | -59.26%            | -33.08% |    -0.29 |       48 | 63.89%     | ok               |
|          15 | -29.99%  | -59.26%            | -32.12% |    -0.34 |       57 | 66.06%     | ok               |

## AGG Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -6.91%   | 0.83%              | -10.16% |    -1.15 |       71 | 31.28%     | ok               |
|          20 | -8.00%   | 0.83%              | -10.96% |    -1.17 |       75 | 36.94%     | ok               |
|          45 | -6.05%   | 0.83%              | -7.89%  |    -1.22 |       54 | 20.63%     | ok               |
|          50 | -5.57%   | 0.83%              | -7.92%  |    -1.25 |       46 | 16.97%     | ok               |
|          25 | -8.17%   | 0.83%              | -11.60% |    -1.25 |       75 | 35.27%     | ok               |

## ALGO-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -50.43%  | -69.42%            | -53.13% |    -0.57 |       86 | 38.12%     | ok               |
|          15 | -61.64%  | -69.42%            | -68.50% |    -0.67 |       84 | 50.38%     | ok               |
|          25 | -61.89%  | -69.42%            | -72.48% |    -0.74 |       84 | 45.02%     | ok               |
|          20 | -65.54%  | -69.42%            | -71.20% |    -0.8  |       86 | 48.08%     | ok               |
|          50 | -45.64%  | -69.42%            | -48.43% |    -0.81 |       42 | 16.86%     | ok               |

## AMAT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -18.45%  | 214.95%            | -54.05% |    -0.02 |       68 | 61.73%     | ok               |
|          30 | -30.74%  | 214.95%            | -57.21% |    -0.24 |       71 | 52.75%     | ok               |
|          35 | -31.22%  | 214.95%            | -55.26% |    -0.27 |       73 | 50.42%     | ok               |
|          50 | -31.06%  | 214.95%            | -48.72% |    -0.3  |       52 | 38.27%     | ok               |
|          20 | -38.69%  | 214.95%            | -60.16% |    -0.35 |       74 | 58.07%     | ok               |

## AMD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 6.74%    | 230.82%            | -44.26% |     0.27 |       54 | 30.62%     | ok               |
|          40 | 5.86%    | 230.82%            | -43.98% |     0.27 |       52 | 35.77%     | ok               |
|          35 | -5.47%   | 230.82%            | -50.71% |     0.16 |       60 | 37.27%     | ok               |
|          45 | -14.79%  | 230.82%            | -53.24% |     0.04 |       60 | 33.44%     | ok               |
|          30 | -17.93%  | 230.82%            | -56.46% |     0.02 |       61 | 39.77%     | ok               |

## AMGN Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -9.55%   | 25.30%             | -26.64% |    -0.12 |       71 | 52.25%     | ok               |
|          35 | -11.27%  | 25.30%             | -31.23% |    -0.18 |       65 | 42.43%     | ok               |
|          15 | -13.40%  | 25.30%             | -27.92% |    -0.2  |       70 | 57.90%     | ok               |
|          30 | -15.41%  | 25.30%             | -34.14% |    -0.29 |       69 | 46.26%     | ok               |
|          25 | -18.85%  | 25.30%             | -33.41% |    -0.37 |       65 | 48.59%     | ok               |

## AMZN Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -16.06%  | 48.13%             | -28.70% |    -0.46 |       54 | 29.28%     | ok               |
|          50 | -22.53%  | 48.13%             | -35.48% |    -0.79 |       52 | 23.29%     | ok               |
|          35 | -28.35%  | 48.13%             | -38.29% |    -0.87 |       68 | 32.78%     | ok               |
|          45 | -25.39%  | 48.13%             | -35.47% |    -0.88 |       56 | 26.29%     | ok               |
|          30 | -34.72%  | 48.13%             | -42.48% |    -1.02 |       80 | 38.27%     | ok               |

## APT-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 19.10%   | -89.47%            | -46.73% |     0.42 |       40 | 18.97%     | ok               |
|          45 | -9.82%   | -89.47%            | -63.86% |     0.08 |       58 | 24.90%     | ok               |
|          20 | -34.30%  | -89.47%            | -70.51% |    -0.1  |       71 | 51.15%     | ok               |
|          40 | -27.15%  | -89.47%            | -63.33% |    -0.11 |       64 | 30.46%     | ok               |
|          35 | -32.48%  | -89.47%            | -64.45% |    -0.16 |       68 | 36.21%     | ok               |

## ARB-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 33.36%   | -79.71%            | -53.74% |     0.52 |       87 | 56.13%     | ok               |
|          40 | 13.00%   | -79.71%            | -45.73% |     0.35 |       50 | 29.69%     | ok               |
|          20 | 0.22%    | -79.71%            | -60.40% |     0.28 |       75 | 49.62%     | ok               |
|          35 | 1.95%    | -79.71%            | -54.43% |     0.25 |       60 | 33.14%     | ok               |
|          45 | 1.34%    | -79.71%            | -49.08% |     0.22 |       56 | 22.99%     | ok               |

## ARKK Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -26.15%  | 63.32%             | -34.75% |    -0.32 |       92 | 50.75%     | ok               |
|          20 | -31.11%  | 63.32%             | -34.36% |    -0.45 |       89 | 46.26%     | ok               |
|          30 | -36.86%  | 63.32%             | -38.31% |    -0.66 |       85 | 40.60%     | ok               |
|          35 | -40.19%  | 63.32%             | -41.56% |    -0.8  |       86 | 38.10%     | ok               |
|          25 | -44.17%  | 63.32%             | -45.46% |    -0.86 |       93 | 42.60%     | ok               |

## ATOM-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -66.72%  | -65.81%            | -70.28% |    -1.02 |       91 | 51.92%     | ok               |
|          15 | -71.24%  | -65.81%            | -71.04% |    -1.08 |       93 | 61.88%     | ok               |
|          45 | -62.46%  | -65.81%            | -64.33% |    -1.21 |       74 | 29.31%     | ok               |
|          30 | -70.44%  | -65.81%            | -73.75% |    -1.23 |       88 | 45.40%     | ok               |
|          20 | -74.30%  | -65.81%            | -74.25% |    -1.25 |       99 | 55.56%     | ok               |

## AVAX-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 2.94%    | -73.39%            | -32.41% |     0.2  |       32 | 18.39%     | ok               |
|          40 | -4.64%   | -73.39%            | -39.29% |     0.1  |       38 | 25.10%     | ok               |
|          45 | -4.66%   | -73.39%            | -39.20% |     0.09 |       34 | 22.22%     | ok               |
|          35 | -11.46%  | -73.39%            | -42.28% |     0.03 |       54 | 30.46%     | ok               |
|          15 | -26.75%  | -73.39%            | -52.46% |    -0.05 |       71 | 53.07%     | ok               |

## AVGO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 21.68%   | 217.24%            | -35.76% |     0.41 |       64 | 43.09%     | ok               |
|          40 | 20.22%   | 217.24%            | -40.70% |     0.39 |       62 | 36.94%     | ok               |
|          25 | 17.62%   | 217.24%            | -38.01% |     0.37 |       70 | 44.43%     | ok               |
|          35 | 15.82%   | 217.24%            | -36.19% |     0.35 |       72 | 40.27%     | ok               |
|          50 | 15.77%   | 217.24%            | -35.84% |     0.35 |       58 | 30.78%     | ok               |

## BA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 23.47%   | 6.76%              | -13.42% |     0.62 |       42 | 31.28%     | ok               |
|          35 | 30.46%   | 6.76%              | -23.77% |     0.59 |       72 | 44.59%     | ok               |
|          40 | 17.66%   | 6.76%              | -25.45% |     0.43 |       46 | 38.44%     | ok               |
|          25 | 10.59%   | 6.76%              | -32.48% |     0.29 |       70 | 52.58%     | ok               |
|          30 | 7.60%    | 6.76%              | -30.56% |     0.25 |       67 | 49.25%     | ok               |

## BAC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 4.80%    | 78.50%             | -18.35% |     0.21 |       58 | 37.27%     | ok               |
|          35 | -0.77%   | 78.50%             | -27.11% |     0.05 |       70 | 45.42%     | ok               |
|          50 | -1.43%   | 78.50%             | -19.12% |     0.02 |       58 | 34.28%     | ok               |
|          40 | -2.50%   | 78.50%             | -22.59% |    -0    |       62 | 40.27%     | ok               |
|          20 | -4.42%   | 78.50%             | -23.16% |    -0.02 |       78 | 53.74%     | ok               |

## BCH-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 2.97%    | -28.59%            | -53.87% |     0.24 |       76 | 48.08%     | ok               |
|          20 | -9.36%   | -28.59%            | -52.88% |     0.14 |       72 | 54.98%     | ok               |
|          15 | -16.30%  | -28.59%            | -58.44% |     0.07 |       78 | 59.39%     | ok               |
|          25 | -20.48%  | -28.59%            | -58.37% |    -0    |       72 | 50.57%     | ok               |
|          35 | -18.99%  | -28.59%            | -64.08% |    -0.04 |       70 | 44.25%     | ok               |

## BITO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 15.03%   | -64.52%            | -32.29% |     0.34 |       54 | 25.29%     | ok               |
|          30 | -1.60%   | -64.52%            | -42.82% |     0.16 |       80 | 41.76%     | ok               |
|          45 | -3.23%   | -64.52%            | -43.53% |     0.11 |       62 | 28.95%     | ok               |
|          15 | -8.86%   | -64.52%            | -48.38% |     0.11 |       89 | 50.75%     | ok               |
|          35 | -6.41%   | -64.52%            | -47.25% |     0.1  |       72 | 37.60%     | ok               |

## BLK Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | -1.31%   | 28.48%             | -17.97% |     0.03 |       76 | 38.44%     | ok               |
|          20 | -3.44%   | 28.48%             | -21.48% |    -0.02 |       76 | 47.25%     | ok               |
|          40 | -4.96%   | 28.48%             | -20.08% |    -0.1  |       70 | 34.44%     | ok               |
|          30 | -7.59%   | 28.48%             | -24.29% |    -0.16 |       71 | 42.43%     | ok               |
|          25 | -8.52%   | 28.48%             | -23.36% |    -0.18 |       71 | 44.76%     | ok               |

## BND Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -6.46%   | 0.85%              | -9.05%  |    -0.94 |       65 | 38.27%     | ok               |
|          25 | -7.16%   | 0.85%              | -10.14% |    -1.09 |       69 | 36.27%     | ok               |
|          30 | -7.60%   | 0.85%              | -9.89%  |    -1.22 |       67 | 32.45%     | ok               |
|          15 | -8.67%   | 0.85%              | -10.73% |    -1.25 |       75 | 41.10%     | ok               |
|          45 | -7.85%   | 0.85%              | -9.57%  |    -1.52 |       52 | 22.13%     | ok               |

## BONK-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 169.29%  | -78.20%            | -35.57% |     1.24 |       44 | 22.03%     | ok               |
|          45 | 121.76%  | -78.20%            | -42.36% |     1.02 |       54 | 26.25%     | ok               |
|          20 | 140.65%  | -78.20%            | -55.43% |     0.95 |       66 | 52.87%     | ok               |
|          15 | 146.15%  | -78.20%            | -63.45% |     0.94 |       69 | 57.85%     | ok               |
|          25 | 111.86%  | -78.20%            | -47.99% |     0.87 |       65 | 48.08%     | ok               |

## BTC-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 43.79%   | -33.07%            | -15.92% |     0.81 |       46 | 34.67%     | ok               |
|          45 | 40.84%   | -33.07%            | -15.18% |     0.81 |       44 | 30.65%     | ok               |
|          35 | 26.71%   | -33.07%            | -27.54% |     0.56 |       70 | 41.57%     | ok               |
|          50 | 13.98%   | -33.07%            | -18.05% |     0.4  |       42 | 25.29%     | ok               |
|          30 | 11.49%   | -33.07%            | -21.75% |     0.33 |       74 | 48.28%     | ok               |

## C Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -6.29%   | 140.47%            | -22.28% |    -0.1  |       64 | 36.11%     | ok               |
|          45 | -18.56%  | 140.47%            | -30.30% |    -0.43 |       76 | 40.27%     | ok               |
|          15 | -27.14%  | 140.47%            | -34.76% |    -0.47 |       74 | 60.23%     | ok               |
|          25 | -26.40%  | 140.47%            | -34.95% |    -0.49 |       73 | 53.41%     | ok               |
|          20 | -28.87%  | 140.47%            | -36.31% |    -0.54 |       81 | 56.41%     | ok               |

## CAT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 25.75%   | 197.49%            | -21.02% |     0.5  |       72 | 56.24%     | ok               |
|          25 | 25.86%   | 197.49%            | -26.37% |     0.5  |       68 | 59.07%     | ok               |
|          20 | 24.36%   | 197.49%            | -25.65% |     0.48 |       78 | 62.56%     | ok               |
|          45 | 20.61%   | 197.49%            | -27.12% |     0.44 |       56 | 44.93%     | ok               |
|          35 | 17.49%   | 197.49%            | -27.72% |     0.39 |       70 | 49.75%     | ok               |

## CL Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 12.43%   | 7.59%              | -11.22% |     0.53 |       44 | 30.12%     | ok               |
|          30 | 9.72%    | 7.59%              | -14.32% |     0.37 |       62 | 46.26%     | ok               |
|          45 | 5.16%    | 7.59%              | -13.51% |     0.25 |       48 | 33.28%     | ok               |
|          35 | 4.50%    | 7.59%              | -13.83% |     0.21 |       64 | 42.60%     | ok               |
|          40 | 1.47%    | 7.59%              | -12.70% |     0.11 |       58 | 37.27%     | ok               |

## CMCSA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -37.68%  | -40.61%            | -44.10% |    -0.85 |       89 | 57.40%     | ok               |
|          30 | -39.33%  | -40.61%            | -40.24% |    -1.04 |       79 | 42.43%     | ok               |
|          25 | -43.14%  | -40.61%            | -42.87% |    -1.16 |       89 | 47.75%     | ok               |
|          50 | -31.69%  | -40.61%            | -32.53% |    -1.27 |       50 | 15.14%     | ok               |
|          20 | -48.38%  | -40.61%            | -48.13% |    -1.3  |       94 | 53.41%     | ok               |

## COMP-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -10.51%  | -66.85%            | -38.71% |     0.05 |       48 | 20.69%     | ok               |
|          30 | -45.98%  | -66.85%            | -58.41% |    -0.36 |       91 | 46.55%     | ok               |
|          25 | -48.61%  | -66.85%            | -60.58% |    -0.37 |       91 | 52.30%     | ok               |
|          15 | -55.44%  | -66.85%            | -65.55% |    -0.44 |      105 | 63.79%     | ok               |
|          40 | -47.71%  | -66.85%            | -50.01% |    -0.51 |       74 | 34.29%     | ok               |

## COP Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -8.45%   | 2.13%              | -34.85% |    -0.11 |       48 | 27.62%     | ok               |
|          35 | -21.00%  | 2.13%              | -43.32% |    -0.37 |       73 | 38.10%     | ok               |
|          45 | -19.27%  | 2.13%              | -40.87% |    -0.39 |       62 | 30.95%     | ok               |
|          30 | -26.58%  | 2.13%              | -43.96% |    -0.5  |       74 | 41.60%     | ok               |
|          40 | -24.37%  | 2.13%              | -46.62% |    -0.51 |       68 | 34.11%     | ok               |

## COST Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 10.38%   | 27.02%             | -24.32% |     0.35 |       66 | 50.58%     | ok               |
|          25 | 8.75%    | 27.02%             | -24.73% |     0.31 |       63 | 47.75%     | ok               |
|          35 | 4.77%    | 27.02%             | -26.58% |     0.21 |       54 | 40.93%     | ok               |
|          30 | -1.11%   | 27.02%             | -29.73% |     0.04 |       62 | 44.09%     | ok               |
|          40 | -1.66%   | 27.02%             | -28.41% |     0.01 |       56 | 37.94%     | ok               |

## CRM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -37.99%  | -41.49%            | -44.67% |    -0.62 |       92 | 54.58%     | ok               |
|          35 | -30.98%  | -41.49%            | -34.36% |    -0.62 |       60 | 38.10%     | ok               |
|          40 | -34.83%  | -41.49%            | -39.11% |    -0.8  |       66 | 33.94%     | ok               |
|          30 | -40.72%  | -41.49%            | -42.49% |    -0.86 |       63 | 42.93%     | ok               |
|          20 | -45.29%  | -41.49%            | -47.55% |    -0.88 |       76 | 48.25%     | ok               |

## CRV-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 17.80%   | -56.72%            | -37.78% |     0.4  |       70 | 31.61%     | ok               |
|          45 | 3.36%    | -56.72%            | -42.29% |     0.24 |       56 | 20.88%     | ok               |
|          40 | -2.40%   | -56.72%            | -38.86% |     0.18 |       60 | 27.20%     | ok               |
|          50 | -0.89%   | -56.72%            | -29.30% |     0.18 |       46 | 17.43%     | ok               |
|          30 | -6.45%   | -56.72%            | -39.89% |     0.17 |       68 | 36.21%     | ok               |

## CSCO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 32.30%   | 142.52%            | -19.34% |     0.7  |       54 | 37.77%     | ok               |
|          45 | 28.20%   | 142.52%            | -19.34% |     0.62 |       51 | 39.77%     | ok               |
|          35 | 24.39%   | 142.52%            | -23.68% |     0.53 |       53 | 46.76%     | ok               |
|          25 | 22.76%   | 142.52%            | -23.28% |     0.5  |       65 | 51.41%     | ok               |
|          30 | 22.19%   | 142.52%            | -21.79% |     0.49 |       61 | 49.42%     | ok               |

## CVX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -14.68%  | 18.03%             | -24.33% |    -0.34 |       75 | 42.26%     | ok               |
|          40 | -12.96%  | 18.03%             | -27.34% |    -0.34 |       77 | 34.78%     | ok               |
|          35 | -14.98%  | 18.03%             | -28.85% |    -0.38 |       69 | 36.94%     | ok               |
|          45 | -14.10%  | 18.03%             | -28.83% |    -0.39 |       67 | 30.95%     | ok               |
|          30 | -18.11%  | 18.03%             | -29.13% |    -0.47 |       75 | 39.60%     | ok               |

## DASH-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 88.57%   | 33.19%             | -27.87% |     0.79 |       40 | 15.33%     | ok               |
|          40 | 51.55%   | 33.19%             | -31.16% |     0.6  |       46 | 22.22%     | ok               |
|          45 | 36.18%   | 33.19%             | -36.59% |     0.51 |       44 | 17.62%     | ok               |
|          35 | -41.45%  | 33.19%             | -63.23% |    -0.02 |       69 | 26.63%     | ok               |
|          25 | -46.77%  | 33.19%             | -64.14% |    -0.08 |       69 | 32.76%     | ok               |

## DBC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -6.96%   | 30.67%             | -26.53% |    -0.18 |       72 | 38.77%     | ok               |
|          50 | -6.80%   | 30.67%             | -20.31% |    -0.24 |       42 | 21.30%     | ok               |
|          35 | -9.49%   | 30.67%             | -23.35% |    -0.31 |       62 | 31.95%     | ok               |
|          25 | -9.94%   | 30.67%             | -25.55% |    -0.31 |       62 | 35.11%     | ok               |
|          45 | -9.38%   | 30.67%             | -21.46% |    -0.33 |       58 | 24.96%     | ok               |

## DE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -6.07%   | 63.52%             | -22.53% |    -0.08 |       70 | 32.45%     | ok               |
|          30 | -8.54%   | 63.52%             | -25.24% |    -0.09 |       72 | 47.59%     | ok               |
|          20 | -8.92%   | 63.52%             | -29.90% |    -0.09 |       74 | 52.75%     | ok               |
|          45 | -8.00%   | 63.52%             | -26.22% |    -0.11 |       70 | 36.94%     | ok               |
|          25 | -11.18%  | 63.52%             | -27.66% |    -0.15 |       76 | 50.08%     | ok               |

## DIA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -0.71%   | 36.04%             | -11.28% |     0    |       60 | 45.26%     | ok               |
|          35 | -1.16%   | 36.04%             | -13.15% |    -0.03 |       62 | 42.10%     | ok               |
|          30 | -2.24%   | 36.04%             | -12.94% |    -0.08 |       60 | 44.09%     | ok               |
|          20 | -4.11%   | 36.04%             | -13.85% |    -0.18 |       64 | 47.59%     | ok               |
|          40 | -5.19%   | 36.04%             | -15.06% |    -0.27 |       68 | 39.27%     | ok               |

## DIS Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 17.83%   | -12.40%            | -14.24% |     0.57 |       50 | 27.95%     | ok               |
|          40 | -7.63%   | -12.40%            | -22.77% |    -0.09 |       65 | 36.77%     | ok               |
|          45 | -6.79%   | -12.40%            | -16.54% |    -0.09 |       53 | 31.61%     | ok               |
|          15 | -15.95%  | -12.40%            | -31.15% |    -0.22 |       89 | 57.24%     | ok               |
|          35 | -13.76%  | -12.40%            | -25.70% |    -0.22 |       75 | 42.93%     | ok               |

## DOGE-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 1.85%    | -70.33%            | -57.89% |     0.3  |       81 | 66.86%     | ok               |
|          25 | -10.46%  | -70.33%            | -53.72% |     0.17 |       70 | 55.94%     | ok               |
|          20 | -12.91%  | -70.33%            | -55.83% |     0.15 |       82 | 61.11%     | ok               |
|          30 | -25.08%  | -70.33%            | -60.95% |    -0.01 |       73 | 50.38%     | ok               |
|          35 | -50.94%  | -70.33%            | -63.16% |    -0.49 |       70 | 43.68%     | ok               |

## DOT-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -32.99%  | -82.13%            | -46.17% |    -0.41 |       56 | 25.29%     | ok               |
|          45 | -36.71%  | -82.13%            | -52.51% |    -0.44 |       50 | 30.27%     | ok               |
|          35 | -55.28%  | -82.13%            | -61.83% |    -0.57 |       78 | 41.00%     | ok               |
|          20 | -62.26%  | -82.13%            | -65.30% |    -0.63 |       94 | 60.34%     | ok               |
|          40 | -48.03%  | -82.13%            | -52.18% |    -0.64 |       54 | 33.52%     | ok               |

## DXY-INDEX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -1.23%   | -0.53%             | -6.02%  |    -0.18 |       38 | 31.02%     | ok               |
|          15 | -3.29%   | -0.53%             | -11.37% |    -0.28 |       82 | 77.01%     | ok               |
|          40 | -4.94%   | -0.53%             | -8.08%  |    -0.62 |       76 | 50.76%     | ok               |
|          25 | -5.86%   | -0.53%             | -12.10% |    -0.63 |       78 | 67.25%     | ok               |
|          30 | -5.59%   | -0.53%             | -10.26% |    -0.64 |       70 | 62.26%     | ok               |

## EEM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -4.96%   | 63.60%             | -19.52% |    -0.11 |       64 | 39.77%     | ok               |
|          35 | -5.62%   | 63.60%             | -23.88% |    -0.12 |       66 | 41.76%     | ok               |
|          50 | -4.94%   | 63.60%             | -15.88% |    -0.12 |       52 | 35.77%     | ok               |
|          45 | -6.04%   | 63.60%             | -17.36% |    -0.16 |       54 | 37.44%     | ok               |
|          30 | -9.40%   | 63.60%             | -25.67% |    -0.25 |       64 | 43.43%     | ok               |

## EFA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -3.05%   | 36.11%             | -10.80% |    -0.05 |       62 | 52.41%     | ok               |
|          30 | -7.42%   | 36.11%             | -13.02% |    -0.26 |       60 | 44.26%     | ok               |
|          20 | -9.78%   | 36.11%             | -12.73% |    -0.34 |       69 | 49.42%     | ok               |
|          40 | -8.83%   | 36.11%             | -14.90% |    -0.35 |       64 | 40.43%     | ok               |
|          50 | -9.07%   | 36.11%             | -17.56% |    -0.4  |       54 | 36.27%     | ok               |

## EOG Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -18.46%  | 21.99%             | -39.69% |    -0.41 |       58 | 32.95%     | ok               |
|          30 | -23.18%  | 21.99%             | -48.13% |    -0.48 |       81 | 46.76%     | ok               |
|          35 | -24.03%  | 21.99%             | -46.26% |    -0.55 |       79 | 41.43%     | ok               |
|          40 | -23.28%  | 21.99%             | -43.26% |    -0.55 |       66 | 36.27%     | ok               |
|          25 | -27.08%  | 21.99%             | -51.99% |    -0.56 |       82 | 49.75%     | ok               |

## ETC-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -5.49%   | -65.26%            | -27.89% |     0.03 |       28 | 16.48%     | ok               |
|          35 | -12.78%  | -65.26%            | -42.62% |    -0.07 |       44 | 26.44%     | ok               |
|          45 | -13.84%  | -65.26%            | -35.44% |    -0.12 |       26 | 18.39%     | ok               |
|          40 | -18.95%  | -65.26%            | -40.48% |    -0.22 |       42 | 22.22%     | ok               |
|          30 | -33.98%  | -65.26%            | -46.54% |    -0.47 |       64 | 30.65%     | ok               |

## ETH-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 134.73%  | -28.92%            | -30.11% |     1.17 |       66 | 45.02%     | ok               |
|          30 | 101.10%  | -28.92%            | -32.89% |     0.97 |       68 | 53.64%     | ok               |
|          15 | 37.65%   | -28.92%            | -42.74% |     0.56 |       77 | 68.77%     | ok               |
|          40 | 34.16%   | -28.92%            | -33.11% |     0.56 |       64 | 36.97%     | ok               |
|          20 | 36.18%   | -28.92%            | -39.10% |     0.55 |       82 | 63.03%     | ok               |

## EWJ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -18.16%  | 38.22%             | -30.73% |    -0.59 |       62 | 39.10%     | ok               |
|          20 | -19.55%  | 38.22%             | -31.32% |    -0.62 |       58 | 41.10%     | ok               |
|          45 | -18.94%  | 38.22%             | -27.68% |    -0.72 |       58 | 31.28%     | ok               |
|          25 | -21.87%  | 38.22%             | -31.18% |    -0.72 |       58 | 40.10%     | ok               |
|          35 | -22.08%  | 38.22%             | -32.54% |    -0.75 |       68 | 37.44%     | ok               |

## FCX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -4.31%   | 62.43%             | -27.70% |     0.06 |       52 | 29.78%     | ok               |
|          45 | -8.44%   | 62.43%             | -35.18% |    -0    |       52 | 34.28%     | ok               |
|          40 | -19.35%  | 62.43%             | -43.57% |    -0.19 |       62 | 38.60%     | ok               |
|          30 | -27.81%  | 62.43%             | -47.47% |    -0.31 |       63 | 45.26%     | ok               |
|          35 | -32.25%  | 62.43%             | -50.71% |    -0.42 |       69 | 43.43%     | ok               |

## FET-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -4.69%   | -79.10%            | -59.54% |     0.28 |       88 | 51.92%     | ok               |
|          15 | -18.93%  | -79.10%            | -59.58% |     0.17 |       84 | 55.75%     | ok               |
|          25 | -37.64%  | -79.10%            | -60.09% |    -0.09 |       91 | 45.59%     | ok               |
|          30 | -39.93%  | -79.10%            | -54.02% |    -0.15 |       83 | 41.38%     | ok               |
|          35 | -53.63%  | -79.10%            | -62.73% |    -0.5  |       69 | 33.72%     | ok               |

## FIL-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -24.59%  | -76.45%            | -39.40% |    -0.23 |       48 | 23.18%     | ok               |
|          35 | -43.92%  | -76.45%            | -47.50% |    -0.59 |       58 | 27.39%     | ok               |
|          30 | -46.58%  | -76.45%            | -50.22% |    -0.6  |       70 | 32.95%     | ok               |
|          45 | -39.88%  | -76.45%            | -43.98% |    -0.61 |       42 | 17.24%     | ok               |
|          50 | -39.00%  | -76.45%            | -44.95% |    -0.69 |       36 | 12.64%     | ok               |

## FXI Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -6.30%   | 47.34%             | -22.57% |    -0.07 |       44 | 31.28%     | ok               |
|          30 | -6.84%   | 47.34%             | -23.91% |    -0.09 |       44 | 30.12%     | ok               |
|          45 | -6.49%   | 47.34%             | -26.75% |    -0.09 |       44 | 24.63%     | ok               |
|          15 | -9.00%   | 47.34%             | -21.68% |    -0.13 |       52 | 34.78%     | ok               |
|          20 | -10.08%  | 47.34%             | -24.53% |    -0.16 |       50 | 32.45%     | ok               |

## GDX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 18.06%   | 177.44%            | -35.59% |     0.39 |       73 | 52.91%     | ok               |
|          40 | 13.85%   | 177.44%            | -31.87% |     0.35 |       64 | 42.93%     | ok               |
|          30 | 11.28%   | 177.44%            | -34.99% |     0.3  |       60 | 48.09%     | ok               |
|          35 | 8.95%    | 177.44%            | -32.37% |     0.27 |       68 | 45.26%     | ok               |
|          25 | 6.77%    | 177.44%            | -38.90% |     0.24 |       63 | 49.75%     | ok               |

## GDXJ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -7.90%   | 203.42%            | -45.05% |     0.06 |       67 | 53.24%     | ok               |
|          30 | -23.13%  | 203.42%            | -44.93% |    -0.22 |       68 | 46.42%     | ok               |
|          50 | -20.22%  | 203.42%            | -44.94% |    -0.22 |       58 | 37.77%     | ok               |
|          25 | -26.54%  | 203.42%            | -47.26% |    -0.25 |       72 | 49.92%     | ok               |
|          35 | -26.76%  | 203.42%            | -43.49% |    -0.3  |       70 | 44.09%     | ok               |

## GE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 32.77%   | 198.23%            | -22.29% |     0.65 |       66 | 40.10%     | ok               |
|          45 | 22.75%   | 198.23%            | -25.68% |     0.49 |       74 | 42.93%     | ok               |
|          20 | 16.29%   | 198.23%            | -26.63% |     0.38 |       71 | 57.24%     | ok               |
|          35 | 12.90%   | 198.23%            | -27.11% |     0.33 |       80 | 48.42%     | ok               |
|          30 | 12.65%   | 198.23%            | -27.82% |     0.33 |       76 | 53.58%     | ok               |

## GLD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | 33.43%   | 98.51%             | -14.61% |     0.79 |       46 | 48.59%     | ok               |
|          20 | 31.44%   | 98.51%             | -14.61% |     0.75 |       48 | 49.92%     | ok               |
|          30 | 27.07%   | 98.51%             | -16.63% |     0.67 |       48 | 47.42%     | ok               |
|          15 | 23.39%   | 98.51%             | -17.54% |     0.57 |       50 | 54.08%     | ok               |
|          35 | 17.12%   | 98.51%             | -17.29% |     0.48 |       54 | 46.09%     | ok               |

## GOOGL Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | 81.59%   | 154.75%            | -19.76% |     1.19 |       55 | 55.41%     | ok               |
|          30 | 76.69%   | 154.75%            | -20.41% |     1.15 |       61 | 52.91%     | ok               |
|          20 | 67.87%   | 154.75%            | -20.57% |     1.04 |       66 | 57.74%     | ok               |
|          35 | 59.50%   | 154.75%            | -22.85% |     1.03 |       69 | 47.75%     | ok               |
|          15 | 68.78%   | 154.75%            | -13.81% |     1.01 |       69 | 62.73%     | ok               |

## GRT-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 16.20%   | -86.56%            | -35.66% |     0.39 |       42 | 21.46%     | ok               |
|          15 | -3.17%   | -86.56%            | -49.67% |     0.22 |       73 | 61.30%     | ok               |
|          45 | 2.68%    | -86.56%            | -46.59% |     0.21 |       48 | 26.82%     | ok               |
|          35 | -1.50%   | -86.56%            | -48.22% |     0.18 |       58 | 35.63%     | ok               |
|          20 | -6.53%   | -86.56%            | -46.47% |     0.18 |       81 | 55.75%     | ok               |

## GS Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 21.11%   | 196.47%            | -20.56% |     0.47 |       74 | 61.06%     | ok               |
|          20 | 4.59%    | 196.47%            | -23.19% |     0.19 |       74 | 57.07%     | ok               |
|          40 | 0.08%    | 196.47%            | -17.88% |     0.09 |       72 | 45.26%     | ok               |
|          25 | -0.70%   | 196.47%            | -23.32% |     0.09 |       74 | 54.58%     | ok               |
|          30 | -2.38%   | 196.47%            | -22.13% |     0.05 |       76 | 52.08%     | ok               |

## HD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -7.53%   | -6.85%             | -17.69% |    -0.12 |       71 | 44.59%     | ok               |
|          25 | -8.25%   | -6.85%             | -18.51% |    -0.14 |       70 | 46.59%     | ok               |
|          15 | -17.46%  | -6.85%             | -27.27% |    -0.37 |      109 | 55.41%     | ok               |
|          35 | -15.13%  | -6.85%             | -22.98% |    -0.38 |       80 | 40.43%     | ok               |
|          40 | -13.89%  | -6.85%             | -19.63% |    -0.39 |       84 | 34.11%     | ok               |

## HON Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -13.43%  | 13.24%             | -21.17% |    -0.4  |       72 | 31.78%     | ok               |
|          45 | -15.16%  | 13.24%             | -19.99% |    -0.43 |       74 | 36.77%     | ok               |
|          40 | -23.52%  | 13.24%             | -26.29% |    -0.66 |       76 | 41.10%     | ok               |
|          35 | -24.98%  | 13.24%             | -27.37% |    -0.69 |       91 | 47.42%     | ok               |
|          30 | -26.82%  | 13.24%             | -29.80% |    -0.72 |       93 | 52.41%     | ok               |

## HYG Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -7.98%   | 3.39%              | -7.98%  |    -0.96 |       70 | 29.28%     | ok               |
|          15 | -9.49%   | 3.39%              | -10.34% |    -1.03 |       88 | 40.93%     | ok               |
|          20 | -9.23%   | 3.39%              | -10.34% |    -1.03 |       86 | 38.77%     | ok               |
|          25 | -9.38%   | 3.39%              | -10.11% |    -1.06 |       83 | 36.61%     | ok               |
|          30 | -9.08%   | 3.39%              | -9.59%  |    -1.06 |       81 | 33.94%     | ok               |

## IBIT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 53.73%   | -3.76%             | -17.37% |     1.07 |       22 | 22.43%     | ok               |
|          15 | 56.91%   | -3.76%             | -19.20% |     0.95 |       40 | 39.95%     | ok               |
|          45 | 44.27%   | -3.76%             | -17.37% |     0.9  |       26 | 23.83%     | ok               |
|          40 | 38.04%   | -3.76%             | -17.78% |     0.81 |       26 | 25.70%     | ok               |
|          30 | 30.82%   | -3.76%             | -18.95% |     0.67 |       34 | 32.24%     | ok               |

## IBM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -10.07%  | 18.33%             | -42.66% |     0    |       92 | 61.90%     | ok               |
|          30 | -20.21%  | 18.33%             | -44.08% |    -0.21 |       78 | 49.58%     | ok               |
|          20 | -23.72%  | 18.33%             | -47.38% |    -0.25 |       76 | 54.24%     | ok               |
|          35 | -22.27%  | 18.33%             | -44.08% |    -0.26 |       72 | 45.26%     | ok               |
|          50 | -24.95%  | 18.33%             | -41.25% |    -0.35 |       52 | 32.78%     | ok               |

## ICP-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | -4.03%   | -68.56%            | -37.87% |     0.16 |       62 | 28.93%     | ok               |
|          30 | -15.33%  | -68.56%            | -51.29% |     0.1  |       77 | 35.06%     | ok               |
|          40 | -9.10%   | -68.56%            | -32.85% |     0.08 |       56 | 24.52%     | ok               |
|          50 | -19.75%  | -68.56%            | -43.65% |    -0.12 |       34 | 14.56%     | ok               |
|          20 | -45.39%  | -68.56%            | -58.71% |    -0.19 |       86 | 45.79%     | ok               |

## IEF Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -6.92%   | -0.37%             | -9.79%  |    -0.82 |       70 | 42.26%     | ok               |
|          15 | -7.48%   | -0.37%             | -10.52% |    -0.88 |       69 | 43.76%     | ok               |
|          40 | -8.39%   | -0.37%             | -9.67%  |    -1.31 |       60 | 24.79%     | ok               |
|          45 | -8.07%   | -0.37%             | -9.73%  |    -1.33 |       50 | 22.80%     | ok               |
|          25 | -10.50%  | -0.37%             | -11.19% |    -1.34 |       76 | 39.43%     | ok               |

## IEMG Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | -2.89%   | 57.77%             | -22.13% |    -0.04 |       63 | 41.93%     | ok               |
|          50 | -3.22%   | 57.77%             | -13.91% |    -0.07 |       54 | 33.61%     | ok               |
|          40 | -3.52%   | 57.77%             | -18.43% |    -0.07 |       60 | 39.43%     | ok               |
|          45 | -3.43%   | 57.77%             | -14.92% |    -0.07 |       50 | 36.27%     | ok               |
|          25 | -7.17%   | 57.77%             | -25.58% |    -0.18 |       59 | 44.76%     | ok               |

## INJ-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -16.04%  | -63.74%            | -56.91% |    -0.02 |       44 | 22.22%     | ok               |
|          35 | -25.06%  | -63.74%            | -61.19% |    -0.08 |       60 | 31.99%     | ok               |
|          50 | -25.16%  | -63.74%            | -52.76% |    -0.19 |       48 | 19.16%     | ok               |
|          40 | -33.63%  | -63.74%            | -59.56% |    -0.26 |       50 | 28.16%     | ok               |
|          20 | -52.25%  | -63.74%            | -80.49% |    -0.39 |       78 | 46.55%     | ok               |

## INTC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 93.40%   | 142.05%            | -53.65% |     0.78 |       79 | 60.07%     | ok               |
|          45 | 76.11%   | 142.05%            | -49.32% |     0.74 |       60 | 34.28%     | ok               |
|          20 | 80.58%   | 142.05%            | -52.47% |     0.73 |       78 | 56.24%     | ok               |
|          25 | 75.50%   | 142.05%            | -56.41% |     0.72 |       75 | 51.58%     | ok               |
|          40 | 70.33%   | 142.05%            | -55.86% |     0.7  |       68 | 38.60%     | ok               |

## INTU Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 1.32%    | -56.27%            | -39.78% |     0.14 |       69 | 28.12%     | ok               |
|          45 | -0.66%   | -56.27%            | -40.83% |     0.11 |       67 | 32.11%     | ok               |
|          40 | -8.64%   | -56.27%            | -45.15% |    -0.04 |       67 | 34.94%     | ok               |
|          35 | -15.62%  | -56.27%            | -46.75% |    -0.16 |       71 | 38.44%     | ok               |
|          25 | -19.50%  | -56.27%            | -39.89% |    -0.22 |       70 | 44.43%     | ok               |

## ITA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 0.42%    | 87.57%             | -25.76% |     0.1  |       85 | 59.90%     | ok               |
|          50 | 0.81%    | 87.57%             | -21.48% |     0.09 |       76 | 38.44%     | ok               |
|          30 | -2.69%   | 87.57%             | -23.75% |    -0    |       72 | 48.42%     | ok               |
|          35 | -4.76%   | 87.57%             | -23.16% |    -0.07 |       76 | 46.76%     | ok               |
|          40 | -5.85%   | 87.57%             | -20.58% |    -0.11 |       78 | 43.26%     | ok               |

## IWM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | 9.59%    | 48.08%             | -13.48% |     0.39 |       50 | 37.10%     | ok               |
|          40 | 8.60%    | 48.08%             | -14.08% |     0.39 |       42 | 31.28%     | ok               |
|          30 | 9.40%    | 48.08%             | -12.83% |     0.39 |       48 | 35.77%     | ok               |
|          35 | 8.35%    | 48.08%             | -14.11% |     0.36 |       48 | 33.61%     | ok               |
|          20 | 5.27%    | 48.08%             | -14.01% |     0.24 |       60 | 38.10%     | ok               |

## JNJ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 22.43%   | 60.81%             | -10.57% |     0.89 |       54 | 37.77%     | ok               |
|          45 | 13.69%   | 60.81%             | -13.35% |     0.56 |       54 | 42.60%     | ok               |
|          15 | 15.47%   | 60.81%             | -18.02% |     0.53 |       64 | 57.07%     | ok               |
|          40 | 11.20%   | 60.81%             | -14.77% |     0.46 |       60 | 46.76%     | ok               |
|          20 | 11.55%   | 60.81%             | -17.61% |     0.43 |       68 | 53.74%     | ok               |

## JPM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 17.63%   | 90.78%             | -15.90% |     0.59 |       52 | 40.93%     | ok               |
|          45 | 6.45%    | 90.78%             | -21.91% |     0.26 |       54 | 43.93%     | ok               |
|          40 | -7.61%   | 90.78%             | -28.47% |    -0.14 |       66 | 46.42%     | ok               |
|          20 | -11.66%  | 90.78%             | -33.59% |    -0.17 |       86 | 58.57%     | ok               |
|          35 | -13.06%  | 90.78%             | -27.43% |    -0.29 |       74 | 50.42%     | ok               |

## KO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 28.93%   | 36.87%             | -8.07%  |     1.03 |       49 | 37.77%     | ok               |
|          35 | 24.98%   | 36.87%             | -8.07%  |     0.93 |       52 | 36.44%     | ok               |
|          40 | 22.37%   | 36.87%             | -9.28%  |     0.9  |       54 | 33.28%     | ok               |
|          25 | 23.60%   | 36.87%             | -9.37%  |     0.86 |       55 | 40.43%     | ok               |
|          50 | 14.81%   | 36.87%             | -11.40% |     0.68 |       36 | 26.79%     | ok               |

## LDO-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 36.62%   | -78.29%            | -46.95% |     0.55 |       83 | 52.87%     | ok               |
|          20 | 25.27%   | -78.29%            | -47.34% |     0.48 |       87 | 48.28%     | ok               |
|          50 | 16.79%   | -78.29%            | -48.04% |     0.39 |       50 | 17.24%     | ok               |
|          30 | 8.66%    | -78.29%            | -62.63% |     0.35 |       78 | 39.46%     | ok               |
|          35 | 6.17%    | -78.29%            | -64.26% |     0.31 |       78 | 32.57%     | ok               |

## LIN Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 1.87%    | 19.86%             | -23.70% |     0.13 |       63 | 50.08%     | ok               |
|          25 | 1.62%    | 19.86%             | -22.01% |     0.12 |       63 | 42.26%     | ok               |
|          20 | -0.56%   | 19.86%             | -23.00% |     0.04 |       62 | 45.42%     | ok               |
|          35 | -2.05%   | 19.86%             | -21.18% |    -0.02 |       62 | 32.95%     | ok               |
|          30 | -2.67%   | 19.86%             | -21.53% |    -0.03 |       66 | 39.43%     | ok               |

## LINK-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -16.53%  | -54.68%            | -49.35% |     0.06 |       73 | 42.15%     | ok               |
|          45 | -13.28%  | -54.68%            | -38.11% |     0.05 |       50 | 26.63%     | ok               |
|          50 | -12.86%  | -54.68%            | -36.52% |     0.03 |       40 | 21.26%     | ok               |
|          35 | -24.33%  | -54.68%            | -49.18% |    -0.05 |       59 | 36.78%     | ok               |
|          40 | -28.49%  | -54.68%            | -50.55% |    -0.14 |       55 | 31.03%     | ok               |

## LLY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 6.98%    | 52.52%             | -38.23% |     0.24 |       46 | 37.10%     | ok               |
|          15 | -2.53%   | 52.52%             | -48.12% |     0.1  |       63 | 60.57%     | ok               |
|          45 | -5.06%   | 52.52%             | -42.66% |     0.02 |       54 | 40.60%     | ok               |
|          20 | -18.22%  | 52.52%             | -51.34% |    -0.18 |       72 | 55.57%     | ok               |
|          25 | -19.57%  | 52.52%             | -53.47% |    -0.21 |       68 | 52.91%     | ok               |

## LRCX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -6.73%   | 284.37%            | -60.45% |     0.12 |       83 | 54.58%     | ok               |
|          50 | -11.80%  | 284.37%            | -50.39% |     0.01 |       80 | 36.27%     | ok               |
|          40 | -14.45%  | 284.37%            | -56.86% |    -0    |       72 | 42.10%     | ok               |
|          35 | -20.00%  | 284.37%            | -61.76% |    -0.07 |       80 | 44.09%     | ok               |
|          20 | -22.59%  | 284.37%            | -67.64% |    -0.09 |       87 | 50.25%     | ok               |

## LTC-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -12.22%  | -58.18%            | -44.78% |    -0    |       56 | 31.80%     | ok               |
|          35 | -22.47%  | -58.18%            | -54.86% |    -0.13 |       66 | 42.91%     | ok               |
|          40 | -31.40%  | -58.18%            | -56.10% |    -0.3  |       58 | 38.12%     | ok               |
|          30 | -36.00%  | -58.18%            | -53.76% |    -0.33 |       70 | 49.04%     | ok               |
|          50 | -29.78%  | -58.18%            | -46.29% |    -0.36 |       54 | 23.95%     | ok               |

## MCD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 2.85%    | -8.10%             | -9.22%  |     0.19 |       42 | 20.63%     | ok               |
|          30 | -2.55%   | -8.10%             | -18.81% |    -0.05 |       75 | 38.10%     | ok               |
|          25 | -3.59%   | -8.10%             | -20.47% |    -0.09 |       75 | 40.77%     | ok               |
|          35 | -7.68%   | -8.10%             | -15.45% |    -0.29 |       67 | 34.44%     | ok               |
|          40 | -7.95%   | -8.10%             | -16.86% |    -0.33 |       71 | 28.79%     | ok               |

## META Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -8.95%   | 40.13%             | -31.03% |    -0.08 |       66 | 37.44%     | ok               |
|          40 | -18.96%  | 40.13%             | -35.11% |    -0.29 |       66 | 40.43%     | ok               |
|          25 | -26.95%  | 40.13%             | -39.84% |    -0.43 |       67 | 51.08%     | ok               |
|          50 | -22.85%  | 40.13%             | -34.00% |    -0.43 |       70 | 33.61%     | ok               |
|          30 | -28.91%  | 40.13%             | -38.96% |    -0.49 |       72 | 47.92%     | ok               |

## MPC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 24.24%   | 84.67%             | -23.96% |     0.53 |       52 | 37.44%     | ok               |
|          45 | 16.36%   | 84.67%             | -25.09% |     0.4  |       58 | 41.10%     | ok               |
|          40 | 14.59%   | 84.67%             | -25.70% |     0.37 |       60 | 43.43%     | ok               |
|          35 | 11.05%   | 84.67%             | -35.90% |     0.31 |       68 | 45.92%     | ok               |
|          30 | -6.42%   | 84.67%             | -44.76% |     0.01 |       71 | 48.75%     | ok               |

## MRK Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -23.56%  | -5.17%             | -30.12% |    -0.46 |       89 | 55.24%     | ok               |
|          25 | -23.19%  | -5.17%             | -31.07% |    -0.49 |       74 | 47.25%     | ok               |
|          20 | -26.95%  | -5.17%             | -29.59% |    -0.59 |       79 | 50.58%     | ok               |
|          45 | -25.92%  | -5.17%             | -27.70% |    -0.71 |       59 | 33.44%     | ok               |
|          50 | -25.88%  | -5.17%             | -27.66% |    -0.76 |       58 | 30.28%     | ok               |

## MS Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -3.32%   | 166.75%            | -19.99% |     0    |       72 | 41.43%     | ok               |
|          15 | -5.59%   | 166.75%            | -22.02% |    -0.02 |       75 | 58.57%     | ok               |
|          20 | -5.71%   | 166.75%            | -25.68% |    -0.04 |       79 | 54.74%     | ok               |
|          30 | -10.35%  | 166.75%            | -27.79% |    -0.17 |       79 | 49.75%     | ok               |
|          35 | -10.11%  | 166.75%            | -25.26% |    -0.17 |       78 | 46.09%     | ok               |

## MSFT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -22.13%  | -4.43%             | -25.26% |    -0.62 |       66 | 34.11%     | ok               |
|          50 | -23.55%  | -4.43%             | -26.14% |    -0.69 |       62 | 29.12%     | ok               |
|          35 | -34.48%  | -4.43%             | -35.38% |    -0.93 |       73 | 42.76%     | ok               |
|          40 | -33.86%  | -4.43%             | -34.77% |    -0.95 |       69 | 37.60%     | ok               |
|          25 | -37.88%  | -4.43%             | -40.21% |    -0.98 |       87 | 50.58%     | ok               |

## MU Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 443.99%  | 1118.09%           | -61.96% |     1.59 |       45 | 67.22%     | ok               |
|          25 | 357.11%  | 1118.09%           | -67.90% |     1.51 |       47 | 61.56%     | ok               |
|          20 | 313.39%  | 1118.09%           | -67.25% |     1.4  |       51 | 63.23%     | ok               |
|          40 | 290.77%  | 1118.09%           | -64.07% |     1.4  |       56 | 55.24%     | ok               |
|          30 | 270.20%  | 1118.09%           | -68.76% |     1.34 |       51 | 59.90%     | ok               |

## NEAR-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 73.04%   | -36.58%            | -45.84% |     0.83 |       42 | 22.99%     | ok               |
|          50 | 45.50%   | -36.58%            | -51.20% |     0.65 |       38 | 18.01%     | ok               |
|          40 | 37.07%   | -36.58%            | -54.53% |     0.56 |       46 | 27.39%     | ok               |
|          35 | 13.88%   | -36.58%            | -58.86% |     0.37 |       68 | 32.76%     | ok               |
|          15 | -16.59%  | -36.58%            | -54.94% |     0.14 |       87 | 55.56%     | ok               |

## NEM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 14.87%   | 185.48%            | -29.41% |     0.34 |       60 | 62.40%     | ok               |
|          20 | 5.12%    | 185.48%            | -30.47% |     0.23 |       70 | 58.24%     | ok               |
|          25 | -14.41%  | 185.48%            | -37.89% |    -0.04 |       66 | 56.07%     | ok               |
|          50 | -13.83%  | 185.48%            | -33.36% |    -0.07 |       60 | 41.43%     | ok               |
|          30 | -27.67%  | 185.48%            | -38.49% |    -0.27 |       72 | 53.91%     | ok               |

## NFLX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 50.11%   | 27.85%             | -11.94% |     1.03 |       46 | 46.09%     | ok               |
|          50 | 44.16%   | 27.85%             | -16.28% |     1    |       46 | 38.44%     | ok               |
|          35 | 42.40%   | 27.85%             | -18.30% |     0.87 |       60 | 49.58%     | ok               |
|          45 | 33.88%   | 27.85%             | -15.48% |     0.78 |       52 | 42.43%     | ok               |
|          25 | 36.04%   | 27.85%             | -21.09% |     0.74 |       62 | 56.91%     | ok               |

## NKE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | -27.03%  | -58.51%            | -42.13% |    -0.38 |       75 | 37.44%     | ok               |
|          20 | -33.86%  | -58.51%            | -50.44% |    -0.42 |       93 | 52.58%     | ok               |
|          25 | -34.08%  | -58.51%            | -51.20% |    -0.44 |       89 | 48.75%     | ok               |
|          15 | -38.05%  | -58.51%            | -55.28% |    -0.5  |       90 | 57.07%     | ok               |
|          40 | -26.61%  | -58.51%            | -31.33% |    -0.51 |       65 | 30.28%     | ok               |

## NOW Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 8.45%    | -30.36%            | -26.36% |     0.27 |       81 | 52.08%     | ok               |
|          30 | 4.35%    | -30.36%            | -28.87% |     0.22 |       84 | 45.76%     | ok               |
|          15 | 2.82%    | -30.36%            | -26.36% |     0.21 |       92 | 55.07%     | ok               |
|          25 | -1.37%   | -30.36%            | -27.26% |     0.15 |       76 | 49.42%     | ok               |
|          40 | -0.36%   | -30.36%            | -30.87% |     0.13 |       68 | 34.78%     | ok               |

## NVDA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -5.54%   | 152.04%            | -35.26% |     0.08 |       74 | 47.95%     | ok               |
|          20 | -11.04%  | 152.04%            | -40.59% |     0.03 |       70 | 55.97%     | ok               |
|          25 | -10.90%  | 152.04%            | -33.22% |     0.01 |       71 | 50.98%     | ok               |
|          50 | -14.29%  | 152.04%            | -40.84% |    -0.11 |       56 | 32.09%     | ok               |
|          15 | -23.69%  | 152.04%            | -45.02% |    -0.14 |       75 | 59.36%     | ok               |

## OP-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 27.06%   | -90.60%            | -36.11% |     0.51 |       30 | 11.11%     | ok               |
|          45 | 26.15%   | -90.60%            | -45.76% |     0.48 |       32 | 15.71%     | ok               |
|          40 | 3.68%    | -90.60%            | -53.61% |     0.25 |       48 | 24.33%     | ok               |
|          35 | -13.71%  | -90.60%            | -58.33% |     0.05 |       56 | 27.39%     | ok               |
|          30 | -29.45%  | -90.60%            | -70.27% |    -0.11 |       72 | 33.91%     | ok               |

## ORCL Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 239.03%  | 17.97%             | -29.32% |     1.37 |       72 | 65.56%     | ok               |
|          25 | 154.33%  | 17.97%             | -27.76% |     1.11 |       73 | 58.07%     | ok               |
|          20 | 149.96%  | 17.97%             | -29.32% |     1.09 |       75 | 61.23%     | ok               |
|          35 | 116.33%  | 17.97%             | -31.95% |     0.98 |       66 | 50.08%     | ok               |
|          30 | 116.52%  | 17.97%             | -29.47% |     0.97 |       72 | 54.24%     | ok               |

## OXY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 5.19%    | -8.38%             | -29.75% |     0.21 |       42 | 28.45%     | ok               |
|          35 | 2.46%    | -8.38%             | -30.04% |     0.16 |       70 | 40.10%     | ok               |
|          30 | -0.03%   | -8.38%             | -34.15% |     0.12 |       71 | 45.42%     | ok               |
|          40 | 0.39%    | -8.38%             | -31.45% |     0.12 |       56 | 35.77%     | ok               |
|          45 | -7.23%   | -8.38%             | -34.99% |    -0.05 |       48 | 30.78%     | ok               |

## PEP Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 12.74%   | -19.69%            | -11.62% |     0.57 |       44 | 27.29%     | ok               |
|          45 | 4.63%    | -19.69%            | -14.22% |     0.24 |       62 | 31.45%     | ok               |
|          40 | 0.85%    | -19.69%            | -18.04% |     0.09 |       72 | 37.10%     | ok               |
|          35 | 0.33%    | -19.69%            | -21.42% |     0.08 |       81 | 41.93%     | ok               |
|          30 | -5.52%   | -19.69%            | -21.35% |    -0.1  |       79 | 48.59%     | ok               |

## PEPE-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 0.11%    | -70.77%            | -57.66% |     0.28 |       79 | 44.83%     | ok               |
|          15 | -7.66%   | -70.77%            | -64.84% |     0.28 |       82 | 61.11%     | ok               |
|          35 | -5.60%   | -70.77%            | -51.35% |     0.2  |       64 | 39.46%     | ok               |
|          25 | -16.40%  | -70.77%            | -53.88% |     0.13 |       89 | 50.57%     | ok               |
|          20 | -28.01%  | -70.77%            | -64.07% |     0.04 |       88 | 57.47%     | ok               |

## PFE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -24.91%  | -12.11%            | -26.10% |    -0.94 |       52 | 18.97%     | ok               |
|          50 | -26.23%  | -12.11%            | -27.28% |    -1.12 |       38 | 15.31%     | ok               |
|          40 | -31.91%  | -12.11%            | -33.01% |    -1.16 |       74 | 23.96%     | ok               |
|          35 | -35.52%  | -12.11%            | -37.03% |    -1.19 |       86 | 31.78%     | ok               |
|          30 | -40.08%  | -12.11%            | -41.48% |    -1.29 |       79 | 35.94%     | ok               |

## PG Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -7.35%   | -7.84%             | -20.08% |    -0.26 |       58 | 33.78%     | ok               |
|          35 | -10.51%  | -7.84%             | -18.99% |    -0.38 |       66 | 37.27%     | ok               |
|          30 | -18.64%  | -7.84%             | -24.55% |    -0.7  |       68 | 40.43%     | ok               |
|          45 | -16.40%  | -7.84%             | -22.43% |    -0.7  |       58 | 31.28%     | ok               |
|          25 | -20.50%  | -7.84%             | -26.24% |    -0.78 |       80 | 41.93%     | ok               |

## PM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | -1.38%   | 96.29%             | -32.20% |     0.06 |       88 | 52.25%     | ok               |
|          20 | -4.52%   | 96.29%             | -31.89% |     0    |       89 | 61.06%     | ok               |
|          30 | -4.28%   | 96.29%             | -33.68% |     0    |       85 | 55.91%     | ok               |
|          50 | -6.95%   | 96.29%             | -35.70% |    -0.09 |       74 | 42.10%     | ok               |
|          40 | -9.33%   | 96.29%             | -37.94% |    -0.14 |       82 | 48.42%     | ok               |

## POL-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 40.66%   | -72.21%            | -46.45% |     0.6  |       77 | 46.74%     | ok               |
|          25 | 26.15%   | -72.21%            | -46.72% |     0.47 |       68 | 54.79%     | ok               |
|          20 | 15.13%   | -72.21%            | -52.88% |     0.38 |       78 | 60.15%     | ok               |
|          15 | -7.61%   | -72.21%            | -58.42% |     0.16 |       78 | 65.90%     | ok               |
|          50 | -1.75%   | -72.21%            | -22.81% |     0.1  |       50 | 18.77%     | ok               |

## QCOM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -3.88%   | 17.20%             | -54.50% |     0.12 |       71 | 47.75%     | ok               |
|          35 | -4.42%   | 17.20%             | -50.58% |     0.11 |       77 | 43.59%     | ok               |
|          20 | -7.78%   | 17.20%             | -54.38% |     0.08 |       67 | 50.58%     | ok               |
|          30 | -15.25%  | 17.20%             | -56.59% |    -0.04 |       73 | 46.09%     | ok               |
|          15 | -23.11%  | 17.20%             | -57.94% |    -0.13 |       71 | 53.74%     | ok               |

## QQQ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | 23.31%   | 68.42%             | -12.88% |     0.63 |       59 | 46.92%     | ok               |
|          15 | 23.85%   | 68.42%             | -14.17% |     0.6  |       63 | 52.41%     | ok               |
|          20 | 20.33%   | 68.42%             | -12.98% |     0.55 |       67 | 49.58%     | ok               |
|          30 | 18.25%   | 68.42%             | -12.88% |     0.53 |       64 | 43.93%     | ok               |
|          35 | 6.17%    | 68.42%             | -19.00% |     0.25 |       70 | 40.27%     | ok               |

## RENDER-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 45.25%   | -63.20%            | -43.43% |     0.61 |       88 | 53.92%     | ok               |
|          15 | 34.05%   | -63.20%            | -44.59% |     0.55 |       88 | 57.25%     | ok               |
|          25 | 15.90%   | -63.20%            | -40.60% |     0.42 |       90 | 49.61%     | ok               |
|          30 | -19.07%  | -63.20%            | -45.00% |     0.1  |       98 | 42.94%     | ok               |
|          35 | -31.74%  | -63.20%            | -41.33% |    -0.12 |       84 | 34.71%     | ok               |

## RTX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 30.99%   | 112.56%            | -18.66% |     0.72 |       76 | 56.07%     | ok               |
|          25 | 26.11%   | 112.56%            | -18.59% |     0.64 |       64 | 52.75%     | ok               |
|          50 | 20.82%   | 112.56%            | -18.42% |     0.63 |       54 | 41.93%     | ok               |
|          35 | 21.50%   | 112.56%            | -18.00% |     0.61 |       54 | 49.58%     | ok               |
|          30 | 24.20%   | 112.56%            | -16.99% |     0.61 |       58 | 51.58%     | ok               |

## SBUX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -13.65%  | 13.60%             | -23.55% |    -0.21 |       64 | 42.76%     | ok               |
|          40 | -16.66%  | 13.60%             | -25.43% |    -0.34 |       60 | 33.61%     | ok               |
|          45 | -16.20%  | 13.60%             | -27.26% |    -0.36 |       66 | 29.78%     | ok               |
|          30 | -22.19%  | 13.60%             | -29.22% |    -0.44 |       67 | 40.27%     | ok               |
|          35 | -22.98%  | 13.60%             | -28.00% |    -0.48 |       62 | 37.27%     | ok               |

## SCHW Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 9.22%    | 59.01%             | -16.53% |     0.33 |       56 | 34.78%     | ok               |
|          50 | 0.46%    | 59.01%             | -13.28% |     0.08 |       58 | 31.78%     | ok               |
|          25 | -1.07%   | 59.01%             | -28.76% |     0.07 |       61 | 49.75%     | ok               |
|          40 | -2.10%   | 59.01%             | -23.35% |     0.02 |       64 | 37.77%     | ok               |
|          20 | -5.24%   | 59.01%             | -29.24% |    -0.03 |       71 | 52.08%     | ok               |

## SHIB-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -14.53%  | -73.14%            | -49.21% |     0.08 |       80 | 68.77%     | ok               |
|          25 | -23.34%  | -73.14%            | -43.85% |    -0.06 |       77 | 59.00%     | ok               |
|          20 | -25.26%  | -73.14%            | -46.38% |    -0.07 |       81 | 63.79%     | ok               |
|          35 | -23.71%  | -73.14%            | -53.32% |    -0.12 |       66 | 45.59%     | ok               |
|          40 | -29.26%  | -73.14%            | -49.96% |    -0.24 |       56 | 37.93%     | ok               |

## SHY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd    |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:-------|---------:|---------:|:-----------|:-----------------|
|          35 | -2.36%   | 0.27%              | -3.27% |    -0.84 |       50 | 32.45%     | ok               |
|          30 | -2.39%   | 0.27%              | -2.85% |    -0.84 |       50 | 34.44%     | ok               |
|          40 | -2.47%   | 0.27%              | -3.33% |    -0.89 |       50 | 30.62%     | ok               |
|          45 | -2.45%   | 0.27%              | -3.23% |    -0.9  |       48 | 27.45%     | ok               |
|          50 | -2.62%   | 0.27%              | -3.40% |    -1.01 |       44 | 24.63%     | ok               |

## SKY-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -28.04%  | 6.09%              | -43.98% |    -0.33 |       72 | 40.18%     | ok               |
|          15 | -32.44%  | 6.09%              | -56.39% |    -0.33 |       62 | 50.11%     | ok               |
|          25 | -31.73%  | 6.09%              | -48.09% |    -0.39 |       67 | 43.71%     | ok               |
|          20 | -42.13%  | 6.09%              | -58.40% |    -0.57 |       64 | 47.24%     | ok               |
|          35 | -39.34%  | 6.09%              | -49.68% |    -0.67 |       66 | 34.00%     | ok               |

## SLB Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 20.91%   | -2.02%             | -21.46% |     0.51 |       52 | 33.44%     | ok               |
|          40 | 17.17%   | -2.02%             | -25.33% |     0.44 |       46 | 36.94%     | ok               |
|          50 | -0.69%   | -2.02%             | -29.64% |     0.07 |       50 | 28.95%     | ok               |
|          35 | -14.04%  | -2.02%             | -43.52% |    -0.19 |       76 | 44.59%     | ok               |
|          30 | -25.47%  | -2.02%             | -54.23% |    -0.43 |       75 | 51.08%     | ok               |

## SLV Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 65.90%   | 152.35%            | -34.72% |     0.84 |       54 | 34.94%     | ok               |
|          45 | 63.89%   | 152.35%            | -32.46% |     0.82 |       60 | 36.11%     | ok               |
|          40 | 61.93%   | 152.35%            | -31.93% |     0.8  |       66 | 38.27%     | ok               |
|          35 | 52.45%   | 152.35%            | -36.89% |     0.72 |       68 | 40.60%     | ok               |
|          30 | 48.52%   | 152.35%            | -42.66% |     0.68 |       58 | 43.09%     | ok               |

## SMH Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 113.87%  | 203.52%            | -30.17% |     1.31 |       47 | 50.92%     | ok               |
|          35 | 91.40%   | 203.52%            | -34.36% |     1.18 |       54 | 46.76%     | ok               |
|          25 | 91.26%   | 203.52%            | -32.94% |     1.16 |       46 | 49.75%     | ok               |
|          30 | 89.01%   | 203.52%            | -33.99% |     1.15 |       48 | 48.09%     | ok               |
|          45 | 75.26%   | 203.52%            | -32.75% |     1.11 |       52 | 40.93%     | ok               |

## SNX-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 5.04%    | -75.49%            | -43.20% |     0.32 |       71 | 48.08%     | ok               |
|          35 | -6.26%   | -75.49%            | -30.08% |     0.17 |       62 | 30.84%     | ok               |
|          30 | -15.26%  | -75.49%            | -34.76% |     0.08 |       58 | 37.93%     | ok               |
|          15 | -29.21%  | -75.49%            | -44.00% |    -0.01 |       79 | 52.68%     | ok               |
|          25 | -25.66%  | -75.49%            | -38.88% |    -0.03 |       72 | 42.53%     | ok               |

## SOL-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 9.10%    | -61.41%            | -51.50% |     0.33 |       60 | 37.36%     | ok               |
|          25 | -20.87%  | -61.41%            | -52.40% |     0.05 |       74 | 56.90%     | ok               |
|          45 | -16.39%  | -61.41%            | -59.86% |     0.03 |       62 | 31.80%     | ok               |
|          35 | -22.95%  | -61.41%            | -61.91% |     0    |       76 | 45.21%     | ok               |
|          15 | -27.68%  | -61.41%            | -59.14% |    -0.01 |       74 | 63.22%     | ok               |

## SOXX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 90.56%   | 177.21%            | -40.27% |     1.1  |       55 | 49.42%     | ok               |
|          35 | 86.56%   | 177.21%            | -38.63% |     1.09 |       59 | 44.59%     | ok               |
|          25 | 86.92%   | 177.21%            | -41.42% |     1.08 |       53 | 49.08%     | ok               |
|          15 | 85.78%   | 177.21%            | -39.35% |     1.03 |       68 | 52.25%     | ok               |
|          30 | 76.42%   | 177.21%            | -41.89% |     0.99 |       57 | 46.92%     | ok               |

## SPY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 16.08%   | 51.35%             | -14.25% |     0.56 |       61 | 53.91%     | ok               |
|          15 | 14.50%   | 51.35%             | -16.80% |     0.5  |       70 | 57.07%     | ok               |
|          25 | 8.86%    | 51.35%             | -15.22% |     0.35 |       61 | 52.91%     | ok               |
|          30 | 4.26%    | 51.35%             | -16.47% |     0.21 |       64 | 50.08%     | ok               |
|          35 | 3.64%    | 51.35%             | -16.72% |     0.19 |       60 | 47.09%     | ok               |

## SUSHI-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -23.49%  | -80.20%            | -40.08% |    -0.19 |       52 | 14.75%     | ok               |
|          45 | -58.58%  | -80.20%            | -64.27% |    -0.77 |       56 | 18.20%     | ok               |
|          40 | -61.52%  | -80.20%            | -68.16% |    -0.77 |       63 | 24.71%     | ok               |
|          35 | -74.22%  | -80.20%            | -79.91% |    -1.05 |       82 | 30.65%     | ok               |
|          15 | -80.74%  | -80.20%            | -80.79% |    -1.05 |       93 | 47.70%     | ok               |

## T Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 64.78%   | 25.84%             | -18.13% |     1.22 |       58 | 57.07%     | ok               |
|          25 | 59.66%   | 25.84%             | -17.66% |     1.16 |       60 | 54.91%     | ok               |
|          15 | 55.78%   | 25.84%             | -15.08% |     1.07 |       67 | 60.90%     | ok               |
|          30 | 42.17%   | 25.84%             | -17.01% |     0.92 |       64 | 52.91%     | ok               |
|          35 | 27.55%   | 25.84%             | -14.49% |     0.69 |       66 | 49.42%     | ok               |

## TGT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -10.98%  | -10.60%            | -42.86% |    -0.1  |       83 | 47.09%     | ok               |
|          45 | -9.45%   | -10.60%            | -29.07% |    -0.14 |       54 | 29.28%     | ok               |
|          30 | -11.24%  | -10.60%            | -40.57% |    -0.15 |       60 | 39.27%     | ok               |
|          25 | -11.87%  | -10.60%            | -43.36% |    -0.15 |       65 | 42.10%     | ok               |
|          15 | -16.62%  | -10.60%            | -40.77% |    -0.21 |       73 | 51.75%     | ok               |

## TIA-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 2.90%    | -86.85%            | -46.58% |     0.22 |       52 | 18.58%     | ok               |
|          35 | -2.69%   | -86.85%            | -49.70% |     0.2  |       64 | 30.65%     | ok               |
|          40 | -2.28%   | -86.85%            | -42.29% |     0.19 |       66 | 25.86%     | ok               |
|          50 | 1.89%    | -86.85%            | -46.02% |     0.18 |       32 | 11.49%     | ok               |
|          30 | -42.33%  | -86.85%            | -66.21% |    -0.27 |       89 | 36.21%     | ok               |

## TLT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -21.30%  | -9.44%             | -21.82% |    -1.65 |       72 | 31.95%     | ok               |
|          50 | -14.64%  | -9.44%             | -15.73% |    -1.73 |       34 | 14.48%     | ok               |
|          40 | -19.67%  | -9.44%             | -20.04% |    -1.9  |       60 | 21.30%     | ok               |
|          15 | -27.06%  | -9.44%             | -27.72% |    -1.91 |       77 | 39.93%     | ok               |
|          35 | -22.06%  | -9.44%             | -22.42% |    -1.95 |       66 | 26.12%     | ok               |

## TMO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 48.59%   | -2.57%             | -8.17%  |     1.08 |       40 | 31.78%     | ok               |
|          45 | 44.28%   | -2.57%             | -10.13% |     0.96 |       46 | 36.61%     | ok               |
|          40 | 42.15%   | -2.57%             | -9.91%  |     0.9  |       49 | 41.10%     | ok               |
|          35 | 24.06%   | -2.57%             | -14.06% |     0.57 |       61 | 45.59%     | ok               |
|          30 | 15.63%   | -2.57%             | -18.85% |     0.41 |       61 | 50.42%     | ok               |

## TMUS Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 8.91%    | 15.48%             | -30.05% |     0.28 |       65 | 60.40%     | ok               |
|          30 | 7.70%    | 15.48%             | -25.71% |     0.26 |       70 | 48.42%     | ok               |
|          20 | 2.63%    | 15.48%             | -29.75% |     0.16 |       71 | 54.74%     | ok               |
|          25 | -0.81%   | 15.48%             | -31.45% |     0.08 |       75 | 50.92%     | ok               |
|          35 | -4.65%   | 15.48%             | -34.23% |    -0.01 |       70 | 45.26%     | ok               |

## TRX-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 6.87%    | 40.18%             | -18.79% |     0.28 |       52 | 37.16%     | ok               |
|          30 | 0.99%    | 40.18%             | -22.90% |     0.12 |       72 | 49.04%     | ok               |
|          50 | 0.66%    | 40.18%             | -18.49% |     0.1  |       44 | 31.99%     | ok               |
|          20 | -0.08%   | 40.18%             | -25.45% |     0.1  |       63 | 55.94%     | ok               |
|          35 | 0.16%    | 40.18%             | -21.77% |     0.09 |       68 | 45.79%     | ok               |

## TSLA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 64.97%   | 104.47%            | -31.33% |     0.77 |       64 | 34.44%     | ok               |
|          50 | 48.84%   | 104.47%            | -33.23% |     0.67 |       64 | 29.78%     | ok               |
|          45 | 39.76%   | 104.47%            | -32.54% |     0.58 |       68 | 31.78%     | ok               |
|          35 | 27.32%   | 104.47%            | -37.58% |     0.46 |       71 | 36.94%     | ok               |
|          30 | 5.29%    | 104.47%            | -42.22% |     0.25 |       69 | 40.93%     | ok               |

## TXN Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 16.55%   | 87.75%             | -45.45% |     0.38 |       66 | 34.78%     | ok               |
|          20 | 4.63%    | 87.75%             | -38.49% |     0.22 |       60 | 59.40%     | ok               |
|          35 | 0.93%    | 87.75%             | -43.28% |     0.15 |       74 | 49.75%     | ok               |
|          15 | -1.35%   | 87.75%             | -38.99% |     0.14 |       65 | 63.23%     | ok               |
|          40 | -1.16%   | 87.75%             | -45.67% |     0.12 |       68 | 47.25%     | ok               |

## UNH Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 28.16%   | -18.40%            | -37.02% |     0.52 |       56 | 31.11%     | ok               |
|          30 | 29.58%   | -18.40%            | -27.86% |     0.51 |       74 | 52.58%     | ok               |
|          15 | 28.27%   | -18.40%            | -32.14% |     0.49 |       75 | 67.55%     | ok               |
|          35 | 26.05%   | -18.40%            | -29.20% |     0.48 |       66 | 47.42%     | ok               |
|          40 | 21.42%   | -18.40%            | -35.94% |     0.43 |       60 | 42.60%     | ok               |

## UNI-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -19.28%  | -59.94%            | -58.49% |    -0.01 |       56 | 27.20%     | ok               |
|          40 | -24.18%  | -59.94%            | -63.75% |    -0.06 |       60 | 32.57%     | ok               |
|          50 | -29.10%  | -59.94%            | -57.60% |    -0.19 |       54 | 21.46%     | ok               |
|          35 | -37.04%  | -59.94%            | -68.71% |    -0.19 |       72 | 37.93%     | ok               |
|          30 | -72.70%  | -59.94%            | -80.61% |    -0.87 |       88 | 43.87%     | ok               |

## UPS Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -31.90%  | -23.53%            | -43.07% |    -0.57 |       80 | 47.75%     | ok               |
|          25 | -32.99%  | -23.53%            | -39.04% |    -0.61 |       76 | 44.26%     | ok               |
|          15 | -36.04%  | -23.53%            | -43.86% |    -0.67 |       88 | 52.58%     | ok               |
|          35 | -34.34%  | -23.53%            | -39.90% |    -0.69 |       65 | 33.44%     | ok               |
|          30 | -37.14%  | -23.53%            | -38.83% |    -0.75 |       70 | 39.27%     | ok               |

## USO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 16.86%   | 65.93%             | -44.16% |     0.37 |       74 | 38.94%     | ok               |
|          45 | 15.67%   | 65.93%             | -33.25% |     0.37 |       50 | 26.12%     | ok               |
|          15 | 12.29%   | 65.93%             | -43.85% |     0.31 |       75 | 42.26%     | ok               |
|          30 | 7.84%    | 65.93%             | -43.35% |     0.25 |       68 | 33.61%     | ok               |
|          25 | 7.68%    | 65.93%             | -43.43% |     0.25 |       68 | 36.44%     | ok               |

## VEA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 5.44%    | 46.38%             | -16.28% |     0.25 |       60 | 50.58%     | ok               |
|          20 | 1.19%    | 46.38%             | -17.70% |     0.1  |       61 | 47.92%     | ok               |
|          25 | -0.82%   | 46.38%             | -17.79% |     0.02 |       57 | 46.26%     | ok               |
|          30 | -0.98%   | 46.38%             | -17.93% |     0.01 |       58 | 44.09%     | ok               |
|          35 | -2.09%   | 46.38%             | -16.79% |    -0.03 |       56 | 43.09%     | ok               |

## VIXY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -46.17%  | -65.01%            | -68.69% |    -0.39 |       44 | 10.32%     | ok               |
|          45 | -56.13%  | -65.01%            | -74.13% |    -0.55 |       56 | 16.31%     | ok               |
|          40 | -64.45%  | -65.01%            | -80.03% |    -0.66 |       70 | 20.63%     | ok               |
|          35 | -68.17%  | -65.01%            | -83.81% |    -0.7  |       86 | 25.79%     | ok               |
|          15 | -78.37%  | -65.01%            | -89.47% |    -0.82 |      101 | 44.26%     | ok               |

## VNQ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -7.59%   | 15.85%             | -19.07% |    -0.32 |       58 | 28.45%     | ok               |
|          50 | -8.03%   | 15.85%             | -17.13% |    -0.36 |       54 | 25.96%     | ok               |
|          25 | -12.00%  | 15.85%             | -22.34% |    -0.46 |       67 | 40.43%     | ok               |
|          20 | -13.62%  | 15.85%             | -23.79% |    -0.52 |       70 | 43.09%     | ok               |
|          15 | -14.46%  | 15.85%             | -24.90% |    -0.54 |       67 | 44.43%     | ok               |

## VTI Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 18.83%   | 50.33%             | -13.96% |     0.64 |       64 | 54.74%     | ok               |
|          15 | 12.74%   | 50.33%             | -15.70% |     0.45 |       67 | 57.24%     | ok               |
|          25 | 5.09%    | 50.33%             | -16.10% |     0.23 |       60 | 52.75%     | ok               |
|          30 | -3.15%   | 50.33%             | -18.77% |    -0.05 |       72 | 50.58%     | ok               |
|          35 | -5.59%   | 50.33%             | -21.19% |    -0.15 |       66 | 47.42%     | ok               |

## VWO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -7.30%   | 43.50%             | -21.18% |    -0.25 |       60 | 32.61%     | ok               |
|          15 | -9.50%   | 43.50%             | -24.01% |    -0.28 |       71 | 49.58%     | ok               |
|          40 | -8.98%   | 43.50%             | -23.57% |    -0.31 |       70 | 37.94%     | ok               |
|          45 | -9.11%   | 43.50%             | -23.26% |    -0.33 |       62 | 35.11%     | ok               |
|          20 | -10.53%  | 43.50%             | -26.14% |    -0.33 |       69 | 47.42%     | ok               |

## VZ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -6.80%   | 4.86%              | -12.71% |    -0.19 |       50 | 24.29%     | ok               |
|          45 | -17.18%  | 4.86%              | -20.47% |    -0.57 |       62 | 27.79%     | ok               |
|          35 | -19.25%  | 4.86%              | -19.99% |    -0.61 |       61 | 33.94%     | ok               |
|          25 | -22.01%  | 4.86%              | -24.67% |    -0.64 |       79 | 41.93%     | ok               |
|          40 | -23.66%  | 4.86%              | -23.66% |    -0.81 |       66 | 31.11%     | ok               |

## WFC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 0.75%    | 64.75%             | -18.29% |     0.09 |       58 | 35.27%     | ok               |
|          35 | -7.20%   | 64.75%             | -23.64% |    -0.08 |       77 | 46.76%     | ok               |
|          45 | -8.07%   | 64.75%             | -23.40% |    -0.16 |       62 | 39.60%     | ok               |
|          20 | -14.84%  | 64.75%             | -29.43% |    -0.19 |       79 | 56.57%     | ok               |
|          40 | -11.75%  | 64.75%             | -24.26% |    -0.27 |       72 | 42.93%     | ok               |

## WIF-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 60.65%   | -76.05%            | -46.21% |     0.66 |       71 | 41.38%     | ok               |
|          20 | 54.98%   | -76.05%            | -40.67% |     0.64 |       65 | 38.70%     | ok               |
|          25 | 2.09%    | -76.05%            | -45.19% |     0.31 |       67 | 36.02%     | ok               |
|          50 | -12.13%  | -76.05%            | -33.04% |    -0.02 |       38 | 11.69%     | ok               |
|          30 | -35.28%  | -76.05%            | -50.54% |    -0.13 |       68 | 31.99%     | ok               |

## WMT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 48.23%   | 93.96%             | -9.18%  |     1.32 |       38 | 42.26%     | ok               |
|          50 | 41.01%   | 93.96%             | -12.19% |     1.22 |       34 | 39.93%     | ok               |
|          40 | 38.97%   | 93.96%             | -10.52% |     1.09 |       42 | 43.43%     | ok               |
|          35 | 36.61%   | 93.96%             | -12.86% |     1.01 |       54 | 47.92%     | ok               |
|          15 | 16.22%   | 93.96%             | -25.74% |     0.44 |       70 | 61.40%     | ok               |

## XBI Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 10.60%   | 68.27%             | -16.56% |     0.34 |       60 | 36.11%     | ok               |
|          45 | 9.75%    | 68.27%             | -16.74% |     0.32 |       52 | 32.95%     | ok               |
|          35 | 6.29%    | 68.27%             | -18.84% |     0.23 |       62 | 39.43%     | ok               |
|          30 | 5.11%    | 68.27%             | -19.80% |     0.21 |       62 | 41.10%     | ok               |
|          25 | 0.38%    | 68.27%             | -23.66% |     0.1  |       72 | 43.26%     | ok               |

## XLB Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -1.68%   | 19.17%             | -20.68% |    -0.01 |       54 | 31.61%     | ok               |
|          50 | -1.74%   | 19.17%             | -17.59% |    -0.02 |       42 | 27.29%     | ok               |
|          35 | -4.92%   | 19.17%             | -23.62% |    -0.13 |       56 | 34.94%     | ok               |
|          45 | -4.65%   | 19.17%             | -20.79% |    -0.14 |       42 | 28.79%     | ok               |
|          25 | -6.87%   | 19.17%             | -22.63% |    -0.19 |       60 | 40.27%     | ok               |

## XLC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 12.36%   | 41.38%             | -12.33% |     0.45 |       67 | 54.41%     | ok               |
|          25 | 9.12%    | 41.38%             | -12.31% |     0.35 |       66 | 56.41%     | ok               |
|          40 | 7.92%    | 41.38%             | -13.38% |     0.34 |       68 | 46.76%     | ok               |
|          35 | 7.90%    | 41.38%             | -13.38% |     0.33 |       64 | 51.25%     | ok               |
|          20 | 1.64%    | 41.38%             | -13.78% |     0.12 |       72 | 59.23%     | ok               |

## XLE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 7.62%    | 34.33%             | -25.98% |     0.29 |       54 | 36.11%     | ok               |
|          45 | 3.21%    | 34.33%             | -29.68% |     0.16 |       60 | 38.10%     | ok               |
|          35 | 1.04%    | 34.33%             | -31.51% |     0.11 |       65 | 42.76%     | ok               |
|          25 | -5.66%   | 34.33%             | -36.05% |    -0.05 |       83 | 48.25%     | ok               |
|          40 | -5.55%   | 34.33%             | -34.51% |    -0.08 |       64 | 40.60%     | ok               |

## XLF Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -3.31%   | 42.16%             | -18.01% |    -0.05 |       70 | 53.74%     | ok               |
|          15 | -7.31%   | 42.16%             | -19.58% |    -0.18 |       78 | 56.57%     | ok               |
|          25 | -9.79%   | 42.16%             | -23.22% |    -0.3  |       77 | 50.42%     | ok               |
|          30 | -10.01%  | 42.16%             | -23.61% |    -0.32 |       76 | 47.75%     | ok               |
|          35 | -17.24%  | 42.16%             | -27.06% |    -0.67 |       66 | 43.59%     | ok               |

## XLI Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 5.70%    | 53.37%             | -10.36% |     0.26 |       74 | 52.08%     | ok               |
|          20 | 1.62%    | 53.37%             | -12.74% |     0.12 |       65 | 47.09%     | ok               |
|          50 | 1.03%    | 53.37%             | -11.03% |     0.09 |       60 | 33.44%     | ok               |
|          45 | -0.31%   | 53.37%             | -14.01% |     0.03 |       64 | 35.94%     | ok               |
|          30 | -0.61%   | 53.37%             | -11.79% |     0.03 |       66 | 44.59%     | ok               |

## XLK Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 85.96%   | 83.15%             | -14.75% |     1.37 |       41 | 51.08%     | ok               |
|          20 | 71.51%   | 83.15%             | -14.75% |     1.23 |       46 | 48.92%     | ok               |
|          25 | 68.02%   | 83.15%             | -14.75% |     1.23 |       40 | 46.76%     | ok               |
|          30 | 65.83%   | 83.15%             | -14.75% |     1.22 |       40 | 45.59%     | ok               |
|          35 | 47.33%   | 83.15%             | -13.61% |     0.99 |       52 | 42.93%     | ok               |

## XLM-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 26.14%   | -41.96%            | -38.97% |     0.48 |       44 | 27.39%     | ok               |
|          45 | 22.34%   | -41.96%            | -43.99% |     0.44 |       50 | 31.03%     | ok               |
|          30 | 5.21%    | -41.96%            | -50.36% |     0.28 |       69 | 45.79%     | ok               |
|          40 | 1.75%    | -41.96%            | -43.80% |     0.23 |       49 | 35.44%     | ok               |
|          35 | -4.00%   | -41.96%            | -50.42% |     0.17 |       69 | 41.76%     | ok               |

## XLP Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 10.28%   | 12.65%             | -5.66%  |     0.64 |       54 | 33.28%     | ok               |
|          50 | 8.85%    | 12.65%             | -6.08%  |     0.57 |       56 | 31.11%     | ok               |
|          40 | 8.06%    | 12.65%             | -7.77%  |     0.5  |       70 | 37.44%     | ok               |
|          35 | 7.11%    | 12.65%             | -9.73%  |     0.44 |       66 | 40.43%     | ok               |
|          30 | 5.21%    | 12.65%             | -11.16% |     0.33 |       68 | 41.93%     | ok               |

## XLU Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 6.98%    | 49.34%             | -12.55% |     0.38 |       52 | 31.11%     | ok               |
|          45 | 5.56%    | 49.34%             | -14.27% |     0.31 |       54 | 32.11%     | ok               |
|          40 | 2.65%    | 49.34%             | -15.59% |     0.17 |       58 | 33.61%     | ok               |
|          35 | -3.32%   | 49.34%             | -19.71% |    -0.11 |       62 | 35.77%     | ok               |
|          30 | -4.23%   | 49.34%             | -20.40% |    -0.15 |       67 | 38.94%     | ok               |

## XLV Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -15.42%  | 9.07%              | -19.97% |    -0.77 |       68 | 36.11%     | ok               |
|          25 | -16.67%  | 9.07%              | -21.14% |    -0.83 |       70 | 37.44%     | ok               |
|          15 | -20.45%  | 9.07%              | -24.43% |    -1    |       81 | 42.26%     | ok               |
|          20 | -20.38%  | 9.07%              | -24.51% |    -1.03 |       75 | 39.10%     | ok               |
|          50 | -17.67%  | 9.07%              | -21.32% |    -1.07 |       56 | 24.79%     | ok               |

## XLY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 4.62%    | 30.72%             | -12.94% |     0.21 |       72 | 41.26%     | ok               |
|          30 | 2.75%    | 30.72%             | -14.01% |     0.15 |       72 | 44.26%     | ok               |
|          15 | 1.20%    | 30.72%             | -15.77% |     0.11 |       74 | 51.25%     | ok               |
|          50 | -0.91%   | 30.72%             | -13.71% |     0.02 |       50 | 29.78%     | ok               |
|          40 | -1.91%   | 30.72%             | -16.99% |    -0.01 |       68 | 37.10%     | ok               |

## XOM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | 4.93%    | 41.21%             | -19.90% |     0.21 |       57 | 37.60%     | ok               |
|          30 | 4.33%    | 41.21%             | -20.29% |     0.19 |       57 | 36.27%     | ok               |
|          50 | 3.03%    | 41.21%             | -21.35% |     0.16 |       38 | 28.79%     | ok               |
|          20 | -2.57%   | 41.21%             | -25.56% |     0.01 |       66 | 39.93%     | ok               |
|          35 | -2.62%   | 41.21%             | -20.93% |    -0    |       57 | 35.11%     | ok               |

## XRP-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | -25.11%  | -54.05%            | -46.87% |    -0.14 |       68 | 39.85%     | ok               |
|          40 | -30.47%  | -54.05%            | -44.89% |    -0.26 |       58 | 33.72%     | ok               |
|          30 | -37.23%  | -54.05%            | -54.70% |    -0.33 |       70 | 44.06%     | ok               |
|          45 | -38.24%  | -54.05%            | -46.06% |    -0.42 |       58 | 29.50%     | ok               |
|          50 | -34.88%  | -54.05%            | -38.03% |    -0.46 |       60 | 22.03%     | ok               |

## YFI-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -53.18%  | -62.58%            | -53.44% |    -0.92 |       62 | 27.39%     | ok               |
|          45 | -49.42%  | -62.58%            | -54.12% |    -1.03 |       68 | 21.65%     | ok               |
|          30 | -65.87%  | -62.58%            | -70.70% |    -1.09 |       81 | 40.80%     | ok               |
|          35 | -64.67%  | -62.58%            | -64.86% |    -1.13 |       71 | 34.87%     | ok               |
|          25 | -69.34%  | -62.58%            | -71.76% |    -1.18 |       75 | 45.79%     | ok               |

## ZEC-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 117.91%  | 1605.07%           | -24.66% |     0.88 |       46 | 23.18%     | ok               |
|          35 | 87.09%   | 1605.07%           | -44.34% |     0.75 |       54 | 29.69%     | ok               |
|          25 | 66.56%   | 1605.07%           | -48.59% |     0.66 |       60 | 38.89%     | ok               |
|          30 | 50.08%   | 1605.07%           | -47.68% |     0.59 |       64 | 35.44%     | ok               |
|          50 | 49.79%   | 1605.07%           | -34.39% |     0.58 |       48 | 20.69%     | ok               |
