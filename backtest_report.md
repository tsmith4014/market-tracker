# Market Tracker Backtest Report

_Generated: 2026-10-15T04:42:19+00:00_

## Data Sources

- Crypto: Kraken -> Coinbase -> CoinGecko OHLC -> CoinPaprika fallback chain.
- Stocks / ETFs / indices: Stooq -> Yahoo Finance fallback chain.
- Data rows are generated from real market APIs. Mock OHLCV rows are not generated.

## Data Freshness

- Rows: **92,740**
- Symbols: **161**
- Date range: **2024-05-22** to **2026-10-15**

## Latest Signals

| symbol     | date                |         close |   composite_score | signal   | data_source   |
|:-----------|:--------------------|--------------:|------------------:|:---------|:--------------|
| ABBV       | 2026-10-14 00:00:00 |   283.48      |        77.4167    | LONG     | Yahoo Finance |
| AMGN       | 2026-10-14 00:00:00 |   426.11      |        72.9167    | LONG     | Yahoo Finance |
| CL         | 2026-10-14 00:00:00 |    92.78      |        55.25      | LONG     | Yahoo Finance |
| COP        | 2026-10-14 00:00:00 |   142.34      |        71.25      | LONG     | Yahoo Finance |
| COST       | 2026-10-14 00:00:00 |   982         |        68         | LONG     | Yahoo Finance |
| CRM        | 2026-10-14 00:00:00 |   235.95      |        52.0833    | LONG     | Yahoo Finance |
| CSCO       | 2026-10-14 00:00:00 |   113.64      |        70.4167    | LONG     | Yahoo Finance |
| CVX        | 2026-10-14 00:00:00 |   222.04      |        55.25      | LONG     | Yahoo Finance |
| DIA        | 2026-10-14 00:00:00 |   515.63      |        33.4167    | LONG     | Yahoo Finance |
| DIS        | 2026-10-14 00:00:00 |   108.99      |        76.0833    | LONG     | Yahoo Finance |
| DXY-INDEX  | 2026-10-15 00:00:00 |   102.04      |        70.1613    | LONG     | Yahoo Finance |
| EOG        | 2026-10-14 00:00:00 |   154.19      |        71.25      | LONG     | Yahoo Finance |
| INTU       | 2026-10-14 00:00:00 |   310.44      |        37.5833    | LONG     | Yahoo Finance |
| LIN        | 2026-10-14 00:00:00 |   492.7       |        67.5       | LONG     | Yahoo Finance |
| LLY        | 2026-10-14 00:00:00 |  1208.74      |        72.9167    | LONG     | Yahoo Finance |
| META       | 2026-10-14 00:00:00 |   737.54      |        37.4167    | LONG     | Yahoo Finance |
| MPC        | 2026-10-14 00:00:00 |   484.92      |        73.75      | LONG     | Yahoo Finance |
| MSFT       | 2026-10-14 00:00:00 |   533.69      |        66.5833    | LONG     | Yahoo Finance |
| OXY        | 2026-10-14 00:00:00 |    61.41      |        74.0833    | LONG     | Yahoo Finance |
| PG         | 2026-10-14 00:00:00 |   156.53      |        77.75      | LONG     | Yahoo Finance |
| TMO        | 2026-10-14 00:00:00 |   673.2       |        38.9167    | LONG     | Yahoo Finance |
| TXN        | 2026-10-14 00:00:00 |   280.65      |        43.0833    | LONG     | Yahoo Finance |
| UNH        | 2026-10-14 00:00:00 |   395.62      |        67.9167    | LONG     | Yahoo Finance |
| XLE        | 2026-10-14 00:00:00 |    67.63      |        73.25      | LONG     | Yahoo Finance |
| XLP        | 2026-10-14 00:00:00 |    86.06      |        59         | LONG     | Yahoo Finance |
| AAPL       | 2026-10-14 00:00:00 |   342.96      |        59.8333    | NEUTRAL  | Yahoo Finance |
| AAVE-USD   | 2026-10-15 00:00:00 |   150.99      |        12.4167    | NEUTRAL  | Kraken API    |
| ADA-USD    | 2026-10-15 00:00:00 |     0.221954  |       -44.3333    | NEUTRAL  | Kraken API    |
| ADBE       | 2026-10-14 00:00:00 |   240.68      |         1.16667   | NEUTRAL  | Yahoo Finance |
| AGG        | 2026-10-14 00:00:00 |    94.82      |       -23.25      | NEUTRAL  | Yahoo Finance |
| ALGO-USD   | 2026-10-15 00:00:00 |     0.10995   |        19.4167    | NEUTRAL  | Kraken API    |
| AMAT       | 2026-10-14 00:00:00 |   446.63      |       -22.0833    | NEUTRAL  | Yahoo Finance |
| AMD        | 2026-10-14 00:00:00 |   570.82      |        15.9167    | NEUTRAL  | Yahoo Finance |
| AMZN       | 2026-10-14 00:00:00 |   254.08      |        22.6667    | NEUTRAL  | Yahoo Finance |
| APT-USD    | 2026-10-15 00:00:00 |     0.7721    |       -17.1667    | NEUTRAL  | Kraken API    |
| ARB-USD    | 2026-10-15 00:00:00 |     0.1755    |         3.08333   | NEUTRAL  | Kraken API    |
| ARKK       | 2026-10-14 00:00:00 |    84.48      |       -13.3333    | NEUTRAL  | Yahoo Finance |
| ATOM-USD   | 2026-10-15 00:00:00 |     1.6852    |       -44.3333    | NEUTRAL  | Kraken API    |
| AVAX-USD   | 2026-10-15 00:00:00 |     9.62      |         0.916667  | NEUTRAL  | Kraken API    |
| AVGO       | 2026-10-14 00:00:00 |   346.25      |       -46.6667    | NEUTRAL  | Yahoo Finance |
| BITO       | 2026-10-14 00:00:00 |    10.9       |       -11.0833    | NEUTRAL  | Yahoo Finance |
| BLK        | 2026-10-14 00:00:00 |  1073.79      |        25.75      | NEUTRAL  | Yahoo Finance |
| BND        | 2026-10-14 00:00:00 |    70.4       |       -23.25      | NEUTRAL  | Yahoo Finance |
| BTC-USD    | 2026-10-15 00:00:00 | 81026.3       |        -5.58333   | NEUTRAL  | Kraken API    |
| CAT        | 2026-10-14 00:00:00 |   748.98      |       -65         | NEUTRAL  | Yahoo Finance |
| COMP-USD   | 2026-10-15 00:00:00 |    21.89      |        -2.08333   | NEUTRAL  | Kraken API    |
| CRV-USD    | 2026-10-15 00:00:00 |     0.32728   |       -36.25      | NEUTRAL  | Kraken API    |
| DASH-USD   | 2026-10-15 00:00:00 |    46.939     |       -25.1667    | NEUTRAL  | Kraken API    |
| DBC        | 2026-10-14 00:00:00 |    33.31      |        59.3333    | NEUTRAL  | Yahoo Finance |
| DE         | 2026-10-14 00:00:00 |   650.38      |       -24.8333    | NEUTRAL  | Yahoo Finance |
| DOT-USD    | 2026-10-15 00:00:00 |     1.1014    |       -30.0833    | NEUTRAL  | Kraken API    |
| EEM        | 2026-10-14 00:00:00 |    64.39      |       -41.25      | NEUTRAL  | Yahoo Finance |
| EFA        | 2026-10-14 00:00:00 |   102.75      |       -23         | NEUTRAL  | Yahoo Finance |
| ETH-USD    | 2026-10-15 00:00:00 |  2368.78      |       -23.6667    | NEUTRAL  | Kraken API    |
| EWJ        | 2026-10-14 00:00:00 |    95.84      |         0.833333  | NEUTRAL  | Yahoo Finance |
| FCX        | 2026-10-14 00:00:00 |    69.62      |       -38.6667    | NEUTRAL  | Yahoo Finance |
| FET-USD    | 2026-10-15 00:00:00 |     0.1953    |       -45.8333    | NEUTRAL  | Kraken API    |
| FIL-USD    | 2026-10-15 00:00:00 |     1.045     |        13.3333    | NEUTRAL  | Kraken API    |
| FXI        | 2026-10-14 00:00:00 |    33.86      |       -35.5       | NEUTRAL  | Yahoo Finance |
| GE         | 2026-10-14 00:00:00 |   307.02      |       -47.8333    | NEUTRAL  | Yahoo Finance |
| GOOGL      | 2026-10-14 00:00:00 |   347.64      |        49.9167    | NEUTRAL  | Yahoo Finance |
| GRT-USD    | 2026-10-15 00:00:00 |     0.02403   |       -15.4167    | NEUTRAL  | Kraken API    |
| HD         | 2026-10-14 00:00:00 |   295.51      |         6.41667   | NEUTRAL  | Yahoo Finance |
| IBIT       | 2026-10-14 00:00:00 |    46.24      |        15.9167    | NEUTRAL  | Yahoo Finance |
| IBM        | 2026-10-14 00:00:00 |   227.88      |        -8.83333   | NEUTRAL  | Yahoo Finance |
| ICP-USD    | 2026-10-15 00:00:00 |     2.917     |       -17.3333    | NEUTRAL  | Kraken API    |
| IEF        | 2026-10-14 00:00:00 |    89.71      |       -16.5833    | NEUTRAL  | Yahoo Finance |
| IEMG       | 2026-10-14 00:00:00 |    78.64      |       -41.25      | NEUTRAL  | Yahoo Finance |
| INJ-USD    | 2026-10-15 00:00:00 |     7.399     |        13.25      | NEUTRAL  | Kraken API    |
| INTC       | 2026-10-14 00:00:00 |    98.12      |       -12.3333    | NEUTRAL  | Yahoo Finance |
| ITA        | 2026-10-14 00:00:00 |   204.24      |       -29.25      | NEUTRAL  | Yahoo Finance |
| JNJ        | 2026-10-14 00:00:00 |   253.91      |       -35.75      | NEUTRAL  | Yahoo Finance |
| JPM        | 2026-10-14 00:00:00 |   335.28      |        13.75      | NEUTRAL  | Yahoo Finance |
| KO         | 2026-10-14 00:00:00 |    91.78      |        65.3333    | NEUTRAL  | Yahoo Finance |
| LINK-USD   | 2026-10-15 00:00:00 |    12.1353    |       -22.5833    | NEUTRAL  | Kraken API    |
| LRCX       | 2026-10-14 00:00:00 |   286.92      |       -22.0833    | NEUTRAL  | Yahoo Finance |
| LTC-USD    | 2026-10-15 00:00:00 |    58.27      |       -13.5833    | NEUTRAL  | Kraken API    |
| MCD        | 2026-10-14 00:00:00 |   238.31      |       -18.5833    | NEUTRAL  | Yahoo Finance |
| MRK        | 2026-10-14 00:00:00 |   147.37      |        18.5       | NEUTRAL  | Yahoo Finance |
| MU         | 2026-10-14 00:00:00 |   914.13      |       -12.0833    | NEUTRAL  | Yahoo Finance |
| NEAR-USD   | 2026-10-15 00:00:00 |     4.67      |         2.41667   | NEUTRAL  | Kraken API    |
| NFLX       | 2026-10-14 00:00:00 |    70.57      |       -15.25      | NEUTRAL  | Yahoo Finance |
| NOW        | 2026-10-14 00:00:00 |   139.98      |        60.8333    | NEUTRAL  | Yahoo Finance |
| NVDA       | 2026-10-14 00:00:00 |   221.3       |        -7.75      | NEUTRAL  | Yahoo Finance |
| OP-USD     | 2026-10-15 00:00:00 |     0.1343    |         2.25      | NEUTRAL  | Kraken API    |
| ORCL       | 2026-10-14 00:00:00 |   130.55      |       -54.75      | NEUTRAL  | Yahoo Finance |
| PEP        | 2026-10-14 00:00:00 |   129.27      |         6.91667   | NEUTRAL  | Yahoo Finance |
| PEPE-USD   | 2026-10-15 00:00:00 |     3.942e-06 |        -2.16667   | NEUTRAL  | Kraken API    |
| PFE        | 2026-10-14 00:00:00 |    29.21      |        63.6667    | NEUTRAL  | Yahoo Finance |
| PM         | 2026-10-14 00:00:00 |   205.58      |        64.5       | NEUTRAL  | Yahoo Finance |
| POL-USD    | 2026-10-15 00:00:00 |     0.09341   |       -55.8333    | NEUTRAL  | Kraken API    |
| QCOM       | 2026-10-14 00:00:00 |   172.62      |       -49.8333    | NEUTRAL  | Yahoo Finance |
| QQQ        | 2026-10-14 00:00:00 |   728.95      |        17.9167    | NEUTRAL  | Yahoo Finance |
| RENDER-USD | 2026-10-15 00:00:00 |     1.857     |         4.91667   | NEUTRAL  | Kraken API    |
| RTX        | 2026-10-14 00:00:00 |   186.47      |       -28.75      | NEUTRAL  | Yahoo Finance |
| SCHW       | 2026-10-14 00:00:00 |    96.8       |        -9.25      | NEUTRAL  | Yahoo Finance |
| SHY        | 2026-10-14 00:00:00 |    81.17      |       -22.5833    | NEUTRAL  | Yahoo Finance |
| SKY-USD    | 2026-10-15 00:00:00 |     0.06919   |       -25.5833    | NEUTRAL  | Kraken API    |
| SMH        | 2026-10-14 00:00:00 |   564.74      |        -3.83333   | NEUTRAL  | Yahoo Finance |
| SOXX       | 2026-10-14 00:00:00 |   519.42      |        -0.0833333 | NEUTRAL  | Yahoo Finance |
| SPY        | 2026-10-14 00:00:00 |   769.6       |        35.5       | NEUTRAL  | Yahoo Finance |
| TGT        | 2026-10-14 00:00:00 |   155.31      |        16.6667    | NEUTRAL  | Yahoo Finance |
| TIA-USD    | 2026-10-15 00:00:00 |     0.5323    |        66.8333    | NEUTRAL  | Kraken API    |
| TLT        | 2026-10-14 00:00:00 |    78.89      |       -16.25      | NEUTRAL  | Yahoo Finance |
| TRX-USD    | 2026-10-15 00:00:00 |     0.330738  |       -42.5833    | NEUTRAL  | Kraken API    |
| TSLA       | 2026-10-14 00:00:00 |   367.16      |       -40.3333    | NEUTRAL  | Yahoo Finance |
| UNI-USD    | 2026-10-15 00:00:00 |     6.9637    |       -24.9167    | NEUTRAL  | Kraken API    |
| UPS        | 2026-10-14 00:00:00 |    95.78      |         6.41667   | NEUTRAL  | Yahoo Finance |
| USO        | 2026-10-14 00:00:00 |   153.56      |        44.5       | NEUTRAL  | Yahoo Finance |
| VEA        | 2026-10-14 00:00:00 |    69.3       |       -28.3333    | NEUTRAL  | Yahoo Finance |
| VIXY       | 2026-10-14 00:00:00 |    16.53      |       -30.5833    | NEUTRAL  | Yahoo Finance |
| VTI        | 2026-10-14 00:00:00 |   376.88      |        25.3333    | NEUTRAL  | Yahoo Finance |
| VWO        | 2026-10-14 00:00:00 |    58.9       |       -39.6667    | NEUTRAL  | Yahoo Finance |
| WFC        | 2026-10-14 00:00:00 |    80.9       |       -26         | NEUTRAL  | Yahoo Finance |
| WMT        | 2026-10-14 00:00:00 |   116.16      |        56.75      | NEUTRAL  | Yahoo Finance |
| XBI        | 2026-10-14 00:00:00 |   146.77      |       -24.75      | NEUTRAL  | Yahoo Finance |
| XLB        | 2026-10-14 00:00:00 |    49.67      |       -20         | NEUTRAL  | Yahoo Finance |
| XLC        | 2026-10-14 00:00:00 |   110.82      |       -63.8333    | NEUTRAL  | Yahoo Finance |
| XLF        | 2026-10-14 00:00:00 |    54.52      |        17.25      | NEUTRAL  | Yahoo Finance |
| XLI        | 2026-10-14 00:00:00 |   167.04      |       -42.6667    | NEUTRAL  | Yahoo Finance |
| XLK        | 2026-10-14 00:00:00 |   190.43      |        -1.83333   | NEUTRAL  | Yahoo Finance |
| XLU        | 2026-10-14 00:00:00 |    41.72      |         3.08333   | NEUTRAL  | Yahoo Finance |
| XLV        | 2026-10-14 00:00:00 |   173.96      |        65.6667    | NEUTRAL  | Yahoo Finance |
| XLY        | 2026-10-14 00:00:00 |   111.5       |       -23.3333    | NEUTRAL  | Yahoo Finance |
| XOM        | 2026-10-14 00:00:00 |   177.01      |        44         | NEUTRAL  | Yahoo Finance |
| ZEC-USD    | 2026-10-15 00:00:00 |  1106.4       |       -21.5833    | NEUTRAL  | Kraken API    |
| BA         | 2026-10-14 00:00:00 |   184.66      |       -35.4167    | SHORT    | Yahoo Finance |
| BAC        | 2026-10-14 00:00:00 |    51.39      |       -35.8333    | SHORT    | Yahoo Finance |
| BCH-USD    | 2026-10-15 00:00:00 |   263.76      |       -38.9167    | SHORT    | Kraken API    |
| BONK-USD   | 2026-10-15 00:00:00 |     3e-06     |       -41.75      | SHORT    | Kraken API    |
| C          | 2026-10-14 00:00:00 |   122.27      |       -52.3333    | SHORT    | Yahoo Finance |
| CMCSA      | 2026-10-14 00:00:00 |    21.05      |       -31.25      | SHORT    | Yahoo Finance |
| DOGE-USD   | 2026-10-15 00:00:00 |     0.080382  |       -51.3333    | SHORT    | Kraken API    |
| ETC-USD    | 2026-10-15 00:00:00 |     7.719     |       -46.4167    | SHORT    | Kraken API    |
| GDX        | 2026-10-14 00:00:00 |    83.4       |       -58.3333    | SHORT    | Yahoo Finance |
| GDXJ       | 2026-10-14 00:00:00 |   104.75      |       -63.3333    | SHORT    | Yahoo Finance |
| GLD        | 2026-10-14 00:00:00 |   375.99      |       -51.25      | SHORT    | Yahoo Finance |
| GS         | 2026-10-14 00:00:00 |   878.72      |       -34.9167    | SHORT    | Yahoo Finance |
| HBAR-USD   | 2026-10-15 00:00:00 |     0.08195   |       -44.8333    | SHORT    | Kraken API    |
| HON        | 2026-10-14 00:00:00 |   207.61      |       -42.4167    | SHORT    | Yahoo Finance |
| HYG        | 2026-10-14 00:00:00 |    76.81      |       -39.25      | SHORT    | Yahoo Finance |
| IWM        | 2026-10-14 00:00:00 |   271.37      |       -46.3333    | SHORT    | Yahoo Finance |
| LDO-USD    | 2026-10-15 00:00:00 |     0.382     |       -41.75      | SHORT    | Kraken API    |
| MS         | 2026-10-14 00:00:00 |   181.51      |       -53.8333    | SHORT    | Yahoo Finance |
| NEM        | 2026-10-14 00:00:00 |   111.56      |       -35.3333    | SHORT    | Yahoo Finance |
| NKE        | 2026-10-14 00:00:00 |    35.3       |       -31.5       | SHORT    | Yahoo Finance |
| SBUX       | 2026-10-14 00:00:00 |    93.25      |       -30.75      | SHORT    | Yahoo Finance |
| SHIB-USD   | 2026-10-15 00:00:00 |     4.973e-06 |       -47.5833    | SHORT    | Kraken API    |
| SLB        | 2026-10-14 00:00:00 |    48.51      |       -48.25      | SHORT    | Yahoo Finance |
| SLV        | 2026-10-14 00:00:00 |    50.22      |       -63.3333    | SHORT    | Yahoo Finance |
| SNX-USD    | 2026-10-15 00:00:00 |     0.2175    |       -41.0833    | SHORT    | Kraken API    |
| SOL-USD    | 2026-10-15 00:00:00 |   102.96      |       -20.5833    | SHORT    | Kraken API    |
| SUSHI-USD  | 2026-10-15 00:00:00 |     0.2186    |       -50.0833    | SHORT    | Kraken API    |
| T          | 2026-10-14 00:00:00 |    23.05      |       -53.6667    | SHORT    | Yahoo Finance |
| TMUS       | 2026-10-14 00:00:00 |   157.79      |       -45.75      | SHORT    | Yahoo Finance |
| VNQ        | 2026-10-14 00:00:00 |    90.35      |       -31.75      | SHORT    | Yahoo Finance |
| VZ         | 2026-10-14 00:00:00 |    44.42      |       -44.8333    | SHORT    | Yahoo Finance |
| WIF-USD    | 2026-10-15 00:00:00 |     0.1942    |       -54.0833    | SHORT    | Kraken API    |
| XLM-USD    | 2026-10-15 00:00:00 |     0.18      |       -44.3333    | SHORT    | Kraken API    |
| XRP-USD    | 2026-10-15 00:00:00 |     1.31017   |       -45.5833    | SHORT    | Kraken API    |
| YFI-USD    | 2026-10-15 00:00:00 |  2204.9       |       -35.25      | SHORT    | Kraken API    |

## Edge Summary

- Symbols with trades: **161** of 161
- Beat buy-and-hold: **33.54%** of traded symbols
- Positive return: **29.81%** of traded symbols
- Median strategy return: **-10.04%** (benchmark **15.52%**)
- Median excess vs benchmark: **-23.55%**
- Median Sharpe: **-0.10**
- Median exposure: **44.26%**

> Edge is real only if both _beat buy-and-hold_ and _median excess_ are convincingly positive across many symbols. Treat a single high-return symbol as noise.

## Portfolio Backtest

Actual capital-allocation books (not per-symbol averages). Benchmarks: `equal_weight_buyhold` (whole tracked universe), `spy_buyhold` (100% SPY), and `sixty_forty` (60% SPY / 40% AGG). `high_conf_voltarget` inverse-vol-weights the HIGH-confidence book; `conviction_long_short` is market-neutral. Judge on **Sharpe** and **max_drawdown** out-of-sample, not raw return: a fully-invested long book wins on return in a bull market but carries all the risk.

| strategy              | scope         | ann_return   | ann_vol   |   sharpe | max_drawdown   | total_return   |   avg_gross_exposure |
|:----------------------|:--------------|:-------------|:----------|---------:|:---------------|:---------------|---------------------:|
| equal_weight_buyhold  | full          | 10.27%       | 28.54%    |     0.36 | -39.53%        | 20.71%         |                 1    |
| equal_weight_buyhold  | out_of_sample | 13.65%       | 27.73%    |     0.49 | -19.75%        | 11.01%         |                 1    |
| all_signals_ew        | full          | -15.87%      | 24.37%    |    -0.65 | -57.16%        | -43.60%        |                 1    |
| all_signals_ew        | out_of_sample | 5.83%        | 23.59%    |     0.25 | -23.10%        | 3.31%          |                 1    |
| high_conf_ew          | full          | -4.79%       | 31.64%    |    -0.15 | -45.09%        | -25.60%        |                 0.9  |
| high_conf_ew          | out_of_sample | 10.46%       | 28.75%    |     0.36 | -22.85%        | 6.89%          |                 0.9  |
| high_conf_voltarget   | full          | -5.64%       | 28.41%    |    -0.2  | -39.85%        | -25.30%        |                 0.9  |
| high_conf_voltarget   | out_of_sample | 0.88%        | 23.99%    |     0.04 | -17.42%        | -2.18%         |                 0.9  |
| conviction_long_short | full          | -14.22%      | 22.25%    |    -0.64 | -47.05%        | -39.84%        |                 0.97 |
| conviction_long_short | out_of_sample | -1.16%       | 19.63%    |    -0.06 | -26.60%        | -3.23%         |                 0.97 |
| spy_buyhold           | full          | 5.39%        | 13.66%    |     0.39 | -19.00%        | 14.53%         |                 0.79 |
| spy_buyhold           | out_of_sample | 0.39%        | 9.93%     |     0.04 | -12.06%        | -0.11%         |                 0.79 |
| sixty_forty           | full          | 2.80%        | 8.61%     |     0.32 | -11.66%        | 7.65%          |                 0.79 |
| sixty_forty           | out_of_sample | -2.02%       | 6.67%     |    -0.3  | -8.26%         | -2.36%         |                 0.79 |

## Walk-Forward Robustness

Each book measured across contiguous time folds (each a different regime). A book has durable edge only if `mean_sharpe` is positive, `min_sharpe` isn't deeply negative, and `pct_positive_folds` is high — a single great fold doesn't count. `fold_sharpes` lists each fold oldest-to-newest.

| strategy              |   n_folds |   mean_sharpe |   median_sharpe |   min_sharpe | pct_positive_folds   | mean_return   | fold_sharpes                 |
|:----------------------|----------:|--------------:|----------------:|-------------:|:---------------------|:--------------|:-----------------------------|
| equal_weight_buyhold  |         5 |          0.51 |            0.72 |        -0.44 | 60.00%               | 4.85%         | 0.72;1.46;-0.44;-0.27;1.07   |
| all_signals_ew        |         5 |         -0.68 |           -0.85 |        -2.06 | 20.00%               | -9.08%        | -1.33;-0.85;-2.06;1.24;-0.42 |
| high_conf_ew          |         5 |         -0.03 |           -0.02 |        -1.04 | 40.00%               | -4.36%        | 0.09;-0.41;-1.04;1.22;-0.02  |
| high_conf_voltarget   |         5 |         -0.07 |           -0.18 |        -0.93 | 40.00%               | -4.88%        | 0.26;-0.24;-0.93;0.74;-0.18  |
| conviction_long_short |         5 |         -0.6  |           -0.64 |        -1.74 | 20.00%               | -9.27%        | -1.74;-0.06;-0.95;-0.64;0.38 |
| spy_buyhold           |         5 |          0.35 |            0.34 |        -0.36 | 60.00%               | 2.84%         | 1.31;0.34;-0.08;0.55;-0.36   |
| sixty_forty           |         5 |          0.26 |            0.18 |        -0.64 | 80.00%               | 1.53%         | 1.25;0.39;0.13;0.18;-0.64    |

## Strategy Comparison

Each decision rule backtested over the same data. `out_of_sample` is the most recent ~35% of each symbol's history (unseen tail). A rule has real edge only if `median_excess` and `beat_benchmark_pct` stay positive out-of-sample, not just full-sample.

| strategy        | scope         |   symbols | beat_benchmark_pct   | positive_pct   | median_return   | median_benchmark   | median_excess   |   median_sharpe |   total_trades |
|:----------------|:--------------|----------:|:---------------------|:---------------|:----------------|:-------------------|:----------------|----------------:|---------------:|
| trend           | full          |       161 | 33.54%               | 29.81%         | -10.04%         | 15.52%             | -23.55%         |           -0.1  |          11326 |
| trend           | out_of_sample |       161 | 30.43%               | 50.31%         | 0.03%           | 5.26%              | -10.61%         |            0.08 |           3818 |
| mean_reversion  | full          |       157 | 40.13%               | 49.68%         | -0.02%          | 13.95%             | -14.33%         |            0.01 |           1220 |
| mean_reversion  | out_of_sample |       120 | 41.67%               | 53.33%         | 0.30%           | 2.70%              | -4.06%          |            0.16 |            488 |
| regime_adaptive | full          |       161 | 34.78%               | 31.06%         | -10.44%         | 15.52%             | -23.55%         |           -0.13 |          11594 |
| regime_adaptive | out_of_sample |       161 | 31.06%               | 49.69%         | -0.09%          | 5.26%              | -12.58%         |            0.07 |           3930 |

## Signal Calibration

Realized forward return in the signal's direction, grouped by confidence. HIGH should outrank LOW for the confidence score to be meaningful.

| confidence_level   |   horizon |     n | mean_return   | median_return   | win_rate   |
|:-------------------|----------:|------:|:--------------|:----------------|:-----------|
| HIGH               |         5 |  7913 | 0.19%         | 0.04%           | 50.83%     |
| MEDIUM             |         5 | 29178 | 0.04%         | 0.03%           | 50.29%     |
| LOW                |         5 |  3509 | -0.41%        | -0.41%          | 46.00%     |
| ALL                |         5 | 40600 | 0.03%         | 0.01%           | 50.02%     |
| HIGH               |        10 |  7885 | 0.44%         | 0.08%           | 50.96%     |
| MEDIUM             |        10 | 28914 | 0.17%         | 0.06%           | 50.46%     |
| LOW                |        10 |  3448 | -0.74%        | -0.51%          | 46.64%     |
| ALL                |        10 | 40247 | 0.15%         | 0.03%           | 50.23%     |
| HIGH               |        20 |  7750 | 1.04%         | 0.31%           | 52.46%     |
| MEDIUM             |        20 | 28299 | 0.90%         | 0.57%           | 53.21%     |
| LOW                |        20 |  3382 | -0.47%        | -0.58%          | 47.19%     |
| ALL                |        20 | 39431 | 0.81%         | 0.44%           | 52.55%     |

## Backtest Summary

### Data Quality / Signal Availability

- **ok**: 161 symbols

| symbol     |   trades | return   | benchmark_return   | mdd     |   sharpe | exposure   | skipped_reason   |
|:-----------|---------:|:---------|:-------------------|:--------|---------:|:-----------|:-----------------|
| AAPL       |       63 | 6.97%    | 79.65%             | -20.65% |     0.24 | 50.75%     | ok               |
| AAVE-USD   |       67 | -38.36%  | -31.87%            | -68.26% |    -0.23 | 42.34%     | ok               |
| ABBV       |       70 | -21.98%  | 77.61%             | -30.52% |    -0.46 | 48.09%     | ok               |
| ADA-USD    |       76 | -36.14%  | -72.85%            | -52.70% |    -0.27 | 45.98%     | ok               |
| ADBE       |       71 | -11.61%  | -50.27%            | -31.20% |    -0.03 | 56.91%     | ok               |
| AGG        |       65 | -6.82%   | -1.98%             | -11.01% |    -1.08 | 33.44%     | ok               |
| ALGO-USD   |       76 | -24.13%  | -54.67%            | -38.19% |    -0.1  | 40.04%     | ok               |
| AMAT       |       71 | -37.73%  | 104.74%            | -53.91% |    -0.36 | 51.58%     | ok               |
| AMD        |       56 | 17.34%   | 244.86%            | -41.09% |     0.37 | 37.27%     | ok               |
| AMGN       |       67 | -14.85%  | 37.72%             | -34.19% |    -0.26 | 50.92%     | ok               |
| AMZN       |       80 | -55.73%  | 38.74%             | -56.19% |    -1.6  | 41.26%     | ok               |
| APT-USD    |       70 | -23.20%  | -86.80%            | -56.73% |    -0    | 39.66%     | ok               |
| ARB-USD    |       75 | -4.93%   | -59.18%            | -48.19% |     0.23 | 43.10%     | ok               |
| ARKK       |       85 | -27.19%  | 87.78%             | -31.44% |    -0.39 | 43.43%     | ok               |
| ATOM-USD   |       92 | -58.27%  | -67.79%            | -58.27% |    -0.81 | 48.28%     | ok               |
| AVAX-USD   |       68 | -31.87%  | -61.26%            | -45.41% |    -0.24 | 40.04%     | ok               |
| AVGO       |       64 | 17.60%   | 148.70%            | -36.09% |     0.37 | 41.60%     | ok               |
| BA         |       69 | 5.73%    | -0.87%             | -24.47% |     0.22 | 51.08%     | ok               |
| BAC        |       72 | -11.08%  | 29.25%             | -25.66% |    -0.25 | 48.59%     | ok               |
| BCH-USD    |       76 | 6.56%    | -35.76%            | -53.87% |     0.28 | 48.85%     | ok               |
| BITO       |       78 | -19.94%  | -61.44%            | -39.47% |    -0.1  | 41.60%     | ok               |
| BLK        |       85 | -14.58%  | 34.29%             | -26.90% |    -0.35 | 47.09%     | ok               |
| BND        |       67 | -6.86%   | -1.95%             | -10.91% |    -1.05 | 35.61%     | ok               |
| BONK-USD   |       74 | 4.70%    | -86.82%            | -51.50% |     0.33 | 45.79%     | ok               |
| BTC-USD    |       72 | 3.70%    | -21.20%            | -23.38% |     0.2  | 52.11%     | ok               |
| C          |       79 | -33.75%  | 91.59%             | -39.51% |    -0.72 | 46.09%     | ok               |
| CAT        |       70 | 4.67%    | 110.42%            | -21.87% |     0.2  | 48.09%     | ok               |
| CL         |       66 | -2.83%   | -2.09%             | -14.32% |    -0.03 | 38.60%     | ok               |
| CMCSA      |       84 | -35.26%  | -42.25%            | -46.39% |    -0.84 | 43.43%     | ok               |
| COMP-USD   |       95 | -32.76%  | -53.42%            | -52.27% |    -0.13 | 50.38%     | ok               |
| COP        |       70 | -14.37%  | 20.43%             | -43.40% |    -0.18 | 44.26%     | ok               |
| COST       |       60 | -0.14%   | 22.47%             | -31.32% |     0.06 | 41.10%     | ok               |
| CRM        |       67 | -32.66%  | -16.87%            | -44.41% |    -0.47 | 46.42%     | ok               |
| CRV-USD    |       66 | 30.99%   | -56.55%            | -39.89% |     0.5  | 36.97%     | ok               |
| CSCO       |       64 | 15.50%   | 139.60%            | -21.79% |     0.38 | 49.42%     | ok               |
| CVX        |       71 | -13.64%  | 40.92%             | -27.78% |    -0.3  | 41.76%     | ok               |
| DASH-USD   |       53 | 2.17%    | 88.91%             | -64.43% |     0.4  | 30.46%     | ok               |
| DBC        |       66 | -8.16%   | 41.87%             | -24.10% |    -0.21 | 35.27%     | ok               |
| DE         |       70 | -12.17%  | 68.49%             | -23.98% |    -0.18 | 44.26%     | ok               |
| DIA        |       66 | -7.42%   | 29.99%             | -12.94% |    -0.38 | 43.59%     | ok               |
| DIS        |       62 | -7.26%   | 5.79%              | -28.17% |    -0.08 | 43.26%     | ok               |
| DOGE-USD   |       69 | -25.79%  | -65.20%            | -60.95% |    -0.07 | 48.85%     | ok               |
| DOT-USD    |       86 | -51.45%  | -78.28%            | -63.33% |    -0.42 | 48.28%     | ok               |
| DXY-INDEX  |       40 | -0.78%   | -4.64%             | -6.02%  |    -0.11 | 32.25%     | ok               |
| EEM        |       62 | -12.03%  | 48.98%             | -24.04% |    -0.34 | 39.93%     | ok               |
| EFA        |       66 | -10.81%  | 27.17%             | -12.96% |    -0.42 | 41.26%     | ok               |
| EOG        |       80 | -29.94%  | 22.32%             | -47.87% |    -0.64 | 44.93%     | ok               |
| ETC-USD    |       60 | -22.18%  | -60.93%            | -47.84% |    -0.19 | 31.42%     | ok               |
| ETH-USD    |       58 | 146.84%  | -5.07%             | -30.11% |     1.32 | 48.08%     | ok               |
| EWJ        |       62 | -22.99%  | 40.90%             | -29.40% |    -0.8  | 36.44%     | ok               |
| FCX        |       65 | -29.37%  | 35.90%             | -46.84% |    -0.32 | 44.26%     | ok               |
| FET-USD    |       83 | -52.60%  | -76.50%            | -65.38% |    -0.39 | 42.72%     | ok               |
| FIL-USD    |       65 | -40.15%  | -66.73%            | -58.54% |    -0.34 | 37.16%     | ok               |
| FXI        |       50 | -7.21%   | 20.07%             | -24.33% |    -0.1  | 31.11%     | ok               |
| GDX        |       62 | 6.09%    | 135.26%            | -33.31% |     0.23 | 44.59%     | ok               |
| GDXJ       |       72 | -31.95%  | 133.92%            | -40.39% |    -0.38 | 43.09%     | ok               |
| GE         |       76 | -8.43%   | 90.92%             | -27.82% |    -0.04 | 48.09%     | ok               |
| GLD        |       50 | 12.96%   | 70.82%             | -13.87% |     0.38 | 45.76%     | ok               |
| GOOGL      |       57 | 56.30%   | 97.10%             | -17.54% |     1    | 47.42%     | ok               |
| GRT-USD    |       77 | 68.95%   | -79.72%            | -33.74% |     0.76 | 45.79%     | ok               |
| GS         |       70 | -2.81%   | 90.04%             | -21.94% |     0.04 | 48.09%     | ok               |
| HBAR-USD   |       40 | -40.92%  | -20.54%            | -56.47% |    -0.86 | 37.88%     | ok               |
| HD         |       67 | 1.72%    | -10.61%            | -17.15% |     0.13 | 43.59%     | ok               |
| HON        |       93 | -27.02%  | 3.57%              | -33.87% |    -0.67 | 55.07%     | ok               |
| HYG        |       85 | -6.36%   | -0.36%             | -10.59% |    -0.7  | 39.10%     | ok               |
| IBIT       |       40 | 36.55%   | 21.65%             | -18.95% |     0.67 | 35.09%     | ok               |
| IBM        |       69 | -26.33%  | 31.20%             | -48.94% |    -0.32 | 49.25%     | ok               |
| ICP-USD    |       79 | -17.76%  | -49.32%            | -46.42% |     0.09 | 39.46%     | ok               |
| IEF        |       78 | -10.64%  | -3.63%             | -13.49% |    -1.45 | 33.94%     | ok               |
| IEMG       |       60 | -9.41%   | 44.96%             | -25.58% |    -0.27 | 39.93%     | ok               |
| INJ-USD    |       65 | -28.38%  | -46.20%            | -68.18% |    -0.04 | 40.42%     | ok               |
| INTC       |       68 | 40.26%   | 212.29%            | -60.60% |     0.53 | 48.09%     | ok               |
| INTU       |       71 | -11.33%  | -53.68%            | -37.41% |    -0.05 | 46.59%     | ok               |
| ITA        |       78 | -4.11%   | 49.46%             | -23.75% |    -0.04 | 48.59%     | ok               |
| IWM        |       54 | 7.82%    | 31.36%             | -10.95% |     0.34 | 34.11%     | ok               |
| JNJ        |       60 | 7.29%    | 65.41%             | -16.86% |     0.31 | 46.76%     | ok               |
| JPM        |       73 | -22.39%  | 69.07%             | -32.74% |    -0.62 | 44.93%     | ok               |
| KO         |       54 | 23.22%   | 45.68%             | -8.64%  |     0.83 | 36.77%     | ok               |
| LDO-USD    |       68 | 49.35%   | -64.53%            | -50.81% |     0.62 | 46.55%     | ok               |
| LIN        |       74 | -10.90%  | 13.32%             | -20.61% |    -0.34 | 38.60%     | ok               |
| LINK-USD   |       68 | 46.50%   | -27.57%            | -33.64% |     0.63 | 45.40%     | ok               |
| LLY        |       80 | -35.35%  | 50.54%             | -53.42% |    -0.59 | 49.25%     | ok               |
| LRCX       |       80 | -27.50%  | 197.09%            | -58.92% |    -0.19 | 42.76%     | ok               |
| LTC-USD    |       68 | -2.49%   | -43.89%            | -32.83% |     0.17 | 52.87%     | ok               |
| MCD        |       77 | -0.16%   | -10.33%            | -21.88% |     0.05 | 40.60%     | ok               |
| META       |       74 | -25.43%  | 57.67%             | -44.52% |    -0.34 | 50.25%     | ok               |
| MPC        |       70 | 22.17%   | 175.49%            | -34.29% |     0.46 | 51.91%     | ok               |
| MRK        |       65 | -23.45%  | 12.41%             | -35.95% |    -0.45 | 42.43%     | ok               |
| MS         |       75 | -6.43%   | 80.18%             | -27.79% |    -0.07 | 48.25%     | ok               |
| MSFT       |       83 | -26.34%  | 23.96%             | -39.15% |    -0.57 | 51.41%     | ok               |
| MU         |       51 | 142.59%  | 623.89%            | -68.76% |     1.01 | 52.58%     | ok               |
| NEAR-USD   |       71 | 158.95%  | 46.58%             | -46.60% |     1.07 | 44.25%     | ok               |
| NEM        |       70 | -22.66%  | 163.18%            | -39.56% |    -0.19 | 50.08%     | ok               |
| NFLX       |       78 | 4.95%    | 10.18%             | -21.09% |     0.2  | 52.91%     | ok               |
| NKE        |       79 | -26.45%  | -61.84%            | -55.35% |    -0.28 | 46.92%     | ok               |
| NOW        |       80 | 11.00%   | -9.20%             | -30.43% |     0.3  | 50.25%     | ok               |
| NVDA       |       77 | -50.12%  | 79.13%             | -53.39% |    -0.72 | 55.61%     | ok               |
| OP-USD     |       70 | -43.71%  | -83.71%            | -60.45% |    -0.37 | 32.76%     | ok               |
| ORCL       |       62 | 85.54%   | 4.78%              | -30.61% |     0.8  | 52.08%     | ok               |
| OXY        |       73 | 2.59%    | -1.99%             | -28.48% |     0.17 | 42.76%     | ok               |
| PEP        |       76 | -2.09%   | -29.01%            | -21.35% |     0.01 | 45.76%     | ok               |
| PEPE-USD   |       83 | -53.92%  | -71.06%            | -61.29% |    -0.4  | 48.28%     | ok               |
| PFE        |       81 | -36.54%  | -1.32%             | -41.77% |    -1.16 | 36.61%     | ok               |
| PG         |       64 | -23.91%  | -6.72%             | -24.16% |    -0.97 | 34.44%     | ok               |
| PM         |       79 | -8.51%   | 103.40%            | -35.15% |    -0.1  | 50.08%     | ok               |
| POL-USD    |       77 | 52.93%   | -63.39%            | -38.69% |     0.68 | 49.62%     | ok               |
| QCOM       |       77 | -28.49%  | -14.94%            | -56.59% |    -0.23 | 43.43%     | ok               |
| QQQ        |       66 | 6.13%    | 59.96%             | -14.20% |     0.24 | 46.09%     | ok               |
| RENDER-USD |       90 | -28.15%  | -64.09%            | -45.92% |    -0.04 | 47.32%     | ok               |
| RTX        |       66 | 26.93%   | 75.40%             | -16.99% |     0.63 | 52.08%     | ok               |
| SBUX       |       60 | -10.86%  | 15.52%             | -29.22% |    -0.15 | 38.44%     | ok               |
| SCHW       |       80 | -17.20%  | 28.60%             | -31.92% |    -0.38 | 46.09%     | ok               |
| SHIB-USD   |       81 | -28.25%  | -68.47%            | -45.33% |    -0.2  | 52.49%     | ok               |
| SHY        |       48 | -1.75%   | -0.26%             | -3.18%  |    -0.58 | 37.10%     | ok               |
| SKY-USD    |       89 | -62.61%  | -7.75%             | -64.59% |    -1.04 | 44.06%     | ok               |
| SLB        |       73 | -38.66%  | 4.37%              | -58.50% |    -0.74 | 48.92%     | ok               |
| SLV        |       68 | 15.34%   | 77.96%             | -42.60% |     0.36 | 40.10%     | ok               |
| SMH        |       48 | 46.91%   | 138.70%            | -34.29% |     0.77 | 43.93%     | ok               |
| SNX-USD    |       64 | -5.62%   | -75.31%            | -50.74% |     0.15 | 33.72%     | ok               |
| SOL-USD    |       70 | -16.70%  | -40.90%            | -44.99% |     0.04 | 60.15%     | ok               |
| SOXX       |       54 | 58.34%   | 120.80%            | -39.81% |     0.85 | 42.93%     | ok               |
| SPY        |       64 | -0.13%   | 45.25%             | -15.53% |     0.06 | 49.42%     | ok               |
| SUSHI-USD  |       94 | -79.49%  | -73.45%            | -79.84% |    -1.33 | 39.46%     | ok               |
| T          |       72 | 44.01%   | 31.71%             | -17.01% |     0.86 | 56.74%     | ok               |
| TGT        |       60 | -11.06%  | 8.40%              | -34.42% |    -0.16 | 37.60%     | ok               |
| TIA-USD    |       93 | -52.01%  | -83.22%            | -75.93% |    -0.32 | 42.91%     | ok               |
| TLT        |       68 | -20.13%  | -13.97%            | -21.85% |    -1.51 | 33.78%     | ok               |
| TMO        |       67 | 25.55%   | 13.95%             | -18.85% |     0.55 | 54.74%     | ok               |
| TMUS       |       74 | -3.97%   | -4.66%             | -32.44% |     0.01 | 47.92%     | ok               |
| TRX-USD    |       66 | 1.44%    | 21.71%             | -22.90% |     0.12 | 50.77%     | ok               |
| TSLA       |       80 | -37.10%  | 103.85%            | -59.64% |    -0.26 | 42.93%     | ok               |
| TXN        |       77 | -27.13%  | 38.57%             | -46.62% |    -0.31 | 50.42%     | ok               |
| UNH        |       77 | 27.70%   | -24.12%            | -26.31% |     0.5  | 48.42%     | ok               |
| UNI-USD    |       90 | -40.02%  | 1.00%              | -72.03% |    -0.16 | 50.19%     | ok               |
| UPS        |       72 | -36.03%  | -33.38%            | -40.08% |    -0.71 | 42.76%     | ok               |
| USO        |       67 | -12.16%  | 105.10%            | -46.69% |    -0.05 | 33.44%     | ok               |
| VEA        |       62 | -3.76%   | 37.06%             | -17.27% |    -0.1  | 42.43%     | ok               |
| VIXY       |       94 | -78.27%  | -63.69%            | -88.17% |    -0.95 | 32.28%     | ok               |
| VNQ        |       73 | -14.48%  | 8.07%              | -24.92% |    -0.58 | 39.77%     | ok               |
| VTI        |       68 | -7.51%   | 43.73%             | -17.64% |    -0.22 | 49.42%     | ok               |
| VWO        |       80 | -18.39%  | 32.66%             | -25.20% |    -0.69 | 40.43%     | ok               |
| VZ         |       84 | -25.21%  | 11.64%             | -28.90% |    -0.77 | 41.76%     | ok               |
| WFC        |       80 | -18.22%  | 32.78%             | -28.90% |    -0.3  | 47.25%     | ok               |
| WIF-USD    |       68 | -26.73%  | -83.08%            | -52.76% |    -0.01 | 37.74%     | ok               |
| WMT        |       69 | 4.21%    | 78.02%             | -25.37% |     0.19 | 48.92%     | ok               |
| XBI        |       64 | -2.63%   | 59.24%             | -17.66% |     0.02 | 38.60%     | ok               |
| XLB        |       66 | -13.80%  | 8.71%              | -24.29% |    -0.49 | 31.78%     | ok               |
| XLC        |       61 | 12.62%   | 33.78%             | -12.33% |     0.47 | 50.25%     | ok               |
| XLE        |       69 | -3.00%   | 46.89%             | -30.31% |     0.01 | 45.26%     | ok               |
| XLF        |       82 | -9.88%   | 30.00%             | -23.61% |    -0.31 | 46.59%     | ok               |
| XLI        |       82 | -10.04%  | 33.30%             | -17.79% |    -0.35 | 42.76%     | ok               |
| XLK        |       42 | 48.86%   | 77.03%             | -14.75% |     0.97 | 46.42%     | ok               |
| XLM-USD    |       68 | -3.52%   | -42.42%            | -54.58% |     0.18 | 47.51%     | ok               |
| XLP        |       67 | 5.67%    | 10.59%             | -10.28% |     0.35 | 38.44%     | ok               |
| XLU        |       69 | -5.88%   | 15.87%             | -20.40% |    -0.21 | 39.60%     | ok               |
| XLV        |       76 | -22.52%  | 18.74%             | -22.75% |    -1.09 | 36.77%     | ok               |
| XLY        |       75 | -4.15%   | 26.24%             | -18.35% |    -0.06 | 47.59%     | ok               |
| XOM        |       55 | 1.71%    | 53.28%             | -20.29% |     0.12 | 34.28%     | ok               |
| XRP-USD    |       66 | 0.50%    | -48.50%            | -33.91% |     0.2  | 36.40%     | ok               |
| YFI-USD    |       77 | -62.99%  | -64.32%            | -63.82% |    -1.19 | 37.74%     | ok               |
| ZEC-USD    |       59 | 132.91%  | 2382.94%           | -56.50% |     0.88 | 41.38%     | ok               |

## AAPL Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 13.66%   | 79.65%             | -21.71% |     0.35 |       72 | 55.57%     | ok               |
|          15 | 10.74%   | 79.65%             | -23.86% |     0.3  |       81 | 62.90%     | ok               |
|          30 | 6.97%    | 79.65%             | -20.65% |     0.24 |       63 | 50.75%     | ok               |
|          35 | 5.44%    | 79.65%             | -22.04% |     0.21 |       63 | 49.42%     | ok               |
|          25 | 2.64%    | 79.65%             | -20.87% |     0.16 |       73 | 52.91%     | ok               |

## AAVE-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 28.92%   | -31.87%            | -43.61% |     0.49 |       43 | 36.59%     | ok               |
|          45 | 16.91%   | -31.87%            | -49.19% |     0.38 |       48 | 31.42%     | ok               |
|          50 | 11.67%   | -31.87%            | -45.07% |     0.33 |       46 | 23.75%     | ok               |
|          35 | 5.50%    | -31.87%            | -51.96% |     0.28 |       53 | 39.85%     | ok               |
|          15 | -36.01%  | -31.87%            | -61.76% |    -0.11 |       72 | 54.98%     | ok               |

## ABBV Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -9.25%   | 77.61%             | -26.16% |    -0.16 |       54 | 35.11%     | ok               |
|          25 | -19.01%  | 77.61%             | -30.04% |    -0.37 |       69 | 49.92%     | ok               |
|          20 | -19.50%  | 77.61%             | -28.73% |    -0.38 |       67 | 51.58%     | ok               |
|          40 | -19.81%  | 77.61%             | -27.36% |    -0.45 |       70 | 40.43%     | ok               |
|          30 | -21.98%  | 77.61%             | -30.52% |    -0.46 |       70 | 48.09%     | ok               |

## ADA-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 15.70%   | -72.85%            | -34.05% |     0.38 |       46 | 31.80%     | ok               |
|          50 | 9.09%    | -72.85%            | -33.96% |     0.3  |       48 | 27.39%     | ok               |
|          40 | -3.97%   | -72.85%            | -40.73% |     0.16 |       56 | 37.74%     | ok               |
|          15 | -23.42%  | -72.85%            | -47.27% |     0.04 |       71 | 61.88%     | ok               |
|          35 | -15.64%  | -72.85%            | -44.07% |     0.02 |       62 | 41.57%     | ok               |

## ADBE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | 4.63%    | -50.27%            | -29.07% |     0.22 |       54 | 61.40%     | ok               |
|          35 | -1.23%   | -50.27%            | -31.73% |     0.11 |       77 | 48.42%     | ok               |
|          20 | -9.08%   | -50.27%            | -31.52% |     0.03 |       60 | 64.39%     | ok               |
|          30 | -11.61%  | -50.27%            | -31.20% |    -0.03 |       71 | 56.91%     | ok               |
|          15 | -16.12%  | -50.27%            | -34.98% |    -0.08 |       62 | 66.06%     | ok               |

## AGG Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -5.65%   | -1.98%             | -9.59%  |    -1.01 |       58 | 24.79%     | ok               |
|          50 | -5.06%   | -1.98%             | -8.07%  |    -1.06 |       56 | 19.80%     | ok               |
|          30 | -6.82%   | -1.98%             | -11.01% |    -1.08 |       65 | 33.44%     | ok               |
|          20 | -8.31%   | -1.98%             | -11.89% |    -1.2  |       72 | 38.60%     | ok               |
|          25 | -8.23%   | -1.98%             | -12.28% |    -1.23 |       71 | 36.77%     | ok               |

## ALGO-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -24.13%  | -54.67%            | -38.19% |    -0.1  |       76 | 40.04%     | ok               |
|          25 | -33.84%  | -54.67%            | -51.92% |    -0.22 |       78 | 44.83%     | ok               |
|          15 | -40.32%  | -54.67%            | -51.37% |    -0.3  |       77 | 50.38%     | ok               |
|          35 | -37.39%  | -54.67%            | -51.36% |    -0.4  |       64 | 34.87%     | ok               |
|          20 | -48.11%  | -54.67%            | -54.48% |    -0.46 |       81 | 47.70%     | ok               |

## AMAT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -27.13%  | 104.74%            | -38.30% |    -0.24 |       50 | 36.11%     | ok               |
|          15 | -35.89%  | 104.74%            | -53.90% |    -0.28 |       72 | 60.57%     | ok               |
|          35 | -33.11%  | 104.74%            | -47.88% |    -0.3  |       71 | 48.92%     | ok               |
|          30 | -37.73%  | 104.74%            | -53.91% |    -0.36 |       71 | 51.58%     | ok               |
|          40 | -38.56%  | 104.74%            | -50.74% |    -0.41 |       69 | 44.09%     | ok               |

## AMD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 27.66%   | 244.86%            | -40.05% |     0.46 |       58 | 32.11%     | ok               |
|          40 | 17.34%   | 244.86%            | -41.09% |     0.37 |       56 | 37.27%     | ok               |
|          35 | 12.30%   | 244.86%            | -43.15% |     0.33 |       64 | 38.94%     | ok               |
|          45 | 2.14%    | 244.86%            | -49.59% |     0.23 |       62 | 35.11%     | ok               |
|          30 | -2.51%   | 244.86%            | -49.79% |     0.2  |       65 | 41.43%     | ok               |

## AMGN Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -10.06%  | 37.72%             | -26.65% |    -0.12 |       66 | 56.57%     | ok               |
|          35 | -12.70%  | 37.72%             | -31.29% |    -0.21 |       69 | 47.59%     | ok               |
|          15 | -15.37%  | 37.72%             | -27.98% |    -0.23 |       63 | 60.73%     | ok               |
|          30 | -14.85%  | 37.72%             | -34.19% |    -0.26 |       67 | 50.92%     | ok               |
|          25 | -16.60%  | 37.72%             | -33.47% |    -0.29 |       63 | 53.08%     | ok               |

## AMZN Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -27.97%  | 38.74%             | -29.61% |    -0.85 |       56 | 29.95%     | ok               |
|          50 | -31.74%  | 38.74%             | -33.91% |    -1.16 |       50 | 22.80%     | ok               |
|          45 | -37.46%  | 38.74%             | -38.25% |    -1.34 |       58 | 26.46%     | ok               |
|          35 | -52.04%  | 38.74%             | -52.54% |    -1.53 |       77 | 35.27%     | ok               |
|          30 | -55.73%  | 38.74%             | -56.19% |    -1.6  |       80 | 41.26%     | ok               |

## APT-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 43.52%   | -86.80%            | -27.79% |     0.73 |       42 | 16.67%     | ok               |
|          20 | 0.36%    | -86.80%            | -56.22% |     0.28 |       78 | 49.62%     | ok               |
|          45 | 2.88%    | -86.80%            | -52.49% |     0.23 |       58 | 23.37%     | ok               |
|          35 | -14.40%  | -86.80%            | -49.10% |     0.07 |       68 | 35.44%     | ok               |
|          25 | -22.50%  | -86.80%            | -55.69% |     0.03 |       70 | 44.25%     | ok               |

## ARB-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 57.32%   | -59.18%            | -33.60% |     0.67 |       54 | 26.44%     | ok               |
|          50 | 46.51%   | -59.18%            | -30.72% |     0.61 |       42 | 19.35%     | ok               |
|          15 | 28.87%   | -59.18%            | -46.19% |     0.5  |       88 | 59.00%     | ok               |
|          40 | 27.44%   | -59.18%            | -40.13% |     0.48 |       55 | 33.72%     | ok               |
|          35 | 21.94%   | -59.18%            | -45.71% |     0.44 |       71 | 37.93%     | ok               |

## ARKK Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -13.51%  | 87.78%             | -37.76% |    -0.06 |       89 | 54.74%     | ok               |
|          20 | -21.49%  | 87.78%             | -34.82% |    -0.22 |       87 | 49.92%     | ok               |
|          30 | -27.19%  | 87.78%             | -31.44% |    -0.39 |       85 | 43.43%     | ok               |
|          35 | -32.93%  | 87.78%             | -36.46% |    -0.55 |       86 | 40.77%     | ok               |
|          40 | -34.01%  | 87.78%             | -40.75% |    -0.61 |       78 | 36.61%     | ok               |

## ATOM-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -41.59%  | -67.79%            | -48.20% |    -0.33 |       86 | 65.90%     | ok               |
|          25 | -48.34%  | -67.79%            | -49.45% |    -0.52 |       92 | 54.60%     | ok               |
|          20 | -55.70%  | -67.79%            | -57.28% |    -0.66 |       96 | 58.24%     | ok               |
|          30 | -58.27%  | -67.79%            | -58.27% |    -0.81 |       92 | 48.28%     | ok               |
|          35 | -58.92%  | -67.79%            | -61.18% |    -0.93 |       82 | 42.34%     | ok               |

## AVAX-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 48.52%   | -61.26%            | -22.06% |     0.78 |       34 | 19.92%     | ok               |
|          40 | 9.52%    | -61.26%            | -30.70% |     0.3  |       40 | 27.78%     | ok               |
|          45 | 6.87%    | -61.26%            | -27.52% |     0.26 |       34 | 24.52%     | ok               |
|          35 | -7.44%   | -61.26%            | -37.03% |     0.09 |       54 | 34.10%     | ok               |
|          15 | -15.71%  | -61.26%            | -43.71% |     0.06 |       73 | 53.07%     | ok               |

## AVGO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | 20.98%   | 148.70%            | -38.01% |     0.4  |       68 | 44.26%     | ok               |
|          30 | 17.60%   | 148.70%            | -36.09% |     0.37 |       64 | 41.60%     | ok               |
|          50 | 12.58%   | 148.70%            | -36.86% |     0.31 |       56 | 29.45%     | ok               |
|          35 | 9.06%    | 148.70%            | -40.43% |     0.27 |       74 | 38.60%     | ok               |
|          40 | 7.83%    | 148.70%            | -40.70% |     0.26 |       64 | 35.27%     | ok               |

## BA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 41.10%   | -0.87%             | -13.34% |     0.9  |       46 | 35.77%     | ok               |
|          40 | 35.35%   | -0.87%             | -23.87% |     0.68 |       46 | 43.59%     | ok               |
|          35 | 36.93%   | -0.87%             | -18.09% |     0.67 |       62 | 47.92%     | ok               |
|          25 | 15.54%   | -0.87%             | -26.02% |     0.36 |       70 | 54.58%     | ok               |
|          45 | 7.60%    | -0.87%             | -26.76% |     0.25 |       44 | 39.93%     | ok               |

## BAC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | -0.90%   | 29.25%             | -22.94% |     0.05 |       64 | 45.26%     | ok               |
|          20 | -3.06%   | 29.25%             | -18.20% |     0.01 |       80 | 53.41%     | ok               |
|          25 | -5.43%   | 29.25%             | -22.11% |    -0.07 |       74 | 50.92%     | ok               |
|          45 | -6.80%   | 29.25%             | -19.32% |    -0.15 |       60 | 36.94%     | ok               |
|          15 | -10.85%  | 29.25%             | -23.94% |    -0.18 |       87 | 60.57%     | ok               |

## BCH-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 48.91%   | -35.76%            | -45.51% |     0.63 |       74 | 57.47%     | ok               |
|          20 | 23.43%   | -35.76%            | -45.82% |     0.44 |       68 | 54.21%     | ok               |
|          25 | 6.35%    | -35.76%            | -51.09% |     0.28 |       70 | 50.38%     | ok               |
|          30 | 6.56%    | -35.76%            | -53.87% |     0.28 |       76 | 48.85%     | ok               |
|          35 | -5.73%   | -35.76%            | -57.75% |     0.14 |       70 | 44.83%     | ok               |

## BITO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -8.95%   | -61.44%            | -31.98% |    -0    |       54 | 25.29%     | ok               |
|          30 | -19.94%  | -61.44%            | -39.47% |    -0.1  |       78 | 41.60%     | ok               |
|          15 | -28.56%  | -61.44%            | -48.38% |    -0.18 |       85 | 49.58%     | ok               |
|          45 | -21.49%  | -61.44%            | -33.99% |    -0.2  |       60 | 28.79%     | ok               |
|          25 | -27.14%  | -61.44%            | -38.26% |    -0.2  |       82 | 44.76%     | ok               |

## BLK Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | -5.94%   | 34.29%             | -20.79% |    -0.1  |       92 | 43.26%     | ok               |
|          40 | -7.20%   | 34.29%             | -22.83% |    -0.16 |       80 | 38.44%     | ok               |
|          20 | -9.12%   | 34.29%             | -21.48% |    -0.16 |       88 | 51.75%     | ok               |
|          25 | -10.43%  | 34.29%             | -24.62% |    -0.21 |       81 | 49.58%     | ok               |
|          30 | -14.58%  | 34.29%             | -26.90% |    -0.35 |       85 | 47.09%     | ok               |

## BND Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -6.55%   | -1.95%             | -10.21% |    -0.92 |       66 | 40.77%     | ok               |
|          30 | -6.86%   | -1.95%             | -10.91% |    -1.05 |       67 | 35.61%     | ok               |
|          25 | -7.20%   | -1.95%             | -11.27% |    -1.05 |       69 | 38.77%     | ok               |
|          15 | -8.25%   | -1.95%             | -11.52% |    -1.15 |       77 | 43.43%     | ok               |
|          35 | -8.41%   | -1.95%             | -12.42% |    -1.35 |       70 | 32.11%     | ok               |

## BONK-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 156.03%  | -86.82%            | -35.57% |     1.2  |       42 | 21.46%     | ok               |
|          15 | 69.51%   | -86.82%            | -62.48% |     0.71 |       72 | 59.77%     | ok               |
|          45 | 50.70%   | -86.82%            | -47.53% |     0.64 |       66 | 27.59%     | ok               |
|          20 | 23.57%   | -86.82%            | -61.03% |     0.48 |       69 | 55.94%     | ok               |
|          40 | 22.88%   | -86.82%            | -53.34% |     0.45 |       58 | 36.78%     | ok               |

## BTC-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 44.63%   | -21.20%            | -14.50% |     0.89 |       44 | 35.25%     | ok               |
|          45 | 40.11%   | -21.20%            | -12.20% |     0.85 |       42 | 31.23%     | ok               |
|          35 | 43.62%   | -21.20%            | -21.56% |     0.84 |       62 | 41.57%     | ok               |
|          50 | 18.02%   | -21.20%            | -20.63% |     0.49 |       38 | 26.44%     | ok               |
|          30 | 18.72%   | -21.20%            | -21.75% |     0.45 |       68 | 47.51%     | ok               |

## C Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -9.53%   | 91.59%             | -21.16% |    -0.2  |       68 | 31.11%     | ok               |
|          45 | -20.33%  | 91.59%             | -29.02% |    -0.5  |       76 | 35.27%     | ok               |
|          40 | -25.92%  | 91.59%             | -34.58% |    -0.63 |       76 | 37.60%     | ok               |
|          25 | -32.45%  | 91.59%             | -36.49% |    -0.67 |       71 | 48.25%     | ok               |
|          30 | -33.75%  | 91.59%             | -39.51% |    -0.72 |       79 | 46.09%     | ok               |

## CAT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 16.33%   | 110.42%            | -21.80% |     0.37 |       73 | 60.57%     | ok               |
|          25 | 12.11%   | 110.42%            | -21.79% |     0.31 |       66 | 50.42%     | ok               |
|          45 | 5.30%    | 110.42%            | -23.56% |     0.21 |       54 | 36.61%     | ok               |
|          30 | 4.67%    | 110.42%            | -21.87% |     0.2  |       70 | 48.09%     | ok               |
|          20 | 3.01%    | 110.42%            | -24.56% |     0.18 |       76 | 53.58%     | ok               |

## CL Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 0.91%    | -2.09%             | -12.98% |     0.09 |       44 | 22.46%     | ok               |
|          30 | -2.83%   | -2.09%             | -14.32% |    -0.03 |       66 | 38.60%     | ok               |
|          45 | -4.94%   | -2.09%             | -13.13% |    -0.15 |       50 | 25.29%     | ok               |
|          35 | -6.70%   | -2.09%             | -15.39% |    -0.18 |       66 | 34.78%     | ok               |
|          15 | -11.54%  | -2.09%             | -19.00% |    -0.28 |       66 | 46.92%     | ok               |

## CMCSA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -18.53%  | -42.25%            | -28.41% |    -0.61 |       48 | 16.81%     | ok               |
|          15 | -35.43%  | -42.25%            | -46.99% |    -0.73 |       91 | 58.07%     | ok               |
|          45 | -23.76%  | -42.25%            | -35.13% |    -0.74 |       62 | 21.46%     | ok               |
|          30 | -35.26%  | -42.25%            | -46.39% |    -0.84 |       84 | 43.43%     | ok               |
|          40 | -31.56%  | -42.25%            | -42.51% |    -0.84 |       89 | 28.95%     | ok               |

## COMP-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -2.05%   | -53.42%            | -38.71% |     0.18 |       52 | 25.10%     | ok               |
|          30 | -32.76%  | -53.42%            | -52.27% |    -0.13 |       95 | 50.38%     | ok               |
|          25 | -39.53%  | -53.42%            | -51.46% |    -0.21 |       94 | 58.43%     | ok               |
|          15 | -46.45%  | -53.42%            | -52.34% |    -0.3  |       98 | 68.58%     | ok               |
|          45 | -40.88%  | -53.42%            | -50.83% |    -0.35 |       64 | 33.72%     | ok               |

## COP Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -5.54%   | 20.43%             | -34.61% |    -0.03 |       48 | 27.95%     | ok               |
|          35 | -12.49%  | 20.43%             | -44.07% |    -0.14 |       73 | 41.43%     | ok               |
|          30 | -14.37%  | 20.43%             | -43.40% |    -0.18 |       70 | 44.26%     | ok               |
|          45 | -12.96%  | 20.43%             | -41.10% |    -0.19 |       64 | 32.11%     | ok               |
|          40 | -20.70%  | 20.43%             | -47.54% |    -0.37 |       76 | 35.77%     | ok               |

## COST Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 13.94%   | 22.47%             | -24.32% |     0.46 |       62 | 47.09%     | ok               |
|          25 | 10.65%   | 22.47%             | -24.93% |     0.38 |       59 | 44.26%     | ok               |
|          35 | 4.27%    | 22.47%             | -30.16% |     0.2  |       58 | 38.60%     | ok               |
|          30 | -0.14%   | 22.47%             | -31.32% |     0.06 |       60 | 41.10%     | ok               |
|          15 | -1.50%   | 22.47%             | -27.30% |     0.03 |       67 | 50.75%     | ok               |

## CRM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | -21.94%  | -16.87%            | -32.74% |    -0.26 |       64 | 41.60%     | ok               |
|          40 | -24.87%  | -16.87%            | -38.23% |    -0.35 |       70 | 37.44%     | ok               |
|          15 | -31.38%  | -16.87%            | -47.54% |    -0.36 |       90 | 57.40%     | ok               |
|          50 | -22.79%  | -16.87%            | -38.38% |    -0.42 |       60 | 24.79%     | ok               |
|          30 | -32.66%  | -16.87%            | -44.41% |    -0.47 |       67 | 46.42%     | ok               |

## CRV-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 62.98%   | -56.55%            | -37.78% |     0.73 |       66 | 32.38%     | ok               |
|          40 | 48.46%   | -56.55%            | -38.86% |     0.64 |       54 | 28.16%     | ok               |
|          45 | 38.76%   | -56.55%            | -42.29% |     0.58 |       54 | 21.65%     | ok               |
|          50 | 37.81%   | -56.55%            | -30.73% |     0.58 |       46 | 17.62%     | ok               |
|          30 | 30.99%   | -56.55%            | -39.89% |     0.5  |       66 | 36.97%     | ok               |

## CSCO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 34.05%   | 139.60%            | -19.34% |     0.7  |       50 | 38.44%     | ok               |
|          45 | 29.51%   | 139.60%            | -19.34% |     0.62 |       52 | 40.10%     | ok               |
|          25 | 21.92%   | 139.60%            | -23.28% |     0.47 |       61 | 50.75%     | ok               |
|          20 | 16.45%   | 139.60%            | -22.72% |     0.39 |       71 | 53.08%     | ok               |
|          30 | 15.50%   | 139.60%            | -21.79% |     0.38 |       64 | 49.42%     | ok               |

## CVX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -9.60%   | 40.92%             | -23.80% |    -0.17 |       73 | 44.59%     | ok               |
|          40 | -10.08%  | 40.92%             | -27.34% |    -0.22 |       73 | 36.61%     | ok               |
|          45 | -10.48%  | 40.92%             | -28.83% |    -0.24 |       65 | 33.28%     | ok               |
|          50 | -10.36%  | 40.92%             | -30.69% |    -0.29 |       58 | 28.79%     | ok               |
|          35 | -13.01%  | 40.92%             | -28.85% |    -0.29 |       67 | 38.60%     | ok               |

## DASH-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 156.61%  | 88.91%             | -33.55% |     1.01 |       38 | 18.01%     | ok               |
|          40 | 125.75%  | 88.91%             | -33.20% |     0.89 |       42 | 24.33%     | ok               |
|          45 | 94.16%   | 88.91%             | -37.63% |     0.78 |       42 | 20.50%     | ok               |
|          30 | 2.17%    | 88.91%             | -64.43% |     0.4  |       53 | 30.46%     | ok               |
|          25 | -3.52%   | 88.91%             | -64.14% |     0.36 |       63 | 32.95%     | ok               |

## DBC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -0.09%   | 41.87%             | -26.05% |     0.07 |       77 | 41.26%     | ok               |
|          20 | -4.49%   | 41.87%             | -25.69% |    -0.08 |       69 | 39.60%     | ok               |
|          25 | -5.28%   | 41.87%             | -24.84% |    -0.11 |       66 | 37.60%     | ok               |
|          50 | -6.09%   | 41.87%             | -19.34% |    -0.18 |       50 | 24.79%     | ok               |
|          35 | -7.76%   | 41.87%             | -23.19% |    -0.2  |       66 | 34.28%     | ok               |

## DE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 2.13%    | 68.49%             | -17.97% |     0.13 |       56 | 29.62%     | ok               |
|          45 | -4.48%   | 68.49%             | -19.53% |    -0.02 |       60 | 34.11%     | ok               |
|          20 | -7.80%   | 68.49%             | -24.11% |    -0.07 |       65 | 48.59%     | ok               |
|          25 | -12.03%  | 68.49%             | -24.29% |    -0.17 |       71 | 46.92%     | ok               |
|          30 | -12.17%  | 68.49%             | -23.98% |    -0.18 |       70 | 44.26%     | ok               |

## DIA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -5.16%   | 29.99%             | -11.17% |    -0.24 |       58 | 44.93%     | ok               |
|          35 | -6.01%   | 29.99%             | -13.15% |    -0.31 |       68 | 40.60%     | ok               |
|          30 | -7.42%   | 29.99%             | -12.94% |    -0.38 |       66 | 43.59%     | ok               |
|          20 | -7.89%   | 29.99%             | -13.60% |    -0.39 |       64 | 46.92%     | ok               |
|          40 | -9.14%   | 29.99%             | -15.06% |    -0.52 |       72 | 37.27%     | ok               |

## DIS Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 34.04%   | 5.79%              | -10.17% |     1.06 |       44 | 25.12%     | ok               |
|          40 | 6.23%    | 5.79%              | -18.75% |     0.23 |       59 | 33.78%     | ok               |
|          45 | 2.94%    | 5.79%              | -16.54% |     0.16 |       45 | 28.95%     | ok               |
|          15 | -5.22%   | 5.79%              | -32.73% |    -0    |       83 | 54.24%     | ok               |
|          35 | -5.11%   | 5.79%              | -25.70% |    -0.03 |       73 | 39.93%     | ok               |

## DOGE-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 6.58%    | -65.20%            | -57.89% |     0.32 |       73 | 64.18%     | ok               |
|          20 | -1.64%   | -65.20%            | -55.83% |     0.24 |       75 | 58.81%     | ok               |
|          25 | -8.69%   | -65.20%            | -53.72% |     0.16 |       67 | 54.98%     | ok               |
|          30 | -25.79%  | -65.20%            | -60.95% |    -0.07 |       69 | 48.85%     | ok               |
|          50 | -26.91%  | -65.20%            | -52.88% |    -0.19 |       62 | 24.52%     | ok               |

## DOT-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -52.89%  | -78.28%            | -72.06% |    -0.32 |       74 | 63.22%     | ok               |
|          20 | -49.63%  | -78.28%            | -66.32% |    -0.34 |       86 | 59.20%     | ok               |
|          30 | -51.45%  | -78.28%            | -63.33% |    -0.42 |       86 | 48.28%     | ok               |
|          25 | -57.40%  | -78.28%            | -69.99% |    -0.51 |       77 | 54.21%     | ok               |
|          35 | -55.47%  | -78.28%            | -62.35% |    -0.54 |       82 | 42.91%     | ok               |

## DXY-INDEX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd    |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:-------|---------:|---------:|:-----------|:-----------------|
|          50 | -0.78%   | -4.64%             | -6.02% |    -0.11 |       40 | 32.25%     | ok               |
|          40 | -2.14%   | -4.64%             | -7.30% |    -0.26 |       64 | 47.62%     | ok               |
|          45 | -2.14%   | -4.64%             | -8.14% |    -0.28 |       60 | 38.31%     | ok               |
|          30 | -5.04%   | -4.64%             | -9.83% |    -0.59 |       74 | 57.58%     | ok               |
|          35 | -5.20%   | -4.64%             | -9.97% |    -0.65 |       77 | 52.60%     | ok               |

## EEM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -7.47%   | 48.98%             | -15.88% |    -0.22 |       54 | 32.45%     | ok               |
|          45 | -7.81%   | 48.98%             | -17.03% |    -0.23 |       52 | 33.94%     | ok               |
|          40 | -8.15%   | 48.98%             | -19.20% |    -0.23 |       64 | 36.11%     | ok               |
|          35 | -8.78%   | 48.98%             | -23.57% |    -0.23 |       66 | 38.10%     | ok               |
|          30 | -12.03%  | 48.98%             | -24.04% |    -0.34 |       62 | 39.93%     | ok               |

## EFA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -2.34%   | 27.17%             | -10.10% |    -0.02 |       64 | 51.41%     | ok               |
|          20 | -9.96%   | 27.17%             | -13.73% |    -0.35 |       71 | 48.42%     | ok               |
|          30 | -10.81%  | 27.17%             | -12.96% |    -0.42 |       66 | 41.26%     | ok               |
|          25 | -11.70%  | 27.17%             | -15.23% |    -0.44 |       70 | 44.76%     | ok               |
|          40 | -11.24%  | 27.17%             | -14.58% |    -0.48 |       62 | 36.44%     | ok               |

## EOG Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -17.13%  | 22.32%             | -35.34% |    -0.36 |       56 | 30.78%     | ok               |
|          50 | -21.70%  | 22.32%             | -35.63% |    -0.52 |       52 | 27.95%     | ok               |
|          40 | -23.40%  | 22.32%             | -37.39% |    -0.53 |       72 | 34.78%     | ok               |
|          35 | -27.42%  | 22.32%             | -41.05% |    -0.62 |       85 | 39.77%     | ok               |
|          30 | -29.94%  | 22.32%             | -47.87% |    -0.64 |       80 | 44.93%     | ok               |

## ETC-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -5.47%   | -60.93%            | -38.47% |     0.05 |       28 | 20.50%     | ok               |
|          50 | -4.94%   | -60.93%            | -31.28% |     0.05 |       28 | 18.20%     | ok               |
|          40 | -17.03%  | -60.93%            | -43.28% |    -0.15 |       38 | 23.56%     | ok               |
|          35 | -18.72%  | -60.93%            | -46.64% |    -0.15 |       46 | 27.39%     | ok               |
|          30 | -22.18%  | -60.93%            | -47.84% |    -0.19 |       60 | 31.42%     | ok               |

## ETH-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 146.84%  | -5.07%             | -30.11% |     1.32 |       58 | 48.08%     | ok               |
|          30 | 108.23%  | -5.07%             | -32.89% |     1.06 |       60 | 55.75%     | ok               |
|          40 | 66.27%   | -5.07%             | -33.11% |     0.86 |       62 | 40.42%     | ok               |
|          25 | 70.46%   | -5.07%             | -40.90% |     0.82 |       60 | 59.58%     | ok               |
|          20 | 54.99%   | -5.07%             | -39.10% |     0.7  |       82 | 63.79%     | ok               |

## EWJ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -22.99%  | 40.90%             | -29.40% |    -0.8  |       62 | 36.44%     | ok               |
|          20 | -23.95%  | 40.90%             | -30.00% |    -0.81 |       56 | 38.44%     | ok               |
|          25 | -25.82%  | 40.90%             | -29.85% |    -0.9  |       56 | 37.60%     | ok               |
|          15 | -27.60%  | 40.90%             | -31.15% |    -0.9  |       67 | 41.76%     | ok               |
|          45 | -23.60%  | 40.90%             | -27.35% |    -0.96 |       60 | 28.29%     | ok               |

## FCX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 2.51%    | 35.90%             | -29.27% |     0.18 |       50 | 31.61%     | ok               |
|          50 | -0.09%   | 35.90%             | -26.57% |     0.13 |       52 | 27.95%     | ok               |
|          40 | -10.00%  | 35.90%             | -42.89% |    -0.01 |       62 | 36.94%     | ok               |
|          30 | -29.37%  | 35.90%             | -46.84% |    -0.32 |       65 | 44.26%     | ok               |
|          35 | -29.20%  | 35.90%             | -50.12% |    -0.34 |       67 | 42.10%     | ok               |

## FET-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -39.02%  | -76.50%            | -59.58% |    -0.08 |       82 | 57.09%     | ok               |
|          25 | -37.94%  | -76.50%            | -65.31% |    -0.11 |       85 | 47.32%     | ok               |
|          20 | -43.00%  | -76.50%            | -65.01% |    -0.16 |       92 | 52.87%     | ok               |
|          30 | -52.60%  | -76.50%            | -65.38% |    -0.39 |       83 | 42.72%     | ok               |
|          50 | -39.06%  | -76.50%            | -45.19% |    -0.53 |       46 | 14.37%     | ok               |

## FIL-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -40.15%  | -66.73%            | -58.54% |    -0.34 |       65 | 37.16%     | ok               |
|          35 | -41.96%  | -66.73%            | -61.90% |    -0.42 |       58 | 31.23%     | ok               |
|          40 | -40.23%  | -66.73%            | -57.60% |    -0.44 |       48 | 26.82%     | ok               |
|          15 | -58.37%  | -66.73%            | -71.82% |    -0.57 |       91 | 49.04%     | ok               |
|          25 | -58.52%  | -66.73%            | -70.65% |    -0.66 |       76 | 40.04%     | ok               |

## FXI Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -6.95%   | 20.07%             | -22.99% |    -0.09 |       52 | 32.61%     | ok               |
|          15 | -7.81%   | 20.07%             | -21.68% |    -0.1  |       54 | 36.61%     | ok               |
|          30 | -7.21%   | 20.07%             | -24.33% |    -0.1  |       50 | 31.11%     | ok               |
|          20 | -10.50%  | 20.07%             | -24.94% |    -0.18 |       54 | 34.44%     | ok               |
|          35 | -10.80%  | 20.07%             | -27.93% |    -0.21 |       52 | 28.62%     | ok               |

## GDX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 10.98%   | 135.26%            | -31.44% |     0.3  |       76 | 50.25%     | ok               |
|          40 | 7.03%    | 135.26%            | -28.04% |     0.24 |       60 | 38.27%     | ok               |
|          30 | 6.09%    | 135.26%            | -33.31% |     0.23 |       62 | 44.59%     | ok               |
|          35 | 0.84%    | 135.26%            | -31.73% |     0.14 |       68 | 40.93%     | ok               |
|          25 | -2.58%   | 135.26%            | -38.90% |     0.1  |       66 | 46.26%     | ok               |

## GDXJ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -19.00%  | 133.92%            | -41.17% |    -0.1  |       74 | 50.25%     | ok               |
|          50 | -21.78%  | 133.92%            | -46.83% |    -0.25 |       60 | 34.44%     | ok               |
|          35 | -30.02%  | 133.92%            | -37.32% |    -0.36 |       72 | 40.43%     | ok               |
|          30 | -31.95%  | 133.92%            | -40.39% |    -0.38 |       72 | 43.09%     | ok               |
|          25 | -36.08%  | 133.92%            | -42.91% |    -0.43 |       77 | 46.26%     | ok               |

## GE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 4.89%    | 90.92%             | -21.25% |     0.2  |       60 | 33.78%     | ok               |
|          45 | -2.34%   | 90.92%             | -21.88% |     0.05 |       70 | 36.44%     | ok               |
|          30 | -8.43%   | 90.92%             | -27.82% |    -0.04 |       76 | 48.09%     | ok               |
|          25 | -8.86%   | 90.92%             | -29.91% |    -0.05 |       72 | 49.92%     | ok               |
|          20 | -9.37%   | 90.92%             | -25.05% |    -0.05 |       72 | 52.58%     | ok               |

## GLD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | 18.61%   | 70.82%             | -13.87% |     0.49 |       48 | 46.92%     | ok               |
|          20 | 17.00%   | 70.82%             | -13.87% |     0.46 |       49 | 48.59%     | ok               |
|          30 | 12.96%   | 70.82%             | -13.87% |     0.38 |       50 | 45.76%     | ok               |
|          35 | 9.97%    | 70.82%             | -15.09% |     0.32 |       52 | 43.43%     | ok               |
|          15 | 6.24%    | 70.82%             | -18.05% |     0.23 |       57 | 51.91%     | ok               |

## GOOGL Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 60.18%   | 97.10%             | -17.38% |     1.07 |       59 | 43.93%     | ok               |
|          30 | 56.30%   | 97.10%             | -17.54% |     1    |       57 | 47.42%     | ok               |
|          45 | 48.78%   | 97.10%             | -11.66% |     0.98 |       52 | 37.44%     | ok               |
|          25 | 53.92%   | 97.10%             | -16.87% |     0.95 |       57 | 49.92%     | ok               |
|          50 | 44.40%   | 97.10%             | -11.52% |     0.94 |       44 | 32.61%     | ok               |

## GRT-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 68.95%   | -79.72%            | -33.74% |     0.76 |       77 | 45.79%     | ok               |
|          45 | 45.34%   | -79.72%            | -39.76% |     0.64 |       48 | 27.78%     | ok               |
|          15 | 45.60%   | -79.72%            | -42.58% |     0.6  |       69 | 62.45%     | ok               |
|          25 | 42.50%   | -79.72%            | -37.67% |     0.58 |       78 | 52.30%     | ok               |
|          50 | 31.50%   | -79.72%            | -31.62% |     0.53 |       46 | 21.26%     | ok               |

## GS Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 23.66%   | 90.04%             | -20.56% |     0.52 |       68 | 56.41%     | ok               |
|          20 | 4.66%    | 90.04%             | -23.19% |     0.2  |       68 | 53.08%     | ok               |
|          40 | 3.21%    | 90.04%             | -16.24% |     0.16 |       70 | 42.26%     | ok               |
|          25 | -0.64%   | 90.04%             | -23.32% |     0.09 |       68 | 50.58%     | ok               |
|          30 | -2.81%   | 90.04%             | -21.94% |     0.04 |       70 | 48.09%     | ok               |

## HBAR-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -18.60%  | -20.54%            | -39.26% |    -0.27 |       18 | 17.80%     | ok               |
|          45 | -33.67%  | -20.54%            | -48.27% |    -0.69 |       22 | 23.86%     | ok               |
|          40 | -34.80%  | -20.54%            | -50.61% |    -0.71 |       28 | 28.79%     | ok               |
|          30 | -40.92%  | -20.54%            | -56.47% |    -0.86 |       40 | 37.88%     | ok               |
|          35 | -40.29%  | -20.54%            | -56.01% |    -0.86 |       30 | 33.33%     | ok               |

## HD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 1.72%    | -10.61%            | -17.15% |     0.13 |       67 | 43.59%     | ok               |
|          40 | 1.06%    | -10.61%            | -16.74% |     0.1  |       72 | 34.78%     | ok               |
|          35 | 0.84%    | -10.61%            | -17.81% |     0.1  |       70 | 39.60%     | ok               |
|          45 | 0.27%    | -10.61%            | -17.41% |     0.07 |       48 | 29.95%     | ok               |
|          25 | -1.35%   | -10.61%            | -18.17% |     0.05 |       66 | 45.92%     | ok               |

## HON Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -11.17%  | 3.57%              | -20.54% |    -0.28 |       70 | 32.95%     | ok               |
|          45 | -14.88%  | 3.57%              | -22.88% |    -0.38 |       72 | 38.44%     | ok               |
|          35 | -25.38%  | 3.57%              | -31.66% |    -0.65 |       93 | 50.08%     | ok               |
|          40 | -25.13%  | 3.57%              | -31.84% |    -0.67 |       76 | 42.76%     | ok               |
|          30 | -27.02%  | 3.57%              | -33.87% |    -0.67 |       93 | 55.07%     | ok               |

## HYG Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -4.37%   | -0.36%             | -7.76%  |    -0.49 |       70 | 34.11%     | ok               |
|          30 | -6.36%   | -0.36%             | -10.59% |    -0.7  |       85 | 39.10%     | ok               |
|          35 | -6.20%   | -0.36%             | -9.66%  |    -0.71 |       79 | 35.77%     | ok               |
|          45 | -6.17%   | -0.36%             | -8.86%  |    -0.74 |       70 | 30.45%     | ok               |
|          25 | -7.32%   | -0.36%             | -11.22% |    -0.79 |       89 | 41.60%     | ok               |

## IBIT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 64.97%   | 21.65%             | -19.20% |     0.94 |       44 | 41.99%     | ok               |
|          50 | 52.34%   | 21.65%             | -17.37% |     0.94 |       26 | 25.56%     | ok               |
|          45 | 42.96%   | 21.65%             | -17.37% |     0.8  |       30 | 26.77%     | ok               |
|          30 | 36.55%   | 21.65%             | -18.95% |     0.67 |       40 | 35.09%     | ok               |
|          40 | 33.95%   | 21.65%             | -18.15% |     0.67 |       32 | 28.80%     | ok               |

## IBM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -20.21%  | 31.20%             | -49.43% |    -0.16 |       83 | 60.73%     | ok               |
|          35 | -23.13%  | 31.20%             | -47.10% |    -0.27 |       63 | 45.59%     | ok               |
|          30 | -26.33%  | 31.20%             | -48.94% |    -0.32 |       69 | 49.25%     | ok               |
|          50 | -27.58%  | 31.20%             | -45.88% |    -0.4  |       48 | 34.78%     | ok               |
|          20 | -31.66%  | 31.20%             | -53.45% |    -0.4  |       69 | 53.74%     | ok               |

## ICP-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -17.76%  | -49.32%            | -46.42% |     0.09 |       79 | 39.46%     | ok               |
|          35 | -19.50%  | -49.32%            | -51.30% |    -0.01 |       72 | 33.91%     | ok               |
|          40 | -20.07%  | -49.32%            | -45.75% |    -0.04 |       64 | 29.12%     | ok               |
|          15 | -44.47%  | -49.32%            | -59.36% |    -0.13 |       79 | 50.38%     | ok               |
|          20 | -46.41%  | -49.32%            | -62.47% |    -0.18 |       88 | 47.51%     | ok               |

## IEF Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -6.54%   | -3.63%             | -10.18% |    -0.77 |       72 | 42.26%     | ok               |
|          15 | -7.10%   | -3.63%             | -10.91% |    -0.82 |       71 | 43.76%     | ok               |
|          50 | -7.26%   | -3.63%             | -9.11%  |    -1.22 |       58 | 21.96%     | ok               |
|          40 | -8.48%   | -3.63%             | -11.39% |    -1.23 |       64 | 26.79%     | ok               |
|          45 | -8.46%   | -3.63%             | -11.30% |    -1.26 |       60 | 25.12%     | ok               |

## IEMG Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -3.12%   | 44.96%             | -14.22% |    -0.07 |       54 | 31.28%     | ok               |
|          35 | -4.42%   | 44.96%             | -21.81% |    -0.09 |       65 | 38.94%     | ok               |
|          45 | -3.91%   | 44.96%             | -15.23% |    -0.09 |       50 | 33.78%     | ok               |
|          40 | -5.40%   | 44.96%             | -18.73% |    -0.14 |       62 | 36.77%     | ok               |
|          25 | -8.64%   | 44.96%             | -24.30% |    -0.24 |       61 | 41.76%     | ok               |

## INJ-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 6.03%    | -46.20%            | -51.11% |     0.31 |       60 | 37.16%     | ok               |
|          40 | 6.66%    | -46.20%            | -44.20% |     0.3  |       50 | 33.91%     | ok               |
|          45 | -2.08%   | -46.20%            | -42.01% |     0.2  |       54 | 28.35%     | ok               |
|          30 | -28.38%  | -46.20%            | -68.18% |    -0.04 |       65 | 40.42%     | ok               |
|          15 | -43.24%  | -46.20%            | -76.62% |    -0.17 |       77 | 51.15%     | ok               |

## INTC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 70.01%   | 212.29%            | -49.32% |     0.71 |       56 | 33.78%     | ok               |
|          50 | 64.73%   | 212.29%            | -48.35% |     0.68 |       60 | 29.95%     | ok               |
|          15 | 62.64%   | 212.29%            | -53.65% |     0.64 |       76 | 59.57%     | ok               |
|          40 | 51.36%   | 212.29%            | -55.86% |     0.59 |       64 | 37.94%     | ok               |
|          25 | 46.47%   | 212.29%            | -56.41% |     0.56 |       77 | 50.75%     | ok               |

## INTU Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 10.17%   | -53.68%            | -34.75% |     0.29 |       65 | 28.45%     | ok               |
|          45 | -1.24%   | -53.68%            | -40.30% |     0.1  |       65 | 32.78%     | ok               |
|          25 | -6.72%   | -53.68%            | -35.05% |     0.03 |       70 | 49.42%     | ok               |
|          40 | -5.65%   | -53.68%            | -42.51% |     0.02 |       67 | 36.77%     | ok               |
|          30 | -11.33%  | -53.68%            | -37.41% |    -0.05 |       71 | 46.59%     | ok               |

## ITA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -1.77%   | 49.46%             | -28.06% |     0.05 |       83 | 60.90%     | ok               |
|          50 | -1.76%   | 49.46%             | -21.48% |     0.01 |       76 | 36.77%     | ok               |
|          30 | -4.11%   | 49.46%             | -23.75% |    -0.04 |       78 | 48.59%     | ok               |
|          20 | -8.04%   | 49.46%             | -28.06% |    -0.14 |       84 | 54.91%     | ok               |
|          40 | -7.44%   | 49.46%             | -20.54% |    -0.16 |       78 | 41.93%     | ok               |

## IWM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | 13.66%   | 31.36%             | -10.63% |     0.53 |       54 | 34.94%     | ok               |
|          20 | 12.15%   | 31.36%             | -10.41% |     0.47 |       60 | 35.94%     | ok               |
|          15 | 8.71%    | 31.36%             | -12.11% |     0.35 |       78 | 41.76%     | ok               |
|          30 | 7.82%    | 31.36%             | -10.95% |     0.34 |       54 | 34.11%     | ok               |
|          40 | 6.87%    | 31.36%             | -12.26% |     0.33 |       46 | 29.45%     | ok               |

## JNJ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 17.02%   | 65.41%             | -10.57% |     0.7  |       40 | 34.78%     | ok               |
|          15 | 12.12%   | 65.41%             | -17.37% |     0.45 |       58 | 53.24%     | ok               |
|          45 | 7.01%    | 65.41%             | -13.35% |     0.32 |       46 | 38.44%     | ok               |
|          30 | 7.29%    | 65.41%             | -16.86% |     0.31 |       60 | 46.76%     | ok               |
|          20 | 6.94%    | 65.41%             | -16.96% |     0.3  |       64 | 49.75%     | ok               |

## JPM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 4.67%    | 69.07%             | -15.90% |     0.22 |       50 | 32.95%     | ok               |
|          45 | -5.76%   | 69.07%             | -21.91% |    -0.12 |       54 | 35.61%     | ok               |
|          20 | -21.03%  | 69.07%             | -35.58% |    -0.46 |       86 | 49.08%     | ok               |
|          35 | -18.04%  | 69.07%             | -27.43% |    -0.51 |       74 | 41.43%     | ok               |
|          40 | -18.70%  | 69.07%             | -28.47% |    -0.54 |       66 | 38.27%     | ok               |

## KO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 23.22%   | 45.68%             | -8.64%  |     0.83 |       54 | 36.77%     | ok               |
|          35 | 19.04%   | 45.68%             | -8.21%  |     0.71 |       58 | 35.27%     | ok               |
|          40 | 16.17%   | 45.68%             | -9.28%  |     0.65 |       60 | 31.95%     | ok               |
|          25 | 17.05%   | 45.68%             | -10.16% |     0.63 |       60 | 39.60%     | ok               |
|          20 | 4.13%    | 45.68%             | -15.99% |     0.2  |       77 | 43.76%     | ok               |

## LDO-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 74.07%   | -64.53%            | -39.01% |     0.74 |       77 | 59.00%     | ok               |
|          20 | 57.25%   | -64.53%            | -41.22% |     0.66 |       79 | 54.41%     | ok               |
|          30 | 49.35%   | -64.53%            | -50.81% |     0.62 |       68 | 46.55%     | ok               |
|          25 | 27.32%   | -64.53%            | -50.58% |     0.48 |       78 | 51.34%     | ok               |
|          35 | 25.35%   | -64.53%            | -58.48% |     0.46 |       74 | 39.08%     | ok               |

## LIN Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -7.89%   | 13.32%             | -23.00% |    -0.21 |       66 | 44.43%     | ok               |
|          25 | -7.82%   | 13.32%             | -22.01% |    -0.21 |       73 | 41.43%     | ok               |
|          15 | -9.63%   | 13.32%             | -23.68% |    -0.27 |       72 | 47.75%     | ok               |
|          30 | -10.90%  | 13.32%             | -20.61% |    -0.34 |       74 | 38.60%     | ok               |
|          35 | -12.66%  | 13.32%             | -19.70% |    -0.45 |       74 | 31.61%     | ok               |

## LINK-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 46.50%   | -27.57%            | -33.64% |     0.63 |       68 | 45.40%     | ok               |
|          45 | 24.83%   | -27.57%            | -33.71% |     0.46 |       52 | 31.80%     | ok               |
|          35 | 22.59%   | -27.57%            | -34.21% |     0.44 |       62 | 41.38%     | ok               |
|          40 | 14.66%   | -27.57%            | -34.00% |     0.36 |       58 | 35.82%     | ok               |
|          25 | 2.12%    | -27.57%            | -46.32% |     0.27 |       64 | 48.85%     | ok               |

## LLY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -2.46%   | 50.54%             | -38.23% |     0.06 |       50 | 35.44%     | ok               |
|          15 | -16.23%  | 50.54%             | -48.12% |    -0.13 |       70 | 60.23%     | ok               |
|          45 | -15.32%  | 50.54%             | -42.75% |    -0.2  |       60 | 39.10%     | ok               |
|          40 | -26.08%  | 50.54%             | -46.32% |    -0.41 |       70 | 42.10%     | ok               |
|          20 | -29.61%  | 50.54%             | -52.31% |    -0.41 |       77 | 55.24%     | ok               |

## LRCX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -19.19%  | 197.09%            | -48.71% |    -0.1  |       74 | 33.94%     | ok               |
|          40 | -21.90%  | 197.09%            | -53.45% |    -0.11 |       70 | 40.10%     | ok               |
|          35 | -23.40%  | 197.09%            | -56.72% |    -0.13 |       78 | 42.26%     | ok               |
|          30 | -27.50%  | 197.09%            | -58.92% |    -0.19 |       80 | 42.76%     | ok               |
|          15 | -33.32%  | 197.09%            | -57.13% |    -0.21 |       78 | 50.75%     | ok               |

## LTC-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 9.57%    | -43.89%            | -34.94% |     0.31 |       64 | 45.59%     | ok               |
|          45 | 8.09%    | -43.89%            | -37.29% |     0.28 |       58 | 35.82%     | ok               |
|          30 | -2.49%   | -43.89%            | -32.83% |     0.17 |       68 | 52.87%     | ok               |
|          25 | -5.99%   | -43.89%            | -34.22% |     0.13 |       70 | 55.17%     | ok               |
|          40 | -10.45%  | -43.89%            | -40.31% |     0.03 |       56 | 41.19%     | ok               |

## MCD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 10.15%   | -10.33%            | -9.22%  |     0.48 |       46 | 24.96%     | ok               |
|          45 | 0.85%    | -10.33%            | -16.79% |     0.08 |       54 | 28.79%     | ok               |
|          30 | -0.16%   | -10.33%            | -21.88% |     0.05 |       77 | 40.60%     | ok               |
|          40 | -0.09%   | -10.33%            | -18.49% |     0.05 |       67 | 32.28%     | ok               |
|          25 | -1.74%   | -10.33%            | -23.62% |    -0    |       75 | 43.09%     | ok               |

## META Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -9.44%   | 57.67%             | -37.10% |    -0.05 |       66 | 40.10%     | ok               |
|          40 | -15.39%  | 57.67%             | -40.49% |    -0.16 |       68 | 43.09%     | ok               |
|          50 | -19.16%  | 57.67%             | -38.63% |    -0.27 |       68 | 35.77%     | ok               |
|          25 | -25.33%  | 57.67%             | -45.35% |    -0.32 |       75 | 52.91%     | ok               |
|          30 | -25.43%  | 57.67%             | -44.52% |    -0.34 |       74 | 50.25%     | ok               |

## MPC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 33.38%   | 175.49%            | -19.02% |     0.65 |       52 | 40.27%     | ok               |
|          40 | 31.19%   | 175.49%            | -20.88% |     0.6  |       62 | 46.92%     | ok               |
|          45 | 28.88%   | 175.49%            | -20.23% |     0.58 |       58 | 44.26%     | ok               |
|          35 | 29.47%   | 175.49%            | -31.08% |     0.56 |       68 | 49.42%     | ok               |
|          30 | 22.17%   | 175.49%            | -34.29% |     0.46 |       70 | 51.91%     | ok               |

## MRK Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -13.09%  | 12.41%             | -28.39% |    -0.16 |       83 | 51.91%     | ok               |
|          25 | -13.85%  | 12.41%             | -31.07% |    -0.2  |       70 | 44.09%     | ok               |
|          20 | -18.07%  | 12.41%             | -29.34% |    -0.29 |       75 | 47.42%     | ok               |
|          50 | -14.54%  | 12.41%             | -23.01% |    -0.3  |       56 | 28.45%     | ok               |
|          45 | -16.67%  | 12.41%             | -25.38% |    -0.33 |       57 | 31.78%     | ok               |

## MS Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 1.08%    | 80.18%             | -22.02% |     0.12 |       74 | 58.24%     | ok               |
|          40 | 0.47%    | 80.18%             | -19.99% |     0.09 |       72 | 39.27%     | ok               |
|          20 | -1.31%   | 80.18%             | -25.68% |     0.06 |       75 | 53.08%     | ok               |
|          30 | -6.43%   | 80.18%             | -27.79% |    -0.07 |       75 | 48.25%     | ok               |
|          25 | -7.87%   | 80.18%             | -28.36% |    -0.1  |       73 | 50.42%     | ok               |

## MSFT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -13.84%  | 23.96%             | -24.64% |    -0.3  |       74 | 37.60%     | ok               |
|          50 | -18.89%  | 23.96%             | -25.48% |    -0.48 |       64 | 31.95%     | ok               |
|          35 | -23.04%  | 23.96%             | -35.38% |    -0.5  |       75 | 46.59%     | ok               |
|          40 | -23.23%  | 23.96%             | -34.92% |    -0.53 |       73 | 41.43%     | ok               |
|          30 | -26.34%  | 23.96%             | -39.15% |    -0.57 |       83 | 51.41%     | ok               |

## MU Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 167.45%  | 623.89%            | -64.26% |     1.1  |       58 | 48.09%     | ok               |
|          15 | 193.10%  | 623.89%            | -61.96% |     1.09 |       51 | 59.57%     | ok               |
|          30 | 142.59%  | 623.89%            | -68.76% |     1.01 |       51 | 52.58%     | ok               |
|          25 | 141.16%  | 623.89%            | -67.90% |     0.99 |       51 | 54.08%     | ok               |
|          35 | 133.95%  | 623.89%            | -69.35% |     0.98 |       63 | 50.42%     | ok               |

## NEAR-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 189.00%  | 46.58%             | -38.74% |     1.3  |       28 | 22.03%     | ok               |
|          40 | 196.86%  | 46.58%             | -42.59% |     1.24 |       42 | 31.23%     | ok               |
|          45 | 149.14%  | 46.58%             | -38.08% |     1.09 |       44 | 27.20%     | ok               |
|          30 | 158.95%  | 46.58%             | -46.60% |     1.07 |       71 | 44.25%     | ok               |
|          35 | 139.03%  | 46.58%             | -52.37% |     1.04 |       64 | 35.82%     | ok               |

## NEM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 5.62%    | 163.18%            | -31.25% |     0.24 |       63 | 58.57%     | ok               |
|          20 | 4.83%    | 163.18%            | -30.50% |     0.23 |       70 | 54.08%     | ok               |
|          25 | -13.33%  | 163.18%            | -39.51% |    -0.03 |       66 | 51.91%     | ok               |
|          50 | -15.70%  | 163.18%            | -33.03% |    -0.11 |       52 | 38.27%     | ok               |
|          30 | -22.66%  | 163.18%            | -39.56% |    -0.19 |       70 | 50.08%     | ok               |

## NFLX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 31.00%   | 10.18%             | -16.28% |     0.78 |       44 | 33.28%     | ok               |
|          40 | 29.90%   | 10.18%             | -15.02% |     0.71 |       50 | 41.26%     | ok               |
|          35 | 25.48%   | 10.18%             | -18.30% |     0.6  |       74 | 45.92%     | ok               |
|          45 | 18.26%   | 10.18%             | -15.48% |     0.5  |       56 | 37.77%     | ok               |
|          15 | 11.82%   | 10.18%             | -26.59% |     0.32 |       71 | 65.06%     | ok               |

## NKE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -19.29%  | -61.84%            | -49.34% |    -0.15 |       83 | 53.91%     | ok               |
|          35 | -16.21%  | -61.84%            | -42.13% |    -0.15 |       71 | 40.43%     | ok               |
|          25 | -22.64%  | -61.84%            | -51.20% |    -0.21 |       83 | 51.25%     | ok               |
|          15 | -24.50%  | -61.84%            | -54.28% |    -0.23 |       86 | 57.74%     | ok               |
|          30 | -26.45%  | -61.84%            | -55.35% |    -0.28 |       79 | 46.92%     | ok               |

## NOW Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 11.00%   | -9.20%             | -30.43% |     0.3  |       80 | 50.25%     | ok               |
|          20 | 8.52%    | -9.20%             | -39.71% |     0.28 |       75 | 56.57%     | ok               |
|          25 | 5.77%    | -9.20%             | -37.51% |     0.25 |       72 | 53.74%     | ok               |
|          15 | 0.58%    | -9.20%             | -43.06% |     0.19 |       83 | 59.57%     | ok               |
|          40 | 1.17%    | -9.20%             | -36.21% |     0.17 |       72 | 39.43%     | ok               |

## NVDA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -36.15%  | 79.13%             | -43.07% |    -0.55 |       78 | 44.21%     | ok               |
|          20 | -44.64%  | 79.13%             | -44.64% |    -0.63 |       78 | 52.23%     | ok               |
|          25 | -44.55%  | 79.13%             | -44.55% |    -0.69 |       79 | 47.24%     | ok               |
|          15 | -50.12%  | 79.13%             | -53.39% |    -0.72 |       77 | 55.61%     | ok               |
|          35 | -45.75%  | 79.13%             | -51.52% |    -0.82 |       88 | 41.35%     | ok               |

## OP-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 23.99%   | -83.71%            | -30.20% |     0.5  |       32 | 9.20%      | ok               |
|          45 | 19.98%   | -83.71%            | -28.24% |     0.42 |       34 | 13.79%     | ok               |
|          40 | -5.98%   | -83.71%            | -43.36% |     0.11 |       46 | 22.03%     | ok               |
|          15 | -40.61%  | -83.71%            | -55.83% |    -0.21 |       74 | 44.44%     | ok               |
|          35 | -38.27%  | -83.71%            | -56.61% |    -0.36 |       56 | 26.63%     | ok               |

## ORCL Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 164.50%  | 4.78%              | -32.54% |     1.11 |       69 | 61.73%     | ok               |
|          25 | 112.66%  | 4.78%              | -27.76% |     0.92 |       61 | 54.24%     | ok               |
|          45 | 97.70%   | 4.78%              | -32.35% |     0.91 |       58 | 39.77%     | ok               |
|          35 | 102.60%  | 4.78%              | -31.95% |     0.9  |       62 | 48.42%     | ok               |
|          20 | 106.73%  | 4.78%              | -29.32% |     0.89 |       70 | 57.40%     | ok               |

## OXY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 2.59%    | -1.99%             | -28.48% |     0.17 |       73 | 42.76%     | ok               |
|          35 | 0.29%    | -1.99%             | -26.37% |     0.12 |       74 | 38.27%     | ok               |
|          50 | -2.04%   | -1.99%             | -26.34% |     0.06 |       46 | 27.29%     | ok               |
|          40 | -5.89%   | -1.99%             | -28.30% |    -0    |       64 | 34.11%     | ok               |
|          25 | -11.61%  | -1.99%             | -38.51% |    -0.08 |       79 | 46.42%     | ok               |

## PEP Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 15.10%   | -29.01%            | -11.62% |     0.64 |       38 | 25.12%     | ok               |
|          45 | 7.75%    | -29.01%            | -14.22% |     0.35 |       54 | 29.12%     | ok               |
|          35 | 4.59%    | -29.01%            | -21.42% |     0.21 |       75 | 39.43%     | ok               |
|          40 | 2.34%    | -29.01%            | -18.04% |     0.14 |       68 | 34.78%     | ok               |
|          30 | -2.09%   | -29.01%            | -21.35% |     0.01 |       76 | 45.76%     | ok               |

## PEPE-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -53.92%  | -71.06%            | -61.29% |    -0.4  |       83 | 48.28%     | ok               |
|          15 | -65.36%  | -71.06%            | -67.32% |    -0.45 |       80 | 62.64%     | ok               |
|          20 | -61.97%  | -71.06%            | -64.13% |    -0.47 |       86 | 59.20%     | ok               |
|          25 | -59.85%  | -71.06%            | -64.26% |    -0.49 |       93 | 53.26%     | ok               |
|          35 | -55.48%  | -71.06%            | -61.54% |    -0.53 |       72 | 43.30%     | ok               |

## PFE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -15.89%  | -1.32%             | -23.37% |    -0.5  |       52 | 21.63%     | ok               |
|          40 | -17.46%  | -1.32%             | -27.08% |    -0.53 |       72 | 26.62%     | ok               |
|          50 | -16.36%  | -1.32%             | -25.42% |    -0.57 |       40 | 18.47%     | ok               |
|          35 | -25.41%  | -1.32%             | -32.87% |    -0.78 |       82 | 33.11%     | ok               |
|          30 | -36.54%  | -1.32%             | -41.77% |    -1.16 |       81 | 36.61%     | ok               |

## PG Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -11.00%  | -6.72%             | -17.50% |    -0.44 |       54 | 27.62%     | ok               |
|          35 | -16.30%  | -6.72%             | -18.57% |    -0.66 |       62 | 31.28%     | ok               |
|          45 | -20.11%  | -6.72%             | -19.90% |    -0.94 |       54 | 24.96%     | ok               |
|          30 | -23.91%  | -6.72%             | -24.16% |    -0.97 |       64 | 34.44%     | ok               |
|          25 | -25.68%  | -6.72%             | -25.50% |    -1.05 |       74 | 35.77%     | ok               |

## PM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | -5.54%   | 103.40%            | -32.20% |    -0.04 |       84 | 46.59%     | ok               |
|          20 | -8.01%   | 103.40%            | -33.51% |    -0.08 |       83 | 55.24%     | ok               |
|          30 | -8.51%   | 103.40%            | -35.15% |    -0.1  |       79 | 50.08%     | ok               |
|          40 | -12.75%  | 103.40%            | -37.94% |    -0.25 |       78 | 42.60%     | ok               |
|          50 | -12.29%  | 103.40%            | -35.70% |    -0.25 |       68 | 36.77%     | ok               |

## POL-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 52.93%   | -63.39%            | -38.69% |     0.68 |       77 | 49.62%     | ok               |
|          25 | 26.64%   | -63.39%            | -38.69% |     0.47 |       71 | 54.98%     | ok               |
|          20 | 19.03%   | -63.39%            | -42.81% |     0.41 |       79 | 58.43%     | ok               |
|          40 | 3.00%    | -63.39%            | -31.98% |     0.22 |       58 | 31.03%     | ok               |
|          15 | -7.46%   | -63.39%            | -47.86% |     0.16 |       84 | 62.07%     | ok               |

## QCOM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -11.57%  | -14.94%            | -54.50% |     0.03 |       71 | 45.26%     | ok               |
|          20 | -18.07%  | -14.94%            | -54.38% |    -0.05 |       67 | 48.59%     | ok               |
|          35 | -19.04%  | -14.94%            | -50.58% |    -0.09 |       79 | 40.93%     | ok               |
|          15 | -27.97%  | -14.94%            | -57.94% |    -0.19 |       69 | 51.25%     | ok               |
|          30 | -28.49%  | -14.94%            | -56.59% |    -0.23 |       77 | 43.43%     | ok               |

## QQQ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 22.09%   | 59.96%             | -14.17% |     0.56 |       63 | 54.08%     | ok               |
|          25 | 13.81%   | 59.96%             | -12.88% |     0.42 |       61 | 48.09%     | ok               |
|          20 | 12.65%   | 59.96%             | -12.98% |     0.38 |       69 | 50.75%     | ok               |
|          30 | 6.13%    | 59.96%             | -14.20% |     0.24 |       66 | 46.09%     | ok               |
|          35 | -4.78%   | 59.96%             | -20.59% |    -0.06 |       72 | 42.26%     | ok               |

## RENDER-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 20.64%   | -64.09%            | -44.59% |     0.45 |       82 | 61.69%     | ok               |
|          20 | 18.08%   | -64.09%            | -43.43% |     0.43 |       85 | 58.43%     | ok               |
|          25 | 12.62%   | -64.09%            | -42.48% |     0.39 |       85 | 53.45%     | ok               |
|          30 | -28.15%  | -64.09%            | -45.92% |    -0.04 |       90 | 47.32%     | ok               |
|          35 | -38.09%  | -64.09%            | -49.04% |    -0.23 |       86 | 40.80%     | ok               |

## RTX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 42.25%   | 75.40%             | -18.66% |     0.87 |       74 | 57.24%     | ok               |
|          25 | 37.39%   | 75.40%             | -18.59% |     0.8  |       62 | 54.58%     | ok               |
|          15 | 33.66%   | 75.40%             | -19.55% |     0.72 |       67 | 61.73%     | ok               |
|          30 | 26.93%   | 75.40%             | -16.99% |     0.63 |       66 | 52.08%     | ok               |
|          35 | 21.79%   | 75.40%             | -18.00% |     0.59 |       58 | 48.75%     | ok               |

## SBUX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | 0.58%    | 15.52%             | -23.55% |     0.11 |       55 | 40.43%     | ok               |
|          40 | -4.35%   | 15.52%             | -25.43% |    -0.02 |       60 | 32.28%     | ok               |
|          45 | -6.16%   | 15.52%             | -27.26% |    -0.08 |       66 | 27.45%     | ok               |
|          35 | -8.64%   | 15.52%             | -26.54% |    -0.1  |       58 | 35.44%     | ok               |
|          20 | -11.41%  | 15.52%             | -30.94% |    -0.13 |       58 | 42.43%     | ok               |

## SCHW Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -3.59%   | 28.60%             | -28.76% |     0    |       65 | 48.59%     | ok               |
|          45 | -2.78%   | 28.60%             | -16.53% |    -0.02 |       60 | 30.62%     | ok               |
|          50 | -4.01%   | 28.60%             | -13.28% |    -0.09 |       52 | 27.62%     | ok               |
|          20 | -8.54%   | 28.60%             | -29.24% |    -0.11 |       75 | 51.08%     | ok               |
|          40 | -11.19%  | 28.60%             | -23.35% |    -0.26 |       70 | 35.27%     | ok               |

## SHIB-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | -18.75%  | -68.47%            | -44.56% |    -0.07 |       71 | 46.55%     | ok               |
|          40 | -19.36%  | -68.47%            | -41.14% |    -0.1  |       60 | 38.70%     | ok               |
|          25 | -26.58%  | -68.47%            | -43.17% |    -0.15 |       80 | 58.24%     | ok               |
|          15 | -28.16%  | -68.47%            | -45.04% |    -0.15 |       86 | 66.67%     | ok               |
|          20 | -28.25%  | -68.47%            | -45.88% |    -0.16 |       80 | 61.88%     | ok               |

## SHY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd    |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:-------|---------:|---------:|:-----------|:-----------------|
|          30 | -1.75%   | -0.26%             | -3.18% |    -0.58 |       48 | 37.10%     | ok               |
|          35 | -2.27%   | -0.26%             | -3.49% |    -0.78 |       52 | 35.44%     | ok               |
|          40 | -2.41%   | -0.26%             | -3.58% |    -0.83 |       54 | 33.94%     | ok               |
|          25 | -2.78%   | -0.26%             | -4.32% |    -0.91 |       60 | 39.77%     | ok               |
|          15 | -3.00%   | -0.26%             | -4.64% |    -0.93 |       61 | 45.42%     | ok               |

## SKY-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | -57.70%  | -7.75%             | -61.02% |    -0.95 |       82 | 36.59%     | ok               |
|          15 | -64.85%  | -7.75%             | -67.57% |    -0.96 |       77 | 53.83%     | ok               |
|          30 | -62.61%  | -7.75%             | -64.59% |    -1.04 |       89 | 44.06%     | ok               |
|          45 | -59.92%  | -7.75%             | -63.07% |    -1.11 |       76 | 28.16%     | ok               |
|          25 | -66.16%  | -7.75%             | -67.81% |    -1.12 |       82 | 47.13%     | ok               |

## SLB Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 2.44%    | 4.37%              | -28.43% |     0.15 |       48 | 34.94%     | ok               |
|          45 | 2.13%    | 4.37%              | -25.36% |     0.15 |       60 | 31.45%     | ok               |
|          50 | -9.63%   | 4.37%              | -30.58% |    -0.14 |       50 | 25.96%     | ok               |
|          35 | -23.73%  | 4.37%              | -47.32% |    -0.4  |       72 | 42.76%     | ok               |
|          25 | -35.11%  | 4.37%              | -55.67% |    -0.62 |       84 | 53.08%     | ok               |

## SLV Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 50.67%   | 77.96%             | -34.04% |     0.72 |       54 | 30.12%     | ok               |
|          45 | 37.88%   | 77.96%             | -31.75% |     0.6  |       65 | 31.61%     | ok               |
|          40 | 36.79%   | 77.96%             | -34.28% |     0.59 |       69 | 33.61%     | ok               |
|          20 | 25.58%   | 77.96%             | -42.60% |     0.46 |       72 | 43.93%     | ok               |
|          15 | 25.56%   | 77.96%             | -47.98% |     0.46 |       73 | 48.75%     | ok               |

## SMH Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 66.04%   | 138.70%            | -31.66% |     0.94 |       47 | 46.76%     | ok               |
|          25 | 51.03%   | 138.70%            | -33.57% |     0.81 |       44 | 45.26%     | ok               |
|          35 | 49.42%   | 138.70%            | -34.65% |     0.8  |       54 | 42.26%     | ok               |
|          30 | 46.91%   | 138.70%            | -34.29% |     0.77 |       48 | 43.93%     | ok               |
|          45 | 36.22%   | 138.70%            | -33.35% |     0.69 |       54 | 36.44%     | ok               |

## SNX-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 15.93%   | -75.31%            | -41.29% |     0.38 |       54 | 27.01%     | ok               |
|          40 | 15.94%   | -75.31%            | -28.61% |     0.38 |       42 | 22.03%     | ok               |
|          20 | -5.20%   | -75.31%            | -53.03% |     0.19 |       73 | 43.87%     | ok               |
|          30 | -5.62%   | -75.31%            | -50.74% |     0.15 |       64 | 33.72%     | ok               |
|          50 | -9.36%   | -75.31%            | -29.88% |    -0.04 |       38 | 13.79%     | ok               |

## SOL-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 40.31%   | -40.90%            | -38.17% |     0.61 |       58 | 40.61%     | ok               |
|          35 | 16.92%   | -40.90%            | -43.70% |     0.39 |       70 | 47.13%     | ok               |
|          45 | 5.67%    | -40.90%            | -46.83% |     0.26 |       62 | 34.87%     | ok               |
|          25 | -4.61%   | -40.90%            | -41.09% |     0.18 |       70 | 57.66%     | ok               |
|          30 | -7.24%   | -40.90%            | -45.53% |     0.14 |       78 | 53.26%     | ok               |

## SOXX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | 62.87%   | 120.80%            | -39.32% |     0.88 |       53 | 45.09%     | ok               |
|          35 | 59.20%   | 120.80%            | -38.76% |     0.87 |       56 | 40.60%     | ok               |
|          30 | 58.34%   | 120.80%            | -39.81% |     0.85 |       54 | 42.93%     | ok               |
|          20 | 48.49%   | 120.80%            | -39.19% |     0.73 |       59 | 46.09%     | ok               |
|          40 | 39.73%   | 120.80%            | -41.03% |     0.67 |       58 | 38.44%     | ok               |

## SPY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 11.01%   | 45.25%             | -14.25% |     0.41 |       59 | 53.08%     | ok               |
|          15 | 10.48%   | 45.25%             | -16.80% |     0.39 |       63 | 55.74%     | ok               |
|          25 | 6.02%    | 45.25%             | -14.25% |     0.26 |       59 | 52.08%     | ok               |
|          30 | -0.13%   | 45.25%             | -15.53% |     0.06 |       64 | 49.42%     | ok               |
|          35 | -1.10%   | 45.25%             | -15.58% |     0.02 |       62 | 46.26%     | ok               |

## SUSHI-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -6.33%   | -73.45%            | -34.75% |     0.08 |       54 | 16.86%     | ok               |
|          45 | -41.81%  | -73.45%            | -57.99% |    -0.49 |       56 | 21.65%     | ok               |
|          40 | -46.31%  | -73.45%            | -60.82% |    -0.52 |       59 | 28.16%     | ok               |
|          35 | -64.61%  | -73.45%            | -72.78% |    -0.87 |       80 | 33.33%     | ok               |
|          15 | -71.79%  | -73.45%            | -75.07% |    -0.87 |       90 | 49.43%     | ok               |

## T Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 64.68%   | 31.71%             | -15.08% |     1.08 |       73 | 65.56%     | ok               |
|          20 | 60.62%   | 31.71%             | -18.13% |     1.06 |       68 | 61.06%     | ok               |
|          25 | 58.79%   | 31.71%             | -17.66% |     1.05 |       68 | 58.90%     | ok               |
|          30 | 44.01%   | 31.71%             | -17.01% |     0.86 |       72 | 56.74%     | ok               |
|          35 | 28.31%   | 31.71%             | -14.49% |     0.64 |       78 | 52.41%     | ok               |

## TGT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -11.06%  | 8.40%              | -34.42% |    -0.16 |       60 | 37.60%     | ok               |
|          45 | -11.97%  | 8.40%              | -25.85% |    -0.23 |       48 | 28.62%     | ok               |
|          20 | -16.69%  | 8.40%              | -38.96% |    -0.25 |       88 | 45.42%     | ok               |
|          25 | -15.22%  | 8.40%              | -37.81% |    -0.25 |       70 | 40.77%     | ok               |
|          35 | -17.42%  | 8.40%              | -32.35% |    -0.35 |       60 | 33.94%     | ok               |

## TIA-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -36.46%  | -83.22%            | -66.82% |     0    |       96 | 59.00%     | ok               |
|          25 | -39.64%  | -83.22%            | -69.36% |    -0.1  |       92 | 48.28%     | ok               |
|          35 | -33.32%  | -83.22%            | -66.58% |    -0.17 |       74 | 35.44%     | ok               |
|          20 | -49.48%  | -83.22%            | -71.87% |    -0.2  |       91 | 53.64%     | ok               |
|          30 | -52.01%  | -83.22%            | -75.93% |    -0.32 |       93 | 42.91%     | ok               |

## TLT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -11.35%  | -13.97%            | -13.26% |    -1.22 |       36 | 17.64%     | ok               |
|          40 | -16.20%  | -13.97%            | -17.65% |    -1.41 |       54 | 25.12%     | ok               |
|          30 | -20.13%  | -13.97%            | -21.85% |    -1.51 |       68 | 33.78%     | ok               |
|          45 | -14.83%  | -13.97%            | -15.76% |    -1.51 |       46 | 20.63%     | ok               |
|          35 | -20.62%  | -13.97%            | -21.68% |    -1.72 |       66 | 28.95%     | ok               |

## TMO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 55.30%   | 13.95%             | -8.17%  |     1.14 |       48 | 34.94%     | ok               |
|          45 | 43.49%   | 13.95%             | -9.69%  |     0.92 |       54 | 39.77%     | ok               |
|          40 | 37.17%   | 13.95%             | -9.91%  |     0.8  |       59 | 44.76%     | ok               |
|          35 | 35.82%   | 13.95%             | -13.84% |     0.73 |       69 | 50.08%     | ok               |
|          20 | 30.99%   | 13.95%             | -22.89% |     0.61 |       78 | 60.73%     | ok               |

## TMUS Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -3.97%   | -4.66%             | -32.44% |     0.01 |       74 | 47.92%     | ok               |
|          15 | -9.63%   | -4.66%             | -40.53% |    -0.09 |       68 | 60.57%     | ok               |
|          50 | -7.84%   | -4.66%             | -32.38% |    -0.14 |       60 | 34.44%     | ok               |
|          25 | -13.12%  | -4.66%             | -38.76% |    -0.19 |       77 | 50.92%     | ok               |
|          20 | -14.84%  | -4.66%             | -39.27% |    -0.22 |       74 | 54.91%     | ok               |

## TRX-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 10.42%   | 21.71%             | -18.79% |     0.39 |       54 | 39.66%     | ok               |
|          35 | 3.94%    | 21.71%             | -21.77% |     0.2  |       66 | 47.89%     | ok               |
|          20 | 1.51%    | 21.71%             | -25.45% |     0.13 |       61 | 57.66%     | ok               |
|          30 | 1.44%    | 21.71%             | -22.90% |     0.12 |       66 | 50.77%     | ok               |
|          45 | 0.73%    | 21.71%             | -22.76% |     0.1  |       46 | 36.02%     | ok               |

## TSLA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 41.47%   | 103.85%            | -30.57% |     0.6  |       64 | 30.12%     | ok               |
|          40 | 13.71%   | 103.85%            | -50.11% |     0.34 |       63 | 35.61%     | ok               |
|          45 | -10.53%  | 103.85%            | -52.01% |     0.07 |       69 | 32.61%     | ok               |
|          35 | -20.51%  | 103.85%            | -60.12% |    -0.03 |       76 | 38.10%     | ok               |
|          30 | -37.10%  | 103.85%            | -59.64% |    -0.26 |       80 | 42.93%     | ok               |

## TXN Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 4.24%    | 38.57%             | -44.65% |     0.19 |       68 | 32.78%     | ok               |
|          35 | -14.88%  | 38.57%             | -42.44% |    -0.11 |       78 | 47.25%     | ok               |
|          40 | -16.37%  | 38.57%             | -44.87% |    -0.14 |       74 | 44.93%     | ok               |
|          20 | -20.19%  | 38.57%             | -37.58% |    -0.15 |       68 | 56.91%     | ok               |
|          45 | -17.45%  | 38.57%             | -45.45% |    -0.17 |       82 | 38.77%     | ok               |

## UNH Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 28.33%   | -24.12%            | -36.92% |     0.52 |       56 | 28.45%     | ok               |
|          30 | 27.70%   | -24.12%            | -26.31% |     0.5  |       77 | 48.42%     | ok               |
|          35 | 23.81%   | -24.12%            | -27.21% |     0.45 |       72 | 43.43%     | ok               |
|          20 | 23.64%   | -24.12%            | -26.96% |     0.44 |       80 | 57.74%     | ok               |
|          15 | 23.60%   | -24.12%            | -26.07% |     0.44 |       85 | 63.89%     | ok               |

## UNI-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 92.10%   | 1.00%              | -25.49% |     0.95 |       50 | 26.44%     | ok               |
|          45 | 75.83%   | 1.00%              | -34.45% |     0.81 |       56 | 33.91%     | ok               |
|          40 | 51.27%   | 1.00%              | -47.29% |     0.65 |       60 | 38.89%     | ok               |
|          35 | 32.67%   | 1.00%              | -54.44% |     0.52 |       70 | 44.44%     | ok               |
|          20 | -38.44%  | 1.00%              | -74.63% |    -0.08 |       93 | 59.77%     | ok               |

## UPS Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | -28.34%  | -33.38%            | -31.52% |    -0.53 |       62 | 36.44%     | ok               |
|          40 | -28.13%  | -33.38%            | -31.55% |    -0.53 |       58 | 30.95%     | ok               |
|          20 | -34.60%  | -33.38%            | -38.74% |    -0.64 |       84 | 50.25%     | ok               |
|          25 | -35.12%  | -33.38%            | -39.23% |    -0.67 |       76 | 46.92%     | ok               |
|          15 | -36.91%  | -33.38%            | -40.91% |    -0.69 |       86 | 54.08%     | ok               |

## USO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 5.24%    | 105.10%            | -42.94% |     0.22 |       69 | 41.26%     | ok               |
|          45 | 5.79%    | 105.10%            | -33.44% |     0.22 |       48 | 25.79%     | ok               |
|          20 | 4.37%    | 105.10%            | -44.30% |     0.21 |       74 | 37.77%     | ok               |
|          25 | -4.18%   | 105.10%            | -45.85% |     0.08 |       68 | 35.27%     | ok               |
|          50 | -3.42%   | 105.10%            | -29.54% |     0.07 |       52 | 24.13%     | ok               |

## VEA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 8.44%    | 37.06%             | -15.99% |     0.35 |       54 | 50.08%     | ok               |
|          20 | 2.14%    | 37.06%             | -17.04% |     0.14 |       59 | 47.42%     | ok               |
|          25 | -1.76%   | 37.06%             | -17.13% |    -0.02 |       57 | 45.42%     | ok               |
|          30 | -3.76%   | 37.06%             | -17.27% |    -0.1  |       62 | 42.43%     | ok               |
|          35 | -4.45%   | 37.06%             | -16.11% |    -0.14 |       52 | 40.60%     | ok               |

## VIXY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -56.48%  | -63.69%            | -69.78% |    -0.67 |       36 | 9.32%      | ok               |
|          15 | -77.62%  | -63.69%            | -89.47% |    -0.81 |       95 | 43.26%     | ok               |
|          45 | -65.81%  | -63.69%            | -75.03% |    -0.88 |       56 | 14.31%     | ok               |
|          30 | -78.27%  | -63.69%            | -88.17% |    -0.95 |       94 | 32.28%     | ok               |
|          40 | -73.17%  | -63.69%            | -80.72% |    -1    |       68 | 18.14%     | ok               |

## VNQ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -9.63%   | 8.07%              | -19.07% |    -0.43 |       62 | 28.29%     | ok               |
|          25 | -11.79%  | 8.07%              | -22.34% |    -0.44 |       71 | 42.60%     | ok               |
|          50 | -10.52%  | 8.07%              | -17.13% |    -0.49 |       54 | 24.96%     | ok               |
|          30 | -14.48%  | 8.07%              | -24.92% |    -0.58 |       73 | 39.77%     | ok               |
|          20 | -16.29%  | 8.07%              | -24.00% |    -0.63 |       76 | 45.26%     | ok               |

## VTI Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 11.93%   | 43.73%             | -13.96% |     0.44 |       62 | 53.58%     | ok               |
|          15 | 7.33%    | 43.73%             | -15.70% |     0.3  |       59 | 55.91%     | ok               |
|          25 | -0.01%   | 43.73%             | -15.00% |     0.06 |       58 | 51.41%     | ok               |
|          30 | -7.51%   | 43.73%             | -17.64% |    -0.22 |       68 | 49.42%     | ok               |
|          40 | -8.63%   | 43.73%             | -19.77% |    -0.29 |       72 | 41.93%     | ok               |

## VWO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -10.47%  | 32.66%             | -22.18% |    -0.4  |       56 | 28.29%     | ok               |
|          15 | -13.58%  | 32.66%             | -24.01% |    -0.44 |       74 | 46.59%     | ok               |
|          45 | -11.66%  | 32.66%             | -23.75% |    -0.45 |       58 | 30.95%     | ok               |
|          40 | -12.12%  | 32.66%             | -23.57% |    -0.46 |       68 | 33.78%     | ok               |
|          20 | -14.95%  | 32.66%             | -26.14% |    -0.51 |       71 | 44.26%     | ok               |

## VZ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -3.10%   | 11.64%             | -12.96% |    -0.04 |       56 | 28.62%     | ok               |
|          20 | -22.26%  | 11.64%             | -35.02% |    -0.45 |       78 | 51.08%     | ok               |
|          25 | -19.09%  | 11.64%             | -24.83% |    -0.5  |       81 | 46.09%     | ok               |
|          35 | -19.34%  | 11.64%             | -25.86% |    -0.57 |       64 | 38.44%     | ok               |
|          45 | -18.75%  | 11.64%             | -24.80% |    -0.57 |       70 | 32.78%     | ok               |

## WFC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | -8.71%   | 32.78%             | -21.57% |    -0.12 |       77 | 44.09%     | ok               |
|          50 | -6.21%   | 32.78%             | -18.29% |    -0.13 |       58 | 32.61%     | ok               |
|          20 | -19.73%  | 32.78%             | -29.87% |    -0.3  |       79 | 52.75%     | ok               |
|          30 | -18.22%  | 32.78%             | -28.90% |    -0.3  |       80 | 47.25%     | ok               |
|          40 | -14.36%  | 32.78%             | -23.94% |    -0.35 |       72 | 40.77%     | ok               |

## WIF-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 3.70%    | -83.08%            | -40.67% |     0.31 |       69 | 44.44%     | ok               |
|          25 | -6.88%   | -83.08%            | -44.74% |     0.21 |       67 | 40.42%     | ok               |
|          15 | -18.96%  | -83.08%            | -46.21% |     0.12 |       79 | 47.70%     | ok               |
|          50 | -8.68%   | -83.08%            | -35.47% |     0.02 |       36 | 13.41%     | ok               |
|          30 | -26.73%  | -83.08%            | -52.76% |    -0.01 |       68 | 37.74%     | ok               |

## WMT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 35.70%   | 78.02%             | -12.18% |     1.09 |       36 | 37.10%     | ok               |
|          45 | 34.57%   | 78.02%             | -14.14% |     1.01 |       42 | 39.43%     | ok               |
|          35 | 24.75%   | 78.02%             | -18.25% |     0.73 |       58 | 45.76%     | ok               |
|          40 | 23.14%   | 78.02%             | -18.53% |     0.71 |       50 | 41.10%     | ok               |
|          15 | 6.43%    | 78.02%             | -26.24% |     0.23 |       82 | 59.73%     | ok               |

## XBI Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 10.06%   | 59.24%             | -16.08% |     0.33 |       54 | 34.28%     | ok               |
|          45 | 5.89%    | 59.24%             | -15.46% |     0.23 |       52 | 31.78%     | ok               |
|          35 | -0.56%   | 59.24%             | -17.66% |     0.07 |       62 | 37.10%     | ok               |
|          30 | -2.63%   | 59.24%             | -17.66% |     0.02 |       64 | 38.60%     | ok               |
|          50 | -3.05%   | 59.24%             | -15.41% |    -0.01 |       52 | 28.79%     | ok               |

## XLB Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -3.04%   | 8.71%              | -15.73% |    -0.08 |       40 | 21.96%     | ok               |
|          40 | -3.93%   | 8.71%              | -17.29% |    -0.1  |       56 | 26.12%     | ok               |
|          45 | -6.51%   | 8.71%              | -17.09% |    -0.22 |       44 | 23.63%     | ok               |
|          35 | -7.19%   | 8.71%              | -20.65% |    -0.23 |       56 | 29.62%     | ok               |
|          25 | -11.51%  | 8.71%              | -22.60% |    -0.38 |       64 | 35.77%     | ok               |

## XLC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 12.62%   | 33.78%             | -12.33% |     0.47 |       61 | 50.25%     | ok               |
|          25 | 12.06%   | 33.78%             | -12.31% |     0.45 |       60 | 52.41%     | ok               |
|          50 | 7.23%    | 33.78%             | -11.12% |     0.38 |       64 | 38.44%     | ok               |
|          40 | 7.80%    | 33.78%             | -13.38% |     0.34 |       62 | 43.93%     | ok               |
|          35 | 7.08%    | 33.78%             | -13.38% |     0.31 |       60 | 47.75%     | ok               |

## XLE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 1.79%    | 46.89%             | -25.98% |     0.13 |       56 | 36.61%     | ok               |
|          35 | -1.38%   | 46.89%             | -26.89% |     0.05 |       65 | 43.09%     | ok               |
|          45 | -1.57%   | 46.89%             | -28.46% |     0.03 |       60 | 38.77%     | ok               |
|          30 | -3.00%   | 46.89%             | -30.31% |     0.01 |       69 | 45.26%     | ok               |
|          25 | -6.94%   | 46.89%             | -33.14% |    -0.08 |       80 | 48.25%     | ok               |

## XLF Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -2.48%   | 30.00%             | -18.63% |    -0.02 |       74 | 51.75%     | ok               |
|          15 | -4.00%   | 30.00%             | -20.19% |    -0.07 |       78 | 54.58%     | ok               |
|          25 | -9.28%   | 30.00%             | -23.22% |    -0.28 |       81 | 48.59%     | ok               |
|          30 | -9.88%   | 30.00%             | -23.61% |    -0.31 |       82 | 46.59%     | ok               |
|          35 | -16.89%  | 30.00%             | -24.48% |    -0.65 |       72 | 42.93%     | ok               |

## XLI Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 5.22%    | 33.30%             | -11.40% |     0.23 |       86 | 51.41%     | ok               |
|          20 | 1.42%    | 33.30%             | -12.74% |     0.11 |       75 | 46.42%     | ok               |
|          50 | -4.76%   | 33.30%             | -14.94% |    -0.18 |       60 | 31.78%     | ok               |
|          45 | -5.38%   | 33.30%             | -16.29% |    -0.19 |       70 | 34.28%     | ok               |
|          25 | -8.78%   | 33.30%             | -17.03% |    -0.29 |       78 | 44.43%     | ok               |

## XLK Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 68.27%   | 77.03%             | -14.75% |     1.13 |       45 | 51.91%     | ok               |
|          20 | 64.09%   | 77.03%             | -14.75% |     1.12 |       46 | 49.75%     | ok               |
|          25 | 58.34%   | 77.03%             | -14.75% |     1.08 |       42 | 47.75%     | ok               |
|          30 | 48.86%   | 77.03%             | -14.75% |     0.97 |       42 | 46.42%     | ok               |
|          35 | 30.44%   | 77.03%             | -14.69% |     0.7  |       56 | 43.59%     | ok               |

## XLM-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | 5.75%    | -42.42%            | -49.14% |     0.28 |       70 | 49.62%     | ok               |
|          40 | 0.06%    | -42.42%            | -47.28% |     0.2  |       52 | 36.78%     | ok               |
|          50 | 0.51%    | -42.42%            | -48.81% |     0.19 |       42 | 26.63%     | ok               |
|          30 | -3.52%   | -42.42%            | -54.58% |     0.18 |       68 | 47.51%     | ok               |
|          45 | -2.81%   | -42.42%            | -51.28% |     0.15 |       54 | 31.42%     | ok               |

## XLP Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 12.03%   | 10.59%             | -5.66%  |     0.74 |       54 | 29.45%     | ok               |
|          40 | 9.78%    | 10.59%             | -7.77%  |     0.59 |       70 | 33.61%     | ok               |
|          50 | 8.07%    | 10.59%             | -6.08%  |     0.53 |       60 | 27.29%     | ok               |
|          35 | 8.82%    | 10.59%             | -9.73%  |     0.53 |       66 | 36.61%     | ok               |
|          30 | 5.67%    | 10.59%             | -10.28% |     0.35 |       67 | 38.44%     | ok               |

## XLU Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 5.26%    | 15.87%             | -14.03% |     0.29 |       54 | 30.28%     | ok               |
|          45 | 4.10%    | 15.87%             | -14.97% |     0.24 |       58 | 31.45%     | ok               |
|          40 | 1.07%    | 15.87%             | -16.41% |     0.09 |       64 | 33.44%     | ok               |
|          35 | -1.62%   | 15.87%             | -19.71% |    -0.03 |       64 | 36.11%     | ok               |
|          30 | -5.88%   | 15.87%             | -20.40% |    -0.21 |       69 | 39.60%     | ok               |

## XLV Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -22.16%  | 18.74%             | -22.40% |    -1.05 |       76 | 38.44%     | ok               |
|          30 | -22.52%  | 18.74%             | -22.75% |    -1.09 |       76 | 36.77%     | ok               |
|          15 | -25.38%  | 18.74%             | -24.70% |    -1.19 |       83 | 42.60%     | ok               |
|          20 | -25.21%  | 18.74%             | -24.54% |    -1.21 |       79 | 40.10%     | ok               |
|          35 | -26.38%  | 18.74%             | -26.58% |    -1.38 |       70 | 33.78%     | ok               |

## XLY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -0.70%   | 26.24%             | -15.77% |     0.06 |       76 | 54.24%     | ok               |
|          30 | -4.15%   | 26.24%             | -18.35% |    -0.06 |       75 | 47.59%     | ok               |
|          20 | -5.95%   | 26.24%             | -19.25% |    -0.1  |       72 | 50.92%     | ok               |
|          25 | -8.05%   | 26.24%             | -19.98% |    -0.17 |       69 | 49.42%     | ok               |
|          50 | -6.34%   | 26.24%             | -15.82% |    -0.22 |       62 | 32.11%     | ok               |

## XOM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | 2.73%    | 53.28%             | -19.90% |     0.15 |       55 | 34.94%     | ok               |
|          50 | 1.92%    | 53.28%             | -21.35% |     0.13 |       38 | 27.12%     | ok               |
|          30 | 1.71%    | 53.28%             | -20.29% |     0.12 |       55 | 34.28%     | ok               |
|          20 | -3.12%   | 53.28%             | -25.56% |    -0.01 |       62 | 37.27%     | ok               |
|          45 | -3.17%   | 53.28%             | -23.33% |    -0.02 |       42 | 28.29%     | ok               |

## XRP-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 18.98%   | -48.50%            | -31.38% |     0.41 |       72 | 42.91%     | ok               |
|          40 | 0.50%    | -48.50%            | -33.91% |     0.2  |       66 | 36.40%     | ok               |
|          30 | -11.06%  | -48.50%            | -31.82% |     0.07 |       67 | 47.89%     | ok               |
|          45 | -10.66%  | -48.50%            | -37.18% |     0.04 |       60 | 31.80%     | ok               |
|          50 | -14.45%  | -48.50%            | -39.26% |    -0.04 |       58 | 24.14%     | ok               |

## YFI-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -46.87%  | -64.32%            | -48.06% |    -0.8  |       52 | 27.20%     | ok               |
|          45 | -43.92%  | -64.32%            | -43.92% |    -0.9  |       64 | 22.22%     | ok               |
|          35 | -54.22%  | -64.32%            | -55.25% |    -0.95 |       62 | 34.10%     | ok               |
|          50 | -46.03%  | -64.32%            | -46.03% |    -1.07 |       48 | 16.86%     | ok               |
|          25 | -64.03%  | -64.32%            | -66.41% |    -1.18 |       78 | 42.34%     | ok               |

## ZEC-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 188.15%  | 2382.94%           | -30.64% |     1.04 |       46 | 32.38%     | ok               |
|          35 | 150.02%  | 2382.94%           | -50.84% |     0.93 |       52 | 37.93%     | ok               |
|          30 | 132.91%  | 2382.94%           | -56.50% |     0.88 |       59 | 41.38%     | ok               |
|          25 | 123.48%  | 2382.94%           | -58.07% |     0.85 |       57 | 43.87%     | ok               |
|          40 | 111.90%  | 2382.94%           | -54.22% |     0.82 |       54 | 35.82%     | ok               |
