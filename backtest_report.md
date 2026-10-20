# Market Tracker Backtest Report

_Generated: 2026-10-20T04:55:57+00:00_

## Data Sources

- Crypto: Kraken -> Coinbase -> CoinGecko OHLC -> CoinPaprika fallback chain.
- Stocks / ETFs / indices: Stooq -> Yahoo Finance fallback chain.
- Data rows are generated from real market APIs. Mock OHLCV rows are not generated.

## Data Freshness

- Rows: **92,748**
- Symbols: **161**
- Date range: **2024-05-28** to **2026-10-20**

## Latest Signals

| symbol     | date                |         close |   composite_score | signal   | data_source   |
|:-----------|:--------------------|--------------:|------------------:|:---------|:--------------|
| ABBV       | 2026-10-19 00:00:00 |   282.68      |         67.75     | LONG     | Yahoo Finance |
| AMGN       | 2026-10-19 00:00:00 |   424.94      |         64.9167   | LONG     | Yahoo Finance |
| CL         | 2026-10-19 00:00:00 |    93.39      |         61.75     | LONG     | Yahoo Finance |
| COP        | 2026-10-19 00:00:00 |   145.24      |         70.75     | LONG     | Yahoo Finance |
| COST       | 2026-10-19 00:00:00 |   995.53      |         68        | LONG     | Yahoo Finance |
| CRM        | 2026-10-19 00:00:00 |   242.45      |         72.0833   | LONG     | Yahoo Finance |
| CVX        | 2026-10-19 00:00:00 |   224.37      |         54.75     | LONG     | Yahoo Finance |
| DIS        | 2026-10-19 00:00:00 |   109.59      |         74.0833   | LONG     | Yahoo Finance |
| DXY-INDEX  | 2026-10-20 00:00:00 |   101.797     |         59.4086   | LONG     | Yahoo Finance |
| EOG        | 2026-10-19 00:00:00 |   157.65      |         70.75     | LONG     | Yahoo Finance |
| IBM        | 2026-10-19 00:00:00 |   236.39      |         35.25     | LONG     | Yahoo Finance |
| INTU       | 2026-10-19 00:00:00 |   325.62      |         39.75     | LONG     | Yahoo Finance |
| KO         | 2026-10-19 00:00:00 |    93.42      |         70.75     | LONG     | Yahoo Finance |
| LIN        | 2026-10-19 00:00:00 |   503.44      |         68        | LONG     | Yahoo Finance |
| LLY        | 2026-10-19 00:00:00 |  1240.34      |         66.5833   | LONG     | Yahoo Finance |
| MPC        | 2026-10-19 00:00:00 |   473.69      |         71.25     | LONG     | Yahoo Finance |
| MSFT       | 2026-10-19 00:00:00 |   533.52      |         59.0833   | LONG     | Yahoo Finance |
| NEM        | 2026-10-19 00:00:00 |   118.01      |         41.9167   | LONG     | Yahoo Finance |
| OXY        | 2026-10-19 00:00:00 |    62.72      |         52.75     | LONG     | Yahoo Finance |
| PG         | 2026-10-19 00:00:00 |   157.69      |         74.75     | LONG     | Yahoo Finance |
| PM         | 2026-10-19 00:00:00 |   201.05      |         71.0833   | LONG     | Yahoo Finance |
| RTX        | 2026-10-19 00:00:00 |   192.11      |         36.9167   | LONG     | Yahoo Finance |
| TMO        | 2026-10-19 00:00:00 |   679.38      |         49.25     | LONG     | Yahoo Finance |
| UNH        | 2026-10-19 00:00:00 |   406.88      |         78.5833   | LONG     | Yahoo Finance |
| WMT        | 2026-10-19 00:00:00 |   118.7       |         63.5      | LONG     | Yahoo Finance |
| XLB        | 2026-10-19 00:00:00 |    50.95      |         49.8333   | LONG     | Yahoo Finance |
| XLE        | 2026-10-19 00:00:00 |    67.8       |         52.75     | LONG     | Yahoo Finance |
| XLF        | 2026-10-19 00:00:00 |    55.06      |         50.9167   | LONG     | Yahoo Finance |
| XLP        | 2026-10-19 00:00:00 |    87.21      |         52.25     | LONG     | Yahoo Finance |
| XOM        | 2026-10-19 00:00:00 |   178.28      |         54.75     | LONG     | Yahoo Finance |
| AAPL       | 2026-10-19 00:00:00 |   342.94      |         59.5      | NEUTRAL  | Yahoo Finance |
| AAVE-USD   | 2026-10-20 00:00:00 |   151.22      |          0.333333 | NEUTRAL  | Kraken API    |
| ADA-USD    | 2026-10-20 00:00:00 |     0.218321  |        -60.8333   | NEUTRAL  | Kraken API    |
| ADBE       | 2026-10-19 00:00:00 |   247.09      |         12.9167   | NEUTRAL  | Yahoo Finance |
| AGG        | 2026-10-19 00:00:00 |    95.11      |         -1.58333  | NEUTRAL  | Yahoo Finance |
| ALGO-USD   | 2026-10-20 00:00:00 |     0.11189   |         16.9167   | NEUTRAL  | Kraken API    |
| AMD        | 2026-10-19 00:00:00 |   538.05      |          0.416667 | NEUTRAL  | Yahoo Finance |
| AMZN       | 2026-10-19 00:00:00 |   262.45      |         66.8333   | NEUTRAL  | Yahoo Finance |
| APT-USD    | 2026-10-20 00:00:00 |     0.7699    |        -24.1667   | NEUTRAL  | Kraken API    |
| ARB-USD    | 2026-10-20 00:00:00 |     0.1997    |         29.8333   | NEUTRAL  | Kraken API    |
| ARKK       | 2026-10-19 00:00:00 |    82.31      |        -24.75     | NEUTRAL  | Yahoo Finance |
| ATOM-USD   | 2026-10-20 00:00:00 |     1.7644    |        -29.25     | NEUTRAL  | Kraken API    |
| AVAX-USD   | 2026-10-20 00:00:00 |     9.605     |         -8.58333  | NEUTRAL  | Kraken API    |
| AVGO       | 2026-10-19 00:00:00 |   334.59      |        -67        | NEUTRAL  | Yahoo Finance |
| BA         | 2026-10-19 00:00:00 |   191.42      |        -13.5833   | NEUTRAL  | Yahoo Finance |
| BCH-USD    | 2026-10-20 00:00:00 |   279.07      |        -10.5833   | NEUTRAL  | Kraken API    |
| BITO       | 2026-10-19 00:00:00 |    10.92      |         -6.91667  | NEUTRAL  | Yahoo Finance |
| BLK        | 2026-10-19 00:00:00 |  1124.6       |         60.8333   | NEUTRAL  | Yahoo Finance |
| BND        | 2026-10-19 00:00:00 |    70.6       |          5.91667  | NEUTRAL  | Yahoo Finance |
| BTC-USD    | 2026-10-20 00:00:00 | 82048.3       |        -10.5833   | NEUTRAL  | Kraken API    |
| CMCSA      | 2026-10-19 00:00:00 |    21.9       |        -23.0833   | NEUTRAL  | Yahoo Finance |
| COMP-USD   | 2026-10-20 00:00:00 |    21.13      |        -19.3333   | NEUTRAL  | Kraken API    |
| CRV-USD    | 2026-10-20 00:00:00 |     0.37359   |         36.9167   | NEUTRAL  | Kraken API    |
| CSCO       | 2026-10-19 00:00:00 |   106.5       |         17        | NEUTRAL  | Yahoo Finance |
| DASH-USD   | 2026-10-20 00:00:00 |    50.299     |        -15.5833   | NEUTRAL  | Kraken API    |
| DBC        | 2026-10-19 00:00:00 |    33.68      |         59.75     | NEUTRAL  | Yahoo Finance |
| DE         | 2026-10-19 00:00:00 |   627         |        -12.3333   | NEUTRAL  | Yahoo Finance |
| DIA        | 2026-10-19 00:00:00 |   518.92      |         40.1667   | NEUTRAL  | Yahoo Finance |
| DOT-USD    | 2026-10-20 00:00:00 |     1.1521    |        -34.9167   | NEUTRAL  | Kraken API    |
| EEM        | 2026-10-19 00:00:00 |    63.31      |        -27.5      | NEUTRAL  | Yahoo Finance |
| EFA        | 2026-10-19 00:00:00 |   102.87      |         -7.75     | NEUTRAL  | Yahoo Finance |
| ETH-USD    | 2026-10-20 00:00:00 |  2409.6       |        -24.6667   | NEUTRAL  | Kraken API    |
| EWJ        | 2026-10-19 00:00:00 |    94.99      |        -24.8333   | NEUTRAL  | Yahoo Finance |
| FCX        | 2026-10-19 00:00:00 |    69.75      |        -41.5      | NEUTRAL  | Yahoo Finance |
| FET-USD    | 2026-10-20 00:00:00 |     0.1922    |        -50.5      | NEUTRAL  | Kraken API    |
| FIL-USD    | 2026-10-20 00:00:00 |     1.023     |         -2.58333  | NEUTRAL  | Kraken API    |
| FXI        | 2026-10-19 00:00:00 |    33.53      |        -35.1667   | NEUTRAL  | Yahoo Finance |
| GDX        | 2026-10-19 00:00:00 |    86.47      |        -17.5      | NEUTRAL  | Yahoo Finance |
| GE         | 2026-10-19 00:00:00 |   311.28      |        -49.5      | NEUTRAL  | Yahoo Finance |
| GLD        | 2026-10-19 00:00:00 |   379.69      |        -25.9167   | NEUTRAL  | Yahoo Finance |
| GOOGL      | 2026-10-19 00:00:00 |   344.18      |         -0.25     | NEUTRAL  | Yahoo Finance |
| HD         | 2026-10-19 00:00:00 |   309.88      |         17.0833   | NEUTRAL  | Yahoo Finance |
| HON        | 2026-10-19 00:00:00 |   209.98      |        -27.25     | NEUTRAL  | Yahoo Finance |
| IBIT       | 2026-10-19 00:00:00 |    46.3       |         20.0833   | NEUTRAL  | Yahoo Finance |
| ICP-USD    | 2026-10-20 00:00:00 |     2.866     |        -34.5      | NEUTRAL  | Kraken API    |
| IEF        | 2026-10-19 00:00:00 |    90.08      |          5.91667  | NEUTRAL  | Yahoo Finance |
| IEMG       | 2026-10-19 00:00:00 |    77.34      |        -27.5      | NEUTRAL  | Yahoo Finance |
| INJ-USD    | 2026-10-20 00:00:00 |     8.623     |         55.9167   | NEUTRAL  | Kraken API    |
| INTC       | 2026-10-19 00:00:00 |    92.03      |         -9.83333  | NEUTRAL  | Yahoo Finance |
| JNJ        | 2026-10-19 00:00:00 |   253.79      |        -41.5833   | NEUTRAL  | Yahoo Finance |
| JPM        | 2026-10-19 00:00:00 |   333.53      |         21.0833   | NEUTRAL  | Yahoo Finance |
| LDO-USD    | 2026-10-20 00:00:00 |     0.398     |        -21.25     | NEUTRAL  | Kraken API    |
| LINK-USD   | 2026-10-20 00:00:00 |    12.08      |        -18.5833   | NEUTRAL  | Kraken API    |
| LTC-USD    | 2026-10-20 00:00:00 |    59.89      |        -18.5833   | NEUTRAL  | Kraken API    |
| MCD        | 2026-10-19 00:00:00 |   242.67      |          4.41667  | NEUTRAL  | Yahoo Finance |
| META       | 2026-10-19 00:00:00 |   705.44      |         16.4167   | NEUTRAL  | Yahoo Finance |
| MRK        | 2026-10-19 00:00:00 |   143.63      |         -9.33333  | NEUTRAL  | Yahoo Finance |
| MU         | 2026-10-19 00:00:00 |   904.9       |        -22.0833   | NEUTRAL  | Yahoo Finance |
| NEAR-USD   | 2026-10-20 00:00:00 |     4.8252    |         -2.58333  | NEUTRAL  | Kraken API    |
| NFLX       | 2026-10-19 00:00:00 |    69.85      |        -15.25     | NEUTRAL  | Yahoo Finance |
| NKE        | 2026-10-19 00:00:00 |    37.21      |        -10.5833   | NEUTRAL  | Yahoo Finance |
| NOW        | 2026-10-19 00:00:00 |   145.36      |         60.8333   | NEUTRAL  | Yahoo Finance |
| OP-USD     | 2026-10-20 00:00:00 |     0.1284    |        -20.3333   | NEUTRAL  | Kraken API    |
| ORCL       | 2026-10-19 00:00:00 |   129.59      |        -50.5      | NEUTRAL  | Yahoo Finance |
| PEP        | 2026-10-19 00:00:00 |   133.57      |         22.9167   | NEUTRAL  | Yahoo Finance |
| PEPE-USD   | 2026-10-20 00:00:00 |     4.19e-06  |         22.5833   | NEUTRAL  | Kraken API    |
| PFE        | 2026-10-19 00:00:00 |    29.44      |         57.8333   | NEUTRAL  | Yahoo Finance |
| QCOM       | 2026-10-19 00:00:00 |   173.53      |        -17.8333   | NEUTRAL  | Yahoo Finance |
| QQQ        | 2026-10-19 00:00:00 |   718.36      |         -4.25     | NEUTRAL  | Yahoo Finance |
| RENDER-USD | 2026-10-20 00:00:00 |     1.825     |          3.16667  | NEUTRAL  | Kraken API    |
| SBUX       | 2026-10-19 00:00:00 |    97.87      |          8.16667  | NEUTRAL  | Yahoo Finance |
| SHY        | 2026-10-19 00:00:00 |    81.31      |          7        | NEUTRAL  | Yahoo Finance |
| SKY-USD    | 2026-10-20 00:00:00 |     0.0723    |        -20.0833   | NEUTRAL  | Kraken API    |
| SMH        | 2026-10-19 00:00:00 |   548.46      |         -5.83333  | NEUTRAL  | Yahoo Finance |
| SOXX       | 2026-10-19 00:00:00 |   501.93      |         -5.83333  | NEUTRAL  | Yahoo Finance |
| SPY        | 2026-10-19 00:00:00 |   766.48      |         12.1667   | NEUTRAL  | Yahoo Finance |
| TGT        | 2026-10-19 00:00:00 |   153.29      |        -26.8333   | NEUTRAL  | Yahoo Finance |
| TIA-USD    | 2026-10-20 00:00:00 |     0.6206    |         67.1667   | NEUTRAL  | Kraken API    |
| TLT        | 2026-10-19 00:00:00 |    79.46      |          3.91667  | NEUTRAL  | Yahoo Finance |
| TRX-USD    | 2026-10-20 00:00:00 |     0.331174  |        -16.9167   | NEUTRAL  | Kraken API    |
| TSLA       | 2026-10-19 00:00:00 |   368.06      |        -18.1667   | NEUTRAL  | Yahoo Finance |
| TXN        | 2026-10-19 00:00:00 |   276.15      |          0.416667 | NEUTRAL  | Yahoo Finance |
| UNI-USD    | 2026-10-20 00:00:00 |     7.2786    |        -16.5833   | NEUTRAL  | Kraken API    |
| UPS        | 2026-10-19 00:00:00 |    97.46      |          4.41667  | NEUTRAL  | Yahoo Finance |
| USO        | 2026-10-19 00:00:00 |   160.81      |         64        | NEUTRAL  | Yahoo Finance |
| VIXY       | 2026-10-19 00:00:00 |    17.01      |          2        | NEUTRAL  | Yahoo Finance |
| VNQ        | 2026-10-19 00:00:00 |    90.71      |        -14.0833   | NEUTRAL  | Yahoo Finance |
| VTI        | 2026-10-19 00:00:00 |   375.54      |         -5.83333  | NEUTRAL  | Yahoo Finance |
| VWO        | 2026-10-19 00:00:00 |    58.03      |        -44.5      | NEUTRAL  | Yahoo Finance |
| WFC        | 2026-10-19 00:00:00 |    81.8       |        -23.3333   | NEUTRAL  | Yahoo Finance |
| XBI        | 2026-10-19 00:00:00 |   147.86      |        -21.0833   | NEUTRAL  | Yahoo Finance |
| XLC        | 2026-10-19 00:00:00 |   110.09      |        -63.3333   | NEUTRAL  | Yahoo Finance |
| XLI        | 2026-10-19 00:00:00 |   166.68      |        -42.1667   | NEUTRAL  | Yahoo Finance |
| XLK        | 2026-10-19 00:00:00 |   185.96      |         -4.25     | NEUTRAL  | Yahoo Finance |
| XLU        | 2026-10-19 00:00:00 |    41.36      |          8.91667  | NEUTRAL  | Yahoo Finance |
| XLV        | 2026-10-19 00:00:00 |   175.65      |         59        | NEUTRAL  | Yahoo Finance |
| XLY        | 2026-10-19 00:00:00 |   114.46      |         20.75     | NEUTRAL  | Yahoo Finance |
| ZEC-USD    | 2026-10-20 00:00:00 |  1149.93      |        -20        | NEUTRAL  | Kraken API    |
| AMAT       | 2026-10-19 00:00:00 |   413.11      |        -58.5833   | SHORT    | Yahoo Finance |
| BAC        | 2026-10-19 00:00:00 |    50.39      |        -34.0833   | SHORT    | Yahoo Finance |
| BONK-USD   | 2026-10-20 00:00:00 |     2.956e-06 |        -42.3333   | SHORT    | Kraken API    |
| C          | 2026-10-19 00:00:00 |   121.69      |        -52.8333   | SHORT    | Yahoo Finance |
| CAT        | 2026-10-19 00:00:00 |   725.79      |        -56.5833   | SHORT    | Yahoo Finance |
| DOGE-USD   | 2026-10-20 00:00:00 |     0.0796824 |        -49.3333   | SHORT    | Kraken API    |
| ETC-USD    | 2026-10-20 00:00:00 |     7.764     |        -45.9167   | SHORT    | Kraken API    |
| GDXJ       | 2026-10-19 00:00:00 |   108.36      |        -49        | SHORT    | Yahoo Finance |
| GRT-USD    | 2026-10-20 00:00:00 |     0.02381   |        -38.5833   | SHORT    | Kraken API    |
| GS         | 2026-10-19 00:00:00 |   875.78      |        -34.9167   | SHORT    | Yahoo Finance |
| HBAR-USD   | 2026-10-20 00:00:00 |     0.08391   |        -49.6667   | SHORT    | Kraken API    |
| HYG        | 2026-10-19 00:00:00 |    76.83      |        -31        | SHORT    | Yahoo Finance |
| ITA        | 2026-10-19 00:00:00 |   207.76      |        -31.25     | SHORT    | Yahoo Finance |
| IWM        | 2026-10-19 00:00:00 |   271.28      |        -47        | SHORT    | Yahoo Finance |
| LRCX       | 2026-10-19 00:00:00 |   272.2       |        -62.5833   | SHORT    | Yahoo Finance |
| MS         | 2026-10-19 00:00:00 |   178.47      |        -52.0833   | SHORT    | Yahoo Finance |
| NVDA       | 2026-10-19 00:00:00 |   217.09      |        -15.25     | SHORT    | Yahoo Finance |
| POL-USD    | 2026-10-20 00:00:00 |     0.09312   |        -42.5833   | SHORT    | Kraken API    |
| SCHW       | 2026-10-19 00:00:00 |    89.58      |        -39.0833   | SHORT    | Yahoo Finance |
| SHIB-USD   | 2026-10-20 00:00:00 |     5.018e-06 |        -43.5833   | SHORT    | Kraken API    |
| SLB        | 2026-10-19 00:00:00 |    49.09      |        -33.25     | SHORT    | Yahoo Finance |
| SLV        | 2026-10-19 00:00:00 |    51.54      |        -56.0833   | SHORT    | Yahoo Finance |
| SNX-USD    | 2026-10-20 00:00:00 |     0.2169    |        -40.3333   | SHORT    | Kraken API    |
| SOL-USD    | 2026-10-20 00:00:00 |   105.14      |        -20.3333   | SHORT    | Kraken API    |
| SUSHI-USD  | 2026-10-20 00:00:00 |     0.2175    |        -44.25     | SHORT    | Kraken API    |
| T          | 2026-10-19 00:00:00 |    23.2       |        -51.1667   | SHORT    | Yahoo Finance |
| TMUS       | 2026-10-19 00:00:00 |   156.09      |        -48.75     | SHORT    | Yahoo Finance |
| VEA        | 2026-10-19 00:00:00 |    69.36      |        -33.25     | SHORT    | Yahoo Finance |
| VZ         | 2026-10-19 00:00:00 |    44.15      |        -47.0833   | SHORT    | Yahoo Finance |
| WIF-USD    | 2026-10-20 00:00:00 |     0.202     |        -47.5833   | SHORT    | Kraken API    |
| XLM-USD    | 2026-10-20 00:00:00 |     0.177714  |        -51.3333   | SHORT    | Kraken API    |
| XRP-USD    | 2026-10-20 00:00:00 |     1.30459   |        -45.5833   | SHORT    | Kraken API    |
| YFI-USD    | 2026-10-20 00:00:00 |  2201.2       |        -47.5833   | SHORT    | Kraken API    |

## Edge Summary

- Symbols with trades: **161** of 161
- Beat buy-and-hold: **32.30%** of traded symbols
- Positive return: **31.68%** of traded symbols
- Median strategy return: **-8.43%** (benchmark **21.66%**)
- Median excess vs benchmark: **-24.97%**
- Median Sharpe: **-0.07**
- Median exposure: **44.09%**

> Edge is real only if both _beat buy-and-hold_ and _median excess_ are convincingly positive across many symbols. Treat a single high-return symbol as noise.

## Portfolio Backtest

Actual capital-allocation books (not per-symbol averages). Benchmarks: `equal_weight_buyhold` (whole tracked universe), `spy_buyhold` (100% SPY), and `sixty_forty` (60% SPY / 40% AGG). `high_conf_voltarget` inverse-vol-weights the HIGH-confidence book; `conviction_long_short` is market-neutral. Judge on **Sharpe** and **max_drawdown** out-of-sample, not raw return: a fully-invested long book wins on return in a bull market but carries all the risk.

| strategy              | scope         | ann_return   | ann_vol   |   sharpe | max_drawdown   | total_return   |   avg_gross_exposure |
|:----------------------|:--------------|:-------------|:----------|---------:|:---------------|:---------------|---------------------:|
| equal_weight_buyhold  | full          | 11.90%       | 28.48%    |     0.42 | -39.53%        | 26.99%         |                 1    |
| equal_weight_buyhold  | out_of_sample | 19.14%       | 27.31%    |     0.7  | -18.71%        | 17.90%         |                 1    |
| all_signals_ew        | full          | -14.43%      | 24.29%    |    -0.59 | -55.89%        | -41.13%        |                 1    |
| all_signals_ew        | out_of_sample | 1.48%        | 23.21%    |     0.06 | -23.20%        | -1.28%         |                 1    |
| high_conf_ew          | full          | -3.75%       | 31.58%    |    -0.12 | -44.33%        | -23.23%        |                 0.9  |
| high_conf_ew          | out_of_sample | 6.10%        | 28.22%    |     0.22 | -22.85%        | 2.22%          |                 0.9  |
| high_conf_voltarget   | full          | -5.51%       | 28.34%    |    -0.19 | -39.75%        | -25.03%        |                 0.9  |
| high_conf_voltarget   | out_of_sample | -4.50%       | 23.34%    |    -0.19 | -17.69%        | -7.51%         |                 0.9  |
| conviction_long_short | full          | -13.34%      | 22.16%    |    -0.6  | -45.97%        | -38.25%        |                 0.97 |
| conviction_long_short | out_of_sample | -1.94%       | 19.61%    |    -0.1  | -26.77%        | -4.03%         |                 0.97 |
| spy_buyhold           | full          | 5.09%        | 13.64%    |     0.37 | -19.00%        | 13.52%         |                 0.78 |
| spy_buyhold           | out_of_sample | -0.93%       | 9.96%     |    -0.09 | -12.06%        | -1.51%         |                 0.78 |
| sixty_forty           | full          | 2.77%        | 8.60%     |     0.32 | -11.66%        | 7.58%          |                 0.78 |
| sixty_forty           | out_of_sample | -2.64%       | 6.69%     |    -0.39 | -8.26%         | -3.01%         |                 0.78 |

## Walk-Forward Robustness

Each book measured across contiguous time folds (each a different regime). A book has durable edge only if `mean_sharpe` is positive, `min_sharpe` isn't deeply negative, and `pct_positive_folds` is high — a single great fold doesn't count. `fold_sharpes` lists each fold oldest-to-newest.

| strategy              |   n_folds |   mean_sharpe |   median_sharpe |   min_sharpe | pct_positive_folds   | mean_return   | fold_sharpes                 |
|:----------------------|----------:|--------------:|----------------:|-------------:|:---------------------|:--------------|:-----------------------------|
| equal_weight_buyhold  |         5 |          0.63 |            1.03 |        -0.77 | 80.00%               | 6.37%         | 1.03;1.71;-0.77;0.02;1.14    |
| all_signals_ew        |         5 |         -0.65 |           -0.5  |        -1.98 | 20.00%               | -8.56%        | -1.49;-0.31;-1.98;1.05;-0.50 |
| high_conf_ew          |         5 |         -0    |           -0.02 |        -1.13 | 40.00%               | -3.72%        | 0.03;-0.12;-1.13;1.21;-0.02  |
| high_conf_voltarget   |         5 |         -0.05 |           -0.09 |        -1.05 | 40.00%               | -4.65%        | 0.25;-0.09;-1.05;0.80;-0.18  |
| conviction_long_short |         5 |         -0.6  |           -0.62 |        -2.05 | 40.00%               | -8.72%        | -2.05;0.27;-0.62;-0.75;0.16  |
| spy_buyhold           |         5 |          0.31 |            0.26 |        -0.58 | 60.00%               | 2.71%         | 1.50;0.26;-0.31;0.70;-0.58   |
| sixty_forty           |         5 |          0.25 |            0.3  |        -0.79 | 60.00%               | 1.53%         | 1.46;0.31;-0.03;0.30;-0.79   |

## Strategy Comparison

Each decision rule backtested over the same data. `out_of_sample` is the most recent ~35% of each symbol's history (unseen tail). A rule has real edge only if `median_excess` and `beat_benchmark_pct` stay positive out-of-sample, not just full-sample.

| strategy        | scope         |   symbols | beat_benchmark_pct   | positive_pct   | median_return   | median_benchmark   | median_excess   |   median_sharpe |   total_trades |
|:----------------|:--------------|----------:|:---------------------|:---------------|:----------------|:-------------------|:----------------|----------------:|---------------:|
| trend           | full          |       161 | 32.30%               | 31.68%         | -8.43%          | 21.66%             | -24.97%         |           -0.07 |          11293 |
| trend           | out_of_sample |       161 | 30.43%               | 52.80%         | 0.50%           | 8.00%              | -13.96%         |            0.14 |           3792 |
| mean_reversion  | full          |       157 | 38.22%               | 48.41%         | -0.23%          | 18.65%             | -18.40%         |           -0.01 |           1230 |
| mean_reversion  | out_of_sample |       121 | 31.40%               | 52.89%         | 0.29%           | 5.89%              | -7.94%          |            0.2  |            476 |
| regime_adaptive | full          |       161 | 33.54%               | 31.06%         | -8.67%          | 21.66%             | -23.97%         |           -0.1  |          11562 |
| regime_adaptive | out_of_sample |       161 | 31.06%               | 51.55%         | 0.19%           | 8.00%              | -14.10%         |            0.09 |           3896 |

## Signal Calibration

Realized forward return in the signal's direction, grouped by confidence. HIGH should outrank LOW for the confidence score to be meaningful.

| confidence_level   |   horizon |     n | mean_return   | median_return   | win_rate   |
|:-------------------|----------:|------:|:--------------|:----------------|:-----------|
| HIGH               |         5 |  7870 | 0.22%         | 0.05%           | 50.97%     |
| MEDIUM             |         5 | 29054 | 0.05%         | 0.04%           | 50.43%     |
| LOW                |         5 |  3539 | -0.36%        | -0.39%          | 46.20%     |
| ALL                |         5 | 40463 | 0.05%         | 0.02%           | 50.16%     |
| HIGH               |        10 |  7825 | 0.44%         | 0.07%           | 50.77%     |
| MEDIUM             |        10 | 28838 | 0.15%         | 0.04%           | 50.34%     |
| LOW                |        10 |  3479 | -0.71%        | -0.50%          | 46.85%     |
| ALL                |        10 | 40142 | 0.13%         | 0.02%           | 50.12%     |
| HIGH               |        20 |  7740 | 0.96%         | 0.26%           | 52.12%     |
| MEDIUM             |        20 | 28270 | 0.88%         | 0.56%           | 53.19%     |
| LOW                |        20 |  3381 | -0.39%        | -0.51%          | 47.47%     |
| ALL                |        20 | 39391 | 0.79%         | 0.43%           | 52.49%     |

## Backtest Summary

### Data Quality / Signal Availability

- **ok**: 161 symbols

| symbol     |   trades | return   | benchmark_return   | mdd     |   sharpe | exposure   | skipped_reason   |
|:-----------|---------:|:---------|:-------------------|:--------|---------:|:-----------|:-----------------|
| AAPL       |       63 | 7.48%    | 80.50%             | -20.65% |     0.25 | 50.25%     | ok               |
| AAVE-USD   |       65 | -34.54%  | -32.02%            | -66.17% |    -0.18 | 41.19%     | ok               |
| ABBV       |       70 | -23.04%  | 81.98%             | -30.52% |    -0.49 | 48.42%     | ok               |
| ADA-USD    |       74 | -29.68%  | -70.62%            | -52.70% |    -0.17 | 45.02%     | ok               |
| ADBE       |       71 | -11.61%  | -48.35%            | -31.20% |    -0.03 | 56.91%     | ok               |
| AGG        |       63 | -5.89%   | -1.06%             | -10.74% |    -0.92 | 33.28%     | ok               |
| ALGO-USD   |       76 | -27.99%  | -48.14%            | -39.25% |    -0.16 | 40.04%     | ok               |
| AMAT       |       73 | -40.67%  | 86.66%             | -57.08% |    -0.42 | 51.25%     | ok               |
| AMD        |       54 | 17.78%   | 213.53%            | -40.85% |     0.38 | 37.10%     | ok               |
| AMGN       |       65 | -12.42%  | 41.56%             | -34.19% |    -0.2  | 50.92%     | ok               |
| AMZN       |       80 | -55.73%  | 44.08%             | -56.19% |    -1.6  | 41.26%     | ok               |
| APT-USD    |       70 | -23.20%  | -84.84%            | -56.73% |    -0    | 39.66%     | ok               |
| ARB-USD    |       77 | -3.61%   | -46.92%            | -48.19% |     0.25 | 43.30%     | ok               |
| ARKK       |       89 | -30.46%  | 86.94%             | -34.52% |    -0.47 | 43.59%     | ok               |
| ATOM-USD   |       90 | -57.79%  | -62.62%            | -57.79% |    -0.8  | 47.89%     | ok               |
| AVAX-USD   |       66 | -32.18%  | -56.73%            | -45.41% |    -0.24 | 39.66%     | ok               |
| AVGO       |       64 | 15.92%   | 136.89%            | -36.09% |     0.35 | 41.10%     | ok               |
| BA         |       67 | 11.36%   | 9.33%              | -24.47% |     0.31 | 51.08%     | ok               |
| BAC        |       74 | -8.36%   | 28.15%             | -23.78% |    -0.17 | 48.59%     | ok               |
| BCH-USD    |       78 | 3.60%    | -28.86%            | -53.87% |     0.25 | 48.28%     | ok               |
| BITO       |       79 | -23.22%  | -60.59%            | -43.10% |    -0.15 | 41.26%     | ok               |
| BLK        |       83 | -12.59%  | 45.78%             | -26.90% |    -0.29 | 46.76%     | ok               |
| BND        |       64 | -6.07%   | -1.02%             | -10.80% |    -0.93 | 34.78%     | ok               |
| BONK-USD   |       72 | 32.46%   | -83.96%            | -48.17% |     0.52 | 45.79%     | ok               |
| BTC-USD    |       72 | 4.23%    | -20.47%            | -23.38% |     0.21 | 50.96%     | ok               |
| C          |       77 | -33.18%  | 94.86%             | -39.51% |    -0.7  | 46.26%     | ok               |
| CAT        |       70 | 7.70%    | 109.48%            | -21.87% |     0.25 | 48.25%     | ok               |
| CL         |       64 | 0.87%    | 1.58%              | -14.32% |     0.09 | 38.60%     | ok               |
| CMCSA      |       86 | -39.01%  | -39.37%            | -47.69% |    -0.96 | 43.59%     | ok               |
| COMP-USD   |       97 | -37.68%  | -50.84%            | -55.77% |    -0.21 | 49.81%     | ok               |
| COP        |       66 | -8.79%   | 22.09%             | -41.35% |    -0.06 | 44.09%     | ok               |
| COST       |       60 | -0.17%   | 22.43%             | -31.32% |     0.06 | 41.10%     | ok               |
| CRM        |       67 | -30.80%  | -10.15%            | -44.41% |    -0.42 | 46.92%     | ok               |
| CRV-USD    |       64 | 42.17%   | -44.60%            | -39.89% |     0.58 | 36.40%     | ok               |
| CSCO       |       63 | 11.21%   | 130.12%            | -22.29% |     0.31 | 49.92%     | ok               |
| CVX        |       71 | -12.26%  | 41.08%             | -26.75% |    -0.25 | 42.93%     | ok               |
| DASH-USD   |       53 | -0.66%   | 119.49%            | -64.43% |     0.38 | 29.89%     | ok               |
| DBC        |       66 | -8.16%   | 40.69%             | -24.10% |    -0.21 | 35.27%     | ok               |
| DE         |       70 | -12.17%  | 69.79%             | -23.98% |    -0.18 | 44.26%     | ok               |
| DIA        |       64 | -4.46%   | 33.54%             | -12.94% |    -0.21 | 43.26%     | ok               |
| DIS        |       64 | -6.51%   | 6.98%              | -28.17% |    -0.06 | 43.76%     | ok               |
| DOGE-USD   |       67 | -19.39%  | -62.87%            | -60.95% |     0.01 | 48.85%     | ok               |
| DOT-USD    |       84 | -48.42%  | -75.00%            | -63.33% |    -0.37 | 47.70%     | ok               |
| DXY-INDEX  |       38 | -0.54%   | -5.77%             | -6.02%  |    -0.07 | 32.03%     | ok               |
| EEM        |       66 | -11.00%  | 47.37%             | -24.14% |    -0.3  | 39.93%     | ok               |
| EFA        |       66 | -11.05%  | 26.97%             | -12.96% |    -0.43 | 40.77%     | ok               |
| EOG        |       78 | -24.43%  | 25.27%             | -47.50% |    -0.48 | 44.93%     | ok               |
| ETC-USD    |       56 | -15.09%  | -57.21%            | -45.54% |    -0.07 | 31.99%     | ok               |
| ETH-USD    |       58 | 148.80%  | -2.67%             | -30.11% |     1.34 | 47.13%     | ok               |
| EWJ        |       62 | -22.99%  | 37.97%             | -29.40% |    -0.8  | 36.44%     | ok               |
| FCX        |       67 | -32.07%  | 30.06%             | -46.84% |    -0.38 | 44.09%     | ok               |
| FET-USD    |       81 | -49.02%  | -74.28%            | -65.38% |    -0.33 | 42.53%     | ok               |
| FIL-USD    |       65 | -40.15%  | -63.20%            | -58.54% |    -0.34 | 37.16%     | ok               |
| FXI        |       48 | -4.53%   | 21.66%             | -23.91% |    -0.03 | 30.45%     | ok               |
| GDX        |       62 | -0.37%   | 139.53%            | -33.31% |     0.13 | 44.26%     | ok               |
| GDXJ       |       72 | -36.02%  | 135.92%            | -39.63% |    -0.46 | 43.09%     | ok               |
| GE         |       76 | -8.43%   | 84.67%             | -27.82% |    -0.04 | 48.09%     | ok               |
| GLD        |       50 | 12.09%   | 74.02%             | -13.87% |     0.36 | 45.59%     | ok               |
| GOOGL      |       57 | 56.29%   | 95.11%             | -17.54% |     1    | 46.92%     | ok               |
| GRT-USD    |       79 | 64.78%   | -77.44%            | -33.74% |     0.74 | 45.98%     | ok               |
| GS         |       70 | -1.97%   | 90.47%             | -21.94% |     0.06 | 48.09%     | ok               |
| HBAR-USD   |       40 | -42.35%  | -18.64%            | -56.47% |    -0.9  | 39.03%     | ok               |
| HD         |       69 | 0.85%    | -5.73%             | -17.15% |     0.1  | 43.43%     | ok               |
| HON        |       91 | -25.82%  | 6.65%              | -33.03% |    -0.64 | 54.41%     | ok               |
| HYG        |       87 | -7.26%   | 0.07%              | -10.59% |    -0.81 | 39.10%     | ok               |
| IBIT       |       40 | 36.51%   | 21.81%             | -18.95% |     0.67 | 34.88%     | ok               |
| IBM        |       69 | -24.58%  | 39.33%             | -48.94% |    -0.29 | 48.75%     | ok               |
| ICP-USD    |       77 | -14.23%  | -44.37%            | -44.07% |     0.13 | 39.08%     | ok               |
| IEF        |       74 | -9.01%   | -2.47%             | -12.66% |    -1.21 | 33.78%     | ok               |
| IEMG       |       62 | -8.10%   | 43.33%             | -24.73% |    -0.22 | 39.77%     | ok               |
| INJ-USD    |       63 | -27.85%  | -25.52%            | -68.17% |    -0.03 | 40.23%     | ok               |
| INTC       |       66 | 41.91%   | 196.30%            | -60.60% |     0.54 | 47.92%     | ok               |
| INTU       |       73 | -6.08%   | -45.73%            | -38.67% |     0.03 | 46.59%     | ok               |
| ITA        |       78 | -2.45%   | 54.72%             | -23.75% |     0.01 | 48.09%     | ok               |
| IWM        |       56 | 8.51%    | 32.23%             | -9.49%  |     0.36 | 34.11%     | ok               |
| JNJ        |       58 | 10.08%   | 75.78%             | -16.86% |     0.41 | 46.59%     | ok               |
| JPM        |       75 | -24.28%  | 67.18%             | -32.74% |    -0.69 | 44.59%     | ok               |
| KO         |       54 | 27.00%   | 51.12%             | -8.64%  |     0.94 | 36.94%     | ok               |
| LDO-USD    |       72 | 41.50%   | -56.36%            | -50.47% |     0.57 | 47.13%     | ok               |
| LIN        |       72 | -7.87%   | 17.10%             | -20.61% |    -0.22 | 38.60%     | ok               |
| LINK-USD   |       64 | 56.97%   | -21.18%            | -33.64% |     0.71 | 44.44%     | ok               |
| LLY        |       80 | -34.06%  | 53.53%             | -53.42% |    -0.55 | 49.25%     | ok               |
| LRCX       |       85 | -34.91%  | 180.25%            | -61.92% |    -0.31 | 43.09%     | ok               |
| LTC-USD    |       67 | 7.48%    | -37.65%            | -30.78% |     0.29 | 51.72%     | ok               |
| MCD        |       79 | -5.85%   | -4.29%             | -21.88% |    -0.17 | 40.27%     | ok               |
| META       |       74 | -28.71%  | 46.99%             | -44.90% |    -0.41 | 50.42%     | ok               |
| MPC        |       72 | 20.26%   | 164.39%            | -34.29% |     0.43 | 52.58%     | ok               |
| MRK        |       65 | -23.45%  | 13.91%             | -35.95% |    -0.45 | 42.43%     | ok               |
| MS         |       75 | -2.87%   | 80.88%             | -27.79% |     0.02 | 48.25%     | ok               |
| MSFT       |       83 | -26.33%  | 23.98%             | -39.15% |    -0.56 | 51.41%     | ok               |
| MU         |       51 | 130.90%  | 582.07%            | -68.76% |     0.96 | 52.08%     | ok               |
| NEAR-USD   |       69 | 172.52%  | 79.24%             | -46.60% |     1.12 | 44.06%     | ok               |
| NEM        |       72 | -26.02%  | 178.33%            | -39.56% |    -0.25 | 49.92%     | ok               |
| NFLX       |       78 | 3.57%    | 7.63%              | -21.09% |     0.18 | 52.41%     | ok               |
| NKE        |       81 | -30.33%  | -59.55%            | -55.35% |    -0.36 | 47.09%     | ok               |
| NOW        |       80 | 11.00%   | -0.28%             | -30.43% |     0.3  | 50.25%     | ok               |
| NVDA       |       79 | -50.84%  | 93.35%             | -54.06% |    -0.74 | 55.79%     | ok               |
| OP-USD     |       70 | -41.46%  | -81.59%            | -58.87% |    -0.33 | 33.14%     | ok               |
| ORCL       |       62 | 85.70%   | 4.10%              | -30.61% |     0.8  | 51.58%     | ok               |
| OXY        |       71 | 4.10%    | 0.82%              | -28.48% |     0.19 | 42.76%     | ok               |
| PEP        |       74 | 2.89%    | -22.96%            | -21.35% |     0.15 | 45.26%     | ok               |
| PEPE-USD   |       81 | -50.17%  | -65.58%            | -61.29% |    -0.34 | 47.51%     | ok               |
| PFE        |       77 | -33.11%  | 4.03%              | -41.77% |    -1.03 | 36.27%     | ok               |
| PG         |       64 | -21.11%  | -3.32%             | -24.16% |    -0.83 | 34.44%     | ok               |
| PM         |       81 | -9.47%   | 100.95%            | -36.48% |    -0.13 | 49.75%     | ok               |
| POL-USD    |       79 | 51.91%   | -59.74%            | -38.69% |     0.68 | 49.81%     | ok               |
| QCOM       |       77 | -31.89%  | -18.56%            | -56.59% |    -0.3  | 42.93%     | ok               |
| QQQ        |       68 | 5.57%    | 56.27%             | -13.88% |     0.22 | 45.42%     | ok               |
| RENDER-USD |       90 | -21.39%  | -59.76%            | -44.65% |     0.05 | 47.51%     | ok               |
| RTX        |       68 | 26.61%   | 82.06%             | -16.99% |     0.63 | 51.75%     | ok               |
| SBUX       |       60 | -14.35%  | 26.32%             | -29.22% |    -0.23 | 38.60%     | ok               |
| SCHW       |       82 | -13.13%  | 26.54%             | -31.92% |    -0.25 | 46.42%     | ok               |
| SHIB-USD   |       79 | -30.55%  | -64.64%            | -46.79% |    -0.25 | 52.68%     | ok               |
| SHY        |       48 | -1.87%   | 0.01%              | -3.30%  |    -0.63 | 36.94%     | ok               |
| SKY-USD    |       85 | -57.99%  | 0.46%              | -61.82% |    -0.9  | 43.30%     | ok               |
| SLB        |       75 | -41.03%  | 5.50%              | -59.65% |    -0.8  | 49.25%     | ok               |
| SLV        |       68 | 8.34%    | 76.27%             | -42.46% |     0.28 | 40.10%     | ok               |
| SMH        |       50 | 39.75%   | 119.53%            | -33.99% |     0.69 | 43.09%     | ok               |
| SNX-USD    |       62 | -5.59%   | -72.37%            | -50.74% |     0.15 | 34.29%     | ok               |
| SOL-USD    |       73 | -15.89%  | -36.67%            | -44.99% |     0.05 | 59.39%     | ok               |
| SOXX       |       56 | 52.71%   | 106.90%            | -40.14% |     0.79 | 42.60%     | ok               |
| SPY        |       64 | -0.13%   | 44.67%             | -15.53% |     0.06 | 48.92%     | ok               |
| SUSHI-USD  |       94 | -69.98%  | -68.66%            | -76.07% |    -1    | 39.66%     | ok               |
| T          |       72 | 44.91%   | 34.34%             | -17.01% |     0.88 | 56.74%     | ok               |
| TGT        |       60 | -11.06%  | 4.21%              | -34.42% |    -0.16 | 37.60%     | ok               |
| TIA-USD    |       91 | -36.08%  | -75.91%            | -74.53% |    -0.07 | 43.30%     | ok               |
| TLT        |       66 | -18.66%  | -11.78%            | -21.85% |    -1.41 | 33.28%     | ok               |
| TMO        |       67 | 35.76%   | 18.65%             | -18.85% |     0.7  | 55.41%     | ok               |
| TMUS       |       74 | -2.98%   | -6.71%             | -33.01% |     0.04 | 48.42%     | ok               |
| TRX-USD    |       66 | 2.27%    | 22.86%             | -22.90% |     0.15 | 49.81%     | ok               |
| TSLA       |       78 | -35.00%  | 108.24%            | -59.64% |    -0.22 | 42.76%     | ok               |
| TXN        |       77 | -27.17%  | 38.35%             | -46.56% |    -0.31 | 50.25%     | ok               |
| UNH        |       75 | 36.02%   | -19.22%            | -26.31% |     0.58 | 48.42%     | ok               |
| UNI-USD    |       86 | -27.77%  | 26.89%             | -65.36% |    -0.01 | 49.43%     | ok               |
| UPS        |       72 | -38.74%  | -29.16%            | -40.10% |    -0.8  | 42.26%     | ok               |
| USO        |       67 | -12.16%  | 107.07%            | -45.91% |    -0.05 | 33.44%     | ok               |
| VEA        |       64 | -3.64%   | 36.80%             | -17.27% |    -0.1  | 42.26%     | ok               |
| VIXY       |       94 | -78.16%  | -62.76%            | -88.17% |    -0.94 | 31.78%     | ok               |
| VNQ        |       73 | -13.66%  | 11.55%             | -24.92% |    -0.54 | 39.77%     | ok               |
| VTI        |       68 | -7.39%   | 43.41%             | -17.64% |    -0.21 | 48.92%     | ok               |
| VWO        |       80 | -17.80%  | 31.65%             | -25.20% |    -0.67 | 39.93%     | ok               |
| VZ         |       84 | -24.78%  | 12.17%             | -29.49% |    -0.75 | 42.26%     | ok               |
| WFC        |       82 | -19.91%  | 37.53%             | -28.90% |    -0.34 | 46.92%     | ok               |
| WIF-USD    |       66 | -28.69%  | -78.31%            | -52.76% |    -0.04 | 38.31%     | ok               |
| WMT        |       69 | 4.55%    | 82.50%             | -25.37% |     0.2  | 48.42%     | ok               |
| XBI        |       62 | 0.54%    | 65.89%             | -17.66% |     0.1  | 38.44%     | ok               |
| XLB        |       66 | -12.76%  | 11.97%             | -24.18% |    -0.45 | 31.61%     | ok               |
| XLC        |       61 | 12.28%   | 32.49%             | -12.33% |     0.46 | 49.75%     | ok               |
| XLE        |       69 | -1.86%   | 46.90%             | -29.67% |     0.04 | 45.92%     | ok               |
| XLF        |       82 | -8.49%   | 33.80%             | -23.61% |    -0.26 | 46.42%     | ok               |
| XLI        |       82 | -10.04%  | 35.58%             | -17.79% |    -0.35 | 42.76%     | ok               |
| XLK        |       44 | 46.12%   | 72.11%             | -14.75% |     0.93 | 45.76%     | ok               |
| XLM-USD    |       66 | 6.68%    | -37.94%            | -54.58% |     0.29 | 47.51%     | ok               |
| XLP        |       65 | 9.00%    | 14.00%             | -10.28% |     0.52 | 38.44%     | ok               |
| XLU        |       69 | -5.11%   | 15.81%             | -20.40% |    -0.18 | 39.10%     | ok               |
| XLV        |       74 | -20.17%  | 23.12%             | -22.55% |    -0.96 | 36.44%     | ok               |
| XLY        |       75 | -4.15%   | 30.73%             | -18.35% |    -0.06 | 47.59%     | ok               |
| XOM        |       57 | 3.77%    | 55.22%             | -20.29% |     0.18 | 34.61%     | ok               |
| XRP-USD    |       66 | 9.02%    | -44.58%            | -33.91% |     0.3  | 36.40%     | ok               |
| YFI-USD    |       76 | -58.98%  | -60.24%            | -60.97% |    -1.07 | 37.36%     | ok               |
| ZEC-USD    |       57 | 160.76%  | 2740.74%           | -56.50% |     0.95 | 40.42%     | ok               |

## AAPL Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 14.21%   | 80.50%             | -21.71% |     0.36 |       72 | 55.07%     | ok               |
|          15 | 11.27%   | 80.50%             | -23.86% |     0.31 |       81 | 62.40%     | ok               |
|          30 | 7.48%    | 80.50%             | -20.65% |     0.25 |       63 | 50.25%     | ok               |
|          35 | 5.94%    | 80.50%             | -22.04% |     0.22 |       63 | 48.92%     | ok               |
|          25 | 3.13%    | 80.50%             | -20.87% |     0.17 |       73 | 52.41%     | ok               |

## AAVE-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 28.44%   | -32.02%            | -43.61% |     0.49 |       43 | 35.63%     | ok               |
|          45 | 16.47%   | -32.02%            | -49.19% |     0.38 |       48 | 30.46%     | ok               |
|          35 | 12.04%   | -32.02%            | -48.79% |     0.34 |       51 | 38.70%     | ok               |
|          50 | 11.25%   | -32.02%            | -45.07% |     0.32 |       46 | 22.80%     | ok               |
|          15 | -36.24%  | -32.02%            | -61.76% |    -0.12 |       72 | 54.02%     | ok               |

## ABBV Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -6.61%   | 81.98%             | -23.80% |    -0.09 |       54 | 35.27%     | ok               |
|          20 | -20.02%  | 81.98%             | -28.73% |    -0.39 |       66 | 51.75%     | ok               |
|          25 | -20.12%  | 81.98%             | -30.04% |    -0.4  |       69 | 50.25%     | ok               |
|          40 | -20.03%  | 81.98%             | -27.36% |    -0.45 |       70 | 40.93%     | ok               |
|          30 | -23.04%  | 81.98%             | -30.52% |    -0.49 |       70 | 48.42%     | ok               |

## ADA-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 24.35%   | -70.62%            | -34.64% |     0.47 |       44 | 30.65%     | ok               |
|          50 | 17.24%   | -70.62%            | -35.54% |     0.39 |       46 | 26.25%     | ok               |
|          40 | 3.14%    | -70.62%            | -40.73% |     0.24 |       56 | 36.59%     | ok               |
|          15 | -15.73%  | -70.62%            | -47.27% |     0.12 |       71 | 60.92%     | ok               |
|          35 | -9.39%   | -70.62%            | -44.07% |     0.1  |       62 | 40.42%     | ok               |

## ADBE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | 8.08%    | -48.35%            | -29.07% |     0.26 |       53 | 61.06%     | ok               |
|          20 | -6.08%   | -48.35%            | -31.52% |     0.07 |       59 | 64.06%     | ok               |
|          35 | -3.98%   | -48.35%            | -31.73% |     0.06 |       78 | 48.25%     | ok               |
|          30 | -11.61%  | -48.35%            | -31.20% |    -0.03 |       71 | 56.91%     | ok               |
|          15 | -13.40%  | -48.35%            | -34.98% |    -0.04 |       64 | 65.72%     | ok               |

## AGG Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -4.96%   | -1.06%             | -9.29%  |    -0.89 |       60 | 24.29%     | ok               |
|          30 | -5.89%   | -1.06%             | -10.74% |    -0.92 |       63 | 33.28%     | ok               |
|          35 | -6.62%   | -1.06%             | -11.43% |    -1.07 |       62 | 30.12%     | ok               |
|          40 | -6.58%   | -1.06%             | -11.07% |    -1.14 |       58 | 27.62%     | ok               |
|          25 | -7.62%   | -1.06%             | -12.28% |    -1.14 |       69 | 36.27%     | ok               |

## ALGO-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -27.99%  | -48.14%            | -39.25% |    -0.16 |       76 | 40.04%     | ok               |
|          25 | -37.21%  | -48.14%            | -51.92% |    -0.28 |       78 | 44.83%     | ok               |
|          15 | -41.71%  | -48.14%            | -51.37% |    -0.32 |       75 | 50.96%     | ok               |
|          35 | -40.58%  | -48.14%            | -52.80% |    -0.46 |       64 | 34.87%     | ok               |
|          20 | -48.39%  | -48.14%            | -53.71% |    -0.47 |       79 | 47.89%     | ok               |

## AMAT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -31.96%  | 86.66%             | -53.90% |    -0.21 |       74 | 60.57%     | ok               |
|          50 | -36.29%  | 86.66%             | -47.29% |    -0.41 |       52 | 36.44%     | ok               |
|          30 | -40.67%  | 86.66%             | -57.08% |    -0.42 |       73 | 51.25%     | ok               |
|          35 | -40.42%  | 86.66%             | -54.63% |    -0.44 |       73 | 48.75%     | ok               |
|          20 | -45.87%  | 86.66%             | -60.04% |    -0.48 |       78 | 56.57%     | ok               |

## AMD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 28.48%   | 213.53%            | -39.67% |     0.47 |       54 | 32.11%     | ok               |
|          40 | 17.78%   | 213.53%            | -40.85% |     0.38 |       54 | 37.10%     | ok               |
|          35 | 12.72%   | 213.53%            | -42.92% |     0.33 |       62 | 38.77%     | ok               |
|          45 | 2.56%    | 213.53%            | -49.38% |     0.23 |       60 | 34.94%     | ok               |
|          30 | -2.14%   | 213.53%            | -49.58% |     0.2  |       63 | 41.26%     | ok               |

## AMGN Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -7.56%   | 41.56%             | -26.65% |    -0.06 |       66 | 56.57%     | ok               |
|          35 | -10.21%  | 41.56%             | -31.29% |    -0.14 |       67 | 47.59%     | ok               |
|          15 | -13.01%  | 41.56%             | -27.98% |    -0.18 |       63 | 60.73%     | ok               |
|          30 | -12.42%  | 41.56%             | -34.19% |    -0.2  |       65 | 50.92%     | ok               |
|          25 | -14.22%  | 41.56%             | -33.47% |    -0.23 |       61 | 53.08%     | ok               |

## AMZN Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -27.97%  | 44.08%             | -29.61% |    -0.85 |       56 | 29.95%     | ok               |
|          50 | -31.74%  | 44.08%             | -33.91% |    -1.16 |       50 | 22.80%     | ok               |
|          45 | -37.46%  | 44.08%             | -38.25% |    -1.34 |       58 | 26.46%     | ok               |
|          35 | -52.04%  | 44.08%             | -52.54% |    -1.53 |       77 | 35.27%     | ok               |
|          30 | -55.73%  | 44.08%             | -56.19% |    -1.6  |       80 | 41.26%     | ok               |

## APT-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 25.37%   | -84.84%            | -31.21% |     0.52 |       42 | 16.28%     | ok               |
|          20 | 0.36%    | -84.84%            | -56.22% |     0.28 |       78 | 49.62%     | ok               |
|          45 | -1.29%   | -84.84%            | -53.47% |     0.18 |       58 | 23.18%     | ok               |
|          35 | -14.40%  | -84.84%            | -49.10% |     0.07 |       68 | 35.44%     | ok               |
|          25 | -22.50%  | -84.84%            | -55.69% |     0.03 |       70 | 44.25%     | ok               |

## ARB-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 57.32%   | -46.92%            | -33.60% |     0.67 |       54 | 26.44%     | ok               |
|          15 | 51.28%   | -46.92%            | -44.26% |     0.62 |       90 | 58.62%     | ok               |
|          50 | 46.51%   | -46.92%            | -30.72% |     0.61 |       42 | 19.35%     | ok               |
|          40 | 27.44%   | -46.92%            | -40.13% |     0.48 |       55 | 33.72%     | ok               |
|          35 | 21.94%   | -46.92%            | -45.71% |     0.44 |       71 | 37.93%     | ok               |

## ARKK Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -16.33%  | 86.94%             | -37.76% |    -0.11 |       90 | 54.74%     | ok               |
|          20 | -25.01%  | 86.94%             | -34.82% |    -0.29 |       91 | 50.08%     | ok               |
|          30 | -30.46%  | 86.94%             | -34.52% |    -0.47 |       89 | 43.59%     | ok               |
|          35 | -37.04%  | 86.94%             | -39.81% |    -0.66 |       90 | 40.77%     | ok               |
|          25 | -40.48%  | 86.94%             | -46.36% |    -0.69 |       99 | 46.09%     | ok               |

## ATOM-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -40.42%  | -62.62%            | -48.77% |    -0.31 |       84 | 65.33%     | ok               |
|          25 | -47.30%  | -62.62%            | -50.00% |    -0.5  |       90 | 54.02%     | ok               |
|          20 | -54.81%  | -62.62%            | -57.75% |    -0.64 |       94 | 57.66%     | ok               |
|          30 | -57.79%  | -62.62%            | -57.79% |    -0.8  |       90 | 47.89%     | ok               |
|          35 | -59.37%  | -62.62%            | -61.61% |    -0.94 |       82 | 42.15%     | ok               |

## AVAX-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 53.25%   | -56.73%            | -22.06% |     0.83 |       32 | 19.73%     | ok               |
|          40 | 19.68%   | -56.73%            | -26.61% |     0.43 |       38 | 27.39%     | ok               |
|          45 | 16.86%   | -56.73%            | -23.19% |     0.39 |       30 | 24.14%     | ok               |
|          15 | -5.67%   | -56.73%            | -43.71% |     0.17 |       71 | 52.11%     | ok               |
|          35 | -2.49%   | -56.73%            | -33.36% |     0.16 |       54 | 33.52%     | ok               |

## AVGO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | 19.25%   | 136.89%            | -38.01% |     0.38 |       68 | 43.76%     | ok               |
|          30 | 15.92%   | 136.89%            | -36.09% |     0.35 |       64 | 41.10%     | ok               |
|          50 | 10.97%   | 136.89%            | -36.86% |     0.29 |       56 | 28.95%     | ok               |
|          35 | 7.50%    | 136.89%            | -40.43% |     0.26 |       74 | 38.10%     | ok               |
|          20 | 5.57%    | 136.89%            | -39.42% |     0.24 |       77 | 46.92%     | ok               |

## BA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 41.10%   | 9.33%              | -13.34% |     0.9  |       46 | 35.77%     | ok               |
|          40 | 34.40%   | 9.33%              | -23.87% |     0.67 |       46 | 43.43%     | ok               |
|          35 | 33.36%   | 9.33%              | -18.19% |     0.62 |       62 | 47.75%     | ok               |
|          25 | 21.69%   | 9.33%              | -26.02% |     0.45 |       68 | 54.58%     | ok               |
|          30 | 11.36%   | 9.33%              | -24.47% |     0.31 |       67 | 51.08%     | ok               |

## BAC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 1.15%    | 28.15%             | -20.99% |     0.11 |       68 | 45.09%     | ok               |
|          20 | -0.10%   | 28.15%             | -18.20% |     0.08 |       82 | 53.41%     | ok               |
|          25 | -2.54%   | 28.15%             | -22.11% |     0.01 |       76 | 50.92%     | ok               |
|          15 | -8.12%   | 28.15%             | -23.94% |    -0.11 |       89 | 60.57%     | ok               |
|          45 | -5.76%   | 28.15%             | -17.34% |    -0.12 |       60 | 36.44%     | ok               |

## BCH-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 45.21%   | -28.86%            | -45.51% |     0.61 |       76 | 56.70%     | ok               |
|          20 | 20.43%   | -28.86%            | -45.63% |     0.42 |       68 | 53.45%     | ok               |
|          25 | 3.40%    | -28.86%            | -51.09% |     0.25 |       72 | 49.81%     | ok               |
|          30 | 3.60%    | -28.86%            | -53.87% |     0.25 |       78 | 48.28%     | ok               |
|          35 | -3.02%   | -28.86%            | -57.75% |     0.17 |       72 | 44.06%     | ok               |

## BITO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -7.11%   | -60.59%            | -31.98% |     0.03 |       54 | 24.79%     | ok               |
|          30 | -23.22%  | -60.59%            | -43.10% |    -0.15 |       79 | 41.26%     | ok               |
|          45 | -19.90%  | -60.59%            | -33.51% |    -0.18 |       60 | 28.29%     | ok               |
|          40 | -24.05%  | -60.59%            | -40.13% |    -0.22 |       62 | 32.61%     | ok               |
|          35 | -26.05%  | -60.59%            | -42.34% |    -0.22 |       70 | 36.77%     | ok               |

## BLK Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | -4.08%   | 45.78%             | -20.79% |    -0.05 |       90 | 43.09%     | ok               |
|          40 | -5.36%   | 45.78%             | -22.83% |    -0.1  |       78 | 38.27%     | ok               |
|          20 | -7.01%   | 45.78%             | -21.48% |    -0.11 |       86 | 51.41%     | ok               |
|          25 | -8.34%   | 45.78%             | -24.62% |    -0.15 |       79 | 49.25%     | ok               |
|          30 | -12.59%  | 45.78%             | -26.90% |    -0.29 |       83 | 46.76%     | ok               |

## BND Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -6.34%   | -1.02%             | -10.09% |    -0.89 |       63 | 40.10%     | ok               |
|          30 | -6.07%   | -1.02%             | -10.80% |    -0.93 |       64 | 34.78%     | ok               |
|          25 | -6.44%   | -1.02%             | -11.16% |    -0.94 |       66 | 37.94%     | ok               |
|          15 | -8.05%   | -1.02%             | -11.42% |    -1.12 |       74 | 42.60%     | ok               |
|          40 | -6.97%   | -1.02%             | -11.70% |    -1.18 |       60 | 29.12%     | ok               |

## BONK-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 156.03%  | -83.96%            | -35.57% |     1.2  |       42 | 21.46%     | ok               |
|          15 | 100.67%  | -83.96%            | -62.48% |     0.82 |       70 | 59.96%     | ok               |
|          20 | 56.33%   | -83.96%            | -58.35% |     0.65 |       67 | 55.94%     | ok               |
|          45 | 50.70%   | -83.96%            | -47.53% |     0.64 |       66 | 27.59%     | ok               |
|          25 | 34.54%   | -83.96%            | -51.34% |     0.54 |       73 | 51.92%     | ok               |

## BTC-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 44.23%   | -20.47%            | -14.50% |     0.88 |       42 | 34.29%     | ok               |
|          45 | 39.72%   | -20.47%            | -12.20% |     0.84 |       38 | 30.46%     | ok               |
|          35 | 43.14%   | -20.47%            | -21.56% |     0.83 |       62 | 40.61%     | ok               |
|          50 | 19.19%   | -20.47%            | -20.63% |     0.51 |       36 | 25.86%     | ok               |
|          30 | 18.33%   | -20.47%            | -21.75% |     0.44 |       68 | 46.55%     | ok               |

## C Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -8.96%   | 94.86%             | -22.03% |    -0.18 |       66 | 31.28%     | ok               |
|          45 | -19.83%  | 94.86%             | -29.81% |    -0.49 |       74 | 35.44%     | ok               |
|          40 | -26.11%  | 94.86%             | -35.31% |    -0.64 |       74 | 37.60%     | ok               |
|          25 | -31.87%  | 94.86%             | -36.49% |    -0.65 |       69 | 48.42%     | ok               |
|          30 | -33.18%  | 94.86%             | -39.51% |    -0.7  |       77 | 46.26%     | ok               |

## CAT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 19.70%   | 109.48%            | -21.80% |     0.41 |       73 | 60.73%     | ok               |
|          25 | 15.35%   | 109.48%            | -21.79% |     0.36 |       66 | 50.58%     | ok               |
|          45 | 8.35%    | 109.48%            | -23.56% |     0.26 |       54 | 36.77%     | ok               |
|          30 | 7.70%    | 109.48%            | -21.87% |     0.25 |       70 | 48.25%     | ok               |
|          20 | 5.99%    | 109.48%            | -24.56% |     0.22 |       76 | 53.74%     | ok               |

## CL Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 4.75%    | 1.58%              | -12.98% |     0.24 |       42 | 22.46%     | ok               |
|          30 | 0.87%    | 1.58%              | -14.32% |     0.09 |       64 | 38.60%     | ok               |
|          45 | -1.32%   | 1.58%              | -13.13% |     0    |       48 | 25.29%     | ok               |
|          35 | -3.15%   | 1.58%              | -15.39% |    -0.05 |       64 | 34.78%     | ok               |
|          40 | -5.96%   | 1.58%              | -15.09% |    -0.18 |       58 | 29.45%     | ok               |

## CMCSA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -19.44%  | -39.37%            | -29.20% |    -0.64 |       50 | 16.64%     | ok               |
|          45 | -24.63%  | -39.37%            | -35.84% |    -0.78 |       64 | 21.30%     | ok               |
|          15 | -39.37%  | -39.37%            | -47.69% |    -0.85 |       89 | 58.07%     | ok               |
|          40 | -32.34%  | -39.37%            | -43.15% |    -0.87 |       91 | 28.79%     | ok               |
|          35 | -36.68%  | -39.37%            | -47.55% |    -0.95 |       93 | 38.44%     | ok               |

## COMP-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -1.20%   | -50.84%            | -38.71% |     0.19 |       50 | 24.90%     | ok               |
|          30 | -37.68%  | -50.84%            | -55.77% |    -0.21 |       97 | 49.81%     | ok               |
|          25 | -43.96%  | -50.84%            | -54.62% |    -0.28 |       96 | 57.85%     | ok               |
|          15 | -49.48%  | -50.84%            | -54.29% |    -0.35 |      102 | 68.97%     | ok               |
|          40 | -45.14%  | -50.84%            | -53.14% |    -0.41 |       72 | 38.31%     | ok               |

## COP Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -3.61%   | 22.09%             | -34.61% |     0.02 |       48 | 28.45%     | ok               |
|          35 | -6.04%   | 22.09%             | -42.05% |    -0.01 |       69 | 41.60%     | ok               |
|          30 | -8.79%   | 22.09%             | -41.35% |    -0.06 |       66 | 44.09%     | ok               |
|          45 | -11.19%  | 22.09%             | -41.10% |    -0.15 |       64 | 32.61%     | ok               |
|          40 | -17.83%  | 22.09%             | -47.48% |    -0.3  |       74 | 36.11%     | ok               |

## COST Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 13.91%   | 22.43%             | -24.32% |     0.46 |       62 | 47.09%     | ok               |
|          25 | 10.62%   | 22.43%             | -24.93% |     0.38 |       59 | 44.26%     | ok               |
|          35 | 4.23%    | 22.43%             | -30.16% |     0.2  |       58 | 38.60%     | ok               |
|          30 | -0.17%   | 22.43%             | -31.32% |     0.06 |       60 | 41.10%     | ok               |
|          15 | -1.53%   | 22.43%             | -27.30% |     0.03 |       67 | 50.75%     | ok               |

## CRM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | -19.79%  | -10.15%            | -32.74% |    -0.22 |       64 | 42.10%     | ok               |
|          40 | -22.80%  | -10.15%            | -38.23% |    -0.3  |       70 | 37.94%     | ok               |
|          15 | -29.49%  | -10.15%            | -47.54% |    -0.32 |       90 | 57.90%     | ok               |
|          50 | -20.66%  | -10.15%            | -38.38% |    -0.36 |       60 | 25.29%     | ok               |
|          30 | -30.80%  | -10.15%            | -44.41% |    -0.42 |       67 | 46.92%     | ok               |

## CRV-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 76.89%   | -44.60%            | -37.78% |     0.81 |       64 | 31.80%     | ok               |
|          40 | 61.13%   | -44.60%            | -38.86% |     0.73 |       52 | 27.59%     | ok               |
|          50 | 42.22%   | -44.60%            | -30.73% |     0.62 |       44 | 17.24%     | ok               |
|          45 | 43.20%   | -44.60%            | -42.29% |     0.62 |       52 | 21.26%     | ok               |
|          30 | 42.17%   | -44.60%            | -39.89% |     0.58 |       64 | 36.40%     | ok               |

## CSCO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 32.91%   | 130.12%            | -19.34% |     0.68 |       50 | 39.60%     | ok               |
|          50 | 29.01%   | 130.12%            | -19.34% |     0.62 |       48 | 38.44%     | ok               |
|          40 | 19.14%   | 130.12%            | -22.37% |     0.44 |       54 | 42.43%     | ok               |
|          35 | 17.16%   | 130.12%            | -23.68% |     0.41 |       56 | 46.42%     | ok               |
|          25 | 14.26%   | 130.12%            | -23.28% |     0.36 |       61 | 51.25%     | ok               |

## CVX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -8.81%   | 41.08%             | -23.25% |    -0.14 |       75 | 45.92%     | ok               |
|          45 | -8.91%   | 41.08%             | -28.32% |    -0.19 |       65 | 33.61%     | ok               |
|          40 | -10.09%  | 41.08%             | -26.30% |    -0.22 |       75 | 37.27%     | ok               |
|          50 | -8.80%   | 41.08%             | -30.19% |    -0.23 |       58 | 29.12%     | ok               |
|          20 | -12.47%  | 41.08%             | -25.16% |    -0.24 |       75 | 47.09%     | ok               |

## DASH-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 156.61%  | 119.49%            | -33.55% |     1.01 |       38 | 18.01%     | ok               |
|          40 | 125.75%  | 119.49%            | -33.20% |     0.89 |       42 | 24.33%     | ok               |
|          45 | 94.16%   | 119.49%            | -37.63% |     0.78 |       42 | 20.50%     | ok               |
|          30 | -0.66%   | 119.49%            | -64.43% |     0.38 |       53 | 29.89%     | ok               |
|          25 | -1.61%   | 119.49%            | -64.14% |     0.38 |       63 | 32.18%     | ok               |

## DBC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -0.09%   | 40.69%             | -26.05% |     0.07 |       77 | 41.26%     | ok               |
|          20 | -4.49%   | 40.69%             | -25.69% |    -0.08 |       69 | 39.60%     | ok               |
|          25 | -5.28%   | 40.69%             | -24.84% |    -0.11 |       66 | 37.60%     | ok               |
|          50 | -6.09%   | 40.69%             | -19.34% |    -0.18 |       50 | 24.79%     | ok               |
|          35 | -7.76%   | 40.69%             | -23.19% |    -0.2  |       66 | 34.28%     | ok               |

## DE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 2.13%    | 69.79%             | -17.97% |     0.13 |       56 | 29.62%     | ok               |
|          45 | -4.48%   | 69.79%             | -19.53% |    -0.02 |       60 | 34.11%     | ok               |
|          20 | -7.80%   | 69.79%             | -24.11% |    -0.07 |       65 | 48.59%     | ok               |
|          25 | -12.03%  | 69.79%             | -24.29% |    -0.17 |       71 | 46.92%     | ok               |
|          30 | -12.17%  | 69.79%             | -23.98% |    -0.18 |       70 | 44.26%     | ok               |

## DIA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -2.12%   | 33.54%             | -11.17% |    -0.08 |       56 | 44.59%     | ok               |
|          35 | -4.03%   | 33.54%             | -13.15% |    -0.2  |       66 | 40.10%     | ok               |
|          30 | -4.46%   | 33.54%             | -12.94% |    -0.21 |       64 | 43.26%     | ok               |
|          20 | -4.94%   | 33.54%             | -13.60% |    -0.22 |       62 | 46.59%     | ok               |
|          40 | -7.23%   | 33.54%             | -15.06% |    -0.41 |       70 | 36.77%     | ok               |

## DIS Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 34.74%   | 6.98%              | -10.17% |     1.07 |       46 | 25.62%     | ok               |
|          40 | 7.09%    | 6.98%              | -18.75% |     0.25 |       61 | 34.28%     | ok               |
|          45 | 3.48%    | 6.98%              | -16.54% |     0.17 |       47 | 29.45%     | ok               |
|          15 | -4.41%   | 6.98%              | -31.15% |     0.02 |       83 | 54.74%     | ok               |
|          35 | -4.35%   | 6.98%              | -25.70% |    -0.01 |       75 | 40.43%     | ok               |

## DOGE-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 20.64%   | -62.87%            | -56.09% |     0.44 |       73 | 64.37%     | ok               |
|          20 | 11.41%   | -62.87%            | -53.94% |     0.36 |       73 | 59.00%     | ok               |
|          25 | 3.42%    | -62.87%            | -51.74% |     0.28 |       65 | 55.17%     | ok               |
|          30 | -19.39%  | -62.87%            | -60.95% |     0.01 |       67 | 48.85%     | ok               |
|          50 | -22.02%  | -62.87%            | -54.12% |    -0.12 |       60 | 23.37%     | ok               |

## DOT-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -48.17%  | -75.00%            | -72.06% |    -0.25 |       74 | 62.26%     | ok               |
|          20 | -44.58%  | -75.00%            | -66.32% |    -0.25 |       86 | 58.24%     | ok               |
|          30 | -48.42%  | -75.00%            | -63.33% |    -0.37 |       84 | 47.70%     | ok               |
|          25 | -53.13%  | -75.00%            | -69.99% |    -0.43 |       77 | 53.26%     | ok               |
|          35 | -53.52%  | -75.00%            | -63.01% |    -0.5  |       82 | 42.15%     | ok               |

## DXY-INDEX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -0.54%   | -5.77%             | -6.02%  |    -0.07 |       38 | 32.03%     | ok               |
|          45 | -3.75%   | -5.77%             | -8.91%  |    -0.53 |       62 | 38.10%     | ok               |
|          40 | -4.12%   | -5.77%             | -8.08%  |    -0.53 |       66 | 47.84%     | ok               |
|          15 | -7.97%   | -5.77%             | -11.61% |    -0.79 |       91 | 73.16%     | ok               |
|          30 | -6.62%   | -5.77%             | -10.26% |    -0.8  |       72 | 58.01%     | ok               |

## EEM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -7.62%   | 47.37%             | -15.88% |    -0.22 |       56 | 32.11%     | ok               |
|          45 | -8.32%   | 47.37%             | -17.36% |    -0.25 |       56 | 33.78%     | ok               |
|          35 | -9.29%   | 47.37%             | -23.88% |    -0.25 |       70 | 37.94%     | ok               |
|          40 | -8.66%   | 47.37%             | -19.52% |    -0.25 |       68 | 35.94%     | ok               |
|          30 | -11.00%  | 47.37%             | -24.14% |    -0.3  |       66 | 39.93%     | ok               |

## EFA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -4.08%   | 26.97%             | -10.10% |    -0.09 |       64 | 50.92%     | ok               |
|          20 | -11.03%  | 26.97%             | -13.73% |    -0.39 |       71 | 48.09%     | ok               |
|          30 | -11.05%  | 26.97%             | -12.96% |    -0.43 |       66 | 40.77%     | ok               |
|          25 | -11.94%  | 26.97%             | -15.23% |    -0.45 |       70 | 44.26%     | ok               |
|          40 | -11.48%  | 26.97%             | -14.58% |    -0.49 |       62 | 35.94%     | ok               |

## EOG Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -13.35%  | 25.27%             | -34.41% |    -0.25 |       52 | 30.95%     | ok               |
|          40 | -19.88%  | 25.27%             | -36.53% |    -0.42 |       70 | 34.61%     | ok               |
|          50 | -19.78%  | 25.27%             | -35.63% |    -0.45 |       52 | 28.12%     | ok               |
|          30 | -24.43%  | 25.27%             | -47.50% |    -0.48 |       78 | 44.93%     | ok               |
|          35 | -24.08%  | 25.27%             | -39.34% |    -0.52 |       83 | 39.60%     | ok               |

## ETC-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -0.67%   | -57.21%            | -35.44% |     0.13 |       28 | 20.88%     | ok               |
|          50 | -0.26%   | -57.21%            | -28.33% |     0.13 |       26 | 18.01%     | ok               |
|          35 | -13.06%  | -57.21%            | -42.62% |    -0.05 |       42 | 27.97%     | ok               |
|          40 | -12.39%  | -57.21%            | -40.48% |    -0.06 |       40 | 24.14%     | ok               |
|          30 | -15.09%  | -57.21%            | -45.54% |    -0.07 |       56 | 31.99%     | ok               |

## ETH-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 148.80%  | -2.67%             | -30.11% |     1.34 |       58 | 47.13%     | ok               |
|          30 | 109.88%  | -2.67%             | -32.89% |     1.08 |       60 | 54.79%     | ok               |
|          40 | 67.59%   | -2.67%             | -33.11% |     0.88 |       62 | 39.46%     | ok               |
|          25 | 71.81%   | -2.67%             | -40.90% |     0.83 |       60 | 58.62%     | ok               |
|          50 | 41.38%   | -2.67%             | -30.50% |     0.69 |       62 | 29.31%     | ok               |

## EWJ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -22.99%  | 37.97%             | -29.40% |    -0.8  |       62 | 36.44%     | ok               |
|          20 | -23.95%  | 37.97%             | -30.00% |    -0.81 |       56 | 38.44%     | ok               |
|          25 | -25.82%  | 37.97%             | -29.85% |    -0.9  |       56 | 37.60%     | ok               |
|          15 | -27.60%  | 37.97%             | -31.15% |    -0.9  |       67 | 41.76%     | ok               |
|          45 | -23.95%  | 37.97%             | -27.68% |    -0.98 |       58 | 28.12%     | ok               |

## FCX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 2.51%    | 30.06%             | -29.27% |     0.18 |       50 | 31.61%     | ok               |
|          50 | -0.09%   | 30.06%             | -26.57% |     0.13 |       52 | 27.95%     | ok               |
|          40 | -13.45%  | 30.06%             | -42.89% |    -0.07 |       64 | 36.77%     | ok               |
|          30 | -32.07%  | 30.06%             | -46.84% |    -0.38 |       67 | 44.09%     | ok               |
|          35 | -31.91%  | 30.06%             | -50.12% |    -0.4  |       69 | 41.93%     | ok               |

## FET-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -34.42%  | -74.28%            | -59.58% |    -0.03 |       80 | 56.90%     | ok               |
|          25 | -33.25%  | -74.28%            | -65.31% |    -0.05 |       83 | 47.13%     | ok               |
|          20 | -38.69%  | -74.28%            | -65.01% |    -0.1  |       90 | 52.68%     | ok               |
|          30 | -49.02%  | -74.28%            | -65.38% |    -0.33 |       81 | 42.53%     | ok               |
|          50 | -39.06%  | -74.28%            | -45.19% |    -0.53 |       46 | 14.37%     | ok               |

## FIL-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -40.15%  | -63.20%            | -58.54% |    -0.34 |       65 | 37.16%     | ok               |
|          40 | -37.11%  | -63.20%            | -57.60% |    -0.38 |       48 | 26.63%     | ok               |
|          35 | -41.96%  | -63.20%            | -61.90% |    -0.42 |       58 | 31.23%     | ok               |
|          15 | -58.37%  | -63.20%            | -71.82% |    -0.57 |       91 | 49.04%     | ok               |
|          45 | -46.29%  | -63.20%            | -55.45% |    -0.65 |       46 | 20.31%     | ok               |

## FXI Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -4.27%   | 21.66%             | -22.57% |    -0.02 |       50 | 31.95%     | ok               |
|          30 | -4.53%   | 21.66%             | -23.91% |    -0.03 |       48 | 30.45%     | ok               |
|          15 | -5.67%   | 21.66%             | -21.68% |    -0.05 |       54 | 36.11%     | ok               |
|          20 | -7.91%   | 21.66%             | -24.53% |    -0.11 |       52 | 33.78%     | ok               |
|          35 | -8.23%   | 21.66%             | -27.53% |    -0.14 |       50 | 27.95%     | ok               |

## GDX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 4.89%    | 139.53%            | -30.40% |     0.22 |       76 | 50.25%     | ok               |
|          40 | 0.48%    | 139.53%            | -28.04% |     0.13 |       62 | 37.94%     | ok               |
|          30 | -0.37%   | 139.53%            | -33.31% |     0.13 |       62 | 44.26%     | ok               |
|          35 | -5.33%   | 139.53%            | -32.08% |     0.04 |       70 | 40.60%     | ok               |
|          25 | -8.51%   | 139.53%            | -38.90% |     0.01 |       66 | 45.92%     | ok               |

## GDXJ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -23.84%  | 135.92%            | -40.42% |    -0.18 |       74 | 50.25%     | ok               |
|          50 | -27.30%  | 135.92%            | -46.83% |    -0.36 |       60 | 34.11%     | ok               |
|          35 | -34.20%  | 135.92%            | -37.15% |    -0.44 |       72 | 40.43%     | ok               |
|          30 | -36.02%  | 135.92%            | -39.63% |    -0.46 |       72 | 43.09%     | ok               |
|          25 | -39.90%  | 135.92%            | -42.18% |    -0.51 |       77 | 46.26%     | ok               |

## GE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 4.89%    | 84.67%             | -21.25% |     0.2  |       60 | 33.78%     | ok               |
|          45 | -2.34%   | 84.67%             | -21.88% |     0.05 |       70 | 36.44%     | ok               |
|          30 | -8.43%   | 84.67%             | -27.82% |    -0.04 |       76 | 48.09%     | ok               |
|          25 | -8.86%   | 84.67%             | -29.91% |    -0.05 |       72 | 49.92%     | ok               |
|          20 | -9.37%   | 84.67%             | -25.05% |    -0.05 |       72 | 52.58%     | ok               |

## GLD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | 17.69%   | 74.02%             | -13.87% |     0.48 |       48 | 46.76%     | ok               |
|          20 | 16.09%   | 74.02%             | -13.87% |     0.44 |       49 | 48.42%     | ok               |
|          30 | 12.09%   | 74.02%             | -13.87% |     0.36 |       50 | 45.59%     | ok               |
|          35 | 8.92%    | 74.02%             | -15.09% |     0.3  |       52 | 43.09%     | ok               |
|          15 | 6.10%    | 74.02%             | -18.05% |     0.23 |       57 | 51.91%     | ok               |

## GOOGL Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 60.16%   | 95.11%             | -17.38% |     1.07 |       59 | 43.43%     | ok               |
|          30 | 56.29%   | 95.11%             | -17.54% |     1    |       57 | 46.92%     | ok               |
|          45 | 48.76%   | 95.11%             | -11.66% |     0.98 |       52 | 36.94%     | ok               |
|          25 | 53.90%   | 95.11%             | -16.87% |     0.95 |       57 | 49.42%     | ok               |
|          50 | 43.07%   | 95.11%             | -11.52% |     0.93 |       46 | 31.95%     | ok               |

## GRT-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 64.78%   | -77.44%            | -33.74% |     0.74 |       79 | 45.98%     | ok               |
|          15 | 62.89%   | -77.44%            | -36.70% |     0.7  |       69 | 62.26%     | ok               |
|          45 | 45.48%   | -77.44%            | -39.70% |     0.64 |       48 | 27.97%     | ok               |
|          20 | 46.03%   | -77.44%            | -37.63% |     0.61 |       78 | 55.56%     | ok               |
|          25 | 45.04%   | -77.44%            | -37.25% |     0.6  |       78 | 51.92%     | ok               |

## GS Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 24.72%   | 90.47%             | -20.56% |     0.53 |       68 | 56.41%     | ok               |
|          20 | 5.56%    | 90.47%             | -23.19% |     0.21 |       68 | 53.08%     | ok               |
|          40 | 3.76%    | 90.47%             | -16.16% |     0.17 |       70 | 41.76%     | ok               |
|          25 | 0.22%    | 90.47%             | -23.32% |     0.11 |       68 | 50.58%     | ok               |
|          30 | -1.97%   | 90.47%             | -21.94% |     0.06 |       70 | 48.09%     | ok               |

## HBAR-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -19.55%  | -18.64%            | -39.26% |    -0.29 |       20 | 17.84%     | ok               |
|          45 | -34.44%  | -18.64%            | -48.88% |    -0.71 |       24 | 23.79%     | ok               |
|          40 | -36.37%  | -18.64%            | -51.16% |    -0.75 |       30 | 29.74%     | ok               |
|          30 | -42.35%  | -18.64%            | -56.47% |    -0.9  |       40 | 39.03%     | ok               |
|          35 | -41.74%  | -18.64%            | -56.01% |    -0.9  |       30 | 34.57%     | ok               |

## HD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 0.85%    | -5.73%             | -17.15% |     0.1  |       69 | 43.43%     | ok               |
|          35 | -0.02%   | -5.73%             | -18.52% |     0.08 |       72 | 39.43%     | ok               |
|          40 | -0.53%   | -5.73%             | -18.05% |     0.05 |       74 | 34.78%     | ok               |
|          45 | -1.31%   | -5.73%             | -18.71% |     0.03 |       50 | 29.95%     | ok               |
|          25 | -2.23%   | -5.73%             | -18.88% |     0.02 |       68 | 45.76%     | ok               |

## HON Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -9.73%   | 6.65%              | -20.54% |    -0.24 |       68 | 32.61%     | ok               |
|          45 | -13.28%  | 6.65%              | -22.88% |    -0.33 |       70 | 37.94%     | ok               |
|          35 | -24.67%  | 6.65%              | -31.30% |    -0.63 |       91 | 49.58%     | ok               |
|          30 | -25.82%  | 6.65%              | -33.03% |    -0.64 |       91 | 54.41%     | ok               |
|          40 | -24.87%  | 6.65%              | -31.84% |    -0.66 |       78 | 42.43%     | ok               |

## HYG Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -4.84%   | 0.07%              | -7.94%  |    -0.55 |       70 | 33.94%     | ok               |
|          15 | -7.53%   | 0.07%              | -11.21% |    -0.79 |       92 | 46.92%     | ok               |
|          20 | -7.36%   | 0.07%              | -11.59% |    -0.79 |       94 | 44.76%     | ok               |
|          25 | -7.35%   | 0.07%              | -11.22% |    -0.79 |       89 | 42.10%     | ok               |
|          45 | -6.60%   | 0.07%              | -9.08%  |    -0.8  |       70 | 30.28%     | ok               |

## IBIT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 65.18%   | 21.81%             | -19.20% |     0.94 |       44 | 42.34%     | ok               |
|          50 | 52.34%   | 21.81%             | -17.37% |     0.93 |       26 | 25.40%     | ok               |
|          45 | 42.96%   | 21.81%             | -17.37% |     0.79 |       30 | 26.61%     | ok               |
|          30 | 36.51%   | 21.81%             | -18.95% |     0.67 |       40 | 34.88%     | ok               |
|          40 | 33.91%   | 21.81%             | -18.18% |     0.67 |       32 | 28.63%     | ok               |

## IBM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -18.32%  | 39.33%             | -49.43% |    -0.13 |       83 | 60.23%     | ok               |
|          35 | -21.72%  | 39.33%             | -47.10% |    -0.24 |       61 | 45.42%     | ok               |
|          30 | -24.58%  | 39.33%             | -48.94% |    -0.29 |       69 | 48.75%     | ok               |
|          20 | -30.04%  | 39.33%             | -53.45% |    -0.36 |       69 | 53.24%     | ok               |
|          45 | -26.90%  | 39.33%             | -48.72% |    -0.37 |       50 | 37.10%     | ok               |

## ICP-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -14.23%  | -44.37%            | -44.07% |     0.13 |       77 | 39.08%     | ok               |
|          35 | -11.56%  | -44.37%            | -51.30% |     0.09 |       70 | 33.33%     | ok               |
|          40 | -12.10%  | -44.37%            | -45.75% |     0.07 |       62 | 28.74%     | ok               |
|          15 | -40.07%  | -44.37%            | -59.36% |    -0.08 |       77 | 50.19%     | ok               |
|          20 | -42.22%  | -44.37%            | -62.50% |    -0.13 |       86 | 47.13%     | ok               |

## IEF Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -5.78%   | -2.47%             | -10.18% |    -0.68 |       70 | 41.76%     | ok               |
|          15 | -7.01%   | -2.47%             | -10.91% |    -0.81 |       69 | 43.43%     | ok               |
|          40 | -7.27%   | -2.47%             | -10.59% |    -1.04 |       62 | 26.96%     | ok               |
|          45 | -7.46%   | -2.47%             | -10.70% |    -1.1  |       60 | 25.12%     | ok               |
|          50 | -6.87%   | -2.47%             | -9.11%  |    -1.16 |       56 | 21.80%     | ok               |

## IEMG Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -2.98%   | 43.33%             | -13.91% |    -0.06 |       56 | 30.62%     | ok               |
|          45 | -3.77%   | 43.33%             | -14.92% |    -0.09 |       52 | 33.11%     | ok               |
|          35 | -4.63%   | 43.33%             | -21.81% |    -0.1  |       67 | 38.60%     | ok               |
|          40 | -5.25%   | 43.33%             | -18.43% |    -0.14 |       64 | 36.11%     | ok               |
|          25 | -7.31%   | 43.33%             | -23.73% |    -0.19 |       63 | 41.60%     | ok               |

## INJ-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 6.03%    | -25.52%            | -51.11% |     0.31 |       60 | 37.16%     | ok               |
|          40 | 6.66%    | -25.52%            | -44.20% |     0.3  |       50 | 33.91%     | ok               |
|          45 | -2.08%   | -25.52%            | -42.01% |     0.2  |       54 | 28.35%     | ok               |
|          30 | -27.85%  | -25.52%            | -68.17% |    -0.03 |       63 | 40.23%     | ok               |
|          15 | -32.57%  | -25.52%            | -74.15% |    -0.04 |       77 | 50.19%     | ok               |

## INTC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 70.01%   | 196.30%            | -49.32% |     0.71 |       56 | 33.78%     | ok               |
|          50 | 64.73%   | 196.30%            | -48.35% |     0.68 |       60 | 29.95%     | ok               |
|          15 | 61.16%   | 196.30%            | -53.65% |     0.63 |       76 | 59.07%     | ok               |
|          40 | 51.36%   | 196.30%            | -55.86% |     0.59 |       64 | 37.94%     | ok               |
|          25 | 51.42%   | 196.30%            | -56.41% |     0.59 |       75 | 50.42%     | ok               |

## INTU Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 20.28%   | -45.73%            | -34.35% |     0.45 |       63 | 28.29%     | ok               |
|          45 | 7.82%    | -45.73%            | -37.13% |     0.25 |       63 | 32.61%     | ok               |
|          25 | 0.84%    | -45.73%            | -35.05% |     0.15 |       70 | 49.58%     | ok               |
|          40 | 1.05%    | -45.73%            | -40.63% |     0.14 |       69 | 36.61%     | ok               |
|          35 | -0.60%   | -45.73%            | -42.78% |     0.12 |       71 | 40.60%     | ok               |

## ITA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -0.03%   | 54.72%             | -21.48% |     0.07 |       76 | 36.27%     | ok               |
|          15 | -1.76%   | 54.72%             | -28.06% |     0.05 |       83 | 60.90%     | ok               |
|          30 | -2.45%   | 54.72%             | -23.75% |     0.01 |       78 | 48.09%     | ok               |
|          40 | -5.84%   | 54.72%             | -20.54% |    -0.11 |       78 | 41.43%     | ok               |
|          35 | -6.53%   | 54.72%             | -23.12% |    -0.12 |       80 | 45.09%     | ok               |

## IWM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | 14.43%   | 32.23%             | -9.17%  |     0.55 |       54 | 34.94%     | ok               |
|          20 | 12.91%   | 32.23%             | -9.67%  |     0.49 |       60 | 35.94%     | ok               |
|          40 | 10.50%   | 32.23%             | -10.82% |     0.47 |       48 | 29.62%     | ok               |
|          35 | 8.59%    | 32.23%             | -10.82% |     0.37 |       54 | 32.11%     | ok               |
|          15 | 9.45%    | 32.23%             | -10.67% |     0.37 |       78 | 41.76%     | ok               |

## JNJ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 20.07%   | 75.78%             | -10.57% |     0.81 |       38 | 34.61%     | ok               |
|          15 | 15.04%   | 75.78%             | -17.37% |     0.54 |       56 | 53.08%     | ok               |
|          45 | 9.79%    | 75.78%             | -13.35% |     0.43 |       44 | 38.27%     | ok               |
|          30 | 10.08%   | 75.78%             | -16.86% |     0.41 |       58 | 46.59%     | ok               |
|          20 | 9.72%    | 75.78%             | -16.96% |     0.39 |       62 | 49.58%     | ok               |

## JPM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 2.12%    | 67.18%             | -15.90% |     0.13 |       52 | 32.61%     | ok               |
|          45 | -8.06%   | 67.18%             | -21.91% |    -0.2  |       56 | 35.27%     | ok               |
|          20 | -22.95%  | 67.18%             | -35.58% |    -0.51 |       88 | 48.75%     | ok               |
|          35 | -20.04%  | 67.18%             | -27.43% |    -0.58 |       76 | 41.10%     | ok               |
|          40 | -20.68%  | 67.18%             | -28.47% |    -0.62 |       68 | 37.94%     | ok               |

## KO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 27.00%   | 51.12%             | -8.64%  |     0.94 |       54 | 36.94%     | ok               |
|          35 | 22.68%   | 51.12%             | -8.21%  |     0.82 |       58 | 35.44%     | ok               |
|          40 | 19.73%   | 51.12%             | -9.28%  |     0.77 |       60 | 32.11%     | ok               |
|          25 | 20.81%   | 51.12%             | -10.16% |     0.75 |       60 | 39.60%     | ok               |
|          20 | 7.79%    | 51.12%             | -15.99% |     0.32 |       77 | 43.59%     | ok               |

## LDO-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 106.91%  | -56.36%            | -39.01% |     0.87 |       78 | 58.81%     | ok               |
|          20 | 72.91%   | -56.36%            | -40.80% |     0.74 |       79 | 54.02%     | ok               |
|          30 | 41.50%   | -56.36%            | -50.47% |     0.57 |       72 | 47.13%     | ok               |
|          25 | 22.52%   | -56.36%            | -47.32% |     0.45 |       80 | 51.53%     | ok               |
|          35 | 18.76%   | -56.36%            | -58.19% |     0.41 |       78 | 39.66%     | ok               |

## LIN Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -4.76%   | 17.10%             | -23.00% |    -0.1  |       64 | 44.43%     | ok               |
|          25 | -4.69%   | 17.10%             | -22.01% |    -0.1  |       71 | 41.43%     | ok               |
|          15 | -6.61%   | 17.10%             | -23.68% |    -0.16 |       72 | 47.75%     | ok               |
|          30 | -7.87%   | 17.10%             | -20.61% |    -0.22 |       72 | 38.60%     | ok               |
|          45 | -8.36%   | 17.10%             | -17.04% |    -0.31 |       48 | 22.13%     | ok               |

## LINK-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 56.97%   | -21.18%            | -33.64% |     0.71 |       64 | 44.44%     | ok               |
|          45 | 28.18%   | -21.18%            | -33.71% |     0.5  |       50 | 30.84%     | ok               |
|          35 | 26.72%   | -21.18%            | -34.21% |     0.48 |       58 | 40.23%     | ok               |
|          40 | 18.53%   | -21.18%            | -34.00% |     0.4  |       54 | 34.67%     | ok               |
|          25 | 9.41%    | -21.18%            | -46.32% |     0.33 |       60 | 47.89%     | ok               |

## LLY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -0.53%   | 53.53%             | -38.23% |     0.1  |       50 | 35.44%     | ok               |
|          15 | -14.57%  | 53.53%             | -48.12% |    -0.1  |       70 | 60.23%     | ok               |
|          45 | -13.64%  | 53.53%             | -42.75% |    -0.16 |       60 | 39.10%     | ok               |
|          40 | -24.61%  | 53.53%             | -46.32% |    -0.37 |       70 | 42.10%     | ok               |
|          20 | -28.21%  | 53.53%             | -52.31% |    -0.38 |       77 | 55.24%     | ok               |

## LRCX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -21.75%  | 180.25%            | -48.71% |    -0.14 |       76 | 34.11%     | ok               |
|          15 | -29.33%  | 180.25%            | -56.69% |    -0.15 |       82 | 51.41%     | ok               |
|          40 | -28.98%  | 180.25%            | -56.29% |    -0.22 |       74 | 40.27%     | ok               |
|          35 | -30.34%  | 180.25%            | -59.36% |    -0.24 |       82 | 42.43%     | ok               |
|          20 | -35.45%  | 180.25%            | -62.91% |    -0.27 |       87 | 47.25%     | ok               |

## LTC-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 18.45%   | -37.65%            | -34.94% |     0.41 |       64 | 44.64%     | ok               |
|          45 | 16.55%   | -37.65%            | -37.46% |     0.39 |       58 | 35.06%     | ok               |
|          30 | 7.48%    | -37.65%            | -30.78% |     0.29 |       67 | 51.72%     | ok               |
|          25 | 3.62%    | -37.65%            | -34.22% |     0.24 |       69 | 54.02%     | ok               |
|          40 | -3.18%   | -37.65%            | -40.31% |     0.14 |       56 | 40.23%     | ok               |

## MCD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 11.66%   | -4.29%             | -9.22%  |     0.54 |       46 | 25.12%     | ok               |
|          45 | 2.23%    | -4.29%             | -16.79% |     0.14 |       54 | 28.95%     | ok               |
|          40 | 1.34%    | -4.29%             | -18.49% |     0.11 |       65 | 32.45%     | ok               |
|          35 | -2.88%   | -4.29%             | -16.63% |    -0.06 |       67 | 37.27%     | ok               |
|          30 | -5.85%   | -4.29%             | -21.88% |    -0.17 |       79 | 40.27%     | ok               |

## META Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -10.12%  | 46.99%             | -37.54% |    -0.07 |       68 | 39.77%     | ok               |
|          40 | -16.02%  | 46.99%             | -40.90% |    -0.17 |       70 | 42.76%     | ok               |
|          50 | -20.13%  | 46.99%             | -39.33% |    -0.29 |       70 | 35.61%     | ok               |
|          30 | -28.71%  | 46.99%             | -44.90% |    -0.41 |       74 | 50.42%     | ok               |
|          25 | -30.83%  | 46.99%             | -45.70% |    -0.44 |       75 | 53.08%     | ok               |

## MPC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 29.46%   | 164.39%            | -19.02% |     0.59 |       54 | 40.60%     | ok               |
|          40 | 27.33%   | 164.39%            | -20.88% |     0.54 |       64 | 47.25%     | ok               |
|          45 | 25.10%   | 164.39%            | -20.23% |     0.52 |       60 | 44.59%     | ok               |
|          35 | 26.44%   | 164.39%            | -31.08% |     0.52 |       70 | 49.92%     | ok               |
|          30 | 20.26%   | 164.39%            | -34.29% |     0.43 |       72 | 52.58%     | ok               |

## MRK Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -13.09%  | 13.91%             | -28.39% |    -0.16 |       83 | 51.91%     | ok               |
|          25 | -13.85%  | 13.91%             | -31.07% |    -0.2  |       70 | 44.09%     | ok               |
|          20 | -18.07%  | 13.91%             | -29.34% |    -0.29 |       75 | 47.42%     | ok               |
|          50 | -14.54%  | 13.91%             | -23.01% |    -0.3  |       56 | 28.45%     | ok               |
|          45 | -16.67%  | 13.91%             | -25.38% |    -0.33 |       57 | 31.78%     | ok               |

## MS Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 4.94%    | 80.88%             | -22.02% |     0.2  |       74 | 58.24%     | ok               |
|          40 | 4.27%    | 80.88%             | -19.99% |     0.19 |       74 | 39.27%     | ok               |
|          20 | 2.45%    | 80.88%             | -25.68% |     0.15 |       75 | 53.08%     | ok               |
|          30 | -2.87%   | 80.88%             | -27.79% |     0.02 |       75 | 48.25%     | ok               |
|          25 | -4.36%   | 80.88%             | -28.36% |    -0.02 |       73 | 50.42%     | ok               |

## MSFT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -14.34%  | 23.98%             | -25.26% |    -0.32 |       74 | 37.60%     | ok               |
|          50 | -19.41%  | 23.98%             | -26.14% |    -0.5  |       66 | 31.95%     | ok               |
|          35 | -23.03%  | 23.98%             | -35.38% |    -0.5  |       75 | 46.59%     | ok               |
|          40 | -23.04%  | 23.98%             | -34.77% |    -0.52 |       73 | 41.26%     | ok               |
|          30 | -26.33%  | 23.98%             | -39.15% |    -0.56 |       83 | 51.41%     | ok               |

## MU Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 154.28%  | 582.07%            | -64.30% |     1.06 |       58 | 47.75%     | ok               |
|          15 | 170.62%  | 582.07%            | -61.96% |     1.03 |       53 | 59.23%     | ok               |
|          30 | 130.90%  | 582.07%            | -68.76% |     0.96 |       51 | 52.08%     | ok               |
|          25 | 129.55%  | 582.07%            | -67.90% |     0.95 |       51 | 53.58%     | ok               |
|          35 | 122.68%  | 582.07%            | -69.35% |     0.94 |       63 | 49.92%     | ok               |

## NEAR-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 189.00%  | 79.24%             | -38.74% |     1.3  |       28 | 22.03%     | ok               |
|          40 | 196.86%  | 79.24%             | -42.59% |     1.24 |       42 | 31.23%     | ok               |
|          30 | 172.52%  | 79.24%             | -46.60% |     1.12 |       69 | 44.06%     | ok               |
|          45 | 149.14%  | 79.24%             | -38.08% |     1.09 |       44 | 27.20%     | ok               |
|          35 | 139.03%  | 79.24%             | -52.37% |     1.04 |       64 | 35.82%     | ok               |

## NEM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -1.43%   | 178.33%            | -31.25% |     0.15 |       64 | 58.57%     | ok               |
|          20 | -2.16%   | 178.33%            | -30.50% |     0.14 |       71 | 54.08%     | ok               |
|          25 | -17.10%  | 178.33%            | -39.51% |    -0.09 |       68 | 51.75%     | ok               |
|          50 | -14.40%  | 178.33%            | -33.24% |    -0.09 |       50 | 37.77%     | ok               |
|          30 | -26.02%  | 178.33%            | -39.56% |    -0.25 |       72 | 49.92%     | ok               |

## NFLX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 29.28%   | 7.63%              | -16.28% |     0.75 |       44 | 32.78%     | ok               |
|          40 | 28.20%   | 7.63%              | -15.02% |     0.68 |       50 | 40.77%     | ok               |
|          35 | 23.83%   | 7.63%              | -18.30% |     0.57 |       74 | 45.42%     | ok               |
|          45 | 16.71%   | 7.63%              | -15.48% |     0.46 |       56 | 37.27%     | ok               |
|          15 | 3.99%    | 7.63%              | -26.59% |     0.19 |       72 | 64.89%     | ok               |

## NKE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | -16.21%  | -59.55%            | -42.13% |    -0.15 |       71 | 40.43%     | ok               |
|          20 | -23.52%  | -59.55%            | -49.34% |    -0.22 |       83 | 54.08%     | ok               |
|          25 | -26.69%  | -59.55%            | -51.20% |    -0.28 |       83 | 51.41%     | ok               |
|          15 | -28.45%  | -59.55%            | -54.28% |    -0.3  |       86 | 57.90%     | ok               |
|          40 | -20.78%  | -59.55%            | -31.79% |    -0.35 |       65 | 32.28%     | ok               |

## NOW Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 11.00%   | -0.28%             | -30.43% |     0.3  |       80 | 50.25%     | ok               |
|          20 | 8.52%    | -0.28%             | -39.71% |     0.28 |       75 | 56.57%     | ok               |
|          25 | 5.77%    | -0.28%             | -37.51% |     0.25 |       72 | 53.74%     | ok               |
|          15 | 0.58%    | -0.28%             | -43.06% |     0.19 |       83 | 59.57%     | ok               |
|          40 | 2.42%    | -0.28%             | -36.21% |     0.19 |       72 | 39.60%     | ok               |

## NVDA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -36.17%  | 93.35%             | -43.08% |    -0.55 |       78 | 44.21%     | ok               |
|          20 | -44.65%  | 93.35%             | -44.65% |    -0.63 |       78 | 52.23%     | ok               |
|          25 | -44.56%  | 93.35%             | -44.56% |    -0.69 |       79 | 47.24%     | ok               |
|          15 | -50.84%  | 93.35%             | -54.06% |    -0.74 |       79 | 55.79%     | ok               |
|          35 | -45.77%  | 93.35%             | -51.54% |    -0.82 |       88 | 41.35%     | ok               |

## OP-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 23.99%   | -81.59%            | -30.20% |     0.5  |       32 | 9.20%      | ok               |
|          45 | 3.25%    | -81.59%            | -35.75% |     0.22 |       36 | 13.98%     | ok               |
|          40 | -19.09%  | -81.59%            | -47.48% |    -0.06 |       48 | 22.22%     | ok               |
|          15 | -45.81%  | -81.59%            | -55.83% |    -0.3  |       72 | 44.25%     | ok               |
|          30 | -41.46%  | -81.59%            | -58.87% |    -0.33 |       70 | 33.14%     | ok               |

## ORCL Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 164.73%  | 4.10%              | -32.54% |     1.11 |       69 | 61.23%     | ok               |
|          25 | 112.85%  | 4.10%              | -27.76% |     0.92 |       61 | 53.74%     | ok               |
|          45 | 97.88%   | 4.10%              | -32.35% |     0.91 |       58 | 39.27%     | ok               |
|          35 | 102.78%  | 4.10%              | -31.95% |     0.9  |       62 | 47.92%     | ok               |
|          20 | 106.92%  | 4.10%              | -29.32% |     0.89 |       70 | 56.91%     | ok               |

## OXY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 4.10%    | 0.82%              | -28.48% |     0.19 |       71 | 42.76%     | ok               |
|          35 | 2.93%    | 0.82%              | -26.37% |     0.17 |       72 | 38.60%     | ok               |
|          50 | 0.64%    | 0.82%              | -26.34% |     0.12 |       46 | 27.45%     | ok               |
|          40 | -3.42%   | 0.82%              | -28.30% |     0.05 |       62 | 34.44%     | ok               |
|          25 | -10.36%  | 0.82%              | -38.51% |    -0.05 |       79 | 46.42%     | ok               |

## PEP Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 17.82%   | -22.96%            | -11.62% |     0.75 |       36 | 24.79%     | ok               |
|          45 | 10.30%   | -22.96%            | -14.22% |     0.45 |       52 | 28.79%     | ok               |
|          35 | 7.07%    | -22.96%            | -21.42% |     0.28 |       73 | 39.10%     | ok               |
|          40 | 4.76%    | -22.96%            | -18.04% |     0.23 |       66 | 34.44%     | ok               |
|          30 | 2.89%    | -22.96%            | -21.35% |     0.15 |       74 | 45.26%     | ok               |

## PEPE-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -50.17%  | -65.58%            | -61.29% |    -0.34 |       81 | 47.51%     | ok               |
|          25 | -56.58%  | -65.58%            | -64.26% |    -0.44 |       91 | 52.49%     | ok               |
|          15 | -65.38%  | -65.58%            | -65.38% |    -0.46 |       80 | 61.69%     | ok               |
|          35 | -51.85%  | -65.58%            | -61.54% |    -0.46 |       70 | 42.53%     | ok               |
|          20 | -61.99%  | -65.58%            | -63.30% |    -0.48 |       86 | 58.24%     | ok               |

## PFE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -12.42%  | 4.03%              | -22.71% |    -0.37 |       50 | 21.30%     | ok               |
|          40 | -14.06%  | 4.03%              | -26.45% |    -0.41 |       70 | 26.29%     | ok               |
|          50 | -12.91%  | 4.03%              | -24.78% |    -0.44 |       38 | 18.14%     | ok               |
|          35 | -23.00%  | 4.03%              | -32.87% |    -0.7  |       80 | 32.95%     | ok               |
|          30 | -33.11%  | 4.03%              | -41.77% |    -1.03 |       77 | 36.27%     | ok               |

## PG Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -7.73%   | -3.32%             | -17.50% |    -0.29 |       54 | 27.62%     | ok               |
|          35 | -13.22%  | -3.32%             | -18.57% |    -0.51 |       62 | 31.28%     | ok               |
|          45 | -17.17%  | -3.32%             | -19.90% |    -0.78 |       54 | 24.96%     | ok               |
|          30 | -21.11%  | -3.32%             | -24.16% |    -0.83 |       64 | 34.44%     | ok               |
|          25 | -22.95%  | -3.32%             | -25.50% |    -0.91 |       74 | 35.77%     | ok               |

## PM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | -6.54%   | 100.95%            | -33.37% |    -0.06 |       86 | 46.26%     | ok               |
|          20 | -8.98%   | 100.95%            | -34.87% |    -0.11 |       85 | 54.91%     | ok               |
|          30 | -9.47%   | 100.95%            | -36.48% |    -0.13 |       81 | 49.75%     | ok               |
|          40 | -13.67%  | 100.95%            | -38.82% |    -0.27 |       80 | 42.26%     | ok               |
|          50 | -13.22%  | 100.95%            | -35.79% |    -0.28 |       70 | 36.44%     | ok               |

## POL-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 51.91%   | -59.74%            | -38.69% |     0.68 |       79 | 49.81%     | ok               |
|          25 | 31.25%   | -59.74%            | -38.69% |     0.51 |       71 | 54.98%     | ok               |
|          20 | 23.39%   | -59.74%            | -41.66% |     0.45 |       79 | 58.43%     | ok               |
|          40 | 2.31%    | -59.74%            | -32.43% |     0.21 |       60 | 31.23%     | ok               |
|          15 | -4.07%   | -59.74%            | -46.81% |     0.2  |       84 | 62.07%     | ok               |

## QCOM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -15.78%  | -18.56%            | -54.50% |    -0.03 |       71 | 44.76%     | ok               |
|          20 | -21.98%  | -18.56%            | -54.38% |    -0.11 |       67 | 48.09%     | ok               |
|          35 | -22.89%  | -18.56%            | -50.58% |    -0.15 |       79 | 40.43%     | ok               |
|          15 | -31.40%  | -18.56%            | -57.94% |    -0.25 |       69 | 50.75%     | ok               |
|          30 | -31.89%  | -18.56%            | -56.59% |    -0.3  |       77 | 42.93%     | ok               |

## QQQ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 20.85%   | 56.27%             | -14.17% |     0.54 |       63 | 53.74%     | ok               |
|          25 | 12.79%   | 56.27%             | -12.88% |     0.39 |       61 | 47.59%     | ok               |
|          20 | 11.64%   | 56.27%             | -12.98% |     0.36 |       69 | 50.25%     | ok               |
|          30 | 5.57%    | 56.27%             | -13.88% |     0.22 |       68 | 45.42%     | ok               |
|          35 | -5.28%   | 56.27%             | -20.29% |    -0.07 |       74 | 41.60%     | ok               |

## RENDER-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 27.03%   | -59.76%            | -44.59% |     0.49 |       82 | 61.69%     | ok               |
|          20 | 24.34%   | -59.76%            | -43.43% |     0.47 |       85 | 58.43%     | ok               |
|          25 | 18.59%   | -59.76%            | -41.13% |     0.43 |       85 | 53.45%     | ok               |
|          30 | -21.39%  | -59.76%            | -44.65% |     0.05 |       90 | 47.51%     | ok               |
|          35 | -32.26%  | -59.76%            | -46.00% |    -0.14 |       86 | 41.00%     | ok               |

## RTX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 36.25%   | 82.06%             | -18.66% |     0.77 |       75 | 57.24%     | ok               |
|          25 | 31.60%   | 82.06%             | -18.59% |     0.7  |       63 | 54.58%     | ok               |
|          30 | 26.61%   | 82.06%             | -16.99% |     0.63 |       68 | 51.75%     | ok               |
|          15 | 28.02%   | 82.06%             | -19.55% |     0.63 |       68 | 61.73%     | ok               |
|          35 | 21.52%   | 82.06%             | -18.00% |     0.58 |       60 | 48.42%     | ok               |

## SBUX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -3.37%   | 26.32%             | -23.55% |     0.03 |       55 | 40.60%     | ok               |
|          40 | -4.35%   | 26.32%             | -25.43% |    -0.02 |       60 | 32.28%     | ok               |
|          45 | -6.16%   | 26.32%             | -27.26% |    -0.08 |       66 | 27.45%     | ok               |
|          35 | -8.64%   | 26.32%             | -26.54% |    -0.1  |       58 | 35.44%     | ok               |
|          20 | -14.89%  | 26.32%             | -30.94% |    -0.2  |       58 | 42.60%     | ok               |

## SCHW Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | 1.15%    | 26.54%             | -28.76% |     0.12 |       67 | 48.92%     | ok               |
|          20 | -0.09%   | 26.54%             | -29.24% |     0.09 |       75 | 51.25%     | ok               |
|          45 | -2.78%   | 26.54%             | -16.53% |    -0.02 |       60 | 30.62%     | ok               |
|          50 | -4.01%   | 26.54%             | -13.28% |    -0.09 |       52 | 27.62%     | ok               |
|          15 | -9.65%   | 26.54%             | -31.37% |    -0.13 |       85 | 55.91%     | ok               |

## SHIB-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -20.85%  | -64.64%            | -45.04% |    -0.05 |       84 | 66.67%     | ok               |
|          35 | -18.47%  | -64.64%            | -44.56% |    -0.07 |       69 | 46.93%     | ok               |
|          40 | -19.46%  | -64.64%            | -41.14% |    -0.11 |       60 | 38.89%     | ok               |
|          20 | -24.93%  | -64.64%            | -47.68% |    -0.12 |       76 | 61.88%     | ok               |
|          25 | -25.17%  | -64.64%            | -45.06% |    -0.13 |       78 | 58.43%     | ok               |

## SHY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd    |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:-------|---------:|---------:|:-----------|:-----------------|
|          30 | -1.87%   | 0.01%              | -3.30% |    -0.63 |       48 | 36.94%     | ok               |
|          35 | -2.39%   | 0.01%              | -3.61% |    -0.82 |       52 | 35.27%     | ok               |
|          40 | -2.41%   | 0.01%              | -3.58% |    -0.83 |       54 | 33.94%     | ok               |
|          45 | -2.43%   | 0.01%              | -3.43% |    -0.89 |       54 | 28.45%     | ok               |
|          50 | -2.67%   | 0.01%              | -3.40% |    -1.03 |       48 | 24.79%     | ok               |

## SKY-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | -54.48%  | 0.46%              | -59.64% |    -0.86 |       78 | 35.63%     | ok               |
|          30 | -57.99%  | 0.46%              | -61.82% |    -0.9  |       85 | 43.30%     | ok               |
|          15 | -64.35%  | 0.46%              | -64.95% |    -0.95 |       79 | 53.45%     | ok               |
|          25 | -62.38%  | 0.46%              | -65.07% |    -1    |       78 | 46.55%     | ok               |
|          40 | -60.28%  | 0.46%              | -62.94% |    -1.1  |       66 | 32.18%     | ok               |

## SLB Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -0.99%   | 5.50%              | -28.36% |     0.09 |       50 | 35.44%     | ok               |
|          45 | -1.23%   | 5.50%              | -25.01% |     0.08 |       60 | 31.95%     | ok               |
|          50 | -4.69%   | 5.50%              | -26.78% |    -0.02 |       50 | 25.62%     | ok               |
|          35 | -26.24%  | 5.50%              | -48.21% |    -0.46 |       72 | 43.26%     | ok               |
|          25 | -35.85%  | 5.50%              | -55.67% |    -0.64 |       84 | 53.08%     | ok               |

## SLV Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 41.52%   | 76.27%             | -33.88% |     0.64 |       54 | 30.12%     | ok               |
|          45 | 29.50%   | 76.27%             | -31.59% |     0.52 |       65 | 31.61%     | ok               |
|          40 | 28.48%   | 76.27%             | -34.28% |     0.5  |       69 | 33.61%     | ok               |
|          20 | 17.95%   | 76.27%             | -42.46% |     0.39 |       72 | 43.93%     | ok               |
|          15 | 17.94%   | 76.27%             | -47.98% |     0.38 |       73 | 48.75%     | ok               |

## SMH Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 58.74%   | 119.53%            | -31.01% |     0.87 |       47 | 46.09%     | ok               |
|          25 | 44.39%   | 119.53%            | -32.94% |     0.74 |       44 | 44.59%     | ok               |
|          35 | 42.14%   | 119.53%            | -34.36% |     0.72 |       56 | 41.43%     | ok               |
|          30 | 39.75%   | 119.53%            | -33.99% |     0.69 |       50 | 43.09%     | ok               |
|          45 | 28.35%   | 119.53%            | -33.68% |     0.58 |       56 | 35.77%     | ok               |

## SNX-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 9.01%    | -72.37%            | -41.29% |     0.31 |       56 | 28.16%     | ok               |
|          20 | 6.61%    | -72.37%            | -53.03% |     0.31 |       73 | 43.87%     | ok               |
|          40 | 3.21%    | -72.37%            | -36.00% |     0.21 |       46 | 22.80%     | ok               |
|          30 | -5.59%   | -72.37%            | -50.74% |     0.15 |       62 | 34.29%     | ok               |
|          15 | -22.96%  | -72.37%            | -54.74% |    -0    |       79 | 48.47%     | ok               |

## SOL-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 36.61%   | -36.67%            | -39.74% |     0.58 |       60 | 39.08%     | ok               |
|          35 | 13.77%   | -36.67%            | -43.70% |     0.36 |       74 | 45.59%     | ok               |
|          45 | 11.43%   | -36.67%            | -46.83% |     0.33 |       58 | 33.72%     | ok               |
|          15 | 1.35%    | -36.67%            | -46.84% |     0.25 |       72 | 63.98%     | ok               |
|          50 | 0.21%    | -36.67%            | -46.56% |     0.17 |       58 | 27.97%     | ok               |

## SOXX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | 57.08%   | 106.90%            | -39.65% |     0.83 |       54 | 44.76%     | ok               |
|          35 | 54.38%   | 106.90%            | -38.76% |     0.82 |       56 | 40.10%     | ok               |
|          30 | 52.71%   | 106.90%            | -40.14% |     0.79 |       56 | 42.60%     | ok               |
|          20 | 45.22%   | 106.90%            | -38.67% |     0.7  |       59 | 45.59%     | ok               |
|          40 | 35.49%   | 106.90%            | -41.03% |     0.62 |       58 | 37.94%     | ok               |

## SPY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 11.02%   | 44.67%             | -14.25% |     0.41 |       59 | 52.58%     | ok               |
|          15 | 10.48%   | 44.67%             | -16.80% |     0.39 |       63 | 55.24%     | ok               |
|          25 | 6.02%    | 44.67%             | -14.25% |     0.26 |       59 | 51.58%     | ok               |
|          30 | -0.13%   | 44.67%             | -15.53% |     0.06 |       64 | 48.92%     | ok               |
|          35 | -1.09%   | 44.67%             | -15.58% |     0.02 |       62 | 45.76%     | ok               |

## SUSHI-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -0.40%   | -68.66%            | -34.75% |     0.16 |       52 | 16.48%     | ok               |
|          40 | -40.62%  | -68.66%            | -60.82% |    -0.41 |       59 | 28.54%     | ok               |
|          45 | -38.89%  | -68.66%            | -57.99% |    -0.44 |       56 | 21.46%     | ok               |
|          35 | -53.54%  | -68.66%            | -67.69% |    -0.62 |       80 | 33.52%     | ok               |
|          15 | -72.15%  | -68.66%            | -78.43% |    -0.89 |       89 | 49.81%     | ok               |

## T Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 65.71%   | 34.34%             | -15.08% |     1.09 |       73 | 65.56%     | ok               |
|          20 | 61.62%   | 34.34%             | -18.13% |     1.07 |       68 | 61.06%     | ok               |
|          25 | 59.78%   | 34.34%             | -17.66% |     1.06 |       68 | 58.90%     | ok               |
|          30 | 44.91%   | 34.34%             | -17.01% |     0.88 |       72 | 56.74%     | ok               |
|          35 | 29.12%   | 34.34%             | -14.49% |     0.65 |       78 | 52.41%     | ok               |

## TGT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -11.06%  | 4.21%              | -34.42% |    -0.16 |       60 | 37.60%     | ok               |
|          45 | -11.97%  | 4.21%              | -25.85% |    -0.23 |       48 | 28.62%     | ok               |
|          20 | -16.69%  | 4.21%              | -38.96% |    -0.25 |       88 | 45.42%     | ok               |
|          25 | -15.22%  | 4.21%              | -37.81% |    -0.25 |       70 | 40.77%     | ok               |
|          35 | -17.42%  | 4.21%              | -32.35% |    -0.35 |       60 | 33.94%     | ok               |

## TIA-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -15.84%  | -75.91%            | -66.82% |     0.21 |       94 | 58.43%     | ok               |
|          25 | -14.21%  | -75.91%            | -69.36% |     0.18 |       90 | 48.28%     | ok               |
|          35 | -9.22%   | -75.91%            | -66.58% |     0.15 |       76 | 36.40%     | ok               |
|          20 | -28.65%  | -75.91%            | -71.57% |     0.06 |       90 | 53.45%     | ok               |
|          30 | -36.08%  | -75.91%            | -74.53% |    -0.07 |       91 | 43.30%     | ok               |

## TLT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -7.38%   | -11.78%            | -12.51% |    -0.81 |       32 | 17.30%     | ok               |
|          40 | -12.73%  | -11.78%            | -17.65% |    -1.11 |       50 | 24.96%     | ok               |
|          45 | -11.31%  | -11.78%            | -15.17% |    -1.17 |       42 | 20.47%     | ok               |
|          30 | -18.66%  | -11.78%            | -21.85% |    -1.41 |       66 | 33.28%     | ok               |
|          35 | -18.49%  | -11.78%            | -21.03% |    -1.54 |       62 | 28.79%     | ok               |

## TMO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 53.28%   | 18.65%             | -8.17%  |     1.11 |       48 | 34.94%     | ok               |
|          45 | 50.35%   | 18.65%             | -9.69%  |     1.02 |       54 | 39.77%     | ok               |
|          40 | 43.73%   | 18.65%             | -10.78% |     0.89 |       59 | 44.76%     | ok               |
|          35 | 45.27%   | 18.65%             | -13.84% |     0.86 |       69 | 50.42%     | ok               |
|          20 | 39.67%   | 18.65%             | -22.89% |     0.73 |       76 | 61.56%     | ok               |

## TMUS Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -2.98%   | -6.71%             | -33.01% |     0.04 |       74 | 48.42%     | ok               |
|          15 | -8.70%   | -6.71%             | -41.03% |    -0.07 |       68 | 61.06%     | ok               |
|          50 | -7.84%   | -6.71%             | -32.38% |    -0.14 |       60 | 34.44%     | ok               |
|          25 | -12.22%  | -6.71%             | -39.27% |    -0.17 |       77 | 51.41%     | ok               |
|          20 | -13.96%  | -6.71%             | -39.78% |    -0.2  |       74 | 55.41%     | ok               |

## TRX-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 11.33%   | 22.86%             | -18.79% |     0.42 |       54 | 38.70%     | ok               |
|          35 | 4.79%    | 22.86%             | -21.77% |     0.22 |       66 | 46.93%     | ok               |
|          20 | 2.34%    | 22.86%             | -25.45% |     0.15 |       61 | 56.70%     | ok               |
|          30 | 2.27%    | 22.86%             | -22.90% |     0.15 |       66 | 49.81%     | ok               |
|          45 | 1.55%    | 22.86%             | -22.76% |     0.12 |       46 | 35.06%     | ok               |

## TSLA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 34.46%   | 108.24%            | -34.01% |     0.54 |       66 | 29.95%     | ok               |
|          40 | 8.08%    | 108.24%            | -52.58% |     0.28 |       65 | 35.44%     | ok               |
|          45 | -14.96%  | 108.24%            | -54.39% |     0.01 |       71 | 32.45%     | ok               |
|          35 | -20.51%  | 108.24%            | -60.12% |    -0.03 |       76 | 38.10%     | ok               |
|          30 | -35.00%  | 108.24%            | -59.64% |    -0.22 |       78 | 42.76%     | ok               |

## TXN Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 5.75%    | 38.35%             | -43.95% |     0.22 |       68 | 32.28%     | ok               |
|          35 | -14.12%  | 38.35%             | -42.26% |    -0.1  |       78 | 46.92%     | ok               |
|          40 | -15.62%  | 38.35%             | -44.70% |    -0.13 |       74 | 44.59%     | ok               |
|          20 | -20.24%  | 38.35%             | -37.39% |    -0.15 |       68 | 56.74%     | ok               |
|          45 | -16.26%  | 38.35%             | -45.28% |    -0.15 |       82 | 38.27%     | ok               |

## UNH Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 35.49%   | -19.22%            | -36.92% |     0.61 |       54 | 28.62%     | ok               |
|          30 | 36.02%   | -19.22%            | -26.31% |     0.58 |       75 | 48.42%     | ok               |
|          35 | 31.88%   | -19.22%            | -27.21% |     0.54 |       70 | 43.43%     | ok               |
|          20 | 31.70%   | -19.22%            | -26.96% |     0.53 |       78 | 57.74%     | ok               |
|          15 | 31.66%   | -19.22%            | -26.07% |     0.52 |       83 | 63.89%     | ok               |

## UNI-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 108.39%  | 26.89%             | -21.42% |     1.04 |       46 | 26.05%     | ok               |
|          45 | 85.00%   | 26.89%             | -30.17% |     0.87 |       54 | 33.33%     | ok               |
|          40 | 60.77%   | 26.89%             | -43.84% |     0.72 |       58 | 38.51%     | ok               |
|          35 | 37.16%   | 26.89%             | -50.47% |     0.55 |       66 | 43.87%     | ok               |
|          20 | -29.03%  | 26.89%             | -69.70% |     0.03 |       92 | 59.00%     | ok               |

## UPS Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | -28.48%  | -29.16%            | -30.91% |    -0.53 |       62 | 35.94%     | ok               |
|          40 | -29.43%  | -29.16%            | -32.06% |    -0.57 |       58 | 30.78%     | ok               |
|          20 | -36.27%  | -29.16%            | -37.68% |    -0.69 |       84 | 50.08%     | ok               |
|          25 | -36.78%  | -29.16%            | -38.18% |    -0.72 |       76 | 46.76%     | ok               |
|          15 | -38.52%  | -29.16%            | -39.89% |    -0.74 |       86 | 53.91%     | ok               |

## USO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 6.59%    | 107.07%            | -41.37% |     0.24 |       67 | 41.10%     | ok               |
|          20 | 5.72%    | 107.07%            | -42.76% |     0.23 |       72 | 37.60%     | ok               |
|          45 | 5.79%    | 107.07%            | -33.44% |     0.22 |       48 | 25.79%     | ok               |
|          25 | -4.18%   | 107.07%            | -45.06% |     0.08 |       68 | 35.27%     | ok               |
|          50 | -3.42%   | 107.07%            | -29.54% |     0.07 |       52 | 24.13%     | ok               |

## VEA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 8.05%    | 36.80%             | -15.99% |     0.34 |       54 | 50.08%     | ok               |
|          20 | 1.76%    | 36.80%             | -17.04% |     0.12 |       59 | 47.42%     | ok               |
|          25 | -2.12%   | 36.80%             | -17.13% |    -0.03 |       57 | 45.42%     | ok               |
|          30 | -3.64%   | 36.80%             | -17.27% |    -0.1  |       64 | 42.26%     | ok               |
|          35 | -4.71%   | 36.80%             | -16.11% |    -0.15 |       52 | 40.10%     | ok               |

## VIXY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -56.24%  | -62.76%            | -69.78% |    -0.67 |       36 | 8.82%      | ok               |
|          15 | -77.50%  | -62.76%            | -89.47% |    -0.81 |       95 | 42.76%     | ok               |
|          45 | -65.63%  | -62.76%            | -75.03% |    -0.87 |       56 | 13.81%     | ok               |
|          30 | -78.16%  | -62.76%            | -88.17% |    -0.94 |       94 | 31.78%     | ok               |
|          40 | -73.03%  | -62.76%            | -80.72% |    -1    |       68 | 17.64%     | ok               |

## VNQ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -7.58%   | 11.55%             | -19.07% |    -0.33 |       60 | 28.12%     | ok               |
|          50 | -8.50%   | 11.55%             | -17.13% |    -0.39 |       52 | 24.79%     | ok               |
|          25 | -10.91%  | 11.55%             | -22.34% |    -0.4  |       69 | 42.60%     | ok               |
|          40 | -12.47%  | 11.55%             | -24.84% |    -0.54 |       78 | 33.61%     | ok               |
|          30 | -13.66%  | 11.55%             | -24.92% |    -0.54 |       73 | 39.77%     | ok               |

## VTI Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 12.08%   | 43.41%             | -13.96% |     0.45 |       62 | 53.08%     | ok               |
|          15 | 7.47%    | 43.41%             | -15.70% |     0.3  |       59 | 55.41%     | ok               |
|          25 | 0.12%    | 43.41%             | -15.00% |     0.07 |       58 | 50.92%     | ok               |
|          30 | -7.39%   | 43.41%             | -17.64% |    -0.21 |       68 | 48.92%     | ok               |
|          40 | -8.50%   | 43.41%             | -19.77% |    -0.28 |       72 | 41.43%     | ok               |

## VWO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -9.25%   | 31.65%             | -21.68% |    -0.35 |       56 | 27.95%     | ok               |
|          15 | -12.95%  | 31.65%             | -24.01% |    -0.41 |       74 | 46.09%     | ok               |
|          45 | -11.02%  | 31.65%             | -23.75% |    -0.42 |       58 | 30.45%     | ok               |
|          40 | -11.48%  | 31.65%             | -23.57% |    -0.43 |       68 | 33.28%     | ok               |
|          20 | -14.34%  | 31.65%             | -26.14% |    -0.48 |       71 | 43.76%     | ok               |

## VZ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -3.10%   | 12.17%             | -12.96% |    -0.04 |       56 | 28.62%     | ok               |
|          20 | -21.81%  | 12.17%             | -35.02% |    -0.43 |       78 | 51.58%     | ok               |
|          25 | -18.62%  | 12.17%             | -25.46% |    -0.48 |       81 | 46.59%     | ok               |
|          35 | -17.16%  | 12.17%             | -26.48% |    -0.49 |       62 | 38.77%     | ok               |
|          45 | -17.84%  | 12.17%             | -25.53% |    -0.54 |       70 | 32.78%     | ok               |

## WFC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | -8.30%   | 37.53%             | -21.57% |    -0.11 |       77 | 43.59%     | ok               |
|          50 | -6.21%   | 37.53%             | -18.29% |    -0.13 |       58 | 32.61%     | ok               |
|          40 | -13.97%  | 37.53%             | -23.94% |    -0.34 |       72 | 40.27%     | ok               |
|          30 | -19.91%  | 37.53%             | -28.90% |    -0.34 |       82 | 46.92%     | ok               |
|          20 | -22.85%  | 37.53%             | -29.87% |    -0.37 |       81 | 52.75%     | ok               |

## WIF-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 16.24%   | -78.31%            | -40.67% |     0.4  |       67 | 44.83%     | ok               |
|          15 | -9.16%   | -78.31%            | -46.21% |     0.2  |       77 | 48.08%     | ok               |
|          25 | -9.38%   | -78.31%            | -44.74% |     0.19 |       65 | 41.00%     | ok               |
|          50 | -9.09%   | -78.31%            | -35.47% |     0.01 |       38 | 13.60%     | ok               |
|          30 | -28.69%  | -78.31%            | -52.76% |    -0.04 |       66 | 38.31%     | ok               |

## WMT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 36.14%   | 82.50%             | -12.18% |     1.1  |       36 | 36.61%     | ok               |
|          45 | 35.00%   | 82.50%             | -14.14% |     1.02 |       42 | 38.94%     | ok               |
|          35 | 25.15%   | 82.50%             | -18.25% |     0.74 |       58 | 45.26%     | ok               |
|          40 | 23.54%   | 82.50%             | -18.53% |     0.72 |       50 | 40.60%     | ok               |
|          15 | 6.78%    | 82.50%             | -26.24% |     0.24 |       82 | 59.23%     | ok               |

## XBI Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 13.65%   | 65.89%             | -16.08% |     0.41 |       52 | 34.11%     | ok               |
|          45 | 9.33%    | 65.89%             | -15.46% |     0.31 |       50 | 31.61%     | ok               |
|          35 | 2.68%    | 65.89%             | -17.66% |     0.15 |       60 | 36.94%     | ok               |
|          30 | 0.54%    | 65.89%             | -17.66% |     0.1  |       62 | 38.44%     | ok               |
|          50 | 0.10%    | 65.89%             | -15.41% |     0.08 |       50 | 28.62%     | ok               |

## XLB Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -0.95%   | 11.97%             | -15.73% |     0.01 |       38 | 21.96%     | ok               |
|          40 | -1.86%   | 11.97%             | -17.29% |    -0.02 |       54 | 26.12%     | ok               |
|          45 | -4.49%   | 11.97%             | -17.09% |    -0.14 |       42 | 23.63%     | ok               |
|          35 | -6.07%   | 11.97%             | -20.65% |    -0.18 |       56 | 29.45%     | ok               |
|          25 | -10.44%  | 11.97%             | -22.28% |    -0.34 |       64 | 35.61%     | ok               |

## XLC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 12.28%   | 32.49%             | -12.33% |     0.46 |       61 | 49.75%     | ok               |
|          25 | 11.73%   | 32.49%             | -12.31% |     0.44 |       60 | 51.91%     | ok               |
|          20 | 11.11%   | 32.49%             | -11.04% |     0.41 |       63 | 54.41%     | ok               |
|          50 | 6.91%    | 32.49%             | -11.12% |     0.36 |       64 | 37.94%     | ok               |
|          40 | 7.48%    | 32.49%             | -13.38% |     0.33 |       62 | 43.43%     | ok               |

## XLE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 2.05%    | 46.90%             | -25.98% |     0.13 |       56 | 37.10%     | ok               |
|          35 | -0.53%   | 46.90%             | -27.11% |     0.07 |       65 | 43.93%     | ok               |
|          30 | -1.86%   | 46.90%             | -29.67% |     0.04 |       69 | 45.92%     | ok               |
|          45 | -1.61%   | 46.90%             | -28.46% |     0.03 |       60 | 39.43%     | ok               |
|          25 | -6.49%   | 46.90%             | -32.98% |    -0.07 |       79 | 49.08%     | ok               |

## XLF Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -0.98%   | 33.80%             | -18.63% |     0.03 |       74 | 51.58%     | ok               |
|          15 | -1.19%   | 33.80%             | -20.19% |     0.02 |       78 | 54.58%     | ok               |
|          25 | -7.89%   | 33.80%             | -23.22% |    -0.23 |       81 | 48.42%     | ok               |
|          30 | -8.49%   | 33.80%             | -23.61% |    -0.26 |       82 | 46.42%     | ok               |
|          35 | -15.61%  | 33.80%             | -24.48% |    -0.6  |       72 | 42.76%     | ok               |

## XLI Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 5.22%    | 35.58%             | -11.40% |     0.23 |       86 | 51.41%     | ok               |
|          20 | 1.42%    | 35.58%             | -12.74% |     0.11 |       75 | 46.42%     | ok               |
|          50 | -4.76%   | 35.58%             | -14.94% |    -0.18 |       60 | 31.78%     | ok               |
|          45 | -5.38%   | 35.58%             | -16.29% |    -0.19 |       70 | 34.28%     | ok               |
|          25 | -8.78%   | 35.58%             | -17.03% |    -0.29 |       78 | 44.43%     | ok               |

## XLK Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 67.47%   | 72.11%             | -14.75% |     1.12 |       45 | 51.41%     | ok               |
|          20 | 61.07%   | 72.11%             | -14.75% |     1.08 |       48 | 49.08%     | ok               |
|          25 | 55.43%   | 72.11%             | -14.75% |     1.04 |       44 | 47.09%     | ok               |
|          30 | 46.12%   | 72.11%             | -14.75% |     0.93 |       44 | 45.76%     | ok               |
|          35 | 29.82%   | 72.11%             | -14.71% |     0.69 |       56 | 43.09%     | ok               |

## XLM-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | 16.93%   | -37.94%            | -49.14% |     0.39 |       68 | 49.62%     | ok               |
|          40 | 10.64%   | -37.94%            | -47.28% |     0.32 |       50 | 36.78%     | ok               |
|          50 | 9.13%    | -37.94%            | -48.81% |     0.29 |       42 | 25.86%     | ok               |
|          30 | 6.68%    | -37.94%            | -54.58% |     0.29 |       66 | 47.51%     | ok               |
|          45 | 5.57%    | -37.94%            | -51.28% |     0.26 |       54 | 31.03%     | ok               |

## XLP Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 15.93%   | 14.00%             | -5.66%  |     0.95 |       50 | 29.62%     | ok               |
|          40 | 13.23%   | 14.00%             | -7.77%  |     0.77 |       68 | 33.61%     | ok               |
|          50 | 12.04%   | 14.00%             | -6.08%  |     0.76 |       56 | 27.29%     | ok               |
|          35 | 12.25%   | 14.00%             | -9.73%  |     0.71 |       64 | 36.61%     | ok               |
|          30 | 9.00%    | 14.00%             | -10.28% |     0.52 |       65 | 38.44%     | ok               |

## XLU Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 6.11%    | 15.81%             | -14.03% |     0.34 |       54 | 29.78%     | ok               |
|          45 | 4.95%    | 15.81%             | -14.97% |     0.28 |       58 | 30.95%     | ok               |
|          40 | 1.89%    | 15.81%             | -16.41% |     0.13 |       64 | 32.95%     | ok               |
|          35 | -0.82%   | 15.81%             | -19.71% |     0.01 |       64 | 35.61%     | ok               |
|          30 | -5.11%   | 15.81%             | -20.40% |    -0.18 |       69 | 39.10%     | ok               |

## XLV Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -19.81%  | 23.12%             | -22.19% |    -0.93 |       74 | 38.10%     | ok               |
|          30 | -20.17%  | 23.12%             | -22.55% |    -0.96 |       74 | 36.44%     | ok               |
|          15 | -23.37%  | 23.12%             | -24.70% |    -1.08 |       83 | 42.10%     | ok               |
|          20 | -23.00%  | 23.12%             | -24.34% |    -1.09 |       79 | 39.77%     | ok               |
|          35 | -24.19%  | 23.12%             | -26.43% |    -1.25 |       70 | 33.44%     | ok               |

## XLY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -0.70%   | 30.73%             | -15.77% |     0.06 |       76 | 54.24%     | ok               |
|          30 | -4.15%   | 30.73%             | -18.35% |    -0.06 |       75 | 47.59%     | ok               |
|          20 | -5.95%   | 30.73%             | -19.25% |    -0.1  |       72 | 50.92%     | ok               |
|          25 | -8.05%   | 30.73%             | -19.98% |    -0.17 |       69 | 49.42%     | ok               |
|          50 | -6.34%   | 30.73%             | -15.82% |    -0.22 |       62 | 32.11%     | ok               |

## XOM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | 4.81%    | 55.22%             | -19.90% |     0.2  |       57 | 35.27%     | ok               |
|          50 | 3.99%    | 55.22%             | -21.35% |     0.19 |       40 | 27.45%     | ok               |
|          30 | 3.77%    | 55.22%             | -20.29% |     0.18 |       57 | 34.61%     | ok               |
|          20 | -1.15%   | 55.22%             | -25.56% |     0.05 |       64 | 37.60%     | ok               |
|          45 | -1.20%   | 55.22%             | -23.33% |     0.04 |       44 | 28.62%     | ok               |

## XRP-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 29.07%   | -44.58%            | -31.38% |     0.51 |       72 | 42.91%     | ok               |
|          40 | 9.02%    | -44.58%            | -33.91% |     0.3  |       66 | 36.40%     | ok               |
|          30 | -3.52%   | -44.58%            | -31.82% |     0.16 |       67 | 47.89%     | ok               |
|          45 | -3.46%   | -44.58%            | -37.18% |     0.14 |       60 | 30.84%     | ok               |
|          50 | -7.56%   | -44.58%            | -39.26% |     0.06 |       58 | 23.18%     | ok               |

## YFI-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -43.33%  | -60.24%            | -43.72% |    -0.71 |       56 | 26.82%     | ok               |
|          45 | -41.84%  | -60.24%            | -42.24% |    -0.84 |       68 | 22.22%     | ok               |
|          35 | -52.82%  | -60.24%            | -53.15% |    -0.92 |       62 | 33.33%     | ok               |
|          30 | -58.98%  | -60.24%            | -60.97% |    -1.07 |       76 | 37.36%     | ok               |
|          50 | -46.53%  | -60.24%            | -46.53% |    -1.09 |       52 | 16.48%     | ok               |

## ZEC-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 217.39%  | 2740.74%           | -30.64% |     1.11 |       44 | 31.42%     | ok               |
|          35 | 175.22%  | 2740.74%           | -50.84% |     1    |       52 | 36.97%     | ok               |
|          30 | 160.76%  | 2740.74%           | -56.50% |     0.95 |       57 | 40.42%     | ok               |
|          25 | 153.33%  | 2740.74%           | -58.07% |     0.93 |       55 | 43.10%     | ok               |
|          40 | 133.40%  | 2740.74%           | -54.22% |     0.89 |       52 | 34.87%     | ok               |
