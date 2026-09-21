# Market Tracker Backtest Report

_Generated: 2026-09-21T05:01:28+00:00_

## Data Sources

- Crypto: Kraken -> Coinbase -> CoinGecko OHLC -> CoinPaprika fallback chain.
- Stocks / ETFs / indices: Stooq -> Yahoo Finance fallback chain.
- Data rows are generated from real market APIs. Mock OHLCV rows are not generated.

## Data Freshness

- Rows: **92,697**
- Symbols: **161**
- Date range: **2024-04-26** to **2026-09-21**

## Latest Signals

| symbol     | date                |         close |   composite_score | signal   | data_source   |
|:-----------|:--------------------|--------------:|------------------:|:---------|:--------------|
| AAPL       | 2026-09-18 00:00:00 |   336.13      |        75.9167    | LONG     | Yahoo Finance |
| AMD        | 2026-09-18 00:00:00 |   559.82      |        74.75      | LONG     | Yahoo Finance |
| APT-USD    | 2026-09-21 00:00:00 |     0.7442    |        50.3333    | LONG     | Kraken API    |
| ARB-USD    | 2026-09-21 00:00:00 |     0.2178    |        63.8333    | LONG     | Kraken API    |
| ATOM-USD   | 2026-09-21 00:00:00 |     1.7662    |        43.6667    | LONG     | Kraken API    |
| AVAX-USD   | 2026-09-21 00:00:00 |    11.524     |        71.25      | LONG     | Kraken API    |
| BITO       | 2026-09-18 00:00:00 |    10.92      |        33         | LONG     | Yahoo Finance |
| BTC-USD    | 2026-09-21 00:00:00 | 81377.3       |        61.0833    | LONG     | Kraken API    |
| CVX        | 2026-09-18 00:00:00 |   209.51      |        49.8333    | LONG     | Yahoo Finance |
| DASH-USD   | 2026-09-21 00:00:00 |    57.383     |        30.4167    | LONG     | Kraken API    |
| DBC        | 2026-09-18 00:00:00 |    32.93      |        73.5833    | LONG     | Yahoo Finance |
| DE         | 2026-09-18 00:00:00 |   683.99      |        54         | LONG     | Yahoo Finance |
| DOT-USD    | 2026-09-21 00:00:00 |     1.1547    |        43.6667    | LONG     | Kraken API    |
| DXY-INDEX  | 2026-09-21 00:00:00 |   100.301     |        76.3441    | LONG     | Yahoo Finance |
| ETC-USD    | 2026-09-21 00:00:00 |     8.502     |        71.1667    | LONG     | Kraken API    |
| ETH-USD    | 2026-09-21 00:00:00 |  2661.72      |        69.6667    | LONG     | Kraken API    |
| FIL-USD    | 2026-09-21 00:00:00 |     0.955     |        63.8333    | LONG     | Kraken API    |
| GRT-USD    | 2026-09-21 00:00:00 |     0.02258   |        50.3333    | LONG     | Kraken API    |
| IBIT       | 2026-09-18 00:00:00 |    46.02      |        56.25      | LONG     | Yahoo Finance |
| ICP-USD    | 2026-09-21 00:00:00 |     2.972     |        55         | LONG     | Kraken API    |
| INJ-USD    | 2026-09-21 00:00:00 |     7.669     |        65.1667    | LONG     | Kraken API    |
| INTC       | 2026-09-18 00:00:00 |   108.6       |        74.75      | LONG     | Yahoo Finance |
| LDO-USD    | 2026-09-21 00:00:00 |     0.432     |        70.0833    | LONG     | Kraken API    |
| LTC-USD    | 2026-09-21 00:00:00 |    58.7       |        71.8333    | LONG     | Kraken API    |
| META       | 2026-09-18 00:00:00 |   665.75      |        55.5833    | LONG     | Yahoo Finance |
| MPC        | 2026-09-18 00:00:00 |   424.89      |        78.75      | LONG     | Yahoo Finance |
| MRK        | 2026-09-18 00:00:00 |   146.87      |        38.3333    | LONG     | Yahoo Finance |
| MSFT       | 2026-09-18 00:00:00 |   493.78      |        34.6667    | LONG     | Yahoo Finance |
| NEAR-USD   | 2026-09-21 00:00:00 |     4.4168    |        67.25      | LONG     | Kraken API    |
| NOW        | 2026-09-18 00:00:00 |   135.47      |        41.4167    | LONG     | Yahoo Finance |
| POL-USD    | 2026-09-21 00:00:00 |     0.10976   |        74.8333    | LONG     | Kraken API    |
| QCOM       | 2026-09-18 00:00:00 |   177.72      |        79.6667    | LONG     | Yahoo Finance |
| SUSHI-USD  | 2026-09-21 00:00:00 |     0.2527    |        63.3333    | LONG     | Kraken API    |
| TXN        | 2026-09-18 00:00:00 |   266.64      |        57.1667    | LONG     | Yahoo Finance |
| UNI-USD    | 2026-09-21 00:00:00 |     8.84      |        63.8333    | LONG     | Kraken API    |
| USO        | 2026-09-18 00:00:00 |   153.82      |        69.0833    | LONG     | Yahoo Finance |
| XLM-USD    | 2026-09-21 00:00:00 |     0.198125  |        73.1667    | LONG     | Kraken API    |
| ZEC-USD    | 2026-09-21 00:00:00 |  1526.18      |        63.8333    | LONG     | Kraken API    |
| AAVE-USD   | 2026-09-21 00:00:00 |   138.93      |        59.0833    | NEUTRAL  | Kraken API    |
| ABBV       | 2026-09-18 00:00:00 |   263.96      |        57.3333    | NEUTRAL  | Yahoo Finance |
| ADA-USD    | 2026-09-21 00:00:00 |     0.232068  |        32.0833    | NEUTRAL  | Kraken API    |
| ALGO-USD   | 2026-09-21 00:00:00 |     0.10969   |        63.6667    | NEUTRAL  | Kraken API    |
| AMAT       | 2026-09-18 00:00:00 |   444.57      |         8.16667   | NEUTRAL  | Yahoo Finance |
| AMGN       | 2026-09-18 00:00:00 |   385.65      |       -18.0833    | NEUTRAL  | Yahoo Finance |
| AMZN       | 2026-09-18 00:00:00 |   253.71      |       -27.75      | NEUTRAL  | Yahoo Finance |
| ARKK       | 2026-09-18 00:00:00 |    88.23      |        48.3333    | NEUTRAL  | Yahoo Finance |
| BAC        | 2026-09-18 00:00:00 |    57.73      |       -16.8333    | NEUTRAL  | Yahoo Finance |
| BCH-USD    | 2026-09-21 00:00:00 |   254.66      |         9.25      | NEUTRAL  | Kraken API    |
| BLK        | 2026-09-18 00:00:00 |  1069.78      |       -14.4167    | NEUTRAL  | Yahoo Finance |
| BONK-USD   | 2026-09-21 00:00:00 |     3.049e-06 |        12.6667    | NEUTRAL  | Kraken API    |
| C          | 2026-09-18 00:00:00 |   131.77      |       -25.25      | NEUTRAL  | Yahoo Finance |
| CAT        | 2026-09-18 00:00:00 |   808.99      |        19.9167    | NEUTRAL  | Yahoo Finance |
| CL         | 2026-09-18 00:00:00 |    87.47      |       -51.1667    | NEUTRAL  | Yahoo Finance |
| COMP-USD   | 2026-09-21 00:00:00 |    22.2       |        61.5833    | NEUTRAL  | Kraken API    |
| COP        | 2026-09-18 00:00:00 |   131.83      |        17.5833    | NEUTRAL  | Yahoo Finance |
| CRM        | 2026-09-18 00:00:00 |   237.92      |        13.9167    | NEUTRAL  | Yahoo Finance |
| CRV-USD    | 2026-09-21 00:00:00 |     0.34611   |        22.8333    | NEUTRAL  | Kraken API    |
| CSCO       | 2026-09-18 00:00:00 |   109.51      |        17.25      | NEUTRAL  | Yahoo Finance |
| DIA        | 2026-09-18 00:00:00 |   515.88      |       -15.75      | NEUTRAL  | Yahoo Finance |
| DIS        | 2026-09-18 00:00:00 |   102.67      |       -38.3333    | NEUTRAL  | Yahoo Finance |
| DOGE-USD   | 2026-09-21 00:00:00 |     0.0883206 |        22.4167    | NEUTRAL  | Kraken API    |
| EEM        | 2026-09-18 00:00:00 |    67.03      |        28.8333    | NEUTRAL  | Yahoo Finance |
| EFA        | 2026-09-18 00:00:00 |   104.97      |       -43.0833    | NEUTRAL  | Yahoo Finance |
| EOG        | 2026-09-18 00:00:00 |   144.23      |        10.25      | NEUTRAL  | Yahoo Finance |
| EWJ        | 2026-09-18 00:00:00 |    97         |        46.3333    | NEUTRAL  | Yahoo Finance |
| FCX        | 2026-09-18 00:00:00 |    71.54      |         2.58333   | NEUTRAL  | Yahoo Finance |
| FET-USD    | 2026-09-21 00:00:00 |     0.1831    |        26         | NEUTRAL  | Kraken API    |
| FXI        | 2026-09-18 00:00:00 |    34.32      |       -61.1667    | NEUTRAL  | Yahoo Finance |
| GDX        | 2026-09-18 00:00:00 |    95.48      |         0.0833333 | NEUTRAL  | Yahoo Finance |
| GDXJ       | 2026-09-18 00:00:00 |   124.44      |        20.0833    | NEUTRAL  | Yahoo Finance |
| GLD        | 2026-09-18 00:00:00 |   401.17      |         4.66667   | NEUTRAL  | Yahoo Finance |
| GOOGL      | 2026-09-18 00:00:00 |   349.54      |        54.4167    | NEUTRAL  | Yahoo Finance |
| HBAR-USD   | 2026-09-21 00:00:00 |     0.08728   |        71.0833    | NEUTRAL  | Kraken API    |
| IBM        | 2026-09-18 00:00:00 |   229.55      |       -51.0833    | NEUTRAL  | Yahoo Finance |
| IEMG       | 2026-09-18 00:00:00 |    81.66      |        28.8333    | NEUTRAL  | Yahoo Finance |
| INTU       | 2026-09-18 00:00:00 |   303.19      |       -70.0833    | NEUTRAL  | Yahoo Finance |
| IWM        | 2026-09-18 00:00:00 |   284.1       |       -19.1667    | NEUTRAL  | Yahoo Finance |
| JNJ        | 2026-09-18 00:00:00 |   269.99      |        17.75      | NEUTRAL  | Yahoo Finance |
| JPM        | 2026-09-18 00:00:00 |   349.67      |        -6.58333   | NEUTRAL  | Yahoo Finance |
| KO         | 2026-09-18 00:00:00 |    88.25      |         0.0833333 | NEUTRAL  | Yahoo Finance |
| LINK-USD   | 2026-09-21 00:00:00 |    12.6683    |        39.9167    | NEUTRAL  | Kraken API    |
| LRCX       | 2026-09-18 00:00:00 |   288.11      |       -11.0833    | NEUTRAL  | Yahoo Finance |
| MS         | 2026-09-18 00:00:00 |   202.58      |       -19         | NEUTRAL  | Yahoo Finance |
| MU         | 2026-09-18 00:00:00 |  1015.8       |        66.1667    | NEUTRAL  | Yahoo Finance |
| NEM        | 2026-09-18 00:00:00 |   123.41      |       -12.9167    | NEUTRAL  | Yahoo Finance |
| NFLX       | 2026-09-18 00:00:00 |    71.79      |       -52.0833    | NEUTRAL  | Yahoo Finance |
| NVDA       | 2026-09-18 00:00:00 |   222.27      |        50         | NEUTRAL  | Yahoo Finance |
| OP-USD     | 2026-09-21 00:00:00 |     0.1278    |        39.0833    | NEUTRAL  | Kraken API    |
| ORCL       | 2026-09-18 00:00:00 |   147.61      |       -32.6667    | NEUTRAL  | Yahoo Finance |
| OXY        | 2026-09-18 00:00:00 |    58.84      |        10.9167    | NEUTRAL  | Yahoo Finance |
| PEPE-USD   | 2026-09-21 00:00:00 |     4.016e-06 |        61.5833    | NEUTRAL  | Kraken API    |
| PFE        | 2026-09-18 00:00:00 |    27.66      |         0.333333  | NEUTRAL  | Yahoo Finance |
| PG         | 2026-09-18 00:00:00 |   146.39      |        33.9167    | NEUTRAL  | Yahoo Finance |
| PM         | 2026-09-18 00:00:00 |   188.62      |        22         | NEUTRAL  | Yahoo Finance |
| QQQ        | 2026-09-18 00:00:00 |   721.45      |        67.8333    | NEUTRAL  | Yahoo Finance |
| RENDER-USD | 2026-09-21 00:00:00 |     1.727     |        63.3333    | NEUTRAL  | Kraken API    |
| SCHW       | 2026-09-18 00:00:00 |   105.25      |       -15         | NEUTRAL  | Yahoo Finance |
| SHIB-USD   | 2026-09-21 00:00:00 |     5.547e-06 |        34.0833    | NEUTRAL  | Kraken API    |
| SKY-USD    | 2026-09-21 00:00:00 |     0.07051   |        31.5833    | NEUTRAL  | Kraken API    |
| SLB        | 2026-09-18 00:00:00 |    51.12      |       -24.75      | NEUTRAL  | Yahoo Finance |
| SLV        | 2026-09-18 00:00:00 |    59.93      |        16.8333    | NEUTRAL  | Yahoo Finance |
| SMH        | 2026-09-18 00:00:00 |   573         |        56.6667    | NEUTRAL  | Yahoo Finance |
| SNX-USD    | 2026-09-21 00:00:00 |     0.229     |        43.0833    | NEUTRAL  | Kraken API    |
| SOL-USD    | 2026-09-21 00:00:00 |   111.45      |        61.0833    | NEUTRAL  | Kraken API    |
| SOXX       | 2026-09-18 00:00:00 |   533.07      |        56.6667    | NEUTRAL  | Yahoo Finance |
| SPY        | 2026-09-18 00:00:00 |   761.69      |        -6.58333   | NEUTRAL  | Yahoo Finance |
| T          | 2026-09-18 00:00:00 |    25.4       |        -3.33333   | NEUTRAL  | Yahoo Finance |
| TGT        | 2026-09-18 00:00:00 |   158.19      |        16.3333    | NEUTRAL  | Yahoo Finance |
| TIA-USD    | 2026-09-21 00:00:00 |     0.4302    |        18.0833    | NEUTRAL  | Kraken API    |
| TLT        | 2026-09-18 00:00:00 |    81.25      |       -59.3333    | NEUTRAL  | Yahoo Finance |
| TMO        | 2026-09-18 00:00:00 |   651.45      |        61         | NEUTRAL  | Yahoo Finance |
| TMUS       | 2026-09-18 00:00:00 |   168.18      |       -57.25      | NEUTRAL  | Yahoo Finance |
| TRX-USD    | 2026-09-21 00:00:00 |     0.342877  |        57.8333    | NEUTRAL  | Kraken API    |
| TSLA       | 2026-09-18 00:00:00 |   364.27      |        25.8333    | NEUTRAL  | Yahoo Finance |
| UNH        | 2026-09-18 00:00:00 |   376.9       |       -11.5833    | NEUTRAL  | Yahoo Finance |
| UPS        | 2026-09-18 00:00:00 |    99.06      |       -69.25      | NEUTRAL  | Yahoo Finance |
| VEA        | 2026-09-18 00:00:00 |    71.38      |       -32.3333    | NEUTRAL  | Yahoo Finance |
| VIXY       | 2026-09-18 00:00:00 |    17.09      |       -15.5       | NEUTRAL  | Yahoo Finance |
| VTI        | 2026-09-18 00:00:00 |   375.43      |        -2.83333   | NEUTRAL  | Yahoo Finance |
| VWO        | 2026-09-18 00:00:00 |    60.01      |       -11.8333    | NEUTRAL  | Yahoo Finance |
| VZ         | 2026-09-18 00:00:00 |    48.09      |        -3.33333   | NEUTRAL  | Yahoo Finance |
| WFC        | 2026-09-18 00:00:00 |    86.12      |       -21.75      | NEUTRAL  | Yahoo Finance |
| WIF-USD    | 2026-09-21 00:00:00 |     0.2031    |        -0.666667  | NEUTRAL  | Kraken API    |
| WMT        | 2026-09-18 00:00:00 |   106.73      |        -6.33333   | NEUTRAL  | Yahoo Finance |
| XBI        | 2026-09-18 00:00:00 |   156.72      |        -8.83333   | NEUTRAL  | Yahoo Finance |
| XLB        | 2026-09-18 00:00:00 |    49.99      |       -67.0833    | NEUTRAL  | Yahoo Finance |
| XLC        | 2026-09-18 00:00:00 |   110.81      |       -56.0833    | NEUTRAL  | Yahoo Finance |
| XLE        | 2026-09-18 00:00:00 |    64.31      |        42.8333    | NEUTRAL  | Yahoo Finance |
| XLF        | 2026-09-18 00:00:00 |    55.86      |       -26.5       | NEUTRAL  | Yahoo Finance |
| XLK        | 2026-09-18 00:00:00 |   189.6       |        69.8333    | NEUTRAL  | Yahoo Finance |
| XLP        | 2026-09-18 00:00:00 |    82.8       |       -63.75      | NEUTRAL  | Yahoo Finance |
| XLV        | 2026-09-18 00:00:00 |   168.39      |         9.33333   | NEUTRAL  | Yahoo Finance |
| XOM        | 2026-09-18 00:00:00 |   163.54      |        44         | NEUTRAL  | Yahoo Finance |
| XRP-USD    | 2026-09-21 00:00:00 |     1.42      |        49.5       | NEUTRAL  | Kraken API    |
| YFI-USD    | 2026-09-21 00:00:00 |  2223.9       |        20.3333    | NEUTRAL  | Kraken API    |
| ADBE       | 2026-09-18 00:00:00 |   248.92      |       -36.5833    | SHORT    | Yahoo Finance |
| AGG        | 2026-09-18 00:00:00 |    95.96      |       -55.9167    | SHORT    | Yahoo Finance |
| AVGO       | 2026-09-18 00:00:00 |   357.61      |       -42.25      | SHORT    | Yahoo Finance |
| BA         | 2026-09-18 00:00:00 |   198.2       |       -50         | SHORT    | Yahoo Finance |
| BND        | 2026-09-18 00:00:00 |    71.2       |       -55.9167    | SHORT    | Yahoo Finance |
| CMCSA      | 2026-09-18 00:00:00 |    22.74      |       -58.3333    | SHORT    | Yahoo Finance |
| COST       | 2026-09-18 00:00:00 |   895.31      |       -58.8333    | SHORT    | Yahoo Finance |
| GE         | 2026-09-18 00:00:00 |   314.27      |       -61.1667    | SHORT    | Yahoo Finance |
| GS         | 2026-09-18 00:00:00 |   942         |       -59.0833    | SHORT    | Yahoo Finance |
| HD         | 2026-09-18 00:00:00 |   299.98      |       -62.8333    | SHORT    | Yahoo Finance |
| HON        | 2026-09-18 00:00:00 |   206.46      |       -35         | SHORT    | Yahoo Finance |
| HYG        | 2026-09-18 00:00:00 |    78.53      |       -55.9167    | SHORT    | Yahoo Finance |
| IEF        | 2026-09-18 00:00:00 |    90.8       |       -55.9167    | SHORT    | Yahoo Finance |
| ITA        | 2026-09-18 00:00:00 |   213.84      |       -59.1667    | SHORT    | Yahoo Finance |
| LIN        | 2026-09-18 00:00:00 |   460.4       |       -45.3333    | SHORT    | Yahoo Finance |
| LLY        | 2026-09-18 00:00:00 |  1152.93      |       -31.6667    | SHORT    | Yahoo Finance |
| MCD        | 2026-09-18 00:00:00 |   248.24      |       -60.8333    | SHORT    | Yahoo Finance |
| NKE        | 2026-09-18 00:00:00 |    35.51      |       -63.3333    | SHORT    | Yahoo Finance |
| PEP        | 2026-09-18 00:00:00 |   129.75      |       -56.8333    | SHORT    | Yahoo Finance |
| RTX        | 2026-09-18 00:00:00 |   194         |       -34.9167    | SHORT    | Yahoo Finance |
| SBUX       | 2026-09-18 00:00:00 |    95.83      |       -45.5833    | SHORT    | Yahoo Finance |
| SHY        | 2026-09-18 00:00:00 |    81.24      |       -57.6667    | SHORT    | Yahoo Finance |
| VNQ        | 2026-09-18 00:00:00 |    92.91      |       -42.3333    | SHORT    | Yahoo Finance |
| XLI        | 2026-09-18 00:00:00 |   169.75      |       -46.6667    | SHORT    | Yahoo Finance |
| XLU        | 2026-09-18 00:00:00 |    41.1       |       -54.5833    | SHORT    | Yahoo Finance |
| XLY        | 2026-09-18 00:00:00 |   111.03      |       -59.0833    | SHORT    | Yahoo Finance |

## Edge Summary

- Symbols with trades: **160** of 160
- Beat buy-and-hold: **30.00%** of traded symbols
- Positive return: **31.25%** of traded symbols
- Median strategy return: **-10.49%** (benchmark **21.73%**)
- Median excess vs benchmark: **-30.25%**
- Median Sharpe: **-0.16**
- Median exposure: **44.43%**

> Edge is real only if both _beat buy-and-hold_ and _median excess_ are convincingly positive across many symbols. Treat a single high-return symbol as noise.

## Portfolio Backtest

Actual capital-allocation books (not per-symbol averages). Benchmarks: `equal_weight_buyhold` (whole tracked universe), `spy_buyhold` (100% SPY), and `sixty_forty` (60% SPY / 40% AGG). `high_conf_voltarget` inverse-vol-weights the HIGH-confidence book; `conviction_long_short` is market-neutral. Judge on **Sharpe** and **max_drawdown** out-of-sample, not raw return: a fully-invested long book wins on return in a bull market but carries all the risk.

| strategy              | scope         | ann_return   | ann_vol   |   sharpe | max_drawdown   | total_return   |   avg_gross_exposure |
|:----------------------|:--------------|:-------------|:----------|---------:|:---------------|:---------------|---------------------:|
| equal_weight_buyhold  | full          | 13.03%       | 28.29%    |     0.46 | -39.63%        | 31.70%         |                 1    |
| equal_weight_buyhold  | out_of_sample | 13.92%       | 28.01%    |     0.5  | -29.33%        | 11.29%         |                 1    |
| all_signals_ew        | full          | -18.80%      | 23.85%    |    -0.79 | -62.96%        | -48.34%        |                 1    |
| all_signals_ew        | out_of_sample | 15.59%       | 23.13%    |     0.67 | -22.77%        | 14.80%         |                 1    |
| high_conf_ew          | full          | -0.08%       | 30.94%    |    -0    | -47.16%        | -13.63%        |                 0.89 |
| high_conf_ew          | out_of_sample | 37.85%       | 27.14%    |     1.39 | -22.62%        | 43.93%         |                 0.89 |
| high_conf_voltarget   | full          | -1.13%       | 27.71%    |    -0.04 | -40.34%        | -13.86%        |                 0.89 |
| high_conf_voltarget   | out_of_sample | 23.17%       | 22.75%    |     1.02 | -16.94%        | 24.49%         |                 0.89 |
| conviction_long_short | full          | -16.61%      | 22.46%    |    -0.74 | -50.16%        | -44.26%        |                 0.97 |
| conviction_long_short | out_of_sample | -2.72%       | 19.69%    |    -0.14 | -26.04%        | -4.85%         |                 0.97 |
| spy_buyhold           | full          | 6.74%        | 13.48%    |     0.5  | -19.00%        | 19.47%         |                 0.78 |
| spy_buyhold           | out_of_sample | 1.33%        | 9.89%     |     0.13 | -12.06%        | 0.90%          |                 0.78 |
| sixty_forty           | full          | 4.03%        | 8.52%     |     0.47 | -11.66%        | 11.82%         |                 0.78 |
| sixty_forty           | out_of_sample | -1.09%       | 6.64%     |    -0.16 | -8.26%         | -1.39%         |                 0.78 |

## Walk-Forward Robustness

Each book measured across contiguous time folds (each a different regime). A book has durable edge only if `mean_sharpe` is positive, `min_sharpe` isn't deeply negative, and `pct_positive_folds` is high — a single great fold doesn't count. `fold_sharpes` lists each fold oldest-to-newest.

| strategy              |   n_folds |   mean_sharpe |   median_sharpe |   min_sharpe | pct_positive_folds   | mean_return   | fold_sharpes                 |
|:----------------------|----------:|--------------:|----------------:|-------------:|:---------------------|:--------------|:-----------------------------|
| equal_weight_buyhold  |         5 |          0.75 |            0.65 |        -0.9  | 80.00%               | 6.72%         | 1.83;0.65;0.52;-0.90;1.67    |
| all_signals_ew        |         5 |         -0.84 |           -1.04 |        -2.38 | 40.00%               | -10.03%       | -1.04;-2.38;-2.10;1.21;0.13  |
| high_conf_ew          |         5 |          0.07 |           -0.13 |        -1.62 | 40.00%               | -1.02%        | -0.13;-1.62;-0.49;1.10;1.51  |
| high_conf_voltarget   |         5 |          0.07 |            0.32 |        -1.67 | 60.00%               | -2.11%        | 0.32;-1.67;-0.31;0.48;1.52   |
| conviction_long_short |         5 |         -0.75 |           -0.77 |        -1.95 | 20.00%               | -10.67%       | -1.95;-0.77;-0.99;-0.09;0.07 |
| spy_buyhold           |         5 |          0.63 |            0.37 |        -0.24 | 80.00%               | 3.93%         | 2.36;-0.24;0.37;0.07;0.60    |
| sixty_forty           |         5 |          0.57 |            0.24 |        -0.23 | 60.00%               | 2.40%         | 2.53;-0.23;0.43;-0.13;0.24   |

## Strategy Comparison

Each decision rule backtested over the same data. `out_of_sample` is the most recent ~35% of each symbol's history (unseen tail). A rule has real edge only if `median_excess` and `beat_benchmark_pct` stay positive out-of-sample, not just full-sample.

| strategy        | scope         |   symbols | beat_benchmark_pct   | positive_pct   | median_return   | median_benchmark   | median_excess   |   median_sharpe |   total_trades |
|:----------------|:--------------|----------:|:---------------------|:---------------|:----------------|:-------------------|:----------------|----------------:|---------------:|
| trend           | full          |       160 | 30.00%               | 31.25%         | -10.49%         | 21.73%             | -30.25%         |           -0.16 |          11354 |
| trend           | out_of_sample |       160 | 23.75%               | 51.88%         | 0.96%           | 12.80%             | -13.96%         |            0.19 |           3762 |
| mean_reversion  | full          |       156 | 32.69%               | 48.08%         | -0.21%          | 21.36%             | -22.02%         |           -0.01 |           1268 |
| mean_reversion  | out_of_sample |       119 | 29.41%               | 56.30%         | 0.39%           | 11.29%             | -11.72%         |            0.22 |            494 |
| regime_adaptive | full          |       160 | 28.75%               | 31.25%         | -12.02%         | 21.73%             | -29.57%         |           -0.12 |          11619 |
| regime_adaptive | out_of_sample |       160 | 24.38%               | 51.25%         | 0.55%           | 12.80%             | -14.45%         |            0.15 |           3898 |

## Signal Calibration

Realized forward return in the signal's direction, grouped by confidence. HIGH should outrank LOW for the confidence score to be meaningful.

| confidence_level   |   horizon |     n | mean_return   | median_return   | win_rate   |
|:-------------------|----------:|------:|:--------------|:----------------|:-----------|
| HIGH               |         5 |  7965 | 0.15%         | 0.07%           | 51.20%     |
| MEDIUM             |         5 | 28842 | 0.00%         | 0.03%           | 50.28%     |
| LOW                |         5 |  3595 | -0.48%        | -0.52%          | 45.31%     |
| ALL                |         5 | 40402 | -0.01%        | 0.01%           | 50.02%     |
| HIGH               |        10 |  7933 | 0.43%         | 0.09%           | 51.09%     |
| MEDIUM             |        10 | 28651 | 0.15%         | 0.07%           | 50.54%     |
| LOW                |        10 |  3560 | -0.74%        | -0.61%          | 46.21%     |
| ALL                |        10 | 40144 | 0.12%         | 0.03%           | 50.27%     |
| HIGH               |        20 |  7788 | 0.93%         | 0.33%           | 52.73%     |
| MEDIUM             |        20 | 28117 | 0.78%         | 0.55%           | 53.14%     |
| LOW                |        20 |  3460 | -0.67%        | -0.55%          | 47.25%     |
| ALL                |        20 | 39365 | 0.68%         | 0.43%           | 52.54%     |

## Backtest Summary

### Data Quality / Signal Availability

- **ok**: 160 symbols

| symbol     |   trades | return   | benchmark_return   | mdd     |   sharpe | exposure   | skipped_reason   |
|:-----------|---------:|:---------|:-------------------|:--------|---------:|:-----------|:-----------------|
| AAPL       |       62 | 10.14%   | 98.54%             | -23.09% |     0.3  | 50.08%     | ok               |
| AAVE-USD   |       71 | -35.43%  | 0.22%              | -66.17% |    -0.2  | 41.19%     | ok               |
| ABBV       |       72 | -26.66%  | 65.37%             | -31.38% |    -0.6  | 47.92%     | ok               |
| ADA-USD    |       79 | -37.61%  | -63.02%            | -45.96% |    -0.29 | 45.98%     | ok               |
| ADBE       |       69 | -13.53%  | -47.88%            | -31.20% |    -0.06 | 55.41%     | ok               |
| AGG        |       71 | -7.33%   | 0.66%              | -10.23% |    -1.22 | 32.45%     | ok               |
| ALGO-USD   |       80 | -34.91%  | -42.09%            | -43.00% |    -0.29 | 39.27%     | ok               |
| AMAT       |       67 | -31.08%  | 118.59%            | -53.91% |    -0.25 | 49.92%     | ok               |
| AMD        |       52 | 16.69%   | 255.67%            | -40.05% |     0.37 | 34.44%     | ok               |
| AMGN       |       67 | -6.80%   | 42.84%             | -34.19% |    -0.04 | 50.58%     | ok               |
| AMZN       |       82 | -55.57%  | 41.25%             | -56.68% |    -1.58 | 41.93%     | ok               |
| APT-USD    |       78 | -39.81%  | -84.15%            | -65.32% |    -0.24 | 40.23%     | ok               |
| ARB-USD    |       77 | -20.77%  | -25.10%            | -57.15% |     0.08 | 41.95%     | ok               |
| ARKK       |       86 | -25.31%  | 100.20%            | -28.66% |    -0.35 | 42.93%     | ok               |
| ATOM-USD   |       90 | -56.72%  | -57.20%            | -59.14% |    -0.79 | 47.32%     | ok               |
| AVAX-USD   |       76 | -31.97%  | -39.63%            | -46.19% |    -0.26 | 38.89%     | ok               |
| AVGO       |       64 | 15.50%   | 166.07%            | -36.08% |     0.34 | 41.76%     | ok               |
| BA         |       71 | -0.26%   | 18.53%             | -26.77% |     0.12 | 49.42%     | ok               |
| BAC        |       76 | -12.84%  | 52.60%             | -25.82% |    -0.29 | 47.92%     | ok               |
| BCH-USD    |       76 | 21.99%   | -23.98%            | -53.41% |     0.43 | 48.85%     | ok               |
| BITO       |       76 | -14.59%  | -60.58%            | -39.47% |    -0.03 | 39.93%     | ok               |
| BLK        |       81 | -9.90%   | 40.23%             | -26.90% |    -0.2  | 48.75%     | ok               |
| BND        |       71 | -7.67%   | 0.66%              | -10.19% |    -1.22 | 34.28%     | ok               |
| BONK-USD   |       76 | 24.46%   | -74.42%            | -45.22% |     0.47 | 44.64%     | ok               |
| BTC-USD    |       70 | 20.10%   | -3.66%             | -23.38% |     0.46 | 52.68%     | ok               |
| C          |       77 | -35.16%  | 110.29%            | -41.08% |    -0.76 | 47.92%     | ok               |
| CAT        |       70 | 9.04%    | 135.60%            | -19.71% |     0.27 | 49.75%     | ok               |
| CL         |       60 | 2.30%    | -3.89%             | -14.32% |     0.14 | 40.60%     | ok               |
| CMCSA      |       82 | -40.66%  | -37.09%            | -47.67% |    -1.04 | 42.10%     | ok               |
| COMP-USD   |       97 | -42.57%  | -43.85%            | -52.81% |    -0.3  | 47.89%     | ok               |
| COP        |       70 | -22.16%  | 1.22%              | -43.40% |    -0.35 | 43.93%     | ok               |
| COST       |       62 | 0.92%    | 22.78%             | -29.73% |     0.09 | 41.76%     | ok               |
| CRM        |       69 | -31.08%  | -13.26%            | -44.86% |    -0.43 | 46.76%     | ok               |
| CRV-USD    |       68 | 45.83%   | -42.03%            | -39.89% |     0.6  | 41.19%     | ok               |
| CSCO       |       60 | 15.86%   | 128.81%            | -21.79% |     0.39 | 47.75%     | ok               |
| CVX        |       73 | -12.62%  | 26.29%             | -29.13% |    -0.27 | 41.60%     | ok               |
| DASH-USD   |       55 | -12.34%  | 175.55%            | -64.43% |     0.29 | 29.89%     | ok               |
| DBC        |       64 | -5.14%   | 39.18%             | -24.60% |    -0.11 | 34.44%     | ok               |
| DE         |       76 | -14.49%  | 73.90%             | -25.41% |    -0.23 | 44.76%     | ok               |
| DIA        |       64 | -4.94%   | 34.94%             | -12.94% |    -0.23 | 45.26%     | ok               |
| DIS        |       66 | -14.81%  | -8.92%             | -28.17% |    -0.24 | 43.76%     | ok               |
| DOGE-USD   |       72 | -32.08%  | -43.95%            | -62.31% |    -0.12 | 47.89%     | ok               |
| DOT-USD    |       92 | -59.26%  | -68.58%            | -64.69% |    -0.6  | 48.08%     | ok               |
| DXY-INDEX  |       44 | -2.93%   | -5.63%             | -6.06%  |    -0.45 | 31.39%     | ok               |
| EEM        |       62 | -10.07%  | 62.81%             | -25.38% |    -0.27 | 41.60%     | ok               |
| EFA        |       58 | -9.14%   | 34.65%             | -12.28% |    -0.34 | 42.76%     | ok               |
| EOG        |       81 | -31.44%  | 6.29%              | -48.55% |    -0.69 | 45.26%     | ok               |
| ETC-USD    |       62 | -28.25%  | -44.97%            | -47.84% |    -0.34 | 28.16%     | ok               |
| ETH-USD    |       58 | 174.10%  | 67.57%             | -30.11% |     1.43 | 46.17%     | ok               |
| EWJ        |       64 | -23.51%  | 44.50%             | -29.40% |    -0.82 | 37.10%     | ok               |
| FCX        |       63 | -27.17%  | 41.66%             | -46.84% |    -0.28 | 44.59%     | ok               |
| FET-USD    |       75 | -27.36%  | -63.80%            | -60.12% |    -0.04 | 40.23%     | ok               |
| FIL-USD    |       69 | -56.67%  | -61.00%            | -58.98% |    -0.8  | 33.72%     | ok               |
| FXI        |       48 | -5.41%   | 32.66%             | -24.33% |    -0.05 | 32.28%     | ok               |
| GDX        |       60 | -1.86%   | 176.11%            | -34.99% |     0.11 | 44.76%     | ok               |
| GDXJ       |       68 | -35.93%  | 193.56%            | -44.61% |    -0.47 | 42.76%     | ok               |
| GE         |       78 | -15.50%  | 93.58%             | -27.82% |    -0.19 | 47.75%     | ok               |
| GLD        |       54 | 8.08%    | 85.20%             | -14.69% |     0.28 | 44.76%     | ok               |
| GOOGL      |       55 | 48.87%   | 103.28%            | -17.63% |     0.89 | 47.25%     | ok               |
| GRT-USD    |       83 | 3.56%    | -70.94%            | -47.21% |     0.25 | 43.10%     | ok               |
| GS         |       66 | -3.01%   | 120.31%            | -22.13% |     0.03 | 47.42%     | ok               |
| HD         |       73 | -3.22%   | -10.48%            | -17.37% |    -0.01 | 42.60%     | ok               |
| HON        |       90 | -23.51%  | 7.97%              | -33.57% |    -0.56 | 56.07%     | ok               |
| HYG        |       87 | -8.95%   | 2.49%              | -10.69% |    -1.03 | 36.61%     | ok               |
| IBIT       |       38 | 36.88%   | 21.07%             | -18.95% |     0.7  | 32.84%     | ok               |
| IBM        |       73 | -25.87%  | 37.35%             | -48.94% |    -0.31 | 50.75%     | ok               |
| ICP-USD    |       75 | 1.32%    | -37.42%            | -46.42% |     0.27 | 36.97%     | ok               |
| IEF        |       86 | -11.70%  | -0.75%             | -12.55% |    -1.69 | 32.45%     | ok               |
| IEMG       |       62 | -10.97%  | 57.64%             | -29.43% |    -0.32 | 41.93%     | ok               |
| INJ-USD    |       69 | -30.25%  | -2.91%             | -73.61% |    -0.07 | 38.12%     | ok               |
| INTC       |       68 | 41.93%   | 240.65%            | -60.60% |     0.54 | 48.25%     | ok               |
| INTU       |       71 | -18.42%  | -52.37%            | -42.50% |    -0.19 | 44.26%     | ok               |
| ITA        |       72 | -0.77%   | 65.09%             | -23.75% |     0.06 | 49.08%     | ok               |
| IWM        |       54 | 11.41%   | 43.22%             | -12.65% |     0.46 | 36.44%     | ok               |
| JNJ        |       68 | -1.24%   | 84.75%             | -17.51% |     0.02 | 47.25%     | ok               |
| JPM        |       73 | -20.45%  | 80.72%             | -32.74% |    -0.53 | 47.92%     | ok               |
| KO         |       54 | 25.74%   | 42.94%             | -8.64%  |     0.9  | 39.77%     | ok               |
| LDO-USD    |       72 | 13.86%   | -38.11%            | -59.60% |     0.39 | 46.36%     | ok               |
| LIN        |       72 | -10.91%  | 3.89%              | -20.61% |    -0.35 | 36.94%     | ok               |
| LINK-USD   |       73 | 45.80%   | 0.95%              | -33.64% |     0.62 | 45.79%     | ok               |
| LLY        |       71 | -30.62%  | 57.18%             | -53.34% |    -0.47 | 48.59%     | ok               |
| LRCX       |       84 | -25.21%  | 211.35%            | -61.08% |    -0.15 | 42.43%     | ok               |
| LTC-USD    |       72 | -2.26%   | -22.72%            | -33.94% |     0.16 | 51.53%     | ok               |
| MCD        |       77 | -4.76%   | -9.10%             | -21.88% |    -0.14 | 37.94%     | ok               |
| META       |       78 | -33.85%  | 50.18%             | -44.52% |    -0.59 | 48.42%     | ok               |
| MPC        |       67 | 13.37%   | 114.17%            | -37.91% |     0.34 | 50.42%     | ok               |
| MRK        |       67 | -24.24%  | 11.94%             | -35.95% |    -0.47 | 44.09%     | ok               |
| MS         |       73 | -9.87%   | 118.23%            | -27.79% |    -0.16 | 47.59%     | ok               |
| MSFT       |       83 | -30.50%  | 21.52%             | -37.80% |    -0.71 | 49.92%     | ok               |
| MU         |       49 | 164.65%  | 784.54%            | -68.76% |     1.08 | 53.91%     | ok               |
| NEAR-USD   |       75 | 94.10%   | 114.82%            | -55.01% |     0.85 | 42.72%     | ok               |
| NEM        |       66 | -25.45%  | 188.81%            | -39.56% |    -0.24 | 52.58%     | ok               |
| NFLX       |       76 | 12.79%   | 27.92%             | -21.09% |     0.35 | 53.24%     | ok               |
| NKE        |       79 | -26.52%  | -62.27%            | -55.35% |    -0.29 | 44.26%     | ok               |
| NOW        |       86 | 6.41%    | -6.39%             | -30.43% |     0.25 | 50.58%     | ok               |
| NVDA       |       77 | -45.16%  | 76.28%             | -52.37% |    -0.59 | 56.86%     | ok               |
| OP-USD     |       68 | -45.01%  | -80.68%            | -68.74% |    -0.4  | 32.57%     | ok               |
| ORCL       |       64 | 91.75%   | 25.94%             | -30.61% |     0.83 | 54.58%     | ok               |
| OXY        |       71 | -3.13%   | -13.19%            | -29.80% |     0.07 | 42.60%     | ok               |
| PEP        |       74 | 1.60%    | -26.10%            | -21.35% |     0.12 | 45.92%     | ok               |
| PEPE-USD   |       89 | -39.87%  | -45.16%            | -57.66% |    -0.17 | 47.70%     | ok               |
| PFE        |       83 | -37.94%  | 8.90%              | -42.69% |    -1.15 | 39.10%     | ok               |
| PG         |       64 | -21.35%  | -9.24%             | -24.25% |    -0.84 | 36.61%     | ok               |
| PM         |       79 | -2.68%   | 98.51%             | -35.15% |     0.03 | 53.08%     | ok               |
| POL-USD    |       87 | 47.30%   | -41.80%            | -39.52% |     0.64 | 49.62%     | ok               |
| QCOM       |       75 | -21.75%  | 7.28%              | -57.69% |    -0.14 | 43.26%     | ok               |
| QQQ        |       66 | 13.22%   | 67.39%             | -14.20% |     0.41 | 46.42%     | ok               |
| RENDER-USD |      102 | -29.76%  | -55.60%            | -44.84% |    -0.05 | 45.98%     | ok               |
| RTX        |       60 | 35.19%   | 91.30%             | -16.99% |     0.78 | 52.75%     | ok               |
| SBUX       |       58 | -14.66%  | 8.59%              | -29.22% |    -0.24 | 38.44%     | ok               |
| SCHW       |       78 | -15.94%  | 40.35%             | -31.92% |    -0.32 | 47.09%     | ok               |
| SHIB-USD   |       82 | -41.02%  | -54.90%            | -43.50% |    -0.42 | 52.11%     | ok               |
| SHY        |       48 | -1.90%   | 0.04%              | -3.18%  |    -0.65 | 35.27%     | ok               |
| SKY-USD    |       85 | -48.76%  | 21.93%             | -58.79% |    -0.65 | 45.49%     | ok               |
| SLB        |       75 | -37.76%  | 3.90%              | -57.55% |    -0.71 | 49.42%     | ok               |
| SLV        |       68 | 14.42%   | 140.78%            | -42.66% |     0.35 | 41.26%     | ok               |
| SMH        |       48 | 67.47%   | 163.28%            | -34.29% |     0.99 | 44.93%     | ok               |
| SNX-USD    |       62 | -21.09%  | -63.06%            | -47.16% |    -0.04 | 32.18%     | ok               |
| SOL-USD    |       68 | -3.19%   | -16.92%            | -44.99% |     0.2  | 60.15%     | ok               |
| SOXX       |       56 | 69.47%   | 145.77%            | -39.81% |     0.95 | 43.26%     | ok               |
| SPY        |       64 | 3.49%    | 49.86%             | -15.53% |     0.18 | 51.58%     | ok               |
| SUSHI-USD  |      100 | -80.10%  | -55.51%            | -82.74% |    -1.31 | 37.93%     | ok               |
| T          |       70 | 42.64%   | 51.64%             | -17.01% |     0.89 | 58.40%     | ok               |
| TGT        |       62 | -13.62%  | -3.98%             | -36.37% |    -0.23 | 37.94%     | ok               |
| TIA-USD    |       93 | -62.95%  | -81.92%            | -73.85% |    -0.62 | 40.42%     | ok               |
| TLT        |       72 | -19.72%  | -7.92%             | -21.87% |    -1.45 | 34.11%     | ok               |
| TMO        |       67 | 27.87%   | 13.57%             | -18.85% |     0.59 | 54.41%     | ok               |
| TMUS       |       76 | 2.41%    | 2.57%              | -27.06% |     0.15 | 48.25%     | ok               |
| TRX-USD    |       68 | 10.93%   | 42.90%             | -22.90% |     0.38 | 52.30%     | ok               |
| TSLA       |       80 | -35.03%  | 116.45%            | -58.36% |    -0.22 | 43.09%     | ok               |
| TXN        |       75 | -23.22%  | 50.24%             | -48.70% |    -0.23 | 49.92%     | ok               |
| UNH        |       73 | 30.80%   | -23.91%            | -26.31% |     0.53 | 49.92%     | ok               |
| UNI-USD    |       92 | -51.92%  | 70.89%             | -78.80% |    -0.32 | 48.47%     | ok               |
| UPS        |       70 | -34.92%  | -32.88%            | -38.32% |    -0.69 | 40.10%     | ok               |
| USO        |       70 | 7.86%    | 91.34%             | -42.37% |     0.25 | 33.11%     | ok               |
| VEA        |       58 | -2.41%   | 46.03%             | -16.30% |    -0.05 | 43.43%     | ok               |
| VIXY       |       96 | -76.58%  | -68.00%            | -88.17% |    -0.88 | 34.11%     | ok               |
| VNQ        |       77 | -16.89%  | 15.91%             | -24.92% |    -0.71 | 38.60%     | ok               |
| VTI        |       70 | -5.97%   | 49.11%             | -17.64% |    -0.16 | 51.75%     | ok               |
| VWO        |       80 | -16.33%  | 41.80%             | -24.94% |    -0.6  | 41.93%     | ok               |
| VZ         |       82 | -18.51%  | 21.19%             | -25.90% |    -0.53 | 40.93%     | ok               |
| WFC        |       78 | -16.69%  | 43.75%             | -28.90% |    -0.27 | 47.09%     | ok               |
| WIF-USD    |       66 | -26.92%  | -49.54%            | -52.76% |    -0.02 | 35.63%     | ok               |
| WMT        |       65 | 10.38%   | 77.41%             | -21.98% |     0.35 | 48.09%     | ok               |
| XBI        |       66 | 0.68%    | 87.71%             | -18.30% |     0.1  | 41.60%     | ok               |
| XLB        |       60 | -12.29%  | 11.68%             | -25.04% |    -0.43 | 31.95%     | ok               |
| XLC        |       63 | 14.20%   | 38.32%             | -12.33% |     0.52 | 50.58%     | ok               |
| XLE        |       73 | -13.13%  | 34.34%             | -34.24% |    -0.26 | 44.59%     | ok               |
| XLF        |       80 | -9.53%   | 36.84%             | -23.61% |    -0.3  | 45.76%     | ok               |
| XLI        |       76 | -5.83%   | 38.39%             | -14.16% |    -0.18 | 41.76%     | ok               |
| XLK        |       40 | 67.33%   | 89.76%             | -14.75% |     1.23 | 47.59%     | ok               |
| XLM-USD    |       67 | -15.27%  | -17.46%            | -54.58% |     0.03 | 45.98%     | ok               |
| XLP        |       64 | 6.92%    | 9.54%              | -10.28% |     0.42 | 38.94%     | ok               |
| XLU        |       69 | -2.19%   | 24.19%             | -20.40% |    -0.05 | 39.43%     | ok               |
| XLV        |       70 | -15.89%  | 20.31%             | -19.60% |    -0.73 | 37.44%     | ok               |
| XLY        |       79 | -6.07%   | 26.24%             | -17.65% |    -0.12 | 46.42%     | ok               |
| XOM        |       57 | 0.48%    | 38.64%             | -20.29% |     0.09 | 34.44%     | ok               |
| XRP-USD    |       60 | 9.21%    | -31.16%            | -33.91% |     0.3  | 36.59%     | ok               |
| YFI-USD    |       77 | -67.41%  | -50.48%            | -72.54% |    -1.21 | 38.12%     | ok               |
| ZEC-USD    |       64 | 183.18%  | 4832.71%           | -56.50% |     1.01 | 41.76%     | ok               |

## AAPL Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 17.03%   | 98.54%             | -22.53% |     0.41 |       71 | 54.91%     | ok               |
|          15 | 12.80%   | 98.54%             | -24.50% |     0.34 |       82 | 62.06%     | ok               |
|          40 | 10.24%   | 98.54%             | -28.08% |     0.3  |       56 | 44.76%     | ok               |
|          30 | 10.14%   | 98.54%             | -23.09% |     0.3  |       62 | 50.08%     | ok               |
|          35 | 8.56%    | 98.54%             | -24.45% |     0.27 |       62 | 48.75%     | ok               |

## AAVE-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 36.74%   | 0.22%              | -43.61% |     0.56 |       41 | 34.48%     | ok               |
|          45 | 24.00%   | 0.22%              | -49.19% |     0.45 |       46 | 29.31%     | ok               |
|          35 | 19.28%   | 0.22%              | -48.79% |     0.41 |       49 | 37.55%     | ok               |
|          50 | 10.25%   | 0.22%              | -45.07% |     0.31 |       44 | 22.03%     | ok               |
|          15 | -26.92%  | 0.22%              | -61.76% |     0.01 |       76 | 55.17%     | ok               |

## ABBV Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -14.18%  | 65.37%             | -26.24% |    -0.3  |       52 | 35.44%     | ok               |
|          45 | -23.85%  | 65.37%             | -27.36% |    -0.59 |       62 | 37.27%     | ok               |
|          40 | -24.09%  | 65.37%             | -27.52% |    -0.59 |       70 | 39.93%     | ok               |
|          30 | -26.66%  | 65.37%             | -31.38% |    -0.6  |       72 | 47.92%     | ok               |
|          25 | -30.02%  | 65.37%             | -35.52% |    -0.68 |       71 | 50.75%     | ok               |

## ADA-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 14.75%   | -63.02%            | -35.54% |     0.36 |       52 | 26.25%     | ok               |
|          45 | 3.87%    | -63.02%            | -34.64% |     0.25 |       51 | 30.84%     | ok               |
|          40 | -13.84%  | -63.02%            | -40.73% |     0.04 |       63 | 36.78%     | ok               |
|          35 | -20.50%  | -63.02%            | -42.89% |    -0.04 |       67 | 40.80%     | ok               |
|          15 | -34.47%  | -63.02%            | -47.27% |    -0.09 |       74 | 62.64%     | ok               |

## ADBE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | 3.97%    | -47.88%            | -29.07% |     0.21 |       57 | 59.40%     | ok               |
|          35 | -0.97%   | -47.88%            | -30.52% |     0.11 |       73 | 47.25%     | ok               |
|          20 | -11.47%  | -47.88%            | -31.52% |    -0.01 |       63 | 62.56%     | ok               |
|          30 | -13.53%  | -47.88%            | -31.20% |    -0.06 |       69 | 55.41%     | ok               |
|          15 | -18.31%  | -47.88%            | -34.98% |    -0.12 |       68 | 64.39%     | ok               |

## AGG Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -5.35%   | 0.66%              | -8.07%  |    -1.14 |       54 | 18.64%     | ok               |
|          30 | -7.33%   | 0.66%              | -10.23% |    -1.22 |       71 | 32.45%     | ok               |
|          45 | -6.38%   | 0.66%              | -8.72%  |    -1.23 |       60 | 23.29%     | ok               |
|          20 | -8.65%   | 0.66%              | -11.36% |    -1.27 |       73 | 37.77%     | ok               |
|          25 | -8.83%   | 0.66%              | -12.00% |    -1.35 |       73 | 36.11%     | ok               |

## ALGO-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -34.91%  | -42.09%            | -43.00% |    -0.29 |       80 | 39.27%     | ok               |
|          15 | -40.16%  | -42.09%            | -51.37% |    -0.3  |       78 | 50.38%     | ok               |
|          25 | -43.64%  | -42.09%            | -58.91% |    -0.4  |       78 | 45.02%     | ok               |
|          20 | -46.45%  | -42.09%            | -54.82% |    -0.43 |       80 | 47.89%     | ok               |
|          35 | -46.20%  | -42.09%            | -49.75% |    -0.62 |       62 | 32.76%     | ok               |

## AMAT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -29.05%  | 118.59%            | -53.90% |    -0.18 |       68 | 58.90%     | ok               |
|          50 | -26.90%  | 118.59%            | -45.04% |    -0.24 |       46 | 35.11%     | ok               |
|          30 | -31.08%  | 118.59%            | -53.91% |    -0.25 |       67 | 49.92%     | ok               |
|          35 | -30.79%  | 118.59%            | -51.27% |    -0.26 |       67 | 47.42%     | ok               |
|          40 | -36.43%  | 118.59%            | -53.95% |    -0.38 |       65 | 42.60%     | ok               |

## AMD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 17.56%   | 255.67%            | -40.05% |     0.37 |       58 | 29.62%     | ok               |
|          40 | 16.69%   | 255.67%            | -40.05% |     0.37 |       52 | 34.44%     | ok               |
|          35 | 14.28%   | 255.67%            | -42.14% |     0.35 |       60 | 35.94%     | ok               |
|          30 | 2.90%    | 255.67%            | -47.00% |     0.25 |       65 | 38.44%     | ok               |
|          25 | -4.16%   | 255.67%            | -52.75% |     0.18 |       65 | 41.10%     | ok               |

## AMGN Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -0.45%   | 42.84%             | -26.65% |     0.1  |       62 | 56.07%     | ok               |
|          35 | -4.38%   | 42.84%             | -31.29% |     0.01 |       67 | 47.09%     | ok               |
|          15 | -6.68%   | 42.84%             | -27.98% |    -0.02 |       61 | 60.23%     | ok               |
|          30 | -6.80%   | 42.84%             | -34.19% |    -0.04 |       67 | 50.58%     | ok               |
|          25 | -8.86%   | 42.84%             | -33.47% |    -0.08 |       61 | 52.91%     | ok               |

## AMZN Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -26.84%  | 41.25%             | -28.95% |    -0.81 |       56 | 30.62%     | ok               |
|          50 | -31.32%  | 41.25%             | -33.94% |    -1.13 |       52 | 23.63%     | ok               |
|          45 | -36.48%  | 41.25%             | -37.70% |    -1.29 |       58 | 27.12%     | ok               |
|          35 | -50.72%  | 41.25%             | -51.56% |    -1.47 |       75 | 35.77%     | ok               |
|          30 | -55.57%  | 41.25%             | -56.68% |    -1.58 |       82 | 41.93%     | ok               |

## APT-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 3.71%    | -84.15%            | -38.58% |     0.21 |       44 | 17.62%     | ok               |
|          20 | -29.56%  | -84.15%            | -65.18% |    -0.04 |       84 | 49.23%     | ok               |
|          45 | -21.97%  | -84.15%            | -58.71% |    -0.11 |       56 | 23.37%     | ok               |
|          35 | -33.46%  | -84.15%            | -57.56% |    -0.2  |       72 | 34.10%     | ok               |
|          30 | -39.81%  | -84.15%            | -65.32% |    -0.24 |       78 | 40.23%     | ok               |

## ARB-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 56.15%   | -25.10%            | -44.26% |     0.64 |       87 | 59.00%     | ok               |
|          45 | 40.57%   | -25.10%            | -35.90% |     0.56 |       56 | 25.48%     | ok               |
|          50 | 30.91%   | -25.10%            | -30.72% |     0.5  |       44 | 18.39%     | ok               |
|          20 | 20.03%   | -25.10%            | -54.05% |     0.45 |       73 | 52.87%     | ok               |
|          40 | 13.87%   | -25.10%            | -40.13% |     0.38 |       57 | 32.76%     | ok               |

## ARKK Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -16.53%  | 100.20%            | -37.76% |    -0.11 |       94 | 55.74%     | ok               |
|          20 | -20.26%  | 100.20%            | -34.82% |    -0.19 |       90 | 50.92%     | ok               |
|          30 | -25.31%  | 100.20%            | -28.66% |    -0.35 |       86 | 42.93%     | ok               |
|          35 | -33.15%  | 100.20%            | -34.08% |    -0.56 |       86 | 40.60%     | ok               |
|          25 | -40.04%  | 100.20%            | -43.18% |    -0.67 |      102 | 46.26%     | ok               |

## ATOM-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -41.20%  | -57.20%            | -48.77% |    -0.34 |       88 | 64.37%     | ok               |
|          25 | -46.43%  | -57.20%            | -51.34% |    -0.49 |       90 | 53.64%     | ok               |
|          20 | -56.34%  | -57.20%            | -59.48% |    -0.7  |       96 | 57.09%     | ok               |
|          30 | -56.72%  | -57.20%            | -59.14% |    -0.79 |       90 | 47.32%     | ok               |
|          35 | -57.17%  | -57.20%            | -58.90% |    -0.9  |       80 | 41.57%     | ok               |

## AVAX-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 37.92%   | -39.63%            | -22.06% |     0.67 |       34 | 17.62%     | ok               |
|          40 | 22.30%   | -39.63%            | -30.70% |     0.46 |       38 | 25.10%     | ok               |
|          45 | 19.35%   | -39.63%            | -27.52% |     0.43 |       32 | 21.84%     | ok               |
|          15 | -2.13%   | -39.63%            | -42.39% |     0.22 |       74 | 53.07%     | ok               |
|          35 | 0.03%    | -39.63%            | -37.03% |     0.18 |       56 | 31.42%     | ok               |

## AVGO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | 18.82%   | 166.07%            | -38.01% |     0.38 |       68 | 44.43%     | ok               |
|          30 | 15.50%   | 166.07%            | -36.08% |     0.34 |       64 | 41.76%     | ok               |
|          50 | 10.84%   | 166.07%            | -36.86% |     0.29 |       56 | 29.78%     | ok               |
|          35 | 7.11%    | 166.07%            | -39.56% |     0.25 |       74 | 38.77%     | ok               |
|          40 | 7.22%    | 166.07%            | -40.70% |     0.25 |       66 | 35.61%     | ok               |

## BA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 28.38%   | 18.53%             | -13.34% |     0.71 |       44 | 32.95%     | ok               |
|          35 | 20.94%   | 18.53%             | -18.53% |     0.46 |       72 | 45.42%     | ok               |
|          40 | 16.40%   | 18.53%             | -23.87% |     0.41 |       48 | 40.43%     | ok               |
|          25 | 6.64%    | 18.53%             | -27.42% |     0.24 |       72 | 53.08%     | ok               |
|          30 | -0.26%   | 18.53%             | -26.77% |     0.12 |       71 | 49.42%     | ok               |

## BAC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -4.59%   | 52.60%             | -18.28% |    -0.03 |       80 | 52.58%     | ok               |
|          25 | -7.29%   | 52.60%             | -22.50% |    -0.12 |       78 | 50.58%     | ok               |
|          15 | -9.49%   | 52.60%             | -21.05% |    -0.14 |       82 | 58.40%     | ok               |
|          35 | -8.16%   | 52.60%             | -27.30% |    -0.17 |       66 | 44.09%     | ok               |
|          45 | -8.23%   | 52.60%             | -20.78% |    -0.2  |       60 | 36.61%     | ok               |

## BCH-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 84.50%   | -23.98%            | -45.51% |     0.85 |       71 | 58.05%     | ok               |
|          20 | 52.55%   | -23.98%            | -45.52% |     0.66 |       67 | 54.60%     | ok               |
|          25 | 30.41%   | -23.98%            | -50.59% |     0.5  |       66 | 51.15%     | ok               |
|          30 | 21.99%   | -23.98%            | -53.41% |     0.43 |       76 | 48.85%     | ok               |
|          35 | -2.42%   | -23.98%            | -58.53% |     0.19 |       74 | 45.21%     | ok               |

## BITO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -3.95%   | -60.58%            | -31.98% |     0.08 |       54 | 24.13%     | ok               |
|          30 | -14.59%  | -60.58%            | -39.47% |    -0.03 |       76 | 39.93%     | ok               |
|          15 | -22.28%  | -60.58%            | -48.29% |    -0.08 |       87 | 49.25%     | ok               |
|          35 | -18.76%  | -60.58%            | -41.51% |    -0.1  |       68 | 35.77%     | ok               |
|          45 | -17.19%  | -60.58%            | -36.67% |    -0.12 |       60 | 27.62%     | ok               |

## BLK Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -4.14%   | 40.23%             | -21.48% |    -0.02 |       84 | 53.41%     | ok               |
|          35 | -3.70%   | 40.23%             | -20.79% |    -0.03 |       88 | 45.09%     | ok               |
|          40 | -4.53%   | 40.23%             | -22.83% |    -0.07 |       78 | 40.43%     | ok               |
|          25 | -5.51%   | 40.23%             | -24.62% |    -0.07 |       77 | 51.25%     | ok               |
|          30 | -9.90%   | 40.23%             | -26.90% |    -0.2  |       81 | 48.75%     | ok               |

## BND Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -6.53%   | 0.66%              | -9.43%  |    -0.94 |       66 | 39.77%     | ok               |
|          25 | -7.23%   | 0.66%              | -10.55% |    -1.08 |       69 | 37.77%     | ok               |
|          30 | -7.67%   | 0.66%              | -10.19% |    -1.22 |       71 | 34.28%     | ok               |
|          15 | -8.79%   | 0.66%              | -11.30% |    -1.25 |       78 | 42.60%     | ok               |
|          40 | -7.98%   | 0.66%              | -10.20% |    -1.44 |       64 | 27.45%     | ok               |

## BONK-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 148.90%  | -74.42%            | -35.57% |     1.17 |       44 | 21.65%     | ok               |
|          15 | 84.86%   | -74.42%            | -63.45% |     0.76 |       68 | 59.96%     | ok               |
|          25 | 72.79%   | -74.42%            | -47.99% |     0.72 |       71 | 51.34%     | ok               |
|          20 | 71.41%   | -74.42%            | -55.43% |     0.71 |       66 | 55.94%     | ok               |
|          45 | 59.87%   | -74.42%            | -42.36% |     0.7  |       62 | 27.20%     | ok               |

## BTC-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 62.50%   | -3.66%             | -13.36% |     1.13 |       42 | 32.76%     | ok               |
|          35 | 64.98%   | -3.66%             | -21.56% |     1.1  |       62 | 42.53%     | ok               |
|          40 | 61.34%   | -3.66%             | -14.50% |     1.09 |       44 | 36.59%     | ok               |
|          50 | 28.70%   | -3.66%             | -19.38% |     0.68 |       42 | 27.20%     | ok               |
|          30 | 34.23%   | -3.66%             | -21.75% |     0.66 |       68 | 48.28%     | ok               |

## C Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -10.42%  | 110.29%            | -21.80% |    -0.23 |       66 | 33.11%     | ok               |
|          45 | -18.66%  | 110.29%            | -27.40% |    -0.45 |       72 | 37.10%     | ok               |
|          40 | -24.41%  | 110.29%            | -33.13% |    -0.58 |       74 | 39.43%     | ok               |
|          25 | -32.20%  | 110.29%            | -38.39% |    -0.66 |       67 | 49.92%     | ok               |
|          15 | -34.46%  | 110.29%            | -38.73% |    -0.67 |       70 | 56.74%     | ok               |

## CAT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | 17.36%   | 135.60%            | -19.50% |     0.39 |       64 | 52.25%     | ok               |
|          15 | 16.60%   | 135.60%            | -20.14% |     0.37 |       74 | 62.73%     | ok               |
|          20 | 11.97%   | 135.60%            | -19.74% |     0.31 |       76 | 55.91%     | ok               |
|          30 | 9.04%    | 135.60%            | -19.71% |     0.27 |       70 | 49.75%     | ok               |
|          45 | 2.71%    | 135.60%            | -26.22% |     0.16 |       56 | 38.27%     | ok               |

## CL Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 2.30%    | -3.89%             | -14.32% |     0.14 |       60 | 40.60%     | ok               |
|          50 | 1.93%    | -3.89%             | -12.98% |     0.13 |       42 | 25.12%     | ok               |
|          45 | -1.67%   | -3.89%             | -13.51% |    -0.01 |       46 | 27.79%     | ok               |
|          35 | -2.29%   | -3.89%             | -13.83% |    -0.02 |       62 | 37.10%     | ok               |
|          40 | -5.13%   | -3.89%             | -12.70% |    -0.15 |       56 | 31.78%     | ok               |

## CMCSA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -41.03%  | -37.09%            | -48.00% |    -0.92 |       91 | 56.91%     | ok               |
|          50 | -25.42%  | -37.09%            | -30.39% |    -0.94 |       48 | 13.81%     | ok               |
|          30 | -40.66%  | -37.09%            | -47.67% |    -1.04 |       82 | 42.10%     | ok               |
|          40 | -37.51%  | -37.09%            | -44.10% |    -1.09 |       93 | 26.96%     | ok               |
|          35 | -40.47%  | -37.09%            | -47.50% |    -1.11 |       93 | 36.77%     | ok               |

## COMP-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -1.53%   | -43.85%            | -38.71% |     0.18 |       46 | 21.84%     | ok               |
|          30 | -42.57%  | -43.85%            | -52.81% |    -0.3  |       97 | 47.89%     | ok               |
|          25 | -48.24%  | -43.85%            | -51.58% |    -0.37 |       96 | 55.75%     | ok               |
|          45 | -42.95%  | -43.85%            | -51.35% |    -0.42 |       60 | 30.27%     | ok               |
|          40 | -45.40%  | -43.85%            | -50.93% |    -0.44 |       68 | 35.63%     | ok               |

## COP Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -6.97%   | 1.22%              | -34.21% |    -0.06 |       46 | 29.28%     | ok               |
|          45 | -12.43%  | 1.22%              | -39.38% |    -0.18 |       56 | 33.44%     | ok               |
|          35 | -19.75%  | 1.22%              | -43.69% |    -0.31 |       71 | 41.10%     | ok               |
|          30 | -22.16%  | 1.22%              | -43.40% |    -0.35 |       70 | 43.93%     | ok               |
|          40 | -23.67%  | 1.22%              | -46.46% |    -0.44 |       68 | 37.10%     | ok               |

## COST Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 12.77%   | 22.78%             | -24.32% |     0.43 |       64 | 47.59%     | ok               |
|          25 | 9.77%    | 22.78%             | -24.73% |     0.36 |       63 | 44.76%     | ok               |
|          35 | 6.16%    | 22.78%             | -27.54% |     0.27 |       58 | 39.10%     | ok               |
|          30 | 0.92%    | 22.78%             | -29.73% |     0.09 |       62 | 41.76%     | ok               |
|          15 | -1.96%   | 22.78%             | -27.30% |     0.02 |       67 | 51.08%     | ok               |

## CRM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | -22.07%  | -13.26%            | -34.06% |    -0.27 |       66 | 41.60%     | ok               |
|          15 | -30.10%  | -13.26%            | -47.54% |    -0.34 |       90 | 58.24%     | ok               |
|          40 | -26.73%  | -13.26%            | -40.30% |    -0.39 |       70 | 37.27%     | ok               |
|          50 | -21.91%  | -13.26%            | -38.24% |    -0.4  |       56 | 24.79%     | ok               |
|          30 | -31.08%  | -13.26%            | -44.86% |    -0.43 |       69 | 46.76%     | ok               |

## CRV-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 86.58%   | -42.03%            | -37.78% |     0.84 |       68 | 36.40%     | ok               |
|          40 | 54.58%   | -42.03%            | -38.86% |     0.67 |       58 | 31.99%     | ok               |
|          45 | 43.91%   | -42.03%            | -42.29% |     0.61 |       58 | 24.90%     | ok               |
|          50 | 42.93%   | -42.03%            | -30.73% |     0.61 |       50 | 20.88%     | ok               |
|          30 | 45.83%   | -42.03%            | -39.89% |     0.6  |       68 | 41.19%     | ok               |

## CSCO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 31.56%   | 128.81%            | -19.34% |     0.68 |       48 | 36.77%     | ok               |
|          45 | 27.11%   | 128.81%            | -19.34% |     0.59 |       50 | 38.44%     | ok               |
|          25 | 22.29%   | 128.81%            | -23.28% |     0.49 |       57 | 49.08%     | ok               |
|          35 | 18.25%   | 128.81%            | -23.68% |     0.43 |       54 | 45.26%     | ok               |
|          20 | 16.35%   | 128.81%            | -22.32% |     0.39 |       67 | 51.41%     | ok               |

## CVX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -8.19%   | 26.29%             | -24.33% |    -0.13 |       73 | 44.09%     | ok               |
|          40 | -7.29%   | 26.29%             | -27.34% |    -0.14 |       75 | 36.61%     | ok               |
|          45 | -7.69%   | 26.29%             | -28.83% |    -0.15 |       67 | 33.28%     | ok               |
|          35 | -10.31%  | 26.29%             | -28.85% |    -0.21 |       69 | 38.60%     | ok               |
|          20 | -13.33%  | 26.29%             | -27.54% |    -0.27 |       77 | 45.59%     | ok               |

## DASH-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 216.94%  | 175.55%            | -25.34% |     1.17 |       36 | 17.05%     | ok               |
|          40 | 129.14%  | 175.55%            | -25.65% |     0.91 |       42 | 22.80%     | ok               |
|          45 | 117.45%  | 175.55%            | -27.83% |     0.87 |       40 | 19.16%     | ok               |
|          30 | -12.34%  | 175.55%            | -64.43% |     0.29 |       55 | 29.89%     | ok               |
|          25 | -12.82%  | 175.55%            | -64.14% |     0.29 |       61 | 31.99%     | ok               |

## DBC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -0.44%   | 39.18%             | -26.70% |     0.05 |       79 | 39.77%     | ok               |
|          25 | -3.12%   | 39.18%             | -25.33% |    -0.04 |       64 | 36.44%     | ok               |
|          50 | -3.52%   | 39.18%             | -19.49% |    -0.08 |       50 | 24.29%     | ok               |
|          20 | -4.81%   | 39.18%             | -26.34% |    -0.09 |       71 | 38.10%     | ok               |
|          35 | -4.72%   | 39.18%             | -23.19% |    -0.1  |       64 | 33.44%     | ok               |

## DE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 3.90%    | 73.90%             | -17.97% |     0.18 |       58 | 29.78%     | ok               |
|          45 | -2.62%   | 73.90%             | -19.56% |     0.02 |       62 | 34.44%     | ok               |
|          20 | -8.19%   | 73.90%             | -24.13% |    -0.08 |       69 | 49.42%     | ok               |
|          25 | -13.50%  | 73.90%             | -24.97% |    -0.2  |       76 | 47.59%     | ok               |
|          30 | -14.49%  | 73.90%             | -25.41% |    -0.23 |       76 | 44.76%     | ok               |

## DIA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -1.59%   | 34.94%             | -11.28% |    -0.04 |       58 | 46.59%     | ok               |
|          35 | -3.49%   | 34.94%             | -13.15% |    -0.16 |       66 | 42.26%     | ok               |
|          20 | -4.30%   | 34.94%             | -13.60% |    -0.18 |       62 | 48.75%     | ok               |
|          30 | -4.94%   | 34.94%             | -12.94% |    -0.23 |       64 | 45.26%     | ok               |
|          40 | -6.68%   | 34.94%             | -15.06% |    -0.36 |       70 | 39.27%     | ok               |

## DIS Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 24.34%   | -8.92%             | -10.17% |     0.74 |       44 | 25.12%     | ok               |
|          40 | -4.77%   | -8.92%             | -18.75% |    -0.02 |       63 | 34.11%     | ok               |
|          45 | -4.62%   | -8.92%             | -16.54% |    -0.03 |       49 | 28.95%     | ok               |
|          15 | -11.99%  | -8.92%             | -31.15% |    -0.13 |       89 | 55.57%     | ok               |
|          35 | -12.84%  | -8.92%             | -25.70% |    -0.2  |       77 | 40.43%     | ok               |

## DOGE-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -5.94%   | -43.95%            | -59.36% |     0.22 |       78 | 63.22%     | ok               |
|          20 | -8.31%   | -43.95%            | -57.37% |     0.19 |       79 | 58.05%     | ok               |
|          25 | -16.24%  | -43.95%            | -55.33% |     0.1  |       71 | 54.02%     | ok               |
|          30 | -32.08%  | -43.95%            | -62.31% |    -0.12 |       72 | 47.89%     | ok               |
|          50 | -32.88%  | -43.95%            | -55.17% |    -0.28 |       58 | 23.75%     | ok               |

## DOT-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -58.84%  | -68.58%            | -66.32% |    -0.51 |       95 | 59.96%     | ok               |
|          15 | -62.70%  | -68.58%            | -72.06% |    -0.52 |       85 | 63.79%     | ok               |
|          30 | -59.26%  | -68.58%            | -64.69% |    -0.6  |       92 | 48.08%     | ok               |
|          45 | -46.81%  | -68.58%            | -53.90% |    -0.63 |       54 | 30.27%     | ok               |
|          50 | -44.30%  | -68.58%            | -49.03% |    -0.64 |       58 | 24.52%     | ok               |

## DXY-INDEX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -2.93%   | -5.63%             | -6.06%  |    -0.45 |       44 | 31.39%     | ok               |
|          40 | -4.31%   | -5.63%             | -7.30%  |    -0.56 |       68 | 46.97%     | ok               |
|          45 | -4.20%   | -5.63%             | -8.12%  |    -0.58 |       62 | 37.45%     | ok               |
|          15 | -8.04%   | -5.63%             | -11.81% |    -0.78 |       93 | 72.94%     | ok               |
|          30 | -6.87%   | -5.63%             | -9.98%  |    -0.82 |       76 | 57.14%     | ok               |

## EEM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -5.41%   | 62.81%             | -15.88% |    -0.14 |       54 | 34.11%     | ok               |
|          45 | -5.76%   | 62.81%             | -17.03% |    -0.15 |       52 | 35.61%     | ok               |
|          40 | -6.10%   | 62.81%             | -19.20% |    -0.15 |       64 | 37.77%     | ok               |
|          35 | -6.76%   | 62.81%             | -23.57% |    -0.16 |       66 | 39.77%     | ok               |
|          30 | -10.07%  | 62.81%             | -25.38% |    -0.27 |       62 | 41.60%     | ok               |

## EFA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -4.29%   | 34.65%             | -10.10% |    -0.1  |       62 | 50.42%     | ok               |
|          30 | -9.14%   | 34.65%             | -12.28% |    -0.34 |       58 | 42.76%     | ok               |
|          20 | -11.80%  | 34.65%             | -12.85% |    -0.43 |       71 | 47.42%     | ok               |
|          25 | -11.89%  | 34.65%             | -14.11% |    -0.45 |       64 | 44.76%     | ok               |
|          35 | -12.26%  | 34.65%             | -13.76% |    -0.48 |       58 | 41.76%     | ok               |

## EOG Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -22.05%  | 6.29%              | -38.89% |    -0.5  |       54 | 30.78%     | ok               |
|          50 | -24.51%  | 6.29%              | -37.65% |    -0.6  |       50 | 28.12%     | ok               |
|          40 | -27.95%  | 6.29%              | -40.83% |    -0.67 |       70 | 34.78%     | ok               |
|          30 | -31.44%  | 6.29%              | -48.55% |    -0.69 |       81 | 45.26%     | ok               |
|          35 | -32.10%  | 6.29%              | -44.69% |    -0.77 |       85 | 39.93%     | ok               |

## ETC-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -8.72%   | -44.97%            | -31.28% |    -0.04 |       28 | 15.90%     | ok               |
|          45 | -10.62%  | -44.97%            | -38.47% |    -0.06 |       28 | 17.82%     | ok               |
|          40 | -20.16%  | -44.97%            | -43.28% |    -0.24 |       38 | 20.69%     | ok               |
|          35 | -24.92%  | -44.97%            | -46.64% |    -0.3  |       48 | 24.52%     | ok               |
|          30 | -28.25%  | -44.97%            | -47.84% |    -0.34 |       62 | 28.16%     | ok               |

## ETH-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 174.10%  | 67.57%             | -30.11% |     1.43 |       58 | 46.17%     | ok               |
|          30 | 139.57%  | 67.57%             | -32.89% |     1.22 |       62 | 53.64%     | ok               |
|          25 | 99.23%   | 67.57%             | -40.90% |     0.99 |       62 | 57.66%     | ok               |
|          20 | 81.80%   | 67.57%             | -39.10% |     0.88 |       82 | 61.69%     | ok               |
|          15 | 74.86%   | 67.57%             | -42.74% |     0.82 |       75 | 67.43%     | ok               |

## EWJ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -24.14%  | 44.50%             | -30.00% |    -0.82 |       58 | 39.27%     | ok               |
|          30 | -23.51%  | 44.50%             | -29.40% |    -0.82 |       64 | 37.10%     | ok               |
|          45 | -22.48%  | 44.50%             | -25.77% |    -0.89 |       60 | 29.45%     | ok               |
|          15 | -27.78%  | 44.50%             | -31.15% |    -0.91 |       69 | 42.60%     | ok               |
|          25 | -26.33%  | 44.50%             | -29.85% |    -0.92 |       58 | 38.27%     | ok               |

## FCX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -1.04%   | 41.66%             | -31.00% |     0.12 |       54 | 32.11%     | ok               |
|          50 | -1.26%   | 41.66%             | -26.57% |     0.11 |       54 | 28.29%     | ok               |
|          40 | -13.12%  | 41.66%             | -42.89% |    -0.06 |       64 | 37.60%     | ok               |
|          30 | -27.17%  | 41.66%             | -46.84% |    -0.28 |       63 | 44.59%     | ok               |
|          35 | -31.65%  | 41.66%             | -50.12% |    -0.38 |       69 | 42.76%     | ok               |

## FET-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -15.32%  | -63.80%            | -64.89% |     0.14 |       88 | 51.92%     | ok               |
|          15 | -17.54%  | -63.80%            | -59.58% |     0.14 |       82 | 56.51%     | ok               |
|          25 | -23.91%  | -63.80%            | -65.31% |     0.03 |       81 | 45.02%     | ok               |
|          30 | -27.36%  | -63.80%            | -60.12% |    -0.04 |       75 | 40.23%     | ok               |
|          50 | -36.31%  | -63.80%            | -42.72% |    -0.6  |       42 | 11.69%     | ok               |

## FIL-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -48.93%  | -61.00%            | -57.27% |    -0.74 |       48 | 23.18%     | ok               |
|          30 | -56.67%  | -61.00%            | -58.98% |    -0.8  |       69 | 33.72%     | ok               |
|          50 | -47.71%  | -61.00%            | -48.84% |    -0.9  |       38 | 13.03%     | ok               |
|          35 | -57.42%  | -61.00%            | -61.90% |    -0.9  |       60 | 27.59%     | ok               |
|          15 | -70.51%  | -61.00%            | -72.08% |    -0.99 |       96 | 46.36%     | ok               |

## FXI Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -5.14%   | 32.66%             | -22.99% |    -0.04 |       50 | 33.78%     | ok               |
|          30 | -5.41%   | 32.66%             | -24.33% |    -0.05 |       48 | 32.28%     | ok               |
|          15 | -7.71%   | 32.66%             | -21.68% |    -0.09 |       52 | 37.60%     | ok               |
|          20 | -8.76%   | 32.66%             | -24.94% |    -0.13 |       52 | 35.61%     | ok               |
|          35 | -9.06%   | 32.66%             | -27.93% |    -0.15 |       50 | 29.78%     | ok               |

## GDX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 2.77%    | 176.11%            | -35.59% |     0.19 |       74 | 49.08%     | ok               |
|          40 | 0.63%    | 176.11%            | -31.37% |     0.14 |       62 | 38.77%     | ok               |
|          30 | -1.86%   | 176.11%            | -34.99% |     0.11 |       60 | 44.76%     | ok               |
|          35 | -5.59%   | 176.11%            | -31.88% |     0.04 |       70 | 41.60%     | ok               |
|          25 | -7.06%   | 176.11%            | -38.90% |     0.03 |       64 | 45.92%     | ok               |

## GDXJ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -25.98%  | 193.56%            | -44.73% |    -0.22 |       70 | 48.75%     | ok               |
|          50 | -28.83%  | 193.56%            | -46.83% |    -0.4  |       58 | 34.44%     | ok               |
|          30 | -35.93%  | 193.56%            | -44.61% |    -0.47 |       68 | 42.76%     | ok               |
|          35 | -37.59%  | 193.56%            | -41.76% |    -0.52 |       70 | 40.27%     | ok               |
|          25 | -40.21%  | 193.56%            | -46.95% |    -0.52 |       73 | 45.59%     | ok               |

## GE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -2.38%   | 93.58%             | -22.14% |     0.05 |       64 | 34.61%     | ok               |
|          20 | -12.51%  | 93.58%             | -25.05% |    -0.11 |       75 | 51.91%     | ok               |
|          45 | -10.25%  | 93.58%             | -25.54% |    -0.12 |       74 | 37.27%     | ok               |
|          30 | -15.50%  | 93.58%             | -27.82% |    -0.19 |       78 | 47.75%     | ok               |
|          25 | -17.21%  | 93.58%             | -29.91% |    -0.22 |       76 | 49.42%     | ok               |

## GLD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | 13.49%   | 85.20%             | -13.87% |     0.39 |       52 | 45.92%     | ok               |
|          20 | 11.53%   | 85.20%             | -13.87% |     0.35 |       55 | 47.75%     | ok               |
|          30 | 8.08%    | 85.20%             | -14.69% |     0.28 |       54 | 44.76%     | ok               |
|          35 | 5.22%    | 85.20%             | -15.36% |     0.21 |       56 | 42.43%     | ok               |
|          15 | 4.70%    | 85.20%             | -17.54% |     0.2  |       57 | 51.91%     | ok               |

## GOOGL Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 52.56%   | 103.28%            | -17.38% |     0.96 |       57 | 43.76%     | ok               |
|          30 | 48.87%   | 103.28%            | -17.63% |     0.89 |       55 | 47.25%     | ok               |
|          45 | 41.70%   | 103.28%            | -11.66% |     0.87 |       50 | 37.27%     | ok               |
|          25 | 46.60%   | 103.28%            | -16.96% |     0.85 |       55 | 49.75%     | ok               |
|          50 | 35.64%   | 103.28%            | -11.92% |     0.79 |       46 | 32.45%     | ok               |

## GRT-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 23.41%   | -70.94%            | -45.47% |     0.45 |       74 | 61.30%     | ok               |
|          50 | 14.75%   | -70.94%            | -31.62% |     0.38 |       44 | 18.58%     | ok               |
|          20 | 13.13%   | -70.94%            | -42.01% |     0.36 |       81 | 55.56%     | ok               |
|          45 | 12.69%   | -70.94%            | -39.70% |     0.34 |       48 | 25.10%     | ok               |
|          30 | 3.56%    | -70.94%            | -47.21% |     0.25 |       83 | 43.10%     | ok               |

## GS Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 22.06%   | 120.31%            | -20.56% |     0.49 |       66 | 55.57%     | ok               |
|          20 | 3.31%    | 120.31%            | -23.19% |     0.17 |       66 | 52.25%     | ok               |
|          40 | 3.29%    | 120.31%            | -17.88% |     0.16 |       64 | 41.76%     | ok               |
|          25 | -1.92%   | 120.31%            | -23.32% |     0.06 |       66 | 49.75%     | ok               |
|          30 | -3.01%   | 120.31%            | -22.13% |     0.03 |       66 | 47.42%     | ok               |

## HD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -3.21%   | -10.48%            | -18.17% |    -0    |       70 | 44.76%     | ok               |
|          30 | -3.22%   | -10.48%            | -17.37% |    -0.01 |       73 | 42.60%     | ok               |
|          35 | -7.21%   | -10.48%            | -19.29% |    -0.13 |       78 | 38.77%     | ok               |
|          45 | -5.90%   | -10.48%            | -16.42% |    -0.13 |       52 | 28.45%     | ok               |
|          40 | -7.16%   | -10.48%            | -17.26% |    -0.16 |       78 | 33.28%     | ok               |

## HON Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -11.33%  | 7.97%              | -23.16% |    -0.28 |       72 | 35.11%     | ok               |
|          45 | -14.25%  | 7.97%              | -25.06% |    -0.35 |       72 | 40.93%     | ok               |
|          30 | -23.51%  | 7.97%              | -33.57% |    -0.56 |       90 | 56.07%     | ok               |
|          35 | -23.14%  | 7.97%              | -31.82% |    -0.57 |       86 | 51.75%     | ok               |
|          40 | -24.57%  | 7.97%              | -33.77% |    -0.64 |       76 | 45.26%     | ok               |

## HYG Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -6.97%   | 2.49%              | -7.76%  |    -0.82 |       70 | 31.45%     | ok               |
|          35 | -8.47%   | 2.49%              | -9.66%  |    -1    |       79 | 33.28%     | ok               |
|          45 | -8.12%   | 2.49%              | -8.86%  |    -1    |       70 | 28.12%     | ok               |
|          30 | -8.95%   | 2.49%              | -10.69% |    -1.03 |       87 | 36.61%     | ok               |
|          15 | -9.63%   | 2.49%              | -11.42% |    -1.03 |       92 | 44.76%     | ok               |

## IBIT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 64.18%   | 21.07%             | -19.20% |     0.96 |       44 | 39.79%     | ok               |
|          50 | 51.64%   | 21.07%             | -17.37% |     0.96 |       24 | 23.58%     | ok               |
|          45 | 42.31%   | 21.07%             | -17.37% |     0.81 |       28 | 24.84%     | ok               |
|          40 | 35.94%   | 21.07%             | -17.78% |     0.72 |       28 | 26.74%     | ok               |
|          30 | 36.88%   | 21.07%             | -18.95% |     0.7  |       38 | 32.84%     | ok               |

## IBM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -20.25%  | 37.35%             | -49.43% |    -0.16 |       89 | 62.73%     | ok               |
|          35 | -24.24%  | 37.35%             | -47.10% |    -0.29 |       69 | 46.59%     | ok               |
|          30 | -25.87%  | 37.35%             | -48.94% |    -0.31 |       73 | 50.75%     | ok               |
|          20 | -30.94%  | 37.35%             | -53.45% |    -0.38 |       73 | 55.41%     | ok               |
|          50 | -29.24%  | 37.35%             | -45.88% |    -0.44 |       46 | 34.44%     | ok               |

## ICP-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 9.06%    | -37.42%            | -46.78% |     0.31 |       66 | 31.03%     | ok               |
|          40 | 8.40%    | -37.42%            | -40.71% |     0.3  |       58 | 26.44%     | ok               |
|          30 | 1.32%    | -37.42%            | -46.42% |     0.27 |       75 | 36.97%     | ok               |
|          50 | -11.08%  | -37.42%            | -50.31% |     0.02 |       40 | 16.28%     | ok               |
|          15 | -33.04%  | -37.42%            | -58.26% |    -0.01 |       77 | 48.47%     | ok               |

## IEF Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -7.58%   | -0.75%             | -10.32% |    -0.92 |       74 | 41.76%     | ok               |
|          15 | -8.13%   | -0.75%             | -11.04% |    -0.97 |       73 | 43.26%     | ok               |
|          40 | -8.55%   | -0.75%             | -10.38% |    -1.34 |       62 | 24.96%     | ok               |
|          50 | -7.74%   | -0.75%             | -9.11%  |    -1.35 |       56 | 20.63%     | ok               |
|          45 | -8.48%   | -0.75%             | -10.31% |    -1.37 |       56 | 23.63%     | ok               |

## IEMG Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -1.30%   | 57.64%             | -14.22% |     0.01 |       54 | 32.78%     | ok               |
|          45 | -2.11%   | 57.64%             | -15.23% |    -0.02 |       50 | 35.27%     | ok               |
|          40 | -3.62%   | 57.64%             | -18.73% |    -0.08 |       62 | 38.27%     | ok               |
|          35 | -6.11%   | 57.64%             | -24.91% |    -0.15 |       67 | 40.77%     | ok               |
|          30 | -10.97%  | 57.64%             | -29.43% |    -0.32 |       62 | 41.93%     | ok               |

## INJ-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 14.62%   | -2.91%             | -46.84% |     0.37 |       48 | 31.23%     | ok               |
|          35 | 13.11%   | -2.91%             | -53.43% |     0.36 |       56 | 33.91%     | ok               |
|          45 | 8.81%    | -2.91%             | -45.62% |     0.31 |       52 | 25.48%     | ok               |
|          30 | -30.25%  | -2.91%             | -73.61% |    -0.07 |       69 | 38.12%     | ok               |
|          50 | -21.33%  | -2.91%             | -43.46% |    -0.08 |       56 | 22.41%     | ok               |

## INTC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 73.50%   | 240.65%            | -49.32% |     0.73 |       58 | 33.28%     | ok               |
|          50 | 63.38%   | 240.65%            | -48.35% |     0.68 |       64 | 29.28%     | ok               |
|          15 | 63.72%   | 240.65%            | -53.65% |     0.65 |       80 | 59.90%     | ok               |
|          40 | 59.58%   | 240.65%            | -55.86% |     0.64 |       66 | 37.44%     | ok               |
|          25 | 47.31%   | 240.65%            | -56.41% |     0.57 |       79 | 50.75%     | ok               |

## INTU Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 6.40%    | -52.37%            | -36.76% |     0.23 |       65 | 26.62%     | ok               |
|          45 | -0.34%   | -52.37%            | -40.64% |     0.11 |       65 | 30.95%     | ok               |
|          40 | -6.98%   | -52.37%            | -44.15% |    -0.01 |       67 | 34.78%     | ok               |
|          25 | -10.11%  | -52.37%            | -39.10% |    -0.03 |       68 | 47.09%     | ok               |
|          15 | -13.56%  | -52.37%            | -43.23% |    -0.08 |       79 | 52.91%     | ok               |

## ITA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 3.48%    | 65.09%             | -21.48% |     0.18 |       72 | 38.94%     | ok               |
|          15 | -0.86%   | 65.09%             | -28.06% |     0.07 |       83 | 60.90%     | ok               |
|          30 | -0.77%   | 65.09%             | -23.75% |     0.06 |       72 | 49.08%     | ok               |
|          35 | -2.84%   | 65.09%             | -23.16% |    -0.01 |       74 | 46.76%     | ok               |
|          40 | -3.02%   | 65.09%             | -20.58% |    -0.02 |       74 | 43.43%     | ok               |

## IWM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | 12.85%   | 43.22%             | -12.34% |     0.5  |       54 | 37.27%     | ok               |
|          40 | 10.43%   | 43.22%             | -13.94% |     0.47 |       46 | 31.78%     | ok               |
|          30 | 11.41%   | 43.22%             | -12.65% |     0.46 |       54 | 36.44%     | ok               |
|          20 | 11.36%   | 43.22%             | -12.12% |     0.44 |       60 | 38.27%     | ok               |
|          35 | 8.46%    | 43.22%             | -13.94% |     0.37 |       54 | 34.28%     | ok               |

## JNJ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 16.00%   | 84.75%             | -10.57% |     0.67 |       48 | 34.78%     | ok               |
|          15 | 7.81%    | 84.75%             | -18.02% |     0.31 |       64 | 54.24%     | ok               |
|          45 | 5.14%    | 84.75%             | -13.35% |     0.25 |       50 | 38.77%     | ok               |
|          20 | 2.83%    | 84.75%             | -17.61% |     0.16 |       70 | 50.75%     | ok               |
|          40 | 1.61%    | 84.75%             | -14.77% |     0.12 |       58 | 43.09%     | ok               |

## JPM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 6.98%    | 80.72%             | -15.90% |     0.29 |       52 | 35.27%     | ok               |
|          45 | -3.18%   | 80.72%             | -21.91% |    -0.03 |       54 | 38.27%     | ok               |
|          20 | -18.88%  | 80.72%             | -35.58% |    -0.38 |       82 | 51.75%     | ok               |
|          35 | -16.00%  | 80.72%             | -27.43% |    -0.42 |       74 | 44.43%     | ok               |
|          40 | -16.47%  | 80.72%             | -28.47% |    -0.44 |       66 | 40.93%     | ok               |

## KO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 25.74%   | 42.94%             | -8.64%  |     0.9  |       54 | 39.77%     | ok               |
|          35 | 21.47%   | 42.94%             | -8.21%  |     0.78 |       58 | 38.27%     | ok               |
|          40 | 18.54%   | 42.94%             | -9.28%  |     0.73 |       60 | 34.94%     | ok               |
|          25 | 19.44%   | 42.94%             | -10.16% |     0.7  |       60 | 42.60%     | ok               |
|          20 | 6.26%    | 42.94%             | -15.99% |     0.27 |       77 | 46.76%     | ok               |

## LDO-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 40.03%   | -38.11%            | -43.36% |     0.57 |       80 | 54.98%     | ok               |
|          15 | 38.55%   | -38.11%            | -46.08% |     0.56 |       78 | 59.96%     | ok               |
|          30 | 13.86%   | -38.11%            | -59.60% |     0.39 |       72 | 46.36%     | ok               |
|          25 | 9.21%    | -38.11%            | -55.12% |     0.37 |       81 | 52.11%     | ok               |
|          35 | -1.87%   | -38.11%            | -61.97% |     0.24 |       76 | 38.51%     | ok               |

## LIN Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -7.45%   | 3.89%              | -23.68% |    -0.19 |       72 | 46.42%     | ok               |
|          20 | -7.48%   | 3.89%              | -23.00% |    -0.2  |       66 | 42.43%     | ok               |
|          25 | -7.43%   | 3.89%              | -22.01% |    -0.21 |       69 | 39.60%     | ok               |
|          30 | -10.91%  | 3.89%              | -20.61% |    -0.35 |       72 | 36.94%     | ok               |
|          35 | -11.14%  | 3.89%              | -19.70% |    -0.39 |       70 | 29.95%     | ok               |

## LINK-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 45.73%   | 0.95%              | -33.71% |     0.65 |       52 | 31.23%     | ok               |
|          30 | 45.80%   | 0.95%              | -33.64% |     0.62 |       73 | 45.79%     | ok               |
|          35 | 27.63%   | 0.95%              | -34.21% |     0.49 |       61 | 40.80%     | ok               |
|          50 | 22.51%   | 0.95%              | -27.44% |     0.44 |       46 | 25.29%     | ok               |
|          40 | 19.38%   | 0.95%              | -34.00% |     0.41 |       57 | 35.25%     | ok               |

## LLY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 1.18%    | 57.18%             | -38.23% |     0.13 |       46 | 35.27%     | ok               |
|          15 | -9.78%   | 57.18%             | -48.12% |    -0.01 |       65 | 59.23%     | ok               |
|          45 | -10.49%  | 57.18%             | -42.66% |    -0.09 |       52 | 38.60%     | ok               |
|          20 | -22.14%  | 57.18%             | -51.34% |    -0.26 |       72 | 54.41%     | ok               |
|          25 | -23.42%  | 57.18%             | -53.47% |    -0.29 |       68 | 51.75%     | ok               |

## LRCX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -13.68%  | 211.35%            | -48.71% |    -0.02 |       76 | 33.61%     | ok               |
|          40 | -18.39%  | 211.35%            | -55.33% |    -0.06 |       72 | 39.60%     | ok               |
|          35 | -19.96%  | 211.35%            | -58.47% |    -0.08 |       80 | 41.76%     | ok               |
|          15 | -27.52%  | 211.35%            | -56.69% |    -0.12 |       83 | 51.75%     | ok               |
|          30 | -25.21%  | 211.35%            | -61.08% |    -0.15 |       84 | 42.43%     | ok               |

## LTC-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 7.89%    | -22.72%            | -35.63% |     0.28 |       56 | 33.33%     | ok               |
|          35 | 5.21%    | -22.72%            | -34.94% |     0.25 |       70 | 43.87%     | ok               |
|          30 | -2.26%   | -22.72%            | -33.94% |     0.16 |       72 | 51.53%     | ok               |
|          25 | -9.25%   | -22.72%            | -34.22% |     0.08 |       76 | 54.21%     | ok               |
|          40 | -8.84%   | -22.72%            | -40.31% |     0.04 |       56 | 38.70%     | ok               |

## MCD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 4.94%    | -9.10%             | -9.22%  |     0.28 |       44 | 22.96%     | ok               |
|          45 | -2.99%   | -9.10%             | -16.79% |    -0.1  |       52 | 26.62%     | ok               |
|          30 | -4.76%   | -9.10%             | -21.88% |    -0.14 |       77 | 37.94%     | ok               |
|          40 | -4.29%   | -9.10%             | -18.49% |    -0.15 |       67 | 29.95%     | ok               |
|          25 | -5.28%   | -9.10%             | -23.62% |    -0.15 |       75 | 40.27%     | ok               |

## META Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -18.66%  | 50.18%             | -37.10% |    -0.28 |       68 | 37.77%     | ok               |
|          40 | -23.92%  | 50.18%             | -40.49% |    -0.38 |       70 | 41.26%     | ok               |
|          50 | -27.39%  | 50.18%             | -38.63% |    -0.52 |       70 | 33.44%     | ok               |
|          25 | -33.87%  | 50.18%             | -45.35% |    -0.57 |       77 | 51.41%     | ok               |
|          30 | -33.85%  | 50.18%             | -44.52% |    -0.59 |       78 | 48.42%     | ok               |

## MPC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 47.36%   | 114.17%            | -18.24% |     0.84 |       48 | 39.60%     | ok               |
|          45 | 38.01%   | 114.17%            | -19.46% |     0.71 |       54 | 43.26%     | ok               |
|          40 | 32.80%   | 114.17%            | -20.11% |     0.63 |       56 | 45.42%     | ok               |
|          35 | 28.69%   | 114.17%            | -31.08% |     0.56 |       64 | 47.92%     | ok               |
|          30 | 13.37%   | 114.17%            | -37.91% |     0.34 |       67 | 50.42%     | ok               |

## MRK Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -13.97%  | 11.94%             | -28.87% |    -0.18 |       85 | 53.58%     | ok               |
|          25 | -14.73%  | 11.94%             | -31.07% |    -0.22 |       72 | 45.76%     | ok               |
|          20 | -18.91%  | 11.94%             | -29.34% |    -0.31 |       77 | 49.08%     | ok               |
|          50 | -15.84%  | 11.94%             | -24.30% |    -0.33 |       58 | 30.28%     | ok               |
|          45 | -17.93%  | 11.94%             | -25.38% |    -0.37 |       59 | 33.61%     | ok               |

## MS Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 1.37%    | 118.23%            | -19.99% |     0.12 |       68 | 39.10%     | ok               |
|          15 | -3.01%   | 118.23%            | -22.02% |     0.03 |       70 | 56.91%     | ok               |
|          20 | -4.94%   | 118.23%            | -25.68% |    -0.03 |       73 | 52.41%     | ok               |
|          30 | -9.87%   | 118.23%            | -27.79% |    -0.16 |       73 | 47.59%     | ok               |
|          35 | -9.80%   | 118.23%            | -26.58% |    -0.17 |       74 | 44.09%     | ok               |

## MSFT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -15.77%  | 21.52%             | -25.23% |    -0.37 |       72 | 36.61%     | ok               |
|          50 | -21.68%  | 21.52%             | -26.37% |    -0.58 |       64 | 30.95%     | ok               |
|          35 | -28.51%  | 21.52%             | -36.02% |    -0.68 |       75 | 45.76%     | ok               |
|          30 | -30.50%  | 21.52%             | -37.80% |    -0.71 |       83 | 49.92%     | ok               |
|          40 | -28.54%  | 21.52%             | -35.43% |    -0.71 |       73 | 40.43%     | ok               |

## MU Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 198.76%  | 784.54%            | -64.30% |     1.2  |       54 | 49.08%     | ok               |
|          15 | 232.09%  | 784.54%            | -61.96% |     1.19 |       49 | 61.40%     | ok               |
|          25 | 175.56%  | 784.54%            | -67.90% |     1.1  |       49 | 55.57%     | ok               |
|          30 | 164.65%  | 784.54%            | -68.76% |     1.08 |       49 | 53.91%     | ok               |
|          35 | 157.20%  | 784.54%            | -69.35% |     1.06 |       61 | 51.58%     | ok               |

## NEAR-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 173.70%  | 114.82%            | -45.21% |     1.21 |       38 | 25.48%     | ok               |
|          40 | 175.54%  | 114.82%            | -51.95% |     1.21 |       40 | 29.50%     | ok               |
|          50 | 135.27%  | 114.82%            | -50.61% |     1.09 |       28 | 20.50%     | ok               |
|          35 | 122.65%  | 114.82%            | -56.29% |     1    |       62 | 34.29%     | ok               |
|          30 | 94.10%   | 114.82%            | -55.01% |     0.85 |       75 | 42.72%     | ok               |

## NEM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 4.89%    | 188.81%            | -31.25% |     0.23 |       58 | 60.40%     | ok               |
|          20 | 1.48%    | 188.81%            | -30.50% |     0.18 |       64 | 56.07%     | ok               |
|          25 | -14.76%  | 188.81%            | -39.51% |    -0.05 |       62 | 54.24%     | ok               |
|          50 | -18.07%  | 188.81%            | -32.97% |    -0.15 |       54 | 40.77%     | ok               |
|          30 | -25.45%  | 188.81%            | -39.56% |    -0.24 |       66 | 52.58%     | ok               |

## NFLX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 41.22%   | 27.92%             | -13.37% |     0.91 |       48 | 42.43%     | ok               |
|          50 | 37.08%   | 27.92%             | -16.28% |     0.89 |       44 | 34.78%     | ok               |
|          35 | 41.25%   | 27.92%             | -18.30% |     0.86 |       70 | 46.92%     | ok               |
|          45 | 25.95%   | 27.92%             | -15.48% |     0.65 |       54 | 38.94%     | ok               |
|          15 | 17.50%   | 27.92%             | -26.59% |     0.41 |       71 | 65.39%     | ok               |

## NKE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | -14.84%  | -62.27%            | -42.13% |    -0.13 |       69 | 38.60%     | ok               |
|          20 | -19.50%  | -62.27%            | -49.34% |    -0.15 |       83 | 50.92%     | ok               |
|          25 | -22.84%  | -62.27%            | -51.20% |    -0.21 |       83 | 48.25%     | ok               |
|          15 | -24.70%  | -62.27%            | -54.28% |    -0.24 |       86 | 54.74%     | ok               |
|          40 | -16.55%  | -62.27%            | -31.79% |    -0.25 |       63 | 30.62%     | ok               |

## NOW Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 6.41%    | -6.39%             | -30.43% |     0.25 |       86 | 50.58%     | ok               |
|          20 | 5.47%    | -6.39%             | -39.71% |     0.24 |       80 | 56.91%     | ok               |
|          25 | 1.40%    | -6.39%             | -37.51% |     0.2  |       78 | 54.08%     | ok               |
|          15 | -2.30%   | -6.39%             | -43.06% |     0.16 |       90 | 59.90%     | ok               |
|          40 | -5.24%   | -6.39%             | -36.21% |     0.08 |       78 | 40.27%     | ok               |

## NVDA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -29.07%  | 76.28%             | -41.21% |    -0.37 |       76 | 45.63%     | ok               |
|          20 | -38.50%  | 76.28%             | -45.26% |    -0.48 |       76 | 53.65%     | ok               |
|          25 | -38.40%  | 76.28%             | -45.17% |    -0.53 |       77 | 48.66%     | ok               |
|          15 | -45.16%  | 76.28%             | -52.37% |    -0.59 |       77 | 56.86%     | ok               |
|          35 | -40.59%  | 76.28%             | -48.32% |    -0.66 |       86 | 42.60%     | ok               |

## OP-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 28.55%   | -80.68%            | -31.68% |     0.55 |       30 | 9.39%      | ok               |
|          45 | 6.74%    | -80.68%            | -43.25% |     0.26 |       32 | 13.79%     | ok               |
|          40 | -12.56%  | -80.68%            | -53.61% |     0.02 |       44 | 21.46%     | ok               |
|          35 | -34.42%  | -80.68%            | -58.13% |    -0.3  |       54 | 26.25%     | ok               |
|          30 | -45.01%  | -80.68%            | -68.74% |    -0.4  |       68 | 32.57%     | ok               |

## ORCL Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 173.36%  | 25.94%             | -32.54% |     1.14 |       71 | 64.23%     | ok               |
|          25 | 119.79%  | 25.94%             | -27.76% |     0.95 |       63 | 56.74%     | ok               |
|          45 | 102.05%  | 25.94%             | -32.35% |     0.93 |       60 | 41.10%     | ok               |
|          20 | 113.66%  | 25.94%             | -29.32% |     0.92 |       72 | 59.90%     | ok               |
|          35 | 102.78%  | 25.94%             | -31.95% |     0.9  |       68 | 50.42%     | ok               |

## OXY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -3.13%   | -13.19%            | -29.80% |     0.07 |       71 | 42.60%     | ok               |
|          35 | -5.11%   | -13.19%            | -28.72% |     0.02 |       74 | 38.44%     | ok               |
|          50 | -6.31%   | -13.19%            | -27.98% |    -0.03 |       44 | 26.96%     | ok               |
|          40 | -10.96%  | -13.19%            | -30.46% |    -0.1  |       64 | 34.28%     | ok               |
|          25 | -16.53%  | -13.19%            | -39.52% |    -0.17 |       79 | 46.09%     | ok               |

## PEP Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 17.67%   | -26.10%            | -11.62% |     0.76 |       40 | 25.62%     | ok               |
|          45 | 10.16%   | -26.10%            | -14.22% |     0.45 |       56 | 29.62%     | ok               |
|          35 | 6.30%    | -26.10%            | -21.42% |     0.26 |       77 | 39.93%     | ok               |
|          40 | 4.01%    | -26.10%            | -18.04% |     0.2  |       70 | 35.27%     | ok               |
|          30 | 1.60%    | -26.10%            | -21.35% |     0.12 |       74 | 45.92%     | ok               |

## PEPE-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -43.08%  | -45.16%            | -64.84% |    -0.08 |       82 | 62.84%     | ok               |
|          30 | -39.87%  | -45.16%            | -57.66% |    -0.17 |       89 | 47.70%     | ok               |
|          25 | -41.37%  | -45.16%            | -53.88% |    -0.17 |       93 | 53.64%     | ok               |
|          35 | -38.97%  | -45.16%            | -54.42% |    -0.22 |       72 | 41.76%     | ok               |
|          20 | -48.68%  | -45.16%            | -64.07% |    -0.23 |       88 | 59.39%     | ok               |

## PFE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -15.95%  | 8.90%              | -22.71% |    -0.5  |       54 | 21.80%     | ok               |
|          50 | -16.49%  | 8.90%              | -24.78% |    -0.57 |       42 | 18.47%     | ok               |
|          40 | -22.54%  | 8.90%              | -28.85% |    -0.69 |       74 | 26.96%     | ok               |
|          35 | -29.42%  | 8.90%              | -34.85% |    -0.9  |       88 | 34.44%     | ok               |
|          30 | -37.94%  | 8.90%              | -42.69% |    -1.15 |       83 | 39.10%     | ok               |

## PG Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -10.43%  | -9.24%             | -19.77% |    -0.41 |       54 | 29.95%     | ok               |
|          35 | -13.49%  | -9.24%             | -18.66% |    -0.52 |       62 | 33.44%     | ok               |
|          30 | -21.35%  | -9.24%             | -24.25% |    -0.84 |       64 | 36.61%     | ok               |
|          45 | -19.18%  | -9.24%             | -22.13% |    -0.86 |       54 | 27.45%     | ok               |
|          25 | -23.14%  | -9.24%             | -25.94% |    -0.92 |       76 | 38.10%     | ok               |

## PM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 0.47%    | 98.51%             | -32.20% |     0.1  |       84 | 49.58%     | ok               |
|          20 | -2.15%   | 98.51%             | -33.51% |     0.05 |       83 | 58.24%     | ok               |
|          30 | -2.68%   | 98.51%             | -35.15% |     0.03 |       79 | 53.08%     | ok               |
|          40 | -7.20%   | 98.51%             | -37.94% |    -0.09 |       78 | 45.59%     | ok               |
|          50 | -6.71%   | 98.51%             | -35.70% |    -0.09 |       68 | 39.77%     | ok               |

## POL-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 47.30%   | -41.80%            | -39.52% |     0.64 |       87 | 49.62%     | ok               |
|          25 | 26.96%   | -41.80%            | -46.12% |     0.48 |       74 | 56.32%     | ok               |
|          20 | 11.13%   | -41.80%            | -52.88% |     0.35 |       82 | 60.54%     | ok               |
|          40 | 11.94%   | -41.80%            | -33.57% |     0.33 |       54 | 30.27%     | ok               |
|          50 | 10.26%   | -41.80%            | -26.14% |     0.3  |       48 | 20.50%     | ok               |

## QCOM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -5.22%   | 7.28%              | -55.66% |     0.11 |       71 | 45.26%     | ok               |
|          35 | -12.35%  | 7.28%              | -51.84% |    -0    |       77 | 40.93%     | ok               |
|          20 | -16.49%  | 7.28%              | -57.05% |    -0.04 |       70 | 48.59%     | ok               |
|          30 | -21.75%  | 7.28%              | -57.69% |    -0.14 |       75 | 43.26%     | ok               |
|          50 | -19.59%  | 7.28%              | -44.80% |    -0.18 |       58 | 27.62%     | ok               |

## QQQ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 27.72%   | 67.39%             | -14.17% |     0.67 |       65 | 54.58%     | ok               |
|          25 | 19.05%   | 67.39%             | -12.88% |     0.53 |       63 | 48.59%     | ok               |
|          20 | 17.83%   | 67.39%             | -12.98% |     0.49 |       71 | 51.25%     | ok               |
|          30 | 13.22%   | 67.39%             | -14.20% |     0.41 |       66 | 46.42%     | ok               |
|          35 | 1.58%    | 67.39%             | -20.59% |     0.12 |       72 | 42.60%     | ok               |

## RENDER-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 31.91%   | -55.60%            | -44.59% |     0.52 |       88 | 61.30%     | ok               |
|          20 | 30.93%   | -55.60%            | -43.43% |     0.52 |       93 | 57.66%     | ok               |
|          25 | 16.10%   | -55.60%            | -40.60% |     0.41 |       93 | 52.68%     | ok               |
|          30 | -29.76%  | -55.60%            | -44.84% |    -0.05 |      102 | 45.98%     | ok               |
|          35 | -31.71%  | -55.60%            | -43.79% |    -0.15 |       82 | 37.93%     | ok               |

## RTX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 43.70%   | 91.30%             | -18.66% |     0.9  |       74 | 57.24%     | ok               |
|          25 | 38.79%   | 91.30%             | -18.59% |     0.83 |       62 | 54.58%     | ok               |
|          30 | 35.19%   | 91.30%             | -16.99% |     0.78 |       60 | 52.75%     | ok               |
|          15 | 35.86%   | 91.30%             | -19.55% |     0.76 |       69 | 62.06%     | ok               |
|          35 | 27.02%   | 91.30%             | -18.00% |     0.7  |       54 | 49.75%     | ok               |

## SBUX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -3.72%   | 8.59%              | -23.55% |     0.02 |       53 | 40.43%     | ok               |
|          40 | -9.93%   | 8.59%              | -25.43% |    -0.15 |       62 | 33.28%     | ok               |
|          45 | -10.66%  | 8.59%              | -27.26% |    -0.2  |       64 | 28.95%     | ok               |
|          30 | -14.66%  | 8.59%              | -29.22% |    -0.24 |       58 | 38.44%     | ok               |
|          20 | -17.57%  | 8.59%              | -30.94% |    -0.27 |       58 | 42.10%     | ok               |

## SCHW Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -1.16%   | 40.35%             | -16.53% |     0.04 |       62 | 33.11%     | ok               |
|          25 | -3.30%   | 40.35%             | -28.76% |     0.02 |       65 | 49.42%     | ok               |
|          20 | -6.77%   | 40.35%             | -29.24% |    -0.06 |       73 | 51.91%     | ok               |
|          50 | -6.79%   | 40.35%             | -13.28% |    -0.18 |       58 | 30.12%     | ok               |
|          40 | -10.46%  | 40.35%             | -23.35% |    -0.22 |       68 | 36.61%     | ok               |

## SHIB-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -29.21%  | -54.90%            | -38.30% |    -0.16 |       75 | 59.58%     | ok               |
|          15 | -35.15%  | -54.90%            | -45.04% |    -0.23 |       85 | 67.62%     | ok               |
|          20 | -35.24%  | -54.90%            | -42.04% |    -0.25 |       79 | 62.84%     | ok               |
|          35 | -34.33%  | -54.90%            | -48.18% |    -0.32 |       72 | 45.40%     | ok               |
|          30 | -41.02%  | -54.90%            | -43.50% |    -0.42 |       82 | 52.11%     | ok               |

## SHY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd    |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:-------|---------:|---------:|:-----------|:-----------------|
|          30 | -1.90%   | 0.04%              | -3.18% |    -0.65 |       48 | 35.27%     | ok               |
|          35 | -2.15%   | 0.04%              | -3.49% |    -0.74 |       50 | 33.78%     | ok               |
|          40 | -2.23%   | 0.04%              | -3.58% |    -0.78 |       50 | 32.45%     | ok               |
|          45 | -2.31%   | 0.04%              | -3.43% |    -0.84 |       52 | 28.62%     | ok               |
|          25 | -2.77%   | 0.04%              | -4.32% |    -0.92 |       60 | 37.44%     | ok               |

## SKY-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -48.76%  | 21.93%             | -58.79% |    -0.65 |       85 | 45.49%     | ok               |
|          15 | -54.18%  | 21.93%             | -64.44% |    -0.68 |       71 | 54.70%     | ok               |
|          25 | -54.39%  | 21.93%             | -63.31% |    -0.76 |       78 | 48.94%     | ok               |
|          35 | -53.07%  | 21.93%             | -57.55% |    -0.85 |       78 | 37.81%     | ok               |
|          20 | -60.76%  | 21.93%             | -69.55% |    -0.88 |       73 | 52.21%     | ok               |

## SLB Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 11.43%   | 3.90%              | -25.36% |     0.33 |       60 | 32.45%     | ok               |
|          40 | 9.20%    | 3.90%              | -28.43% |     0.28 |       48 | 35.94%     | ok               |
|          50 | -1.79%   | 3.90%              | -29.27% |     0.05 |       48 | 27.79%     | ok               |
|          35 | -19.01%  | 3.90%              | -45.96% |    -0.28 |       70 | 43.09%     | ok               |
|          25 | -38.19%  | 3.90%              | -55.80% |    -0.71 |       84 | 53.58%     | ok               |

## SLV Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 44.14%   | 140.78%            | -34.72% |     0.66 |       54 | 30.78%     | ok               |
|          45 | 31.90%   | 140.78%            | -32.46% |     0.54 |       65 | 32.28%     | ok               |
|          40 | 30.32%   | 140.78%            | -34.28% |     0.52 |       71 | 34.44%     | ok               |
|          15 | 21.13%   | 140.78%            | -47.98% |     0.41 |       75 | 50.75%     | ok               |
|          20 | 20.30%   | 140.78%            | -42.66% |     0.41 |       74 | 45.42%     | ok               |

## SMH Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 86.99%   | 163.28%            | -31.66% |     1.13 |       49 | 47.92%     | ok               |
|          35 | 70.33%   | 163.28%            | -34.65% |     1.02 |       54 | 43.26%     | ok               |
|          25 | 69.26%   | 163.28%            | -33.57% |     1    |       46 | 46.59%     | ok               |
|          30 | 67.47%   | 163.28%            | -34.29% |     0.99 |       48 | 44.93%     | ok               |
|          45 | 55.28%   | 163.28%            | -33.35% |     0.93 |       54 | 37.44%     | ok               |

## SNX-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | -8.03%   | -63.06%            | -37.62% |     0.11 |       54 | 26.05%     | ok               |
|          20 | -16.18%  | -63.06%            | -47.56% |     0.07 |       71 | 42.53%     | ok               |
|          40 | -8.09%   | -63.06%            | -36.00% |     0.06 |       44 | 21.07%     | ok               |
|          30 | -21.09%  | -63.06%            | -47.16% |    -0.04 |       62 | 32.18%     | ok               |
|          15 | -41.51%  | -63.06%            | -49.47% |    -0.25 |       81 | 47.51%     | ok               |

## SOL-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 54.83%   | -16.92%            | -37.98% |     0.73 |       56 | 38.31%     | ok               |
|          35 | 26.39%   | -16.92%            | -43.70% |     0.48 |       68 | 45.02%     | ok               |
|          45 | 10.67%   | -16.92%            | -45.22% |     0.32 |       58 | 32.57%     | ok               |
|          25 | 8.14%    | -16.92%            | -41.09% |     0.31 |       70 | 58.24%     | ok               |
|          15 | 3.53%    | -16.92%            | -46.84% |     0.27 |       73 | 63.98%     | ok               |

## SOXX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | 75.64%   | 145.77%            | -39.32% |     1    |       55 | 45.59%     | ok               |
|          35 | 70.38%   | 145.77%            | -38.76% |     0.97 |       58 | 40.93%     | ok               |
|          30 | 69.47%   | 145.77%            | -39.81% |     0.95 |       56 | 43.26%     | ok               |
|          20 | 60.13%   | 145.77%            | -39.19% |     0.85 |       61 | 46.59%     | ok               |
|          40 | 48.85%   | 145.77%            | -41.03% |     0.78 |       58 | 38.77%     | ok               |

## SPY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 13.55%   | 49.86%             | -14.25% |     0.49 |       61 | 55.57%     | ok               |
|          15 | 13.00%   | 49.86%             | -16.80% |     0.46 |       65 | 58.24%     | ok               |
|          25 | 8.06%    | 49.86%             | -14.25% |     0.33 |       61 | 54.41%     | ok               |
|          30 | 3.49%    | 49.86%             | -15.53% |     0.18 |       64 | 51.58%     | ok               |
|          35 | 2.49%    | 49.86%             | -15.58% |     0.15 |       62 | 48.42%     | ok               |

## SUSHI-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -14.31%  | -55.51%            | -34.75% |    -0.06 |       58 | 14.94%     | ok               |
|          40 | -63.48%  | -55.51%            | -66.52% |    -0.88 |       63 | 25.86%     | ok               |
|          45 | -60.84%  | -55.51%            | -64.10% |    -0.88 |       60 | 19.73%     | ok               |
|          15 | -75.54%  | -55.51%            | -79.85% |    -0.92 |       89 | 48.66%     | ok               |
|          35 | -72.07%  | -55.51%            | -74.39% |    -1.07 |       86 | 31.23%     | ok               |

## T Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 65.73%   | 51.64%             | -15.08% |     1.15 |       71 | 67.39%     | ok               |
|          20 | 61.65%   | 51.64%             | -18.13% |     1.13 |       66 | 62.90%     | ok               |
|          25 | 57.27%   | 51.64%             | -17.66% |     1.08 |       66 | 60.57%     | ok               |
|          30 | 42.64%   | 51.64%             | -17.01% |     0.89 |       70 | 58.40%     | ok               |
|          35 | 27.09%   | 51.64%             | -14.49% |     0.65 |       76 | 54.08%     | ok               |

## TGT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -13.62%  | -3.98%             | -36.37% |    -0.23 |       62 | 37.94%     | ok               |
|          25 | -14.65%  | -3.98%             | -39.65% |    -0.23 |       68 | 40.60%     | ok               |
|          20 | -16.39%  | -3.98%             | -40.95% |    -0.24 |       86 | 45.26%     | ok               |
|          45 | -12.96%  | -3.98%             | -26.68% |    -0.25 |       52 | 28.79%     | ok               |
|          15 | -20.75%  | -3.98%             | -40.65% |    -0.32 |       76 | 50.25%     | ok               |

## TIA-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | -35.51%  | -81.92%            | -60.54% |    -0.22 |       70 | 33.33%     | ok               |
|          15 | -58.76%  | -81.92%            | -67.53% |    -0.34 |       96 | 58.43%     | ok               |
|          40 | -45.53%  | -81.92%            | -62.61% |    -0.44 |       74 | 27.39%     | ok               |
|          25 | -61.56%  | -81.92%            | -67.62% |    -0.51 |       92 | 46.74%     | ok               |
|          45 | -42.58%  | -81.92%            | -62.37% |    -0.55 |       56 | 18.20%     | ok               |

## TLT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -19.72%  | -7.92%             | -21.87% |    -1.45 |       72 | 34.11%     | ok               |
|          50 | -13.75%  | -7.92%             | -14.77% |    -1.6  |       34 | 15.64%     | ok               |
|          40 | -17.78%  | -7.92%             | -17.85% |    -1.6  |       54 | 23.96%     | ok               |
|          15 | -25.39%  | -7.92%             | -27.76% |    -1.71 |       79 | 42.26%     | ok               |
|          35 | -21.17%  | -7.92%             | -21.37% |    -1.78 |       66 | 28.12%     | ok               |

## TMO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 52.44%   | 13.57%             | -8.17%  |     1.12 |       46 | 33.94%     | ok               |
|          45 | 46.50%   | 13.57%             | -9.69%  |     0.98 |       50 | 38.77%     | ok               |
|          40 | 42.21%   | 13.57%             | -9.91%  |     0.89 |       55 | 43.59%     | ok               |
|          35 | 36.75%   | 13.57%             | -13.84% |     0.75 |       67 | 48.92%     | ok               |
|          20 | 30.35%   | 13.57%             | -22.89% |     0.61 |       76 | 60.40%     | ok               |

## TMUS Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 2.41%    | 2.57%              | -27.06% |     0.15 |       76 | 48.25%     | ok               |
|          15 | -1.02%   | 2.57%              | -34.48% |     0.08 |       68 | 60.90%     | ok               |
|          25 | -5.27%   | 2.57%              | -32.65% |    -0.01 |       79 | 51.08%     | ok               |
|          20 | -6.73%   | 2.57%              | -33.09% |    -0.04 |       74 | 55.24%     | ok               |
|          50 | -6.53%   | 2.57%              | -29.49% |    -0.11 |       60 | 34.94%     | ok               |

## TRX-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 19.40%   | 42.90%             | -18.79% |     0.62 |       54 | 40.42%     | ok               |
|          35 | 12.97%   | 42.90%             | -21.77% |     0.43 |       68 | 49.23%     | ok               |
|          20 | 12.33%   | 42.90%             | -25.45% |     0.39 |       61 | 59.39%     | ok               |
|          30 | 10.93%   | 42.90%             | -22.90% |     0.38 |       68 | 52.30%     | ok               |
|          25 | 8.24%    | 42.90%             | -26.84% |     0.3  |       66 | 55.94%     | ok               |

## TSLA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 41.91%   | 116.45%            | -30.57% |     0.61 |       62 | 29.78%     | ok               |
|          40 | 14.07%   | 116.45%            | -50.11% |     0.34 |       61 | 35.27%     | ok               |
|          45 | -10.25%  | 116.45%            | -52.01% |     0.07 |       67 | 32.28%     | ok               |
|          35 | -17.74%  | 116.45%            | -58.86% |     0    |       72 | 37.94%     | ok               |
|          30 | -35.03%  | 116.45%            | -58.36% |    -0.22 |       80 | 43.09%     | ok               |

## TXN Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 7.81%    | 50.24%             | -45.45% |     0.25 |       60 | 32.11%     | ok               |
|          35 | -10.27%  | 50.24%             | -45.21% |    -0.03 |       74 | 46.76%     | ok               |
|          40 | -11.18%  | 50.24%             | -47.43% |    -0.05 |       70 | 44.59%     | ok               |
|          45 | -11.69%  | 50.24%             | -46.24% |    -0.07 |       76 | 38.60%     | ok               |
|          20 | -17.23%  | 50.24%             | -40.96% |    -0.1  |       68 | 56.57%     | ok               |

## UNH Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 30.80%   | -23.91%            | -26.31% |     0.53 |       73 | 49.92%     | ok               |
|          50 | 28.37%   | -23.91%            | -36.71% |     0.53 |       52 | 29.28%     | ok               |
|          35 | 26.15%   | -23.91%            | -28.26% |     0.48 |       68 | 44.93%     | ok               |
|          15 | 22.54%   | -23.91%            | -29.48% |     0.43 |       79 | 65.06%     | ok               |
|          20 | 20.30%   | -23.91%            | -30.79% |     0.41 |       76 | 58.74%     | ok               |

## UNI-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 46.15%   | 70.89%             | -45.09% |     0.64 |       52 | 25.10%     | ok               |
|          45 | 34.20%   | 70.89%             | -51.70% |     0.54 |       58 | 32.76%     | ok               |
|          40 | 20.29%   | 70.89%             | -61.16% |     0.43 |       62 | 36.97%     | ok               |
|          35 | 2.44%    | 70.89%             | -65.47% |     0.29 |       74 | 42.72%     | ok               |
|          20 | -52.87%  | 70.89%             | -81.19% |    -0.27 |       97 | 58.24%     | ok               |

## UPS Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | -29.07%  | -32.88%            | -31.52% |    -0.55 |       62 | 34.28%     | ok               |
|          40 | -29.19%  | -32.88%            | -31.37% |    -0.57 |       58 | 28.95%     | ok               |
|          20 | -33.91%  | -32.88%            | -37.58% |    -0.63 |       84 | 47.25%     | ok               |
|          25 | -34.44%  | -32.88%            | -37.87% |    -0.66 |       76 | 43.93%     | ok               |
|          15 | -36.63%  | -32.88%            | -39.94% |    -0.69 |       88 | 51.25%     | ok               |

## USO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 17.17%   | 91.34%             | -32.35% |     0.38 |       46 | 25.96%     | ok               |
|          20 | 14.52%   | 91.34%             | -45.06% |     0.34 |       72 | 38.10%     | ok               |
|          25 | 10.50%   | 91.34%             | -44.76% |     0.29 |       68 | 35.77%     | ok               |
|          15 | 8.98%    | 91.34%             | -44.65% |     0.27 |       75 | 41.26%     | ok               |
|          30 | 7.86%    | 91.34%             | -42.37% |     0.25 |       70 | 33.11%     | ok               |

## VEA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 7.52%    | 46.03%             | -14.01% |     0.32 |       57 | 49.08%     | ok               |
|          20 | 1.27%    | 46.03%             | -15.76% |     0.1  |       61 | 46.42%     | ok               |
|          25 | -2.30%   | 46.03%             | -16.21% |    -0.04 |       57 | 44.76%     | ok               |
|          30 | -2.41%   | 46.03%             | -16.30% |    -0.05 |       58 | 43.43%     | ok               |
|          35 | -3.16%   | 46.03%             | -14.84% |    -0.08 |       56 | 42.26%     | ok               |

## VIXY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -55.17%  | -68.00%            | -69.78% |    -0.63 |       40 | 10.82%     | ok               |
|          15 | -75.88%  | -68.00%            | -89.47% |    -0.75 |       97 | 45.09%     | ok               |
|          45 | -64.78%  | -68.00%            | -75.03% |    -0.84 |       60 | 15.81%     | ok               |
|          30 | -76.58%  | -68.00%            | -88.17% |    -0.88 |       96 | 34.11%     | ok               |
|          20 | -80.72%  | -68.00%            | -90.58% |    -0.94 |       93 | 41.10%     | ok               |

## VNQ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -11.05%  | 15.91%             | -19.07% |    -0.5  |       60 | 28.29%     | ok               |
|          25 | -13.08%  | 15.91%             | -22.34% |    -0.5  |       73 | 41.93%     | ok               |
|          50 | -11.47%  | 15.91%             | -17.13% |    -0.54 |       56 | 25.79%     | ok               |
|          40 | -14.20%  | 15.91%             | -24.84% |    -0.62 |       78 | 33.11%     | ok               |
|          20 | -16.64%  | 15.91%             | -24.00% |    -0.64 |       76 | 45.26%     | ok               |

## VTI Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 14.24%   | 49.11%             | -13.96% |     0.51 |       64 | 56.07%     | ok               |
|          15 | 9.54%    | 49.11%             | -15.70% |     0.36 |       61 | 58.40%     | ok               |
|          25 | 1.65%    | 49.11%             | -15.00% |     0.12 |       60 | 53.74%     | ok               |
|          30 | -5.97%   | 49.11%             | -17.64% |    -0.16 |       70 | 51.75%     | ok               |
|          40 | -7.10%   | 49.11%             | -19.77% |    -0.22 |       74 | 44.26%     | ok               |

## VWO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -11.39%  | 41.80%             | -23.73% |    -0.35 |       74 | 48.09%     | ok               |
|          45 | -9.75%   | 41.80%             | -23.75% |    -0.36 |       58 | 32.28%     | ok               |
|          40 | -10.21%  | 41.80%             | -23.57% |    -0.37 |       68 | 35.11%     | ok               |
|          50 | -10.11%  | 41.80%             | -23.51% |    -0.38 |       56 | 29.45%     | ok               |
|          20 | -12.80%  | 41.80%             | -25.88% |    -0.42 |       71 | 45.76%     | ok               |

## VZ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 0.82%    | 21.19%             | -12.55% |     0.09 |       54 | 27.95%     | ok               |
|          25 | -11.39%  | 21.19%             | -22.13% |    -0.26 |       78 | 45.42%     | ok               |
|          35 | -10.26%  | 21.19%             | -22.73% |    -0.26 |       60 | 37.44%     | ok               |
|          45 | -10.75%  | 21.19%             | -21.44% |    -0.29 |       66 | 31.78%     | ok               |
|          40 | -15.28%  | 21.19%             | -24.21% |    -0.45 |       64 | 34.78%     | ok               |

## WFC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | -7.00%   | 43.75%             | -21.57% |    -0.08 |       75 | 43.93%     | ok               |
|          50 | -4.95%   | 43.75%             | -18.29% |    -0.09 |       58 | 32.28%     | ok               |
|          20 | -18.09%  | 43.75%             | -29.87% |    -0.26 |       77 | 52.41%     | ok               |
|          30 | -16.69%  | 43.75%             | -28.90% |    -0.27 |       78 | 47.09%     | ok               |
|          40 | -12.75%  | 43.75%             | -23.94% |    -0.3  |       70 | 40.60%     | ok               |

## WIF-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 68.08%   | -49.54%            | -40.67% |     0.7  |       67 | 43.87%     | ok               |
|          15 | 31.35%   | -49.54%            | -46.21% |     0.51 |       77 | 47.13%     | ok               |
|          25 | 0.90%    | -49.54%            | -44.74% |     0.29 |       69 | 39.46%     | ok               |
|          30 | -26.92%  | -49.54%            | -52.76% |    -0.02 |       66 | 35.63%     | ok               |
|          50 | -12.18%  | -49.54%            | -34.40% |    -0.04 |       32 | 11.30%     | ok               |

## WMT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 38.72%   | 77.41%             | -11.62% |     1.11 |       40 | 39.10%     | ok               |
|          50 | 33.90%   | 77.41%             | -12.19% |     1.05 |       32 | 36.77%     | ok               |
|          35 | 29.02%   | 77.41%             | -16.55% |     0.83 |       56 | 45.26%     | ok               |
|          40 | 27.36%   | 77.41%             | -15.99% |     0.82 |       48 | 40.60%     | ok               |
|          15 | 12.05%   | 77.41%             | -25.74% |     0.35 |       76 | 58.57%     | ok               |

## XBI Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 15.04%   | 87.71%             | -16.08% |     0.43 |       54 | 36.77%     | ok               |
|          45 | 10.67%   | 87.71%             | -15.46% |     0.34 |       52 | 34.28%     | ok               |
|          35 | 2.82%    | 87.71%             | -16.96% |     0.15 |       64 | 40.10%     | ok               |
|          50 | 2.21%    | 87.71%             | -15.97% |     0.14 |       54 | 30.78%     | ok               |
|          30 | 0.68%    | 87.71%             | -18.30% |     0.1  |       66 | 41.60%     | ok               |

## XLB Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -2.33%   | 11.68%             | -18.27% |    -0.04 |       54 | 26.79%     | ok               |
|          50 | -3.17%   | 11.68%             | -16.40% |    -0.08 |       38 | 22.96%     | ok               |
|          45 | -4.96%   | 11.68%             | -18.10% |    -0.16 |       42 | 24.29%     | ok               |
|          35 | -5.65%   | 11.68%             | -21.38% |    -0.16 |       54 | 30.28%     | ok               |
|          25 | -10.56%  | 11.68%             | -23.37% |    -0.35 |       62 | 35.61%     | ok               |

## XLC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 14.20%   | 38.32%             | -12.33% |     0.52 |       63 | 50.58%     | ok               |
|          25 | 13.65%   | 38.32%             | -12.31% |     0.5  |       62 | 52.75%     | ok               |
|          50 | 7.28%    | 38.32%             | -11.12% |     0.38 |       66 | 38.60%     | ok               |
|          20 | 9.17%    | 38.32%             | -14.06% |     0.35 |       67 | 55.07%     | ok               |
|          40 | 7.86%    | 38.32%             | -13.38% |     0.34 |       64 | 44.09%     | ok               |

## XLE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -1.77%   | 34.34%             | -25.98% |     0.03 |       54 | 35.94%     | ok               |
|          35 | -9.62%   | 34.34%             | -30.52% |    -0.17 |       69 | 42.76%     | ok               |
|          45 | -9.47%   | 34.34%             | -29.68% |    -0.2  |       62 | 38.10%     | ok               |
|          30 | -13.13%  | 34.34%             | -34.24% |    -0.26 |       73 | 44.59%     | ok               |
|          25 | -14.19%  | 34.34%             | -35.04% |    -0.27 |       83 | 47.59%     | ok               |

## XLF Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -3.46%   | 36.84%             | -18.63% |    -0.05 |       70 | 50.92%     | ok               |
|          15 | -6.17%   | 36.84%             | -20.19% |    -0.15 |       76 | 53.08%     | ok               |
|          25 | -8.93%   | 36.84%             | -23.22% |    -0.26 |       79 | 47.75%     | ok               |
|          30 | -9.53%   | 36.84%             | -23.61% |    -0.3  |       80 | 45.76%     | ok               |
|          35 | -16.57%  | 36.84%             | -24.48% |    -0.64 |       70 | 42.10%     | ok               |

## XLI Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 7.85%    | 38.39%             | -11.40% |     0.32 |       84 | 49.58%     | ok               |
|          20 | 3.95%    | 38.39%             | -12.74% |     0.2  |       73 | 44.59%     | ok               |
|          25 | -5.25%   | 38.39%             | -15.60% |    -0.15 |       74 | 42.76%     | ok               |
|          50 | -4.73%   | 38.39%             | -14.94% |    -0.18 |       60 | 31.78%     | ok               |
|          30 | -5.83%   | 38.39%             | -14.16% |    -0.18 |       76 | 41.76%     | ok               |

## XLK Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | 77.98%   | 89.76%             | -14.75% |     1.33 |       40 | 48.92%     | ok               |
|          20 | 81.41%   | 89.76%             | -14.75% |     1.33 |       46 | 50.92%     | ok               |
|          15 | 79.56%   | 89.76%             | -14.75% |     1.27 |       46 | 52.75%     | ok               |
|          30 | 67.33%   | 89.76%             | -14.75% |     1.23 |       40 | 47.59%     | ok               |
|          35 | 50.42%   | 89.76%             | -13.43% |     1.02 |       54 | 44.93%     | ok               |

## XLM-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -6.21%   | -17.46%            | -48.81% |     0.09 |       46 | 25.67%     | ok               |
|          45 | -7.26%   | -17.46%            | -51.28% |     0.09 |       56 | 30.65%     | ok               |
|          25 | -11.65%  | -17.46%            | -49.14% |     0.09 |       71 | 49.04%     | ok               |
|          30 | -15.27%  | -17.46%            | -54.58% |     0.03 |       67 | 45.98%     | ok               |
|          40 | -19.45%  | -17.46%            | -47.28% |    -0.05 |       53 | 35.82%     | ok               |

## XLP Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 10.97%   | 9.54%              | -5.66%  |     0.69 |       50 | 30.12%     | ok               |
|          40 | 8.73%    | 9.54%              | -7.77%  |     0.54 |       66 | 34.28%     | ok               |
|          50 | 7.86%    | 9.54%              | -6.08%  |     0.52 |       54 | 28.45%     | ok               |
|          35 | 7.79%    | 9.54%              | -9.73%  |     0.48 |       62 | 37.27%     | ok               |
|          30 | 6.92%    | 9.54%              | -10.28% |     0.42 |       64 | 38.94%     | ok               |

## XLU Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 6.24%    | 24.19%             | -13.94% |     0.34 |       54 | 30.45%     | ok               |
|          45 | 5.07%    | 24.19%             | -14.88% |     0.28 |       58 | 31.61%     | ok               |
|          40 | 1.90%    | 24.19%             | -16.41% |     0.13 |       64 | 33.44%     | ok               |
|          35 | -0.81%   | 24.19%             | -19.71% |     0.01 |       64 | 36.11%     | ok               |
|          30 | -2.19%   | 24.19%             | -20.40% |    -0.05 |       69 | 39.43%     | ok               |

## XLV Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -15.89%  | 20.31%             | -19.60% |    -0.73 |       70 | 37.44%     | ok               |
|          25 | -16.80%  | 20.31%             | -21.14% |    -0.76 |       72 | 39.60%     | ok               |
|          20 | -20.06%  | 20.31%             | -24.51% |    -0.92 |       75 | 41.26%     | ok               |
|          15 | -20.58%  | 20.31%             | -24.84% |    -0.92 |       81 | 43.93%     | ok               |
|          35 | -20.06%  | 20.31%             | -23.39% |    -1    |       66 | 34.78%     | ok               |

## XLY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -1.52%   | 26.24%             | -15.77% |     0.04 |       80 | 52.91%     | ok               |
|          30 | -6.07%   | 26.24%             | -17.65% |    -0.12 |       79 | 46.42%     | ok               |
|          20 | -6.73%   | 26.24%             | -19.25% |    -0.12 |       76 | 49.58%     | ok               |
|          25 | -8.81%   | 26.24%             | -19.29% |    -0.19 |       73 | 48.09%     | ok               |
|          50 | -7.78%   | 26.24%             | -14.85% |    -0.28 |       62 | 31.28%     | ok               |

## XOM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | 1.49%    | 38.64%             | -19.90% |     0.12 |       57 | 35.11%     | ok               |
|          30 | 0.48%    | 38.64%             | -20.29% |     0.09 |       57 | 34.44%     | ok               |
|          50 | 0.63%    | 38.64%             | -21.35% |     0.09 |       36 | 26.96%     | ok               |
|          45 | -3.17%   | 38.64%             | -23.33% |    -0.02 |       42 | 28.29%     | ok               |
|          40 | -4.60%   | 38.64%             | -21.45% |    -0.06 |       52 | 31.61%     | ok               |

## XRP-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 23.51%   | -31.16%            | -31.38% |     0.45 |       70 | 43.10%     | ok               |
|          40 | 9.21%    | -31.16%            | -33.91% |     0.3  |       60 | 36.59%     | ok               |
|          30 | 4.01%    | -31.16%            | -31.82% |     0.25 |       65 | 47.89%     | ok               |
|          45 | -1.97%   | -31.16%            | -36.27% |     0.16 |       58 | 32.18%     | ok               |
|          20 | -8.04%   | -31.16%            | -38.12% |     0.12 |       77 | 55.94%     | ok               |

## YFI-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -50.04%  | -50.48%            | -50.04% |    -0.87 |       56 | 26.82%     | ok               |
|          45 | -50.12%  | -50.48%            | -50.12% |    -1.12 |       70 | 21.46%     | ok               |
|          35 | -63.96%  | -50.48%            | -66.31% |    -1.16 |       65 | 34.10%     | ok               |
|          30 | -67.41%  | -50.48%            | -72.54% |    -1.21 |       77 | 38.12%     | ok               |
|          15 | -72.94%  | -50.48%            | -76.87% |    -1.29 |       85 | 50.19%     | ok               |

## ZEC-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 244.27%  | 4832.71%           | -30.64% |     1.18 |       46 | 30.84%     | ok               |
|          35 | 218.64%  | 4832.71%           | -50.84% |     1.1  |       50 | 37.55%     | ok               |
|          25 | 203.46%  | 4832.71%           | -58.07% |     1.04 |       56 | 44.64%     | ok               |
|          30 | 183.18%  | 4832.71%           | -56.50% |     1.01 |       64 | 41.76%     | ok               |
|          20 | 154.25%  | 4832.71%           | -62.70% |     0.93 |       63 | 46.74%     | ok               |
