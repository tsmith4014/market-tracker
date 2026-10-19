# Market Tracker Backtest Report

_Generated: 2026-10-19T04:45:03+00:00_

## Data Sources

- Crypto: Kraken -> Coinbase -> CoinGecko OHLC -> CoinPaprika fallback chain.
- Stocks / ETFs / indices: Stooq -> Yahoo Finance fallback chain.
- Data rows are generated from real market APIs. Mock OHLCV rows are not generated.

## Data Freshness

- Rows: **92,746**
- Symbols: **161**
- Date range: **2024-05-24** to **2026-10-19**

## Latest Signals

| symbol     | date                |         close |   composite_score | signal   | data_source   |
|:-----------|:--------------------|--------------:|------------------:|:---------|:--------------|
| ABBV       | 2026-10-16 00:00:00 |   285.42      |         68.25     | LONG     | Yahoo Finance |
| AMGN       | 2026-10-16 00:00:00 |   432.49      |         65.4167   | LONG     | Yahoo Finance |
| CL         | 2026-10-16 00:00:00 |    94.11      |         54.75     | LONG     | Yahoo Finance |
| COP        | 2026-10-16 00:00:00 |   146.51      |         71.25     | LONG     | Yahoo Finance |
| COST       | 2026-10-16 00:00:00 |   989.11      |         67.5      | LONG     | Yahoo Finance |
| CRM        | 2026-10-16 00:00:00 |   240.7       |         71.5833   | LONG     | Yahoo Finance |
| CVX        | 2026-10-16 00:00:00 |   224.99      |         53.25     | LONG     | Yahoo Finance |
| DIS        | 2026-10-16 00:00:00 |   110.59      |         74.0833   | LONG     | Yahoo Finance |
| DXY-INDEX  | 2026-10-19 00:00:00 |   101.83      |         60.2151   | LONG     | Yahoo Finance |
| EOG        | 2026-10-16 00:00:00 |   158.01      |         74.75     | LONG     | Yahoo Finance |
| INTU       | 2026-10-16 00:00:00 |   325.15      |         41.75     | LONG     | Yahoo Finance |
| JPM        | 2026-10-16 00:00:00 |   339.72      |         51.9167   | LONG     | Yahoo Finance |
| KO         | 2026-10-16 00:00:00 |    93.9       |         73.25     | LONG     | Yahoo Finance |
| LIN        | 2026-10-16 00:00:00 |   498.43      |         68        | LONG     | Yahoo Finance |
| LLY        | 2026-10-16 00:00:00 |  1257.03      |         69.0833   | LONG     | Yahoo Finance |
| MPC        | 2026-10-16 00:00:00 |   478.07      |         73.25     | LONG     | Yahoo Finance |
| MSFT       | 2026-10-16 00:00:00 |   529.05      |         69.9167   | LONG     | Yahoo Finance |
| NEM        | 2026-10-16 00:00:00 |   118.6       |         31.0833   | LONG     | Yahoo Finance |
| OXY        | 2026-10-16 00:00:00 |    62.38      |         71.25     | LONG     | Yahoo Finance |
| PG         | 2026-10-16 00:00:00 |   159.35      |         81.25     | LONG     | Yahoo Finance |
| PM         | 2026-10-16 00:00:00 |   205.2       |         73.5833   | LONG     | Yahoo Finance |
| RTX        | 2026-10-16 00:00:00 |   193.92      |         41.1667   | LONG     | Yahoo Finance |
| TMO        | 2026-10-16 00:00:00 |   690         |         56.4167   | LONG     | Yahoo Finance |
| UNH        | 2026-10-16 00:00:00 |   401.43      |         72.0833   | LONG     | Yahoo Finance |
| WFC        | 2026-10-16 00:00:00 |    83.87      |         31.6667   | LONG     | Yahoo Finance |
| XLB        | 2026-10-16 00:00:00 |    50.92      |         55.6667   | LONG     | Yahoo Finance |
| XLE        | 2026-10-16 00:00:00 |    68.24      |         73.25     | LONG     | Yahoo Finance |
| XLF        | 2026-10-16 00:00:00 |    55.52      |         69.4167   | LONG     | Yahoo Finance |
| XLP        | 2026-10-16 00:00:00 |    87.62      |         58.25     | LONG     | Yahoo Finance |
| XOM        | 2026-10-16 00:00:00 |   178.98      |         55.25     | LONG     | Yahoo Finance |
| AAPL       | 2026-10-16 00:00:00 |   343.46      |         63.3333   | NEUTRAL  | Yahoo Finance |
| AAVE-USD   | 2026-10-19 00:00:00 |   151.34      |          9.33333  | NEUTRAL  | Kraken API    |
| ADA-USD    | 2026-10-19 00:00:00 |     0.220458  |        -58.8333   | NEUTRAL  | Kraken API    |
| ADBE       | 2026-10-16 00:00:00 |   245.2       |         12.4167   | NEUTRAL  | Yahoo Finance |
| AGG        | 2026-10-16 00:00:00 |    95.38      |         -1.08333  | NEUTRAL  | Yahoo Finance |
| ALGO-USD   | 2026-10-19 00:00:00 |     0.11091   |         21.9167   | NEUTRAL  | Kraken API    |
| AMD        | 2026-10-16 00:00:00 |   528.75      |         -5.41667  | NEUTRAL  | Yahoo Finance |
| AMZN       | 2026-10-16 00:00:00 |   250         |         22.9167   | NEUTRAL  | Yahoo Finance |
| APT-USD    | 2026-10-19 00:00:00 |     0.7738    |        -25.8333   | NEUTRAL  | Kraken API    |
| ARB-USD    | 2026-10-19 00:00:00 |     0.192     |         28.6667   | NEUTRAL  | Kraken API    |
| ARKK       | 2026-10-16 00:00:00 |    81.65      |        -25.25     | NEUTRAL  | Yahoo Finance |
| ATOM-USD   | 2026-10-19 00:00:00 |     1.6966    |        -37.8333   | NEUTRAL  | Kraken API    |
| AVAX-USD   | 2026-10-19 00:00:00 |     9.733     |          3.41667  | NEUTRAL  | Kraken API    |
| AVGO       | 2026-10-16 00:00:00 |   328.75      |        -66.1667   | NEUTRAL  | Yahoo Finance |
| BA         | 2026-10-16 00:00:00 |   190.21      |        -17.0833   | NEUTRAL  | Yahoo Finance |
| BCH-USD    | 2026-10-19 00:00:00 |   277.47      |        -15.5833   | NEUTRAL  | Kraken API    |
| BITO       | 2026-10-16 00:00:00 |    10.88      |         -8.91667  | NEUTRAL  | Yahoo Finance |
| BLK        | 2026-10-16 00:00:00 |  1134.38      |         66.3333   | NEUTRAL  | Yahoo Finance |
| BND        | 2026-10-16 00:00:00 |    70.82      |          6.41667  | NEUTRAL  | Yahoo Finance |
| BTC-USD    | 2026-10-19 00:00:00 | 82453.6       |         -1.91667  | NEUTRAL  | Kraken API    |
| CMCSA      | 2026-10-16 00:00:00 |    21.9       |        -13.5833   | NEUTRAL  | Yahoo Finance |
| COMP-USD   | 2026-10-19 00:00:00 |    21.45      |        -18.5833   | NEUTRAL  | Kraken API    |
| CRV-USD    | 2026-10-19 00:00:00 |     0.35428   |        -14.5833   | NEUTRAL  | Kraken API    |
| CSCO       | 2026-10-16 00:00:00 |   107.39      |         29.8333   | NEUTRAL  | Yahoo Finance |
| DASH-USD   | 2026-10-19 00:00:00 |    48.863     |        -22.6667   | NEUTRAL  | Kraken API    |
| DBC        | 2026-10-16 00:00:00 |    33.74      |         69.8333   | NEUTRAL  | Yahoo Finance |
| DE         | 2026-10-16 00:00:00 |   641.86      |        -12.3333   | NEUTRAL  | Yahoo Finance |
| DIA        | 2026-10-16 00:00:00 |   519.1       |         43.6667   | NEUTRAL  | Yahoo Finance |
| DOT-USD    | 2026-10-19 00:00:00 |     1.1155    |        -36.5833   | NEUTRAL  | Kraken API    |
| EFA        | 2026-10-16 00:00:00 |   103.55      |        -10.9167   | NEUTRAL  | Yahoo Finance |
| ETH-USD    | 2026-10-19 00:00:00 |  2420.88      |        -21.6667   | NEUTRAL  | Kraken API    |
| EWJ        | 2026-10-16 00:00:00 |    94.88      |        -26.5      | NEUTRAL  | Yahoo Finance |
| FCX        | 2026-10-16 00:00:00 |    69.54      |        -39.5      | NEUTRAL  | Yahoo Finance |
| FET-USD    | 2026-10-19 00:00:00 |     0.1885    |        -53.8333   | NEUTRAL  | Kraken API    |
| FIL-USD    | 2026-10-19 00:00:00 |     1.036     |         -2.58333  | NEUTRAL  | Kraken API    |
| FXI        | 2026-10-16 00:00:00 |    33.84      |        -37.1667   | NEUTRAL  | Yahoo Finance |
| GDX        | 2026-10-16 00:00:00 |    87.71      |        -22.8333   | NEUTRAL  | Yahoo Finance |
| GE         | 2026-10-16 00:00:00 |   313.83      |        -22.6667   | NEUTRAL  | Yahoo Finance |
| GLD        | 2026-10-16 00:00:00 |   382.01      |        -15.0833   | NEUTRAL  | Yahoo Finance |
| GOOGL      | 2026-10-16 00:00:00 |   340.59      |        -11.0833   | NEUTRAL  | Yahoo Finance |
| HD         | 2026-10-16 00:00:00 |   309.63      |         22.4167   | NEUTRAL  | Yahoo Finance |
| HON        | 2026-10-16 00:00:00 |   211.41      |         -3.25     | NEUTRAL  | Yahoo Finance |
| HYG        | 2026-10-16 00:00:00 |    76.86      |        -29.75     | NEUTRAL  | Yahoo Finance |
| IBIT       | 2026-10-16 00:00:00 |    46.15      |         20.0833   | NEUTRAL  | Yahoo Finance |
| IBM        | 2026-10-16 00:00:00 |   232.14      |         13.4167   | NEUTRAL  | Yahoo Finance |
| ICP-USD    | 2026-10-19 00:00:00 |     2.888     |        -32.5      | NEUTRAL  | Kraken API    |
| IEF        | 2026-10-16 00:00:00 |    90.42      |          6.41667  | NEUTRAL  | Yahoo Finance |
| INJ-USD    | 2026-10-19 00:00:00 |     8.506     |         59.3333   | NEUTRAL  | Kraken API    |
| INTC       | 2026-10-16 00:00:00 |    89.85      |        -12.3333   | NEUTRAL  | Yahoo Finance |
| ITA        | 2026-10-16 00:00:00 |   209.07      |        -21.75     | NEUTRAL  | Yahoo Finance |
| JNJ        | 2026-10-16 00:00:00 |   255.56      |        -41.0833   | NEUTRAL  | Yahoo Finance |
| LINK-USD   | 2026-10-19 00:00:00 |    12.1371    |        -20.5833   | NEUTRAL  | Kraken API    |
| LTC-USD    | 2026-10-19 00:00:00 |    59.1       |        -18.5833   | NEUTRAL  | Kraken API    |
| MCD        | 2026-10-16 00:00:00 |   242.97      |          1.08333  | NEUTRAL  | Yahoo Finance |
| META       | 2026-10-16 00:00:00 |   709.33      |         25.0833   | NEUTRAL  | Yahoo Finance |
| MRK        | 2026-10-16 00:00:00 |   145.95      |         16.6667   | NEUTRAL  | Yahoo Finance |
| MU         | 2026-10-16 00:00:00 |   878.84      |        -21.3333   | NEUTRAL  | Yahoo Finance |
| NEAR-USD   | 2026-10-19 00:00:00 |     5.0226    |         17.4167   | NEUTRAL  | Kraken API    |
| NFLX       | 2026-10-16 00:00:00 |    70.53      |          1.91667  | NEUTRAL  | Yahoo Finance |
| NKE        | 2026-10-16 00:00:00 |    37.13      |         -6.83333  | NEUTRAL  | Yahoo Finance |
| NOW        | 2026-10-16 00:00:00 |   141.97      |         60.3333   | NEUTRAL  | Yahoo Finance |
| OP-USD     | 2026-10-19 00:00:00 |     0.1243    |        -27.8333   | NEUTRAL  | Kraken API    |
| ORCL       | 2026-10-16 00:00:00 |   128.23      |        -45.5      | NEUTRAL  | Yahoo Finance |
| PEP        | 2026-10-16 00:00:00 |   131.49      |          4.41667  | NEUTRAL  | Yahoo Finance |
| PEPE-USD   | 2026-10-19 00:00:00 |     4.021e-06 |         -3.5      | NEUTRAL  | Kraken API    |
| PFE        | 2026-10-16 00:00:00 |    29.58      |         57.8333   | NEUTRAL  | Yahoo Finance |
| QCOM       | 2026-10-16 00:00:00 |   172.11      |        -49.8333   | NEUTRAL  | Yahoo Finance |
| QQQ        | 2026-10-16 00:00:00 |   709.8       |         -1.83333  | NEUTRAL  | Yahoo Finance |
| RENDER-USD | 2026-10-19 00:00:00 |     1.806     |          3.16667  | NEUTRAL  | Kraken API    |
| SBUX       | 2026-10-16 00:00:00 |    97.52      |          0.666667 | NEUTRAL  | Yahoo Finance |
| SHY        | 2026-10-16 00:00:00 |    81.36      |         11.1667   | NEUTRAL  | Yahoo Finance |
| SKY-USD    | 2026-10-19 00:00:00 |     0.06938   |        -11.5833   | NEUTRAL  | Kraken API    |
| SMH        | 2026-10-16 00:00:00 |   539.79      |        -10.0833   | NEUTRAL  | Yahoo Finance |
| SOXX       | 2026-10-16 00:00:00 |   493.39      |        -10.0833   | NEUTRAL  | Yahoo Finance |
| SPY        | 2026-10-16 00:00:00 |   763.25      |        -20.0833   | NEUTRAL  | Yahoo Finance |
| TGT        | 2026-10-16 00:00:00 |   154.26      |        -11.0833   | NEUTRAL  | Yahoo Finance |
| TIA-USD    | 2026-10-19 00:00:00 |     0.6108    |         65.1667   | NEUTRAL  | Kraken API    |
| TLT        | 2026-10-16 00:00:00 |    80.05      |         -3.08333  | NEUTRAL  | Yahoo Finance |
| TRX-USD    | 2026-10-19 00:00:00 |     0.330897  |        -26.4167   | NEUTRAL  | Kraken API    |
| TSLA       | 2026-10-16 00:00:00 |   354.72      |        -47.5833   | NEUTRAL  | Yahoo Finance |
| TXN        | 2026-10-16 00:00:00 |   276.48      |          7.91667  | NEUTRAL  | Yahoo Finance |
| UNI-USD    | 2026-10-19 00:00:00 |     7.2854    |        -17.9167   | NEUTRAL  | Kraken API    |
| UPS        | 2026-10-16 00:00:00 |    97.48      |          6.41667  | NEUTRAL  | Yahoo Finance |
| USO        | 2026-10-16 00:00:00 |   161.76      |         67.8333   | NEUTRAL  | Yahoo Finance |
| VIXY       | 2026-10-16 00:00:00 |    17.73      |          6.16667  | NEUTRAL  | Yahoo Finance |
| VNQ        | 2026-10-16 00:00:00 |    91.76      |          6.41667  | NEUTRAL  | Yahoo Finance |
| VTI        | 2026-10-16 00:00:00 |   374.07      |        -18.3333   | NEUTRAL  | Yahoo Finance |
| VWO        | 2026-10-16 00:00:00 |    58.03      |        -45        | NEUTRAL  | Yahoo Finance |
| WMT        | 2026-10-16 00:00:00 |   118.81      |         52.25     | NEUTRAL  | Yahoo Finance |
| XBI        | 2026-10-16 00:00:00 |   144.32      |        -25.25     | NEUTRAL  | Yahoo Finance |
| XLC        | 2026-10-16 00:00:00 |   110.32      |        -63.8333   | NEUTRAL  | Yahoo Finance |
| XLI        | 2026-10-16 00:00:00 |   167.76      |        -40.1667   | NEUTRAL  | Yahoo Finance |
| XLK        | 2026-10-16 00:00:00 |   183.47      |         -1.83333  | NEUTRAL  | Yahoo Finance |
| XLU        | 2026-10-16 00:00:00 |    42.21      |         28.25     | NEUTRAL  | Yahoo Finance |
| XLV        | 2026-10-16 00:00:00 |   176.71      |         57.8333   | NEUTRAL  | Yahoo Finance |
| XLY        | 2026-10-16 00:00:00 |   112.46      |          0.416667 | NEUTRAL  | Yahoo Finance |
| ZEC-USD    | 2026-10-19 00:00:00 |  1166.71      |        -21.6667   | NEUTRAL  | Kraken API    |
| AMAT       | 2026-10-16 00:00:00 |   409.29      |        -61.0833   | SHORT    | Yahoo Finance |
| BAC        | 2026-10-16 00:00:00 |    51.23      |        -35.3333   | SHORT    | Yahoo Finance |
| BONK-USD   | 2026-10-19 00:00:00 |     2.93e-06  |        -42.3333   | SHORT    | Kraken API    |
| C          | 2026-10-16 00:00:00 |   124.26      |        -50.3333   | SHORT    | Yahoo Finance |
| CAT        | 2026-10-16 00:00:00 |   730.76      |        -54.5833   | SHORT    | Yahoo Finance |
| DOGE-USD   | 2026-10-19 00:00:00 |     0.0793999 |        -51.3333   | SHORT    | Kraken API    |
| EEM        | 2026-10-16 00:00:00 |    62.85      |        -57.5833   | SHORT    | Yahoo Finance |
| ETC-USD    | 2026-10-19 00:00:00 |     7.756     |        -45.5833   | SHORT    | Kraken API    |
| GDXJ       | 2026-10-16 00:00:00 |   109.91      |        -45.3333   | SHORT    | Yahoo Finance |
| GRT-USD    | 2026-10-19 00:00:00 |     0.02376   |        -38.5833   | SHORT    | Kraken API    |
| GS         | 2026-10-16 00:00:00 |   881.26      |        -31.25     | SHORT    | Yahoo Finance |
| HBAR-USD   | 2026-10-19 00:00:00 |     0.08399   |        -53.3333   | SHORT    | Kraken API    |
| IEMG       | 2026-10-16 00:00:00 |    76.79      |        -55.8333   | SHORT    | Yahoo Finance |
| IWM        | 2026-10-16 00:00:00 |   270.44      |        -47.5      | SHORT    | Yahoo Finance |
| LDO-USD    | 2026-10-19 00:00:00 |     0.391     |        -48.25     | SHORT    | Kraken API    |
| LRCX       | 2026-10-16 00:00:00 |   263.94      |        -61.0833   | SHORT    | Yahoo Finance |
| MS         | 2026-10-16 00:00:00 |   180.57      |        -51.5833   | SHORT    | Yahoo Finance |
| NVDA       | 2026-10-16 00:00:00 |   214.13      |        -17.25     | SHORT    | Yahoo Finance |
| POL-USD    | 2026-10-19 00:00:00 |     0.0917    |        -47.5833   | SHORT    | Kraken API    |
| SCHW       | 2026-10-16 00:00:00 |    91.96      |        -32.5      | SHORT    | Yahoo Finance |
| SHIB-USD   | 2026-10-19 00:00:00 |     5e-06     |        -43.5833   | SHORT    | Kraken API    |
| SLB        | 2026-10-16 00:00:00 |    49.5       |        -30.75     | SHORT    | Yahoo Finance |
| SLV        | 2026-10-16 00:00:00 |    51.51      |        -56.0833   | SHORT    | Yahoo Finance |
| SNX-USD    | 2026-10-19 00:00:00 |     0.2135    |        -40.3333   | SHORT    | Kraken API    |
| SOL-USD    | 2026-10-19 00:00:00 |   105.19      |        -20.3333   | SHORT    | Kraken API    |
| SUSHI-USD  | 2026-10-19 00:00:00 |     0.2162    |        -44.25     | SHORT    | Kraken API    |
| T          | 2026-10-16 00:00:00 |    23.44      |        -52.3333   | SHORT    | Yahoo Finance |
| TMUS       | 2026-10-16 00:00:00 |   159.1       |        -46.25     | SHORT    | Yahoo Finance |
| VEA        | 2026-10-16 00:00:00 |    69.49      |        -31.25     | SHORT    | Yahoo Finance |
| VZ         | 2026-10-16 00:00:00 |    44.79      |        -44.5833   | SHORT    | Yahoo Finance |
| WIF-USD    | 2026-10-19 00:00:00 |     0.1989    |        -47.5833   | SHORT    | Kraken API    |
| XLM-USD    | 2026-10-19 00:00:00 |     0.178756  |        -49.3333   | SHORT    | Kraken API    |
| XRP-USD    | 2026-10-19 00:00:00 |     1.30981   |        -43.5833   | SHORT    | Kraken API    |
| YFI-USD    | 2026-10-19 00:00:00 |  2235.9       |        -45.5833   | SHORT    | Kraken API    |

## Edge Summary

- Symbols with trades: **161** of 161
- Beat buy-and-hold: **32.92%** of traded symbols
- Positive return: **32.30%** of traded symbols
- Median strategy return: **-8.80%** (benchmark **20.02%**)
- Median excess vs benchmark: **-24.46%**
- Median Sharpe: **-0.07**
- Median exposure: **44.09%**

> Edge is real only if both _beat buy-and-hold_ and _median excess_ are convincingly positive across many symbols. Treat a single high-return symbol as noise.

## Portfolio Backtest

Actual capital-allocation books (not per-symbol averages). Benchmarks: `equal_weight_buyhold` (whole tracked universe), `spy_buyhold` (100% SPY), and `sixty_forty` (60% SPY / 40% AGG). `high_conf_voltarget` inverse-vol-weights the HIGH-confidence book; `conviction_long_short` is market-neutral. Judge on **Sharpe** and **max_drawdown** out-of-sample, not raw return: a fully-invested long book wins on return in a bull market but carries all the risk.

| strategy              | scope         | ann_return   | ann_vol   |   sharpe | max_drawdown   | total_return   |   avg_gross_exposure |
|:----------------------|:--------------|:-------------|:----------|---------:|:---------------|:---------------|---------------------:|
| equal_weight_buyhold  | full          | 11.52%       | 28.48%    |     0.4  | -39.53%        | 25.53%         |                 1    |
| equal_weight_buyhold  | out_of_sample | 14.37%       | 27.70%    |     0.52 | -18.71%        | 11.92%         |                 1    |
| all_signals_ew        | full          | -14.40%      | 24.29%    |    -0.59 | -55.91%        | -41.08%        |                 1    |
| all_signals_ew        | out_of_sample | 5.63%        | 23.56%    |     0.24 | -23.19%        | 3.11%          |                 1    |
| high_conf_ew          | full          | -4.03%       | 31.59%    |    -0.13 | -44.86%        | -23.89%        |                 0.9  |
| high_conf_ew          | out_of_sample | 11.35%       | 28.72%    |     0.4  | -22.85%        | 7.94%          |                 0.9  |
| high_conf_voltarget   | full          | -5.69%       | 28.35%    |    -0.2  | -40.05%        | -25.44%        |                 0.9  |
| high_conf_voltarget   | out_of_sample | 0.74%        | 23.95%    |     0.03 | -17.69%        | -2.33%         |                 0.9  |
| conviction_long_short | full          | -13.41%      | 22.16%    |    -0.61 | -46.17%        | -38.37%        |                 0.97 |
| conviction_long_short | out_of_sample | -1.53%       | 19.61%    |    -0.08 | -26.77%        | -3.61%         |                 0.97 |
| spy_buyhold           | full          | 5.13%        | 13.64%    |     0.38 | -19.00%        | 13.67%         |                 0.78 |
| spy_buyhold           | out_of_sample | -0.91%       | 9.96%     |    -0.09 | -12.06%        | -1.48%         |                 0.78 |
| sixty_forty           | full          | 2.74%        | 8.60%     |     0.32 | -11.66%        | 7.49%          |                 0.78 |
| sixty_forty           | out_of_sample | -2.61%       | 6.69%     |    -0.39 | -8.26%         | -2.98%         |                 0.78 |

## Walk-Forward Robustness

Each book measured across contiguous time folds (each a different regime). A book has durable edge only if `mean_sharpe` is positive, `min_sharpe` isn't deeply negative, and `pct_positive_folds` is high — a single great fold doesn't count. `fold_sharpes` lists each fold oldest-to-newest.

| strategy              |   n_folds |   mean_sharpe |   median_sharpe |   min_sharpe | pct_positive_folds   | mean_return   | fold_sharpes                 |
|:----------------------|----------:|--------------:|----------------:|-------------:|:---------------------|:--------------|:-----------------------------|
| equal_weight_buyhold  |         5 |          0.61 |            0.99 |        -0.69 | 60.00%               | 6.03%         | 0.99;1.62;-0.69;-0.08;1.20   |
| all_signals_ew        |         5 |         -0.65 |           -0.5  |        -1.97 | 20.00%               | -8.49%        | -1.49;-0.42;-1.97;1.15;-0.50 |
| high_conf_ew          |         5 |         -0.01 |            0    |        -1.14 | 60.00%               | -3.82%        | 0.04;-0.20;-1.14;1.26;0.00   |
| high_conf_voltarget   |         5 |         -0.06 |           -0.16 |        -1.04 | 40.00%               | -4.74%        | 0.24;-0.16;-1.04;0.85;-0.20  |
| conviction_long_short |         5 |         -0.6  |           -0.63 |        -1.96 | 40.00%               | -8.79%        | -1.96;0.24;-0.76;-0.63;0.14  |
| spy_buyhold           |         5 |          0.33 |            0.26 |        -0.37 | 60.00%               | 2.72%         | 1.44;0.26;-0.34;0.66;-0.37   |
| sixty_forty           |         5 |          0.26 |            0.23 |        -0.53 | 60.00%               | 1.50%         | 1.38;0.30;-0.09;0.23;-0.53   |

## Strategy Comparison

Each decision rule backtested over the same data. `out_of_sample` is the most recent ~35% of each symbol's history (unseen tail). A rule has real edge only if `median_excess` and `beat_benchmark_pct` stay positive out-of-sample, not just full-sample.

| strategy        | scope         |   symbols | beat_benchmark_pct   | positive_pct   | median_return   | median_benchmark   | median_excess   |   median_sharpe |   total_trades |
|:----------------|:--------------|----------:|:---------------------|:---------------|:----------------|:-------------------|:----------------|----------------:|---------------:|
| trend           | full          |       161 | 32.92%               | 32.30%         | -8.80%          | 20.02%             | -24.46%         |           -0.07 |          11328 |
| trend           | out_of_sample |       161 | 27.33%               | 52.80%         | 0.19%           | 7.66%              | -14.81%         |            0.1  |           3810 |
| mean_reversion  | full          |       157 | 38.85%               | 48.41%         | -0.23%          | 18.14%             | -16.28%         |           -0.01 |           1228 |
| mean_reversion  | out_of_sample |       120 | 31.67%               | 51.67%         | 0.26%           | 6.37%              | -7.43%          |            0.13 |            474 |
| regime_adaptive | full          |       161 | 34.16%               | 32.30%         | -8.96%          | 20.02%             | -23.91%         |           -0.1  |          11597 |
| regime_adaptive | out_of_sample |       161 | 27.95%               | 52.80%         | 0.19%           | 7.66%              | -14.81%         |            0.09 |           3916 |

## Signal Calibration

Realized forward return in the signal's direction, grouped by confidence. HIGH should outrank LOW for the confidence score to be meaningful.

| confidence_level   |   horizon |     n | mean_return   | median_return   | win_rate   |
|:-------------------|----------:|------:|:--------------|:----------------|:-----------|
| HIGH               |         5 |  7886 | 0.21%         | 0.05%           | 50.91%     |
| MEDIUM             |         5 | 29075 | 0.05%         | 0.04%           | 50.42%     |
| LOW                |         5 |  3530 | -0.36%        | -0.39%          | 46.29%     |
| ALL                |         5 | 40491 | 0.05%         | 0.02%           | 50.15%     |
| HIGH               |        10 |  7846 | 0.44%         | 0.07%           | 50.80%     |
| MEDIUM             |        10 | 28851 | 0.16%         | 0.05%           | 50.39%     |
| LOW                |        10 |  3470 | -0.71%        | -0.50%          | 46.74%     |
| ALL                |        10 | 40167 | 0.14%         | 0.02%           | 50.15%     |
| HIGH               |        20 |  7749 | 1.00%         | 0.28%           | 52.25%     |
| MEDIUM             |        20 | 28274 | 0.89%         | 0.57%           | 53.21%     |
| LOW                |        20 |  3380 | -0.39%        | -0.52%          | 47.40%     |
| ALL                |        20 | 39403 | 0.80%         | 0.44%           | 52.52%     |

## Backtest Summary

### Data Quality / Signal Availability

- **ok**: 161 symbols

| symbol     |   trades | return   | benchmark_return   | mdd     |   sharpe | exposure   | skipped_reason   |
|:-----------|---------:|:---------|:-------------------|:--------|---------:|:-----------|:-----------------|
| AAPL       |       63 | 7.49%    | 80.79%             | -20.65% |     0.25 | 50.42%     | ok               |
| AAVE-USD   |       65 | -37.11%  | -34.64%            | -66.17% |    -0.22 | 41.38%     | ok               |
| ABBV       |       70 | -21.44%  | 81.73%             | -30.52% |    -0.44 | 48.42%     | ok               |
| ADA-USD    |       76 | -31.23%  | -70.96%            | -52.70% |    -0.2  | 45.21%     | ok               |
| ADBE       |       71 | -11.61%  | -48.43%            | -31.20% |    -0.03 | 56.91%     | ok               |
| AGG        |       67 | -6.96%   | -1.24%             | -11.29% |    -1.1  | 33.28%     | ok               |
| ALGO-USD   |       76 | -27.99%  | -50.30%            | -39.25% |    -0.16 | 40.04%     | ok               |
| AMAT       |       73 | -35.56%  | 85.29%             | -53.91% |    -0.32 | 51.41%     | ok               |
| AMD        |       56 | 17.30%   | 217.83%            | -41.09% |     0.37 | 37.27%     | ok               |
| AMGN       |       67 | -12.56%  | 41.41%             | -34.19% |    -0.2  | 50.92%     | ok               |
| AMZN       |       80 | -55.73%  | 38.31%             | -56.19% |    -1.6  | 41.26%     | ok               |
| APT-USD    |       70 | -23.20%  | -85.30%            | -56.73% |    -0    | 39.66%     | ok               |
| ARB-USD    |       75 | -4.93%   | -50.74%            | -48.19% |     0.23 | 43.10%     | ok               |
| ARKK       |       89 | -30.46%  | 83.98%             | -34.52% |    -0.47 | 43.59%     | ok               |
| ATOM-USD   |       92 | -60.19%  | -64.83%            | -59.30% |    -0.87 | 48.08%     | ok               |
| AVAX-USD   |       66 | -32.18%  | -57.85%            | -45.41% |    -0.24 | 39.66%     | ok               |
| AVGO       |       64 | 16.30%   | 133.51%            | -36.09% |     0.35 | 41.26%     | ok               |
| BA         |       67 | 11.04%   | 8.99%              | -24.47% |     0.3  | 51.25%     | ok               |
| BAC        |       74 | -5.04%   | 29.04%             | -20.18% |    -0.06 | 48.75%     | ok               |
| BCH-USD    |       78 | 3.80%    | -29.92%            | -53.87% |     0.25 | 48.47%     | ok               |
| BITO       |       79 | -24.21%  | -61.24%            | -43.10% |    -0.17 | 41.43%     | ok               |
| BLK        |       83 | -12.59%  | 45.08%             | -26.90% |    -0.29 | 46.76%     | ok               |
| BND        |       66 | -6.57%   | -1.19%             | -10.80% |    -1    | 34.94%     | ok               |
| BONK-USD   |       72 | 55.64%   | -84.99%            | -43.77% |     0.65 | 45.59%     | ok               |
| BTC-USD    |       72 | 4.62%    | -20.33%            | -23.38% |     0.21 | 51.34%     | ok               |
| C          |       77 | -34.54%  | 95.44%             | -39.51% |    -0.74 | 46.09%     | ok               |
| CAT        |       70 | 6.97%    | 109.45%            | -21.87% |     0.24 | 48.09%     | ok               |
| CL         |       66 | 0.11%    | 0.87%              | -14.32% |     0.07 | 38.60%     | ok               |
| CMCSA      |       86 | -39.01%  | -39.37%            | -47.69% |    -0.96 | 43.59%     | ok               |
| COMP-USD   |       97 | -37.68%  | -53.30%            | -55.77% |    -0.21 | 49.81%     | ok               |
| COP        |       68 | -9.39%   | 24.96%             | -41.35% |    -0.07 | 44.09%     | ok               |
| COST       |       60 | -0.40%   | 22.15%             | -31.32% |     0.05 | 41.10%     | ok               |
| CRM        |       67 | -31.30%  | -11.60%            | -44.41% |    -0.43 | 46.76%     | ok               |
| CRV-USD    |       64 | 42.17%   | -49.17%            | -39.89% |     0.58 | 36.40%     | ok               |
| CSCO       |       63 | 11.24%   | 131.34%            | -22.26% |     0.31 | 49.92%     | ok               |
| CVX        |       73 | -11.25%  | 42.62%             | -27.78% |    -0.22 | 42.26%     | ok               |
| DASH-USD   |       53 | -0.66%   | 108.48%            | -64.43% |     0.38 | 29.89%     | ok               |
| DBC        |       66 | -8.16%   | 43.45%             | -24.10% |    -0.21 | 35.27%     | ok               |
| DE         |       70 | -12.17%  | 71.18%             | -23.98% |    -0.18 | 44.26%     | ok               |
| DIA        |       66 | -5.01%   | 32.88%             | -12.94% |    -0.24 | 43.43%     | ok               |
| DIS        |       64 | -5.66%   | 8.68%              | -28.17% |    -0.04 | 43.59%     | ok               |
| DOGE-USD   |       67 | -19.11%  | -64.10%            | -60.95% |     0.01 | 48.66%     | ok               |
| DOT-USD    |       84 | -48.42%  | -76.56%            | -63.33% |    -0.37 | 47.70%     | ok               |
| DXY-INDEX  |       38 | -0.89%   | -4.80%             | -6.02%  |    -0.12 | 32.25%     | ok               |
| EEM        |       64 | -10.11%  | 46.09%             | -23.94% |    -0.27 | 39.77%     | ok               |
| EFA        |       68 | -11.28%  | 27.76%             | -13.15% |    -0.44 | 41.26%     | ok               |
| EOG        |       80 | -28.64%  | 28.18%             | -47.87% |    -0.6  | 45.09%     | ok               |
| ETC-USD    |       56 | -15.00%  | -58.63%            | -45.54% |    -0.07 | 31.80%     | ok               |
| ETH-USD    |       58 | 142.75%  | -4.59%             | -30.11% |     1.31 | 47.32%     | ok               |
| EWJ        |       62 | -22.99%  | 38.59%             | -29.40% |    -0.8  | 36.44%     | ok               |
| FCX        |       65 | -29.37%  | 34.95%             | -46.84% |    -0.32 | 44.26%     | ok               |
| FET-USD    |       79 | -46.79%  | -75.34%            | -65.38% |    -0.29 | 42.34%     | ok               |
| FIL-USD    |       65 | -40.15%  | -64.07%            | -58.54% |    -0.34 | 37.16%     | ok               |
| FXI        |       50 | -5.13%   | 22.70%             | -24.33% |    -0.05 | 30.78%     | ok               |
| GDX        |       62 | 2.01%    | 148.75%            | -33.31% |     0.17 | 44.43%     | ok               |
| GDXJ       |       72 | -35.03%  | 146.43%            | -40.39% |    -0.44 | 43.09%     | ok               |
| GE         |       76 | -8.43%   | 87.55%             | -27.82% |    -0.04 | 48.09%     | ok               |
| GLD        |       50 | 13.30%   | 76.92%             | -13.87% |     0.39 | 45.76%     | ok               |
| GOOGL      |       57 | 57.55%   | 94.63%             | -17.54% |     1.01 | 47.09%     | ok               |
| GRT-USD    |       79 | 65.12%   | -78.46%            | -33.74% |     0.74 | 45.79%     | ok               |
| GS         |       70 | -2.87%   | 91.09%             | -21.94% |     0.04 | 48.09%     | ok               |
| HBAR-USD   |       40 | -42.37%  | -18.56%            | -56.47% |    -0.9  | 38.81%     | ok               |
| HD         |       67 | 1.72%    | -4.76%             | -17.15% |     0.13 | 43.59%     | ok               |
| HON        |       93 | -26.93%  | 7.10%              | -33.87% |    -0.67 | 54.91%     | ok               |
| HYG        |       85 | -6.78%   | -0.30%             | -10.59% |    -0.75 | 39.27%     | ok               |
| IBIT       |       40 | 36.51%   | 21.42%             | -18.95% |     0.67 | 34.95%     | ok               |
| IBM        |       69 | -25.12%  | 35.84%             | -48.94% |    -0.3  | 48.92%     | ok               |
| ICP-USD    |       77 | -14.23%  | -45.07%            | -44.07% |     0.13 | 39.08%     | ok               |
| IEF        |       78 | -10.28%  | -2.65%             | -13.34% |    -1.4  | 33.78%     | ok               |
| IEMG       |       62 | -9.83%   | 42.15%             | -27.35% |    -0.28 | 39.93%     | ok               |
| INJ-USD    |       63 | -30.06%  | -28.92%            | -69.14% |    -0.06 | 40.04%     | ok               |
| INTC       |       68 | 40.26%   | 192.48%            | -60.60% |     0.53 | 48.09%     | ok               |
| INTU       |       73 | 1.22%    | -46.43%            | -37.50% |     0.15 | 46.92%     | ok               |
| ITA        |       78 | -3.36%   | 54.24%             | -23.75% |    -0.02 | 48.25%     | ok               |
| IWM        |       56 | 8.70%    | 31.64%             | -10.83% |     0.37 | 34.11%     | ok               |
| JNJ        |       58 | 10.08%   | 73.89%             | -16.86% |     0.41 | 46.59%     | ok               |
| JPM        |       73 | -23.32%  | 69.26%             | -32.74% |    -0.65 | 44.59%     | ok               |
| KO         |       54 | 27.65%   | 51.45%             | -8.64%  |     0.96 | 36.77%     | ok               |
| LDO-USD    |       72 | 44.08%   | -59.44%            | -50.47% |     0.59 | 46.93%     | ok               |
| LIN        |       74 | -10.02%  | 14.43%             | -20.61% |    -0.31 | 38.60%     | ok               |
| LINK-USD   |       64 | 56.97%   | -22.95%            | -33.64% |     0.71 | 44.44%     | ok               |
| LLY        |       80 | -33.14%  | 55.68%             | -53.42% |    -0.53 | 49.25%     | ok               |
| LRCX       |       80 | -30.42%  | 171.94%            | -60.58% |    -0.24 | 42.60%     | ok               |
| LTC-USD    |       67 | 3.80%    | -40.58%            | -30.78% |     0.24 | 51.92%     | ok               |
| MCD        |       79 | -3.15%   | -5.87%             | -21.88% |    -0.06 | 40.60%     | ok               |
| META       |       72 | -27.93%  | 48.33%             | -44.52% |    -0.39 | 50.42%     | ok               |
| MPC        |       72 | 21.37%   | 168.88%            | -34.29% |     0.45 | 52.41%     | ok               |
| MRK        |       67 | -23.98%  | 12.71%             | -35.95% |    -0.46 | 42.60%     | ok               |
| MS         |       75 | -4.27%   | 82.45%             | -27.79% |    -0.02 | 48.25%     | ok               |
| MSFT       |       83 | -26.92%  | 22.99%             | -39.15% |    -0.58 | 51.41%     | ok               |
| MU         |       51 | 136.57%  | 578.69%            | -68.76% |     0.98 | 52.25%     | ok               |
| NEAR-USD   |       69 | 172.52%  | 79.64%             | -46.60% |     1.12 | 44.06%     | ok               |
| NEM        |       70 | -24.88%  | 182.52%            | -39.56% |    -0.23 | 49.92%     | ok               |
| NFLX       |       78 | 3.93%    | 9.05%              | -21.09% |     0.18 | 52.58%     | ok               |
| NKE        |       81 | -30.33%  | -59.53%            | -55.35% |    -0.36 | 47.09%     | ok               |
| NOW        |       80 | 11.00%   | -3.88%             | -30.43% |     0.3  | 50.25%     | ok               |
| NVDA       |       77 | -50.14%  | 87.42%             | -53.41% |    -0.72 | 55.61%     | ok               |
| OP-USD     |       70 | -41.46%  | -82.46%            | -58.87% |    -0.33 | 33.14%     | ok               |
| ORCL       |       62 | 88.09%   | 4.33%              | -30.61% |     0.81 | 51.75%     | ok               |
| OXY        |       73 | 3.04%    | 0.69%              | -28.48% |     0.18 | 42.76%     | ok               |
| PEP        |       76 | 0.17%    | -26.13%            | -21.35% |     0.08 | 45.42%     | ok               |
| PEPE-USD   |       81 | -50.17%  | -68.10%            | -61.29% |    -0.34 | 47.51%     | ok               |
| PFE        |       79 | -34.49%  | 2.42%              | -41.77% |    -1.08 | 36.44%     | ok               |
| PG         |       66 | -21.40%  | -3.62%             | -24.16% |    -0.84 | 34.44%     | ok               |
| PM         |       79 | -7.46%   | 105.34%            | -35.15% |    -0.08 | 49.75%     | ok               |
| POL-USD    |       77 | 52.93%   | -61.62%            | -38.69% |     0.68 | 49.62%     | ok               |
| QCOM       |       77 | -31.01%  | -18.18%            | -56.59% |    -0.28 | 43.09%     | ok               |
| QQQ        |       66 | 5.57%    | 55.00%             | -14.20% |     0.22 | 45.76%     | ok               |
| RENDER-USD |       90 | -21.39%  | -61.00%            | -44.65% |     0.05 | 47.51%     | ok               |
| RTX        |       66 | 26.94%   | 82.48%             | -16.99% |     0.63 | 51.75%     | ok               |
| SBUX       |       60 | -14.73%  | 23.65%             | -29.22% |    -0.24 | 38.77%     | ok               |
| SCHW       |       82 | -15.32%  | 27.25%             | -31.92% |    -0.32 | 46.26%     | ok               |
| SHIB-USD   |       79 | -30.30%  | -65.66%            | -46.79% |    -0.24 | 52.49%     | ok               |
| SHY        |       48 | -1.87%   | -0.01%             | -3.30%  |    -0.63 | 36.94%     | ok               |
| SKY-USD    |       89 | -62.50%  | -8.20%             | -64.20% |    -1.05 | 43.10%     | ok               |
| SLB        |       75 | -41.88%  | 7.05%              | -59.65% |    -0.82 | 49.25%     | ok               |
| SLV        |       68 | 14.26%   | 85.69%             | -42.60% |     0.35 | 40.10%     | ok               |
| SMH        |       48 | 43.66%   | 120.99%            | -33.66% |     0.73 | 43.43%     | ok               |
| SNX-USD    |       62 | -4.03%   | -72.80%            | -50.74% |     0.17 | 34.10%     | ok               |
| SOL-USD    |       77 | -17.60%  | -37.20%            | -44.99% |     0.02 | 59.39%     | ok               |
| SOXX       |       56 | 55.30%   | 106.82%            | -40.14% |     0.82 | 42.76%     | ok               |
| SPY        |       64 | -0.06%   | 44.16%             | -15.53% |     0.06 | 49.08%     | ok               |
| SUSHI-USD  |       94 | -69.80%  | -70.22%            | -76.07% |    -1    | 39.46%     | ok               |
| T          |       72 | 41.56%   | 33.94%             | -17.01% |     0.83 | 56.74%     | ok               |
| TGT        |       60 | -11.06%  | 6.22%              | -34.42% |    -0.16 | 37.60%     | ok               |
| TIA-USD    |       91 | -39.58%  | -77.21%            | -75.93% |    -0.12 | 42.91%     | ok               |
| TLT        |       68 | -19.87%  | -12.40%            | -21.85% |    -1.49 | 33.44%     | ok               |
| TMO        |       69 | 29.81%   | 18.14%             | -18.85% |     0.62 | 55.24%     | ok               |
| TMUS       |       74 | -4.78%   | -4.16%             | -33.01% |    -0    | 48.25%     | ok               |
| TRX-USD    |       66 | 1.50%    | 21.84%             | -22.90% |     0.13 | 50.00%     | ok               |
| TSLA       |       78 | -35.00%  | 97.90%             | -59.64% |    -0.22 | 42.76%     | ok               |
| TXN        |       77 | -27.00%  | 38.81%             | -46.62% |    -0.3  | 50.42%     | ok               |
| UNH        |       77 | 32.94%   | -21.00%            | -26.31% |     0.55 | 48.42%     | ok               |
| UNI-USD    |       86 | -27.77%  | 20.02%             | -65.36% |    -0.01 | 49.43%     | ok               |
| UPS        |       72 | -38.26%  | -29.70%            | -40.10% |    -0.78 | 42.43%     | ok               |
| USO        |       67 | -12.16%  | 114.68%            | -46.69% |    -0.05 | 33.44%     | ok               |
| VEA        |       64 | -3.80%   | 37.09%             | -17.27% |    -0.11 | 42.26%     | ok               |
| VIXY       |       94 | -78.70%  | -60.21%            | -88.17% |    -0.96 | 31.95%     | ok               |
| VNQ        |       73 | -13.66%  | 12.09%             | -24.92% |    -0.54 | 39.77%     | ok               |
| VTI        |       68 | -7.39%   | 42.85%             | -17.64% |    -0.21 | 49.08%     | ok               |
| VWO        |       80 | -18.02%  | 31.29%             | -25.20% |    -0.68 | 40.10%     | ok               |
| VZ         |       84 | -25.84%  | 12.71%             | -29.49% |    -0.8  | 42.10%     | ok               |
| WFC        |       80 | -17.86%  | 39.30%             | -28.90% |    -0.3  | 46.76%     | ok               |
| WIF-USD    |       66 | -27.56%  | -80.19%            | -52.76% |    -0.02 | 38.12%     | ok               |
| WMT        |       69 | 4.00%    | 81.72%             | -25.37% |     0.18 | 48.59%     | ok               |
| XBI        |       62 | -1.06%   | 62.47%             | -17.92% |     0.06 | 38.60%     | ok               |
| XLB        |       68 | -13.20%  | 11.47%             | -24.18% |    -0.47 | 31.61%     | ok               |
| XLC        |       61 | 12.47%   | 33.00%             | -12.33% |     0.47 | 49.92%     | ok               |
| XLE        |       69 | -1.23%   | 49.37%             | -29.67% |     0.06 | 45.76%     | ok               |
| XLF        |       84 | -8.80%   | 33.43%             | -23.61% |    -0.27 | 46.42%     | ok               |
| XLI        |       82 | -10.04%  | 34.79%             | -17.79% |    -0.35 | 42.76%     | ok               |
| XLK        |       44 | 46.74%   | 70.52%             | -14.75% |     0.94 | 45.92%     | ok               |
| XLM-USD    |       68 | 8.66%    | -39.02%            | -54.58% |     0.31 | 47.70%     | ok               |
| XLP        |       67 | 8.59%    | 13.64%             | -10.28% |     0.5  | 38.44%     | ok               |
| XLU        |       69 | -5.20%   | 18.07%             | -20.40% |    -0.18 | 39.27%     | ok               |
| XLV        |       76 | -21.39%  | 22.36%             | -22.75% |    -1.03 | 36.44%     | ok               |
| XLY        |       75 | -4.15%   | 28.13%             | -18.35% |    -0.06 | 47.59%     | ok               |
| XOM        |       57 | 4.18%    | 57.80%             | -20.29% |     0.19 | 34.44%     | ok               |
| XRP-USD    |       66 | 7.40%    | -44.97%            | -33.91% |     0.28 | 36.40%     | ok               |
| YFI-USD    |       76 | -59.62%  | -60.72%            | -60.97% |    -1.09 | 37.16%     | ok               |
| ZEC-USD    |       57 | 160.57%  | 2780.05%           | -56.50% |     0.95 | 40.61%     | ok               |

## AAPL Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 14.21%   | 80.79%             | -21.71% |     0.36 |       72 | 55.24%     | ok               |
|          15 | 11.27%   | 80.79%             | -23.86% |     0.31 |       81 | 62.56%     | ok               |
|          30 | 7.49%    | 80.79%             | -20.65% |     0.25 |       63 | 50.42%     | ok               |
|          35 | 5.95%    | 80.79%             | -22.04% |     0.22 |       63 | 49.08%     | ok               |
|          25 | 3.14%    | 80.79%             | -20.87% |     0.17 |       73 | 52.58%     | ok               |

## AAVE-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 23.38%   | -34.64%            | -43.61% |     0.44 |       43 | 35.82%     | ok               |
|          45 | 11.89%   | -34.64%            | -49.19% |     0.33 |       48 | 30.65%     | ok               |
|          35 | 7.63%    | -34.64%            | -48.79% |     0.3  |       51 | 38.89%     | ok               |
|          50 | 6.87%    | -34.64%            | -45.07% |     0.27 |       46 | 22.99%     | ok               |
|          15 | -38.75%  | -34.64%            | -61.76% |    -0.16 |       72 | 54.21%     | ok               |

## ABBV Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -5.76%   | 81.73%             | -23.85% |    -0.07 |       54 | 35.27%     | ok               |
|          20 | -18.36%  | 81.73%             | -28.73% |    -0.35 |       66 | 51.75%     | ok               |
|          25 | -18.46%  | 81.73%             | -30.04% |    -0.36 |       69 | 50.25%     | ok               |
|          40 | -19.26%  | 81.73%             | -27.36% |    -0.43 |       70 | 40.77%     | ok               |
|          30 | -21.44%  | 81.73%             | -30.52% |    -0.44 |       70 | 48.42%     | ok               |

## ADA-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 21.61%   | -70.96%            | -34.64% |     0.44 |       46 | 30.84%     | ok               |
|          50 | 14.66%   | -70.96%            | -35.54% |     0.36 |       48 | 26.44%     | ok               |
|          40 | 0.87%    | -70.96%            | -40.73% |     0.22 |       58 | 36.78%     | ok               |
|          15 | -17.54%  | -70.96%            | -47.27% |     0.1  |       71 | 61.11%     | ok               |
|          35 | -11.39%  | -70.96%            | -44.07% |     0.08 |       64 | 40.61%     | ok               |

## ADBE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | 6.66%    | -48.43%            | -29.07% |     0.24 |       55 | 61.06%     | ok               |
|          35 | -3.98%   | -48.43%            | -31.73% |     0.06 |       78 | 48.25%     | ok               |
|          20 | -7.31%   | -48.43%            | -31.52% |     0.05 |       61 | 64.06%     | ok               |
|          30 | -11.61%  | -48.43%            | -31.20% |    -0.03 |       71 | 56.91%     | ok               |
|          15 | -14.48%  | -48.43%            | -34.98% |    -0.05 |       64 | 65.72%     | ok               |

## AGG Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -6.96%   | -1.24%             | -11.29% |    -1.1  |       67 | 33.28%     | ok               |
|          45 | -6.25%   | -1.24%             | -9.79%  |    -1.15 |       62 | 24.13%     | ok               |
|          25 | -8.10%   | -1.24%             | -12.28% |    -1.21 |       71 | 36.44%     | ok               |
|          35 | -7.63%   | -1.24%             | -11.92% |    -1.24 |       64 | 30.12%     | ok               |
|          20 | -8.76%   | -1.24%             | -11.89% |    -1.25 |       72 | 38.44%     | ok               |

## ALGO-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -27.99%  | -50.30%            | -39.25% |    -0.16 |       76 | 40.04%     | ok               |
|          25 | -37.21%  | -50.30%            | -51.92% |    -0.28 |       78 | 44.83%     | ok               |
|          15 | -41.12%  | -50.30%            | -51.37% |    -0.31 |       75 | 50.96%     | ok               |
|          35 | -40.58%  | -50.30%            | -52.80% |    -0.46 |       64 | 34.87%     | ok               |
|          20 | -48.39%  | -50.30%            | -53.71% |    -0.47 |       79 | 47.89%     | ok               |

## AMAT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -31.19%  | 85.29%             | -53.90% |    -0.2  |       74 | 60.57%     | ok               |
|          50 | -27.93%  | 85.29%             | -41.04% |    -0.25 |       52 | 36.11%     | ok               |
|          35 | -30.77%  | 85.29%             | -47.88% |    -0.26 |       73 | 48.75%     | ok               |
|          30 | -35.56%  | 85.29%             | -53.91% |    -0.32 |       73 | 51.41%     | ok               |
|          40 | -36.41%  | 85.29%             | -50.74% |    -0.37 |       71 | 43.93%     | ok               |

## AMD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 27.96%   | 217.83%            | -39.92% |     0.46 |       56 | 32.28%     | ok               |
|          40 | 17.30%   | 217.83%            | -41.09% |     0.37 |       56 | 37.27%     | ok               |
|          35 | 12.27%   | 217.83%            | -43.15% |     0.33 |       64 | 38.94%     | ok               |
|          45 | 2.14%    | 217.83%            | -49.59% |     0.23 |       62 | 35.11%     | ok               |
|          30 | -2.54%   | 217.83%            | -49.79% |     0.2  |       65 | 41.43%     | ok               |

## AMGN Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -7.65%   | 41.41%             | -26.65% |    -0.06 |       66 | 56.57%     | ok               |
|          35 | -10.36%  | 41.41%             | -31.29% |    -0.15 |       69 | 47.59%     | ok               |
|          15 | -13.10%  | 41.41%             | -27.98% |    -0.18 |       63 | 60.73%     | ok               |
|          30 | -12.56%  | 41.41%             | -34.19% |    -0.2  |       67 | 50.92%     | ok               |
|          25 | -14.36%  | 41.41%             | -33.47% |    -0.23 |       63 | 53.08%     | ok               |

## AMZN Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -27.97%  | 38.31%             | -29.61% |    -0.85 |       56 | 29.95%     | ok               |
|          50 | -31.74%  | 38.31%             | -33.91% |    -1.16 |       50 | 22.80%     | ok               |
|          45 | -37.46%  | 38.31%             | -38.25% |    -1.34 |       58 | 26.46%     | ok               |
|          35 | -52.04%  | 38.31%             | -52.54% |    -1.53 |       77 | 35.27%     | ok               |
|          30 | -55.73%  | 38.31%             | -56.19% |    -1.6  |       80 | 41.26%     | ok               |

## APT-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 25.37%   | -85.30%            | -31.21% |     0.52 |       42 | 16.28%     | ok               |
|          20 | 0.36%    | -85.30%            | -56.22% |     0.28 |       78 | 49.62%     | ok               |
|          45 | -1.29%   | -85.30%            | -53.47% |     0.18 |       58 | 23.18%     | ok               |
|          35 | -14.40%  | -85.30%            | -49.10% |     0.07 |       68 | 35.44%     | ok               |
|          25 | -22.50%  | -85.30%            | -55.69% |     0.03 |       70 | 44.25%     | ok               |

## ARB-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 57.32%   | -50.74%            | -33.60% |     0.67 |       54 | 26.44%     | ok               |
|          50 | 46.51%   | -50.74%            | -30.72% |     0.61 |       42 | 19.35%     | ok               |
|          15 | 43.91%   | -50.74%            | -44.26% |     0.58 |       90 | 58.62%     | ok               |
|          40 | 27.44%   | -50.74%            | -40.13% |     0.48 |       55 | 33.72%     | ok               |
|          35 | 21.94%   | -50.74%            | -45.71% |     0.44 |       71 | 37.93%     | ok               |

## ARKK Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -16.33%  | 83.98%             | -37.76% |    -0.11 |       90 | 54.74%     | ok               |
|          20 | -25.01%  | 83.98%             | -34.82% |    -0.29 |       91 | 50.08%     | ok               |
|          30 | -30.46%  | 83.98%             | -34.52% |    -0.47 |       89 | 43.59%     | ok               |
|          35 | -37.04%  | 83.98%             | -39.81% |    -0.66 |       90 | 40.77%     | ok               |
|          25 | -40.48%  | 83.98%             | -46.36% |    -0.69 |       99 | 46.09%     | ok               |

## ATOM-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -41.09%  | -64.83%            | -48.20% |    -0.32 |       86 | 65.71%     | ok               |
|          25 | -50.33%  | -64.83%            | -51.81% |    -0.56 |       94 | 54.21%     | ok               |
|          20 | -55.33%  | -64.83%            | -57.28% |    -0.65 |       96 | 58.05%     | ok               |
|          30 | -60.19%  | -64.83%            | -59.30% |    -0.87 |       92 | 48.08%     | ok               |
|          35 | -61.25%  | -64.83%            | -63.38% |    -1    |       82 | 41.95%     | ok               |

## AVAX-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 53.25%   | -57.85%            | -22.06% |     0.83 |       32 | 19.73%     | ok               |
|          40 | 19.68%   | -57.85%            | -26.61% |     0.43 |       38 | 27.39%     | ok               |
|          45 | 16.86%   | -57.85%            | -23.19% |     0.39 |       30 | 24.14%     | ok               |
|          15 | -5.98%   | -57.85%            | -43.71% |     0.17 |       73 | 52.11%     | ok               |
|          35 | -2.49%   | -57.85%            | -33.36% |     0.16 |       54 | 33.52%     | ok               |

## AVGO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | 19.64%   | 133.51%            | -38.01% |     0.39 |       68 | 43.93%     | ok               |
|          30 | 16.30%   | 133.51%            | -36.09% |     0.35 |       64 | 41.26%     | ok               |
|          50 | 11.33%   | 133.51%            | -36.86% |     0.3  |       56 | 29.12%     | ok               |
|          35 | 7.85%    | 133.51%            | -40.43% |     0.26 |       74 | 38.27%     | ok               |
|          20 | 5.92%    | 133.51%            | -39.42% |     0.25 |       77 | 47.09%     | ok               |

## BA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 41.10%   | 8.99%              | -13.34% |     0.9  |       46 | 35.77%     | ok               |
|          40 | 35.35%   | 8.99%              | -23.87% |     0.68 |       46 | 43.59%     | ok               |
|          35 | 33.87%   | 8.99%              | -18.09% |     0.63 |       62 | 48.09%     | ok               |
|          25 | 21.34%   | 8.99%              | -26.02% |     0.45 |       68 | 54.74%     | ok               |
|          20 | 12.43%   | 8.99%              | -26.02% |     0.32 |       69 | 58.07%     | ok               |

## BAC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 2.18%    | 29.04%             | -16.89% |     0.14 |       81 | 53.41%     | ok               |
|          25 | 0.99%    | 29.04%             | -17.17% |     0.11 |       76 | 51.08%     | ok               |
|          35 | -1.40%   | 29.04%             | -22.19% |     0.03 |       66 | 45.09%     | ok               |
|          15 | -6.02%   | 29.04%             | -21.05% |    -0.05 |       88 | 60.57%     | ok               |
|          30 | -5.04%   | 29.04%             | -20.18% |    -0.06 |       74 | 48.75%     | ok               |

## BCH-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 45.49%   | -29.92%            | -45.51% |     0.61 |       76 | 56.90%     | ok               |
|          20 | 20.67%   | -29.92%            | -45.63% |     0.42 |       68 | 53.64%     | ok               |
|          25 | 3.60%    | -29.92%            | -51.09% |     0.26 |       72 | 50.00%     | ok               |
|          30 | 3.80%    | -29.92%            | -53.87% |     0.25 |       78 | 48.47%     | ok               |
|          35 | -2.83%   | -29.92%            | -57.75% |     0.18 |       72 | 44.25%     | ok               |

## BITO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -8.30%   | -61.24%            | -31.98% |     0.01 |       54 | 24.96%     | ok               |
|          30 | -24.21%  | -61.24%            | -43.10% |    -0.17 |       79 | 41.43%     | ok               |
|          45 | -20.93%  | -61.24%            | -33.51% |    -0.19 |       60 | 28.45%     | ok               |
|          40 | -25.03%  | -61.24%            | -40.13% |    -0.23 |       62 | 32.78%     | ok               |
|          35 | -27.00%  | -61.24%            | -42.34% |    -0.24 |       70 | 36.94%     | ok               |

## BLK Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | -4.08%   | 45.08%             | -20.79% |    -0.05 |       90 | 43.09%     | ok               |
|          40 | -5.36%   | 45.08%             | -22.83% |    -0.1  |       78 | 38.27%     | ok               |
|          20 | -7.01%   | 45.08%             | -21.48% |    -0.11 |       86 | 51.41%     | ok               |
|          25 | -8.34%   | 45.08%             | -24.62% |    -0.15 |       79 | 49.25%     | ok               |
|          30 | -12.59%  | 45.08%             | -26.90% |    -0.29 |       83 | 46.76%     | ok               |

## BND Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -6.84%   | -1.19%             | -10.09% |    -0.96 |       65 | 40.27%     | ok               |
|          30 | -6.57%   | -1.19%             | -10.80% |    -1    |       66 | 34.94%     | ok               |
|          25 | -6.94%   | -1.19%             | -11.16% |    -1.02 |       68 | 38.10%     | ok               |
|          15 | -8.53%   | -1.19%             | -11.41% |    -1.19 |       76 | 42.93%     | ok               |
|          40 | -7.47%   | -1.19%             | -11.70% |    -1.26 |       62 | 29.28%     | ok               |

## BONK-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 156.03%  | -84.99%            | -35.57% |     1.2  |       42 | 21.46%     | ok               |
|          15 | 114.75%  | -84.99%            | -62.48% |     0.87 |       69 | 59.96%     | ok               |
|          20 | 83.80%   | -84.99%            | -54.25% |     0.78 |       66 | 55.75%     | ok               |
|          45 | 65.56%   | -84.99%            | -42.36% |     0.74 |       64 | 27.39%     | ok               |
|          25 | 58.18%   | -84.99%            | -46.61% |     0.66 |       71 | 51.72%     | ok               |

## BTC-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 44.69%   | -20.33%            | -13.90% |     0.89 |       44 | 34.67%     | ok               |
|          35 | 43.69%   | -20.33%            | -21.01% |     0.84 |       62 | 41.00%     | ok               |
|          45 | 39.19%   | -20.33%            | -12.20% |     0.83 |       40 | 30.65%     | ok               |
|          50 | 18.74%   | -20.33%            | -20.63% |     0.51 |       38 | 26.05%     | ok               |
|          30 | 18.78%   | -20.33%            | -21.75% |     0.45 |       68 | 46.93%     | ok               |

## C Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -10.81%  | 95.44%             | -22.03% |    -0.24 |       66 | 31.11%     | ok               |
|          45 | -21.46%  | 95.44%             | -29.81% |    -0.54 |       74 | 35.27%     | ok               |
|          40 | -27.61%  | 95.44%             | -35.31% |    -0.69 |       74 | 37.44%     | ok               |
|          25 | -33.25%  | 95.44%             | -36.49% |    -0.7  |       69 | 48.25%     | ok               |
|          30 | -34.54%  | 95.44%             | -39.51% |    -0.74 |       77 | 46.09%     | ok               |

## CAT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 18.89%   | 109.45%            | -21.80% |     0.4  |       73 | 60.57%     | ok               |
|          25 | 14.57%   | 109.45%            | -21.79% |     0.35 |       66 | 50.42%     | ok               |
|          45 | 7.62%    | 109.45%            | -23.56% |     0.25 |       54 | 36.61%     | ok               |
|          30 | 6.97%    | 109.45%            | -21.87% |     0.24 |       70 | 48.09%     | ok               |
|          20 | 5.27%    | 109.45%            | -24.56% |     0.21 |       76 | 53.58%     | ok               |

## CL Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 3.96%    | 0.87%              | -12.98% |     0.21 |       44 | 22.46%     | ok               |
|          30 | 0.11%    | 0.87%              | -14.32% |     0.07 |       66 | 38.60%     | ok               |
|          45 | -2.07%   | 0.87%              | -13.13% |    -0.03 |       50 | 25.29%     | ok               |
|          35 | -3.88%   | 0.87%              | -15.39% |    -0.07 |       66 | 34.78%     | ok               |
|          15 | -8.87%   | 0.87%              | -19.00% |    -0.2  |       66 | 46.92%     | ok               |

## CMCSA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -19.44%  | -39.37%            | -29.20% |    -0.64 |       50 | 16.64%     | ok               |
|          45 | -24.63%  | -39.37%            | -35.84% |    -0.78 |       64 | 21.30%     | ok               |
|          15 | -39.39%  | -39.37%            | -47.70% |    -0.85 |       91 | 58.24%     | ok               |
|          40 | -32.34%  | -39.37%            | -43.15% |    -0.87 |       91 | 28.79%     | ok               |
|          35 | -36.68%  | -39.37%            | -47.55% |    -0.95 |       93 | 38.44%     | ok               |

## COMP-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -1.20%   | -53.30%            | -38.71% |     0.19 |       50 | 24.90%     | ok               |
|          30 | -37.68%  | -53.30%            | -55.77% |    -0.21 |       97 | 49.81%     | ok               |
|          25 | -43.96%  | -53.30%            | -54.62% |    -0.28 |       96 | 57.85%     | ok               |
|          15 | -50.57%  | -53.30%            | -54.29% |    -0.37 |      100 | 68.77%     | ok               |
|          40 | -45.14%  | -53.30%            | -53.14% |    -0.41 |       72 | 38.31%     | ok               |

## COP Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -2.77%   | 24.96%             | -34.61% |     0.04 |       48 | 28.29%     | ok               |
|          35 | -6.66%   | 24.96%             | -42.05% |    -0.02 |       71 | 41.60%     | ok               |
|          30 | -9.39%   | 24.96%             | -41.35% |    -0.07 |       68 | 44.09%     | ok               |
|          45 | -10.41%  | 24.96%             | -41.10% |    -0.13 |       64 | 32.45%     | ok               |
|          40 | -18.37%  | 24.96%             | -47.48% |    -0.31 |       76 | 36.11%     | ok               |

## COST Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 13.65%   | 22.15%             | -24.32% |     0.45 |       62 | 47.09%     | ok               |
|          25 | 10.37%   | 22.15%             | -24.93% |     0.37 |       59 | 44.26%     | ok               |
|          35 | 4.00%    | 22.15%             | -30.16% |     0.2  |       58 | 38.60%     | ok               |
|          30 | -0.40%   | 22.15%             | -31.32% |     0.05 |       60 | 41.10%     | ok               |
|          15 | -1.75%   | 22.15%             | -27.30% |     0.03 |       67 | 50.75%     | ok               |

## CRM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | -20.37%  | -11.60%            | -32.74% |    -0.23 |       64 | 41.93%     | ok               |
|          40 | -23.35%  | -11.60%            | -38.23% |    -0.31 |       70 | 37.77%     | ok               |
|          15 | -29.99%  | -11.60%            | -47.54% |    -0.33 |       90 | 57.74%     | ok               |
|          50 | -21.23%  | -11.60%            | -38.38% |    -0.37 |       60 | 25.12%     | ok               |
|          30 | -31.30%  | -11.60%            | -44.41% |    -0.43 |       67 | 46.76%     | ok               |

## CRV-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 76.89%   | -49.17%            | -37.78% |     0.81 |       64 | 31.80%     | ok               |
|          40 | 61.13%   | -49.17%            | -38.86% |     0.73 |       52 | 27.59%     | ok               |
|          50 | 42.22%   | -49.17%            | -30.73% |     0.62 |       44 | 17.24%     | ok               |
|          45 | 43.20%   | -49.17%            | -42.29% |     0.62 |       52 | 21.26%     | ok               |
|          30 | 42.17%   | -49.17%            | -39.89% |     0.58 |       64 | 36.40%     | ok               |

## CSCO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 29.54%   | 131.34%            | -19.34% |     0.63 |       50 | 38.60%     | ok               |
|          45 | 25.27%   | 131.34%            | -19.34% |     0.55 |       54 | 40.10%     | ok               |
|          25 | 15.21%   | 131.34%            | -23.28% |     0.37 |       61 | 51.08%     | ok               |
|          40 | 11.99%   | 131.34%            | -22.37% |     0.32 |       57 | 43.09%     | ok               |
|          30 | 11.24%   | 131.34%            | -22.26% |     0.31 |       63 | 49.92%     | ok               |

## CVX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -7.10%   | 42.62%             | -23.80% |    -0.1  |       75 | 45.09%     | ok               |
|          40 | -8.92%   | 42.62%             | -27.34% |    -0.18 |       75 | 36.94%     | ok               |
|          45 | -9.31%   | 42.62%             | -28.83% |    -0.2  |       67 | 33.61%     | ok               |
|          35 | -10.66%  | 42.62%             | -28.85% |    -0.22 |       71 | 39.10%     | ok               |
|          30 | -11.25%  | 42.62%             | -27.78% |    -0.22 |       73 | 42.26%     | ok               |

## DASH-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 156.61%  | 108.48%            | -33.55% |     1.01 |       38 | 18.01%     | ok               |
|          40 | 125.75%  | 108.48%            | -33.20% |     0.89 |       42 | 24.33%     | ok               |
|          45 | 94.16%   | 108.48%            | -37.63% |     0.78 |       42 | 20.50%     | ok               |
|          30 | -0.66%   | 108.48%            | -64.43% |     0.38 |       53 | 29.89%     | ok               |
|          25 | -1.61%   | 108.48%            | -64.14% |     0.38 |       63 | 32.18%     | ok               |

## DBC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -0.09%   | 43.45%             | -26.05% |     0.07 |       77 | 41.26%     | ok               |
|          20 | -4.49%   | 43.45%             | -25.69% |    -0.08 |       69 | 39.60%     | ok               |
|          25 | -5.28%   | 43.45%             | -24.84% |    -0.11 |       66 | 37.60%     | ok               |
|          50 | -6.09%   | 43.45%             | -19.34% |    -0.18 |       50 | 24.79%     | ok               |
|          35 | -7.76%   | 43.45%             | -23.19% |    -0.2  |       66 | 34.28%     | ok               |

## DE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 2.13%    | 71.18%             | -17.97% |     0.13 |       56 | 29.62%     | ok               |
|          45 | -4.48%   | 71.18%             | -19.53% |    -0.02 |       60 | 34.11%     | ok               |
|          20 | -7.80%   | 71.18%             | -24.11% |    -0.07 |       65 | 48.59%     | ok               |
|          25 | -12.03%  | 71.18%             | -24.29% |    -0.17 |       71 | 46.92%     | ok               |
|          30 | -12.17%  | 71.18%             | -23.98% |    -0.18 |       70 | 44.26%     | ok               |

## DIA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -2.82%   | 32.88%             | -11.28% |    -0.11 |       60 | 44.59%     | ok               |
|          35 | -4.59%   | 32.88%             | -13.15% |    -0.23 |       68 | 40.27%     | ok               |
|          30 | -5.01%   | 32.88%             | -12.94% |    -0.24 |       66 | 43.43%     | ok               |
|          20 | -5.62%   | 32.88%             | -13.72% |    -0.26 |       66 | 46.59%     | ok               |
|          40 | -7.77%   | 32.88%             | -15.06% |    -0.44 |       72 | 36.94%     | ok               |

## DIS Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 39.47%   | 8.68%              | -10.17% |     1.2  |       44 | 25.29%     | ok               |
|          40 | 9.97%    | 8.68%              | -18.75% |     0.32 |       63 | 33.94%     | ok               |
|          45 | 8.94%    | 8.68%              | -16.54% |     0.31 |       49 | 28.95%     | ok               |
|          35 | -1.77%   | 8.68%              | -25.70% |     0.05 |       77 | 40.10%     | ok               |
|          15 | -3.91%   | 8.68%              | -31.15% |     0.03 |       85 | 54.41%     | ok               |

## DOGE-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 23.48%   | -64.10%            | -53.85% |     0.46 |       71 | 64.56%     | ok               |
|          20 | 8.43%    | -64.10%            | -53.94% |     0.33 |       75 | 59.00%     | ok               |
|          25 | 3.79%    | -64.10%            | -51.74% |     0.28 |       65 | 54.98%     | ok               |
|          30 | -19.11%  | -64.10%            | -60.95% |     0.01 |       67 | 48.66%     | ok               |
|          50 | -17.19%  | -64.10%            | -51.28% |    -0.05 |       60 | 23.18%     | ok               |

## DOT-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -49.79%  | -76.56%            | -72.06% |    -0.27 |       74 | 62.45%     | ok               |
|          20 | -46.32%  | -76.56%            | -66.32% |    -0.28 |       86 | 58.43%     | ok               |
|          30 | -48.42%  | -76.56%            | -63.33% |    -0.37 |       84 | 47.70%     | ok               |
|          25 | -54.60%  | -76.56%            | -69.99% |    -0.45 |       77 | 53.45%     | ok               |
|          35 | -53.52%  | -76.56%            | -63.01% |    -0.5  |       82 | 42.15%     | ok               |

## DXY-INDEX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd    |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:-------|---------:|---------:|:-----------|:-----------------|
|          50 | -0.89%   | -4.80%             | -6.02% |    -0.12 |       38 | 32.25%     | ok               |
|          40 | -2.30%   | -4.80%             | -7.30% |    -0.29 |       64 | 47.62%     | ok               |
|          45 | -2.30%   | -4.80%             | -8.14% |    -0.31 |       60 | 38.31%     | ok               |
|          30 | -5.20%   | -4.80%             | -9.83% |    -0.61 |       74 | 57.58%     | ok               |
|          35 | -5.36%   | -4.80%             | -9.97% |    -0.67 |       77 | 52.60%     | ok               |

## EEM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -7.04%   | 46.09%             | -15.88% |    -0.2  |       54 | 32.11%     | ok               |
|          45 | -7.38%   | 46.09%             | -17.03% |    -0.21 |       52 | 33.61%     | ok               |
|          40 | -7.72%   | 46.09%             | -19.20% |    -0.22 |       64 | 35.77%     | ok               |
|          35 | -8.36%   | 46.09%             | -23.57% |    -0.22 |       66 | 37.77%     | ok               |
|          30 | -10.11%  | 46.09%             | -23.94% |    -0.27 |       64 | 39.77%     | ok               |

## EFA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -3.08%   | 27.76%             | -10.10% |    -0.05 |       62 | 51.58%     | ok               |
|          20 | -10.69%  | 27.76%             | -13.36% |    -0.38 |       71 | 48.59%     | ok               |
|          30 | -11.28%  | 27.76%             | -13.15% |    -0.44 |       68 | 41.26%     | ok               |
|          25 | -12.32%  | 27.76%             | -15.56% |    -0.47 |       70 | 44.59%     | ok               |
|          40 | -11.36%  | 27.76%             | -14.44% |    -0.48 |       64 | 36.27%     | ok               |

## EOG Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -15.08%  | 28.18%             | -35.34% |    -0.29 |       56 | 31.11%     | ok               |
|          50 | -20.25%  | 28.18%             | -35.63% |    -0.47 |       54 | 28.12%     | ok               |
|          40 | -21.98%  | 28.18%             | -37.39% |    -0.48 |       72 | 34.94%     | ok               |
|          35 | -26.07%  | 28.18%             | -39.96% |    -0.58 |       85 | 39.93%     | ok               |
|          30 | -28.64%  | 28.18%             | -47.87% |    -0.6  |       80 | 45.09%     | ok               |

## ETC-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -0.57%   | -58.63%            | -35.44% |     0.14 |       28 | 20.69%     | ok               |
|          50 | -0.26%   | -58.63%            | -28.33% |     0.13 |       26 | 18.01%     | ok               |
|          35 | -12.97%  | -58.63%            | -42.62% |    -0.05 |       42 | 27.78%     | ok               |
|          40 | -12.30%  | -58.63%            | -40.48% |    -0.06 |       40 | 23.95%     | ok               |
|          30 | -15.00%  | -58.63%            | -45.54% |    -0.07 |       56 | 31.80%     | ok               |

## ETH-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 142.75%  | -4.59%             | -30.11% |     1.31 |       58 | 47.32%     | ok               |
|          30 | 104.78%  | -4.59%             | -32.89% |     1.05 |       60 | 54.98%     | ok               |
|          40 | 63.51%   | -4.59%             | -33.11% |     0.85 |       62 | 39.66%     | ok               |
|          25 | 67.63%   | -4.59%             | -40.90% |     0.8  |       60 | 58.81%     | ok               |
|          50 | 41.38%   | -4.59%             | -30.50% |     0.69 |       62 | 29.31%     | ok               |

## EWJ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -22.99%  | 38.59%             | -29.40% |    -0.8  |       62 | 36.44%     | ok               |
|          20 | -23.95%  | 38.59%             | -30.00% |    -0.81 |       56 | 38.44%     | ok               |
|          25 | -25.82%  | 38.59%             | -29.85% |    -0.9  |       56 | 37.60%     | ok               |
|          15 | -27.60%  | 38.59%             | -31.15% |    -0.9  |       67 | 41.76%     | ok               |
|          45 | -23.95%  | 38.59%             | -27.68% |    -0.98 |       58 | 28.12%     | ok               |

## FCX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 2.51%    | 34.95%             | -29.27% |     0.18 |       50 | 31.61%     | ok               |
|          50 | -0.09%   | 34.95%             | -26.57% |     0.13 |       52 | 27.95%     | ok               |
|          40 | -10.00%  | 34.95%             | -42.89% |    -0.01 |       62 | 36.94%     | ok               |
|          30 | -29.37%  | 34.95%             | -46.84% |    -0.32 |       65 | 44.26%     | ok               |
|          35 | -29.20%  | 34.95%             | -50.12% |    -0.34 |       67 | 42.10%     | ok               |

## FET-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -31.55%  | -75.34%            | -59.58% |     0.01 |       78 | 56.70%     | ok               |
|          25 | -30.33%  | -75.34%            | -65.31% |    -0.02 |       81 | 46.93%     | ok               |
|          20 | -36.01%  | -75.34%            | -65.01% |    -0.07 |       88 | 52.49%     | ok               |
|          30 | -46.79%  | -75.34%            | -65.38% |    -0.29 |       79 | 42.34%     | ok               |
|          50 | -39.06%  | -75.34%            | -45.19% |    -0.53 |       46 | 14.37%     | ok               |

## FIL-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -40.15%  | -64.07%            | -58.54% |    -0.34 |       65 | 37.16%     | ok               |
|          35 | -41.96%  | -64.07%            | -61.90% |    -0.42 |       58 | 31.23%     | ok               |
|          40 | -40.23%  | -64.07%            | -57.60% |    -0.44 |       48 | 26.82%     | ok               |
|          15 | -58.37%  | -64.07%            | -71.82% |    -0.57 |       91 | 49.04%     | ok               |
|          25 | -58.52%  | -64.07%            | -70.65% |    -0.66 |       76 | 40.04%     | ok               |

## FXI Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -4.86%   | 22.70%             | -22.99% |    -0.04 |       52 | 32.28%     | ok               |
|          30 | -5.13%   | 22.70%             | -24.33% |    -0.05 |       50 | 30.78%     | ok               |
|          15 | -5.74%   | 22.70%             | -21.68% |    -0.05 |       54 | 36.27%     | ok               |
|          20 | -8.49%   | 22.70%             | -24.94% |    -0.13 |       54 | 34.11%     | ok               |
|          35 | -8.80%   | 22.70%             | -27.93% |    -0.15 |       52 | 28.29%     | ok               |

## GDX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 5.89%    | 148.75%            | -31.44% |     0.23 |       76 | 50.25%     | ok               |
|          40 | 2.88%    | 148.75%            | -28.04% |     0.17 |       62 | 38.10%     | ok               |
|          30 | 2.01%    | 148.75%            | -33.31% |     0.17 |       62 | 44.43%     | ok               |
|          35 | -3.07%   | 148.75%            | -32.08% |     0.08 |       70 | 40.77%     | ok               |
|          25 | -6.33%   | 148.75%            | -38.90% |     0.04 |       66 | 46.09%     | ok               |

## GDXJ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -22.65%  | 146.43%            | -41.17% |    -0.16 |       74 | 50.25%     | ok               |
|          50 | -25.13%  | 146.43%            | -46.83% |    -0.31 |       60 | 34.28%     | ok               |
|          35 | -33.18%  | 146.43%            | -37.32% |    -0.42 |       72 | 40.43%     | ok               |
|          30 | -35.03%  | 146.43%            | -40.39% |    -0.44 |       72 | 43.09%     | ok               |
|          25 | -38.97%  | 146.43%            | -42.91% |    -0.48 |       77 | 46.26%     | ok               |

## GE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 4.89%    | 87.55%             | -21.25% |     0.2  |       60 | 33.78%     | ok               |
|          45 | -2.34%   | 87.55%             | -21.88% |     0.05 |       70 | 36.44%     | ok               |
|          30 | -8.43%   | 87.55%             | -27.82% |    -0.04 |       76 | 48.09%     | ok               |
|          25 | -8.86%   | 87.55%             | -29.91% |    -0.05 |       72 | 49.92%     | ok               |
|          20 | -9.37%   | 87.55%             | -25.05% |    -0.05 |       72 | 52.58%     | ok               |

## GLD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | 18.97%   | 76.92%             | -13.87% |     0.5  |       48 | 46.92%     | ok               |
|          20 | 17.35%   | 76.92%             | -13.87% |     0.47 |       49 | 48.59%     | ok               |
|          30 | 13.30%   | 76.92%             | -13.87% |     0.39 |       50 | 45.76%     | ok               |
|          35 | 10.07%   | 76.92%             | -15.09% |     0.32 |       52 | 43.26%     | ok               |
|          15 | 6.56%    | 76.92%             | -18.05% |     0.24 |       57 | 51.91%     | ok               |

## GOOGL Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 61.45%   | 94.63%             | -17.38% |     1.09 |       59 | 43.59%     | ok               |
|          30 | 57.55%   | 94.63%             | -17.54% |     1.01 |       57 | 47.09%     | ok               |
|          45 | 49.96%   | 94.63%             | -11.66% |     1    |       52 | 37.10%     | ok               |
|          25 | 55.14%   | 94.63%             | -16.87% |     0.97 |       57 | 49.58%     | ok               |
|          50 | 44.22%   | 94.63%             | -11.52% |     0.94 |       46 | 32.11%     | ok               |

## GRT-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 65.12%   | -78.46%            | -33.74% |     0.74 |       79 | 45.79%     | ok               |
|          15 | 56.03%   | -78.46%            | -36.70% |     0.66 |       71 | 62.26%     | ok               |
|          45 | 45.48%   | -78.46%            | -39.70% |     0.64 |       48 | 27.97%     | ok               |
|          25 | 45.35%   | -78.46%            | -37.25% |     0.6  |       78 | 51.72%     | ok               |
|          20 | 39.89%   | -78.46%            | -37.63% |     0.57 |       80 | 55.56%     | ok               |

## GS Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 23.58%   | 91.09%             | -20.56% |     0.51 |       68 | 56.41%     | ok               |
|          20 | 4.60%    | 91.09%             | -23.19% |     0.19 |       68 | 53.08%     | ok               |
|          40 | 3.45%    | 91.09%             | -16.16% |     0.17 |       70 | 41.93%     | ok               |
|          25 | -0.70%   | 91.09%             | -23.32% |     0.09 |       68 | 50.58%     | ok               |
|          30 | -2.87%   | 91.09%             | -21.94% |     0.04 |       70 | 48.09%     | ok               |

## HBAR-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -18.60%  | -18.56%            | -39.26% |    -0.27 |       18 | 17.54%     | ok               |
|          45 | -33.67%  | -18.56%            | -48.27% |    -0.69 |       22 | 23.51%     | ok               |
|          40 | -36.39%  | -18.56%            | -51.16% |    -0.75 |       30 | 29.48%     | ok               |
|          30 | -42.37%  | -18.56%            | -56.47% |    -0.9  |       40 | 38.81%     | ok               |
|          35 | -41.76%  | -18.56%            | -56.01% |    -0.91 |       30 | 34.33%     | ok               |

## HD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 1.72%    | -4.76%             | -17.15% |     0.13 |       67 | 43.59%     | ok               |
|          40 | 1.06%    | -4.76%             | -16.74% |     0.1  |       72 | 34.78%     | ok               |
|          35 | 0.84%    | -4.76%             | -17.81% |     0.1  |       70 | 39.60%     | ok               |
|          45 | 0.27%    | -4.76%             | -17.41% |     0.07 |       48 | 29.95%     | ok               |
|          25 | -1.38%   | -4.76%             | -18.17% |     0.05 |       66 | 45.92%     | ok               |

## HON Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -9.73%   | 7.10%              | -20.54% |    -0.24 |       68 | 32.61%     | ok               |
|          45 | -13.56%  | 7.10%              | -22.88% |    -0.34 |       72 | 38.10%     | ok               |
|          35 | -25.30%  | 7.10%              | -31.66% |    -0.65 |       93 | 49.92%     | ok               |
|          40 | -25.06%  | 7.10%              | -31.84% |    -0.67 |       78 | 42.60%     | ok               |
|          30 | -26.93%  | 7.10%              | -33.87% |    -0.67 |       93 | 54.91%     | ok               |

## HYG Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -4.40%   | -0.30%             | -7.76%  |    -0.5  |       70 | 34.11%     | ok               |
|          45 | -6.17%   | -0.30%             | -8.86%  |    -0.74 |       70 | 30.45%     | ok               |
|          30 | -6.78%   | -0.30%             | -10.59% |    -0.75 |       85 | 39.27%     | ok               |
|          35 | -6.62%   | -0.30%             | -9.66%  |    -0.75 |       79 | 35.94%     | ok               |
|          25 | -7.39%   | -0.30%             | -11.22% |    -0.8  |       89 | 41.93%     | ok               |

## IBIT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 64.65%   | 21.42%             | -19.20% |     0.94 |       44 | 42.22%     | ok               |
|          50 | 52.34%   | 21.42%             | -17.37% |     0.93 |       26 | 25.45%     | ok               |
|          45 | 42.96%   | 21.42%             | -17.37% |     0.79 |       30 | 26.67%     | ok               |
|          30 | 36.51%   | 21.42%             | -18.95% |     0.67 |       40 | 34.95%     | ok               |
|          40 | 33.91%   | 21.42%             | -18.18% |     0.67 |       32 | 28.69%     | ok               |

## IBM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -18.90%  | 35.84%             | -49.43% |    -0.14 |       83 | 60.40%     | ok               |
|          35 | -21.72%  | 35.84%             | -47.10% |    -0.24 |       61 | 45.42%     | ok               |
|          30 | -25.12%  | 35.84%             | -48.94% |    -0.3  |       69 | 48.92%     | ok               |
|          45 | -26.90%  | 35.84%             | -48.72% |    -0.37 |       50 | 37.10%     | ok               |
|          20 | -30.54%  | 35.84%             | -53.45% |    -0.38 |       69 | 53.41%     | ok               |

## ICP-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -14.23%  | -45.07%            | -44.07% |     0.13 |       77 | 39.08%     | ok               |
|          35 | -11.56%  | -45.07%            | -51.30% |     0.09 |       70 | 33.33%     | ok               |
|          40 | -12.10%  | -45.07%            | -45.75% |     0.07 |       62 | 28.74%     | ok               |
|          15 | -40.07%  | -45.07%            | -59.36% |    -0.08 |       77 | 50.19%     | ok               |
|          20 | -42.22%  | -45.07%            | -62.50% |    -0.13 |       86 | 47.13%     | ok               |

## IEF Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -6.36%   | -2.65%             | -10.18% |    -0.75 |       72 | 41.93%     | ok               |
|          15 | -7.58%   | -2.65%             | -10.91% |    -0.88 |       71 | 43.59%     | ok               |
|          40 | -7.94%   | -2.65%             | -11.24% |    -1.15 |       62 | 26.79%     | ok               |
|          50 | -6.87%   | -2.65%             | -9.11%  |    -1.16 |       56 | 21.80%     | ok               |
|          45 | -8.07%   | -2.65%             | -11.30% |    -1.21 |       58 | 24.96%     | ok               |

## IEMG Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -2.71%   | 42.15%             | -14.22% |    -0.05 |       54 | 30.95%     | ok               |
|          45 | -3.51%   | 42.15%             | -15.23% |    -0.08 |       50 | 33.44%     | ok               |
|          40 | -4.99%   | 42.15%             | -18.73% |    -0.13 |       62 | 36.44%     | ok               |
|          35 | -6.40%   | 42.15%             | -23.75% |    -0.16 |       65 | 38.77%     | ok               |
|          25 | -9.06%   | 42.15%             | -26.09% |    -0.25 |       62 | 41.76%     | ok               |

## INJ-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 2.78%    | -28.92%            | -52.61% |     0.28 |       60 | 36.97%     | ok               |
|          40 | 3.39%    | -28.92%            | -45.92% |     0.27 |       50 | 33.72%     | ok               |
|          45 | -5.09%   | -28.92%            | -43.79% |     0.16 |       54 | 28.16%     | ok               |
|          30 | -30.06%  | -28.92%            | -69.14% |    -0.06 |       63 | 40.04%     | ok               |
|          15 | -34.77%  | -28.92%            | -74.15% |    -0.06 |       77 | 50.38%     | ok               |

## INTC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 70.01%   | 192.48%            | -49.32% |     0.71 |       56 | 33.78%     | ok               |
|          50 | 64.73%   | 192.48%            | -48.35% |     0.68 |       60 | 29.95%     | ok               |
|          15 | 59.37%   | 192.48%            | -53.65% |     0.63 |       76 | 59.23%     | ok               |
|          40 | 51.36%   | 192.48%            | -55.86% |     0.59 |       64 | 37.94%     | ok               |
|          25 | 49.66%   | 192.48%            | -56.41% |     0.58 |       77 | 50.58%     | ok               |

## INTU Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 20.11%   | -46.43%            | -34.44% |     0.45 |       65 | 28.45%     | ok               |
|          45 | 7.67%    | -46.43%            | -37.21% |     0.25 |       65 | 32.78%     | ok               |
|          25 | 6.64%    | -46.43%            | -35.05% |     0.24 |       70 | 49.58%     | ok               |
|          40 | 2.87%    | -46.43%            | -39.49% |     0.17 |       67 | 36.77%     | ok               |
|          30 | 1.22%    | -46.43%            | -37.50% |     0.15 |       73 | 46.92%     | ok               |

## ITA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -0.96%   | 54.24%             | -21.48% |     0.04 |       76 | 36.44%     | ok               |
|          15 | -3.29%   | 54.24%             | -28.06% |     0.01 |       83 | 60.90%     | ok               |
|          30 | -3.36%   | 54.24%             | -23.75% |    -0.02 |       78 | 48.25%     | ok               |
|          40 | -6.72%   | 54.24%             | -20.54% |    -0.14 |       78 | 41.60%     | ok               |
|          35 | -7.41%   | 54.24%             | -23.12% |    -0.15 |       80 | 45.26%     | ok               |

## IWM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | 14.63%   | 31.64%             | -10.51% |     0.56 |       54 | 34.94%     | ok               |
|          20 | 13.11%   | 31.64%             | -10.28% |     0.5  |       60 | 35.94%     | ok               |
|          40 | 10.69%   | 31.64%             | -12.14% |     0.48 |       48 | 29.62%     | ok               |
|          35 | 8.78%    | 31.64%             | -12.14% |     0.38 |       54 | 32.11%     | ok               |
|          15 | 9.64%    | 31.64%             | -11.99% |     0.37 |       78 | 41.76%     | ok               |

## JNJ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 20.07%   | 73.89%             | -10.57% |     0.81 |       38 | 34.61%     | ok               |
|          15 | 15.04%   | 73.89%             | -17.37% |     0.54 |       56 | 53.08%     | ok               |
|          45 | 9.79%    | 73.89%             | -13.35% |     0.43 |       44 | 38.27%     | ok               |
|          30 | 10.08%   | 73.89%             | -16.86% |     0.41 |       58 | 46.59%     | ok               |
|          20 | 9.72%    | 73.89%             | -16.96% |     0.39 |       62 | 49.58%     | ok               |

## JPM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 3.42%    | 69.26%             | -15.90% |     0.18 |       50 | 32.61%     | ok               |
|          45 | -6.89%   | 69.26%             | -21.91% |    -0.16 |       54 | 35.27%     | ok               |
|          20 | -21.97%  | 69.26%             | -35.58% |    -0.48 |       86 | 48.75%     | ok               |
|          35 | -19.02%  | 69.26%             | -27.43% |    -0.55 |       74 | 41.10%     | ok               |
|          40 | -19.67%  | 69.26%             | -28.47% |    -0.58 |       66 | 37.94%     | ok               |

## KO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 27.65%   | 51.45%             | -8.64%  |     0.96 |       54 | 36.77%     | ok               |
|          35 | 23.31%   | 51.45%             | -8.21%  |     0.84 |       58 | 35.27%     | ok               |
|          40 | 20.34%   | 51.45%             | -9.28%  |     0.79 |       60 | 31.95%     | ok               |
|          25 | 21.44%   | 51.45%             | -10.16% |     0.77 |       60 | 39.43%     | ok               |
|          20 | 7.97%    | 51.45%             | -15.99% |     0.33 |       79 | 43.59%     | ok               |

## LDO-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 99.19%   | -59.44%            | -39.01% |     0.84 |       79 | 58.81%     | ok               |
|          20 | 76.06%   | -59.44%            | -40.80% |     0.75 |       79 | 53.83%     | ok               |
|          30 | 44.08%   | -59.44%            | -50.47% |     0.59 |       72 | 46.93%     | ok               |
|          25 | 24.75%   | -59.44%            | -47.32% |     0.47 |       80 | 51.34%     | ok               |
|          35 | 20.93%   | -59.44%            | -58.19% |     0.43 |       78 | 39.46%     | ok               |

## LIN Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -6.99%   | 14.43%             | -23.00% |    -0.18 |       66 | 44.43%     | ok               |
|          25 | -6.92%   | 14.43%             | -22.01% |    -0.18 |       73 | 41.43%     | ok               |
|          15 | -8.74%   | 14.43%             | -23.68% |    -0.23 |       72 | 47.75%     | ok               |
|          30 | -10.02%  | 14.43%             | -20.61% |    -0.31 |       74 | 38.60%     | ok               |
|          35 | -11.64%  | 14.43%             | -19.70% |    -0.4  |       74 | 31.95%     | ok               |

## LINK-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 56.97%   | -22.95%            | -33.64% |     0.71 |       64 | 44.44%     | ok               |
|          45 | 32.86%   | -22.95%            | -33.71% |     0.54 |       50 | 31.03%     | ok               |
|          35 | 31.35%   | -22.95%            | -34.21% |     0.52 |       58 | 40.42%     | ok               |
|          40 | 22.85%   | -22.95%            | -34.00% |     0.44 |       54 | 34.87%     | ok               |
|          25 | 9.41%    | -22.95%            | -46.32% |     0.33 |       60 | 47.89%     | ok               |

## LLY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 0.86%    | 55.68%             | -38.23% |     0.13 |       50 | 35.44%     | ok               |
|          15 | -13.37%  | 55.68%             | -48.12% |    -0.07 |       70 | 60.23%     | ok               |
|          45 | -12.43%  | 55.68%             | -42.75% |    -0.13 |       60 | 39.10%     | ok               |
|          40 | -23.55%  | 55.68%             | -46.32% |    -0.35 |       70 | 42.10%     | ok               |
|          20 | -27.20%  | 55.68%             | -52.31% |    -0.36 |       77 | 55.24%     | ok               |

## LRCX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -24.49%  | 171.94%            | -55.17% |    -0.08 |       79 | 50.92%     | ok               |
|          50 | -19.19%  | 171.94%            | -48.71% |    -0.1  |       74 | 33.94%     | ok               |
|          40 | -25.05%  | 171.94%            | -55.33% |    -0.16 |       70 | 39.93%     | ok               |
|          35 | -26.49%  | 171.94%            | -58.47% |    -0.17 |       78 | 42.10%     | ok               |
|          20 | -31.02%  | 171.94%            | -61.61% |    -0.2  |       84 | 46.76%     | ok               |

## LTC-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 14.40%   | -40.58%            | -36.44% |     0.36 |       56 | 35.44%     | ok               |
|          35 | 14.40%   | -40.58%            | -34.94% |     0.36 |       64 | 44.83%     | ok               |
|          30 | 3.80%    | -40.58%            | -30.78% |     0.24 |       67 | 51.92%     | ok               |
|          25 | 0.08%    | -40.58%            | -34.22% |     0.2  |       69 | 54.21%     | ok               |
|          50 | -4.75%   | -40.58%            | -35.25% |     0.09 |       58 | 26.44%     | ok               |

## MCD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 10.95%   | -5.87%             | -9.22%  |     0.51 |       46 | 24.96%     | ok               |
|          40 | 1.66%    | -5.87%             | -18.49% |     0.12 |       69 | 32.45%     | ok               |
|          45 | 1.58%    | -5.87%             | -16.79% |     0.12 |       54 | 28.79%     | ok               |
|          35 | -1.84%   | -5.87%             | -16.63% |    -0.02 |       67 | 37.44%     | ok               |
|          30 | -3.15%   | -5.87%             | -21.88% |    -0.06 |       79 | 40.60%     | ok               |

## META Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -8.40%   | 48.33%             | -37.10% |    -0.03 |       66 | 39.93%     | ok               |
|          40 | -14.42%  | 48.33%             | -40.49% |    -0.14 |       68 | 42.93%     | ok               |
|          50 | -18.60%  | 48.33%             | -38.90% |    -0.25 |       68 | 35.77%     | ok               |
|          30 | -27.93%  | 48.33%             | -44.52% |    -0.39 |       72 | 50.42%     | ok               |
|          35 | -28.00%  | 48.33%             | -40.80% |    -0.41 |       81 | 48.09%     | ok               |

## MPC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 30.66%   | 168.88%            | -19.02% |     0.61 |       54 | 40.43%     | ok               |
|          40 | 28.51%   | 168.88%            | -20.88% |     0.56 |       64 | 47.09%     | ok               |
|          45 | 26.25%   | 168.88%            | -20.23% |     0.54 |       60 | 44.43%     | ok               |
|          35 | 27.60%   | 168.88%            | -31.08% |     0.53 |       70 | 49.75%     | ok               |
|          30 | 21.37%   | 168.88%            | -34.29% |     0.45 |       72 | 52.41%     | ok               |

## MRK Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -13.09%  | 12.71%             | -28.39% |    -0.16 |       83 | 51.91%     | ok               |
|          25 | -14.40%  | 12.71%             | -31.07% |    -0.21 |       70 | 44.26%     | ok               |
|          50 | -14.54%  | 12.71%             | -23.01% |    -0.3  |       56 | 28.45%     | ok               |
|          20 | -18.59%  | 12.71%             | -29.34% |    -0.3  |       75 | 47.59%     | ok               |
|          45 | -16.67%  | 12.71%             | -25.38% |    -0.33 |       57 | 31.78%     | ok               |

## MS Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 3.42%    | 82.45%             | -22.02% |     0.17 |       74 | 58.24%     | ok               |
|          40 | 2.76%    | 82.45%             | -19.99% |     0.15 |       74 | 39.27%     | ok               |
|          20 | 0.97%    | 82.45%             | -25.68% |     0.11 |       75 | 53.08%     | ok               |
|          30 | -4.27%   | 82.45%             | -27.79% |    -0.02 |       75 | 48.25%     | ok               |
|          25 | -5.74%   | 82.45%             | -28.36% |    -0.05 |       73 | 50.42%     | ok               |

## MSFT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -14.32%  | 22.99%             | -24.64% |    -0.32 |       74 | 37.44%     | ok               |
|          50 | -19.34%  | 22.99%             | -25.48% |    -0.49 |       64 | 31.78%     | ok               |
|          35 | -23.65%  | 22.99%             | -35.38% |    -0.51 |       75 | 46.59%     | ok               |
|          40 | -23.65%  | 22.99%             | -34.77% |    -0.54 |       73 | 41.26%     | ok               |
|          30 | -26.92%  | 22.99%             | -39.15% |    -0.58 |       83 | 51.41%     | ok               |

## MU Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 160.52%  | 578.69%            | -64.30% |     1.08 |       58 | 47.92%     | ok               |
|          15 | 185.83%  | 578.69%            | -61.96% |     1.08 |       51 | 59.23%     | ok               |
|          30 | 136.57%  | 578.69%            | -68.76% |     0.98 |       51 | 52.25%     | ok               |
|          25 | 135.19%  | 578.69%            | -67.90% |     0.97 |       51 | 53.74%     | ok               |
|          35 | 128.15%  | 578.69%            | -69.35% |     0.96 |       63 | 50.08%     | ok               |

## NEAR-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 189.00%  | 79.64%             | -38.74% |     1.3  |       28 | 22.03%     | ok               |
|          40 | 196.86%  | 79.64%             | -42.59% |     1.24 |       42 | 31.23%     | ok               |
|          30 | 172.52%  | 79.64%             | -46.60% |     1.12 |       69 | 44.06%     | ok               |
|          45 | 149.14%  | 79.64%             | -38.08% |     1.09 |       44 | 27.20%     | ok               |
|          35 | 139.03%  | 79.64%             | -52.37% |     1.04 |       64 | 35.82%     | ok               |

## NEM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 0.12%    | 182.52%            | -31.25% |     0.17 |       63 | 58.57%     | ok               |
|          20 | -0.63%   | 182.52%            | -30.50% |     0.16 |       70 | 54.08%     | ok               |
|          25 | -15.82%  | 182.52%            | -39.51% |    -0.07 |       66 | 51.75%     | ok               |
|          50 | -13.27%  | 182.52%            | -33.03% |    -0.07 |       50 | 38.10%     | ok               |
|          30 | -24.88%  | 182.52%            | -39.56% |    -0.23 |       70 | 49.92%     | ok               |

## NFLX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 29.73%   | 9.05%              | -16.28% |     0.76 |       44 | 32.95%     | ok               |
|          40 | 28.64%   | 9.05%              | -15.02% |     0.69 |       50 | 40.93%     | ok               |
|          35 | 24.26%   | 9.05%              | -18.30% |     0.58 |       74 | 45.59%     | ok               |
|          45 | 17.11%   | 9.05%              | -15.48% |     0.47 |       56 | 37.44%     | ok               |
|          15 | 4.39%    | 9.05%              | -26.59% |     0.19 |       72 | 65.06%     | ok               |

## NKE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | -16.21%  | -59.53%            | -42.13% |    -0.15 |       71 | 40.43%     | ok               |
|          20 | -23.52%  | -59.53%            | -49.34% |    -0.22 |       83 | 54.08%     | ok               |
|          25 | -26.69%  | -59.53%            | -51.20% |    -0.28 |       83 | 51.41%     | ok               |
|          15 | -28.45%  | -59.53%            | -54.28% |    -0.3  |       86 | 57.90%     | ok               |
|          40 | -20.78%  | -59.53%            | -31.79% |    -0.35 |       65 | 32.28%     | ok               |

## NOW Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 11.00%   | -3.88%             | -30.43% |     0.3  |       80 | 50.25%     | ok               |
|          20 | 8.52%    | -3.88%             | -39.71% |     0.28 |       75 | 56.57%     | ok               |
|          25 | 5.77%    | -3.88%             | -37.51% |     0.25 |       72 | 53.74%     | ok               |
|          15 | 0.58%    | -3.88%             | -43.06% |     0.19 |       83 | 59.57%     | ok               |
|          40 | 1.17%    | -3.88%             | -36.21% |     0.17 |       72 | 39.43%     | ok               |

## NVDA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -36.17%  | 87.42%             | -43.08% |    -0.55 |       78 | 44.21%     | ok               |
|          20 | -44.65%  | 87.42%             | -44.65% |    -0.63 |       78 | 52.23%     | ok               |
|          25 | -44.56%  | 87.42%             | -44.56% |    -0.69 |       79 | 47.24%     | ok               |
|          15 | -50.14%  | 87.42%             | -53.41% |    -0.72 |       77 | 55.61%     | ok               |
|          35 | -45.77%  | 87.42%             | -51.54% |    -0.82 |       88 | 41.35%     | ok               |

## OP-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 23.99%   | -82.46%            | -30.20% |     0.5  |       32 | 9.20%      | ok               |
|          45 | 19.98%   | -82.46%            | -28.24% |     0.42 |       34 | 13.79%     | ok               |
|          40 | -5.98%   | -82.46%            | -43.36% |     0.11 |       46 | 22.03%     | ok               |
|          15 | -45.81%  | -82.46%            | -55.83% |    -0.3  |       72 | 44.25%     | ok               |
|          35 | -35.85%  | -82.46%            | -56.61% |    -0.31 |       58 | 27.01%     | ok               |

## ORCL Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 168.14%  | 4.33%              | -32.54% |     1.12 |       69 | 61.40%     | ok               |
|          25 | 115.59%  | 4.33%              | -27.76% |     0.93 |       61 | 53.91%     | ok               |
|          45 | 100.42%  | 4.33%              | -32.35% |     0.92 |       58 | 39.43%     | ok               |
|          35 | 105.38%  | 4.33%              | -31.95% |     0.91 |       62 | 48.09%     | ok               |
|          20 | 109.58%  | 4.33%              | -29.32% |     0.9  |       70 | 57.07%     | ok               |

## OXY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 3.04%    | 0.69%              | -28.48% |     0.18 |       73 | 42.76%     | ok               |
|          35 | 1.88%    | 0.69%              | -26.37% |     0.15 |       74 | 38.60%     | ok               |
|          50 | -0.49%   | 0.69%              | -26.34% |     0.1  |       46 | 27.62%     | ok               |
|          40 | -4.40%   | 0.69%              | -28.30% |     0.03 |       64 | 34.44%     | ok               |
|          25 | -11.22%  | 0.69%              | -38.51% |    -0.07 |       79 | 46.42%     | ok               |

## PEP Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 17.82%   | -26.13%            | -11.62% |     0.75 |       36 | 24.79%     | ok               |
|          45 | 10.30%   | -26.13%            | -14.22% |     0.45 |       52 | 28.79%     | ok               |
|          35 | 7.07%    | -26.13%            | -21.42% |     0.28 |       73 | 39.10%     | ok               |
|          40 | 4.76%    | -26.13%            | -18.04% |     0.23 |       66 | 34.44%     | ok               |
|          30 | 0.17%    | -26.13%            | -21.35% |     0.08 |       76 | 45.42%     | ok               |

## PEPE-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -50.17%  | -68.10%            | -61.29% |    -0.34 |       81 | 47.51%     | ok               |
|          25 | -56.58%  | -68.10%            | -64.26% |    -0.44 |       91 | 52.49%     | ok               |
|          15 | -65.38%  | -68.10%            | -65.38% |    -0.46 |       80 | 61.69%     | ok               |
|          35 | -51.85%  | -68.10%            | -61.54% |    -0.46 |       70 | 42.53%     | ok               |
|          20 | -61.99%  | -68.10%            | -63.30% |    -0.48 |       86 | 58.24%     | ok               |

## PFE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -13.17%  | 2.42%              | -23.37% |    -0.4  |       50 | 21.46%     | ok               |
|          40 | -14.79%  | 2.42%              | -27.08% |    -0.44 |       70 | 26.46%     | ok               |
|          50 | -13.66%  | 2.42%              | -25.42% |    -0.47 |       38 | 18.30%     | ok               |
|          35 | -23.00%  | 2.42%              | -32.87% |    -0.7  |       80 | 32.95%     | ok               |
|          30 | -34.49%  | 2.42%              | -41.77% |    -1.08 |       79 | 36.44%     | ok               |

## PG Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -8.07%   | -3.62%             | -17.50% |    -0.31 |       56 | 27.62%     | ok               |
|          35 | -13.54%  | -3.62%             | -18.57% |    -0.53 |       64 | 31.28%     | ok               |
|          45 | -17.47%  | -3.62%             | -19.90% |    -0.79 |       56 | 24.96%     | ok               |
|          30 | -21.40%  | -3.62%             | -24.16% |    -0.84 |       66 | 34.44%     | ok               |
|          25 | -23.19%  | -3.62%             | -25.46% |    -0.92 |       78 | 35.94%     | ok               |

## PM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | -4.46%   | 105.34%            | -32.20% |    -0.01 |       84 | 46.26%     | ok               |
|          20 | -6.96%   | 105.34%            | -33.51% |    -0.06 |       83 | 54.91%     | ok               |
|          30 | -7.46%   | 105.34%            | -35.15% |    -0.08 |       79 | 49.75%     | ok               |
|          40 | -11.76%  | 105.34%            | -37.94% |    -0.22 |       78 | 42.26%     | ok               |
|          50 | -11.29%  | 105.34%            | -35.70% |    -0.23 |       68 | 36.44%     | ok               |

## POL-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 52.93%   | -61.62%            | -38.69% |     0.68 |       77 | 49.62%     | ok               |
|          25 | 32.14%   | -61.62%            | -38.69% |     0.52 |       69 | 54.79%     | ok               |
|          20 | 24.22%   | -61.62%            | -41.66% |     0.45 |       77 | 58.24%     | ok               |
|          40 | 3.00%    | -61.62%            | -31.98% |     0.22 |       58 | 31.03%     | ok               |
|          15 | -3.43%   | -61.62%            | -46.81% |     0.2  |       82 | 61.88%     | ok               |

## QCOM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -14.69%  | -18.18%            | -54.50% |    -0.01 |       71 | 44.93%     | ok               |
|          20 | -20.97%  | -18.18%            | -54.38% |    -0.09 |       67 | 48.25%     | ok               |
|          35 | -21.90%  | -18.18%            | -50.58% |    -0.14 |       79 | 40.60%     | ok               |
|          15 | -30.52%  | -18.18%            | -57.94% |    -0.23 |       69 | 50.92%     | ok               |
|          30 | -31.01%  | -18.18%            | -56.59% |    -0.28 |       77 | 43.09%     | ok               |

## QQQ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 21.30%   | 55.00%             | -14.17% |     0.54 |       63 | 53.91%     | ok               |
|          25 | 13.22%   | 55.00%             | -12.88% |     0.4  |       61 | 47.75%     | ok               |
|          20 | 12.06%   | 55.00%             | -12.98% |     0.37 |       69 | 50.42%     | ok               |
|          30 | 5.57%    | 55.00%             | -14.20% |     0.22 |       66 | 45.76%     | ok               |
|          35 | -5.27%   | 55.00%             | -20.59% |    -0.07 |       72 | 41.93%     | ok               |

## RENDER-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 27.03%   | -61.00%            | -44.59% |     0.49 |       82 | 61.69%     | ok               |
|          20 | 24.34%   | -61.00%            | -43.43% |     0.47 |       85 | 58.43%     | ok               |
|          25 | 18.59%   | -61.00%            | -41.13% |     0.43 |       85 | 53.45%     | ok               |
|          30 | -21.39%  | -61.00%            | -44.65% |     0.05 |       90 | 47.51%     | ok               |
|          35 | -32.26%  | -61.00%            | -46.00% |    -0.14 |       86 | 41.00%     | ok               |

## RTX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 36.65%   | 82.48%             | -18.66% |     0.78 |       74 | 57.24%     | ok               |
|          25 | 31.98%   | 82.48%             | -18.59% |     0.71 |       62 | 54.58%     | ok               |
|          30 | 26.94%   | 82.48%             | -16.99% |     0.63 |       66 | 51.75%     | ok               |
|          15 | 28.39%   | 82.48%             | -19.55% |     0.63 |       67 | 61.73%     | ok               |
|          35 | 21.84%   | 82.48%             | -18.00% |     0.59 |       58 | 48.42%     | ok               |

## SBUX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -3.80%   | 23.65%             | -23.55% |     0.02 |       55 | 40.77%     | ok               |
|          40 | -4.77%   | 23.65%             | -25.43% |    -0.03 |       60 | 32.45%     | ok               |
|          45 | -6.16%   | 23.65%             | -27.26% |    -0.08 |       66 | 27.45%     | ok               |
|          35 | -9.05%   | 23.65%             | -26.54% |    -0.11 |       58 | 35.61%     | ok               |
|          20 | -15.27%  | 23.65%             | -30.94% |    -0.21 |       58 | 42.76%     | ok               |

## SCHW Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -1.40%   | 27.25%             | -28.76% |     0.06 |       67 | 48.75%     | ok               |
|          20 | -2.61%   | 27.25%             | -29.24% |     0.03 |       75 | 51.08%     | ok               |
|          45 | -2.78%   | 27.25%             | -16.53% |    -0.02 |       60 | 30.62%     | ok               |
|          50 | -4.01%   | 27.25%             | -13.28% |    -0.09 |       52 | 27.62%     | ok               |
|          15 | -11.93%  | 27.25%             | -31.37% |    -0.19 |       85 | 55.74%     | ok               |

## SHIB-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -22.62%  | -65.66%            | -45.04% |    -0.07 |       86 | 66.67%     | ok               |
|          35 | -20.98%  | -65.66%            | -44.56% |    -0.11 |       71 | 46.55%     | ok               |
|          25 | -24.90%  | -65.66%            | -45.06% |    -0.13 |       78 | 58.24%     | ok               |
|          20 | -26.62%  | -65.66%            | -47.68% |    -0.14 |       78 | 61.88%     | ok               |
|          40 | -21.89%  | -65.66%            | -41.69% |    -0.15 |       60 | 38.51%     | ok               |

## SHY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd    |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:-------|---------:|---------:|:-----------|:-----------------|
|          30 | -1.87%   | -0.01%             | -3.30% |    -0.63 |       48 | 36.94%     | ok               |
|          35 | -2.39%   | -0.01%             | -3.61% |    -0.82 |       52 | 35.27%     | ok               |
|          40 | -2.41%   | -0.01%             | -3.58% |    -0.83 |       54 | 33.94%     | ok               |
|          45 | -2.43%   | -0.01%             | -3.43% |    -0.89 |       54 | 28.45%     | ok               |
|          50 | -2.67%   | -0.01%             | -3.40% |    -1.03 |       48 | 24.79%     | ok               |

## SKY-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | -57.56%  | -8.20%             | -60.48% |    -0.95 |       82 | 35.63%     | ok               |
|          15 | -65.41%  | -8.20%             | -64.95% |    -0.98 |       79 | 53.64%     | ok               |
|          30 | -62.50%  | -8.20%             | -64.20% |    -1.05 |       89 | 43.10%     | ok               |
|          45 | -59.80%  | -8.20%             | -60.61% |    -1.12 |       76 | 27.20%     | ok               |
|          25 | -66.42%  | -8.20%             | -67.25% |    -1.14 |       82 | 46.36%     | ok               |

## SLB Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -2.61%   | 7.05%              | -29.11% |     0.05 |       50 | 35.44%     | ok               |
|          45 | -2.91%   | 7.05%              | -25.80% |     0.04 |       62 | 31.95%     | ok               |
|          50 | -9.27%   | 7.05%              | -30.30% |    -0.13 |       50 | 25.79%     | ok               |
|          35 | -27.50%  | 7.05%              | -48.78% |    -0.49 |       74 | 43.26%     | ok               |
|          25 | -36.77%  | 7.05%              | -55.67% |    -0.66 |       84 | 53.08%     | ok               |

## SLV Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 49.26%   | 85.69%             | -34.04% |     0.71 |       54 | 30.12%     | ok               |
|          45 | 36.59%   | 85.69%             | -31.75% |     0.59 |       65 | 31.61%     | ok               |
|          40 | 35.51%   | 85.69%             | -34.28% |     0.57 |       69 | 33.61%     | ok               |
|          20 | 24.41%   | 85.69%             | -42.60% |     0.45 |       72 | 43.93%     | ok               |
|          15 | 24.39%   | 85.69%             | -47.98% |     0.44 |       73 | 48.75%     | ok               |

## SMH Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 62.37%   | 120.99%            | -31.01% |     0.91 |       47 | 46.26%     | ok               |
|          25 | 47.68%   | 120.99%            | -32.94% |     0.78 |       44 | 44.76%     | ok               |
|          35 | 46.11%   | 120.99%            | -34.03% |     0.77 |       54 | 41.76%     | ok               |
|          30 | 43.66%   | 120.99%            | -33.66% |     0.73 |       48 | 43.43%     | ok               |
|          45 | 31.94%   | 120.99%            | -33.35% |     0.63 |       54 | 36.11%     | ok               |

## SNX-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 10.80%   | -72.80%            | -41.29% |     0.33 |       56 | 27.97%     | ok               |
|          20 | 8.36%    | -72.80%            | -53.03% |     0.32 |       73 | 43.87%     | ok               |
|          40 | 4.91%    | -72.80%            | -36.00% |     0.24 |       46 | 22.61%     | ok               |
|          30 | -4.03%   | -72.80%            | -50.74% |     0.17 |       62 | 34.10%     | ok               |
|          15 | -21.70%  | -72.80%            | -54.74% |     0.01 |       79 | 48.47%     | ok               |

## SOL-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 33.62%   | -37.20%            | -39.83% |     0.55 |       64 | 39.27%     | ok               |
|          35 | 11.28%   | -37.20%            | -43.79% |     0.34 |       78 | 45.79%     | ok               |
|          45 | 10.22%   | -37.20%            | -46.91% |     0.31 |       60 | 34.10%     | ok               |
|          15 | -0.71%   | -37.20%            | -46.84% |     0.23 |       74 | 63.79%     | ok               |
|          50 | -0.73%   | -37.20%            | -46.56% |     0.16 |       60 | 28.16%     | ok               |

## SOXX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | 59.73%   | 106.82%            | -39.65% |     0.85 |       54 | 44.93%     | ok               |
|          35 | 56.99%   | 106.82%            | -38.76% |     0.85 |       56 | 40.27%     | ok               |
|          30 | 55.30%   | 106.82%            | -40.14% |     0.82 |       56 | 42.76%     | ok               |
|          20 | 47.67%   | 106.82%            | -38.67% |     0.73 |       59 | 45.76%     | ok               |
|          40 | 37.78%   | 106.82%            | -41.03% |     0.65 |       58 | 38.10%     | ok               |

## SPY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 11.09%   | 44.16%             | -14.25% |     0.42 |       59 | 52.75%     | ok               |
|          15 | 10.56%   | 44.16%             | -16.80% |     0.39 |       63 | 55.41%     | ok               |
|          25 | 6.10%    | 44.16%             | -14.25% |     0.26 |       59 | 51.75%     | ok               |
|          30 | -0.06%   | 44.16%             | -15.53% |     0.06 |       64 | 49.08%     | ok               |
|          35 | -1.02%   | 44.16%             | -15.58% |     0.02 |       62 | 45.92%     | ok               |

## SUSHI-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -0.40%   | -70.22%            | -34.75% |     0.16 |       52 | 16.48%     | ok               |
|          40 | -40.26%  | -70.22%            | -60.82% |    -0.4  |       59 | 28.35%     | ok               |
|          45 | -38.58%  | -70.22%            | -57.99% |    -0.43 |       56 | 21.46%     | ok               |
|          35 | -53.25%  | -70.22%            | -67.69% |    -0.61 |       80 | 33.33%     | ok               |
|          15 | -71.98%  | -70.22%            | -78.43% |    -0.88 |       89 | 49.62%     | ok               |

## T Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 61.87%   | 33.94%             | -15.08% |     1.05 |       73 | 65.56%     | ok               |
|          20 | 57.88%   | 33.94%             | -18.13% |     1.03 |       68 | 61.06%     | ok               |
|          25 | 56.09%   | 33.94%             | -17.66% |     1.01 |       68 | 58.90%     | ok               |
|          30 | 41.56%   | 33.94%             | -17.01% |     0.83 |       72 | 56.74%     | ok               |
|          35 | 26.13%   | 33.94%             | -14.49% |     0.6  |       78 | 52.41%     | ok               |

## TGT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -11.06%  | 6.22%              | -34.42% |    -0.16 |       60 | 37.60%     | ok               |
|          45 | -11.97%  | 6.22%              | -25.85% |    -0.23 |       48 | 28.62%     | ok               |
|          20 | -16.69%  | 6.22%              | -38.96% |    -0.25 |       88 | 45.42%     | ok               |
|          25 | -15.22%  | 6.22%              | -37.81% |    -0.25 |       70 | 40.77%     | ok               |
|          35 | -17.42%  | 6.22%              | -32.35% |    -0.35 |       60 | 33.94%     | ok               |

## TIA-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -13.53%  | -77.21%            | -66.82% |     0.23 |       95 | 58.62%     | ok               |
|          25 | -15.65%  | -77.21%            | -69.36% |     0.17 |       90 | 48.08%     | ok               |
|          20 | -29.40%  | -77.21%            | -71.87% |     0.06 |       89 | 53.45%     | ok               |
|          35 | -19.12%  | -77.21%            | -66.58% |     0.04 |       74 | 35.82%     | ok               |
|          30 | -39.58%  | -77.21%            | -75.93% |    -0.12 |       91 | 42.91%     | ok               |

## TLT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -10.32%  | -12.40%            | -12.71% |    -1.11 |       34 | 17.64%     | ok               |
|          40 | -15.23%  | -12.40%            | -17.65% |    -1.32 |       52 | 25.12%     | ok               |
|          45 | -13.84%  | -12.40%            | -15.22% |    -1.41 |       44 | 20.63%     | ok               |
|          30 | -19.87%  | -12.40%            | -21.85% |    -1.49 |       68 | 33.44%     | ok               |
|          35 | -20.01%  | -12.40%            | -21.33% |    -1.66 |       66 | 28.79%     | ok               |

## TMO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 55.68%   | 18.14%             | -8.17%  |     1.15 |       48 | 34.78%     | ok               |
|          45 | 43.76%   | 18.14%             | -9.69%  |     0.92 |       56 | 39.60%     | ok               |
|          40 | 37.42%   | 18.14%             | -9.91%  |     0.8  |       61 | 44.59%     | ok               |
|          35 | 38.90%   | 18.14%             | -13.84% |     0.77 |       71 | 50.25%     | ok               |
|          20 | 36.94%   | 18.14%             | -22.89% |     0.69 |       78 | 61.40%     | ok               |

## TMUS Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -4.78%   | -4.16%             | -33.01% |    -0    |       74 | 48.25%     | ok               |
|          15 | -10.39%  | -4.16%             | -41.03% |    -0.11 |       68 | 60.90%     | ok               |
|          50 | -7.84%   | -4.16%             | -32.38% |    -0.14 |       60 | 34.44%     | ok               |
|          25 | -13.85%  | -4.16%             | -39.27% |    -0.21 |       77 | 51.25%     | ok               |
|          20 | -15.56%  | -4.16%             | -39.78% |    -0.24 |       74 | 55.24%     | ok               |

## TRX-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 10.49%   | 21.84%             | -18.79% |     0.39 |       54 | 38.89%     | ok               |
|          35 | 4.01%    | 21.84%             | -21.77% |     0.2  |       66 | 47.13%     | ok               |
|          20 | 1.57%    | 21.84%             | -25.45% |     0.13 |       61 | 56.90%     | ok               |
|          30 | 1.50%    | 21.84%             | -22.90% |     0.13 |       66 | 50.00%     | ok               |
|          45 | 0.79%    | 21.84%             | -22.76% |     0.1  |       46 | 35.25%     | ok               |

## TSLA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 34.46%   | 97.90%             | -34.01% |     0.54 |       66 | 29.95%     | ok               |
|          40 | 8.08%    | 97.90%             | -52.58% |     0.28 |       65 | 35.44%     | ok               |
|          45 | -14.96%  | 97.90%             | -54.39% |     0.01 |       71 | 32.45%     | ok               |
|          35 | -20.51%  | 97.90%             | -60.12% |    -0.03 |       76 | 38.10%     | ok               |
|          30 | -35.00%  | 97.90%             | -59.64% |    -0.22 |       78 | 42.76%     | ok               |

## TXN Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 5.97%    | 38.81%             | -44.65% |     0.22 |       68 | 32.45%     | ok               |
|          35 | -13.94%  | 38.81%             | -42.44% |    -0.1  |       78 | 47.09%     | ok               |
|          40 | -15.44%  | 38.81%             | -44.87% |    -0.13 |       74 | 44.76%     | ok               |
|          20 | -20.05%  | 38.81%             | -37.58% |    -0.14 |       68 | 56.91%     | ok               |
|          45 | -16.08%  | 38.81%             | -45.45% |    -0.15 |       82 | 38.44%     | ok               |

## UNH Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 33.68%   | -21.00%            | -36.92% |     0.59 |       54 | 28.45%     | ok               |
|          30 | 32.94%   | -21.00%            | -26.31% |     0.55 |       77 | 48.42%     | ok               |
|          35 | 28.89%   | -21.00%            | -27.21% |     0.51 |       72 | 43.43%     | ok               |
|          20 | 28.71%   | -21.00%            | -26.96% |     0.5  |       80 | 57.74%     | ok               |
|          15 | 28.67%   | -21.00%            | -26.07% |     0.49 |       85 | 63.89%     | ok               |

## UNI-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 102.12%  | 20.02%             | -21.42% |     1.01 |       48 | 25.86%     | ok               |
|          45 | 85.00%   | 20.02%             | -30.17% |     0.87 |       54 | 33.33%     | ok               |
|          40 | 60.77%   | 20.02%             | -43.84% |     0.72 |       58 | 38.51%     | ok               |
|          35 | 37.16%   | 20.02%             | -50.47% |     0.55 |       66 | 43.87%     | ok               |
|          20 | -29.03%  | 20.02%             | -69.70% |     0.03 |       92 | 59.00%     | ok               |

## UPS Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | -28.56%  | -29.70%            | -31.52% |    -0.53 |       62 | 36.27%     | ok               |
|          40 | -28.35%  | -29.70%            | -31.55% |    -0.54 |       58 | 30.78%     | ok               |
|          20 | -36.88%  | -29.70%            | -38.76% |    -0.71 |       84 | 49.92%     | ok               |
|          25 | -37.38%  | -29.70%            | -39.25% |    -0.74 |       76 | 46.59%     | ok               |
|          15 | -39.11%  | -29.70%            | -40.92% |    -0.75 |       86 | 53.74%     | ok               |

## USO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 6.59%    | 114.68%            | -42.21% |     0.24 |       67 | 41.10%     | ok               |
|          20 | 5.72%    | 114.68%            | -43.58% |     0.23 |       72 | 37.60%     | ok               |
|          45 | 5.79%    | 114.68%            | -33.44% |     0.22 |       48 | 25.79%     | ok               |
|          25 | -4.18%   | 114.68%            | -45.85% |     0.08 |       68 | 35.27%     | ok               |
|          50 | -3.42%   | 114.68%            | -29.54% |     0.07 |       52 | 24.13%     | ok               |

## VEA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 7.87%    | 37.09%             | -15.99% |     0.33 |       54 | 50.08%     | ok               |
|          20 | 1.59%    | 37.09%             | -17.04% |     0.12 |       59 | 47.42%     | ok               |
|          25 | -2.28%   | 37.09%             | -17.13% |    -0.04 |       57 | 45.42%     | ok               |
|          30 | -3.80%   | 37.09%             | -17.27% |    -0.11 |       64 | 42.26%     | ok               |
|          35 | -4.69%   | 37.09%             | -16.11% |    -0.15 |       52 | 40.27%     | ok               |

## VIXY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -57.34%  | -60.21%            | -69.78% |    -0.69 |       36 | 8.99%      | ok               |
|          15 | -78.07%  | -60.21%            | -89.47% |    -0.83 |       95 | 42.93%     | ok               |
|          45 | -66.49%  | -60.21%            | -75.03% |    -0.9  |       56 | 13.98%     | ok               |
|          30 | -78.70%  | -60.21%            | -88.17% |    -0.96 |       94 | 31.95%     | ok               |
|          20 | -82.47%  | -60.21%            | -90.58% |    -1.02 |       91 | 38.94%     | ok               |

## VNQ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -7.58%   | 12.09%             | -19.07% |    -0.33 |       60 | 28.12%     | ok               |
|          50 | -8.50%   | 12.09%             | -17.13% |    -0.39 |       52 | 24.79%     | ok               |
|          25 | -10.91%  | 12.09%             | -22.34% |    -0.4  |       69 | 42.60%     | ok               |
|          40 | -12.47%  | 12.09%             | -24.84% |    -0.54 |       78 | 33.61%     | ok               |
|          30 | -13.66%  | 12.09%             | -24.92% |    -0.54 |       73 | 39.77%     | ok               |

## VTI Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 12.08%   | 42.85%             | -13.96% |     0.45 |       62 | 53.24%     | ok               |
|          15 | 7.47%    | 42.85%             | -15.70% |     0.3  |       59 | 55.57%     | ok               |
|          25 | 0.12%    | 42.85%             | -15.00% |     0.07 |       58 | 51.08%     | ok               |
|          30 | -7.39%   | 42.85%             | -17.64% |    -0.21 |       68 | 49.08%     | ok               |
|          40 | -8.50%   | 42.85%             | -19.77% |    -0.28 |       72 | 41.60%     | ok               |

## VWO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -10.07%  | 31.29%             | -22.18% |    -0.38 |       56 | 27.95%     | ok               |
|          15 | -13.19%  | 31.29%             | -24.01% |    -0.42 |       74 | 46.26%     | ok               |
|          45 | -11.26%  | 31.29%             | -23.75% |    -0.43 |       58 | 30.62%     | ok               |
|          40 | -11.72%  | 31.29%             | -23.57% |    -0.44 |       68 | 33.44%     | ok               |
|          20 | -14.57%  | 31.29%             | -26.14% |    -0.49 |       71 | 43.93%     | ok               |

## VZ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -3.10%   | 12.71%             | -12.96% |    -0.04 |       56 | 28.62%     | ok               |
|          20 | -22.91%  | 12.71%             | -35.02% |    -0.46 |       78 | 51.41%     | ok               |
|          25 | -19.77%  | 12.71%             | -25.46% |    -0.52 |       81 | 46.42%     | ok               |
|          35 | -18.33%  | 12.71%             | -26.48% |    -0.53 |       62 | 38.60%     | ok               |
|          45 | -17.82%  | 12.71%             | -25.50% |    -0.54 |       70 | 32.78%     | ok               |

## WFC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | -8.30%   | 39.30%             | -21.57% |    -0.11 |       77 | 43.59%     | ok               |
|          50 | -8.06%   | 39.30%             | -18.29% |    -0.19 |       60 | 32.45%     | ok               |
|          30 | -17.86%  | 39.30%             | -28.90% |    -0.3  |       80 | 46.76%     | ok               |
|          20 | -20.87%  | 39.30%             | -29.87% |    -0.32 |       79 | 52.58%     | ok               |
|          40 | -13.97%  | 39.30%             | -23.94% |    -0.34 |       72 | 40.27%     | ok               |

## WIF-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 18.08%   | -80.19%            | -40.67% |     0.42 |       67 | 44.64%     | ok               |
|          15 | -7.72%   | -80.19%            | -46.21% |     0.22 |       77 | 47.89%     | ok               |
|          25 | -7.94%   | -80.19%            | -44.74% |     0.2  |       65 | 40.80%     | ok               |
|          30 | -27.56%  | -80.19%            | -52.76% |    -0.02 |       66 | 38.12%     | ok               |
|          40 | -23.27%  | -80.19%            | -51.66% |    -0.09 |       62 | 26.63%     | ok               |

## WMT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 35.43%   | 81.72%             | -12.18% |     1.08 |       36 | 36.77%     | ok               |
|          45 | 34.30%   | 81.72%             | -14.14% |     1.01 |       42 | 39.10%     | ok               |
|          35 | 24.50%   | 81.72%             | -18.25% |     0.72 |       58 | 45.42%     | ok               |
|          40 | 22.90%   | 81.72%             | -18.53% |     0.7  |       50 | 40.77%     | ok               |
|          15 | 6.22%    | 81.72%             | -26.24% |     0.23 |       82 | 59.40%     | ok               |

## XBI Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 13.65%   | 62.47%             | -16.08% |     0.41 |       52 | 34.11%     | ok               |
|          45 | 9.33%    | 62.47%             | -15.46% |     0.31 |       50 | 31.61%     | ok               |
|          35 | 1.05%    | 62.47%             | -17.66% |     0.11 |       60 | 37.10%     | ok               |
|          50 | 0.10%    | 62.47%             | -15.41% |     0.08 |       50 | 28.62%     | ok               |
|          30 | -1.06%   | 62.47%             | -17.92% |     0.06 |       62 | 38.60%     | ok               |

## XLB Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -1.45%   | 11.47%             | -15.73% |    -0.01 |       40 | 21.96%     | ok               |
|          40 | -2.35%   | 11.47%             | -17.29% |    -0.04 |       56 | 26.12%     | ok               |
|          45 | -4.97%   | 11.47%             | -17.09% |    -0.16 |       44 | 23.63%     | ok               |
|          35 | -6.54%   | 11.47%             | -20.65% |    -0.2  |       58 | 29.45%     | ok               |
|          25 | -10.89%  | 11.47%             | -22.30% |    -0.36 |       66 | 35.61%     | ok               |

## XLC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 12.47%   | 33.00%             | -12.33% |     0.47 |       61 | 49.92%     | ok               |
|          25 | 11.92%   | 33.00%             | -12.31% |     0.45 |       60 | 52.08%     | ok               |
|          50 | 7.09%    | 33.00%             | -11.12% |     0.37 |       64 | 38.10%     | ok               |
|          40 | 7.66%    | 33.00%             | -13.38% |     0.34 |       62 | 43.59%     | ok               |
|          35 | 6.94%    | 33.00%             | -13.38% |     0.31 |       60 | 47.42%     | ok               |

## XLE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 2.71%    | 49.37%             | -25.98% |     0.15 |       56 | 36.94%     | ok               |
|          35 | 0.42%    | 49.37%             | -26.89% |     0.1  |       65 | 43.59%     | ok               |
|          45 | -0.68%   | 49.37%             | -28.46% |     0.06 |       60 | 39.10%     | ok               |
|          30 | -1.23%   | 49.37%             | -29.67% |     0.06 |       69 | 45.76%     | ok               |
|          25 | -5.88%   | 49.37%             | -32.98% |    -0.05 |       79 | 48.92%     | ok               |

## XLF Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -1.32%   | 33.43%             | -18.63% |     0.02 |       76 | 51.58%     | ok               |
|          15 | -1.47%   | 33.43%             | -20.19% |     0.02 |       78 | 54.58%     | ok               |
|          25 | -8.20%   | 33.43%             | -23.22% |    -0.24 |       83 | 48.42%     | ok               |
|          30 | -8.80%   | 33.43%             | -23.61% |    -0.27 |       84 | 46.42%     | ok               |
|          35 | -15.90%  | 33.43%             | -24.48% |    -0.61 |       74 | 42.76%     | ok               |

## XLI Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 5.22%    | 34.79%             | -11.40% |     0.23 |       86 | 51.41%     | ok               |
|          20 | 1.42%    | 34.79%             | -12.74% |     0.11 |       75 | 46.42%     | ok               |
|          50 | -4.76%   | 34.79%             | -14.94% |    -0.18 |       60 | 31.78%     | ok               |
|          45 | -5.38%   | 34.79%             | -16.29% |    -0.19 |       70 | 34.28%     | ok               |
|          25 | -8.78%   | 34.79%             | -17.03% |    -0.29 |       78 | 44.43%     | ok               |

## XLK Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 68.18%   | 70.52%             | -14.75% |     1.13 |       45 | 51.58%     | ok               |
|          20 | 61.76%   | 70.52%             | -14.75% |     1.09 |       48 | 49.25%     | ok               |
|          25 | 56.08%   | 70.52%             | -14.75% |     1.05 |       44 | 47.25%     | ok               |
|          30 | 46.74%   | 70.52%             | -14.75% |     0.94 |       44 | 45.92%     | ok               |
|          35 | 30.37%   | 70.52%             | -14.71% |     0.7  |       56 | 43.26%     | ok               |

## XLM-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | 19.10%   | -39.02%            | -49.14% |     0.41 |       70 | 49.81%     | ok               |
|          40 | 12.69%   | -39.02%            | -47.28% |     0.34 |       52 | 36.97%     | ok               |
|          30 | 8.66%    | -39.02%            | -54.58% |     0.31 |       68 | 47.70%     | ok               |
|          50 | 6.55%    | -39.02%            | -48.81% |     0.26 |       44 | 26.05%     | ok               |
|          45 | 2.47%    | -39.02%            | -51.28% |     0.22 |       56 | 31.03%     | ok               |

## XLP Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 15.50%   | 13.64%             | -5.66%  |     0.93 |       52 | 29.62%     | ok               |
|          40 | 12.81%   | 13.64%             | -7.77%  |     0.75 |       70 | 33.61%     | ok               |
|          50 | 11.42%   | 13.64%             | -6.08%  |     0.72 |       58 | 27.45%     | ok               |
|          35 | 11.83%   | 13.64%             | -9.73%  |     0.68 |       66 | 36.61%     | ok               |
|          30 | 8.59%    | 13.64%             | -10.28% |     0.5  |       67 | 38.44%     | ok               |

## XLU Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 6.01%    | 18.07%             | -14.03% |     0.33 |       54 | 29.95%     | ok               |
|          45 | 4.85%    | 18.07%             | -14.97% |     0.27 |       58 | 31.11%     | ok               |
|          40 | 1.79%    | 18.07%             | -16.41% |     0.13 |       64 | 33.11%     | ok               |
|          35 | -0.92%   | 18.07%             | -19.71% |     0    |       64 | 35.77%     | ok               |
|          30 | -5.20%   | 18.07%             | -20.40% |    -0.18 |       69 | 39.27%     | ok               |

## XLV Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -21.04%  | 22.36%             | -22.40% |    -0.99 |       76 | 38.10%     | ok               |
|          30 | -21.39%  | 22.36%             | -22.75% |    -1.03 |       76 | 36.44%     | ok               |
|          15 | -24.30%  | 22.36%             | -24.70% |    -1.13 |       83 | 42.26%     | ok               |
|          20 | -24.13%  | 22.36%             | -24.54% |    -1.15 |       79 | 39.77%     | ok               |
|          35 | -25.31%  | 22.36%             | -26.58% |    -1.31 |       70 | 33.44%     | ok               |

## XLY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -0.70%   | 28.13%             | -15.77% |     0.06 |       76 | 54.24%     | ok               |
|          30 | -4.15%   | 28.13%             | -18.35% |    -0.06 |       75 | 47.59%     | ok               |
|          20 | -5.95%   | 28.13%             | -19.25% |    -0.1  |       72 | 50.92%     | ok               |
|          25 | -8.05%   | 28.13%             | -19.98% |    -0.17 |       69 | 49.42%     | ok               |
|          50 | -6.34%   | 28.13%             | -15.82% |    -0.22 |       62 | 32.11%     | ok               |

## XOM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | 5.22%    | 57.80%             | -19.90% |     0.22 |       57 | 35.11%     | ok               |
|          50 | 4.40%    | 57.80%             | -21.35% |     0.2  |       40 | 27.29%     | ok               |
|          30 | 4.18%    | 57.80%             | -20.29% |     0.19 |       57 | 34.44%     | ok               |
|          20 | -0.76%   | 57.80%             | -25.56% |     0.06 |       64 | 37.44%     | ok               |
|          45 | -0.81%   | 57.80%             | -23.33% |     0.05 |       44 | 28.45%     | ok               |

## XRP-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 27.16%   | -44.97%            | -31.38% |     0.49 |       72 | 42.91%     | ok               |
|          40 | 7.40%    | -44.97%            | -33.91% |     0.28 |       66 | 36.40%     | ok               |
|          30 | -4.95%   | -44.97%            | -31.82% |     0.15 |       67 | 47.89%     | ok               |
|          45 | -4.52%   | -44.97%            | -37.18% |     0.12 |       60 | 31.03%     | ok               |
|          50 | -8.57%   | -44.97%            | -39.26% |     0.05 |       58 | 23.37%     | ok               |

## YFI-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -44.21%  | -60.72%            | -44.21% |    -0.73 |       56 | 26.63%     | ok               |
|          35 | -53.55%  | -60.72%            | -53.55% |    -0.94 |       62 | 33.14%     | ok               |
|          45 | -47.38%  | -60.72%            | -47.38% |    -1.06 |       68 | 21.84%     | ok               |
|          30 | -59.62%  | -60.72%            | -60.97% |    -1.09 |       76 | 37.16%     | ok               |
|          25 | -62.70%  | -60.72%            | -63.96% |    -1.14 |       77 | 41.76%     | ok               |

## ZEC-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 216.96%  | 2780.05%           | -30.64% |     1.11 |       46 | 31.61%     | ok               |
|          35 | 175.01%  | 2780.05%           | -50.84% |     0.99 |       52 | 37.16%     | ok               |
|          30 | 160.57%  | 2780.05%           | -56.50% |     0.95 |       57 | 40.61%     | ok               |
|          25 | 153.14%  | 2780.05%           | -58.07% |     0.93 |       55 | 43.30%     | ok               |
|          40 | 133.09%  | 2780.05%           | -54.22% |     0.89 |       54 | 35.06%     | ok               |
