# Market Tracker Backtest Report

_Generated: 2026-06-03T01:48:25+00:00_

## Data Sources

- Crypto: Kraken -> Coinbase -> CoinGecko OHLC -> CoinPaprika fallback chain.
- Stocks / ETFs / indices: Stooq -> Yahoo Finance fallback chain.
- Data rows are generated from real market APIs. Mock OHLCV rows are not generated.

## Data Freshness

- Rows: **92,347**
- Symbols: **161**
- Date range: **2024-01-09** to **2026-06-03**

## Latest Signals

| symbol     | date                |         close |   composite_score | signal   | data_source   |
|:-----------|:--------------------|--------------:|------------------:|:---------|:--------------|
| AAPL       | 2026-06-02 00:00:00 |   315.2       |         53.5833   | LONG     | Yahoo Finance |
| ABBV       | 2026-06-02 00:00:00 |   215.4       |         67.1667   | LONG     | Yahoo Finance |
| AMD        | 2026-06-02 00:00:00 |   521.54      |         61.75     | LONG     | Yahoo Finance |
| CSCO       | 2026-06-02 00:00:00 |   128         |         72.0833   | LONG     | Yahoo Finance |
| DE         | 2026-06-02 00:00:00 |   579.25      |         43.5      | LONG     | Yahoo Finance |
| DXY-INDEX  | 2026-06-02 00:00:00 |    99.218     |         79.5699   | LONG     | Yahoo Finance |
| FCX        | 2026-06-02 00:00:00 |    71.72      |         77.4167   | LONG     | Yahoo Finance |
| FET-USD    | 2026-06-03 00:00:00 |     0.2481    |         42.6667   | LONG     | Kraken API    |
| GS         | 2026-06-02 00:00:00 |  1064.58      |         62.25     | LONG     | Yahoo Finance |
| HON        | 2026-06-02 00:00:00 |   235.23      |         71.5833   | LONG     | Yahoo Finance |
| IBM        | 2026-06-02 00:00:00 |   329.23      |         63.25     | LONG     | Yahoo Finance |
| ICP-USD    | 2026-06-03 00:00:00 |     3.075     |         75.25     | LONG     | Kraken API    |
| INJ-USD    | 2026-06-03 00:00:00 |     6.51      |         63.5      | LONG     | Kraken API    |
| ITA        | 2026-06-02 00:00:00 |   228.33      |         60.1667   | LONG     | Yahoo Finance |
| LLY        | 2026-06-02 00:00:00 |  1064.15      |         72.75     | LONG     | Yahoo Finance |
| MRK        | 2026-06-02 00:00:00 |   115.65      |         48.9167   | LONG     | Yahoo Finance |
| MSFT       | 2026-06-02 00:00:00 |   441.31      |         64.6667   | LONG     | Yahoo Finance |
| MU         | 2026-06-02 00:00:00 |  1064.1       |         66.75     | LONG     | Yahoo Finance |
| NVDA       | 2026-06-02 00:00:00 |   222.82      |         37.75     | LONG     | Yahoo Finance |
| ORCL       | 2026-06-02 00:00:00 |   244.58      |         59.75     | LONG     | Yahoo Finance |
| QCOM       | 2026-06-02 00:00:00 |   240.84      |         65.5833   | LONG     | Yahoo Finance |
| QQQ        | 2026-06-02 00:00:00 |   746.16      |         49.75     | LONG     | Yahoo Finance |
| RENDER-USD | 2026-06-03 00:00:00 |     2.124     |         70.9167   | LONG     | Kraken API    |
| SPY        | 2026-06-02 00:00:00 |   759.57      |         36.4167   | LONG     | Yahoo Finance |
| TXN        | 2026-06-02 00:00:00 |   308.12      |         56.25     | LONG     | Yahoo Finance |
| UNH        | 2026-06-02 00:00:00 |   377.92      |         32.6667   | LONG     | Yahoo Finance |
| UPS        | 2026-06-02 00:00:00 |   108.93      |         75.25     | LONG     | Yahoo Finance |
| VTI        | 2026-06-02 00:00:00 |   374.36      |         53.0833   | LONG     | Yahoo Finance |
| XLB        | 2026-06-02 00:00:00 |    51.52      |         45.25     | LONG     | Yahoo Finance |
| XLK        | 2026-06-02 00:00:00 |   198.21      |         75.75     | LONG     | Yahoo Finance |
| XLM-USD    | 2026-06-03 00:00:00 |     0.226594  |         68.9167   | LONG     | Kraken API    |
| ADBE       | 2026-06-02 00:00:00 |   262.11      |         24.3333   | NEUTRAL  | Yahoo Finance |
| AGG        | 2026-06-02 00:00:00 |    98.71      |        -17.0833   | NEUTRAL  | Yahoo Finance |
| ALGO-USD   | 2026-06-03 00:00:00 |     0.11174   |        -19.4167   | NEUTRAL  | Kraken API    |
| AMAT       | 2026-06-02 00:00:00 |   490.05      |         64.5      | NEUTRAL  | Yahoo Finance |
| AMGN       | 2026-06-02 00:00:00 |   328.26      |        -29.4167   | NEUTRAL  | Yahoo Finance |
| AMZN       | 2026-06-02 00:00:00 |   256.52      |          4.66667  | NEUTRAL  | Yahoo Finance |
| ARKK       | 2026-06-02 00:00:00 |    79.91      |         53.4167   | NEUTRAL  | Yahoo Finance |
| AVGO       | 2026-06-02 00:00:00 |   481.57      |         54.5      | NEUTRAL  | Yahoo Finance |
| BA         | 2026-06-02 00:00:00 |   217.7       |        -34.25     | NEUTRAL  | Yahoo Finance |
| BAC        | 2026-06-02 00:00:00 |    52.48      |         49.6667   | NEUTRAL  | Yahoo Finance |
| BITO       | 2026-06-02 00:00:00 |     9.17      |        -70.0833   | NEUTRAL  | Yahoo Finance |
| BLK        | 2026-06-02 00:00:00 |  1018.96      |        -64.5      | NEUTRAL  | Yahoo Finance |
| BND        | 2026-06-02 00:00:00 |    73.2       |         -5.83333  | NEUTRAL  | Yahoo Finance |
| C          | 2026-06-02 00:00:00 |   131.26      |         45.3333   | NEUTRAL  | Yahoo Finance |
| CAT        | 2026-06-02 00:00:00 |   909.81      |         30.8333   | NEUTRAL  | Yahoo Finance |
| CL         | 2026-06-02 00:00:00 |    88.27      |         26.8333   | NEUTRAL  | Yahoo Finance |
| CMCSA      | 2026-06-02 00:00:00 |    24.85      |        -15.25     | NEUTRAL  | Yahoo Finance |
| COP        | 2026-06-02 00:00:00 |   116.87      |        -14.25     | NEUTRAL  | Yahoo Finance |
| COST       | 2026-06-02 00:00:00 |   954.27      |        -49.75     | NEUTRAL  | Yahoo Finance |
| CRM        | 2026-06-02 00:00:00 |   200.84      |         21        | NEUTRAL  | Yahoo Finance |
| CVX        | 2026-06-02 00:00:00 |   187.55      |          8.91667  | NEUTRAL  | Yahoo Finance |
| DASH-USD   | 2026-06-03 00:00:00 |    39.21      |        -80.0833   | NEUTRAL  | Kraken API    |
| DBC        | 2026-06-02 00:00:00 |    30.12      |         -8.25     | NEUTRAL  | Yahoo Finance |
| DIA        | 2026-06-02 00:00:00 |   514.05      |         53        | NEUTRAL  | Yahoo Finance |
| DIS        | 2026-06-02 00:00:00 |   101.41      |        -64.5      | NEUTRAL  | Yahoo Finance |
| DOT-USD    | 2026-06-03 00:00:00 |     1.0877    |        -53.5833   | NEUTRAL  | Kraken API    |
| EEM        | 2026-06-02 00:00:00 |    70.8       |         62        | NEUTRAL  | Yahoo Finance |
| EFA        | 2026-06-02 00:00:00 |   105.02      |         48.8333   | NEUTRAL  | Yahoo Finance |
| EOG        | 2026-06-02 00:00:00 |   138.58      |         50        | NEUTRAL  | Yahoo Finance |
| EWJ        | 2026-06-02 00:00:00 |    93.58      |         43.8333   | NEUTRAL  | Yahoo Finance |
| FIL-USD    | 2026-06-03 00:00:00 |     0.878     |        -50.75     | NEUTRAL  | Kraken API    |
| FXI        | 2026-06-02 00:00:00 |    36.36      |        -29.0833   | NEUTRAL  | Yahoo Finance |
| GDX        | 2026-06-02 00:00:00 |    88.05      |        -17.9167   | NEUTRAL  | Yahoo Finance |
| GDXJ       | 2026-06-02 00:00:00 |   115.98      |        -18.4167   | NEUTRAL  | Yahoo Finance |
| GE         | 2026-06-02 00:00:00 |   317.72      |         53.9167   | NEUTRAL  | Yahoo Finance |
| GLD        | 2026-06-02 00:00:00 |   411.95      |        -28.0833   | NEUTRAL  | Yahoo Finance |
| GOOGL      | 2026-06-02 00:00:00 |   361.85      |         14.1667   | NEUTRAL  | Yahoo Finance |
| GRT-USD    | 2026-06-03 00:00:00 |     0.02332   |        -45.0833   | NEUTRAL  | Kraken API    |
| HBAR-USD   | 2026-06-03 00:00:00 |     0.08706   |        -13.75     | NEUTRAL  | Kraken API    |
| HD         | 2026-06-02 00:00:00 |   311.52      |        -12.0833   | NEUTRAL  | Yahoo Finance |
| HYG        | 2026-06-02 00:00:00 |    79.9       |         -6        | NEUTRAL  | Yahoo Finance |
| IBIT       | 2026-06-02 00:00:00 |    38.05      |        -70.0833   | NEUTRAL  | Yahoo Finance |
| IEF        | 2026-06-02 00:00:00 |    94.24      |        -20.25     | NEUTRAL  | Yahoo Finance |
| IEMG       | 2026-06-02 00:00:00 |    85.99      |         62        | NEUTRAL  | Yahoo Finance |
| INTC       | 2026-06-02 00:00:00 |   107.93      |         10.4167   | NEUTRAL  | Yahoo Finance |
| INTU       | 2026-06-02 00:00:00 |   322.14      |        -75.8333   | NEUTRAL  | Yahoo Finance |
| IWM        | 2026-06-02 00:00:00 |   291.66      |         65.3333   | NEUTRAL  | Yahoo Finance |
| JNJ        | 2026-06-02 00:00:00 |   222.89      |        -15.9167   | NEUTRAL  | Yahoo Finance |
| JPM        | 2026-06-02 00:00:00 |   300.96      |        -25.75     | NEUTRAL  | Yahoo Finance |
| KO         | 2026-06-02 00:00:00 |    78.41      |          0.416667 | NEUTRAL  | Yahoo Finance |
| LIN        | 2026-06-02 00:00:00 |   495.91      |        -24.5      | NEUTRAL  | Yahoo Finance |
| LRCX       | 2026-06-02 00:00:00 |   334.41      |         64.5      | NEUTRAL  | Yahoo Finance |
| MCD        | 2026-06-02 00:00:00 |   276.36      |        -26.3333   | NEUTRAL  | Yahoo Finance |
| MPC        | 2026-06-02 00:00:00 |   263.06      |         36        | NEUTRAL  | Yahoo Finance |
| MS         | 2026-06-02 00:00:00 |   214.98      |         51        | NEUTRAL  | Yahoo Finance |
| NEAR-USD   | 2026-06-03 00:00:00 |     2.725     |         63.8333   | NEUTRAL  | Kraken API    |
| NEM        | 2026-06-02 00:00:00 |   109.5       |        -31.75     | NEUTRAL  | Yahoo Finance |
| NFLX       | 2026-06-02 00:00:00 |    83.33      |        -61.6667   | NEUTRAL  | Yahoo Finance |
| NKE        | 2026-06-02 00:00:00 |    43.73      |        -12.25     | NEUTRAL  | Yahoo Finance |
| NOW        | 2026-06-02 00:00:00 |   127.65      |         26.5833   | NEUTRAL  | Yahoo Finance |
| OXY        | 2026-06-02 00:00:00 |    59.09      |         62.8333   | NEUTRAL  | Yahoo Finance |
| PFE        | 2026-06-02 00:00:00 |    25.55      |        -26.1667   | NEUTRAL  | Yahoo Finance |
| PM         | 2026-06-02 00:00:00 |   173.66      |         -2.91667  | NEUTRAL  | Yahoo Finance |
| POL-USD    | 2026-06-03 00:00:00 |     0.09079   |        -17        | NEUTRAL  | Kraken API    |
| RTX        | 2026-06-02 00:00:00 |   174.26      |        -51.1667   | NEUTRAL  | Yahoo Finance |
| SBUX       | 2026-06-02 00:00:00 |    95.51      |         -7.83333  | NEUTRAL  | Yahoo Finance |
| SCHW       | 2026-06-02 00:00:00 |    87.61      |        -67.3333   | NEUTRAL  | Yahoo Finance |
| SHY        | 2026-06-02 00:00:00 |    82.01      |        -17.6667   | NEUTRAL  | Yahoo Finance |
| SKY-USD    | 2026-06-03 00:00:00 |     0.0674    |        -11.25     | NEUTRAL  | Kraken API    |
| SLB        | 2026-06-02 00:00:00 |    56.56      |         36        | NEUTRAL  | Yahoo Finance |
| SLV        | 2026-06-02 00:00:00 |    67.99      |        -18.8333   | NEUTRAL  | Yahoo Finance |
| SMH        | 2026-06-02 00:00:00 |   632.21      |         56.6667   | NEUTRAL  | Yahoo Finance |
| SOXX       | 2026-06-02 00:00:00 |   605.02      |         60        | NEUTRAL  | Yahoo Finance |
| SUSHI-USD  | 2026-06-03 00:00:00 |     0.2078    |          4.5      | NEUTRAL  | Kraken API    |
| TGT        | 2026-06-02 00:00:00 |   123.18      |          4.58333  | NEUTRAL  | Yahoo Finance |
| TIA-USD    | 2026-06-03 00:00:00 |     0.3629    |        -65.25     | NEUTRAL  | Kraken API    |
| TLT        | 2026-06-02 00:00:00 |    85.65      |          8.41667  | NEUTRAL  | Yahoo Finance |
| TMO        | 2026-06-02 00:00:00 |   482.08      |         24.9167   | NEUTRAL  | Yahoo Finance |
| TMUS       | 2026-06-02 00:00:00 |   188.83      |        -53.1667   | NEUTRAL  | Yahoo Finance |
| TRX-USD    | 2026-06-03 00:00:00 |     0.333161  |        -15.25     | NEUTRAL  | Kraken API    |
| TSLA       | 2026-06-02 00:00:00 |   423.74      |         18.4167   | NEUTRAL  | Yahoo Finance |
| USO        | 2026-06-02 00:00:00 |   137.27      |         -3.58333  | NEUTRAL  | Yahoo Finance |
| VEA        | 2026-06-02 00:00:00 |    72.32      |         65.3333   | NEUTRAL  | Yahoo Finance |
| VNQ        | 2026-06-02 00:00:00 |    94.52      |         -6.83333  | NEUTRAL  | Yahoo Finance |
| VWO        | 2026-06-02 00:00:00 |    61.19      |         47.3333   | NEUTRAL  | Yahoo Finance |
| VZ         | 2026-06-02 00:00:00 |    47.87      |         47.6667   | NEUTRAL  | Yahoo Finance |
| WFC        | 2026-06-02 00:00:00 |    79.44      |         22.9167   | NEUTRAL  | Yahoo Finance |
| XBI        | 2026-06-02 00:00:00 |   127.76      |        -18.8333   | NEUTRAL  | Yahoo Finance |
| XLC        | 2026-06-02 00:00:00 |   113.57      |        -22.75     | NEUTRAL  | Yahoo Finance |
| XLE        | 2026-06-02 00:00:00 |    57.96      |          7.83333  | NEUTRAL  | Yahoo Finance |
| XLF        | 2026-06-02 00:00:00 |    51.46      |        -16.0833   | NEUTRAL  | Yahoo Finance |
| XLI        | 2026-06-02 00:00:00 |   174.19      |         48.1667   | NEUTRAL  | Yahoo Finance |
| XLP        | 2026-06-02 00:00:00 |    81.83      |        -40.75     | NEUTRAL  | Yahoo Finance |
| XLV        | 2026-06-02 00:00:00 |   146.4       |        -20.25     | NEUTRAL  | Yahoo Finance |
| XLY        | 2026-06-02 00:00:00 |   117.59      |         -5.83333  | NEUTRAL  | Yahoo Finance |
| XOM        | 2026-06-02 00:00:00 |   149.56      |        -13.5833   | NEUTRAL  | Yahoo Finance |
| ZEC-USD    | 2026-06-03 00:00:00 |   634.9       |          0.916667 | NEUTRAL  | Kraken API    |
| AAVE-USD   | 2026-06-03 00:00:00 |    74.15      |        -49.6667   | SHORT    | Kraken API    |
| ADA-USD    | 2026-06-03 00:00:00 |     0.214312  |        -49.3333   | SHORT    | Kraken API    |
| APT-USD    | 2026-06-03 00:00:00 |     0.8334    |        -37.3333   | SHORT    | Kraken API    |
| ARB-USD    | 2026-06-03 00:00:00 |     0.0925    |        -51.6667   | SHORT    | Kraken API    |
| ATOM-USD   | 2026-06-03 00:00:00 |     1.846     |        -37        | SHORT    | Kraken API    |
| AVAX-USD   | 2026-06-03 00:00:00 |     8.25      |        -49.3333   | SHORT    | Kraken API    |
| BCH-USD    | 2026-06-03 00:00:00 |   267.65      |        -65.1667   | SHORT    | Kraken API    |
| BONK-USD   | 2026-06-03 00:00:00 |     5.034e-06 |        -51.6667   | SHORT    | Kraken API    |
| BTC-USD    | 2026-06-03 00:00:00 | 66885         |        -49.3333   | SHORT    | Kraken API    |
| COMP-USD   | 2026-06-03 00:00:00 |    17.61      |        -51.3333   | SHORT    | Kraken API    |
| CRV-USD    | 2026-06-03 00:00:00 |     0.2024    |        -51.3333   | SHORT    | Kraken API    |
| DOGE-USD   | 2026-06-03 00:00:00 |     0.0931443 |        -47.6667   | SHORT    | Kraken API    |
| ETC-USD    | 2026-06-03 00:00:00 |     7.695     |        -49.3333   | SHORT    | Kraken API    |
| ETH-USD    | 2026-06-03 00:00:00 |  1863.68      |        -48.6667   | SHORT    | Kraken API    |
| LDO-USD    | 2026-06-03 00:00:00 |     0.304     |        -49.6667   | SHORT    | Kraken API    |
| LINK-USD   | 2026-06-03 00:00:00 |     8.39281   |        -49.3333   | SHORT    | Kraken API    |
| LTC-USD    | 2026-06-03 00:00:00 |    47.46      |        -47.6667   | SHORT    | Kraken API    |
| META       | 2026-06-02 00:00:00 |   597.63      |        -39.25     | SHORT    | Yahoo Finance |
| OP-USD     | 2026-06-03 00:00:00 |     0.1171    |        -44.6667   | SHORT    | Kraken API    |
| PEP        | 2026-06-02 00:00:00 |   142         |        -47.5833   | SHORT    | Yahoo Finance |
| PEPE-USD   | 2026-06-03 00:00:00 |     3.139e-06 |        -51.3333   | SHORT    | Kraken API    |
| PG         | 2026-06-02 00:00:00 |   140.82      |        -31.5833   | SHORT    | Yahoo Finance |
| SHIB-USD   | 2026-06-03 00:00:00 |     5.24e-06  |        -38.6667   | SHORT    | Kraken API    |
| SNX-USD    | 2026-06-03 00:00:00 |     0.2695    |        -46.3333   | SHORT    | Kraken API    |
| SOL-USD    | 2026-06-03 00:00:00 |    74.9       |        -49.3333   | SHORT    | Kraken API    |
| T          | 2026-06-02 00:00:00 |    24.64      |        -38.25     | SHORT    | Yahoo Finance |
| UNI-USD    | 2026-06-03 00:00:00 |     2.824     |        -53.3333   | SHORT    | Kraken API    |
| VIXY       | 2026-06-02 00:00:00 |    23.46      |        -47.5833   | SHORT    | Yahoo Finance |
| WIF-USD    | 2026-06-03 00:00:00 |     0.1771    |        -34        | SHORT    | Kraken API    |
| WMT        | 2026-06-02 00:00:00 |   113.06      |        -44.3333   | SHORT    | Yahoo Finance |
| XLU        | 2026-06-02 00:00:00 |    43.9       |        -51.5833   | SHORT    | Yahoo Finance |
| XRP-USD    | 2026-06-03 00:00:00 |     1.2286    |        -47.6667   | SHORT    | Kraken API    |
| YFI-USD    | 2026-06-03 00:00:00 |  2135         |        -47.6667   | SHORT    | Kraken API    |

## Edge Summary

- Symbols with trades: **160** of 160
- Beat buy-and-hold: **33.12%** of traded symbols
- Positive return: **32.50%** of traded symbols
- Median strategy return: **-8.68%** (benchmark **18.41%**)
- Median excess vs benchmark: **-28.55%**
- Median Sharpe: **-0.09**
- Median exposure: **44.70%**

> Edge is real only if both _beat buy-and-hold_ and _median excess_ are convincingly positive across many symbols. Treat a single high-return symbol as noise.

## Portfolio Backtest

Actual capital-allocation books (not per-symbol averages). Benchmarks: `equal_weight_buyhold` (whole tracked universe), `spy_buyhold` (100% SPY), and `sixty_forty` (60% SPY / 40% AGG). `high_conf_voltarget` inverse-vol-weights the HIGH-confidence book; `conviction_long_short` is market-neutral. Judge on **Sharpe** and **max_drawdown** out-of-sample, not raw return: a fully-invested long book wins on return in a bull market but carries all the risk.

| strategy              | scope         | ann_return   | ann_vol   |   sharpe | max_drawdown   | total_return   |   avg_gross_exposure |
|:----------------------|:--------------|:-------------|:----------|---------:|:---------------|:---------------|---------------------:|
| equal_weight_buyhold  | full          | -9.13%       | 33.76%    |    -0.27 | -57.60%        | -36.48%        |                 1    |
| equal_weight_buyhold  | out_of_sample | -16.45%      | 34.35%    |    -0.48 | -39.63%        | -21.23%        |                 1    |
| all_signals_ew        | full          | -6.95%       | 28.15%    |    -0.25 | -60.23%        | -28.35%        |                 1    |
| all_signals_ew        | out_of_sample | 8.31%        | 28.55%    |     0.29 | -32.69%        | 4.65%          |                 1    |
| high_conf_ew          | full          | 0.29%        | 32.23%    |     0.01 | -47.93%        | -13.72%        |                 0.89 |
| high_conf_ew          | out_of_sample | 19.30%       | 37.30%    |     0.52 | -20.90%        | 14.28%         |                 0.89 |
| high_conf_voltarget   | full          | 0.34%        | 29.81%    |     0.01 | -40.80%        | -11.58%        |                 0.89 |
| high_conf_voltarget   | out_of_sample | 11.35%       | 35.55%    |     0.32 | -17.06%        | 5.71%          |                 0.89 |
| conviction_long_short | full          | -9.31%       | 23.30%    |    -0.4  | -39.73%        | -30.73%        |                 0.97 |
| conviction_long_short | out_of_sample | -2.28%       | 27.00%    |    -0.08 | -20.75%        | -6.15%         |                 0.97 |
| spy_buyhold           | full          | 10.32%       | 13.21%    |     0.78 | -17.81%        | 33.34%         |                 0.78 |
| spy_buyhold           | out_of_sample | 1.71%        | 9.33%     |     0.18 | -14.83%        | 1.37%          |                 0.78 |
| sixty_forty           | full          | 5.89%        | 8.37%     |     0.7  | -10.80%        | 18.37%         |                 0.78 |
| sixty_forty           | out_of_sample | -0.20%       | 6.03%     |    -0.03 | -10.09%        | -0.41%         |                 0.78 |

## Walk-Forward Robustness

Each book measured across contiguous time folds (each a different regime). A book has durable edge only if `mean_sharpe` is positive, `min_sharpe` isn't deeply negative, and `pct_positive_folds` is high — a single great fold doesn't count. `fold_sharpes` lists each fold oldest-to-newest.

| strategy              |   n_folds |   mean_sharpe |   median_sharpe |   min_sharpe | pct_positive_folds   | mean_return   | fold_sharpes                 |
|:----------------------|----------:|--------------:|----------------:|-------------:|:---------------------|:--------------|:-----------------------------|
| equal_weight_buyhold  |         5 |         -0.02 |           -0.04 |        -1.51 | 40.00%               | -7.68%        | 1.96;-1.51;0.07;-0.61;-0.04  |
| all_signals_ew        |         5 |          0.09 |            0.89 |        -2.21 | 60.00%               | -3.38%        | 0.92;0.89;-0.87;-2.21;1.70   |
| high_conf_ew          |         5 |          0.34 |           -0.39 |        -0.73 | 40.00%               | -1.16%        | 1.81;-0.39;-0.73;-0.60;1.59  |
| high_conf_voltarget   |         5 |          0.4  |           -0.44 |        -0.5  | 40.00%               | -1.53%        | 2.51;-0.50;-0.44;-0.44;0.88  |
| conviction_long_short |         5 |         -0.38 |           -0.37 |        -1.12 | 20.00%               | -6.76%        | -0.40;-0.30;-0.37;-1.12;0.31 |
| spy_buyhold           |         5 |          0.88 |            0.86 |         0.02 | 100.00%              | 6.14%         | 2.21;1.27;0.02;0.02;0.86     |
| sixty_forty           |         5 |          0.76 |            0.55 |        -0    | 80.00%               | 3.52%         | 2.15;1.01;-0.00;0.07;0.55    |

## Strategy Comparison

Each decision rule backtested over the same data. `out_of_sample` is the most recent ~35% of each symbol's history (unseen tail). A rule has real edge only if `median_excess` and `beat_benchmark_pct` stay positive out-of-sample, not just full-sample.

| strategy        | scope         |   symbols | beat_benchmark_pct   | positive_pct   | median_return   | median_benchmark   | median_excess   |   median_sharpe |   total_trades |
|:----------------|:--------------|----------:|:---------------------|:---------------|:----------------|:-------------------|:----------------|----------------:|---------------:|
| trend           | full          |       160 | 33.12%               | 32.50%         | -8.68%          | 18.41%             | -28.55%         |           -0.09 |          11327 |
| trend           | out_of_sample |       160 | 35.00%               | 58.13%         | 4.08%           | 8.16%              | -10.24%         |            0.39 |           3910 |
| mean_reversion  | full          |       159 | 38.99%               | 47.80%         | -0.14%          | 17.44%             | -18.91%         |           -0.03 |           1270 |
| mean_reversion  | out_of_sample |       128 | 44.53%               | 57.03%         | 0.32%           | 3.17%              | -3.42%          |            0.65 |            478 |
| regime_adaptive | full          |       160 | 34.38%               | 31.87%         | -9.59%          | 18.41%             | -29.32%         |           -0.09 |          11605 |
| regime_adaptive | out_of_sample |       160 | 35.00%               | 60.00%         | 4.27%           | 8.16%              | -10.61%         |            0.4  |           4015 |

## Signal Calibration

Realized forward return in the signal's direction, grouped by confidence. HIGH should outrank LOW for the confidence score to be meaningful.

| confidence_level   |   horizon |     n | mean_return   | median_return   | win_rate   |
|:-------------------|----------:|------:|:--------------|:----------------|:-----------|
| HIGH               |         5 |  8102 | 0.16%         | 0.14%           | 52.36%     |
| MEDIUM             |         5 | 29167 | 0.03%         | 0.09%           | 51.10%     |
| LOW                |         5 |  3279 | -0.61%        | -0.48%          | 45.11%     |
| ALL                |         5 | 40548 | 0.00%         | 0.06%           | 50.86%     |
| HIGH               |        10 |  8065 | 0.51%         | 0.19%           | 52.32%     |
| MEDIUM             |        10 | 28859 | 0.18%         | 0.15%           | 51.30%     |
| LOW                |        10 |  3255 | -0.90%        | -0.73%          | 45.25%     |
| ALL                |        10 | 40179 | 0.16%         | 0.11%           | 51.02%     |
| HIGH               |        20 |  7942 | 0.88%         | 0.46%           | 53.68%     |
| MEDIUM             |        20 | 28227 | 0.74%         | 0.61%           | 53.48%     |
| LOW                |        20 |  3204 | -0.73%        | -0.57%          | 46.82%     |
| ALL                |        20 | 39373 | 0.65%         | 0.50%           | 52.98%     |

## Backtest Summary

### Data Quality / Signal Availability

- **ok**: 160 symbols

| symbol     |   trades | return   | benchmark_return   | mdd     |   sharpe | exposure   | skipped_reason   |
|:-----------|---------:|:---------|:-------------------|:--------|---------:|:-----------|:-----------------|
| AAPL       |       67 | 14.81%   | 70.25%             | -20.65% |     0.39 | 49.08%     | ok               |
| AAVE-USD   |       80 | -64.62%  | -77.68%            | -69.30% |    -0.86 | 34.87%     | ok               |
| ABBV       |       64 | -17.68%  | 32.71%             | -30.55% |    -0.37 | 49.25%     | ok               |
| ADA-USD    |       86 | -86.58%  | -75.01%            | -91.71% |    -0.85 | 45.40%     | ok               |
| ADBE       |       66 | -22.69%  | -55.29%            | -38.01% |    -0.23 | 56.91%     | ok               |
| AGG        |       71 | -6.84%   | 0.16%              | -10.16% |    -1.11 | 31.78%     | ok               |
| ALGO-USD   |       84 | -52.60%  | -65.62%            | -61.76% |    -0.61 | 38.31%     | ok               |
| AMAT       |       67 | -19.38%  | 224.47%            | -57.80% |    -0.1  | 53.58%     | ok               |
| AMD        |       56 | 45.53%   | 249.42%            | -47.17% |     0.59 | 38.94%     | ok               |
| AMGN       |       71 | -18.60%  | 6.83%              | -34.14% |    -0.35 | 49.58%     | ok               |
| AMZN       |       74 | -33.84%  | 69.47%             | -42.48% |    -0.99 | 38.27%     | ok               |
| APT-USD    |       80 | -52.19%  | -90.62%            | -69.98% |    -0.41 | 41.95%     | ok               |
| ARB-USD    |       74 | -2.50%   | -87.54%            | -61.76% |     0.22 | 38.89%     | ok               |
| ARKK       |       79 | -30.02%  | 61.43%             | -32.63% |    -0.5  | 38.94%     | ok               |
| ATOM-USD   |       92 | -64.89%  | -70.64%            | -68.64% |    -1.07 | 43.49%     | ok               |
| AVAX-USD   |       72 | -37.87%  | -76.94%            | -53.72% |    -0.34 | 36.97%     | ok               |
| AVGO       |       60 | 47.16%   | 344.87%            | -35.76% |     0.63 | 47.25%     | ok               |
| BA         |       71 | 2.28%    | -3.57%             | -30.56% |     0.17 | 51.41%     | ok               |
| BAC        |       80 | -18.03%  | 56.05%             | -26.91% |    -0.46 | 45.59%     | ok               |
| BCH-USD    |       80 | -37.71%  | -39.02%            | -58.22% |    -0.37 | 45.59%     | ok               |
| BITO       |       76 | 3.90%    | -59.64%            | -42.82% |     0.22 | 38.77%     | ok               |
| BLK        |       73 | -0.88%   | 28.25%             | -20.81% |     0.04 | 42.10%     | ok               |
| BND        |       69 | -8.06%   | 0.19%              | -9.89%  |    -1.28 | 32.78%     | ok               |
| BONK-USD   |       72 | 62.94%   | -83.65%            | -45.22% |     0.69 | 40.23%     | ok               |
| BTC-USD    |       74 | -6.28%   | -28.50%            | -30.44% |     0.04 | 50.77%     | ok               |
| C          |       83 | -28.88%  | 145.44%            | -36.36% |    -0.58 | 51.25%     | ok               |
| CAT        |       74 | 28.78%   | 211.27%            | -21.02% |     0.55 | 57.90%     | ok               |
| CL         |       60 | 20.05%   | 9.22%              | -14.32% |     0.67 | 49.42%     | ok               |
| CMCSA      |       80 | -36.01%  | -38.74%            | -39.80% |    -0.9  | 44.26%     | ok               |
| COMP-USD   |       93 | -43.66%  | -77.12%            | -63.55% |    -0.32 | 44.64%     | ok               |
| COP        |       77 | -24.11%  | 3.64%              | -44.23% |    -0.44 | 42.26%     | ok               |
| COST       |       62 | 9.37%    | 43.03%             | -29.73% |     0.34 | 47.59%     | ok               |
| CRM        |       67 | -32.89%  | -23.15%            | -41.46% |    -0.64 | 44.26%     | ok               |
| CRV-USD    |       62 | 4.42%    | -78.63%            | -39.89% |     0.27 | 31.80%     | ok               |
| CSCO       |       59 | 32.99%   | 156.46%            | -21.79% |     0.67 | 48.59%     | ok               |
| CVX        |       73 | -18.64%  | 28.72%             | -29.70% |    -0.49 | 41.93%     | ok               |
| DASH-USD   |       65 | -44.95%  | -1.34%             | -64.43% |    -0.06 | 30.46%     | ok               |
| DBC        |       62 | -13.57%  | 37.10%             | -25.70% |    -0.47 | 33.44%     | ok               |
| DE         |       74 | -10.48%  | 47.31%             | -25.24% |    -0.15 | 45.26%     | ok               |
| DIA        |       58 | -1.73%   | 37.01%             | -12.94% |    -0.06 | 46.09%     | ok               |
| DIS        |       59 | 2.59%    | 13.09%             | -22.67% |     0.16 | 47.42%     | ok               |
| DOGE-USD   |       77 | -21.98%  | -70.33%            | -60.95% |     0.03 | 48.66%     | ok               |
| DOT-USD    |       88 | -46.93%  | -84.13%            | -57.66% |    -0.34 | 46.74%     | ok               |
| DXY-INDEX  |       44 | -4.08%   | -3.87%             | -6.06%  |    -0.67 | 26.90%     | ok               |
| EEM        |       64 | -9.40%   | 81.59%             | -25.67% |    -0.25 | 43.43%     | ok               |
| EFA        |       58 | -8.43%   | 41.36%             | -13.53% |    -0.31 | 43.59%     | ok               |
| EOG        |       83 | -29.95%  | 19.39%             | -48.13% |    -0.69 | 47.75%     | ok               |
| ETC-USD    |       70 | -46.10%  | -69.83%            | -54.25% |    -0.78 | 30.27%     | ok               |
| ETH-USD    |       62 | 127.90%  | -44.36%            | -30.11% |     1.15 | 43.49%     | ok               |
| EWJ        |       64 | -18.27%  | 46.06%             | -30.73% |    -0.59 | 41.43%     | ok               |
| FCX        |       73 | -28.75%  | 71.99%             | -48.31% |    -0.34 | 45.42%     | ok               |
| FET-USD    |       77 | -13.29%  | -80.84%            | -48.39% |     0.16 | 39.46%     | ok               |
| FIL-USD    |       70 | -26.60%  | -82.27%            | -46.68% |    -0.16 | 32.76%     | ok               |
| FXI        |       48 | -13.95%  | 61.74%             | -24.33% |    -0.29 | 26.79%     | ok               |
| GDX        |       60 | 5.77%    | 201.85%            | -34.99% |     0.22 | 49.08%     | ok               |
| GDXJ       |       68 | -21.59%  | 228.00%            | -44.93% |    -0.21 | 46.59%     | ok               |
| GE         |       74 | 6.39%    | 209.13%            | -27.82% |     0.23 | 51.58%     | ok               |
| GLD        |       50 | 18.75%   | 119.20%            | -16.63% |     0.53 | 43.59%     | ok               |
| GOOGL      |       65 | 75.11%   | 156.72%            | -20.41% |     1.12 | 55.24%     | ok               |
| GRT-USD    |       89 | -24.54%  | -88.72%            | -57.25% |    -0.08 | 41.19%     | ok               |
| GS         |       76 | 0.17%    | 177.42%            | -22.13% |     0.1  | 50.58%     | ok               |
| HD         |       69 | -1.60%   | -10.01%            | -17.69% |     0.04 | 45.26%     | ok               |
| HON        |       95 | -19.92%  | 23.78%             | -28.64% |    -0.53 | 51.91%     | ok               |
| HYG        |       83 | -9.54%   | 3.46%              | -10.06% |    -1.11 | 34.78%     | ok               |
| IBIT       |       30 | 35.78%   | 0.11%              | -18.95% |     0.79 | 29.25%     | ok               |
| IBM        |       72 | 59.50%   | 105.67%            | -25.31% |     1.06 | 50.75%     | ok               |
| ICP-USD    |       81 | 20.76%   | -69.67%            | -50.29% |     0.43 | 37.16%     | ok               |
| IEF        |       80 | -11.63%  | -1.43%             | -12.27% |    -1.63 | 33.28%     | ok               |
| IEMG       |       58 | -5.52%   | 75.03%             | -26.84% |    -0.12 | 43.59%     | ok               |
| INJ-USD    |       77 | -54.25%  | -67.93%            | -79.29% |    -0.55 | 38.31%     | ok               |
| INTC       |       70 | 53.88%   | 124.62%            | -60.60% |     0.61 | 49.75%     | ok               |
| INTU       |       67 | -14.99%  | -46.77%            | -43.77% |    -0.14 | 42.93%     | ok               |
| ITA        |       70 | 1.79%    | 87.97%             | -23.75% |     0.12 | 45.76%     | ok               |
| IWM        |       50 | 9.94%    | 49.59%             | -12.83% |     0.4  | 36.77%     | ok               |
| JNJ        |       76 | 2.06%    | 37.90%             | -17.51% |     0.13 | 51.41%     | ok               |
| JPM        |       77 | -24.37%  | 76.35%             | -33.02% |    -0.65 | 52.75%     | ok               |
| KO         |       49 | 23.27%   | 30.68%             | -8.07%  |     0.88 | 37.27%     | ok               |
| LDO-USD    |       80 | -17.45%  | -83.00%            | -60.93% |     0.11 | 36.97%     | ok               |
| LIN        |       72 | -3.07%   | 21.94%             | -21.53% |    -0.05 | 39.27%     | ok               |
| LINK-USD   |       72 | -21.89%  | -59.86%            | -55.61% |    -0.01 | 40.23%     | ok               |
| LLY        |       69 | -15.72%  | 70.13%             | -53.34% |    -0.14 | 51.41%     | ok               |
| LRCX       |       82 | -15.93%  | 344.68%            | -63.56% |    -0.07 | 46.09%     | ok               |
| LTC-USD    |       67 | -40.78%  | -51.72%            | -55.04% |    -0.42 | 46.93%     | ok               |
| MCD        |       75 | -2.11%   | -4.99%             | -19.14% |    -0.03 | 38.94%     | ok               |
| META       |       72 | -2.46%   | 67.20%             | -36.21% |     0.1  | 52.08%     | ok               |
| MPC        |       71 | -13.74%  | 70.48%             | -44.76% |    -0.14 | 49.92%     | ok               |
| MRK        |       67 | -20.82%  | -2.35%             | -32.14% |    -0.44 | 47.09%     | ok               |
| MS         |       81 | -16.72%  | 133.52%            | -26.72% |    -0.36 | 46.92%     | ok               |
| MSFT       |       76 | -28.99%  | 17.44%             | -33.48% |    -0.74 | 47.42%     | ok               |
| MU         |       55 | 237.76%  | 1176.97%           | -68.76% |     1.32 | 58.57%     | ok               |
| NEAR-USD   |       91 | -10.41%  | -46.78%            | -60.07% |     0.16 | 42.91%     | ok               |
| NEM        |       72 | -18.69%  | 183.09%            | -38.49% |    -0.11 | 55.74%     | ok               |
| NFLX       |       64 | 21.64%   | 72.85%             | -21.09% |     0.53 | 54.58%     | ok               |
| NKE        |       93 | -37.58%  | -57.44%            | -55.35% |    -0.52 | 45.42%     | ok               |
| NOW        |       78 | 26.82%   | -8.65%             | -31.32% |     0.48 | 46.09%     | ok               |
| NVDA       |       74 | -26.45%  | 140.45%            | -45.02% |    -0.18 | 60.96%     | ok               |
| OP-USD     |       76 | -8.19%   | -93.53%            | -70.11% |     0.16 | 35.44%     | ok               |
| ORCL       |       70 | 89.79%   | 136.01%            | -29.47% |     0.85 | 52.25%     | ok               |
| OXY        |       73 | -4.86%   | 2.84%              | -34.69% |     0.03 | 44.76%     | ok               |
| PEP        |       85 | -9.45%   | -15.06%            | -21.35% |    -0.22 | 48.92%     | ok               |
| PEPE-USD   |       79 | -4.17%   | -82.44%            | -57.66% |     0.24 | 42.53%     | ok               |
| PFE        |       77 | -38.05%  | -13.10%            | -42.29% |    -1.18 | 37.27%     | ok               |
| PG         |       61 | -9.90%   | -5.68%             | -20.33% |    -0.36 | 40.43%     | ok               |
| PM         |       81 | -1.20%   | 81.67%             | -34.41% |     0.07 | 56.74%     | ok               |
| POL-USD    |       80 | 44.01%   | -80.50%            | -46.45% |     0.62 | 47.32%     | ok               |
| QCOM       |       81 | -5.73%   | 72.16%             | -57.69% |     0.09 | 48.59%     | ok               |
| QQQ        |       60 | 25.24%   | 83.90%             | -12.88% |     0.7  | 46.26%     | ok               |
| RENDER-USD |       94 | -5.83%   | -48.94%            | -45.00% |     0.23 | 44.87%     | ok               |
| RTX        |       58 | 18.66%   | 103.10%            | -16.99% |     0.51 | 52.25%     | ok               |
| SBUX       |       65 | -23.46%  | 2.60%              | -31.15% |    -0.47 | 40.43%     | ok               |
| SCHW       |       74 | -21.97%  | 31.25%             | -30.41% |    -0.52 | 45.42%     | ok               |
| SHIB-USD   |       78 | -37.46%  | -75.40%            | -48.95% |    -0.3  | 50.77%     | ok               |
| SHY        |       52 | -2.22%   | 0.04%              | -2.85%  |    -0.75 | 37.10%     | ok               |
| SKY-USD    |       66 | -29.93%  | 16.55%             | -43.98% |    -0.42 | 39.42%     | ok               |
| SLB        |       77 | -31.21%  | 16.47%             | -54.23% |    -0.56 | 51.91%     | ok               |
| SLV        |       58 | 36.93%   | 223.76%            | -42.66% |     0.58 | 40.60%     | ok               |
| SMH        |       50 | 96.77%   | 266.67%            | -33.99% |     1.2  | 51.91%     | ok               |
| SNX-USD    |       67 | 13.75%   | -86.49%            | -32.91% |     0.37 | 39.27%     | ok               |
| SOL-USD    |       70 | -43.45%  | -60.50%            | -56.90% |    -0.25 | 58.81%     | ok               |
| SOXX       |       57 | 86.77%   | 224.30%            | -40.34% |     1.07 | 51.08%     | ok               |
| SPY        |       60 | 10.62%   | 60.29%             | -16.47% |     0.42 | 50.92%     | ok               |
| SUSHI-USD  |       93 | -78.29%  | -85.08%            | -79.09% |    -1.21 | 35.44%     | ok               |
| T          |       66 | 17.39%   | 45.37%             | -17.01% |     0.49 | 49.25%     | ok               |
| TGT        |       58 | -13.22%  | -14.32%            | -40.57% |    -0.2  | 39.27%     | ok               |
| TIA-USD    |       78 | -7.24%   | -92.36%            | -54.46% |     0.18 | 32.95%     | ok               |
| TLT        |       70 | -22.73%  | -11.35%            | -24.69% |    -1.65 | 33.44%     | ok               |
| TMO        |       57 | 20.00%   | -11.03%            | -16.83% |     0.49 | 49.92%     | ok               |
| TMUS       |       68 | 19.83%   | 15.70%             | -24.50% |     0.5  | 48.92%     | ok               |
| TRX-USD    |       70 | -2.64%   | 29.48%             | -22.90% |     0.03 | 49.23%     | ok               |
| TSLA       |       68 | 8.00%    | 80.35%             | -57.89% |     0.29 | 44.09%     | ok               |
| TXN        |       73 | -5.80%   | 82.72%             | -46.98% |     0.06 | 53.74%     | ok               |
| UNH        |       78 | 14.41%   | -29.80%            | -32.80% |     0.34 | 52.25%     | ok               |
| UNI-USD    |       92 | -69.35%  | -78.25%            | -79.17% |    -0.77 | 40.04%     | ok               |
| UPS        |       66 | -35.02%  | -31.89%            | -40.62% |    -0.71 | 38.10%     | ok               |
| USO        |       68 | 2.80%    | 103.69%            | -43.35% |     0.17 | 34.44%     | ok               |
| VEA        |       60 | -2.87%   | 53.25%             | -19.49% |    -0.07 | 43.43%     | ok               |
| VIXY       |       92 | -77.59%  | -60.34%            | -87.63% |    -0.92 | 30.95%     | ok               |
| VNQ        |       77 | -17.89%  | 8.32%              | -24.92% |    -0.76 | 37.77%     | ok               |
| VTI        |       70 | 1.26%    | 58.62%             | -18.77% |     0.1  | 52.25%     | ok               |
| VWO        |       76 | -13.41%  | 52.63%             | -25.20% |    -0.47 | 44.09%     | ok               |
| VZ         |       83 | -19.52%  | 22.62%             | -31.88% |    -0.57 | 39.77%     | ok               |
| WFC        |       84 | -22.35%  | 61.17%             | -30.22% |    -0.42 | 47.09%     | ok               |
| WIF-USD    |       72 | -36.24%  | -90.33%            | -50.40% |    -0.13 | 31.03%     | ok               |
| WMT        |       55 | 39.66%   | 112.91%            | -21.31% |     1.01 | 53.24%     | ok               |
| XBI        |       64 | -8.11%   | 36.50%             | -20.48% |    -0.12 | 40.10%     | ok               |
| XLB        |       66 | -10.52%  | 23.06%             | -24.41% |    -0.34 | 36.77%     | ok               |
| XLC        |       63 | 20.34%   | 55.55%             | -12.33% |     0.67 | 56.91%     | ok               |
| XLE        |       79 | -10.75%  | 40.75%             | -37.64% |    -0.2  | 46.92%     | ok               |
| XLF        |       76 | -16.62%  | 36.32%             | -24.78% |    -0.63 | 49.42%     | ok               |
| XLI        |       66 | 5.94%    | 55.79%             | -11.38% |     0.28 | 47.92%     | ok               |
| XLK        |       40 | 89.57%   | 109.70%            | -14.75% |     1.56 | 48.92%     | ok               |
| XLM-USD    |       69 | 22.08%   | -32.87%            | -41.96% |     0.44 | 47.51%     | ok               |
| XLP        |       72 | 5.85%    | 12.51%             | -10.28% |     0.36 | 44.09%     | ok               |
| XLU        |       69 | -6.01%   | 36.19%             | -15.29% |    -0.23 | 38.44%     | ok               |
| XLV        |       66 | -8.93%   | 4.33%              | -14.23% |    -0.42 | 37.60%     | ok               |
| XLY        |       76 | -0.80%   | 34.46%             | -14.01% |     0.04 | 44.59%     | ok               |
| XOM        |       61 | -0.77%   | 50.06%             | -20.29% |     0.05 | 36.77%     | ok               |
| XRP-USD    |       64 | -41.34%  | -41.24%            | -54.34% |    -0.47 | 35.25%     | ok               |
| YFI-USD    |       85 | -57.18%  | -74.38%            | -67.78% |    -0.94 | 38.89%     | ok               |
| ZEC-USD    |       67 | 46.51%   | 952.55%            | -46.93% |     0.57 | 36.40%     | ok               |

## AAPL Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 26.97%   | 70.25%             | -21.71% |     0.58 |       69 | 53.74%     | ok               |
|          15 | 22.70%   | 70.25%             | -23.86% |     0.5  |       75 | 61.23%     | ok               |
|          25 | 20.90%   | 70.25%             | -20.03% |     0.49 |       67 | 51.58%     | ok               |
|          30 | 14.81%   | 70.25%             | -20.65% |     0.39 |       67 | 49.08%     | ok               |
|          35 | 12.17%   | 70.25%             | -22.04% |     0.34 |       63 | 46.09%     | ok               |

## AAVE-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -5.65%   | -77.68%            | -43.61% |     0.14 |       38 | 27.59%     | ok               |
|          45 | -6.07%   | -77.68%            | -46.87% |     0.12 |       36 | 24.71%     | ok               |
|          35 | -29.05%  | -77.68%            | -51.96% |    -0.18 |       52 | 30.27%     | ok               |
|          50 | -33.22%  | -77.68%            | -47.78% |    -0.36 |       38 | 19.35%     | ok               |
|          15 | -60.95%  | -77.68%            | -66.51% |    -0.54 |       82 | 48.66%     | ok               |

## ABBV Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -5.03%   | 32.71%             | -26.16% |    -0.05 |       48 | 38.94%     | ok               |
|          40 | -14.24%  | 32.71%             | -26.61% |    -0.3  |       62 | 43.59%     | ok               |
|          35 | -15.49%  | 32.71%             | -27.83% |    -0.32 |       66 | 46.42%     | ok               |
|          30 | -17.68%  | 32.71%             | -30.55% |    -0.37 |       64 | 49.25%     | ok               |
|          45 | -16.92%  | 32.71%             | -29.59% |    -0.38 |       52 | 40.93%     | ok               |

## ADA-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -87.27%  | -75.01%            | -91.83% |    -0.74 |       82 | 61.11%     | ok               |
|          20 | -87.28%  | -75.01%            | -92.33% |    -0.76 |       86 | 56.32%     | ok               |
|          50 | -83.55%  | -75.01%            | -88.20% |    -0.83 |       55 | 26.82%     | ok               |
|          25 | -88.41%  | -75.01%            | -92.37% |    -0.85 |       87 | 52.87%     | ok               |
|          30 | -86.58%  | -75.01%            | -91.71% |    -0.85 |       86 | 45.40%     | ok               |

## ADBE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 10.63%   | -55.29%            | -21.34% |     0.3  |       76 | 49.25%     | ok               |
|          40 | -3.65%   | -55.29%            | -20.88% |     0.05 |       72 | 42.26%     | ok               |
|          25 | -9.10%   | -55.29%            | -32.60% |     0.01 |       50 | 61.23%     | ok               |
|          15 | -18.75%  | -55.29%            | -33.11% |    -0.14 |       59 | 65.89%     | ok               |
|          20 | -20.39%  | -55.29%            | -35.67% |    -0.17 |       50 | 63.39%     | ok               |

## AGG Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -6.84%   | 0.16%              | -10.16% |    -1.11 |       71 | 31.78%     | ok               |
|          20 | -7.81%   | 0.16%              | -10.67% |    -1.12 |       77 | 37.60%     | ok               |
|          25 | -8.10%   | 0.16%              | -11.31% |    -1.21 |       75 | 35.77%     | ok               |
|          45 | -6.57%   | 0.16%              | -7.89%  |    -1.3  |       56 | 20.97%     | ok               |
|          15 | -9.55%   | 0.16%              | -12.18% |    -1.35 |       84 | 41.10%     | ok               |

## ALGO-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -52.60%  | -65.62%            | -61.76% |    -0.61 |       84 | 38.31%     | ok               |
|          15 | -62.01%  | -65.62%            | -70.86% |    -0.67 |       80 | 50.00%     | ok               |
|          25 | -62.11%  | -65.62%            | -75.14% |    -0.72 |       86 | 45.59%     | ok               |
|          20 | -66.03%  | -65.62%            | -73.99% |    -0.8  |       84 | 47.89%     | ok               |
|          35 | -55.82%  | -65.62%            | -58.56% |    -0.81 |       62 | 31.23%     | ok               |

## AMAT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -5.33%   | 224.47%            | -54.69% |     0.12 |       66 | 62.40%     | ok               |
|          30 | -19.38%  | 224.47%            | -57.80% |    -0.1  |       67 | 53.58%     | ok               |
|          20 | -25.27%  | 224.47%            | -60.72% |    -0.17 |       70 | 58.74%     | ok               |
|          35 | -25.12%  | 224.47%            | -55.89% |    -0.21 |       69 | 51.41%     | ok               |
|          25 | -28.77%  | 224.47%            | -60.95% |    -0.25 |       69 | 56.41%     | ok               |

## AMD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 45.53%   | 249.42%            | -47.17% |     0.59 |       56 | 38.94%     | ok               |
|          50 | 36.01%   | 249.42%            | -48.79% |     0.53 |       60 | 33.44%     | ok               |
|          35 | 26.97%   | 249.42%            | -54.57% |     0.45 |       62 | 40.93%     | ok               |
|          45 | 16.26%   | 249.42%            | -56.22% |     0.36 |       64 | 36.27%     | ok               |
|          30 | 10.23%   | 249.42%            | -59.88% |     0.31 |       63 | 43.43%     | ok               |

## AMGN Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -13.22%  | 6.83%              | -26.64% |    -0.19 |       73 | 55.74%     | ok               |
|          15 | -16.05%  | 6.83%              | -27.92% |    -0.24 |       70 | 61.73%     | ok               |
|          35 | -14.61%  | 6.83%              | -31.23% |    -0.25 |       67 | 45.76%     | ok               |
|          30 | -18.60%  | 6.83%              | -34.14% |    -0.35 |       71 | 49.58%     | ok               |
|          25 | -21.91%  | 6.83%              | -33.41% |    -0.43 |       67 | 51.91%     | ok               |

## AMZN Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -17.83%  | 69.47%             | -28.70% |    -0.52 |       50 | 29.78%     | ok               |
|          50 | -25.03%  | 69.47%             | -35.48% |    -0.88 |       48 | 24.13%     | ok               |
|          45 | -25.89%  | 69.47%             | -35.47% |    -0.89 |       50 | 26.96%     | ok               |
|          35 | -29.70%  | 69.47%             | -38.29% |    -0.91 |       62 | 32.95%     | ok               |
|          30 | -33.84%  | 69.47%             | -42.48% |    -0.99 |       74 | 38.27%     | ok               |

## APT-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 28.30%   | -90.62%            | -46.73% |     0.52 |       46 | 18.77%     | ok               |
|          45 | -16.69%  | -90.62%            | -64.17% |    -0.01 |       62 | 24.90%     | ok               |
|          40 | -35.44%  | -90.62%            | -63.33% |    -0.23 |       68 | 30.65%     | ok               |
|          20 | -45.15%  | -90.62%            | -70.51% |    -0.24 |       75 | 50.57%     | ok               |
|          35 | -41.64%  | -90.62%            | -64.48% |    -0.29 |       74 | 36.21%     | ok               |

## ARB-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 47.21%   | -87.54%            | -52.62% |     0.6  |       89 | 55.36%     | ok               |
|          40 | 40.06%   | -87.54%            | -45.37% |     0.58 |       52 | 29.31%     | ok               |
|          20 | 23.07%   | -87.54%            | -59.44% |     0.46 |       79 | 49.81%     | ok               |
|          35 | 23.41%   | -87.54%            | -54.93% |     0.45 |       66 | 33.33%     | ok               |
|          45 | 16.10%   | -87.54%            | -49.55% |     0.38 |       58 | 22.61%     | ok               |

## ARKK Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -30.53%  | 61.43%             | -38.41% |    -0.41 |       96 | 51.08%     | ok               |
|          20 | -30.68%  | 61.43%             | -34.90% |    -0.44 |       87 | 45.76%     | ok               |
|          30 | -30.02%  | 61.43%             | -32.63% |    -0.5  |       79 | 38.94%     | ok               |
|          35 | -31.21%  | 61.43%             | -33.79% |    -0.56 |       78 | 36.61%     | ok               |
|          40 | -32.66%  | 61.43%             | -34.78% |    -0.64 |       70 | 31.78%     | ok               |

## ATOM-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -63.50%  | -70.64%            | -68.50% |    -0.96 |       97 | 49.81%     | ok               |
|          15 | -67.93%  | -70.64%            | -74.68% |    -1    |       96 | 60.15%     | ok               |
|          30 | -64.89%  | -70.64%            | -68.64% |    -1.07 |       92 | 43.49%     | ok               |
|          20 | -71.28%  | -70.64%            | -74.33% |    -1.18 |      105 | 54.21%     | ok               |
|          35 | -64.69%  | -70.64%            | -64.37% |    -1.19 |       82 | 38.70%     | ok               |

## AVAX-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -0.47%   | -76.94%            | -29.53% |     0.16 |       32 | 18.58%     | ok               |
|          45 | -3.51%   | -76.94%            | -32.82% |     0.12 |       34 | 21.46%     | ok               |
|          35 | -6.81%   | -76.94%            | -36.30% |     0.11 |       60 | 29.69%     | ok               |
|          40 | -5.52%   | -76.94%            | -32.96% |     0.1  |       42 | 24.14%     | ok               |
|          15 | -18.86%  | -76.94%            | -50.68% |     0.05 |       65 | 51.15%     | ok               |

## AVGO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 47.16%   | 344.87%            | -35.76% |     0.63 |       60 | 47.25%     | ok               |
|          25 | 41.93%   | 344.87%            | -38.01% |     0.58 |       64 | 47.92%     | ok               |
|          35 | 34.65%   | 344.87%            | -36.19% |     0.53 |       72 | 44.43%     | ok               |
|          40 | 29.71%   | 344.87%            | -40.70% |     0.48 |       62 | 40.93%     | ok               |
|          20 | 28.52%   | 344.87%            | -40.10% |     0.47 |       72 | 50.75%     | ok               |

## BA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 18.43%   | -3.57%             | -15.40% |     0.51 |       46 | 31.78%     | ok               |
|          35 | 23.99%   | -3.57%             | -23.77% |     0.49 |       76 | 46.76%     | ok               |
|          25 | 5.33%    | -3.57%             | -32.48% |     0.22 |       74 | 54.91%     | ok               |
|          40 | 4.31%    | -3.57%             | -29.44% |     0.19 |       52 | 40.10%     | ok               |
|          30 | 2.28%    | -3.57%             | -30.56% |     0.17 |       71 | 51.41%     | ok               |

## BAC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -7.39%   | 56.05%             | -19.60% |    -0.18 |       60 | 33.61%     | ok               |
|          20 | -13.01%  | 56.05%             | -20.73% |    -0.25 |       80 | 50.42%     | ok               |
|          35 | -12.11%  | 56.05%             | -27.11% |    -0.3  |       72 | 41.60%     | ok               |
|          50 | -11.42%  | 56.05%             | -20.35% |    -0.35 |       58 | 30.78%     | ok               |
|          15 | -17.59%  | 56.05%             | -22.24% |    -0.36 |       82 | 55.41%     | ok               |

## BCH-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -42.26%  | -39.02%            | -61.84% |    -0.37 |       87 | 57.09%     | ok               |
|          30 | -37.71%  | -39.02%            | -58.22% |    -0.37 |       80 | 45.59%     | ok               |
|          20 | -41.33%  | -39.02%            | -59.44% |    -0.38 |       82 | 52.49%     | ok               |
|          25 | -42.31%  | -39.02%            | -61.30% |    -0.43 |       74 | 47.89%     | ok               |
|          40 | -42.56%  | -39.02%            | -62.46% |    -0.53 |       65 | 38.51%     | ok               |

## BITO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 17.67%   | -59.64%            | -32.29% |     0.38 |       52 | 24.13%     | ok               |
|          30 | 3.90%    | -59.64%            | -42.82% |     0.22 |       76 | 38.77%     | ok               |
|          15 | -2.62%   | -59.64%            | -48.38% |     0.17 |       85 | 47.59%     | ok               |
|          45 | -1.86%   | -59.64%            | -43.53% |     0.13 |       56 | 27.12%     | ok               |
|          25 | -4.32%   | -59.64%            | -41.73% |     0.13 |       80 | 41.76%     | ok               |

## BLK Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 5.83%    | 28.25%             | -14.19% |     0.24 |       78 | 38.27%     | ok               |
|          40 | 4.62%    | 28.25%             | -15.20% |     0.21 |       72 | 33.94%     | ok               |
|          20 | 1.46%    | 28.25%             | -17.89% |     0.12 |       75 | 46.92%     | ok               |
|          30 | -0.88%   | 28.25%             | -20.81% |     0.04 |       73 | 42.10%     | ok               |
|          25 | -1.87%   | 28.25%             | -19.84% |     0.02 |       73 | 44.43%     | ok               |

## BND Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -7.24%   | 0.19%              | -9.05%  |    -1.04 |       69 | 39.10%     | ok               |
|          25 | -7.62%   | 0.19%              | -10.14% |    -1.15 |       71 | 36.61%     | ok               |
|          15 | -8.98%   | 0.19%              | -10.58% |    -1.27 |       73 | 42.43%     | ok               |
|          30 | -8.06%   | 0.19%              | -9.89%  |    -1.28 |       69 | 32.78%     | ok               |
|          45 | -8.27%   | 0.19%              | -9.57%  |    -1.58 |       52 | 22.13%     | ok               |

## BONK-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 131.84%  | -83.65%            | -35.57% |     1.1  |       44 | 21.26%     | ok               |
|          20 | 161.34%  | -83.65%            | -55.43% |     1.01 |       68 | 51.34%     | ok               |
|          25 | 143.82%  | -83.65%            | -47.99% |     0.97 |       67 | 46.55%     | ok               |
|          15 | 152.82%  | -83.65%            | -63.45% |     0.96 |       69 | 55.75%     | ok               |
|          45 | 70.97%   | -83.65%            | -42.36% |     0.77 |       56 | 25.10%     | ok               |

## BTC-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 39.52%   | -28.50%            | -18.97% |     0.76 |       46 | 32.95%     | ok               |
|          45 | 36.21%   | -28.50%            | -19.59% |     0.75 |       44 | 29.31%     | ok               |
|          35 | 20.57%   | -28.50%            | -31.52% |     0.47 |       70 | 40.04%     | ok               |
|          50 | 14.92%   | -28.50%            | -17.58% |     0.41 |       40 | 25.29%     | ok               |
|          30 | 3.53%    | -28.50%            | -27.92% |     0.2  |       72 | 46.93%     | ok               |

## C Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -11.29%  | 145.44%            | -21.64% |    -0.26 |       68 | 34.78%     | ok               |
|          15 | -26.59%  | 145.44%            | -34.03% |    -0.47 |       76 | 59.90%     | ok               |
|          25 | -25.28%  | 145.44%            | -33.47% |    -0.47 |       75 | 53.08%     | ok               |
|          45 | -19.77%  | 145.44%            | -29.28% |    -0.48 |       82 | 39.27%     | ok               |
|          20 | -27.16%  | 145.44%            | -34.53% |    -0.51 |       81 | 56.24%     | ok               |

## CAT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 28.78%   | 211.27%            | -21.02% |     0.55 |       74 | 57.90%     | ok               |
|          25 | 28.90%   | 211.27%            | -26.37% |     0.54 |       70 | 60.73%     | ok               |
|          20 | 26.29%   | 211.27%            | -25.65% |     0.51 |       80 | 64.06%     | ok               |
|          45 | 20.52%   | 211.27%            | -28.85% |     0.45 |       58 | 46.26%     | ok               |
|          50 | 17.92%   | 211.27%            | -26.39% |     0.42 |       60 | 43.76%     | ok               |

## CL Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 20.05%   | 9.22%              | -14.32% |     0.67 |       60 | 49.42%     | ok               |
|          50 | 15.26%   | 9.22%              | -12.98% |     0.63 |       44 | 33.11%     | ok               |
|          45 | 15.52%   | 9.22%              | -13.51% |     0.62 |       46 | 36.11%     | ok               |
|          35 | 14.34%   | 9.22%              | -13.83% |     0.52 |       62 | 45.76%     | ok               |
|          25 | 14.12%   | 9.22%              | -14.29% |     0.49 |       58 | 50.75%     | ok               |

## CMCSA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -37.95%  | -38.74%            | -48.76% |    -0.88 |       84 | 58.40%     | ok               |
|          30 | -36.01%  | -38.74%            | -39.80% |    -0.9  |       80 | 44.26%     | ok               |
|          20 | -41.79%  | -38.74%            | -46.96% |    -1.04 |       91 | 54.74%     | ok               |
|          25 | -40.86%  | -38.74%            | -44.37% |    -1.04 |       85 | 48.92%     | ok               |
|          50 | -29.51%  | -38.74%            | -33.68% |    -1.08 |       50 | 17.14%     | ok               |

## COMP-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -18.16%  | -77.12%            | -38.71% |    -0.05 |       48 | 20.31%     | ok               |
|          25 | -44.61%  | -77.12%            | -63.29% |    -0.3  |       93 | 50.00%     | ok               |
|          30 | -43.66%  | -77.12%            | -63.55% |    -0.32 |       93 | 44.64%     | ok               |
|          15 | -51.85%  | -77.12%            | -67.05% |    -0.38 |      109 | 61.88%     | ok               |
|          40 | -43.39%  | -77.12%            | -47.33% |    -0.42 |       76 | 32.76%     | ok               |

## COP Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -12.78%  | 3.64%              | -34.85% |    -0.22 |       50 | 28.79%     | ok               |
|          45 | -18.18%  | 3.64%              | -40.87% |    -0.36 |       62 | 31.78%     | ok               |
|          35 | -22.10%  | 3.64%              | -43.32% |    -0.4  |       75 | 38.60%     | ok               |
|          30 | -24.11%  | 3.64%              | -44.23% |    -0.44 |       77 | 42.26%     | ok               |
|          40 | -26.13%  | 3.64%              | -46.62% |    -0.56 |       70 | 34.28%     | ok               |

## COST Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | 21.60%   | 43.03%             | -24.73% |     0.63 |       63 | 51.08%     | ok               |
|          20 | 20.98%   | 43.03%             | -24.32% |     0.6  |       64 | 53.58%     | ok               |
|          35 | 14.61%   | 43.03%             | -26.58% |     0.49 |       56 | 44.59%     | ok               |
|          30 | 9.37%    | 43.03%             | -29.73% |     0.34 |       62 | 47.59%     | ok               |
|          40 | 7.58%    | 43.03%             | -28.41% |     0.3  |       58 | 41.60%     | ok               |

## CRM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -27.55%  | -23.15%            | -38.20% |    -0.38 |       92 | 55.74%     | ok               |
|          35 | -21.86%  | -23.15%            | -36.72% |    -0.39 |       64 | 39.43%     | ok               |
|          40 | -27.53%  | -23.15%            | -41.30% |    -0.59 |       70 | 35.44%     | ok               |
|          30 | -32.89%  | -23.15%            | -41.46% |    -0.64 |       67 | 44.26%     | ok               |
|          20 | -38.24%  | -23.15%            | -42.88% |    -0.69 |       80 | 49.42%     | ok               |

## CRV-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 30.68%   | -78.63%            | -37.78% |     0.51 |       62 | 27.39%     | ok               |
|          50 | 15.81%   | -78.63%            | -29.30% |     0.37 |       38 | 16.09%     | ok               |
|          40 | 14.75%   | -78.63%            | -38.86% |     0.36 |       52 | 23.75%     | ok               |
|          30 | 4.42%    | -78.63%            | -39.89% |     0.27 |       62 | 31.80%     | ok               |
|          45 | 4.51%    | -78.63%            | -42.29% |     0.24 |       52 | 18.77%     | ok               |

## CSCO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 38.41%   | 156.46%            | -19.34% |     0.82 |       56 | 37.77%     | ok               |
|          45 | 34.82%   | 156.46%            | -19.34% |     0.74 |       51 | 39.93%     | ok               |
|          30 | 32.99%   | 156.46%            | -21.79% |     0.67 |       59 | 48.59%     | ok               |
|          25 | 32.64%   | 156.46%            | -23.28% |     0.66 |       65 | 50.75%     | ok               |
|          35 | 30.48%   | 156.46%            | -23.68% |     0.63 |       51 | 46.26%     | ok               |

## CVX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -14.25%  | 28.72%             | -25.91% |    -0.33 |       72 | 44.43%     | ok               |
|          35 | -16.76%  | 28.72%             | -28.85% |    -0.44 |       69 | 39.10%     | ok               |
|          20 | -18.37%  | 28.72%             | -30.41% |    -0.45 |       78 | 45.92%     | ok               |
|          30 | -18.64%  | 28.72%             | -29.70% |    -0.49 |       73 | 41.93%     | ok               |
|          40 | -17.80%  | 28.72%             | -28.41% |    -0.52 |       79 | 36.11%     | ok               |

## DASH-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 109.52%  | -1.34%             | -34.71% |     0.88 |       42 | 15.90%     | ok               |
|          40 | 64.67%   | -1.34%             | -34.44% |     0.67 |       46 | 22.61%     | ok               |
|          45 | 51.31%   | -1.34%             | -42.52% |     0.6  |       46 | 18.20%     | ok               |
|          25 | -35.92%  | -1.34%             | -64.14% |     0.06 |       71 | 33.52%     | ok               |
|          35 | -39.92%  | -1.34%             | -63.23% |     0    |       71 | 27.01%     | ok               |

## DBC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -7.75%   | 37.10%             | -20.31% |    -0.29 |       40 | 21.13%     | ok               |
|          45 | -9.53%   | 37.10%             | -21.46% |    -0.33 |       54 | 24.63%     | ok               |
|          35 | -10.31%  | 37.10%             | -23.91% |    -0.34 |       60 | 31.45%     | ok               |
|          15 | -12.29%  | 37.10%             | -26.60% |    -0.4  |       65 | 38.10%     | ok               |
|          30 | -13.57%  | 37.10%             | -25.70% |    -0.47 |       62 | 33.44%     | ok               |

## DE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -7.86%   | 47.31%             | -28.94% |    -0.08 |       74 | 51.08%     | ok               |
|          25 | -9.27%   | 47.31%             | -26.67% |    -0.12 |       76 | 48.25%     | ok               |
|          30 | -10.48%  | 47.31%             | -25.24% |    -0.15 |       74 | 45.26%     | ok               |
|          50 | -8.16%   | 47.31%             | -24.93% |    -0.16 |       66 | 29.28%     | ok               |
|          45 | -10.97%  | 47.31%             | -28.13% |    -0.21 |       68 | 34.28%     | ok               |

## DIA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -0.08%   | 37.01%             | -11.28% |     0.04 |       58 | 47.42%     | ok               |
|          35 | -0.08%   | 37.01%             | -13.15% |     0.03 |       60 | 44.26%     | ok               |
|          30 | -1.73%   | 37.01%             | -12.94% |    -0.06 |       58 | 46.09%     | ok               |
|          20 | -2.90%   | 37.01%             | -14.29% |    -0.11 |       60 | 49.92%     | ok               |
|          40 | -3.91%   | 37.01%             | -15.06% |    -0.19 |       66 | 41.26%     | ok               |

## DIS Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 40.04%   | 13.09%             | -14.24% |     0.96 |       46 | 30.12%     | ok               |
|          45 | 9.81%    | 13.09%             | -15.09% |     0.3  |       49 | 33.44%     | ok               |
|          40 | 8.82%    | 13.09%             | -22.77% |     0.28 |       61 | 38.60%     | ok               |
|          35 | 5.61%    | 13.09%             | -20.85% |     0.21 |       69 | 44.43%     | ok               |
|          15 | 2.91%    | 13.09%             | -25.87% |     0.17 |       87 | 58.07%     | ok               |

## DOGE-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 6.53%    | -70.33%            | -57.89% |     0.35 |       83 | 64.56%     | ok               |
|          20 | -5.31%   | -70.33%            | -55.83% |     0.23 |       86 | 60.34%     | ok               |
|          25 | -9.60%   | -70.33%            | -53.72% |     0.18 |       74 | 54.21%     | ok               |
|          30 | -21.98%  | -70.33%            | -60.95% |     0.03 |       77 | 48.66%     | ok               |
|          35 | -48.91%  | -70.33%            | -67.40% |    -0.43 |       74 | 41.95%     | ok               |

## DOT-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -24.98%  | -84.13%            | -43.91% |    -0.21 |       54 | 26.25%     | ok               |
|          45 | -29.59%  | -84.13%            | -48.71% |    -0.26 |       50 | 29.69%     | ok               |
|          30 | -46.93%  | -84.13%            | -57.66% |    -0.34 |       88 | 46.74%     | ok               |
|          35 | -45.90%  | -84.13%            | -59.34% |    -0.35 |       78 | 40.04%     | ok               |
|          40 | -37.31%  | -84.13%            | -48.60% |    -0.35 |       56 | 33.14%     | ok               |

## DXY-INDEX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -6.16%   | -3.87%             | -12.09% |    -0.57 |       90 | 75.49%     | ok               |
|          40 | -4.58%   | -3.87%             | -7.30%  |    -0.58 |       70 | 45.77%     | ok               |
|          30 | -5.29%   | -3.87%             | -10.51% |    -0.6  |       68 | 57.92%     | ok               |
|          45 | -4.78%   | -3.87%             | -8.12%  |    -0.66 |       66 | 35.36%     | ok               |
|          50 | -4.08%   | -3.87%             | -6.06%  |    -0.67 |       44 | 26.90%     | ok               |

## EEM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -4.96%   | 81.59%             | -19.52% |    -0.11 |       64 | 39.77%     | ok               |
|          35 | -5.62%   | 81.59%             | -23.88% |    -0.12 |       66 | 41.76%     | ok               |
|          50 | -4.94%   | 81.59%             | -15.88% |    -0.12 |       52 | 35.77%     | ok               |
|          45 | -6.04%   | 81.59%             | -17.36% |    -0.16 |       54 | 37.44%     | ok               |
|          30 | -9.40%   | 81.59%             | -25.67% |    -0.25 |       64 | 43.43%     | ok               |

## EFA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -1.76%   | 41.36%             | -11.27% |    -0    |       58 | 51.41%     | ok               |
|          20 | -7.98%   | 41.36%             | -12.37% |    -0.26 |       63 | 48.59%     | ok               |
|          30 | -8.43%   | 41.36%             | -13.53% |    -0.31 |       58 | 43.59%     | ok               |
|          25 | -10.49%  | 41.36%             | -15.78% |    -0.39 |       62 | 46.26%     | ok               |
|          50 | -9.33%   | 41.36%             | -17.80% |    -0.41 |       56 | 36.44%     | ok               |

## EOG Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -29.95%  | 19.39%             | -48.13% |    -0.69 |       83 | 47.75%     | ok               |
|          25 | -31.71%  | 19.39%             | -51.99% |    -0.7  |       84 | 51.08%     | ok               |
|          40 | -28.13%  | 19.39%             | -43.26% |    -0.72 |       64 | 36.77%     | ok               |
|          45 | -28.02%  | 19.39%             | -43.17% |    -0.76 |       58 | 33.28%     | ok               |
|          35 | -30.72%  | 19.39%             | -46.26% |    -0.77 |       81 | 42.43%     | ok               |

## ETC-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -14.16%  | -69.83%            | -30.24% |    -0.14 |       26 | 16.86%     | ok               |
|          35 | -26.76%  | -69.83%            | -42.62% |    -0.35 |       46 | 25.67%     | ok               |
|          45 | -27.00%  | -69.83%            | -36.69% |    -0.42 |       28 | 18.20%     | ok               |
|          40 | -30.87%  | -69.83%            | -41.87% |    -0.5  |       42 | 21.65%     | ok               |
|          30 | -46.10%  | -69.83%            | -54.25% |    -0.78 |       70 | 30.27%     | ok               |

## ETH-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 127.90%  | -44.36%            | -30.11% |     1.15 |       62 | 43.49%     | ok               |
|          30 | 120.28%  | -44.36%            | -32.89% |     1.07 |       66 | 51.34%     | ok               |
|          40 | 44.12%   | -44.36%            | -33.11% |     0.65 |       58 | 36.02%     | ok               |
|          50 | 31.75%   | -44.36%            | -30.50% |     0.55 |       54 | 26.44%     | ok               |
|          45 | 26.93%   | -44.36%            | -34.50% |     0.5  |       54 | 32.18%     | ok               |

## EWJ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -18.27%  | 46.06%             | -30.73% |    -0.59 |       64 | 41.43%     | ok               |
|          20 | -19.65%  | 46.06%             | -31.32% |    -0.62 |       60 | 43.43%     | ok               |
|          25 | -21.97%  | 46.06%             | -31.18% |    -0.72 |       60 | 42.43%     | ok               |
|          35 | -22.19%  | 46.06%             | -32.54% |    -0.75 |       70 | 39.77%     | ok               |
|          15 | -24.97%  | 46.06%             | -32.24% |    -0.78 |       74 | 46.59%     | ok               |

## FCX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -5.10%   | 71.99%             | -27.80% |     0.04 |       58 | 29.28%     | ok               |
|          45 | -9.66%   | 71.99%             | -35.28% |    -0.03 |       60 | 33.78%     | ok               |
|          40 | -22.55%  | 71.99%             | -44.23% |    -0.25 |       70 | 38.77%     | ok               |
|          30 | -28.75%  | 71.99%             | -48.31% |    -0.34 |       73 | 45.42%     | ok               |
|          20 | -32.02%  | 71.99%             | -57.65% |    -0.35 |       80 | 52.91%     | ok               |

## FET-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 66.55%   | -80.84%            | -51.84% |     0.7  |       86 | 50.57%     | ok               |
|          15 | 14.75%   | -80.84%            | -54.49% |     0.42 |       88 | 53.83%     | ok               |
|          25 | -1.37%   | -80.84%            | -52.50% |     0.28 |       91 | 43.68%     | ok               |
|          30 | -13.29%  | -80.84%            | -48.39% |     0.16 |       77 | 39.46%     | ok               |
|          35 | -36.13%  | -80.84%            | -55.22% |    -0.18 |       65 | 32.95%     | ok               |

## FIL-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -4.52%   | -82.27%            | -43.79% |     0.12 |       48 | 23.18%     | ok               |
|          50 | -17.17%  | -82.27%            | -42.59% |    -0.12 |       38 | 13.22%     | ok               |
|          30 | -26.60%  | -82.27%            | -46.68% |    -0.16 |       70 | 32.76%     | ok               |
|          35 | -26.06%  | -82.27%            | -46.24% |    -0.18 |       56 | 27.20%     | ok               |
|          45 | -24.84%  | -82.27%            | -41.50% |    -0.22 |       46 | 17.82%     | ok               |

## FXI Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -10.98%  | 61.74%             | -23.27% |    -0.23 |       36 | 19.30%     | ok               |
|          30 | -13.95%  | 61.74%             | -24.33% |    -0.29 |       48 | 26.79%     | ok               |
|          25 | -15.41%  | 61.74%             | -22.99% |    -0.33 |       50 | 27.79%     | ok               |
|          15 | -16.80%  | 61.74%             | -21.68% |    -0.34 |       54 | 31.28%     | ok               |
|          45 | -14.99%  | 61.74%             | -26.73% |    -0.35 |       42 | 21.46%     | ok               |

## GDX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 26.05%   | 201.85%            | -31.87% |     0.53 |       60 | 43.59%     | ok               |
|          20 | 14.61%   | 201.85%            | -35.59% |     0.35 |       72 | 53.24%     | ok               |
|          35 | 10.23%   | 201.85%            | -32.37% |     0.29 |       66 | 46.09%     | ok               |
|          30 | 5.77%    | 201.85%            | -34.99% |     0.22 |       60 | 49.08%     | ok               |
|          45 | 4.99%    | 201.85%            | -32.07% |     0.21 |       62 | 40.43%     | ok               |

## GDXJ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -4.27%   | 228.00%            | -45.05% |     0.1  |       66 | 53.08%     | ok               |
|          50 | -8.38%   | 228.00%            | -35.02% |    -0.02 |       58 | 37.27%     | ok               |
|          30 | -21.59%  | 228.00%            | -44.93% |    -0.21 |       68 | 46.59%     | ok               |
|          25 | -23.64%  | 228.00%            | -47.26% |    -0.22 |       71 | 49.75%     | ok               |
|          40 | -23.69%  | 228.00%            | -44.27% |    -0.28 |       64 | 42.26%     | ok               |

## GE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 18.92%   | 209.13%            | -22.29% |     0.45 |       66 | 38.10%     | ok               |
|          20 | 11.65%   | 209.13%            | -26.63% |     0.31 |       69 | 55.07%     | ok               |
|          45 | 10.95%   | 209.13%            | -25.68% |     0.31 |       76 | 41.10%     | ok               |
|          15 | 6.89%    | 209.13%            | -28.62% |     0.24 |       68 | 57.40%     | ok               |
|          35 | 6.64%    | 209.13%            | -27.11% |     0.23 |       80 | 46.59%     | ok               |

## GLD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | 20.29%   | 119.20%            | -14.61% |     0.56 |       48 | 44.59%     | ok               |
|          20 | 19.49%   | 119.20%            | -14.61% |     0.54 |       50 | 45.76%     | ok               |
|          30 | 18.75%   | 119.20%            | -16.63% |     0.53 |       50 | 43.59%     | ok               |
|          35 | 12.95%   | 119.20%            | -17.29% |     0.4  |       52 | 42.93%     | ok               |
|          15 | 13.06%   | 119.20%            | -16.82% |     0.39 |       52 | 50.42%     | ok               |

## GOOGL Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | 83.89%   | 156.72%            | -19.76% |     1.2  |       59 | 57.40%     | ok               |
|          30 | 75.11%   | 156.72%            | -20.41% |     1.12 |       65 | 55.24%     | ok               |
|          15 | 75.42%   | 156.72%            | -13.59% |     1.07 |       69 | 64.89%     | ok               |
|          20 | 71.80%   | 156.72%            | -20.57% |     1.07 |       68 | 59.57%     | ok               |
|          35 | 59.69%   | 156.72%            | -22.85% |     1.01 |       71 | 50.08%     | ok               |

## GRT-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 30.77%   | -88.72%            | -30.82% |     0.55 |       44 | 21.84%     | ok               |
|          45 | 2.78%    | -88.72%            | -49.33% |     0.22 |       50 | 26.05%     | ok               |
|          35 | -2.99%   | -88.72%            | -50.43% |     0.17 |       62 | 34.87%     | ok               |
|          40 | -1.60%   | -88.72%            | -48.92% |     0.17 |       52 | 29.31%     | ok               |
|          15 | -9.72%   | -88.72%            | -49.67% |     0.16 |       79 | 60.15%     | ok               |

## GS Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 27.19%   | 177.42%            | -20.56% |     0.58 |       74 | 59.57%     | ok               |
|          20 | 9.84%    | 177.42%            | -23.19% |     0.29 |       74 | 55.57%     | ok               |
|          25 | 6.36%    | 177.42%            | -23.32% |     0.23 |       74 | 53.08%     | ok               |
|          40 | 1.57%    | 177.42%            | -17.88% |     0.12 |       72 | 43.93%     | ok               |
|          30 | 0.17%    | 177.42%            | -22.13% |     0.1  |       76 | 50.58%     | ok               |

## HD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -1.60%   | -10.01%            | -17.69% |     0.04 |       69 | 45.26%     | ok               |
|          25 | -2.37%   | -10.01%            | -18.51% |     0.02 |       68 | 47.25%     | ok               |
|          35 | -10.76%  | -10.01%            | -22.98% |    -0.24 |       76 | 41.60%     | ok               |
|          40 | -10.16%  | -10.01%            | -20.58% |    -0.26 |       80 | 35.27%     | ok               |
|          20 | -15.23%  | -10.01%            | -23.94% |    -0.33 |       87 | 50.58%     | ok               |

## HON Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -12.40%  | 23.78%             | -23.12% |    -0.37 |       74 | 31.78%     | ok               |
|          45 | -15.10%  | 23.78%             | -22.74% |    -0.43 |       80 | 37.27%     | ok               |
|          40 | -16.04%  | 23.78%             | -23.13% |    -0.44 |       80 | 41.26%     | ok               |
|          35 | -17.65%  | 23.78%             | -26.26% |    -0.48 |       95 | 47.59%     | ok               |
|          30 | -19.92%  | 23.78%             | -28.64% |    -0.53 |       95 | 51.91%     | ok               |

## HYG Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -7.99%   | 3.46%              | -8.52%  |    -0.96 |       70 | 29.78%     | ok               |
|          15 | -9.74%   | 3.46%              | -10.32% |    -1.05 |       90 | 41.76%     | ok               |
|          20 | -9.62%   | 3.46%              | -10.26% |    -1.07 |       86 | 39.43%     | ok               |
|          45 | -8.67%   | 3.46%              | -9.19%  |    -1.08 |       66 | 26.62%     | ok               |
|          25 | -9.84%   | 3.46%              | -10.36% |    -1.1  |       85 | 37.44%     | ok               |

## IBIT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 52.15%   | 0.11%              | -12.64% |     1.12 |       18 | 21.25%     | ok               |
|          15 | 64.79%   | 0.11%              | -19.20% |     1.11 |       36 | 37.25%     | ok               |
|          45 | 43.69%   | 0.11%              | -17.12% |     0.95 |       20 | 22.00%     | ok               |
|          40 | 42.27%   | 0.11%              | -17.12% |     0.93 |       22 | 23.50%     | ok               |
|          30 | 35.78%   | 0.11%              | -18.95% |     0.79 |       30 | 29.25%     | ok               |

## IBM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 59.50%   | 105.67%            | -25.31% |     1.06 |       72 | 50.75%     | ok               |
|          15 | 66.49%   | 105.67%            | -28.20% |     1.03 |       87 | 62.73%     | ok               |
|          35 | 52.56%   | 105.67%            | -25.15% |     0.99 |       68 | 46.26%     | ok               |
|          45 | 46.42%   | 105.67%            | -18.73% |     0.95 |       54 | 37.10%     | ok               |
|          50 | 41.20%   | 105.67%            | -21.46% |     0.88 |       52 | 34.11%     | ok               |

## ICP-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 42.46%   | -69.67%            | -36.91% |     0.61 |       64 | 31.23%     | ok               |
|          40 | 34.93%   | -69.67%            | -29.38% |     0.55 |       58 | 26.82%     | ok               |
|          30 | 20.76%   | -69.67%            | -50.29% |     0.43 |       81 | 37.16%     | ok               |
|          50 | 17.76%   | -69.67%            | -32.35% |     0.39 |       40 | 17.05%     | ok               |
|          45 | 3.04%    | -69.67%            | -38.80% |     0.23 |       58 | 21.07%     | ok               |

## IEF Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -8.70%   | -1.43%             | -9.79%  |    -1.04 |       76 | 42.43%     | ok               |
|          15 | -9.24%   | -1.43%             | -10.52% |    -1.09 |       75 | 43.93%     | ok               |
|          40 | -8.39%   | -1.43%             | -9.67%  |    -1.31 |       60 | 24.79%     | ok               |
|          45 | -8.07%   | -1.43%             | -9.73%  |    -1.33 |       50 | 22.80%     | ok               |
|          25 | -11.04%  | -1.43%             | -11.56% |    -1.39 |       78 | 39.77%     | ok               |

## IEMG Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | -0.32%   | 75.03%             | -22.13% |     0.05 |       63 | 42.60%     | ok               |
|          50 | -2.14%   | 75.03%             | -13.91% |    -0.03 |       54 | 34.11%     | ok               |
|          40 | -2.44%   | 75.03%             | -18.43% |    -0.03 |       60 | 39.93%     | ok               |
|          45 | -2.35%   | 75.03%             | -14.92% |    -0.03 |       50 | 36.77%     | ok               |
|          25 | -4.72%   | 75.03%             | -25.58% |    -0.09 |       59 | 45.42%     | ok               |

## INJ-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -6.46%   | -67.93%            | -56.91% |     0.1  |       48 | 22.99%     | ok               |
|          35 | -23.61%  | -67.93%            | -65.28% |    -0.07 |       62 | 32.76%     | ok               |
|          50 | -16.63%  | -67.93%            | -52.76% |    -0.07 |       52 | 19.92%     | ok               |
|          40 | -31.28%  | -67.93%            | -64.83% |    -0.23 |       52 | 29.12%     | ok               |
|          20 | -46.89%  | -67.93%            | -79.76% |    -0.3  |       81 | 47.89%     | ok               |

## INTC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 72.60%   | 124.62%            | -49.32% |     0.73 |       62 | 34.78%     | ok               |
|          15 | 76.83%   | 124.62%            | -53.65% |     0.71 |       84 | 61.90%     | ok               |
|          25 | 73.32%   | 124.62%            | -56.41% |     0.71 |       75 | 52.08%     | ok               |
|          40 | 68.21%   | 124.62%            | -55.86% |     0.69 |       68 | 39.10%     | ok               |
|          20 | 70.55%   | 124.62%            | -52.47% |     0.69 |       82 | 57.07%     | ok               |

## INTU Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -2.92%   | -46.77%            | -43.31% |     0.06 |       69 | 28.45%     | ok               |
|          45 | -6.24%   | -46.77%            | -45.13% |     0    |       67 | 32.61%     | ok               |
|          15 | -11.92%  | -46.77%            | -47.30% |    -0.07 |       81 | 51.08%     | ok               |
|          25 | -11.92%  | -46.77%            | -42.24% |    -0.08 |       66 | 45.59%     | ok               |
|          40 | -11.09%  | -46.77%            | -48.32% |    -0.09 |       73 | 35.77%     | ok               |

## ITA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 6.07%    | 87.97%             | -21.48% |     0.26 |       72 | 35.77%     | ok               |
|          30 | 1.79%    | 87.97%             | -23.75% |     0.12 |       70 | 45.76%     | ok               |
|          15 | 0.01%    | 87.97%             | -26.46% |     0.08 |       89 | 58.40%     | ok               |
|          35 | -0.83%   | 87.97%             | -23.16% |     0.04 |       74 | 43.93%     | ok               |
|          40 | -1.97%   | 87.97%             | -20.58% |     0    |       76 | 40.43%     | ok               |

## IWM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 9.94%    | 49.59%             | -12.83% |     0.4  |       50 | 36.77%     | ok               |
|          25 | 8.91%    | 49.59%             | -14.80% |     0.36 |       52 | 38.44%     | ok               |
|          35 | 7.46%    | 49.59%             | -14.41% |     0.33 |       50 | 34.44%     | ok               |
|          40 | 6.82%    | 49.59%             | -14.38% |     0.32 |       44 | 31.95%     | ok               |
|          20 | 4.62%    | 49.59%             | -15.32% |     0.22 |       62 | 39.43%     | ok               |

## JNJ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 15.31%   | 37.90%             | -11.39% |     0.68 |       62 | 37.94%     | ok               |
|          15 | 10.11%   | 37.90%             | -18.02% |     0.39 |       72 | 58.07%     | ok               |
|          20 | 7.38%    | 37.90%             | -17.61% |     0.31 |       76 | 54.58%     | ok               |
|          45 | 5.72%    | 37.90%             | -15.23% |     0.28 |       64 | 42.93%     | ok               |
|          40 | 4.22%    | 37.90%             | -14.77% |     0.22 |       70 | 47.25%     | ok               |

## JPM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 11.70%   | 76.35%             | -15.40% |     0.44 |       56 | 39.93%     | ok               |
|          45 | 2.06%    | 76.35%             | -21.44% |     0.13 |       56 | 43.09%     | ok               |
|          40 | -11.40%  | 76.35%             | -28.02% |    -0.28 |       68 | 45.59%     | ok               |
|          20 | -16.65%  | 76.35%             | -33.20% |    -0.31 |       84 | 57.07%     | ok               |
|          35 | -16.34%  | 76.35%             | -26.98% |    -0.41 |       74 | 49.25%     | ok               |

## KO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 23.27%   | 30.68%             | -8.07%  |     0.88 |       49 | 37.27%     | ok               |
|          35 | 19.49%   | 30.68%             | -8.07%  |     0.77 |       52 | 35.94%     | ok               |
|          50 | 16.35%   | 30.68%             | -11.40% |     0.74 |       34 | 26.62%     | ok               |
|          40 | 17.09%   | 30.68%             | -9.28%  |     0.73 |       54 | 32.95%     | ok               |
|          25 | 18.21%   | 30.68%             | -9.34%  |     0.71 |       55 | 39.93%     | ok               |

## LDO-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -7.03%   | -83.00%            | -47.58% |     0.27 |       86 | 51.34%     | ok               |
|          20 | -5.87%   | -83.00%            | -44.97% |     0.26 |       91 | 46.55%     | ok               |
|          30 | -17.45%  | -83.00%            | -60.93% |     0.11 |       80 | 36.97%     | ok               |
|          25 | -29.45%  | -83.00%            | -56.60% |     0.01 |       87 | 42.53%     | ok               |
|          50 | -13.37%  | -83.00%            | -48.77% |    -0.04 |       46 | 16.28%     | ok               |

## LIN Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 3.30%    | 21.94%             | -23.70% |     0.17 |       68 | 50.25%     | ok               |
|          25 | 1.46%    | 21.94%             | -22.01% |     0.11 |       68 | 41.93%     | ok               |
|          20 | -0.71%   | 21.94%             | -23.00% |     0.04 |       67 | 45.09%     | ok               |
|          35 | -2.45%   | 21.94%             | -21.18% |    -0.04 |       68 | 32.78%     | ok               |
|          30 | -3.07%   | 21.94%             | -21.53% |    -0.05 |       72 | 39.27%     | ok               |

## LINK-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -21.89%  | -59.86%            | -55.61% |    -0.01 |       72 | 40.23%     | ok               |
|          50 | -22.45%  | -59.86%            | -42.26% |    -0.11 |       38 | 20.31%     | ok               |
|          45 | -27.17%  | -59.86%            | -43.89% |    -0.16 |       50 | 24.71%     | ok               |
|          35 | -34.91%  | -59.86%            | -53.72% |    -0.21 |       62 | 34.87%     | ok               |
|          25 | -45.95%  | -59.86%            | -56.54% |    -0.31 |       68 | 45.79%     | ok               |

## LLY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 23.37%   | 70.13%             | -38.23% |     0.51 |       42 | 39.27%     | ok               |
|          45 | 11.54%   | 70.13%             | -42.66% |     0.32 |       50 | 42.43%     | ok               |
|          15 | 5.19%    | 70.13%             | -48.12% |     0.22 |       63 | 61.90%     | ok               |
|          40 | -5.15%   | 70.13%             | -46.23% |     0.03 |       62 | 44.93%     | ok               |
|          20 | -11.75%  | 70.13%             | -51.34% |    -0.06 |       72 | 56.91%     | ok               |

## LRCX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 9.67%    | 344.68%            | -60.45% |     0.29 |       81 | 55.74%     | ok               |
|          50 | 0.69%    | 344.68%            | -50.39% |     0.15 |       76 | 36.61%     | ok               |
|          40 | -8.88%   | 344.68%            | -56.86% |     0.03 |       72 | 42.43%     | ok               |
|          35 | -11.51%  | 344.68%            | -61.76% |    -0    |       82 | 45.09%     | ok               |
|          20 | -14.08%  | 344.68%            | -67.64% |    -0.02 |       89 | 51.08%     | ok               |

## LTC-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -27.02%  | -51.72%            | -47.47% |    -0.25 |       58 | 31.03%     | ok               |
|          35 | -31.76%  | -51.72%            | -56.94% |    -0.29 |       68 | 41.57%     | ok               |
|          50 | -32.64%  | -51.72%            | -48.91% |    -0.4  |       52 | 24.52%     | ok               |
|          30 | -40.78%  | -51.72%            | -55.04% |    -0.42 |       67 | 46.93%     | ok               |
|          25 | -43.27%  | -51.72%            | -55.83% |    -0.45 |       75 | 49.43%     | ok               |

## MCD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 2.92%    | -4.99%             | -9.22%  |     0.19 |       44 | 20.47%     | ok               |
|          30 | -2.11%   | -4.99%             | -19.14% |    -0.03 |       75 | 38.94%     | ok               |
|          25 | -3.51%   | -4.99%             | -20.80% |    -0.08 |       77 | 41.43%     | ok               |
|          40 | -6.24%   | -4.99%             | -16.86% |    -0.24 |       73 | 29.78%     | ok               |
|          35 | -7.56%   | -4.99%             | -15.80% |    -0.28 |       69 | 35.61%     | ok               |

## META Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 19.56%   | 67.20%             | -31.03% |     0.42 |       68 | 41.76%     | ok               |
|          40 | 6.42%    | 67.20%             | -35.11% |     0.23 |       68 | 44.76%     | ok               |
|          50 | 1.31%    | 67.20%             | -34.00% |     0.14 |       72 | 37.94%     | ok               |
|          25 | 0.22%    | 67.20%             | -37.13% |     0.14 |       67 | 55.24%     | ok               |
|          35 | -1.57%   | 67.20%             | -32.24% |     0.1  |       77 | 49.42%     | ok               |

## MPC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 14.51%   | 70.48%             | -23.96% |     0.37 |       52 | 38.60%     | ok               |
|          45 | 7.25%    | 70.48%             | -25.09% |     0.24 |       58 | 42.26%     | ok               |
|          40 | 5.62%    | 70.48%             | -25.70% |     0.22 |       60 | 44.59%     | ok               |
|          35 | 2.36%    | 70.48%             | -35.90% |     0.16 |       68 | 47.09%     | ok               |
|          30 | -13.74%  | 70.48%             | -44.76% |    -0.14 |       71 | 49.92%     | ok               |

## MRK Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -15.05%  | -2.35%             | -29.91% |    -0.24 |       85 | 57.74%     | ok               |
|          25 | -14.64%  | -2.35%             | -31.07% |    -0.26 |       70 | 49.75%     | ok               |
|          20 | -18.83%  | -2.35%             | -29.38% |    -0.36 |       75 | 53.08%     | ok               |
|          30 | -20.82%  | -2.35%             | -32.14% |    -0.44 |       67 | 47.09%     | ok               |
|          35 | -20.57%  | -2.35%             | -30.50% |    -0.45 |       67 | 43.43%     | ok               |

## MS Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -3.98%   | 133.52%            | -19.61% |    -0.03 |       70 | 38.60%     | ok               |
|          35 | -11.34%  | 133.52%            | -21.83% |    -0.22 |       78 | 43.43%     | ok               |
|          15 | -15.16%  | 133.52%            | -25.72% |    -0.26 |       84 | 56.57%     | ok               |
|          50 | -10.06%  | 133.52%            | -15.66% |    -0.3  |       58 | 30.45%     | ok               |
|          20 | -15.61%  | 133.52%            | -25.68% |    -0.3  |       86 | 52.58%     | ok               |

## MSFT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -13.48%  | 17.44%             | -25.28% |    -0.36 |       60 | 35.11%     | ok               |
|          50 | -17.08%  | 17.44%             | -28.69% |    -0.5  |       58 | 30.78%     | ok               |
|          35 | -25.89%  | 17.44%             | -30.57% |    -0.67 |       69 | 43.43%     | ok               |
|          25 | -29.45%  | 17.44%             | -33.90% |    -0.74 |       82 | 50.75%     | ok               |
|          40 | -26.77%  | 17.44%             | -32.42% |    -0.74 |       65 | 38.44%     | ok               |

## MU Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 389.06%  | 1176.97%           | -61.96% |     1.55 |       50 | 66.89%     | ok               |
|          25 | 296.51%  | 1176.97%           | -67.90% |     1.45 |       53 | 60.40%     | ok               |
|          40 | 256.53%  | 1176.97%           | -64.07% |     1.38 |       60 | 53.91%     | ok               |
|          20 | 263.02%  | 1176.97%           | -67.25% |     1.35 |       59 | 62.56%     | ok               |
|          30 | 237.76%  | 1176.97%           | -68.76% |     1.32 |       55 | 58.57%     | ok               |

## NEAR-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 87.99%   | -46.78%            | -45.84% |     0.9  |       48 | 24.90%     | ok               |
|          50 | 58.08%   | -46.78%            | -51.20% |     0.73 |       44 | 19.92%     | ok               |
|          40 | 49.51%   | -46.78%            | -54.53% |     0.65 |       50 | 29.12%     | ok               |
|          35 | 22.26%   | -46.78%            | -58.86% |     0.44 |       74 | 34.29%     | ok               |
|          15 | -4.87%   | -46.78%            | -54.94% |     0.26 |       94 | 58.24%     | ok               |

## NEM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 39.24%   | 183.09%            | -25.79% |     0.58 |       62 | 64.06%     | ok               |
|          20 | 23.08%   | 183.09%            | -30.47% |     0.43 |       72 | 59.23%     | ok               |
|          25 | -1.57%   | 183.09%            | -30.80% |     0.14 |       68 | 57.24%     | ok               |
|          50 | -8.96%   | 183.09%            | -33.36% |     0.01 |       56 | 41.93%     | ok               |
|          30 | -18.69%  | 183.09%            | -38.49% |    -0.11 |       72 | 55.74%     | ok               |

## NFLX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 44.79%   | 72.85%             | -11.94% |     0.99 |       46 | 46.92%     | ok               |
|          50 | 35.49%   | 72.85%             | -16.28% |     0.87 |       48 | 39.27%     | ok               |
|          35 | 37.35%   | 72.85%             | -18.30% |     0.82 |       60 | 50.42%     | ok               |
|          45 | 32.06%   | 72.85%             | -15.48% |     0.78 |       52 | 43.09%     | ok               |
|          25 | 30.06%   | 72.85%             | -21.09% |     0.66 |       60 | 57.40%     | ok               |

## NKE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | -26.63%  | -57.44%            | -42.13% |    -0.37 |       77 | 38.94%     | ok               |
|          20 | -35.79%  | -57.44%            | -50.44% |    -0.46 |       97 | 54.74%     | ok               |
|          25 | -36.75%  | -57.44%            | -51.20% |    -0.49 |       95 | 50.75%     | ok               |
|          40 | -27.10%  | -57.44%            | -31.84% |    -0.52 |       69 | 30.95%     | ok               |
|          30 | -37.58%  | -57.44%            | -55.35% |    -0.52 |       93 | 45.42%     | ok               |

## NOW Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 47.22%   | -8.65%             | -26.36% |     0.67 |       77 | 51.58%     | ok               |
|          15 | 37.44%   | -8.65%             | -27.25% |     0.57 |       86 | 54.74%     | ok               |
|          25 | 35.91%   | -8.65%             | -26.83% |     0.57 |       72 | 49.08%     | ok               |
|          30 | 26.82%   | -8.65%             | -31.32% |     0.48 |       78 | 46.09%     | ok               |
|          35 | 18.38%   | -8.65%             | -29.30% |     0.39 |       77 | 41.10%     | ok               |

## NVDA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -4.81%   | 140.45%            | -33.22% |     0.11 |       68 | 52.94%     | ok               |
|          30 | -6.59%   | 140.45%            | -35.26% |     0.07 |       70 | 50.62%     | ok               |
|          20 | -11.12%  | 140.45%            | -40.59% |     0.03 |       71 | 57.40%     | ok               |
|          35 | -17.54%  | 140.45%            | -41.25% |    -0.12 |       82 | 47.77%     | ok               |
|          50 | -17.47%  | 140.45%            | -40.84% |    -0.15 |       60 | 34.94%     | ok               |

## OP-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 51.92%   | -93.53%            | -53.61% |     0.68 |       50 | 25.67%     | ok               |
|          45 | 40.64%   | -93.53%            | -45.76% |     0.61 |       38 | 17.24%     | ok               |
|          50 | 34.11%   | -93.53%            | -36.11% |     0.58 |       34 | 12.45%     | ok               |
|          35 | 27.04%   | -93.53%            | -58.13% |     0.48 |       58 | 28.93%     | ok               |
|          30 | -8.19%   | -93.53%            | -70.11% |     0.16 |       76 | 35.44%     | ok               |

## ORCL Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 213.37%  | 136.01%            | -21.44% |     1.33 |       73 | 64.23%     | ok               |
|          25 | 139.95%  | 136.01%            | -24.79% |     1.08 |       70 | 56.41%     | ok               |
|          20 | 137.29%  | 136.01%            | -22.81% |     1.06 |       76 | 59.73%     | ok               |
|          35 | 90.27%   | 136.01%            | -31.95% |     0.86 |       62 | 47.92%     | ok               |
|          30 | 89.79%   | 136.01%            | -29.47% |     0.85 |       70 | 52.25%     | ok               |

## OXY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 2.99%    | 2.84%              | -29.57% |     0.16 |       36 | 28.62%     | ok               |
|          35 | -0.19%   | 2.84%              | -30.62% |     0.11 |       70 | 39.10%     | ok               |
|          40 | -1.69%   | 2.84%              | -31.66% |     0.07 |       54 | 34.78%     | ok               |
|          30 | -4.86%   | 2.84%              | -34.69% |     0.03 |       73 | 44.76%     | ok               |
|          45 | -6.26%   | 2.84%              | -34.84% |    -0.03 |       42 | 30.45%     | ok               |

## PEP Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 8.79%    | -15.06%            | -11.62% |     0.41 |       44 | 27.95%     | ok               |
|          45 | 1.85%    | -15.06%            | -14.22% |     0.13 |       66 | 32.61%     | ok               |
|          40 | -1.71%   | -15.06%            | -18.04% |    -0.01 |       76 | 37.94%     | ok               |
|          35 | -4.04%   | -15.06%            | -21.42% |    -0.06 |       87 | 42.60%     | ok               |
|          30 | -9.45%   | -15.06%            | -21.35% |    -0.22 |       85 | 48.92%     | ok               |

## PEPE-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -4.17%   | -82.44%            | -57.66% |     0.24 |       79 | 42.53%     | ok               |
|          35 | -10.60%  | -82.44%            | -51.35% |     0.14 |       64 | 37.36%     | ok               |
|          25 | -27.75%  | -82.44%            | -62.34% |     0    |       89 | 48.08%     | ok               |
|          15 | -47.95%  | -82.44%            | -72.26% |    -0.13 |       86 | 58.05%     | ok               |
|          50 | -25.52%  | -82.44%            | -39.66% |    -0.14 |       52 | 22.03%     | ok               |

## PFE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -23.76%  | -13.10%            | -27.74% |    -0.83 |       52 | 21.46%     | ok               |
|          35 | -31.86%  | -13.10%            | -36.39% |    -1    |       82 | 33.61%     | ok               |
|          50 | -26.08%  | -13.10%            | -28.97% |    -1.01 |       44 | 17.64%     | ok               |
|          40 | -30.22%  | -13.10%            | -33.87% |    -1.03 |       76 | 26.29%     | ok               |
|          30 | -38.05%  | -13.10%            | -42.29% |    -1.18 |       77 | 37.27%     | ok               |

## PG Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -3.81%   | -5.68%             | -19.77% |    -0.12 |       54 | 34.11%     | ok               |
|          35 | -4.99%   | -5.68%             | -18.66% |    -0.16 |       60 | 37.77%     | ok               |
|          30 | -9.90%   | -5.68%             | -20.33% |    -0.36 |       61 | 40.43%     | ok               |
|          25 | -10.99%  | -5.68%             | -20.01% |    -0.4  |       71 | 41.60%     | ok               |
|          45 | -14.31%  | -5.68%             | -20.33% |    -0.64 |       54 | 31.28%     | ok               |

## PM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 0.32%    | 81.67%             | -32.95% |     0.1  |       84 | 52.91%     | ok               |
|          20 | -0.94%   | 81.67%             | -32.63% |     0.08 |       87 | 61.73%     | ok               |
|          30 | -1.20%   | 81.67%             | -34.41% |     0.07 |       81 | 56.74%     | ok               |
|          50 | -4.69%   | 81.67%             | -35.70% |    -0.03 |       76 | 43.26%     | ok               |
|          40 | -6.59%   | 81.67%             | -37.94% |    -0.07 |       80 | 49.92%     | ok               |

## POL-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 44.01%   | -80.50%            | -46.45% |     0.62 |       80 | 47.32%     | ok               |
|          25 | 23.25%   | -80.50%            | -46.72% |     0.45 |       72 | 56.51%     | ok               |
|          20 | 21.78%   | -80.50%            | -52.88% |     0.44 |       80 | 62.07%     | ok               |
|          50 | 12.83%   | -80.50%            | -22.46% |     0.34 |       54 | 20.50%     | ok               |
|          15 | -4.94%   | -80.50%            | -58.42% |     0.21 |       79 | 68.39%     | ok               |

## QCOM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | 13.08%   | 72.16%             | -55.66% |     0.32 |       75 | 50.75%     | ok               |
|          20 | 10.17%   | 72.16%             | -57.05% |     0.29 |       72 | 53.41%     | ok               |
|          35 | 5.82%    | 72.16%             | -51.84% |     0.23 |       87 | 45.92%     | ok               |
|          30 | -5.73%   | 72.16%             | -57.69% |     0.09 |       81 | 48.59%     | ok               |
|          15 | -8.14%   | 72.16%             | -60.40% |     0.07 |       76 | 56.57%     | ok               |

## QQQ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | 30.59%   | 83.90%             | -12.88% |     0.79 |       55 | 49.25%     | ok               |
|          20 | 30.04%   | 83.90%             | -12.98% |     0.75 |       63 | 51.75%     | ok               |
|          30 | 25.24%   | 83.90%             | -12.88% |     0.7  |       60 | 46.26%     | ok               |
|          15 | 27.32%   | 83.90%             | -14.17% |     0.68 |       63 | 54.24%     | ok               |
|          35 | 12.43%   | 83.90%             | -19.00% |     0.41 |       66 | 42.60%     | ok               |

## RENDER-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 71.10%   | -48.94%            | -43.43% |     0.78 |       82 | 55.56%     | ok               |
|          15 | 51.23%   | -48.94%            | -44.59% |     0.67 |       82 | 58.76%     | ok               |
|          25 | 37.19%   | -48.94%            | -40.60% |     0.59 |       86 | 51.50%     | ok               |
|          30 | -5.83%   | -48.94%            | -45.00% |     0.23 |       94 | 44.87%     | ok               |
|          40 | -16.41%  | -48.94%            | -38.60% |     0.04 |       68 | 29.91%     | ok               |

## RTX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 25.78%   | 103.10%            | -18.66% |     0.65 |       76 | 56.91%     | ok               |
|          25 | 21.09%   | 103.10%            | -18.59% |     0.56 |       64 | 53.58%     | ok               |
|          50 | 16.04%   | 103.10%            | -18.42% |     0.53 |       60 | 42.10%     | ok               |
|          30 | 18.66%   | 103.10%            | -16.99% |     0.51 |       58 | 52.25%     | ok               |
|          35 | 16.09%   | 103.10%            | -18.00% |     0.5  |       54 | 50.25%     | ok               |

## SBUX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -14.56%  | 2.60%              | -23.55% |    -0.23 |       62 | 42.60%     | ok               |
|          45 | -17.91%  | 2.60%              | -27.26% |    -0.41 |       72 | 29.62%     | ok               |
|          40 | -19.25%  | 2.60%              | -27.13% |    -0.42 |       68 | 33.11%     | ok               |
|          30 | -23.46%  | 2.60%              | -31.15% |    -0.47 |       65 | 40.43%     | ok               |
|          20 | -26.33%  | 2.60%              | -34.48% |    -0.49 |       67 | 44.59%     | ok               |

## SCHW Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 1.55%    | 31.25%             | -15.92% |     0.12 |       54 | 33.28%     | ok               |
|          50 | -2.36%   | 31.25%             | -12.59% |    -0.02 |       48 | 30.78%     | ok               |
|          25 | -10.23%  | 31.25%             | -28.76% |    -0.16 |       61 | 47.75%     | ok               |
|          40 | -8.98%   | 31.25%             | -21.81% |    -0.18 |       62 | 36.27%     | ok               |
|          20 | -11.91%  | 31.25%             | -29.24% |    -0.2  |       69 | 50.42%     | ok               |

## SHIB-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -17.52%  | -75.40%            | -49.21% |     0.05 |       80 | 67.05%     | ok               |
|          25 | -24.40%  | -75.40%            | -43.85% |    -0.06 |       79 | 57.85%     | ok               |
|          20 | -29.22%  | -75.40%            | -48.69% |    -0.11 |       83 | 62.84%     | ok               |
|          30 | -37.46%  | -75.40%            | -48.95% |    -0.3  |       78 | 50.77%     | ok               |
|          40 | -34.04%  | -75.40%            | -53.38% |    -0.31 |       56 | 36.97%     | ok               |

## SHY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd    |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:-------|---------:|---------:|:-----------|:-----------------|
|          35 | -2.18%   | 0.04%              | -3.27% |    -0.74 |       52 | 35.11%     | ok               |
|          30 | -2.22%   | 0.04%              | -2.85% |    -0.75 |       52 | 37.10%     | ok               |
|          40 | -2.29%   | 0.04%              | -3.33% |    -0.79 |       52 | 33.28%     | ok               |
|          45 | -2.27%   | 0.04%              | -3.23% |    -0.8  |       50 | 30.12%     | ok               |
|          50 | -2.44%   | 0.04%              | -3.40% |    -0.9  |       46 | 27.29%     | ok               |

## SKY-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -29.93%  | 16.55%             | -43.98% |    -0.42 |       66 | 39.42%     | ok               |
|          25 | -33.53%  | 16.55%             | -48.09% |    -0.48 |       61 | 43.31%     | ok               |
|          15 | -38.89%  | 16.55%             | -56.39% |    -0.53 |       56 | 49.64%     | ok               |
|          20 | -43.65%  | 16.55%             | -58.40% |    -0.67 |       58 | 47.20%     | ok               |
|          35 | -40.38%  | 16.55%             | -49.68% |    -0.79 |       58 | 33.09%     | ok               |

## SLB Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 8.33%    | 16.47%             | -21.46% |     0.27 |       54 | 34.61%     | ok               |
|          40 | 8.08%    | 16.47%             | -25.33% |     0.26 |       50 | 37.77%     | ok               |
|          50 | -13.80%  | 16.47%             | -29.64% |    -0.26 |       58 | 30.78%     | ok               |
|          35 | -20.66%  | 16.47%             | -43.52% |    -0.34 |       78 | 45.42%     | ok               |
|          30 | -31.21%  | 16.47%             | -54.23% |    -0.56 |       77 | 51.91%     | ok               |

## SLV Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 67.27%   | 223.76%            | -29.75% |     0.86 |       60 | 36.27%     | ok               |
|          45 | 62.01%   | 223.76%            | -31.82% |     0.82 |       54 | 34.44%     | ok               |
|          50 | 57.25%   | 223.76%            | -34.10% |     0.78 |       52 | 33.61%     | ok               |
|          35 | 54.63%   | 223.76%            | -36.89% |     0.75 |       62 | 38.60%     | ok               |
|          30 | 36.93%   | 223.76%            | -42.66% |     0.58 |       58 | 40.60%     | ok               |

## SMH Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 122.65%  | 266.67%            | -30.17% |     1.36 |       49 | 54.74%     | ok               |
|          35 | 99.26%   | 266.67%            | -34.36% |     1.23 |       56 | 50.58%     | ok               |
|          25 | 99.12%   | 266.67%            | -32.94% |     1.22 |       48 | 53.58%     | ok               |
|          30 | 96.77%   | 266.67%            | -33.99% |     1.2  |       50 | 51.91%     | ok               |
|          45 | 78.31%   | 266.67%            | -32.75% |     1.12 |       56 | 44.26%     | ok               |

## SNX-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 34.28%   | -86.49%            | -28.28% |     0.54 |       68 | 31.42%     | ok               |
|          30 | 13.75%   | -86.49%            | -32.91% |     0.37 |       67 | 39.27%     | ok               |
|          20 | -4.34%   | -86.49%            | -43.20% |     0.23 |       74 | 50.38%     | ok               |
|          25 | -9.23%   | -86.49%            | -35.81% |     0.16 |       78 | 43.68%     | ok               |
|          40 | -14.15%  | -86.49%            | -33.53% |     0.01 |       58 | 25.29%     | ok               |

## SOL-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -27.74%  | -60.50%            | -60.05% |    -0.1  |       66 | 37.93%     | ok               |
|          25 | -33.96%  | -60.50%            | -53.21% |    -0.12 |       74 | 56.32%     | ok               |
|          35 | -37.38%  | -60.50%            | -61.96% |    -0.2  |       74 | 45.59%     | ok               |
|          15 | -42.14%  | -60.50%            | -59.14% |    -0.21 |       80 | 64.18%     | ok               |
|          20 | -43.45%  | -60.50%            | -56.90% |    -0.25 |       70 | 58.81%     | ok               |

## SOXX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 101.75%  | 224.30%            | -38.67% |     1.17 |       55 | 53.58%     | ok               |
|          25 | 97.89%   | 224.30%            | -39.85% |     1.15 |       53 | 53.24%     | ok               |
|          15 | 96.68%   | 224.30%            | -37.72% |     1.1  |       68 | 56.41%     | ok               |
|          35 | 88.75%   | 224.30%            | -38.63% |     1.1  |       65 | 48.25%     | ok               |
|          30 | 86.77%   | 224.30%            | -40.34% |     1.07 |       57 | 51.08%     | ok               |

## SPY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 21.78%   | 60.29%             | -14.25% |     0.73 |       58 | 54.08%     | ok               |
|          15 | 20.99%   | 60.29%             | -16.80% |     0.69 |       63 | 56.91%     | ok               |
|          25 | 14.76%   | 60.29%             | -15.22% |     0.53 |       58 | 53.41%     | ok               |
|          30 | 10.62%   | 60.29%             | -16.47% |     0.42 |       60 | 50.92%     | ok               |
|          35 | 7.23%    | 60.29%             | -16.72% |     0.31 |       60 | 48.42%     | ok               |

## SUSHI-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -32.29%  | -85.08%            | -40.12% |    -0.33 |       52 | 14.94%     | ok               |
|          45 | -61.52%  | -85.08%            | -64.69% |    -0.83 |       52 | 17.62%     | ok               |
|          40 | -63.97%  | -85.08%            | -68.78% |    -0.84 |       61 | 24.33%     | ok               |
|          35 | -69.36%  | -85.08%            | -74.72% |    -0.96 |       79 | 29.50%     | ok               |
|          15 | -80.55%  | -85.08%            | -81.26% |    -1.03 |       89 | 47.32%     | ok               |

## T Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 37.03%   | 45.37%             | -18.13% |     0.84 |       61 | 53.91%     | ok               |
|          25 | 30.40%   | 45.37%             | -17.66% |     0.73 |       64 | 51.41%     | ok               |
|          15 | 29.55%   | 45.37%             | -15.08% |     0.69 |       70 | 57.74%     | ok               |
|          35 | 18.73%   | 45.37%             | -14.49% |     0.53 |       64 | 45.92%     | ok               |
|          30 | 17.39%   | 45.37%             | -17.01% |     0.49 |       66 | 49.25%     | ok               |

## TGT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -12.98%  | -14.32%            | -42.86% |    -0.15 |       81 | 47.09%     | ok               |
|          45 | -9.84%   | -14.32%            | -29.07% |    -0.15 |       52 | 29.12%     | ok               |
|          15 | -15.82%  | -14.32%            | -40.77% |    -0.19 |       71 | 51.58%     | ok               |
|          25 | -13.84%  | -14.32%            | -43.36% |    -0.2  |       63 | 42.10%     | ok               |
|          30 | -13.22%  | -14.32%            | -40.57% |    -0.2  |       58 | 39.27%     | ok               |

## TIA-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 63.31%   | -92.36%            | -32.25% |     0.74 |       54 | 29.12%     | ok               |
|          40 | 56.01%   | -92.36%            | -32.87% |     0.7  |       56 | 25.10%     | ok               |
|          45 | 35.77%   | -92.36%            | -32.94% |     0.57 |       52 | 18.58%     | ok               |
|          50 | 23.57%   | -92.36%            | -38.67% |     0.49 |       34 | 11.30%     | ok               |
|          30 | -7.24%   | -92.36%            | -54.46% |     0.18 |       78 | 32.95%     | ok               |

## TLT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -14.18%  | -11.35%            | -16.11% |    -1.5  |       36 | 15.14%     | ok               |
|          40 | -18.28%  | -11.35%            | -20.35% |    -1.65 |       60 | 22.30%     | ok               |
|          30 | -22.73%  | -11.35%            | -24.69% |    -1.65 |       70 | 33.44%     | ok               |
|          45 | -17.99%  | -11.35%            | -19.60% |    -1.81 |       42 | 17.97%     | ok               |
|          35 | -22.23%  | -11.35%            | -24.20% |    -1.82 |       68 | 27.45%     | ok               |

## TMO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 43.47%   | -11.03%            | -10.55% |     0.99 |       36 | 30.12%     | ok               |
|          45 | 42.67%   | -11.03%            | -12.29% |     0.94 |       44 | 35.11%     | ok               |
|          40 | 40.50%   | -11.03%            | -12.07% |     0.89 |       51 | 39.93%     | ok               |
|          35 | 27.40%   | -11.03%            | -16.12% |     0.64 |       63 | 44.76%     | ok               |
|          30 | 20.00%   | -11.03%            | -16.83% |     0.49 |       57 | 49.92%     | ok               |

## TMUS Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 21.29%   | 15.70%             | -26.87% |     0.51 |       67 | 60.57%     | ok               |
|          30 | 19.83%   | 15.70%             | -24.50% |     0.5  |       68 | 48.92%     | ok               |
|          20 | 13.84%   | 15.70%             | -24.82% |     0.38 |       69 | 54.91%     | ok               |
|          25 | 12.71%   | 15.70%             | -25.91% |     0.36 |       73 | 51.25%     | ok               |
|          50 | 8.86%    | 15.70%             | -18.84% |     0.31 |       58 | 36.77%     | ok               |

## TRX-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -2.64%   | 29.48%             | -22.90% |     0.03 |       70 | 49.23%     | ok               |
|          35 | -3.97%   | 29.48%             | -21.77% |    -0.01 |       66 | 46.55%     | ok               |
|          25 | -4.39%   | 29.48%             | -26.84% |    -0.02 |       66 | 52.49%     | ok               |
|          40 | -3.78%   | 29.48%             | -22.27% |    -0.02 |       52 | 38.51%     | ok               |
|          50 | -6.77%   | 29.48%             | -21.14% |    -0.13 |       46 | 33.14%     | ok               |

## TSLA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 93.00%   | 80.35%             | -32.60% |     0.98 |       64 | 31.95%     | ok               |
|          40 | 83.28%   | 80.35%             | -45.90% |     0.85 |       61 | 36.44%     | ok               |
|          45 | 55.27%   | 80.35%             | -46.86% |     0.68 |       65 | 33.78%     | ok               |
|          35 | 33.01%   | 80.35%             | -54.51% |     0.5  |       74 | 39.60%     | ok               |
|          30 | 8.00%    | 80.35%             | -57.89% |     0.29 |       68 | 44.09%     | ok               |

## TXN Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 14.40%   | 82.72%             | -45.45% |     0.35 |       68 | 34.94%     | ok               |
|          20 | 8.98%    | 82.72%             | -38.98% |     0.27 |       64 | 60.73%     | ok               |
|          40 | 8.01%    | 82.72%             | -45.67% |     0.25 |       72 | 47.59%     | ok               |
|          15 | 7.00%    | 82.72%             | -39.48% |     0.25 |       67 | 64.23%     | ok               |
|          35 | 7.18%    | 82.72%             | -43.38% |     0.24 |       74 | 50.42%     | ok               |

## UNH Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 23.18%   | -29.80%            | -37.02% |     0.46 |       52 | 28.79%     | ok               |
|          30 | 14.41%   | -29.80%            | -32.80% |     0.34 |       78 | 52.25%     | ok               |
|          35 | 11.02%   | -29.80%            | -34.05% |     0.3  |       70 | 47.25%     | ok               |
|          15 | 9.39%    | -29.80%            | -36.80% |     0.28 |       77 | 67.05%     | ok               |
|          40 | 6.94%    | -29.80%            | -39.28% |     0.25 |       66 | 41.43%     | ok               |

## UNI-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -12.12%  | -78.25%            | -53.40% |     0.08 |       52 | 23.37%     | ok               |
|          50 | -14.98%  | -78.25%            | -50.59% |     0.02 |       46 | 20.11%     | ok               |
|          40 | -20.19%  | -78.25%            | -60.60% |    -0    |       54 | 28.54%     | ok               |
|          35 | -30.93%  | -78.25%            | -65.80% |    -0.11 |       72 | 33.14%     | ok               |
|          20 | -72.25%  | -78.25%            | -80.81% |    -0.74 |      101 | 50.38%     | ok               |

## UPS Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -33.65%  | -31.89%            | -42.25% |    -0.65 |       74 | 42.76%     | ok               |
|          35 | -32.54%  | -31.89%            | -40.47% |    -0.66 |       59 | 32.45%     | ok               |
|          20 | -34.76%  | -31.89%            | -45.77% |    -0.66 |       80 | 45.92%     | ok               |
|          30 | -35.02%  | -31.89%            | -40.62% |    -0.71 |       66 | 38.10%     | ok               |
|          40 | -33.89%  | -31.89%            | -42.12% |    -0.72 |       51 | 27.29%     | ok               |

## USO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 8.31%    | 103.69%            | -35.12% |     0.26 |       50 | 26.79%     | ok               |
|          30 | 2.80%    | 103.69%            | -43.35% |     0.17 |       68 | 34.44%     | ok               |
|          25 | 1.57%    | 103.69%            | -43.43% |     0.16 |       70 | 37.44%     | ok               |
|          20 | 0.27%    | 103.69%            | -44.16% |     0.14 |       74 | 39.43%     | ok               |
|          40 | -1.01%   | 103.69%            | -41.14% |     0.11 |       61 | 29.62%     | ok               |

## VEA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 4.31%    | 53.25%             | -17.18% |     0.21 |       60 | 50.08%     | ok               |
|          20 | 0.74%    | 53.25%             | -18.07% |     0.08 |       59 | 47.59%     | ok               |
|          25 | -2.41%   | 53.25%             | -19.11% |    -0.04 |       59 | 45.92%     | ok               |
|          30 | -2.87%   | 53.25%             | -19.49% |    -0.07 |       60 | 43.43%     | ok               |
|          35 | -4.16%   | 53.25%             | -18.54% |    -0.12 |       56 | 42.26%     | ok               |

## VIXY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -46.17%  | -60.34%            | -68.69% |    -0.39 |       44 | 10.32%     | ok               |
|          45 | -54.22%  | -60.34%            | -74.12% |    -0.51 |       56 | 15.81%     | ok               |
|          40 | -63.65%  | -60.34%            | -79.58% |    -0.65 |       70 | 19.80%     | ok               |
|          35 | -67.45%  | -60.34%            | -83.87% |    -0.68 |       86 | 24.96%     | ok               |
|          15 | -77.27%  | -60.34%            | -89.47% |    -0.8  |       99 | 42.26%     | ok               |

## VNQ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -8.60%   | 8.32%              | -19.07% |    -0.37 |       60 | 28.62%     | ok               |
|          50 | -9.03%   | 8.32%              | -17.13% |    -0.41 |       56 | 26.12%     | ok               |
|          25 | -14.09%  | 8.32%              | -22.16% |    -0.55 |       70 | 41.10%     | ok               |
|          40 | -14.13%  | 8.32%              | -24.84% |    -0.62 |       74 | 32.11%     | ok               |
|          20 | -18.82%  | 8.32%              | -23.61% |    -0.75 |       79 | 44.43%     | ok               |

## VTI Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 20.17%   | 58.62%             | -13.96% |     0.67 |       62 | 55.91%     | ok               |
|          15 | 15.02%   | 58.62%             | -15.70% |     0.52 |       65 | 58.57%     | ok               |
|          25 | 8.86%    | 58.62%             | -16.10% |     0.35 |       60 | 54.24%     | ok               |
|          30 | 1.26%    | 58.62%             | -18.77% |     0.1  |       70 | 52.25%     | ok               |
|          35 | -1.29%   | 58.62%             | -21.19% |     0.01 |       64 | 49.08%     | ok               |

## VWO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -7.30%   | 52.63%             | -21.18% |    -0.25 |       60 | 32.61%     | ok               |
|          15 | -9.03%   | 52.63%             | -24.01% |    -0.26 |       69 | 49.42%     | ok               |
|          20 | -10.06%  | 52.63%             | -26.14% |    -0.31 |       67 | 47.25%     | ok               |
|          40 | -8.98%   | 52.63%             | -23.57% |    -0.31 |       70 | 37.94%     | ok               |
|          45 | -9.11%   | 52.63%             | -23.26% |    -0.33 |       62 | 35.11%     | ok               |

## VZ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 0.03%    | 22.62%             | -16.98% |     0.06 |       52 | 27.29%     | ok               |
|          45 | -6.88%   | 22.62%             | -20.38% |    -0.16 |       58 | 30.12%     | ok               |
|          35 | -10.81%  | 22.62%             | -24.68% |    -0.28 |       59 | 35.77%     | ok               |
|          25 | -14.14%  | 22.62%             | -28.84% |    -0.35 |       76 | 43.59%     | ok               |
|          40 | -15.42%  | 22.62%             | -26.72% |    -0.45 |       64 | 32.61%     | ok               |

## WFC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 0.64%    | 61.17%             | -18.29% |     0.09 |       52 | 31.45%     | ok               |
|          35 | -8.15%   | 61.17%             | -23.06% |    -0.11 |       75 | 43.59%     | ok               |
|          45 | -7.65%   | 61.17%             | -23.40% |    -0.16 |       58 | 35.77%     | ok               |
|          20 | -19.25%  | 61.17%             | -28.10% |    -0.29 |       79 | 52.91%     | ok               |
|          40 | -13.37%  | 61.17%             | -24.26% |    -0.33 |       72 | 39.43%     | ok               |

## WIF-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 39.08%   | -90.33%            | -40.67% |     0.56 |       69 | 38.51%     | ok               |
|          15 | 36.69%   | -90.33%            | -46.21% |     0.55 |       76 | 41.38%     | ok               |
|          25 | 2.20%    | -90.33%            | -45.19% |     0.31 |       73 | 35.63%     | ok               |
|          50 | -3.56%   | -90.33%            | -31.17% |     0.11 |       32 | 10.92%     | ok               |
|          45 | -17.40%  | -90.33%            | -44.01% |    -0.08 |       42 | 13.41%     | ok               |

## WMT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 65.00%   | 112.91%            | -9.85%  |     1.63 |       36 | 45.92%     | ok               |
|          40 | 60.15%   | 112.91%            | -9.99%  |     1.52 |       40 | 46.92%     | ok               |
|          35 | 61.48%   | 112.91%            | -9.90%  |     1.51 |       48 | 50.58%     | ok               |
|          50 | 53.37%   | 112.91%            | -12.19% |     1.49 |       32 | 43.43%     | ok               |
|          30 | 39.66%   | 112.91%            | -21.31% |     1.01 |       55 | 53.24%     | ok               |

## XBI Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 0.42%    | 36.50%             | -16.71% |     0.09 |       62 | 34.94%     | ok               |
|          45 | -0.35%   | 36.50%             | -16.88% |     0.07 |       54 | 31.78%     | ok               |
|          35 | -6.32%   | 36.50%             | -20.11% |    -0.07 |       64 | 38.27%     | ok               |
|          50 | -6.28%   | 36.50%             | -16.83% |    -0.1  |       56 | 28.45%     | ok               |
|          30 | -8.11%   | 36.50%             | -20.48% |    -0.12 |       64 | 40.10%     | ok               |

## XLB Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 0.40%    | 23.06%             | -17.59% |     0.07 |       42 | 27.29%     | ok               |
|          40 | -1.80%   | 23.06%             | -19.67% |    -0.01 |       56 | 31.61%     | ok               |
|          45 | -2.15%   | 23.06%             | -19.78% |    -0.03 |       44 | 28.45%     | ok               |
|          35 | -5.03%   | 23.06%             | -22.65% |    -0.13 |       58 | 34.94%     | ok               |
|          25 | -10.74%  | 23.06%             | -23.63% |    -0.34 |       67 | 41.43%     | ok               |

## XLC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 20.34%   | 55.55%             | -12.33% |     0.67 |       63 | 56.91%     | ok               |
|          25 | 18.08%   | 55.55%             | -12.31% |     0.6  |       60 | 58.74%     | ok               |
|          40 | 14.33%   | 55.55%             | -13.38% |     0.54 |       66 | 49.58%     | ok               |
|          35 | 14.30%   | 55.55%             | -13.38% |     0.53 |       62 | 54.08%     | ok               |
|          20 | 9.77%    | 55.55%             | -13.37% |     0.35 |       68 | 61.40%     | ok               |

## XLE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -0.94%   | 40.75%             | -25.98% |     0.05 |       60 | 37.10%     | ok               |
|          35 | -1.99%   | 40.75%             | -31.51% |     0.03 |       69 | 44.43%     | ok               |
|          45 | -3.24%   | 40.75%             | -29.68% |    -0.02 |       64 | 39.60%     | ok               |
|          25 | -8.48%   | 40.75%             | -36.05% |    -0.13 |       87 | 49.92%     | ok               |
|          40 | -9.27%   | 40.75%             | -34.51% |    -0.19 |       68 | 42.10%     | ok               |

## XLF Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -8.76%   | 36.32%             | -21.04% |    -0.26 |       68 | 55.74%     | ok               |
|          15 | -12.54%  | 36.32%             | -23.87% |    -0.4  |       76 | 58.57%     | ok               |
|          25 | -16.41%  | 36.32%             | -24.49% |    -0.6  |       77 | 52.08%     | ok               |
|          30 | -16.62%  | 36.32%             | -24.78% |    -0.63 |       76 | 49.42%     | ok               |
|          35 | -18.65%  | 36.32%             | -27.06% |    -0.74 |       66 | 45.42%     | ok               |

## XLI Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 13.48%   | 55.79%             | -10.36% |     0.5  |       72 | 55.74%     | ok               |
|          20 | 8.31%    | 55.79%             | -12.74% |     0.36 |       65 | 50.42%     | ok               |
|          50 | 6.69%    | 55.79%             | -9.25%  |     0.34 |       58 | 35.77%     | ok               |
|          45 | 6.38%    | 55.79%             | -12.27% |     0.32 |       66 | 38.44%     | ok               |
|          30 | 5.94%    | 55.79%             | -11.38% |     0.28 |       66 | 47.92%     | ok               |

## XLK Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 109.76%  | 109.70%            | -14.75% |     1.66 |       41 | 54.08%     | ok               |
|          20 | 100.67%  | 109.70%            | -14.75% |     1.61 |       46 | 52.08%     | ok               |
|          25 | 92.08%   | 109.70%            | -14.75% |     1.56 |       40 | 50.08%     | ok               |
|          30 | 89.57%   | 109.70%            | -14.75% |     1.56 |       40 | 48.92%     | ok               |
|          35 | 68.63%   | 109.70%            | -13.61% |     1.34 |       52 | 46.26%     | ok               |

## XLM-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 48.44%   | -32.87%            | -33.55% |     0.66 |       50 | 33.33%     | ok               |
|          50 | 44.30%   | -32.87%            | -27.60% |     0.63 |       46 | 29.50%     | ok               |
|          30 | 22.08%   | -32.87%            | -41.96% |     0.44 |       69 | 47.51%     | ok               |
|          40 | 15.04%   | -32.87%            | -35.98% |     0.37 |       49 | 37.55%     | ok               |
|          35 | 12.88%   | -32.87%            | -41.26% |     0.35 |       69 | 43.68%     | ok               |

## XLP Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 10.20%   | 12.51%             | -5.66%  |     0.63 |       58 | 34.61%     | ok               |
|          40 | 9.05%    | 12.51%             | -7.77%  |     0.54 |       72 | 39.27%     | ok               |
|          35 | 8.10%    | 12.51%             | -9.73%  |     0.48 |       68 | 42.26%     | ok               |
|          50 | 6.39%    | 12.51%             | -6.08%  |     0.42 |       60 | 32.45%     | ok               |
|          30 | 5.85%    | 12.51%             | -10.28% |     0.36 |       72 | 44.09%     | ok               |

## XLU Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 5.28%    | 36.19%             | -9.01%  |     0.3  |       50 | 31.45%     | ok               |
|          50 | 5.24%    | 36.19%             | -9.11%  |     0.29 |       50 | 30.78%     | ok               |
|          40 | 2.57%    | 36.19%             | -9.85%  |     0.17 |       58 | 32.61%     | ok               |
|          35 | -4.23%   | 36.19%             | -14.25% |    -0.15 |       64 | 35.27%     | ok               |
|          30 | -6.01%   | 36.19%             | -15.29% |    -0.23 |       69 | 38.44%     | ok               |

## XLV Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -8.93%   | 4.33%              | -14.23% |    -0.42 |       66 | 37.60%     | ok               |
|          25 | -11.65%  | 4.33%              | -16.79% |    -0.56 |       70 | 39.43%     | ok               |
|          45 | -11.75%  | 4.33%              | -16.50% |    -0.68 |       56 | 27.62%     | ok               |
|          35 | -13.81%  | 4.33%              | -18.49% |    -0.73 |       66 | 34.78%     | ok               |
|          20 | -15.59%  | 4.33%              | -20.35% |    -0.76 |       75 | 41.10%     | ok               |

## XLY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 2.94%    | 34.46%             | -12.94% |     0.16 |       74 | 41.43%     | ok               |
|          30 | -0.80%   | 34.46%             | -14.01% |     0.04 |       76 | 44.59%     | ok               |
|          45 | -1.70%   | 34.46%             | -13.71% |    -0.01 |       52 | 32.28%     | ok               |
|          50 | -1.99%   | 34.46%             | -13.71% |    -0.03 |       52 | 29.62%     | ok               |
|          15 | -4.25%   | 34.46%             | -15.77% |    -0.04 |       79 | 52.75%     | ok               |

## XOM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 1.96%    | 50.06%             | -21.35% |     0.13 |       40 | 29.28%     | ok               |
|          40 | 0.98%    | 50.06%             | -21.45% |     0.1  |       48 | 33.28%     | ok               |
|          25 | -0.20%   | 50.06%             | -19.90% |     0.07 |       61 | 38.10%     | ok               |
|          30 | -0.77%   | 50.06%             | -20.29% |     0.05 |       61 | 36.77%     | ok               |
|          35 | -1.46%   | 50.06%             | -20.93% |     0.03 |       60 | 35.27%     | ok               |

## XRP-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | -35.88%  | -41.24%            | -55.83% |    -0.32 |       74 | 41.19%     | ok               |
|          40 | -41.34%  | -41.24%            | -54.34% |    -0.47 |       64 | 35.25%     | ok               |
|          30 | -47.90%  | -41.24%            | -63.50% |    -0.54 |       78 | 45.59%     | ok               |
|          50 | -43.13%  | -41.24%            | -46.41% |    -0.63 |       64 | 23.56%     | ok               |
|          45 | -51.42%  | -41.24%            | -56.00% |    -0.72 |       64 | 30.65%     | ok               |

## YFI-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -40.89%  | -74.38%            | -50.17% |    -0.71 |       62 | 25.29%     | ok               |
|          30 | -57.18%  | -74.38%            | -67.78% |    -0.94 |       85 | 38.89%     | ok               |
|          45 | -47.08%  | -74.38%            | -51.92% |    -0.99 |       60 | 21.07%     | ok               |
|          35 | -57.94%  | -74.38%            | -64.34% |    -1.04 |       75 | 32.76%     | ok               |
|          50 | -46.82%  | -74.38%            | -51.80% |    -1.07 |       50 | 17.05%     | ok               |

## ZEC-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 124.17%  | 952.55%            | -24.66% |     0.9  |       50 | 23.18%     | ok               |
|          35 | 90.22%   | 952.55%            | -43.54% |     0.76 |       58 | 30.84%     | ok               |
|          25 | 76.78%   | 952.55%            | -46.61% |     0.7  |       59 | 39.66%     | ok               |
|          50 | 54.10%   | 952.55%            | -37.94% |     0.6  |       52 | 20.69%     | ok               |
|          30 | 46.51%   | 952.55%            | -46.93% |     0.57 |       67 | 36.40%     | ok               |
