# Market Tracker Backtest Report

_Generated: 2026-07-07T04:24:51+00:00_

## Data Sources

- Crypto: Kraken -> Coinbase -> CoinGecko OHLC -> CoinPaprika fallback chain.
- Stocks / ETFs / indices: Stooq -> Yahoo Finance fallback chain.
- Data rows are generated from real market APIs. Mock OHLCV rows are not generated.

## Data Freshness

- Rows: **92,470**
- Symbols: **161**
- Date range: **2024-02-09** to **2026-07-07**

## Latest Signals

| symbol     | date                |         close |   composite_score | signal   | data_source   |
|:-----------|:--------------------|--------------:|------------------:|:---------|:--------------|
| AAPL       | 2026-07-06 00:00:00 |   312.66      |        56.0833    | LONG     | Yahoo Finance |
| AAVE-USD   | 2026-07-07 00:00:00 |    91.61      |        43.3333    | LONG     | Kraken API    |
| ABBV       | 2026-07-06 00:00:00 |   254.76      |        61.4167    | LONG     | Yahoo Finance |
| AMAT       | 2026-07-06 00:00:00 |   592.79      |        31.5833    | LONG     | Yahoo Finance |
| AMZN       | 2026-07-06 00:00:00 |   244.16      |        53.1667    | LONG     | Yahoo Finance |
| BAC        | 2026-07-06 00:00:00 |    59.9       |        57.25      | LONG     | Yahoo Finance |
| C          | 2026-07-06 00:00:00 |   143.86      |        54.5833    | LONG     | Yahoo Finance |
| CAT        | 2026-07-06 00:00:00 |   969.92      |        33.9167    | LONG     | Yahoo Finance |
| CL         | 2026-07-06 00:00:00 |    93.39      |        74.4167    | LONG     | Yahoo Finance |
| DE         | 2026-07-06 00:00:00 |   635.24      |        74.0833    | LONG     | Yahoo Finance |
| DXY-INDEX  | 2026-07-07 00:00:00 |   100.872     |        69.6237    | LONG     | Yahoo Finance |
| GE         | 2026-07-06 00:00:00 |   378.68      |        61.75      | LONG     | Yahoo Finance |
| HD         | 2026-07-06 00:00:00 |   350.65      |        61.3333    | LONG     | Yahoo Finance |
| IBM        | 2026-07-06 00:00:00 |   299.52      |        65.5833    | LONG     | Yahoo Finance |
| ITA        | 2026-07-06 00:00:00 |   250.78      |        64.25      | LONG     | Yahoo Finance |
| JNJ        | 2026-07-06 00:00:00 |   259.33      |        74.9167    | LONG     | Yahoo Finance |
| JPM        | 2026-07-06 00:00:00 |   337.72      |        61.75      | LONG     | Yahoo Finance |
| LIN        | 2026-07-06 00:00:00 |   540.52      |        74.9167    | LONG     | Yahoo Finance |
| MS         | 2026-07-06 00:00:00 |   222.1       |        56.25      | LONG     | Yahoo Finance |
| NOW        | 2026-07-06 00:00:00 |   107.93      |        33.1667    | LONG     | Yahoo Finance |
| RTX        | 2026-07-06 00:00:00 |   201.37      |        62.25      | LONG     | Yahoo Finance |
| SCHW       | 2026-07-06 00:00:00 |   100.62      |        60.5833    | LONG     | Yahoo Finance |
| SPY        | 2026-07-06 00:00:00 |   751.28      |        51.4167    | LONG     | Yahoo Finance |
| TMO        | 2026-07-06 00:00:00 |   517.6       |        63.5       | LONG     | Yahoo Finance |
| TSLA       | 2026-07-06 00:00:00 |   419.77      |        47.75      | LONG     | Yahoo Finance |
| UNH        | 2026-07-06 00:00:00 |   417.99      |        42.5833    | LONG     | Yahoo Finance |
| UNI-USD    | 2026-07-07 00:00:00 |     3.1344    |        50.75      | LONG     | Kraken API    |
| VTI        | 2026-07-06 00:00:00 |   371.67      |        50.9167    | LONG     | Yahoo Finance |
| WFC        | 2026-07-06 00:00:00 |    87.45      |        55.3333    | LONG     | Yahoo Finance |
| XBI        | 2026-07-06 00:00:00 |   160.81      |        73.25      | LONG     | Yahoo Finance |
| XLF        | 2026-07-06 00:00:00 |    56.14      |        64.25      | LONG     | Yahoo Finance |
| XLI        | 2026-07-06 00:00:00 |   185.56      |        78.9167    | LONG     | Yahoo Finance |
| XLU        | 2026-07-06 00:00:00 |    45.3       |        67.1667    | LONG     | Yahoo Finance |
| YFI-USD    | 2026-07-07 00:00:00 |  2429.8       |        50.25      | LONG     | Kraken API    |
| ADA-USD    | 2026-07-07 00:00:00 |     0.180806  |        14.6667    | NEUTRAL  | Kraken API    |
| ADBE       | 2026-07-06 00:00:00 |   218.07      |         0.416667  | NEUTRAL  | Yahoo Finance |
| AGG        | 2026-07-06 00:00:00 |    98.66      |       -40.5833    | NEUTRAL  | Yahoo Finance |
| ALGO-USD   | 2026-07-07 00:00:00 |     0.08615   |       -35.75      | NEUTRAL  | Kraken API    |
| AMD        | 2026-07-06 00:00:00 |   552.05      |        43         | NEUTRAL  | Yahoo Finance |
| AMGN       | 2026-07-06 00:00:00 |   366.44      |        59.8333    | NEUTRAL  | Yahoo Finance |
| APT-USD    | 2026-07-07 00:00:00 |     0.6206    |       -31.75      | NEUTRAL  | Kraken API    |
| ARB-USD    | 2026-07-07 00:00:00 |     0.0781    |       -22.75      | NEUTRAL  | Kraken API    |
| ARKK       | 2026-07-06 00:00:00 |    83.61      |        42         | NEUTRAL  | Yahoo Finance |
| ATOM-USD   | 2026-07-07 00:00:00 |     1.5964    |       -23.3333    | NEUTRAL  | Kraken API    |
| AVAX-USD   | 2026-07-07 00:00:00 |     6.787     |        15         | NEUTRAL  | Kraken API    |
| AVGO       | 2026-07-06 00:00:00 |   373.9       |       -13.3333    | NEUTRAL  | Yahoo Finance |
| BA         | 2026-07-06 00:00:00 |   234.54      |        45.3333    | NEUTRAL  | Yahoo Finance |
| BCH-USD    | 2026-07-07 00:00:00 |   238.39      |         2.33333   | NEUTRAL  | Kraken API    |
| BITO       | 2026-07-06 00:00:00 |     8.64      |        -9.25      | NEUTRAL  | Yahoo Finance |
| BLK        | 2026-07-06 00:00:00 |  1011.21      |       -44.5       | NEUTRAL  | Yahoo Finance |
| BND        | 2026-07-06 00:00:00 |    73.14      |       -40.5833    | NEUTRAL  | Yahoo Finance |
| BONK-USD   | 2026-07-07 00:00:00 |     4.444e-06 |       -23.5833    | NEUTRAL  | Kraken API    |
| BTC-USD    | 2026-07-07 00:00:00 | 63134.2       |         7.83333   | NEUTRAL  | Kraken API    |
| CMCSA      | 2026-07-06 00:00:00 |    23.38      |        -9.41667   | NEUTRAL  | Yahoo Finance |
| COMP-USD   | 2026-07-07 00:00:00 |    17.19      |         6.91667   | NEUTRAL  | Kraken API    |
| COST       | 2026-07-06 00:00:00 |   950.25      |       -44.75      | NEUTRAL  | Yahoo Finance |
| CRM        | 2026-07-06 00:00:00 |   165.65      |        -2.25      | NEUTRAL  | Yahoo Finance |
| CRV-USD    | 2026-07-07 00:00:00 |     0.20632   |         0.166667  | NEUTRAL  | Kraken API    |
| CSCO       | 2026-07-06 00:00:00 |   113.98      |        11.0833    | NEUTRAL  | Yahoo Finance |
| DASH-USD   | 2026-07-07 00:00:00 |    34.693     |       -42.25      | NEUTRAL  | Kraken API    |
| DBC        | 2026-07-06 00:00:00 |    27         |        -5.66667   | NEUTRAL  | Yahoo Finance |
| DIA        | 2026-07-06 00:00:00 |   530.09      |        53         | NEUTRAL  | Yahoo Finance |
| DIS        | 2026-07-06 00:00:00 |    97.41      |       -64         | NEUTRAL  | Yahoo Finance |
| DOGE-USD   | 2026-07-07 00:00:00 |     0.0749776 |       -17         | NEUTRAL  | Kraken API    |
| DOT-USD    | 2026-07-07 00:00:00 |     0.8595    |       -14.8333    | NEUTRAL  | Kraken API    |
| EEM        | 2026-07-06 00:00:00 |    67.57      |        30.8333    | NEUTRAL  | Yahoo Finance |
| EFA        | 2026-07-06 00:00:00 |   105.46      |        44.3333    | NEUTRAL  | Yahoo Finance |
| EOG        | 2026-07-06 00:00:00 |   129.39      |       -12.3333    | NEUTRAL  | Yahoo Finance |
| ETC-USD    | 2026-07-07 00:00:00 |     7.033     |       -33.25      | NEUTRAL  | Kraken API    |
| ETH-USD    | 2026-07-07 00:00:00 |  1771.15      |         0.0833333 | NEUTRAL  | Kraken API    |
| EWJ        | 2026-07-06 00:00:00 |    95.27      |        54.8333    | NEUTRAL  | Yahoo Finance |
| FCX        | 2026-07-06 00:00:00 |    61         |       -20.8333    | NEUTRAL  | Yahoo Finance |
| FET-USD    | 2026-07-07 00:00:00 |     0.167     |       -19         | NEUTRAL  | Kraken API    |
| FIL-USD    | 2026-07-07 00:00:00 |     0.777     |        -0.833333  | NEUTRAL  | Kraken API    |
| GDX        | 2026-07-06 00:00:00 |    78.74      |       -36.6667    | NEUTRAL  | Yahoo Finance |
| GDXJ       | 2026-07-06 00:00:00 |   103.91      |       -15.1667    | NEUTRAL  | Yahoo Finance |
| GOOGL      | 2026-07-06 00:00:00 |   366.46      |        31.1667    | NEUTRAL  | Yahoo Finance |
| GRT-USD    | 2026-07-07 00:00:00 |     0.0181    |       -35.25      | NEUTRAL  | Kraken API    |
| GS         | 2026-07-06 00:00:00 |  1055.29      |        33.1667    | NEUTRAL  | Yahoo Finance |
| HBAR-USD   | 2026-07-07 00:00:00 |     0.0723    |       -22         | NEUTRAL  | Kraken API    |
| HON        | 2026-07-06 00:00:00 |   231.18      |         6.91667   | NEUTRAL  | Yahoo Finance |
| HYG        | 2026-07-06 00:00:00 |    79.87      |       -31.0833    | NEUTRAL  | Yahoo Finance |
| IBIT       | 2026-07-06 00:00:00 |    36.12      |        -2.58333   | NEUTRAL  | Yahoo Finance |
| ICP-USD    | 2026-07-07 00:00:00 |     2.176     |       -30.25      | NEUTRAL  | Kraken API    |
| IEF        | 2026-07-06 00:00:00 |    94.18      |       -31.1667    | NEUTRAL  | Yahoo Finance |
| IEMG       | 2026-07-06 00:00:00 |    82         |        30.8333    | NEUTRAL  | Yahoo Finance |
| INJ-USD    | 2026-07-07 00:00:00 |     4.759     |        -8.83333   | NEUTRAL  | Kraken API    |
| INTC       | 2026-07-06 00:00:00 |   122.2       |        -2.83333   | NEUTRAL  | Yahoo Finance |
| INTU       | 2026-07-06 00:00:00 |   272.14      |       -25.75      | NEUTRAL  | Yahoo Finance |
| IWM        | 2026-07-06 00:00:00 |   298.9       |        42.3333    | NEUTRAL  | Yahoo Finance |
| KO         | 2026-07-06 00:00:00 |    82.96      |        60.3333    | NEUTRAL  | Yahoo Finance |
| LDO-USD    | 2026-07-07 00:00:00 |     0.279     |         7.41667   | NEUTRAL  | Kraken API    |
| LINK-USD   | 2026-07-07 00:00:00 |     7.87366   |         7.41667   | NEUTRAL  | Kraken API    |
| LLY        | 2026-07-06 00:00:00 |  1200.06      |        42.8333    | NEUTRAL  | Yahoo Finance |
| LRCX       | 2026-07-06 00:00:00 |   350.2       |         8.41667   | NEUTRAL  | Yahoo Finance |
| LTC-USD    | 2026-07-07 00:00:00 |    44.05      |        16.4167    | NEUTRAL  | Kraken API    |
| MCD        | 2026-07-06 00:00:00 |   279.5       |       -26         | NEUTRAL  | Yahoo Finance |
| META       | 2026-07-06 00:00:00 |   600.29      |        14.9167    | NEUTRAL  | Yahoo Finance |
| MPC        | 2026-07-06 00:00:00 |   268.99      |        59.5       | NEUTRAL  | Yahoo Finance |
| MRK        | 2026-07-06 00:00:00 |   126.78      |        63.1667    | NEUTRAL  | Yahoo Finance |
| MSFT       | 2026-07-06 00:00:00 |   386.74      |       -11.75      | NEUTRAL  | Yahoo Finance |
| MU         | 2026-07-06 00:00:00 |   984.75      |         3.83333   | NEUTRAL  | Yahoo Finance |
| NEAR-USD   | 2026-07-07 00:00:00 |     2.0197    |        52.1667    | NEUTRAL  | Kraken API    |
| NEM        | 2026-07-06 00:00:00 |    98.2       |       -36.1667    | NEUTRAL  | Yahoo Finance |
| NKE        | 2026-07-06 00:00:00 |    43.34      |       -28.5       | NEUTRAL  | Yahoo Finance |
| OP-USD     | 2026-07-07 00:00:00 |     0.1054    |        12.75      | NEUTRAL  | Kraken API    |
| PEP        | 2026-07-06 00:00:00 |   143.29      |       -23         | NEUTRAL  | Yahoo Finance |
| PEPE-USD   | 2026-07-07 00:00:00 |     2.675e-06 |         0.5       | NEUTRAL  | Kraken API    |
| PG         | 2026-07-06 00:00:00 |   149.31      |        14.6667    | NEUTRAL  | Yahoo Finance |
| PM         | 2026-07-06 00:00:00 |   184.76      |        54.1667    | NEUTRAL  | Yahoo Finance |
| POL-USD    | 2026-07-07 00:00:00 |     0.07418   |       -29.75      | NEUTRAL  | Kraken API    |
| QCOM       | 2026-07-06 00:00:00 |   186.48      |       -28.5833    | NEUTRAL  | Yahoo Finance |
| QQQ        | 2026-07-06 00:00:00 |   722.82      |        37         | NEUTRAL  | Yahoo Finance |
| RENDER-USD | 2026-07-07 00:00:00 |     1.596     |       -12.3333    | NEUTRAL  | Kraken API    |
| SBUX       | 2026-07-06 00:00:00 |   102.11      |        39.5       | NEUTRAL  | Yahoo Finance |
| SHIB-USD   | 2026-07-07 00:00:00 |     4.33e-06  |       -20.3333    | NEUTRAL  | Kraken API    |
| SHY        | 2026-07-06 00:00:00 |    81.98      |       -31.75      | NEUTRAL  | Yahoo Finance |
| SKY-USD    | 2026-07-07 00:00:00 |     0.05504   |       -35.0833    | NEUTRAL  | Kraken API    |
| SMH        | 2026-07-06 00:00:00 |   604.3       |        -3.83333   | NEUTRAL  | Yahoo Finance |
| SNX-USD    | 2026-07-07 00:00:00 |     0.2216    |       -30.4167    | NEUTRAL  | Kraken API    |
| SOL-USD    | 2026-07-07 00:00:00 |    80.95      |        33.75      | NEUTRAL  | Kraken API    |
| SOXX       | 2026-07-06 00:00:00 |   581.51      |        -3.83333   | NEUTRAL  | Yahoo Finance |
| SUSHI-USD  | 2026-07-07 00:00:00 |     0.1624    |       -24.5833    | NEUTRAL  | Kraken API    |
| TGT        | 2026-07-06 00:00:00 |   126.1       |       -11.0833    | NEUTRAL  | Yahoo Finance |
| TIA-USD    | 2026-07-07 00:00:00 |     0.3761    |       -19.8333    | NEUTRAL  | Kraken API    |
| TLT        | 2026-07-06 00:00:00 |    85.45      |       -44.8333    | NEUTRAL  | Yahoo Finance |
| TRX-USD    | 2026-07-07 00:00:00 |     0.329708  |        47.6667    | NEUTRAL  | Kraken API    |
| TXN        | 2026-07-06 00:00:00 |   303.5       |        38.8333    | NEUTRAL  | Yahoo Finance |
| UPS        | 2026-07-06 00:00:00 |   110.02      |        48.3333    | NEUTRAL  | Yahoo Finance |
| USO        | 2026-07-06 00:00:00 |   104.35      |       -16.9167    | NEUTRAL  | Yahoo Finance |
| VEA        | 2026-07-06 00:00:00 |    71.89      |        39.5       | NEUTRAL  | Yahoo Finance |
| VIXY       | 2026-07-06 00:00:00 |    20.65      |       -54.3333    | NEUTRAL  | Yahoo Finance |
| VNQ        | 2026-07-06 00:00:00 |    97.24      |        17.6667    | NEUTRAL  | Yahoo Finance |
| VWO        | 2026-07-06 00:00:00 |    60.07      |        21.5       | NEUTRAL  | Yahoo Finance |
| WIF-USD    | 2026-07-07 00:00:00 |     0.168     |        -2.58333   | NEUTRAL  | Kraken API    |
| XLB        | 2026-07-06 00:00:00 |    51.98      |        47.5       | NEUTRAL  | Yahoo Finance |
| XLC        | 2026-07-06 00:00:00 |   110.21      |        -7.75      | NEUTRAL  | Yahoo Finance |
| XLE        | 2026-07-06 00:00:00 |    53.13      |       -14.8333    | NEUTRAL  | Yahoo Finance |
| XLK        | 2026-07-06 00:00:00 |   183.57      |        -0.166667  | NEUTRAL  | Yahoo Finance |
| XLM-USD    | 2026-07-07 00:00:00 |     0.195815  |        -5.75      | NEUTRAL  | Kraken API    |
| XLP        | 2026-07-06 00:00:00 |    84.1       |        21.4167    | NEUTRAL  | Yahoo Finance |
| XLV        | 2026-07-06 00:00:00 |   161.96      |        52.1667    | NEUTRAL  | Yahoo Finance |
| XLY        | 2026-07-06 00:00:00 |   118.01      |        38.5       | NEUTRAL  | Yahoo Finance |
| XRP-USD    | 2026-07-07 00:00:00 |     1.12764   |         7.41667   | NEUTRAL  | Kraken API    |
| ZEC-USD    | 2026-07-07 00:00:00 |   447.94      |        34.1667    | NEUTRAL  | Kraken API    |
| COP        | 2026-07-06 00:00:00 |   103.58      |       -48.0833    | SHORT    | Yahoo Finance |
| CVX        | 2026-07-06 00:00:00 |   168.1       |       -45.9167    | SHORT    | Yahoo Finance |
| FXI        | 2026-07-06 00:00:00 |    32.49      |       -54.9167    | SHORT    | Yahoo Finance |
| GLD        | 2026-07-06 00:00:00 |   382.13      |       -32.5       | SHORT    | Yahoo Finance |
| NFLX       | 2026-07-06 00:00:00 |    76.02      |       -33.25      | SHORT    | Yahoo Finance |
| NVDA       | 2026-07-06 00:00:00 |   195.55      |       -29.8333    | SHORT    | Yahoo Finance |
| ORCL       | 2026-07-06 00:00:00 |   143.76      |       -61.4167    | SHORT    | Yahoo Finance |
| OXY        | 2026-07-06 00:00:00 |    48.81      |       -45.5833    | SHORT    | Yahoo Finance |
| PFE        | 2026-07-06 00:00:00 |    23.72      |       -48.0833    | SHORT    | Yahoo Finance |
| SLB        | 2026-07-06 00:00:00 |    45.72      |       -43.3333    | SHORT    | Yahoo Finance |
| SLV        | 2026-07-06 00:00:00 |    56.11      |       -34.4167    | SHORT    | Yahoo Finance |
| T          | 2026-07-06 00:00:00 |    20.58      |       -60.8333    | SHORT    | Yahoo Finance |
| TMUS       | 2026-07-06 00:00:00 |   181.79      |       -36.5833    | SHORT    | Yahoo Finance |
| VZ         | 2026-07-06 00:00:00 |    42.07      |       -49.3333    | SHORT    | Yahoo Finance |
| WMT        | 2026-07-06 00:00:00 |   110.65      |       -61.0833    | SHORT    | Yahoo Finance |
| XOM        | 2026-07-06 00:00:00 |   136.44      |       -42.1667    | SHORT    | Yahoo Finance |

## Edge Summary

- Symbols with trades: **160** of 160
- Beat buy-and-hold: **33.75%** of traded symbols
- Positive return: **35.62%** of traded symbols
- Median strategy return: **-9.43%** (benchmark **15.14%**)
- Median excess vs benchmark: **-25.39%**
- Median Sharpe: **-0.10**
- Median exposure: **44.43%**

> Edge is real only if both _beat buy-and-hold_ and _median excess_ are convincingly positive across many symbols. Treat a single high-return symbol as noise.

## Portfolio Backtest

Actual capital-allocation books (not per-symbol averages). Benchmarks: `equal_weight_buyhold` (whole tracked universe), `spy_buyhold` (100% SPY), and `sixty_forty` (60% SPY / 40% AGG). `high_conf_voltarget` inverse-vol-weights the HIGH-confidence book; `conviction_long_short` is market-neutral. Judge on **Sharpe** and **max_drawdown** out-of-sample, not raw return: a fully-invested long book wins on return in a bull market but carries all the risk.

| strategy              | scope         | ann_return   | ann_vol   |   sharpe | max_drawdown   | total_return   |   avg_gross_exposure |
|:----------------------|:--------------|:-------------|:----------|---------:|:---------------|:---------------|---------------------:|
| equal_weight_buyhold  | full          | -6.47%       | 33.26%    |    -0.19 | -51.66%        | -30.78%        |                 1    |
| equal_weight_buyhold  | out_of_sample | -15.55%      | 31.63%    |    -0.49 | -39.63%        | -19.72%        |                 1    |
| all_signals_ew        | full          | -12.38%      | 28.24%    |    -0.44 | -60.22%        | -39.36%        |                 1    |
| all_signals_ew        | out_of_sample | 17.41%       | 27.10%    |     0.64 | -15.78%        | 15.85%         |                 1    |
| high_conf_ew          | full          | 7.31%        | 31.62%    |     0.23 | -41.17%        | 7.59%          |                 0.88 |
| high_conf_ew          | out_of_sample | 21.90%       | 33.68%    |     0.65 | -17.35%        | 19.13%         |                 0.88 |
| high_conf_voltarget   | full          | 9.20%        | 29.12%    |     0.32 | -35.18%        | 16.67%         |                 0.88 |
| high_conf_voltarget   | out_of_sample | 18.16%       | 31.24%    |     0.58 | -16.94%        | 15.44%         |                 0.88 |
| conviction_long_short | full          | -14.40%      | 23.44%    |    -0.61 | -42.05%        | -40.77%        |                 0.97 |
| conviction_long_short | out_of_sample | -10.83%      | 26.38%    |    -0.41 | -21.34%        | -14.19%        |                 0.97 |
| spy_buyhold           | full          | 6.40%        | 13.37%    |     0.48 | -17.81%        | 18.28%         |                 0.78 |
| spy_buyhold           | out_of_sample | -2.24%       | 9.75%     |    -0.23 | -13.27%        | -2.86%         |                 0.78 |
| sixty_forty           | full          | 3.82%        | 8.47%     |     0.45 | -10.80%        | 11.12%         |                 0.78 |
| sixty_forty           | out_of_sample | -2.54%       | 6.41%     |    -0.4  | -9.26%         | -2.89%         |                 0.78 |

## Walk-Forward Robustness

Each book measured across contiguous time folds (each a different regime). A book has durable edge only if `mean_sharpe` is positive, `min_sharpe` isn't deeply negative, and `pct_positive_folds` is high — a single great fold doesn't count. `fold_sharpes` lists each fold oldest-to-newest.

| strategy              |   n_folds |   mean_sharpe |   median_sharpe |   min_sharpe | pct_positive_folds   | mean_return   | fold_sharpes                  |
|:----------------------|----------:|--------------:|----------------:|-------------:|:---------------------|:--------------|:------------------------------|
| equal_weight_buyhold  |         5 |          0.11 |            0.33 |        -1.49 | 60.00%               | -4.97%        | 1.71;-1.49;0.76;-0.78;0.33    |
| all_signals_ew        |         5 |         -0.38 |           -0.22 |        -1.31 | 0.00%                | -9.00%        | -0.01;-0.05;-1.31;-0.31;-0.22 |
| high_conf_ew          |         5 |          0.4  |            0.5  |        -0.98 | 80.00%               | 2.70%         | 1.02;1.28;-0.98;0.50;0.18     |
| high_conf_voltarget   |         5 |          0.59 |            0.51 |        -1.05 | 80.00%               | 4.45%         | 1.85;1.58;-1.05;0.51;0.09     |
| conviction_long_short |         5 |         -0.69 |           -0.5  |        -1.44 | 20.00%               | -9.79%        | -1.44;-0.41;-0.50;0.02;-1.13  |
| spy_buyhold           |         5 |          0.35 |           -0.07 |        -0.57 | 40.00%               | 3.69%         | 1.69;-0.40;1.08;-0.57;-0.07   |
| sixty_forty           |         5 |          0.3  |           -0.28 |        -0.58 | 40.00%               | 2.27%         | 1.86;-0.55;1.07;-0.58;-0.28   |

## Strategy Comparison

Each decision rule backtested over the same data. `out_of_sample` is the most recent ~35% of each symbol's history (unseen tail). A rule has real edge only if `median_excess` and `beat_benchmark_pct` stay positive out-of-sample, not just full-sample.

| strategy        | scope         |   symbols | beat_benchmark_pct   | positive_pct   | median_return   | median_benchmark   | median_excess   |   median_sharpe |   total_trades |
|:----------------|:--------------|----------:|:---------------------|:---------------|:----------------|:-------------------|:----------------|----------------:|---------------:|
| trend           | full          |       160 | 33.75%               | 35.62%         | -9.43%          | 15.14%             | -25.39%         |           -0.1  |          11233 |
| trend           | out_of_sample |       160 | 41.88%               | 51.88%         | 1.06%           | 5.89%              | -6.10%          |            0.24 |           3891 |
| mean_reversion  | full          |       157 | 41.40%               | 50.32%         | 0.01%           | 15.03%             | -17.12%         |            0.01 |           1266 |
| mean_reversion  | out_of_sample |       128 | 49.22%               | 62.50%         | 0.48%           | -0.31%             | -2.14%          |            0.78 |            472 |
| regime_adaptive | full          |       160 | 34.38%               | 36.25%         | -10.59%         | 15.14%             | -26.19%         |           -0.1  |          11506 |
| regime_adaptive | out_of_sample |       160 | 41.88%               | 52.50%         | 1.05%           | 5.89%              | -6.28%          |            0.21 |           3991 |

## Signal Calibration

Realized forward return in the signal's direction, grouped by confidence. HIGH should outrank LOW for the confidence score to be meaningful.

| confidence_level   |   horizon |     n | mean_return   | median_return   | win_rate   |
|:-------------------|----------:|------:|:--------------|:----------------|:-----------|
| HIGH               |         5 |  7982 | 0.17%         | 0.13%           | 52.17%     |
| MEDIUM             |         5 | 29253 | 0.04%         | 0.09%           | 50.98%     |
| LOW                |         5 |  3294 | -0.61%        | -0.53%          | 44.72%     |
| ALL                |         5 | 40529 | 0.01%         | 0.05%           | 50.70%     |
| HIGH               |        10 |  7939 | 0.47%         | 0.16%           | 51.91%     |
| MEDIUM             |        10 | 29033 | 0.20%         | 0.15%           | 51.25%     |
| LOW                |        10 |  3266 | -0.90%        | -0.72%          | 45.35%     |
| ALL                |        10 | 40238 | 0.17%         | 0.11%           | 50.90%     |
| HIGH               |        20 |  7858 | 0.83%         | 0.39%           | 53.12%     |
| MEDIUM             |        20 | 28686 | 0.87%         | 0.64%           | 53.68%     |
| LOW                |        20 |  3244 | -0.62%        | -0.48%          | 47.35%     |
| ALL                |        20 | 39788 | 0.74%         | 0.51%           | 53.05%     |

## Backtest Summary

### Data Quality / Signal Availability

- **ok**: 160 symbols

| symbol     |   trades | return   | benchmark_return   | mdd     |   sharpe | exposure   | skipped_reason   |
|:-----------|---------:|:---------|:-------------------|:--------|---------:|:-----------|:-----------------|
| AAPL       |       65 | 14.19%   | 65.56%             | -20.65% |     0.38 | 48.42%     | ok               |
| AAVE-USD   |       74 | -50.46%  | -69.07%            | -68.26% |    -0.46 | 37.74%     | ok               |
| ABBV       |       66 | -17.71%  | 46.35%             | -30.55% |    -0.36 | 47.25%     | ok               |
| ADA-USD    |       88 | -83.94%  | -79.79%            | -89.69% |    -0.71 | 46.74%     | ok               |
| ADBE       |       66 | -31.08%  | -65.23%            | -34.86% |    -0.39 | 57.24%     | ok               |
| AGG        |       69 | -6.61%   | 1.06%              | -10.16% |    -1.1  | 31.11%     | ok               |
| ALGO-USD   |       86 | -50.43%  | -75.24%            | -53.13% |    -0.57 | 38.12%     | ok               |
| AMAT       |       69 | -26.30%  | 218.98%            | -57.21% |    -0.17 | 53.41%     | ok               |
| AMD        |       56 | 4.02%    | 220.07%            | -44.58% |     0.25 | 36.27%     | ok               |
| AMGN       |       69 | -15.41%  | 25.87%             | -34.14% |    -0.29 | 46.26%     | ok               |
| AMZN       |       80 | -38.32%  | 39.96%             | -42.48% |    -1.16 | 38.27%     | ok               |
| APT-USD    |       76 | -34.86%  | -91.20%            | -69.96% |    -0.12 | 42.91%     | ok               |
| ARB-USD    |       68 | -12.63%  | -86.52%            | -62.67% |     0.11 | 38.12%     | ok               |
| ARKK       |       83 | -34.44%  | 68.60%             | -36.89% |    -0.6  | 39.93%     | ok               |
| ATOM-USD   |       90 | -68.04%  | -72.61%            | -74.00% |    -1.12 | 46.17%     | ok               |
| AVAX-USD   |       70 | -17.84%  | -78.86%            | -55.62% |    -0.01 | 39.08%     | ok               |
| AVGO       |       62 | 21.52%   | 191.33%            | -35.76% |     0.4  | 43.76%     | ok               |
| BA         |       67 | 7.60%    | 12.11%             | -30.56% |     0.25 | 49.25%     | ok               |
| BAC        |       78 | -9.46%   | 81.13%             | -27.64% |    -0.18 | 48.59%     | ok               |
| BCH-USD    |       76 | 3.75%    | -40.98%            | -53.87% |     0.25 | 48.85%     | ok               |
| BITO       |       78 | 5.28%    | -61.67%            | -42.82% |     0.24 | 42.26%     | ok               |
| BLK        |       73 | -9.17%   | 26.84%             | -24.29% |    -0.21 | 42.60%     | ok               |
| BND        |       65 | -7.32%   | 1.06%              | -9.89%  |    -1.18 | 32.28%     | ok               |
| BONK-USD   |       70 | 70.45%   | -79.80%            | -45.22% |     0.72 | 41.95%     | ok               |
| BTC-USD    |       74 | -2.02%   | -37.26%            | -23.38% |     0.12 | 52.68%     | ok               |
| C          |       81 | -22.93%  | 166.46%            | -37.02% |    -0.41 | 51.58%     | ok               |
| CAT        |       72 | 28.37%   | 205.81%            | -21.02% |     0.53 | 57.07%     | ok               |
| CL         |       60 | 14.15%   | 11.90%             | -14.32% |     0.51 | 46.26%     | ok               |
| CMCSA      |       82 | -38.18%  | -40.70%            | -38.49% |    -0.99 | 43.59%     | ok               |
| COMP-USD   |       91 | -42.58%  | -73.20%            | -59.19% |    -0.3  | 46.36%     | ok               |
| COP        |       71 | -18.54%  | -6.82%             | -43.96% |    -0.31 | 40.93%     | ok               |
| COST       |       60 | 0.29%    | 31.36%             | -29.73% |     0.08 | 44.93%     | ok               |
| CRM        |       67 | -42.74%  | -43.13%            | -42.49% |    -0.92 | 43.59%     | ok               |
| CRV-USD    |       66 | -10.58%  | -70.06%            | -39.89% |     0.12 | 36.02%     | ok               |
| CSCO       |       59 | 28.10%   | 127.37%            | -21.79% |     0.58 | 49.92%     | ok               |
| CVX        |       75 | -11.36%  | 11.30%             | -27.27% |    -0.26 | 41.43%     | ok               |
| DASH-USD   |       63 | -37.83%  | 13.75%             | -64.43% |     0.03 | 31.61%     | ok               |
| DBC        |       58 | -12.98%  | 21.29%             | -25.70% |    -0.45 | 32.78%     | ok               |
| DE         |       72 | -0.97%   | 66.60%             | -25.24% |     0.08 | 46.92%     | ok               |
| DIA        |       60 | -2.50%   | 37.07%             | -12.94% |    -0.1  | 45.09%     | ok               |
| DIS        |       66 | -16.30%  | -10.13%            | -28.17% |    -0.27 | 47.25%     | ok               |
| DOGE-USD   |       77 | -21.59%  | -75.64%            | -60.95% |     0.03 | 50.77%     | ok               |
| DOT-USD    |       88 | -46.31%  | -85.46%            | -61.81% |    -0.34 | 48.85%     | ok               |
| DXY-INDEX  |       40 | -2.28%   | -0.30%             | -6.28%  |    -0.35 | 30.00%     | ok               |
| EEM        |       64 | -9.40%   | 70.72%             | -25.67% |    -0.25 | 43.43%     | ok               |
| EFA        |       60 | -8.17%   | 40.05%             | -13.72% |    -0.29 | 44.09%     | ok               |
| EOG        |       77 | -24.73%  | 16.52%             | -48.13% |    -0.54 | 46.09%     | ok               |
| ETC-USD    |       64 | -35.69%  | -71.93%            | -48.16% |    -0.51 | 31.23%     | ok               |
| ETH-USD    |       62 | 144.24%  | -43.17%            | -30.11% |     1.21 | 45.21%     | ok               |
| EWJ        |       62 | -18.16%  | 42.98%             | -30.73% |    -0.59 | 39.10%     | ok               |
| FCX        |       63 | -28.65%  | 63.28%             | -48.09% |    -0.33 | 45.09%     | ok               |
| FET-USD    |       77 | -34.65%  | -82.12%            | -48.39% |    -0.08 | 39.66%     | ok               |
| FIL-USD    |       72 | -36.50%  | -82.23%            | -50.88% |    -0.35 | 32.95%     | ok               |
| FXI        |       44 | -4.00%   | 45.30%             | -23.91% |    -0.01 | 29.78%     | ok               |
| GDX        |       60 | 11.28%   | 191.95%            | -34.99% |     0.3  | 48.09%     | ok               |
| GDXJ       |       68 | -23.13%  | 216.80%            | -44.93% |    -0.22 | 46.42%     | ok               |
| GE         |       74 | 27.07%   | 240.67%            | -27.82% |     0.53 | 53.91%     | ok               |
| GLD        |       48 | 23.90%   | 103.69%            | -16.63% |     0.62 | 46.42%     | ok               |
| GOOGL      |       63 | 72.01%   | 145.95%            | -20.41% |     1.1  | 53.24%     | ok               |
| GRT-USD    |       87 | -20.09%  | -89.11%            | -57.16% |    -0.03 | 41.76%     | ok               |
| GS         |       76 | -2.38%   | 174.63%            | -22.13% |     0.05 | 52.08%     | ok               |
| HD         |       71 | -3.53%   | -3.44%             | -17.69% |    -0.01 | 44.26%     | ok               |
| HON        |       93 | -26.82%  | 20.04%             | -29.80% |    -0.72 | 52.41%     | ok               |
| HYG        |       81 | -9.52%   | 3.24%              | -9.59%  |    -1.11 | 34.28%     | ok               |
| IBIT       |       32 | 33.13%   | -4.97%             | -18.95% |     0.7  | 32.46%     | ok               |
| IBM        |       78 | 6.48%    | 60.74%             | -27.54% |     0.23 | 49.75%     | ok               |
| ICP-USD    |       81 | 3.64%    | -74.42%            | -51.29% |     0.29 | 35.82%     | ok               |
| IEF        |       76 | -10.90%  | -0.33%             | -11.70% |    -1.54 | 32.78%     | ok               |
| IEMG       |       58 | -5.52%   | 64.53%             | -26.84% |    -0.12 | 43.59%     | ok               |
| INJ-USD    |       73 | -53.62%  | -73.99%            | -77.42% |    -0.52 | 37.16%     | ok               |
| INTC       |       70 | 55.82%   | 182.15%            | -60.60% |     0.62 | 49.25%     | ok               |
| INTU       |       67 | -19.58%  | -58.65%            | -43.00% |    -0.23 | 42.26%     | ok               |
| ITA        |       72 | 1.88%    | 101.17%            | -23.75% |     0.13 | 47.92%     | ok               |
| IWM        |       48 | 9.40%    | 49.94%             | -12.83% |     0.39 | 35.77%     | ok               |
| JNJ        |       72 | 7.58%    | 65.43%             | -17.51% |     0.32 | 50.58%     | ok               |
| JPM        |       75 | -16.79%  | 92.97%             | -33.43% |    -0.38 | 54.08%     | ok               |
| KO         |       49 | 28.93%   | 39.29%             | -8.07%  |     1.03 | 37.77%     | ok               |
| LDO-USD    |       72 | 8.74%    | -86.32%            | -58.32% |     0.34 | 37.74%     | ok               |
| LIN        |       64 | 0.44%    | 28.87%             | -21.53% |     0.08 | 38.60%     | ok               |
| LINK-USD   |       72 | -18.18%  | -65.75%            | -50.48% |     0.04 | 41.76%     | ok               |
| LLY        |       71 | -25.61%  | 62.14%             | -53.34% |    -0.35 | 50.92%     | ok               |
| LRCX       |       80 | -24.92%  | 284.17%            | -63.56% |    -0.14 | 46.09%     | ok               |
| LTC-USD    |       66 | -34.00%  | -62.67%            | -53.76% |    -0.29 | 48.47%     | ok               |
| MCD        |       75 | -2.55%   | -3.44%             | -18.81% |    -0.05 | 38.10%     | ok               |
| META       |       72 | -28.36%  | 28.24%             | -38.96% |    -0.47 | 48.92%     | ok               |
| MPC        |       71 | -15.43%  | 58.26%             | -44.76% |    -0.17 | 49.42%     | ok               |
| MRK        |       67 | -29.70%  | 1.06%              | -34.46% |    -0.72 | 44.93%     | ok               |
| MS         |       81 | -13.27%  | 158.59%            | -27.79% |    -0.24 | 49.92%     | ok               |
| MSFT       |       83 | -40.57%  | -8.04%             | -39.79% |    -1.1  | 48.09%     | ok               |
| MU         |       51 | 270.20%  | 1050.95%           | -68.76% |     1.34 | 59.90%     | ok               |
| NEAR-USD   |       85 | 22.12%   | -52.58%            | -60.07% |     0.44 | 41.00%     | ok               |
| NEM        |       74 | -32.79%  | 199.48%            | -38.49% |    -0.36 | 53.24%     | ok               |
| NFLX       |       62 | 30.31%   | 35.43%             | -21.09% |     0.65 | 54.58%     | ok               |
| NKE        |       91 | -37.83%  | -58.53%            | -55.35% |    -0.53 | 43.76%     | ok               |
| NOW        |       80 | 4.84%    | -33.62%            | -28.41% |     0.22 | 45.59%     | ok               |
| NVDA       |       74 | -23.08%  | 129.10%            | -45.02% |    -0.14 | 58.29%     | ok               |
| OP-USD     |       70 | -13.99%  | -92.12%            | -70.11% |     0.1  | 34.10%     | ok               |
| ORCL       |       74 | 88.92%   | 23.25%             | -29.47% |     0.84 | 53.58%     | ok               |
| OXY        |       67 | 8.21%    | -15.07%            | -31.73% |     0.26 | 43.09%     | ok               |
| PEP        |       81 | -6.99%   | -14.54%            | -21.35% |    -0.14 | 48.75%     | ok               |
| PEPE-USD   |       79 | 0.11%    | -78.18%            | -57.66% |     0.28 | 44.83%     | ok               |
| PFE        |       77 | -38.27%  | -13.93%            | -40.87% |    -1.21 | 35.11%     | ok               |
| PG         |       66 | -15.60%  | -5.15%             | -22.27% |    -0.57 | 41.26%     | ok               |
| PM         |       85 | -4.86%   | 107.32%            | -33.68% |    -0.01 | 56.91%     | ok               |
| POL-USD    |       79 | 59.25%   | -80.20%            | -46.45% |     0.73 | 50.19%     | ok               |
| QCOM       |       75 | -13.66%  | 23.50%             | -56.59% |    -0.02 | 46.59%     | ok               |
| QQQ        |       64 | 15.62%   | 65.39%             | -12.88% |     0.47 | 44.93%     | ok               |
| RENDER-USD |       98 | -19.07%  | -61.63%            | -45.00% |     0.1  | 43.63%     | ok               |
| RTX        |       58 | 29.99%   | 122.48%            | -16.99% |     0.72 | 51.58%     | ok               |
| SBUX       |       64 | -21.25%  | 4.94%              | -27.45% |    -0.41 | 39.43%     | ok               |
| SCHW       |       78 | -17.38%  | 58.78%             | -31.92% |    -0.36 | 46.42%     | ok               |
| SHIB-USD   |       78 | -37.08%  | -75.43%            | -48.95% |    -0.29 | 52.87%     | ok               |
| SHY        |       48 | -2.24%   | 0.21%              | -2.85%  |    -0.79 | 34.28%     | ok               |
| SKY-USD    |       70 | -28.56%  | -4.82%             | -43.98% |    -0.34 | 40.67%     | ok               |
| SLB        |       75 | -22.01%  | -2.89%             | -54.23% |    -0.35 | 51.25%     | ok               |
| SLV        |       58 | 41.28%   | 171.32%            | -42.66% |     0.62 | 42.10%     | ok               |
| SMH        |       48 | 83.38%   | 196.44%            | -33.99% |     1.1  | 49.08%     | ok               |
| SNX-USD    |       60 | -1.63%   | -84.71%            | -34.76% |     0.23 | 37.36%     | ok               |
| SOL-USD    |       66 | -34.04%  | -61.98%            | -56.90% |    -0.11 | 58.62%     | ok               |
| SOXX       |       57 | 72.26%   | 177.16%            | -41.89% |     0.96 | 47.92%     | ok               |
| SPY        |       64 | 3.26%    | 49.90%             | -16.47% |     0.17 | 50.08%     | ok               |
| SUSHI-USD  |       94 | -78.10%  | -85.55%            | -82.41% |    -1.15 | 36.21%     | ok               |
| T          |       64 | 47.19%   | 22.21%             | -17.01% |     1.01 | 51.91%     | ok               |
| TGT        |       58 | -12.57%  | -13.94%            | -40.57% |    -0.18 | 38.94%     | ok               |
| TIA-USD    |       89 | -49.45%  | -90.43%            | -70.38% |    -0.38 | 36.40%     | ok               |
| TLT        |       70 | -21.65%  | -8.95%             | -21.82% |    -1.69 | 31.45%     | ok               |
| TMO        |       61 | 14.84%   | -6.02%             | -18.85% |     0.39 | 49.75%     | ok               |
| TMUS       |       70 | 10.03%   | 12.08%             | -24.50% |     0.3  | 48.25%     | ok               |
| TRX-USD    |       72 | 0.99%    | 34.96%             | -22.90% |     0.12 | 49.04%     | ok               |
| TSLA       |       69 | 12.31%   | 116.86%            | -42.22% |     0.32 | 41.26%     | ok               |
| TXN        |       75 | -13.92%  | 86.88%             | -47.39% |    -0.07 | 53.91%     | ok               |
| UNH        |       74 | 28.09%   | -19.34%            | -27.86% |     0.5  | 52.58%     | ok               |
| UNI-USD    |       90 | -76.71%  | -71.16%            | -80.61% |    -1    | 42.72%     | ok               |
| UPS        |       72 | -38.23%  | -24.78%            | -40.45% |    -0.78 | 40.27%     | ok               |
| USO        |       68 | 7.40%    | 45.60%             | -43.35% |     0.24 | 34.11%     | ok               |
| VEA        |       58 | -0.98%   | 50.90%             | -17.93% |     0.01 | 44.09%     | ok               |
| VIXY       |       94 | -79.98%  | -63.13%            | -88.16% |    -1    | 31.95%     | ok               |
| VNQ        |       75 | -16.77%  | 15.24%             | -24.92% |    -0.7  | 37.60%     | ok               |
| VTI        |       70 | -2.51%   | 49.33%             | -18.77% |    -0.03 | 50.92%     | ok               |
| VWO        |       76 | -13.41%  | 47.85%             | -25.20% |    -0.47 | 44.09%     | ok               |
| VZ         |       89 | -26.33%  | 5.92%              | -27.84% |    -0.88 | 36.94%     | ok               |
| WFC        |       86 | -15.11%  | 81.96%             | -29.91% |    -0.23 | 49.58%     | ok               |
| WIF-USD    |       68 | -35.28%  | -83.38%            | -50.54% |    -0.13 | 31.99%     | ok               |
| WMT        |       61 | 21.43%   | 96.10%             | -21.31% |     0.61 | 50.58%     | ok               |
| XBI        |       62 | 4.70%    | 76.64%             | -21.61% |     0.2  | 40.77%     | ok               |
| XLB        |       62 | -9.41%   | 25.04%             | -25.37% |    -0.3  | 36.61%     | ok               |
| XLC        |       67 | 12.45%   | 39.21%             | -12.33% |     0.45 | 55.24%     | ok               |
| XLE        |       73 | -10.91%  | 27.55%             | -37.51% |    -0.21 | 46.42%     | ok               |
| XLF        |       78 | -9.28%   | 43.65%             | -23.61% |    -0.29 | 48.09%     | ok               |
| XLI        |       64 | 4.62%    | 58.67%             | -10.77% |     0.23 | 44.59%     | ok               |
| XLK        |       42 | 59.88%   | 76.65%             | -14.75% |     1.14 | 46.59%     | ok               |
| XLM-USD    |       69 | 5.21%    | -50.11%            | -50.36% |     0.28 | 45.79%     | ok               |
| XLP        |       68 | 6.56%    | 15.03%             | -11.16% |     0.4  | 42.93%     | ok               |
| XLU        |       71 | -8.34%   | 50.32%             | -20.40% |    -0.34 | 38.44%     | ok               |
| XLV        |       66 | -12.12%  | 12.46%             | -16.83% |    -0.59 | 35.61%     | ok               |
| XLY        |       72 | 2.75%    | 31.20%             | -14.01% |     0.15 | 44.26%     | ok               |
| XOM        |       58 | 5.06%    | 34.07%             | -20.29% |     0.22 | 36.94%     | ok               |
| XRP-USD    |       58 | -30.47%  | -60.82%            | -44.89% |    -0.26 | 33.72%     | ok               |
| YFI-USD    |       83 | -55.71%  | -63.18%            | -67.78% |    -0.83 | 40.42%     | ok               |
| ZEC-USD    |       64 | 52.99%   | 1040.67%           | -47.68% |     0.6  | 34.87%     | ok               |

## AAPL Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 25.06%   | 65.56%             | -21.71% |     0.55 |       68 | 53.24%     | ok               |
|          15 | 21.21%   | 65.56%             | -23.86% |     0.48 |       75 | 60.40%     | ok               |
|          30 | 14.19%   | 65.56%             | -20.65% |     0.38 |       65 | 48.42%     | ok               |
|          25 | 13.58%   | 65.56%             | -20.03% |     0.36 |       67 | 50.92%     | ok               |
|          35 | 8.51%    | 65.56%             | -22.04% |     0.27 |       65 | 46.09%     | ok               |

## AAVE-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 14.69%   | -69.07%            | -43.61% |     0.37 |       38 | 31.03%     | ok               |
|          45 | 4.82%    | -69.07%            | -46.87% |     0.26 |       40 | 26.63%     | ok               |
|          35 | -5.67%   | -69.07%            | -51.96% |     0.16 |       50 | 33.72%     | ok               |
|          50 | -29.26%  | -69.07%            | -43.73% |    -0.28 |       42 | 19.54%     | ok               |
|          15 | -51.46%  | -69.07%            | -61.76% |    -0.32 |       80 | 51.92%     | ok               |

## ABBV Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -2.11%   | 46.35%             | -23.85% |     0.03 |       52 | 36.77%     | ok               |
|          40 | -14.30%  | 46.35%             | -26.61% |    -0.29 |       66 | 41.60%     | ok               |
|          35 | -15.52%  | 46.35%             | -27.83% |    -0.32 |       68 | 44.43%     | ok               |
|          30 | -17.71%  | 46.35%             | -30.55% |    -0.36 |       66 | 47.25%     | ok               |
|          45 | -16.97%  | 46.35%             | -29.59% |    -0.37 |       56 | 38.94%     | ok               |

## ADA-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -83.86%  | -79.79%            | -91.83% |    -0.58 |       82 | 64.18%     | ok               |
|          50 | -77.92%  | -79.79%            | -85.97% |    -0.59 |       55 | 26.82%     | ok               |
|          45 | -80.28%  | -79.79%            | -88.02% |    -0.62 |       58 | 31.61%     | ok               |
|          20 | -84.86%  | -79.79%            | -92.33% |    -0.64 |       92 | 58.24%     | ok               |
|          35 | -82.72%  | -79.79%            | -89.77% |    -0.67 |       78 | 42.34%     | ok               |

## ADBE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 0.21%    | -65.23%            | -21.34% |     0.13 |       74 | 49.42%     | ok               |
|          40 | -12.77%  | -65.23%            | -24.87% |    -0.12 |       72 | 42.43%     | ok               |
|          25 | -18.13%  | -65.23%            | -30.06% |    -0.14 |       50 | 61.40%     | ok               |
|          15 | -28.50%  | -65.23%            | -32.12% |    -0.31 |       61 | 66.06%     | ok               |
|          20 | -28.30%  | -65.23%            | -32.36% |    -0.31 |       50 | 63.56%     | ok               |

## AGG Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -6.61%   | 1.06%              | -10.16% |    -1.1  |       69 | 31.11%     | ok               |
|          45 | -5.75%   | 1.06%              | -7.89%  |    -1.16 |       52 | 20.47%     | ok               |
|          20 | -8.00%   | 1.06%              | -10.96% |    -1.18 |       73 | 36.61%     | ok               |
|          50 | -5.57%   | 1.06%              | -7.92%  |    -1.25 |       46 | 16.97%     | ok               |
|          25 | -8.17%   | 1.06%              | -11.60% |    -1.25 |       73 | 34.94%     | ok               |

## ALGO-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -50.43%  | -75.24%            | -53.13% |    -0.57 |       86 | 38.12%     | ok               |
|          15 | -60.12%  | -75.24%            | -68.72% |    -0.63 |       88 | 50.77%     | ok               |
|          25 | -60.38%  | -75.24%            | -72.68% |    -0.69 |       88 | 45.40%     | ok               |
|          20 | -64.17%  | -75.24%            | -71.41% |    -0.76 |       90 | 48.47%     | ok               |
|          50 | -45.64%  | -75.24%            | -48.43% |    -0.81 |       42 | 16.86%     | ok               |

## AMAT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -11.95%  | 218.98%            | -54.05% |     0.06 |       66 | 62.06%     | ok               |
|          30 | -26.30%  | 218.98%            | -57.21% |    -0.17 |       69 | 53.41%     | ok               |
|          20 | -31.69%  | 218.98%            | -60.16% |    -0.23 |       72 | 58.57%     | ok               |
|          35 | -31.55%  | 218.98%            | -55.26% |    -0.26 |       71 | 51.25%     | ok               |
|          50 | -29.82%  | 218.98%            | -48.72% |    -0.27 |       52 | 39.27%     | ok               |

## AMD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 6.10%    | 220.07%            | -44.26% |     0.26 |       56 | 30.95%     | ok               |
|          40 | 4.02%    | 220.07%            | -44.58% |     0.25 |       56 | 36.27%     | ok               |
|          35 | -9.24%   | 220.07%            | -54.16% |     0.12 |       62 | 38.27%     | ok               |
|          45 | -15.31%  | 220.07%            | -53.24% |     0.03 |       62 | 33.78%     | ok               |
|          30 | -21.21%  | 220.07%            | -59.51% |    -0.01 |       63 | 40.77%     | ok               |

## AMGN Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -9.83%   | 25.87%             | -26.64% |    -0.12 |       71 | 52.41%     | ok               |
|          35 | -11.27%  | 25.87%             | -31.23% |    -0.18 |       65 | 42.43%     | ok               |
|          15 | -13.61%  | 25.87%             | -27.92% |    -0.2  |       69 | 58.24%     | ok               |
|          30 | -15.41%  | 25.87%             | -34.14% |    -0.29 |       69 | 46.26%     | ok               |
|          25 | -18.85%  | 25.87%             | -33.41% |    -0.37 |       65 | 48.59%     | ok               |

## AMZN Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -18.97%  | 39.96%             | -27.15% |    -0.56 |       52 | 29.12%     | ok               |
|          50 | -24.13%  | 39.96%             | -34.08% |    -0.85 |       48 | 23.29%     | ok               |
|          45 | -26.92%  | 39.96%             | -34.08% |    -0.94 |       52 | 26.29%     | ok               |
|          35 | -32.30%  | 39.96%             | -38.29% |    -1.02 |       68 | 32.78%     | ok               |
|          30 | -38.32%  | 39.96%             | -42.48% |    -1.16 |       80 | 38.27%     | ok               |

## APT-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 34.70%   | -91.20%            | -46.73% |     0.58 |       42 | 19.54%     | ok               |
|          45 | 1.99%    | -91.20%            | -63.86% |     0.23 |       60 | 25.48%     | ok               |
|          40 | -17.60%  | -91.20%            | -63.33% |     0.03 |       66 | 31.03%     | ok               |
|          20 | -25.70%  | -91.20%            | -70.51% |     0.02 |       73 | 51.72%     | ok               |
|          35 | -23.64%  | -91.20%            | -64.45% |    -0.02 |       70 | 36.78%     | ok               |

## ARB-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 50.75%   | -86.52%            | -53.74% |     0.62 |       87 | 55.56%     | ok               |
|          40 | 27.74%   | -86.52%            | -47.60% |     0.48 |       50 | 29.12%     | ok               |
|          20 | 13.29%   | -86.52%            | -60.40% |     0.38 |       75 | 49.04%     | ok               |
|          35 | 15.25%   | -86.52%            | -56.00% |     0.38 |       60 | 32.57%     | ok               |
|          45 | 14.56%   | -86.52%            | -50.83% |     0.36 |       56 | 22.41%     | ok               |

## ARKK Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -24.24%  | 68.60%             | -34.75% |    -0.28 |       89 | 50.25%     | ok               |
|          20 | -29.33%  | 68.60%             | -35.15% |    -0.42 |       86 | 45.76%     | ok               |
|          30 | -34.44%  | 68.60%             | -36.89% |    -0.6  |       83 | 39.93%     | ok               |
|          35 | -39.28%  | 68.60%             | -41.55% |    -0.78 |       86 | 37.27%     | ok               |
|          25 | -42.03%  | 68.60%             | -44.20% |    -0.8  |       91 | 41.93%     | ok               |

## ATOM-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -65.40%  | -72.61%            | -71.56% |    -0.97 |       95 | 52.87%     | ok               |
|          15 | -69.86%  | -72.61%            | -72.91% |    -1.02 |       95 | 62.64%     | ok               |
|          45 | -59.71%  | -72.61%            | -65.46% |    -1.1  |       74 | 29.89%     | ok               |
|          30 | -68.04%  | -72.61%            | -74.00% |    -1.12 |       90 | 46.17%     | ok               |
|          20 | -72.66%  | -72.61%            | -75.43% |    -1.17 |      103 | 56.70%     | ok               |

## AVAX-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 24.48%   | -78.86%            | -32.41% |     0.48 |       34 | 19.16%     | ok               |
|          45 | 22.16%   | -78.86%            | -35.57% |     0.45 |       34 | 22.80%     | ok               |
|          40 | 22.12%   | -78.86%            | -35.70% |     0.45 |       40 | 25.67%     | ok               |
|          35 | 13.32%   | -78.86%            | -38.91% |     0.35 |       58 | 31.03%     | ok               |
|          15 | -6.43%   | -78.86%            | -52.46% |     0.19 |       69 | 53.45%     | ok               |

## AVGO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 21.52%   | 191.33%            | -35.76% |     0.4  |       62 | 43.76%     | ok               |
|          35 | 15.68%   | 191.33%            | -36.19% |     0.35 |       70 | 40.93%     | ok               |
|          40 | 15.28%   | 191.33%            | -40.70% |     0.34 |       60 | 37.77%     | ok               |
|          25 | 13.87%   | 191.33%            | -38.01% |     0.33 |       68 | 44.93%     | ok               |
|          50 | 9.58%    | 191.33%            | -35.84% |     0.28 |       62 | 31.61%     | ok               |

## BA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 26.03%   | 12.11%             | -13.34% |     0.67 |       42 | 31.45%     | ok               |
|          35 | 30.46%   | 12.11%             | -23.77% |     0.59 |       72 | 44.59%     | ok               |
|          40 | 20.11%   | 12.11%             | -23.90% |     0.47 |       46 | 38.60%     | ok               |
|          25 | 10.59%   | 12.11%             | -32.48% |     0.29 |       70 | 52.58%     | ok               |
|          30 | 7.60%    | 12.11%             | -30.56% |     0.25 |       67 | 49.25%     | ok               |

## BAC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -1.06%   | 81.13%             | -22.29% |     0.03 |       62 | 36.94%     | ok               |
|          20 | -3.50%   | 81.13%             | -21.48% |     0    |       80 | 53.24%     | ok               |
|          50 | -2.67%   | 81.13%             | -20.82% |    -0.02 |       60 | 33.78%     | ok               |
|          35 | -4.66%   | 81.13%             | -29.13% |    -0.06 |       70 | 44.76%     | ok               |
|          15 | -8.93%   | 81.13%             | -23.70% |    -0.12 |       80 | 58.24%     | ok               |

## BCH-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 3.75%    | -40.98%            | -53.87% |     0.25 |       76 | 48.85%     | ok               |
|          20 | -8.48%   | -40.98%            | -54.02% |     0.15 |       70 | 55.36%     | ok               |
|          15 | -18.95%  | -40.98%            | -60.20% |     0.04 |       79 | 59.96%     | ok               |
|          25 | -20.00%  | -40.98%            | -59.80% |     0    |       72 | 51.15%     | ok               |
|          35 | -18.38%  | -40.98%            | -64.08% |    -0.03 |       70 | 45.02%     | ok               |

## BITO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 21.07%   | -61.67%            | -32.29% |     0.41 |       54 | 25.96%     | ok               |
|          30 | 5.28%    | -61.67%            | -42.82% |     0.24 |       78 | 42.26%     | ok               |
|          15 | -1.33%   | -61.67%            | -48.38% |     0.19 |       87 | 51.08%     | ok               |
|          45 | 1.85%    | -61.67%            | -43.53% |     0.18 |       62 | 29.62%     | ok               |
|          35 | 0.10%    | -61.67%            | -47.25% |     0.18 |       70 | 38.10%     | ok               |

## BLK Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | -3.02%   | 26.84%             | -17.97% |    -0.03 |       78 | 38.77%     | ok               |
|          20 | -5.09%   | 26.84%             | -21.48% |    -0.07 |       78 | 47.42%     | ok               |
|          40 | -4.99%   | 26.84%             | -20.08% |    -0.1  |       70 | 34.61%     | ok               |
|          30 | -9.17%   | 26.84%             | -24.29% |    -0.21 |       73 | 42.60%     | ok               |
|          25 | -10.08%  | 26.84%             | -23.36% |    -0.22 |       73 | 44.93%     | ok               |

## BND Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -6.17%   | 1.06%              | -9.05%  |    -0.9  |       63 | 38.10%     | ok               |
|          25 | -6.87%   | 1.06%              | -10.14% |    -1.05 |       67 | 36.11%     | ok               |
|          30 | -7.32%   | 1.06%              | -9.89%  |    -1.18 |       65 | 32.28%     | ok               |
|          15 | -8.39%   | 1.06%              | -10.58% |    -1.21 |       73 | 40.93%     | ok               |
|          45 | -7.56%   | 1.06%              | -9.57%  |    -1.47 |       50 | 21.96%     | ok               |

## BONK-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 169.29%  | -79.80%            | -35.57% |     1.24 |       44 | 22.03%     | ok               |
|          45 | 121.76%  | -79.80%            | -42.36% |     1.02 |       54 | 26.25%     | ok               |
|          25 | 155.05%  | -79.80%            | -47.99% |     1    |       65 | 48.28%     | ok               |
|          40 | 122.45%  | -79.80%            | -50.07% |     0.97 |       50 | 33.33%     | ok               |
|          20 | 140.65%  | -79.80%            | -55.43% |     0.95 |       66 | 52.87%     | ok               |

## BTC-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 46.18%   | -37.26%            | -14.53% |     0.84 |       46 | 34.87%     | ok               |
|          45 | 40.84%   | -37.26%            | -15.18% |     0.81 |       44 | 30.65%     | ok               |
|          35 | 28.81%   | -37.26%            | -26.34% |     0.58 |       70 | 41.76%     | ok               |
|          50 | 13.98%   | -37.26%            | -18.05% |     0.4  |       42 | 25.29%     | ok               |
|          30 | 13.35%   | -37.26%            | -21.75% |     0.35 |       74 | 48.47%     | ok               |

## C Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -5.07%   | 166.46%            | -22.28% |    -0.06 |       68 | 36.27%     | ok               |
|          45 | -14.74%  | 166.46%            | -30.30% |    -0.31 |       80 | 40.77%     | ok               |
|          25 | -19.47%  | 166.46%            | -34.18% |    -0.32 |       73 | 53.58%     | ok               |
|          15 | -21.51%  | 166.46%            | -35.02% |    -0.34 |       74 | 60.23%     | ok               |
|          20 | -22.16%  | 166.46%            | -35.56% |    -0.37 |       81 | 56.57%     | ok               |

## CAT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 28.37%   | 205.81%            | -21.02% |     0.53 |       72 | 57.07%     | ok               |
|          25 | 28.49%   | 205.81%            | -26.37% |     0.53 |       68 | 59.90%     | ok               |
|          20 | 25.89%   | 205.81%            | -25.65% |     0.49 |       78 | 63.23%     | ok               |
|          45 | 19.31%   | 205.81%            | -27.12% |     0.42 |       56 | 45.92%     | ok               |
|          35 | 16.22%   | 205.81%            | -27.72% |     0.37 |       70 | 50.75%     | ok               |

## CL Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 14.65%   | 11.90%             | -12.98% |     0.62 |       42 | 30.28%     | ok               |
|          30 | 14.15%   | 11.90%             | -14.32% |     0.51 |       60 | 46.26%     | ok               |
|          45 | 9.41%    | 11.90%             | -13.51% |     0.41 |       46 | 33.28%     | ok               |
|          35 | 8.72%    | 11.90%             | -13.83% |     0.35 |       62 | 42.60%     | ok               |
|          40 | 5.56%    | 11.90%             | -12.70% |     0.26 |       56 | 37.27%     | ok               |

## CMCSA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -34.67%  | -40.70%            | -44.35% |    -0.75 |       86 | 58.57%     | ok               |
|          30 | -38.18%  | -40.70%            | -38.49% |    -0.99 |       82 | 43.59%     | ok               |
|          25 | -41.47%  | -40.70%            | -41.51% |    -1.09 |       89 | 48.75%     | ok               |
|          50 | -30.21%  | -40.70%            | -31.36% |    -1.17 |       48 | 15.47%     | ok               |
|          20 | -45.88%  | -40.70%            | -46.89% |    -1.2  |       92 | 54.58%     | ok               |

## COMP-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -4.45%   | -73.20%            | -38.71% |     0.14 |       50 | 20.88%     | ok               |
|          25 | -43.63%  | -73.20%            | -61.30% |    -0.28 |       89 | 51.34%     | ok               |
|          30 | -42.58%  | -73.20%            | -59.19% |    -0.3  |       91 | 46.36%     | ok               |
|          15 | -51.14%  | -73.20%            | -66.20% |    -0.36 |      105 | 62.84%     | ok               |
|          40 | -44.17%  | -73.20%            | -50.01% |    -0.43 |       76 | 34.48%     | ok               |

## COP Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -9.44%   | -6.82%             | -34.85% |    -0.14 |       48 | 27.45%     | ok               |
|          35 | -17.98%  | -6.82%             | -43.58% |    -0.3  |       73 | 37.77%     | ok               |
|          30 | -18.54%  | -6.82%             | -43.96% |    -0.31 |       71 | 40.93%     | ok               |
|          45 | -16.15%  | -6.82%             | -41.14% |    -0.31 |       60 | 30.62%     | ok               |
|          40 | -21.47%  | -6.82%             | -46.86% |    -0.44 |       68 | 33.78%     | ok               |

## COST Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 11.89%   | 31.36%             | -24.32% |     0.39 |       66 | 51.41%     | ok               |
|          25 | 10.23%   | 31.36%             | -24.73% |     0.35 |       63 | 48.59%     | ok               |
|          35 | 5.11%    | 31.36%             | -26.58% |     0.22 |       54 | 41.93%     | ok               |
|          30 | 0.29%    | 31.36%             | -29.73% |     0.08 |       60 | 44.93%     | ok               |
|          40 | -1.35%   | 31.36%             | -28.41% |     0.02 |       56 | 38.94%     | ok               |

## CRM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -37.99%  | -43.13%            | -44.49% |    -0.62 |       92 | 55.24%     | ok               |
|          35 | -33.33%  | -43.13%            | -35.70% |    -0.69 |       64 | 38.77%     | ok               |
|          40 | -37.05%  | -43.13%            | -40.35% |    -0.87 |       70 | 34.61%     | ok               |
|          30 | -42.74%  | -43.13%            | -42.49% |    -0.92 |       67 | 43.59%     | ok               |
|          20 | -47.14%  | -43.13%            | -47.55% |    -0.94 |       80 | 48.92%     | ok               |

## CRV-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 12.61%   | -70.06%            | -37.78% |     0.35 |       68 | 31.42%     | ok               |
|          45 | -1.09%   | -70.06%            | -42.29% |     0.18 |       54 | 20.69%     | ok               |
|          50 | -0.89%   | -70.06%            | -29.30% |     0.18 |       46 | 17.43%     | ok               |
|          40 | -6.61%   | -70.06%            | -38.86% |     0.13 |       58 | 27.01%     | ok               |
|          30 | -10.58%  | -70.06%            | -39.89% |     0.12 |       66 | 36.02%     | ok               |

## CSCO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 34.09%   | 127.37%            | -19.34% |     0.73 |       54 | 38.60%     | ok               |
|          45 | 32.98%   | 127.37%            | -19.34% |     0.7  |       51 | 40.77%     | ok               |
|          25 | 28.70%   | 127.37%            | -23.28% |     0.59 |       63 | 51.91%     | ok               |
|          35 | 28.09%   | 127.37%            | -23.68% |     0.59 |       51 | 47.42%     | ok               |
|          30 | 28.10%   | 127.37%            | -21.79% |     0.58 |       59 | 49.92%     | ok               |

## CVX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -5.78%   | 11.30%             | -23.25% |    -0.08 |       74 | 43.76%     | ok               |
|          20 | -8.98%   | 11.30%             | -25.35% |    -0.17 |       74 | 45.09%     | ok               |
|          35 | -10.99%  | 11.30%             | -28.34% |    -0.26 |       71 | 38.44%     | ok               |
|          30 | -11.36%  | 11.30%             | -27.27% |    -0.26 |       75 | 41.43%     | ok               |
|          40 | -10.83%  | 11.30%             | -26.83% |    -0.28 |       75 | 34.94%     | ok               |

## DASH-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 137.88%  | 13.75%             | -28.93% |     0.99 |       40 | 16.09%     | ok               |
|          40 | 81.99%   | 13.75%             | -32.07% |     0.75 |       48 | 23.56%     | ok               |
|          45 | 71.79%   | 13.75%             | -37.43% |     0.71 |       44 | 18.39%     | ok               |
|          35 | -32.14%  | 13.75%             | -63.23% |     0.09 |       69 | 28.16%     | ok               |
|          25 | -38.31%  | 13.75%             | -64.14% |     0.03 |       69 | 34.29%     | ok               |

## DBC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -10.38%  | 21.29%             | -27.14% |    -0.32 |       73 | 37.94%     | ok               |
|          50 | -8.58%   | 21.29%             | -20.31% |    -0.32 |       40 | 20.97%     | ok               |
|          35 | -10.31%  | 21.29%             | -23.91% |    -0.34 |       60 | 31.45%     | ok               |
|          45 | -10.35%  | 21.29%             | -21.46% |    -0.37 |       54 | 24.46%     | ok               |
|          30 | -12.98%  | 21.29%             | -25.70% |    -0.45 |       58 | 32.78%     | ok               |

## DE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 0.02%    | 66.60%             | -22.53% |     0.08 |       70 | 32.11%     | ok               |
|          30 | -0.97%   | 66.60%             | -25.24% |     0.08 |       72 | 46.92%     | ok               |
|          20 | -1.38%   | 66.60%             | -29.90% |     0.07 |       74 | 52.08%     | ok               |
|          45 | -2.03%   | 66.60%             | -26.22% |     0.04 |       70 | 36.61%     | ok               |
|          25 | -3.82%   | 66.60%             | -27.66% |     0.02 |       76 | 49.42%     | ok               |

## DIA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | -0.44%   | 37.07%             | -13.15% |     0.01 |       60 | 42.93%     | ok               |
|          25 | -0.97%   | 37.07%             | -11.28% |    -0.01 |       60 | 46.26%     | ok               |
|          30 | -2.50%   | 37.07%             | -12.94% |    -0.1  |       60 | 45.09%     | ok               |
|          20 | -4.36%   | 37.07%             | -13.85% |    -0.19 |       64 | 48.59%     | ok               |
|          40 | -4.50%   | 37.07%             | -15.06% |    -0.23 |       66 | 40.10%     | ok               |

## DIS Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 18.97%   | -10.13%            | -14.24% |     0.59 |       50 | 28.95%     | ok               |
|          45 | -5.88%   | -10.13%            | -16.54% |    -0.06 |       53 | 32.61%     | ok               |
|          40 | -6.73%   | -10.13%            | -22.77% |    -0.06 |       65 | 37.77%     | ok               |
|          35 | -12.92%  | -10.13%            | -25.70% |    -0.2  |       75 | 43.93%     | ok               |
|          15 | -15.14%  | -10.13%            | -31.15% |    -0.2  |       89 | 58.24%     | ok               |

## DOGE-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 16.81%   | -75.64%            | -57.89% |     0.42 |       83 | 66.67%     | ok               |
|          20 | -0.26%   | -75.64%            | -55.83% |     0.27 |       86 | 61.88%     | ok               |
|          25 | -6.29%   | -75.64%            | -53.72% |     0.21 |       74 | 56.32%     | ok               |
|          30 | -21.59%  | -75.64%            | -60.95% |     0.03 |       77 | 50.77%     | ok               |
|          35 | -48.65%  | -75.64%            | -63.16% |    -0.44 |       74 | 44.06%     | ok               |

## DOT-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -14.04%  | -85.46%            | -46.17% |    -0.03 |       58 | 26.25%     | ok               |
|          45 | -21.37%  | -85.46%            | -54.01% |    -0.12 |       50 | 31.03%     | ok               |
|          35 | -42.54%  | -85.46%            | -61.76% |    -0.3  |       78 | 41.57%     | ok               |
|          40 | -35.47%  | -85.46%            | -53.72% |    -0.33 |       56 | 34.29%     | ok               |
|          30 | -46.31%  | -85.46%            | -61.81% |    -0.34 |       88 | 48.85%     | ok               |

## DXY-INDEX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -3.43%   | -0.30%             | -11.37% |    -0.29 |       82 | 76.96%     | ok               |
|          50 | -2.28%   | -0.30%             | -6.28%  |    -0.35 |       40 | 30.00%     | ok               |
|          40 | -4.09%   | -0.30%             | -7.30%  |    -0.52 |       74 | 49.57%     | ok               |
|          30 | -5.04%   | -0.30%             | -9.61%  |    -0.58 |       72 | 61.96%     | ok               |
|          25 | -6.00%   | -0.30%             | -12.10% |    -0.65 |       78 | 67.17%     | ok               |

## EEM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -4.96%   | 70.72%             | -19.52% |    -0.11 |       64 | 39.77%     | ok               |
|          35 | -5.62%   | 70.72%             | -23.88% |    -0.12 |       66 | 41.76%     | ok               |
|          50 | -4.94%   | 70.72%             | -15.88% |    -0.12 |       52 | 35.77%     | ok               |
|          45 | -6.04%   | 70.72%             | -17.36% |    -0.16 |       54 | 37.44%     | ok               |
|          25 | -8.49%   | 70.72%             | -25.60% |    -0.21 |       65 | 44.76%     | ok               |

## EFA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -3.05%   | 40.05%             | -10.80% |    -0.05 |       62 | 52.41%     | ok               |
|          30 | -8.17%   | 40.05%             | -13.72% |    -0.29 |       60 | 44.09%     | ok               |
|          20 | -9.78%   | 40.05%             | -12.73% |    -0.34 |       69 | 49.42%     | ok               |
|          40 | -9.56%   | 40.05%             | -15.58% |    -0.39 |       64 | 40.27%     | ok               |
|          50 | -9.07%   | 40.05%             | -17.56% |    -0.4  |       54 | 36.27%     | ok               |

## EOG Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -20.10%  | 16.52%             | -39.69% |    -0.48 |       54 | 32.28%     | ok               |
|          50 | -21.27%  | 16.52%             | -40.57% |    -0.53 |       58 | 29.45%     | ok               |
|          30 | -24.73%  | 16.52%             | -48.13% |    -0.54 |       77 | 46.09%     | ok               |
|          35 | -25.56%  | 16.52%             | -46.26% |    -0.61 |       75 | 40.77%     | ok               |
|          40 | -24.83%  | 16.52%             | -43.26% |    -0.61 |       62 | 35.61%     | ok               |

## ETC-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -7.93%   | -71.93%            | -27.89% |    -0.02 |       28 | 17.05%     | ok               |
|          35 | -15.03%  | -71.93%            | -42.62% |    -0.11 |       44 | 27.01%     | ok               |
|          45 | -16.07%  | -71.93%            | -35.44% |    -0.17 |       26 | 18.97%     | ok               |
|          40 | -21.04%  | -71.93%            | -40.48% |    -0.26 |       42 | 22.80%     | ok               |
|          30 | -35.69%  | -71.93%            | -48.16% |    -0.51 |       64 | 31.23%     | ok               |

## ETH-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 144.24%  | -43.17%            | -30.11% |     1.21 |       62 | 45.21%     | ok               |
|          30 | 142.03%  | -43.17%            | -32.89% |     1.16 |       66 | 53.64%     | ok               |
|          40 | 50.09%   | -43.17%            | -33.11% |     0.69 |       60 | 37.93%     | ok               |
|          20 | 54.08%   | -43.17%            | -39.10% |     0.67 |       82 | 62.84%     | ok               |
|          25 | 52.95%   | -43.17%            | -40.90% |     0.67 |       66 | 58.62%     | ok               |

## EWJ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -18.16%  | 42.98%             | -30.73% |    -0.59 |       62 | 39.10%     | ok               |
|          20 | -19.55%  | 42.98%             | -31.32% |    -0.62 |       58 | 41.10%     | ok               |
|          45 | -18.94%  | 42.98%             | -27.68% |    -0.72 |       58 | 31.28%     | ok               |
|          25 | -21.87%  | 42.98%             | -31.18% |    -0.72 |       58 | 40.10%     | ok               |
|          35 | -22.08%  | 42.98%             | -32.54% |    -0.75 |       68 | 37.44%     | ok               |

## FCX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -4.48%   | 63.28%             | -27.82% |     0.06 |       52 | 29.45%     | ok               |
|          45 | -8.60%   | 63.28%             | -35.29% |    -0    |       52 | 33.94%     | ok               |
|          40 | -20.30%  | 63.28%             | -44.23% |    -0.2  |       62 | 38.44%     | ok               |
|          30 | -28.65%  | 63.28%             | -48.09% |    -0.33 |       63 | 45.09%     | ok               |
|          20 | -34.13%  | 63.28%             | -57.65% |    -0.39 |       70 | 51.91%     | ok               |

## FET-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 7.96%    | -82.12%            | -58.75% |     0.37 |       82 | 50.19%     | ok               |
|          15 | -18.22%  | -82.12%            | -59.58% |     0.17 |       82 | 54.02%     | ok               |
|          25 | -32.88%  | -82.12%            | -59.31% |    -0.03 |       85 | 43.68%     | ok               |
|          30 | -34.65%  | -82.12%            | -48.39% |    -0.08 |       77 | 39.66%     | ok               |
|          35 | -50.57%  | -82.12%            | -60.25% |    -0.44 |       63 | 32.95%     | ok               |

## FIL-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -11.71%  | -82.23%            | -41.11% |     0.01 |       48 | 23.37%     | ok               |
|          45 | -27.58%  | -82.23%            | -43.98% |    -0.29 |       44 | 17.62%     | ok               |
|          35 | -33.31%  | -82.23%            | -48.17% |    -0.32 |       58 | 27.39%     | ok               |
|          50 | -26.52%  | -82.23%            | -44.97% |    -0.32 |       38 | 13.03%     | ok               |
|          30 | -36.50%  | -82.23%            | -50.88% |    -0.35 |       72 | 32.95%     | ok               |

## FXI Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -3.45%   | 45.30%             | -22.57% |     0    |       44 | 30.95%     | ok               |
|          30 | -4.00%   | 45.30%             | -23.91% |    -0.01 |       44 | 29.78%     | ok               |
|          15 | -6.31%   | 45.30%             | -21.68% |    -0.06 |       52 | 34.28%     | ok               |
|          45 | -6.46%   | 45.30%             | -26.75% |    -0.09 |       44 | 24.46%     | ok               |
|          20 | -7.34%   | 45.30%             | -24.53% |    -0.09 |       50 | 32.11%     | ok               |

## GDX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 18.06%   | 191.95%            | -35.59% |     0.39 |       73 | 52.91%     | ok               |
|          40 | 13.85%   | 191.95%            | -31.87% |     0.35 |       64 | 42.93%     | ok               |
|          30 | 11.28%   | 191.95%            | -34.99% |     0.3  |       60 | 48.09%     | ok               |
|          35 | 8.95%    | 191.95%            | -32.37% |     0.27 |       68 | 45.26%     | ok               |
|          25 | 6.77%    | 191.95%            | -38.90% |     0.24 |       63 | 49.75%     | ok               |

## GDXJ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -7.90%   | 216.80%            | -45.05% |     0.06 |       67 | 53.24%     | ok               |
|          50 | -18.94%  | 216.80%            | -44.94% |    -0.2  |       58 | 37.94%     | ok               |
|          30 | -23.13%  | 216.80%            | -44.93% |    -0.22 |       68 | 46.42%     | ok               |
|          25 | -26.54%  | 216.80%            | -47.26% |    -0.25 |       72 | 49.92%     | ok               |
|          35 | -26.76%  | 216.80%            | -43.49% |    -0.3  |       70 | 44.09%     | ok               |

## GE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 45.31%   | 240.67%            | -22.29% |     0.82 |       66 | 40.77%     | ok               |
|          45 | 34.34%   | 240.67%            | -25.68% |     0.66 |       74 | 43.59%     | ok               |
|          20 | 33.35%   | 240.67%            | -26.63% |     0.6  |       69 | 57.40%     | ok               |
|          35 | 27.36%   | 240.67%            | -27.11% |     0.54 |       80 | 48.92%     | ok               |
|          40 | 26.40%   | 240.67%            | -26.97% |     0.54 |       76 | 45.09%     | ok               |

## GLD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | 30.10%   | 103.69%            | -14.61% |     0.73 |       46 | 47.59%     | ok               |
|          20 | 28.16%   | 103.69%            | -14.61% |     0.69 |       48 | 48.92%     | ok               |
|          30 | 23.90%   | 103.69%            | -16.63% |     0.62 |       48 | 46.42%     | ok               |
|          35 | 19.08%   | 103.69%            | -17.29% |     0.52 |       50 | 45.59%     | ok               |
|          15 | 20.31%   | 103.69%            | -17.54% |     0.52 |       50 | 53.08%     | ok               |

## GOOGL Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | 76.77%   | 145.95%            | -19.76% |     1.14 |       57 | 55.74%     | ok               |
|          30 | 72.01%   | 145.95%            | -20.41% |     1.1  |       63 | 53.24%     | ok               |
|          20 | 63.42%   | 145.95%            | -20.57% |     0.99 |       68 | 58.07%     | ok               |
|          15 | 65.21%   | 145.95%            | -13.81% |     0.98 |       71 | 63.23%     | ok               |
|          35 | 55.27%   | 145.95%            | -22.85% |     0.97 |       71 | 48.09%     | ok               |

## GRT-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 35.80%   | -89.11%            | -30.00% |     0.61 |       40 | 20.88%     | ok               |
|          15 | 6.32%    | -89.11%            | -49.67% |     0.32 |       75 | 61.69%     | ok               |
|          20 | 2.63%    | -89.11%            | -46.47% |     0.27 |       83 | 56.13%     | ok               |
|          45 | 5.51%    | -89.11%            | -48.76% |     0.25 |       48 | 26.05%     | ok               |
|          35 | 1.62%    | -89.11%            | -49.87% |     0.22 |       60 | 35.25%     | ok               |

## GS Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 21.11%   | 174.63%            | -20.56% |     0.47 |       74 | 61.06%     | ok               |
|          20 | 4.59%    | 174.63%            | -23.19% |     0.19 |       74 | 57.07%     | ok               |
|          40 | 0.08%    | 174.63%            | -17.88% |     0.09 |       72 | 45.26%     | ok               |
|          25 | -0.70%   | 174.63%            | -23.32% |     0.09 |       74 | 54.58%     | ok               |
|          30 | -2.38%   | 174.63%            | -22.13% |     0.05 |       76 | 52.08%     | ok               |

## HD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -3.53%   | -3.44%             | -17.69% |    -0.01 |       71 | 44.26%     | ok               |
|          25 | -4.28%   | -3.44%             | -18.51% |    -0.03 |       70 | 46.26%     | ok               |
|          15 | -14.59%  | -3.44%             | -27.53% |    -0.29 |      108 | 54.91%     | ok               |
|          35 | -13.77%  | -3.44%             | -22.98% |    -0.33 |       80 | 40.27%     | ok               |
|          45 | -11.70%  | -3.44%             | -21.41% |    -0.34 |       60 | 28.29%     | ok               |

## HON Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -13.43%  | 20.04%             | -21.17% |    -0.4  |       72 | 31.78%     | ok               |
|          45 | -15.16%  | 20.04%             | -19.99% |    -0.43 |       74 | 36.77%     | ok               |
|          40 | -23.52%  | 20.04%             | -26.29% |    -0.66 |       76 | 41.10%     | ok               |
|          35 | -24.98%  | 20.04%             | -27.37% |    -0.69 |       91 | 47.42%     | ok               |
|          30 | -26.82%  | 20.04%             | -29.80% |    -0.72 |       93 | 52.41%     | ok               |

## HYG Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -7.92%   | 3.24%              | -7.92%  |    -0.96 |       70 | 29.45%     | ok               |
|          15 | -9.71%   | 3.24%              | -10.06% |    -1.05 |       88 | 41.43%     | ok               |
|          20 | -9.69%   | 3.24%              | -10.29% |    -1.08 |       86 | 39.10%     | ok               |
|          45 | -8.60%   | 3.24%              | -8.60%  |    -1.08 |       66 | 26.29%     | ok               |
|          30 | -9.52%   | 3.24%              | -9.59%  |    -1.11 |       81 | 34.28%     | ok               |

## IBIT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 53.73%   | -4.97%             | -17.37% |     1.08 |       22 | 22.75%     | ok               |
|          15 | 61.58%   | -4.97%             | -19.20% |     1.01 |       38 | 40.05%     | ok               |
|          45 | 44.27%   | -4.97%             | -17.37% |     0.91 |       26 | 24.17%     | ok               |
|          40 | 38.04%   | -4.97%             | -17.78% |     0.81 |       26 | 26.07%     | ok               |
|          30 | 33.13%   | -4.97%             | -18.95% |     0.7  |       32 | 32.46%     | ok               |

## IBM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 20.02%   | 60.74%             | -28.20% |     0.44 |       92 | 62.06%     | ok               |
|          30 | 6.48%    | 60.74%             | -27.54% |     0.23 |       78 | 49.75%     | ok               |
|          20 | 1.80%    | 60.74%             | -34.12% |     0.15 |       76 | 54.41%     | ok               |
|          35 | 1.85%    | 60.74%             | -27.54% |     0.14 |       74 | 45.26%     | ok               |
|          50 | -0.38%   | 60.74%             | -22.50% |     0.08 |       56 | 32.45%     | ok               |

## ICP-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 17.48%   | -74.42%            | -38.23% |     0.39 |       66 | 29.69%     | ok               |
|          40 | 11.27%   | -74.42%            | -32.85% |     0.33 |       60 | 25.29%     | ok               |
|          30 | 3.64%    | -74.42%            | -51.29% |     0.29 |       81 | 35.82%     | ok               |
|          50 | -0.81%   | -74.42%            | -43.65% |     0.17 |       38 | 15.52%     | ok               |
|          45 | -12.39%  | -74.42%            | -40.57% |     0.02 |       58 | 19.54%     | ok               |

## IEF Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -6.92%   | -0.33%             | -9.79%  |    -0.82 |       70 | 42.26%     | ok               |
|          15 | -7.48%   | -0.33%             | -10.52% |    -0.88 |       69 | 43.76%     | ok               |
|          40 | -8.39%   | -0.33%             | -9.67%  |    -1.31 |       60 | 24.79%     | ok               |
|          45 | -8.07%   | -0.33%             | -9.73%  |    -1.33 |       50 | 22.80%     | ok               |
|          25 | -10.50%  | -0.33%             | -11.19% |    -1.34 |       76 | 39.43%     | ok               |

## IEMG Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | -0.32%   | 64.53%             | -22.13% |     0.05 |       63 | 42.60%     | ok               |
|          50 | -2.69%   | 64.53%             | -14.40% |    -0.05 |       56 | 33.94%     | ok               |
|          40 | -2.99%   | 64.53%             | -18.89% |    -0.05 |       62 | 39.77%     | ok               |
|          45 | -2.90%   | 64.53%             | -15.40% |    -0.05 |       52 | 36.61%     | ok               |
|          25 | -4.72%   | 64.53%             | -25.58% |    -0.09 |       59 | 45.42%     | ok               |

## INJ-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -16.04%  | -73.99%            | -56.91% |    -0.02 |       44 | 22.22%     | ok               |
|          35 | -22.55%  | -73.99%            | -61.19% |    -0.04 |       58 | 31.61%     | ok               |
|          50 | -25.16%  | -73.99%            | -52.76% |    -0.19 |       48 | 19.16%     | ok               |
|          40 | -30.34%  | -73.99%            | -59.56% |    -0.21 |       48 | 27.97%     | ok               |
|          20 | -50.45%  | -73.99%            | -79.76% |    -0.36 |       78 | 46.36%     | ok               |

## INTC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 87.36%   | 182.15%            | -53.65% |     0.76 |       82 | 60.90%     | ok               |
|          45 | 76.11%   | 182.15%            | -49.32% |     0.74 |       60 | 34.28%     | ok               |
|          25 | 75.50%   | 182.15%            | -56.41% |     0.72 |       75 | 51.58%     | ok               |
|          20 | 76.16%   | 182.15%            | -52.47% |     0.71 |       80 | 56.41%     | ok               |
|          40 | 70.33%   | 182.15%            | -55.86% |     0.7  |       68 | 38.60%     | ok               |

## INTU Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -5.44%   | -58.65%            | -43.68% |     0.02 |       73 | 28.79%     | ok               |
|          45 | -7.43%   | -58.65%            | -44.75% |    -0.02 |       71 | 32.78%     | ok               |
|          40 | -12.78%  | -58.65%            | -47.52% |    -0.12 |       71 | 35.44%     | ok               |
|          25 | -17.80%  | -58.65%            | -42.24% |    -0.19 |       66 | 45.09%     | ok               |
|          15 | -18.42%  | -58.65%            | -47.30% |    -0.19 |       83 | 50.58%     | ok               |

## ITA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 5.54%    | 101.17%            | -21.48% |     0.24 |       76 | 37.94%     | ok               |
|          15 | 4.38%    | 101.17%            | -26.46% |     0.19 |       85 | 59.40%     | ok               |
|          30 | 1.88%    | 101.17%            | -23.75% |     0.13 |       72 | 47.92%     | ok               |
|          35 | -0.29%   | 101.17%            | -23.16% |     0.06 |       76 | 46.26%     | ok               |
|          40 | -1.44%   | 101.17%            | -20.58% |     0.02 |       78 | 42.76%     | ok               |

## IWM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | 9.59%    | 49.94%             | -13.48% |     0.39 |       50 | 37.10%     | ok               |
|          40 | 8.60%    | 49.94%             | -14.08% |     0.39 |       42 | 31.28%     | ok               |
|          30 | 9.40%    | 49.94%             | -12.83% |     0.39 |       48 | 35.77%     | ok               |
|          35 | 8.35%    | 49.94%             | -14.11% |     0.36 |       48 | 33.61%     | ok               |
|          20 | 5.27%    | 49.94%             | -14.01% |     0.24 |       60 | 38.10%     | ok               |

## JNJ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 22.89%   | 65.43%             | -10.57% |     0.93 |       58 | 37.27%     | ok               |
|          15 | 15.94%   | 65.43%             | -18.02% |     0.55 |       68 | 56.91%     | ok               |
|          45 | 13.09%   | 65.43%             | -13.35% |     0.55 |       60 | 42.26%     | ok               |
|          20 | 12.01%   | 65.43%             | -17.61% |     0.45 |       72 | 53.58%     | ok               |
|          40 | 10.62%   | 65.43%             | -14.77% |     0.44 |       66 | 46.42%     | ok               |

## JPM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 23.43%   | 92.97%             | -15.90% |     0.75 |       52 | 41.60%     | ok               |
|          45 | 11.71%   | 92.97%             | -21.91% |     0.4  |       54 | 44.59%     | ok               |
|          40 | -3.05%   | 92.97%             | -28.47% |    -0.01 |       66 | 47.09%     | ok               |
|          20 | -10.64%  | 92.97%             | -33.59% |    -0.15 |       86 | 58.57%     | ok               |
|          35 | -8.46%   | 92.97%             | -27.43% |    -0.16 |       72 | 50.75%     | ok               |

## KO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 28.93%   | 39.29%             | -8.07%  |     1.03 |       49 | 37.77%     | ok               |
|          35 | 24.98%   | 39.29%             | -8.07%  |     0.93 |       52 | 36.44%     | ok               |
|          40 | 22.37%   | 39.29%             | -9.28%  |     0.9  |       54 | 33.28%     | ok               |
|          25 | 23.60%   | 39.29%             | -9.37%  |     0.86 |       55 | 40.43%     | ok               |
|          50 | 14.81%   | 39.29%             | -11.40% |     0.68 |       36 | 26.79%     | ok               |

## LDO-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 33.16%   | -86.32%            | -43.48% |     0.53 |       83 | 51.72%     | ok               |
|          20 | 20.87%   | -86.32%            | -43.71% |     0.45 |       85 | 47.13%     | ok               |
|          50 | 13.59%   | -86.32%            | -48.77% |     0.35 |       46 | 16.67%     | ok               |
|          30 | 8.74%    | -86.32%            | -58.32% |     0.34 |       72 | 37.74%     | ok               |
|          35 | -0.97%   | -86.32%            | -63.16% |     0.24 |       74 | 30.65%     | ok               |

## LIN Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 5.16%    | 28.87%             | -23.68% |     0.23 |       62 | 49.42%     | ok               |
|          25 | 4.87%    | 28.87%             | -22.01% |     0.23 |       61 | 41.43%     | ok               |
|          20 | 2.62%    | 28.87%             | -23.00% |     0.15 |       60 | 44.59%     | ok               |
|          35 | 1.08%    | 28.87%             | -21.18% |     0.1  |       60 | 32.11%     | ok               |
|          30 | 0.44%    | 28.87%             | -21.53% |     0.08 |       64 | 38.60%     | ok               |

## LINK-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -18.18%  | -65.75%            | -50.48% |     0.04 |       72 | 41.76%     | ok               |
|          45 | -16.95%  | -65.75%            | -38.56% |    -0    |       50 | 26.25%     | ok               |
|          50 | -16.55%  | -65.75%            | -36.98% |    -0.02 |       40 | 20.88%     | ok               |
|          35 | -27.53%  | -65.75%            | -49.56% |    -0.1  |       60 | 36.40%     | ok               |
|          40 | -31.51%  | -65.75%            | -50.91% |    -0.19 |       56 | 30.65%     | ok               |

## LLY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 6.56%    | 62.14%             | -38.23% |     0.23 |       46 | 37.77%     | ok               |
|          15 | -0.48%   | 62.14%             | -48.12% |     0.14 |       63 | 61.56%     | ok               |
|          45 | -5.43%   | 62.14%             | -42.66% |     0.01 |       54 | 41.26%     | ok               |
|          20 | -16.51%  | 62.14%             | -51.34% |    -0.14 |       72 | 56.57%     | ok               |
|          25 | -17.89%  | 62.14%             | -53.47% |    -0.17 |       68 | 53.91%     | ok               |

## LRCX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -7.85%   | 284.17%            | -60.45% |     0.11 |       83 | 55.57%     | ok               |
|          50 | -12.88%  | 284.17%            | -50.39% |    -0    |       80 | 37.27%     | ok               |
|          40 | -15.49%  | 284.17%            | -56.86% |    -0.02 |       72 | 43.09%     | ok               |
|          35 | -20.98%  | 284.17%            | -61.76% |    -0.08 |       80 | 45.09%     | ok               |
|          20 | -23.51%  | 284.17%            | -67.64% |    -0.1  |       87 | 51.25%     | ok               |

## LTC-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -12.22%  | -62.67%            | -44.78% |    -0    |       56 | 31.80%     | ok               |
|          35 | -22.47%  | -62.67%            | -54.86% |    -0.13 |       66 | 42.91%     | ok               |
|          30 | -34.00%  | -62.67%            | -53.76% |    -0.29 |       66 | 48.47%     | ok               |
|          40 | -31.40%  | -62.67%            | -56.10% |    -0.3  |       58 | 38.12%     | ok               |
|          25 | -36.79%  | -62.67%            | -54.26% |    -0.33 |       74 | 50.96%     | ok               |

## MCD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 2.85%    | -3.44%             | -9.22%  |     0.19 |       42 | 20.63%     | ok               |
|          30 | -2.55%   | -3.44%             | -18.81% |    -0.05 |       75 | 38.10%     | ok               |
|          25 | -3.59%   | -3.44%             | -20.47% |    -0.09 |       75 | 40.77%     | ok               |
|          35 | -7.68%   | -3.44%             | -15.45% |    -0.29 |       67 | 34.44%     | ok               |
|          40 | -7.95%   | -3.44%             | -16.86% |    -0.33 |       71 | 28.79%     | ok               |

## META Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -8.24%   | 28.24%             | -31.03% |    -0.06 |       66 | 38.44%     | ok               |
|          40 | -18.32%  | 28.24%             | -35.11% |    -0.27 |       66 | 41.43%     | ok               |
|          25 | -26.39%  | 28.24%             | -39.84% |    -0.41 |       67 | 52.08%     | ok               |
|          50 | -22.25%  | 28.24%             | -34.00% |    -0.41 |       70 | 34.61%     | ok               |
|          30 | -28.36%  | 28.24%             | -38.96% |    -0.47 |       72 | 48.92%     | ok               |

## MPC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 12.27%   | 58.26%             | -23.96% |     0.34 |       52 | 38.10%     | ok               |
|          45 | 5.15%    | 58.26%             | -25.09% |     0.21 |       58 | 41.76%     | ok               |
|          40 | 3.55%    | 58.26%             | -25.70% |     0.18 |       60 | 44.09%     | ok               |
|          35 | 0.35%    | 58.26%             | -35.90% |     0.12 |       68 | 46.59%     | ok               |
|          30 | -15.43%  | 58.26%             | -44.76% |    -0.17 |       71 | 49.42%     | ok               |

## MRK Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -20.59%  | 1.06%              | -30.12% |    -0.38 |       87 | 55.91%     | ok               |
|          25 | -20.21%  | 1.06%              | -31.07% |    -0.41 |       72 | 47.92%     | ok               |
|          20 | -24.12%  | 1.06%              | -29.59% |    -0.51 |       77 | 51.25%     | ok               |
|          45 | -23.04%  | 1.06%              | -26.02% |    -0.61 |       57 | 34.11%     | ok               |
|          50 | -22.69%  | 1.06%              | -25.69% |    -0.65 |       56 | 31.11%     | ok               |

## MS Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -0.59%   | 158.59%            | -19.99% |     0.07 |       72 | 41.26%     | ok               |
|          35 | -7.52%   | 158.59%            | -25.26% |    -0.1  |       76 | 45.92%     | ok               |
|          15 | -11.36%  | 158.59%            | -23.25% |    -0.15 |       78 | 58.74%     | ok               |
|          20 | -11.47%  | 158.59%            | -25.68% |    -0.18 |       82 | 54.91%     | ok               |
|          30 | -13.27%  | 158.59%            | -27.79% |    -0.24 |       81 | 49.92%     | ok               |

## MSFT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -25.23%  | -8.04%             | -25.60% |    -0.73 |       68 | 34.94%     | ok               |
|          50 | -27.38%  | -8.04%             | -28.14% |    -0.83 |       64 | 30.12%     | ok               |
|          35 | -37.09%  | -8.04%             | -36.27% |    -1.02 |       75 | 43.59%     | ok               |
|          40 | -36.49%  | -8.04%             | -35.66% |    -1.04 |       71 | 38.44%     | ok               |
|          25 | -40.15%  | -8.04%             | -40.01% |    -1.06 |       87 | 51.25%     | ok               |

## MU Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 421.65%  | 1050.95%           | -61.96% |     1.55 |       48 | 68.05%     | ok               |
|          25 | 334.60%  | 1050.95%           | -67.90% |     1.46 |       49 | 61.73%     | ok               |
|          40 | 290.77%  | 1050.95%           | -64.07% |     1.4  |       56 | 55.24%     | ok               |
|          20 | 297.89%  | 1050.95%           | -67.25% |     1.37 |       55 | 63.89%     | ok               |
|          30 | 270.20%  | 1050.95%           | -68.76% |     1.34 |       51 | 59.90%     | ok               |

## NEAR-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 117.25%  | -52.58%            | -44.39% |     1.06 |       44 | 23.95%     | ok               |
|          50 | 82.68%   | -52.58%            | -49.90% |     0.9  |       40 | 18.97%     | ok               |
|          40 | 85.21%   | -52.58%            | -53.32% |     0.88 |       44 | 27.97%     | ok               |
|          35 | 51.62%   | -52.58%            | -58.99% |     0.66 |       66 | 32.76%     | ok               |
|          30 | 22.12%   | -52.58%            | -60.07% |     0.44 |       85 | 41.00%     | ok               |

## NEM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 0.76%    | 199.48%            | -29.41% |     0.19 |       64 | 61.56%     | ok               |
|          20 | -10.03%  | 199.48%            | -30.47% |     0.04 |       74 | 57.07%     | ok               |
|          25 | -23.16%  | 199.48%            | -37.89% |    -0.18 |       70 | 54.91%     | ok               |
|          50 | -23.65%  | 199.48%            | -32.97% |    -0.25 |       56 | 40.77%     | ok               |
|          30 | -32.79%  | 199.48%            | -38.49% |    -0.36 |       74 | 53.24%     | ok               |

## NFLX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 53.81%   | 35.43%             | -11.94% |     1.07 |       46 | 47.09%     | ok               |
|          50 | 47.62%   | 35.43%             | -16.28% |     1.04 |       48 | 39.43%     | ok               |
|          35 | 45.90%   | 35.43%             | -18.30% |     0.91 |       60 | 50.58%     | ok               |
|          45 | 37.18%   | 35.43%             | -15.48% |     0.82 |       52 | 43.43%     | ok               |
|          25 | 35.57%   | 35.43%             | -21.09% |     0.73 |       60 | 57.07%     | ok               |

## NKE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | -26.93%  | -58.53%            | -42.13% |    -0.38 |       75 | 37.27%     | ok               |
|          20 | -33.86%  | -58.53%            | -50.44% |    -0.42 |       93 | 52.58%     | ok               |
|          25 | -34.08%  | -58.53%            | -51.20% |    -0.44 |       89 | 48.75%     | ok               |
|          40 | -26.46%  | -58.53%            | -31.19% |    -0.5  |       63 | 30.12%     | ok               |
|          15 | -38.05%  | -58.53%            | -55.28% |    -0.5  |       90 | 57.07%     | ok               |

## NOW Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 8.70%    | -33.62%            | -26.36% |     0.27 |       79 | 51.58%     | ok               |
|          30 | 4.84%    | -33.62%            | -28.41% |     0.22 |       80 | 45.59%     | ok               |
|          15 | 1.48%    | -33.62%            | -26.36% |     0.19 |       88 | 54.74%     | ok               |
|          25 | -1.12%   | -33.62%            | -25.70% |     0.15 |       72 | 48.92%     | ok               |
|          35 | -1.93%   | -33.62%            | -27.43% |     0.12 |       81 | 40.27%     | ok               |

## NVDA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -1.32%   | 129.10%            | -35.26% |     0.14 |       70 | 47.59%     | ok               |
|          25 | -2.68%   | 129.10%            | -33.22% |     0.13 |       68 | 50.27%     | ok               |
|          20 | -6.66%   | 129.10%            | -40.59% |     0.09 |       69 | 55.08%     | ok               |
|          35 | -14.66%  | 129.10%            | -41.25% |    -0.08 |       78 | 44.74%     | ok               |
|          50 | -14.29%  | 129.10%            | -40.84% |    -0.11 |       56 | 32.09%     | ok               |

## OP-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 48.20%   | -92.12%            | -36.11% |     0.71 |       32 | 11.30%     | ok               |
|          45 | 47.14%   | -92.12%            | -45.76% |     0.66 |       34 | 15.90%     | ok               |
|          40 | 25.72%   | -92.12%            | -53.61% |     0.47 |       48 | 24.33%     | ok               |
|          35 | 5.13%    | -92.12%            | -58.13% |     0.27 |       56 | 27.59%     | ok               |
|          30 | -13.99%  | -92.12%            | -70.11% |     0.1  |       70 | 34.10%     | ok               |

## ORCL Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 193.48%  | 23.25%             | -29.32% |     1.23 |       74 | 65.22%     | ok               |
|          25 | 120.16%  | 23.25%             | -27.76% |     0.97 |       75 | 57.74%     | ok               |
|          20 | 116.38%  | 23.25%             | -29.32% |     0.95 |       77 | 60.90%     | ok               |
|          35 | 88.76%   | 23.25%             | -31.95% |     0.84 |       68 | 49.42%     | ok               |
|          30 | 88.92%   | 23.25%             | -29.47% |     0.84 |       74 | 53.58%     | ok               |

## OXY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 8.21%    | -15.07%            | -31.73% |     0.26 |       67 | 43.09%     | ok               |
|          35 | 7.10%    | -15.07%            | -29.95% |     0.24 |       66 | 38.44%     | ok               |
|          40 | 4.48%    | -15.07%            | -31.66% |     0.19 |       54 | 34.44%     | ok               |
|          50 | 0.83%    | -15.07%            | -30.54% |     0.12 |       36 | 27.79%     | ok               |
|          25 | -4.99%   | -15.07%            | -40.06% |     0.03 |       73 | 47.42%     | ok               |

## PEP Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 13.53%   | -14.54%            | -11.62% |     0.61 |       44 | 26.96%     | ok               |
|          45 | 4.94%    | -14.54%            | -14.22% |     0.25 |       64 | 31.45%     | ok               |
|          40 | -0.16%   | -14.54%            | -18.04% |     0.05 |       78 | 37.10%     | ok               |
|          35 | -1.28%   | -14.54%            | -21.42% |     0.02 |       85 | 42.10%     | ok               |
|          30 | -6.99%   | -14.54%            | -21.35% |    -0.14 |       81 | 48.75%     | ok               |

## PEPE-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -7.44%   | -78.18%            | -64.84% |     0.28 |       80 | 60.15%     | ok               |
|          30 | 0.11%    | -78.18%            | -57.66% |     0.28 |       79 | 44.83%     | ok               |
|          35 | -5.60%   | -78.18%            | -51.35% |     0.2  |       64 | 39.46%     | ok               |
|          25 | -18.07%  | -78.18%            | -53.88% |     0.12 |       85 | 50.00%     | ok               |
|          20 | -27.83%  | -78.18%            | -64.07% |     0.04 |       86 | 56.51%     | ok               |

## PFE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -22.93%  | -13.93%            | -25.61% |    -0.86 |       52 | 18.47%     | ok               |
|          40 | -30.12%  | -13.93%            | -32.57% |    -1.08 |       74 | 23.46%     | ok               |
|          50 | -25.87%  | -13.93%            | -26.71% |    -1.1  |       36 | 14.81%     | ok               |
|          35 | -33.56%  | -13.93%            | -36.37% |    -1.11 |       84 | 30.95%     | ok               |
|          30 | -38.27%  | -13.93%            | -40.87% |    -1.21 |       77 | 35.11%     | ok               |

## PG Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -3.89%   | -5.15%             | -20.08% |    -0.11 |       56 | 34.61%     | ok               |
|          35 | -7.16%   | -5.15%             | -18.99% |    -0.24 |       64 | 38.10%     | ok               |
|          45 | -13.28%  | -5.15%             | -20.75% |    -0.56 |       56 | 32.11%     | ok               |
|          30 | -15.60%  | -5.15%             | -22.27% |    -0.57 |       66 | 41.26%     | ok               |
|          25 | -16.61%  | -5.15%             | -23.16% |    -0.61 |       76 | 42.43%     | ok               |

## PM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | -1.90%   | 107.32%            | -32.20% |     0.05 |       90 | 52.75%     | ok               |
|          20 | -5.09%   | 107.32%            | -31.89% |    -0.01 |       89 | 62.06%     | ok               |
|          30 | -4.86%   | 107.32%            | -33.68% |    -0.01 |       85 | 56.91%     | ok               |
|          50 | -6.95%   | 107.32%            | -35.70% |    -0.09 |       74 | 42.10%     | ok               |
|          40 | -9.29%   | 107.32%            | -37.94% |    -0.14 |       82 | 48.42%     | ok               |

## POL-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 59.25%   | -80.20%            | -46.45% |     0.73 |       79 | 50.19%     | ok               |
|          25 | 62.18%   | -80.20%            | -46.72% |     0.73 |       64 | 58.05%     | ok               |
|          20 | 49.71%   | -80.20%            | -52.88% |     0.64 |       70 | 62.26%     | ok               |
|          15 | 33.60%   | -80.20%            | -58.42% |     0.53 |       72 | 67.05%     | ok               |
|          50 | 14.77%   | -80.20%            | -22.86% |     0.37 |       50 | 20.50%     | ok               |

## QCOM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -2.06%   | 23.50%             | -54.50% |     0.15 |       73 | 48.25%     | ok               |
|          35 | -2.62%   | 23.50%             | -50.58% |     0.13 |       79 | 44.09%     | ok               |
|          20 | -6.04%   | 23.50%             | -54.38% |     0.1  |       69 | 51.08%     | ok               |
|          30 | -13.66%  | 23.50%             | -56.59% |    -0.02 |       75 | 46.59%     | ok               |
|          15 | -21.66%  | 23.50%             | -57.94% |    -0.11 |       73 | 54.24%     | ok               |

## QQQ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | 20.57%   | 65.39%             | -12.88% |     0.57 |       59 | 47.92%     | ok               |
|          15 | 21.09%   | 65.39%             | -14.17% |     0.54 |       63 | 53.41%     | ok               |
|          20 | 17.65%   | 65.39%             | -12.98% |     0.49 |       67 | 50.58%     | ok               |
|          30 | 15.62%   | 65.39%             | -12.88% |     0.47 |       64 | 44.93%     | ok               |
|          35 | 3.80%    | 65.39%             | -19.00% |     0.18 |       70 | 41.26%     | ok               |

## RENDER-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 44.64%   | -61.63%            | -43.43% |     0.61 |       86 | 54.38%     | ok               |
|          15 | 29.39%   | -61.63%            | -44.59% |     0.52 |       86 | 57.57%     | ok               |
|          25 | 15.90%   | -61.63%            | -40.60% |     0.42 |       90 | 50.40%     | ok               |
|          30 | -19.07%  | -61.63%            | -45.00% |     0.1  |       98 | 43.63%     | ok               |
|          35 | -31.74%  | -61.63%            | -41.33% |    -0.12 |       84 | 35.26%     | ok               |

## RTX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 37.11%   | 122.48%            | -18.66% |     0.84 |       76 | 56.07%     | ok               |
|          25 | 32.00%   | 122.48%            | -18.59% |     0.75 |       64 | 52.75%     | ok               |
|          35 | 27.18%   | 122.48%            | -18.00% |     0.74 |       54 | 49.58%     | ok               |
|          50 | 24.89%   | 122.48%            | -18.42% |     0.73 |       58 | 41.60%     | ok               |
|          30 | 29.99%   | 122.48%            | -16.99% |     0.72 |       58 | 51.58%     | ok               |

## SBUX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -15.19%  | 4.94%              | -25.39% |    -0.33 |       68 | 29.62%     | ok               |
|          40 | -17.21%  | 4.94%              | -23.51% |    -0.35 |       60 | 33.94%     | ok               |
|          30 | -21.25%  | 4.94%              | -27.45% |    -0.41 |       64 | 39.43%     | ok               |
|          35 | -22.74%  | 4.94%              | -26.56% |    -0.47 |       58 | 36.77%     | ok               |
|          25 | -28.62%  | 4.94%              | -32.94% |    -0.51 |       64 | 41.93%     | ok               |

## SCHW Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 5.62%    | 58.78%             | -16.53% |     0.23 |       58 | 33.94%     | ok               |
|          50 | 1.49%    | 58.78%             | -13.28% |     0.11 |       54 | 31.45%     | ok               |
|          25 | -4.95%   | 58.78%             | -28.76% |    -0.02 |       65 | 48.75%     | ok               |
|          20 | -6.72%   | 58.78%             | -29.24% |    -0.06 |       73 | 51.41%     | ok               |
|          40 | -5.33%   | 58.78%             | -23.35% |    -0.07 |       66 | 36.94%     | ok               |

## SHIB-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -7.99%   | -75.43%            | -49.21% |     0.16 |       80 | 70.11%     | ok               |
|          20 | -24.50%  | -75.43%            | -48.69% |    -0.04 |       79 | 64.75%     | ok               |
|          25 | -23.79%  | -75.43%            | -43.85% |    -0.05 |       77 | 59.96%     | ok               |
|          35 | -33.97%  | -75.43%            | -55.49% |    -0.28 |       68 | 46.36%     | ok               |
|          30 | -37.08%  | -75.43%            | -48.95% |    -0.29 |       78 | 52.87%     | ok               |

## SHY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd    |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:-------|---------:|---------:|:-----------|:-----------------|
|          30 | -2.24%   | 0.21%              | -2.85% |    -0.79 |       48 | 34.28%     | ok               |
|          35 | -2.36%   | 0.21%              | -3.27% |    -0.84 |       50 | 32.45%     | ok               |
|          40 | -2.47%   | 0.21%              | -3.33% |    -0.89 |       50 | 30.62%     | ok               |
|          45 | -2.45%   | 0.21%              | -3.23% |    -0.9  |       48 | 27.45%     | ok               |
|          50 | -2.62%   | 0.21%              | -3.40% |    -1.01 |       44 | 24.63%     | ok               |

## SKY-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -28.56%  | -4.82%             | -43.98% |    -0.34 |       70 | 40.67%     | ok               |
|          15 | -32.92%  | -4.82%             | -56.39% |    -0.35 |       60 | 50.79%     | ok               |
|          25 | -32.22%  | -4.82%             | -48.09% |    -0.4  |       65 | 44.27%     | ok               |
|          20 | -42.55%  | -4.82%             | -58.40% |    -0.59 |       62 | 47.87%     | ok               |
|          35 | -39.77%  | -4.82%             | -49.68% |    -0.69 |       64 | 34.38%     | ok               |

## SLB Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 23.32%   | -2.89%             | -23.33% |     0.55 |       48 | 36.61%     | ok               |
|          45 | 20.37%   | -2.89%             | -20.73% |     0.51 |       56 | 33.11%     | ok               |
|          50 | -4.32%   | -2.89%             | -30.82% |    -0.02 |       52 | 28.45%     | ok               |
|          35 | -7.64%   | -2.89%             | -42.01% |    -0.05 |       76 | 44.59%     | ok               |
|          30 | -22.01%  | -2.89%             | -54.23% |    -0.35 |       75 | 51.25%     | ok               |

## SLV Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 67.50%   | 171.32%            | -34.10% |     0.86 |       52 | 34.78%     | ok               |
|          45 | 64.85%   | 171.32%            | -31.82% |     0.83 |       56 | 35.61%     | ok               |
|          40 | 62.88%   | 171.32%            | -31.93% |     0.81 |       62 | 37.77%     | ok               |
|          35 | 49.99%   | 171.32%            | -36.89% |     0.7  |       64 | 39.93%     | ok               |
|          30 | 41.28%   | 171.32%            | -42.66% |     0.62 |       58 | 42.10%     | ok               |

## SMH Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 107.50%  | 196.44%            | -30.17% |     1.26 |       47 | 51.91%     | ok               |
|          35 | 85.70%   | 196.44%            | -34.36% |     1.13 |       54 | 47.75%     | ok               |
|          25 | 85.57%   | 196.44%            | -32.94% |     1.11 |       46 | 50.75%     | ok               |
|          30 | 83.38%   | 196.44%            | -33.99% |     1.1  |       48 | 49.08%     | ok               |
|          45 | 70.04%   | 196.44%            | -32.75% |     1.05 |       52 | 41.93%     | ok               |

## SNX-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 13.20%   | -84.71%            | -30.08% |     0.37 |       64 | 30.46%     | ok               |
|          20 | 3.62%    | -84.71%            | -43.20% |     0.31 |       73 | 47.89%     | ok               |
|          30 | -1.63%   | -84.71%            | -34.76% |     0.23 |       60 | 37.36%     | ok               |
|          40 | -12.24%  | -84.71%            | -34.88% |     0.04 |       50 | 24.71%     | ok               |
|          25 | -24.47%  | -84.71%            | -38.84% |    -0.01 |       74 | 41.57%     | ok               |

## SOL-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -2.98%   | -61.98%            | -55.18% |     0.21 |       60 | 37.74%     | ok               |
|          25 | -22.97%  | -61.98%            | -53.21% |     0.02 |       70 | 56.13%     | ok               |
|          15 | -26.23%  | -61.98%            | -59.14% |     0    |       72 | 63.03%     | ok               |
|          35 | -23.30%  | -61.98%            | -61.58% |    -0    |       72 | 45.02%     | ok               |
|          45 | -25.19%  | -61.98%            | -61.94% |    -0.09 |       64 | 32.18%     | ok               |

## SOXX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 86.07%   | 177.16%            | -40.27% |     1.07 |       55 | 50.42%     | ok               |
|          35 | 82.17%   | 177.16%            | -38.63% |     1.05 |       59 | 45.59%     | ok               |
|          25 | 82.51%   | 177.16%            | -41.42% |     1.04 |       53 | 50.08%     | ok               |
|          15 | 81.40%   | 177.16%            | -39.35% |     1    |       68 | 53.24%     | ok               |
|          30 | 72.26%   | 177.16%            | -41.89% |     0.96 |       57 | 47.92%     | ok               |

## SPY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 14.97%   | 49.90%             | -14.25% |     0.53 |       61 | 53.91%     | ok               |
|          15 | 13.40%   | 49.90%             | -16.80% |     0.47 |       70 | 57.07%     | ok               |
|          25 | 7.82%    | 49.90%             | -15.22% |     0.32 |       61 | 52.91%     | ok               |
|          30 | 3.26%    | 49.90%             | -16.47% |     0.17 |       64 | 50.08%     | ok               |
|          35 | 2.65%    | 49.90%             | -16.72% |     0.15 |       60 | 47.09%     | ok               |

## SUSHI-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -23.49%  | -85.55%            | -40.08% |    -0.19 |       52 | 14.75%     | ok               |
|          45 | -58.58%  | -85.55%            | -64.27% |    -0.77 |       56 | 18.20%     | ok               |
|          40 | -61.52%  | -85.55%            | -68.16% |    -0.77 |       63 | 24.71%     | ok               |
|          35 | -69.48%  | -85.55%            | -76.15% |    -0.92 |       80 | 30.27%     | ok               |
|          15 | -80.30%  | -85.55%            | -80.30% |    -1.03 |       89 | 47.13%     | ok               |

## T Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 70.59%   | 22.21%             | -18.13% |     1.31 |       58 | 56.07%     | ok               |
|          25 | 65.29%   | 22.21%             | -17.66% |     1.25 |       60 | 53.91%     | ok               |
|          15 | 61.27%   | 22.21%             | -15.08% |     1.15 |       67 | 59.90%     | ok               |
|          30 | 47.19%   | 22.21%             | -17.01% |     1.01 |       64 | 51.91%     | ok               |
|          35 | 32.05%   | 22.21%             | -14.49% |     0.78 |       66 | 48.42%     | ok               |

## TGT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -12.32%  | -13.94%            | -42.86% |    -0.13 |       81 | 46.76%     | ok               |
|          45 | -10.91%  | -13.94%            | -29.07% |    -0.18 |       52 | 29.12%     | ok               |
|          25 | -13.19%  | -13.94%            | -43.36% |    -0.18 |       63 | 41.76%     | ok               |
|          30 | -12.57%  | -13.94%            | -40.57% |    -0.18 |       58 | 38.94%     | ok               |
|          15 | -17.84%  | -13.94%            | -40.77% |    -0.24 |       71 | 51.41%     | ok               |

## TIA-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 2.90%    | -90.43%            | -46.58% |     0.22 |       52 | 18.58%     | ok               |
|          50 | 1.89%    | -90.43%            | -46.02% |     0.18 |       32 | 11.49%     | ok               |
|          35 | -14.76%  | -90.43%            | -49.70% |     0.07 |       66 | 30.84%     | ok               |
|          40 | -14.40%  | -90.43%            | -48.55% |     0.06 |       68 | 26.05%     | ok               |
|          15 | -57.93%  | -90.43%            | -61.13% |    -0.35 |       97 | 52.49%     | ok               |

## TLT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -21.65%  | -8.95%             | -21.82% |    -1.69 |       70 | 31.45%     | ok               |
|          50 | -15.00%  | -8.95%             | -15.73% |    -1.79 |       32 | 14.14%     | ok               |
|          15 | -27.39%  | -8.95%             | -27.71% |    -1.94 |       75 | 39.43%     | ok               |
|          40 | -20.03%  | -8.95%             | -20.03% |    -1.95 |       58 | 20.80%     | ok               |
|          35 | -22.42%  | -8.95%             | -22.42% |    -1.99 |       64 | 25.62%     | ok               |

## TMO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 44.01%   | -6.02%             | -8.17%  |     1.01 |       40 | 30.78%     | ok               |
|          45 | 39.83%   | -6.02%             | -10.13% |     0.89 |       46 | 35.61%     | ok               |
|          40 | 37.77%   | -6.02%             | -9.91%  |     0.83 |       49 | 40.10%     | ok               |
|          35 | 20.23%   | -6.02%             | -14.06% |     0.5  |       61 | 44.59%     | ok               |
|          30 | 14.84%   | -6.02%             | -18.85% |     0.39 |       61 | 49.75%     | ok               |

## TMUS Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 11.24%   | 12.08%             | -27.64% |     0.32 |       69 | 60.23%     | ok               |
|          30 | 10.03%   | 12.08%             | -24.50% |     0.3  |       70 | 48.25%     | ok               |
|          20 | 2.25%    | 12.08%             | -28.59% |     0.15 |       73 | 54.41%     | ok               |
|          25 | 1.34%    | 12.08%             | -29.74% |     0.13 |       75 | 50.75%     | ok               |
|          35 | -2.27%   | 12.08%             | -32.59% |     0.05 |       68 | 44.93%     | ok               |

## TRX-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 6.87%    | 34.96%             | -18.79% |     0.28 |       52 | 37.16%     | ok               |
|          30 | 0.99%    | 34.96%             | -22.90% |     0.12 |       72 | 49.04%     | ok               |
|          50 | 0.66%    | 34.96%             | -18.49% |     0.1  |       44 | 31.99%     | ok               |
|          35 | 0.16%    | 34.96%             | -21.77% |     0.09 |       68 | 45.79%     | ok               |
|          45 | -0.23%   | 34.96%             | -18.27% |     0.07 |       44 | 33.52%     | ok               |

## TSLA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 65.00%   | 116.86%            | -34.12% |     0.76 |       62 | 35.11%     | ok               |
|          50 | 42.79%   | 116.86%            | -35.95% |     0.61 |       64 | 30.62%     | ok               |
|          45 | 39.78%   | 116.86%            | -35.28% |     0.58 |       66 | 32.45%     | ok               |
|          35 | 40.90%   | 116.86%            | -35.12% |     0.57 |       67 | 37.27%     | ok               |
|          30 | 12.31%   | 116.86%            | -42.22% |     0.32 |       69 | 41.26%     | ok               |

## TXN Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 16.62%   | 86.88%             | -45.45% |     0.38 |       68 | 35.27%     | ok               |
|          20 | 2.52%    | 86.88%             | -38.49% |     0.19 |       62 | 60.07%     | ok               |
|          35 | -0.29%   | 86.88%             | -43.28% |     0.13 |       76 | 50.58%     | ok               |
|          15 | -3.33%   | 86.88%             | -38.99% |     0.11 |       67 | 63.89%     | ok               |
|          40 | -2.35%   | 86.88%             | -45.67% |     0.1  |       70 | 48.09%     | ok               |

## UNH Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 31.11%   | -19.34%            | -37.02% |     0.56 |       52 | 30.78%     | ok               |
|          30 | 28.09%   | -19.34%            | -27.86% |     0.5  |       74 | 52.58%     | ok               |
|          35 | 24.60%   | -19.34%            | -29.20% |     0.46 |       66 | 47.42%     | ok               |
|          15 | 24.50%   | -19.34%            | -33.62% |     0.45 |       74 | 67.39%     | ok               |
|          40 | 20.02%   | -19.34%            | -35.94% |     0.41 |       60 | 42.60%     | ok               |

## UNI-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -29.92%  | -71.16%            | -58.49% |    -0.16 |       56 | 26.05%     | ok               |
|          40 | -35.32%  | -71.16%            | -63.75% |    -0.22 |       62 | 31.42%     | ok               |
|          50 | -36.00%  | -71.16%            | -57.60% |    -0.3  |       54 | 21.26%     | ok               |
|          35 | -46.30%  | -71.16%            | -68.71% |    -0.34 |       74 | 36.78%     | ok               |
|          20 | -77.21%  | -71.16%            | -82.90% |    -0.87 |      104 | 53.45%     | ok               |

## UPS Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -33.09%  | -24.78%            | -43.08% |    -0.6  |       82 | 48.75%     | ok               |
|          25 | -34.16%  | -24.78%            | -39.39% |    -0.64 |       78 | 45.26%     | ok               |
|          15 | -37.16%  | -24.78%            | -45.34% |    -0.69 |       90 | 53.58%     | ok               |
|          35 | -35.48%  | -24.78%            | -40.47% |    -0.72 |       67 | 34.44%     | ok               |
|          30 | -38.23%  | -24.78%            | -40.45% |    -0.78 |       72 | 40.27%     | ok               |

## USO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 13.16%   | 45.60%             | -33.25% |     0.33 |       50 | 26.46%     | ok               |
|          15 | 8.74%    | 45.60%             | -45.09% |     0.26 |       72 | 42.43%     | ok               |
|          30 | 7.40%    | 45.60%             | -43.35% |     0.24 |       68 | 34.11%     | ok               |
|          20 | 5.92%    | 45.60%             | -44.92% |     0.22 |       75 | 39.60%     | ok               |
|          25 | 4.53%    | 45.60%             | -44.86% |     0.2  |       69 | 37.10%     | ok               |

## VEA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 5.44%    | 50.90%             | -16.28% |     0.25 |       60 | 50.58%     | ok               |
|          20 | 1.19%    | 50.90%             | -17.70% |     0.1  |       61 | 47.92%     | ok               |
|          25 | -0.82%   | 50.90%             | -17.79% |     0.02 |       57 | 46.26%     | ok               |
|          30 | -0.98%   | 50.90%             | -17.93% |     0.01 |       58 | 44.09%     | ok               |
|          35 | -2.09%   | 50.90%             | -16.79% |    -0.03 |       56 | 43.09%     | ok               |

## VIXY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -46.17%  | -63.13%            | -68.69% |    -0.39 |       44 | 10.32%     | ok               |
|          45 | -56.13%  | -63.13%            | -74.13% |    -0.55 |       56 | 16.31%     | ok               |
|          40 | -64.45%  | -63.13%            | -80.03% |    -0.66 |       70 | 20.63%     | ok               |
|          35 | -68.17%  | -63.13%            | -83.81% |    -0.7  |       86 | 25.79%     | ok               |
|          15 | -77.76%  | -63.13%            | -89.47% |    -0.79 |      103 | 44.43%     | ok               |

## VNQ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -8.60%   | 15.24%             | -19.07% |    -0.37 |       60 | 28.62%     | ok               |
|          50 | -9.03%   | 15.24%             | -17.13% |    -0.41 |       56 | 26.12%     | ok               |
|          25 | -12.92%  | 15.24%             | -22.16% |    -0.5  |       68 | 40.93%     | ok               |
|          40 | -14.13%  | 15.24%             | -24.84% |    -0.62 |       74 | 32.11%     | ok               |
|          20 | -16.33%  | 15.24%             | -23.61% |    -0.63 |       73 | 43.76%     | ok               |

## VTI Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 18.51%   | 49.33%             | -13.96% |     0.62 |       64 | 54.91%     | ok               |
|          15 | 12.44%   | 49.33%             | -15.70% |     0.44 |       67 | 57.40%     | ok               |
|          25 | 4.81%    | 49.33%             | -16.10% |     0.22 |       60 | 52.91%     | ok               |
|          30 | -2.51%   | 49.33%             | -18.77% |    -0.03 |       70 | 50.92%     | ok               |
|          35 | -4.96%   | 49.33%             | -21.19% |    -0.13 |       64 | 47.75%     | ok               |

## VWO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -7.30%   | 47.85%             | -21.18% |    -0.25 |       60 | 32.61%     | ok               |
|          15 | -9.03%   | 47.85%             | -24.01% |    -0.26 |       69 | 49.42%     | ok               |
|          20 | -10.06%  | 47.85%             | -26.14% |    -0.31 |       67 | 47.25%     | ok               |
|          40 | -8.98%   | 47.85%             | -23.57% |    -0.31 |       70 | 37.94%     | ok               |
|          45 | -9.11%   | 47.85%             | -23.26% |    -0.33 |       62 | 35.11%     | ok               |

## VZ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -6.80%   | 5.92%              | -12.71% |    -0.19 |       50 | 24.29%     | ok               |
|          45 | -16.37%  | 5.92%              | -19.45% |    -0.53 |       60 | 27.45%     | ok               |
|          25 | -20.77%  | 5.92%              | -24.92% |    -0.59 |       83 | 41.26%     | ok               |
|          35 | -18.70%  | 5.92%              | -19.89% |    -0.6  |       63 | 33.11%     | ok               |
|          40 | -22.50%  | 5.92%              | -23.39% |    -0.77 |       66 | 30.28%     | ok               |

## WFC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 0.30%    | 81.96%             | -18.29% |     0.08 |       60 | 34.44%     | ok               |
|          35 | -5.05%   | 81.96%             | -22.53% |    -0.03 |       81 | 46.26%     | ok               |
|          20 | -13.34%  | 81.96%             | -29.96% |    -0.16 |       79 | 55.74%     | ok               |
|          45 | -8.03%   | 81.96%             | -24.02% |    -0.16 |       68 | 39.27%     | ok               |
|          30 | -15.11%  | 81.96%             | -29.91% |    -0.23 |       86 | 49.58%     | ok               |

## WIF-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 60.65%   | -83.38%            | -46.21% |     0.66 |       71 | 41.38%     | ok               |
|          20 | 54.98%   | -83.38%            | -40.67% |     0.64 |       65 | 38.70%     | ok               |
|          25 | 2.09%    | -83.38%            | -45.19% |     0.31 |       67 | 36.02%     | ok               |
|          30 | -35.28%  | -83.38%            | -50.54% |    -0.13 |       68 | 31.99%     | ok               |
|          50 | -21.97%  | -83.38%            | -38.87% |    -0.18 |       40 | 11.88%     | ok               |

## WMT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 58.65%   | 96.10%             | -9.18%  |     1.53 |       38 | 42.60%     | ok               |
|          50 | 52.21%   | 96.10%             | -12.19% |     1.46 |       32 | 40.43%     | ok               |
|          40 | 48.73%   | 96.10%             | -9.18%  |     1.29 |       42 | 43.76%     | ok               |
|          35 | 45.93%   | 96.10%             | -10.48% |     1.2  |       54 | 47.92%     | ok               |
|          30 | 21.43%   | 96.10%             | -21.31% |     0.61 |       61 | 50.58%     | ok               |

## XBI Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 10.44%   | 76.64%             | -16.56% |     0.33 |       62 | 35.77%     | ok               |
|          45 | 9.59%    | 76.64%             | -16.74% |     0.32 |       54 | 32.61%     | ok               |
|          35 | 5.87%    | 76.64%             | -21.24% |     0.22 |       62 | 39.10%     | ok               |
|          30 | 4.70%    | 76.64%             | -21.61% |     0.2  |       62 | 40.77%     | ok               |
|          50 | 0.60%    | 76.64%             | -16.83% |     0.09 |       56 | 29.28%     | ok               |

## XLB Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -1.68%   | 25.04%             | -20.68% |    -0.01 |       54 | 31.61%     | ok               |
|          50 | -1.74%   | 25.04%             | -17.59% |    -0.02 |       42 | 27.29%     | ok               |
|          35 | -4.92%   | 25.04%             | -23.62% |    -0.13 |       56 | 34.94%     | ok               |
|          45 | -4.65%   | 25.04%             | -20.79% |    -0.14 |       42 | 28.79%     | ok               |
|          25 | -6.87%   | 25.04%             | -22.63% |    -0.19 |       60 | 40.27%     | ok               |

## XLC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 12.45%   | 39.21%             | -12.33% |     0.45 |       67 | 55.24%     | ok               |
|          25 | 10.33%   | 39.21%             | -12.31% |     0.39 |       64 | 57.07%     | ok               |
|          40 | 7.46%    | 39.21%             | -13.38% |     0.32 |       68 | 47.75%     | ok               |
|          35 | 7.44%    | 39.21%             | -13.38% |     0.31 |       64 | 52.25%     | ok               |
|          20 | 2.77%    | 39.21%             | -13.37% |     0.15 |       70 | 59.90%     | ok               |

## XLE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -0.30%   | 27.55%             | -25.98% |     0.06 |       54 | 36.44%     | ok               |
|          35 | -4.12%   | 27.55%             | -32.75% |    -0.02 |       67 | 44.09%     | ok               |
|          45 | -5.44%   | 27.55%             | -31.48% |    -0.08 |       62 | 39.10%     | ok               |
|          25 | -10.39%  | 27.55%             | -37.15% |    -0.18 |       79 | 49.42%     | ok               |
|          30 | -10.91%  | 27.55%             | -37.51% |    -0.21 |       73 | 46.42%     | ok               |

## XLF Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -2.01%   | 43.65%             | -18.01% |    -0    |       68 | 53.91%     | ok               |
|          15 | -6.06%   | 43.65%             | -19.58% |    -0.14 |       76 | 56.74%     | ok               |
|          25 | -8.84%   | 43.65%             | -23.22% |    -0.26 |       77 | 50.42%     | ok               |
|          30 | -9.28%   | 43.65%             | -23.61% |    -0.29 |       78 | 48.09%     | ok               |
|          35 | -16.57%  | 43.65%             | -27.24% |    -0.64 |       68 | 43.93%     | ok               |

## XLI Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 9.44%    | 58.67%             | -10.36% |     0.38 |       74 | 52.25%     | ok               |
|          50 | 5.82%    | 58.67%             | -9.25%  |     0.31 |       58 | 33.44%     | ok               |
|          45 | 4.85%    | 58.67%             | -12.27% |     0.26 |       64 | 35.61%     | ok               |
|          20 | 5.21%    | 58.67%             | -12.74% |     0.25 |       65 | 47.25%     | ok               |
|          30 | 4.62%    | 58.67%             | -10.77% |     0.23 |       64 | 44.59%     | ok               |

## XLK Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 79.40%   | 76.65%             | -14.75% |     1.29 |       41 | 52.08%     | ok               |
|          20 | 65.37%   | 76.65%             | -14.75% |     1.15 |       48 | 49.92%     | ok               |
|          25 | 62.00%   | 76.65%             | -14.75% |     1.15 |       42 | 47.75%     | ok               |
|          30 | 59.88%   | 76.65%             | -14.75% |     1.14 |       42 | 46.59%     | ok               |
|          35 | 42.04%   | 76.65%             | -13.61% |     0.9  |       54 | 43.93%     | ok               |

## XLM-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 27.47%   | -50.11%            | -38.97% |     0.49 |       44 | 27.20%     | ok               |
|          45 | 23.64%   | -50.11%            | -43.99% |     0.45 |       50 | 30.84%     | ok               |
|          30 | 5.21%    | -50.11%            | -50.36% |     0.28 |       69 | 45.79%     | ok               |
|          40 | 2.83%    | -50.11%            | -43.80% |     0.24 |       49 | 35.25%     | ok               |
|          35 | -4.00%   | -50.11%            | -50.42% |     0.17 |       69 | 41.76%     | ok               |

## XLP Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 11.69%   | 15.03%             | -5.66%  |     0.71 |       54 | 34.28%     | ok               |
|          50 | 9.69%    | 15.03%             | -6.08%  |     0.61 |       58 | 31.78%     | ok               |
|          40 | 9.44%    | 15.03%             | -7.77%  |     0.57 |       70 | 38.44%     | ok               |
|          35 | 8.49%    | 15.03%             | -9.73%  |     0.51 |       66 | 41.43%     | ok               |
|          30 | 6.56%    | 15.03%             | -11.16% |     0.4  |       68 | 42.93%     | ok               |

## XLU Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 6.79%    | 50.32%             | -12.19% |     0.37 |       50 | 30.28%     | ok               |
|          45 | 4.66%    | 50.32%             | -13.95% |     0.27 |       54 | 31.11%     | ok               |
|          40 | 1.78%    | 50.32%             | -15.27% |     0.13 |       58 | 32.61%     | ok               |
|          35 | -6.96%   | 50.32%             | -19.41% |    -0.29 |       66 | 35.11%     | ok               |
|          30 | -8.34%   | 50.32%             | -20.40% |    -0.34 |       71 | 38.44%     | ok               |

## XLV Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -12.12%  | 12.46%             | -16.83% |    -0.59 |       66 | 35.61%     | ok               |
|          25 | -13.41%  | 12.46%             | -18.06% |    -0.66 |       68 | 36.94%     | ok               |
|          15 | -17.34%  | 12.46%             | -21.47% |    -0.84 |       79 | 41.76%     | ok               |
|          20 | -17.27%  | 12.46%             | -21.56% |    -0.86 |       73 | 38.60%     | ok               |
|          50 | -14.45%  | 12.46%             | -18.24% |    -0.87 |       54 | 24.29%     | ok               |

## XLY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 4.62%    | 31.20%             | -12.94% |     0.21 |       72 | 41.26%     | ok               |
|          30 | 2.75%    | 31.20%             | -14.01% |     0.15 |       72 | 44.26%     | ok               |
|          15 | 1.20%    | 31.20%             | -15.77% |     0.11 |       74 | 51.25%     | ok               |
|          50 | -0.91%   | 31.20%             | -13.71% |     0.02 |       50 | 29.78%     | ok               |
|          40 | -1.91%   | 31.20%             | -16.99% |    -0.01 |       68 | 37.10%     | ok               |

## XOM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | 6.12%    | 34.07%             | -19.90% |     0.24 |       58 | 37.60%     | ok               |
|          30 | 5.06%    | 34.07%             | -20.29% |     0.22 |       58 | 36.94%     | ok               |
|          50 | 2.44%    | 34.07%             | -21.35% |     0.14 |       44 | 29.62%     | ok               |
|          20 | 2.19%    | 34.07%             | -25.56% |     0.14 |       63 | 40.10%     | ok               |
|          35 | 0.65%    | 34.07%             | -20.93% |     0.09 |       58 | 35.77%     | ok               |

## XRP-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | -25.11%  | -60.82%            | -46.87% |    -0.14 |       68 | 39.85%     | ok               |
|          40 | -30.47%  | -60.82%            | -44.89% |    -0.26 |       58 | 33.72%     | ok               |
|          30 | -37.23%  | -60.82%            | -54.70% |    -0.33 |       70 | 44.06%     | ok               |
|          45 | -38.24%  | -60.82%            | -46.06% |    -0.42 |       58 | 29.50%     | ok               |
|          50 | -34.88%  | -60.82%            | -38.03% |    -0.46 |       60 | 22.03%     | ok               |

## YFI-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -33.86%  | -63.18%            | -50.17% |    -0.47 |       60 | 27.01%     | ok               |
|          45 | -32.67%  | -63.18%            | -51.92% |    -0.53 |       60 | 22.22%     | ok               |
|          35 | -52.65%  | -63.18%            | -64.34% |    -0.82 |       71 | 34.29%     | ok               |
|          30 | -55.71%  | -63.18%            | -67.78% |    -0.83 |       83 | 40.42%     | ok               |
|          50 | -41.48%  | -63.18%            | -51.80% |    -0.84 |       52 | 17.43%     | ok               |

## ZEC-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 122.12%  | 1040.67%           | -24.66% |     0.89 |       46 | 22.61%     | ok               |
|          35 | 90.71%   | 1040.67%           | -44.34% |     0.76 |       54 | 29.12%     | ok               |
|          25 | 69.79%   | 1040.67%           | -48.59% |     0.67 |       60 | 38.31%     | ok               |
|          30 | 52.99%   | 1040.67%           | -47.68% |     0.6  |       64 | 34.87%     | ok               |
|          50 | 52.69%   | 1040.67%           | -34.39% |     0.59 |       48 | 20.11%     | ok               |
