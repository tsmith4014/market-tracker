# Market Tracker Backtest Report

_Generated: 2026-11-24T09:57:55+00:00_

## Data Sources

- Crypto: Kraken -> Coinbase -> CoinGecko OHLC -> CoinPaprika fallback chain.
- Stocks / ETFs / indices: Stooq -> Yahoo Finance fallback chain.
- Data rows are generated from real market APIs. Mock OHLCV rows are not generated.

## Data Freshness

- Rows: **92,808**
- Symbols: **161**
- Date range: **2024-07-03** to **2026-11-24**

## Latest Signals

| symbol     | date                |         close |   composite_score | signal   | data_source   |
|:-----------|:--------------------|--------------:|------------------:|:---------|:--------------|
| AGG        | 2026-11-23 00:00:00 |    96.24      |          30.3333  | LONG     | Yahoo Finance |
| BND        | 2026-11-23 00:00:00 |    71.36      |          30.3333  | LONG     | Yahoo Finance |
| CL         | 2026-11-23 00:00:00 |    97.93      |          36.8333  | LONG     | Yahoo Finance |
| COST       | 2026-11-23 00:00:00 |  1097.91      |          46.75    | LONG     | Yahoo Finance |
| DIS        | 2026-11-23 00:00:00 |   120.27      |          58.5833  | LONG     | Yahoo Finance |
| DXY-INDEX  | 2026-11-24 00:00:00 |   104.255     |          82.2581  | LONG     | Yahoo Finance |
| GE         | 2026-11-23 00:00:00 |   321.26      |          32.8333  | LONG     | Yahoo Finance |
| HD         | 2026-11-23 00:00:00 |   346.06      |          56.25    | LONG     | Yahoo Finance |
| MCD        | 2026-11-23 00:00:00 |   276.38      |          41.5     | LONG     | Yahoo Finance |
| PG         | 2026-11-23 00:00:00 |   169.6       |          57.0833  | LONG     | Yahoo Finance |
| SBUX       | 2026-11-23 00:00:00 |   106.36      |          36.5833  | LONG     | Yahoo Finance |
| TGT        | 2026-11-23 00:00:00 |   168.19      |          78.5833  | LONG     | Yahoo Finance |
| TLT        | 2026-11-23 00:00:00 |    81.69      |          31.8333  | LONG     | Yahoo Finance |
| TMUS       | 2026-11-23 00:00:00 |   166.36      |          36.4167  | LONG     | Yahoo Finance |
| WMT        | 2026-11-23 00:00:00 |   129.58      |          37.75    | LONG     | Yahoo Finance |
| XLP        | 2026-11-23 00:00:00 |    90.38      |          34.25    | LONG     | Yahoo Finance |
| AAPL       | 2026-11-23 00:00:00 |   349.08      |          49.5     | NEUTRAL  | Yahoo Finance |
| ABBV       | 2026-11-23 00:00:00 |   288.45      |          23       | NEUTRAL  | Yahoo Finance |
| ADA-USD    | 2026-11-24 00:00:00 |     0.14659   |         -29.3333  | NEUTRAL  | Kraken API    |
| ADBE       | 2026-11-23 00:00:00 |   223.98      |         -42.8333  | NEUTRAL  | Yahoo Finance |
| ALGO-USD   | 2026-11-24 00:00:00 |     0.07962   |         -25.75    | NEUTRAL  | Kraken API    |
| AMD        | 2026-11-23 00:00:00 |   453.46      |         -16.75    | NEUTRAL  | Yahoo Finance |
| AMGN       | 2026-11-23 00:00:00 |   449.04      |          20.5833  | NEUTRAL  | Yahoo Finance |
| AMZN       | 2026-11-23 00:00:00 |   255.39      |          17.3333  | NEUTRAL  | Yahoo Finance |
| ATOM-USD   | 2026-11-24 00:00:00 |     1.2961    |         -18.6667  | NEUTRAL  | Kraken API    |
| AVGO       | 2026-11-23 00:00:00 |   313.55      |         -52.5     | NEUTRAL  | Yahoo Finance |
| BAC        | 2026-11-23 00:00:00 |    48.14      |         -57.5     | NEUTRAL  | Yahoo Finance |
| BLK        | 2026-11-23 00:00:00 |  1144.52      |           9.33333 | NEUTRAL  | Yahoo Finance |
| C          | 2026-11-23 00:00:00 |   114.35      |         -64.8333  | NEUTRAL  | Yahoo Finance |
| CMCSA      | 2026-11-23 00:00:00 |    24.72      |          16.0833  | NEUTRAL  | Yahoo Finance |
| DE         | 2026-11-23 00:00:00 |   633.03      |         -27.3333  | NEUTRAL  | Yahoo Finance |
| DIA        | 2026-11-23 00:00:00 |   495.8       |         -56.5833  | NEUTRAL  | Yahoo Finance |
| EFA        | 2026-11-23 00:00:00 |    98.76      |         -62.8333  | NEUTRAL  | Yahoo Finance |
| EOG        | 2026-11-23 00:00:00 |   145.34      |         -21.3333  | NEUTRAL  | Yahoo Finance |
| ETC-USD    | 2026-11-24 00:00:00 |     5.79      |         -29.9167  | NEUTRAL  | Kraken API    |
| GDX        | 2026-11-23 00:00:00 |    72.8       |         -65.5     | NEUTRAL  | Yahoo Finance |
| GDXJ       | 2026-11-23 00:00:00 |    86.91      |         -65.5     | NEUTRAL  | Yahoo Finance |
| GLD        | 2026-11-23 00:00:00 |   333.02      |         -61.5     | NEUTRAL  | Yahoo Finance |
| GOOGL      | 2026-11-23 00:00:00 |   282.1       |         -16.5833  | NEUTRAL  | Yahoo Finance |
| GRT-USD    | 2026-11-24 00:00:00 |     0.0165    |         -19       | NEUTRAL  | Kraken API    |
| GS         | 2026-11-23 00:00:00 |   823.62      |         -62.0833  | NEUTRAL  | Yahoo Finance |
| HON        | 2026-11-23 00:00:00 |   221.97      |         -10.4167  | NEUTRAL  | Yahoo Finance |
| HYG        | 2026-11-23 00:00:00 |    76.52      |         -56.3333  | NEUTRAL  | Yahoo Finance |
| ICP-USD    | 2026-11-24 00:00:00 |     2.076     |         -63.25    | NEUTRAL  | Kraken API    |
| IEF        | 2026-11-23 00:00:00 |    91.64      |          15.0833  | NEUTRAL  | Yahoo Finance |
| INJ-USD    | 2026-11-24 00:00:00 |     6.115     |         -54       | NEUTRAL  | Kraken API    |
| ITA        | 2026-11-23 00:00:00 |    68.48      |         -60.3333  | NEUTRAL  | Yahoo Finance |
| IWM        | 2026-11-23 00:00:00 |   265.74      |         -56.5833  | NEUTRAL  | Yahoo Finance |
| JNJ        | 2026-11-23 00:00:00 |   270.05      |          14.25    | NEUTRAL  | Yahoo Finance |
| JPM        | 2026-11-23 00:00:00 |   316.66      |         -40.75    | NEUTRAL  | Yahoo Finance |
| KO         | 2026-11-23 00:00:00 |    95.88      |          22.8333  | NEUTRAL  | Yahoo Finance |
| LIN        | 2026-11-23 00:00:00 |   517         |          19.5     | NEUTRAL  | Yahoo Finance |
| LLY        | 2026-11-23 00:00:00 |  1364.6       |          18.4167  | NEUTRAL  | Yahoo Finance |
| META       | 2026-11-23 00:00:00 |   597.6       |         -27.75    | NEUTRAL  | Yahoo Finance |
| MPC        | 2026-11-23 00:00:00 |   357.69      |         -16.3333  | NEUTRAL  | Yahoo Finance |
| MRK        | 2026-11-23 00:00:00 |   135.47      |          -9.83333 | NEUTRAL  | Yahoo Finance |
| MS         | 2026-11-23 00:00:00 |   172.6       |         -60.3333  | NEUTRAL  | Yahoo Finance |
| MSFT       | 2026-11-23 00:00:00 |   492.5       |         -26.5     | NEUTRAL  | Yahoo Finance |
| NEM        | 2026-11-23 00:00:00 |   100.73      |         -65.5     | NEUTRAL  | Yahoo Finance |
| NFLX       | 2026-11-23 00:00:00 |    58.1       |         -59.1667  | NEUTRAL  | Yahoo Finance |
| ORCL       | 2026-11-23 00:00:00 |   113.68      |         -55.3333  | NEUTRAL  | Yahoo Finance |
| PEP        | 2026-11-23 00:00:00 |   140.21      |           1.5     | NEUTRAL  | Yahoo Finance |
| PFE        | 2026-11-23 00:00:00 |    27.4       |         -28.0833  | NEUTRAL  | Yahoo Finance |
| PM         | 2026-11-23 00:00:00 |   182.5       |         -55.0833  | NEUTRAL  | Yahoo Finance |
| QCOM       | 2026-11-23 00:00:00 |   165.38      |         -41.6667  | NEUTRAL  | Yahoo Finance |
| RTX        | 2026-11-23 00:00:00 |   194.77      |         -25.0833  | NEUTRAL  | Yahoo Finance |
| SCHW       | 2026-11-23 00:00:00 |    92.37      |          10       | NEUTRAL  | Yahoo Finance |
| SHY        | 2026-11-23 00:00:00 |    81.57      |          17.0833  | NEUTRAL  | Yahoo Finance |
| SKY-USD    | 2026-11-24 00:00:00 |     0.03858   |         -55.5833  | NEUTRAL  | Kraken API    |
| SNX-USD    | 2026-11-24 00:00:00 |     0.1478    |         -13.1667  | NEUTRAL  | Kraken API    |
| SPY        | 2026-11-23 00:00:00 |   722.29      |         -44.25    | NEUTRAL  | Yahoo Finance |
| SUSHI-USD  | 2026-11-24 00:00:00 |     0.1536    |         -22.6667  | NEUTRAL  | Kraken API    |
| T          | 2026-11-23 00:00:00 |    22.3       |           0.75    | NEUTRAL  | Yahoo Finance |
| TMO        | 2026-11-23 00:00:00 |   688.08      |          -1.33333 | NEUTRAL  | Yahoo Finance |
| TSLA       | 2026-11-23 00:00:00 |   385.46      |          -4.83333 | NEUTRAL  | Yahoo Finance |
| TXN        | 2026-11-23 00:00:00 |   291.19      |         -17.3333  | NEUTRAL  | Yahoo Finance |
| UNH        | 2026-11-23 00:00:00 |   336.08      |         -52.3333  | NEUTRAL  | Yahoo Finance |
| UPS        | 2026-11-23 00:00:00 |   108.51      |          22.1667  | NEUTRAL  | Yahoo Finance |
| VEA        | 2026-11-23 00:00:00 |    65.58      |         -66.5833  | NEUTRAL  | Yahoo Finance |
| VIXY       | 2026-11-23 00:00:00 |    22.58      |          26.3333  | NEUTRAL  | Yahoo Finance |
| VTI        | 2026-11-23 00:00:00 |   355.27      |         -47.5833  | NEUTRAL  | Yahoo Finance |
| VZ         | 2026-11-23 00:00:00 |    46.45      |          53.9167  | NEUTRAL  | Yahoo Finance |
| XBI        | 2026-11-23 00:00:00 |   147.16      |         -38.5833  | NEUTRAL  | Yahoo Finance |
| XLC        | 2026-11-23 00:00:00 |   103.6       |         -42.8333  | NEUTRAL  | Yahoo Finance |
| XLF        | 2026-11-23 00:00:00 |    55.65      |          -5.75    | NEUTRAL  | Yahoo Finance |
| XLI        | 2026-11-23 00:00:00 |   162.47      |         -60.3333  | NEUTRAL  | Yahoo Finance |
| XLU        | 2026-11-23 00:00:00 |    43.32      |           1.33333 | NEUTRAL  | Yahoo Finance |
| XLV        | 2026-11-23 00:00:00 |   179.42      |          18.4167  | NEUTRAL  | Yahoo Finance |
| XLY        | 2026-11-23 00:00:00 |   116.93      |           2.58333 | NEUTRAL  | Yahoo Finance |
| XRP-USD    | 2026-11-24 00:00:00 |     0.9346    |         -21       | NEUTRAL  | Kraken API    |
| ZEC-USD    | 2026-11-24 00:00:00 |   750.63      |         -55.6667  | NEUTRAL  | Kraken API    |
| AAVE-USD   | 2026-11-24 00:00:00 |    95.58      |         -57.3333  | SHORT    | Kraken API    |
| AMAT       | 2026-11-23 00:00:00 |   346.87      |         -53.75    | SHORT    | Yahoo Finance |
| APT-USD    | 2026-11-24 00:00:00 |     0.3797    |         -57.3333  | SHORT    | Kraken API    |
| ARB-USD    | 2026-11-24 00:00:00 |     0.1136    |         -57.3333  | SHORT    | Kraken API    |
| ARKK       | 2026-11-23 00:00:00 |    69.36      |         -44.0833  | SHORT    | Yahoo Finance |
| AVAX-USD   | 2026-11-24 00:00:00 |     6.716     |         -53.3333  | SHORT    | Kraken API    |
| BA         | 2026-11-23 00:00:00 |   162.39      |         -49.0833  | SHORT    | Yahoo Finance |
| BCH-USD    | 2026-11-24 00:00:00 |   198.99      |         -46.6667  | SHORT    | Kraken API    |
| BITO       | 2026-11-23 00:00:00 |    16.24      |         -50.8333  | SHORT    | Yahoo Finance |
| BONK-USD   | 2026-11-24 00:00:00 |     2.194e-06 |         -53.5833  | SHORT    | Kraken API    |
| BTC-USD    | 2026-11-24 00:00:00 | 59965.8       |         -51.6667  | SHORT    | Kraken API    |
| CAT        | 2026-11-23 00:00:00 |   547.04      |         -48.0833  | SHORT    | Yahoo Finance |
| COMP-USD   | 2026-11-24 00:00:00 |    17.45      |         -51.3333  | SHORT    | Kraken API    |
| COP        | 2026-11-23 00:00:00 |   132.19      |         -30.3333  | SHORT    | Yahoo Finance |
| CRM        | 2026-11-23 00:00:00 |   185.46      |         -45.9167  | SHORT    | Yahoo Finance |
| CRV-USD    | 2026-11-24 00:00:00 |     0.1782    |         -57.3333  | SHORT    | Kraken API    |
| CSCO       | 2026-11-23 00:00:00 |    96.8       |         -48.5833  | SHORT    | Yahoo Finance |
| CVX        | 2026-11-23 00:00:00 |   206.17      |         -33.1667  | SHORT    | Yahoo Finance |
| DASH-USD   | 2026-11-24 00:00:00 |    35.37      |         -55.6667  | SHORT    | Kraken API    |
| DBC        | 2026-11-23 00:00:00 |    29.11      |         -59.5833  | SHORT    | Yahoo Finance |
| DOGE-USD   | 2026-11-24 00:00:00 |     0.0558368 |         -51.6667  | SHORT    | Kraken API    |
| DOT-USD    | 2026-11-24 00:00:00 |     0.6735    |         -51.6667  | SHORT    | Kraken API    |
| EEM        | 2026-11-23 00:00:00 |    57.83      |         -52       | SHORT    | Yahoo Finance |
| ETH-USD    | 2026-11-24 00:00:00 |  1684.68      |         -50.8333  | SHORT    | Kraken API    |
| EWJ        | 2026-11-23 00:00:00 |    86.9       |         -50.25    | SHORT    | Yahoo Finance |
| FCX        | 2026-11-23 00:00:00 |    49.71      |         -54.25    | SHORT    | Yahoo Finance |
| FET-USD    | 2026-11-24 00:00:00 |     0.1078    |         -57.3333  | SHORT    | Kraken API    |
| FIL-USD    | 2026-11-24 00:00:00 |     0.555     |         -53.6667  | SHORT    | Kraken API    |
| FXI        | 2026-11-23 00:00:00 |    31.63      |         -53.25    | SHORT    | Yahoo Finance |
| HBAR-USD   | 2026-11-24 00:00:00 |     0.05174   |         -53.3333  | SHORT    | Kraken API    |
| IBIT       | 2026-11-23 00:00:00 |    34.62      |         -49.0833  | SHORT    | Yahoo Finance |
| IBM        | 2026-11-23 00:00:00 |   233         |         -31.0833  | SHORT    | Yahoo Finance |
| IEMG       | 2026-11-23 00:00:00 |    70.43      |         -50.25    | SHORT    | Yahoo Finance |
| INTC       | 2026-11-23 00:00:00 |    59.66      |         -34.75    | SHORT    | Yahoo Finance |
| INTU       | 2026-11-23 00:00:00 |   275.46      |         -42.5833  | SHORT    | Yahoo Finance |
| LDO-USD    | 2026-11-24 00:00:00 |     0.237     |         -57.3333  | SHORT    | Kraken API    |
| LINK-USD   | 2026-11-24 00:00:00 |     9.02701   |         -35       | SHORT    | Kraken API    |
| LRCX       | 2026-11-23 00:00:00 |   209.76      |         -40.4167  | SHORT    | Yahoo Finance |
| LTC-USD    | 2026-11-24 00:00:00 |    41.36      |         -51.6667  | SHORT    | Kraken API    |
| MU         | 2026-11-23 00:00:00 |   707.7       |         -57.8333  | SHORT    | Yahoo Finance |
| NEAR-USD   | 2026-11-24 00:00:00 |     2.9646    |         -40       | SHORT    | Kraken API    |
| NKE        | 2026-11-23 00:00:00 |    33.76      |         -35.25    | SHORT    | Yahoo Finance |
| NOW        | 2026-11-23 00:00:00 |    91.72      |         -45.75    | SHORT    | Yahoo Finance |
| NVDA       | 2026-11-23 00:00:00 |   165.05      |         -61.6667  | SHORT    | Yahoo Finance |
| OP-USD     | 2026-11-24 00:00:00 |     0.0702    |         -57.3333  | SHORT    | Kraken API    |
| OXY        | 2026-11-23 00:00:00 |    52.7       |         -61.5833  | SHORT    | Yahoo Finance |
| PEPE-USD   | 2026-11-24 00:00:00 |     3.489e-06 |         -57.3333  | SHORT    | Kraken API    |
| POL-USD    | 2026-11-24 00:00:00 |     0.07695   |         -50       | SHORT    | Kraken API    |
| QQQ        | 2026-11-23 00:00:00 |   651.03      |         -46.5     | SHORT    | Yahoo Finance |
| RENDER-USD | 2026-11-24 00:00:00 |     1.294     |         -57.3333  | SHORT    | Kraken API    |
| SHIB-USD   | 2026-11-24 00:00:00 |     3.617e-06 |         -53.3333  | SHORT    | Kraken API    |
| SLB        | 2026-11-23 00:00:00 |    46.16      |         -56.5833  | SHORT    | Yahoo Finance |
| SLV        | 2026-11-23 00:00:00 |    38.91      |         -52.25    | SHORT    | Yahoo Finance |
| SMH        | 2026-11-23 00:00:00 |   460.18      |         -54.25    | SHORT    | Yahoo Finance |
| SOL-USD    | 2026-11-24 00:00:00 |    70.78      |         -24.3333  | SHORT    | Kraken API    |
| SOXX       | 2026-11-23 00:00:00 |   140.22      |         -56       | SHORT    | Yahoo Finance |
| TIA-USD    | 2026-11-24 00:00:00 |     0.3339    |         -48.3333  | SHORT    | Kraken API    |
| TRX-USD    | 2026-11-24 00:00:00 |     0.308242  |         -38       | SHORT    | Kraken API    |
| UNI-USD    | 2026-11-24 00:00:00 |     4.7706    |         -57.3333  | SHORT    | Kraken API    |
| USO        | 2026-11-23 00:00:00 |   133.36      |         -35.6667  | SHORT    | Yahoo Finance |
| VNQ        | 2026-11-23 00:00:00 |    93.67      |         -31.3333  | SHORT    | Yahoo Finance |
| VWO        | 2026-11-23 00:00:00 |    53.55      |         -52       | SHORT    | Yahoo Finance |
| WFC        | 2026-11-23 00:00:00 |    80         |         -33.25    | SHORT    | Yahoo Finance |
| WIF-USD    | 2026-11-24 00:00:00 |     0.1244    |         -38.3333  | SHORT    | Kraken API    |
| XLB        | 2026-11-23 00:00:00 |    49.9       |         -45.3333  | SHORT    | Yahoo Finance |
| XLE        | 2026-11-23 00:00:00 |    59.87      |         -35.3333  | SHORT    | Yahoo Finance |
| XLK        | 2026-11-23 00:00:00 |   162.38      |         -31.3333  | SHORT    | Yahoo Finance |
| XLM-USD    | 2026-11-24 00:00:00 |     0.128365  |         -52.3333  | SHORT    | Kraken API    |
| XOM        | 2026-11-23 00:00:00 |   156.9       |         -33.6667  | SHORT    | Yahoo Finance |
| YFI-USD    | 2026-11-24 00:00:00 |  1657.4       |         -53.3333  | SHORT    | Kraken API    |

## Edge Summary

- Symbols with trades: **161** of 161
- Beat buy-and-hold: **37.89%** of traded symbols
- Positive return: **32.92%** of traded symbols
- Median strategy return: **-7.27%** (benchmark **15.18%**)
- Median excess vs benchmark: **-20.97%**
- Median Sharpe: **-0.05**
- Median exposure: **44.93%**

> Edge is real only if both _beat buy-and-hold_ and _median excess_ are convincingly positive across many symbols. Treat a single high-return symbol as noise.

## Portfolio Backtest

Actual capital-allocation books (not per-symbol averages). Benchmarks: `equal_weight_buyhold` (whole tracked universe), `spy_buyhold` (100% SPY), and `sixty_forty` (60% SPY / 40% AGG). `high_conf_voltarget` inverse-vol-weights the HIGH-confidence book; `conviction_long_short` is market-neutral. Judge on **Sharpe** and **max_drawdown** out-of-sample, not raw return: a fully-invested long book wins on return in a bull market but carries all the risk.

| strategy              | scope         | ann_return   | ann_vol   |   sharpe | max_drawdown   | total_return   |   avg_gross_exposure |
|:----------------------|:--------------|:-------------|:----------|---------:|:---------------|:---------------|---------------------:|
| equal_weight_buyhold  | full          | 4.92%        | 28.50%    |     0.17 | -39.53%        | 2.64%          |                 1    |
| equal_weight_buyhold  | out_of_sample | 13.88%       | 26.28%    |     0.53 | -24.61%        | 11.74%         |                 1    |
| all_signals_ew        | full          | -10.95%      | 24.41%    |    -0.45 | -52.46%        | -34.54%        |                 1    |
| all_signals_ew        | out_of_sample | -1.68%       | 21.75%    |    -0.08 | -22.66%        | -4.20%         |                 1    |
| high_conf_ew          | full          | -10.91%      | 29.94%    |    -0.36 | -50.45%        | -37.31%        |                 0.89 |
| high_conf_ew          | out_of_sample | 5.82%        | 25.30%    |     0.23 | -27.61%        | 2.83%          |                 0.89 |
| high_conf_voltarget   | full          | -13.49%      | 26.64%    |    -0.51 | -45.42%        | -40.36%        |                 0.89 |
| high_conf_voltarget   | out_of_sample | 0.20%        | 20.27%    |     0.01 | -23.45%        | -1.97%         |                 0.89 |
| conviction_long_short | full          | -15.89%      | 22.01%    |    -0.72 | -52.65%        | -42.71%        |                 0.96 |
| conviction_long_short | out_of_sample | -4.32%       | 17.27%    |    -0.25 | -22.69%        | -5.99%         |                 0.96 |
| spy_buyhold           | full          | 0.08%        | 14.21%    |     0.01 | -19.00%        | -2.76%         |                 0.79 |
| spy_buyhold           | out_of_sample | -10.24%      | 11.58%    |    -0.88 | -14.96%        | -10.96%        |                 0.79 |
| sixty_forty           | full          | -0.37%       | 8.88%     |    -0.04 | -11.86%        | -2.28%         |                 0.79 |
| sixty_forty           | out_of_sample | -8.31%       | 7.52%     |    -1.11 | -9.98%         | -8.73%         |                 0.79 |

## Walk-Forward Robustness

Each book measured across contiguous time folds (each a different regime). A book has durable edge only if `mean_sharpe` is positive, `min_sharpe` isn't deeply negative, and `pct_positive_folds` is high — a single great fold doesn't count. `fold_sharpes` lists each fold oldest-to-newest.

| strategy              |   n_folds |   mean_sharpe |   median_sharpe |   min_sharpe | pct_positive_folds   | mean_return   | fold_sharpes                 |
|:----------------------|----------:|--------------:|----------------:|-------------:|:---------------------|:--------------|:-----------------------------|
| equal_weight_buyhold  |         5 |          0.38 |            0.21 |        -0.85 | 60.00%               | 1.95%         | 1.23;1.59;-0.85;-0.30;0.21   |
| all_signals_ew        |         5 |         -0.53 |           -0.52 |        -1.69 | 40.00%               | -7.09%        | -1.54;-0.52;-1.69;0.72;0.37  |
| high_conf_ew          |         5 |         -0.23 |           -0.38 |        -2.09 | 40.00%               | -7.40%        | 0.99;-2.09;-0.38;0.85;-0.53  |
| high_conf_voltarget   |         5 |         -0.43 |           -0.35 |        -2.28 | 40.00%               | -8.84%        | 1.00;-2.28;-0.35;0.47;-0.99  |
| conviction_long_short |         5 |         -0.72 |           -0.58 |        -2.4  | 20.00%               | -9.98%        | -2.40;-0.58;-0.87;-0.14;0.42 |
| spy_buyhold           |         5 |         -0.1  |           -0.06 |        -1.56 | 40.00%               | -0.35%        | 1.13;0.24;-0.06;-0.24;-1.56  |
| sixty_forty           |         5 |         -0.16 |            0.03 |        -1.77 | 60.00%               | -0.37%        | 1.04;0.29;0.03;-0.39;-1.77   |

## Strategy Comparison

Each decision rule backtested over the same data. `out_of_sample` is the most recent ~35% of each symbol's history (unseen tail). A rule has real edge only if `median_excess` and `beat_benchmark_pct` stay positive out-of-sample, not just full-sample.

| strategy        | scope         |   symbols | beat_benchmark_pct   | positive_pct   | median_return   | median_benchmark   | median_excess   |   median_sharpe |   total_trades |
|:----------------|:--------------|----------:|:---------------------|:---------------|:----------------|:-------------------|:----------------|----------------:|---------------:|
| trend           | full          |       161 | 37.89%               | 32.92%         | -7.27%          | 15.18%             | -20.97%         |           -0.05 |          11352 |
| trend           | out_of_sample |       161 | 54.04%               | 54.04%         | 1.47%           | -4.41%             | 1.61%           |            0.19 |           3880 |
| mean_reversion  | full          |       159 | 40.88%               | 47.80%         | -0.23%          | 15.18%             | -12.64%         |           -0.02 |           1296 |
| mean_reversion  | out_of_sample |       132 | 61.36%               | 58.33%         | 0.38%           | -4.52%             | 4.32%           |            0.52 |            446 |
| regime_adaptive | full          |       161 | 37.89%               | 31.68%         | -7.60%          | 15.18%             | -21.88%         |           -0.06 |          11620 |
| regime_adaptive | out_of_sample |       161 | 54.04%               | 54.04%         | 1.47%           | -4.41%             | 1.61%           |            0.23 |           3989 |

## Signal Calibration

Realized forward return in the signal's direction, grouped by confidence. HIGH should outrank LOW for the confidence score to be meaningful.

| confidence_level   |   horizon |     n | mean_return   | median_return   | win_rate   |
|:-------------------|----------:|------:|:--------------|:----------------|:-----------|
| HIGH               |         5 |  7726 | 0.18%         | 0.06%           | 51.02%     |
| MEDIUM             |         5 | 29494 | 0.15%         | 0.08%           | 50.93%     |
| LOW                |         5 |  3712 | -0.15%        | -0.24%          | 47.63%     |
| ALL                |         5 | 40932 | 0.13%         | 0.05%           | 50.64%     |
| HIGH               |        10 |  7661 | 0.47%         | 0.07%           | 50.87%     |
| MEDIUM             |        10 | 29122 | 0.32%         | 0.09%           | 50.72%     |
| LOW                |        10 |  3680 | -0.28%        | -0.22%          | 48.37%     |
| ALL                |        10 | 40463 | 0.29%         | 0.07%           | 50.54%     |
| HIGH               |        20 |  7443 | 1.03%         | 0.25%           | 51.94%     |
| MEDIUM             |        20 | 28453 | 0.88%         | 0.50%           | 52.81%     |
| LOW                |        20 |  3607 | 0.03%         | -0.37%          | 48.29%     |
| ALL                |        20 | 39503 | 0.83%         | 0.39%           | 52.23%     |

## Backtest Summary

### Data Quality / Signal Availability

- **ok**: 161 symbols

| symbol     |   trades | return   | benchmark_return   | mdd     |   sharpe | exposure   | skipped_reason   |
|:-----------|---------:|:---------|:-------------------|:--------|---------:|:-----------|:-----------------|
| AAPL       |       67 | -10.99%  | 57.56%             | -20.65% |    -0.13 | 47.09%     | ok               |
| AAVE-USD   |       73 | -44.29%  | -59.32%            | -67.38% |    -0.34 | 41.19%     | ok               |
| ABBV       |       66 | -13.91%  | 76.06%             | -30.52% |    -0.24 | 49.42%     | ok               |
| ADA-USD    |       72 | -12.16%  | -73.66%            | -52.70% |     0.09 | 50.00%     | ok               |
| ADBE       |       74 | -1.66%   | -60.72%            | -31.20% |     0.11 | 54.08%     | ok               |
| AGG        |       65 | -7.44%   | -0.88%             | -10.74% |    -1.13 | 35.11%     | ok               |
| ALGO-USD   |       84 | -32.49%  | -50.97%            | -45.50% |    -0.2  | 41.57%     | ok               |
| AMAT       |       73 | -40.70%  | 42.56%             | -57.08% |    -0.33 | 51.25%     | ok               |
| AMD        |       54 | 23.48%   | 176.67%            | -38.64% |     0.42 | 36.44%     | ok               |
| AMGN       |       63 | -7.33%   | 45.14%             | -34.19% |    -0.06 | 53.24%     | ok               |
| AMZN       |       84 | -58.68%  | 29.25%             | -59.16% |    -1.74 | 40.93%     | ok               |
| APT-USD    |       76 | -5.49%   | -90.89%            | -56.73% |     0.2  | 41.19%     | ok               |
| ARB-USD    |       75 | 19.81%   | -58.40%            | -42.80% |     0.43 | 43.10%     | ok               |
| ARKK       |       89 | -25.75%  | 52.07%             | -38.67% |    -0.32 | 45.26%     | ok               |
| ATOM-USD   |       80 | -63.01%  | -65.80%            | -65.09% |    -1.02 | 44.83%     | ok               |
| AVAX-USD   |       66 | -39.32%  | -60.10%            | -48.46% |    -0.38 | 39.85%     | ok               |
| AVGO       |       68 | -14.06%  | 81.32%             | -44.82% |    -0.01 | 39.10%     | ok               |
| BA         |       63 | 24.05%   | -11.89%            | -24.47% |     0.48 | 53.58%     | ok               |
| BAC        |       78 | -7.42%   | 17.70%             | -23.14% |    -0.12 | 49.08%     | ok               |
| BCH-USD    |       82 | -2.44%   | -57.45%            | -54.04% |     0.19 | 50.00%     | ok               |
| BITO       |       83 | -14.37%  | -61.63%            | -43.13% |    -0.02 | 41.76%     | ok               |
| BLK        |       77 | -8.82%   | 45.04%             | -26.90% |    -0.16 | 46.92%     | ok               |
| BND        |       68 | -7.60%   | -0.99%             | -10.80% |    -1.14 | 36.11%     | ok               |
| BONK-USD   |       70 | 31.88%   | -82.81%            | -53.62% |     0.51 | 45.21%     | ok               |
| BTC-USD    |       75 | 12.24%   | -41.29%            | -25.52% |     0.34 | 53.26%     | ok               |
| C          |       79 | -37.30%  | 77.40%             | -39.84% |    -0.83 | 46.59%     | ok               |
| CAT        |       68 | 37.77%   | 65.46%             | -21.87% |     0.62 | 52.08%     | ok               |
| CL         |       60 | 7.82%    | 2.13%              | -14.32% |     0.3  | 40.43%     | ok               |
| CMCSA      |       86 | -35.50%  | -30.68%            | -45.76% |    -0.84 | 44.93%     | ok               |
| COMP-USD   |       91 | -36.34%  | -62.63%            | -52.17% |    -0.23 | 49.43%     | ok               |
| COP        |       68 | -12.98%  | 15.18%             | -38.80% |    -0.14 | 43.93%     | ok               |
| COST       |       58 | 3.84%    | 27.27%             | -31.32% |     0.18 | 41.10%     | ok               |
| CRM        |       69 | -18.88%  | -28.93%            | -39.41% |    -0.17 | 47.09%     | ok               |
| CRV-USD    |       64 | 102.22%  | -67.89%            | -41.76% |     0.93 | 37.93%     | ok               |
| CSCO       |       65 | 1.54%    | 105.56%            | -29.59% |     0.15 | 52.08%     | ok               |
| CVX        |       71 | -13.82%  | 31.56%             | -26.75% |    -0.28 | 44.09%     | ok               |
| DASH-USD   |       57 | -9.19%   | 88.37%             | -64.43% |     0.33 | 29.31%     | ok               |
| DBC        |       70 | -8.15%   | 22.88%             | -23.87% |    -0.2  | 37.10%     | ok               |
| DE         |       74 | -8.53%   | 74.49%             | -21.34% |    -0.08 | 45.26%     | ok               |
| DIA        |       72 | -9.80%   | 26.21%             | -16.20% |    -0.5  | 43.26%     | ok               |
| DIS        |       62 | 1.55%    | 21.97%             | -28.37% |     0.13 | 47.59%     | ok               |
| DOGE-USD   |       68 | -16.23%  | -63.85%            | -61.52% |     0.03 | 47.13%     | ok               |
| DOT-USD    |       76 | -58.61%  | -79.77%            | -68.61% |    -0.64 | 41.19%     | ok               |
| DXY-INDEX  |       40 | -0.02%   | -2.87%             | -5.13%  |     0.01 | 31.39%     | ok               |
| EEM        |       68 | -6.42%   | 33.10%             | -24.14% |    -0.1  | 42.76%     | ok               |
| EFA        |       64 | -9.07%   | 24.13%             | -12.63% |    -0.35 | 38.94%     | ok               |
| EOG        |       76 | -31.07%  | 14.65%             | -47.50% |    -0.66 | 44.26%     | ok               |
| ETC-USD    |       51 | 10.30%   | -62.82%            | -44.14% |     0.31 | 36.97%     | ok               |
| ETH-USD    |       59 | 154.36%  | -26.63%            | -30.11% |     1.33 | 48.85%     | ok               |
| EWJ        |       70 | -23.68%  | 25.05%             | -29.40% |    -0.76 | 38.94%     | ok               |
| FCX        |       67 | -12.22%  | -1.86%             | -46.84% |    -0    | 46.76%     | ok               |
| FET-USD    |       79 | -29.74%  | -82.40%            | -66.52% |    -0.05 | 44.83%     | ok               |
| FIL-USD    |       61 | -7.09%   | -74.54%            | -58.54% |     0.15 | 39.66%     | ok               |
| FXI        |       48 | -2.06%   | 17.58%             | -23.91% |     0.03 | 30.95%     | ok               |
| GDX        |       68 | -4.93%   | 106.35%            | -34.29% |     0.07 | 45.26%     | ok               |
| GDXJ       |       70 | -30.10%  | 97.75%             | -36.01% |    -0.32 | 44.43%     | ok               |
| GE         |       82 | -19.50%  | 97.09%             | -31.39% |    -0.27 | 49.42%     | ok               |
| GLD        |       52 | 11.67%   | 52.77%             | -14.15% |     0.35 | 46.09%     | ok               |
| GOOGL      |       57 | 63.82%   | 51.81%             | -17.55% |     1    | 49.92%     | ok               |
| GRT-USD    |       71 | 56.59%   | -78.46%            | -38.70% |     0.69 | 45.02%     | ok               |
| GS         |       68 | -2.77%   | 76.02%             | -21.94% |     0.04 | 47.42%     | ok               |
| HBAR-USD   |       44 | -23.58%  | -49.83%            | -56.47% |    -0.26 | 42.43%     | ok               |
| HD         |       69 | 9.28%    | 3.72%              | -17.15% |     0.3  | 45.42%     | ok               |
| HON        |       87 | -27.63%  | 5.69%              | -32.93% |    -0.7  | 51.58%     | ok               |
| HYG        |       91 | -7.27%   | -0.88%             | -10.59% |    -0.81 | 39.60%     | ok               |
| IBIT       |       46 | 57.48%   | -8.92%             | -18.95% |     0.86 | 36.47%     | ok               |
| IBM        |       73 | -24.18%  | 32.59%             | -48.94% |    -0.27 | 50.42%     | ok               |
| ICP-USD    |       70 | 15.46%   | -56.83%            | -42.66% |     0.4  | 41.76%     | ok               |
| IEF        |       78 | -10.33%  | -2.14%             | -12.21% |    -1.35 | 35.61%     | ok               |
| IEMG       |       64 | -3.05%   | 29.16%             | -24.73% |    -0.01 | 42.60%     | ok               |
| INJ-USD    |       56 | -2.07%   | -39.50%            | -56.80% |     0.23 | 38.51%     | ok               |
| INTC       |       72 | 48.08%   | 91.03%             | -60.60% |     0.57 | 50.75%     | ok               |
| INTU       |       75 | -11.61%  | -58.26%            | -37.44% |    -0.05 | 46.76%     | ok               |
| ITA        |       72 | 0.52%    | 54.29%             | -22.33% |     0.09 | 47.09%     | ok               |
| IWM        |       56 | 10.39%   | 31.67%             | -8.62%  |     0.42 | 34.44%     | ok               |
| JNJ        |       60 | 10.89%   | 85.36%             | -17.51% |     0.42 | 47.92%     | ok               |
| JPM        |       77 | -28.81%  | 51.74%             | -32.74% |    -0.85 | 44.93%     | ok               |
| KO         |       54 | 25.13%   | 51.40%             | -8.64%  |     0.85 | 40.43%     | ok               |
| LDO-USD    |       68 | 99.20%   | -65.04%            | -51.13% |     0.87 | 48.47%     | ok               |
| LIN        |       70 | -5.63%   | 19.42%             | -20.61% |    -0.13 | 42.43%     | ok               |
| LINK-USD   |       68 | 32.75%   | -24.91%            | -35.01% |     0.53 | 42.91%     | ok               |
| LLY        |       80 | -34.09%  | 51.94%             | -52.47% |    -0.52 | 49.25%     | ok               |
| LRCX       |       86 | -27.63%  | 93.73%             | -61.08% |    -0.11 | 45.26%     | ok               |
| LTC-USD    |       69 | 50.23%   | -48.47%            | -29.27% |     0.69 | 52.11%     | ok               |
| MCD        |       77 | 6.36%    | 10.55%             | -22.20% |     0.27 | 41.43%     | ok               |
| META       |       72 | -37.04%  | 17.19%             | -44.52% |    -0.59 | 49.25%     | ok               |
| MPC        |       70 | 11.57%   | 104.41%            | -33.74% |     0.31 | 53.41%     | ok               |
| MRK        |       67 | -24.79%  | 7.64%              | -35.95% |    -0.48 | 43.59%     | ok               |
| MS         |       69 | -6.30%   | 72.26%             | -27.79% |    -0.06 | 47.25%     | ok               |
| MSFT       |       83 | -30.04%  | 6.89%              | -39.07% |    -0.68 | 49.92%     | ok               |
| MU         |       53 | 77.04%   | 417.25%            | -64.76% |     0.73 | 49.92%     | ok               |
| NEAR-USD   |       67 | 162.95%  | 50.18%             | -47.64% |     1.09 | 44.25%     | ok               |
| NEM        |       70 | -25.86%  | 131.83%            | -39.56% |    -0.25 | 49.75%     | ok               |
| NFLX       |       86 | -6.78%   | -14.87%            | -27.17% |    -0.04 | 50.08%     | ok               |
| NKE        |       91 | -44.83%  | -55.13%            | -55.35% |    -0.76 | 47.25%     | ok               |
| NOW        |       79 | -6.29%   | -41.65%            | -42.66% |     0.14 | 51.75%     | ok               |
| NVDA       |       82 | -41.64%  | 40.36%             | -47.95% |    -0.38 | 55.79%     | ok               |
| OP-USD     |       72 | -2.71%   | -86.14%            | -56.85% |     0.21 | 36.78%     | ok               |
| ORCL       |       60 | 56.55%   | -21.26%            | -31.06% |     0.64 | 49.42%     | ok               |
| OXY        |       65 | 11.70%   | -15.44%            | -28.48% |     0.31 | 43.59%     | ok               |
| PEP        |       70 | 0.90%    | -13.77%            | -21.35% |     0.1  | 46.26%     | ok               |
| PEPE-USD   |       76 | -26.02%  | -62.38%            | -60.19% |     0.02 | 47.13%     | ok               |
| PFE        |       81 | -38.60%  | -1.08%             | -46.24% |    -1.19 | 37.94%     | ok               |
| PG         |       62 | -17.45%  | 3.52%              | -24.55% |    -0.59 | 37.94%     | ok               |
| PM         |       77 | -5.63%   | 79.94%             | -37.61% |    -0.03 | 47.75%     | ok               |
| POL-USD    |       81 | 6.45%    | -55.50%            | -46.25% |     0.28 | 47.51%     | ok               |
| QCOM       |       77 | -35.78%  | -18.86%            | -50.90% |    -0.37 | 40.10%     | ok               |
| QQQ        |       72 | -5.45%   | 32.58%             | -15.84% |    -0.05 | 43.26%     | ok               |
| RENDER-USD |       88 | -51.14%  | -56.12%            | -56.14% |    -0.4  | 46.36%     | ok               |
| RTX        |       73 | 16.35%   | 93.34%             | -16.99% |     0.43 | 52.91%     | ok               |
| SBUX       |       64 | -12.97%  | 39.47%             | -29.22% |    -0.18 | 40.77%     | ok               |
| SCHW       |       84 | -20.31%  | 24.61%             | -31.92% |    -0.44 | 48.25%     | ok               |
| SHIB-USD   |       81 | -32.83%  | -66.82%            | -55.32% |    -0.3  | 51.34%     | ok               |
| SHY        |       54 | -1.90%   | 0.09%              | -3.30%  |    -0.63 | 38.94%     | ok               |
| SKY-USD    |       87 | -42.58%  | -48.08%            | -66.76% |    -0.46 | 45.98%     | ok               |
| SLB        |       75 | -38.22%  | -2.43%             | -53.66% |    -0.72 | 48.25%     | ok               |
| SLV        |       66 | 53.29%   | 39.76%             | -37.05% |     0.71 | 42.93%     | ok               |
| SMH        |       52 | 48.20%   | 70.68%             | -33.99% |     0.71 | 41.76%     | ok               |
| SNX-USD    |       62 | -20.59%  | -71.36%            | -50.74% |    -0.05 | 35.82%     | ok               |
| SOL-USD    |       69 | 10.08%   | -47.75%            | -42.33% |     0.33 | 59.00%     | ok               |
| SOXX       |       58 | 53.24%   | 65.44%             | -40.14% |     0.73 | 41.10%     | ok               |
| SPY        |       63 | -6.43%   | 30.98%             | -15.53% |    -0.17 | 46.42%     | ok               |
| SUSHI-USD  |       89 | -58.77%  | -72.17%            | -78.67% |    -0.63 | 45.02%     | ok               |
| T          |       68 | 53.35%   | 19.38%             | -17.01% |     0.95 | 57.40%     | ok               |
| TGT        |       60 | -5.12%   | 16.15%             | -32.83% |    -0.02 | 38.27%     | ok               |
| TIA-USD    |       85 | -50.04%  | -77.21%            | -74.75% |    -0.28 | 44.25%     | ok               |
| TLT        |       68 | -22.70%  | -11.01%            | -23.34% |    -1.71 | 35.27%     | ok               |
| TMO        |       67 | 38.81%   | 28.47%             | -18.85% |     0.74 | 56.41%     | ok               |
| TMUS       |       76 | -7.31%   | -6.78%             | -33.05% |    -0.06 | 45.59%     | ok               |
| TRX-USD    |       60 | 9.94%    | 13.76%             | -23.08% |     0.37 | 49.81%     | ok               |
| TSLA       |       74 | -48.55%  | 56.44%             | -58.36% |    -0.48 | 41.26%     | ok               |
| TXN        |       83 | -30.18%  | 46.37%             | -46.56% |    -0.35 | 48.75%     | ok               |
| UNH        |       72 | 50.09%   | -31.40%            | -26.31% |     0.72 | 48.09%     | ok               |
| UNI-USD    |       80 | 12.41%   | -26.35%            | -60.56% |     0.38 | 50.77%     | ok               |
| UPS        |       71 | -37.94%  | -19.95%            | -41.37% |    -0.74 | 44.59%     | ok               |
| USO        |       73 | -15.47%  | 64.09%             | -45.90% |    -0.1  | 33.78%     | ok               |
| VEA        |       64 | -7.02%   | 30.74%             | -18.84% |    -0.25 | 41.26%     | ok               |
| VIXY       |      102 | -85.16%  | -45.41%            | -91.81% |    -1.17 | 32.28%     | ok               |
| VNQ        |       68 | -12.22%  | 12.48%             | -24.92% |    -0.45 | 40.60%     | ok               |
| VTI        |       67 | -12.68%  | 31.24%             | -17.64% |    -0.41 | 46.42%     | ok               |
| VWO        |       80 | -16.36%  | 19.88%             | -25.20% |    -0.52 | 41.76%     | ok               |
| VZ         |       86 | -27.73%  | 12.96%             | -31.67% |    -0.84 | 43.26%     | ok               |
| WFC        |       80 | -20.55%  | 31.88%             | -30.08% |    -0.36 | 46.92%     | ok               |
| WIF-USD    |       64 | 19.10%   | -82.25%            | -48.32% |     0.42 | 44.83%     | ok               |
| WMT        |       69 | 9.39%    | 89.89%             | -25.96% |     0.32 | 49.08%     | ok               |
| XBI        |       60 | -3.53%   | 61.95%             | -19.01% |    -0.01 | 37.27%     | ok               |
| XLB        |       68 | -11.40%  | 13.72%             | -24.92% |    -0.35 | 35.11%     | ok               |
| XLC        |       63 | -0.16%   | 20.34%             | -12.33% |     0.06 | 48.25%     | ok               |
| XLE        |       72 | -2.78%   | 30.82%             | -34.77% |     0.01 | 48.25%     | ok               |
| XLF        |       78 | -5.19%   | 33.94%             | -23.61% |    -0.12 | 49.75%     | ok               |
| XLI        |       82 | -12.77%  | 33.54%             | -18.27% |    -0.49 | 42.60%     | ok               |
| XLK        |       46 | 28.93%   | 39.88%             | -19.09% |     0.62 | 43.76%     | ok               |
| XLM-USD    |       75 | 2.71%    | -45.97%            | -56.32% |     0.25 | 49.81%     | ok               |
| XLP        |       65 | 12.84%   | 18.24%             | -8.96%  |     0.63 | 41.60%     | ok               |
| XLU        |       71 | -3.32%   | 26.61%             | -20.40% |    -0.09 | 41.60%     | ok               |
| XLV        |       72 | -19.55%  | 25.21%             | -21.39% |    -0.86 | 37.60%     | ok               |
| XLY        |       81 | -14.57%  | 24.55%             | -22.09% |    -0.38 | 47.42%     | ok               |
| XOM        |       59 | 5.18%    | 36.72%             | -20.29% |     0.21 | 37.27%     | ok               |
| XRP-USD    |       70 | 0.65%    | -54.73%            | -38.39% |     0.2  | 37.55%     | ok               |
| YFI-USD    |       76 | -42.19%  | -64.33%            | -55.32% |    -0.55 | 40.23%     | ok               |
| ZEC-USD    |       54 | 115.10%  | 1800.81%           | -56.50% |     0.83 | 36.59%     | ok               |

## AAPL Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -5.42%   | 57.56%             | -21.71% |     0    |       76 | 51.91%     | ok               |
|          15 | -9.60%   | 57.56%             | -23.86% |    -0.08 |       85 | 59.40%     | ok               |
|          30 | -10.99%  | 57.56%             | -20.65% |    -0.13 |       67 | 47.09%     | ok               |
|          35 | -12.27%  | 57.56%             | -22.04% |    -0.17 |       67 | 45.76%     | ok               |
|          25 | -14.59%  | 57.56%             | -22.37% |    -0.21 |       77 | 49.25%     | ok               |

## AAVE-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -3.49%   | -59.32%            | -45.38% |     0.18 |       49 | 35.25%     | ok               |
|          35 | -15.20%  | -59.32%            | -50.40% |     0.06 |       59 | 39.08%     | ok               |
|          50 | -12.77%  | -59.32%            | -47.89% |     0.02 |       46 | 22.99%     | ok               |
|          45 | -15.23%  | -59.32%            | -51.44% |     0.02 |       54 | 29.89%     | ok               |
|          15 | -28.49%  | -59.32%            | -58.12% |    -0.03 |       78 | 54.79%     | ok               |

## ABBV Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 2.91%    | 76.06%             | -21.96% |     0.16 |       50 | 36.61%     | ok               |
|          20 | -10.23%  | 76.06%             | -28.48% |    -0.14 |       61 | 53.24%     | ok               |
|          25 | -10.64%  | 76.06%             | -30.04% |    -0.15 |       65 | 51.25%     | ok               |
|          30 | -13.91%  | 76.06%             | -30.52% |    -0.24 |       66 | 49.42%     | ok               |
|          40 | -14.56%  | 76.06%             | -27.87% |    -0.28 |       70 | 42.60%     | ok               |

## ADA-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 22.85%   | -73.66%            | -46.50% |     0.46 |       68 | 64.18%     | ok               |
|          20 | 1.86%    | -73.66%            | -53.45% |     0.28 |       77 | 58.81%     | ok               |
|          35 | 3.18%    | -73.66%            | -44.07% |     0.25 |       62 | 44.25%     | ok               |
|          25 | -15.95%  | -73.66%            | -59.89% |     0.09 |       67 | 54.60%     | ok               |
|          30 | -12.16%  | -73.66%            | -52.70% |     0.09 |       72 | 50.00%     | ok               |

## ADBE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | 14.90%   | -60.72%            | -29.07% |     0.35 |       59 | 58.57%     | ok               |
|          20 | -1.21%   | -60.72%            | -31.52% |     0.13 |       65 | 61.73%     | ok               |
|          30 | -1.66%   | -60.72%            | -31.20% |     0.11 |       74 | 54.08%     | ok               |
|          15 | -9.07%   | -60.72%            | -34.98% |     0.01 |       67 | 63.89%     | ok               |
|          35 | -9.37%   | -60.72%            | -32.89% |    -0.03 |       77 | 45.76%     | ok               |

## AGG Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -7.44%   | -0.88%             | -10.74% |    -1.13 |       65 | 35.11%     | ok               |
|          45 | -6.98%   | -0.88%             | -9.39%  |    -1.27 |       60 | 24.46%     | ok               |
|          20 | -9.28%   | -0.88%             | -11.89% |    -1.3  |       70 | 40.77%     | ok               |
|          25 | -9.05%   | -0.88%             | -12.28% |    -1.32 |       71 | 38.60%     | ok               |
|          35 | -8.70%   | -0.88%             | -11.53% |    -1.38 |       66 | 31.78%     | ok               |

## ALGO-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -26.94%  | -50.97%            | -47.97% |    -0.1  |       86 | 45.98%     | ok               |
|          30 | -32.49%  | -50.97%            | -45.50% |    -0.2  |       84 | 41.57%     | ok               |
|          15 | -43.21%  | -50.97%            | -55.15% |    -0.32 |       84 | 53.64%     | ok               |
|          20 | -45.58%  | -50.97%            | -57.02% |    -0.39 |       83 | 49.04%     | ok               |
|          35 | -52.69%  | -50.97%            | -55.58% |    -0.69 |       72 | 35.82%     | ok               |

## AMAT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -35.43%  | 42.56%             | -53.90% |    -0.2  |       76 | 60.40%     | ok               |
|          30 | -40.70%  | 42.56%             | -57.08% |    -0.33 |       73 | 51.25%     | ok               |
|          35 | -42.04%  | 42.56%             | -54.63% |    -0.37 |       73 | 48.59%     | ok               |
|          20 | -48.63%  | 42.56%             | -60.04% |    -0.44 |       80 | 56.41%     | ok               |
|          25 | -49.10%  | 42.56%             | -59.59% |    -0.47 |       75 | 53.91%     | ok               |

## AMD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 39.99%   | 176.67%            | -37.12% |     0.56 |       52 | 31.61%     | ok               |
|          40 | 23.48%   | 176.67%            | -38.64% |     0.42 |       54 | 36.44%     | ok               |
|          35 | 13.24%   | 176.67%            | -40.22% |     0.34 |       62 | 37.94%     | ok               |
|          45 | 11.74%   | 176.67%            | -42.84% |     0.32 |       58 | 34.44%     | ok               |
|          30 | -3.80%   | 176.67%            | -47.20% |     0.19 |       65 | 40.60%     | ok               |

## AMGN Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -2.43%   | 45.14%             | -26.65% |     0.05 |       62 | 58.57%     | ok               |
|          35 | -4.99%   | 45.14%             | -31.29% |    -0.01 |       65 | 49.92%     | ok               |
|          30 | -7.33%   | 45.14%             | -34.19% |    -0.06 |       63 | 53.24%     | ok               |
|          50 | -6.48%   | 45.14%             | -24.68% |    -0.1  |       54 | 34.11%     | ok               |
|          25 | -9.23%   | 45.14%             | -33.47% |    -0.1  |       59 | 55.41%     | ok               |

## AMZN Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -33.78%  | 29.25%             | -34.72% |    -1.08 |       62 | 29.78%     | ok               |
|          50 | -34.81%  | 29.25%             | -35.58% |    -1.29 |       52 | 22.30%     | ok               |
|          45 | -41.18%  | 29.25%             | -41.87% |    -1.51 |       62 | 26.12%     | ok               |
|          35 | -55.86%  | 29.25%             | -56.38% |    -1.7  |       79 | 35.11%     | ok               |
|          30 | -58.68%  | 29.25%             | -59.16% |    -1.74 |       84 | 40.93%     | ok               |

## APT-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 78.66%   | -90.89%            | -25.96% |     1.1  |       44 | 17.62%     | ok               |
|          45 | 47.79%   | -90.89%            | -52.49% |     0.69 |       62 | 24.52%     | ok               |
|          20 | 30.00%   | -90.89%            | -56.22% |     0.51 |       84 | 52.68%     | ok               |
|          40 | 17.32%   | -90.89%            | -53.58% |     0.4  |       58 | 31.03%     | ok               |
|          35 | 9.57%    | -90.89%            | -49.10% |     0.33 |       74 | 36.40%     | ok               |

## ARB-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 133.83%  | -58.40%            | -34.35% |     1.04 |       60 | 26.82%     | ok               |
|          40 | 90.04%   | -58.40%            | -38.69% |     0.82 |       57 | 34.29%     | ok               |
|          35 | 71.37%   | -58.40%            | -37.63% |     0.73 |       69 | 38.51%     | ok               |
|          50 | 41.01%   | -58.40%            | -34.35% |     0.57 |       54 | 18.77%     | ok               |
|          15 | 21.85%   | -58.40%            | -56.32% |     0.46 |       98 | 57.85%     | ok               |

## ARKK Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -8.62%   | 52.07%             | -37.76% |     0.03 |       88 | 56.07%     | ok               |
|          20 | -18.81%  | 52.07%             | -35.06% |    -0.15 |       91 | 51.58%     | ok               |
|          30 | -25.75%  | 52.07%             | -38.67% |    -0.32 |       89 | 45.26%     | ok               |
|          35 | -31.06%  | 52.07%             | -41.28% |    -0.47 |       94 | 41.93%     | ok               |
|          25 | -36.45%  | 52.07%             | -47.50% |    -0.54 |       99 | 47.75%     | ok               |

## ATOM-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -48.88%  | -65.80%            | -56.71% |    -0.49 |       82 | 65.52%     | ok               |
|          20 | -55.38%  | -65.80%            | -60.19% |    -0.68 |       92 | 56.90%     | ok               |
|          25 | -54.22%  | -65.80%            | -56.00% |    -0.7  |       82 | 50.96%     | ok               |
|          45 | -49.56%  | -65.80%            | -53.91% |    -0.76 |       64 | 30.46%     | ok               |
|          50 | -40.82%  | -65.80%            | -40.87% |    -0.77 |       64 | 19.16%     | ok               |

## AVAX-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 36.52%   | -60.10%            | -22.06% |     0.65 |       40 | 17.43%     | ok               |
|          40 | 15.67%   | -60.10%            | -26.27% |     0.38 |       42 | 28.93%     | ok               |
|          45 | 14.37%   | -60.10%            | -26.90% |     0.36 |       38 | 24.52%     | ok               |
|          35 | -0.92%   | -60.10%            | -33.05% |     0.17 |       52 | 34.48%     | ok               |
|          15 | -25.43%  | -60.10%            | -43.91% |    -0.08 |       76 | 51.92%     | ok               |

## AVGO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -14.06%  | 81.32%             | -44.82% |    -0.01 |       68 | 39.10%     | ok               |
|          25 | -15.06%  | 81.32%             | -45.43% |    -0.02 |       72 | 41.93%     | ok               |
|          20 | -21.64%  | 81.32%             | -45.94% |    -0.09 |       81 | 45.76%     | ok               |
|          50 | -20.56%  | 81.32%             | -44.23% |    -0.14 |       62 | 26.96%     | ok               |
|          35 | -22.38%  | 81.32%             | -48.57% |    -0.14 |       78 | 36.27%     | ok               |

## BA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 39.24%   | -11.89%            | -18.09% |     0.69 |       66 | 50.25%     | ok               |
|          25 | 34.45%   | -11.89%            | -26.02% |     0.61 |       64 | 56.91%     | ok               |
|          50 | 24.37%   | -11.89%            | -13.34% |     0.6  |       50 | 35.94%     | ok               |
|          40 | 24.92%   | -11.89%            | -23.87% |     0.53 |       50 | 44.43%     | ok               |
|          30 | 24.05%   | -11.89%            | -24.47% |     0.48 |       63 | 53.58%     | ok               |

## BAC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 3.18%    | 17.70%             | -16.89% |     0.16 |       84 | 55.07%     | ok               |
|          35 | -0.35%   | 17.70%             | -23.35% |     0.06 |       70 | 44.26%     | ok               |
|          15 | -2.69%   | 17.70%             | -21.05% |     0.03 |       90 | 61.06%     | ok               |
|          45 | -1.37%   | 17.70%             | -16.06% |     0.02 |       56 | 34.44%     | ok               |
|          25 | -2.48%   | 17.70%             | -22.01% |     0.02 |       84 | 52.41%     | ok               |

## BCH-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 19.88%   | -57.45%            | -45.64% |     0.41 |       79 | 58.81%     | ok               |
|          20 | 16.76%   | -57.45%            | -45.52% |     0.39 |       74 | 55.56%     | ok               |
|          35 | 3.42%    | -57.45%            | -57.75% |     0.25 |       72 | 46.17%     | ok               |
|          25 | 0.25%    | -57.45%            | -48.42% |     0.22 |       78 | 51.92%     | ok               |
|          30 | -2.44%   | -57.45%            | -54.04% |     0.19 |       82 | 50.00%     | ok               |

## BITO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 3.92%    | -61.63%            | -31.98% |     0.2  |       54 | 24.96%     | ok               |
|          45 | -2.52%   | -61.63%            | -32.05% |     0.11 |       56 | 28.29%     | ok               |
|          30 | -14.37%  | -61.63%            | -43.13% |    -0.02 |       83 | 41.76%     | ok               |
|          35 | -15.92%  | -61.63%            | -42.80% |    -0.05 |       74 | 37.44%     | ok               |
|          40 | -15.65%  | -61.63%            | -40.13% |    -0.07 |       68 | 32.78%     | ok               |

## BLK Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 0.53%    | 45.04%             | -20.79% |     0.09 |       84 | 43.43%     | ok               |
|          25 | -4.38%   | 45.04%             | -24.62% |    -0.03 |       73 | 49.42%     | ok               |
|          40 | -3.85%   | 45.04%             | -22.83% |    -0.04 |       76 | 38.94%     | ok               |
|          20 | -5.76%   | 45.04%             | -21.48% |    -0.06 |       80 | 51.75%     | ok               |
|          30 | -8.82%   | 45.04%             | -26.90% |    -0.16 |       77 | 46.92%     | ok               |

## BND Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -8.01%   | -0.99%             | -10.72% |    -1.12 |       65 | 41.93%     | ok               |
|          25 | -7.81%   | -0.99%             | -11.16% |    -1.13 |       70 | 39.77%     | ok               |
|          30 | -7.60%   | -0.99%             | -10.80% |    -1.14 |       68 | 36.11%     | ok               |
|          40 | -7.75%   | -0.99%             | -11.34% |    -1.29 |       60 | 29.95%     | ok               |
|          15 | -9.37%   | -0.99%             | -12.04% |    -1.31 |       77 | 44.26%     | ok               |

## BONK-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 154.73%  | -82.81%            | -23.92% |     1.27 |       40 | 18.58%     | ok               |
|          40 | 134.88%  | -82.81%            | -42.38% |     1.06 |       62 | 35.44%     | ok               |
|          45 | 107.47%  | -82.81%            | -31.97% |     0.99 |       64 | 25.10%     | ok               |
|          35 | 71.97%   | -82.81%            | -48.89% |     0.75 |       60 | 41.00%     | ok               |
|          15 | 47.09%   | -82.81%            | -56.51% |     0.61 |       65 | 60.92%     | ok               |

## BTC-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 70.71%   | -41.29%            | -21.12% |     1.15 |       58 | 42.91%     | ok               |
|          40 | 63.18%   | -41.29%            | -17.26% |     1.11 |       46 | 36.40%     | ok               |
|          45 | 54.39%   | -41.29%            | -12.58% |     1.04 |       38 | 31.61%     | ok               |
|          30 | 32.33%   | -41.29%            | -22.34% |     0.63 |       70 | 48.66%     | ok               |
|          50 | 19.58%   | -41.29%            | -20.16% |     0.52 |       36 | 25.29%     | ok               |

## C Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -15.04%  | 77.40%             | -22.98% |    -0.38 |       66 | 30.62%     | ok               |
|          45 | -24.68%  | 77.40%             | -30.69% |    -0.65 |       76 | 35.61%     | ok               |
|          40 | -29.42%  | 77.40%             | -35.05% |    -0.75 |       72 | 38.10%     | ok               |
|          25 | -36.37%  | 77.40%             | -37.53% |    -0.79 |       69 | 49.25%     | ok               |
|          20 | -38.36%  | 77.40%             | -39.30% |    -0.83 |       75 | 51.91%     | ok               |

## CAT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 52.86%   | 65.46%             | -21.99% |     0.75 |       69 | 62.40%     | ok               |
|          25 | 48.07%   | 65.46%             | -21.79% |     0.72 |       66 | 54.24%     | ok               |
|          30 | 37.77%   | 65.46%             | -21.87% |     0.62 |       68 | 52.08%     | ok               |
|          20 | 34.60%   | 65.46%             | -24.75% |     0.58 |       70 | 56.74%     | ok               |
|          35 | 31.17%   | 65.46%             | -25.22% |     0.55 |       68 | 46.09%     | ok               |

## CL Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 8.75%    | 2.13%              | -13.51% |     0.36 |       40 | 24.63%     | ok               |
|          30 | 7.82%    | 2.13%              | -14.32% |     0.3  |       60 | 40.43%     | ok               |
|          45 | 3.76%    | 2.13%              | -13.13% |     0.19 |       44 | 27.95%     | ok               |
|          35 | 3.52%    | 2.13%              | -15.39% |     0.17 |       60 | 36.61%     | ok               |
|          15 | -1.97%   | 2.13%              | -19.00% |     0.02 |       62 | 48.09%     | ok               |

## CMCSA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -17.43%  | -30.68%            | -27.57% |    -0.57 |       48 | 16.81%     | ok               |
|          45 | -22.75%  | -30.68%            | -34.36% |    -0.71 |       62 | 21.46%     | ok               |
|          15 | -35.90%  | -30.68%            | -43.40% |    -0.74 |       92 | 59.73%     | ok               |
|          40 | -30.66%  | -30.68%            | -41.83% |    -0.81 |       89 | 28.95%     | ok               |
|          35 | -33.41%  | -30.68%            | -46.34% |    -0.84 |       93 | 39.43%     | ok               |

## COMP-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -14.38%  | -62.63%            | -36.92% |    -0.05 |       44 | 18.58%     | ok               |
|          30 | -36.34%  | -62.63%            | -52.17% |    -0.23 |       91 | 49.43%     | ok               |
|          45 | -36.93%  | -62.63%            | -39.73% |    -0.38 |       66 | 28.35%     | ok               |
|          35 | -46.29%  | -62.63%            | -53.74% |    -0.44 |       83 | 43.10%     | ok               |
|          15 | -58.93%  | -62.63%            | -70.27% |    -0.54 |       98 | 68.20%     | ok               |

## COP Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -12.98%  | 15.18%             | -38.80% |    -0.14 |       68 | 43.93%     | ok               |
|          35 | -15.25%  | 15.18%             | -41.20% |    -0.19 |       67 | 40.93%     | ok               |
|          50 | -14.99%  | 15.18%             | -38.05% |    -0.24 |       50 | 30.78%     | ok               |
|          45 | -19.67%  | 15.18%             | -42.92% |    -0.34 |       60 | 34.28%     | ok               |
|          25 | -24.08%  | 15.18%             | -44.40% |    -0.36 |       79 | 47.09%     | ok               |

## COST Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 18.48%   | 27.27%             | -24.32% |     0.56 |       60 | 47.09%     | ok               |
|          25 | 15.07%   | 27.27%             | -24.93% |     0.49 |       57 | 44.26%     | ok               |
|          35 | 8.42%    | 27.27%             | -30.16% |     0.33 |       56 | 38.60%     | ok               |
|          30 | 3.84%    | 27.27%             | -31.32% |     0.18 |       58 | 41.10%     | ok               |
|          40 | 3.30%    | 27.27%             | -31.90% |     0.17 |       54 | 36.11%     | ok               |

## CRM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | -5.97%   | -28.93%            | -26.69% |     0.04 |       66 | 42.26%     | ok               |
|          40 | -9.50%   | -28.93%            | -32.67% |    -0.03 |       72 | 38.10%     | ok               |
|          15 | -19.21%  | -28.93%            | -47.54% |    -0.13 |       94 | 58.24%     | ok               |
|          30 | -18.88%  | -28.93%            | -39.41% |    -0.17 |       69 | 47.09%     | ok               |
|          25 | -21.64%  | -28.93%            | -43.03% |    -0.21 |       70 | 49.25%     | ok               |

## CRV-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 115.43%  | -67.89%            | -40.84% |     1.01 |       62 | 33.91%     | ok               |
|          30 | 102.22%  | -67.89%            | -41.76% |     0.93 |       64 | 37.93%     | ok               |
|          40 | 87.35%   | -67.89%            | -40.10% |     0.88 |       56 | 30.46%     | ok               |
|          45 | 70.32%   | -67.89%            | -41.44% |     0.8  |       56 | 23.56%     | ok               |
|          20 | 76.81%   | -67.89%            | -56.11% |     0.78 |       69 | 45.02%     | ok               |

## CSCO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 26.37%   | 105.56%            | -22.87% |     0.56 |       54 | 42.26%     | ok               |
|          50 | 22.39%   | 105.56%            | -21.93% |     0.5  |       56 | 40.27%     | ok               |
|          40 | 10.59%   | 105.56%            | -28.93% |     0.3  |       58 | 45.42%     | ok               |
|          20 | 7.25%    | 105.56%            | -29.33% |     0.24 |       71 | 55.07%     | ok               |
|          35 | 7.10%    | 105.56%            | -28.42% |     0.24 |       60 | 48.92%     | ok               |

## CVX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -8.74%   | 31.56%             | -27.82% |    -0.17 |       63 | 35.94%     | ok               |
|          40 | -9.92%   | 31.56%             | -25.79% |    -0.19 |       73 | 39.60%     | ok               |
|          25 | -11.25%  | 31.56%             | -23.25% |    -0.2  |       75 | 46.92%     | ok               |
|          50 | -8.62%   | 31.56%             | -29.71% |    -0.2  |       56 | 31.45%     | ok               |
|          30 | -13.82%  | 31.56%             | -26.75% |    -0.28 |       71 | 44.09%     | ok               |

## DASH-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 107.83%  | 88.37%             | -43.46% |     0.84 |       42 | 17.82%     | ok               |
|          40 | 81.06%   | 88.37%             | -42.64% |     0.73 |       48 | 24.52%     | ok               |
|          45 | 56.19%   | 88.37%             | -46.93% |     0.62 |       46 | 21.07%     | ok               |
|          25 | -7.80%   | 88.37%             | -64.14% |     0.34 |       69 | 31.61%     | ok               |
|          30 | -9.19%   | 88.37%             | -64.43% |     0.33 |       57 | 29.31%     | ok               |

## DBC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 1.16%    | 22.88%             | -26.01% |     0.1  |       83 | 44.26%     | ok               |
|          20 | -5.08%   | 22.88%             | -25.45% |    -0.09 |       75 | 41.60%     | ok               |
|          25 | -5.27%   | 22.88%             | -24.61% |    -0.1  |       70 | 39.43%     | ok               |
|          30 | -8.15%   | 22.88%             | -23.87% |    -0.2  |       70 | 37.10%     | ok               |
|          50 | -8.63%   | 22.88%             | -18.84% |    -0.27 |       52 | 25.62%     | ok               |

## DE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -3.72%   | 74.49%             | -20.02% |     0.03 |       64 | 49.25%     | ok               |
|          25 | -5.12%   | 74.49%             | -20.21% |    -0.01 |       71 | 47.25%     | ok               |
|          50 | -5.21%   | 74.49%             | -19.21% |    -0.06 |       60 | 31.11%     | ok               |
|          30 | -8.53%   | 74.49%             | -21.34% |    -0.08 |       74 | 45.26%     | ok               |
|          45 | -7.45%   | 74.49%             | -18.05% |    -0.09 |       60 | 35.11%     | ok               |

## DIA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -7.72%   | 26.21%             | -13.58% |    -0.37 |       66 | 44.43%     | ok               |
|          20 | -9.83%   | 26.21%             | -15.48% |    -0.48 |       68 | 46.76%     | ok               |
|          35 | -9.40%   | 26.21%             | -16.94% |    -0.49 |       74 | 40.10%     | ok               |
|          30 | -9.80%   | 26.21%             | -16.20% |    -0.5  |       72 | 43.26%     | ok               |
|          40 | -11.98%  | 26.21%             | -18.41% |    -0.68 |       76 | 36.61%     | ok               |

## DIS Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 45.06%   | 21.97%             | -10.17% |     1.22 |       48 | 29.95%     | ok               |
|          40 | 15.05%   | 21.97%             | -18.75% |     0.42 |       61 | 38.10%     | ok               |
|          45 | 12.32%   | 21.97%             | -16.54% |     0.37 |       49 | 33.61%     | ok               |
|          15 | 6.67%    | 21.97%             | -32.73% |     0.23 |       79 | 57.24%     | ok               |
|          35 | 3.91%    | 21.97%             | -25.87% |     0.18 |       73 | 44.26%     | ok               |

## DOGE-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -12.73%  | -63.85%            | -60.29% |     0.12 |       81 | 62.45%     | ok               |
|          20 | -14.96%  | -63.85%            | -60.01% |     0.07 |       79 | 56.51%     | ok               |
|          30 | -16.23%  | -63.85%            | -61.52% |     0.03 |       68 | 47.13%     | ok               |
|          50 | -11.64%  | -63.85%            | -52.77% |     0.03 |       60 | 20.31%     | ok               |
|          25 | -19.18%  | -63.85%            | -60.53% |     0.01 |       72 | 51.92%     | ok               |

## DOT-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -34.52%  | -79.77%            | -46.40% |    -0.48 |       56 | 18.39%     | ok               |
|          40 | -41.61%  | -79.77%            | -50.99% |    -0.51 |       58 | 31.61%     | ok               |
|          35 | -51.91%  | -79.77%            | -59.91% |    -0.53 |       68 | 37.16%     | ok               |
|          20 | -57.97%  | -79.77%            | -71.39% |    -0.54 |       92 | 52.49%     | ok               |
|          15 | -62.49%  | -79.77%            | -76.85% |    -0.54 |       81 | 57.28%     | ok               |

## DXY-INDEX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -0.02%   | -2.87%             | -5.13%  |     0.01 |       40 | 31.39%     | ok               |
|          40 | -1.97%   | -2.87%             | -6.15%  |    -0.26 |       66 | 46.97%     | ok               |
|          45 | -2.38%   | -2.87%             | -6.67%  |    -0.35 |       62 | 38.10%     | ok               |
|          30 | -3.25%   | -2.87%             | -8.65%  |    -0.39 |       76 | 57.14%     | ok               |
|          15 | -4.87%   | -2.87%             | -10.94% |    -0.47 |       97 | 73.16%     | ok               |

## EEM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -2.01%   | 33.10%             | -25.18% |     0.03 |       67 | 46.26%     | ok               |
|          25 | -3.08%   | 33.10%             | -23.69% |    -0    |       67 | 44.59%     | ok               |
|          15 | -4.84%   | 33.10%             | -26.83% |    -0.04 |       73 | 50.08%     | ok               |
|          30 | -6.42%   | 33.10%             | -24.14% |    -0.1  |       68 | 42.76%     | ok               |
|          35 | -8.30%   | 33.10%             | -23.88% |    -0.16 |       72 | 40.60%     | ok               |

## EFA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -0.91%   | 24.13%             | -10.10% |     0.03 |       60 | 49.08%     | ok               |
|          20 | -8.09%   | 24.13%             | -12.23% |    -0.28 |       67 | 46.26%     | ok               |
|          30 | -9.07%   | 24.13%             | -12.63% |    -0.35 |       64 | 38.94%     | ok               |
|          25 | -9.53%   | 24.13%             | -13.73% |    -0.36 |       68 | 42.60%     | ok               |
|          40 | -8.96%   | 24.13%             | -14.83% |    -0.38 |       60 | 34.44%     | ok               |

## EOG Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -13.58%  | 14.65%             | -34.41% |    -0.24 |       46 | 31.61%     | ok               |
|          40 | -18.08%  | 14.65%             | -36.53% |    -0.35 |       62 | 35.11%     | ok               |
|          50 | -21.13%  | 14.65%             | -35.63% |    -0.47 |       50 | 29.12%     | ok               |
|          35 | -23.88%  | 14.65%             | -39.26% |    -0.49 |       75 | 39.60%     | ok               |
|          30 | -31.07%  | 14.65%             | -47.50% |    -0.66 |       76 | 44.26%     | ok               |

## ETC-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 10.30%   | -62.82%            | -44.14% |     0.31 |       51 | 36.97%     | ok               |
|          35 | 7.70%    | -62.82%            | -44.37% |     0.27 |       45 | 33.33%     | ok               |
|          50 | 1.48%    | -62.82%            | -30.03% |     0.16 |       30 | 18.58%     | ok               |
|          40 | -1.57%   | -62.82%            | -36.96% |     0.13 |       44 | 27.20%     | ok               |
|          45 | -3.86%   | -62.82%            | -32.70% |     0.08 |       36 | 22.22%     | ok               |

## ETH-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 154.36%  | -26.63%            | -30.11% |     1.33 |       59 | 48.85%     | ok               |
|          30 | 110.94%  | -26.63%            | -32.89% |     1.06 |       65 | 56.90%     | ok               |
|          40 | 92.17%   | -26.63%            | -33.11% |     1.04 |       60 | 41.00%     | ok               |
|          25 | 85.67%   | -26.63%            | -40.90% |     0.91 |       63 | 60.73%     | ok               |
|          45 | 67.15%   | -26.63%            | -33.73% |     0.87 |       64 | 37.36%     | ok               |

## EWJ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -17.75%  | 25.05%             | -30.00% |    -0.49 |       58 | 41.43%     | ok               |
|          15 | -21.70%  | 25.05%             | -31.15% |    -0.59 |       69 | 44.76%     | ok               |
|          25 | -22.05%  | 25.05%             | -29.85% |    -0.65 |       62 | 40.27%     | ok               |
|          30 | -23.68%  | 25.05%             | -29.40% |    -0.76 |       70 | 38.94%     | ok               |
|          45 | -24.42%  | 25.05%             | -28.91% |    -0.91 |       66 | 30.28%     | ok               |

## FCX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 18.11%   | -1.86%             | -30.39% |     0.39 |       54 | 34.28%     | ok               |
|          50 | 11.43%   | -1.86%             | -26.57% |     0.3  |       58 | 30.45%     | ok               |
|          40 | 5.97%    | -1.86%             | -42.89% |     0.23 |       64 | 39.27%     | ok               |
|          30 | -12.22%  | -1.86%             | -46.84% |    -0    |       67 | 46.76%     | ok               |
|          35 | -16.64%  | -1.86%             | -50.12% |    -0.08 |       69 | 44.43%     | ok               |

## FET-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 41.01%   | -82.40%            | -59.58% |     0.57 |       69 | 59.39%     | ok               |
|          20 | -13.20%  | -82.40%            | -66.17% |     0.18 |       84 | 55.36%     | ok               |
|          25 | -20.99%  | -82.40%            | -65.31% |     0.09 |       83 | 49.43%     | ok               |
|          30 | -29.74%  | -82.40%            | -66.52% |    -0.05 |       79 | 44.83%     | ok               |
|          45 | -31.26%  | -82.40%            | -51.19% |    -0.27 |       54 | 23.18%     | ok               |

## FIL-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -7.09%   | -74.54%            | -58.54% |     0.15 |       61 | 39.66%     | ok               |
|          25 | -27.62%  | -74.54%            | -70.65% |    -0.07 |       68 | 43.49%     | ok               |
|          15 | -38.27%  | -74.54%            | -71.31% |    -0.16 |       87 | 52.68%     | ok               |
|          40 | -30.47%  | -74.54%            | -64.10% |    -0.2  |       54 | 30.84%     | ok               |
|          35 | -34.43%  | -74.54%            | -70.22% |    -0.24 |       62 | 34.87%     | ok               |

## FXI Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 1.88%    | 17.58%             | -21.68% |     0.13 |       51 | 35.61%     | ok               |
|          25 | 0.13%    | 17.58%             | -22.57% |     0.09 |       50 | 32.28%     | ok               |
|          20 | -1.34%   | 17.58%             | -24.53% |     0.05 |       48 | 33.61%     | ok               |
|          30 | -2.06%   | 17.58%             | -23.91% |     0.03 |       48 | 30.95%     | ok               |
|          35 | -6.28%   | 17.58%             | -27.53% |    -0.08 |       50 | 28.12%     | ok               |

## GDX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -1.32%   | 106.35%            | -30.00% |     0.14 |       82 | 51.41%     | ok               |
|          40 | -3.49%   | 106.35%            | -34.42% |     0.07 |       66 | 39.10%     | ok               |
|          30 | -4.93%   | 106.35%            | -34.29% |     0.07 |       68 | 45.26%     | ok               |
|          35 | -9.07%   | 106.35%            | -38.67% |    -0.01 |       74 | 41.76%     | ok               |
|          25 | -13.90%  | 106.35%            | -42.42% |    -0.07 |       72 | 47.09%     | ok               |

## GDXJ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -16.79%  | 97.75%             | -34.84% |    -0.05 |       72 | 51.58%     | ok               |
|          35 | -28.11%  | 97.75%             | -38.09% |    -0.29 |       70 | 41.76%     | ok               |
|          30 | -30.10%  | 97.75%             | -36.01% |    -0.32 |       70 | 44.43%     | ok               |
|          25 | -34.34%  | 97.75%             | -39.67% |    -0.37 |       75 | 47.59%     | ok               |
|          40 | -30.85%  | 97.75%             | -46.16% |    -0.38 |       64 | 39.27%     | ok               |

## GE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 1.03%    | 97.09%             | -21.25% |     0.12 |       62 | 34.61%     | ok               |
|          45 | -10.76%  | 97.09%             | -21.88% |    -0.13 |       74 | 37.60%     | ok               |
|          30 | -19.50%  | 97.09%             | -31.39% |    -0.27 |       82 | 49.42%     | ok               |
|          20 | -20.32%  | 97.09%             | -29.62% |    -0.27 |       78 | 53.91%     | ok               |
|          25 | -19.88%  | 97.09%             | -31.57% |    -0.27 |       78 | 51.25%     | ok               |

## GLD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | 21.05%   | 52.77%             | -13.87% |     0.54 |       48 | 47.59%     | ok               |
|          20 | 19.41%   | 52.77%             | -13.87% |     0.51 |       49 | 49.25%     | ok               |
|          30 | 11.67%   | 52.77%             | -14.15% |     0.35 |       52 | 46.09%     | ok               |
|          35 | 8.96%    | 52.77%             | -15.57% |     0.3  |       52 | 43.43%     | ok               |
|          15 | 9.21%    | 52.77%             | -18.05% |     0.29 |       53 | 52.58%     | ok               |

## GOOGL Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 66.36%   | 51.81%             | -17.38% |     1.05 |       61 | 46.09%     | ok               |
|          45 | 57.80%   | 51.81%             | -11.66% |     1.03 |       52 | 38.44%     | ok               |
|          25 | 65.18%   | 51.81%             | -17.13% |     1    |       57 | 52.41%     | ok               |
|          30 | 63.82%   | 51.81%             | -17.55% |     1    |       57 | 49.92%     | ok               |
|          50 | 53.15%   | 51.81%             | -11.52% |     0.99 |       44 | 33.61%     | ok               |

## GRT-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 86.64%   | -78.46%            | -36.70% |     0.82 |       68 | 61.69%     | ok               |
|          35 | 66.03%   | -78.46%            | -29.35% |     0.76 |       64 | 39.08%     | ok               |
|          20 | 64.50%   | -78.46%            | -37.63% |     0.72 |       80 | 54.60%     | ok               |
|          30 | 56.59%   | -78.46%            | -38.70% |     0.69 |       71 | 45.02%     | ok               |
|          45 | 50.38%   | -78.46%            | -37.14% |     0.68 |       48 | 25.67%     | ok               |

## GS Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 22.58%   | 76.02%             | -20.56% |     0.5  |       66 | 55.24%     | ok               |
|          40 | 7.27%    | 76.02%             | -16.16% |     0.25 |       64 | 40.93%     | ok               |
|          20 | 7.49%    | 76.02%             | -23.19% |     0.25 |       64 | 51.91%     | ok               |
|          25 | -0.60%   | 76.02%             | -23.32% |     0.09 |       66 | 49.92%     | ok               |
|          35 | -1.92%   | 76.02%             | -19.95% |     0.06 |       68 | 44.59%     | ok               |

## HBAR-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -21.25%  | -49.83%            | -58.64% |    -0.18 |       54 | 56.25%     | ok               |
|          30 | -23.58%  | -49.83%            | -56.47% |    -0.26 |       44 | 42.43%     | ok               |
|          45 | -22.91%  | -49.83%            | -49.09% |    -0.3  |       30 | 27.63%     | ok               |
|          40 | -24.59%  | -49.83%            | -51.16% |    -0.33 |       34 | 33.22%     | ok               |
|          20 | -29.92%  | -49.83%            | -63.19% |    -0.38 |       57 | 51.64%     | ok               |

## HD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 9.28%    | 3.72%              | -17.15% |     0.3  |       69 | 45.42%     | ok               |
|          35 | 7.03%    | 3.72%              | -16.37% |     0.26 |       72 | 40.60%     | ok               |
|          25 | 6.63%    | 3.72%              | -16.67% |     0.24 |       70 | 47.59%     | ok               |
|          40 | 5.83%    | 3.72%              | -14.18% |     0.23 |       72 | 35.11%     | ok               |
|          45 | 4.78%    | 3.72%              | -12.98% |     0.21 |       44 | 29.95%     | ok               |

## HON Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -10.69%  | 5.69%              | -20.43% |    -0.27 |       64 | 30.28%     | ok               |
|          45 | -14.32%  | 5.69%              | -22.88% |    -0.36 |       66 | 35.44%     | ok               |
|          35 | -26.51%  | 5.69%              | -31.30% |    -0.7  |       87 | 46.76%     | ok               |
|          30 | -27.63%  | 5.69%              | -32.93% |    -0.7  |       87 | 51.58%     | ok               |
|          40 | -26.70%  | 5.69%              | -31.84% |    -0.74 |       74 | 39.60%     | ok               |

## HYG Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -4.80%   | -0.88%             | -7.94%  |    -0.55 |       72 | 34.28%     | ok               |
|          45 | -6.56%   | -0.88%             | -9.08%  |    -0.79 |       72 | 30.62%     | ok               |
|          35 | -7.00%   | -0.88%             | -9.70%  |    -0.8  |       81 | 36.11%     | ok               |
|          20 | -7.53%   | -0.88%             | -11.59% |    -0.81 |       96 | 45.42%     | ok               |
|          25 | -7.52%   | -0.88%             | -11.22% |    -0.81 |       91 | 42.76%     | ok               |

## IBIT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 92.30%   | -8.92%             | -19.20% |     1.12 |       48 | 43.76%     | ok               |
|          50 | 60.77%   | -8.92%             | -17.37% |     0.99 |       28 | 25.14%     | ok               |
|          45 | 59.15%   | -8.92%             | -17.37% |     0.94 |       34 | 26.68%     | ok               |
|          30 | 57.48%   | -8.92%             | -18.95% |     0.86 |       46 | 36.47%     | ok               |
|          40 | 46.63%   | -8.92%             | -22.57% |     0.79 |       42 | 29.75%     | ok               |

## IBM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -18.26%  | 32.59%             | -49.43% |    -0.12 |       89 | 62.40%     | ok               |
|          35 | -22.56%  | 32.59%             | -47.10% |    -0.25 |       67 | 47.25%     | ok               |
|          30 | -24.18%  | 32.59%             | -48.94% |    -0.27 |       73 | 50.42%     | ok               |
|          20 | -29.98%  | 32.59%             | -53.45% |    -0.35 |       75 | 55.41%     | ok               |
|          50 | -28.87%  | 32.59%             | -45.97% |    -0.42 |       48 | 35.44%     | ok               |

## ICP-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 15.46%   | -56.83%            | -42.66% |     0.4  |       70 | 41.76%     | ok               |
|          35 | 3.04%    | -56.83%            | -49.65% |     0.28 |       68 | 36.59%     | ok               |
|          40 | -8.65%   | -56.83%            | -47.74% |     0.15 |       64 | 32.18%     | ok               |
|          20 | -26.75%  | -56.83%            | -63.83% |     0.07 |       81 | 49.23%     | ok               |
|          25 | -28.34%  | -56.83%            | -58.19% |     0.03 |       70 | 45.21%     | ok               |

## IEF Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -6.88%   | -2.14%             | -10.18% |    -0.79 |       74 | 43.93%     | ok               |
|          15 | -8.13%   | -2.14%             | -11.01% |    -0.92 |       74 | 45.76%     | ok               |
|          40 | -8.44%   | -2.14%             | -10.34% |    -1.22 |       68 | 26.96%     | ok               |
|          45 | -8.80%   | -2.14%             | -10.45% |    -1.32 |       64 | 24.29%     | ok               |
|          30 | -10.33%  | -2.14%             | -12.21% |    -1.35 |       78 | 35.61%     | ok               |

## IEMG Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | 0.21%    | 29.16%             | -23.73% |     0.08 |       63 | 44.93%     | ok               |
|          20 | -1.48%   | 29.16%             | -25.26% |     0.04 |       61 | 46.59%     | ok               |
|          30 | -3.05%   | 29.16%             | -24.73% |    -0.01 |       64 | 42.60%     | ok               |
|          35 | -3.23%   | 29.16%             | -21.81% |    -0.02 |       69 | 41.26%     | ok               |
|          40 | -5.78%   | 29.16%             | -18.43% |    -0.11 |       68 | 38.77%     | ok               |

## INJ-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 33.68%   | -39.50%            | -42.48% |     0.53 |       52 | 35.63%     | ok               |
|          40 | 31.33%   | -39.50%            | -33.49% |     0.51 |       42 | 32.38%     | ok               |
|          45 | 13.61%   | -39.50%            | -39.58% |     0.35 |       48 | 26.05%     | ok               |
|          25 | 1.63%    | -39.50%            | -51.31% |     0.28 |       60 | 41.57%     | ok               |
|          15 | -0.59%   | -39.50%            | -60.14% |     0.27 |       69 | 46.55%     | ok               |

## INTC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 108.30%  | 91.03%             | -49.32% |     0.88 |       60 | 35.94%     | ok               |
|          50 | 101.83%  | 91.03%             | -48.35% |     0.86 |       64 | 32.11%     | ok               |
|          15 | 70.68%   | 91.03%             | -53.65% |     0.67 |       76 | 61.06%     | ok               |
|          20 | 61.18%   | 91.03%             | -52.47% |     0.63 |       82 | 57.57%     | ok               |
|          25 | 58.00%   | 91.03%             | -56.41% |     0.62 |       81 | 53.24%     | ok               |

## INTU Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 8.08%    | -58.26%            | -34.18% |     0.26 |       67 | 28.29%     | ok               |
|          35 | 2.03%    | -58.26%            | -41.63% |     0.16 |       71 | 40.77%     | ok               |
|          45 | 2.12%    | -58.26%            | -36.41% |     0.15 |       65 | 32.28%     | ok               |
|          40 | -1.41%   | -58.26%            | -38.72% |     0.09 |       71 | 35.94%     | ok               |
|          15 | -5.67%   | -58.26%            | -39.48% |     0.06 |       83 | 56.41%     | ok               |

## ITA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 0.31%    | 54.29%             | -26.15% |     0.1  |       73 | 59.40%     | ok               |
|          30 | 0.52%    | 54.29%             | -22.33% |     0.09 |       72 | 47.09%     | ok               |
|          50 | -0.54%   | 54.29%             | -21.48% |     0.05 |       68 | 34.78%     | ok               |
|          35 | -4.77%   | 54.29%             | -22.44% |    -0.07 |       72 | 43.43%     | ok               |
|          20 | -5.79%   | 54.29%             | -26.56% |    -0.07 |       72 | 53.74%     | ok               |

## IWM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd    |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:-------|---------:|---------:|:-----------|:-----------------|
|          25 | 15.74%   | 31.67%             | -8.39% |     0.59 |       54 | 35.94%     | ok               |
|          20 | 11.17%   | 31.67%             | -9.67% |     0.44 |       64 | 36.94%     | ok               |
|          30 | 10.39%   | 31.67%             | -8.62% |     0.42 |       56 | 34.44%     | ok               |
|          40 | 8.67%    | 31.67%             | -9.21% |     0.4  |       44 | 29.28%     | ok               |
|          35 | 8.33%    | 31.67%             | -9.25% |     0.36 |       52 | 31.95%     | ok               |

## JNJ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 17.00%   | 85.36%             | -10.97% |     0.67 |       44 | 36.61%     | ok               |
|          15 | 14.37%   | 85.36%             | -18.02% |     0.5  |       60 | 54.58%     | ok               |
|          30 | 10.89%   | 85.36%             | -17.51% |     0.42 |       60 | 47.92%     | ok               |
|          20 | 9.09%    | 85.36%             | -17.61% |     0.36 |       66 | 51.08%     | ok               |
|          45 | 6.99%    | 85.36%             | -13.35% |     0.31 |       50 | 40.27%     | ok               |

## JPM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 0.07%    | 51.74%             | -15.90% |     0.06 |       52 | 32.11%     | ok               |
|          45 | -10.24%  | 51.74%             | -21.91% |    -0.27 |       56 | 34.78%     | ok               |
|          20 | -27.14%  | 51.74%             | -35.58% |    -0.64 |       88 | 49.25%     | ok               |
|          40 | -22.56%  | 51.74%             | -28.47% |    -0.69 |       68 | 37.44%     | ok               |
|          35 | -25.11%  | 51.74%             | -29.39% |    -0.77 |       78 | 41.10%     | ok               |

## KO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 25.13%   | 51.40%             | -8.64%  |     0.85 |       54 | 40.43%     | ok               |
|          40 | 20.37%   | 51.40%             | -9.28%  |     0.75 |       58 | 35.94%     | ok               |
|          35 | 20.88%   | 51.40%             | -8.73%  |     0.73 |       58 | 38.94%     | ok               |
|          25 | 19.03%   | 51.40%             | -10.61% |     0.67 |       60 | 43.09%     | ok               |
|          50 | 7.57%    | 51.40%             | -16.13% |     0.34 |       44 | 30.12%     | ok               |

## LDO-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 190.99%  | -65.04%            | -43.31% |     1.15 |       78 | 60.92%     | ok               |
|          30 | 99.20%   | -65.04%            | -51.13% |     0.87 |       68 | 48.47%     | ok               |
|          20 | 101.25%  | -65.04%            | -45.41% |     0.86 |       81 | 55.36%     | ok               |
|          25 | 87.68%   | -65.04%            | -49.38% |     0.81 |       78 | 52.68%     | ok               |
|          35 | 36.68%   | -65.04%            | -58.29% |     0.55 |       82 | 41.38%     | ok               |

## LIN Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -2.38%   | 19.42%             | -22.01% |    -0.01 |       69 | 45.26%     | ok               |
|          20 | -3.14%   | 19.42%             | -23.00% |    -0.04 |       64 | 48.09%     | ok               |
|          45 | -3.83%   | 19.42%             | -17.04% |    -0.1  |       48 | 25.79%     | ok               |
|          30 | -5.63%   | 19.42%             | -20.61% |    -0.13 |       70 | 42.43%     | ok               |
|          35 | -5.97%   | 19.42%             | -19.70% |    -0.16 |       72 | 35.94%     | ok               |

## LINK-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 38.94%   | -24.91%            | -34.21% |     0.58 |       60 | 38.70%     | ok               |
|          30 | 32.75%   | -24.91%            | -35.01% |     0.53 |       68 | 42.91%     | ok               |
|          45 | 27.78%   | -24.91%            | -34.16% |     0.49 |       52 | 30.65%     | ok               |
|          40 | 26.58%   | -24.91%            | -36.88% |     0.48 |       52 | 33.72%     | ok               |
|          50 | 24.44%   | -24.91%            | -28.65% |     0.47 |       48 | 24.71%     | ok               |

## LLY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -0.28%   | 51.94%             | -38.23% |     0.11 |       50 | 34.94%     | ok               |
|          15 | -15.45%  | 51.94%             | -48.12% |    -0.1  |       70 | 60.23%     | ok               |
|          45 | -15.75%  | 51.94%             | -42.99% |    -0.18 |       60 | 38.94%     | ok               |
|          40 | -24.65%  | 51.94%             | -45.23% |    -0.35 |       70 | 42.10%     | ok               |
|          20 | -27.94%  | 51.94%             | -51.14% |    -0.35 |       77 | 55.07%     | ok               |

## LRCX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -19.79%  | 93.73%             | -56.69% |     0.03 |       82 | 54.08%     | ok               |
|          35 | -22.56%  | 93.73%             | -58.47% |    -0.04 |       82 | 44.59%     | ok               |
|          20 | -26.72%  | 93.73%             | -62.91% |    -0.06 |       87 | 49.92%     | ok               |
|          40 | -25.98%  | 93.73%             | -55.33% |    -0.1  |       74 | 42.26%     | ok               |
|          30 | -27.63%  | 93.73%             | -61.08% |    -0.11 |       86 | 45.26%     | ok               |

## LTC-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | 51.08%   | -48.47%            | -32.32% |     0.7  |       69 | 54.60%     | ok               |
|          30 | 50.23%   | -48.47%            | -29.27% |     0.69 |       69 | 52.11%     | ok               |
|          35 | 45.60%   | -48.47%            | -30.75% |     0.68 |       68 | 45.98%     | ok               |
|          45 | 36.83%   | -48.47%            | -35.29% |     0.61 |       56 | 34.48%     | ok               |
|          20 | 21.72%   | -48.47%            | -44.78% |     0.44 |       66 | 58.81%     | ok               |

## MCD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 6.19%    | 10.55%             | -9.22%  |     0.31 |       50 | 25.96%     | ok               |
|          30 | 6.36%    | 10.55%             | -22.20% |     0.27 |       77 | 41.43%     | ok               |
|          35 | 4.91%    | 10.55%             | -16.97% |     0.24 |       69 | 38.60%     | ok               |
|          25 | 4.15%    | 10.55%             | -23.93% |     0.2  |       75 | 44.09%     | ok               |
|          20 | -0.10%   | 10.55%             | -24.58% |     0.06 |       77 | 47.25%     | ok               |

## META Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -17.19%  | 17.19%             | -37.10% |    -0.21 |       64 | 38.10%     | ok               |
|          40 | -21.48%  | 17.19%             | -40.49% |    -0.28 |       66 | 41.26%     | ok               |
|          50 | -21.67%  | 17.19%             | -38.90% |    -0.33 |       64 | 33.78%     | ok               |
|          35 | -32.66%  | 17.19%             | -40.80% |    -0.52 |       79 | 46.76%     | ok               |
|          30 | -37.04%  | 17.19%             | -44.52% |    -0.59 |       72 | 49.25%     | ok               |

## MPC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 20.28%   | 104.41%            | -18.24% |     0.45 |       52 | 41.43%     | ok               |
|          40 | 18.30%   | 104.41%            | -20.11% |     0.41 |       62 | 48.09%     | ok               |
|          35 | 17.46%   | 104.41%            | -30.41% |     0.39 |       68 | 50.75%     | ok               |
|          45 | 16.22%   | 104.41%            | -19.46% |     0.38 |       58 | 45.42%     | ok               |
|          30 | 11.57%   | 104.41%            | -33.74% |     0.31 |       70 | 53.41%     | ok               |

## MRK Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -15.24%  | 7.64%              | -28.03% |    -0.21 |       87 | 53.24%     | ok               |
|          25 | -15.36%  | 7.64%              | -31.07% |    -0.23 |       72 | 45.26%     | ok               |
|          20 | -19.51%  | 7.64%              | -29.34% |    -0.33 |       77 | 48.59%     | ok               |
|          50 | -16.04%  | 7.64%              | -23.01% |    -0.34 |       58 | 29.62%     | ok               |
|          45 | -18.12%  | 7.64%              | -25.38% |    -0.37 |       59 | 32.95%     | ok               |

## MS Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 0.68%    | 72.26%             | -19.99% |     0.1  |       64 | 38.27%     | ok               |
|          15 | -1.58%   | 72.26%             | -22.02% |     0.07 |       70 | 56.24%     | ok               |
|          20 | -3.77%   | 72.26%             | -25.68% |     0.01 |       69 | 52.08%     | ok               |
|          30 | -6.30%   | 72.26%             | -27.79% |    -0.06 |       69 | 47.25%     | ok               |
|          25 | -7.77%   | 72.26%             | -28.36% |    -0.1  |       67 | 49.42%     | ok               |

## MSFT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -17.75%  | 6.89%              | -24.64% |    -0.43 |       70 | 35.94%     | ok               |
|          50 | -21.08%  | 6.89%              | -25.48% |    -0.56 |       60 | 30.78%     | ok               |
|          35 | -27.00%  | 6.89%              | -35.38% |    -0.63 |       73 | 45.26%     | ok               |
|          40 | -26.80%  | 6.89%              | -34.92% |    -0.65 |       69 | 39.60%     | ok               |
|          30 | -30.04%  | 6.89%              | -39.07% |    -0.68 |       83 | 49.92%     | ok               |

## MU Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 95.75%   | 417.25%            | -61.12% |     0.81 |       60 | 45.42%     | ok               |
|          45 | 84.22%   | 417.25%            | -62.28% |     0.77 |       62 | 42.60%     | ok               |
|          15 | 85.55%   | 417.25%            | -61.96% |     0.74 |       58 | 58.07%     | ok               |
|          30 | 77.04%   | 417.25%            | -64.76% |     0.73 |       53 | 49.92%     | ok               |
|          35 | 72.14%   | 417.25%            | -65.13% |     0.7  |       65 | 47.59%     | ok               |

## NEAR-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 242.24%  | 50.18%             | -36.62% |     1.47 |       32 | 22.22%     | ok               |
|          40 | 260.70%  | 50.18%             | -36.30% |     1.41 |       44 | 32.95%     | ok               |
|          45 | 213.02%  | 50.18%             | -39.04% |     1.3  |       46 | 28.74%     | ok               |
|          30 | 162.95%  | 50.18%             | -47.64% |     1.09 |       67 | 44.25%     | ok               |
|          35 | 152.30%  | 50.18%             | -52.16% |     1.08 |       62 | 37.16%     | ok               |

## NEM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -4.90%   | 131.83%            | -35.45% |     0.11 |       67 | 58.57%     | ok               |
|          20 | -4.57%   | 131.83%            | -30.50% |     0.1  |       71 | 54.08%     | ok               |
|          50 | -12.79%  | 131.83%            | -33.24% |    -0.06 |       48 | 37.60%     | ok               |
|          25 | -19.14%  | 131.83%            | -39.51% |    -0.12 |       68 | 51.75%     | ok               |
|          30 | -25.86%  | 131.83%            | -39.56% |    -0.25 |       70 | 49.75%     | ok               |

## NFLX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 17.55%   | -14.87%            | -20.78% |     0.48 |       54 | 37.60%     | ok               |
|          50 | 12.67%   | -14.87%            | -16.28% |     0.4  |       44 | 29.12%     | ok               |
|          35 | 11.81%   | -14.87%            | -18.30% |     0.34 |       82 | 42.76%     | ok               |
|          15 | 5.71%    | -14.87%            | -26.59% |     0.22 |       76 | 63.39%     | ok               |
|          45 | 1.42%    | -14.87%            | -18.06% |     0.12 |       58 | 33.44%     | ok               |

## NKE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -26.19%  | -55.13%            | -33.81% |    -0.49 |       69 | 32.11%     | ok               |
|          25 | -37.88%  | -55.13%            | -51.20% |    -0.56 |       87 | 52.25%     | ok               |
|          35 | -31.83%  | -55.13%            | -42.13% |    -0.57 |       75 | 39.27%     | ok               |
|          20 | -39.74%  | -55.13%            | -49.69% |    -0.59 |       90 | 55.24%     | ok               |
|          15 | -44.95%  | -55.13%            | -56.07% |    -0.7  |       91 | 59.07%     | ok               |

## NOW Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -7.07%   | -41.65%            | -49.77% |     0.14 |       73 | 57.57%     | ok               |
|          30 | -6.29%   | -41.65%            | -42.66% |     0.14 |       79 | 51.75%     | ok               |
|          25 | -10.70%  | -41.65%            | -47.93% |     0.1  |       71 | 55.24%     | ok               |
|          15 | -15.05%  | -41.65%            | -52.56% |     0.05 |       83 | 60.40%     | ok               |
|          35 | -19.01%  | -41.65%            | -48.24% |    -0.04 |       82 | 46.92%     | ok               |

## NVDA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -29.90%  | 40.36%             | -38.53% |    -0.19 |       76 | 51.52%     | ok               |
|          25 | -34.86%  | 40.36%             | -44.52% |    -0.29 |       81 | 47.59%     | ok               |
|          30 | -34.64%  | 40.36%             | -43.72% |    -0.3  |       82 | 44.74%     | ok               |
|          15 | -41.64%  | 40.36%             | -47.95% |    -0.38 |       82 | 55.79%     | ok               |
|          35 | -44.44%  | 40.36%             | -51.29% |    -0.51 |       90 | 41.89%     | ok               |

## OP-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 61.55%   | -86.14%            | -33.09% |     0.89 |       44 | 12.64%     | ok               |
|          45 | 66.61%   | -86.14%            | -30.78% |     0.83 |       46 | 18.58%     | ok               |
|          40 | 54.14%   | -86.14%            | -43.68% |     0.7  |       48 | 26.44%     | ok               |
|          35 | 8.82%    | -86.14%            | -56.85% |     0.31 |       58 | 31.23%     | ok               |
|          30 | -2.71%   | -86.14%            | -56.85% |     0.21 |       72 | 36.78%     | ok               |

## ORCL Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 123.19%  | -21.26%            | -37.59% |     0.96 |       67 | 59.07%     | ok               |
|          45 | 80.33%   | -21.26%            | -32.35% |     0.82 |       54 | 36.77%     | ok               |
|          25 | 79.45%   | -21.26%            | -31.06% |     0.77 |       59 | 51.58%     | ok               |
|          20 | 74.44%   | -21.26%            | -32.60% |     0.74 |       68 | 54.74%     | ok               |
|          35 | 70.95%   | -21.26%            | -31.95% |     0.73 |       60 | 45.76%     | ok               |

## OXY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 11.70%   | -15.44%            | -28.48% |     0.31 |       65 | 43.59%     | ok               |
|          35 | 9.82%    | -15.44%            | -26.37% |     0.28 |       70 | 38.77%     | ok               |
|          50 | 1.82%    | -15.44%            | -26.34% |     0.14 |       48 | 28.12%     | ok               |
|          40 | 0.99%    | -15.44%            | -28.30% |     0.13 |       58 | 35.27%     | ok               |
|          25 | -3.87%   | -15.44%            | -38.51% |     0.07 |       75 | 47.09%     | ok               |

## PEP Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 13.38%   | -13.77%            | -11.62% |     0.56 |       40 | 26.79%     | ok               |
|          45 | 2.07%    | -13.77%            | -14.22% |     0.13 |       54 | 30.62%     | ok               |
|          30 | 0.90%    | -13.77%            | -21.35% |     0.1  |       70 | 46.26%     | ok               |
|          35 | -0.67%   | -13.77%            | -21.42% |     0.05 |       73 | 40.60%     | ok               |
|          40 | -3.48%   | -13.77%            | -18.04% |    -0.07 |       68 | 35.94%     | ok               |

## PEPE-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -26.02%  | -62.38%            | -60.19% |     0.02 |       76 | 47.13%     | ok               |
|          15 | -36.40%  | -62.38%            | -65.53% |     0    |       83 | 62.07%     | ok               |
|          20 | -37.82%  | -62.38%            | -63.48% |    -0.08 |       89 | 57.66%     | ok               |
|          35 | -32.71%  | -62.38%            | -60.83% |    -0.12 |       68 | 43.30%     | ok               |
|          25 | -44.82%  | -62.38%            | -64.37% |    -0.21 |       90 | 52.11%     | ok               |

## PFE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -16.29%  | -1.08%             | -29.60% |    -0.54 |       42 | 19.80%     | ok               |
|          45 | -21.49%  | -1.08%             | -30.53% |    -0.67 |       54 | 23.29%     | ok               |
|          40 | -24.28%  | -1.08%             | -34.20% |    -0.74 |       76 | 28.45%     | ok               |
|          35 | -31.57%  | -1.08%             | -40.11% |    -0.97 |       86 | 34.94%     | ok               |
|          30 | -38.60%  | -1.08%             | -46.24% |    -1.19 |       81 | 37.94%     | ok               |

## PG Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -5.99%   | 3.52%              | -20.08% |    -0.17 |       52 | 31.28%     | ok               |
|          35 | -9.20%   | 3.52%              | -18.99% |    -0.28 |       60 | 34.78%     | ok               |
|          45 | -13.96%  | 3.52%              | -22.00% |    -0.51 |       52 | 28.95%     | ok               |
|          30 | -17.45%  | 3.52%              | -24.55% |    -0.59 |       62 | 37.94%     | ok               |
|          25 | -19.33%  | 3.52%              | -25.84% |    -0.66 |       74 | 39.43%     | ok               |

## PM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | -2.57%   | 79.94%             | -34.56% |     0.03 |       82 | 44.26%     | ok               |
|          20 | -4.86%   | 79.94%             | -36.03% |    -0.01 |       79 | 52.75%     | ok               |
|          30 | -5.63%   | 79.94%             | -37.61% |    -0.03 |       77 | 47.75%     | ok               |
|          50 | -9.22%   | 79.94%             | -36.94% |    -0.16 |       66 | 35.44%     | ok               |
|          25 | -12.50%  | 79.94%             | -41.68% |    -0.2  |       75 | 49.58%     | ok               |

## POL-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 10.09%   | -55.50%            | -25.31% |     0.3  |       56 | 18.77%     | ok               |
|          25 | 7.04%    | -55.50%            | -46.25% |     0.3  |       79 | 53.07%     | ok               |
|          45 | 9.23%    | -55.50%            | -30.67% |     0.29 |       54 | 26.63%     | ok               |
|          30 | 6.45%    | -55.50%            | -46.25% |     0.28 |       81 | 47.51%     | ok               |
|          20 | 3.57%    | -55.50%            | -48.58% |     0.27 |       89 | 57.47%     | ok               |

## QCOM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -20.59%  | -18.86%            | -48.54% |    -0.09 |       71 | 41.93%     | ok               |
|          20 | -26.43%  | -18.86%            | -48.40% |    -0.18 |       67 | 45.26%     | ok               |
|          35 | -27.29%  | -18.86%            | -44.11% |    -0.23 |       79 | 37.60%     | ok               |
|          15 | -35.32%  | -18.86%            | -52.43% |    -0.31 |       69 | 47.92%     | ok               |
|          30 | -35.78%  | -18.86%            | -50.90% |    -0.37 |       77 | 40.10%     | ok               |

## QQQ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 4.84%    | 32.58%             | -17.16% |     0.2  |       73 | 52.41%     | ok               |
|          25 | 1.39%    | 32.58%             | -14.05% |     0.12 |       67 | 45.26%     | ok               |
|          20 | 0.17%    | 32.58%             | -14.88% |     0.1  |       79 | 48.42%     | ok               |
|          30 | -5.45%   | 32.58%             | -15.84% |    -0.05 |       72 | 43.26%     | ok               |
|          35 | -17.64%  | 32.58%             | -20.59% |    -0.42 |       82 | 39.10%     | ok               |

## RENDER-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -9.21%   | -56.12%            | -44.12% |     0.22 |       90 | 62.45%     | ok               |
|          20 | -15.58%  | -56.12%            | -49.76% |     0.14 |       91 | 57.09%     | ok               |
|          25 | -17.54%  | -56.12%            | -49.55% |     0.11 |       85 | 52.11%     | ok               |
|          50 | -29.98%  | -56.12%            | -44.99% |    -0.37 |       60 | 17.24%     | ok               |
|          30 | -51.14%  | -56.12%            | -56.14% |    -0.4  |       88 | 46.36%     | ok               |

## RTX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 26.32%   | 93.34%             | -18.66% |     0.59 |       72 | 58.57%     | ok               |
|          25 | 23.72%   | 93.34%             | -18.59% |     0.55 |       64 | 55.91%     | ok               |
|          15 | 18.59%   | 93.34%             | -19.55% |     0.45 |       69 | 62.23%     | ok               |
|          50 | 13.31%   | 93.34%             | -18.42% |     0.43 |       62 | 39.77%     | ok               |
|          30 | 16.35%   | 93.34%             | -16.99% |     0.43 |       73 | 52.91%     | ok               |

## SBUX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -0.52%   | 39.47%             | -25.43% |     0.08 |       58 | 34.11%     | ok               |
|          25 | -2.02%   | 39.47%             | -23.55% |     0.06 |       59 | 42.60%     | ok               |
|          45 | -2.46%   | 39.47%             | -27.26% |     0.03 |       62 | 29.45%     | ok               |
|          50 | -4.97%   | 39.47%             | -25.13% |    -0.04 |       50 | 24.96%     | ok               |
|          35 | -8.08%   | 39.47%             | -26.54% |    -0.08 |       64 | 37.60%     | ok               |

## SCHW Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -3.45%   | 24.61%             | -16.53% |    -0.04 |       62 | 31.28%     | ok               |
|          20 | -6.50%   | 24.61%             | -29.24% |    -0.06 |       73 | 52.91%     | ok               |
|          50 | -3.90%   | 24.61%             | -13.28% |    -0.08 |       54 | 28.12%     | ok               |
|          25 | -7.72%   | 24.61%             | -28.76% |    -0.09 |       67 | 51.08%     | ok               |
|          15 | -12.90%  | 24.61%             | -31.37% |    -0.21 |       82 | 57.07%     | ok               |

## SHIB-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -1.07%   | -66.82%            | -27.01% |     0.12 |       48 | 17.82%     | ok               |
|          15 | -20.54%  | -66.82%            | -47.25% |    -0.05 |       85 | 65.71%     | ok               |
|          20 | -23.88%  | -66.82%            | -49.90% |    -0.11 |       78 | 61.11%     | ok               |
|          25 | -30.03%  | -66.82%            | -50.56% |    -0.22 |       78 | 57.66%     | ok               |
|          35 | -26.88%  | -66.82%            | -48.55% |    -0.22 |       79 | 44.64%     | ok               |

## SHY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd    |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:-------|---------:|---------:|:-----------|:-----------------|
|          30 | -1.90%   | 0.09%              | -3.30% |    -0.63 |       54 | 38.94%     | ok               |
|          40 | -2.13%   | 0.09%              | -3.58% |    -0.73 |       58 | 35.27%     | ok               |
|          35 | -2.43%   | 0.09%              | -3.61% |    -0.82 |       56 | 36.77%     | ok               |
|          45 | -2.20%   | 0.09%              | -3.43% |    -0.83 |       56 | 28.62%     | ok               |
|          50 | -2.20%   | 0.09%              | -3.40% |    -0.88 |       46 | 24.63%     | ok               |

## SKY-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -33.83%  | -48.08%            | -63.86% |    -0.23 |       76 | 57.09%     | ok               |
|          30 | -42.58%  | -48.08%            | -66.76% |    -0.46 |       87 | 45.98%     | ok               |
|          35 | -43.97%  | -48.08%            | -67.57% |    -0.54 |       78 | 37.74%     | ok               |
|          25 | -49.07%  | -48.08%            | -69.77% |    -0.58 |       80 | 49.23%     | ok               |
|          20 | -53.96%  | -48.08%            | -72.67% |    -0.65 |       82 | 52.87%     | ok               |

## SLB Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -10.22%  | -2.43%             | -30.97% |    -0.1  |       54 | 34.78%     | ok               |
|          45 | -10.39%  | -2.43%             | -29.29% |    -0.12 |       60 | 32.11%     | ok               |
|          50 | -8.79%   | -2.43%             | -27.89% |    -0.12 |       48 | 25.46%     | ok               |
|          35 | -30.91%  | -2.43%             | -46.64% |    -0.57 |       74 | 42.60%     | ok               |
|          25 | -34.56%  | -2.43%             | -51.35% |    -0.6  |       86 | 52.25%     | ok               |

## SLV Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 67.30%   | 39.76%             | -28.72% |     0.85 |       54 | 31.95%     | ok               |
|          45 | 64.32%   | 39.76%             | -31.33% |     0.82 |       63 | 33.78%     | ok               |
|          40 | 63.02%   | 39.76%             | -34.28% |     0.81 |       67 | 35.77%     | ok               |
|          20 | 66.89%   | 39.76%             | -37.05% |     0.8  |       70 | 46.76%     | ok               |
|          15 | 64.10%   | 39.76%             | -47.98% |     0.75 |       71 | 51.41%     | ok               |

## SMH Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 68.33%   | 70.68%             | -31.01% |     0.88 |       49 | 44.76%     | ok               |
|          25 | 53.11%   | 70.68%             | -32.94% |     0.76 |       46 | 43.26%     | ok               |
|          30 | 48.20%   | 70.68%             | -33.99% |     0.71 |       52 | 41.76%     | ok               |
|          35 | 37.17%   | 70.68%             | -34.36% |     0.61 |       58 | 39.77%     | ok               |
|          45 | 26.84%   | 70.68%             | -33.18% |     0.51 |       56 | 34.28%     | ok               |

## SNX-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | -0.21%   | -71.36%            | -44.08% |     0.2  |       50 | 29.31%     | ok               |
|          20 | -10.44%  | -71.36%            | -53.03% |     0.13 |       75 | 45.59%     | ok               |
|          40 | -2.78%   | -71.36%            | -29.01% |     0.12 |       48 | 24.90%     | ok               |
|          15 | -24.32%  | -71.36%            | -54.74% |    -0.03 |       76 | 50.00%     | ok               |
|          30 | -20.59%  | -71.36%            | -50.74% |    -0.05 |       62 | 35.82%     | ok               |

## SOL-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 72.70%   | -47.75%            | -40.41% |     0.85 |       52 | 40.04%     | ok               |
|          35 | 39.56%   | -47.75%            | -44.32% |     0.59 |       66 | 45.98%     | ok               |
|          45 | 34.88%   | -47.75%            | -47.42% |     0.58 |       50 | 33.52%     | ok               |
|          25 | 22.11%   | -47.75%            | -38.62% |     0.44 |       65 | 56.51%     | ok               |
|          30 | 16.48%   | -47.75%            | -42.98% |     0.39 |       73 | 52.49%     | ok               |

## SOXX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | 57.62%   | 65.44%             | -39.65% |     0.77 |       56 | 43.26%     | ok               |
|          30 | 53.24%   | 65.44%             | -40.14% |     0.73 |       58 | 41.10%     | ok               |
|          35 | 51.75%   | 65.44%             | -38.43% |     0.73 |       58 | 38.77%     | ok               |
|          20 | 45.72%   | 65.44%             | -38.67% |     0.66 |       61 | 44.09%     | ok               |
|          15 | 32.30%   | 65.44%             | -37.72% |     0.52 |       79 | 47.75%     | ok               |

## SPY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 2.58%    | 30.98%             | -14.25% |     0.15 |       62 | 50.08%     | ok               |
|          15 | 0.09%    | 30.98%             | -16.80% |     0.07 |       68 | 53.08%     | ok               |
|          25 | -1.63%   | 30.98%             | -14.25% |     0.01 |       60 | 48.92%     | ok               |
|          30 | -6.43%   | 30.98%             | -15.53% |    -0.17 |       63 | 46.42%     | ok               |
|          35 | -7.34%   | 30.98%             | -15.58% |    -0.21 |       61 | 43.26%     | ok               |

## SUSHI-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -36.31%  | -72.17%            | -63.59% |    -0.3  |       68 | 33.52%     | ok               |
|          35 | -40.81%  | -72.17%            | -71.33% |    -0.32 |       75 | 39.08%     | ok               |
|          50 | -29.23%  | -72.17%            | -41.50% |    -0.34 |       66 | 17.24%     | ok               |
|          45 | -35.47%  | -72.17%            | -61.12% |    -0.34 |       66 | 24.52%     | ok               |
|          15 | -60.63%  | -72.17%            | -79.80% |    -0.54 |       85 | 55.17%     | ok               |

## T Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | 64.20%   | 19.38%             | -17.66% |     1.07 |       66 | 59.40%     | ok               |
|          20 | 64.31%   | 19.38%             | -18.13% |     1.06 |       68 | 61.90%     | ok               |
|          15 | 64.92%   | 19.38%             | -15.08% |     1.04 |       73 | 66.56%     | ok               |
|          30 | 53.35%   | 19.38%             | -17.01% |     0.95 |       68 | 57.40%     | ok               |
|          35 | 35.31%   | 19.38%             | -14.49% |     0.72 |       76 | 52.75%     | ok               |

## TGT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -5.38%   | 16.15%             | -33.35% |    -0.02 |       68 | 41.60%     | ok               |
|          30 | -5.12%   | 16.15%             | -32.83% |    -0.02 |       60 | 38.27%     | ok               |
|          20 | -8.49%   | 16.15%             | -35.62% |    -0.06 |       84 | 46.09%     | ok               |
|          45 | -8.67%   | 16.15%             | -26.12% |    -0.13 |       50 | 29.78%     | ok               |
|          15 | -14.81%  | 16.15%             | -35.05% |    -0.18 |       70 | 50.92%     | ok               |

## TIA-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -39.58%  | -77.21%            | -66.94% |    -0.02 |       93 | 60.54%     | ok               |
|          20 | -44.54%  | -77.21%            | -68.67% |    -0.13 |       87 | 54.60%     | ok               |
|          25 | -42.85%  | -77.21%            | -69.36% |    -0.13 |       90 | 49.43%     | ok               |
|          35 | -35.80%  | -77.21%            | -65.55% |    -0.16 |       76 | 37.93%     | ok               |
|          30 | -50.04%  | -77.21%            | -74.75% |    -0.28 |       85 | 44.25%     | ok               |

## TLT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -6.80%   | -11.01%            | -12.00% |    -0.75 |       32 | 16.81%     | ok               |
|          40 | -14.89%  | -11.01%            | -18.39% |    -1.3  |       50 | 25.96%     | ok               |
|          45 | -13.31%  | -11.01%            | -15.44% |    -1.36 |       44 | 20.80%     | ok               |
|          30 | -22.70%  | -11.01%            | -23.34% |    -1.71 |       68 | 35.27%     | ok               |
|          35 | -21.28%  | -11.01%            | -21.92% |    -1.76 |       66 | 30.45%     | ok               |

## TMO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 45.90%   | 28.47%             | -8.17%  |     0.99 |       50 | 35.11%     | ok               |
|          45 | 44.88%   | 28.47%             | -9.69%  |     0.93 |       54 | 40.10%     | ok               |
|          40 | 37.94%   | 28.47%             | -11.54% |     0.8  |       59 | 45.26%     | ok               |
|          35 | 40.76%   | 28.47%             | -13.84% |     0.79 |       67 | 50.58%     | ok               |
|          30 | 38.81%   | 28.47%             | -18.85% |     0.74 |       67 | 56.41%     | ok               |

## TMUS Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -6.95%   | -6.78%             | -41.04% |    -0.03 |       72 | 58.57%     | ok               |
|          30 | -7.31%   | -6.78%             | -33.05% |    -0.06 |       76 | 45.59%     | ok               |
|          25 | -9.93%   | -6.78%             | -39.29% |    -0.11 |       77 | 48.59%     | ok               |
|          20 | -11.46%  | -6.78%             | -39.79% |    -0.13 |       76 | 52.75%     | ok               |
|          50 | -9.38%   | -6.78%             | -32.38% |    -0.19 |       58 | 31.78%     | ok               |

## TRX-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 12.76%   | 13.76%             | -20.10% |     0.46 |       54 | 41.19%     | ok               |
|          50 | 11.60%   | 13.76%             | -19.79% |     0.46 |       46 | 34.48%     | ok               |
|          45 | 10.55%   | 13.76%             | -24.40% |     0.42 |       48 | 36.78%     | ok               |
|          35 | 11.59%   | 13.76%             | -21.45% |     0.41 |       62 | 47.89%     | ok               |
|          30 | 9.94%    | 13.76%             | -23.08% |     0.37 |       60 | 49.81%     | ok               |

## TSLA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 25.44%   | 56.44%             | -30.57% |     0.45 |       62 | 29.62%     | ok               |
|          40 | -5.65%   | 56.44%             | -50.11% |     0.13 |       61 | 34.61%     | ok               |
|          45 | -20.66%  | 56.44%             | -52.01% |    -0.07 |       67 | 32.11%     | ok               |
|          35 | -36.74%  | 56.44%             | -58.86% |    -0.29 |       72 | 36.94%     | ok               |
|          25 | -47.35%  | 56.44%             | -54.86% |    -0.45 |       70 | 43.93%     | ok               |

## TXN Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -3.96%   | 46.37%             | -43.95% |     0.06 |       70 | 31.78%     | ok               |
|          35 | -17.67%  | 46.37%             | -42.08% |    -0.15 |       84 | 45.42%     | ok               |
|          20 | -23.53%  | 46.37%             | -37.19% |    -0.19 |       74 | 55.24%     | ok               |
|          15 | -25.27%  | 46.37%             | -38.02% |    -0.21 |       79 | 59.57%     | ok               |
|          40 | -22.70%  | 46.37%             | -44.52% |    -0.25 |       78 | 42.93%     | ok               |

## UNH Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 50.09%   | -31.40%            | -26.31% |     0.72 |       72 | 48.09%     | ok               |
|          35 | 45.31%   | -31.40%            | -27.21% |     0.68 |       67 | 43.09%     | ok               |
|          15 | 47.11%   | -31.40%            | -26.07% |     0.67 |       78 | 63.06%     | ok               |
|          20 | 44.43%   | -31.40%            | -26.96% |     0.65 |       73 | 56.74%     | ok               |
|          25 | 40.68%   | -31.40%            | -24.25% |     0.63 |       72 | 52.91%     | ok               |

## UNI-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 162.18%  | -26.35%            | -22.21% |     1.25 |       54 | 27.01%     | ok               |
|          45 | 143.85%  | -26.35%            | -31.03% |     1.12 |       58 | 34.87%     | ok               |
|          40 | 114.76%  | -26.35%            | -44.12% |     0.98 |       62 | 41.57%     | ok               |
|          35 | 86.06%   | -26.35%            | -48.64% |     0.83 |       60 | 46.17%     | ok               |
|          30 | 12.41%   | -26.35%            | -60.56% |     0.38 |       80 | 50.77%     | ok               |

## UPS Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -16.78%  | -19.95%            | -24.11% |    -0.31 |       44 | 25.29%     | ok               |
|          40 | -18.72%  | -19.95%            | -25.98% |    -0.31 |       60 | 34.78%     | ok               |
|          20 | -29.07%  | -19.95%            | -33.47% |    -0.47 |       78 | 51.41%     | ok               |
|          15 | -31.41%  | -19.95%            | -35.66% |    -0.52 |       80 | 54.91%     | ok               |
|          35 | -30.72%  | -19.95%            | -32.44% |    -0.57 |       67 | 38.94%     | ok               |

## USO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 7.42%    | 64.09%             | -39.48% |     0.25 |       67 | 42.60%     | ok               |
|          20 | 3.18%    | 64.09%             | -44.17% |     0.2  |       74 | 38.60%     | ok               |
|          45 | 1.21%    | 64.09%             | -33.59% |     0.15 |       50 | 25.62%     | ok               |
|          50 | -5.63%   | 64.09%             | -28.41% |     0.03 |       50 | 23.63%     | ok               |
|          25 | -8.20%   | 64.09%             | -45.29% |     0.03 |       74 | 35.94%     | ok               |

## VEA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 2.17%    | 30.74%             | -17.27% |     0.14 |       58 | 49.92%     | ok               |
|          20 | -1.45%   | 30.74%             | -17.78% |    -0    |       59 | 47.42%     | ok               |
|          25 | -5.88%   | 30.74%             | -18.46% |    -0.19 |       59 | 45.26%     | ok               |
|          30 | -7.02%   | 30.74%             | -18.84% |    -0.25 |       64 | 41.26%     | ok               |
|          35 | -7.67%   | 30.74%             | -17.88% |    -0.29 |       50 | 38.77%     | ok               |

## VIXY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -56.27%  | -45.41%            | -70.53% |    -0.62 |       36 | 9.15%      | ok               |
|          45 | -64.77%  | -45.41%            | -75.37% |    -0.8  |       56 | 13.98%     | ok               |
|          40 | -73.62%  | -45.41%            | -81.61% |    -0.97 |       72 | 18.14%     | ok               |
|          35 | -80.65%  | -45.41%            | -85.76% |    -1.13 |       98 | 24.96%     | ok               |
|          30 | -85.16%  | -45.41%            | -91.81% |    -1.17 |      102 | 32.28%     | ok               |

## VNQ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -8.37%   | 12.48%             | -22.16% |    -0.28 |       68 | 43.59%     | ok               |
|          45 | -9.62%   | 12.48%             | -21.23% |    -0.4  |       58 | 28.45%     | ok               |
|          50 | -9.59%   | 12.48%             | -19.34% |    -0.42 |       48 | 25.29%     | ok               |
|          30 | -12.22%  | 12.48%             | -24.92% |    -0.45 |       68 | 40.60%     | ok               |
|          20 | -13.05%  | 12.48%             | -23.83% |    -0.47 |       73 | 46.26%     | ok               |

## VTI Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 4.80%    | 31.24%             | -13.96% |     0.22 |       63 | 50.42%     | ok               |
|          15 | -2.86%   | 31.24%             | -15.70% |    -0.02 |       64 | 53.24%     | ok               |
|          25 | -5.60%   | 31.24%             | -15.00% |    -0.13 |       57 | 48.42%     | ok               |
|          40 | -9.75%   | 31.24%             | -19.77% |    -0.34 |       70 | 38.77%     | ok               |
|          35 | -11.73%  | 31.24%             | -20.22% |    -0.4  |       64 | 43.09%     | ok               |

## VWO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -9.33%   | 19.88%             | -24.01% |    -0.23 |       74 | 47.59%     | ok               |
|          20 | -9.35%   | 19.88%             | -26.14% |    -0.24 |       69 | 45.59%     | ok               |
|          45 | -10.56%  | 19.88%             | -23.26% |    -0.33 |       60 | 32.45%     | ok               |
|          40 | -11.39%  | 19.88%             | -23.57% |    -0.36 |       70 | 35.27%     | ok               |
|          50 | -14.58%  | 19.88%             | -23.68% |    -0.52 |       58 | 29.62%     | ok               |

## VZ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -3.10%   | 12.96%             | -12.96% |    -0.04 |       56 | 28.62%     | ok               |
|          20 | -22.26%  | 12.96%             | -35.02% |    -0.43 |       80 | 52.75%     | ok               |
|          25 | -19.09%  | 12.96%             | -26.32% |    -0.47 |       83 | 47.75%     | ok               |
|          35 | -18.88%  | 12.96%             | -26.97% |    -0.55 |       64 | 39.10%     | ok               |
|          45 | -18.61%  | 12.96%             | -26.23% |    -0.57 |       72 | 32.95%     | ok               |

## WFC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | -11.20%  | 31.88%             | -25.31% |    -0.18 |       75 | 43.43%     | ok               |
|          50 | -9.07%   | 31.88%             | -20.08% |    -0.23 |       56 | 32.61%     | ok               |
|          30 | -20.55%  | 31.88%             | -30.08% |    -0.36 |       80 | 46.92%     | ok               |
|          40 | -15.18%  | 31.88%             | -24.30% |    -0.38 |       68 | 39.93%     | ok               |
|          20 | -23.60%  | 31.88%             | -32.32% |    -0.39 |       80 | 53.08%     | ok               |

## WIF-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 77.46%   | -82.25%            | -40.67% |     0.75 |       67 | 51.53%     | ok               |
|          25 | 51.35%   | -82.25%            | -44.74% |     0.63 |       63 | 47.51%     | ok               |
|          15 | 38.68%   | -82.25%            | -46.21% |     0.55 |       77 | 54.79%     | ok               |
|          30 | 19.10%   | -82.25%            | -48.32% |     0.42 |       64 | 44.83%     | ok               |
|          35 | 10.98%   | -82.25%            | -52.54% |     0.34 |       62 | 38.70%     | ok               |

## WMT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 37.97%   | 89.89%             | -12.87% |     1.1  |       36 | 35.77%     | ok               |
|          45 | 36.95%   | 89.89%             | -14.82% |     1.04 |       42 | 38.27%     | ok               |
|          35 | 30.26%   | 89.89%             | -18.90% |     0.83 |       60 | 45.59%     | ok               |
|          40 | 26.88%   | 89.89%             | -19.17% |     0.78 |       52 | 40.10%     | ok               |
|          15 | 11.72%   | 89.89%             | -26.82% |     0.34 |       82 | 59.90%     | ok               |

## XBI Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 8.56%    | 61.95%             | -16.08% |     0.3  |       50 | 33.11%     | ok               |
|          45 | 4.44%    | 61.95%             | -17.35% |     0.19 |       48 | 30.62%     | ok               |
|          35 | -1.47%   | 61.95%             | -17.82% |     0.04 |       58 | 35.77%     | ok               |
|          30 | -3.53%   | 61.95%             | -19.01% |    -0.01 |       60 | 37.27%     | ok               |
|          25 | -5.00%   | 61.95%             | -24.31% |    -0.04 |       70 | 39.77%     | ok               |

## XLB Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -0.14%   | 13.72%             | -18.60% |     0.05 |       56 | 29.28%     | ok               |
|          50 | -1.24%   | 13.72%             | -16.22% |     0.01 |       40 | 24.63%     | ok               |
|          35 | -4.01%   | 13.72%             | -21.91% |    -0.08 |       56 | 32.61%     | ok               |
|          45 | -5.00%   | 13.72%             | -18.61% |    -0.14 |       40 | 26.29%     | ok               |
|          25 | -7.28%   | 13.72%             | -21.77% |    -0.19 |       62 | 38.94%     | ok               |

## XLC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 1.10%    | 20.34%             | -12.48% |     0.1  |       64 | 36.11%     | ok               |
|          30 | -0.16%   | 20.34%             | -12.33% |     0.06 |       63 | 48.25%     | ok               |
|          45 | -1.75%   | 20.34%             | -13.21% |    -0.01 |       60 | 38.94%     | ok               |
|          25 | -3.41%   | 20.34%             | -15.40% |    -0.05 |       66 | 50.75%     | ok               |
|          40 | -4.42%   | 20.34%             | -15.87% |    -0.1  |       64 | 41.93%     | ok               |

## XLE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -0.76%   | 30.82%             | -25.98% |     0.06 |       58 | 38.60%     | ok               |
|          30 | -2.78%   | 30.82%             | -34.77% |     0.01 |       72 | 48.25%     | ok               |
|          45 | -2.44%   | 30.82%             | -28.46% |     0.01 |       60 | 41.10%     | ok               |
|          20 | -7.81%   | 30.82%             | -35.29% |    -0.09 |       80 | 53.41%     | ok               |
|          15 | -9.00%   | 30.82%             | -37.43% |    -0.11 |       96 | 57.40%     | ok               |

## XLF Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 1.15%    | 33.94%             | -20.19% |     0.1  |       72 | 57.74%     | ok               |
|          20 | 0.53%    | 33.94%             | -18.63% |     0.08 |       72 | 55.07%     | ok               |
|          30 | -5.19%   | 33.94%             | -23.61% |    -0.12 |       78 | 49.75%     | ok               |
|          25 | -6.49%   | 33.94%             | -23.22% |    -0.16 |       79 | 51.91%     | ok               |
|          35 | -12.96%  | 33.94%             | -24.48% |    -0.44 |       70 | 46.26%     | ok               |

## XLI Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 1.40%    | 33.54%             | -11.06% |     0.11 |       85 | 51.41%     | ok               |
|          20 | -3.75%   | 33.54%             | -12.74% |    -0.08 |       77 | 46.42%     | ok               |
|          45 | -8.73%   | 33.54%             | -16.29% |    -0.36 |       72 | 32.95%     | ok               |
|          40 | -10.81%  | 33.54%             | -14.16% |    -0.43 |       80 | 35.61%     | ok               |
|          50 | -9.90%   | 33.54%             | -14.94% |    -0.44 |       64 | 30.45%     | ok               |

## XLK Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 46.79%   | 39.88%             | -18.51% |     0.81 |       54 | 50.75%     | ok               |
|          25 | 37.14%   | 39.88%             | -15.06% |     0.73 |       46 | 45.09%     | ok               |
|          20 | 37.67%   | 39.88%             | -19.61% |     0.72 |       56 | 47.59%     | ok               |
|          30 | 28.93%   | 39.88%             | -19.09% |     0.62 |       46 | 43.76%     | ok               |
|          35 | 13.17%   | 39.88%             | -21.79% |     0.36 |       60 | 40.93%     | ok               |

## XLM-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 19.28%   | -45.97%            | -61.51% |     0.42 |       72 | 61.30%     | ok               |
|          45 | 19.09%   | -45.97%            | -50.08% |     0.41 |       64 | 29.50%     | ok               |
|          25 | 17.92%   | -45.97%            | -53.31% |     0.4  |       75 | 52.30%     | ok               |
|          40 | 12.74%   | -45.97%            | -53.52% |     0.34 |       66 | 37.16%     | ok               |
|          35 | 3.46%    | -45.97%            | -57.46% |     0.25 |       72 | 45.40%     | ok               |

## XLP Threshold Sweep

|   threshold | return   | benchmark_return   | mdd    |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:-------|---------:|---------:|:-----------|:-----------------|
|          45 | 21.78%   | 18.24%             | -5.66% |     1.06 |       48 | 33.28%     | ok               |
|          50 | 18.91%   | 18.24%             | -6.08% |     0.96 |       54 | 31.45%     | ok               |
|          40 | 19.52%   | 18.24%             | -7.32% |     0.95 |       64 | 36.61%     | ok               |
|          35 | 16.34%   | 18.24%             | -8.39% |     0.79 |       62 | 39.60%     | ok               |
|          30 | 12.84%   | 18.24%             | -8.96% |     0.63 |       65 | 41.60%     | ok               |

## XLU Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 4.81%    | 26.61%             | -14.03% |     0.28 |       56 | 30.45%     | ok               |
|          45 | 3.66%    | 26.61%             | -14.97% |     0.22 |       60 | 31.61%     | ok               |
|          35 | 1.06%    | 26.61%             | -19.71% |     0.09 |       66 | 38.10%     | ok               |
|          40 | -0.17%   | 26.61%             | -16.41% |     0.03 |       72 | 34.44%     | ok               |
|          30 | -3.32%   | 26.61%             | -20.40% |    -0.09 |       71 | 41.60%     | ok               |

## XLV Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -19.55%  | 25.21%             | -21.39% |    -0.86 |       72 | 37.60%     | ok               |
|          25 | -20.64%  | 25.21%             | -22.46% |    -0.9  |       74 | 39.60%     | ok               |
|          20 | -24.73%  | 25.21%             | -25.35% |    -1.09 |       77 | 41.26%     | ok               |
|          15 | -25.30%  | 25.21%             | -25.92% |    -1.1  |       83 | 43.59%     | ok               |
|          35 | -23.56%  | 25.21%             | -25.29% |    -1.12 |       66 | 34.61%     | ok               |

## XLY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -9.85%   | 24.55%             | -18.78% |    -0.18 |       80 | 54.24%     | ok               |
|          20 | -14.62%  | 24.55%             | -22.30% |    -0.34 |       76 | 50.92%     | ok               |
|          30 | -14.57%  | 24.55%             | -22.09% |    -0.38 |       81 | 47.42%     | ok               |
|          50 | -11.35%  | 24.55%             | -17.00% |    -0.41 |       66 | 31.78%     | ok               |
|          25 | -18.04%  | 24.55%             | -24.54% |    -0.46 |       75 | 49.25%     | ok               |

## XOM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | 6.24%    | 36.72%             | -19.90% |     0.24 |       59 | 37.94%     | ok               |
|          30 | 5.18%    | 36.72%             | -20.29% |     0.21 |       59 | 37.27%     | ok               |
|          50 | 3.94%    | 36.72%             | -21.35% |     0.18 |       40 | 29.12%     | ok               |
|          45 | -1.68%   | 36.72%             | -23.33% |     0.03 |       44 | 30.45%     | ok               |
|          40 | -3.14%   | 36.72%             | -21.45% |    -0.01 |       54 | 33.78%     | ok               |

## XRP-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 13.62%   | -54.73%            | -36.96% |     0.35 |       74 | 44.83%     | ok               |
|          45 | 4.26%    | -54.73%            | -34.90% |     0.24 |       60 | 31.23%     | ok               |
|          20 | 1.59%    | -54.73%            | -37.30% |     0.23 |       72 | 56.13%     | ok               |
|          30 | 0.63%    | -54.73%            | -39.26% |     0.21 |       67 | 50.38%     | ok               |
|          40 | 0.65%    | -54.73%            | -38.39% |     0.2  |       70 | 37.55%     | ok               |

## YFI-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -42.19%  | -64.33%            | -55.32% |    -0.55 |       76 | 40.23%     | ok               |
|          25 | -46.07%  | -64.33%            | -58.33% |    -0.61 |       77 | 45.02%     | ok               |
|          35 | -42.90%  | -64.33%            | -50.73% |    -0.63 |       68 | 34.67%     | ok               |
|          40 | -41.75%  | -64.33%            | -47.07% |    -0.66 |       64 | 26.82%     | ok               |
|          15 | -53.65%  | -64.33%            | -65.43% |    -0.71 |       82 | 54.60%     | ok               |

## ZEC-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 237.18%  | 1800.81%           | -30.64% |     1.17 |       44 | 27.78%     | ok               |
|          35 | 148.98%  | 1800.81%           | -50.84% |     0.94 |       52 | 33.72%     | ok               |
|          50 | 132.23%  | 1800.81%           | -41.34% |     0.91 |       42 | 23.37%     | ok               |
|          40 | 138.58%  | 1800.81%           | -54.22% |     0.91 |       50 | 31.80%     | ok               |
|          30 | 115.10%  | 1800.81%           | -56.50% |     0.83 |       54 | 36.59%     | ok               |
