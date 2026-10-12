# Market Tracker Backtest Report

_Generated: 2026-10-12T05:52:57+00:00_

## Data Sources

- Crypto: Kraken -> Coinbase -> CoinGecko OHLC -> CoinPaprika fallback chain.
- Stocks / ETFs / indices: Stooq -> Yahoo Finance fallback chain.
- Data rows are generated from real market APIs. Mock OHLCV rows are not generated.

## Data Freshness

- Rows: **92,734**
- Symbols: **161**
- Date range: **2024-05-17** to **2026-10-12**

## Latest Signals

| symbol     | date                |         close |   composite_score | signal   | data_source   |
|:-----------|:--------------------|--------------:|------------------:|:---------|:--------------|
| AAVE-USD   | 2026-10-12 00:00:00 |   168.94      |         48        | LONG     | Kraken API    |
| ABBV       | 2026-10-09 00:00:00 |   276.47      |         74.0833   | LONG     | Yahoo Finance |
| ADA-USD    | 2026-10-12 00:00:00 |     0.253448  |         52        | LONG     | Kraken API    |
| ALGO-USD   | 2026-10-12 00:00:00 |     0.13049   |         39.6667   | LONG     | Kraken API    |
| AMAT       | 2026-10-09 00:00:00 |   507.03      |         76.6667   | LONG     | Yahoo Finance |
| AMGN       | 2026-10-09 00:00:00 |   414.87      |         72.9167   | LONG     | Yahoo Finance |
| APT-USD    | 2026-10-12 00:00:00 |     0.8979    |         36.3333   | LONG     | Kraken API    |
| ARB-USD    | 2026-10-12 00:00:00 |     0.1963    |         30.3333   | LONG     | Kraken API    |
| AVAX-USD   | 2026-10-12 00:00:00 |    11.025     |         52        | LONG     | Kraken API    |
| BTC-USD    | 2026-10-12 00:00:00 | 83830.2       |         41.5      | LONG     | Kraken API    |
| COMP-USD   | 2026-10-12 00:00:00 |    25.18      |         52        | LONG     | Kraken API    |
| COP        | 2026-10-09 00:00:00 |   134.1       |         74.0833   | LONG     | Yahoo Finance |
| CSCO       | 2026-10-09 00:00:00 |   118.39      |         72.9167   | LONG     | Yahoo Finance |
| DIA        | 2026-10-09 00:00:00 |   516.11      |         39.75     | LONG     | Yahoo Finance |
| DXY-INDEX  | 2026-10-12 00:00:00 |   102.232     |         79.5699   | LONG     | Yahoo Finance |
| FET-USD    | 2026-10-12 00:00:00 |     0.2389    |         48        | LONG     | Kraken API    |
| GRT-USD    | 2026-10-12 00:00:00 |     0.02792   |         32.3333   | LONG     | Kraken API    |
| ICP-USD    | 2026-10-12 00:00:00 |     3.475     |         52        | LONG     | Kraken API    |
| INJ-USD    | 2026-10-12 00:00:00 |     8.128     |         54.25     | LONG     | Kraken API    |
| LIN        | 2026-10-09 00:00:00 |   483.73      |         40.5      | LONG     | Yahoo Finance |
| LLY        | 2026-10-09 00:00:00 |  1179.27      |         72.4167   | LONG     | Yahoo Finance |
| LRCX       | 2026-10-09 00:00:00 |   318.84      |         45.1667   | LONG     | Yahoo Finance |
| LTC-USD    | 2026-10-12 00:00:00 |    65.3       |         36.3333   | LONG     | Kraken API    |
| META       | 2026-10-09 00:00:00 |   718.67      |         34.4167   | LONG     | Yahoo Finance |
| MSFT       | 2026-10-09 00:00:00 |   535.07      |         71.25     | LONG     | Yahoo Finance |
| NEAR-USD   | 2026-10-12 00:00:00 |     5.8896    |         46        | LONG     | Kraken API    |
| NVDA       | 2026-10-09 00:00:00 |   229.28      |         71.5833   | LONG     | Yahoo Finance |
| OP-USD     | 2026-10-12 00:00:00 |     0.1433    |         50        | LONG     | Kraken API    |
| OXY        | 2026-10-09 00:00:00 |    60.11      |         74.0833   | LONG     | Yahoo Finance |
| QQQ        | 2026-10-09 00:00:00 |   751.27      |         66.4167   | LONG     | Yahoo Finance |
| RENDER-USD | 2026-10-12 00:00:00 |     2.008     |         52        | LONG     | Kraken API    |
| SMH        | 2026-10-09 00:00:00 |   603.33      |         56.5833   | LONG     | Yahoo Finance |
| SOXX       | 2026-10-09 00:00:00 |   559.4       |         35.5833   | LONG     | Yahoo Finance |
| TIA-USD    | 2026-10-12 00:00:00 |     0.5928    |         63.5      | LONG     | Kraken API    |
| TMO        | 2026-10-09 00:00:00 |   658.02      |         34.9167   | LONG     | Yahoo Finance |
| TXN        | 2026-10-09 00:00:00 |   283.74      |         72.75     | LONG     | Yahoo Finance |
| UNH        | 2026-10-09 00:00:00 |   379.3       |         55.6667   | LONG     | Yahoo Finance |
| XLE        | 2026-10-09 00:00:00 |    65.08      |         76.0833   | LONG     | Yahoo Finance |
| XLK        | 2026-10-09 00:00:00 |   198.78      |         73.9167   | LONG     | Yahoo Finance |
| XLP        | 2026-10-09 00:00:00 |    83.43      |         51.4167   | LONG     | Yahoo Finance |
| AAPL       | 2026-10-09 00:00:00 |   336.64      |         30.1667   | NEUTRAL  | Yahoo Finance |
| ADBE       | 2026-10-09 00:00:00 |   242.27      |         -9.5      | NEUTRAL  | Yahoo Finance |
| AMD        | 2026-10-09 00:00:00 |   608.1       |         35.9167   | NEUTRAL  | Yahoo Finance |
| AMZN       | 2026-10-09 00:00:00 |   262.43      |         61.6667   | NEUTRAL  | Yahoo Finance |
| ARKK       | 2026-10-09 00:00:00 |    89.62      |         36.6667   | NEUTRAL  | Yahoo Finance |
| ATOM-USD   | 2026-10-12 00:00:00 |     1.9003    |         59.9167   | NEUTRAL  | Kraken API    |
| AVGO       | 2026-10-09 00:00:00 |   361.54      |        -17.1667   | NEUTRAL  | Yahoo Finance |
| BAC        | 2026-10-09 00:00:00 |    54.32      |        -27        | NEUTRAL  | Yahoo Finance |
| BCH-USD    | 2026-10-12 00:00:00 |   286.79      |         -6.91667  | NEUTRAL  | Kraken API    |
| BITO       | 2026-10-09 00:00:00 |    11         |        -11.9167   | NEUTRAL  | Yahoo Finance |
| BLK        | 2026-10-09 00:00:00 |  1082.39      |         36.0833   | NEUTRAL  | Yahoo Finance |
| BONK-USD   | 2026-10-12 00:00:00 |     3.475e-06 |        -10.6667   | NEUTRAL  | Kraken API    |
| C          | 2026-10-09 00:00:00 |   129.64      |        -27.3333   | NEUTRAL  | Yahoo Finance |
| CAT        | 2026-10-09 00:00:00 |   800.47      |        -24.75     | NEUTRAL  | Yahoo Finance |
| CL         | 2026-10-09 00:00:00 |    88.27      |          6.41667  | NEUTRAL  | Yahoo Finance |
| COST       | 2026-10-09 00:00:00 |   946.92      |         25.75     | NEUTRAL  | Yahoo Finance |
| CRM        | 2026-10-09 00:00:00 |   229.13      |          7.66667  | NEUTRAL  | Yahoo Finance |
| CRV-USD    | 2026-10-12 00:00:00 |     0.36832   |         13.9167   | NEUTRAL  | Kraken API    |
| CVX        | 2026-10-09 00:00:00 |   211.98      |         37.8333   | NEUTRAL  | Yahoo Finance |
| DASH-USD   | 2026-10-12 00:00:00 |    53.256     |        -18.9167   | NEUTRAL  | Kraken API    |
| DBC        | 2026-10-09 00:00:00 |    32.96      |         48.5      | NEUTRAL  | Yahoo Finance |
| DE         | 2026-10-09 00:00:00 |   620.93      |        -19.5833   | NEUTRAL  | Yahoo Finance |
| DIS        | 2026-10-09 00:00:00 |   108.05      |         64.8333   | NEUTRAL  | Yahoo Finance |
| DOT-USD    | 2026-10-12 00:00:00 |     1.2616    |         33.25     | NEUTRAL  | Kraken API    |
| EEM        | 2026-10-09 00:00:00 |    66.8       |        -17.3333   | NEUTRAL  | Yahoo Finance |
| EFA        | 2026-10-09 00:00:00 |   103.4       |        -27.0833   | NEUTRAL  | Yahoo Finance |
| EOG        | 2026-10-09 00:00:00 |   148.16      |         62.8333   | NEUTRAL  | Yahoo Finance |
| ETC-USD    | 2026-10-12 00:00:00 |     8.505     |         22.0833   | NEUTRAL  | Kraken API    |
| ETH-USD    | 2026-10-12 00:00:00 |  2555.48      |         -0.166667 | NEUTRAL  | Kraken API    |
| EWJ        | 2026-10-09 00:00:00 |    97.86      |         42.3333   | NEUTRAL  | Yahoo Finance |
| FCX        | 2026-10-09 00:00:00 |    73.69      |         43.6667   | NEUTRAL  | Yahoo Finance |
| FIL-USD    | 2026-10-12 00:00:00 |     1.245     |         57.0833   | NEUTRAL  | Kraken API    |
| FXI        | 2026-10-09 00:00:00 |    34.24      |        -20        | NEUTRAL  | Yahoo Finance |
| GDX        | 2026-10-09 00:00:00 |    89.28      |        -27.3333   | NEUTRAL  | Yahoo Finance |
| GDXJ       | 2026-10-09 00:00:00 |   114.43      |        -27.3333   | NEUTRAL  | Yahoo Finance |
| GE         | 2026-10-09 00:00:00 |   308.2       |        -45.8333   | NEUTRAL  | Yahoo Finance |
| GOOGL      | 2026-10-09 00:00:00 |   351.66      |         26.25     | NEUTRAL  | Yahoo Finance |
| HBAR-USD   | 2026-10-12 00:00:00 |     0.09462   |         13.0833   | NEUTRAL  | Kraken API    |
| HON        | 2026-10-09 00:00:00 |   207.73      |        -18.4167   | NEUTRAL  | Yahoo Finance |
| IBIT       | 2026-10-09 00:00:00 |    46.55      |         18.4167   | NEUTRAL  | Yahoo Finance |
| IBM        | 2026-10-09 00:00:00 |   227.13      |        -22        | NEUTRAL  | Yahoo Finance |
| IEMG       | 2026-10-09 00:00:00 |    81.4       |        -17.3333   | NEUTRAL  | Yahoo Finance |
| INTC       | 2026-10-09 00:00:00 |   104.7       |         -8.91667  | NEUTRAL  | Yahoo Finance |
| INTU       | 2026-10-09 00:00:00 |   302.75      |         13.75     | NEUTRAL  | Yahoo Finance |
| IWM        | 2026-10-09 00:00:00 |   278.94      |          2.33333  | NEUTRAL  | Yahoo Finance |
| JNJ        | 2026-10-09 00:00:00 |   261.44      |        -40.3333   | NEUTRAL  | Yahoo Finance |
| JPM        | 2026-10-09 00:00:00 |   332.99      |        -11.1667   | NEUTRAL  | Yahoo Finance |
| KO         | 2026-10-09 00:00:00 |    88.05      |         43.6667   | NEUTRAL  | Yahoo Finance |
| LDO-USD    | 2026-10-12 00:00:00 |     0.452     |         25.75     | NEUTRAL  | Kraken API    |
| LINK-USD   | 2026-10-12 00:00:00 |    13.3844    |         22.3333   | NEUTRAL  | Kraken API    |
| MPC        | 2026-10-09 00:00:00 |   455.03      |         62        | NEUTRAL  | Yahoo Finance |
| MRK        | 2026-10-09 00:00:00 |   145.6       |         10        | NEUTRAL  | Yahoo Finance |
| MU         | 2026-10-09 00:00:00 |  1029         |         14.1667   | NEUTRAL  | Yahoo Finance |
| NEM        | 2026-10-09 00:00:00 |   117.84      |        -13.0833   | NEUTRAL  | Yahoo Finance |
| NFLX       | 2026-10-09 00:00:00 |    70.3       |        -26.4167   | NEUTRAL  | Yahoo Finance |
| NOW        | 2026-10-09 00:00:00 |   140.86      |         46.3333   | NEUTRAL  | Yahoo Finance |
| ORCL       | 2026-10-09 00:00:00 |   141.4       |        -42.3333   | NEUTRAL  | Yahoo Finance |
| PEPE-USD   | 2026-10-12 00:00:00 |     4.268e-06 |         28.25     | NEUTRAL  | Kraken API    |
| PFE        | 2026-10-09 00:00:00 |    28.28      |         41.3333   | NEUTRAL  | Yahoo Finance |
| PG         | 2026-10-09 00:00:00 |   151.23      |         73.4167   | NEUTRAL  | Yahoo Finance |
| PM         | 2026-10-09 00:00:00 |   201.19      |         64        | NEUTRAL  | Yahoo Finance |
| POL-USD    | 2026-10-12 00:00:00 |     0.10387   |        -13.8333   | NEUTRAL  | Kraken API    |
| QCOM       | 2026-10-09 00:00:00 |   175.5       |         -7.08333  | NEUTRAL  | Yahoo Finance |
| RTX        | 2026-10-09 00:00:00 |   185.97      |        -29.25     | NEUTRAL  | Yahoo Finance |
| SHIB-USD   | 2026-10-12 00:00:00 |     5.504e-06 |        -24.3333   | NEUTRAL  | Kraken API    |
| SHY        | 2026-10-09 00:00:00 |    81.2       |        -23.75     | NEUTRAL  | Yahoo Finance |
| SKY-USD    | 2026-10-12 00:00:00 |     0.08046   |         26.5833   | NEUTRAL  | Kraken API    |
| SLV        | 2026-10-09 00:00:00 |    54.78      |        -64.8333   | NEUTRAL  | Yahoo Finance |
| SNX-USD    | 2026-10-12 00:00:00 |     0.26      |         18        | NEUTRAL  | Kraken API    |
| SOL-USD    | 2026-10-12 00:00:00 |   112.46      |          9.33333  | NEUTRAL  | Kraken API    |
| SPY        | 2026-10-09 00:00:00 |   778.57      |         65.6667   | NEUTRAL  | Yahoo Finance |
| SUSHI-USD  | 2026-10-12 00:00:00 |     0.2425    |         11.0833   | NEUTRAL  | Kraken API    |
| TGT        | 2026-10-09 00:00:00 |   153.64      |        -26.8333   | NEUTRAL  | Yahoo Finance |
| TRX-USD    | 2026-10-12 00:00:00 |     0.332128  |        -40.0833   | NEUTRAL  | Kraken API    |
| TSLA       | 2026-10-09 00:00:00 |   382.7       |         56.4167   | NEUTRAL  | Yahoo Finance |
| UNI-USD    | 2026-10-12 00:00:00 |     7.7369    |         14.3333   | NEUTRAL  | Kraken API    |
| USO        | 2026-10-09 00:00:00 |   148.2       |         39.25     | NEUTRAL  | Yahoo Finance |
| VEA        | 2026-10-09 00:00:00 |    70.35      |        -28.75     | NEUTRAL  | Yahoo Finance |
| VIXY       | 2026-10-09 00:00:00 |    16.3       |        -40.5      | NEUTRAL  | Yahoo Finance |
| VTI        | 2026-10-09 00:00:00 |   381.94      |         54.8333   | NEUTRAL  | Yahoo Finance |
| VWO        | 2026-10-09 00:00:00 |    59.76      |        -31        | NEUTRAL  | Yahoo Finance |
| WFC        | 2026-10-09 00:00:00 |    83.55      |        -14.3333   | NEUTRAL  | Yahoo Finance |
| WIF-USD    | 2026-10-12 00:00:00 |     0.2233    |          7.08333  | NEUTRAL  | Kraken API    |
| WMT        | 2026-10-09 00:00:00 |   111.35      |         23.5      | NEUTRAL  | Yahoo Finance |
| XBI        | 2026-10-09 00:00:00 |   153.77      |        -21        | NEUTRAL  | Yahoo Finance |
| XLB        | 2026-10-09 00:00:00 |    49.43      |        -29.25     | NEUTRAL  | Yahoo Finance |
| XLC        | 2026-10-09 00:00:00 |   110.38      |        -67.5      | NEUTRAL  | Yahoo Finance |
| XLF        | 2026-10-09 00:00:00 |    54.73      |         16.25     | NEUTRAL  | Yahoo Finance |
| XLI        | 2026-10-09 00:00:00 |   169.25      |        -35.9167   | NEUTRAL  | Yahoo Finance |
| XLM-USD    | 2026-10-12 00:00:00 |     0.202373  |         18.4167   | NEUTRAL  | Kraken API    |
| XLU        | 2026-10-09 00:00:00 |    41.41      |         -2.83333  | NEUTRAL  | Yahoo Finance |
| XLV        | 2026-10-09 00:00:00 |   170.81      |         59        | NEUTRAL  | Yahoo Finance |
| XLY        | 2026-10-09 00:00:00 |   112.85      |         12.6667   | NEUTRAL  | Yahoo Finance |
| XOM        | 2026-10-09 00:00:00 |   168.94      |         43.5      | NEUTRAL  | Yahoo Finance |
| XRP-USD    | 2026-10-12 00:00:00 |     1.41089   |          6.41667  | NEUTRAL  | Kraken API    |
| YFI-USD    | 2026-10-12 00:00:00 |  2415.1       |         -4        | NEUTRAL  | Kraken API    |
| ZEC-USD    | 2026-10-12 00:00:00 |  1335         |         23.8333   | NEUTRAL  | Kraken API    |
| AGG        | 2026-10-09 00:00:00 |    94.59      |        -41.75     | SHORT    | Yahoo Finance |
| BA         | 2026-10-09 00:00:00 |   190.37      |        -38.5833   | SHORT    | Yahoo Finance |
| BND        | 2026-10-09 00:00:00 |    70.22      |        -41.75     | SHORT    | Yahoo Finance |
| CMCSA      | 2026-10-09 00:00:00 |    20.66      |        -55.4167   | SHORT    | Yahoo Finance |
| DOGE-USD   | 2026-10-12 00:00:00 |     0.0873299 |        -38.5833   | SHORT    | Kraken API    |
| GLD        | 2026-10-09 00:00:00 |   384.58      |        -51.5833   | SHORT    | Yahoo Finance |
| GS         | 2026-10-09 00:00:00 |   895.32      |        -52.4167   | SHORT    | Yahoo Finance |
| HD         | 2026-10-09 00:00:00 |   290.74      |        -33.25     | SHORT    | Yahoo Finance |
| HYG        | 2026-10-09 00:00:00 |    77.23      |        -54.5833   | SHORT    | Yahoo Finance |
| IEF        | 2026-10-09 00:00:00 |    89.4       |        -35.5833   | SHORT    | Yahoo Finance |
| ITA        | 2026-10-09 00:00:00 |   206.65      |        -32.0833   | SHORT    | Yahoo Finance |
| MCD        | 2026-10-09 00:00:00 |   235.23      |        -35.75     | SHORT    | Yahoo Finance |
| MS         | 2026-10-09 00:00:00 |   190.02      |        -53.1667   | SHORT    | Yahoo Finance |
| NKE        | 2026-10-09 00:00:00 |    34.71      |        -32.9167   | SHORT    | Yahoo Finance |
| PEP        | 2026-10-09 00:00:00 |   125.97      |        -33.25     | SHORT    | Yahoo Finance |
| SBUX       | 2026-10-09 00:00:00 |    90.75      |        -34.9167   | SHORT    | Yahoo Finance |
| SCHW       | 2026-10-09 00:00:00 |    96.7       |        -40.1667   | SHORT    | Yahoo Finance |
| SLB        | 2026-10-09 00:00:00 |    48.95      |        -50.75     | SHORT    | Yahoo Finance |
| T          | 2026-10-09 00:00:00 |    22.18      |        -63.3333   | SHORT    | Yahoo Finance |
| TLT        | 2026-10-09 00:00:00 |    77.98      |        -57.0833   | SHORT    | Yahoo Finance |
| TMUS       | 2026-10-09 00:00:00 |   148.58      |        -53.8333   | SHORT    | Yahoo Finance |
| UPS        | 2026-10-09 00:00:00 |    94.57      |        -33.75     | SHORT    | Yahoo Finance |
| VNQ        | 2026-10-09 00:00:00 |    90.65      |        -36.5833   | SHORT    | Yahoo Finance |
| VZ         | 2026-10-09 00:00:00 |    41.65      |        -61.6667   | SHORT    | Yahoo Finance |

## Edge Summary

- Symbols with trades: **161** of 161
- Beat buy-and-hold: **33.54%** of traded symbols
- Positive return: **30.43%** of traded symbols
- Median strategy return: **-10.06%** (benchmark **14.49%**)
- Median excess vs benchmark: **-24.36%**
- Median Sharpe: **-0.12**
- Median exposure: **44.26%**

> Edge is real only if both _beat buy-and-hold_ and _median excess_ are convincingly positive across many symbols. Treat a single high-return symbol as noise.

## Portfolio Backtest

Actual capital-allocation books (not per-symbol averages). Benchmarks: `equal_weight_buyhold` (whole tracked universe), `spy_buyhold` (100% SPY), and `sixty_forty` (60% SPY / 40% AGG). `high_conf_voltarget` inverse-vol-weights the HIGH-confidence book; `conviction_long_short` is market-neutral. Judge on **Sharpe** and **max_drawdown** out-of-sample, not raw return: a fully-invested long book wins on return in a bull market but carries all the risk.

| strategy              | scope         | ann_return   | ann_vol   |   sharpe | max_drawdown   | total_return   |   avg_gross_exposure |
|:----------------------|:--------------|:-------------|:----------|---------:|:---------------|:---------------|---------------------:|
| equal_weight_buyhold  | full          | 12.13%       | 28.33%    |     0.43 | -39.53%        | 28.04%         |                 1    |
| equal_weight_buyhold  | out_of_sample | 11.95%       | 27.86%    |     0.43 | -24.72%        | 9.02%          |                 1    |
| all_signals_ew        | full          | -14.55%      | 24.15%    |    -0.6  | -58.51%        | -41.28%        |                 1    |
| all_signals_ew        | out_of_sample | 16.48%       | 23.32%    |     0.71 | -23.20%        | 15.85%         |                 1    |
| high_conf_ew          | full          | -0.06%       | 31.34%    |    -0    | -42.74%        | -13.85%        |                 0.9  |
| high_conf_ew          | out_of_sample | 24.42%       | 27.78%    |     0.88 | -22.85%        | 24.48%         |                 0.9  |
| high_conf_voltarget   | full          | -1.55%       | 28.02%    |    -0.06 | -37.96%        | -15.16%        |                 0.9  |
| high_conf_voltarget   | out_of_sample | 12.87%       | 22.71%    |     0.57 | -17.00%        | 11.53%         |                 0.9  |
| conviction_long_short | full          | -12.62%      | 22.22%    |    -0.57 | -44.87%        | -36.90%        |                 0.97 |
| conviction_long_short | out_of_sample | 2.73%        | 19.60%    |     0.14 | -26.77%        | 0.87%          |                 0.97 |
| spy_buyhold           | full          | 4.68%        | 13.50%    |     0.35 | -19.00%        | 12.17%         |                 0.78 |
| spy_buyhold           | out_of_sample | 2.49%        | 9.92%     |     0.25 | -12.06%        | 2.16%          |                 0.78 |
| sixty_forty           | full          | 2.39%        | 8.53%     |     0.28 | -11.66%        | 6.36%          |                 0.78 |
| sixty_forty           | out_of_sample | -0.69%       | 6.68%     |    -0.1  | -8.26%         | -0.97%         |                 0.78 |

## Walk-Forward Robustness

Each book measured across contiguous time folds (each a different regime). A book has durable edge only if `mean_sharpe` is positive, `min_sharpe` isn't deeply negative, and `pct_positive_folds` is high — a single great fold doesn't count. `fold_sharpes` lists each fold oldest-to-newest.

| strategy              |   n_folds |   mean_sharpe |   median_sharpe |   min_sharpe | pct_positive_folds   | mean_return   | fold_sharpes                 |
|:----------------------|----------:|--------------:|----------------:|-------------:|:---------------------|:--------------|:-----------------------------|
| equal_weight_buyhold  |         5 |          0.59 |            0.86 |        -0.39 | 80.00%               | 5.75%         | 0.91;0.86;0.00;-0.39;1.57    |
| all_signals_ew        |         5 |         -0.64 |           -1.33 |        -1.87 | 20.00%               | -8.03%        | -1.33;-1.44;-1.87;1.56;-0.12 |
| high_conf_ew          |         5 |          0.12 |            0.01 |        -0.78 | 60.00%               | -1.70%        | 0.01;-0.48;-0.78;1.18;0.66   |
| high_conf_voltarget   |         5 |          0.11 |            0.14 |        -0.74 | 60.00%               | -2.50%        | 0.14;-0.33;-0.74;0.68;0.82   |
| conviction_long_short |         5 |         -0.53 |           -0.57 |        -1.75 | 20.00%               | -8.43%        | -1.75;-0.21;-0.71;-0.57;0.58 |
| spy_buyhold           |         5 |          0.38 |            0.08 |        -0.11 | 60.00%               | 2.48%         | 1.66;-0.08;0.08;0.39;-0.11   |
| sixty_forty           |         5 |          0.28 |            0.06 |        -0.49 | 80.00%               | 1.30%         | 1.56;0.01;0.26;0.06;-0.49    |

## Strategy Comparison

Each decision rule backtested over the same data. `out_of_sample` is the most recent ~35% of each symbol's history (unseen tail). A rule has real edge only if `median_excess` and `beat_benchmark_pct` stay positive out-of-sample, not just full-sample.

| strategy        | scope         |   symbols | beat_benchmark_pct   | positive_pct   | median_return   | median_benchmark   | median_excess   |   median_sharpe |   total_trades |
|:----------------|:--------------|----------:|:---------------------|:---------------|:----------------|:-------------------|:----------------|----------------:|---------------:|
| trend           | full          |       161 | 33.54%               | 30.43%         | -10.06%         | 14.49%             | -24.36%         |           -0.12 |          11259 |
| trend           | out_of_sample |       161 | 26.71%               | 51.55%         | 0.38%           | 10.82%             | -15.59%         |            0.14 |           3797 |
| mean_reversion  | full          |       156 | 39.10%               | 50.00%         | -0.00%          | 13.60%             | -12.88%         |            0.02 |           1228 |
| mean_reversion  | out_of_sample |       120 | 24.17%               | 52.50%         | 0.29%           | 9.63%              | -10.55%         |            0.16 |            490 |
| regime_adaptive | full          |       161 | 33.54%               | 30.43%         | -9.92%          | 14.49%             | -25.09%         |           -0.11 |          11530 |
| regime_adaptive | out_of_sample |       161 | 27.95%               | 49.69%         | -0.06%          | 10.82%             | -16.48%         |            0.08 |           3908 |

## Signal Calibration

Realized forward return in the signal's direction, grouped by confidence. HIGH should outrank LOW for the confidence score to be meaningful.

| confidence_level   |   horizon |     n | mean_return   | median_return   | win_rate   |
|:-------------------|----------:|------:|:--------------|:----------------|:-----------|
| HIGH               |         5 |  7946 | 0.20%         | 0.04%           | 50.55%     |
| MEDIUM             |         5 | 29201 | 0.03%         | 0.03%           | 50.23%     |
| LOW                |         5 |  3491 | -0.42%        | -0.43%          | 45.77%     |
| ALL                |         5 | 40638 | 0.03%         | 0.00%           | 49.91%     |
| HIGH               |        10 |  7907 | 0.47%         | 0.08%           | 50.85%     |
| MEDIUM             |        10 | 28893 | 0.19%         | 0.07%           | 50.53%     |
| LOW                |        10 |  3433 | -0.72%        | -0.51%          | 46.58%     |
| ALL                |        10 | 40233 | 0.17%         | 0.03%           | 50.26%     |
| HIGH               |        20 |  7741 | 1.12%         | 0.32%           | 52.64%     |
| MEDIUM             |        20 | 28345 | 0.88%         | 0.54%           | 53.08%     |
| LOW                |        20 |  3385 | -0.48%        | -0.59%          | 47.15%     |
| ALL                |        20 | 39471 | 0.81%         | 0.43%           | 52.48%     |

## Backtest Summary

### Data Quality / Signal Availability

- **ok**: 161 symbols

| symbol     |   trades | return   | benchmark_return   | mdd     |   sharpe | exposure   | skipped_reason   |
|:-----------|---------:|:---------|:-------------------|:--------|---------:|:-----------|:-----------------|
| AAPL       |       64 | 4.24%    | 77.30%             | -23.09% |     0.19 | 51.08%     | ok               |
| AAVE-USD   |       65 | -25.74%  | -20.11%            | -66.17% |    -0.05 | 42.72%     | ok               |
| ABBV       |       72 | -25.55%  | 66.13%             | -30.52% |    -0.57 | 47.92%     | ok               |
| ADA-USD    |       76 | -26.81%  | -67.40%            | -49.38% |    -0.12 | 46.55%     | ok               |
| ADBE       |       71 | -11.61%  | -49.89%            | -31.20% |    -0.03 | 56.91%     | ok               |
| AGG        |       65 | -6.42%   | -2.25%             | -10.74% |    -1    | 33.94%     | ok               |
| ALGO-USD   |       76 | -17.69%  | -43.88%            | -38.19% |    -0.01 | 40.04%     | ok               |
| AMAT       |       71 | -32.48%  | 139.07%            | -53.91% |    -0.27 | 51.41%     | ok               |
| AMD        |       54 | 24.55%   | 269.73%            | -41.09% |     0.43 | 37.10%     | ok               |
| AMGN       |       69 | -16.54%  | 32.77%             | -34.19% |    -0.3  | 50.25%     | ok               |
| AMZN       |       82 | -56.75%  | 42.08%             | -57.20% |    -1.64 | 40.60%     | ok               |
| APT-USD    |       70 | -23.20%  | -83.90%            | -56.73% |    -0    | 39.66%     | ok               |
| ARB-USD    |       77 | -7.60%   | -48.10%            | -48.19% |     0.21 | 43.49%     | ok               |
| ARKK       |       85 | -27.19%  | 97.18%             | -31.44% |    -0.39 | 43.43%     | ok               |
| ATOM-USD   |       92 | -60.19%  | -61.59%            | -60.19% |    -0.87 | 48.08%     | ok               |
| AVAX-USD   |       68 | -25.55%  | -52.62%            | -45.19% |    -0.14 | 39.85%     | ok               |
| AVGO       |       64 | 15.79%   | 159.11%            | -36.09% |     0.35 | 41.93%     | ok               |
| BA         |       71 | 2.41%    | 2.93%              | -26.91% |     0.17 | 51.25%     | ok               |
| BAC        |       72 | -11.05%  | 38.25%             | -25.80% |    -0.25 | 48.59%     | ok               |
| BCH-USD    |       74 | 4.78%    | -31.04%            | -53.87% |     0.27 | 48.85%     | ok               |
| BITO       |       79 | -21.84%  | -59.59%            | -43.10% |    -0.13 | 42.26%     | ok               |
| BLK        |       85 | -15.91%  | 33.26%             | -26.90% |    -0.4  | 47.59%     | ok               |
| BND        |       66 | -6.58%   | -2.21%             | -10.80% |    -1    | 35.44%     | ok               |
| BONK-USD   |       72 | 25.85%   | -83.97%            | -45.22% |     0.48 | 45.79%     | ok               |
| BTC-USD    |       72 | 6.23%    | -18.59%            | -23.38% |     0.24 | 52.68%     | ok               |
| C          |       77 | -35.17%  | 102.34%            | -39.51% |    -0.76 | 46.42%     | ok               |
| CAT        |       70 | 4.57%    | 124.68%            | -22.01% |     0.2  | 48.59%     | ok               |
| CL         |       64 | -5.10%   | -6.23%             | -14.32% |    -0.11 | 38.77%     | ok               |
| CMCSA      |       82 | -34.17%  | -43.86%            | -46.50% |    -0.8  | 42.76%     | ok               |
| COMP-USD   |       97 | -32.92%  | -44.44%            | -55.77% |    -0.14 | 49.81%     | ok               |
| COP        |       70 | -19.33%  | 10.18%             | -43.40% |    -0.29 | 43.76%     | ok               |
| COST       |       58 | -1.66%   | 18.99%             | -30.95% |     0.01 | 41.26%     | ok               |
| CRM        |       65 | -34.52%  | -19.78%            | -45.50% |    -0.51 | 45.92%     | ok               |
| CRV-USD    |       66 | 29.14%   | -51.79%            | -39.89% |     0.49 | 37.55%     | ok               |
| CSCO       |       64 | 20.33%   | 145.78%            | -21.79% |     0.45 | 48.92%     | ok               |
| CVX        |       71 | -13.64%  | 30.31%             | -27.78% |    -0.3  | 41.76%     | ok               |
| DASH-USD   |       55 | 0.17%    | 122.05%            | -64.43% |     0.39 | 30.46%     | ok               |
| DBC        |       66 | -8.16%   | 39.01%             | -24.10% |    -0.21 | 35.27%     | ok               |
| DE         |       70 | -12.17%  | 56.40%             | -23.98% |    -0.18 | 44.26%     | ok               |
| DIA        |       64 | -8.07%   | 29.04%             | -12.94% |    -0.42 | 43.59%     | ok               |
| DIS        |       60 | -7.94%   | 4.65%              | -28.37% |    -0.09 | 42.93%     | ok               |
| DOGE-USD   |       69 | -22.82%  | -57.48%            | -60.95% |    -0.01 | 48.85%     | ok               |
| DOT-USD    |       86 | -51.64%  | -73.68%            | -63.33% |    -0.43 | 48.47%     | ok               |
| DXY-INDEX  |       40 | -0.46%   | -3.92%             | -6.02%  |    -0.06 | 31.39%     | ok               |
| EEM        |       62 | -13.17%  | 52.55%             | -25.11% |    -0.39 | 40.43%     | ok               |
| EFA        |       64 | -11.75%  | 26.65%             | -12.96% |    -0.46 | 41.43%     | ok               |
| EOG        |       78 | -29.89%  | 14.02%             | -47.50% |    -0.64 | 44.43%     | ok               |
| ETC-USD    |       58 | -25.19%  | -55.68%            | -48.09% |    -0.25 | 30.84%     | ok               |
| ETH-USD    |       58 | 162.59%  | 8.94%              | -30.11% |     1.38 | 48.66%     | ok               |
| EWJ        |       62 | -22.99%  | 42.38%             | -29.40% |    -0.8  | 36.44%     | ok               |
| FCX        |       65 | -29.37%  | 35.88%             | -46.84% |    -0.32 | 44.26%     | ok               |
| FET-USD    |       81 | -44.28%  | -71.12%            | -61.24% |    -0.26 | 42.53%     | ok               |
| FIL-USD    |       65 | -40.15%  | -58.77%            | -58.54% |    -0.34 | 37.16%     | ok               |
| FXI        |       50 | -10.79%  | 16.74%             | -24.33% |    -0.2  | 31.61%     | ok               |
| GDX        |       60 | -3.83%   | 142.15%            | -33.31% |     0.07 | 44.43%     | ok               |
| GDXJ       |       70 | -39.42%  | 146.88%            | -41.57% |    -0.54 | 42.93%     | ok               |
| GE         |       76 | -8.43%   | 92.76%             | -27.82% |    -0.04 | 48.09%     | ok               |
| GLD        |       50 | 8.28%    | 71.95%             | -13.87% |     0.28 | 45.59%     | ok               |
| GOOGL      |       55 | 57.04%   | 99.74%             | -17.15% |     1.01 | 47.25%     | ok               |
| GRT-USD    |       77 | 42.52%   | -75.13%            | -39.90% |     0.59 | 45.98%     | ok               |
| GS         |       70 | -5.68%   | 91.42%             | -22.13% |    -0.02 | 48.09%     | ok               |
| HBAR-USD   |       38 | -44.08%  | -8.25%             | -56.39% |    -0.98 | 37.16%     | ok               |
| HD         |       65 | 2.91%    | -15.53%            | -17.15% |     0.16 | 43.26%     | ok               |
| HON        |       89 | -27.91%  | 2.03%              | -33.03% |    -0.7  | 54.91%     | ok               |
| HYG        |       85 | -7.06%   | -0.06%             | -10.25% |    -0.79 | 38.10%     | ok               |
| IBIT       |       38 | 38.46%   | 22.47%             | -18.95% |     0.7  | 34.90%     | ok               |
| IBM        |       69 | -24.30%  | 34.37%             | -48.94% |    -0.28 | 49.75%     | ok               |
| ICP-USD    |       79 | -8.17%   | -36.05%            | -46.42% |     0.18 | 39.46%     | ok               |
| IEF        |       76 | -9.63%   | -3.98%             | -12.66% |    -1.28 | 34.44%     | ok               |
| IEMG       |       60 | -12.78%  | 48.13%             | -28.42% |    -0.39 | 40.60%     | ok               |
| INJ-USD    |       63 | -14.31%  | -31.17%            | -69.36% |     0.12 | 40.23%     | ok               |
| INTC       |       68 | 40.26%   | 228.93%            | -60.60% |     0.53 | 48.09%     | ok               |
| INTU       |       73 | -17.96%  | -54.21%            | -41.31% |    -0.18 | 46.26%     | ok               |
| ITA        |       74 | -3.38%   | 52.51%             | -23.75% |    -0.02 | 48.75%     | ok               |
| IWM        |       54 | 7.04%    | 34.05%             | -12.28% |     0.31 | 34.61%     | ok               |
| JNJ        |       64 | 4.52%    | 69.06%             | -16.86% |     0.22 | 46.76%     | ok               |
| JPM        |       73 | -24.84%  | 62.60%             | -32.74% |    -0.69 | 45.42%     | ok               |
| KO         |       54 | 23.16%   | 39.70%             | -8.64%  |     0.83 | 37.27%     | ok               |
| LDO-USD    |       70 | 44.87%   | -56.12%            | -50.47% |     0.6  | 46.55%     | ok               |
| LIN        |       74 | -12.52%  | 11.84%             | -20.61% |    -0.41 | 38.10%     | ok               |
| LINK-USD   |       66 | 54.55%   | -16.30%            | -33.64% |     0.69 | 45.79%     | ok               |
| LLY        |       78 | -34.12%  | 53.15%             | -53.34% |    -0.56 | 49.08%     | ok               |
| LRCX       |       80 | -25.30%  | 249.58%            | -58.92% |    -0.15 | 42.60%     | ok               |
| LTC-USD    |       68 | 0.73%    | -35.04%            | -33.94% |     0.21 | 53.45%     | ok               |
| MCD        |       77 | 0.15%    | -13.64%            | -21.88% |     0.06 | 40.43%     | ok               |
| META       |       76 | -27.86%  | 52.29%             | -44.52% |    -0.39 | 49.92%     | ok               |
| MPC        |       71 | 15.43%   | 153.26%            | -37.91% |     0.36 | 52.08%     | ok               |
| MRK        |       65 | -23.45%  | 10.98%             | -35.95% |    -0.45 | 42.43%     | ok               |
| MS         |       75 | -10.06%  | 89.60%             | -27.79% |    -0.17 | 48.25%     | ok               |
| MSFT       |       83 | -25.89%  | 27.33%             | -39.15% |    -0.55 | 51.08%     | ok               |
| MU         |       51 | 144.50%  | 721.29%            | -68.76% |     1.01 | 53.08%     | ok               |
| NEAR-USD   |       73 | 193.64%  | 103.02%            | -47.03% |     1.18 | 44.25%     | ok               |
| NEM        |       68 | -28.50%  | 169.41%            | -39.56% |    -0.3  | 50.25%     | ok               |
| NFLX       |       78 | 8.22%    | 13.19%             | -21.09% |     0.26 | 53.41%     | ok               |
| NKE        |       79 | -25.04%  | -62.35%            | -55.35% |    -0.26 | 46.76%     | ok               |
| NOW        |       80 | 11.00%   | -7.94%             | -30.43% |     0.3  | 50.25%     | ok               |
| NVDA       |       77 | -48.32%  | 94.32%             | -52.37% |    -0.68 | 55.08%     | ok               |
| OP-USD     |       68 | -27.83%  | -81.07%            | -58.87% |    -0.12 | 32.95%     | ok               |
| ORCL       |       62 | 87.19%   | 14.49%             | -30.61% |     0.81 | 52.58%     | ok               |
| OXY        |       69 | -0.67%   | -5.20%             | -28.48% |     0.11 | 42.26%     | ok               |
| PEP        |       74 | 0.57%    | -30.86%            | -21.35% |     0.09 | 45.92%     | ok               |
| PEPE-USD   |       83 | -49.26%  | -65.51%            | -61.29% |    -0.31 | 48.85%     | ok               |
| PFE        |       81 | -34.01%  | -1.26%             | -41.77% |    -1.04 | 37.27%     | ok               |
| PG         |       64 | -23.83%  | -9.79%             | -24.16% |    -0.96 | 34.94%     | ok               |
| PM         |       79 | -7.37%   | 101.53%            | -35.15% |    -0.08 | 50.58%     | ok               |
| POL-USD    |       79 | 51.76%   | -58.91%            | -38.69% |     0.68 | 49.62%     | ok               |
| QCOM       |       77 | -27.05%  | -9.47%             | -57.69% |    -0.21 | 43.76%     | ok               |
| QQQ        |       66 | 10.33%   | 66.30%             | -14.20% |     0.34 | 46.09%     | ok               |
| RENDER-USD |       92 | -11.61%  | -59.74%            | -44.65% |     0.16 | 47.13%     | ok               |
| RTX        |       64 | 32.09%   | 78.51%             | -16.99% |     0.73 | 52.41%     | ok               |
| SBUX       |       62 | -8.67%   | 16.57%             | -29.22% |    -0.1  | 38.44%     | ok               |
| SCHW       |       80 | -19.88%  | 22.75%             | -31.92% |    -0.45 | 46.26%     | ok               |
| SHIB-USD   |       79 | -37.77%  | -63.36%            | -46.45% |    -0.37 | 51.92%     | ok               |
| SHY        |       46 | -1.78%   | -0.27%             | -3.30%  |    -0.6  | 36.77%     | ok               |
| SKY-USD    |       85 | -58.58%  | 10.22%             | -62.08% |    -0.89 | 44.83%     | ok               |
| SLB        |       73 | -37.82%  | 0.74%              | -57.55% |    -0.71 | 48.75%     | ok               |
| SLV        |       66 | 4.92%    | 90.27%             | -42.66% |     0.24 | 40.27%     | ok               |
| SMH        |       48 | 54.16%   | 162.03%            | -34.29% |     0.85 | 44.26%     | ok               |
| SNX-USD    |       62 | -9.86%   | -67.82%            | -50.74% |     0.1  | 33.52%     | ok               |
| SOL-USD    |       70 | -21.20%  | -34.91%            | -44.99% |    -0.02 | 60.34%     | ok               |
| SOXX       |       54 | 67.61%   | 145.09%            | -39.81% |     0.93 | 43.26%     | ok               |
| SPY        |       64 | -0.06%   | 47.05%             | -15.53% |     0.06 | 49.92%     | ok               |
| SUSHI-USD  |       98 | -77.97%  | -68.72%            | -77.97% |    -1.29 | 39.66%     | ok               |
| T          |       72 | 50.60%   | 27.47%             | -17.01% |     0.96 | 56.74%     | ok               |
| TGT        |       62 | -11.80%  | -4.05%             | -34.98% |    -0.18 | 37.77%     | ok               |
| TIA-USD    |       93 | -53.16%  | -80.61%            | -78.90% |    -0.34 | 42.53%     | ok               |
| TLT        |       68 | -18.91%  | -14.67%            | -21.85% |    -1.41 | 33.78%     | ok               |
| TMO        |       67 | 21.49%   | 10.54%             | -18.85% |     0.49 | 55.24%     | ok               |
| TMUS       |       74 | 2.31%    | -9.40%             | -28.14% |     0.15 | 47.75%     | ok               |
| TRX-USD    |       66 | 6.00%    | 27.71%             | -22.90% |     0.25 | 51.34%     | ok               |
| TSLA       |       78 | -35.10%  | 115.65%            | -58.36% |    -0.22 | 43.09%     | ok               |
| TXN        |       77 | -23.48%  | 45.49%             | -47.39% |    -0.24 | 50.42%     | ok               |
| UNH        |       75 | 21.70%   | -27.70%            | -26.31% |     0.43 | 48.42%     | ok               |
| UNI-USD    |       88 | -34.82%  | 21.57%             | -69.60% |    -0.09 | 50.00%     | ok               |
| UPS        |       72 | -34.99%  | -36.63%            | -39.06% |    -0.68 | 42.43%     | ok               |
| USO        |       67 | -10.09%  | 92.54%             | -45.43% |    -0.02 | 33.44%     | ok               |
| VEA        |       60 | -4.57%   | 37.67%             | -17.74% |    -0.14 | 42.76%     | ok               |
| VIXY       |       94 | -78.39%  | -64.03%            | -88.17% |    -0.95 | 32.78%     | ok               |
| VNQ        |       73 | -15.09%  | 6.79%              | -24.92% |    -0.6  | 40.10%     | ok               |
| VTI        |       68 | -7.54%   | 45.61%             | -17.64% |    -0.22 | 49.92%     | ok               |
| VWO        |       80 | -18.99%  | 33.13%             | -24.94% |    -0.72 | 41.10%     | ok               |
| VZ         |       82 | -20.10%  | 3.97%              | -25.90% |    -0.59 | 41.26%     | ok               |
| WFC        |       80 | -18.40%  | 36.79%             | -28.90% |    -0.31 | 47.75%     | ok               |
| WIF-USD    |       66 | -30.03%  | -70.09%            | -52.76% |    -0.05 | 37.16%     | ok               |
| WMT        |       69 | 4.37%    | 72.24%             | -25.37% |     0.19 | 49.08%     | ok               |
| XBI        |       64 | -2.96%   | 68.64%             | -18.10% |     0.01 | 39.43%     | ok               |
| XLB        |       64 | -13.99%  | 7.28%              | -25.04% |    -0.5  | 32.11%     | ok               |
| XLC        |       61 | 12.62%   | 33.62%             | -12.33% |     0.47 | 50.25%     | ok               |
| XLE        |       69 | -6.66%   | 37.07%             | -30.31% |    -0.08 | 44.76%     | ok               |
| XLF        |       80 | -10.15%  | 28.81%             | -23.61% |    -0.32 | 46.76%     | ok               |
| XLI        |       82 | -10.04%  | 35.04%             | -17.79% |    -0.35 | 42.76%     | ok               |
| XLK        |       42 | 57.82%   | 87.69%             | -14.75% |     1.11 | 46.42%     | ok               |
| XLM-USD    |       66 | -3.19%   | -31.51%            | -54.58% |     0.18 | 47.51%     | ok               |
| XLP        |       67 | -0.24%   | 6.67%              | -11.16% |     0.02 | 38.10%     | ok               |
| XLU        |       69 | -6.30%   | 14.49%             | -20.40% |    -0.23 | 40.10%     | ok               |
| XLV        |       76 | -22.41%  | 16.75%             | -22.75% |    -1.08 | 37.27%     | ok               |
| XLY        |       75 | -4.15%   | 26.30%             | -18.35% |    -0.06 | 47.59%     | ok               |
| XOM        |       55 | 1.71%    | 41.21%             | -20.29% |     0.12 | 34.28%     | ok               |
| XRP-USD    |       62 | 9.57%    | -39.83%            | -33.91% |     0.31 | 36.59%     | ok               |
| YFI-USD    |       76 | -62.90%  | -59.99%            | -65.66% |    -1.17 | 37.55%     | ok               |
| ZEC-USD    |       57 | 152.71%  | 3096.07%           | -56.50% |     0.93 | 41.95%     | ok               |

## AAPL Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 10.76%   | 77.30%             | -22.53% |     0.31 |       73 | 55.91%     | ok               |
|          15 | 7.91%    | 77.30%             | -24.50% |     0.26 |       82 | 63.23%     | ok               |
|          30 | 4.24%    | 77.30%             | -23.09% |     0.19 |       64 | 51.08%     | ok               |
|          40 | 3.13%    | 77.30%             | -28.08% |     0.17 |       60 | 45.59%     | ok               |
|          35 | 2.74%    | 77.30%             | -24.45% |     0.16 |       64 | 49.75%     | ok               |

## AAVE-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 45.70%   | -20.11%            | -43.61% |     0.62 |       43 | 37.16%     | ok               |
|          45 | 32.12%   | -20.11%            | -49.19% |     0.52 |       48 | 31.99%     | ok               |
|          35 | 27.09%   | -20.11%            | -48.79% |     0.47 |       51 | 40.23%     | ok               |
|          50 | 17.03%   | -20.11%            | -45.07% |     0.38 |       46 | 24.33%     | ok               |
|          15 | -29.29%  | -20.11%            | -61.76% |    -0.03 |       72 | 55.36%     | ok               |

## ABBV Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -15.45%  | 66.13%             | -27.91% |    -0.34 |       56 | 35.11%     | ok               |
|          25 | -24.29%  | 66.13%             | -30.04% |    -0.53 |       71 | 49.92%     | ok               |
|          20 | -24.75%  | 66.13%             | -28.82% |    -0.53 |       69 | 51.58%     | ok               |
|          40 | -23.48%  | 66.13%             | -27.36% |    -0.57 |       72 | 40.27%     | ok               |
|          30 | -25.55%  | 66.13%             | -30.52% |    -0.57 |       72 | 47.92%     | ok               |

## ADA-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 18.75%   | -67.40%            | -34.64% |     0.41 |       46 | 32.18%     | ok               |
|          50 | 11.97%   | -67.40%            | -35.54% |     0.33 |       48 | 27.78%     | ok               |
|          40 | -1.49%   | -67.40%            | -40.73% |     0.19 |       58 | 38.12%     | ok               |
|          15 | -12.23%  | -67.40%            | -47.27% |     0.16 |       71 | 62.45%     | ok               |
|          35 | -5.68%   | -67.40%            | -42.89% |     0.15 |       64 | 41.95%     | ok               |

## ADBE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | 4.63%    | -49.89%            | -29.07% |     0.22 |       54 | 61.40%     | ok               |
|          35 | -1.80%   | -49.89%            | -31.73% |     0.1  |       79 | 48.25%     | ok               |
|          20 | -9.08%   | -49.89%            | -31.52% |     0.03 |       60 | 64.39%     | ok               |
|          30 | -11.61%  | -49.89%            | -31.20% |    -0.03 |       71 | 56.91%     | ok               |
|          15 | -16.12%  | -49.89%            | -34.98% |    -0.08 |       62 | 66.06%     | ok               |

## AGG Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -6.42%   | -2.25%             | -10.74% |    -1    |       65 | 33.94%     | ok               |
|          45 | -5.78%   | -2.25%             | -9.29%  |    -1.03 |       64 | 25.12%     | ok               |
|          35 | -7.15%   | -2.25%             | -11.43% |    -1.15 |       64 | 30.78%     | ok               |
|          20 | -8.12%   | -2.25%             | -11.89% |    -1.16 |       72 | 38.60%     | ok               |
|          25 | -8.03%   | -2.25%             | -12.28% |    -1.2  |       71 | 36.77%     | ok               |

## ALGO-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -17.69%  | -43.88%            | -38.19% |    -0.01 |       76 | 40.04%     | ok               |
|          15 | -26.10%  | -43.88%            | -51.37% |    -0.07 |       77 | 50.38%     | ok               |
|          25 | -28.22%  | -43.88%            | -51.92% |    -0.13 |       78 | 44.83%     | ok               |
|          20 | -35.75%  | -43.88%            | -53.23% |    -0.23 |       81 | 47.70%     | ok               |
|          35 | -32.08%  | -43.88%            | -50.16% |    -0.29 |       64 | 34.87%     | ok               |

## AMAT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -24.49%  | 139.07%            | -41.04% |    -0.2  |       50 | 36.11%     | ok               |
|          15 | -30.49%  | 139.07%            | -53.90% |    -0.2  |       72 | 60.40%     | ok               |
|          35 | -27.47%  | 139.07%            | -47.88% |    -0.21 |       71 | 48.75%     | ok               |
|          30 | -32.48%  | 139.07%            | -53.91% |    -0.27 |       71 | 51.41%     | ok               |
|          40 | -33.38%  | 139.07%            | -50.74% |    -0.32 |       69 | 43.93%     | ok               |

## AMD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 27.70%   | 269.73%            | -40.05% |     0.46 |       58 | 32.11%     | ok               |
|          40 | 24.55%   | 269.73%            | -41.09% |     0.43 |       54 | 37.10%     | ok               |
|          35 | 21.98%   | 269.73%            | -43.15% |     0.41 |       62 | 38.60%     | ok               |
|          30 | 5.90%    | 269.73%            | -49.79% |     0.28 |       63 | 41.10%     | ok               |
|          25 | 1.28%    | 269.73%            | -54.33% |     0.24 |       59 | 43.26%     | ok               |

## AMGN Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -11.76%  | 32.77%             | -26.65% |    -0.16 |       64 | 56.07%     | ok               |
|          35 | -14.37%  | 32.77%             | -31.29% |    -0.25 |       69 | 46.76%     | ok               |
|          30 | -16.54%  | 32.77%             | -34.19% |    -0.3  |       69 | 50.25%     | ok               |
|          15 | -18.93%  | 32.77%             | -27.98% |    -0.32 |       63 | 60.40%     | ok               |
|          25 | -18.38%  | 32.77%             | -33.47% |    -0.34 |       63 | 52.58%     | ok               |

## AMZN Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -25.60%  | 42.08%             | -27.34% |    -0.77 |       52 | 29.62%     | ok               |
|          50 | -30.16%  | 42.08%             | -32.37% |    -1.09 |       48 | 22.63%     | ok               |
|          45 | -35.40%  | 42.08%             | -36.22% |    -1.25 |       54 | 26.12%     | ok               |
|          35 | -51.39%  | 42.08%             | -51.90% |    -1.5  |       75 | 34.78%     | ok               |
|          30 | -56.75%  | 42.08%             | -57.20% |    -1.64 |       82 | 40.60%     | ok               |

## APT-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 25.37%   | -83.90%            | -31.21% |     0.52 |       42 | 16.28%     | ok               |
|          20 | 16.34%   | -83.90%            | -56.22% |     0.41 |       76 | 49.43%     | ok               |
|          45 | -1.29%   | -83.90%            | -53.47% |     0.18 |       58 | 23.18%     | ok               |
|          25 | -12.27%  | -83.90%            | -55.69% |     0.14 |       70 | 44.25%     | ok               |
|          15 | -18.47%  | -83.90%            | -58.22% |     0.12 |       75 | 55.17%     | ok               |

## ARB-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 75.31%   | -48.10%            | -44.26% |     0.72 |       86 | 59.58%     | ok               |
|          45 | 57.32%   | -48.10%            | -33.60% |     0.67 |       54 | 26.44%     | ok               |
|          50 | 46.51%   | -48.10%            | -30.72% |     0.61 |       42 | 19.35%     | ok               |
|          20 | 30.62%   | -48.10%            | -54.05% |     0.51 |       72 | 54.02%     | ok               |
|          40 | 27.44%   | -48.10%            | -40.13% |     0.48 |       55 | 33.72%     | ok               |

## ARKK Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -13.51%  | 97.18%             | -37.76% |    -0.06 |       89 | 54.74%     | ok               |
|          20 | -21.49%  | 97.18%             | -34.82% |    -0.22 |       87 | 49.92%     | ok               |
|          30 | -27.19%  | 97.18%             | -31.44% |    -0.39 |       85 | 43.43%     | ok               |
|          35 | -32.93%  | 97.18%             | -36.46% |    -0.55 |       86 | 40.77%     | ok               |
|          40 | -34.01%  | 97.18%             | -40.75% |    -0.61 |       78 | 36.61%     | ok               |

## ATOM-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -41.59%  | -61.59%            | -48.20% |    -0.33 |       86 | 65.90%     | ok               |
|          25 | -50.75%  | -61.59%            | -51.81% |    -0.57 |       94 | 54.41%     | ok               |
|          20 | -55.70%  | -61.59%            | -57.28% |    -0.66 |       96 | 58.24%     | ok               |
|          30 | -60.19%  | -61.59%            | -60.19% |    -0.87 |       92 | 48.08%     | ok               |
|          35 | -61.25%  | -61.59%            | -63.38% |    -1    |       82 | 41.95%     | ok               |

## AVAX-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 53.25%   | -52.62%            | -22.06% |     0.83 |       32 | 19.73%     | ok               |
|          40 | 30.85%   | -52.62%            | -26.27% |     0.56 |       36 | 27.20%     | ok               |
|          45 | 27.18%   | -52.62%            | -23.19% |     0.52 |       30 | 24.14%     | ok               |
|          35 | 10.45%   | -52.62%            | -33.05% |     0.32 |       54 | 33.52%     | ok               |
|          15 | 0.67%    | -52.62%            | -42.49% |     0.24 |       73 | 53.26%     | ok               |

## AVGO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | 19.12%   | 159.11%            | -38.01% |     0.38 |       68 | 44.59%     | ok               |
|          30 | 15.79%   | 159.11%            | -36.09% |     0.35 |       64 | 41.93%     | ok               |
|          50 | 10.84%   | 159.11%            | -36.86% |     0.29 |       56 | 29.78%     | ok               |
|          35 | 7.38%    | 159.11%            | -40.43% |     0.26 |       74 | 38.94%     | ok               |
|          20 | 5.45%    | 159.11%            | -39.42% |     0.24 |       77 | 47.75%     | ok               |

## BA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 39.55%   | 2.93%              | -13.34% |     0.87 |       46 | 35.44%     | ok               |
|          40 | 32.92%   | 2.93%              | -23.87% |     0.65 |       46 | 43.09%     | ok               |
|          35 | 27.78%   | 2.93%              | -19.93% |     0.55 |       68 | 47.59%     | ok               |
|          25 | 11.91%   | 2.93%              | -27.37% |     0.31 |       72 | 54.74%     | ok               |
|          45 | 5.66%    | 2.93%              | -26.76% |     0.22 |       44 | 39.43%     | ok               |

## BAC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | -0.87%   | 38.25%             | -23.08% |     0.05 |       64 | 45.26%     | ok               |
|          20 | -2.56%   | 38.25%             | -18.20% |     0.02 |       80 | 53.24%     | ok               |
|          25 | -4.95%   | 38.25%             | -22.11% |    -0.06 |       74 | 50.75%     | ok               |
|          45 | -6.80%   | 38.25%             | -19.47% |    -0.15 |       60 | 36.94%     | ok               |
|          15 | -10.39%  | 38.25%             | -23.94% |    -0.17 |       87 | 60.40%     | ok               |

## BCH-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 46.86%   | -31.04%            | -45.51% |     0.62 |       72 | 57.28%     | ok               |
|          20 | 21.80%   | -31.04%            | -45.63% |     0.43 |       64 | 54.02%     | ok               |
|          25 | 4.58%    | -31.04%            | -51.09% |     0.27 |       68 | 50.38%     | ok               |
|          30 | 4.78%    | -31.04%            | -53.87% |     0.27 |       74 | 48.85%     | ok               |
|          35 | -6.94%   | -31.04%            | -57.99% |     0.13 |       70 | 45.40%     | ok               |

## BITO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -5.43%   | -59.59%            | -31.98% |     0.06 |       54 | 25.79%     | ok               |
|          30 | -21.84%  | -59.59%            | -43.10% |    -0.13 |       79 | 42.26%     | ok               |
|          45 | -18.46%  | -59.59%            | -34.92% |    -0.14 |       60 | 29.28%     | ok               |
|          40 | -22.68%  | -59.59%            | -40.13% |    -0.19 |       62 | 33.61%     | ok               |
|          35 | -24.72%  | -59.59%            | -42.34% |    -0.2  |       70 | 37.77%     | ok               |

## BLK Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | -7.40%   | 33.26%             | -20.79% |    -0.15 |       92 | 43.76%     | ok               |
|          40 | -8.64%   | 33.26%             | -22.83% |    -0.2  |       80 | 38.94%     | ok               |
|          20 | -10.53%  | 33.26%             | -21.48% |    -0.2  |       88 | 52.25%     | ok               |
|          25 | -11.82%  | 33.26%             | -24.62% |    -0.25 |       81 | 50.08%     | ok               |
|          30 | -15.91%  | 33.26%             | -26.90% |    -0.4  |       85 | 47.59%     | ok               |

## BND Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -6.86%   | -2.21%             | -10.72% |    -0.97 |       65 | 40.27%     | ok               |
|          25 | -6.85%   | -2.21%             | -11.16% |    -1    |       68 | 38.44%     | ok               |
|          30 | -6.58%   | -2.21%             | -10.80% |    -1    |       66 | 35.44%     | ok               |
|          40 | -7.00%   | -2.21%             | -11.24% |    -1.16 |       62 | 29.95%     | ok               |
|          15 | -8.56%   | -2.21%             | -12.04% |    -1.21 |       76 | 42.76%     | ok               |

## BONK-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 156.03%  | -83.97%            | -35.57% |     1.2  |       42 | 21.46%     | ok               |
|          45 | 69.26%   | -83.97%            | -42.36% |     0.75 |       66 | 27.78%     | ok               |
|          15 | 60.37%   | -83.97%            | -63.45% |     0.67 |       71 | 60.15%     | ok               |
|          20 | 48.62%   | -83.97%            | -55.43% |     0.61 |       66 | 55.94%     | ok               |
|          40 | 38.07%   | -83.97%            | -50.07% |     0.55 |       56 | 37.36%     | ok               |

## BTC-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 44.41%   | -18.59%            | -14.50% |     0.88 |       44 | 35.82%     | ok               |
|          45 | 39.90%   | -18.59%            | -12.20% |     0.84 |       42 | 31.80%     | ok               |
|          35 | 43.41%   | -18.59%            | -21.56% |     0.83 |       62 | 42.15%     | ok               |
|          50 | 18.02%   | -18.59%            | -20.63% |     0.49 |       38 | 26.44%     | ok               |
|          30 | 18.55%   | -18.59%            | -21.75% |     0.44 |       68 | 48.08%     | ok               |

## C Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -12.19%  | 102.34%            | -21.80% |    -0.28 |       66 | 31.61%     | ok               |
|          45 | -22.67%  | 102.34%            | -29.60% |    -0.58 |       74 | 35.77%     | ok               |
|          25 | -32.69%  | 102.34%            | -36.44% |    -0.68 |       69 | 48.42%     | ok               |
|          40 | -28.09%  | 102.34%            | -35.11% |    -0.7  |       74 | 38.10%     | ok               |
|          15 | -36.63%  | 102.34%            | -38.43% |    -0.73 |       74 | 55.41%     | ok               |

## CAT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 15.93%   | 124.68%            | -22.20% |     0.36 |       73 | 61.23%     | ok               |
|          25 | 12.01%   | 124.68%            | -22.20% |     0.31 |       66 | 50.92%     | ok               |
|          45 | 5.32%    | 124.68%            | -24.44% |     0.21 |       54 | 37.27%     | ok               |
|          30 | 4.57%    | 124.68%            | -22.01% |     0.2  |       70 | 48.59%     | ok               |
|          20 | 2.66%    | 124.68%            | -24.75% |     0.17 |       76 | 54.24%     | ok               |

## CL Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -1.45%   | -6.23%             | -12.98% |    -0.01 |       42 | 22.63%     | ok               |
|          30 | -5.10%   | -6.23%             | -14.32% |    -0.11 |       64 | 38.77%     | ok               |
|          45 | -7.16%   | -6.23%             | -13.51% |    -0.24 |       48 | 25.46%     | ok               |
|          35 | -8.88%   | -6.23%             | -15.34% |    -0.26 |       64 | 34.94%     | ok               |
|          15 | -13.61%  | -6.23%             | -18.95% |    -0.36 |       64 | 47.09%     | ok               |

## CMCSA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -17.61%  | -43.86%            | -28.41% |    -0.57 |       46 | 16.47%     | ok               |
|          45 | -22.31%  | -43.86%            | -35.13% |    -0.69 |       62 | 20.97%     | ok               |
|          15 | -34.35%  | -43.86%            | -47.11% |    -0.7  |       89 | 57.40%     | ok               |
|          40 | -30.26%  | -43.86%            | -42.51% |    -0.8  |       89 | 28.45%     | ok               |
|          30 | -34.17%  | -43.86%            | -46.50% |    -0.8  |       82 | 42.76%     | ok               |

## COMP-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 6.35%    | -44.44%            | -38.71% |     0.28 |       50 | 24.90%     | ok               |
|          30 | -32.92%  | -44.44%            | -55.77% |    -0.14 |       97 | 49.81%     | ok               |
|          25 | -39.68%  | -44.44%            | -54.62% |    -0.22 |       96 | 57.85%     | ok               |
|          15 | -43.56%  | -44.44%            | -54.29% |    -0.25 |       98 | 68.20%     | ok               |
|          45 | -39.87%  | -44.44%            | -53.54% |    -0.33 |       66 | 33.14%     | ok               |

## COP Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -11.36%  | 10.18%             | -34.61% |    -0.17 |       50 | 27.45%     | ok               |
|          35 | -17.93%  | 10.18%             | -44.33% |    -0.27 |       73 | 40.77%     | ok               |
|          30 | -19.33%  | 10.18%             | -43.40% |    -0.29 |       70 | 43.76%     | ok               |
|          45 | -19.81%  | 10.18%             | -42.39% |    -0.37 |       64 | 31.61%     | ok               |
|          40 | -26.93%  | 10.18%             | -48.70% |    -0.54 |       76 | 35.27%     | ok               |

## COST Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 10.71%   | 18.99%             | -24.32% |     0.38 |       62 | 47.09%     | ok               |
|          25 | 7.51%    | 18.99%             | -24.93% |     0.29 |       59 | 44.26%     | ok               |
|          35 | 2.68%    | 18.99%             | -29.78% |     0.15 |       56 | 38.77%     | ok               |
|          30 | -1.66%   | 18.99%             | -30.95% |     0.01 |       58 | 41.26%     | ok               |
|          15 | -4.30%   | 18.99%             | -27.30% |    -0.05 |       67 | 50.75%     | ok               |

## CRM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | -22.78%  | -19.78%            | -34.06% |    -0.28 |       62 | 41.26%     | ok               |
|          40 | -25.67%  | -19.78%            | -39.44% |    -0.37 |       68 | 37.10%     | ok               |
|          15 | -33.25%  | -19.78%            | -47.54% |    -0.4  |       88 | 57.24%     | ok               |
|          50 | -22.09%  | -19.78%            | -38.38% |    -0.4  |       58 | 24.63%     | ok               |
|          30 | -34.52%  | -19.78%            | -45.50% |    -0.51 |       65 | 45.92%     | ok               |

## CRV-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 60.68%   | -51.79%            | -37.78% |     0.71 |       66 | 32.95%     | ok               |
|          40 | 46.36%   | -51.79%            | -38.86% |     0.62 |       54 | 28.74%     | ok               |
|          45 | 36.80%   | -51.79%            | -42.29% |     0.56 |       54 | 22.22%     | ok               |
|          50 | 35.87%   | -51.79%            | -30.73% |     0.56 |       46 | 18.20%     | ok               |
|          30 | 29.14%   | -51.79%            | -39.89% |     0.49 |       66 | 37.55%     | ok               |

## CSCO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 39.65%   | 145.78%            | -19.34% |     0.79 |       50 | 37.94%     | ok               |
|          45 | 34.93%   | 145.78%            | -19.34% |     0.7  |       52 | 39.60%     | ok               |
|          25 | 27.01%   | 145.78%            | -23.28% |     0.55 |       61 | 50.25%     | ok               |
|          20 | 21.31%   | 145.78%            | -22.72% |     0.46 |       71 | 52.58%     | ok               |
|          30 | 20.33%   | 145.78%            | -21.79% |     0.45 |       64 | 48.92%     | ok               |

## CVX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -9.60%   | 30.31%             | -23.80% |    -0.17 |       73 | 44.59%     | ok               |
|          40 | -10.08%  | 30.31%             | -27.34% |    -0.22 |       73 | 36.61%     | ok               |
|          45 | -10.48%  | 30.31%             | -28.83% |    -0.24 |       65 | 33.28%     | ok               |
|          50 | -10.36%  | 30.31%             | -30.69% |    -0.29 |       58 | 28.79%     | ok               |
|          35 | -13.01%  | 30.31%             | -28.85% |    -0.29 |       67 | 38.60%     | ok               |

## DASH-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 156.61%  | 122.05%            | -33.55% |     1.01 |       38 | 18.01%     | ok               |
|          40 | 125.75%  | 122.05%            | -33.20% |     0.89 |       42 | 24.33%     | ok               |
|          45 | 94.16%   | 122.05%            | -37.63% |     0.78 |       42 | 20.50%     | ok               |
|          30 | 0.17%    | 122.05%            | -64.43% |     0.39 |       55 | 30.46%     | ok               |
|          25 | -3.60%   | 122.05%            | -64.14% |     0.36 |       63 | 32.76%     | ok               |

## DBC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -0.09%   | 39.01%             | -26.05% |     0.07 |       77 | 41.26%     | ok               |
|          20 | -4.49%   | 39.01%             | -25.69% |    -0.08 |       69 | 39.60%     | ok               |
|          25 | -5.28%   | 39.01%             | -24.84% |    -0.11 |       66 | 37.60%     | ok               |
|          50 | -6.09%   | 39.01%             | -19.34% |    -0.18 |       50 | 24.79%     | ok               |
|          35 | -7.76%   | 39.01%             | -23.19% |    -0.2  |       66 | 34.28%     | ok               |

## DE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 2.13%    | 56.40%             | -17.97% |     0.13 |       56 | 29.62%     | ok               |
|          45 | -4.48%   | 56.40%             | -19.53% |    -0.02 |       60 | 34.11%     | ok               |
|          20 | -7.80%   | 56.40%             | -24.11% |    -0.07 |       65 | 48.59%     | ok               |
|          25 | -12.03%  | 56.40%             | -24.29% |    -0.17 |       71 | 46.92%     | ok               |
|          30 | -12.17%  | 56.40%             | -23.98% |    -0.18 |       70 | 44.26%     | ok               |

## DIA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -5.95%   | 29.04%             | -11.28% |    -0.29 |       58 | 44.76%     | ok               |
|          35 | -6.67%   | 29.04%             | -13.15% |    -0.35 |       66 | 40.60%     | ok               |
|          30 | -8.07%   | 29.04%             | -12.94% |    -0.42 |       64 | 43.59%     | ok               |
|          20 | -8.66%   | 29.04%             | -13.72% |    -0.43 |       64 | 46.76%     | ok               |
|          40 | -9.76%   | 29.04%             | -15.06% |    -0.56 |       70 | 37.60%     | ok               |

## DIS Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 33.83%   | 4.65%              | -10.17% |     1.05 |       44 | 25.46%     | ok               |
|          40 | 6.14%    | 4.65%              | -18.75% |     0.23 |       57 | 33.61%     | ok               |
|          45 | 3.62%    | 4.65%              | -16.54% |     0.17 |       45 | 29.12%     | ok               |
|          15 | -5.96%   | 4.65%              | -32.73% |    -0.02 |       83 | 54.58%     | ok               |
|          35 | -5.81%   | 4.65%              | -25.87% |    -0.05 |       71 | 39.60%     | ok               |

## DOGE-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 10.84%   | -57.48%            | -57.89% |     0.36 |       73 | 64.18%     | ok               |
|          20 | 2.30%    | -57.48%            | -55.83% |     0.28 |       75 | 58.81%     | ok               |
|          25 | -5.03%   | -57.48%            | -53.72% |     0.21 |       67 | 54.98%     | ok               |
|          30 | -22.82%  | -57.48%            | -60.95% |    -0.01 |       69 | 48.85%     | ok               |
|          50 | -36.29%  | -57.48%            | -55.41% |    -0.36 |       62 | 24.71%     | ok               |

## DOT-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -53.07%  | -73.68%            | -72.06% |    -0.33 |       74 | 63.41%     | ok               |
|          20 | -49.83%  | -73.68%            | -66.32% |    -0.34 |       86 | 59.39%     | ok               |
|          30 | -51.64%  | -73.68%            | -63.33% |    -0.43 |       86 | 48.47%     | ok               |
|          25 | -57.57%  | -73.68%            | -69.99% |    -0.51 |       77 | 54.41%     | ok               |
|          35 | -56.42%  | -73.68%            | -63.01% |    -0.56 |       84 | 42.91%     | ok               |

## DXY-INDEX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd    |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:-------|---------:|---------:|:-----------|:-----------------|
|          50 | -0.46%   | -3.92%             | -6.02% |    -0.06 |       40 | 31.39%     | ok               |
|          40 | -1.37%   | -3.92%             | -7.30% |    -0.16 |       66 | 47.19%     | ok               |
|          45 | -1.83%   | -3.92%             | -8.14% |    -0.24 |       60 | 37.45%     | ok               |
|          30 | -4.32%   | -3.92%             | -9.83% |    -0.51 |       74 | 57.58%     | ok               |
|          35 | -4.48%   | -3.92%             | -9.97% |    -0.56 |       77 | 52.60%     | ok               |

## EEM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -8.68%   | 52.55%             | -15.88% |    -0.26 |       54 | 32.95%     | ok               |
|          35 | -9.97%   | 52.55%             | -23.57% |    -0.27 |       66 | 38.60%     | ok               |
|          45 | -9.01%   | 52.55%             | -17.03% |    -0.28 |       52 | 34.44%     | ok               |
|          40 | -9.34%   | 52.55%             | -19.20% |    -0.28 |       64 | 36.61%     | ok               |
|          30 | -13.17%  | 52.55%             | -25.11% |    -0.39 |       62 | 40.43%     | ok               |

## EFA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -4.52%   | 26.65%             | -10.10% |    -0.1  |       64 | 51.25%     | ok               |
|          20 | -11.44%  | 26.65%             | -13.73% |    -0.41 |       71 | 48.42%     | ok               |
|          30 | -11.75%  | 26.65%             | -12.96% |    -0.46 |       64 | 41.43%     | ok               |
|          25 | -12.49%  | 26.65%             | -15.23% |    -0.48 |       68 | 44.93%     | ok               |
|          50 | -11.53%  | 26.65%             | -17.36% |    -0.54 |       56 | 32.95%     | ok               |

## EOG Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -15.79%  | 14.02%             | -34.41% |    -0.32 |       50 | 30.28%     | ok               |
|          40 | -23.34%  | 14.02%             | -36.53% |    -0.53 |       70 | 34.28%     | ok               |
|          50 | -22.04%  | 14.02%             | -35.63% |    -0.53 |       50 | 27.45%     | ok               |
|          35 | -27.36%  | 14.02%             | -40.63% |    -0.62 |       83 | 39.27%     | ok               |
|          30 | -29.89%  | 14.02%             | -47.50% |    -0.64 |       78 | 44.43%     | ok               |

## ETC-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -5.47%   | -55.68%            | -38.47% |     0.05 |       28 | 20.50%     | ok               |
|          50 | -4.94%   | -55.68%            | -31.28% |     0.05 |       28 | 18.20%     | ok               |
|          40 | -17.03%  | -55.68%            | -43.28% |    -0.15 |       38 | 23.56%     | ok               |
|          35 | -19.28%  | -55.68%            | -45.32% |    -0.16 |       42 | 27.01%     | ok               |
|          30 | -25.19%  | -55.68%            | -48.09% |    -0.25 |       58 | 30.84%     | ok               |

## ETH-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 162.59%  | 8.94%              | -30.11% |     1.38 |       58 | 48.66%     | ok               |
|          30 | 121.52%  | 8.94%              | -32.89% |     1.12 |       60 | 56.32%     | ok               |
|          25 | 81.33%   | 8.94%              | -40.90% |     0.88 |       60 | 60.15%     | ok               |
|          40 | 60.51%   | 8.94%              | -33.11% |     0.81 |       62 | 40.80%     | ok               |
|          20 | 65.20%   | 8.94%              | -39.10% |     0.77 |       78 | 63.98%     | ok               |

## EWJ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -22.99%  | 42.38%             | -29.40% |    -0.8  |       62 | 36.44%     | ok               |
|          20 | -23.95%  | 42.38%             | -30.00% |    -0.81 |       56 | 38.44%     | ok               |
|          25 | -25.82%  | 42.38%             | -29.85% |    -0.9  |       56 | 37.60%     | ok               |
|          15 | -27.60%  | 42.38%             | -31.15% |    -0.9  |       67 | 41.76%     | ok               |
|          45 | -23.95%  | 42.38%             | -27.68% |    -0.98 |       58 | 28.12%     | ok               |

## FCX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 2.51%    | 35.88%             | -29.27% |     0.18 |       50 | 31.61%     | ok               |
|          50 | -0.09%   | 35.88%             | -26.57% |     0.13 |       52 | 27.95%     | ok               |
|          40 | -10.00%  | 35.88%             | -42.89% |    -0.01 |       62 | 36.94%     | ok               |
|          30 | -29.37%  | 35.88%             | -46.84% |    -0.32 |       65 | 44.26%     | ok               |
|          35 | -29.20%  | 35.88%             | -50.12% |    -0.34 |       67 | 42.10%     | ok               |

## FET-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -20.42%  | -71.12%            | -64.89% |     0.11 |       90 | 52.49%     | ok               |
|          15 | -22.46%  | -71.12%            | -59.58% |     0.1  |       82 | 57.09%     | ok               |
|          25 | -27.04%  | -71.12%            | -65.31% |     0.02 |       83 | 47.13%     | ok               |
|          30 | -44.28%  | -71.12%            | -61.24% |    -0.26 |       81 | 42.53%     | ok               |
|          50 | -39.06%  | -71.12%            | -45.19% |    -0.53 |       46 | 14.37%     | ok               |

## FIL-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -40.15%  | -58.77%            | -58.54% |    -0.34 |       65 | 37.16%     | ok               |
|          40 | -39.50%  | -58.77%            | -57.60% |    -0.43 |       50 | 26.44%     | ok               |
|          35 | -44.17%  | -58.77%            | -61.90% |    -0.47 |       60 | 31.03%     | ok               |
|          15 | -58.37%  | -58.77%            | -71.82% |    -0.57 |       91 | 49.04%     | ok               |
|          25 | -58.52%  | -58.77%            | -70.65% |    -0.66 |       76 | 40.04%     | ok               |

## FXI Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -10.54%  | 16.74%             | -22.99% |    -0.19 |       52 | 33.11%     | ok               |
|          15 | -11.36%  | 16.74%             | -21.68% |    -0.19 |       54 | 37.10%     | ok               |
|          30 | -10.79%  | 16.74%             | -24.33% |    -0.2  |       50 | 31.61%     | ok               |
|          20 | -13.95%  | 16.74%             | -24.94% |    -0.28 |       54 | 34.94%     | ok               |
|          35 | -14.24%  | 16.74%             | -27.93% |    -0.31 |       52 | 29.12%     | ok               |

## GDX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 2.74%    | 142.15%            | -28.47% |     0.17 |       60 | 38.44%     | ok               |
|          20 | -0.26%   | 142.15%            | -33.01% |     0.14 |       76 | 49.92%     | ok               |
|          35 | -3.20%   | 142.15%            | -31.73% |     0.08 |       68 | 41.10%     | ok               |
|          30 | -3.83%   | 142.15%            | -33.31% |     0.07 |       60 | 44.43%     | ok               |
|          25 | -12.45%  | 142.15%            | -38.90% |    -0.06 |       66 | 45.92%     | ok               |

## GDXJ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -28.87%  | 146.88%            | -42.33% |    -0.26 |       74 | 49.92%     | ok               |
|          50 | -28.96%  | 146.88%            | -46.83% |    -0.4  |       58 | 34.44%     | ok               |
|          35 | -37.70%  | 146.88%            | -38.56% |    -0.52 |       70 | 40.27%     | ok               |
|          30 | -39.42%  | 146.88%            | -41.57% |    -0.54 |       70 | 42.93%     | ok               |
|          40 | -38.86%  | 146.88%            | -44.70% |    -0.6  |       64 | 37.94%     | ok               |

## GE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 4.89%    | 92.76%             | -21.25% |     0.2  |       60 | 33.78%     | ok               |
|          45 | -2.34%   | 92.76%             | -21.88% |     0.05 |       70 | 36.44%     | ok               |
|          20 | -8.34%   | 92.76%             | -25.05% |    -0.03 |       71 | 52.41%     | ok               |
|          30 | -8.43%   | 92.76%             | -27.82% |    -0.04 |       76 | 48.09%     | ok               |
|          25 | -8.86%   | 92.76%             | -29.91% |    -0.05 |       72 | 49.92%     | ok               |

## GLD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | 13.69%   | 71.95%             | -13.87% |     0.39 |       48 | 46.76%     | ok               |
|          20 | 12.15%   | 71.95%             | -13.87% |     0.36 |       49 | 48.42%     | ok               |
|          30 | 8.28%    | 71.95%             | -13.87% |     0.28 |       50 | 45.59%     | ok               |
|          35 | 5.41%    | 71.95%             | -15.09% |     0.22 |       52 | 43.26%     | ok               |
|          15 | 1.84%    | 71.95%             | -18.05% |     0.13 |       57 | 51.75%     | ok               |

## GOOGL Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 60.93%   | 99.74%             | -17.38% |     1.08 |       57 | 43.76%     | ok               |
|          30 | 57.04%   | 99.74%             | -17.15% |     1.01 |       55 | 47.25%     | ok               |
|          45 | 49.48%   | 99.74%             | -11.66% |     0.99 |       50 | 37.27%     | ok               |
|          25 | 54.65%   | 99.74%             | -16.48% |     0.96 |       55 | 49.75%     | ok               |
|          50 | 43.08%   | 99.74%             | -11.52% |     0.92 |       46 | 32.45%     | ok               |

## GRT-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 78.53%   | -75.13%            | -42.58% |     0.78 |       69 | 62.45%     | ok               |
|          20 | 52.75%   | -75.13%            | -40.19% |     0.64 |       78 | 56.70%     | ok               |
|          25 | 46.31%   | -75.13%            | -37.67% |     0.61 |       78 | 52.49%     | ok               |
|          30 | 42.52%   | -75.13%            | -39.90% |     0.59 |       77 | 45.98%     | ok               |
|          50 | 33.06%   | -75.13%            | -30.80% |     0.55 |       44 | 21.07%     | ok               |

## GS Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 20.01%   | 91.42%             | -20.56% |     0.46 |       68 | 56.41%     | ok               |
|          20 | 1.57%    | 91.42%             | -23.19% |     0.14 |       68 | 53.08%     | ok               |
|          40 | 0.45%    | 91.42%             | -17.88% |     0.1  |       68 | 42.43%     | ok               |
|          25 | -3.57%   | 91.42%             | -23.32% |     0.03 |       68 | 50.58%     | ok               |
|          30 | -5.68%   | 91.42%             | -22.13% |    -0.02 |       70 | 48.09%     | ok               |

## HBAR-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -18.60%  | -8.25%             | -39.26% |    -0.27 |       18 | 18.01%     | ok               |
|          45 | -33.67%  | -8.25%             | -48.27% |    -0.7  |       22 | 24.14%     | ok               |
|          40 | -36.66%  | -8.25%             | -50.61% |    -0.78 |       26 | 28.74%     | ok               |
|          15 | -42.04%  | -8.25%             | -56.87% |    -0.87 |       51 | 51.72%     | ok               |
|          30 | -44.08%  | -8.25%             | -56.39% |    -0.98 |       38 | 37.16%     | ok               |

## HD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 2.91%    | -15.53%            | -17.15% |     0.16 |       65 | 43.26%     | ok               |
|          35 | 2.06%    | -15.53%            | -17.81% |     0.13 |       68 | 39.43%     | ok               |
|          25 | 0.31%    | -15.53%            | -18.17% |     0.09 |       64 | 45.42%     | ok               |
|          40 | 0.33%    | -15.53%            | -17.34% |     0.08 |       72 | 34.94%     | ok               |
|          45 | -0.45%   | -15.53%            | -18.00% |     0.05 |       48 | 30.12%     | ok               |

## HON Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -12.54%  | 2.03%              | -20.54% |    -0.33 |       70 | 33.44%     | ok               |
|          45 | -16.19%  | 2.03%              | -22.88% |    -0.42 |       72 | 38.94%     | ok               |
|          35 | -25.97%  | 2.03%              | -31.30% |    -0.67 |       89 | 50.25%     | ok               |
|          30 | -27.91%  | 2.03%              | -33.03% |    -0.7  |       89 | 54.91%     | ok               |
|          40 | -26.28%  | 2.03%              | -31.84% |    -0.71 |       76 | 43.26%     | ok               |

## HYG Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -5.32%   | -0.06%             | -7.93%  |    -0.61 |       68 | 33.11%     | ok               |
|          45 | -6.49%   | -0.06%             | -9.07%  |    -0.78 |       68 | 29.78%     | ok               |
|          30 | -7.06%   | -0.06%             | -10.25% |    -0.79 |       85 | 38.10%     | ok               |
|          25 | -7.48%   | -0.06%             | -10.88% |    -0.81 |       87 | 40.93%     | ok               |
|          35 | -7.19%   | -0.06%             | -9.76%  |    -0.83 |       79 | 34.94%     | ok               |

## IBIT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 66.07%   | 22.47%             | -19.20% |     0.95 |       44 | 41.63%     | ok               |
|          50 | 52.34%   | 22.47%             | -17.37% |     0.94 |       26 | 25.71%     | ok               |
|          45 | 42.96%   | 22.47%             | -17.37% |     0.8  |       30 | 26.94%     | ok               |
|          40 | 36.57%   | 22.47%             | -17.78% |     0.71 |       30 | 28.78%     | ok               |
|          30 | 38.46%   | 22.47%             | -18.95% |     0.7  |       38 | 34.90%     | ok               |

## IBM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -18.01%  | 34.37%             | -49.43% |    -0.12 |       83 | 61.23%     | ok               |
|          35 | -21.42%  | 34.37%             | -47.10% |    -0.23 |       63 | 45.92%     | ok               |
|          30 | -24.30%  | 34.37%             | -48.94% |    -0.28 |       69 | 49.75%     | ok               |
|          20 | -29.78%  | 34.37%             | -53.45% |    -0.36 |       69 | 54.24%     | ok               |
|          45 | -28.12%  | 34.37%             | -48.72% |    -0.4  |       52 | 37.44%     | ok               |

## ICP-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | -1.53%   | -36.05%            | -46.78% |     0.2  |       72 | 33.72%     | ok               |
|          30 | -8.17%   | -36.05%            | -46.42% |     0.18 |       79 | 39.46%     | ok               |
|          40 | -2.22%   | -36.05%            | -40.71% |     0.18 |       64 | 28.93%     | ok               |
|          15 | -37.61%  | -36.05%            | -58.26% |    -0.05 |       79 | 50.38%     | ok               |
|          50 | -19.79%  | -36.05%            | -53.37% |    -0.09 |       46 | 18.77%     | ok               |

## IEF Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -6.24%   | -3.98%             | -10.18% |    -0.73 |       72 | 42.26%     | ok               |
|          15 | -6.80%   | -3.98%             | -10.91% |    -0.79 |       71 | 43.76%     | ok               |
|          40 | -7.67%   | -3.98%             | -10.59% |    -1.09 |       64 | 27.62%     | ok               |
|          45 | -7.86%   | -3.98%             | -10.70% |    -1.15 |       62 | 25.79%     | ok               |
|          50 | -7.28%   | -3.98%             | -9.11%  |    -1.22 |       58 | 22.46%     | ok               |

## IEMG Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -4.36%   | 48.13%             | -14.22% |    -0.12 |       54 | 31.78%     | ok               |
|          45 | -5.14%   | 48.13%             | -15.23% |    -0.14 |       50 | 34.28%     | ok               |
|          40 | -6.60%   | 48.13%             | -18.73% |    -0.19 |       62 | 37.27%     | ok               |
|          35 | -7.98%   | 48.13%             | -23.81% |    -0.22 |       65 | 39.60%     | ok               |
|          30 | -12.78%  | 48.13%             | -28.42% |    -0.39 |       60 | 40.60%     | ok               |

## INJ-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 21.29%   | -31.17%            | -52.61% |     0.43 |       58 | 36.78%     | ok               |
|          40 | 9.38%    | -31.17%            | -45.92% |     0.32 |       48 | 33.52%     | ok               |
|          45 | -2.86%   | -31.17%            | -45.62% |     0.19 |       54 | 27.78%     | ok               |
|          30 | -14.31%  | -31.17%            | -69.36% |     0.12 |       63 | 40.23%     | ok               |
|          15 | -21.98%  | -31.17%            | -76.78% |     0.09 |       75 | 51.53%     | ok               |

## INTC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 70.01%   | 228.93%            | -49.32% |     0.71 |       56 | 33.78%     | ok               |
|          50 | 64.73%   | 228.93%            | -48.35% |     0.68 |       60 | 29.95%     | ok               |
|          15 | 62.78%   | 228.93%            | -53.65% |     0.64 |       78 | 59.90%     | ok               |
|          40 | 51.36%   | 228.93%            | -55.86% |     0.59 |       64 | 37.94%     | ok               |
|          25 | 46.47%   | 228.93%            | -56.41% |     0.56 |       77 | 50.75%     | ok               |

## INTU Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 10.17%   | -54.21%            | -34.75% |     0.29 |       65 | 28.45%     | ok               |
|          45 | -1.24%   | -54.21%            | -40.30% |     0.1  |       65 | 32.78%     | ok               |
|          40 | -7.55%   | -54.21%            | -43.67% |    -0.01 |       69 | 36.61%     | ok               |
|          25 | -11.92%  | -54.21%            | -37.85% |    -0.06 |       70 | 49.25%     | ok               |
|          35 | -13.17%  | -54.21%            | -45.88% |    -0.11 |       71 | 40.27%     | ok               |

## ITA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -0.93%   | 52.51%             | -21.48% |     0.04 |       76 | 37.27%     | ok               |
|          15 | -2.24%   | 52.51%             | -28.17% |     0.04 |       82 | 61.06%     | ok               |
|          30 | -3.38%   | 52.51%             | -23.75% |    -0.02 |       74 | 48.75%     | ok               |
|          40 | -6.52%   | 52.51%             | -20.58% |    -0.13 |       76 | 42.26%     | ok               |
|          35 | -7.21%   | 52.51%             | -23.16% |    -0.14 |       78 | 45.92%     | ok               |

## IWM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | 10.74%   | 34.05%             | -11.96% |     0.44 |       52 | 35.27%     | ok               |
|          20 | 9.27%    | 34.05%             | -11.74% |     0.38 |       58 | 36.27%     | ok               |
|          30 | 7.04%    | 34.05%             | -12.28% |     0.31 |       54 | 34.61%     | ok               |
|          40 | 6.10%    | 34.05%             | -13.56% |     0.3  |       46 | 29.95%     | ok               |
|          15 | 5.92%    | 34.05%             | -13.42% |     0.26 |       76 | 42.10%     | ok               |

## JNJ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 17.02%   | 69.06%             | -10.57% |     0.7  |       40 | 34.78%     | ok               |
|          15 | 10.90%   | 69.06%             | -17.37% |     0.41 |       60 | 53.58%     | ok               |
|          20 | 5.78%    | 69.06%             | -16.96% |     0.26 |       66 | 50.08%     | ok               |
|          45 | 4.61%    | 69.06%             | -13.35% |     0.23 |       48 | 38.60%     | ok               |
|          30 | 4.52%    | 69.06%             | -16.86% |     0.22 |       64 | 46.76%     | ok               |

## JPM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 1.35%    | 62.60%             | -15.90% |     0.11 |       50 | 33.44%     | ok               |
|          45 | -8.75%   | 62.60%             | -21.91% |    -0.21 |       54 | 36.11%     | ok               |
|          20 | -23.53%  | 62.60%             | -35.58% |    -0.52 |       86 | 49.58%     | ok               |
|          35 | -20.64%  | 62.60%             | -27.43% |    -0.59 |       74 | 41.93%     | ok               |
|          40 | -21.27%  | 62.60%             | -28.47% |    -0.62 |       66 | 38.77%     | ok               |

## KO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 23.16%   | 39.70%             | -8.64%  |     0.83 |       54 | 37.27%     | ok               |
|          35 | 18.98%   | 39.70%             | -8.21%  |     0.71 |       58 | 35.77%     | ok               |
|          40 | 16.11%   | 39.70%             | -9.28%  |     0.65 |       60 | 32.45%     | ok               |
|          25 | 17.00%   | 39.70%             | -10.16% |     0.63 |       60 | 40.10%     | ok               |
|          20 | 4.08%    | 39.70%             | -15.99% |     0.2  |       77 | 44.26%     | ok               |

## LDO-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 82.02%   | -56.12%            | -39.01% |     0.77 |       77 | 59.58%     | ok               |
|          20 | 65.59%   | -56.12%            | -40.80% |     0.7  |       79 | 54.79%     | ok               |
|          30 | 44.87%   | -56.12%            | -50.47% |     0.6  |       70 | 46.55%     | ok               |
|          25 | 29.14%   | -56.12%            | -51.34% |     0.5  |       80 | 51.92%     | ok               |
|          35 | 21.59%   | -56.12%            | -58.19% |     0.43 |       76 | 39.08%     | ok               |

## LIN Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -9.60%   | 11.84%             | -23.00% |    -0.27 |       68 | 44.09%     | ok               |
|          25 | -9.50%   | 11.84%             | -22.01% |    -0.28 |       73 | 40.93%     | ok               |
|          15 | -10.81%  | 11.84%             | -23.68% |    -0.31 |       72 | 47.75%     | ok               |
|          30 | -12.52%  | 11.84%             | -20.61% |    -0.41 |       74 | 38.10%     | ok               |
|          45 | -12.31%  | 11.84%             | -17.04% |    -0.5  |       46 | 21.30%     | ok               |

## LINK-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 54.55%   | -16.30%            | -33.64% |     0.69 |       66 | 45.79%     | ok               |
|          45 | 30.81%   | -16.30%            | -33.71% |     0.52 |       52 | 32.38%     | ok               |
|          35 | 29.32%   | -16.30%            | -34.21% |     0.5  |       60 | 41.76%     | ok               |
|          40 | 20.96%   | -16.30%            | -34.00% |     0.43 |       56 | 36.21%     | ok               |
|          25 | 7.72%    | -16.30%            | -46.32% |     0.32 |       62 | 49.23%     | ok               |

## LLY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -0.77%   | 53.15%             | -38.23% |     0.09 |       50 | 35.44%     | ok               |
|          15 | -13.05%  | 53.15%             | -48.12% |    -0.07 |       70 | 60.40%     | ok               |
|          45 | -13.71%  | 53.15%             | -42.66% |    -0.16 |       58 | 38.94%     | ok               |
|          20 | -26.93%  | 53.15%             | -51.34% |    -0.36 |       77 | 55.41%     | ok               |
|          40 | -24.67%  | 53.15%             | -46.23% |    -0.38 |       68 | 41.93%     | ok               |

## LRCX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -19.53%  | 249.58%            | -53.45% |    -0.08 |       70 | 39.93%     | ok               |
|          35 | -21.08%  | 249.58%            | -56.72% |    -0.09 |       78 | 42.10%     | ok               |
|          50 | -19.17%  | 249.58%            | -48.71% |    -0.1  |       74 | 33.94%     | ok               |
|          30 | -25.30%  | 249.58%            | -58.92% |    -0.15 |       80 | 42.60%     | ok               |
|          15 | -31.30%  | 249.58%            | -57.13% |    -0.18 |       78 | 50.58%     | ok               |

## LTC-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 13.19%   | -35.04%            | -34.94% |     0.35 |       64 | 46.17%     | ok               |
|          45 | 11.37%   | -35.04%            | -37.46% |     0.33 |       58 | 36.59%     | ok               |
|          30 | 0.73%    | -35.04%            | -33.94% |     0.21 |       68 | 53.45%     | ok               |
|          25 | -2.88%   | -35.04%            | -34.22% |     0.17 |       70 | 55.75%     | ok               |
|          40 | -7.49%   | -35.04%            | -40.31% |     0.08 |       56 | 41.76%     | ok               |

## MCD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 10.53%   | -13.64%            | -9.22%  |     0.49 |       46 | 25.12%     | ok               |
|          45 | 1.26%    | -13.64%            | -16.79% |     0.1  |       52 | 28.95%     | ok               |
|          30 | 0.15%    | -13.64%            | -21.88% |     0.06 |       77 | 40.43%     | ok               |
|          40 | -0.09%   | -13.64%            | -18.49% |     0.05 |       67 | 32.28%     | ok               |
|          25 | -0.40%   | -13.64%            | -23.62% |     0.04 |       75 | 42.76%     | ok               |

## META Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -8.72%   | 52.29%             | -37.10% |    -0.04 |       64 | 39.77%     | ok               |
|          40 | -15.32%  | 52.29%             | -40.49% |    -0.16 |       68 | 42.93%     | ok               |
|          50 | -18.52%  | 52.29%             | -38.63% |    -0.25 |       66 | 35.44%     | ok               |
|          35 | -25.94%  | 52.29%             | -41.18% |    -0.37 |       81 | 47.75%     | ok               |
|          25 | -27.88%  | 52.29%             | -45.35% |    -0.38 |       75 | 52.91%     | ok               |

## MPC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 34.68%   | 153.26%            | -18.24% |     0.67 |       50 | 40.10%     | ok               |
|          40 | 32.46%   | 153.26%            | -20.11% |     0.61 |       60 | 46.76%     | ok               |
|          45 | 30.14%   | 153.26%            | -19.46% |     0.59 |       56 | 44.09%     | ok               |
|          35 | 29.47%   | 153.26%            | -31.08% |     0.56 |       68 | 49.42%     | ok               |
|          30 | 15.43%   | 153.26%            | -37.91% |     0.36 |       71 | 52.08%     | ok               |

## MRK Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -13.09%  | 10.98%             | -28.39% |    -0.16 |       83 | 51.91%     | ok               |
|          25 | -13.85%  | 10.98%             | -31.07% |    -0.2  |       70 | 44.09%     | ok               |
|          20 | -18.07%  | 10.98%             | -29.34% |    -0.29 |       75 | 47.42%     | ok               |
|          50 | -14.54%  | 10.98%             | -23.01% |    -0.3  |       56 | 28.45%     | ok               |
|          45 | -16.67%  | 10.98%             | -25.38% |    -0.33 |       57 | 31.78%     | ok               |

## MS Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 1.03%    | 89.60%             | -19.99% |     0.11 |       72 | 39.60%     | ok               |
|          15 | -2.84%   | 89.60%             | -22.02% |     0.04 |       74 | 58.24%     | ok               |
|          20 | -5.14%   | 89.60%             | -25.68% |    -0.03 |       75 | 53.08%     | ok               |
|          30 | -10.06%  | 89.60%             | -27.79% |    -0.17 |       75 | 48.25%     | ok               |
|          35 | -9.99%   | 89.60%             | -26.58% |    -0.17 |       76 | 44.76%     | ok               |

## MSFT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -13.32%  | 27.33%             | -24.64% |    -0.29 |       74 | 37.27%     | ok               |
|          50 | -18.40%  | 27.33%             | -25.48% |    -0.47 |       64 | 31.61%     | ok               |
|          35 | -22.58%  | 27.33%             | -35.38% |    -0.49 |       75 | 46.26%     | ok               |
|          40 | -22.76%  | 27.33%             | -34.92% |    -0.51 |       73 | 41.10%     | ok               |
|          30 | -25.89%  | 27.33%             | -39.15% |    -0.55 |       83 | 51.08%     | ok               |

## MU Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 169.56%  | 721.29%            | -64.26% |     1.11 |       58 | 48.59%     | ok               |
|          15 | 195.41%  | 721.29%            | -61.96% |     1.1  |       51 | 60.07%     | ok               |
|          30 | 144.50%  | 721.29%            | -68.76% |     1.01 |       51 | 53.08%     | ok               |
|          25 | 143.07%  | 721.29%            | -67.90% |     1    |       51 | 54.58%     | ok               |
|          35 | 135.80%  | 721.29%            | -69.35% |     0.99 |       63 | 50.92%     | ok               |

## NEAR-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 249.21%  | 103.02%            | -41.76% |     1.4  |       42 | 31.42%     | ok               |
|          50 | 188.04%  | 103.02%            | -38.95% |     1.3  |       28 | 21.84%     | ok               |
|          45 | 193.07%  | 103.02%            | -35.54% |     1.25 |       44 | 27.39%     | ok               |
|          35 | 181.18%  | 103.02%            | -52.37% |     1.19 |       64 | 36.02%     | ok               |
|          30 | 193.64%  | 103.02%            | -47.03% |     1.18 |       73 | 44.25%     | ok               |

## NEM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -2.33%   | 169.41%            | -31.25% |     0.14 |       61 | 58.74%     | ok               |
|          20 | -3.06%   | 169.41%            | -30.50% |     0.12 |       68 | 54.24%     | ok               |
|          25 | -19.85%  | 169.41%            | -39.51% |    -0.13 |       64 | 52.08%     | ok               |
|          50 | -18.55%  | 169.41%            | -33.24% |    -0.16 |       52 | 38.60%     | ok               |
|          30 | -28.50%  | 169.41%            | -39.56% |    -0.3  |       68 | 50.25%     | ok               |

## NFLX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 35.09%   | 13.19%             | -16.28% |     0.86 |       44 | 33.78%     | ok               |
|          40 | 33.95%   | 13.19%             | -15.02% |     0.78 |       50 | 41.76%     | ok               |
|          35 | 29.39%   | 13.19%             | -18.30% |     0.66 |       74 | 46.42%     | ok               |
|          45 | 21.95%   | 13.19%             | -15.48% |     0.57 |       56 | 38.27%     | ok               |
|          15 | 15.75%   | 13.19%             | -26.59% |     0.38 |       71 | 65.06%     | ok               |

## NKE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -17.89%  | -62.35%            | -49.34% |    -0.12 |       83 | 53.41%     | ok               |
|          35 | -16.21%  | -62.35%            | -42.13% |    -0.15 |       71 | 40.43%     | ok               |
|          25 | -21.29%  | -62.35%            | -51.20% |    -0.18 |       83 | 50.75%     | ok               |
|          15 | -23.19%  | -62.35%            | -54.28% |    -0.21 |       86 | 57.24%     | ok               |
|          30 | -25.04%  | -62.35%            | -55.35% |    -0.26 |       79 | 46.76%     | ok               |

## NOW Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 11.00%   | -7.94%             | -30.43% |     0.3  |       80 | 50.25%     | ok               |
|          20 | 8.52%    | -7.94%             | -39.71% |     0.28 |       75 | 56.57%     | ok               |
|          25 | 5.77%    | -7.94%             | -37.51% |     0.25 |       72 | 53.74%     | ok               |
|          15 | 0.58%    | -7.94%             | -43.06% |     0.19 |       83 | 59.57%     | ok               |
|          40 | 2.42%    | -7.94%             | -36.21% |     0.19 |       72 | 39.60%     | ok               |

## NVDA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -33.16%  | 94.32%             | -41.21% |    -0.48 |       76 | 43.85%     | ok               |
|          20 | -42.05%  | 94.32%             | -42.84% |    -0.57 |       76 | 51.87%     | ok               |
|          25 | -41.95%  | 94.32%             | -42.74% |    -0.63 |       77 | 46.88%     | ok               |
|          15 | -48.32%  | 94.32%             | -52.37% |    -0.68 |       77 | 55.08%     | ok               |
|          35 | -43.22%  | 94.32%             | -49.25% |    -0.76 |       86 | 41.00%     | ok               |

## OP-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 39.39%   | -81.07%            | -21.53% |     0.71 |       30 | 9.00%      | ok               |
|          45 | 34.88%   | -81.07%            | -25.91% |     0.59 |       32 | 13.60%     | ok               |
|          40 | 5.70%    | -81.07%            | -38.97% |     0.25 |       44 | 21.84%     | ok               |
|          35 | -20.91%  | -81.07%            | -48.52% |    -0.08 |       56 | 26.82%     | ok               |
|          30 | -27.83%  | -81.07%            | -58.87% |    -0.12 |       68 | 32.95%     | ok               |

## ORCL Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 166.86%  | 14.49%             | -32.54% |     1.12 |       69 | 62.23%     | ok               |
|          25 | 114.56%  | 14.49%             | -27.76% |     0.93 |       61 | 54.74%     | ok               |
|          45 | 99.47%   | 14.49%             | -32.35% |     0.92 |       58 | 40.27%     | ok               |
|          35 | 104.40%  | 14.49%             | -31.95% |     0.91 |       62 | 48.92%     | ok               |
|          20 | 108.57%  | 14.49%             | -29.32% |     0.9  |       70 | 57.90%     | ok               |

## OXY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -0.67%   | -5.20%             | -28.48% |     0.11 |       69 | 42.26%     | ok               |
|          35 | -2.70%   | -5.20%             | -26.44% |     0.07 |       72 | 38.10%     | ok               |
|          50 | -6.31%   | -5.20%             | -27.98% |    -0.03 |       44 | 26.96%     | ok               |
|          40 | -8.69%   | -5.20%             | -28.30% |    -0.06 |       62 | 33.94%     | ok               |
|          25 | -14.41%  | -5.20%             | -38.51% |    -0.13 |       77 | 45.76%     | ok               |

## PEP Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 14.34%   | -30.86%            | -11.62% |     0.61 |       40 | 25.46%     | ok               |
|          45 | 7.03%    | -30.86%            | -14.22% |     0.33 |       56 | 29.45%     | ok               |
|          35 | 5.22%    | -30.86%            | -21.42% |     0.23 |       77 | 39.93%     | ok               |
|          40 | 2.96%    | -30.86%            | -18.04% |     0.16 |       70 | 35.27%     | ok               |
|          30 | 0.57%    | -30.86%            | -21.35% |     0.09 |       74 | 45.92%     | ok               |

## PEPE-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -49.26%  | -65.51%            | -61.29% |    -0.31 |       83 | 48.85%     | ok               |
|          25 | -51.68%  | -65.51%            | -61.43% |    -0.33 |       93 | 53.83%     | ok               |
|          15 | -61.47%  | -65.51%            | -67.41% |    -0.37 |       82 | 63.03%     | ok               |
|          20 | -57.70%  | -65.51%            | -64.22% |    -0.38 |       88 | 59.58%     | ok               |
|          35 | -50.98%  | -65.51%            | -61.54% |    -0.43 |       72 | 43.87%     | ok               |

## PFE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -18.42%  | -1.26%             | -25.68% |    -0.59 |       54 | 21.80%     | ok               |
|          40 | -19.46%  | -1.26%             | -29.27% |    -0.6  |       74 | 26.96%     | ok               |
|          50 | -18.88%  | -1.26%             | -27.67% |    -0.67 |       42 | 18.64%     | ok               |
|          35 | -27.21%  | -1.26%             | -34.89% |    -0.85 |       84 | 33.44%     | ok               |
|          30 | -34.01%  | -1.26%             | -41.77% |    -1.04 |       81 | 37.27%     | ok               |

## PG Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -10.91%  | -9.79%             | -17.50% |    -0.44 |       54 | 28.12%     | ok               |
|          35 | -16.22%  | -9.79%             | -18.57% |    -0.65 |       62 | 31.78%     | ok               |
|          45 | -20.03%  | -9.79%             | -20.34% |    -0.93 |       54 | 25.46%     | ok               |
|          30 | -23.83%  | -9.79%             | -24.16% |    -0.96 |       64 | 34.94%     | ok               |
|          25 | -25.61%  | -9.79%             | -25.90% |    -1.04 |       74 | 36.27%     | ok               |

## PM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | -4.37%   | 101.53%            | -32.20% |    -0.01 |       84 | 47.09%     | ok               |
|          20 | -6.87%   | 101.53%            | -33.51% |    -0.06 |       83 | 55.74%     | ok               |
|          30 | -7.37%   | 101.53%            | -35.15% |    -0.08 |       79 | 50.58%     | ok               |
|          40 | -11.67%  | 101.53%            | -37.94% |    -0.22 |       78 | 43.09%     | ok               |
|          50 | -11.20%  | 101.53%            | -35.70% |    -0.22 |       68 | 37.27%     | ok               |

## POL-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 51.76%   | -58.91%            | -38.69% |     0.68 |       79 | 49.62%     | ok               |
|          25 | 23.25%   | -58.91%            | -38.69% |     0.45 |       71 | 54.79%     | ok               |
|          20 | 9.73%    | -58.91%            | -41.15% |     0.33 |       79 | 58.62%     | ok               |
|          40 | 6.65%    | -58.91%            | -31.98% |     0.27 |       58 | 31.03%     | ok               |
|          15 | -11.42%  | -58.91%            | -46.76% |     0.12 |       82 | 62.84%     | ok               |

## QCOM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -9.79%   | -9.47%             | -55.66% |     0.06 |       71 | 45.59%     | ok               |
|          20 | -16.42%  | -9.47%             | -55.54% |    -0.03 |       67 | 48.92%     | ok               |
|          35 | -17.40%  | -9.47%             | -51.84% |    -0.07 |       79 | 41.26%     | ok               |
|          15 | -26.52%  | -9.47%             | -59.01% |    -0.17 |       69 | 51.58%     | ok               |
|          30 | -27.05%  | -9.47%             | -57.69% |    -0.21 |       77 | 43.76%     | ok               |

## QQQ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 26.93%   | 66.30%             | -14.17% |     0.65 |       63 | 54.08%     | ok               |
|          25 | 18.32%   | 66.30%             | -12.88% |     0.52 |       61 | 48.09%     | ok               |
|          20 | 17.11%   | 66.30%             | -12.98% |     0.48 |       69 | 50.75%     | ok               |
|          30 | 10.33%   | 66.30%             | -14.20% |     0.34 |       66 | 46.09%     | ok               |
|          35 | -1.01%   | 66.30%             | -20.59% |     0.05 |       72 | 42.26%     | ok               |

## RENDER-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 42.85%   | -59.74%            | -44.59% |     0.59 |       84 | 61.30%     | ok               |
|          20 | 39.81%   | -59.74%            | -43.43% |     0.57 |       87 | 58.05%     | ok               |
|          25 | 33.35%   | -59.74%            | -41.13% |     0.53 |       87 | 53.07%     | ok               |
|          30 | -11.61%  | -59.74%            | -44.65% |     0.16 |       92 | 47.13%     | ok               |
|          35 | -30.44%  | -59.74%            | -46.00% |    -0.11 |       86 | 40.42%     | ok               |

## RTX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 45.66%   | 78.51%             | -18.66% |     0.93 |       74 | 57.24%     | ok               |
|          25 | 40.68%   | 78.51%             | -18.59% |     0.86 |       62 | 54.58%     | ok               |
|          15 | 36.86%   | 78.51%             | -19.55% |     0.78 |       67 | 61.73%     | ok               |
|          30 | 32.09%   | 78.51%             | -16.99% |     0.73 |       64 | 52.41%     | ok               |
|          35 | 24.32%   | 78.51%             | -18.00% |     0.64 |       58 | 49.25%     | ok               |

## SBUX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | 3.04%    | 16.57%             | -23.55% |     0.16 |       57 | 40.43%     | ok               |
|          40 | -6.86%   | 16.57%             | -25.43% |    -0.08 |       62 | 32.95%     | ok               |
|          20 | -9.24%   | 16.57%             | -30.94% |    -0.08 |       60 | 42.43%     | ok               |
|          30 | -8.67%   | 16.57%             | -29.22% |    -0.1  |       62 | 38.44%     | ok               |
|          35 | -8.93%   | 16.57%             | -26.54% |    -0.11 |       60 | 35.94%     | ok               |

## SCHW Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -7.83%   | 22.75%             | -28.76% |    -0.1  |       67 | 48.59%     | ok               |
|          45 | -7.17%   | 22.75%             | -16.53% |    -0.15 |       62 | 31.11%     | ok               |
|          20 | -12.50%  | 22.75%             | -29.24% |    -0.21 |       75 | 51.08%     | ok               |
|          50 | -8.34%   | 22.75%             | -13.28% |    -0.24 |       54 | 28.12%     | ok               |
|          40 | -14.83%  | 22.75%             | -23.35% |    -0.36 |       70 | 35.61%     | ok               |

## SHIB-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -28.07%  | -63.36%            | -44.71% |    -0.16 |       78 | 58.05%     | ok               |
|          15 | -31.54%  | -63.36%            | -45.04% |    -0.19 |       86 | 66.67%     | ok               |
|          35 | -29.09%  | -63.36%            | -44.56% |    -0.24 |       71 | 45.79%     | ok               |
|          20 | -33.91%  | -63.36%            | -47.84% |    -0.24 |       80 | 61.69%     | ok               |
|          40 | -28.38%  | -63.36%            | -41.14% |    -0.26 |       60 | 37.93%     | ok               |

## SHY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd    |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:-------|---------:|---------:|:-----------|:-----------------|
|          30 | -1.78%   | -0.27%             | -3.30% |    -0.6  |       46 | 36.77%     | ok               |
|          35 | -2.39%   | -0.27%             | -3.61% |    -0.82 |       52 | 35.27%     | ok               |
|          40 | -2.41%   | -0.27%             | -3.58% |    -0.83 |       54 | 33.94%     | ok               |
|          45 | -2.43%   | -0.27%             | -3.43% |    -0.89 |       54 | 28.45%     | ok               |
|          25 | -3.05%   | -0.27%             | -4.43% |    -1.01 |       60 | 39.27%     | ok               |

## SKY-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | -55.12%  | 10.22%             | -60.18% |    -0.84 |       78 | 37.16%     | ok               |
|          15 | -62.72%  | 10.22%             | -65.86% |    -0.88 |       75 | 54.21%     | ok               |
|          30 | -58.58%  | 10.22%             | -62.08% |    -0.89 |       85 | 44.83%     | ok               |
|          25 | -62.91%  | 10.22%             | -66.04% |    -0.98 |       78 | 48.08%     | ok               |
|          40 | -60.84%  | 10.22%             | -65.26% |    -1.07 |       66 | 33.72%     | ok               |

## SLB Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 4.96%    | 0.74%              | -28.43% |     0.2  |       50 | 34.78%     | ok               |
|          45 | 4.64%    | 0.74%              | -25.36% |     0.2  |       62 | 31.28%     | ok               |
|          50 | -9.73%   | 0.74%              | -30.44% |    -0.14 |       50 | 26.12%     | ok               |
|          35 | -22.47%  | 0.74%              | -45.96% |    -0.37 |       72 | 42.43%     | ok               |
|          25 | -35.53%  | 0.74%              | -55.80% |    -0.63 |       86 | 53.08%     | ok               |

## SLV Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 37.05%   | 90.27%             | -34.10% |     0.6  |       52 | 30.28%     | ok               |
|          45 | 25.41%   | 90.27%             | -31.82% |     0.47 |       63 | 31.78%     | ok               |
|          40 | 24.42%   | 90.27%             | -34.28% |     0.46 |       67 | 33.78%     | ok               |
|          15 | 14.21%   | 90.27%             | -47.98% |     0.35 |       71 | 48.92%     | ok               |
|          20 | 14.23%   | 90.27%             | -42.66% |     0.35 |       70 | 44.09%     | ok               |

## SMH Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 75.08%   | 162.03%            | -31.66% |     1.03 |       47 | 46.92%     | ok               |
|          25 | 58.47%   | 162.03%            | -33.57% |     0.89 |       44 | 45.59%     | ok               |
|          35 | 56.79%   | 162.03%            | -34.65% |     0.89 |       54 | 42.60%     | ok               |
|          30 | 54.16%   | 162.03%            | -34.29% |     0.85 |       48 | 44.26%     | ok               |
|          45 | 42.93%   | 162.03%            | -33.35% |     0.78 |       54 | 36.77%     | ok               |

## SNX-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 3.99%    | -67.82%            | -41.29% |     0.25 |       54 | 27.20%     | ok               |
|          40 | 1.46%    | -67.82%            | -37.52% |     0.19 |       44 | 22.41%     | ok               |
|          20 | -9.46%   | -67.82%            | -53.03% |     0.14 |       71 | 43.68%     | ok               |
|          30 | -9.86%   | -67.82%            | -50.74% |     0.1  |       62 | 33.52%     | ok               |
|          15 | -34.57%  | -67.82%            | -54.74% |    -0.16 |       77 | 48.28%     | ok               |

## SOL-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 37.45%   | -34.91%            | -39.74% |     0.58 |       60 | 41.19%     | ok               |
|          35 | 14.54%   | -34.91%            | -43.70% |     0.37 |       72 | 47.70%     | ok               |
|          45 | 6.54%    | -34.91%            | -46.83% |     0.27 |       62 | 35.44%     | ok               |
|          25 | -6.55%   | -34.91%            | -41.36% |     0.15 |       72 | 58.24%     | ok               |
|          50 | -3.77%   | -34.91%            | -46.56% |     0.12 |       60 | 29.50%     | ok               |

## SOXX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | 72.40%   | 145.09%            | -39.32% |     0.97 |       53 | 45.42%     | ok               |
|          35 | 68.52%   | 145.09%            | -38.76% |     0.96 |       56 | 40.93%     | ok               |
|          30 | 67.61%   | 145.09%            | -39.81% |     0.93 |       54 | 43.26%     | ok               |
|          20 | 57.17%   | 145.09%            | -39.19% |     0.82 |       59 | 46.42%     | ok               |
|          40 | 44.06%   | 145.09%            | -41.03% |     0.72 |       58 | 38.94%     | ok               |

## SPY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 11.09%   | 47.05%             | -14.25% |     0.42 |       59 | 53.58%     | ok               |
|          15 | 10.56%   | 47.05%             | -16.80% |     0.39 |       63 | 56.24%     | ok               |
|          25 | 6.10%    | 47.05%             | -14.25% |     0.26 |       59 | 52.58%     | ok               |
|          30 | -0.06%   | 47.05%             | -15.53% |     0.06 |       64 | 49.92%     | ok               |
|          35 | -1.03%   | 47.05%             | -15.58% |     0.02 |       62 | 46.76%     | ok               |

## SUSHI-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -13.55%  | -68.72%            | -34.75% |    -0.03 |       56 | 16.86%     | ok               |
|          45 | -46.30%  | -68.72%            | -57.99% |    -0.59 |       58 | 21.65%     | ok               |
|          40 | -52.00%  | -68.72%            | -62.05% |    -0.65 |       63 | 28.35%     | ok               |
|          35 | -62.44%  | -68.72%            | -68.70% |    -0.84 |       84 | 33.33%     | ok               |
|          15 | -73.99%  | -68.72%            | -77.63% |    -0.91 |       87 | 49.81%     | ok               |

## T Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 72.21%   | 27.47%             | -15.08% |     1.17 |       73 | 65.56%     | ok               |
|          20 | 67.96%   | 27.47%             | -18.13% |     1.15 |       68 | 61.06%     | ok               |
|          25 | 66.05%   | 27.47%             | -17.66% |     1.14 |       68 | 58.90%     | ok               |
|          30 | 50.60%   | 27.47%             | -17.01% |     0.96 |       72 | 56.74%     | ok               |
|          35 | 34.18%   | 27.47%             | -14.49% |     0.74 |       78 | 52.41%     | ok               |

## TGT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -11.80%  | -4.05%             | -34.98% |    -0.18 |       62 | 37.77%     | ok               |
|          45 | -11.70%  | -4.05%             | -25.62% |    -0.22 |       50 | 28.62%     | ok               |
|          20 | -16.69%  | -4.05%             | -38.96% |    -0.25 |       88 | 45.42%     | ok               |
|          25 | -15.93%  | -4.05%             | -38.33% |    -0.27 |       72 | 40.93%     | ok               |
|          40 | -16.78%  | -4.05%             | -29.65% |    -0.35 |       52 | 31.28%     | ok               |

## TIA-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -26.36%  | -80.61%            | -66.82% |     0.11 |       96 | 59.20%     | ok               |
|          25 | -42.52%  | -80.61%            | -70.91% |    -0.14 |       94 | 48.28%     | ok               |
|          20 | -46.42%  | -80.61%            | -71.78% |    -0.16 |       91 | 53.64%     | ok               |
|          35 | -34.95%  | -80.61%            | -65.35% |    -0.19 |       76 | 35.06%     | ok               |
|          30 | -53.16%  | -80.61%            | -78.90% |    -0.34 |       93 | 42.53%     | ok               |

## TLT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -8.90%   | -14.67%            | -12.51% |    -0.95 |       38 | 17.30%     | ok               |
|          40 | -13.90%  | -14.67%            | -17.65% |    -1.2  |       54 | 25.46%     | ok               |
|          45 | -12.80%  | -14.67%            | -15.17% |    -1.29 |       48 | 20.97%     | ok               |
|          30 | -18.91%  | -14.67%            | -21.85% |    -1.41 |       68 | 33.78%     | ok               |
|          35 | -18.75%  | -14.67%            | -21.03% |    -1.54 |       64 | 29.28%     | ok               |

## TMO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 54.13%   | 10.54%             | -8.17%  |     1.13 |       48 | 35.44%     | ok               |
|          45 | 42.32%   | 10.54%             | -9.69%  |     0.9  |       52 | 40.10%     | ok               |
|          40 | 36.06%   | 10.54%             | -9.91%  |     0.78 |       57 | 45.09%     | ok               |
|          35 | 30.83%   | 10.54%             | -13.84% |     0.65 |       69 | 50.42%     | ok               |
|          20 | 28.12%   | 10.54%             | -22.89% |     0.57 |       78 | 61.40%     | ok               |

## TMUS Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 2.31%    | -9.40%             | -28.14% |     0.15 |       74 | 47.75%     | ok               |
|          15 | -3.72%   | -9.40%             | -36.74% |     0.03 |       68 | 60.40%     | ok               |
|          25 | -7.43%   | -9.40%             | -34.85% |    -0.06 |       77 | 50.75%     | ok               |
|          50 | -5.70%   | -9.40%             | -30.81% |    -0.08 |       58 | 34.28%     | ok               |
|          20 | -9.27%   | -9.40%             | -35.39% |    -0.1  |       74 | 54.74%     | ok               |

## TRX-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 14.17%   | 27.71%             | -18.79% |     0.49 |       54 | 40.04%     | ok               |
|          35 | 8.62%    | 27.71%             | -21.77% |     0.32 |       66 | 48.47%     | ok               |
|          30 | 6.00%    | 27.71%             | -22.90% |     0.25 |       66 | 51.34%     | ok               |
|          20 | 6.07%    | 27.71%             | -25.45% |     0.25 |       61 | 58.24%     | ok               |
|          45 | 4.14%    | 27.71%             | -22.76% |     0.21 |       46 | 36.40%     | ok               |

## TSLA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 41.47%   | 115.65%            | -30.57% |     0.6  |       64 | 30.12%     | ok               |
|          40 | 13.71%   | 115.65%            | -50.11% |     0.34 |       63 | 35.61%     | ok               |
|          45 | -10.53%  | 115.65%            | -52.01% |     0.07 |       69 | 32.61%     | ok               |
|          35 | -18.00%  | 115.65%            | -58.86% |     0    |       74 | 38.27%     | ok               |
|          30 | -35.10%  | 115.65%            | -58.36% |    -0.22 |       78 | 43.09%     | ok               |

## TXN Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 8.37%    | 45.49%             | -45.45% |     0.26 |       66 | 32.95%     | ok               |
|          35 | -10.62%  | 45.49%             | -43.28% |    -0.04 |       78 | 47.25%     | ok               |
|          40 | -12.18%  | 45.49%             | -45.67% |    -0.07 |       74 | 44.93%     | ok               |
|          20 | -16.19%  | 45.49%             | -38.49% |    -0.08 |       68 | 56.91%     | ok               |
|          45 | -14.18%  | 45.49%             | -46.24% |    -0.11 |       80 | 38.94%     | ok               |

## UNH Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 22.31%   | -27.70%            | -36.92% |     0.45 |       54 | 28.45%     | ok               |
|          30 | 21.70%   | -27.70%            | -26.31% |     0.43 |       75 | 48.42%     | ok               |
|          35 | 18.00%   | -27.70%            | -27.34% |     0.39 |       70 | 43.43%     | ok               |
|          20 | 17.83%   | -27.70%            | -26.96% |     0.38 |       78 | 57.74%     | ok               |
|          15 | 17.80%   | -27.70%            | -26.07% |     0.38 |       83 | 63.89%     | ok               |

## UNI-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 102.12%  | 21.57%             | -21.42% |     1.01 |       48 | 25.86%     | ok               |
|          45 | 85.00%   | 21.57%             | -30.17% |     0.87 |       54 | 33.33%     | ok               |
|          40 | 60.77%   | 21.57%             | -43.84% |     0.72 |       58 | 38.51%     | ok               |
|          35 | 41.01%   | 21.57%             | -50.48% |     0.58 |       68 | 44.06%     | ok               |
|          20 | -37.10%  | 21.57%             | -74.08% |    -0.06 |       92 | 59.58%     | ok               |

## UPS Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | -29.15%  | -36.63%            | -31.52% |    -0.55 |       64 | 36.61%     | ok               |
|          40 | -28.96%  | -36.63%            | -31.55% |    -0.56 |       60 | 31.11%     | ok               |
|          20 | -33.96%  | -36.63%            | -38.09% |    -0.62 |       86 | 49.75%     | ok               |
|          25 | -34.49%  | -36.63%            | -38.59% |    -0.65 |       78 | 46.42%     | ok               |
|          15 | -36.29%  | -36.63%            | -40.28% |    -0.67 |       88 | 53.58%     | ok               |

## USO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 7.46%    | 92.54%             | -32.38% |     0.25 |       48 | 25.96%     | ok               |
|          20 | 3.15%    | 92.54%             | -44.76% |     0.19 |       77 | 38.27%     | ok               |
|          15 | -0.15%   | 92.54%             | -45.68% |     0.15 |       71 | 41.93%     | ok               |
|          50 | -3.42%   | 92.54%             | -29.54% |     0.07 |       52 | 24.13%     | ok               |
|          25 | -5.38%   | 92.54%             | -46.34% |     0.06 |       71 | 35.61%     | ok               |

## VEA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 5.71%    | 37.67%             | -15.99% |     0.26 |       54 | 50.08%     | ok               |
|          20 | -0.43%   | 37.67%             | -17.51% |     0.04 |       59 | 47.42%     | ok               |
|          25 | -4.23%   | 37.67%             | -17.60% |    -0.12 |       57 | 45.42%     | ok               |
|          30 | -4.57%   | 37.67%             | -17.74% |    -0.14 |       60 | 42.76%     | ok               |
|          35 | -5.46%   | 37.67%             | -16.59% |    -0.18 |       52 | 41.10%     | ok               |

## VIXY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -56.72%  | -64.03%            | -69.78% |    -0.67 |       36 | 9.82%      | ok               |
|          15 | -77.75%  | -64.03%            | -89.47% |    -0.82 |       95 | 43.76%     | ok               |
|          45 | -66.00%  | -64.03%            | -75.03% |    -0.88 |       56 | 14.81%     | ok               |
|          30 | -78.39%  | -64.03%            | -88.17% |    -0.95 |       94 | 32.78%     | ok               |
|          40 | -73.32%  | -64.03%            | -80.72% |    -1.01 |       68 | 18.64%     | ok               |

## VNQ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -11.00%  | 6.79%              | -19.07% |    -0.5  |       62 | 28.79%     | ok               |
|          25 | -13.14%  | 6.79%              | -22.34% |    -0.5  |       69 | 42.76%     | ok               |
|          50 | -11.88%  | 6.79%              | -17.13% |    -0.57 |       54 | 25.46%     | ok               |
|          30 | -15.09%  | 6.79%              | -24.92% |    -0.6  |       73 | 40.10%     | ok               |
|          35 | -16.08%  | 6.79%              | -27.01% |    -0.68 |       76 | 37.60%     | ok               |

## VTI Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 11.89%   | 45.61%             | -13.96% |     0.44 |       62 | 54.08%     | ok               |
|          15 | 7.29%    | 45.61%             | -15.70% |     0.29 |       59 | 56.41%     | ok               |
|          25 | -0.04%   | 45.61%             | -15.00% |     0.06 |       58 | 51.91%     | ok               |
|          30 | -7.54%   | 45.61%             | -17.64% |    -0.22 |       68 | 49.92%     | ok               |
|          40 | -8.65%   | 45.61%             | -19.77% |    -0.29 |       72 | 42.43%     | ok               |

## VWO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -11.45%  | 33.13%             | -22.18% |    -0.45 |       56 | 28.79%     | ok               |
|          15 | -14.21%  | 33.13%             | -23.73% |    -0.46 |       74 | 47.25%     | ok               |
|          45 | -12.62%  | 33.13%             | -23.75% |    -0.49 |       58 | 31.45%     | ok               |
|          40 | -13.07%  | 33.13%             | -23.57% |    -0.5  |       68 | 34.28%     | ok               |
|          20 | -15.58%  | 33.13%             | -25.88% |    -0.53 |       71 | 44.93%     | ok               |

## VZ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -0.34%   | 3.97%              | -12.96% |     0.05 |       54 | 28.45%     | ok               |
|          20 | -16.97%  | 3.97%              | -35.02% |    -0.31 |       78 | 50.58%     | ok               |
|          45 | -11.36%  | 3.97%              | -21.44% |    -0.31 |       66 | 32.11%     | ok               |
|          35 | -12.01%  | 3.97%              | -22.73% |    -0.32 |       60 | 37.77%     | ok               |
|          25 | -13.56%  | 3.97%              | -22.13% |    -0.32 |       79 | 45.59%     | ok               |

## WFC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | -8.91%   | 36.79%             | -21.57% |    -0.12 |       77 | 44.59%     | ok               |
|          50 | -6.21%   | 36.79%             | -18.29% |    -0.13 |       58 | 32.61%     | ok               |
|          20 | -19.72%  | 36.79%             | -29.87% |    -0.3  |       77 | 53.08%     | ok               |
|          30 | -18.40%  | 36.79%             | -28.90% |    -0.31 |       80 | 47.75%     | ok               |
|          40 | -14.54%  | 36.79%             | -23.94% |    -0.35 |       72 | 41.26%     | ok               |

## WIF-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 52.26%   | -70.09%            | -40.67% |     0.62 |       67 | 44.44%     | ok               |
|          15 | 18.99%   | -70.09%            | -46.21% |     0.44 |       77 | 47.70%     | ok               |
|          25 | 8.23%    | -70.09%            | -44.74% |     0.35 |       65 | 40.23%     | ok               |
|          50 | -12.09%  | -70.09%            | -35.47% |    -0.04 |       34 | 13.22%     | ok               |
|          30 | -30.03%  | -70.09%            | -52.76% |    -0.05 |       66 | 37.16%     | ok               |

## WMT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 35.91%   | 72.24%             | -12.18% |     1.09 |       36 | 37.27%     | ok               |
|          45 | 34.77%   | 72.24%             | -14.14% |     1.02 |       42 | 39.60%     | ok               |
|          35 | 24.94%   | 72.24%             | -18.25% |     0.73 |       58 | 45.92%     | ok               |
|          40 | 23.33%   | 72.24%             | -18.53% |     0.71 |       50 | 41.26%     | ok               |
|          15 | 6.60%    | 72.24%             | -26.24% |     0.24 |       82 | 59.90%     | ok               |

## XBI Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 11.46%   | 68.64%             | -16.08% |     0.36 |       54 | 34.94%     | ok               |
|          45 | 7.23%    | 68.64%             | -15.46% |     0.26 |       52 | 32.45%     | ok               |
|          35 | -0.90%   | 68.64%             | -17.66% |     0.06 |       62 | 37.94%     | ok               |
|          50 | -2.00%   | 68.64%             | -15.66% |     0.02 |       52 | 29.28%     | ok               |
|          30 | -2.96%   | 68.64%             | -18.10% |     0.01 |       64 | 39.43%     | ok               |

## XLB Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -3.85%   | 7.28%              | -16.40% |    -0.11 |       40 | 22.46%     | ok               |
|          40 | -4.73%   | 7.28%              | -18.27% |    -0.14 |       56 | 26.62%     | ok               |
|          45 | -7.29%   | 7.28%              | -18.10% |    -0.26 |       44 | 24.13%     | ok               |
|          35 | -7.97%   | 7.28%              | -21.38% |    -0.26 |       56 | 30.12%     | ok               |
|          25 | -11.71%  | 7.28%              | -23.37% |    -0.39 |       64 | 35.94%     | ok               |

## XLC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 12.62%   | 33.62%             | -12.33% |     0.47 |       61 | 50.25%     | ok               |
|          25 | 12.06%   | 33.62%             | -12.31% |     0.45 |       60 | 52.41%     | ok               |
|          20 | 11.44%   | 33.62%             | -11.04% |     0.41 |       63 | 54.91%     | ok               |
|          50 | 7.23%    | 33.62%             | -11.12% |     0.38 |       64 | 38.44%     | ok               |
|          40 | 7.80%    | 33.62%             | -13.38% |     0.34 |       62 | 43.93%     | ok               |

## XLE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -2.04%   | 37.07%             | -25.98% |     0.02 |       56 | 36.11%     | ok               |
|          35 | -5.10%   | 37.07%             | -26.89% |    -0.05 |       65 | 42.60%     | ok               |
|          45 | -5.28%   | 37.07%             | -28.46% |    -0.07 |       60 | 38.27%     | ok               |
|          30 | -6.66%   | 37.07%             | -30.31% |    -0.08 |       69 | 44.76%     | ok               |
|          25 | -10.45%  | 37.07%             | -33.14% |    -0.17 |       80 | 47.75%     | ok               |

## XLF Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -2.78%   | 28.81%             | -18.63% |    -0.03 |       72 | 51.91%     | ok               |
|          15 | -4.85%   | 28.81%             | -20.19% |    -0.1  |       76 | 54.58%     | ok               |
|          25 | -9.56%   | 28.81%             | -23.22% |    -0.29 |       79 | 48.75%     | ok               |
|          30 | -10.15%  | 28.81%             | -23.61% |    -0.32 |       80 | 46.76%     | ok               |
|          35 | -17.14%  | 28.81%             | -24.48% |    -0.66 |       70 | 43.09%     | ok               |

## XLI Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 5.22%    | 35.04%             | -11.40% |     0.23 |       86 | 51.41%     | ok               |
|          20 | 1.42%    | 35.04%             | -12.74% |     0.11 |       75 | 46.42%     | ok               |
|          50 | -4.76%   | 35.04%             | -14.94% |    -0.18 |       60 | 31.78%     | ok               |
|          45 | -5.38%   | 35.04%             | -16.29% |    -0.19 |       70 | 34.28%     | ok               |
|          25 | -8.78%   | 35.04%             | -17.03% |    -0.29 |       78 | 44.43%     | ok               |

## XLK Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 77.94%   | 87.69%             | -14.75% |     1.25 |       46 | 51.75%     | ok               |
|          20 | 73.97%   | 87.69%             | -14.75% |     1.25 |       46 | 49.75%     | ok               |
|          25 | 67.87%   | 87.69%             | -14.75% |     1.21 |       42 | 47.75%     | ok               |
|          30 | 57.82%   | 87.69%             | -14.75% |     1.11 |       42 | 46.42%     | ok               |
|          35 | 38.29%   | 87.69%             | -13.61% |     0.84 |       56 | 43.59%     | ok               |

## XLM-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | 6.11%    | -31.51%            | -49.14% |     0.29 |       68 | 49.62%     | ok               |
|          50 | 3.98%    | -31.51%            | -48.81% |     0.24 |       44 | 27.01%     | ok               |
|          45 | 2.83%    | -31.51%            | -51.28% |     0.23 |       54 | 31.99%     | ok               |
|          40 | 0.40%    | -31.51%            | -47.28% |     0.21 |       50 | 36.78%     | ok               |
|          30 | -3.19%   | -31.51%            | -54.58% |     0.18 |       66 | 47.51%     | ok               |

## XLP Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 6.81%    | 6.67%              | -5.66%  |     0.45 |       54 | 29.28%     | ok               |
|          50 | 4.44%    | 6.67%              | -6.08%  |     0.32 |       60 | 27.12%     | ok               |
|          40 | 4.66%    | 6.67%              | -7.77%  |     0.31 |       70 | 33.44%     | ok               |
|          35 | 3.75%    | 6.67%              | -9.73%  |     0.25 |       66 | 36.44%     | ok               |
|          30 | -0.24%   | 6.67%              | -11.16% |     0.02 |       67 | 38.10%     | ok               |

## XLU Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 4.78%    | 14.49%             | -14.03% |     0.27 |       54 | 30.78%     | ok               |
|          45 | 3.63%    | 14.49%             | -14.97% |     0.22 |       58 | 31.95%     | ok               |
|          40 | 0.61%    | 14.49%             | -16.41% |     0.07 |       64 | 33.94%     | ok               |
|          35 | -2.07%   | 14.49%             | -19.71% |    -0.05 |       64 | 36.61%     | ok               |
|          30 | -6.30%   | 14.49%             | -20.40% |    -0.23 |       69 | 40.10%     | ok               |

## XLV Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -22.06%  | 16.75%             | -22.40% |    -1.05 |       76 | 38.94%     | ok               |
|          30 | -22.41%  | 16.75%             | -22.75% |    -1.08 |       76 | 37.27%     | ok               |
|          15 | -25.27%  | 16.75%             | -25.35% |    -1.18 |       83 | 43.09%     | ok               |
|          20 | -25.11%  | 16.75%             | -25.19% |    -1.2  |       79 | 40.60%     | ok               |
|          35 | -26.28%  | 16.75%             | -26.58% |    -1.37 |       70 | 34.28%     | ok               |

## XLY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -0.70%   | 26.30%             | -15.77% |     0.06 |       76 | 54.24%     | ok               |
|          30 | -4.15%   | 26.30%             | -18.35% |    -0.06 |       75 | 47.59%     | ok               |
|          20 | -5.95%   | 26.30%             | -19.25% |    -0.1  |       72 | 50.92%     | ok               |
|          25 | -8.05%   | 26.30%             | -19.98% |    -0.17 |       69 | 49.42%     | ok               |
|          50 | -6.34%   | 26.30%             | -15.82% |    -0.22 |       62 | 32.11%     | ok               |

## XOM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | 2.73%    | 41.21%             | -19.90% |     0.15 |       55 | 34.94%     | ok               |
|          50 | 1.92%    | 41.21%             | -21.35% |     0.13 |       38 | 27.12%     | ok               |
|          30 | 1.71%    | 41.21%             | -20.29% |     0.12 |       55 | 34.28%     | ok               |
|          20 | -3.12%   | 41.21%             | -25.56% |    -0.01 |       62 | 37.27%     | ok               |
|          45 | -3.17%   | 41.21%             | -23.33% |    -0.02 |       42 | 28.29%     | ok               |

## XRP-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 26.40%   | -39.83%            | -31.38% |     0.48 |       70 | 42.91%     | ok               |
|          40 | 9.57%    | -39.83%            | -33.91% |     0.31 |       62 | 36.59%     | ok               |
|          45 | -3.09%   | -39.83%            | -37.18% |     0.15 |       60 | 32.38%     | ok               |
|          30 | -5.52%   | -39.83%            | -31.82% |     0.14 |       65 | 47.89%     | ok               |
|          50 | -7.20%   | -39.83%            | -39.26% |     0.08 |       58 | 24.71%     | ok               |

## YFI-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -47.14%  | -59.99%            | -51.08% |    -0.78 |       56 | 27.39%     | ok               |
|          45 | -47.23%  | -59.99%            | -51.16% |    -1    |       70 | 22.03%     | ok               |
|          35 | -57.19%  | -59.99%            | -60.38% |    -1.02 |       64 | 34.10%     | ok               |
|          30 | -62.90%  | -59.99%            | -65.66% |    -1.17 |       76 | 37.55%     | ok               |
|          25 | -65.20%  | -59.99%            | -67.79% |    -1.21 |       77 | 41.57%     | ok               |

## ZEC-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 207.41%  | 3096.07%           | -30.64% |     1.09 |       46 | 32.95%     | ok               |
|          35 | 166.72%  | 3096.07%           | -50.84% |     0.97 |       52 | 38.51%     | ok               |
|          25 | 157.24%  | 3096.07%           | -58.07% |     0.94 |       53 | 44.44%     | ok               |
|          30 | 152.71%  | 3096.07%           | -56.50% |     0.93 |       57 | 41.95%     | ok               |
|          40 | 126.06%  | 3096.07%           | -54.22% |     0.87 |       54 | 36.40%     | ok               |
