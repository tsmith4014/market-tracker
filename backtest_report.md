# Market Tracker Backtest Report

_Generated: 2026-07-20T04:14:06+00:00_

## Data Sources

- Crypto: Kraken -> Coinbase -> CoinGecko OHLC -> CoinPaprika fallback chain.
- Stocks / ETFs / indices: Stooq -> Yahoo Finance fallback chain.
- Data rows are generated from real market APIs. Mock OHLCV rows are not generated.

## Data Freshness

- Rows: **92,518**
- Symbols: **161**
- Date range: **2024-02-23** to **2026-07-20**

## Latest Signals

| symbol     | date                |         close |   composite_score | signal   | data_source   |
|:-----------|:--------------------|--------------:|------------------:|:---------|:--------------|
| AAPL       | 2026-07-17 00:00:00 |   333.74      |         52.75     | LONG     | Yahoo Finance |
| ABBV       | 2026-07-17 00:00:00 |   254.49      |         36.0833   | LONG     | Yahoo Finance |
| AMZN       | 2026-07-17 00:00:00 |   247.23      |         70.4167   | LONG     | Yahoo Finance |
| BAC        | 2026-07-17 00:00:00 |    61.27      |         49.0833   | LONG     | Yahoo Finance |
| COP        | 2026-07-17 00:00:00 |   114.71      |         71.6667   | LONG     | Yahoo Finance |
| CVX        | 2026-07-17 00:00:00 |   187.38      |         75        | LONG     | Yahoo Finance |
| DBC        | 2026-07-17 00:00:00 |    28.98      |         76.75     | LONG     | Yahoo Finance |
| DE         | 2026-07-17 00:00:00 |   597.24      |         43.9167   | LONG     | Yahoo Finance |
| EOG        | 2026-07-17 00:00:00 |   139.89      |         74.5833   | LONG     | Yahoo Finance |
| ETH-USD    | 2026-07-20 00:00:00 |  1878.53      |         50        | LONG     | Kraken API    |
| LDO-USD    | 2026-07-20 00:00:00 |     0.354     |         45.4167   | LONG     | Kraken API    |
| LINK-USD   | 2026-07-20 00:00:00 |     8.44355   |         53.1667   | LONG     | Kraken API    |
| LTC-USD    | 2026-07-20 00:00:00 |    47.13      |         52.3333   | LONG     | Kraken API    |
| META       | 2026-07-17 00:00:00 |   646.01      |         60.5833   | LONG     | Yahoo Finance |
| MPC        | 2026-07-17 00:00:00 |   312.6       |         73.75     | LONG     | Yahoo Finance |
| MRK        | 2026-07-17 00:00:00 |   127.5       |         47.4167   | LONG     | Yahoo Finance |
| OXY        | 2026-07-17 00:00:00 |    54.86      |         71.6667   | LONG     | Yahoo Finance |
| PEPE-USD   | 2026-07-20 00:00:00 |     2.88e-06  |         52.6667   | LONG     | Kraken API    |
| POL-USD    | 2026-07-20 00:00:00 |     0.08088   |         50.6667   | LONG     | Kraken API    |
| RTX        | 2026-07-17 00:00:00 |   193.51      |         51.8333   | LONG     | Yahoo Finance |
| SCHW       | 2026-07-17 00:00:00 |   101.56      |         57.5833   | LONG     | Yahoo Finance |
| SKY-USD    | 2026-07-20 00:00:00 |     0.06131   |         32.6667   | LONG     | Kraken API    |
| TMO        | 2026-07-17 00:00:00 |   532.48      |         61.3333   | LONG     | Yahoo Finance |
| UNH        | 2026-07-17 00:00:00 |   426.09      |         39.9167   | LONG     | Yahoo Finance |
| UNI-USD    | 2026-07-20 00:00:00 |     3.494     |         31.6667   | LONG     | Kraken API    |
| USO        | 2026-07-17 00:00:00 |   123.96      |         64.5833   | LONG     | Yahoo Finance |
| XBI        | 2026-07-17 00:00:00 |   154.26      |         36.4167   | LONG     | Yahoo Finance |
| XLE        | 2026-07-17 00:00:00 |    57.68      |         73.25     | LONG     | Yahoo Finance |
| XLF        | 2026-07-17 00:00:00 |    56.26      |         59.5833   | LONG     | Yahoo Finance |
| XLV        | 2026-07-17 00:00:00 |   161.09      |         45.0833   | LONG     | Yahoo Finance |
| XOM        | 2026-07-17 00:00:00 |   147.36      |         75        | LONG     | Yahoo Finance |
| ZEC-USD    | 2026-07-20 00:00:00 |   536.24      |         67        | LONG     | Kraken API    |
| AAVE-USD   | 2026-07-20 00:00:00 |    89.73      |         -4.83333  | NEUTRAL  | Kraken API    |
| ADA-USD    | 2026-07-20 00:00:00 |     0.165464  |        -23.6667   | NEUTRAL  | Kraken API    |
| ADBE       | 2026-07-17 00:00:00 |   237.25      |         23.75     | NEUTRAL  | Yahoo Finance |
| ALGO-USD   | 2026-07-20 00:00:00 |     0.08237   |        -38.25     | NEUTRAL  | Kraken API    |
| AMAT       | 2026-07-17 00:00:00 |   529.66      |        -17.5833   | NEUTRAL  | Yahoo Finance |
| AMD        | 2026-07-17 00:00:00 |   495.76      |         -9.83333  | NEUTRAL  | Yahoo Finance |
| AMGN       | 2026-07-17 00:00:00 |   366.29      |         35.1667   | NEUTRAL  | Yahoo Finance |
| APT-USD    | 2026-07-20 00:00:00 |     0.5916    |        -34.9167   | NEUTRAL  | Kraken API    |
| ARB-USD    | 2026-07-20 00:00:00 |     0.0878    |         25.1667   | NEUTRAL  | Kraken API    |
| ATOM-USD   | 2026-07-20 00:00:00 |     1.4664    |        -23.6667   | NEUTRAL  | Kraken API    |
| AVAX-USD   | 2026-07-20 00:00:00 |     6.6       |        -21.1667   | NEUTRAL  | Kraken API    |
| AVGO       | 2026-07-17 00:00:00 |   370.83      |         -8.75     | NEUTRAL  | Yahoo Finance |
| BA         | 2026-07-17 00:00:00 |   214.03      |        -65.25     | NEUTRAL  | Yahoo Finance |
| BITO       | 2026-07-17 00:00:00 |     8.69      |         12.6667   | NEUTRAL  | Yahoo Finance |
| BLK        | 2026-07-17 00:00:00 |  1072.2       |         39.5      | NEUTRAL  | Yahoo Finance |
| BTC-USD    | 2026-07-20 00:00:00 | 64828.8       |         14.25     | NEUTRAL  | Kraken API    |
| C          | 2026-07-17 00:00:00 |   129.36      |         -8.75     | NEUTRAL  | Yahoo Finance |
| CAT        | 2026-07-17 00:00:00 |   880.28      |        -30.5      | NEUTRAL  | Yahoo Finance |
| CL         | 2026-07-17 00:00:00 |    92.98      |         40.8333   | NEUTRAL  | Yahoo Finance |
| CMCSA      | 2026-07-17 00:00:00 |    23.79      |         27.75     | NEUTRAL  | Yahoo Finance |
| COMP-USD   | 2026-07-20 00:00:00 |    16.81      |        -11.6667   | NEUTRAL  | Kraken API    |
| COST       | 2026-07-17 00:00:00 |   940.87      |        -13.25     | NEUTRAL  | Yahoo Finance |
| CRM        | 2026-07-17 00:00:00 |   170.77      |         -8.83333  | NEUTRAL  | Yahoo Finance |
| CRV-USD    | 2026-07-20 00:00:00 |     0.21006   |          4.75     | NEUTRAL  | Kraken API    |
| CSCO       | 2026-07-17 00:00:00 |   111.94      |         -9.75     | NEUTRAL  | Yahoo Finance |
| DASH-USD   | 2026-07-20 00:00:00 |    34.275     |        -45.4167   | NEUTRAL  | Kraken API    |
| DIA        | 2026-07-17 00:00:00 |   520.81      |         16.0833   | NEUTRAL  | Yahoo Finance |
| DIS        | 2026-07-17 00:00:00 |    97.67      |        -47        | NEUTRAL  | Yahoo Finance |
| DOGE-USD   | 2026-07-20 00:00:00 |     0.0726043 |        -12.6667   | NEUTRAL  | Kraken API    |
| DOT-USD    | 2026-07-20 00:00:00 |     0.8136    |        -25.9167   | NEUTRAL  | Kraken API    |
| DXY-INDEX  | 2026-07-17 00:00:00 |   100.75      |         29.8387   | NEUTRAL  | Yahoo Finance |
| EEM        | 2026-07-17 00:00:00 |    63.29      |        -12.3333   | NEUTRAL  | Yahoo Finance |
| EFA        | 2026-07-17 00:00:00 |   103.33      |         -8.16667  | NEUTRAL  | Yahoo Finance |
| ETC-USD    | 2026-07-20 00:00:00 |     6.913     |        -25.9167   | NEUTRAL  | Kraken API    |
| EWJ        | 2026-07-17 00:00:00 |    90.49      |        -23.3333   | NEUTRAL  | Yahoo Finance |
| FCX        | 2026-07-17 00:00:00 |    58.38      |        -11.8333   | NEUTRAL  | Yahoo Finance |
| FIL-USD    | 2026-07-20 00:00:00 |     0.72      |        -48.25     | NEUTRAL  | Kraken API    |
| FXI        | 2026-07-17 00:00:00 |    34.13      |          0.583333 | NEUTRAL  | Yahoo Finance |
| GDX        | 2026-07-17 00:00:00 |    71.32      |        -62.8333   | NEUTRAL  | Yahoo Finance |
| GDXJ       | 2026-07-17 00:00:00 |    92.2       |        -62.8333   | NEUTRAL  | Yahoo Finance |
| GE         | 2026-07-17 00:00:00 |   348.83      |          0.416667 | NEUTRAL  | Yahoo Finance |
| GOOGL      | 2026-07-17 00:00:00 |   346.77      |        -14.5833   | NEUTRAL  | Yahoo Finance |
| GRT-USD    | 2026-07-20 00:00:00 |     0.01635   |        -51.5833   | NEUTRAL  | Kraken API    |
| GS         | 2026-07-17 00:00:00 |  1065.22      |         37.1667   | NEUTRAL  | Yahoo Finance |
| HD         | 2026-07-17 00:00:00 |   338.87      |        -29.0833   | NEUTRAL  | Yahoo Finance |
| HON        | 2026-07-17 00:00:00 |   225.02      |        -49.75     | NEUTRAL  | Yahoo Finance |
| HYG        | 2026-07-17 00:00:00 |    79.65      |        -55.5833   | NEUTRAL  | Yahoo Finance |
| IBIT       | 2026-07-17 00:00:00 |    36.35      |         -8.83333  | NEUTRAL  | Yahoo Finance |
| ICP-USD    | 2026-07-20 00:00:00 |     2.148     |        -55.25     | NEUTRAL  | Kraken API    |
| IEF        | 2026-07-17 00:00:00 |    93.84      |        -58        | NEUTRAL  | Yahoo Finance |
| IEMG       | 2026-07-17 00:00:00 |    76.98      |        -12.3333   | NEUTRAL  | Yahoo Finance |
| INJ-USD    | 2026-07-20 00:00:00 |     5.134     |         61.1667   | NEUTRAL  | Kraken API    |
| INTC       | 2026-07-17 00:00:00 |    95.04      |        -24.8333   | NEUTRAL  | Yahoo Finance |
| INTU       | 2026-07-17 00:00:00 |   291.09      |         -6.83333  | NEUTRAL  | Yahoo Finance |
| ITA        | 2026-07-17 00:00:00 |   230.73      |        -19.5833   | NEUTRAL  | Yahoo Finance |
| IWM        | 2026-07-17 00:00:00 |   294.04      |          0.166667 | NEUTRAL  | Yahoo Finance |
| JNJ        | 2026-07-17 00:00:00 |   253.04      |         29.4167   | NEUTRAL  | Yahoo Finance |
| JPM        | 2026-07-17 00:00:00 |   341.1       |         30.3333   | NEUTRAL  | Yahoo Finance |
| KO         | 2026-07-17 00:00:00 |    81.56      |         12.0833   | NEUTRAL  | Yahoo Finance |
| LIN        | 2026-07-17 00:00:00 |   513.22      |        -13.3333   | NEUTRAL  | Yahoo Finance |
| LLY        | 2026-07-17 00:00:00 |  1179.11      |         10.6667   | NEUTRAL  | Yahoo Finance |
| LRCX       | 2026-07-17 00:00:00 |   313.3       |        -32.75     | NEUTRAL  | Yahoo Finance |
| MCD        | 2026-07-17 00:00:00 |   267.71      |        -43.5      | NEUTRAL  | Yahoo Finance |
| MS         | 2026-07-17 00:00:00 |   215.5       |          7.83333  | NEUTRAL  | Yahoo Finance |
| MSFT       | 2026-07-17 00:00:00 |   393.82      |        -10.5      | NEUTRAL  | Yahoo Finance |
| MU         | 2026-07-17 00:00:00 |   848.95      |        -36.0833   | NEUTRAL  | Yahoo Finance |
| NEAR-USD   | 2026-07-20 00:00:00 |     1.9238    |         -2.16667  | NEUTRAL  | Kraken API    |
| NEM        | 2026-07-17 00:00:00 |    89.7       |        -62.8333   | NEUTRAL  | Yahoo Finance |
| NKE        | 2026-07-17 00:00:00 |    43.76      |          0.166667 | NEUTRAL  | Yahoo Finance |
| NOW        | 2026-07-17 00:00:00 |   103.24      |        -26.1667   | NEUTRAL  | Yahoo Finance |
| NVDA       | 2026-07-17 00:00:00 |   202.81      |         10.0833   | NEUTRAL  | Yahoo Finance |
| OP-USD     | 2026-07-20 00:00:00 |     0.0947    |        -51.5833   | NEUTRAL  | Kraken API    |
| PEP        | 2026-07-17 00:00:00 |   137.12      |        -67.8333   | NEUTRAL  | Yahoo Finance |
| PFE        | 2026-07-17 00:00:00 |    25.05      |          2.41667  | NEUTRAL  | Yahoo Finance |
| PG         | 2026-07-17 00:00:00 |   149.98      |         46.25     | NEUTRAL  | Yahoo Finance |
| PM         | 2026-07-17 00:00:00 |   192.98      |         63.3333   | NEUTRAL  | Yahoo Finance |
| QCOM       | 2026-07-17 00:00:00 |   171.78      |        -55.8333   | NEUTRAL  | Yahoo Finance |
| QQQ        | 2026-07-17 00:00:00 |   695.33      |        -27.3333   | NEUTRAL  | Yahoo Finance |
| RENDER-USD | 2026-07-20 00:00:00 |     1.486     |        -45.25     | NEUTRAL  | Kraken API    |
| SBUX       | 2026-07-17 00:00:00 |   105.49      |         53.6667   | NEUTRAL  | Yahoo Finance |
| SHIB-USD   | 2026-07-20 00:00:00 |     4.187e-06 |        -30.75     | NEUTRAL  | Kraken API    |
| SHY        | 2026-07-17 00:00:00 |    81.99      |        -21.4167   | NEUTRAL  | Yahoo Finance |
| SLB        | 2026-07-17 00:00:00 |    46.99      |         -4        | NEUTRAL  | Yahoo Finance |
| SMH        | 2026-07-17 00:00:00 |   556.53      |        -32.75     | NEUTRAL  | Yahoo Finance |
| SNX-USD    | 2026-07-20 00:00:00 |     0.2358    |         16.4167   | NEUTRAL  | Kraken API    |
| SOL-USD    | 2026-07-20 00:00:00 |    76.72      |          9.41667  | NEUTRAL  | Kraken API    |
| SOXX       | 2026-07-17 00:00:00 |   521.81      |        -21.5      | NEUTRAL  | Yahoo Finance |
| SPY        | 2026-07-17 00:00:00 |   743.29      |         27.8333   | NEUTRAL  | Yahoo Finance |
| SUSHI-USD  | 2026-07-20 00:00:00 |     0.1676    |         26        | NEUTRAL  | Kraken API    |
| T          | 2026-07-17 00:00:00 |    21.81      |        -16.75     | NEUTRAL  | Yahoo Finance |
| TGT        | 2026-07-17 00:00:00 |   139.6       |         41.6667   | NEUTRAL  | Yahoo Finance |
| TMUS       | 2026-07-17 00:00:00 |   192.43      |         30.5833   | NEUTRAL  | Yahoo Finance |
| TRX-USD    | 2026-07-20 00:00:00 |     0.326229  |         16.8333   | NEUTRAL  | Kraken API    |
| TSLA       | 2026-07-17 00:00:00 |   380.84      |        -55        | NEUTRAL  | Yahoo Finance |
| TXN        | 2026-07-17 00:00:00 |   284.02      |        -27.3333   | NEUTRAL  | Yahoo Finance |
| UPS        | 2026-07-17 00:00:00 |   117.72      |         64        | NEUTRAL  | Yahoo Finance |
| VEA        | 2026-07-17 00:00:00 |    69.7       |        -23.3333   | NEUTRAL  | Yahoo Finance |
| VIXY       | 2026-07-17 00:00:00 |    21.65      |          1        | NEUTRAL  | Yahoo Finance |
| VNQ        | 2026-07-17 00:00:00 |   100.02      |         61.8333   | NEUTRAL  | Yahoo Finance |
| VTI        | 2026-07-17 00:00:00 |   367.01      |         27.8333   | NEUTRAL  | Yahoo Finance |
| VWO        | 2026-07-17 00:00:00 |    57.84      |        -39.5833   | NEUTRAL  | Yahoo Finance |
| VZ         | 2026-07-17 00:00:00 |    43.59      |        -20.25     | NEUTRAL  | Yahoo Finance |
| WFC        | 2026-07-17 00:00:00 |    87.51      |         40.5833   | NEUTRAL  | Yahoo Finance |
| WMT        | 2026-07-17 00:00:00 |   114.24      |        -29.5      | NEUTRAL  | Yahoo Finance |
| XLB        | 2026-07-17 00:00:00 |    50.53      |        -22.8333   | NEUTRAL  | Yahoo Finance |
| XLC        | 2026-07-17 00:00:00 |   110.65      |        -20.3333   | NEUTRAL  | Yahoo Finance |
| XLI        | 2026-07-17 00:00:00 |   179.41      |          9.16667  | NEUTRAL  | Yahoo Finance |
| XLK        | 2026-07-17 00:00:00 |   175.59      |        -27.3333   | NEUTRAL  | Yahoo Finance |
| XLM-USD    | 2026-07-20 00:00:00 |     0.187482  |        -43.9167   | NEUTRAL  | Kraken API    |
| XLP        | 2026-07-17 00:00:00 |    85.19      |         59.8333   | NEUTRAL  | Yahoo Finance |
| XLU        | 2026-07-17 00:00:00 |    45.17      |        -16.0833   | NEUTRAL  | Yahoo Finance |
| XLY        | 2026-07-17 00:00:00 |   115.44      |        -24.75     | NEUTRAL  | Yahoo Finance |
| XRP-USD    | 2026-07-20 00:00:00 |     1.09967   |        -21.6667   | NEUTRAL  | Kraken API    |
| YFI-USD    | 2026-07-20 00:00:00 |  2119.5       |          4.08333  | NEUTRAL  | Kraken API    |
| AGG        | 2026-07-17 00:00:00 |    98.2       |        -50.5833   | SHORT    | Yahoo Finance |
| ARKK       | 2026-07-17 00:00:00 |    75.2       |        -47        | SHORT    | Yahoo Finance |
| BCH-USD    | 2026-07-20 00:00:00 |   213.98      |        -58.3333   | SHORT    | Kraken API    |
| BND        | 2026-07-17 00:00:00 |    72.86      |        -47.25     | SHORT    | Yahoo Finance |
| BONK-USD   | 2026-07-20 00:00:00 |     3.068e-06 |        -48.3333   | SHORT    | Kraken API    |
| FET-USD    | 2026-07-20 00:00:00 |     0.1506    |        -36.75     | SHORT    | Kraken API    |
| GLD        | 2026-07-17 00:00:00 |   368.41      |        -30.4167   | SHORT    | Yahoo Finance |
| HBAR-USD   | 2026-07-20 00:00:00 |     0.06611   |        -36        | SHORT    | Kraken API    |
| IBM        | 2026-07-17 00:00:00 |   212.67      |        -57.25     | SHORT    | Yahoo Finance |
| NFLX       | 2026-07-17 00:00:00 |    68.95      |        -37.1667   | SHORT    | Yahoo Finance |
| ORCL       | 2026-07-17 00:00:00 |   126.41      |        -53.9167   | SHORT    | Yahoo Finance |
| SLV        | 2026-07-17 00:00:00 |    50.78      |        -32.9167   | SHORT    | Yahoo Finance |
| TIA-USD    | 2026-07-20 00:00:00 |     0.3618    |        -37        | SHORT    | Kraken API    |
| TLT        | 2026-07-17 00:00:00 |    84.52      |        -52.0833   | SHORT    | Yahoo Finance |
| WIF-USD    | 2026-07-20 00:00:00 |     0.1528    |        -40.3333   | SHORT    | Kraken API    |

## Edge Summary

- Symbols with trades: **160** of 160
- Beat buy-and-hold: **33.75%** of traded symbols
- Positive return: **30.00%** of traded symbols
- Median strategy return: **-10.73%** (benchmark **14.22%**)
- Median excess vs benchmark: **-25.97%**
- Median Sharpe: **-0.13**
- Median exposure: **44.34%**

> Edge is real only if both _beat buy-and-hold_ and _median excess_ are convincingly positive across many symbols. Treat a single high-return symbol as noise.

## Portfolio Backtest

Actual capital-allocation books (not per-symbol averages). Benchmarks: `equal_weight_buyhold` (whole tracked universe), `spy_buyhold` (100% SPY), and `sixty_forty` (60% SPY / 40% AGG). `high_conf_voltarget` inverse-vol-weights the HIGH-confidence book; `conviction_long_short` is market-neutral. Judge on **Sharpe** and **max_drawdown** out-of-sample, not raw return: a fully-invested long book wins on return in a bull market but carries all the risk.

| strategy              | scope         | ann_return   | ann_vol   |   sharpe | max_drawdown   | total_return   |   avg_gross_exposure |
|:----------------------|:--------------|:-------------|:----------|---------:|:---------------|:---------------|---------------------:|
| equal_weight_buyhold  | full          | -4.82%       | 32.44%    |    -0.15 | -47.08%        | -26.57%        |                 1    |
| equal_weight_buyhold  | out_of_sample | -23.76%      | 31.02%    |    -0.77 | -39.63%        | -26.31%        |                 1    |
| all_signals_ew        | full          | -18.20%      | 26.98%    |    -0.67 | -61.93%        | -48.71%        |                 1    |
| all_signals_ew        | out_of_sample | 20.01%       | 26.79%    |     0.75 | -18.39%        | 19.22%         |                 1    |
| high_conf_ew          | full          | -1.11%       | 31.39%    |    -0.04 | -44.00%        | -16.66%        |                 0.88 |
| high_conf_ew          | out_of_sample | 19.91%       | 33.87%    |     0.59 | -17.94%        | 16.54%         |                 0.88 |
| high_conf_voltarget   | full          | 0.97%        | 28.95%    |     0.03 | -36.19%        | -9.14%         |                 0.88 |
| high_conf_voltarget   | out_of_sample | 14.36%       | 31.36%    |     0.46 | -16.94%        | 10.80%         |                 0.88 |
| conviction_long_short | full          | -19.43%      | 22.97%    |    -0.85 | -50.68%        | -49.03%        |                 0.97 |
| conviction_long_short | out_of_sample | -11.65%      | 26.25%    |    -0.44 | -24.28%        | -14.90%        |                 0.97 |
| spy_buyhold           | full          | 5.88%        | 13.32%    |     0.44 | -17.80%        | 16.45%         |                 0.78 |
| spy_buyhold           | out_of_sample | -3.51%       | 9.78%     |    -0.36 | -13.27%        | -4.17%         |                 0.78 |
| sixty_forty           | full          | 3.51%        | 8.42%     |     0.42 | -10.77%        | 10.11%         |                 0.78 |
| sixty_forty           | out_of_sample | -3.45%       | 6.45%     |    -0.54 | -9.26%         | -3.83%         |                 0.78 |

## Walk-Forward Robustness

Each book measured across contiguous time folds (each a different regime). A book has durable edge only if `mean_sharpe` is positive, `min_sharpe` isn't deeply negative, and `pct_positive_folds` is high — a single great fold doesn't count. `fold_sharpes` lists each fold oldest-to-newest.

| strategy              |   n_folds |   mean_sharpe |   median_sharpe |   min_sharpe | pct_positive_folds   | mean_return   | fold_sharpes                 |
|:----------------------|----------:|--------------:|----------------:|-------------:|:---------------------|:--------------|:-----------------------------|
| equal_weight_buyhold  |         5 |          0.23 |            0.55 |        -1.6  | 60.00%               | -2.45%        | 1.71;-1.60;1.53;-1.03;0.55   |
| all_signals_ew        |         5 |         -0.76 |           -0.25 |        -2.64 | 20.00%               | -11.18%       | -0.25;-0.15;-2.64;0.31;-1.08 |
| high_conf_ew          |         5 |          0.07 |           -0.43 |        -0.78 | 40.00%               | -2.73%        | 1.26;-0.44;-0.78;0.74;-0.43  |
| high_conf_voltarget   |         5 |          0.24 |           -0.13 |        -0.87 | 40.00%               | -1.06%        | 2.04;-0.13;-0.87;0.71;-0.54  |
| conviction_long_short |         5 |         -1.01 |           -1.33 |        -1.72 | 20.00%               | -12.26%       | -1.53;-1.33;-0.79;0.32;-1.72 |
| spy_buyhold           |         5 |          0.66 |            0.05 |        -1.09 | 60.00%               | 3.52%         | 1.52;-0.37;3.17;-1.09;0.05   |
| sixty_forty           |         5 |          0.61 |           -0.29 |        -1.07 | 40.00%               | 2.14%         | 1.71;-0.48;3.19;-1.07;-0.29  |

## Strategy Comparison

Each decision rule backtested over the same data. `out_of_sample` is the most recent ~35% of each symbol's history (unseen tail). A rule has real edge only if `median_excess` and `beat_benchmark_pct` stay positive out-of-sample, not just full-sample.

| strategy        | scope         |   symbols | beat_benchmark_pct   | positive_pct   | median_return   | median_benchmark   | median_excess   |   median_sharpe |   total_trades |
|:----------------|:--------------|----------:|:---------------------|:---------------|:----------------|:-------------------|:----------------|----------------:|---------------:|
| trend           | full          |       160 | 33.75%               | 30.00%         | -10.73%         | 14.22%             | -25.97%         |           -0.13 |          11243 |
| trend           | out_of_sample |       160 | 41.25%               | 53.12%         | 1.71%           | 4.66%              | -4.87%          |            0.33 |           3765 |
| mean_reversion  | full          |       157 | 40.13%               | 50.96%         | 0.06%           | 13.92%             | -14.42%         |            0.04 |           1266 |
| mean_reversion  | out_of_sample |       124 | 49.19%               | 59.68%         | 0.38%           | -0.76%             | -1.13%          |            0.5  |            426 |
| regime_adaptive | full          |       160 | 35.00%               | 31.25%         | -11.22%         | 14.22%             | -25.47%         |           -0.13 |          11520 |
| regime_adaptive | out_of_sample |       160 | 41.88%               | 54.37%         | 1.73%           | 4.66%              | -4.20%          |            0.33 |           3870 |

## Signal Calibration

Realized forward return in the signal's direction, grouped by confidence. HIGH should outrank LOW for the confidence score to be meaningful.

| confidence_level   |   horizon |     n | mean_return   | median_return   | win_rate   |
|:-------------------|----------:|------:|:--------------|:----------------|:-----------|
| HIGH               |         5 |  7923 | 0.11%         | 0.10%           | 51.65%     |
| MEDIUM             |         5 | 29151 | 0.01%         | 0.07%           | 50.75%     |
| LOW                |         5 |  3379 | -0.63%        | -0.56%          | 44.48%     |
| ALL                |         5 | 40453 | -0.02%        | 0.04%           | 50.40%     |
| HIGH               |        10 |  7887 | 0.38%         | 0.10%           | 51.16%     |
| MEDIUM             |        10 | 28960 | 0.15%         | 0.11%           | 50.80%     |
| LOW                |        10 |  3320 | -0.91%        | -0.73%          | 45.27%     |
| ALL                |        10 | 40167 | 0.11%         | 0.05%           | 50.42%     |
| HIGH               |        20 |  7797 | 0.76%         | 0.32%           | 52.70%     |
| MEDIUM             |        20 | 28586 | 0.81%         | 0.60%           | 53.41%     |
| LOW                |        20 |  3252 | -0.69%        | -0.49%          | 47.36%     |
| ALL                |        20 | 39635 | 0.68%         | 0.47%           | 52.78%     |

## Backtest Summary

### Data Quality / Signal Availability

- **ok**: 160 symbols

| symbol     |   trades | return   | benchmark_return   | mdd     |   sharpe | exposure   | skipped_reason   |
|:-----------|---------:|:---------|:-------------------|:--------|---------:|:-----------|:-----------------|
| AAPL       |       61 | 20.81%   | 82.85%             | -20.65% |     0.49 | 49.25%     | ok               |
| AAVE-USD   |       74 | -52.09%  | -65.80%            | -68.26% |    -0.48 | 39.27%     | ok               |
| ABBV       |       66 | -19.64%  | 42.90%             | -30.55% |    -0.41 | 47.25%     | ok               |
| ADA-USD    |       90 | -83.04%  | -79.32%            | -89.12% |    -0.67 | 46.93%     | ok               |
| ADBE       |       64 | -30.20%  | -57.13%            | -35.81% |    -0.38 | 57.40%     | ok               |
| AGG        |       69 | -6.87%   | 0.88%              | -10.02% |    -1.14 | 31.61%     | ok               |
| ALGO-USD   |       86 | -50.43%  | -72.22%            | -53.13% |    -0.57 | 38.12%     | ok               |
| AMAT       |       71 | -33.55%  | 168.64%            | -57.21% |    -0.29 | 52.25%     | ok               |
| AMD        |       52 | 5.86%    | 180.85%            | -43.98% |     0.27 | 35.77%     | ok               |
| AMGN       |       69 | -15.41%  | 26.67%             | -34.14% |    -0.29 | 46.26%     | ok               |
| AMZN       |       80 | -37.74%  | 41.28%             | -42.48% |    -1.14 | 38.27%     | ok               |
| APT-USD    |       74 | -42.76%  | -90.30%            | -69.96% |    -0.26 | 42.15%     | ok               |
| ARB-USD    |       72 | -26.78%  | -82.34%            | -62.34% |    -0.08 | 39.27%     | ok               |
| ARKK       |       83 | -35.16%  | 55.34%             | -36.65% |    -0.63 | 39.60%     | ok               |
| ATOM-USD   |       88 | -68.01%  | -70.12%            | -73.75% |    -1.16 | 44.44%     | ok               |
| AVAX-USD   |       72 | -39.70%  | -75.00%            | -60.45% |    -0.36 | 37.93%     | ok               |
| AVGO       |       64 | 15.12%   | 186.05%            | -35.76% |     0.34 | 42.60%     | ok               |
| BA         |       67 | 7.60%    | 6.57%              | -30.56% |     0.25 | 49.25%     | ok               |
| BAC        |       78 | -6.46%   | 80.63%             | -26.91% |    -0.09 | 49.92%     | ok               |
| BCH-USD    |       80 | -4.92%   | -37.33%            | -54.34% |     0.16 | 48.47%     | ok               |
| BITO       |       80 | 0.48%    | -64.02%            | -42.82% |     0.18 | 41.26%     | ok               |
| BLK        |       71 | -7.59%   | 31.79%             | -24.29% |    -0.16 | 42.43%     | ok               |
| BND        |       67 | -7.81%   | 0.94%              | -9.98%  |    -1.26 | 32.95%     | ok               |
| BONK-USD   |       70 | 70.45%   | -83.47%            | -45.22% |     0.72 | 41.95%     | ok               |
| BTC-USD    |       76 | -3.75%   | -33.48%            | -24.23% |     0.09 | 52.68%     | ok               |
| C          |       79 | -30.57%  | 131.29%            | -38.11% |    -0.61 | 51.08%     | ok               |
| CAT        |       72 | 21.81%   | 171.79%            | -21.02% |     0.45 | 55.74%     | ok               |
| CL         |       62 | 7.60%    | 7.80%              | -14.32% |     0.3  | 45.76%     | ok               |
| CMCSA      |       82 | -41.17%  | -39.42%            | -41.04% |    -1.1  | 42.26%     | ok               |
| COMP-USD   |       89 | -42.10%  | -71.27%            | -57.88% |    -0.3  | 45.59%     | ok               |
| COP        |       72 | -22.31%  | 2.87%              | -43.96% |    -0.39 | 41.93%     | ok               |
| COST       |       60 | -1.68%   | 27.50%             | -29.73% |     0.02 | 43.43%     | ok               |
| CRM        |       63 | -39.56%  | -41.68%            | -41.36% |    -0.83 | 42.76%     | ok               |
| CRV-USD    |       68 | -6.45%   | -60.22%            | -39.89% |     0.17 | 36.21%     | ok               |
| CSCO       |       61 | 23.62%   | 129.10%            | -21.79% |     0.52 | 48.92%     | ok               |
| CVX        |       75 | -15.68%  | 21.16%             | -29.13% |    -0.39 | 39.93%     | ok               |
| DASH-USD   |       61 | -41.76%  | 22.79%             | -64.43% |    -0.02 | 29.12%     | ok               |
| DBC        |       62 | -11.77%  | 33.30%             | -25.70% |    -0.39 | 33.61%     | ok               |
| DE         |       74 | -6.93%   | 63.78%             | -25.24% |    -0.05 | 47.25%     | ok               |
| DIA        |       62 | -4.38%   | 33.10%             | -12.94% |    -0.21 | 44.09%     | ok               |
| DIS        |       66 | -21.49%  | -9.35%             | -28.17% |    -0.42 | 45.59%     | ok               |
| DOGE-USD   |       71 | -22.30%  | -73.29%            | -60.95% |     0.02 | 50.00%     | ok               |
| DOT-USD    |       86 | -56.50%  | -84.27%            | -63.10% |    -0.58 | 47.70%     | ok               |
| DXY-INDEX  |       40 | -1.53%   | 0.15%              | -6.02%  |    -0.23 | 30.87%     | ok               |
| EEM        |       64 | -10.42%  | 55.89%             | -25.67% |    -0.28 | 42.93%     | ok               |
| EFA        |       62 | -9.68%   | 33.50%             | -15.14% |    -0.36 | 44.76%     | ok               |
| EOG        |       81 | -22.13%  | 25.06%             | -48.13% |    -0.45 | 47.25%     | ok               |
| ETC-USD    |       64 | -29.79%  | -67.70%            | -45.98% |    -0.38 | 29.69%     | ok               |
| ETH-USD    |       64 | 144.88%  | -31.08%            | -30.11% |     1.22 | 44.83%     | ok               |
| EWJ        |       62 | -19.61%  | 31.13%             | -30.73% |    -0.65 | 38.77%     | ok               |
| FCX        |       63 | -27.81%  | 49.85%             | -47.47% |    -0.31 | 45.26%     | ok               |
| FET-USD    |       85 | -37.15%  | -81.38%            | -54.02% |    -0.11 | 42.15%     | ok               |
| FIL-USD    |       70 | -45.82%  | -79.61%            | -50.22% |    -0.58 | 32.57%     | ok               |
| FXI        |       44 | -6.84%   | 41.50%             | -23.91% |    -0.09 | 30.12%     | ok               |
| GDX        |       60 | 11.28%   | 167.52%            | -34.99% |     0.3  | 48.09%     | ok               |
| GDXJ       |       66 | -22.87%  | 185.27%            | -44.93% |    -0.21 | 46.09%     | ok               |
| GE         |       76 | 11.46%   | 185.06%            | -27.82% |     0.31 | 52.91%     | ok               |
| GLD        |       50 | 25.73%   | 95.32%             | -16.63% |     0.65 | 47.75%     | ok               |
| GOOGL      |       59 | 79.31%   | 140.88%            | -20.41% |     1.18 | 53.08%     | ok               |
| GRT-USD    |       81 | -19.42%  | -88.56%            | -54.83% |    -0.02 | 41.76%     | ok               |
| GS         |       76 | -2.38%   | 172.40%            | -22.13% |     0.05 | 52.08%     | ok               |
| HD         |       71 | -7.53%   | -8.90%             | -17.69% |    -0.12 | 44.59%     | ok               |
| HON        |       93 | -26.82%  | 13.46%             | -29.80% |    -0.72 | 52.41%     | ok               |
| HYG        |       81 | -9.08%   | 2.97%              | -9.59%  |    -1.06 | 33.94%     | ok               |
| IBIT       |       34 | 30.82%   | -4.37%             | -18.95% |     0.66 | 32.02%     | ok               |
| IBM        |       77 | -17.78%  | 14.51%             | -44.74% |    -0.16 | 49.75%     | ok               |
| ICP-USD    |       77 | -14.10%  | -70.34%            | -52.78% |     0.11 | 34.87%     | ok               |
| IEF        |       78 | -11.04%  | -0.21%             | -11.70% |    -1.56 | 32.95%     | ok               |
| IEMG       |       58 | -8.89%   | 50.79%             | -26.84% |    -0.25 | 42.43%     | ok               |
| INJ-USD    |       75 | -52.18%  | -66.53%            | -77.42% |    -0.49 | 37.93%     | ok               |
| INTC       |       68 | 59.68%   | 121.07%            | -60.60% |     0.64 | 49.08%     | ok               |
| INTU       |       67 | -19.54%  | -55.88%            | -42.15% |    -0.23 | 41.60%     | ok               |
| ITA        |       72 | -3.02%   | 82.51%             | -23.75% |    -0.01 | 48.25%     | ok               |
| IWM        |       48 | 9.40%    | 47.10%             | -12.83% |     0.39 | 35.77%     | ok               |
| JNJ        |       68 | 4.23%    | 56.35%             | -17.51% |     0.2  | 50.92%     | ok               |
| JPM        |       77 | -21.27%  | 85.39%             | -33.43% |    -0.52 | 53.91%     | ok               |
| KO         |       51 | 23.79%   | 33.27%             | -8.18%  |     0.86 | 37.94%     | ok               |
| LDO-USD    |       78 | 9.45%    | -81.08%            | -62.63% |     0.35 | 40.42%     | ok               |
| LIN        |       66 | -5.20%   | 14.67%             | -21.53% |    -0.13 | 38.94%     | ok               |
| LINK-USD   |       75 | -15.44%  | -56.43%            | -49.35% |     0.08 | 42.91%     | ok               |
| LLY        |       71 | -28.45%  | 53.22%             | -53.34% |    -0.42 | 49.42%     | ok               |
| LRCX       |       80 | -26.29%  | 237.43%            | -63.56% |    -0.16 | 44.59%     | ok               |
| LTC-USD    |       72 | -32.41%  | -62.26%            | -53.76% |    -0.26 | 49.81%     | ok               |
| MCD        |       75 | -2.55%   | -10.09%            | -18.81% |    -0.05 | 38.10%     | ok               |
| META       |       74 | -32.31%  | 33.46%             | -40.36% |    -0.58 | 47.92%     | ok               |
| MPC        |       71 | -5.56%   | 84.38%             | -44.76% |     0.02 | 48.92%     | ok               |
| MRK        |       69 | -29.71%  | -1.51%             | -35.95% |    -0.71 | 44.26%     | ok               |
| MS         |       77 | -10.18%  | 148.99%            | -27.79% |    -0.16 | 49.58%     | ok               |
| MSFT       |       83 | -38.11%  | -4.03%             | -39.15% |    -1.01 | 47.25%     | ok               |
| MU         |       49 | 270.03%  | 887.15%            | -68.76% |     1.34 | 59.73%     | ok               |
| NEAR-USD   |       85 | -11.27%  | -45.81%            | -59.86% |     0.14 | 41.38%     | ok               |
| NEM        |       72 | -31.13%  | 186.76%            | -38.49% |    -0.33 | 53.08%     | ok               |
| NFLX       |       64 | 28.87%   | 18.15%             | -21.09% |     0.63 | 53.91%     | ok               |
| NKE        |       91 | -48.19%  | -58.57%            | -57.25% |    -0.9  | 43.59%     | ok               |
| NOW        |       80 | 6.39%    | -33.05%            | -27.34% |     0.24 | 45.76%     | ok               |
| NVDA       |       75 | -26.92%  | 155.05%            | -45.02% |    -0.19 | 59.89%     | ok               |
| OP-USD     |       74 | -35.22%  | -91.81%            | -71.48% |    -0.19 | 34.10%     | ok               |
| ORCL       |       70 | 123.37%  | 12.92%             | -29.47% |     1    | 54.41%     | ok               |
| OXY        |       71 | 0.50%    | -8.60%             | -34.15% |     0.13 | 45.92%     | ok               |
| PEP        |       75 | -4.54%   | -19.15%            | -21.35% |    -0.07 | 48.25%     | ok               |
| PEPE-USD   |       81 | 4.55%    | -72.03%            | -57.66% |     0.32 | 45.21%     | ok               |
| PFE        |       77 | -41.09%  | -9.76%             | -41.92% |    -1.32 | 36.27%     | ok               |
| PG         |       68 | -19.91%  | -6.86%             | -24.55% |    -0.76 | 39.93%     | ok               |
| PM         |       83 | -3.22%   | 110.77%            | -33.68% |     0.03 | 55.74%     | ok               |
| POL-USD    |       75 | 39.80%   | -74.99%            | -46.45% |     0.6  | 46.93%     | ok               |
| QCOM       |       73 | -15.25%  | 10.89%             | -56.59% |    -0.04 | 46.09%     | ok               |
| QQQ        |       62 | 20.19%   | 59.19%             | -12.88% |     0.58 | 43.76%     | ok               |
| RENDER-USD |       98 | -19.07%  | -64.28%            | -45.00% |     0.1  | 42.52%     | ok               |
| RTX        |       56 | 25.41%   | 114.99%            | -16.99% |     0.63 | 51.91%     | ok               |
| SBUX       |       64 | -19.93%  | 10.32%             | -29.22% |    -0.37 | 39.93%     | ok               |
| SCHW       |       74 | -13.61%  | 57.60%             | -31.92% |    -0.26 | 47.92%     | ok               |
| SHIB-USD   |       76 | -30.88%  | -74.94%            | -47.96% |    -0.22 | 51.34%     | ok               |
| SHY        |       48 | -2.24%   | 0.39%              | -2.85%  |    -0.79 | 34.28%     | ok               |
| SKY-USD    |       74 | -31.05%  | 6.02%              | -44.74% |    -0.39 | 40.61%     | ok               |
| SLB        |       73 | -23.87%  | -3.75%             | -54.23% |    -0.39 | 51.08%     | ok               |
| SLV        |       60 | 49.94%   | 141.92%            | -42.66% |     0.69 | 43.43%     | ok               |
| SMH        |       48 | 79.19%   | 166.77%            | -33.99% |     1.08 | 47.59%     | ok               |
| SNX-USD    |       58 | -15.26%  | -77.11%            | -34.76% |     0.08 | 37.93%     | ok               |
| SOL-USD    |       70 | -33.05%  | -61.53%            | -56.90% |    -0.09 | 60.15%     | ok               |
| SOXX       |       57 | 70.36%   | 145.96%            | -41.89% |     0.95 | 46.42%     | ok               |
| SPY        |       64 | 1.80%    | 46.36%             | -16.47% |     0.12 | 49.92%     | ok               |
| SUSHI-USD  |       98 | -81.93%  | -81.98%            | -85.48% |    -1.29 | 36.78%     | ok               |
| T          |       64 | 37.51%   | 29.82%             | -17.01% |     0.84 | 53.24%     | ok               |
| TGT        |       60 | -12.17%  | -7.84%             | -40.57% |    -0.17 | 38.77%     | ok               |
| TIA-USD    |       93 | -45.27%  | -88.64%            | -67.94% |    -0.32 | 36.78%     | ok               |
| TLT        |       72 | -21.71%  | -9.96%             | -21.87% |    -1.69 | 32.45%     | ok               |
| TMO        |       61 | 18.14%   | -5.71%             | -18.85% |     0.45 | 51.25%     | ok               |
| TMUS       |       70 | 6.20%    | 17.09%             | -25.71% |     0.23 | 47.92%     | ok               |
| TRX-USD    |       68 | 7.33%    | 40.89%             | -22.90% |     0.28 | 48.66%     | ok               |
| TSLA       |       70 | -14.59%  | 98.39%             | -54.91% |     0.05 | 41.26%     | ok               |
| TXN        |       73 | -12.67%  | 73.51%             | -47.39% |    -0.05 | 52.75%     | ok               |
| UNH        |       74 | 28.33%   | -19.18%            | -27.59% |     0.5  | 52.58%     | ok               |
| UNI-USD    |       86 | -72.48%  | -65.24%            | -80.61% |    -0.87 | 44.44%     | ok               |
| UPS        |       70 | -37.14%  | -20.80%            | -38.83% |    -0.75 | 39.27%     | ok               |
| USO        |       68 | 11.24%   | 72.36%             | -43.35% |     0.3  | 34.11%     | ok               |
| VEA        |       58 | -0.98%   | 42.68%             | -17.93% |     0.01 | 44.09%     | ok               |
| VIXY       |       96 | -80.86%  | -60.89%            | -88.16% |    -1.03 | 32.78%     | ok               |
| VNQ        |       71 | -15.77%  | 17.93%             | -24.92% |    -0.66 | 36.94%     | ok               |
| VTI        |       70 | -4.76%   | 45.64%             | -18.77% |    -0.11 | 50.25%     | ok               |
| VWO        |       78 | -14.74%  | 39.11%             | -25.20% |    -0.52 | 43.76%     | ok               |
| VZ         |       85 | -29.12%  | 7.21%              | -27.37% |    -0.99 | 37.60%     | ok               |
| WFC        |       86 | -16.92%  | 62.48%             | -31.43% |    -0.27 | 51.08%     | ok               |
| WIF-USD    |       70 | -35.45%  | -79.02%            | -51.39% |    -0.13 | 32.95%     | ok               |
| WMT        |       61 | 12.53%   | 95.22%             | -21.31% |     0.4  | 50.42%     | ok               |
| XBI        |       62 | 0.18%    | 62.81%             | -19.80% |     0.09 | 40.93%     | ok               |
| XLB        |       62 | -9.41%   | 16.39%             | -25.37% |    -0.3  | 36.61%     | ok               |
| XLC        |       69 | 10.32%   | 38.80%             | -12.33% |     0.39 | 54.08%     | ok               |
| XLE        |       75 | -8.08%   | 34.20%             | -37.64% |    -0.13 | 45.26%     | ok               |
| XLF        |       78 | -11.84%  | 39.60%             | -23.61% |    -0.39 | 48.09%     | ok               |
| XLI        |       66 | -2.98%   | 49.23%             | -11.79% |    -0.07 | 44.26%     | ok               |
| XLK        |       40 | 65.83%   | 71.07%             | -14.75% |     1.22 | 45.59%     | ok               |
| XLM-USD    |       69 | 5.21%    | -46.53%            | -50.36% |     0.28 | 45.79%     | ok               |
| XLP        |       68 | 4.18%    | 13.92%             | -11.16% |     0.27 | 41.43%     | ok               |
| XLU        |       67 | -5.24%   | 45.80%             | -20.40% |    -0.19 | 39.10%     | ok               |
| XLV        |       68 | -15.51%  | 8.95%              | -19.97% |    -0.77 | 36.11%     | ok               |
| XLY        |       70 | 3.26%    | 27.35%             | -14.01% |     0.17 | 44.43%     | ok               |
| XOM        |       57 | 5.96%    | 41.91%             | -20.29% |     0.24 | 36.77%     | ok               |
| XRP-USD    |       58 | -30.47%  | -59.86%            | -44.89% |    -0.26 | 33.72%     | ok               |
| YFI-USD    |       81 | -64.14%  | -65.28%            | -71.12% |    -1.03 | 40.61%     | ok               |
| ZEC-USD    |       64 | 44.96%   | 1528.42%           | -47.68% |     0.56 | 36.40%     | ok               |

## AAPL Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 30.25%   | 82.85%             | -21.71% |     0.63 |       68 | 53.41%     | ok               |
|          15 | 26.24%   | 82.85%             | -23.86% |     0.55 |       75 | 60.57%     | ok               |
|          30 | 20.81%   | 82.85%             | -20.65% |     0.49 |       61 | 49.25%     | ok               |
|          35 | 18.10%   | 82.85%             | -22.04% |     0.45 |       61 | 47.75%     | ok               |
|          25 | 18.29%   | 82.85%             | -20.03% |     0.44 |       67 | 51.08%     | ok               |

## AAVE-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 10.06%   | -65.80%            | -43.61% |     0.32 |       40 | 31.99%     | ok               |
|          45 | -4.67%   | -65.80%            | -49.19% |     0.15 |       44 | 27.20%     | ok               |
|          35 | -8.77%   | -65.80%            | -51.96% |     0.13 |       50 | 35.25%     | ok               |
|          15 | -52.34%  | -65.80%            | -61.76% |    -0.33 |       80 | 53.83%     | ok               |
|          50 | -33.87%  | -65.80%            | -47.39% |    -0.36 |       42 | 19.73%     | ok               |

## ABBV Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -12.55%  | 42.90%             | -28.51% |    -0.26 |       50 | 36.61%     | ok               |
|          30 | -19.64%  | 42.90%             | -30.55% |    -0.41 |       66 | 47.25%     | ok               |
|          40 | -19.75%  | 42.90%             | -26.61% |    -0.45 |       66 | 41.26%     | ok               |
|          25 | -21.44%  | 42.90%             | -31.26% |    -0.46 |       69 | 48.75%     | ok               |
|          20 | -22.04%  | 42.90%             | -30.60% |    -0.46 |       69 | 50.58%     | ok               |

## ADA-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -77.92%  | -79.32%            | -85.97% |    -0.59 |       55 | 26.82%     | ok               |
|          45 | -80.28%  | -79.32%            | -88.02% |    -0.62 |       58 | 31.61%     | ok               |
|          35 | -82.72%  | -79.32%            | -89.77% |    -0.67 |       78 | 42.34%     | ok               |
|          30 | -83.04%  | -79.32%            | -89.12% |    -0.67 |       90 | 46.93%     | ok               |
|          15 | -86.96%  | -79.32%            | -91.11% |    -0.72 |       78 | 63.41%     | ok               |

## ADBE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 1.24%    | -57.13%            | -22.53% |     0.14 |       72 | 49.08%     | ok               |
|          40 | -11.88%  | -57.13%            | -24.87% |    -0.11 |       70 | 42.10%     | ok               |
|          25 | -17.07%  | -57.13%            | -31.11% |    -0.12 |       48 | 61.56%     | ok               |
|          20 | -24.45%  | -57.13%            | -32.14% |    -0.24 |       50 | 63.89%     | ok               |
|          15 | -27.89%  | -57.13%            | -32.12% |    -0.3  |       59 | 65.72%     | ok               |

## AGG Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -6.87%   | 0.88%              | -10.02% |    -1.14 |       69 | 31.61%     | ok               |
|          20 | -8.20%   | 0.88%              | -11.27% |    -1.21 |       71 | 36.94%     | ok               |
|          50 | -5.57%   | 0.88%              | -7.92%  |    -1.25 |       46 | 16.97%     | ok               |
|          45 | -6.25%   | 0.88%              | -7.91%  |    -1.26 |       54 | 21.13%     | ok               |
|          25 | -8.37%   | 0.88%              | -11.79% |    -1.28 |       71 | 35.27%     | ok               |

## ALGO-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -50.43%  | -72.22%            | -53.13% |    -0.57 |       86 | 38.12%     | ok               |
|          15 | -61.64%  | -72.22%            | -68.50% |    -0.67 |       84 | 50.38%     | ok               |
|          25 | -61.89%  | -72.22%            | -72.48% |    -0.74 |       84 | 45.02%     | ok               |
|          20 | -65.54%  | -72.22%            | -71.20% |    -0.8  |       86 | 48.08%     | ok               |
|          50 | -45.64%  | -72.22%            | -48.43% |    -0.81 |       42 | 16.86%     | ok               |

## AMAT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -21.77%  | 168.64%            | -54.05% |    -0.07 |       68 | 61.23%     | ok               |
|          30 | -33.55%  | 168.64%            | -57.21% |    -0.29 |       71 | 52.25%     | ok               |
|          35 | -34.02%  | 168.64%            | -55.26% |    -0.32 |       73 | 49.92%     | ok               |
|          50 | -33.87%  | 168.64%            | -48.72% |    -0.36 |       52 | 37.77%     | ok               |
|          20 | -41.18%  | 168.64%            | -60.16% |    -0.4  |       74 | 57.57%     | ok               |

## AMD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 6.74%    | 180.85%            | -44.26% |     0.27 |       54 | 30.62%     | ok               |
|          40 | 5.86%    | 180.85%            | -43.98% |     0.27 |       52 | 35.77%     | ok               |
|          35 | -5.47%   | 180.85%            | -50.71% |     0.16 |       60 | 37.27%     | ok               |
|          45 | -14.79%  | 180.85%            | -53.24% |     0.04 |       60 | 33.44%     | ok               |
|          30 | -17.93%  | 180.85%            | -56.46% |     0.02 |       61 | 39.77%     | ok               |

## AMGN Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -9.83%   | 26.67%             | -26.64% |    -0.12 |       71 | 52.41%     | ok               |
|          35 | -11.27%  | 26.67%             | -31.23% |    -0.18 |       65 | 42.43%     | ok               |
|          15 | -13.63%  | 26.67%             | -27.92% |    -0.2  |       67 | 57.90%     | ok               |
|          30 | -15.41%  | 26.67%             | -34.14% |    -0.29 |       69 | 46.26%     | ok               |
|          25 | -18.85%  | 26.67%             | -33.41% |    -0.37 |       65 | 48.59%     | ok               |

## AMZN Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -18.21%  | 41.28%             | -27.15% |    -0.54 |       52 | 29.12%     | ok               |
|          50 | -24.52%  | 41.28%             | -34.08% |    -0.88 |       50 | 23.13%     | ok               |
|          45 | -27.30%  | 41.28%             | -34.08% |    -0.97 |       54 | 26.12%     | ok               |
|          35 | -31.66%  | 41.28%             | -38.29% |    -1    |       68 | 32.78%     | ok               |
|          30 | -37.74%  | 41.28%             | -42.48% |    -1.14 |       80 | 38.27%     | ok               |

## APT-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 19.10%   | -90.30%            | -46.73% |     0.42 |       40 | 18.97%     | ok               |
|          45 | -10.39%  | -90.30%            | -63.86% |     0.07 |       58 | 24.71%     | ok               |
|          20 | -34.71%  | -90.30%            | -70.51% |    -0.1  |       71 | 50.96%     | ok               |
|          40 | -27.60%  | -90.30%            | -63.33% |    -0.12 |       64 | 30.27%     | ok               |
|          35 | -32.91%  | -90.30%            | -64.45% |    -0.16 |       68 | 36.02%     | ok               |

## ARB-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 28.81%   | -82.34%            | -53.74% |     0.49 |       87 | 57.09%     | ok               |
|          40 | 10.52%   | -82.34%            | -43.98% |     0.33 |       52 | 30.46%     | ok               |
|          20 | -3.20%   | -82.34%            | -60.40% |     0.25 |       75 | 50.57%     | ok               |
|          45 | -0.88%   | -82.34%            | -47.43% |     0.19 |       58 | 23.75%     | ok               |
|          35 | -3.41%   | -82.34%            | -54.43% |     0.19 |       64 | 33.72%     | ok               |

## ARKK Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -29.84%  | 55.34%             | -35.59% |    -0.39 |       94 | 51.08%     | ok               |
|          20 | -33.98%  | 55.34%             | -35.50% |    -0.52 |       89 | 46.42%     | ok               |
|          30 | -35.16%  | 55.34%             | -36.65% |    -0.63 |       83 | 39.60%     | ok               |
|          35 | -36.27%  | 55.34%             | -37.73% |    -0.69 |       82 | 37.27%     | ok               |
|          40 | -37.61%  | 55.34%             | -39.04% |    -0.78 |       74 | 32.45%     | ok               |

## ATOM-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -63.75%  | -70.12%            | -70.28% |    -0.94 |       93 | 51.15%     | ok               |
|          15 | -67.98%  | -70.12%            | -70.48% |    -0.98 |       95 | 61.69%     | ok               |
|          45 | -58.00%  | -70.12%            | -64.33% |    -1.08 |       72 | 28.74%     | ok               |
|          30 | -68.01%  | -70.12%            | -73.75% |    -1.16 |       88 | 44.44%     | ok               |
|          20 | -71.61%  | -70.12%            | -74.25% |    -1.16 |      101 | 54.98%     | ok               |

## AVAX-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 3.29%    | -75.00%            | -34.50% |     0.21 |       32 | 18.20%     | ok               |
|          45 | -8.08%   | -75.00%            | -41.07% |     0.04 |       34 | 21.84%     | ok               |
|          15 | -24.54%  | -75.00%            | -52.46% |    -0.03 |       73 | 53.07%     | ok               |
|          25 | -23.67%  | -75.00%            | -52.93% |    -0.07 |       71 | 42.72%     | ok               |
|          40 | -17.78%  | -75.00%            | -45.62% |    -0.09 |       40 | 24.71%     | ok               |

## AVGO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 16.61%   | 186.05%            | -35.84% |     0.36 |       56 | 30.62%     | ok               |
|          30 | 15.12%   | 186.05%            | -35.76% |     0.34 |       64 | 42.60%     | ok               |
|          40 | 13.74%   | 186.05%            | -40.70% |     0.33 |       62 | 36.44%     | ok               |
|          25 | 12.70%   | 186.05%            | -38.01% |     0.32 |       72 | 44.09%     | ok               |
|          45 | 10.69%   | 186.05%            | -41.66% |     0.29 |       58 | 34.11%     | ok               |

## BA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 26.03%   | 6.57%              | -13.34% |     0.67 |       42 | 31.45%     | ok               |
|          35 | 30.46%   | 6.57%              | -23.77% |     0.59 |       72 | 44.59%     | ok               |
|          40 | 20.11%   | 6.57%              | -23.90% |     0.47 |       46 | 38.60%     | ok               |
|          25 | 10.59%   | 6.57%              | -32.48% |     0.29 |       70 | 52.58%     | ok               |
|          30 | 7.60%    | 6.57%              | -30.56% |     0.25 |       67 | 49.25%     | ok               |

## BAC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 4.27%    | 80.63%             | -19.60% |     0.2  |       62 | 37.94%     | ok               |
|          35 | 0.30%    | 80.63%             | -27.11% |     0.08 |       70 | 45.92%     | ok               |
|          20 | -0.35%   | 80.63%             | -20.73% |     0.08 |       78 | 54.41%     | ok               |
|          50 | -1.60%   | 80.63%             | -20.35% |     0.01 |       62 | 34.78%     | ok               |
|          40 | -2.99%   | 80.63%             | -23.77% |    -0.02 |       66 | 40.93%     | ok               |

## BCH-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 7.97%    | -37.33%            | -48.11% |     0.31 |       73 | 54.41%     | ok               |
|          15 | 4.59%    | -37.33%            | -52.32% |     0.28 |       80 | 59.00%     | ok               |
|          25 | -5.48%   | -37.33%            | -54.62% |     0.16 |       72 | 50.57%     | ok               |
|          30 | -4.92%   | -37.33%            | -54.34% |     0.16 |       80 | 48.47%     | ok               |
|          35 | -18.74%  | -37.33%            | -64.08% |    -0.04 |       72 | 44.44%     | ok               |

## BITO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 22.38%   | -64.02%            | -31.98% |     0.43 |       54 | 24.63%     | ok               |
|          45 | 2.95%    | -64.02%            | -41.16% |     0.2  |       62 | 28.29%     | ok               |
|          30 | 0.48%    | -64.02%            | -42.82% |     0.18 |       80 | 41.26%     | ok               |
|          40 | -1.65%   | -64.02%            | -43.67% |     0.15 |       66 | 33.11%     | ok               |
|          15 | -6.93%   | -64.02%            | -48.38% |     0.13 |       89 | 50.25%     | ok               |

## BLK Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | -1.31%   | 31.79%             | -17.97% |     0.03 |       76 | 38.44%     | ok               |
|          20 | -3.44%   | 31.79%             | -21.48% |    -0.02 |       76 | 47.25%     | ok               |
|          40 | -4.96%   | 31.79%             | -20.08% |    -0.1  |       70 | 34.44%     | ok               |
|          30 | -7.59%   | 31.79%             | -24.29% |    -0.16 |       71 | 42.43%     | ok               |
|          25 | -8.52%   | 31.79%             | -23.36% |    -0.18 |       71 | 44.76%     | ok               |

## BND Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -6.94%   | 0.94%              | -9.41%  |    -1.01 |       65 | 38.60%     | ok               |
|          25 | -7.63%   | 0.94%              | -10.50% |    -1.17 |       69 | 36.61%     | ok               |
|          30 | -7.81%   | 0.94%              | -9.98%  |    -1.26 |       67 | 32.95%     | ok               |
|          15 | -9.13%   | 0.94%              | -11.19% |    -1.32 |       75 | 41.43%     | ok               |
|          45 | -7.70%   | 0.94%              | -9.57%  |    -1.48 |       52 | 22.80%     | ok               |

## BONK-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 169.29%  | -83.47%            | -35.57% |     1.24 |       44 | 22.03%     | ok               |
|          25 | 155.05%  | -83.47%            | -47.99% |     1    |       65 | 48.28%     | ok               |
|          20 | 140.65%  | -83.47%            | -55.43% |     0.95 |       66 | 52.87%     | ok               |
|          15 | 146.15%  | -83.47%            | -63.45% |     0.94 |       69 | 57.85%     | ok               |
|          45 | 88.02%   | -83.47%            | -42.36% |     0.85 |       56 | 26.44%     | ok               |

## BTC-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 43.79%   | -33.48%            | -15.92% |     0.81 |       46 | 34.67%     | ok               |
|          45 | 40.84%   | -33.48%            | -15.18% |     0.81 |       44 | 30.65%     | ok               |
|          35 | 26.71%   | -33.48%            | -27.54% |     0.56 |       70 | 41.57%     | ok               |
|          50 | 13.98%   | -33.48%            | -18.05% |     0.4  |       42 | 25.29%     | ok               |
|          30 | 11.49%   | -33.48%            | -21.75% |     0.33 |       74 | 48.28%     | ok               |

## C Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -6.29%   | 131.29%            | -22.28% |    -0.1  |       64 | 36.11%     | ok               |
|          45 | -18.56%  | 131.29%            | -30.30% |    -0.43 |       76 | 40.27%     | ok               |
|          25 | -27.45%  | 131.29%            | -35.32% |    -0.52 |       71 | 53.08%     | ok               |
|          15 | -29.86%  | 131.29%            | -36.66% |    -0.54 |       72 | 60.07%     | ok               |
|          40 | -24.27%  | 131.29%            | -35.18% |    -0.56 |       76 | 42.60%     | ok               |

## CAT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 21.81%   | 171.79%            | -21.02% |     0.45 |       72 | 55.74%     | ok               |
|          25 | 21.92%   | 171.79%            | -26.37% |     0.45 |       68 | 58.57%     | ok               |
|          20 | 20.46%   | 171.79%            | -25.65% |     0.43 |       78 | 62.06%     | ok               |
|          45 | 16.83%   | 171.79%            | -27.12% |     0.39 |       56 | 44.43%     | ok               |
|          35 | 13.81%   | 171.79%            | -27.72% |     0.34 |       70 | 49.25%     | ok               |

## CL Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 10.26%   | 7.80%              | -11.22% |     0.45 |       44 | 29.62%     | ok               |
|          30 | 7.60%    | 7.80%              | -14.32% |     0.3  |       62 | 45.76%     | ok               |
|          45 | 3.13%    | 7.80%              | -13.51% |     0.17 |       48 | 32.78%     | ok               |
|          35 | 2.48%    | 7.80%              | -13.83% |     0.14 |       64 | 42.10%     | ok               |
|          40 | -0.49%   | 7.80%              | -12.70% |     0.04 |       58 | 36.77%     | ok               |

## CMCSA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -38.85%  | -39.42%            | -44.02% |    -0.88 |       90 | 57.24%     | ok               |
|          30 | -41.17%  | -39.42%            | -41.04% |    -1.1  |       82 | 42.26%     | ok               |
|          25 | -44.21%  | -39.42%            | -43.86% |    -1.19 |       90 | 47.59%     | ok               |
|          50 | -31.59%  | -39.42%            | -32.82% |    -1.26 |       50 | 14.48%     | ok               |
|          20 | -49.35%  | -39.42%            | -49.03% |    -1.34 |       95 | 53.24%     | ok               |

## COMP-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -4.94%   | -71.27%            | -38.71% |     0.13 |       44 | 20.11%     | ok               |
|          30 | -42.10%  | -71.27%            | -57.88% |    -0.3  |       89 | 45.59%     | ok               |
|          25 | -45.12%  | -71.27%            | -61.30% |    -0.31 |       89 | 52.11%     | ok               |
|          15 | -52.88%  | -71.27%            | -66.20% |    -0.4  |      107 | 63.79%     | ok               |
|          40 | -43.93%  | -71.27%            | -50.01% |    -0.43 |       72 | 33.72%     | ok               |

## COP Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -5.37%   | 2.87%              | -35.08% |    -0.04 |       48 | 27.79%     | ok               |
|          35 | -18.05%  | 2.87%              | -43.58% |    -0.3  |       73 | 38.44%     | ok               |
|          45 | -16.54%  | 2.87%              | -41.35% |    -0.31 |       62 | 31.11%     | ok               |
|          30 | -22.31%  | 2.87%              | -43.96% |    -0.39 |       72 | 41.93%     | ok               |
|          40 | -21.81%  | 2.87%              | -47.05% |    -0.44 |       68 | 34.28%     | ok               |

## COST Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 9.68%    | 27.50%             | -24.32% |     0.33 |       66 | 49.92%     | ok               |
|          25 | 8.06%    | 27.50%             | -24.73% |     0.3  |       63 | 47.09%     | ok               |
|          35 | 3.04%    | 27.50%             | -26.58% |     0.16 |       54 | 40.43%     | ok               |
|          30 | -1.68%   | 27.50%             | -29.73% |     0.02 |       60 | 43.43%     | ok               |
|          15 | -4.64%   | 27.50%             | -27.30% |    -0.04 |       69 | 53.41%     | ok               |

## CRM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -35.79%  | -41.68%            | -44.67% |    -0.57 |       90 | 54.91%     | ok               |
|          35 | -29.63%  | -41.68%            | -33.08% |    -0.59 |       60 | 37.94%     | ok               |
|          40 | -34.83%  | -41.68%            | -39.11% |    -0.8  |       66 | 33.94%     | ok               |
|          20 | -43.35%  | -41.68%            | -45.69% |    -0.82 |       74 | 48.59%     | ok               |
|          30 | -39.56%  | -41.68%            | -41.36% |    -0.83 |       63 | 42.76%     | ok               |

## CRV-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 17.80%   | -60.22%            | -37.78% |     0.4  |       70 | 31.61%     | ok               |
|          45 | 3.36%    | -60.22%            | -42.29% |     0.24 |       56 | 20.88%     | ok               |
|          40 | -2.40%   | -60.22%            | -38.86% |     0.18 |       60 | 27.20%     | ok               |
|          50 | -0.89%   | -60.22%            | -29.30% |     0.18 |       46 | 17.43%     | ok               |
|          30 | -6.45%   | -60.22%            | -39.89% |     0.17 |       68 | 36.21%     | ok               |

## CSCO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 34.29%   | 129.10%            | -19.34% |     0.74 |       50 | 37.60%     | ok               |
|          45 | 29.75%   | 129.10%            | -19.34% |     0.65 |       51 | 39.27%     | ok               |
|          35 | 25.89%   | 129.10%            | -23.68% |     0.55 |       53 | 46.26%     | ok               |
|          25 | 24.20%   | 129.10%            | -23.28% |     0.52 |       65 | 50.92%     | ok               |
|          30 | 23.62%   | 129.10%            | -21.79% |     0.52 |       61 | 48.92%     | ok               |

## CVX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -12.14%  | 21.16%             | -24.33% |    -0.26 |       75 | 42.60%     | ok               |
|          40 | -10.65%  | 21.16%             | -27.34% |    -0.26 |       77 | 34.78%     | ok               |
|          35 | -12.09%  | 21.16%             | -28.85% |    -0.29 |       69 | 37.10%     | ok               |
|          45 | -11.82%  | 21.16%             | -28.83% |    -0.31 |       67 | 30.95%     | ok               |
|          30 | -15.68%  | 21.16%             | -29.13% |    -0.39 |       75 | 39.93%     | ok               |

## DASH-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 105.37%  | 22.79%             | -25.18% |     0.87 |       38 | 14.94%     | ok               |
|          40 | 64.68%   | 22.79%             | -28.66% |     0.67 |       46 | 21.65%     | ok               |
|          45 | 48.07%   | 22.79%             | -34.23% |     0.58 |       42 | 17.05%     | ok               |
|          35 | -38.60%  | 22.79%             | -63.23% |     0.01 |       67 | 26.25%     | ok               |
|          25 | -42.25%  | 22.79%             | -64.14% |    -0.02 |       69 | 31.80%     | ok               |

## DBC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -6.60%   | 33.30%             | -27.14% |    -0.17 |       75 | 39.10%     | ok               |
|          50 | -6.51%   | 33.30%             | -20.31% |    -0.23 |       42 | 21.63%     | ok               |
|          35 | -9.06%   | 33.30%             | -23.91% |    -0.28 |       64 | 32.28%     | ok               |
|          25 | -9.51%   | 33.30%             | -26.10% |    -0.29 |       64 | 35.44%     | ok               |
|          45 | -9.10%   | 33.30%             | -21.46% |    -0.31 |       58 | 25.29%     | ok               |

## DE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -4.54%   | 63.78%             | -28.94% |     0.01 |       74 | 52.75%     | ok               |
|          25 | -6.91%   | 63.78%             | -26.67% |    -0.05 |       76 | 50.08%     | ok               |
|          30 | -6.93%   | 63.78%             | -25.24% |    -0.05 |       74 | 47.25%     | ok               |
|          50 | -6.83%   | 63.78%             | -24.35% |    -0.1  |       72 | 31.78%     | ok               |
|          45 | -8.69%   | 63.78%             | -27.91% |    -0.13 |       70 | 36.27%     | ok               |

## DIA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | -2.35%   | 33.10%             | -13.15% |    -0.1  |       62 | 41.93%     | ok               |
|          25 | -2.88%   | 33.10%             | -11.28% |    -0.12 |       62 | 45.26%     | ok               |
|          30 | -4.38%   | 33.10%             | -12.94% |    -0.21 |       62 | 44.09%     | ok               |
|          20 | -6.20%   | 33.10%             | -13.85% |    -0.29 |       66 | 47.59%     | ok               |
|          40 | -6.33%   | 33.10%             | -15.06% |    -0.34 |       68 | 39.10%     | ok               |

## DIS Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 19.96%   | -9.35%             | -14.24% |     0.62 |       48 | 27.45%     | ok               |
|          45 | -5.04%   | -9.35%             | -16.54% |    -0.04 |       49 | 31.11%     | ok               |
|          40 | -6.54%   | -9.35%             | -23.29% |    -0.06 |       63 | 36.27%     | ok               |
|          15 | -17.04%  | -9.35%             | -31.15% |    -0.24 |       88 | 57.07%     | ok               |
|          35 | -15.88%  | -9.35%             | -25.70% |    -0.28 |       73 | 42.26%     | ok               |

## DOGE-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 8.84%    | -73.29%            | -57.89% |     0.36 |       79 | 66.09%     | ok               |
|          20 | -6.28%   | -73.29%            | -55.83% |     0.22 |       78 | 60.54%     | ok               |
|          25 | -7.14%   | -73.29%            | -53.72% |     0.2  |       68 | 55.56%     | ok               |
|          30 | -22.30%  | -73.29%            | -60.95% |     0.02 |       71 | 50.00%     | ok               |
|          35 | -49.12%  | -73.29%            | -63.16% |    -0.45 |       68 | 43.30%     | ok               |

## DOT-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -35.77%  | -84.27%            | -47.42% |    -0.47 |       56 | 25.48%     | ok               |
|          45 | -38.61%  | -84.27%            | -50.71% |    -0.48 |       50 | 30.65%     | ok               |
|          35 | -52.94%  | -84.27%            | -60.35% |    -0.53 |       74 | 41.19%     | ok               |
|          40 | -44.80%  | -84.27%            | -52.42% |    -0.57 |       54 | 33.72%     | ok               |
|          30 | -56.50%  | -84.27%            | -63.10% |    -0.58 |       86 | 47.70%     | ok               |

## DXY-INDEX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -1.53%   | 0.15%              | -6.02%  |    -0.23 |       40 | 30.87%     | ok               |
|          15 | -4.09%   | 0.15%              | -11.37% |    -0.36 |       82 | 76.96%     | ok               |
|          40 | -5.28%   | 0.15%              | -8.08%  |    -0.67 |       72 | 50.65%     | ok               |
|          25 | -6.91%   | 0.15%              | -12.10% |    -0.75 |       80 | 66.96%     | ok               |
|          35 | -6.24%   | 0.15%              | -10.39% |    -0.76 |       71 | 57.17%     | ok               |

## EEM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -6.04%   | 55.89%             | -19.52% |    -0.15 |       64 | 39.27%     | ok               |
|          35 | -6.69%   | 55.89%             | -23.88% |    -0.16 |       66 | 41.26%     | ok               |
|          50 | -6.02%   | 55.89%             | -15.88% |    -0.16 |       52 | 35.27%     | ok               |
|          45 | -7.10%   | 55.89%             | -17.36% |    -0.2  |       54 | 36.94%     | ok               |
|          30 | -10.42%  | 55.89%             | -25.67% |    -0.28 |       64 | 42.93%     | ok               |

## EFA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -3.05%   | 33.50%             | -10.80% |    -0.05 |       62 | 52.41%     | ok               |
|          20 | -9.78%   | 33.50%             | -12.73% |    -0.34 |       69 | 49.42%     | ok               |
|          30 | -9.68%   | 33.50%             | -15.14% |    -0.36 |       62 | 44.76%     | ok               |
|          50 | -9.07%   | 33.50%             | -17.56% |    -0.4  |       54 | 36.27%     | ok               |
|          25 | -11.91%  | 33.50%             | -16.37% |    -0.45 |       64 | 46.76%     | ok               |

## EOG Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -17.34%  | 25.06%             | -39.69% |    -0.38 |       58 | 33.44%     | ok               |
|          30 | -22.13%  | 25.06%             | -48.13% |    -0.45 |       81 | 47.25%     | ok               |
|          40 | -22.23%  | 25.06%             | -43.26% |    -0.51 |       66 | 36.77%     | ok               |
|          35 | -22.99%  | 25.06%             | -46.26% |    -0.51 |       79 | 41.93%     | ok               |
|          25 | -26.09%  | 25.06%             | -51.99% |    -0.53 |       82 | 50.25%     | ok               |

## ETC-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 1.95%    | -67.70%            | -27.89% |     0.16 |       24 | 15.71%     | ok               |
|          35 | -7.23%   | -67.70%            | -42.62% |     0.03 |       44 | 25.48%     | ok               |
|          45 | -8.31%   | -67.70%            | -35.44% |    -0.02 |       24 | 17.43%     | ok               |
|          40 | -13.75%  | -67.70%            | -40.48% |    -0.12 |       40 | 21.26%     | ok               |
|          30 | -29.79%  | -67.70%            | -45.98% |    -0.38 |       64 | 29.69%     | ok               |

## ETH-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 144.88%  | -31.08%            | -30.11% |     1.22 |       64 | 44.83%     | ok               |
|          30 | 110.13%  | -31.08%            | -32.89% |     1.02 |       70 | 53.26%     | ok               |
|          40 | 40.52%   | -31.08%            | -33.11% |     0.62 |       62 | 36.97%     | ok               |
|          15 | 44.09%   | -31.08%            | -42.74% |     0.6  |       77 | 68.77%     | ok               |
|          20 | 42.87%   | -31.08%            | -39.10% |     0.6  |       84 | 62.84%     | ok               |

## EWJ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -19.61%  | 31.13%             | -30.73% |    -0.65 |       62 | 38.77%     | ok               |
|          20 | -20.97%  | 31.13%             | -31.32% |    -0.68 |       58 | 40.77%     | ok               |
|          25 | -23.25%  | 31.13%             | -31.18% |    -0.78 |       58 | 39.77%     | ok               |
|          45 | -20.38%  | 31.13%             | -27.68% |    -0.79 |       58 | 30.95%     | ok               |
|          35 | -23.46%  | 31.13%             | -32.54% |    -0.81 |       68 | 37.10%     | ok               |

## FCX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -3.35%   | 49.85%             | -26.97% |     0.08 |       52 | 29.62%     | ok               |
|          45 | -7.51%   | 49.85%             | -34.52% |     0.01 |       52 | 34.11%     | ok               |
|          40 | -19.35%  | 49.85%             | -43.57% |    -0.19 |       62 | 38.60%     | ok               |
|          30 | -27.81%  | 49.85%             | -47.47% |    -0.31 |       63 | 45.26%     | ok               |
|          35 | -32.25%  | 49.85%             | -50.71% |    -0.42 |       69 | 43.43%     | ok               |

## FET-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 1.55%    | -81.38%            | -59.54% |     0.32 |       88 | 52.87%     | ok               |
|          15 | -13.62%  | -81.38%            | -59.58% |     0.21 |       84 | 56.70%     | ok               |
|          25 | -33.56%  | -81.38%            | -60.09% |    -0.04 |       91 | 46.55%     | ok               |
|          30 | -37.15%  | -81.38%            | -54.02% |    -0.11 |       85 | 42.15%     | ok               |
|          35 | -53.10%  | -81.38%            | -62.73% |    -0.49 |       71 | 33.91%     | ok               |

## FIL-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -23.47%  | -79.61%            | -39.40% |    -0.21 |       46 | 22.80%     | ok               |
|          35 | -43.13%  | -79.61%            | -47.50% |    -0.57 |       58 | 27.01%     | ok               |
|          30 | -45.82%  | -79.61%            | -50.22% |    -0.58 |       70 | 32.57%     | ok               |
|          45 | -41.18%  | -79.61%            | -43.98% |    -0.65 |       40 | 17.05%     | ok               |
|          50 | -39.00%  | -79.61%            | -44.95% |    -0.69 |       36 | 12.64%     | ok               |

## FXI Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -6.30%   | 41.50%             | -22.57% |    -0.07 |       44 | 31.28%     | ok               |
|          30 | -6.84%   | 41.50%             | -23.91% |    -0.09 |       44 | 30.12%     | ok               |
|          45 | -6.49%   | 41.50%             | -26.75% |    -0.09 |       44 | 24.63%     | ok               |
|          15 | -10.08%  | 41.50%             | -21.68% |    -0.15 |       54 | 34.94%     | ok               |
|          50 | -9.19%   | 41.50%             | -24.76% |    -0.18 |       44 | 21.63%     | ok               |

## GDX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 18.06%   | 167.52%            | -35.59% |     0.39 |       73 | 52.91%     | ok               |
|          40 | 13.85%   | 167.52%            | -31.87% |     0.35 |       64 | 42.93%     | ok               |
|          30 | 11.28%   | 167.52%            | -34.99% |     0.3  |       60 | 48.09%     | ok               |
|          35 | 8.95%    | 167.52%            | -32.37% |     0.27 |       68 | 45.26%     | ok               |
|          25 | 6.77%    | 167.52%            | -38.90% |     0.24 |       63 | 49.75%     | ok               |

## GDXJ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -7.64%   | 185.27%            | -45.05% |     0.06 |       67 | 52.91%     | ok               |
|          30 | -22.87%  | 185.27%            | -44.93% |    -0.21 |       66 | 46.09%     | ok               |
|          50 | -20.22%  | 185.27%            | -44.94% |    -0.22 |       58 | 37.77%     | ok               |
|          25 | -26.29%  | 185.27%            | -47.26% |    -0.24 |       70 | 49.58%     | ok               |
|          35 | -26.51%  | 185.27%            | -43.49% |    -0.29 |       68 | 43.76%     | ok               |

## GE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 28.70%   | 185.06%            | -22.29% |     0.59 |       66 | 39.60%     | ok               |
|          45 | 18.98%   | 185.06%            | -25.68% |     0.44 |       74 | 42.43%     | ok               |
|          20 | 12.72%   | 185.06%            | -26.63% |     0.32 |       71 | 56.74%     | ok               |
|          35 | 11.71%   | 185.06%            | -27.11% |     0.31 |       80 | 47.75%     | ok               |
|          30 | 11.46%   | 185.06%            | -27.82% |     0.31 |       76 | 52.91%     | ok               |

## GLD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 32.71%   | 95.32%             | -14.61% |     0.77 |       48 | 50.42%     | ok               |
|          25 | 32.02%   | 95.32%             | -14.61% |     0.76 |       48 | 48.92%     | ok               |
|          30 | 25.73%   | 95.32%             | -16.63% |     0.65 |       50 | 47.75%     | ok               |
|          15 | 24.58%   | 95.32%             | -17.54% |     0.59 |       50 | 54.58%     | ok               |
|          35 | 17.08%   | 95.32%             | -17.29% |     0.48 |       54 | 46.09%     | ok               |

## GOOGL Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 80.35%   | 140.88%            | -19.12% |     1.22 |       63 | 48.42%     | ok               |
|          25 | 81.59%   | 140.88%            | -19.76% |     1.19 |       55 | 55.41%     | ok               |
|          30 | 79.31%   | 140.88%            | -20.41% |     1.18 |       59 | 53.08%     | ok               |
|          45 | 64.33%   | 140.88%            | -15.05% |     1.11 |       56 | 41.60%     | ok               |
|          40 | 60.75%   | 140.88%            | -20.80% |     1.04 |       52 | 43.26%     | ok               |

## GRT-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 16.20%   | -88.56%            | -35.66% |     0.39 |       42 | 21.46%     | ok               |
|          45 | 2.68%    | -88.56%            | -46.59% |     0.21 |       48 | 26.82%     | ok               |
|          15 | -4.49%   | -88.56%            | -49.67% |     0.21 |       73 | 60.92%     | ok               |
|          35 | -1.50%   | -88.56%            | -48.22% |     0.18 |       58 | 35.63%     | ok               |
|          20 | -7.81%   | -88.56%            | -46.47% |     0.16 |       81 | 55.36%     | ok               |

## GS Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 21.11%   | 172.40%            | -20.56% |     0.47 |       74 | 61.06%     | ok               |
|          20 | 4.59%    | 172.40%            | -23.19% |     0.19 |       74 | 57.07%     | ok               |
|          40 | 0.08%    | 172.40%            | -17.88% |     0.09 |       72 | 45.26%     | ok               |
|          25 | -0.70%   | 172.40%            | -23.32% |     0.09 |       74 | 54.58%     | ok               |
|          30 | -2.38%   | 172.40%            | -22.13% |     0.05 |       76 | 52.08%     | ok               |

## HD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -7.53%   | -8.90%             | -17.69% |    -0.12 |       71 | 44.59%     | ok               |
|          25 | -8.25%   | -8.90%             | -18.51% |    -0.14 |       70 | 46.59%     | ok               |
|          15 | -17.75%  | -8.90%             | -27.53% |    -0.37 |      110 | 55.57%     | ok               |
|          35 | -15.13%  | -8.90%             | -22.98% |    -0.38 |       80 | 40.43%     | ok               |
|          40 | -13.89%  | -8.90%             | -19.63% |    -0.39 |       84 | 34.11%     | ok               |

## HON Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -13.43%  | 13.46%             | -21.17% |    -0.4  |       72 | 31.78%     | ok               |
|          45 | -15.16%  | 13.46%             | -19.99% |    -0.43 |       74 | 36.77%     | ok               |
|          40 | -23.52%  | 13.46%             | -26.29% |    -0.66 |       76 | 41.10%     | ok               |
|          35 | -24.98%  | 13.46%             | -27.37% |    -0.69 |       91 | 47.42%     | ok               |
|          30 | -26.82%  | 13.46%             | -29.80% |    -0.72 |       93 | 52.41%     | ok               |

## HYG Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -7.98%   | 2.97%              | -7.98%  |    -0.96 |       70 | 29.28%     | ok               |
|          15 | -9.49%   | 2.97%              | -10.34% |    -1.03 |       88 | 40.93%     | ok               |
|          20 | -9.23%   | 2.97%              | -10.34% |    -1.03 |       86 | 38.77%     | ok               |
|          25 | -9.38%   | 2.97%              | -10.11% |    -1.06 |       83 | 36.61%     | ok               |
|          30 | -9.08%   | 2.97%              | -9.59%  |    -1.06 |       81 | 33.94%     | ok               |

## IBIT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 53.73%   | -4.37%             | -17.37% |     1.06 |       22 | 22.27%     | ok               |
|          15 | 56.91%   | -4.37%             | -19.20% |     0.95 |       40 | 39.68%     | ok               |
|          45 | 44.27%   | -4.37%             | -17.37% |     0.9  |       26 | 23.67%     | ok               |
|          40 | 38.04%   | -4.37%             | -17.78% |     0.8  |       26 | 25.52%     | ok               |
|          30 | 30.82%   | -4.37%             | -18.95% |     0.66 |       34 | 32.02%     | ok               |

## IBM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -9.66%   | 14.51%             | -43.33% |     0.01 |       93 | 61.90%     | ok               |
|          30 | -17.78%  | 14.51%             | -44.74% |    -0.16 |       77 | 49.75%     | ok               |
|          20 | -21.40%  | 14.51%             | -48.00% |    -0.2  |       75 | 54.41%     | ok               |
|          35 | -19.90%  | 14.51%             | -44.74% |    -0.21 |       71 | 45.42%     | ok               |
|          25 | -28.67%  | 14.51%             | -51.09% |    -0.36 |       74 | 52.41%     | ok               |

## ICP-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 1.02%    | -70.34%            | -32.85% |     0.21 |       50 | 23.75%     | ok               |
|          35 | -4.60%   | -70.34%            | -39.08% |     0.16 |       58 | 28.54%     | ok               |
|          30 | -14.10%  | -70.34%            | -52.78% |     0.11 |       77 | 34.87%     | ok               |
|          50 | -18.12%  | -70.34%            | -43.65% |    -0.09 |       32 | 14.18%     | ok               |
|          45 | -24.62%  | -70.34%            | -40.57% |    -0.18 |       52 | 18.01%     | ok               |

## IEF Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -7.38%   | -0.21%             | -10.09% |    -0.88 |       72 | 42.26%     | ok               |
|          15 | -7.93%   | -0.21%             | -10.82% |    -0.94 |       71 | 43.76%     | ok               |
|          40 | -8.54%   | -0.21%             | -9.67%  |    -1.33 |       62 | 24.96%     | ok               |
|          45 | -8.22%   | -0.21%             | -9.73%  |    -1.35 |       52 | 22.96%     | ok               |
|          25 | -10.94%  | -0.21%             | -11.49% |    -1.4  |       78 | 39.43%     | ok               |

## IEMG Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -2.21%   | 50.79%             | -13.91% |    -0.03 |       52 | 33.44%     | ok               |
|          45 | -3.01%   | 50.79%             | -14.92% |    -0.06 |       48 | 35.94%     | ok               |
|          35 | -3.88%   | 50.79%             | -22.13% |    -0.07 |       63 | 41.43%     | ok               |
|          40 | -4.51%   | 50.79%             | -18.43% |    -0.11 |       60 | 38.94%     | ok               |
|          25 | -8.11%   | 50.79%             | -25.58% |    -0.21 |       59 | 44.26%     | ok               |

## INJ-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -12.91%  | -66.53%            | -55.31% |     0.02 |       44 | 22.41%     | ok               |
|          35 | -20.16%  | -66.53%            | -61.19% |    -0.01 |       60 | 32.38%     | ok               |
|          50 | -22.38%  | -66.53%            | -51.00% |    -0.14 |       48 | 19.35%     | ok               |
|          40 | -28.35%  | -66.53%            | -58.05% |    -0.17 |       50 | 28.54%     | ok               |
|          20 | -56.26%  | -66.53%            | -81.53% |    -0.46 |       82 | 47.13%     | ok               |

## INTC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 104.23%  | 121.07%            | -53.65% |     0.83 |       81 | 59.73%     | ok               |
|          20 | 90.69%   | 121.07%            | -52.47% |     0.78 |       80 | 55.91%     | ok               |
|          45 | 80.47%   | 121.07%            | -49.32% |     0.77 |       58 | 34.11%     | ok               |
|          25 | 83.39%   | 121.07%            | -56.41% |     0.75 |       75 | 51.58%     | ok               |
|          40 | 74.55%   | 121.07%            | -55.86% |     0.72 |       66 | 38.44%     | ok               |

## INTU Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -0.28%   | -55.88%            | -40.73% |     0.11 |       69 | 27.95%     | ok               |
|          45 | -2.22%   | -55.88%            | -41.76% |     0.08 |       67 | 31.95%     | ok               |
|          40 | -8.64%   | -55.88%            | -45.15% |    -0.04 |       67 | 34.94%     | ok               |
|          35 | -15.62%  | -55.88%            | -46.75% |    -0.16 |       71 | 38.44%     | ok               |
|          25 | -18.48%  | -55.88%            | -39.87% |    -0.2  |       68 | 44.26%     | ok               |

## ITA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 0.46%    | 82.51%             | -21.48% |     0.08 |       76 | 38.27%     | ok               |
|          15 | -0.83%   | 82.51%             | -26.46% |     0.07 |       87 | 60.07%     | ok               |
|          30 | -3.02%   | 82.51%             | -23.75% |    -0.01 |       72 | 48.25%     | ok               |
|          35 | -5.09%   | 82.51%             | -23.16% |    -0.08 |       76 | 46.59%     | ok               |
|          40 | -6.18%   | 82.51%             | -20.58% |    -0.12 |       78 | 43.09%     | ok               |

## IWM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 8.60%    | 47.10%             | -14.08% |     0.39 |       42 | 31.28%     | ok               |
|          30 | 9.40%    | 47.10%             | -12.83% |     0.39 |       48 | 35.77%     | ok               |
|          25 | 9.50%    | 47.10%             | -13.55% |     0.39 |       50 | 36.94%     | ok               |
|          35 | 8.35%    | 47.10%             | -14.11% |     0.36 |       48 | 33.61%     | ok               |
|          20 | 5.19%    | 47.10%             | -14.08% |     0.24 |       60 | 37.94%     | ok               |

## JNJ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 19.24%   | 56.35%             | -10.57% |     0.79 |       56 | 37.60%     | ok               |
|          15 | 15.64%   | 56.35%             | -18.02% |     0.53 |       62 | 57.74%     | ok               |
|          45 | 10.73%   | 56.35%             | -13.35% |     0.46 |       56 | 42.43%     | ok               |
|          20 | 10.33%   | 56.35%             | -17.61% |     0.39 |       66 | 54.24%     | ok               |
|          25 | 6.96%    | 56.35%             | -17.84% |     0.29 |       65 | 52.75%     | ok               |

## JPM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 13.59%   | 85.39%             | -15.90% |     0.48 |       54 | 40.60%     | ok               |
|          45 | 2.80%    | 85.39%             | -21.91% |     0.15 |       56 | 43.59%     | ok               |
|          20 | -14.15%  | 85.39%             | -33.59% |    -0.23 |       86 | 58.57%     | ok               |
|          40 | -11.28%  | 85.39%             | -28.47% |    -0.26 |       68 | 46.26%     | ok               |
|          35 | -16.52%  | 85.39%             | -27.43% |    -0.4  |       76 | 50.25%     | ok               |

## KO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 23.79%   | 33.27%             | -8.18%  |     0.86 |       51 | 37.94%     | ok               |
|          35 | 20.00%   | 33.27%             | -8.07%  |     0.75 |       54 | 36.61%     | ok               |
|          40 | 17.49%   | 33.27%             | -9.28%  |     0.71 |       56 | 33.44%     | ok               |
|          25 | 18.68%   | 33.27%             | -9.70%  |     0.69 |       57 | 40.60%     | ok               |
|          50 | 10.23%   | 33.27%             | -12.28% |     0.48 |       38 | 26.96%     | ok               |

## LDO-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 47.45%   | -81.08%            | -46.95% |     0.61 |       83 | 53.83%     | ok               |
|          50 | 27.44%   | -81.08%            | -48.04% |     0.51 |       50 | 17.82%     | ok               |
|          20 | 28.00%   | -81.08%            | -47.34% |     0.5  |       85 | 49.43%     | ok               |
|          30 | 9.45%    | -81.08%            | -62.63% |     0.35 |       78 | 40.42%     | ok               |
|          35 | 6.94%    | -81.08%            | -64.26% |     0.32 |       78 | 33.52%     | ok               |

## LIN Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -0.74%   | 14.67%             | -23.68% |     0.04 |       64 | 49.75%     | ok               |
|          25 | -1.02%   | 14.67%             | -22.01% |     0.03 |       63 | 41.76%     | ok               |
|          20 | -3.14%   | 14.67%             | -23.00% |    -0.04 |       62 | 44.93%     | ok               |
|          35 | -4.59%   | 14.67%             | -21.18% |    -0.12 |       62 | 32.45%     | ok               |
|          30 | -5.20%   | 14.67%             | -21.53% |    -0.13 |       66 | 38.94%     | ok               |

## LINK-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -15.44%  | -56.43%            | -49.35% |     0.08 |       75 | 42.91%     | ok               |
|          45 | -12.15%  | -56.43%            | -38.11% |     0.06 |       52 | 27.39%     | ok               |
|          50 | -11.72%  | -56.43%            | -36.52% |     0.05 |       42 | 22.03%     | ok               |
|          35 | -23.34%  | -56.43%            | -49.18% |    -0.04 |       61 | 37.55%     | ok               |
|          40 | -27.55%  | -56.43%            | -50.55% |    -0.13 |       57 | 31.80%     | ok               |

## LLY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 5.05%    | 53.22%             | -38.23% |     0.21 |       46 | 36.61%     | ok               |
|          15 | -4.28%   | 53.22%             | -48.12% |     0.08 |       63 | 60.07%     | ok               |
|          45 | -6.77%   | 53.22%             | -42.66% |    -0.01 |       54 | 40.10%     | ok               |
|          20 | -19.69%  | 53.22%             | -51.34% |    -0.21 |       72 | 55.07%     | ok               |
|          25 | -21.02%  | 53.22%             | -53.47% |    -0.24 |       68 | 52.41%     | ok               |

## LRCX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -9.55%   | 237.43%            | -60.45% |     0.09 |       83 | 54.08%     | ok               |
|          50 | -14.47%  | 237.43%            | -50.39% |    -0.03 |       80 | 35.77%     | ok               |
|          40 | -17.03%  | 237.43%            | -56.86% |    -0.04 |       72 | 41.60%     | ok               |
|          35 | -22.42%  | 237.43%            | -61.76% |    -0.11 |       80 | 43.59%     | ok               |
|          20 | -24.93%  | 237.43%            | -67.64% |    -0.13 |       87 | 49.75%     | ok               |

## LTC-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -11.98%  | -62.26%            | -44.78% |     0    |       58 | 32.18%     | ok               |
|          35 | -22.26%  | -62.26%            | -54.86% |    -0.13 |       68 | 43.30%     | ok               |
|          30 | -32.41%  | -62.26%            | -53.76% |    -0.26 |       72 | 49.81%     | ok               |
|          40 | -31.22%  | -62.26%            | -56.10% |    -0.29 |       60 | 38.51%     | ok               |
|          25 | -35.09%  | -62.26%            | -54.26% |    -0.3  |       76 | 52.30%     | ok               |

## MCD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 1.93%    | -10.09%            | -9.22%  |     0.14 |       40 | 20.80%     | ok               |
|          30 | -2.55%   | -10.09%            | -18.81% |    -0.05 |       75 | 38.10%     | ok               |
|          25 | -3.59%   | -10.09%            | -20.47% |    -0.09 |       75 | 40.77%     | ok               |
|          35 | -7.68%   | -10.09%            | -15.45% |    -0.29 |       67 | 34.44%     | ok               |
|          40 | -7.95%   | -10.09%            | -16.86% |    -0.33 |       71 | 28.79%     | ok               |

## META Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -13.30%  | 33.46%             | -31.43% |    -0.18 |       68 | 37.44%     | ok               |
|          40 | -22.83%  | 33.46%             | -36.01% |    -0.38 |       68 | 40.43%     | ok               |
|          25 | -30.45%  | 33.46%             | -41.22% |    -0.51 |       69 | 51.08%     | ok               |
|          50 | -26.53%  | 33.46%             | -34.13% |    -0.53 |       72 | 33.61%     | ok               |
|          30 | -32.31%  | 33.46%             | -40.36% |    -0.58 |       74 | 47.92%     | ok               |

## MPC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 25.37%   | 84.38%             | -23.96% |     0.55 |       52 | 37.60%     | ok               |
|          45 | 17.42%   | 84.38%             | -25.09% |     0.42 |       58 | 41.26%     | ok               |
|          40 | 15.64%   | 84.38%             | -25.70% |     0.38 |       60 | 43.59%     | ok               |
|          35 | 12.06%   | 84.38%             | -35.90% |     0.32 |       68 | 46.09%     | ok               |
|          30 | -5.56%   | 84.38%             | -44.76% |     0.02 |       71 | 48.92%     | ok               |

## MRK Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -20.60%  | -1.51%             | -30.12% |    -0.37 |       89 | 55.24%     | ok               |
|          25 | -20.22%  | -1.51%             | -31.07% |    -0.4  |       74 | 47.25%     | ok               |
|          20 | -24.13%  | -1.51%             | -29.59% |    -0.5  |       79 | 50.58%     | ok               |
|          45 | -24.86%  | -1.51%             | -27.72% |    -0.67 |       61 | 33.28%     | ok               |
|          35 | -28.73%  | -1.51%             | -35.44% |    -0.69 |       69 | 40.77%     | ok               |

## MS Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -3.32%   | 148.99%            | -19.99% |     0    |       72 | 41.43%     | ok               |
|          15 | -4.98%   | 148.99%            | -22.02% |    -0.01 |       73 | 58.24%     | ok               |
|          20 | -5.09%   | 148.99%            | -25.68% |    -0.02 |       77 | 54.41%     | ok               |
|          30 | -10.18%  | 148.99%            | -27.79% |    -0.16 |       77 | 49.58%     | ok               |
|          35 | -10.11%  | 148.99%            | -25.26% |    -0.17 |       78 | 46.09%     | ok               |

## MSFT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -21.88%  | -4.03%             | -25.26% |    -0.61 |       66 | 33.94%     | ok               |
|          50 | -23.26%  | -4.03%             | -26.14% |    -0.68 |       60 | 28.95%     | ok               |
|          35 | -34.27%  | -4.03%             | -35.38% |    -0.92 |       73 | 42.60%     | ok               |
|          40 | -33.64%  | -4.03%             | -34.77% |    -0.94 |       69 | 37.44%     | ok               |
|          30 | -38.11%  | -4.03%             | -39.15% |    -1.01 |       83 | 47.25%     | ok               |

## MU Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 443.43%  | 887.15%            | -61.96% |     1.58 |       45 | 67.05%     | ok               |
|          25 | 356.63%  | 887.15%            | -67.90% |     1.51 |       47 | 61.40%     | ok               |
|          20 | 312.97%  | 887.15%            | -67.25% |     1.4  |       51 | 63.06%     | ok               |
|          40 | 290.77%  | 887.15%            | -64.07% |     1.4  |       56 | 55.24%     | ok               |
|          30 | 270.03%  | 887.15%            | -68.76% |     1.34 |       49 | 59.73%     | ok               |

## NEAR-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 63.49%   | -45.81%            | -48.01% |     0.77 |       40 | 22.61%     | ok               |
|          50 | 37.56%   | -45.81%            | -53.13% |     0.58 |       34 | 17.62%     | ok               |
|          40 | 36.82%   | -45.81%            | -56.35% |     0.56 |       44 | 26.82%     | ok               |
|          35 | 14.20%   | -45.81%            | -60.30% |     0.37 |       68 | 32.38%     | ok               |
|          15 | -4.09%   | -45.81%            | -54.94% |     0.26 |       87 | 55.36%     | ok               |

## NEM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 3.24%    | 186.76%            | -29.41% |     0.21 |       62 | 61.40%     | ok               |
|          20 | -7.81%   | 186.76%            | -30.47% |     0.07 |       72 | 56.91%     | ok               |
|          25 | -21.27%  | 186.76%            | -37.89% |    -0.14 |       68 | 54.74%     | ok               |
|          50 | -25.02%  | 186.76%            | -33.36% |    -0.27 |       58 | 40.43%     | ok               |
|          30 | -31.13%  | 186.76%            | -38.49% |    -0.33 |       72 | 53.08%     | ok               |

## NFLX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 47.95%   | 18.15%             | -11.94% |     1    |       46 | 45.59%     | ok               |
|          50 | 41.64%   | 18.15%             | -16.28% |     0.96 |       46 | 38.10%     | ok               |
|          35 | 40.34%   | 18.15%             | -18.30% |     0.84 |       60 | 49.08%     | ok               |
|          45 | 31.95%   | 18.15%             | -15.48% |     0.75 |       52 | 41.93%     | ok               |
|          15 | 38.04%   | 18.15%             | -26.59% |     0.72 |       67 | 64.89%     | ok               |

## NKE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -33.86%  | -58.57%            | -50.44% |    -0.42 |       93 | 52.58%     | ok               |
|          40 | -26.46%  | -58.57%            | -31.19% |    -0.5  |       63 | 30.12%     | ok               |
|          15 | -38.38%  | -58.57%            | -55.52% |    -0.51 |       91 | 56.91%     | ok               |
|          25 | -45.09%  | -58.57%            | -52.84% |    -0.79 |       91 | 48.59%     | ok               |
|          35 | -39.10%  | -58.57%            | -43.08% |    -0.8  |       75 | 37.10%     | ok               |

## NOW Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 9.89%    | -33.05%            | -26.36% |     0.29 |       77 | 51.91%     | ok               |
|          30 | 6.39%    | -33.05%            | -27.34% |     0.24 |       80 | 45.76%     | ok               |
|          15 | 1.14%    | -33.05%            | -26.77% |     0.19 |       88 | 54.91%     | ok               |
|          25 | -0.07%   | -33.05%            | -27.28% |     0.17 |       72 | 49.25%     | ok               |
|          40 | -0.36%   | -33.05%            | -30.87% |     0.13 |       68 | 34.78%     | ok               |

## NVDA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -9.57%   | 155.05%            | -35.26% |     0.01 |       76 | 48.48%     | ok               |
|          20 | -14.84%  | 155.05%            | -40.59% |    -0.03 |       72 | 56.51%     | ok               |
|          25 | -14.70%  | 155.05%            | -33.22% |    -0.04 |       73 | 51.52%     | ok               |
|          50 | -18.23%  | 155.05%            | -40.84% |    -0.18 |       58 | 32.44%     | ok               |
|          15 | -26.92%  | 155.05%            | -45.02% |    -0.19 |       75 | 59.89%     | ok               |

## OP-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 27.06%   | -91.81%            | -36.11% |     0.51 |       30 | 11.11%     | ok               |
|          45 | 26.15%   | -91.81%            | -45.76% |     0.48 |       32 | 15.71%     | ok               |
|          40 | 3.68%    | -91.81%            | -53.61% |     0.25 |       48 | 24.33%     | ok               |
|          35 | -20.77%  | -91.81%            | -59.75% |    -0.04 |       58 | 27.59%     | ok               |
|          30 | -35.22%  | -91.81%            | -71.48% |    -0.19 |       74 | 34.10%     | ok               |

## ORCL Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 249.77%  | 12.92%             | -29.32% |     1.39 |       70 | 65.72%     | ok               |
|          25 | 162.38%  | 12.92%             | -27.76% |     1.14 |       71 | 58.24%     | ok               |
|          20 | 157.87%  | 12.92%             | -29.32% |     1.11 |       73 | 61.40%     | ok               |
|          35 | 123.18%  | 12.92%             | -31.95% |     1    |       64 | 50.25%     | ok               |
|          30 | 123.37%  | 12.92%             | -29.47% |     1    |       70 | 54.41%     | ok               |

## OXY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 6.00%    | -8.60%             | -29.57% |     0.22 |       38 | 28.45%     | ok               |
|          35 | 3.00%    | -8.60%             | -30.04% |     0.17 |       70 | 40.60%     | ok               |
|          30 | 0.50%    | -8.60%             | -34.15% |     0.13 |       71 | 45.92%     | ok               |
|          40 | 0.62%    | -8.60%             | -31.65% |     0.12 |       56 | 35.94%     | ok               |
|          45 | -6.56%   | -8.60%             | -34.87% |    -0.03 |       46 | 30.78%     | ok               |

## PEP Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 12.85%   | -19.15%            | -11.62% |     0.58 |       44 | 27.62%     | ok               |
|          45 | 5.64%    | -19.15%            | -14.22% |     0.28 |       60 | 31.61%     | ok               |
|          40 | 2.08%    | -19.15%            | -18.04% |     0.13 |       70 | 37.10%     | ok               |
|          35 | 1.55%    | -19.15%            | -21.42% |     0.11 |       79 | 41.93%     | ok               |
|          30 | -4.54%   | -19.15%            | -21.35% |    -0.07 |       75 | 48.25%     | ok               |

## PEPE-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 4.55%    | -72.03%            | -57.66% |     0.32 |       81 | 45.21%     | ok               |
|          15 | -4.65%   | -72.03%            | -64.84% |     0.3  |       82 | 62.07%     | ok               |
|          35 | -5.60%   | -72.03%            | -51.35% |     0.2  |       64 | 39.46%     | ok               |
|          25 | -14.72%  | -72.03%            | -53.88% |     0.15 |       93 | 51.15%     | ok               |
|          20 | -25.66%  | -72.03%            | -64.07% |     0.07 |       88 | 58.43%     | ok               |

## PFE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -24.41%  | -9.76%             | -25.61% |    -0.92 |       52 | 19.13%     | ok               |
|          50 | -26.23%  | -9.76%             | -27.28% |    -1.12 |       38 | 15.31%     | ok               |
|          40 | -31.46%  | -9.76%             | -32.57% |    -1.14 |       74 | 24.13%     | ok               |
|          35 | -35.07%  | -9.76%             | -36.57% |    -1.17 |       84 | 31.95%     | ok               |
|          30 | -41.09%  | -9.76%             | -41.92% |    -1.32 |       77 | 36.27%     | ok               |

## PG Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -8.80%   | -6.86%             | -20.08% |    -0.32 |       58 | 33.28%     | ok               |
|          35 | -11.91%  | -6.86%             | -18.99% |    -0.44 |       66 | 36.77%     | ok               |
|          30 | -19.91%  | -6.86%             | -24.55% |    -0.76 |       68 | 39.93%     | ok               |
|          45 | -17.71%  | -6.86%             | -22.43% |    -0.77 |       58 | 30.78%     | ok               |
|          25 | -21.74%  | -6.86%             | -26.24% |    -0.84 |       80 | 41.43%     | ok               |

## PM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | -0.28%   | 110.77%            | -32.20% |     0.09 |       86 | 52.08%     | ok               |
|          20 | -2.79%   | 110.77%            | -31.89% |     0.04 |       87 | 60.73%     | ok               |
|          30 | -3.22%   | 110.77%            | -33.68% |     0.03 |       83 | 55.74%     | ok               |
|          50 | -6.95%   | 110.77%            | -35.70% |    -0.09 |       74 | 42.10%     | ok               |
|          40 | -8.33%   | 110.77%            | -37.94% |    -0.12 |       80 | 48.25%     | ok               |

## POL-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 39.80%   | -74.99%            | -46.45% |     0.6  |       75 | 46.93%     | ok               |
|          25 | 25.31%   | -74.99%            | -46.72% |     0.47 |       68 | 54.98%     | ok               |
|          20 | 14.36%   | -74.99%            | -52.88% |     0.37 |       78 | 60.34%     | ok               |
|          15 | -8.22%   | -74.99%            | -58.42% |     0.16 |       78 | 66.09%     | ok               |
|          40 | -2.30%   | -74.99%            | -41.02% |     0.14 |       54 | 30.84%     | ok               |

## QCOM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -3.88%   | 10.89%             | -54.50% |     0.12 |       71 | 47.75%     | ok               |
|          35 | -4.42%   | 10.89%             | -50.58% |     0.11 |       77 | 43.59%     | ok               |
|          20 | -7.78%   | 10.89%             | -54.38% |     0.08 |       67 | 50.58%     | ok               |
|          30 | -15.25%  | 10.89%             | -56.59% |    -0.04 |       73 | 46.09%     | ok               |
|          15 | -23.11%  | 10.89%             | -57.94% |    -0.13 |       71 | 53.74%     | ok               |

## QQQ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 20.19%   | 59.19%             | -12.88% |     0.58 |       62 | 43.76%     | ok               |
|          25 | 20.64%   | 59.19%             | -12.88% |     0.58 |       59 | 46.42%     | ok               |
|          15 | 21.16%   | 59.19%             | -14.17% |     0.55 |       63 | 51.91%     | ok               |
|          20 | 17.73%   | 59.19%             | -12.98% |     0.49 |       67 | 49.08%     | ok               |
|          35 | 7.91%    | 59.19%             | -18.29% |     0.29 |       68 | 40.10%     | ok               |

## RENDER-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 45.25%   | -64.28%            | -43.43% |     0.61 |       88 | 53.40%     | ok               |
|          15 | 34.05%   | -64.28%            | -44.59% |     0.54 |       88 | 56.70%     | ok               |
|          25 | 15.90%   | -64.28%            | -40.60% |     0.42 |       90 | 49.13%     | ok               |
|          30 | -19.07%  | -64.28%            | -45.00% |     0.1  |       98 | 42.52%     | ok               |
|          35 | -31.74%  | -64.28%            | -41.33% |    -0.12 |       84 | 34.37%     | ok               |

## RTX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 32.27%   | 114.99%            | -18.66% |     0.75 |       74 | 56.41%     | ok               |
|          25 | 27.34%   | 114.99%            | -18.59% |     0.66 |       62 | 53.08%     | ok               |
|          50 | 21.39%   | 114.99%            | -18.42% |     0.64 |       54 | 42.26%     | ok               |
|          35 | 22.69%   | 114.99%            | -18.00% |     0.64 |       52 | 49.92%     | ok               |
|          30 | 25.41%   | 114.99%            | -16.99% |     0.63 |       56 | 51.91%     | ok               |

## SBUX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -12.45%  | 10.32%             | -23.55% |    -0.18 |       65 | 42.26%     | ok               |
|          40 | -16.20%  | 10.32%             | -25.43% |    -0.32 |       62 | 34.11%     | ok               |
|          45 | -15.74%  | 10.32%             | -27.26% |    -0.34 |       68 | 30.28%     | ok               |
|          30 | -19.93%  | 10.32%             | -29.22% |    -0.37 |       64 | 39.93%     | ok               |
|          35 | -21.50%  | 10.32%             | -27.06% |    -0.43 |       60 | 37.27%     | ok               |

## SCHW Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 9.72%    | 57.60%             | -16.53% |     0.34 |       56 | 35.27%     | ok               |
|          50 | 0.91%    | 57.60%             | -13.28% |     0.09 |       58 | 32.28%     | ok               |
|          25 | -0.62%   | 57.60%             | -28.76% |     0.08 |       61 | 50.25%     | ok               |
|          40 | -1.66%   | 57.60%             | -23.35% |     0.03 |       64 | 38.27%     | ok               |
|          20 | -4.80%   | 57.60%             | -29.24% |    -0.02 |       71 | 52.58%     | ok               |

## SHIB-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -8.05%   | -74.94%            | -49.21% |     0.15 |       80 | 67.82%     | ok               |
|          20 | -16.17%  | -74.94%            | -46.38% |     0.05 |       77 | 63.03%     | ok               |
|          25 | -16.28%  | -74.94%            | -43.85% |     0.03 |       75 | 58.43%     | ok               |
|          35 | -23.66%  | -74.94%            | -53.32% |    -0.12 |       64 | 45.21%     | ok               |
|          30 | -30.88%  | -74.94%            | -47.96% |    -0.22 |       76 | 51.34%     | ok               |

## SHY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd    |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:-------|---------:|---------:|:-----------|:-----------------|
|          30 | -2.24%   | 0.39%              | -2.85% |    -0.79 |       48 | 34.28%     | ok               |
|          35 | -2.36%   | 0.39%              | -3.27% |    -0.84 |       50 | 32.45%     | ok               |
|          40 | -2.47%   | 0.39%              | -3.33% |    -0.89 |       50 | 30.62%     | ok               |
|          45 | -2.45%   | 0.39%              | -3.23% |    -0.9  |       48 | 27.45%     | ok               |
|          50 | -2.62%   | 0.39%              | -3.40% |    -1.01 |       44 | 24.63%     | ok               |

## SKY-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -35.27%  | 6.02%              | -56.39% |    -0.39 |       64 | 50.44%     | ok               |
|          30 | -31.05%  | 6.02%              | -44.74% |    -0.39 |       74 | 40.61%     | ok               |
|          25 | -34.59%  | 6.02%              | -48.09% |    -0.45 |       69 | 44.10%     | ok               |
|          20 | -44.55%  | 6.02%              | -58.40% |    -0.63 |       66 | 47.60%     | ok               |
|          35 | -37.92%  | 6.02%              | -49.68% |    -0.63 |       66 | 33.62%     | ok               |

## SLB Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 19.27%   | -3.75%             | -21.46% |     0.48 |       52 | 33.28%     | ok               |
|          40 | 15.58%   | -3.75%             | -25.33% |     0.41 |       46 | 36.77%     | ok               |
|          50 | -2.68%   | -3.75%             | -29.66% |     0.02 |       50 | 28.45%     | ok               |
|          35 | -12.19%  | -3.75%             | -43.52% |    -0.15 |       74 | 44.59%     | ok               |
|          30 | -23.87%  | -3.75%             | -54.23% |    -0.39 |       73 | 51.08%     | ok               |

## SLV Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 65.90%   | 141.92%            | -34.72% |     0.84 |       54 | 34.94%     | ok               |
|          45 | 63.89%   | 141.92%            | -32.46% |     0.82 |       60 | 36.11%     | ok               |
|          40 | 61.93%   | 141.92%            | -31.93% |     0.8  |       66 | 38.27%     | ok               |
|          20 | 54.84%   | 141.92%            | -42.66% |     0.72 |       66 | 47.25%     | ok               |
|          35 | 51.18%   | 141.92%            | -36.89% |     0.71 |       70 | 40.77%     | ok               |

## SMH Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 102.76%  | 166.77%            | -30.17% |     1.24 |       47 | 50.42%     | ok               |
|          35 | 81.46%   | 166.77%            | -34.36% |     1.11 |       54 | 46.26%     | ok               |
|          25 | 81.33%   | 166.77%            | -32.94% |     1.09 |       46 | 49.25%     | ok               |
|          30 | 79.19%   | 166.77%            | -33.99% |     1.08 |       48 | 47.59%     | ok               |
|          45 | 66.15%   | 166.77%            | -32.75% |     1.03 |       52 | 40.43%     | ok               |

## SNX-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -8.06%   | -77.11%            | -43.20% |     0.19 |       71 | 47.70%     | ok               |
|          35 | -6.26%   | -77.11%            | -30.08% |     0.17 |       62 | 30.84%     | ok               |
|          30 | -15.26%  | -77.11%            | -34.76% |     0.08 |       58 | 37.93%     | ok               |
|          40 | -18.26%  | -77.11%            | -40.36% |    -0.04 |       52 | 24.90%     | ok               |
|          15 | -38.08%  | -77.11%            | -47.56% |    -0.14 |       81 | 52.30%     | ok               |

## SOL-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 12.13%   | -61.53%            | -51.50% |     0.36 |       58 | 37.16%     | ok               |
|          25 | -20.47%  | -61.53%            | -52.40% |     0.05 |       74 | 57.47%     | ok               |
|          35 | -20.81%  | -61.53%            | -61.91% |     0.03 |       74 | 45.02%     | ok               |
|          45 | -16.39%  | -61.53%            | -59.86% |     0.03 |       62 | 31.80%     | ok               |
|          15 | -27.36%  | -61.53%            | -59.14% |    -0.01 |       76 | 63.79%     | ok               |

## SOXX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 84.02%   | 145.96%            | -40.27% |     1.06 |       55 | 48.92%     | ok               |
|          35 | 80.15%   | 145.96%            | -38.63% |     1.05 |       59 | 44.09%     | ok               |
|          25 | 80.50%   | 145.96%            | -41.42% |     1.03 |       53 | 48.59%     | ok               |
|          15 | 79.40%   | 145.96%            | -39.35% |     0.99 |       68 | 51.75%     | ok               |
|          30 | 70.36%   | 145.96%            | -41.89% |     0.95 |       57 | 46.42%     | ok               |

## SPY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 13.35%   | 46.36%             | -14.25% |     0.48 |       61 | 53.74%     | ok               |
|          15 | 11.80%   | 46.36%             | -16.80% |     0.43 |       70 | 56.91%     | ok               |
|          25 | 6.29%    | 46.36%             | -15.22% |     0.27 |       61 | 52.75%     | ok               |
|          30 | 1.80%    | 46.36%             | -16.47% |     0.12 |       64 | 49.92%     | ok               |
|          35 | 1.20%    | 46.36%             | -16.72% |     0.1  |       60 | 46.92%     | ok               |

## SUSHI-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -23.49%  | -81.98%            | -40.08% |    -0.19 |       52 | 14.75%     | ok               |
|          45 | -58.58%  | -81.98%            | -64.27% |    -0.77 |       56 | 18.20%     | ok               |
|          40 | -61.52%  | -81.98%            | -68.16% |    -0.77 |       63 | 24.71%     | ok               |
|          35 | -74.59%  | -81.98%            | -80.15% |    -1.06 |       82 | 30.65%     | ok               |
|          15 | -81.56%  | -81.98%            | -81.56% |    -1.09 |       95 | 48.28%     | ok               |

## T Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 59.37%   | 29.82%             | -18.13% |     1.14 |       58 | 57.40%     | ok               |
|          25 | 54.42%   | 29.82%             | -17.66% |     1.08 |       60 | 55.24%     | ok               |
|          15 | 50.66%   | 29.82%             | -15.08% |     0.99 |       67 | 61.23%     | ok               |
|          30 | 37.51%   | 29.82%             | -17.01% |     0.84 |       64 | 53.24%     | ok               |
|          35 | 23.37%   | 29.82%             | -14.49% |     0.6  |       66 | 49.75%     | ok               |

## TGT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -11.92%  | -7.84%             | -42.86% |    -0.12 |       83 | 46.59%     | ok               |
|          45 | -10.40%  | -7.84%             | -29.07% |    -0.17 |       54 | 28.79%     | ok               |
|          25 | -12.80%  | -7.84%             | -43.36% |    -0.17 |       65 | 41.60%     | ok               |
|          30 | -12.17%  | -7.84%             | -40.57% |    -0.17 |       60 | 38.77%     | ok               |
|          15 | -17.49%  | -7.84%             | -40.77% |    -0.23 |       73 | 51.25%     | ok               |

## TIA-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -2.21%   | -88.64%            | -49.23% |     0.16 |       54 | 18.77%     | ok               |
|          35 | -7.52%   | -88.64%            | -52.20% |     0.14 |       66 | 30.84%     | ok               |
|          40 | -7.13%   | -88.64%            | -45.16% |     0.14 |       68 | 26.05%     | ok               |
|          50 | -3.16%   | -88.64%            | -48.70% |     0.1  |       34 | 11.69%     | ok               |
|          30 | -45.27%  | -88.64%            | -67.94% |    -0.32 |       93 | 36.78%     | ok               |

## TLT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -21.71%  | -9.96%             | -21.87% |    -1.69 |       72 | 32.45%     | ok               |
|          50 | -15.08%  | -9.96%             | -15.73% |    -1.79 |       34 | 14.98%     | ok               |
|          40 | -19.91%  | -9.96%             | -19.91% |    -1.93 |       58 | 21.96%     | ok               |
|          15 | -27.44%  | -9.96%             | -27.76% |    -1.94 |       77 | 40.43%     | ok               |
|          35 | -22.47%  | -9.96%             | -22.47% |    -1.99 |       66 | 26.62%     | ok               |

## TMO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 48.15%   | -5.71%             | -8.17%  |     1.07 |       40 | 32.28%     | ok               |
|          45 | 43.85%   | -5.71%             | -10.13% |     0.95 |       46 | 37.10%     | ok               |
|          40 | 41.73%   | -5.71%             | -9.91%  |     0.89 |       49 | 41.60%     | ok               |
|          35 | 23.69%   | -5.71%             | -14.06% |     0.56 |       61 | 46.09%     | ok               |
|          30 | 18.14%   | -5.71%             | -18.85% |     0.45 |       61 | 51.25%     | ok               |

## TMUS Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 7.40%    | 17.09%             | -30.05% |     0.25 |       65 | 59.90%     | ok               |
|          30 | 6.20%    | 17.09%             | -25.71% |     0.23 |       70 | 47.92%     | ok               |
|          20 | 1.20%    | 17.09%             | -29.75% |     0.13 |       71 | 54.24%     | ok               |
|          25 | -2.19%   | 17.09%             | -31.45% |     0.05 |       75 | 50.42%     | ok               |
|          50 | -4.03%   | 17.09%             | -28.89% |    -0.03 |       60 | 35.94%     | ok               |

## TRX-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 11.18%   | 40.89%             | -18.79% |     0.4  |       50 | 36.97%     | ok               |
|          30 | 7.33%    | 40.89%             | -22.90% |     0.28 |       68 | 48.66%     | ok               |
|          35 | 6.44%    | 40.89%             | -21.77% |     0.26 |       64 | 45.40%     | ok               |
|          25 | 5.40%    | 40.89%             | -26.84% |     0.23 |       64 | 51.92%     | ok               |
|          20 | 5.10%    | 40.89%             | -25.45% |     0.22 |       61 | 55.36%     | ok               |

## TSLA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 56.12%   | 98.39%             | -32.60% |     0.73 |       64 | 29.78%     | ok               |
|          40 | 35.10%   | 98.39%             | -45.90% |     0.52 |       63 | 34.61%     | ok               |
|          45 | 14.45%   | 98.39%             | -46.86% |     0.34 |       67 | 31.95%     | ok               |
|          35 | 3.29%    | 98.39%             | -51.29% |     0.23 |       72 | 37.27%     | ok               |
|          30 | -14.59%  | 98.39%             | -54.91% |     0.05 |       70 | 41.26%     | ok               |

## TXN Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 17.86%   | 73.51%             | -45.45% |     0.4  |       64 | 34.61%     | ok               |
|          20 | 4.02%    | 73.51%             | -38.49% |     0.21 |       60 | 58.90%     | ok               |
|          35 | 1.17%    | 73.51%             | -43.28% |     0.15 |       74 | 49.42%     | ok               |
|          15 | -1.92%   | 73.51%             | -38.99% |     0.13 |       65 | 62.73%     | ok               |
|          40 | -0.93%   | 73.51%             | -45.67% |     0.12 |       68 | 46.92%     | ok               |

## UNH Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 28.33%   | -19.18%            | -27.59% |     0.5  |       74 | 52.58%     | ok               |
|          50 | 25.03%   | -19.18%            | -36.82% |     0.48 |       56 | 30.95%     | ok               |
|          15 | 27.03%   | -19.18%            | -32.14% |     0.47 |       75 | 67.55%     | ok               |
|          35 | 24.84%   | -19.18%            | -28.94% |     0.46 |       66 | 47.42%     | ok               |
|          40 | 20.64%   | -19.18%            | -35.73% |     0.42 |       60 | 42.76%     | ok               |

## UNI-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -23.55%  | -65.24%            | -63.75% |    -0.05 |       58 | 33.14%     | ok               |
|          45 | -22.49%  | -65.24%            | -58.49% |    -0.06 |       56 | 27.97%     | ok               |
|          35 | -36.53%  | -65.24%            | -68.71% |    -0.19 |       70 | 38.51%     | ok               |
|          50 | -29.10%  | -65.24%            | -57.60% |    -0.19 |       54 | 21.46%     | ok               |
|          30 | -72.48%  | -65.24%            | -80.61% |    -0.87 |       86 | 44.44%     | ok               |

## UPS Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -31.90%  | -20.80%            | -43.07% |    -0.57 |       80 | 47.75%     | ok               |
|          25 | -32.99%  | -20.80%            | -39.04% |    -0.61 |       76 | 44.26%     | ok               |
|          15 | -35.37%  | -20.80%            | -43.86% |    -0.65 |       86 | 52.41%     | ok               |
|          35 | -34.34%  | -20.80%            | -39.90% |    -0.69 |       65 | 33.44%     | ok               |
|          30 | -37.14%  | -20.80%            | -38.83% |    -0.75 |       70 | 39.27%     | ok               |

## USO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 19.32%   | 72.36%             | -33.25% |     0.42 |       50 | 26.62%     | ok               |
|          20 | 18.89%   | 72.36%             | -44.92% |     0.4  |       75 | 39.77%     | ok               |
|          15 | 13.27%   | 72.36%             | -45.09% |     0.33 |       74 | 42.93%     | ok               |
|          30 | 11.24%   | 72.36%             | -43.35% |     0.3  |       68 | 34.11%     | ok               |
|          25 | 8.27%    | 72.36%             | -44.86% |     0.26 |       69 | 37.10%     | ok               |

## VEA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 5.44%    | 42.68%             | -16.28% |     0.25 |       60 | 50.58%     | ok               |
|          20 | 1.19%    | 42.68%             | -17.70% |     0.1  |       61 | 47.92%     | ok               |
|          25 | -0.82%   | 42.68%             | -17.79% |     0.02 |       57 | 46.26%     | ok               |
|          30 | -0.98%   | 42.68%             | -17.93% |     0.01 |       58 | 44.09%     | ok               |
|          35 | -2.09%   | 42.68%             | -16.79% |    -0.03 |       56 | 43.09%     | ok               |

## VIXY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -48.04%  | -60.89%            | -69.78% |    -0.43 |       46 | 10.48%     | ok               |
|          45 | -59.37%  | -60.89%            | -75.03% |    -0.61 |       60 | 16.64%     | ok               |
|          40 | -67.66%  | -60.89%            | -80.72% |    -0.74 |       76 | 21.46%     | ok               |
|          35 | -70.62%  | -60.89%            | -84.37% |    -0.76 |       90 | 26.79%     | ok               |
|          15 | -77.31%  | -60.89%            | -89.47% |    -0.78 |       99 | 44.43%     | ok               |

## VNQ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -7.66%   | 17.93%             | -19.07% |    -0.32 |       56 | 28.12%     | ok               |
|          50 | -8.10%   | 17.93%             | -17.13% |    -0.36 |       52 | 25.62%     | ok               |
|          25 | -12.08%  | 17.93%             | -22.34% |    -0.46 |       65 | 40.10%     | ok               |
|          20 | -13.69%  | 17.93%             | -23.79% |    -0.52 |       68 | 42.76%     | ok               |
|          15 | -15.00%  | 17.93%             | -24.90% |    -0.57 |       65 | 43.93%     | ok               |

## VTI Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 16.42%   | 45.64%             | -13.96% |     0.57 |       64 | 54.24%     | ok               |
|          15 | 10.46%   | 45.64%             | -15.70% |     0.39 |       67 | 56.74%     | ok               |
|          25 | 2.96%    | 45.64%             | -16.10% |     0.16 |       60 | 52.25%     | ok               |
|          30 | -4.76%   | 45.64%             | -18.77% |    -0.11 |       70 | 50.25%     | ok               |
|          35 | -7.15%   | 45.64%             | -20.89% |    -0.22 |       64 | 47.09%     | ok               |

## VWO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -10.42%  | 39.11%             | -24.01% |    -0.31 |       71 | 49.08%     | ok               |
|          50 | -8.80%   | 39.11%             | -21.68% |    -0.32 |       60 | 31.95%     | ok               |
|          40 | -9.88%   | 39.11%             | -23.57% |    -0.35 |       70 | 37.44%     | ok               |
|          20 | -11.44%  | 39.11%             | -26.14% |    -0.36 |       69 | 46.92%     | ok               |
|          45 | -10.58%  | 39.11%             | -23.75% |    -0.39 |       62 | 34.44%     | ok               |

## VZ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -6.80%   | 7.21%              | -12.71% |    -0.19 |       50 | 24.29%     | ok               |
|          45 | -17.93%  | 7.21%              | -20.96% |    -0.59 |       64 | 27.95%     | ok               |
|          35 | -21.08%  | 7.21%              | -22.26% |    -0.68 |       61 | 33.94%     | ok               |
|          25 | -23.77%  | 7.21%              | -22.13% |    -0.7  |       79 | 41.93%     | ok               |
|          40 | -25.49%  | 7.21%              | -23.75% |    -0.89 |       66 | 31.28%     | ok               |

## WFC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -2.85%   | 62.48%             | -18.29% |    -0.02 |       62 | 35.61%     | ok               |
|          35 | -7.13%   | 62.48%             | -24.26% |    -0.07 |       83 | 47.75%     | ok               |
|          20 | -13.28%  | 62.48%             | -29.96% |    -0.15 |       79 | 57.24%     | ok               |
|          45 | -10.39%  | 62.48%             | -24.02% |    -0.23 |       70 | 40.43%     | ok               |
|          40 | -11.68%  | 62.48%             | -24.88% |    -0.26 |       78 | 43.93%     | ok               |

## WIF-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 60.24%   | -79.02%            | -46.21% |     0.66 |       73 | 42.34%     | ok               |
|          20 | 54.58%   | -79.02%            | -40.67% |     0.64 |       67 | 39.66%     | ok               |
|          25 | 1.83%    | -79.02%            | -45.19% |     0.3  |       69 | 36.97%     | ok               |
|          50 | -12.13%  | -79.02%            | -33.04% |    -0.02 |       38 | 11.69%     | ok               |
|          30 | -35.45%  | -79.02%            | -51.39% |    -0.13 |       70 | 32.95%     | ok               |

## WMT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 48.49%   | 95.22%             | -9.18%  |     1.33 |       38 | 41.76%     | ok               |
|          50 | 41.25%   | 95.22%             | -12.19% |     1.23 |       34 | 39.43%     | ok               |
|          40 | 36.13%   | 95.22%             | -12.49% |     1.02 |       44 | 43.09%     | ok               |
|          35 | 35.24%   | 95.22%             | -13.08% |     0.97 |       54 | 47.75%     | ok               |
|          15 | 15.05%   | 95.22%             | -25.74% |     0.41 |       70 | 61.23%     | ok               |

## XBI Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 5.41%    | 62.81%             | -16.56% |     0.21 |       60 | 35.94%     | ok               |
|          45 | 4.60%    | 62.81%             | -16.74% |     0.2  |       52 | 32.78%     | ok               |
|          35 | 1.30%    | 62.81%             | -18.84% |     0.12 |       62 | 39.27%     | ok               |
|          30 | 0.18%    | 62.81%             | -19.80% |     0.09 |       62 | 40.93%     | ok               |
|          25 | -2.26%   | 62.81%             | -23.66% |     0.04 |       72 | 43.26%     | ok               |

## XLB Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -1.68%   | 16.39%             | -20.68% |    -0.01 |       54 | 31.61%     | ok               |
|          50 | -1.74%   | 16.39%             | -17.59% |    -0.02 |       42 | 27.29%     | ok               |
|          35 | -4.92%   | 16.39%             | -23.62% |    -0.13 |       56 | 34.94%     | ok               |
|          45 | -4.65%   | 16.39%             | -20.79% |    -0.14 |       42 | 28.79%     | ok               |
|          25 | -6.87%   | 16.39%             | -22.63% |    -0.19 |       60 | 40.27%     | ok               |

## XLC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 10.32%   | 38.80%             | -12.33% |     0.39 |       69 | 54.08%     | ok               |
|          25 | 7.15%    | 38.80%             | -12.31% |     0.29 |       68 | 56.07%     | ok               |
|          40 | 5.97%    | 38.80%             | -13.38% |     0.27 |       70 | 46.42%     | ok               |
|          35 | 5.94%    | 38.80%             | -13.38% |     0.27 |       66 | 50.92%     | ok               |
|          20 | -0.20%   | 38.80%             | -13.78% |     0.06 |       74 | 58.90%     | ok               |

## XLE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 7.52%    | 34.20%             | -25.98% |     0.28 |       54 | 36.11%     | ok               |
|          45 | 3.11%    | 34.20%             | -29.68% |     0.16 |       60 | 38.10%     | ok               |
|          35 | 0.94%    | 34.20%             | -31.51% |     0.11 |       65 | 42.76%     | ok               |
|          25 | -5.75%   | 34.20%             | -36.05% |    -0.06 |       83 | 48.25%     | ok               |
|          40 | -5.64%   | 34.20%             | -34.51% |    -0.08 |       64 | 40.60%     | ok               |

## XLF Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -4.77%   | 39.60%             | -18.01% |    -0.1  |       68 | 53.91%     | ok               |
|          15 | -8.71%   | 39.60%             | -19.58% |    -0.23 |       76 | 56.74%     | ok               |
|          25 | -11.41%  | 39.60%             | -23.22% |    -0.36 |       77 | 50.42%     | ok               |
|          30 | -11.84%  | 39.60%             | -23.61% |    -0.39 |       78 | 48.09%     | ok               |
|          35 | -18.92%  | 39.60%             | -27.24% |    -0.75 |       68 | 43.93%     | ok               |

## XLI Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 3.38%    | 49.23%             | -10.36% |     0.18 |       74 | 51.25%     | ok               |
|          20 | -0.81%   | 49.23%             | -12.74% |     0.02 |       65 | 46.76%     | ok               |
|          30 | -2.98%   | 49.23%             | -11.79% |    -0.07 |       66 | 44.26%     | ok               |
|          45 | -3.38%   | 49.23%             | -14.01% |    -0.11 |       64 | 35.77%     | ok               |
|          50 | -3.27%   | 49.23%             | -11.03% |    -0.11 |       60 | 33.44%     | ok               |

## XLK Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 87.25%   | 71.07%             | -14.75% |     1.38 |       39 | 50.92%     | ok               |
|          20 | 71.51%   | 71.07%             | -14.75% |     1.23 |       46 | 48.92%     | ok               |
|          25 | 68.02%   | 71.07%             | -14.75% |     1.23 |       40 | 46.76%     | ok               |
|          30 | 65.83%   | 71.07%             | -14.75% |     1.22 |       40 | 45.59%     | ok               |
|          35 | 47.33%   | 71.07%             | -13.61% |     0.99 |       52 | 42.93%     | ok               |

## XLM-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 26.14%   | -46.53%            | -38.97% |     0.48 |       44 | 27.39%     | ok               |
|          45 | 22.34%   | -46.53%            | -43.99% |     0.44 |       50 | 31.03%     | ok               |
|          30 | 5.21%    | -46.53%            | -50.36% |     0.28 |       69 | 45.79%     | ok               |
|          40 | 1.75%    | -46.53%            | -43.80% |     0.23 |       49 | 35.44%     | ok               |
|          35 | -4.00%   | -46.53%            | -50.42% |     0.17 |       69 | 41.76%     | ok               |

## XLP Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 7.69%    | 13.92%             | -6.85%  |     0.5  |       56 | 32.61%     | ok               |
|          40 | 7.00%    | 13.92%             | -7.77%  |     0.44 |       70 | 36.94%     | ok               |
|          50 | 6.36%    | 13.92%             | -7.01%  |     0.43 |       56 | 30.45%     | ok               |
|          35 | 6.07%    | 13.92%             | -9.73%  |     0.38 |       66 | 39.93%     | ok               |
|          30 | 4.18%    | 13.92%             | -11.16% |     0.27 |       68 | 41.43%     | ok               |

## XLU Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 5.85%    | 45.80%             | -12.97% |     0.32 |       52 | 31.28%     | ok               |
|          45 | 4.45%    | 45.80%             | -14.27% |     0.25 |       54 | 32.28%     | ok               |
|          40 | 1.57%    | 45.80%             | -15.59% |     0.12 |       58 | 33.78%     | ok               |
|          35 | -4.35%   | 45.80%             | -19.71% |    -0.16 |       62 | 35.94%     | ok               |
|          30 | -5.24%   | 45.80%             | -20.40% |    -0.19 |       67 | 39.10%     | ok               |

## XLV Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -15.51%  | 8.95%              | -19.97% |    -0.77 |       68 | 36.11%     | ok               |
|          25 | -16.76%  | 8.95%              | -21.14% |    -0.83 |       70 | 37.44%     | ok               |
|          15 | -20.53%  | 8.95%              | -24.43% |    -1    |       81 | 42.26%     | ok               |
|          20 | -20.47%  | 8.95%              | -24.51% |    -1.02 |       75 | 39.10%     | ok               |
|          35 | -19.93%  | 8.95%              | -23.94% |    -1.08 |       66 | 33.61%     | ok               |

## XLY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 5.14%    | 27.35%             | -12.94% |     0.23 |       70 | 41.43%     | ok               |
|          30 | 3.26%    | 27.35%             | -14.01% |     0.17 |       70 | 44.43%     | ok               |
|          50 | 1.64%    | 27.35%             | -11.49% |     0.12 |       50 | 29.45%     | ok               |
|          15 | 1.20%    | 27.35%             | -15.77% |     0.11 |       74 | 51.25%     | ok               |
|          45 | -1.43%   | 27.35%             | -13.48% |    -0    |       54 | 32.11%     | ok               |

## XOM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | 7.52%    | 41.91%             | -19.90% |     0.28 |       57 | 37.94%     | ok               |
|          50 | 5.97%    | 41.91%             | -21.35% |     0.25 |       40 | 29.45%     | ok               |
|          30 | 5.96%    | 41.91%             | -20.29% |     0.24 |       57 | 36.77%     | ok               |
|          20 | 1.41%    | 41.91%             | -25.56% |     0.12 |       64 | 40.27%     | ok               |
|          35 | -1.10%   | 41.91%             | -20.93% |     0.04 |       57 | 35.61%     | ok               |

## XRP-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | -25.11%  | -59.86%            | -46.87% |    -0.14 |       68 | 39.85%     | ok               |
|          40 | -30.47%  | -59.86%            | -44.89% |    -0.26 |       58 | 33.72%     | ok               |
|          30 | -37.23%  | -59.86%            | -54.70% |    -0.33 |       70 | 44.06%     | ok               |
|          45 | -38.24%  | -59.86%            | -46.06% |    -0.42 |       58 | 29.50%     | ok               |
|          50 | -34.88%  | -59.86%            | -38.03% |    -0.46 |       60 | 22.03%     | ok               |

## YFI-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -49.69%  | -65.28%            | -50.74% |    -0.82 |       62 | 27.20%     | ok               |
|          45 | -46.11%  | -65.28%            | -51.53% |    -0.92 |       68 | 21.26%     | ok               |
|          35 | -61.45%  | -65.28%            | -63.29% |    -1.02 |       71 | 34.67%     | ok               |
|          30 | -64.14%  | -65.28%            | -71.12% |    -1.03 |       81 | 40.61%     | ok               |
|          25 | -67.78%  | -65.28%            | -72.16% |    -1.12 |       75 | 45.59%     | ok               |

## ZEC-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 110.48%  | 1528.42%           | -24.66% |     0.85 |       46 | 24.14%     | ok               |
|          35 | 80.71%   | 1528.42%           | -44.34% |     0.72 |       54 | 30.65%     | ok               |
|          25 | 62.59%   | 1528.42%           | -48.59% |     0.64 |       60 | 39.66%     | ok               |
|          30 | 44.96%   | 1528.42%           | -47.68% |     0.56 |       64 | 36.40%     | ok               |
|          50 | 44.68%   | 1528.42%           | -34.39% |     0.55 |       48 | 21.65%     | ok               |
