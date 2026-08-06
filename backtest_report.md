# Market Tracker Backtest Report

_Generated: 2026-08-06T03:46:44+00:00_

## Data Sources

- Crypto: Kraken -> Coinbase -> CoinGecko OHLC -> CoinPaprika fallback chain.
- Stocks / ETFs / indices: Stooq -> Yahoo Finance fallback chain.
- Data rows are generated from real market APIs. Mock OHLCV rows are not generated.

## Data Freshness

- Rows: **92,574**
- Symbols: **161**
- Date range: **2024-03-13** to **2026-08-06**

## Latest Signals

| symbol     | date                |         close |   composite_score | signal   | data_source   |
|:-----------|:--------------------|--------------:|------------------:|:---------|:--------------|
| ADBE       | 2026-08-05 00:00:00 |   259.32      |         34.8333   | LONG     | Yahoo Finance |
| AMGN       | 2026-08-05 00:00:00 |   407.83      |         65.75     | LONG     | Yahoo Finance |
| AMZN       | 2026-08-05 00:00:00 |   272.65      |         70.75     | LONG     | Yahoo Finance |
| BA         | 2026-08-05 00:00:00 |   240.19      |         65.5833   | LONG     | Yahoo Finance |
| BLK        | 2026-08-05 00:00:00 |  1133.58      |         54.6667   | LONG     | Yahoo Finance |
| C          | 2026-08-05 00:00:00 |   137.64      |         67.4167   | LONG     | Yahoo Finance |
| COP        | 2026-08-05 00:00:00 |   115.04      |         56.1667   | LONG     | Yahoo Finance |
| CVX        | 2026-08-05 00:00:00 |   186.41      |         33.8333   | LONG     | Yahoo Finance |
| EEM        | 2026-08-05 00:00:00 |    65.72      |         57.9167   | LONG     | Yahoo Finance |
| FXI        | 2026-08-05 00:00:00 |    36.08      |         35.1667   | LONG     | Yahoo Finance |
| GE         | 2026-08-05 00:00:00 |   381.22      |         52.75     | LONG     | Yahoo Finance |
| HON        | 2026-08-05 00:00:00 |   248.12      |         75.25     | LONG     | Yahoo Finance |
| IEMG       | 2026-08-05 00:00:00 |    79.96      |         59.9167   | LONG     | Yahoo Finance |
| INTC       | 2026-08-05 00:00:00 |   101.06      |         37.9167   | LONG     | Yahoo Finance |
| INTU       | 2026-08-05 00:00:00 |   327.94      |         33.0833   | LONG     | Yahoo Finance |
| ITA        | 2026-08-05 00:00:00 |   252.28      |         52.75     | LONG     | Yahoo Finance |
| IWM        | 2026-08-05 00:00:00 |   299.77      |         76.0833   | LONG     | Yahoo Finance |
| MSFT       | 2026-08-05 00:00:00 |   487.46      |         54.4167   | LONG     | Yahoo Finance |
| PFE        | 2026-08-05 00:00:00 |    25.81      |         60.5833   | LONG     | Yahoo Finance |
| PM         | 2026-08-05 00:00:00 |   188.93      |         35.4167   | LONG     | Yahoo Finance |
| QQQ        | 2026-08-05 00:00:00 |   717.3       |         57.9167   | LONG     | Yahoo Finance |
| RTX        | 2026-08-05 00:00:00 |   222.31      |         62.25     | LONG     | Yahoo Finance |
| SCHW       | 2026-08-05 00:00:00 |   108.02      |         51.5833   | LONG     | Yahoo Finance |
| SHIB-USD   | 2026-08-06 00:00:00 |     4.818e-06 |         42.6667   | LONG     | Kraken API    |
| SLB        | 2026-08-05 00:00:00 |    49.91      |         70.4167   | LONG     | Yahoo Finance |
| TGT        | 2026-08-05 00:00:00 |   147.7       |         74.9167   | LONG     | Yahoo Finance |
| TRX-USD    | 2026-08-06 00:00:00 |     0.327985  |         52.9167   | LONG     | Kraken API    |
| UNI-USD    | 2026-08-06 00:00:00 |     4.1062    |         54.5      | LONG     | Kraken API    |
| VTI        | 2026-08-05 00:00:00 |   379.65      |         72.75     | LONG     | Yahoo Finance |
| VZ         | 2026-08-05 00:00:00 |    46.47      |         78.6667   | LONG     | Yahoo Finance |
| XBI        | 2026-08-05 00:00:00 |   153.01      |         53.25     | LONG     | Yahoo Finance |
| XLE        | 2026-08-05 00:00:00 |    57.31      |         30.0833   | LONG     | Yahoo Finance |
| XLI        | 2026-08-05 00:00:00 |   186.35      |         76.0833   | LONG     | Yahoo Finance |
| XLK        | 2026-08-05 00:00:00 |   185.91      |         67.4167   | LONG     | Yahoo Finance |
| XLP        | 2026-08-05 00:00:00 |    85.33      |         68.9167   | LONG     | Yahoo Finance |
| XOM        | 2026-08-05 00:00:00 |   151.63      |         73.6667   | LONG     | Yahoo Finance |
| ZEC-USD    | 2026-08-06 00:00:00 |   508.05      |         67        | LONG     | Kraken API    |
| AAPL       | 2026-08-05 00:00:00 |   311         |         18.4167   | NEUTRAL  | Yahoo Finance |
| AAVE-USD   | 2026-08-06 00:00:00 |    88.25      |        -50.75     | NEUTRAL  | Kraken API    |
| ABBV       | 2026-08-05 00:00:00 |   246.2       |          0.416667 | NEUTRAL  | Yahoo Finance |
| ADA-USD    | 2026-08-06 00:00:00 |     0.189962  |         39.0833   | NEUTRAL  | Kraken API    |
| AGG        | 2026-08-05 00:00:00 |    97.71      |        -36.6667   | NEUTRAL  | Yahoo Finance |
| ALGO-USD   | 2026-08-06 00:00:00 |     0.08761   |         41.0833   | NEUTRAL  | Kraken API    |
| AMAT       | 2026-08-05 00:00:00 |   534.24      |          6.66667  | NEUTRAL  | Yahoo Finance |
| AMD        | 2026-08-05 00:00:00 |   482.05      |        -33.75     | NEUTRAL  | Yahoo Finance |
| APT-USD    | 2026-08-06 00:00:00 |     0.5937    |         -9.75     | NEUTRAL  | Kraken API    |
| ARKK       | 2026-08-05 00:00:00 |    76.18      |          4.91667  | NEUTRAL  | Yahoo Finance |
| ATOM-USD   | 2026-08-06 00:00:00 |     1.3365    |        -19        | NEUTRAL  | Kraken API    |
| AVAX-USD   | 2026-08-06 00:00:00 |     6.64      |         18.4167   | NEUTRAL  | Kraken API    |
| AVGO       | 2026-08-05 00:00:00 |   418.28      |         41.5      | NEUTRAL  | Yahoo Finance |
| BAC        | 2026-08-05 00:00:00 |    63.25      |         26.8333   | NEUTRAL  | Yahoo Finance |
| BCH-USD    | 2026-08-06 00:00:00 |   213.43      |        -11.8333   | NEUTRAL  | Kraken API    |
| BITO       | 2026-08-05 00:00:00 |     8.77      |         -4.25     | NEUTRAL  | Yahoo Finance |
| BND        | 2026-08-05 00:00:00 |    72.46      |        -25.4167   | NEUTRAL  | Yahoo Finance |
| BONK-USD   | 2026-08-06 00:00:00 |     2.918e-06 |        -20.75     | NEUTRAL  | Kraken API    |
| BTC-USD    | 2026-08-06 00:00:00 | 64450.8       |        -18.4167   | NEUTRAL  | Kraken API    |
| CAT        | 2026-08-05 00:00:00 |   871.08      |        -12.5833   | NEUTRAL  | Yahoo Finance |
| CL         | 2026-08-05 00:00:00 |    93.28      |         37.8333   | NEUTRAL  | Yahoo Finance |
| CMCSA      | 2026-08-05 00:00:00 |    24.75      |         41.5      | NEUTRAL  | Yahoo Finance |
| COST       | 2026-08-05 00:00:00 |   941.99      |         -7.75     | NEUTRAL  | Yahoo Finance |
| CRM        | 2026-08-05 00:00:00 |   192.98      |         23.5      | NEUTRAL  | Yahoo Finance |
| CRV-USD    | 2026-08-06 00:00:00 |     0.20411   |        -46.5833   | NEUTRAL  | Kraken API    |
| CSCO       | 2026-08-05 00:00:00 |   121.5       |         59.5      | NEUTRAL  | Yahoo Finance |
| DBC        | 2026-08-05 00:00:00 |    28.48      |          9.58333  | NEUTRAL  | Yahoo Finance |
| DE         | 2026-08-05 00:00:00 |   612         |         50.3333   | NEUTRAL  | Yahoo Finance |
| DIA        | 2026-08-05 00:00:00 |   542.81      |         64.8333   | NEUTRAL  | Yahoo Finance |
| DIS        | 2026-08-05 00:00:00 |   101.76      |         22.25     | NEUTRAL  | Yahoo Finance |
| DOGE-USD   | 2026-08-06 00:00:00 |     0.0696142 |         -1.33333  | NEUTRAL  | Kraken API    |
| DOT-USD    | 2026-08-06 00:00:00 |     0.84      |         27.6667   | NEUTRAL  | Kraken API    |
| DXY-INDEX  | 2026-08-05 00:00:00 |    99.714     |        -13.172    | NEUTRAL  | Yahoo Finance |
| EFA        | 2026-08-05 00:00:00 |   107.43      |         46.8333   | NEUTRAL  | Yahoo Finance |
| EOG        | 2026-08-05 00:00:00 |   134.23      |         -3.83333  | NEUTRAL  | Yahoo Finance |
| ETH-USD    | 2026-08-06 00:00:00 |  1894.07      |         17.5      | NEUTRAL  | Kraken API    |
| EWJ        | 2026-08-05 00:00:00 |    95.16      |         47.3333   | NEUTRAL  | Yahoo Finance |
| FCX        | 2026-08-05 00:00:00 |    69.39      |         60        | NEUTRAL  | Yahoo Finance |
| FET-USD    | 2026-08-06 00:00:00 |     0.1407    |         -9.91667  | NEUTRAL  | Kraken API    |
| FIL-USD    | 2026-08-06 00:00:00 |     0.711     |         -9.66667  | NEUTRAL  | Kraken API    |
| GDX        | 2026-08-05 00:00:00 |    83.68      |         54.5      | NEUTRAL  | Yahoo Finance |
| GDXJ       | 2026-08-05 00:00:00 |   109.48      |         54.5      | NEUTRAL  | Yahoo Finance |
| GLD        | 2026-08-05 00:00:00 |   389.64      |         26.1667   | NEUTRAL  | Yahoo Finance |
| GOOGL      | 2026-08-05 00:00:00 |   362.43      |         39        | NEUTRAL  | Yahoo Finance |
| GRT-USD    | 2026-08-06 00:00:00 |     0.0145    |        -17        | NEUTRAL  | Kraken API    |
| GS         | 2026-08-05 00:00:00 |  1060.38      |         11.1667   | NEUTRAL  | Yahoo Finance |
| HBAR-USD   | 2026-08-06 00:00:00 |     0.06872   |        -14.6667   | NEUTRAL  | Kraken API    |
| HD         | 2026-08-05 00:00:00 |   353.14      |         58.0833   | NEUTRAL  | Yahoo Finance |
| HYG        | 2026-08-05 00:00:00 |    79.52      |        -17.5      | NEUTRAL  | Yahoo Finance |
| IBIT       | 2026-08-05 00:00:00 |    36.74      |        -18.8333   | NEUTRAL  | Yahoo Finance |
| IBM        | 2026-08-05 00:00:00 |   235.92      |          0.666667 | NEUTRAL  | Yahoo Finance |
| ICP-USD    | 2026-08-06 00:00:00 |     2.099     |        -16.6667   | NEUTRAL  | Kraken API    |
| IEF        | 2026-08-05 00:00:00 |    93.31      |        -40.1667   | NEUTRAL  | Yahoo Finance |
| INJ-USD    | 2026-08-06 00:00:00 |     4.737     |        -39.5      | NEUTRAL  | Kraken API    |
| JNJ        | 2026-08-05 00:00:00 |   257.59      |         32        | NEUTRAL  | Yahoo Finance |
| JPM        | 2026-08-05 00:00:00 |   359.24      |         52.4167   | NEUTRAL  | Yahoo Finance |
| KO         | 2026-08-05 00:00:00 |    86.83      |         62.3333   | NEUTRAL  | Yahoo Finance |
| LIN        | 2026-08-05 00:00:00 |   491.05      |        -13.0833   | NEUTRAL  | Yahoo Finance |
| LINK-USD   | 2026-08-06 00:00:00 |     8.10924   |        -34.0833   | NEUTRAL  | Kraken API    |
| LLY        | 2026-08-05 00:00:00 |  1169.86      |         16.5      | NEUTRAL  | Yahoo Finance |
| LRCX       | 2026-08-05 00:00:00 |   307.42      |         -2        | NEUTRAL  | Yahoo Finance |
| MCD        | 2026-08-05 00:00:00 |   274         |         -0.666667 | NEUTRAL  | Yahoo Finance |
| MPC        | 2026-08-05 00:00:00 |   297.75      |         15.9167   | NEUTRAL  | Yahoo Finance |
| MRK        | 2026-08-05 00:00:00 |   128.33      |         49        | NEUTRAL  | Yahoo Finance |
| MS         | 2026-08-05 00:00:00 |   218.27      |         18        | NEUTRAL  | Yahoo Finance |
| MU         | 2026-08-05 00:00:00 |   893.19      |         11.5833   | NEUTRAL  | Yahoo Finance |
| NEM        | 2026-08-05 00:00:00 |   104.29      |         54.75     | NEUTRAL  | Yahoo Finance |
| NFLX       | 2026-08-05 00:00:00 |    74.2       |         -3.58333  | NEUTRAL  | Yahoo Finance |
| NKE        | 2026-08-05 00:00:00 |    42.45      |        -62        | NEUTRAL  | Yahoo Finance |
| NOW        | 2026-08-05 00:00:00 |   117.22      |         10.5      | NEUTRAL  | Yahoo Finance |
| NVDA       | 2026-08-05 00:00:00 |   219.22      |         33        | NEUTRAL  | Yahoo Finance |
| OP-USD     | 2026-08-06 00:00:00 |     0.0873    |        -26        | NEUTRAL  | Kraken API    |
| ORCL       | 2026-08-05 00:00:00 |   144.39      |         -1.33333  | NEUTRAL  | Yahoo Finance |
| OXY        | 2026-08-05 00:00:00 |    53.81      |         15.8333   | NEUTRAL  | Yahoo Finance |
| PEP        | 2026-08-05 00:00:00 |   138.78      |        -27.5      | NEUTRAL  | Yahoo Finance |
| PEPE-USD   | 2026-08-06 00:00:00 |     2.844e-06 |         27.0833   | NEUTRAL  | Kraken API    |
| PG         | 2026-08-05 00:00:00 |   146.8       |        -53.5      | NEUTRAL  | Yahoo Finance |
| POL-USD    | 2026-08-06 00:00:00 |     0.07519   |         -0.333333 | NEUTRAL  | Kraken API    |
| SBUX       | 2026-08-05 00:00:00 |   106         |         28.6667   | NEUTRAL  | Yahoo Finance |
| SHY        | 2026-08-05 00:00:00 |    81.9       |        -29.9167   | NEUTRAL  | Yahoo Finance |
| SLV        | 2026-08-05 00:00:00 |    56.07      |         -9.66667  | NEUTRAL  | Yahoo Finance |
| SMH        | 2026-08-05 00:00:00 |   569.7       |         29.1667   | NEUTRAL  | Yahoo Finance |
| SNX-USD    | 2026-08-06 00:00:00 |     0.2138    |        -12.8333   | NEUTRAL  | Kraken API    |
| SOXX       | 2026-08-05 00:00:00 |   530.7       |         10.4167   | NEUTRAL  | Yahoo Finance |
| SPY        | 2026-08-05 00:00:00 |   769.79      |         61.5      | NEUTRAL  | Yahoo Finance |
| SUSHI-USD  | 2026-08-06 00:00:00 |     0.1535    |        -51.5833   | NEUTRAL  | Kraken API    |
| T          | 2026-08-05 00:00:00 |    23.06      |         15.9167   | NEUTRAL  | Yahoo Finance |
| TIA-USD    | 2026-08-06 00:00:00 |     0.3326    |        -17        | NEUTRAL  | Kraken API    |
| TMO        | 2026-08-05 00:00:00 |   577.83      |         47.5833   | NEUTRAL  | Yahoo Finance |
| TXN        | 2026-08-05 00:00:00 |   277.72      |        -12.25     | NEUTRAL  | Yahoo Finance |
| UNH        | 2026-08-05 00:00:00 |   412.75      |          9.41667  | NEUTRAL  | Yahoo Finance |
| UPS        | 2026-08-05 00:00:00 |   107.7       |        -13.5      | NEUTRAL  | Yahoo Finance |
| USO        | 2026-08-05 00:00:00 |   114.88      |         -1.83333  | NEUTRAL  | Yahoo Finance |
| VEA        | 2026-08-05 00:00:00 |    72.35      |         64.8333   | NEUTRAL  | Yahoo Finance |
| VIXY       | 2026-08-05 00:00:00 |    19.77      |        -29.1667   | NEUTRAL  | Yahoo Finance |
| VNQ        | 2026-08-05 00:00:00 |    98.92      |         22.4167   | NEUTRAL  | Yahoo Finance |
| VWO        | 2026-08-05 00:00:00 |    60.01      |         46.8333   | NEUTRAL  | Yahoo Finance |
| WFC        | 2026-08-05 00:00:00 |    89.17      |         39.8333   | NEUTRAL  | Yahoo Finance |
| WIF-USD    | 2026-08-06 00:00:00 |     0.1402    |        -52.25     | NEUTRAL  | Kraken API    |
| WMT        | 2026-08-05 00:00:00 |   112.34      |        -11.1667   | NEUTRAL  | Yahoo Finance |
| XLB        | 2026-08-05 00:00:00 |    52.64      |         63.6667   | NEUTRAL  | Yahoo Finance |
| XLC        | 2026-08-05 00:00:00 |   110.87      |        -10.5      | NEUTRAL  | Yahoo Finance |
| XLF        | 2026-08-05 00:00:00 |    58         |         59.8333   | NEUTRAL  | Yahoo Finance |
| XLU        | 2026-08-05 00:00:00 |    43.66      |        -63        | NEUTRAL  | Yahoo Finance |
| XLV        | 2026-08-05 00:00:00 |   164.16      |         32.5      | NEUTRAL  | Yahoo Finance |
| XLY        | 2026-08-05 00:00:00 |   118.64      |         43.5      | NEUTRAL  | Yahoo Finance |
| XRP-USD    | 2026-08-06 00:00:00 |     1.04571   |        -48.75     | NEUTRAL  | Kraken API    |
| YFI-USD    | 2026-08-06 00:00:00 |  2077.4       |          9.08333  | NEUTRAL  | Kraken API    |
| ARB-USD    | 2026-08-06 00:00:00 |     0.0798    |        -33.6667   | SHORT    | Kraken API    |
| COMP-USD   | 2026-08-06 00:00:00 |    16.46      |        -30.8333   | SHORT    | Kraken API    |
| DASH-USD   | 2026-08-06 00:00:00 |    30.685     |        -40        | SHORT    | Kraken API    |
| ETC-USD    | 2026-08-06 00:00:00 |     6.482     |        -35.3333   | SHORT    | Kraken API    |
| LDO-USD    | 2026-08-06 00:00:00 |     0.297     |        -46.3333   | SHORT    | Kraken API    |
| LTC-USD    | 2026-08-06 00:00:00 |    44.91      |        -37        | SHORT    | Kraken API    |
| META       | 2026-08-05 00:00:00 |   588.77      |        -51.1667   | SHORT    | Yahoo Finance |
| NEAR-USD   | 2026-08-06 00:00:00 |     1.7065    |        -31        | SHORT    | Kraken API    |
| QCOM       | 2026-08-05 00:00:00 |   157.53      |        -41.25     | SHORT    | Yahoo Finance |
| RENDER-USD | 2026-08-06 00:00:00 |     1.317     |        -49.3333   | SHORT    | Kraken API    |
| SKY-USD    | 2026-08-06 00:00:00 |     0.05649   |        -45.8333   | SHORT    | Kraken API    |
| SOL-USD    | 2026-08-06 00:00:00 |    73.41      |        -42.8333   | SHORT    | Kraken API    |
| TLT        | 2026-08-05 00:00:00 |    83         |        -41.75     | SHORT    | Yahoo Finance |
| TMUS       | 2026-08-05 00:00:00 |   173.46      |        -35.75     | SHORT    | Yahoo Finance |
| TSLA       | 2026-08-05 00:00:00 |   321.55      |        -61.9167   | SHORT    | Yahoo Finance |
| XLM-USD    | 2026-08-06 00:00:00 |     0.162298  |        -49.8333   | SHORT    | Kraken API    |

## Edge Summary

- Symbols with trades: **160** of 160
- Beat buy-and-hold: **31.25%** of traded symbols
- Positive return: **30.00%** of traded symbols
- Median strategy return: **-10.26%** (benchmark **15.41%**)
- Median excess vs benchmark: **-27.59%**
- Median Sharpe: **-0.12**
- Median exposure: **43.82%**

> Edge is real only if both _beat buy-and-hold_ and _median excess_ are convincingly positive across many symbols. Treat a single high-return symbol as noise.

## Portfolio Backtest

Actual capital-allocation books (not per-symbol averages). Benchmarks: `equal_weight_buyhold` (whole tracked universe), `spy_buyhold` (100% SPY), and `sixty_forty` (60% SPY / 40% AGG). `high_conf_voltarget` inverse-vol-weights the HIGH-confidence book; `conviction_long_short` is market-neutral. Judge on **Sharpe** and **max_drawdown** out-of-sample, not raw return: a fully-invested long book wins on return in a bull market but carries all the risk.

| strategy              | scope         | ann_return   | ann_vol   |   sharpe | max_drawdown   | total_return   |   avg_gross_exposure |
|:----------------------|:--------------|:-------------|:----------|---------:|:---------------|:---------------|---------------------:|
| equal_weight_buyhold  | full          | 0.52%        | 29.66%    |     0.02 | -39.63%        | -11.16%        |                 1    |
| equal_weight_buyhold  | out_of_sample | -19.76%      | 29.02%    |    -0.68 | -33.57%        | -22.50%        |                 1    |
| all_signals_ew        | full          | -15.93%      | 25.18%    |    -0.63 | -57.12%        | -44.02%        |                 1    |
| all_signals_ew        | out_of_sample | 15.70%       | 23.79%    |     0.66 | -20.95%        | 14.69%         |                 1    |
| high_conf_ew          | full          | -0.10%       | 30.92%    |    -0    | -40.84%        | -13.56%        |                 0.88 |
| high_conf_ew          | out_of_sample | 13.06%       | 25.67%    |     0.51 | -21.63%        | 10.88%         |                 0.88 |
| high_conf_voltarget   | full          | 2.83%        | 28.37%    |     0.1  | -33.89%        | -3.29%         |                 0.88 |
| high_conf_voltarget   | out_of_sample | 6.27%        | 22.26%    |     0.28 | -16.94%        | 4.05%          |                 0.88 |
| conviction_long_short | full          | -17.24%      | 22.74%    |    -0.76 | -46.89%        | -45.30%        |                 0.97 |
| conviction_long_short | out_of_sample | -6.35%       | 22.22%    |    -0.29 | -24.12%        | -8.96%         |                 0.97 |
| spy_buyhold           | full          | 5.49%        | 13.46%    |     0.41 | -19.51%        | 14.96%         |                 0.79 |
| spy_buyhold           | out_of_sample | 0.49%        | 10.13%    |     0.05 | -12.06%        | -0.02%         |                 0.79 |
| sixty_forty           | full          | 3.14%        | 8.52%     |     0.37 | -11.81%        | 8.79%          |                 0.79 |
| sixty_forty           | out_of_sample | -1.08%       | 6.70%     |    -0.16 | -8.26%         | -1.38%         |                 0.79 |

## Walk-Forward Robustness

Each book measured across contiguous time folds (each a different regime). A book has durable edge only if `mean_sharpe` is positive, `min_sharpe` isn't deeply negative, and `pct_positive_folds` is high — a single great fold doesn't count. `fold_sharpes` lists each fold oldest-to-newest.

| strategy              |   n_folds |   mean_sharpe |   median_sharpe |   min_sharpe | pct_positive_folds   | mean_return   | fold_sharpes                 |
|:----------------------|----------:|--------------:|----------------:|-------------:|:---------------------|:--------------|:-----------------------------|
| equal_weight_buyhold  |         5 |          0.29 |            1    |        -1.24 | 60.00%               | -0.29%        | 1.43;-0.91;1.00;-1.24;1.16   |
| all_signals_ew        |         5 |         -0.84 |           -0.59 |        -2.35 | 20.00%               | -9.44%        | -0.59;-0.09;-2.35;0.77;-1.92 |
| high_conf_ew          |         5 |          0.12 |            0.13 |        -0.48 | 60.00%               | -2.65%        | 0.94;-0.48;0.13;-0.18;0.21   |
| high_conf_voltarget   |         5 |          0.37 |            0.03 |        -0.28 | 80.00%               | -0.40%        | 1.61;0.02;0.03;-0.28;0.48    |
| conviction_long_short |         5 |         -0.89 |           -1.32 |        -1.68 | 20.00%               | -10.98%       | -1.62;-1.32;0.45;-0.29;-1.68 |
| spy_buyhold           |         5 |          0.5  |            0.46 |        -1.26 | 80.00%               | 3.05%         | 1.65;0.04;1.64;-1.26;0.46    |
| sixty_forty           |         5 |          0.44 |            0.07 |        -1.21 | 80.00%               | 1.79%         | 1.61;0.03;1.69;-1.21;0.07    |

## Strategy Comparison

Each decision rule backtested over the same data. `out_of_sample` is the most recent ~35% of each symbol's history (unseen tail). A rule has real edge only if `median_excess` and `beat_benchmark_pct` stay positive out-of-sample, not just full-sample.

| strategy        | scope         |   symbols | beat_benchmark_pct   | positive_pct   | median_return   | median_benchmark   | median_excess   |   median_sharpe |   total_trades |
|:----------------|:--------------|----------:|:---------------------|:---------------|:----------------|:-------------------|:----------------|----------------:|---------------:|
| trend           | full          |       160 | 31.25%               | 30.00%         | -10.26%         | 15.41%             | -27.59%         |           -0.12 |          11261 |
| trend           | out_of_sample |       160 | 23.75%               | 41.25%         | -4.27%          | 8.15%              | -13.98%         |           -0.37 |           3831 |
| mean_reversion  | full          |       157 | 42.04%               | 50.32%         | 0.01%           | 15.03%             | -13.64%         |            0.03 |           1268 |
| mean_reversion  | out_of_sample |       127 | 44.09%               | 59.84%         | 0.39%           | 5.25%              | -7.40%          |            0.63 |            452 |
| regime_adaptive | full          |       160 | 32.50%               | 31.87%         | -10.04%         | 15.41%             | -28.20%         |           -0.11 |          11544 |
| regime_adaptive | out_of_sample |       160 | 25.00%               | 41.25%         | -3.65%          | 8.15%              | -13.83%         |           -0.29 |           3946 |

## Signal Calibration

Realized forward return in the signal's direction, grouped by confidence. HIGH should outrank LOW for the confidence score to be meaningful.

| confidence_level   |   horizon |     n | mean_return   | median_return   | win_rate   |
|:-------------------|----------:|------:|:--------------|:----------------|:-----------|
| HIGH               |         5 |  7782 | 0.08%         | 0.06%           | 51.14%     |
| MEDIUM             |         5 | 29084 | 0.02%         | 0.06%           | 50.65%     |
| LOW                |         5 |  3423 | -0.65%        | -0.56%          | 44.52%     |
| ALL                |         5 | 40289 | -0.03%        | 0.02%           | 50.22%     |
| HIGH               |        10 |  7734 | 0.29%         | 0.07%           | 50.76%     |
| MEDIUM             |        10 | 28873 | 0.11%         | 0.08%           | 50.58%     |
| LOW                |        10 |  3403 | -0.95%        | -0.77%          | 45.05%     |
| ALL                |        10 | 40010 | 0.06%         | 0.02%           | 50.14%     |
| HIGH               |        20 |  7670 | 0.59%         | 0.25%           | 52.01%     |
| MEDIUM             |        20 | 28454 | 0.71%         | 0.51%           | 52.87%     |
| LOW                |        20 |  3338 | -0.84%        | -0.69%          | 46.58%     |
| ALL                |        20 | 39462 | 0.55%         | 0.36%           | 52.17%     |

## Backtest Summary

### Data Quality / Signal Availability

- **ok**: 160 symbols

| symbol     |   trades | return   | benchmark_return   | mdd     |   sharpe | exposure   | skipped_reason   |
|:-----------|---------:|:---------|:-------------------|:--------|---------:|:-----------|:-----------------|
| AAPL       |       61 | 5.03%    | 81.73%             | -20.65% |     0.21 | 48.75%     | ok               |
| AAVE-USD   |       74 | -48.93%  | -51.05%            | -68.26% |    -0.49 | 37.93%     | ok               |
| ABBV       |       68 | -22.25%  | 36.88%             | -30.52% |    -0.48 | 46.26%     | ok               |
| ADA-USD    |       83 | -12.69%  | -77.83%            | -45.19% |     0.07 | 45.79%     | ok               |
| ADBE       |       68 | -27.71%  | -54.79%            | -31.30% |    -0.31 | 57.24%     | ok               |
| AGG        |       69 | -7.37%   | -0.02%             | -10.95% |    -1.18 | 33.78%     | ok               |
| ALGO-USD   |       80 | -28.14%  | -63.20%            | -41.20% |    -0.19 | 36.59%     | ok               |
| AMAT       |       71 | -35.59%  | 166.37%            | -57.08% |    -0.34 | 49.92%     | ok               |
| AMD        |       54 | 7.59%    | 147.47%            | -41.75% |     0.28 | 35.11%     | ok               |
| AMGN       |       73 | -7.14%   | 47.77%             | -34.19% |    -0.07 | 47.75%     | ok               |
| AMZN       |       81 | -53.49%  | 54.42%             | -54.61% |    -1.51 | 39.93%     | ok               |
| APT-USD    |       72 | -28.16%  | -89.66%            | -66.73% |    -0.06 | 41.76%     | ok               |
| ARB-USD    |       76 | -30.41%  | -79.61%            | -62.55% |    -0.12 | 41.76%     | ok               |
| ARKK       |       89 | -37.14%  | 51.27%             | -38.58% |    -0.66 | 41.10%     | ok               |
| ATOM-USD   |       88 | -67.57%  | -68.33%            | -73.98% |    -1.11 | 46.74%     | ok               |
| AVAX-USD   |       77 | -52.93%  | -68.29%            | -61.58% |    -0.65 | 38.51%     | ok               |
| AVGO       |       60 | 27.80%   | 232.53%            | -35.76% |     0.47 | 40.60%     | ok               |
| BA         |       67 | -1.82%   | 31.72%             | -30.56% |     0.1  | 48.09%     | ok               |
| BAC        |       78 | -6.12%   | 75.30%             | -27.64% |    -0.08 | 51.08%     | ok               |
| BCH-USD    |       76 | 5.55%    | -33.48%            | -54.26% |     0.27 | 50.57%     | ok               |
| BITO       |       80 | -27.89%  | -73.94%            | -39.47% |    -0.23 | 39.10%     | ok               |
| BLK        |       79 | -5.83%   | 37.24%             | -26.90% |    -0.09 | 44.76%     | ok               |
| BND        |       67 | -7.48%   | -0.04%             | -10.16% |    -1.18 | 35.27%     | ok               |
| BONK-USD   |       68 | 47.58%   | -76.50%            | -51.50% |     0.61 | 42.53%     | ok               |
| BTC-USD    |       72 | 8.49%    | -25.18%            | -23.38% |     0.28 | 51.72%     | ok               |
| C          |       81 | -30.77%  | 138.30%            | -38.11% |    -0.61 | 50.42%     | ok               |
| CAT        |       72 | 15.52%   | 155.06%            | -21.02% |     0.36 | 53.58%     | ok               |
| CL         |       62 | 4.04%    | 4.57%              | -14.32% |     0.19 | 43.59%     | ok               |
| CMCSA      |       80 | -45.05%  | -38.98%            | -48.04% |    -1.21 | 41.76%     | ok               |
| COMP-USD   |       95 | -41.75%  | -64.96%            | -55.27% |    -0.29 | 46.74%     | ok               |
| COP        |       72 | -22.09%  | -2.14%             | -43.96% |    -0.37 | 44.09%     | ok               |
| COST       |       56 | 2.10%    | 28.30%             | -29.73% |     0.13 | 41.43%     | ok               |
| CRM        |       63 | -40.74%  | -36.66%            | -42.51% |    -0.87 | 42.60%     | ok               |
| CRV-USD    |       70 | -0.17%   | -50.46%            | -39.89% |     0.23 | 36.59%     | ok               |
| CSCO       |       59 | 23.34%   | 142.47%            | -21.79% |     0.51 | 47.75%     | ok               |
| CVX        |       71 | -13.00%  | 21.13%             | -29.13% |    -0.3  | 40.43%     | ok               |
| DASH-USD   |       63 | -41.02%  | 27.55%             | -64.43% |    -0.01 | 30.08%     | ok               |
| DBC        |       62 | -13.84%  | 25.96%             | -25.70% |    -0.45 | 35.61%     | ok               |
| DE         |       70 | -5.05%   | 61.54%             | -24.56% |    -0.01 | 45.42%     | ok               |
| DIA        |       60 | -3.93%   | 38.75%             | -12.94% |    -0.18 | 43.59%     | ok               |
| DIS        |       66 | -19.35%  | -9.55%             | -28.17% |    -0.36 | 43.59%     | ok               |
| DOGE-USD   |       70 | -12.19%  | -64.98%            | -62.31% |     0.13 | 48.66%     | ok               |
| DOT-USD    |       88 | -63.03%  | -81.20%            | -67.64% |    -0.74 | 48.08%     | ok               |
| DXY-INDEX  |       42 | -1.69%   | -2.23%             | -6.29%  |    -0.25 | 32.68%     | ok               |
| EEM        |       66 | -12.19%  | 59.40%             | -25.67% |    -0.35 | 40.93%     | ok               |
| EFA        |       58 | -10.33%  | 35.23%             | -13.53% |    -0.4  | 41.60%     | ok               |
| EOG        |       81 | -25.28%  | 9.51%              | -48.13% |    -0.5  | 49.42%     | ok               |
| ETC-USD    |       62 | -31.66%  | -65.28%            | -48.09% |    -0.43 | 28.93%     | ok               |
| ETH-USD    |       60 | 177.27%  | -11.79%            | -30.11% |     1.38 | 45.79%     | ok               |
| EWJ        |       62 | -20.02%  | 37.18%             | -30.73% |    -0.68 | 36.61%     | ok               |
| FCX        |       67 | -29.92%  | 59.85%             | -48.22% |    -0.35 | 45.92%     | ok               |
| FET-USD    |       85 | -40.91%  | -77.15%            | -52.44% |    -0.19 | 41.38%     | ok               |
| FIL-USD    |       68 | -44.63%  | -76.81%            | -48.59% |    -0.54 | 34.10%     | ok               |
| FXI        |       44 | -1.83%   | 46.43%             | -23.91% |     0.04 | 30.95%     | ok               |
| GDX        |       58 | 6.19%    | 176.26%            | -34.99% |     0.23 | 46.59%     | ok               |
| GDXJ       |       64 | -25.64%  | 196.94%            | -44.93% |    -0.27 | 44.76%     | ok               |
| GE         |       80 | 2.45%    | 180.72%            | -27.82% |     0.17 | 51.41%     | ok               |
| GLD        |       50 | 22.04%   | 93.67%             | -16.63% |     0.57 | 47.25%     | ok               |
| GOOGL      |       55 | 78.89%   | 159.27%            | -20.41% |     1.18 | 52.25%     | ok               |
| GRT-USD    |       81 | 7.37%    | -86.70%            | -50.20% |     0.3  | 43.87%     | ok               |
| GS         |       74 | -1.59%   | 170.29%            | -22.13% |     0.07 | 50.58%     | ok               |
| HD         |       71 | -7.90%   | -6.82%             | -17.69% |    -0.13 | 43.76%     | ok               |
| HON        |       95 | -25.74%  | 25.68%             | -29.81% |    -0.68 | 52.41%     | ok               |
| HYG        |       83 | -9.49%   | 2.62%              | -10.00% |    -1.11 | 34.61%     | ok               |
| IBIT       |       34 | 30.82%   | -3.34%             | -18.95% |     0.65 | 31.08%     | ok               |
| IBM        |       75 | -28.39%  | 19.94%             | -48.94% |    -0.37 | 51.08%     | ok               |
| ICP-USD    |       77 | -10.52%  | -65.98%            | -50.29% |     0.15 | 34.67%     | ok               |
| IEF        |       84 | -11.27%  | -1.27%             | -12.10% |    -1.58 | 33.78%     | ok               |
| IEMG       |       60 | -10.41%  | 54.60%             | -26.84% |    -0.31 | 40.43%     | ok               |
| INJ-USD    |       75 | -52.79%  | -60.34%            | -76.24% |    -0.5  | 38.12%     | ok               |
| INTC       |       66 | 58.39%   | 133.77%            | -60.60% |     0.63 | 48.59%     | ok               |
| INTU       |       69 | -15.25%  | -49.94%            | -41.36% |    -0.14 | 42.10%     | ok               |
| ITA        |       74 | -2.83%   | 98.72%             | -23.75% |    -0.01 | 46.26%     | ok               |
| IWM        |       50 | 10.39%   | 45.72%             | -12.83% |     0.42 | 35.77%     | ok               |
| JNJ        |       70 | 5.03%    | 59.89%             | -17.51% |     0.23 | 49.92%     | ok               |
| JPM        |       75 | -24.02%  | 87.71%             | -33.16% |    -0.61 | 51.58%     | ok               |
| KO         |       51 | 23.75%   | 42.06%             | -8.20%  |     0.85 | 37.94%     | ok               |
| LDO-USD    |       78 | 16.89%   | -72.98%            | -61.16% |     0.41 | 43.87%     | ok               |
| LIN        |       68 | -12.63%  | 3.40%              | -21.38% |    -0.42 | 37.10%     | ok               |
| LINK-USD   |       71 | -2.06%   | -43.82%            | -40.80% |     0.21 | 43.68%     | ok               |
| LLY        |       67 | -25.22%  | 54.37%             | -53.34% |    -0.35 | 47.42%     | ok               |
| LRCX       |       82 | -23.96%  | 231.73%            | -61.08% |    -0.14 | 42.26%     | ok               |
| LTC-USD    |       70 | -19.67%  | -59.09%            | -38.94% |    -0.09 | 49.81%     | ok               |
| MCD        |       77 | -3.77%   | -3.13%             | -18.81% |    -0.1  | 38.27%     | ok               |
| META       |       76 | -36.02%  | 18.81%             | -42.43% |    -0.66 | 47.42%     | ok               |
| MPC        |       67 | -11.76%  | 57.63%             | -44.76% |    -0.09 | 49.92%     | ok               |
| MRK        |       67 | -27.34%  | 5.05%              | -35.95% |    -0.63 | 43.59%     | ok               |
| MS         |       77 | -10.18%  | 144.29%            | -27.79% |    -0.16 | 49.58%     | ok               |
| MSFT       |       83 | -33.43%  | 17.43%             | -38.06% |    -0.83 | 47.42%     | ok               |
| MU         |       51 | 226.76%  | 848.59%            | -68.76% |     1.24 | 57.90%     | ok               |
| NEAR-USD   |       83 | 4.96%    | -42.60%            | -59.54% |     0.3  | 40.42%     | ok               |
| NEM        |       70 | -20.55%  | 203.43%            | -38.49% |    -0.15 | 52.75%     | ok               |
| NFLX       |       72 | 19.68%   | 21.75%             | -21.09% |     0.48 | 52.91%     | ok               |
| NKE        |       83 | -36.04%  | -58.12%            | -55.35% |    -0.49 | 43.93%     | ok               |
| NOW        |       80 | 1.54%    | -24.56%            | -26.78% |     0.18 | 45.76%     | ok               |
| NVDA       |       71 | -26.95%  | 147.02%            | -45.14% |    -0.2  | 58.65%     | ok               |
| OP-USD     |       66 | -15.92%  | -91.16%            | -71.26% |     0.07 | 35.25%     | ok               |
| ORCL       |       66 | 101.39%  | 15.03%             | -30.61% |     0.88 | 56.24%     | ok               |
| OXY        |       71 | -3.62%   | -13.29%            | -34.15% |     0.06 | 46.92%     | ok               |
| PEP        |       77 | -4.68%   | -16.04%            | -21.35% |    -0.07 | 48.25%     | ok               |
| PEPE-USD   |       81 | -8.77%   | -60.53%            | -57.66% |     0.2  | 45.98%     | ok               |
| PFE        |       83 | -41.44%  | -8.54%             | -43.15% |    -1.34 | 36.61%     | ok               |
| PG         |       67 | -19.88%  | -9.55%             | -23.92% |    -0.76 | 37.44%     | ok               |
| PM         |       83 | -6.67%   | 98.21%             | -34.97% |    -0.05 | 55.91%     | ok               |
| POL-USD    |       79 | 60.31%   | -70.65%            | -41.08% |     0.76 | 49.62%     | ok               |
| QCOM       |       77 | -21.69%  | -6.92%             | -56.59% |    -0.14 | 45.59%     | ok               |
| QQQ        |       64 | 15.87%   | 62.93%             | -13.49% |     0.48 | 43.93%     | ok               |
| RENDER-USD |       98 | -6.70%   | -64.56%            | -45.62% |     0.21 | 42.15%     | ok               |
| RTX        |       54 | 44.96%   | 145.48%            | -16.99% |     0.94 | 53.91%     | ok               |
| SBUX       |       62 | -19.04%  | 15.71%             | -29.22% |    -0.35 | 39.93%     | ok               |
| SCHW       |       76 | -7.39%   | 60.91%             | -31.92% |    -0.09 | 48.92%     | ok               |
| SHIB-USD   |       76 | -33.69%  | -62.68%            | -47.96% |    -0.3  | 52.49%     | ok               |
| SHY        |       46 | -2.23%   | 0.36%              | -2.85%  |    -0.78 | 34.11%     | ok               |
| SKY-USD    |       76 | -32.73%  | -2.32%             | -47.82% |    -0.41 | 42.53%     | ok               |
| SLB        |       77 | -32.08%  | -5.06%             | -54.23% |    -0.61 | 50.58%     | ok               |
| SLV        |       62 | 40.49%   | 146.03%            | -42.66% |     0.61 | 43.59%     | ok               |
| SMH        |       48 | 66.32%   | 154.94%            | -33.66% |     0.98 | 45.76%     | ok               |
| SNX-USD    |       64 | -6.87%   | -76.11%            | -38.68% |     0.17 | 37.55%     | ok               |
| SOL-USD    |       72 | -30.61%  | -48.30%            | -46.86% |    -0.12 | 59.58%     | ok               |
| SOXX       |       56 | 66.09%   | 136.74%            | -40.14% |     0.92 | 44.26%     | ok               |
| SPY        |       62 | 0.89%    | 49.19%             | -16.47% |     0.09 | 48.92%     | ok               |
| SUSHI-USD  |      104 | -83.17%  | -79.09%            | -86.73% |    -1.34 | 38.51%     | ok               |
| T          |       62 | 34.56%   | 34.15%             | -17.01% |     0.78 | 54.24%     | ok               |
| TGT        |       62 | -18.43%  | -11.38%            | -40.57% |    -0.37 | 37.27%     | ok               |
| TIA-USD    |       89 | -40.67%  | -90.28%            | -68.36% |    -0.24 | 38.89%     | ok               |
| TLT        |       70 | -19.02%  | -12.09%            | -21.87% |    -1.41 | 33.94%     | ok               |
| TMO        |       61 | 27.81%   | -2.61%             | -18.85% |     0.59 | 52.58%     | ok               |
| TMUS       |       70 | 6.48%    | 5.71%              | -25.71% |     0.23 | 46.76%     | ok               |
| TRX-USD    |       70 | 9.99%    | 42.05%             | -22.90% |     0.35 | 48.47%     | ok               |
| TSLA       |       74 | -28.06%  | 89.73%             | -57.89% |    -0.12 | 42.60%     | ok               |
| TXN        |       71 | -15.49%  | 60.83%             | -46.98% |    -0.1  | 50.75%     | ok               |
| UNH        |       74 | 29.50%   | -15.42%            | -26.96% |     0.51 | 51.91%     | ok               |
| UNI-USD    |       92 | -74.42%  | -42.36%            | -80.61% |    -0.94 | 45.79%     | ok               |
| UPS        |       72 | -41.93%  | -30.41%            | -43.16% |    -0.87 | 40.27%     | ok               |
| USO        |       70 | 1.85%    | 52.99%             | -43.35% |     0.16 | 34.44%     | ok               |
| VEA        |       56 | -2.66%   | 44.38%             | -17.93% |    -0.06 | 42.60%     | ok               |
| VIXY       |       96 | -80.41%  | -63.28%            | -88.42% |    -1.02 | 31.78%     | ok               |
| VNQ        |       73 | -17.49%  | 14.12%             | -24.92% |    -0.74 | 37.94%     | ok               |
| VTI        |       68 | -5.73%   | 48.18%             | -18.77% |    -0.15 | 49.25%     | ok               |
| VWO        |       82 | -17.13%  | 42.91%             | -25.20% |    -0.63 | 41.93%     | ok               |
| VZ         |       83 | -26.41%  | 15.42%             | -26.98% |    -0.85 | 38.60%     | ok               |
| WFC        |       84 | -20.99%  | 54.22%             | -29.78% |    -0.37 | 49.08%     | ok               |
| WIF-USD    |       72 | -52.90%  | -78.20%            | -61.76% |    -0.39 | 33.91%     | ok               |
| WMT        |       65 | 9.02%    | 83.32%             | -21.31% |     0.32 | 48.75%     | ok               |
| XBI        |       68 | -5.27%   | 57.58%             | -18.30% |    -0.05 | 39.27%     | ok               |
| XLB        |       62 | -11.95%  | 15.39%             | -24.41% |    -0.41 | 34.94%     | ok               |
| XLC        |       65 | 14.08%   | 38.10%             | -12.33% |     0.51 | 52.58%     | ok               |
| XLE        |       75 | -13.12%  | 26.85%             | -37.64% |    -0.26 | 45.26%     | ok               |
| XLF        |       78 | -12.24%  | 40.91%             | -23.61% |    -0.4  | 47.59%     | ok               |
| XLI        |       72 | -5.50%   | 52.07%             | -14.12% |    -0.17 | 42.76%     | ok               |
| XLK        |       42 | 64.90%   | 78.13%             | -14.75% |     1.21 | 45.76%     | ok               |
| XLM-USD    |       65 | 7.39%    | -44.40%            | -50.36% |     0.3  | 45.21%     | ok               |
| XLP        |       66 | 8.40%    | 12.06%             | -8.96%  |     0.5  | 40.60%     | ok               |
| XLU        |       67 | -5.24%   | 36.69%             | -20.40% |    -0.19 | 39.10%     | ok               |
| XLV        |       66 | -15.44%  | 12.09%             | -19.17% |    -0.77 | 34.28%     | ok               |
| XLY        |       68 | 3.44%    | 31.10%             | -14.01% |     0.17 | 43.76%     | ok               |
| XOM        |       55 | 5.41%    | 38.44%             | -20.29% |     0.22 | 37.94%     | ok               |
| XRP-USD    |       52 | -5.00%   | -56.15%            | -33.91% |     0.11 | 32.95%     | ok               |
| YFI-USD    |       81 | -64.19%  | -61.20%            | -71.12% |    -1.03 | 40.61%     | ok               |
| ZEC-USD    |       66 | 37.61%   | 1300.74%           | -49.80% |     0.53 | 37.36%     | ok               |

## AAPL Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 13.24%   | 81.73%             | -21.71% |     0.35 |       68 | 52.91%     | ok               |
|          15 | 9.75%    | 81.73%             | -23.86% |     0.29 |       75 | 60.07%     | ok               |
|          30 | 5.03%    | 81.73%             | -20.65% |     0.21 |       61 | 48.75%     | ok               |
|          25 | 2.84%    | 81.73%             | -20.03% |     0.16 |       67 | 50.58%     | ok               |
|          35 | 2.67%    | 81.73%             | -22.04% |     0.16 |       61 | 47.25%     | ok               |

## AAVE-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 11.46%   | -51.05%            | -43.61% |     0.33 |       40 | 30.65%     | ok               |
|          45 | -2.33%   | -51.05%            | -49.19% |     0.16 |       42 | 26.05%     | ok               |
|          35 | -7.60%   | -51.05%            | -51.96% |     0.12 |       50 | 33.91%     | ok               |
|          50 | -25.64%  | -51.05%            | -45.07% |    -0.24 |       40 | 19.16%     | ok               |
|          15 | -46.46%  | -51.05%            | -61.76% |    -0.29 |       79 | 52.30%     | ok               |

## ABBV Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -11.04%  | 36.88%             | -26.55% |    -0.21 |       50 | 34.61%     | ok               |
|          25 | -22.35%  | 36.88%             | -30.41% |    -0.48 |       67 | 48.09%     | ok               |
|          30 | -22.25%  | 36.88%             | -30.52% |    -0.48 |       68 | 46.26%     | ok               |
|          20 | -22.94%  | 36.88%             | -29.72% |    -0.48 |       67 | 49.92%     | ok               |
|          40 | -21.38%  | 36.88%             | -26.61% |    -0.5  |       66 | 39.10%     | ok               |

## ADA-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 9.81%    | -77.83%            | -33.96% |     0.3  |       54 | 27.20%     | ok               |
|          45 | 3.26%    | -77.83%            | -38.21% |     0.24 |       57 | 31.61%     | ok               |
|          35 | -8.89%   | -77.83%            | -48.54% |     0.12 |       71 | 42.15%     | ok               |
|          40 | -9.65%   | -77.83%            | -47.45% |     0.1  |       69 | 37.16%     | ok               |
|          30 | -12.69%  | -77.83%            | -45.19% |     0.07 |       83 | 45.79%     | ok               |

## ADBE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 5.44%    | -54.79%            | -21.57% |     0.21 |       74 | 49.08%     | ok               |
|          40 | -11.30%  | -54.79%            | -27.85% |    -0.09 |       70 | 41.76%     | ok               |
|          25 | -16.94%  | -54.79%            | -28.72% |    -0.11 |       50 | 61.06%     | ok               |
|          20 | -25.27%  | -54.79%            | -31.52% |    -0.24 |       54 | 64.06%     | ok               |
|          30 | -27.71%  | -54.79%            | -31.30% |    -0.31 |       68 | 57.24%     | ok               |

## AGG Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -5.29%   | -0.02%             | -7.92%  |    -1.16 |       52 | 18.30%     | ok               |
|          20 | -8.09%   | -0.02%             | -11.49% |    -1.17 |       71 | 39.10%     | ok               |
|          30 | -7.37%   | -0.02%             | -10.95% |    -1.18 |       69 | 33.78%     | ok               |
|          25 | -8.27%   | -0.02%             | -12.13% |    -1.24 |       71 | 37.44%     | ok               |
|          45 | -7.10%   | -0.02%             | -9.08%  |    -1.35 |       60 | 22.96%     | ok               |

## ALGO-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -28.14%  | -63.20%            | -41.20% |    -0.19 |       80 | 36.59%     | ok               |
|          35 | -35.82%  | -63.20%            | -43.45% |    -0.41 |       58 | 30.08%     | ok               |
|          25 | -45.94%  | -63.20%            | -60.86% |    -0.46 |       80 | 43.30%     | ok               |
|          15 | -48.88%  | -63.20%            | -54.77% |    -0.47 |       82 | 48.85%     | ok               |
|          20 | -51.12%  | -63.20%            | -56.96% |    -0.54 |       82 | 46.36%     | ok               |

## AMAT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -24.80%  | 166.37%            | -54.01% |    -0.12 |       70 | 58.90%     | ok               |
|          30 | -35.59%  | 166.37%            | -57.08% |    -0.34 |       71 | 49.92%     | ok               |
|          35 | -35.32%  | 166.37%            | -54.63% |    -0.35 |       71 | 47.42%     | ok               |
|          50 | -34.21%  | 166.37%            | -48.13% |    -0.37 |       48 | 35.44%     | ok               |
|          40 | -38.96%  | 166.37%            | -55.84% |    -0.43 |       67 | 42.60%     | ok               |

## AMD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 7.59%    | 147.47%            | -41.75% |     0.28 |       54 | 35.11%     | ok               |
|          50 | 7.89%    | 147.47%            | -41.14% |     0.28 |       58 | 29.78%     | ok               |
|          35 | 0.27%    | 147.47%            | -46.50% |     0.21 |       62 | 36.77%     | ok               |
|          30 | -9.72%   | 147.47%            | -51.00% |     0.12 |       67 | 39.27%     | ok               |
|          25 | -14.36%  | 147.47%            | -55.79% |     0.07 |       67 | 41.76%     | ok               |

## AMGN Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | -1.29%   | 47.77%             | -31.29% |     0.06 |       67 | 43.93%     | ok               |
|          20 | -3.15%   | 47.77%             | -26.65% |     0.03 |       72 | 53.74%     | ok               |
|          15 | -5.92%   | 47.77%             | -27.98% |    -0.02 |       67 | 58.40%     | ok               |
|          30 | -7.14%   | 47.77%             | -34.19% |    -0.07 |       73 | 47.75%     | ok               |
|          25 | -9.69%   | 47.77%             | -33.47% |    -0.12 |       67 | 50.08%     | ok               |

## AMZN Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -23.16%  | 54.42%             | -28.96% |    -0.68 |       56 | 29.95%     | ok               |
|          50 | -26.04%  | 54.42%             | -34.08% |    -0.91 |       50 | 23.13%     | ok               |
|          45 | -33.28%  | 54.42%             | -35.71% |    -1.17 |       58 | 26.46%     | ok               |
|          35 | -48.12%  | 54.42%             | -49.36% |    -1.38 |       71 | 33.94%     | ok               |
|          30 | -53.49%  | 54.42%             | -54.61% |    -1.51 |       81 | 39.93%     | ok               |

## APT-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 19.10%   | -89.66%            | -46.73% |     0.42 |       40 | 18.97%     | ok               |
|          45 | -11.65%  | -89.66%            | -63.86% |     0.05 |       56 | 24.52%     | ok               |
|          35 | -17.11%  | -89.66%            | -60.63% |     0.04 |       66 | 35.25%     | ok               |
|          20 | -24.12%  | -89.66%            | -68.18% |     0.01 |       71 | 50.19%     | ok               |
|          25 | -28.42%  | -89.66%            | -68.00% |    -0.05 |       68 | 45.79%     | ok               |

## ARB-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 36.57%   | -79.61%            | -51.09% |     0.54 |       86 | 58.05%     | ok               |
|          20 | 4.98%    | -79.61%            | -58.28% |     0.32 |       72 | 51.92%     | ok               |
|          25 | -11.86%  | -79.61%            | -55.53% |     0.16 |       74 | 47.70%     | ok               |
|          40 | -10.08%  | -79.61%            | -48.16% |     0.11 |       60 | 31.42%     | ok               |
|          45 | -10.55%  | -79.61%            | -51.09% |     0.08 |       62 | 24.33%     | ok               |

## ARKK Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -31.75%  | 51.27%             | -37.76% |    -0.42 |       96 | 52.75%     | ok               |
|          20 | -35.78%  | 51.27%             | -37.99% |    -0.54 |       91 | 48.09%     | ok               |
|          30 | -37.14%  | 51.27%             | -38.58% |    -0.66 |       89 | 41.10%     | ok               |
|          35 | -39.25%  | 51.27%             | -40.65% |    -0.76 |       88 | 38.44%     | ok               |
|          40 | -40.53%  | 51.27%             | -41.90% |    -0.84 |       80 | 33.61%     | ok               |

## ATOM-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -59.56%  | -68.33%            | -69.46% |    -0.72 |       83 | 62.84%     | ok               |
|          25 | -64.24%  | -68.33%            | -71.09% |    -0.93 |       93 | 53.45%     | ok               |
|          20 | -67.87%  | -68.33%            | -74.75% |    -1.01 |       93 | 56.70%     | ok               |
|          30 | -67.57%  | -68.33%            | -73.98% |    -1.11 |       88 | 46.74%     | ok               |
|          45 | -61.27%  | -68.33%            | -67.66% |    -1.12 |       74 | 31.61%     | ok               |

## AVAX-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -5.68%   | -68.29%            | -40.19% |     0.08 |       34 | 18.39%     | ok               |
|          40 | -14.36%  | -68.29%            | -47.33% |    -0.05 |       38 | 24.90%     | ok               |
|          45 | -17.71%  | -68.29%            | -47.25% |    -0.12 |       34 | 22.22%     | ok               |
|          15 | -32.68%  | -68.29%            | -43.71% |    -0.15 |       75 | 52.49%     | ok               |
|          35 | -27.85%  | -68.29%            | -48.89% |    -0.22 |       56 | 30.27%     | ok               |

## AVGO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 27.80%   | 232.53%            | -35.76% |     0.47 |       60 | 40.60%     | ok               |
|          25 | 25.11%   | 232.53%            | -38.01% |     0.44 |       68 | 42.10%     | ok               |
|          50 | 24.25%   | 232.53%            | -36.86% |     0.44 |       52 | 29.45%     | ok               |
|          40 | 24.20%   | 232.53%            | -40.70% |     0.44 |       58 | 34.28%     | ok               |
|          35 | 19.66%   | 232.53%            | -36.19% |     0.39 |       68 | 37.60%     | ok               |

## BA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 24.75%   | 31.72%             | -13.34% |     0.65 |       42 | 31.28%     | ok               |
|          35 | 20.62%   | 31.72%             | -23.77% |     0.46 |       70 | 43.93%     | ok               |
|          40 | 14.00%   | 31.72%             | -23.90% |     0.37 |       46 | 38.27%     | ok               |
|          25 | 0.91%    | 31.72%             | -32.48% |     0.14 |       70 | 51.41%     | ok               |
|          30 | -1.82%   | 31.72%             | -30.56% |     0.1  |       67 | 48.09%     | ok               |

## BAC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 0.06%    | 75.30%             | -21.48% |     0.09 |       80 | 55.74%     | ok               |
|          35 | -1.14%   | 75.30%             | -29.13% |     0.04 |       70 | 47.25%     | ok               |
|          45 | -0.84%   | 75.30%             | -22.29% |     0.04 |       64 | 38.60%     | ok               |
|          15 | -5.57%   | 75.30%             | -23.70% |    -0.04 |       80 | 60.73%     | ok               |
|          25 | -4.87%   | 75.30%             | -27.14% |    -0.04 |       80 | 53.74%     | ok               |

## BCH-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 6.93%    | -33.48%            | -47.24% |     0.31 |       72 | 59.96%     | ok               |
|          30 | 5.55%    | -33.48%            | -54.26% |     0.27 |       76 | 50.57%     | ok               |
|          20 | -3.32%   | -33.48%            | -50.86% |     0.21 |       68 | 56.51%     | ok               |
|          25 | -17.71%  | -33.48%            | -57.98% |     0.03 |       71 | 53.07%     | ok               |
|          35 | -17.01%  | -33.48%            | -64.58% |    -0.01 |       72 | 46.74%     | ok               |

## BITO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -13.37%  | -73.94%            | -31.98% |    -0.08 |       52 | 22.30%     | ok               |
|          30 | -27.89%  | -73.94%            | -39.47% |    -0.23 |       80 | 39.10%     | ok               |
|          15 | -33.21%  | -73.94%            | -48.38% |    -0.24 |       89 | 48.09%     | ok               |
|          45 | -27.12%  | -73.94%            | -38.53% |    -0.31 |       60 | 25.96%     | ok               |
|          40 | -30.38%  | -73.94%            | -41.15% |    -0.33 |       64 | 30.78%     | ok               |

## BLK Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 1.77%    | 37.24%             | -21.48% |     0.13 |       80 | 49.42%     | ok               |
|          35 | 0.48%    | 37.24%             | -20.79% |     0.08 |       86 | 40.93%     | ok               |
|          40 | -1.43%   | 37.24%             | -22.83% |     0.02 |       78 | 36.61%     | ok               |
|          25 | -3.32%   | 37.24%             | -24.62% |    -0.01 |       75 | 47.42%     | ok               |
|          30 | -5.83%   | 37.24%             | -26.90% |    -0.09 |       79 | 44.76%     | ok               |

## BND Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -6.72%   | -0.04%             | -9.66%  |    -0.96 |       65 | 40.60%     | ok               |
|          25 | -7.37%   | -0.04%             | -10.73% |    -1.1  |       67 | 38.60%     | ok               |
|          30 | -7.48%   | -0.04%             | -10.16% |    -1.18 |       67 | 35.27%     | ok               |
|          15 | -8.98%   | -0.04%             | -11.52% |    -1.28 |       77 | 43.43%     | ok               |
|          45 | -7.99%   | -0.04%             | -9.84%  |    -1.51 |       56 | 24.29%     | ok               |

## BONK-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 165.22%  | -76.50%            | -35.57% |     1.21 |       48 | 22.41%     | ok               |
|          25 | 140.14%  | -76.50%            | -54.47% |     0.96 |       65 | 48.47%     | ok               |
|          15 | 128.37%  | -76.50%            | -62.48% |     0.9  |       70 | 57.09%     | ok               |
|          45 | 92.16%   | -76.50%            | -47.53% |     0.87 |       62 | 27.59%     | ok               |
|          20 | 109.90%  | -76.50%            | -61.03% |     0.86 |       65 | 52.68%     | ok               |

## BTC-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 64.79%   | -25.18%            | -14.50% |     1.12 |       42 | 33.52%     | ok               |
|          45 | 49.87%   | -25.18%            | -13.36% |     0.94 |       40 | 30.08%     | ok               |
|          35 | 42.81%   | -25.18%            | -21.56% |     0.79 |       66 | 40.61%     | ok               |
|          30 | 25.66%   | -25.18%            | -21.75% |     0.53 |       70 | 47.32%     | ok               |
|          50 | 17.90%   | -25.18%            | -18.05% |     0.47 |       40 | 25.10%     | ok               |

## C Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -5.79%   | 138.30%            | -21.64% |    -0.08 |       66 | 35.27%     | ok               |
|          45 | -18.13%  | 138.30%            | -29.73% |    -0.42 |       78 | 39.43%     | ok               |
|          25 | -27.26%  | 138.30%            | -34.97% |    -0.51 |       73 | 52.25%     | ok               |
|          40 | -23.87%  | 138.30%            | -34.65% |    -0.55 |       78 | 41.76%     | ok               |
|          20 | -29.70%  | 138.30%            | -36.33% |    -0.56 |       81 | 55.24%     | ok               |

## CAT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 15.52%   | 155.06%            | -21.02% |     0.36 |       72 | 53.58%     | ok               |
|          25 | 15.62%   | 155.06%            | -26.37% |     0.36 |       68 | 56.41%     | ok               |
|          45 | 10.80%   | 155.06%            | -27.12% |     0.3  |       56 | 42.26%     | ok               |
|          20 | 10.32%   | 155.06%            | -25.65% |     0.29 |       80 | 60.07%     | ok               |
|          15 | 10.01%   | 155.06%            | -30.60% |     0.28 |       75 | 67.22%     | ok               |

## CL Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 4.50%    | 4.57%              | -12.98% |     0.23 |       44 | 27.62%     | ok               |
|          30 | 4.04%    | 4.57%              | -14.32% |     0.19 |       62 | 43.59%     | ok               |
|          45 | -0.28%   | 4.57%              | -13.51% |     0.04 |       48 | 30.62%     | ok               |
|          35 | -0.91%   | 4.57%              | -13.83% |     0.03 |       64 | 39.93%     | ok               |
|          40 | -3.78%   | 4.57%              | -12.70% |    -0.09 |       58 | 34.61%     | ok               |

## CMCSA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -42.11%  | -38.98%            | -45.19% |    -0.97 |       89 | 56.24%     | ok               |
|          30 | -45.05%  | -38.98%            | -48.04% |    -1.21 |       80 | 41.76%     | ok               |
|          50 | -30.72%  | -38.98%            | -32.82% |    -1.22 |       48 | 13.64%     | ok               |
|          25 | -46.75%  | -38.98%            | -49.58% |    -1.26 |       87 | 46.92%     | ok               |
|          35 | -45.20%  | -38.98%            | -47.87% |    -1.31 |       93 | 36.11%     | ok               |

## COMP-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -6.30%   | -64.96%            | -38.71% |     0.11 |       48 | 20.88%     | ok               |
|          30 | -41.75%  | -64.96%            | -55.27% |    -0.29 |       95 | 46.74%     | ok               |
|          25 | -45.07%  | -64.96%            | -58.90% |    -0.31 |       95 | 54.41%     | ok               |
|          15 | -54.85%  | -64.96%            | -64.08% |    -0.46 |      105 | 64.94%     | ok               |
|          40 | -46.76%  | -64.96%            | -51.97% |    -0.48 |       72 | 34.48%     | ok               |

## COP Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -5.09%   | -2.14%             | -35.08% |    -0.02 |       48 | 29.95%     | ok               |
|          35 | -17.82%  | -2.14%             | -43.58% |    -0.28 |       73 | 40.60%     | ok               |
|          45 | -16.30%  | -2.14%             | -41.35% |    -0.29 |       62 | 33.28%     | ok               |
|          30 | -22.09%  | -2.14%             | -43.96% |    -0.37 |       72 | 44.09%     | ok               |
|          40 | -21.59%  | -2.14%             | -47.05% |    -0.42 |       68 | 36.44%     | ok               |

## COST Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 12.36%   | 28.30%             | -24.32% |     0.42 |       64 | 47.75%     | ok               |
|          25 | 10.70%   | 28.30%             | -24.73% |     0.38 |       61 | 44.93%     | ok               |
|          35 | 6.54%    | 28.30%             | -26.58% |     0.28 |       52 | 38.60%     | ok               |
|          30 | 2.10%    | 28.30%             | -29.73% |     0.13 |       56 | 41.43%     | ok               |
|          15 | -2.31%   | 28.30%             | -27.30% |     0.01 |       67 | 51.25%     | ok               |

## CRM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -36.98%  | -36.66%            | -44.67% |    -0.59 |       90 | 55.24%     | ok               |
|          35 | -31.01%  | -36.66%            | -34.39% |    -0.63 |       60 | 37.77%     | ok               |
|          40 | -36.11%  | -36.66%            | -40.30% |    -0.84 |       66 | 33.78%     | ok               |
|          20 | -44.40%  | -36.66%            | -46.70% |    -0.85 |       74 | 48.92%     | ok               |
|          30 | -40.74%  | -36.66%            | -42.51% |    -0.87 |       63 | 42.60%     | ok               |

## CRV-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 27.72%   | -50.46%            | -37.78% |     0.48 |       70 | 31.80%     | ok               |
|          45 | 12.07%   | -50.46%            | -42.29% |     0.33 |       56 | 21.07%     | ok               |
|          50 | 7.86%    | -50.46%            | -29.30% |     0.28 |       46 | 17.43%     | ok               |
|          40 | 5.82%    | -50.46%            | -38.86% |     0.27 |       60 | 27.39%     | ok               |
|          30 | -0.17%   | -50.46%            | -39.89% |     0.23 |       70 | 36.59%     | ok               |

## CSCO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 35.16%   | 142.47%            | -19.34% |     0.75 |       48 | 36.61%     | ok               |
|          45 | 30.59%   | 142.47%            | -19.34% |     0.66 |       49 | 38.27%     | ok               |
|          35 | 25.61%   | 142.47%            | -23.68% |     0.55 |       51 | 45.09%     | ok               |
|          25 | 24.55%   | 142.47%            | -23.28% |     0.53 |       61 | 49.58%     | ok               |
|          30 | 23.34%   | 142.47%            | -21.79% |     0.51 |       59 | 47.75%     | ok               |

## CVX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -7.62%   | 21.13%             | -27.34% |    -0.16 |       73 | 35.77%     | ok               |
|          25 | -9.35%   | 21.13%             | -24.33% |    -0.17 |       71 | 43.09%     | ok               |
|          45 | -8.49%   | 21.13%             | -28.83% |    -0.19 |       63 | 32.28%     | ok               |
|          35 | -9.76%   | 21.13%             | -28.85% |    -0.2  |       65 | 37.94%     | ok               |
|          30 | -13.00%  | 21.13%             | -29.13% |    -0.3  |       71 | 40.43%     | ok               |

## DASH-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 100.56%  | 27.55%             | -27.84% |     0.85 |       40 | 16.09%     | ok               |
|          40 | 60.92%   | 27.55%             | -31.16% |     0.65 |       46 | 22.80%     | ok               |
|          45 | 44.60%   | 27.55%             | -36.57% |     0.56 |       44 | 18.20%     | ok               |
|          35 | -37.83%  | 27.55%             | -63.23% |     0.02 |       69 | 27.20%     | ok               |
|          30 | -41.02%  | 27.55%             | -64.43% |    -0.01 |       63 | 30.08%     | ok               |

## DBC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -8.70%   | 25.96%             | -27.07% |    -0.23 |       74 | 41.10%     | ok               |
|          25 | -11.63%  | 25.96%             | -26.10% |    -0.35 |       64 | 37.44%     | ok               |
|          20 | -12.16%  | 25.96%             | -26.24% |    -0.37 |       67 | 39.27%     | ok               |
|          50 | -10.49%  | 25.96%             | -20.31% |    -0.38 |       44 | 23.63%     | ok               |
|          30 | -13.84%  | 25.96%             | -25.70% |    -0.45 |       62 | 35.61%     | ok               |

## DE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -4.78%   | 61.54%             | -29.90% |    -0    |       74 | 51.25%     | ok               |
|          30 | -5.05%   | 61.54%             | -24.56% |    -0.01 |       70 | 45.42%     | ok               |
|          50 | -4.08%   | 61.54%             | -22.53% |    -0.03 |       66 | 30.95%     | ok               |
|          45 | -5.12%   | 61.54%             | -25.49% |    -0.04 |       64 | 35.27%     | ok               |
|          25 | -8.40%   | 61.54%             | -28.64% |    -0.08 |       76 | 48.25%     | ok               |

## DIA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -2.43%   | 38.75%             | -11.28% |    -0.09 |       60 | 44.76%     | ok               |
|          35 | -2.88%   | 38.75%             | -13.15% |    -0.12 |       62 | 41.60%     | ok               |
|          30 | -3.93%   | 38.75%             | -12.94% |    -0.18 |       60 | 43.59%     | ok               |
|          20 | -5.84%   | 38.75%             | -13.85% |    -0.27 |       66 | 47.25%     | ok               |
|          40 | -6.84%   | 38.75%             | -15.06% |    -0.37 |       68 | 38.77%     | ok               |

## DIS Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 15.28%   | -9.55%             | -16.40% |     0.5  |       48 | 25.79%     | ok               |
|          40 | -10.63%  | -9.55%             | -24.07% |    -0.16 |       63 | 34.44%     | ok               |
|          45 | -10.39%  | -9.55%             | -18.50% |    -0.18 |       49 | 29.62%     | ok               |
|          15 | -19.15%  | -9.55%             | -32.73% |    -0.3  |       91 | 55.07%     | ok               |
|          35 | -17.52%  | -9.55%             | -25.70% |    -0.32 |       75 | 40.60%     | ok               |

## DOGE-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 8.86%    | -64.98%            | -59.36% |     0.35 |       76 | 64.18%     | ok               |
|          25 | 4.95%    | -64.98%            | -55.33% |     0.31 |       67 | 54.21%     | ok               |
|          20 | 1.52%    | -64.98%            | -57.37% |     0.28 |       79 | 59.39%     | ok               |
|          30 | -12.19%  | -64.98%            | -62.31% |     0.13 |       70 | 48.66%     | ok               |
|          35 | -38.20%  | -64.98%            | -61.79% |    -0.28 |       66 | 42.34%     | ok               |

## DOT-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -37.25%  | -81.20%            | -48.63% |    -0.5  |       58 | 26.25%     | ok               |
|          45 | -39.99%  | -81.20%            | -51.81% |    -0.5  |       50 | 31.42%     | ok               |
|          35 | -57.95%  | -81.20%            | -63.08% |    -0.63 |       78 | 41.57%     | ok               |
|          15 | -67.15%  | -81.20%            | -73.29% |    -0.66 |       83 | 63.22%     | ok               |
|          40 | -50.09%  | -81.20%            | -56.98% |    -0.68 |       56 | 34.29%     | ok               |

## DXY-INDEX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -1.69%   | -2.23%             | -6.29%  |    -0.25 |       42 | 32.68%     | ok               |
|          15 | -2.97%   | -2.23%             | -11.37% |    -0.25 |       80 | 76.19%     | ok               |
|          40 | -4.66%   | -2.23%             | -8.24%  |    -0.59 |       68 | 50.43%     | ok               |
|          25 | -6.28%   | -2.23%             | -12.10% |    -0.68 |       78 | 66.45%     | ok               |
|          35 | -5.86%   | -2.23%             | -10.39% |    -0.72 |       71 | 56.49%     | ok               |

## EEM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -5.91%   | 59.40%             | -15.88% |    -0.16 |       52 | 33.61%     | ok               |
|          45 | -7.56%   | 59.40%             | -17.36% |    -0.22 |       54 | 35.11%     | ok               |
|          40 | -7.90%   | 59.40%             | -19.52% |    -0.22 |       66 | 37.27%     | ok               |
|          35 | -8.54%   | 59.40%             | -23.88% |    -0.22 |       68 | 39.27%     | ok               |
|          30 | -12.19%  | 59.40%             | -25.67% |    -0.35 |       66 | 40.93%     | ok               |

## EFA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -6.00%   | 35.23%             | -11.24% |    -0.16 |       64 | 49.92%     | ok               |
|          30 | -10.33%  | 35.23%             | -13.53% |    -0.4  |       58 | 41.60%     | ok               |
|          20 | -12.47%  | 35.23%             | -13.10% |    -0.46 |       69 | 46.92%     | ok               |
|          40 | -12.03%  | 35.23%             | -15.73% |    -0.51 |       62 | 37.94%     | ok               |
|          25 | -13.56%  | 35.23%             | -15.78% |    -0.53 |       64 | 44.26%     | ok               |

## EOG Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -25.28%  | 9.51%              | -48.13% |    -0.5  |       81 | 49.42%     | ok               |
|          35 | -26.11%  | 9.51%              | -46.26% |    -0.56 |       79 | 44.09%     | ok               |
|          40 | -25.38%  | 9.51%              | -43.26% |    -0.56 |       66 | 38.94%     | ok               |
|          25 | -29.08%  | 9.51%              | -51.99% |    -0.58 |       82 | 52.41%     | ok               |
|          45 | -25.26%  | 9.51%              | -43.17% |    -0.59 |       60 | 35.44%     | ok               |

## ETC-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -2.84%   | -65.28%            | -31.28% |     0.08 |       26 | 15.90%     | ok               |
|          45 | -12.62%  | -65.28%            | -38.47% |    -0.1  |       26 | 17.62%     | ok               |
|          35 | -15.58%  | -65.28%            | -45.32% |    -0.12 |       44 | 25.29%     | ok               |
|          40 | -19.39%  | -65.28%            | -43.28% |    -0.23 |       40 | 21.26%     | ok               |
|          30 | -31.66%  | -65.28%            | -48.09% |    -0.43 |       62 | 28.93%     | ok               |

## ETH-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 177.27%  | -11.79%            | -30.11% |     1.38 |       60 | 45.79%     | ok               |
|          30 | 125.49%  | -11.79%            | -32.89% |     1.1  |       66 | 54.41%     | ok               |
|          25 | 75.35%   | -11.79%            | -40.90% |     0.82 |       62 | 59.20%     | ok               |
|          20 | 75.63%   | -11.79%            | -39.10% |     0.81 |       80 | 63.60%     | ok               |
|          15 | 67.40%   | -11.79%            | -42.74% |     0.75 |       75 | 69.16%     | ok               |

## EWJ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -20.02%  | 37.18%             | -30.73% |    -0.68 |       62 | 36.61%     | ok               |
|          20 | -21.38%  | 37.18%             | -31.32% |    -0.71 |       58 | 38.60%     | ok               |
|          25 | -23.65%  | 37.18%             | -31.18% |    -0.81 |       58 | 37.60%     | ok               |
|          45 | -20.79%  | 37.18%             | -27.68% |    -0.83 |       58 | 28.79%     | ok               |
|          35 | -23.86%  | 37.18%             | -32.54% |    -0.85 |       68 | 34.94%     | ok               |

## FCX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -6.01%   | 59.85%             | -27.70% |     0.03 |       56 | 30.45%     | ok               |
|          45 | -10.07%  | 59.85%             | -35.18% |    -0.03 |       56 | 34.94%     | ok               |
|          40 | -21.91%  | 59.85%             | -44.37% |    -0.23 |       68 | 39.10%     | ok               |
|          30 | -29.92%  | 59.85%             | -48.22% |    -0.35 |       67 | 45.92%     | ok               |
|          35 | -34.24%  | 59.85%             | -51.41% |    -0.46 |       73 | 44.09%     | ok               |

## FET-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -18.53%  | -77.15%            | -62.04% |     0.13 |       92 | 52.68%     | ok               |
|          15 | -28.34%  | -77.15%            | -59.58% |     0.05 |       86 | 56.70%     | ok               |
|          25 | -30.86%  | -77.15%            | -60.96% |    -0.02 |       87 | 46.36%     | ok               |
|          30 | -40.91%  | -77.15%            | -52.44% |    -0.19 |       85 | 41.38%     | ok               |
|          45 | -35.13%  | -77.15%            | -48.61% |    -0.37 |       52 | 18.39%     | ok               |

## FIL-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -21.24%  | -76.81%            | -34.38% |    -0.16 |       44 | 23.37%     | ok               |
|          35 | -38.50%  | -76.81%            | -41.43% |    -0.45 |       56 | 27.97%     | ok               |
|          30 | -44.63%  | -76.81%            | -48.59% |    -0.54 |       68 | 34.10%     | ok               |
|          45 | -38.83%  | -76.81%            | -41.74% |    -0.58 |       42 | 17.82%     | ok               |
|          15 | -58.77%  | -76.81%            | -61.48% |    -0.68 |       89 | 45.79%     | ok               |

## FXI Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -1.55%   | 46.43%             | -22.57% |     0.05 |       46 | 32.45%     | ok               |
|          30 | -1.83%   | 46.43%             | -23.91% |     0.04 |       44 | 30.95%     | ok               |
|          15 | -3.13%   | 46.43%             | -21.68% |     0.02 |       50 | 36.11%     | ok               |
|          20 | -3.71%   | 46.43%             | -24.53% |    -0    |       48 | 33.94%     | ok               |
|          35 | -6.22%   | 46.43%             | -27.53% |    -0.08 |       44 | 28.95%     | ok               |

## GDX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 11.20%   | 176.26%            | -35.59% |     0.3  |       72 | 50.92%     | ok               |
|          30 | 6.19%    | 176.26%            | -34.99% |     0.23 |       58 | 46.59%     | ok               |
|          40 | 4.27%    | 176.26%            | -31.87% |     0.2  |       64 | 41.26%     | ok               |
|          35 | 3.97%    | 176.26%            | -32.37% |     0.19 |       66 | 43.76%     | ok               |
|          25 | 0.56%    | 176.26%            | -38.90% |     0.14 |       62 | 47.75%     | ok               |

## GDXJ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -14.08%  | 196.94%            | -45.05% |    -0.03 |       66 | 50.75%     | ok               |
|          50 | -21.93%  | 196.94%            | -44.94% |    -0.26 |       58 | 37.10%     | ok               |
|          30 | -25.64%  | 196.94%            | -44.93% |    -0.27 |       64 | 44.76%     | ok               |
|          25 | -30.61%  | 196.94%            | -47.26% |    -0.33 |       69 | 47.59%     | ok               |
|          35 | -29.15%  | 196.94%            | -43.49% |    -0.35 |       66 | 42.43%     | ok               |

## GE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 19.79%   | 180.72%            | -22.29% |     0.46 |       68 | 37.77%     | ok               |
|          45 | 10.75%   | 180.72%            | -25.68% |     0.3  |       76 | 40.60%     | ok               |
|          20 | 4.18%    | 180.72%            | -26.63% |     0.2  |       75 | 55.41%     | ok               |
|          30 | 2.45%    | 180.72%            | -27.82% |     0.17 |       80 | 51.41%     | ok               |
|          35 | 0.22%    | 180.72%            | -27.11% |     0.13 |       84 | 46.09%     | ok               |

## GLD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 28.81%   | 93.67%             | -14.61% |     0.7  |       48 | 49.92%     | ok               |
|          25 | 28.14%   | 93.67%             | -14.61% |     0.69 |       48 | 48.42%     | ok               |
|          30 | 22.04%   | 93.67%             | -16.63% |     0.57 |       50 | 47.25%     | ok               |
|          15 | 20.92%   | 93.67%             | -17.54% |     0.53 |       50 | 54.08%     | ok               |
|          35 | 15.69%   | 93.67%             | -17.29% |     0.45 |       54 | 45.26%     | ok               |

## GOOGL Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 83.32%   | 159.27%            | -18.25% |     1.25 |       57 | 48.75%     | ok               |
|          30 | 78.89%   | 159.27%            | -20.41% |     1.18 |       55 | 52.25%     | ok               |
|          45 | 67.79%   | 159.27%            | -14.13% |     1.15 |       52 | 42.10%     | ok               |
|          25 | 76.17%   | 159.27%            | -19.76% |     1.14 |       53 | 54.24%     | ok               |
|          50 | 60.60%   | 159.27%            | -14.89% |     1.09 |       48 | 37.27%     | ok               |

## GRT-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 23.61%   | -86.70%            | -49.67% |     0.46 |       69 | 61.88%     | ok               |
|          20 | 13.89%   | -86.70%            | -46.47% |     0.37 |       75 | 56.90%     | ok               |
|          50 | 14.84%   | -86.70%            | -36.42% |     0.37 |       44 | 21.65%     | ok               |
|          45 | 11.83%   | -86.70%            | -41.83% |     0.33 |       50 | 26.63%     | ok               |
|          30 | 7.37%    | -86.70%            | -50.20% |     0.3  |       81 | 43.87%     | ok               |

## GS Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 21.38%   | 170.29%            | -20.56% |     0.47 |       74 | 59.40%     | ok               |
|          20 | 4.82%    | 170.29%            | -23.19% |     0.2  |       74 | 55.41%     | ok               |
|          40 | 0.68%    | 170.29%            | -17.88% |     0.11 |       70 | 43.93%     | ok               |
|          25 | -0.48%   | 170.29%            | -23.32% |     0.09 |       74 | 52.91%     | ok               |
|          30 | -1.59%   | 170.29%            | -22.13% |     0.07 |       74 | 50.58%     | ok               |

## HD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -7.90%   | -6.82%             | -17.69% |    -0.13 |       71 | 43.76%     | ok               |
|          25 | -8.62%   | -6.82%             | -18.51% |    -0.15 |       70 | 45.76%     | ok               |
|          45 | -11.96%  | -6.82%             | -20.74% |    -0.35 |       58 | 27.95%     | ok               |
|          40 | -13.49%  | -6.82%             | -19.63% |    -0.37 |       82 | 33.44%     | ok               |
|          15 | -17.78%  | -6.82%             | -27.26% |    -0.38 |      109 | 54.58%     | ok               |

## HON Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -10.38%  | 25.68%             | -21.17% |    -0.28 |       70 | 32.11%     | ok               |
|          45 | -12.17%  | 25.68%             | -19.99% |    -0.32 |       72 | 37.10%     | ok               |
|          40 | -21.11%  | 25.68%             | -26.92% |    -0.57 |       76 | 41.26%     | ok               |
|          35 | -22.62%  | 25.68%             | -27.99% |    -0.6  |       91 | 47.59%     | ok               |
|          30 | -25.74%  | 25.68%             | -29.81% |    -0.68 |       95 | 52.41%     | ok               |

## HYG Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -8.33%   | 2.62%              | -8.33%  |    -1.01 |       70 | 29.78%     | ok               |
|          15 | -9.82%   | 2.62%              | -10.69% |    -1.06 |       90 | 41.60%     | ok               |
|          20 | -9.56%   | 2.62%              | -10.67% |    -1.07 |       86 | 39.27%     | ok               |
|          25 | -9.78%   | 2.62%              | -10.52% |    -1.1  |       85 | 37.27%     | ok               |
|          30 | -9.49%   | 2.62%              | -10.00% |    -1.11 |       83 | 34.61%     | ok               |

## IBIT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 53.73%   | -3.34%             | -17.37% |     1.05 |       22 | 21.62%     | ok               |
|          15 | 56.91%   | -3.34%             | -19.20% |     0.94 |       40 | 38.51%     | ok               |
|          45 | 44.27%   | -3.34%             | -17.37% |     0.89 |       26 | 22.97%     | ok               |
|          40 | 38.04%   | -3.34%             | -17.78% |     0.79 |       26 | 24.77%     | ok               |
|          30 | 30.82%   | -3.34%             | -18.95% |     0.65 |       34 | 31.08%     | ok               |

## IBM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -21.31%  | 19.94%             | -47.64% |    -0.18 |       91 | 63.23%     | ok               |
|          35 | -25.62%  | 19.94%             | -47.10% |    -0.32 |       69 | 46.76%     | ok               |
|          30 | -28.39%  | 19.94%             | -48.94% |    -0.37 |       75 | 51.08%     | ok               |
|          20 | -31.54%  | 19.94%             | -51.95% |    -0.39 |       73 | 55.74%     | ok               |
|          50 | -30.29%  | 19.94%             | -45.88% |    -0.46 |       50 | 34.44%     | ok               |

## ICP-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -10.52%  | -65.98%            | -50.29% |     0.15 |       77 | 34.67%     | ok               |
|          35 | -5.52%   | -65.98%            | -41.66% |     0.14 |       60 | 28.93%     | ok               |
|          40 | -8.14%   | -65.98%            | -34.69% |     0.1  |       52 | 24.14%     | ok               |
|          15 | -46.31%  | -65.98%            | -59.86% |    -0.18 |       77 | 47.13%     | ok               |
|          20 | -45.26%  | -65.98%            | -58.96% |    -0.19 |       84 | 44.25%     | ok               |

## IEF Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -7.14%   | -1.27%             | -10.32% |    -0.84 |       72 | 43.09%     | ok               |
|          15 | -7.69%   | -1.27%             | -11.04% |    -0.9  |       71 | 44.59%     | ok               |
|          45 | -8.16%   | -1.27%             | -9.85%  |    -1.33 |       56 | 23.29%     | ok               |
|          25 | -10.71%  | -1.27%             | -11.84% |    -1.35 |       78 | 40.27%     | ok               |
|          40 | -8.76%   | -1.27%             | -9.92%  |    -1.36 |       66 | 25.46%     | ok               |

## IEMG Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -3.84%   | 54.60%             | -13.91% |    -0.1  |       54 | 31.45%     | ok               |
|          45 | -4.63%   | 54.60%             | -14.92% |    -0.12 |       50 | 33.94%     | ok               |
|          35 | -5.48%   | 54.60%             | -22.13% |    -0.13 |       65 | 39.43%     | ok               |
|          40 | -6.10%   | 54.60%             | -18.43% |    -0.17 |       62 | 36.94%     | ok               |
|          25 | -9.65%   | 54.60%             | -25.58% |    -0.27 |       61 | 42.26%     | ok               |

## INJ-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -10.15%  | -60.34%            | -52.34% |     0.06 |       44 | 23.37%     | ok               |
|          35 | -21.17%  | -60.34%            | -59.17% |    -0.02 |       60 | 32.57%     | ok               |
|          40 | -26.45%  | -60.34%            | -55.86% |    -0.14 |       50 | 29.12%     | ok               |
|          50 | -22.38%  | -60.34%            | -49.35% |    -0.14 |       48 | 20.11%     | ok               |
|          20 | -55.65%  | -60.34%            | -81.16% |    -0.45 |       78 | 46.74%     | ok               |

## INTC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 81.91%   | 133.77%            | -49.32% |     0.78 |       54 | 33.61%     | ok               |
|          15 | 82.71%   | 133.77%            | -53.65% |     0.73 |       78 | 60.23%     | ok               |
|          40 | 75.94%   | 133.77%            | -55.86% |     0.73 |       62 | 37.94%     | ok               |
|          50 | 69.07%   | 133.77%            | -48.35% |     0.71 |       62 | 29.78%     | ok               |
|          25 | 64.40%   | 133.77%            | -56.41% |     0.66 |       77 | 51.08%     | ok               |

## INTU Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 1.32%    | -49.94%            | -39.78% |     0.14 |       69 | 28.12%     | ok               |
|          45 | 0.69%    | -49.94%            | -40.02% |     0.13 |       67 | 31.95%     | ok               |
|          40 | -7.39%   | -49.94%            | -44.40% |    -0.01 |       67 | 34.78%     | ok               |
|          35 | -14.47%  | -49.94%            | -46.02% |    -0.14 |       71 | 38.27%     | ok               |
|          25 | -15.29%  | -49.94%            | -39.87% |    -0.14 |       70 | 44.93%     | ok               |

## ITA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 0.72%    | 98.72%             | -21.48% |     0.09 |       76 | 36.44%     | ok               |
|          15 | -2.98%   | 98.72%             | -25.76% |     0.01 |       89 | 58.57%     | ok               |
|          30 | -2.83%   | 98.72%             | -23.75% |    -0.01 |       74 | 46.26%     | ok               |
|          35 | -4.84%   | 98.72%             | -23.16% |    -0.07 |       76 | 44.59%     | ok               |
|          40 | -5.94%   | 98.72%             | -20.58% |    -0.12 |       78 | 41.10%     | ok               |

## IWM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | 10.83%   | 45.72%             | -13.30% |     0.43 |       52 | 36.77%     | ok               |
|          40 | 9.59%    | 45.72%             | -14.08% |     0.43 |       44 | 31.28%     | ok               |
|          30 | 10.39%   | 45.72%             | -12.83% |     0.42 |       50 | 35.77%     | ok               |
|          35 | 9.33%    | 45.72%             | -14.11% |     0.4  |       50 | 33.61%     | ok               |
|          20 | 6.46%    | 45.72%             | -13.83% |     0.28 |       62 | 37.77%     | ok               |

## JNJ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 20.35%   | 59.89%             | -10.57% |     0.83 |       52 | 36.77%     | ok               |
|          15 | 16.56%   | 59.89%             | -18.02% |     0.56 |       66 | 56.91%     | ok               |
|          45 | 9.66%    | 59.89%             | -13.77% |     0.42 |       54 | 41.26%     | ok               |
|          20 | 11.18%   | 59.89%             | -17.61% |     0.42 |       72 | 53.41%     | ok               |
|          40 | 5.51%    | 59.89%             | -14.77% |     0.26 |       60 | 45.59%     | ok               |

## JPM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 9.20%    | 87.71%             | -15.90% |     0.35 |       54 | 38.44%     | ok               |
|          45 | -1.17%   | 87.71%             | -21.91% |     0.04 |       56 | 41.43%     | ok               |
|          20 | -17.16%  | 87.71%             | -33.59% |    -0.31 |       84 | 56.24%     | ok               |
|          40 | -14.74%  | 87.71%             | -28.47% |    -0.37 |       68 | 44.09%     | ok               |
|          35 | -19.77%  | 87.71%             | -27.43% |    -0.51 |       76 | 48.09%     | ok               |

## KO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 23.75%   | 42.06%             | -8.20%  |     0.85 |       51 | 37.94%     | ok               |
|          35 | 19.96%   | 42.06%             | -8.07%  |     0.75 |       54 | 36.61%     | ok               |
|          40 | 17.46%   | 42.06%             | -9.28%  |     0.71 |       56 | 33.44%     | ok               |
|          25 | 18.64%   | 42.06%             | -9.73%  |     0.69 |       57 | 40.60%     | ok               |
|          50 | 10.20%   | 42.06%             | -12.31% |     0.48 |       38 | 26.96%     | ok               |

## LDO-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 65.94%   | -72.98%            | -48.17% |     0.7  |       82 | 57.66%     | ok               |
|          20 | 44.27%   | -72.98%            | -45.55% |     0.59 |       84 | 52.49%     | ok               |
|          50 | 33.03%   | -72.98%            | -48.04% |     0.57 |       52 | 18.20%     | ok               |
|          30 | 16.89%   | -72.98%            | -61.16% |     0.41 |       78 | 43.87%     | ok               |
|          35 | 16.85%   | -72.98%            | -61.98% |     0.4  |       80 | 36.78%     | ok               |

## LIN Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -8.55%   | 3.40%              | -23.70% |    -0.23 |       65 | 47.75%     | ok               |
|          25 | -8.78%   | 3.40%              | -22.01% |    -0.26 |       65 | 39.93%     | ok               |
|          20 | -10.73%  | 3.40%              | -23.00% |    -0.32 |       64 | 43.09%     | ok               |
|          30 | -12.63%  | 3.40%              | -21.38% |    -0.42 |       68 | 37.10%     | ok               |
|          35 | -12.07%  | 3.40%              | -21.03% |    -0.43 |       64 | 30.62%     | ok               |

## LINK-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 1.24%    | -43.82%            | -33.71% |     0.22 |       48 | 28.54%     | ok               |
|          30 | -2.06%   | -43.82%            | -40.80% |     0.21 |       71 | 43.68%     | ok               |
|          50 | -3.72%   | -43.82%            | -32.27% |     0.14 |       42 | 22.61%     | ok               |
|          35 | -13.06%  | -43.82%            | -40.61% |     0.08 |       59 | 38.51%     | ok               |
|          40 | -17.84%  | -43.82%            | -42.20% |    -0.01 |       55 | 32.76%     | ok               |

## LLY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 6.14%    | 54.37%             | -38.23% |     0.23 |       44 | 34.94%     | ok               |
|          15 | -2.75%   | 54.37%             | -48.12% |     0.1  |       61 | 57.90%     | ok               |
|          45 | -6.11%   | 54.37%             | -42.66% |    -0    |       50 | 38.27%     | ok               |
|          20 | -16.07%  | 54.37%             | -51.34% |    -0.14 |       68 | 53.08%     | ok               |
|          25 | -17.46%  | 54.37%             | -53.47% |    -0.18 |       64 | 50.42%     | ok               |

## LRCX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -13.68%  | 231.73%            | -48.71% |    -0.02 |       76 | 33.61%     | ok               |
|          40 | -17.02%  | 231.73%            | -55.33% |    -0.04 |       70 | 39.43%     | ok               |
|          35 | -18.62%  | 231.73%            | -58.47% |    -0.06 |       78 | 41.60%     | ok               |
|          30 | -23.96%  | 231.73%            | -61.08% |    -0.14 |       82 | 42.26%     | ok               |
|          15 | -30.51%  | 231.73%            | -57.51% |    -0.17 |       87 | 52.41%     | ok               |

## LTC-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | -5.80%   | -59.09%            | -38.62% |     0.1  |       66 | 42.72%     | ok               |
|          45 | -8.26%   | -59.09%            | -37.29% |     0.05 |       56 | 31.99%     | ok               |
|          40 | -15.58%  | -59.09%            | -40.32% |    -0.06 |       56 | 37.74%     | ok               |
|          30 | -19.67%  | -59.09%            | -38.94% |    -0.09 |       70 | 49.81%     | ok               |
|          25 | -23.48%  | -59.09%            | -39.59% |    -0.14 |       74 | 52.68%     | ok               |

## MCD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 3.90%    | -3.13%             | -9.22%  |     0.24 |       42 | 20.63%     | ok               |
|          30 | -3.77%   | -3.13%             | -18.81% |    -0.1  |       77 | 38.27%     | ok               |
|          25 | -4.80%   | -3.13%             | -20.47% |    -0.13 |       77 | 40.93%     | ok               |
|          40 | -6.63%   | -3.13%             | -16.86% |    -0.26 |       69 | 28.95%     | ok               |
|          35 | -8.84%   | -3.13%             | -15.45% |    -0.34 |       69 | 34.61%     | ok               |

## META Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -19.96%  | 18.81%             | -34.72% |    -0.32 |       70 | 37.10%     | ok               |
|          40 | -27.97%  | 18.81%             | -38.23% |    -0.49 |       70 | 40.27%     | ok               |
|          25 | -34.26%  | 18.81%             | -43.26% |    -0.59 |       71 | 50.58%     | ok               |
|          50 | -29.98%  | 18.81%             | -37.42% |    -0.6  |       72 | 33.44%     | ok               |
|          30 | -36.02%  | 18.81%             | -42.43% |    -0.66 |       76 | 47.42%     | ok               |

## MPC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 19.89%   | 57.63%             | -23.96% |     0.46 |       48 | 38.77%     | ok               |
|          45 | 12.29%   | 57.63%             | -25.09% |     0.33 |       54 | 42.43%     | ok               |
|          40 | 8.05%    | 57.63%             | -25.70% |     0.26 |       56 | 44.59%     | ok               |
|          35 | 4.71%    | 57.63%             | -35.90% |     0.2  |       64 | 47.09%     | ok               |
|          30 | -11.76%  | 57.63%             | -44.76% |    -0.09 |       67 | 49.92%     | ok               |

## MRK Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -17.49%  | 5.05%              | -29.92% |    -0.29 |       87 | 54.08%     | ok               |
|          25 | -16.47%  | 5.05%              | -31.07% |    -0.3  |       72 | 46.26%     | ok               |
|          20 | -20.57%  | 5.05%              | -29.39% |    -0.4  |       77 | 49.58%     | ok               |
|          50 | -21.52%  | 5.05%              | -27.68% |    -0.6  |       58 | 29.12%     | ok               |
|          45 | -23.47%  | 5.05%              | -27.72% |    -0.62 |       59 | 32.45%     | ok               |

## MS Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -3.32%   | 144.29%            | -19.99% |     0    |       72 | 41.43%     | ok               |
|          15 | -4.98%   | 144.29%            | -22.02% |    -0.01 |       73 | 58.24%     | ok               |
|          20 | -5.09%   | 144.29%            | -25.68% |    -0.02 |       77 | 54.41%     | ok               |
|          30 | -10.18%  | 144.29%            | -27.79% |    -0.16 |       77 | 49.58%     | ok               |
|          35 | -10.11%  | 144.29%            | -25.26% |    -0.17 |       78 | 46.09%     | ok               |

## MSFT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -17.97%  | 17.43%             | -25.54% |    -0.46 |       68 | 34.44%     | ok               |
|          50 | -19.97%  | 17.43%             | -26.37% |    -0.54 |       62 | 29.62%     | ok               |
|          35 | -31.53%  | 17.43%             | -36.28% |    -0.8  |       75 | 43.26%     | ok               |
|          40 | -30.90%  | 17.43%             | -35.70% |    -0.82 |       71 | 38.10%     | ok               |
|          30 | -33.43%  | 17.43%             | -38.06% |    -0.83 |       83 | 47.42%     | ok               |

## MU Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 272.35%  | 848.59%            | -63.96% |     1.37 |       56 | 52.75%     | ok               |
|          15 | 296.07%  | 848.59%            | -61.96% |     1.3  |       51 | 66.39%     | ok               |
|          25 | 240.23%  | 848.59%            | -67.90% |     1.26 |       51 | 59.57%     | ok               |
|          30 | 226.76%  | 848.59%            | -68.76% |     1.24 |       51 | 57.90%     | ok               |
|          35 | 220.18%  | 848.59%            | -69.09% |     1.23 |       63 | 55.41%     | ok               |

## NEAR-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 58.08%   | -42.60%            | -49.73% |     0.73 |       40 | 22.22%     | ok               |
|          40 | 45.01%   | -42.60%            | -57.80% |     0.63 |       42 | 26.25%     | ok               |
|          50 | 38.01%   | -42.60%            | -52.97% |     0.58 |       34 | 17.82%     | ok               |
|          35 | 17.75%   | -42.60%            | -61.61% |     0.4  |       66 | 31.03%     | ok               |
|          30 | 4.96%    | -42.60%            | -59.54% |     0.3  |       83 | 40.42%     | ok               |

## NEM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 21.11%   | 203.43%            | -29.41% |     0.41 |       58 | 60.73%     | ok               |
|          20 | 8.14%    | 203.43%            | -30.47% |     0.27 |       68 | 56.24%     | ok               |
|          25 | -9.17%   | 203.43%            | -37.89% |     0.04 |       66 | 54.41%     | ok               |
|          30 | -20.55%  | 203.43%            | -38.49% |    -0.15 |       70 | 52.75%     | ok               |
|          50 | -20.74%  | 203.43%            | -33.24% |    -0.21 |       58 | 39.60%     | ok               |

## NFLX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 39.28%   | 21.75%             | -13.37% |     0.87 |       50 | 44.26%     | ok               |
|          50 | 35.04%   | 21.75%             | -16.28% |     0.85 |       48 | 36.27%     | ok               |
|          35 | 35.32%   | 21.75%             | -18.30% |     0.76 |       66 | 48.25%     | ok               |
|          45 | 25.49%   | 21.75%             | -15.48% |     0.63 |       56 | 40.60%     | ok               |
|          15 | 28.47%   | 21.75%             | -26.59% |     0.58 |       69 | 64.06%     | ok               |

## NKE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -29.39%  | -58.12%            | -54.28% |    -0.32 |       90 | 54.91%     | ok               |
|          20 | -29.39%  | -58.12%            | -49.34% |    -0.34 |       87 | 50.92%     | ok               |
|          35 | -26.77%  | -58.12%            | -42.13% |    -0.37 |       73 | 37.77%     | ok               |
|          25 | -32.32%  | -58.12%            | -51.20% |    -0.4  |       87 | 48.25%     | ok               |
|          30 | -36.04%  | -58.12%            | -55.35% |    -0.49 |       83 | 43.93%     | ok               |

## NOW Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 1.54%    | -24.56%            | -26.78% |     0.18 |       80 | 45.76%     | ok               |
|          20 | 0.36%    | -24.56%            | -34.71% |     0.18 |       77 | 52.25%     | ok               |
|          25 | -4.29%   | -24.56%            | -32.31% |     0.12 |       74 | 49.08%     | ok               |
|          15 | -8.40%   | -24.56%            | -38.33% |     0.07 |       87 | 55.41%     | ok               |
|          40 | -6.73%   | -24.56%            | -30.91% |     0.04 |       70 | 35.11%     | ok               |

## NVDA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -13.01%  | 147.02%            | -35.26% |    -0.05 |       74 | 47.42%     | ok               |
|          20 | -18.08%  | 147.02%            | -40.59% |    -0.08 |       70 | 55.44%     | ok               |
|          25 | -17.95%  | 147.02%            | -37.16% |    -0.1  |       71 | 50.45%     | ok               |
|          15 | -26.95%  | 147.02%            | -45.14% |    -0.2  |       71 | 58.65%     | ok               |
|          35 | -24.77%  | 147.02%            | -42.39% |    -0.27 |       82 | 44.56%     | ok               |

## OP-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 26.62%   | -91.16%            | -34.16% |     0.5  |       34 | 11.49%     | ok               |
|          45 | 20.44%   | -91.16%            | -45.76% |     0.42 |       34 | 15.90%     | ok               |
|          40 | 10.62%   | -91.16%            | -53.61% |     0.32 |       48 | 24.33%     | ok               |
|          35 | -12.10%  | -91.16%            | -59.71% |     0.07 |       52 | 28.74%     | ok               |
|          30 | -15.92%  | -91.16%            | -71.26% |     0.07 |       66 | 35.25%     | ok               |

## ORCL Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 213.05%  | 15.03%             | -29.32% |     1.27 |       65 | 65.39%     | ok               |
|          25 | 134.81%  | 15.03%             | -27.76% |     1.01 |       63 | 58.90%     | ok               |
|          20 | 133.46%  | 15.03%             | -29.32% |     1    |       68 | 61.23%     | ok               |
|          45 | 108.34%  | 15.03%             | -32.35% |     0.96 |       62 | 43.09%     | ok               |
|          35 | 112.58%  | 15.03%             | -31.95% |     0.94 |       68 | 52.25%     | ok               |

## OXY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | -1.23%   | -13.29%            | -30.05% |     0.09 |       70 | 41.43%     | ok               |
|          30 | -3.62%   | -13.29%            | -34.15% |     0.06 |       71 | 46.92%     | ok               |
|          50 | -2.20%   | -13.29%            | -29.57% |     0.06 |       40 | 29.28%     | ok               |
|          40 | -7.19%   | -13.29%            | -31.66% |    -0.03 |       58 | 36.61%     | ok               |
|          25 | -15.96%  | -13.29%            | -42.58% |    -0.16 |       79 | 51.25%     | ok               |

## PEP Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 13.39%   | -16.04%            | -11.62% |     0.6  |       42 | 27.62%     | ok               |
|          45 | 6.54%    | -16.04%            | -14.22% |     0.32 |       62 | 32.11%     | ok               |
|          40 | 2.43%    | -16.04%            | -18.04% |     0.15 |       70 | 37.60%     | ok               |
|          35 | 1.27%    | -16.04%            | -21.42% |     0.1  |       77 | 42.26%     | ok               |
|          30 | -4.68%   | -16.04%            | -21.35% |    -0.07 |       77 | 48.25%     | ok               |

## PEPE-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -8.77%   | -60.53%            | -57.66% |     0.2  |       81 | 45.98%     | ok               |
|          15 | -17.71%  | -60.53%            | -61.96% |     0.19 |       78 | 61.88%     | ok               |
|          35 | -11.24%  | -60.53%            | -49.27% |     0.14 |       68 | 40.04%     | ok               |
|          25 | -17.94%  | -60.53%            | -53.88% |     0.12 |       87 | 51.53%     | ok               |
|          20 | -25.81%  | -60.53%            | -61.13% |     0.07 |       84 | 58.43%     | ok               |

## PFE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -21.69%  | -8.54%             | -22.94% |    -0.8  |       52 | 18.97%     | ok               |
|          50 | -23.07%  | -8.54%             | -24.78% |    -0.96 |       38 | 15.31%     | ok               |
|          40 | -27.86%  | -8.54%             | -30.10% |    -0.97 |       74 | 24.13%     | ok               |
|          35 | -33.84%  | -8.54%             | -35.77% |    -1.12 |       88 | 31.95%     | ok               |
|          30 | -41.44%  | -8.54%             | -43.15% |    -1.34 |       83 | 36.61%     | ok               |

## PG Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -9.15%   | -9.55%             | -19.77% |    -0.34 |       56 | 30.95%     | ok               |
|          35 | -12.25%  | -9.55%             | -18.66% |    -0.46 |       64 | 34.44%     | ok               |
|          30 | -19.88%  | -9.55%             | -23.92% |    -0.76 |       67 | 37.44%     | ok               |
|          45 | -18.03%  | -9.55%             | -22.13% |    -0.8  |       56 | 28.45%     | ok               |
|          25 | -21.71%  | -9.55%             | -25.62% |    -0.84 |       79 | 38.94%     | ok               |

## PM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | -3.65%   | 98.21%             | -32.95% |     0.01 |       88 | 52.41%     | ok               |
|          20 | -6.26%   | 98.21%             | -33.29% |    -0.04 |       87 | 60.90%     | ok               |
|          30 | -6.67%   | 98.21%             | -34.97% |    -0.05 |       83 | 55.91%     | ok               |
|          40 | -10.44%  | 98.21%             | -37.94% |    -0.17 |       82 | 48.75%     | ok               |
|          50 | -9.84%   | 98.21%             | -35.70% |    -0.17 |       76 | 42.26%     | ok               |

## POL-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 60.31%   | -70.65%            | -41.08% |     0.76 |       79 | 49.62%     | ok               |
|          25 | 40.63%   | -70.65%            | -46.72% |     0.59 |       64 | 57.66%     | ok               |
|          20 | 29.19%   | -70.65%            | -52.88% |     0.5  |       70 | 62.07%     | ok               |
|          15 | -3.40%   | -70.65%            | -58.42% |     0.2  |       74 | 66.48%     | ok               |
|          40 | 0.42%    | -70.65%            | -38.75% |     0.17 |       54 | 30.27%     | ok               |

## QCOM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -5.14%   | -6.92%             | -54.50% |     0.11 |       73 | 47.59%     | ok               |
|          20 | -8.99%   | -6.92%             | -54.38% |     0.06 |       69 | 50.42%     | ok               |
|          35 | -11.68%  | -6.92%             | -50.58% |     0.01 |       81 | 43.09%     | ok               |
|          30 | -21.69%  | -6.92%             | -56.59% |    -0.14 |       77 | 45.59%     | ok               |
|          15 | -24.12%  | -6.92%             | -57.94% |    -0.15 |       73 | 53.58%     | ok               |

## QQQ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 24.96%   | 62.93%             | -14.17% |     0.62 |       65 | 52.41%     | ok               |
|          25 | 18.14%   | 62.93%             | -13.90% |     0.52 |       63 | 46.42%     | ok               |
|          30 | 15.87%   | 62.93%             | -13.49% |     0.48 |       64 | 43.93%     | ok               |
|          20 | 15.29%   | 62.93%             | -15.99% |     0.44 |       71 | 49.08%     | ok               |
|          35 | 2.63%    | 62.93%             | -19.93% |     0.15 |       72 | 40.43%     | ok               |

## RENDER-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 47.58%   | -64.56%            | -43.43% |     0.62 |       92 | 53.26%     | ok               |
|          15 | 39.54%   | -64.56%            | -44.59% |     0.57 |       92 | 56.70%     | ok               |
|          25 | 38.29%   | -64.56%            | -40.60% |     0.56 |       90 | 48.66%     | ok               |
|          30 | -6.70%   | -64.56%            | -45.62% |     0.21 |       98 | 42.15%     | ok               |
|          40 | -11.60%  | -64.56%            | -40.91% |     0.1  |       74 | 27.20%     | ok               |

## RTX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 52.41%   | 145.48%            | -18.66% |     1.04 |       72 | 57.74%     | ok               |
|          35 | 41.82%   | 145.48%            | -18.00% |     0.98 |       50 | 51.91%     | ok               |
|          25 | 47.20%   | 145.48%            | -18.59% |     0.97 |       60 | 55.07%     | ok               |
|          30 | 44.96%   | 145.48%            | -16.99% |     0.94 |       54 | 53.91%     | ok               |
|          15 | 43.73%   | 145.48%            | -19.55% |     0.89 |       67 | 62.40%     | ok               |

## SBUX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -9.63%   | 15.71%             | -23.55% |    -0.11 |       59 | 42.10%     | ok               |
|          45 | -12.59%  | 15.71%             | -27.26% |    -0.25 |       68 | 30.45%     | ok               |
|          40 | -15.23%  | 15.71%             | -25.43% |    -0.29 |       64 | 34.11%     | ok               |
|          30 | -19.04%  | 15.71%             | -29.22% |    -0.35 |       62 | 39.93%     | ok               |
|          50 | -16.60%  | 15.71%             | -25.77% |    -0.39 |       56 | 26.12%     | ok               |

## SCHW Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 11.40%   | 60.91%             | -16.53% |     0.38 |       60 | 35.27%     | ok               |
|          25 | 6.53%    | 60.91%             | -28.76% |     0.24 |       63 | 51.25%     | ok               |
|          50 | 4.75%    | 60.91%             | -13.28% |     0.22 |       54 | 32.45%     | ok               |
|          20 | 2.71%    | 60.91%             | -29.24% |     0.15 |       71 | 53.74%     | ok               |
|          40 | 0.71%    | 60.91%             | -23.35% |     0.1  |       66 | 38.44%     | ok               |

## SHIB-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -24.93%  | -62.68%            | -50.97% |    -0.09 |       80 | 67.05%     | ok               |
|          25 | -24.02%  | -62.68%            | -45.80% |    -0.09 |       75 | 59.20%     | ok               |
|          20 | -28.59%  | -62.68%            | -48.24% |    -0.16 |       77 | 63.03%     | ok               |
|          35 | -27.56%  | -62.68%            | -52.76% |    -0.21 |       66 | 46.55%     | ok               |
|          30 | -33.69%  | -62.68%            | -47.96% |    -0.3  |       76 | 52.49%     | ok               |

## SHY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd    |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:-------|---------:|---------:|:-----------|:-----------------|
|          30 | -2.23%   | 0.36%              | -2.85% |    -0.78 |       46 | 34.11%     | ok               |
|          35 | -2.34%   | 0.36%              | -3.27% |    -0.83 |       48 | 32.28%     | ok               |
|          40 | -2.46%   | 0.36%              | -3.33% |    -0.89 |       48 | 30.45%     | ok               |
|          45 | -2.61%   | 0.36%              | -3.23% |    -0.98 |       48 | 26.79%     | ok               |
|          25 | -3.10%   | 0.36%              | -3.99% |    -1.06 |       58 | 36.27%     | ok               |

## SKY-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -36.28%  | -2.32%             | -56.39% |    -0.39 |       65 | 52.21%     | ok               |
|          30 | -32.73%  | -2.32%             | -47.82% |    -0.41 |       76 | 42.53%     | ok               |
|          25 | -35.62%  | -2.32%             | -50.05% |    -0.45 |       70 | 46.11%     | ok               |
|          20 | -45.42%  | -2.32%             | -59.15% |    -0.62 |       67 | 49.47%     | ok               |
|          35 | -38.93%  | -2.32%             | -49.68% |    -0.63 |       70 | 35.16%     | ok               |

## SLB Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 12.93%   | -5.06%             | -21.46% |     0.36 |       54 | 33.44%     | ok               |
|          40 | 9.44%    | -5.06%             | -25.33% |     0.29 |       48 | 36.94%     | ok               |
|          50 | -7.24%   | -5.06%             | -29.64% |    -0.1  |       52 | 28.95%     | ok               |
|          35 | -19.69%  | -5.06%             | -43.52% |    -0.33 |       76 | 44.09%     | ok               |
|          30 | -32.08%  | -5.06%             | -54.23% |    -0.61 |       77 | 50.58%     | ok               |

## SLV Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 63.41%   | 146.03%            | -34.10% |     0.83 |       52 | 34.11%     | ok               |
|          45 | 61.43%   | 146.03%            | -31.82% |     0.8  |       58 | 35.27%     | ok               |
|          40 | 59.50%   | 146.03%            | -31.93% |     0.78 |       64 | 37.44%     | ok               |
|          20 | 47.80%   | 146.03%            | -42.66% |     0.66 |       66 | 47.75%     | ok               |
|          35 | 45.90%   | 146.03%            | -36.89% |     0.66 |       72 | 40.27%     | ok               |

## SMH Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 85.01%   | 154.94%            | -31.01% |     1.12 |       51 | 48.59%     | ok               |
|          35 | 70.25%   | 154.94%            | -34.03% |     1.02 |       52 | 44.26%     | ok               |
|          25 | 67.47%   | 154.94%            | -32.94% |     0.98 |       48 | 47.25%     | ok               |
|          30 | 66.32%   | 154.94%            | -33.66% |     0.98 |       48 | 45.76%     | ok               |
|          45 | 53.74%   | 154.94%            | -33.35% |     0.91 |       52 | 38.60%     | ok               |

## SNX-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 22.19%   | -76.11%            | -30.08% |     0.44 |       60 | 29.50%     | ok               |
|          40 | 11.29%   | -76.11%            | -28.61% |     0.33 |       46 | 23.75%     | ok               |
|          20 | 3.96%    | -76.11%            | -43.20% |     0.3  |       71 | 48.28%     | ok               |
|          30 | -6.87%   | -76.11%            | -38.68% |     0.17 |       64 | 37.55%     | ok               |
|          15 | -26.72%  | -76.11%            | -44.00% |    -0    |       81 | 52.87%     | ok               |

## SOL-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 22.61%   | -48.30%            | -39.68% |     0.45 |       58 | 36.40%     | ok               |
|          35 | -11.12%  | -48.30%            | -48.34% |     0.1  |       72 | 43.87%     | ok               |
|          25 | -18.96%  | -48.30%            | -41.09% |     0.02 |       76 | 57.09%     | ok               |
|          45 | -13.80%  | -48.30%            | -48.75% |     0.01 |       58 | 30.46%     | ok               |
|          15 | -28.62%  | -48.30%            | -49.65% |    -0.08 |       81 | 63.22%     | ok               |

## SOXX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 70.15%   | 136.74%            | -38.76% |     0.97 |       60 | 41.60%     | ok               |
|          25 | 72.19%   | 136.74%            | -39.65% |     0.97 |       54 | 46.59%     | ok               |
|          30 | 66.09%   | 136.74%            | -40.14% |     0.92 |       56 | 44.26%     | ok               |
|          20 | 59.18%   | 136.74%            | -38.67% |     0.84 |       59 | 47.42%     | ok               |
|          40 | 52.35%   | 136.74%            | -41.03% |     0.81 |       60 | 39.27%     | ok               |

## SPY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 12.33%   | 49.19%             | -14.25% |     0.45 |       59 | 52.75%     | ok               |
|          15 | 11.33%   | 49.19%             | -16.80% |     0.42 |       67 | 55.74%     | ok               |
|          25 | 5.34%    | 49.19%             | -15.22% |     0.24 |       59 | 51.75%     | ok               |
|          30 | 0.89%    | 49.19%             | -16.47% |     0.09 |       62 | 48.92%     | ok               |
|          35 | 0.29%    | 49.19%             | -16.72% |     0.07 |       58 | 45.92%     | ok               |

## SUSHI-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -28.52%  | -79.09%            | -40.08% |    -0.27 |       54 | 14.94%     | ok               |
|          40 | -64.10%  | -79.09%            | -70.29% |    -0.84 |       67 | 25.10%     | ok               |
|          45 | -61.36%  | -79.09%            | -65.87% |    -0.84 |       60 | 18.58%     | ok               |
|          15 | -76.04%  | -79.09%            | -82.03% |    -0.89 |       91 | 49.04%     | ok               |
|          20 | -80.08%  | -79.09%            | -84.30% |    -1.09 |       95 | 46.17%     | ok               |

## T Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 55.32%   | 34.15%             | -18.13% |     1.07 |       58 | 58.57%     | ok               |
|          25 | 51.12%   | 34.15%             | -17.66% |     1.02 |       58 | 56.24%     | ok               |
|          15 | 53.33%   | 34.15%             | -15.08% |     1.01 |       67 | 62.73%     | ok               |
|          30 | 34.56%   | 34.15%             | -17.01% |     0.78 |       62 | 54.24%     | ok               |
|          35 | 20.32%   | 34.15%             | -14.49% |     0.54 |       66 | 50.25%     | ok               |

## TGT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -19.86%  | -11.38%            | -44.02% |    -0.34 |       86 | 44.76%     | ok               |
|          25 | -19.41%  | -11.38%            | -43.64% |    -0.37 |       68 | 39.93%     | ok               |
|          30 | -18.43%  | -11.38%            | -40.57% |    -0.37 |       62 | 37.27%     | ok               |
|          15 | -24.97%  | -11.38%            | -42.01% |    -0.44 |       78 | 49.42%     | ok               |
|          45 | -20.90%  | -11.38%            | -32.58% |    -0.52 |       58 | 27.79%     | ok               |

## TIA-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 3.06%    | -90.28%            | -53.37% |     0.26 |       66 | 32.95%     | ok               |
|          40 | -4.77%   | -90.28%            | -48.24% |     0.16 |       68 | 27.59%     | ok               |
|          45 | -2.76%   | -90.28%            | -49.52% |     0.16 |       56 | 19.73%     | ok               |
|          50 | -0.89%   | -90.28%            | -48.70% |     0.14 |       36 | 12.45%     | ok               |
|          25 | -35.55%  | -90.28%            | -59.67% |    -0.11 |       89 | 45.02%     | ok               |

## TLT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -19.02%  | -12.09%            | -21.87% |    -1.41 |       70 | 33.94%     | ok               |
|          50 | -13.39%  | -12.09%            | -14.79% |    -1.55 |       34 | 15.64%     | ok               |
|          40 | -17.16%  | -12.09%            | -18.61% |    -1.56 |       56 | 23.46%     | ok               |
|          35 | -19.81%  | -12.09%            | -21.63% |    -1.66 |       64 | 28.12%     | ok               |
|          15 | -24.95%  | -12.09%            | -27.76% |    -1.69 |       75 | 41.93%     | ok               |

## TMO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 48.70%   | -2.61%             | -8.17%  |     1.07 |       44 | 33.11%     | ok               |
|          45 | 42.25%   | -2.61%             | -9.39%  |     0.91 |       48 | 38.10%     | ok               |
|          40 | 40.95%   | -2.61%             | -9.81%  |     0.87 |       51 | 42.76%     | ok               |
|          35 | 33.81%   | -2.61%             | -13.84% |     0.71 |       61 | 47.42%     | ok               |
|          30 | 27.81%   | -2.61%             | -18.85% |     0.59 |       61 | 52.58%     | ok               |

## TMUS Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 7.68%    | 5.71%              | -30.05% |     0.25 |       65 | 58.74%     | ok               |
|          30 | 6.48%    | 5.71%              | -25.71% |     0.23 |       70 | 46.76%     | ok               |
|          20 | 1.47%    | 5.71%              | -29.75% |     0.13 |       71 | 53.08%     | ok               |
|          25 | -1.93%   | 5.71%              | -31.45% |     0.06 |       75 | 49.25%     | ok               |
|          35 | -7.65%   | 5.71%              | -34.23% |    -0.08 |       68 | 43.43%     | ok               |

## TRX-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 13.27%   | 42.05%             | -18.79% |     0.46 |       54 | 36.40%     | ok               |
|          30 | 9.99%    | 42.05%             | -22.90% |     0.35 |       70 | 48.47%     | ok               |
|          35 | 8.34%    | 42.05%             | -21.77% |     0.32 |       68 | 45.02%     | ok               |
|          20 | 8.68%    | 42.05%             | -25.45% |     0.31 |       63 | 55.56%     | ok               |
|          25 | 7.94%    | 42.05%             | -26.84% |     0.3  |       66 | 51.72%     | ok               |

## TSLA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 42.24%   | 89.73%             | -32.60% |     0.61 |       66 | 30.62%     | ok               |
|          40 | 21.78%   | 89.73%             | -45.90% |     0.41 |       67 | 35.77%     | ok               |
|          45 | 2.62%    | 89.73%             | -46.86% |     0.22 |       71 | 32.95%     | ok               |
|          35 | -13.06%  | 89.73%             | -54.51% |     0.06 |       78 | 38.60%     | ok               |
|          30 | -28.06%  | 89.73%             | -57.89% |    -0.12 |       74 | 42.60%     | ok               |

## TXN Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 12.39%   | 60.83%             | -45.45% |     0.32 |       66 | 33.44%     | ok               |
|          35 | -5.06%   | 60.83%             | -43.38% |     0.05 |       72 | 47.75%     | ok               |
|          15 | -7.77%   | 60.83%             | -39.48% |     0.05 |       65 | 61.40%     | ok               |
|          40 | -5.70%   | 60.83%             | -45.67% |     0.04 |       70 | 45.59%     | ok               |
|          20 | -8.35%   | 60.83%             | -38.98% |     0.04 |       64 | 57.07%     | ok               |

## UNH Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 29.50%   | -15.42%            | -26.96% |     0.51 |       74 | 51.91%     | ok               |
|          50 | 26.51%   | -15.42%            | -37.02% |     0.5  |       56 | 30.62%     | ok               |
|          35 | 26.81%   | -15.42%            | -28.32% |     0.49 |       66 | 46.59%     | ok               |
|          15 | 25.96%   | -15.42%            | -33.62% |     0.46 |       73 | 66.89%     | ok               |
|          25 | 15.22%   | -15.42%            | -29.39% |     0.35 |       74 | 57.24%     | ok               |

## UNI-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -25.40%  | -42.36%            | -63.75% |    -0.08 |       62 | 34.10%     | ok               |
|          45 | -30.54%  | -42.36%            | -58.49% |    -0.18 |       64 | 29.12%     | ok               |
|          50 | -29.23%  | -42.36%            | -54.35% |    -0.18 |       58 | 22.80%     | ok               |
|          35 | -42.10%  | -42.36%            | -68.71% |    -0.28 |       76 | 40.04%     | ok               |
|          20 | -76.61%  | -42.36%            | -83.47% |    -0.88 |      101 | 56.32%     | ok               |

## UPS Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -39.51%  | -30.41%            | -42.17% |    -0.76 |       86 | 48.25%     | ok               |
|          25 | -39.66%  | -30.41%            | -40.05% |    -0.78 |       78 | 44.76%     | ok               |
|          35 | -38.80%  | -30.41%            | -40.10% |    -0.8  |       67 | 34.44%     | ok               |
|          15 | -41.65%  | -30.41%            | -42.97% |    -0.81 |       88 | 52.08%     | ok               |
|          30 | -41.93%  | -30.41%            | -43.16% |    -0.87 |       72 | 40.27%     | ok               |

## USO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 12.37%   | 52.99%             | -33.25% |     0.32 |       48 | 27.29%     | ok               |
|          20 | 10.82%   | 52.99%             | -44.92% |     0.29 |       75 | 40.43%     | ok               |
|          25 | 6.44%    | 52.99%             | -44.86% |     0.23 |       69 | 37.60%     | ok               |
|          15 | 5.58%    | 52.99%             | -45.09% |     0.22 |       74 | 43.59%     | ok               |
|          30 | 1.85%    | 52.99%             | -43.35% |     0.16 |       70 | 34.44%     | ok               |

## VEA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 3.65%    | 44.38%             | -16.28% |     0.19 |       58 | 49.08%     | ok               |
|          20 | -0.53%   | 44.38%             | -17.70% |     0.03 |       59 | 46.42%     | ok               |
|          25 | -2.50%   | 44.38%             | -17.79% |    -0.05 |       55 | 44.76%     | ok               |
|          30 | -2.66%   | 44.38%             | -17.93% |    -0.06 |       56 | 42.60%     | ok               |
|          35 | -3.75%   | 44.38%             | -16.79% |    -0.11 |       54 | 41.60%     | ok               |

## VIXY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -48.04%  | -63.28%            | -69.78% |    -0.43 |       46 | 10.48%     | ok               |
|          45 | -57.65%  | -63.28%            | -75.03% |    -0.58 |       58 | 16.47%     | ok               |
|          40 | -65.68%  | -63.28%            | -80.72% |    -0.69 |       72 | 20.80%     | ok               |
|          35 | -69.93%  | -63.28%            | -84.37% |    -0.74 |       90 | 25.79%     | ok               |
|          15 | -76.29%  | -63.28%            | -89.47% |    -0.75 |       99 | 43.43%     | ok               |

## VNQ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -9.57%   | 14.12%             | -19.07% |    -0.42 |       58 | 28.95%     | ok               |
|          50 | -10.00%  | 14.12%             | -17.13% |    -0.46 |       54 | 26.46%     | ok               |
|          25 | -13.67%  | 14.12%             | -22.16% |    -0.53 |       66 | 41.26%     | ok               |
|          20 | -15.25%  | 14.12%             | -23.61% |    -0.59 |       69 | 43.93%     | ok               |
|          15 | -16.54%  | 14.12%             | -24.73% |    -0.64 |       66 | 45.09%     | ok               |

## VTI Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 15.23%   | 48.18%             | -13.96% |     0.54 |       62 | 53.24%     | ok               |
|          15 | 9.33%    | 48.18%             | -15.70% |     0.35 |       65 | 55.74%     | ok               |
|          25 | 1.91%    | 48.18%             | -16.10% |     0.13 |       58 | 51.25%     | ok               |
|          30 | -5.73%   | 48.18%             | -18.77% |    -0.15 |       68 | 49.25%     | ok               |
|          40 | -7.08%   | 48.18%             | -20.44% |    -0.23 |       68 | 42.10%     | ok               |

## VWO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -7.93%   | 42.91%             | -21.18% |    -0.28 |       58 | 30.12%     | ok               |
|          45 | -9.73%   | 42.91%             | -23.26% |    -0.36 |       60 | 32.61%     | ok               |
|          15 | -12.24%  | 42.91%             | -24.01% |    -0.38 |       76 | 48.09%     | ok               |
|          40 | -10.76%  | 42.91%             | -23.57% |    -0.39 |       70 | 35.27%     | ok               |
|          20 | -13.64%  | 42.91%             | -26.14% |    -0.45 |       73 | 45.76%     | ok               |

## VZ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -6.65%   | 15.42%             | -12.71% |    -0.17 |       52 | 25.62%     | ok               |
|          25 | -19.99%  | 15.42%             | -22.13% |    -0.55 |       79 | 43.09%     | ok               |
|          45 | -17.79%  | 15.42%             | -21.44% |    -0.57 |       66 | 29.28%     | ok               |
|          35 | -18.97%  | 15.42%             | -22.73% |    -0.58 |       61 | 35.11%     | ok               |
|          40 | -23.50%  | 15.42%             | -24.21% |    -0.78 |       66 | 32.45%     | ok               |

## WFC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | -11.80%  | 54.22%             | -22.54% |    -0.19 |       81 | 45.92%     | ok               |
|          50 | -9.08%   | 54.22%             | -18.29% |    -0.23 |       62 | 33.61%     | ok               |
|          20 | -18.73%  | 54.22%             | -29.87% |    -0.27 |       79 | 55.07%     | ok               |
|          30 | -20.99%  | 54.22%             | -29.78% |    -0.37 |       84 | 49.08%     | ok               |
|          25 | -24.40%  | 54.22%             | -33.38% |    -0.43 |       76 | 52.08%     | ok               |

## WIF-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 29.75%   | -78.20%            | -46.21% |     0.51 |       74 | 43.87%     | ok               |
|          20 | 26.38%   | -78.20%            | -40.67% |     0.48 |       67 | 41.00%     | ok               |
|          25 | -35.79%  | -78.20%            | -52.50% |    -0.07 |       71 | 37.74%     | ok               |
|          50 | -24.32%  | -78.20%            | -41.18% |    -0.22 |       42 | 12.26%     | ok               |
|          30 | -52.90%  | -78.20%            | -61.76% |    -0.39 |       72 | 33.91%     | ok               |

## WMT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 40.32%   | 83.32%             | -9.18%  |     1.16 |       40 | 39.77%     | ok               |
|          50 | 34.89%   | 83.32%             | -12.19% |     1.09 |       34 | 37.27%     | ok               |
|          40 | 28.64%   | 83.32%             | -13.41% |     0.86 |       46 | 41.10%     | ok               |
|          35 | 27.79%   | 83.32%             | -13.99% |     0.81 |       56 | 45.76%     | ok               |
|          15 | 14.49%   | 83.32%             | -25.74% |     0.4  |       72 | 59.90%     | ok               |

## XBI Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 3.88%    | 57.58%             | -16.08% |     0.18 |       58 | 33.94%     | ok               |
|          45 | 3.08%    | 57.58%             | -15.46% |     0.16 |       50 | 30.78%     | ok               |
|          35 | -3.25%   | 57.58%             | -16.96% |    -0    |       66 | 37.77%     | ok               |
|          30 | -5.27%   | 57.58%             | -18.30% |    -0.05 |       68 | 39.27%     | ok               |
|          50 | -5.38%   | 57.58%             | -15.97% |    -0.09 |       52 | 27.45%     | ok               |

## XLB Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -4.44%   | 15.39%             | -19.67% |    -0.12 |       54 | 29.95%     | ok               |
|          50 | -5.71%   | 15.39%             | -17.59% |    -0.19 |       42 | 25.79%     | ok               |
|          35 | -7.58%   | 15.39%             | -22.65% |    -0.24 |       56 | 33.28%     | ok               |
|          45 | -7.32%   | 15.39%             | -19.78% |    -0.25 |       42 | 27.12%     | ok               |
|          25 | -10.63%  | 15.39%             | -22.63% |    -0.34 |       60 | 38.77%     | ok               |

## XLC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 14.08%   | 38.10%             | -12.33% |     0.51 |       65 | 52.58%     | ok               |
|          25 | 11.27%   | 38.10%             | -12.31% |     0.42 |       64 | 54.41%     | ok               |
|          40 | 7.83%    | 38.10%             | -13.38% |     0.34 |       66 | 45.76%     | ok               |
|          35 | 7.01%    | 38.10%             | -13.38% |     0.3  |       64 | 49.92%     | ok               |
|          20 | 3.64%    | 38.10%             | -11.36% |     0.18 |       70 | 57.24%     | ok               |

## XLE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 1.63%    | 26.85%             | -25.98% |     0.12 |       54 | 36.11%     | ok               |
|          45 | -2.54%   | 26.85%             | -29.68% |     0    |       60 | 38.10%     | ok               |
|          35 | -4.59%   | 26.85%             | -31.51% |    -0.04 |       65 | 42.76%     | ok               |
|          25 | -10.91%  | 26.85%             | -36.05% |    -0.19 |       83 | 48.25%     | ok               |
|          40 | -10.81%  | 26.85%             | -34.51% |    -0.24 |       64 | 40.60%     | ok               |

## XLF Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -4.11%   | 40.91%             | -18.01% |    -0.07 |       68 | 53.74%     | ok               |
|          15 | -8.07%   | 40.91%             | -19.58% |    -0.21 |       76 | 56.57%     | ok               |
|          25 | -10.79%  | 40.91%             | -23.22% |    -0.33 |       77 | 50.25%     | ok               |
|          30 | -12.24%  | 40.91%             | -23.61% |    -0.4  |       78 | 47.59%     | ok               |
|          35 | -20.09%  | 40.91%             | -27.41% |    -0.8  |       68 | 43.26%     | ok               |

## XLI Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 4.55%    | 52.07%             | -10.36% |     0.21 |       80 | 50.92%     | ok               |
|          20 | 0.35%    | 52.07%             | -12.74% |     0.07 |       73 | 45.76%     | ok               |
|          25 | -4.92%   | 52.07%             | -14.41% |    -0.14 |       70 | 43.76%     | ok               |
|          30 | -5.50%   | 52.07%             | -14.12% |    -0.17 |       72 | 42.76%     | ok               |
|          45 | -5.21%   | 52.07%             | -16.29% |    -0.18 |       70 | 34.11%     | ok               |

## XLK Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 86.15%   | 78.13%             | -14.75% |     1.34 |       45 | 51.58%     | ok               |
|          20 | 79.05%   | 78.13%             | -14.75% |     1.31 |       48 | 49.25%     | ok               |
|          25 | 75.40%   | 78.13%             | -14.75% |     1.31 |       42 | 47.09%     | ok               |
|          30 | 64.90%   | 78.13%             | -14.75% |     1.21 |       42 | 45.76%     | ok               |
|          35 | 46.50%   | 78.13%             | -13.61% |     0.97 |       54 | 43.09%     | ok               |

## XLM-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 26.14%   | -44.40%            | -38.97% |     0.48 |       44 | 27.39%     | ok               |
|          45 | 22.34%   | -44.40%            | -43.99% |     0.44 |       50 | 31.03%     | ok               |
|          30 | 7.39%    | -44.40%            | -50.36% |     0.3  |       65 | 45.21%     | ok               |
|          25 | 4.10%    | -44.40%            | -48.11% |     0.27 |       67 | 47.70%     | ok               |
|          20 | -4.13%   | -44.40%            | -55.30% |     0.18 |       66 | 50.00%     | ok               |

## XLP Threshold Sweep

|   threshold | return   | benchmark_return   | mdd    |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:-------|---------:|---------:|:-----------|:-----------------|
|          45 | 10.86%   | 12.06%             | -5.66% |     0.68 |       52 | 31.95%     | ok               |
|          40 | 10.24%   | 12.06%             | -7.32% |     0.62 |       68 | 35.94%     | ok               |
|          35 | 9.28%    | 12.06%             | -8.39% |     0.56 |       64 | 38.94%     | ok               |
|          50 | 7.83%    | 12.06%             | -6.08% |     0.51 |       56 | 30.28%     | ok               |
|          30 | 8.40%    | 12.06%             | -8.96% |     0.5  |       66 | 40.60%     | ok               |

## XLU Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 5.85%    | 36.69%             | -12.97% |     0.32 |       52 | 31.28%     | ok               |
|          45 | 4.45%    | 36.69%             | -14.27% |     0.25 |       54 | 32.28%     | ok               |
|          40 | 1.57%    | 36.69%             | -15.59% |     0.12 |       58 | 33.78%     | ok               |
|          35 | -4.35%   | 36.69%             | -19.71% |    -0.16 |       62 | 35.94%     | ok               |
|          30 | -5.24%   | 36.69%             | -20.40% |    -0.19 |       67 | 39.10%     | ok               |

## XLV Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -15.44%  | 12.09%             | -19.17% |    -0.77 |       66 | 34.28%     | ok               |
|          25 | -15.99%  | 12.09%             | -21.24% |    -0.79 |       66 | 36.27%     | ok               |
|          15 | -19.24%  | 12.09%             | -24.51% |    -0.92 |       79 | 41.26%     | ok               |
|          20 | -19.17%  | 12.09%             | -24.60% |    -0.95 |       71 | 38.10%     | ok               |
|          45 | -17.35%  | 12.09%             | -20.89% |    -1.03 |       56 | 24.96%     | ok               |

## XLY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 3.44%    | 31.10%             | -14.01% |     0.17 |       68 | 43.76%     | ok               |
|          35 | 1.77%    | 31.10%             | -12.94% |     0.12 |       70 | 41.26%     | ok               |
|          15 | 0.79%    | 31.10%             | -15.77% |     0.1  |       72 | 49.92%     | ok               |
|          20 | -1.93%   | 31.10%             | -19.25% |     0.02 |       67 | 46.59%     | ok               |
|          50 | -2.61%   | 31.10%             | -12.26% |    -0.05 |       56 | 29.78%     | ok               |

## XOM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | 6.47%    | 38.44%             | -19.90% |     0.25 |       55 | 38.60%     | ok               |
|          50 | 5.55%    | 38.44%             | -21.35% |     0.23 |       38 | 30.78%     | ok               |
|          30 | 5.41%    | 38.44%             | -20.29% |     0.22 |       55 | 37.94%     | ok               |
|          20 | -1.06%   | 38.44%             | -25.56% |     0.05 |       64 | 40.77%     | ok               |
|          45 | -1.26%   | 38.44%             | -23.33% |     0.04 |       44 | 32.28%     | ok               |

## XRP-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 6.29%    | -56.15%            | -31.38% |     0.27 |       62 | 38.70%     | ok               |
|          40 | -5.00%   | -56.15%            | -33.91% |     0.11 |       52 | 32.95%     | ok               |
|          30 | -10.91%  | -56.15%            | -35.71% |     0.05 |       64 | 42.91%     | ok               |
|          45 | -15.61%  | -56.15%            | -36.27% |    -0.06 |       52 | 28.74%     | ok               |
|          20 | -31.73%  | -56.15%            | -49.05% |    -0.23 |       82 | 52.11%     | ok               |

## YFI-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -48.54%  | -61.20%            | -52.84% |    -0.77 |       60 | 28.16%     | ok               |
|          45 | -47.02%  | -61.20%            | -54.66% |    -0.92 |       70 | 22.80%     | ok               |
|          35 | -59.50%  | -61.20%            | -63.29% |    -0.94 |       65 | 35.44%     | ok               |
|          30 | -64.19%  | -61.20%            | -71.12% |    -1.03 |       81 | 40.61%     | ok               |
|          15 | -69.66%  | -61.20%            | -74.96% |    -1.08 |       89 | 53.83%     | ok               |

## ZEC-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 104.24%  | 1300.74%           | -24.66% |     0.83 |       46 | 25.10%     | ok               |
|          35 | 74.77%   | 1300.74%           | -44.34% |     0.7  |       54 | 31.23%     | ok               |
|          25 | 58.90%   | 1300.74%           | -51.83% |     0.63 |       60 | 40.61%     | ok               |
|          30 | 37.61%   | 1300.74%           | -49.80% |     0.53 |       66 | 37.36%     | ok               |
|          50 | 40.39%   | 1300.74%           | -34.17% |     0.52 |       48 | 22.61%     | ok               |
