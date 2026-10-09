# Market Tracker Backtest Report

_Generated: 2026-10-09T06:14:20+00:00_

## Data Sources

- Crypto: Kraken -> Coinbase -> CoinGecko OHLC -> CoinPaprika fallback chain.
- Stocks / ETFs / indices: Stooq -> Yahoo Finance fallback chain.
- Data rows are generated from real market APIs. Mock OHLCV rows are not generated.

## Data Freshness

- Rows: **92,730**
- Symbols: **161**
- Date range: **2024-05-16** to **2026-10-09**

## Latest Signals

| symbol     | date                |         close |   composite_score | signal   | data_source   |
|:-----------|:--------------------|--------------:|------------------:|:---------|:--------------|
| AAVE-USD   | 2026-10-09 00:00:00 |   168.73      |         52.8333   | LONG     | Kraken API    |
| ABBV       | 2026-10-08 00:00:00 |   272.42      |         72.4167   | LONG     | Yahoo Finance |
| ALGO-USD   | 2026-10-09 00:00:00 |     0.11976   |         38.8333   | LONG     | Kraken API    |
| AMAT       | 2026-10-08 00:00:00 |   509.57      |         72.8333   | LONG     | Yahoo Finance |
| AMD        | 2026-10-08 00:00:00 |   620.68      |         67.4167   | LONG     | Yahoo Finance |
| AMGN       | 2026-10-08 00:00:00 |   407.44      |         70.4167   | LONG     | Yahoo Finance |
| COP        | 2026-10-08 00:00:00 |   134.19      |         58.9167   | LONG     | Yahoo Finance |
| CSCO       | 2026-10-08 00:00:00 |   114.89      |         69.9167   | LONG     | Yahoo Finance |
| DXY-INDEX  | 2026-10-09 00:00:00 |   101.996     |         77.6882   | LONG     | Yahoo Finance |
| FIL-USD    | 2026-10-09 00:00:00 |     1.074     |         46.3333   | LONG     | Kraken API    |
| GRT-USD    | 2026-10-09 00:00:00 |     0.02687   |         37.9167   | LONG     | Kraken API    |
| IBIT       | 2026-10-08 00:00:00 |    46.26      |         30.0833   | LONG     | Yahoo Finance |
| LIN        | 2026-10-08 00:00:00 |   481.7       |         41.8333   | LONG     | Yahoo Finance |
| LLY        | 2026-10-08 00:00:00 |  1169.6       |         63.75     | LONG     | Yahoo Finance |
| LRCX       | 2026-10-08 00:00:00 |   320.59      |         62.6667   | LONG     | Yahoo Finance |
| META       | 2026-10-08 00:00:00 |   720.89      |         52.0833   | LONG     | Yahoo Finance |
| MSFT       | 2026-10-08 00:00:00 |   522.61      |         68.25     | LONG     | Yahoo Finance |
| NEAR-USD   | 2026-10-09 00:00:00 |     4.837     |         30.1667   | LONG     | Kraken API    |
| NVDA       | 2026-10-08 00:00:00 |   230.48      |         74.4167   | LONG     | Yahoo Finance |
| QQQ        | 2026-10-08 00:00:00 |   747.58      |         76.4167   | LONG     | Yahoo Finance |
| RENDER-USD | 2026-10-09 00:00:00 |     1.943     |         43.6667   | LONG     | Kraken API    |
| SMH        | 2026-10-08 00:00:00 |   607.27      |         76.25     | LONG     | Yahoo Finance |
| SOXX       | 2026-10-08 00:00:00 |   563.28      |         71        | LONG     | Yahoo Finance |
| TIA-USD    | 2026-10-09 00:00:00 |     0.5099    |         51.8333   | LONG     | Kraken API    |
| TXN        | 2026-10-08 00:00:00 |   288.2       |         71.5833   | LONG     | Yahoo Finance |
| XLE        | 2026-10-08 00:00:00 |    65.24      |         62.25     | LONG     | Yahoo Finance |
| XLK        | 2026-10-08 00:00:00 |   197.78      |         76.4167   | LONG     | Yahoo Finance |
| XLP        | 2026-10-08 00:00:00 |    83.42      |         51.9167   | LONG     | Yahoo Finance |
| AAPL       | 2026-10-08 00:00:00 |   340.42      |         49        | NEUTRAL  | Yahoo Finance |
| ADA-USD    | 2026-10-09 00:00:00 |     0.237663  |        -14.3333   | NEUTRAL  | Kraken API    |
| ADBE       | 2026-10-08 00:00:00 |   241.05      |         -9        | NEUTRAL  | Yahoo Finance |
| AMZN       | 2026-10-08 00:00:00 |   254.06      |         52        | NEUTRAL  | Yahoo Finance |
| APT-USD    | 2026-10-09 00:00:00 |     0.7981    |          2.16667  | NEUTRAL  | Kraken API    |
| ARB-USD    | 2026-10-09 00:00:00 |     0.1774    |          9.08333  | NEUTRAL  | Kraken API    |
| ARKK       | 2026-10-08 00:00:00 |    87.6       |         12.1667   | NEUTRAL  | Yahoo Finance |
| ATOM-USD   | 2026-10-09 00:00:00 |     1.8869    |         56.3333   | NEUTRAL  | Kraken API    |
| AVAX-USD   | 2026-10-09 00:00:00 |    10.303     |         12.6667   | NEUTRAL  | Kraken API    |
| AVGO       | 2026-10-08 00:00:00 |   360.14      |        -11        | NEUTRAL  | Yahoo Finance |
| BCH-USD    | 2026-10-09 00:00:00 |   280.48      |        -13.9167   | NEUTRAL  | Kraken API    |
| BITO       | 2026-10-08 00:00:00 |    10.93      |          3.08333  | NEUTRAL  | Yahoo Finance |
| BLK        | 2026-10-08 00:00:00 |  1065.35      |        -14.9167   | NEUTRAL  | Yahoo Finance |
| BONK-USD   | 2026-10-09 00:00:00 |     3.385e-06 |        -12.5833   | NEUTRAL  | Kraken API    |
| BTC-USD    | 2026-10-09 00:00:00 | 82307.3       |          7.66667  | NEUTRAL  | Kraken API    |
| C          | 2026-10-08 00:00:00 |   128.08      |        -27.8333   | NEUTRAL  | Yahoo Finance |
| CAT        | 2026-10-08 00:00:00 |   796.18      |         -5.25     | NEUTRAL  | Yahoo Finance |
| CL         | 2026-10-08 00:00:00 |    88.1       |         -2.33333  | NEUTRAL  | Yahoo Finance |
| COMP-USD   | 2026-10-09 00:00:00 |    23.42      |         22.1667   | NEUTRAL  | Kraken API    |
| COST       | 2026-10-08 00:00:00 |   947.92      |         27.75     | NEUTRAL  | Yahoo Finance |
| CRM        | 2026-10-08 00:00:00 |   227.8       |          9.91667  | NEUTRAL  | Yahoo Finance |
| CRV-USD    | 2026-10-09 00:00:00 |     0.3448    |         -4.08333  | NEUTRAL  | Kraken API    |
| CVX        | 2026-10-08 00:00:00 |   211.55      |         12.1667   | NEUTRAL  | Yahoo Finance |
| DASH-USD   | 2026-10-09 00:00:00 |    51.036     |        -23.25     | NEUTRAL  | Kraken API    |
| DBC        | 2026-10-08 00:00:00 |    32.91      |         40.5833   | NEUTRAL  | Yahoo Finance |
| DE         | 2026-10-08 00:00:00 |   652.58      |        -12.8333   | NEUTRAL  | Yahoo Finance |
| DIA        | 2026-10-08 00:00:00 |   511.65      |         16.0833   | NEUTRAL  | Yahoo Finance |
| DIS        | 2026-10-08 00:00:00 |   107.02      |         53.1667   | NEUTRAL  | Yahoo Finance |
| DOT-USD    | 2026-10-09 00:00:00 |     1.1622    |         -7.33333  | NEUTRAL  | Kraken API    |
| EEM        | 2026-10-08 00:00:00 |    66.1       |        -22.0833   | NEUTRAL  | Yahoo Finance |
| EFA        | 2026-10-08 00:00:00 |   102.7       |        -22.5      | NEUTRAL  | Yahoo Finance |
| EOG        | 2026-10-08 00:00:00 |   148.51      |         56.6667   | NEUTRAL  | Yahoo Finance |
| ETC-USD    | 2026-10-09 00:00:00 |     8.3       |        -11.9167   | NEUTRAL  | Kraken API    |
| ETH-USD    | 2026-10-09 00:00:00 |  2489.35      |        -14.3333   | NEUTRAL  | Kraken API    |
| EWJ        | 2026-10-08 00:00:00 |    97.32      |         15.5      | NEUTRAL  | Yahoo Finance |
| FCX        | 2026-10-08 00:00:00 |    71.14      |         -0.333333 | NEUTRAL  | Yahoo Finance |
| FET-USD    | 2026-10-09 00:00:00 |     0.2225    |         26.6667   | NEUTRAL  | Kraken API    |
| FXI        | 2026-10-08 00:00:00 |    33.45      |        -60        | NEUTRAL  | Yahoo Finance |
| GDX        | 2026-10-08 00:00:00 |    86.72      |        -29        | NEUTRAL  | Yahoo Finance |
| GE         | 2026-10-08 00:00:00 |   305.62      |        -57.5      | NEUTRAL  | Yahoo Finance |
| GOOGL      | 2026-10-08 00:00:00 |   348.29      |         27.9167   | NEUTRAL  | Yahoo Finance |
| HBAR-USD   | 2026-10-09 00:00:00 |     0.09252   |         19.9167   | NEUTRAL  | Kraken API    |
| HD         | 2026-10-08 00:00:00 |   295.47      |         -5.75     | NEUTRAL  | Yahoo Finance |
| HON        | 2026-10-08 00:00:00 |   206.6       |        -19.25     | NEUTRAL  | Yahoo Finance |
| IBM        | 2026-10-08 00:00:00 |   226.61      |        -55.3333   | NEUTRAL  | Yahoo Finance |
| ICP-USD    | 2026-10-09 00:00:00 |     3.044     |         10.6667   | NEUTRAL  | Kraken API    |
| IEMG       | 2026-10-08 00:00:00 |    80.5       |        -20.3333   | NEUTRAL  | Yahoo Finance |
| INJ-USD    | 2026-10-09 00:00:00 |     7.075     |         10.6667   | NEUTRAL  | Kraken API    |
| INTC       | 2026-10-08 00:00:00 |   107.08      |          1.41667  | NEUTRAL  | Yahoo Finance |
| INTU       | 2026-10-08 00:00:00 |   303.88      |         20.9167   | NEUTRAL  | Yahoo Finance |
| ITA        | 2026-10-08 00:00:00 |   204.88      |        -29.25     | NEUTRAL  | Yahoo Finance |
| IWM        | 2026-10-08 00:00:00 |   277.57      |         -0.166667 | NEUTRAL  | Yahoo Finance |
| JNJ        | 2026-10-08 00:00:00 |   256.48      |        -44.0833   | NEUTRAL  | Yahoo Finance |
| JPM        | 2026-10-08 00:00:00 |   331.42      |        -10.6667   | NEUTRAL  | Yahoo Finance |
| KO         | 2026-10-08 00:00:00 |    87.77      |         22.5      | NEUTRAL  | Yahoo Finance |
| LDO-USD    | 2026-10-09 00:00:00 |     0.426     |         -2.58333  | NEUTRAL  | Kraken API    |
| LINK-USD   | 2026-10-09 00:00:00 |    12.8727    |          5.66667  | NEUTRAL  | Kraken API    |
| LTC-USD    | 2026-10-09 00:00:00 |    63.94      |         13.3333   | NEUTRAL  | Kraken API    |
| MPC        | 2026-10-08 00:00:00 |   463.34      |         64.5      | NEUTRAL  | Yahoo Finance |
| MRK        | 2026-10-08 00:00:00 |   142.38      |        -10.5      | NEUTRAL  | Yahoo Finance |
| MU         | 2026-10-08 00:00:00 |  1035.84      |         20.3333   | NEUTRAL  | Yahoo Finance |
| NEM        | 2026-10-08 00:00:00 |   115.55      |        -27.3333   | NEUTRAL  | Yahoo Finance |
| NFLX       | 2026-10-08 00:00:00 |    71.57      |        -21.75     | NEUTRAL  | Yahoo Finance |
| NOW        | 2026-10-08 00:00:00 |   139.75      |         33        | NEUTRAL  | Yahoo Finance |
| OP-USD     | 2026-10-09 00:00:00 |     0.1231    |        -12.5833   | NEUTRAL  | Kraken API    |
| ORCL       | 2026-10-08 00:00:00 |   135.69      |        -45.3333   | NEUTRAL  | Yahoo Finance |
| OXY        | 2026-10-08 00:00:00 |    60.28      |         47.6667   | NEUTRAL  | Yahoo Finance |
| PEPE-USD   | 2026-10-09 00:00:00 |     3.928e-06 |          9.41667  | NEUTRAL  | Kraken API    |
| PFE        | 2026-10-08 00:00:00 |    27.82      |         17.3333   | NEUTRAL  | Yahoo Finance |
| PG         | 2026-10-08 00:00:00 |   150.59      |         69.4167   | NEUTRAL  | Yahoo Finance |
| PM         | 2026-10-08 00:00:00 |   200.5       |         51        | NEUTRAL  | Yahoo Finance |
| POL-USD    | 2026-10-09 00:00:00 |     0.10023   |        -23.1667   | NEUTRAL  | Kraken API    |
| QCOM       | 2026-10-08 00:00:00 |   176.01      |         -7.41667  | NEUTRAL  | Yahoo Finance |
| SHY        | 2026-10-08 00:00:00 |    81.2       |        -27.25     | NEUTRAL  | Yahoo Finance |
| SKY-USD    | 2026-10-09 00:00:00 |     0.07716   |          8.58333  | NEUTRAL  | Kraken API    |
| SLV        | 2026-10-08 00:00:00 |    53.45      |        -72.8333   | NEUTRAL  | Yahoo Finance |
| SOL-USD    | 2026-10-09 00:00:00 |   110.28      |          2.33333  | NEUTRAL  | Kraken API    |
| SPY        | 2026-10-08 00:00:00 |   773.93      |         62.6667   | NEUTRAL  | Yahoo Finance |
| SUSHI-USD  | 2026-10-09 00:00:00 |     0.2309    |         18.4167   | NEUTRAL  | Kraken API    |
| TGT        | 2026-10-08 00:00:00 |   154.76      |         -3        | NEUTRAL  | Yahoo Finance |
| TMO        | 2026-10-08 00:00:00 |   651.98      |         21.5833   | NEUTRAL  | Yahoo Finance |
| TMUS       | 2026-10-08 00:00:00 |   171.31      |          4.91667  | NEUTRAL  | Yahoo Finance |
| TRX-USD    | 2026-10-09 00:00:00 |     0.33213   |        -44.25     | NEUTRAL  | Kraken API    |
| TSLA       | 2026-10-08 00:00:00 |   375         |         14.1667   | NEUTRAL  | Yahoo Finance |
| UNH        | 2026-10-08 00:00:00 |   370.95      |         -3.66667  | NEUTRAL  | Yahoo Finance |
| UNI-USD    | 2026-10-09 00:00:00 |     7.4006    |          9.08333  | NEUTRAL  | Kraken API    |
| USO        | 2026-10-08 00:00:00 |   147.58      |         27.3333   | NEUTRAL  | Yahoo Finance |
| VEA        | 2026-10-08 00:00:00 |    69.86      |        -28.5      | NEUTRAL  | Yahoo Finance |
| VIXY       | 2026-10-08 00:00:00 |    16.5       |        -20        | NEUTRAL  | Yahoo Finance |
| VTI        | 2026-10-08 00:00:00 |   379.56      |         62.6667   | NEUTRAL  | Yahoo Finance |
| VWO        | 2026-10-08 00:00:00 |    59.1       |        -29        | NEUTRAL  | Yahoo Finance |
| VZ         | 2026-10-08 00:00:00 |    46.35      |        -23.6667   | NEUTRAL  | Yahoo Finance |
| WIF-USD    | 2026-10-09 00:00:00 |     0.2148    |        -26.9167   | NEUTRAL  | Kraken API    |
| WMT        | 2026-10-08 00:00:00 |   110.56      |          8.33333  | NEUTRAL  | Yahoo Finance |
| XBI        | 2026-10-08 00:00:00 |   149.29      |        -24.75     | NEUTRAL  | Yahoo Finance |
| XLB        | 2026-10-08 00:00:00 |    49.27      |        -29.25     | NEUTRAL  | Yahoo Finance |
| XLC        | 2026-10-08 00:00:00 |   112.07      |         25.9167   | NEUTRAL  | Yahoo Finance |
| XLF        | 2026-10-08 00:00:00 |    54.23      |         -2.33333  | NEUTRAL  | Yahoo Finance |
| XLI        | 2026-10-08 00:00:00 |   168.4       |        -38.4167   | NEUTRAL  | Yahoo Finance |
| XLM-USD    | 2026-10-09 00:00:00 |     0.194714  |         -3.33333  | NEUTRAL  | Kraken API    |
| XLU        | 2026-10-08 00:00:00 |    41.07      |         -9.75     | NEUTRAL  | Yahoo Finance |
| XLV        | 2026-10-08 00:00:00 |   168.16      |          7.5      | NEUTRAL  | Yahoo Finance |
| XLY        | 2026-10-08 00:00:00 |   111.71      |         12.1667   | NEUTRAL  | Yahoo Finance |
| XOM        | 2026-10-08 00:00:00 |   168.5       |         36.3333   | NEUTRAL  | Yahoo Finance |
| XRP-USD    | 2026-10-09 00:00:00 |     1.3947    |         -9.91667  | NEUTRAL  | Kraken API    |
| YFI-USD    | 2026-10-09 00:00:00 |  2322         |         -8.58333  | NEUTRAL  | Kraken API    |
| ZEC-USD    | 2026-10-09 00:00:00 |  1218.78      |         -3.66667  | NEUTRAL  | Kraken API    |
| AGG        | 2026-10-08 00:00:00 |    94.63      |        -46.25     | SHORT    | Yahoo Finance |
| BA         | 2026-10-08 00:00:00 |   187.75      |        -37.75     | SHORT    | Yahoo Finance |
| BAC        | 2026-10-08 00:00:00 |    53.61      |        -38.1667   | SHORT    | Yahoo Finance |
| BND        | 2026-10-08 00:00:00 |    70.22      |        -48        | SHORT    | Yahoo Finance |
| CMCSA      | 2026-10-08 00:00:00 |    21.21      |        -47.9167   | SHORT    | Yahoo Finance |
| DOGE-USD   | 2026-10-09 00:00:00 |     0.0852108 |        -38.9167   | SHORT    | Kraken API    |
| GDXJ       | 2026-10-08 00:00:00 |   110.9       |        -51.5      | SHORT    | Yahoo Finance |
| GLD        | 2026-10-08 00:00:00 |   378.62      |        -56.5833   | SHORT    | Yahoo Finance |
| GS         | 2026-10-08 00:00:00 |   882.59      |        -54.0833   | SHORT    | Yahoo Finance |
| HYG        | 2026-10-08 00:00:00 |    77.14      |        -55.0833   | SHORT    | Yahoo Finance |
| IEF        | 2026-10-08 00:00:00 |    89.45      |        -31.25     | SHORT    | Yahoo Finance |
| MCD        | 2026-10-08 00:00:00 |   236.9       |        -37        | SHORT    | Yahoo Finance |
| MS         | 2026-10-08 00:00:00 |   187.44      |        -55.6667   | SHORT    | Yahoo Finance |
| NKE        | 2026-10-08 00:00:00 |    34.74      |        -30.75     | SHORT    | Yahoo Finance |
| PEP        | 2026-10-08 00:00:00 |   128.34      |        -43.0833   | SHORT    | Yahoo Finance |
| RTX        | 2026-10-08 00:00:00 |   184.32      |        -45.4167   | SHORT    | Yahoo Finance |
| SBUX       | 2026-10-08 00:00:00 |    93.21      |        -35        | SHORT    | Yahoo Finance |
| SCHW       | 2026-10-08 00:00:00 |    96.87      |        -39.6667   | SHORT    | Yahoo Finance |
| SHIB-USD   | 2026-10-09 00:00:00 |     5.378e-06 |        -38.9167   | SHORT    | Kraken API    |
| SLB        | 2026-10-08 00:00:00 |    48.98      |        -49.0833   | SHORT    | Yahoo Finance |
| SNX-USD    | 2026-10-09 00:00:00 |     0.233     |        -32.3333   | SHORT    | Kraken API    |
| T          | 2026-10-08 00:00:00 |    24.87      |        -36.4167   | SHORT    | Yahoo Finance |
| TLT        | 2026-10-08 00:00:00 |    77.87      |        -54.9167   | SHORT    | Yahoo Finance |
| UPS        | 2026-10-08 00:00:00 |    94.13      |        -36.9167   | SHORT    | Yahoo Finance |
| VNQ        | 2026-10-08 00:00:00 |    89.35      |        -38.5833   | SHORT    | Yahoo Finance |
| WFC        | 2026-10-08 00:00:00 |    82.03      |        -49.8333   | SHORT    | Yahoo Finance |

## Edge Summary

- Symbols with trades: **161** of 161
- Beat buy-and-hold: **31.06%** of traded symbols
- Positive return: **29.19%** of traded symbols
- Median strategy return: **-10.04%** (benchmark **16.10%**)
- Median excess vs benchmark: **-24.98%**
- Median Sharpe: **-0.17**
- Median exposure: **44.26%**

> Edge is real only if both _beat buy-and-hold_ and _median excess_ are convincingly positive across many symbols. Treat a single high-return symbol as noise.

## Portfolio Backtest

Actual capital-allocation books (not per-symbol averages). Benchmarks: `equal_weight_buyhold` (whole tracked universe), `spy_buyhold` (100% SPY), and `sixty_forty` (60% SPY / 40% AGG). `high_conf_voltarget` inverse-vol-weights the HIGH-confidence book; `conviction_long_short` is market-neutral. Judge on **Sharpe** and **max_drawdown** out-of-sample, not raw return: a fully-invested long book wins on return in a bull market but carries all the risk.

| strategy              | scope         | ann_return   | ann_vol   |   sharpe | max_drawdown   | total_return   |   avg_gross_exposure |
|:----------------------|:--------------|:-------------|:----------|---------:|:---------------|:---------------|---------------------:|
| equal_weight_buyhold  | full          | 12.44%       | 28.43%    |     0.44 | -39.53%        | 29.07%         |                 1    |
| equal_weight_buyhold  | out_of_sample | 7.94%        | 27.76%    |     0.29 | -28.22%        | 4.47%          |                 1    |
| all_signals_ew        | full          | -17.65%      | 24.20%    |    -0.73 | -60.60%        | -46.50%        |                 1    |
| all_signals_ew        | out_of_sample | 12.53%       | 23.19%    |     0.54 | -23.20%        | 11.05%         |                 1    |
| high_conf_ew          | full          | -0.46%       | 31.41%    |    -0.01 | -44.58%        | -14.94%        |                 0.9  |
| high_conf_ew          | out_of_sample | 25.78%       | 27.54%    |     0.94 | -22.85%        | 26.27%         |                 0.9  |
| high_conf_voltarget   | full          | -1.21%       | 27.98%    |    -0.04 | -38.47%        | -14.20%        |                 0.9  |
| high_conf_voltarget   | out_of_sample | 14.15%       | 22.39%    |     0.63 | -17.00%        | 13.11%         |                 0.9  |
| conviction_long_short | full          | -16.78%      | 22.47%    |    -0.75 | -49.86%        | -44.42%        |                 0.96 |
| conviction_long_short | out_of_sample | 0.31%        | 19.58%    |     0.02 | -26.60%        | -1.69%         |                 0.96 |
| spy_buyhold           | full          | 4.54%        | 13.51%    |     0.34 | -19.00%        | 11.66%         |                 0.79 |
| spy_buyhold           | out_of_sample | 1.86%        | 9.92%     |     0.19 | -12.06%        | 1.47%          |                 0.79 |
| sixty_forty           | full          | 2.27%        | 8.54%     |     0.27 | -11.66%        | 5.95%          |                 0.79 |
| sixty_forty           | out_of_sample | -1.12%       | 6.68%     |    -0.17 | -8.26%         | -1.42%         |                 0.79 |

## Walk-Forward Robustness

Each book measured across contiguous time folds (each a different regime). A book has durable edge only if `mean_sharpe` is positive, `min_sharpe` isn't deeply negative, and `pct_positive_folds` is high — a single great fold doesn't count. `fold_sharpes` lists each fold oldest-to-newest.

| strategy              |   n_folds |   mean_sharpe |   median_sharpe |   min_sharpe | pct_positive_folds   | mean_return   | fold_sharpes                 |
|:----------------------|----------:|--------------:|----------------:|-------------:|:---------------------|:--------------|:-----------------------------|
| equal_weight_buyhold  |         5 |          0.59 |            0.96 |        -0.24 | 80.00%               | 5.72%         | 0.96;1.04;0.03;-0.24;1.16    |
| all_signals_ew        |         5 |         -0.76 |           -1.24 |        -1.94 | 20.00%               | -9.41%        | -1.24;-1.72;-1.94;1.72;-0.62 |
| high_conf_ew          |         5 |          0.13 |            0.1  |        -0.8  | 60.00%               | -1.71%        | 0.10;-0.67;-0.80;1.30;0.71   |
| high_conf_voltarget   |         5 |          0.15 |            0.24 |        -0.75 | 60.00%               | -2.19%        | 0.24;-0.42;-0.75;0.78;0.91   |
| conviction_long_short |         5 |         -0.72 |           -0.62 |        -1.75 | 20.00%               | -10.78%       | -1.75;-0.62;-0.93;-0.58;0.30 |
| spy_buyhold           |         5 |          0.38 |            0.09 |        -0.26 | 60.00%               | 2.40%         | 1.67;-0.13;0.09;0.50;-0.26   |
| sixty_forty           |         5 |          0.27 |            0.22 |        -0.65 | 60.00%               | 1.23%         | 1.54;-0.05;0.30;0.22;-0.65   |

## Strategy Comparison

Each decision rule backtested over the same data. `out_of_sample` is the most recent ~35% of each symbol's history (unseen tail). A rule has real edge only if `median_excess` and `beat_benchmark_pct` stay positive out-of-sample, not just full-sample.

| strategy        | scope         |   symbols | beat_benchmark_pct   | positive_pct   | median_return   | median_benchmark   | median_excess   |   median_sharpe |   total_trades |
|:----------------|:--------------|----------:|:---------------------|:---------------|:----------------|:-------------------|:----------------|----------------:|---------------:|
| trend           | full          |       161 | 31.06%               | 29.19%         | -10.04%         | 16.10%             | -24.98%         |           -0.17 |          11289 |
| trend           | out_of_sample |       161 | 27.95%               | 52.17%         | 0.15%           | 9.07%              | -14.79%         |            0.14 |           3792 |
| mean_reversion  | full          |       156 | 38.46%               | 48.72%         | -0.14%          | 15.15%             | -15.21%         |            0    |           1230 |
| mean_reversion  | out_of_sample |       120 | 30.83%               | 53.33%         | 0.30%           | 8.28%              | -9.78%          |            0.16 |            494 |
| regime_adaptive | full          |       161 | 30.43%               | 30.43%         | -10.07%         | 16.10%             | -24.99%         |           -0.14 |          11560 |
| regime_adaptive | out_of_sample |       161 | 29.19%               | 50.31%         | 0.04%           | 9.07%              | -15.37%         |            0.05 |           3905 |

## Signal Calibration

Realized forward return in the signal's direction, grouped by confidence. HIGH should outrank LOW for the confidence score to be meaningful.

| confidence_level   |   horizon |     n | mean_return   | median_return   | win_rate   |
|:-------------------|----------:|------:|:--------------|:----------------|:-----------|
| HIGH               |         5 |  7985 | 0.18%         | 0.04%           | 50.58%     |
| MEDIUM             |         5 | 29180 | 0.01%         | 0.03%           | 50.22%     |
| LOW                |         5 |  3473 | -0.41%        | -0.41%          | 45.95%     |
| ALL                |         5 | 40638 | 0.01%         | 0.00%           | 49.93%     |
| HIGH               |        10 |  7931 | 0.46%         | 0.08%           | 50.90%     |
| MEDIUM             |        10 | 28849 | 0.18%         | 0.06%           | 50.48%     |
| LOW                |        10 |  3431 | -0.72%        | -0.53%          | 46.55%     |
| ALL                |        10 | 40211 | 0.16%         | 0.03%           | 50.23%     |
| HIGH               |        20 |  7753 | 1.10%         | 0.32%           | 52.62%     |
| MEDIUM             |        20 | 28360 | 0.86%         | 0.54%           | 53.02%     |
| LOW                |        20 |  3384 | -0.48%        | -0.60%          | 47.07%     |
| ALL                |        20 | 39497 | 0.80%         | 0.42%           | 52.43%     |

## Backtest Summary

### Data Quality / Signal Availability

- **ok**: 161 symbols

| symbol     |   trades | return   | benchmark_return   | mdd     |   sharpe | exposure   | skipped_reason   |
|:-----------|---------:|:---------|:-------------------|:--------|---------:|:-----------|:-----------------|
| AAPL       |       64 | 4.25%    | 79.32%             | -23.09% |     0.19 | 51.25%     | ok               |
| AAVE-USD   |       65 | -23.97%  | -5.11%             | -66.17% |    -0.03 | 42.34%     | ok               |
| ABBV       |       72 | -25.71%  | 65.76%             | -30.52% |    -0.58 | 47.92%     | ok               |
| ADA-USD    |       75 | -37.41%  | -64.95%            | -49.38% |    -0.27 | 46.74%     | ok               |
| ADBE       |       73 | -8.36%   | -50.08%            | -31.20% |     0.02 | 56.91%     | ok               |
| AGG        |       67 | -7.33%   | -2.52%             | -11.29% |    -1.16 | 33.78%     | ok               |
| ALGO-USD   |       76 | -35.34%  | -39.90%            | -38.19% |    -0.27 | 40.04%     | ok               |
| AMAT       |       71 | -32.15%  | 138.08%            | -53.91% |    -0.27 | 51.25%     | ok               |
| AMD        |       54 | 27.13%   | 281.68%            | -41.09% |     0.45 | 36.94%     | ok               |
| AMGN       |       69 | -18.62%  | 29.46%             | -34.19% |    -0.36 | 50.25%     | ok               |
| AMZN       |       82 | -56.75%  | 38.35%             | -57.20% |    -1.64 | 40.60%     | ok               |
| APT-USD    |       72 | -34.60%  | -83.28%            | -61.91% |    -0.15 | 40.04%     | ok               |
| ARB-USD    |       77 | -22.21%  | -42.46%            | -54.96% |     0.07 | 43.68%     | ok               |
| ARKK       |       86 | -26.40%  | 94.84%             | -31.32% |    -0.37 | 43.26%     | ok               |
| ATOM-USD   |       92 | -58.27%  | -54.05%            | -58.27% |    -0.81 | 48.28%     | ok               |
| AVAX-USD   |       68 | -34.31%  | -48.51%            | -45.19% |    -0.27 | 40.04%     | ok               |
| AVGO       |       64 | 15.79%   | 155.03%            | -36.09% |     0.35 | 41.93%     | ok               |
| BA         |       71 | 4.99%    | 2.62%              | -26.91% |     0.21 | 51.25%     | ok               |
| BAC        |       72 | -9.86%   | 36.69%             | -25.80% |    -0.21 | 48.42%     | ok               |
| BCH-USD    |       74 | 16.03%   | -25.10%            | -53.87% |     0.38 | 49.23%     | ok               |
| BITO       |       79 | -19.66%  | -58.74%            | -43.10% |    -0.09 | 42.43%     | ok               |
| BLK        |       85 | -16.54%  | 31.90%             | -26.90% |    -0.41 | 47.92%     | ok               |
| BND        |       65 | -6.80%   | -2.46%             | -10.79% |    -1.03 | 35.61%     | ok               |
| BONK-USD   |       74 | 22.95%   | -80.05%            | -45.22% |     0.46 | 45.98%     | ok               |
| BTC-USD    |       70 | 13.77%   | -14.99%            | -23.38% |     0.36 | 52.87%     | ok               |
| C          |       77 | -35.22%  | 99.69%             | -39.51% |    -0.76 | 46.59%     | ok               |
| CAT        |       70 | 6.23%    | 127.01%            | -22.01% |     0.23 | 48.75%     | ok               |
| CL         |       64 | -5.50%   | -6.80%             | -14.32% |    -0.13 | 38.94%     | ok               |
| CMCSA      |       82 | -35.83%  | -42.52%            | -46.50% |    -0.86 | 42.60%     | ok               |
| COMP-USD   |       95 | -35.33%  | -39.17%            | -55.77% |    -0.17 | 49.23%     | ok               |
| COP        |       68 | -19.25%  | 11.98%             | -43.40% |    -0.29 | 43.59%     | ok               |
| COST       |       58 | -1.32%   | 19.53%             | -30.95% |     0.02 | 41.43%     | ok               |
| CRM        |       65 | -34.52%  | -19.98%            | -45.50% |    -0.51 | 45.92%     | ok               |
| CRV-USD    |       66 | 29.63%   | -48.69%            | -39.89% |     0.49 | 37.74%     | ok               |
| CSCO       |       64 | 16.78%   | 137.67%            | -21.79% |     0.4  | 48.75%     | ok               |
| CVX        |       71 | -13.64%  | 31.32%             | -27.78% |    -0.3  | 41.76%     | ok               |
| DASH-USD   |       57 | -9.06%   | 140.84%            | -64.43% |     0.33 | 30.84%     | ok               |
| DBC        |       66 | -8.16%   | 40.22%             | -24.10% |    -0.21 | 35.27%     | ok               |
| DE         |       70 | -12.17%  | 65.45%             | -23.98% |    -0.18 | 44.26%     | ok               |
| DIA        |       64 | -7.90%   | 28.17%             | -12.94% |    -0.41 | 43.76%     | ok               |
| DIS        |       60 | -6.18%   | 3.53%              | -28.17% |    -0.05 | 43.09%     | ok               |
| DOGE-USD   |       73 | -33.52%  | -50.46%            | -60.95% |    -0.14 | 48.47%     | ok               |
| DOT-USD    |       88 | -57.53%  | -70.72%            | -63.33% |    -0.54 | 48.85%     | ok               |
| DXY-INDEX  |       40 | -0.69%   | -3.91%             | -6.02%  |    -0.1  | 31.17%     | ok               |
| EEM        |       62 | -12.79%  | 51.61%             | -25.38% |    -0.37 | 40.60%     | ok               |
| EFA        |       64 | -10.98%  | 26.23%             | -12.96% |    -0.42 | 41.76%     | ok               |
| EOG        |       78 | -30.38%  | 16.10%             | -47.87% |    -0.66 | 44.76%     | ok               |
| ETC-USD    |       56 | -20.80%  | -48.84%            | -45.54% |    -0.17 | 30.65%     | ok               |
| ETH-USD    |       58 | 178.93%  | 37.04%             | -30.11% |     1.44 | 48.85%     | ok               |
| EWJ        |       62 | -22.99%  | 42.55%             | -29.40% |    -0.8  | 36.44%     | ok               |
| FCX        |       65 | -29.37%  | 36.70%             | -46.84% |    -0.32 | 44.26%     | ok               |
| FET-USD    |       79 | -48.46%  | -67.31%            | -61.24% |    -0.33 | 41.95%     | ok               |
| FIL-USD    |       65 | -47.64%  | -58.48%            | -58.54% |    -0.5  | 36.78%     | ok               |
| FXI        |       50 | -10.27%  | 14.71%             | -24.33% |    -0.18 | 31.78%     | ok               |
| GDX        |       60 | -3.80%   | 143.19%            | -33.31% |     0.07 | 44.43%     | ok               |
| GDXJ       |       70 | -37.43%  | 150.45%            | -41.57% |    -0.5  | 42.76%     | ok               |
| GE         |       76 | -8.43%   | 89.68%             | -27.82% |    -0.04 | 48.09%     | ok               |
| GLD        |       50 | 10.01%   | 72.08%             | -13.87% |     0.32 | 45.42%     | ok               |
| GOOGL      |       55 | 57.09%   | 99.96%             | -17.15% |     1.01 | 47.25%     | ok               |
| GRT-USD    |       77 | 20.05%   | -70.09%            | -45.34% |     0.42 | 45.79%     | ok               |
| GS         |       70 | -3.64%   | 90.00%             | -22.13% |     0.02 | 48.09%     | ok               |
| HBAR-USD   |       38 | -44.08%  | -10.29%            | -56.39% |    -0.99 | 37.60%     | ok               |
| HD         |       65 | 2.94%    | -13.79%            | -17.15% |     0.16 | 43.26%     | ok               |
| HON        |       89 | -28.13%  | 1.16%              | -33.03% |    -0.71 | 55.07%     | ok               |
| HYG        |       87 | -7.30%   | -0.17%             | -10.59% |    -0.82 | 38.10%     | ok               |
| IBIT       |       38 | 37.60%   | 21.70%             | -18.95% |     0.69 | 34.76%     | ok               |
| IBM        |       69 | -24.27%  | 34.11%             | -48.94% |    -0.28 | 49.92%     | ok               |
| ICP-USD    |       77 | -8.32%   | -34.30%            | -46.42% |     0.18 | 39.27%     | ok               |
| IEF        |       78 | -10.66%  | -4.23%             | -13.34% |    -1.45 | 34.28%     | ok               |
| IEMG       |       60 | -12.35%  | 47.22%             | -28.65% |    -0.37 | 40.77%     | ok               |
| INJ-USD    |       63 | -23.82%  | -23.31%            | -69.96% |     0.01 | 39.85%     | ok               |
| INTC       |       68 | 40.30%   | 234.31%            | -60.60% |     0.53 | 48.09%     | ok               |
| INTU       |       73 | -17.96%  | -53.49%            | -41.31% |    -0.18 | 46.26%     | ok               |
| ITA        |       74 | -2.95%   | 51.83%             | -23.75% |    -0    | 48.92%     | ok               |
| IWM        |       54 | 7.12%    | 33.49%             | -12.28% |     0.31 | 34.78%     | ok               |
| JNJ        |       64 | 4.76%    | 66.24%             | -16.86% |     0.23 | 46.92%     | ok               |
| JPM        |       73 | -23.98%  | 63.69%             | -32.74% |    -0.66 | 45.59%     | ok               |
| KO         |       54 | 22.60%   | 38.61%             | -8.64%  |     0.81 | 37.44%     | ok               |
| LDO-USD    |       72 | 10.52%   | -45.24%            | -59.02% |     0.37 | 46.93%     | ok               |
| LIN        |       74 | -12.89%  | 12.10%             | -20.61% |    -0.42 | 37.94%     | ok               |
| LINK-USD   |       69 | 31.57%   | -6.83%             | -33.64% |     0.52 | 46.55%     | ok               |
| LLY        |       78 | -34.75%  | 51.68%             | -53.34% |    -0.58 | 49.08%     | ok               |
| LRCX       |       80 | -27.92%  | 240.00%            | -60.58% |    -0.2  | 42.26%     | ok               |
| LTC-USD    |       67 | 12.78%   | -30.15%            | -32.66% |     0.35 | 53.83%     | ok               |
| MCD        |       77 | -0.55%   | -13.39%            | -21.88% |     0.04 | 40.27%     | ok               |
| META       |       76 | -27.84%  | 52.33%             | -44.52% |    -0.39 | 49.92%     | ok               |
| MPC        |       71 | 15.43%   | 165.11%            | -37.91% |     0.36 | 52.08%     | ok               |
| MRK        |       65 | -23.45%  | 8.79%              | -35.95% |    -0.45 | 42.43%     | ok               |
| MS         |       75 | -8.22%   | 88.23%             | -27.79% |    -0.12 | 48.25%     | ok               |
| MSFT       |       85 | -27.52%  | 24.14%             | -39.07% |    -0.61 | 50.75%     | ok               |
| MU         |       51 | 139.60%  | 709.95%            | -68.76% |     0.99 | 53.24%     | ok               |
| NEAR-USD   |       73 | 99.86%   | 107.77%            | -52.00% |     0.86 | 44.25%     | ok               |
| NEM        |       68 | -26.97%  | 169.72%            | -39.56% |    -0.27 | 50.42%     | ok               |
| NFLX       |       78 | 10.13%   | 17.23%             | -21.09% |     0.3  | 53.58%     | ok               |
| NKE        |       79 | -25.11%  | -62.14%            | -55.35% |    -0.26 | 46.59%     | ok               |
| NOW        |       80 | 11.00%   | -7.82%             | -30.43% |     0.3  | 50.25%     | ok               |
| NVDA       |       77 | -48.05%  | 82.40%             | -52.37% |    -0.67 | 54.90%     | ok               |
| OP-USD     |       68 | -43.69%  | -79.84%            | -68.74% |    -0.35 | 33.33%     | ok               |
| ORCL       |       62 | 89.24%   | 11.08%             | -30.61% |     0.82 | 52.75%     | ok               |
| OXY        |       69 | -0.67%   | -4.10%             | -28.48% |     0.11 | 42.26%     | ok               |
| PEP        |       74 | -1.75%   | -29.91%            | -21.35% |     0.02 | 45.92%     | ok               |
| PEPE-USD   |       85 | -45.46%  | -50.81%            | -61.29% |    -0.24 | 49.23%     | ok               |
| PFE        |       81 | -35.05%  | -3.80%             | -41.90% |    -1.08 | 37.27%     | ok               |
| PG         |       64 | -23.93%  | -10.29%            | -24.16% |    -0.97 | 35.11%     | ok               |
| PM         |       79 | -8.13%   | 99.19%             | -35.15% |    -0.1  | 50.75%     | ok               |
| POL-USD    |       81 | 29.19%   | -54.03%            | -38.69% |     0.5  | 50.00%     | ok               |
| QCOM       |       77 | -26.82%  | -8.93%             | -57.69% |    -0.21 | 43.93%     | ok               |
| QQQ        |       66 | 9.79%    | 65.40%             | -14.20% |     0.33 | 45.92%     | ok               |
| RENDER-USD |       92 | -23.37%  | -54.90%            | -44.84% |     0.03 | 46.93%     | ok               |
| RTX        |       64 | 33.21%   | 76.82%             | -16.99% |     0.74 | 52.41%     | ok               |
| SBUX       |       62 | -14.06%  | 23.82%             | -29.22% |    -0.23 | 38.44%     | ok               |
| SCHW       |       80 | -19.26%  | 24.13%             | -31.92% |    -0.43 | 46.26%     | ok               |
| SHIB-USD   |       79 | -44.18%  | -57.82%            | -45.40% |    -0.48 | 52.11%     | ok               |
| SHY        |       46 | -1.78%   | -0.33%             | -3.30%  |    -0.6  | 36.77%     | ok               |
| SKY-USD    |       85 | -52.16%  | 26.45%             | -62.08% |    -0.68 | 45.21%     | ok               |
| SLB        |       73 | -37.86%  | 1.16%              | -57.55% |    -0.71 | 48.59%     | ok               |
| SLV        |       66 | 11.63%   | 97.52%             | -42.66% |     0.32 | 40.43%     | ok               |
| SMH        |       48 | 53.86%   | 161.53%            | -34.29% |     0.85 | 44.26%     | ok               |
| SNX-USD    |       64 | -21.55%  | -63.76%            | -50.27% |    -0.04 | 33.91%     | ok               |
| SOL-USD    |       68 | -14.77%  | -24.89%            | -44.99% |     0.06 | 60.54%     | ok               |
| SOXX       |       54 | 67.82%   | 145.40%            | -39.81% |     0.94 | 43.26%     | ok               |
| SPY        |       64 | 0.09%    | 46.39%             | -15.53% |     0.06 | 50.08%     | ok               |
| SUSHI-USD  |       98 | -82.99%  | -61.71%            | -82.90% |    -1.42 | 39.85%     | ok               |
| T          |       72 | 36.69%   | 43.76%             | -17.01% |     0.79 | 56.74%     | ok               |
| TGT        |       62 | -11.80%  | -3.67%             | -34.98% |    -0.18 | 37.77%     | ok               |
| TIA-USD    |       95 | -65.98%  | -78.37%            | -78.90% |    -0.66 | 42.34%     | ok               |
| TLT        |       68 | -19.35%  | -15.37%            | -21.85% |    -1.44 | 33.78%     | ok               |
| TMO        |       65 | 23.33%   | 9.18%              | -18.85% |     0.52 | 55.07%     | ok               |
| TMUS       |       74 | 2.58%    | 4.73%              | -28.14% |     0.15 | 47.92%     | ok               |
| TRX-USD    |       66 | 10.86%   | 35.08%             | -22.90% |     0.38 | 51.72%     | ok               |
| TSLA       |       80 | -37.10%  | 114.48%            | -59.64% |    -0.26 | 42.93%     | ok               |
| TXN        |       77 | -22.26%  | 47.82%             | -47.39% |    -0.21 | 50.42%     | ok               |
| UNH        |       75 | 22.49%   | -28.84%            | -26.31% |     0.44 | 48.59%     | ok               |
| UNI-USD    |       92 | -55.03%  | 49.18%             | -78.80% |    -0.35 | 50.57%     | ok               |
| UPS        |       72 | -34.69%  | -37.10%            | -39.06% |    -0.67 | 42.26%     | ok               |
| USO        |       67 | -9.34%   | 93.55%             | -44.98% |    -0.01 | 33.28%     | ok               |
| VEA        |       60 | -4.20%   | 37.20%             | -17.74% |    -0.12 | 42.93%     | ok               |
| VIXY       |       94 | -78.21%  | -63.91%            | -88.17% |    -0.94 | 32.95%     | ok               |
| VNQ        |       73 | -13.85%  | 5.24%              | -24.92% |    -0.55 | 40.10%     | ok               |
| VTI        |       68 | -7.41%   | 44.91%             | -17.64% |    -0.21 | 50.08%     | ok               |
| VWO        |       80 | -18.70%  | 32.60%             | -25.20% |    -0.7  | 41.10%     | ok               |
| VZ         |       82 | -20.07%  | 15.16%             | -25.90% |    -0.59 | 41.26%     | ok               |
| WFC        |       80 | -16.83%  | 34.34%             | -28.90% |    -0.27 | 47.75%     | ok               |
| WIF-USD    |       66 | -29.15%  | -61.73%            | -52.76% |    -0.04 | 37.16%     | ok               |
| WMT        |       69 | 4.37%    | 72.72%             | -25.37% |     0.19 | 49.08%     | ok               |
| XBI        |       64 | -4.44%   | 61.24%             | -18.10% |    -0.03 | 39.60%     | ok               |
| XLB        |       64 | -13.23%  | 7.85%              | -25.04% |    -0.47 | 32.28%     | ok               |
| XLC        |       61 | 12.62%   | 35.89%             | -12.33% |     0.47 | 50.25%     | ok               |
| XLE        |       73 | -8.97%   | 39.33%             | -32.20% |    -0.15 | 44.59%     | ok               |
| XLF        |       80 | -9.46%   | 28.57%             | -23.61% |    -0.29 | 46.92%     | ok               |
| XLI        |       82 | -10.04%  | 34.52%             | -17.79% |    -0.35 | 42.76%     | ok               |
| XLK        |       42 | 61.90%   | 86.33%             | -14.75% |     1.16 | 46.59%     | ok               |
| XLM-USD    |       67 | -8.23%   | -25.83%            | -54.59% |     0.13 | 48.28%     | ok               |
| XLP        |       66 | -0.43%   | 6.40%              | -11.16% |     0.01 | 38.10%     | ok               |
| XLU        |       69 | -6.23%   | 13.64%             | -20.40% |    -0.23 | 40.27%     | ok               |
| XLV        |       76 | -22.26%  | 15.15%             | -22.75% |    -1.07 | 37.44%     | ok               |
| XLY        |       75 | -4.15%   | 25.67%             | -18.35% |    -0.06 | 47.59%     | ok               |
| XOM        |       55 | 1.71%    | 42.95%             | -20.29% |     0.12 | 34.28%     | ok               |
| XRP-USD    |       62 | 10.41%   | -35.27%            | -33.91% |     0.32 | 36.78%     | ok               |
| YFI-USD    |       77 | -70.53%  | -54.86%            | -70.53% |    -1.37 | 37.93%     | ok               |
| ZEC-USD    |       59 | 169.97%  | 3109.85%           | -56.50% |     0.97 | 42.34%     | ok               |

## AAPL Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 10.77%   | 79.32%             | -22.53% |     0.31 |       73 | 56.07%     | ok               |
|          15 | 7.92%    | 79.32%             | -24.50% |     0.26 |       82 | 63.39%     | ok               |
|          30 | 4.25%    | 79.32%             | -23.09% |     0.19 |       64 | 51.25%     | ok               |
|          40 | 3.15%    | 79.32%             | -28.08% |     0.17 |       60 | 45.76%     | ok               |
|          35 | 2.76%    | 79.32%             | -24.45% |     0.16 |       64 | 49.92%     | ok               |

## AAVE-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 49.17%   | -5.11%             | -43.61% |     0.64 |       43 | 36.78%     | ok               |
|          45 | 35.28%   | -5.11%             | -49.19% |     0.55 |       48 | 31.61%     | ok               |
|          35 | 30.13%   | -5.11%             | -48.79% |     0.5  |       51 | 39.85%     | ok               |
|          50 | 20.27%   | -5.11%             | -45.07% |     0.42 |       46 | 24.33%     | ok               |
|          15 | -16.02%  | -5.11%             | -61.76% |     0.13 |       72 | 55.36%     | ok               |

## ABBV Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -15.64%  | 65.76%             | -27.91% |    -0.35 |       56 | 35.11%     | ok               |
|          25 | -24.46%  | 65.76%             | -30.41% |    -0.53 |       71 | 49.92%     | ok               |
|          20 | -24.91%  | 65.76%             | -29.62% |    -0.53 |       69 | 51.58%     | ok               |
|          40 | -23.65%  | 65.76%             | -27.36% |    -0.57 |       72 | 40.27%     | ok               |
|          30 | -25.71%  | 65.76%             | -30.52% |    -0.58 |       72 | 47.92%     | ok               |

## ADA-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 13.14%   | -64.95%            | -35.54% |     0.35 |       48 | 27.97%     | ok               |
|          45 | 2.40%    | -64.95%            | -34.64% |     0.23 |       47 | 32.57%     | ok               |
|          40 | -15.06%  | -64.95%            | -40.73% |     0.03 |       59 | 38.51%     | ok               |
|          15 | -26.71%  | -64.95%            | -47.27% |     0.01 |       70 | 62.45%     | ok               |
|          35 | -19.12%  | -64.95%            | -42.89% |    -0.01 |       63 | 42.15%     | ok               |

## ADBE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | 7.08%    | -50.08%            | -29.07% |     0.25 |       58 | 61.40%     | ok               |
|          35 | -1.80%   | -50.08%            | -31.73% |     0.1  |       79 | 48.25%     | ok               |
|          20 | -6.95%   | -50.08%            | -31.52% |     0.06 |       64 | 64.39%     | ok               |
|          30 | -8.36%   | -50.08%            | -31.20% |     0.02 |       73 | 56.91%     | ok               |
|          15 | -17.40%  | -50.08%            | -34.98% |    -0.1  |       64 | 66.22%     | ok               |

## AGG Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -7.33%   | -2.52%             | -11.29% |    -1.16 |       67 | 33.78%     | ok               |
|          20 | -8.45%   | -2.52%             | -11.89% |    -1.21 |       72 | 38.60%     | ok               |
|          45 | -6.77%   | -2.52%             | -9.79%  |    -1.22 |       62 | 25.29%     | ok               |
|          25 | -8.37%   | -2.52%             | -12.28% |    -1.25 |       71 | 36.77%     | ok               |
|          35 | -8.00%   | -2.52%             | -11.92% |    -1.3  |       64 | 30.62%     | ok               |

## ALGO-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -35.34%  | -39.90%            | -38.19% |    -0.27 |       76 | 40.04%     | ok               |
|          15 | -41.09%  | -39.90%            | -51.37% |    -0.3  |       79 | 50.19%     | ok               |
|          25 | -43.61%  | -39.90%            | -54.38% |    -0.38 |       78 | 44.83%     | ok               |
|          20 | -47.28%  | -39.90%            | -53.23% |    -0.43 |       81 | 47.70%     | ok               |
|          35 | -46.64%  | -39.90%            | -50.16% |    -0.58 |       64 | 34.87%     | ok               |

## AMAT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -24.11%  | 138.08%            | -41.04% |    -0.19 |       50 | 35.94%     | ok               |
|          15 | -30.14%  | 138.08%            | -53.90% |    -0.19 |       72 | 60.23%     | ok               |
|          35 | -27.10%  | 138.08%            | -47.88% |    -0.2  |       71 | 48.59%     | ok               |
|          30 | -32.15%  | 138.08%            | -53.91% |    -0.27 |       71 | 51.25%     | ok               |
|          40 | -33.04%  | 138.08%            | -50.74% |    -0.32 |       69 | 43.76%     | ok               |

## AMD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 30.65%   | 281.68%            | -39.92% |     0.48 |       56 | 32.11%     | ok               |
|          40 | 27.13%   | 281.68%            | -41.09% |     0.45 |       54 | 36.94%     | ok               |
|          35 | 24.51%   | 281.68%            | -43.15% |     0.43 |       62 | 38.44%     | ok               |
|          30 | 8.09%    | 281.68%            | -49.79% |     0.3  |       63 | 40.93%     | ok               |
|          25 | 3.37%    | 281.68%            | -54.33% |     0.26 |       59 | 43.09%     | ok               |

## AMGN Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -13.96%  | 29.46%             | -26.65% |    -0.22 |       64 | 56.07%     | ok               |
|          35 | -16.51%  | 29.46%             | -31.29% |    -0.31 |       69 | 46.76%     | ok               |
|          30 | -18.62%  | 29.46%             | -34.19% |    -0.36 |       69 | 50.25%     | ok               |
|          15 | -20.95%  | 29.46%             | -27.98% |    -0.37 |       63 | 60.40%     | ok               |
|          25 | -20.42%  | 29.46%             | -33.47% |    -0.4  |       63 | 52.58%     | ok               |

## AMZN Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -25.60%  | 38.35%             | -27.34% |    -0.77 |       52 | 29.62%     | ok               |
|          50 | -30.16%  | 38.35%             | -32.37% |    -1.09 |       48 | 22.63%     | ok               |
|          45 | -35.40%  | 38.35%             | -36.22% |    -1.25 |       54 | 26.12%     | ok               |
|          35 | -51.39%  | 38.35%             | -51.90% |    -1.5  |       75 | 34.78%     | ok               |
|          30 | -56.75%  | 38.35%             | -57.20% |    -1.64 |       82 | 40.60%     | ok               |

## APT-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -0.60%   | -83.28%            | -61.21% |     0.28 |       76 | 49.62%     | ok               |
|          50 | 6.76%    | -83.28%            | -39.44% |     0.26 |       44 | 16.67%     | ok               |
|          25 | -25.05%  | -83.28%            | -60.99% |    -0    |       70 | 44.44%     | ok               |
|          45 | -15.94%  | -83.28%            | -59.04% |    -0.01 |       60 | 23.56%     | ok               |
|          15 | -35.66%  | -83.28%            | -63.22% |    -0.07 |       74 | 55.36%     | ok               |

## ARB-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 54.13%   | -42.46%            | -44.26% |     0.63 |       85 | 59.96%     | ok               |
|          45 | 30.34%   | -42.46%            | -35.19% |     0.49 |       56 | 26.82%     | ok               |
|          50 | 21.38%   | -42.46%            | -30.72% |     0.42 |       44 | 19.73%     | ok               |
|          20 | 14.85%   | -42.46%            | -54.05% |     0.42 |       71 | 54.41%     | ok               |
|          40 | 5.58%    | -42.46%            | -40.13% |     0.31 |       57 | 34.10%     | ok               |

## ARKK Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -12.57%  | 94.84%             | -37.76% |    -0.04 |       90 | 54.58%     | ok               |
|          20 | -20.63%  | 94.84%             | -34.82% |    -0.2  |       88 | 49.75%     | ok               |
|          30 | -26.40%  | 94.84%             | -31.32% |    -0.37 |       86 | 43.26%     | ok               |
|          35 | -32.93%  | 94.84%             | -36.46% |    -0.55 |       86 | 40.77%     | ok               |
|          25 | -37.00%  | 94.84%             | -43.74% |    -0.6  |       96 | 45.76%     | ok               |

## ATOM-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -41.59%  | -54.05%            | -48.20% |    -0.33 |       86 | 65.90%     | ok               |
|          25 | -48.34%  | -54.05%            | -49.45% |    -0.52 |       92 | 54.60%     | ok               |
|          20 | -55.70%  | -54.05%            | -57.28% |    -0.66 |       96 | 58.24%     | ok               |
|          30 | -58.27%  | -54.05%            | -58.27% |    -0.81 |       92 | 48.28%     | ok               |
|          35 | -59.37%  | -54.05%            | -61.61% |    -0.94 |       82 | 42.15%     | ok               |

## AVAX-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 32.87%   | -48.51%            | -22.06% |     0.59 |       34 | 19.92%     | ok               |
|          40 | 15.46%   | -48.51%            | -26.27% |     0.37 |       36 | 27.39%     | ok               |
|          45 | 12.22%   | -48.51%            | -23.19% |     0.33 |       30 | 24.33%     | ok               |
|          35 | -2.54%   | -48.51%            | -33.05% |     0.16 |       54 | 33.72%     | ok               |
|          15 | -16.15%  | -48.51%            | -42.49% |     0.06 |       73 | 53.26%     | ok               |

## AVGO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | 19.12%   | 155.03%            | -38.01% |     0.38 |       68 | 44.59%     | ok               |
|          30 | 15.79%   | 155.03%            | -36.09% |     0.35 |       64 | 41.93%     | ok               |
|          50 | 10.84%   | 155.03%            | -36.86% |     0.29 |       56 | 29.78%     | ok               |
|          35 | 7.38%    | 155.03%            | -40.43% |     0.26 |       74 | 38.94%     | ok               |
|          20 | 5.45%    | 155.03%            | -39.42% |     0.24 |       77 | 47.75%     | ok               |

## BA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 39.59%   | 2.62%              | -13.34% |     0.87 |       46 | 35.44%     | ok               |
|          40 | 32.96%   | 2.62%              | -23.87% |     0.65 |       46 | 43.09%     | ok               |
|          35 | 31.00%   | 2.62%              | -19.93% |     0.59 |       68 | 47.59%     | ok               |
|          25 | 14.73%   | 2.62%              | -27.37% |     0.35 |       72 | 54.74%     | ok               |
|          45 | 5.70%    | 2.62%              | -26.76% |     0.22 |       44 | 39.43%     | ok               |

## BAC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 0.46%    | 36.69%             | -23.08% |     0.09 |       64 | 45.09%     | ok               |
|          20 | -1.26%   | 36.69%             | -18.20% |     0.05 |       80 | 53.08%     | ok               |
|          25 | -3.67%   | 36.69%             | -22.11% |    -0.02 |       74 | 50.58%     | ok               |
|          15 | -9.19%   | 36.69%             | -23.94% |    -0.14 |       87 | 60.23%     | ok               |
|          45 | -6.80%   | 36.69%             | -19.47% |    -0.15 |       60 | 36.94%     | ok               |

## BCH-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 62.64%   | -25.10%            | -45.51% |     0.72 |       72 | 57.66%     | ok               |
|          20 | 34.89%   | -25.10%            | -45.63% |     0.53 |       64 | 54.41%     | ok               |
|          30 | 16.03%   | -25.10%            | -53.87% |     0.38 |       74 | 49.23%     | ok               |
|          25 | 15.81%   | -25.10%            | -51.09% |     0.38 |       68 | 50.77%     | ok               |
|          35 | 0.88%    | -25.10%            | -57.99% |     0.22 |       70 | 45.79%     | ok               |

## BITO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -5.43%   | -58.74%            | -31.98% |     0.06 |       54 | 25.79%     | ok               |
|          30 | -19.66%  | -58.74%            | -43.10% |    -0.09 |       79 | 42.43%     | ok               |
|          45 | -18.46%  | -58.74%            | -34.92% |    -0.14 |       60 | 29.28%     | ok               |
|          15 | -28.31%  | -58.74%            | -51.47% |    -0.17 |       86 | 50.42%     | ok               |
|          40 | -22.68%  | -58.74%            | -40.13% |    -0.19 |       62 | 33.61%     | ok               |

## BLK Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | -8.12%   | 31.90%             | -20.79% |    -0.17 |       92 | 44.09%     | ok               |
|          20 | -11.21%  | 31.90%             | -21.48% |    -0.22 |       88 | 52.58%     | ok               |
|          40 | -9.35%   | 31.90%             | -22.83% |    -0.22 |       80 | 39.27%     | ok               |
|          25 | -12.48%  | 31.90%             | -24.62% |    -0.27 |       81 | 50.42%     | ok               |
|          30 | -16.54%  | 31.90%             | -26.90% |    -0.41 |       85 | 47.92%     | ok               |

## BND Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -6.43%   | -2.46%             | -10.08% |    -0.9  |       64 | 40.60%     | ok               |
|          25 | -7.07%   | -2.46%             | -11.14% |    -1.03 |       67 | 38.60%     | ok               |
|          30 | -6.80%   | -2.46%             | -10.79% |    -1.03 |       65 | 35.61%     | ok               |
|          15 | -8.13%   | -2.46%             | -11.40% |    -1.13 |       75 | 43.26%     | ok               |
|          40 | -7.87%   | -2.46%             | -11.70% |    -1.32 |       64 | 29.62%     | ok               |

## BONK-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 156.03%  | -80.05%            | -35.57% |     1.2  |       42 | 21.46%     | ok               |
|          45 | 69.26%   | -80.05%            | -42.36% |     0.75 |       66 | 27.78%     | ok               |
|          15 | 56.58%   | -80.05%            | -63.45% |     0.65 |       70 | 60.15%     | ok               |
|          20 | 45.19%   | -80.05%            | -55.43% |     0.6  |       68 | 56.13%     | ok               |
|          40 | 38.07%   | -80.05%            | -50.07% |     0.55 |       56 | 37.36%     | ok               |

## BTC-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 53.60%   | -14.99%            | -14.50% |     1    |       44 | 36.40%     | ok               |
|          45 | 48.80%   | -14.99%            | -12.20% |     0.96 |       42 | 32.38%     | ok               |
|          35 | 52.53%   | -14.99%            | -21.56% |     0.94 |       62 | 42.72%     | ok               |
|          30 | 26.09%   | -14.99%            | -21.75% |     0.55 |       68 | 48.66%     | ok               |
|          50 | 17.85%   | -14.99%            | -20.63% |     0.49 |       42 | 26.82%     | ok               |

## C Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -12.28%  | 99.69%             | -21.80% |    -0.29 |       66 | 31.78%     | ok               |
|          45 | -22.75%  | 99.69%             | -29.60% |    -0.58 |       74 | 35.94%     | ok               |
|          25 | -31.93%  | 99.69%             | -36.44% |    -0.66 |       69 | 48.42%     | ok               |
|          40 | -28.17%  | 99.69%             | -35.11% |    -0.7  |       74 | 38.27%     | ok               |
|          15 | -35.92%  | 99.69%             | -38.43% |    -0.71 |       74 | 55.41%     | ok               |

## CAT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 18.06%   | 127.01%            | -22.00% |     0.39 |       73 | 61.23%     | ok               |
|          25 | 13.78%   | 127.01%            | -22.20% |     0.34 |       66 | 51.08%     | ok               |
|          45 | 7.08%    | 127.01%            | -24.37% |     0.24 |       54 | 37.10%     | ok               |
|          30 | 6.23%    | 127.01%            | -22.01% |     0.23 |       70 | 48.75%     | ok               |
|          20 | 4.54%    | 127.01%            | -24.56% |     0.2  |       76 | 54.24%     | ok               |

## CL Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -1.87%   | -6.80%             | -12.98% |    -0.03 |       42 | 22.80%     | ok               |
|          30 | -5.50%   | -6.80%             | -14.32% |    -0.13 |       64 | 38.94%     | ok               |
|          45 | -7.56%   | -6.80%             | -13.51% |    -0.26 |       48 | 25.62%     | ok               |
|          35 | -9.27%   | -6.80%             | -15.34% |    -0.28 |       64 | 35.11%     | ok               |
|          15 | -13.98%  | -6.80%             | -18.95% |    -0.37 |       64 | 47.25%     | ok               |

## CMCSA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -17.59%  | -42.52%            | -28.41% |    -0.57 |       46 | 16.47%     | ok               |
|          15 | -36.01%  | -42.52%            | -47.11% |    -0.76 |       89 | 57.24%     | ok               |
|          45 | -24.27%  | -42.52%            | -35.13% |    -0.77 |       62 | 20.80%     | ok               |
|          30 | -35.83%  | -42.52%            | -46.50% |    -0.86 |       82 | 42.60%     | ok               |
|          40 | -32.02%  | -42.52%            | -42.51% |    -0.87 |       89 | 28.29%     | ok               |

## COMP-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 4.77%    | -39.17%            | -38.71% |     0.26 |       48 | 24.52%     | ok               |
|          30 | -35.33%  | -39.17%            | -55.77% |    -0.17 |       95 | 49.23%     | ok               |
|          25 | -41.84%  | -39.17%            | -54.62% |    -0.25 |       94 | 57.28%     | ok               |
|          15 | -47.51%  | -39.17%            | -54.29% |    -0.32 |       98 | 67.62%     | ok               |
|          40 | -43.07%  | -39.17%            | -53.14% |    -0.38 |       70 | 37.74%     | ok               |

## COP Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -10.92%  | 11.98%             | -34.61% |    -0.16 |       46 | 27.29%     | ok               |
|          35 | -17.48%  | 11.98%             | -44.07% |    -0.26 |       71 | 40.77%     | ok               |
|          30 | -19.25%  | 11.98%             | -43.40% |    -0.29 |       68 | 43.59%     | ok               |
|          45 | -17.92%  | 11.98%             | -41.10% |    -0.32 |       62 | 31.45%     | ok               |
|          40 | -25.21%  | 11.98%             | -47.54% |    -0.5  |       74 | 35.11%     | ok               |

## COST Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 11.66%   | 19.53%             | -24.32% |     0.4  |       62 | 47.25%     | ok               |
|          25 | 8.00%    | 19.53%             | -24.93% |     0.31 |       59 | 44.26%     | ok               |
|          35 | 3.03%    | 19.53%             | -29.78% |     0.16 |       56 | 38.94%     | ok               |
|          30 | -1.32%   | 19.53%             | -30.95% |     0.02 |       58 | 41.43%     | ok               |
|          15 | -3.47%   | 19.53%             | -27.30% |    -0.02 |       67 | 50.92%     | ok               |

## CRM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | -22.78%  | -19.98%            | -34.06% |    -0.28 |       62 | 41.26%     | ok               |
|          40 | -25.67%  | -19.98%            | -39.44% |    -0.37 |       68 | 37.10%     | ok               |
|          50 | -22.09%  | -19.98%            | -38.38% |    -0.4  |       58 | 24.63%     | ok               |
|          15 | -33.60%  | -19.98%            | -47.54% |    -0.41 |       88 | 57.57%     | ok               |
|          30 | -34.52%  | -19.98%            | -45.50% |    -0.51 |       65 | 45.92%     | ok               |

## CRV-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 61.29%   | -48.69%            | -37.78% |     0.72 |       66 | 33.14%     | ok               |
|          40 | 46.92%   | -48.69%            | -38.86% |     0.63 |       54 | 28.93%     | ok               |
|          45 | 36.80%   | -48.69%            | -42.29% |     0.56 |       54 | 22.22%     | ok               |
|          50 | 35.87%   | -48.69%            | -30.73% |     0.56 |       46 | 18.20%     | ok               |
|          30 | 29.63%   | -48.69%            | -39.89% |     0.49 |       66 | 37.74%     | ok               |

## CSCO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 32.58%   | 137.67%            | -19.34% |     0.69 |       50 | 37.60%     | ok               |
|          45 | 28.10%   | 137.67%            | -19.34% |     0.6  |       52 | 39.27%     | ok               |
|          25 | 23.26%   | 137.67%            | -23.28% |     0.5  |       61 | 50.08%     | ok               |
|          20 | 17.73%   | 137.67%            | -22.72% |     0.41 |       71 | 52.41%     | ok               |
|          30 | 16.78%   | 137.67%            | -21.79% |     0.4  |       64 | 48.75%     | ok               |

## CVX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -9.60%   | 31.32%             | -23.80% |    -0.17 |       73 | 44.59%     | ok               |
|          40 | -10.08%  | 31.32%             | -27.34% |    -0.22 |       73 | 36.61%     | ok               |
|          45 | -10.48%  | 31.32%             | -28.83% |    -0.24 |       65 | 33.28%     | ok               |
|          50 | -10.36%  | 31.32%             | -30.69% |    -0.29 |       58 | 28.79%     | ok               |
|          35 | -13.01%  | 31.32%             | -28.85% |    -0.29 |       67 | 38.60%     | ok               |

## DASH-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 156.61%  | 140.84%            | -33.55% |     1.01 |       38 | 18.01%     | ok               |
|          40 | 107.73%  | 140.84%            | -33.20% |     0.83 |       44 | 24.52%     | ok               |
|          45 | 78.66%   | 140.84%            | -37.63% |     0.72 |       44 | 20.69%     | ok               |
|          30 | -9.06%   | 140.84%            | -64.43% |     0.33 |       57 | 30.84%     | ok               |
|          25 | -12.04%  | 140.84%            | -64.14% |     0.31 |       65 | 33.14%     | ok               |

## DBC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 0.41%    | 40.22%             | -25.67% |     0.08 |       77 | 41.10%     | ok               |
|          20 | -4.00%   | 40.22%             | -25.31% |    -0.06 |       69 | 39.43%     | ok               |
|          25 | -5.28%   | 40.22%             | -24.84% |    -0.11 |       66 | 37.60%     | ok               |
|          50 | -6.09%   | 40.22%             | -19.34% |    -0.18 |       50 | 24.96%     | ok               |
|          35 | -7.76%   | 40.22%             | -23.19% |    -0.2  |       66 | 34.28%     | ok               |

## DE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 2.13%    | 65.45%             | -17.97% |     0.13 |       56 | 29.62%     | ok               |
|          45 | -4.48%   | 65.45%             | -19.53% |    -0.02 |       60 | 34.11%     | ok               |
|          20 | -7.80%   | 65.45%             | -24.11% |    -0.07 |       65 | 48.59%     | ok               |
|          25 | -12.03%  | 65.45%             | -24.29% |    -0.17 |       71 | 46.92%     | ok               |
|          30 | -12.17%  | 65.45%             | -23.98% |    -0.18 |       70 | 44.26%     | ok               |

## DIA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -5.77%   | 28.17%             | -11.28% |    -0.28 |       58 | 44.93%     | ok               |
|          35 | -6.49%   | 28.17%             | -13.15% |    -0.34 |       66 | 40.77%     | ok               |
|          30 | -7.90%   | 28.17%             | -12.94% |    -0.41 |       64 | 43.76%     | ok               |
|          20 | -8.49%   | 28.17%             | -13.72% |    -0.42 |       64 | 46.92%     | ok               |
|          40 | -9.59%   | 28.17%             | -15.06% |    -0.55 |       70 | 37.77%     | ok               |

## DIS Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 33.83%   | 3.53%              | -10.17% |     1.05 |       44 | 25.46%     | ok               |
|          40 | 8.18%    | 3.53%              | -18.75% |     0.28 |       57 | 33.78%     | ok               |
|          45 | 3.62%    | 3.53%              | -16.54% |     0.17 |       45 | 29.12%     | ok               |
|          35 | -4.01%   | 3.53%              | -25.70% |    -0    |       71 | 39.77%     | ok               |
|          15 | -5.96%   | 3.53%              | -32.73% |    -0.02 |       83 | 54.58%     | ok               |

## DOGE-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -0.18%   | -50.46%            | -57.89% |     0.28 |       74 | 64.18%     | ok               |
|          20 | -7.87%   | -50.46%            | -55.83% |     0.19 |       76 | 58.81%     | ok               |
|          25 | -14.47%  | -50.46%            | -53.72% |     0.12 |       68 | 54.98%     | ok               |
|          30 | -33.52%  | -50.46%            | -60.95% |    -0.14 |       73 | 48.47%     | ok               |
|          50 | -36.84%  | -50.46%            | -55.41% |    -0.37 |       64 | 24.52%     | ok               |

## DOT-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -55.64%  | -70.72%            | -72.06% |    -0.36 |       77 | 63.98%     | ok               |
|          20 | -52.57%  | -70.72%            | -66.32% |    -0.37 |       89 | 59.96%     | ok               |
|          30 | -57.53%  | -70.72%            | -63.33% |    -0.54 |       88 | 48.85%     | ok               |
|          25 | -59.89%  | -70.72%            | -69.99% |    -0.54 |       80 | 54.98%     | ok               |
|          35 | -61.72%  | -70.72%            | -63.01% |    -0.67 |       86 | 43.30%     | ok               |

## DXY-INDEX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd    |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:-------|---------:|---------:|:-----------|:-----------------|
|          50 | -0.69%   | -3.91%             | -6.02% |    -0.1  |       40 | 31.17%     | ok               |
|          40 | -1.59%   | -3.91%             | -7.30% |    -0.19 |       66 | 46.97%     | ok               |
|          45 | -2.05%   | -3.91%             | -8.14% |    -0.27 |       60 | 37.23%     | ok               |
|          30 | -4.32%   | -3.91%             | -9.83% |    -0.51 |       74 | 57.58%     | ok               |
|          35 | -4.48%   | -3.91%             | -9.97% |    -0.56 |       77 | 52.60%     | ok               |

## EEM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -8.28%   | 51.61%             | -15.88% |    -0.25 |       54 | 33.11%     | ok               |
|          35 | -9.58%   | 51.61%             | -23.57% |    -0.26 |       66 | 38.77%     | ok               |
|          45 | -8.61%   | 51.61%             | -17.03% |    -0.26 |       52 | 34.61%     | ok               |
|          40 | -8.95%   | 51.61%             | -19.20% |    -0.26 |       64 | 36.77%     | ok               |
|          30 | -12.79%  | 51.61%             | -25.38% |    -0.37 |       62 | 40.60%     | ok               |

## EFA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -3.53%   | 26.23%             | -10.10% |    -0.07 |       64 | 51.25%     | ok               |
|          20 | -10.52%  | 26.23%             | -13.73% |    -0.37 |       71 | 48.42%     | ok               |
|          30 | -10.98%  | 26.23%             | -12.96% |    -0.42 |       64 | 41.76%     | ok               |
|          25 | -12.17%  | 26.23%             | -15.23% |    -0.46 |       68 | 45.09%     | ok               |
|          40 | -11.85%  | 26.23%             | -14.70% |    -0.51 |       62 | 37.10%     | ok               |

## EOG Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -17.66%  | 16.10%             | -35.34% |    -0.37 |       54 | 30.62%     | ok               |
|          50 | -22.19%  | 16.10%             | -35.63% |    -0.53 |       50 | 27.79%     | ok               |
|          40 | -23.88%  | 16.10%             | -37.39% |    -0.54 |       70 | 34.61%     | ok               |
|          35 | -27.88%  | 16.10%             | -41.05% |    -0.64 |       83 | 39.60%     | ok               |
|          30 | -30.38%  | 16.10%             | -47.87% |    -0.66 |       78 | 44.76%     | ok               |

## ETC-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -0.26%   | -48.84%            | -28.33% |     0.13 |       26 | 18.01%     | ok               |
|          45 | -0.82%   | -48.84%            | -35.44% |     0.13 |       26 | 20.31%     | ok               |
|          40 | -12.94%  | -48.84%            | -40.48% |    -0.07 |       36 | 23.37%     | ok               |
|          35 | -15.30%  | -48.84%            | -42.62% |    -0.09 |       40 | 26.82%     | ok               |
|          30 | -20.80%  | -48.84%            | -45.54% |    -0.17 |       56 | 30.65%     | ok               |

## ETH-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 178.93%  | 37.04%             | -30.11% |     1.44 |       58 | 48.85%     | ok               |
|          30 | 135.30%  | 37.04%             | -32.89% |     1.19 |       60 | 56.51%     | ok               |
|          25 | 92.62%   | 37.04%             | -40.90% |     0.95 |       60 | 60.34%     | ok               |
|          20 | 75.48%   | 37.04%             | -39.10% |     0.83 |       78 | 64.18%     | ok               |
|          40 | 60.51%   | 37.04%             | -33.11% |     0.81 |       62 | 40.80%     | ok               |

## EWJ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -22.99%  | 42.55%             | -29.40% |    -0.8  |       62 | 36.44%     | ok               |
|          20 | -23.95%  | 42.55%             | -30.00% |    -0.81 |       56 | 38.44%     | ok               |
|          25 | -25.82%  | 42.55%             | -29.85% |    -0.9  |       56 | 37.60%     | ok               |
|          15 | -27.60%  | 42.55%             | -31.15% |    -0.9  |       67 | 41.76%     | ok               |
|          45 | -23.95%  | 42.55%             | -27.68% |    -0.98 |       58 | 28.12%     | ok               |

## FCX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 2.51%    | 36.70%             | -29.27% |     0.18 |       50 | 31.61%     | ok               |
|          50 | -0.09%   | 36.70%             | -26.57% |     0.13 |       52 | 27.95%     | ok               |
|          40 | -10.00%  | 36.70%             | -42.89% |    -0.01 |       62 | 36.94%     | ok               |
|          30 | -29.37%  | 36.70%             | -46.84% |    -0.32 |       65 | 44.26%     | ok               |
|          35 | -29.20%  | 36.70%             | -50.12% |    -0.34 |       67 | 42.10%     | ok               |

## FET-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -26.95%  | -67.31%            | -64.89% |     0.04 |       88 | 51.92%     | ok               |
|          15 | -28.87%  | -67.31%            | -59.58% |     0.04 |       82 | 56.51%     | ok               |
|          25 | -36.37%  | -67.31%            | -65.31% |    -0.1  |       81 | 46.36%     | ok               |
|          30 | -48.46%  | -67.31%            | -61.24% |    -0.33 |       79 | 41.95%     | ok               |
|          50 | -39.06%  | -67.31%            | -45.19% |    -0.53 |       46 | 14.37%     | ok               |

## FIL-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -41.87%  | -58.48%            | -57.60% |    -0.48 |       50 | 26.25%     | ok               |
|          30 | -47.64%  | -58.48%            | -58.54% |    -0.5  |       65 | 36.78%     | ok               |
|          35 | -51.16%  | -58.48%            | -61.90% |    -0.64 |       60 | 30.65%     | ok               |
|          15 | -63.58%  | -58.48%            | -71.82% |    -0.71 |       91 | 48.66%     | ok               |
|          50 | -46.43%  | -58.48%            | -47.18% |    -0.74 |       38 | 15.52%     | ok               |

## FXI Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -10.01%  | 14.71%             | -22.99% |    -0.17 |       52 | 33.28%     | ok               |
|          15 | -10.85%  | 14.71%             | -21.68% |    -0.18 |       54 | 37.27%     | ok               |
|          30 | -10.27%  | 14.71%             | -24.33% |    -0.18 |       50 | 31.78%     | ok               |
|          20 | -13.44%  | 14.71%             | -24.94% |    -0.26 |       54 | 35.11%     | ok               |
|          35 | -13.74%  | 14.71%             | -27.93% |    -0.29 |       52 | 29.28%     | ok               |

## GDX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 2.77%    | 143.19%            | -33.01% |     0.19 |       76 | 49.75%     | ok               |
|          40 | 2.77%    | 143.19%            | -28.47% |     0.17 |       60 | 38.44%     | ok               |
|          35 | -3.17%   | 143.19%            | -31.73% |     0.08 |       68 | 41.10%     | ok               |
|          30 | -3.80%   | 143.19%            | -33.31% |     0.07 |       60 | 44.43%     | ok               |
|          25 | -9.78%   | 143.19%            | -38.90% |    -0.02 |       66 | 45.76%     | ok               |

## GDXJ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -26.53%  | 150.45%            | -42.33% |    -0.22 |       74 | 49.75%     | ok               |
|          50 | -26.62%  | 150.45%            | -46.83% |    -0.35 |       58 | 34.28%     | ok               |
|          35 | -35.65%  | 150.45%            | -38.56% |    -0.48 |       70 | 40.10%     | ok               |
|          30 | -37.43%  | 150.45%            | -41.57% |    -0.5  |       70 | 42.76%     | ok               |
|          40 | -36.85%  | 150.45%            | -44.70% |    -0.55 |       64 | 37.77%     | ok               |

## GE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 4.89%    | 89.68%             | -21.25% |     0.2  |       60 | 33.78%     | ok               |
|          45 | -2.34%   | 89.68%             | -21.88% |     0.05 |       70 | 36.44%     | ok               |
|          30 | -8.43%   | 89.68%             | -27.82% |    -0.04 |       76 | 48.09%     | ok               |
|          20 | -9.10%   | 89.68%             | -25.05% |    -0.05 |       73 | 52.58%     | ok               |
|          35 | -8.71%   | 89.68%             | -27.11% |    -0.06 |       74 | 41.93%     | ok               |

## GLD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | 15.51%   | 72.08%             | -13.87% |     0.43 |       48 | 46.59%     | ok               |
|          20 | 13.94%   | 72.08%             | -13.87% |     0.4  |       49 | 48.25%     | ok               |
|          30 | 10.01%   | 72.08%             | -13.87% |     0.32 |       50 | 45.42%     | ok               |
|          35 | 7.10%    | 72.08%             | -14.65% |     0.25 |       52 | 43.09%     | ok               |
|          15 | 3.47%    | 72.08%             | -17.63% |     0.17 |       57 | 51.58%     | ok               |

## GOOGL Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 60.98%   | 99.96%             | -17.38% |     1.08 |       57 | 43.76%     | ok               |
|          30 | 57.09%   | 99.96%             | -17.15% |     1.01 |       55 | 47.25%     | ok               |
|          45 | 49.53%   | 99.96%             | -11.66% |     0.99 |       50 | 37.27%     | ok               |
|          25 | 54.69%   | 99.96%             | -16.48% |     0.96 |       55 | 49.75%     | ok               |
|          50 | 43.13%   | 99.96%             | -11.52% |     0.92 |       46 | 32.45%     | ok               |

## GRT-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 58.92%   | -70.09%            | -42.58% |     0.67 |       70 | 62.45%     | ok               |
|          20 | 38.19%   | -70.09%            | -40.19% |     0.55 |       77 | 56.70%     | ok               |
|          50 | 33.06%   | -70.09%            | -30.80% |     0.55 |       44 | 21.07%     | ok               |
|          45 | 33.45%   | -70.09%            | -44.68% |     0.54 |       46 | 27.97%     | ok               |
|          25 | 21.99%   | -70.09%            | -44.66% |     0.44 |       78 | 52.30%     | ok               |

## GS Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 22.60%   | 90.00%             | -20.56% |     0.5  |       68 | 56.41%     | ok               |
|          20 | 3.77%    | 90.00%             | -23.19% |     0.18 |       68 | 53.08%     | ok               |
|          40 | 2.63%    | 90.00%             | -17.88% |     0.15 |       68 | 42.43%     | ok               |
|          25 | -1.49%   | 90.00%             | -23.32% |     0.07 |       68 | 50.58%     | ok               |
|          30 | -3.64%   | 90.00%             | -22.13% |     0.02 |       70 | 48.09%     | ok               |

## HBAR-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -18.60%  | -10.29%            | -39.26% |    -0.27 |       18 | 18.22%     | ok               |
|          45 | -33.67%  | -10.29%            | -48.27% |    -0.7  |       22 | 24.42%     | ok               |
|          40 | -36.66%  | -10.29%            | -50.61% |    -0.78 |       26 | 29.07%     | ok               |
|          15 | -43.32%  | -10.29%            | -56.87% |    -0.92 |       51 | 51.16%     | ok               |
|          30 | -44.08%  | -10.29%            | -56.39% |    -0.99 |       38 | 37.60%     | ok               |

## HD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 2.94%    | -13.79%            | -17.15% |     0.16 |       65 | 43.26%     | ok               |
|          35 | 2.06%    | -13.79%            | -17.81% |     0.13 |       68 | 39.43%     | ok               |
|          40 | 1.06%    | -13.79%            | -16.74% |     0.1  |       72 | 34.78%     | ok               |
|          25 | 0.34%    | -13.79%            | -18.17% |     0.09 |       64 | 45.42%     | ok               |
|          45 | 0.27%    | -13.79%            | -17.41% |     0.07 |       48 | 29.95%     | ok               |

## HON Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -12.81%  | 1.16%              | -20.92% |    -0.34 |       70 | 33.61%     | ok               |
|          45 | -16.45%  | 1.16%              | -22.88% |    -0.43 |       72 | 39.10%     | ok               |
|          35 | -26.20%  | 1.16%              | -31.30% |    -0.68 |       89 | 50.42%     | ok               |
|          30 | -28.13%  | 1.16%              | -33.03% |    -0.71 |       89 | 55.07%     | ok               |
|          40 | -26.51%  | 1.16%              | -31.84% |    -0.72 |       76 | 43.43%     | ok               |

## HYG Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -5.21%   | -0.17%             | -7.93%  |    -0.6  |       68 | 32.95%     | ok               |
|          45 | -6.38%   | -0.17%             | -9.07%  |    -0.77 |       68 | 29.62%     | ok               |
|          35 | -7.09%   | -0.17%             | -9.76%  |    -0.82 |       79 | 34.78%     | ok               |
|          30 | -7.30%   | -0.17%             | -10.59% |    -0.82 |       87 | 38.10%     | ok               |
|          25 | -7.72%   | -0.17%             | -11.22% |    -0.84 |       89 | 40.93%     | ok               |

## IBIT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 65.04%   | 21.70%             | -19.20% |     0.95 |       44 | 41.51%     | ok               |
|          50 | 52.39%   | 21.70%             | -17.37% |     0.94 |       26 | 25.77%     | ok               |
|          45 | 43.01%   | 21.70%             | -17.37% |     0.8  |       30 | 26.99%     | ok               |
|          40 | 36.61%   | 21.70%             | -17.78% |     0.71 |       30 | 28.83%     | ok               |
|          30 | 37.60%   | 21.70%             | -18.95% |     0.69 |       38 | 34.76%     | ok               |

## IBM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -17.98%  | 34.11%             | -49.43% |    -0.12 |       83 | 61.40%     | ok               |
|          35 | -21.42%  | 34.11%             | -47.10% |    -0.23 |       63 | 45.92%     | ok               |
|          30 | -24.27%  | 34.11%             | -48.94% |    -0.28 |       69 | 49.92%     | ok               |
|          20 | -29.75%  | 34.11%             | -53.45% |    -0.36 |       69 | 54.41%     | ok               |
|          45 | -28.12%  | 34.11%             | -48.72% |    -0.4  |       52 | 37.44%     | ok               |

## ICP-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | -1.32%   | -34.30%            | -46.78% |     0.2  |       68 | 33.33%     | ok               |
|          40 | -2.01%   | -34.30%            | -40.71% |     0.18 |       60 | 28.54%     | ok               |
|          30 | -8.32%   | -34.30%            | -46.42% |     0.18 |       77 | 39.27%     | ok               |
|          15 | -37.72%  | -34.30%            | -58.26% |    -0.05 |       77 | 50.19%     | ok               |
|          50 | -19.62%  | -34.30%            | -53.37% |    -0.09 |       42 | 18.39%     | ok               |

## IEF Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -6.58%   | -4.23%             | -10.18% |    -0.77 |       72 | 42.26%     | ok               |
|          15 | -7.14%   | -4.23%             | -10.91% |    -0.83 |       71 | 43.76%     | ok               |
|          50 | -7.25%   | -4.23%             | -9.11%  |    -1.22 |       58 | 22.46%     | ok               |
|          40 | -8.60%   | -4.23%             | -11.24% |    -1.25 |       64 | 27.62%     | ok               |
|          25 | -10.15%  | -4.23%             | -11.95% |    -1.28 |       76 | 39.60%     | ok               |

## IEMG Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -3.88%   | 47.22%             | -14.22% |    -0.1  |       54 | 31.95%     | ok               |
|          45 | -4.67%   | 47.22%             | -15.23% |    -0.12 |       50 | 34.44%     | ok               |
|          40 | -6.14%   | 47.22%             | -18.73% |    -0.17 |       62 | 37.44%     | ok               |
|          35 | -7.53%   | 47.22%             | -24.06% |    -0.2  |       65 | 39.77%     | ok               |
|          25 | -11.60%  | 47.22%             | -27.42% |    -0.34 |       60 | 42.60%     | ok               |

## INJ-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 7.83%    | -23.31%            | -52.64% |     0.32 |       58 | 36.40%     | ok               |
|          40 | -0.33%   | -23.31%            | -47.89% |     0.23 |       50 | 33.33%     | ok               |
|          45 | -6.35%   | -23.31%            | -47.58% |     0.15 |       54 | 27.59%     | ok               |
|          30 | -23.82%  | -23.31%            | -69.96% |     0.01 |       63 | 39.85%     | ok               |
|          15 | -31.67%  | -23.31%            | -74.54% |    -0    |       74 | 51.34%     | ok               |

## INTC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 70.01%   | 234.31%            | -49.32% |     0.71 |       56 | 33.78%     | ok               |
|          50 | 64.73%   | 234.31%            | -48.35% |     0.68 |       60 | 29.95%     | ok               |
|          15 | 62.83%   | 234.31%            | -53.65% |     0.64 |       78 | 59.90%     | ok               |
|          40 | 51.41%   | 234.31%            | -55.86% |     0.6  |       64 | 37.94%     | ok               |
|          25 | 46.52%   | 234.31%            | -56.41% |     0.56 |       77 | 50.75%     | ok               |

## INTU Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 10.17%   | -53.49%            | -34.75% |     0.29 |       65 | 28.45%     | ok               |
|          45 | -1.24%   | -53.49%            | -40.30% |     0.1  |       65 | 32.78%     | ok               |
|          40 | -7.55%   | -53.49%            | -43.67% |    -0.01 |       69 | 36.61%     | ok               |
|          25 | -11.92%  | -53.49%            | -37.85% |    -0.06 |       70 | 49.25%     | ok               |
|          35 | -13.17%  | -53.49%            | -45.88% |    -0.11 |       71 | 40.27%     | ok               |

## ITA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -0.98%   | 51.83%             | -28.17% |     0.07 |       82 | 61.06%     | ok               |
|          50 | -0.52%   | 51.83%             | -21.48% |     0.05 |       76 | 37.44%     | ok               |
|          30 | -2.95%   | 51.83%             | -23.75% |    -0    |       74 | 48.92%     | ok               |
|          20 | -7.30%   | 51.83%             | -28.17% |    -0.11 |       84 | 55.07%     | ok               |
|          40 | -6.13%   | 51.83%             | -20.58% |    -0.12 |       76 | 42.43%     | ok               |

## IWM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | 10.82%   | 33.49%             | -11.96% |     0.44 |       52 | 35.44%     | ok               |
|          20 | 9.35%    | 33.49%             | -11.74% |     0.38 |       58 | 36.44%     | ok               |
|          30 | 7.12%    | 33.49%             | -12.28% |     0.31 |       54 | 34.78%     | ok               |
|          40 | 6.17%    | 33.49%             | -13.56% |     0.3  |       46 | 30.12%     | ok               |
|          15 | 6.00%    | 33.49%             | -13.42% |     0.26 |       76 | 42.26%     | ok               |

## JNJ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 17.23%   | 66.24%             | -10.57% |     0.7  |       42 | 34.94%     | ok               |
|          15 | 11.16%   | 66.24%             | -17.37% |     0.42 |       60 | 53.74%     | ok               |
|          20 | 6.02%    | 66.24%             | -16.96% |     0.26 |       66 | 50.25%     | ok               |
|          45 | 4.86%    | 66.24%             | -13.35% |     0.24 |       48 | 38.77%     | ok               |
|          30 | 4.76%    | 66.24%             | -16.86% |     0.23 |       64 | 46.92%     | ok               |

## JPM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 2.52%    | 63.69%             | -15.90% |     0.15 |       50 | 33.61%     | ok               |
|          45 | -7.70%   | 63.69%             | -21.91% |    -0.18 |       54 | 36.27%     | ok               |
|          20 | -22.65%  | 63.69%             | -35.58% |    -0.49 |       86 | 49.75%     | ok               |
|          35 | -19.73%  | 63.69%             | -27.43% |    -0.55 |       74 | 42.10%     | ok               |
|          40 | -20.37%  | 63.69%             | -28.47% |    -0.58 |       66 | 38.94%     | ok               |

## KO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 22.60%   | 38.61%             | -8.64%  |     0.81 |       54 | 37.44%     | ok               |
|          35 | 18.43%   | 38.61%             | -8.21%  |     0.69 |       58 | 35.94%     | ok               |
|          40 | 15.58%   | 38.61%             | -9.28%  |     0.63 |       60 | 32.61%     | ok               |
|          25 | 16.46%   | 38.61%             | -10.16% |     0.61 |       60 | 40.27%     | ok               |
|          20 | 3.61%    | 38.61%             | -15.99% |     0.18 |       77 | 44.43%     | ok               |

## LDO-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 48.36%   | -45.24%            | -39.66% |     0.61 |       78 | 60.15%     | ok               |
|          20 | 34.97%   | -45.24%            | -42.94% |     0.54 |       80 | 55.36%     | ok               |
|          30 | 10.52%   | -45.24%            | -59.02% |     0.37 |       72 | 46.93%     | ok               |
|          25 | 5.26%    | -45.24%            | -54.79% |     0.34 |       81 | 52.49%     | ok               |
|          35 | -7.24%   | -45.24%            | -61.76% |     0.19 |       78 | 39.46%     | ok               |

## LIN Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -9.98%   | 12.10%             | -23.00% |    -0.29 |       68 | 43.93%     | ok               |
|          25 | -9.88%   | 12.10%             | -22.01% |    -0.29 |       73 | 40.77%     | ok               |
|          15 | -10.60%  | 12.10%             | -23.68% |    -0.3  |       72 | 47.75%     | ok               |
|          30 | -12.89%  | 12.10%             | -20.61% |    -0.42 |       74 | 37.94%     | ok               |
|          45 | -11.58%  | 12.10%             | -17.04% |    -0.46 |       48 | 21.63%     | ok               |

## LINK-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 31.69%   | -6.83%             | -33.71% |     0.53 |       54 | 32.76%     | ok               |
|          30 | 31.57%   | -6.83%             | -33.64% |     0.52 |       69 | 46.55%     | ok               |
|          35 | 10.09%   | -6.83%             | -34.21% |     0.33 |       63 | 42.53%     | ok               |
|          50 | 10.71%   | -6.83%             | -27.92% |     0.32 |       48 | 26.82%     | ok               |
|          40 | 2.97%    | -6.83%             | -34.00% |     0.24 |       59 | 36.97%     | ok               |

## LLY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -1.73%   | 51.68%             | -38.23% |     0.07 |       50 | 35.44%     | ok               |
|          15 | -13.89%  | 51.68%             | -48.12% |    -0.08 |       70 | 60.40%     | ok               |
|          45 | -14.54%  | 51.68%             | -42.66% |    -0.18 |       58 | 38.94%     | ok               |
|          20 | -27.64%  | 51.68%             | -51.34% |    -0.37 |       77 | 55.41%     | ok               |
|          40 | -25.40%  | 51.68%             | -46.23% |    -0.39 |       68 | 41.93%     | ok               |

## LRCX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -18.72%  | 240.00%            | -48.71% |    -0.1  |       74 | 33.78%     | ok               |
|          40 | -22.35%  | 240.00%            | -55.33% |    -0.12 |       70 | 39.60%     | ok               |
|          15 | -27.77%  | 240.00%            | -55.17% |    -0.13 |       77 | 50.25%     | ok               |
|          35 | -23.85%  | 240.00%            | -58.47% |    -0.13 |       78 | 41.76%     | ok               |
|          30 | -27.92%  | 240.00%            | -60.58% |    -0.2  |       80 | 42.26%     | ok               |

## LTC-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 19.88%   | -30.15%            | -36.44% |     0.43 |       56 | 36.97%     | ok               |
|          35 | 17.11%   | -30.15%            | -34.94% |     0.39 |       66 | 46.55%     | ok               |
|          30 | 12.78%   | -30.15%            | -32.66% |     0.35 |       67 | 53.83%     | ok               |
|          25 | 8.74%    | -30.15%            | -34.22% |     0.3  |       69 | 56.13%     | ok               |
|          15 | -4.48%   | -30.15%            | -46.99% |     0.17 |       79 | 64.37%     | ok               |

## MCD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 10.18%   | -13.39%            | -9.22%  |     0.48 |       46 | 24.96%     | ok               |
|          45 | 0.88%    | -13.39%            | -16.79% |     0.09 |       54 | 28.79%     | ok               |
|          40 | -0.06%   | -13.39%            | -18.49% |     0.05 |       67 | 32.28%     | ok               |
|          30 | -0.55%   | -13.39%            | -21.88% |     0.04 |       77 | 40.27%     | ok               |
|          25 | -1.10%   | -13.39%            | -23.62% |     0.02 |       75 | 42.60%     | ok               |

## META Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -8.75%   | 52.33%             | -37.10% |    -0.04 |       66 | 39.77%     | ok               |
|          40 | -15.29%  | 52.33%             | -40.49% |    -0.16 |       68 | 42.93%     | ok               |
|          50 | -18.55%  | 52.33%             | -38.63% |    -0.26 |       68 | 35.44%     | ok               |
|          35 | -25.92%  | 52.33%             | -41.18% |    -0.37 |       81 | 47.75%     | ok               |
|          25 | -27.86%  | 52.33%             | -45.35% |    -0.38 |       75 | 52.91%     | ok               |

## MPC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 34.68%   | 165.11%            | -18.24% |     0.67 |       50 | 40.10%     | ok               |
|          40 | 32.46%   | 165.11%            | -20.11% |     0.61 |       60 | 46.76%     | ok               |
|          45 | 30.14%   | 165.11%            | -19.46% |     0.59 |       56 | 44.09%     | ok               |
|          35 | 29.47%   | 165.11%            | -31.08% |     0.56 |       68 | 49.42%     | ok               |
|          30 | 15.43%   | 165.11%            | -37.91% |     0.36 |       71 | 52.08%     | ok               |

## MRK Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -13.09%  | 8.79%              | -28.39% |    -0.16 |       83 | 51.91%     | ok               |
|          25 | -13.85%  | 8.79%              | -31.07% |    -0.2  |       70 | 44.09%     | ok               |
|          20 | -18.07%  | 8.79%              | -29.34% |    -0.29 |       75 | 47.42%     | ok               |
|          50 | -14.54%  | 8.79%              | -23.01% |    -0.3  |       56 | 28.45%     | ok               |
|          45 | -16.67%  | 8.79%              | -25.38% |    -0.33 |       57 | 31.78%     | ok               |

## MS Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 3.09%    | 88.23%             | -19.99% |     0.16 |       72 | 39.60%     | ok               |
|          15 | -0.85%   | 88.23%             | -22.02% |     0.08 |       74 | 58.24%     | ok               |
|          20 | -3.20%   | 88.23%             | -25.68% |     0.02 |       75 | 53.08%     | ok               |
|          30 | -8.22%   | 88.23%             | -27.79% |    -0.12 |       75 | 48.25%     | ok               |
|          35 | -8.15%   | 88.23%             | -26.58% |    -0.12 |       76 | 44.76%     | ok               |

## MSFT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -15.34%  | 24.14%             | -24.64% |    -0.35 |       74 | 37.10%     | ok               |
|          50 | -20.30%  | 24.14%             | -25.48% |    -0.53 |       64 | 31.45%     | ok               |
|          35 | -24.38%  | 24.14%             | -35.38% |    -0.54 |       75 | 46.09%     | ok               |
|          40 | -24.56%  | 24.14%             | -34.92% |    -0.57 |       73 | 40.93%     | ok               |
|          30 | -27.52%  | 24.14%             | -39.07% |    -0.61 |       85 | 50.75%     | ok               |

## MU Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 164.16%  | 709.95%            | -64.26% |     1.09 |       58 | 48.75%     | ok               |
|          15 | 189.49%  | 709.95%            | -61.96% |     1.08 |       51 | 60.23%     | ok               |
|          30 | 139.60%  | 709.95%            | -68.76% |     0.99 |       51 | 53.24%     | ok               |
|          25 | 138.20%  | 709.95%            | -67.90% |     0.98 |       51 | 54.74%     | ok               |
|          35 | 131.07%  | 709.95%            | -69.35% |     0.97 |       63 | 51.08%     | ok               |

## NEAR-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 161.18%  | 107.77%            | -51.95% |     1.12 |       42 | 31.61%     | ok               |
|          50 | 131.01%  | 107.77%            | -50.61% |     1.05 |       30 | 22.03%     | ok               |
|          45 | 115.11%  | 107.77%            | -45.21% |     0.96 |       44 | 27.39%     | ok               |
|          35 | 111.05%  | 107.77%            | -56.29% |     0.92 |       64 | 36.40%     | ok               |
|          30 | 99.86%   | 107.77%            | -52.00% |     0.86 |       73 | 44.25%     | ok               |

## NEM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 1.74%    | 169.72%            | -31.25% |     0.19 |       61 | 58.74%     | ok               |
|          20 | 0.98%    | 169.72%            | -30.50% |     0.18 |       68 | 54.24%     | ok               |
|          25 | -16.51%  | 169.72%            | -39.51% |    -0.08 |       64 | 52.08%     | ok               |
|          50 | -18.55%  | 169.72%            | -33.24% |    -0.16 |       52 | 38.60%     | ok               |
|          30 | -26.97%  | 169.72%            | -39.56% |    -0.27 |       68 | 50.42%     | ok               |

## NFLX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 37.43%   | 17.23%             | -16.28% |     0.9  |       44 | 33.94%     | ok               |
|          40 | 36.28%   | 17.23%             | -15.02% |     0.82 |       50 | 41.93%     | ok               |
|          35 | 31.67%   | 17.23%             | -18.30% |     0.7  |       74 | 46.59%     | ok               |
|          45 | 24.06%   | 17.23%             | -15.48% |     0.61 |       56 | 38.44%     | ok               |
|          15 | 15.70%   | 17.23%             | -26.59% |     0.38 |       71 | 65.06%     | ok               |

## NKE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -17.96%  | -62.14%            | -49.34% |    -0.12 |       83 | 53.24%     | ok               |
|          35 | -16.18%  | -62.14%            | -42.13% |    -0.15 |       71 | 40.43%     | ok               |
|          25 | -21.36%  | -62.14%            | -51.20% |    -0.18 |       83 | 50.58%     | ok               |
|          15 | -23.25%  | -62.14%            | -54.28% |    -0.21 |       86 | 57.07%     | ok               |
|          30 | -25.11%  | -62.14%            | -55.35% |    -0.26 |       79 | 46.59%     | ok               |

## NOW Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 11.00%   | -7.82%             | -30.43% |     0.3  |       80 | 50.25%     | ok               |
|          20 | 8.52%    | -7.82%             | -39.71% |     0.28 |       75 | 56.57%     | ok               |
|          25 | 5.77%    | -7.82%             | -37.51% |     0.25 |       72 | 53.74%     | ok               |
|          15 | 0.58%    | -7.82%             | -43.06% |     0.19 |       83 | 59.57%     | ok               |
|          40 | 1.48%    | -7.82%             | -36.21% |     0.17 |       72 | 39.77%     | ok               |

## NVDA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -32.81%  | 82.40%             | -41.21% |    -0.47 |       76 | 43.67%     | ok               |
|          20 | -41.75%  | 82.40%             | -42.84% |    -0.57 |       76 | 51.69%     | ok               |
|          25 | -41.65%  | 82.40%             | -42.74% |    -0.62 |       77 | 46.70%     | ok               |
|          15 | -48.05%  | 82.40%             | -52.37% |    -0.67 |       77 | 54.90%     | ok               |
|          35 | -42.92%  | 82.40%             | -48.99% |    -0.75 |       86 | 40.82%     | ok               |

## OP-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 8.48%    | -79.84%            | -31.68% |     0.28 |       32 | 9.58%      | ok               |
|          45 | 4.98%    | -79.84%            | -43.25% |     0.24 |       34 | 14.18%     | ok               |
|          40 | -17.74%  | -79.84%            | -53.61% |    -0.04 |       46 | 22.41%     | ok               |
|          35 | -38.30%  | -79.84%            | -58.13% |    -0.34 |       56 | 27.20%     | ok               |
|          30 | -43.69%  | -79.84%            | -68.74% |    -0.35 |       68 | 33.33%     | ok               |

## ORCL Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 169.78%  | 11.08%             | -32.54% |     1.13 |       69 | 62.40%     | ok               |
|          25 | 116.91%  | 11.08%             | -27.76% |     0.94 |       61 | 54.91%     | ok               |
|          45 | 101.65%  | 11.08%             | -32.35% |     0.93 |       58 | 40.43%     | ok               |
|          35 | 106.64%  | 11.08%             | -31.95% |     0.92 |       62 | 49.08%     | ok               |
|          20 | 110.86%  | 11.08%             | -29.32% |     0.91 |       70 | 58.07%     | ok               |

## OXY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -0.67%   | -4.10%             | -28.48% |     0.11 |       69 | 42.26%     | ok               |
|          35 | -2.70%   | -4.10%             | -26.44% |     0.07 |       72 | 38.10%     | ok               |
|          50 | -6.31%   | -4.10%             | -27.98% |    -0.03 |       44 | 26.96%     | ok               |
|          40 | -8.69%   | -4.10%             | -28.30% |    -0.06 |       62 | 33.94%     | ok               |
|          25 | -14.41%  | -4.10%             | -38.51% |    -0.13 |       77 | 45.76%     | ok               |

## PEP Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 13.80%   | -29.91%            | -11.62% |     0.59 |       40 | 25.62%     | ok               |
|          45 | 6.53%    | -29.91%            | -14.22% |     0.31 |       56 | 29.62%     | ok               |
|          35 | 2.80%    | -29.91%            | -21.42% |     0.15 |       77 | 39.93%     | ok               |
|          40 | 0.58%    | -29.91%            | -18.04% |     0.08 |       70 | 35.27%     | ok               |
|          30 | -1.75%   | -29.91%            | -21.35% |     0.02 |       74 | 45.92%     | ok               |

## PEPE-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -45.46%  | -50.81%            | -61.29% |    -0.24 |       85 | 49.23%     | ok               |
|          25 | -48.73%  | -50.81%            | -61.43% |    -0.27 |       93 | 54.02%     | ok               |
|          15 | -59.12%  | -50.81%            | -67.41% |    -0.32 |       82 | 63.22%     | ok               |
|          20 | -55.12%  | -50.81%            | -64.22% |    -0.33 |       88 | 59.77%     | ok               |
|          35 | -47.31%  | -50.81%            | -61.54% |    -0.35 |       74 | 44.25%     | ok               |

## PFE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -15.89%  | -3.80%             | -23.37% |    -0.5  |       52 | 21.63%     | ok               |
|          40 | -17.46%  | -3.80%             | -27.08% |    -0.53 |       72 | 26.62%     | ok               |
|          50 | -16.36%  | -3.80%             | -25.42% |    -0.57 |       40 | 18.47%     | ok               |
|          35 | -25.41%  | -3.80%             | -32.87% |    -0.78 |       82 | 33.11%     | ok               |
|          30 | -35.05%  | -3.80%             | -41.90% |    -1.08 |       81 | 37.27%     | ok               |

## PG Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -11.03%  | -10.29%            | -17.50% |    -0.44 |       54 | 28.29%     | ok               |
|          35 | -16.33%  | -10.29%            | -18.57% |    -0.66 |       62 | 31.95%     | ok               |
|          45 | -20.13%  | -10.29%            | -20.34% |    -0.94 |       54 | 25.62%     | ok               |
|          30 | -23.93%  | -10.29%            | -24.16% |    -0.97 |       64 | 35.11%     | ok               |
|          25 | -25.66%  | -10.29%            | -25.86% |    -1.04 |       76 | 36.61%     | ok               |

## PM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | -5.16%   | 99.19%             | -32.20% |    -0.03 |       84 | 47.25%     | ok               |
|          20 | -7.63%   | 99.19%             | -33.51% |    -0.07 |       83 | 55.91%     | ok               |
|          30 | -8.13%   | 99.19%             | -35.15% |    -0.1  |       79 | 50.75%     | ok               |
|          40 | -12.40%  | 99.19%             | -37.94% |    -0.24 |       78 | 43.26%     | ok               |
|          50 | -11.94%  | 99.19%             | -35.70% |    -0.24 |       68 | 37.44%     | ok               |

## POL-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 29.19%   | -54.03%            | -38.69% |     0.5  |       81 | 50.00%     | ok               |
|          25 | 4.92%    | -54.03%            | -41.14% |     0.28 |       73 | 55.17%     | ok               |
|          20 | -6.58%   | -54.03%            | -48.47% |     0.17 |       81 | 59.00%     | ok               |
|          40 | -5.77%   | -54.03%            | -33.36% |     0.12 |       58 | 31.23%     | ok               |
|          50 | -7.18%   | -54.03%            | -29.40% |     0.05 |       52 | 21.46%     | ok               |

## QCOM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -11.91%  | -8.93%             | -56.84% |     0.03 |       73 | 45.59%     | ok               |
|          35 | -17.15%  | -8.93%             | -51.84% |    -0.06 |       79 | 41.43%     | ok               |
|          20 | -20.93%  | -8.93%             | -58.06% |    -0.09 |       68 | 49.25%     | ok               |
|          30 | -26.82%  | -8.93%             | -57.69% |    -0.21 |       77 | 43.93%     | ok               |
|          15 | -30.48%  | -8.93%             | -61.34% |    -0.23 |       70 | 51.91%     | ok               |

## QQQ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 26.31%   | 65.40%             | -14.17% |     0.64 |       63 | 53.91%     | ok               |
|          25 | 17.74%   | 65.40%             | -12.88% |     0.51 |       61 | 47.92%     | ok               |
|          20 | 16.53%   | 65.40%             | -12.98% |     0.47 |       69 | 50.58%     | ok               |
|          30 | 9.79%    | 65.40%             | -14.20% |     0.33 |       66 | 45.92%     | ok               |
|          35 | -1.49%   | 65.40%             | -20.59% |     0.03 |       72 | 42.10%     | ok               |

## RENDER-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 24.51%   | -54.90%            | -44.59% |     0.48 |       86 | 61.11%     | ok               |
|          20 | 24.15%   | -54.90%            | -43.43% |     0.47 |       89 | 57.66%     | ok               |
|          25 | 18.41%   | -54.90%            | -41.13% |     0.43 |       89 | 52.68%     | ok               |
|          30 | -23.37%  | -54.90%            | -44.84% |     0.03 |       92 | 46.93%     | ok               |
|          35 | -35.73%  | -54.90%            | -47.10% |    -0.19 |       82 | 40.04%     | ok               |

## RTX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 46.89%   | 76.82%             | -18.66% |     0.95 |       74 | 57.24%     | ok               |
|          25 | 41.87%   | 76.82%             | -18.59% |     0.88 |       62 | 54.58%     | ok               |
|          15 | 38.02%   | 76.82%             | -19.55% |     0.79 |       67 | 61.73%     | ok               |
|          30 | 33.21%   | 76.82%             | -16.99% |     0.74 |       64 | 52.41%     | ok               |
|          35 | 25.37%   | 76.82%             | -18.00% |     0.66 |       58 | 49.25%     | ok               |

## SBUX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -3.03%   | 23.82%             | -23.55% |     0.03 |       57 | 40.43%     | ok               |
|          40 | -10.04%  | 23.82%             | -25.43% |    -0.16 |       62 | 33.11%     | ok               |
|          20 | -14.59%  | 23.82%             | -30.94% |    -0.2  |       60 | 42.43%     | ok               |
|          45 | -11.50%  | 23.82%             | -27.26% |    -0.22 |       68 | 27.79%     | ok               |
|          30 | -14.06%  | 23.82%             | -29.22% |    -0.23 |       62 | 38.44%     | ok               |

## SCHW Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -7.12%   | 24.13%             | -28.76% |    -0.08 |       67 | 48.59%     | ok               |
|          45 | -6.26%   | 24.13%             | -16.53% |    -0.12 |       62 | 31.28%     | ok               |
|          20 | -11.83%  | 24.13%             | -29.24% |    -0.19 |       75 | 51.08%     | ok               |
|          50 | -7.47%   | 24.13%             | -13.28% |    -0.21 |       54 | 28.29%     | ok               |
|          40 | -13.99%  | 24.13%             | -23.35% |    -0.34 |       70 | 35.77%     | ok               |

## SHIB-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -32.66%  | -57.82%            | -43.62% |    -0.22 |       77 | 58.43%     | ok               |
|          15 | -36.18%  | -57.82%            | -45.04% |    -0.25 |       87 | 66.67%     | ok               |
|          20 | -38.39%  | -57.82%            | -47.04% |    -0.3  |       81 | 61.69%     | ok               |
|          35 | -36.07%  | -57.82%            | -44.56% |    -0.35 |       71 | 45.59%     | ok               |
|          40 | -37.21%  | -57.82%            | -41.69% |    -0.41 |       60 | 37.93%     | ok               |

## SHY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd    |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:-------|---------:|---------:|:-----------|:-----------------|
|          30 | -1.78%   | -0.33%             | -3.30% |    -0.6  |       46 | 36.77%     | ok               |
|          35 | -2.39%   | -0.33%             | -3.61% |    -0.82 |       52 | 35.27%     | ok               |
|          40 | -2.41%   | -0.33%             | -3.58% |    -0.83 |       54 | 33.94%     | ok               |
|          45 | -2.43%   | -0.33%             | -3.43% |    -0.89 |       54 | 28.45%     | ok               |
|          25 | -3.05%   | -0.33%             | -4.43% |    -1.01 |       60 | 39.10%     | ok               |

## SKY-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -54.53%  | 26.45%             | -65.62% |    -0.64 |       73 | 54.60%     | ok               |
|          30 | -52.16%  | 26.45%             | -62.08% |    -0.68 |       85 | 45.21%     | ok               |
|          25 | -57.17%  | 26.45%             | -66.04% |    -0.78 |       78 | 48.47%     | ok               |
|          35 | -53.90%  | 26.45%             | -60.18% |    -0.81 |       78 | 37.36%     | ok               |
|          20 | -61.54%  | 26.45%             | -70.56% |    -0.84 |       75 | 51.92%     | ok               |

## SLB Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 4.48%    | 1.16%              | -28.43% |     0.19 |       50 | 35.11%     | ok               |
|          45 | 4.16%    | 1.16%              | -25.36% |     0.19 |       62 | 31.61%     | ok               |
|          50 | -8.19%   | 1.16%              | -29.27% |    -0.1  |       50 | 26.96%     | ok               |
|          35 | -22.51%  | 1.16%              | -45.96% |    -0.37 |       72 | 42.26%     | ok               |
|          25 | -35.79%  | 1.16%              | -55.80% |    -0.64 |       86 | 53.08%     | ok               |

## SLV Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 45.82%   | 97.52%             | -34.10% |     0.68 |       52 | 30.45%     | ok               |
|          45 | 33.44%   | 97.52%             | -31.82% |     0.55 |       63 | 31.95%     | ok               |
|          40 | 32.38%   | 97.52%             | -34.28% |     0.54 |       67 | 33.94%     | ok               |
|          20 | 21.54%   | 97.52%             | -42.66% |     0.42 |       70 | 44.26%     | ok               |
|          15 | 21.52%   | 97.52%             | -47.98% |     0.42 |       71 | 49.08%     | ok               |

## SMH Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 74.74%   | 161.53%            | -31.66% |     1.03 |       47 | 46.92%     | ok               |
|          25 | 58.17%   | 161.53%            | -33.57% |     0.89 |       44 | 45.59%     | ok               |
|          35 | 56.49%   | 161.53%            | -34.65% |     0.88 |       54 | 42.60%     | ok               |
|          30 | 53.86%   | 161.53%            | -34.29% |     0.85 |       48 | 44.26%     | ok               |
|          45 | 42.66%   | 161.53%            | -33.35% |     0.77 |       54 | 36.77%     | ok               |

## SNX-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | -13.22%  | -63.76%            | -41.29% |     0.05 |       56 | 27.59%     | ok               |
|          20 | -21.21%  | -63.76%            | -51.02% |     0.01 |       73 | 44.06%     | ok               |
|          40 | -13.27%  | -63.76%            | -36.00% |    -0.02 |       46 | 22.61%     | ok               |
|          30 | -21.55%  | -63.76%            | -50.27% |    -0.04 |       64 | 33.91%     | ok               |
|          15 | -43.06%  | -63.76%            | -52.80% |    -0.27 |       79 | 48.66%     | ok               |

## SOL-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 48.67%   | -24.89%            | -38.17% |     0.68 |       58 | 41.38%     | ok               |
|          35 | 23.89%   | -24.89%            | -43.70% |     0.46 |       70 | 47.89%     | ok               |
|          45 | 11.97%   | -24.89%            | -46.83% |     0.33 |       62 | 35.63%     | ok               |
|          25 | 1.07%    | -24.89%            | -41.09% |     0.24 |       70 | 58.43%     | ok               |
|          30 | -1.72%   | -24.89%            | -45.53% |     0.2  |       78 | 54.02%     | ok               |

## SOXX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | 72.61%   | 145.40%            | -39.32% |     0.97 |       53 | 45.42%     | ok               |
|          35 | 68.72%   | 145.40%            | -38.76% |     0.96 |       56 | 40.93%     | ok               |
|          30 | 67.82%   | 145.40%            | -39.81% |     0.94 |       54 | 43.26%     | ok               |
|          20 | 57.37%   | 145.40%            | -39.19% |     0.82 |       59 | 46.42%     | ok               |
|          40 | 44.23%   | 145.40%            | -41.03% |     0.72 |       58 | 38.94%     | ok               |

## SPY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 11.25%   | 46.39%             | -14.25% |     0.42 |       59 | 53.74%     | ok               |
|          15 | 10.72%   | 46.39%             | -16.80% |     0.4  |       63 | 56.41%     | ok               |
|          25 | 6.25%    | 46.39%             | -14.25% |     0.27 |       59 | 52.75%     | ok               |
|          30 | 0.09%    | 46.39%             | -15.53% |     0.06 |       64 | 50.08%     | ok               |
|          35 | -0.88%   | 46.39%             | -15.58% |     0.03 |       62 | 46.92%     | ok               |

## SUSHI-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -14.03%  | -61.71%            | -34.75% |    -0.04 |       58 | 17.05%     | ok               |
|          45 | -60.31%  | -61.71%            | -63.91% |    -0.83 |       60 | 22.03%     | ok               |
|          40 | -63.38%  | -61.71%            | -66.35% |    -0.84 |       63 | 28.54%     | ok               |
|          15 | -77.41%  | -61.71%            | -77.40% |    -0.97 |       86 | 50.00%     | ok               |
|          35 | -71.34%  | -61.71%            | -73.67% |    -1.01 |       84 | 33.52%     | ok               |

## T Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 56.30%   | 43.76%             | -15.08% |     1.02 |       73 | 65.56%     | ok               |
|          20 | 52.45%   | 43.76%             | -18.13% |     1.01 |       68 | 61.06%     | ok               |
|          25 | 50.71%   | 43.76%             | -17.66% |     0.99 |       68 | 58.90%     | ok               |
|          30 | 36.69%   | 43.76%             | -17.01% |     0.79 |       72 | 56.74%     | ok               |
|          35 | 21.78%   | 43.76%             | -14.49% |     0.55 |       78 | 52.41%     | ok               |

## TGT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -11.80%  | -3.67%             | -34.98% |    -0.18 |       62 | 37.77%     | ok               |
|          45 | -11.70%  | -3.67%             | -25.62% |    -0.22 |       50 | 28.62%     | ok               |
|          20 | -16.69%  | -3.67%             | -38.96% |    -0.25 |       88 | 45.42%     | ok               |
|          25 | -15.93%  | -3.67%             | -38.33% |    -0.27 |       72 | 40.93%     | ok               |
|          40 | -16.78%  | -3.67%             | -29.65% |    -0.35 |       52 | 31.28%     | ok               |

## TIA-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -52.65%  | -78.37%            | -66.82% |    -0.23 |       97 | 59.20%     | ok               |
|          35 | -40.83%  | -78.37%            | -65.93% |    -0.28 |       76 | 35.25%     | ok               |
|          25 | -63.05%  | -78.37%            | -70.91% |    -0.52 |       96 | 48.28%     | ok               |
|          20 | -65.55%  | -78.37%            | -71.78% |    -0.53 |       93 | 53.64%     | ok               |
|          40 | -52.99%  | -78.37%            | -71.23% |    -0.56 |       80 | 29.12%     | ok               |

## TLT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -11.01%  | -15.37%            | -13.82% |    -1.18 |       36 | 17.47%     | ok               |
|          40 | -15.91%  | -15.37%            | -17.65% |    -1.38 |       54 | 25.29%     | ok               |
|          30 | -19.35%  | -15.37%            | -21.85% |    -1.44 |       68 | 33.78%     | ok               |
|          45 | -14.90%  | -15.37%            | -16.30% |    -1.51 |       46 | 20.97%     | ok               |
|          35 | -19.84%  | -15.37%            | -21.68% |    -1.64 |       66 | 28.95%     | ok               |

## TMO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 53.65%   | 9.18%              | -8.17%  |     1.12 |       48 | 35.61%     | ok               |
|          45 | 41.88%   | 9.18%              | -9.69%  |     0.89 |       52 | 40.27%     | ok               |
|          40 | 35.67%   | 9.18%              | -9.91%  |     0.77 |       57 | 45.26%     | ok               |
|          35 | 32.26%   | 9.18%              | -13.84% |     0.67 |       67 | 50.42%     | ok               |
|          20 | 27.41%   | 9.18%              | -22.89% |     0.56 |       78 | 60.90%     | ok               |

## TMUS Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 2.58%    | 4.73%              | -28.14% |     0.15 |       74 | 47.92%     | ok               |
|          15 | -3.44%   | 4.73%              | -36.72% |     0.04 |       68 | 60.57%     | ok               |
|          25 | -7.17%   | 4.73%              | -34.83% |    -0.05 |       77 | 50.92%     | ok               |
|          50 | -5.70%   | 4.73%              | -30.81% |    -0.08 |       58 | 34.28%     | ok               |
|          20 | -9.01%   | 4.73%              | -35.38% |    -0.09 |       74 | 54.91%     | ok               |

## TRX-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 19.40%   | 35.08%             | -18.79% |     0.62 |       54 | 40.42%     | ok               |
|          35 | 13.59%   | 35.08%             | -21.77% |     0.45 |       66 | 48.85%     | ok               |
|          20 | 12.19%   | 35.08%             | -25.45% |     0.39 |       61 | 58.81%     | ok               |
|          30 | 10.86%   | 35.08%             | -22.90% |     0.38 |       66 | 51.72%     | ok               |
|          25 | 8.11%    | 35.08%             | -26.84% |     0.3  |       66 | 55.36%     | ok               |

## TSLA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 41.47%   | 114.48%            | -30.57% |     0.6  |       64 | 30.12%     | ok               |
|          40 | 13.71%   | 114.48%            | -50.11% |     0.34 |       63 | 35.61%     | ok               |
|          45 | -10.53%  | 114.48%            | -52.01% |     0.07 |       69 | 32.61%     | ok               |
|          35 | -20.51%  | 114.48%            | -60.12% |    -0.03 |       76 | 38.10%     | ok               |
|          30 | -37.10%  | 114.48%            | -59.64% |    -0.26 |       80 | 42.93%     | ok               |

## TXN Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 11.26%   | 47.82%             | -45.45% |     0.3  |       66 | 32.78%     | ok               |
|          35 | -9.19%   | 47.82%             | -43.28% |    -0.01 |       78 | 47.25%     | ok               |
|          40 | -10.78%  | 47.82%             | -45.67% |    -0.04 |       74 | 44.93%     | ok               |
|          20 | -14.86%  | 47.82%             | -38.49% |    -0.06 |       68 | 56.91%     | ok               |
|          45 | -12.81%  | 47.82%             | -46.24% |    -0.09 |       80 | 38.94%     | ok               |

## UNH Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 23.10%   | -28.84%            | -36.92% |     0.46 |       54 | 28.62%     | ok               |
|          30 | 22.49%   | -28.84%            | -26.31% |     0.44 |       75 | 48.59%     | ok               |
|          35 | 18.76%   | -28.84%            | -27.49% |     0.4  |       70 | 43.59%     | ok               |
|          20 | 18.63%   | -28.84%            | -26.96% |     0.39 |       78 | 57.90%     | ok               |
|          15 | 18.59%   | -28.84%            | -26.07% |     0.39 |       83 | 64.06%     | ok               |

## UNI-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 44.03%   | 49.18%             | -45.09% |     0.62 |       52 | 26.82%     | ok               |
|          45 | 31.83%   | 49.18%             | -51.70% |     0.52 |       58 | 34.29%     | ok               |
|          40 | 13.42%   | 49.18%             | -61.16% |     0.38 |       62 | 39.27%     | ok               |
|          35 | -0.53%   | 49.18%             | -65.47% |     0.27 |       72 | 44.83%     | ok               |
|          20 | -53.85%  | 49.18%             | -80.78% |    -0.26 |       95 | 60.15%     | ok               |

## UPS Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | -28.82%  | -37.10%            | -31.52% |    -0.54 |       64 | 36.44%     | ok               |
|          40 | -28.94%  | -37.10%            | -31.55% |    -0.56 |       60 | 31.11%     | ok               |
|          20 | -33.65%  | -37.10%            | -38.09% |    -0.61 |       86 | 49.58%     | ok               |
|          25 | -34.18%  | -37.10%            | -38.59% |    -0.64 |       78 | 46.26%     | ok               |
|          15 | -36.38%  | -37.10%            | -40.64% |    -0.67 |       89 | 53.58%     | ok               |

## USO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 7.46%    | 93.55%             | -32.38% |     0.25 |       48 | 25.96%     | ok               |
|          20 | 5.35%    | 93.55%             | -43.78% |     0.22 |       75 | 37.94%     | ok               |
|          15 | 1.97%    | 93.55%             | -44.72% |     0.18 |       68 | 41.43%     | ok               |
|          25 | -4.59%   | 93.55%             | -46.08% |     0.07 |       71 | 35.44%     | ok               |
|          50 | -3.42%   | 93.55%             | -29.54% |     0.07 |       52 | 24.13%     | ok               |

## VEA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 6.84%    | 37.20%             | -15.99% |     0.3  |       54 | 50.08%     | ok               |
|          20 | 0.62%    | 37.20%             | -17.51% |     0.08 |       59 | 47.42%     | ok               |
|          25 | -3.22%   | 37.20%             | -17.60% |    -0.08 |       57 | 45.42%     | ok               |
|          30 | -4.20%   | 37.20%             | -17.74% |    -0.12 |       60 | 42.93%     | ok               |
|          35 | -5.12%   | 37.20%             | -16.59% |    -0.17 |       52 | 41.26%     | ok               |

## VIXY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -56.34%  | -63.91%            | -69.78% |    -0.67 |       36 | 9.98%      | ok               |
|          15 | -77.55%  | -63.91%            | -89.47% |    -0.81 |       95 | 43.93%     | ok               |
|          45 | -65.70%  | -63.91%            | -75.03% |    -0.87 |       56 | 14.98%     | ok               |
|          30 | -78.21%  | -63.91%            | -88.17% |    -0.94 |       94 | 32.95%     | ok               |
|          40 | -73.09%  | -63.91%            | -80.72% |    -1    |       68 | 18.80%     | ok               |

## VNQ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -11.87%  | 5.24%              | -22.34% |    -0.45 |       69 | 42.76%     | ok               |
|          45 | -11.01%  | 5.24%              | -19.07% |    -0.5  |       62 | 28.95%     | ok               |
|          30 | -13.85%  | 5.24%              | -24.92% |    -0.55 |       73 | 40.10%     | ok               |
|          50 | -11.89%  | 5.24%              | -17.13% |    -0.57 |       54 | 25.62%     | ok               |
|          35 | -14.86%  | 5.24%              | -27.01% |    -0.62 |       76 | 37.60%     | ok               |

## VTI Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 12.05%   | 44.91%             | -13.96% |     0.44 |       62 | 54.24%     | ok               |
|          15 | 7.45%    | 44.91%             | -15.70% |     0.3  |       59 | 56.57%     | ok               |
|          25 | 0.10%    | 44.91%             | -15.00% |     0.07 |       58 | 52.08%     | ok               |
|          30 | -7.41%   | 44.91%             | -17.64% |    -0.21 |       68 | 50.08%     | ok               |
|          40 | -8.52%   | 44.91%             | -19.77% |    -0.28 |       72 | 42.60%     | ok               |

## VWO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -10.81%  | 32.60%             | -22.18% |    -0.42 |       56 | 28.95%     | ok               |
|          15 | -13.91%  | 32.60%             | -24.01% |    -0.45 |       74 | 47.25%     | ok               |
|          45 | -12.00%  | 32.60%             | -23.75% |    -0.46 |       58 | 31.61%     | ok               |
|          40 | -12.45%  | 32.60%             | -23.57% |    -0.47 |       68 | 34.44%     | ok               |
|          20 | -15.28%  | 32.60%             | -26.14% |    -0.52 |       71 | 44.93%     | ok               |

## VZ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -0.31%   | 15.16%             | -12.96% |     0.05 |       54 | 28.45%     | ok               |
|          45 | -11.34%  | 15.16%             | -21.44% |    -0.31 |       66 | 32.11%     | ok               |
|          35 | -11.98%  | 15.16%             | -22.73% |    -0.32 |       60 | 37.77%     | ok               |
|          25 | -13.53%  | 15.16%             | -22.13% |    -0.32 |       79 | 45.59%     | ok               |
|          40 | -15.64%  | 15.16%             | -24.21% |    -0.46 |       64 | 35.27%     | ok               |

## WFC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | -7.16%   | 34.34%             | -21.57% |    -0.08 |       77 | 44.59%     | ok               |
|          50 | -6.21%   | 34.34%             | -18.29% |    -0.13 |       60 | 32.78%     | ok               |
|          20 | -18.18%  | 34.34%             | -29.87% |    -0.26 |       77 | 53.08%     | ok               |
|          30 | -16.83%  | 34.34%             | -28.90% |    -0.27 |       80 | 47.75%     | ok               |
|          40 | -12.90%  | 34.34%             | -23.94% |    -0.3  |       72 | 41.26%     | ok               |

## WIF-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 72.11%   | -61.73%            | -40.67% |     0.71 |       67 | 44.25%     | ok               |
|          15 | 34.50%   | -61.73%            | -46.21% |     0.53 |       77 | 47.51%     | ok               |
|          25 | 9.58%    | -61.73%            | -44.74% |     0.36 |       65 | 40.23%     | ok               |
|          30 | -29.15%  | -61.73%            | -52.76% |    -0.04 |       66 | 37.16%     | ok               |
|          40 | -24.07%  | -61.73%            | -51.66% |    -0.1  |       60 | 25.29%     | ok               |

## WMT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 35.91%   | 72.72%             | -12.18% |     1.09 |       36 | 37.27%     | ok               |
|          45 | 34.77%   | 72.72%             | -14.14% |     1.02 |       42 | 39.60%     | ok               |
|          35 | 24.94%   | 72.72%             | -18.25% |     0.73 |       58 | 45.92%     | ok               |
|          40 | 23.33%   | 72.72%             | -18.53% |     0.71 |       50 | 41.26%     | ok               |
|          15 | 6.60%    | 72.72%             | -26.24% |     0.24 |       82 | 59.90%     | ok               |

## XBI Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 9.76%    | 61.24%             | -16.08% |     0.32 |       54 | 35.11%     | ok               |
|          45 | 5.59%    | 61.24%             | -15.46% |     0.22 |       52 | 32.61%     | ok               |
|          35 | -2.41%   | 61.24%             | -17.66% |     0.02 |       62 | 38.10%     | ok               |
|          50 | -3.49%   | 61.24%             | -15.66% |    -0.02 |       52 | 29.45%     | ok               |
|          30 | -4.44%   | 61.24%             | -18.10% |    -0.03 |       64 | 39.60%     | ok               |

## XLB Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -3.03%   | 7.85%              | -16.40% |    -0.08 |       40 | 22.63%     | ok               |
|          40 | -3.92%   | 7.85%              | -18.27% |    -0.1  |       56 | 26.79%     | ok               |
|          45 | -6.50%   | 7.85%              | -18.10% |    -0.22 |       44 | 24.29%     | ok               |
|          35 | -7.18%   | 7.85%              | -21.38% |    -0.23 |       56 | 30.28%     | ok               |
|          25 | -10.66%  | 7.85%              | -23.37% |    -0.35 |       64 | 35.94%     | ok               |

## XLC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 12.62%   | 35.89%             | -12.33% |     0.47 |       61 | 50.25%     | ok               |
|          25 | 12.06%   | 35.89%             | -12.31% |     0.45 |       60 | 52.41%     | ok               |
|          50 | 7.23%    | 35.89%             | -11.12% |     0.38 |       64 | 38.44%     | ok               |
|          40 | 7.80%    | 35.89%             | -13.38% |     0.34 |       62 | 43.93%     | ok               |
|          35 | 7.08%    | 35.89%             | -13.38% |     0.31 |       60 | 47.75%     | ok               |

## XLE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -1.77%   | 39.33%             | -25.98% |     0.03 |       54 | 35.94%     | ok               |
|          35 | -7.42%   | 39.33%             | -28.88% |    -0.11 |       67 | 42.43%     | ok               |
|          45 | -6.64%   | 39.33%             | -29.68% |    -0.11 |       60 | 37.94%     | ok               |
|          30 | -8.97%   | 39.33%             | -32.20% |    -0.15 |       73 | 44.59%     | ok               |
|          25 | -11.15%  | 39.33%             | -33.83% |    -0.19 |       82 | 47.75%     | ok               |

## XLF Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -2.03%   | 28.57%             | -18.63% |    -0.01 |       72 | 52.08%     | ok               |
|          15 | -4.12%   | 28.57%             | -20.19% |    -0.07 |       76 | 54.74%     | ok               |
|          25 | -8.87%   | 28.57%             | -23.22% |    -0.26 |       79 | 48.92%     | ok               |
|          30 | -9.46%   | 28.57%             | -23.61% |    -0.29 |       80 | 46.92%     | ok               |
|          35 | -16.51%  | 28.57%             | -24.48% |    -0.63 |       70 | 43.26%     | ok               |

## XLI Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 5.22%    | 34.52%             | -11.40% |     0.23 |       86 | 51.41%     | ok               |
|          20 | 1.42%    | 34.52%             | -12.74% |     0.11 |       75 | 46.42%     | ok               |
|          50 | -4.76%   | 34.52%             | -14.94% |    -0.18 |       60 | 31.78%     | ok               |
|          45 | -5.38%   | 34.52%             | -16.29% |    -0.19 |       70 | 34.28%     | ok               |
|          25 | -8.78%   | 34.52%             | -17.03% |    -0.29 |       78 | 44.43%     | ok               |

## XLK Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 78.20%   | 86.33%             | -14.75% |     1.29 |       46 | 49.75%     | ok               |
|          25 | 72.21%   | 86.33%             | -14.75% |     1.26 |       42 | 47.92%     | ok               |
|          15 | 76.39%   | 86.33%             | -14.75% |     1.23 |       46 | 51.58%     | ok               |
|          30 | 61.90%   | 86.33%             | -14.75% |     1.16 |       42 | 46.59%     | ok               |
|          35 | 41.87%   | 86.33%             | -13.43% |     0.89 |       56 | 43.76%     | ok               |

## XLM-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 5.66%    | -25.83%            | -48.81% |     0.26 |       44 | 27.20%     | ok               |
|          45 | 4.49%    | -25.83%            | -51.28% |     0.25 |       54 | 32.18%     | ok               |
|          25 | 0.58%    | -25.83%            | -49.14% |     0.23 |       69 | 50.38%     | ok               |
|          40 | -4.77%   | -25.83%            | -47.28% |     0.16 |       51 | 37.55%     | ok               |
|          30 | -8.23%   | -25.83%            | -54.59% |     0.13 |       67 | 48.28%     | ok               |

## XLP Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 6.58%    | 6.40%              | -5.66%  |     0.44 |       52 | 29.28%     | ok               |
|          50 | 4.20%    | 6.40%              | -6.08%  |     0.3  |       58 | 27.12%     | ok               |
|          40 | 4.43%    | 6.40%              | -7.77%  |     0.3  |       68 | 33.44%     | ok               |
|          35 | 3.52%    | 6.40%              | -9.73%  |     0.24 |       64 | 36.44%     | ok               |
|          30 | -0.43%   | 6.40%              | -11.16% |     0.01 |       66 | 38.10%     | ok               |

## XLU Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 4.97%    | 13.64%             | -13.94% |     0.28 |       54 | 31.11%     | ok               |
|          45 | 3.82%    | 13.64%             | -14.88% |     0.22 |       58 | 32.28%     | ok               |
|          40 | 0.69%    | 13.64%             | -16.41% |     0.08 |       64 | 34.11%     | ok               |
|          35 | -1.98%   | 13.64%             | -19.71% |    -0.05 |       64 | 36.77%     | ok               |
|          30 | -6.23%   | 13.64%             | -20.40% |    -0.23 |       69 | 40.27%     | ok               |

## XLV Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -21.91%  | 15.15%             | -22.40% |    -1.04 |       76 | 39.10%     | ok               |
|          30 | -22.26%  | 15.15%             | -22.75% |    -1.07 |       76 | 37.44%     | ok               |
|          15 | -25.13%  | 15.15%             | -25.35% |    -1.17 |       83 | 43.26%     | ok               |
|          20 | -24.97%  | 15.15%             | -25.19% |    -1.19 |       79 | 40.77%     | ok               |
|          35 | -26.13%  | 15.15%             | -26.58% |    -1.36 |       70 | 34.44%     | ok               |

## XLY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -0.70%   | 25.67%             | -15.77% |     0.06 |       76 | 54.24%     | ok               |
|          30 | -4.15%   | 25.67%             | -18.35% |    -0.06 |       75 | 47.59%     | ok               |
|          20 | -5.95%   | 25.67%             | -19.25% |    -0.1  |       72 | 50.92%     | ok               |
|          25 | -8.05%   | 25.67%             | -19.98% |    -0.17 |       69 | 49.42%     | ok               |
|          50 | -6.34%   | 25.67%             | -15.82% |    -0.22 |       62 | 32.11%     | ok               |

## XOM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | 2.73%    | 42.95%             | -19.90% |     0.15 |       55 | 34.94%     | ok               |
|          30 | 1.71%    | 42.95%             | -20.29% |     0.12 |       55 | 34.28%     | ok               |
|          50 | 0.63%    | 42.95%             | -21.35% |     0.09 |       36 | 26.96%     | ok               |
|          45 | -3.17%   | 42.95%             | -23.33% |    -0.02 |       42 | 28.29%     | ok               |
|          20 | -4.53%   | 42.95%             | -25.56% |    -0.05 |       64 | 37.10%     | ok               |

## XRP-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 27.38%   | -35.27%            | -31.38% |     0.49 |       70 | 43.10%     | ok               |
|          40 | 10.41%   | -35.27%            | -33.91% |     0.32 |       62 | 36.78%     | ok               |
|          45 | -2.35%   | -35.27%            | -37.18% |     0.16 |       60 | 32.57%     | ok               |
|          30 | -4.79%   | -35.27%            | -31.82% |     0.15 |       65 | 48.08%     | ok               |
|          50 | -6.49%   | -35.27%            | -39.26% |     0.09 |       58 | 24.90%     | ok               |

## YFI-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -45.66%  | -54.86%            | -48.73% |    -0.74 |       54 | 27.39%     | ok               |
|          45 | -45.75%  | -54.86%            | -48.82% |    -0.96 |       68 | 22.03%     | ok               |
|          35 | -64.36%  | -54.86%            | -64.36% |    -1.17 |       63 | 34.29%     | ok               |
|          50 | -50.48%  | -54.86%            | -50.48% |    -1.28 |       52 | 16.28%     | ok               |
|          30 | -70.53%  | -54.86%            | -70.53% |    -1.37 |       77 | 37.93%     | ok               |

## ZEC-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 217.75%  | 3109.85%           | -30.64% |     1.11 |       46 | 33.33%     | ok               |
|          35 | 193.41%  | 3109.85%           | -50.84% |     1.04 |       52 | 39.08%     | ok               |
|          30 | 169.97%  | 3109.85%           | -56.50% |     0.97 |       59 | 42.34%     | ok               |
|          25 | 171.41%  | 3109.85%           | -58.07% |     0.97 |       55 | 44.64%     | ok               |
|          40 | 133.67%  | 3109.85%           | -54.22% |     0.89 |       54 | 36.78%     | ok               |
