# Market Tracker Backtest Report

_Generated: 2026-07-29T03:46:59+00:00_

## Data Sources

- Crypto: Kraken -> Coinbase -> CoinGecko OHLC -> CoinPaprika fallback chain.
- Stocks / ETFs / indices: Stooq -> Yahoo Finance fallback chain.
- Data rows are generated from real market APIs. Mock OHLCV rows are not generated.

## Data Freshness

- Rows: **92,549**
- Symbols: **161**
- Date range: **2024-03-05** to **2026-07-29**

## Latest Signals

| symbol     | date                |         close |   composite_score | signal   | data_source   |
|:-----------|:--------------------|--------------:|------------------:|:---------|:--------------|
| AAPL       | 2026-07-28 00:00:00 |   340.08      |        69.5833    | LONG     | Yahoo Finance |
| ABBV       | 2026-07-28 00:00:00 |   263.2       |        38.25      | LONG     | Yahoo Finance |
| ADBE       | 2026-07-28 00:00:00 |   249.18      |        36.9167    | LONG     | Yahoo Finance |
| AMGN       | 2026-07-28 00:00:00 |   393.1       |        54.9167    | LONG     | Yahoo Finance |
| BLK        | 2026-07-28 00:00:00 |  1097.55      |        65.5833    | LONG     | Yahoo Finance |
| CMCSA      | 2026-07-28 00:00:00 |    24.19      |        39.25      | LONG     | Yahoo Finance |
| COP        | 2026-07-28 00:00:00 |   114.1       |        78.1667    | LONG     | Yahoo Finance |
| CVX        | 2026-07-28 00:00:00 |   187.58      |        78.1667    | LONG     | Yahoo Finance |
| DBC        | 2026-07-28 00:00:00 |    28.6       |        34.1667    | LONG     | Yahoo Finance |
| EOG        | 2026-07-28 00:00:00 |   139.64      |        65.4167    | LONG     | Yahoo Finance |
| FXI        | 2026-07-28 00:00:00 |    35.65      |        39.3333    | LONG     | Yahoo Finance |
| GE         | 2026-07-28 00:00:00 |   363.59      |        42.75      | LONG     | Yahoo Finance |
| HON        | 2026-07-28 00:00:00 |   247.05      |        70.75      | LONG     | Yahoo Finance |
| MPC        | 2026-07-28 00:00:00 |   306.05      |        67.4167    | LONG     | Yahoo Finance |
| OXY        | 2026-07-28 00:00:00 |    53.93      |        36         | LONG     | Yahoo Finance |
| PFE        | 2026-07-28 00:00:00 |    25.25      |        33.9167    | LONG     | Yahoo Finance |
| RTX        | 2026-07-28 00:00:00 |   218.58      |        65.25      | LONG     | Yahoo Finance |
| SCHW       | 2026-07-28 00:00:00 |   105.97      |        51.5833    | LONG     | Yahoo Finance |
| SHIB-USD   | 2026-07-29 00:00:00 |     4.61e-06  |        43.1667    | LONG     | Kraken API    |
| T          | 2026-07-28 00:00:00 |    24.66      |        39         | LONG     | Yahoo Finance |
| TMO        | 2026-07-28 00:00:00 |   576.41      |        62.25      | LONG     | Yahoo Finance |
| UNH        | 2026-07-28 00:00:00 |   428.79      |        49.25      | LONG     | Yahoo Finance |
| VNQ        | 2026-07-28 00:00:00 |   100.95      |        77.25      | LONG     | Yahoo Finance |
| VZ         | 2026-07-28 00:00:00 |    48.19      |        71.25      | LONG     | Yahoo Finance |
| XLE        | 2026-07-28 00:00:00 |    57.57      |        71.9167    | LONG     | Yahoo Finance |
| XLF        | 2026-07-28 00:00:00 |    57.6       |        55.25      | LONG     | Yahoo Finance |
| XLI        | 2026-07-28 00:00:00 |   182.49      |        76.0833    | LONG     | Yahoo Finance |
| XOM        | 2026-07-28 00:00:00 |   153.04      |        71.0833    | LONG     | Yahoo Finance |
| AAVE-USD   | 2026-07-29 00:00:00 |    99.24      |        27.0833    | NEUTRAL  | Kraken API    |
| ADA-USD    | 2026-07-29 00:00:00 |     0.164634  |       -35.5833    | NEUTRAL  | Kraken API    |
| ALGO-USD   | 2026-07-29 00:00:00 |     0.07926   |       -37.5833    | NEUTRAL  | Kraken API    |
| AMAT       | 2026-07-28 00:00:00 |   476.46      |       -31.5833    | NEUTRAL  | Yahoo Finance |
| AMD        | 2026-07-28 00:00:00 |   454.62      |       -35         | NEUTRAL  | Yahoo Finance |
| AVAX-USD   | 2026-07-29 00:00:00 |     6.456     |       -13         | NEUTRAL  | Kraken API    |
| AVGO       | 2026-07-28 00:00:00 |   380.91      |       -20.4167    | NEUTRAL  | Yahoo Finance |
| BA         | 2026-07-28 00:00:00 |   221.56      |        19.4167    | NEUTRAL  | Yahoo Finance |
| BAC        | 2026-07-28 00:00:00 |    62.62      |        39.1667    | NEUTRAL  | Yahoo Finance |
| BITO       | 2026-07-28 00:00:00 |     8.64      |        -7.25      | NEUTRAL  | Yahoo Finance |
| BONK-USD   | 2026-07-29 00:00:00 |     3.059e-06 |       -26.3333    | NEUTRAL  | Kraken API    |
| BTC-USD    | 2026-07-29 00:00:00 | 63793.7       |       -39.5833    | NEUTRAL  | Kraken API    |
| C          | 2026-07-28 00:00:00 |   132.47      |       -12.25      | NEUTRAL  | Yahoo Finance |
| CAT        | 2026-07-28 00:00:00 |   840.85      |       -17.3333    | NEUTRAL  | Yahoo Finance |
| CL         | 2026-07-28 00:00:00 |    92.73      |        28.8333    | NEUTRAL  | Yahoo Finance |
| COMP-USD   | 2026-07-29 00:00:00 |    15.92      |       -28.25      | NEUTRAL  | Kraken API    |
| COST       | 2026-07-28 00:00:00 |   966.58      |        60.4167    | NEUTRAL  | Yahoo Finance |
| CRM        | 2026-07-28 00:00:00 |   181.5       |        16.6667    | NEUTRAL  | Yahoo Finance |
| CRV-USD    | 2026-07-29 00:00:00 |     0.21005   |        -6.08333   | NEUTRAL  | Kraken API    |
| CSCO       | 2026-07-28 00:00:00 |   115.58      |        56.1667    | NEUTRAL  | Yahoo Finance |
| DASH-USD   | 2026-07-29 00:00:00 |    30.945     |       -66.25      | NEUTRAL  | Kraken API    |
| DE         | 2026-07-28 00:00:00 |   639.84      |        60         | NEUTRAL  | Yahoo Finance |
| DIA        | 2026-07-28 00:00:00 |   526.89      |        43.3333    | NEUTRAL  | Yahoo Finance |
| DIS        | 2026-07-28 00:00:00 |    98.89      |        -6.33333   | NEUTRAL  | Yahoo Finance |
| DOGE-USD   | 2026-07-29 00:00:00 |     0.0705194 |       -11         | NEUTRAL  | Kraken API    |
| DOT-USD    | 2026-07-29 00:00:00 |     0.7617    |       -49.5833    | NEUTRAL  | Kraken API    |
| DXY-INDEX  | 2026-07-28 00:00:00 |   101.313     |        49.4624    | NEUTRAL  | Yahoo Finance |
| EEM        | 2026-07-28 00:00:00 |    62.36      |       -12.3333    | NEUTRAL  | Yahoo Finance |
| EFA        | 2026-07-28 00:00:00 |   103.89      |        22.8333    | NEUTRAL  | Yahoo Finance |
| ETC-USD    | 2026-07-29 00:00:00 |     6.671     |       -46.5833    | NEUTRAL  | Kraken API    |
| ETH-USD    | 2026-07-29 00:00:00 |  1902.45      |        16.3333    | NEUTRAL  | Kraken API    |
| EWJ        | 2026-07-28 00:00:00 |    89.83      |       -21.5833    | NEUTRAL  | Yahoo Finance |
| FCX        | 2026-07-28 00:00:00 |    61.64      |        29.4167    | NEUTRAL  | Yahoo Finance |
| GDX        | 2026-07-28 00:00:00 |    74.21      |       -30.8333    | NEUTRAL  | Yahoo Finance |
| GDXJ       | 2026-07-28 00:00:00 |    96.78      |       -30.8333    | NEUTRAL  | Yahoo Finance |
| GLD        | 2026-07-28 00:00:00 |   369.37      |       -42.6667    | NEUTRAL  | Yahoo Finance |
| GOOGL      | 2026-07-28 00:00:00 |   333.71      |       -38.5833    | NEUTRAL  | Yahoo Finance |
| GS         | 2026-07-28 00:00:00 |  1033.34      |        -1.16667   | NEUTRAL  | Yahoo Finance |
| HBAR-USD   | 2026-07-29 00:00:00 |     0.06862   |         6.5       | NEUTRAL  | Kraken API    |
| HD         | 2026-07-28 00:00:00 |   344.47      |         8.75      | NEUTRAL  | Yahoo Finance |
| HYG        | 2026-07-28 00:00:00 |    79.42      |       -55.25      | NEUTRAL  | Yahoo Finance |
| IBIT       | 2026-07-28 00:00:00 |    36.14      |       -20         | NEUTRAL  | Yahoo Finance |
| ICP-USD    | 2026-07-29 00:00:00 |     2.095     |       -46.5833    | NEUTRAL  | Kraken API    |
| IEF        | 2026-07-28 00:00:00 |    93.56      |       -25.9167    | NEUTRAL  | Yahoo Finance |
| IEMG       | 2026-07-28 00:00:00 |    75.8       |       -12.3333    | NEUTRAL  | Yahoo Finance |
| INJ-USD    | 2026-07-29 00:00:00 |     4.59      |       -55.5       | NEUTRAL  | Kraken API    |
| INTC       | 2026-07-28 00:00:00 |    86.3       |       -23.6667    | NEUTRAL  | Yahoo Finance |
| INTU       | 2026-07-28 00:00:00 |   312.99      |        24         | NEUTRAL  | Yahoo Finance |
| ITA        | 2026-07-28 00:00:00 |   244.98      |        44.8333    | NEUTRAL  | Yahoo Finance |
| IWM        | 2026-07-28 00:00:00 |   293.37      |        15.0833    | NEUTRAL  | Yahoo Finance |
| JNJ        | 2026-07-28 00:00:00 |   266.73      |        39.8333    | NEUTRAL  | Yahoo Finance |
| JPM        | 2026-07-28 00:00:00 |   357.31      |        50.5       | NEUTRAL  | Yahoo Finance |
| KO         | 2026-07-28 00:00:00 |    88.27      |        54.5       | NEUTRAL  | Yahoo Finance |
| LDO-USD    | 2026-07-29 00:00:00 |     0.361     |        19.3333    | NEUTRAL  | Kraken API    |
| LIN        | 2026-07-28 00:00:00 |   511.18      |       -22.8333    | NEUTRAL  | Yahoo Finance |
| LINK-USD   | 2026-07-29 00:00:00 |     8.40271   |         7.41667   | NEUTRAL  | Kraken API    |
| LLY        | 2026-07-28 00:00:00 |  1220.66      |        18         | NEUTRAL  | Yahoo Finance |
| LRCX       | 2026-07-28 00:00:00 |   269.61      |       -31.5833    | NEUTRAL  | Yahoo Finance |
| LTC-USD    | 2026-07-29 00:00:00 |    46.05      |        14.3333    | NEUTRAL  | Kraken API    |
| MCD        | 2026-07-28 00:00:00 |   273.02      |       -14.6667    | NEUTRAL  | Yahoo Finance |
| MRK        | 2026-07-28 00:00:00 |   131.82      |        59.5       | NEUTRAL  | Yahoo Finance |
| MS         | 2026-07-28 00:00:00 |   211.58      |        -3.83333   | NEUTRAL  | Yahoo Finance |
| MSFT       | 2026-07-28 00:00:00 |   393.35      |        -8         | NEUTRAL  | Yahoo Finance |
| MU         | 2026-07-28 00:00:00 |   820.53      |       -20.3333    | NEUTRAL  | Yahoo Finance |
| NEAR-USD   | 2026-07-29 00:00:00 |     1.6242    |       -62.5833    | NEUTRAL  | Kraken API    |
| NEM        | 2026-07-28 00:00:00 |    91.52      |       -39.1667    | NEUTRAL  | Yahoo Finance |
| NFLX       | 2026-07-28 00:00:00 |    72.39      |       -23.25      | NEUTRAL  | Yahoo Finance |
| NKE        | 2026-07-28 00:00:00 |    43.05      |       -21.3333    | NEUTRAL  | Yahoo Finance |
| NOW        | 2026-07-28 00:00:00 |   110.62      |         3.16667   | NEUTRAL  | Yahoo Finance |
| NVDA       | 2026-07-28 00:00:00 |   197.01      |       -33.75      | NEUTRAL  | Yahoo Finance |
| PEP        | 2026-07-28 00:00:00 |   142.86      |        20.6667    | NEUTRAL  | Yahoo Finance |
| PEPE-USD   | 2026-07-29 00:00:00 |     2.766e-06 |       -11.5       | NEUTRAL  | Kraken API    |
| PG         | 2026-07-28 00:00:00 |   148.88      |        20.8333    | NEUTRAL  | Yahoo Finance |
| PM         | 2026-07-28 00:00:00 |   200.17      |        66.8333    | NEUTRAL  | Yahoo Finance |
| QQQ        | 2026-07-28 00:00:00 |   675.49      |       -15.25      | NEUTRAL  | Yahoo Finance |
| SBUX       | 2026-07-28 00:00:00 |   103.1       |        12.6667    | NEUTRAL  | Yahoo Finance |
| SHY        | 2026-07-28 00:00:00 |    81.94      |         8.91667   | NEUTRAL  | Yahoo Finance |
| SLB        | 2026-07-28 00:00:00 |    49.98      |        52         | NEUTRAL  | Yahoo Finance |
| SLV        | 2026-07-28 00:00:00 |    51.7       |       -46.6667    | NEUTRAL  | Yahoo Finance |
| SMH        | 2026-07-28 00:00:00 |   529.6       |       -14         | NEUTRAL  | Yahoo Finance |
| SOXX       | 2026-07-28 00:00:00 |   491.46      |       -16         | NEUTRAL  | Yahoo Finance |
| SPY        | 2026-07-28 00:00:00 |   740.86      |        -2.83333   | NEUTRAL  | Yahoo Finance |
| TGT        | 2026-07-28 00:00:00 |   144.2       |        64.5       | NEUTRAL  | Yahoo Finance |
| TMUS       | 2026-07-28 00:00:00 |   182.39      |       -19.8333    | NEUTRAL  | Yahoo Finance |
| TRX-USD    | 2026-07-29 00:00:00 |     0.324443  |        20.25      | NEUTRAL  | Kraken API    |
| TXN        | 2026-07-28 00:00:00 |   277.07      |       -28.5       | NEUTRAL  | Yahoo Finance |
| UNI-USD    | 2026-07-29 00:00:00 |     3.8013    |        23         | NEUTRAL  | Kraken API    |
| UPS        | 2026-07-28 00:00:00 |   105.53      |        -0.0833333 | NEUTRAL  | Yahoo Finance |
| USO        | 2026-07-28 00:00:00 |   120.49      |        28.4167    | NEUTRAL  | Yahoo Finance |
| VEA        | 2026-07-28 00:00:00 |    69.6       |       -19.5       | NEUTRAL  | Yahoo Finance |
| VIXY       | 2026-07-28 00:00:00 |    21.24      |         0.166667  | NEUTRAL  | Yahoo Finance |
| VTI        | 2026-07-28 00:00:00 |   365.99      |        -2.83333   | NEUTRAL  | Yahoo Finance |
| VWO        | 2026-07-28 00:00:00 |    57.74      |       -37.5833    | NEUTRAL  | Yahoo Finance |
| WFC        | 2026-07-28 00:00:00 |    86.87      |        22.3333    | NEUTRAL  | Yahoo Finance |
| WIF-USD    | 2026-07-29 00:00:00 |     0.1453    |       -23.5       | NEUTRAL  | Kraken API    |
| WMT        | 2026-07-28 00:00:00 |   113.1       |        -2.58333   | NEUTRAL  | Yahoo Finance |
| XBI        | 2026-07-28 00:00:00 |   149.78      |        13.0833    | NEUTRAL  | Yahoo Finance |
| XLB        | 2026-07-28 00:00:00 |    52.34      |        69.8333    | NEUTRAL  | Yahoo Finance |
| XLC        | 2026-07-28 00:00:00 |   109.67      |       -39.3333    | NEUTRAL  | Yahoo Finance |
| XLK        | 2026-07-28 00:00:00 |   171.09      |       -14         | NEUTRAL  | Yahoo Finance |
| XLM-USD    | 2026-07-29 00:00:00 |     0.172853  |       -55.25      | NEUTRAL  | Kraken API    |
| XLP        | 2026-07-28 00:00:00 |    87.06      |        70.8333    | NEUTRAL  | Yahoo Finance |
| XLU        | 2026-07-28 00:00:00 |    45.52      |        50.8333    | NEUTRAL  | Yahoo Finance |
| XLV        | 2026-07-28 00:00:00 |   167.26      |        42.3333    | NEUTRAL  | Yahoo Finance |
| XLY        | 2026-07-28 00:00:00 |   112.48      |       -59.0833    | NEUTRAL  | Yahoo Finance |
| XRP-USD    | 2026-07-29 00:00:00 |     1.07396   |       -44.5833    | NEUTRAL  | Kraken API    |
| YFI-USD    | 2026-07-29 00:00:00 |  1984.9       |       -28.6667    | NEUTRAL  | Kraken API    |
| ZEC-USD    | 2026-07-29 00:00:00 |   458.51      |       -13.5833    | NEUTRAL  | Kraken API    |
| AGG        | 2026-07-28 00:00:00 |    97.92      |       -37.0833    | SHORT    | Yahoo Finance |
| AMZN       | 2026-07-28 00:00:00 |   230.86      |       -40.5       | SHORT    | Yahoo Finance |
| APT-USD    | 2026-07-29 00:00:00 |     0.5741    |       -37.5       | SHORT    | Kraken API    |
| ARB-USD    | 2026-07-29 00:00:00 |     0.0779    |       -37         | SHORT    | Kraken API    |
| ARKK       | 2026-07-28 00:00:00 |    72.45      |       -54         | SHORT    | Yahoo Finance |
| ATOM-USD   | 2026-07-29 00:00:00 |     1.2877    |       -51.8333    | SHORT    | Kraken API    |
| BCH-USD    | 2026-07-29 00:00:00 |   213.54      |       -51.3333    | SHORT    | Kraken API    |
| BND        | 2026-07-28 00:00:00 |    72.64      |       -44.5833    | SHORT    | Yahoo Finance |
| FET-USD    | 2026-07-29 00:00:00 |     0.1358    |       -40.8333    | SHORT    | Kraken API    |
| FIL-USD    | 2026-07-29 00:00:00 |     0.69      |       -37.5       | SHORT    | Kraken API    |
| GRT-USD    | 2026-07-29 00:00:00 |     0.01492   |       -40.8333    | SHORT    | Kraken API    |
| IBM        | 2026-07-28 00:00:00 |   227.55      |       -62.5833    | SHORT    | Yahoo Finance |
| META       | 2026-07-28 00:00:00 |   593.41      |       -42.8333    | SHORT    | Yahoo Finance |
| OP-USD     | 2026-07-29 00:00:00 |     0.0886    |       -38.3333    | SHORT    | Kraken API    |
| ORCL       | 2026-07-28 00:00:00 |   119.96      |       -35.25      | SHORT    | Yahoo Finance |
| POL-USD    | 2026-07-29 00:00:00 |     0.07131   |       -40.8333    | SHORT    | Kraken API    |
| QCOM       | 2026-07-28 00:00:00 |   162.88      |       -39.0833    | SHORT    | Yahoo Finance |
| RENDER-USD | 2026-07-29 00:00:00 |     1.403     |       -35.3333    | SHORT    | Kraken API    |
| SKY-USD    | 2026-07-29 00:00:00 |     0.05736   |       -47.5       | SHORT    | Kraken API    |
| SNX-USD    | 2026-07-29 00:00:00 |     0.21      |       -31.5       | SHORT    | Kraken API    |
| SOL-USD    | 2026-07-29 00:00:00 |    73.3       |       -35.3333    | SHORT    | Kraken API    |
| SUSHI-USD  | 2026-07-29 00:00:00 |     0.1514    |       -32         | SHORT    | Kraken API    |
| TIA-USD    | 2026-07-29 00:00:00 |     0.3219    |       -53.8333    | SHORT    | Kraken API    |
| TLT        | 2026-07-28 00:00:00 |    84.24      |       -44.5833    | SHORT    | Yahoo Finance |
| TSLA       | 2026-07-28 00:00:00 |   307.44      |       -65.0833    | SHORT    | Yahoo Finance |

## Edge Summary

- Symbols with trades: **160** of 160
- Beat buy-and-hold: **32.50%** of traded symbols
- Positive return: **28.75%** of traded symbols
- Median strategy return: **-10.09%** (benchmark **15.94%**)
- Median excess vs benchmark: **-28.45%**
- Median Sharpe: **-0.14**
- Median exposure: **44.09%**

> Edge is real only if both _beat buy-and-hold_ and _median excess_ are convincingly positive across many symbols. Treat a single high-return symbol as noise.

## Portfolio Backtest

Actual capital-allocation books (not per-symbol averages). Benchmarks: `equal_weight_buyhold` (whole tracked universe), `spy_buyhold` (100% SPY), and `sixty_forty` (60% SPY / 40% AGG). `high_conf_voltarget` inverse-vol-weights the HIGH-confidence book; `conviction_long_short` is market-neutral. Judge on **Sharpe** and **max_drawdown** out-of-sample, not raw return: a fully-invested long book wins on return in a bull market but carries all the risk.

| strategy              | scope         | ann_return   | ann_vol   |   sharpe | max_drawdown   | total_return   |   avg_gross_exposure |
|:----------------------|:--------------|:-------------|:----------|---------:|:---------------|:---------------|---------------------:|
| equal_weight_buyhold  | full          | -3.87%       | 32.53%    |    -0.12 | -44.41%        | -24.44%        |                 1    |
| equal_weight_buyhold  | out_of_sample | -18.04%      | 29.38%    |    -0.61 | -35.70%        | -21.23%        |                 1    |
| all_signals_ew        | full          | -17.71%      | 26.93%    |    -0.66 | -61.37%        | -47.80%        |                 1    |
| all_signals_ew        | out_of_sample | 12.00%       | 24.21%    |     0.5  | -18.52%        | 10.19%         |                 1    |
| high_conf_ew          | full          | -3.45%       | 31.62%    |    -0.11 | -44.58%        | -22.52%        |                 0.89 |
| high_conf_ew          | out_of_sample | 1.11%        | 27.33%    |     0.04 | -20.38%        | -2.84%         |                 0.89 |
| high_conf_voltarget   | full          | -0.90%       | 29.15%    |    -0.03 | -37.38%        | -14.31%        |                 0.89 |
| high_conf_voltarget   | out_of_sample | -3.98%       | 24.13%    |    -0.16 | -16.94%        | -7.17%         |                 0.89 |
| conviction_long_short | full          | -18.06%      | 23.06%    |    -0.78 | -49.81%        | -46.80%        |                 0.97 |
| conviction_long_short | out_of_sample | -20.43%      | 24.64%    |    -0.83 | -23.96%        | -22.19%        |                 0.97 |
| spy_buyhold           | full          | 5.95%        | 13.34%    |     0.45 | -17.80%        | 16.66%         |                 0.79 |
| spy_buyhold           | out_of_sample | -3.28%       | 9.82%     |    -0.33 | -12.06%        | -3.93%         |                 0.79 |
| sixty_forty           | full          | 3.40%        | 8.44%     |     0.4  | -10.77%        | 9.69%          |                 0.79 |
| sixty_forty           | out_of_sample | -3.17%       | 6.47%     |    -0.49 | -8.26%         | -3.54%         |                 0.79 |

## Walk-Forward Robustness

Each book measured across contiguous time folds (each a different regime). A book has durable edge only if `mean_sharpe` is positive, `min_sharpe` isn't deeply negative, and `pct_positive_folds` is high — a single great fold doesn't count. `fold_sharpes` lists each fold oldest-to-newest.

| strategy              |   n_folds |   mean_sharpe |   median_sharpe |   min_sharpe | pct_positive_folds   | mean_return   | fold_sharpes                  |
|:----------------------|----------:|--------------:|----------------:|-------------:|:---------------------|:--------------|:------------------------------|
| equal_weight_buyhold  |         5 |          0.23 |            0.53 |        -0.95 | 60.00%               | -3.89%        | 1.75;-0.95;0.53;-0.89;0.70    |
| all_signals_ew        |         5 |         -0.77 |           -0.44 |        -2.49 | 20.00%               | -10.67%       | -0.23;-0.44;-2.49;0.70;-1.41  |
| high_conf_ew          |         5 |          0.05 |            0.26 |        -1.08 | 60.00%               | -3.87%        | 1.30;-1.08;-0.83;0.59;0.26    |
| high_conf_voltarget   |         5 |          0.25 |            0.46 |        -0.95 | 60.00%               | -2.13%        | 1.96;-0.73;-0.95;0.50;0.46    |
| conviction_long_short |         5 |         -0.91 |           -1.12 |        -1.56 | 0.00%                | -11.65%       | -1.50;-1.56;-0.27;-0.09;-1.12 |
| spy_buyhold           |         5 |          0.59 |            0.04 |        -0.65 | 60.00%               | 3.36%         | 1.77;0.04;2.03;-0.65;-0.27    |
| sixty_forty           |         5 |          0.52 |            0.04 |        -0.61 | 60.00%               | 1.97%         | 1.78;0.04;1.97;-0.57;-0.61    |

## Strategy Comparison

Each decision rule backtested over the same data. `out_of_sample` is the most recent ~35% of each symbol's history (unseen tail). A rule has real edge only if `median_excess` and `beat_benchmark_pct` stay positive out-of-sample, not just full-sample.

| strategy        | scope         |   symbols | beat_benchmark_pct   | positive_pct   | median_return   | median_benchmark   | median_excess   |   median_sharpe |   total_trades |
|:----------------|:--------------|----------:|:---------------------|:---------------|:----------------|:-------------------|:----------------|----------------:|---------------:|
| trend           | full          |       160 | 32.50%               | 28.75%         | -10.09%         | 15.94%             | -28.45%         |           -0.14 |          11263 |
| trend           | out_of_sample |       160 | 42.50%               | 53.12%         | 2.63%           | 4.79%              | -3.96%          |            0.31 |           3809 |
| mean_reversion  | full          |       157 | 40.76%               | 50.96%         | 0.06%           | 15.33%             | -16.82%         |            0.04 |           1260 |
| mean_reversion  | out_of_sample |       125 | 49.60%               | 59.20%         | 0.37%           | -1.09%             | -0.43%          |            0.52 |            434 |
| regime_adaptive | full          |       160 | 34.38%               | 29.38%         | -10.53%         | 15.94%             | -28.35%         |           -0.13 |          11541 |
| regime_adaptive | out_of_sample |       160 | 43.12%               | 53.75%         | 2.82%           | 4.79%              | -4.50%          |            0.31 |           3919 |

## Signal Calibration

Realized forward return in the signal's direction, grouped by confidence. HIGH should outrank LOW for the confidence score to be meaningful.

| confidence_level   |   horizon |     n | mean_return   | median_return   | win_rate   |
|:-------------------|----------:|------:|:--------------|:----------------|:-----------|
| HIGH               |         5 |  7879 | 0.08%         | 0.07%           | 51.16%     |
| MEDIUM             |         5 | 29156 | 0.01%         | 0.06%           | 50.68%     |
| LOW                |         5 |  3429 | -0.63%        | -0.56%          | 44.68%     |
| ALL                |         5 | 40464 | -0.03%        | 0.02%           | 50.27%     |
| HIGH               |        10 |  7846 | 0.33%         | 0.07%           | 50.76%     |
| MEDIUM             |        10 | 28970 | 0.15%         | 0.10%           | 50.79%     |
| LOW                |        10 |  3398 | -0.92%        | -0.74%          | 45.17%     |
| ALL                |        10 | 40214 | 0.09%         | 0.04%           | 50.31%     |
| HIGH               |        20 |  7776 | 0.70%         | 0.28%           | 52.30%     |
| MEDIUM             |        20 | 28563 | 0.78%         | 0.56%           | 53.17%     |
| LOW                |        20 |  3285 | -0.70%        | -0.54%          | 47.18%     |
| ALL                |        20 | 39624 | 0.64%         | 0.43%           | 52.50%     |

## Backtest Summary

### Data Quality / Signal Availability

- **ok**: 160 symbols

| symbol     |   trades | return   | benchmark_return   | mdd     |   sharpe | exposure   | skipped_reason   |
|:-----------|---------:|:---------|:-------------------|:--------|---------:|:-----------|:-----------------|
| AAPL       |       61 | 14.93%   | 99.91%             | -20.65% |     0.39 | 49.25%     | ok               |
| AAVE-USD   |       76 | -46.67%  | -59.90%            | -68.26% |    -0.38 | 39.66%     | ok               |
| ABBV       |       70 | -19.13%  | 46.91%             | -30.55% |    -0.39 | 46.92%     | ok               |
| ADA-USD    |       86 | -81.51%  | -78.61%            | -88.96% |    -0.62 | 46.74%     | ok               |
| ADBE       |       64 | -32.59%  | -54.27%            | -33.98% |    -0.42 | 57.07%     | ok               |
| AGG        |       69 | -6.76%   | 0.10%              | -10.17% |    -1.11 | 32.61%     | ok               |
| ALGO-USD   |       84 | -47.64%  | -69.47%            | -50.49% |    -0.51 | 37.74%     | ok               |
| AMAT       |       71 | -37.71%  | 129.74%            | -57.80% |    -0.37 | 50.92%     | ok               |
| AMD        |       54 | 1.02%    | 121.63%            | -46.54% |     0.22 | 35.77%     | ok               |
| AMGN       |       73 | -10.38%  | 42.09%             | -34.19% |    -0.15 | 46.92%     | ok               |
| AMZN       |       81 | -43.93%  | 32.59%             | -45.72% |    -1.37 | 38.60%     | ok               |
| APT-USD    |       70 | -36.45%  | -90.63%            | -66.73% |    -0.17 | 41.38%     | ok               |
| ARB-USD    |       78 | -29.89%  | -83.68%            | -62.55% |    -0.12 | 41.19%     | ok               |
| ARKK       |       87 | -33.01%  | 48.16%             | -37.98% |    -0.57 | 40.27%     | ok               |
| ATOM-USD   |       88 | -65.11%  | -73.60%            | -73.98% |    -1.04 | 45.59%     | ok               |
| AVAX-USD   |       74 | -50.26%  | -74.05%            | -60.54% |    -0.57 | 38.89%     | ok               |
| AVGO       |       62 | 19.65%   | 183.68%            | -35.76% |     0.39 | 41.60%     | ok               |
| BA         |       67 | 7.93%    | 10.15%             | -30.56% |     0.25 | 49.08%     | ok               |
| BAC        |       78 | -6.12%   | 76.94%             | -27.64% |    -0.08 | 51.08%     | ok               |
| BCH-USD    |       78 | -0.77%   | -34.91%            | -54.26% |     0.2  | 49.81%     | ok               |
| BITO       |       80 | -14.74%  | -69.64%            | -42.82% |    -0.02 | 40.10%     | ok               |
| BLK        |       81 | -9.28%   | 32.72%             | -26.90% |    -0.2  | 43.93%     | ok               |
| BND        |       67 | -7.53%   | 0.14%              | -9.98%  |    -1.2  | 34.11%     | ok               |
| BONK-USD   |       70 | 51.52%   | -80.58%            | -48.17% |     0.63 | 43.68%     | ok               |
| BTC-USD    |       74 | 5.94%    | -33.76%            | -23.38% |     0.24 | 52.30%     | ok               |
| C          |       79 | -30.57%  | 135.46%            | -38.11% |    -0.61 | 51.08%     | ok               |
| CAT        |       72 | 18.29%   | 152.11%            | -21.02% |     0.4  | 54.58%     | ok               |
| CL         |       62 | 7.01%    | 6.92%              | -14.32% |     0.29 | 44.59%     | ok               |
| CMCSA      |       79 | -45.57%  | -38.63%            | -48.22% |    -1.24 | 41.93%     | ok               |
| COMP-USD   |       93 | -33.23%  | -71.33%            | -54.23% |    -0.14 | 46.93%     | ok               |
| COP        |       72 | -22.72%  | 2.59%              | -43.96% |    -0.4  | 43.09%     | ok               |
| COST       |       60 | -4.53%   | 27.19%             | -29.73% |    -0.07 | 42.26%     | ok               |
| CRM        |       63 | -40.74%  | -39.25%            | -42.51% |    -0.87 | 42.60%     | ok               |
| CRV-USD    |       70 | -7.84%   | -58.89%            | -39.89% |     0.15 | 36.59%     | ok               |
| CSCO       |       59 | 23.34%   | 136.12%            | -21.79% |     0.51 | 47.75%     | ok               |
| CVX        |       73 | -13.92%  | 25.40%             | -29.13% |    -0.33 | 40.10%     | ok               |
| DASH-USD   |       61 | -41.76%  | 14.05%             | -64.43% |    -0.02 | 29.12%     | ok               |
| DBC        |       60 | -12.28%  | 30.00%             | -25.15% |    -0.4  | 34.94%     | ok               |
| DE         |       72 | -6.11%   | 74.47%             | -23.57% |    -0.03 | 45.92%     | ok               |
| DIA        |       60 | -3.93%   | 36.43%             | -12.94% |    -0.18 | 43.59%     | ok               |
| DIS        |       66 | -19.62%  | -12.39%            | -28.17% |    -0.37 | 44.59%     | ok               |
| DOGE-USD   |       72 | -25.02%  | -70.96%            | -62.31% |    -0.01 | 49.81%     | ok               |
| DOT-USD    |       86 | -61.03%  | -84.62%            | -66.00% |    -0.68 | 47.70%     | ok               |
| DXY-INDEX  |       42 | -1.49%   | 0.75%              | -6.02%  |    -0.22 | 32.39%     | ok               |
| EEM        |       64 | -9.15%   | 55.78%             | -25.67% |    -0.24 | 41.76%     | ok               |
| EFA        |       60 | -8.25%   | 33.78%             | -13.51% |    -0.3  | 43.26%     | ok               |
| EOG        |       81 | -22.27%  | 20.17%             | -48.13% |    -0.45 | 48.42%     | ok               |
| ETC-USD    |       64 | -34.57%  | -67.88%            | -48.09% |    -0.49 | 29.31%     | ok               |
| ETH-USD    |       64 | 143.32%  | -32.53%            | -30.11% |     1.21 | 46.36%     | ok               |
| EWJ        |       62 | -19.56%  | 27.78%             | -29.40% |    -0.65 | 37.77%     | ok               |
| FCX        |       65 | -28.89%  | 66.06%             | -47.47% |    -0.33 | 46.09%     | ok               |
| FET-USD    |       85 | -36.84%  | -82.09%            | -52.82% |    -0.11 | 41.95%     | ok               |
| FIL-USD    |       70 | -47.62%  | -79.78%            | -51.30% |    -0.6  | 33.91%     | ok               |
| FXI        |       44 | -3.00%   | 54.80%             | -23.91% |     0.01 | 29.95%     | ok               |
| GDX        |       58 | 10.31%   | 158.93%            | -34.99% |     0.29 | 47.42%     | ok               |
| GDXJ       |       64 | -21.17%  | 178.26%            | -44.93% |    -0.18 | 45.76%     | ok               |
| GE         |       76 | 8.26%    | 188.60%            | -27.82% |     0.26 | 51.75%     | ok               |
| GLD        |       50 | 23.50%   | 87.32%             | -16.63% |     0.6  | 48.09%     | ok               |
| GOOGL      |       57 | 75.05%   | 151.53%            | -20.41% |     1.14 | 52.75%     | ok               |
| GRT-USD    |       83 | 0.08%    | -89.08%            | -50.20% |     0.22 | 43.68%     | ok               |
| GS         |       76 | -1.81%   | 164.34%            | -22.13% |     0.06 | 51.41%     | ok               |
| HD         |       73 | -8.53%   | -8.98%             | -18.58% |    -0.15 | 44.43%     | ok               |
| HON        |       96 | -27.50%  | 26.64%             | -31.48% |    -0.74 | 52.75%     | ok               |
| HYG        |       81 | -9.08%   | 3.01%              | -9.59%  |    -1.06 | 33.94%     | ok               |
| IBIT       |       34 | 30.82%   | -4.92%             | -18.95% |     0.66 | 31.51%     | ok               |
| IBM        |       75 | -25.81%  | 18.55%             | -47.10% |    -0.32 | 50.25%     | ok               |
| ICP-USD    |       75 | -20.42%  | -70.31%            | -54.22% |     0.05 | 35.25%     | ok               |
| IEF        |       80 | -11.33%  | -1.28%             | -11.70% |    -1.6  | 33.78%     | ok               |
| IEMG       |       58 | -7.73%   | 50.37%             | -26.84% |    -0.21 | 41.26%     | ok               |
| INJ-USD    |       77 | -51.33%  | -71.54%            | -76.24% |    -0.47 | 38.89%     | ok               |
| INTC       |       66 | 59.37%   | 99.95%             | -60.60% |     0.64 | 48.59%     | ok               |
| INTU       |       67 | -19.54%  | -51.07%            | -42.15% |    -0.23 | 41.60%     | ok               |
| ITA        |       72 | -4.78%   | 90.28%             | -23.75% |    -0.06 | 47.09%     | ok               |
| IWM        |       48 | 9.40%    | 44.00%             | -12.83% |     0.39 | 35.77%     | ok               |
| JNJ        |       72 | 6.87%    | 66.74%             | -17.51% |     0.29 | 51.25%     | ok               |
| JPM        |       75 | -22.88%  | 89.50%             | -33.16% |    -0.57 | 52.58%     | ok               |
| KO         |       51 | 23.75%   | 48.30%             | -8.20%  |     0.85 | 37.94%     | ok               |
| LDO-USD    |       78 | 28.90%   | -78.75%            | -61.16% |     0.5  | 42.72%     | ok               |
| LIN        |       66 | -7.95%   | 10.89%             | -21.53% |    -0.23 | 37.77%     | ok               |
| LINK-USD   |       73 | -14.33%  | -52.29%            | -49.94% |     0.09 | 44.64%     | ok               |
| LLY        |       71 | -29.19%  | 56.98%             | -53.34% |    -0.44 | 48.25%     | ok               |
| LRCX       |       84 | -26.87%  | 179.94%            | -62.50% |    -0.18 | 43.26%     | ok               |
| LTC-USD    |       72 | -36.14%  | -64.54%            | -47.07% |    -0.33 | 50.19%     | ok               |
| MCD        |       75 | -2.55%   | -6.67%             | -18.81% |    -0.05 | 38.10%     | ok               |
| META       |       76 | -35.10%  | 21.05%             | -42.12% |    -0.66 | 47.42%     | ok               |
| MPC        |       69 | -9.35%   | 74.72%             | -44.76% |    -0.05 | 49.08%     | ok               |
| MRK        |       67 | -27.34%  | 7.32%              | -35.95% |    -0.63 | 43.59%     | ok               |
| MS         |       77 | -10.18%  | 137.38%            | -27.79% |    -0.16 | 49.58%     | ok               |
| MSFT       |       81 | -37.64%  | -2.31%             | -39.15% |    -0.99 | 47.09%     | ok               |
| MU         |       51 | 225.70%  | 768.56%            | -68.76% |     1.23 | 58.90%     | ok               |
| NEAR-USD   |       83 | -11.73%  | -52.62%            | -59.54% |     0.13 | 41.19%     | ok               |
| NEM        |       70 | -20.55%  | 174.51%            | -38.49% |    -0.15 | 52.75%     | ok               |
| NFLX       |       70 | 24.80%   | 20.95%             | -21.09% |     0.57 | 53.74%     | ok               |
| NKE        |       89 | -37.36%  | -56.21%            | -55.35% |    -0.52 | 43.76%     | ok               |
| NOW        |       80 | 1.54%    | -25.27%            | -26.78% |     0.18 | 45.76%     | ok               |
| NVDA       |       73 | -24.50%  | 137.24%            | -45.14% |    -0.15 | 59.54%     | ok               |
| OP-USD     |       70 | -26.73%  | -92.49%            | -71.26% |    -0.07 | 34.48%     | ok               |
| ORCL       |       68 | 139.00%  | 8.13%              | -30.61% |     1.06 | 56.07%     | ok               |
| OXY        |       71 | -1.04%   | -10.98%            | -34.15% |     0.11 | 46.92%     | ok               |
| PEP        |       75 | -4.54%   | -11.84%            | -21.35% |    -0.07 | 48.25%     | ok               |
| PEPE-USD   |       83 | -5.04%   | -70.41%            | -57.66% |     0.24 | 46.17%     | ok               |
| PFE        |       79 | -41.51%  | -3.18%             | -42.34% |    -1.34 | 36.11%     | ok               |
| PG         |       66 | -18.73%  | -6.55%             | -24.25% |    -0.71 | 38.60%     | ok               |
| PM         |       81 | -4.47%   | 121.01%            | -34.41% |    -0    | 55.41%     | ok               |
| POL-USD    |       79 | 42.50%   | -75.86%            | -46.45% |     0.61 | 49.43%     | ok               |
| QCOM       |       75 | -19.75%  | 0.89%              | -56.59% |    -0.11 | 45.59%     | ok               |
| QQQ        |       62 | 16.58%   | 54.91%             | -13.78% |     0.49 | 43.76%     | ok               |
| RENDER-USD |      100 | -18.07%  | -66.31%            | -45.00% |     0.11 | 42.15%     | ok               |
| RTX        |       54 | 42.53%   | 142.70%            | -16.99% |     0.91 | 52.91%     | ok               |
| SBUX       |       58 | -17.57%  | 13.02%             | -29.22% |    -0.31 | 39.43%     | ok               |
| SCHW       |       76 | -10.44%  | 55.61%             | -31.92% |    -0.17 | 48.92%     | ok               |
| SHIB-USD   |       76 | -27.84%  | -70.20%            | -47.96% |    -0.15 | 52.49%     | ok               |
| SHY        |       48 | -2.24%   | 0.37%              | -2.85%  |    -0.79 | 34.28%     | ok               |
| SKY-USD    |       76 | -33.72%  | -0.81%             | -47.82% |    -0.43 | 41.54%     | ok               |
| SLB        |       77 | -28.61%  | 0.64%              | -54.23% |    -0.51 | 51.41%     | ok               |
| SLV        |       62 | 44.01%   | 138.58%            | -42.66% |     0.64 | 44.26%     | ok               |
| SMH        |       48 | 69.41%   | 140.01%            | -33.99% |     0.99 | 46.42%     | ok               |
| SNX-USD    |       60 | -16.27%  | -79.08%            | -35.55% |     0.07 | 38.12%     | ok               |
| SOL-USD    |       74 | -42.52%  | -56.37%            | -56.90% |    -0.24 | 59.58%     | ok               |
| SOXX       |       55 | 65.41%   | 119.06%            | -40.34% |     0.91 | 45.42%     | ok               |
| SPY        |       62 | 1.82%    | 46.07%             | -16.47% |     0.12 | 49.25%     | ok               |
| SUSHI-USD  |      100 | -82.66%  | -82.81%            | -86.07% |    -1.32 | 37.36%     | ok               |
| T          |       66 | 40.49%   | 43.62%             | -17.01% |     0.88 | 53.58%     | ok               |
| TGT        |       60 | -21.08%  | -14.46%            | -40.57% |    -0.45 | 37.60%     | ok               |
| TIA-USD    |       91 | -36.42%  | -91.33%            | -68.36% |    -0.17 | 37.93%     | ok               |
| TLT        |       72 | -21.46%  | -11.73%            | -21.87% |    -1.65 | 33.61%     | ok               |
| TMO        |       61 | 27.89%   | -1.40%             | -18.85% |     0.6  | 52.41%     | ok               |
| TMUS       |       70 | 5.20%    | 9.94%              | -25.71% |     0.21 | 46.76%     | ok               |
| TRX-USD    |       68 | 4.26%    | 31.89%             | -22.90% |     0.2  | 48.08%     | ok               |
| TSLA       |       72 | -14.12%  | 70.10%             | -54.91% |     0.05 | 41.43%     | ok               |
| TXN        |       73 | -15.57%  | 62.37%             | -47.39% |    -0.1  | 51.75%     | ok               |
| UNH        |       74 | 25.37%   | -9.38%             | -28.69% |     0.47 | 52.91%     | ok               |
| UNI-USD    |       90 | -72.79%  | -57.91%            | -80.33% |    -0.87 | 45.98%     | ok               |
| UPS        |       72 | -41.39%  | -29.49%            | -41.62% |    -0.86 | 40.27%     | ok               |
| USO        |       68 | 10.35%   | 64.04%             | -43.35% |     0.29 | 34.94%     | ok               |
| VEA        |       56 | -0.35%   | 42.19%             | -17.93% |     0.04 | 43.59%     | ok               |
| VIXY       |       96 | -80.31%  | -62.21%            | -88.36% |    -1.02 | 32.00%     | ok               |
| VNQ        |       71 | -15.77%  | 16.95%             | -24.92% |    -0.66 | 36.94%     | ok               |
| VTI        |       68 | -4.92%   | 45.26%             | -18.77% |    -0.12 | 49.58%     | ok               |
| VWO        |       80 | -13.39%  | 40.42%             | -25.20% |    -0.47 | 42.76%     | ok               |
| VZ         |       85 | -24.53%  | 19.43%             | -26.56% |    -0.79 | 37.77%     | ok               |
| WFC        |       84 | -19.28%  | 53.48%             | -29.78% |    -0.33 | 50.08%     | ok               |
| WIF-USD    |       70 | -51.48%  | -77.96%            | -60.60% |    -0.37 | 33.72%     | ok               |
| WMT        |       65 | 11.28%   | 88.37%             | -21.31% |     0.37 | 49.75%     | ok               |
| XBI        |       66 | -8.17%   | 50.59%             | -18.30% |    -0.13 | 40.10%     | ok               |
| XLB        |       62 | -9.99%   | 18.78%             | -25.37% |    -0.32 | 36.11%     | ok               |
| XLC        |       67 | 11.88%   | 40.01%             | -12.33% |     0.44 | 52.75%     | ok               |
| XLE        |       75 | -9.20%   | 32.57%             | -37.64% |    -0.16 | 45.26%     | ok               |
| XLF        |       78 | -9.57%   | 42.57%             | -23.61% |    -0.3  | 48.09%     | ok               |
| XLI        |       68 | -2.81%   | 50.87%             | -11.79% |    -0.06 | 43.76%     | ok               |
| XLK        |       40 | 65.83%   | 66.45%             | -14.75% |     1.22 | 45.59%     | ok               |
| XLM-USD    |       67 | 11.39%   | -48.09%            | -50.36% |     0.34 | 45.59%     | ok               |
| XLP        |       66 | 4.67%    | 16.55%             | -11.16% |     0.3  | 41.26%     | ok               |
| XLU        |       67 | -5.24%   | 45.48%             | -20.40% |    -0.19 | 39.10%     | ok               |
| XLV        |       68 | -14.30%  | 15.33%             | -18.96% |    -0.7  | 35.11%     | ok               |
| XLY        |       66 | 8.22%    | 24.80%             | -14.01% |     0.32 | 44.43%     | ok               |
| XOM        |       55 | 8.53%    | 44.87%             | -20.29% |     0.3  | 37.60%     | ok               |
| XRP-USD    |       54 | -22.96%  | -58.31%            | -38.94% |    -0.14 | 33.14%     | ok               |
| YFI-USD    |       81 | -64.19%  | -66.74%            | -71.12% |    -1.03 | 40.61%     | ok               |
| ZEC-USD    |       64 | 38.08%   | 1175.06%           | -48.77% |     0.53 | 36.97%     | ok               |

## AAPL Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 23.91%   | 99.91%             | -21.71% |     0.53 |       68 | 53.41%     | ok               |
|          15 | 20.10%   | 99.91%             | -23.86% |     0.46 |       75 | 60.57%     | ok               |
|          30 | 14.93%   | 99.91%             | -20.65% |     0.39 |       61 | 49.25%     | ok               |
|          35 | 12.35%   | 99.91%             | -22.04% |     0.34 |       61 | 47.75%     | ok               |
|          25 | 12.54%   | 99.91%             | -20.03% |     0.34 |       67 | 51.08%     | ok               |

## AAVE-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 16.40%   | -59.90%            | -43.61% |     0.39 |       42 | 32.38%     | ok               |
|          35 | -3.52%   | -59.90%            | -51.96% |     0.19 |       52 | 35.63%     | ok               |
|          45 | -4.67%   | -59.90%            | -49.19% |     0.15 |       44 | 27.20%     | ok               |
|          15 | -50.07%  | -59.90%            | -61.76% |    -0.29 |       82 | 53.83%     | ok               |
|          50 | -33.87%  | -59.90%            | -47.39% |    -0.36 |       42 | 19.73%     | ok               |

## ABBV Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -13.07%  | 46.91%             | -28.51% |    -0.27 |       50 | 35.44%     | ok               |
|          25 | -19.23%  | 46.91%             | -31.26% |    -0.39 |       69 | 48.75%     | ok               |
|          30 | -19.13%  | 46.91%             | -30.55% |    -0.39 |       70 | 46.92%     | ok               |
|          20 | -19.85%  | 46.91%             | -30.60% |    -0.4  |       69 | 50.58%     | ok               |
|          40 | -20.23%  | 46.91%             | -26.61% |    -0.47 |       66 | 40.10%     | ok               |

## ADA-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -79.78%  | -78.61%            | -87.96% |    -0.61 |       60 | 31.99%     | ok               |
|          35 | -81.23%  | -78.61%            | -89.66% |    -0.61 |       78 | 42.72%     | ok               |
|          50 | -78.58%  | -78.61%            | -86.38% |    -0.61 |       59 | 27.39%     | ok               |
|          30 | -81.51%  | -78.61%            | -88.96% |    -0.62 |       86 | 46.74%     | ok               |
|          40 | -82.33%  | -78.61%            | -89.67% |    -0.68 |       76 | 37.55%     | ok               |

## ADBE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 2.79%    | -54.27%            | -21.34% |     0.17 |       72 | 49.25%     | ok               |
|          40 | -10.53%  | -54.27%            | -24.87% |    -0.08 |       70 | 42.26%     | ok               |
|          25 | -22.01%  | -54.27%            | -30.06% |    -0.2  |       50 | 60.73%     | ok               |
|          20 | -29.81%  | -54.27%            | -33.21% |    -0.34 |       54 | 63.39%     | ok               |
|          15 | -33.01%  | -54.27%            | -37.26% |    -0.39 |       63 | 65.22%     | ok               |

## AGG Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -5.08%   | 0.10%              | -7.92%  |    -1.11 |       50 | 17.97%     | ok               |
|          45 | -5.64%   | 0.10%              | -7.91%  |    -1.11 |       54 | 22.46%     | ok               |
|          30 | -6.76%   | 0.10%              | -10.17% |    -1.11 |       69 | 32.61%     | ok               |
|          20 | -8.09%   | 0.10%              | -11.30% |    -1.18 |       71 | 37.94%     | ok               |
|          25 | -8.26%   | 0.10%              | -11.94% |    -1.26 |       71 | 36.27%     | ok               |

## ALGO-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -47.64%  | -69.47%            | -50.49% |    -0.51 |       84 | 37.74%     | ok               |
|          25 | -59.75%  | -69.47%            | -72.48% |    -0.68 |       82 | 44.64%     | ok               |
|          15 | -62.02%  | -69.47%            | -69.75% |    -0.68 |       84 | 50.00%     | ok               |
|          20 | -63.60%  | -69.47%            | -71.20% |    -0.75 |       84 | 47.70%     | ok               |
|          35 | -53.24%  | -69.47%            | -53.24% |    -0.75 |       62 | 31.23%     | ok               |

## AMAT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -25.57%  | 129.74%            | -54.01% |    -0.13 |       68 | 59.73%     | ok               |
|          30 | -37.71%  | 129.74%            | -57.80% |    -0.37 |       71 | 50.92%     | ok               |
|          35 | -38.15%  | 129.74%            | -55.89% |    -0.4  |       73 | 48.59%     | ok               |
|          50 | -37.13%  | 129.74%            | -48.72% |    -0.43 |       52 | 36.61%     | ok               |
|          20 | -44.04%  | 129.74%            | -60.13% |    -0.46 |       74 | 56.07%     | ok               |

## AMD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 1.02%    | 121.63%            | -46.54% |     0.22 |       54 | 35.77%     | ok               |
|          50 | 1.86%    | 121.63%            | -46.81% |     0.22 |       56 | 30.62%     | ok               |
|          35 | -5.85%   | 121.63%            | -50.91% |     0.15 |       62 | 37.44%     | ok               |
|          30 | -18.27%  | 121.63%            | -56.64% |     0.02 |       63 | 39.93%     | ok               |
|          45 | -18.69%  | 121.63%            | -55.38% |    -0.01 |       62 | 33.44%     | ok               |

## AMGN Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -5.49%   | 42.09%             | -26.65% |    -0.02 |       71 | 52.91%     | ok               |
|          35 | -6.00%   | 42.09%             | -31.29% |    -0.05 |       69 | 43.09%     | ok               |
|          15 | -9.69%   | 42.09%             | -27.98% |    -0.11 |       68 | 57.74%     | ok               |
|          30 | -10.38%  | 42.09%             | -34.19% |    -0.15 |       73 | 46.92%     | ok               |
|          25 | -12.93%  | 42.09%             | -33.47% |    -0.21 |       67 | 49.42%     | ok               |

## AMZN Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -21.73%  | 32.59%             | -28.96% |    -0.67 |       54 | 29.12%     | ok               |
|          50 | -26.31%  | 32.59%             | -34.08% |    -0.96 |       48 | 22.63%     | ok               |
|          45 | -30.78%  | 32.59%             | -35.71% |    -1.12 |       54 | 25.79%     | ok               |
|          35 | -37.59%  | 32.59%             | -39.82% |    -1.23 |       70 | 32.95%     | ok               |
|          30 | -43.93%  | 32.59%             | -45.72% |    -1.37 |       81 | 38.60%     | ok               |

## APT-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 19.10%   | -90.63%            | -46.73% |     0.42 |       40 | 18.97%     | ok               |
|          45 | -11.65%  | -90.63%            | -63.86% |     0.05 |       56 | 24.52%     | ok               |
|          20 | -28.79%  | -90.63%            | -68.96% |    -0.03 |       73 | 50.00%     | ok               |
|          35 | -25.50%  | -90.63%            | -60.63% |    -0.07 |       64 | 35.25%     | ok               |
|          40 | -29.96%  | -90.63%            | -63.33% |    -0.16 |       62 | 29.69%     | ok               |

## ARB-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 56.77%   | -83.68%            | -51.09% |     0.65 |       88 | 57.66%     | ok               |
|          20 | 5.77%    | -83.68%            | -58.28% |     0.33 |       74 | 51.34%     | ok               |
|          40 | -1.61%   | -83.68%            | -45.32% |     0.2  |       58 | 31.80%     | ok               |
|          25 | -11.20%  | -83.68%            | -55.53% |     0.17 |       76 | 47.13%     | ok               |
|          45 | -3.87%   | -83.68%            | -47.43% |     0.16 |       60 | 24.14%     | ok               |

## ARKK Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -27.27%  | 48.16%             | -37.76% |    -0.33 |       94 | 51.91%     | ok               |
|          20 | -31.56%  | 48.16%             | -37.99% |    -0.45 |       89 | 47.25%     | ok               |
|          30 | -33.01%  | 48.16%             | -37.98% |    -0.57 |       87 | 40.27%     | ok               |
|          35 | -35.26%  | 48.16%             | -38.33% |    -0.66 |       86 | 37.60%     | ok               |
|          40 | -36.63%  | 48.16%             | -39.63% |    -0.74 |       78 | 32.78%     | ok               |

## ATOM-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -64.05%  | -73.60%            | -69.82% |    -0.84 |       87 | 62.26%     | ok               |
|          25 | -61.53%  | -73.60%            | -71.09% |    -0.86 |       93 | 52.30%     | ok               |
|          45 | -57.67%  | -73.60%            | -67.17% |    -1.03 |       74 | 29.89%     | ok               |
|          30 | -65.11%  | -73.60%            | -73.98% |    -1.04 |       88 | 45.59%     | ok               |
|          20 | -69.08%  | -73.60%            | -74.75% |    -1.06 |       95 | 55.56%     | ok               |

## AVAX-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 3.29%    | -74.05%            | -34.50% |     0.21 |       32 | 18.20%     | ok               |
|          45 | -6.13%   | -74.05%            | -41.07% |     0.07 |       36 | 22.03%     | ok               |
|          40 | -15.64%  | -74.05%            | -45.60% |    -0.06 |       42 | 25.10%     | ok               |
|          15 | -37.12%  | -74.05%            | -49.09% |    -0.21 |       74 | 53.07%     | ok               |
|          35 | -31.97%  | -74.05%            | -48.39% |    -0.28 |       56 | 31.03%     | ok               |

## AVGO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 21.51%   | 183.68%            | -35.84% |     0.41 |       56 | 30.28%     | ok               |
|          30 | 19.65%   | 183.68%            | -35.76% |     0.39 |       62 | 41.60%     | ok               |
|          40 | 18.22%   | 183.68%            | -40.70% |     0.37 |       60 | 35.44%     | ok               |
|          25 | 17.13%   | 183.68%            | -38.01% |     0.36 |       70 | 43.09%     | ok               |
|          45 | 16.56%   | 183.68%            | -41.66% |     0.36 |       56 | 33.61%     | ok               |

## BA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 26.03%   | 10.15%             | -13.34% |     0.67 |       42 | 31.45%     | ok               |
|          35 | 30.93%   | 10.15%             | -23.77% |     0.6  |       70 | 44.43%     | ok               |
|          40 | 20.11%   | 10.15%             | -23.90% |     0.47 |       46 | 38.60%     | ok               |
|          25 | 10.92%   | 10.15%             | -32.48% |     0.3  |       70 | 52.41%     | ok               |
|          30 | 7.93%    | 10.15%             | -30.56% |     0.25 |       67 | 49.08%     | ok               |

## BAC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 0.06%    | 76.94%             | -21.48% |     0.09 |       80 | 55.74%     | ok               |
|          35 | -1.14%   | 76.94%             | -29.13% |     0.04 |       70 | 47.25%     | ok               |
|          45 | -0.84%   | 76.94%             | -22.29% |     0.04 |       64 | 38.60%     | ok               |
|          15 | -5.57%   | 76.94%             | -23.70% |    -0.04 |       80 | 60.73%     | ok               |
|          25 | -4.87%   | 76.94%             | -27.14% |    -0.04 |       80 | 53.74%     | ok               |

## BCH-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -0.77%   | -34.91%            | -54.26% |     0.2  |       78 | 49.81%     | ok               |
|          15 | -7.48%   | -34.91%            | -54.40% |     0.17 |       74 | 59.58%     | ok               |
|          20 | -10.78%  | -34.91%            | -54.70% |     0.13 |       72 | 55.94%     | ok               |
|          40 | -16.29%  | -34.91%            | -61.24% |    -0.02 |       67 | 41.00%     | ok               |
|          25 | -22.33%  | -34.91%            | -61.06% |    -0.02 |       73 | 52.11%     | ok               |

## BITO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 2.43%    | -69.64%            | -31.98% |     0.18 |       52 | 23.29%     | ok               |
|          30 | -14.74%  | -69.64%            | -42.82% |    -0.02 |       80 | 40.10%     | ok               |
|          15 | -21.02%  | -69.64%            | -48.38% |    -0.06 |       89 | 49.08%     | ok               |
|          45 | -13.83%  | -69.64%            | -41.96% |    -0.06 |       60 | 26.96%     | ok               |
|          40 | -17.68%  | -69.64%            | -44.44% |    -0.1  |       64 | 31.78%     | ok               |

## BLK Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -1.95%   | 32.72%             | -21.48% |     0.03 |       82 | 48.59%     | ok               |
|          35 | -3.20%   | 32.72%             | -20.79% |    -0.03 |       88 | 40.10%     | ok               |
|          40 | -5.03%   | 32.72%             | -22.83% |    -0.1  |       80 | 35.77%     | ok               |
|          25 | -6.86%   | 32.72%             | -24.62% |    -0.12 |       77 | 46.59%     | ok               |
|          30 | -9.28%   | 32.72%             | -26.90% |    -0.2  |       81 | 43.93%     | ok               |

## BND Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -6.72%   | 0.14%              | -9.43%  |    -0.97 |       64 | 39.43%     | ok               |
|          25 | -7.41%   | 0.14%              | -10.55% |    -1.12 |       67 | 37.44%     | ok               |
|          30 | -7.53%   | 0.14%              | -9.98%  |    -1.2  |       67 | 34.11%     | ok               |
|          15 | -8.97%   | 0.14%              | -11.30% |    -1.29 |       76 | 42.26%     | ok               |
|          45 | -7.43%   | 0.14%              | -9.57%  |    -1.41 |       52 | 23.96%     | ok               |

## BONK-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 166.69%  | -80.58%            | -35.57% |     1.22 |       52 | 22.80%     | ok               |
|          25 | 148.14%  | -80.58%            | -51.34% |     0.98 |       67 | 49.43%     | ok               |
|          15 | 148.81%  | -80.58%            | -62.48% |     0.95 |       72 | 58.05%     | ok               |
|          20 | 116.89%  | -80.58%            | -58.35% |     0.88 |       67 | 53.64%     | ok               |
|          40 | 72.30%   | -80.58%            | -53.34% |     0.74 |       56 | 36.02%     | ok               |

## BTC-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 55.68%   | -33.76%            | -14.50% |     1    |       44 | 34.29%     | ok               |
|          45 | 40.86%   | -33.76%            | -13.36% |     0.81 |       44 | 30.65%     | ok               |
|          35 | 39.46%   | -33.76%            | -21.56% |     0.75 |       68 | 41.19%     | ok               |
|          30 | 22.71%   | -33.76%            | -21.75% |     0.49 |       72 | 47.89%     | ok               |
|          50 | 14.00%   | -33.76%            | -18.05% |     0.4  |       42 | 25.29%     | ok               |

## C Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -6.29%   | 135.46%            | -22.28% |    -0.1  |       64 | 36.11%     | ok               |
|          45 | -18.56%  | 135.46%            | -30.30% |    -0.43 |       76 | 40.27%     | ok               |
|          25 | -27.45%  | 135.46%            | -35.32% |    -0.52 |       71 | 53.08%     | ok               |
|          15 | -30.55%  | 135.46%            | -37.28% |    -0.56 |       74 | 60.40%     | ok               |
|          40 | -24.27%  | 135.46%            | -35.18% |    -0.56 |       76 | 42.60%     | ok               |

## CAT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 18.29%   | 152.11%            | -21.02% |     0.4  |       72 | 54.58%     | ok               |
|          25 | 18.39%   | 152.11%            | -26.37% |     0.4  |       68 | 57.40%     | ok               |
|          20 | 16.98%   | 152.11%            | -25.65% |     0.38 |       78 | 60.90%     | ok               |
|          45 | 13.45%   | 152.11%            | -27.12% |     0.34 |       56 | 43.26%     | ok               |
|          15 | 11.93%   | 152.11%            | -30.60% |     0.31 |       75 | 67.55%     | ok               |

## CL Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 9.65%    | 6.92%              | -11.22% |     0.43 |       44 | 28.45%     | ok               |
|          30 | 7.01%    | 6.92%              | -14.32% |     0.29 |       62 | 44.59%     | ok               |
|          45 | 2.56%    | 6.92%              | -13.51% |     0.15 |       48 | 31.61%     | ok               |
|          35 | 1.91%    | 6.92%              | -13.83% |     0.13 |       64 | 40.93%     | ok               |
|          40 | -1.04%   | 6.92%              | -12.70% |     0.02 |       58 | 35.61%     | ok               |

## CMCSA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -44.05%  | -38.63%            | -46.06% |    -1.03 |       90 | 56.91%     | ok               |
|          30 | -45.57%  | -38.63%            | -48.22% |    -1.24 |       79 | 41.93%     | ok               |
|          50 | -31.69%  | -38.63%            | -33.36% |    -1.27 |       46 | 14.14%     | ok               |
|          35 | -45.73%  | -38.63%            | -48.07% |    -1.35 |       92 | 36.27%     | ok               |
|          25 | -48.92%  | -38.63%            | -50.38% |    -1.35 |       88 | 47.25%     | ok               |

## COMP-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -6.30%   | -71.33%            | -38.71% |     0.11 |       48 | 20.88%     | ok               |
|          30 | -33.23%  | -71.33%            | -54.23% |    -0.14 |       93 | 46.93%     | ok               |
|          25 | -41.86%  | -71.33%            | -57.94% |    -0.25 |       93 | 53.26%     | ok               |
|          45 | -38.19%  | -71.33%            | -50.78% |    -0.33 |       62 | 29.12%     | ok               |
|          40 | -39.43%  | -71.33%            | -50.85% |    -0.33 |       72 | 34.87%     | ok               |

## COP Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -5.87%   | 2.59%              | -35.08% |    -0.05 |       48 | 28.95%     | ok               |
|          35 | -18.49%  | 2.59%              | -43.58% |    -0.3  |       73 | 39.60%     | ok               |
|          45 | -16.99%  | 2.59%              | -41.35% |    -0.32 |       62 | 32.28%     | ok               |
|          30 | -22.72%  | 2.59%              | -43.96% |    -0.4  |       72 | 43.09%     | ok               |
|          40 | -22.23%  | 2.59%              | -47.05% |    -0.44 |       68 | 35.44%     | ok               |

## COST Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 6.51%    | 27.19%             | -24.32% |     0.25 |       66 | 48.75%     | ok               |
|          25 | 4.93%    | 27.19%             | -24.73% |     0.21 |       63 | 45.92%     | ok               |
|          35 | 0.05%    | 27.19%             | -26.58% |     0.07 |       54 | 39.27%     | ok               |
|          30 | -4.53%   | 27.19%             | -29.73% |    -0.07 |       60 | 42.26%     | ok               |
|          15 | -7.40%   | 27.19%             | -27.30% |    -0.12 |       69 | 52.25%     | ok               |

## CRM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -37.02%  | -39.25%            | -44.67% |    -0.6  |       90 | 55.07%     | ok               |
|          35 | -31.01%  | -39.25%            | -34.39% |    -0.63 |       60 | 37.77%     | ok               |
|          40 | -36.11%  | -39.25%            | -40.30% |    -0.84 |       66 | 33.78%     | ok               |
|          20 | -44.44%  | -39.25%            | -46.73% |    -0.86 |       74 | 48.75%     | ok               |
|          30 | -40.74%  | -39.25%            | -42.51% |    -0.87 |       63 | 42.60%     | ok               |

## CRV-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 16.06%   | -58.89%            | -37.78% |     0.38 |       72 | 31.99%     | ok               |
|          45 | 1.84%    | -58.89%            | -42.29% |     0.22 |       58 | 21.26%     | ok               |
|          40 | -3.85%   | -58.89%            | -38.86% |     0.17 |       62 | 27.59%     | ok               |
|          50 | -1.99%   | -58.89%            | -29.30% |     0.16 |       48 | 17.62%     | ok               |
|          30 | -7.84%   | -58.89%            | -39.89% |     0.15 |       70 | 36.59%     | ok               |

## CSCO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 35.16%   | 136.12%            | -19.34% |     0.75 |       48 | 36.61%     | ok               |
|          45 | 30.59%   | 136.12%            | -19.34% |     0.66 |       49 | 38.27%     | ok               |
|          35 | 25.61%   | 136.12%            | -23.68% |     0.55 |       51 | 45.09%     | ok               |
|          25 | 23.92%   | 136.12%            | -23.28% |     0.52 |       63 | 49.75%     | ok               |
|          30 | 23.34%   | 136.12%            | -21.79% |     0.51 |       59 | 47.75%     | ok               |

## CVX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -8.60%   | 25.40%             | -27.34% |    -0.19 |       75 | 35.44%     | ok               |
|          25 | -10.32%  | 25.40%             | -24.33% |    -0.2  |       73 | 42.76%     | ok               |
|          35 | -10.72%  | 25.40%             | -28.85% |    -0.24 |       67 | 37.60%     | ok               |
|          45 | -10.22%  | 25.40%             | -28.83% |    -0.25 |       65 | 31.78%     | ok               |
|          30 | -13.92%  | 25.40%             | -29.13% |    -0.33 |       73 | 40.10%     | ok               |

## DASH-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 97.15%   | 14.05%             | -31.64% |     0.83 |       38 | 15.52%     | ok               |
|          40 | 58.92%   | 14.05%             | -31.16% |     0.64 |       44 | 21.84%     | ok               |
|          45 | 42.14%   | 14.05%             | -39.91% |     0.55 |       42 | 17.62%     | ok               |
|          35 | -38.60%  | 14.05%             | -63.23% |     0.01 |       67 | 26.25%     | ok               |
|          30 | -41.76%  | 14.05%             | -64.43% |    -0.02 |       61 | 29.12%     | ok               |

## DBC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -7.05%   | 30.00%             | -26.53% |    -0.18 |       72 | 40.43%     | ok               |
|          50 | -6.89%   | 30.00%             | -20.31% |    -0.23 |       42 | 22.96%     | ok               |
|          35 | -9.59%   | 30.00%             | -23.35% |    -0.29 |       62 | 33.61%     | ok               |
|          25 | -10.03%  | 30.00%             | -25.55% |    -0.3  |       62 | 36.77%     | ok               |
|          45 | -9.47%   | 30.00%             | -21.46% |    -0.31 |       58 | 26.62%     | ok               |

## DE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -2.78%   | 74.47%             | -21.47% |     0.01 |       66 | 30.95%     | ok               |
|          45 | -4.78%   | 74.47%             | -25.22% |    -0.03 |       66 | 35.44%     | ok               |
|          30 | -6.11%   | 74.47%             | -23.57% |    -0.03 |       72 | 45.92%     | ok               |
|          20 | -7.06%   | 74.47%             | -29.90% |    -0.05 |       76 | 51.58%     | ok               |
|          25 | -9.43%   | 74.47%             | -27.71% |    -0.11 |       78 | 48.75%     | ok               |

## DIA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | -1.90%   | 36.43%             | -13.15% |    -0.07 |       60 | 41.43%     | ok               |
|          25 | -2.43%   | 36.43%             | -11.28% |    -0.09 |       60 | 44.76%     | ok               |
|          30 | -3.93%   | 36.43%             | -12.94% |    -0.18 |       60 | 43.59%     | ok               |
|          20 | -5.84%   | 36.43%             | -13.85% |    -0.27 |       66 | 47.25%     | ok               |
|          40 | -5.90%   | 36.43%             | -15.06% |    -0.32 |       66 | 38.60%     | ok               |

## DIS Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 15.44%   | -12.39%            | -14.24% |     0.51 |       48 | 26.12%     | ok               |
|          40 | -9.52%   | -12.39%            | -22.74% |    -0.13 |       67 | 35.11%     | ok               |
|          45 | -8.64%   | -12.39%            | -16.54% |    -0.14 |       53 | 29.95%     | ok               |
|          15 | -17.84%  | -12.39%            | -31.15% |    -0.26 |       91 | 56.07%     | ok               |
|          35 | -16.34%  | -12.39%            | -25.70% |    -0.29 |       77 | 41.43%     | ok               |

## DOGE-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 5.36%    | -70.96%            | -59.36% |     0.33 |       78 | 65.52%     | ok               |
|          25 | -10.38%  | -70.96%            | -55.33% |     0.17 |       69 | 55.36%     | ok               |
|          20 | -13.31%  | -70.96%            | -57.37% |     0.15 |       81 | 60.54%     | ok               |
|          30 | -25.02%  | -70.96%            | -62.31% |    -0.01 |       72 | 49.81%     | ok               |
|          35 | -47.23%  | -70.96%            | -61.79% |    -0.41 |       68 | 43.49%     | ok               |

## DOT-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -36.94%  | -84.62%            | -48.37% |    -0.49 |       58 | 25.86%     | ok               |
|          45 | -39.69%  | -84.62%            | -51.57% |    -0.5  |       50 | 31.03%     | ok               |
|          35 | -56.64%  | -84.62%            | -62.33% |    -0.6  |       76 | 41.38%     | ok               |
|          40 | -48.55%  | -84.62%            | -55.65% |    -0.65 |       54 | 34.10%     | ok               |
|          30 | -61.03%  | -84.62%            | -66.00% |    -0.68 |       86 | 47.70%     | ok               |

## DXY-INDEX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -1.49%   | 0.75%              | -6.02%  |    -0.22 |       42 | 32.39%     | ok               |
|          40 | -2.81%   | 0.75%              | -7.30%  |    -0.34 |       68 | 50.65%     | ok               |
|          15 | -5.18%   | 0.75%              | -11.37% |    -0.48 |       84 | 76.74%     | ok               |
|          35 | -4.31%   | 0.75%              | -9.74%  |    -0.52 |       73 | 56.96%     | ok               |
|          30 | -4.71%   | 0.75%              | -9.61%  |    -0.53 |       72 | 61.52%     | ok               |

## EEM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -4.70%   | 55.78%             | -19.52% |    -0.1  |       64 | 38.10%     | ok               |
|          50 | -4.62%   | 55.78%             | -15.88% |    -0.11 |       50 | 34.11%     | ok               |
|          35 | -5.36%   | 55.78%             | -23.88% |    -0.11 |       66 | 40.10%     | ok               |
|          45 | -5.72%   | 55.78%             | -17.36% |    -0.15 |       52 | 35.77%     | ok               |
|          30 | -9.15%   | 55.78%             | -25.67% |    -0.24 |       64 | 41.76%     | ok               |

## EFA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -3.38%   | 33.78%             | -10.80% |    -0.06 |       62 | 51.25%     | ok               |
|          30 | -8.25%   | 33.78%             | -13.51% |    -0.3  |       60 | 43.26%     | ok               |
|          20 | -10.08%  | 33.78%             | -12.73% |    -0.35 |       69 | 48.25%     | ok               |
|          40 | -9.64%   | 33.78%             | -15.38% |    -0.39 |       64 | 39.43%     | ok               |
|          50 | -9.37%   | 33.78%             | -17.56% |    -0.42 |       54 | 35.11%     | ok               |

## EOG Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -17.49%  | 20.17%             | -39.69% |    -0.37 |       58 | 34.61%     | ok               |
|          30 | -22.27%  | 20.17%             | -48.13% |    -0.45 |       81 | 48.42%     | ok               |
|          40 | -22.37%  | 20.17%             | -43.26% |    -0.51 |       66 | 37.94%     | ok               |
|          35 | -23.13%  | 20.17%             | -46.26% |    -0.51 |       79 | 43.09%     | ok               |
|          25 | -26.22%  | 20.17%             | -51.99% |    -0.53 |       82 | 51.41%     | ok               |

## ETC-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -2.84%   | -67.88%            | -31.28% |     0.08 |       26 | 15.90%     | ok               |
|          45 | -12.62%  | -67.88%            | -38.47% |    -0.1  |       26 | 17.62%     | ok               |
|          35 | -15.58%  | -67.88%            | -45.32% |    -0.12 |       44 | 25.29%     | ok               |
|          40 | -19.39%  | -67.88%            | -43.28% |    -0.23 |       40 | 21.26%     | ok               |
|          30 | -34.57%  | -67.88%            | -48.09% |    -0.49 |       64 | 29.31%     | ok               |

## ETH-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 143.32%  | -32.53%            | -30.11% |     1.21 |       64 | 46.36%     | ok               |
|          30 | 108.46%  | -32.53%            | -32.89% |     1    |       66 | 54.98%     | ok               |
|          15 | 46.94%   | -32.53%            | -42.74% |     0.62 |       75 | 69.73%     | ok               |
|          20 | 45.54%   | -32.53%            | -39.10% |     0.62 |       80 | 64.18%     | ok               |
|          25 | 44.47%   | -32.53%            | -40.90% |     0.61 |       64 | 59.96%     | ok               |

## EWJ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -19.56%  | 27.78%             | -29.40% |    -0.65 |       62 | 37.77%     | ok               |
|          20 | -20.93%  | 27.78%             | -30.00% |    -0.68 |       58 | 39.77%     | ok               |
|          25 | -23.21%  | 27.78%             | -29.85% |    -0.78 |       58 | 38.77%     | ok               |
|          15 | -26.05%  | 27.78%             | -30.84% |    -0.83 |       71 | 43.09%     | ok               |
|          45 | -21.84%  | 27.78%             | -27.68% |    -0.86 |       58 | 29.78%     | ok               |

## FCX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -5.98%   | 66.06%             | -27.70% |     0.03 |       56 | 30.45%     | ok               |
|          45 | -10.04%  | 66.06%             | -35.18% |    -0.03 |       56 | 34.94%     | ok               |
|          40 | -20.76%  | 66.06%             | -43.57% |    -0.21 |       66 | 39.27%     | ok               |
|          30 | -28.89%  | 66.06%             | -47.47% |    -0.33 |       65 | 46.09%     | ok               |
|          35 | -33.27%  | 66.06%             | -50.71% |    -0.44 |       71 | 44.26%     | ok               |

## FET-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -3.03%   | -82.09%            | -59.70% |     0.29 |       92 | 52.68%     | ok               |
|          15 | -14.71%  | -82.09%            | -59.58% |     0.2  |       86 | 56.70%     | ok               |
|          25 | -29.44%  | -82.09%            | -60.09% |     0.01 |       89 | 46.36%     | ok               |
|          30 | -36.84%  | -82.09%            | -52.82% |    -0.11 |       85 | 41.95%     | ok               |
|          35 | -51.91%  | -82.09%            | -61.76% |    -0.47 |       73 | 33.72%     | ok               |

## FIL-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -17.13%  | -79.78%            | -34.38% |    -0.1  |       44 | 23.18%     | ok               |
|          35 | -42.20%  | -79.78%            | -43.72% |    -0.52 |       60 | 28.16%     | ok               |
|          45 | -36.38%  | -79.78%            | -39.41% |    -0.52 |       42 | 17.43%     | ok               |
|          30 | -47.62%  | -79.78%            | -51.30% |    -0.6  |       70 | 33.91%     | ok               |
|          50 | -39.00%  | -79.78%            | -44.95% |    -0.69 |       36 | 12.64%     | ok               |

## FXI Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -2.72%   | 54.80%             | -22.57% |     0.02 |       46 | 31.45%     | ok               |
|          30 | -3.00%   | 54.80%             | -23.91% |     0.01 |       44 | 29.95%     | ok               |
|          15 | -4.59%   | 54.80%             | -21.68% |    -0.02 |       52 | 35.44%     | ok               |
|          20 | -5.72%   | 54.80%             | -24.53% |    -0.05 |       50 | 33.11%     | ok               |
|          45 | -6.49%   | 54.80%             | -26.75% |    -0.09 |       44 | 24.63%     | ok               |

## GDX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 17.52%   | 158.93%            | -35.59% |     0.38 |       72 | 51.91%     | ok               |
|          40 | 11.14%   | 158.93%            | -31.87% |     0.3  |       62 | 42.10%     | ok               |
|          30 | 10.31%   | 158.93%            | -34.99% |     0.29 |       58 | 47.42%     | ok               |
|          35 | 6.36%    | 158.93%            | -32.37% |     0.23 |       66 | 44.43%     | ok               |
|          25 | 4.46%    | 158.93%            | -38.90% |     0.2  |       62 | 48.59%     | ok               |

## GDXJ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -8.92%   | 178.26%            | -45.05% |     0.04 |       66 | 51.75%     | ok               |
|          30 | -21.17%  | 178.26%            | -44.93% |    -0.18 |       64 | 45.76%     | ok               |
|          50 | -18.94%  | 178.26%            | -44.94% |    -0.2  |       58 | 37.94%     | ok               |
|          25 | -26.44%  | 178.26%            | -47.26% |    -0.25 |       69 | 48.59%     | ok               |
|          35 | -24.89%  | 178.26%            | -43.49% |    -0.26 |       66 | 43.43%     | ok               |

## GE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 25.00%   | 188.60%            | -22.29% |     0.54 |       66 | 38.44%     | ok               |
|          45 | 15.57%   | 188.60%            | -25.68% |     0.38 |       74 | 41.26%     | ok               |
|          20 | 10.05%   | 188.60%            | -26.63% |     0.29 |       73 | 55.74%     | ok               |
|          35 | 8.51%    | 188.60%            | -27.11% |     0.26 |       80 | 46.59%     | ok               |
|          30 | 8.26%    | 188.60%            | -27.82% |     0.26 |       76 | 51.75%     | ok               |

## GLD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 30.35%   | 87.32%             | -14.61% |     0.72 |       48 | 50.75%     | ok               |
|          25 | 29.67%   | 87.32%             | -14.61% |     0.72 |       48 | 49.25%     | ok               |
|          30 | 23.50%   | 87.32%             | -16.63% |     0.6  |       50 | 48.09%     | ok               |
|          15 | 22.37%   | 87.32%             | -17.54% |     0.55 |       50 | 54.91%     | ok               |
|          35 | 17.08%   | 87.32%             | -17.29% |     0.48 |       54 | 46.09%     | ok               |

## GOOGL Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 80.77%   | 151.53%            | -18.25% |     1.22 |       59 | 49.08%     | ok               |
|          45 | 67.79%   | 151.53%            | -14.13% |     1.15 |       52 | 42.10%     | ok               |
|          30 | 75.05%   | 151.53%            | -20.41% |     1.14 |       57 | 52.75%     | ok               |
|          25 | 72.38%   | 151.53%            | -19.76% |     1.1  |       55 | 54.74%     | ok               |
|          50 | 60.60%   | 151.53%            | -14.89% |     1.09 |       48 | 37.27%     | ok               |

## GRT-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 24.78%   | -89.08%            | -49.67% |     0.47 |       71 | 61.69%     | ok               |
|          20 | 18.24%   | -89.08%            | -46.47% |     0.41 |       77 | 56.90%     | ok               |
|          50 | 14.84%   | -89.08%            | -36.42% |     0.37 |       44 | 21.65%     | ok               |
|          30 | 0.08%    | -89.08%            | -50.20% |     0.22 |       83 | 43.68%     | ok               |
|          35 | 0.88%    | -89.08%            | -43.61% |     0.21 |       66 | 37.55%     | ok               |

## GS Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 21.82%   | 164.34%            | -20.56% |     0.48 |       74 | 60.40%     | ok               |
|          20 | 5.20%    | 164.34%            | -23.19% |     0.21 |       74 | 56.41%     | ok               |
|          40 | 0.67%    | 164.34%            | -17.88% |     0.11 |       72 | 44.59%     | ok               |
|          25 | -0.13%   | 164.34%            | -23.32% |     0.1  |       74 | 53.91%     | ok               |
|          30 | -1.81%   | 164.34%            | -22.13% |     0.06 |       76 | 51.41%     | ok               |

## HD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -8.53%   | -8.98%             | -18.58% |    -0.15 |       73 | 44.43%     | ok               |
|          25 | -9.24%   | -8.98%             | -19.40% |    -0.17 |       72 | 46.42%     | ok               |
|          45 | -12.36%  | -8.98%             | -20.74% |    -0.36 |       60 | 28.62%     | ok               |
|          15 | -17.44%  | -8.98%             | -27.26% |    -0.36 |      109 | 55.41%     | ok               |
|          35 | -16.05%  | -8.98%             | -23.81% |    -0.41 |       82 | 40.27%     | ok               |

## HON Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -11.42%  | 26.64%             | -21.17% |    -0.32 |       72 | 31.78%     | ok               |
|          45 | -13.20%  | 26.64%             | -19.99% |    -0.36 |       74 | 36.77%     | ok               |
|          40 | -21.75%  | 26.64%             | -26.29% |    -0.6  |       76 | 41.10%     | ok               |
|          35 | -25.08%  | 26.64%             | -29.07% |    -0.69 |       91 | 47.59%     | ok               |
|          30 | -27.50%  | 26.64%             | -31.48% |    -0.74 |       96 | 52.75%     | ok               |

## HYG Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -7.91%   | 3.01%              | -7.91%  |    -0.96 |       68 | 29.12%     | ok               |
|          15 | -9.49%   | 3.01%              | -10.34% |    -1.03 |       88 | 40.93%     | ok               |
|          20 | -9.23%   | 3.01%              | -10.34% |    -1.03 |       86 | 38.77%     | ok               |
|          25 | -9.38%   | 3.01%              | -10.11% |    -1.06 |       83 | 36.61%     | ok               |
|          30 | -9.08%   | 3.01%              | -9.59%  |    -1.06 |       81 | 33.94%     | ok               |

## IBIT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 53.73%   | -4.92%             | -17.37% |     1.06 |       22 | 21.92%     | ok               |
|          15 | 56.91%   | -4.92%             | -19.20% |     0.94 |       40 | 39.04%     | ok               |
|          45 | 44.27%   | -4.92%             | -17.37% |     0.89 |       26 | 23.29%     | ok               |
|          40 | 38.04%   | -4.92%             | -17.78% |     0.8  |       26 | 25.11%     | ok               |
|          30 | 30.82%   | -4.92%             | -18.95% |     0.66 |       34 | 31.51%     | ok               |

## IBM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -18.48%  | 18.55%             | -45.75% |    -0.13 |       91 | 62.40%     | ok               |
|          30 | -25.81%  | 18.55%             | -47.10% |    -0.32 |       75 | 50.25%     | ok               |
|          20 | -29.08%  | 18.55%             | -50.22% |    -0.35 |       73 | 54.91%     | ok               |
|          35 | -27.72%  | 18.55%             | -47.10% |    -0.36 |       69 | 45.92%     | ok               |
|          50 | -31.43%  | 18.55%             | -45.88% |    -0.49 |       50 | 33.94%     | ok               |

## ICP-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 0.63%    | -70.31%            | -32.85% |     0.2  |       52 | 23.95%     | ok               |
|          35 | -8.92%   | -70.31%            | -42.43% |     0.1  |       62 | 29.50%     | ok               |
|          30 | -20.42%  | -70.31%            | -54.22% |     0.05 |       75 | 35.25%     | ok               |
|          50 | -18.44%  | -70.31%            | -43.65% |    -0.1  |       34 | 14.37%     | ok               |
|          15 | -46.53%  | -70.31%            | -63.03% |    -0.17 |       77 | 47.51%     | ok               |

## IEF Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -7.70%   | -1.28%             | -10.10% |    -0.92 |       72 | 42.93%     | ok               |
|          15 | -8.25%   | -1.28%             | -10.83% |    -0.97 |       71 | 44.43%     | ok               |
|          45 | -8.27%   | -1.28%             | -9.73%  |    -1.35 |       54 | 23.63%     | ok               |
|          40 | -8.84%   | -1.28%             | -9.67%  |    -1.37 |       64 | 25.79%     | ok               |
|          25 | -11.25%  | -1.28%             | -11.63% |    -1.43 |       78 | 40.10%     | ok               |

## IEMG Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | -2.65%   | 50.37%             | -22.13% |    -0.03 |       63 | 40.27%     | ok               |
|          50 | -2.93%   | 50.37%             | -13.91% |    -0.06 |       52 | 31.95%     | ok               |
|          40 | -3.29%   | 50.37%             | -18.43% |    -0.06 |       60 | 37.77%     | ok               |
|          45 | -3.14%   | 50.37%             | -14.92% |    -0.06 |       48 | 34.61%     | ok               |
|          25 | -6.95%   | 50.37%             | -25.58% |    -0.17 |       59 | 43.09%     | ok               |

## INJ-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -10.15%  | -71.54%            | -52.34% |     0.06 |       44 | 23.37%     | ok               |
|          35 | -18.74%  | -71.54%            | -59.17% |     0.01 |       62 | 33.33%     | ok               |
|          50 | -22.38%  | -71.54%            | -49.35% |    -0.14 |       48 | 20.11%     | ok               |
|          40 | -27.07%  | -71.54%            | -55.86% |    -0.15 |       52 | 29.50%     | ok               |
|          20 | -54.28%  | -71.54%            | -81.16% |    -0.42 |       80 | 47.51%     | ok               |

## INTC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 125.65%  | 99.95%             | -53.65% |     0.9  |       77 | 59.90%     | ok               |
|          25 | 90.25%   | 99.95%             | -56.41% |     0.78 |       75 | 51.08%     | ok               |
|          45 | 83.34%   | 99.95%             | -49.32% |     0.78 |       56 | 33.78%     | ok               |
|          40 | 77.32%   | 99.95%             | -55.86% |     0.74 |       64 | 38.10%     | ok               |
|          20 | 80.11%   | 99.95%             | -52.47% |     0.73 |       78 | 55.57%     | ok               |

## INTU Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 0.97%    | -51.07%            | -39.99% |     0.13 |       69 | 27.62%     | ok               |
|          45 | -1.00%   | -51.07%            | -41.03% |     0.1  |       67 | 31.61%     | ok               |
|          40 | -8.34%   | -51.07%            | -44.97% |    -0.03 |       69 | 34.78%     | ok               |
|          35 | -15.62%  | -51.07%            | -46.75% |    -0.16 |       71 | 38.44%     | ok               |
|          25 | -18.48%  | -51.07%            | -39.87% |    -0.2  |       68 | 44.26%     | ok               |

## ITA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -1.36%   | 90.28%             | -21.48% |     0.02 |       76 | 37.10%     | ok               |
|          30 | -4.78%   | 90.28%             | -23.75% |    -0.06 |       72 | 47.09%     | ok               |
|          15 | -8.02%   | 90.28%             | -28.17% |    -0.12 |       86 | 59.73%     | ok               |
|          35 | -6.81%   | 90.28%             | -23.16% |    -0.13 |       76 | 45.42%     | ok               |
|          40 | -7.88%   | 90.28%             | -20.58% |    -0.18 |       78 | 41.93%     | ok               |

## IWM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | 9.83%    | 44.00%             | -13.30% |     0.4  |       50 | 36.77%     | ok               |
|          40 | 8.60%    | 44.00%             | -14.08% |     0.39 |       42 | 31.28%     | ok               |
|          30 | 9.40%    | 44.00%             | -12.83% |     0.39 |       48 | 35.77%     | ok               |
|          35 | 8.35%    | 44.00%             | -14.11% |     0.36 |       48 | 33.61%     | ok               |
|          20 | 5.50%    | 44.00%             | -13.83% |     0.25 |       60 | 37.77%     | ok               |

## JNJ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 19.45%   | 66.74%             | -10.57% |     0.79 |       56 | 37.27%     | ok               |
|          15 | 18.48%   | 66.74%             | -18.02% |     0.61 |       64 | 58.40%     | ok               |
|          20 | 13.01%   | 66.74%             | -17.61% |     0.47 |       70 | 54.91%     | ok               |
|          45 | 10.92%   | 66.74%             | -13.35% |     0.47 |       56 | 42.10%     | ok               |
|          25 | 7.78%    | 66.74%             | -17.84% |     0.32 |       71 | 53.24%     | ok               |

## JPM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 10.84%   | 89.50%             | -15.90% |     0.4  |       54 | 39.43%     | ok               |
|          45 | 0.31%    | 89.50%             | -21.91% |     0.08 |       56 | 42.43%     | ok               |
|          20 | -15.92%  | 89.50%             | -33.59% |    -0.28 |       84 | 57.24%     | ok               |
|          40 | -13.46%  | 89.50%             | -28.47% |    -0.33 |       68 | 45.09%     | ok               |
|          35 | -18.57%  | 89.50%             | -27.43% |    -0.47 |       76 | 49.08%     | ok               |

## KO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 23.75%   | 48.30%             | -8.20%  |     0.85 |       51 | 37.94%     | ok               |
|          35 | 19.96%   | 48.30%             | -8.07%  |     0.75 |       54 | 36.61%     | ok               |
|          40 | 17.46%   | 48.30%             | -9.28%  |     0.71 |       56 | 33.44%     | ok               |
|          25 | 18.64%   | 48.30%             | -9.73%  |     0.69 |       57 | 40.60%     | ok               |
|          50 | 10.20%   | 48.30%             | -12.31% |     0.48 |       38 | 26.96%     | ok               |

## LDO-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 62.04%   | -78.75%            | -48.17% |     0.68 |       80 | 56.32%     | ok               |
|          50 | 33.03%   | -78.75%            | -48.04% |     0.57 |       52 | 18.20%     | ok               |
|          20 | 36.88%   | -78.75%            | -45.55% |     0.55 |       82 | 51.15%     | ok               |
|          30 | 28.90%   | -78.75%            | -61.16% |     0.5  |       78 | 42.72%     | ok               |
|          35 | 28.93%   | -78.75%            | -61.98% |     0.49 |       78 | 35.63%     | ok               |

## LIN Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -3.63%   | 10.89%             | -23.68% |    -0.06 |       64 | 48.59%     | ok               |
|          25 | -3.89%   | 10.89%             | -22.01% |    -0.08 |       63 | 40.60%     | ok               |
|          20 | -5.95%   | 10.89%             | -23.00% |    -0.14 |       62 | 43.76%     | ok               |
|          35 | -7.37%   | 10.89%             | -21.18% |    -0.23 |       62 | 31.28%     | ok               |
|          30 | -7.95%   | 10.89%             | -21.53% |    -0.23 |       66 | 37.77%     | ok               |

## LINK-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -14.33%  | -52.29%            | -49.94% |     0.09 |       73 | 44.64%     | ok               |
|          45 | -12.57%  | -52.29%            | -38.11% |     0.06 |       52 | 29.12%     | ok               |
|          50 | -17.37%  | -52.29%            | -36.52% |    -0.03 |       44 | 22.99%     | ok               |
|          35 | -23.95%  | -52.29%            | -49.77% |    -0.04 |       61 | 39.46%     | ok               |
|          40 | -28.13%  | -52.29%            | -51.13% |    -0.13 |       57 | 33.72%     | ok               |

## LLY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 3.97%    | 56.98%             | -38.23% |     0.19 |       46 | 35.44%     | ok               |
|          15 | -5.27%   | 56.98%             | -48.12% |     0.06 |       63 | 58.90%     | ok               |
|          45 | -7.73%   | 56.98%             | -42.66% |    -0.04 |       54 | 38.94%     | ok               |
|          20 | -20.53%  | 56.98%             | -51.34% |    -0.22 |       72 | 53.91%     | ok               |
|          25 | -21.84%  | 56.98%             | -53.47% |    -0.26 |       68 | 51.25%     | ok               |

## LRCX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -12.80%  | 179.94%            | -60.45% |     0.05 |       83 | 52.91%     | ok               |
|          50 | -18.75%  | 179.94%            | -51.13% |    -0.1  |       80 | 34.44%     | ok               |
|          40 | -21.90%  | 179.94%            | -57.88% |    -0.11 |       74 | 40.27%     | ok               |
|          35 | -23.40%  | 179.94%            | -60.84% |    -0.13 |       82 | 42.43%     | ok               |
|          20 | -24.84%  | 179.94%            | -66.39% |    -0.13 |       89 | 48.42%     | ok               |

## LTC-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -14.97%  | -64.54%            | -35.63% |    -0.05 |       58 | 32.18%     | ok               |
|          35 | -26.84%  | -64.54%            | -48.33% |    -0.21 |       70 | 43.49%     | ok               |
|          30 | -36.14%  | -64.54%            | -47.07% |    -0.33 |       72 | 50.19%     | ok               |
|          40 | -35.27%  | -64.54%            | -49.75% |    -0.38 |       62 | 38.70%     | ok               |
|          50 | -33.94%  | -64.54%            | -36.35% |    -0.46 |       56 | 23.75%     | ok               |

## MCD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 2.85%    | -6.67%             | -9.22%  |     0.19 |       42 | 20.63%     | ok               |
|          30 | -2.55%   | -6.67%             | -18.81% |    -0.05 |       75 | 38.10%     | ok               |
|          25 | -3.59%   | -6.67%             | -20.47% |    -0.09 |       75 | 40.77%     | ok               |
|          35 | -7.68%   | -6.67%             | -15.45% |    -0.29 |       67 | 34.44%     | ok               |
|          40 | -7.95%   | -6.67%             | -16.86% |    -0.33 |       71 | 28.79%     | ok               |

## META Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -16.92%  | 21.05%             | -33.45% |    -0.26 |       68 | 36.77%     | ok               |
|          40 | -26.01%  | 21.05%             | -37.90% |    -0.47 |       70 | 39.93%     | ok               |
|          25 | -33.32%  | 21.05%             | -42.95% |    -0.58 |       71 | 50.58%     | ok               |
|          50 | -29.60%  | 21.05%             | -36.07% |    -0.62 |       72 | 32.95%     | ok               |
|          30 | -35.10%  | 21.05%             | -42.12% |    -0.66 |       76 | 47.42%     | ok               |

## MPC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 23.17%   | 74.72%             | -23.96% |     0.52 |       50 | 37.94%     | ok               |
|          45 | 15.36%   | 74.72%             | -25.09% |     0.38 |       56 | 41.60%     | ok               |
|          40 | 11.00%   | 74.72%             | -25.70% |     0.31 |       58 | 43.76%     | ok               |
|          35 | 7.57%    | 74.72%             | -35.90% |     0.25 |       66 | 46.26%     | ok               |
|          30 | -9.35%   | 74.72%             | -44.76% |    -0.05 |       69 | 49.08%     | ok               |

## MRK Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -17.16%  | 7.32%              | -30.12% |    -0.29 |       89 | 54.41%     | ok               |
|          25 | -16.71%  | 7.32%              | -31.07% |    -0.31 |       72 | 46.42%     | ok               |
|          20 | -20.79%  | 7.32%              | -29.59% |    -0.41 |       77 | 49.75%     | ok               |
|          50 | -21.52%  | 7.32%              | -27.68% |    -0.6  |       58 | 29.12%     | ok               |
|          45 | -23.47%  | 7.32%              | -27.72% |    -0.62 |       59 | 32.45%     | ok               |

## MS Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -3.32%   | 137.38%            | -19.99% |     0    |       72 | 41.43%     | ok               |
|          15 | -4.98%   | 137.38%            | -22.02% |    -0.01 |       73 | 58.24%     | ok               |
|          20 | -5.09%   | 137.38%            | -25.68% |    -0.02 |       77 | 54.41%     | ok               |
|          30 | -10.18%  | 137.38%            | -27.79% |    -0.16 |       77 | 49.58%     | ok               |
|          35 | -10.11%  | 137.38%            | -25.26% |    -0.17 |       78 | 46.09%     | ok               |

## MSFT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -20.82%  | -2.31%             | -24.64% |    -0.57 |       64 | 33.78%     | ok               |
|          50 | -22.75%  | -2.31%             | -25.48% |    -0.66 |       58 | 28.95%     | ok               |
|          35 | -33.78%  | -2.31%             | -35.38% |    -0.9  |       71 | 42.43%     | ok               |
|          40 | -33.30%  | -2.31%             | -34.92% |    -0.93 |       67 | 37.44%     | ok               |
|          30 | -37.64%  | -2.31%             | -39.15% |    -0.99 |       81 | 47.09%     | ok               |

## MU Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 353.25%  | 768.56%            | -61.96% |     1.43 |       51 | 66.56%     | ok               |
|          40 | 268.09%  | 768.56%            | -64.26% |     1.35 |       56 | 53.91%     | ok               |
|          25 | 239.12%  | 768.56%            | -67.90% |     1.25 |       51 | 60.57%     | ok               |
|          30 | 225.70%  | 768.56%            | -68.76% |     1.23 |       51 | 58.90%     | ok               |
|          35 | 216.52%  | 768.56%            | -69.35% |     1.22 |       63 | 56.57%     | ok               |

## NEAR-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 58.08%   | -52.62%            | -49.73% |     0.73 |       40 | 22.22%     | ok               |
|          50 | 38.01%   | -52.62%            | -52.97% |     0.58 |       34 | 17.82%     | ok               |
|          40 | 32.29%   | -52.62%            | -57.80% |     0.52 |       44 | 26.44%     | ok               |
|          35 | 5.83%    | -52.62%            | -61.61% |     0.29 |       66 | 31.61%     | ok               |
|          15 | -10.91%  | -52.62%            | -53.23% |     0.2  |       85 | 54.60%     | ok               |

## NEM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 16.36%   | 174.51%            | -29.41% |     0.36 |       60 | 60.90%     | ok               |
|          20 | 3.91%    | 174.51%            | -30.47% |     0.22 |       70 | 56.41%     | ok               |
|          25 | -9.17%   | 174.51%            | -37.89% |     0.04 |       66 | 54.41%     | ok               |
|          30 | -20.55%  | 174.51%            | -38.49% |    -0.15 |       70 | 52.75%     | ok               |
|          50 | -21.22%  | 174.51%            | -33.17% |    -0.22 |       54 | 40.10%     | ok               |

## NFLX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 41.87%   | 20.95%             | -13.34% |     0.91 |       50 | 45.26%     | ok               |
|          50 | 37.51%   | 20.95%             | -16.28% |     0.89 |       48 | 37.27%     | ok               |
|          35 | 37.84%   | 20.95%             | -18.30% |     0.8  |       66 | 49.25%     | ok               |
|          45 | 27.78%   | 20.95%             | -15.48% |     0.67 |       56 | 41.60%     | ok               |
|          15 | 32.72%   | 20.95%             | -26.59% |     0.64 |       69 | 64.39%     | ok               |

## NKE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | -26.37%  | -56.21%            | -42.13% |    -0.36 |       73 | 37.27%     | ok               |
|          20 | -33.26%  | -56.21%            | -50.44% |    -0.41 |       91 | 52.41%     | ok               |
|          25 | -33.48%  | -56.21%            | -51.20% |    -0.42 |       87 | 48.59%     | ok               |
|          15 | -37.96%  | -56.21%            | -55.28% |    -0.5  |       93 | 56.74%     | ok               |
|          40 | -26.27%  | -56.21%            | -31.79% |    -0.51 |       65 | 29.12%     | ok               |

## NOW Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 4.71%    | -25.27%            | -31.29% |     0.23 |       77 | 51.91%     | ok               |
|          30 | 1.54%    | -25.27%            | -26.78% |     0.18 |       80 | 45.76%     | ok               |
|          15 | -4.41%   | -25.27%            | -35.09% |     0.12 |       87 | 55.07%     | ok               |
|          25 | -4.29%   | -25.27%            | -32.31% |     0.12 |       74 | 49.08%     | ok               |
|          40 | -6.73%   | -25.27%            | -30.91% |     0.04 |       70 | 35.11%     | ok               |

## NVDA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -10.10%  | 137.24%            | -35.26% |     0    |       76 | 48.31%     | ok               |
|          20 | -15.33%  | 137.24%            | -40.59% |    -0.03 |       72 | 56.33%     | ok               |
|          25 | -15.20%  | 137.24%            | -37.16% |    -0.05 |       73 | 51.34%     | ok               |
|          15 | -24.50%  | 137.24%            | -45.14% |    -0.15 |       73 | 59.54%     | ok               |
|          35 | -22.24%  | 137.24%            | -42.39% |    -0.21 |       84 | 45.45%     | ok               |

## OP-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 27.06%   | -92.49%            | -36.11% |     0.51 |       30 | 11.11%     | ok               |
|          45 | 26.15%   | -92.49%            | -45.76% |     0.48 |       32 | 15.71%     | ok               |
|          40 | 7.84%    | -92.49%            | -53.61% |     0.29 |       48 | 24.33%     | ok               |
|          35 | -17.48%  | -92.49%            | -59.71% |    -0    |       56 | 27.78%     | ok               |
|          30 | -26.73%  | -92.49%            | -71.26% |    -0.07 |       70 | 34.48%     | ok               |

## ORCL Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 300.83%  | 8.13%              | -29.32% |     1.51 |       65 | 66.22%     | ok               |
|          20 | 192.70%  | 8.13%              | -29.32% |     1.23 |       70 | 62.23%     | ok               |
|          25 | 188.09%  | 8.13%              | -27.76% |     1.22 |       67 | 59.57%     | ok               |
|          30 | 139.00%  | 8.13%              | -30.61% |     1.06 |       68 | 56.07%     | ok               |
|          35 | 128.73%  | 8.13%              | -31.95% |     1.02 |       68 | 52.08%     | ok               |

## OXY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 1.27%    | -10.98%            | -30.14% |     0.14 |       70 | 41.76%     | ok               |
|          40 | 1.02%    | -10.98%            | -30.31% |     0.13 |       56 | 38.10%     | ok               |
|          50 | 0.75%    | -10.98%            | -32.02% |     0.12 |       46 | 30.95%     | ok               |
|          30 | -1.04%   | -10.98%            | -34.15% |     0.11 |       71 | 46.92%     | ok               |
|          45 | -8.21%   | -10.98%            | -35.02% |    -0.06 |       48 | 33.28%     | ok               |

## PEP Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 11.74%   | -11.84%            | -11.62% |     0.53 |       44 | 26.79%     | ok               |
|          45 | 4.60%    | -11.84%            | -14.22% |     0.24 |       60 | 30.78%     | ok               |
|          40 | 1.33%    | -11.84%            | -18.04% |     0.1  |       72 | 36.77%     | ok               |
|          35 | 1.21%    | -11.84%            | -21.42% |     0.1  |       79 | 41.76%     | ok               |
|          30 | -4.54%   | -11.84%            | -21.35% |    -0.07 |       75 | 48.25%     | ok               |

## PEPE-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -0.11%   | -70.41%            | -61.96% |     0.34 |       78 | 62.84%     | ok               |
|          30 | -5.04%   | -70.41%            | -57.66% |     0.24 |       83 | 46.17%     | ok               |
|          25 | -18.42%  | -70.41%            | -53.88% |     0.11 |       91 | 51.92%     | ok               |
|          20 | -22.12%  | -70.41%            | -61.13% |     0.11 |       84 | 59.20%     | ok               |
|          35 | -14.89%  | -70.41%            | -51.35% |     0.1  |       68 | 40.23%     | ok               |

## PFE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -24.15%  | -3.18%             | -25.35% |    -0.89 |       54 | 19.13%     | ok               |
|          40 | -31.18%  | -3.18%             | -32.29% |    -1.11 |       74 | 24.13%     | ok               |
|          35 | -34.18%  | -3.18%             | -35.70% |    -1.14 |       84 | 31.61%     | ok               |
|          50 | -27.42%  | -3.18%             | -28.45% |    -1.14 |       42 | 15.64%     | ok               |
|          30 | -41.51%  | -3.18%             | -42.34% |    -1.34 |       79 | 36.11%     | ok               |

## PG Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -7.45%   | -6.55%             | -19.77% |    -0.27 |       56 | 31.95%     | ok               |
|          35 | -10.61%  | -6.55%             | -18.66% |    -0.39 |       64 | 35.44%     | ok               |
|          30 | -18.73%  | -6.55%             | -24.25% |    -0.71 |       66 | 38.60%     | ok               |
|          45 | -16.50%  | -6.55%             | -22.13% |    -0.71 |       56 | 29.45%     | ok               |
|          25 | -20.59%  | -6.55%             | -25.94% |    -0.79 |       78 | 40.10%     | ok               |

## PM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | -1.38%   | 121.01%            | -32.95% |     0.06 |       86 | 51.91%     | ok               |
|          20 | -4.06%   | 121.01%            | -32.63% |     0.01 |       85 | 60.40%     | ok               |
|          30 | -4.47%   | 121.01%            | -34.41% |    -0    |       81 | 55.41%     | ok               |
|          50 | -6.95%   | 121.01%            | -35.70% |    -0.09 |       74 | 42.10%     | ok               |
|          40 | -8.33%   | 121.01%            | -37.94% |    -0.12 |       80 | 48.25%     | ok               |

## POL-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 42.50%   | -75.86%            | -46.45% |     0.61 |       79 | 49.43%     | ok               |
|          25 | 37.54%   | -75.86%            | -46.72% |     0.56 |       66 | 57.28%     | ok               |
|          20 | 26.36%   | -75.86%            | -52.88% |     0.47 |       72 | 61.69%     | ok               |
|          15 | 12.76%   | -75.86%            | -58.42% |     0.36 |       74 | 66.48%     | ok               |
|          50 | 2.17%    | -75.86%            | -23.33% |     0.17 |       48 | 19.73%     | ok               |

## QCOM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -2.81%   | 0.89%              | -54.50% |     0.14 |       73 | 47.59%     | ok               |
|          20 | -6.76%   | 0.89%              | -54.38% |     0.09 |       69 | 50.42%     | ok               |
|          35 | -9.48%   | 0.89%              | -50.58% |     0.03 |       79 | 43.09%     | ok               |
|          30 | -19.75%  | 0.89%              | -56.59% |    -0.11 |       75 | 45.59%     | ok               |
|          15 | -22.25%  | 0.89%              | -57.94% |    -0.12 |       73 | 53.58%     | ok               |

## QQQ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 20.95%   | 54.91%             | -14.95% |     0.55 |       63 | 52.08%     | ok               |
|          30 | 16.58%   | 54.91%             | -13.78% |     0.49 |       62 | 43.76%     | ok               |
|          25 | 13.96%   | 54.91%             | -14.93% |     0.42 |       59 | 46.26%     | ok               |
|          20 | 11.21%   | 54.91%             | -17.00% |     0.35 |       67 | 48.92%     | ok               |
|          35 | 4.66%    | 54.91%             | -19.11% |     0.2  |       68 | 40.10%     | ok               |

## RENDER-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 44.95%   | -66.31%            | -43.43% |     0.6  |       92 | 53.26%     | ok               |
|          15 | 37.05%   | -66.31%            | -44.59% |     0.56 |       92 | 56.70%     | ok               |
|          25 | 16.88%   | -66.31%            | -40.60% |     0.42 |       92 | 48.47%     | ok               |
|          30 | -18.07%  | -66.31%            | -45.00% |     0.11 |      100 | 42.15%     | ok               |
|          35 | -30.89%  | -66.31%            | -41.33% |    -0.11 |       86 | 34.10%     | ok               |

## RTX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 49.85%   | 142.70%            | -18.66% |     1.01 |       72 | 56.74%     | ok               |
|          35 | 39.44%   | 142.70%            | -18.00% |     0.94 |       50 | 50.92%     | ok               |
|          25 | 44.73%   | 142.70%            | -18.59% |     0.94 |       60 | 54.08%     | ok               |
|          30 | 42.53%   | 142.70%            | -16.99% |     0.91 |       54 | 52.91%     | ok               |
|          15 | 41.67%   | 142.70%            | -19.55% |     0.86 |       67 | 61.56%     | ok               |

## SBUX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -9.87%   | 13.02%             | -23.55% |    -0.12 |       59 | 41.76%     | ok               |
|          40 | -15.57%  | 13.02%             | -25.43% |    -0.3  |       60 | 34.11%     | ok               |
|          30 | -17.57%  | 13.02%             | -29.22% |    -0.31 |       58 | 39.43%     | ok               |
|          45 | -15.10%  | 13.02%             | -27.26% |    -0.32 |       66 | 30.28%     | ok               |
|          35 | -20.34%  | 13.02%             | -27.06% |    -0.4  |       58 | 37.10%     | ok               |

## SCHW Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 8.08%    | 55.61%             | -16.53% |     0.3  |       58 | 35.77%     | ok               |
|          25 | 3.02%    | 55.61%             | -28.76% |     0.16 |       63 | 51.25%     | ok               |
|          50 | 2.74%    | 55.61%             | -13.28% |     0.15 |       50 | 32.95%     | ok               |
|          20 | -0.67%   | 55.61%             | -29.24% |     0.08 |       71 | 53.74%     | ok               |
|          40 | -2.29%   | 55.61%             | -23.35% |     0.02 |       64 | 38.94%     | ok               |

## SHIB-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -14.34%  | -70.20%            | -43.85% |     0.06 |       73 | 59.39%     | ok               |
|          15 | -15.37%  | -70.20%            | -49.21% |     0.06 |       78 | 67.24%     | ok               |
|          20 | -19.49%  | -70.20%            | -46.38% |     0    |       75 | 63.22%     | ok               |
|          35 | -21.16%  | -70.20%            | -52.76% |    -0.07 |       66 | 46.55%     | ok               |
|          30 | -27.84%  | -70.20%            | -47.96% |    -0.15 |       76 | 52.49%     | ok               |

## SHY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd    |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:-------|---------:|---------:|:-----------|:-----------------|
|          30 | -2.24%   | 0.37%              | -2.85% |    -0.79 |       48 | 34.28%     | ok               |
|          35 | -2.36%   | 0.37%              | -3.27% |    -0.84 |       50 | 32.45%     | ok               |
|          40 | -2.47%   | 0.37%              | -3.33% |    -0.89 |       50 | 30.62%     | ok               |
|          45 | -2.45%   | 0.37%              | -3.23% |    -0.9  |       48 | 27.45%     | ok               |
|          50 | -2.62%   | 0.37%              | -3.40% |    -1.01 |       44 | 24.63%     | ok               |

## SKY-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -37.22%  | -0.81%             | -56.39% |    -0.41 |       65 | 51.39%     | ok               |
|          30 | -33.72%  | -0.81%             | -47.82% |    -0.43 |       76 | 41.54%     | ok               |
|          25 | -36.56%  | -0.81%             | -50.05% |    -0.47 |       70 | 45.18%     | ok               |
|          20 | -46.23%  | -0.81%             | -59.15% |    -0.65 |       67 | 48.61%     | ok               |
|          35 | -39.82%  | -0.81%             | -49.68% |    -0.66 |       70 | 34.05%     | ok               |

## SLB Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 15.24%   | 0.64%              | -21.46% |     0.41 |       54 | 33.78%     | ok               |
|          40 | 11.68%   | 0.64%              | -25.33% |     0.33 |       48 | 37.27%     | ok               |
|          50 | -5.34%   | 0.64%              | -29.64% |    -0.05 |       52 | 29.28%     | ok               |
|          35 | -16.83%  | 0.64%              | -43.52% |    -0.25 |       76 | 44.76%     | ok               |
|          30 | -28.61%  | 0.64%              | -54.23% |    -0.51 |       77 | 51.41%     | ok               |

## SLV Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 67.45%   | 138.58%            | -34.10% |     0.86 |       52 | 34.78%     | ok               |
|          45 | 65.43%   | 138.58%            | -31.82% |     0.83 |       58 | 35.94%     | ok               |
|          40 | 63.45%   | 138.58%            | -31.93% |     0.82 |       64 | 38.10%     | ok               |
|          35 | 49.51%   | 138.58%            | -36.89% |     0.69 |       72 | 40.93%     | ok               |
|          20 | 51.50%   | 138.58%            | -42.66% |     0.69 |       66 | 48.42%     | ok               |

## SMH Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 89.40%   | 140.01%            | -31.01% |     1.14 |       49 | 49.42%     | ok               |
|          35 | 71.56%   | 140.01%            | -34.36% |     1.02 |       54 | 45.09%     | ok               |
|          25 | 71.43%   | 140.01%            | -32.94% |     1.01 |       46 | 48.09%     | ok               |
|          30 | 69.41%   | 140.01%            | -33.99% |     0.99 |       48 | 46.42%     | ok               |
|          45 | 57.09%   | 140.01%            | -32.75% |     0.93 |       52 | 39.27%     | ok               |

## SNX-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 0.97%    | -79.08%            | -43.20% |     0.28 |       73 | 48.28%     | ok               |
|          35 | 4.50%    | -79.08%            | -30.08% |     0.28 |       62 | 30.65%     | ok               |
|          40 | -6.60%   | -79.08%            | -31.85% |     0.11 |       50 | 24.52%     | ok               |
|          30 | -16.27%  | -79.08%            | -35.55% |     0.07 |       60 | 38.12%     | ok               |
|          15 | -28.54%  | -79.08%            | -44.00% |    -0.01 |       83 | 52.68%     | ok               |

## SOL-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -8.08%   | -56.37%            | -56.32% |     0.15 |       58 | 36.21%     | ok               |
|          25 | -32.87%  | -56.37%            | -53.21% |    -0.11 |       78 | 57.09%     | ok               |
|          35 | -31.99%  | -56.37%            | -62.56% |    -0.13 |       74 | 43.68%     | ok               |
|          45 | -29.84%  | -56.37%            | -63.23% |    -0.16 |       60 | 31.42%     | ok               |
|          15 | -40.84%  | -56.37%            | -59.14% |    -0.2  |       81 | 63.22%     | ok               |

## SOXX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 77.77%   | 119.06%            | -38.67% |     1.01 |       55 | 48.09%     | ok               |
|          25 | 75.26%   | 119.06%            | -39.85% |     0.99 |       51 | 47.59%     | ok               |
|          35 | 70.36%   | 119.06%            | -38.63% |     0.97 |       59 | 42.93%     | ok               |
|          30 | 65.41%   | 119.06%            | -40.34% |     0.91 |       55 | 45.42%     | ok               |
|          15 | 67.12%   | 119.06%            | -37.72% |     0.88 |       70 | 51.25%     | ok               |

## SPY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 13.36%   | 46.07%             | -14.25% |     0.48 |       59 | 53.08%     | ok               |
|          15 | 11.81%   | 46.07%             | -16.80% |     0.43 |       68 | 56.24%     | ok               |
|          25 | 6.31%    | 46.07%             | -15.22% |     0.27 |       59 | 52.08%     | ok               |
|          30 | 1.82%    | 46.07%             | -16.47% |     0.12 |       62 | 49.25%     | ok               |
|          35 | 1.21%    | 46.07%             | -16.72% |     0.1  |       58 | 46.26%     | ok               |

## SUSHI-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -28.52%  | -82.81%            | -40.08% |    -0.27 |       54 | 14.94%     | ok               |
|          40 | -64.04%  | -82.81%            | -70.25% |    -0.83 |       65 | 24.90%     | ok               |
|          45 | -61.31%  | -82.81%            | -65.82% |    -0.84 |       58 | 18.39%     | ok               |
|          15 | -79.55%  | -82.81%            | -81.69% |    -1    |       93 | 48.85%     | ok               |
|          35 | -76.26%  | -82.81%            | -81.46% |    -1.12 |       84 | 30.84%     | ok               |

## T Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 62.16%   | 43.62%             | -18.13% |     1.18 |       62 | 57.90%     | ok               |
|          25 | 57.77%   | 43.62%             | -17.66% |     1.13 |       62 | 55.57%     | ok               |
|          15 | 60.08%   | 43.62%             | -15.08% |     1.11 |       71 | 62.06%     | ok               |
|          30 | 40.49%   | 43.62%             | -17.01% |     0.88 |       66 | 53.58%     | ok               |
|          35 | 26.04%   | 43.62%             | -14.49% |     0.65 |       68 | 50.08%     | ok               |

## TGT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -20.85%  | -14.46%            | -42.86% |    -0.36 |       83 | 45.42%     | ok               |
|          25 | -21.64%  | -14.46%            | -43.36% |    -0.44 |       65 | 40.43%     | ok               |
|          30 | -21.08%  | -14.46%            | -40.57% |    -0.45 |       60 | 37.60%     | ok               |
|          15 | -25.86%  | -14.46%            | -40.77% |    -0.46 |       73 | 50.08%     | ok               |
|          45 | -19.49%  | -14.46%            | -29.07% |    -0.49 |       54 | 27.62%     | ok               |

## TIA-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 9.12%    | -91.33%            | -53.37% |     0.32 |       66 | 31.99%     | ok               |
|          40 | 0.83%    | -91.33%            | -46.21% |     0.23 |       68 | 26.63%     | ok               |
|          45 | -0.39%   | -91.33%            | -49.23% |     0.18 |       56 | 18.97%     | ok               |
|          50 | -1.36%   | -91.33%            | -48.70% |     0.13 |       36 | 11.88%     | ok               |
|          15 | -38.90%  | -91.33%            | -63.05% |    -0.07 |       98 | 54.02%     | ok               |

## TLT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -21.46%  | -11.73%            | -21.87% |    -1.65 |       72 | 33.61%     | ok               |
|          50 | -14.34%  | -11.73%            | -15.73% |    -1.66 |       34 | 15.97%     | ok               |
|          40 | -19.66%  | -11.73%            | -19.91% |    -1.87 |       58 | 23.13%     | ok               |
|          15 | -27.21%  | -11.73%            | -27.76% |    -1.91 |       77 | 41.60%     | ok               |
|          35 | -22.22%  | -11.73%            | -22.47% |    -1.94 |       66 | 27.79%     | ok               |

## TMO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 48.79%   | -1.40%             | -8.17%  |     1.07 |       44 | 32.95%     | ok               |
|          45 | 42.34%   | -1.40%             | -10.13% |     0.91 |       48 | 37.94%     | ok               |
|          40 | 41.04%   | -1.40%             | -9.91%  |     0.87 |       51 | 42.60%     | ok               |
|          35 | 33.89%   | -1.40%             | -14.06% |     0.71 |       61 | 47.25%     | ok               |
|          30 | 27.89%   | -1.40%             | -18.85% |     0.6  |       61 | 52.41%     | ok               |

## TMUS Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 6.39%    | 9.94%              | -30.05% |     0.23 |       65 | 58.74%     | ok               |
|          30 | 5.20%    | 9.94%              | -25.71% |     0.21 |       70 | 46.76%     | ok               |
|          20 | 0.25%    | 9.94%              | -29.75% |     0.11 |       71 | 53.08%     | ok               |
|          25 | -3.11%   | 9.94%              | -31.45% |     0.03 |       75 | 49.25%     | ok               |
|          50 | -4.93%   | 9.94%              | -28.89% |    -0.06 |       60 | 34.78%     | ok               |

## TRX-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 8.10%    | 31.89%             | -18.79% |     0.32 |       50 | 36.21%     | ok               |
|          30 | 4.26%    | 31.89%             | -22.90% |     0.2  |       68 | 48.08%     | ok               |
|          35 | 3.40%    | 31.89%             | -21.77% |     0.18 |       64 | 44.83%     | ok               |
|          50 | 2.12%    | 31.89%             | -18.49% |     0.14 |       42 | 31.80%     | ok               |
|          25 | 1.62%    | 31.89%             | -26.84% |     0.13 |       66 | 51.15%     | ok               |

## TSLA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 56.97%   | 70.10%             | -32.60% |     0.73 |       66 | 29.95%     | ok               |
|          40 | 35.84%   | 70.10%             | -45.90% |     0.53 |       65 | 34.78%     | ok               |
|          45 | 15.08%   | 70.10%             | -46.86% |     0.35 |       69 | 32.11%     | ok               |
|          35 | 3.85%    | 70.10%             | -51.29% |     0.24 |       74 | 37.44%     | ok               |
|          30 | -14.12%  | 70.10%             | -54.91% |     0.05 |       72 | 41.43%     | ok               |

## TXN Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 12.02%   | 62.37%             | -45.45% |     0.31 |       66 | 34.28%     | ok               |
|          20 | -0.22%   | 62.37%             | -38.49% |     0.15 |       60 | 57.74%     | ok               |
|          15 | -3.08%   | 62.37%             | -38.99% |     0.11 |       63 | 61.73%     | ok               |
|          35 | -4.79%   | 62.37%             | -43.28% |     0.06 |       74 | 48.75%     | ok               |
|          40 | -7.49%   | 62.37%             | -45.67% |     0.01 |       72 | 46.59%     | ok               |

## UNH Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 25.37%   | -9.38%             | -28.69% |     0.47 |       74 | 52.91%     | ok               |
|          15 | 26.29%   | -9.38%             | -33.62% |     0.47 |       73 | 67.39%     | ok               |
|          50 | 23.40%   | -9.38%             | -37.02% |     0.46 |       60 | 30.95%     | ok               |
|          35 | 22.77%   | -9.38%             | -30.02% |     0.44 |       66 | 47.59%     | ok               |
|          25 | 13.87%   | -9.38%             | -29.76% |     0.33 |       72 | 58.07%     | ok               |

## UNI-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -24.72%  | -57.91%            | -63.24% |    -0.06 |       62 | 34.10%     | ok               |
|          45 | -26.56%  | -57.91%            | -57.91% |    -0.11 |       62 | 28.93%     | ok               |
|          35 | -38.40%  | -57.91%            | -68.27% |    -0.21 |       74 | 40.23%     | ok               |
|          50 | -34.38%  | -57.91%            | -57.01% |    -0.28 |       58 | 22.22%     | ok               |
|          15 | -76.91%  | -57.91%            | -85.38% |    -0.86 |      111 | 60.34%     | ok               |

## UPS Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -36.51%  | -29.49%            | -43.07% |    -0.68 |       82 | 48.75%     | ok               |
|          25 | -37.52%  | -29.49%            | -39.08% |    -0.72 |       78 | 45.26%     | ok               |
|          15 | -38.75%  | -29.49%            | -43.86% |    -0.72 |       84 | 52.58%     | ok               |
|          35 | -38.78%  | -29.49%            | -40.08% |    -0.8  |       67 | 34.44%     | ok               |
|          30 | -41.39%  | -29.49%            | -41.62% |    -0.86 |       72 | 40.27%     | ok               |

## USO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 18.37%   | 64.04%             | -33.25% |     0.4  |       50 | 27.45%     | ok               |
|          20 | 16.55%   | 64.04%             | -45.57% |     0.37 |       75 | 40.43%     | ok               |
|          15 | 11.05%   | 64.04%             | -45.74% |     0.3  |       74 | 43.59%     | ok               |
|          30 | 10.35%   | 64.04%             | -43.35% |     0.29 |       68 | 34.94%     | ok               |
|          25 | 7.40%    | 64.04%             | -44.86% |     0.25 |       69 | 37.94%     | ok               |

## VEA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 6.11%    | 42.19%             | -16.28% |     0.27 |       58 | 50.08%     | ok               |
|          20 | 1.83%    | 42.19%             | -17.70% |     0.13 |       59 | 47.42%     | ok               |
|          25 | -0.19%   | 42.19%             | -17.79% |     0.05 |       55 | 45.76%     | ok               |
|          30 | -0.35%   | 42.19%             | -17.93% |     0.04 |       56 | 43.59%     | ok               |
|          35 | -1.46%   | 42.19%             | -16.79% |    -0.01 |       54 | 42.60%     | ok               |

## VIXY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -48.04%  | -62.21%            | -69.78% |    -0.43 |       46 | 10.50%     | ok               |
|          45 | -57.65%  | -62.21%            | -75.03% |    -0.58 |       58 | 16.50%     | ok               |
|          40 | -65.68%  | -62.21%            | -80.72% |    -0.69 |       72 | 20.83%     | ok               |
|          35 | -69.78%  | -62.21%            | -84.29% |    -0.74 |       90 | 26.00%     | ok               |
|          15 | -76.29%  | -62.21%            | -89.47% |    -0.75 |       99 | 43.50%     | ok               |

## VNQ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -7.66%   | 16.95%             | -19.07% |    -0.32 |       56 | 28.12%     | ok               |
|          50 | -8.10%   | 16.95%             | -17.13% |    -0.36 |       52 | 25.62%     | ok               |
|          25 | -11.87%  | 16.95%             | -22.16% |    -0.45 |       64 | 40.27%     | ok               |
|          20 | -13.49%  | 16.95%             | -23.61% |    -0.51 |       67 | 42.93%     | ok               |
|          15 | -14.80%  | 16.95%             | -24.73% |    -0.56 |       64 | 44.09%     | ok               |

## VTI Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 16.22%   | 45.26%             | -13.96% |     0.56 |       62 | 53.58%     | ok               |
|          15 | 10.27%   | 45.26%             | -15.70% |     0.38 |       65 | 56.07%     | ok               |
|          25 | 2.79%    | 45.26%             | -16.10% |     0.16 |       58 | 51.58%     | ok               |
|          30 | -4.92%   | 45.26%             | -18.77% |    -0.12 |       68 | 49.58%     | ok               |
|          40 | -6.28%   | 45.26%             | -20.44% |    -0.19 |       68 | 42.43%     | ok               |

## VWO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -7.80%   | 40.42%             | -24.01% |    -0.22 |       73 | 48.59%     | ok               |
|          50 | -7.14%   | 40.42%             | -21.18% |    -0.25 |       58 | 30.95%     | ok               |
|          20 | -8.84%   | 40.42%             | -26.14% |    -0.26 |       71 | 46.42%     | ok               |
|          40 | -8.87%   | 40.42%             | -23.57% |    -0.31 |       70 | 36.27%     | ok               |
|          45 | -8.95%   | 40.42%             | -23.26% |    -0.32 |       60 | 33.44%     | ok               |

## VZ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -3.19%   | 19.43%             | -12.71% |    -0.05 |       52 | 24.63%     | ok               |
|          45 | -14.75%  | 19.43%             | -20.96% |    -0.46 |       66 | 28.29%     | ok               |
|          35 | -15.97%  | 19.43%             | -22.26% |    -0.48 |       61 | 34.11%     | ok               |
|          25 | -17.94%  | 19.43%             | -22.13% |    -0.48 |       81 | 42.26%     | ok               |
|          40 | -20.67%  | 19.43%             | -23.75% |    -0.68 |       66 | 31.45%     | ok               |

## WFC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | -9.89%   | 53.48%             | -22.54% |    -0.15 |       81 | 46.92%     | ok               |
|          50 | -7.12%   | 53.48%             | -18.29% |    -0.16 |       62 | 34.61%     | ok               |
|          20 | -16.98%  | 53.48%             | -29.87% |    -0.23 |       79 | 56.07%     | ok               |
|          30 | -19.28%  | 53.48%             | -29.78% |    -0.33 |       84 | 50.08%     | ok               |
|          45 | -14.99%  | 53.48%             | -24.02% |    -0.38 |       70 | 39.77%     | ok               |

## WIF-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 45.70%   | -77.96%            | -46.21% |     0.59 |       74 | 43.30%     | ok               |
|          20 | 41.91%   | -77.96%            | -40.67% |     0.57 |       67 | 40.42%     | ok               |
|          25 | -23.50%  | -77.96%            | -52.41% |     0.08 |       71 | 37.74%     | ok               |
|          50 | -20.06%  | -77.96%            | -37.87% |    -0.14 |       40 | 12.07%     | ok               |
|          30 | -51.48%  | -77.96%            | -60.60% |    -0.37 |       70 | 33.72%     | ok               |

## WMT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 43.21%   | 88.37%             | -9.18%  |     1.22 |       40 | 40.77%     | ok               |
|          50 | 37.68%   | 88.37%             | -12.19% |     1.15 |       34 | 38.27%     | ok               |
|          40 | 31.29%   | 88.37%             | -13.41% |     0.92 |       46 | 42.10%     | ok               |
|          35 | 30.43%   | 88.37%             | -13.99% |     0.87 |       56 | 46.76%     | ok               |
|          15 | 16.86%   | 88.37%             | -25.74% |     0.45 |       72 | 60.90%     | ok               |

## XBI Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 0.41%    | 50.59%             | -16.08% |     0.09 |       60 | 34.78%     | ok               |
|          45 | -0.36%   | 50.59%             | -15.46% |     0.07 |       52 | 31.61%     | ok               |
|          35 | -7.14%   | 50.59%             | -16.96% |    -0.11 |       66 | 38.44%     | ok               |
|          30 | -8.17%   | 50.59%             | -18.30% |    -0.13 |       66 | 40.10%     | ok               |
|          25 | -10.41%  | 50.59%             | -23.66% |    -0.18 |       76 | 42.43%     | ok               |

## XLB Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -2.32%   | 18.78%             | -20.68% |    -0.03 |       54 | 31.11%     | ok               |
|          50 | -2.38%   | 18.78%             | -17.59% |    -0.05 |       42 | 26.79%     | ok               |
|          35 | -5.53%   | 18.78%             | -23.62% |    -0.15 |       56 | 34.44%     | ok               |
|          45 | -5.27%   | 18.78%             | -20.79% |    -0.16 |       42 | 28.29%     | ok               |
|          25 | -7.48%   | 18.78%             | -22.63% |    -0.22 |       60 | 39.77%     | ok               |

## XLC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 11.88%   | 40.01%             | -12.33% |     0.44 |       67 | 52.75%     | ok               |
|          25 | 9.12%    | 40.01%             | -12.31% |     0.35 |       66 | 54.58%     | ok               |
|          40 | 7.83%    | 40.01%             | -13.38% |     0.34 |       66 | 45.76%     | ok               |
|          35 | 7.01%    | 40.01%             | -13.38% |     0.3  |       64 | 49.92%     | ok               |
|          45 | 2.84%    | 40.01%             | -13.21% |     0.16 |       64 | 42.93%     | ok               |

## XLE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 6.21%    | 32.57%             | -25.98% |     0.25 |       54 | 36.11%     | ok               |
|          45 | 1.86%    | 32.57%             | -29.68% |     0.13 |       60 | 38.10%     | ok               |
|          35 | -0.28%   | 32.57%             | -31.51% |     0.08 |       65 | 42.76%     | ok               |
|          25 | -6.89%   | 32.57%             | -36.05% |    -0.08 |       83 | 48.25%     | ok               |
|          40 | -6.78%   | 32.57%             | -34.51% |    -0.12 |       64 | 40.60%     | ok               |

## XLF Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -2.74%   | 42.57%             | -18.01% |    -0.03 |       68 | 53.91%     | ok               |
|          15 | -6.77%   | 42.57%             | -19.58% |    -0.16 |       76 | 56.74%     | ok               |
|          25 | -9.53%   | 42.57%             | -23.22% |    -0.28 |       77 | 50.42%     | ok               |
|          30 | -9.57%   | 42.57%             | -23.61% |    -0.3  |       78 | 48.09%     | ok               |
|          35 | -17.53%  | 42.57%             | -26.13% |    -0.68 |       70 | 44.09%     | ok               |

## XLI Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 5.44%    | 50.87%             | -10.36% |     0.25 |       76 | 51.08%     | ok               |
|          20 | 1.33%    | 50.87%             | -12.74% |     0.11 |       69 | 46.59%     | ok               |
|          30 | -2.81%   | 50.87%             | -11.79% |    -0.06 |       68 | 43.76%     | ok               |
|          45 | -3.37%   | 50.87%             | -14.01% |    -0.11 |       66 | 34.94%     | ok               |
|          25 | -3.98%   | 50.87%             | -12.51% |    -0.11 |       66 | 44.59%     | ok               |

## XLK Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 88.82%   | 66.45%             | -14.75% |     1.4  |       41 | 51.08%     | ok               |
|          20 | 71.51%   | 66.45%             | -14.75% |     1.23 |       46 | 48.92%     | ok               |
|          25 | 68.02%   | 66.45%             | -14.75% |     1.23 |       40 | 46.76%     | ok               |
|          30 | 65.83%   | 66.45%             | -14.75% |     1.22 |       40 | 45.59%     | ok               |
|          35 | 47.33%   | 66.45%             | -13.61% |     0.99 |       52 | 42.93%     | ok               |

## XLM-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 27.47%   | -48.09%            | -38.97% |     0.49 |       44 | 27.20%     | ok               |
|          45 | 23.64%   | -48.09%            | -43.99% |     0.45 |       50 | 30.84%     | ok               |
|          30 | 11.39%   | -48.09%            | -50.36% |     0.34 |       67 | 45.59%     | ok               |
|          40 | 2.83%    | -48.09%            | -43.80% |     0.24 |       49 | 35.25%     | ok               |
|          25 | -3.53%   | -48.09%            | -48.11% |     0.19 |       71 | 48.28%     | ok               |

## XLP Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 9.70%    | 16.55%             | -5.66%  |     0.61 |       52 | 32.61%     | ok               |
|          50 | 8.29%    | 16.55%             | -6.08%  |     0.54 |       54 | 30.45%     | ok               |
|          40 | 7.50%    | 16.55%             | -7.77%  |     0.47 |       68 | 36.77%     | ok               |
|          35 | 6.56%    | 16.55%             | -9.73%  |     0.41 |       64 | 39.77%     | ok               |
|          30 | 4.67%    | 16.55%             | -11.16% |     0.3  |       66 | 41.26%     | ok               |

## XLU Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 5.85%    | 45.48%             | -12.97% |     0.32 |       52 | 31.28%     | ok               |
|          45 | 4.45%    | 45.48%             | -14.27% |     0.25 |       54 | 32.28%     | ok               |
|          40 | 1.57%    | 45.48%             | -15.59% |     0.12 |       58 | 33.78%     | ok               |
|          35 | -4.35%   | 45.48%             | -19.71% |    -0.16 |       62 | 35.94%     | ok               |
|          30 | -5.24%   | 45.48%             | -20.40% |    -0.19 |       67 | 39.10%     | ok               |

## XLV Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -14.30%  | 15.33%             | -18.96% |    -0.7  |       68 | 35.11%     | ok               |
|          25 | -14.98%  | 15.33%             | -21.14% |    -0.73 |       70 | 36.94%     | ok               |
|          20 | -18.19%  | 15.33%             | -24.51% |    -0.89 |       75 | 38.77%     | ok               |
|          15 | -18.71%  | 15.33%             | -24.84% |    -0.89 |       83 | 41.76%     | ok               |
|          35 | -18.78%  | 15.33%             | -22.99% |    -1.01 |       66 | 32.61%     | ok               |

## XLY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 8.22%    | 24.80%             | -14.01% |     0.32 |       66 | 44.43%     | ok               |
|          35 | 5.60%    | 24.80%             | -12.94% |     0.24 |       70 | 41.76%     | ok               |
|          15 | 5.45%    | 24.80%             | -15.77% |     0.22 |       70 | 50.58%     | ok               |
|          20 | 2.61%    | 24.80%             | -19.25% |     0.15 |       65 | 47.25%     | ok               |
|          25 | -0.86%   | 24.80%             | -19.25% |     0.04 |       65 | 45.76%     | ok               |

## XOM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | 9.62%    | 44.87%             | -19.90% |     0.33 |       55 | 38.27%     | ok               |
|          50 | 8.67%    | 44.87%             | -21.35% |     0.32 |       38 | 30.45%     | ok               |
|          30 | 8.53%    | 44.87%             | -20.29% |     0.3  |       55 | 37.60%     | ok               |
|          20 | 1.87%    | 44.87%             | -25.56% |     0.13 |       64 | 40.43%     | ok               |
|          45 | 1.66%    | 44.87%             | -23.33% |     0.12 |       44 | 31.95%     | ok               |

## XRP-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | -13.80%  | -58.31%            | -38.85% |     0.02 |       64 | 38.89%     | ok               |
|          40 | -22.96%  | -58.31%            | -38.94% |    -0.14 |       54 | 33.14%     | ok               |
|          30 | -27.75%  | -58.31%            | -47.86% |    -0.17 |       66 | 43.10%     | ok               |
|          45 | -31.57%  | -58.31%            | -40.24% |    -0.3  |       54 | 28.93%     | ok               |
|          50 | -27.85%  | -58.31%            | -38.03% |    -0.32 |       56 | 21.46%     | ok               |

## YFI-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -50.49%  | -66.74%            | -51.52% |    -0.84 |       60 | 27.78%     | ok               |
|          30 | -64.19%  | -66.74%            | -71.12% |    -1.03 |       81 | 40.61%     | ok               |
|          45 | -49.89%  | -66.74%            | -53.41% |    -1.04 |       70 | 22.22%     | ok               |
|          35 | -62.10%  | -66.74%            | -63.29% |    -1.04 |       67 | 35.25%     | ok               |
|          25 | -67.98%  | -66.74%            | -73.07% |    -1.12 |       78 | 46.17%     | ok               |

## ZEC-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 105.68%  | 1175.06%           | -24.66% |     0.83 |       44 | 24.90%     | ok               |
|          35 | 76.00%   | 1175.06%           | -44.34% |     0.7  |       52 | 31.03%     | ok               |
|          25 | 57.65%   | 1175.06%           | -51.18% |     0.62 |       58 | 40.04%     | ok               |
|          50 | 41.39%   | 1175.06%           | -34.17% |     0.53 |       46 | 22.41%     | ok               |
|          40 | 40.16%   | 1175.06%           | -48.16% |     0.53 |       54 | 28.74%     | ok               |
