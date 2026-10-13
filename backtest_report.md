# Market Tracker Backtest Report

_Generated: 2026-10-13T06:52:27+00:00_

## Data Sources

- Crypto: Kraken -> Coinbase -> CoinGecko OHLC -> CoinPaprika fallback chain.
- Stocks / ETFs / indices: Stooq -> Yahoo Finance fallback chain.
- Data rows are generated from real market APIs. Mock OHLCV rows are not generated.

## Data Freshness

- Rows: **92,736**
- Symbols: **161**
- Date range: **2024-05-20** to **2026-10-13**

## Latest Signals

| symbol     | date                |         close |   composite_score | signal   | data_source   |
|:-----------|:--------------------|--------------:|------------------:|:---------|:--------------|
| ABBV       | 2026-10-12 00:00:00 |   281.12      |        74.0833    | LONG     | Yahoo Finance |
| ALGO-USD   | 2026-10-13 00:00:00 |     0.12103   |        35.8333    | LONG     | Kraken API    |
| AMAT       | 2026-10-12 00:00:00 |   497.53      |        61         | LONG     | Yahoo Finance |
| AMGN       | 2026-10-12 00:00:00 |   417.57      |        72.4167    | LONG     | Yahoo Finance |
| CL         | 2026-10-12 00:00:00 |    89.98      |        55.6667    | LONG     | Yahoo Finance |
| COMP-USD   | 2026-10-13 00:00:00 |    23.98      |        30.6667    | LONG     | Kraken API    |
| COP        | 2026-10-12 00:00:00 |   137.56      |        71.25      | LONG     | Yahoo Finance |
| COST       | 2026-10-12 00:00:00 |   959.44      |        55.25      | LONG     | Yahoo Finance |
| CRM        | 2026-10-12 00:00:00 |   233.92      |        34.5833    | LONG     | Yahoo Finance |
| CSCO       | 2026-10-12 00:00:00 |   115.34      |        68.25      | LONG     | Yahoo Finance |
| DIA        | 2026-10-12 00:00:00 |   517.91      |        39.25      | LONG     | Yahoo Finance |
| DXY-INDEX  | 2026-10-13 00:00:00 |   102.407     |        76.3441    | LONG     | Yahoo Finance |
| IBIT       | 2026-10-12 00:00:00 |    46.86      |        38.1667    | LONG     | Yahoo Finance |
| LIN        | 2026-10-12 00:00:00 |   487.35      |        68         | LONG     | Yahoo Finance |
| LLY        | 2026-10-12 00:00:00 |  1182.62      |        69.0833    | LONG     | Yahoo Finance |
| META       | 2026-10-12 00:00:00 |   742.96      |        54.5833    | LONG     | Yahoo Finance |
| MSFT       | 2026-10-12 00:00:00 |   541.15      |        71.25      | LONG     | Yahoo Finance |
| NEAR-USD   | 2026-10-13 00:00:00 |     5.31      |        42.3333    | LONG     | Kraken API    |
| NVDA       | 2026-10-12 00:00:00 |   226.32      |        15.9167    | LONG     | Yahoo Finance |
| OXY        | 2026-10-12 00:00:00 |    61.13      |        71.25      | LONG     | Yahoo Finance |
| QQQ        | 2026-10-12 00:00:00 |   746.04      |        57.25      | LONG     | Yahoo Finance |
| RENDER-USD | 2026-10-13 00:00:00 |     2.178     |        54.25      | LONG     | Kraken API    |
| TIA-USD    | 2026-10-13 00:00:00 |     0.6246    |        67.75      | LONG     | Kraken API    |
| TMO        | 2026-10-12 00:00:00 |   662.24      |        45.0833    | LONG     | Yahoo Finance |
| TXN        | 2026-10-12 00:00:00 |   281.74      |        69.9167    | LONG     | Yahoo Finance |
| UNH        | 2026-10-12 00:00:00 |   378.52      |        53.1667    | LONG     | Yahoo Finance |
| XLE        | 2026-10-12 00:00:00 |    66.01      |        73.25      | LONG     | Yahoo Finance |
| XLF        | 2026-10-12 00:00:00 |    55.05      |        44.4167    | LONG     | Yahoo Finance |
| XLK        | 2026-10-12 00:00:00 |   196.36      |        50.5833    | LONG     | Yahoo Finance |
| XLP        | 2026-10-12 00:00:00 |    84.41      |        55.6667    | LONG     | Yahoo Finance |
| AAPL       | 2026-10-12 00:00:00 |   340.97      |        39.8333    | NEUTRAL  | Yahoo Finance |
| AAVE-USD   | 2026-10-13 00:00:00 |   160.99      |        10.6667    | NEUTRAL  | Kraken API    |
| ADA-USD    | 2026-10-13 00:00:00 |     0.239838  |       -10.9167    | NEUTRAL  | Kraken API    |
| ADBE       | 2026-10-12 00:00:00 |   238.14      |       -12         | NEUTRAL  | Yahoo Finance |
| AMD        | 2026-10-12 00:00:00 |   594.24      |        13.9167    | NEUTRAL  | Yahoo Finance |
| AMZN       | 2026-10-12 00:00:00 |   259.53      |        59.1667    | NEUTRAL  | Yahoo Finance |
| APT-USD    | 2026-10-13 00:00:00 |     0.8481    |        21         | NEUTRAL  | Kraken API    |
| ARB-USD    | 2026-10-13 00:00:00 |     0.19      |        14.3333    | NEUTRAL  | Kraken API    |
| ARKK       | 2026-10-12 00:00:00 |    88.02      |         4.66667   | NEUTRAL  | Yahoo Finance |
| ATOM-USD   | 2026-10-13 00:00:00 |     1.8213    |        53.0833    | NEUTRAL  | Kraken API    |
| AVAX-USD   | 2026-10-13 00:00:00 |    10.567     |        21.4167    | NEUTRAL  | Kraken API    |
| AVGO       | 2026-10-12 00:00:00 |   354.73      |       -50         | NEUTRAL  | Yahoo Finance |
| BAC        | 2026-10-12 00:00:00 |    54.58      |        -7.5       | NEUTRAL  | Yahoo Finance |
| BITO       | 2026-10-12 00:00:00 |    11.06      |         9.41667   | NEUTRAL  | Yahoo Finance |
| BLK        | 2026-10-12 00:00:00 |  1083.92      |        44.25      | NEUTRAL  | Yahoo Finance |
| BTC-USD    | 2026-10-13 00:00:00 | 83634.3       |        23.25      | NEUTRAL  | Kraken API    |
| C          | 2026-10-12 00:00:00 |   131.92      |         5.41667   | NEUTRAL  | Yahoo Finance |
| CAT        | 2026-10-12 00:00:00 |   799.37      |       -22.75      | NEUTRAL  | Yahoo Finance |
| CRV-USD    | 2026-10-13 00:00:00 |     0.36652   |        13.6667    | NEUTRAL  | Kraken API    |
| CVX        | 2026-10-12 00:00:00 |   215         |        44         | NEUTRAL  | Yahoo Finance |
| DASH-USD   | 2026-10-13 00:00:00 |    50.602     |       -20.9167    | NEUTRAL  | Kraken API    |
| DBC        | 2026-10-12 00:00:00 |    33.33      |        52.25      | NEUTRAL  | Yahoo Finance |
| DE         | 2026-10-12 00:00:00 |   632.61      |       -19.0833    | NEUTRAL  | Yahoo Finance |
| DIS        | 2026-10-12 00:00:00 |   108.49      |        64.8333    | NEUTRAL  | Yahoo Finance |
| DOT-USD    | 2026-10-13 00:00:00 |     1.2136    |        35         | NEUTRAL  | Kraken API    |
| EEM        | 2026-10-12 00:00:00 |    66.15      |       -45         | NEUTRAL  | Yahoo Finance |
| EOG        | 2026-10-12 00:00:00 |   150.51      |        60         | NEUTRAL  | Yahoo Finance |
| ETC-USD    | 2026-10-13 00:00:00 |     8.241     |       -11.5833    | NEUTRAL  | Kraken API    |
| ETH-USD    | 2026-10-13 00:00:00 |  2531.3       |        -0.166667  | NEUTRAL  | Kraken API    |
| EWJ        | 2026-10-12 00:00:00 |    97.32      |        -2.08333   | NEUTRAL  | Yahoo Finance |
| FCX        | 2026-10-12 00:00:00 |    73.29      |        31.1667    | NEUTRAL  | Yahoo Finance |
| FET-USD    | 2026-10-13 00:00:00 |     0.2198    |        17.8333    | NEUTRAL  | Kraken API    |
| FIL-USD    | 2026-10-13 00:00:00 |     1.169     |        38.5       | NEUTRAL  | Kraken API    |
| FXI        | 2026-10-12 00:00:00 |    34.14      |       -26         | NEUTRAL  | Yahoo Finance |
| GE         | 2026-10-12 00:00:00 |   308.64      |       -49.1667    | NEUTRAL  | Yahoo Finance |
| GOOGL      | 2026-10-12 00:00:00 |   352.72      |        52.5833    | NEUTRAL  | Yahoo Finance |
| GRT-USD    | 2026-10-13 00:00:00 |     0.0265    |        18.0833    | NEUTRAL  | Kraken API    |
| IBM        | 2026-10-12 00:00:00 |   227.02      |       -41.75      | NEUTRAL  | Yahoo Finance |
| ICP-USD    | 2026-10-13 00:00:00 |     3.188     |        26.6667    | NEUTRAL  | Kraken API    |
| IEMG       | 2026-10-12 00:00:00 |    80.63      |       -46.75      | NEUTRAL  | Yahoo Finance |
| INJ-USD    | 2026-10-13 00:00:00 |     7.958     |        31.5       | NEUTRAL  | Kraken API    |
| INTC       | 2026-10-12 00:00:00 |   101.35      |        -5.66667   | NEUTRAL  | Yahoo Finance |
| INTU       | 2026-10-12 00:00:00 |   305.99      |        22.4167    | NEUTRAL  | Yahoo Finance |
| ITA        | 2026-10-12 00:00:00 |   206.03      |       -29.25      | NEUTRAL  | Yahoo Finance |
| IWM        | 2026-10-12 00:00:00 |   277.9       |        -3.5       | NEUTRAL  | Yahoo Finance |
| JNJ        | 2026-10-12 00:00:00 |   263.73      |        -4.33333   | NEUTRAL  | Yahoo Finance |
| JPM        | 2026-10-12 00:00:00 |   334.3       |        -6.08333   | NEUTRAL  | Yahoo Finance |
| KO         | 2026-10-12 00:00:00 |    89.79      |        58.6667    | NEUTRAL  | Yahoo Finance |
| LDO-USD    | 2026-10-13 00:00:00 |     0.418     |        -0.833333  | NEUTRAL  | Kraken API    |
| LINK-USD   | 2026-10-13 00:00:00 |    13.0905    |         7.33333   | NEUTRAL  | Kraken API    |
| LRCX       | 2026-10-12 00:00:00 |   309.56      |         1.66667   | NEUTRAL  | Yahoo Finance |
| LTC-USD    | 2026-10-13 00:00:00 |    62.17      |        16.3333    | NEUTRAL  | Kraken API    |
| MPC        | 2026-10-12 00:00:00 |   458.81      |        64         | NEUTRAL  | Yahoo Finance |
| MRK        | 2026-10-12 00:00:00 |   145.45      |         9.5       | NEUTRAL  | Yahoo Finance |
| MU         | 2026-10-12 00:00:00 |   989.04      |        -2.08333   | NEUTRAL  | Yahoo Finance |
| NFLX       | 2026-10-12 00:00:00 |    70.61      |       -15.25      | NEUTRAL  | Yahoo Finance |
| NKE        | 2026-10-12 00:00:00 |    35.35      |       -29         | NEUTRAL  | Yahoo Finance |
| NOW        | 2026-10-12 00:00:00 |   140.32      |        51.8333    | NEUTRAL  | Yahoo Finance |
| OP-USD     | 2026-10-13 00:00:00 |     0.1381    |         9.75      | NEUTRAL  | Kraken API    |
| ORCL       | 2026-10-12 00:00:00 |   137.39      |       -45.3333    | NEUTRAL  | Yahoo Finance |
| PEPE-USD   | 2026-10-13 00:00:00 |     4.127e-06 |        25.3333    | NEUTRAL  | Kraken API    |
| PFE        | 2026-10-12 00:00:00 |    28.4       |        40.8333    | NEUTRAL  | Yahoo Finance |
| PG         | 2026-10-12 00:00:00 |   153.2       |        71.9167    | NEUTRAL  | Yahoo Finance |
| PM         | 2026-10-12 00:00:00 |   202         |        64         | NEUTRAL  | Yahoo Finance |
| POL-USD    | 2026-10-13 00:00:00 |     0.10486   |        -8.83333   | NEUTRAL  | Kraken API    |
| QCOM       | 2026-10-12 00:00:00 |   174.43      |       -22.8333    | NEUTRAL  | Yahoo Finance |
| RTX        | 2026-10-12 00:00:00 |   186.66      |       -29.25      | NEUTRAL  | Yahoo Finance |
| SCHW       | 2026-10-12 00:00:00 |    97.06      |       -29.8333    | NEUTRAL  | Yahoo Finance |
| SKY-USD    | 2026-10-13 00:00:00 |     0.07776   |        -0.0833333 | NEUTRAL  | Kraken API    |
| SMH        | 2026-10-12 00:00:00 |   590.99      |        24.9167    | NEUTRAL  | Yahoo Finance |
| SNX-USD    | 2026-10-13 00:00:00 |     0.2446    |         5.33333   | NEUTRAL  | Kraken API    |
| SOL-USD    | 2026-10-13 00:00:00 |   108.52      |         2.66667   | NEUTRAL  | Kraken API    |
| SOXX       | 2026-10-12 00:00:00 |   544.85      |         6.91667   | NEUTRAL  | Yahoo Finance |
| SPY        | 2026-10-12 00:00:00 |   778.1       |        52.5833    | NEUTRAL  | Yahoo Finance |
| SUSHI-USD  | 2026-10-13 00:00:00 |     0.2376    |         2.75      | NEUTRAL  | Kraken API    |
| TGT        | 2026-10-12 00:00:00 |   153.62      |       -26.8333    | NEUTRAL  | Yahoo Finance |
| TRX-USD    | 2026-10-13 00:00:00 |     0.329937  |       -42.5833    | NEUTRAL  | Kraken API    |
| TSLA       | 2026-10-12 00:00:00 |   378.03      |        39.6667    | NEUTRAL  | Yahoo Finance |
| UNI-USD    | 2026-10-13 00:00:00 |     7.4181    |         2.41667   | NEUTRAL  | Kraken API    |
| UPS        | 2026-10-12 00:00:00 |    95.34      |       -25.25      | NEUTRAL  | Yahoo Finance |
| USO        | 2026-10-12 00:00:00 |   151.03      |        48.25      | NEUTRAL  | Yahoo Finance |
| VIXY       | 2026-10-12 00:00:00 |    16.04      |       -37.6667    | NEUTRAL  | Yahoo Finance |
| VNQ        | 2026-10-12 00:00:00 |    91.36      |        -7.25      | NEUTRAL  | Yahoo Finance |
| VTI        | 2026-10-12 00:00:00 |   381.57      |        54.3333    | NEUTRAL  | Yahoo Finance |
| VWO        | 2026-10-12 00:00:00 |    59.73      |       -33.5       | NEUTRAL  | Yahoo Finance |
| WFC        | 2026-10-12 00:00:00 |    83.32      |         0.666667  | NEUTRAL  | Yahoo Finance |
| WMT        | 2026-10-12 00:00:00 |   113.08      |        51.3333    | NEUTRAL  | Yahoo Finance |
| XBI        | 2026-10-12 00:00:00 |   151.4       |       -28.5       | NEUTRAL  | Yahoo Finance |
| XLC        | 2026-10-12 00:00:00 |   111.45      |       -57.0833    | NEUTRAL  | Yahoo Finance |
| XLI        | 2026-10-12 00:00:00 |   169.15      |       -36.4167    | NEUTRAL  | Yahoo Finance |
| XLM-USD    | 2026-10-13 00:00:00 |     0.195164  |       -10         | NEUTRAL  | Kraken API    |
| XLU        | 2026-10-12 00:00:00 |    41.63      |         5.16667   | NEUTRAL  | Yahoo Finance |
| XLV        | 2026-10-12 00:00:00 |   171.99      |        65.1667    | NEUTRAL  | Yahoo Finance |
| XLY        | 2026-10-12 00:00:00 |   112.27      |        -6.16667   | NEUTRAL  | Yahoo Finance |
| XOM        | 2026-10-12 00:00:00 |   172.15      |        44         | NEUTRAL  | Yahoo Finance |
| XRP-USD    | 2026-10-13 00:00:00 |     1.37491   |       -38.5833    | NEUTRAL  | Kraken API    |
| YFI-USD    | 2026-10-13 00:00:00 |  2339.8       |       -10.5833    | NEUTRAL  | Kraken API    |
| ZEC-USD    | 2026-10-13 00:00:00 |  1217.12      |        -5.58333   | NEUTRAL  | Kraken API    |
| AGG        | 2026-10-12 00:00:00 |    94.66      |       -40.0833    | SHORT    | Yahoo Finance |
| BA         | 2026-10-12 00:00:00 |   189.5       |       -38.3333    | SHORT    | Yahoo Finance |
| BCH-USD    | 2026-10-13 00:00:00 |   274.14      |       -33.5833    | SHORT    | Kraken API    |
| BND        | 2026-10-12 00:00:00 |    70.25      |       -40.0833    | SHORT    | Yahoo Finance |
| BONK-USD   | 2026-10-13 00:00:00 |     3.295e-06 |       -32.5833    | SHORT    | Kraken API    |
| CMCSA      | 2026-10-12 00:00:00 |    20.68      |       -54.9167    | SHORT    | Yahoo Finance |
| DOGE-USD   | 2026-10-13 00:00:00 |     0.0849117 |       -40.5833    | SHORT    | Kraken API    |
| EFA        | 2026-10-12 00:00:00 |   103.05      |       -33.5       | SHORT    | Yahoo Finance |
| GDX        | 2026-10-12 00:00:00 |    88.53      |       -31.5       | SHORT    | Yahoo Finance |
| GDXJ       | 2026-10-12 00:00:00 |   112.92      |       -35.3333    | SHORT    | Yahoo Finance |
| GLD        | 2026-10-12 00:00:00 |   382.15      |       -54.5833    | SHORT    | Yahoo Finance |
| GS         | 2026-10-12 00:00:00 |   893.95      |       -39.5833    | SHORT    | Yahoo Finance |
| HBAR-USD   | 2026-10-13 00:00:00 |     0.08812   |       -36         | SHORT    | Kraken API    |
| HD         | 2026-10-12 00:00:00 |   290.62      |       -38.25      | SHORT    | Yahoo Finance |
| HON        | 2026-10-12 00:00:00 |   209.64      |       -31.9167    | SHORT    | Yahoo Finance |
| HYG        | 2026-10-12 00:00:00 |    77.29      |       -41.8333    | SHORT    | Yahoo Finance |
| IEF        | 2026-10-12 00:00:00 |    89.43      |       -37.3333    | SHORT    | Yahoo Finance |
| MCD        | 2026-10-12 00:00:00 |   235.65      |       -39.5833    | SHORT    | Yahoo Finance |
| MS         | 2026-10-12 00:00:00 |   190.02      |       -33.8333    | SHORT    | Yahoo Finance |
| NEM        | 2026-10-12 00:00:00 |   117.15      |       -34.8333    | SHORT    | Yahoo Finance |
| PEP        | 2026-10-12 00:00:00 |   126.68      |       -30.9167    | SHORT    | Yahoo Finance |
| SBUX       | 2026-10-12 00:00:00 |    92.29      |       -31.25      | SHORT    | Yahoo Finance |
| SHIB-USD   | 2026-10-13 00:00:00 |     5.262e-06 |       -42.5       | SHORT    | Kraken API    |
| SHY        | 2026-10-12 00:00:00 |    81.17      |       -32.6667    | SHORT    | Yahoo Finance |
| SLB        | 2026-10-12 00:00:00 |    48.77      |       -48.25      | SHORT    | Yahoo Finance |
| SLV        | 2026-10-12 00:00:00 |    54.35      |       -61.5833    | SHORT    | Yahoo Finance |
| T          | 2026-10-12 00:00:00 |    22.49      |       -57.4167    | SHORT    | Yahoo Finance |
| TLT        | 2026-10-12 00:00:00 |    78.05      |       -43.8333    | SHORT    | Yahoo Finance |
| TMUS       | 2026-10-12 00:00:00 |   151.87      |       -46.25      | SHORT    | Yahoo Finance |
| VEA        | 2026-10-12 00:00:00 |    69.95      |       -31.75      | SHORT    | Yahoo Finance |
| VZ         | 2026-10-12 00:00:00 |    42.78      |       -49.0833    | SHORT    | Yahoo Finance |
| WIF-USD    | 2026-10-13 00:00:00 |     0.2119    |       -46.5       | SHORT    | Kraken API    |
| XLB        | 2026-10-12 00:00:00 |    49.44      |       -30.9167    | SHORT    | Yahoo Finance |

## Edge Summary

- Symbols with trades: **161** of 161
- Beat buy-and-hold: **33.54%** of traded symbols
- Positive return: **29.19%** of traded symbols
- Median strategy return: **-10.23%** (benchmark **13.79%**)
- Median excess vs benchmark: **-26.46%**
- Median Sharpe: **-0.17**
- Median exposure: **44.26%**

> Edge is real only if both _beat buy-and-hold_ and _median excess_ are convincingly positive across many symbols. Treat a single high-return symbol as noise.

## Portfolio Backtest

Actual capital-allocation books (not per-symbol averages). Benchmarks: `equal_weight_buyhold` (whole tracked universe), `spy_buyhold` (100% SPY), and `sixty_forty` (60% SPY / 40% AGG). `high_conf_voltarget` inverse-vol-weights the HIGH-confidence book; `conviction_long_short` is market-neutral. Judge on **Sharpe** and **max_drawdown** out-of-sample, not raw return: a fully-invested long book wins on return in a bull market but carries all the risk.

| strategy              | scope         | ann_return   | ann_vol   |   sharpe | max_drawdown   | total_return   |   avg_gross_exposure |
|:----------------------|:--------------|:-------------|:----------|---------:|:---------------|:---------------|---------------------:|
| equal_weight_buyhold  | full          | 9.04%        | 28.56%    |     0.32 | -39.53%        | 16.33%         |                 1    |
| equal_weight_buyhold  | out_of_sample | 10.22%       | 28.29%    |     0.36 | -23.00%        | 6.88%          |                 1    |
| all_signals_ew        | full          | -17.66%      | 24.37%    |    -0.72 | -59.37%        | -46.67%        |                 1    |
| all_signals_ew        | out_of_sample | 11.43%       | 24.07%    |     0.47 | -23.20%        | 9.56%          |                 1    |
| high_conf_ew          | full          | -4.99%       | 31.64%    |    -0.16 | -46.26%        | -26.10%        |                 0.9  |
| high_conf_ew          | out_of_sample | 16.37%       | 29.06%    |     0.56 | -22.85%        | 13.76%         |                 0.9  |
| high_conf_voltarget   | full          | -6.48%       | 28.38%    |    -0.23 | -40.98%        | -27.23%        |                 0.9  |
| high_conf_voltarget   | out_of_sample | 3.21%        | 24.17%    |     0.13 | -17.08%        | 0.22%          |                 0.9  |
| conviction_long_short | full          | -13.91%      | 22.21%    |    -0.63 | -46.22%        | -39.32%        |                 0.97 |
| conviction_long_short | out_of_sample | 0.44%        | 19.61%    |     0.02 | -26.77%        | -1.57%         |                 0.97 |
| spy_buyhold           | full          | 4.62%        | 13.50%    |     0.34 | -19.00%        | 11.97%         |                 0.78 |
| spy_buyhold           | out_of_sample | 2.46%        | 9.92%     |     0.25 | -12.06%        | 2.13%          |                 0.78 |
| sixty_forty           | full          | 2.36%        | 8.53%     |     0.28 | -11.66%        | 6.26%          |                 0.78 |
| sixty_forty           | out_of_sample | -0.72%       | 6.68%     |    -0.11 | -8.26%         | -1.00%         |                 0.78 |

## Walk-Forward Robustness

Each book measured across contiguous time folds (each a different regime). A book has durable edge only if `mean_sharpe` is positive, `min_sharpe` isn't deeply negative, and `pct_positive_folds` is high — a single great fold doesn't count. `fold_sharpes` lists each fold oldest-to-newest.

| strategy              |   n_folds |   mean_sharpe |   median_sharpe |   min_sharpe | pct_positive_folds   | mean_return   | fold_sharpes                 |
|:----------------------|----------:|--------------:|----------------:|-------------:|:---------------------|:--------------|:-----------------------------|
| equal_weight_buyhold  |         5 |          0.45 |            0.8  |        -0.41 | 60.00%               | 3.61%         | 0.80;0.86;-0.09;-0.41;1.09   |
| all_signals_ew        |         5 |         -0.78 |           -1.38 |        -1.9  | 20.00%               | -9.83%        | -1.38;-1.51;-1.90;1.51;-0.61 |
| high_conf_ew          |         5 |         -0.07 |           -0.11 |        -0.9  | 40.00%               | -4.66%        | -0.11;-0.57;-0.90;1.15;0.10  |
| high_conf_voltarget   |         5 |         -0.13 |           -0.12 |        -0.81 | 40.00%               | -5.52%        | 0.02;-0.42;-0.81;0.67;-0.12  |
| conviction_long_short |         5 |         -0.6  |           -0.62 |        -1.78 | 20.00%               | -9.20%        | -1.78;-0.37;-0.63;-0.62;0.38 |
| spy_buyhold           |         5 |          0.36 |            0.07 |        -0.23 | 80.00%               | 2.41%         | 1.50;0.02;0.07;0.44;-0.23    |
| sixty_forty           |         5 |          0.26 |            0.12 |        -0.6  | 80.00%               | 1.27%         | 1.40;0.12;0.26;0.11;-0.60    |

## Strategy Comparison

Each decision rule backtested over the same data. `out_of_sample` is the most recent ~35% of each symbol's history (unseen tail). A rule has real edge only if `median_excess` and `beat_benchmark_pct` stay positive out-of-sample, not just full-sample.

| strategy        | scope         |   symbols | beat_benchmark_pct   | positive_pct   | median_return   | median_benchmark   | median_excess   |   median_sharpe |   total_trades |
|:----------------|:--------------|----------:|:---------------------|:---------------|:----------------|:-------------------|:----------------|----------------:|---------------:|
| trend           | full          |       161 | 33.54%               | 29.19%         | -10.23%         | 13.79%             | -26.46%         |           -0.17 |          11303 |
| trend           | out_of_sample |       161 | 27.95%               | 50.31%         | 0.06%           | 10.16%             | -16.09%         |            0.1  |           3804 |
| mean_reversion  | full          |       157 | 40.13%               | 50.32%         | 0.01%           | 12.65%             | -13.50%         |            0.02 |           1232 |
| mean_reversion  | out_of_sample |       121 | 26.45%               | 52.89%         | 0.29%           | 9.48%              | -10.37%         |            0.16 |            492 |
| regime_adaptive | full          |       161 | 34.78%               | 29.81%         | -11.22%         | 13.79%             | -26.30%         |           -0.13 |          11576 |
| regime_adaptive | out_of_sample |       161 | 28.57%               | 49.69%         | -0.10%          | 10.16%             | -16.54%         |            0.07 |           3917 |

## Signal Calibration

Realized forward return in the signal's direction, grouped by confidence. HIGH should outrank LOW for the confidence score to be meaningful.

| confidence_level   |   horizon |     n | mean_return   | median_return   | win_rate   |
|:-------------------|----------:|------:|:--------------|:----------------|:-----------|
| HIGH               |         5 |  7932 | 0.20%         | 0.04%           | 50.67%     |
| MEDIUM             |         5 | 29196 | 0.03%         | 0.02%           | 50.19%     |
| LOW                |         5 |  3504 | -0.42%        | -0.44%          | 45.78%     |
| ALL                |         5 | 40632 | 0.02%         | 0.00%           | 49.90%     |
| HIGH               |        10 |  7899 | 0.46%         | 0.09%           | 50.97%     |
| MEDIUM             |        10 | 28904 | 0.18%         | 0.06%           | 50.48%     |
| LOW                |        10 |  3442 | -0.71%        | -0.51%          | 46.66%     |
| ALL                |        10 | 40245 | 0.16%         | 0.03%           | 50.25%     |
| HIGH               |        20 |  7745 | 1.09%         | 0.32%           | 52.63%     |
| MEDIUM             |        20 | 28328 | 0.89%         | 0.56%           | 53.13%     |
| LOW                |        20 |  3385 | -0.46%        | -0.58%          | 47.21%     |
| ALL                |        20 | 39458 | 0.81%         | 0.44%           | 52.53%     |

## Backtest Summary

### Data Quality / Signal Availability

- **ok**: 161 symbols

| symbol     |   trades | return   | benchmark_return   | mdd     |   sharpe | exposure   | skipped_reason   |
|:-----------|---------:|:---------|:-------------------|:--------|---------:|:-----------|:-----------------|
| AAPL       |       63 | 6.89%    | 78.48%             | -20.65% |     0.24 | 51.08%     | ok               |
| AAVE-USD   |       65 | -36.26%  | -29.54%            | -66.17% |    -0.2  | 42.53%     | ok               |
| ABBV       |       72 | -23.44%  | 70.83%             | -30.52% |    -0.51 | 47.92%     | ok               |
| ADA-USD    |       76 | -37.91%  | -71.48%            | -52.70% |    -0.3  | 46.36%     | ok               |
| ADBE       |       71 | -8.14%   | -50.87%            | -31.20% |     0.03 | 56.74%     | ok               |
| AGG        |       67 | -6.98%   | -2.09%             | -11.29% |    -1.1  | 33.78%     | ok               |
| ALGO-USD   |       76 | -23.66%  | -52.22%            | -38.19% |    -0.09 | 40.23%     | ok               |
| AMAT       |       71 | -33.75%  | 126.20%            | -53.91% |    -0.29 | 51.58%     | ok               |
| AMD        |       52 | 26.72%   | 257.27%            | -40.05% |     0.45 | 36.94%     | ok               |
| AMGN       |       69 | -16.55%  | 32.76%             | -34.19% |    -0.3  | 50.25%     | ok               |
| AMZN       |       80 | -55.73%  | 41.40%             | -56.19% |    -1.6  | 41.26%     | ok               |
| APT-USD    |       70 | -23.20%  | -86.04%            | -56.73% |    -0    | 39.66%     | ok               |
| ARB-USD    |       77 | -15.63%  | -60.75%            | -48.19% |     0.14 | 43.49%     | ok               |
| ARKK       |       85 | -27.19%  | 93.03%             | -31.44% |    -0.39 | 43.43%     | ok               |
| ATOM-USD   |       92 | -60.19%  | -66.11%            | -60.19% |    -0.87 | 48.08%     | ok               |
| AVAX-USD   |       68 | -31.87%  | -59.07%            | -45.41% |    -0.24 | 40.04%     | ok               |
| AVGO       |       64 | 15.79%   | 150.86%            | -36.09% |     0.35 | 41.93%     | ok               |
| BA         |       71 | 1.97%    | 1.55%              | -26.78% |     0.16 | 51.25%     | ok               |
| BAC        |       72 | -11.08%  | 40.60%             | -25.80% |    -0.25 | 48.59%     | ok               |
| BCH-USD    |       76 | -2.27%   | -36.39%            | -53.87% |     0.19 | 48.85%     | ok               |
| BITO       |       79 | -25.27%  | -61.15%            | -43.10% |    -0.19 | 42.10%     | ok               |
| BLK        |       85 | -15.17%  | 34.62%             | -26.90% |    -0.37 | 47.42%     | ok               |
| BND        |       67 | -6.65%   | -2.08%             | -10.91% |    -1.01 | 35.77%     | ok               |
| BONK-USD   |       74 | 14.17%   | -86.09%            | -43.77% |     0.4  | 45.59%     | ok               |
| BTC-USD    |       72 | 1.74%    | -20.20%            | -23.38% |     0.17 | 52.49%     | ok               |
| C          |       77 | -34.23%  | 108.87%            | -39.51% |    -0.73 | 46.26%     | ok               |
| CAT        |       70 | 2.70%    | 120.36%            | -21.87% |     0.17 | 48.42%     | ok               |
| CL         |       64 | -5.36%   | -4.67%             | -14.32% |    -0.12 | 38.60%     | ok               |
| CMCSA      |       82 | -34.23%  | -43.72%            | -46.50% |    -0.81 | 42.93%     | ok               |
| COMP-USD   |       97 | -37.68%  | -51.02%            | -55.77% |    -0.21 | 49.81%     | ok               |
| COP        |       70 | -17.25%  | 13.79%             | -43.40% |    -0.24 | 43.93%     | ok               |
| COST       |       58 | -1.32%   | 20.99%             | -30.95% |     0.02 | 41.10%     | ok               |
| CRM        |       65 | -34.52%  | -18.51%            | -45.50% |    -0.51 | 45.92%     | ok               |
| CRV-USD    |       66 | 20.58%   | -55.20%            | -39.89% |     0.42 | 37.36%     | ok               |
| CSCO       |       64 | 17.23%   | 144.73%            | -21.79% |     0.4  | 49.08%     | ok               |
| CVX        |       71 | -13.64%  | 33.42%             | -27.78% |    -0.3  | 41.76%     | ok               |
| DASH-USD   |       55 | 0.17%    | 100.63%            | -64.43% |     0.39 | 30.46%     | ok               |
| DBC        |       66 | -8.16%   | 39.34%             | -24.10% |    -0.21 | 35.27%     | ok               |
| DE         |       70 | -12.17%  | 61.59%             | -23.98% |    -0.18 | 44.26%     | ok               |
| DIA        |       66 | -7.35%   | 30.10%             | -12.94% |    -0.38 | 43.59%     | ok               |
| DIS        |       60 | -6.18%   | 5.43%              | -28.17% |    -0.05 | 43.09%     | ok               |
| DOGE-USD   |       71 | -35.81%  | -66.14%            | -60.95% |    -0.22 | 48.66%     | ok               |
| DOT-USD    |       86 | -51.64%  | -77.14%            | -63.33% |    -0.43 | 48.47%     | ok               |
| DXY-INDEX  |       40 | -0.39%   | -4.03%             | -6.02%  |    -0.05 | 32.03%     | ok               |
| EEM        |       62 | -12.86%  | 51.62%             | -24.64% |    -0.37 | 40.27%     | ok               |
| EFA        |       64 | -11.38%  | 26.13%             | -12.96% |    -0.44 | 41.43%     | ok               |
| EOG        |       78 | -30.38%  | 15.90%             | -47.87% |    -0.66 | 44.76%     | ok               |
| ETC-USD    |       58 | -25.24%  | -60.15%            | -46.55% |    -0.25 | 30.84%     | ok               |
| ETH-USD    |       58 | 138.28%  | -2.08%             | -30.11% |     1.27 | 48.47%     | ok               |
| EWJ        |       62 | -22.99%  | 40.60%             | -29.40% |    -0.8  | 36.44%     | ok               |
| FCX        |       65 | -29.37%  | 33.59%             | -46.84% |    -0.32 | 44.26%     | ok               |
| FET-USD    |       81 | -50.27%  | -75.77%            | -65.38% |    -0.35 | 42.53%     | ok               |
| FIL-USD    |       65 | -40.15%  | -63.95%            | -58.54% |    -0.34 | 37.16%     | ok               |
| FXI        |       50 | -9.80%   | 17.68%             | -24.33% |    -0.17 | 31.45%     | ok               |
| GDX        |       60 | -3.83%   | 137.73%            | -33.31% |     0.07 | 44.43%     | ok               |
| GDXJ       |       70 | -39.44%  | 140.56%            | -41.57% |    -0.54 | 42.93%     | ok               |
| GE         |       76 | -8.43%   | 93.77%             | -27.82% |    -0.04 | 48.09%     | ok               |
| GLD        |       50 | 8.96%    | 70.18%             | -13.87% |     0.29 | 45.76%     | ok               |
| GOOGL      |       55 | 57.04%   | 99.37%             | -17.15% |     1.01 | 47.25%     | ok               |
| GRT-USD    |       79 | 57.11%   | -78.86%            | -33.74% |     0.69 | 45.79%     | ok               |
| GS         |       70 | -4.56%   | 93.10%             | -22.13% |     0    | 48.09%     | ok               |
| HBAR-USD   |       40 | -44.98%  | -14.55%            | -57.09% |    -1.01 | 37.40%     | ok               |
| HD         |       67 | 2.92%    | -13.97%            | -17.15% |     0.16 | 43.43%     | ok               |
| HON        |       91 | -27.96%  | 3.65%              | -33.53% |    -0.71 | 54.91%     | ok               |
| HYG        |       87 | -7.48%   | -0.04%             | -10.59% |    -0.84 | 38.44%     | ok               |
| IBIT       |       38 | 38.42%   | 23.28%             | -18.95% |     0.7  | 34.83%     | ok               |
| IBM        |       69 | -24.70%  | 33.60%             | -48.94% |    -0.29 | 49.58%     | ok               |
| ICP-USD    |       79 | -17.84%  | -45.44%            | -46.42% |     0.09 | 39.27%     | ok               |
| IEF        |       78 | -10.23%  | -3.81%             | -13.34% |    -1.39 | 34.28%     | ok               |
| IEMG       |       60 | -12.49%  | 47.22%             | -27.97% |    -0.38 | 40.43%     | ok               |
| INJ-USD    |       63 | -23.18%  | -40.82%            | -69.36% |     0.02 | 40.23%     | ok               |
| INTC       |       68 | 40.26%   | 215.73%            | -60.60% |     0.53 | 48.09%     | ok               |
| INTU       |       73 | -17.96%  | -54.34%            | -41.31% |    -0.18 | 46.26%     | ok               |
| ITA        |       76 | -3.75%   | 51.07%             | -23.75% |    -0.03 | 48.75%     | ok               |
| IWM        |       54 | 6.80%    | 33.26%             | -12.19% |     0.3  | 34.44%     | ok               |
| JNJ        |       62 | 6.91%    | 74.34%             | -16.86% |     0.3  | 46.59%     | ok               |
| JPM        |       73 | -21.30%  | 70.93%             | -32.74% |    -0.58 | 45.26%     | ok               |
| KO         |       54 | 24.07%   | 43.50%             | -8.64%  |     0.85 | 37.10%     | ok               |
| LDO-USD    |       70 | 44.87%   | -64.21%            | -50.47% |     0.6  | 46.55%     | ok               |
| LIN        |       74 | -11.87%  | 12.65%             | -20.61% |    -0.38 | 38.27%     | ok               |
| LINK-USD   |       68 | 41.83%   | -24.36%            | -33.64% |     0.6  | 45.79%     | ok               |
| LLY        |       78 | -35.04%  | 51.00%             | -53.34% |    -0.58 | 49.08%     | ok               |
| LRCX       |       80 | -27.48%  | 228.61%            | -58.92% |    -0.19 | 42.76%     | ok               |
| LTC-USD    |       68 | -3.81%   | -40.95%            | -33.04% |     0.15 | 53.26%     | ok               |
| MCD        |       79 | -0.23%   | -12.03%            | -21.88% |     0.05 | 40.93%     | ok               |
| META       |       74 | -24.88%  | 58.47%             | -44.52% |    -0.33 | 49.92%     | ok               |
| MPC        |       71 | 15.43%   | 160.57%            | -37.91% |     0.36 | 52.08%     | ok               |
| MRK        |       67 | -23.98%  | 11.04%             | -35.95% |    -0.46 | 42.60%     | ok               |
| MS         |       75 | -10.16%  | 89.39%             | -27.79% |    -0.17 | 48.25%     | ok               |
| MSFT       |       85 | -24.95%  | 27.23%             | -39.07% |    -0.53 | 51.08%     | ok               |
| MU         |       51 | 137.47%  | 666.70%            | -68.76% |     0.99 | 52.91%     | ok               |
| NEAR-USD   |       73 | 153.48%  | 58.51%             | -47.03% |     1.05 | 44.25%     | ok               |
| NEM        |       68 | -29.63%  | 163.61%            | -39.56% |    -0.32 | 50.08%     | ok               |
| NFLX       |       78 | 4.89%    | 10.19%             | -21.09% |     0.2  | 53.24%     | ok               |
| NKE        |       79 | -26.43%  | -61.48%            | -55.35% |    -0.28 | 46.92%     | ok               |
| NOW        |       80 | 9.63%    | -9.38%             | -30.43% |     0.29 | 50.08%     | ok               |
| NVDA       |       77 | -48.99%  | 86.90%             | -52.37% |    -0.69 | 55.26%     | ok               |
| OP-USD     |       68 | -34.19%  | -84.83%            | -58.87% |    -0.22 | 32.95%     | ok               |
| ORCL       |       62 | 85.66%   | 10.34%             | -30.61% |     0.8  | 52.41%     | ok               |
| OXY        |       73 | 2.12%    | -3.84%             | -28.48% |     0.16 | 42.43%     | ok               |
| PEP        |       76 | -0.60%   | -29.74%            | -21.35% |     0.05 | 45.92%     | ok               |
| PEPE-USD   |       83 | -54.13%  | -69.84%            | -61.29% |    -0.4  | 48.66%     | ok               |
| PFE        |       81 | -33.76%  | -0.46%             | -41.77% |    -1.03 | 37.10%     | ok               |
| PG         |       64 | -24.07%  | -8.43%             | -24.55% |    -0.98 | 34.61%     | ok               |
| PM         |       79 | -7.15%   | 102.83%            | -35.15% |    -0.07 | 50.42%     | ok               |
| POL-USD    |       79 | 51.05%   | -61.77%            | -38.69% |     0.67 | 49.62%     | ok               |
| QCOM       |       77 | -28.48%  | -11.80%            | -57.69% |    -0.24 | 43.59%     | ok               |
| QQQ        |       66 | 8.80%    | 64.00%             | -14.20% |     0.31 | 46.09%     | ok               |
| RENDER-USD |       90 | -12.44%  | -60.14%            | -44.65% |     0.15 | 47.13%     | ok               |
| RTX        |       64 | 31.00%   | 77.74%             | -16.99% |     0.71 | 52.25%     | ok               |
| SBUX       |       62 | -10.18%  | 19.02%             | -29.22% |    -0.13 | 38.27%     | ok               |
| SCHW       |       80 | -20.05%  | 23.39%             | -31.92% |    -0.45 | 46.26%     | ok               |
| SHIB-USD   |       81 | -39.03%  | -69.19%            | -47.54% |    -0.4  | 52.11%     | ok               |
| SHY        |       46 | -1.78%   | -0.28%             | -3.30%  |    -0.6  | 36.77%     | ok               |
| SKY-USD    |       85 | -62.09%  | -2.50%             | -61.82% |    -1.01 | 44.64%     | ok               |
| SLB        |       73 | -37.59%  | 1.12%              | -57.55% |    -0.7  | 48.92%     | ok               |
| SLV        |       66 | 4.23%    | 87.54%             | -42.66% |     0.23 | 40.10%     | ok               |
| SMH        |       48 | 47.95%   | 151.49%            | -34.29% |     0.78 | 44.26%     | ok               |
| SNX-USD    |       62 | -9.86%   | -73.18%            | -50.74% |     0.1  | 33.52%     | ok               |
| SOL-USD    |       69 | -18.69%  | -39.01%            | -44.99% |     0.01 | 60.34%     | ok               |
| SOXX       |       54 | 59.74%   | 133.58%            | -39.81% |     0.86 | 43.26%     | ok               |
| SPY        |       64 | -0.17%   | 46.79%             | -15.53% |     0.05 | 49.75%     | ok               |
| SUSHI-USD  |       96 | -77.26%  | -72.72%            | -76.07% |    -1.26 | 39.46%     | ok               |
| T          |       72 | 47.48%   | 28.37%             | -17.01% |     0.91 | 56.74%     | ok               |
| TGT        |       62 | -11.80%  | -1.97%             | -34.98% |    -0.18 | 37.77%     | ok               |
| TIA-USD    |       93 | -50.65%  | -81.31%            | -78.90% |    -0.28 | 42.72%     | ok               |
| TLT        |       68 | -18.75%  | -14.34%            | -21.85% |    -1.4  | 33.78%     | ok               |
| TMO        |       69 | 22.50%   | 11.49%             | -18.85% |     0.5  | 55.24%     | ok               |
| TMUS       |       76 | 0.08%    | -7.34%             | -29.75% |     0.1  | 47.75%     | ok               |
| TRX-USD    |       66 | 3.59%    | 23.98%             | -22.90% |     0.19 | 51.15%     | ok               |
| TSLA       |       80 | -37.10%  | 116.08%            | -59.64% |    -0.26 | 42.93%     | ok               |
| TXN        |       77 | -25.62%  | 41.44%             | -47.39% |    -0.28 | 50.42%     | ok               |
| UNH        |       77 | 23.15%   | -26.82%            | -26.31% |     0.45 | 48.42%     | ok               |
| UNI-USD    |       90 | -40.02%  | -1.81%             | -72.03% |    -0.16 | 50.19%     | ok               |
| UPS        |       70 | -35.32%  | -35.40%            | -39.58% |    -0.69 | 42.60%     | ok               |
| USO        |       67 | -12.16%  | 96.83%             | -46.69% |    -0.05 | 33.44%     | ok               |
| VEA        |       60 | -4.61%   | 36.83%             | -17.61% |    -0.14 | 42.60%     | ok               |
| VIXY       |       94 | -78.34%  | -64.70%            | -88.17% |    -0.95 | 32.61%     | ok               |
| VNQ        |       73 | -15.26%  | 8.26%              | -24.92% |    -0.61 | 40.10%     | ok               |
| VTI        |       68 | -7.64%   | 45.32%             | -17.64% |    -0.22 | 49.75%     | ok               |
| VWO        |       80 | -18.81%  | 33.36%             | -24.94% |    -0.71 | 40.93%     | ok               |
| VZ         |       84 | -22.29%  | 6.63%              | -26.12% |    -0.67 | 41.43%     | ok               |
| WFC        |       80 | -17.91%  | 37.27%             | -28.90% |    -0.29 | 47.59%     | ok               |
| WIF-USD    |       68 | -32.76%  | -77.53%            | -52.76% |    -0.09 | 37.36%     | ok               |
| WMT        |       69 | 4.37%    | 76.19%             | -25.37% |     0.19 | 49.08%     | ok               |
| XBI        |       64 | -4.11%   | 64.08%             | -18.01% |    -0.02 | 39.27%     | ok               |
| XLB        |       64 | -14.11%  | 7.15%              | -25.04% |    -0.51 | 31.95%     | ok               |
| XLC        |       61 | 12.62%   | 34.52%             | -12.33% |     0.47 | 50.25%     | ok               |
| XLE        |       69 | -5.32%   | 39.94%             | -30.31% |    -0.05 | 44.93%     | ok               |
| XLF        |       80 | -8.91%   | 31.35%             | -23.61% |    -0.27 | 46.59%     | ok               |
| XLI        |       82 | -10.04%  | 34.71%             | -17.79% |    -0.35 | 42.76%     | ok               |
| XLK        |       42 | 54.09%   | 83.25%             | -14.75% |     1.05 | 46.42%     | ok               |
| XLM-USD    |       68 | -13.32%  | -39.26%            | -55.76% |     0.06 | 47.51%     | ok               |
| XLP        |       67 | 3.85%    | 8.68%              | -10.28% |     0.25 | 38.44%     | ok               |
| XLU        |       69 | -6.15%   | 15.29%             | -20.40% |    -0.22 | 39.93%     | ok               |
| XLV        |       76 | -22.24%  | 17.80%             | -22.75% |    -1.07 | 37.10%     | ok               |
| XLY        |       75 | -4.15%   | 26.59%             | -18.35% |    -0.06 | 47.59%     | ok               |
| XOM        |       55 | 1.71%    | 45.07%             | -20.29% |     0.12 | 34.28%     | ok               |
| XRP-USD    |       64 | 1.26%    | -44.34%            | -33.91% |     0.21 | 36.59%     | ok               |
| YFI-USD    |       77 | -65.43%  | -64.14%            | -64.55% |    -1.29 | 37.55%     | ok               |
| ZEC-USD    |       57 | 142.10%  | 2691.56%           | -56.50% |     0.9  | 41.76%     | ok               |

## AAPL Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 13.58%   | 78.48%             | -21.71% |     0.35 |       72 | 55.91%     | ok               |
|          15 | 10.66%   | 78.48%             | -23.86% |     0.3  |       81 | 63.23%     | ok               |
|          30 | 6.89%    | 78.48%             | -20.65% |     0.24 |       63 | 51.08%     | ok               |
|          35 | 5.36%    | 78.48%             | -22.04% |     0.21 |       63 | 49.75%     | ok               |
|          25 | 2.57%    | 78.48%             | -20.87% |     0.16 |       73 | 53.24%     | ok               |

## AAVE-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 25.05%   | -29.54%            | -43.61% |     0.46 |       43 | 36.97%     | ok               |
|          45 | 13.40%   | -29.54%            | -49.19% |     0.35 |       48 | 31.80%     | ok               |
|          35 | 9.08%    | -29.54%            | -48.79% |     0.32 |       51 | 40.04%     | ok               |
|          50 | 8.31%    | -29.54%            | -45.07% |     0.29 |       46 | 24.14%     | ok               |
|          15 | -37.63%  | -29.54%            | -61.76% |    -0.14 |       72 | 55.36%     | ok               |

## ABBV Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -13.05%  | 70.83%             | -27.91% |    -0.27 |       56 | 35.11%     | ok               |
|          25 | -22.15%  | 70.83%             | -30.04% |    -0.46 |       71 | 49.92%     | ok               |
|          20 | -22.61%  | 70.83%             | -28.73% |    -0.47 |       69 | 51.58%     | ok               |
|          40 | -21.31%  | 70.83%             | -27.36% |    -0.5  |       72 | 40.27%     | ok               |
|          30 | -23.44%  | 70.83%             | -30.52% |    -0.51 |       72 | 47.92%     | ok               |

## ADA-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 9.79%    | -71.48%            | -34.64% |     0.31 |       46 | 31.99%     | ok               |
|          50 | 3.51%    | -71.48%            | -35.54% |     0.23 |       48 | 27.59%     | ok               |
|          40 | -8.93%   | -71.48%            | -40.73% |     0.1  |       58 | 37.93%     | ok               |
|          15 | -25.55%  | -71.48%            | -47.27% |     0.01 |       71 | 62.26%     | ok               |
|          35 | -20.00%  | -71.48%            | -44.07% |    -0.03 |       64 | 41.76%     | ok               |

## ADBE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | 8.27%    | -50.87%            | -29.07% |     0.26 |       55 | 61.06%     | ok               |
|          35 | -1.80%   | -50.87%            | -31.73% |     0.1  |       79 | 48.25%     | ok               |
|          20 | -5.91%   | -50.87%            | -31.52% |     0.07 |       61 | 64.06%     | ok               |
|          30 | -8.14%   | -50.87%            | -31.20% |     0.03 |       71 | 56.74%     | ok               |
|          15 | -16.48%  | -50.87%            | -34.98% |    -0.08 |       62 | 65.89%     | ok               |

## AGG Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -5.80%   | -2.09%             | -9.79%  |    -1.04 |       60 | 25.46%     | ok               |
|          30 | -6.98%   | -2.09%             | -11.29% |    -1.1  |       67 | 33.78%     | ok               |
|          50 | -5.30%   | -2.09%             | -8.35%  |    -1.11 |       58 | 20.30%     | ok               |
|          20 | -8.10%   | -2.09%             | -11.89% |    -1.16 |       72 | 38.60%     | ok               |
|          25 | -8.02%   | -2.09%             | -12.28% |    -1.2  |       71 | 36.77%     | ok               |

## ALGO-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -23.66%  | -52.22%            | -38.19% |    -0.09 |       76 | 40.23%     | ok               |
|          25 | -33.43%  | -52.22%            | -51.92% |    -0.21 |       78 | 45.02%     | ok               |
|          15 | -37.08%  | -52.22%            | -51.37% |    -0.24 |       77 | 50.38%     | ok               |
|          35 | -37.01%  | -52.22%            | -50.16% |    -0.38 |       64 | 35.06%     | ok               |
|          20 | -45.30%  | -52.22%            | -53.23% |    -0.4  |       81 | 47.70%     | ok               |

## AMAT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -31.79%  | 126.20%            | -53.90% |    -0.22 |       72 | 60.57%     | ok               |
|          50 | -25.90%  | 126.20%            | -41.04% |    -0.22 |       50 | 36.27%     | ok               |
|          35 | -28.83%  | 126.20%            | -47.88% |    -0.23 |       71 | 48.92%     | ok               |
|          30 | -33.75%  | 126.20%            | -53.91% |    -0.29 |       71 | 51.58%     | ok               |
|          40 | -34.63%  | 126.20%            | -50.74% |    -0.34 |       69 | 44.09%     | ok               |

## AMD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 27.66%   | 257.27%            | -40.05% |     0.46 |       58 | 32.11%     | ok               |
|          40 | 26.72%   | 257.27%            | -40.05% |     0.45 |       52 | 36.94%     | ok               |
|          35 | 21.31%   | 257.27%            | -42.14% |     0.41 |       60 | 38.60%     | ok               |
|          30 | 9.22%    | 257.27%            | -47.00% |     0.31 |       65 | 41.10%     | ok               |
|          25 | 4.46%    | 257.27%            | -51.79% |     0.27 |       61 | 43.26%     | ok               |

## AMGN Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -11.77%  | 32.76%             | -26.65% |    -0.16 |       64 | 56.07%     | ok               |
|          35 | -14.38%  | 32.76%             | -31.29% |    -0.25 |       69 | 46.76%     | ok               |
|          30 | -16.55%  | 32.76%             | -34.19% |    -0.3  |       69 | 50.25%     | ok               |
|          15 | -18.94%  | 32.76%             | -27.98% |    -0.32 |       63 | 60.40%     | ok               |
|          25 | -18.39%  | 32.76%             | -33.47% |    -0.34 |       63 | 52.58%     | ok               |

## AMZN Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -27.97%  | 41.40%             | -29.61% |    -0.85 |       56 | 29.95%     | ok               |
|          50 | -31.74%  | 41.40%             | -33.91% |    -1.16 |       50 | 22.80%     | ok               |
|          45 | -37.46%  | 41.40%             | -38.25% |    -1.34 |       58 | 26.46%     | ok               |
|          35 | -52.04%  | 41.40%             | -52.54% |    -1.53 |       77 | 35.27%     | ok               |
|          30 | -55.73%  | 41.40%             | -56.19% |    -1.6  |       80 | 41.26%     | ok               |

## APT-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 25.37%   | -86.04%            | -31.21% |     0.52 |       42 | 16.28%     | ok               |
|          20 | 2.78%    | -86.04%            | -56.22% |     0.31 |       76 | 49.43%     | ok               |
|          45 | -1.29%   | -86.04%            | -53.47% |     0.18 |       58 | 23.18%     | ok               |
|          35 | -14.40%  | -86.04%            | -49.10% |     0.07 |       68 | 35.44%     | ok               |
|          25 | -22.50%  | -86.04%            | -55.69% |     0.03 |       70 | 44.25%     | ok               |

## ARB-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 57.32%   | -60.75%            | -33.60% |     0.67 |       54 | 26.44%     | ok               |
|          50 | 46.51%   | -60.75%            | -30.72% |     0.61 |       42 | 19.35%     | ok               |
|          15 | 25.04%   | -60.75%            | -44.26% |     0.48 |       86 | 59.39%     | ok               |
|          40 | 27.44%   | -60.75%            | -40.13% |     0.48 |       55 | 33.72%     | ok               |
|          35 | 21.94%   | -60.75%            | -45.71% |     0.44 |       71 | 37.93%     | ok               |

## ARKK Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -13.51%  | 93.03%             | -37.76% |    -0.06 |       89 | 54.74%     | ok               |
|          20 | -21.49%  | 93.03%             | -34.82% |    -0.22 |       87 | 49.92%     | ok               |
|          30 | -27.19%  | 93.03%             | -31.44% |    -0.39 |       85 | 43.43%     | ok               |
|          35 | -32.93%  | 93.03%             | -36.46% |    -0.55 |       86 | 40.77%     | ok               |
|          40 | -34.01%  | 93.03%             | -40.75% |    -0.61 |       78 | 36.61%     | ok               |

## ATOM-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -41.59%  | -66.11%            | -48.20% |    -0.33 |       86 | 65.90%     | ok               |
|          25 | -50.75%  | -66.11%            | -51.81% |    -0.57 |       94 | 54.41%     | ok               |
|          20 | -55.70%  | -66.11%            | -57.28% |    -0.66 |       96 | 58.24%     | ok               |
|          30 | -60.19%  | -66.11%            | -60.19% |    -0.87 |       92 | 48.08%     | ok               |
|          35 | -61.25%  | -66.11%            | -63.38% |    -1    |       82 | 41.95%     | ok               |

## AVAX-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 53.25%   | -59.07%            | -22.06% |     0.83 |       32 | 19.73%     | ok               |
|          40 | 19.68%   | -59.07%            | -26.61% |     0.43 |       38 | 27.39%     | ok               |
|          45 | 16.86%   | -59.07%            | -23.19% |     0.39 |       30 | 24.14%     | ok               |
|          35 | 1.03%    | -59.07%            | -33.36% |     0.2  |       56 | 33.72%     | ok               |
|          15 | -13.05%  | -59.07%            | -43.71% |     0.09 |       73 | 53.26%     | ok               |

## AVGO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | 19.12%   | 150.86%            | -38.01% |     0.38 |       68 | 44.59%     | ok               |
|          30 | 15.79%   | 150.86%            | -36.09% |     0.35 |       64 | 41.93%     | ok               |
|          50 | 10.84%   | 150.86%            | -36.86% |     0.29 |       56 | 29.78%     | ok               |
|          35 | 7.38%    | 150.86%            | -40.43% |     0.26 |       74 | 38.94%     | ok               |
|          20 | 5.45%    | 150.86%            | -39.42% |     0.24 |       77 | 47.75%     | ok               |

## BA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 39.55%   | 1.55%              | -13.34% |     0.87 |       46 | 35.44%     | ok               |
|          40 | 32.92%   | 1.55%              | -23.87% |     0.65 |       46 | 43.09%     | ok               |
|          35 | 27.22%   | 1.55%              | -19.93% |     0.54 |       68 | 47.59%     | ok               |
|          25 | 11.43%   | 1.55%              | -27.24% |     0.31 |       72 | 54.74%     | ok               |
|          45 | 5.66%    | 1.55%              | -26.76% |     0.22 |       44 | 39.43%     | ok               |

## BAC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | -0.90%   | 40.60%             | -23.08% |     0.05 |       64 | 45.26%     | ok               |
|          20 | -3.03%   | 40.60%             | -18.20% |     0.01 |       80 | 53.41%     | ok               |
|          25 | -5.40%   | 40.60%             | -22.11% |    -0.07 |       74 | 50.92%     | ok               |
|          45 | -6.80%   | 40.60%             | -19.47% |    -0.15 |       60 | 36.94%     | ok               |
|          15 | -10.82%  | 40.60%             | -23.94% |    -0.18 |       87 | 60.57%     | ok               |

## BCH-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 36.57%   | -36.39%            | -45.51% |     0.55 |       74 | 57.47%     | ok               |
|          20 | 13.21%   | -36.39%            | -45.82% |     0.35 |       68 | 54.21%     | ok               |
|          25 | -2.46%   | -36.39%            | -51.09% |     0.19 |       70 | 50.38%     | ok               |
|          30 | -2.27%   | -36.39%            | -53.87% |     0.19 |       76 | 48.85%     | ok               |
|          35 | -10.20%  | -36.39%            | -57.75% |     0.09 |       70 | 45.21%     | ok               |

## BITO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -9.58%   | -61.15%            | -31.98% |    -0.01 |       54 | 25.62%     | ok               |
|          30 | -25.27%  | -61.15%            | -43.10% |    -0.19 |       79 | 42.10%     | ok               |
|          45 | -22.04%  | -61.15%            | -34.45% |    -0.21 |       60 | 29.12%     | ok               |
|          40 | -26.08%  | -61.15%            | -40.13% |    -0.25 |       62 | 33.44%     | ok               |
|          35 | -28.03%  | -61.15%            | -42.34% |    -0.26 |       70 | 37.60%     | ok               |

## BLK Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | -6.59%   | 34.62%             | -20.79% |    -0.12 |       92 | 43.59%     | ok               |
|          40 | -7.84%   | 34.62%             | -22.83% |    -0.18 |       80 | 38.77%     | ok               |
|          20 | -9.75%   | 34.62%             | -21.48% |    -0.18 |       88 | 52.08%     | ok               |
|          25 | -11.05%  | 34.62%             | -24.62% |    -0.23 |       81 | 49.92%     | ok               |
|          30 | -15.17%  | 34.62%             | -26.90% |    -0.37 |       85 | 47.42%     | ok               |

## BND Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -6.27%   | -2.08%             | -10.21% |    -0.88 |       66 | 40.77%     | ok               |
|          25 | -6.92%   | -2.08%             | -11.27% |    -1.01 |       69 | 38.77%     | ok               |
|          30 | -6.65%   | -2.08%             | -10.91% |    -1.01 |       67 | 35.77%     | ok               |
|          15 | -7.98%   | -2.08%             | -11.52% |    -1.11 |       77 | 43.43%     | ok               |
|          40 | -7.60%   | -2.08%             | -11.70% |    -1.28 |       62 | 29.95%     | ok               |

## BONK-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 156.03%  | -86.09%            | -35.57% |     1.2  |       42 | 21.46%     | ok               |
|          45 | 54.83%   | -86.09%            | -42.36% |     0.67 |       66 | 27.59%     | ok               |
|          15 | 57.53%   | -86.09%            | -62.48% |     0.66 |       71 | 59.96%     | ok               |
|          20 | 34.82%   | -86.09%            | -54.25% |     0.54 |       68 | 55.75%     | ok               |
|          40 | 29.64%   | -86.09%            | -48.74% |     0.5  |       56 | 36.97%     | ok               |

## BTC-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 41.90%   | -20.20%            | -14.50% |     0.85 |       44 | 35.63%     | ok               |
|          45 | 37.46%   | -20.20%            | -12.20% |     0.8  |       42 | 31.61%     | ok               |
|          35 | 40.91%   | -20.20%            | -21.56% |     0.8  |       62 | 41.95%     | ok               |
|          50 | 18.02%   | -20.20%            | -20.63% |     0.49 |       38 | 26.44%     | ok               |
|          30 | 16.48%   | -20.20%            | -21.75% |     0.41 |       68 | 47.89%     | ok               |

## C Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -10.92%  | 108.87%            | -21.80% |    -0.24 |       66 | 31.45%     | ok               |
|          45 | -21.56%  | 108.87%            | -29.60% |    -0.54 |       74 | 35.61%     | ok               |
|          40 | -27.06%  | 108.87%            | -35.11% |    -0.67 |       74 | 37.94%     | ok               |
|          25 | -32.92%  | 108.87%            | -36.47% |    -0.68 |       69 | 48.42%     | ok               |
|          30 | -34.23%  | 108.87%            | -39.51% |    -0.73 |       77 | 46.26%     | ok               |

## CAT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 12.67%   | 120.36%            | -22.02% |     0.32 |       73 | 61.06%     | ok               |
|          25 | 10.00%   | 120.36%            | -21.79% |     0.28 |       66 | 50.75%     | ok               |
|          45 | 3.44%    | 120.36%            | -23.66% |     0.18 |       54 | 37.10%     | ok               |
|          30 | 2.70%    | 120.36%            | -21.87% |     0.17 |       70 | 48.42%     | ok               |
|          20 | 0.79%    | 120.36%            | -24.78% |     0.14 |       76 | 54.24%     | ok               |

## CL Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -1.72%   | -4.67%             | -12.98% |    -0.02 |       42 | 22.46%     | ok               |
|          30 | -5.36%   | -4.67%             | -14.32% |    -0.12 |       64 | 38.60%     | ok               |
|          45 | -7.42%   | -4.67%             | -13.51% |    -0.26 |       48 | 25.29%     | ok               |
|          35 | -9.14%   | -4.67%             | -15.34% |    -0.27 |       64 | 34.78%     | ok               |
|          15 | -13.85%  | -4.67%             | -18.95% |    -0.36 |       64 | 46.92%     | ok               |

## CMCSA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -19.16%  | -43.72%            | -29.66% |    -0.63 |       50 | 16.47%     | ok               |
|          15 | -34.41%  | -43.72%            | -47.11% |    -0.7  |       89 | 57.57%     | ok               |
|          45 | -23.74%  | -43.72%            | -36.26% |    -0.75 |       64 | 20.97%     | ok               |
|          30 | -34.23%  | -43.72%            | -46.50% |    -0.81 |       82 | 42.93%     | ok               |
|          40 | -31.54%  | -43.72%            | -43.51% |    -0.85 |       91 | 28.45%     | ok               |

## COMP-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -1.20%   | -51.02%            | -38.71% |     0.19 |       50 | 24.90%     | ok               |
|          30 | -37.68%  | -51.02%            | -55.77% |    -0.21 |       97 | 49.81%     | ok               |
|          25 | -43.96%  | -51.02%            | -54.62% |    -0.28 |       96 | 57.85%     | ok               |
|          15 | -46.25%  | -51.02%            | -54.29% |    -0.29 |       98 | 68.39%     | ok               |
|          40 | -43.87%  | -51.02%            | -52.04% |    -0.39 |       70 | 38.51%     | ok               |

## COP Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -5.69%   | 13.79%             | -35.08% |    -0.03 |       48 | 28.12%     | ok               |
|          35 | -15.81%  | 13.79%             | -44.33% |    -0.22 |       73 | 40.93%     | ok               |
|          45 | -14.68%  | 13.79%             | -40.25% |    -0.24 |       62 | 32.28%     | ok               |
|          30 | -17.25%  | 13.79%             | -43.40% |    -0.24 |       70 | 43.93%     | ok               |
|          40 | -23.81%  | 13.79%             | -47.85% |    -0.45 |       76 | 36.11%     | ok               |

## COST Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 13.03%   | 20.99%             | -24.32% |     0.44 |       62 | 47.25%     | ok               |
|          25 | 9.32%    | 20.99%             | -24.93% |     0.34 |       59 | 44.26%     | ok               |
|          35 | 3.04%    | 20.99%             | -29.78% |     0.16 |       56 | 38.60%     | ok               |
|          30 | -1.32%   | 20.99%             | -30.95% |     0.02 |       58 | 41.10%     | ok               |
|          15 | -2.29%   | 20.99%             | -27.30% |     0.01 |       67 | 50.92%     | ok               |

## CRM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | -22.78%  | -18.51%            | -34.06% |    -0.28 |       62 | 41.26%     | ok               |
|          40 | -25.67%  | -18.51%            | -39.44% |    -0.37 |       68 | 37.10%     | ok               |
|          15 | -33.25%  | -18.51%            | -47.54% |    -0.4  |       88 | 57.24%     | ok               |
|          50 | -22.09%  | -18.51%            | -38.38% |    -0.4  |       58 | 24.63%     | ok               |
|          30 | -34.52%  | -18.51%            | -45.50% |    -0.51 |       65 | 45.92%     | ok               |

## CRV-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 50.03%   | -55.20%            | -37.78% |     0.64 |       66 | 32.76%     | ok               |
|          40 | 36.66%   | -55.20%            | -38.86% |     0.55 |       54 | 28.54%     | ok               |
|          45 | 27.74%   | -55.20%            | -42.29% |     0.48 |       54 | 22.03%     | ok               |
|          50 | 26.86%   | -55.20%            | -30.73% |     0.48 |       46 | 18.01%     | ok               |
|          30 | 20.58%   | -55.20%            | -39.89% |     0.42 |       66 | 37.36%     | ok               |

## CSCO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 33.10%   | 144.73%            | -19.34% |     0.69 |       50 | 37.94%     | ok               |
|          45 | 28.60%   | 144.73%            | -19.34% |     0.61 |       52 | 39.60%     | ok               |
|          25 | 23.74%   | 144.73%            | -23.28% |     0.5  |       61 | 50.42%     | ok               |
|          20 | 18.19%   | 144.73%            | -22.72% |     0.42 |       71 | 52.75%     | ok               |
|          30 | 17.23%   | 144.73%            | -21.79% |     0.4  |       64 | 49.08%     | ok               |

## CVX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -9.60%   | 33.42%             | -23.80% |    -0.17 |       73 | 44.59%     | ok               |
|          40 | -10.08%  | 33.42%             | -27.34% |    -0.22 |       73 | 36.61%     | ok               |
|          45 | -10.48%  | 33.42%             | -28.83% |    -0.24 |       65 | 33.28%     | ok               |
|          50 | -10.36%  | 33.42%             | -30.69% |    -0.29 |       58 | 28.79%     | ok               |
|          35 | -13.01%  | 33.42%             | -28.85% |    -0.29 |       67 | 38.60%     | ok               |

## DASH-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 156.61%  | 100.63%            | -33.55% |     1.01 |       38 | 18.01%     | ok               |
|          40 | 125.75%  | 100.63%            | -33.20% |     0.89 |       42 | 24.33%     | ok               |
|          45 | 94.16%   | 100.63%            | -37.63% |     0.78 |       42 | 20.50%     | ok               |
|          30 | 0.17%    | 100.63%            | -64.43% |     0.39 |       55 | 30.46%     | ok               |
|          25 | -6.68%   | 100.63%            | -64.14% |     0.34 |       65 | 32.95%     | ok               |

## DBC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -0.09%   | 39.34%             | -26.05% |     0.07 |       77 | 41.26%     | ok               |
|          20 | -4.49%   | 39.34%             | -25.69% |    -0.08 |       69 | 39.60%     | ok               |
|          25 | -5.28%   | 39.34%             | -24.84% |    -0.11 |       66 | 37.60%     | ok               |
|          50 | -6.09%   | 39.34%             | -19.34% |    -0.18 |       50 | 24.79%     | ok               |
|          35 | -7.76%   | 39.34%             | -23.19% |    -0.2  |       66 | 34.28%     | ok               |

## DE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 2.13%    | 61.59%             | -17.97% |     0.13 |       56 | 29.62%     | ok               |
|          45 | -4.48%   | 61.59%             | -19.53% |    -0.02 |       60 | 34.11%     | ok               |
|          20 | -7.80%   | 61.59%             | -24.11% |    -0.07 |       65 | 48.59%     | ok               |
|          25 | -12.03%  | 61.59%             | -24.29% |    -0.17 |       71 | 46.92%     | ok               |
|          30 | -12.17%  | 61.59%             | -23.98% |    -0.18 |       70 | 44.26%     | ok               |

## DIA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -5.21%   | 30.10%             | -11.28% |    -0.25 |       60 | 44.76%     | ok               |
|          35 | -5.93%   | 30.10%             | -13.15% |    -0.3  |       68 | 40.60%     | ok               |
|          30 | -7.35%   | 30.10%             | -12.94% |    -0.38 |       66 | 43.59%     | ok               |
|          20 | -7.94%   | 30.10%             | -13.72% |    -0.39 |       66 | 46.76%     | ok               |
|          40 | -9.34%   | 30.10%             | -15.06% |    -0.54 |       70 | 37.44%     | ok               |

## DIS Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 33.83%   | 5.43%              | -10.17% |     1.05 |       44 | 25.46%     | ok               |
|          40 | 8.18%    | 5.43%              | -18.75% |     0.28 |       57 | 33.78%     | ok               |
|          45 | 3.62%    | 5.43%              | -16.54% |     0.17 |       45 | 29.12%     | ok               |
|          35 | -4.01%   | 5.43%              | -25.70% |    -0    |       71 | 39.77%     | ok               |
|          15 | -5.96%   | 5.43%              | -32.73% |    -0.02 |       83 | 54.58%     | ok               |

## DOGE-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -7.01%   | -66.14%            | -57.89% |     0.2  |       73 | 64.18%     | ok               |
|          20 | -14.17%  | -66.14%            | -55.83% |     0.1  |       75 | 58.81%     | ok               |
|          25 | -20.32%  | -66.14%            | -53.72% |     0.02 |       67 | 54.98%     | ok               |
|          30 | -35.81%  | -66.14%            | -60.95% |    -0.22 |       71 | 48.66%     | ok               |
|          50 | -36.84%  | -66.14%            | -55.41% |    -0.37 |       64 | 24.52%     | ok               |

## DOT-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -53.07%  | -77.14%            | -72.06% |    -0.33 |       74 | 63.41%     | ok               |
|          20 | -49.83%  | -77.14%            | -66.32% |    -0.34 |       86 | 59.39%     | ok               |
|          30 | -51.64%  | -77.14%            | -63.33% |    -0.43 |       86 | 48.47%     | ok               |
|          25 | -57.57%  | -77.14%            | -69.99% |    -0.51 |       77 | 54.41%     | ok               |
|          35 | -56.42%  | -77.14%            | -63.01% |    -0.56 |       84 | 42.91%     | ok               |

## DXY-INDEX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd    |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:-------|---------:|---------:|:-----------|:-----------------|
|          50 | -0.39%   | -4.03%             | -6.02% |    -0.05 |       40 | 32.03%     | ok               |
|          40 | -1.52%   | -4.03%             | -7.30% |    -0.18 |       64 | 47.62%     | ok               |
|          45 | -1.75%   | -4.03%             | -8.14% |    -0.23 |       60 | 38.10%     | ok               |
|          30 | -4.44%   | -4.03%             | -9.83% |    -0.52 |       74 | 57.58%     | ok               |
|          35 | -4.60%   | -4.03%             | -9.97% |    -0.58 |       77 | 52.60%     | ok               |

## EEM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -8.34%   | 51.62%             | -15.88% |    -0.25 |       54 | 32.78%     | ok               |
|          35 | -9.64%   | 51.62%             | -23.57% |    -0.26 |       66 | 38.44%     | ok               |
|          45 | -8.68%   | 51.62%             | -17.03% |    -0.26 |       52 | 34.28%     | ok               |
|          40 | -9.01%   | 51.62%             | -19.20% |    -0.26 |       64 | 36.44%     | ok               |
|          30 | -12.86%  | 51.62%             | -24.64% |    -0.37 |       62 | 40.27%     | ok               |

## EFA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -4.27%   | 26.13%             | -10.10% |    -0.09 |       64 | 51.25%     | ok               |
|          20 | -11.20%  | 26.13%             | -13.73% |    -0.4  |       71 | 48.42%     | ok               |
|          30 | -11.38%  | 26.13%             | -12.96% |    -0.44 |       64 | 41.43%     | ok               |
|          25 | -12.29%  | 26.13%             | -15.23% |    -0.47 |       70 | 44.93%     | ok               |
|          40 | -12.22%  | 26.13%             | -14.58% |    -0.53 |       62 | 36.77%     | ok               |

## EOG Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -17.66%  | 15.90%             | -35.34% |    -0.37 |       54 | 30.62%     | ok               |
|          50 | -22.19%  | 15.90%             | -35.63% |    -0.53 |       50 | 27.79%     | ok               |
|          40 | -23.88%  | 15.90%             | -37.39% |    -0.54 |       70 | 34.61%     | ok               |
|          35 | -27.88%  | 15.90%             | -41.05% |    -0.64 |       83 | 39.60%     | ok               |
|          30 | -30.38%  | 15.90%             | -47.87% |    -0.66 |       78 | 44.76%     | ok               |

## ETC-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -5.47%   | -60.15%            | -38.47% |     0.05 |       28 | 20.50%     | ok               |
|          50 | -4.94%   | -60.15%            | -31.28% |     0.05 |       28 | 18.20%     | ok               |
|          40 | -17.03%  | -60.15%            | -43.28% |    -0.15 |       38 | 23.56%     | ok               |
|          35 | -19.28%  | -60.15%            | -45.32% |    -0.16 |       42 | 27.01%     | ok               |
|          30 | -25.24%  | -60.15%            | -46.55% |    -0.25 |       58 | 30.84%     | ok               |

## ETH-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 138.28%  | -2.08%             | -30.11% |     1.27 |       58 | 48.47%     | ok               |
|          30 | 101.01%  | -2.08%             | -32.89% |     1.02 |       60 | 56.13%     | ok               |
|          40 | 60.51%   | -2.08%             | -33.11% |     0.81 |       62 | 40.80%     | ok               |
|          25 | 64.55%   | -2.08%             | -40.90% |     0.78 |       60 | 59.96%     | ok               |
|          50 | 37.75%   | -2.08%             | -30.50% |     0.64 |       66 | 30.08%     | ok               |

## EWJ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -22.99%  | 40.60%             | -29.40% |    -0.8  |       62 | 36.44%     | ok               |
|          20 | -23.95%  | 40.60%             | -30.00% |    -0.81 |       56 | 38.44%     | ok               |
|          25 | -25.82%  | 40.60%             | -29.85% |    -0.9  |       56 | 37.60%     | ok               |
|          15 | -27.60%  | 40.60%             | -31.15% |    -0.9  |       67 | 41.76%     | ok               |
|          45 | -23.60%  | 40.60%             | -27.35% |    -0.96 |       60 | 28.29%     | ok               |

## FCX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 2.51%    | 33.59%             | -29.27% |     0.18 |       50 | 31.61%     | ok               |
|          50 | -0.09%   | 33.59%             | -26.57% |     0.13 |       52 | 27.95%     | ok               |
|          40 | -10.00%  | 33.59%             | -42.89% |    -0.01 |       62 | 36.94%     | ok               |
|          30 | -29.37%  | 33.59%             | -46.84% |    -0.32 |       65 | 44.26%     | ok               |
|          35 | -29.20%  | 33.59%             | -50.12% |    -0.34 |       67 | 42.10%     | ok               |

## FET-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -34.96%  | -75.77%            | -59.58% |    -0.03 |       82 | 57.09%     | ok               |
|          20 | -33.25%  | -75.77%            | -64.89% |    -0.03 |       90 | 52.49%     | ok               |
|          25 | -34.88%  | -75.77%            | -65.31% |    -0.07 |       83 | 47.13%     | ok               |
|          30 | -50.27%  | -75.77%            | -65.38% |    -0.35 |       81 | 42.53%     | ok               |
|          50 | -39.06%  | -75.77%            | -45.19% |    -0.53 |       46 | 14.37%     | ok               |

## FIL-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -40.15%  | -63.95%            | -58.54% |    -0.34 |       65 | 37.16%     | ok               |
|          35 | -41.96%  | -63.95%            | -61.90% |    -0.42 |       58 | 31.23%     | ok               |
|          40 | -40.23%  | -63.95%            | -57.60% |    -0.44 |       48 | 26.82%     | ok               |
|          15 | -58.37%  | -63.95%            | -71.82% |    -0.57 |       91 | 49.04%     | ok               |
|          25 | -58.52%  | -63.95%            | -70.65% |    -0.66 |       76 | 40.04%     | ok               |

## FXI Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -9.55%   | 17.68%             | -22.99% |    -0.16 |       52 | 32.95%     | ok               |
|          15 | -10.39%  | 17.68%             | -21.68% |    -0.16 |       54 | 36.94%     | ok               |
|          30 | -9.80%   | 17.68%             | -24.33% |    -0.17 |       50 | 31.45%     | ok               |
|          20 | -13.00%  | 17.68%             | -24.94% |    -0.25 |       54 | 34.78%     | ok               |
|          35 | -13.29%  | 17.68%             | -27.93% |    -0.28 |       52 | 28.95%     | ok               |

## GDX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 2.74%    | 137.73%            | -28.47% |     0.17 |       60 | 38.44%     | ok               |
|          20 | 0.57%    | 137.73%            | -33.01% |     0.16 |       76 | 50.08%     | ok               |
|          35 | -3.20%   | 137.73%            | -31.73% |     0.08 |       68 | 41.10%     | ok               |
|          30 | -3.83%   | 137.73%            | -33.31% |     0.07 |       60 | 44.43%     | ok               |
|          25 | -11.71%  | 137.73%            | -38.90% |    -0.05 |       66 | 46.09%     | ok               |

## GDXJ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -27.93%  | 140.56%            | -42.33% |    -0.25 |       74 | 50.08%     | ok               |
|          50 | -28.98%  | 140.56%            | -46.83% |    -0.4  |       58 | 34.44%     | ok               |
|          35 | -37.72%  | 140.56%            | -38.56% |    -0.52 |       70 | 40.27%     | ok               |
|          30 | -39.44%  | 140.56%            | -41.57% |    -0.54 |       70 | 42.93%     | ok               |
|          25 | -43.13%  | 140.56%            | -44.03% |    -0.58 |       77 | 46.09%     | ok               |

## GE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 4.89%    | 93.77%             | -21.25% |     0.2  |       60 | 33.78%     | ok               |
|          45 | -2.34%   | 93.77%             | -21.88% |     0.05 |       70 | 36.44%     | ok               |
|          20 | -8.34%   | 93.77%             | -25.05% |    -0.03 |       71 | 52.41%     | ok               |
|          30 | -8.43%   | 93.77%             | -27.82% |    -0.04 |       76 | 48.09%     | ok               |
|          25 | -8.86%   | 93.77%             | -29.91% |    -0.05 |       72 | 49.92%     | ok               |

## GLD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | 14.41%   | 70.18%             | -13.87% |     0.41 |       48 | 46.92%     | ok               |
|          20 | 12.85%   | 70.18%             | -13.87% |     0.37 |       49 | 48.59%     | ok               |
|          30 | 8.96%    | 70.18%             | -13.87% |     0.29 |       50 | 45.76%     | ok               |
|          35 | 6.08%    | 70.18%             | -15.09% |     0.23 |       52 | 43.43%     | ok               |
|          15 | 2.48%    | 70.18%             | -18.05% |     0.15 |       57 | 51.91%     | ok               |

## GOOGL Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 60.93%   | 99.37%             | -17.38% |     1.08 |       57 | 43.76%     | ok               |
|          30 | 57.04%   | 99.37%             | -17.15% |     1.01 |       55 | 47.25%     | ok               |
|          45 | 49.48%   | 99.37%             | -11.66% |     0.99 |       50 | 37.27%     | ok               |
|          25 | 54.65%   | 99.37%             | -16.48% |     0.96 |       55 | 49.75%     | ok               |
|          50 | 43.08%   | 99.37%             | -11.52% |     0.92 |       46 | 32.45%     | ok               |

## GRT-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 57.11%   | -78.86%            | -33.74% |     0.69 |       79 | 45.79%     | ok               |
|          45 | 45.48%   | -78.86%            | -39.70% |     0.64 |       48 | 27.97%     | ok               |
|          15 | 51.80%   | -78.86%            | -42.58% |     0.64 |       69 | 62.45%     | ok               |
|          50 | 31.50%   | -78.86%            | -31.62% |     0.53 |       46 | 21.26%     | ok               |
|          25 | 33.01%   | -78.86%            | -37.67% |     0.52 |       78 | 52.49%     | ok               |

## GS Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 21.43%   | 93.10%             | -20.56% |     0.48 |       68 | 56.41%     | ok               |
|          20 | 2.78%    | 93.10%             | -23.19% |     0.16 |       68 | 53.08%     | ok               |
|          40 | 1.65%    | 93.10%             | -17.88% |     0.13 |       68 | 42.43%     | ok               |
|          25 | -2.43%   | 93.10%             | -23.32% |     0.05 |       68 | 50.58%     | ok               |
|          30 | -4.56%   | 93.10%             | -22.13% |     0    |       70 | 48.09%     | ok               |

## HBAR-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -18.60%  | -14.55%            | -39.26% |    -0.27 |       18 | 17.94%     | ok               |
|          45 | -33.67%  | -14.55%            | -48.27% |    -0.7  |       22 | 24.05%     | ok               |
|          40 | -36.66%  | -14.55%            | -50.61% |    -0.77 |       26 | 28.63%     | ok               |
|          30 | -44.98%  | -14.55%            | -57.09% |    -1.01 |       40 | 37.40%     | ok               |
|          35 | -44.40%  | -14.55%            | -56.64% |    -1.02 |       30 | 32.82%     | ok               |

## HD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 2.92%    | -13.97%            | -17.15% |     0.16 |       67 | 43.43%     | ok               |
|          35 | 2.06%    | -13.97%            | -17.81% |     0.13 |       68 | 39.43%     | ok               |
|          40 | 1.06%    | -13.97%            | -16.74% |     0.1  |       72 | 34.78%     | ok               |
|          25 | 0.32%    | -13.97%            | -18.17% |     0.09 |       66 | 45.59%     | ok               |
|          45 | 0.27%    | -13.97%            | -17.41% |     0.07 |       48 | 29.95%     | ok               |

## HON Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -11.96%  | 3.65%              | -20.54% |    -0.31 |       70 | 33.28%     | ok               |
|          45 | -15.64%  | 3.65%              | -22.88% |    -0.4  |       72 | 38.77%     | ok               |
|          35 | -25.48%  | 3.65%              | -31.30% |    -0.66 |       89 | 50.08%     | ok               |
|          40 | -25.79%  | 3.65%              | -31.84% |    -0.69 |       76 | 43.09%     | ok               |
|          30 | -27.96%  | 3.65%              | -33.53% |    -0.71 |       91 | 54.91%     | ok               |

## HYG Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -5.46%   | -0.04%             | -8.00%  |    -0.63 |       70 | 33.44%     | ok               |
|          45 | -6.63%   | -0.04%             | -9.14%  |    -0.8  |       70 | 30.12%     | ok               |
|          35 | -7.27%   | -0.04%             | -9.76%  |    -0.84 |       79 | 35.11%     | ok               |
|          30 | -7.48%   | -0.04%             | -10.59% |    -0.84 |       87 | 38.44%     | ok               |
|          20 | -7.91%   | -0.04%             | -11.59% |    -0.86 |       94 | 43.93%     | ok               |

## IBIT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 67.18%   | 23.28%             | -19.20% |     0.96 |       44 | 41.75%     | ok               |
|          50 | 52.34%   | 23.28%             | -17.37% |     0.94 |       26 | 25.66%     | ok               |
|          45 | 42.96%   | 23.28%             | -17.37% |     0.8  |       30 | 26.88%     | ok               |
|          40 | 36.57%   | 23.28%             | -17.78% |     0.71 |       30 | 28.72%     | ok               |
|          30 | 38.42%   | 23.28%             | -18.95% |     0.7  |       38 | 34.83%     | ok               |

## IBM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -18.44%  | 33.60%             | -49.43% |    -0.13 |       83 | 61.06%     | ok               |
|          35 | -21.42%  | 33.60%             | -47.10% |    -0.23 |       63 | 45.92%     | ok               |
|          30 | -24.70%  | 33.60%             | -48.94% |    -0.29 |       69 | 49.58%     | ok               |
|          20 | -30.14%  | 33.60%             | -53.45% |    -0.37 |       69 | 54.08%     | ok               |
|          45 | -28.12%  | 33.60%             | -48.72% |    -0.4  |       52 | 37.44%     | ok               |

## ICP-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -17.84%  | -45.44%            | -46.42% |     0.09 |       79 | 39.27%     | ok               |
|          35 | -11.56%  | -45.44%            | -51.30% |     0.09 |       70 | 33.33%     | ok               |
|          40 | -12.10%  | -45.44%            | -45.75% |     0.07 |       62 | 28.74%     | ok               |
|          15 | -42.76%  | -45.44%            | -59.36% |    -0.11 |       79 | 50.57%     | ok               |
|          20 | -46.10%  | -45.44%            | -62.50% |    -0.18 |       88 | 47.51%     | ok               |

## IEF Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -6.13%   | -3.81%             | -10.18% |    -0.72 |       72 | 42.26%     | ok               |
|          15 | -6.69%   | -3.81%             | -10.91% |    -0.77 |       71 | 43.76%     | ok               |
|          40 | -8.20%   | -3.81%             | -11.24% |    -1.19 |       64 | 27.29%     | ok               |
|          50 | -7.14%   | -3.81%             | -9.11%  |    -1.2  |       58 | 22.30%     | ok               |
|          25 | -9.72%   | -3.81%             | -11.95% |    -1.22 |       76 | 39.60%     | ok               |

## IEMG Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -4.04%   | 47.22%             | -14.22% |    -0.1  |       54 | 31.61%     | ok               |
|          45 | -4.83%   | 47.22%             | -15.23% |    -0.13 |       50 | 34.11%     | ok               |
|          40 | -6.29%   | 47.22%             | -18.73% |    -0.18 |       62 | 37.10%     | ok               |
|          35 | -7.68%   | 47.22%             | -23.75% |    -0.21 |       65 | 39.43%     | ok               |
|          30 | -12.49%  | 47.22%             | -27.97% |    -0.38 |       60 | 40.43%     | ok               |

## INJ-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 8.74%    | -40.82%            | -52.61% |     0.33 |       58 | 36.78%     | ok               |
|          40 | 9.38%    | -40.82%            | -45.92% |     0.32 |       48 | 33.52%     | ok               |
|          45 | 0.42%    | -40.82%            | -43.79% |     0.22 |       52 | 27.97%     | ok               |
|          30 | -23.18%  | -40.82%            | -69.36% |     0.02 |       63 | 40.23%     | ok               |
|          15 | -38.58%  | -40.82%            | -76.78% |    -0.11 |       75 | 51.34%     | ok               |

## INTC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 70.01%   | 215.73%            | -49.32% |     0.71 |       56 | 33.78%     | ok               |
|          50 | 64.73%   | 215.73%            | -48.35% |     0.68 |       60 | 29.95%     | ok               |
|          15 | 64.27%   | 215.73%            | -53.65% |     0.65 |       76 | 59.73%     | ok               |
|          40 | 51.36%   | 215.73%            | -55.86% |     0.59 |       64 | 37.94%     | ok               |
|          25 | 46.47%   | 215.73%            | -56.41% |     0.56 |       77 | 50.75%     | ok               |

## INTU Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 10.17%   | -54.34%            | -34.75% |     0.29 |       65 | 28.45%     | ok               |
|          45 | -1.24%   | -54.34%            | -40.30% |     0.1  |       65 | 32.78%     | ok               |
|          40 | -7.55%   | -54.34%            | -43.67% |    -0.01 |       69 | 36.61%     | ok               |
|          25 | -11.92%  | -54.34%            | -37.85% |    -0.06 |       70 | 49.25%     | ok               |
|          35 | -13.17%  | -54.34%            | -45.88% |    -0.11 |       71 | 40.27%     | ok               |

## ITA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -2.58%   | 51.07%             | -28.17% |     0.03 |       82 | 61.06%     | ok               |
|          50 | -1.57%   | 51.07%             | -21.48% |     0.02 |       76 | 37.10%     | ok               |
|          30 | -3.75%   | 51.07%             | -23.75% |    -0.03 |       76 | 48.75%     | ok               |
|          40 | -7.12%   | 51.07%             | -20.58% |    -0.15 |       76 | 42.10%     | ok               |
|          20 | -8.80%   | 51.07%             | -28.17% |    -0.16 |       84 | 55.07%     | ok               |

## IWM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | 10.49%   | 33.26%             | -11.88% |     0.43 |       52 | 35.11%     | ok               |
|          20 | 9.03%    | 33.26%             | -11.65% |     0.37 |       58 | 36.11%     | ok               |
|          30 | 6.80%    | 33.26%             | -12.19% |     0.3  |       54 | 34.44%     | ok               |
|          40 | 5.86%    | 33.26%             | -13.48% |     0.29 |       46 | 29.78%     | ok               |
|          15 | 5.69%    | 33.26%             | -13.33% |     0.25 |       76 | 41.93%     | ok               |

## JNJ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 17.02%   | 74.34%             | -10.57% |     0.7  |       40 | 34.78%     | ok               |
|          15 | 13.37%   | 74.34%             | -17.37% |     0.48 |       60 | 53.41%     | ok               |
|          20 | 8.13%    | 74.34%             | -16.96% |     0.33 |       66 | 49.92%     | ok               |
|          45 | 7.01%    | 74.34%             | -13.35% |     0.32 |       46 | 38.44%     | ok               |
|          30 | 6.91%    | 74.34%             | -16.86% |     0.3  |       62 | 46.59%     | ok               |

## JPM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 6.13%    | 70.93%             | -15.90% |     0.27 |       50 | 33.28%     | ok               |
|          45 | -4.45%   | 70.93%             | -21.91% |    -0.08 |       54 | 35.94%     | ok               |
|          20 | -19.92%  | 70.93%             | -35.58% |    -0.42 |       86 | 49.42%     | ok               |
|          35 | -16.90%  | 70.93%             | -27.43% |    -0.47 |       74 | 41.76%     | ok               |
|          40 | -17.56%  | 70.93%             | -28.47% |    -0.5  |       66 | 38.60%     | ok               |

## KO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 24.07%   | 43.50%             | -8.64%  |     0.85 |       54 | 37.10%     | ok               |
|          35 | 19.85%   | 43.50%             | -8.21%  |     0.73 |       58 | 35.61%     | ok               |
|          40 | 16.97%   | 43.50%             | -9.28%  |     0.68 |       60 | 32.28%     | ok               |
|          25 | 17.86%   | 43.50%             | -10.16% |     0.66 |       60 | 39.93%     | ok               |
|          20 | 4.85%    | 43.50%             | -15.99% |     0.23 |       77 | 44.09%     | ok               |

## LDO-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 60.50%   | -64.21%            | -39.01% |     0.67 |       77 | 59.39%     | ok               |
|          20 | 46.02%   | -64.21%            | -40.80% |     0.6  |       79 | 54.60%     | ok               |
|          30 | 44.87%   | -64.21%            | -50.47% |     0.6  |       70 | 46.55%     | ok               |
|          35 | 21.59%   | -64.21%            | -58.19% |     0.43 |       76 | 39.08%     | ok               |
|          25 | 13.88%   | -64.21%            | -50.23% |     0.39 |       80 | 51.72%     | ok               |

## LIN Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -8.89%   | 12.65%             | -23.00% |    -0.25 |       66 | 44.09%     | ok               |
|          25 | -8.82%   | 12.65%             | -22.01% |    -0.25 |       73 | 41.10%     | ok               |
|          15 | -10.16%  | 12.65%             | -23.68% |    -0.29 |       72 | 47.75%     | ok               |
|          30 | -11.87%  | 12.65%             | -20.61% |    -0.38 |       74 | 38.27%     | ok               |
|          35 | -13.46%  | 12.65%             | -19.70% |    -0.48 |       72 | 31.11%     | ok               |

## LINK-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 41.83%   | -24.36%            | -33.64% |     0.6  |       68 | 45.79%     | ok               |
|          45 | 20.85%   | -24.36%            | -33.71% |     0.42 |       52 | 32.18%     | ok               |
|          35 | 18.68%   | -24.36%            | -34.21% |     0.41 |       62 | 41.76%     | ok               |
|          40 | 11.00%   | -24.36%            | -34.00% |     0.32 |       58 | 36.21%     | ok               |
|          25 | -1.14%   | -24.36%            | -46.32% |     0.23 |       64 | 49.23%     | ok               |

## LLY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -2.17%   | 51.00%             | -38.23% |     0.07 |       50 | 35.44%     | ok               |
|          15 | -14.27%  | 51.00%             | -48.12% |    -0.09 |       70 | 60.40%     | ok               |
|          45 | -14.92%  | 51.00%             | -42.66% |    -0.19 |       58 | 38.94%     | ok               |
|          20 | -27.96%  | 51.00%             | -51.34% |    -0.38 |       77 | 55.41%     | ok               |
|          40 | -25.73%  | 51.00%             | -46.23% |    -0.4  |       68 | 41.93%     | ok               |

## LRCX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -19.19%  | 228.61%            | -48.71% |    -0.1  |       74 | 33.94%     | ok               |
|          40 | -21.87%  | 228.61%            | -53.45% |    -0.11 |       70 | 40.10%     | ok               |
|          35 | -23.38%  | 228.61%            | -56.72% |    -0.13 |       78 | 42.26%     | ok               |
|          30 | -27.48%  | 228.61%            | -58.92% |    -0.19 |       80 | 42.76%     | ok               |
|          15 | -33.30%  | 228.61%            | -57.13% |    -0.21 |       78 | 50.75%     | ok               |

## LTC-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 8.08%    | -40.95%            | -34.94% |     0.29 |       64 | 45.98%     | ok               |
|          45 | 6.34%    | -40.95%            | -37.46% |     0.26 |       58 | 36.40%     | ok               |
|          30 | -3.81%   | -40.95%            | -33.04% |     0.15 |       68 | 53.26%     | ok               |
|          25 | -7.27%   | -40.95%            | -34.22% |     0.11 |       70 | 55.56%     | ok               |
|          40 | -11.66%  | -40.95%            | -40.31% |     0.02 |       56 | 41.57%     | ok               |

## MCD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 10.95%   | -12.03%            | -9.22%  |     0.51 |       46 | 24.96%     | ok               |
|          40 | 1.66%    | -12.03%            | -18.49% |     0.12 |       69 | 32.45%     | ok               |
|          45 | 1.58%    | -12.03%            | -16.79% |     0.12 |       54 | 28.79%     | ok               |
|          30 | -0.23%   | -12.03%            | -21.88% |     0.05 |       79 | 40.93%     | ok               |
|          25 | -0.78%   | -12.03%            | -23.62% |     0.03 |       77 | 43.26%     | ok               |

## META Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -7.67%   | 58.47%             | -37.10% |    -0.02 |       64 | 39.60%     | ok               |
|          40 | -13.74%  | 58.47%             | -40.49% |    -0.13 |       66 | 42.60%     | ok               |
|          50 | -17.59%  | 58.47%             | -38.63% |    -0.23 |       66 | 35.27%     | ok               |
|          25 | -24.95%  | 58.47%             | -45.35% |    -0.32 |       75 | 52.91%     | ok               |
|          30 | -24.88%  | 58.47%             | -44.52% |    -0.33 |       74 | 49.92%     | ok               |

## MPC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 34.68%   | 160.57%            | -18.24% |     0.67 |       50 | 40.10%     | ok               |
|          40 | 32.46%   | 160.57%            | -20.11% |     0.61 |       60 | 46.76%     | ok               |
|          45 | 30.14%   | 160.57%            | -19.46% |     0.59 |       56 | 44.09%     | ok               |
|          35 | 29.47%   | 160.57%            | -31.08% |     0.56 |       68 | 49.42%     | ok               |
|          30 | 15.43%   | 160.57%            | -37.91% |     0.36 |       71 | 52.08%     | ok               |

## MRK Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -13.09%  | 11.04%             | -28.39% |    -0.16 |       83 | 51.91%     | ok               |
|          25 | -14.40%  | 11.04%             | -31.07% |    -0.21 |       70 | 44.26%     | ok               |
|          50 | -14.54%  | 11.04%             | -23.01% |    -0.3  |       56 | 28.45%     | ok               |
|          20 | -18.59%  | 11.04%             | -29.34% |    -0.3  |       75 | 47.59%     | ok               |
|          45 | -16.67%  | 11.04%             | -25.38% |    -0.33 |       57 | 31.78%     | ok               |

## MS Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 0.92%    | 89.39%             | -19.99% |     0.1  |       72 | 39.60%     | ok               |
|          15 | -2.94%   | 89.39%             | -22.02% |     0.03 |       74 | 58.24%     | ok               |
|          20 | -5.24%   | 89.39%             | -25.68% |    -0.03 |       75 | 53.08%     | ok               |
|          30 | -10.16%  | 89.39%             | -27.79% |    -0.17 |       75 | 48.25%     | ok               |
|          35 | -10.09%  | 89.39%             | -26.58% |    -0.18 |       76 | 44.76%     | ok               |

## MSFT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -12.34%  | 27.23%             | -24.64% |    -0.26 |       74 | 37.44%     | ok               |
|          50 | -17.47%  | 27.23%             | -25.48% |    -0.44 |       64 | 31.78%     | ok               |
|          35 | -21.70%  | 27.23%             | -35.38% |    -0.46 |       75 | 46.42%     | ok               |
|          40 | -21.88%  | 27.23%             | -34.92% |    -0.49 |       73 | 41.26%     | ok               |
|          30 | -24.95%  | 27.23%             | -39.07% |    -0.53 |       85 | 51.08%     | ok               |

## MU Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 163.97%  | 666.70%            | -63.96% |     1.09 |       58 | 48.25%     | ok               |
|          15 | 186.91%  | 666.70%            | -61.96% |     1.08 |       51 | 59.90%     | ok               |
|          30 | 137.47%  | 666.70%            | -68.76% |     0.99 |       51 | 52.91%     | ok               |
|          25 | 136.08%  | 666.70%            | -67.90% |     0.97 |       51 | 54.41%     | ok               |
|          35 | 130.90%  | 666.70%            | -69.09% |     0.97 |       63 | 50.58%     | ok               |

## NEAR-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 188.04%  | 58.51%             | -38.95% |     1.3  |       28 | 21.84%     | ok               |
|          40 | 201.45%  | 58.51%             | -41.76% |     1.25 |       42 | 31.42%     | ok               |
|          45 | 152.99%  | 58.51%             | -38.08% |     1.11 |       44 | 27.39%     | ok               |
|          30 | 153.48%  | 58.51%             | -47.03% |     1.05 |       73 | 44.25%     | ok               |
|          35 | 142.72%  | 58.51%             | -52.37% |     1.05 |       64 | 36.02%     | ok               |

## NEM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -1.41%   | 163.61%            | -31.25% |     0.15 |       62 | 58.40%     | ok               |
|          20 | -4.61%   | 163.61%            | -30.50% |     0.1  |       68 | 54.08%     | ok               |
|          25 | -21.14%  | 163.61%            | -39.51% |    -0.16 |       64 | 51.91%     | ok               |
|          50 | -19.84%  | 163.61%            | -33.24% |    -0.19 |       52 | 38.44%     | ok               |
|          30 | -29.63%  | 163.61%            | -39.56% |    -0.32 |       68 | 50.08%     | ok               |

## NFLX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 30.93%   | 10.19%             | -16.28% |     0.78 |       44 | 33.61%     | ok               |
|          40 | 29.83%   | 10.19%             | -15.02% |     0.71 |       50 | 41.60%     | ok               |
|          35 | 25.41%   | 10.19%             | -18.30% |     0.6  |       74 | 46.26%     | ok               |
|          45 | 18.20%   | 10.19%             | -15.48% |     0.49 |       56 | 38.10%     | ok               |
|          15 | 11.69%   | 10.19%             | -26.59% |     0.32 |       71 | 65.06%     | ok               |

## NKE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -19.40%  | -61.48%            | -49.34% |    -0.15 |       83 | 53.58%     | ok               |
|          35 | -16.21%  | -61.48%            | -42.13% |    -0.15 |       71 | 40.43%     | ok               |
|          25 | -22.75%  | -61.48%            | -51.20% |    -0.21 |       83 | 50.92%     | ok               |
|          15 | -24.60%  | -61.48%            | -54.28% |    -0.23 |       86 | 57.40%     | ok               |
|          30 | -26.43%  | -61.48%            | -55.35% |    -0.28 |       79 | 46.92%     | ok               |

## NOW Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 9.63%    | -9.38%             | -30.43% |     0.29 |       80 | 50.08%     | ok               |
|          20 | 8.52%    | -9.38%             | -39.71% |     0.28 |       75 | 56.57%     | ok               |
|          25 | 4.47%    | -9.38%             | -37.51% |     0.23 |       72 | 53.58%     | ok               |
|          15 | 0.58%    | -9.38%             | -43.06% |     0.19 |       83 | 59.57%     | ok               |
|          40 | -0.02%   | -9.38%             | -36.21% |     0.15 |       70 | 39.27%     | ok               |

## NVDA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -34.03%  | 86.90%             | -41.21% |    -0.5  |       76 | 44.03%     | ok               |
|          20 | -42.80%  | 86.90%             | -42.84% |    -0.59 |       76 | 52.05%     | ok               |
|          25 | -42.70%  | 86.90%             | -42.74% |    -0.65 |       77 | 47.06%     | ok               |
|          15 | -48.99%  | 86.90%             | -52.37% |    -0.69 |       77 | 55.26%     | ok               |
|          35 | -43.95%  | 86.90%             | -49.91% |    -0.78 |       86 | 41.18%     | ok               |

## OP-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 39.39%   | -84.83%            | -21.53% |     0.71 |       30 | 9.00%      | ok               |
|          45 | 34.88%   | -84.83%            | -25.91% |     0.59 |       32 | 13.60%     | ok               |
|          40 | 5.70%    | -84.83%            | -38.97% |     0.25 |       44 | 21.84%     | ok               |
|          35 | -27.88%  | -84.83%            | -51.22% |    -0.19 |       56 | 26.82%     | ok               |
|          15 | -39.53%  | -84.83%            | -55.83% |    -0.2  |       72 | 44.64%     | ok               |

## ORCL Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 164.67%  | 10.34%             | -32.54% |     1.11 |       69 | 62.06%     | ok               |
|          25 | 112.80%  | 10.34%             | -27.76% |     0.92 |       61 | 54.58%     | ok               |
|          45 | 97.83%   | 10.34%             | -32.35% |     0.91 |       58 | 40.10%     | ok               |
|          35 | 102.73%  | 10.34%             | -31.95% |     0.9  |       62 | 48.75%     | ok               |
|          20 | 106.87%  | 10.34%             | -29.32% |     0.89 |       70 | 57.74%     | ok               |

## OXY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 2.12%    | -3.84%             | -28.48% |     0.16 |       73 | 42.43%     | ok               |
|          35 | -0.17%   | -3.84%             | -26.37% |     0.11 |       74 | 37.94%     | ok               |
|          50 | -3.87%   | -3.84%             | -27.38% |     0.03 |       46 | 26.79%     | ok               |
|          40 | -6.32%   | -3.84%             | -28.30% |    -0.01 |       64 | 33.78%     | ok               |
|          25 | -12.01%  | -3.84%             | -38.51% |    -0.09 |       79 | 46.09%     | ok               |

## PEP Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 16.24%   | -29.74%            | -11.62% |     0.69 |       38 | 25.46%     | ok               |
|          45 | 8.81%    | -29.74%            | -14.22% |     0.39 |       54 | 29.45%     | ok               |
|          35 | 5.62%    | -29.74%            | -21.42% |     0.24 |       75 | 39.77%     | ok               |
|          40 | 3.35%    | -29.74%            | -18.04% |     0.18 |       68 | 35.11%     | ok               |
|          30 | -0.60%   | -29.74%            | -21.35% |     0.05 |       76 | 45.92%     | ok               |

## PEPE-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -54.13%  | -69.84%            | -61.29% |    -0.4  |       83 | 48.66%     | ok               |
|          25 | -60.03%  | -69.84%            | -64.26% |    -0.5  |       93 | 53.64%     | ok               |
|          15 | -68.13%  | -69.84%            | -69.80% |    -0.51 |       82 | 62.84%     | ok               |
|          35 | -55.68%  | -69.84%            | -61.54% |    -0.53 |       72 | 43.68%     | ok               |
|          20 | -65.01%  | -69.84%            | -66.84% |    -0.54 |       88 | 59.39%     | ok               |

## PFE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -18.42%  | -0.46%             | -25.68% |    -0.59 |       54 | 21.80%     | ok               |
|          40 | -19.46%  | -0.46%             | -29.27% |    -0.6  |       74 | 26.96%     | ok               |
|          50 | -18.88%  | -0.46%             | -27.67% |    -0.67 |       42 | 18.64%     | ok               |
|          35 | -27.21%  | -0.46%             | -34.89% |    -0.85 |       84 | 33.44%     | ok               |
|          30 | -33.76%  | -0.46%             | -41.77% |    -1.03 |       81 | 37.10%     | ok               |

## PG Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -11.19%  | -8.43%             | -17.93% |    -0.45 |       54 | 27.79%     | ok               |
|          35 | -16.48%  | -8.43%             | -18.99% |    -0.67 |       62 | 31.45%     | ok               |
|          45 | -19.87%  | -8.43%             | -20.34% |    -0.92 |       54 | 25.29%     | ok               |
|          30 | -24.07%  | -8.43%             | -24.55% |    -0.98 |       64 | 34.61%     | ok               |
|          25 | -25.80%  | -8.43%             | -26.24% |    -1.05 |       76 | 36.11%     | ok               |

## PM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | -4.14%   | 102.83%            | -32.20% |    -0.01 |       84 | 46.92%     | ok               |
|          20 | -6.64%   | 102.83%            | -33.51% |    -0.05 |       83 | 55.57%     | ok               |
|          30 | -7.15%   | 102.83%            | -35.15% |    -0.07 |       79 | 50.42%     | ok               |
|          40 | -11.46%  | 102.83%            | -37.94% |    -0.21 |       78 | 42.93%     | ok               |
|          50 | -10.99%  | 102.83%            | -35.70% |    -0.22 |       68 | 37.10%     | ok               |

## POL-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 51.05%   | -61.77%            | -38.69% |     0.67 |       79 | 49.62%     | ok               |
|          25 | 25.17%   | -61.77%            | -38.69% |     0.46 |       71 | 54.98%     | ok               |
|          20 | 11.44%   | -61.77%            | -41.15% |     0.34 |       79 | 58.81%     | ok               |
|          40 | 4.59%    | -61.77%            | -31.98% |     0.24 |       56 | 30.84%     | ok               |
|          15 | -11.42%  | -61.77%            | -46.34% |     0.12 |       82 | 62.84%     | ok               |

## QCOM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -11.57%  | -11.80%            | -55.66% |     0.03 |       71 | 45.42%     | ok               |
|          20 | -20.85%  | -11.80%            | -57.05% |    -0.09 |       68 | 48.92%     | ok               |
|          35 | -19.03%  | -11.80%            | -51.84% |    -0.09 |       79 | 41.10%     | ok               |
|          15 | -30.42%  | -11.80%            | -60.40% |    -0.23 |       70 | 51.58%     | ok               |
|          30 | -28.48%  | -11.80%            | -57.69% |    -0.24 |       77 | 43.59%     | ok               |

## QQQ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 25.18%   | 64.00%             | -14.17% |     0.62 |       63 | 54.08%     | ok               |
|          25 | 16.68%   | 64.00%             | -12.88% |     0.48 |       61 | 48.09%     | ok               |
|          20 | 15.49%   | 64.00%             | -12.98% |     0.44 |       69 | 50.75%     | ok               |
|          30 | 8.80%    | 64.00%             | -14.20% |     0.31 |       66 | 46.09%     | ok               |
|          35 | -2.38%   | 64.00%             | -20.59% |     0.01 |       72 | 42.26%     | ok               |

## RENDER-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 41.49%   | -60.14%            | -44.59% |     0.58 |       82 | 61.30%     | ok               |
|          20 | 38.49%   | -60.14%            | -43.43% |     0.56 |       85 | 58.05%     | ok               |
|          25 | 32.09%   | -60.14%            | -41.13% |     0.52 |       85 | 53.07%     | ok               |
|          30 | -12.44%  | -60.14%            | -44.65% |     0.15 |       90 | 47.13%     | ok               |
|          35 | -24.55%  | -60.14%            | -46.00% |    -0.03 |       86 | 40.61%     | ok               |

## RTX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 43.96%   | 77.74%             | -18.66% |     0.9  |       74 | 57.24%     | ok               |
|          25 | 39.04%   | 77.74%             | -18.59% |     0.83 |       62 | 54.58%     | ok               |
|          15 | 35.26%   | 77.74%             | -19.55% |     0.75 |       67 | 61.73%     | ok               |
|          30 | 31.00%   | 77.74%             | -16.99% |     0.71 |       64 | 52.25%     | ok               |
|          35 | 23.29%   | 77.74%             | -18.00% |     0.62 |       58 | 49.08%     | ok               |

## SBUX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | 1.34%    | 19.02%             | -23.55% |     0.13 |       57 | 40.27%     | ok               |
|          40 | -4.63%   | 19.02%             | -25.43% |    -0.02 |       62 | 32.45%     | ok               |
|          45 | -6.16%   | 19.02%             | -27.26% |    -0.08 |       66 | 27.45%     | ok               |
|          35 | -8.91%   | 19.02%             | -26.54% |    -0.11 |       60 | 35.61%     | ok               |
|          20 | -10.74%  | 19.02%             | -30.94% |    -0.11 |       60 | 42.26%     | ok               |

## SCHW Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -8.03%   | 23.39%             | -28.76% |    -0.1  |       67 | 48.59%     | ok               |
|          45 | -7.03%   | 23.39%             | -16.53% |    -0.15 |       62 | 30.95%     | ok               |
|          20 | -12.69%  | 23.39%             | -29.24% |    -0.22 |       75 | 51.08%     | ok               |
|          50 | -8.20%   | 23.39%             | -13.28% |    -0.24 |       54 | 27.95%     | ok               |
|          40 | -15.04%  | 23.39%             | -23.35% |    -0.37 |       72 | 35.61%     | ok               |

## SHIB-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -28.67%  | -69.19%            | -41.14% |    -0.26 |       62 | 38.31%     | ok               |
|          35 | -30.53%  | -69.19%            | -44.56% |    -0.26 |       73 | 45.98%     | ok               |
|          15 | -37.28%  | -69.19%            | -45.04% |    -0.3  |       86 | 66.67%     | ok               |
|          25 | -38.03%  | -69.19%            | -45.83% |    -0.34 |       80 | 58.05%     | ok               |
|          20 | -39.45%  | -69.19%            | -47.68% |    -0.35 |       80 | 61.69%     | ok               |

## SHY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd    |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:-------|---------:|---------:|:-----------|:-----------------|
|          30 | -1.78%   | -0.28%             | -3.30% |    -0.6  |       46 | 36.77%     | ok               |
|          35 | -2.39%   | -0.28%             | -3.61% |    -0.82 |       52 | 35.27%     | ok               |
|          40 | -2.41%   | -0.28%             | -3.58% |    -0.83 |       54 | 33.94%     | ok               |
|          45 | -2.40%   | -0.28%             | -3.43% |    -0.88 |       54 | 28.62%     | ok               |
|          25 | -3.08%   | -0.28%             | -4.43% |    -1.02 |       60 | 39.27%     | ok               |

## SKY-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | -58.92%  | -2.50%             | -59.75% |    -0.98 |       78 | 36.97%     | ok               |
|          30 | -62.09%  | -2.50%             | -61.82% |    -1.01 |       85 | 44.64%     | ok               |
|          15 | -67.93%  | -2.50%             | -67.57% |    -1.06 |       75 | 54.02%     | ok               |
|          25 | -66.05%  | -2.50%             | -65.67% |    -1.11 |       78 | 47.89%     | ok               |
|          40 | -64.15%  | -2.50%             | -64.87% |    -1.22 |       66 | 33.52%     | ok               |

## SLB Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 6.66%    | 1.12%              | -28.43% |     0.23 |       50 | 35.11%     | ok               |
|          45 | 6.33%    | 1.12%              | -25.36% |     0.23 |       62 | 31.61%     | ok               |
|          50 | -8.25%   | 1.12%              | -29.54% |    -0.11 |       52 | 26.62%     | ok               |
|          35 | -22.18%  | 1.12%              | -45.96% |    -0.36 |       72 | 42.60%     | ok               |
|          25 | -35.77%  | 1.12%              | -55.80% |    -0.64 |       86 | 53.08%     | ok               |

## SLV Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 36.16%   | 87.54%             | -34.10% |     0.59 |       52 | 30.12%     | ok               |
|          45 | 24.59%   | 87.54%             | -31.82% |     0.46 |       63 | 31.61%     | ok               |
|          40 | 23.61%   | 87.54%             | -34.28% |     0.45 |       67 | 33.61%     | ok               |
|          15 | 13.46%   | 87.54%             | -47.98% |     0.34 |       71 | 48.75%     | ok               |
|          20 | 13.48%   | 87.54%             | -42.66% |     0.34 |       70 | 43.93%     | ok               |

## SMH Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 68.03%   | 151.49%            | -31.66% |     0.96 |       47 | 46.92%     | ok               |
|          25 | 52.09%   | 151.49%            | -33.57% |     0.82 |       44 | 45.59%     | ok               |
|          35 | 50.48%   | 151.49%            | -34.65% |     0.82 |       54 | 42.60%     | ok               |
|          30 | 47.95%   | 151.49%            | -34.29% |     0.78 |       48 | 44.26%     | ok               |
|          45 | 37.18%   | 151.49%            | -33.35% |     0.7  |       54 | 36.77%     | ok               |

## SNX-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 3.99%    | -73.18%            | -41.29% |     0.25 |       54 | 27.20%     | ok               |
|          40 | 3.93%    | -73.18%            | -36.00% |     0.22 |       44 | 22.22%     | ok               |
|          20 | -9.46%   | -73.18%            | -53.03% |     0.14 |       71 | 43.68%     | ok               |
|          30 | -9.86%   | -73.18%            | -50.74% |     0.1  |       62 | 33.52%     | ok               |
|          15 | -34.57%  | -73.18%            | -54.74% |    -0.16 |       77 | 48.28%     | ok               |

## SOL-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 33.46%   | -39.01%            | -39.74% |     0.55 |       60 | 41.00%     | ok               |
|          35 | 11.22%   | -39.01%            | -43.70% |     0.34 |       72 | 47.51%     | ok               |
|          45 | 3.45%    | -39.01%            | -46.83% |     0.23 |       62 | 35.25%     | ok               |
|          15 | -6.73%   | -39.01%            | -46.84% |     0.16 |       70 | 63.98%     | ok               |
|          25 | -9.26%   | -39.01%            | -41.36% |     0.12 |       72 | 58.05%     | ok               |

## SOXX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | 64.30%   | 133.58%            | -39.32% |     0.9  |       53 | 45.42%     | ok               |
|          35 | 60.60%   | 133.58%            | -38.76% |     0.88 |       56 | 40.93%     | ok               |
|          30 | 59.74%   | 133.58%            | -39.81% |     0.86 |       54 | 43.26%     | ok               |
|          20 | 49.79%   | 133.58%            | -39.19% |     0.75 |       59 | 46.42%     | ok               |
|          40 | 40.91%   | 133.58%            | -41.03% |     0.69 |       58 | 38.77%     | ok               |

## SPY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 10.96%   | 46.79%             | -14.25% |     0.41 |       59 | 53.41%     | ok               |
|          15 | 10.43%   | 46.79%             | -16.80% |     0.39 |       63 | 56.07%     | ok               |
|          25 | 5.98%    | 46.79%             | -14.25% |     0.26 |       59 | 52.41%     | ok               |
|          30 | -0.17%   | 46.79%             | -15.53% |     0.05 |       64 | 49.75%     | ok               |
|          35 | -1.14%   | 46.79%             | -15.58% |     0.02 |       62 | 46.59%     | ok               |

## SUSHI-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -13.55%  | -72.72%            | -34.75% |    -0.03 |       56 | 16.86%     | ok               |
|          45 | -46.30%  | -72.72%            | -57.99% |    -0.59 |       58 | 21.65%     | ok               |
|          40 | -50.45%  | -72.72%            | -60.82% |    -0.61 |       61 | 28.16%     | ok               |
|          35 | -61.23%  | -72.72%            | -67.69% |    -0.81 |       82 | 33.14%     | ok               |
|          15 | -74.32%  | -72.72%            | -74.86% |    -0.96 |       88 | 49.62%     | ok               |

## T Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 68.64%   | 28.37%             | -15.08% |     1.13 |       73 | 65.56%     | ok               |
|          20 | 64.48%   | 28.37%             | -18.13% |     1.11 |       68 | 61.06%     | ok               |
|          25 | 62.61%   | 28.37%             | -17.66% |     1.1  |       68 | 58.90%     | ok               |
|          30 | 47.48%   | 28.37%             | -17.01% |     0.91 |       72 | 56.74%     | ok               |
|          35 | 31.40%   | 28.37%             | -14.49% |     0.69 |       78 | 52.41%     | ok               |

## TGT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -11.80%  | -1.97%             | -34.98% |    -0.18 |       62 | 37.77%     | ok               |
|          45 | -11.70%  | -1.97%             | -25.62% |    -0.22 |       50 | 28.62%     | ok               |
|          20 | -16.69%  | -1.97%             | -38.96% |    -0.25 |       88 | 45.42%     | ok               |
|          25 | -15.93%  | -1.97%             | -38.33% |    -0.27 |       72 | 40.93%     | ok               |
|          40 | -16.78%  | -1.97%             | -29.65% |    -0.35 |       52 | 31.28%     | ok               |

## TIA-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -29.00%  | -81.31%            | -66.82% |     0.09 |       96 | 59.20%     | ok               |
|          25 | -39.44%  | -81.31%            | -70.91% |    -0.08 |       94 | 48.47%     | ok               |
|          35 | -30.38%  | -81.31%            | -66.58% |    -0.1  |       76 | 35.63%     | ok               |
|          20 | -43.55%  | -81.31%            | -71.78% |    -0.11 |       91 | 53.83%     | ok               |
|          50 | -22.68%  | -81.31%            | -62.29% |    -0.24 |       40 | 12.84%     | ok               |

## TLT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -10.82%  | -14.34%            | -13.43% |    -1.16 |       36 | 17.97%     | ok               |
|          40 | -14.91%  | -14.34%            | -17.65% |    -1.29 |       54 | 25.46%     | ok               |
|          30 | -18.75%  | -14.34%            | -21.85% |    -1.4  |       68 | 33.78%     | ok               |
|          45 | -13.88%  | -14.34%            | -15.92% |    -1.4  |       46 | 21.13%     | ok               |
|          35 | -18.89%  | -14.34%            | -21.33% |    -1.55 |       66 | 29.12%     | ok               |

## TMO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 54.46%   | 11.49%             | -8.17%  |     1.13 |       48 | 35.27%     | ok               |
|          45 | 42.63%   | 11.49%             | -9.69%  |     0.9  |       52 | 39.93%     | ok               |
|          40 | 36.35%   | 11.49%             | -9.91%  |     0.78 |       57 | 44.93%     | ok               |
|          35 | 31.11%   | 11.49%             | -13.84% |     0.66 |       69 | 50.25%     | ok               |
|          20 | 29.22%   | 11.49%             | -22.89% |     0.59 |       78 | 61.40%     | ok               |

## TMUS Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 0.08%    | -7.34%             | -29.75% |     0.1  |       76 | 47.75%     | ok               |
|          15 | -5.82%   | -7.34%             | -38.16% |    -0.01 |       70 | 60.40%     | ok               |
|          25 | -9.45%   | -7.34%             | -36.31% |    -0.11 |       79 | 50.75%     | ok               |
|          20 | -11.25%  | -7.34%             | -36.84% |    -0.14 |       76 | 54.74%     | ok               |
|          50 | -7.82%   | -7.34%             | -32.36% |    -0.14 |       60 | 34.44%     | ok               |

## TRX-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 11.57%   | 23.98%             | -18.79% |     0.42 |       54 | 39.85%     | ok               |
|          35 | 6.14%    | 23.98%             | -21.77% |     0.26 |       66 | 48.28%     | ok               |
|          20 | 3.66%    | 23.98%             | -25.45% |     0.19 |       61 | 58.05%     | ok               |
|          30 | 3.59%    | 23.98%             | -22.90% |     0.19 |       66 | 51.15%     | ok               |
|          45 | 1.77%    | 23.98%             | -22.76% |     0.13 |       46 | 36.21%     | ok               |

## TSLA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 41.47%   | 116.08%            | -30.57% |     0.6  |       64 | 30.12%     | ok               |
|          40 | 13.71%   | 116.08%            | -50.11% |     0.34 |       63 | 35.61%     | ok               |
|          45 | -10.53%  | 116.08%            | -52.01% |     0.07 |       69 | 32.61%     | ok               |
|          35 | -20.51%  | 116.08%            | -60.12% |    -0.03 |       76 | 38.10%     | ok               |
|          30 | -37.10%  | 116.08%            | -59.64% |    -0.26 |       80 | 42.93%     | ok               |

## TXN Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 6.40%    | 41.44%             | -45.45% |     0.23 |       68 | 32.78%     | ok               |
|          35 | -13.11%  | 41.44%             | -43.28% |    -0.08 |       78 | 47.25%     | ok               |
|          40 | -14.63%  | 41.44%             | -45.67% |    -0.11 |       74 | 44.93%     | ok               |
|          20 | -18.53%  | 41.44%             | -38.49% |    -0.12 |       68 | 56.91%     | ok               |
|          45 | -15.74%  | 41.44%             | -46.24% |    -0.14 |       82 | 38.77%     | ok               |

## UNH Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 23.78%   | -26.82%            | -36.91% |     0.47 |       56 | 28.29%     | ok               |
|          30 | 23.15%   | -26.82%            | -26.31% |     0.45 |       77 | 48.42%     | ok               |
|          35 | 19.41%   | -26.82%            | -27.34% |     0.4  |       72 | 43.43%     | ok               |
|          20 | 19.24%   | -26.82%            | -26.96% |     0.4  |       80 | 57.74%     | ok               |
|          15 | 19.20%   | -26.82%            | -26.07% |     0.39 |       85 | 63.89%     | ok               |

## UNI-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 85.98%   | -1.81%             | -25.49% |     0.91 |       50 | 26.05%     | ok               |
|          45 | 70.23%   | -1.81%             | -34.45% |     0.78 |       56 | 33.52%     | ok               |
|          40 | 47.94%   | -1.81%             | -47.29% |     0.63 |       60 | 38.70%     | ok               |
|          35 | 29.75%   | -1.81%             | -54.44% |     0.5  |       70 | 44.25%     | ok               |
|          20 | -37.10%  | -1.81%             | -74.08% |    -0.06 |       92 | 59.58%     | ok               |

## UPS Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | -28.34%  | -35.40%            | -31.52% |    -0.53 |       62 | 36.44%     | ok               |
|          40 | -28.13%  | -35.40%            | -31.55% |    -0.53 |       58 | 30.95%     | ok               |
|          20 | -34.29%  | -35.40%            | -38.62% |    -0.63 |       84 | 49.92%     | ok               |
|          25 | -34.82%  | -35.40%            | -39.11% |    -0.66 |       76 | 46.59%     | ok               |
|          15 | -36.61%  | -35.40%            | -40.79% |    -0.68 |       86 | 53.74%     | ok               |

## USO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 5.79%    | 96.83%             | -33.44% |     0.22 |       48 | 25.79%     | ok               |
|          20 | 4.37%    | 96.83%             | -44.30% |     0.21 |       74 | 37.77%     | ok               |
|          15 | 1.03%    | 96.83%             | -45.22% |     0.17 |       68 | 41.43%     | ok               |
|          25 | -4.18%   | 96.83%             | -45.85% |     0.08 |       68 | 35.27%     | ok               |
|          50 | -3.42%   | 96.83%             | -29.54% |     0.07 |       52 | 24.13%     | ok               |

## VEA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 6.27%    | 36.83%             | -15.99% |     0.28 |       54 | 50.08%     | ok               |
|          20 | 0.09%    | 36.83%             | -17.38% |     0.06 |       59 | 47.42%     | ok               |
|          25 | -3.73%   | 36.83%             | -17.47% |    -0.1  |       57 | 45.42%     | ok               |
|          30 | -4.61%   | 36.83%             | -17.61% |    -0.14 |       60 | 42.60%     | ok               |
|          35 | -5.49%   | 36.83%             | -16.46% |    -0.18 |       52 | 40.93%     | ok               |

## VIXY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -56.61%  | -64.70%            | -69.78% |    -0.67 |       36 | 9.65%      | ok               |
|          15 | -77.69%  | -64.70%            | -89.47% |    -0.81 |       95 | 43.59%     | ok               |
|          45 | -65.91%  | -64.70%            | -75.03% |    -0.88 |       56 | 14.64%     | ok               |
|          30 | -78.34%  | -64.70%            | -88.17% |    -0.95 |       94 | 32.61%     | ok               |
|          40 | -73.25%  | -64.70%            | -80.72% |    -1    |       68 | 18.47%     | ok               |

## VNQ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -10.47%  | 8.26%              | -19.07% |    -0.47 |       62 | 28.62%     | ok               |
|          25 | -13.31%  | 8.26%              | -22.34% |    -0.51 |       69 | 42.76%     | ok               |
|          50 | -11.36%  | 8.26%              | -17.13% |    -0.54 |       54 | 25.29%     | ok               |
|          30 | -15.26%  | 8.26%              | -24.92% |    -0.61 |       73 | 40.10%     | ok               |
|          40 | -15.21%  | 8.26%              | -24.84% |    -0.67 |       80 | 34.11%     | ok               |

## VTI Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 11.78%   | 45.32%             | -13.96% |     0.44 |       62 | 53.91%     | ok               |
|          15 | 7.18%    | 45.32%             | -15.70% |     0.29 |       59 | 56.24%     | ok               |
|          25 | -0.15%   | 45.32%             | -15.00% |     0.06 |       58 | 51.75%     | ok               |
|          30 | -7.64%   | 45.32%             | -17.64% |    -0.22 |       68 | 49.75%     | ok               |
|          40 | -8.75%   | 45.32%             | -19.77% |    -0.29 |       72 | 42.26%     | ok               |

## VWO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -11.25%  | 33.36%             | -22.18% |    -0.44 |       56 | 28.62%     | ok               |
|          15 | -14.02%  | 33.36%             | -23.73% |    -0.45 |       74 | 47.09%     | ok               |
|          45 | -12.43%  | 33.36%             | -23.75% |    -0.48 |       58 | 31.28%     | ok               |
|          40 | -12.88%  | 33.36%             | -23.57% |    -0.49 |       68 | 34.11%     | ok               |
|          20 | -15.39%  | 33.36%             | -25.88% |    -0.52 |       71 | 44.76%     | ok               |

## VZ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -3.07%   | 6.63%              | -12.96% |    -0.04 |       56 | 28.62%     | ok               |
|          20 | -19.23%  | 6.63%              | -35.02% |    -0.37 |       78 | 50.75%     | ok               |
|          25 | -15.93%  | 6.63%              | -22.13% |    -0.4  |       81 | 45.76%     | ok               |
|          45 | -15.57%  | 6.63%              | -21.86% |    -0.46 |       70 | 32.45%     | ok               |
|          35 | -16.19%  | 6.63%              | -22.96% |    -0.46 |       64 | 38.10%     | ok               |

## WFC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | -8.37%   | 37.27%             | -21.57% |    -0.11 |       77 | 44.43%     | ok               |
|          50 | -6.21%   | 37.27%             | -18.29% |    -0.13 |       58 | 32.61%     | ok               |
|          20 | -19.24%  | 37.27%             | -29.87% |    -0.28 |       77 | 52.91%     | ok               |
|          30 | -17.91%  | 37.27%             | -28.90% |    -0.29 |       80 | 47.59%     | ok               |
|          40 | -14.03%  | 37.27%             | -23.94% |    -0.33 |       72 | 41.10%     | ok               |

## WIF-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 15.82%   | -77.53%            | -40.67% |     0.41 |       69 | 44.44%     | ok               |
|          25 | 4.01%    | -77.53%            | -44.74% |     0.31 |       67 | 40.42%     | ok               |
|          15 | -9.49%   | -77.53%            | -46.21% |     0.22 |       79 | 47.70%     | ok               |
|          50 | -7.18%   | -77.53%            | -35.47% |     0.05 |       34 | 13.03%     | ok               |
|          30 | -32.76%  | -77.53%            | -52.76% |    -0.09 |       68 | 37.36%     | ok               |

## WMT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 32.78%   | 76.19%             | -12.19% |     1.02 |       34 | 37.10%     | ok               |
|          45 | 34.77%   | 76.19%             | -14.14% |     1.02 |       42 | 39.60%     | ok               |
|          35 | 24.94%   | 76.19%             | -18.25% |     0.73 |       58 | 45.92%     | ok               |
|          40 | 23.33%   | 76.19%             | -18.53% |     0.71 |       50 | 41.26%     | ok               |
|          15 | 6.60%    | 76.19%             | -26.24% |     0.24 |       82 | 59.90%     | ok               |

## XBI Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 10.14%   | 64.08%             | -16.08% |     0.33 |       54 | 34.78%     | ok               |
|          45 | 5.96%    | 64.08%             | -15.46% |     0.23 |       52 | 32.28%     | ok               |
|          35 | -2.07%   | 64.08%             | -17.66% |     0.03 |       62 | 37.77%     | ok               |
|          50 | -3.16%   | 64.08%             | -15.57% |    -0.01 |       52 | 29.12%     | ok               |
|          30 | -4.11%   | 64.08%             | -18.01% |    -0.02 |       64 | 39.27%     | ok               |

## XLB Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -3.99%   | 7.15%              | -16.40% |    -0.12 |       40 | 22.30%     | ok               |
|          40 | -4.87%   | 7.15%              | -18.27% |    -0.14 |       56 | 26.46%     | ok               |
|          45 | -7.42%   | 7.15%              | -18.10% |    -0.26 |       44 | 23.96%     | ok               |
|          35 | -8.10%   | 7.15%              | -21.38% |    -0.26 |       56 | 29.95%     | ok               |
|          25 | -11.85%  | 7.15%              | -23.37% |    -0.4  |       64 | 35.94%     | ok               |

## XLC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 12.62%   | 34.52%             | -12.33% |     0.47 |       61 | 50.25%     | ok               |
|          25 | 12.06%   | 34.52%             | -12.31% |     0.45 |       60 | 52.41%     | ok               |
|          20 | 11.44%   | 34.52%             | -11.04% |     0.41 |       63 | 54.91%     | ok               |
|          50 | 7.23%    | 34.52%             | -11.12% |     0.38 |       64 | 38.44%     | ok               |
|          40 | 7.80%    | 34.52%             | -13.38% |     0.34 |       62 | 43.93%     | ok               |

## XLE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -0.64%   | 39.94%             | -25.98% |     0.06 |       56 | 36.27%     | ok               |
|          35 | -3.74%   | 39.94%             | -26.89% |    -0.01 |       65 | 42.76%     | ok               |
|          45 | -3.92%   | 39.94%             | -28.46% |    -0.03 |       60 | 38.44%     | ok               |
|          30 | -5.32%   | 39.94%             | -30.31% |    -0.05 |       69 | 44.93%     | ok               |
|          25 | -9.17%   | 39.94%             | -33.14% |    -0.14 |       80 | 47.92%     | ok               |

## XLF Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -1.43%   | 31.35%             | -18.63% |     0.01 |       72 | 51.75%     | ok               |
|          15 | -3.00%   | 31.35%             | -20.19% |    -0.04 |       78 | 54.58%     | ok               |
|          25 | -8.31%   | 31.35%             | -23.22% |    -0.24 |       79 | 48.59%     | ok               |
|          30 | -8.91%   | 31.35%             | -23.61% |    -0.27 |       80 | 46.59%     | ok               |
|          35 | -15.99%  | 31.35%             | -24.48% |    -0.61 |       70 | 42.93%     | ok               |

## XLI Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 6.87%    | 34.71%             | -10.01% |     0.29 |       86 | 51.58%     | ok               |
|          20 | 1.42%    | 34.71%             | -12.74% |     0.11 |       75 | 46.42%     | ok               |
|          50 | -4.76%   | 34.71%             | -14.94% |    -0.18 |       60 | 31.78%     | ok               |
|          45 | -5.38%   | 34.71%             | -16.29% |    -0.19 |       70 | 34.28%     | ok               |
|          25 | -8.78%   | 34.71%             | -17.03% |    -0.29 |       78 | 44.43%     | ok               |

## XLK Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 74.18%   | 83.25%             | -14.75% |     1.2  |       45 | 51.91%     | ok               |
|          20 | 69.86%   | 83.25%             | -14.75% |     1.2  |       46 | 49.75%     | ok               |
|          25 | 63.90%   | 83.25%             | -14.75% |     1.16 |       42 | 47.75%     | ok               |
|          30 | 54.09%   | 83.25%             | -14.75% |     1.05 |       42 | 46.42%     | ok               |
|          35 | 35.02%   | 83.25%             | -13.61% |     0.78 |       56 | 43.59%     | ok               |

## XLM-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -5.00%   | -39.26%            | -50.26% |     0.17 |       70 | 49.62%     | ok               |
|          50 | -4.38%   | -39.26%            | -48.81% |     0.13 |       44 | 26.82%     | ok               |
|          45 | -5.44%   | -39.26%            | -51.28% |     0.12 |       54 | 31.80%     | ok               |
|          40 | -10.11%  | -39.26%            | -47.28% |     0.08 |       52 | 36.78%     | ok               |
|          30 | -13.32%  | -39.26%            | -55.76% |     0.06 |       68 | 47.51%     | ok               |

## XLP Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 10.10%   | 8.68%              | -5.66%  |     0.64 |       54 | 29.45%     | ok               |
|          40 | 7.88%    | 8.68%              | -7.77%  |     0.49 |       70 | 33.61%     | ok               |
|          35 | 6.94%    | 8.68%              | -9.73%  |     0.43 |       66 | 36.61%     | ok               |
|          50 | 6.21%    | 8.68%              | -6.08%  |     0.43 |       60 | 27.29%     | ok               |
|          30 | 3.85%    | 8.68%              | -10.28% |     0.25 |       67 | 38.44%     | ok               |

## XLU Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 4.95%    | 15.29%             | -14.03% |     0.28 |       54 | 30.62%     | ok               |
|          45 | 3.80%    | 15.29%             | -14.97% |     0.22 |       58 | 31.78%     | ok               |
|          40 | 0.77%    | 15.29%             | -16.41% |     0.08 |       64 | 33.78%     | ok               |
|          35 | -1.90%   | 15.29%             | -19.71% |    -0.04 |       64 | 36.44%     | ok               |
|          30 | -6.15%   | 15.29%             | -20.40% |    -0.22 |       69 | 39.93%     | ok               |

## XLV Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -21.89%  | 17.80%             | -22.40% |    -1.04 |       76 | 38.77%     | ok               |
|          30 | -22.24%  | 17.80%             | -22.75% |    -1.07 |       76 | 37.10%     | ok               |
|          15 | -25.11%  | 17.80%             | -25.35% |    -1.17 |       83 | 42.93%     | ok               |
|          20 | -24.95%  | 17.80%             | -25.19% |    -1.19 |       79 | 40.43%     | ok               |
|          35 | -26.12%  | 17.80%             | -26.58% |    -1.36 |       70 | 34.11%     | ok               |

## XLY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -0.70%   | 26.59%             | -15.77% |     0.06 |       76 | 54.24%     | ok               |
|          30 | -4.15%   | 26.59%             | -18.35% |    -0.06 |       75 | 47.59%     | ok               |
|          20 | -5.95%   | 26.59%             | -19.25% |    -0.1  |       72 | 50.92%     | ok               |
|          25 | -8.05%   | 26.59%             | -19.98% |    -0.17 |       69 | 49.42%     | ok               |
|          50 | -6.34%   | 26.59%             | -15.82% |    -0.22 |       62 | 32.11%     | ok               |

## XOM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | 2.73%    | 45.07%             | -19.90% |     0.15 |       55 | 34.94%     | ok               |
|          50 | 1.92%    | 45.07%             | -21.35% |     0.13 |       38 | 27.12%     | ok               |
|          30 | 1.71%    | 45.07%             | -20.29% |     0.12 |       55 | 34.28%     | ok               |
|          20 | -3.12%   | 45.07%             | -25.56% |    -0.01 |       62 | 37.27%     | ok               |
|          45 | -3.17%   | 45.07%             | -23.33% |    -0.02 |       42 | 28.29%     | ok               |

## XRP-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 16.82%   | -44.34%            | -31.38% |     0.39 |       72 | 42.91%     | ok               |
|          40 | 1.26%    | -44.34%            | -33.91% |     0.21 |       64 | 36.59%     | ok               |
|          45 | -8.00%   | -44.34%            | -37.18% |     0.08 |       60 | 32.18%     | ok               |
|          30 | -12.68%  | -44.34%            | -31.82% |     0.05 |       67 | 47.89%     | ok               |
|          50 | -11.90%  | -44.34%            | -39.26% |     0.01 |       58 | 24.52%     | ok               |

## YFI-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -49.94%  | -64.14%            | -48.67% |    -0.88 |       54 | 27.39%     | ok               |
|          45 | -45.62%  | -64.14%            | -44.23% |    -0.95 |       68 | 22.22%     | ok               |
|          35 | -58.19%  | -64.14%            | -57.13% |    -1.08 |       64 | 33.91%     | ok               |
|          50 | -46.31%  | -64.14%            | -46.31% |    -1.08 |       50 | 16.67%     | ok               |
|          30 | -65.43%  | -64.14%            | -64.55% |    -1.29 |       77 | 37.55%     | ok               |

## ZEC-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 194.50%  | 2691.56%           | -30.64% |     1.06 |       46 | 32.76%     | ok               |
|          35 | 155.52%  | 2691.56%           | -50.84% |     0.94 |       52 | 38.31%     | ok               |
|          30 | 142.10%  | 2691.56%           | -56.50% |     0.9  |       57 | 41.76%     | ok               |
|          25 | 132.61%  | 2691.56%           | -58.07% |     0.87 |       55 | 44.25%     | ok               |
|          40 | 116.57%  | 2691.56%           | -54.22% |     0.84 |       54 | 36.21%     | ok               |
