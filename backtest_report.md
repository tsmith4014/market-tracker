# Market Tracker Backtest Report

_Generated: 2026-06-08T01:37:00+00:00_

## Data Sources

- Crypto: Kraken -> Coinbase -> CoinGecko OHLC -> CoinPaprika fallback chain.
- Stocks / ETFs / indices: Stooq -> Yahoo Finance fallback chain.
- Data rows are generated from real market APIs. Mock OHLCV rows are not generated.

## Data Freshness

- Rows: **92,365**
- Symbols: **161**
- Date range: **2024-01-12** to **2026-06-08**

## Latest Signals

| symbol     | date                |         close |   composite_score | signal   | data_source   |
|:-----------|:--------------------|--------------:|------------------:|:---------|:--------------|
| AAPL       | 2026-06-05 00:00:00 |   307.34      |         35.5833   | LONG     | Yahoo Finance |
| ABBV       | 2026-06-05 00:00:00 |   227.23      |         60.5833   | LONG     | Yahoo Finance |
| BAC        | 2026-06-05 00:00:00 |    53.83      |         61.75     | LONG     | Yahoo Finance |
| CL         | 2026-06-05 00:00:00 |    88.58      |         49        | LONG     | Yahoo Finance |
| CSCO       | 2026-06-05 00:00:00 |   121.64      |         49.5833   | LONG     | Yahoo Finance |
| DE         | 2026-06-05 00:00:00 |   583.44      |         64.9167   | LONG     | Yahoo Finance |
| DXY-INDEX  | 2026-06-07 00:00:00 |   100.052     |         82.2581   | LONG     | Yahoo Finance |
| FCX        | 2026-06-05 00:00:00 |    63.37      |         52.4167   | LONG     | Yahoo Finance |
| GE         | 2026-06-05 00:00:00 |   328         |         61.75     | LONG     | Yahoo Finance |
| GS         | 2026-06-05 00:00:00 |  1038.68      |         60.9167   | LONG     | Yahoo Finance |
| IBM        | 2026-06-05 00:00:00 |   284.84      |         57.3333   | LONG     | Yahoo Finance |
| ITA        | 2026-06-05 00:00:00 |   229.45      |         65.1667   | LONG     | Yahoo Finance |
| JPM        | 2026-06-05 00:00:00 |   312.37      |         59.8333   | LONG     | Yahoo Finance |
| KO         | 2026-06-05 00:00:00 |    79.48      |         38.8333   | LONG     | Yahoo Finance |
| LLY        | 2026-06-05 00:00:00 |  1131.42      |         70.25     | LONG     | Yahoo Finance |
| LRCX       | 2026-06-05 00:00:00 |   303.28      |         48.4167   | LONG     | Yahoo Finance |
| MRK        | 2026-06-05 00:00:00 |   120.79      |         75.9167   | LONG     | Yahoo Finance |
| MS         | 2026-06-05 00:00:00 |   211.93      |         57.5833   | LONG     | Yahoo Finance |
| MU         | 2026-06-05 00:00:00 |   864.01      |         61.4167   | LONG     | Yahoo Finance |
| NOW        | 2026-06-05 00:00:00 |   112.45      |         32        | LONG     | Yahoo Finance |
| ORCL       | 2026-06-05 00:00:00 |   213.68      |         53.5833   | LONG     | Yahoo Finance |
| PG         | 2026-06-05 00:00:00 |   146.54      |         49.9167   | LONG     | Yahoo Finance |
| UPS        | 2026-06-05 00:00:00 |   108.54      |         72.75     | LONG     | Yahoo Finance |
| WFC        | 2026-06-05 00:00:00 |    81.94      |         52.75     | LONG     | Yahoo Finance |
| XLK        | 2026-06-05 00:00:00 |   180.3       |         33.5833   | LONG     | Yahoo Finance |
| ADBE       | 2026-06-05 00:00:00 |   251.44      |        -20.1667   | NEUTRAL  | Yahoo Finance |
| AGG        | 2026-06-05 00:00:00 |    98.17      |        -28.5833   | NEUTRAL  | Yahoo Finance |
| ALGO-USD   | 2026-06-08 00:00:00 |     0.09379   |        -65.25     | NEUTRAL  | Kraken API    |
| AMAT       | 2026-06-05 00:00:00 |   453.01      |         56.1667   | NEUTRAL  | Yahoo Finance |
| AMD        | 2026-06-05 00:00:00 |   466.38      |         26.0833   | NEUTRAL  | Yahoo Finance |
| AMGN       | 2026-06-05 00:00:00 |   349.58      |         64.5      | NEUTRAL  | Yahoo Finance |
| AMZN       | 2026-06-05 00:00:00 |   246.03      |        -16.25     | NEUTRAL  | Yahoo Finance |
| ARKK       | 2026-06-05 00:00:00 |    74.49      |        -16.8333   | NEUTRAL  | Yahoo Finance |
| AVGO       | 2026-06-05 00:00:00 |   385.73      |        -31.3333   | NEUTRAL  | Yahoo Finance |
| BA         | 2026-06-05 00:00:00 |   215.45      |        -54.0833   | NEUTRAL  | Yahoo Finance |
| BLK        | 2026-06-05 00:00:00 |   995.6       |        -65        | NEUTRAL  | Yahoo Finance |
| BND        | 2026-06-05 00:00:00 |    72.83      |        -34.3333   | NEUTRAL  | Yahoo Finance |
| C          | 2026-06-05 00:00:00 |   132.47      |         42.8333   | NEUTRAL  | Yahoo Finance |
| CAT        | 2026-06-05 00:00:00 |   904.28      |         42        | NEUTRAL  | Yahoo Finance |
| CMCSA      | 2026-06-05 00:00:00 |    23.82      |        -28.25     | NEUTRAL  | Yahoo Finance |
| COP        | 2026-06-05 00:00:00 |   117.14      |         -6.66667  | NEUTRAL  | Yahoo Finance |
| COST       | 2026-06-05 00:00:00 |   971.87      |        -51.75     | NEUTRAL  | Yahoo Finance |
| CRM        | 2026-06-05 00:00:00 |   185.66      |         21.1667   | NEUTRAL  | Yahoo Finance |
| CVX        | 2026-06-05 00:00:00 |   187.31      |          4.58333  | NEUTRAL  | Yahoo Finance |
| DBC        | 2026-06-05 00:00:00 |    29.23      |        -30.3333   | NEUTRAL  | Yahoo Finance |
| DIA        | 2026-06-05 00:00:00 |   509.7       |         51.6667   | NEUTRAL  | Yahoo Finance |
| EEM        | 2026-06-05 00:00:00 |    64.59      |        -15.0833   | NEUTRAL  | Yahoo Finance |
| EFA        | 2026-06-05 00:00:00 |   102.26      |        -15.6667   | NEUTRAL  | Yahoo Finance |
| EOG        | 2026-06-05 00:00:00 |   137.78      |         21.5      | NEUTRAL  | Yahoo Finance |
| EWJ        | 2026-06-05 00:00:00 |    90.72      |        -11.0833   | NEUTRAL  | Yahoo Finance |
| FET-USD    | 2026-06-08 00:00:00 |     0.2082    |        -41.25     | NEUTRAL  | Kraken API    |
| FIL-USD    | 2026-06-08 00:00:00 |     0.766     |        -65.25     | NEUTRAL  | Kraken API    |
| GDX        | 2026-06-05 00:00:00 |    78.84      |        -69.5833   | NEUTRAL  | Yahoo Finance |
| GOOGL      | 2026-06-05 00:00:00 |   368.53      |          8.83333  | NEUTRAL  | Yahoo Finance |
| HD         | 2026-06-05 00:00:00 |   310.78      |         -6.58333  | NEUTRAL  | Yahoo Finance |
| HON        | 2026-06-05 00:00:00 |   213.97      |         -2.16667  | NEUTRAL  | Yahoo Finance |
| HYG        | 2026-06-05 00:00:00 |    79.43      |        -44.75     | NEUTRAL  | Yahoo Finance |
| ICP-USD    | 2026-06-08 00:00:00 |     2.354     |        -49        | NEUTRAL  | Kraken API    |
| IEF        | 2026-06-05 00:00:00 |    93.62      |        -23.0833   | NEUTRAL  | Yahoo Finance |
| IEMG       | 2026-06-05 00:00:00 |    78.63      |        -13.3333   | NEUTRAL  | Yahoo Finance |
| INJ-USD    | 2026-06-08 00:00:00 |     5.476     |         19.9167   | NEUTRAL  | Kraken API    |
| INTC       | 2026-06-05 00:00:00 |    99.17      |          5.83333  | NEUTRAL  | Yahoo Finance |
| IWM        | 2026-06-05 00:00:00 |   281.65      |         25.8333   | NEUTRAL  | Yahoo Finance |
| JNJ        | 2026-06-05 00:00:00 |   232.77      |         57        | NEUTRAL  | Yahoo Finance |
| LIN        | 2026-06-05 00:00:00 |   507.9       |         31.3333   | NEUTRAL  | Yahoo Finance |
| MCD        | 2026-06-05 00:00:00 |   279.84      |        -20.3333   | NEUTRAL  | Yahoo Finance |
| META       | 2026-06-05 00:00:00 |   593         |        -52.75     | NEUTRAL  | Yahoo Finance |
| MPC        | 2026-06-05 00:00:00 |   262.01      |         55.3333   | NEUTRAL  | Yahoo Finance |
| NEAR-USD   | 2026-06-08 00:00:00 |     2.0405    |         19.9167   | NEUTRAL  | Kraken API    |
| NEM        | 2026-06-05 00:00:00 |    99.71      |        -64.0833   | NEUTRAL  | Yahoo Finance |
| NFLX       | 2026-06-05 00:00:00 |    82.18      |        -69        | NEUTRAL  | Yahoo Finance |
| NKE        | 2026-06-05 00:00:00 |    42.98      |        -23        | NEUTRAL  | Yahoo Finance |
| NVDA       | 2026-06-05 00:00:00 |   205.1       |        -31.3333   | NEUTRAL  | Yahoo Finance |
| OXY        | 2026-06-05 00:00:00 |    56.93      |        -13.3333   | NEUTRAL  | Yahoo Finance |
| PFE        | 2026-06-05 00:00:00 |    26.04      |         19.4167   | NEUTRAL  | Yahoo Finance |
| PM         | 2026-06-05 00:00:00 |   178.29      |         18.9167   | NEUTRAL  | Yahoo Finance |
| QCOM       | 2026-06-05 00:00:00 |   215.94      |         23.75     | NEUTRAL  | Yahoo Finance |
| QQQ        | 2026-06-05 00:00:00 |   705.06      |         16.1667   | NEUTRAL  | Yahoo Finance |
| RENDER-USD | 2026-06-08 00:00:00 |     1.656     |        -54        | NEUTRAL  | Kraken API    |
| RTX        | 2026-06-05 00:00:00 |   180.99      |         23.9167   | NEUTRAL  | Yahoo Finance |
| SBUX       | 2026-06-05 00:00:00 |    95.29      |         -7.83333  | NEUTRAL  | Yahoo Finance |
| SCHW       | 2026-06-05 00:00:00 |    88.84      |        -48        | NEUTRAL  | Yahoo Finance |
| SHY        | 2026-06-05 00:00:00 |    81.86      |        -55.5      | NEUTRAL  | Yahoo Finance |
| SLB        | 2026-06-05 00:00:00 |    54.87      |          3.16667  | NEUTRAL  | Yahoo Finance |
| SLV        | 2026-06-05 00:00:00 |    61.57      |        -22.0833   | NEUTRAL  | Yahoo Finance |
| SMH        | 2026-06-05 00:00:00 |   569.69      |         22.3333   | NEUTRAL  | Yahoo Finance |
| SOXX       | 2026-06-05 00:00:00 |   539.77      |         18.3333   | NEUTRAL  | Yahoo Finance |
| SPY        | 2026-06-05 00:00:00 |   737.55      |          0.166667 | NEUTRAL  | Yahoo Finance |
| TGT        | 2026-06-05 00:00:00 |   122.57      |         -0.833333 | NEUTRAL  | Yahoo Finance |
| TIA-USD    | 2026-06-08 00:00:00 |     0.3141    |        -68.5833   | NEUTRAL  | Kraken API    |
| TLT        | 2026-06-05 00:00:00 |    85.06      |        -14.3333   | NEUTRAL  | Yahoo Finance |
| TMO        | 2026-06-05 00:00:00 |   472.8       |         17.5833   | NEUTRAL  | Yahoo Finance |
| TRX-USD    | 2026-06-08 00:00:00 |     0.326382  |        -16.5833   | NEUTRAL  | Kraken API    |
| TSLA       | 2026-06-05 00:00:00 |   391         |        -54.5833   | NEUTRAL  | Yahoo Finance |
| TXN        | 2026-06-05 00:00:00 |   285.06      |         15.9167   | NEUTRAL  | Yahoo Finance |
| UNH        | 2026-06-05 00:00:00 |   399.47      |         48        | NEUTRAL  | Yahoo Finance |
| USO        | 2026-06-05 00:00:00 |   133.02      |         -4.33333  | NEUTRAL  | Yahoo Finance |
| VEA        | 2026-06-05 00:00:00 |    69.17      |         -4.66667  | NEUTRAL  | Yahoo Finance |
| VNQ        | 2026-06-05 00:00:00 |    96.79      |         54        | NEUTRAL  | Yahoo Finance |
| VTI        | 2026-06-05 00:00:00 |   363.38      |          6.83333  | NEUTRAL  | Yahoo Finance |
| VWO        | 2026-06-05 00:00:00 |    58.03      |        -29.3333   | NEUTRAL  | Yahoo Finance |
| VZ         | 2026-06-05 00:00:00 |    45.37      |        -23.0833   | NEUTRAL  | Yahoo Finance |
| WMT        | 2026-06-05 00:00:00 |   118.88      |        -13.1667   | NEUTRAL  | Yahoo Finance |
| XBI        | 2026-06-05 00:00:00 |   128.67      |        -24        | NEUTRAL  | Yahoo Finance |
| XLB        | 2026-06-05 00:00:00 |    50.63      |         26.5833   | NEUTRAL  | Yahoo Finance |
| XLC        | 2026-06-05 00:00:00 |   111.67      |        -61        | NEUTRAL  | Yahoo Finance |
| XLE        | 2026-06-05 00:00:00 |    57.67      |         -4.33333  | NEUTRAL  | Yahoo Finance |
| XLF        | 2026-06-05 00:00:00 |    52.3       |         61.5833   | NEUTRAL  | Yahoo Finance |
| XLI        | 2026-06-05 00:00:00 |   174.18      |         68.8333   | NEUTRAL  | Yahoo Finance |
| XLM-USD    | 2026-06-08 00:00:00 |     0.203363  |         52.0833   | NEUTRAL  | Kraken API    |
| XLP        | 2026-06-05 00:00:00 |    83.44      |         -9.58333  | NEUTRAL  | Yahoo Finance |
| XLU        | 2026-06-05 00:00:00 |    44.35      |         -4.66667  | NEUTRAL  | Yahoo Finance |
| XLV        | 2026-06-05 00:00:00 |   153.01      |         59.8333   | NEUTRAL  | Yahoo Finance |
| XLY        | 2026-06-05 00:00:00 |   114.86      |        -49.25     | NEUTRAL  | Yahoo Finance |
| XOM        | 2026-06-05 00:00:00 |   149.92      |        -25.25     | NEUTRAL  | Yahoo Finance |
| ZEC-USD    | 2026-06-08 00:00:00 |   426.81      |        -39.25     | NEUTRAL  | Kraken API    |
| AAVE-USD   | 2026-06-08 00:00:00 |    63.1       |        -51.6667   | SHORT    | Kraken API    |
| ADA-USD    | 2026-06-08 00:00:00 |     0.162707  |        -51.6667   | SHORT    | Kraken API    |
| APT-USD    | 2026-06-08 00:00:00 |     0.6606    |        -57.3333   | SHORT    | Kraken API    |
| ARB-USD    | 2026-06-08 00:00:00 |     0.0823    |        -57.3333   | SHORT    | Kraken API    |
| ATOM-USD   | 2026-06-08 00:00:00 |     1.7101    |        -51.3333   | SHORT    | Kraken API    |
| AVAX-USD   | 2026-06-08 00:00:00 |     6.698     |        -53.3333   | SHORT    | Kraken API    |
| BCH-USD    | 2026-06-08 00:00:00 |   226.92      |        -63.8333   | SHORT    | Kraken API    |
| BITO       | 2026-06-05 00:00:00 |     8.22      |        -60.8333   | SHORT    | Yahoo Finance |
| BONK-USD   | 2026-06-08 00:00:00 |     4.362e-06 |        -51.6667   | SHORT    | Kraken API    |
| BTC-USD    | 2026-06-08 00:00:00 | 62965.4       |        -47.6667   | SHORT    | Kraken API    |
| COMP-USD   | 2026-06-08 00:00:00 |    16.42      |        -46.3333   | SHORT    | Kraken API    |
| CRV-USD    | 2026-06-08 00:00:00 |     0.19545   |        -43        | SHORT    | Kraken API    |
| DASH-USD   | 2026-06-08 00:00:00 |    36.626     |        -63.8333   | SHORT    | Kraken API    |
| DIS        | 2026-06-05 00:00:00 |    99.71      |        -51.5833   | SHORT    | Yahoo Finance |
| DOGE-USD   | 2026-06-08 00:00:00 |     0.0853245 |        -49.6667   | SHORT    | Kraken API    |
| DOT-USD    | 2026-06-08 00:00:00 |     0.965     |        -53.3333   | SHORT    | Kraken API    |
| ETC-USD    | 2026-06-08 00:00:00 |     7.017     |        -51.6667   | SHORT    | Kraken API    |
| ETH-USD    | 2026-06-08 00:00:00 |  1679         |        -59.8333   | SHORT    | Kraken API    |
| FXI        | 2026-06-05 00:00:00 |    34.75      |        -50.0833   | SHORT    | Yahoo Finance |
| GDXJ       | 2026-06-05 00:00:00 |   100.59      |        -64        | SHORT    | Yahoo Finance |
| GLD        | 2026-06-05 00:00:00 |   396.24      |        -56.3333   | SHORT    | Yahoo Finance |
| GRT-USD    | 2026-06-08 00:00:00 |     0.01996   |        -57.3333   | SHORT    | Kraken API    |
| HBAR-USD   | 2026-06-08 00:00:00 |     0.08187   |        -37.5      | SHORT    | Kraken API    |
| IBIT       | 2026-06-05 00:00:00 |    34.14      |        -65.3333   | SHORT    | Yahoo Finance |
| INTU       | 2026-06-05 00:00:00 |   296.76      |        -65.75     | SHORT    | Yahoo Finance |
| LDO-USD    | 2026-06-08 00:00:00 |     0.27      |        -49.6667   | SHORT    | Kraken API    |
| LINK-USD   | 2026-06-08 00:00:00 |     7.8676    |        -49.6667   | SHORT    | Kraken API    |
| LTC-USD    | 2026-06-08 00:00:00 |    42.42      |        -51.6667   | SHORT    | Kraken API    |
| MSFT       | 2026-06-05 00:00:00 |   416.67      |        -30.5833   | SHORT    | Yahoo Finance |
| OP-USD     | 2026-06-08 00:00:00 |     0.0956    |        -57.3333   | SHORT    | Kraken API    |
| PEP        | 2026-06-05 00:00:00 |   141.92      |        -44.3333   | SHORT    | Yahoo Finance |
| PEPE-USD   | 2026-06-08 00:00:00 |     2.777e-06 |        -51.6667   | SHORT    | Kraken API    |
| POL-USD    | 2026-06-08 00:00:00 |     0.07897   |        -44.6667   | SHORT    | Kraken API    |
| SHIB-USD   | 2026-06-08 00:00:00 |     4.678e-06 |        -48.3333   | SHORT    | Kraken API    |
| SKY-USD    | 2026-06-08 00:00:00 |     0.05734   |        -46.3333   | SHORT    | Kraken API    |
| SNX-USD    | 2026-06-08 00:00:00 |     0.246     |        -51.3333   | SHORT    | Kraken API    |
| SOL-USD    | 2026-06-08 00:00:00 |    65.8       |        -49.6667   | SHORT    | Kraken API    |
| SUSHI-USD  | 2026-06-08 00:00:00 |     0.1702    |        -49        | SHORT    | Kraken API    |
| T          | 2026-06-05 00:00:00 |    22.75      |        -52.75     | SHORT    | Yahoo Finance |
| TMUS       | 2026-06-05 00:00:00 |   178.1       |        -56.0833   | SHORT    | Yahoo Finance |
| UNI-USD    | 2026-06-08 00:00:00 |     2.5536    |        -49.6667   | SHORT    | Kraken API    |
| VIXY       | 2026-06-05 00:00:00 |    24.31      |        -41.8333   | SHORT    | Yahoo Finance |
| WIF-USD    | 2026-06-08 00:00:00 |     0.1566    |        -50.6667   | SHORT    | Kraken API    |
| XRP-USD    | 2026-06-08 00:00:00 |     1.14814   |        -49.6667   | SHORT    | Kraken API    |
| YFI-USD    | 2026-06-08 00:00:00 |  1886.4       |        -49.6667   | SHORT    | Kraken API    |

## Edge Summary

- Symbols with trades: **160** of 160
- Beat buy-and-hold: **35.00%** of traded symbols
- Positive return: **34.38%** of traded symbols
- Median strategy return: **-9.40%** (benchmark **14.33%**)
- Median excess vs benchmark: **-29.01%**
- Median Sharpe: **-0.07**
- Median exposure: **44.68%**

> Edge is real only if both _beat buy-and-hold_ and _median excess_ are convincingly positive across many symbols. Treat a single high-return symbol as noise.

## Portfolio Backtest

Actual capital-allocation books (not per-symbol averages). Benchmarks: `equal_weight_buyhold` (whole tracked universe), `spy_buyhold` (100% SPY), and `sixty_forty` (60% SPY / 40% AGG). `high_conf_voltarget` inverse-vol-weights the HIGH-confidence book; `conviction_long_short` is market-neutral. Judge on **Sharpe** and **max_drawdown** out-of-sample, not raw return: a fully-invested long book wins on return in a bull market but carries all the risk.

| strategy              | scope         | ann_return   | ann_vol   |   sharpe | max_drawdown   | total_return   |   avg_gross_exposure |
|:----------------------|:--------------|:-------------|:----------|---------:|:---------------|:---------------|---------------------:|
| equal_weight_buyhold  | full          | -12.15%      | 33.88%    |    -0.36 | -58.54%        | -42.14%        |                 1    |
| equal_weight_buyhold  | out_of_sample | -21.72%      | 34.91%    |    -0.62 | -39.63%        | -25.69%        |                 1    |
| all_signals_ew        | full          | -6.03%       | 28.30%    |    -0.21 | -59.73%        | -26.39%        |                 1    |
| all_signals_ew        | out_of_sample | 4.58%        | 28.87%    |     0.16 | -30.14%        | 0.47%          |                 1    |
| high_conf_ew          | full          | 3.95%        | 32.87%    |     0.12 | -43.65%        | -4.15%         |                 0.89 |
| high_conf_ew          | out_of_sample | 20.40%       | 37.23%    |     0.55 | -20.90%        | 15.66%         |                 0.89 |
| high_conf_voltarget   | full          | 4.37%        | 30.52%    |     0.14 | -37.85%        | -0.65%         |                 0.89 |
| high_conf_voltarget   | out_of_sample | 12.50%       | 35.47%    |     0.35 | -17.06%        | 7.05%          |                 0.89 |
| conviction_long_short | full          | -8.78%       | 23.64%    |    -0.37 | -39.41%        | -29.76%        |                 0.97 |
| conviction_long_short | out_of_sample | -3.93%       | 27.17%    |    -0.14 | -21.22%        | -7.82%         |                 0.97 |
| spy_buyhold           | full          | 8.75%        | 13.32%    |     0.66 | -17.81%        | 27.08%         |                 0.78 |
| spy_buyhold           | out_of_sample | -2.22%       | 9.65%     |    -0.23 | -14.83%        | -2.82%         |                 0.78 |
| sixty_forty           | full          | 4.87%        | 8.44%     |     0.58 | -10.80%        | 14.75%         |                 0.78 |
| sixty_forty           | out_of_sample | -2.79%       | 6.25%     |    -0.45 | -10.06%        | -3.13%         |                 0.78 |

## Walk-Forward Robustness

Each book measured across contiguous time folds (each a different regime). A book has durable edge only if `mean_sharpe` is positive, `min_sharpe` isn't deeply negative, and `pct_positive_folds` is high — a single great fold doesn't count. `fold_sharpes` lists each fold oldest-to-newest.

| strategy              |   n_folds |   mean_sharpe |   median_sharpe |   min_sharpe | pct_positive_folds   | mean_return   | fold_sharpes                |
|:----------------------|----------:|--------------:|----------------:|-------------:|:---------------------|:--------------|:----------------------------|
| equal_weight_buyhold  |         5 |         -0.09 |           -0.31 |        -1.42 | 40.00%               | -8.89%        | 1.83;-1.42;0.40;-0.31;-0.93 |
| all_signals_ew        |         5 |         -0    |           -0.2  |        -1.53 | 40.00%               | -4.67%        | 0.87;-0.20;-0.34;-1.53;1.18 |
| high_conf_ew          |         5 |          0.43 |           -0.38 |        -0.46 | 40.00%               | 0.59%         | 1.82;-0.38;-0.46;-0.40;1.58 |
| high_conf_voltarget   |         5 |          0.53 |           -0.25 |        -0.27 | 40.00%               | 0.56%         | 2.53;-0.25;-0.27;-0.25;0.88 |
| conviction_long_short |         5 |         -0.34 |           -0.18 |        -1.16 | 40.00%               | -6.26%        | -0.18;-1.16;0.33;-1.09;0.37 |
| spy_buyhold           |         5 |          0.72 |            0.3  |         0.05 | 100.00%              | 5.10%         | 2.05;1.12;0.05;0.08;0.30    |
| sixty_forty           |         5 |          0.6  |            0.12 |         0.02 | 100.00%              | 2.87%         | 1.96;0.86;0.06;0.12;0.02    |

## Strategy Comparison

Each decision rule backtested over the same data. `out_of_sample` is the most recent ~35% of each symbol's history (unseen tail). A rule has real edge only if `median_excess` and `beat_benchmark_pct` stay positive out-of-sample, not just full-sample.

| strategy        | scope         |   symbols | beat_benchmark_pct   | positive_pct   | median_return   | median_benchmark   | median_excess   |   median_sharpe |   total_trades |
|:----------------|:--------------|----------:|:---------------------|:---------------|:----------------|:-------------------|:----------------|----------------:|---------------:|
| trend           | full          |       160 | 35.00%               | 34.38%         | -9.40%          | 14.33%             | -29.01%         |           -0.07 |          11336 |
| trend           | out_of_sample |       160 | 38.12%               | 55.62%         | 3.28%           | 5.30%              | -8.69%          |            0.36 |           3928 |
| mean_reversion  | full          |       158 | 41.77%               | 48.73%         | -0.09%          | 14.33%             | -14.65%         |           -0.02 |           1272 |
| mean_reversion  | out_of_sample |       128 | 45.31%               | 57.81%         | 0.33%           | 2.89%              | -2.73%          |            0.67 |            480 |
| regime_adaptive | full          |       160 | 35.62%               | 35.00%         | -10.26%         | 14.33%             | -29.72%         |           -0.07 |          11614 |
| regime_adaptive | out_of_sample |       160 | 37.50%               | 58.13%         | 3.28%           | 5.30%              | -8.67%          |            0.37 |           4033 |

## Signal Calibration

Realized forward return in the signal's direction, grouped by confidence. HIGH should outrank LOW for the confidence score to be meaningful.

| confidence_level   |   horizon |     n | mean_return   | median_return   | win_rate   |
|:-------------------|----------:|------:|:--------------|:----------------|:-----------|
| HIGH               |         5 |  8179 | 0.13%         | 0.13%           | 52.28%     |
| MEDIUM             |         5 | 29172 | 0.09%         | 0.12%           | 51.33%     |
| LOW                |         5 |  3261 | -0.58%        | -0.49%          | 45.11%     |
| ALL                |         5 | 40612 | 0.05%         | 0.08%           | 51.02%     |
| HIGH               |        10 |  8117 | 0.50%         | 0.19%           | 52.26%     |
| MEDIUM             |        10 | 28903 | 0.24%         | 0.18%           | 51.47%     |
| LOW                |        10 |  3248 | -0.85%        | -0.72%          | 45.35%     |
| ALL                |        10 | 40268 | 0.21%         | 0.13%           | 51.13%     |
| HIGH               |        20 |  8010 | 0.89%         | 0.47%           | 53.72%     |
| MEDIUM             |        20 | 28222 | 0.77%         | 0.61%           | 53.52%     |
| LOW                |        20 |  3202 | -0.78%        | -0.63%          | 46.63%     |
| ALL                |        20 | 39434 | 0.67%         | 0.50%           | 53.00%     |

## Backtest Summary

### Data Quality / Signal Availability

- **ok**: 160 symbols

| symbol     |   trades | return   | benchmark_return   | mdd     |   sharpe | exposure   | skipped_reason   |
|:-----------|---------:|:---------|:-------------------|:--------|---------:|:-----------|:-----------------|
| AAPL       |       65 | 11.86%   | 65.31%             | -20.65% |     0.33 | 49.25%     | ok               |
| AAVE-USD   |       80 | -59.26%  | -81.97%            | -69.30% |    -0.68 | 35.82%     | ok               |
| ABBV       |       64 | -13.21%  | 39.92%             | -30.55% |    -0.24 | 49.25%     | ok               |
| ADA-USD    |       88 | -84.06%  | -85.05%            | -91.25% |    -0.72 | 46.36%     | ok               |
| ADBE       |       66 | -22.69%  | -57.85%            | -38.01% |    -0.23 | 56.91%     | ok               |
| AGG        |       69 | -7.13%   | -0.94%             | -9.93%  |    -1.17 | 31.11%     | ok               |
| ALGO-USD   |       86 | -55.03%  | -77.61%            | -61.38% |    -0.66 | 38.51%     | ok               |
| AMAT       |       67 | -19.38%  | 199.51%            | -57.80% |    -0.1  | 53.58%     | ok               |
| AMD        |       56 | 32.54%   | 218.22%            | -47.17% |     0.49 | 38.94%     | ok               |
| AMGN       |       71 | -18.40%  | 14.05%             | -34.14% |    -0.35 | 49.08%     | ok               |
| AMZN       |       74 | -33.84%  | 59.12%             | -42.48% |    -0.99 | 38.27%     | ok               |
| APT-USD    |       78 | -30.79%  | -93.25%            | -69.96% |    -0.06 | 42.72%     | ok               |
| ARB-USD    |       72 | 7.56%    | -90.12%            | -62.67% |     0.32 | 38.89%     | ok               |
| ARKK       |       81 | -32.67%  | 57.22%             | -35.19% |    -0.57 | 38.94%     | ok               |
| ATOM-USD   |       88 | -62.00%  | -76.95%            | -70.27% |    -0.96 | 43.87%     | ok               |
| AVAX-USD   |       74 | -32.25%  | -84.01%            | -55.62% |    -0.22 | 37.93%     | ok               |
| AVGO       |       60 | 43.82%   | 248.23%            | -35.76% |     0.6  | 46.76%     | ok               |
| BA         |       69 | 1.80%    | -1.03%             | -30.56% |     0.16 | 51.25%     | ok               |
| BAC        |       80 | -18.17%  | 64.12%             | -27.64% |    -0.46 | 45.59%     | ok               |
| BCH-USD    |       78 | -16.12%  | -52.04%            | -53.87% |     0    | 45.98%     | ok               |
| BITO       |       78 | 12.09%   | -60.97%            | -42.82% |     0.31 | 39.10%     | ok               |
| BLK        |       77 | -2.44%   | 24.51%             | -20.81% |    -0    | 41.93%     | ok               |
| BND        |       65 | -7.32%   | -0.86%             | -9.89%  |    -1.18 | 32.28%     | ok               |
| BONK-USD   |       70 | 57.68%   | -87.89%            | -48.17% |     0.66 | 41.19%     | ok               |
| BTC-USD    |       74 | -0.95%   | -35.82%            | -30.44% |     0.13 | 51.72%     | ok               |
| C          |       83 | -27.72%  | 151.75%            | -36.36% |    -0.55 | 50.75%     | ok               |
| CAT        |       74 | 29.61%   | 211.38%            | -21.02% |     0.56 | 57.40%     | ok               |
| CL         |       58 | 21.25%   | 9.48%              | -14.32% |     0.7  | 49.25%     | ok               |
| CMCSA      |       82 | -37.38%  | -40.88%            | -41.09% |    -0.95 | 44.43%     | ok               |
| COMP-USD   |       91 | -34.85%  | -80.71%            | -60.50% |    -0.18 | 45.59%     | ok               |
| COP        |       77 | -25.45%  | 4.87%              | -43.99% |    -0.48 | 41.60%     | ok               |
| COST       |       62 | 6.80%    | 42.24%             | -29.73% |     0.27 | 47.09%     | ok               |
| CRM        |       65 | -34.20%  | -31.73%            | -40.31% |    -0.68 | 43.59%     | ok               |
| CRV-USD    |       60 | 17.80%   | -81.97%            | -39.89% |     0.4  | 32.57%     | ok               |
| CSCO       |       61 | 25.58%   | 141.64%            | -21.79% |     0.55 | 49.08%     | ok               |
| CVX        |       73 | -16.18%  | 27.19%             | -28.37% |    -0.41 | 41.60%     | ok               |
| DASH-USD   |       67 | -44.56%  | -14.85%            | -64.43% |    -0.05 | 30.65%     | ok               |
| DBC        |       60 | -13.47%  | 32.50%             | -25.70% |    -0.47 | 33.11%     | ok               |
| DE         |       76 | -10.61%  | 50.95%             | -25.72% |    -0.15 | 45.26%     | ok               |
| DIA        |       60 | -1.41%   | 35.59%             | -12.94% |    -0.04 | 45.76%     | ok               |
| DIS        |       63 | 1.48%    | 10.36%             | -22.94% |     0.14 | 47.59%     | ok               |
| DOGE-USD   |       77 | -21.48%  | -77.53%            | -60.95% |     0.04 | 49.62%     | ok               |
| DOT-USD    |       92 | -49.81%  | -87.55%            | -59.34% |    -0.4  | 47.51%     | ok               |
| DXY-INDEX  |       44 | -3.18%   | -3.06%             | -6.06%  |    -0.51 | 27.33%     | ok               |
| EEM        |       64 | -9.40%   | 64.77%             | -25.67% |    -0.25 | 43.43%     | ok               |
| EFA        |       58 | -8.43%   | 36.22%             | -13.53% |    -0.31 | 43.59%     | ok               |
| EOG        |       83 | -29.95%  | 18.72%             | -48.13% |    -0.69 | 47.75%     | ok               |
| ETC-USD    |       66 | -39.81%  | -75.31%            | -53.13% |    -0.6  | 30.84%     | ok               |
| ETH-USD    |       62 | 148.37%  | -53.46%            | -30.11% |     1.23 | 44.44%     | ok               |
| EWJ        |       64 | -18.27%  | 36.56%             | -30.73% |    -0.59 | 41.43%     | ok               |
| FCX        |       71 | -36.12%  | 54.79%             | -48.09% |    -0.48 | 45.59%     | ok               |
| FET-USD    |       79 | -19.14%  | -86.10%            | -54.02% |     0.11 | 39.85%     | ok               |
| FIL-USD    |       70 | -32.70%  | -86.48%            | -46.54% |    -0.27 | 32.95%     | ok               |
| FXI        |       50 | -12.08%  | 52.88%             | -24.33% |    -0.23 | 27.12%     | ok               |
| GDX        |       60 | 8.90%    | 165.45%            | -34.99% |     0.27 | 48.75%     | ok               |
| GDXJ       |       66 | -18.63%  | 176.65%            | -44.93% |    -0.16 | 46.09%     | ok               |
| GE         |       76 | 10.01%   | 216.65%            | -27.82% |     0.29 | 51.41%     | ok               |
| GLD        |       48 | 19.09%   | 108.87%            | -16.63% |     0.54 | 43.43%     | ok               |
| GOOGL      |       65 | 83.40%   | 158.35%            | -20.41% |     1.2  | 54.58%     | ok               |
| GRT-USD    |       87 | -22.60%  | -91.74%            | -57.16% |    -0.05 | 40.80%     | ok               |
| GS         |       78 | -0.74%   | 174.96%            | -22.13% |     0.08 | 50.58%     | ok               |
| HD         |       69 | -4.23%   | -12.63%            | -17.69% |    -0.04 | 44.76%     | ok               |
| HON        |       93 | -25.95%  | 12.89%             | -27.46% |    -0.72 | 52.58%     | ok               |
| HYG        |       83 | -10.09%  | 2.23%              | -9.59%  |    -1.18 | 34.28%     | ok               |
| IBIT       |       32 | 42.82%   | -10.18%            | -18.95% |     0.88 | 29.28%     | ok               |
| IBM        |       72 | 34.19%   | 71.80%             | -25.31% |     0.69 | 50.92%     | ok               |
| ICP-USD    |       83 | -5.61%   | -80.99%            | -55.67% |     0.21 | 38.70%     | ok               |
| IEF        |       78 | -11.67%  | -2.71%             | -11.70% |    -1.64 | 32.95%     | ok               |
| IEMG       |       58 | -5.52%   | 59.01%             | -26.84% |    -0.12 | 43.59%     | ok               |
| INJ-USD    |       79 | -54.10%  | -76.19%            | -77.00% |    -0.5  | 39.46%     | ok               |
| INTC       |       72 | 55.53%   | 110.46%            | -60.60% |     0.62 | 49.42%     | ok               |
| INTU       |       67 | -15.91%  | -51.49%            | -43.77% |    -0.16 | 42.43%     | ok               |
| ITA        |       70 | 0.23%    | 87.55%             | -23.75% |     0.08 | 45.92%     | ok               |
| IWM        |       50 | 8.72%    | 45.76%             | -12.83% |     0.36 | 37.10%     | ok               |
| JNJ        |       76 | 2.50%    | 43.34%             | -17.51% |     0.15 | 51.08%     | ok               |
| JPM        |       79 | -23.33%  | 84.78%             | -33.04% |    -0.61 | 52.41%     | ok               |
| KO         |       49 | 23.27%   | 31.61%             | -8.07%  |     0.88 | 37.27%     | ok               |
| LDO-USD    |       80 | -2.37%   | -86.54%            | -58.32% |     0.26 | 38.12%     | ok               |
| LIN        |       72 | -3.07%   | 24.21%             | -21.53% |    -0.05 | 39.27%     | ok               |
| LINK-USD   |       72 | -17.74%  | -66.46%            | -55.61% |     0.05 | 41.19%     | ok               |
| LLY        |       69 | -12.82%  | 75.98%             | -53.34% |    -0.09 | 51.41%     | ok               |
| LRCX       |       82 | -25.51%  | 299.23%            | -63.56% |    -0.21 | 46.09%     | ok               |
| LTC-USD    |       68 | -35.44%  | -62.35%            | -55.90% |    -0.31 | 48.08%     | ok               |
| MCD        |       77 | -3.06%   | -4.64%             | -19.14% |    -0.07 | 38.77%     | ok               |
| META       |       74 | -10.91%  | 58.35%             | -38.96% |    -0.04 | 51.75%     | ok               |
| MPC        |       71 | -13.74%  | 66.40%             | -44.76% |    -0.14 | 49.92%     | ok               |
| MRK        |       69 | -21.30%  | 1.82%              | -32.14% |    -0.45 | 46.92%     | ok               |
| MS         |       83 | -18.91%  | 136.27%            | -26.72% |    -0.43 | 47.25%     | ok               |
| MSFT       |       76 | -32.96%  | 7.26%              | -37.19% |    -0.87 | 47.92%     | ok               |
| MU         |       53 | 177.54%  | 948.68%            | -68.76% |     1.13 | 58.57%     | ok               |
| NEAR-USD   |       89 | -4.04%   | -64.92%            | -59.86% |     0.22 | 42.91%     | ok               |
| NEM        |       70 | -19.45%  | 164.90%            | -38.49% |    -0.12 | 55.74%     | ok               |
| NFLX       |       62 | 22.69%   | 66.98%             | -21.09% |     0.55 | 54.24%     | ok               |
| NKE        |       93 | -36.13%  | -59.09%            | -55.35% |    -0.49 | 44.93%     | ok               |
| NOW        |       78 | 21.27%   | -22.89%            | -30.25% |     0.41 | 46.09%     | ok               |
| NVDA       |       74 | -28.55%  | 123.15%            | -45.02% |    -0.22 | 60.61%     | ok               |
| OP-USD     |       74 | 13.40%   | -95.26%            | -70.11% |     0.37 | 35.63%     | ok               |
| ORCL       |       70 | 61.89%   | 100.45%            | -29.47% |     0.68 | 52.75%     | ok               |
| OXY        |       65 | 4.11%    | -1.95%             | -29.70% |     0.19 | 44.59%     | ok               |
| PEP        |       85 | -9.40%   | -15.16%            | -21.35% |    -0.22 | 49.42%     | ok               |
| PEPE-USD   |       79 | 1.20%    | -87.13%            | -57.66% |     0.29 | 43.30%     | ok               |
| PFE        |       77 | -38.05%  | -9.27%             | -42.29% |    -1.18 | 37.27%     | ok               |
| PG         |       63 | -13.60%  | -2.70%             | -20.82% |    -0.5  | 40.93%     | ok               |
| PM         |       81 | -0.11%   | 87.14%             | -33.68% |     0.09 | 56.91%     | ok               |
| POL-USD    |       81 | 61.23%   | -84.79%            | -46.45% |     0.74 | 47.70%     | ok               |
| QCOM       |       81 | -15.67%  | 54.02%             | -57.69% |    -0.04 | 48.59%     | ok               |
| QQQ        |       60 | 17.24%   | 72.15%             | -12.88% |     0.51 | 46.26%     | ok               |
| RENDER-USD |       94 | -16.54%  | -60.19%            | -45.00% |     0.13 | 44.61%     | ok               |
| RTX        |       58 | 17.94%   | 109.65%            | -16.99% |     0.5  | 51.75%     | ok               |
| SBUX       |       67 | -25.64%  | 3.60%              | -31.46% |    -0.54 | 40.27%     | ok               |
| SCHW       |       74 | -21.97%  | 36.19%             | -30.41% |    -0.52 | 45.42%     | ok               |
| SHIB-USD   |       78 | -28.71%  | -80.84%            | -48.95% |    -0.14 | 52.11%     | ok               |
| SHY        |       50 | -2.49%   | -0.58%             | -2.85%  |    -0.85 | 36.44%     | ok               |
| SKY-USD    |       68 | -28.79%  | -0.85%             | -43.98% |    -0.38 | 39.66%     | ok               |
| SLB        |       79 | -29.65%  | 9.85%              | -54.13% |    -0.52 | 51.08%     | ok               |
| SLV        |       58 | 36.93%   | 190.56%            | -42.66% |     0.58 | 40.60%     | ok               |
| SMH        |       50 | 96.11%   | 229.40%            | -33.99% |     1.2  | 51.41%     | ok               |
| SNX-USD    |       67 | 5.80%    | -88.77%            | -32.91% |     0.31 | 40.23%     | ok               |
| SOL-USD    |       70 | -37.39%  | -69.77%            | -55.52% |    -0.15 | 59.39%     | ok               |
| SOXX       |       57 | 87.48%   | 190.52%            | -40.34% |     1.07 | 50.58%     | ok               |
| SPY        |       60 | 6.78%    | 54.73%             | -16.47% |     0.29 | 50.92%     | ok               |
| SUSHI-USD  |       92 | -80.34%  | -90.43%            | -81.70% |    -1.23 | 36.21%     | ok               |
| T          |       64 | 32.46%   | 38.05%             | -17.01% |     0.78 | 49.42%     | ok               |
| TGT        |       58 | -11.46%  | -13.02%            | -40.57% |    -0.16 | 38.77%     | ok               |
| TIA-USD    |       80 | -7.22%   | -94.29%            | -55.60% |     0.18 | 32.57%     | ok               |
| TLT        |       74 | -22.24%  | -11.87%            | -24.21% |    -1.6  | 33.61%     | ok               |
| TMO        |       59 | 22.17%   | -13.14%            | -16.83% |     0.53 | 49.42%     | ok               |
| TMUS       |       70 | 19.54%   | 9.57%              | -24.50% |     0.49 | 48.59%     | ok               |
| TRX-USD    |       70 | -4.46%   | 20.85%             | -22.90% |    -0.02 | 49.04%     | ok               |
| TSLA       |       68 | 8.00%    | 78.63%             | -57.89% |     0.29 | 44.09%     | ok               |
| TXN        |       73 | -12.11%  | 72.90%             | -46.98% |    -0.04 | 54.08%     | ok               |
| UNH        |       80 | 13.76%   | -23.40%            | -32.85% |     0.33 | 51.91%     | ok               |
| UNI-USD    |       90 | -68.59%  | -83.19%            | -79.39% |    -0.74 | 41.00%     | ok               |
| UPS        |       66 | -35.25%  | -31.44%            | -40.62% |    -0.71 | 38.60%     | ok               |
| USO        |       68 | 2.80%    | 95.56%             | -43.35% |     0.17 | 34.44%     | ok               |
| VEA        |       60 | -2.87%   | 45.41%             | -19.49% |    -0.07 | 43.43%     | ok               |
| VIXY       |       92 | -78.51%  | -58.96%            | -87.63% |    -0.95 | 31.45%     | ok               |
| VNQ        |       75 | -16.77%  | 11.16%             | -24.92% |    -0.7  | 37.60%     | ok               |
| VTI        |       70 | -2.17%   | 53.25%             | -18.77% |    -0.02 | 52.25%     | ok               |
| VWO        |       76 | -13.41%  | 43.60%             | -25.20% |    -0.47 | 44.09%     | ok               |
| VZ         |       83 | -18.51%  | 17.66%             | -31.88% |    -0.54 | 39.27%     | ok               |
| WFC        |       84 | -18.91%  | 72.87%             | -30.22% |    -0.33 | 46.76%     | ok               |
| WIF-USD    |       72 | -31.20%  | -92.76%            | -50.40% |    -0.05 | 31.61%     | ok               |
| WMT        |       55 | 33.20%   | 121.08%            | -21.31% |     0.87 | 52.91%     | ok               |
| XBI        |       64 | -6.39%   | 42.30%             | -21.75% |    -0.07 | 39.77%     | ok               |
| XLB        |       70 | -14.82%  | 21.34%             | -26.57% |    -0.51 | 37.60%     | ok               |
| XLC        |       63 | 19.04%   | 51.29%             | -12.33% |     0.63 | 56.41%     | ok               |
| XLE        |       77 | -10.75%  | 39.50%             | -37.89% |    -0.2  | 46.76%     | ok               |
| XLF        |       76 | -11.61%  | 39.10%             | -23.61% |    -0.38 | 49.25%     | ok               |
| XLI        |       66 | 5.55%    | 55.37%             | -11.38% |     0.27 | 47.92%     | ok               |
| XLK        |       40 | 69.57%   | 87.58%             | -14.75% |     1.27 | 48.92%     | ok               |
| XLM-USD    |       69 | 6.29%    | -54.61%            | -45.54% |     0.3  | 47.13%     | ok               |
| XLP        |       72 | 5.75%    | 14.62%             | -10.28% |     0.35 | 43.59%     | ok               |
| XLU        |       69 | -6.98%   | 40.08%             | -16.16% |    -0.28 | 38.94%     | ok               |
| XLV        |       66 | -9.06%   | 8.89%              | -14.23% |    -0.43 | 37.10%     | ok               |
| XLY        |       76 | 0.25%    | 32.05%             | -14.01% |     0.07 | 44.76%     | ok               |
| XOM        |       61 | 0.51%    | 50.00%             | -20.29% |     0.09 | 36.44%     | ok               |
| XRP-USD    |       64 | -40.91%  | -53.20%            | -53.73% |    -0.45 | 35.82%     | ok               |
| YFI-USD    |       85 | -54.61%  | -78.85%            | -67.78% |    -0.81 | 40.04%     | ok               |
| ZEC-USD    |       69 | 41.84%   | 600.84%            | -46.93% |     0.55 | 36.59%     | ok               |

## AAPL Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 24.33%   | 65.31%             | -21.71% |     0.54 |       69 | 53.74%     | ok               |
|          15 | 20.15%   | 65.31%             | -23.86% |     0.46 |       75 | 61.23%     | ok               |
|          25 | 18.39%   | 65.31%             | -20.03% |     0.45 |       67 | 51.58%     | ok               |
|          30 | 11.86%   | 65.31%             | -20.65% |     0.33 |       65 | 49.25%     | ok               |
|          35 | 9.37%    | 65.31%             | -22.04% |     0.29 |       63 | 46.59%     | ok               |

## AAVE-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 8.63%    | -81.97%            | -43.61% |     0.31 |       38 | 28.54%     | ok               |
|          45 | 7.09%    | -81.97%            | -46.87% |     0.29 |       36 | 25.48%     | ok               |
|          35 | -18.31%  | -81.97%            | -51.96% |    -0.01 |       52 | 31.23%     | ok               |
|          50 | -26.94%  | -81.97%            | -47.78% |    -0.22 |       40 | 19.92%     | ok               |
|          15 | -55.04%  | -81.97%            | -66.51% |    -0.41 |       82 | 49.62%     | ok               |

## ABBV Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 0.10%    | 39.92%             | -26.16% |     0.09 |       50 | 38.94%     | ok               |
|          40 | -9.61%   | 39.92%             | -26.61% |    -0.16 |       64 | 43.59%     | ok               |
|          35 | -10.90%  | 39.92%             | -27.83% |    -0.19 |       66 | 46.42%     | ok               |
|          30 | -13.21%  | 39.92%             | -30.55% |    -0.24 |       64 | 49.25%     | ok               |
|          45 | -12.43%  | 39.92%             | -29.59% |    -0.24 |       54 | 40.93%     | ok               |

## ADA-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -83.63%  | -85.05%            | -91.37% |    -0.57 |       80 | 61.49%     | ok               |
|          20 | -83.64%  | -85.05%            | -91.89% |    -0.59 |       84 | 56.70%     | ok               |
|          45 | -81.17%  | -85.05%            | -89.98% |    -0.66 |       62 | 31.80%     | ok               |
|          25 | -84.80%  | -85.05%            | -91.94% |    -0.66 |       83 | 53.45%     | ok               |
|          50 | -80.76%  | -85.05%            | -88.27% |    -0.69 |       57 | 27.78%     | ok               |

## ADBE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 10.63%   | -57.85%            | -21.34% |     0.3  |       76 | 49.25%     | ok               |
|          40 | -3.65%   | -57.85%            | -20.88% |     0.05 |       72 | 42.26%     | ok               |
|          25 | -7.34%   | -57.85%            | -31.29% |     0.04 |       50 | 61.06%     | ok               |
|          15 | -17.23%  | -57.85%            | -31.86% |    -0.11 |       61 | 65.72%     | ok               |
|          20 | -18.85%  | -57.85%            | -34.42% |    -0.14 |       50 | 63.23%     | ok               |

## AGG Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -5.75%   | -0.94%             | -7.89%  |    -1.16 |       52 | 20.47%     | ok               |
|          30 | -7.13%   | -0.94%             | -9.93%  |    -1.17 |       69 | 31.11%     | ok               |
|          20 | -8.40%   | -0.94%             | -10.85% |    -1.22 |       75 | 36.77%     | ok               |
|          50 | -5.57%   | -0.94%             | -7.92%  |    -1.25 |       46 | 16.97%     | ok               |
|          25 | -8.68%   | -0.94%             | -11.38% |    -1.32 |       73 | 34.94%     | ok               |

## ALGO-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -55.03%  | -77.61%            | -61.38% |    -0.66 |       86 | 38.51%     | ok               |
|          15 | -63.37%  | -77.61%            | -71.69% |    -0.71 |       78 | 50.00%     | ok               |
|          35 | -56.21%  | -77.61%            | -58.15% |    -0.82 |       64 | 31.61%     | ok               |
|          25 | -65.43%  | -77.61%            | -75.85% |    -0.82 |       84 | 45.40%     | ok               |
|          20 | -67.25%  | -77.61%            | -74.73% |    -0.84 |       82 | 47.89%     | ok               |

## AMAT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -5.33%   | 199.51%            | -54.69% |     0.12 |       66 | 62.40%     | ok               |
|          30 | -19.38%  | 199.51%            | -57.80% |    -0.1  |       67 | 53.58%     | ok               |
|          20 | -25.27%  | 199.51%            | -60.72% |    -0.17 |       70 | 58.74%     | ok               |
|          35 | -25.12%  | 199.51%            | -55.89% |    -0.21 |       69 | 51.41%     | ok               |
|          25 | -28.77%  | 199.51%            | -60.95% |    -0.25 |       69 | 56.41%     | ok               |

## AMD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 32.54%   | 218.22%            | -47.17% |     0.49 |       56 | 38.94%     | ok               |
|          50 | 23.87%   | 218.22%            | -48.79% |     0.43 |       60 | 33.44%     | ok               |
|          35 | 15.64%   | 218.22%            | -54.57% |     0.36 |       62 | 40.93%     | ok               |
|          45 | 5.89%    | 218.22%            | -56.22% |     0.27 |       64 | 36.27%     | ok               |
|          30 | 0.39%    | 218.22%            | -59.88% |     0.23 |       63 | 43.43%     | ok               |

## AMGN Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -13.01%  | 14.05%             | -26.64% |    -0.19 |       73 | 55.24%     | ok               |
|          15 | -16.25%  | 14.05%             | -27.92% |    -0.25 |       71 | 61.06%     | ok               |
|          35 | -14.40%  | 14.05%             | -31.23% |    -0.25 |       67 | 45.26%     | ok               |
|          30 | -18.40%  | 14.05%             | -34.14% |    -0.35 |       71 | 49.08%     | ok               |
|          25 | -21.72%  | 14.05%             | -33.41% |    -0.43 |       67 | 51.41%     | ok               |

## AMZN Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -17.83%  | 59.12%             | -28.70% |    -0.52 |       50 | 29.78%     | ok               |
|          50 | -25.03%  | 59.12%             | -35.48% |    -0.88 |       48 | 24.13%     | ok               |
|          45 | -25.89%  | 59.12%             | -35.47% |    -0.89 |       50 | 26.96%     | ok               |
|          35 | -29.70%  | 59.12%             | -38.29% |    -0.91 |       62 | 32.95%     | ok               |
|          30 | -33.84%  | 59.12%             | -42.48% |    -0.99 |       74 | 38.27%     | ok               |

## APT-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 54.97%   | -93.25%            | -46.73% |     0.77 |       44 | 19.16%     | ok               |
|          45 | 12.94%   | -93.25%            | -63.86% |     0.35 |       62 | 25.67%     | ok               |
|          40 | -8.75%   | -93.25%            | -63.33% |     0.14 |       68 | 31.23%     | ok               |
|          35 | -15.30%  | -93.25%            | -64.45% |     0.09 |       72 | 36.78%     | ok               |
|          20 | -24.49%  | -93.25%            | -70.51% |     0.04 |       73 | 50.77%     | ok               |

## ARB-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 64.14%   | -90.12%            | -53.74% |     0.69 |       87 | 55.17%     | ok               |
|          40 | 49.80%   | -90.12%            | -47.60% |     0.65 |       52 | 30.08%     | ok               |
|          35 | 40.06%   | -90.12%            | -56.00% |     0.57 |       64 | 33.72%     | ok               |
|          20 | 35.77%   | -90.12%            | -60.40% |     0.54 |       77 | 49.81%     | ok               |
|          45 | 26.17%   | -90.12%            | -50.83% |     0.47 |       58 | 23.37%     | ok               |

## ARKK Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -27.38%  | 57.22%             | -35.82% |    -0.35 |       94 | 50.58%     | ok               |
|          20 | -30.68%  | 57.22%             | -34.90% |    -0.44 |       87 | 45.76%     | ok               |
|          30 | -32.67%  | 57.22%             | -35.19% |    -0.57 |       81 | 38.94%     | ok               |
|          35 | -33.82%  | 57.22%             | -36.30% |    -0.63 |       80 | 36.61%     | ok               |
|          40 | -35.22%  | 57.22%             | -36.71% |    -0.71 |       72 | 31.78%     | ok               |

## ATOM-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -58.85%  | -76.95%            | -68.50% |    -0.81 |       93 | 50.57%     | ok               |
|          15 | -64.28%  | -76.95%            | -73.24% |    -0.87 |       94 | 60.54%     | ok               |
|          30 | -62.00%  | -76.95%            | -70.27% |    -0.96 |       88 | 43.87%     | ok               |
|          45 | -56.07%  | -76.95%            | -60.60% |    -1.03 |       72 | 28.54%     | ok               |
|          20 | -68.42%  | -76.95%            | -73.22% |    -1.06 |      103 | 54.79%     | ok               |

## AVAX-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 12.54%   | -84.01%            | -32.41% |     0.34 |       36 | 19.73%     | ok               |
|          40 | 3.40%    | -84.01%            | -39.29% |     0.23 |       44 | 25.48%     | ok               |
|          45 | 2.96%    | -84.01%            | -39.20% |     0.22 |       40 | 22.80%     | ok               |
|          15 | -5.97%   | -84.01%            | -52.46% |     0.2  |       63 | 51.53%     | ok               |
|          35 | -3.98%   | -84.01%            | -42.28% |     0.15 |       60 | 30.84%     | ok               |

## AVGO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 43.82%   | 248.23%            | -35.76% |     0.6  |       60 | 46.76%     | ok               |
|          25 | 38.70%   | 248.23%            | -38.01% |     0.56 |       64 | 47.42%     | ok               |
|          35 | 34.03%   | 248.23%            | -36.19% |     0.52 |       70 | 44.09%     | ok               |
|          40 | 28.80%   | 248.23%            | -40.70% |     0.48 |       62 | 40.77%     | ok               |
|          20 | 25.59%   | 248.23%            | -40.10% |     0.44 |       72 | 50.25%     | ok               |

## BA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 18.43%   | -1.03%             | -15.40% |     0.51 |       46 | 31.78%     | ok               |
|          35 | 23.42%   | -1.03%             | -23.77% |     0.49 |       74 | 46.59%     | ok               |
|          25 | 4.84%    | -1.03%             | -32.48% |     0.21 |       72 | 54.74%     | ok               |
|          40 | 4.31%    | -1.03%             | -29.44% |     0.19 |       52 | 40.10%     | ok               |
|          30 | 1.80%    | -1.03%             | -30.56% |     0.16 |       69 | 51.25%     | ok               |

## BAC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -12.19%  | 64.12%             | -21.48% |    -0.23 |       82 | 50.42%     | ok               |
|          45 | -9.88%   | 64.12%             | -21.23% |    -0.27 |       62 | 33.94%     | ok               |
|          50 | -11.35%  | 64.12%             | -19.75% |    -0.35 |       60 | 30.78%     | ok               |
|          35 | -13.83%  | 64.12%             | -29.13% |    -0.36 |       72 | 41.76%     | ok               |
|          15 | -17.63%  | 64.12%             | -23.70% |    -0.36 |       84 | 56.07%     | ok               |

## BCH-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -11.73%  | -52.04%            | -48.02% |     0.08 |       75 | 52.49%     | ok               |
|          25 | -16.72%  | -52.04%            | -51.09% |     0.01 |       72 | 48.08%     | ok               |
|          30 | -16.12%  | -52.04%            | -53.87% |     0    |       78 | 45.98%     | ok               |
|          15 | -21.83%  | -52.04%            | -55.01% |    -0.03 |       84 | 57.09%     | ok               |
|          40 | -28.79%  | -52.04%            | -60.69% |    -0.22 |       65 | 39.08%     | ok               |

## BITO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 26.95%   | -60.97%            | -32.29% |     0.48 |       54 | 24.46%     | ok               |
|          30 | 12.09%   | -60.97%            | -42.82% |     0.31 |       78 | 39.10%     | ok               |
|          15 | 5.06%    | -60.97%            | -48.38% |     0.25 |       87 | 47.92%     | ok               |
|          45 | 5.88%    | -60.97%            | -43.53% |     0.23 |       58 | 27.45%     | ok               |
|          40 | 4.41%    | -60.97%            | -45.94% |     0.22 |       64 | 31.95%     | ok               |

## BLK Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 4.16%    | 24.51%             | -14.19% |     0.19 |       82 | 38.10%     | ok               |
|          40 | 3.26%    | 24.51%             | -15.20% |     0.17 |       72 | 33.78%     | ok               |
|          20 | 0.05%    | 24.51%             | -17.89% |     0.08 |       77 | 46.59%     | ok               |
|          30 | -2.44%   | 24.51%             | -20.81% |    -0    |       77 | 41.93%     | ok               |
|          25 | -3.42%   | 24.51%             | -19.84% |    -0.03 |       77 | 44.26%     | ok               |

## BND Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -7.48%   | -0.86%             | -9.32%  |    -1.08 |       67 | 38.60%     | ok               |
|          30 | -7.32%   | -0.86%             | -9.89%  |    -1.18 |       65 | 32.28%     | ok               |
|          25 | -7.86%   | -0.86%             | -10.40% |    -1.19 |       69 | 36.11%     | ok               |
|          15 | -9.66%   | -0.86%             | -10.85% |    -1.39 |       77 | 41.60%     | ok               |
|          45 | -7.22%   | -0.86%             | -9.57%  |    -1.39 |       50 | 22.13%     | ok               |

## BONK-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 159.76%  | -87.89%            | -35.57% |     1.2  |       48 | 22.22%     | ok               |
|          25 | 167.02%  | -87.89%            | -51.34% |     1.03 |       69 | 47.51%     | ok               |
|          15 | 167.76%  | -87.89%            | -62.48% |     1    |       70 | 56.32%     | ok               |
|          20 | 151.93%  | -87.89%            | -58.35% |     0.98 |       69 | 52.11%     | ok               |
|          40 | 82.73%   | -87.89%            | -53.34% |     0.79 |       54 | 33.72%     | ok               |

## BTC-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 47.45%   | -35.82%            | -18.97% |     0.86 |       46 | 33.91%     | ok               |
|          45 | 43.95%   | -35.82%            | -19.59% |     0.85 |       44 | 30.27%     | ok               |
|          35 | 27.43%   | -35.82%            | -31.52% |     0.56 |       70 | 41.00%     | ok               |
|          50 | 15.20%   | -35.82%            | -17.58% |     0.42 |       42 | 25.48%     | ok               |
|          30 | 9.41%    | -35.82%            | -27.92% |     0.29 |       72 | 47.89%     | ok               |

## C Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -12.51%  | 151.75%            | -22.28% |    -0.3  |       68 | 34.94%     | ok               |
|          15 | -25.75%  | 151.75%            | -34.34% |    -0.45 |       74 | 59.57%     | ok               |
|          25 | -24.47%  | 151.75%            | -33.83% |    -0.45 |       75 | 52.75%     | ok               |
|          20 | -26.37%  | 151.75%            | -34.89% |    -0.49 |       81 | 55.91%     | ok               |
|          45 | -21.65%  | 151.75%            | -29.85% |    -0.54 |       82 | 39.60%     | ok               |

## CAT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 29.61%   | 211.38%            | -21.02% |     0.56 |       74 | 57.40%     | ok               |
|          25 | 29.73%   | 211.38%            | -26.37% |     0.56 |       70 | 60.23%     | ok               |
|          20 | 27.10%   | 211.38%            | -25.65% |     0.52 |       80 | 63.56%     | ok               |
|          45 | 21.30%   | 211.38%            | -28.85% |     0.46 |       58 | 45.76%     | ok               |
|          15 | 20.06%   | 211.38%            | -30.60% |     0.42 |       73 | 69.88%     | ok               |

## CL Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 21.25%   | 9.48%              | -14.32% |     0.7  |       58 | 49.25%     | ok               |
|          50 | 17.02%   | 9.48%              | -12.98% |     0.69 |       44 | 32.95%     | ok               |
|          45 | 15.00%   | 9.48%              | -13.51% |     0.6  |       46 | 35.77%     | ok               |
|          35 | 13.80%   | 9.48%              | -13.83% |     0.5  |       62 | 45.42%     | ok               |
|          40 | 10.50%   | 9.48%              | -12.70% |     0.43 |       56 | 40.10%     | ok               |

## CMCSA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -35.49%  | -40.88%            | -49.03% |    -0.78 |       86 | 58.90%     | ok               |
|          30 | -37.38%  | -40.88%            | -41.09% |    -0.95 |       82 | 44.43%     | ok               |
|          20 | -42.56%  | -40.88%            | -47.23% |    -1.07 |       93 | 55.07%     | ok               |
|          50 | -29.51%  | -40.88%            | -33.68% |    -1.08 |       50 | 17.14%     | ok               |
|          25 | -42.43%  | -40.88%            | -45.84% |    -1.1  |       89 | 49.25%     | ok               |

## COMP-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -14.13%  | -80.71%            | -38.71% |     0.01 |       48 | 21.07%     | ok               |
|          30 | -34.85%  | -80.71%            | -60.50% |    -0.18 |       91 | 45.59%     | ok               |
|          25 | -38.18%  | -80.71%            | -60.58% |    -0.2  |       91 | 50.77%     | ok               |
|          15 | -46.39%  | -80.71%            | -65.55% |    -0.28 |      105 | 62.26%     | ok               |
|          40 | -41.24%  | -80.71%            | -48.69% |    -0.37 |       76 | 33.91%     | ok               |

## COP Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -13.41%  | 4.87%              | -34.85% |    -0.24 |       52 | 27.79%     | ok               |
|          45 | -20.66%  | 4.87%              | -41.14% |    -0.43 |       64 | 30.62%     | ok               |
|          30 | -25.45%  | 4.87%              | -43.99% |    -0.48 |       77 | 41.60%     | ok               |
|          35 | -25.31%  | 4.87%              | -43.88% |    -0.49 |       79 | 37.94%     | ok               |
|          25 | -33.73%  | 4.87%              | -49.53% |    -0.67 |       90 | 46.09%     | ok               |

## COST Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | 18.75%   | 42.24%             | -24.73% |     0.56 |       63 | 50.58%     | ok               |
|          20 | 18.13%   | 42.24%             | -24.32% |     0.54 |       64 | 53.08%     | ok               |
|          35 | 11.92%   | 42.24%             | -26.58% |     0.42 |       56 | 44.09%     | ok               |
|          30 | 6.80%    | 42.24%             | -29.73% |     0.27 |       62 | 47.09%     | ok               |
|          40 | 5.05%    | 42.24%             | -28.41% |     0.22 |       58 | 41.10%     | ok               |

## CRM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -29.21%  | -31.73%            | -38.20% |    -0.42 |       90 | 55.24%     | ok               |
|          35 | -23.39%  | -31.73%            | -35.48% |    -0.43 |       62 | 38.77%     | ok               |
|          40 | -30.31%  | -31.73%            | -41.30% |    -0.68 |       68 | 34.94%     | ok               |
|          30 | -34.20%  | -31.73%            | -40.31% |    -0.68 |       65 | 43.59%     | ok               |
|          20 | -39.65%  | -31.73%            | -41.96% |    -0.73 |       78 | 48.92%     | ok               |

## CRV-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 47.43%   | -81.97%            | -37.78% |     0.64 |       60 | 28.16%     | ok               |
|          40 | 29.46%   | -81.97%            | -38.86% |     0.5  |       50 | 24.52%     | ok               |
|          50 | 23.26%   | -81.97%            | -29.30% |     0.45 |       38 | 16.48%     | ok               |
|          30 | 17.80%   | -81.97%            | -39.89% |     0.4  |       60 | 32.57%     | ok               |
|          45 | 17.23%   | -81.97%            | -42.29% |     0.39 |       50 | 19.35%     | ok               |

## CSCO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 31.53%   | 141.64%            | -19.34% |     0.69 |       56 | 38.27%     | ok               |
|          45 | 28.12%   | 141.64%            | -19.34% |     0.62 |       51 | 40.43%     | ok               |
|          25 | 26.79%   | 141.64%            | -23.28% |     0.56 |       65 | 51.25%     | ok               |
|          30 | 25.58%   | 141.64%            | -21.79% |     0.55 |       61 | 49.08%     | ok               |
|          35 | 23.21%   | 141.64%            | -23.68% |     0.51 |       53 | 46.76%     | ok               |

## CVX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -11.65%  | 27.19%             | -25.38% |    -0.25 |       72 | 44.09%     | ok               |
|          20 | -15.45%  | 27.19%             | -29.29% |    -0.36 |       76 | 45.42%     | ok               |
|          30 | -16.18%  | 27.19%             | -28.37% |    -0.41 |       73 | 41.60%     | ok               |
|          35 | -15.84%  | 27.19%             | -28.85% |    -0.41 |       69 | 38.60%     | ok               |
|          45 | -16.35%  | 27.19%             | -28.83% |    -0.49 |       65 | 31.28%     | ok               |

## DASH-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 110.05%  | -14.85%            | -35.01% |     0.88 |       44 | 16.48%     | ok               |
|          40 | 65.85%   | -14.85%            | -34.44% |     0.68 |       48 | 22.80%     | ok               |
|          45 | 51.69%   | -14.85%            | -42.78% |     0.6  |       48 | 18.77%     | ok               |
|          25 | -39.68%  | -14.85%            | -64.14% |     0.02 |       73 | 33.52%     | ok               |
|          35 | -39.50%  | -14.85%            | -63.23% |     0.01 |       73 | 27.20%     | ok               |

## DBC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | -10.31%  | 32.50%             | -23.91% |    -0.34 |       60 | 31.45%     | ok               |
|          50 | -8.98%   | 32.50%             | -20.31% |    -0.34 |       42 | 21.13%     | ok               |
|          45 | -10.35%  | 32.50%             | -21.46% |    -0.37 |       54 | 24.46%     | ok               |
|          15 | -12.56%  | 32.50%             | -27.14% |    -0.41 |       65 | 37.77%     | ok               |
|          25 | -13.59%  | 32.50%             | -26.10% |    -0.47 |       64 | 35.27%     | ok               |

## DE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -6.66%   | 50.95%             | -28.94% |    -0.05 |       74 | 50.92%     | ok               |
|          25 | -8.97%   | 50.95%             | -26.67% |    -0.11 |       76 | 48.25%     | ok               |
|          30 | -10.61%  | 50.95%             | -25.72% |    -0.15 |       76 | 45.26%     | ok               |
|          50 | -8.74%   | 50.95%             | -23.74% |    -0.18 |       62 | 29.62%     | ok               |
|          45 | -11.36%  | 50.95%             | -26.80% |    -0.23 |       66 | 34.11%     | ok               |

## DIA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | 0.25%    | 35.59%             | -11.28% |     0.05 |       60 | 47.09%     | ok               |
|          35 | -0.27%   | 35.59%             | -13.15% |     0.02 |       60 | 43.76%     | ok               |
|          30 | -1.41%   | 35.59%             | -12.94% |    -0.04 |       60 | 45.76%     | ok               |
|          20 | -2.58%   | 35.59%             | -13.85% |    -0.09 |       62 | 49.58%     | ok               |
|          40 | -4.10%   | 35.59%             | -15.06% |    -0.2  |       66 | 40.77%     | ok               |

## DIS Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 39.55%   | 10.36%             | -14.24% |     0.95 |       48 | 30.45%     | ok               |
|          45 | 9.42%    | 10.36%             | -15.09% |     0.3  |       51 | 33.78%     | ok               |
|          40 | 8.44%    | 10.36%             | -22.77% |     0.27 |       63 | 38.94%     | ok               |
|          35 | 5.24%    | 10.36%             | -21.13% |     0.21 |       71 | 44.76%     | ok               |
|          15 | 1.43%    | 10.36%             | -26.13% |     0.14 |       87 | 58.07%     | ok               |

## DOGE-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 6.28%    | -77.53%            | -57.89% |     0.34 |       81 | 64.75%     | ok               |
|          20 | -5.53%   | -77.53%            | -55.83% |     0.23 |       84 | 60.54%     | ok               |
|          25 | -9.12%   | -77.53%            | -53.72% |     0.19 |       72 | 54.98%     | ok               |
|          30 | -21.48%  | -77.53%            | -60.95% |     0.04 |       77 | 49.62%     | ok               |
|          35 | -48.58%  | -77.53%            | -65.95% |    -0.43 |       74 | 42.91%     | ok               |

## DOT-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -28.84%  | -87.55%            | -48.53% |    -0.24 |       54 | 30.46%     | ok               |
|          50 | -27.11%  | -87.55%            | -44.94% |    -0.24 |       56 | 26.63%     | ok               |
|          40 | -36.60%  | -87.55%            | -48.38% |    -0.34 |       58 | 33.91%     | ok               |
|          35 | -47.14%  | -87.55%            | -59.66% |    -0.37 |       82 | 41.00%     | ok               |
|          30 | -49.81%  | -87.55%            | -59.34% |    -0.4  |       92 | 47.51%     | ok               |

## DXY-INDEX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -3.67%   | -3.06%             | -9.98%  |    -0.4  |       70 | 59.00%     | ok               |
|          15 | -4.81%   | -3.06%             | -11.57% |    -0.43 |       90 | 75.70%     | ok               |
|          50 | -3.18%   | -3.06%             | -6.06%  |    -0.51 |       44 | 27.33%     | ok               |
|          35 | -4.74%   | -3.06%             | -10.12% |    -0.56 |       75 | 54.01%     | ok               |
|          25 | -5.32%   | -3.06%             | -12.52% |    -0.56 |       82 | 64.21%     | ok               |

## EEM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -4.96%   | 64.77%             | -19.52% |    -0.11 |       64 | 39.77%     | ok               |
|          35 | -5.62%   | 64.77%             | -23.88% |    -0.12 |       66 | 41.76%     | ok               |
|          50 | -4.94%   | 64.77%             | -15.88% |    -0.12 |       52 | 35.77%     | ok               |
|          45 | -6.04%   | 64.77%             | -17.36% |    -0.16 |       54 | 37.44%     | ok               |
|          30 | -9.40%   | 64.77%             | -25.67% |    -0.25 |       64 | 43.43%     | ok               |

## EFA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -1.76%   | 36.22%             | -11.27% |    -0    |       58 | 51.41%     | ok               |
|          20 | -7.98%   | 36.22%             | -12.37% |    -0.26 |       63 | 48.59%     | ok               |
|          30 | -8.43%   | 36.22%             | -13.53% |    -0.31 |       58 | 43.59%     | ok               |
|          25 | -10.49%  | 36.22%             | -15.78% |    -0.39 |       62 | 46.26%     | ok               |
|          50 | -9.07%   | 36.22%             | -17.56% |    -0.4  |       54 | 36.27%     | ok               |

## EOG Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -23.61%  | 18.72%             | -39.69% |    -0.58 |       56 | 33.44%     | ok               |
|          50 | -24.73%  | 18.72%             | -40.57% |    -0.64 |       60 | 30.62%     | ok               |
|          30 | -29.95%  | 18.72%             | -48.13% |    -0.69 |       83 | 47.75%     | ok               |
|          25 | -31.71%  | 18.72%             | -51.99% |    -0.7  |       84 | 51.08%     | ok               |
|          40 | -28.13%  | 18.72%             | -43.26% |    -0.72 |       64 | 36.77%     | ok               |

## ETC-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -12.79%  | -75.31%            | -30.24% |    -0.11 |       28 | 17.43%     | ok               |
|          35 | -20.48%  | -75.31%            | -42.62% |    -0.2  |       46 | 26.63%     | ok               |
|          45 | -20.74%  | -75.31%            | -36.69% |    -0.26 |       28 | 19.16%     | ok               |
|          40 | -24.95%  | -75.31%            | -41.87% |    -0.34 |       42 | 22.61%     | ok               |
|          30 | -39.81%  | -75.31%            | -53.13% |    -0.6  |       66 | 30.84%     | ok               |

## ETH-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 148.37%  | -53.46%            | -30.11% |     1.23 |       62 | 44.44%     | ok               |
|          30 | 140.06%  | -53.46%            | -32.89% |     1.15 |       66 | 52.30%     | ok               |
|          40 | 57.06%   | -53.46%            | -33.11% |     0.75 |       58 | 36.97%     | ok               |
|          45 | 38.33%   | -53.46%            | -34.50% |     0.6  |       54 | 33.14%     | ok               |
|          50 | 23.43%   | -53.46%            | -30.50% |     0.46 |       56 | 27.01%     | ok               |

## EWJ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -18.27%  | 36.56%             | -30.73% |    -0.59 |       64 | 41.43%     | ok               |
|          20 | -19.65%  | 36.56%             | -31.32% |    -0.62 |       60 | 43.43%     | ok               |
|          25 | -21.97%  | 36.56%             | -31.18% |    -0.72 |       60 | 42.43%     | ok               |
|          35 | -22.19%  | 36.56%             | -32.54% |    -0.75 |       70 | 39.77%     | ok               |
|          15 | -24.97%  | 36.56%             | -32.24% |    -0.78 |       74 | 46.59%     | ok               |

## FCX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -10.23%  | 54.79%             | -27.80% |    -0.04 |       56 | 29.62%     | ok               |
|          45 | -15.20%  | 54.79%             | -35.28% |    -0.12 |       56 | 33.78%     | ok               |
|          40 | -27.62%  | 54.79%             | -44.23% |    -0.35 |       68 | 38.77%     | ok               |
|          30 | -36.12%  | 54.79%             | -48.09% |    -0.48 |       71 | 45.59%     | ok               |
|          35 | -37.08%  | 54.79%             | -51.29% |    -0.53 |       75 | 43.43%     | ok               |

## FET-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 30.87%   | -86.10%            | -56.84% |     0.52 |       88 | 50.57%     | ok               |
|          15 | -3.03%   | -86.10%            | -59.22% |     0.3  |       87 | 53.64%     | ok               |
|          25 | -15.63%  | -86.10%            | -57.43% |     0.17 |       91 | 44.06%     | ok               |
|          30 | -19.14%  | -86.10%            | -54.02% |     0.11 |       79 | 39.85%     | ok               |
|          45 | -28.89%  | -86.10%            | -48.61% |    -0.19 |       54 | 19.16%     | ok               |

## FIL-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -5.73%   | -86.48%            | -39.40% |     0.1  |       48 | 23.56%     | ok               |
|          35 | -28.83%  | -86.48%            | -45.85% |    -0.23 |       58 | 27.59%     | ok               |
|          45 | -27.10%  | -86.48%            | -40.90% |    -0.27 |       44 | 17.82%     | ok               |
|          30 | -32.70%  | -86.48%            | -46.54% |    -0.27 |       70 | 32.95%     | ok               |
|          50 | -26.98%  | -86.48%            | -44.97% |    -0.31 |       38 | 13.60%     | ok               |

## FXI Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -11.57%  | 52.88%             | -22.99% |    -0.21 |       50 | 28.29%     | ok               |
|          50 | -10.86%  | 52.88%             | -23.27% |    -0.23 |       38 | 19.47%     | ok               |
|          30 | -12.08%  | 52.88%             | -24.33% |    -0.23 |       50 | 27.12%     | ok               |
|          15 | -13.03%  | 52.88%             | -21.68% |    -0.24 |       54 | 31.78%     | ok               |
|          45 | -13.15%  | 52.88%             | -26.75% |    -0.29 |       44 | 21.80%     | ok               |

## GDX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 25.00%   | 165.45%            | -31.87% |     0.51 |       60 | 43.43%     | ok               |
|          20 | 19.56%   | 165.45%            | -35.59% |     0.41 |       71 | 53.41%     | ok               |
|          35 | 13.49%   | 165.45%            | -32.37% |     0.34 |       66 | 45.76%     | ok               |
|          30 | 8.90%    | 165.45%            | -34.99% |     0.27 |       60 | 48.75%     | ok               |
|          25 | 8.12%    | 165.45%            | -33.46% |     0.26 |       61 | 50.25%     | ok               |

## GDXJ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -8.12%   | 176.65%            | -45.05% |     0.05 |       65 | 52.91%     | ok               |
|          50 | -8.38%   | 176.65%            | -35.02% |    -0.02 |       58 | 37.27%     | ok               |
|          30 | -18.63%  | 176.65%            | -44.93% |    -0.16 |       66 | 46.09%     | ok               |
|          40 | -20.36%  | 176.65%            | -44.27% |    -0.22 |       64 | 42.10%     | ok               |
|          25 | -24.06%  | 176.65%            | -47.26% |    -0.22 |       69 | 49.42%     | ok               |

## GE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 22.97%   | 216.65%            | -22.29% |     0.51 |       68 | 37.94%     | ok               |
|          45 | 14.73%   | 216.65%            | -25.68% |     0.37 |       78 | 40.93%     | ok               |
|          20 | 15.45%   | 216.65%            | -26.63% |     0.37 |       71 | 54.91%     | ok               |
|          15 | 10.52%   | 216.65%            | -28.62% |     0.29 |       70 | 57.24%     | ok               |
|          35 | 10.27%   | 216.65%            | -27.11% |     0.29 |       82 | 46.42%     | ok               |

## GLD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | 25.01%   | 108.87%            | -14.61% |     0.65 |       48 | 44.59%     | ok               |
|          20 | 23.14%   | 108.87%            | -14.61% |     0.61 |       50 | 45.92%     | ok               |
|          30 | 19.09%   | 108.87%            | -16.63% |     0.54 |       48 | 43.43%     | ok               |
|          15 | 15.09%   | 108.87%            | -17.54% |     0.43 |       54 | 50.25%     | ok               |
|          35 | 13.28%   | 108.87%            | -17.29% |     0.41 |       50 | 42.76%     | ok               |

## GOOGL Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 83.40%   | 158.35%            | -20.41% |     1.2  |       65 | 54.58%     | ok               |
|          25 | 81.70%   | 158.35%            | -19.76% |     1.18 |       59 | 56.91%     | ok               |
|          35 | 67.26%   | 158.35%            | -22.85% |     1.1  |       71 | 49.42%     | ok               |
|          20 | 68.03%   | 158.35%            | -20.57% |     1.03 |       70 | 59.23%     | ok               |
|          15 | 70.58%   | 158.35%            | -13.59% |     1.02 |       71 | 64.39%     | ok               |

## GRT-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 34.00%   | -91.74%            | -30.00% |     0.58 |       40 | 21.07%     | ok               |
|          45 | 4.28%    | -91.74%            | -48.76% |     0.24 |       48 | 25.48%     | ok               |
|          15 | -3.86%   | -91.74%            | -49.67% |     0.22 |       75 | 59.77%     | ok               |
|          20 | -4.40%   | -91.74%            | -46.47% |     0.21 |       83 | 54.79%     | ok               |
|          35 | -1.57%   | -91.74%            | -49.87% |     0.19 |       60 | 34.29%     | ok               |

## GS Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 26.02%   | 174.96%            | -20.56% |     0.55 |       76 | 59.57%     | ok               |
|          20 | 8.83%    | 174.96%            | -23.19% |     0.27 |       76 | 55.57%     | ok               |
|          25 | 5.39%    | 174.96%            | -23.32% |     0.21 |       76 | 53.08%     | ok               |
|          40 | 0.64%    | 174.96%            | -17.88% |     0.1  |       74 | 43.93%     | ok               |
|          30 | -0.74%   | 174.96%            | -22.13% |     0.08 |       78 | 50.58%     | ok               |

## HD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -4.23%   | -12.63%            | -17.69% |    -0.04 |       69 | 44.76%     | ok               |
|          25 | -4.98%   | -12.63%            | -18.51% |    -0.05 |       68 | 46.76%     | ok               |
|          40 | -9.89%   | -12.63%            | -20.58% |    -0.25 |       80 | 34.94%     | ok               |
|          35 | -13.15%  | -12.63%            | -22.98% |    -0.32 |       76 | 41.10%     | ok               |
|          45 | -13.30%  | -12.63%            | -21.91% |    -0.39 |       62 | 29.78%     | ok               |

## HON Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -17.09%  | 12.89%             | -23.31% |    -0.53 |       74 | 32.11%     | ok               |
|          45 | -19.07%  | 12.89%             | -22.37% |    -0.56 |       78 | 37.27%     | ok               |
|          40 | -21.97%  | 12.89%             | -22.77% |    -0.63 |       78 | 41.43%     | ok               |
|          35 | -23.47%  | 12.89%             | -25.91% |    -0.66 |       93 | 47.75%     | ok               |
|          30 | -25.95%  | 12.89%             | -27.46% |    -0.72 |       93 | 52.58%     | ok               |

## HYG Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -8.61%   | 2.23%              | -8.00%  |    -1.04 |       72 | 29.45%     | ok               |
|          15 | -10.27%  | 2.23%              | -10.29% |    -1.11 |       90 | 41.60%     | ok               |
|          20 | -10.20%  | 2.23%              | -10.29% |    -1.14 |       88 | 39.27%     | ok               |
|          45 | -9.29%   | 2.23%              | -8.68%  |    -1.17 |       68 | 26.29%     | ok               |
|          25 | -10.39%  | 2.23%              | -10.11% |    -1.17 |       85 | 36.94%     | ok               |

## IBIT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 60.04%   | -10.18%            | -12.64% |     1.22 |       20 | 21.34%     | ok               |
|          15 | 73.34%   | -10.18%            | -19.20% |     1.2  |       38 | 37.22%     | ok               |
|          45 | 51.15%   | -10.18%            | -17.12% |     1.06 |       22 | 22.08%     | ok               |
|          40 | 49.66%   | -10.18%            | -17.12% |     1.03 |       24 | 23.57%     | ok               |
|          30 | 42.82%   | -10.18%            | -18.95% |     0.88 |       32 | 29.28%     | ok               |

## IBM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 39.07%   | 71.80%             | -28.20% |     0.69 |       87 | 62.73%     | ok               |
|          30 | 34.19%   | 71.80%             | -25.31% |     0.69 |       72 | 50.92%     | ok               |
|          35 | 31.51%   | 71.80%             | -25.15% |     0.65 |       68 | 46.59%     | ok               |
|          45 | 26.94%   | 71.80%             | -18.33% |     0.61 |       54 | 37.60%     | ok               |
|          40 | 23.21%   | 71.80%             | -24.66% |     0.54 |       64 | 41.26%     | ok               |

## ICP-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 20.44%   | -80.99%            | -29.38% |     0.42 |       58 | 27.20%     | ok               |
|          35 | 8.90%    | -80.99%            | -45.97% |     0.31 |       68 | 32.57%     | ok               |
|          50 | 4.33%    | -80.99%            | -37.33% |     0.24 |       40 | 17.24%     | ok               |
|          30 | -5.61%   | -80.99%            | -55.67% |     0.21 |       83 | 38.70%     | ok               |
|          45 | -8.72%   | -80.99%            | -38.80% |     0.08 |       58 | 21.26%     | ok               |

## IEF Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -8.11%   | -2.71%             | -10.09% |    -0.97 |       72 | 42.10%     | ok               |
|          15 | -8.66%   | -2.71%             | -10.82% |    -1.02 |       71 | 43.59%     | ok               |
|          40 | -8.39%   | -2.71%             | -9.67%  |    -1.31 |       60 | 24.79%     | ok               |
|          45 | -8.07%   | -2.71%             | -9.73%  |    -1.33 |       50 | 22.80%     | ok               |
|          50 | -8.13%   | -2.71%             | -9.17%  |    -1.45 |       52 | 20.30%     | ok               |

## IEMG Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | -0.32%   | 59.01%             | -22.13% |     0.05 |       63 | 42.60%     | ok               |
|          50 | -1.54%   | 59.01%             | -13.91% |    -0    |       54 | 34.28%     | ok               |
|          40 | -2.44%   | 59.01%             | -18.43% |    -0.03 |       60 | 39.93%     | ok               |
|          45 | -2.35%   | 59.01%             | -14.92% |    -0.03 |       50 | 36.77%     | ok               |
|          25 | -4.72%   | 59.01%             | -25.58% |    -0.09 |       59 | 45.42%     | ok               |

## INJ-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -14.36%  | -76.19%            | -54.43% |     0.01 |       44 | 23.56%     | ok               |
|          35 | -22.54%  | -76.19%            | -61.03% |    -0.03 |       62 | 33.52%     | ok               |
|          50 | -24.86%  | -76.19%            | -49.35% |    -0.18 |       48 | 19.92%     | ok               |
|          40 | -30.49%  | -76.19%            | -60.61% |    -0.19 |       52 | 29.69%     | ok               |
|          25 | -55.78%  | -76.19%            | -81.57% |    -0.48 |       77 | 44.06%     | ok               |

## INTC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 76.11%   | 110.46%            | -49.32% |     0.74 |       60 | 34.28%     | ok               |
|          15 | 78.72%   | 110.46%            | -53.65% |     0.72 |       86 | 61.56%     | ok               |
|          25 | 75.17%   | 110.46%            | -56.41% |     0.71 |       77 | 51.75%     | ok               |
|          40 | 70.01%   | 110.46%            | -55.86% |     0.7  |       70 | 38.77%     | ok               |
|          20 | 72.38%   | 110.46%            | -52.47% |     0.7  |       84 | 56.74%     | ok               |

## INTU Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -2.08%   | -51.49%            | -42.82% |     0.08 |       69 | 28.29%     | ok               |
|          45 | -5.43%   | -51.49%            | -44.66% |     0.02 |       67 | 32.45%     | ok               |
|          40 | -11.04%  | -51.49%            | -48.32% |    -0.09 |       71 | 35.61%     | ok               |
|          15 | -12.87%  | -51.49%            | -47.30% |    -0.09 |       81 | 50.58%     | ok               |
|          25 | -12.88%  | -51.49%            | -42.24% |    -0.1  |       66 | 45.09%     | ok               |

## ITA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 4.44%    | 87.55%             | -21.48% |     0.21 |       72 | 35.94%     | ok               |
|          30 | 0.23%    | 87.55%             | -23.75% |     0.08 |       70 | 45.92%     | ok               |
|          35 | -2.35%   | 87.55%             | -23.16% |    -0    |       74 | 44.09%     | ok               |
|          15 | -4.51%   | 87.55%             | -28.17% |    -0.03 |       88 | 58.24%     | ok               |
|          40 | -3.48%   | 87.55%             | -20.58% |    -0.04 |       76 | 40.60%     | ok               |

## IWM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 8.72%    | 45.76%             | -12.83% |     0.36 |       50 | 37.10%     | ok               |
|          25 | 8.83%    | 45.76%             | -14.87% |     0.36 |       52 | 38.27%     | ok               |
|          40 | 6.51%    | 45.76%             | -14.38% |     0.31 |       44 | 32.45%     | ok               |
|          35 | 6.26%    | 45.76%             | -14.41% |     0.28 |       50 | 34.78%     | ok               |
|          15 | 4.90%    | 45.76%             | -17.63% |     0.22 |       73 | 43.09%     | ok               |

## JNJ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 15.67%   | 43.34%             | -10.70% |     0.69 |       62 | 37.60%     | ok               |
|          15 | 9.60%    | 43.34%             | -18.02% |     0.37 |       72 | 57.57%     | ok               |
|          45 | 7.00%    | 43.34%             | -13.80% |     0.33 |       64 | 42.76%     | ok               |
|          20 | 6.87%    | 43.34%             | -17.61% |     0.29 |       76 | 54.08%     | ok               |
|          40 | 4.66%    | 43.34%             | -14.77% |     0.23 |       70 | 46.92%     | ok               |

## JPM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 13.27%   | 84.78%             | -15.40% |     0.49 |       58 | 39.60%     | ok               |
|          45 | 3.49%    | 84.78%             | -21.44% |     0.17 |       58 | 42.76%     | ok               |
|          40 | -10.18%  | 84.78%             | -28.04% |    -0.24 |       70 | 45.26%     | ok               |
|          20 | -16.02%  | 84.78%             | -33.20% |    -0.29 |       88 | 57.24%     | ok               |
|          35 | -15.20%  | 84.78%             | -27.00% |    -0.38 |       76 | 48.92%     | ok               |

## KO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 23.27%   | 31.61%             | -8.07%  |     0.88 |       49 | 37.27%     | ok               |
|          35 | 19.49%   | 31.61%             | -8.07%  |     0.77 |       52 | 35.94%     | ok               |
|          50 | 16.35%   | 31.61%             | -11.40% |     0.74 |       34 | 26.62%     | ok               |
|          40 | 17.09%   | 31.61%             | -9.28%  |     0.73 |       54 | 32.95%     | ok               |
|          25 | 18.18%   | 31.61%             | -9.37%  |     0.7  |       55 | 39.93%     | ok               |

## LDO-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 7.19%    | -86.54%            | -45.67% |     0.37 |       88 | 52.30%     | ok               |
|          20 | 8.53%    | -86.54%            | -43.71% |     0.37 |       93 | 47.51%     | ok               |
|          30 | -2.37%   | -86.54%            | -58.32% |     0.26 |       80 | 38.12%     | ok               |
|          25 | -16.61%  | -86.54%            | -54.15% |     0.15 |       89 | 43.68%     | ok               |
|          35 | -21.05%  | -86.54%            | -63.16% |     0.03 |       82 | 30.84%     | ok               |

## LIN Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 2.30%    | 24.21%             | -23.70% |     0.14 |       69 | 50.25%     | ok               |
|          25 | 1.21%    | 24.21%             | -22.01% |     0.1  |       69 | 42.10%     | ok               |
|          20 | -0.96%   | 24.21%             | -23.00% |     0.03 |       68 | 45.26%     | ok               |
|          35 | -2.45%   | 24.21%             | -21.18% |    -0.04 |       68 | 32.78%     | ok               |
|          30 | -3.07%   | 24.21%             | -21.53% |    -0.05 |       72 | 39.27%     | ok               |

## LINK-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -17.74%  | -66.46%            | -55.61% |     0.05 |       72 | 41.19%     | ok               |
|          45 | -23.30%  | -66.46%            | -43.89% |    -0.09 |       50 | 25.67%     | ok               |
|          50 | -21.84%  | -66.46%            | -42.26% |    -0.1  |       40 | 20.88%     | ok               |
|          35 | -31.45%  | -66.46%            | -53.72% |    -0.15 |       62 | 35.82%     | ok               |
|          25 | -42.48%  | -66.46%            | -56.08% |    -0.24 |       70 | 46.93%     | ok               |

## LLY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 27.61%   | 75.98%             | -38.23% |     0.58 |       42 | 39.27%     | ok               |
|          45 | 15.38%   | 75.98%             | -42.66% |     0.38 |       50 | 42.43%     | ok               |
|          15 | 8.80%    | 75.98%             | -48.12% |     0.27 |       63 | 61.90%     | ok               |
|          40 | -1.89%   | 75.98%             | -46.23% |     0.09 |       62 | 44.93%     | ok               |
|          20 | -8.72%   | 75.98%             | -51.34% |    -0    |       72 | 56.91%     | ok               |

## LRCX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -4.23%   | 299.23%            | -60.45% |     0.13 |       83 | 55.57%     | ok               |
|          50 | -11.18%  | 299.23%            | -50.39% |    -0.02 |       78 | 36.94%     | ok               |
|          40 | -19.52%  | 299.23%            | -56.86% |    -0.13 |       72 | 42.60%     | ok               |
|          35 | -21.60%  | 299.23%            | -61.76% |    -0.15 |       82 | 45.09%     | ok               |
|          20 | -23.87%  | 299.23%            | -67.64% |    -0.17 |       89 | 51.08%     | ok               |

## LTC-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -18.68%  | -62.35%            | -47.33% |    -0.1  |       58 | 31.80%     | ok               |
|          35 | -24.16%  | -62.35%            | -56.94% |    -0.15 |       68 | 42.53%     | ok               |
|          30 | -35.44%  | -62.35%            | -55.90% |    -0.31 |       68 | 48.08%     | ok               |
|          40 | -32.90%  | -62.35%            | -58.13% |    -0.32 |       60 | 37.74%     | ok               |
|          25 | -38.16%  | -62.35%            | -56.67% |    -0.35 |       76 | 50.57%     | ok               |

## MCD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 3.24%    | -4.64%             | -9.22%  |     0.2  |       42 | 20.47%     | ok               |
|          30 | -3.06%   | -4.64%             | -19.14% |    -0.07 |       77 | 38.77%     | ok               |
|          25 | -4.09%   | -4.64%             | -20.80% |    -0.11 |       77 | 41.43%     | ok               |
|          40 | -6.27%   | -4.64%             | -16.86% |    -0.25 |       73 | 29.28%     | ok               |
|          35 | -8.16%   | -4.64%             | -15.80% |    -0.31 |       69 | 35.11%     | ok               |

## META Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 14.11%   | 58.35%             | -31.03% |     0.34 |       68 | 41.26%     | ok               |
|          40 | 1.57%    | 58.35%             | -35.11% |     0.15 |       68 | 44.26%     | ok               |
|          50 | -3.31%   | 58.35%             | -34.00% |     0.06 |       72 | 37.44%     | ok               |
|          25 | -8.46%   | 58.35%             | -39.84% |     0    |       69 | 54.91%     | ok               |
|          35 | -10.09%  | 58.35%             | -34.87% |    -0.04 |       79 | 49.08%     | ok               |

## MPC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 14.51%   | 66.40%             | -23.96% |     0.37 |       52 | 38.60%     | ok               |
|          45 | 7.25%    | 66.40%             | -25.09% |     0.24 |       58 | 42.26%     | ok               |
|          40 | 5.62%    | 66.40%             | -25.70% |     0.22 |       60 | 44.59%     | ok               |
|          35 | 2.36%    | 66.40%             | -35.90% |     0.16 |       68 | 47.09%     | ok               |
|          30 | -13.74%  | 66.40%             | -44.76% |    -0.14 |       71 | 49.92%     | ok               |

## MRK Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -11.43%  | 1.82%              | -29.91% |    -0.15 |       85 | 57.74%     | ok               |
|          25 | -11.00%  | 1.82%              | -31.07% |    -0.16 |       70 | 49.75%     | ok               |
|          20 | -15.36%  | 1.82%              | -29.38% |    -0.27 |       75 | 53.08%     | ok               |
|          30 | -21.30%  | 1.82%              | -32.14% |    -0.45 |       69 | 46.92%     | ok               |
|          35 | -21.08%  | 1.82%              | -30.82% |    -0.46 |       71 | 43.26%     | ok               |

## MS Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -6.24%   | 136.27%            | -19.61% |    -0.09 |       72 | 38.94%     | ok               |
|          35 | -12.82%  | 136.27%            | -23.35% |    -0.26 |       78 | 43.59%     | ok               |
|          15 | -17.11%  | 136.27%            | -26.54% |    -0.31 |       82 | 56.24%     | ok               |
|          20 | -17.21%  | 136.27%            | -25.68% |    -0.35 |       86 | 52.41%     | ok               |
|          50 | -12.70%  | 136.27%            | -15.66% |    -0.39 |       60 | 30.62%     | ok               |

## MSFT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -16.24%  | 7.26%              | -25.28% |    -0.45 |       60 | 35.27%     | ok               |
|          50 | -19.73%  | 7.26%              | -28.69% |    -0.59 |       58 | 30.95%     | ok               |
|          35 | -28.26%  | 7.26%              | -32.79% |    -0.75 |       69 | 43.59%     | ok               |
|          40 | -29.11%  | 7.26%              | -33.59% |    -0.81 |       65 | 38.60%     | ok               |
|          25 | -33.38%  | 7.26%              | -37.59% |    -0.86 |       82 | 51.25%     | ok               |

## MU Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 301.64%  | 948.68%            | -61.96% |     1.38 |       50 | 66.89%     | ok               |
|          25 | 225.82%  | 948.68%            | -67.90% |     1.26 |       51 | 60.40%     | ok               |
|          40 | 191.09%  | 948.68%            | -64.30% |     1.18 |       58 | 53.74%     | ok               |
|          20 | 198.30%  | 948.68%            | -67.25% |     1.16 |       57 | 62.56%     | ok               |
|          30 | 177.54%  | 948.68%            | -68.76% |     1.13 |       53 | 58.57%     | ok               |

## NEAR-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 83.93%   | -64.92%            | -48.95% |     0.88 |       46 | 23.95%     | ok               |
|          50 | 57.61%   | -64.92%            | -53.13% |     0.73 |       40 | 19.16%     | ok               |
|          40 | 45.71%   | -64.92%            | -57.15% |     0.62 |       50 | 28.35%     | ok               |
|          35 | 21.25%   | -64.92%            | -61.02% |     0.43 |       72 | 33.72%     | ok               |
|          15 | -2.57%   | -64.92%            | -54.94% |     0.28 |       92 | 58.05%     | ok               |

## NEM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 30.17%   | 164.90%            | -25.79% |     0.49 |       60 | 63.73%     | ok               |
|          20 | 16.24%   | 164.90%            | -30.47% |     0.36 |       70 | 59.23%     | ok               |
|          25 | -2.49%   | 164.90%            | -30.80% |     0.13 |       66 | 57.24%     | ok               |
|          30 | -19.45%  | 164.90%            | -38.49% |    -0.12 |       70 | 55.74%     | ok               |
|          35 | -19.14%  | 164.90%            | -39.55% |    -0.12 |       77 | 52.91%     | ok               |

## NFLX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 44.81%   | 66.98%             | -11.94% |     0.99 |       46 | 46.76%     | ok               |
|          50 | 35.59%   | 66.98%             | -16.28% |     0.88 |       46 | 39.10%     | ok               |
|          35 | 37.37%   | 66.98%             | -18.30% |     0.82 |       60 | 50.25%     | ok               |
|          45 | 32.16%   | 66.98%             | -15.48% |     0.78 |       50 | 42.93%     | ok               |
|          25 | 27.40%   | 66.98%             | -21.09% |     0.62 |       60 | 56.91%     | ok               |

## NKE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | -24.93%  | -59.09%            | -42.13% |    -0.33 |       77 | 38.44%     | ok               |
|          20 | -34.30%  | -59.09%            | -50.44% |    -0.43 |       97 | 54.24%     | ok               |
|          25 | -35.29%  | -59.09%            | -51.20% |    -0.46 |       95 | 50.25%     | ok               |
|          40 | -25.41%  | -59.09%            | -31.84% |    -0.47 |       69 | 30.45%     | ok               |
|          30 | -36.13%  | -59.09%            | -55.35% |    -0.49 |       93 | 44.93%     | ok               |

## NOW Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 31.64%   | -22.89%            | -26.36% |     0.52 |       77 | 51.91%     | ok               |
|          15 | 22.89%   | -22.89%            | -26.36% |     0.43 |       86 | 55.07%     | ok               |
|          25 | 21.53%   | -22.89%            | -25.74% |     0.42 |       72 | 49.42%     | ok               |
|          30 | 21.27%   | -22.89%            | -30.25% |     0.41 |       78 | 46.09%     | ok               |
|          35 | 18.35%   | -22.89%            | -29.30% |     0.39 |       77 | 41.10%     | ok               |

## NVDA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -7.53%   | 123.15%            | -33.22% |     0.07 |       68 | 52.58%     | ok               |
|          30 | -9.26%   | 123.15%            | -35.26% |     0.02 |       70 | 50.27%     | ok               |
|          20 | -13.66%  | 123.15%            | -40.59% |    -0.01 |       71 | 57.04%     | ok               |
|          50 | -16.79%  | 123.15%            | -40.84% |    -0.15 |       60 | 34.40%     | ok               |
|          35 | -19.89%  | 123.15%            | -41.25% |    -0.17 |       82 | 47.42%     | ok               |

## OP-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 68.18%   | -95.26%            | -45.76% |     0.82 |       38 | 17.24%     | ok               |
|          40 | 71.91%   | -95.26%            | -53.61% |     0.81 |       50 | 25.67%     | ok               |
|          50 | 52.94%   | -95.26%            | -36.11% |     0.74 |       34 | 12.45%     | ok               |
|          35 | 43.76%   | -95.26%            | -58.13% |     0.61 |       58 | 28.93%     | ok               |
|          30 | 13.40%   | -95.26%            | -70.11% |     0.37 |       74 | 35.63%     | ok               |

## ORCL Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 181.90%  | 100.45%            | -21.44% |     1.21 |       71 | 64.23%     | ok               |
|          20 | 107.84%  | 100.45%            | -22.81% |     0.92 |       74 | 59.90%     | ok               |
|          25 | 106.37%  | 100.45%            | -24.79% |     0.92 |       70 | 56.74%     | ok               |
|          35 | 61.75%   | 100.45%            | -31.95% |     0.69 |       64 | 48.59%     | ok               |
|          30 | 61.89%   | 100.45%            | -29.47% |     0.68 |       70 | 52.75%     | ok               |

## OXY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 4.11%    | -1.95%             | -29.70% |     0.19 |       65 | 44.59%     | ok               |
|          35 | 1.63%    | -1.95%             | -30.50% |     0.14 |       68 | 39.77%     | ok               |
|          50 | 0.80%    | -1.95%             | -31.07% |     0.12 |       38 | 29.12%     | ok               |
|          40 | -0.86%   | -1.95%             | -32.21% |     0.09 |       56 | 35.77%     | ok               |
|          25 | -10.30%  | -1.95%             | -39.43% |    -0.07 |       73 | 48.09%     | ok               |

## PEP Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 8.79%    | -15.16%            | -11.62% |     0.41 |       44 | 27.95%     | ok               |
|          45 | 1.40%    | -15.16%            | -14.22% |     0.11 |       68 | 32.78%     | ok               |
|          40 | -1.98%   | -15.16%            | -18.04% |    -0.02 |       78 | 38.27%     | ok               |
|          35 | -3.98%   | -15.16%            | -21.42% |    -0.06 |       87 | 43.09%     | ok               |
|          30 | -9.40%   | -15.16%            | -21.35% |    -0.22 |       85 | 49.42%     | ok               |

## PEPE-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 1.20%    | -87.13%            | -57.66% |     0.29 |       79 | 43.30%     | ok               |
|          35 | -5.59%   | -87.13%            | -51.35% |     0.2  |       64 | 38.12%     | ok               |
|          25 | -21.36%  | -87.13%            | -61.52% |     0.08 |       87 | 48.66%     | ok               |
|          15 | -36.37%  | -87.13%            | -69.84% |     0.02 |       83 | 58.24%     | ok               |
|          40 | -29.58%  | -87.13%            | -60.13% |    -0.13 |       60 | 33.33%     | ok               |

## PFE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -24.03%  | -9.27%             | -27.99% |    -0.84 |       52 | 21.30%     | ok               |
|          35 | -31.86%  | -9.27%             | -36.39% |    -1    |       82 | 33.61%     | ok               |
|          50 | -26.33%  | -9.27%             | -29.22% |    -1.03 |       44 | 17.47%     | ok               |
|          40 | -30.46%  | -9.27%             | -34.09% |    -1.04 |       76 | 26.12%     | ok               |
|          30 | -38.05%  | -9.27%             | -42.29% |    -1.18 |       77 | 37.27%     | ok               |

## PG Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -3.81%   | -2.70%             | -19.77% |    -0.12 |       54 | 34.11%     | ok               |
|          35 | -4.99%   | -2.70%             | -18.66% |    -0.16 |       60 | 37.77%     | ok               |
|          30 | -13.60%  | -2.70%             | -20.82% |    -0.5  |       63 | 40.93%     | ok               |
|          25 | -14.63%  | -2.70%             | -21.73% |    -0.54 |       73 | 42.10%     | ok               |
|          45 | -14.31%  | -2.70%             | -20.33% |    -0.64 |       54 | 31.28%     | ok               |

## PM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 1.44%    | 87.14%             | -32.20% |     0.12 |       84 | 53.08%     | ok               |
|          20 | 0.16%    | 87.14%             | -31.89% |     0.1  |       87 | 61.90%     | ok               |
|          30 | -0.11%   | 87.14%             | -33.68% |     0.09 |       81 | 56.91%     | ok               |
|          50 | -4.69%   | 87.14%             | -35.70% |    -0.03 |       76 | 43.26%     | ok               |
|          25 | -6.99%   | 87.14%             | -37.05% |    -0.06 |       81 | 59.23%     | ok               |

## POL-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 61.23%   | -84.79%            | -46.45% |     0.74 |       81 | 47.70%     | ok               |
|          25 | 48.70%   | -84.79%            | -46.72% |     0.64 |       74 | 56.70%     | ok               |
|          20 | 38.56%   | -84.79%            | -52.88% |     0.56 |       82 | 62.07%     | ok               |
|          50 | 12.05%   | -84.79%            | -22.86% |     0.33 |       48 | 20.88%     | ok               |
|          15 | 8.16%    | -84.79%            | -58.42% |     0.33 |       81 | 68.39%     | ok               |

## QCOM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | 1.16%    | 54.02%             | -55.66% |     0.19 |       75 | 50.75%     | ok               |
|          20 | -1.44%   | 54.02%             | -57.05% |     0.16 |       72 | 53.41%     | ok               |
|          35 | -5.33%   | 54.02%             | -51.84% |     0.1  |       87 | 45.92%     | ok               |
|          30 | -15.67%  | 54.02%             | -57.69% |    -0.04 |       81 | 48.59%     | ok               |
|          15 | -17.82%  | 54.02%             | -60.40% |    -0.05 |       76 | 56.57%     | ok               |

## QQQ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | 22.25%   | 72.15%             | -12.88% |     0.61 |       55 | 49.25%     | ok               |
|          20 | 21.73%   | 72.15%             | -12.98% |     0.58 |       63 | 51.75%     | ok               |
|          15 | 19.18%   | 72.15%             | -14.17% |     0.51 |       63 | 54.24%     | ok               |
|          30 | 17.24%   | 72.15%             | -12.88% |     0.51 |       60 | 46.26%     | ok               |
|          35 | 5.25%    | 72.15%             | -19.00% |     0.22 |       66 | 42.60%     | ok               |

## RENDER-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 51.64%   | -60.19%            | -43.43% |     0.67 |       82 | 55.18%     | ok               |
|          15 | 34.03%   | -60.19%            | -44.59% |     0.57 |       82 | 58.35%     | ok               |
|          25 | 21.59%   | -60.19%            | -40.60% |     0.48 |       86 | 51.16%     | ok               |
|          30 | -16.54%  | -60.19%            | -45.00% |     0.13 |       94 | 44.61%     | ok               |
|          40 | -25.92%  | -60.19%            | -38.60% |    -0.08 |       68 | 29.81%     | ok               |

## RTX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 25.01%   | 109.65%            | -18.66% |     0.63 |       76 | 56.41%     | ok               |
|          50 | 17.65%   | 109.65%            | -18.42% |     0.58 |       56 | 41.93%     | ok               |
|          25 | 20.35%   | 109.65%            | -18.59% |     0.54 |       64 | 53.08%     | ok               |
|          30 | 17.94%   | 109.65%            | -16.99% |     0.5  |       58 | 51.75%     | ok               |
|          35 | 15.38%   | 109.65%            | -18.00% |     0.49 |       54 | 49.75%     | ok               |

## SBUX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -17.00%  | 3.60%              | -23.81% |    -0.29 |       64 | 42.43%     | ok               |
|          45 | -17.27%  | 3.60%              | -27.26% |    -0.39 |       70 | 28.95%     | ok               |
|          40 | -20.56%  | 3.60%              | -27.45% |    -0.45 |       68 | 32.78%     | ok               |
|          50 | -20.31%  | 3.60%              | -26.80% |    -0.51 |       56 | 24.79%     | ok               |
|          30 | -25.64%  | 3.60%              | -31.46% |    -0.54 |       67 | 40.27%     | ok               |

## SCHW Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 2.81%    | 36.19%             | -15.92% |     0.15 |       52 | 33.11%     | ok               |
|          50 | -2.36%   | 36.19%             | -12.59% |    -0.02 |       48 | 30.78%     | ok               |
|          40 | -7.85%   | 36.19%             | -21.81% |    -0.15 |       60 | 36.11%     | ok               |
|          25 | -10.23%  | 36.19%             | -28.76% |    -0.16 |       61 | 47.75%     | ok               |
|          20 | -11.91%  | 36.19%             | -29.24% |    -0.2  |       69 | 50.42%     | ok               |

## SHIB-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -6.92%   | -80.84%            | -49.21% |     0.18 |       78 | 67.43%     | ok               |
|          25 | -14.00%  | -80.84%            | -43.85% |     0.08 |       77 | 58.81%     | ok               |
|          20 | -17.37%  | -80.84%            | -46.92% |     0.05 |       81 | 63.41%     | ok               |
|          35 | -17.03%  | -80.84%            | -53.32% |     0    |       66 | 45.98%     | ok               |
|          40 | -21.57%  | -80.84%            | -50.74% |    -0.08 |       56 | 38.31%     | ok               |

## SHY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd    |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:-------|---------:|---------:|:-----------|:-----------------|
|          30 | -2.49%   | -0.58%             | -2.85% |    -0.85 |       50 | 36.44%     | ok               |
|          35 | -2.60%   | -0.58%             | -3.27% |    -0.9  |       52 | 34.61%     | ok               |
|          40 | -2.72%   | -0.58%             | -3.33% |    -0.95 |       52 | 32.78%     | ok               |
|          45 | -2.70%   | -0.58%             | -3.23% |    -0.97 |       50 | 29.62%     | ok               |
|          50 | -2.87%   | -0.58%             | -3.40% |    -1.08 |       46 | 26.79%     | ok               |

## SKY-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -32.90%  | -0.85%             | -56.39% |    -0.37 |       58 | 50.00%     | ok               |
|          30 | -28.79%  | -0.85%             | -43.98% |    -0.38 |       68 | 39.66%     | ok               |
|          25 | -32.44%  | -0.85%             | -48.09% |    -0.44 |       63 | 43.51%     | ok               |
|          20 | -42.73%  | -0.85%             | -58.40% |    -0.64 |       60 | 47.36%     | ok               |
|          35 | -39.41%  | -0.85%             | -49.68% |    -0.74 |       60 | 33.41%     | ok               |

## SLB Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 11.39%   | 9.85%              | -23.07% |     0.33 |       48 | 36.44%     | ok               |
|          45 | 9.74%    | 9.85%              | -20.46% |     0.3  |       54 | 33.11%     | ok               |
|          35 | -16.58%  | 9.85%              | -41.81% |    -0.24 |       76 | 44.43%     | ok               |
|          50 | -15.17%  | 9.85%              | -30.87% |    -0.3  |       56 | 29.45%     | ok               |
|          30 | -29.65%  | 9.85%              | -54.13% |    -0.52 |       79 | 51.08%     | ok               |

## SLV Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 67.27%   | 190.56%            | -29.75% |     0.86 |       60 | 36.27%     | ok               |
|          45 | 62.01%   | 190.56%            | -31.82% |     0.82 |       54 | 34.44%     | ok               |
|          50 | 57.25%   | 190.56%            | -34.10% |     0.78 |       52 | 33.61%     | ok               |
|          35 | 54.63%   | 190.56%            | -36.89% |     0.75 |       62 | 38.60%     | ok               |
|          30 | 36.93%   | 190.56%            | -42.66% |     0.58 |       58 | 40.60%     | ok               |

## SMH Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 119.24%  | 229.40%            | -31.01% |     1.33 |       51 | 54.41%     | ok               |
|          35 | 98.59%   | 229.40%            | -34.36% |     1.23 |       56 | 50.08%     | ok               |
|          25 | 98.45%   | 229.40%            | -32.94% |     1.21 |       48 | 53.08%     | ok               |
|          30 | 96.11%   | 229.40%            | -33.99% |     1.2  |       50 | 51.41%     | ok               |
|          45 | 78.99%   | 229.40%            | -32.75% |     1.13 |       54 | 44.09%     | ok               |

## SNX-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 25.87%   | -88.77%            | -28.28% |     0.47 |       70 | 32.38%     | ok               |
|          30 | 5.80%    | -88.77%            | -32.91% |     0.31 |       67 | 40.23%     | ok               |
|          20 | 0.95%    | -88.77%            | -43.20% |     0.28 |       75 | 50.38%     | ok               |
|          25 | -15.62%  | -88.77%            | -36.73% |     0.1  |       80 | 44.64%     | ok               |
|          15 | -31.90%  | -88.77%            | -47.56% |    -0.04 |       85 | 54.41%     | ok               |

## SOL-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -11.12%  | -69.77%            | -54.19% |     0.12 |       66 | 39.08%     | ok               |
|          25 | -26.89%  | -69.77%            | -51.71% |    -0.02 |       74 | 56.90%     | ok               |
|          35 | -27.67%  | -69.77%            | -59.05% |    -0.05 |       74 | 46.55%     | ok               |
|          15 | -34.47%  | -69.77%            | -57.85% |    -0.1  |       80 | 64.18%     | ok               |
|          20 | -37.39%  | -69.77%            | -55.52% |    -0.15 |       70 | 59.39%     | ok               |

## SOXX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 102.52%  | 190.52%            | -38.67% |     1.18 |       55 | 53.08%     | ok               |
|          25 | 98.65%   | 190.52%            | -39.85% |     1.15 |       53 | 52.75%     | ok               |
|          35 | 90.39%   | 190.52%            | -38.63% |     1.11 |       61 | 47.92%     | ok               |
|          15 | 97.43%   | 190.52%            | -37.72% |     1.11 |       68 | 55.91%     | ok               |
|          30 | 87.48%   | 190.52%            | -40.34% |     1.07 |       57 | 50.58%     | ok               |

## SPY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 17.55%   | 54.73%             | -14.25% |     0.6  |       58 | 54.08%     | ok               |
|          15 | 16.79%   | 54.73%             | -16.80% |     0.57 |       63 | 56.91%     | ok               |
|          25 | 10.78%   | 54.73%             | -15.22% |     0.41 |       58 | 53.41%     | ok               |
|          30 | 6.78%    | 54.73%             | -16.47% |     0.29 |       60 | 50.92%     | ok               |
|          35 | 3.51%    | 54.73%             | -16.72% |     0.18 |       60 | 48.42%     | ok               |

## SUSHI-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -35.94%  | -90.43%            | -43.35% |    -0.4  |       54 | 15.13%     | ok               |
|          40 | -65.85%  | -90.43%            | -67.38% |    -0.87 |       63 | 24.90%     | ok               |
|          45 | -63.29%  | -90.43%            | -66.13% |    -0.88 |       56 | 18.01%     | ok               |
|          35 | -72.25%  | -90.43%            | -75.30% |    -0.99 |       78 | 30.27%     | ok               |
|          15 | -84.11%  | -90.43%            | -85.21% |    -1.15 |       92 | 48.08%     | ok               |

## T Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 54.62%   | 38.05%             | -18.13% |     1.12 |       59 | 54.08%     | ok               |
|          25 | 47.14%   | 38.05%             | -17.66% |     1.02 |       62 | 51.58%     | ok               |
|          15 | 46.18%   | 38.05%             | -15.08% |     0.97 |       68 | 57.90%     | ok               |
|          35 | 33.93%   | 38.05%             | -14.49% |     0.83 |       64 | 46.09%     | ok               |
|          30 | 32.46%   | 38.05%             | -17.01% |     0.78 |       64 | 49.42%     | ok               |

## TGT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -9.69%   | -13.02%            | -41.89% |    -0.08 |       81 | 46.42%     | ok               |
|          25 | -10.59%  | -13.02%            | -42.39% |    -0.12 |       63 | 41.43%     | ok               |
|          15 | -12.65%  | -13.02%            | -39.76% |    -0.13 |       71 | 50.92%     | ok               |
|          45 | -9.84%   | -13.02%            | -29.07% |    -0.15 |       52 | 29.12%     | ok               |
|          30 | -11.46%  | -13.02%            | -40.57% |    -0.16 |       58 | 38.77%     | ok               |

## TIA-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 42.22%   | -94.29%            | -40.13% |     0.59 |       58 | 27.97%     | ok               |
|          40 | 35.94%   | -94.29%            | -39.80% |     0.55 |       58 | 23.95%     | ok               |
|          45 | 26.15%   | -94.29%            | -39.18% |     0.48 |       48 | 17.62%     | ok               |
|          50 | 22.56%   | -94.29%            | -40.62% |     0.48 |       30 | 10.73%     | ok               |
|          30 | -7.22%   | -94.29%            | -55.60% |     0.18 |       80 | 32.57%     | ok               |

## TLT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -22.24%  | -11.87%            | -24.21% |    -1.6  |       74 | 33.61%     | ok               |
|          40 | -21.31%  | -11.87%            | -23.31% |    -1.86 |       60 | 22.63%     | ok               |
|          35 | -23.44%  | -11.87%            | -25.38% |    -1.9  |       68 | 27.62%     | ok               |
|          50 | -17.12%  | -11.87%            | -18.99% |    -1.91 |       36 | 14.98%     | ok               |
|          15 | -28.65%  | -11.87%            | -30.94% |    -1.91 |       79 | 41.60%     | ok               |

## TMO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 48.48%   | -13.14%            | -12.29% |     1.03 |       44 | 35.27%     | ok               |
|          50 | 43.47%   | -13.14%            | -10.55% |     0.99 |       36 | 30.12%     | ok               |
|          40 | 46.29%   | -13.14%            | -12.07% |     0.97 |       47 | 39.77%     | ok               |
|          35 | 32.57%   | -13.14%            | -16.12% |     0.72 |       61 | 44.59%     | ok               |
|          30 | 22.17%   | -13.14%            | -16.83% |     0.53 |       59 | 49.42%     | ok               |

## TMUS Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 21.00%   | 9.57%              | -26.87% |     0.5  |       69 | 60.23%     | ok               |
|          30 | 19.54%   | 9.57%              | -24.50% |     0.49 |       70 | 48.59%     | ok               |
|          20 | 13.57%   | 9.57%              | -24.82% |     0.37 |       71 | 54.58%     | ok               |
|          25 | 12.44%   | 9.57%              | -25.91% |     0.35 |       75 | 50.92%     | ok               |
|          50 | 8.60%    | 9.57%              | -19.36% |     0.3  |       60 | 36.44%     | ok               |

## TRX-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -4.46%   | 20.85%             | -22.90% |    -0.02 |       70 | 49.04%     | ok               |
|          25 | -6.17%   | 20.85%             | -26.84% |    -0.06 |       66 | 52.30%     | ok               |
|          35 | -5.76%   | 20.85%             | -21.77% |    -0.06 |       66 | 46.36%     | ok               |
|          40 | -5.58%   | 20.85%             | -22.12% |    -0.07 |       52 | 38.31%     | ok               |
|          50 | -6.77%   | 20.85%             | -20.97% |    -0.13 |       46 | 33.14%     | ok               |

## TSLA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 86.08%   | 78.63%             | -32.60% |     0.93 |       64 | 31.61%     | ok               |
|          40 | 76.71%   | 78.63%             | -45.90% |     0.81 |       61 | 36.11%     | ok               |
|          45 | 49.70%   | 78.63%             | -46.86% |     0.64 |       65 | 33.44%     | ok               |
|          35 | 28.16%   | 78.63%             | -54.51% |     0.46 |       76 | 39.27%     | ok               |
|          30 | 8.00%    | 78.63%             | -57.89% |     0.29 |       68 | 44.09%     | ok               |

## TXN Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 13.18%   | 72.90%             | -45.45% |     0.33 |       70 | 35.11%     | ok               |
|          20 | 3.19%    | 72.90%             | -38.98% |     0.2  |       63 | 60.73%     | ok               |
|          15 | 1.31%    | 72.90%             | -39.48% |     0.17 |       66 | 64.23%     | ok               |
|          35 | 0.01%    | 72.90%             | -43.38% |     0.14 |       74 | 50.75%     | ok               |
|          40 | -0.11%   | 72.90%             | -45.67% |     0.13 |       74 | 48.09%     | ok               |

## UNH Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 24.83%   | -23.40%            | -36.71% |     0.48 |       52 | 28.79%     | ok               |
|          30 | 13.76%   | -23.40%            | -32.85% |     0.33 |       80 | 51.91%     | ok               |
|          15 | 12.89%   | -23.40%            | -34.13% |     0.32 |       80 | 66.39%     | ok               |
|          35 | 10.67%   | -23.40%            | -34.10% |     0.29 |       72 | 46.76%     | ok               |
|          40 | 8.73%    | -23.40%            | -38.11% |     0.27 |       64 | 40.93%     | ok               |

## UNI-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -3.75%   | -83.19%            | -53.40% |     0.18 |       52 | 24.33%     | ok               |
|          40 | -12.59%  | -83.19%            | -60.60% |     0.1  |       54 | 29.50%     | ok               |
|          50 | -10.25%  | -83.19%            | -50.59% |     0.09 |       48 | 20.69%     | ok               |
|          35 | -25.18%  | -83.19%            | -65.85% |    -0.02 |       72 | 34.29%     | ok               |
|          20 | -71.26%  | -83.19%            | -80.81% |    -0.71 |      101 | 51.15%     | ok               |

## UPS Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -33.92%  | -31.44%            | -42.28% |    -0.65 |       74 | 43.09%     | ok               |
|          35 | -32.78%  | -31.44%            | -40.47% |    -0.66 |       59 | 32.95%     | ok               |
|          20 | -35.03%  | -31.44%            | -45.80% |    -0.67 |       80 | 46.26%     | ok               |
|          30 | -35.25%  | -31.44%            | -40.62% |    -0.71 |       66 | 38.60%     | ok               |
|          40 | -34.12%  | -31.44%            | -42.12% |    -0.72 |       51 | 27.79%     | ok               |

## USO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 8.31%    | 95.56%             | -35.12% |     0.26 |       50 | 26.79%     | ok               |
|          30 | 2.80%    | 95.56%             | -43.35% |     0.17 |       68 | 34.44%     | ok               |
|          25 | -1.00%   | 95.56%             | -44.86% |     0.11 |       71 | 37.60%     | ok               |
|          20 | -1.10%   | 95.56%             | -44.92% |     0.11 |       75 | 39.77%     | ok               |
|          40 | -1.01%   | 95.56%             | -41.14% |     0.11 |       61 | 29.62%     | ok               |

## VEA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 5.44%    | 45.41%             | -16.28% |     0.25 |       60 | 50.58%     | ok               |
|          20 | 1.19%    | 45.41%             | -17.70% |     0.1  |       61 | 47.92%     | ok               |
|          25 | -2.41%   | 45.41%             | -19.11% |    -0.04 |       59 | 45.92%     | ok               |
|          30 | -2.87%   | 45.41%             | -19.49% |    -0.07 |       60 | 43.43%     | ok               |
|          35 | -3.95%   | 45.41%             | -18.37% |    -0.12 |       58 | 42.43%     | ok               |

## VIXY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -46.17%  | -58.96%            | -68.69% |    -0.39 |       44 | 10.32%     | ok               |
|          45 | -56.11%  | -58.96%            | -74.13% |    -0.55 |       56 | 16.31%     | ok               |
|          40 | -65.15%  | -58.96%            | -80.10% |    -0.68 |       70 | 20.30%     | ok               |
|          35 | -68.80%  | -58.96%            | -83.87% |    -0.71 |       86 | 25.46%     | ok               |
|          15 | -78.21%  | -58.96%            | -89.47% |    -0.82 |       99 | 42.76%     | ok               |

## VNQ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -8.60%   | 11.16%             | -19.07% |    -0.37 |       60 | 28.62%     | ok               |
|          50 | -9.03%   | 11.16%             | -17.13% |    -0.41 |       56 | 26.12%     | ok               |
|          25 | -13.12%  | 11.16%             | -22.34% |    -0.51 |       69 | 40.77%     | ok               |
|          40 | -14.13%  | 11.16%             | -24.84% |    -0.62 |       74 | 32.11%     | ok               |
|          20 | -17.31%  | 11.16%             | -23.79% |    -0.68 |       78 | 44.09%     | ok               |

## VTI Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 16.10%   | 53.25%             | -13.96% |     0.56 |       62 | 55.91%     | ok               |
|          15 | 11.13%   | 53.25%             | -15.70% |     0.4  |       65 | 58.57%     | ok               |
|          25 | 5.18%    | 53.25%             | -16.10% |     0.23 |       60 | 54.24%     | ok               |
|          30 | -2.17%   | 53.25%             | -18.77% |    -0.02 |       70 | 52.25%     | ok               |
|          40 | -3.82%   | 53.25%             | -20.73% |    -0.09 |       72 | 45.42%     | ok               |

## VWO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -9.03%   | 43.60%             | -24.01% |    -0.26 |       69 | 49.42%     | ok               |
|          50 | -7.89%   | 43.60%             | -21.68% |    -0.28 |       60 | 32.45%     | ok               |
|          20 | -10.06%  | 43.60%             | -26.14% |    -0.31 |       67 | 47.25%     | ok               |
|          40 | -8.98%   | 43.60%             | -23.57% |    -0.31 |       70 | 37.94%     | ok               |
|          45 | -9.69%   | 43.60%             | -23.75% |    -0.35 |       62 | 34.94%     | ok               |

## VZ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 3.10%    | 17.66%             | -16.98% |     0.16 |       50 | 26.96%     | ok               |
|          45 | -4.02%   | 17.66%             | -20.38% |    -0.07 |       56 | 29.78%     | ok               |
|          35 | -9.70%   | 17.66%             | -24.68% |    -0.24 |       59 | 35.27%     | ok               |
|          25 | -13.07%  | 17.66%             | -28.84% |    -0.32 |       76 | 43.09%     | ok               |
|          40 | -12.82%  | 17.66%             | -26.72% |    -0.36 |       62 | 32.28%     | ok               |

## WFC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -1.92%   | 72.87%             | -18.29% |     0    |       56 | 31.78%     | ok               |
|          35 | -5.68%   | 72.87%             | -23.06% |    -0.05 |       79 | 43.59%     | ok               |
|          45 | -8.42%   | 72.87%             | -23.40% |    -0.18 |       62 | 36.11%     | ok               |
|          20 | -16.53%  | 72.87%             | -28.83% |    -0.23 |       81 | 52.75%     | ok               |
|          40 | -11.07%  | 72.87%             | -24.26% |    -0.26 |       74 | 39.60%     | ok               |

## WIF-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 80.47%   | -92.76%            | -40.67% |     0.75 |       67 | 39.08%     | ok               |
|          15 | 77.38%   | -92.76%            | -46.21% |     0.74 |       75 | 41.95%     | ok               |
|          25 | 10.27%   | -92.76%            | -45.19% |     0.38 |       73 | 36.21%     | ok               |
|          30 | -31.20%  | -92.76%            | -50.40% |    -0.05 |       72 | 31.61%     | ok               |
|          50 | -15.94%  | -92.76%            | -37.87% |    -0.08 |       36 | 11.49%     | ok               |

## WMT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 64.78%   | 121.08%            | -9.18%  |     1.63 |       36 | 45.59%     | ok               |
|          50 | 51.46%   | 121.08%            | -12.19% |     1.45 |       32 | 42.93%     | ok               |
|          40 | 54.48%   | 121.08%            | -9.18%  |     1.4  |       40 | 46.76%     | ok               |
|          35 | 55.75%   | 121.08%            | -9.11%  |     1.39 |       48 | 50.42%     | ok               |
|          30 | 33.20%   | 121.08%            | -21.31% |     0.87 |       55 | 52.91%     | ok               |

## XBI Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 3.96%    | 42.30%             | -16.71% |     0.18 |       60 | 34.61%     | ok               |
|          45 | 3.16%    | 42.30%             | -16.88% |     0.16 |       52 | 31.45%     | ok               |
|          35 | -4.57%   | 42.30%             | -21.38% |    -0.03 |       64 | 37.94%     | ok               |
|          50 | -5.14%   | 42.30%             | -16.83% |    -0.07 |       54 | 28.29%     | ok               |
|          30 | -6.39%   | 42.30%             | -21.75% |    -0.07 |       64 | 39.77%     | ok               |

## XLB Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -4.75%   | 21.34%             | -20.68% |    -0.13 |       58 | 32.28%     | ok               |
|          50 | -4.81%   | 21.34%             | -17.59% |    -0.15 |       46 | 27.95%     | ok               |
|          35 | -7.88%   | 21.34%             | -23.62% |    -0.24 |       60 | 35.61%     | ok               |
|          45 | -7.62%   | 21.34%             | -20.79% |    -0.26 |       46 | 29.45%     | ok               |
|          25 | -11.27%  | 21.34%             | -23.87% |    -0.36 |       68 | 41.10%     | ok               |

## XLC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 19.04%   | 51.29%             | -12.33% |     0.63 |       63 | 56.41%     | ok               |
|          25 | 16.80%   | 51.29%             | -12.31% |     0.57 |       60 | 58.24%     | ok               |
|          40 | 13.09%   | 51.29%             | -13.38% |     0.5  |       66 | 49.08%     | ok               |
|          35 | 13.06%   | 51.29%             | -13.38% |     0.49 |       62 | 53.58%     | ok               |
|          20 | 8.58%    | 51.29%             | -13.37% |     0.32 |       68 | 60.90%     | ok               |

## XLE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 1.60%    | 39.50%             | -25.98% |     0.12 |       56 | 36.61%     | ok               |
|          45 | -5.42%   | 39.50%             | -31.11% |    -0.08 |       64 | 39.10%     | ok               |
|          35 | -6.81%   | 39.50%             | -33.61% |    -0.1  |       71 | 44.43%     | ok               |
|          25 | -10.28%  | 39.50%             | -37.56% |    -0.17 |       85 | 49.92%     | ok               |
|          30 | -10.75%  | 39.50%             | -37.89% |    -0.2  |       77 | 46.76%     | ok               |

## XLF Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -2.83%   | 39.10%             | -18.01% |    -0.03 |       68 | 55.41%     | ok               |
|          15 | -6.85%   | 39.10%             | -19.58% |    -0.17 |       76 | 58.24%     | ok               |
|          25 | -10.98%  | 39.10%             | -23.22% |    -0.34 |       77 | 51.75%     | ok               |
|          30 | -11.61%  | 39.10%             | -23.61% |    -0.38 |       76 | 49.25%     | ok               |
|          35 | -18.71%  | 39.10%             | -27.41% |    -0.74 |       66 | 45.09%     | ok               |

## XLI Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 13.11%   | 55.37%             | -10.36% |     0.49 |       72 | 54.91%     | ok               |
|          20 | 7.91%    | 55.37%             | -12.74% |     0.34 |       65 | 50.42%     | ok               |
|          45 | 5.38%    | 55.37%             | -12.27% |     0.28 |       62 | 38.77%     | ok               |
|          30 | 5.55%    | 55.37%             | -11.38% |     0.27 |       66 | 47.92%     | ok               |
|          50 | 4.34%    | 55.37%             | -9.25%  |     0.24 |       56 | 36.44%     | ok               |

## XLK Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 87.63%   | 87.58%             | -14.75% |     1.4  |       41 | 54.08%     | ok               |
|          20 | 79.50%   | 87.58%             | -14.75% |     1.33 |       46 | 52.08%     | ok               |
|          25 | 71.82%   | 87.58%             | -14.75% |     1.28 |       40 | 50.08%     | ok               |
|          30 | 69.57%   | 87.58%             | -14.75% |     1.27 |       40 | 48.92%     | ok               |
|          35 | 50.84%   | 87.58%             | -13.61% |     1.04 |       52 | 46.26%     | ok               |

## XLM-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 31.61%   | -54.61%            | -37.64% |     0.52 |       50 | 33.14%     | ok               |
|          50 | 27.93%   | -54.61%            | -32.06% |     0.49 |       46 | 29.31%     | ok               |
|          30 | 6.29%    | -54.61%            | -45.54% |     0.3  |       69 | 47.13%     | ok               |
|          15 | 0.54%    | -54.61%            | -39.98% |     0.26 |       85 | 59.20%     | ok               |
|          20 | 0.87%    | -54.61%            | -43.12% |     0.25 |       75 | 52.49%     | ok               |

## XLP Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 10.10%   | 14.62%             | -5.66%  |     0.63 |       58 | 34.11%     | ok               |
|          40 | 8.95%    | 14.62%             | -7.77%  |     0.54 |       72 | 38.77%     | ok               |
|          35 | 8.00%    | 14.62%             | -9.73%  |     0.48 |       68 | 41.76%     | ok               |
|          50 | 6.29%    | 14.62%             | -6.08%  |     0.42 |       60 | 31.95%     | ok               |
|          30 | 5.75%    | 14.62%             | -10.28% |     0.35 |       72 | 43.59%     | ok               |

## XLU Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 5.66%    | 40.08%             | -9.11%  |     0.31 |       50 | 30.95%     | ok               |
|          45 | 4.69%    | 40.08%             | -9.53%  |     0.27 |       52 | 31.78%     | ok               |
|          40 | 1.51%    | 40.08%             | -10.77% |     0.12 |       58 | 33.11%     | ok               |
|          35 | -5.22%   | 40.08%             | -15.13% |    -0.2  |       64 | 35.77%     | ok               |
|          30 | -6.98%   | 40.08%             | -16.16% |    -0.28 |       69 | 38.94%     | ok               |

## XLV Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -9.06%   | 8.89%              | -14.23% |    -0.43 |       66 | 37.10%     | ok               |
|          25 | -11.77%  | 8.89%              | -16.79% |    -0.57 |       70 | 38.94%     | ok               |
|          45 | -11.87%  | 8.89%              | -16.50% |    -0.69 |       56 | 27.12%     | ok               |
|          35 | -13.93%  | 8.89%              | -18.49% |    -0.74 |       66 | 34.28%     | ok               |
|          20 | -15.70%  | 8.89%              | -20.35% |    -0.77 |       75 | 40.60%     | ok               |

## XLY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 4.50%    | 32.05%             | -12.94% |     0.21 |       74 | 41.43%     | ok               |
|          50 | 1.30%    | 32.05%             | -11.79% |     0.1  |       50 | 29.62%     | ok               |
|          30 | 0.25%    | 32.05%             | -14.01% |     0.07 |       76 | 44.76%     | ok               |
|          15 | -1.35%   | 32.05%             | -15.77% |     0.04 |       80 | 52.25%     | ok               |
|          40 | -1.91%   | 32.05%             | -16.99% |    -0.01 |       68 | 37.10%     | ok               |

## XOM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 4.68%    | 50.00%             | -21.35% |     0.21 |       40 | 29.28%     | ok               |
|          40 | 2.28%    | 50.00%             | -21.45% |     0.14 |       48 | 32.95%     | ok               |
|          25 | 1.09%    | 50.00%             | -19.90% |     0.11 |       61 | 37.77%     | ok               |
|          30 | 0.51%    | 50.00%             | -20.29% |     0.09 |       61 | 36.44%     | ok               |
|          35 | -0.19%   | 50.00%             | -20.93% |     0.07 |       60 | 34.94%     | ok               |

## XRP-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | -35.40%  | -53.20%            | -55.24% |    -0.3  |       74 | 41.76%     | ok               |
|          40 | -40.91%  | -53.20%            | -53.73% |    -0.45 |       64 | 35.82%     | ok               |
|          30 | -47.52%  | -53.20%            | -63.01% |    -0.52 |       78 | 46.17%     | ok               |
|          45 | -48.40%  | -53.20%            | -55.40% |    -0.63 |       64 | 31.61%     | ok               |
|          50 | -46.17%  | -53.20%            | -46.65% |    -0.7  |       66 | 23.95%     | ok               |

## YFI-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -37.38%  | -78.85%            | -52.37% |    -0.56 |       64 | 26.44%     | ok               |
|          45 | -43.80%  | -78.85%            | -54.04% |    -0.81 |       62 | 22.03%     | ok               |
|          30 | -54.61%  | -78.85%            | -67.78% |    -0.81 |       85 | 40.04%     | ok               |
|          50 | -44.08%  | -78.85%            | -51.80% |    -0.9  |       52 | 17.62%     | ok               |
|          35 | -55.44%  | -78.85%            | -65.91% |    -0.9  |       77 | 33.91%     | ok               |

## ZEC-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 124.17%  | 600.84%            | -24.66% |     0.9  |       50 | 23.18%     | ok               |
|          35 | 84.16%   | 600.84%            | -43.54% |     0.73 |       60 | 31.03%     | ok               |
|          25 | 71.15%   | 600.84%            | -46.61% |     0.68 |       61 | 39.85%     | ok               |
|          50 | 54.10%   | 600.84%            | -37.94% |     0.6  |       52 | 20.69%     | ok               |
|          30 | 41.84%   | 600.84%            | -46.93% |     0.55 |       69 | 36.59%     | ok               |
