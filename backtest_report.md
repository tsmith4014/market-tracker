# Market Tracker Backtest Report

_Generated: 2026-10-06T06:25:04+00:00_

## Data Sources

- Crypto: Kraken -> Coinbase -> CoinGecko OHLC -> CoinPaprika fallback chain.
- Stocks / ETFs / indices: Stooq -> Yahoo Finance fallback chain.
- Data rows are generated from real market APIs. Mock OHLCV rows are not generated.

## Data Freshness

- Rows: **92,724**
- Symbols: **161**
- Date range: **2024-05-13** to **2026-10-06**

## Latest Signals

| symbol     | date                |         close |   composite_score | signal   | data_source   |
|:-----------|:--------------------|--------------:|------------------:|:---------|:--------------|
| AAPL       | 2026-10-05 00:00:00 |   332.89      |        54.0833    | LONG     | Yahoo Finance |
| AAVE-USD   | 2026-10-06 00:00:00 |   181.44      |        69.1667    | LONG     | Kraken API    |
| ADA-USD    | 2026-10-06 00:00:00 |     0.26717   |        59.6667    | LONG     | Kraken API    |
| ALGO-USD   | 2026-10-06 00:00:00 |     0.1275    |        61.8333    | LONG     | Kraken API    |
| AMAT       | 2026-10-05 00:00:00 |   542.28      |        77         | LONG     | Yahoo Finance |
| AMD        | 2026-10-05 00:00:00 |   631.75      |        71.25      | LONG     | Yahoo Finance |
| AMGN       | 2026-10-05 00:00:00 |   402.98      |        54.0833    | LONG     | Yahoo Finance |
| AVAX-USD   | 2026-10-06 00:00:00 |    11.221     |        41.6667    | LONG     | Kraken API    |
| BCH-USD    | 2026-10-06 00:00:00 |   315.28      |        36.3333    | LONG     | Kraken API    |
| BITO       | 2026-10-05 00:00:00 |    11.44      |        61.9167    | LONG     | Yahoo Finance |
| BONK-USD   | 2026-10-06 00:00:00 |     3.742e-06 |        37.6667    | LONG     | Kraken API    |
| BTC-USD    | 2026-10-06 00:00:00 | 85380.1       |        34.6667    | LONG     | Kraken API    |
| COMP-USD   | 2026-10-06 00:00:00 |    24.39      |        50.3333    | LONG     | Kraken API    |
| CSCO       | 2026-10-05 00:00:00 |   112.82      |        59.9167    | LONG     | Yahoo Finance |
| DXY-INDEX  | 2026-10-06 00:00:00 |   102.251     |        80.914     | LONG     | Yahoo Finance |
| ETC-USD    | 2026-10-06 00:00:00 |     8.83      |        37.6667    | LONG     | Kraken API    |
| FET-USD    | 2026-10-06 00:00:00 |     0.2461    |        60.1667    | LONG     | Kraken API    |
| FIL-USD    | 2026-10-06 00:00:00 |     1.182     |        63.3333    | LONG     | Kraken API    |
| GOOGL      | 2026-10-05 00:00:00 |   346.47      |        61         | LONG     | Yahoo Finance |
| GRT-USD    | 2026-10-06 00:00:00 |     0.02892   |        42.3333    | LONG     | Kraken API    |
| HBAR-USD   | 2026-10-06 00:00:00 |     0.10026   |        47.0833    | LONG     | Kraken API    |
| IBIT       | 2026-10-05 00:00:00 |    48.56      |        61.9167    | LONG     | Yahoo Finance |
| ICP-USD    | 2026-10-06 00:00:00 |     3.46      |        69.1667    | LONG     | Kraken API    |
| INTC       | 2026-10-05 00:00:00 |   116.19      |        57.0833    | LONG     | Yahoo Finance |
| LIN        | 2026-10-05 00:00:00 |   482.38      |        33.8333    | LONG     | Yahoo Finance |
| LINK-USD   | 2026-10-06 00:00:00 |    13.7837    |        40.6667    | LONG     | Kraken API    |
| LRCX       | 2026-10-05 00:00:00 |   345.8       |        57.75      | LONG     | Yahoo Finance |
| LTC-USD    | 2026-10-06 00:00:00 |    69.63      |        46.3333    | LONG     | Kraken API    |
| META       | 2026-10-05 00:00:00 |   741.9       |        52.5833    | LONG     | Yahoo Finance |
| MPC        | 2026-10-05 00:00:00 |   433.47      |        69.5833    | LONG     | Yahoo Finance |
| MSFT       | 2026-10-05 00:00:00 |   525.18      |        74.5833    | LONG     | Yahoo Finance |
| MU         | 2026-10-05 00:00:00 |  1063.96      |        73.25      | LONG     | Yahoo Finance |
| NEAR-USD   | 2026-10-06 00:00:00 |     5.1761    |        44.3333    | LONG     | Kraken API    |
| RENDER-USD | 2026-10-06 00:00:00 |     2.052     |        61.6667    | LONG     | Kraken API    |
| SHIB-USD   | 2026-10-06 00:00:00 |     5.83e-06  |        34.1667    | LONG     | Kraken API    |
| SKY-USD    | 2026-10-06 00:00:00 |     0.08752   |        51.6667    | LONG     | Kraken API    |
| SMH        | 2026-10-05 00:00:00 |   633.9       |        75.25      | LONG     | Yahoo Finance |
| SOL-USD    | 2026-10-06 00:00:00 |   119.4       |        50.3333    | LONG     | Kraken API    |
| SOXX       | 2026-10-05 00:00:00 |   589.51      |        73.25      | LONG     | Yahoo Finance |
| SUSHI-USD  | 2026-10-06 00:00:00 |     0.252     |        34.4167    | LONG     | Kraken API    |
| TMO        | 2026-10-05 00:00:00 |   676.76      |        59.5833    | LONG     | Yahoo Finance |
| TXN        | 2026-10-05 00:00:00 |   294.9       |        75.25      | LONG     | Yahoo Finance |
| UNH        | 2026-10-05 00:00:00 |   378.58      |        44.6667    | LONG     | Yahoo Finance |
| XLK        | 2026-10-05 00:00:00 |   200.93      |        77.25      | LONG     | Yahoo Finance |
| XLM-USD    | 2026-10-06 00:00:00 |     0.214066  |        34.4167    | LONG     | Kraken API    |
| YFI-USD    | 2026-10-06 00:00:00 |  2513         |        69         | LONG     | Kraken API    |
| ABBV       | 2026-10-05 00:00:00 |   265.76      |        52.1667    | NEUTRAL  | Yahoo Finance |
| ADBE       | 2026-10-05 00:00:00 |   238.79      |       -29.8333    | NEUTRAL  | Yahoo Finance |
| AMZN       | 2026-10-05 00:00:00 |   251.4       |        18.4167    | NEUTRAL  | Yahoo Finance |
| APT-USD    | 2026-10-06 00:00:00 |     0.8158    |         8.66667   | NEUTRAL  | Kraken API    |
| ARB-USD    | 2026-10-06 00:00:00 |     0.2016    |        24.1667    | NEUTRAL  | Kraken API    |
| ARKK       | 2026-10-05 00:00:00 |    92.78      |        64.5       | NEUTRAL  | Yahoo Finance |
| ATOM-USD   | 2026-10-06 00:00:00 |     1.8027    |        26.5833    | NEUTRAL  | Kraken API    |
| AVGO       | 2026-10-05 00:00:00 |   362.51      |        -6.33333   | NEUTRAL  | Yahoo Finance |
| BLK        | 2026-10-05 00:00:00 |  1066.45      |        -2.83333   | NEUTRAL  | Yahoo Finance |
| C          | 2026-10-05 00:00:00 |   128.55      |       -39.0833    | NEUTRAL  | Yahoo Finance |
| CAT        | 2026-10-05 00:00:00 |   848.14      |        54.25      | NEUTRAL  | Yahoo Finance |
| COP        | 2026-10-05 00:00:00 |   128.4       |        -0.0833333 | NEUTRAL  | Yahoo Finance |
| COST       | 2026-10-05 00:00:00 |   923.52      |         8.41667   | NEUTRAL  | Yahoo Finance |
| CRM        | 2026-10-05 00:00:00 |   229.79      |        12.5833    | NEUTRAL  | Yahoo Finance |
| CRV-USD    | 2026-10-06 00:00:00 |     0.365     |        37.5833    | NEUTRAL  | Kraken API    |
| CVX        | 2026-10-05 00:00:00 |   206.47      |         6.08333   | NEUTRAL  | Yahoo Finance |
| DASH-USD   | 2026-10-06 00:00:00 |    56.412     |        11.6667    | NEUTRAL  | Kraken API    |
| DBC        | 2026-10-05 00:00:00 |    32.39      |        20.4167    | NEUTRAL  | Yahoo Finance |
| DE         | 2026-10-05 00:00:00 |   682.2       |        25.1667    | NEUTRAL  | Yahoo Finance |
| DIA        | 2026-10-05 00:00:00 |   512.11      |        -4.58333   | NEUTRAL  | Yahoo Finance |
| DIS        | 2026-10-05 00:00:00 |   103.61      |       -42.25      | NEUTRAL  | Yahoo Finance |
| DOGE-USD   | 2026-10-06 00:00:00 |     0.0941054 |        21.6667    | NEUTRAL  | Kraken API    |
| DOT-USD    | 2026-10-06 00:00:00 |     1.2253    |        34.9167    | NEUTRAL  | Kraken API    |
| EEM        | 2026-10-05 00:00:00 |    68.73      |        47.3333    | NEUTRAL  | Yahoo Finance |
| EFA        | 2026-10-05 00:00:00 |   104.03      |       -24.25      | NEUTRAL  | Yahoo Finance |
| EOG        | 2026-10-05 00:00:00 |   144.08      |        13.5       | NEUTRAL  | Yahoo Finance |
| ETH-USD    | 2026-10-06 00:00:00 |  2694.53      |        29.3333    | NEUTRAL  | Kraken API    |
| EWJ        | 2026-10-05 00:00:00 |    99.3       |        65.1667    | NEUTRAL  | Yahoo Finance |
| FCX        | 2026-10-05 00:00:00 |    72.6       |        22.5       | NEUTRAL  | Yahoo Finance |
| FXI        | 2026-10-05 00:00:00 |    33.85      |       -53.3333    | NEUTRAL  | Yahoo Finance |
| GDX        | 2026-10-05 00:00:00 |    87.42      |       -26.5       | NEUTRAL  | Yahoo Finance |
| GDXJ       | 2026-10-05 00:00:00 |   112.81      |       -26.5       | NEUTRAL  | Yahoo Finance |
| GE         | 2026-10-05 00:00:00 |   306.34      |       -25.75      | NEUTRAL  | Yahoo Finance |
| HON        | 2026-10-05 00:00:00 |   214.14      |         1.08333   | NEUTRAL  | Yahoo Finance |
| IBM        | 2026-10-05 00:00:00 |   221.58      |       -67.8333    | NEUTRAL  | Yahoo Finance |
| IEMG       | 2026-10-05 00:00:00 |    83.58      |        45.5833    | NEUTRAL  | Yahoo Finance |
| INJ-USD    | 2026-10-06 00:00:00 |     7.51      |        28.6667    | NEUTRAL  | Kraken API    |
| IWM        | 2026-10-05 00:00:00 |   283.38      |        16.25      | NEUTRAL  | Yahoo Finance |
| JNJ        | 2026-10-05 00:00:00 |   252.93      |       -44.5833    | NEUTRAL  | Yahoo Finance |
| JPM        | 2026-10-05 00:00:00 |   332.38      |       -14.8333    | NEUTRAL  | Yahoo Finance |
| KO         | 2026-10-05 00:00:00 |    86.51      |       -17         | NEUTRAL  | Yahoo Finance |
| LDO-USD    | 2026-10-06 00:00:00 |     0.456     |        30.5833    | NEUTRAL  | Kraken API    |
| LLY        | 2026-10-05 00:00:00 |  1143.12      |        10.9167    | NEUTRAL  | Yahoo Finance |
| MRK        | 2026-10-05 00:00:00 |   139.54      |        -9.83333   | NEUTRAL  | Yahoo Finance |
| NEM        | 2026-10-05 00:00:00 |   115.82      |       -37.4167    | NEUTRAL  | Yahoo Finance |
| NOW        | 2026-10-05 00:00:00 |   136.08      |        16.1667    | NEUTRAL  | Yahoo Finance |
| NVDA       | 2026-10-05 00:00:00 |   238.9       |        64.5       | NEUTRAL  | Yahoo Finance |
| OP-USD     | 2026-10-06 00:00:00 |     0.1338    |         8.66667   | NEUTRAL  | Kraken API    |
| ORCL       | 2026-10-05 00:00:00 |   142.48      |       -23.6667    | NEUTRAL  | Yahoo Finance |
| OXY        | 2026-10-05 00:00:00 |    58.31      |         9.5       | NEUTRAL  | Yahoo Finance |
| PEPE-USD   | 2026-10-06 00:00:00 |     4.29e-06  |        28.1667    | NEUTRAL  | Kraken API    |
| PFE        | 2026-10-05 00:00:00 |    27.41      |         2.66667   | NEUTRAL  | Yahoo Finance |
| PG         | 2026-10-05 00:00:00 |   145.94      |       -13.3333    | NEUTRAL  | Yahoo Finance |
| PM         | 2026-10-05 00:00:00 |   189.53      |         0.333333  | NEUTRAL  | Yahoo Finance |
| POL-USD    | 2026-10-06 00:00:00 |     0.10847   |        -0.0833333 | NEUTRAL  | Kraken API    |
| QCOM       | 2026-10-05 00:00:00 |   180.79      |         8.41667   | NEUTRAL  | Yahoo Finance |
| QQQ        | 2026-10-05 00:00:00 |   756.2       |        66.5       | NEUTRAL  | Yahoo Finance |
| SHY        | 2026-10-05 00:00:00 |    81.08      |       -29.25      | NEUTRAL  | Yahoo Finance |
| SLV        | 2026-10-05 00:00:00 |    55.13      |       -57.5       | NEUTRAL  | Yahoo Finance |
| SNX-USD    | 2026-10-06 00:00:00 |     0.2497    |        21.3333    | NEUTRAL  | Kraken API    |
| SPY        | 2026-10-05 00:00:00 |   774.83      |        67.3333    | NEUTRAL  | Yahoo Finance |
| TGT        | 2026-10-05 00:00:00 |   152.99      |       -24         | NEUTRAL  | Yahoo Finance |
| TIA-USD    | 2026-10-06 00:00:00 |     0.4602    |        27.6667    | NEUTRAL  | Kraken API    |
| TRX-USD    | 2026-10-06 00:00:00 |     0.336064  |       -24.25      | NEUTRAL  | Kraken API    |
| TSLA       | 2026-10-05 00:00:00 |   378.73      |        32         | NEUTRAL  | Yahoo Finance |
| UNI-USD    | 2026-10-06 00:00:00 |     8.795     |        26.8333    | NEUTRAL  | Kraken API    |
| USO        | 2026-10-05 00:00:00 |   143.99      |        16.4167    | NEUTRAL  | Yahoo Finance |
| VEA        | 2026-10-05 00:00:00 |    71.13      |       -24.25      | NEUTRAL  | Yahoo Finance |
| VIXY       | 2026-10-05 00:00:00 |    16.54      |       -22.1667    | NEUTRAL  | Yahoo Finance |
| VTI        | 2026-10-05 00:00:00 |   380.6       |        67.3333    | NEUTRAL  | Yahoo Finance |
| VWO        | 2026-10-05 00:00:00 |    60.61      |        20.3333    | NEUTRAL  | Yahoo Finance |
| WIF-USD    | 2026-10-06 00:00:00 |     0.246     |        28.1667    | NEUTRAL  | Kraken API    |
| XBI        | 2026-10-05 00:00:00 |   156.19      |        -4.16667   | NEUTRAL  | Yahoo Finance |
| XLC        | 2026-10-05 00:00:00 |   111.61      |       -54.5833    | NEUTRAL  | Yahoo Finance |
| XLE        | 2026-10-05 00:00:00 |    63.45      |        23.25      | NEUTRAL  | Yahoo Finance |
| XLI        | 2026-10-05 00:00:00 |   170.1       |       -13.3333    | NEUTRAL  | Yahoo Finance |
| XLV        | 2026-10-05 00:00:00 |   167.37      |        10         | NEUTRAL  | Yahoo Finance |
| XLY        | 2026-10-05 00:00:00 |   110.42      |       -29.25      | NEUTRAL  | Yahoo Finance |
| XOM        | 2026-10-05 00:00:00 |   164         |         1.66667   | NEUTRAL  | Yahoo Finance |
| XRP-USD    | 2026-10-06 00:00:00 |     1.49351   |        34.6667    | NEUTRAL  | Kraken API    |
| ZEC-USD    | 2026-10-06 00:00:00 |  1322.96      |         3.33333   | NEUTRAL  | Kraken API    |
| AGG        | 2026-10-05 00:00:00 |    94.13      |       -52.0833    | SHORT    | Yahoo Finance |
| BA         | 2026-10-05 00:00:00 |   192.72      |       -56.0833    | SHORT    | Yahoo Finance |
| BAC        | 2026-10-05 00:00:00 |    54         |       -38.1667    | SHORT    | Yahoo Finance |
| BND        | 2026-10-05 00:00:00 |    69.88      |       -53.8333    | SHORT    | Yahoo Finance |
| CL         | 2026-10-05 00:00:00 |    86.19      |       -42.0833    | SHORT    | Yahoo Finance |
| CMCSA      | 2026-10-05 00:00:00 |    21.57      |       -63.0833    | SHORT    | Yahoo Finance |
| GLD        | 2026-10-05 00:00:00 |   379.55      |       -52.5       | SHORT    | Yahoo Finance |
| GS         | 2026-10-05 00:00:00 |   893.46      |       -56.5833    | SHORT    | Yahoo Finance |
| HD         | 2026-10-05 00:00:00 |   281.15      |       -56.0833    | SHORT    | Yahoo Finance |
| HYG        | 2026-10-05 00:00:00 |    76.98      |       -52.0833    | SHORT    | Yahoo Finance |
| IEF        | 2026-10-05 00:00:00 |    88.92      |       -52.0833    | SHORT    | Yahoo Finance |
| INTU       | 2026-10-05 00:00:00 |   284.68      |       -45.4167    | SHORT    | Yahoo Finance |
| ITA        | 2026-10-05 00:00:00 |   206.98      |       -31.25      | SHORT    | Yahoo Finance |
| MCD        | 2026-10-05 00:00:00 |   233.04      |       -54.9167    | SHORT    | Yahoo Finance |
| MS         | 2026-10-05 00:00:00 |   190.19      |       -40.1667    | SHORT    | Yahoo Finance |
| NFLX       | 2026-10-05 00:00:00 |    67.5       |       -45.5833    | SHORT    | Yahoo Finance |
| NKE        | 2026-10-05 00:00:00 |    33.96      |       -46.25      | SHORT    | Yahoo Finance |
| PEP        | 2026-10-05 00:00:00 |   125.65      |       -57.4167    | SHORT    | Yahoo Finance |
| RTX        | 2026-10-05 00:00:00 |   184.33      |       -49.5833    | SHORT    | Yahoo Finance |
| SBUX       | 2026-10-05 00:00:00 |    94.43      |       -31.25      | SHORT    | Yahoo Finance |
| SCHW       | 2026-10-05 00:00:00 |    97.96      |       -40.1667    | SHORT    | Yahoo Finance |
| SLB        | 2026-10-05 00:00:00 |    50.28      |       -30.6667    | SHORT    | Yahoo Finance |
| T          | 2026-10-05 00:00:00 |    24.24      |       -57.3333    | SHORT    | Yahoo Finance |
| TLT        | 2026-10-05 00:00:00 |    77.11      |       -55.75      | SHORT    | Yahoo Finance |
| TMUS       | 2026-10-05 00:00:00 |   164.64      |       -57.4167    | SHORT    | Yahoo Finance |
| UPS        | 2026-10-05 00:00:00 |    93.14      |       -61.0833    | SHORT    | Yahoo Finance |
| VNQ        | 2026-10-05 00:00:00 |    89.15      |       -40.5833    | SHORT    | Yahoo Finance |
| VZ         | 2026-10-05 00:00:00 |    45.85      |       -57.3333    | SHORT    | Yahoo Finance |
| WFC        | 2026-10-05 00:00:00 |    81.44      |       -54.8333    | SHORT    | Yahoo Finance |
| WMT        | 2026-10-05 00:00:00 |   105.07      |       -48.75      | SHORT    | Yahoo Finance |
| XLB        | 2026-10-05 00:00:00 |    49.5       |       -46.5833    | SHORT    | Yahoo Finance |
| XLF        | 2026-10-05 00:00:00 |    53.88      |       -37.6667    | SHORT    | Yahoo Finance |
| XLP        | 2026-10-05 00:00:00 |    81.04      |       -48.25      | SHORT    | Yahoo Finance |
| XLU        | 2026-10-05 00:00:00 |    39.97      |       -33.75      | SHORT    | Yahoo Finance |

## Edge Summary

- Symbols with trades: **161** of 161
- Beat buy-and-hold: **33.54%** of traded symbols
- Positive return: **32.30%** of traded symbols
- Median strategy return: **-9.78%** (benchmark **19.14%**)
- Median excess vs benchmark: **-25.92%**
- Median Sharpe: **-0.11**
- Median exposure: **44.26%**

> Edge is real only if both _beat buy-and-hold_ and _median excess_ are convincingly positive across many symbols. Treat a single high-return symbol as noise.

## Portfolio Backtest

Actual capital-allocation books (not per-symbol averages). Benchmarks: `equal_weight_buyhold` (whole tracked universe), `spy_buyhold` (100% SPY), and `sixty_forty` (60% SPY / 40% AGG). `high_conf_voltarget` inverse-vol-weights the HIGH-confidence book; `conviction_long_short` is market-neutral. Judge on **Sharpe** and **max_drawdown** out-of-sample, not raw return: a fully-invested long book wins on return in a bull market but carries all the risk.

| strategy              | scope         | ann_return   | ann_vol   |   sharpe | max_drawdown   | total_return   |   avg_gross_exposure |
|:----------------------|:--------------|:-------------|:----------|---------:|:---------------|:---------------|---------------------:|
| equal_weight_buyhold  | full          | 12.79%       | 28.40%    |     0.45 | -39.53%        | 30.59%         |                 1    |
| equal_weight_buyhold  | out_of_sample | 9.91%        | 27.78%    |     0.36 | -28.81%        | 6.70%          |                 1    |
| all_signals_ew        | full          | -15.46%      | 24.14%    |    -0.64 | -60.26%        | -42.87%        |                 1    |
| all_signals_ew        | out_of_sample | 12.80%       | 23.27%    |     0.55 | -23.20%        | 11.40%         |                 1    |
| high_conf_ew          | full          | 1.61%        | 31.28%    |     0.05 | -44.57%        | -9.33%         |                 0.9  |
| high_conf_ew          | out_of_sample | 31.88%       | 27.23%    |     1.17 | -22.85%        | 35.00%         |                 0.9  |
| high_conf_voltarget   | full          | 0.18%        | 27.92%    |     0.01 | -38.57%        | -10.49%        |                 0.9  |
| high_conf_voltarget   | out_of_sample | 18.09%       | 22.27%    |     0.81 | -17.00%        | 18.05%         |                 0.9  |
| conviction_long_short | full          | -14.64%      | 22.39%    |    -0.65 | -48.90%        | -40.73%        |                 0.96 |
| conviction_long_short | out_of_sample | 0.48%        | 19.88%    |     0.02 | -26.60%        | -1.58%         |                 0.96 |
| spy_buyhold           | full          | 5.22%        | 13.50%    |     0.39 | -19.00%        | 14.05%         |                 0.78 |
| spy_buyhold           | out_of_sample | 1.54%        | 9.90%     |     0.16 | -12.06%        | 1.13%          |                 0.78 |
| sixty_forty           | full          | 2.73%        | 8.54%     |     0.32 | -11.66%        | 7.47%          |                 0.78 |
| sixty_forty           | out_of_sample | -1.48%       | 6.66%     |    -0.22 | -8.26%         | -1.80%         |                 0.78 |

## Walk-Forward Robustness

Each book measured across contiguous time folds (each a different regime). A book has durable edge only if `mean_sharpe` is positive, `min_sharpe` isn't deeply negative, and `pct_positive_folds` is high — a single great fold doesn't count. `fold_sharpes` lists each fold oldest-to-newest.

| strategy              |   n_folds |   mean_sharpe |   median_sharpe |   min_sharpe | pct_positive_folds   | mean_return   | fold_sharpes                 |
|:----------------------|----------:|--------------:|----------------:|-------------:|:---------------------|:--------------|:-----------------------------|
| equal_weight_buyhold  |         5 |          0.6  |            0.87 |        -0.39 | 80.00%               | 6.15%         | 0.87;0.95;0.06;-0.39;1.53    |
| all_signals_ew        |         5 |         -0.6  |           -0.79 |        -1.91 | 40.00%               | -8.39%        | -0.79;-1.82;-1.91;1.48;0.03  |
| high_conf_ew          |         5 |          0.13 |            0.07 |        -1.55 | 60.00%               | -0.29%        | 0.07;-1.55;-0.25;1.28;1.10   |
| high_conf_voltarget   |         5 |          0.12 |            0.34 |        -1.58 | 60.00%               | -1.32%        | 0.34;-1.58;-0.17;0.74;1.26   |
| conviction_long_short |         5 |         -0.62 |           -0.79 |        -1.54 | 20.00%               | -9.64%        | -1.54;-0.90;-0.79;-0.31;0.43 |
| spy_buyhold           |         5 |          0.4  |            0.11 |        -0.15 | 80.00%               | 2.78%         | 1.54;0.11;0.03;0.45;-0.15    |
| sixty_forty           |         5 |          0.3  |            0.19 |        -0.61 | 80.00%               | 1.50%         | 1.47;0.19;0.25;0.16;-0.61    |

## Strategy Comparison

Each decision rule backtested over the same data. `out_of_sample` is the most recent ~35% of each symbol's history (unseen tail). A rule has real edge only if `median_excess` and `beat_benchmark_pct` stay positive out-of-sample, not just full-sample.

| strategy        | scope         |   symbols | beat_benchmark_pct   | positive_pct   | median_return   | median_benchmark   | median_excess   |   median_sharpe |   total_trades |
|:----------------|:--------------|----------:|:---------------------|:---------------|:----------------|:-------------------|:----------------|----------------:|---------------:|
| trend           | full          |       161 | 33.54%               | 32.30%         | -9.78%          | 19.14%             | -25.92%         |           -0.11 |          11253 |
| trend           | out_of_sample |       161 | 29.81%               | 55.28%         | 1.81%           | 10.30%             | -14.51%         |            0.25 |           3782 |
| mean_reversion  | full          |       156 | 37.82%               | 49.36%         | -0.04%          | 15.62%             | -16.67%         |            0.02 |           1214 |
| mean_reversion  | out_of_sample |       118 | 29.66%               | 52.54%         | 0.29%           | 9.15%              | -11.31%         |            0.16 |            476 |
| regime_adaptive | full          |       161 | 32.30%               | 32.30%         | -10.24%         | 19.14%             | -25.92%         |           -0.11 |          11522 |
| regime_adaptive | out_of_sample |       161 | 29.81%               | 52.17%         | 0.27%           | 10.30%             | -15.15%         |            0.13 |           3893 |

## Signal Calibration

Realized forward return in the signal's direction, grouped by confidence. HIGH should outrank LOW for the confidence score to be meaningful.

| confidence_level   |   horizon |     n | mean_return   | median_return   | win_rate   |
|:-------------------|----------:|------:|:--------------|:----------------|:-----------|
| HIGH               |         5 |  8062 | 0.19%         | 0.05%           | 50.86%     |
| MEDIUM             |         5 | 29095 | 0.02%         | 0.04%           | 50.37%     |
| LOW                |         5 |  3462 | -0.38%        | -0.40%          | 46.16%     |
| ALL                |         5 | 40619 | 0.02%         | 0.01%           | 50.11%     |
| HIGH               |        10 |  7985 | 0.48%         | 0.09%           | 51.02%     |
| MEDIUM             |        10 | 28779 | 0.18%         | 0.06%           | 50.46%     |
| LOW                |        10 |  3437 | -0.72%        | -0.56%          | 46.35%     |
| ALL                |        10 | 40201 | 0.17%         | 0.03%           | 50.22%     |
| HIGH               |        20 |  7818 | 1.13%         | 0.33%           | 52.75%     |
| MEDIUM             |        20 | 28362 | 0.84%         | 0.52%           | 52.92%     |
| LOW                |        20 |  3390 | -0.52%        | -0.66%          | 46.90%     |
| ALL                |        20 | 39570 | 0.78%         | 0.41%           | 52.37%     |

## Backtest Summary

### Data Quality / Signal Availability

- **ok**: 161 symbols

| symbol     |   trades | return   | benchmark_return   | mdd     |   sharpe | exposure   | skipped_reason   |
|:-----------|---------:|:---------|:-------------------|:--------|---------:|:-----------|:-----------------|
| AAPL       |       64 | 6.04%    | 78.70%             | -23.09% |     0.22 | 51.58%     | ok               |
| AAVE-USD   |       67 | -21.34%  | 1.98%              | -66.17% |     0    | 41.95%     | ok               |
| ABBV       |       70 | -25.73%  | 64.78%             | -30.52% |    -0.58 | 47.92%     | ok               |
| ADA-USD    |       77 | -30.38%  | -61.83%            | -46.79% |    -0.17 | 46.55%     | ok               |
| ADBE       |       69 | -6.76%   | -50.57%            | -31.20% |     0.05 | 56.41%     | ok               |
| AGG        |       65 | -5.78%   | -2.24%             | -11.01% |    -0.89 | 33.61%     | ok               |
| ALGO-USD   |       76 | -29.72%  | -38.53%            | -38.19% |    -0.18 | 39.85%     | ok               |
| AMAT       |       73 | -33.51%  | 162.44%            | -57.56% |    -0.29 | 50.92%     | ok               |
| AMD        |       54 | 29.40%   | 319.60%            | -41.09% |     0.47 | 36.44%     | ok               |
| AMGN       |       69 | -17.88%  | 30.65%             | -34.19% |    -0.34 | 50.25%     | ok               |
| AMZN       |       80 | -56.43%  | 34.75%             | -56.88% |    -1.62 | 40.77%     | ok               |
| APT-USD    |       72 | -30.37%  | -84.27%            | -62.06% |    -0.08 | 40.42%     | ok               |
| ARB-USD    |       77 | -20.76%  | -36.98%            | -55.44% |     0.09 | 43.87%     | ok               |
| ARKK       |       84 | -23.42%  | 110.05%            | -28.66% |    -0.31 | 42.76%     | ok               |
| ATOM-USD   |       92 | -58.73%  | -57.26%            | -58.73% |    -0.82 | 48.08%     | ok               |
| AVAX-USD   |       68 | -27.22%  | -45.40%            | -45.19% |    -0.16 | 40.04%     | ok               |
| AVGO       |       64 | 15.79%   | 171.03%            | -36.09% |     0.35 | 41.93%     | ok               |
| BA         |       69 | 3.24%    | 8.00%              | -26.26% |     0.18 | 50.58%     | ok               |
| BAC        |       72 | -10.50%  | 41.32%             | -25.80% |    -0.23 | 47.92%     | ok               |
| BCH-USD    |       74 | 19.12%   | -13.25%            | -53.87% |     0.4  | 49.23%     | ok               |
| BITO       |       78 | -10.55%  | -55.45%            | -39.47% |     0.03 | 41.76%     | ok               |
| BLK        |       83 | -13.55%  | 34.94%             | -26.90% |    -0.32 | 48.09%     | ok               |
| BND        |       65 | -5.46%   | -2.18%             | -10.37% |    -0.82 | 35.44%     | ok               |
| BONK-USD   |       72 | 38.85%   | -77.45%            | -45.22% |     0.56 | 45.40%     | ok               |
| BTC-USD    |       70 | 16.84%   | -10.94%            | -23.38% |     0.41 | 53.45%     | ok               |
| C          |       77 | -35.76%  | 102.76%            | -41.08% |    -0.78 | 47.09%     | ok               |
| CAT        |       70 | 8.91%    | 137.79%            | -18.69% |     0.27 | 49.58%     | ok               |
| CL         |       64 | -4.23%   | -8.76%             | -14.32% |    -0.08 | 39.27%     | ok               |
| CMCSA      |       84 | -36.70%  | -42.03%            | -46.39% |    -0.9  | 42.26%     | ok               |
| COMP-USD   |       95 | -32.14%  | -39.78%            | -55.77% |    -0.13 | 49.04%     | ok               |
| COP        |       66 | -16.32%  | 5.60%              | -41.35% |    -0.22 | 43.43%     | ok               |
| COST       |       58 | 0.96%    | 19.14%             | -30.95% |     0.1  | 41.93%     | ok               |
| CRM        |       67 | -32.20%  | -17.20%            | -45.51% |    -0.45 | 46.26%     | ok               |
| CRV-USD    |       68 | 24.02%   | -48.01%            | -39.89% |     0.45 | 38.31%     | ok               |
| CSCO       |       64 | 14.67%   | 131.76%            | -21.79% |     0.37 | 48.25%     | ok               |
| CVX        |       71 | -13.64%  | 25.49%             | -27.78% |    -0.3  | 41.76%     | ok               |
| DASH-USD   |       57 | -9.06%   | 150.45%            | -64.43% |     0.33 | 30.84%     | ok               |
| DBC        |       64 | -7.57%   | 38.24%             | -24.10% |    -0.19 | 35.11%     | ok               |
| DE         |       72 | -11.19%  | 67.21%             | -24.01% |    -0.15 | 44.43%     | ok               |
| DIA        |       64 | -6.79%   | 29.83%             | -12.94% |    -0.34 | 44.26%     | ok               |
| DIS        |       60 | -6.18%   | -2.10%             | -28.17% |    -0.05 | 43.09%     | ok               |
| DOGE-USD   |       69 | -31.60%  | -46.44%            | -60.95% |    -0.11 | 48.47%     | ok               |
| DOT-USD    |       88 | -58.07%  | -69.58%            | -63.33% |    -0.55 | 49.04%     | ok               |
| DXY-INDEX  |       40 | -0.54%   | -3.85%             | -6.02%  |    -0.07 | 30.95%     | ok               |
| EEM        |       62 | -11.21%  | 60.51%             | -25.38% |    -0.31 | 41.10%     | ok               |
| EFA        |       62 | -11.08%  | 29.49%             | -12.28% |    -0.42 | 43.09%     | ok               |
| EOG        |       78 | -30.38%  | 11.34%             | -47.87% |    -0.66 | 44.76%     | ok               |
| ETC-USD    |       56 | -19.29%  | -46.81%            | -48.09% |    -0.15 | 30.46%     | ok               |
| ETH-USD    |       58 | 178.93%  | 46.93%             | -30.11% |     1.44 | 48.85%     | ok               |
| EWJ        |       62 | -22.99%  | 46.72%             | -29.40% |    -0.8  | 36.44%     | ok               |
| FCX        |       65 | -29.37%  | 39.51%             | -46.84% |    -0.32 | 44.26%     | ok               |
| FET-USD    |       77 | -37.10%  | -64.19%            | -60.12% |    -0.16 | 41.38%     | ok               |
| FIL-USD    |       65 | -42.38%  | -55.35%            | -58.54% |    -0.4  | 36.21%     | ok               |
| FXI        |       50 | -7.74%   | 19.36%             | -24.33% |    -0.11 | 32.28%     | ok               |
| GDX        |       58 | -2.33%   | 150.13%            | -33.31% |     0.1  | 44.26%     | ok               |
| GDXJ       |       68 | -36.38%  | 162.96%            | -41.57% |    -0.48 | 42.60%     | ok               |
| GE         |       78 | -9.78%   | 92.06%             | -27.82% |    -0.07 | 48.25%     | ok               |
| GLD        |       50 | 9.78%    | 75.51%             | -13.87% |     0.31 | 44.93%     | ok               |
| GOOGL      |       55 | 55.58%   | 104.84%            | -17.54% |     0.99 | 46.92%     | ok               |
| GRT-USD    |       77 | 33.42%   | -69.02%            | -45.34% |     0.52 | 45.40%     | ok               |
| GS         |       70 | -2.49%   | 96.99%             | -22.13% |     0.05 | 48.09%     | ok               |
| HBAR-USD   |       38 | -39.60%  | -2.78%             | -56.29% |    -0.85 | 37.65%     | ok               |
| HD         |       69 | 5.53%    | -17.54%            | -17.15% |     0.22 | 42.76%     | ok               |
| HON        |       89 | -27.14%  | 6.30%              | -33.03% |    -0.68 | 55.57%     | ok               |
| HYG        |       85 | -6.56%   | 0.13%              | -10.59% |    -0.73 | 37.94%     | ok               |
| IBIT       |       38 | 44.44%   | 27.76%             | -18.95% |     0.78 | 34.36%     | ok               |
| IBM        |       69 | -24.27%  | 32.24%             | -48.94% |    -0.28 | 49.92%     | ok               |
| ICP-USD    |       77 | 9.15%    | -26.69%            | -46.42% |     0.34 | 38.89%     | ok               |
| IEF        |       78 | -9.78%   | -3.98%             | -13.49% |    -1.31 | 33.94%     | ok               |
| IEMG       |       62 | -11.68%  | 55.70%             | -29.43% |    -0.35 | 41.60%     | ok               |
| INJ-USD    |       63 | -21.84%  | -22.11%            | -69.36% |     0.03 | 39.85%     | ok               |
| INTC       |       68 | 45.67%   | 280.83%            | -60.60% |     0.56 | 48.25%     | ok               |
| INTU       |       73 | -9.91%   | -54.61%            | -37.57% |    -0.03 | 46.76%     | ok               |
| ITA        |       72 | -1.21%   | 54.11%             | -23.75% |     0.04 | 49.08%     | ok               |
| IWM        |       54 | 8.79%    | 38.41%             | -12.65% |     0.37 | 35.27%     | ok               |
| JNJ        |       62 | 6.25%    | 67.26%             | -16.86% |     0.28 | 47.25%     | ok               |
| JPM        |       73 | -22.55%  | 67.25%             | -32.74% |    -0.61 | 46.09%     | ok               |
| KO         |       54 | 22.10%   | 36.06%             | -8.64%  |     0.79 | 37.94%     | ok               |
| LDO-USD    |       72 | 10.52%   | -44.66%            | -59.24% |     0.37 | 46.93%     | ok               |
| LIN        |       70 | -12.12%  | 10.95%             | -20.61% |    -0.39 | 37.60%     | ok               |
| LINK-USD   |       69 | 36.17%   | -3.36%             | -33.64% |     0.55 | 46.36%     | ok               |
| LLY        |       76 | -32.49%  | 50.87%             | -53.34% |    -0.52 | 49.42%     | ok               |
| LRCX       |       76 | -18.71%  | 282.61%            | -58.79% |    -0.06 | 42.10%     | ok               |
| LTC-USD    |       67 | 24.45%   | -19.56%            | -32.66% |     0.47 | 53.45%     | ok               |
| MCD        |       77 | 1.17%    | -14.11%            | -21.88% |     0.1  | 39.77%     | ok               |
| META       |       78 | -24.47%  | 58.52%             | -44.52% |    -0.32 | 50.08%     | ok               |
| MPC        |       71 | 15.76%   | 143.71%            | -37.91% |     0.37 | 51.91%     | ok               |
| MRK        |       67 | -22.56%  | 7.93%              | -35.95% |    -0.42 | 42.93%     | ok               |
| MS         |       73 | -7.91%   | 92.97%             | -27.25% |    -0.11 | 48.09%     | ok               |
| MSFT       |       83 | -25.95%  | 26.94%             | -38.06% |    -0.56 | 50.25%     | ok               |
| MU         |       51 | 155.89%  | 765.01%            | -68.76% |     1.05 | 53.24%     | ok               |
| NEAR-USD   |       73 | 129.53%  | 113.62%            | -52.25% |     0.98 | 43.87%     | ok               |
| NEM        |       66 | -24.97%  | 172.77%            | -39.56% |    -0.23 | 50.75%     | ok               |
| NFLX       |       78 | 15.76%   | 9.47%              | -21.09% |     0.4  | 53.58%     | ok               |
| NKE        |       79 | -23.35%  | -63.37%            | -55.35% |    -0.23 | 46.09%     | ok               |
| NOW        |       84 | 9.21%    | -6.81%             | -30.43% |     0.28 | 50.58%     | ok               |
| NVDA       |       77 | -45.72%  | 87.52%             | -52.37% |    -0.61 | 54.90%     | ok               |
| OP-USD     |       68 | -37.66%  | -80.29%            | -68.74% |    -0.25 | 33.91%     | ok               |
| ORCL       |       62 | 98.66%   | 22.44%             | -30.61% |     0.87 | 53.24%     | ok               |
| OXY        |       69 | -0.67%   | -7.31%             | -28.48% |     0.11 | 42.26%     | ok               |
| PEP        |       74 | 1.91%    | -30.54%            | -21.35% |     0.13 | 46.09%     | ok               |
| PEPE-USD   |       85 | -45.68%  | -47.51%            | -61.29% |    -0.24 | 49.43%     | ok               |
| PFE        |       81 | -33.95%  | -3.62%             | -41.90% |    -1.03 | 37.77%     | ok               |
| PG         |       64 | -23.02%  | -12.02%            | -24.16% |    -0.92 | 35.61%     | ok               |
| PM         |       79 | -6.86%   | 90.89%             | -35.15% |    -0.06 | 51.25%     | ok               |
| POL-USD    |       81 | 29.19%   | -52.83%            | -38.69% |     0.5  | 50.00%     | ok               |
| QCOM       |       77 | -23.20%  | -1.86%             | -57.69% |    -0.15 | 44.43%     | ok               |
| QQQ        |       64 | 11.60%   | 70.67%             | -14.20% |     0.37 | 45.59%     | ok               |
| RENDER-USD |       94 | -15.41%  | -55.14%            | -44.84% |     0.12 | 46.74%     | ok               |
| RTX        |       64 | 31.34%   | 74.22%             | -16.99% |     0.72 | 52.41%     | ok               |
| SBUX       |       58 | -11.73%  | 23.96%             | -29.22% |    -0.17 | 38.60%     | ok               |
| SCHW       |       80 | -16.55%  | 31.14%             | -31.92% |    -0.34 | 46.26%     | ok               |
| SHIB-USD   |       78 | -40.94%  | -55.05%            | -42.45% |    -0.42 | 51.72%     | ok               |
| SHY        |       46 | -1.63%   | -0.27%             | -3.18%  |    -0.55 | 36.94%     | ok               |
| SKY-USD    |       87 | -46.91%  | 38.68%             | -61.34% |    -0.57 | 45.40%     | ok               |
| SLB        |       75 | -37.33%  | 3.14%              | -56.30% |    -0.71 | 48.25%     | ok               |
| SLV        |       66 | 11.38%   | 113.68%            | -42.66% |     0.31 | 40.60%     | ok               |
| SMH        |       48 | 64.23%   | 183.93%            | -34.29% |     0.96 | 44.09%     | ok               |
| SNX-USD    |       62 | -21.23%  | -62.79%            | -50.27% |    -0.04 | 34.10%     | ok               |
| SOL-USD    |       68 | -7.03%   | -18.64%            | -44.99% |     0.15 | 60.15%     | ok               |
| SOXX       |       54 | 75.63%   | 167.11%            | -39.81% |     1.01 | 42.76%     | ok               |
| SPY        |       64 | 1.58%    | 48.75%             | -15.53% |     0.12 | 50.58%     | ok               |
| SUSHI-USD  |       96 | -81.02%  | -60.13%            | -82.74% |    -1.33 | 39.66%     | ok               |
| T          |       70 | 40.65%   | 40.44%             | -17.01% |     0.86 | 56.74%     | ok               |
| TGT        |       62 | -11.80%  | -4.92%             | -34.98% |    -0.18 | 37.77%     | ok               |
| TIA-USD    |       95 | -68.10%  | -81.23%            | -78.90% |    -0.72 | 42.34%     | ok               |
| TLT        |       70 | -17.59%  | -14.65%            | -22.36% |    -1.28 | 34.11%     | ok               |
| TMO        |       65 | 23.63%   | 14.57%             | -18.85% |     0.52 | 54.41%     | ok               |
| TMUS       |       76 | 3.84%    | 0.79%              | -27.54% |     0.18 | 47.75%     | ok               |
| TRX-USD    |       68 | 10.93%   | 36.85%             | -22.90% |     0.38 | 52.30%     | ok               |
| TSLA       |       80 | -36.44%  | 120.33%            | -58.36% |    -0.25 | 43.26%     | ok               |
| TXN        |       77 | -16.78%  | 57.01%             | -46.98% |    -0.12 | 50.08%     | ok               |
| UNH        |       74 | 25.63%   | -26.02%            | -26.31% |     0.47 | 48.92%     | ok               |
| UNI-USD    |       92 | -52.55%  | 72.48%             | -78.80% |    -0.31 | 51.15%     | ok               |
| UPS        |       72 | -33.96%  | -38.15%            | -39.06% |    -0.66 | 41.76%     | ok               |
| USO        |       67 | -9.31%   | 89.14%             | -44.98% |    -0.01 | 33.28%     | ok               |
| VEA        |       58 | -3.38%   | 41.27%             | -16.28% |    -0.09 | 43.26%     | ok               |
| VIXY       |       94 | -78.22%  | -65.97%            | -88.19% |    -0.94 | 33.28%     | ok               |
| VNQ        |       73 | -11.82%  | 7.20%              | -24.92% |    -0.46 | 40.10%     | ok               |
| VTI        |       68 | -6.07%   | 47.41%             | -17.64% |    -0.16 | 50.58%     | ok               |
| VWO        |       79 | -19.45%  | 38.38%             | -27.17% |    -0.73 | 41.93%     | ok               |
| VZ         |       84 | -19.81%  | 13.10%             | -25.90% |    -0.58 | 41.26%     | ok               |
| WFC        |       80 | -16.44%  | 32.94%             | -28.90% |    -0.26 | 47.75%     | ok               |
| WIF-USD    |       64 | -26.25%  | -56.74%            | -52.76% |    -0.01 | 36.97%     | ok               |
| WMT        |       69 | 6.56%    | 73.93%             | -23.80% |     0.25 | 48.92%     | ok               |
| XBI        |       64 | -0.72%   | 73.78%             | -18.30% |     0.07 | 39.93%     | ok               |
| XLB        |       62 | -12.64%  | 7.87%              | -25.04% |    -0.44 | 32.45%     | ok               |
| XLC        |       61 | 12.62%   | 36.71%             | -12.33% |     0.47 | 50.25%     | ok               |
| XLE        |       71 | -11.02%  | 35.61%             | -32.20% |    -0.2  | 44.26%     | ok               |
| XLF        |       80 | -8.86%   | 29.33%             | -23.61% |    -0.27 | 46.42%     | ok               |
| XLI        |       80 | -7.98%   | 35.92%             | -15.90% |    -0.27 | 42.60%     | ok               |
| XLK        |       40 | 64.12%   | 94.60%             | -14.75% |     1.19 | 46.59%     | ok               |
| XLM-USD    |       65 | -5.09%   | -20.50%            | -54.58% |     0.17 | 47.70%     | ok               |
| XLP        |       68 | 3.41%    | 4.70%              | -11.56% |     0.23 | 37.94%     | ok               |
| XLU        |       69 | -1.95%   | 12.17%             | -20.40% |    -0.04 | 40.60%     | ok               |
| XLV        |       76 | -20.86%  | 16.67%             | -22.75% |    -0.99 | 37.94%     | ok               |
| XLY        |       75 | -4.12%   | 24.16%             | -18.35% |    -0.06 | 47.59%     | ok               |
| XOM        |       55 | 1.71%    | 39.09%             | -20.29% |     0.12 | 34.28%     | ok               |
| XRP-USD    |       64 | 8.72%    | -31.76%            | -33.91% |     0.3  | 36.97%     | ok               |
| YFI-USD    |       77 | -69.30%  | -53.71%            | -69.91% |    -1.32 | 37.74%     | ok               |
| ZEC-USD    |       61 | 177.85%  | 3590.26%           | -56.50% |     0.99 | 42.53%     | ok               |

## AAPL Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 12.68%   | 78.70%             | -22.53% |     0.34 |       73 | 56.41%     | ok               |
|          15 | 9.77%    | 78.70%             | -24.50% |     0.29 |       82 | 63.73%     | ok               |
|          30 | 6.04%    | 78.70%             | -23.09% |     0.22 |       64 | 51.58%     | ok               |
|          40 | 4.92%    | 78.70%             | -28.08% |     0.2  |       60 | 46.09%     | ok               |
|          35 | 4.52%    | 78.70%             | -24.45% |     0.2  |       64 | 50.25%     | ok               |

## AAVE-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 60.41%   | 1.98%              | -43.61% |     0.72 |       43 | 36.21%     | ok               |
|          45 | 45.47%   | 1.98%              | -49.19% |     0.63 |       48 | 31.03%     | ok               |
|          35 | 39.93%   | 1.98%              | -48.79% |     0.57 |       51 | 39.27%     | ok               |
|          50 | 29.33%   | 1.98%              | -45.07% |     0.5  |       46 | 23.75%     | ok               |
|          15 | -9.73%   | 1.98%              | -61.76% |     0.19 |       72 | 55.36%     | ok               |

## ABBV Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -13.90%  | 64.78%             | -26.16% |    -0.3  |       54 | 34.78%     | ok               |
|          20 | -24.39%  | 64.78%             | -29.11% |    -0.52 |       66 | 51.41%     | ok               |
|          25 | -24.48%  | 64.78%             | -30.41% |    -0.53 |       69 | 49.92%     | ok               |
|          30 | -25.73%  | 64.78%             | -30.52% |    -0.58 |       70 | 47.92%     | ok               |
|          40 | -23.92%  | 64.78%             | -27.36% |    -0.58 |       70 | 40.10%     | ok               |

## ADA-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 30.26%   | -61.83%            | -35.54% |     0.53 |       48 | 27.59%     | ok               |
|          45 | 17.91%   | -61.83%            | -34.64% |     0.4  |       47 | 32.18%     | ok               |
|          40 | -2.20%   | -61.83%            | -40.73% |     0.19 |       59 | 38.12%     | ok               |
|          35 | -10.03%  | -61.83%            | -42.89% |     0.1  |       65 | 41.95%     | ok               |
|          15 | -20.34%  | -61.83%            | -47.27% |     0.08 |       72 | 62.45%     | ok               |

## ADBE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | 8.57%    | -50.57%            | -29.07% |     0.27 |       56 | 60.73%     | ok               |
|          35 | -1.77%   | -50.57%            | -31.71% |     0.1  |       79 | 48.25%     | ok               |
|          20 | -5.65%   | -50.57%            | -31.52% |     0.08 |       62 | 63.73%     | ok               |
|          30 | -6.76%   | -50.57%            | -31.20% |     0.05 |       69 | 56.41%     | ok               |
|          15 | -16.25%  | -50.57%            | -34.98% |    -0.08 |       62 | 65.56%     | ok               |

## AGG Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -4.95%   | -2.24%             | -9.56%  |    -0.87 |       58 | 24.96%     | ok               |
|          30 | -5.78%   | -2.24%             | -11.01% |    -0.89 |       65 | 33.61%     | ok               |
|          50 | -4.46%   | -2.24%             | -8.07%  |    -0.92 |       56 | 20.30%     | ok               |
|          20 | -6.85%   | -2.24%             | -11.55% |    -0.96 |       71 | 38.60%     | ok               |
|          25 | -7.03%   | -2.24%             | -12.19% |    -1.03 |       71 | 36.94%     | ok               |

## ALGO-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -29.72%  | -38.53%            | -38.19% |    -0.18 |       76 | 39.85%     | ok               |
|          15 | -34.81%  | -38.53%            | -51.37% |    -0.19 |       79 | 50.19%     | ok               |
|          25 | -38.60%  | -38.53%            | -54.40% |    -0.29 |       78 | 44.83%     | ok               |
|          20 | -41.66%  | -38.53%            | -53.23% |    -0.32 |       81 | 47.70%     | ok               |
|          35 | -42.01%  | -38.53%            | -49.75% |    -0.48 |       64 | 34.67%     | ok               |

## AMAT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -15.49%  | 162.44%            | -38.30% |    -0.05 |       50 | 35.27%     | ok               |
|          15 | -25.65%  | 162.44%            | -53.90% |    -0.13 |       72 | 59.73%     | ok               |
|          35 | -28.57%  | 162.44%            | -52.00% |    -0.22 |       73 | 48.25%     | ok               |
|          30 | -33.51%  | 162.44%            | -57.56% |    -0.29 |       73 | 50.92%     | ok               |
|          40 | -34.39%  | 162.44%            | -54.64% |    -0.33 |       71 | 43.43%     | ok               |

## AMD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 32.67%   | 319.60%            | -40.05% |     0.5  |       58 | 31.45%     | ok               |
|          40 | 29.40%   | 319.60%            | -41.09% |     0.47 |       54 | 36.44%     | ok               |
|          35 | 26.73%   | 319.60%            | -43.15% |     0.45 |       62 | 37.94%     | ok               |
|          30 | 10.01%   | 319.60%            | -49.79% |     0.31 |       63 | 40.43%     | ok               |
|          25 | 5.21%    | 319.60%            | -54.33% |     0.27 |       59 | 42.60%     | ok               |

## AMGN Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -13.18%  | 30.65%             | -26.65% |    -0.2  |       64 | 56.07%     | ok               |
|          35 | -15.74%  | 30.65%             | -31.29% |    -0.29 |       69 | 46.76%     | ok               |
|          30 | -17.88%  | 30.65%             | -34.19% |    -0.34 |       69 | 50.25%     | ok               |
|          15 | -20.22%  | 30.65%             | -27.98% |    -0.36 |       63 | 60.40%     | ok               |
|          25 | -19.69%  | 30.65%             | -33.47% |    -0.38 |       63 | 52.58%     | ok               |

## AMZN Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -27.29%  | 34.75%             | -28.95% |    -0.83 |       54 | 29.78%     | ok               |
|          50 | -31.74%  | 34.75%             | -33.91% |    -1.16 |       50 | 22.80%     | ok               |
|          45 | -36.87%  | 34.75%             | -37.67% |    -1.31 |       56 | 26.29%     | ok               |
|          35 | -51.03%  | 34.75%             | -51.54% |    -1.48 |       73 | 34.94%     | ok               |
|          30 | -56.43%  | 34.75%             | -56.88% |    -1.62 |       80 | 40.77%     | ok               |

## APT-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 5.82%    | -84.27%            | -61.36% |     0.33 |       76 | 50.00%     | ok               |
|          50 | 6.76%    | -84.27%            | -39.70% |     0.26 |       44 | 16.67%     | ok               |
|          25 | -20.21%  | -84.27%            | -61.15% |     0.06 |       70 | 44.83%     | ok               |
|          45 | -15.94%  | -84.27%            | -59.21% |    -0.01 |       60 | 23.56%     | ok               |
|          15 | -31.17%  | -84.27%            | -63.36% |    -0.02 |       74 | 55.94%     | ok               |

## ARB-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 68.81%   | -36.98%            | -44.26% |     0.7  |       85 | 60.15%     | ok               |
|          45 | 30.34%   | -36.98%            | -35.90% |     0.49 |       56 | 26.82%     | ok               |
|          20 | 25.95%   | -36.98%            | -54.05% |     0.48 |       71 | 54.41%     | ok               |
|          50 | 21.38%   | -36.98%            | -30.72% |     0.42 |       44 | 19.73%     | ok               |
|          25 | 1.36%    | -36.98%            | -52.32% |     0.32 |       73 | 50.00%     | ok               |

## ARKK Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -12.57%  | 110.05%            | -37.76% |    -0.04 |       90 | 54.58%     | ok               |
|          20 | -16.48%  | 110.05%            | -34.82% |    -0.12 |       86 | 49.75%     | ok               |
|          30 | -23.42%  | 110.05%            | -28.66% |    -0.31 |       84 | 42.76%     | ok               |
|          35 | -31.46%  | 110.05%            | -34.08% |    -0.52 |       84 | 40.43%     | ok               |
|          25 | -36.96%  | 110.05%            | -43.18% |    -0.6  |       96 | 45.59%     | ok               |

## ATOM-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -42.24%  | -57.26%            | -48.77% |    -0.34 |       86 | 65.71%     | ok               |
|          25 | -48.91%  | -57.26%            | -50.00% |    -0.53 |       92 | 54.41%     | ok               |
|          20 | -56.19%  | -57.26%            | -57.75% |    -0.67 |       96 | 58.05%     | ok               |
|          30 | -58.73%  | -57.26%            | -58.73% |    -0.82 |       92 | 48.08%     | ok               |
|          35 | -59.37%  | -57.26%            | -61.61% |    -0.94 |       82 | 42.15%     | ok               |

## AVAX-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 38.74%   | -45.40%            | -22.06% |     0.66 |       32 | 19.73%     | ok               |
|          40 | 30.99%   | -45.40%            | -26.27% |     0.56 |       34 | 27.20%     | ok               |
|          45 | 27.31%   | -45.40%            | -23.19% |     0.52 |       28 | 24.14%     | ok               |
|          35 | 7.98%    | -45.40%            | -33.05% |     0.29 |       54 | 33.72%     | ok               |
|          15 | -4.12%   | -45.40%            | -42.39% |     0.2  |       73 | 53.45%     | ok               |

## AVGO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | 19.12%   | 171.03%            | -38.01% |     0.38 |       68 | 44.59%     | ok               |
|          30 | 15.79%   | 171.03%            | -36.09% |     0.35 |       64 | 41.93%     | ok               |
|          50 | 10.84%   | 171.03%            | -36.86% |     0.29 |       56 | 29.78%     | ok               |
|          35 | 7.38%    | 171.03%            | -40.43% |     0.26 |       74 | 38.94%     | ok               |
|          20 | 5.45%    | 171.03%            | -39.42% |     0.24 |       77 | 47.75%     | ok               |

## BA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 37.54%   | 8.00%              | -13.34% |     0.84 |       46 | 35.27%     | ok               |
|          40 | 31.94%   | 8.00%              | -23.87% |     0.63 |       46 | 43.09%     | ok               |
|          35 | 32.54%   | 8.00%              | -18.09% |     0.62 |       64 | 47.25%     | ok               |
|          25 | 12.81%   | 8.00%              | -26.72% |     0.33 |       70 | 54.08%     | ok               |
|          20 | 4.53%    | 8.00%              | -27.98% |     0.2  |       71 | 57.40%     | ok               |

## BAC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | -0.25%   | 41.32%             | -23.08% |     0.07 |       64 | 44.59%     | ok               |
|          20 | -1.96%   | 41.32%             | -18.20% |     0.03 |       80 | 52.58%     | ok               |
|          25 | -4.36%   | 41.32%             | -22.11% |    -0.04 |       74 | 50.08%     | ok               |
|          45 | -6.80%   | 41.32%             | -19.47% |    -0.15 |       60 | 36.94%     | ok               |
|          15 | -9.83%   | 41.32%             | -23.94% |    -0.15 |       87 | 59.73%     | ok               |

## BCH-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 57.29%   | -13.25%            | -45.51% |     0.69 |       73 | 57.47%     | ok               |
|          20 | 30.45%   | -13.25%            | -45.63% |     0.5  |       65 | 54.21%     | ok               |
|          30 | 19.12%   | -13.25%            | -53.87% |     0.4  |       74 | 49.23%     | ok               |
|          25 | 18.12%   | -13.25%            | -51.09% |     0.4  |       68 | 50.96%     | ok               |
|          35 | 2.00%    | -13.25%            | -57.99% |     0.23 |       70 | 45.79%     | ok               |

## BITO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -2.86%   | -55.45%            | -31.98% |     0.1  |       54 | 25.46%     | ok               |
|          30 | -10.55%  | -55.45%            | -39.47% |     0.03 |       78 | 41.76%     | ok               |
|          25 | -18.59%  | -55.45%            | -38.26% |    -0.07 |       82 | 44.93%     | ok               |
|          15 | -21.21%  | -55.45%            | -48.38% |    -0.07 |       85 | 49.92%     | ok               |
|          20 | -20.55%  | -55.45%            | -38.52% |    -0.1  |       82 | 46.26%     | ok               |

## BLK Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | -5.19%   | 34.94%             | -20.79% |    -0.08 |       90 | 44.43%     | ok               |
|          40 | -6.45%   | 34.94%             | -22.83% |    -0.13 |       78 | 39.60%     | ok               |
|          20 | -8.03%   | 34.94%             | -21.48% |    -0.13 |       86 | 52.75%     | ok               |
|          25 | -9.35%   | 34.94%             | -24.62% |    -0.18 |       79 | 50.58%     | ok               |
|          30 | -13.55%  | 34.94%             | -26.90% |    -0.32 |       83 | 48.09%     | ok               |

## BND Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -4.80%   | -2.18%             | -9.66%  |    -0.66 |       65 | 40.60%     | ok               |
|          25 | -5.46%   | -2.18%             | -10.73% |    -0.78 |       67 | 38.60%     | ok               |
|          30 | -5.46%   | -2.18%             | -10.37% |    -0.82 |       65 | 35.44%     | ok               |
|          15 | -7.10%   | -2.18%             | -11.52% |    -0.97 |       77 | 43.43%     | ok               |
|          40 | -5.90%   | -2.18%             | -10.43% |    -1    |       62 | 29.12%     | ok               |

## BONK-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 156.03%  | -77.45%            | -35.57% |     1.2  |       42 | 21.46%     | ok               |
|          45 | 69.26%   | -77.45%            | -42.36% |     0.75 |       66 | 27.78%     | ok               |
|          15 | 74.05%   | -77.45%            | -63.45% |     0.72 |       68 | 59.77%     | ok               |
|          20 | 63.97%   | -77.45%            | -55.19% |     0.69 |       66 | 55.56%     | ok               |
|          40 | 41.59%   | -77.45%            | -50.07% |     0.58 |       56 | 37.36%     | ok               |

## BTC-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 55.12%   | -10.94%            | -14.50% |     1.01 |       44 | 36.97%     | ok               |
|          35 | 57.98%   | -10.94%            | -21.56% |     1.01 |       62 | 43.10%     | ok               |
|          45 | 50.27%   | -10.94%            | -12.20% |     0.98 |       42 | 32.95%     | ok               |
|          30 | 30.59%   | -10.94%            | -21.75% |     0.61 |       68 | 49.04%     | ok               |
|          50 | 19.02%   | -10.94%            | -20.63% |     0.51 |       42 | 27.39%     | ok               |

## C Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -11.26%  | 102.76%            | -21.80% |    -0.25 |       66 | 32.28%     | ok               |
|          45 | -19.41%  | 102.76%            | -27.40% |    -0.47 |       72 | 36.27%     | ok               |
|          40 | -25.11%  | 102.76%            | -33.13% |    -0.61 |       74 | 38.60%     | ok               |
|          25 | -32.83%  | 102.76%            | -38.39% |    -0.68 |       67 | 49.08%     | ok               |
|          15 | -35.07%  | 102.76%            | -38.73% |    -0.69 |       70 | 55.91%     | ok               |

## CAT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 18.03%   | 137.79%            | -19.89% |     0.39 |       70 | 62.23%     | ok               |
|          25 | 17.22%   | 137.79%            | -18.48% |     0.39 |       64 | 52.08%     | ok               |
|          20 | 9.70%    | 137.79%            | -19.49% |     0.28 |       74 | 55.74%     | ok               |
|          30 | 8.91%    | 137.79%            | -18.69% |     0.27 |       70 | 49.58%     | ok               |
|          45 | 2.71%    | 137.79%            | -26.22% |     0.16 |       56 | 38.27%     | ok               |

## CL Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -1.79%   | -8.76%             | -12.98% |    -0.03 |       42 | 23.29%     | ok               |
|          30 | -4.23%   | -8.76%             | -14.32% |    -0.08 |       64 | 39.27%     | ok               |
|          35 | -8.04%   | -8.76%             | -14.26% |    -0.23 |       64 | 35.44%     | ok               |
|          45 | -7.46%   | -8.76%             | -13.51% |    -0.26 |       48 | 26.12%     | ok               |
|          15 | -12.82%  | -8.76%             | -18.51% |    -0.33 |       64 | 47.59%     | ok               |

## CMCSA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -18.88%  | -42.03%            | -28.41% |    -0.63 |       46 | 15.97%     | ok               |
|          15 | -37.10%  | -42.03%            | -46.99% |    -0.79 |       93 | 57.07%     | ok               |
|          45 | -25.46%  | -42.03%            | -35.13% |    -0.83 |       62 | 20.30%     | ok               |
|          30 | -36.70%  | -42.03%            | -46.39% |    -0.9  |       84 | 42.26%     | ok               |
|          40 | -33.09%  | -42.03%            | -42.51% |    -0.91 |       89 | 27.79%     | ok               |

## COMP-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 9.94%    | -39.78%            | -38.71% |     0.32 |       48 | 24.33%     | ok               |
|          30 | -32.14%  | -39.78%            | -55.77% |    -0.13 |       95 | 49.04%     | ok               |
|          25 | -38.84%  | -39.78%            | -54.62% |    -0.21 |       94 | 56.90%     | ok               |
|          15 | -45.33%  | -39.78%            | -54.29% |    -0.28 |       98 | 67.05%     | ok               |
|          45 | -39.17%  | -39.78%            | -53.54% |    -0.32 |       64 | 32.38%     | ok               |

## COP Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -10.92%  | 5.60%              | -34.61% |    -0.16 |       46 | 27.29%     | ok               |
|          35 | -14.48%  | 5.60%              | -42.05% |    -0.19 |       69 | 40.60%     | ok               |
|          30 | -16.32%  | 5.60%              | -41.35% |    -0.22 |       66 | 43.43%     | ok               |
|          45 | -17.92%  | 5.60%              | -41.10% |    -0.32 |       62 | 31.45%     | ok               |
|          25 | -27.95%  | 5.60%              | -47.42% |    -0.48 |       77 | 46.42%     | ok               |

## COST Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 12.34%   | 19.14%             | -24.32% |     0.42 |       60 | 47.25%     | ok               |
|          25 | 9.87%    | 19.14%             | -24.93% |     0.36 |       57 | 44.59%     | ok               |
|          35 | 5.41%    | 19.14%             | -29.78% |     0.24 |       56 | 39.43%     | ok               |
|          30 | 0.96%    | 19.14%             | -30.95% |     0.1  |       58 | 41.93%     | ok               |
|          15 | -2.88%   | 19.14%             | -27.30% |    -0.01 |       65 | 50.92%     | ok               |

## CRM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | -22.78%  | -17.20%            | -34.06% |    -0.28 |       62 | 41.26%     | ok               |
|          15 | -31.54%  | -17.20%            | -47.54% |    -0.36 |       90 | 58.07%     | ok               |
|          40 | -25.67%  | -17.20%            | -39.44% |    -0.37 |       68 | 37.10%     | ok               |
|          50 | -21.91%  | -17.20%            | -38.24% |    -0.4  |       56 | 24.79%     | ok               |
|          30 | -32.20%  | -17.20%            | -45.51% |    -0.45 |       67 | 46.26%     | ok               |

## CRV-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 58.67%   | -48.01%            | -37.78% |     0.7  |       68 | 33.52%     | ok               |
|          40 | 44.53%   | -48.01%            | -38.86% |     0.61 |       56 | 29.31%     | ok               |
|          45 | 34.97%   | -48.01%            | -42.29% |     0.55 |       56 | 22.41%     | ok               |
|          50 | 34.05%   | -48.01%            | -30.73% |     0.54 |       48 | 18.39%     | ok               |
|          30 | 24.02%   | -48.01%            | -39.89% |     0.45 |       68 | 38.31%     | ok               |

## CSCO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 30.19%   | 131.76%            | -19.34% |     0.65 |       50 | 37.10%     | ok               |
|          45 | 25.79%   | 131.76%            | -19.34% |     0.57 |       52 | 38.77%     | ok               |
|          25 | 21.04%   | 131.76%            | -23.28% |     0.46 |       61 | 49.58%     | ok               |
|          20 | 16.37%   | 131.76%            | -22.72% |     0.39 |       71 | 52.08%     | ok               |
|          30 | 14.67%   | 131.76%            | -21.79% |     0.37 |       64 | 48.25%     | ok               |

## CVX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -9.57%   | 25.49%             | -23.80% |    -0.17 |       73 | 44.59%     | ok               |
|          40 | -10.08%  | 25.49%             | -27.34% |    -0.22 |       73 | 36.61%     | ok               |
|          45 | -10.48%  | 25.49%             | -28.83% |    -0.24 |       65 | 33.28%     | ok               |
|          50 | -10.36%  | 25.49%             | -30.69% |    -0.29 |       58 | 28.79%     | ok               |
|          35 | -13.01%  | 25.49%             | -28.85% |    -0.29 |       67 | 38.60%     | ok               |

## DASH-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 156.61%  | 150.45%            | -33.55% |     1.01 |       38 | 18.01%     | ok               |
|          40 | 107.73%  | 150.45%            | -33.20% |     0.83 |       44 | 24.52%     | ok               |
|          45 | 78.66%   | 150.45%            | -37.63% |     0.72 |       44 | 20.69%     | ok               |
|          25 | -8.59%   | 150.45%            | -64.14% |     0.33 |       63 | 33.14%     | ok               |
|          30 | -9.06%   | 150.45%            | -64.43% |     0.33 |       57 | 30.84%     | ok               |

## DBC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -0.43%   | 38.24%             | -26.05% |     0.05 |       77 | 40.93%     | ok               |
|          25 | -4.67%   | 38.24%             | -24.84% |    -0.09 |       64 | 37.44%     | ok               |
|          20 | -4.81%   | 38.24%             | -25.69% |    -0.09 |       69 | 39.27%     | ok               |
|          50 | -5.52%   | 38.24%             | -18.84% |    -0.15 |       48 | 24.63%     | ok               |
|          35 | -7.16%   | 38.24%             | -23.19% |    -0.18 |       64 | 34.11%     | ok               |

## DE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 3.27%    | 67.21%             | -17.97% |     0.16 |       58 | 29.78%     | ok               |
|          45 | -3.42%   | 67.21%             | -19.56% |     0    |       62 | 34.28%     | ok               |
|          20 | -6.77%   | 67.21%             | -24.13% |    -0.05 |       67 | 48.75%     | ok               |
|          25 | -11.05%  | 67.21%             | -24.31% |    -0.15 |       73 | 47.09%     | ok               |
|          30 | -11.19%  | 67.21%             | -24.01% |    -0.15 |       72 | 44.43%     | ok               |

## DIA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -4.51%   | 29.83%             | -11.17% |    -0.21 |       56 | 45.59%     | ok               |
|          35 | -5.37%   | 29.83%             | -13.15% |    -0.27 |       66 | 41.26%     | ok               |
|          30 | -6.79%   | 29.83%             | -12.94% |    -0.34 |       64 | 44.26%     | ok               |
|          20 | -7.27%   | 29.83%             | -13.60% |    -0.35 |       62 | 47.59%     | ok               |
|          40 | -8.50%   | 29.83%             | -15.06% |    -0.48 |       70 | 38.27%     | ok               |

## DIS Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 33.83%   | -2.10%             | -10.17% |     1.05 |       44 | 25.46%     | ok               |
|          40 | 8.18%    | -2.10%             | -18.75% |     0.28 |       57 | 33.78%     | ok               |
|          45 | 3.62%    | -2.10%             | -16.54% |     0.17 |       45 | 29.12%     | ok               |
|          35 | -4.01%   | -2.10%             | -25.70% |    -0    |       71 | 39.77%     | ok               |
|          15 | -6.56%   | -2.10%             | -32.73% |    -0.03 |       85 | 54.74%     | ok               |

## DOGE-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 0.63%    | -46.44%            | -57.89% |     0.28 |       73 | 63.79%     | ok               |
|          20 | -1.89%   | -46.44%            | -55.83% |     0.25 |       74 | 58.62%     | ok               |
|          25 | -12.76%  | -46.44%            | -53.72% |     0.14 |       66 | 54.79%     | ok               |
|          30 | -31.60%  | -46.44%            | -60.95% |    -0.11 |       69 | 48.47%     | ok               |
|          50 | -38.25%  | -46.44%            | -56.78% |    -0.39 |       62 | 25.10%     | ok               |

## DOT-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -56.20%  | -69.58%            | -72.06% |    -0.37 |       77 | 64.37%     | ok               |
|          20 | -53.17%  | -69.58%            | -66.32% |    -0.39 |       89 | 60.34%     | ok               |
|          30 | -58.07%  | -69.58%            | -63.33% |    -0.55 |       88 | 49.04%     | ok               |
|          25 | -60.40%  | -69.58%            | -69.99% |    -0.56 |       80 | 55.17%     | ok               |
|          35 | -61.72%  | -69.58%            | -63.01% |    -0.67 |       86 | 43.30%     | ok               |

## DXY-INDEX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd    |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:-------|---------:|---------:|:-----------|:-----------------|
|          50 | -0.54%   | -3.85%             | -6.02% |    -0.07 |       40 | 30.95%     | ok               |
|          40 | -1.38%   | -3.85%             | -7.30% |    -0.16 |       64 | 46.75%     | ok               |
|          45 | -1.90%   | -3.85%             | -8.14% |    -0.25 |       60 | 37.01%     | ok               |
|          35 | -4.24%   | -3.85%             | -9.97% |    -0.53 |       77 | 51.95%     | ok               |
|          30 | -4.71%   | -3.85%             | -9.83% |    -0.56 |       76 | 57.14%     | ok               |

## EEM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -6.65%   | 60.51%             | -15.92% |    -0.19 |       54 | 33.28%     | ok               |
|          45 | -6.99%   | 60.51%             | -17.07% |    -0.2  |       52 | 34.78%     | ok               |
|          40 | -7.33%   | 60.51%             | -19.24% |    -0.2  |       64 | 36.94%     | ok               |
|          35 | -7.93%   | 60.51%             | -23.57% |    -0.2  |       66 | 39.27%     | ok               |
|          30 | -11.21%  | 60.51%             | -25.38% |    -0.31 |       62 | 41.10%     | ok               |

## EFA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -4.24%   | 29.49%             | -10.10% |    -0.09 |       62 | 51.41%     | ok               |
|          30 | -11.08%  | 29.49%             | -12.28% |    -0.42 |       62 | 43.09%     | ok               |
|          20 | -11.75%  | 29.49%             | -13.36% |    -0.42 |       71 | 48.42%     | ok               |
|          25 | -11.80%  | 29.49%             | -14.11% |    -0.44 |       64 | 45.59%     | ok               |
|          35 | -12.54%  | 29.49%             | -13.73% |    -0.5  |       56 | 41.60%     | ok               |

## EOG Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -17.66%  | 11.34%             | -35.34% |    -0.37 |       54 | 30.62%     | ok               |
|          40 | -23.88%  | 11.34%             | -37.39% |    -0.54 |       70 | 34.61%     | ok               |
|          50 | -22.67%  | 11.34%             | -35.63% |    -0.55 |       52 | 27.62%     | ok               |
|          35 | -27.88%  | 11.34%             | -41.05% |    -0.64 |       83 | 39.60%     | ok               |
|          30 | -30.38%  | 11.34%             | -47.87% |    -0.66 |       78 | 44.76%     | ok               |

## ETC-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -5.47%   | -46.81%            | -38.47% |     0.05 |       28 | 20.50%     | ok               |
|          50 | -4.94%   | -46.81%            | -31.28% |     0.05 |       28 | 18.20%     | ok               |
|          35 | -15.99%  | -46.81%            | -45.32% |    -0.1  |       42 | 26.82%     | ok               |
|          30 | -19.29%  | -46.81%            | -48.09% |    -0.15 |       56 | 30.46%     | ok               |
|          40 | -17.08%  | -46.81%            | -43.28% |    -0.15 |       38 | 23.56%     | ok               |

## ETH-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 178.93%  | 46.93%             | -30.11% |     1.44 |       58 | 48.85%     | ok               |
|          30 | 146.51%  | 46.93%             | -32.89% |     1.25 |       60 | 56.32%     | ok               |
|          25 | 101.80%  | 46.93%             | -40.90% |     1    |       60 | 60.15%     | ok               |
|          20 | 83.84%   | 46.93%             | -39.10% |     0.89 |       78 | 63.98%     | ok               |
|          15 | 76.77%   | 46.93%             | -42.74% |     0.83 |       69 | 68.97%     | ok               |

## EWJ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -22.99%  | 46.72%             | -29.40% |    -0.8  |       62 | 36.44%     | ok               |
|          20 | -23.95%  | 46.72%             | -30.00% |    -0.81 |       56 | 38.44%     | ok               |
|          45 | -21.95%  | 46.72%             | -25.77% |    -0.87 |       58 | 28.79%     | ok               |
|          25 | -25.82%  | 46.72%             | -29.85% |    -0.9  |       56 | 37.60%     | ok               |
|          15 | -27.60%  | 46.72%             | -31.15% |    -0.9  |       67 | 41.76%     | ok               |

## FCX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 2.51%    | 39.51%             | -29.27% |     0.18 |       50 | 31.61%     | ok               |
|          50 | -0.09%   | 39.51%             | -26.57% |     0.13 |       52 | 27.95%     | ok               |
|          40 | -10.00%  | 39.51%             | -42.89% |    -0.01 |       62 | 36.94%     | ok               |
|          30 | -29.37%  | 39.51%             | -46.84% |    -0.32 |       65 | 44.26%     | ok               |
|          35 | -29.20%  | 39.51%             | -50.12% |    -0.34 |       67 | 42.10%     | ok               |

## FET-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -20.36%  | -64.19%            | -64.89% |     0.1  |       90 | 51.72%     | ok               |
|          15 | -22.45%  | -64.19%            | -59.58% |     0.1  |       84 | 56.32%     | ok               |
|          25 | -22.34%  | -64.19%            | -65.31% |     0.06 |       79 | 45.79%     | ok               |
|          30 | -37.10%  | -64.19%            | -60.12% |    -0.16 |       77 | 41.38%     | ok               |
|          50 | -34.74%  | -64.19%            | -43.68% |    -0.44 |       46 | 14.18%     | ok               |

## FIL-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -36.02%  | -55.35%            | -57.60% |    -0.37 |       50 | 25.67%     | ok               |
|          30 | -42.38%  | -55.35%            | -58.54% |    -0.4  |       65 | 36.21%     | ok               |
|          35 | -46.25%  | -55.35%            | -61.90% |    -0.54 |       60 | 30.08%     | ok               |
|          50 | -39.79%  | -55.35%            | -47.18% |    -0.59 |       38 | 15.33%     | ok               |
|          15 | -59.49%  | -55.35%            | -71.82% |    -0.62 |       93 | 48.47%     | ok               |

## FXI Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -7.48%   | 19.36%             | -22.99% |    -0.1  |       52 | 33.78%     | ok               |
|          15 | -8.33%   | 19.36%             | -21.68% |    -0.11 |       54 | 37.77%     | ok               |
|          30 | -7.74%   | 19.36%             | -24.33% |    -0.11 |       50 | 32.28%     | ok               |
|          20 | -11.00%  | 19.36%             | -24.94% |    -0.19 |       54 | 35.61%     | ok               |
|          35 | -11.30%  | 19.36%             | -27.93% |    -0.22 |       52 | 29.78%     | ok               |

## GDX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 4.34%    | 150.13%            | -28.47% |     0.2  |       58 | 38.27%     | ok               |
|          20 | 2.08%    | 150.13%            | -33.01% |     0.18 |       76 | 49.25%     | ok               |
|          35 | -1.69%   | 150.13%            | -31.73% |     0.1  |       66 | 40.93%     | ok               |
|          30 | -2.33%   | 150.13%            | -33.31% |     0.1  |       58 | 44.26%     | ok               |
|          25 | -7.50%   | 150.13%            | -38.90% |     0.02 |       62 | 45.42%     | ok               |

## GDXJ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -27.64%  | 162.96%            | -42.33% |    -0.25 |       74 | 49.25%     | ok               |
|          50 | -25.39%  | 162.96%            | -46.83% |    -0.33 |       56 | 34.11%     | ok               |
|          35 | -34.57%  | 162.96%            | -38.56% |    -0.46 |       68 | 39.93%     | ok               |
|          30 | -36.38%  | 162.96%            | -41.57% |    -0.48 |       68 | 42.60%     | ok               |
|          40 | -35.79%  | 162.96%            | -44.70% |    -0.52 |       62 | 37.60%     | ok               |

## GE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 4.89%    | 92.06%             | -21.25% |     0.2  |       60 | 33.78%     | ok               |
|          45 | -3.80%   | 92.06%             | -21.88% |     0.02 |       72 | 36.61%     | ok               |
|          20 | -8.55%   | 92.06%             | -25.05% |    -0.04 |       74 | 52.91%     | ok               |
|          30 | -9.78%   | 92.06%             | -27.82% |    -0.07 |       78 | 48.25%     | ok               |
|          25 | -9.99%   | 92.06%             | -29.91% |    -0.07 |       74 | 50.08%     | ok               |

## GLD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | 15.27%   | 75.51%             | -13.87% |     0.43 |       48 | 46.09%     | ok               |
|          20 | 13.70%   | 75.51%             | -13.87% |     0.39 |       49 | 47.75%     | ok               |
|          30 | 9.78%    | 75.51%             | -13.87% |     0.31 |       50 | 44.93%     | ok               |
|          35 | 6.88%    | 75.51%             | -14.65% |     0.25 |       52 | 42.60%     | ok               |
|          15 | 3.25%    | 75.51%             | -17.63% |     0.17 |       57 | 51.08%     | ok               |

## GOOGL Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 59.43%   | 104.84%            | -17.38% |     1.06 |       57 | 43.43%     | ok               |
|          30 | 55.58%   | 104.84%            | -17.54% |     0.99 |       55 | 46.92%     | ok               |
|          45 | 48.09%   | 104.84%            | -11.66% |     0.97 |       50 | 36.94%     | ok               |
|          25 | 53.21%   | 104.84%            | -16.87% |     0.94 |       55 | 49.42%     | ok               |
|          50 | 43.73%   | 104.84%            | -11.52% |     0.93 |       42 | 32.11%     | ok               |

## GRT-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 71.16%   | -69.02%            | -42.58% |     0.74 |       70 | 62.26%     | ok               |
|          20 | 56.90%   | -69.02%            | -40.19% |     0.67 |       77 | 56.51%     | ok               |
|          25 | 35.58%   | -69.02%            | -45.66% |     0.54 |       78 | 51.92%     | ok               |
|          50 | 32.00%   | -69.02%            | -30.80% |     0.54 |       44 | 21.07%     | ok               |
|          45 | 32.39%   | -69.02%            | -44.68% |     0.53 |       46 | 27.97%     | ok               |

## GS Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 24.06%   | 96.99%             | -20.56% |     0.52 |       68 | 56.41%     | ok               |
|          20 | 5.00%    | 96.99%             | -23.19% |     0.2  |       68 | 53.08%     | ok               |
|          40 | 3.84%    | 96.99%             | -17.88% |     0.18 |       68 | 42.43%     | ok               |
|          25 | -0.32%   | 96.99%             | -23.32% |     0.1  |       68 | 50.58%     | ok               |
|          30 | -2.49%   | 96.99%             | -22.13% |     0.05 |       70 | 48.09%     | ok               |

## HBAR-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -18.09%  | -2.78%             | -39.26% |    -0.26 |       18 | 18.43%     | ok               |
|          45 | -28.35%  | -2.78%             | -48.15% |    -0.54 |       22 | 24.31%     | ok               |
|          40 | -31.58%  | -2.78%             | -50.49% |    -0.63 |       26 | 29.02%     | ok               |
|          15 | -38.58%  | -2.78%             | -55.56% |    -0.78 |       51 | 50.59%     | ok               |
|          30 | -39.60%  | -2.78%             | -56.29% |    -0.85 |       38 | 37.65%     | ok               |

## HD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 5.53%    | -17.54%            | -17.15% |     0.22 |       69 | 42.76%     | ok               |
|          25 | 2.86%    | -17.54%            | -18.88% |     0.15 |       68 | 44.93%     | ok               |
|          35 | 1.11%    | -17.54%            | -18.52% |     0.11 |       72 | 39.10%     | ok               |
|          40 | -0.61%   | -17.54%            | -18.05% |     0.05 |       76 | 34.61%     | ok               |
|          45 | -1.07%   | -17.54%            | -18.71% |     0.03 |       52 | 29.95%     | ok               |

## HON Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -11.61%  | 6.30%              | -21.17% |    -0.3  |       70 | 34.11%     | ok               |
|          45 | -15.30%  | 6.30%              | -22.88% |    -0.39 |       72 | 39.60%     | ok               |
|          35 | -25.18%  | 6.30%              | -31.30% |    -0.65 |       89 | 50.92%     | ok               |
|          30 | -27.14%  | 6.30%              | -33.03% |    -0.68 |       89 | 55.57%     | ok               |
|          40 | -25.49%  | 6.30%              | -31.84% |    -0.68 |       76 | 43.93%     | ok               |

## HYG Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -4.35%   | 0.13%              | -7.76%  |    -0.5  |       68 | 33.11%     | ok               |
|          45 | -5.54%   | 0.13%              | -8.86%  |    -0.66 |       68 | 29.78%     | ok               |
|          35 | -6.18%   | 0.13%              | -9.66%  |    -0.71 |       77 | 34.78%     | ok               |
|          30 | -6.56%   | 0.13%              | -10.59% |    -0.73 |       85 | 37.94%     | ok               |
|          25 | -7.53%   | 0.13%              | -11.22% |    -0.82 |       89 | 40.43%     | ok               |

## IBIT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 59.96%   | 27.76%             | -17.37% |     1.04 |       26 | 25.31%     | ok               |
|          15 | 73.24%   | 27.76%             | -19.20% |     1.03 |       44 | 41.15%     | ok               |
|          45 | 50.12%   | 27.76%             | -17.37% |     0.89 |       30 | 26.54%     | ok               |
|          40 | 43.40%   | 27.76%             | -17.78% |     0.8  |       30 | 28.40%     | ok               |
|          30 | 44.44%   | 27.76%             | -18.95% |     0.78 |       38 | 34.36%     | ok               |

## IBM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -18.03%  | 32.24%             | -49.43% |    -0.12 |       84 | 61.90%     | ok               |
|          35 | -21.42%  | 32.24%             | -47.10% |    -0.23 |       63 | 45.92%     | ok               |
|          30 | -24.27%  | 32.24%             | -48.94% |    -0.28 |       69 | 49.92%     | ok               |
|          20 | -29.79%  | 32.24%             | -53.45% |    -0.36 |       70 | 54.91%     | ok               |
|          45 | -28.12%  | 32.24%             | -48.72% |    -0.4  |       52 | 37.44%     | ok               |

## ICP-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 17.04%   | -26.69%            | -46.78% |     0.39 |       70 | 33.14%     | ok               |
|          40 | 16.21%   | -26.69%            | -40.71% |     0.38 |       62 | 28.35%     | ok               |
|          30 | 9.15%    | -26.69%            | -46.42% |     0.34 |       77 | 38.89%     | ok               |
|          50 | -4.67%   | -26.69%            | -50.31% |     0.12 |       44 | 18.20%     | ok               |
|          15 | -26.34%  | -26.69%            | -58.26% |     0.07 |       77 | 49.62%     | ok               |

## IEF Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -5.36%   | -3.98%             | -10.32% |    -0.62 |       72 | 42.43%     | ok               |
|          15 | -5.93%   | -3.98%             | -11.04% |    -0.67 |       71 | 43.93%     | ok               |
|          40 | -7.70%   | -3.98%             | -11.39% |    -1.1  |       64 | 27.29%     | ok               |
|          25 | -8.98%   | -3.98%             | -12.17% |    -1.11 |       76 | 39.77%     | ok               |
|          45 | -7.60%   | -3.98%             | -11.30% |    -1.11 |       58 | 25.79%     | ok               |

## IEMG Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -1.78%   | 55.70%             | -13.95% |    -0.01 |       54 | 32.28%     | ok               |
|          45 | -2.13%   | 55.70%             | -14.56% |    -0.02 |       50 | 34.61%     | ok               |
|          40 | -3.95%   | 55.70%             | -18.35% |    -0.09 |       62 | 37.77%     | ok               |
|          35 | -6.43%   | 55.70%             | -24.56% |    -0.16 |       67 | 40.27%     | ok               |
|          30 | -11.68%  | 55.70%             | -29.43% |    -0.35 |       62 | 41.60%     | ok               |

## INJ-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 14.69%   | -22.11%            | -46.84% |     0.37 |       48 | 33.52%     | ok               |
|          35 | 10.63%   | -22.11%            | -53.43% |     0.34 |       58 | 36.40%     | ok               |
|          45 | 5.66%    | -22.11%            | -45.62% |     0.28 |       52 | 27.59%     | ok               |
|          30 | -21.84%  | -22.11%            | -69.36% |     0.03 |       63 | 39.85%     | ok               |
|          20 | -27.64%  | -22.11%            | -77.39% |     0.01 |       74 | 48.28%     | ok               |

## INTC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 75.64%   | 280.83%            | -49.32% |     0.74 |       56 | 33.61%     | ok               |
|          50 | 70.18%   | 280.83%            | -48.35% |     0.71 |       60 | 29.78%     | ok               |
|          40 | 65.30%   | 280.83%            | -55.86% |     0.67 |       62 | 37.60%     | ok               |
|          15 | 68.04%   | 280.83%            | -53.65% |     0.67 |       80 | 59.90%     | ok               |
|          25 | 51.20%   | 280.83%            | -56.41% |     0.59 |       79 | 50.75%     | ok               |

## INTU Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 10.49%   | -54.61%            | -34.58% |     0.3  |       67 | 29.12%     | ok               |
|          45 | 1.74%    | -54.61%            | -39.62% |     0.15 |       65 | 32.95%     | ok               |
|          25 | -2.59%   | -54.61%            | -35.13% |     0.1  |       70 | 49.25%     | ok               |
|          40 | -2.80%   | -54.61%            | -41.86% |     0.07 |       67 | 36.94%     | ok               |
|          20 | -8.88%   | -54.61%            | -39.46% |    -0    |       75 | 51.25%     | ok               |

## ITA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -0.05%   | 54.11%             | -21.48% |     0.07 |       76 | 37.94%     | ok               |
|          15 | -1.31%   | 54.11%             | -28.06% |     0.06 |       83 | 60.90%     | ok               |
|          30 | -1.21%   | 54.11%             | -23.75% |     0.04 |       72 | 49.08%     | ok               |
|          35 | -5.74%   | 54.11%             | -23.16% |    -0.1  |       76 | 46.42%     | ok               |
|          40 | -5.69%   | 54.11%             | -20.58% |    -0.11 |       76 | 42.93%     | ok               |

## IWM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | 12.54%   | 38.41%             | -12.34% |     0.49 |       52 | 35.94%     | ok               |
|          20 | 11.05%   | 38.41%             | -12.12% |     0.43 |       58 | 36.94%     | ok               |
|          30 | 8.79%    | 38.41%             | -12.65% |     0.37 |       54 | 35.27%     | ok               |
|          40 | 7.83%    | 38.41%             | -13.94% |     0.37 |       46 | 30.62%     | ok               |
|          15 | 8.49%    | 38.41%             | -13.79% |     0.34 |       74 | 42.60%     | ok               |

## JNJ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 17.23%   | 67.26%             | -10.57% |     0.7  |       42 | 34.94%     | ok               |
|          15 | 13.81%   | 67.26%             | -17.37% |     0.49 |       58 | 54.41%     | ok               |
|          20 | 8.55%    | 67.26%             | -16.96% |     0.35 |       64 | 50.92%     | ok               |
|          45 | 5.96%    | 67.26%             | -13.35% |     0.28 |       48 | 38.94%     | ok               |
|          30 | 6.25%    | 67.26%             | -16.86% |     0.28 |       62 | 47.25%     | ok               |

## JPM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 4.45%    | 67.25%             | -15.90% |     0.21 |       50 | 34.11%     | ok               |
|          45 | -5.96%   | 67.25%             | -21.91% |    -0.12 |       54 | 36.77%     | ok               |
|          20 | -21.19%  | 67.25%             | -35.58% |    -0.45 |       86 | 50.25%     | ok               |
|          35 | -18.22%  | 67.25%             | -27.43% |    -0.5  |       74 | 42.60%     | ok               |
|          40 | -18.87%  | 67.25%             | -28.47% |    -0.53 |       66 | 39.43%     | ok               |

## KO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 22.10%   | 36.06%             | -8.64%  |     0.79 |       54 | 37.94%     | ok               |
|          35 | 17.95%   | 36.06%             | -8.21%  |     0.67 |       58 | 36.44%     | ok               |
|          40 | 15.11%   | 36.06%             | -9.28%  |     0.61 |       60 | 33.11%     | ok               |
|          25 | 15.99%   | 36.06%             | -10.16% |     0.6  |       60 | 40.77%     | ok               |
|          20 | 3.18%    | 36.06%             | -15.99% |     0.17 |       77 | 44.93%     | ok               |

## LDO-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 48.36%   | -44.66%            | -39.99% |     0.61 |       78 | 60.15%     | ok               |
|          20 | 34.97%   | -44.66%            | -43.25% |     0.54 |       80 | 55.36%     | ok               |
|          30 | 10.52%   | -44.66%            | -59.24% |     0.37 |       72 | 46.93%     | ok               |
|          25 | 5.26%    | -44.66%            | -55.04% |     0.34 |       81 | 52.49%     | ok               |
|          35 | -7.24%   | -44.66%            | -61.97% |     0.19 |       78 | 39.46%     | ok               |

## LIN Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -9.08%   | 10.95%             | -22.01% |    -0.26 |       69 | 40.43%     | ok               |
|          20 | -9.83%   | 10.95%             | -23.00% |    -0.28 |       66 | 43.43%     | ok               |
|          15 | -10.45%  | 10.95%             | -23.68% |    -0.3  |       70 | 47.25%     | ok               |
|          30 | -12.12%  | 10.95%             | -20.61% |    -0.39 |       70 | 37.60%     | ok               |
|          35 | -11.72%  | 10.95%             | -19.70% |    -0.41 |       72 | 31.11%     | ok               |

## LINK-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 36.17%   | -3.36%             | -33.64% |     0.55 |       69 | 46.36%     | ok               |
|          45 | 30.10%   | -3.36%             | -33.71% |     0.51 |       54 | 32.76%     | ok               |
|          35 | 13.94%   | -3.36%             | -34.21% |     0.36 |       63 | 42.34%     | ok               |
|          50 | 9.37%    | -3.36%             | -27.98% |     0.3  |       48 | 26.82%     | ok               |
|          40 | 6.57%    | -3.36%             | -34.00% |     0.28 |       59 | 36.78%     | ok               |

## LLY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 1.67%    | 50.87%             | -38.23% |     0.14 |       48 | 35.77%     | ok               |
|          15 | -13.22%  | 50.87%             | -48.12% |    -0.07 |       68 | 60.57%     | ok               |
|          45 | -11.58%  | 50.87%             | -42.66% |    -0.11 |       56 | 39.27%     | ok               |
|          20 | -25.11%  | 50.87%             | -51.34% |    -0.32 |       75 | 55.74%     | ok               |
|          40 | -22.82%  | 50.87%             | -46.23% |    -0.33 |       66 | 42.26%     | ok               |

## LRCX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -1.65%   | 282.61%            | -47.56% |     0.15 |       64 | 39.27%     | ok               |
|          50 | -1.52%   | 282.61%            | -42.40% |     0.14 |       70 | 33.11%     | ok               |
|          45 | -10.63%  | 282.61%            | -47.62% |     0.03 |       70 | 36.77%     | ok               |
|          35 | -14.11%  | 282.61%            | -56.59% |     0.01 |       74 | 41.60%     | ok               |
|          30 | -18.71%  | 282.61%            | -58.79% |    -0.06 |       76 | 42.10%     | ok               |

## LTC-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 29.22%   | -19.56%            | -34.94% |     0.52 |       66 | 46.17%     | ok               |
|          45 | 24.34%   | -19.56%            | -37.46% |     0.48 |       58 | 36.59%     | ok               |
|          30 | 24.45%   | -19.56%            | -32.66% |     0.47 |       67 | 53.45%     | ok               |
|          25 | 17.84%   | -19.56%            | -34.22% |     0.4  |       71 | 55.94%     | ok               |
|          40 | 8.13%    | -19.56%            | -40.31% |     0.29 |       56 | 41.57%     | ok               |

## MCD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 12.48%   | -14.11%            | -9.22%  |     0.58 |       46 | 24.63%     | ok               |
|          45 | 3.04%    | -14.11%            | -16.79% |     0.18 |       52 | 28.45%     | ok               |
|          40 | 1.67%    | -14.11%            | -18.49% |     0.12 |       67 | 31.78%     | ok               |
|          30 | 1.17%    | -14.11%            | -21.88% |     0.1  |       77 | 39.77%     | ok               |
|          25 | 0.61%    | -14.11%            | -23.62% |     0.08 |       75 | 42.10%     | ok               |

## META Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -9.51%   | 58.52%             | -37.10% |    -0.06 |       66 | 39.60%     | ok               |
|          40 | -14.83%  | 58.52%             | -40.49% |    -0.15 |       70 | 43.09%     | ok               |
|          50 | -17.62%  | 58.52%             | -38.63% |    -0.24 |       68 | 35.11%     | ok               |
|          25 | -24.50%  | 58.52%             | -45.35% |    -0.31 |       77 | 53.08%     | ok               |
|          30 | -24.47%  | 58.52%             | -44.52% |    -0.32 |       78 | 50.08%     | ok               |

## MPC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 35.11%   | 143.71%            | -18.24% |     0.67 |       48 | 39.93%     | ok               |
|          40 | 32.84%   | 143.71%            | -20.11% |     0.62 |       60 | 46.59%     | ok               |
|          45 | 30.51%   | 143.71%            | -19.46% |     0.6  |       56 | 43.93%     | ok               |
|          35 | 29.84%   | 143.71%            | -31.08% |     0.56 |       68 | 49.25%     | ok               |
|          30 | 15.76%   | 143.71%            | -37.91% |     0.37 |       71 | 51.91%     | ok               |

## MRK Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -12.07%  | 7.93%              | -28.87% |    -0.14 |       85 | 52.41%     | ok               |
|          25 | -12.85%  | 7.93%              | -31.07% |    -0.17 |       72 | 44.59%     | ok               |
|          50 | -13.54%  | 7.93%              | -23.53% |    -0.27 |       58 | 28.95%     | ok               |
|          20 | -17.12%  | 7.93%              | -29.34% |    -0.27 |       77 | 47.92%     | ok               |
|          45 | -15.69%  | 7.93%              | -25.38% |    -0.3  |       59 | 32.28%     | ok               |

## MS Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 2.71%    | 92.97%             | -19.99% |     0.15 |       70 | 39.60%     | ok               |
|          15 | -0.51%   | 92.97%             | -21.44% |     0.09 |       72 | 58.07%     | ok               |
|          20 | -2.87%   | 92.97%             | -25.13% |     0.02 |       73 | 52.91%     | ok               |
|          30 | -7.91%   | 92.97%             | -27.25% |    -0.11 |       73 | 48.09%     | ok               |
|          35 | -8.52%   | 92.97%             | -26.58% |    -0.13 |       76 | 44.76%     | ok               |

## MSFT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -15.94%  | 26.94%             | -25.54% |    -0.37 |       76 | 36.77%     | ok               |
|          50 | -20.87%  | 26.94%             | -26.37% |    -0.55 |       66 | 31.11%     | ok               |
|          30 | -25.95%  | 26.94%             | -38.06% |    -0.56 |       83 | 50.25%     | ok               |
|          35 | -25.06%  | 26.94%             | -36.28% |    -0.56 |       77 | 45.92%     | ok               |
|          25 | -27.16%  | 26.94%             | -39.13% |    -0.59 |       87 | 53.24%     | ok               |

## MU Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 184.45%  | 765.01%            | -63.96% |     1.16 |       58 | 48.59%     | ok               |
|          15 | 209.17%  | 765.01%            | -61.96% |     1.14 |       51 | 60.23%     | ok               |
|          30 | 155.89%  | 765.01%            | -68.76% |     1.05 |       51 | 53.24%     | ok               |
|          25 | 154.39%  | 765.01%            | -67.90% |     1.04 |       51 | 54.74%     | ok               |
|          35 | 148.82%  | 765.01%            | -69.09% |     1.03 |       63 | 50.92%     | ok               |

## NEAR-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 215.89%  | 113.62%            | -49.95% |     1.31 |       42 | 31.42%     | ok               |
|          45 | 173.82%  | 113.62%            | -42.93% |     1.19 |       42 | 27.39%     | ok               |
|          35 | 153.92%  | 113.62%            | -54.71% |     1.1  |       64 | 36.02%     | ok               |
|          50 | 140.50%  | 113.62%            | -48.58% |     1.09 |       32 | 22.22%     | ok               |
|          30 | 129.53%  | 113.62%            | -52.25% |     0.98 |       73 | 43.87%     | ok               |

## NEM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 4.67%    | 172.77%            | -31.25% |     0.23 |       60 | 58.74%     | ok               |
|          20 | 1.27%    | 172.77%            | -30.50% |     0.18 |       66 | 54.41%     | ok               |
|          25 | -14.22%  | 172.77%            | -39.51% |    -0.04 |       62 | 52.41%     | ok               |
|          50 | -17.87%  | 172.77%            | -33.24% |    -0.15 |       54 | 39.10%     | ok               |
|          30 | -24.97%  | 172.77%            | -39.56% |    -0.23 |       66 | 50.75%     | ok               |

## NFLX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 39.45%   | 9.47%              | -13.37% |     0.88 |       50 | 42.10%     | ok               |
|          50 | 36.08%   | 9.47%              | -16.28% |     0.87 |       44 | 34.44%     | ok               |
|          35 | 38.41%   | 9.47%              | -18.30% |     0.81 |       74 | 46.59%     | ok               |
|          45 | 25.08%   | 9.47%              | -15.48% |     0.63 |       56 | 38.77%     | ok               |
|          15 | 21.62%   | 9.47%              | -26.59% |     0.47 |       71 | 65.06%     | ok               |

## NKE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -16.03%  | -63.37%            | -49.34% |    -0.09 |       83 | 52.75%     | ok               |
|          35 | -14.21%  | -63.37%            | -42.13% |    -0.11 |       71 | 39.93%     | ok               |
|          25 | -19.51%  | -63.37%            | -51.20% |    -0.15 |       83 | 50.08%     | ok               |
|          15 | -21.45%  | -63.37%            | -54.28% |    -0.18 |       86 | 56.57%     | ok               |
|          30 | -23.35%  | -63.37%            | -55.35% |    -0.23 |       79 | 46.09%     | ok               |

## NOW Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 9.21%    | -6.81%             | -30.43% |     0.28 |       84 | 50.58%     | ok               |
|          20 | 6.76%    | -6.81%             | -39.71% |     0.26 |       79 | 56.91%     | ok               |
|          25 | 4.06%    | -6.81%             | -37.51% |     0.23 |       76 | 54.08%     | ok               |
|          15 | -1.04%   | -6.81%             | -43.06% |     0.17 |       87 | 59.90%     | ok               |
|          40 | -2.21%   | -6.81%             | -36.21% |     0.12 |       74 | 40.10%     | ok               |

## NVDA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -29.80%  | 87.52%             | -41.21% |    -0.4  |       76 | 43.67%     | ok               |
|          20 | -39.13%  | 87.52%             | -42.85% |    -0.51 |       76 | 51.69%     | ok               |
|          25 | -39.03%  | 87.52%             | -42.76% |    -0.56 |       77 | 46.70%     | ok               |
|          15 | -45.72%  | 87.52%             | -52.37% |    -0.61 |       77 | 54.90%     | ok               |
|          35 | -41.17%  | 87.52%             | -48.32% |    -0.7  |       84 | 40.64%     | ok               |

## OP-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 17.50%   | -80.29%            | -31.68% |     0.4  |       32 | 9.96%      | ok               |
|          45 | 0.02%    | -80.29%            | -51.17% |     0.19 |       36 | 14.94%     | ok               |
|          40 | -21.62%  | -80.29%            | -60.08% |    -0.08 |       48 | 23.18%     | ok               |
|          30 | -37.66%  | -80.29%            | -68.74% |    -0.25 |       68 | 33.91%     | ok               |
|          35 | -41.17%  | -80.29%            | -63.95% |    -0.37 |       56 | 27.97%     | ok               |

## ORCL Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 183.21%  | 22.44%             | -32.54% |     1.17 |       69 | 62.90%     | ok               |
|          25 | 127.71%  | 22.44%             | -27.76% |     0.98 |       61 | 55.41%     | ok               |
|          20 | 121.36%  | 22.44%             | -29.32% |     0.95 |       70 | 58.57%     | ok               |
|          45 | 103.81%  | 22.44%             | -32.35% |     0.94 |       58 | 40.77%     | ok               |
|          35 | 108.85%  | 22.44%             | -31.95% |     0.93 |       62 | 49.42%     | ok               |

## OXY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -0.67%   | -7.31%             | -28.48% |     0.11 |       69 | 42.26%     | ok               |
|          35 | -2.70%   | -7.31%             | -26.44% |     0.07 |       72 | 38.10%     | ok               |
|          50 | -6.31%   | -7.31%             | -27.98% |    -0.03 |       44 | 26.96%     | ok               |
|          40 | -8.69%   | -7.31%             | -28.30% |    -0.06 |       62 | 33.94%     | ok               |
|          25 | -14.41%  | -7.31%             | -38.51% |    -0.13 |       77 | 45.76%     | ok               |

## PEP Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 17.85%   | -30.54%            | -11.62% |     0.76 |       40 | 25.62%     | ok               |
|          45 | 10.32%   | -30.54%            | -14.22% |     0.46 |       56 | 29.62%     | ok               |
|          35 | 6.63%    | -30.54%            | -21.42% |     0.27 |       77 | 40.10%     | ok               |
|          40 | 4.34%    | -30.54%            | -18.04% |     0.21 |       70 | 35.44%     | ok               |
|          30 | 1.91%    | -30.54%            | -21.35% |     0.13 |       74 | 46.09%     | ok               |

## PEPE-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -45.63%  | -47.51%            | -60.33% |    -0.22 |       93 | 54.21%     | ok               |
|          15 | -53.56%  | -47.51%            | -64.84% |    -0.23 |       82 | 63.22%     | ok               |
|          30 | -45.68%  | -47.51%            | -61.29% |    -0.24 |       85 | 49.43%     | ok               |
|          20 | -52.41%  | -47.51%            | -64.07% |    -0.28 |       88 | 59.96%     | ok               |
|          35 | -47.51%  | -47.51%            | -61.54% |    -0.35 |       74 | 44.44%     | ok               |

## PFE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -15.89%  | -3.62%             | -23.37% |    -0.5  |       52 | 21.63%     | ok               |
|          40 | -17.46%  | -3.62%             | -27.08% |    -0.53 |       72 | 26.62%     | ok               |
|          50 | -16.36%  | -3.62%             | -25.42% |    -0.57 |       40 | 18.47%     | ok               |
|          35 | -24.20%  | -3.62%             | -32.87% |    -0.73 |       84 | 33.61%     | ok               |
|          30 | -33.95%  | -3.62%             | -41.90% |    -1.03 |       81 | 37.77%     | ok               |

## PG Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -9.96%   | -12.02%            | -17.50% |    -0.39 |       54 | 28.79%     | ok               |
|          35 | -15.32%  | -12.02%            | -18.57% |    -0.61 |       62 | 32.45%     | ok               |
|          45 | -19.17%  | -12.02%            | -20.34% |    -0.88 |       54 | 26.12%     | ok               |
|          30 | -23.02%  | -12.02%            | -24.16% |    -0.92 |       64 | 35.61%     | ok               |
|          25 | -24.77%  | -12.02%            | -25.86% |    -1    |       76 | 37.10%     | ok               |

## PM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | -3.85%   | 90.89%             | -32.20% |     0    |       84 | 47.75%     | ok               |
|          20 | -6.36%   | 90.89%             | -33.51% |    -0.05 |       83 | 56.41%     | ok               |
|          30 | -6.86%   | 90.89%             | -35.15% |    -0.06 |       79 | 51.25%     | ok               |
|          40 | -11.19%  | 90.89%             | -37.94% |    -0.2  |       78 | 43.76%     | ok               |
|          50 | -10.72%  | 90.89%             | -35.70% |    -0.21 |       68 | 37.94%     | ok               |

## POL-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 29.19%   | -52.83%            | -38.69% |     0.5  |       81 | 50.00%     | ok               |
|          25 | 4.63%    | -52.83%            | -41.49% |     0.28 |       74 | 55.56%     | ok               |
|          20 | -6.99%   | -52.83%            | -48.76% |     0.17 |       82 | 59.58%     | ok               |
|          40 | -5.77%   | -52.83%            | -33.57% |     0.12 |       58 | 31.23%     | ok               |
|          50 | -7.18%   | -52.83%            | -29.40% |     0.05 |       52 | 21.46%     | ok               |

## QCOM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -7.55%   | -1.86%             | -56.84% |     0.09 |       73 | 46.09%     | ok               |
|          35 | -13.05%  | -1.86%             | -51.84% |    -0    |       79 | 41.93%     | ok               |
|          20 | -15.53%  | -1.86%             | -57.31% |    -0.01 |       68 | 49.58%     | ok               |
|          30 | -23.20%  | -1.86%             | -57.69% |    -0.15 |       77 | 44.43%     | ok               |
|          15 | -25.74%  | -1.86%             | -60.65% |    -0.15 |       70 | 52.25%     | ok               |

## QQQ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 28.39%   | 70.67%             | -14.17% |     0.68 |       61 | 53.58%     | ok               |
|          25 | 19.68%   | 70.67%             | -12.88% |     0.55 |       59 | 47.59%     | ok               |
|          20 | 18.45%   | 70.67%             | -12.98% |     0.51 |       67 | 50.25%     | ok               |
|          30 | 11.60%   | 70.67%             | -14.20% |     0.37 |       64 | 45.59%     | ok               |
|          35 | 0.13%    | 70.67%             | -20.59% |     0.08 |       70 | 41.76%     | ok               |

## RENDER-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 37.06%   | -55.14%            | -43.43% |     0.55 |       91 | 57.47%     | ok               |
|          25 | 30.72%   | -55.14%            | -40.60% |     0.51 |       91 | 52.49%     | ok               |
|          15 | 29.21%   | -55.14%            | -44.59% |     0.51 |       88 | 60.73%     | ok               |
|          30 | -15.41%  | -55.14%            | -44.84% |     0.12 |       94 | 46.74%     | ok               |
|          35 | -27.79%  | -55.14%            | -44.76% |    -0.08 |       82 | 39.66%     | ok               |

## RTX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 44.84%   | 74.22%             | -18.66% |     0.92 |       74 | 57.24%     | ok               |
|          25 | 39.89%   | 74.22%             | -18.59% |     0.85 |       62 | 54.58%     | ok               |
|          15 | 36.08%   | 74.22%             | -19.55% |     0.77 |       67 | 61.73%     | ok               |
|          30 | 31.34%   | 74.22%             | -16.99% |     0.72 |       64 | 52.41%     | ok               |
|          35 | 23.62%   | 74.22%             | -18.00% |     0.63 |       58 | 49.25%     | ok               |

## SBUX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -0.41%   | 23.96%             | -23.55% |     0.09 |       53 | 40.60%     | ok               |
|          40 | -6.83%   | 23.96%             | -25.43% |    -0.08 |       62 | 33.44%     | ok               |
|          45 | -8.35%   | 23.96%             | -27.26% |    -0.14 |       68 | 28.12%     | ok               |
|          30 | -11.73%  | 23.96%             | -29.22% |    -0.17 |       58 | 38.60%     | ok               |
|          20 | -14.58%  | 23.96%             | -30.94% |    -0.2  |       58 | 42.43%     | ok               |

## SCHW Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -0.70%   | 31.14%             | -16.53% |     0.05 |       60 | 31.61%     | ok               |
|          25 | -4.00%   | 31.14%             | -28.76% |    -0    |       67 | 48.59%     | ok               |
|          20 | -8.86%   | 31.14%             | -29.24% |    -0.12 |       75 | 51.08%     | ok               |
|          50 | -6.31%   | 31.14%             | -13.28% |    -0.16 |       54 | 28.62%     | ok               |
|          40 | -11.10%  | 31.14%             | -23.35% |    -0.24 |       70 | 35.77%     | ok               |

## SHIB-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -27.21%  | -55.05%            | -40.57% |    -0.13 |       76 | 58.43%     | ok               |
|          15 | -31.02%  | -55.05%            | -45.04% |    -0.17 |       86 | 66.67%     | ok               |
|          20 | -33.41%  | -55.05%            | -44.18% |    -0.22 |       80 | 61.69%     | ok               |
|          35 | -35.01%  | -55.05%            | -45.32% |    -0.34 |       72 | 45.40%     | ok               |
|          30 | -40.94%  | -55.05%            | -42.45% |    -0.42 |       78 | 51.72%     | ok               |

## SHY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd    |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:-------|---------:|---------:|:-----------|:-----------------|
|          30 | -1.63%   | -0.27%             | -3.18% |    -0.55 |       46 | 36.94%     | ok               |
|          35 | -2.24%   | -0.27%             | -3.49% |    -0.77 |       52 | 35.44%     | ok               |
|          40 | -2.38%   | -0.27%             | -3.58% |    -0.82 |       54 | 33.94%     | ok               |
|          45 | -2.40%   | -0.27%             | -3.43% |    -0.88 |       54 | 28.62%     | ok               |
|          25 | -2.79%   | -0.27%             | -4.32% |    -0.92 |       60 | 38.77%     | ok               |

## SKY-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -50.14%  | 38.68%             | -64.97% |    -0.55 |       73 | 54.60%     | ok               |
|          30 | -46.91%  | 38.68%             | -61.34% |    -0.57 |       87 | 45.40%     | ok               |
|          25 | -52.47%  | 38.68%             | -65.39% |    -0.67 |       80 | 48.66%     | ok               |
|          20 | -57.29%  | 38.68%             | -69.99% |    -0.74 |       75 | 52.11%     | ok               |
|          35 | -51.37%  | 38.68%             | -60.18% |    -0.75 |       80 | 37.74%     | ok               |

## SLB Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 9.41%    | 3.14%              | -26.32% |     0.29 |       48 | 35.11%     | ok               |
|          45 | 9.14%    | 3.14%              | -23.11% |     0.28 |       58 | 31.61%     | ok               |
|          50 | -6.14%   | 3.14%              | -29.27% |    -0.05 |       48 | 27.29%     | ok               |
|          35 | -18.44%  | 3.14%              | -44.37% |    -0.27 |       70 | 41.93%     | ok               |
|          25 | -36.78%  | 3.14%              | -55.72% |    -0.67 |       88 | 53.24%     | ok               |

## SLV Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 45.49%   | 113.68%            | -34.10% |     0.67 |       52 | 30.62%     | ok               |
|          45 | 33.14%   | 113.68%            | -31.82% |     0.55 |       63 | 32.11%     | ok               |
|          40 | 32.08%   | 113.68%            | -34.28% |     0.54 |       67 | 34.11%     | ok               |
|          20 | 21.26%   | 113.68%            | -42.66% |     0.42 |       70 | 44.43%     | ok               |
|          15 | 21.25%   | 113.68%            | -47.98% |     0.42 |       71 | 49.25%     | ok               |

## SMH Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 86.52%   | 183.93%            | -31.66% |     1.13 |       47 | 46.76%     | ok               |
|          25 | 68.83%   | 183.93%            | -33.57% |     1    |       44 | 45.42%     | ok               |
|          35 | 67.03%   | 183.93%            | -34.65% |     0.99 |       54 | 42.43%     | ok               |
|          30 | 64.23%   | 183.93%            | -34.29% |     0.96 |       48 | 44.09%     | ok               |
|          45 | 52.27%   | 183.93%            | -33.35% |     0.89 |       54 | 36.61%     | ok               |

## SNX-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -15.94%  | -62.79%            | -50.65% |     0.08 |       71 | 44.25%     | ok               |
|          35 | -11.36%  | -62.79%            | -41.29% |     0.08 |       56 | 27.97%     | ok               |
|          40 | -11.41%  | -62.79%            | -36.00% |     0.01 |       46 | 22.99%     | ok               |
|          30 | -21.23%  | -62.79%            | -50.27% |    -0.04 |       62 | 34.10%     | ok               |
|          15 | -39.26%  | -62.79%            | -52.44% |    -0.21 |       77 | 48.85%     | ok               |

## SOL-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 52.74%   | -18.64%            | -38.17% |     0.71 |       58 | 41.19%     | ok               |
|          35 | 27.28%   | -18.64%            | -43.70% |     0.49 |       70 | 47.70%     | ok               |
|          45 | 8.17%    | -18.64%            | -46.83% |     0.29 |       60 | 35.63%     | ok               |
|          25 | 3.84%    | -18.64%            | -41.09% |     0.27 |       70 | 58.24%     | ok               |
|          30 | 0.98%    | -18.64%            | -45.53% |     0.23 |       78 | 53.83%     | ok               |

## SOXX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | 80.65%   | 167.11%            | -39.32% |     1.04 |       53 | 44.93%     | ok               |
|          35 | 76.58%   | 167.11%            | -38.76% |     1.03 |       56 | 40.43%     | ok               |
|          30 | 75.63%   | 167.11%            | -39.81% |     1.01 |       54 | 42.76%     | ok               |
|          20 | 64.70%   | 167.11%            | -39.19% |     0.89 |       59 | 45.92%     | ok               |
|          45 | 49.14%   | 167.11%            | -37.15% |     0.8  |       60 | 35.61%     | ok               |

## SPY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 12.91%   | 48.75%             | -14.25% |     0.47 |       59 | 54.24%     | ok               |
|          15 | 12.37%   | 48.75%             | -16.80% |     0.45 |       63 | 56.91%     | ok               |
|          25 | 7.84%    | 48.75%             | -14.25% |     0.32 |       59 | 53.24%     | ok               |
|          30 | 1.58%    | 48.75%             | -15.53% |     0.12 |       64 | 50.58%     | ok               |
|          35 | 0.60%    | 48.75%             | -15.58% |     0.08 |       62 | 47.42%     | ok               |

## SUSHI-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -14.03%  | -60.13%            | -34.75% |    -0.04 |       58 | 17.05%     | ok               |
|          45 | -60.31%  | -60.13%            | -64.10% |    -0.83 |       60 | 22.03%     | ok               |
|          40 | -63.38%  | -60.13%            | -66.52% |    -0.84 |       63 | 28.54%     | ok               |
|          15 | -77.05%  | -60.13%            | -80.55% |    -0.94 |       86 | 50.00%     | ok               |
|          35 | -71.02%  | -60.13%            | -73.80% |    -1    |       84 | 33.72%     | ok               |

## T Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 60.84%   | 40.44%             | -15.08% |     1.09 |       71 | 65.56%     | ok               |
|          20 | 56.87%   | 40.44%             | -18.13% |     1.07 |       66 | 61.06%     | ok               |
|          25 | 55.09%   | 40.44%             | -17.66% |     1.05 |       66 | 58.90%     | ok               |
|          30 | 40.65%   | 40.44%             | -17.01% |     0.86 |       70 | 56.74%     | ok               |
|          35 | 25.32%   | 40.44%             | -14.49% |     0.62 |       76 | 52.41%     | ok               |

## TGT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -11.80%  | -4.92%             | -34.98% |    -0.18 |       62 | 37.77%     | ok               |
|          20 | -15.43%  | -4.92%             | -38.94% |    -0.22 |       88 | 45.59%     | ok               |
|          45 | -11.70%  | -4.92%             | -25.62% |    -0.22 |       50 | 28.62%     | ok               |
|          25 | -15.93%  | -4.92%             | -38.33% |    -0.27 |       72 | 40.93%     | ok               |
|          15 | -21.63%  | -4.92%             | -38.69% |    -0.34 |       76 | 50.58%     | ok               |

## TIA-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -55.60%  | -81.23%            | -66.82% |    -0.28 |       97 | 59.20%     | ok               |
|          35 | -46.53%  | -81.23%            | -65.93% |    -0.38 |       74 | 35.44%     | ok               |
|          25 | -65.35%  | -81.23%            | -70.91% |    -0.58 |       96 | 48.28%     | ok               |
|          20 | -67.70%  | -81.23%            | -71.78% |    -0.58 |       93 | 53.64%     | ok               |
|          40 | -54.84%  | -81.23%            | -71.23% |    -0.6  |       78 | 29.50%     | ok               |

## TLT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -10.88%  | -14.65%            | -14.46% |    -1.2  |       38 | 16.97%     | ok               |
|          30 | -17.59%  | -14.65%            | -22.36% |    -1.28 |       70 | 34.11%     | ok               |
|          40 | -15.35%  | -14.65%            | -17.85% |    -1.34 |       56 | 25.12%     | ok               |
|          45 | -14.67%  | -14.65%            | -17.21% |    -1.52 |       44 | 20.47%     | ok               |
|          15 | -23.77%  | -14.65%            | -28.21% |    -1.6  |       81 | 41.76%     | ok               |

## TMO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 56.62%   | 14.57%             | -8.17%  |     1.17 |       48 | 35.44%     | ok               |
|          45 | 44.62%   | 14.57%             | -9.69%  |     0.94 |       52 | 40.10%     | ok               |
|          40 | 40.39%   | 14.57%             | -9.91%  |     0.85 |       57 | 44.93%     | ok               |
|          35 | 36.86%   | 14.57%             | -13.84% |     0.75 |       67 | 50.08%     | ok               |
|          20 | 27.72%   | 14.57%             | -22.89% |     0.57 |       78 | 60.23%     | ok               |

## TMUS Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 3.84%    | 0.79%              | -27.54% |     0.18 |       76 | 47.75%     | ok               |
|          15 | -0.10%   | 0.79%              | -34.79% |     0.1  |       70 | 60.23%     | ok               |
|          25 | -3.96%   | 0.79%              | -32.84% |     0.02 |       79 | 50.58%     | ok               |
|          20 | -5.87%   | 0.79%              | -33.40% |    -0.02 |       76 | 54.58%     | ok               |
|          50 | -5.53%   | 0.79%              | -30.24% |    -0.08 |       60 | 34.28%     | ok               |

## TRX-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 19.40%   | 36.85%             | -18.79% |     0.62 |       54 | 40.42%     | ok               |
|          35 | 12.97%   | 36.85%             | -21.77% |     0.43 |       68 | 49.23%     | ok               |
|          20 | 12.33%   | 36.85%             | -25.45% |     0.39 |       61 | 59.39%     | ok               |
|          30 | 10.93%   | 36.85%             | -22.90% |     0.38 |       68 | 52.30%     | ok               |
|          25 | 8.24%    | 36.85%             | -26.84% |     0.3  |       66 | 55.94%     | ok               |

## TSLA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 41.47%   | 120.33%            | -30.57% |     0.6  |       64 | 30.12%     | ok               |
|          40 | 13.71%   | 120.33%            | -50.11% |     0.34 |       63 | 35.61%     | ok               |
|          45 | -10.53%  | 120.33%            | -52.01% |     0.07 |       69 | 32.61%     | ok               |
|          35 | -18.00%  | 120.33%            | -58.86% |     0    |       74 | 38.27%     | ok               |
|          30 | -36.44%  | 120.33%            | -58.36% |    -0.25 |       80 | 43.26%     | ok               |

## TXN Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 18.05%   | 57.01%             | -45.45% |     0.4  |       66 | 32.61%     | ok               |
|          35 | -2.74%   | 57.01%             | -43.38% |     0.09 |       76 | 46.92%     | ok               |
|          40 | -3.73%   | 57.01%             | -45.67% |     0.08 |       72 | 44.76%     | ok               |
|          20 | -10.28%  | 57.01%             | -38.98% |     0.01 |       70 | 56.74%     | ok               |
|          45 | -7.38%   | 57.01%             | -46.24% |     0.01 |       80 | 38.94%     | ok               |

## UNH Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 25.40%   | -26.02%            | -36.91% |     0.49 |       54 | 28.95%     | ok               |
|          30 | 25.63%   | -26.02%            | -26.31% |     0.47 |       74 | 48.92%     | ok               |
|          20 | 23.40%   | -26.02%            | -26.96% |     0.44 |       77 | 57.90%     | ok               |
|          15 | 23.36%   | -26.02%            | -26.07% |     0.44 |       82 | 64.06%     | ok               |
|          35 | 21.77%   | -26.02%            | -27.49% |     0.43 |       68 | 43.93%     | ok               |

## UNI-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 42.92%   | 72.48%             | -45.09% |     0.61 |       52 | 26.82%     | ok               |
|          45 | 31.24%   | 72.48%             | -51.70% |     0.52 |       58 | 34.48%     | ok               |
|          40 | 19.68%   | 72.48%             | -61.16% |     0.43 |       62 | 39.85%     | ok               |
|          35 | 4.97%    | 72.48%             | -65.47% |     0.32 |       72 | 45.40%     | ok               |
|          20 | -51.30%  | 72.48%             | -80.78% |    -0.22 |       95 | 60.73%     | ok               |

## UPS Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | -28.03%  | -38.15%            | -31.52% |    -0.52 |       64 | 35.94%     | ok               |
|          40 | -28.15%  | -38.15%            | -31.55% |    -0.54 |       60 | 30.62%     | ok               |
|          20 | -34.00%  | -38.15%            | -39.10% |    -0.62 |       86 | 48.59%     | ok               |
|          30 | -33.96%  | -38.15%            | -39.06% |    -0.66 |       72 | 41.76%     | ok               |
|          25 | -34.53%  | -38.15%            | -39.59% |    -0.66 |       78 | 45.26%     | ok               |

## USO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 7.46%    | 89.14%             | -32.38% |     0.25 |       48 | 25.96%     | ok               |
|          20 | 4.04%    | 89.14%             | -44.49% |     0.2  |       77 | 38.10%     | ok               |
|          15 | 0.77%    | 89.14%             | -45.41% |     0.16 |       71 | 41.43%     | ok               |
|          25 | -4.56%   | 89.14%             | -46.08% |     0.08 |       71 | 35.44%     | ok               |
|          50 | -3.42%   | 89.14%             | -29.54% |     0.07 |       52 | 24.13%     | ok               |

## VEA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 6.06%    | 41.27%             | -14.62% |     0.27 |       55 | 48.92%     | ok               |
|          20 | -0.11%   | 41.27%             | -16.33% |     0.05 |       59 | 46.26%     | ok               |
|          25 | -3.09%   | 41.27%             | -16.77% |    -0.07 |       55 | 44.76%     | ok               |
|          30 | -3.38%   | 41.27%             | -16.28% |    -0.09 |       58 | 43.26%     | ok               |
|          35 | -3.45%   | 41.27%             | -14.81% |    -0.09 |       52 | 41.60%     | ok               |

## VIXY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -56.34%  | -65.97%            | -69.78% |    -0.67 |       36 | 10.15%     | ok               |
|          15 | -77.55%  | -65.97%            | -89.47% |    -0.81 |       95 | 44.09%     | ok               |
|          45 | -65.70%  | -65.97%            | -75.03% |    -0.87 |       56 | 15.14%     | ok               |
|          30 | -78.22%  | -65.97%            | -88.19% |    -0.94 |       94 | 33.28%     | ok               |
|          40 | -73.09%  | -65.97%            | -80.72% |    -1    |       68 | 18.97%     | ok               |

## VNQ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -9.80%   | 7.20%              | -22.34% |    -0.35 |       69 | 42.76%     | ok               |
|          45 | -9.15%   | 7.20%              | -19.07% |    -0.4  |       62 | 29.45%     | ok               |
|          30 | -11.82%  | 7.20%              | -24.92% |    -0.46 |       73 | 40.10%     | ok               |
|          50 | -10.05%  | 7.20%              | -17.13% |    -0.46 |       54 | 26.12%     | ok               |
|          35 | -12.85%  | 7.20%              | -27.01% |    -0.52 |       76 | 37.60%     | ok               |

## VTI Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 11.67%   | 47.41%             | -14.91% |     0.43 |       62 | 54.58%     | ok               |
|          15 | 7.08%    | 47.41%             | -17.19% |     0.29 |       59 | 56.91%     | ok               |
|          25 | 1.55%    | 47.41%             | -15.00% |     0.11 |       58 | 52.58%     | ok               |
|          30 | -6.07%   | 47.41%             | -17.64% |    -0.16 |       68 | 50.58%     | ok               |
|          40 | -7.20%   | 47.41%             | -19.77% |    -0.23 |       72 | 43.09%     | ok               |

## VWO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -10.91%  | 38.38%             | -23.57% |    -0.4  |       68 | 34.94%     | ok               |
|          45 | -11.15%  | 38.38%             | -24.34% |    -0.42 |       60 | 31.95%     | ok               |
|          50 | -11.44%  | 38.38%             | -24.06% |    -0.45 |       56 | 29.12%     | ok               |
|          15 | -14.70%  | 38.38%             | -26.00% |    -0.47 |       73 | 48.09%     | ok               |
|          20 | -16.06%  | 38.38%             | -28.09% |    -0.54 |       70 | 45.76%     | ok               |

## VZ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 0.49%    | 13.10%             | -12.55% |     0.08 |       56 | 28.29%     | ok               |
|          45 | -11.05%  | 13.10%             | -21.44% |    -0.3  |       68 | 32.11%     | ok               |
|          35 | -11.70%  | 13.10%             | -22.73% |    -0.31 |       62 | 37.77%     | ok               |
|          25 | -13.25%  | 13.10%             | -22.13% |    -0.32 |       81 | 45.59%     | ok               |
|          40 | -15.36%  | 13.10%             | -24.21% |    -0.45 |       66 | 35.27%     | ok               |

## WFC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | -6.72%   | 32.94%             | -21.57% |    -0.07 |       77 | 44.59%     | ok               |
|          50 | -5.77%   | 32.94%             | -18.29% |    -0.12 |       60 | 32.78%     | ok               |
|          30 | -16.44%  | 32.94%             | -28.90% |    -0.26 |       80 | 47.75%     | ok               |
|          40 | -12.49%  | 32.94%             | -23.94% |    -0.29 |       72 | 41.26%     | ok               |
|          20 | -19.59%  | 32.94%             | -31.40% |    -0.29 |       79 | 52.91%     | ok               |

## WIF-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 83.08%   | -56.74%            | -40.67% |     0.76 |       67 | 44.06%     | ok               |
|          15 | 43.07%   | -56.74%            | -46.21% |     0.58 |       77 | 47.32%     | ok               |
|          25 | 16.57%   | -56.74%            | -44.74% |     0.41 |       65 | 40.04%     | ok               |
|          30 | -26.25%  | -56.74%            | -52.76% |    -0.01 |       64 | 36.97%     | ok               |
|          40 | -20.96%  | -56.74%            | -51.66% |    -0.06 |       58 | 25.10%     | ok               |

## WMT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 35.95%   | 73.93%             | -12.15% |     1.09 |       36 | 37.27%     | ok               |
|          45 | 37.60%   | 73.93%             | -12.34% |     1.09 |       42 | 39.43%     | ok               |
|          35 | 27.56%   | 73.93%             | -16.55% |     0.8  |       58 | 45.76%     | ok               |
|          40 | 25.92%   | 73.93%             | -16.82% |     0.78 |       50 | 41.10%     | ok               |
|          15 | 8.84%    | 73.93%             | -25.74% |     0.29 |       82 | 59.73%     | ok               |

## XBI Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 13.07%   | 73.78%             | -16.08% |     0.39 |       54 | 35.61%     | ok               |
|          45 | 8.78%    | 73.78%             | -15.46% |     0.3  |       52 | 33.11%     | ok               |
|          35 | 1.39%    | 73.78%             | -16.96% |     0.12 |       62 | 38.44%     | ok               |
|          30 | -0.72%   | 73.78%             | -18.30% |     0.07 |       64 | 39.93%     | ok               |
|          50 | -0.58%   | 73.78%             | -15.97% |     0.06 |       52 | 29.95%     | ok               |

## XLB Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -3.46%   | 7.87%              | -16.40% |    -0.1  |       40 | 23.13%     | ok               |
|          40 | -3.87%   | 7.87%              | -18.27% |    -0.1  |       56 | 27.12%     | ok               |
|          45 | -6.45%   | 7.87%              | -18.10% |    -0.22 |       44 | 24.63%     | ok               |
|          35 | -7.14%   | 7.87%              | -21.38% |    -0.22 |       56 | 30.62%     | ok               |
|          25 | -11.45%  | 7.87%              | -23.37% |    -0.38 |       64 | 35.94%     | ok               |

## XLC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 12.62%   | 36.71%             | -12.33% |     0.47 |       61 | 50.25%     | ok               |
|          25 | 12.06%   | 36.71%             | -12.31% |     0.45 |       60 | 52.41%     | ok               |
|          50 | 8.47%    | 36.71%             | -11.12% |     0.43 |       64 | 38.77%     | ok               |
|          40 | 8.61%    | 36.71%             | -13.38% |     0.37 |       60 | 44.09%     | ok               |
|          35 | 7.08%    | 36.71%             | -13.38% |     0.31 |       60 | 47.75%     | ok               |

## XLE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -1.77%   | 35.61%             | -25.98% |     0.03 |       54 | 35.94%     | ok               |
|          35 | -7.42%   | 35.61%             | -28.88% |    -0.11 |       67 | 42.43%     | ok               |
|          45 | -6.64%   | 35.61%             | -29.68% |    -0.11 |       60 | 37.94%     | ok               |
|          30 | -11.02%  | 35.61%             | -32.20% |    -0.2  |       71 | 44.26%     | ok               |
|          25 | -13.16%  | 35.61%             | -33.83% |    -0.25 |       80 | 47.42%     | ok               |

## XLF Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -1.39%   | 29.33%             | -18.63% |     0.02 |       72 | 51.58%     | ok               |
|          15 | -3.49%   | 29.33%             | -20.19% |    -0.05 |       76 | 54.24%     | ok               |
|          25 | -8.26%   | 29.33%             | -23.22% |    -0.24 |       79 | 48.42%     | ok               |
|          30 | -8.86%   | 29.33%             | -23.61% |    -0.27 |       80 | 46.42%     | ok               |
|          35 | -15.96%  | 29.33%             | -24.48% |    -0.61 |       70 | 42.76%     | ok               |

## XLI Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 6.00%    | 35.92%             | -12.74% |     0.26 |       84 | 51.08%     | ok               |
|          20 | 3.74%    | 35.92%             | -12.74% |     0.19 |       73 | 46.26%     | ok               |
|          50 | -4.76%   | 35.92%             | -14.94% |    -0.18 |       60 | 31.78%     | ok               |
|          45 | -5.38%   | 35.92%             | -16.29% |    -0.19 |       70 | 34.28%     | ok               |
|          25 | -6.69%   | 35.92%             | -15.60% |    -0.21 |       76 | 44.26%     | ok               |

## XLK Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 80.64%   | 94.60%             | -14.75% |     1.32 |       44 | 49.75%     | ok               |
|          25 | 74.57%   | 94.60%             | -14.75% |     1.29 |       40 | 47.92%     | ok               |
|          15 | 78.80%   | 94.60%             | -14.75% |     1.26 |       44 | 51.58%     | ok               |
|          30 | 64.12%   | 94.60%             | -14.75% |     1.19 |       40 | 46.59%     | ok               |
|          35 | 47.54%   | 94.60%             | -13.43% |     0.98 |       54 | 43.93%     | ok               |

## XLM-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 5.66%    | -20.50%            | -48.81% |     0.26 |       44 | 27.20%     | ok               |
|          25 | 2.35%    | -20.50%            | -49.14% |     0.25 |       67 | 50.00%     | ok               |
|          45 | 4.49%    | -20.50%            | -51.28% |     0.25 |       54 | 32.18%     | ok               |
|          30 | -5.09%   | -20.50%            | -54.58% |     0.17 |       65 | 47.70%     | ok               |
|          40 | -9.25%   | -20.50%            | -47.28% |     0.1  |       51 | 37.36%     | ok               |

## XLP Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 7.37%    | 4.70%              | -6.85%  |     0.49 |       54 | 29.28%     | ok               |
|          40 | 6.68%    | 4.70%              | -7.77%  |     0.43 |       68 | 33.61%     | ok               |
|          35 | 5.75%    | 4.70%              | -9.73%  |     0.37 |       64 | 36.61%     | ok               |
|          50 | 4.18%    | 4.70%              | -7.01%  |     0.3  |       58 | 27.45%     | ok               |
|          30 | 3.41%    | 4.70%              | -11.56% |     0.23 |       68 | 37.94%     | ok               |

## XLU Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 6.49%    | 12.17%             | -13.94% |     0.35 |       54 | 31.61%     | ok               |
|          45 | 5.33%    | 12.17%             | -14.88% |     0.29 |       58 | 32.78%     | ok               |
|          40 | 2.15%    | 12.17%             | -16.41% |     0.14 |       64 | 34.61%     | ok               |
|          35 | -0.57%   | 12.17%             | -19.71% |     0.02 |       64 | 37.27%     | ok               |
|          30 | -1.95%   | 12.17%             | -20.40% |    -0.04 |       69 | 40.60%     | ok               |

## XLV Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -20.50%  | 16.67%             | -22.40% |    -0.95 |       76 | 39.60%     | ok               |
|          30 | -20.86%  | 16.67%             | -22.75% |    -0.99 |       76 | 37.94%     | ok               |
|          15 | -23.78%  | 16.67%             | -25.35% |    -1.09 |       83 | 43.76%     | ok               |
|          20 | -23.62%  | 16.67%             | -25.19% |    -1.11 |       79 | 41.26%     | ok               |
|          35 | -24.81%  | 16.67%             | -26.58% |    -1.27 |       70 | 34.94%     | ok               |

## XLY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 0.52%    | 24.16%             | -15.77% |     0.09 |       76 | 54.08%     | ok               |
|          30 | -4.12%   | 24.16%             | -18.35% |    -0.06 |       75 | 47.59%     | ok               |
|          20 | -4.80%   | 24.16%             | -19.25% |    -0.07 |       72 | 50.75%     | ok               |
|          25 | -6.93%   | 24.16%             | -19.98% |    -0.14 |       69 | 49.25%     | ok               |
|          50 | -6.34%   | 24.16%             | -15.82% |    -0.22 |       62 | 32.11%     | ok               |

## XOM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | 2.73%    | 39.09%             | -19.90% |     0.15 |       55 | 34.94%     | ok               |
|          30 | 1.71%    | 39.09%             | -20.29% |     0.12 |       55 | 34.28%     | ok               |
|          50 | 0.63%    | 39.09%             | -21.35% |     0.09 |       36 | 26.96%     | ok               |
|          45 | -3.17%   | 39.09%             | -23.33% |    -0.02 |       42 | 28.29%     | ok               |
|          20 | -4.53%   | 39.09%             | -25.56% |    -0.05 |       64 | 37.10%     | ok               |

## XRP-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 25.43%   | -31.76%            | -31.38% |     0.47 |       72 | 43.30%     | ok               |
|          40 | 8.72%    | -31.76%            | -33.91% |     0.3  |       64 | 36.97%     | ok               |
|          30 | -1.42%   | -31.76%            | -31.82% |     0.19 |       67 | 48.08%     | ok               |
|          45 | -2.35%   | -31.76%            | -37.18% |     0.16 |       60 | 32.57%     | ok               |
|          50 | -6.49%   | -31.76%            | -39.26% |     0.09 |       58 | 24.90%     | ok               |

## YFI-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -44.94%  | -53.71%            | -49.08% |    -0.73 |       56 | 27.39%     | ok               |
|          45 | -45.03%  | -53.71%            | -49.16% |    -0.94 |       70 | 22.03%     | ok               |
|          35 | -62.88%  | -53.71%            | -63.61% |    -1.12 |       63 | 34.10%     | ok               |
|          50 | -49.82%  | -53.71%            | -50.81% |    -1.26 |       54 | 16.28%     | ok               |
|          30 | -69.30%  | -53.71%            | -69.91% |    -1.32 |       77 | 37.74%     | ok               |

## ZEC-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 217.75%  | 3590.26%           | -30.64% |     1.11 |       46 | 33.33%     | ok               |
|          35 | 193.41%  | 3590.26%           | -50.84% |     1.04 |       52 | 39.08%     | ok               |
|          25 | 187.45%  | 3590.26%           | -58.07% |     1.01 |       55 | 45.21%     | ok               |
|          30 | 177.85%  | 3590.26%           | -56.50% |     0.99 |       61 | 42.53%     | ok               |
|          20 | 142.69%  | 3590.26%           | -62.70% |     0.9  |       63 | 46.93%     | ok               |
