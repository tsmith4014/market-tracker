# Market Tracker Backtest Report

_Generated: 2026-06-12T01:40:44+00:00_

## Data Sources

- Crypto: Kraken -> Coinbase -> CoinGecko OHLC -> CoinPaprika fallback chain.
- Stocks / ETFs / indices: Stooq -> Yahoo Finance fallback chain.
- Data rows are generated from real market APIs. Mock OHLCV rows are not generated.

## Data Freshness

- Rows: **92,381**
- Symbols: **161**
- Date range: **2024-01-19** to **2026-06-12**

## Latest Signals

| symbol     | date                |         close |   composite_score | signal   | data_source   |
|:-----------|:--------------------|--------------:|------------------:|:---------|:--------------|
| ABBV       | 2026-06-11 00:00:00 |   224.77      |        56.4167    | LONG     | Yahoo Finance |
| BAC        | 2026-06-11 00:00:00 |    55.16      |        53.25      | LONG     | Yahoo Finance |
| C          | 2026-06-11 00:00:00 |   138.07      |        71.25      | LONG     | Yahoo Finance |
| CRV-USD    | 2026-06-12 00:00:00 |     0.25534   |        34.6667    | LONG     | Kraken API    |
| CSCO       | 2026-06-11 00:00:00 |   121.83      |        54.5833    | LONG     | Yahoo Finance |
| DE         | 2026-06-11 00:00:00 |   568.64      |        58.0833    | LONG     | Yahoo Finance |
| DIA        | 2026-06-11 00:00:00 |   509.36      |        42.25      | LONG     | Yahoo Finance |
| DXY-INDEX  | 2026-06-11 00:00:00 |    99.824     |        80.3763    | LONG     | Yahoo Finance |
| GE         | 2026-06-11 00:00:00 |   332.76      |        63.9167    | LONG     | Yahoo Finance |
| GS         | 2026-06-11 00:00:00 |  1035.64      |        45.5833    | LONG     | Yahoo Finance |
| IBM        | 2026-06-11 00:00:00 |   274.85      |        39.5833    | LONG     | Yahoo Finance |
| ITA        | 2026-06-11 00:00:00 |   236.04      |        63.9167    | LONG     | Yahoo Finance |
| JPM        | 2026-06-11 00:00:00 |   313.49      |        58.6667    | LONG     | Yahoo Finance |
| LLY        | 2026-06-11 00:00:00 |  1160.95      |        74.0833    | LONG     | Yahoo Finance |
| LRCX       | 2026-06-11 00:00:00 |   362.52      |        73.4167    | LONG     | Yahoo Finance |
| MRK        | 2026-06-11 00:00:00 |   120.76      |        74.0833    | LONG     | Yahoo Finance |
| MS         | 2026-06-11 00:00:00 |   212.66      |        45.5833    | LONG     | Yahoo Finance |
| MU         | 2026-06-11 00:00:00 |   995.87      |        52.75      | LONG     | Yahoo Finance |
| PG         | 2026-06-11 00:00:00 |   148.34      |        54.0833    | LONG     | Yahoo Finance |
| PM         | 2026-06-11 00:00:00 |   180.77      |        36.0833    | LONG     | Yahoo Finance |
| QQQ        | 2026-06-11 00:00:00 |   717.12      |        45.25      | LONG     | Yahoo Finance |
| SBUX       | 2026-06-11 00:00:00 |   102.28      |        31.4167    | LONG     | Yahoo Finance |
| UNH        | 2026-06-11 00:00:00 |   405.55      |        72.0833    | LONG     | Yahoo Finance |
| UPS        | 2026-06-11 00:00:00 |   108.65      |        74.0833    | LONG     | Yahoo Finance |
| WFC        | 2026-06-11 00:00:00 |    82.4       |        52.75      | LONG     | Yahoo Finance |
| XLK        | 2026-06-11 00:00:00 |   183.21      |        47.0833    | LONG     | Yahoo Finance |
| AAPL       | 2026-06-11 00:00:00 |   295.63      |         0.916667  | NEUTRAL  | Yahoo Finance |
| ADBE       | 2026-06-11 00:00:00 |   218.8       |       -66.75      | NEUTRAL  | Yahoo Finance |
| AGG        | 2026-06-11 00:00:00 |    98.88      |        -0.0833333 | NEUTRAL  | Yahoo Finance |
| ALGO-USD   | 2026-06-12 00:00:00 |     0.08856   |       -66.5833    | NEUTRAL  | Kraken API    |
| AMAT       | 2026-06-11 00:00:00 |   552.64      |        60.5       | NEUTRAL  | Yahoo Finance |
| AMD        | 2026-06-11 00:00:00 |   488.45      |        41         | NEUTRAL  | Yahoo Finance |
| AMGN       | 2026-06-11 00:00:00 |   354.06      |        69.6667    | NEUTRAL  | Yahoo Finance |
| AMZN       | 2026-06-11 00:00:00 |   241.51      |       -14.8333    | NEUTRAL  | Yahoo Finance |
| ARKK       | 2026-06-11 00:00:00 |    75.46      |       -29.5833    | NEUTRAL  | Yahoo Finance |
| ATOM-USD   | 2026-06-12 00:00:00 |     1.9831    |        11.9167    | NEUTRAL  | Kraken API    |
| AVGO       | 2026-06-11 00:00:00 |   385.57      |       -44.25      | NEUTRAL  | Yahoo Finance |
| BA         | 2026-06-11 00:00:00 |   221.63      |        29.0833    | NEUTRAL  | Yahoo Finance |
| BND        | 2026-06-11 00:00:00 |    73.33      |        -0.0833333 | NEUTRAL  | Yahoo Finance |
| CAT        | 2026-06-11 00:00:00 |   897.63      |        39.3333    | NEUTRAL  | Yahoo Finance |
| CL         | 2026-06-11 00:00:00 |    89.39      |        34.0833    | NEUTRAL  | Yahoo Finance |
| CMCSA      | 2026-06-11 00:00:00 |    23.97      |       -14.9167    | NEUTRAL  | Yahoo Finance |
| COMP-USD   | 2026-06-12 00:00:00 |    17.72      |        -1.33333   | NEUTRAL  | Kraken API    |
| COP        | 2026-06-11 00:00:00 |   115.36      |       -10.25      | NEUTRAL  | Yahoo Finance |
| COST       | 2026-06-11 00:00:00 |   975.69      |       -15.1667    | NEUTRAL  | Yahoo Finance |
| CRM        | 2026-06-11 00:00:00 |   166.45      |       -63.6667    | NEUTRAL  | Yahoo Finance |
| CVX        | 2026-06-11 00:00:00 |   185.82      |       -10.25      | NEUTRAL  | Yahoo Finance |
| DBC        | 2026-06-11 00:00:00 |    28.85      |       -17.4167    | NEUTRAL  | Yahoo Finance |
| EEM        | 2026-06-11 00:00:00 |    67.5       |        37.5       | NEUTRAL  | Yahoo Finance |
| EFA        | 2026-06-11 00:00:00 |   104.73      |        14.5       | NEUTRAL  | Yahoo Finance |
| EOG        | 2026-06-11 00:00:00 |   136.53      |        -2.66667   | NEUTRAL  | Yahoo Finance |
| EWJ        | 2026-06-11 00:00:00 |    92.18      |        21.5       | NEUTRAL  | Yahoo Finance |
| FCX        | 2026-06-11 00:00:00 |    66.34      |        43         | NEUTRAL  | Yahoo Finance |
| FET-USD    | 2026-06-12 00:00:00 |     0.191     |       -43         | NEUTRAL  | Kraken API    |
| GOOGL      | 2026-06-11 00:00:00 |   357.77      |       -17.8333    | NEUTRAL  | Yahoo Finance |
| HD         | 2026-06-11 00:00:00 |   326.01      |        19         | NEUTRAL  | Yahoo Finance |
| HON        | 2026-06-11 00:00:00 |   219.12      |       -11         | NEUTRAL  | Yahoo Finance |
| HYG        | 2026-06-11 00:00:00 |    79.94      |        -4.83333   | NEUTRAL  | Yahoo Finance |
| IEF        | 2026-06-11 00:00:00 |    94.34      |        -2.33333   | NEUTRAL  | Yahoo Finance |
| IEMG       | 2026-06-11 00:00:00 |    82.07      |        37.5       | NEUTRAL  | Yahoo Finance |
| INJ-USD    | 2026-06-12 00:00:00 |     5.401     |        12.4167    | NEUTRAL  | Kraken API    |
| INTC       | 2026-06-11 00:00:00 |   116.96      |        36.3333    | NEUTRAL  | Yahoo Finance |
| IWM        | 2026-06-11 00:00:00 |   290.41      |        40.8333    | NEUTRAL  | Yahoo Finance |
| JNJ        | 2026-06-11 00:00:00 |   238.33      |        61.1667    | NEUTRAL  | Yahoo Finance |
| KO         | 2026-06-11 00:00:00 |    82.53      |        55.8333    | NEUTRAL  | Yahoo Finance |
| LIN        | 2026-06-11 00:00:00 |   515.44      |        52.8333    | NEUTRAL  | Yahoo Finance |
| MCD        | 2026-06-11 00:00:00 |   284.77      |        -4.5       | NEUTRAL  | Yahoo Finance |
| META       | 2026-06-11 00:00:00 |   568.43      |       -69         | NEUTRAL  | Yahoo Finance |
| MPC        | 2026-06-11 00:00:00 |   260.81      |        47.5       | NEUTRAL  | Yahoo Finance |
| NEAR-USD   | 2026-06-12 00:00:00 |     2.0371    |        10.4167    | NEUTRAL  | Kraken API    |
| NFLX       | 2026-06-11 00:00:00 |    81.27      |       -72.3333    | NEUTRAL  | Yahoo Finance |
| NKE        | 2026-06-11 00:00:00 |    45.96      |         1         | NEUTRAL  | Yahoo Finance |
| NVDA       | 2026-06-11 00:00:00 |   204.87      |       -33.8333    | NEUTRAL  | Yahoo Finance |
| OXY        | 2026-06-11 00:00:00 |    55.47      |       -25.25      | NEUTRAL  | Yahoo Finance |
| PEP        | 2026-06-11 00:00:00 |   143.73      |       -24.25      | NEUTRAL  | Yahoo Finance |
| PFE        | 2026-06-11 00:00:00 |    26.17      |        44.75      | NEUTRAL  | Yahoo Finance |
| QCOM       | 2026-06-11 00:00:00 |   202.96      |         3.41667   | NEUTRAL  | Yahoo Finance |
| RENDER-USD | 2026-06-12 00:00:00 |     1.626     |       -50.3333    | NEUTRAL  | Kraken API    |
| RTX        | 2026-06-11 00:00:00 |   184.21      |        40.75      | NEUTRAL  | Yahoo Finance |
| SCHW       | 2026-06-11 00:00:00 |    88.7       |       -46         | NEUTRAL  | Yahoo Finance |
| SHY        | 2026-06-11 00:00:00 |    82.09      |       -15.9167    | NEUTRAL  | Yahoo Finance |
| SLB        | 2026-06-11 00:00:00 |    56         |        16.1667    | NEUTRAL  | Yahoo Finance |
| SMH        | 2026-06-11 00:00:00 |   609.45      |        37.5       | NEUTRAL  | Yahoo Finance |
| SOXX       | 2026-06-11 00:00:00 |   586.93      |        41         | NEUTRAL  | Yahoo Finance |
| SPY        | 2026-06-11 00:00:00 |   737.76      |         4.58333   | NEUTRAL  | Yahoo Finance |
| SUSHI-USD  | 2026-06-12 00:00:00 |     0.1752    |       -50.75      | NEUTRAL  | Kraken API    |
| TGT        | 2026-06-11 00:00:00 |   132.64      |        63.3333    | NEUTRAL  | Yahoo Finance |
| TLT        | 2026-06-11 00:00:00 |    85.98      |        24.6667    | NEUTRAL  | Yahoo Finance |
| TMO        | 2026-06-11 00:00:00 |   475.66      |        15.9167    | NEUTRAL  | Yahoo Finance |
| TSLA       | 2026-06-11 00:00:00 |   399.15      |       -29.5833    | NEUTRAL  | Yahoo Finance |
| TXN        | 2026-06-11 00:00:00 |   297.1       |        25.3333    | NEUTRAL  | Yahoo Finance |
| USO        | 2026-06-11 00:00:00 |   128.83      |       -29.0833    | NEUTRAL  | Yahoo Finance |
| VEA        | 2026-06-11 00:00:00 |    71.31      |        37.75      | NEUTRAL  | Yahoo Finance |
| VIXY       | 2026-06-11 00:00:00 |    24.41      |       -15.75      | NEUTRAL  | Yahoo Finance |
| VNQ        | 2026-06-11 00:00:00 |    97.61      |        65.6667    | NEUTRAL  | Yahoo Finance |
| VTI        | 2026-06-11 00:00:00 |   364.3       |         4.58333   | NEUTRAL  | Yahoo Finance |
| VWO        | 2026-06-11 00:00:00 |    59.1       |        -5.66667   | NEUTRAL  | Yahoo Finance |
| VZ         | 2026-06-11 00:00:00 |    46.94      |        13.4167    | NEUTRAL  | Yahoo Finance |
| WMT        | 2026-06-11 00:00:00 |   120.5       |         8.5       | NEUTRAL  | Yahoo Finance |
| XBI        | 2026-06-11 00:00:00 |   132.74      |        31.6667    | NEUTRAL  | Yahoo Finance |
| XLB        | 2026-06-11 00:00:00 |    51.22      |        36.1667    | NEUTRAL  | Yahoo Finance |
| XLC        | 2026-06-11 00:00:00 |   112.12      |       -59.0833    | NEUTRAL  | Yahoo Finance |
| XLE        | 2026-06-11 00:00:00 |    57.12      |       -27.3333    | NEUTRAL  | Yahoo Finance |
| XLF        | 2026-06-11 00:00:00 |    52.62      |        59.9167    | NEUTRAL  | Yahoo Finance |
| XLI        | 2026-06-11 00:00:00 |   175.15      |        52.3333    | NEUTRAL  | Yahoo Finance |
| XLM-USD    | 2026-06-12 00:00:00 |     0.190093  |       -21.6667    | NEUTRAL  | Kraken API    |
| XLP        | 2026-06-11 00:00:00 |    85.27      |        59.8333    | NEUTRAL  | Yahoo Finance |
| XLV        | 2026-06-11 00:00:00 |   154.09      |        54.1667    | NEUTRAL  | Yahoo Finance |
| XLY        | 2026-06-11 00:00:00 |   116.3       |       -31.3333    | NEUTRAL  | Yahoo Finance |
| XOM        | 2026-06-11 00:00:00 |   146.6       |       -23.5833    | NEUTRAL  | Yahoo Finance |
| ZEC-USD    | 2026-06-12 00:00:00 |   426.22      |       -39.5833    | NEUTRAL  | Kraken API    |
| AAVE-USD   | 2026-06-12 00:00:00 |    64.03      |       -46.3333    | SHORT    | Kraken API    |
| ADA-USD    | 2026-06-12 00:00:00 |     0.168828  |       -46.3333    | SHORT    | Kraken API    |
| APT-USD    | 2026-06-12 00:00:00 |     0.6433    |       -55.3333    | SHORT    | Kraken API    |
| ARB-USD    | 2026-06-12 00:00:00 |     0.0829    |       -44.6667    | SHORT    | Kraken API    |
| AVAX-USD   | 2026-06-12 00:00:00 |     6.622     |       -49.6667    | SHORT    | Kraken API    |
| BCH-USD    | 2026-06-12 00:00:00 |   204.63      |       -62.1667    | SHORT    | Kraken API    |
| BITO       | 2026-06-11 00:00:00 |     8.64      |       -60.6667    | SHORT    | Yahoo Finance |
| BLK        | 2026-06-11 00:00:00 |  1016.58      |       -54.0833    | SHORT    | Yahoo Finance |
| BONK-USD   | 2026-06-12 00:00:00 |     4.405e-06 |       -46.3333    | SHORT    | Kraken API    |
| BTC-USD    | 2026-06-12 00:00:00 | 63346.9       |       -44.3333    | SHORT    | Kraken API    |
| DASH-USD   | 2026-06-12 00:00:00 |    35.311     |       -63.8333    | SHORT    | Kraken API    |
| DIS        | 2026-06-11 00:00:00 |   100.34      |       -51.5833    | SHORT    | Yahoo Finance |
| DOGE-USD   | 2026-06-12 00:00:00 |     0.0858458 |       -46.3333    | SHORT    | Kraken API    |
| DOT-USD    | 2026-06-12 00:00:00 |     0.946     |       -51.6667    | SHORT    | Kraken API    |
| ETC-USD    | 2026-06-12 00:00:00 |     7.217     |       -41.3333    | SHORT    | Kraken API    |
| ETH-USD    | 2026-06-12 00:00:00 |  1666.41      |       -54.3333    | SHORT    | Kraken API    |
| FIL-USD    | 2026-06-12 00:00:00 |     0.754     |       -52.3333    | SHORT    | Kraken API    |
| FXI        | 2026-06-11 00:00:00 |    34.91      |       -52.0833    | SHORT    | Yahoo Finance |
| GDX        | 2026-06-11 00:00:00 |    77.72      |       -53.5833    | SHORT    | Yahoo Finance |
| GDXJ       | 2026-06-11 00:00:00 |   101.08      |       -59.3333    | SHORT    | Yahoo Finance |
| GLD        | 2026-06-11 00:00:00 |   386.32      |       -55.3333    | SHORT    | Yahoo Finance |
| GRT-USD    | 2026-06-12 00:00:00 |     0.01978   |       -49.6667    | SHORT    | Kraken API    |
| HBAR-USD   | 2026-06-12 00:00:00 |     0.07942   |       -51.3333    | SHORT    | Kraken API    |
| IBIT       | 2026-06-11 00:00:00 |    36.05      |       -58.9167    | SHORT    | Yahoo Finance |
| ICP-USD    | 2026-06-12 00:00:00 |     2.256     |       -54         | SHORT    | Kraken API    |
| INTU       | 2026-06-11 00:00:00 |   276.91      |       -55.5833    | SHORT    | Yahoo Finance |
| LDO-USD    | 2026-06-12 00:00:00 |     0.266     |       -46.3333    | SHORT    | Kraken API    |
| LINK-USD   | 2026-06-12 00:00:00 |     7.87048   |       -41.3333    | SHORT    | Kraken API    |
| LTC-USD    | 2026-06-12 00:00:00 |    42.48      |       -48.3333    | SHORT    | Kraken API    |
| MSFT       | 2026-06-11 00:00:00 |   390.34      |       -53.75      | SHORT    | Yahoo Finance |
| NEM        | 2026-06-11 00:00:00 |    97.59      |       -53.5833    | SHORT    | Yahoo Finance |
| NOW        | 2026-06-11 00:00:00 |   103.08      |       -40.9167    | SHORT    | Yahoo Finance |
| OP-USD     | 2026-06-12 00:00:00 |     0.0956    |       -47         | SHORT    | Kraken API    |
| ORCL       | 2026-06-11 00:00:00 |   184.1       |       -53.0833    | SHORT    | Yahoo Finance |
| PEPE-USD   | 2026-06-12 00:00:00 |     2.778e-06 |       -49.6667    | SHORT    | Kraken API    |
| POL-USD    | 2026-06-12 00:00:00 |     0.07427   |       -48         | SHORT    | Kraken API    |
| SHIB-USD   | 2026-06-12 00:00:00 |     4.817e-06 |       -43         | SHORT    | Kraken API    |
| SKY-USD    | 2026-06-12 00:00:00 |     0.05668   |       -45         | SHORT    | Kraken API    |
| SLV        | 2026-06-11 00:00:00 |    60.82      |       -42.0833    | SHORT    | Yahoo Finance |
| SNX-USD    | 2026-06-12 00:00:00 |     0.2446    |       -49.6667    | SHORT    | Kraken API    |
| SOL-USD    | 2026-06-12 00:00:00 |    66.57      |       -49.6667    | SHORT    | Kraken API    |
| T          | 2026-06-11 00:00:00 |    23         |       -61.0833    | SHORT    | Yahoo Finance |
| TIA-USD    | 2026-06-12 00:00:00 |     0.3218    |       -53.6667    | SHORT    | Kraken API    |
| TMUS       | 2026-06-11 00:00:00 |   185.82      |       -36.25      | SHORT    | Yahoo Finance |
| TRX-USD    | 2026-06-12 00:00:00 |     0.315471  |       -43.9167    | SHORT    | Kraken API    |
| UNI-USD    | 2026-06-12 00:00:00 |     2.4978    |       -49.6667    | SHORT    | Kraken API    |
| WIF-USD    | 2026-06-12 00:00:00 |     0.157     |       -50.3333    | SHORT    | Kraken API    |
| XLU        | 2026-06-11 00:00:00 |    44.05      |       -30.9167    | SHORT    | Yahoo Finance |
| XRP-USD    | 2026-06-12 00:00:00 |     1.13863   |       -44.6667    | SHORT    | Kraken API    |
| YFI-USD    | 2026-06-12 00:00:00 |  1882.7       |       -45         | SHORT    | Kraken API    |

## Edge Summary

- Symbols with trades: **160** of 160
- Beat buy-and-hold: **34.38%** of traded symbols
- Positive return: **35.62%** of traded symbols
- Median strategy return: **-8.42%** (benchmark **17.07%**)
- Median excess vs benchmark: **-30.37%**
- Median Sharpe: **-0.06**
- Median exposure: **44.34%**

> Edge is real only if both _beat buy-and-hold_ and _median excess_ are convincingly positive across many symbols. Treat a single high-return symbol as noise.

## Portfolio Backtest

Actual capital-allocation books (not per-symbol averages). Benchmarks: `equal_weight_buyhold` (whole tracked universe), `spy_buyhold` (100% SPY), and `sixty_forty` (60% SPY / 40% AGG). `high_conf_voltarget` inverse-vol-weights the HIGH-confidence book; `conviction_long_short` is market-neutral. Judge on **Sharpe** and **max_drawdown** out-of-sample, not raw return: a fully-invested long book wins on return in a bull market but carries all the risk.

| strategy              | scope         | ann_return   | ann_vol   |   sharpe | max_drawdown   | total_return   |   avg_gross_exposure |
|:----------------------|:--------------|:-------------|:----------|---------:|:---------------|:---------------|---------------------:|
| equal_weight_buyhold  | full          | -11.22%      | 33.92%    |    -0.33 | -57.73%        | -40.41%        |                 1    |
| equal_weight_buyhold  | out_of_sample | -16.48%      | 34.78%    |    -0.47 | -39.63%        | -21.30%        |                 1    |
| all_signals_ew        | full          | -5.79%       | 28.13%    |    -0.21 | -59.44%        | -25.67%        |                 1    |
| all_signals_ew        | out_of_sample | 8.20%        | 28.59%    |     0.29 | -28.38%        | 4.50%          |                 1    |
| high_conf_ew          | full          | 3.87%        | 32.92%    |     0.12 | -44.24%        | -4.44%         |                 0.89 |
| high_conf_ew          | out_of_sample | 23.37%       | 37.01%    |     0.63 | -20.90%        | 19.41%         |                 0.89 |
| high_conf_voltarget   | full          | 4.60%        | 30.58%    |     0.15 | -36.25%        | -0.04%         |                 0.89 |
| high_conf_voltarget   | out_of_sample | 17.81%       | 35.21%    |     0.51 | -17.06%        | 13.35%         |                 0.89 |
| conviction_long_short | full          | -7.35%       | 23.53%    |    -0.31 | -35.42%        | -26.52%        |                 0.97 |
| conviction_long_short | out_of_sample | -0.42%       | 27.12%    |    -0.02 | -21.23%        | -4.28%         |                 0.97 |
| spy_buyhold           | full          | 8.51%        | 13.37%    |     0.64 | -17.81%        | 26.04%         |                 0.79 |
| spy_buyhold           | out_of_sample | -2.58%       | 9.92%     |    -0.26 | -14.83%        | -3.21%         |                 0.79 |
| sixty_forty           | full          | 4.95%        | 8.47%     |     0.58 | -10.80%        | 14.97%         |                 0.79 |
| sixty_forty           | out_of_sample | -2.58%       | 6.45%     |    -0.4  | -10.06%        | -2.92%         |                 0.79 |

## Walk-Forward Robustness

Each book measured across contiguous time folds (each a different regime). A book has durable edge only if `mean_sharpe` is positive, `min_sharpe` isn't deeply negative, and `pct_positive_folds` is high — a single great fold doesn't count. `fold_sharpes` lists each fold oldest-to-newest.

| strategy              |   n_folds |   mean_sharpe |   median_sharpe |   min_sharpe | pct_positive_folds   | mean_return   | fold_sharpes                 |
|:----------------------|----------:|--------------:|----------------:|-------------:|:---------------------|:--------------|:-----------------------------|
| equal_weight_buyhold  |         5 |         -0.01 |           -0.33 |        -1.93 | 40.00%               | -6.75%        | 1.87;-1.93;1.11;-0.33;-0.78  |
| all_signals_ew        |         5 |         -0.01 |            0.66 |        -1.51 | 60.00%               | -3.84%        | 0.71;0.66;-1.18;-1.51;1.25   |
| high_conf_ew          |         5 |          0.44 |            0.15 |        -0.9  | 60.00%               | 0.59%         | 1.84;0.15;-0.90;-0.37;1.47   |
| high_conf_voltarget   |         5 |          0.56 |            0.31 |        -0.9  | 60.00%               | 0.92%         | 2.71;0.31;-0.90;-0.16;0.85   |
| conviction_long_short |         5 |         -0.34 |           -0.26 |        -0.91 | 20.00%               | -5.74%        | -0.82;-0.10;-0.26;-0.91;0.37 |
| spy_buyhold           |         5 |          0.66 |            0.28 |         0.01 | 100.00%              | 4.89%         | 1.95;0.84;0.28;0.01;0.21     |
| sixty_forty           |         5 |          0.58 |            0.3  |        -0    | 80.00%               | 2.90%         | 1.98;0.52;0.30;0.10;-0.00    |

## Strategy Comparison

Each decision rule backtested over the same data. `out_of_sample` is the most recent ~35% of each symbol's history (unseen tail). A rule has real edge only if `median_excess` and `beat_benchmark_pct` stay positive out-of-sample, not just full-sample.

| strategy        | scope         |   symbols | beat_benchmark_pct   | positive_pct   | median_return   | median_benchmark   | median_excess   |   median_sharpe |   total_trades |
|:----------------|:--------------|----------:|:---------------------|:---------------|:----------------|:-------------------|:----------------|----------------:|---------------:|
| trend           | full          |       160 | 34.38%               | 35.62%         | -8.42%          | 17.07%             | -30.37%         |           -0.06 |          11223 |
| trend           | out_of_sample |       160 | 36.88%               | 55.62%         | 3.44%           | 4.44%              | -7.46%          |            0.34 |           3924 |
| mean_reversion  | full          |       157 | 40.13%               | 49.04%         | -0.10%          | 15.79%             | -18.02%         |           -0.02 |           1244 |
| mean_reversion  | out_of_sample |       129 | 46.51%               | 58.14%         | 0.33%           | 1.29%              | -1.48%          |            0.7  |            478 |
| regime_adaptive | full          |       160 | 35.00%               | 34.38%         | -9.01%          | 17.07%             | -31.16%         |           -0.06 |          11498 |
| regime_adaptive | out_of_sample |       160 | 35.62%               | 56.25%         | 3.55%           | 4.44%              | -6.93%          |            0.34 |           4027 |

## Signal Calibration

Realized forward return in the signal's direction, grouped by confidence. HIGH should outrank LOW for the confidence score to be meaningful.

| confidence_level   |   horizon |     n | mean_return   | median_return   | win_rate   |
|:-------------------|----------:|------:|:--------------|:----------------|:-----------|
| HIGH               |         5 |  8190 | 0.20%         | 0.16%           | 52.52%     |
| MEDIUM             |         5 | 29094 | 0.10%         | 0.11%           | 51.29%     |
| LOW                |         5 |  3265 | -0.57%        | -0.48%          | 45.24%     |
| ALL                |         5 | 40549 | 0.06%         | 0.08%           | 51.05%     |
| HIGH               |        10 |  8141 | 0.52%         | 0.20%           | 52.44%     |
| MEDIUM             |        10 | 28832 | 0.29%         | 0.19%           | 51.57%     |
| LOW                |        10 |  3248 | -0.85%        | -0.72%          | 45.41%     |
| ALL                |        10 | 40221 | 0.25%         | 0.14%           | 51.25%     |
| HIGH               |        20 |  8049 | 0.96%         | 0.53%           | 54.02%     |
| MEDIUM             |        20 | 28213 | 0.83%         | 0.61%           | 53.57%     |
| LOW                |        20 |  3203 | -0.73%        | -0.59%          | 46.80%     |
| ALL                |        20 | 39465 | 0.73%         | 0.52%           | 53.12%     |

## Backtest Summary

### Data Quality / Signal Availability

- **ok**: 160 symbols

| symbol     |   trades | return   | benchmark_return   | mdd     |   sharpe | exposure   | skipped_reason   |
|:-----------|---------:|:---------|:-------------------|:--------|---------:|:-----------|:-----------------|
| AAPL       |       63 | 13.82%   | 54.33%             | -20.65% |     0.37 | 49.58%     | ok               |
| AAVE-USD   |       80 | -59.98%  | -79.12%            | -69.30% |    -0.7  | 36.59%     | ok               |
| ABBV       |       64 | -15.38%  | 36.41%             | -30.55% |    -0.3  | 49.25%     | ok               |
| ADA-USD    |       88 | -83.21%  | -82.94%            | -89.89% |    -0.68 | 46.36%     | ok               |
| ADBE       |       66 | -22.69%  | -64.22%            | -38.01% |    -0.23 | 56.91%     | ok               |
| AGG        |       69 | -6.61%   | 0.88%              | -10.16% |    -1.1  | 31.11%     | ok               |
| ALGO-USD   |       86 | -49.47%  | -76.24%            | -55.33% |    -0.55 | 37.74%     | ok               |
| AMAT       |       67 | -23.03%  | 229.07%            | -57.80% |    -0.17 | 53.41%     | ok               |
| AMD        |       58 | 2.77%    | 180.35%            | -47.17% |     0.24 | 38.60%     | ok               |
| AMGN       |       71 | -18.90%  | 15.03%             | -34.14% |    -0.36 | 48.59%     | ok               |
| AMZN       |       74 | -33.84%  | 55.47%             | -42.48% |    -0.99 | 38.27%     | ok               |
| APT-USD    |       76 | -26.36%  | -93.35%            | -69.96% |    -0    | 43.10%     | ok               |
| ARB-USD    |       70 | 7.63%    | -89.90%            | -62.67% |     0.32 | 38.89%     | ok               |
| ARKK       |       81 | -31.77%  | 63.05%             | -34.32% |    -0.55 | 38.94%     | ok               |
| ATOM-USD   |       86 | -65.80%  | -70.75%            | -72.11% |    -1.05 | 43.68%     | ok               |
| AVAX-USD   |       74 | -37.18%  | -83.09%            | -60.45% |    -0.3  | 38.12%     | ok               |
| AVGO       |       60 | 31.52%   | 218.34%            | -35.76% |     0.5  | 46.09%     | ok               |
| BA         |       69 | 9.73%    | 3.07%              | -30.56% |     0.28 | 50.58%     | ok               |
| BAC        |       80 | -16.14%  | 71.20%             | -27.64% |    -0.39 | 46.26%     | ok               |
| BCH-USD    |       76 | -1.59%   | -53.26%            | -53.87% |     0.19 | 46.17%     | ok               |
| BITO       |       78 | 6.28%    | -56.99%            | -42.82% |     0.25 | 39.77%     | ok               |
| BLK        |       75 | -4.23%   | 26.21%             | -20.81% |    -0.06 | 41.93%     | ok               |
| BND        |       65 | -7.32%   | 0.91%              | -9.89%  |    -1.18 | 32.28%     | ok               |
| BONK-USD   |       68 | 59.30%   | -85.73%            | -48.17% |     0.67 | 41.38%     | ok               |
| BTC-USD    |       74 | -0.51%   | -34.65%            | -25.19% |     0.14 | 51.72%     | ok               |
| C          |       83 | -23.72%  | 167.99%            | -37.02% |    -0.44 | 50.58%     | ok               |
| CAT        |       72 | 35.17%   | 214.65%            | -21.02% |     0.63 | 57.07%     | ok               |
| CL         |       60 | 18.52%   | 11.21%             | -14.32% |     0.62 | 48.75%     | ok               |
| CMCSA      |       80 | -36.24%  | -41.00%            | -40.02% |    -0.9  | 44.59%     | ok               |
| COMP-USD   |       89 | -36.73%  | -76.65%            | -58.43% |    -0.21 | 45.02%     | ok               |
| COP        |       75 | -27.14%  | 6.94%              | -44.32% |    -0.53 | 40.93%     | ok               |
| COST       |       60 | 6.71%    | 40.39%             | -29.73% |     0.26 | 46.76%     | ok               |
| CRM        |       65 | -34.20%  | -40.74%            | -40.31% |    -0.68 | 43.59%     | ok               |
| CRV-USD    |       62 | 8.89%    | -71.37%            | -39.89% |     0.32 | 33.14%     | ok               |
| CSCO       |       59 | 26.11%   | 137.62%            | -21.79% |     0.55 | 49.25%     | ok               |
| CVX        |       71 | -18.53%  | 30.64%             | -27.83% |    -0.49 | 42.10%     | ok               |
| DASH-USD   |       65 | -42.38%  | -8.91%             | -64.43% |    -0.02 | 31.23%     | ok               |
| DBC        |       58 | -12.57%  | 31.49%             | -25.35% |    -0.43 | 32.78%     | ok               |
| DE         |       76 | -11.92%  | 48.58%             | -25.24% |    -0.18 | 45.59%     | ok               |
| DIA        |       58 | -3.07%   | 34.54%             | -12.94% |    -0.13 | 45.76%     | ok               |
| DIS        |       63 | -4.95%   | 7.82%              | -24.36% |     0.01 | 48.25%     | ok               |
| DOGE-USD   |       77 | -15.03%  | -75.33%            | -60.95% |     0.11 | 49.62%     | ok               |
| DOT-USD    |       90 | -43.53%  | -86.51%            | -59.38% |    -0.29 | 47.51%     | ok               |
| DXY-INDEX  |       44 | -3.72%   | -2.67%             | -6.06%  |    -0.6  | 28.20%     | ok               |
| EEM        |       64 | -9.40%   | 75.83%             | -25.67% |    -0.25 | 43.43%     | ok               |
| EFA        |       58 | -8.33%   | 41.66%             | -13.87% |    -0.3  | 43.93%     | ok               |
| EOG        |       81 | -29.07%  | 23.93%             | -48.13% |    -0.66 | 47.25%     | ok               |
| ETC-USD    |       64 | -35.93%  | -72.15%            | -48.16% |    -0.52 | 30.84%     | ok               |
| ETH-USD    |       60 | 166.66%  | -50.71%            | -30.11% |     1.32 | 44.44%     | ok               |
| EWJ        |       64 | -18.27%  | 39.88%             | -30.73% |    -0.59 | 41.43%     | ok               |
| FCX        |       71 | -35.36%  | 71.11%             | -48.09% |    -0.46 | 46.26%     | ok               |
| FET-USD    |       73 | -3.74%   | -86.49%            | -48.39% |     0.25 | 38.70%     | ok               |
| FIL-USD    |       68 | -28.71%  | -85.91%            | -46.54% |    -0.21 | 32.18%     | ok               |
| FXI        |       50 | -12.49%  | 61.02%             | -24.33% |    -0.24 | 27.79%     | ok               |
| GDX        |       62 | 7.90%    | 180.68%            | -34.99% |     0.25 | 48.59%     | ok               |
| GDXJ       |       68 | -20.46%  | 198.26%            | -44.93% |    -0.18 | 46.42%     | ok               |
| GE         |       74 | 11.66%   | 221.20%            | -27.82% |     0.31 | 51.41%     | ok               |
| GLD        |       48 | 22.99%   | 105.57%            | -16.63% |     0.61 | 43.93%     | ok               |
| GOOGL      |       63 | 74.57%   | 144.41%            | -20.41% |     1.12 | 54.41%     | ok               |
| GRT-USD    |       87 | -13.59%  | -91.04%            | -56.53% |     0.06 | 40.61%     | ok               |
| GS         |       76 | -4.14%   | 170.97%            | -22.13% |     0.01 | 50.75%     | ok               |
| HD         |       69 | -6.00%   | -10.04%            | -17.69% |    -0.09 | 44.09%     | ok               |
| HON        |       95 | -30.75%  | 15.79%             | -30.75% |    -0.86 | 52.75%     | ok               |
| HYG        |       81 | -9.52%   | 3.59%              | -9.59%  |    -1.11 | 34.28%     | ok               |
| IBIT       |       32 | 34.74%   | -5.16%             | -18.95% |     0.75 | 29.98%     | ok               |
| IBM        |       72 | 25.20%   | 60.28%             | -25.31% |     0.55 | 50.92%     | ok               |
| ICP-USD    |       83 | 6.93%    | -79.54%            | -55.67% |     0.32 | 38.12%     | ok               |
| IEF        |       76 | -10.90%  | -0.63%             | -11.70% |    -1.54 | 32.78%     | ok               |
| IEMG       |       58 | -5.52%   | 69.57%             | -26.84% |    -0.12 | 43.59%     | ok               |
| INJ-USD    |       79 | -58.54%  | -77.33%            | -76.97% |    -0.61 | 38.51%     | ok               |
| INTC       |       70 | 55.82%   | 142.91%            | -60.60% |     0.62 | 49.25%     | ok               |
| INTU       |       67 | -10.03%  | -55.49%            | -43.77% |    -0.05 | 42.60%     | ok               |
| ITA        |       72 | -1.83%   | 93.94%             | -23.75% |     0.02 | 46.42%     | ok               |
| IWM        |       50 | 8.72%    | 50.92%             | -12.83% |     0.36 | 37.10%     | ok               |
| JNJ        |       74 | 4.67%    | 47.41%             | -17.51% |     0.22 | 50.75%     | ok               |
| JPM        |       77 | -22.10%  | 84.07%             | -33.43% |    -0.57 | 52.75%     | ok               |
| KO         |       51 | 27.96%   | 37.94%             | -8.07%  |     1    | 37.94%     | ok               |
| LDO-USD    |       78 | 15.20%   | -84.96%            | -58.32% |     0.4  | 38.31%     | ok               |
| LIN        |       70 | -2.47%   | 26.53%             | -21.53% |    -0.03 | 39.10%     | ok               |
| LINK-USD   |       70 | -10.11%  | -63.21%            | -50.48% |     0.14 | 41.19%     | ok               |
| LLY        |       69 | -8.50%   | 84.69%             | -53.34% |    -0.01 | 51.41%     | ok               |
| LRCX       |       80 | -14.53%  | 338.72%            | -63.56% |    -0.02 | 46.26%     | ok               |
| LTC-USD    |       66 | -29.31%  | -58.64%            | -53.76% |    -0.21 | 48.08%     | ok               |
| MCD        |       77 | -3.77%   | -5.24%             | -18.81% |    -0.1  | 38.27%     | ok               |
| META       |       72 | -12.94%  | 48.24%             | -38.96% |    -0.08 | 51.08%     | ok               |
| MPC        |       71 | -13.74%  | 70.49%             | -44.76% |    -0.14 | 49.92%     | ok               |
| MRK        |       69 | -21.49%  | 1.57%              | -32.14% |    -0.46 | 46.92%     | ok               |
| MS         |       79 | -16.84%  | 149.19%            | -27.79% |    -0.36 | 47.42%     | ok               |
| MSFT       |       81 | -31.77%  | -2.09%             | -38.02% |    -0.82 | 48.42%     | ok               |
| MU         |       51 | 225.21%  | 1038.01%           | -68.76% |     1.25 | 59.07%     | ok               |
| NEAR-USD   |       87 | 4.42%    | -62.04%            | -59.86% |     0.3  | 42.34%     | ok               |
| NEM        |       76 | -25.68%  | 182.22%            | -38.49% |    -0.23 | 55.41%     | ok               |
| NFLX       |       62 | 25.14%   | 68.28%             | -21.09% |     0.59 | 54.24%     | ok               |
| NKE        |       93 | -37.96%  | -54.84%            | -55.35% |    -0.53 | 44.09%     | ok               |
| NOW        |       78 | 19.56%   | -31.20%            | -30.25% |     0.4  | 45.92%     | ok               |
| NVDA       |       74 | -25.76%  | 131.61%            | -45.02% |    -0.18 | 59.89%     | ok               |
| OP-USD     |       72 | 20.19%   | -94.95%            | -70.11% |     0.42 | 35.63%     | ok               |
| ORCL       |       70 | 56.30%   | 67.87%             | -29.47% |     0.65 | 53.24%     | ok               |
| OXY        |       65 | -0.42%   | -1.68%             | -30.85% |     0.11 | 43.76%     | ok               |
| PEP        |       85 | -10.58%  | -13.30%            | -21.35% |    -0.25 | 50.08%     | ok               |
| PEPE-USD   |       77 | 17.18%   | -85.07%            | -57.66% |     0.42 | 43.30%     | ok               |
| PFE        |       77 | -37.76%  | -7.46%             | -42.29% |    -1.17 | 36.94%     | ok               |
| PG         |       62 | -11.08%  | 0.52%              | -21.65% |    -0.39 | 41.10%     | ok               |
| PM         |       83 | 1.14%    | 95.81%             | -33.68% |     0.12 | 57.24%     | ok               |
| POL-USD    |       79 | 69.37%   | -84.21%            | -46.45% |     0.8  | 48.85%     | ok               |
| QCOM       |       77 | -18.79%  | 33.56%             | -57.69% |    -0.09 | 48.09%     | ok               |
| QQQ        |       60 | 15.89%   | 70.26%             | -12.88% |     0.48 | 46.09%     | ok               |
| RENDER-USD |       94 | -16.54%  | -60.91%            | -45.00% |     0.13 | 44.23%     | ok               |
| RTX        |       56 | 19.78%   | 115.37%            | -16.99% |     0.54 | 51.41%     | ok               |
| SBUX       |       65 | -23.09%  | 8.97%              | -30.54% |    -0.47 | 38.94%     | ok               |
| SCHW       |       74 | -21.97%  | 39.07%             | -30.41% |    -0.52 | 45.42%     | ok               |
| SHIB-USD   |       76 | -22.55%  | -77.90%            | -48.95% |    -0.06 | 52.11%     | ok               |
| SHY        |       50 | -2.12%   | 0.07%              | -2.85%  |    -0.73 | 35.77%     | ok               |
| SKY-USD    |       68 | -28.24%  | -1.99%             | -43.98% |    -0.36 | 40.24%     | ok               |
| SLB        |       77 | -31.56%  | 12.81%             | -54.95% |    -0.58 | 50.08%     | ok               |
| SLV        |       60 | 30.22%   | 194.24%            | -42.66% |     0.52 | 40.27%     | ok               |
| SMH        |       48 | 94.32%   | 225.60%            | -33.99% |     1.19 | 51.08%     | ok               |
| SNX-USD    |       63 | 23.84%   | -87.34%            | -32.91% |     0.46 | 40.42%     | ok               |
| SOL-USD    |       68 | -33.65%  | -67.07%            | -55.52% |    -0.1  | 59.39%     | ok               |
| SOXX       |       55 | 80.72%   | 192.86%            | -40.34% |     1.02 | 50.08%     | ok               |
| SPY        |       58 | 7.21%    | 52.93%             | -16.47% |     0.31 | 50.75%     | ok               |
| SUSHI-USD  |       92 | -77.47%  | -88.81%            | -81.22% |    -1.13 | 35.82%     | ok               |
| T          |       64 | 30.91%   | 37.97%             | -17.01% |     0.75 | 50.08%     | ok               |
| TGT        |       56 | -11.79%  | -3.98%             | -41.74% |    -0.16 | 38.60%     | ok               |
| TIA-USD    |       82 | -6.82%   | -93.40%            | -55.60% |     0.18 | 33.14%     | ok               |
| TLT        |       70 | -23.31%  | -8.62%             | -24.69% |    -1.71 | 32.95%     | ok               |
| TMO        |       57 | 15.46%   | -13.79%            | -16.83% |     0.41 | 48.75%     | ok               |
| TMUS       |       70 | 12.62%   | 12.51%             | -24.50% |     0.36 | 48.59%     | ok               |
| TRX-USD    |       70 | 2.59%    | 24.90%             | -22.90% |     0.16 | 48.47%     | ok               |
| TSLA       |       68 | 4.77%    | 88.11%             | -57.89% |     0.26 | 43.43%     | ok               |
| TXN        |       73 | -12.13%  | 71.09%             | -46.98% |    -0.04 | 54.08%     | ok               |
| UNH        |       74 | 23.25%   | -19.46%            | -27.25% |     0.45 | 51.58%     | ok               |
| UNI-USD    |       90 | -64.09%  | -81.55%            | -79.39% |    -0.63 | 41.00%     | ok               |
| UPS        |       66 | -35.18%  | -30.75%            | -40.62% |    -0.69 | 39.27%     | ok               |
| USO        |       68 | 2.80%    | 87.20%             | -43.35% |     0.17 | 34.44%     | ok               |
| VEA        |       58 | -0.98%   | 52.44%             | -17.93% |     0.01 | 44.09%     | ok               |
| VIXY       |       92 | -78.16%  | -59.15%            | -87.63% |    -0.94 | 31.61%     | ok               |
| VNQ        |       75 | -16.77%  | 14.30%             | -24.92% |    -0.7  | 37.60%     | ok               |
| VTI        |       66 | -0.72%   | 52.08%             | -18.77% |     0.04 | 52.08%     | ok               |
| VWO        |       76 | -13.41%  | 49.13%             | -25.20% |    -0.47 | 44.09%     | ok               |
| VZ         |       83 | -20.11%  | 19.35%             | -31.88% |    -0.6  | 38.60%     | ok               |
| WFC        |       86 | -19.54%  | 71.24%             | -30.87% |    -0.35 | 47.25%     | ok               |
| WIF-USD    |       72 | -40.82%  | -91.53%            | -56.94% |    -0.17 | 32.57%     | ok               |
| WMT        |       55 | 32.33%   | 122.63%            | -21.31% |     0.85 | 52.25%     | ok               |
| XBI        |       62 | -4.13%   | 52.49%             | -21.75% |    -0.02 | 39.43%     | ok               |
| XLB        |       70 | -14.85%  | 24.58%             | -26.57% |    -0.51 | 37.60%     | ok               |
| XLC        |       63 | 16.85%   | 49.83%             | -12.33% |     0.58 | 55.91%     | ok               |
| XLE        |       75 | -11.95%  | 42.50%             | -37.51% |    -0.23 | 47.09%     | ok               |
| XLF        |       74 | -10.78%  | 38.73%             | -23.61% |    -0.35 | 48.92%     | ok               |
| XLI        |       64 | 5.82%    | 55.76%             | -11.38% |     0.28 | 47.25%     | ok               |
| XLK        |       40 | 63.23%   | 83.05%             | -14.75% |     1.19 | 48.59%     | ok               |
| XLM-USD    |       69 | 13.95%   | -54.51%            | -45.54% |     0.37 | 46.36%     | ok               |
| XLP        |       74 | 6.74%    | 18.35%             | -10.28% |     0.4  | 43.09%     | ok               |
| XLU        |       71 | -8.16%   | 44.47%             | -17.22% |    -0.33 | 39.43%     | ok               |
| XLV        |       68 | -9.77%   | 10.49%             | -15.55% |    -0.46 | 36.94%     | ok               |
| XLY        |       74 | 0.75%    | 33.00%             | -14.01% |     0.09 | 44.93%     | ok               |
| XOM        |       58 | 1.42%    | 51.21%             | -20.29% |     0.11 | 36.61%     | ok               |
| XRP-USD    |       62 | -35.95%  | -49.85%            | -50.65% |    -0.35 | 35.63%     | ok               |
| YFI-USD    |       83 | -50.68%  | -77.02%            | -67.78% |    -0.71 | 40.04%     | ok               |
| ZEC-USD    |       69 | 43.83%   | 711.85%            | -46.93% |     0.56 | 36.40%     | ok               |

## AAPL Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 23.95%   | 54.33%             | -21.71% |     0.54 |       67 | 53.41%     | ok               |
|          25 | 18.03%   | 54.33%             | -20.03% |     0.44 |       65 | 51.25%     | ok               |
|          15 | 17.95%   | 54.33%             | -23.86% |     0.43 |       74 | 60.73%     | ok               |
|          30 | 13.82%   | 54.33%             | -20.65% |     0.37 |       63 | 49.58%     | ok               |
|          35 | 8.61%    | 54.33%             | -22.04% |     0.28 |       63 | 47.42%     | ok               |

## AAVE-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 6.73%    | -79.12%            | -43.61% |     0.29 |       38 | 29.31%     | ok               |
|          45 | 5.38%    | -79.12%            | -46.87% |     0.27 |       38 | 26.05%     | ok               |
|          35 | -19.74%  | -79.12%            | -51.96% |    -0.02 |       52 | 31.99%     | ok               |
|          50 | -29.70%  | -79.12%            | -47.78% |    -0.27 |       42 | 20.31%     | ok               |
|          15 | -55.83%  | -79.12%            | -66.51% |    -0.42 |       82 | 50.38%     | ok               |

## ABBV Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -2.40%   | 36.41%             | -26.16% |     0.02 |       50 | 38.94%     | ok               |
|          40 | -11.88%  | 36.41%             | -26.61% |    -0.22 |       64 | 43.59%     | ok               |
|          35 | -13.13%  | 36.41%             | -27.83% |    -0.25 |       66 | 46.42%     | ok               |
|          30 | -15.38%  | 36.41%             | -30.55% |    -0.3  |       64 | 49.25%     | ok               |
|          45 | -14.62%  | 36.41%             | -29.59% |    -0.31 |       54 | 40.93%     | ok               |

## ADA-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -82.76%  | -82.94%            | -91.37% |    -0.54 |       80 | 61.49%     | ok               |
|          20 | -82.77%  | -82.94%            | -91.89% |    -0.56 |       84 | 56.70%     | ok               |
|          45 | -80.16%  | -82.94%            | -88.43% |    -0.62 |       62 | 31.80%     | ok               |
|          25 | -83.99%  | -82.94%            | -91.94% |    -0.63 |       83 | 53.45%     | ok               |
|          50 | -79.60%  | -82.94%            | -86.45% |    -0.65 |       59 | 27.39%     | ok               |

## ADBE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 10.63%   | -64.22%            | -21.34% |     0.3  |       76 | 49.25%     | ok               |
|          40 | -3.65%   | -64.22%            | -20.88% |     0.05 |       72 | 42.26%     | ok               |
|          25 | -7.34%   | -64.22%            | -31.29% |     0.04 |       50 | 61.06%     | ok               |
|          15 | -17.24%  | -64.22%            | -31.87% |    -0.11 |       61 | 65.89%     | ok               |
|          20 | -18.91%  | -64.22%            | -34.48% |    -0.14 |       52 | 63.39%     | ok               |

## AGG Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -6.61%   | 0.88%              | -10.16% |    -1.1  |       69 | 31.11%     | ok               |
|          20 | -7.58%   | 0.88%              | -10.67% |    -1.11 |       75 | 36.94%     | ok               |
|          45 | -5.75%   | 0.88%              | -7.89%  |    -1.16 |       52 | 20.47%     | ok               |
|          25 | -7.87%   | 0.88%              | -11.31% |    -1.2  |       73 | 35.11%     | ok               |
|          50 | -5.57%   | 0.88%              | -7.92%  |    -1.25 |       46 | 16.97%     | ok               |

## ALGO-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -49.47%  | -76.24%            | -55.33% |    -0.55 |       86 | 37.74%     | ok               |
|          15 | -58.84%  | -76.24%            | -68.50% |    -0.61 |       78 | 49.23%     | ok               |
|          50 | -40.80%  | -76.24%            | -43.84% |    -0.69 |       38 | 16.48%     | ok               |
|          35 | -50.76%  | -76.24%            | -53.42% |    -0.69 |       62 | 30.84%     | ok               |
|          25 | -61.15%  | -76.24%            | -72.48% |    -0.72 |       84 | 44.64%     | ok               |

## AMAT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -8.03%   | 229.07%            | -54.69% |     0.08 |       64 | 62.06%     | ok               |
|          30 | -23.03%  | 229.07%            | -57.80% |    -0.17 |       67 | 53.41%     | ok               |
|          20 | -28.65%  | 229.07%            | -60.72% |    -0.23 |       70 | 58.57%     | ok               |
|          50 | -25.66%  | 229.07%            | -48.72% |    -0.26 |       50 | 39.43%     | ok               |
|          35 | -28.51%  | 229.07%            | -55.89% |    -0.27 |       69 | 51.25%     | ok               |

## AMD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 2.77%    | 180.35%            | -47.17% |     0.24 |       58 | 38.60%     | ok               |
|          50 | 0.96%    | 180.35%            | -48.79% |     0.21 |       62 | 32.95%     | ok               |
|          35 | -10.33%  | 180.35%            | -54.57% |     0.11 |       64 | 40.60%     | ok               |
|          45 | -17.90%  | 180.35%            | -56.22% |     0.01 |       66 | 35.94%     | ok               |
|          30 | -22.16%  | 180.35%            | -59.88% |    -0.02 |       65 | 43.09%     | ok               |

## AMGN Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -13.54%  | 15.03%             | -26.64% |    -0.2  |       73 | 54.74%     | ok               |
|          15 | -16.60%  | 15.03%             | -27.92% |    -0.26 |       71 | 60.40%     | ok               |
|          35 | -16.11%  | 15.03%             | -31.23% |    -0.29 |       69 | 44.93%     | ok               |
|          30 | -18.90%  | 15.03%             | -34.14% |    -0.36 |       71 | 48.59%     | ok               |
|          25 | -22.20%  | 15.03%             | -33.41% |    -0.44 |       67 | 50.92%     | ok               |

## AMZN Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -17.83%  | 55.47%             | -28.70% |    -0.52 |       50 | 29.78%     | ok               |
|          50 | -25.03%  | 55.47%             | -35.48% |    -0.88 |       48 | 24.13%     | ok               |
|          45 | -25.89%  | 55.47%             | -35.47% |    -0.89 |       50 | 26.96%     | ok               |
|          35 | -29.70%  | 55.47%             | -38.29% |    -0.91 |       62 | 32.95%     | ok               |
|          30 | -33.84%  | 55.47%             | -42.48% |    -0.99 |       74 | 38.27%     | ok               |

## APT-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 58.04%   | -93.35%            | -46.73% |     0.79 |       44 | 19.92%     | ok               |
|          45 | 20.17%   | -93.35%            | -63.86% |     0.42 |       60 | 26.05%     | ok               |
|          40 | -2.92%   | -93.35%            | -63.33% |     0.21 |       66 | 31.61%     | ok               |
|          35 | -9.88%   | -93.35%            | -64.45% |     0.15 |       70 | 37.16%     | ok               |
|          20 | -20.45%  | -93.35%            | -70.51% |     0.09 |       73 | 50.96%     | ok               |

## ARB-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 64.15%   | -89.90%            | -53.74% |     0.69 |       87 | 55.17%     | ok               |
|          40 | 49.89%   | -89.90%            | -47.60% |     0.65 |       50 | 30.08%     | ok               |
|          35 | 40.15%   | -89.90%            | -56.00% |     0.58 |       62 | 33.72%     | ok               |
|          20 | 35.77%   | -89.90%            | -60.40% |     0.54 |       77 | 49.81%     | ok               |
|          45 | 26.25%   | -89.90%            | -50.83% |     0.47 |       56 | 23.37%     | ok               |

## ARKK Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -26.70%  | 63.05%             | -35.23% |    -0.33 |       90 | 50.42%     | ok               |
|          20 | -31.03%  | 63.05%             | -35.22% |    -0.45 |       85 | 45.76%     | ok               |
|          30 | -31.77%  | 63.05%             | -34.32% |    -0.55 |       81 | 38.94%     | ok               |
|          35 | -32.16%  | 63.05%             | -34.69% |    -0.59 |       80 | 36.44%     | ok               |
|          40 | -33.59%  | 63.05%             | -35.11% |    -0.67 |       72 | 31.61%     | ok               |

## ATOM-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -62.97%  | -70.75%            | -69.49% |    -0.9  |       91 | 50.38%     | ok               |
|          15 | -68.61%  | -70.75%            | -72.76% |    -0.98 |       93 | 60.54%     | ok               |
|          30 | -65.80%  | -70.75%            | -72.11% |    -1.05 |       86 | 43.68%     | ok               |
|          45 | -59.16%  | -70.75%            | -64.98% |    -1.09 |       72 | 28.35%     | ok               |
|          20 | -71.58%  | -70.75%            | -73.64% |    -1.14 |      101 | 54.60%     | ok               |

## AVAX-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 15.04%   | -83.09%            | -34.50% |     0.37 |       38 | 19.54%     | ok               |
|          45 | 7.64%    | -83.09%            | -41.07% |     0.28 |       40 | 22.99%     | ok               |
|          15 | 1.37%    | -83.09%            | -52.46% |     0.26 |       63 | 51.53%     | ok               |
|          40 | -7.09%   | -83.09%            | -47.98% |     0.09 |       46 | 25.86%     | ok               |
|          35 | -13.68%  | -83.09%            | -48.82% |     0.03 |       60 | 31.23%     | ok               |

## AVGO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 31.52%   | 218.34%            | -35.76% |     0.5  |       60 | 46.09%     | ok               |
|          25 | 26.85%   | 218.34%            | -38.01% |     0.45 |       64 | 46.76%     | ok               |
|          35 | 22.58%   | 218.34%            | -36.19% |     0.42 |       70 | 43.43%     | ok               |
|          40 | 22.16%   | 218.34%            | -40.70% |     0.41 |       60 | 40.27%     | ok               |
|          50 | 16.12%   | 218.34%            | -35.84% |     0.35 |       62 | 34.11%     | ok               |

## BA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 25.12%   | 3.07%              | -13.34% |     0.65 |       44 | 31.78%     | ok               |
|          35 | 33.11%   | 3.07%              | -23.77% |     0.62 |       72 | 45.92%     | ok               |
|          40 | 13.37%   | 3.07%              | -24.52% |     0.35 |       52 | 39.77%     | ok               |
|          25 | 13.00%   | 3.07%              | -32.48% |     0.33 |       72 | 54.08%     | ok               |
|          30 | 9.73%    | 3.07%              | -30.56% |     0.28 |       69 | 50.58%     | ok               |

## BAC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -9.16%   | 71.20%             | -20.73% |    -0.15 |       80 | 50.75%     | ok               |
|          45 | -6.67%   | 71.20%             | -20.40% |    -0.16 |       60 | 34.11%     | ok               |
|          15 | -12.57%  | 71.20%             | -22.24% |    -0.22 |       82 | 55.24%     | ok               |
|          35 | -10.08%  | 71.20%             | -27.83% |    -0.23 |       72 | 42.26%     | ok               |
|          50 | -9.84%   | 71.20%             | -20.35% |    -0.29 |       58 | 31.11%     | ok               |

## BCH-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 4.46%    | -53.26%            | -45.63% |     0.27 |       73 | 52.49%     | ok               |
|          25 | -2.23%   | -53.26%            | -51.09% |     0.19 |       68 | 48.28%     | ok               |
|          30 | -1.59%   | -53.26%            | -53.87% |     0.19 |       76 | 46.17%     | ok               |
|          15 | -7.48%   | -53.26%            | -50.38% |     0.15 |       82 | 57.09%     | ok               |
|          40 | -16.46%  | -53.26%            | -60.69% |    -0.02 |       63 | 39.27%     | ok               |

## BITO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 20.36%   | -56.99%            | -32.29% |     0.41 |       54 | 25.12%     | ok               |
|          30 | 6.28%    | -56.99%            | -42.82% |     0.25 |       78 | 39.77%     | ok               |
|          15 | -0.39%   | -56.99%            | -48.38% |     0.2  |       87 | 48.59%     | ok               |
|          45 | 0.39%    | -56.99%            | -43.53% |     0.16 |       58 | 28.12%     | ok               |
|          25 | -2.13%   | -56.99%            | -41.73% |     0.16 |       82 | 42.76%     | ok               |

## BLK Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 2.25%    | 26.21%             | -14.19% |     0.14 |       80 | 38.10%     | ok               |
|          40 | 0.86%    | 26.21%             | -15.20% |     0.09 |       70 | 33.94%     | ok               |
|          20 | -2.81%   | 26.21%             | -17.89% |    -0    |       77 | 46.42%     | ok               |
|          30 | -4.23%   | 26.21%             | -20.81% |    -0.06 |       75 | 41.93%     | ok               |
|          25 | -5.20%   | 26.21%             | -19.84% |    -0.08 |       75 | 44.26%     | ok               |

## BND Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -6.49%   | 0.91%              | -9.05%  |    -0.94 |       65 | 38.60%     | ok               |
|          25 | -6.87%   | 0.91%              | -10.14% |    -1.05 |       67 | 36.11%     | ok               |
|          30 | -7.32%   | 0.91%              | -9.89%  |    -1.18 |       65 | 32.28%     | ok               |
|          15 | -8.69%   | 0.91%              | -10.58% |    -1.25 |       75 | 41.43%     | ok               |
|          45 | -7.56%   | 0.91%              | -9.57%  |    -1.47 |       50 | 21.96%     | ok               |

## BONK-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 170.78%  | -85.73%            | -35.57% |     1.24 |       48 | 22.41%     | ok               |
|          25 | 169.76%  | -85.73%            | -51.34% |     1.04 |       67 | 47.70%     | ok               |
|          15 | 170.51%  | -85.73%            | -62.48% |     1    |       68 | 56.51%     | ok               |
|          20 | 154.52%  | -85.73%            | -58.35% |     0.99 |       67 | 52.30%     | ok               |
|          45 | 76.94%   | -85.73%            | -47.53% |     0.79 |       56 | 27.20%     | ok               |

## BTC-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 48.48%   | -34.65%            | -14.53% |     0.87 |       44 | 34.29%     | ok               |
|          45 | 41.09%   | -34.65%            | -15.18% |     0.81 |       44 | 30.65%     | ok               |
|          35 | 28.24%   | -34.65%            | -26.36% |     0.58 |       70 | 41.38%     | ok               |
|          50 | 14.18%   | -34.65%            | -16.15% |     0.4  |       42 | 25.29%     | ok               |
|          30 | 9.89%    | -34.65%            | -22.49% |     0.3  |       72 | 47.89%     | ok               |

## C Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -9.02%   | 167.99%            | -22.28% |    -0.18 |       68 | 35.11%     | ok               |
|          25 | -20.28%  | 167.99%            | -34.18% |    -0.34 |       75 | 52.58%     | ok               |
|          15 | -22.31%  | 167.99%            | -35.02% |    -0.36 |       76 | 59.23%     | ok               |
|          20 | -22.95%  | 167.99%            | -35.56% |    -0.4  |       83 | 55.57%     | ok               |
|          45 | -17.71%  | 167.99%            | -30.30% |    -0.41 |       82 | 39.60%     | ok               |

## CAT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 35.17%   | 214.65%            | -21.02% |     0.63 |       72 | 57.07%     | ok               |
|          25 | 35.30%   | 214.65%            | -26.37% |     0.63 |       68 | 59.90%     | ok               |
|          20 | 32.56%   | 214.65%            | -25.65% |     0.59 |       78 | 63.23%     | ok               |
|          45 | 22.72%   | 214.65%            | -28.85% |     0.49 |       56 | 45.59%     | ok               |
|          15 | 23.73%   | 214.65%            | -30.60% |     0.47 |       71 | 69.38%     | ok               |

## CL Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 17.30%   | 11.21%             | -12.98% |     0.69 |       44 | 32.61%     | ok               |
|          30 | 18.52%   | 11.21%             | -14.32% |     0.62 |       60 | 48.75%     | ok               |
|          45 | 11.94%   | 11.21%             | -13.51% |     0.49 |       48 | 35.61%     | ok               |
|          35 | 11.23%   | 11.21%             | -13.83% |     0.42 |       64 | 44.93%     | ok               |
|          40 | 8.01%    | 11.21%             | -12.70% |     0.34 |       58 | 39.60%     | ok               |

## CMCSA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -34.34%  | -41.00%            | -49.03% |    -0.74 |       85 | 59.07%     | ok               |
|          30 | -36.24%  | -41.00%            | -40.02% |    -0.9  |       80 | 44.59%     | ok               |
|          20 | -42.65%  | -41.00%            | -47.23% |    -1.07 |       91 | 55.41%     | ok               |
|          25 | -41.75%  | -41.00%            | -45.20% |    -1.07 |       87 | 49.92%     | ok               |
|          50 | -29.51%  | -41.00%            | -33.68% |    -1.08 |       50 | 17.14%     | ok               |

## COMP-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -3.83%   | -76.65%            | -38.71% |     0.15 |       46 | 20.69%     | ok               |
|          30 | -36.73%  | -76.65%            | -58.43% |    -0.21 |       89 | 45.02%     | ok               |
|          25 | -39.96%  | -76.65%            | -60.58% |    -0.22 |       89 | 50.19%     | ok               |
|          15 | -47.94%  | -76.65%            | -65.55% |    -0.31 |      103 | 61.69%     | ok               |
|          40 | -41.16%  | -76.65%            | -47.52% |    -0.37 |       74 | 33.14%     | ok               |

## COP Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -9.77%   | 6.94%              | -34.21% |    -0.15 |       48 | 27.29%     | ok               |
|          45 | -17.04%  | 6.94%              | -40.57% |    -0.33 |       60 | 30.28%     | ok               |
|          35 | -26.56%  | 6.94%              | -43.96% |    -0.52 |       77 | 37.44%     | ok               |
|          30 | -27.14%  | 6.94%              | -44.32% |    -0.53 |       75 | 40.93%     | ok               |
|          40 | -28.99%  | 6.94%              | -46.34% |    -0.65 |       70 | 33.11%     | ok               |

## COST Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | 18.65%   | 40.39%             | -24.73% |     0.56 |       61 | 50.25%     | ok               |
|          20 | 18.04%   | 40.39%             | -24.32% |     0.54 |       62 | 52.75%     | ok               |
|          35 | 11.83%   | 40.39%             | -26.58% |     0.41 |       54 | 43.76%     | ok               |
|          30 | 6.71%    | 40.39%             | -29.73% |     0.26 |       60 | 46.76%     | ok               |
|          40 | 4.97%    | 40.39%             | -28.41% |     0.22 |       56 | 40.77%     | ok               |

## CRM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -29.22%  | -40.74%            | -38.20% |    -0.42 |       90 | 55.41%     | ok               |
|          35 | -23.39%  | -40.74%            | -35.48% |    -0.43 |       62 | 38.77%     | ok               |
|          40 | -30.31%  | -40.74%            | -41.30% |    -0.68 |       68 | 34.94%     | ok               |
|          30 | -34.20%  | -40.74%            | -40.31% |    -0.68 |       65 | 43.59%     | ok               |
|          20 | -39.66%  | -40.74%            | -41.97% |    -0.73 |       78 | 49.08%     | ok               |

## CRV-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 36.28%   | -71.37%            | -37.78% |     0.55 |       62 | 28.74%     | ok               |
|          40 | 25.82%   | -71.37%            | -38.86% |     0.47 |       52 | 24.90%     | ok               |
|          50 | 23.26%   | -71.37%            | -29.30% |     0.45 |       38 | 16.48%     | ok               |
|          45 | 17.23%   | -71.37%            | -42.29% |     0.39 |       50 | 19.35%     | ok               |
|          30 | 8.89%    | -71.37%            | -39.89% |     0.32 |       62 | 33.14%     | ok               |

## CSCO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 28.99%   | 137.62%            | -19.34% |     0.64 |       58 | 38.77%     | ok               |
|          45 | 29.01%   | 137.62%            | -19.34% |     0.63 |       51 | 40.77%     | ok               |
|          30 | 26.11%   | 137.62%            | -21.79% |     0.55 |       59 | 49.25%     | ok               |
|          25 | 25.49%   | 137.62%            | -23.28% |     0.54 |       63 | 51.41%     | ok               |
|          35 | 23.21%   | 137.62%            | -23.68% |     0.51 |       51 | 46.76%     | ok               |

## CVX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -14.03%  | 30.64%             | -24.72% |    -0.32 |       72 | 44.59%     | ok               |
|          20 | -14.93%  | 30.64%             | -26.25% |    -0.34 |       72 | 45.76%     | ok               |
|          30 | -18.53%  | 30.64%             | -27.83% |    -0.49 |       71 | 42.10%     | ok               |
|          35 | -18.29%  | 30.64%             | -27.83% |    -0.49 |       71 | 39.10%     | ok               |
|          45 | -17.09%  | 30.64%             | -28.32% |    -0.52 |       63 | 30.62%     | ok               |

## DASH-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 130.50%  | -8.91%             | -31.38% |     0.96 |       42 | 16.86%     | ok               |
|          40 | 72.37%   | -8.91%             | -34.44% |     0.71 |       46 | 23.37%     | ok               |
|          45 | 66.46%   | -8.91%             | -39.58% |     0.68 |       46 | 19.16%     | ok               |
|          25 | -37.31%  | -8.91%             | -64.14% |     0.05 |       71 | 34.10%     | ok               |
|          35 | -37.12%  | -8.91%             | -63.23% |     0.03 |       71 | 27.78%     | ok               |

## DBC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | -9.68%   | 31.49%             | -23.38% |    -0.31 |       60 | 31.61%     | ok               |
|          50 | -8.54%   | 31.49%             | -19.91% |    -0.32 |       42 | 21.13%     | ok               |
|          45 | -9.90%   | 31.49%             | -21.08% |    -0.35 |       54 | 24.46%     | ok               |
|          30 | -12.57%  | 31.49%             | -25.35% |    -0.43 |       58 | 32.78%     | ok               |
|          15 | -13.57%  | 31.49%             | -27.30% |    -0.46 |       67 | 37.10%     | ok               |

## DE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -9.61%   | 48.58%             | -28.94% |    -0.12 |       74 | 51.08%     | ok               |
|          25 | -11.85%  | 48.58%             | -26.67% |    -0.18 |       76 | 48.42%     | ok               |
|          30 | -11.92%  | 48.58%             | -25.24% |    -0.18 |       76 | 45.59%     | ok               |
|          50 | -12.43%  | 48.58%             | -23.74% |    -0.28 |       62 | 30.12%     | ok               |
|          15 | -17.56%  | 48.58%             | -27.41% |    -0.3  |       80 | 54.41%     | ok               |

## DIA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | -1.02%   | 34.54%             | -13.15% |    -0.02 |       58 | 43.59%     | ok               |
|          25 | -1.55%   | 34.54%             | -11.28% |    -0.04 |       58 | 46.92%     | ok               |
|          30 | -3.07%   | 34.54%             | -12.94% |    -0.13 |       58 | 45.76%     | ok               |
|          20 | -4.92%   | 34.54%             | -13.85% |    -0.22 |       62 | 49.25%     | ok               |
|          40 | -5.05%   | 34.54%             | -15.06% |    -0.26 |       64 | 40.77%     | ok               |

## DIS Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 37.53%   | 7.82%              | -14.24% |     0.91 |       50 | 30.95%     | ok               |
|          45 | 8.69%    | 7.82%              | -15.37% |     0.28 |       51 | 34.44%     | ok               |
|          40 | 7.71%    | 7.82%              | -22.77% |     0.26 |       63 | 39.60%     | ok               |
|          35 | 0.76%    | 7.82%              | -22.75% |     0.12 |       71 | 45.26%     | ok               |
|          15 | -1.45%   | 7.82%              | -26.63% |     0.09 |       86 | 58.90%     | ok               |

## DOGE-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 15.01%   | -75.33%            | -57.89% |     0.41 |       81 | 64.75%     | ok               |
|          20 | 2.23%    | -75.33%            | -55.83% |     0.3  |       84 | 60.54%     | ok               |
|          25 | -1.66%   | -75.33%            | -53.72% |     0.25 |       72 | 54.98%     | ok               |
|          30 | -15.03%  | -75.33%            | -60.95% |     0.11 |       77 | 49.62%     | ok               |
|          35 | -44.36%  | -75.33%            | -63.16% |    -0.36 |       74 | 42.91%     | ok               |

## DOT-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -19.93%  | -86.51%            | -48.59% |    -0.1  |       52 | 30.46%     | ok               |
|          50 | -19.10%  | -86.51%            | -44.94% |    -0.11 |       56 | 26.25%     | ok               |
|          40 | -28.67%  | -86.51%            | -48.44% |    -0.2  |       56 | 33.91%     | ok               |
|          35 | -40.52%  | -86.51%            | -59.70% |    -0.26 |       80 | 41.00%     | ok               |
|          30 | -43.53%  | -86.51%            | -59.38% |    -0.29 |       90 | 47.51%     | ok               |

## DXY-INDEX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -2.92%   | -2.67%             | -9.99%  |    -0.31 |       68 | 58.35%     | ok               |
|          15 | -4.22%   | -2.67%             | -11.63% |    -0.37 |       90 | 75.70%     | ok               |
|          35 | -3.52%   | -2.67%             | -9.23%  |    -0.4  |       71 | 53.36%     | ok               |
|          40 | -3.54%   | -2.67%             | -7.30%  |    -0.44 |       68 | 47.07%     | ok               |
|          45 | -3.97%   | -2.67%             | -8.12%  |    -0.54 |       64 | 36.44%     | ok               |

## EEM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -2.91%   | 75.83%             | -15.88% |    -0.04 |       50 | 36.11%     | ok               |
|          45 | -4.62%   | 75.83%             | -17.36% |    -0.11 |       52 | 37.60%     | ok               |
|          40 | -4.96%   | 75.83%             | -19.52% |    -0.11 |       64 | 39.77%     | ok               |
|          35 | -5.62%   | 75.83%             | -23.88% |    -0.12 |       66 | 41.76%     | ok               |
|          30 | -9.40%   | 75.83%             | -25.67% |    -0.25 |       64 | 43.43%     | ok               |

## EFA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -1.25%   | 41.66%             | -10.80% |     0.02 |       58 | 52.08%     | ok               |
|          20 | -8.10%   | 41.66%             | -12.49% |    -0.27 |       65 | 49.08%     | ok               |
|          30 | -8.33%   | 41.66%             | -13.87% |    -0.3  |       58 | 43.93%     | ok               |
|          40 | -9.72%   | 41.66%             | -15.73% |    -0.39 |       62 | 40.10%     | ok               |
|          50 | -9.07%   | 41.66%             | -17.56% |    -0.4  |       54 | 36.27%     | ok               |

## EOG Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -19.95%  | 23.93%             | -39.57% |    -0.49 |       58 | 29.78%     | ok               |
|          45 | -22.18%  | 23.93%             | -38.89% |    -0.54 |       56 | 33.28%     | ok               |
|          30 | -29.07%  | 23.93%             | -48.13% |    -0.66 |       81 | 47.25%     | ok               |
|          40 | -27.23%  | 23.93%             | -42.30% |    -0.69 |       64 | 36.77%     | ok               |
|          35 | -29.43%  | 23.93%             | -45.93% |    -0.73 |       79 | 42.10%     | ok               |

## ETC-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -7.93%   | -72.15%            | -27.89% |    -0.02 |       28 | 17.05%     | ok               |
|          35 | -15.35%  | -72.15%            | -42.62% |    -0.11 |       44 | 26.63%     | ok               |
|          45 | -16.07%  | -72.15%            | -35.44% |    -0.17 |       26 | 18.97%     | ok               |
|          40 | -20.53%  | -72.15%            | -40.48% |    -0.25 |       40 | 22.41%     | ok               |
|          30 | -35.93%  | -72.15%            | -48.16% |    -0.52 |       64 | 30.84%     | ok               |

## ETH-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 166.66%  | -50.71%            | -30.11% |     1.32 |       60 | 44.44%     | ok               |
|          30 | 157.74%  | -50.71%            | -32.89% |     1.23 |       64 | 52.30%     | ok               |
|          40 | 68.63%   | -50.71%            | -33.11% |     0.84 |       56 | 36.97%     | ok               |
|          45 | 48.52%   | -50.71%            | -34.50% |     0.69 |       52 | 33.14%     | ok               |
|          50 | 32.53%   | -50.71%            | -30.50% |     0.56 |       54 | 27.01%     | ok               |

## EWJ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -18.27%  | 39.88%             | -30.73% |    -0.59 |       64 | 41.43%     | ok               |
|          20 | -19.65%  | 39.88%             | -31.32% |    -0.62 |       60 | 43.43%     | ok               |
|          45 | -19.05%  | 39.88%             | -27.68% |    -0.71 |       60 | 33.61%     | ok               |
|          25 | -21.97%  | 39.88%             | -31.18% |    -0.72 |       60 | 42.43%     | ok               |
|          35 | -22.19%  | 39.88%             | -32.54% |    -0.75 |       70 | 39.77%     | ok               |

## FCX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -7.45%   | 71.11%             | -26.57% |     0    |       56 | 29.62%     | ok               |
|          45 | -12.11%  | 71.11%             | -33.82% |    -0.06 |       56 | 33.94%     | ok               |
|          40 | -26.64%  | 71.11%             | -44.23% |    -0.33 |       68 | 39.10%     | ok               |
|          30 | -35.36%  | 71.11%             | -48.09% |    -0.46 |       71 | 46.26%     | ok               |
|          35 | -38.37%  | 71.11%             | -51.29% |    -0.56 |       75 | 43.93%     | ok               |

## FET-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 65.02%   | -86.49%            | -56.84% |     0.69 |       82 | 49.23%     | ok               |
|          15 | 13.69%   | -86.49%            | -59.22% |     0.42 |       84 | 52.49%     | ok               |
|          25 | 6.38%    | -86.49%            | -57.43% |     0.35 |       85 | 42.72%     | ok               |
|          30 | -3.74%   | -86.49%            | -48.39% |     0.25 |       73 | 38.70%     | ok               |
|          35 | -29.10%  | -86.49%            | -57.78% |    -0.08 |       61 | 32.18%     | ok               |

## FIL-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -0.14%   | -85.91%            | -39.40% |     0.17 |       46 | 22.80%     | ok               |
|          35 | -24.60%  | -85.91%            | -45.85% |    -0.17 |       56 | 26.82%     | ok               |
|          45 | -22.78%  | -85.91%            | -40.90% |    -0.2  |       42 | 17.05%     | ok               |
|          30 | -28.71%  | -85.91%            | -46.54% |    -0.21 |       68 | 32.18%     | ok               |
|          50 | -22.65%  | -85.91%            | -44.97% |    -0.25 |       36 | 12.84%     | ok               |

## FXI Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -11.98%  | 61.02%             | -22.99% |    -0.23 |       50 | 28.95%     | ok               |
|          50 | -11.32%  | 61.02%             | -23.56% |    -0.24 |       42 | 19.97%     | ok               |
|          30 | -12.49%  | 61.02%             | -24.33% |    -0.24 |       50 | 27.79%     | ok               |
|          15 | -13.43%  | 61.02%             | -21.68% |    -0.25 |       54 | 32.45%     | ok               |
|          45 | -13.55%  | 61.02%             | -26.75% |    -0.3  |       44 | 22.46%     | ok               |

## GDX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 21.88%   | 180.68%            | -31.87% |     0.46 |       64 | 43.09%     | ok               |
|          20 | 18.46%   | 180.68%            | -35.59% |     0.39 |       73 | 53.24%     | ok               |
|          35 | 13.76%   | 180.68%            | -32.37% |     0.34 |       68 | 45.59%     | ok               |
|          30 | 7.90%    | 180.68%            | -34.99% |     0.25 |       62 | 48.59%     | ok               |
|          25 | 7.14%    | 180.68%            | -33.46% |     0.24 |       63 | 50.08%     | ok               |

## GDXJ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -8.96%   | 198.26%            | -45.05% |     0.04 |       67 | 53.41%     | ok               |
|          50 | -7.07%   | 198.26%            | -35.86% |     0.01 |       56 | 37.10%     | ok               |
|          30 | -20.46%  | 198.26%            | -44.93% |    -0.18 |       68 | 46.42%     | ok               |
|          45 | -20.78%  | 198.26%            | -40.41% |    -0.23 |       62 | 39.77%     | ok               |
|          25 | -25.82%  | 198.26%            | -47.26% |    -0.25 |       73 | 49.75%     | ok               |

## GE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 27.69%   | 221.20%            | -22.29% |     0.58 |       66 | 38.27%     | ok               |
|          45 | 18.05%   | 221.20%            | -25.68% |     0.42 |       74 | 41.10%     | ok               |
|          20 | 17.18%   | 221.20%            | -26.63% |     0.39 |       69 | 54.91%     | ok               |
|          35 | 11.92%   | 221.20%            | -27.11% |     0.32 |       80 | 46.42%     | ok               |
|          15 | 12.18%   | 221.20%            | -28.62% |     0.32 |       68 | 57.24%     | ok               |

## GLD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | 29.14%   | 105.57%            | -14.61% |     0.73 |       46 | 45.09%     | ok               |
|          20 | 27.21%   | 105.57%            | -14.61% |     0.69 |       48 | 46.42%     | ok               |
|          30 | 22.99%   | 105.57%            | -16.63% |     0.61 |       48 | 43.93%     | ok               |
|          15 | 18.90%   | 105.57%            | -17.54% |     0.5  |       52 | 50.75%     | ok               |
|          35 | 16.99%   | 105.57%            | -17.29% |     0.49 |       50 | 43.26%     | ok               |

## GOOGL Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | 83.33%   | 144.41%            | -19.76% |     1.19 |       57 | 56.57%     | ok               |
|          30 | 74.57%   | 144.41%            | -20.41% |     1.12 |       63 | 54.41%     | ok               |
|          15 | 73.00%   | 144.41%            | -13.59% |     1.05 |       69 | 64.23%     | ok               |
|          20 | 69.48%   | 144.41%            | -20.57% |     1.04 |       68 | 58.90%     | ok               |
|          35 | 59.20%   | 144.41%            | -22.85% |     1    |       69 | 49.25%     | ok               |

## GRT-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 47.41%   | -91.04%            | -30.00% |     0.72 |       40 | 21.07%     | ok               |
|          45 | 14.72%   | -91.04%            | -48.76% |     0.36 |       48 | 25.48%     | ok               |
|          15 | 7.27%    | -91.04%            | -49.67% |     0.32 |       77 | 59.58%     | ok               |
|          20 | 6.66%    | -91.04%            | -46.47% |     0.31 |       85 | 54.60%     | ok               |
|          40 | 9.83%    | -91.04%            | -48.35% |     0.31 |       50 | 28.74%     | ok               |

## GS Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 24.19%   | 170.97%            | -20.56% |     0.52 |       76 | 59.57%     | ok               |
|          20 | 7.25%    | 170.97%            | -23.19% |     0.24 |       76 | 55.57%     | ok               |
|          25 | 1.85%    | 170.97%            | -23.32% |     0.14 |       74 | 53.08%     | ok               |
|          40 | -2.80%   | 170.97%            | -17.88% |     0.03 |       72 | 44.09%     | ok               |
|          30 | -4.14%   | 170.97%            | -22.13% |     0.01 |       76 | 50.75%     | ok               |

## HD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -6.00%   | -10.04%            | -17.69% |    -0.09 |       69 | 44.09%     | ok               |
|          25 | -6.74%   | -10.04%            | -18.51% |    -0.1  |       68 | 46.09%     | ok               |
|          40 | -11.56%  | -10.04%            | -19.63% |    -0.31 |       80 | 34.28%     | ok               |
|          35 | -14.75%  | -10.04%            | -22.98% |    -0.37 |       76 | 40.43%     | ok               |
|          45 | -14.18%  | -10.04%            | -20.74% |    -0.43 |       62 | 29.28%     | ok               |

## HON Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -17.09%  | 15.79%             | -23.31% |    -0.53 |       74 | 32.11%     | ok               |
|          45 | -19.07%  | 15.79%             | -22.37% |    -0.56 |       78 | 37.27%     | ok               |
|          40 | -27.01%  | 15.79%             | -27.01% |    -0.79 |       80 | 41.60%     | ok               |
|          35 | -28.41%  | 15.79%             | -28.41% |    -0.81 |       95 | 47.92%     | ok               |
|          30 | -30.75%  | 15.79%             | -30.75% |    -0.86 |       95 | 52.75%     | ok               |

## HYG Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -7.92%   | 3.59%              | -7.92%  |    -0.96 |       70 | 29.45%     | ok               |
|          15 | -9.71%   | 3.59%              | -10.06% |    -1.05 |       88 | 41.43%     | ok               |
|          20 | -9.69%   | 3.59%              | -10.29% |    -1.08 |       86 | 39.10%     | ok               |
|          45 | -8.60%   | 3.59%              | -8.60%  |    -1.08 |       66 | 26.29%     | ok               |
|          30 | -9.52%   | 3.59%              | -9.59%  |    -1.11 |       81 | 34.28%     | ok               |

## IBIT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 63.53%   | -5.16%             | -19.20% |     1.07 |       38 | 37.84%     | ok               |
|          50 | 50.99%   | -5.16%             | -13.31% |     1.07 |       20 | 22.11%     | ok               |
|          45 | 42.59%   | -5.16%             | -17.12% |     0.91 |       22 | 22.85%     | ok               |
|          40 | 41.19%   | -5.16%             | -17.12% |     0.89 |       24 | 24.32%     | ok               |
|          30 | 34.74%   | -5.16%             | -18.95% |     0.75 |       32 | 29.98%     | ok               |

## IBM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 29.75%   | 60.28%             | -28.20% |     0.57 |       87 | 62.73%     | ok               |
|          30 | 25.20%   | 60.28%             | -25.31% |     0.55 |       72 | 50.92%     | ok               |
|          35 | 22.69%   | 60.28%             | -25.15% |     0.51 |       68 | 46.59%     | ok               |
|          45 | 17.32%   | 60.28%             | -18.33% |     0.44 |       54 | 37.44%     | ok               |
|          40 | 14.95%   | 60.28%             | -24.66% |     0.39 |       64 | 41.26%     | ok               |

## ICP-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 36.44%   | -79.54%            | -29.38% |     0.56 |       58 | 26.63%     | ok               |
|          35 | 23.36%   | -79.54%            | -45.97% |     0.45 |       68 | 31.99%     | ok               |
|          50 | 18.18%   | -79.54%            | -37.33% |     0.4  |       40 | 16.67%     | ok               |
|          30 | 6.93%    | -79.54%            | -55.67% |     0.32 |       83 | 38.12%     | ok               |
|          45 | 3.40%    | -79.54%            | -38.80% |     0.23 |       58 | 20.69%     | ok               |

## IEF Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -7.21%   | -0.63%             | -9.79%  |    -0.86 |       72 | 42.43%     | ok               |
|          15 | -7.76%   | -0.63%             | -10.52% |    -0.91 |       71 | 43.93%     | ok               |
|          40 | -8.39%   | -0.63%             | -9.67%  |    -1.31 |       60 | 24.79%     | ok               |
|          45 | -8.07%   | -0.63%             | -9.73%  |    -1.33 |       50 | 22.80%     | ok               |
|          25 | -10.78%  | -0.63%             | -11.19% |    -1.37 |       78 | 39.60%     | ok               |

## IEMG Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -0.10%   | 69.57%             | -13.91% |     0.05 |       52 | 34.44%     | ok               |
|          35 | -0.32%   | 69.57%             | -22.13% |     0.05 |       63 | 42.60%     | ok               |
|          45 | -0.91%   | 69.57%             | -14.92% |     0.02 |       48 | 36.94%     | ok               |
|          40 | -2.44%   | 69.57%             | -18.43% |    -0.03 |       60 | 39.93%     | ok               |
|          25 | -4.72%   | 69.57%             | -25.58% |    -0.09 |       59 | 45.42%     | ok               |

## INJ-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | -25.22%  | -77.33%            | -60.42% |    -0.07 |       62 | 32.76%     | ok               |
|          45 | -20.02%  | -77.33%            | -55.31% |    -0.08 |       46 | 22.61%     | ok               |
|          50 | -22.38%  | -77.33%            | -51.00% |    -0.14 |       48 | 19.35%     | ok               |
|          40 | -32.90%  | -77.33%            | -57.21% |    -0.24 |       52 | 28.93%     | ok               |
|          15 | -63.68%  | -77.33%            | -83.89% |    -0.55 |       83 | 51.34%     | ok               |

## INTC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 76.11%   | 142.91%            | -49.32% |     0.74 |       60 | 34.28%     | ok               |
|          15 | 82.95%   | 142.91%            | -53.65% |     0.74 |       84 | 61.23%     | ok               |
|          25 | 75.50%   | 142.91%            | -56.41% |     0.72 |       75 | 51.58%     | ok               |
|          40 | 70.33%   | 142.91%            | -55.86% |     0.7  |       68 | 38.60%     | ok               |
|          20 | 72.70%   | 142.91%            | -52.47% |     0.7  |       82 | 56.57%     | ok               |

## INTU Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 4.48%    | -55.49%            | -42.82% |     0.2  |       71 | 28.95%     | ok               |
|          45 | 0.91%    | -55.49%            | -44.66% |     0.13 |       69 | 33.11%     | ok               |
|          40 | -5.44%   | -55.49%            | -48.32% |     0.02 |       71 | 35.94%     | ok               |
|          25 | -6.78%   | -55.49%            | -42.24% |     0.01 |       66 | 45.26%     | ok               |
|          15 | -7.88%   | -55.49%            | -46.90% |     0    |       81 | 50.75%     | ok               |

## ITA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 2.30%    | 93.94%             | -21.48% |     0.14 |       74 | 36.44%     | ok               |
|          15 | -2.43%   | 93.94%             | -28.17% |     0.02 |       86 | 58.40%     | ok               |
|          30 | -1.83%   | 93.94%             | -23.75% |     0.02 |       72 | 46.42%     | ok               |
|          35 | -4.36%   | 93.94%             | -23.16% |    -0.06 |       76 | 44.59%     | ok               |
|          40 | -5.46%   | 93.94%             | -20.58% |    -0.11 |       78 | 41.10%     | ok               |

## IWM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 8.72%    | 50.92%             | -12.83% |     0.36 |       50 | 37.10%     | ok               |
|          25 | 8.83%    | 50.92%             | -14.87% |     0.36 |       52 | 38.27%     | ok               |
|          40 | 6.51%    | 50.92%             | -14.38% |     0.31 |       44 | 32.45%     | ok               |
|          35 | 6.26%    | 50.92%             | -14.41% |     0.28 |       50 | 34.78%     | ok               |
|          15 | 5.26%    | 50.92%             | -17.63% |     0.23 |       71 | 42.76%     | ok               |

## JNJ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 16.18%   | 47.41%             | -10.70% |     0.71 |       62 | 36.94%     | ok               |
|          15 | 15.85%   | 47.41%             | -18.02% |     0.56 |       66 | 57.74%     | ok               |
|          20 | 11.93%   | 47.41%             | -17.61% |     0.46 |       70 | 54.41%     | ok               |
|          45 | 7.47%    | 47.41%             | -13.80% |     0.35 |       64 | 42.10%     | ok               |
|          25 | 7.41%    | 47.41%             | -17.84% |     0.31 |       71 | 52.58%     | ok               |

## JPM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 14.46%   | 84.07%             | -15.90% |     0.52 |       56 | 40.10%     | ok               |
|          45 | 4.58%    | 84.07%             | -21.91% |     0.21 |       56 | 43.26%     | ok               |
|          40 | -9.23%   | 84.07%             | -28.47% |    -0.21 |       68 | 45.76%     | ok               |
|          20 | -15.79%  | 84.07%             | -33.59% |    -0.29 |       88 | 57.07%     | ok               |
|          35 | -14.30%  | 84.07%             | -27.43% |    -0.35 |       74 | 49.42%     | ok               |

## KO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 27.96%   | 37.94%             | -8.07%  |     1    |       51 | 37.94%     | ok               |
|          35 | 24.04%   | 37.94%             | -8.07%  |     0.89 |       54 | 36.61%     | ok               |
|          40 | 21.45%   | 37.94%             | -9.28%  |     0.87 |       56 | 33.44%     | ok               |
|          25 | 22.68%   | 37.94%             | -9.37%  |     0.83 |       57 | 40.60%     | ok               |
|          50 | 14.84%   | 37.94%             | -11.40% |     0.68 |       36 | 26.79%     | ok               |

## LDO-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 28.06%   | -84.96%            | -43.71% |     0.5  |       91 | 47.70%     | ok               |
|          15 | 26.48%   | -84.96%            | -43.48% |     0.5  |       86 | 52.49%     | ok               |
|          30 | 15.20%   | -84.96%            | -58.32% |     0.4  |       78 | 38.31%     | ok               |
|          25 | -1.60%   | -84.96%            | -54.15% |     0.28 |       87 | 43.87%     | ok               |
|          35 | -6.84%   | -84.96%            | -63.16% |     0.18 |       80 | 31.03%     | ok               |

## LIN Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 3.11%    | 26.53%             | -23.70% |     0.16 |       65 | 49.92%     | ok               |
|          25 | 1.83%    | 26.53%             | -22.01% |     0.12 |       67 | 41.93%     | ok               |
|          20 | -0.35%   | 26.53%             | -23.00% |     0.05 |       66 | 45.09%     | ok               |
|          35 | -1.85%   | 26.53%             | -21.18% |    -0.01 |       66 | 32.61%     | ok               |
|          30 | -2.47%   | 26.53%             | -21.53% |    -0.03 |       70 | 39.10%     | ok               |

## LINK-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -10.11%  | -63.21%            | -50.48% |     0.14 |       70 | 41.19%     | ok               |
|          45 | -11.70%  | -63.21%            | -38.56% |     0.07 |       48 | 26.25%     | ok               |
|          50 | -13.50%  | -63.21%            | -36.98% |     0.02 |       40 | 21.07%     | ok               |
|          35 | -21.89%  | -63.21%            | -49.56% |    -0.02 |       60 | 36.21%     | ok               |
|          40 | -26.07%  | -63.21%            | -50.91% |    -0.11 |       54 | 30.46%     | ok               |

## LLY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 33.93%   | 84.69%             | -38.23% |     0.67 |       42 | 39.27%     | ok               |
|          45 | 21.09%   | 84.69%             | -42.66% |     0.46 |       50 | 42.43%     | ok               |
|          15 | 14.19%   | 84.69%             | -48.12% |     0.34 |       63 | 61.90%     | ok               |
|          40 | 2.97%    | 84.69%             | -46.23% |     0.18 |       62 | 44.93%     | ok               |
|          20 | -4.20%   | 84.69%             | -51.34% |     0.07 |       72 | 56.91%     | ok               |

## LRCX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 5.24%    | 338.72%            | -60.45% |     0.24 |       83 | 55.57%     | ok               |
|          50 | -0.82%   | 338.72%            | -50.39% |     0.14 |       80 | 37.44%     | ok               |
|          40 | -3.80%   | 338.72%            | -56.86% |     0.11 |       72 | 43.26%     | ok               |
|          35 | -10.04%  | 338.72%            | -61.76% |     0.04 |       80 | 45.26%     | ok               |
|          20 | -12.65%  | 338.72%            | -67.64% |     0.01 |       87 | 51.25%     | ok               |

## LTC-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -10.95%  | -58.64%            | -44.78% |     0.02 |       56 | 31.80%     | ok               |
|          35 | -16.96%  | -58.64%            | -54.86% |    -0.04 |       66 | 42.53%     | ok               |
|          40 | -26.53%  | -58.64%            | -56.10% |    -0.21 |       58 | 37.74%     | ok               |
|          30 | -29.31%  | -58.64%            | -53.76% |    -0.21 |       66 | 48.08%     | ok               |
|          25 | -32.29%  | -58.64%            | -54.26% |    -0.25 |       74 | 50.57%     | ok               |

## MCD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 3.90%    | -5.24%             | -9.22%  |     0.24 |       42 | 20.63%     | ok               |
|          30 | -3.77%   | -5.24%             | -18.81% |    -0.1  |       77 | 38.27%     | ok               |
|          25 | -4.80%   | -5.24%             | -20.47% |    -0.13 |       77 | 40.93%     | ok               |
|          40 | -6.63%   | -5.24%             | -16.86% |    -0.26 |       69 | 28.95%     | ok               |
|          35 | -8.84%   | -5.24%             | -15.45% |    -0.34 |       69 | 34.61%     | ok               |

## META Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 11.51%   | 48.24%             | -31.03% |     0.3  |       66 | 40.60%     | ok               |
|          40 | -0.74%   | 48.24%             | -35.11% |     0.11 |       66 | 43.59%     | ok               |
|          50 | -5.51%   | 48.24%             | -34.00% |     0.02 |       70 | 36.77%     | ok               |
|          25 | -10.54%  | 48.24%             | -39.84% |    -0.03 |       67 | 54.24%     | ok               |
|          35 | -12.14%  | 48.24%             | -34.87% |    -0.07 |       77 | 48.42%     | ok               |

## MPC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 14.51%   | 70.49%             | -23.96% |     0.37 |       52 | 38.60%     | ok               |
|          45 | 7.25%    | 70.49%             | -25.09% |     0.24 |       58 | 42.26%     | ok               |
|          40 | 5.62%    | 70.49%             | -25.70% |     0.22 |       60 | 44.59%     | ok               |
|          35 | 2.36%    | 70.49%             | -35.90% |     0.16 |       68 | 47.09%     | ok               |
|          30 | -13.74%  | 70.49%             | -44.76% |    -0.14 |       71 | 49.92%     | ok               |

## MRK Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -11.64%  | 1.57%              | -29.91% |    -0.16 |       85 | 57.74%     | ok               |
|          25 | -11.22%  | 1.57%              | -31.07% |    -0.17 |       70 | 49.75%     | ok               |
|          20 | -15.57%  | 1.57%              | -29.38% |    -0.27 |       75 | 53.08%     | ok               |
|          30 | -21.49%  | 1.57%              | -32.14% |    -0.46 |       69 | 46.92%     | ok               |
|          35 | -21.28%  | 1.57%              | -31.51% |    -0.46 |       71 | 43.26%     | ok               |

## MS Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -4.79%   | 149.19%            | -19.99% |    -0.05 |       70 | 39.27%     | ok               |
|          35 | -11.48%  | 149.19%            | -25.26% |    -0.22 |       76 | 43.93%     | ok               |
|          15 | -16.20%  | 149.19%            | -23.85% |    -0.28 |       82 | 56.41%     | ok               |
|          20 | -16.65%  | 149.19%            | -25.68% |    -0.33 |       84 | 52.41%     | ok               |
|          30 | -16.84%  | 149.19%            | -27.79% |    -0.36 |       79 | 47.42%     | ok               |

## MSFT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -15.68%  | -2.09%             | -26.27% |    -0.43 |       64 | 35.61%     | ok               |
|          50 | -19.48%  | -2.09%             | -28.83% |    -0.58 |       62 | 30.95%     | ok               |
|          35 | -27.78%  | -2.09%             | -33.68% |    -0.73 |       73 | 43.93%     | ok               |
|          25 | -31.30%  | -2.09%             | -37.59% |    -0.78 |       85 | 51.58%     | ok               |
|          40 | -28.63%  | -2.09%             | -34.46% |    -0.79 |       69 | 38.94%     | ok               |

## MU Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 358.25%  | 1038.01%           | -61.96% |     1.47 |       48 | 67.22%     | ok               |
|          25 | 281.78%  | 1038.01%           | -67.90% |     1.37 |       49 | 60.90%     | ok               |
|          40 | 240.53%  | 1038.01%           | -64.36% |     1.3  |       56 | 54.58%     | ok               |
|          20 | 249.53%  | 1038.01%           | -67.25% |     1.28 |       55 | 63.06%     | ok               |
|          30 | 225.21%  | 1038.01%           | -68.76% |     1.25 |       51 | 59.07%     | ok               |

## NEAR-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 103.12%  | -62.04%            | -48.01% |     0.99 |       44 | 23.37%     | ok               |
|          50 | 70.90%   | -62.04%            | -53.13% |     0.82 |       38 | 18.39%     | ok               |
|          40 | 60.91%   | -62.04%            | -56.35% |     0.73 |       48 | 27.78%     | ok               |
|          35 | 34.38%   | -62.04%            | -60.30% |     0.54 |       70 | 33.33%     | ok               |
|          15 | 9.65%    | -62.04%            | -54.94% |     0.37 |       92 | 56.90%     | ok               |

## NEM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 33.92%   | 182.22%            | -25.79% |     0.53 |       60 | 64.39%     | ok               |
|          20 | 21.32%   | 182.22%            | -30.47% |     0.41 |       72 | 59.90%     | ok               |
|          25 | -7.72%   | 182.22%            | -30.80% |     0.06 |       70 | 57.57%     | ok               |
|          50 | -11.41%  | 182.22%            | -33.36% |    -0.03 |       60 | 41.26%     | ok               |
|          30 | -25.68%  | 182.22%            | -38.49% |    -0.23 |       76 | 55.41%     | ok               |

## NFLX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 48.18%   | 68.28%             | -11.94% |     1.05 |       44 | 46.59%     | ok               |
|          50 | 35.59%   | 68.28%             | -16.28% |     0.88 |       46 | 39.10%     | ok               |
|          35 | 40.11%   | 68.28%             | -18.30% |     0.86 |       60 | 50.25%     | ok               |
|          45 | 32.16%   | 68.28%             | -15.48% |     0.78 |       50 | 42.93%     | ok               |
|          15 | 34.20%   | 68.28%             | -26.59% |     0.68 |       63 | 64.56%     | ok               |

## NKE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | -27.08%  | -54.84%            | -42.13% |    -0.38 |       77 | 37.60%     | ok               |
|          20 | -36.28%  | -54.84%            | -50.44% |    -0.47 |       97 | 53.58%     | ok               |
|          25 | -37.23%  | -54.84%            | -51.20% |    -0.5  |       95 | 49.58%     | ok               |
|          40 | -27.49%  | -54.84%            | -31.19% |    -0.53 |       65 | 30.28%     | ok               |
|          30 | -37.96%  | -54.84%            | -55.35% |    -0.53 |       93 | 44.09%     | ok               |

## NOW Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 20.09%   | -31.20%            | -26.36% |     0.4  |       77 | 51.91%     | ok               |
|          30 | 19.56%   | -31.20%            | -30.25% |     0.4  |       78 | 45.92%     | ok               |
|          35 | 14.94%   | -31.20%            | -29.30% |     0.35 |       77 | 40.77%     | ok               |
|          15 | 13.60%   | -31.20%            | -26.36% |     0.33 |       85 | 55.24%     | ok               |
|          25 | 12.77%   | -31.20%            | -25.70% |     0.32 |       70 | 49.25%     | ok               |

## NVDA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -3.91%   | 131.61%            | -33.22% |     0.12 |       68 | 51.87%     | ok               |
|          30 | -5.71%   | 131.61%            | -35.26% |     0.07 |       70 | 49.55%     | ok               |
|          20 | -10.29%  | 131.61%            | -40.59% |     0.04 |       71 | 56.33%     | ok               |
|          50 | -13.53%  | 131.61%            | -40.84% |    -0.09 |       60 | 33.69%     | ok               |
|          35 | -16.76%  | 131.61%            | -41.25% |    -0.11 |       82 | 46.70%     | ok               |

## OP-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 82.25%   | -94.95%            | -45.76% |     0.92 |       36 | 17.43%     | ok               |
|          40 | 82.20%   | -94.95%            | -53.61% |     0.87 |       48 | 25.67%     | ok               |
|          50 | 66.86%   | -94.95%            | -36.11% |     0.86 |       34 | 12.45%     | ok               |
|          35 | 52.37%   | -94.95%            | -58.13% |     0.67 |       56 | 28.93%     | ok               |
|          30 | 20.19%   | -94.95%            | -70.11% |     0.42 |       72 | 35.63%     | ok               |

## ORCL Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 142.88%  | 67.87%             | -25.81% |     1.06 |       71 | 64.89%     | ok               |
|          25 | 82.20%   | 67.87%             | -24.79% |     0.79 |       72 | 57.40%     | ok               |
|          20 | 79.07%   | 67.87%             | -25.81% |     0.77 |       74 | 60.57%     | ok               |
|          35 | 56.17%   | 67.87%             | -31.95% |     0.65 |       64 | 49.08%     | ok               |
|          30 | 56.30%   | 67.87%             | -29.47% |     0.65 |       70 | 53.24%     | ok               |

## OXY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -0.42%   | -1.68%             | -30.85% |     0.11 |       65 | 43.76%     | ok               |
|          35 | -1.28%   | -1.68%             | -30.50% |     0.09 |       70 | 38.77%     | ok               |
|          50 | -1.47%   | -1.68%             | -31.07% |     0.07 |       38 | 27.95%     | ok               |
|          40 | -3.09%   | -1.68%             | -32.21% |     0.05 |       56 | 34.61%     | ok               |
|          45 | -11.35%  | -1.68%             | -37.99% |    -0.14 |       48 | 30.28%     | ok               |

## PEP Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 8.75%    | -13.30%            | -11.62% |     0.41 |       44 | 27.79%     | ok               |
|          45 | -0.21%   | -13.30%            | -14.22% |     0.04 |       70 | 32.78%     | ok               |
|          40 | -3.72%   | -13.30%            | -18.04% |    -0.08 |       78 | 38.60%     | ok               |
|          35 | -5.27%   | -13.30%            | -21.42% |    -0.1  |       87 | 43.59%     | ok               |
|          30 | -10.58%  | -13.30%            | -21.35% |    -0.25 |       85 | 50.08%     | ok               |

## PEPE-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 17.18%   | -85.07%            | -57.66% |     0.42 |       77 | 43.30%     | ok               |
|          35 | 9.32%    | -85.07%            | -51.35% |     0.34 |       62 | 38.12%     | ok               |
|          25 | -8.94%   | -85.07%            | -56.30% |     0.2  |       85 | 48.66%     | ok               |
|          15 | -26.32%  | -85.07%            | -65.75% |     0.12 |       81 | 58.24%     | ok               |
|          40 | -18.46%  | -85.07%            | -60.13% |     0.02 |       58 | 33.33%     | ok               |

## PFE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -22.05%  | -7.46%             | -26.62% |    -0.76 |       52 | 21.46%     | ok               |
|          50 | -24.42%  | -7.46%             | -27.87% |    -0.93 |       44 | 17.64%     | ok               |
|          40 | -28.66%  | -7.46%             | -32.84% |    -0.96 |       76 | 26.29%     | ok               |
|          35 | -31.40%  | -7.46%             | -36.39% |    -0.98 |       82 | 33.44%     | ok               |
|          30 | -37.76%  | -7.46%             | -42.29% |    -1.17 |       77 | 36.94%     | ok               |

## PG Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 0.02%    | 0.52%              | -19.77% |     0.05 |       52 | 34.61%     | ok               |
|          35 | -2.20%   | 0.52%              | -18.66% |    -0.04 |       60 | 37.94%     | ok               |
|          30 | -11.08%  | 0.52%              | -21.65% |    -0.39 |       62 | 41.10%     | ok               |
|          45 | -9.75%   | 0.52%              | -20.43% |    -0.4  |       52 | 32.11%     | ok               |
|          25 | -12.15%  | 0.52%              | -22.55% |    -0.43 |       72 | 42.26%     | ok               |

## PM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 2.70%    | 95.81%             | -32.20% |     0.15 |       86 | 53.41%     | ok               |
|          20 | 1.41%    | 95.81%             | -31.89% |     0.13 |       89 | 62.23%     | ok               |
|          30 | 1.14%    | 95.81%             | -33.68% |     0.12 |       83 | 57.24%     | ok               |
|          25 | -5.83%   | 95.81%             | -37.05% |    -0.03 |       83 | 59.57%     | ok               |
|          50 | -4.69%   | 95.81%             | -35.70% |    -0.03 |       76 | 43.26%     | ok               |

## POL-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 69.37%   | -84.21%            | -46.45% |     0.8  |       79 | 48.85%     | ok               |
|          25 | 59.04%   | -84.21%            | -46.72% |     0.71 |       70 | 57.66%     | ok               |
|          20 | 51.26%   | -84.21%            | -52.88% |     0.65 |       78 | 62.64%     | ok               |
|          15 | 44.08%   | -84.21%            | -58.42% |     0.6  |       78 | 68.39%     | ok               |
|          50 | 22.37%   | -84.21%            | -22.86% |     0.48 |       48 | 20.50%     | ok               |

## QCOM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -6.64%   | 33.56%             | -55.66% |     0.09 |       73 | 50.08%     | ok               |
|          35 | -8.83%   | 33.56%             | -51.84% |     0.05 |       83 | 45.42%     | ok               |
|          20 | -13.47%  | 33.56%             | -57.05% |     0    |       70 | 53.08%     | ok               |
|          30 | -18.79%  | 33.56%             | -57.69% |    -0.09 |       77 | 48.09%     | ok               |
|          15 | -27.85%  | 33.56%             | -60.40% |    -0.2  |       74 | 56.24%     | ok               |

## QQQ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | 19.81%   | 70.26%             | -12.88% |     0.55 |       55 | 48.92%     | ok               |
|          15 | 20.29%   | 70.26%             | -14.17% |     0.53 |       61 | 54.41%     | ok               |
|          30 | 15.89%   | 70.26%             | -12.88% |     0.48 |       60 | 46.09%     | ok               |
|          20 | 16.91%   | 70.26%             | -12.98% |     0.47 |       63 | 51.58%     | ok               |
|          35 | 4.05%    | 70.26%             | -18.29% |     0.19 |       66 | 42.43%     | ok               |

## RENDER-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 51.64%   | -60.91%            | -43.43% |     0.67 |       82 | 54.72%     | ok               |
|          15 | 34.03%   | -60.91%            | -44.59% |     0.56 |       82 | 57.86%     | ok               |
|          25 | 21.59%   | -60.91%            | -40.60% |     0.48 |       86 | 50.73%     | ok               |
|          30 | -16.54%  | -60.91%            | -45.00% |     0.13 |       94 | 44.23%     | ok               |
|          40 | -25.92%  | -60.91%            | -38.60% |    -0.08 |       68 | 29.56%     | ok               |

## RTX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 26.11%   | 115.37%            | -18.66% |     0.65 |       76 | 56.07%     | ok               |
|          50 | 18.93%   | 115.37%            | -18.42% |     0.61 |       56 | 41.93%     | ok               |
|          25 | 21.63%   | 115.37%            | -18.59% |     0.57 |       62 | 52.58%     | ok               |
|          30 | 19.78%   | 115.37%            | -16.99% |     0.54 |       56 | 51.41%     | ok               |
|          35 | 17.25%   | 115.37%            | -18.00% |     0.53 |       54 | 49.58%     | ok               |

## SBUX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -14.66%  | 8.97%              | -23.55% |    -0.24 |       62 | 41.43%     | ok               |
|          40 | -18.77%  | 8.97%              | -25.69% |    -0.4  |       58 | 31.61%     | ok               |
|          45 | -17.88%  | 8.97%              | -27.26% |    -0.41 |       62 | 27.79%     | ok               |
|          30 | -23.09%  | 8.97%              | -30.54% |    -0.47 |       65 | 38.94%     | ok               |
|          20 | -27.22%  | 8.97%              | -35.01% |    -0.52 |       67 | 43.59%     | ok               |

## SCHW Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 2.59%    | 39.07%             | -15.92% |     0.15 |       54 | 33.44%     | ok               |
|          50 | -1.42%   | 39.07%             | -11.75% |     0.01 |       50 | 30.95%     | ok               |
|          40 | -8.05%   | 39.07%             | -21.81% |    -0.15 |       62 | 36.44%     | ok               |
|          25 | -10.23%  | 39.07%             | -28.76% |    -0.16 |       61 | 47.75%     | ok               |
|          20 | -11.91%  | 39.07%             | -29.24% |    -0.2  |       69 | 50.42%     | ok               |

## SHIB-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 1.12%    | -77.90%            | -49.21% |     0.26 |       76 | 67.43%     | ok               |
|          25 | -6.57%   | -77.90%            | -43.85% |     0.16 |       75 | 58.81%     | ok               |
|          20 | -10.24%  | -77.90%            | -46.92% |     0.13 |       79 | 63.41%     | ok               |
|          35 | -9.86%   | -77.90%            | -53.32% |     0.09 |       64 | 45.98%     | ok               |
|          40 | -14.81%  | -77.90%            | -50.74% |     0.01 |       54 | 38.31%     | ok               |

## SHY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd    |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:-------|---------:|---------:|:-----------|:-----------------|
|          30 | -2.12%   | 0.07%              | -2.85% |    -0.73 |       50 | 35.77%     | ok               |
|          35 | -2.24%   | 0.07%              | -3.27% |    -0.78 |       52 | 33.94%     | ok               |
|          40 | -2.35%   | 0.07%              | -3.33% |    -0.83 |       52 | 32.11%     | ok               |
|          45 | -2.33%   | 0.07%              | -3.23% |    -0.84 |       50 | 28.95%     | ok               |
|          50 | -2.50%   | 0.07%              | -3.40% |    -0.95 |       46 | 26.12%     | ok               |

## SKY-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -32.39%  | -1.99%             | -56.39% |    -0.36 |       58 | 50.48%     | ok               |
|          30 | -28.24%  | -1.99%             | -43.98% |    -0.36 |       68 | 40.24%     | ok               |
|          25 | -31.92%  | -1.99%             | -48.09% |    -0.42 |       63 | 44.05%     | ok               |
|          20 | -42.29%  | -1.99%             | -58.40% |    -0.61 |       60 | 47.86%     | ok               |
|          35 | -38.94%  | -1.99%             | -49.68% |    -0.71 |       60 | 34.05%     | ok               |

## SLB Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 12.74%   | 12.81%             | -23.07% |     0.35 |       46 | 35.44%     | ok               |
|          45 | 11.08%   | 12.81%             | -20.46% |     0.33 |       52 | 32.11%     | ok               |
|          50 | -8.84%   | 12.81%             | -28.89% |    -0.13 |       52 | 28.45%     | ok               |
|          35 | -15.57%  | 12.81%             | -41.81% |    -0.22 |       74 | 43.43%     | ok               |
|          30 | -31.56%  | 12.81%             | -54.95% |    -0.58 |       77 | 50.08%     | ok               |

## SLV Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 60.17%   | 194.24%            | -29.75% |     0.8  |       62 | 35.94%     | ok               |
|          50 | 56.72%   | 194.24%            | -34.10% |     0.78 |       50 | 32.95%     | ok               |
|          45 | 51.82%   | 194.24%            | -31.82% |     0.73 |       56 | 33.94%     | ok               |
|          35 | 46.20%   | 194.24%            | -36.89% |     0.67 |       64 | 38.27%     | ok               |
|          30 | 30.22%   | 194.24%            | -42.66% |     0.52 |       60 | 40.27%     | ok               |

## SMH Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 117.25%  | 225.60%            | -31.01% |     1.32 |       49 | 54.08%     | ok               |
|          35 | 96.79%   | 225.60%            | -34.36% |     1.22 |       54 | 49.75%     | ok               |
|          25 | 96.64%   | 225.60%            | -32.94% |     1.2  |       46 | 52.75%     | ok               |
|          30 | 94.32%   | 225.60%            | -33.99% |     1.19 |       48 | 51.08%     | ok               |
|          45 | 80.19%   | 225.60%            | -32.75% |     1.14 |       52 | 43.93%     | ok               |

## SNX-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 34.81%   | -87.34%            | -28.28% |     0.55 |       68 | 32.95%     | ok               |
|          30 | 23.84%   | -87.34%            | -32.91% |     0.46 |       63 | 40.42%     | ok               |
|          20 | 16.58%   | -87.34%            | -43.20% |     0.41 |       73 | 50.57%     | ok               |
|          25 | -1.24%   | -87.34%            | -36.73% |     0.25 |       76 | 44.83%     | ok               |
|          15 | -21.36%  | -87.34%            | -47.56% |     0.08 |       83 | 54.60%     | ok               |

## SOL-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -5.81%   | -67.07%            | -51.20% |     0.18 |       64 | 39.08%     | ok               |
|          25 | -22.52%  | -67.07%            | -51.71% |     0.03 |       72 | 56.90%     | ok               |
|          35 | -23.35%  | -67.07%            | -59.05% |     0.01 |       72 | 46.55%     | ok               |
|          15 | -30.55%  | -67.07%            | -57.85% |    -0.04 |       78 | 64.18%     | ok               |
|          20 | -33.65%  | -67.07%            | -55.52% |    -0.1  |       68 | 59.39%     | ok               |

## SOXX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 95.21%   | 192.86%            | -38.67% |     1.13 |       53 | 52.58%     | ok               |
|          25 | 91.48%   | 192.86%            | -39.85% |     1.1  |       51 | 52.25%     | ok               |
|          35 | 86.13%   | 192.86%            | -38.63% |     1.08 |       59 | 47.59%     | ok               |
|          15 | 90.31%   | 192.86%            | -37.72% |     1.06 |       66 | 55.41%     | ok               |
|          30 | 80.72%   | 192.86%            | -40.34% |     1.02 |       55 | 50.08%     | ok               |

## SPY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 18.02%   | 52.93%             | -14.25% |     0.62 |       56 | 53.91%     | ok               |
|          15 | 16.85%   | 52.93%             | -16.80% |     0.57 |       63 | 56.91%     | ok               |
|          25 | 11.22%   | 52.93%             | -15.22% |     0.42 |       56 | 53.24%     | ok               |
|          30 | 7.21%    | 52.93%             | -16.47% |     0.31 |       58 | 50.75%     | ok               |
|          35 | 3.93%    | 52.93%             | -16.72% |     0.2  |       58 | 48.25%     | ok               |

## SUSHI-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -24.39%  | -88.81%            | -40.79% |    -0.2  |       52 | 14.56%     | ok               |
|          45 | -56.30%  | -88.81%            | -64.69% |    -0.71 |       54 | 17.82%     | ok               |
|          40 | -60.87%  | -88.81%            | -66.97% |    -0.76 |       63 | 24.52%     | ok               |
|          35 | -68.20%  | -88.81%            | -75.30% |    -0.88 |       78 | 29.89%     | ok               |
|          15 | -81.80%  | -88.81%            | -81.91% |    -1.06 |       92 | 47.70%     | ok               |

## T Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 53.29%   | 37.97%             | -18.13% |     1.1  |       57 | 54.58%     | ok               |
|          25 | 45.42%   | 37.97%             | -17.66% |     0.99 |       62 | 52.25%     | ok               |
|          15 | 44.91%   | 37.97%             | -15.08% |     0.94 |       66 | 58.40%     | ok               |
|          35 | 32.38%   | 37.97%             | -14.49% |     0.8  |       64 | 46.76%     | ok               |
|          30 | 30.91%   | 37.97%             | -17.01% |     0.75 |       64 | 50.08%     | ok               |

## TGT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -6.81%   | -3.98%             | -40.99% |    -0.02 |       77 | 45.92%     | ok               |
|          15 | -9.86%   | -3.98%             | -38.83% |    -0.07 |       67 | 50.42%     | ok               |
|          25 | -10.93%  | -3.98%             | -43.53% |    -0.13 |       61 | 41.26%     | ok               |
|          45 | -10.17%  | -3.98%             | -30.47% |    -0.16 |       50 | 28.95%     | ok               |
|          30 | -11.79%  | -3.98%             | -41.74% |    -0.16 |       56 | 38.60%     | ok               |

## TIA-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 42.83%   | -93.40%            | -40.13% |     0.6  |       60 | 28.54%     | ok               |
|          40 | 36.53%   | -93.40%            | -39.80% |     0.55 |       60 | 24.52%     | ok               |
|          45 | 26.69%   | -93.40%            | -39.18% |     0.48 |       50 | 18.20%     | ok               |
|          50 | 23.09%   | -93.40%            | -40.62% |     0.48 |       32 | 11.30%     | ok               |
|          30 | -6.82%   | -93.40%            | -55.60% |     0.18 |       82 | 33.14%     | ok               |

## TLT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -13.85%  | -8.62%             | -16.11% |    -1.46 |       34 | 14.98%     | ok               |
|          30 | -23.31%  | -8.62%             | -24.69% |    -1.71 |       70 | 32.95%     | ok               |
|          40 | -18.90%  | -8.62%             | -20.35% |    -1.72 |       60 | 21.80%     | ok               |
|          45 | -17.72%  | -8.62%             | -19.60% |    -1.78 |       42 | 17.80%     | ok               |
|          35 | -22.82%  | -8.62%             | -24.20% |    -1.89 |       68 | 26.96%     | ok               |

## TMO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 40.33%   | -13.79%            | -10.55% |     0.93 |       38 | 30.62%     | ok               |
|          45 | 39.08%   | -13.79%            | -12.29% |     0.88 |       46 | 35.77%     | ok               |
|          40 | 37.03%   | -13.79%            | -12.07% |     0.83 |       49 | 40.27%     | ok               |
|          35 | 22.01%   | -13.79%            | -16.12% |     0.54 |       59 | 44.43%     | ok               |
|          30 | 15.46%   | -13.79%            | -16.83% |     0.41 |       57 | 48.75%     | ok               |

## TMUS Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 14.00%   | 12.51%             | -26.87% |     0.38 |       69 | 60.23%     | ok               |
|          30 | 12.62%   | 12.51%             | -24.50% |     0.36 |       70 | 48.59%     | ok               |
|          20 | 7.00%    | 12.51%             | -24.82% |     0.24 |       71 | 54.58%     | ok               |
|          25 | 5.93%    | 12.51%             | -25.91% |     0.22 |       75 | 50.92%     | ok               |
|          50 | 2.44%    | 12.51%             | -22.71% |     0.14 |       60 | 36.27%     | ok               |

## TRX-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 2.59%    | 24.90%             | -22.90% |     0.16 |       70 | 48.47%     | ok               |
|          40 | 1.39%    | 24.90%             | -19.12% |     0.12 |       52 | 37.74%     | ok               |
|          35 | 1.19%    | 24.90%             | -21.77% |     0.12 |       66 | 45.79%     | ok               |
|          25 | 0.75%    | 24.90%             | -26.84% |     0.11 |       66 | 51.72%     | ok               |
|          50 | -0.25%   | 24.90%             | -18.49% |     0.07 |       44 | 32.38%     | ok               |

## TSLA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 86.35%   | 88.11%             | -32.60% |     0.93 |       64 | 31.45%     | ok               |
|          40 | 76.97%   | 88.11%             | -45.90% |     0.82 |       61 | 35.94%     | ok               |
|          45 | 49.92%   | 88.11%             | -46.86% |     0.64 |       65 | 33.28%     | ok               |
|          35 | 29.03%   | 88.11%             | -54.51% |     0.47 |       74 | 38.94%     | ok               |
|          30 | 4.77%    | 88.11%             | -57.89% |     0.26 |       68 | 43.43%     | ok               |

## TXN Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 13.18%   | 71.09%             | -45.45% |     0.33 |       70 | 35.11%     | ok               |
|          20 | 4.58%    | 71.09%             | -38.98% |     0.22 |       61 | 60.23%     | ok               |
|          15 | 1.58%    | 71.09%             | -39.48% |     0.18 |       64 | 64.23%     | ok               |
|          35 | -0.02%   | 71.09%             | -43.38% |     0.13 |       74 | 50.75%     | ok               |
|          40 | -0.14%   | 71.09%             | -45.67% |     0.13 |       74 | 48.09%     | ok               |

## UNH Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 27.08%   | -19.46%            | -36.82% |     0.51 |       50 | 28.29%     | ok               |
|          30 | 23.25%   | -19.46%            | -27.25% |     0.45 |       74 | 51.58%     | ok               |
|          15 | 21.92%   | -19.46%            | -32.14% |     0.42 |       75 | 66.72%     | ok               |
|          35 | 19.90%   | -19.46%            | -28.60% |     0.41 |       66 | 46.42%     | ok               |
|          40 | 12.30%   | -19.46%            | -36.08% |     0.32 |       62 | 40.93%     | ok               |

## UNI-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 10.78%   | -81.55%            | -53.40% |     0.34 |       50 | 24.52%     | ok               |
|          40 | 0.00%    | -81.55%            | -60.60% |     0.23 |       52 | 29.50%     | ok               |
|          50 | -2.93%   | -81.55%            | -50.59% |     0.18 |       48 | 20.31%     | ok               |
|          35 | -14.41%  | -81.55%            | -65.85% |     0.1  |       70 | 34.29%     | ok               |
|          20 | -67.14%  | -81.55%            | -80.81% |    -0.61 |      101 | 51.15%     | ok               |

## UPS Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -33.82%  | -30.75%            | -42.25% |    -0.63 |       74 | 43.93%     | ok               |
|          35 | -32.71%  | -30.75%            | -40.47% |    -0.64 |       59 | 33.61%     | ok               |
|          20 | -34.92%  | -30.75%            | -45.77% |    -0.65 |       80 | 47.09%     | ok               |
|          30 | -35.18%  | -30.75%            | -40.62% |    -0.69 |       66 | 39.27%     | ok               |
|          40 | -34.06%  | -30.75%            | -42.12% |    -0.7  |       51 | 28.45%     | ok               |

## USO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 10.72%   | 87.20%             | -33.68% |     0.3  |       48 | 27.12%     | ok               |
|          30 | 2.80%    | 87.20%             | -43.35% |     0.17 |       68 | 34.44%     | ok               |
|          40 | -0.60%   | 87.20%             | -41.14% |     0.11 |       59 | 29.78%     | ok               |
|          25 | -1.49%   | 87.20%             | -45.72% |     0.11 |       70 | 37.10%     | ok               |
|          20 | -1.60%   | 87.20%             | -45.77% |     0.11 |       74 | 39.27%     | ok               |

## VEA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 5.44%    | 52.44%             | -16.28% |     0.25 |       60 | 50.58%     | ok               |
|          20 | 1.19%    | 52.44%             | -17.70% |     0.1  |       61 | 47.92%     | ok               |
|          25 | -0.82%   | 52.44%             | -17.79% |     0.02 |       57 | 46.26%     | ok               |
|          30 | -0.98%   | 52.44%             | -17.93% |     0.01 |       58 | 44.09%     | ok               |
|          35 | -2.09%   | 52.44%             | -16.79% |    -0.03 |       56 | 43.09%     | ok               |

## VIXY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -46.17%  | -59.15%            | -68.69% |    -0.39 |       44 | 10.32%     | ok               |
|          45 | -56.13%  | -59.15%            | -74.13% |    -0.55 |       56 | 16.31%     | ok               |
|          40 | -64.59%  | -59.15%            | -80.10% |    -0.66 |       70 | 20.47%     | ok               |
|          35 | -68.29%  | -59.15%            | -83.87% |    -0.7  |       86 | 25.62%     | ok               |
|          15 | -79.46%  | -59.15%            | -89.47% |    -0.86 |       99 | 43.26%     | ok               |

## VNQ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -8.60%   | 14.30%             | -19.07% |    -0.37 |       60 | 28.62%     | ok               |
|          50 | -9.03%   | 14.30%             | -17.13% |    -0.41 |       56 | 26.12%     | ok               |
|          25 | -13.12%  | 14.30%             | -22.34% |    -0.51 |       69 | 40.77%     | ok               |
|          40 | -14.13%  | 14.30%             | -24.84% |    -0.62 |       74 | 32.11%     | ok               |
|          20 | -16.65%  | 14.30%             | -23.79% |    -0.65 |       76 | 43.93%     | ok               |

## VTI Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 17.38%   | 52.08%             | -13.96% |     0.59 |       60 | 55.57%     | ok               |
|          15 | 11.37%   | 52.08%             | -15.70% |     0.41 |       63 | 58.07%     | ok               |
|          25 | 6.34%    | 52.08%             | -16.10% |     0.27 |       58 | 53.91%     | ok               |
|          30 | -0.72%   | 52.08%             | -18.77% |     0.04 |       66 | 52.08%     | ok               |
|          40 | -2.95%   | 52.08%             | -20.44% |    -0.05 |       68 | 45.42%     | ok               |

## VWO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -6.69%   | 49.13%             | -21.68% |    -0.22 |       58 | 32.61%     | ok               |
|          15 | -9.03%   | 49.13%             | -24.01% |    -0.26 |       69 | 49.42%     | ok               |
|          45 | -8.51%   | 49.13%             | -23.75% |    -0.3  |       60 | 35.11%     | ok               |
|          20 | -10.06%  | 49.13%             | -26.14% |    -0.31 |       67 | 47.25%     | ok               |
|          40 | -8.98%   | 49.13%             | -23.57% |    -0.31 |       70 | 37.94%     | ok               |

## VZ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 1.08%    | 19.35%             | -16.98% |     0.1  |       50 | 26.29%     | ok               |
|          45 | -5.90%   | 19.35%             | -20.38% |    -0.13 |       56 | 29.12%     | ok               |
|          35 | -11.47%  | 19.35%             | -24.68% |    -0.31 |       59 | 34.61%     | ok               |
|          25 | -14.77%  | 19.35%             | -28.84% |    -0.38 |       76 | 42.43%     | ok               |
|          40 | -14.53%  | 19.35%             | -26.72% |    -0.43 |       62 | 31.61%     | ok               |

## WFC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -2.68%   | 71.24%             | -18.29% |    -0.02 |       58 | 32.28%     | ok               |
|          35 | -6.41%   | 71.24%             | -23.64% |    -0.06 |       81 | 44.09%     | ok               |
|          45 | -9.13%   | 71.24%             | -23.40% |    -0.2  |       64 | 36.61%     | ok               |
|          20 | -16.07%  | 71.24%             | -29.43% |    -0.22 |       81 | 53.41%     | ok               |
|          40 | -11.76%  | 71.24%             | -24.26% |    -0.28 |       76 | 40.10%     | ok               |

## WIF-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 81.20%   | -91.53%            | -46.21% |     0.75 |       73 | 42.34%     | ok               |
|          20 | 78.79%   | -91.53%            | -40.67% |     0.74 |       67 | 39.85%     | ok               |
|          25 | -5.15%   | -91.53%            | -52.41% |     0.26 |       73 | 37.16%     | ok               |
|          50 | -17.86%  | -91.53%            | -37.87% |    -0.11 |       38 | 11.88%     | ok               |
|          30 | -40.82%  | -91.53%            | -56.94% |    -0.17 |       72 | 32.57%     | ok               |

## WMT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 63.70%   | 122.63%            | -9.18%  |     1.61 |       36 | 44.93%     | ok               |
|          50 | 56.31%   | 122.63%            | -12.19% |     1.54 |       32 | 42.60%     | ok               |
|          40 | 53.47%   | 122.63%            | -9.18%  |     1.38 |       40 | 46.09%     | ok               |
|          35 | 54.74%   | 122.63%            | -9.11%  |     1.37 |       48 | 49.75%     | ok               |
|          30 | 32.33%   | 122.63%            | -21.31% |     0.85 |       55 | 52.25%     | ok               |

## XBI Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 3.96%    | 52.49%             | -16.71% |     0.18 |       60 | 34.61%     | ok               |
|          45 | 3.16%    | 52.49%             | -16.88% |     0.16 |       52 | 31.45%     | ok               |
|          35 | -3.05%   | 52.49%             | -21.38% |     0.01 |       62 | 37.77%     | ok               |
|          30 | -4.13%   | 52.49%             | -21.75% |    -0.02 |       62 | 39.43%     | ok               |
|          50 | -5.14%   | 52.49%             | -16.83% |    -0.07 |       54 | 28.29%     | ok               |

## XLB Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -4.67%   | 24.58%             | -20.60% |    -0.12 |       60 | 32.11%     | ok               |
|          50 | -4.61%   | 24.58%             | -17.40% |    -0.14 |       44 | 27.79%     | ok               |
|          35 | -7.91%   | 24.58%             | -23.62% |    -0.24 |       60 | 35.61%     | ok               |
|          45 | -7.43%   | 24.58%             | -20.61% |    -0.25 |       44 | 29.28%     | ok               |
|          25 | -12.47%  | 24.58%             | -23.87% |    -0.4  |       68 | 41.26%     | ok               |

## XLC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 16.85%   | 49.83%             | -12.33% |     0.58 |       63 | 55.91%     | ok               |
|          25 | 14.65%   | 49.83%             | -12.31% |     0.51 |       60 | 57.74%     | ok               |
|          40 | 11.55%   | 49.83%             | -13.38% |     0.45 |       66 | 48.42%     | ok               |
|          35 | 11.52%   | 49.83%             | -13.38% |     0.44 |       62 | 52.91%     | ok               |
|          20 | 6.59%    | 49.83%             | -13.78% |     0.26 |       68 | 60.40%     | ok               |

## XLE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -0.02%   | 42.50%             | -25.98% |     0.07 |       54 | 36.94%     | ok               |
|          35 | -3.79%   | 42.50%             | -32.17% |    -0.02 |       65 | 44.59%     | ok               |
|          45 | -5.17%   | 42.50%             | -30.88% |    -0.07 |       62 | 39.60%     | ok               |
|          25 | -11.92%  | 42.50%             | -37.50% |    -0.22 |       83 | 50.25%     | ok               |
|          30 | -11.95%  | 42.50%             | -37.51% |    -0.23 |       75 | 47.09%     | ok               |

## XLF Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -3.40%   | 38.73%             | -18.01% |    -0.05 |       66 | 54.91%     | ok               |
|          15 | -7.39%   | 38.73%             | -19.58% |    -0.19 |       74 | 57.74%     | ok               |
|          25 | -10.13%  | 38.73%             | -23.22% |    -0.31 |       75 | 51.41%     | ok               |
|          30 | -10.78%  | 38.73%             | -23.61% |    -0.35 |       74 | 48.92%     | ok               |
|          35 | -17.94%  | 38.73%             | -27.41% |    -0.71 |       64 | 44.76%     | ok               |

## XLI Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 12.76%   | 55.76%             | -10.36% |     0.48 |       72 | 54.24%     | ok               |
|          20 | 8.19%    | 55.76%             | -12.74% |     0.35 |       63 | 49.75%     | ok               |
|          30 | 5.82%    | 55.76%             | -11.38% |     0.28 |       64 | 47.25%     | ok               |
|          45 | 5.38%    | 55.76%             | -12.27% |     0.28 |       62 | 38.77%     | ok               |
|          50 | 4.34%    | 55.76%             | -9.25%  |     0.24 |       56 | 36.44%     | ok               |

## XLK Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 83.11%   | 83.05%             | -14.75% |     1.34 |       41 | 54.08%     | ok               |
|          20 | 68.83%   | 83.05%             | -14.75% |     1.2  |       46 | 51.91%     | ok               |
|          25 | 65.39%   | 83.05%             | -14.75% |     1.2  |       40 | 49.75%     | ok               |
|          30 | 63.23%   | 83.05%             | -14.75% |     1.19 |       40 | 48.59%     | ok               |
|          35 | 45.02%   | 83.05%             | -13.61% |     0.95 |       52 | 45.92%     | ok               |

## XLM-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 41.10%   | -54.51%            | -37.64% |     0.6  |       50 | 32.38%     | ok               |
|          50 | 37.16%   | -54.51%            | -32.06% |     0.57 |       46 | 28.54%     | ok               |
|          30 | 13.95%   | -54.51%            | -45.54% |     0.37 |       69 | 46.36%     | ok               |
|          15 | 7.79%    | -54.51%            | -39.98% |     0.32 |       85 | 58.43%     | ok               |
|          20 | 8.15%    | -54.51%            | -43.12% |     0.32 |       75 | 51.72%     | ok               |

## XLP Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 12.84%   | 18.35%             | -5.66%  |     0.78 |       56 | 33.94%     | ok               |
|          50 | 9.52%    | 18.35%             | -6.08%  |     0.6  |       58 | 31.61%     | ok               |
|          40 | 9.97%    | 18.35%             | -7.77%  |     0.59 |       74 | 38.27%     | ok               |
|          35 | 9.01%    | 18.35%             | -9.73%  |     0.53 |       70 | 41.26%     | ok               |
|          30 | 6.74%    | 18.35%             | -10.28% |     0.4  |       74 | 43.09%     | ok               |

## XLU Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 5.66%    | 44.47%             | -9.11%  |     0.31 |       50 | 30.95%     | ok               |
|          45 | 3.49%    | 44.47%             | -10.56% |     0.21 |       54 | 31.95%     | ok               |
|          40 | 0.22%    | 44.47%             | -11.91% |     0.05 |       60 | 33.61%     | ok               |
|          35 | -6.42%   | 44.47%             | -16.22% |    -0.26 |       66 | 36.27%     | ok               |
|          30 | -8.16%   | 44.47%             | -17.22% |    -0.33 |       71 | 39.43%     | ok               |

## XLV Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -9.77%   | 10.49%             | -15.55% |    -0.46 |       68 | 36.94%     | ok               |
|          25 | -11.10%  | 10.49%             | -16.79% |    -0.53 |       70 | 38.27%     | ok               |
|          15 | -14.60%  | 10.49%             | -20.26% |    -0.69 |       79 | 43.26%     | ok               |
|          20 | -14.52%  | 10.49%             | -20.35% |    -0.7  |       73 | 40.10%     | ok               |
|          35 | -14.49%  | 10.49%             | -19.74% |    -0.77 |       66 | 34.44%     | ok               |

## XLY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 3.11%    | 33.00%             | -12.94% |     0.16 |       72 | 41.76%     | ok               |
|          30 | 0.75%    | 33.00%             | -14.01% |     0.09 |       74 | 44.93%     | ok               |
|          50 | -0.27%   | 33.00%             | -11.49% |     0.04 |       52 | 29.62%     | ok               |
|          15 | -1.25%   | 33.00%             | -15.77% |     0.04 |       78 | 51.75%     | ok               |
|          45 | -3.28%   | 33.00%             | -13.48% |    -0.07 |       56 | 32.28%     | ok               |

## XOM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | 2.44%    | 51.21%             | -19.90% |     0.14 |       58 | 37.27%     | ok               |
|          50 | 2.44%    | 51.21%             | -21.35% |     0.14 |       44 | 29.62%     | ok               |
|          30 | 1.42%    | 51.21%             | -20.29% |     0.11 |       58 | 36.61%     | ok               |
|          20 | -1.35%   | 51.21%             | -25.56% |     0.04 |       63 | 39.77%     | ok               |
|          40 | -2.68%   | 51.21%             | -21.45% |    -0.01 |       54 | 33.94%     | ok               |

## XRP-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | -29.83%  | -49.85%            | -52.26% |    -0.21 |       72 | 41.76%     | ok               |
|          40 | -35.95%  | -49.85%            | -50.65% |    -0.35 |       62 | 35.63%     | ok               |
|          30 | -43.00%  | -49.85%            | -60.55% |    -0.43 |       76 | 46.17%     | ok               |
|          45 | -44.07%  | -49.85%            | -52.43% |    -0.53 |       62 | 31.42%     | ok               |
|          50 | -43.49%  | -49.85%            | -43.49% |    -0.64 |       66 | 23.95%     | ok               |

## YFI-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -31.64%  | -77.02%            | -52.37% |    -0.43 |       62 | 26.82%     | ok               |
|          45 | -37.27%  | -77.02%            | -54.04% |    -0.64 |       62 | 22.22%     | ok               |
|          30 | -50.68%  | -77.02%            | -67.78% |    -0.71 |       83 | 40.04%     | ok               |
|          35 | -51.07%  | -77.02%            | -65.91% |    -0.78 |       73 | 34.10%     | ok               |
|          25 | -55.70%  | -77.02%            | -69.14% |    -0.81 |       77 | 45.02%     | ok               |

## ZEC-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 124.17%  | 711.85%            | -24.66% |     0.9  |       50 | 23.18%     | ok               |
|          35 | 86.85%   | 711.85%            | -43.54% |     0.74 |       58 | 30.84%     | ok               |
|          25 | 73.54%   | 711.85%            | -46.61% |     0.69 |       61 | 39.66%     | ok               |
|          50 | 54.10%   | 711.85%            | -37.94% |     0.6  |       52 | 20.69%     | ok               |
|          30 | 43.83%   | 711.85%            | -46.93% |     0.56 |       69 | 36.40%     | ok               |
