# Market Tracker Backtest Report

_Generated: 2026-11-23T07:29:15+00:00_

## Data Sources

- Crypto: Kraken -> Coinbase -> CoinGecko OHLC -> CoinPaprika fallback chain.
- Stocks / ETFs / indices: Stooq -> Yahoo Finance fallback chain.
- Data rows are generated from real market APIs. Mock OHLCV rows are not generated.

## Data Freshness

- Rows: **92,806**
- Symbols: **161**
- Date range: **2024-07-02** to **2026-11-23**

## Latest Signals

| symbol     | date                |         close |   composite_score | signal   | data_source   |
|:-----------|:--------------------|--------------:|------------------:|:---------|:--------------|
| CL         | 2026-11-20 00:00:00 |    98.71      |        45.5833    | LONG     | Yahoo Finance |
| CMCSA      | 2026-11-20 00:00:00 |    24.9       |        31.4167    | LONG     | Yahoo Finance |
| COST       | 2026-11-20 00:00:00 |  1102.15      |        66.0833    | LONG     | Yahoo Finance |
| DIS        | 2026-11-20 00:00:00 |   117.98      |        56.0833    | LONG     | Yahoo Finance |
| DXY-INDEX  | 2026-11-23 00:00:00 |   103.64      |        81.7204    | LONG     | Yahoo Finance |
| HD         | 2026-11-20 00:00:00 |   339.04      |        42.1667    | LONG     | Yahoo Finance |
| KO         | 2026-11-20 00:00:00 |    96.99      |        61.0833    | LONG     | Yahoo Finance |
| PG         | 2026-11-20 00:00:00 |   169.37      |        60.75      | LONG     | Yahoo Finance |
| TGT        | 2026-11-20 00:00:00 |   165.83      |        71.5833    | LONG     | Yahoo Finance |
| TMUS       | 2026-11-20 00:00:00 |   165.6       |        36.9167    | LONG     | Yahoo Finance |
| VIXY       | 2026-11-20 00:00:00 |    25.95      |        61.0833    | LONG     | Yahoo Finance |
| WMT        | 2026-11-20 00:00:00 |   127.95      |        40.0833    | LONG     | Yahoo Finance |
| XLP        | 2026-11-20 00:00:00 |    90.46      |        31.9167    | LONG     | Yahoo Finance |
| AAPL       | 2026-11-20 00:00:00 |   342.56      |        27.3333    | NEUTRAL  | Yahoo Finance |
| ABBV       | 2026-11-20 00:00:00 |   286.2       |        14.5833    | NEUTRAL  | Yahoo Finance |
| ADBE       | 2026-11-20 00:00:00 |   217.71      |       -50.3333    | NEUTRAL  | Yahoo Finance |
| AGG        | 2026-11-20 00:00:00 |    96.15      |         1.91667   | NEUTRAL  | Yahoo Finance |
| AMD        | 2026-11-20 00:00:00 |   424.39      |       -48         | NEUTRAL  | Yahoo Finance |
| AMGN       | 2026-11-20 00:00:00 |   435.64      |        -3.33333   | NEUTRAL  | Yahoo Finance |
| AMZN       | 2026-11-20 00:00:00 |   246.82      |       -10.0833    | NEUTRAL  | Yahoo Finance |
| AVGO       | 2026-11-20 00:00:00 |   304.41      |       -36.1667    | NEUTRAL  | Yahoo Finance |
| BAC        | 2026-11-20 00:00:00 |    47.04      |       -60         | NEUTRAL  | Yahoo Finance |
| BLK        | 2026-11-20 00:00:00 |  1101.72      |        -0.0833333 | NEUTRAL  | Yahoo Finance |
| BND        | 2026-11-20 00:00:00 |    71.33      |         4.41667   | NEUTRAL  | Yahoo Finance |
| C          | 2026-11-20 00:00:00 |   110.62      |       -74.5833    | NEUTRAL  | Yahoo Finance |
| DIA        | 2026-11-20 00:00:00 |   481.08      |       -65         | NEUTRAL  | Yahoo Finance |
| EFA        | 2026-11-20 00:00:00 |    96.14      |       -69.25      | NEUTRAL  | Yahoo Finance |
| EOG        | 2026-11-20 00:00:00 |   148.6       |       -20.8333    | NEUTRAL  | Yahoo Finance |
| GDX        | 2026-11-20 00:00:00 |    68.4       |       -71.9167    | NEUTRAL  | Yahoo Finance |
| GDXJ       | 2026-11-20 00:00:00 |    81.26      |       -70.1667    | NEUTRAL  | Yahoo Finance |
| GLD        | 2026-11-20 00:00:00 |   322.87      |       -74.5833    | NEUTRAL  | Yahoo Finance |
| GRT-USD    | 2026-11-23 00:00:00 |     0.01628   |       -19         | NEUTRAL  | Kraken API    |
| GS         | 2026-11-20 00:00:00 |   790.69      |       -66.75      | NEUTRAL  | Yahoo Finance |
| HON        | 2026-11-20 00:00:00 |   212.64      |       -58.3333    | NEUTRAL  | Yahoo Finance |
| HYG        | 2026-11-20 00:00:00 |    76.33      |       -61         | NEUTRAL  | Yahoo Finance |
| ICP-USD    | 2026-11-23 00:00:00 |     2.013     |       -63.25      | NEUTRAL  | Kraken API    |
| IEF        | 2026-11-20 00:00:00 |    91.65      |        15.25      | NEUTRAL  | Yahoo Finance |
| INJ-USD    | 2026-11-23 00:00:00 |     6.242     |       -59.5       | NEUTRAL  | Kraken API    |
| ITA        | 2026-11-20 00:00:00 |    66.17      |       -65         | NEUTRAL  | Yahoo Finance |
| IWM        | 2026-11-20 00:00:00 |   256.61      |       -66.75      | NEUTRAL  | Yahoo Finance |
| JNJ        | 2026-11-20 00:00:00 |   270.47      |         8.33333   | NEUTRAL  | Yahoo Finance |
| JPM        | 2026-11-20 00:00:00 |   310.53      |       -48.75      | NEUTRAL  | Yahoo Finance |
| LIN        | 2026-11-20 00:00:00 |   502.83      |       -16.0833    | NEUTRAL  | Yahoo Finance |
| LLY        | 2026-11-20 00:00:00 |  1347.11      |        16.4167    | NEUTRAL  | Yahoo Finance |
| MCD        | 2026-11-20 00:00:00 |   273.24      |        12.8333    | NEUTRAL  | Yahoo Finance |
| MPC        | 2026-11-20 00:00:00 |   367.19      |       -19.1667    | NEUTRAL  | Yahoo Finance |
| MRK        | 2026-11-20 00:00:00 |   133.72      |       -29.8333    | NEUTRAL  | Yahoo Finance |
| MS         | 2026-11-20 00:00:00 |   165.67      |       -66.75      | NEUTRAL  | Yahoo Finance |
| MSFT       | 2026-11-20 00:00:00 |   484.52      |       -27.4167    | NEUTRAL  | Yahoo Finance |
| NEM        | 2026-11-20 00:00:00 |    94.68      |       -75.25      | NEUTRAL  | Yahoo Finance |
| NFLX       | 2026-11-20 00:00:00 |    56.73      |       -61.75      | NEUTRAL  | Yahoo Finance |
| ORCL       | 2026-11-20 00:00:00 |   101.19      |       -55         | NEUTRAL  | Yahoo Finance |
| PEP        | 2026-11-20 00:00:00 |   140.54      |        13.3333    | NEUTRAL  | Yahoo Finance |
| PFE        | 2026-11-20 00:00:00 |    27.4       |       -28.0833    | NEUTRAL  | Yahoo Finance |
| PM         | 2026-11-20 00:00:00 |   184.09      |       -56.8333    | NEUTRAL  | Yahoo Finance |
| QCOM       | 2026-11-20 00:00:00 |   149.94      |       -54.75      | NEUTRAL  | Yahoo Finance |
| RTX        | 2026-11-20 00:00:00 |   190.17      |       -58.3333    | NEUTRAL  | Yahoo Finance |
| SBUX       | 2026-11-20 00:00:00 |   103.13      |         5.91667   | NEUTRAL  | Yahoo Finance |
| SCHW       | 2026-11-20 00:00:00 |    90.16      |       -14.5       | NEUTRAL  | Yahoo Finance |
| SHY        | 2026-11-20 00:00:00 |    81.61      |        19.5833    | NEUTRAL  | Yahoo Finance |
| SNX-USD    | 2026-11-23 00:00:00 |     0.1447    |       -13.1667    | NEUTRAL  | Kraken API    |
| SPY        | 2026-11-20 00:00:00 |   689.81      |       -57.3333    | NEUTRAL  | Yahoo Finance |
| SUSHI-USD  | 2026-11-23 00:00:00 |     0.1538    |       -23.5       | NEUTRAL  | Kraken API    |
| T          | 2026-11-20 00:00:00 |    22.31      |         3.25      | NEUTRAL  | Yahoo Finance |
| TLT        | 2026-11-20 00:00:00 |    81.45      |        -3.58333   | NEUTRAL  | Yahoo Finance |
| TMO        | 2026-11-20 00:00:00 |   669.54      |       -22.3333    | NEUTRAL  | Yahoo Finance |
| TSLA       | 2026-11-20 00:00:00 |   345.82      |       -63.25      | NEUTRAL  | Yahoo Finance |
| TXN        | 2026-11-20 00:00:00 |   263.75      |       -65         | NEUTRAL  | Yahoo Finance |
| UNH        | 2026-11-20 00:00:00 |   339.85      |       -45.8333    | NEUTRAL  | Yahoo Finance |
| UPS        | 2026-11-20 00:00:00 |   106.22      |         1.66667   | NEUTRAL  | Yahoo Finance |
| VEA        | 2026-11-20 00:00:00 |    63.62      |       -72.5833    | NEUTRAL  | Yahoo Finance |
| VTI        | 2026-11-20 00:00:00 |   340.02      |       -57.3333    | NEUTRAL  | Yahoo Finance |
| VZ         | 2026-11-20 00:00:00 |    46.48      |        56.4167    | NEUTRAL  | Yahoo Finance |
| XBI        | 2026-11-20 00:00:00 |   140.18      |       -65.75      | NEUTRAL  | Yahoo Finance |
| XLF        | 2026-11-20 00:00:00 |    54.57      |       -27.0833    | NEUTRAL  | Yahoo Finance |
| XLI        | 2026-11-20 00:00:00 |   156.37      |       -65         | NEUTRAL  | Yahoo Finance |
| XLV        | 2026-11-20 00:00:00 |   177.24      |        -1.58333   | NEUTRAL  | Yahoo Finance |
| XRP-USD    | 2026-11-23 00:00:00 |     0.94104   |       -27.5       | NEUTRAL  | Kraken API    |
| ZEC-USD    | 2026-11-23 00:00:00 |   790.94      |       -53.6667    | NEUTRAL  | Kraken API    |
| AAVE-USD   | 2026-11-23 00:00:00 |    98.2       |       -55.3333    | SHORT    | Kraken API    |
| ADA-USD    | 2026-11-23 00:00:00 |     0.14625   |       -49.6667    | SHORT    | Kraken API    |
| ALGO-USD   | 2026-11-23 00:00:00 |     0.07773   |       -49.1667    | SHORT    | Kraken API    |
| AMAT       | 2026-11-20 00:00:00 |   302.63      |       -58.5       | SHORT    | Yahoo Finance |
| APT-USD    | 2026-11-23 00:00:00 |     0.3863    |       -55.3333    | SHORT    | Kraken API    |
| ARB-USD    | 2026-11-23 00:00:00 |     0.1162    |       -55.3333    | SHORT    | Kraken API    |
| ARKK       | 2026-11-20 00:00:00 |    64.22      |       -53.8333    | SHORT    | Yahoo Finance |
| ATOM-USD   | 2026-11-23 00:00:00 |     1.1834    |       -39         | SHORT    | Kraken API    |
| AVAX-USD   | 2026-11-23 00:00:00 |     6.733     |       -51.3333    | SHORT    | Kraken API    |
| BA         | 2026-11-20 00:00:00 |   155.89      |       -57.0833    | SHORT    | Yahoo Finance |
| BCH-USD    | 2026-11-23 00:00:00 |   199.67      |       -48         | SHORT    | Kraken API    |
| BITO       | 2026-11-20 00:00:00 |    15.5       |       -50.0833    | SHORT    | Yahoo Finance |
| BONK-USD   | 2026-11-23 00:00:00 |     2.13e-06  |       -54.8333    | SHORT    | Kraken API    |
| BTC-USD    | 2026-11-23 00:00:00 | 61439.8       |       -49.6667    | SHORT    | Kraken API    |
| CAT        | 2026-11-20 00:00:00 |   510.45      |       -56.0833    | SHORT    | Yahoo Finance |
| COMP-USD   | 2026-11-23 00:00:00 |    17.3       |       -49.3333    | SHORT    | Kraken API    |
| COP        | 2026-11-20 00:00:00 |   136.12      |       -31.5833    | SHORT    | Yahoo Finance |
| CRM        | 2026-11-20 00:00:00 |   180.62      |       -51.5833    | SHORT    | Yahoo Finance |
| CRV-USD    | 2026-11-23 00:00:00 |     0.18389   |       -55.3333    | SHORT    | Kraken API    |
| CSCO       | 2026-11-20 00:00:00 |    90.64      |       -53.25      | SHORT    | Yahoo Finance |
| CVX        | 2026-11-20 00:00:00 |   208.37      |       -30.6667    | SHORT    | Yahoo Finance |
| DASH-USD   | 2026-11-23 00:00:00 |    35.839     |       -53.6667    | SHORT    | Kraken API    |
| DBC        | 2026-11-20 00:00:00 |    29.32      |       -59.5833    | SHORT    | Yahoo Finance |
| DE         | 2026-11-20 00:00:00 |   609.25      |       -59.5833    | SHORT    | Yahoo Finance |
| DOGE-USD   | 2026-11-23 00:00:00 |     0.0556433 |       -49.6667    | SHORT    | Kraken API    |
| DOT-USD    | 2026-11-23 00:00:00 |     0.6733    |       -49.1667    | SHORT    | Kraken API    |
| EEM        | 2026-11-20 00:00:00 |    53.84      |       -60         | SHORT    | Yahoo Finance |
| ETC-USD    | 2026-11-23 00:00:00 |     5.803     |       -45.8333    | SHORT    | Kraken API    |
| ETH-USD    | 2026-11-23 00:00:00 |  1724.79      |       -47.8333    | SHORT    | Kraken API    |
| EWJ        | 2026-11-20 00:00:00 |    83.43      |       -58.3333    | SHORT    | Yahoo Finance |
| FCX        | 2026-11-20 00:00:00 |    45.99      |       -64         | SHORT    | Yahoo Finance |
| FET-USD    | 2026-11-23 00:00:00 |     0.1101    |       -55.3333    | SHORT    | Kraken API    |
| FIL-USD    | 2026-11-23 00:00:00 |     0.541     |       -55.3333    | SHORT    | Kraken API    |
| FXI        | 2026-11-20 00:00:00 |    31.23      |       -58         | SHORT    | Yahoo Finance |
| GE         | 2026-11-20 00:00:00 |   309.62      |       -38.0833    | SHORT    | Yahoo Finance |
| GOOGL      | 2026-11-20 00:00:00 |   265.29      |       -40.75      | SHORT    | Yahoo Finance |
| HBAR-USD   | 2026-11-23 00:00:00 |     0.05238   |       -51.3333    | SHORT    | Kraken API    |
| IBIT       | 2026-11-20 00:00:00 |    33.02      |       -51.8333    | SHORT    | Yahoo Finance |
| IBM        | 2026-11-20 00:00:00 |   224.44      |       -40.3333    | SHORT    | Yahoo Finance |
| IEMG       | 2026-11-20 00:00:00 |    65.69      |       -60         | SHORT    | Yahoo Finance |
| INTC       | 2026-11-20 00:00:00 |    51.28      |       -41.75      | SHORT    | Yahoo Finance |
| INTU       | 2026-11-20 00:00:00 |   270.44      |       -42.8333    | SHORT    | Yahoo Finance |
| LDO-USD    | 2026-11-23 00:00:00 |     0.241     |       -51.3333    | SHORT    | Kraken API    |
| LINK-USD   | 2026-11-23 00:00:00 |     8.90395   |       -49.6667    | SHORT    | Kraken API    |
| LRCX       | 2026-11-20 00:00:00 |   183.27      |       -58.5       | SHORT    | Yahoo Finance |
| LTC-USD    | 2026-11-23 00:00:00 |    40.6       |       -51.3333    | SHORT    | Kraken API    |
| META       | 2026-11-20 00:00:00 |   560.84      |       -30.75      | SHORT    | Yahoo Finance |
| MU         | 2026-11-20 00:00:00 |   594.51      |       -68         | SHORT    | Yahoo Finance |
| NEAR-USD   | 2026-11-23 00:00:00 |     3.0163    |       -41.3333    | SHORT    | Kraken API    |
| NKE        | 2026-11-20 00:00:00 |    32.92      |       -41.0833    | SHORT    | Yahoo Finance |
| NOW        | 2026-11-20 00:00:00 |    87.61      |       -49.9167    | SHORT    | Yahoo Finance |
| NVDA       | 2026-11-20 00:00:00 |   125.53      |       -71.3333    | SHORT    | Yahoo Finance |
| OP-USD     | 2026-11-23 00:00:00 |     0.0714    |       -55.3333    | SHORT    | Kraken API    |
| OXY        | 2026-11-20 00:00:00 |    53.9       |       -61.0833    | SHORT    | Yahoo Finance |
| PEPE-USD   | 2026-11-23 00:00:00 |     3.427e-06 |       -55.3333    | SHORT    | Kraken API    |
| POL-USD    | 2026-11-23 00:00:00 |     0.07831   |       -45.8333    | SHORT    | Kraken API    |
| QQQ        | 2026-11-20 00:00:00 |   608.45      |       -56.6667    | SHORT    | Yahoo Finance |
| RENDER-USD | 2026-11-23 00:00:00 |     1.341     |       -52         | SHORT    | Kraken API    |
| SHIB-USD   | 2026-11-23 00:00:00 |     3.623e-06 |       -51.3333    | SHORT    | Kraken API    |
| SKY-USD    | 2026-11-23 00:00:00 |     0.04165   |       -57.3333    | SHORT    | Kraken API    |
| SLB        | 2026-11-20 00:00:00 |    45.89      |       -57.0833    | SHORT    | Yahoo Finance |
| SLV        | 2026-11-20 00:00:00 |    36.97      |       -65.3333    | SHORT    | Yahoo Finance |
| SMH        | 2026-11-20 00:00:00 |   400.06      |       -67.3333    | SHORT    | Yahoo Finance |
| SOL-USD    | 2026-11-23 00:00:00 |    72.17      |       -30.8333    | SHORT    | Kraken API    |
| SOXX       | 2026-11-20 00:00:00 |   123.4       |       -64.6667    | SHORT    | Yahoo Finance |
| TIA-USD    | 2026-11-23 00:00:00 |     0.3371    |       -55.3333    | SHORT    | Kraken API    |
| TRX-USD    | 2026-11-23 00:00:00 |     0.30473   |       -59.1667    | SHORT    | Kraken API    |
| UNI-USD    | 2026-11-23 00:00:00 |     4.7725    |       -55.3333    | SHORT    | Kraken API    |
| USO        | 2026-11-20 00:00:00 |   139.63      |       -32.6667    | SHORT    | Yahoo Finance |
| VNQ        | 2026-11-20 00:00:00 |    92.56      |       -33.8333    | SHORT    | Yahoo Finance |
| VWO        | 2026-11-20 00:00:00 |    50.62      |       -55         | SHORT    | Yahoo Finance |
| WFC        | 2026-11-20 00:00:00 |    78.62      |       -39.0833    | SHORT    | Yahoo Finance |
| WIF-USD    | 2026-11-23 00:00:00 |     0.1236    |       -49.1667    | SHORT    | Kraken API    |
| XLB        | 2026-11-20 00:00:00 |    48.34      |       -57.0833    | SHORT    | Yahoo Finance |
| XLC        | 2026-11-20 00:00:00 |   100.03      |       -41.25      | SHORT    | Yahoo Finance |
| XLE        | 2026-11-20 00:00:00 |    60.51      |       -34.8333    | SHORT    | Yahoo Finance |
| XLK        | 2026-11-20 00:00:00 |   149.01      |       -48.5       | SHORT    | Yahoo Finance |
| XLM-USD    | 2026-11-23 00:00:00 |     0.128738  |       -59.8333    | SHORT    | Kraken API    |
| XLU        | 2026-11-20 00:00:00 |    42.69      |       -39.3333    | SHORT    | Yahoo Finance |
| XLY        | 2026-11-20 00:00:00 |   112.46      |       -43.3333    | SHORT    | Yahoo Finance |
| XOM        | 2026-11-20 00:00:00 |   159.99      |       -32.8333    | SHORT    | Yahoo Finance |
| YFI-USD    | 2026-11-23 00:00:00 |  1662.8       |       -51.3333    | SHORT    | Kraken API    |

## Edge Summary

- Symbols with trades: **161** of 161
- Beat buy-and-hold: **40.99%** of traded symbols
- Positive return: **34.78%** of traded symbols
- Median strategy return: **-7.03%** (benchmark **13.09%**)
- Median excess vs benchmark: **-16.65%**
- Median Sharpe: **-0.03**
- Median exposure: **44.93%**

> Edge is real only if both _beat buy-and-hold_ and _median excess_ are convincingly positive across many symbols. Treat a single high-return symbol as noise.

## Portfolio Backtest

Actual capital-allocation books (not per-symbol averages). Benchmarks: `equal_weight_buyhold` (whole tracked universe), `spy_buyhold` (100% SPY), and `sixty_forty` (60% SPY / 40% AGG). `high_conf_voltarget` inverse-vol-weights the HIGH-confidence book; `conviction_long_short` is market-neutral. Judge on **Sharpe** and **max_drawdown** out-of-sample, not raw return: a fully-invested long book wins on return in a bull market but carries all the risk.

| strategy              | scope         | ann_return   | ann_vol   |   sharpe | max_drawdown   | total_return   |   avg_gross_exposure |
|:----------------------|:--------------|:-------------|:----------|---------:|:---------------|:---------------|---------------------:|
| equal_weight_buyhold  | full          | 4.65%        | 28.50%    |     0.16 | -39.53%        | 1.82%          |                 1    |
| equal_weight_buyhold  | out_of_sample | 16.53%       | 26.40%    |     0.63 | -24.61%        | 14.89%         |                 1    |
| all_signals_ew        | full          | -10.65%      | 24.43%    |    -0.44 | -52.05%        | -33.96%        |                 1    |
| all_signals_ew        | out_of_sample | -3.88%       | 21.85%    |    -0.18 | -22.66%        | -6.44%         |                 1    |
| high_conf_ew          | full          | -11.07%      | 29.99%    |    -0.37 | -50.34%        | -37.64%        |                 0.89 |
| high_conf_ew          | out_of_sample | 2.37%        | 25.43%    |     0.09 | -27.61%        | -0.91%         |                 0.89 |
| high_conf_voltarget   | full          | -13.55%      | 26.69%    |    -0.51 | -45.39%        | -40.48%        |                 0.89 |
| high_conf_voltarget   | out_of_sample | -2.76%       | 20.44%    |    -0.13 | -23.45%        | -5.04%         |                 0.89 |
| conviction_long_short | full          | -14.82%      | 22.05%    |    -0.67 | -51.33%        | -40.85%        |                 0.96 |
| conviction_long_short | out_of_sample | -5.13%       | 17.31%    |    -0.3  | -22.59%        | -6.80%         |                 0.96 |
| spy_buyhold           | full          | 0.25%        | 14.21%    |     0.02 | -19.00%        | -2.27%         |                 0.79 |
| spy_buyhold           | out_of_sample | -10.19%      | 11.58%    |    -0.88 | -14.90%        | -10.91%        |                 0.79 |
| sixty_forty           | full          | -0.19%       | 8.88%     |    -0.02 | -11.86%        | -1.75%         |                 0.79 |
| sixty_forty           | out_of_sample | -8.25%       | 7.52%     |    -1.1  | -9.92%         | -8.68%         |                 0.79 |

## Walk-Forward Robustness

Each book measured across contiguous time folds (each a different regime). A book has durable edge only if `mean_sharpe` is positive, `min_sharpe` isn't deeply negative, and `pct_positive_folds` is high — a single great fold doesn't count. `fold_sharpes` lists each fold oldest-to-newest.

| strategy              |   n_folds |   mean_sharpe |   median_sharpe |   min_sharpe | pct_positive_folds   | mean_return   | fold_sharpes                 |
|:----------------------|----------:|--------------:|----------------:|-------------:|:---------------------|:--------------|:-----------------------------|
| equal_weight_buyhold  |         5 |          0.38 |            0.18 |        -0.86 | 60.00%               | 1.73%         | 1.33;1.52;-0.86;-0.28;0.18   |
| all_signals_ew        |         5 |         -0.51 |           -0.45 |        -1.71 | 40.00%               | -6.92%        | -1.45;-0.45;-1.71;0.63;0.46  |
| high_conf_ew          |         5 |         -0.24 |           -0.38 |        -2    | 40.00%               | -7.65%        | 0.93;-2.00;-0.38;0.75;-0.50  |
| high_conf_voltarget   |         5 |         -0.43 |           -0.36 |        -2.2  | 40.00%               | -8.96%        | 0.95;-2.20;-0.36;0.39;-0.93  |
| conviction_long_short |         5 |         -0.66 |           -0.43 |        -2.35 | 20.00%               | -9.42%        | -2.35;-0.43;-0.78;-0.26;0.51 |
| spy_buyhold           |         5 |         -0.08 |           -0.07 |        -1.53 | 40.00%               | -0.24%        | 1.22;0.21;-0.07;-0.26;-1.53  |
| sixty_forty           |         5 |         -0.14 |            0    |        -1.73 | 60.00%               | -0.25%        | 1.20;0.24;0.00;-0.40;-1.73   |

## Strategy Comparison

Each decision rule backtested over the same data. `out_of_sample` is the most recent ~35% of each symbol's history (unseen tail). A rule has real edge only if `median_excess` and `beat_benchmark_pct` stay positive out-of-sample, not just full-sample.

| strategy        | scope         |   symbols | beat_benchmark_pct   | positive_pct   | median_return   | median_benchmark   | median_excess   |   median_sharpe |   total_trades |
|:----------------|:--------------|----------:|:---------------------|:---------------|:----------------|:-------------------|:----------------|----------------:|---------------:|
| trend           | full          |       161 | 40.99%               | 34.78%         | -7.03%          | 13.09%             | -16.65%         |           -0.03 |          11336 |
| trend           | out_of_sample |       161 | 60.87%               | 55.28%         | 2.21%           | -6.13%             | 4.94%           |            0.25 |           3874 |
| mean_reversion  | full          |       159 | 40.88%               | 47.80%         | -0.16%          | 13.09%             | -10.37%         |           -0.02 |           1300 |
| mean_reversion  | out_of_sample |       132 | 67.42%               | 58.33%         | 0.38%           | -7.00%             | 5.75%           |            0.52 |            446 |
| regime_adaptive | full          |       161 | 40.99%               | 34.16%         | -7.09%          | 13.09%             | -14.83%         |           -0.01 |          11606 |
| regime_adaptive | out_of_sample |       161 | 62.11%               | 54.66%         | 2.21%           | -6.13%             | 4.20%           |            0.27 |           3981 |

## Signal Calibration

Realized forward return in the signal's direction, grouped by confidence. HIGH should outrank LOW for the confidence score to be meaningful.

| confidence_level   |   horizon |     n | mean_return   | median_return   | win_rate   |
|:-------------------|----------:|------:|:--------------|:----------------|:-----------|
| HIGH               |         5 |  7734 | 0.18%         | 0.06%           | 50.98%     |
| MEDIUM             |         5 | 29469 | 0.15%         | 0.08%           | 50.92%     |
| LOW                |         5 |  3707 | -0.15%        | -0.24%          | 47.67%     |
| ALL                |         5 | 40910 | 0.13%         | 0.05%           | 50.64%     |
| HIGH               |        10 |  7661 | 0.47%         | 0.07%           | 50.80%     |
| MEDIUM             |        10 | 29105 | 0.31%         | 0.09%           | 50.71%     |
| LOW                |        10 |  3667 | -0.28%        | -0.23%          | 48.32%     |
| ALL                |        10 | 40433 | 0.29%         | 0.06%           | 50.51%     |
| HIGH               |        20 |  7456 | 1.03%         | 0.23%           | 51.86%     |
| MEDIUM             |        20 | 28440 | 0.86%         | 0.49%           | 52.76%     |
| LOW                |        20 |  3597 | 0.00%         | -0.39%          | 48.18%     |
| ALL                |        20 | 39493 | 0.81%         | 0.37%           | 52.18%     |

## Backtest Summary

### Data Quality / Signal Availability

- **ok**: 161 symbols

| symbol     |   trades | return   | benchmark_return   | mdd     |   sharpe | exposure   | skipped_reason   |
|:-----------|---------:|:---------|:-------------------|:--------|---------:|:-----------|:-----------------|
| AAPL       |       67 | -10.47%  | 55.52%             | -20.65% |    -0.12 | 47.25%     | ok               |
| AAVE-USD   |       73 | -45.76%  | -60.31%            | -67.38% |    -0.36 | 41.00%     | ok               |
| ABBV       |       66 | -13.91%  | 72.45%             | -30.52% |    -0.24 | 49.42%     | ok               |
| ADA-USD    |       72 | -8.70%   | -74.67%            | -52.70% |     0.13 | 50.00%     | ok               |
| ADBE       |       72 | -2.02%   | -61.65%            | -31.20% |     0.11 | 54.24%     | ok               |
| AGG        |       63 | -7.03%   | -0.43%             | -10.37% |    -1.06 | 35.27%     | ok               |
| ALGO-USD   |       82 | -27.85%  | -53.51%            | -46.24% |    -0.14 | 40.80%     | ok               |
| AMAT       |       73 | -29.84%  | 25.65%             | -57.08% |    -0.17 | 51.25%     | ok               |
| AMD        |       54 | 23.48%   | 158.29%            | -38.64% |     0.42 | 36.44%     | ok               |
| AMGN       |       63 | -7.74%   | 40.18%             | -34.19% |    -0.07 | 53.41%     | ok               |
| AMZN       |       84 | -59.18%  | 23.41%             | -59.16% |    -1.76 | 41.10%     | ok               |
| APT-USD    |       76 | -10.60%  | -90.96%            | -56.73% |     0.15 | 40.61%     | ok               |
| ARB-USD    |       75 | 4.05%    | -59.36%            | -43.85% |     0.31 | 42.72%     | ok               |
| ARKK       |       89 | -19.29%  | 43.28%             | -38.67% |    -0.2  | 45.09%     | ok               |
| ATOM-USD   |       80 | -58.06%  | -69.90%            | -62.98% |    -0.88 | 45.02%     | ok               |
| AVAX-USD   |       66 | -37.57%  | -61.24%            | -48.07% |    -0.35 | 39.85%     | ok               |
| AVGO       |       68 | -10.34%  | 83.66%             | -44.82% |     0.04 | 39.27%     | ok               |
| BA         |       63 | 29.45%   | -15.93%            | -24.47% |     0.55 | 53.41%     | ok               |
| BAC        |       78 | -7.42%   | 14.93%             | -23.14% |    -0.12 | 49.08%     | ok               |
| BCH-USD    |       82 | -2.77%   | -57.83%            | -54.04% |     0.18 | 49.81%     | ok               |
| BITO       |       83 | -7.88%   | -64.27%            | -43.13% |     0.07 | 41.76%     | ok               |
| BLK        |       77 | -8.82%   | 39.61%             | -26.90% |    -0.16 | 47.09%     | ok               |
| BND        |       68 | -7.57%   | -0.46%             | -10.80% |    -1.14 | 36.11%     | ok               |
| BONK-USD   |       68 | 47.39%   | -84.29%            | -52.57% |     0.61 | 45.40%     | ok               |
| BTC-USD    |       75 | 9.59%    | -40.52%            | -25.52% |     0.3  | 53.07%     | ok               |
| C          |       79 | -37.30%  | 71.03%             | -39.84% |    -0.83 | 46.59%     | ok               |
| CAT        |       68 | 49.70%   | 55.74%             | -21.87% |     0.75 | 52.08%     | ok               |
| CL         |       60 | 8.35%    | 2.69%              | -14.32% |     0.31 | 40.27%     | ok               |
| CMCSA      |       84 | -35.01%  | -30.38%            | -45.76% |    -0.82 | 44.76%     | ok               |
| COMP-USD   |       93 | -36.76%  | -64.58%            | -52.17% |    -0.23 | 49.81%     | ok               |
| COP        |       66 | -15.39%  | 19.28%             | -38.80% |    -0.19 | 43.76%     | ok               |
| COST       |       60 | 4.58%    | 28.25%             | -31.32% |     0.21 | 41.10%     | ok               |
| CRM        |       69 | -16.65%  | -29.50%            | -39.41% |    -0.13 | 46.92%     | ok               |
| CRV-USD    |       62 | 108.80%  | -67.59%            | -39.49% |     0.96 | 37.74%     | ok               |
| CSCO       |       67 | 8.44%    | 91.71%             | -29.36% |     0.26 | 52.08%     | ok               |
| CVX        |       71 | -14.72%  | 32.93%             | -26.75% |    -0.31 | 43.93%     | ok               |
| DASH-USD   |       57 | -7.09%   | 83.82%             | -64.43% |     0.34 | 29.31%     | ok               |
| DBC        |       70 | -8.81%   | 24.45%             | -23.87% |    -0.23 | 36.94%     | ok               |
| DE         |       74 | -7.23%   | 66.94%             | -22.44% |    -0.06 | 44.93%     | ok               |
| DIA        |       72 | -9.91%   | 22.32%             | -16.20% |    -0.51 | 43.43%     | ok               |
| DIS        |       62 | -0.38%   | 20.40%             | -28.37% |     0.09 | 47.42%     | ok               |
| DOGE-USD   |       68 | -12.08%  | -65.73%            | -61.52% |     0.09 | 47.70%     | ok               |
| DOT-USD    |       78 | -55.30%  | -80.43%            | -67.17% |    -0.56 | 41.57%     | ok               |
| DXY-INDEX  |       40 | -0.61%   | -3.54%             | -5.13%  |    -0.09 | 31.17%     | ok               |
| EEM        |       68 | 1.07%    | 25.74%             | -24.14% |     0.1  | 42.60%     | ok               |
| EFA        |       64 | -9.07%   | 22.22%             | -12.63% |    -0.35 | 38.94%     | ok               |
| EOG        |       74 | -30.63%  | 17.33%             | -47.21% |    -0.65 | 44.26%     | ok               |
| ETC-USD    |       58 | 4.34%    | -63.97%            | -47.10% |     0.23 | 37.55%     | ok               |
| ETH-USD    |       63 | 145.19%  | -28.31%            | -30.11% |     1.28 | 49.04%     | ok               |
| EWJ        |       70 | -20.36%  | 21.16%             | -29.40% |    -0.64 | 38.77%     | ok               |
| FCX        |       67 | -4.50%   | -5.58%             | -46.84% |     0.1  | 46.59%     | ok               |
| FET-USD    |       79 | -31.21%  | -82.98%            | -66.52% |    -0.06 | 44.64%     | ok               |
| FIL-USD    |       61 | -4.58%   | -76.07%            | -58.54% |     0.18 | 39.46%     | ok               |
| FXI        |       48 | -0.79%   | 18.16%             | -23.91% |     0.06 | 30.78%     | ok               |
| GDX        |       68 | -4.93%   | 101.06%            | -34.29% |     0.07 | 45.26%     | ok               |
| GDXJ       |       70 | -30.10%  | 93.06%             | -36.01% |    -0.32 | 44.43%     | ok               |
| GE         |       80 | -16.33%  | 91.77%             | -28.69% |    -0.2  | 49.25%     | ok               |
| GLD        |       52 | 11.67%   | 49.78%             | -14.15% |     0.35 | 46.09%     | ok               |
| GOOGL      |       55 | 75.51%   | 43.21%             | -17.55% |     1.14 | 49.92%     | ok               |
| GRT-USD    |       71 | 63.78%   | -79.73%            | -38.70% |     0.73 | 45.21%     | ok               |
| GS         |       68 | -2.77%   | 69.82%             | -21.94% |     0.04 | 47.42%     | ok               |
| HBAR-USD   |       44 | -24.49%  | -49.21%            | -56.47% |    -0.28 | 42.24%     | ok               |
| HD         |       69 | 7.07%    | 1.22%              | -17.15% |     0.25 | 45.26%     | ok               |
| HON        |       87 | -27.89%  | 0.89%              | -32.93% |    -0.71 | 51.75%     | ok               |
| HYG        |       91 | -7.33%   | -0.78%             | -10.59% |    -0.82 | 39.43%     | ok               |
| IBIT       |       46 | 65.50%   | -13.13%            | -18.95% |     0.95 | 36.35%     | ok               |
| IBM        |       73 | -21.87%  | 26.59%             | -48.94% |    -0.23 | 50.42%     | ok               |
| ICP-USD    |       70 | 15.46%   | -59.09%            | -42.66% |     0.4  | 41.76%     | ok               |
| IEF        |       78 | -10.33%  | -1.47%             | -12.21% |    -1.35 | 35.61%     | ok               |
| IEMG       |       64 | 4.48%    | 22.12%             | -24.73% |     0.2  | 42.43%     | ok               |
| INJ-USD    |       56 | -2.07%   | -42.94%            | -56.80% |     0.23 | 38.51%     | ok               |
| INTC       |       72 | 77.00%   | 65.05%             | -60.60% |     0.71 | 50.58%     | ok               |
| INTU       |       73 | -9.41%   | -58.79%            | -37.44% |    -0.01 | 46.76%     | ok               |
| ITA        |       72 | 0.52%    | 49.78%             | -22.33% |     0.09 | 47.09%     | ok               |
| IWM        |       56 | 10.39%   | 27.11%             | -8.62%  |     0.42 | 34.44%     | ok               |
| JNJ        |       60 | 10.09%   | 85.22%             | -17.51% |     0.39 | 47.75%     | ok               |
| JPM        |       77 | -28.81%  | 48.70%             | -32.74% |    -0.85 | 44.93%     | ok               |
| KO         |       54 | 26.58%   | 53.59%             | -8.64%  |     0.89 | 40.27%     | ok               |
| LDO-USD    |       70 | 97.19%   | -67.03%            | -51.52% |     0.86 | 48.28%     | ok               |
| LIN        |       70 | -5.63%   | 16.91%             | -20.61% |    -0.13 | 42.43%     | ok               |
| LINK-USD   |       68 | 34.63%   | -28.86%            | -35.01% |     0.54 | 42.72%     | ok               |
| LLY        |       80 | -34.72%  | 48.57%             | -52.47% |    -0.54 | 49.42%     | ok               |
| LRCX       |       84 | -12.71%  | 70.83%             | -60.21% |     0.07 | 45.09%     | ok               |
| LTC-USD    |       67 | 53.32%   | -51.02%            | -29.62% |     0.72 | 52.11%     | ok               |
| MCD        |       77 | 6.36%    | 10.27%             | -22.20% |     0.27 | 41.43%     | ok               |
| META       |       72 | -33.01%  | 10.08%             | -44.90% |    -0.5  | 49.42%     | ok               |
| MPC        |       70 | 11.57%   | 110.86%            | -33.74% |     0.31 | 53.41%     | ok               |
| MRK        |       67 | -24.79%  | 4.70%              | -35.95% |    -0.48 | 43.59%     | ok               |
| MS         |       69 | -6.30%   | 66.25%             | -27.79% |    -0.06 | 47.25%     | ok               |
| MSFT       |       83 | -29.81%  | 5.50%              | -39.07% |    -0.68 | 50.08%     | ok               |
| MU         |       53 | 118.67%  | 348.38%            | -64.76% |     0.91 | 49.75%     | ok               |
| NEAR-USD   |       67 | 158.42%  | 45.29%             | -47.64% |     1.07 | 44.06%     | ok               |
| NEM        |       70 | -25.86%  | 127.00%            | -39.56% |    -0.25 | 49.75%     | ok               |
| NFLX       |       86 | -6.38%   | -16.52%            | -27.17% |    -0.03 | 50.25%     | ok               |
| NKE        |       91 | -42.79%  | -56.71%            | -55.35% |    -0.71 | 47.25%     | ok               |
| NOW        |       79 | -2.69%   | -44.84%            | -42.66% |     0.18 | 51.75%     | ok               |
| NVDA       |       82 | -20.26%  | -0.06%             | -47.95% |    -0.12 | 55.79%     | ok               |
| OP-USD     |       72 | -5.21%   | -86.82%            | -57.23% |     0.18 | 36.78%     | ok               |
| ORCL       |       60 | 57.76%   | -29.38%            | -31.06% |     0.65 | 49.58%     | ok               |
| OXY        |       65 | 9.27%    | -13.57%            | -28.48% |     0.27 | 43.43%     | ok               |
| PEP        |       70 | 0.90%    | -14.08%            | -21.35% |     0.1  | 46.26%     | ok               |
| PEPE-USD   |       74 | -31.23%  | -65.21%            | -60.19% |    -0.04 | 47.32%     | ok               |
| PFE        |       79 | -33.58%  | -1.55%             | -42.77% |    -1.02 | 37.60%     | ok               |
| PG         |       62 | -17.56%  | 3.34%              | -24.55% |    -0.59 | 37.77%     | ok               |
| PM         |       77 | -5.63%   | 81.12%             | -37.61% |    -0.03 | 47.75%     | ok               |
| POL-USD    |       83 | 5.68%    | -57.11%            | -46.25% |     0.27 | 47.51%     | ok               |
| QCOM       |       77 | -35.78%  | -25.09%            | -50.90% |    -0.37 | 40.10%     | ok               |
| QQQ        |       72 | 2.51%    | 24.94%             | -15.84% |     0.15 | 43.26%     | ok               |
| RENDER-USD |       88 | -51.20%  | -56.09%            | -56.24% |    -0.41 | 46.36%     | ok               |
| RTX        |       73 | 16.35%   | 89.39%             | -16.99% |     0.43 | 52.91%     | ok               |
| SBUX       |       64 | -12.97%  | 34.23%             | -29.22% |    -0.18 | 40.77%     | ok               |
| SCHW       |       84 | -16.47%  | 21.59%             | -31.92% |    -0.34 | 48.09%     | ok               |
| SHIB-USD   |       81 | -30.56%  | -67.94%            | -55.32% |    -0.25 | 51.34%     | ok               |
| SHY        |       54 | -1.90%   | 0.28%              | -3.30%  |    -0.63 | 38.94%     | ok               |
| SKY-USD    |       87 | -44.21%  | -46.58%            | -66.76% |    -0.5  | 45.98%     | ok               |
| SLB        |       76 | -38.36%  | -1.71%             | -55.19% |    -0.72 | 48.25%     | ok               |
| SLV        |       66 | 61.78%   | 37.08%             | -37.05% |     0.77 | 42.76%     | ok               |
| SMH        |       52 | 78.37%   | 51.75%             | -33.99% |     1.02 | 41.76%     | ok               |
| SNX-USD    |       62 | -14.09%  | -74.25%            | -50.74% |     0.04 | 36.02%     | ok               |
| SOL-USD    |       73 | 6.02%    | -48.51%            | -44.96% |     0.29 | 58.81%     | ok               |
| SOXX       |       58 | 80.39%   | 48.03%             | -40.14% |     0.98 | 41.10%     | ok               |
| SPY        |       63 | -6.02%   | 25.65%             | -15.53% |    -0.15 | 46.59%     | ok               |
| SUSHI-USD  |       89 | -58.18%  | -74.07%            | -78.32% |    -0.62 | 45.02%     | ok               |
| T          |       68 | 52.21%   | 18.54%             | -17.01% |     0.94 | 57.57%     | ok               |
| TGT        |       60 | -6.45%   | 14.06%             | -32.83% |    -0.05 | 38.10%     | ok               |
| TIA-USD    |       85 | -47.07%  | -78.60%            | -74.75% |    -0.23 | 44.25%     | ok               |
| TLT        |       68 | -22.68%  | -10.11%            | -23.31% |    -1.71 | 35.27%     | ok               |
| TMO        |       67 | 38.81%   | 25.40%             | -18.85% |     0.74 | 56.41%     | ok               |
| TMUS       |       74 | -8.48%   | -7.99%             | -33.05% |    -0.09 | 45.59%     | ok               |
| TRX-USD    |       58 | 6.30%    | 11.90%             | -26.48% |     0.26 | 49.62%     | ok               |
| TSLA       |       74 | -45.19%  | 49.54%             | -58.36% |    -0.41 | 41.43%     | ok               |
| TXN        |       83 | -30.18%  | 32.93%             | -46.56% |    -0.35 | 48.75%     | ok               |
| UNH        |       72 | 50.09%   | -31.79%            | -26.31% |     0.72 | 48.09%     | ok               |
| UNI-USD    |       80 | 13.16%   | -32.53%            | -60.31% |     0.39 | 50.77%     | ok               |
| UPS        |       71 | -37.92%  | -21.27%            | -41.37% |    -0.73 | 44.59%     | ok               |
| USO        |       73 | -18.94%  | 72.15%             | -45.90% |    -0.16 | 33.78%     | ok               |
| VEA        |       62 | -5.22%   | 28.34%             | -17.27% |    -0.17 | 41.93%     | ok               |
| VIXY       |      102 | -82.94%  | -36.95%            | -91.70% |    -1.08 | 32.11%     | ok               |
| VNQ        |       70 | -11.30%  | 11.04%             | -24.92% |    -0.42 | 40.60%     | ok               |
| VTI        |       67 | -12.32%  | 26.12%             | -17.64% |    -0.4  | 46.59%     | ok               |
| VWO        |       80 | -9.91%   | 14.99%             | -25.20% |    -0.3  | 41.76%     | ok               |
| VZ         |       86 | -27.73%  | 13.09%             | -31.67% |    -0.84 | 43.26%     | ok               |
| WFC        |       80 | -19.13%  | 28.95%             | -30.08% |    -0.33 | 46.76%     | ok               |
| WIF-USD    |       64 | 19.99%   | -83.75%            | -48.32% |     0.43 | 44.64%     | ok               |
| WMT        |       69 | 8.01%    | 87.97%             | -25.96% |     0.28 | 48.92%     | ok               |
| XBI        |       60 | 1.23%    | 53.44%             | -17.66% |     0.11 | 37.44%     | ok               |
| XLB        |       66 | -7.54%   | 10.99%             | -24.18% |    -0.21 | 35.11%     | ok               |
| XLC        |       61 | 3.60%    | 16.23%             | -12.33% |     0.18 | 48.25%     | ok               |
| XLE        |       72 | -3.79%   | 32.80%             | -34.77% |    -0.01 | 48.09%     | ok               |
| XLF        |       78 | -5.19%   | 30.93%             | -23.61% |    -0.12 | 49.75%     | ok               |
| XLI        |       82 | -12.77%  | 29.00%             | -18.27% |    -0.49 | 42.60%     | ok               |
| XLK        |       46 | 43.55%   | 30.09%             | -19.09% |     0.87 | 43.76%     | ok               |
| XLM-USD    |       75 | 2.46%    | -46.81%            | -56.32% |     0.25 | 49.62%     | ok               |
| XLP        |       63 | 12.97%   | 18.14%             | -8.96%  |     0.63 | 41.43%     | ok               |
| XLU        |       69 | -1.84%   | 25.52%             | -20.40% |    -0.03 | 41.43%     | ok               |
| XLV        |       74 | -21.00%  | 22.74%             | -22.82% |    -0.93 | 37.94%     | ok               |
| XLY        |       79 | -10.44%  | 20.55%             | -18.83% |    -0.25 | 47.42%     | ok               |
| XOM        |       59 | 3.19%    | 40.12%             | -20.29% |     0.16 | 37.10%     | ok               |
| XRP-USD    |       68 | -0.40%   | -55.60%            | -36.92% |     0.19 | 37.55%     | ok               |
| YFI-USD    |       76 | -39.41%  | -65.70%            | -53.02% |    -0.48 | 40.80%     | ok               |
| ZEC-USD    |       54 | 119.37%  | 1863.12%           | -56.50% |     0.85 | 36.78%     | ok               |

## AAPL Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -4.87%   | 55.52%             | -21.71% |     0.01 |       76 | 52.08%     | ok               |
|          15 | -9.08%   | 55.52%             | -23.86% |    -0.07 |       85 | 59.57%     | ok               |
|          30 | -10.47%  | 55.52%             | -20.65% |    -0.12 |       67 | 47.25%     | ok               |
|          35 | -11.76%  | 55.52%             | -22.04% |    -0.15 |       67 | 45.92%     | ok               |
|          25 | -14.09%  | 55.52%             | -22.37% |    -0.2  |       77 | 49.42%     | ok               |

## AAVE-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -6.03%   | -60.31%            | -45.38% |     0.16 |       49 | 35.06%     | ok               |
|          35 | -17.43%  | -60.31%            | -50.40% |     0.03 |       59 | 38.89%     | ok               |
|          45 | -17.46%  | -60.31%            | -51.44% |    -0.01 |       54 | 29.69%     | ok               |
|          50 | -15.07%  | -60.31%            | -47.89% |    -0.01 |       46 | 22.80%     | ok               |
|          15 | -41.15%  | -60.31%            | -64.61% |    -0.19 |       78 | 54.79%     | ok               |

## ABBV Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 2.91%    | 72.45%             | -21.96% |     0.16 |       50 | 36.61%     | ok               |
|          20 | -10.54%  | 72.45%             | -28.73% |    -0.14 |       62 | 52.75%     | ok               |
|          25 | -10.64%  | 72.45%             | -30.04% |    -0.15 |       65 | 51.25%     | ok               |
|          40 | -11.94%  | 72.45%             | -25.65% |    -0.22 |       68 | 42.26%     | ok               |
|          30 | -13.91%  | 72.45%             | -30.52% |    -0.24 |       66 | 49.42%     | ok               |

## ADA-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 27.69%   | -74.67%            | -46.50% |     0.49 |       68 | 64.18%     | ok               |
|          20 | 5.88%    | -74.67%            | -53.45% |     0.32 |       77 | 58.81%     | ok               |
|          35 | 7.24%    | -74.67%            | -44.07% |     0.3  |       62 | 44.25%     | ok               |
|          30 | -8.70%   | -74.67%            | -52.70% |     0.13 |       72 | 50.00%     | ok               |
|          25 | -12.64%  | -74.67%            | -59.89% |     0.12 |       67 | 54.60%     | ok               |

## ADBE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | 15.99%   | -61.65%            | -29.07% |     0.36 |       56 | 58.74%     | ok               |
|          20 | 0.79%    | -61.65%            | -31.52% |     0.16 |       62 | 61.73%     | ok               |
|          30 | -2.02%   | -61.65%            | -31.20% |     0.11 |       72 | 54.24%     | ok               |
|          15 | -7.23%   | -61.65%            | -34.98% |     0.04 |       65 | 63.89%     | ok               |
|          35 | -9.94%   | -61.65%            | -32.89% |    -0.04 |       77 | 46.09%     | ok               |

## AGG Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -7.03%   | -0.43%             | -10.37% |    -1.06 |       63 | 35.27%     | ok               |
|          45 | -6.63%   | -0.43%             | -9.07%  |    -1.2  |       60 | 24.63%     | ok               |
|          20 | -9.26%   | -0.43%             | -11.89% |    -1.29 |       70 | 40.77%     | ok               |
|          25 | -9.02%   | -0.43%             | -12.28% |    -1.31 |       71 | 38.60%     | ok               |
|          35 | -8.35%   | -0.43%             | -11.22% |    -1.32 |       66 | 31.95%     | ok               |

## ALGO-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -23.62%  | -53.51%            | -44.63% |    -0.06 |       84 | 45.02%     | ok               |
|          30 | -27.85%  | -53.51%            | -46.24% |    -0.14 |       82 | 40.80%     | ok               |
|          20 | -41.03%  | -53.51%            | -56.20% |    -0.31 |       83 | 48.08%     | ok               |
|          15 | -43.35%  | -53.51%            | -57.79% |    -0.33 |       88 | 53.26%     | ok               |
|          35 | -51.17%  | -53.51%            | -56.85% |    -0.66 |       70 | 35.44%     | ok               |

## AMAT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -23.78%  | 25.65%             | -54.01% |    -0.06 |       76 | 60.57%     | ok               |
|          30 | -29.84%  | 25.65%             | -57.08% |    -0.17 |       73 | 51.25%     | ok               |
|          35 | -32.19%  | 25.65%             | -55.13% |    -0.22 |       75 | 48.75%     | ok               |
|          20 | -39.36%  | 25.65%             | -60.13% |    -0.3  |       80 | 56.57%     | ok               |
|          25 | -39.92%  | 25.65%             | -59.69% |    -0.32 |       75 | 54.08%     | ok               |

## AMD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 39.99%   | 158.29%            | -37.12% |     0.56 |       52 | 31.61%     | ok               |
|          40 | 23.48%   | 158.29%            | -38.64% |     0.42 |       54 | 36.44%     | ok               |
|          35 | 13.24%   | 158.29%            | -40.22% |     0.34 |       62 | 37.94%     | ok               |
|          45 | 11.74%   | 158.29%            | -42.84% |     0.32 |       58 | 34.44%     | ok               |
|          30 | -3.80%   | 158.29%            | -47.20% |     0.19 |       65 | 40.60%     | ok               |

## AMGN Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -2.87%   | 40.18%             | -26.65% |     0.05 |       62 | 58.74%     | ok               |
|          35 | -5.42%   | 40.18%             | -31.29% |    -0.02 |       65 | 50.08%     | ok               |
|          30 | -7.74%   | 40.18%             | -34.19% |    -0.07 |       63 | 53.41%     | ok               |
|          25 | -9.64%   | 40.18%             | -33.47% |    -0.11 |       59 | 55.57%     | ok               |
|          50 | -6.90%   | 40.18%             | -24.68% |    -0.11 |       54 | 34.28%     | ok               |

## AMZN Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -34.58%  | 23.41%             | -34.72% |    -1.11 |       62 | 29.95%     | ok               |
|          50 | -35.60%  | 23.41%             | -35.58% |    -1.33 |       52 | 22.46%     | ok               |
|          45 | -41.89%  | 23.41%             | -41.87% |    -1.54 |       62 | 26.29%     | ok               |
|          35 | -56.39%  | 23.41%             | -56.38% |    -1.72 |       79 | 35.27%     | ok               |
|          30 | -59.18%  | 23.41%             | -59.16% |    -1.76 |       84 | 41.10%     | ok               |

## APT-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 75.56%   | -90.96%            | -25.96% |     1.07 |       44 | 17.43%     | ok               |
|          45 | 45.23%   | -90.96%            | -52.49% |     0.67 |       62 | 24.33%     | ok               |
|          20 | 27.74%   | -90.96%            | -56.22% |     0.5  |       84 | 52.49%     | ok               |
|          40 | 15.29%   | -90.96%            | -53.58% |     0.38 |       58 | 30.84%     | ok               |
|          15 | 1.52%    | -90.96%            | -58.22% |     0.31 |       79 | 58.81%     | ok               |

## ARB-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 90.09%   | -59.36%            | -35.56% |     0.85 |       58 | 26.63%     | ok               |
|          40 | 54.49%   | -59.36%            | -38.69% |     0.65 |       55 | 34.10%     | ok               |
|          35 | 48.83%   | -59.36%            | -37.63% |     0.61 |       69 | 38.12%     | ok               |
|          50 | 28.94%   | -59.36%            | -35.56% |     0.48 |       54 | 18.77%     | ok               |
|          15 | 18.59%   | -59.36%            | -57.12% |     0.44 |       97 | 57.66%     | ok               |

## ARKK Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -0.67%   | 43.28%             | -37.76% |     0.14 |       88 | 55.91%     | ok               |
|          20 | -11.75%  | 43.28%             | -35.06% |    -0.04 |       91 | 51.41%     | ok               |
|          30 | -19.29%  | 43.28%             | -38.67% |    -0.2  |       89 | 45.09%     | ok               |
|          35 | -27.89%  | 43.28%             | -43.49% |    -0.41 |       94 | 41.93%     | ok               |
|          25 | -30.92%  | 43.28%             | -47.50% |    -0.43 |       99 | 47.59%     | ok               |

## ATOM-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -41.49%  | -69.90%            | -56.71% |    -0.35 |       82 | 65.52%     | ok               |
|          20 | -48.93%  | -69.90%            | -60.19% |    -0.54 |       92 | 56.90%     | ok               |
|          25 | -47.59%  | -69.90%            | -54.88% |    -0.56 |       82 | 50.96%     | ok               |
|          45 | -49.56%  | -69.90%            | -53.91% |    -0.76 |       64 | 30.46%     | ok               |
|          50 | -40.68%  | -69.90%            | -40.73% |    -0.76 |       64 | 19.35%     | ok               |

## AVAX-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 35.22%   | -61.24%            | -22.06% |     0.64 |       38 | 17.24%     | ok               |
|          40 | 19.00%   | -61.24%            | -26.27% |     0.42 |       42 | 28.93%     | ok               |
|          45 | 17.66%   | -61.24%            | -26.35% |     0.4  |       38 | 24.52%     | ok               |
|          35 | 1.94%    | -61.24%            | -33.05% |     0.21 |       52 | 34.48%     | ok               |
|          15 | -23.29%  | -61.24%            | -43.71% |    -0.05 |       76 | 51.92%     | ok               |

## AVGO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -10.34%  | 83.66%             | -44.82% |     0.04 |       68 | 39.27%     | ok               |
|          25 | -11.38%  | 83.66%             | -45.43% |     0.03 |       72 | 42.10%     | ok               |
|          20 | -18.24%  | 83.66%             | -45.94% |    -0.04 |       81 | 45.92%     | ok               |
|          50 | -17.12%  | 83.66%             | -44.23% |    -0.08 |       62 | 27.12%     | ok               |
|          35 | -19.02%  | 83.66%             | -48.57% |    -0.09 |       78 | 36.44%     | ok               |

## BA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 45.30%   | -15.93%            | -18.09% |     0.77 |       66 | 50.08%     | ok               |
|          50 | 29.78%   | -15.93%            | -13.34% |     0.7  |       50 | 35.77%     | ok               |
|          25 | 40.30%   | -15.93%            | -26.02% |     0.68 |       64 | 56.74%     | ok               |
|          40 | 30.35%   | -15.93%            | -23.87% |     0.61 |       50 | 44.26%     | ok               |
|          30 | 29.45%   | -15.93%            | -24.47% |     0.55 |       63 | 53.41%     | ok               |

## BAC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 3.18%    | 14.93%             | -16.89% |     0.16 |       84 | 55.07%     | ok               |
|          35 | -0.35%   | 14.93%             | -23.35% |     0.06 |       70 | 44.26%     | ok               |
|          15 | -2.69%   | 14.93%             | -21.05% |     0.03 |       90 | 61.06%     | ok               |
|          45 | -1.37%   | 14.93%             | -16.06% |     0.02 |       56 | 34.44%     | ok               |
|          25 | -2.48%   | 14.93%             | -22.01% |     0.02 |       84 | 52.41%     | ok               |

## BCH-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 19.47%   | -57.83%            | -45.64% |     0.41 |       79 | 58.62%     | ok               |
|          20 | 16.37%   | -57.83%            | -45.52% |     0.38 |       74 | 55.36%     | ok               |
|          35 | 3.07%    | -57.83%            | -57.75% |     0.25 |       72 | 45.98%     | ok               |
|          25 | -0.09%   | -57.83%            | -48.42% |     0.22 |       78 | 51.72%     | ok               |
|          30 | -2.77%   | -57.83%            | -54.04% |     0.18 |       82 | 49.81%     | ok               |

## BITO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 9.13%    | -64.27%            | -31.98% |     0.27 |       54 | 24.79%     | ok               |
|          45 | 2.37%    | -64.27%            | -32.05% |     0.18 |       56 | 28.12%     | ok               |
|          30 | -7.88%   | -64.27%            | -43.13% |     0.07 |       83 | 41.76%     | ok               |
|          35 | -9.55%   | -64.27%            | -42.80% |     0.04 |       74 | 37.44%     | ok               |
|          40 | -9.26%   | -64.27%            | -40.13% |     0.03 |       68 | 32.78%     | ok               |

## BLK Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 0.53%    | 39.61%             | -20.79% |     0.09 |       84 | 43.59%     | ok               |
|          25 | -4.38%   | 39.61%             | -24.62% |    -0.03 |       73 | 49.58%     | ok               |
|          40 | -3.85%   | 39.61%             | -22.83% |    -0.04 |       76 | 39.10%     | ok               |
|          20 | -5.76%   | 39.61%             | -21.48% |    -0.06 |       80 | 51.91%     | ok               |
|          30 | -8.82%   | 39.61%             | -26.90% |    -0.16 |       77 | 47.09%     | ok               |

## BND Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -7.98%   | -0.46%             | -10.72% |    -1.12 |       65 | 41.93%     | ok               |
|          25 | -7.78%   | -0.46%             | -11.16% |    -1.12 |       70 | 39.77%     | ok               |
|          30 | -7.57%   | -0.46%             | -10.80% |    -1.14 |       68 | 36.11%     | ok               |
|          40 | -7.73%   | -0.46%             | -11.34% |    -1.28 |       60 | 29.95%     | ok               |
|          15 | -9.34%   | -0.46%             | -12.04% |    -1.3  |       77 | 44.26%     | ok               |

## BONK-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 162.97%  | -84.29%            | -23.92% |     1.31 |       40 | 18.39%     | ok               |
|          40 | 147.98%  | -84.29%            | -41.07% |     1.12 |       60 | 35.44%     | ok               |
|          45 | 114.18%  | -84.29%            | -31.97% |     1.02 |       64 | 24.90%     | ok               |
|          35 | 92.20%   | -84.29%            | -47.73% |     0.85 |       58 | 41.19%     | ok               |
|          15 | 60.74%   | -84.29%            | -56.51% |     0.67 |       65 | 60.92%     | ok               |

## BTC-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 66.68%   | -40.52%            | -21.12% |     1.1  |       58 | 42.72%     | ok               |
|          40 | 59.33%   | -40.52%            | -17.26% |     1.06 |       46 | 36.21%     | ok               |
|          45 | 50.75%   | -40.52%            | -12.58% |     0.99 |       38 | 31.42%     | ok               |
|          30 | 29.21%   | -40.52%            | -22.34% |     0.59 |       70 | 48.47%     | ok               |
|          50 | 19.58%   | -40.52%            | -20.16% |     0.52 |       36 | 25.29%     | ok               |

## C Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -15.04%  | 71.03%             | -22.98% |    -0.38 |       66 | 30.62%     | ok               |
|          45 | -24.68%  | 71.03%             | -30.69% |    -0.65 |       76 | 35.61%     | ok               |
|          40 | -29.42%  | 71.03%             | -35.05% |    -0.75 |       72 | 38.10%     | ok               |
|          25 | -36.37%  | 71.03%             | -37.53% |    -0.79 |       69 | 49.25%     | ok               |
|          20 | -38.36%  | 71.03%             | -39.30% |    -0.83 |       75 | 51.91%     | ok               |

## CAT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 64.42%   | 55.74%             | -21.99% |     0.86 |       69 | 62.23%     | ok               |
|          25 | 60.89%   | 55.74%             | -21.79% |     0.85 |       66 | 54.24%     | ok               |
|          30 | 49.70%   | 55.74%             | -21.87% |     0.75 |       68 | 52.08%     | ok               |
|          20 | 46.26%   | 55.74%             | -24.75% |     0.7  |       70 | 56.74%     | ok               |
|          35 | 41.30%   | 55.74%             | -25.22% |     0.67 |       68 | 45.92%     | ok               |

## CL Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 13.07%   | 2.69%              | -10.72% |     0.49 |       42 | 24.96%     | ok               |
|          45 | 8.77%    | 2.69%              | -10.96% |     0.35 |       44 | 28.12%     | ok               |
|          30 | 8.35%    | 2.69%              | -14.32% |     0.31 |       60 | 40.27%     | ok               |
|          35 | 4.03%    | 2.69%              | -15.39% |     0.19 |       60 | 36.44%     | ok               |
|          40 | 3.57%    | 2.69%              | -15.09% |     0.18 |       50 | 31.45%     | ok               |

## CMCSA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -17.43%  | -30.38%            | -27.57% |    -0.57 |       48 | 16.81%     | ok               |
|          45 | -22.75%  | -30.38%            | -34.36% |    -0.71 |       62 | 21.46%     | ok               |
|          15 | -35.43%  | -30.38%            | -43.40% |    -0.72 |       92 | 59.57%     | ok               |
|          40 | -30.66%  | -30.38%            | -41.83% |    -0.81 |       89 | 28.95%     | ok               |
|          30 | -35.01%  | -30.38%            | -45.76% |    -0.82 |       84 | 44.76%     | ok               |

## COMP-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -20.01%  | -64.58%            | -41.50% |    -0.14 |       46 | 20.31%     | ok               |
|          30 | -36.76%  | -64.58%            | -52.17% |    -0.23 |       93 | 49.81%     | ok               |
|          15 | -55.63%  | -64.58%            | -69.49% |    -0.48 |      101 | 68.39%     | ok               |
|          20 | -54.05%  | -64.58%            | -65.00% |    -0.5  |      104 | 63.79%     | ok               |
|          25 | -54.19%  | -64.58%            | -63.74% |    -0.53 |      102 | 58.05%     | ok               |

## COP Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -12.51%  | 19.28%             | -36.24% |    -0.18 |       50 | 31.11%     | ok               |
|          30 | -15.39%  | 19.28%             | -38.80% |    -0.19 |       66 | 43.76%     | ok               |
|          35 | -15.25%  | 19.28%             | -41.20% |    -0.19 |       67 | 40.93%     | ok               |
|          45 | -17.33%  | 19.28%             | -41.25% |    -0.28 |       60 | 34.61%     | ok               |
|          25 | -26.19%  | 19.28%             | -44.40% |    -0.42 |       77 | 46.92%     | ok               |

## COST Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 19.33%   | 28.25%             | -24.32% |     0.58 |       62 | 47.09%     | ok               |
|          25 | 15.88%   | 28.25%             | -24.93% |     0.51 |       59 | 44.26%     | ok               |
|          35 | 9.19%    | 28.25%             | -30.16% |     0.35 |       58 | 38.60%     | ok               |
|          30 | 4.58%    | 28.25%             | -31.32% |     0.21 |       60 | 41.10%     | ok               |
|          15 | 3.16%    | 28.25%             | -27.30% |     0.16 |       67 | 50.75%     | ok               |

## CRM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | -3.38%   | -29.50%            | -26.69% |     0.08 |       66 | 42.10%     | ok               |
|          40 | -7.00%   | -29.50%            | -32.67% |     0.01 |       72 | 37.94%     | ok               |
|          15 | -15.45%  | -29.50%            | -47.54% |    -0.07 |       94 | 58.24%     | ok               |
|          30 | -16.65%  | -29.50%            | -39.41% |    -0.13 |       69 | 46.92%     | ok               |
|          25 | -19.48%  | -29.50%            | -43.03% |    -0.18 |       70 | 49.08%     | ok               |

## CRV-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 138.26%  | -67.59%            | -37.68% |     1.11 |       60 | 33.72%     | ok               |
|          30 | 108.80%  | -67.59%            | -39.49% |     0.96 |       62 | 37.74%     | ok               |
|          40 | 97.77%   | -67.59%            | -38.45% |     0.93 |       54 | 30.08%     | ok               |
|          20 | 73.23%   | -67.59%            | -55.63% |     0.76 |       71 | 45.21%     | ok               |
|          45 | 63.71%   | -67.59%            | -41.91% |     0.76 |       56 | 23.18%     | ok               |

## CSCO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 35.59%   | 91.71%             | -22.62% |     0.7  |       54 | 42.10%     | ok               |
|          50 | 31.32%   | 91.71%             | -19.66% |     0.65 |       56 | 40.10%     | ok               |
|          40 | 18.65%   | 91.71%             | -28.70% |     0.43 |       58 | 45.26%     | ok               |
|          35 | 14.91%   | 91.71%             | -28.19% |     0.37 |       60 | 48.75%     | ok               |
|          20 | 14.54%   | 91.71%             | -29.33% |     0.36 |       73 | 55.07%     | ok               |

## CVX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -8.74%   | 32.93%             | -27.82% |    -0.17 |       63 | 35.94%     | ok               |
|          40 | -9.92%   | 32.93%             | -25.79% |    -0.19 |       73 | 39.60%     | ok               |
|          50 | -8.62%   | 32.93%             | -29.71% |    -0.2  |       56 | 31.45%     | ok               |
|          25 | -12.18%  | 32.93%             | -23.25% |    -0.23 |       75 | 46.76%     | ok               |
|          35 | -13.87%  | 32.93%             | -27.83% |    -0.29 |       69 | 41.43%     | ok               |

## DASH-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 105.07%  | 83.82%             | -43.46% |     0.83 |       42 | 17.62%     | ok               |
|          40 | 85.25%   | 83.82%             | -42.64% |     0.74 |       48 | 24.52%     | ok               |
|          45 | 54.11%   | 83.82%             | -46.93% |     0.61 |       46 | 20.88%     | ok               |
|          25 | -5.67%   | 83.82%             | -64.14% |     0.35 |       69 | 31.61%     | ok               |
|          30 | -7.09%   | 83.82%             | -64.43% |     0.34 |       57 | 29.31%     | ok               |

## DBC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 0.44%    | 24.45%             | -26.01% |     0.08 |       83 | 44.09%     | ok               |
|          20 | -5.76%   | 24.45%             | -25.45% |    -0.11 |       75 | 41.43%     | ok               |
|          25 | -5.94%   | 24.45%             | -24.61% |    -0.12 |       70 | 39.27%     | ok               |
|          30 | -8.81%   | 24.45%             | -23.87% |    -0.23 |       70 | 36.94%     | ok               |
|          50 | -9.25%   | 24.45%             | -18.84% |    -0.3  |       50 | 25.46%     | ok               |

## DE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -2.36%   | 66.94%             | -20.02% |     0.05 |       64 | 48.92%     | ok               |
|          50 | -1.33%   | 66.94%             | -17.97% |     0.04 |       58 | 30.95%     | ok               |
|          25 | -3.78%   | 66.94%             | -20.21% |     0.02 |       71 | 46.92%     | ok               |
|          45 | -3.67%   | 66.94%             | -18.05% |    -0    |       58 | 34.94%     | ok               |
|          30 | -7.23%   | 66.94%             | -22.44% |    -0.06 |       74 | 44.93%     | ok               |

## DIA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -7.83%   | 22.32%             | -13.58% |    -0.38 |       66 | 44.59%     | ok               |
|          20 | -9.93%   | 22.32%             | -15.48% |    -0.48 |       68 | 46.92%     | ok               |
|          35 | -9.51%   | 22.32%             | -16.94% |    -0.5  |       74 | 40.27%     | ok               |
|          30 | -9.91%   | 22.32%             | -16.20% |    -0.51 |       72 | 43.43%     | ok               |
|          40 | -12.08%  | 22.32%             | -18.41% |    -0.68 |       76 | 36.77%     | ok               |

## DIS Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 42.30%   | 20.40%             | -10.17% |     1.16 |       48 | 29.78%     | ok               |
|          40 | 12.86%   | 20.40%             | -18.75% |     0.37 |       61 | 37.94%     | ok               |
|          45 | 10.18%   | 20.40%             | -16.54% |     0.33 |       49 | 33.44%     | ok               |
|          15 | 4.64%    | 20.40%             | -32.73% |     0.2  |       79 | 57.07%     | ok               |
|          35 | 1.93%    | 20.40%             | -25.87% |     0.14 |       73 | 44.09%     | ok               |

## DOGE-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -8.12%   | -65.73%            | -60.29% |     0.17 |       81 | 62.45%     | ok               |
|          50 | -4.24%   | -65.73%            | -51.01% |     0.13 |       60 | 21.07%     | ok               |
|          20 | -12.89%  | -65.73%            | -60.01% |     0.1  |       79 | 56.90%     | ok               |
|          30 | -12.08%  | -65.73%            | -61.52% |     0.09 |       68 | 47.70%     | ok               |
|          25 | -15.18%  | -65.73%            | -60.53% |     0.06 |       72 | 52.49%     | ok               |

## DOT-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -32.10%  | -80.43%            | -46.40% |    -0.43 |       56 | 18.97%     | ok               |
|          35 | -48.07%  | -80.43%            | -58.07% |    -0.44 |       70 | 37.55%     | ok               |
|          40 | -38.76%  | -80.43%            | -50.22% |    -0.44 |       56 | 31.80%     | ok               |
|          20 | -54.55%  | -80.43%            | -70.04% |    -0.46 |       90 | 52.87%     | ok               |
|          15 | -61.27%  | -80.43%            | -76.85% |    -0.51 |       81 | 57.28%     | ok               |

## DXY-INDEX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -0.61%   | -3.54%             | -5.13%  |    -0.09 |       40 | 31.17%     | ok               |
|          40 | -2.55%   | -3.54%             | -6.15%  |    -0.35 |       66 | 46.75%     | ok               |
|          45 | -2.95%   | -3.54%             | -6.67%  |    -0.44 |       62 | 37.88%     | ok               |
|          30 | -3.82%   | -3.54%             | -8.65%  |    -0.46 |       76 | 56.93%     | ok               |
|          15 | -5.43%   | -3.54%             | -10.94% |    -0.53 |       97 | 72.94%     | ok               |

## EEM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 5.83%    | 25.74%             | -25.18% |     0.23 |       67 | 46.09%     | ok               |
|          25 | 4.68%    | 25.74%             | -23.69% |     0.2  |       67 | 44.43%     | ok               |
|          15 | 2.78%    | 25.74%             | -26.83% |     0.15 |       73 | 49.92%     | ok               |
|          30 | 1.07%    | 25.74%             | -24.14% |     0.1  |       68 | 42.60%     | ok               |
|          35 | -0.96%   | 25.74%             | -23.88% |     0.04 |       72 | 40.43%     | ok               |

## EFA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -0.91%   | 22.22%             | -10.10% |     0.03 |       60 | 49.08%     | ok               |
|          20 | -8.09%   | 22.22%             | -12.23% |    -0.28 |       67 | 46.26%     | ok               |
|          30 | -9.07%   | 22.22%             | -12.63% |    -0.35 |       64 | 38.94%     | ok               |
|          25 | -9.53%   | 22.22%             | -13.73% |    -0.36 |       68 | 42.60%     | ok               |
|          40 | -8.70%   | 22.22%             | -14.58% |    -0.37 |       58 | 34.28%     | ok               |

## EOG Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -13.50%  | 17.33%             | -34.41% |    -0.24 |       46 | 31.78%     | ok               |
|          40 | -17.55%  | 17.33%             | -36.18% |    -0.34 |       60 | 35.11%     | ok               |
|          50 | -21.05%  | 17.33%             | -35.63% |    -0.47 |       50 | 29.28%     | ok               |
|          35 | -23.39%  | 17.33%             | -38.93% |    -0.48 |       73 | 39.60%     | ok               |
|          30 | -30.63%  | 17.33%             | -47.21% |    -0.65 |       74 | 44.26%     | ok               |

## ETC-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 6.23%    | -63.97%            | -45.07% |     0.26 |       50 | 33.72%     | ok               |
|          30 | 4.34%    | -63.97%            | -47.10% |     0.23 |       58 | 37.55%     | ok               |
|          50 | 1.48%    | -63.97%            | -30.03% |     0.16 |       30 | 18.58%     | ok               |
|          45 | -3.86%   | -63.97%            | -32.70% |     0.08 |       36 | 22.22%     | ok               |
|          40 | -5.94%   | -63.97%            | -39.39% |     0.06 |       50 | 27.59%     | ok               |

## ETH-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 145.19%  | -28.31%            | -30.11% |     1.28 |       63 | 49.04%     | ok               |
|          30 | 105.95%  | -28.31%            | -32.89% |     1.03 |       65 | 56.90%     | ok               |
|          40 | 83.32%   | -28.31%            | -33.11% |     0.98 |       64 | 41.19%     | ok               |
|          25 | 81.27%   | -28.31%            | -40.90% |     0.88 |       63 | 60.73%     | ok               |
|          50 | 56.91%   | -28.31%            | -31.12% |     0.82 |       70 | 30.84%     | ok               |

## EWJ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -14.18%  | 21.16%             | -30.00% |    -0.37 |       58 | 41.26%     | ok               |
|          15 | -18.30%  | 21.16%             | -31.15% |    -0.48 |       69 | 44.59%     | ok               |
|          25 | -18.67%  | 21.16%             | -29.85% |    -0.54 |       62 | 40.10%     | ok               |
|          30 | -20.36%  | 21.16%             | -29.40% |    -0.64 |       70 | 38.77%     | ok               |
|          45 | -21.14%  | 21.16%             | -28.91% |    -0.78 |       66 | 30.12%     | ok               |

## FCX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 30.12%   | -5.58%             | -29.52% |     0.53 |       54 | 33.94%     | ok               |
|          50 | 22.76%   | -5.58%             | -26.57% |     0.45 |       58 | 30.12%     | ok               |
|          40 | 15.29%   | -5.58%             | -42.89% |     0.35 |       64 | 39.10%     | ok               |
|          30 | -4.50%   | -5.58%             | -46.84% |     0.1  |       67 | 46.59%     | ok               |
|          35 | -9.31%   | -5.58%             | -50.12% |     0.03 |       69 | 44.26%     | ok               |

## FET-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 38.05%   | -82.98%            | -59.58% |     0.55 |       69 | 59.20%     | ok               |
|          20 | -15.02%  | -82.98%            | -66.17% |     0.17 |       84 | 55.17%     | ok               |
|          25 | -22.64%  | -82.98%            | -65.31% |     0.07 |       83 | 49.23%     | ok               |
|          30 | -31.21%  | -82.98%            | -66.52% |    -0.06 |       79 | 44.64%     | ok               |
|          45 | -32.70%  | -82.98%            | -51.19% |    -0.3  |       54 | 22.99%     | ok               |

## FIL-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -4.58%   | -76.07%            | -58.54% |     0.18 |       61 | 39.46%     | ok               |
|          25 | -25.66%  | -76.07%            | -70.65% |    -0.04 |       68 | 43.30%     | ok               |
|          40 | -26.43%  | -76.07%            | -63.02% |    -0.14 |       52 | 31.23%     | ok               |
|          15 | -36.60%  | -76.07%            | -71.31% |    -0.14 |       87 | 52.49%     | ok               |
|          35 | -32.65%  | -76.07%            | -70.22% |    -0.21 |       62 | 34.67%     | ok               |

## FXI Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 3.20%    | 18.16%             | -21.68% |     0.16 |       51 | 35.44%     | ok               |
|          25 | 1.43%    | 18.16%             | -22.57% |     0.12 |       50 | 32.11%     | ok               |
|          20 | -0.06%   | 18.16%             | -24.53% |     0.08 |       48 | 33.44%     | ok               |
|          30 | -0.79%   | 18.16%             | -23.91% |     0.06 |       48 | 30.78%     | ok               |
|          35 | -5.06%   | 18.16%             | -27.53% |    -0.05 |       50 | 27.95%     | ok               |

## GDX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -1.32%   | 101.06%            | -30.00% |     0.14 |       82 | 51.41%     | ok               |
|          40 | -3.49%   | 101.06%            | -34.42% |     0.07 |       66 | 39.10%     | ok               |
|          30 | -4.93%   | 101.06%            | -34.29% |     0.07 |       68 | 45.26%     | ok               |
|          35 | -9.07%   | 101.06%            | -38.67% |    -0.01 |       74 | 41.76%     | ok               |
|          25 | -13.90%  | 101.06%            | -42.42% |    -0.07 |       72 | 47.09%     | ok               |

## GDXJ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -16.79%  | 93.06%             | -34.84% |    -0.05 |       72 | 51.58%     | ok               |
|          35 | -28.11%  | 93.06%             | -38.09% |    -0.29 |       70 | 41.76%     | ok               |
|          30 | -30.10%  | 93.06%             | -36.01% |    -0.32 |       70 | 44.43%     | ok               |
|          25 | -34.34%  | 93.06%             | -39.67% |    -0.37 |       75 | 47.59%     | ok               |
|          40 | -30.85%  | 93.06%             | -46.16% |    -0.38 |       64 | 39.27%     | ok               |

## GE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 1.03%    | 91.77%             | -21.25% |     0.12 |       62 | 34.61%     | ok               |
|          45 | -10.76%  | 91.77%             | -21.88% |    -0.13 |       74 | 37.60%     | ok               |
|          30 | -16.33%  | 91.77%             | -28.69% |    -0.2  |       80 | 49.25%     | ok               |
|          25 | -16.72%  | 91.77%             | -29.91% |    -0.21 |       76 | 51.08%     | ok               |
|          20 | -17.18%  | 91.77%             | -26.85% |    -0.21 |       76 | 53.74%     | ok               |

## GLD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | 21.05%   | 49.78%             | -13.87% |     0.54 |       48 | 47.59%     | ok               |
|          20 | 19.41%   | 49.78%             | -13.87% |     0.51 |       49 | 49.25%     | ok               |
|          30 | 11.67%   | 49.78%             | -14.15% |     0.35 |       52 | 46.09%     | ok               |
|          35 | 8.96%    | 49.78%             | -15.57% |     0.3  |       52 | 43.43%     | ok               |
|          15 | 9.21%    | 49.78%             | -18.05% |     0.29 |       53 | 52.58%     | ok               |

## GOOGL Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 78.23%   | 43.21%             | -17.38% |     1.19 |       59 | 46.09%     | ok               |
|          25 | 77.45%   | 43.21%             | -16.87% |     1.14 |       57 | 52.58%     | ok               |
|          30 | 75.51%   | 43.21%             | -17.55% |     1.14 |       55 | 49.92%     | ok               |
|          20 | 71.90%   | 43.21%             | -19.23% |     1.07 |       65 | 54.58%     | ok               |
|          15 | 72.07%   | 43.21%             | -15.62% |     1.04 |       68 | 59.07%     | ok               |

## GRT-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 90.89%   | -79.73%            | -36.70% |     0.84 |       70 | 61.88%     | ok               |
|          35 | 73.66%   | -79.73%            | -29.35% |     0.81 |       64 | 39.27%     | ok               |
|          30 | 63.78%   | -79.73%            | -38.70% |     0.73 |       71 | 45.21%     | ok               |
|          45 | 57.29%   | -79.73%            | -37.14% |     0.73 |       48 | 25.86%     | ok               |
|          20 | 65.80%   | -79.73%            | -37.63% |     0.73 |       82 | 54.98%     | ok               |

## GS Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 22.58%   | 69.82%             | -20.56% |     0.5  |       66 | 55.24%     | ok               |
|          40 | 7.27%    | 69.82%             | -16.16% |     0.25 |       64 | 40.93%     | ok               |
|          20 | 7.49%    | 69.82%             | -23.19% |     0.25 |       64 | 51.91%     | ok               |
|          25 | -0.60%   | 69.82%             | -23.32% |     0.09 |       66 | 49.92%     | ok               |
|          35 | -1.92%   | 69.82%             | -19.95% |     0.06 |       68 | 44.59%     | ok               |

## HBAR-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -22.20%  | -49.21%            | -58.64% |    -0.2  |       54 | 56.11%     | ok               |
|          30 | -24.49%  | -49.21%            | -56.47% |    -0.28 |       44 | 42.24%     | ok               |
|          45 | -23.84%  | -49.21%            | -49.09% |    -0.32 |       30 | 27.39%     | ok               |
|          40 | -25.49%  | -49.21%            | -51.16% |    -0.35 |       34 | 33.00%     | ok               |
|          20 | -30.76%  | -49.21%            | -63.19% |    -0.41 |       57 | 51.49%     | ok               |

## HD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 7.07%    | 1.22%              | -17.15% |     0.25 |       69 | 45.26%     | ok               |
|          25 | 5.30%    | 1.22%              | -16.67% |     0.21 |       68 | 47.59%     | ok               |
|          45 | 4.78%    | 1.22%              | -12.98% |     0.21 |       44 | 29.95%     | ok               |
|          35 | 4.89%    | 1.22%              | -16.37% |     0.2  |       70 | 40.43%     | ok               |
|          40 | 3.71%    | 1.22%              | -14.18% |     0.18 |       70 | 34.94%     | ok               |

## HON Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -11.01%  | 0.89%              | -20.43% |    -0.28 |       64 | 30.45%     | ok               |
|          45 | -14.63%  | 0.89%              | -22.88% |    -0.38 |       66 | 35.61%     | ok               |
|          35 | -26.77%  | 0.89%              | -31.30% |    -0.71 |       87 | 46.92%     | ok               |
|          30 | -27.89%  | 0.89%              | -32.93% |    -0.71 |       87 | 51.75%     | ok               |
|          40 | -26.97%  | 0.89%              | -31.84% |    -0.75 |       74 | 39.77%     | ok               |

## HYG Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -4.86%   | -0.78%             | -8.00%  |    -0.56 |       72 | 34.11%     | ok               |
|          45 | -6.62%   | -0.78%             | -9.14%  |    -0.8  |       72 | 30.45%     | ok               |
|          20 | -7.53%   | -0.78%             | -11.59% |    -0.81 |       96 | 45.42%     | ok               |
|          25 | -7.52%   | -0.78%             | -11.22% |    -0.81 |       91 | 42.76%     | ok               |
|          35 | -7.06%   | -0.78%             | -9.76%  |    -0.81 |       81 | 35.94%     | ok               |

## IBIT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 102.09%  | -13.13%            | -19.20% |     1.19 |       48 | 43.65%     | ok               |
|          50 | 68.96%   | -13.13%            | -17.37% |     1.09 |       28 | 25.00%     | ok               |
|          45 | 67.25%   | -13.13%            | -17.37% |     1.04 |       34 | 26.54%     | ok               |
|          30 | 65.50%   | -13.13%            | -18.95% |     0.95 |       46 | 36.35%     | ok               |
|          40 | 54.10%   | -13.13%            | -22.57% |     0.88 |       42 | 29.62%     | ok               |

## IBM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -15.77%  | 26.59%             | -49.43% |    -0.08 |       89 | 62.40%     | ok               |
|          35 | -20.20%  | 26.59%             | -47.10% |    -0.2  |       67 | 47.25%     | ok               |
|          30 | -21.87%  | 26.59%             | -48.94% |    -0.23 |       73 | 50.42%     | ok               |
|          20 | -27.85%  | 26.59%             | -53.45% |    -0.31 |       75 | 55.41%     | ok               |
|          25 | -32.79%  | 26.59%             | -55.45% |    -0.43 |       72 | 53.08%     | ok               |

## ICP-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 15.46%   | -59.09%            | -42.66% |     0.4  |       70 | 41.76%     | ok               |
|          35 | 3.04%    | -59.09%            | -49.65% |     0.28 |       68 | 36.59%     | ok               |
|          40 | -8.65%   | -59.09%            | -47.74% |     0.15 |       64 | 32.18%     | ok               |
|          20 | -26.75%  | -59.09%            | -63.83% |     0.07 |       81 | 49.23%     | ok               |
|          25 | -28.34%  | -59.09%            | -58.19% |     0.03 |       70 | 45.21%     | ok               |

## IEF Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -6.85%   | -1.47%             | -10.18% |    -0.78 |       74 | 43.93%     | ok               |
|          15 | -8.07%   | -1.47%             | -10.94% |    -0.91 |       73 | 45.59%     | ok               |
|          40 | -8.44%   | -1.47%             | -10.34% |    -1.22 |       68 | 26.96%     | ok               |
|          45 | -8.80%   | -1.47%             | -10.45% |    -1.32 |       64 | 24.29%     | ok               |
|          30 | -10.33%  | -1.47%             | -12.21% |    -1.35 |       78 | 35.61%     | ok               |

## IEMG Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | 8.00%    | 22.12%             | -23.73% |     0.3  |       63 | 44.76%     | ok               |
|          20 | 6.18%    | 22.12%             | -25.26% |     0.24 |       61 | 46.42%     | ok               |
|          30 | 4.48%    | 22.12%             | -24.73% |     0.2  |       64 | 42.43%     | ok               |
|          35 | 4.30%    | 22.12%             | -21.81% |     0.2  |       69 | 41.10%     | ok               |
|          40 | 1.55%    | 22.12%             | -18.43% |     0.11 |       68 | 38.60%     | ok               |

## INJ-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 33.68%   | -42.94%            | -42.48% |     0.53 |       52 | 35.63%     | ok               |
|          40 | 31.33%   | -42.94%            | -33.49% |     0.51 |       42 | 32.38%     | ok               |
|          45 | 17.42%   | -42.94%            | -37.55% |     0.39 |       48 | 25.86%     | ok               |
|          25 | 1.63%    | -42.94%            | -51.31% |     0.28 |       60 | 41.57%     | ok               |
|          15 | -0.59%   | -42.94%            | -60.14% |     0.27 |       69 | 46.55%     | ok               |

## INTC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 108.30%  | 65.05%             | -49.32% |     0.88 |       60 | 35.94%     | ok               |
|          50 | 101.83%  | 65.05%             | -48.35% |     0.86 |       64 | 32.11%     | ok               |
|          15 | 104.02%  | 65.05%             | -53.65% |     0.81 |       76 | 60.90%     | ok               |
|          20 | 92.66%   | 65.05%             | -52.47% |     0.77 |       82 | 57.40%     | ok               |
|          25 | 88.87%   | 65.05%             | -56.41% |     0.76 |       81 | 53.08%     | ok               |

## INTU Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 8.68%    | -58.79%            | -34.18% |     0.27 |       67 | 28.45%     | ok               |
|          35 | 4.58%    | -58.79%            | -41.63% |     0.2  |       69 | 40.77%     | ok               |
|          45 | 2.69%    | -58.79%            | -36.41% |     0.16 |       65 | 32.45%     | ok               |
|          40 | 1.05%    | -58.79%            | -38.72% |     0.14 |       69 | 35.94%     | ok               |
|          15 | -3.32%   | -58.79%            | -39.48% |     0.1  |       81 | 56.41%     | ok               |

## ITA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 0.31%    | 49.78%             | -26.15% |     0.1  |       73 | 59.40%     | ok               |
|          30 | 0.52%    | 49.78%             | -22.33% |     0.09 |       72 | 47.09%     | ok               |
|          50 | -0.54%   | 49.78%             | -21.48% |     0.05 |       68 | 34.78%     | ok               |
|          35 | -4.77%   | 49.78%             | -22.44% |    -0.07 |       72 | 43.43%     | ok               |
|          20 | -5.79%   | 49.78%             | -26.56% |    -0.07 |       72 | 53.74%     | ok               |

## IWM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd    |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:-------|---------:|---------:|:-----------|:-----------------|
|          25 | 17.32%   | 27.11%             | -8.02% |     0.64 |       52 | 35.77%     | ok               |
|          20 | 12.69%   | 27.11%             | -9.67% |     0.49 |       62 | 36.77%     | ok               |
|          30 | 10.39%   | 27.11%             | -8.62% |     0.42 |       56 | 34.44%     | ok               |
|          40 | 8.67%    | 27.11%             | -9.21% |     0.4  |       44 | 29.28%     | ok               |
|          35 | 8.33%    | 27.11%             | -9.25% |     0.36 |       52 | 31.95%     | ok               |

## JNJ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 17.00%   | 85.22%             | -10.97% |     0.67 |       44 | 36.61%     | ok               |
|          15 | 13.58%   | 85.22%             | -18.02% |     0.48 |       60 | 54.41%     | ok               |
|          30 | 10.09%   | 85.22%             | -17.51% |     0.39 |       60 | 47.75%     | ok               |
|          20 | 8.33%    | 85.22%             | -17.61% |     0.33 |       66 | 50.92%     | ok               |
|          45 | 6.99%    | 85.22%             | -13.35% |     0.31 |       50 | 40.27%     | ok               |

## JPM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 0.07%    | 48.70%             | -15.90% |     0.06 |       52 | 32.11%     | ok               |
|          45 | -10.24%  | 48.70%             | -21.91% |    -0.27 |       56 | 34.78%     | ok               |
|          20 | -27.14%  | 48.70%             | -35.58% |    -0.64 |       88 | 49.25%     | ok               |
|          40 | -22.56%  | 48.70%             | -28.47% |    -0.69 |       68 | 37.44%     | ok               |
|          35 | -25.11%  | 48.70%             | -29.39% |    -0.77 |       78 | 41.10%     | ok               |

## KO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 26.58%   | 53.59%             | -8.64%  |     0.89 |       54 | 40.27%     | ok               |
|          40 | 21.76%   | 53.59%             | -9.28%  |     0.79 |       58 | 35.77%     | ok               |
|          35 | 22.27%   | 53.59%             | -8.73%  |     0.77 |       58 | 38.77%     | ok               |
|          25 | 20.41%   | 53.59%             | -10.61% |     0.71 |       60 | 42.93%     | ok               |
|          50 | 8.82%    | 53.59%             | -16.13% |     0.39 |       44 | 29.95%     | ok               |

## LDO-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 183.99%  | -67.03%            | -43.72% |     1.13 |       78 | 60.92%     | ok               |
|          30 | 97.19%   | -67.03%            | -51.52% |     0.86 |       70 | 48.28%     | ok               |
|          20 | 96.41%   | -67.03%            | -45.80% |     0.84 |       81 | 55.36%     | ok               |
|          25 | 83.17%   | -67.03%            | -49.75% |     0.79 |       78 | 52.68%     | ok               |
|          35 | 36.37%   | -67.03%            | -58.29% |     0.54 |       82 | 41.00%     | ok               |

## LIN Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -2.38%   | 16.91%             | -22.01% |    -0.01 |       69 | 45.26%     | ok               |
|          20 | -3.14%   | 16.91%             | -23.00% |    -0.04 |       64 | 48.09%     | ok               |
|          15 | -5.01%   | 16.91%             | -23.68% |    -0.1  |       70 | 51.08%     | ok               |
|          45 | -3.83%   | 16.91%             | -17.04% |    -0.1  |       48 | 25.79%     | ok               |
|          30 | -5.63%   | 16.91%             | -20.61% |    -0.13 |       70 | 42.43%     | ok               |

## LINK-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 40.91%   | -28.86%            | -34.21% |     0.6  |       60 | 38.51%     | ok               |
|          30 | 34.63%   | -28.86%            | -35.01% |     0.54 |       68 | 42.72%     | ok               |
|          45 | 29.60%   | -28.86%            | -34.16% |     0.51 |       52 | 30.46%     | ok               |
|          40 | 28.37%   | -28.86%            | -36.88% |     0.5  |       52 | 33.52%     | ok               |
|          50 | 24.44%   | -28.86%            | -28.65% |     0.47 |       48 | 24.71%     | ok               |

## LLY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -1.23%   | 48.57%             | -38.23% |     0.09 |       50 | 35.11%     | ok               |
|          15 | -17.33%  | 48.57%             | -48.12% |    -0.13 |       70 | 60.23%     | ok               |
|          45 | -16.55%  | 48.57%             | -42.99% |    -0.2  |       60 | 39.10%     | ok               |
|          40 | -25.36%  | 48.57%             | -45.23% |    -0.36 |       70 | 42.26%     | ok               |
|          20 | -28.63%  | 48.57%             | -51.14% |    -0.37 |       77 | 55.24%     | ok               |

## LRCX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -5.36%   | 70.83%             | -56.69% |     0.18 |       82 | 54.08%     | ok               |
|          35 | -6.59%   | 70.83%             | -57.54% |     0.14 |       80 | 44.43%     | ok               |
|          20 | -11.62%  | 70.83%             | -62.08% |     0.1  |       85 | 49.75%     | ok               |
|          30 | -12.71%  | 70.83%             | -60.21% |     0.07 |       84 | 45.09%     | ok               |
|          40 | -12.68%  | 70.83%             | -55.33% |     0.06 |       74 | 42.26%     | ok               |

## LTC-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 51.51%   | -51.02%            | -33.55% |     0.73 |       64 | 45.59%     | ok               |
|          30 | 53.32%   | -51.02%            | -29.62% |     0.72 |       67 | 52.11%     | ok               |
|          25 | 52.60%   | -51.02%            | -32.65% |     0.71 |       67 | 54.60%     | ok               |
|          45 | 31.90%   | -51.02%            | -37.65% |     0.56 |       56 | 33.91%     | ok               |
|          20 | 25.09%   | -51.02%            | -45.05% |     0.47 |       66 | 58.05%     | ok               |

## MCD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 7.87%    | 10.27%             | -9.22%  |     0.38 |       50 | 26.12%     | ok               |
|          30 | 6.36%    | 10.27%             | -22.20% |     0.27 |       77 | 41.43%     | ok               |
|          35 | 4.91%    | 10.27%             | -16.97% |     0.24 |       69 | 38.60%     | ok               |
|          25 | 4.15%    | 10.27%             | -23.93% |     0.2  |       75 | 44.09%     | ok               |
|          20 | -0.10%   | 10.27%             | -24.58% |     0.06 |       77 | 47.25%     | ok               |

## META Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -18.38%  | 10.08%             | -37.54% |    -0.24 |       66 | 38.27%     | ok               |
|          40 | -22.61%  | 10.08%             | -40.90% |    -0.31 |       68 | 41.43%     | ok               |
|          50 | -22.87%  | 10.08%             | -39.33% |    -0.36 |       66 | 33.78%     | ok               |
|          30 | -33.01%  | 10.08%             | -44.90% |    -0.5  |       72 | 49.42%     | ok               |
|          35 | -33.63%  | 10.08%             | -41.40% |    -0.54 |       81 | 46.92%     | ok               |

## MPC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 20.28%   | 110.86%            | -18.24% |     0.45 |       52 | 41.43%     | ok               |
|          40 | 18.30%   | 110.86%            | -20.11% |     0.41 |       62 | 48.09%     | ok               |
|          35 | 17.46%   | 110.86%            | -30.41% |     0.39 |       68 | 50.75%     | ok               |
|          45 | 16.22%   | 110.86%            | -19.46% |     0.38 |       58 | 45.42%     | ok               |
|          30 | 11.57%   | 110.86%            | -33.74% |     0.31 |       70 | 53.41%     | ok               |

## MRK Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -15.21%  | 4.70%              | -28.39% |    -0.21 |       87 | 53.24%     | ok               |
|          25 | -15.36%  | 4.70%              | -31.07% |    -0.23 |       72 | 45.26%     | ok               |
|          20 | -19.51%  | 4.70%              | -29.34% |    -0.33 |       77 | 48.59%     | ok               |
|          50 | -16.04%  | 4.70%              | -23.01% |    -0.34 |       58 | 29.62%     | ok               |
|          45 | -18.12%  | 4.70%              | -25.38% |    -0.37 |       59 | 32.95%     | ok               |

## MS Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 0.68%    | 66.25%             | -19.99% |     0.1  |       64 | 38.27%     | ok               |
|          15 | -1.58%   | 66.25%             | -22.02% |     0.07 |       70 | 56.24%     | ok               |
|          20 | -3.77%   | 66.25%             | -25.68% |     0.01 |       69 | 52.08%     | ok               |
|          30 | -6.30%   | 66.25%             | -27.79% |    -0.06 |       69 | 47.25%     | ok               |
|          25 | -7.77%   | 66.25%             | -28.36% |    -0.1  |       67 | 49.42%     | ok               |

## MSFT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -17.48%  | 5.50%              | -24.64% |    -0.42 |       70 | 36.11%     | ok               |
|          50 | -20.83%  | 5.50%              | -25.48% |    -0.55 |       60 | 30.95%     | ok               |
|          35 | -26.77%  | 5.50%              | -35.38% |    -0.62 |       73 | 45.42%     | ok               |
|          40 | -26.56%  | 5.50%              | -34.92% |    -0.64 |       69 | 39.77%     | ok               |
|          30 | -29.81%  | 5.50%              | -39.07% |    -0.68 |       83 | 50.08%     | ok               |

## MU Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 141.78%  | 348.38%            | -61.12% |     1.01 |       60 | 45.26%     | ok               |
|          45 | 127.55%  | 348.38%            | -62.28% |     0.97 |       62 | 42.43%     | ok               |
|          15 | 136.51%  | 348.38%            | -61.96% |     0.92 |       58 | 58.07%     | ok               |
|          30 | 118.67%  | 348.38%            | -64.76% |     0.91 |       53 | 49.75%     | ok               |
|          35 | 112.62%  | 348.38%            | -65.13% |     0.89 |       65 | 47.42%     | ok               |

## NEAR-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 242.24%  | 45.29%             | -36.62% |     1.47 |       32 | 22.22%     | ok               |
|          40 | 260.70%  | 45.29%             | -36.30% |     1.41 |       44 | 32.95%     | ok               |
|          45 | 213.02%  | 45.29%             | -39.04% |     1.3  |       46 | 28.74%     | ok               |
|          30 | 158.42%  | 45.29%             | -47.64% |     1.07 |       67 | 44.06%     | ok               |
|          35 | 147.96%  | 45.29%             | -52.16% |     1.07 |       62 | 36.97%     | ok               |

## NEM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -4.57%   | 127.00%            | -30.50% |     0.1  |       71 | 54.08%     | ok               |
|          15 | -7.30%   | 127.00%            | -35.45% |     0.08 |       66 | 58.74%     | ok               |
|          50 | -12.79%  | 127.00%            | -33.24% |    -0.06 |       48 | 37.60%     | ok               |
|          25 | -19.14%  | 127.00%            | -39.51% |    -0.12 |       68 | 51.75%     | ok               |
|          30 | -25.86%  | 127.00%            | -39.56% |    -0.25 |       70 | 49.75%     | ok               |

## NFLX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 18.05%   | -16.52%            | -20.78% |     0.49 |       54 | 37.77%     | ok               |
|          50 | 15.43%   | -16.52%            | -16.28% |     0.46 |       44 | 29.45%     | ok               |
|          35 | 12.29%   | -16.52%            | -18.30% |     0.35 |       82 | 42.93%     | ok               |
|          15 | 6.16%    | -16.52%            | -26.59% |     0.23 |       76 | 63.56%     | ok               |
|          45 | 3.90%    | -16.52%            | -18.06% |     0.18 |       58 | 33.78%     | ok               |

## NKE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -23.43%  | -56.71%            | -33.81% |    -0.42 |       67 | 32.11%     | ok               |
|          25 | -35.59%  | -56.71%            | -51.20% |    -0.51 |       87 | 52.25%     | ok               |
|          35 | -29.30%  | -56.71%            | -42.13% |    -0.51 |       75 | 39.27%     | ok               |
|          20 | -37.51%  | -56.71%            | -49.69% |    -0.54 |       90 | 55.24%     | ok               |
|          15 | -42.92%  | -56.71%            | -56.07% |    -0.65 |       91 | 59.07%     | ok               |

## NOW Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -2.69%   | -44.84%            | -42.66% |     0.18 |       79 | 51.75%     | ok               |
|          20 | -3.50%   | -44.84%            | -49.77% |     0.18 |       73 | 57.57%     | ok               |
|          25 | -7.28%   | -44.84%            | -47.93% |     0.13 |       71 | 55.24%     | ok               |
|          15 | -11.78%  | -44.84%            | -52.56% |     0.09 |       83 | 60.40%     | ok               |
|          35 | -15.90%  | -44.84%            | -48.24% |     0    |       82 | 46.92%     | ok               |

## NVDA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -4.22%   | -0.06%             | -38.53% |     0.11 |       76 | 51.52%     | ok               |
|          25 | -11.00%  | -0.06%             | -44.52% |     0    |       81 | 47.59%     | ok               |
|          30 | -10.70%  | -0.06%             | -43.72% |    -0    |       82 | 44.74%     | ok               |
|          15 | -20.26%  | -0.06%             | -47.95% |    -0.12 |       82 | 55.79%     | ok               |
|          35 | -24.13%  | -0.06%             | -51.29% |    -0.25 |       92 | 41.89%     | ok               |

## OP-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 58.81%   | -86.82%            | -33.09% |     0.87 |       44 | 12.45%     | ok               |
|          45 | 69.32%   | -86.82%            | -30.78% |     0.85 |       46 | 18.20%     | ok               |
|          40 | 56.65%   | -86.82%            | -43.68% |     0.72 |       48 | 26.05%     | ok               |
|          35 | 6.98%    | -86.82%            | -56.85% |     0.29 |       58 | 31.03%     | ok               |
|          30 | -5.21%   | -86.82%            | -57.23% |     0.18 |       72 | 36.78%     | ok               |

## ORCL Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 124.90%  | -29.38%            | -37.59% |     0.97 |       67 | 59.23%     | ok               |
|          45 | 81.72%   | -29.38%            | -32.35% |     0.83 |       54 | 36.94%     | ok               |
|          25 | 80.82%   | -29.38%            | -31.06% |     0.77 |       59 | 51.75%     | ok               |
|          20 | 75.78%   | -29.38%            | -32.60% |     0.74 |       68 | 54.91%     | ok               |
|          35 | 72.26%   | -29.38%            | -31.95% |     0.74 |       60 | 45.92%     | ok               |

## OXY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 9.27%    | -13.57%            | -28.48% |     0.27 |       65 | 43.43%     | ok               |
|          35 | 7.43%    | -13.57%            | -26.37% |     0.25 |       70 | 38.60%     | ok               |
|          50 | 0.20%    | -13.57%            | -26.34% |     0.11 |       48 | 28.12%     | ok               |
|          40 | -1.21%   | -13.57%            | -28.30% |     0.09 |       58 | 35.11%     | ok               |
|          25 | -6.03%   | -13.57%            | -38.51% |     0.03 |       75 | 47.09%     | ok               |

## PEP Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 13.38%   | -14.08%            | -11.62% |     0.56 |       40 | 26.79%     | ok               |
|          45 | 2.07%    | -14.08%            | -14.22% |     0.13 |       54 | 30.62%     | ok               |
|          30 | 0.90%    | -14.08%            | -21.35% |     0.1  |       70 | 46.26%     | ok               |
|          35 | -0.67%   | -14.08%            | -21.42% |     0.05 |       73 | 40.60%     | ok               |
|          40 | -3.48%   | -14.08%            | -18.04% |    -0.07 |       68 | 35.94%     | ok               |

## PEPE-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -35.21%  | -65.21%            | -65.53% |     0.01 |       81 | 61.88%     | ok               |
|          30 | -31.23%  | -65.21%            | -60.19% |    -0.04 |       74 | 47.32%     | ok               |
|          20 | -36.66%  | -65.21%            | -63.48% |    -0.06 |       87 | 57.47%     | ok               |
|          35 | -37.45%  | -65.21%            | -60.83% |    -0.19 |       66 | 43.49%     | ok               |
|          25 | -48.70%  | -65.21%            | -64.37% |    -0.27 |       88 | 52.30%     | ok               |

## PFE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -15.07%  | -1.55%             | -25.81% |    -0.45 |       52 | 22.96%     | ok               |
|          50 | -14.14%  | -1.55%             | -27.79% |    -0.46 |       40 | 19.63%     | ok               |
|          40 | -18.08%  | -1.55%             | -30.60% |    -0.53 |       74 | 28.12%     | ok               |
|          35 | -25.97%  | -1.55%             | -36.12% |    -0.78 |       84 | 34.61%     | ok               |
|          30 | -33.58%  | -1.55%             | -42.77% |    -1.02 |       79 | 37.60%     | ok               |

## PG Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -6.12%   | 3.34%              | -20.08% |    -0.18 |       52 | 31.11%     | ok               |
|          35 | -9.32%   | 3.34%              | -18.99% |    -0.29 |       60 | 34.61%     | ok               |
|          45 | -14.08%  | 3.34%              | -22.00% |    -0.52 |       52 | 28.79%     | ok               |
|          30 | -17.56%  | 3.34%              | -24.55% |    -0.59 |       62 | 37.77%     | ok               |
|          25 | -19.44%  | 3.34%              | -25.84% |    -0.66 |       74 | 39.27%     | ok               |

## PM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | -2.57%   | 81.12%             | -34.56% |     0.03 |       82 | 44.26%     | ok               |
|          20 | -5.12%   | 81.12%             | -36.03% |    -0.02 |       81 | 52.91%     | ok               |
|          30 | -5.63%   | 81.12%             | -37.61% |    -0.03 |       77 | 47.75%     | ok               |
|          50 | -9.22%   | 81.12%             | -36.94% |    -0.16 |       66 | 35.44%     | ok               |
|          40 | -11.18%  | 81.12%             | -39.92% |    -0.2  |       76 | 40.60%     | ok               |

## POL-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 15.72%   | -57.11%            | -25.31% |     0.38 |       54 | 19.16%     | ok               |
|          45 | 11.18%   | -57.11%            | -30.67% |     0.32 |       54 | 26.63%     | ok               |
|          25 | 6.33%    | -57.11%            | -46.25% |     0.29 |       79 | 53.07%     | ok               |
|          30 | 5.68%    | -57.11%            | -46.25% |     0.27 |       83 | 47.51%     | ok               |
|          20 | 2.88%    | -57.11%            | -48.58% |     0.26 |       89 | 57.47%     | ok               |

## QCOM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -20.59%  | -25.09%            | -48.54% |    -0.09 |       71 | 41.93%     | ok               |
|          20 | -26.43%  | -25.09%            | -48.40% |    -0.18 |       67 | 45.26%     | ok               |
|          35 | -27.29%  | -25.09%            | -44.11% |    -0.23 |       79 | 37.60%     | ok               |
|          15 | -35.32%  | -25.09%            | -52.43% |    -0.31 |       69 | 47.92%     | ok               |
|          30 | -35.78%  | -25.09%            | -50.90% |    -0.37 |       77 | 40.10%     | ok               |

## QQQ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 13.67%   | 24.94%             | -17.16% |     0.38 |       73 | 52.41%     | ok               |
|          25 | 9.93%    | 24.94%             | -14.05% |     0.32 |       67 | 45.26%     | ok               |
|          20 | 8.61%    | 24.94%             | -14.88% |     0.29 |       79 | 48.42%     | ok               |
|          30 | 2.51%    | 24.94%             | -15.84% |     0.15 |       72 | 43.26%     | ok               |
|          35 | -10.71%  | 24.94%             | -20.59% |    -0.22 |       82 | 39.10%     | ok               |

## RENDER-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -9.32%   | -56.09%            | -44.12% |     0.22 |       90 | 62.45%     | ok               |
|          20 | -15.68%  | -56.09%            | -49.88% |     0.14 |       91 | 57.09%     | ok               |
|          25 | -17.64%  | -56.09%            | -49.67% |     0.11 |       85 | 52.11%     | ok               |
|          50 | -30.70%  | -56.09%            | -44.99% |    -0.39 |       58 | 17.05%     | ok               |
|          30 | -51.20%  | -56.09%            | -56.24% |    -0.41 |       88 | 46.36%     | ok               |

## RTX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 26.32%   | 89.39%             | -18.66% |     0.59 |       72 | 58.57%     | ok               |
|          25 | 23.72%   | 89.39%             | -18.59% |     0.55 |       64 | 55.91%     | ok               |
|          15 | 18.20%   | 89.39%             | -19.55% |     0.45 |       69 | 62.40%     | ok               |
|          50 | 13.31%   | 89.39%             | -18.42% |     0.43 |       62 | 39.77%     | ok               |
|          30 | 16.35%   | 89.39%             | -16.99% |     0.43 |       73 | 52.91%     | ok               |

## SBUX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | -0.52%   | 34.23%             | -25.43% |     0.08 |       58 | 34.11%     | ok               |
|          25 | -2.02%   | 34.23%             | -23.55% |     0.06 |       59 | 42.60%     | ok               |
|          45 | -2.46%   | 34.23%             | -27.26% |     0.03 |       62 | 29.45%     | ok               |
|          50 | -4.97%   | 34.23%             | -25.13% |    -0.04 |       50 | 24.96%     | ok               |
|          35 | -8.08%   | 34.23%             | -26.54% |    -0.08 |       64 | 37.60%     | ok               |

## SCHW Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | -2.00%   | 21.59%             | -29.24% |     0.05 |       73 | 52.75%     | ok               |
|          25 | -3.28%   | 21.59%             | -28.76% |     0.02 |       67 | 50.92%     | ok               |
|          45 | -3.45%   | 21.59%             | -16.53% |    -0.04 |       62 | 31.28%     | ok               |
|          50 | -3.90%   | 21.59%             | -13.28% |    -0.08 |       54 | 28.12%     | ok               |
|          15 | -8.71%   | 21.59%             | -31.37% |    -0.11 |       82 | 56.91%     | ok               |

## SHIB-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 0.64%    | -67.94%            | -27.01% |     0.15 |       50 | 19.35%     | ok               |
|          15 | -17.86%  | -67.94%            | -47.25% |    -0.01 |       85 | 65.71%     | ok               |
|          20 | -21.31%  | -67.94%            | -49.90% |    -0.07 |       78 | 61.11%     | ok               |
|          35 | -24.46%  | -67.94%            | -48.59% |    -0.17 |       77 | 44.83%     | ok               |
|          25 | -27.66%  | -67.94%            | -50.56% |    -0.18 |       78 | 57.66%     | ok               |

## SHY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd    |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:-------|---------:|---------:|:-----------|:-----------------|
|          30 | -1.90%   | 0.28%              | -3.30% |    -0.63 |       54 | 38.94%     | ok               |
|          40 | -2.13%   | 0.28%              | -3.58% |    -0.73 |       58 | 35.27%     | ok               |
|          35 | -2.43%   | 0.28%              | -3.61% |    -0.82 |       56 | 36.77%     | ok               |
|          45 | -2.20%   | 0.28%              | -3.43% |    -0.83 |       56 | 28.62%     | ok               |
|          50 | -2.20%   | 0.28%              | -3.40% |    -0.88 |       46 | 24.63%     | ok               |

## SKY-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -35.71%  | -46.58%            | -63.86% |    -0.26 |       76 | 57.09%     | ok               |
|          30 | -44.21%  | -46.58%            | -66.76% |    -0.5  |       87 | 45.98%     | ok               |
|          35 | -45.56%  | -46.58%            | -67.57% |    -0.58 |       78 | 37.74%     | ok               |
|          25 | -50.52%  | -46.58%            | -69.77% |    -0.62 |       80 | 49.23%     | ok               |
|          20 | -55.27%  | -46.58%            | -72.67% |    -0.69 |       82 | 52.87%     | ok               |

## SLB Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | -0.16%   | -1.71%             | -25.01% |     0.1  |       58 | 31.61%     | ok               |
|          40 | -1.18%   | -1.71%             | -26.80% |     0.08 |       52 | 34.44%     | ok               |
|          50 | -4.28%   | -1.71%             | -27.89% |    -0.01 |       46 | 24.96%     | ok               |
|          35 | -24.67%  | -1.71%             | -43.61% |    -0.42 |       74 | 42.26%     | ok               |
|          25 | -35.43%  | -1.71%             | -52.60% |    -0.63 |       85 | 52.08%     | ok               |

## SLV Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 76.57%   | 37.08%             | -28.72% |     0.93 |       54 | 31.78%     | ok               |
|          45 | 73.42%   | 37.08%             | -31.33% |     0.89 |       63 | 33.61%     | ok               |
|          40 | 72.05%   | 37.08%             | -34.28% |     0.88 |       67 | 35.61%     | ok               |
|          20 | 76.14%   | 37.08%             | -37.05% |     0.87 |       70 | 46.59%     | ok               |
|          15 | 73.19%   | 37.08%             | -47.98% |     0.81 |       71 | 51.25%     | ok               |

## SMH Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 102.61%  | 51.75%             | -31.01% |     1.18 |       49 | 44.76%     | ok               |
|          25 | 84.28%   | 51.75%             | -32.94% |     1.06 |       46 | 43.26%     | ok               |
|          30 | 78.37%   | 51.75%             | -33.99% |     1.02 |       52 | 41.76%     | ok               |
|          35 | 65.10%   | 51.75%             | -34.36% |     0.92 |       58 | 39.77%     | ok               |
|          45 | 52.67%   | 51.75%             | -33.18% |     0.83 |       56 | 34.28%     | ok               |

## SNX-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | 7.96%    | -74.25%            | -44.08% |     0.3  |       50 | 29.50%     | ok               |
|          40 | 5.18%    | -74.25%            | -29.01% |     0.24 |       48 | 25.10%     | ok               |
|          20 | -3.11%   | -74.25%            | -53.03% |     0.21 |       75 | 45.79%     | ok               |
|          15 | -18.12%  | -74.25%            | -54.74% |     0.05 |       76 | 50.19%     | ok               |
|          30 | -14.09%  | -74.25%            | -50.74% |     0.04 |       62 | 36.02%     | ok               |

## SOL-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 77.86%   | -48.51%            | -40.41% |     0.89 |       54 | 40.23%     | ok               |
|          45 | 39.31%   | -48.51%            | -47.42% |     0.62 |       52 | 33.72%     | ok               |
|          35 | 36.71%   | -48.51%            | -44.32% |     0.56 |       68 | 45.98%     | ok               |
|          25 | 17.67%   | -48.51%            | -39.39% |     0.4  |       67 | 56.32%     | ok               |
|          50 | 15.46%   | -48.51%            | -46.56% |     0.37 |       56 | 27.78%     | ok               |

## SOXX Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | 85.54%   | 48.03%             | -39.65% |     1.01 |       56 | 43.26%     | ok               |
|          35 | 78.63%   | 48.03%             | -38.43% |     0.98 |       58 | 38.77%     | ok               |
|          30 | 80.39%   | 48.03%             | -40.14% |     0.98 |       58 | 41.10%     | ok               |
|          20 | 71.53%   | 48.03%             | -38.67% |     0.89 |       61 | 44.09%     | ok               |
|          40 | 51.10%   | 48.03%             | -40.71% |     0.75 |       58 | 36.61%     | ok               |

## SPY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 3.04%    | 25.65%             | -14.25% |     0.16 |       62 | 50.25%     | ok               |
|          15 | 0.54%    | 25.65%             | -16.80% |     0.08 |       68 | 53.24%     | ok               |
|          25 | -1.19%   | 25.65%             | -14.25% |     0.02 |       60 | 49.08%     | ok               |
|          30 | -6.02%   | 25.65%             | -15.53% |    -0.15 |       63 | 46.59%     | ok               |
|          35 | -6.93%   | 25.65%             | -15.58% |    -0.2  |       61 | 43.43%     | ok               |

## SUSHI-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -27.09%  | -74.07%            | -39.73% |    -0.3  |       66 | 17.62%     | ok               |
|          35 | -39.99%  | -74.07%            | -70.89% |    -0.3  |       77 | 39.08%     | ok               |
|          45 | -33.52%  | -74.07%            | -59.95% |    -0.3  |       66 | 24.90%     | ok               |
|          40 | -37.19%  | -74.07%            | -63.59% |    -0.31 |       68 | 33.52%     | ok               |
|          15 | -60.07%  | -74.07%            | -79.47% |    -0.53 |       85 | 55.17%     | ok               |

## T Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | 62.97%   | 18.54%             | -17.66% |     1.06 |       66 | 59.57%     | ok               |
|          20 | 63.09%   | 18.54%             | -18.13% |     1.05 |       68 | 62.06%     | ok               |
|          15 | 63.74%   | 18.54%             | -15.08% |     1.03 |       73 | 66.72%     | ok               |
|          30 | 52.21%   | 18.54%             | -17.01% |     0.94 |       68 | 57.57%     | ok               |
|          35 | 34.31%   | 18.54%             | -14.49% |     0.71 |       76 | 52.91%     | ok               |

## TGT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -6.45%   | 14.06%             | -32.83% |    -0.05 |       60 | 38.10%     | ok               |
|          25 | -8.30%   | 14.06%             | -34.49% |    -0.08 |       68 | 41.10%     | ok               |
|          20 | -11.38%  | 14.06%             | -36.76% |    -0.12 |       86 | 45.59%     | ok               |
|          45 | -9.95%   | 14.06%             | -26.12% |    -0.17 |       50 | 29.62%     | ok               |
|          35 | -13.14%  | 14.06%             | -30.71% |    -0.23 |       60 | 34.44%     | ok               |

## TIA-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -35.98%  | -78.60%            | -66.94% |     0.02 |       93 | 60.54%     | ok               |
|          20 | -41.24%  | -78.60%            | -68.67% |    -0.09 |       87 | 54.60%     | ok               |
|          25 | -39.45%  | -78.60%            | -69.36% |    -0.09 |       90 | 49.43%     | ok               |
|          35 | -31.98%  | -78.60%            | -65.55% |    -0.1  |       76 | 37.93%     | ok               |
|          30 | -47.07%  | -78.60%            | -74.75% |    -0.23 |       85 | 44.25%     | ok               |

## TLT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -7.55%   | -10.11%            | -12.00% |    -0.82 |       32 | 16.97%     | ok               |
|          40 | -15.55%  | -10.11%            | -18.37% |    -1.35 |       50 | 26.12%     | ok               |
|          45 | -13.98%  | -10.11%            | -15.41% |    -1.43 |       44 | 20.97%     | ok               |
|          30 | -22.68%  | -10.11%            | -23.31% |    -1.71 |       68 | 35.27%     | ok               |
|          35 | -21.25%  | -10.11%            | -21.90% |    -1.76 |       66 | 30.45%     | ok               |

## TMO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 45.90%   | 25.40%             | -8.17%  |     0.99 |       50 | 35.11%     | ok               |
|          45 | 44.88%   | 25.40%             | -9.69%  |     0.93 |       54 | 40.10%     | ok               |
|          40 | 37.94%   | 25.40%             | -11.54% |     0.8  |       59 | 45.26%     | ok               |
|          35 | 40.76%   | 25.40%             | -13.84% |     0.79 |       67 | 50.58%     | ok               |
|          20 | 41.41%   | 25.40%             | -22.89% |     0.75 |       75 | 62.40%     | ok               |

## TMUS Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -8.13%   | -7.99%             | -41.04% |    -0.05 |       70 | 58.57%     | ok               |
|          30 | -8.48%   | -7.99%             | -33.05% |    -0.09 |       74 | 45.59%     | ok               |
|          25 | -11.08%  | -7.99%             | -39.29% |    -0.13 |       75 | 48.59%     | ok               |
|          20 | -12.58%  | -7.99%             | -39.79% |    -0.16 |       74 | 52.75%     | ok               |
|          50 | -10.15%  | -7.99%             | -32.38% |    -0.22 |       58 | 31.95%     | ok               |

## TRX-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 11.49%   | 11.90%             | -25.35% |     0.45 |       48 | 36.97%     | ok               |
|          50 | 10.87%   | 11.90%             | -21.45% |     0.44 |       46 | 34.48%     | ok               |
|          40 | 11.47%   | 11.90%             | -22.93% |     0.42 |       54 | 41.38%     | ok               |
|          35 | 7.90%    | 11.90%             | -24.93% |     0.31 |       60 | 47.70%     | ok               |
|          20 | 7.23%    | 11.90%             | -28.07% |     0.28 |       58 | 55.56%     | ok               |

## TSLA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 33.64%   | 49.54%             | -30.57% |     0.54 |       62 | 29.78%     | ok               |
|          40 | 0.52%    | 49.54%             | -50.11% |     0.2  |       61 | 34.78%     | ok               |
|          45 | -15.47%  | 49.54%             | -52.01% |     0    |       67 | 32.28%     | ok               |
|          35 | -32.60%  | 49.54%             | -58.86% |    -0.22 |       72 | 37.10%     | ok               |
|          25 | -43.90%  | 49.54%             | -54.86% |    -0.38 |       70 | 44.09%     | ok               |

## TXN Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -3.96%   | 32.93%             | -43.95% |     0.06 |       70 | 31.78%     | ok               |
|          35 | -17.67%  | 32.93%             | -42.08% |    -0.15 |       84 | 45.42%     | ok               |
|          20 | -23.53%  | 32.93%             | -37.19% |    -0.19 |       74 | 55.24%     | ok               |
|          15 | -25.27%  | 32.93%             | -38.02% |    -0.21 |       79 | 59.57%     | ok               |
|          40 | -22.70%  | 32.93%             | -44.52% |    -0.25 |       78 | 42.93%     | ok               |

## UNH Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 50.09%   | -31.79%            | -26.31% |     0.72 |       72 | 48.09%     | ok               |
|          35 | 45.31%   | -31.79%            | -27.21% |     0.68 |       67 | 43.09%     | ok               |
|          15 | 44.55%   | -31.79%            | -26.07% |     0.65 |       79 | 63.23%     | ok               |
|          20 | 41.92%   | -31.79%            | -26.96% |     0.63 |       74 | 56.91%     | ok               |
|          25 | 40.68%   | -31.79%            | -24.25% |     0.63 |       72 | 52.91%     | ok               |

## UNI-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 169.48%  | -32.53%            | -22.21% |     1.28 |       54 | 27.01%     | ok               |
|          45 | 149.37%  | -32.53%            | -30.27% |     1.14 |       58 | 34.67%     | ok               |
|          40 | 114.89%  | -32.53%            | -44.12% |     0.98 |       62 | 41.38%     | ok               |
|          35 | 87.21%   | -32.53%            | -48.64% |     0.83 |       62 | 46.17%     | ok               |
|          30 | 13.16%   | -32.53%            | -60.31% |     0.39 |       80 | 50.77%     | ok               |

## UPS Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -16.78%  | -21.27%            | -24.11% |    -0.31 |       44 | 25.29%     | ok               |
|          40 | -18.72%  | -21.27%            | -25.98% |    -0.31 |       60 | 34.78%     | ok               |
|          20 | -29.05%  | -21.27%            | -33.47% |    -0.47 |       78 | 51.41%     | ok               |
|          15 | -31.39%  | -21.27%            | -35.66% |    -0.52 |       80 | 54.91%     | ok               |
|          35 | -30.72%  | -21.27%            | -32.44% |    -0.57 |       67 | 38.94%     | ok               |

## USO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 3.00%    | 72.15%             | -39.48% |     0.2  |       67 | 42.60%     | ok               |
|          45 | 1.41%    | 72.15%             | -33.59% |     0.16 |       50 | 25.79%     | ok               |
|          20 | -1.06%   | 72.15%             | -44.17% |     0.14 |       74 | 38.60%     | ok               |
|          50 | -5.45%   | 72.15%             | -28.41% |     0.04 |       50 | 23.79%     | ok               |
|          25 | -11.97%  | 72.15%             | -45.29% |    -0.03 |       74 | 35.94%     | ok               |

## VEA Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 3.75%    | 28.34%             | -15.99% |     0.19 |       56 | 50.25%     | ok               |
|          20 | -0.56%   | 28.34%             | -17.04% |     0.03 |       59 | 47.59%     | ok               |
|          25 | -4.35%   | 28.34%             | -17.13% |    -0.12 |       57 | 45.59%     | ok               |
|          30 | -5.22%   | 28.34%             | -17.27% |    -0.17 |       62 | 41.93%     | ok               |
|          35 | -5.68%   | 28.34%             | -16.11% |    -0.19 |       50 | 39.60%     | ok               |

## VIXY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -49.74%  | -36.95%            | -70.53% |    -0.5  |       36 | 8.99%      | ok               |
|          45 | -59.51%  | -36.95%            | -75.03% |    -0.69 |       56 | 13.81%     | ok               |
|          40 | -69.68%  | -36.95%            | -81.61% |    -0.87 |       72 | 17.97%     | ok               |
|          35 | -77.76%  | -36.95%            | -85.57% |    -1.04 |       98 | 24.79%     | ok               |
|          30 | -82.94%  | -36.95%            | -91.70% |    -1.08 |      102 | 32.11%     | ok               |

## VNQ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -7.35%   | 11.04%             | -22.16% |    -0.24 |       68 | 43.59%     | ok               |
|          45 | -7.15%   | 11.04%             | -19.07% |    -0.29 |       58 | 28.29%     | ok               |
|          50 | -7.12%   | 11.04%             | -17.13% |    -0.3  |       48 | 25.12%     | ok               |
|          30 | -11.30%  | 11.04%             | -24.92% |    -0.42 |       70 | 40.60%     | ok               |
|          20 | -12.08%  | 11.04%             | -23.83% |    -0.43 |       73 | 46.26%     | ok               |

## VTI Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 5.24%    | 26.12%             | -13.96% |     0.23 |       63 | 50.58%     | ok               |
|          15 | -2.46%   | 26.12%             | -15.70% |    -0.01 |       64 | 53.41%     | ok               |
|          25 | -5.21%   | 26.12%             | -15.00% |    -0.12 |       57 | 48.59%     | ok               |
|          40 | -9.38%   | 26.12%             | -19.77% |    -0.32 |       70 | 38.94%     | ok               |
|          35 | -11.36%  | 26.12%             | -20.22% |    -0.39 |       64 | 43.26%     | ok               |

## VWO Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -2.33%   | 14.99%             | -24.01% |    -0.01 |       74 | 47.59%     | ok               |
|          20 | -2.36%   | 14.99%             | -26.14% |    -0.01 |       69 | 45.59%     | ok               |
|          45 | -4.27%   | 14.99%             | -23.75% |    -0.1  |       60 | 32.28%     | ok               |
|          40 | -4.56%   | 14.99%             | -23.57% |    -0.11 |       70 | 35.27%     | ok               |
|          50 | -8.54%   | 14.99%             | -21.68% |    -0.29 |       56 | 29.45%     | ok               |

## VZ Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -3.10%   | 13.09%             | -12.96% |    -0.04 |       56 | 28.62%     | ok               |
|          20 | -22.26%  | 13.09%             | -35.02% |    -0.43 |       80 | 52.75%     | ok               |
|          25 | -19.09%  | 13.09%             | -26.32% |    -0.47 |       83 | 47.75%     | ok               |
|          35 | -18.88%  | 13.09%             | -26.97% |    -0.55 |       64 | 39.10%     | ok               |
|          45 | -18.61%  | 13.09%             | -26.23% |    -0.57 |       72 | 32.95%     | ok               |

## WFC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          35 | -9.59%   | 28.95%             | -23.96% |    -0.14 |       73 | 43.26%     | ok               |
|          50 | -10.87%  | 28.95%             | -20.08% |    -0.29 |       58 | 32.45%     | ok               |
|          30 | -19.13%  | 28.95%             | -30.08% |    -0.33 |       80 | 46.76%     | ok               |
|          20 | -22.23%  | 28.95%             | -32.32% |    -0.35 |       80 | 52.91%     | ok               |
|          40 | -15.18%  | 28.95%             | -24.30% |    -0.38 |       68 | 39.93%     | ok               |

## WIF-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          20 | 78.79%   | -83.75%            | -40.67% |     0.76 |       67 | 51.34%     | ok               |
|          25 | 52.49%   | -83.75%            | -44.74% |     0.63 |       63 | 47.32%     | ok               |
|          15 | 39.72%   | -83.75%            | -46.21% |     0.56 |       77 | 54.60%     | ok               |
|          30 | 19.99%   | -83.75%            | -48.32% |     0.43 |       64 | 44.64%     | ok               |
|          35 | 11.81%   | -83.75%            | -52.54% |     0.35 |       62 | 38.51%     | ok               |

## WMT Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 37.97%   | 87.97%             | -12.87% |     1.1  |       36 | 35.77%     | ok               |
|          45 | 36.95%   | 87.97%             | -14.82% |     1.04 |       42 | 38.27%     | ok               |
|          35 | 28.66%   | 87.97%             | -18.90% |     0.8  |       58 | 45.42%     | ok               |
|          40 | 25.32%   | 87.97%             | -19.17% |     0.74 |       50 | 39.93%     | ok               |
|          15 | 10.32%   | 87.97%             | -26.82% |     0.31 |       82 | 59.73%     | ok               |

## XBI Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 13.91%   | 53.44%             | -16.08% |     0.42 |       50 | 33.28%     | ok               |
|          45 | 9.59%    | 53.44%             | -15.46% |     0.32 |       48 | 30.78%     | ok               |
|          35 | 3.38%    | 53.44%             | -17.66% |     0.17 |       58 | 35.94%     | ok               |
|          30 | 1.23%    | 53.44%             | -17.66% |     0.11 |       60 | 37.44%     | ok               |
|          50 | 0.20%    | 53.44%             | -15.41% |     0.08 |       48 | 27.95%     | ok               |

## XLB Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          40 | 5.08%    | 10.99%             | -17.29% |     0.24 |       56 | 29.45%     | ok               |
|          50 | 2.05%    | 10.99%             | -16.22% |     0.13 |       40 | 24.46%     | ok               |
|          35 | 1.02%    | 10.99%             | -20.65% |     0.1  |       56 | 32.78%     | ok               |
|          45 | -1.00%   | 10.99%             | -17.93% |     0.02 |       42 | 26.29%     | ok               |
|          25 | -4.02%   | 10.99%             | -21.62% |    -0.08 |       64 | 38.94%     | ok               |

## XLC Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | 3.60%    | 16.23%             | -12.33% |     0.18 |       61 | 48.25%     | ok               |
|          50 | 1.13%    | 16.23%             | -12.48% |     0.1  |       64 | 36.27%     | ok               |
|          25 | 0.23%    | 16.23%             | -12.31% |     0.07 |       64 | 50.75%     | ok               |
|          40 | -0.82%   | 16.23%             | -13.38% |     0.03 |       62 | 41.93%     | ok               |
|          35 | -1.49%   | 16.23%             | -13.38% |     0.01 |       60 | 45.76%     | ok               |

## XLE Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | -0.76%   | 32.80%             | -25.98% |     0.06 |       58 | 38.60%     | ok               |
|          45 | -2.44%   | 32.80%             | -28.46% |     0.01 |       60 | 41.10%     | ok               |
|          30 | -3.79%   | 32.80%             | -34.77% |    -0.01 |       72 | 48.09%     | ok               |
|          20 | -7.58%   | 32.80%             | -34.45% |    -0.08 |       81 | 53.41%     | ok               |
|          15 | -8.78%   | 32.80%             | -36.62% |    -0.11 |       97 | 57.40%     | ok               |

## XLF Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 3.22%    | 30.93%             | -20.19% |     0.17 |       70 | 57.57%     | ok               |
|          20 | 2.59%    | 30.93%             | -18.63% |     0.15 |       70 | 54.91%     | ok               |
|          25 | -4.57%   | 30.93%             | -23.22% |    -0.09 |       77 | 51.75%     | ok               |
|          30 | -5.19%   | 30.93%             | -23.61% |    -0.12 |       78 | 49.75%     | ok               |
|          35 | -12.96%  | 30.93%             | -24.48% |    -0.44 |       70 | 46.26%     | ok               |

## XLI Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 1.40%    | 29.00%             | -11.06% |     0.11 |       85 | 51.41%     | ok               |
|          20 | -3.75%   | 29.00%             | -12.74% |    -0.08 |       77 | 46.42%     | ok               |
|          45 | -9.28%   | 29.00%             | -16.29% |    -0.38 |       72 | 33.11%     | ok               |
|          25 | -12.21%  | 29.00%             | -17.60% |    -0.45 |       78 | 44.26%     | ok               |
|          40 | -11.35%  | 29.00%             | -14.16% |    -0.46 |       80 | 35.77%     | ok               |

## XLK Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 63.44%   | 30.09%             | -18.51% |     1.04 |       54 | 50.75%     | ok               |
|          25 | 52.69%   | 30.09%             | -15.06% |     0.98 |       46 | 45.09%     | ok               |
|          20 | 53.28%   | 30.09%             | -19.61% |     0.96 |       56 | 47.59%     | ok               |
|          30 | 43.55%   | 30.09%             | -19.09% |     0.87 |       46 | 43.76%     | ok               |
|          35 | 26.01%   | 30.09%             | -21.79% |     0.61 |       60 | 40.93%     | ok               |

## XLM-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | 18.98%   | -46.81%            | -61.51% |     0.41 |       72 | 61.11%     | ok               |
|          25 | 17.63%   | -46.81%            | -53.31% |     0.4  |       75 | 52.11%     | ok               |
|          45 | 13.45%   | -46.81%            | -49.94% |     0.35 |       60 | 28.74%     | ok               |
|          40 | 11.52%   | -46.81%            | -53.91% |     0.33 |       68 | 36.59%     | ok               |
|          30 | 2.46%    | -46.81%            | -56.32% |     0.25 |       75 | 49.62%     | ok               |

## XLP Threshold Sweep

|   threshold | return   | benchmark_return   | mdd    |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:-------|---------:|---------:|:-----------|:-----------------|
|          45 | 21.41%   | 18.14%             | -5.66% |     1.05 |       48 | 33.11%     | ok               |
|          50 | 18.55%   | 18.14%             | -6.08% |     0.94 |       54 | 31.28%     | ok               |
|          40 | 19.08%   | 18.14%             | -7.32% |     0.93 |       66 | 36.44%     | ok               |
|          35 | 16.34%   | 18.14%             | -8.39% |     0.79 |       62 | 39.60%     | ok               |
|          30 | 12.97%   | 18.14%             | -8.96% |     0.63 |       63 | 41.43%     | ok               |

## XLU Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          50 | 4.92%    | 25.52%             | -13.94% |     0.28 |       56 | 30.62%     | ok               |
|          45 | 3.77%    | 25.52%             | -14.88% |     0.23 |       60 | 31.78%     | ok               |
|          35 | 2.60%    | 25.52%             | -19.71% |     0.16 |       64 | 37.94%     | ok               |
|          40 | -0.17%   | 25.52%             | -16.41% |     0.03 |       72 | 34.44%     | ok               |
|          30 | -1.84%   | 25.52%             | -20.40% |    -0.03 |       69 | 41.43%     | ok               |

## XLV Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | -20.64%  | 22.74%             | -22.46% |    -0.9  |       74 | 39.60%     | ok               |
|          30 | -21.00%  | 22.74%             | -22.82% |    -0.93 |       74 | 37.94%     | ok               |
|          15 | -24.89%  | 22.74%             | -25.51% |    -1.08 |       81 | 43.76%     | ok               |
|          20 | -24.73%  | 22.74%             | -25.35% |    -1.09 |       77 | 41.26%     | ok               |
|          35 | -24.94%  | 22.74%             | -26.64% |    -1.19 |       68 | 34.94%     | ok               |

## XLY Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          15 | -5.49%   | 20.55%             | -16.52% |    -0.07 |       78 | 54.24%     | ok               |
|          20 | -10.49%  | 20.55%             | -20.14% |    -0.22 |       74 | 50.92%     | ok               |
|          30 | -10.44%  | 20.55%             | -18.83% |    -0.25 |       79 | 47.42%     | ok               |
|          25 | -14.08%  | 20.55%             | -21.39% |    -0.34 |       73 | 49.25%     | ok               |
|          50 | -10.79%  | 20.55%             | -17.00% |    -0.38 |       66 | 31.95%     | ok               |

## XOM Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          25 | 4.22%    | 40.12%             | -19.90% |     0.19 |       59 | 37.77%     | ok               |
|          50 | 3.48%    | 40.12%             | -21.35% |     0.17 |       40 | 29.28%     | ok               |
|          30 | 3.19%    | 40.12%             | -20.29% |     0.16 |       59 | 37.10%     | ok               |
|          45 | -1.68%   | 40.12%             | -23.33% |     0.03 |       44 | 30.45%     | ok               |
|          40 | -3.14%   | 40.12%             | -21.45% |    -0.01 |       54 | 33.78%     | ok               |

## XRP-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 7.43%    | -55.60%            | -32.85% |     0.28 |       58 | 31.61%     | ok               |
|          35 | 6.70%    | -55.60%            | -36.96% |     0.28 |       74 | 44.44%     | ok               |
|          20 | 0.90%    | -55.60%            | -37.30% |     0.22 |       72 | 55.94%     | ok               |
|          40 | -0.40%   | -55.60%            | -36.92% |     0.19 |       68 | 37.55%     | ok               |
|          15 | -6.63%   | -55.60%            | -38.27% |     0.14 |       73 | 59.58%     | ok               |

## YFI-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          30 | -39.41%  | -65.70%            | -53.02% |    -0.48 |       76 | 40.80%     | ok               |
|          25 | -42.90%  | -65.70%            | -55.74% |    -0.53 |       77 | 45.40%     | ok               |
|          35 | -42.23%  | -65.70%            | -49.99% |    -0.61 |       70 | 35.63%     | ok               |
|          15 | -53.80%  | -65.70%            | -65.43% |    -0.72 |       82 | 54.41%     | ok               |
|          40 | -44.54%  | -65.70%            | -49.44% |    -0.74 |       68 | 27.20%     | ok               |

## ZEC-USD Threshold Sweep

|   threshold | return   | benchmark_return   | mdd     |   sharpe |   trades | exposure   | skipped_reason   |
|------------:|:---------|:-------------------|:--------|---------:|---------:|:-----------|:-----------------|
|          45 | 237.18%  | 1863.12%           | -30.64% |     1.17 |       44 | 27.78%     | ok               |
|          35 | 153.92%  | 1863.12%           | -50.84% |     0.95 |       52 | 33.91%     | ok               |
|          40 | 143.31%  | 1863.12%           | -54.22% |     0.92 |       50 | 31.99%     | ok               |
|          50 | 133.15%  | 1863.12%           | -41.34% |     0.91 |       40 | 23.18%     | ok               |
|          30 | 119.37%  | 1863.12%           | -56.50% |     0.85 |       54 | 36.78%     | ok               |
